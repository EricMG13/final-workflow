from decimal import Decimal as D
from deploy_vii.canonical_kpis import _canonical_frame
from deploy_vii.model._cells import ABSENT
from deploy_vii.model.frame import Cell
from deploy_vii.model import statements as st

# Column where add-back "restructuring" has no row in this column's periods (NOT_SOURCED),
# reported EBITDA 45, no stated adjusted EBITDA.
accounts = {"FY:fy2023": {"acct:ebitda": Cell(D(45), basis="REPORTED"),
                          "addback:restructuring": ABSENT}}
stmt = {"FY:fy2023": {"revenue": Cell(D(100), basis="REPORTED"), "cogs": Cell(D(-40), basis="REPORTED"),
                      "opex_total": Cell(D(-20), basis="REPORTED"), "da": Cell(D(-5), basis="REPORTED"),
                      "ebitda": Cell(D(45), basis="REPORTED")}}
canon = _canonical_frame(accounts, stmt, {})["FY:fy2023"]["adjusted_ebitda"]
print("canonical adjusted_ebitda:", canon.value, canon.reason, canon.note)

get = lambda k: accounts["FY:fy2023"].get(k, stmt["FY:fy2023"].get(k, ABSENT))
model = st._income(get, accounts["FY:fy2023"], frozenset())
print("model/statement adjusted_ebitda:", model["adjusted_ebitda"].value, model["adjusted_ebitda"].reason)
