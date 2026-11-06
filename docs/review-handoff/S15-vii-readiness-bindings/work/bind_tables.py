import subprocess, re
from deploy_vii.bindings.shipped import SHIPPED_MAPS
for m in SHIPPED_MAPS:
    for e in m.entries:
        t = e.fact_coord.table_id
        if t is None: print("WILDCARD table", m.module_id, e); continue
        # search literal in src excluding bindings dir
        r = subprocess.run(["grep","-rlF","--include=*.py",f'"{t}"',"src/deploy_workflow","src/deploy_vii"],capture_output=True,text=True)
        files=[f for f in r.stdout.split() if "/bindings/" not in f]
        if not files:
            print("NOLITERAL", m.module_id, t, e.block_id)
