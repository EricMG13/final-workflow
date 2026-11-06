from deploy_vii.live.submission import STEPS
from deploy_vii.live.schema import _admits_null, _Walker
seen=set()
for sid, d in STEPS.items():
    s = d.schema.model_json_schema(); w=_Walker(s)
    nodes=[("root",s)]+list(s.get("$defs",{}).items())
    for owner,node in nodes:
        for name,prop in node.get("properties",{}).items():
            if "default" in prop and name not in node.get("required",[]):
                spec = w.resolve(prop) if "$ref" in prop else prop
                dv=prop["default"]
                if not _admits_null(spec) and dv not in ([],{},(),"",None,False,0):
                    key=(owner,name,repr(dv))
                    if key not in seen:
                        seen.add(key); print(sid, owner, name, repr(dv)[:60])
