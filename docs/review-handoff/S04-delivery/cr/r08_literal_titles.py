import hashlib
from deploy_workflow.model_handoff_delivery import _literal_tables
raw = b"""# CP-2 TDG
## Request
TDG.
### Request detail
Scope words.
## Sources
None.
## Findings
**Assessment \xe2\x80\x94** Leverage is high and the long paragraph continues here at length.
| Metric | FY2024 |
|---|---|
| Revenue | 100 |
## Calculations
| Calc | Value |
|---|---|
| Margin | 0.5 |
## Gaps
| Gap | Why |
|---|---|
| G | x |
## Next module
D.
"""
_, _, tables, _ = _literal_tables("current_synthesis", raw, hashlib.sha256(raw).hexdigest())
for t in tables: print(t.table_id, "|", t.title)
