/* DOM simulation of the Library screen's credit and market screening over the hand-written fixture catalogue; expected ids and counts come from the committed answer keys. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const {JSDOM}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const read=name=>fs.readFileSync(path.join(__dirname,name),'utf8');
const fixture=name=>JSON.parse(fs.readFileSync(path.join(__dirname,'../../../tests/fixtures/library-credit',name),'utf8'));
const html=read('index.html'),catalogue=fixture('screening-catalogue.json'),cases=fixture('filter-cases.json'),sortCases=fixture('sort-cases.json');
const text=el=>el.textContent.replace(/\s+/g,' ').trim();
const empty={runs:{},outputs:{},inputs:{},pins:{},reports:[],models:[],visuals:[],issues:[],handoffs:{}};
const sorted=list=>[...list].sort();
const byName=name=>cases.find(c=>c.name===name);
function page(t,hash='W-Library/cases',data=catalogue){
  const dom=new JSDOM(html,{url:`http://127.0.0.1:1/index.html#${hash}`,runScripts:'outside-only'}),w=dom.window;
  w.scrollTo=()=>{};w.fetch=()=>new Promise(()=>{});w.HTMLElement.prototype.scrollIntoView=function(){};
  const context=dom.getInternalVMContext();
  vm.runInContext(read('hydrate.js'),context);w.hydrate(structuredClone(empty));
  w.DESIGN_DATA={runs:{},outputs:{},inputs:{},pins:{}};w.DESIGN_WORKSPACE={reports:[],models:[],visuals:[]};
  w.DESIGN_CATALOGUE=structuredClone({real:data.real,sources:data.sources});
  w.DESIGN_APP={workspace:'',policy_locked:false,issues:[],problem:''};
  for(const name of ['screening.js','views.js','actions.js','screen.js'])vm.runInContext(read(name),context);
  t.after(()=>w.close());
  const d=w.document,set=(id,value)=>{const el=d.getElementById(id);el.value=value;
    if(el.type==='number'&&value!==''&&!Number.isFinite(Number(value)))Object.defineProperty(el,'validity',{value:{badInput:true},configurable:true}); // jsdom blanks unreadable number text; a browser reports badInput
    el.dispatchEvent(new w.Event(el.tagName==='SELECT'?'change':'input',{bubbles:true}));};
  const ids=()=>[...d.querySelectorAll('#library-results button[data-library-select]')].map(b=>b.dataset.librarySelect);
  return {w,d,set,ids,logic:code=>JSON.parse(vm.runInContext(`JSON.stringify(${code})`,context)),
    through:filters=>{for(const [k,v] of Object.entries(filters))set(`library-${k}`,v);},
    cell:(id,column)=>{const heads=[...d.querySelectorAll('#library-results thead th')].map(text),i=heads.findIndex(h=>h.startsWith(column));
      return text(d.querySelector(`#library-results tr:has([data-library-select="${id}"])`).children[i]);},
    row:id=>text(d.querySelector(`#library-results tr:has([data-library-select="${id}"])`)),
    lines:()=>[...d.querySelectorAll('#library-coverage [data-library-coverage]')],
    detail:()=>text(d.getElementById('run-detail'))};
}
const total=catalogue.real.length;

for(const c of cases) test(`${c.focus}: ${c.name} through the controls`,t=>{
  const p=page(t);
  p.through(c.filters);
  assert.deepEqual(sorted(p.ids()),c.expected_ids);
  const lines=p.lines();
  assert.deepEqual(sorted(lines.map(l=>l.dataset.libraryCoverage)),sorted(Object.keys(c.coverage||{})),'one line per active group');
  for(const group of Object.keys(c.coverage||{})) {
    const {recorded,hidden}=c.coverage[group],line=p.d.querySelector(`[data-library-coverage="${group}"]`),shown=text(line);
    assert.ok(shown.includes(`recorded for ${recorded} of ${total} runs`),shown);
    assert.equal(shown.includes(`· ${hidden} hidden · Show them`),hidden>0,shown);
    if(hidden) {
      line.querySelector('button').click();
      assert.equal(p.ids().length,hidden,`${group}: Show them lists the key's hidden count`);
      assert.match(text(p.d.getElementById('library-results')),/^Hidden by .+: (no figure|not) recorded/);
      p.d.querySelector('#library-results [data-library-back]').click();
      assert.deepEqual(sorted(p.ids()),c.expected_ids,'Back to results restores the matching rows');
    }
  }
});

test('RF17 Show them lists rows that carry no net leverage figure, none that carry one',t=>{
  const p=page(t);p.through({runs:'any',netLeverageMax:'4'});
  p.d.querySelector('[data-library-coverage="net_leverage"] button').click();
  assert.ok(text(p.d.getElementById('library-results')).startsWith('Hidden by Net leverage: no figure recorded'));
  assert.equal(p.ids().length,byName('RF17 net leverage max 4, any').coverage.net_leverage.hidden);
  for(const id of p.ids()) {
    const metric=catalogue.real.find(r=>r.id===id).metrics.net_leverage,value=String(metric?.value??'').trim();
    assert.ok(value===''||!Number.isFinite(Number(value))||Number(value)<0,`${id} carries a figure`);
  }
});

test('default Latest view shows the key rows, tags what Latest does not screen and says how many',t=>{
  const p=page(t),key=byName('default filters, latest');
  assert.deepEqual(sorted(p.ids()),key.expected_ids);
  const tagged=sorted(p.logic('LibraryLogic.screened(window.DESIGN_CATALOGUE.real,{}).filter(e=>e.notScreened).map(e=>e.run.id)'));
  assert.deepEqual(sorted(p.ids().filter(id=>p.row(id).includes('No report · not screened'))),tagged);
  assert.ok(tagged.includes('aldermoor-2025-001'),'the stopped run is tagged');
  const left=byName('runs any, no other filter').expected_ids.length-key.expected_ids.length; // rows Any run adds, from the key
  assert.match(text(p.d.getElementById('library-coverage')),new RegExp(`${left} runs not screened.*Any run`));
  p.set('library-runs','any');
  assert.deepEqual(sorted(p.ids()),byName('runs any, no other filter').expected_ids);
  assert.equal(p.d.getElementById('library-runs').selectedOptions[0].textContent,'Any run');
  assert.doesNotMatch(text(p.d.getElementById('library-coverage')),/not screened/);
});

test('RF18 Leverage reads only metrics.leverage: a net-leverage-only run shows a dash; the basis default text stays',t=>{
  const p=page(t);p.set('library-runs','any');
  assert.ok(p.cell('fairholt-001','Leverage').startsWith('—'));
  assert.ok(p.cell('fairholt-001','Net leverage').includes('×'));
  assert.equal(p.d.getElementById('library-basis').options[0].textContent,'All bases · definitions differ');
});

test('RF20 the Rating column shows the lowest rating as entered with agency, scope and date',t=>{
  const p=page(t);p.set('library-runs','any');
  assert.ok(p.cell('hartley-001','Rating').startsWith('(P)B2'),p.cell('hartley-001','Rating'));
  assert.match(p.cell('hartley-001','Rating'),/S&P|Fitch|Moody/);
  assert.ok(p.cell('kestrel-001','Rating').startsWith('—'),'a scope-less rating is not counted under issuer scope');
  assert.equal(p.d.getElementById('library-ratingBelow').selectedOptions[0].textContent,'Any');
  assert.ok([...p.d.getElementById('library-ratingBelow').options].some(o=>o.textContent==='BB+ / Ba1'&&o.value==='BB+/Ba1'));
  p.through(byName('RF20 rating below B/B2, issuer scope, any runs').filters);
  const issuer=p.ids();
  p.through({ratingScope:'any'});
  assert.deepEqual(sorted(p.ids()),byName('RF20 rating below B/B2, any scope, any runs').expected_ids);
  assert.deepEqual(sorted(issuer),byName('RF20 rating below B/B2, issuer scope, any runs').expected_ids);
});

test('RF23 the private-side run carries a Private-side label in its row and its detail; its terms show as entered',t=>{
  const p=page(t),id='brackenfell-hy-001';
  assert.ok(p.row(id).includes('Private-side')&&p.row(id).includes('High yield'));
  assert.ok(!p.row('dunmore-001').includes('Private-side'));
  p.d.querySelector(`[data-library-select="${id}"]`).click();
  const detail=p.detail();
  for(const shown of ['Private-side','Classification','High yield','Currency','USD','Net leverage','Undrawn facilities','TLB','Spread talk, low','325','bps','Entered by the user · shown as entered','Facilities & quotes as entered','B · S&P'])assert.ok(detail.includes(shown),shown);
  assert.ok(p.d.querySelector('#run-detail [data-library-source="brackenfell-hy-001.TLB-talk_spread_bps_low"]'),'a facility figure has View source');
});

test('the new sort buttons are native buttons and sort to the key order, both ways',t=>{
  for(const c of sortCases) {
    const p=page(t);p.through(c.filters);
    const button=p.d.querySelector(`[data-library-sort="${c.key}"]`);
    assert.equal(button.tagName,'BUTTON');assert.equal(button.type,'button');
    button.click();if(c.direction==='desc')p.d.querySelector(`[data-library-sort="${c.key}"]`).click();
    assert.deepEqual(p.ids(),c.expected_ids,c.name);
    assert.equal(p.d.activeElement.dataset.librarySort,c.key);
  }
});

test('every new control is labelled, ids are unique, disclosures report their active count',t=>{
  const {d,set}=page(t);
  const need=['runs','classification','currency','ratingBelow','ratingAbove','ratingScope','netLeverageMin','netLeverageMax','cashMin','cashMax','undrawnMin','undrawnMax','talkMin','talkMax','marginMin','marginMax','couponMin','couponMax','priceMin','priceMax','yieldMin','yieldMax','limitation'];
  for(const k of need) {
    const el=d.getElementById(`library-${k}`);
    assert.ok(el,k);assert.ok(el.labels.length&&text(el.labels[0]),`${k} has a label`);
    if(/(Min|Max)$/.test(k))assert.equal(el.type==='number'&&el.step==='any',true,k);
  }
  const ids=[...d.querySelectorAll('[id]')].map(x=>x.id);assert.equal(ids.length,new Set(ids).size);
  assert.match(text(d.getElementById('library-coverage')),/not screened/);
  assert.equal(d.getElementById('library-coverage').getAttribute('role'),'status');
  set('library-currency','EUR');set('library-talkMin','300');
  const summaries=[...d.querySelectorAll('#library-filters details > summary')].map(text);
  assert.ok(summaries.some(s=>s.startsWith('Classification, rating & currency')&&s.endsWith('· 1 active')),summaries.join('|'));
  assert.ok(summaries.some(s=>s.startsWith('Facilities & quotes')&&s.endsWith('· 1 active')),summaries.join('|'));
  assert.deepEqual([...d.getElementById('library-currency').options].map(o=>o.value),['','EUR','GBP','USD']);
  assert.ok(text(d.getElementById('library-filters')).includes('Matched within one facility'));
});

test('hostile facility id and limitation text render as text and create no element',t=>{
  const bad='<img src=x onerror=alert(1)>',data=structuredClone(catalogue);
  const run=data.real.find(r=>r.id==='brackenfell-hy-001');run.facilities[0].facility_id=bad;run.gaps=[bad];
  const p=page(t,'W-Library/cases',data);
  p.d.querySelector('[data-library-select="brackenfell-hy-001"]').click();
  assert.ok(p.detail().includes(bad));
  assert.equal(p.d.querySelectorAll('.library-screen img[src="x"],.library-screen [onerror]').length,0);
  assert.ok([...p.d.getElementById('library-limitation').options].some(o=>o.value===bad&&o.textContent===bad));
  p.set('library-limitation',bad);assert.deepEqual(p.ids(),['brackenfell-hy-001']);
});

test('the Library query carries the filter state and is read back; unknown or invalid parts are dropped',t=>{
  const p=page(t);
  p.through({runs:'any',netLeverageMax:'4'});
  p.d.querySelector('[data-library-sort="net_leverage"]').click();
  assert.equal(p.w.location.hash,'#W-Library/cases?runs=any&netLeverageMax=4&sort=net_leverage&dir=asc');
  p.set('library-netLeverageMax','');p.set('library-runs','latest');
  assert.equal(p.w.location.hash,'#W-Library/cases?sort=net_leverage&dir=asc','defaults are not written');
  const key=byName('RF17 net leverage max 4, any');
  const q=page(t,'W-Library/cases?runs=any&netLeverageMax=4&ratingBelow=BB%2B%2FBa1&classification=high_yield');
  assert.equal(q.d.getElementById('library-netLeverageMax').value,'4');assert.equal(q.d.getElementById('library-runs').value,'any');
  assert.equal(q.d.getElementById('library-ratingBelow').value,'BB+/Ba1');
  assert.ok(q.ids().every(id=>key.expected_ids.includes(id)));
  const r=page(t,`W-Library/cases?runs=any&netLeverageMax=4&sort=net_leverage&dir=desc`);
  assert.deepEqual(sorted(r.ids()),key.expected_ids);
  assert.deepEqual(r.ids(),sortCases.find(c=>c.name==='net leverage descending, any').expected_ids.filter(id=>key.expected_ids.includes(id)));
  const junk=page(t,`W-Library/cases?bogus=1&classification=nope&netLeverageMax=abc&runs=any&sort=nothing&search=${'x'.repeat(300)}`);
  const value=id=>junk.d.getElementById(id).value;
  assert.deepEqual(['classification','netLeverageMax','query'].map(k=>value(`library-${k}`)),['','','']);
  assert.equal(value('library-runs'),'any','a valid part beside invalid ones is kept');
  assert.equal(junk.ids().length,total);
  const later=page(t);
  later.w.location.hash='#W-Library/cases?runs=any&classification=high_yield';
  return new Promise(resolve=>setTimeout(()=>{
    assert.equal(later.d.getElementById('library-classification').value,'high_yield');
    assert.deepEqual(sorted(later.ids()),byName('RF23 high yield, any').expected_ids);
    resolve();
  },50));
});

test('narrow screens stack the panel, table and detail',()=>{
  const css=read('screen.css'),block=query=>[...css.matchAll(new RegExp(`@media\\(max-width:${query}px\\)\\{`,'g'))].map(m=>{
    let depth=1,i=m.index+m[0].length;const start=i;
    while(depth&&i<css.length){depth+=css[i]==='{'?1:css[i]==='}'?-1:0;i+=1;}
    return css.slice(start,i-1);}).join('');
  assert.match(block(900),/\.library-screen\{grid-template-columns:minmax\(0,1fr\)\}/);
  assert.match(block(720),/\.library-filters,\.metric-grid,\.detail-layout\{grid-template-columns:minmax\(0,1fr\)\}/);
});

test('Rating sort follows the Rating scope the column shows (probe-13d-rating-sort-scope)',t=>{
  const p=page(t,'W-Library/cases?runs=any&ratingScope=any&sort=rating&dir=asc');
  const shown=p.ids().map(id=>p.cell(id,'Rating').startsWith('—'));
  assert.ok(shown.includes(false)&&shown.includes(true));
  assert.equal(shown.lastIndexOf(false)<shown.indexOf(true),true,'rated rows sort before unrated rows');
});

test('cash and undrawn sort as metrics, missing last',t=>{
  const p=page(t),rows=catalogue.real,fig=(r,k)=>{const v=Number(r.metrics[k]?.value);return r.metrics[k]&&String(r.metrics[k].value).trim()!==''&&v>=0?v:null;};
  for(const k of ['cash','undrawn']) {
    const out=p.logic(`LibraryLogic.sortRuns(window.DESIGN_CATALOGUE.real,'${k}','desc').map(r=>r.id)`);
    const have=out.filter(id=>fig(rows.find(r=>r.id===id),k)!==null).map(id=>fig(rows.find(r=>r.id===id),k));
    assert.deepEqual(have,[...have].sort((a,b)=>b-a),k);
    const firstMissing=out.findIndex(id=>fig(rows.find(r=>r.id===id),k)===null);
    assert.ok(firstMissing===-1||firstMissing===have.length,`${k}: missing last`);
  }
});

test('a change event after the input event applied the value rebuilds nothing, so the click that caused the blur lands',t=>{
  const p=page(t);p.through({runs:'any'});
  const box=p.d.getElementById('library-netLeverageMax');box.value='4';box.dispatchEvent(new p.w.Event('input',{bubbles:true}));
  const button=p.d.querySelector('[data-library-hidden="net_leverage"]');
  box.dispatchEvent(new p.w.Event('change',{bubbles:true}));
  assert.equal(button.isConnected,true);
});

test('query numbers the number box would blank are dropped',t=>{
  const p=page(t,'W-Library/cases?runs=any&netLeverageMax=%2B4&cashMin=4.&undrawnMax=.5');
  assert.deepEqual(['netLeverageMax','cashMin','undrawnMax'].map(k=>p.d.getElementById(`library-${k}`).value),['','','.5']);
});

test('the Latest line counts what Any run adds under the active filters, from the key',t=>{
  const p=page(t),latest=byName('RF17 net leverage max 4, latest'),any=byName('RF17 net leverage max 4, any');
  p.through({netLeverageMax:'4'});
  const added=any.expected_ids.length-latest.expected_ids.length;
  assert.match(text(p.d.getElementById('library-coverage')),new RegExp(`${added} runs not screened by the Latest run rule`));
});

test('the Private-side detail row appears only for a private-side run',t=>{
  const p=page(t);
  p.d.querySelector('[data-library-select="brackenfell-hy-001"]').click();assert.ok(p.detail().includes('Private-side · Yes'));
  p.d.querySelector('[data-library-select="dunmore-001"]').click();assert.ok(!p.detail().includes('Private-side'));
});

test('issuers differing only in case are one nav entry and one issuer in the count',t=>{
  const key=fixture('issuer-case-cases.json'),p=page(t,'W-Library/cases',{real:key.runs,sources:{}});
  p.set('library-runs','any');
  const entries=[...p.d.querySelectorAll('#library-nav [data-library-issuer]')];
  assert.deepEqual(entries.map(b=>({label:text(b.querySelector('span:not(.monogram):not(.count)')),count:Number(text(b.querySelector('.count')))})),key.nav.issuers.map(({label,count})=>({label,count})));
  assert.deepEqual(entries.map(b=>text(b.querySelector('.monogram'))),key.nav.issuers.map(i=>i.monogram_from.slice(0,3)));
  assert.match(text(p.d.getElementById('library-count')),new RegExp(`· ${key.nav.count_line_issuers} issuers$`));
  entries[0].click();
  assert.equal(entries[0].dataset.libraryIssuer,'TDG');
  assert.deepEqual(sorted(p.ids()),sorted(key.runs.filter(r=>r.issuer.toLowerCase()==='tdg').map(r=>r.id)));
  assert.equal(p.d.querySelector('#library-nav .nav-choice.active [data-x]'),null);
});
