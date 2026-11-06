"""CP-2G: analyst limitation texts are checked only for blankness: a bare invented figure, a
probability-weighted conclusion or a rating call passes and is stored as Claim.limitation."""
import sys, json
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp2g as T
from deploy_workflow.owners import cp2g
payload = T._bind_all(T._payload("positive"))
bad = "Management guided FY2026 EBITDA of 41.7 million; the probability-weighted expected value implies the issuer will be downgraded."
payload["base_drivers"]["revenue_growth"]["limitation"] = bad
payload["downside"]["limitation"] = bad
payload["assessment"]["limitation"] = bad
sub = cp2g.ForwardSubmission.model_validate_json(json.dumps(payload))
inp = cp2g.ForwardInputs(T._context("positive"), sub)
print("issues:", cp2g.content_issues(inp))
r = cp2g.compute(inp)
print([ (c.claim_id, c.limitation) for c in r.claims if c.limitation == bad])
# the same text as a rationale is refused
payload["base_drivers"]["revenue_growth"]["limitation"] = None
payload["downside"]["rationale"] = bad
sub = cp2g.ForwardSubmission.model_validate_json(json.dumps(payload))
print("as rationale:", cp2g.content_issues(cp2g.ForwardInputs(T._context("positive"), sub))[:4])
