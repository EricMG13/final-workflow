"""code-review repro: a USD-run CP-L10 Upstream accepts EUR CP-1 money operands and stamps the
derived change cells USD (the RunUpstream currency check is skipped for the default currency)."""
import sys
sys.path.insert(0, "tests")
import test_method_cpl10 as t
from deploy_workflow.owners import cpl10

facts = [f.model_copy(update={"currency": "EUR"}) if f.unit == "MILLIONS" else f for f in t._cp1_facts()]
up = t._upstream(facts)  # no UpstreamError raised
res = cpl10.change_screen(submission=t._payload("positive"), upstream=up)
cells = {c.fact.fact_id: c.fact for c in res.cells}
for fid in ("TL10.2.cash.change", "TL10.2.cash.from_value", "TL10.2.cash.to_value", "TL10.2.ebitda.change"):
    f = cells.get(fid)
    print(fid, None if f is None else (f.amount, f.unit, f.currency))
print([k for k in cells if k.startswith("TL10.2.cash.")])
