import json, tempfile
from pathlib import Path
import test_connect_cp2d as tc, test_method_cp2d as tm
from deploy_workflow.owner_workflow import OwnerWorkflow
root = Path(tempfile.mkdtemp(dir="/tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S06-cp2-ade"))
store = tc.make_store(root, tc.cp1_module(tm._operands("positive")))
wf = OwnerWorkflow(store, ("CP-2D",), None)
wf.read_inputs()
payload = tc._literal("positive")
print("submit:", wf.submit_review(payload)["status"])
sub = json.loads(payload)
head = next(h for h in store.read().heads if h.module_id == "CP-2D")
module = store.head_module(head)
blob = module.model_dump_json()
for a in sub["assessments"]:
    for k in ("text", "credit_implication", "limitation"):
        v = a.get(k)
        if v:
            print(a["section"], k, "present in module:", v[:50] in blob)
mc = sub.get("minimum_cash") or {}
if mc.get("rationale"): print("minimum_cash.rationale present:", mc["rationale"][:50] in blob)
mca = sub.get("minimum_cash_absence") or {}
for k in ("reason","follow_up"):
    if mca.get(k): print("minimum_cash_absence."+k, "present:", mca[k][:50] in blob)
for t in module.tables:
    if t.table_id == "T2E.6":
        print("T2E.6 rows:", [r.label for r in t.rows])
