"""CP-4C content_issues raises (not an issue) on a CP-4 head with one capacity basket."""
import importlib
from dataclasses import replace
from deploy_workflow.owners import cp4c
t = importlib.import_module("test_method_cp4c")
inputs = t._inputs("positive")
print("baseline issues:", cp4c.content_issues(inputs))
cp4 = inputs.context.cp4
print("CP-4 rows read:", sorted({(f.table_id, f.row_id) for f in cp4.facts}))
# a CP-4 head whose model listed one basket only: T4.10 has r01 but no r02
one = cp4c.Cp4Head(status=cp4.status, facts=tuple(f for f in cp4.facts if not (f.table_id == "T4.10" and f.row_id == "r02")))
bad = replace(inputs, context=replace(inputs.context, cp4=one))
try:
    print("issues:", cp4c.content_issues(bad))
except Exception as e:
    print("content_issues RAISED", type(e).__name__, e)
# baskets in the other order: r02 is the restricted-payments basket, r01 the debt basket
swap = {"r01": "r02", "r02": "r01"}
sw = cp4c.Cp4Head(status=cp4.status, facts=tuple(
    f.model_copy(update={"row_id": swap[f.row_id], "fact_id": f.fact_id.replace(f".{f.row_id}.", f".{swap[f.row_id]}.")})
    if f.table_id == "T4.10" and f.row_id in swap else f for f in cp4.facts))
bad2 = replace(inputs, context=replace(inputs.context, cp4=sw))
try:
    print("swapped issues:", cp4c.content_issues(bad2))
    cp4c.compute(bad2)
    print("compute ok")
except Exception as e:
    print("swapped RAISED", type(e).__name__, str(e)[:160])
