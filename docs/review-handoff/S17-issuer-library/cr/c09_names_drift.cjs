// Compare report-adapter.js MODULE_NAMES with screen.js groups+aliases.
const fs=require('fs'),W='/home/user/final-workflow/apps/issuer-library/web/';
const ra=fs.readFileSync(W+'report-adapter.js','utf8'),sc=fs.readFileSync(W+'screen.js','utf8');
const MN=JSON.parse(ra.match(/const MODULE_NAMES=(\{.*?\});/)[1]);
const groups=eval(sc.match(/const groups = (\[[\s\S]*?\n\]);/)[1]);
const aliases=eval('('+sc.match(/const aliases = (\{.*?\});/)[1]+')');
const names={};for(const [,items] of groups)for(const [id,name] of items)names[id]=name;
for(const [a,t] of Object.entries(aliases))names[a]??=names[t];
const diff=[];for(const k of new Set([...Object.keys(MN),...Object.keys(names)]))if(MN[k]!==names[k])diff.push([k,MN[k],names[k]]);
console.log(diff.length?diff:'identical (static parts)');
