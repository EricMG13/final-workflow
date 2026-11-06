import deploy_vii.live.submission as sub
from deploy_vii.execution import StepValidation
step_id = next(s for s, st in sub.STEPS.items() if st.module_id == "CP-3")
calls = []
def rules(p):
    calls.append(len(p)); return ("Unread page: S1 page:3",)
class FakeStore:
    def pack(self): return None
    def submit_step(self, ticket, module, seq, step, payload, validator):
        return validator(None, None)
sub.RULED_ENTRIES = {**sub.RULED_ENTRIES, "CP-3": lambda store, pack, attempt: StepValidation(output="{}")}
out = sub.submit_model_payload(FakeStore(), "t", step_id, "{}", rules=rules)
print("step", step_id, "rules() calls for one submit:", len(calls))
