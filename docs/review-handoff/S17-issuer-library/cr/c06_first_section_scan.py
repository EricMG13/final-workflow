# Scan: outputs whose views.js installDestinations 'first' section id is not one of its listed sections.
import importlib.util, re
from pathlib import Path
REPO = Path("/home/user/final-workflow")
spec = importlib.util.spec_from_file_location("store", REPO / "apps/issuer-library/engine/store.py")
store = importlib.util.module_from_spec(spec); spec.loader.exec_module(store)
runs = sorted(p.name for p in (REPO / "runs").iterdir() if p.is_dir())
s = store.workspace_store(REPO, {"real": [{"id": r, "name": r} for r in runs]})
curated = {s["pins"].get(m) for m in ("CP-1", "CP-1A", "CP-2", "CP-8")}
bad = 0
for oid, out in s["outputs"].items():
    if oid in curated: continue
    ids = ["s%d" % sec["line"] for sec in out["sections"] if sec["blocks"] and not re.match(r"^(Request|Calculations|Next module)", sec["heading"])]
    if out.get("summary"):
        first = next((x for x in out["sections"] if x["heading"] == "Reader summary"), None)
    else:
        fh = out.get("firstHeading")
        first = fh and next((x for x in out["sections"] if x["heading"].startswith(fh)), None)
    if first and "s%d" % first["line"] not in ids:
        bad += 1
        print(oid, "first heading:", first["heading"][:60], "blocks:", len(first["blocks"]))
print("outputs with an unlisted first section:", bad)
