"""absent_input_limitation downgrades structural BLOCKs where every input is present."""
from decimal import Decimal
from datetime import date
from deploy_vii.financial_reconciliation import ReconciliationTerm, _check
from deploy_vii.financial_contracts import FinancialPeriod
from deploy_vii.canonical_audit import absent_input_limitation

def t(label, amt, oid, coef=1):
    return ReconciliationTerm(label=label, observation_id=oid, original_amount=Decimal(amt),
                              amount=Decimal(amt), coefficient=coef, citations=())

period = FinancialPeriod.model_construct(period_id="fy2024", citations=(), expense_presentation="unknown")
# Hand-derived: revenue 100 + cogs -40 + opex -30 - (da -10) = 40, reported EBITDA 55 -> real disagreement of 15.
check = _check(period, "EBITDA_BRIDGE", "ebitda", t("ebitda", "55", "o-ebitda"),
               (t("revenue","100","o-rev"), t("cogs","-40","o-cogs"), t("opex","-30","o-opex"), t("da","-10","o-da",-1)),
               "revenue + cogs + opex - da", blocker="Expense presentation is unknown")
print("status", check.status, "difference", check.difference, "explanation", check.explanation)
print("all inputs present:", all(x.amount is not None for x in (check.reported, *check.components)))
lim = absent_input_limitation(check, public=True, conflicting=frozenset())
print("limitation ->", repr(lim))
print("severity in audit/gap ledger ->", check.status if lim is None else "WARN")
