"""Count how many times render_owner_slice runs _capture (each is a full receipt verify + render)."""
import sys, tempfile
from pathlib import Path
from types import SimpleNamespace as NS
from deploy_workflow import owner_rendering as r

calls = 0
tree = {"report.html": b"<html/>", r.RECEIPT_NAME: b"{}"}
cap = NS(tree=tree, wire="W")
def fake_capture(*a):
    global calls; calls += 1; return cap
r._capture = fake_capture
r.OwnerRenderReceipt = NS(from_wire=lambda b: "W")
base = Path(tempfile.mkdtemp(dir=sys.argv[1]))
(base / "store").mkdir()
r.render_owner_slice(base / "store", base / "receipt.json", None, base / "out")
print("_capture calls per render_owner_slice:", calls)
