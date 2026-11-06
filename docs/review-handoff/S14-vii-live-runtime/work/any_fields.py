from deploy_vii.live.submission import STEPS
from deploy_vii.live.schema import strict_copy, open_objects
def walk(node, path, out, defs):
    if isinstance(node, dict):
        if node == {} or ("type" not in node and not ({"$ref","anyOf","oneOf","allOf","enum","const","properties","items"} & set(node))):
            out.append(path)
        ap = node.get("additionalProperties")
        if ap not in (None, False):
            out.append(path+" [additionalProperties=%r]" % (ap,))
        for k,v in node.items():
            if k in ("properties","$defs") and isinstance(v, dict):
                for n,c in v.items(): walk(c, f"{path}.{n}", out, defs)
            elif k not in ("enum","const","required","default","discriminator"):
                walk(v, f"{path}/{k}", out, defs)
    elif isinstance(node, list):
        for i,x in enumerate(node): walk(x, f"{path}[{i}]", out, defs)
for sid, d in STEPS.items():
    s = d.schema.model_json_schema()
    out=[]; walk(s, sid, out, s.get("$defs",{}))
    print(sid, open_objects(s), out[:10])
