"""A T4.12 gap row with no periods records field_2=None as an InterfaceGap, which the
projection-gap loop in canonical_tables() then turns into another T4.12 row."""
import sys
sys.path.insert(0, "tests")
import test_statement_quantity_outputs as t
from deploy_vii.canonical_tables import COLUMNS, _keys, _row, _join
from deploy_vii.financial_periods import _id
from deploy_vii.model_interface import _Tables

tables = _Tables(t._book(), schemas={k: (title, None, _keys(k)) for k, (title, _) in COLUMNS.items()})
# Exactly what _decisions writes for a narrative gap with no periods.
_row(tables, "T4.12", "gap-funding", _join(()) or "Unspecified gap scope",
     ("gap-funding: Funding not assessed", "funding", _join(()), "impact", "WARN", "action"))
print("gaps after upstream row:", [(g.table_id, g.field, g.reason) for g in tables.gaps])
# The projection-gap loop body from canonical_tables() (lines 810-824):
for gap in tuple(tables.gaps):
    _row(tables, "T4.12", _id("projection-gap", gap.table_id, gap.row_id, gap.field), "See referenced row",
         (f"{gap.table_id}/{gap.row_id}/{gap.field}: {gap.reason}", gap.field, "See referenced row",
          "Review source/analysis completeness", "WARN", "Resolve or retain the explicit limitation"))
print("T4.12 rows:", len(tables.rows["T4.12"]))
print([f.text for f in tables.facts if f.table_id == "T4.12" and f.field == "field_0"])
