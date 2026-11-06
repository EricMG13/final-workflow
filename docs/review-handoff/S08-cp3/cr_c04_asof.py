"""CP-3: MarketEvidence.as_of is free model text, never checked against the quote or run.as_of."""
import dataclasses
import tests.test_method_cp3 as t
from deploy_workflow.owners.cp3 import compute

inputs = t.make_inputs("positive")
print("run as_of:", inputs.pack.run.as_of)
for as_of in ("January 9, 2031", "the close", "March 1, 2019"):
    ev = list(inputs.submission.market_evidence)
    ev[0] = ev[0].model_copy(update={"as_of": as_of})
    sub = inputs.submission.model_copy(update={"market_evidence": tuple(ev)})
    r = compute(dataclasses.replace(inputs, submission=sub))
    shown = None
    if r.report:
        shown = {f.field: f.text for f in r.report.facts if f.table_id == "T3.3" and f.row_id == "m01"}
    print(repr(as_of), "issues:", r.issues, "| T3.3 m01:", shown and (shown.get("kind"), shown.get("as_of")),
          "| stale limitation:", r.report and any("tale" in l for l in r.report.limitations))
