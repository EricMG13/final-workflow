// Repro: the comparison chart prints a fixed 'Not available' for the launcher's `Not supplied: <reason>` cells.
const fs=require('fs');
const v=fs.readFileSync('/home/user/final-workflow/apps/issuer-library/web/views.js','utf8');
const plain=value=>String(value).replace(/\*\*|`/g,'');   // screen.js:47
eval(v.match(/function chartNumber\(value\) \{[\s\S]*?\n\}/)[0]);
for(const cell of ['1,234.5','Not supplied: reported in EUR m','(5.0%)','−1.2']){
  const n=chartNumber(cell);
  console.log(JSON.stringify(cell),'->',n===null?'Not available':n);   // views.js:121 strong text
}
