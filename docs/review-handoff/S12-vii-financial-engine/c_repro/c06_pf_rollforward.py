"""C: PF-LTM debt roll-forward does not foot after a total_debt adjustment."""
from decimal import Decimal as D
from deploy_vii.model.registers import Cp1Registers, PeriodRow, AccountRow, FacilityRow, PfAdjustmentRow
from deploy_vii.model.frame import SourceRef
from deploy_vii.model import history
from deploy_vii.model.statements import statement_frame, pro_forma_column

src = SourceRef("s1", "p1", "x")
fy24 = PeriodRow("FY24", "FY2024", None, "FY", "2024-01-01", "2024-12-31", 366, "USD", "MILLIONS", ())
fy25 = PeriodRow("FY25", "FY2025", None, "FY", "2025-01-01", "2025-12-31", 365, "USD", "MILLIONS", ())
def fac(pid, v):
    return FacilityRow("TL", "TL", pid, "TERM_LOAN", "USD", D(v), None, None, "SECURED", "SENIOR",
                       "NOT_LEASE", None, "x", "NOT_STATED", "NOT_STATED", None, None, None, None, src)
accts = (AccountRow("net_debt_issue_repay", "FY25", D(20), "VERIFIED", src),)
pf = (PfAdjustmentRow("pf1", "refi", "FY25", "REFINANCING", "total_debt", D(50), src),)
regs = Cp1Registers((fy24, fy25), accts, (), (), (), (fac("FY24", 100), fac("FY25", 125)), pf, "USD", "MILLIONS")
cols = history.historical_columns(regs)
fr = statement_frame(history.account_frame(regs, cols), cols, regs)
col = next(c for c in cols if c.period_id == "FY25")
k = col.column_id
print("LTM/FY25:", {x: fr[k][x].value for x in ("debt_opening", "debt_raised_net", "debt_non_cash", "debt_closing")})
pcol, pfr = pro_forma_column(regs, col, fr)
c = pfr[pcol.column_id]
vals = {x: (c[x].value, c[x].reason) for x in ("debt_opening", "debt_raised_net", "debt_non_cash", "debt_closing", "total_debt")}
print("PF:", vals)
o, n, cl = c["debt_opening"].value, c["debt_non_cash"].value, c["debt_closing"].value
print("opening + non_cash (+ raised, blank) =", o + n, "vs closing", cl)
