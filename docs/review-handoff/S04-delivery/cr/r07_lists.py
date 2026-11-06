from deploy_workflow.markdown_delivery import literal_module
raw = b"# CP-1B TDG\n## Request\nTDG.\n## Sources\nS.\n## Findings\n### Watch\n- Track cash interest\n- Track `covenant` headroom\n1. First\n2. Second\n## Calculations\nNone.\n## Gaps\nT.\n## Next module\nD.\n"
m, _, meta = literal_module("CP-1B", raw)
for f in m.facts:
    if meta.get(f.table_id) == ("Watch", "prose"):
        print(repr(f.text), [c.locator for c in f.citations])
