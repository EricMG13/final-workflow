"""O1 (compose) names the only admissible inputs; the CP-OS handoff message appended by factory is none of them."""
import inspect
from deploy_workflow.prompts import compose, factory
from deploy_workflow import cpos_handoffs
print("O1:", compose.O1)
print("O2:", compose.O2)
src = inspect.getsource(cpos_handoffs.prompt_messages)
print("handoff message prefix present:", "Retained upstream analytical handoffs" in src)
print("factory appends via prompt_messages:", "prompt_messages(store, binding, messages)" in inspect.getsource(factory.prompt_factory))
print("O1 mentions handoff:", "handoff" in compose.O1.lower(), "| O2 mentions handoff:", "handoff" in compose.O2.lower())
