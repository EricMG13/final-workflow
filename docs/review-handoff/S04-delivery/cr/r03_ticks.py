import re
from decimal import Decimal
from deploy_vii.report_view import ChartSpec, ChartMark, Block, Row, Cell
from deploy_vii.display import format_value
from deploy_vii import charts

def spec(kind, values, unit_class="amount"):
    marks = tuple(ChartMark(series="A", label=f"P{i}", value=Decimal(v), text=format_value(Decimal(v), unit_class, "known")) for i, v in enumerate(values))
    twin = Block(block_id="twin", title="t", owner="o", state="populated", kind="dense", columns=("Value",),
                 rows=tuple(Row(row_id=f"r{i}", label=m.label, cells=(Cell(text=m.text, state="known", prov="none", unit_class=unit_class),)) for i, m in enumerate(marks)))
    return ChartSpec(kind=kind, series=("A",), table_twin=twin, marks=marks, unit_class=unit_class)

for kind, vals in [("line", ["0.4", "0.8"]), ("grouped", ["0.03", "0.05"]), ("waterfall", ["4", "5"])]:
    svg = charts.render_svg(spec(kind, vals), chart_id="c", title="t")
    ticks = re.findall(r'class="ax">([^<]*)</text>', svg)
    print(kind, vals, "axis labels:", [t for t in ticks if not t.startswith("P")])
