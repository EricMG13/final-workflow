"""CP-2G/CP-2H: with downside EBITDA at zero and debt positive, every leverage test is 'Not
calculable' instead of reached; the first-break claim then reports FCF/coverage only."""
import sys
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp2g as G
import test_method_cp2h as H
r = G._result("fixture_total_loss")
y = r.forecast["down"].years[0]
print("down FY1 EBITDA", y.ebitda.amount, "closing debt", y.closing_debt.amount, "total lev", y.total_leverage)
for br in r.break_tests:
    print(br.row, br.kind, br.down.first, br.down.reason)
print([c.text for c in r.claims if c.claim_id == "T2H.7.down"])
rep = H.report("fixture_total_loss")
for o in rep.outcomes: print("CP-2H", o.row, o.down.first)
print({k: v for k, v in rep.totals.items()})
