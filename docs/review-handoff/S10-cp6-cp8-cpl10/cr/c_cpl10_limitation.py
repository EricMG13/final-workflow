"""code-review repro: CP-L10 overall.limitation and gap text skip the figure/prohibited checks."""
import sys
sys.path.insert(0, "tests")
import test_method_cpl10 as t
from deploy_workflow.owners import cpl10

sub = t._with(("overall", "category"), cpl10.INSUFFICIENT)
sub["overall"]["confidence"] = cpl10.INSUFFICIENT
sub["overall"]["limitation"] = "We recommend a covenant reset at 5.2x; recovery is 40% at most."
print("limitation issues:", t._issues(sub))
res = cpl10.change_screen(submission=t.json.dumps(sub), upstream=t.UPSTREAM)
print([ (c.claim_id, c.limitation) for c in res.claims if c.claim_id == "TL10.3.overall"])
# control: the same words in overall.rationale are refused
ctl = t._with(("overall", "rationale"), "We recommend a covenant reset at 5.2x.")
print("rationale issues:", t._issues(ctl))
# gap text: no prohibited check
sub2 = t.deepcopy(t.SUBMISSIONS["positive"])
print("gaps:", sub2.get("gaps"))
if sub2.get("gaps"):
    sub2["gaps"][0]["gap"] = "Recovery prospects support a recommend-hold under the covenant"
    print("gap issues:", t._issues(sub2))
    res2 = cpl10.change_screen(submission=t.json.dumps(sub2), upstream=t.UPSTREAM)
    print([l for l in res2.limitations if "Gap" in l])
