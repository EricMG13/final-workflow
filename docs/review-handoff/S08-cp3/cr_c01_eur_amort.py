"""CP-3C: a EUR facility whose T4.18 annual_amortisation is in EUR (as CP-2D requires) crashes."""
from dataclasses import replace
import tests.test_method_cp3c as t
from deploy_workflow.owners import cp3c

fx = "Not calculable: facility term-loan is in EUR, not USD; no FX conversion is applied"
row = t._positive_row()
wall = (replace(row, principal=t._gone(row.principal, fx)),)
terms = replace(t._positive_terms(), currency="EUR")
print("amortisation fact:", terms.annual_amortisation.status, terms.annual_amortisation.amount, terms.annual_amortisation.currency)
r = cp3c.compute(t._positive_with(terms, wall=wall))
print("baseline (amortisation stamped USD): ok, own gaps", len(t._own_gaps(r)))
terms_eur = replace(terms, annual_amortisation=replace(terms.annual_amortisation, currency="EUR"))
try:
    cp3c.compute(t._positive_with(terms_eur, wall=wall))
    print("EUR amortisation: ok")
except Exception as e:
    print("EUR amortisation:", type(e).__name__, e)
