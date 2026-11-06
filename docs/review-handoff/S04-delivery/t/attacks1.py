import sys, re, json
sys.path.insert(0, "/tmp/claude-0/-workspace-final-workflow/10d71552-cdca-5952-86dc-d4ef0b76ab9e/scratchpad/review/S04-delivery/t")
from harness import *

def strip(rv):
    return {f.fig_id: f for b in rv.blocks for f in b.figures}

print("== A1 descending period rows -> category (x-axis) order")
files, rv, view = deliver(handoff(leverage=[("FY2024","3.8","3.5"),("FY2023","4.1","3.9"),("FY2022","5.0","4.6")]))
f = strip(rv)["S.1"]
from deploy_vii.charts import _categories
print("categories left->right:", _categories(f.chart))

print("== A2 Reporting unit EUR m accepted and labelled US$m by markdown_files")
files, rv, view = deliver(handoff(unit_liq="EUR m"))
f = strip(rv)["S.3"]
print(f.chart.unit, [(m.series, m.label, m.value) for m in f.chart.marks])
from deploy_workflow.owners.cpos_launch import _layout, chart_issues
layout,_ = _layout(RUN, ("CP-1",), (), "cfg")
r = [x for x in layout.routes if x.figure_id=="S.3"][0]
print("cpos chart_issues gate:", chart_issues(handoff(unit_liq="EUR m"), r))

print("== A3 U+2028 inside a prose line shifts every later citation locator")
text = handoff(extra_findings="Revenue rose  strongly.\n\nLater paragraph about leverage.\n\n")
files, rv, view = deliver(text)
raw = text.encode()
phys = raw.split(b"\n")
mod = [m for m in view.modules if m.module_id=="CP-1"][0]
bad = 0
for fact in mod.facts:
    for c in fact.citations:
        n = int(c.locator.split()[-1])
        if phys[n-1].decode() != c.quote:
            bad += 1
            if bad <= 3: print("  locator", c.locator, "quote", repr(c.quote[:40]), "physical line is", repr(phys[n-1][:40]))
print("citations whose 'line N' != physical newline-delimited line N:", bad)

print("== A4 multi-line HTML comment published as prose")
text = handoff(extra_findings="<!--\nDRAFT: internal estimate 999 not for publication\n-->\n\n")
files, rv, view = deliver(text)
mod = [m for m in view.modules if m.module_id=="CP-1"][0]
print([f.text for f in mod.facts if f.text and "DRAFT" in (f.text or "")])
print("in report.html:", b"DRAFT: internal estimate 999" in files["report.html"])

print("== A5 trailing space after a table's closing pipe")
try:
    deliver(handoff(fin_table="| Metric | FY2023 | FY2024 |\n| --- | ---: | ---: |\n| Revenue | 1 | 2 | \n"))
    print("accepted")
except ValueError as e:
    print("refused:", e)

print("== A6 CRLF handoff")
try:
    files, rv, view = deliver(None, raw=handoff().replace("\n","\r\n").encode())
    print("CRLF ok", [b.state for b in rv.blocks])
except Exception as e:
    print("CRLF refused", type(e).__name__, e)
