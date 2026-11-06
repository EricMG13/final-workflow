# Repro: one unreadable CP-*.md beside one deliverable fails the whole workspace store.
import importlib.util, json, tempfile
from pathlib import Path
REPO = Path("/home/user/final-workflow")
spec = importlib.util.spec_from_file_location("store", REPO / "apps/issuer-library/engine/store.py")
store = importlib.util.module_from_spec(spec); spec.loader.exec_module(store)
ws = Path(tempfile.mkdtemp(dir=Path(__file__).parent))
arts = []
for name, bad in [("good", False), ("bad", True)]:
    d = ws / "deliverables" / name; d.mkdir(parents=True)
    (d / "delivery.json").write_text(json.dumps({"files": {"report.html": "ab", "view.json": "cd"}}))
    (d / "view.json").write_text(json.dumps({"run": {"issuer_name": "Acme", "as_of": "2024-12-31"}}))
    (d / "CP-1.md").write_text("# CP-1\n\ntext\n")
    if bad:
        (d / "CP-2.md").mkdir()   # stands in for any unreadable handoff (lock, permission, directory)
    arts.append({"folder": f"deliverables/{name}", "available": True, "label": name, "href": f"/files/deliverables/{name}/report.html?sha256=ab"})
cat = {"real": [{"id": "delivery:x", "artifacts": arts}]}
try:
    s = store.workspace_store(ws, cat)
    print("reports:", [r["id"] for r in s["reports"]], "issues:", s["issues"])
except Exception as e:
    print("workspace_store raised:", type(e).__name__, e)
