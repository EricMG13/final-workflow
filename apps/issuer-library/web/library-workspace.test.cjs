/* The Library and Reports screens over the real retained workspace, read through the real app and compared with the frozen answer key. No provider is started. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path'),vm=require('node:vm'),net=require('node:net');
const {spawn,spawnSync}=require('node:child_process');
const {JSDOM}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const app=path.resolve(__dirname,'..'),repo=path.resolve(app,'../..');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const key=JSON.parse(fs.readFileSync(path.join(app,'designs/library-answer-key.json'),'utf8'));
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
async function until(check,what,ms=30000){
  const end=Date.now()+ms;
  for(;;){
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
  const child=spawn(binary(temp),['--workspace',repo,'--state-dir',path.join(temp,'state'),'--no-browser','--port',String(port)],{env,stdio:'ignore'});
  let exited=null;child.on('exit',code=>{exited=code;});
  try{
    await until(async()=>{if(exited!==null)throw new Error(`server exited ${exited}`);return (await fetch(`${base}/health`)).ok;},'server not serving');
    const read=async url=>{const response=await fetch(base+url,{cache:'no-store'});if(!response.ok)assert.fail(`${url}: ${response.status} ${await response.text()}`);return response.json();};
    const catalogue=await read('/api/catalogue'),store=await read('/api/workspace');
    return {catalogue,store};
  }finally{
    child.kill();
    await new Promise(resolve=>{if(exited!==null)resolve();else child.on('exit',resolve);});
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
  w.DESIGN_WORKSPACE={reports:store.reports,visuals:store.visuals};
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

test('Each deliverable listed on the run overview shows its report’s state',async t=>{
  const w=screens(workspace,'W-Overview/overview?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  await settle();
  const entries=[...d.querySelectorAll('.summary-deliverables .deliverable')];
  assert.equal(entries.length,key.reports['tdg-002'].built.length);
  for(const entry of entries){
    const id=entry.querySelector('a').getAttribute('href').split('?')[0].split('/').at(-1);
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
