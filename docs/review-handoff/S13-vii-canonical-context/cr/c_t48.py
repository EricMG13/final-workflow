"""T4.8: in Q4 = FY - 9M YTD, the same-year 9M YTD is filed under 'Prior-Year Stub'."""
import sys
from datetime import date, timedelta
sys.path.insert(0, "tests")
import test_statement_quantity_outputs as t
import deploy_vii.statement_history as hm
from deploy_vii.canonical_tables import COLUMNS, _constructed, _keys
from deploy_vii.model_interface import _Tables
from deploy_vii.statement_history import statement_history

book = t._book()
fy = next(p for p in book.periods if p.period_id == "FY2024")
ytd_end = date(fy.end_date.year, 6, 29)
ytd = fy.model_copy(update={"period_id": "YTD9M2024", "period_type": "YTD", "fiscal_quarter": 3,
                            "end_date": ytd_end, "day_count": (ytd_end - fy.start_date).days + 1})
line = next(l for l in book.statement_lines if l.period_id == "FY2024" and l.quantity.kind == "monetary")
extra = line.model_copy(update={"line_id": line.line_id + ":ytd", "period_id": "YTD9M2024",
    "value": line.value.model_copy(update={"observation_id": line.value.observation_id + ":ytd"})})
book = book.model_copy(update={"periods": (*book.periods, ytd), "statement_lines": (*book.statement_lines, extra)})
print("FY", fy.start_date, fy.end_date, "YTD", ytd.start_date, ytd.end_date)
pack, review = t._pack_and_review(book)
report = t._report(book, pack, review)
hm.statement_report = lambda *_a: report
history = statement_history(pack, review, book.book_id)
for c in history.constructions:
    if c.kind == "QUARTER":
        print("construction", c.kind, c.label, c.start_date, c.end_date)
tables = _Tables(book, schemas={k: (title, None, _keys(k)) for k, (title, _) in COLUMNS.items()})
_constructed(tables, history)
rows = {}
for f in tables.facts:
    if f.table_id == "T4.8":
        rows.setdefault(f.row_id, {})[f.field] = f
print(sorted(next(iter(rows.values())).keys())); print({k:(v.text if hasattr(v,"text") else None) for k,v in next(iter(rows.values())).items()})
for r in []:
    if r["derived_period_type"].text == "QUARTER" and r["prior_year_stub"].text:
        print("period:", r["metric_name"].period)
        for k in ("full_year_component", "current_stub", "prior_year_stub"):
            print(" ", k, "->", r[k].text)
        break
