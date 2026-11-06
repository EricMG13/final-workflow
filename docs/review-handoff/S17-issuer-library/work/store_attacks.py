"""Adversarial repros against apps/issuer-library/engine/store.py (read-only on repo)."""
import hashlib, json, subprocess, sys, tempfile, shutil
from pathlib import Path
REPO=Path('/workspace/final-workflow')
STORE=REPO/'apps/issuer-library/engine/store.py'
PY=str(REPO/'.venv/bin/python')

def run_store(ws, catalogue):
    p=subprocess.run([PY,'-I','-B','-X','utf8',str(STORE),str(ws)],input=json.dumps(catalogue).encode(),capture_output=True)
    return p.returncode, p.stdout.decode(), p.stderr.decode()[-400:]

GOOD="# CP-1\n\n## Findings\n\nNet debt was 10.\n"
def handoff(ws, run, name, text=GOOD):
    d=ws/'runs'/run; d.mkdir(parents=True,exist_ok=True); (d/name).write_text(text)

def delivery(ws, folder, issuer='Acme', extra=None):
    d=ws/folder; d.mkdir(parents=True)
    files={}
    for n,c in {'report.html':'<html></html>','view.json':json.dumps({'run':{'issuer_id':'acme','issuer_name':issuer,'run_id':'r1','as_of':'2024-12-31'}}),'CP-1.md':GOOD}.items():
        (d/n).write_text(c); files[n]=hashlib.sha256(c.encode()).hexdigest()
    (d/'delivery.json').write_text(json.dumps({'files':files,'scope':'x'}))
    if extra: extra(d)
    return {'folder':folder,'available':True,'label':Path(folder).name,'href':f'/files/{folder}/report.html?sha256={files["report.html"]}'}

def case1():
    print('== A: one handoff named CP-1x.md hides the whole run')
    ws=Path(tempfile.mkdtemp(dir=sys.argv[1]))
    handoff(ws,'acme-001','CP-1.md'); handoff(ws,'acme-001','CP-2.md',GOOD.replace('CP-1','CP-2'))
    handoff(ws,'acme-001','CP-1x.md',GOOD+'Draft.\n')
    rc,out,err=run_store(ws,{'issues':[],'real':[{'id':'acme-001','name':'Acme','artifacts':[]}]})
    d=json.loads(out); print('rc',rc,'runs:',list(d['runs']),'issues:',d['issues'])

def case2():
    print('== B: a directory named CP-notes.md inside a verified delivery breaks the whole store')
    ws=Path(tempfile.mkdtemp(dir=sys.argv[1]))
    handoff(ws,'acme-001','CP-1.md')
    art=delivery(ws,'deliverables/acme-report',extra=lambda d:(d/'CP-notes.md').mkdir())
    rc,out,err=run_store(ws,{'issues':[],'real':[{'id':'acme-001','name':'Acme','artifacts':[art]}]})
    print('rc',rc,'stdout empty' if not out.strip() else out[:200]); print('stderr tail:',err.strip().splitlines()[-1] if err.strip() else '')

def case3():
    print('== C: run folder named like a curated route key collides and overwrites the curated run')
    ws=Path(tempfile.mkdtemp(dir=sys.argv[1]))
    handoff(ws,'frontier-2020-001','CP-1.md'); handoff(ws,'frontier-2020','CP-2.md',GOOD.replace('CP-1','CP-2'))
    rc,out,err=run_store(ws,{'issues':[],'real':[{'id':'frontier-2020-001','name':'Frontier','artifacts':[]},{'id':'frontier-2020','name':'Frontier new','artifacts':[]}]})
    d=json.loads(out); print('rc',rc,'runs:',{k:(v['folder'],list(v['modules'])) for k,v in d['runs'].items()},'issues:',d['issues'])

def case4():
    print('== D: deliverable folder named like a curated report is relabelled TransDigm/Latest regardless of view.json')
    ws=Path(tempfile.mkdtemp(dir=sys.argv[1]))
    art=delivery(ws,'deliverables/tdg-fy2024-snapshot-7',issuer='Ford Otosan')
    rc,out,err=run_store(ws,{'issues':[],'real':[{'id':'delivery:x','name':'x','artifacts':[art]}]})
    d=json.loads(out); r=d['reports'][0]; print('rc',rc,'issuer:',r['issuer'],'label:',r['label'],'status:',r['status'])

def case5():
    print('== E: UTF-8 BOM handoff is shown unstructured')
    ws=Path(tempfile.mkdtemp(dir=sys.argv[1]))
    d=ws/'runs'/'acme-001'; d.mkdir(parents=True); (d/'CP-1.md').write_bytes(b'\xef\xbb\xbf'+GOOD.encode())
    rc,out,err=run_store(ws,{'issues':[],'real':[{'id':'acme-001','name':'Acme','artifacts':[]}]})
    print('rc',rc,json.loads(out)['issues'])

for c in (case1,case2,case3,case4,case5): c()

def case6():
    print('== F: a CP-*.md file not listed in the verified delivery.json is shown as "Built from"')
    ws=Path(tempfile.mkdtemp(dir=sys.argv[1]))
    handoff(ws,'acme-001','CP-1.md'); handoff(ws,'acme-001','CP-2.md',GOOD.replace('CP-1','CP-2'))
    art=delivery(ws,'deliverables/acme-report',extra=lambda d:(d/'CP-2.md').write_text(GOOD.replace('CP-1','CP-2')))
    listed=list(json.loads((ws/'deliverables/acme-report/delivery.json').read_text())['files'])
    rc,out,err=run_store(ws,{'issues':[],'real':[{'id':'acme-001','name':'Acme','artifacts':[art]}]})
    r=json.loads(out)['reports'][0]
    print('listed in delivery.json:',listed); print('builtFrom:',[(b['module'],b['source']) for b in r['builtFrom']])
case6()
