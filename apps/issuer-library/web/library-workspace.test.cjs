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
  const child=spawn(binary(temp),['--workspace',repo,'--state-dir',path.join(temp,'state'),'--no-browser','--port',String(port)],{env,stdio:['ignore','ignore','pipe']});
  let exited=null,stderr='';child.stderr.on('data',chunk=>{stderr+=chunk;});
  const gone=new Promise(resolve=>child.on('exit',code=>{exited=code;resolve();}));
  try{
    await until(async()=>(await fetch(`${base}/health`)).ok,'server not serving',30000,()=>exited===null?null:`server exited ${exited}: ${stderr}`);
    const read=async url=>{const response=await fetch(base+url,{cache:'no-store'});if(!response.ok)assert.fail(`${url}: ${response.status} ${await response.text()}`);return response.json();};
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
  w.DESIGN_DATA={runs:store.runs,outputs:store.outputs,inputs:store.inputs,pins:store.pins};
  w.DESIGN_WORKSPACE={reports:store.reports,models:store.models,visuals:store.visuals};
  w.DESIGN_APP={workspace:catalogue.workspace||'',policy_locked:!!catalogue.policy_locked,issues:store.issues,problem:''};
  for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());
  return dom;
}
const runKey=a=>new URLSearchParams(a.getAttribute('href').split('?')[1]).get('c');
const sorted=list=>[...list].sort();
const renderedKeys=d=>sorted([...d.querySelectorAll('#library-results a.run-link')].map(runKey));

let workspace;
test.before(async()=>{workspace=await readWorkspace();});

test('Library groups the retained workspace by issuer and counts it as the answer key does',t=>{
  const w=screens(workspace,'W-Library/cases').window,d=w.document;t.after(()=>w.close());
  assert.equal(text(d.getElementById('library-count')),key.library.count);
  const groups=[...d.querySelectorAll('#library-results tbody.run-list')];
  assert.deepEqual(groups.map(g=>text(g.querySelector('h2'))),key.library.groups.map(g=>g[0]));
  groups.forEach((group,i)=>{
    assert.deepEqual(sorted([...group.querySelectorAll('a.run-link')].map(runKey)),sorted(key.library.groups[i][1]),key.library.groups[i][0]);
  });
});

test('A run recorded under another name says so, and only that run',t=>{
  const w=screens(workspace,'W-Library/cases').window,d=w.document;t.after(()=>w.close());
  const seen=new Set();
  for(const link of d.querySelectorAll('#library-results a.run-link')){
    const id=runKey(link),row=link.closest('tr'),line=row.querySelector('.recorded-as');
    seen.add(id);
    if(Object.hasOwn(key.library.recordedAs,id))assert.equal(line&&text(line),key.library.recordedAs[id],id);
    else assert.doesNotMatch(text(row),/Recorded as/,id);
  }
  for(const id of Object.keys(key.library.recordedAs))assert.ok(seen.has(id),`${id} not rendered`);
});

test('Library search finds every run of the issuer searched',t=>{
  const w=screens(workspace,'W-Library/cases').window,d=w.document;t.after(()=>w.close());
  const box=d.getElementById('library-query');
  for(const [query,expected] of Object.entries(key.library.search)){
    box.value=query;box.dispatchEvent(new w.Event('input',{bubbles:true}));
    assert.deepEqual(renderedKeys(d),sorted(expected),`search "${query}"`);
  }
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
  assert.ok(sep.nextElementSibling.classList.contains('badge'));
  assert.equal(sep.getAttribute('aria-hidden'),'true');
});

test('A model source with no valid path or hash still renders, flagged, with no hash',async t=>{
  const forged=structuredClone(workspace);
  const model=forged.store.models.find(m=>m.id==='tdg-model-3');
  Object.assign(model.sources[0],{sha256:null,changed:null});
  const w=await forecastTab(forged,'tdg-002',t),d=w.document;
  const cells=[...d.querySelector('.forecast-built tbody tr').children];
  assert.equal(cells[2].textContent,'');
  assert.equal(text(cells[3]),'Invalid path or hash');
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
  assert.ok(candidate&&candidate.classList.contains('badge-attention'),'candidate state is an attention badge');
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
    assert.deepEqual([...d.querySelectorAll('.forecast > section > h2')].map(text),['Why this model was built','Assumptions and their rationale','Built from']);
    const assumptions=d.querySelector('.forecast-assumptions');
    assert.equal(assumptions.querySelector('h3').textContent,expected.registerHeading);
    assert.equal(collapse(assumptions.querySelector('.register-intro').textContent),expected.registerIntro);
    const rows=[...assumptions.querySelectorAll('tbody tr')].map(tr=>[...tr.children].map(c=>c.textContent));
    assert.deepEqual(rows.map(r=>r[0]),expected.registerIds);
    assert.deepEqual(rows,expected.registerRows);
    const built=[...d.querySelectorAll('.forecast-built tbody tr')];
    assert.deepEqual(built.map(tr=>tr.querySelector('th').textContent),expected.builtFrom.map(b=>b.role));
    built.forEach((tr,i)=>{
      const b=expected.builtFrom[i],cells=[...tr.querySelectorAll('td')],link=cells[0].querySelector('a');
      assert.equal(cells[1].textContent,b.sha256Prefix,b.role);
      assert.equal(text(cells[2]).includes('Changed since publication'),b.changed,b.role);
      if(b.output===null){assert.equal(link,null,`${b.role} must not link`);assert.equal(cells[0].textContent,b.path);}
      else{assert.ok(link,`${b.role} has no link`);assert.equal(link.textContent,b.output.split('/').at(-1));}
    });
    const frame=d.getElementById('model-preview');
    assert.equal(frame.getAttribute('sandbox'),'allow-scripts allow-downloads');
    assert.match(frame.getAttribute('src'),/^\/files\/deliverables\/tdg-model-3\/model\.html\?sha256=[0-9a-f]{64}&embedded=1$/);
    assert.ok(frame.getAttribute('src').includes(`sha256=${expected.modelSha256}`));
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

test('Choosing another model in the Forecast tab shows that model',async t=>{
  const run='tdg-002',w=await forecastTab(workspace,run,t),d=w.document;
  const select=d.getElementById('model-select');
  select.value='tdg-model-1';select.dispatchEvent(new w.Event('change',{bubbles:true}));
  await settle();
  assert.equal(d.getElementById('model-select').selectedOptions[0].textContent,forecast.runs[run].options[2]);
  assert.match(d.getElementById('model-preview').getAttribute('src'),/tdg-model-1\/model\.html/);
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
  const status=[...d.querySelectorAll('.forecast-built tbody tr')].map(tr=>text(tr.children[3]));
  assert.equal(status[0],'Changed since publication');
  assert.deepEqual(status.slice(1),['','','','']);
});

test('The model frame shows loading, then the failure with a download link when the page never arrives',async t=>{
  const w=screens(workspace,'W-Overview/overview?c=tdg-002').window;t.after(()=>w.close());
  w.DESIGN_FRAME_TIMEOUT_MS=20;
  await go(w,'W-Forecast/forecast?c=tdg-002');
  const status=w.document.querySelector('.forecast .frame-status');
  assert.equal(text(status),'Loading model…');
  await until(()=>/did not load/.test(status.textContent),'the model frame never reported failure',2000);
  assert.match(text(status),/^The model did not load\. Download original HTML Retry$/);
  assert.match(status.querySelector('a').getAttribute('href'),/model\.html\?sha256=[0-9a-f]{64}&download=1$/);
  w.document.getElementById('model-preview').dispatchEvent(new w.Event('load'));
  assert.equal(status.hidden,true);
});
