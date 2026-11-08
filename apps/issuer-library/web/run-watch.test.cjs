/* The app-wide run watcher: title mark, rail mark, finish notification, stop sentences and turn text.
   jsdom with fake timers, fetch and Notification; synthetic job lists only; no network or provider. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const {JSDOM,VirtualConsole}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const settle=()=>new Promise(resolve=>setTimeout(resolve,10));
const ID='web-'+'a'.repeat(32);
const MODULES=['CP-0','CP-1','CP-2','CP-3'];
const job=(over={})=>({id:ID,state:'running',message:'Working',run_available:true,issuer:'Northbridge Group',pathway:'covenant_refinancing',as_of:'2025-03-31',modules:MODULES,module_details:MODULES.map(id=>({id,title:'Title '+id})),progress:{module:'CP-2',step:'running',turn:2,max_turns:24,spent_usd:'0.42',held_usd:'1.86',cap_usd:'10.00',accepted:2},...over});
async function page(t,{permission='granted',list=[]}={}){
  const errors=[],built=[];const virtualConsole=new VirtualConsole();virtualConsole.on('jsdomError',error=>errors.push(error));
  const dom=new JSDOM(html,{url:'http://127.0.0.1:54321/#W-Library/cases',runScripts:'outside-only',virtualConsole});
  const win=dom.window;win.scrollTo=()=>{};win.focus=()=>{};win.HTMLElement.prototype.scrollIntoView=function(){};
  const timers=new Map(),cleared=[];let next=1;
  win.setInterval=(fn,ms)=>{timers.set(next,{fn,ms});return next++;};win.clearInterval=id=>{cleared.push(id);timers.delete(id);};
  win.Notification=class{static permission=permission;static requestPermission=async()=>permission;constructor(title,options){this.title=title;this.options=options;built.push(this);}};
  const state={list};
  win.fetch=async url=>({ok:true,json:async()=>url.split('?')[0]==='/api/runs/list'?state.list:{}});
  win.eval('window.DESIGN_DATA={runs:{},outputs:{},inputs:{},pins:{}};window.DESIGN_WORKSPACE={reports:[],models:[],visuals:[]};window.DESIGN_APP={workspace:"/research",policy_locked:false,issues:[],problem:""};');
  for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());
  await settle();
  t.after(()=>{win.close();assert.deepEqual(errors.map(error=>error.message),[]);});
  const doc=win.document;
  return{win,doc,built,state,timers,cleared,mark:()=>vm.runInContext('runMark',dom.getInternalVMContext()),
    watch:async()=>{await win.watchRuns();await settle();},
    tick:async()=>{for(const {fn} of [...timers.values()])fn();await settle();},
    go:async hash=>{win.location.hash=hash;await settle();}};
}
test('a run that finishes while the Library is open notifies once with the run id as tag',async t=>{
  const p=await page(t,{list:[job()]});
  await p.watch();assert.equal(p.built.length,0);
  p.state.list=[job({state:'complete',message:'Done',spent_usd:'3.10'})];
  await p.watch();await p.watch();
  assert.equal(p.built.length,1);
  assert.equal(p.built[0].title,'Issuer Library');
  assert.deepEqual({...p.built[0].options},{body:'Northbridge Group run complete',tag:ID});
  let reloaded=0;p.win.reloadApp=()=>{reloaded++;};
  p.built[0].onclick();
  assert.equal(p.win.location.hash,`#W-Reports/list?c=${ID}`);assert.equal(reloaded,1);
});
test('a run already finished at load sets no mark and no notification',async t=>{
  const p=await page(t,{list:[job({state:'complete',spent_usd:'3.10'})]});
  await p.watch();
  assert.equal(p.mark(),'');assert.equal(p.built.length,0);
  assert.equal(p.doc.getElementById('run-mark').hidden,true);
});
test('the title carries the run mark on every route and clears with no job',async t=>{
  const p=await page(t,{list:[job()]});
  await p.watch();
  assert.equal(p.mark(),'● 2/4 · ');
  for(const [hash,name] of [['#W-Library/cases','Issuer library'],['#W-Settings/workspace','Settings'],['#W-Help/help','Help']]){
    await p.go(hash);
    assert.equal(p.doc.title,`● 2/4 · ${name} · Issuer Library`,hash);
  }
  const rail=p.doc.getElementById('run-mark');
  assert.equal(rail.hidden,false);assert.equal(rail.textContent,'●');
  assert.equal(rail.getAttribute('aria-label'),'Run running, 2 of 4 modules');
  assert.equal(rail.closest('a').getAttribute('href'),'#CP-OS/activity');
  p.state.list=[job({state:'stopped',reason:'budget'})];
  await p.watch();
  assert.equal(p.doc.title,'! Help · Issuer Library');assert.equal(rail.getAttribute('aria-label'),'Run stopped');
  p.state.list=[job({state:'complete'})];await p.watch();
  assert.equal(p.doc.title,'✓ Help · Issuer Library');
  p.state.list=[];await p.watch();
  // a finished job leaves the list; the page keeps describing the run it saw finish
  assert.equal(p.mark(),'✓ ');
});
test('no job at all leaves the title unmarked',async t=>{
  const p=await page(t,{list:[]});
  await p.watch();await p.go('#W-Help/help');
  assert.equal(p.mark(),'');assert.equal(p.doc.title,'Help · Issuer Library');
});
test('a job without modules shows the mark without a count',async t=>{
  const p=await page(t,{list:[job({modules:undefined,module_details:undefined})]});
  await p.watch();
  assert.equal(p.mark(),'● ');
  assert.equal(p.doc.getElementById('run-mark').getAttribute('aria-label'),'Run running');
});
test('no notification is created without permission',async t=>{
  for(const permission of ['denied','default']){
    const p=await page(t,{permission,list:[job()]});
    await p.watch();p.state.list=[job({state:'failed',reason:'provider'})];await p.watch();
    assert.equal(p.built.length,0,permission);
    assert.equal(p.mark(),'! ');
  }
});
test('polling stops when no run is active',async t=>{
  const p=await page(t,{list:[job()]});
  await p.watch();
  assert.deepEqual([...p.timers.values()].map(item=>item.ms),[5000]);
  await p.watch();assert.equal(p.timers.size,1);
  p.state.list=[job({state:'complete'})];
  await p.tick();
  assert.equal(p.timers.size,0);assert.equal(p.cleared.length,1);
  assert.equal(p.built.length,1);
});
test('a stopped run leads with the sentence for its reason',async t=>{
  const rows=[
    ['budget','stopped','Stopped: the next model call would pass the spending cap; a new run needs a higher cap.'],
    ['checker','stopped','Stopped: a module\'s handoff did not pass its check within the allowed turns.'],
    ['provider','stopped','Stopped: the model provider returned an error or an unknown charge.'],
    ['interrupted','interrupted','Stopped: the run was interrupted before a response was retained.'],
    ['ruling','failed','Failed: a provider ruling or pause is in force.'],
  ];
  for(const [reason,state,sentence] of rows){
    const p=await page(t,{list:[job()]});
    await p.watch();
    p.state.list=[job({state,reason,message:'detail text'})];
    await p.watch();
    assert.equal(p.built[0].options.body,sentence,reason);
    assert.equal(p.win.stopText(p.state.list[0]),`${sentence} detail text`,reason);
  }
  const p=await page(t,{list:[job()]});
  await p.watch();p.state.list=[job({state:'failed',reason:'other',message:'plain message'})];await p.watch();
  assert.equal(p.built[0].options.body,'plain message');
  assert.equal(p.win.stopText(p.state.list[0]),'failed: plain message');
});
test('a repairing module shows its turn and the rejected draft',async t=>{
  const p=await page(t);
  const names=id=>'Title '+id,run=progress=>p.win.describeModule({state:'running',progress},MODULES,names);
  assert.equal(run({module:'CP-2',step:'running',turn:2,max_turns:24}),'running Title CP-2, turn 2 of 24');
  assert.equal(run({module:'CP-2',step:'repairing',turn:3,max_turns:24}),'repairing Title CP-2 after a rejected draft, turn 3 of 24');
  assert.equal(run({step:'delivering'}),'delivering the report');
  assert.equal(run({module:'CP-1',step:'started'}),'running Title CP-1 (2 of 4)');
  assert.equal(run({module:'CP-1',step:'accepted'}),'Title CP-1 accepted (2 of 4)');
});
test('the spend line states the cap and the held amount while the run reports them',async t=>{
  const p=await page(t);
  assert.equal(p.win.spendText({state:'running',progress:{spent_usd:'0.42',held_usd:'1.86',cap_usd:'10.00'}}),'Recorded spend: USD 0.42 of a USD 10.00 cap; the next call holds USD 1.86');
  assert.equal(p.win.spendText({state:'running',progress:{spent_usd:'0.42'}}),'Recorded spend: USD 0.42');
});
test('a notification click with a run draft open asks before leaving it',async t=>{
  for(const [answer,reloads,hash] of [[true,1,`#W-Reports/list?c=${ID}`],[false,0,'#W-Library/cases']]){
    const p=await page(t,{list:[job()]});
    await p.watch();p.state.list=[job({state:'complete'})];await p.watch();
    p.doc.body.dataset.draft='1';
    let reloaded=0,asked=0;p.win.reloadApp=()=>{reloaded++;};p.win.confirm=()=>{asked++;return answer;};
    p.built[0].onclick();
    assert.equal(asked,1,String(answer));assert.equal(reloaded,reloads,String(answer));assert.equal(p.win.location.hash,hash,String(answer));
  }
});
test('the run list request says whether the tab can show the browser notice',async t=>{
  for(const [permission,url] of [['granted','/api/runs/list'],['denied','/api/runs/list?notify=0'],['default','/api/runs/list?notify=0']]){
    const p=await page(t,{permission,list:[job()]});
    const urls=[];const real=p.win.fetch;p.win.fetch=async(u,o)=>{urls.push(u);return real(u,o);};
    await p.watch();
    assert.deepEqual(urls,[url],permission);
  }
});
