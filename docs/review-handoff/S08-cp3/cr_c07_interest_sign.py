"""CP-3C: a positive CP-1 cash_interest is negated to negative interest paid; the base cover is
n.m. but the pro forma cover nets the step-up against it and prints a meaningful-looking multiple.
Also: a negative adjusted EBITDA gives a negative interest cover (not n.m.)."""
from dataclasses import replace
import tests.test_method_cp3c as t
from deploy_workflow.owners import cp3c

base = t._inputs("positive")
print("fixture cash_interest:", base.cp1.cash_interest.amount, "ebitda:", base.cp1.adjusted_ebitda.amount)
r0 = cp3c.compute(base).refinancing
print("fixture: paid", r0.cash_interest_paid, "added", r0.added_interest, "cover", r0.interest_cover, "pf cover", r0.pro_forma_interest_cover)
from decimal import Decimal
amt = Decimal("2.00")
inp = t._with_cp1(cash_interest=replace(base.cp1.cash_interest, amount=amt))
inp = t._with_step_up(inp, 1000)
r = cp3c.compute(inp).refinancing
print("positive cash_interest", amt, "+ step-up 1000bp: paid", r.cash_interest_paid, "added", r.added_interest,
      "pro forma", r.pro_forma_interest, "| cover", r.interest_cover, "| pf cover", r.pro_forma_interest_cover)
neg = t._with_cp1(adjusted_ebitda=replace(base.cp1.adjusted_ebitda, amount=-base.cp1.adjusted_ebitda.amount))
rn = cp3c.compute(neg).refinancing
print("negative EBITDA: interest cover", rn.interest_cover, "| payable/EBITDA", rn.payable_over_ebitda)
res = cp3c.compute(neg)
print("COST claim:", next(c for c in res.claims if c.claim_id == "CP-3C-COST-01").text[:300] if hasattr(res.claims[0], "claim_id") else None)
