"""CP-3: the talk-only cap is over all market evidence, not over what the preference cites."""
import dataclasses
import tests.test_method_cp3 as t
from deploy_workflow.owners.cp3 import compute

inputs = t.make_inputs("positive")
print("upstream caps:", __import__("deploy_workflow.owners.cp3", fromlist=["_upstream"])._upstream(inputs).caps)
pref = inputs.submission.preference
talk = [q for q in pref.basis.quotes if q.locator == "page:2"]
basis = pref.basis.model_copy(update={"quotes": tuple(talk)})
for conf in ("High", "Medium"):
    p = pref.model_copy(update={"basis": basis, "confidence": conf})
    sub = inputs.submission.model_copy(update={"preference": p})
    r = compute(dataclasses.replace(inputs, submission=sub))
    print(conf, "issues:", r.issues)
    if r.report:
        t34 = {f.field: f.text for f in r.report.facts if f.table_id == "T3.4"}
        print("  T3.4:", t34.get("confidence"), "| talk limitation present:",
              any("indicative talk only" in l for l in r.report.limitations))
# control: whole submission only talk -> cap applies
ev = tuple(e for e in inputs.submission.market_evidence if e.kind == "indicative_talk")
inst = inputs.submission.instruments[0]
ib = inst.basis.model_copy(update={"quotes": tuple(talk)})
inst2 = inst.model_copy(update={"basis": ib, "market_observation": "Indicative dealer talk is the only market evidence and is not a quotation."})
p = pref.model_copy(update={"basis": basis, "confidence": "High"})
sub = inputs.submission.model_copy(update={"preference": p, "market_evidence": ev, "instruments": (inst2,)})
r = compute(dataclasses.replace(inputs, submission=sub))
print("control (submission talk only, High):", [i for i in r.issues if "capped" in i])
