"""CP-3: an Insufficient Information preference with no market basis still publishes an ordering."""
import dataclasses
import tests.test_method_cp3 as t
from deploy_workflow.owners.cp3 import compute

inputs = t.make_inputs("positive")
pref = inputs.submission.preference.model_copy(update={
    "confidence": "Insufficient Information",
    "basis": inputs.submission.preference.basis.model_copy(update={"quotes": ()}),
    "limitation": "Evidence does not support a ranking.",
})
sub = inputs.submission.model_copy(update={"preference": pref})
r = compute(dataclasses.replace(inputs, submission=sub))
print("issues:", r.issues)
if r.report:
    print({f.field: f.text for f in r.report.facts if f.table_id == "T3.4"})
