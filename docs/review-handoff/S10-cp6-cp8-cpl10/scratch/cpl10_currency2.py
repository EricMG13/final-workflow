import sys
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cpl10 as t
from deploy_workflow.owners import cpl10
from deploy_vii import prose
facts = t._cp1_facts()
eur = [f.model_copy(update={"currency": "EUR"}) if f.unit == "MILLIONS" else f for f in facts]
up = t._upstream(eur)
res = cpl10.change_screen(submission=t._payload("positive"), upstream=up)
bound = prose.bind(c.fact for c in res.cells)
for c in res.claims:
    if c.claim_id in ("TL10.2.ebitda", "TL10.2.cash"):
        print(c.claim_id, "issues:", prose.issues(c.text, bound))
# full module path
from deploy_vii.contracts import Run
import inspect
print(inspect.signature(cpl10.screen_report))
