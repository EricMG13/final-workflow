"""CP-3 with CP-2 accepted: a preference citing only indicative talk validates at High."""
import dataclasses
import tests.test_method_cp3 as t
from deploy_workflow.owners.cp3 import compute

inputs = t.make_inputs("positive")
bound = tuple(i.model_copy(update={"status": "accepted"}) if i.input_id == "CP-2" else i for i in inputs.bound)
inputs = dataclasses.replace(inputs, bound=bound, current=bound)
pref = inputs.submission.preference
talk = tuple(q for q in pref.basis.quotes if q.locator == "page:2")
observed = tuple(q for q in pref.basis.quotes if q.locator == "page:1")
for label, quotes in (("talk-only basis", talk), ("observed basis", observed)):
    p = pref.model_copy(update={"basis": pref.basis.model_copy(update={"quotes": quotes}), "confidence": "High"})
    sub = inputs.submission.model_copy(update={"preference": p})
    r = compute(dataclasses.replace(inputs, submission=sub))
    print(label, "-> issues:", r.issues)
    if r.report:
        t34 = {f.field: f.text for f in r.report.facts if f.table_id == "T3.4"}
        print("   T3.4 confidence:", t34.get("confidence"),
              "| 'indicative talk only' limitation:", any("indicative talk only" in l for l in r.report.limitations))
