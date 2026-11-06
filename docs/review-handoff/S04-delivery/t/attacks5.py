import sys
sys.path.insert(0, "/tmp/claude-0/-workspace-final-workflow/10d71552-cdca-5952-86dc-d4ef0b76ab9e/scratchpad/review/S04-delivery/t")
from harness import *
files, rv, view = deliver(handoff(cover=[("FY2023","0.125"),("FY2024","12.3456")], liq=[("FY2023","0.004","1,234.5"),("FY2024","150","200")]))
for b in rv.blocks:
    for f in b.figures:
        if f.fig_id in {"S.2","S.3"}:
            print(f.fig_id, [(m.series, m.label, str(m.value), m.text) for m in f.chart.marks])
