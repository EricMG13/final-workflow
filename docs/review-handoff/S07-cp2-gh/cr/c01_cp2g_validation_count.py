"""Count how often one CP-2G submit runs content_issues / compute (efficiency finding C01)."""
import json, sys, tempfile, time
from collections import Counter
from pathlib import Path
sys.path.insert(0, "tests")
import test_connect_cp2g as tc
from deploy_workflow.owners import cp2g

calls = Counter()
def wrap(name):
    orig = getattr(cp2g, name)
    def w(*a, **k):
        calls[name] += 1
        return orig(*a, **k)
    setattr(cp2g, name, w)
for n in ("content_issues", "compute", "validate_forward", "forward_model", "_validate_step",
          "cp2g_upstream", "_basis_of"):
    wrap(n)

with tempfile.TemporaryDirectory() as d:
    store, pack, attempt = tc._case_seed(Path(d), "positive")
    calls.clear()
    t = time.perf_counter()
    sub = tc._submit(store, attempt, json.dumps(tc._payload("positive")))
    el = time.perf_counter() - t
    print("attempt status:", sub.journal.status if hasattr(sub, "journal") else sub)
print(dict(calls), f"submit {el*1000:.0f} ms")
