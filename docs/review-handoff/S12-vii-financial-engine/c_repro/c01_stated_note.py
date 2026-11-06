"""C: _stated() wipes the notes calc() put on gross profit / EBIT / EBITDA."""
from decimal import Decimal as D
from deploy_vii.model.registers import Cp1Registers, PeriodRow, AccountRow
from deploy_vii.model.frame import SourceRef
from deploy_vii.model import history
from deploy_vii.model.statements import statement_frame

src = SourceRef("s1", "p1", "x")
fy = PeriodRow("FY25", "FY2025", None, "FY", "2025-01-01", "2025-12-31", 365, "USD", "MILLIONS", ())
def a(m, v):
    return AccountRow(m, "FY25", None if v is None else D(v), "VERIFIED", src)
accts = (a("revenue", "100"), a("cogs", "60"), a("gross_profit", "40"),
         a("opex_including_da", "-20"), a("depreciation_amortization", "-5"))
regs = Cp1Registers((fy,), accts, (), (), (), (), (), "USD", "MILLIONS")
cols = history.historical_columns(regs)
acc = history.account_frame(regs, cols)
fr = statement_frame(acc, cols, regs)
c = cols[0].column_id
print("cogs cell note:", acc[c]["acct:cogs"].note, acc[c]["acct:cogs"].value)
for k in ("gross_profit", "ebit", "ebitda", "opex_ex_da"):
    print(k, fr[c][k].value, "note=", fr[c][k].note)

# missing-figure reason note
accts2 = (a("revenue", None), a("cogs", "-60"))
regs2 = Cp1Registers((fy,), accts2, (), (), (), (), (), "USD", "MILLIONS")
acc2 = history.account_frame(regs2, cols)
fr2 = statement_frame(acc2, cols, regs2)
print("revenue:", acc2[c]["acct:revenue"])
print("gross_profit missing:", fr2[c]["gross_profit"].reason, fr2[c]["gross_profit"].note)

# UNSPANNED: FY names a single quarter as its components
q1 = PeriodRow("Q1", "FY2025", "1", "QUARTER", "2025-01-01", "2025-03-31", 90, "USD", "MILLIONS", ())
fy3 = PeriodRow("FY25", "FY2025", None, "FY", "2025-01-01", "2025-12-31", 365, "USD", "MILLIONS", ("Q1",))
def b(m, p, v):
    return AccountRow(m, p, D(v), "VERIFIED", src)
regs3 = Cp1Registers((q1, fy3), (b("revenue", "Q1", "10"), b("cogs", "Q1", "-6")), (), (), (), (), (), "USD", "MILLIONS")
cols3 = history.historical_columns(regs3)
acc3 = history.account_frame(regs3, cols3)
fr3 = statement_frame(acc3, cols3, regs3)
for col in cols3:
    r = acc3[col.column_id]["acct:revenue"]
    g = fr3[col.column_id]["gross_profit"]
    print(col.column_id, "revenue", r.reason, repr(r.note), "| gross_profit", g.reason, repr(g.note), "| opex_ex_da", fr3[col.column_id]["opex_ex_da"].note)
