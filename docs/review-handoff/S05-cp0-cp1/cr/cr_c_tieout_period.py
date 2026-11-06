"""CR: cp1c._tie_out compares the peer sheet's issuer line with CP-1's LTM ratio without checking
that the issuer line's period end is CP-1's period end; the difference is stamped with CP-1's period
and the result reads Reconciled/Differs."""
import sys
from dataclasses import replace
sys.path.insert(0, "tests")
import test_method_cp1c as m
from deploy_workflow.owners import cp1c
inp = m.inputs("positive")
orig = cp1c.parse_peer_source
def shifted(*a, **k):
    sheet = orig(*a, **k)
    return replace(sheet, issuer=replace(sheet.issuer, period_end="2023-06-30"))
cp1c.parse_peer_source = shifted
res = cp1c.compute(inp)
for f in res.facts:
    r = f.fact
    if r.fact_id.startswith("T1C.6.") or r.fact_id.startswith("T1C.2.issuer.revenue"):
        print(r.fact_id, "| amount:", r.amount, "| text:", r.text, "| period:", r.period, "| status:", r.status)
print("limitation mentions period mismatch:", [l for l in res.limitations if "2023" in l or "period" in l.lower()])
