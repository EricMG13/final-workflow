// Repro: boot.js reload guard skips the confirm when a draft exists but the New run screen is hidden.
const fs=require('fs');
const src=fs.readFileSync('/home/user/final-workflow/apps/issuer-library/web/boot.js','utf8');
const els={};const el=id=>els[id]||(els[id]={id,hidden:true,handlers:{},addEventListener(t,f){this.handlers[t]=f;}});
let confirmed=0,reloaded=0;
global.document={body:{dataset:{}},getElementById:el,createElement:()=>({}),head:{append(s){setTimeout(()=>s.onload(),0);}}};
global.window={confirm:()=>{confirmed++;return false;}};
global.location={reload:()=>{reloaded++;}};
global.fetch=async()=>({ok:true,json:async()=>({real:[]})});
global.setInterval=()=>0;
eval(src);
setTimeout(()=>{
  document.body.dataset.draft='1';      // a prepared run (actions.js sets this)
  el('new-run').hidden=true;            // reader moved to Help; draft kept (browser_check checks this)
  el('reload-workspace').handlers.click();
  console.log('draft=1, new-run hidden -> confirm calls:',confirmed,'reloads:',reloaded);
  el('new-run').hidden=false;
  el('reload-workspace').handlers.click();
  console.log('draft=1, new-run shown  -> confirm calls:',confirmed,'reloads:',reloaded);
},20);
