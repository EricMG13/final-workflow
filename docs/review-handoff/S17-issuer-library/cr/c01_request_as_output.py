# Repro: request files are classified as module outputs by engine/store.py
import importlib.util, json, sys
from pathlib import Path
REPO = Path("/home/user/final-workflow")
spec = importlib.util.spec_from_file_location("store", REPO / "apps/issuer-library/engine/store.py")
store = importlib.util.module_from_spec(spec); spec.loader.exec_module(store)
cat = {"real": [{"id": "crc-liquidity-2020-001", "name": "CRC"}, {"id": "tdg-valuation-2025-001", "name": "TDG"}]}
s = store.workspace_store(REPO, cat)
for key, run in s["runs"].items():
    for m, info in run["modules"].items():
        print(key, m, "outputs=", [o.split("/",1)[1] for o in info["outputs"]], "default=", info["default"])
for oid in ["crc-liquidity-2020-001/CP-3C-request.md", "crc-liquidity-2020-001/CP-2D-repair-request.md", "tdg-valuation-2025-001/CP-2-request.md"]:
    r = s["outputs"].get(oid)
    print(oid, "->", r and (r["label"], r["scope"]))
