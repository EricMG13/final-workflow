"""Time validate vs compute for the CP-2H positive oracle case."""
import sys, time
sys.path.insert(0, "tests")
import test_method_cp2h as t
from deploy_workflow.owners import cp2h
case = next(iter(t.EXPECTED["cases"]))
inp = t.inputs(case)
cp2h.compute(inp)
n = 5
s = time.perf_counter()
for _ in range(n): cp2h.validate(inp)
v = (time.perf_counter() - s) / n
s = time.perf_counter()
for _ in range(n): cp2h.compute(inp)
c = (time.perf_counter() - s) / n
print(f"case {case}: validate {v*1000:.1f} ms; compute (incl. validate) {c*1000:.1f} ms")
