"""CP-2D minimum_cash.amount: hostile Decimal forms through the real step parser and validator."""
import json, sys, time
sys.path.insert(0, "tests")
import test_connect_cp2d as tc
from deploy_workflow.owners import cp2d
base = json.loads(tc._literal("positive"))
for raw in ['"NaN"', '"Infinity"', '1e400', '"1E+400"', '"-0"', '0.0000000000000000000000000000001']:
    payload = json.dumps(base).replace('"amount": "10"', f'"amount": {raw}')
    sub, issues = cp2d._parsed(payload)
    if sub is None:
        print(raw, "-> parse issues:", issues[:2]); continue
    t = time.time()
    try:
        si = cp2d.submission_issues(submission=sub, offered_refs=frozenset({r for a in sub.assessments for r in a.basis_refs} | set(sub.minimum_cash.basis_refs if sub.minimum_cash else ())), maturity_date_refs=frozenset({"cp1:T4.18_maturity_date"}))
        print(raw, "-> amount", repr(sub.minimum_cash.amount), "issues", si)
        b = cp2d.compose_bridge(operands=__import__("test_method_cp2d")._operands("positive"), horizon_months=24, minimum_cash=sub.minimum_cash.amount, balance_date=__import__("datetime").date(2025,12,31))
        txt = cp2d.amount_text(b.minimum_cash)
        print("   amount_text len", len(txt), txt[:40], "runway", b.runway_state, b.months_to_minimum_cash, f"{time.time()-t:.2f}s")
    except Exception as e:
        print(raw, "-> EXC", type(e).__name__, str(e)[:120])
