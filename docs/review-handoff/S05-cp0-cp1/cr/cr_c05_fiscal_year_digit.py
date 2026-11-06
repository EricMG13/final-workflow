"""CR-C05: cp1b._default_pairs calls int() on any str.isdigit() fiscal year; a superscript digit
passes isdigit() and the FinancialPeriod validator but int() raises (view() crashes)."""
from types import SimpleNamespace as NS
from deploy_vii.model.dates import fiscal_year_number
from deploy_workflow.owners import cp1b
fy = "2025²"
print("fiscal_year_number accepts:", fiscal_year_number(fy), "| isdigit:", fy.isdigit(), "| isascii:", fy.isascii())
rows = {"q4-2025": {"fiscal_year": NS(text=fy), "period_type": NS(text="QUARTER")}}
print("_prior_year (guarded):", cp1b._prior_year(rows, "q4-2025"))
try:
    print(cp1b._default_pairs(rows))
except ValueError as e:
    print("_default_pairs RAISES:", e)
