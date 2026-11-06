"""An income-statement unit whose dated header (52/53-week year) verifies a QUARTER map."""
from datetime import date
from types import SimpleNamespace as P
from deploy_workflow.html_text import convert_html
from deploy_workflow.statement_lines import line_table
from deploy_workflow.financial_workflow import _mapped_columns
from deploy_workflow.unit_maps import _header_verifies
from deploy_vii.contracts import Span

html = b"""<html><body><p>CONSOLIDATED STATEMENTS OF OPERATIONS</p><p>(In millions)</p><table>
<tr><td></td><td>Fiscal Year Ended</td></tr>
<tr><td></td><td>December 28, 2024</td><td>December 30, 2023</td></tr>
<tr><td>Net sales</td><td>$</td><td>1,234</td><td>$</td><td>1,100</td></tr>
<tr><td>Cost of sales</td><td>800</td><td>700</td></tr>
</table></body></html>"""
lines = convert_html(html).text.splitlines()
spans = {i: Span(locator=f"line:{i}", text=l) for i, l in enumerate(lines, 1)}
t = line_table(spans, f"line:3-{len(lines)}", "fin")
print("headers:", t.headers)
print("rows:", [(r.label, r.values) for r in t.lines])
periods = [
    P(period_id="fy-2024", fiscal_year="2024", fiscal_quarter=None, period_type="FY",
      start_date=date(2023, 12, 31), end_date=date(2024, 12, 28)),
    P(period_id="q4-2024", fiscal_year="2024", fiscal_quarter=4, period_type="QUARTER",
      start_date=date(2024, 9, 29), end_date=date(2024, 12, 28)),
    P(period_id="fy-2023", fiscal_year="2023", fiscal_quarter=None, period_type="FY",
      start_date=date(2023, 1, 1), end_date=date(2023, 12, 30)),
]
mapped = _mapped_columns(t.headers, periods)
print("mapped:", mapped)
print("model maps annual IS columns to q4-2024 / fy-2023 -> verified:",
      _header_verifies(mapped, ("q4-2024", "fy-2023")))
