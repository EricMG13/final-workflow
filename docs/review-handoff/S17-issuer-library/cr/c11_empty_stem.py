# Repro: one handoff whose name has a single character after the module code hides the whole run.
import importlib.util, shutil
from pathlib import Path
REPO = Path("/home/user/final-workflow")
spec = importlib.util.spec_from_file_location("store", REPO / "apps/issuer-library/engine/store.py")
store = importlib.util.module_from_spec(spec); spec.loader.exec_module(store)
ws = Path(__file__).parent / "stem-ws"; shutil.rmtree(ws, ignore_errors=True)
run = ws / "runs" / "case-001"; run.mkdir(parents=True)
(run / "CP-0.md").write_text("# CP-0\n\n## Findings\n\nReady.\n")
(run / "CP-2d.md").write_text("# CP-2D\n\n## Findings\n\nLiquidity.\n")   # lower-case suffix; also CP-1-.md
s = store.workspace_store(ws, {"real": [{"id": "case-001", "name": "Case"}]})
print("runs shown:", list(s["runs"]), "| issues:", s["issues"])
