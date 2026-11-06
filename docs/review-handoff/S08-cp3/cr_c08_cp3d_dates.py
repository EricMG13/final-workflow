"""CP-3D: a pack (non-context) bid/offer dated long before, or after, the run as-of is accepted
without a stale limitation and drives the DM/PD figures; only context rows get the stale rule."""
import copy
import tests.test_method_cp3d as t
from deploy_workflow.owners import cp3d

base_ctx = t._context("positive")
print("run as_of:", base_ctx.run_as_of)
for when in ("January 9, 2019", "January 9, 2027"):
    page = f"Dealer quotation on {when}: bid 98.50 and offer 99.25."
    raw = copy.deepcopy(t.SUBMISSIONS["positive"])
    for obs, level in ((raw["observations"][0], "98.50"), (raw["observations"][1], "99.25")):
        obs.update(locator="page:9", quote=page, level_text=level, as_of_text=when)
    ctx = t._with_page(base_ctx, "market", "page:9", page)
    sub = t._submission(raw)
    issues = cp3d.submission_issues(submission=sub, context=ctx)
    print(when, "issues:", issues)
    if not issues:
        res = cp3d.market_implied_result(submission=sub, context=ctx)
        d = cp3d.compose(inputs=cp3d.inputs_from_submission(sub))
        print("   days to maturity:", d.days, "| stale/date limitation:",
              [l for l in res.own_limitations if "tale" in l or "as-of" in l or "after" in l])
