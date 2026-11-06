from deploy_vii.contracts import Span
from deploy_vii.live.tools import _line_table, extracted_body
texts = {
 100: "Consolidated Statement of Operations",
 101: "(in thousands)                     2024        2023",
 102: "",
 103: "Revenue from contracts",
 104: "  with customers                  1,234       1,100",
 105: "Cost of revenue                    (500)       (450)",
}
spans = {n: Span(locator=f"line:{n}", text=t) for n, t in texts.items()}
table = _line_table(spans, "line:100-105", "S1")
for line in table.lines:
    print("row", line.line_no, line.locator, [(p.line_no, p.text) for p in line.label_candidates])
print("omitted", table.omitted)
print(extracted_body(table))
