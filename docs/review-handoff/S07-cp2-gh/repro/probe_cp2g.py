import sys, json, dataclasses
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp2g as T
from deploy_workflow.owners import cp2g
inp = T._inputs("positive")
ctx = inp.context
print("cp2a base_period:", ctx.cp2a.base_period, "| basis ltm:", ctx.basis.ltm_period)
for b in ctx.cp2a.breaks:
    print(b.row, b.origin, repr(b.test), b.level.amount, b.level.unit, b.required_decline.status, b.required_decline.amount, b.required_decline.formula)
print("submitted break metrics:", [(m.break_id, m.metric) for m in inp.submission.break_metrics])
print("scenarios:", [(s.row, s.name, s.decline.amount, s.increase.amount) for s in ctx.cp2a.scenarios])
print("downside:", inp.submission.downside.scenario)
ops = cp2g.Operands.from_cp1(ctx.cp1_facts, ctx.basis)
print({k: v.amount for k, v in ops.items()})
r = cp2g.compute(inp)
for br in r.break_tests:
    print(br.row, br.kind, br.test, br.base.first, br.down.first)
