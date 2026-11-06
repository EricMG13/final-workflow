"""CP-3 (relative value engine) adversarial repros through deploy_workflow.owners.cp3.compute."""
import copy, json, sys
sys.path.insert(0, "tests")
import test_method_cp3 as m3
import test_cp3_context_evidence as cx
from deploy_vii.contracts import Fact, Input
from deploy_vii.cp3_relative_value import RelativeValueSubmission
from deploy_workflow.owners.cp3 import compute

def show(label, inputs):
    res = compute(inputs)
    print(f"== {label}: issues={list(res.issues)}")
    if res.report:
        t33 = next(t for t in res.report.tables if t.table_id == "T3.3")
        facts = {f.fact_id: f for f in res.report.facts}
        for row in t33.rows:
            print("   T3.3", row.row_id, [facts[i].text for i in row.fact_ids][:4])
        t31 = next(t for t in res.report.tables if t.table_id == "T3.1")
        for row in t31.rows:
            print("   T3.1", row.row_id, row.label, "| basis:", facts[row.fact_ids[3]].text)
        t34 = next(t for t in res.report.tables if t.table_id == "T3.4")
        print("   T3.4 confidence:", facts[t34.rows[0].fact_ids[2]].text)
    return res

base = m3.SUBMISSIONS["positive"]["relative_value"]
show("baseline R3 positive", m3.make_inputs("positive"))

# A: model-written market_evidence.as_of is never checked against the quote or the run as-of
lit = copy.deepcopy(base)
lit["market_evidence"][0]["as_of"] = "January 9, 2031"
show("A as_of after run as-of (quote says January 9, 2026)", m3.make_inputs("positive", lit))
lit = copy.deepcopy(base)
lit["market_evidence"][0]["as_of"] = "the close"
show("A2 as_of not a date at all", m3.make_inputs("positive", lit))

# B: talk sentence sub-span quoted as observed: TALK_MARKERS checked only inside the quote
lit = copy.deepcopy(base)
sub = "the Northbridge Term Loan as around 99.75"
lit["market_evidence"][1]["kind"] = "observed"
lit["market_evidence"][1]["quote"]["quote"] = sub
lit["market_evidence"][1]["limitation"] = None
for row in (*lit["instruments"], lit["preference"]):
    for q in row["basis"]["quotes"]:
        if q["locator"] == "page:2":
            q["quote"] = sub
lit["market_evidence"] = [lit["market_evidence"][1]]
for row in (*lit["instruments"], lit["preference"]):
    row["basis"]["quotes"] = [q for q in row["basis"]["quotes"] if q["locator"] == "page:2"]
show("B dealer-talk sentence (page:2, 'This is talk') submitted as observed", m3.make_inputs("positive", lit))

# C: context row of facility notes-2031 cited as the market basis of term-loan
pack = cx.pack_for("observed-and-talk", cx.context_source("observed-and-talk",
        cx.context_bytes("observed-and-talk").replace(b'"facility_id": "term-loan"', b'"facility_id": "notes-2031"')))
lit = copy.deepcopy(cx.SUBS["cases"]["observed-and-talk"])
inputs = cx.inputs_for("observed-and-talk", pack, lit)
extra = tuple(Fact(fact_id=f"T4.18.notes-2031.fy2025.{f}", label=f, table_id="T4.18",
                   row_id="notes-2031.fy2025", field=f, text=t)
              for f, t in (("facility_id", "notes-2031"), ("facility_name", "Northbridge Notes 2031")))
cp1 = inputs.cp1.model_copy(update={"facts": (*inputs.cp1.facts, *extra)})
bound = tuple(Input(input_id=i.input_id, sha256=cp1.content_hash(), status=i.status) if i.input_id == "CP-1" else i
              for i in inputs.bound)
lit2 = copy.deepcopy(lit)
inst2 = copy.deepcopy(lit2["instruments"][0])
inst2.update(facility_id="notes-2031", market_observation="none",
             basis={"cp2_refs": ["T2.11.r01"], "quotes": [], "context_rows": []}, limitation=None)
lit2["instruments"].append(inst2)
lit2["preference"]["ordering"] = ["term-loan", "notes-2031"]
sub = RelativeValueSubmission.model_validate_json(m3._instantiate(lit2))
import dataclasses
inputs = dataclasses.replace(inputs, cp1=cp1, bound=bound, current=bound, submission=sub)
res = show("C term-loan market_observation cites context rows c01/c02 that quote notes-2031", inputs)
