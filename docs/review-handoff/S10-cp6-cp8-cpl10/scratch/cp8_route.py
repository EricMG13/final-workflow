from deploy_vii.registry import modules
from deploy_workflow.owner_workflow import OWNER_SPECS
from deploy_workflow.owners import cp8
m = next(m for m in modules() if m.module_id == "CP-8")
print("registry title:", m.title, "| required:", m.required, "| optional:", m.optional)
spec = OWNER_SPECS["CP-8"]
print("native owner step:", [s.step_id if hasattr(s,'step_id') else s for s in spec.steps][0])
print("owner decision source:", cp8.DECISION_SOURCE, "| labels:", cp8.LABELS[:3], "| LIM_ONE_DECISION:", cp8.LIM_ONE_DECISION[:60])
