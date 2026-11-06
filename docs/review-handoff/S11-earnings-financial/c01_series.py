"""C01/C02: cp1_chart_series raises on a realistic extra T4.14 period (YTD/LTM, or FY alias without facility rows)."""
from decimal import Decimal
from deploy_vii.contracts import Fact
from test_financial_series import fixture
from deploy_workflow.financial_series import cp1_chart_series

base = fixture()
tmpl = [f for f in base.facts if f.table_id == "T4.14"]
first_row = tmpl[0].row_id
def add_period(module, pid, ptype, start, end, fq=None):
    new = []
    for f in tmpl:
        if f.row_id != first_row:
            continue
        val = {"period_id": pid, "period_type": ptype, "start_date": start, "end_date": end,
               "fiscal_quarter": fq if fq else "-", "fiscal_year": "2025"}.get(f.field, f.text)
        new.append(f.model_copy(update=dict(fact_id=f"T4.14.{pid}.{f.field}", row_id=f"T4.14.{pid}", text=val, period=pid)))
    return module.model_copy(update={"facts": (*module.facts, *new)})

def run(label, m):
    try:
        print(label, "->", [(s.fig_id, bool(s.points), s.reason) for s in cp1_chart_series(m)])
    except Exception as e:
        print(label, "-> RAISES", type(e).__name__, e)

run("baseline", base)
run("plus YTD six-month period 2025-01-01..2025-06-30", add_period(base, "ytd-h1-2025", "YTD", "2025-01-01", "2025-06-30"))
run("plus LTM period ending 2025-09-30", add_period(base, "ltm-q3-2025", "LTM", "2024-10-01", "2025-09-30"))
last_end = max(f.text for f in tmpl if f.field == "end_date")
run(f"plus FY alias ending {last_end} (no FY facility rows)", add_period(base, "fy-2025", "FY", "2025-01-01", last_end))
