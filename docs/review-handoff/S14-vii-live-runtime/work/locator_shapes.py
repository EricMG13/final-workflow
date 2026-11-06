from deploy_vii.live.submission import STEPS
from deploy_vii.live.tools import applicable_rules
from deploy_vii.registry import tool_set
for sid, d in STEPS.items():
    s = d.schema.model_json_schema()
    odd=[]
    for owner,node in [("root",s)]+list(s.get("$defs",{}).items()):
        props=node.get("properties",{})
        if "locator" in props and "source_id" not in props: odd.append(owner)
        for n in props:
            if "locator" in n.lower() and n!="locator": odd.append(f"{owner}.{n}")
            if n in ("page","pages","page_number"): odd.append(f"{owner}.{n}")
    print(sid, tool_set(sid), applicable_rules(sid), odd)
