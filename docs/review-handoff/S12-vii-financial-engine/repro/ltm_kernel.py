"""Hand-derived LTM / quarter derivation checks on the kernel."""
from decimal import Decimal as D
from deploy_vii.model.registers import Cp1Registers, PeriodRow, AccountRow
from deploy_vii.model.frame import SourceRef
from deploy_vii.model import history

def P(pid, fy, q, typ, start, end, comps=()):
    from datetime import date
    days = None
    if start and end:
        days = (date.fromisoformat(end) - date.fromisoformat(start)).days + 1
    return PeriodRow(pid, fy, q, typ, start, end, days, "USD", "MILLIONS", tuple(comps))

def A(metric, pid, v):
    return AccountRow(metric, pid, None if v is None else D(v), "VERIFIED", SourceRef(f"o-{metric}-{pid}", "financial-observation", str(v)))

def regs(periods, accounts):
    return Cp1Registers(tuple(periods), tuple(accounts), (), (), (), (), (), "USD", "MILLIONS")

def show(r, keys=("acct:revenue",)):
    cols = history.historical_columns(r)
    fr = history.account_frame(r, cols)
    for c in cols:
        for k in keys:
            cell = fr[c.column_id].get(k)
            print(f"{c.column_id:35s} {c.kind:7s} days={c.days} {k}={cell.value if cell else None} reason={cell.reason if cell else None} note={cell.note if cell else None} stated={cell.stated if cell else None}")
    return cols, fr

print("== Case 1: calendar FY2024 + H1 2024/H1 2025 (leap year)")
r = regs([
    P("fy24","FY2024",None,"FY","2024-01-01","2024-12-31"),
    P("h124","FY2024","2","YTD","2024-01-01","2024-06-30"),
    P("h125","FY2025","2","YTD","2025-01-01","2025-06-30"),
    P("q125","FY2025","1","QUARTER","2025-01-01","2025-03-31"),
], [A("revenue","fy24",1000),A("revenue","h124",480),A("revenue","h125",530),A("revenue","q125",250)])
show(r)
print("expected: LTM = 1000+530-480 = 1050, days 365; Q2 25 = 530-250 = 280, days 91")

print("== Case 2: 52/53 week retailer FY ending Sat nearest Jan 31")
r = regs([
    P("fy24","FY2024",None,"FY","2024-02-04","2025-02-01"),  # 52w = 364
    P("q324","FY2024","3","YTD","2024-02-04","2024-11-02"),  # 39w = 273
    P("q325","FY2025","3","YTD","2025-02-02","2025-11-01"),  # 39w
], [A("revenue","fy24",5200),A("revenue","q324",3800),A("revenue","q325",4000)])
show(r)
print("expected: LTM = 5200+4000-3800 = 5400, days 364; Q4 FY24 = 5200-3800 = 1400")

print("== Case 3: 53-week FY then 52-week YTD")
r = regs([
    P("fy23","FY2023",None,"FY","2023-01-29","2024-02-03"),  # 53w = 371
    P("q123","FY2023","1","QUARTER","2023-01-29","2023-04-29"),
    P("q124","FY2024","1","QUARTER","2024-02-04","2024-05-04"),
], [A("revenue","fy23",5300),A("revenue","q123",1200),A("revenue","q124",1300)])
show(r)
print("expected: LTM Q1 24 = 5300+1300-1200 = 5400, days 371-91+91... ")
