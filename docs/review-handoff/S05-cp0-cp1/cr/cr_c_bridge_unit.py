"""CR: cp1d.parse_bridge only checks that a line STARTS WITH the period basis line; the bridge's
currency and unit clause is never read, yet every bridge amount is stamped MILLIONS in the run
currency. Compare cp1c._basis, which requires the (currency, 'amounts in millions') clause."""
import copy, json, sys
sys.path.insert(0, "tests")
import test_method_cp1d as t
from deploy_workflow.owners import cp1d
from deploy_workflow.owners.period_basis import DEFAULT_BASIS

print("required basis prefix:", repr(DEFAULT_BASIS.bridge_basis_line))
orig = t.MANIFEST["synthetic_source"]["positive"]["pages"]
page1 = orig[0]["text"]
basis = next(l for l in page1.split("\n") if l.startswith("Basis:"))
print("genuine basis line:   ", repr(basis))
forged = basis.replace("USD; amounts in millions", "EUR; amounts in thousands")
print("forged basis line:    ", repr(forged))
b0 = cp1d.parse_bridge([page1], DEFAULT_BASIS.bridge_basis_line)
b1 = cp1d.parse_bridge([page1.replace(basis, forged)], DEFAULT_BASIS.bridge_basis_line)
print("genuine parse items:", [(i.label, str(i.amount)) for i in b0.items][:3])
print("forged  parse items:", None if b1 is None else [(i.label, str(i.amount)) for i in b1.items][:3])
# full compute with the forged page (positive case submission)
t.MANIFEST["synthetic_source"]["positive"]["pages"] = [dict(orig[0], text=page1.replace(basis, forged)), *orig[1:]]
try:
    res = cp1d.compute(t._case_inputs("positive"))
    src = [f.record() for f in res.facts if f.record().get("derivation") == "source" or "Bridge source" in str(f.record().get("formula"))][:2]
    for r in src:
        print("fact:", {k: r[k] for k in ("fact_id", "amount", "amount_exact", "value", "unit", "currency", "status") if k in r})
    adj = [f.record() for f in res.facts if "T1D.2" in f.record()["fact_id"] or "T1D.3" in f.record()["fact_id"]][:3]
    for r in adj: print("derived:", {k: r[k] for k in ("fact_id","amount_exact","value","unit","currency","status") if k in r})
    print("limitations mention EUR/thousands:", any("EUR" in l or "thousand" in l for l in res.limitations))
except Exception as e:
    print("compute refused:", type(e).__name__, str(e)[:300])
