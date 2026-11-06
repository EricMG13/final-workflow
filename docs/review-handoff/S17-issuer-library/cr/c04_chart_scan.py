# Scan: chart cells that views.js chartNumber() maps to 'Not available' although they hold digits.
import importlib.util, json, re
from pathlib import Path
REPO = Path("/home/user/final-workflow")
spec = importlib.util.spec_from_file_location("store", REPO / "apps/issuer-library/engine/store.py")
store = importlib.util.module_from_spec(spec); spec.loader.exec_module(store)
RX = re.compile(r"^(?:[-+]?\d+(?:\.\d+)?|\(\d+(?:\.\d+)?\))(?:%|x)?$")   # views.js chartNumber
def num(v):
    c = str(v).replace("**", "").replace("`", "").strip().replace(",", "")
    return None if not RX.match(c) else c
runs = sorted(p.name for p in (REPO / "runs").iterdir() if p.is_dir())
cat = {"real": [{"id": r, "name": r} for r in runs]}
s = store.workspace_store(REPO, cat)
for oid, rec in s["outputs"].items():
    tables = {b["line"]: b for sec in rec["sections"] for b in sec["blocks"] if b["type"] == "table"}
    specs = []
    v = rec.get("visual")
    if v and v.get("kind") in ("paired", "peers", "bars"):
        specs.append(("visual", v["table"], v.get("columns") or [v.get("column")], v.get("rows")))
    for c in rec.get("charts") or []:
        specs.append(("reader", c["table"], c["columns"], None))
    for kind, line, cols, rows in specs:
        t = tables[line]
        rws = [t["rows"][i] for i in rows] if rows else t["rows"]
        for r in rws:
            for ci in cols:
                if ci is None or ci >= len(r["cells"]): continue
                val = r["cells"][ci]
                if num(val) is None:
                    print(f"{oid} [{kind}] line {r['line']} col {ci}: {val[:90]!r}")
