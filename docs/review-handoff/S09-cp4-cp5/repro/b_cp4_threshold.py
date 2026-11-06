"""CP-4 validator attacks: direction wording outside the regex, step-down schedules cut to one
step, and a threshold quoted from a different legal document than document_id."""
import copy, hashlib, json, sys
from dataclasses import replace
sys.path.insert(0, "tests")
import test_method_cp4 as t
from deploy_vii import cp4_legal
from deploy_vii.contracts import Source, Span
from deploy_workflow.owners import cp4

ORIG = ("The Borrower shall maintain the ratio of Covenant Net Debt to Covenant EBITDA at not more "
        "than 4.00x, tested at every calendar quarter end from December 31, 2025.")

def pack_with(new_sentence, extra_source=None):
    pack = t.make_pack("positive")
    sources = []
    for s in pack.sources:
        if s.source_id == "legal-covenants":
            spans = tuple(sp.model_copy(update={"text": sp.text.replace(ORIG, new_sentence)}) if sp.locator == "page:2" else sp for sp in s.spans)
            s = s.model_copy(update={"spans": spans})
        sources.append(s)
    if extra_source:
        sources.append(extra_source)
    return pack.model_copy(update={"sources": tuple(sources)})

def run(label, new_sentence, threshold_text, value, comparison, extra=None, extra_quote=None):
    pack = pack_with(new_sentence, extra)
    up = t.make_upstream("positive")
    if extra is not None:
        up = replace(up, authority={**up.authority, extra.source_id: "executed"},
                     legal_sources=(*up.legal_sources, extra.source_id))
    raw = copy.deepcopy(t.SUBMISSIONS["positive"]["legal_covenants"])
    cov = raw["covenants"][0]
    cov["citations"][2]["quote"] = new_sentence
    if extra_quote:
        cov["citations"].append(extra_quote)
    cov.update(threshold_text=threshold_text, threshold_value=value, comparison=comparison)
    text = json.dumps(raw).replace(t.FIG, t.select_metric(pack, up))
    sub = cp4_legal.CovenantInterpretationSubmission.model_validate_json(text)
    res = cp4.compute(cp4.Cp4Inputs(pack=pack, submission=sub, upstream=up, inputs=t.make_inputs("positive", pack)))
    print(f"--- {label}")
    if res.issues:
        print("REFUSED:", res.issues); return
    facts = {f.fact_id: f for f in res.report.facts}
    for fid in ("T4.9.r01.threshold", "T4.9.r01.comparison", "T4.9.r01.current", "T4.9.r01.headroom", *[k for k in facts if k.startswith("T4.9.r01.test")]):
        f = facts.get(fid)
        print(fid, "=", f.text if f and f.text is not None else (f.amount if f else None))

# A1: floor/cap wording the regex does not know; metric 1.00x vs a 0.75x cap -> breach.
run("A1 'no greater than 0.75x' accepted with >=",
    "The Borrower shall keep the ratio of Covenant Net Debt to Covenant EBITDA no greater than 0.75x, tested at every calendar quarter end from December 31, 2025.",
    "0.75x", "0.75", ">=")
# A1 control: the regex-known wording is refused.
run("A1 control 'not more than 0.75x' with >=",
    "The Borrower shall maintain the ratio of Covenant Net Debt to Covenant EBITDA at not more than 0.75x, tested at every calendar quarter end from December 31, 2025.",
    "0.75x", "0.75", ">=")
# A2: step-down schedule; model quotes the later, looser step against the Dec 2025 LTM metric.
run("A2 step-down: 0.75x for 2025 test dates, 4.00x thereafter; threshold_text '4.00x'",
    "The Borrower shall maintain the ratio of Covenant Net Debt to Covenant EBITDA at not more than 0.75x for each test date in 2025 and not more than 4.00x for each test date thereafter.",
    "4.00x", "4.00", "<=")
# A3: threshold quoted from another executed document than document_id.
other = Source(source_id="legal-other", name="Other indenture", status="ready", sha256=hashlib.sha256(b"x").hexdigest(),
               spans=(Span(locator="page:1", text="Section 4.09. The Consolidated Leverage Ratio shall not be more than 6.00x."),),
               extraction_status="complete", limitation=None)
run("A3 document_id legal-covenants, threshold from legal-other",
    ORIG.replace("4.00x", "0.75x"), "6.00x", "6.00", "<=", extra=other,
    extra_quote={"source_id": "legal-other", "locator": "page:1", "quote": "Section 4.09. The Consolidated Leverage Ratio shall not be more than 6.00x."})
