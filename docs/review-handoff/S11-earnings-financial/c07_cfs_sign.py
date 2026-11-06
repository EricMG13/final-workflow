"""C07: CFS net-change check sums raw cells and ignores the row map's outflow_magnitude convention."""
from deploy_vii.contracts import Span
from deploy_workflow.statement_lines import line_table
from deploy_workflow.statement_compose import compose_unit, RowJudgment

lines = ["CONSOLIDATED STATEMENTS OF CASH FLOWS", "2025 2024",
         "Net cash provided by operating activities 400 300",
         "Net cash used in investing activities 250 200",
         "Net cash used in financing activities 100 50",
         "Net increase in cash 50 50"]
spans = {i + 1: Span(locator=f"line:{i+1}", text=t) for i, t in enumerate(lines)}
t = line_table(spans, f"line:1-{len(lines)}", "s")
print("rows:", [(r.line_no, r.label, r.values) for r in t.lines])
rows = {r.label: r.line_no for r in t.lines}
row_map = {
    rows["Net cash provided by operating activities"]: RowJudgment("op", "cfo_ncfo", "total", "signed"),
    rows["Net cash used in investing activities"]: RowJudgment("inv", "investing_cash_flow", "total", "outflow_magnitude"),
    rows["Net cash used in financing activities"]: RowJudgment("fin", "financing_cash_flow", "total", "outflow_magnitude"),
    rows["Net increase in cash"]: RowJudgment("net", "net_cash_change", "total", "signed"),
}
c = compose_unit(t, source_id="s", source_sha256="0" * 64, unit_locator="line:1-6", kind="CFS",
                 column_periods=["fy-2025", "fy-2024"], row_map=row_map, declared_periods={"fy-2025", "fy-2024"})
print("lines composed:", len(c.lines))
print("issues:", [i.message for i in c.issues])
print("left:", sorted({l.reason for l in c.left_to_model}))
