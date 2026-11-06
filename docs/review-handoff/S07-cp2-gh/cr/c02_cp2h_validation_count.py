"""Count how often one CP-2H submit parses the ratings source and composes the book (C02)."""
import sys, tempfile, time
from collections import Counter
from pathlib import Path
sys.path.insert(0, "tests")
import test_connect_cp2h as tc
from deploy_workflow.owners import cp2h

calls = Counter()
def wrap(name):
    orig = getattr(cp2h, name)
    def w(*a, **k):
        calls[name] += 1
        return orig(*a, **k)
    setattr(cp2h, name, w)
for n in ("validate", "compute", "register_source", "parse_ratings", "_compose",
          "_validate_step", "cp2h_upstream", "select_cp1"):
    wrap(n)

with tempfile.TemporaryDirectory() as d:
    store, pack, attempt = tc.seed(Path(d), "positive")
    payload = tc._submission(store, "positive").model_dump_json()
    calls.clear()
    t = time.perf_counter()
    sub = tc._submit(store, attempt, payload)
    el = time.perf_counter() - t
    print("attempt status:", sub.journal.status)
print(dict(calls), f"submit {el*1000:.0f} ms")
