"""Count python_checks passes per CP-5 compute and per owner view_body."""
import importlib
from deploy_vii import cp5_integrity
from deploy_workflow.owners import cp5
t = importlib.import_module("test_method_cp5")
calls = {"n": 0}
real = cp5_integrity.python_checks
def counted(scope):
    calls["n"] += 1
    return real(scope)
cp5_integrity.python_checks = counted
import deploy_vii.live.context as lc
cp5.python_checks = counted
case = t.CASES[0] if hasattr(t, "CASES") else "positive"
inputs = t.make_inputs(case)
calls["n"] = 0; r = cp5.compute(inputs); print("compute: python_checks calls =", calls["n"], "issues", r.issues[:1])
calls["n"] = 0; cp5.view_body(inputs.scope); print("view_body: python_checks calls =", calls["n"])
