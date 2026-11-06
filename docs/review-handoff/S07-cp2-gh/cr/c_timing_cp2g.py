"""Time content_issues vs compute for the CP-2G positive oracle case."""
import sys, time
sys.path.insert(0, "tests")
import test_method_cp2g as t
from deploy_workflow.owners import cp2g
inp = t._inputs("positive")
cp2g.compute(inp)
n = 5
s = time.perf_counter()
for _ in range(n): cp2g.content_issues(inp)
ci = (time.perf_counter() - s) / n
s = time.perf_counter()
for _ in range(n): cp2g.compute(inp)
co = (time.perf_counter() - s) / n
print(f"content_issues {ci*1000:.1f} ms; compute (incl. 1 content_issues) {co*1000:.1f} ms")
