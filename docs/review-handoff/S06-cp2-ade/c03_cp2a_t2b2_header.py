import test_method_cp2a as tm
result, _, _ = tm.composed("positive")
for t in result.tables:
    if t.table_id in ("T2B.2", "T2B.3"):
        print(t.table_id, t.title, "columns:", [(c.field, c.label) for c in t.columns])
        print("   rows:", [r.label for r in t.rows])
