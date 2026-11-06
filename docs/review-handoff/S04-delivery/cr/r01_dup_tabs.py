import sys; sys.path.insert(0, __import__('os').path.dirname(__file__))
from common import deliver
MD = """# CP-1B TransDigm Group Incorporated
## Request
Earnings view: first paragraph.

Earnings view: second paragraph.

Scope note, not selected.
## Sources
None.
## Findings
### Values
| Metric | Value |
|---|---|
| Revenue | 1 |
## Calculations
None.
## Gaps
None.
## Next module
Delivery.
"""
blocks = ["headline-results"]
routes = [{"module_id": "CP-1B", "heading": "Request", "kind": "prose", "block_id": "headline-results", "prefix": "Earnings view", "label": "Earnings assessment"}]
try:
    files = deliver(MD, blocks, routes)
    print("OK", list(files))
except Exception as e:
    print(type(e).__name__, str(e)[:400])
