const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const files = ['screen.css', 'report-adapter.css', 'context-embed.css'];
const read = (f) => fs.readFileSync(path.join(__dirname, f), 'utf8');
const screen = read('screen.css');

function luminance(hex) {
  const v = hex.replace('#', '');
  const [r, g, b] = [0, 2, 4].map((i) => {
    const c = parseInt(v.slice(i, i + 2), 16) / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
function contrast(a, b) {
  const [l1, l2] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (l1 + 0.05) / (l2 + 0.05);
}

test('primary hover excludes disabled and keeps white text', () => {
  const m = screen.match(/(\.primary-action:hover[^{]*)\{([^}]*)\}/);
  assert.ok(m, 'no .primary-action:hover rule');
  assert.equal(m[1], '.primary-action:hover:not(:disabled)');
  assert.ok(m[2].includes('color:#fff'), `hover block lacks color:#fff: ${m[2]}`);
});

test('no text below 11px and no em/rem below 1', () => {
  const offenders = [];
  for (const f of files) {
    for (const m of read(f).matchAll(/font(?:-size)?:\s*(?:\d{3}\s+)?([\d.]+)(px|em|rem)/g)) {
      const v = parseFloat(m[1]);
      if ((m[2] === 'px' && v < 11) || (m[2] !== 'px' && v < 1)) offenders.push(`${f}: ${m[0]}`);
    }
  }
  assert.deepEqual(offenders, [], `undersized text: ${offenders.join('; ')}`);
});

test('type ramp tokens are declared and used', () => {
  for (const d of ['--fs-label:11px', '--fs-compact:12px', '--fs-body:13px', '--fs-control:14px']) {
    assert.ok(/:root\{[^}]*/.test(screen) && screen.split('}')[screen.split('}').findIndex((s) => s.includes(':root{'))].includes(d), `:root lacks ${d}`);
  }
  assert.doesNotMatch(screen, /font-size:1[1-4]px/);
  assert.doesNotMatch(screen, /font:(?:\d{3}\s+)?1[1-4]px/);
});

test('--text-quaternary contrast on white', () => {
  const m = screen.match(/--text-quaternary:(#[0-9a-fA-F]{6})/);
  assert.ok(m, 'token missing');
  const ratio = contrast(m[1], '#ffffff');
  assert.ok(ratio >= 5.5, `contrast ${ratio.toFixed(2)} < 5.5`);
  assert.equal(ratio.toFixed(2), '6.06');
});

test('report-adapter.css declares every --fs token it uses (injected without screen.css)', () => {
  const adapter = read('report-adapter.css');
  const brand = read('brand.css');
  const used = [...new Set(adapter.match(/var\(--fs-[a-z]+\)/g) || [])].map((v) => v.slice(4, -1));
  const block = (adapter.match(/\.library-report\s*\{[^}]*\}/) || [''])[0];
  const missing = used.filter((t) => !block.includes(`${t}:`) && !brand.includes(`${t}:`));
  assert.deepEqual(missing, [], `undeclared in the report document: ${missing.join(', ')}`);
});

const rule = (selector) => [...screen.matchAll(/([^{}]+)\{([^}]*)\}/g)].filter((m) => m[1].trim().split(',').map((x) => x.trim()).includes(selector)).map((m) => m[2]);

test('tools-workspace: the opened navigator takes a 238px column beside the content', () => {
  const found = [...screen.matchAll(/([^{}]*\.tools-workspace[^{}]*:has\(\.navigator\.mobile-open\)[^{}]*)\{([^}]*)\}/g)];
  assert.ok(found.some((m) => /grid-template-columns:\s*238px minmax\(0,\s*1fr\)\s*(;|$)/.test(m[2])), 'no two-column 238px rule');
});

test('tools-workspace: the Modules toggle spans every column', () => {
  assert.ok(rule('.tools-workspace .mobile-modules').some((b) => /grid-column:\s*1\/-1/.test(b)), 'toggle does not span');
});

test('border radii use only the DESIGN.md scale', () => {
  const allowed = new Set(['0', '1px', '50%', '999px', 'var(--radius-inline)', 'var(--radius-control)', 'var(--radius-card)']);
  const values = [...screen.matchAll(/border-radius:([^;}]*)/g)].flatMap((m) => m[1].trim().split(/\s+/));
  const bad = [...new Set(values.filter((v) => !allowed.has(v)))];
  assert.deepEqual(bad, []);
  assert.match(screen, /:root\{[^}]*--radius-inline:4px/);
});

test('forced colours keep pills, buttons and the active rail item visible; the case link does not wrap', () => {
  const block = /@media\(forced-colors:active\)\{(.*)\}\s*$/m.exec(screen);
  assert.ok(block, 'no forced-colors block');
  assert.ok(block[1].includes('.rail a[aria-current]') && block[1].includes('.badge'));
  assert.ok(rule('.issuer-meta a').some((b) => b.includes('white-space:nowrap')));
});

// Layout pass answer keys.
const mediaBlocks = (query) => [...screen.matchAll(/@media\(([^)]*)\)(?: and \(([^)]*)\))?\{/g)].filter((m) => query(m[1], m[2])).map((m) => {
  let depth = 1, i = m.index + m[0].length;
  const start = i;
  while (depth && i < screen.length) { depth += screen[i] === '{' ? 1 : screen[i] === '}' ? -1 : 0; i += 1; }
  return screen.slice(start, i - 1);
});

