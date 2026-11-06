"""Canonical adjusted EBITDA derivation vs an add-back that has no row in this column."""
from decimal import Decimal as D
from deploy_vii.model.frame import Cell
from deploy_vii.model._cells import ABSENT
from deploy_vii.model.statements import _income
from deploy_vii.canonical_kpis import _canonical_frame

# FY2023 column: revenue 100, cogs -40, opex incl. D&A -30, D&A -10; no stated EBITDA/adj. EBITDA.
# Add-back "restructuring" 5 reported in this column; add-back "acquisition_costs" only exists in
# another column (account_frame gives it Cell(None, "NOT_SOURCED") here).
acct = {
    "acct:revenue": Cell(D(100)), "acct:cogs": Cell(D(-40)),
    "addback:restructuring": Cell(D(5)), "addback:acquisition_costs": ABSENT,
}
lines = {"revenue": Cell(D(100)), "cogs": Cell(D(-40)), "opex_total": Cell(D(-30)), "da": Cell(D(-10))}
get = lambda k: lines.get(k, acct.get(k, ABSENT))
stmt = _income(get, acct, frozenset())
print("statement adjusted_ebitda:", stmt["adjusted_ebitda"].value, stmt["adjusted_ebitda"].reason)
statement = {**lines, **stmt}
frame = _canonical_frame({"FY:2023": acct}, {"FY:2023": statement}, {})
c = frame["FY:2023"]
# Hand-derived: GP 60, EBIT 60-30=30, EBITDA 30+10=40, adj EBITDA 40+5=45
print("canonical ebitda:", c["ebitda"].value, " adjusted_ebitda:", c["adjusted_ebitda"].value, c["adjusted_ebitda"].reason, c["adjusted_ebitda"].note)
