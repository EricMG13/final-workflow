"""C03/C07: four contiguous trailing quarters spanning two fiscal years, and a EUR book."""
from test_financial_series import fixture, change
from deploy_workflow.financial_series import cp1_chart_series
base = fixture()
q = sorted({f.row_id for f in base.facts if f.table_id == "T4.14"})
ends = {f.row_id: f.text for f in base.facts if f.table_id == "T4.14" and f.field == "end_date"}
order = sorted(q, key=lambda r: ends[r])
# Relabel as a fiscal year ending 31 March: Q1-Q3 2025 are Q2..Q4 of FY2025's predecessor? use FY ending Mar:
# Jan-Mar 2025 = Q4 FY2025; Apr-Jun 2025 = Q1 FY2026; Jul-Sep = Q2 FY2026; Oct-Dec = Q3 FY2026
labels = [("2025", "4"), ("2026", "1"), ("2026", "2"), ("2026", "3")]
m = base
for row, (fy, fq) in zip(order, labels):
    m = change(m, table="T4.14", row=row, field="fiscal_year", text=fy)
    m = change(m, table="T4.14", row=row, field="fiscal_quarter", text=fq)
for label, mod in (("trailing four quarters across FY boundary", m),
                   ("EUR book", change(base, table="T4.14", field="currency", text="EUR"))):
    try:
        print(label, "->", [(s.fig_id, s.reason) for s in cp1_chart_series(mod)])
    except Exception as e:
        print(label, "-> RAISES", type(e).__name__, e)
