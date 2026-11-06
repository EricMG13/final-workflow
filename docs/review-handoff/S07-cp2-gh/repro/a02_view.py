"""CP-2H: the analyst's migration view is never checked against the computed trigger outcomes."""
import sys, json, copy
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp2h as T
from deploy_workflow.owners import cp2h
rep = T.report("positive")
for o in rep.outcomes:
    print(o.row, o.fy25_reached, o.base.first, o.down.first)
print("totals:", dict(rep.totals))
payload = copy.deepcopy(T.raw_payload("positive"))
print("views as submitted:", [(v["agency"], v["view"]) for v in payload["views"]])
for v in payload["views"]:
    v["view"] = "Upgrade potential"
inp = T.inputs("positive", payload)
print("issues with every view flipped to Upgrade potential:", cp2h.validate(inp))
rep2 = cp2h.compute(inp)
print([ (c.fact.fact_id, c.fact.text) for c in rep2.cells if c.fact.fact_id.startswith("T2R.7") and c.fact.field=="view"])
