"""CP-4: a basket's capacity amount written in words is accepted and rendered, though the quote
states no amount; the digit form is refused (bare figure)."""
import copy, json, sys
sys.path.insert(0, "tests")
import test_method_cp4 as t
from deploy_vii import cp4_legal
from deploy_workflow.owners import cp4

for permits in ("Additional debt up to five hundred million US dollars without lender consent, growing to the greater of that and one hundred percent of Covenant EBITDA",
                "Additional debt up to 500 million US dollars without lender consent"):
    pack, up = t.make_pack("positive"), t.make_upstream("positive")
    raw = copy.deepcopy(t.SUBMISSIONS["positive"]["legal_covenants"])
    raw["capacity"][1]["permits"] = permits
    sub = cp4_legal.CovenantInterpretationSubmission.model_validate_json(json.dumps(raw).replace(t.FIG, t.select_metric(pack, up)))
    res = cp4.compute(cp4.Cp4Inputs(pack=pack, submission=sub, upstream=up, inputs=t.make_inputs("positive", pack)))
    print("issues:", res.issues)
    if res.report:
        f = {x.fact_id: x for x in res.report.facts}
        print("T4.10.r02.permits =", f["T4.10.r02.permits"].text)
        print("quotes:", [c.quote for c in f["T4.10.r02.permits"].citations])
