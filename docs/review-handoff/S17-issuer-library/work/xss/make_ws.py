import hashlib, json, shutil, sys
from pathlib import Path
REPO=Path('/workspace/final-workflow'); ws=Path(sys.argv[1])
shutil.rmtree(ws,ignore_errors=True); (ws/'runs').mkdir(parents=True)
shutil.copytree(REPO/'runs/tdg-002', ws/'runs/tdg-002')
f=ws/'runs/tdg-002/CP-1-attempt-2.md'; t=f.read_text()
old='| Net sales | 7,940 | 6,585 | 5,429 |'; assert old in t
f.write_text(t.replace(old,'| Net sales | <img src=q onerror=window.__xss1=1> | 6,585 | 5,429 |'))
# control: hostile cell in an ordinary handoff, rendered through esc()/rich()
evil='x"><img src=q onerror=window.__xss2=1>'
d=ws/'runs/acme-001'/'deliveries'/evil; d.mkdir(parents=True)
(d/'CP-3.md').write_text('# CP-3\n\n## Findings\n\nControl <img src=q onerror=window.__ctl=1> text.\n\n## Chart data: leverage\n\n| Period | Leverage | Reporting unit | Basis and limitation |\n|---|---|---|---|\n| FY2024 | 5.1 | x | reported |\n')
(ws/'runs/acme-001/workflow.json').write_text(json.dumps({'run':{'issuer_name':'Acme','as_of':'2024-12-31','pathway':'credit_snapshot'}}))
rid='r"><img src=q onerror=window.__xss3=1>'
r=ws/'deliverables'/rid; r.mkdir(parents=True)
files={}
for n,c in {'report.html':'<html><body>r</body></html>','view.json':json.dumps({'run':{'issuer_id':'acme','issuer_name':'Acme','run_id':'acme-001','as_of':'2024-12-31'}})}.items():
    (r/n).write_text(c); files[n]=hashlib.sha256(c.encode()).hexdigest()
(r/'delivery.json').write_text(json.dumps({'files':files,'scope':'x'}))
cat={'workspace':str(ws),'issues':[],'real':[
 {'id':'tdg-002','name':'TransDigm','artifacts':[]},
 {'id':'acme-001','name':'Acme','artifacts':[{'folder':f'deliverables/{rid}','available':True,'label':rid,'href':'/files/x/report.html?sha256='+files['report.html']}]}]}
(ws.parent/'catalogue.json').write_text(json.dumps(cat))
print('ok')
