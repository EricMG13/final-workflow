from deploy_vii.live.submission import STEPS, PREFILLED
from deploy_vii.live.schema import prefilled_kind
for step_id in PREFILLED:
    schema = STEPS[step_id].schema.model_json_schema()
    defs = schema.get("$defs", {})
    hits = set()
    def walk(node, path, union, seen):
        if not isinstance(node, dict): return
        ref = node.get("$ref")
        if ref:
            name = ref.split("/")[-1]
            if name in seen: return
            walk(defs.get(name), path, union, seen | {name}); return
        for key, prop in node.get("properties", {}).items():
            if prefilled_kind(prop) is not None:
                hits.add((path + key, union, "discriminator" in str(node)[:0]))
            else:
                walk(prop, path + key + ".", union, seen)
        if "items" in node: walk(node["items"], path + "N.", union, seen)
        for k in ("anyOf", "oneOf"):
            opts = node.get(k, ())
            real = [o for o in opts if o.get("type") != "null"]
            for o in opts: walk(o, path, union or len(real) > 1, seen)
    walk(schema, "", False, frozenset())
    inunion = sorted(h[0] for h in hits if h[1])
    print(step_id, "marked:", len(hits), "behind a multi-branch union:", inunion[:8])
