import copy, json, sys
sys.path.insert(0, "tests")
import test_financial_workflow as fw
from deploy_vii.financial_contracts import FinancialReview
from deploy_vii.canonical_kpis import canonical_kpis
from deploy_vii.financial_adapter import kernel_registers
from deploy_vii.model import history
from deploy_vii.model.statements import statement_frame

pack = fw.make_pack()
doc = fw.financials(pack)["financial"]
book = doc["books"][0]
q1 = next(a for a in book["accounts"] if a["period_id"] == "q1-2025")
book["addbacks"] = [{
    "addback_id": "restructuring", "addback_label": "Restructuring", "period_id": "q1-2025",
    "classification": "restructuring", "realization_status": "REALIZED", "display_priority": 1,
    "value": {**q1["value"], "observation_id": "addback-q1", "amount": "2"},
    "classification_citations": q1["value"]["citations"],
}]
doc.pop("limitations", None)
try:
    review = FinancialReview.model_validate_json(json.dumps({**doc, "pack_sha256": pack.content_hash()}))
except Exception as e:
    print("BUILD", e); raise
regs = kernel_registers(pack, review, "consolidated")
cols = history.historical_columns(regs)
acc = history.account_frame(regs, cols)
sf = statement_frame(acc, cols, regs, False)
print({c.column_id: (acc[c.column_id].get("addback:restructuring").reason, sf[c.column_id]["adjusted_ebitda"].value) for c in cols})
rep = canonical_kpis(pack, review, "consolidated")
for v in rep.values:
    if v.key == "adjusted_ebitda":
        print(v.basis_id, v.value.amount, v.value.calculation_status)
