from deploy_workflow.markdown_delivery import literal_module
raw = b"""# CP-1B TDG
## Request
TDG.
## Sources
None.
## Findings
### Covenants
| Covenant | Headroom |
| Net leverage 7.25x | DROPPED-ROW-ONE |
| Interest cover 2.0x | DROPPED-ROW-TWO |
|Pipe-led caveat line DROPPED-CAVEAT
## Calculations
None.
## Gaps
None.
## Next module
D.
"""
m, _, meta = literal_module("CP-1B", raw)
texts = [f.text or "" for f in m.facts] + [c.quote for f in m.facts for c in f.citations]
for tok in ("DROPPED-ROW-ONE", "DROPPED-ROW-TWO", "DROPPED-CAVEAT"):
    print(tok, "retained in any fact:", any(tok in t for t in texts))
print("tables:", [(t.table_id, meta[t.table_id]) for t in m.tables])
