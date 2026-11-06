"""CR-C07: count full readiness/narrative recomputations in one cp1_registers call."""
import importlib, sys, tempfile, time
from collections import Counter
from pathlib import Path
sys.path.insert(0, "tests")
from deploy_vii import cp1_workflow, canonical_tables, downstream_readiness
from deploy_vii.execution import Execution
fw = importlib.import_module("test_financial_workflow")
calls = Counter()
def wrap(mod, name, key):
    orig = getattr(mod, name)
    def f(*a, **k):
        calls[key] += 1
        return orig(*a, **k)
    setattr(mod, name, f)
wrap(cp1_workflow, "canonical_downstream_readiness", "cp1_workflow->canonical_downstream_readiness")
wrap(canonical_tables, "canonical_downstream_readiness", "canonical_tables->canonical_downstream_readiness")
with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
    root = Path(d) / "case"
    fw.quality_ready_case(root)
    store = Execution(root / "store")
    ticket = next(a for a in store.read().attempts if a.module_id == "CP-1" and a.status == "pending").ticket_id
    calls.clear()
    t = time.perf_counter(); cp1_workflow.cp1_registers(store, ticket); total = time.perf_counter() - t
    print("one cp1_registers call:", dict(calls), "%.2fs" % total)
