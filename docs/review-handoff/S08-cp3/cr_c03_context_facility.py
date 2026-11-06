"""CP-3: a basis may cite a context row for a different facility than the instrument row.
The fixtures have one CP-1 facility, so the context rows are re-tagged to another facility id
(as a second T4.18 facility's quotes would be) by wrapping context_evidence."""
import dataclasses
import deploy_vii.cp3_relative_value as rv
import tests.test_cp3_context_evidence as t
from deploy_workflow.owners.cp3 import compute

orig = rv.context_evidence
def retagged(pack, facilities):
    ev = orig(pack, facilities)
    return dataclasses.replace(ev, rows=tuple(dataclasses.replace(r, facility_id="notes-2031") for r in ev.rows))
rv.context_evidence = retagged

inputs = t.case_inputs("observed-and-talk")
r = compute(inputs)
print("issues:", r.issues)
inst = inputs.submission.instruments[0]
print("instrument facility:", inst.facility_id, "| cites context rows:", inst.basis.context_rows,
      "| those rows' facility:", {row.row_id: row.facility_id for row in rv._bind_evidence(inputs.pack, inputs.submission, rv.Upstream(bound=inputs.bound, current=inputs.current, cp0=inputs.cp0, cp1=inputs.cp1, cp2=inputs.cp2, optional=inputs.optional, inherited=())).context.rows})
if r.report:
    basis = next(f for f in r.report.facts if f.table_id == "T3.1" and f.field == "basis")
    print("T3.1 basis cell:", basis.text)
