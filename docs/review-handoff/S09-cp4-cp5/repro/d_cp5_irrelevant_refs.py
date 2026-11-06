"""CP-5: a `supported` verdict passes with upstream_refs that name any fact of the producer head,
even one unrelated to the claim (not cited, not named by the claim)."""
import json, sys
sys.path.insert(0, "tests")
import test_method_cp5 as t
from deploy_workflow.owners import cp5
from deploy_vii.cp5_integrity import IntegritySubmission, python_checks

case = t.CASES[0]
inputs = t.make_inputs(case)
sub = json.loads(inputs.submission.model_dump_json())
heads = {h.module_id: h for h in inputs.scope.evaluated}
marks = python_checks(inputs.scope).ref_marks
for r in sub["claim_reviews"]:
    if r["support"] == "supported":
        head = heads[r["producer_module"]]
        claim = next(c for c in head.claims if c.claim_id == r["claim_ref"])
        flagged = marks.get(head.module_id, frozenset())
        unrelated = next(f.fact_id for f in head.facts
                         if f.fact_id not in r["upstream_refs"] and f.fact_id not in claim.text
                         and f.fact_id not in flagged and f.text is not None)
        print("claim:", head.module_id, claim.claim_id, "|", claim.text[:120])
        print("orig refs:", r["upstream_refs"], "-> replaced by:", [unrelated])
        r["upstream_refs"] = [unrelated]
        break
res = cp5.compute(cp5.CP5Inputs(scope=inputs.scope, submission=IntegritySubmission.model_validate_json(json.dumps(sub))))
print("issues:", res.issues)
print("report status:", res.report.status if res.report else None)
