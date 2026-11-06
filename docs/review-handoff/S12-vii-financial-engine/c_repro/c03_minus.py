"""C: leading-minus / percent rows are neither data nor omitted."""
import inspect
from deploy_vii.statement_extract import extract_statement_lines
print(inspect.signature(extract_statement_lines))
text = "\n".join([
    "                         2025      2024",
    "Revenue                 1,000       900",
    "Net loss                 -120       -80",
    "Net loss (alt)          (120)      (80)",
    "Margin                  12.5%     10.0%",
    "Operating result         -1,234    2,345",
])
t = extract_statement_lines(text, "page-1")
for l in t.lines:
    print("LINE", l.label, l.raw_values)
print("OMITTED", t.omitted)
