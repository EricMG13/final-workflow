"""A symlinked deliveries/<sub> directory lets store.py read handoffs outside the workspace."""
import json, os, subprocess, sys, tempfile
from pathlib import Path
REPO=Path('/workspace/final-workflow')
base=Path(tempfile.mkdtemp(dir=sys.argv[1]))
outside=base/'outside'; outside.mkdir(); (outside/'CP-9.md').write_text('# CP-9\n\n## Findings\n\nSECRET-OUTSIDE-WORKSPACE.\n')
(outside/'CP-8.md').symlink_to(outside/'CP-9.md')  # control: a file link is refused
ws=base/'ws'; run=ws/'runs'/'acme-001'; (run/'deliveries').mkdir(parents=True)
(run/'CP-1.md').write_text('# CP-1\n\n## Findings\n\nInside.\n')
os.symlink(outside, run/'deliveries'/'link')
cat={'issues':[],'real':[{'id':'acme-001','name':'Acme','artifacts':[]}]}
out=subprocess.run([str(REPO/'.venv/bin/python'),'-I','-B',str(REPO/'apps/issuer-library/engine/store.py'),str(ws)],input=json.dumps(cat).encode(),capture_output=True).stdout
d=json.loads(out)
print('outputs:',list(d['outputs']))
print('outside text leaked:', any('SECRET-OUTSIDE-WORKSPACE' in json.dumps(o['sections']) for o in d['outputs'].values()))
