"""CP-2D: a CP-1 without a T4.18 schedule (or a zero-debt issuer with an empty one) can never
pass validation, because the maturity_wall assessment must cite a T4.18 maturity_date."""
import json, sys, tempfile
from dataclasses import replace
from decimal import Decimal
from pathlib import Path
sys.path.insert(0, "tests")
import test_connect_cp2d as tc
import test_method_cp2d as tm
from deploy_workflow.owners import cp2d

def run(label, operands):
    root = Path(tempfile.mkdtemp())
    cp1 = tc.cp1_module(operands)
    store = tc.make_store(root, cp1)
    attempt = store.begin("CP-2D")
    up = cp2d.cp2d_upstream(store=store, attempt=attempt)
    sel = cp2d.select_cp1(up.cp1)
    payload = json.loads(tc._literal("positive"))
    # Best-effort analyst: Insufficient Information on the wall, citing nothing it cannot cite.
    for a in payload["assessments"]:
        if a["section"] == "maturity_wall":
            a["basis_refs"] = [r for r in a["basis_refs"] if r in {o.fact.fact_id for o in sel.offered}]
            a["category"] = "Insufficient Information"
            a["limitation"] = "No facility schedule is disclosed."
    sub = cp2d.LiquidityBridgeSubmission.model_validate_json(json.dumps(payload))
    issues = cp2d.validate_liquidity_bridge(pack=store.pack(), submission=sub, upstream=up)
    print(label, "facilities=", sel.operands.facilities, "maturity_refs=", set(sel.maturity_date_refs))
    print("  issues:", issues)

base = tm._base_operands()
run("baseline(with loan)", base)
run("no T4.18 schedule", replace(base, facilities=None))
run("zero debt, empty schedule", tm._ro(base, facilities=(), total_debt_bs=Decimal(0), total_debt=Decimal(0)))
