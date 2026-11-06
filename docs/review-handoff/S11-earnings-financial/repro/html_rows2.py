"""Footnote marker and note column on HTML line rows."""
from deploy_workflow.statement_lines import line_table, respace
from deploy_vii.contracts import Span

lines = [
    "(In millions) 2024 2023",
    "Revenue (1) $ 1,234 $ 1,100",
    "Cost of sales (2) 800 700",
    "Senior notes due 2027 500 450",
    "Interest expense 2,024 2,023",
]
for l in lines:
    print(repr(l), "->", repr(respace(l)))
spans = {i: Span(locator=f"line:{i}", text=l) for i, l in enumerate(lines, 1)}
t = line_table(spans, f"line:1-{len(lines)}", "fin")
print("headers", t.headers)
for row in t.lines:
    print(row.line_no, repr(row.label), row.values, row.raw_values, row.flags)
