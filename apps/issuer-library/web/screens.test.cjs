/* Frame states, search scope, tab vocabulary and report rows. Synthetic fixture only; no network or provider. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const {JSDOM,VirtualConsole}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const root=path.resolve(__dirname,'../../../artifacts/issuer-library/design-fixture');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const settle=(ms=10)=>new Promise(resolve=>setTimeout(resolve,ms));
function fixture(hash,timeout,before){
  const dom=new JSDOM(html,{url:`file://${__dirname}/index.html#${hash}`,runScripts:'outside-only'});
  const w=dom.window;w.scrollTo=()=>{};w.fetch=()=>new Promise(()=>{});
  w.HTMLElement.prototype.scrollIntoView=function(){};
  if(timeout!==undefined)w.DESIGN_FRAME_TIMEOUT_MS=timeout;
  if(before)before(w);
  for(const name of ['data.js','workspace-data.js'])vm.runInContext(fs.readFileSync(path.join(root,name),'utf8'),dom.getInternalVMContext());
  for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());
  return dom;
}
const go=async(w,hash)=>{w.location.hash=hash;w.dispatchEvent(new w.Event('hashchange'));await settle();};
const text=el=>el.textContent.replace(/\s+/g,' ').trim();

test('tab and rail vocabulary follows the approved destinations',t=>{
  const w=fixture('W-Overview/overview?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  assert.deepEqual([...d.querySelectorAll('.workspace-tabs a')].map(a=>a.textContent),['Overview','Modules','Calendar','Forecast','Reports','Evidence']);
  assert.ok(d.querySelector('.rail a[data-place="Reports"]'));
  assert.equal(d.querySelector('.rail a[data-place="Deliverables"]'),null);
  assert.ok(d.querySelector('.rail a[data-place="Run activity"] img').getAttribute('src').endsWith('icons/activity.svg'));
  w.location.hash='W-Reports/list?c=tdg-002';w.dispatchEvent(new w.Event('hashchange'));
  assert.equal(d.title,'Reports · Issuer Library');
  assert.equal(d.getElementById('section-title').textContent,'Reports');
  assert.equal(d.querySelector('h1').textContent,w.eval('contexts["tdg-002"].title'));
});

test('search is cleared when leaving the analytical modules and can be cleared in place',async t=>{
  const w=fixture('CP-1/performance?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  const search=d.getElementById('module-search'),clear=()=>d.getElementById('module-search-clear');
  search.value='liquidity';search.dispatchEvent(new w.Event('input',{bubbles:true}));
  assert.ok(d.getElementById('search-results').children.length>0);
  assert.equal(clear().hidden,false);
  await go(w,'W-Calendar/events?c=tdg-002');
  assert.equal(search.value,'');assert.equal(d.getElementById('search-results').children.length,0);
  assert.ok(d.getElementById('workbench').classList.contains('tools-workspace'));
  await go(w,'CP-2/assessment?c=tdg-002');
  assert.ok(!d.getElementById('workbench').classList.contains('tools-workspace'));
  search.value='liquidity';search.dispatchEvent(new w.Event('input',{bubbles:true}));
  clear().click();
  assert.equal(search.value,'');assert.equal(d.getElementById('search-results').children.length,0);
  assert.equal(d.activeElement,search);assert.equal(clear().hidden,true);
});

test('the navigator is resident on Overview and Modules only',async t=>{
  const w=fixture('W-Overview/overview?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  const tools=()=>d.getElementById('workbench').classList.contains('tools-workspace');
  assert.equal(tools(),false);
  await go(w,'CP-1/performance?c=tdg-002');assert.equal(tools(),false);
  for(const hash of ['W-Reports/list','W-Evidence/sources','CP-OS/activity']){await go(w,`${hash}?c=tdg-002`);assert.equal(tools(),true,hash);}
});

test('the report frame shows loading, failure with retry, and loaded',async t=>{
  const dom=fixture('W-Calendar/events?c=tdg-002',20),w=dom.window,d=w.document;t.after(()=>w.close());
  const report=w.eval('window.DESIGN_WORKSPACE.reports[0]');
  await go(w,`W-Reports/${report.id}`);
  const status=()=>d.querySelector('.frame-status');
  assert.match(text(status()),/^Loading report/);
  await settle(60);
  assert.match(text(status()),/did not load/);
  assert.equal(status().querySelector('a').getAttribute('href'),report.download);
  const frame=d.getElementById('report-preview'),src=frame.getAttribute('src');
  status().querySelector('.frame-retry').click();
  assert.equal(text(status()),'Loading report…');assert.equal(frame.getAttribute('src'),src);
  frame.dispatchEvent(new w.Event('load'));
  assert.equal(status().hidden,true);
  await settle(60);assert.equal(status().hidden,true);
});

test('the run context frame shows loading, failure with retry, and ready',async t=>{
  const errors=[],virtualConsole=new VirtualConsole();virtualConsole.on('jsdomError',e=>errors.push(e));
  const dom=new JSDOM(html,{url:'http://127.0.0.1:54321/#W-NewRun/run',runScripts:'outside-only',virtualConsole}),w=dom.window,d=w.document;
  w.scrollTo=()=>{};w.HTMLElement.prototype.scrollIntoView=function(){};w.setInterval=()=>1;w.clearInterval=()=>{};
  w.fetch=async()=>({ok:true,json:async()=>[]});
  w.eval('window.DESIGN_FRAME_TIMEOUT_MS=20;window.DESIGN_DATA={runs:{},outputs:{},inputs:{},pins:{}};window.DESIGN_WORKSPACE={reports:[],models:[],visuals:[]};window.DESIGN_APP={workspace:"/research",policy_locked:false,issues:[],problem:""};');
  for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());
  t.after(()=>{w.close();assert.deepEqual(errors.map(e=>e.message),[]);});
  const status=()=>d.querySelector('#context-step .frame-status');
  assert.match(text(status()),/^Loading run context form/);
  await settle(60);
  assert.match(text(status()),/did not load/);
  status().querySelector('.frame-retry').click();
  assert.match(text(status()),/^Loading run context form/);
  const editor=d.getElementById('context-editor');
  w.dispatchEvent(new w.MessageEvent('message',{source:editor.contentWindow,data:{type:'cpos:height',height:500}}));
  assert.equal(status().hidden,true);
});

test('report rows carry the id, sort by build and prefix other issuers',async t=>{
  const w=fixture('W-Reports/list?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  const reports=w.eval('window.DESIGN_WORKSPACE.reports'),ids=new Set(reports.map(r=>r.id));
  const rows=[...d.querySelectorAll('.report-built .report-list li')];
  assert.ok(rows.length>0);
  const builds=rows.map(li=>Number(/Build (\d+)/.exec(li.textContent)?.[1]??0));
  builds.forEach((b,i)=>{if(i)assert.ok(b<=builds[i-1],`build order ${builds}`);});
  for(const li of d.querySelectorAll('.report-list li')){
    assert.ok(ids.has(li.querySelector('.code')?.textContent),li.textContent);
    assert.ok(!/  /.test(li.textContent),JSON.stringify(li.textContent));
  }
  assertRestRows(w,d,'tdg-002',false);
  // The engine's default label for an uncurated report already starts with its issuer; the fixture's curated labels do not.
  w.eval('window.DESIGN_WORKSPACE.reports[0].label=window.DESIGN_WORKSPACE.reports[0].issuer+" · as of 2025-05-31"');
  await go(w,'W-Reports/list?c=ford-otosan-2024');
  assert.ok(d.querySelector('.report-rest .report-list li .code')&&[...d.querySelectorAll('.report-rest .report-list li a')].some(a=>text(a).includes('TransDigm Group · as of 2025-05-31')),'issuer-led label case missing');
  assertRestRows(w,d,'ford-otosan-2024',true);
});

function assertRestRows(w,d,context,required){
  const reports=w.eval('window.DESIGN_WORKSPACE.reports'),run=w.eval(`contexts["${context}"].issuer`);
  const rest=[...d.querySelectorAll('.report-rest .report-list li')];
  if(required)assert.ok(rest.length>0,`no rows under .report-rest for ${context}`);
  for(const li of rest){
    const report=reports.find(r=>r.id===li.querySelector('.code').textContent),label=text(li.querySelector('a')),shown=text(li).replace(text(li.querySelector('.code')),'');
    const led=report.label.trim().startsWith(report.issuer);
    if(report.issuer!==run&&!led)assert.ok(text(li).startsWith(report.issuer),li.textContent);
    if(led)assert.ok(text(li).includes(report.label.trim()),li.textContent);
    assert.equal(shown.split(report.issuer).length-1,1,`issuer repeated: ${text(li)}`);
    if(led)assert.ok(!li.querySelector('.report-issuer'),`prefix added to a label that has the issuer: ${text(li)}`);
    else assert.ok(li.querySelector('.report-issuer'),`label without issuer left unprefixed: ${label}`);
  }
}

test('the report selector lists builds in the list-page order',async t=>{
  const w=fixture('W-Reports/list?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  const report=w.eval('window.DESIGN_WORKSPACE.reports.filter(r=>r.issuer===contexts["tdg-002"].issuer)[0]');
  await go(w,`W-Reports/${report.id}?c=tdg-002`);
  const options=[...d.querySelectorAll('#report-select option')].map(o=>o.textContent);
  assert.ok(options.length>1);
  const builds=options.map(o=>Number(/^Build (\d+)/.exec(o)?.[1]??0));
  builds.forEach((b,i)=>{if(i)assert.ok(b<=builds[i-1],`select order ${builds}`);});
});

test('Help names Reports, not Deliverables',async t=>{
  const w=fixture('W-Help/help?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  const help=text(d.getElementById('content'));
  assert.match(help,/Reports lists/);assert.doesNotMatch(help,/Deliverables lists/);
});
test('Settings lists workspace issues as path and message and quits as a tertiary action',async t=>{
  const dom=new JSDOM(html,{url:'http://127.0.0.1:54321/#W-Settings/workspace',runScripts:'outside-only'});
  const w=dom.window;t.after(()=>w.close());w.scrollTo=()=>{};w.fetch=()=>new Promise(()=>{});w.HTMLElement.prototype.scrollIntoView=function(){};
  w.eval("window.DESIGN_DATA={runs:{},outputs:{},inputs:{},pins:{}};window.DESIGN_WORKSPACE={reports:[],models:[],visuals:[]};window.DESIGN_APP={workspace:'/research',policy_locked:false,issues:['deliverables/x: Delivery manifest requires report.html: and view.json','plain note'],problem:''};");
  for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());
  await settle();
  const d=w.document,quit=d.getElementById('quit-library');
  assert.ok(quit.classList.contains('tertiary-action'));
  assert.equal(quit.parentElement.lastElementChild,quit);assert.ok(quit.parentElement.classList.contains('step-actions'));
  const items=[...d.querySelectorAll('.issue-list li')];
  assert.equal(items.length,2);
  assert.equal(items[0].querySelector('.code').textContent,'deliverables/x');
  assert.equal(items[0].children[1].textContent,'Delivery manifest requires report.html: and view.json');
  assert.equal(items[1].querySelector('.code'),null);
});

function emptyPage(hash,t){
  const errors=[],virtualConsole=new VirtualConsole();virtualConsole.on('jsdomError',e=>errors.push(e));
  const dom=new JSDOM(html,{url:`http://127.0.0.1:54321/#${hash}`,runScripts:'outside-only',virtualConsole}),w=dom.window;
  t.after(()=>w.close());w.scrollTo=()=>{};w.HTMLElement.prototype.scrollIntoView=function(){};
  w.eval("window.DESIGN_DATA={runs:{},outputs:{},inputs:{},pins:{}};window.DESIGN_WORKSPACE={reports:[],models:[],visuals:[]};window.DESIGN_APP={workspace:'/research',policy_locked:false,issues:[],problem:''};");
  return {dom,w,errors,load:()=>{for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());}};
}
async function settingsPage(t,fail){
  const p=emptyPage('W-Settings/workspace',t),calls=[];
  p.w.fetch=url=>{calls.push(url);return new Promise((resolve,reject)=>setTimeout(()=>fail?reject(new Error('down')):resolve({ok:true,json:async()=>({})}),30));};
  p.load();await settle();return {...p,calls,d:p.w.document};
}
const SETTINGS_BUTTONS=['save-workspace','refresh-library','quit-library'];
test('H1 Settings sends one request at a time and shows what is happening',async t=>{
  const p=await settingsPage(t,false);
  p.d.getElementById('refresh-library').click();await settle(2);p.d.getElementById('refresh-library').click();
  assert.deepEqual(SETTINGS_BUTTONS.map(id=>p.d.getElementById(id).disabled),[true,true,true]);
  for(const id of SETTINGS_BUTTONS)assert.equal(p.d.getElementById(id).disabled,true,id);
  assert.match(p.d.getElementById('settings-status').textContent,/^Refreshing/);
  await settle(60);
  assert.equal(p.calls.filter(u=>u==='/api/refresh').length,1);
});
test('H1 a failed Settings request re-enables the buttons and says why',async t=>{
  const p=await settingsPage(t,true);
  p.d.getElementById('save-workspace').click();await settle(60);
  assert.deepEqual(SETTINGS_BUTTONS.map(id=>p.d.getElementById(id).disabled),[false,false,false]);
  assert.match(p.d.getElementById('settings-status').textContent,/^Could not update the library/);
});
test('H1 Quit locks the buttons while stopping and is ignored during another request',async t=>{
  const p=await settingsPage(t,false);
  p.d.getElementById('quit-library').click();await settle(2);
  for(const id of SETTINGS_BUTTONS)assert.equal(p.d.getElementById(id).disabled,true,id);
  await settle(60);
  const q=await settingsPage(t,false);
  q.d.getElementById('refresh-library').click();await settle(2);
  q.d.getElementById('quit-library').disabled=false;q.d.getElementById('quit-library').click();await settle(2);
  assert.equal(q.calls.includes('/api/quit'),false);await settle(60);
});
test('H2 Quit marks the library stopped',async t=>{
  const p=await settingsPage(t,false);
  p.d.getElementById('quit-library').click();await settle(60);
  assert.equal(p.d.body.dataset.quit,'1');
});
// Runs boot.js itself: fetch is stubbed, its discovery interval is captured, and each script load fires onload.
async function bootPage(t,hash,reply){
  const errors=[],virtualConsole=new VirtualConsole();virtualConsole.on('jsdomError',e=>errors.push(e.message));
  const dom=new JSDOM(html,{url:`http://127.0.0.1:54321/#${hash}`,runScripts:'outside-only',virtualConsole}),w=dom.window;t.after(()=>w.close());
  let tick=null;w.setInterval=fn=>{tick=fn;return 1;};w.console.warn=()=>{};
  w.fetch=async()=>reply();
  const real=w.document.createElement.bind(w.document);
  w.document.createElement=name=>{const el=real(name);if(name==='script')setTimeout(()=>el.onload&&el.onload(),0);return el;};
  vm.runInContext(fs.readFileSync(path.join(__dirname,'boot.js'),'utf8'),dom.getInternalVMContext());await settle(30);
  return {w,d:w.document,errors,tick:async()=>{await tick();}};
}
const GOOD={real:[],runs:{},outputs:{},inputs:{},pins:{},reports:[],models:[],visuals:[],issues:[],workspace:'/r'};
test('H2 the service banner appears after two failed checks and clears on success',async t=>{
  let mode='ok';
  const reply=()=>{if(mode==='down')throw new Error('down');return{ok:true,json:async()=>GOOD};};
  const p=await bootPage(t,'W-Library/cases',reply),banner=()=>p.d.getElementById('service-down').hidden;
  mode='down';
  await p.tick();assert.equal(banner(),true);
  await p.tick();assert.equal(banner(),false);
  mode='ok';await p.tick();assert.equal(banner(),true);
  mode='down';p.d.body.dataset.quit='1';
  await p.tick();await p.tick();await p.tick();assert.equal(banner(),true);
});
test('H2 a success between failures resets the count',async t=>{
  let mode='down';
  const reply=()=>{if(mode==='down')throw new Error('down');return{ok:true,json:async()=>GOOD};};
  const p=await bootPage(t,'W-Library/cases',reply),banner=()=>p.d.getElementById('service-down').hidden;
  await p.tick();mode='ok';await p.tick();mode='down';await p.tick();
  assert.equal(banner(),true);
});
test('H3 Reload service honours the unsaved-run confirm',async t=>{
  const b=await bootPage(t,'W-NewRun/run',()=>({ok:true,json:async()=>GOOD}));
  b.d.body.dataset.draft='1';b.d.getElementById('new-run').hidden=false;
  b.w.confirm=()=>false;b.d.getElementById('reload-service').click();await settle();
  assert.deepEqual(b.errors.filter(m=>/navigation/i.test(m)),[]);
});
test('H3 Start clears the unsaved-run flag',async t=>{
  const p=emptyPage('W-NewRun/run',t),w=p.w,ID='run-1';
  w.setInterval=()=>1;w.clearInterval=()=>{};
  const review={ok:true,id:ID,review_id:'b'.repeat(64),issuer:'N',pathway:'covenant_refinancing',as_of:'2025-03-31',modules:[],module_details:[],config:'c',provider:'p',model:'m',effort:'e',cap_usd:'1',hold_usd:'1',max_turns:1,prices_as_of:'x',provider_ready:true,provider_key:'K',sources:[],ignored:[],report_sections:[],omitted:[],scope:'s'};
  w.fetch=async url=>({ok:true,json:async()=>url==='/api/runs/review'?review:url==='/api/runs/start'?{state:'running',id:ID}:url.startsWith('/api/runs/status')?{state:'running',message:'w',run_available:true}:[]});
  p.load();await settle();
  const d=w.document,ctx=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../../../cases/context/research-minimal.json'),'utf8'));
  w.dispatchEvent(new w.MessageEvent('message',{source:d.getElementById('context-editor').contentWindow,data:{type:'cpos:context',context:ctx,problems:[]}}));
  const input=d.getElementById('run-sources'),file=new w.File(['x'],'a.txt');
  Object.defineProperty(input,'files',{configurable:true,value:[file]});
  d.getElementById('review-run').click();await settle();
  assert.equal(d.body.dataset.draft,'1');
  const box=d.getElementById('run-confirm');box.checked=true;box.dispatchEvent(new w.Event('change'));
  d.getElementById('start-run').click();await settle();
  assert.equal(d.body.dataset.draft,undefined);
});
test('H3 reloading with an unsaved New run asks first',async t=>{
  const p=emptyPage('W-NewRun/run',t),w=p.w;
  w.fetch=async()=>({ok:true,json:async()=>[]});w.setInterval=()=>1;w.clearInterval=()=>{};
  p.load();await settle();
  const d=w.document,editor=d.getElementById('context-editor');
  const ctx=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../../../cases/context/research-minimal.json'),'utf8'));
  w.dispatchEvent(new w.MessageEvent('message',{source:editor.contentWindow,data:{type:'cpos:context',context:ctx,problems:[]}}));
  assert.equal(d.body.dataset.draft,'1');
  d.getElementById('another-run').hidden=false;d.getElementById('another-run').click();
  assert.equal(d.body.dataset.draft,undefined);
  const b=await bootPage(t,'W-NewRun/run',()=>({ok:true,json:async()=>GOOD}));
  b.d.body.dataset.draft='1';b.d.getElementById('new-run').hidden=false;
  b.w.confirm=()=>false;b.d.getElementById('reload-workspace').click();await settle();
  assert.deepEqual(b.errors.filter(m=>/navigation/i.test(m)),[]);
  b.w.confirm=()=>true;b.d.getElementById('reload-workspace').click();await settle();
  assert.equal(b.errors.filter(m=>/navigation/i.test(m)).length,1);
});
test('H4 a report whose file has gone says so at once, with Reload',async t=>{
  const dom=fixture('W-Calendar/events?c=tdg-002',500),w=dom.window,d=w.document;t.after(()=>w.close());
  const heads=[];w.fetch=async(url,o)=>{heads.push(o.method);return{ok:false,status:404};};
  const report=w.eval('window.DESIGN_WORKSPACE.reports[0]');
  await go(w,`W-Reports/${report.id}`);
  const s=d.querySelector('.frame-status');
  assert.match(text(s),/could not be found/);assert.ok(s.querySelector('button'));assert.equal(s.querySelector('.frame-retry'),null);
  assert.equal(heads[0],'HEAD');
});
test('H4 a 404 page loading after the missing answer does not hide it',async t=>{
  const dom=fixture('W-Calendar/events?c=tdg-002',500),w=dom.window,d=w.document;t.after(()=>w.close());
  w.fetch=async()=>({ok:false,status:404});
  await go(w,`W-Reports/${w.eval('window.DESIGN_WORKSPACE.reports[0].id')}`);
  d.getElementById('report-preview').dispatchEvent(new w.Event('load'));
  const s=d.querySelector('.frame-status');
  assert.equal(s.hidden,false);assert.match(text(s),/could not be found/);
});
test('H4 a failed request for the file also says it could not be found',async t=>{
  const dom=fixture('W-Calendar/events?c=tdg-002',500),w=dom.window,d=w.document;t.after(()=>w.close());
  w.fetch=async()=>{throw new Error('down');};
  await go(w,`W-Reports/${w.eval('window.DESIGN_WORKSPACE.reports[0].id')}`);
  assert.match(text(d.querySelector('.frame-status')),/could not be found/);
});
test('H4 a present file keeps the loading state until the frame loads',async t=>{
  const dom=fixture('W-Calendar/events?c=tdg-002',500),w=dom.window,d=w.document;t.after(()=>w.close());
  w.fetch=async()=>({ok:true,status:200});
  const report=w.eval('window.DESIGN_WORKSPACE.reports[0]');
  await go(w,`W-Reports/${report.id}`);
  assert.equal(text(d.querySelector('.frame-status')),'Loading report…');
});
test('H5 an Evidence tab with no retained files says so',async t=>{
  const w=fixture('W-Overview/overview?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  w.eval('contexts["tdg-002"].modules={}');
  await go(w,'W-Evidence/sources?c=tdg-002');
  assert.match(text(d.getElementById('content')),/No retained files for this run/);
  assert.ok(d.querySelector('#content a[href="#W-Library/cases"]'));
});

test('layout: toggle label, issuer title, library band offset and row labels', async t=>{
  const w=fixture('W-Reports/list?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  assert.equal(text(d.getElementById('module-toggle')),'Browse modules');
  await go(w,'W-Overview/overview?c=tdg-002');
  const h1=d.querySelector('.issuer h1');
  assert.ok(h1.getAttribute('title'));assert.equal(h1.getAttribute('title'),h1.textContent);
  await go(w,'W-Library/cases');
  assert.equal(d.querySelector('.library-workspace').style.getPropertyValue('--band-h'),'-8px');
  await go(w,'W-Overview/overview?c=tdg-002');
  assert.ok(!d.getElementById('workbench').style.cssText.includes('--band-h'));
  await go(w,'W-Library/cases');
  const cells=[...d.querySelectorAll('.run-row td:not(:first-child):not(.row-open), .issuer-row td:not(.row-open)')];
  assert.ok(cells.length>0);
  for(const c of cells)assert.ok(c.dataset.label,c.outerHTML);
  assert.deepEqual([...new Set(cells.map(c=>c.dataset.label))].sort(),['Period','Reports','Run','Workflow']);
});

test('a group stays open across searches because its state is keyed by the issuer key',async t=>{
  const w=fixture('W-Library/cases').window,d=w.document;t.after(()=>w.close());
  const group=()=>d.querySelector('tbody.run-list[data-group="id:tdg"]');
  group().querySelector('.run-toggle').click();
  assert.equal(group().querySelector('.run-toggle').getAttribute('aria-expanded'),'true');
  assert.deepEqual([...w.eval('expandedIssuers')],['id:tdg']);
  const box=d.getElementById('library-query');
  box.value='transdigm';box.dispatchEvent(new w.Event('input',{bubbles:true}));
  assert.equal(group().querySelector('.run-toggle').getAttribute('aria-expanded'),'true');
  assert.ok([...group().querySelectorAll('.run-row')].every(row=>!row.hidden));
});

test('other runs of the issuer are found by issuer key, never by display name, and an unrecorded run matches nothing',async t=>{
  const w=fixture('W-Library/cases').window,d=w.document;t.after(()=>w.close());
  const module=w.eval(`Object.keys(moduleNames).find(m=>isAnalytical(m)&&contexts['tdg-003'].modules[m]?.outputs.length&&!contexts['tdg-002'].modules[m]?.outputs.length)`);
  assert.ok(module,'the fixture has a module tdg-003 holds and tdg-002 lacks');
  const others=()=>[...d.querySelectorAll('.available-case a')].map(a=>text(a)),third=w.eval(`contexts['tdg-003'].run`);
  const show=async()=>{await go(w,'W-Help/help');await go(w,`${module}?c=tdg-002`);};
  await show();
  assert.ok(others().includes(third),'a run of the same issuer is offered');
  w.eval(`contexts['tdg-003'].issuer='A different recorded name'`);await show();
  assert.ok(others().includes(third),'a different recorded name is still the same issuer');
  w.eval(`contexts['tdg-003'].issuerKey='id:someone-else'`);await show();
  assert.ok(!others().includes(third),'another key is another issuer');
  w.eval(`contexts['tdg-003'].issuerKey=null;contexts['tdg-002'].issuerKey=null`);await show();
  assert.deepEqual(others(),[],'an unrecorded issuer equals nothing, not even itself');
  assert.equal(w.eval('sameIssuer(null,null)'),false);
  assert.equal(w.eval('issuerReports("tdg-002").length'),0);
});

test('the section bar leads with the run and the module or destination name',async t=>{
  const w=fixture('CP-1/performance?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  const prefix=()=>d.querySelector('#section-nav .section-context');
  assert.equal(text(prefix()),'TDG-002 · Financial foundation');
  assert.equal(d.querySelector('#section-nav').firstElementChild,prefix());
  await go(w,'W-Forecast/forecast?c=tdg-002');
  assert.equal(text(prefix()),'TDG-002 · Forecast');
  await go(w,'W-Reports/list?c=tdg-002');
  assert.equal(text(prefix()),'TDG-002 · Reports');
  for(const destination of ['W-Library/cases','W-NewRun/new','W-Settings/settings','W-Help/help']){
    await go(w,`${destination}?c=tdg-002`);
    assert.equal(prefix(),null,`${destination} must not carry a run prefix`);
  }
  // A run label that holds markup is shown as text.
  w.eval(`contexts['tdg-002'].run='<b id=x>R</b>'`);
  await go(w,'CP-2/assessment?c=tdg-002');
  assert.equal(d.querySelector('#section-nav b#x'),null);
  assert.equal(text(prefix()),`<b id=x>R</b> · ${w.eval('moduleNames["CP-2"]')}`);
});

test('Overview charts carry their period, name their bars, and the lead is not repeated',t=>{
  const w=fixture('W-Overview/overview?c=tdg-002').window,d=w.document;t.after(()=>w.close());
  const bridge=[...d.querySelectorAll('.summary-chart')].find(c=>c.querySelector('.bridge-key'));
  assert.ok(bridge,'a waterfall chart is on the Overview');
  assert.equal(text(bridge.querySelector('.section-heading span')),'USD millions · FY2024 cash bridge · historical opening basis');
  assert.equal([...bridge.querySelectorAll('text.axis-label')].map(l=>[...l.querySelectorAll('tspan')].map(s=>s.textContent).join(' ')).join('|'),'Beginning cash|Operating cash flow|Investing cash flow|Financing cash flow|Exchange-rate effect|Calculated closing cash');
  assert.equal(bridge.querySelectorAll('.bridge-key b').length,0);
  const lead=text(d.querySelector('.summary-lead .call-quote'));
  assert.equal(text(d.body).split(lead).length-1,1);
  const owner=text(d.querySelector('.summary-lead .summary-owner'));
  assert.equal(d.querySelector(`.summary-card[data-module]`)&&[...d.querySelectorAll('.summary-card')].some(c=>text(c.querySelector('h3'))===owner),false);
  for(const s of d.querySelectorAll('.question-map>section'))assert.ok(s.querySelector('.summary-card'));
});

// Rail proximity: the rail opens 100 ms after the pointer is within 16 px of its right edge, closes 300 ms after it leaves.
function railFixture(coarse){
  const dom=fixture('W-Library/cases',undefined,w=>{w.matchMedia=query=>({matches:coarse&&query==='(hover: none), (pointer: coarse)',media:query});}),w=dom.window,rail=w.document.querySelector('.rail');
  rail.getBoundingClientRect=()=>({left:0,top:0,right:56,bottom:800,width:56,height:800});
  return {dom,w,rail,move:(x,pointerType='mouse')=>{const e=new w.MouseEvent('pointermove',{clientX:x,clientY:100,bubbles:true});Object.defineProperty(e,'pointerType',{value:pointerType});w.document.dispatchEvent(e);}};
}
test('rail items carry their names as visually hidden labels, found by data-place',t=>{
  const {w,rail}=railFixture(false);t.after(()=>w.close());
  const items=[...rail.querySelectorAll('[data-place]')];
  assert.deepEqual(items.map(i=>i.dataset.place),['Issuer library','Research workspace','Reports','Run activity','New run','Search','Settings','Help']);
  for(const item of items){
    assert.equal(item.querySelector('.rail-label').textContent,item.dataset.place);
    assert.equal(item.textContent.trim(),item.dataset.place);
    assert.equal(item.hasAttribute('title'),false);assert.equal(item.hasAttribute('aria-label'),false);
  }
  assert.equal(rail.querySelector('a[href="#W-Library/cases"] .symbol'),null);
  const symbol=rail.querySelector('img.symbol');assert.ok(symbol);assert.equal(symbol.closest('a'),null);
});
test('rail opens within 16 px of its edge after 100 ms and closes 300 ms after the pointer leaves',async t=>{
  const {w,rail,move}=railFixture(false);t.after(()=>w.close());
  move(66);assert.equal(rail.classList.contains('rail-open'),false);
  await settle(160);assert.equal(rail.classList.contains('rail-open'),true);
  move(200);await settle(150);assert.equal(rail.classList.contains('rail-open'),true);
  await settle(300);assert.equal(rail.classList.contains('rail-open'),false);
});
test('rail stays closed with the pointer 40 px away, and re-entering cancels a pending close',async t=>{
  const {w,rail,move}=railFixture(false);t.after(()=>w.close());
  move(96);await settle(160);assert.equal(rail.classList.contains('rail-open'),false);
  move(72);await settle(160);assert.equal(rail.classList.contains('rail-open'),true);
  move(200);await settle(150);move(30);await settle(400);assert.equal(rail.classList.contains('rail-open'),true);
  move(200);move(30);await settle(0);
  move(96);await settle(50);move(66);await settle(160);assert.equal(rail.classList.contains('rail-open'),true);
});
test('leaving the zone cancels a pending open',async t=>{
  const {w,rail,move}=railFixture(false);t.after(()=>w.close());
  move(66);await settle(30);move(200);await settle(200);assert.equal(rail.classList.contains('rail-open'),false);
});
test('a coarse pointer or no hover never opens the rail by proximity',async t=>{
  const {w,rail,move}=railFixture(true);t.after(()=>w.close());
  move(10);await settle(200);assert.equal(rail.classList.contains('rail-open'),false);
});
test('a touch or pen pointer never opens the rail by proximity',async t=>{
  const {w,rail,move}=railFixture(false);t.after(()=>w.close());
  move(66,'touch');move(66,'pen');await settle(200);assert.equal(rail.classList.contains('rail-open'),false);
});

// Task 13: Forecast wiring and report routing (adversarial review).
function bare(hash,models){
  const dom=new JSDOM(html,{url:`file://${__dirname}/index.html#${hash}`,runScripts:'outside-only'}),w=dom.window;
  w.scrollTo=()=>{};w.fetch=()=>new Promise(()=>{});w.HTMLElement.prototype.scrollIntoView=function(){};
  w.eval(`window.DESIGN_DATA={runs:{},outputs:{},inputs:{},pins:{}};window.DESIGN_WORKSPACE={reports:[],models:${JSON.stringify(models)},visuals:[]};window.DESIGN_APP={workspace:'',policy_locked:false,issues:[],problem:''};`);
  let error=null;
  try{for(const name of ['views.js','actions.js','screen.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,name),'utf8'),dom.getInternalVMContext());}catch(e){error=e;}
  return {w,error};
}
test('every route renders in a workspace with no run, whatever it holds',t=>{
  const model={id:'m-1',issuerKey:'id:ex',mode:'candidate',qualification:null,runId:'r-1',scope:null,inputContract:null,revisionNote:null,previous:null,href:'/files/deliverables/m-1/model.html?sha256=0',download:'/files/x',files:[],sources:[],register:null,cashflow:null};
  for(const hash of ['W-Library/cases','W-Forecast/forecast','W-Forecast/m-1','W-Reports/list','W-Reports/x','W-Settings/settings','CP-OS/activity']){
    const {w,error}=bare(hash,[model]);t.after(()=>w.close());
    assert.equal(error,null,`${hash}: ${error&&error.message}`);
    assert.ok(w.document.getElementById('content').textContent.trim().length>0,hash);
  }
});
test("another issuer's model, or one with no recorded issuer, is not a run's published model",async t=>{
  const w=fixture('W-Forecast/tdg-model-1?c=tdg-002').window;t.after(()=>w.close());
  const base=JSON.parse(JSON.stringify(w.DESIGN_WORKSPACE.models[0])),folder=w.eval('contexts["tdg-002"].folder');
  const foreign=Object.assign(JSON.parse(JSON.stringify(base)),{id:'beta-model',runId:folder,issuerKey:'id:bet',sources:[]});
  const unkeyed=Object.assign(JSON.parse(JSON.stringify(base)),{id:'null-model',runId:folder,issuerKey:null,sources:[]});
  const own=Object.assign(JSON.parse(JSON.stringify(base)),{id:'own-model',runId:folder,sources:[]});
  // Naming the run in its sources does not make another issuer's model the run's own when its runId is elsewhere.
  const reach=Object.assign(JSON.parse(JSON.stringify(base)),{id:'reach-model',runId:'elsewhere',issuerKey:'id:bet',sources:[{run:'tdg-002'}]});
  w.DESIGN_WORKSPACE.models.push(foreign,unkeyed,own,reach);
  await go(w,'W-Forecast/own-model?c=tdg-002');
  const options=[...w.document.querySelectorAll('#model-select option')].map(o=>o.textContent);
  assert.ok(options.some(o=>o.startsWith('own-model')),JSON.stringify(options));
  assert.equal(options.some(o=>o.startsWith('beta-model')||o.startsWith('null-model')||o.startsWith('reach-model')),false,JSON.stringify(options));
});
test("a report built from a run opens under that run even when its issuer differs from the run's",async t=>{
  const w=fixture('W-Reports/list?c=tdg-002').window;t.after(()=>w.close());
  const copy=Object.assign(JSON.parse(JSON.stringify(w.DESIGN_WORKSPACE.reports[0])),{id:'erste-parse',issuerKey:null});
  copy.builtFrom=copy.builtFrom.map(b=>({...b,run:'tdg-002'}));
  w.DESIGN_WORKSPACE.reports.push(copy);
  await go(w,'W-Library/cases');await go(w,'W-Reports/list?c=tdg-002');
  assert.ok([...w.document.querySelectorAll('.report-row a')].some(a=>a.getAttribute('href').includes('erste-parse')));
  await go(w,'W-Reports/erste-parse?c=tdg-002');
  assert.ok(w.document.getElementById('report-preview'),text(w.document.getElementById('content')).slice(0,120));
  assert.equal(w.eval('current.context'),'tdg-002');
});
test('the Report select lists the same reports as the report tabs and selects the open one under the built-from route',async t=>{
  const w=fixture('W-Reports/list?c=tdg-002').window;t.after(()=>w.close());
  const copy=Object.assign(JSON.parse(JSON.stringify(w.DESIGN_WORKSPACE.reports[0])),{id:'erste-parse',issuerKey:null});
  copy.builtFrom=copy.builtFrom.map(b=>({...b,run:'tdg-002'}));
  w.DESIGN_WORKSPACE.reports.push(copy);
  await go(w,'W-Library/cases');await go(w,'W-Reports/erste-parse?c=tdg-002');
  const select=w.document.getElementById('report-select');
  assert.equal(select.value,'erste-parse');
  const tabs=[...w.eval('reportSections("tdg-002")')].filter(s=>s[0]!=='list').map(s=>s[0]).sort();
  assert.deepEqual([...select.options].map(o=>o.value).sort(),[...tabs]);
});
test('an Other models row links only to a run whose Forecast lists that model',async t=>{
  const w=fixture('W-Forecast/forecast?c=tdg-002').window;t.after(()=>w.close());
  const base=w.DESIGN_WORKSPACE.models[0],keys=w.eval('Object.fromEntries(Object.entries(contexts).map(([k,c])=>[k,[c.issuerKey,c.folder]]))');
  const mine=keys['tdg-002'][0],elsewhere=Object.values(keys).find(([key])=>key!==mine);
  assert.ok(elsewhere);
  // The model has tdg-002's issuer key but names a run of another issuer: no run lists it on its Forecast.
  w.DESIGN_WORKSPACE.models.splice(0,w.DESIGN_WORKSPACE.models.length,Object.assign(JSON.parse(JSON.stringify(base)),{id:'stray-model',issuerKey:mine,runId:elsewhere[1],sources:[]}));
  await go(w,'W-Library/cases');await go(w,'W-Forecast/forecast?c=tdg-002');
  const section=w.document.querySelector('.forecast-other');
  assert.ok(section,'the Other models list is shown');
  assert.match(text(section),/stray-model/);
  assert.equal(section.querySelector('a'),null,'no link to a Forecast page that lists nothing');
});
test('the rail closes 300 ms after the pointer leaves it for an embedded frame',async t=>{
  const {w,rail,move}=railFixture(false);t.after(()=>w.close());
  move(66);await settle(160);assert.equal(rail.classList.contains('rail-open'),true);
  rail.dispatchEvent(new w.Event('pointerleave'));
  await settle(150);assert.equal(rail.classList.contains('rail-open'),true);
  await settle(300);assert.equal(rail.classList.contains('rail-open'),false);
});
test('the cash flow grid reads cell status and column ytd, never the display or label text',async t=>{
  const w=fixture('W-Forecast/tdg-model-1?c=tdg-002').window;t.after(()=>w.close());
  const cf=w.DESIGN_WORKSPACE.models[0].cashflow,d=w.document;
  const ytdColumns=cf.columns.filter(c=>c.ytd).length;
  assert.ok(ytdColumns>0&&cf.columns.some(c=>!c.ytd));
  cf.columns[cf.columns.findIndex(c=>c.ytd)].label='Q1 FY1 (YTD)';
  const plain=cf.columns.find(c=>!c.ytd);plain.label='Looks (YTD)';
  const cell=cf.rows[0].cells.find(c=>c.status==='value');
  cell.display='n.a.';cell.reason='text only';
  const gone=cf.rows.flatMap(r=>r.cells).find(c=>c.status==='gap');
  gone.status='na';gone.display='shown as text';gone.reason='by status';
  await go(w,'W-Library/cases');await go(w,'W-Forecast/tdg-model-1?c=tdg-002');
  assert.equal(d.querySelectorAll('.cashflow thead .col-sub').length,ytdColumns);
  const lines=[...d.querySelectorAll('.cashflow-na li')].map(li=>li.textContent);
  assert.equal(lines.some(l=>l.includes('text only')),false,lines.join('|'));
  assert.ok(lines.some(l=>l.endsWith('by status')),lines.join('|'));
});
