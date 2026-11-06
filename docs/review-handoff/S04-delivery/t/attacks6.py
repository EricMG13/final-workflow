import sys
sys.path.insert(0, "/tmp/claude-0/-workspace-final-workflow/10d71552-cdca-5952-86dc-d4ef0b76ab9e/scratchpad/review/S04-delivery/t")
import harness
from harness import *
fin = "All amounts in EUR thousands; FY2024 is unaudited.\n\n| Metric | FY2023 | FY2024 |\n| --- | ---: | ---: |\n| Revenue | 1,000.5 | 1,200.0 |\n"
files, rv, view = deliver(handoff(fin_table=fin))
b = [b for b in rv.blocks if b.block_id == "financials-credit-metrics"][0]
d = b.model_dump()
print({k: d[k] for k in ("title","note","scale","row_header","columns","meta","summary") if k in d})
print([(r.label, [c.text for c in r.cells]) for r in b.rows])
txt = b.model_dump_json()
print("EUR thousands anywhere in financials block:", "EUR thousands" in txt)
other = [x.block_id for x in rv.blocks if "EUR thousands" in x.model_dump_json()]
print("blocks carrying it:", other)
