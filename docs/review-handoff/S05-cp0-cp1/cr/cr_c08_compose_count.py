"""CR-C08: one cp1c.compute(inputs) composes the module and parses the peer sheet twice; _checked
adds a third (calculation_issues before compute)."""
import sys
from collections import Counter
sys.path.insert(0, "tests")
import test_method_cp1c as m
from deploy_workflow.owners import cp1c
calls = Counter()
for name in ("_compose", "parse_peer_source"):
    orig = getattr(cp1c, name)
    def f(*a, _o=orig, _n=name, **k):
        calls[_n] += 1
        return _o(*a, **k)
    setattr(cp1c, name, f)
inp = m.inputs("positive")
calls.clear(); cp1c.compute(inp); print("compute:", dict(calls))
calls.clear(); cp1c.calculation_issues(inp); cp1c.compute(inp); print("_checked path (calculation_issues + compute):", dict(calls))
