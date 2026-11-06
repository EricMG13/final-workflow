/* The run status line never shows a stale spend. Plain node (no jsdom): showStatus is lifted from the
   real actions.js into a vm context with stub elements. Synthetic statuses only; no network or provider. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const source=fs.readFileSync(path.join(__dirname,'actions.js'),'utf8');
const grab=(name,indent)=>{const m=source.match(new RegExp(`^${indent}function ${name}\\([^)]*\\)\\{[\\s\\S]*?\\n${indent}\\}`,'m'));assert.ok(m,name);return m[0];};
const line=start=>{const m=source.match(new RegExp(`^const ${start}.*$`,'m'));assert.ok(m,start);return m[0];};
function spendText(status){
  const elements={};
  const context=vm.createContext({elements,$:id=>elements[id]??={hidden:false,textContent:'',dataset:{}},review:null});
  vm.runInContext([line('WORKFLOW_ACTIVE'),line('workflowTitle'),grab('titleOf','  '),grab('describeModule','  '),grab('showStatus','  ')].join('\n'),context);
  context.showStatus(status);
  return elements['run-spend'].textContent;
}
const stale={module:'CP-1',step:'started',spent_usd:'0'};

test('an unreadable ledger is shown as unreadable, not as the stale progress figure',()=>{
  assert.equal(spendText({state:'failed',message:'x',spent_usd:'unknown',progress:stale}),'Recorded spend could not be read; it may be above zero.');
});
test('a recorded spend wins over progress, and progress is the fallback while running',()=>{
  assert.equal(spendText({state:'stopped',message:'x',spent_usd:'7.42',progress:stale}),'Recorded spend: USD 7.42');
  assert.equal(spendText({state:'running',message:'x',progress:{...stale,spent_usd:'0.10'}}),'Recorded spend: USD 0.10');
  assert.equal(spendText({state:'running',message:'x'}),'Spend appears after CP-OS records a completed model response.');
});
