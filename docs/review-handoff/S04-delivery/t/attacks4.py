"""Model display of sub-unit source amounts (decimals=0 hard-coded)."""
import hashlib, json, re
from pathlib import Path
from deploy_vii.contracts import View
from deploy_vii.report_view import ReportView
from deploy_workflow.handoff_delivery import delivery_files

ROOT = Path("/workspace/final-workflow")
SOURCE = ROOT / "runs/cpos-sol-medium-20261105"
OUT = Path("/tmp/claude-0/-workspace-final-workflow/10d71552-cdca-5952-86dc-d4ef0b76ab9e/scratchpad/review/S04-delivery/t/a4")
OUT.mkdir(exist_ok=True)
data = json.loads(next(SOURCE.glob("delivery-*.json")).read_bytes())
for group in (data["handoffs"], data["model"]["extra_handoffs"]):
    for item in group.values():
        item["path"] = str((SOURCE / item["path"]).resolve())
if data["model"]["forecast_exact"]:
    data["model"]["forecast_exact"]["path"] = str((SOURCE / data["model"]["forecast_exact"]["path"]).resolve())
cp1 = Path(data["handoffs"]["CP-1"]["path"]).read_text()
old = "| Cash paid during period for income taxes, net of refunds | 539 | 260 | 220 |"
assert old in cp1
cp1 = cp1.replace(old, "| Cash paid during period for income taxes, net of refunds | 0.4 | (0.3) | 220.5 |")
(OUT / "CP-1.md").write_text(cp1)
data["handoffs"]["CP-1"] = {"path": str(OUT / "CP-1.md"), "sha256": hashlib.sha256(cp1.encode()).hexdigest()}
data.pop("layout", None)
(OUT / "delivery.json").write_text(json.dumps(data))
files = delivery_files(OUT / "delivery.json")
calc = json.loads(files["calculation.json"])["values"]
print("calculation.json tax_cash:", {p: calc[p]["tax_cash"]["amount"] for p in calc})
mrv = ReportView.model_validate_json(files["model-report-view.json"])
for b in mrv.blocks:
    for r in b.rows:
        if r.row_id == "tax_cash" or "Tax Cash" in r.label:
            print("HTML Model row", r.label, [c.text for c in r.cells])
