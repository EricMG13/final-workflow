/* The Library and Reports screens over the real retained workspace, read through the real app and compared with the frozen answer key. No provider is started. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path'),vm=require('node:vm'),net=require('node:net');
const {spawn,spawnSync}=require('node:child_process');
const {JSDOM}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const app=path.resolve(__dirname,'..'),repo=path.resolve(app,'../..');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const key=JSON.parse(fs.readFileSync(path.join(app,'designs/library-answer-key.json'),'utf8'));
const forecast=JSON.parse(fs.readFileSync(path.join(app,'designs/forecast-answer-key.json'),'utf8'));
const settle=(ms=10)=>new Promise(resolve=>setTimeout(resolve,ms));
const text=el=>el.textContent.replace(/\s+/g,' ').trim();
const PROVIDER_KEYS=['OPENAI_API_KEY','ANTHROPIC_API_KEY','OPENROUTER_API_KEY'];

function freePort(){
  return new Promise((resolve,reject)=>{
    const server=net.createServer();
    server.on('error',reject);
    server.listen(0,'127.0.0.1',()=>{const {port}=server.address();server.close(()=>resolve(port));});
  });
}
function binary(temp){
  if(process.env.ISSUER_LIBRARY_BINARY)return process.env.ISSUER_LIBRARY_BINARY;
  const out=path.join(temp,process.platform==='win32'?'issuer-library.exe':'issuer-library');
  const built=spawnSync('go',['build','-o',out,'.'],{cwd:app,encoding:'utf8'});
  assert.equal(built.status,0,`go build failed: ${built.stderr}`);
  return out;
}
async function until(check,what,ms=30000,fatal=()=>null){
  const end=Date.now()+ms;
  for(;;){
    const dead=fatal();if(dead)throw new Error(`${what}: ${dead}`);
    try{const value=await check();if(value)return value;}catch(error){if(Date.now()>end)throw new Error(`${what}: ${error.message}`);}
    if(Date.now()>end)throw new Error(`${what} timed out`);
    await settle(100);
  }
}
// Starts the real app on a loopback port, reads what the browser would read, and stops it.
async function readWorkspace(){
  const python=process.env.FW_PYTHON;
  assert.ok(python,'FW_PYTHON must name the interpreter that runs the engine');
  const temp=fs.mkdtempSync(path.join(os.tmpdir(),'issuer-library-surface-'));
  const port=await freePort(),base=`http://127.0.0.1:${port}`;
  const env={...process.env,ISSUER_LIBRARY_PYTHON:python,ISSUER_LIBRARY_ENGINE_ROOT:path.join(app,'engine')};
  for(const name of PROVIDER_KEYS)delete env[name];
  const child=spawn(binary(temp),['--workspace',repo,'--state-dir',path.join(temp,'state'),'--no-browser','--port',String(port)],{env,stdio:['ignore','pipe','pipe']});
  let printed='';child.stdout.on('data',chunk=>{printed+=chunk;});
  let exited=null,stderr='';child.stderr.on('data',chunk=>{stderr+=chunk;});
  const gone=new Promise(resolve=>child.on('exit',code=>{exited=code;resolve();}));
  try{
    await until(async()=>(await fetch(`${base}/health`)).ok,'server not serving',30000,()=>exited===null?null:`server exited ${exited}: ${stderr}`);
    // The library answers only a browser holding its session: exchange the one-time link it prints for the cookie.
    const link=await until(async()=>printed.split('\n').find(line=>line.startsWith(`Issuer Library: ${base}/launch?ticket=`)),'no launch link printed',30000,()=>exited===null?null:`server exited ${exited}: ${stderr}`);
    const launched=await fetch(link.slice('Issuer Library: '.length),{redirect:'manual'});
    const cookie=(launched.headers.get('set-cookie')||'').split(';')[0];
    assert.equal(launched.status,303,'the launch link was refused');assert.ok(cookie.includes('='),'no session cookie');
    const read=async url=>{const response=await fetch(base+url,{cache:'no-store',headers:{cookie}});if(!response.ok)assert.fail(`${url}: ${response.status} ${await response.text()}`);return response.json();};
    const catalogue=await read('/api/catalogue'),store=await read('/api/workspace');
    return {catalogue,store};
  }finally{
    child.kill();
    await gone;
    fs.rmSync(temp,{recursive:true,force:true});
  }
}
// The page's own data setup (web/boot.js), then the real screens.
function screens(read,hash){
  // The screens add their own destinations to the data, so each page gets its own copy, as each fetch would give.
  const {catalogue,store}=structuredClone(read);
  const dom=new JSDOM(html,{url:`http://127.0.0.1:1/index.html#${hash}`,runScripts:'outside-only'}),w=dom.window;
  w.scrollTo=()=>{};w.fetch=()=>new Promise(()=>{});w.HTMLElement.prototype.scrollIntoView=function(){};
  vm.runInContext(fs.readFileSync(path.join(__dirname,'hydrate.js'),'utf8'),dom.getInternalVMContext());
  w.hydrate(store);
  w.DESIGN_DATA={runs:store.runs,outputs:store.outputs,inputs:store.inputs,pins:store.pins};
  w.DESIGN_WORKSPACE={reports:store.reports,models:store.models,visuals:store.visuals};
  w.DESIGN_CATALOGUE={real:catalogue.real||[],sources:catalogue.sources||{}};
  w.DESIGN_APP={workspace:catalogue.workspace||'',policy_locked:!!catalogue.policy_locked,issues:store.issues,problem:''};
  for(const name of ['screening.js','views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());
  return dom;
}
const runKey=a=>new URLSearchParams(a.getAttribute('href').split('?')[1]).get('c');
const sorted=list=>[...list].sort();
const renderedKeys=d=>sorted([...d.querySelectorAll('#library-results a.run-link')].map(runKey));
const rowIds=d=>[...d.querySelectorAll('#library-results tbody button[data-library-select]')].map(b=>b.dataset.librarySelect);
// Hand-written by someone else (Plan 1, L0); read here only to check what the screen lists.
const expected=JSON.parse(fs.readFileSync(path.join(__dirname,'testdata/library-screening-expected.json'),'utf8'));

let workspace;
test.before(async()=>{workspace=await readWorkspace();});

test('Library lists every catalogue row; each run folder opens its Overview and each delivery row opens its report or model in the app',t=>{
  const w=screens(workspace,'W-Library/cases').window,d=w.document;t.after(()=>w.close());
  assert.equal(text(d.getElementById('library-count')),`${expected.row_count.value} of ${expected.row_count.value} runs · ${expected.issuer_count.value} issuers`);
  assert.deepEqual(sorted(rowIds(d)),sorted([...expected.run_folder_rows.ids,...expected.delivery_rows.ids]));
  assert.deepEqual(renderedKeys(d),sorted(Object.keys(workspace.store.runs)),'one Overview link per run folder');
  for(const id of expected.delivery_rows.ids) {
    const link=d.querySelector(`#library-results tr:has([data-library-select="${id}"]) a.report-link`);
    assert.match(link?.getAttribute('href')||'',/^#W-(Reports|Forecast)\//,id);
  }
});

test('Library search finds every run of the issuer searched',t=>{
  const w=screens(workspace,'W-Library/cases').window,d=w.document;t.after(()=>w.close());
  const box=d.getElementById('library-query');
  for(const [query,want] of Object.entries(key.library.search)){
    box.value=query;box.dispatchEvent(new w.Event('input',{bubbles:true}));
    assert.deepEqual(renderedKeys(d),sorted(want),`search "${query}"`);
  }
  box.value='TDG tdg-002';box.dispatchEvent(new w.Event('input',{bubbles:true}));
  assert.ok(rowIds(d).includes('tdg-002'),'a query spanning issuer and id');
  box.value=expected.filter_cases.c_search_issuer_name.filters.search;box.dispatchEvent(new w.Event('input',{bubbles:true}));
  assert.deepEqual(rowIds(d),expected.filter_cases.c_search_issuer_name.expected_ids);
});

test('A metric with more than 20 decimals is shown as served and does not blank the other rows',t=>{
  const forged=structuredClone(workspace),run=forged.catalogue.real.find(r=>r.id==='tdg-002'),long=`1.${'0'.repeat(100)}1`;
  run.metrics.ebitda.value=long;
  const w=screens(forged,'W-Library/cases').window,d=w.document;t.after(()=>w.close());
  assert.equal(rowIds(d).length,forged.catalogue.real.length);
  d.querySelector('[data-library-select="tdg-002"]').click();
  assert.ok(text(d.getElementById('run-detail')).includes(long));
});

test('Reports for a run list the same issuer by identity, not by display name',async t=>{
  const w=screens(workspace,'W-Reports/list?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  await settle();
  const ids=cls=>[...d.querySelectorAll(`.${cls} .report-list li .code`)].map(code=>code.textContent);
  const expected=key.reports['tdg-002'];
  assert.deepEqual(sorted(ids('report-built')),sorted(expected.built));
  assert.deepEqual(sorted(ids('report-other')),sorted(expected.sameIssuer));
  assert.deepEqual(sorted(ids('report-rest')),sorted(expected.otherIssuers));
});

test('Every report row shows the report’s declared acceptance state and qualification',async t=>{
  const w=screens(workspace,'W-Reports/list?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  await settle();
  const rows=new Map([...d.querySelectorAll('.report-list li')].map(li=>[li.querySelector('.code').textContent,li]));
  for(const [id,expected] of Object.entries(key.reports.byId)){
    const row=rows.get(id);
    assert.ok(row,`${id} has no row`);
    assert.ok(text(row).includes(expected.state),`${id}: ${expected.state} missing from "${text(row)}"`);
    assert.ok(text(row).includes(expected.qualification),`${id}: ${expected.qualification} missing from "${text(row)}"`);
  }
});

test('The reading toolbar shows the curated status with the acceptance state',async t=>{
  const toolbar=async id=>{
    const w=screens(workspace,`W-Reports/${id}?c=tdg-002`).window;t.after(()=>w.close());
    await settle();
    return text(w.document.querySelector('.report-tools'));
  };
  const latest=await toolbar('tdg-fy2024-snapshot-7');
  for(const part of [key.reports.status['tdg-fy2024-snapshot-7'],key.reports.byId['tdg-fy2024-snapshot-7'].state,key.reports.byId['tdg-fy2024-snapshot-7'].qualification])assert.ok(latest.includes(part),`${part} missing from "${latest}"`);
  assert.ok((await toolbar('tdg-fy2024-snapshot')).includes(key.reports.status['tdg-fy2024-snapshot']));
});

test('The reading toolbar separates the status from the acceptance badge',async t=>{
  const w=screens(workspace,'W-Reports/tdg-fy2024-snapshot-7?c=tdg-002').window;t.after(()=>w.close());
  await settle();
  const tools=w.document.querySelector('.report-tools'),sep=tools.querySelector('.tool-sep');
  assert.ok(sep,'no separator');
  assert.equal(sep.previousElementSibling.textContent,key.reports.status['tdg-fy2024-snapshot-7']);
  // The badge and its qualification text are one inline group, so they wrap as a unit.
  const group=sep.nextElementSibling;
  assert.ok(group.classList.contains('acceptance'));
  assert.ok(group.firstElementChild.classList.contains('badge'));
  assert.ok(group.querySelector('.muted').textContent.startsWith('Analytical qualification'));
  assert.equal(sep.getAttribute('aria-hidden'),'true');
});

test('A model source with no valid path or hash still renders, flagged, with no hash',async t=>{
  const forged=structuredClone(workspace);
  const model=forged.store.models.find(m=>m.id==='tdg-model-3');
  Object.assign(model.sources[0],{sha256:null,changed:null});
  const w=await forecastTab(forged,'tdg-002',t),d=w.document;
  const cells=[...d.querySelector('.forecast-built tbody tr').children];
  assert.equal(cells[3].textContent,'');
  assert.equal(text(cells[4]),'Invalid path or hash');
});

test('Each deliverable listed on the run overview shows its report’s state',async t=>{
  const w=screens(workspace,'W-Overview/overview?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  await settle();
  const entries=[...d.querySelectorAll('.summary-deliverables .deliverable')];
  const linked=entry=>entry.querySelector('a').getAttribute('href').split('?')[0].split('/').at(-1);
  assert.deepEqual(sorted(entries.map(linked)),sorted(key.reports['tdg-002'].built));
  for(const entry of entries){
    const id=linked(entry);
    const expected=key.reports.byId[id];
    assert.ok(expected,`${id} not in the answer key`);
    assert.ok(text(entry).includes(expected.state),`${id}: ${expected.state} missing from "${text(entry)}"`);
    assert.ok(text(entry).includes(expected.qualification),`${id}: qualification missing`);
  }
});

test('A synthetic delivery shows accepted, unrecorded and unknown states in exact words',async t=>{
  const forged=structuredClone(workspace);
  const [first,second,third]=forged.store.reports.filter(r=>r.issuerKey===forged.store.reports.find(x=>x.id==='tdg-fy2024-snapshot-7').issuerKey);
  Object.assign(first,{mode:'accepted',qualification:'qualified'});
  Object.assign(second,{mode:null,qualification:'mystery'});
  Object.assign(third,{mode:'draft',qualification:null});
  const w=screens(forged,'W-Reports/list?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  await settle();
  const row=r=>text([...d.querySelectorAll('.report-list li')].find(li=>li.querySelector('.code').textContent===r.id));
  assert.match(row(first),/Accepted.*Analytical qualification: qualified/);
  assert.doesNotMatch(row(first),/not accepted|not recorded/);
  assert.match(row(second),/Acceptance not recorded.*Analytical qualification not recorded/);
  assert.match(row(third),/Acceptance not recorded.*Analytical qualification not recorded/);
  const stateBadge=r=>[...d.querySelectorAll('.report-list li')].find(li=>li.querySelector('.code').textContent===r.id).querySelectorAll('.badge');
  const kinds=r=>[...stateBadge(r)].map(b=>`${text(b)}|${b.className}`);
  assert.ok(kinds(first).includes('Accepted|badge badge-gray'),kinds(first).join());
  assert.ok(kinds(second).includes('Acceptance not recorded|badge badge-gray'),kinds(second).join());
  assert.ok(kinds(third).includes('Acceptance not recorded|badge badge-gray'),kinds(third).join());
  const candidate=[...d.querySelectorAll('.report-list li .badge')].find(b=>text(b)==='Candidate · not accepted');
  assert.ok(candidate&&candidate.classList.contains('badge-gray'),'candidate state is a grey badge');
  assert.equal(d.querySelector('.report-list .badge-attention'),null,'no report row uses amber for acceptance');
});

// The Forecast tab, opened the way a reader opens it: from the run, through the tab.
const go=async(w,hash)=>{w.location.hash=hash;w.dispatchEvent(new w.Event('hashchange'));await settle();};
async function forecastTab(read,run,t){
  const w=screens(read,`W-Overview/overview?c=${run}`).window;t.after(()=>w.close());
  const tab=[...w.document.querySelectorAll('.workspace-tabs a')].find(a=>text(a)==='Forecast');
  assert.ok(tab,'no Forecast tab');
  await go(w,tab.getAttribute('href').slice(1));
  return w;
}
// Role words for the source roles a delivery declares, written here independently of the app.
const ROLE_WORDS={annual:'Annual handoff',quarter:'Quarterly handoff',forecast:'Forecast handoff',forecast_exact:'Forecast calculations',current_synthesis:'Current synthesis'};
const collapse=value=>value.replace(/\s+/g,' ').trim();

for(const [run,expected] of Object.entries(forecast.runs).filter(([,e])=>e.models.length)){
  test(`Forecast for ${run} shows its models, their state, why they were built and what they were built from`,async t=>{
    const w=await forecastTab(workspace,run,t),d=w.document;
    assert.deepEqual([...d.querySelectorAll('#model-select option')].map(o=>o.textContent),expected.options);
    assert.deepEqual([...d.querySelectorAll('#model-select option')].filter(o=>o.selected).map(o=>o.textContent),[expected.selected]);
    const tools=d.querySelector('.forecast-tools');
    assert.deepEqual([...tools.querySelectorAll('.badge')].map(b=>b.textContent),[expected.state]);
    assert.deepEqual([...tools.querySelectorAll('.muted')].map(b=>b.textContent),[expected.qualification]);
    assert.equal(text(tools.querySelector('a[download]')),'Download original HTML');
    assert.equal(d.querySelector('.forecast-scope').textContent,expected.scope);
    assert.equal(d.querySelector('.forecast-input').textContent,expected.inputContract);
    assert.equal(d.querySelector('.forecast-revision').textContent,expected.revisionNote);
    assert.deepEqual([...d.querySelectorAll('.forecast > section > h2')].map(text),['Cash flow model','Assumptions and their rationale','Model limitations','Why this model was built','Built from']);
    const assumptions=d.querySelector('.forecast-assumptions');
    assert.equal(assumptions.querySelector('h3').textContent,expected.registerHeading);
    assert.equal(collapse(assumptions.querySelector('.register-intro').textContent),expected.registerIntro);
    const rows=[...assumptions.querySelectorAll('tbody tr')].map(tr=>[...tr.children].map(c=>c.textContent));
    assert.deepEqual(rows.map(r=>r[0]),expected.registerIds);
    assert.deepEqual(rows,expected.registerRows);
    const built=[...d.querySelectorAll('.forecast-built tbody tr')];
    assert.deepEqual([...d.querySelectorAll('.forecast-built thead th')].map(text),['Role','Run','Source','SHA-256 prefix','Status']);
    assert.deepEqual(built.map(tr=>tr.querySelector('th').textContent),expected.builtFrom.map(b=>ROLE_WORDS[b.role]));
    built.forEach((tr,i)=>{
      const b=expected.builtFrom[i],cells=[...tr.querySelectorAll('td')],link=cells[1].querySelector('a');
      const runBadge=cells[0].querySelector('span.code');
      assert.ok(runBadge,`${b.role} has no run badge`);
      assert.equal(runBadge.textContent,b.path.split('/')[1],b.role);
      assert.equal(cells[2].textContent,b.sha256Prefix,b.role);
      assert.equal(text(cells[3]),b.changed?'Changed since publication':'Matches publication',b.role);
      assert.ok(cells[3].querySelector('.badge'),`${b.role} status is a badge`);
      assert.ok(cells[3].querySelector('.badge').classList.contains(b.changed?'badge-attention':'badge-gray'),b.role);
      if(b.output===null){assert.equal(link,null,`${b.role} must not link`);assert.equal(cells[1].textContent,b.path.split('/').at(-1),`${b.role} shows the file name, as a linked source does`);assert.equal(cells[1].querySelector('[title]')?.getAttribute('title'),b.path,`${b.role} keeps the full path in a title`);}
      else{assert.ok(link,`${b.role} has no link`);assert.equal(link.textContent,b.output.split('/').at(-1));}
    });
    // The sources come from different attempts, and the note says which files, as a fact.
    assert.equal(text(d.querySelector('.forecast-built .forecast-attempts')),'These files come from different attempts: CP-1-attempt-2.md (attempt 2), CP-2G-attempt-2.md (attempt 2), CP-2G-attempt-1-calculations.json (attempt 1)');
    assert.equal(d.querySelector('.forecast-built .table-scroll').nextElementSibling,d.querySelector('.forecast-attempts'));
    const frame=d.getElementById('model-preview');
    assert.equal(frame.getAttribute('sandbox'),'allow-scripts allow-downloads');
    assert.equal(frame.getAttribute('src'),null,'the frame has no address until the disclosure is opened');
    assert.match(frame.dataset.src,/^\/files\/deliverables\/tdg-model-3\/model\.html\?sha256=[0-9a-f]{64}&embedded=1$/);
    assert.ok(frame.dataset.src.includes(`sha256=${expected.modelSha256}`));
    // Each link opens the output it names, in the run that holds it.
    const open=async(link,output)=>{await go(w,link.getAttribute('href').slice(1));assert.equal(w.eval('current.output'),output);await go(w,`W-Forecast/forecast?c=${run}`);};
    await open(assumptions.querySelector('a.text-action'),expected.registerLinkOutput);
    assert.equal(text(assumptions.querySelector('a.text-action')),'Open the full forward credit model output');
    for(const [i,b] of expected.builtFrom.entries()){
      if(!b.output)continue;
      await open(d.querySelectorAll('.forecast-built tbody tr')[i].querySelector('td a'),b.output);
    }
  });
}

// The cash flow model, compared with the controller's frozen oracle (cashflow in the Forecast answer key).
const cashflow=forecast.cashflow;
test('Forecast for tdg-002 lays the calculation record out as a cash flow model',async t=>{
  const w=await forecastTab(workspace,'tdg-002',t),d=w.document;
  assert.equal(d.querySelector('#model-select').value,cashflow.model);
  const section=d.querySelector('.forecast-cashflow');
  assert.equal(section.querySelector('h2').textContent,'Cash flow model');
  assert.equal(section.querySelector('h2').nextElementSibling.textContent,cashflow.caption);
  const table=section.querySelector('table');
  const headRows=[...table.querySelectorAll('thead tr')];
  assert.deepEqual([...headRows[0].querySelectorAll('th[colspan]')].map(text),cashflow.groups);
  assert.deepEqual([...headRows[0].querySelectorAll('th[colspan]')].map(th=>Number(th.getAttribute('colspan'))),[2,3,3,3]);
  assert.deepEqual([...headRows[1].querySelectorAll('th')].map(text),cashflow.columns);
  // A year-to-date header puts "(YTD)" in its own span; the header text is unchanged.
  const ytd=[...headRows[1].querySelectorAll('th')].filter(th=>th.textContent.endsWith(' (YTD)'));
  assert.equal(ytd.length,2);
  ytd.forEach(th=>{assert.equal(th.querySelector('span.col-sub').textContent,'(YTD)');assert.equal(th.querySelectorAll('*').length,1);});
  const body=[...table.querySelectorAll('tbody tr')];
  assert.deepEqual(body.filter(tr=>tr.classList.contains('band-row')).map(text),cashflow.bands);
  const rows=body.filter(tr=>!tr.classList.contains('band-row'));
  assert.deepEqual(rows.map(tr=>text(tr.querySelector('th'))),cashflow.rows.map(r=>r.label));
  rows.forEach((tr,i)=>assert.deepEqual([...tr.querySelectorAll('td')].map(td=>td.textContent),cashflow.rows[i].display,cashflow.rows[i].label));
  // Each band heading sits directly before its first row.
  body.forEach((tr,i)=>{if(tr.classList.contains('band-row'))assert.equal(text(body[i+1].querySelector('th')),cashflow.rows.find(r=>r.band===text(tr)).label);});
  for(const [name,exact] of Object.entries(cashflow.titles)){
    const [label,column,group]=name.split('|');
    const row=rows.find(tr=>text(tr.querySelector('th'))===label);
    // A title key names its group only where the column label alone is not unique (the forecast years).
    const matches=cashflow.columns.map((c,i)=>c===column&&(group===undefined||cashflow.columnGroups[i]===group)?i:-1).filter(i=>i>=0);
    assert.equal(matches.length,1,`${name} must name exactly one column`);
    const index=matches[0];
    assert.equal(row.querySelectorAll('td')[index].getAttribute('title'),exact,name);
  }
  // The notes sit under the table, before the Not available lines.
  assert.deepEqual([...section.querySelectorAll('.cashflow-notes li')].map(li=>li.textContent),cashflow.notes);
  assert.equal(section.querySelector('.cashflow-notes').previousElementSibling,section.querySelector('.table-scroll'));
  assert.equal(section.querySelector('.cashflow-notes').nextElementSibling,section.querySelector('.cashflow-na'));
  assert.deepEqual([...section.querySelectorAll('.cashflow-na li')].map(text),cashflow.notAvailable);
  // The Not available lines sit in a disclosure, closed by default, whose summary counts them.
  const na=section.querySelector('.cashflow-na');
  assert.equal(na.tagName,'DETAILS');
  assert.equal(na.hasAttribute('open'),false);
  assert.equal(text(na.querySelector('summary')),`Why cells show n.a. (${cashflow.notAvailable.length} lines)`);
  assert.deepEqual([...section.querySelectorAll('tbody td')].filter(td=>td.textContent==='—'),[],'no cell shows a dash');
  // Totals: exactly the rows the key names carry total-row, in order.
  assert.deepEqual(rows.filter(tr=>tr.classList.contains('total-row')).map(tr=>text(tr.querySelector('th'))),cashflow.totals);
  // Every n.a. and n.m. cell states what it is; the label repeats the title's reason, the text stays the display.
  rows.forEach((tr,i)=>[...tr.querySelectorAll('td')].forEach((td,j)=>{
    const shown=cashflow.rows[i].display[j],at=`${cashflow.rows[i].label} / ${cashflow.columns[j]}`;
    if(shown==='n.a.')assert.equal(td.getAttribute('aria-label'),`n.a.: ${td.getAttribute('title')}`,at);
    else if(shown==='n.m.')assert.equal(td.getAttribute('aria-label'),'n.m.: not modelled in the calculation record',at);
    else assert.equal(td.hasAttribute('aria-label'),false,at);
  }));
  assert.ok(rows.some(tr=>[...tr.querySelectorAll('td')].some(td=>td.getAttribute('aria-label')==='n.m.: not modelled in the calculation record')));
  assert.deepEqual([...d.querySelectorAll('.forecast-limits li')].map(text),cashflow.limits);
  assert.equal(d.querySelector('.forecast-limits h2').textContent,'Model limitations');
});

for(const run of ['tdg-model-001','tdg-003'])test(`Forecast for ${run} shows the same model's cash flow caption and first row`,async t=>{
  const w=await forecastTab(workspace,run,t),d=w.document;
  assert.equal(d.querySelector('#model-select').value,cashflow.model);
  assert.equal(d.querySelector('.forecast-cashflow h2').nextElementSibling.textContent,cashflow.caption);
  const first=d.querySelector('.forecast-cashflow tbody tr:not(.band-row)');
  assert.equal(text(first.querySelector('th')),cashflow.rows[0].label);
  assert.deepEqual([...first.querySelectorAll('td')].map(td=>td.textContent),cashflow.rows[0].display);
});

test('A model with no calculation record says so in place of the table; hostile reasons and limits stay text',async t=>{
  const bad='<img src=x onerror=alert(1)>',quoted='x" onmouseover="alert(1)';
  const forged=structuredClone(workspace);
  const models=forged.store.models;
  const a=models.find(m=>m.id==='tdg-model-3'),b=models.find(m=>m.id==='tdg-model-2');
  b.cashflow=null;
  a.cashflow.limits=[bad];
  a.cashflow.notes=[bad];
  a.cashflow.rows[0].cells[1]={exact:null,display:'n.a.',reason:bad,status:'na'};
  a.cashflow.rows[0].cells[2]={exact:null,display:'n.a.',reason:quoted,status:'na'};
  a.cashflow.units=null;
  const w=await forecastTab(forged,'tdg-002',t),d=w.document;
  assert.equal(d.querySelector('.forecast-cashflow h2').nextElementSibling.textContent,'Units not recorded · Q1 FY2024 (YTD) to FY2027E · history as retained in the handoffs; forecasts are conditional illustrations from the calculation record');
  assert.equal(d.querySelector('.forecast-limits li').textContent,bad);
  assert.deepEqual([...d.querySelectorAll('.cashflow-notes li')].map(li=>li.textContent),[bad]);
  assert.deepEqual([...d.querySelectorAll('.cashflow-na li')].map(li=>li.textContent).slice(0,1),[`Not available: Power & Control — ${cashflow.columns[1]}: ${bad}`]);
  assert.equal(d.querySelectorAll('.cashflow td')[1].getAttribute('aria-label'),`n.a.: ${bad}`);
  // A quote in a reason must stay inside the one aria-label attribute: unescaped it would open an onmouseover attribute.
  const quotedCell=d.querySelectorAll('.cashflow td')[2];
  assert.equal(quotedCell.getAttribute('aria-label'),`n.a.: ${quoted}`);
  assert.equal(quotedCell.hasAttribute('onmouseover'),false);
  assert.deepEqual([...quotedCell.attributes].map(attr=>attr.name).sort(),['aria-label','class','title'].filter(n=>quotedCell.hasAttribute(n)).sort());
  assert.equal(d.querySelector('.forecast-cashflow img,.forecast-limits img'),null);
  assert.equal(d.querySelector('[onerror]'),null);
  const select=d.getElementById('model-select');
  select.value='tdg-model-2';select.dispatchEvent(new w.Event('change',{bubbles:true}));
  await settle();
  assert.equal(d.querySelector('.forecast-cashflow table'),null);
  assert.equal(d.querySelector('.forecast-cashflow p').textContent,'This model has no readable calculation record.');
  assert.equal(d.querySelector('.forecast-limits'),null);
});

test('Choosing another model in the Forecast tab shows that model',async t=>{
  const run='tdg-002',w=await forecastTab(workspace,run,t),d=w.document;
  const select=d.getElementById('model-select');
  select.value='tdg-model-1';select.dispatchEvent(new w.Event('change',{bubbles:true}));
  await settle();
  assert.equal(d.getElementById('model-select').selectedOptions[0].textContent,forecast.runs[run].options[2]);
  assert.match(d.getElementById('model-preview').dataset.src,/tdg-model-1\/model\.html/);
});

for(const [run,expected] of Object.entries(forecast.runs).filter(([,e])=>!e.models.length)){
  test(`Forecast for ${run} says no model was published from its files and lists the issuer's other models`,async t=>{
    const w=await forecastTab(workspace,run,t),d=w.document;
    assert.equal(d.querySelector('#content .missing-state h2').textContent,forecast.emptyHeading);
    assert.equal(d.getElementById('model-select'),null);
    assert.equal(d.getElementById('model-preview'),null);
    const others=d.querySelector('.forecast-other');
    if(expected.otherHeading===null){assert.equal(others,null);return;}
    assert.equal(others.querySelector('h2').textContent,expected.otherHeading);
    assert.deepEqual([...others.querySelectorAll('li > a, li > span:first-child')].map(e=>e.textContent),expected.others);
  });
}

test('Ratio titles show four decimals, with the approximation sign only where rounding changed the value',async t=>{
  const forged=structuredClone(workspace);
  const model=forged.store.models.find(m=>m.id==='tdg-model-3');
  const percent=model.cashflow.rows.find(r=>r.kind==='percent'),multiple=model.cashflow.rows.find(r=>r.kind==='multiple'),money=model.cashflow.rows.find(r=>r.kind==='money');
  const set=(row,i,exact)=>{row.cells[i]={exact,display:'shown',reason:null,status:'value'};};
  const cases=[[percent,'0.5','50.0000%'],[percent,'0.123456789','≈ 12.3457%'],[percent,'-0.12345','-12.3450%'],[percent,'-0.0000000001','≈ 0.0000%'],[percent,'1E-4','0.0100%'],[multiple,'4.79755','≈ 4.7976x'],[multiple,'3','3.0000x'],[money,'1221.04741248','1221.04741248']];
  cases.forEach(([row,exact],i)=>set(row,i,exact));
  const w=await forecastTab(forged,'tdg-002',t),d=w.document;
  const rows=[...d.querySelectorAll('.cashflow tbody tr:not(.band-row)')];
  cases.forEach(([row,exact,title],i)=>{
    const tr=rows.find(r=>text(r.querySelector('th'))===row.label);
    assert.equal(tr.querySelectorAll('td')[i].getAttribute('title'),title,`${row.label} ${exact}`);
  });
});

test('Built from names an unknown role by its token and adds no attempt note when the files share an attempt',async t=>{
  const forged=structuredClone(workspace);
  const model=forged.store.models.find(m=>m.id==='tdg-model-3');
  model.sources[0].role='<b>mystery</b>';
  for(const s of model.sources)if(s.path)s.path=s.path.replace(/-attempt-\d+/,'-attempt-2');
  const w=await forecastTab(forged,'tdg-002',t),d=w.document;
  assert.equal(d.querySelector('.forecast-built tbody th').textContent,'<b>mystery</b>');
  assert.equal(d.querySelector('.forecast-built tbody th b'),null);
  assert.equal(d.querySelector('.forecast-attempts'),null);
});

test('A report whose qualification is unrun reads "not run" and no acceptance badge is amber',async t=>{
  const forged=structuredClone(workspace);
  const report=forged.store.reports.find(r=>r.qualification==='unrun');
  assert.ok(report,'the workspace holds an unrun report');
  const w=screens(forged,'W-Reports/list?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  await settle();
  const row=[...d.querySelectorAll('.report-list li')].find(li=>li.querySelector('.code').textContent===report.id);
  assert.match(text(row),/Analytical qualification: not run/);
  assert.doesNotMatch(text(row),/unrun/);
  assert.equal(d.querySelector('.badge-attention'),null);
});

test('Model text from a workspace stays text, and a source that changed says so',async t=>{
  const bad='<img src=x onerror=alert(1)>',forged=structuredClone(workspace);
  const model=forged.store.models.find(m=>m.id==='tdg-model-3');
  model.scope=bad;model.revisionNote=bad;model.register.rows[0][1]=bad;model.sources[0].changed=true;
  const w=await forecastTab(forged,'tdg-002',t),d=w.document;
  assert.equal(d.querySelector('.forecast-scope').textContent,bad);
  assert.equal(d.querySelector('.forecast-revision').textContent,`Revision note: ${bad}`);
  assert.equal(d.querySelector('.forecast-assumptions tbody tr').children[1].textContent,bad);
  assert.equal(d.querySelector('#content img[src="x"]'),null);
  assert.equal(d.querySelector('#content [onerror]'),null);
  const status=[...d.querySelectorAll('.forecast-built tbody tr')].map(tr=>text(tr.children[4]));
  assert.equal(status[0],'Changed since publication');
  assert.deepEqual(status.slice(1),Array(4).fill('Matches publication'));
});

test('The model frame is not loaded or watched until its disclosure is opened, then shows loading and the failure with a download link',async t=>{
  const w=screens(workspace,'W-Overview/overview?c=tdg-002').window;t.after(()=>w.close());
  w.DESIGN_FRAME_TIMEOUT_MS=20;
  await go(w,'W-Forecast/forecast?c=tdg-002');
  const d=w.document,details=d.querySelector('details.model-original'),frame=d.getElementById('model-preview'),status=details.querySelector('.frame-status');
  assert.equal(details.open,false);
  assert.equal(text(details.querySelector('summary')),'Published model (original HTML)');
  assert.equal(frame.closest('details'),details);
  assert.equal(frame.getAttribute('src'),null);
  await settle(80);
  assert.equal(status.hidden,true,'no watch has started');
  assert.equal(text(status),'');
  details.open=true;
  await until(()=>frame.getAttribute('src'),'the frame never got its address',2000);
  assert.equal(frame.getAttribute('src'),frame.dataset.src);
  await until(()=>/did not load/.test(status.textContent),'the model frame never reported failure',2000);
  assert.match(text(status),/^The model did not load\. Download original HTML Retry$/);
  assert.match(status.querySelector('a').getAttribute('href'),/model\.html\?sha256=[0-9a-f]{64}&download=1$/);
  frame.dispatchEvent(new w.Event('load'));
  assert.equal(status.hidden,true);
  // Closing and opening again does not start a second watch or reset the address.
  const src=frame.getAttribute('src');details.open=false;await settle(30);details.open=true;await settle(30);
  assert.equal(frame.getAttribute('src'),src);
});

// Security review M1/M2/P1: a model or report id reaches the address as one encoded section and is read back exactly.
const HOSTILE='x"><b id=pwn>Continue';
function renamed(from,to){
  const forged=structuredClone(workspace),model=forged.store.models.find(m=>m.id===from);
  assert.ok(model,`no model ${from}`);model.id=to;
  for(const other of forged.store.models)if(other.previous===from)other.previous=to;
  return forged;
}
test('A model id with markup in it renders no element of its own on Overview, Forecast, Library and Settings',async t=>{
  const forged=renamed('tdg-model-3',HOSTILE);
  for(const hash of ['W-Overview/overview?c=tdg-002','W-Forecast/forecast?c=tdg-002','W-Library/cases','W-Settings/workspace']){
    const w=screens(forged,hash).window,d=w.document;t.after(()=>w.close());
    await settle();
    assert.equal(d.querySelector('[id^=pwn]'),null,hash);
  }
  const w=await forecastTab(forged,'tdg-002',t),d=w.document;
  assert.equal(d.querySelector('[id^=pwn]'),null,'Forecast tab');
  assert.ok([...d.querySelectorAll('a')].some(a=>a.getAttribute('href')===`#W-Forecast/${encodeURIComponent(HOSTILE)}?c=tdg-002`||a.getAttribute('href').startsWith(`#W-Forecast/${encodeURIComponent(HOSTILE)}`)),'the id is one encoded section');
});
test('Catalogue text with markup in it renders no element of its own in the rows or the selected run',t=>{
  const forged=structuredClone(workspace),run=forged.catalogue.real.find(r=>r.id==='tdg-002');
  for(const field of ['name','title','issuer','sector','workflow','summary','period'])run[field]=HOSTILE;
  run.gaps=[HOSTILE];run.ratings=[{label:HOSTILE,date:HOSTILE,source:''}];run.artifacts[0].label=HOSTILE;run.artifacts[0].issue=HOSTILE;
  run.metrics.leverage.basis=HOSTILE;run.metrics.leverage.source='s"><b id=pwn2>';
  forged.catalogue.sources={'s"><b id=pwn2>':{path:HOSTILE,line:1,quote:HOSTILE,href:HOSTILE}};
  const w=screens(forged,'W-Library/cases').window,d=w.document;t.after(()=>w.close());
  d.querySelector('[data-library-select="tdg-002"]').click();
  assert.equal(d.querySelector('[id^=pwn]'),null);
  assert.ok(text(d.getElementById('run-detail')).includes(HOSTILE),'shown as text');
});
test('A report id with markup in it renders no element of its own',async t=>{
  const forged=structuredClone(workspace);
  forged.store.reports[0].id=HOSTILE;
  for(const hash of ['W-Library/cases','W-Reports/list?c=tdg-002','W-Overview/overview?c=tdg-002']){
    const w=screens(forged,hash).window,d=w.document;t.after(()=>w.close());
    await settle();
    assert.equal(d.querySelector('[id^=pwn]'),null,hash);
  }
});
for(const id of ['m é 1','a%20b','Société modèle','a/b?c=1#x']){
  test(`A model id "${id}" chosen in the Model select shows that model`,async t=>{
    const forged=renamed('tdg-model-1',id),want=forged.store.models.find(m=>m.id===id);
    const w=await forecastTab(forged,'tdg-002',t),d=w.document;
    const select=d.getElementById('model-select');
    select.value=id;select.dispatchEvent(new w.Event('change',{bubbles:true}));
    await settle();
    assert.equal(d.getElementById('model-select').value,id);
    assert.match(d.getElementById('model-preview').dataset.src,new RegExp(want.href.split('?')[0].replace(/[.*+?^${}()|[\]\\]/g,'\\$&')));
    assert.equal(d.querySelector('.forecast-scope')?.textContent??null,want.scope);
    const again=w.eval('parseRoute()');
    assert.equal(again.section,id);
  });
}
test('A malformed escape in the section is an unknown section, never an error',async t=>{
  const w=screens(workspace,'W-Overview/overview?c=tdg-002').window;t.after(()=>w.close());
  w.location.hash='#W-Forecast/%E0%A4%A?c=tdg-002';
  const route=w.eval('parseRoute()');
  assert.equal(route.module,'W-Forecast');
  assert.notEqual(route.section,'%E0%A4%A');
});

test('The Forecast tab opens the default model: not superseded, preferring one that records a predecessor',async t=>{
  // tdg-model-2 records tdg-model-1; the latest folder, tdg-model-3, records none: the rule, not the folder name, decides.
  const forged=structuredClone(workspace),by=id=>forged.store.models.find(m=>m.id===id);
  by('tdg-model-3').previous=null;by('tdg-model-2').previous='tdg-model-1';by('tdg-model-1').previous=null;
  const w=await forecastTab(forged,'tdg-002',t),d=w.document;
  assert.equal(d.getElementById('model-select').value,'tdg-model-2');
  assert.deepEqual([...d.querySelectorAll('#model-select option')].map(o=>o.value),['tdg-model-2','tdg-model-3','tdg-model-1']);
});

// Hand-written store in the shape /api/workspace sends: outputs carry a digest, the sections are sent once per digest.
function loadHydrate(){const context=vm.createContext({});vm.runInContext(fs.readFileSync(path.join(__dirname,'hydrate.js'),'utf8'),context);return vm.runInContext('hydrate',context);}
test('hydrate gives every output the sections of its own hash',()=>{
  const hydrate=loadHydrate();
  const a=[{heading:'A',level:1,line:1,blocks:[]}],b=[{heading:'B',level:1,line:1,blocks:[]}];
  const data={runs:{},inputs:{},pins:{},handoffs:{aa:a,bb:b},outputs:{
    'r1/CP-1.md':{id:'r1/CP-1.md',sha256:'aa'},'r2/CP-1.md':{id:'r2/CP-1.md',sha256:'aa'},'r2/CP-2.md':{id:'r2/CP-2.md',sha256:'bb'}}};
  assert.equal(hydrate(data),data);
  assert.equal(data.outputs['r1/CP-1.md'].sections[0].heading,'A');
  assert.equal(data.outputs['r2/CP-1.md'].sections[0].heading,'A');
  assert.equal(data.outputs['r2/CP-2.md'].sections[0].heading,'B');
});
test('hydrate refuses an output whose handoff was not sent',()=>{
  const hydrate=loadHydrate();
  assert.throws(()=>hydrate({outputs:{'r1/CP-1.md':{id:'r1/CP-1.md',sha256:'zz'}},handoffs:{}}),/r1\/CP-1\.md/);
});

test('The cash flow table is a labelled scroll region with ruled column groups and quiet scenario cells',async t=>{
  const w=await forecastTab(workspace,'tdg-002',t),d=w.document;
  const region=d.querySelector('.forecast-cashflow .table-scroll'),h2=d.querySelector('.forecast-cashflow h2');
  assert.equal(region.getAttribute('role'),'region');
  assert.equal(region.getAttribute('tabindex'),'0');
  assert.equal(region.getAttribute('aria-labelledby'),h2.id);
  assert.ok(h2.id);
  const names=cashflow.groups;
  const first=d.querySelector('.cashflow tbody tr:not(.band-row)');
  const cells=[...first.querySelectorAll('td')],columns=cashflow.columns;
  assert.equal(cells.length,columns.length);
  const starts=cells.map(c=>c.classList.contains('group-start'));
  assert.equal(starts.filter(Boolean).length,names.length,'one ruled first column per group');
  assert.equal(starts[0],true);
  const scenario=cells.map(c=>c.classList.contains('scenario'));
  assert.ok(scenario.some(Boolean)&&scenario.some(v=>!v),'some cells are scenario columns and some are not');
  // jsdom does not resolve var(), so each token the cash flow rules read is replaced by the value screen.css defines it with.
  const css=fs.readFileSync(path.join(__dirname,'screen.css'),'utf8'),token=name=>css.match(new RegExp(`${name}:(#[0-9a-f]{6})`))[1];
  const sheet=[...css.matchAll(/\.cashflow[^{]*\{[^}]*\}/g)].map(m=>m[0]).join('\n').replaceAll('var(--rule)',token('--rule')).replaceAll('var(--quiet)',token('--quiet'));
  const style=d.createElement('style');style.textContent=sheet;d.head.append(style);
  const cs=w.getComputedStyle(cells[starts.indexOf(true)]);
  assert.equal(w.getComputedStyle(cells[0]).height,'32px');
  assert.equal(w.getComputedStyle(first.querySelector('th')).minWidth,'12rem');
  const startCell=cells.find(c=>c.classList.contains('group-start'));
  assert.match(w.getComputedStyle(startCell).borderLeft,/^1px solid (rgb\(221, 225, 234\)|#dde1ea)$/);
  assert.equal(cs.paddingTop,'5px');
  const quiet=cells.find(c=>c.classList.contains('scenario'));
  assert.equal(w.getComputedStyle(quiet).backgroundColor,'rgb(246, 247, 250)');
  assert.equal(w.getComputedStyle(cells.find(c=>!c.classList.contains('scenario'))).backgroundColor,'rgba(0, 0, 0, 0)');
});

test('The section pager names models on Forecast and reports on Reports, and sections elsewhere',async t=>{
  const w=await forecastTab(workspace,'tdg-002',t),d=w.document;
  assert.equal(d.getElementById('previous-section').getAttribute('aria-label'),'Previous model');
  assert.equal(d.getElementById('next-section').getAttribute('aria-label'),'Next model');
  await go(w,'W-Reports/list?c=tdg-002');
  assert.equal(d.getElementById('previous-section').getAttribute('aria-label'),'Previous report');
  assert.equal(d.getElementById('next-section').getAttribute('aria-label'),'Next report');
  // An analytical module with several sections keeps the default labels.
  await go(w,'CP-1/summary?c=tdg-002');
  assert.equal(d.getElementById('previous-section').getAttribute('aria-label'),'Previous section');
  assert.equal(d.getElementById('next-section').getAttribute('aria-label'),'Next section');
});

test('Help explains run notices, resuming a stopped run and n.a. and n.m. in the cash flow model',t=>{
  const w=screens(workspace,'W-Help/help').window,d=w.document;t.after(()=>w.close());
  const heads=[...d.querySelectorAll('.help-copy h2')].map(text);
  for(const name of ['Run notices','Resuming a stopped run','n.a. and n.m. in the cash flow model'])assert.ok(heads.includes(name),name);
  const body=name=>text([...d.querySelectorAll('.help-copy h2')].find(h=>text(h)===name).nextElementSibling);
  const notices=body('Run notices');
  for(const state of ['running','complete','stopped','failed','interrupted'])assert.match(notices,new RegExp(state),state);
  assert.match(notices,/Dismiss/);
  assert.match(notices,/Resume appears on stopped, failed or interrupted notices, except a run stopped by a provider ruling\./);
  assert.equal(body('Resuming a stopped run'),'A run started from New run that stopped, failed or was interrupted can be resumed from its notice, from Run activity or from Recent runs. The resumed run is a new run: it keeps the accepted modules without a new model call and has its own spending cap, and what the stopped run spent is not counted against it. A run stopped by a provider ruling cannot be resumed.');
  const na=body('n.a. and n.m. in the cash flow model');
  assert.match(na,/n\.a\. means not available/);assert.match(na,/Why cells show n\.a\./);assert.match(na,/never zero/);assert.match(na,/n\.m\. means not modelled/);
});

test('An Other models row opens the model under the run it was published for, not an earlier run that only supplied files',async t=>{
  const w=await forecastTab(workspace,'tdg-run-comparison',t),d=w.document;
  const keys=w.eval('Object.keys(contexts)'),folderOf=k=>w.eval(`contexts[${JSON.stringify(k)}].folder`);
  const issuer=w.eval('contexts["tdg-run-comparison"].issuerKey');
  const same=keys.filter(k=>w.eval(`contexts[${JSON.stringify(k)}].issuerKey`)===issuer&&k!=='tdg-run-comparison');
  const supplier=same[0],owner=same.at(-1);
  assert.notEqual(supplier,owner);
  const base=JSON.parse(JSON.stringify(w.DESIGN_WORKSPACE.models[0]));
  base.id='zz-owned-model';base.issuerKey=issuer;base.runId=folderOf(owner);base.sources=[{...base.sources[0],run:supplier}];
  w.DESIGN_WORKSPACE.models.splice(0,w.DESIGN_WORKSPACE.models.length,base);
  await go(w,'W-Library/cases');await go(w,'W-Forecast/forecast?c=tdg-run-comparison');
  const link=d.querySelector('.forecast-other li a');
  assert.ok(link,'the row links');
  assert.equal(new URLSearchParams(link.getAttribute('href').split('?')[1]).get('c'),owner);
});
