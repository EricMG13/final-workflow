/* A run being prepared is never cleared by a reload without asking, whichever screen is showing.
   Plain node (no jsdom): boot.js runs in a vm context with stub elements; installSettings, watchFrame and
   the shared guard are lifted from the real actions.js and views.js. Synthetic state only; no network or provider. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const read=name=>fs.readFileSync(path.join(__dirname,name),'utf8');
const settle=()=>new Promise(resolve=>setTimeout(resolve,20));
const guard=read('views.js').match(/^const mayDiscardDraft=.*$/m)[0];

async function boot({draft,newRunHidden,answer}){
  const elements={},calls={confirm:0,reload:0};
  const element=id=>elements[id]??={hidden:true,handlers:{},addEventListener(type,fn){this.handlers[type]=fn;}};
  const context=vm.createContext({
    document:{body:{dataset:draft?{draft:'1'}:{}},getElementById:element,createElement:()=>({}),head:{append:script=>setTimeout(()=>script.onload(),0)}},
    window:{confirm:()=>{calls.confirm++;return answer;}},
    location:{reload:()=>{calls.reload++;}},
    fetch:async()=>({ok:true,json:async()=>({real:[]})}),
    setInterval:()=>0,setTimeout,console,JSON,Promise,watchRuns:()=>{},
  });
  vm.runInContext(read('boot.js'),context);
  await settle();
  element('new-run').hidden=newRunHidden;
  return {click:id=>element(id).handlers.click(),calls};
}

test('Reload asks before clearing a prepared run while another screen is shown',async()=>{
  // Expected by hand: a draft asks once whether or not #new-run is visible; "Cancel" keeps the page.
  for(const newRunHidden of [true,false])for(const id of ['reload-workspace','reload-service']){
    const page=await boot({draft:true,newRunHidden,answer:false});
    page.click(id);
    assert.deepEqual(page.calls,{confirm:1,reload:0},`${id} hidden=${newRunHidden}`);
  }
  const accepted=await boot({draft:true,newRunHidden:true,answer:true});
  accepted.click('reload-workspace');
  assert.deepEqual(accepted.calls,{confirm:1,reload:1});
  const none=await boot({draft:false,newRunHidden:true,answer:false});
  none.click('reload-workspace');
  assert.deepEqual(none.calls,{confirm:0,reload:1});
});

function settings({draft,answer}){
  const source=read('actions.js'),grabbed=source.match(/^function installSettings\(\)\{[\s\S]*?\n\}/m);
  assert.ok(grabbed,'installSettings');
  const elements={},calls={confirm:0,reload:0,requests:[]};
  let onClick=null;
  const context=vm.createContext({
    $:id=>elements[id]??={disabled:false,textContent:'',value:' /research '},
    appRequest:async url=>{calls.requests.push(url);return{};},
    document:{body:{dataset:draft?{draft:'1'}:{}},addEventListener:(type,fn)=>{onClick=fn;}},
    window:{confirm:()=>{calls.confirm++;return answer;},DESIGN_APP:{policy_locked:false}},
    location:{reload:()=>{calls.reload++;}},
  });
  vm.runInContext(`${guard}\nlet settingsBusy=false;\n${grabbed[0]}\ninstallSettings();`,context);
  return {click:async id=>{await onClick({target:{closest:selector=>selector===`#${id}`}});},calls};
}

test('Settings save and refresh ask before clearing a prepared run, and send nothing on Cancel',async()=>{
  // Expected by hand: with a draft, Cancel sends no request and does not reload; OK sends one and reloads.
  for(const [id,url] of [['save-workspace','/api/settings'],['refresh-library','/api/refresh']]){
    const kept=settings({draft:true,answer:false});
    await kept.click(id);
    assert.deepEqual(kept.calls,{confirm:1,reload:0,requests:[]},id);
    const cleared=settings({draft:true,answer:true});
    await cleared.click(id);
    assert.deepEqual(cleared.calls,{confirm:1,reload:1,requests:[url]},id);
    const plain=settings({draft:false,answer:false});
    await plain.click(id);
    assert.deepEqual(plain.calls,{confirm:0,reload:1,requests:[url]},id);
  }
});

test('the Reload offered for a deliverable that has gone asks before clearing a prepared run',async()=>{
  // Expected by hand: the HEAD check fails, so the frame status offers Reload; with a draft it asks once
  // and Cancel keeps the page; without one it reloads at once.
  const source=read('views.js'),grabbed=source.match(/^function watchFrame\([^)]*\) \{[\s\S]*?\n\}/m);
  assert.ok(grabbed,'watchFrame');
  for(const [draft,answer,expected] of [[true,false,{confirm:1,reload:0}],[true,true,{confirm:1,reload:1}],[false,false,{confirm:0,reload:1}]]){
    const calls={confirm:0,reload:0},buttons=[];
    const node=()=>({listeners:{},addEventListener(type,fn){this.listeners[type]=fn;},removeEventListener(){},append(...items){buttons.push(...items.filter(item=>item.listeners));}});
    const context=vm.createContext({
      document:{body:{dataset:draft?{draft:'1'}:{}},createElement:()=>node()},
      window:{confirm:()=>{calls.confirm++;return answer;}},
      location:{reload:()=>{calls.reload++;}},
      fetch:async()=>({ok:false}),setTimeout:()=>0,clearTimeout:()=>{},
    });
    vm.runInContext(`${guard}\nconst frameTimeout=()=>60000;\n${grabbed[0]}`,context);
    const frame={...node(),isConnected:true,getAttribute:()=>'/files/r/report.html'},status={...node(),hidden:true,textContent:''};
    context.watchFrame(frame,status,'Loading','Failed',null,'This deliverable could not be found.');
    await settle();
    assert.equal(buttons.length,1);
    buttons[0].listeners.click();
    assert.deepEqual(calls,expected,`draft=${draft} answer=${answer}`);
  }
});
