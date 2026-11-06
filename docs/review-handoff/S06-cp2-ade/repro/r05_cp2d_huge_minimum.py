"""CP-2D: a minimum_cash.amount that passes every validator issue but crashes composition,
driven through the real journal entry `cp2d.submit`."""
import json, sys, tempfile, traceback
from pathlib import Path
sys.path.insert(0, "tests")
import test_connect_cp2d as tc
from deploy_workflow.owners import cp2d
for raw in ['1e300', '"1E+300"', '"1E+40"']:
    store, attempt = tc.make_upstream(Path(tempfile.mkdtemp()))
    payload = tc._literal("positive").replace('"amount": "10"', f'"amount": {raw}')
    sub, shape = cp2d._parsed(payload)
    up = cp2d.cp2d_upstream(store=store, attempt=attempt)
    print(raw, "shape:", shape, "validator issues:",
          None if sub is None else cp2d.validate_liquidity_bridge(pack=store.pack(), submission=sub, upstream=up))
    try:
        res = cp2d.submit(store, attempt.ticket_id, cp2d.STEP_ID, payload, None)
        print("   submitted:", res.attempt.status if hasattr(res, "attempt") else res)
    except Exception as e:
        print("   submit raised:", type(e).__name__, str(e)[:100])
    a = next(x for x in store.read().attempts if x.ticket_id == attempt.ticket_id)
    print("   attempt after:", a.status, [s.status for s in a.steps])
    try:
        cp2d.submit(store, attempt.ticket_id, cp2d.STEP_ID, payload, None)
    except Exception as e:
        print("   resume raised:", type(e).__name__, str(e)[:100])
