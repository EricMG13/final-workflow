"""A CFS cash-taxes line explicitly declared `signed` with a printed net refund (+15)
is turned into an outflow of -15 by the statement report and the reconciliation term.

Hand-derived expectation: sign_convention="signed" means the amount already carries the
source sign; a net refund of 15 stays +15 (an inflow). Only `outflow_magnitude` rows may be
negated.
"""
import sys
sys.path.insert(0, "tests")
from decimal import Decimal
import test_statement_quantities as q
from deploy_vii.financial_contracts import Observation
from deploy_vii.statement_output import _cells
from deploy_vii.financial_reconciliation import _account

obs = Observation(observation_id="obs-tax", status="known", amount=Decimal(15),
                  citations=(q.cite("Income taxes refunded (paid), net | 15"),))
ln = q.line("tax", "FY2024", "cash_taxes_paid", statement="CFS").model_copy(update={"value": obs})
assert ln.sign_convention == "signed"
book = q.book((ln,))
cell = next(c for c in _cells(book) if c.item_id == "cash_taxes_paid" and c.period_id == "FY2024")
print("statement_output: source", cell.source_amount, "normalized", cell.normalized_amount, cell.normalization)
term = _account(book, "FY2024", "cash_taxes_paid")
print("reconciliation term: original", term.original_amount, "amount", term.amount)
