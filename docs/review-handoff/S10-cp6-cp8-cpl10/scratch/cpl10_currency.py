"""CP-L10: a plain (USD/no-context) Upstream never checks CP-1 operand currency."""
import json, sys
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cpl10 as t
from deploy_workflow.owners import cpl10

facts = t._cp1_facts()
# Case A: all money operands in EUR (issuer reports EUR; no run context -> plain Upstream)
eur = [f.model_copy(update={"currency": "EUR"}) if f.unit == "MILLIONS" else f for f in facts]
try:
    up = t._upstream(eur)
    print("A: Upstream accepted EUR operands; currency basis =", up.currency.currency)
    res = cpl10.change_screen(submission=t._payload("positive"), upstream=up)
    cells = {c.fact.fact_id: c.fact for c in res.cells}
    for fid in ("TL10.2.ebitda.from_value", "TL10.2.ebitda.to_value", "TL10.2.ebitda.change"):
        f = cells[fid]; print(" ", fid, f.amount, f.currency, f.unit)
    print("  claim:", next(c.text for c in res.claims if c.claim_id == "TL10.2.ebitda"))
except Exception as e:
    print("A refused:", type(e).__name__, e)

# Case B: mixed currency across quarters for one topic
mixed = []
for f in facts:
    if f.unit == "MILLIONS" and f.label.startswith("Q4 25") and f.row_id == "ebitda":
        f = f.model_copy(update={"currency": "EUR"})
    mixed.append(f)
try:
    up = t._upstream(mixed)
    sub = json.loads(t._payload("positive"))
    print("B: comparison", sub["comparison"])
    res = cpl10.change_screen(submission=json.dumps(sub), upstream=up)
    cells = {c.fact.fact_id: c.fact for c in res.cells}
    for fid in ("TL10.2.ebitda.from_value", "TL10.2.ebitda.to_value", "TL10.2.ebitda.change", "TL10.2.ebitda.materiality"):
        f = cells[fid]; print(" ", fid, f.amount if f.amount is not None else f.text, f.currency)
except Exception as e:
    print("B refused:", type(e).__name__, e)