test('layout: an opened navigator keeps two columns at 1000px', () => {
  const blocks = mediaBlocks((a, b) => a === 'min-width:721px' && b === 'max-width:1050px');
  assert.ok(blocks.some((b) => /(^|[{};])\.workbench\.tools-workspace:has\(\.navigator\.mobile-open\)\{grid-template-columns:220px minmax\(0,1fr\)\}/.test(b)), 'no 220px two-column rule in 721-1050');
  assert.ok(blocks.some((b) => /(^|[{};])\.workbench\.tools-workspace\.has-evidence:has\(\.navigator\.mobile-open\)\{grid-template-columns:220px minmax\(0,1fr\)\}/.test(b)), 'no 220px two-column evidence rule in 721-1050');
});

test('layout: the tools Browse modules toggle is auto-width', () => {
  const found = rule('.tools-workspace .mobile-modules').join(';');
  assert.ok(found.includes('width:auto') && !found.includes('width:100%'), found);
});

test('layout: filters flex, headers stick, long names truncate, groups fit', () => {
  assert.ok(rule('.library-select').some((b) => b.includes('flex:1 1 140px')));
  assert.ok(rule('.case-list thead th').some((b) => b.includes('position:sticky')));
  assert.ok(rule('.issuer h1').some((b) => b.includes('text-overflow:ellipsis')));
  assert.ok(rule('.question-map>section>div').some((b) => b.includes('auto-fit')));
});

test('layout: controls reach 32px', () => {
  for (const s of ['.output-select select', '#report-select', '.module-catalogue>summary', '.issuer-meta a', '#section-nav select', '#section-nav button']) {
    assert.ok(rule(s).some((b) => /(^|;)(min-)?height:32px/.test(b)), `${s} under 32px`);
  }
});

test('content table cards are bounded and keep their header in view', () => {
  const card = screen.match(/(?:^|[}\n])\.table-scroll\{([^}]*)\}/);
  assert.ok(card, 'no .table-scroll rule');
  assert.ok(card[1].includes('max-height:70vh'), card[1]);
  assert.ok(card[1].includes('overflow:auto'), card[1]);
  const head = screen.match(/\.table-scroll thead th\{([^}]*)\}/);
  assert.ok(head, 'no .table-scroll thead th rule');
  assert.ok(head[1].includes('position:sticky') && head[1].includes('top:0'), head[1]);
  assert.ok(head[1].includes('background:var(--gray-50)'), head[1]);
  assert.match(screen, /\.case-list thead th\{[^}]*position:sticky;top:var\(--band-h,101px\)/);
});

