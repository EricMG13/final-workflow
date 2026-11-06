"""C06: growth = delta / prior with a signed denominator inverts the sign for a negative prior."""
from decimal import Decimal
from test_earnings import fixture, BASES
from deploy_workflow.earnings import build_earnings_delta

m = fixture()
def set_amt(m, metric, pid, val):
    return m.model_copy(update={"facts": tuple(
        f.model_copy(update={"amount": Decimal(val)})
        if f.table_id == "T4.10" and f.field == BASES[pid] and f.row_id.endswith(metric) and f.amount is not None
        else f for f in m.facts)})
m = set_amt(m, "ebitda", "q3-2025", "-10")
m = set_amt(m, "ebitda", "q4-2025", "-5")
r = build_earnings_delta(m, "q3-2025", "q4-2025")
p = next(p for p in r.points if p.measure_id == "ebitda")
print("EBITDA prior", p.prior_value, "current", p.current_value, "delta", p.delta, "growth", p.growth, p.growth_status)
