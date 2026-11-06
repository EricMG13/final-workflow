"""C04: respace/_NUMTOK know only '$'; euro/pound value cells are not re-spaced and line_table drops the row."""
from deploy_vii.contracts import Span
from deploy_vii.statement_extract import extract_statement_lines
from deploy_workflow.statement_lines import line_table, respace

def spans(lines):
    return {i + 1: Span(locator=f"line:{i+1}", text=t) for i, t in enumerate(lines)}

for sym in ("$", "€", "£"):
    lines = ["CONSOLIDATED INCOME STATEMENT", "2024 2023",
             f"Revenue {sym} 1,234 {sym} 1,100", "Cost of sales (800) (700)",
             f"Operating profit {sym} 434 {sym} 400"]
    print(sym, "respace:", repr(respace(lines[2])))
    try:
        t = line_table(spans(lines), f"line:1-{len(lines)}", "s")
        print(sym, "line_table rows:", [(r.label, r.values if hasattr(r, "values") else r.cells if hasattr(r, "cells") else None) for r in t.lines])
    except Exception as e:
        print(sym, "RAISES", type(e).__name__, e)
# Does DVII itself read euro cells when they ARE double-spaced?
txt = "CONSOLIDATED INCOME STATEMENT\n2024  2023\nRevenue  € 1,234  € 1,100\nOperating profit  € 434  € 400"
print("DVII on pre-spaced euro lines:", [r.label for r in extract_statement_lines(txt, "line:1-4", source_id="s").lines])
txt2 = "CONSOLIDATED INCOME STATEMENT\n2024  2023\nRevenue  1,234  1,100\nOperating profit  434  400"
print("DVII on pre-spaced bare lines:", [r.label for r in extract_statement_lines(txt2, "line:1-4", source_id="s").lines])
