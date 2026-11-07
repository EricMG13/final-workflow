/* Existing context form + embedded presentation, no browser/network/providers. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {JSDOM,VirtualConsole}=require(process.env.ISSUER_LIBRARY_JSDOM||'jsdom');
const html=fs.readFileSync(path.join(__dirname,'context-form.html'),'utf8');
function form(t){
 const errors=[],messages=[],console=new VirtualConsole();console.on('jsdomError',error=>errors.push(error));
 const dom=new JSDOM(html,{runScripts:'dangerously',virtualConsole:console,beforeParse(win){win.scrollTo=()=>{};win.matchMedia=()=>({matches:false,addEventListener(){},removeEventListener(){}});win.ResizeObserver=class{observe(){}};win.HTMLElement.prototype.scrollIntoView=function(){};win.postMessage=value=>messages.push(value);}});
 const win=dom.window,doc=win.document;
 t.after(()=>{assert.deepEqual(errors,[]);win.close();});
 return{win,doc,messages,set(id,value){const field=doc.getElementById(id);field.value=value;field.dispatchEvent(new win.Event('input',{bubbles:true}));},submit(){win.dispatchEvent(new win.MessageEvent('message',{source:win,data:{type:'cpos:get-context'}}));return messages.filter(item=>item.type==='cpos:context').at(-1);}};
}
test('one required context path retains all original optional fields',t=>{
 const p=form(t);for(const id of ['sec1','sec2','sec3'])assert.equal(p.doc.getElementById(id).hidden,false);
 assert.equal(p.win.getComputedStyle(p.doc.querySelector('.stepnav')).display,'none');
 assert.equal(p.doc.querySelector('#sec2 details').open,false);assert.ok(p.doc.getElementById('s2-guarantors'));
 assert.equal(p.submit().problems.length,2);assert.equal(p.doc.activeElement.id,'s2-issuer_name');
 p.set('s2-issuer_name','Synthetic Émetteur');p.set('s3-reporting_currency','EUR');
 const result=p.submit();assert.equal(result.problems.length,0);assert.equal(result.context.identity.issuer_name,'Synthetic Émetteur');assert.equal(result.context.run.reporting_currency,'EUR');
});
test('context destinations use visible disclosure names instead of removed numbering',t=>{
 const p=form(t),labels=[...p.doc.querySelectorAll('summary')].map(node=>node.textContent);
 for(const label of ['Deal terms','Quotes','Valuation'])assert.ok(labels.includes(label));
 assert.doesNotMatch(p.doc.body.textContent,/section [457]/i);
 assert.match(p.doc.getElementById('sec1').textContent,/Shows “Deal terms”/);
 assert.match(p.doc.getElementById('sec1').textContent,/Shows “Quotes”/);
 assert.match(p.doc.getElementById('sec2').textContent,/market cap and net debt in “Valuation”/);
});
test('earnings requirements and optional-section errors keep native validation',t=>{
 const p=form(t);p.set('s2-issuer_name','Synthetic earnings');
 const choice=p.doc.getElementById('run_type-earnings');choice.checked=true;choice.dispatchEvent(new p.win.Event('change',{bubbles:true}));
 assert.ok(p.submit().problems.some(value=>value.includes('Current period')));
 p.set('s3-current_period','q3-2026');p.set('s3-prior_period','q2-2026');assert.equal(p.submit().problems.length,0);
});
test('loading a valid saved context keeps focus on visible context for review',async t=>{
 const p=form(t),input=p.doc.getElementById('load');
 const raw=fs.readFileSync(path.resolve(__dirname,'../../../cases/context/research-minimal.json'),'utf8');
 Object.defineProperty(input,'files',{configurable:true,value:[new p.win.File([raw],'context.json',{type:'application/json'})]});input.dispatchEvent(new p.win.Event('change'));
 for(let attempt=0;attempt<30&&!p.doc.getElementById('loadmsg').textContent.startsWith('Loaded');attempt++)await new Promise(resolve=>setTimeout(resolve,5));
 assert.match(p.doc.getElementById('loadmsg').textContent,/Loaded context.json/);
 assert.equal(p.doc.activeElement.closest('section').id,'sec2');
 const result=p.submit();assert.equal(result.problems.length,0);assert.equal(result.context.identity.issuer_name,'Northbridge Group');assert.equal(result.context.run.as_of,'2026-10-31');
});
const INTRO='Name the issuer so CP-0 can confirm it and the filings can be matched.';
const sendNames=(p,names,source)=>p.win.dispatchEvent(new p.win.MessageEvent('message',{source:source===undefined?p.win:source,data:{type:'cpos:names',names}}));
const intro=p=>p.doc.querySelector('#sec2 .intro');
test('the names message replaces a visible module code with its name and keeps the code as a title',t=>{
 const p=form(t);assert.equal(intro(p).textContent,INTRO);
 sendNames(p,{'CP-0':'Source readiness'});
 assert.equal(intro(p).textContent,'Name the issuer so Source readiness can confirm it and the filings can be matched.');
 assert.equal(intro(p).title,'CP-0');
 assert.ok(!p.doc.getElementById('s2-borrower_name-h').textContent.includes('CP-0'));
});
test('a code with no name stays a code, and values and options keep codes',t=>{
 const p=form(t);p.doc.querySelector('[data-add="q"]').click();sendNames(p,{'CP-0':'Source readiness'});
 assert.match(p.doc.getElementById('s2-borrower_name-h').textContent,/CP-1 looks/);
 const option=[...p.doc.querySelectorAll('option')].find(o=>o.textContent==='CP-0');assert.ok(option);
 assert.equal(option.value,'CP-0');
});
test('names apply again when the form rewrites its own text',async t=>{
 const p=form(t);sendNames(p,{'CP-0':'Source readiness'});
 intro(p).textContent='Ask CP-0 first.';
 await new Promise(resolve=>setTimeout(resolve,20));
 assert.equal(intro(p).textContent,'Ask Source readiness first.');
});
test('the names message is ignored from another source or with a non-string value',t=>{
 const p=form(t),other=new JSDOM('').window;t.after(()=>other.close());
 sendNames(p,{'CP-0':'Source readiness'},other);assert.equal(intro(p).textContent,INTRO);
 sendNames(p,{'CP-0':'Source readiness'},null);assert.equal(intro(p).textContent,INTRO);
 sendNames(p,{'CP-0':'Source readiness','CP-1':{toString:()=>'x'}});assert.equal(intro(p).textContent,INTRO);
 sendNames(p,null);sendNames(p,'CP-0');assert.equal(intro(p).textContent,INTRO);
});
test('a name is written as text, never markup',t=>{
 const p=form(t);sendNames(p,{'CP-0':'<img src=x onerror=1>'});
 assert.equal(p.doc.querySelector('#sec2 .intro img'),null);assert.match(intro(p).textContent,/<img src=x onerror=1>/);
});
test('names leave the emitted context JSON unchanged',t=>{
 const before=form(t),after=form(t);
 for(const p of [before,after]){p.set('s2-issuer_name','Synthetic');p.set('s3-reporting_currency','EUR');}
 sendNames(after,{'CP-0':'Source readiness','CP-1':'Filing intake'});
 assert.match(intro(after).textContent,/Source readiness/);
 assert.equal(JSON.stringify(after.submit().context),JSON.stringify(before.submit().context));
});
test('the date help names the picker and keeps the saved format',t=>{
 const p=form(t),help=p.doc.getElementById('s3-as_of-h').textContent;
 assert.match(help,/Choose the date; it is saved as YYYY-MM-DD\./);assert.doesNotMatch(help,/Format YYYY-MM-DD/);
});
test('the form uses the app look: 40 px fields, 16 px text, pills and a styled file button',t=>{
 const p=form(t),css=fs.readFileSync(path.join(__dirname,'context-embed.css'),'utf8');
 for(const id of ['s2-issuer_name','s3-as_of']){const s=p.win.getComputedStyle(p.doc.getElementById(id));assert.equal(s.height,'40px');assert.equal(s.fontSize,'16px');assert.equal(s.borderRadius,'8px');}
 const select=p.win.getComputedStyle(p.doc.querySelector('.f select'));assert.equal(select.height,'40px');assert.match(css,/\.f select \{[^}]*background-image:url\("data:image\/svg\+xml/);
 assert.match(css,/::file-selector-button/);
 const req=p.win.getComputedStyle(p.doc.querySelector('.rtag.req'));assert.equal(req.backgroundColor,'rgb(248, 249, 251)');assert.equal(req.color,'rgb(58, 64, 86)');
 const rec=p.win.getComputedStyle(p.doc.querySelector('.rtag.rec'));assert.equal(rec.backgroundColor,'rgba(0, 0, 0, 0)');assert.equal(rec.borderTopColor,'rgb(207, 211, 221)');
 assert.match(css,/\.tag\.def \{[^}]*background:#E7ECFF;[^}]*color:#0017E5/);
});
const later=()=>new Promise(resolve=>setTimeout(resolve,20));
test('a host with several text nodes titles all their codes once, and loses the title when they go',async t=>{
 const p=form(t),host=intro(p);
 host.textContent='';host.append('Ask CP-0 then ',p.doc.createElement('br'),'CP-2 after.');
 sendNames(p,{'CP-0':'Source readiness','CP-2':'Review'});
 assert.equal(host.textContent,'Ask Source readiness then Review after.');
 assert.equal(host.title,'CP-0, CP-2');
 host.textContent='No codes here.';await later();
 assert.equal(host.hasAttribute('title'),false);
});
test('a title the host had before the script ran is never overwritten or removed',async t=>{
 const p=form(t),host=intro(p);host.title='Their own';
 sendNames(p,{'CP-0':'Source readiness'});
 assert.equal(host.title,'Their own');
 host.textContent='None.';await later();
 assert.equal(host.title,'Their own');
});
