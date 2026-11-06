from deploy_workflow.markdown_delivery import literal_module
raw = b"# CP-1B TDG\n## Request\nTDG.\n## Sources\nNone.\n## Findings\n### Risks\n#1 risk is the 2027 refinancing wall.\nSecond sentence.\n## Calculations\nNone.\n## Gaps\nNone.\n## Next module\nD.\n"
m, _, meta = literal_module("CP-1B", raw)
print(any("refinancing wall" in (f.text or "") for f in m.facts), [(meta[t.table_id], [r.label for r in t.rows]) for t in m.tables if "Risk" in meta[t.table_id][0] or "risk" in meta[t.table_id][0]])
