"""C: adapter fills absent add-back periods with realization NOT_STATED; exclude_unrealised
then drops an add-back CP-1 disclosed as REALIZED from every column."""
from decimal import Decimal as D
from dataclasses import replace
from test_cash_scope import book, cite, observation
from deploy_vii.financial_contracts import AddbackObservation, Disclosure, AccountObservation
from deploy_vii.financial_adapter import _addbacks
from deploy_vii.model.statements import excluded_addbacks
from deploy_vii.model.registers import Cp1Registers

b = book()
ab = AddbackObservation(addback_id="restr", addback_label="Restructuring", classification="RESTRUCTURING",
    realization_status="REALIZED", display_priority=1, period_id="fy-2025",
    value=observation("ab-fy", 12, cite("Restructuring 12")), source_definition="x",
    classification_citations=(cite("Restructuring 12"),))
b2 = b.model_copy(update={"addbacks": (ab,), "addback_disclosure": Disclosure(
    status="complete", explanation="bridge", citations=(cite("bridge"),))})
rows = _addbacks(b2)
for r in rows:
    print(r.period_id, r.realization_status, r.value)
regs = Cp1Registers((), (), rows, (), (), (), (), "USD", "MILLIONS")
print("excluded with exclude_unrealised=True:", sorted(excluded_addbacks(regs, True)))
