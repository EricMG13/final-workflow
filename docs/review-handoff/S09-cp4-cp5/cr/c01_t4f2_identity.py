"""CP-5 figure_identity flags CP-4's verbatim T4F.2 copy of a CP-1 figure."""
from datetime import date
from decimal import Decimal
from deploy_vii.contracts import Fact, Module
from deploy_vii.cp4_legal import REGISTERS
from deploy_vii.cp5_integrity import figure_identity, REFERENCE_TABLES

src = Fact(fact_id="net_leverage_reported", label="Net leverage", table_id="T1.9",
           row_id="net_leverage", field="value", amount=Decimal("3.2"), unit="MULTIPLE",
           period="FY2024")
# exactly what cp4_legal._referenced_table does
copy = src.model_copy(update={"table_id": REGISTERS["T4F.2"].table_id, "row_id": "ref01", "field": "value"})
base = dict(run_id="r", issuer_id="i", as_of=date(2025, 1, 1))
cp1 = Module(module_id="CP-1", facts=(src,), **base)
cp4 = Module(module_id="CP-4", facts=(copy,), **base)
print("REFERENCE_TABLES =", sorted(REFERENCE_TABLES), "copy table =", copy.table_id)
for f in figure_identity([cp1, cp4]):
    print(f.kind, f.subject, "|", f.detail)
