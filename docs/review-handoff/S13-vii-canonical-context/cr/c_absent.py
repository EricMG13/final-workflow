"""absent_input_limitation downgrades a structural-blocker BLOCK whose terms all have amounts."""
from decimal import Decimal as D
from types import SimpleNamespace
from deploy_vii.financial_reconciliation import _check, ReconciliationTerm
from deploy_vii.canonical_audit import absent_input_limitation

period = SimpleNamespace(period_id="fy-2025", citations=())
def term(label, amount, oid):
    return ReconciliationTerm.model_construct(label=label, observation_id=oid, original_amount=D(amount),
        amount=D(amount), coefficient=1, reason=None, citations=(), normalization=None)
quarters = tuple(term(f"q{i}", a, f"obs-q{i}") for i, a in enumerate(("20", "25", "30", "35"), 1))
for blocker in ("Four dated discrete quarters do not span the reported FY", "Expense presentation is unknown"):
    check = _check(period, "FY_QUARTERS", "revenue", term("revenue FY", "150", "obs-fy"), quarters,
                   "sum(four discrete quarters)", blocker=blocker)
    print(check.status, "difference:", check.difference, "| sum of terms would be", sum(q.amount for q in quarters), "vs reported 150")
    print("  ->", absent_input_limitation(check, public=True, conflicting=frozenset()))
