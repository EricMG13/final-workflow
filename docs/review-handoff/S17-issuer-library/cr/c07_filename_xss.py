# Repro step 1: a handoff whose file name holds markup reaches the store as an output id with charts.
import importlib.util, json, shutil, tempfile
from pathlib import Path
REPO = Path("/home/user/final-workflow")
spec = importlib.util.spec_from_file_location("store", REPO / "apps/issuer-library/engine/store.py")
store = importlib.util.module_from_spec(spec); spec.loader.exec_module(store)
here = Path(__file__).parent
ws = here / "xss-ws"; shutil.rmtree(ws, ignore_errors=True)
run = ws / "runs" / "shared-run"; run.mkdir(parents=True)
name = 'CP-1"><img src=x onerror=alert(document.domain)>.md'   # legal on macOS/Linux, no slash needed
shutil.copyfile(REPO / "apps/issuer-library/designs/reader-fixture/CP-1.md", run / name)
s = store.workspace_store(ws, {"real": [{"id": "shared-run", "name": "Shared"}]})
oid = next(iter(s["outputs"]))
print("output id:", oid, "| charts:", len(s["outputs"][oid]["charts"]), "| default:", s["runs"]["shared-run"]["modules"]["CP-1"]["default"])
(here / "xss-store.json").write_text(json.dumps(s))
