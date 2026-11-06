from types import SimpleNamespace as NS
import deploy_vii.live.context as ctx
from deploy_vii import cp3_relative_value as cp3
counts = {"pack": 0, "cp3_upstream": 0}
src = [NS(source_id="S1", status="ready"), NS(source_id="S2", status="ready")]
class FakeStore:
    def pack(self):
        counts["pack"] += 1; return NS(sources=src)
def fake_upstream(store, attempt):
    counts["cp3_upstream"] += 1; return NS(market_sources={"S1"})
cp3.cp3_upstream = fake_upstream
cp3.context_block = lambda pack, up: {}
store, step = FakeStore(), cp3.STEP_ID
ctx.module_context(store, None, step)
ids = [s.source_id for s in src]
ctx.declared_sources(store, None, step, ids)
ctx.readable_sources(store, None, step)
print("one CP-3 dispatch (module_context + declared_sources + readable_sources):", counts)
