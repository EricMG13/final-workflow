/* Chart renderers escape handoff values and output ids. Plain node (no jsdom): functions are lifted from the
   real source files into a bare vm context. Synthetic markup only; no network or provider. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const read=name=>fs.readFileSync(path.join(__dirname,name),'utf8');
const grab=(source,name)=>{const m=source.match(new RegExp(`^function ${name}\\([^)]*\\) \\{[\\s\\S]*?\\n\\}`,'m'));assert.ok(m,name);return m[0];};
const line=(source,start)=>{const m=source.match(new RegExp(`^const ${start}.*$`,'m'));assert.ok(m,start);return m[0];};
const screen=read('screen.js'),views=read('views.js');
const sandbox=(...parts)=>{const context=vm.createContext({});vm.runInContext(parts.join('\n'),context);return context;};
const basics=[line(screen,'esc '),line(screen,'plain '),line(screen,'rich ')];
const MARK='<img src=q onerror=1>',ENTITY='&lt;5';

test('the pinned CP-1 bar chart escapes the cell value, the period label and the evidence key',()=>{
  const context=sandbox(...basics,grab(screen,'trendChart'),`
    var data={'CP-1':{basis:{unit:'USD m'}}};
    var findRow=()=>({table:{headers:['','${MARK}A','${MARK}B','${ENTITY}','']},row:{cells:['Net sales','${MARK}1','2','${ENTITY}','note']},key:'x"><b>:7'});
    var sourceFooter=()=>'';`);
  const html=vm.runInContext("trendChart('CP-1','Net sales')",context);
  assert.ok(!html.includes('<img'),html);
  assert.ok(!html.includes('"><b>'),html);
  // An entity is shown as typed: the figure beside the exact table cell is the same text.
  assert.match(html,/<span class="bar-value">&amp;lt;5<\/span>/);
  assert.match(html,/<span class="bar-period">&amp;lt;5<\/span>/);
});

test('a chart row built on an output id with markup in its file name stays one attribute',()=>{
  const id='shared-run/CP-1"><img src=x onerror=1>.md';
  const context=sandbox(...basics,grab(views,'chartNumber'),grab(views,'chartIntro'),grab(views,'comparisonChart'),`
    var sourceFooter=()=>'';
    var table={headers:['Item','Value'],rows:[{line:9,cells:['Revenue','5']}]};
    var fixtureTable=()=>table;
    var data={};data[${JSON.stringify(id)}]={module:'CP-1'};`);
  const html=vm.runInContext(`comparisonChart(${JSON.stringify(id)},{kind:'bars',title:'T',table:1,column:1})`,context);
  assert.ok(!html.includes('<img'),html);
  assert.match(html,/data-evidence="shared-run\/CP-1&quot;&gt;&lt;img src=x onerror=1&gt;\.md:9"/);
});

test('no web script writes an evidence key into an attribute without escaping it',()=>{
  for(const name of ['screen.js','views.js','actions.js']){
    const raw=[...read(name).matchAll(/data-evidence="\$\{(?!esc\()/g)];
    assert.equal(raw.length,0,`${name} has ${raw.length} unescaped data-evidence`);
  }
});

// routeHref's signature has a call in a default argument, so it is lifted with a wider pattern.
const routeHref=views.match(/^function routeHref\(.*\) \{[\s\S]*?\n\}/m)[0];
const parseSegments=screen.match(/^ {2}const \[requestedModule,requestedSection\]=.*$/m)[0];
const route=(section,hash)=>{
  const context=sandbox(`var current={context:'acme-001'},lastFile=new Map(),contexts={'acme-001':{folder:'acme-001',modules:{}}},defaultOutput=()=>null;`,routeHref,
    `function parse(path){${parseSegments}return [requestedModule,requestedSection];}`);
  context.URLSearchParams=URLSearchParams;
  const href=vm.runInContext(`routeHref('W-Reports',${JSON.stringify(section)},null,'acme-001')`,context);
  return {href,parsed:[...vm.runInContext(`parse(${JSON.stringify(hash(href))})`,context)]};
};
// A browser's location.hash percent-encodes space, ", <, > and backtick in the fragment (URL standard).
const browserHash=href=>new URL(`http://x/${href}`).hash.slice(1).split('?')[0];

test('a report id from a folder name stays inside its href and routes back to the same report',()=>{
  // Expected by hand: encodeURIComponent of each id; every one decodes back to the folder name.
  const cases={
    'r"><img src=q onerror=1>':'#W-Reports/r%22%3E%3Cimg%20src%3Dq%20onerror%3D1%3E?c=acme-001',
    'TDG report 2024':'#W-Reports/TDG%20report%202024?c=acme-001',
    "a?b#c&d'":"#W-Reports/a%3Fb%23c%26d'?c=acme-001",
    '100% build':'#W-Reports/100%25%20build?c=acme-001',
  };
  for(const [id,expected] of Object.entries(cases)){
    const {href,parsed}=route(id,browserHash);
    assert.equal(href,expected);
    assert.ok(!/["<>&]/.test(href),href);
    assert.deepEqual(parsed,['W-Reports',id]);
  }
});

test('a hand-typed malformed escape in the address is read as typed, not thrown',()=>{
  const {parsed}=route('list',()=>'W-Reports/%E0%A4%A');
  assert.deepEqual(parsed,['W-Reports','%E0%A4%A']);
});

test('a chart cell that is not a number shows its retained text, escaped, and draws no bar',()=>{
  // Expected by hand: only "5" parses (the row maximum, 100% wide); a cell with any letter or digit keeps
  // its own text, and an empty, absent or placeholder-only ("—") cell says "Not available". None draws a bar.
  const cells=['5','Not supplied: reported in EUR m','Not supplied:','','(5.0%)','<b>x</b> & y','—'];
  const context=sandbox(...basics,grab(views,'chartNumber'),grab(views,'chartIntro'),grab(views,'comparisonChart'),`
    var sourceFooter=()=>'';
    var table={headers:['Item',${cells.map((_,i)=>`'c${i}'`).join(',')},'c7'],rows:[{line:3,cells:['Revenue',...${JSON.stringify(cells)}]}]};
    var fixtureTable=()=>table;
    var data={'r/CP-1.md':{module:'CP-1'}};`);
  const html=vm.runInContext(`comparisonChart('r/CP-1.md',{kind:'bars',title:'T',table:1,columns:[1,2,3,4,5,6,7,8]})`,context);
  const shown=[...html.matchAll(/<strong>(.*?)<\/strong>/g)].map(m=>m[1]);
  assert.deepEqual(shown,['5','Not supplied: reported in EUR m','Not supplied:','Not available','(5.0%)','&lt;b&gt;x&lt;/b&gt; &amp; y','Not available','Not available']);
  const tracks=[...html.matchAll(/<span class="track ([^"]*)">/g)].map(m=>m[1]);
  assert.deepEqual(tracks,['','missing','missing','missing','missing','missing','missing','missing']);
  assert.match(html,/<i class="series-0" style="width:100%">/);
});

test('an escaped slash, a doubled escape or a path-like id cannot make a second route segment',()=>{
  // Expected by hand: the path is split on "/" and "?" before decoding, so %2F and %3F stay inside
  // their segment; %252F decodes once to the literal text "%2F".
  const parse=hash=>route('list',()=>hash).parsed;
  assert.deepEqual(parse('W-Reports/a%2Fb'),['W-Reports','a/b']);
  assert.deepEqual(parse('W-Reports/a%252Fb'),['W-Reports','a%2Fb']);
  assert.deepEqual(parse('W-Library%2Fcases'),['W-Library/cases',undefined]);
  assert.deepEqual(parse('W-Reports/a%3Fc=1'),['W-Reports','a?c=1']);
  assert.deepEqual(parse('W-Reports/..%2F..'),['W-Reports','../..']);
});
