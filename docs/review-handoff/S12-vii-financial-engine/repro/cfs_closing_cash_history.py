"""statement_history sums CFS opening/closing cash balances as period flows.

Hand-derived expectation: the Q2 2024 column (derived as H1 - Q1) of the CFS
`closing_cash` item is the cash balance at 2024-06-30 = 520 (the H1 closing cash
printed on the CFS), never 520 - 500 = 20. Its `opening_cash` is the balance at
2024-03-31 = 500 (Q1's closing), never 480 - 480 = 0.
"""
import sys
sys.path.insert(0, "tests")
from datetime import date
from decimal import Decimal
import test_statement_quantities as q
import test_statement_quantity_outputs as qo
from deploy_vii.financial_contracts import FinancialPeriod, Observation
from deploy_vii.statement_history import statement_history

cite = q.cite("interim period date")
def per(pid, typ, fq, start, end):
    return FinancialPeriod(period_id=pid, fiscal_year="FY2024", fiscal_quarter=fq, period_type=typ,
        start_date=start, end_date=end, day_count=(end-start).days+1, audit_status="unaudited",
        currency="USD", unit="MILLIONS", accounting_basis="US GAAP", entity_perimeter="Consolidated",
        citations=(cite,))
periods = (per("Q1","QUARTER",1,date(2024,1,1),date(2024,3,31)), per("H1","YTD",2,date(2024,1,1),date(2024,6,30)))
vals = {("opening_cash","Q1"):480, ("opening_cash","H1"):480, ("closing_cash","Q1"):500, ("closing_cash","H1"):520,
        ("net_cash_change","Q1"):20, ("net_cash_change","H1"):40}
lines = []
pri = 0
for (item, pid), amt in vals.items():
    pri += 1
    obs = Observation(observation_id=f"obs:{item}:{pid}", status="known", amount=Decimal(amt),
                      citations=(q.cite(f"{item} {pid} {amt}"),))
    lines.append(q.line(f"{item}-{pid}", pid, item, statement="CFS", priority=pri).model_copy(update={"value": obs}))
book = q.book(tuple(lines)).model_copy(update={"periods": periods})
pack, review = qo._bound_pack_review(book)
h = statement_history(pack, review, book.book_id)
labels = {c.construction_id: (c.label, c.kind) for c in h.constructions}
for v in h.values:
    if v.item_id in {"closing_cash","opening_cash","net_cash_change"}:
        print(labels[v.construction_id], v.item_id, v.value.amount, v.value.calculation_status, v.value.value_class)
