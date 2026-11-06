import sys
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp2g as G
r = G._result("fixture_debt_repaid")
for case in ("base", "down"):
    for t, y in enumerate(r.forecast[case].years):
        print(case, t, "debt", y.closing_debt.amount, "interest", y.interest.amount, "cov", y.coverage.amount, y.coverage.reason)
for br in r.break_tests:
    print(br.row, br.kind, br.base.first, br.base.reason, "|", br.down.first)
