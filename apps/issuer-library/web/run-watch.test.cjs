/* The app-wide run watcher: title mark, rail mark, finish notification, stop sentences and turn text.
   jsdom with fake timers, fetch and Notification; synthetic job lists only; no network or provider. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const {JSDOM,VirtualConsole}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const settle=()=>new Promise(resolve=>setTimeout(resolve,10));
const ID='web-'+'a'.repeat(32),ID2='web-'+'d'.repeat(32),KEY='issuer-library.run-strip-dismissed';
const MODULES=['CP-0','CP-1','CP-2','CP-3'];
const job=(over={})=>({id:ID,state:'running',message:'Working',run_available:true,issuer:'Northbridge Group',pathway:'covenant_refinancing',as_of:'2025-03-31',modules:MODULES,module_details:MODULES.map(id=>({id,title:'Title '+id})),progress:{module:'CP-2',step:'running',turn:2,max_turns:24,spent_usd:'0.42',held_usd:'1.86',cap_usd:'10.00',accepted:2},...over});
async function page(t,{permission='granted',list=[],stored=null,broken=[]}={}){
  const errors=[],built=[];const virtualConsole=new VirtualConsole();virtualConsole.on('jsdomError',error=>errors.push(error));
  const dom=new JSDOM(html,{url:'http://127.0.0.1:54321/#W-Library/cases',runScripts:'outside-only',virtualConsole});
  const win=dom.window;win.scrollTo=()=>{};win.focus=()=>{};win.HTMLElement.prototype.scrollIntoView=function(){};
  const timers=new Map(),cleared=[];let next=1;
  win.setInterval=(fn,ms)=>{timers.set(next,{fn,ms});return next++;};win.clearInterval=id=>{cleared.push(id);timers.delete(id);};
  win.Notification=class{static permission=permission;static requestPermission=async()=>permission;constructor(title,options){this.title=title;this.options=options;built.push(this);}};
  const state={list};
  win.fetch=async url=>({ok:true,json:async()=>url.split('?')[0]==='/api/runs/list'?state.list:{}});
  if(stored)win.localStorage.setItem(KEY,JSON.stringify(stored));
  for(const method of broken)win.Storage.prototype[method]=()=>{throw new Error('storage unavailable');};
  const warnings=[];win.console.warn=(...args)=>warnings.push(args[0]);
  win.eval('window.DESIGN_DATA={runs:{},outputs:{},inputs:{},pins:{}};window.DESIGN_WORKSPACE={reports:[],models:[],visuals:[]};window.DESIGN_APP={workspace:"/research",policy_locked:false,issues:[],problem:""};');
  for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());
  await settle();
  t.after(()=>{win.close();assert.deepEqual(errors.map(error=>error.message),[]);});
  const doc=win.document;
  return{win,doc,built,warnings,state,timers,cleared,mark:()=>vm.runInContext('runMark',dom.getInternalVMContext()),
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
  assert.equal(rail.getAttribute('aria-hidden'),'true');assert.equal(rail.hasAttribute('role'),false);assert.equal(rail.hasAttribute('aria-label'),false);
  assert.equal(rail.closest('a').getAttribute('aria-label'),'Run activity — run running');
  assert.equal(rail.closest('a').getAttribute('href'),`#CP-OS/activity?c=${ID}`);
  p.state.list=[job({state:'stopped',reason:'budget'})];
  await p.watch();
  assert.equal(p.doc.title,'! Help · Issuer Library');assert.equal(rail.closest('a').getAttribute('aria-label'),'Run activity — run stopped');
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
  assert.equal(p.doc.getElementById('run-mark').closest('a').getAttribute('aria-label'),'Run activity — run running');
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
  assert.equal(p.win.stopText(p.state.list[0]),'Failed: plain message');
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

const strip=p=>p.doc.getElementById('run-strip');
const parts=p=>({title:strip(p).querySelector('.strip-title').textContent,lines:[...strip(p).querySelectorAll('.strip-text')].map(n=>n.textContent),actions:[...strip(p).querySelectorAll('.strip-actions a')].map(a=>[a.textContent,a.getAttribute('href')])});
const ACTIVITY=['View activity',`#CP-OS/activity?c=${ID}`];
test('the strip is the polite live region at the top of the page and is empty when there is nothing to show',async t=>{
  const p=await page(t,{list:[]});
  await p.watch();
  assert.equal(strip(p).hidden,true);assert.equal(strip(p).getAttribute('role'),'status');
  assert.equal(strip(p).parentElement.querySelector('.issuer').previousElementSibling,strip(p),'placed above the issuer header, inside the main column');
});
test('a running run shows the brand strip with the accepted count and one action',async t=>{
  const p=await page(t,{list:[job()]});
  await p.watch();
  assert.equal(strip(p).hidden,false);assert.equal(strip(p).dataset.tone,'brand');
  assert.deepEqual(parts(p),{title:'Run running · Northbridge Group',lines:['2 of 4 modules accepted'],actions:[ACTIVITY]});
  assert.equal(strip(p).querySelector('.strip-icon').dataset.icon,'activity');
  const close=strip(p).querySelector('.strip-close');
  assert.equal(close.getAttribute('aria-label'),'Dismiss run notice');assert.equal(close.title,'Dismiss');
});
test('a running run without counts falls back to the module text, or to no text',async t=>{
  const p=await page(t,{list:[job({modules:MODULES,progress:{module:'CP-2',step:'running',turn:2,max_turns:24}})]});
  await p.watch();
  assert.deepEqual(parts(p).lines,['running Title CP-2, turn 2 of 24']);
  p.state.list=[job({modules:undefined,module_details:undefined,progress:{}})];await p.watch();
  assert.deepEqual(parts(p).lines,[]);
});
test('a stopped, failed or interrupted run shows the amber strip with its sentence, spend line and Resume',async t=>{
  const rows=[['stopped','budget','Stopped','Stopped: the next model call would pass the spending cap; a new run needs a higher cap.'],
    ['failed','provider','Failed','Stopped: the model provider returned an error or an unknown charge.'],
    ['interrupted','interrupted','Interrupted','Stopped: the run was interrupted before a response was retained.']];
  for(const [state,reason,word,sentence] of rows){
    const p=await page(t,{list:[job({state,reason,message:'',spent_usd:'0.42'})]});
    await p.watch();
    assert.equal(strip(p).dataset.tone,'amber',state);assert.equal(strip(p).querySelector('.strip-icon').dataset.icon,'triangle-alert',state);
    assert.deepEqual(parts(p),{title:`Run ${word.toLowerCase()} · Northbridge Group`,lines:[sentence,'Recorded spend: USD 0.42'],actions:[ACTIVITY,['Resume',`#W-NewRun/run?resume=${ID}`]]},state);
  }
});
test('a complete run shows the grey strip with a tick and View reports only',async t=>{
  const p=await page(t,{list:[job({state:'complete'})]});
  await p.watch();
  assert.equal(strip(p).dataset.tone,'grey');assert.equal(strip(p).querySelector('.strip-icon').dataset.icon,'circle-check');
  assert.deepEqual(parts(p),{title:'Run complete · Northbridge Group',lines:[],actions:[['View reports',`#W-Reports/list?c=${ID}`]]});
});
test('at load the active job wins, else the newest job that is not running; reloads and notification clicks do not clear it',async t=>{
  const stopped=job({id:ID2,state:'stopped',reason:'budget',message:''}),done=job({state:'complete'});
  let p=await page(t,{list:[stopped,done]});
  await p.watch();
  assert.equal(parts(p).title,'Run stopped · Northbridge Group');assert.equal(p.mark(),'! ');
  assert.equal(parts(p).actions[0][1],`#CP-OS/activity?c=${ID2}`);
  p=await page(t,{list:[done,job({id:ID2})]});
  await p.watch();
  assert.equal(parts(p).title,'Run running · Northbridge Group');assert.equal(p.mark(),'● 2/4 · ');
  p=await page(t,{list:[done]});
  await p.watch();
  assert.equal(strip(p).hidden,false);assert.equal(p.mark(),'✓ ');assert.equal(p.doc.getElementById('run-mark').hidden,false);assert.equal(p.built.length,0);
  // a notification click for a finished run leaves the notice in place
  p=await page(t,{list:[job()]});
  await p.watch();p.state.list=[done];await p.watch();
  p.win.reloadApp=()=>{};p.built[0].onclick();
  assert.equal(strip(p).hidden,false);
});
test('the rail mark takes its colour state and glyph from the run and is not announced',async t=>{
  for(const [over,glyph,state] of [[{},'●','running'],[{state:'complete'},'✓','complete'],[{state:'stopped',reason:'budget'},'!','stopped'],[{state:'failed',reason:'provider'},'!','stopped'],[{state:'interrupted',reason:'interrupted'},'!','stopped']]){
    const p=await page(t,{list:[job(over)]});
    await p.watch();
    const mark=p.doc.getElementById('run-mark');
    assert.deepEqual([mark.textContent,mark.dataset.state,mark.getAttribute('aria-hidden'),mark.hasAttribute('role'),mark.hidden],[glyph,state,'true',false,false],JSON.stringify(over));
    assert.equal(mark.closest('a').getAttribute('aria-label'),`Run activity — run ${(over.state||'running')}`);
  }
});
test('a poll that only moves the count does not rebuild the strip; a change of state does',async t=>{
  const p=await page(t,{list:[job()]});
  await p.watch();
  const title=strip(p).querySelector('.strip-title');
  p.state.list=[job({progress:{module:'CP-3',step:'running',accepted:3}})];await p.watch();
  assert.equal(strip(p).querySelector('.strip-title'),title);assert.deepEqual(parts(p).lines,['3 of 4 modules accepted']);
  p.state.list=[job({state:'stopped',reason:'budget',message:''})];await p.watch();
  assert.notEqual(strip(p).querySelector('.strip-title'),title);assert.equal(strip(p).dataset.tone,'amber');
});
test('dismissing hides the strip and mark for that job until its state changes, and is stored per viewer',async t=>{
  const p=await page(t,{list:[job({state:'stopped',reason:'budget',message:''})]});
  await p.watch();
  strip(p).querySelector('.strip-close').click();
  assert.equal(strip(p).hidden,true);assert.equal(p.doc.getElementById('run-mark').hidden,true);assert.equal(p.mark(),'');
  assert.deepEqual(JSON.parse(p.win.localStorage.getItem(KEY)),{[ID]:'stopped'});
  await p.watch();assert.equal(strip(p).hidden,true);
  p.state.list=[job({state:'failed',reason:'provider',message:''})];await p.watch();
  assert.equal(strip(p).hidden,false,'a changed state shows the notice again');
});
test('a stored dismissal is read at load',async t=>{
  const p=await page(t,{list:[job({state:'stopped',reason:'budget',message:''})],stored:{[ID]:'stopped'}});
  await p.watch();
  assert.equal(strip(p).hidden,true);
  const q=await page(t,{list:[job({state:'stopped',reason:'budget',message:''})],stored:{[ID]:'running'}});
  await q.watch();assert.equal(strip(q).hidden,false);
});
test('without usable storage a dismissal holds for the page, is warned about, and the notice returns after a reload',async t=>{
  const p=await page(t,{list:[job({state:'stopped',reason:'budget',message:''})],broken:['getItem','setItem']});
  await p.watch();
  assert.equal(strip(p).hidden,false,'unreadable storage shows the notice');
  strip(p).querySelector('.strip-close').click();
  assert.equal(strip(p).hidden,true);
  await p.watch();assert.equal(strip(p).hidden,true);
  assert.ok(p.warnings.some(w=>/could not be (read|saved)/.test(w)),'the failure is logged');
});
test('the strip links go to that job, and ask before leaving a run draft',async t=>{
  let p=await page(t,{list:[job({state:'stopped',reason:'budget',message:''})]});
  await p.watch();
  let reloads=0;p.win.reloadApp=()=>{reloads++;};
  const link=label=>[...strip(p).querySelectorAll('a')].find(a=>a.textContent===label);
  link('View activity').click();
  assert.equal(p.win.location.hash,`#CP-OS/activity?c=${ID}`);assert.equal(reloads,1);
  link('Resume').click();
  assert.equal(p.win.location.hash,`#W-NewRun/run?resume=${ID}`);assert.equal(reloads,1,'Resume reads the live status, no reload');
  for(const [answer,hash,count] of [[false,'#W-Library/cases',0],[true,`#CP-OS/activity?c=${ID}`,1]]){
    p=await page(t,{list:[job({state:'stopped',reason:'budget',message:''})]});
    await p.watch();
    let asked=0;reloads=0;p.win.reloadApp=()=>{reloads++;};p.win.confirm=()=>{asked++;return answer;};
    p.doc.body.dataset.draft='1';
    [...strip(p).querySelectorAll('a')].find(a=>a.textContent==='View activity').click();
    assert.equal(asked,1);assert.equal(p.win.location.hash,hash);assert.equal(reloads,count);
  }
});
test('plain state words replace raw states, and bare module codes are named',async t=>{
  const p=await page(t);
  const details=[{id:'CP-1',title:'Financial analysis'}];
  const text=(state,message,extra={})=>p.win.stopText({state,message,module_details:details,...extra});
  assert.equal(text('failed','boom'),'Failed: boom');assert.equal(text('complete','Done'),'Complete: Done');
  assert.equal(text('interrupted',''),'Interrupted');assert.equal(text('stopped','halt'),'Stopped: halt');
  assert.equal(text('weird','x'),'Not running: x');
  assert.equal(p.win.stopText({state:'running',message:'Working'},true),'Running');
  assert.equal(p.win.stopText({state:'running',message:'Working'}),'Running: Working');
  assert.equal(text('failed','CP-1 rejected; CP-OS stopped; CP-9 unknown'),'Failed: Financial analysis (CP-1) rejected; CP-OS stopped; CP-9 unknown');
  assert.equal(text('failed','Financial analysis (CP-1) rejected'),'Failed: Financial analysis (CP-1) rejected','an already named code is left alone');
  assert.equal(text('stopped','x',{reason:'budget'}),'Stopped: the next model call would pass the spending cap; a new run needs a higher cap. x');
});
test('Fix 1: dismissing a running strip hides it (and the mark) until the run changes state',async t=>{
  const p=await page(t,{list:[job()]});
  await p.watch();
  strip(p).querySelector('.strip-close').click();
  assert.equal(strip(p).hidden,true);assert.equal(p.doc.getElementById('run-mark').hidden,true);
  assert.deepEqual(JSON.parse(p.win.localStorage.getItem(KEY)),{[ID]:'running'});
  p.state.list=[job({progress:{module:'CP-3',step:'running',accepted:3}})];await p.watch();
  assert.equal(strip(p).hidden,true,'a poll in the same state keeps it hidden');
  p.state.list=[job({state:'stopped',reason:'budget',message:''})];await p.watch();
  assert.equal(strip(p).hidden,false,'the stop shows it again');
});
test('Fix 1: a running job left dismissed does not hide a newer state of another job',async t=>{
  const p=await page(t,{list:[job()],stored:{[ID]:'running'}});
  await p.watch();assert.equal(strip(p).hidden,true);
  p.state.list=[job({id:ID2})];await p.watch();assert.equal(strip(p).hidden,false);
});
test('Fix 2: an unchanged state with no supporting text updates in place and does not rebuild',async t=>{
  const p=await page(t,{list:[job({modules:undefined,module_details:undefined,progress:{}})]});
  await p.watch();
  const title=strip(p).querySelector('.strip-title');
  await p.watch();await p.watch();
  assert.equal(strip(p).querySelector('.strip-title'),title);
});
