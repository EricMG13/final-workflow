"""HTML statement rows: EDGAR split-parenthesis negatives, unicode minus, footnote markers."""
from deploy_workflow.html_text import convert_html
from deploy_workflow.statement_lines import line_table, respace
from deploy_vii.contracts import Span

html = b"""<html><body><table>
<tr><td></td><td>2024</td><td>2023</td></tr>
<tr><td>Revenue</td><td>$</td><td>1,234</td><td></td><td>$</td><td>1,100</td></tr>
<tr><td>Operating loss</td><td>$</td><td>(250</td><td>)</td><td>$</td><td>(10</td><td>)</td></tr>
<tr><td>Other expense</td><td>&#8722;45</td><td>&#8722;30</td></tr>
<tr><td>Net loss</td><td>$</td><td>(300)</td><td>$</td><td>(40)</td></tr>
</table></body></html>"""
text = convert_html(html).text
lines = text.splitlines()
for i, l in enumerate(lines, 1):
    print(i, repr(l), "->", repr(respace(l)))
spans = {i: Span(locator=f"line:{i}", text=l) for i, l in enumerate(lines, 1)}
t = line_table(spans, f"line:1-{len(lines)}", "fin")
print("headers", t.headers)
for row in t.lines:
    print(row.line_no, repr(row.label), row.values, row.flags)
