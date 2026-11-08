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
const same=(a,b,m)=>assert.equal(JSON.stringify(a),JSON.stringify(b),m);
const pick=(p,id)=>{const choice=p.doc.getElementById(id);choice.checked=true;choice.dispatchEvent(new p.win.Event('change',{bubbles:true}));};
const declare=p=>{pick(p,'issue_classification-high_yield');pick(p,'legal_documents-executed');};
test('one required context path retains all original optional fields',t=>{
 const p=form(t);for(const id of ['sec1','sec2','sec3'])assert.equal(p.doc.getElementById(id).hidden,false);
 assert.equal(p.win.getComputedStyle(p.doc.querySelector('.stepnav')).display,'none');
 assert.equal(p.doc.querySelector('#sec2 details').open,false);assert.ok(p.doc.getElementById('s2-guarantors'));
 assert.equal(p.submit().problems.length,4);assert.equal(p.doc.activeElement.id,'s2-issuer_name');
 p.set('s2-issuer_name','Synthetic Émetteur');p.set('s3-reporting_currency','EUR');declare(p);
 const result=p.submit();assert.equal(result.problems.length,0);assert.equal(result.context.identity.issuer_name,'Synthetic Émetteur');assert.equal(result.context.run.reporting_currency,'EUR');
 assert.equal(result.context.identity.issue_classification,'high_yield');assert.equal(result.context.attachments.legal_documents,'executed');
});
test('the issue classification is visible after the issuer ID, required and not preselected',t=>{
 const p=form(t),box=p.doc.getElementById('classf');
 assert.equal(box.closest('details'),null);assert.equal(box.closest('section').id,'sec2');
 assert.ok(box.previousElementSibling.contains(p.doc.getElementById('s2-issuer_id')));
 assert.deepEqual([...box.querySelectorAll('input')].map(i=>[i.value,i.checked]),[['investment_grade',false],['high_yield',false]]);
 assert.match(box.textContent,/Investment grade/);assert.match(box.textContent,/High yield/);
 assert.match(box.textContent,/Classify by the debt this run analyses; for split-rated or unrated issuers use your firm's convention\. The workflow's methods are written for high-yield and leveraged-loan credit\./);
 assert.equal(box.querySelector('legend .rtag').textContent,'Required');
 assert.equal(p.doc.querySelector('[data-cards="legal_documents"]').closest('fieldset').querySelector('legend .rtag').textContent,'Required');
 assert.equal(p.doc.querySelectorAll('input[name="legal_documents"]:checked').length,0);
 assert.doesNotMatch(p.doc.body.textContent,/CP-4 refuses them today|draft mode|Planned\s*CP-4 draft/);
 assert.match(p.doc.querySelector('[data-cards="legal_documents"]').textContent,/Provisional/);
 assert.ok(p.submit().problems.some(value=>value.startsWith('Issue classification')&&value.endsWith('required.')));
 assert.ok(p.submit().problems.some(value=>value.startsWith('Legal documents')&&value.endsWith('required.')));
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
 const p=form(t);p.set('s2-issuer_name','Synthetic earnings');declare(p);
 const choice=p.doc.getElementById('run_type-earnings');choice.checked=true;choice.dispatchEvent(new p.win.Event('change',{bubbles:true}));
 assert.ok(p.submit().problems.some(value=>value.includes('Current period')));
 p.set('s3-current_period','q3-2026');p.set('s3-prior_period','q2-2026');assert.equal(p.submit().problems.length,0);
});
test('loading a context from before the classification existed asks for it and changes nothing else',async t=>{
 const p=form(t),input=p.doc.getElementById('load');
 const raw=fs.readFileSync(path.resolve(__dirname,'../../../cases/context/research-minimal.json'),'utf8');
 assert.equal(JSON.parse(raw).identity.issue_classification,undefined);
 Object.defineProperty(input,'files',{configurable:true,value:[new p.win.File([raw],'context.json',{type:'application/json'})]});input.dispatchEvent(new p.win.Event('change'));
 for(let attempt=0;attempt<30&&!p.doc.getElementById('loadmsg').textContent.startsWith('Loaded');attempt++)await new Promise(resolve=>setTimeout(resolve,5));
 assert.match(p.doc.getElementById('loadmsg').textContent,/Loaded context.json/);
 assert.match(p.doc.getElementById('loadmsg').textContent,/issue_classification: not stated in this file/);
 assert.equal(p.doc.activeElement.closest('section').id,'sec2');
 assert.equal(p.doc.querySelectorAll('input[name="issue_classification"]:checked').length,0);
 const first=p.submit();same(first.problems,['Issue classification: required.']);
 assert.equal(p.doc.getElementById('classf').querySelector('.err').textContent,'required.');
 pick(p,'issue_classification-investment_grade');
 const result=p.submit();assert.equal(result.problems.length,0);assert.equal(result.context.identity.issuer_name,'Northbridge Group');assert.equal(result.context.run.as_of,'2026-10-31');
 assert.equal(result.context.attachments.legal_documents,JSON.parse(raw).attachments.legal_documents);
 assert.equal(result.context.identity.issue_classification,'investment_grade');
});
test('a saved classification and facility terms load back into the form',async t=>{
 const p=form(t),input=p.doc.getElementById('load');
 const o=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../../../cases/context/research-minimal.json'),'utf8'));
 o.identity.issue_classification='high_yield';o.run.run_type='secondary';o.run.pathway='relative_value';
 o.deal_terms=[{facility_id:'tlb',instrument:'Term loan B',currency:'USD',size_m:'1250',tenor_years:'',talk_spread_bps_low:'',talk_spread_bps_high:'',talk_oid_low:'',talk_oid_high:'',floor_pct:'',coupon_pct:'8.25',margin_bps:'350',maturity:'2031-06-30',call_protection:'',use_of_proceeds:'',as_of:'',provider:''}];
 Object.defineProperty(input,'files',{configurable:true,value:[new p.win.File([JSON.stringify(o)],'context.json',{type:'application/json'})]});input.dispatchEvent(new p.win.Event('change'));
 for(let attempt=0;attempt<30&&!p.doc.getElementById('loadmsg').textContent.startsWith('Loaded');attempt++)await new Promise(resolve=>setTimeout(resolve,5));
 const result=p.submit();same(result.problems,[]);
 assert.equal(result.context.identity.issue_classification,'high_yield');
 same([result.context.deal_terms[0].coupon_pct,result.context.deal_terms[0].margin_bps,result.context.deal_terms[0].maturity],['8.25','350','2031-06-30']);
 assert.doesNotMatch(p.doc.getElementById('loadmsg').textContent,/tenor and price talk/);
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
 assert.match(css,/\.tag\.def \{[^}]*background:#F8F9FB;[^}]*color:#3A4056/);
});
test('the Default tag is the grey pill in sentence case, and the form text sizes are 13px and 11px',t=>{
 const p=form(t),tag=p.doc.querySelector('.tag.def');
 assert.ok(tag,'a Default tag is shown');
 assert.equal(tag.textContent,'Default');
 const s=p.win.getComputedStyle(tag);
 assert.equal(s.textTransform,'none');assert.equal(s.backgroundColor,'rgb(248, 249, 251)');assert.equal(s.color,'rgb(58, 64, 86)');assert.equal(s.borderRadius,'999px');
 const html=fs.readFileSync(path.join(__dirname,'context-form.html'),'utf8');
 assert.match(html,/--rb-fs-body: 13px;/);assert.match(html,/--rb-fs-micro: 11px;/);assert.doesNotMatch(html,/13\.5px|10\.5px/);
 assert.match(html,/\.tag\.def \{ background:#F8F9FB; border:1px solid #E4E6EC; color:#3A4056; text-transform:none;/);
 const css=fs.readFileSync(path.join(__dirname,'context-embed.css'),'utf8');
 assert.match(html,/\.badge-gray of screen\.css/);assert.match(css,/\.badge-gray of screen\.css/);
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

const facility=(p,values)=>{
 p.doc.querySelector('[data-add="deal"]').click();
 const row=p.doc.getElementById('rows-deal').lastElementChild;
 for(const [k,v] of Object.entries(values)){const field=row.querySelector(`[data-k="${k}"]`);field.value=v;field.dispatchEvent(new p.win.Event('input',{bubbles:true}));}
 return row;
};
const runType=(p,id)=>pick(p,'run_type-'+id);
const TALK=['tenor_years','talk_spread_bps_low','talk_spread_bps_high','talk_oid_low','talk_oid_high'];
test('facility rows are available on every run type and required only for Primary',t=>{
 const p=form(t);p.set('s2-issuer_name','Synthetic');declare(p);
 for(const type of ['secondary','research','primary','earnings']){
  runType(p,type);
  assert.equal(p.doc.getElementById('sec4').hidden,false,type);
  if(type==='earnings'){p.set('s3-current_period','q3-2026');p.set('s3-prior_period','q2-2026');}
  const problems=p.submit().problems;
  if(type==='primary'){assert.equal(problems.length,1);assert.match(problems[0],/add at least one facility row/);}
  else same(problems,[],type);
 }
 runType(p,'primary');facility(p,{facility_id:'tlb',size_m:'1250'});same(p.submit().problems,[]);
});
test('coupon, margin and maturity are plain non-negative numbers and a date (invalid dates cannot be typed into the date input)',t=>{
 const p=form(t);p.set('s2-issuer_name','Synthetic');declare(p);runType(p,'secondary');
 const row=facility(p,{facility_id:'tlb',coupon_pct:'8.25',margin_bps:'350',maturity:'2031-06-30'});
 let r=p.submit();same(r.problems,[]);
 same([r.context.deal_terms[0].coupon_pct,r.context.deal_terms[0].margin_bps,r.context.deal_terms[0].maturity],['8.25','350','2031-06-30']);
 for(const [k,v] of [['coupon_pct','8.25%'],['coupon_pct','-1'],['margin_bps','350bps'],['margin_bps','1,5'],['coupon_pct','1e3']]){
  const field=row.querySelector(`[data-k="${k}"]`),was=field.value;field.value=v;field.dispatchEvent(new p.win.Event('input',{bubbles:true}));
  assert.equal(p.submit().problems.length,1,k+' '+v);field.value=was;field.dispatchEvent(new p.win.Event('input',{bubbles:true}));
 }
 for(const k of ['coupon_pct','margin_bps','maturity']){const field=row.querySelector(`[data-k="${k}"]`);field.value='';field.dispatchEvent(new p.win.Event('input',{bubbles:true}));}
 r=p.submit();same(r.problems,[]);assert.equal(r.context.deal_terms[0].coupon_pct,'');assert.equal(r.context.deal_terms[0].maturity,'');
});
test('switching from Primary to Secondary blanks the hidden talk fields before build()',t=>{
 const p=form(t);p.set('s2-issuer_name','Synthetic');declare(p);runType(p,'primary');
 const row=facility(p,{facility_id:'tlb',size_m:'1250',tenor_years:'7',talk_spread_bps_low:'325',talk_spread_bps_high:'350',talk_oid_low:'99.0',talk_oid_high:'99.5',floor_pct:'0.50'});
 let deal=p.submit().context.deal_terms[0];
 for(const k of TALK)assert.notEqual(deal[k],'',k);
 runType(p,'secondary');
 for(const k of TALK)assert.equal(row.querySelector(`[data-k="${k}"]`).closest('.f').hidden,true,k);
 assert.equal(row.querySelector('[data-k="size_m"]').closest('.f').hidden,false);
 const result=p.submit();same(result.problems,[]);deal=result.context.deal_terms[0];
 for(const k of TALK)assert.equal(deal[k],'',k);
 assert.equal(deal.size_m,'1250');assert.equal(deal.floor_pct,'0.50');
 runType(p,'primary');deal=p.submit().context.deal_terms[0];assert.equal(deal.tenor_years,'7');assert.equal(deal.talk_oid_high,'99.5');
});
test('an invalid value in a hidden talk field is not an error on a Secondary run',t=>{
 const p=form(t);p.set('s2-issuer_name','Synthetic');declare(p);runType(p,'primary');
 facility(p,{facility_id:'tlb',talk_spread_bps_low:'400',talk_spread_bps_high:'300',tenor_years:'7%'});
 assert.ok(p.submit().problems.length>0);
 runType(p,'secondary');const result=p.submit();same(result.problems,[]);assert.equal(result.context.deal_terms[0].talk_spread_bps_low,'');
});
