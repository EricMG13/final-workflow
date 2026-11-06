"""CP-3D accepts as executable bid/offer a quote that calls itself indicative and not firm,
which CP-3 refuses as an observed row (TALK_MARKERS)."""
import copy
import tests.test_method_cp3d as t
from deploy_workflow.owners import cp3d
from deploy_vii.cp3_relative_value import _found, _TALK

page = ("Indicative dealer quotation on January 9, 2026, subject to confirmation and not firm: "
        "bid 98.50 and offer 99.25.")
raw = copy.deepcopy(t.SUBMISSIONS["positive"])
for obs, level in ((raw["observations"][0], "98.50"), (raw["observations"][1], "99.25")):
    assert obs["kind"] in ("bid", "offer")
    obs.update(locator="page:9", quote=page, level_text=level)
ctx = t._with_page(t._context("positive"), "market", "page:9", page)
sub = t._submission(raw)
print("CP-3D issues:", cp3d.submission_issues(submission=sub, context=ctx))
res = cp3d.market_implied_result(submission=sub, context=ctx)
cells = {c.fact_id: c for tb in res.tables for r in tb.rows for c in r.facts}
for fid in ("T3E.1.r01.level", "T3E.1.r02.level"):
    print(fid, cells[fid].shown)
print("DM / PD mid:", [(k, c.shown) for k, c in cells.items() if k.endswith(".mid") and k.startswith(("T3E.3", "T3E.4"))][:6])
print("CP-3 talk markers in the same quote:", _found(_TALK, page))
