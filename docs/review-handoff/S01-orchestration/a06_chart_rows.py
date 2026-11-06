"""Attack: chart_issues skips rows[0:2] assuming header+separator. (a) a chart table with no data
rows, (b) a table without the |---| separator whose first data row holds a non-number."""
from deploy_workflow.owners.cpos_launch import chart_issues, _chart_route, _chart_header
route = _chart_route("leverage-coverage", "S.1")
head = "| " + " | ".join(_chart_header(route)) + " |"
base = "## Findings\n\n### Chart data: leverage\n\n"
a = base + head + "\n| --- | --- | --- | --- | --- |\n"
b = base + head + "\n| FY2024 | about four | n/a | x | |\n| FY2023 | 4.2 | 3.9 | x | Reported. |\n"
c = base + head + "\n| --- | --- | --- | --- | --- |\n| FY2024 | about four | n/a | x | |\n"
print("(a) header only, issues:", chart_issues(a, route))
print("(b) no separator, bad first row, issues:", chart_issues(b, route))
print("(c) control: same bad row after separator, issues:", len(chart_issues(c, route)))
