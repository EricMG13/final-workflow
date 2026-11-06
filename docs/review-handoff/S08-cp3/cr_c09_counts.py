"""CP-3: count validation passes and catalogue rebuilds per compute()."""
import dataclasses, time
import deploy_vii.cp3_relative_value as rv
import tests.test_method_cp3 as t
from deploy_workflow.owners import cp3

counts = {"validate": 0, "catalogue": 0, "context": 0}
ov, oc, oe = rv.validate_relative_value, rv.cp2_catalogue, rv.context_evidence
def v(*a, **k): counts["validate"] += 1; return ov(*a, **k)
def c(*a, **k): counts["catalogue"] += 1; return oc(*a, **k)
def e(*a, **k): counts["context"] += 1; return oe(*a, **k)
rv.validate_relative_value, rv.cp2_catalogue, rv.context_evidence = v, c, e
cp3.validate_relative_value = v
inputs = t.make_inputs("positive")
risks = tuple(inputs.submission.risks[0].model_copy(update={"cp2_refs": ("T2.11.r01",) * 1}) for _ in range(10))
inputs = dataclasses.replace(inputs, submission=inputs.submission.model_copy(update={"risks": risks}))
t0 = time.perf_counter(); r = cp3.compute(inputs); dt = time.perf_counter() - t0
print("issues:", r.issues[:2], "| counts:", counts, f"| {dt*1000:.0f} ms")
