/* DOM simulation of the Library screen over the pinned 2026-11-08 catalogue, compared with the hand-written key. No browser, network, store or provider: rows join no run, so none links to an Overview. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const {JSDOM}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const read=name=>fs.readFileSync(path.join(__dirname,name),'utf8');
const html=read('index.html'),pinned=JSON.parse(read('testdata/catalogue-2026-11-08.json')),key=JSON.parse(read('testdata/library-screening-expected.json'));
const text=el=>el.textContent.replace(/\s+/g,' ').trim();
const empty={runs:{},outputs:{},inputs:{},pins:{},reports:[],models:[],visuals:[],issues:[],handoffs:{}};
function page(t,catalogue=pinned,problem=''){
  const dom=new JSDOM(html,{url:'http://127.0.0.1:1/index.html#W-Library/cases',runScripts:'outside-only'}),w=dom.window;
  w.scrollTo=()=>{};w.fetch=()=>new Promise(()=>{});w.HTMLElement.prototype.scrollIntoView=function(){};
  const context=dom.getInternalVMContext(),store=structuredClone(empty);
  vm.runInContext(read('hydrate.js'),context);w.hydrate(store);
  w.DESIGN_DATA={runs:{},outputs:{},inputs:{},pins:{}};w.DESIGN_WORKSPACE={reports:[],models:[],visuals:[]};
  w.DESIGN_CATALOGUE=structuredClone({real:catalogue.real,sources:catalogue.sources});
  w.DESIGN_APP={workspace:'',policy_locked:false,issues:[],problem};
  for(const name of ['screening.js','views.js','actions.js','screen.js'])vm.runInContext(read(name),context);
  t.after(()=>w.close());
  const d=w.document,fire=(el,type)=>el.dispatchEvent(new w.Event(type,{bubbles:true}));
  const set=(id,value)=>{const el=d.getElementById(id);el.value=value;fire(el,el.tagName==='SELECT'?'change':'input');};
  const ids=()=>[...d.querySelectorAll('#library-results button[data-library-select]')].map(b=>b.dataset.librarySelect);
  const sort=name=>d.querySelector(`[data-library-sort="${name}"]`);
  return {w,d,set,ids,sort,count:()=>text(d.getElementById('library-count')),detail:()=>text(d.getElementById('run-detail'))};
}
const sorted=list=>[...list].sort();
const all=[...key.run_folder_rows.ids,...key.delivery_rows.ids];

test('the screen lists the 59 served rows in served order under 7 issuers, each issuer choice with its key count',t=>{
  const p=page(t);
  assert.equal(p.count(),`59 of 59 runs · 7 issuers`);
  assert.deepEqual(p.ids(),key.default_sort.served_order);
  assert.deepEqual(sorted(p.ids()),sorted(all));
  const nav=Object.fromEntries([...p.d.querySelectorAll('[data-library-issuer]')].map(b=>[b.dataset.libraryIssuer,text(b.querySelector('.count'))]));
  assert.deepEqual(nav,Object.fromEntries(Object.entries(key.issuer_count.rows_per_issuer).map(([k,v])=>[k,String(v)])));
  assert.equal(p.d.querySelectorAll('a.run-link').length,0,'with no joined store run no row links to an Overview');
});

test('missing is never shown as zero: a row without metrics shows a dash and Not assessed',t=>{
  const p=page(t),row=p.d.querySelector('tr:has([data-library-select="tdg-001"])');
  const cells=[...row.querySelectorAll('td')].map(text);
  assert.ok(cells[3].startsWith('—')&&cells[4].startsWith('—'),cells.join(' | '));
  assert.ok(cells[5].startsWith('Not assessed'));
  assert.doesNotMatch(cells.join(' '),/\b0(\.0+)?×/);
});

test('each filter selects the key rows; a blank bound is ignored and a set one never matches a missing value',t=>{
  const p=page(t);
  p.set('library-leverageMin',key.filter_cases.a_leverage_min.filters.leverageMin);
  assert.deepEqual(sorted(p.ids()),sorted(key.filter_cases.a_leverage_min.expected_ids));
  p.set('library-leverageMin','1.61');assert.deepEqual(p.ids(),['tdg-002'],'a minimum is inclusive and the smaller leverage falls out');
  p.set('library-leverageMin','');p.set('library-leverageMax','1.59');assert.deepEqual(p.ids(),[],'a maximum below every leverage');
  p.set('library-leverageMax','100');assert.deepEqual(sorted(p.ids()),sorted(['ford-otosan-2024-001','tdg-002']),'a set bound never matches a missing leverage');
  p.set('library-leverageMax','');assert.equal(p.ids().length,59,'a blank bound ignores the filter');
  p.set('library-coverageMin','3.6');assert.deepEqual(sorted(p.ids()),sorted(['ford-otosan-2024-001','tdg-002']));
  p.set('library-coverageMin','3.61');assert.deepEqual(p.ids(),['ford-otosan-2024-001']);
  p.set('library-coverageMin','');p.set('library-coverageMax','3.6');assert.deepEqual(p.ids(),['tdg-002']);
  p.set('library-coverageMax','');
  p.set('library-basis',key.filter_cases.b_leverage_basis.filters.basis);assert.deepEqual(p.ids(),key.filter_cases.b_leverage_basis.expected_ids);
  p.set('library-basis','');
  p.set('library-query',key.filter_cases.c_search_issuer_name.filters.search);assert.deepEqual(p.ids(),key.filter_cases.c_search_issuer_name.expected_ids);
  p.set('library-query','');
  p.set('library-period','Quarterly actual');assert.deepEqual(p.ids().filter(id=>key.with_metrics.rows.some(r=>r.id===id)),['tdg-003']);
  p.set('library-period','');p.set('library-completion','unassessed');assert.equal(p.ids().length,59,'no served run has a completeness');
  p.set('library-completion','50');assert.deepEqual(p.ids(),[],'a completeness bound never matches a missing one');
  p.set('library-completion','');p.set('library-availability','handoff');
  const none=p.ids().length;p.set('library-availability','report');
  assert.equal(none+p.ids().length,59,'every row has a report or has none');
});

test('combined filters narrow together and count the metric filters in use',t=>{
  const p=page(t);
  p.set('library-sector','Aerospace & defense');p.set('library-leverageMin','5');
  assert.deepEqual(p.ids(),['tdg-002']);
  assert.equal(p.d.getElementById('metric-filter-count').textContent,'· 1 active');
  p.set('library-leverageMin','');for(const id of ['tdg-002','tdg-003','tdg-guidance-001'])assert.ok(p.ids().includes(id),id);
  assert.equal(p.d.getElementById('metric-filter-count').textContent,'');
});

test('sorting: missing last, descending after ascending, the key order; the header says which way',t=>{
  const p=page(t);
  assert.equal(p.sort('leverage').closest('th').getAttribute('aria-sort'),'none');
  p.sort('leverage').click();
  assert.equal(p.sort('leverage').closest('th').getAttribute('aria-sort'),'ascending');
  assert.deepEqual(p.ids().slice(0,2),['ford-otosan-2024-001','tdg-002']);
  p.sort('leverage').click();
  assert.equal(p.sort('leverage').closest('th').getAttribute('aria-sort'),'descending');
  assert.deepEqual(p.ids().slice(0,4),key.sort_leverage_desc_missing_last.first_4_ids);
  assert.equal(p.ids().length,59);
  p.sort('coverage').click();assert.deepEqual(p.ids().slice(0,2),['tdg-002','ford-otosan-2024-001'],'3.60 before 8.2');
  assert.equal(p.w.document.activeElement,p.sort('coverage'),'the sort button keeps focus');
});

test('sort buttons and issuer choices are native buttons: tabbable, named, and keep focus and state when used',t=>{
  const p=page(t),{d}=p;
  for(const b of d.querySelectorAll('[data-library-sort],[data-library-issuer],[data-library-nav],[data-library-select]')){
    assert.equal(b.tagName,'BUTTON');assert.equal(b.type,'button');assert.notEqual(b.getAttribute('tabindex'),'-1');assert.ok(text(b)||b.getAttribute('aria-label'));
  }
  const tdg=()=>d.querySelector('[data-library-issuer="TDG"]');
  assert.equal(tdg().getAttribute('aria-pressed'),'false');
  tdg().click();
  assert.equal(d.activeElement.dataset.libraryIssuer,'TDG');assert.equal(d.activeElement.getAttribute('aria-pressed'),'true');
  assert.equal(p.count(),`13 of 59 runs · 1 issuer`);
  tdg().click();assert.equal(p.ids().length,59,'a second choice releases the issuer');
  d.querySelector('[data-library-nav="reports"]').click();
  assert.equal(d.activeElement.dataset.libraryNav,'reports');assert.equal(d.activeElement.getAttribute('aria-pressed'),'true');
  d.querySelector('[data-library-nav="all"]').click();assert.equal(p.ids().length,59);
});

test('selecting a row opens its detail with the key values and bases, one run at a time',t=>{
  const p=page(t);
  assert.equal(p.d.getElementById('run-detail').hidden,false,'the first row is selected on load');
  for(const row of key.with_metrics.rows) {
    p.d.querySelector(`[data-library-select="${row.id}"]`).click();
    const detail=p.detail();
    assert.ok(detail.includes(row.id),row.id);
    for(const [name,m] of Object.entries(row.metrics_present)) {
      assert.ok(detail.includes(m.basis),`${row.id} ${name} basis`);
      const shown=m.unit==='x'?`${m.value}×`:Number(m.value).toLocaleString('en-GB');
      assert.ok(detail.includes(shown),`${row.id} ${name}: ${shown}`);
    }
    assert.ok(detail.includes('Not assessed'));
  }
  p.d.querySelector('[data-library-select="tdg-003"]').click();
  assert.ok(p.detail().includes('Not established for this case.'),'tdg-003 has no leverage');
  assert.equal(p.d.querySelectorAll('#library-results tr.selected').length,1);
});

test('View source moves to the source block; Reset returns every filter, the sort and the selection to the start',t=>{
  const p=page(t);
  p.d.querySelector('[data-library-select="tdg-002"]').click();
  p.d.querySelector('[data-library-source="tdg-002.tdg-base"]').click();
  assert.equal(p.d.getElementById('metric-sources').open,true);
  assert.equal(p.d.activeElement.id,'source-tdg-002.tdg-base');
  p.set('library-leverageMin','5');p.sort('leverage').click();p.d.querySelector('[data-library-issuer="TDG"]').click();
  assert.deepEqual(p.ids(),['tdg-002']);
  p.d.getElementById('library-clear').click();
  assert.deepEqual(p.ids(),key.default_sort.served_order);
  for(const el of p.d.querySelectorAll('#library-filters [data-library-filter]'))assert.equal(el.value,'',el.id);
  assert.equal(p.d.querySelector('[data-library-sort="leverage"]').closest('th').getAttribute('aria-sort'),'none');
  assert.equal(p.d.activeElement.id,'library-query');
});

test('no match shows a reset that works; an empty workspace and an unreadable one each say so',t=>{
  const p=page(t);
  p.set('library-query','no such issuer anywhere');
  assert.equal(p.count(),'0 of 59 runs · 0 issuers');
  assert.ok(text(p.d.getElementById('library-results')).includes('No runs match these filters'));
  assert.equal(p.d.getElementById('run-detail').hidden,true);
  p.d.getElementById('library-empty-reset').click();
  assert.equal(p.ids().length,59);
  const none=page(t,{real:[],sources:{}});
  assert.ok(text(none.d.getElementById('library-results')).includes('No runs in this workspace yet'));
  const bad=page(t,{real:[],sources:{}},'503');
  assert.ok(text(bad.d.getElementById('library-results')).includes('The library could not read this workspace'));
  assert.equal(bad.d.querySelector('#library-results a').getAttribute('href'),'#W-Settings/workspace');
});

test('every control is labelled, ids are unique, and the count is announced',t=>{
  const {d}=page(t);
  const ids=[...d.querySelectorAll('[id]')].map(x=>x.id);
  assert.equal(ids.length,new Set(ids).size);
  for(const control of d.querySelectorAll('#library-filters input,#library-filters select'))assert.ok(control.labels.length&&text(control.labels[0]),control.id);
  assert.equal(d.getElementById('library-count').getAttribute('role'),'status');
  assert.equal(d.getElementById('library-count').getAttribute('aria-live'),'polite');
  assert.ok(d.querySelector('#library-results table caption'));
  for(const th of d.querySelectorAll('#library-results thead th'))assert.equal(th.getAttribute('scope'),'col');
});

test('hostile record text is rendered as text; no markup, handler or script link comes of it',t=>{
  const bad='<img src=x onerror=alert(1)>',quote='x" onmouseover="alert(1)',evil='javascript:alert(1)';
  const base=structuredClone(pinned.real.find(r=>r.id==='tdg-002'));
  const metric=name=>({value:'12.5',unit:bad,period:bad,basis:quote+name,source:`s${name}"><i>`});
  const run={...base,id:`${quote}-1`,issuer:bad,name:bad,title:quote,sector:bad,workflow:quote,date:bad,period:bad,period_kind:bad,summary:bad,
    gaps:[bad],ratings:[{label:bad,date:bad,source:`r"><i>`}],identity_source:bad,sector_source:quote,handoff_href:evil,completion:null,
    metrics:{revenue:metric('r'),ebitda:metric('e'),leverage:{...metric('l'),unit:'x'},coverage:metric('c'),cash:metric('h'),cashflow:metric('f')},
    artifacts:[{folder:'f',kind:'report',label:bad,state:'candidate',relationship:'direct',available:true,href:evil,issue:''},
      {folder:'g',kind:'report',label:bad,state:'candidate',relationship:'direct',available:false,href:'/files/x',issue:bad},
      {folder:'h',kind:'model',label:bad,state:'candidate',relationship:'related',available:true,href:'//evil.example/x',issue:''}]};
  const sources={};
  for(const id of [bad,quote,'r"><i>','sr"><i>','se"><i>','sl"><i>','sc"><i>','sh"><i>','sf"><i>'])sources[id]={path:bad,sha256:'0',line:quote,quote:`${bad}</blockquote><script>alert(1)</script>`,href:evil};
  const p=page(t,{real:[run,{...base,id:'plain-1',issuer:quote,artifacts:[],handoff_href:evil}],sources});
  const check=()=>{
    const screen=p.d.querySelector('.library-screen');
    for(const el of [screen,...screen.querySelectorAll('*')])for(const attr of el.attributes)assert.doesNotMatch(attr.name,/^on/i,`${el.tagName} ${attr.name}`);
    assert.equal(screen.querySelectorAll('script,i,b,img[src="x"]').length,0);
    assert.equal([...screen.querySelectorAll('a')].filter(a=>/^\s*(javascript|data):/i.test(a.getAttribute('href'))||a.getAttribute('href').startsWith('//')).length,0,'no script or off-origin link');
  };
  assert.deepEqual(p.ids(),[run.id,'plain-1']);
  check();
  assert.ok(text(p.d.getElementById('library-results')).includes(bad),'the markup shows as text');
  p.d.querySelector('[data-library-select]').click();
  check();
  const detail=p.detail();
  for(const shown of [bad,quote,'Unavailable'])assert.ok(detail.includes(shown),shown);
  assert.equal(p.d.querySelectorAll('.artifact-list li').length,3);
  const gone=[...p.d.querySelectorAll('.artifact-list li')].filter(li=>text(li).includes('Unavailable'));
  assert.equal(gone.length,1);
  assert.equal(gone[0].querySelector('a'),null,'the unavailable artifact is text, not a link');
  p.d.querySelector('[data-library-select="plain-1"]').click();
  check();
  assert.ok(p.detail().includes('No final deliverable has been indexed'),'a run with no artifact and a script handoff link offers no link');
  p.set('library-period',bad);assert.deepEqual(p.ids(),[run.id],'the period kind selects as text');
  check();
});

test('a number box holding unreadable text does not leave an invisible filter after the panel is rebuilt',t=>{
  const p=page(t),box=p.d.getElementById('library-leverageMin');
  Object.defineProperty(box,'validity',{value:{badInput:true}});
  box.dispatchEvent(new p.w.Event('input',{bubbles:true}));
  assert.deepEqual(p.ids(),[],'unreadable text excludes every run while it is shown');
  p.d.querySelector('[data-library-nav="reports"]').click();
  assert.equal(p.d.getElementById('library-leverageMin').value,'');
  assert.ok(p.ids().length>0,'the report rows are listed under the empty box');
});