test('the section bar is sticky with its run and module prefix at 720px and below', () => {
  assert.match(screen, /\.section-context\{display:none\}/);
  const media = [...screen.matchAll(/@media\(max-width:720px\)\{(.*)/g)].map((m) => m[1]).join('\n');
  const bar = media.match(/#section-nav\{[^}]*position:sticky[^}]*\}/);
  assert.ok(bar, 'no sticky #section-nav at 720px');
  assert.ok(bar[0].includes('top:0') && bar[0].includes('background:#fff') && bar[0].includes('border-bottom:1px solid var(--rule)'), bar[0]);
  assert.match(media, /#section-nav \.section-context\{display:block/);
});

test('the rail opens as an overlay, for focus too, and stops animating under reduced motion', () => {
  const open = screen.match(/\.rail\.rail-open[^{}]*\{[^}]*\}/g) || [];
  assert.ok(open.some((r) => r.includes('width:220px')), 'open rail is 220px wide');
  assert.ok(!/\.app\{[^}]*margin-left:220px/.test(screen), 'the page does not reflow');
  assert.ok(!screen.includes('.rail:focus-within'), 'a mouse click must not leave the rail open');
  const covered = screen.split('\n').filter((l) => /^\.rail\.rail-open/.test(l));
  assert.ok(covered.length >= 4);
  for (const l of covered) for (const sel of l.slice(0, l.indexOf('{')).split(',').filter((x) => x.includes('.rail-open'))) {
    assert.ok(l.slice(0, l.indexOf('{')).includes(sel.replace('.rail-open', ':has(:focus-visible)')), `keyboard focus mirrors ${sel}`);
  }
  assert.match(screen, /\.rail:not\(\.rail-open\)[^{]*\.rail-label|\.rail-label\{[^}]*clip:rect\(0,0,0,0\)/, 'labels are clipped at rest');
  assert.ok(!/\.rail-label\{[^}]*display:none/.test(screen), 'labels keep their accessible name');
  const reduced = [...screen.matchAll(/@media\(prefers-reduced-motion:reduce\)\{(.*)\}/g)].map((m) => m[1]).join('');
  assert.match(reduced, /\.rail\{[^}]*transition:none/);
  assert.match(screen, /\.rail\{[^}]*transition:width/);
});

test('at 720px and below the section bar outranks every sticky table cell and cash flow row labels are capped', () => {
  const mobile = screen.slice(screen.lastIndexOf('@media(max-width:720px){#section-nav{z-index:5}'));
  assert.ok(mobile.startsWith('@media(max-width:720px){#section-nav{z-index:5}'), 'no section bar z-index rule');
  const bar = Number(mobile.match(/#section-nav\{z-index:(\d+)\}/)[1]);
  const cells = [...screen.matchAll(/position:sticky[^}]*z-index:(\d+)/g)].map((m) => Number(m[1]));
  assert.ok(cells.length > 0);
  assert.ok(cells.every((z) => z < bar), `a sticky cell reaches ${Math.max(...cells)}, bar is ${bar}`);
  assert.match(mobile, /\.cashflow tbody th\[scope=row\]\{[^}]*white-space:normal[^}]*min-width:12rem[^}]*max-width:12rem/);
});

test('every custom property screen.css reads without a fallback is defined in screen.css', () => {
  // index.html loads screen.css alone, so a token from another stylesheet (such as the report's
  // --rb-ink-2) would silently fall back to the inherited colour. --band-h has a fallback (set by JS).
  const defined = new Set([...screen.matchAll(/(--[\w-]+)\s*:/g)].map((m) => m[1]));
  const bare = [...screen.matchAll(/var\((--[\w-]+)\)/g)].map((m) => m[1]);
  assert.deepEqual([...new Set(bare.filter((name) => !defined.has(name)))], []);
  assert.match(screen, /\.ref\{[^}]*color:var\(--muted\)/);
});

test('the amber run mark glyph and the amber strip text hold 4.5:1 on their backgrounds', () => {
  const token = (name) => screen.match(new RegExp(`--${name}:(#[0-9a-f]{6})`, 'i'))[1];
  const mark = screen.match(/\.run-mark\[data-state=stopped\]\{background:var\(--([a-z-]+)\);color:var\(--([a-z-]+)\)/);
  assert.ok(mark, 'amber mark rule');
  assert.ok(contrast(token(mark[2]), token(mark[1])) >= 4.5, `${mark[2]} on ${mark[1]}`);
  assert.ok(contrast(token('amber'), token('amber-bg')) >= 4.5);
});

test('cash flow rows are 32px, row labels hold 12rem, column groups are ruled and scenarios sit on --quiet', () => {
  const cell = screen.match(/\.cashflow tbody th,\.cashflow tbody td\{([^}]*)\}/);
  assert.ok(cell, 'no cash flow cell rule');
  assert.match(cell[1], /height:32px/);
  // 5px above and below a 20px line leaves the 1px rule inside the 32px row.
  assert.match(cell[1], /padding-top:5px/);assert.match(cell[1], /padding-bottom:5px/);assert.match(cell[1], /line-height:20px/);
  const label = screen.match(/\.cashflow tbody th\[scope=row\]\{([^}]*min-width:12rem[^}]*)\}/);
  assert.ok(label, 'row labels have no 12rem minimum');
  assert.match(label[1], /white-space:normal/);
  assert.doesNotMatch(screen, /\.cashflow[^{]*\{[^}]*text-overflow:ellipsis/);
  assert.match(screen, /\.cashflow \.group-start\{border-left:1px solid var\(--rule\)\}/);
  assert.match(screen, /\.cashflow td\.scenario\{background:var\(--quiet\)\}/);
});

test('the published model disclosure and the cash flow region are styled as a quiet disclosure', () => {
  assert.match(screen, /\.model-original>summary\{[^}]*cursor:pointer[^}]*min-height:32px/);
});

test('the run strip uses the card radius, a wide supporting line and 24px action targets', () => {
  const rule = (selector) => screen.match(new RegExp(`(?:^|\\})${selector.replace(/[.[\]]/g, '\\$&')}\\{([^}]*)\\}`, 'm'))?.[1] ?? '';
  assert.match(rule('.run-strip'), /border-radius:var\(--radius-card\)/);
  assert.match(rule('.strip-text'), /max-width:120ch/);
  assert.match(rule('.strip-actions a'), /min-height:24px/);
});
