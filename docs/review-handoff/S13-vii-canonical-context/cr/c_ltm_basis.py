"""A QUARTER column's LTM leverage reads rolling (4Q) cells but is labelled with the quarter basis."""
from decimal import Decimal as D
from types import SimpleNamespace
import deploy_vii.canonical_kpis as ck
from deploy_vii.model.frame import Cell, Column
from deploy_vii.financial_model import _basis_id

ck.normalize_facilities = lambda book: ()
ck._evidence = lambda book, n: {}
col = Column("Q:q3-2025", "QUARTER", "Q3 25", "q3-2025", "2025", "2025-09-30", 92, None)
def cells(ebitda, debt):
    d = {k: Cell(None, "NOT_SOURCED") for k in ck._SCALARS}
    d["ebitda"] = Cell(D(ebitda), basis="REPORTED"); d["total_debt"] = Cell(D(debt), basis="REPORTED")
    return d
frame = {col.column_id: cells(25, 500)}     # quarter EBITDA 25
rolling = {col.column_id: cells(100, 500)}  # LTM EBITDA 100
book = SimpleNamespace(currency="USD", unit="MILLIONS")
rows = ck._kpi_rows((col,), frame, rolling, book, {})
r = next(r for r in rows if r.key == "total_leverage_reported")
print("value:", r.value.amount)
print("display_basis is quarter basis:", r.display_basis_id == _basis_id(col))
print("operands basis is rolling:", {o.value_id for o in r.denominator.operands} == {ck._value_id(_basis_id(col, True), "ebitda")})
