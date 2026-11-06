import json, sys
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cpl10 as t
from deploy_workflow.owners import cpl10
facts = t._cp1_facts()
out = []
for f in facts:
    if f.label.startswith("Q4 25"):
        f = f.model_copy(update={"status": "missing", "amount": None, "limitation": "Not reported"})
    out.append(f)
up = t._upstream(out)
sub = json.loads(t._payload("positive"))
sub["assessments"] = []
sub["overall"] = {"rationale": "No topic can be screened for this pair.", "category": "Insufficient Information",
                  "confidence": "Insufficient Information", "limitation": "Closing quarter values are not reported."}
sub["gaps"] = []
print("issues:", cpl10.validate_screen(submission=json.dumps(sub), upstream=up))
res = cpl10.change_screen(submission=json.dumps(sub), upstream=up)
cells = {c.fact.fact_id: c.fact for c in res.cells}
f = cells["TL10.1.cp1.topics_supported"]
print("topics_supported:", repr(f.text), f.status, f.value_class)
from deploy_vii.report_view import fact_spelling
try:
    print("spelling:", fact_spelling(f, "G1"))
except Exception as e:
    print("spelling raised:", type(e).__name__, e)
from deploy_vii import execution
import inspect
print(inspect.signature(execution.candidate_issues))
from deploy_vii import report_view
try:
    report_view._cell(f, ())
    print("_cell ok")
except Exception as e:
    print("report_view._cell raised:", type(e).__name__, e)
# check the module also passes Module construction + prose_issues of candidate
from deploy_vii.prose import issues as pi
