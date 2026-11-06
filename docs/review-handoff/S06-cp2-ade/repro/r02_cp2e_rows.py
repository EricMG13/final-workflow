"""CP-2E row reading: a row whose FY cell is absent, a parenthesised interest outflow, a page
in thousands. Expected values derived by hand from the page text."""
import copy, json, sys
from decimal import Decimal
sys.path.insert(0, "tests")
import test_method_cp2e as tm
from deploy_workflow.owners import cp2e

case = "positive"
pages = dict(tm._pages(case))
sub = copy.deepcopy(tm.SUBMISSIONS[case])
print("baseline issues:", cp2e.validate_macro_fx(submission=sub, pages=pages))
td = sub["earnings"]["total_debt"]; print("total_debt ref:", td["locator"], repr(td["quote"]), td["value_text"])
it = sub["earnings"]["interest"]; print("interest ref:", it["locator"], repr(it["quote"]), it["value_text"])

# (a) FY cell absent on the page: the row has one value fewer than the header.
loc = td["locator"]; page = pages[loc]
line = next(l for l in page.split("\n") if l.strip() == td["quote"].strip())
toks = line.split("  ")
short = "  ".join(toks[:-1])   # drop the FY 2025 value
prior = short.split()[-1]
pages_a = dict(pages); pages_a[loc] = page.replace(line, short)
sub_a = copy.deepcopy(sub); sub_a["earnings"]["total_debt"]["quote"] = short
sub_a["earnings"]["total_debt"]["value_text"] = prior
hdr = next(l for l in page.split("\n") if l.startswith("Period"))
print("\n(a) header:", repr(hdr)); print("    row   :", repr(short), "-> value_text", prior)
print("    issues:", cp2e.validate_macro_fx(submission=sub_a, pages=pages_a))
i_a = cp2e.inputs_from_submission(sub_a, source_names=tm._names(case))
print("    total_debt read as FY value:", i_a.total_debt.value)

# (b) Interest outflow printed in accounting parentheses.
loc = it["locator"]; page = pages[loc]
line = next(l for l in page.split("\n") if l.strip() == it["quote"].strip())
parts = line.split("  "); neg = "  ".join(p if i == 0 else f"({p})" for i, p in enumerate(parts))
pages_b = dict(pages); pages_b[loc] = page.replace(line, neg)
sub_b = copy.deepcopy(sub); sub_b["earnings"]["interest"]["quote"] = neg
sub_b["earnings"]["interest"]["value_text"] = neg.split()[-1]
print("\n(b) row:", repr(neg))
print("    issues:", cp2e.validate_macro_fx(submission=sub_b, pages=pages_b))
i_b = cp2e.inputs_from_submission(sub_b, source_names=tm._names(case))
s = cp2e.derive_sensitivity(operands=cp2e.operands_of(i_b), rate_shocks_bp=i_b.rate_shocks_bp,
                            fx_shocks=i_b.fx_shocks, hedge_ratio=i_b.hedge_ratio)
print("    interest operand:", i_b.interest.value, " cov_base:", s.cov_base)
for r in s.rate:
    print("    shock", r.shock_bp.amount, "gross", r.gross, "interest_after", r.interest_after, "cov_after", r.cov_after)

# (c) Units: the page says thousands; nothing reads it.
pages_c = {k: v.replace("amounts in millions", "amounts in thousands").replace("USD millions", "USD thousands") for k, v in pages.items()}
print("\n(c) thousands page issues:", cp2e.validate_macro_fx(submission=sub, pages=pages_c))

print("\n--- (a2) flow row with FY cell absent: Levered free cash flow")
fc = sub["earnings"]["fcf"]; loc = fc["locator"]; page = pages[loc]
line = next(l for l in page.split("\n") if l.strip() == fc["quote"].strip())
short = "  ".join(line.split("  ")[:-1]); prior = short.split()[-1]
pages_a2 = dict(pages); pages_a2[loc] = page.replace(line, short)
sub_a2 = copy.deepcopy(sub); sub_a2["earnings"]["fcf"]["quote"] = short; sub_a2["earnings"]["fcf"]["value_text"] = prior
print("    header:", repr(next(l for l in page.split("\n") if l.startswith("Period"))))
print("    row   :", repr(short), "(FY 2025 cell absent; last value is Q4 2025)")
print("    issues:", cp2e.validate_macro_fx(submission=sub_a2, pages=pages_a2))
i2 = cp2e.inputs_from_submission(sub_a2, source_names=tm._names(case))
res = cp2e.compute(i2)
for t in res.tables:
    for r in t.rows:
        if "free cash flow" in r.label.lower():
            print("   ", t.table_id, r.label, [(c.shown, c.period) for c in r.cells][:3])

print("\n--- (c2) page states thousands; quotes follow the page")
def thou(s): return s.replace("amounts in millions", "amounts in thousands").replace("USD millions", "USD thousands")
pages_c = {k: thou(v) for k, v in pages.items()}
sub_c = json.loads(thou(json.dumps(sub)))
print("    currency quote:", repr(sub_c["reporting_currency"]["quote"]))
print("    issues:", cp2e.validate_macro_fx(submission=sub_c, pages=pages_c))
ic = cp2e.inputs_from_submission(sub_c, source_names=tm._names(case))
rc = cp2e.compute(ic)
for t in rc.tables:
    for r in t.rows:
        if r.label.lower().startswith("total debt"):
            print("   ", t.table_id, r.label, [(c.shown, c.unit, c.scale if hasattr(c,'scale') else None) for c in r.cells][:2])
