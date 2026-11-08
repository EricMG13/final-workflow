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
async function page(t,{key=ID,run={status:status(),events:{events:EVENTS,complete:true}}}={}){
  const errors=[],calls=[];const virtualConsole=new VirtualConsole();virtualConsole.on('jsdomError',error=>errors.push(error));
  const dom=new JSDOM(html,{url:`http://127.0.0.1:54321/#CP-OS/activity?c=${key}`,runScripts:'outside-only',virtualConsole});
  const win=dom.window;win.scrollTo=()=>{};win.focus=()=>{};win.HTMLElement.prototype.scrollIntoView=function(){};
  win.fetch=async url=>{
    calls.push(url);
    const body=url.startsWith('/api/runs/status')?run.status:url.startsWith('/api/runs/events')?run.events:[];
    if(body instanceof Error)return{ok:false,text:async()=>body.message,json:async()=>({})};
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
    '09:00:00Started Title CP-0',
    '09:00:01Turn 1 of 24 · spend USD 0.00 of USD 10; this call holds USD 5.73',
    '09:00:02Draft of Title CP-0 rejected · 2 writes left',
    '09:00:03Accepted Title CP-0',
    '09:00:04Delivery started',
    '09:00:05Report delivered',
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
  assert.deepEqual(rows(p.doc),['09:00:02Draft of Title CP-1 rejected · 1 write left','09:00:03<b>odd</b>','09:00:04Stopped (other)']);
  assert.equal(p.doc.querySelector('.activity-log b'),null);
});
test('a stopped run leads with its stop sentence',async t=>{
  const p=await page(t,{run:{status:status({state:'stopped',reason:'budget',message:'cap reached',spent_usd:'9.90'}),events:{events:[{at:'2026-11-08T09:00:00Z',event:'stopped',reason:'budget'}],complete:true}}});
  const first=text(p.doc.querySelector('#run-activity p'));
  assert.ok(first.startsWith(p.vm.budget),first);
  assert.deepEqual(rows(p.doc),['09:00:00'+p.vm.budget]);
  assert.equal(text(p.doc.querySelectorAll('#run-activity p')[1]),'Recorded spend: USD 9.90');
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
test('a failed fetch says the record could not be loaded',async t=>{
  const p=await page(t,{run:{status:status(),events:new Error('boom')}});
  assert.equal(text(p.doc.querySelector('#run-activity .caution')),'Could not load the run record. Details: boom');
  assert.equal(p.doc.querySelector('.activity-log'),null);
});
test('a retained run keeps the retained-record text',async t=>{
  const p=await page(t,{key:'tdg-002'});
  assert.match(p.doc.getElementById('content').textContent,/No live progress or cost recorded/);
  assert.equal(p.doc.getElementById('run-activity'),null);
  assert.deepEqual(p.calls,[]);
});
