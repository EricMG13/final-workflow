"""CP-5 figure_identity: a verbatim CP-4 T4F.2 copy (and CP-4C cp2g/cp2a/cp4_references copies)
of an upstream fact is reported as a Figure mismatch although the value is identical."""
from decimal import Decimal
from datetime import date
from deploy_vii.contracts import Fact, Module, ReportTable, TableColumn, TableRow
from deploy_vii import cp5_integrity as c5

src = Fact(fact_id="interface-fact:abc", label="Net leverage", table_id="T4.10", row_id="net_leverage",
           field="ltm", amount=Decimal("4.2"), unit="MULTIPLE", period="LTM Q4 25")
# What cp4_legal._referenced_table writes: same fact_id, new placement, value untouched.
copy = src.model_copy(update={"table_id": "T4F.2", "row_id": "ref01", "field": "value"})

def mod(mid, fact):
    t = ReportTable(table_id=fact.table_id, title="t", columns=(TableColumn(field=fact.field, label="v"),),
                    rows=(TableRow(row_id=fact.row_id, label="r", fact_ids=(fact.fact_id,)),))
    return Module(run_id="r", issuer_id="i", as_of=date(2026,1,1), module_id=mid, status="accepted",
                  facts=(fact,), tables=(t,))

heads = [mod("CP-1", src), mod("CP-4", copy)]
print("identical value/unit/period:", c5.exact_value(src) == c5.exact_value(copy), src.unit == copy.unit, src.period == copy.period)
for f in c5.figure_identity(heads):
    print("FINDING:", f.kind, f.subject, "|", f.detail)
# control: the same copy under cp1_references is accepted
ctrl = src.model_copy(update={"table_id": "cp1_references", "row_id": "ref01", "field": "value"})
print("control findings (cp1_references):", c5.figure_identity([mod("CP-1", src), mod("CP-4", ctrl)]))
