import sys, os, json; sys.path.insert(0, os.path.dirname(__file__))
from common import deliver
MD = """# CP-1B TransDigm Group Incorporated
## Request
Earnings view.
## Sources
None.
## Findings
### Notes
Findings note one.
## Calculations
### Notes
Calculation note two (different section).
## Gaps
None.
## Next module
Delivery.
"""
from deploy_workflow.markdown_delivery import literal_module
m, _, meta = literal_module("CP-1B", MD.encode())
for t in m.tables:
    if meta[t.table_id] == ("Notes", "prose"):
        print(t.table_id, t.title, [r.label for r in t.rows])
blocks = ["watch-items"]
routes = [{"module_id": "CP-1B", "heading": "Notes", "kind": "prose", "block_id": "watch-items", "label": "Findings notes"}]
files = deliver(MD, blocks, routes)
rv = json.loads(files["report-view.json"])
b = next(b for b in rv["blocks"] if b["block_id"] == "watch-items")
print([r["text"] for l in b["lines"] for r in l["runs"] if r["kind"] != "fig"])
