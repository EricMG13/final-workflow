import sys, hashlib, re
from pathlib import Path
sys.path.insert(0,'apps/issuer-library/engine')
import store
root=Path('runs')
for run in sorted(p for p in root.iterdir() if p.is_dir()):
    cands=[*sorted(run.glob("CP-*.md")),*sorted(run.glob("deliveries/*/CP-*.md"))]
    kept=store.handoff_files(run)
    keptset=set(kept)
    by={}
    for p in cands:
        if p.is_file() and store.HANDOFF_NAME.match(p.name) and not store.OUTPUT_SKIP.search(p.name):
            by.setdefault(store.sha256(p),[]).append(p)
    for h,ps in by.items():
        mods={store.HANDOFF_NAME.match(p.name)[0] for p in ps}
        if len(mods)>1:
            print(run.name, [str(p.relative_to(run)) for p in ps], 'kept:', [str(p.relative_to(run)) for p in ps if p in keptset])
    # also label crash
    for p in kept:
        m=store.HANDOFF_NAME.match(p.name)[0]
        try: store.output_label(m,p,kept)
        except Exception as e: print('LABEL CRASH',run.name,p.name,repr(e))
