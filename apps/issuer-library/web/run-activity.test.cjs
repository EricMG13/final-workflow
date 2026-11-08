/* The Run activity page for an app run: events, spend and stop reason from /api/runs/status and /api/runs/events.
   jsdom with a fetch mock; synthetic logs written by hand; no network or provider. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const {JSDOM,VirtualConsole}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const settle=()=>new Promise(resolve=>setTimeout(resolve,20));
const ID='web-'+'b'.repeat(32);
const MODULES=['CP-0','CP-1'];
const status=(over={})=>({id:ID,state:'running',message:'Working',run_available:true,modules:MODULES,module_details:MODULES.map(id=>({id,title:'Title '+id})),spent_usd:'0.00',progress:{module:'CP-1',step:'running',turn:1,max_turns:24,spent_usd:'0.00',held_usd:'5.73',cap_usd:'10',accepted:1},...over});
const EVENTS=[
  {at:'2026-11-08T09:00:00Z',event:'module_started',module:'CP-0'},
  {at:'2026-11-08T09:00:01Z',event:'turn',module:'CP-0',turn:1,max_turns:24,spent_usd:'0.00',held_usd:'5.73',cap_usd:'10'},
  {at:'2026-11-08T09:00:02Z',event:'draft_rejected',module:'CP-0',writes_left:2},
  {at:'2026-11-08T09:00:03Z',event:'module_accepted',module:'CP-0'},
  {at:'2026-11-08T09:00:04Z',event:'delivery_started'},
  {at:'2026-11-08T09:00:05Z',event:'delivered'},
];
async function page(t,{key=ID,gate=null,run={status:status(),events:{events:EVENTS,complete:true}}}={}){
  const errors=[],calls=[];const virtualConsole=new VirtualConsole();virtualConsole.on('jsdomError',error=>errors.push(error));
  const dom=new JSDOM(html,{url:`http://127.0.0.1:54321/#CP-OS/activity?c=${key}`,runScripts:'outside-only',virtualConsole});
  const win=dom.window;win.scrollTo=()=>{};win.focus=()=>{};win.HTMLElement.prototype.scrollIntoView=function(){};
  win.fetch=async url=>{
    calls.push(url);
    if(gate&&url.startsWith('/api/runs/status')){await gate;return{ok:false,status:404,text:async()=>'404 page not found',json:async()=>({})};}
    const body=url.startsWith('/api/runs/status')?run.status:url.startsWith('/api/runs/events')?run.events:[];
    if(body instanceof Error)return{ok:false,status:body.httpStatus,text:async()=>body.message,json:async()=>({})};
    return{ok:true,json:async()=>body};
  };
  win.eval(`window.DESIGN_DATA={runs:{${JSON.stringify(key)}:{run:${JSON.stringify(key)},title:'Northbridge Group',period:'as of 31 March 2025',issuerKey:'id:nbg',issuer:'Northbridge Group',modules:{},first:null}},outputs:{},inputs:{},pins:{}};window.DESIGN_WORKSPACE={reports:[],models:[],visuals:[]};window.DESIGN_APP={workspace:"/research",policy_locked:false,issues:[],problem:""};`);
  for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());
  await settle();
  t.after(()=>{win.close();assert.deepEqual(errors.map(error=>error.message),[]);});
  return{win,doc:win.document,calls,vm:vm.runInContext('STOP_COPY',dom.getInternalVMContext())};
}
const text=node=>node.textContent.trim();
const rows=doc=>[...doc.querySelectorAll('.activity-log tbody tr')].map(text);
test('the run activity page lists each event in order with its text',async t=>{
  const p=await page(t);
  assert.deepEqual(rows(p.doc),[
    '8 November 2026 · 09:00:00 UTCStarted Title CP-0',
    '8 November 2026 · 09:00:01 UTCTurn 1 of 24 · spend USD 0.00 of USD 10; this call holds USD 5.73',
    '8 November 2026 · 09:00:02 UTCDraft of Title CP-0 rejected · 2 writes left',
    '8 November 2026 · 09:00:03 UTCAccepted Title CP-0',
    '8 November 2026 · 09:00:04 UTCDelivery started',
    '8 November 2026 · 09:00:05 UTCReport delivered',
  ]);
  assert.equal(text(p.doc.querySelector('.activity-summary')),'Running · running Title CP-1, turn 1 of 24');
  assert.equal(text(p.doc.querySelector('#run-activity h2')),'Run activity · '+ID);
  assert.equal(text(p.doc.querySelector('.activity-log caption')),'Events (UTC)');
  assert.ok(p.doc.querySelector('.activity-flow'));
  assert.equal(p.doc.querySelector('#run-activity .caution'),null);
});
test('one write left reads in the singular and an unknown event is shown as written',async t=>{
  const p=await page(t,{run:{status:status(),events:{events:[
    {at:'2026-11-08T09:00:02Z',event:'draft_rejected',module:'CP-1',writes_left:1},
    {at:'2026-11-08T09:00:03Z',event:'<b>odd</b>'},
    {at:'2026-11-08T09:00:04Z',event:'stopped',reason:'other'},
  ],complete:true}}});
  assert.deepEqual(rows(p.doc),['8 November 2026 · 09:00:02 UTCDraft of Title CP-1 rejected · 1 write left','8 November 2026 · 09:00:03 UTC<b>odd</b>','8 November 2026 · 09:00:04 UTCStopped (other)']);
  assert.equal(p.doc.querySelector('.activity-log b'),null);
});
test('a stopped run leads with its stop sentence',async t=>{
  const p=await page(t,{run:{status:status({state:'stopped',reason:'budget',message:'cap reached',spent_usd:'9.90'}),events:{events:[{at:'2026-11-08T09:00:00Z',event:'stopped',reason:'budget'}],complete:true}}});
  const first=text(p.doc.querySelector('#run-activity p'));
  assert.ok(first.startsWith(p.vm.budget),first);
  assert.deepEqual(rows(p.doc),['8 November 2026 · 09:00:00 UTC'+p.vm.budget]);
  assert.equal(text(p.doc.querySelectorAll('#run-activity p')[1]),'Recorded spend: USD 9.90 of a USD 10 cap');
});
test('an incomplete log says so',async t=>{
  const p=await page(t,{run:{status:status(),events:{events:EVENTS.slice(0,2),complete:false}}});
  assert.equal(rows(p.doc).length,2);
  assert.equal(text(p.doc.querySelector('#run-activity .caution')),'The record is incomplete: the log was cut or stopped mid-write.');
});
test('a run without a log shows the no-events line',async t=>{
  const p=await page(t,{run:{status:status(),events:{events:[],complete:true}}});
  assert.equal(p.doc.querySelector('.activity-log'),null);
  assert.equal(text(p.doc.querySelector('#run-activity .hint')),'No events were recorded for this run.');
});
const httpError=(message,httpStatus)=>Object.assign(new Error(message),{httpStatus});
test('a failed fetch says the record could not be loaded and keeps the raw detail closed',async t=>{
  const p=await page(t,{run:{status:status(),events:httpError('boom',500)}});
  const note=p.doc.querySelector('#run-activity .caution');
  assert.equal(text(note.querySelector('p')||note.firstChild),'Could not load this run\'s live record. Reload the library to try again.');
  const details=p.doc.querySelector('#run-activity details');
  assert.equal(details.open,false);assert.equal(text(details.querySelector('summary')),'Technical detail');
  assert.match(text(details),/boom/);
  assert.doesNotMatch(note.textContent.replace(details.textContent,''),/boom/);
  assert.equal(p.doc.querySelector('.activity-log'),null);
});
test('a 404 for the live record shows the retained-record view, never the raw 404 text',async t=>{
  const p=await page(t,{run:{status:httpError('404 page not found\n',404),events:{events:[],complete:true}}});
  const content=p.doc.getElementById('content').textContent;
  assert.match(content,/Retained record · /);assert.match(content,/No live progress is recorded for this run in this workspace\./);
  assert.doesNotMatch(content,/404|page not found|Could not load/);
  assert.equal(p.doc.getElementById('run-activity'),null);
  assert.ok(p.doc.querySelector('.activity-flow'),'the flow stays');
});
test('a 404 status with a recorded event log shows the retained heading, the log and the last recorded spend',async t=>{
  const events={events:[EVENTS[0],EVENTS[1],{at:'2026-11-08T09:10:00Z',event:'turn',module:'CP-0',turn:2,max_turns:24,spent_usd:'2.40',held_usd:'1.00',cap_usd:'10'}],complete:true};
  const p=await page(t,{run:{status:httpError('404 page not found\n',404),events}});
  const content=p.doc.getElementById('content').textContent;
  assert.match(content,/Retained record · /);
  assert.doesNotMatch(content,/No live progress is recorded for this run in this workspace\./);
  assert.equal(p.doc.querySelectorAll('.activity-log tbody tr').length,3);
  assert.ok(p.doc.querySelector('#content .table-scroll .activity-log'));
  assert.match(content,/Last recorded spend: USD 2\.40/);
  assert.doesNotMatch(content,/404|page not found/);
  const none=await page(t,{run:{status:httpError('404',404),events:{events:[],complete:true}}});
  assert.match(none.doc.getElementById('content').textContent,/No live progress is recorded for this run in this workspace\./);
  const lost=await page(t,{run:{status:httpError('404',404),events:httpError('boom',500)}});
  assert.match(lost.doc.getElementById('content').textContent,/No live progress is recorded for this run in this workspace\./);
});
test('a 404 that lands after the reader left Run activity neither throws nor writes onto the new page',async t=>{
  const rejections=[];const onRejection=error=>rejections.push(error);process.on('unhandledRejection',onRejection);t.after(()=>process.off('unhandledRejection',onRejection));
  let release;const gate=new Promise(resolve=>{release=resolve;});
  const p=await page(t,{run:{status:null,events:{events:[],complete:true}},gate});
  p.win.location.hash='#W-Library/cases';await settle();
  release();await new Promise(resolve=>setTimeout(resolve,50));
  assert.deepEqual(rejections,[]);
  assert.doesNotMatch(p.doc.getElementById('content').textContent,/Live progress and spend are recorded only/);
});
test('a 404 on the events request alone is also the retained record',async t=>{
  const p=await page(t,{run:{status:status(),events:httpError('404 page not found',404)}});
  assert.match(p.doc.getElementById('content').textContent,/No live progress is recorded for this run in this workspace\./);
  assert.doesNotMatch(p.doc.getElementById('content').textContent,/404/);
});
test('the log sits in the bordered content-table card and only the summary line is live',async t=>{
  const p=await page(t);
  const card=p.doc.querySelector('#run-activity .table-scroll');
  assert.ok(card&&card.querySelector('table.activity-log'),'the log is inside the card');
  assert.equal(card.tabIndex,0);
  assert.equal(p.doc.getElementById('run-activity').hasAttribute('aria-live'),false);
  assert.equal(p.doc.querySelector('.activity-summary').getAttribute('aria-live'),'polite');
  assert.equal(p.doc.querySelectorAll('#run-activity [aria-live]').length,1);
  assert.equal(text(p.doc.querySelector('.activity-log td')),'8 November 2026 · 09:00:00 UTC');
});
test('a stopped app run offers Resume this run through New run\'s resume route; other runs do not',async t=>{
  const stopped=(over={})=>({run:{status:status({state:'stopped',reason:'budget',spent_usd:'9.90',...over}),events:{events:EVENTS.slice(0,1),complete:true}}});
  const p=await page(t,stopped());
  const link=[...p.doc.querySelectorAll('#run-activity a')].find(a=>text(a)==='Resume this run');
  assert.ok(link);assert.equal(link.getAttribute('href'),`#W-NewRun/run?resume=${ID}`);
  for(const over of [{reason:'ruling',state:'failed'},{state:'running'},{state:'complete'}]){
    const q=await page(t,stopped(over));
    assert.equal([...q.doc.querySelectorAll('#run-activity a')].some(a=>/Resume/.test(text(a))),false,JSON.stringify(over));
  }
});
test('a retained run keeps the retained-record text',async t=>{
  const p=await page(t,{key:'tdg-002'});
  assert.match(p.doc.getElementById('content').textContent,/No live progress is recorded for this run in this workspace\./);
  assert.equal(p.doc.getElementById('run-activity'),null);
  assert.deepEqual(p.calls,[]);
});
test('Final 2: the retained-record sentence makes no claim about cost',async t=>{
  const p=await page(t,{run:{status:httpError('404 page not found',404),events:httpError('404 page not found',404)}});
  const content=p.doc.getElementById('content').textContent;
  assert.match(content,/No live progress is recorded for this run in this workspace\./);
  assert.doesNotMatch(content,/No live progress or cost/);
});
test('Final 4: the activity log card is a named region',async t=>{
  const p=await page(t);
  const card=p.doc.querySelector('#run-activity .table-scroll');
  assert.equal(card.getAttribute('role'),'region');
  assert.equal(card.getAttribute('aria-label'),'Run events');
});
