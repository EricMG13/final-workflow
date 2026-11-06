// Repro step 2: views.js comparisonChart (used by readerCharts and the Overview's summaryCharts) puts the output id raw into data-evidence.
const fs=require('fs');
const v=fs.readFileSync('/home/user/final-workflow/apps/issuer-library/web/views.js','utf8');
const s=JSON.parse(fs.readFileSync(__dirname+'/xss-store.json','utf8'));
const data=s.outputs;
const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));   // screen.js:44
const plain=value=>String(value).replace(/\*\*|`/g,'');
const rich=value=>esc(value);
const grab=name=>v.match(new RegExp(`function ${name}\\([^)]*\\) \\{[\\s\\S]*?\\n\\}`))[0];
eval([grab('fixtureTable'),grab('chartNumber'),grab('chartIntro'),grab('comparisonChart')].join('\n'));
const id=Object.keys(data)[0];
const html=comparisonChart(id,{kind:'bars',...data[id].charts[0]});
const m=html.match(/<button class="chart-row" data-evidence="[^"]*"[^<]*<img[^>]*>/);
console.log(m?m[0]:'no injection');
