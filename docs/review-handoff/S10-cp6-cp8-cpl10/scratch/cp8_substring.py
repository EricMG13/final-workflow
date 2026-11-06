"""CP-8 decision vocabulary: a confidence word accepted as a substring of another word."""
import copy, hashlib, json, sys
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp8 as t
from deploy_vii.contracts import Source, Span
from deploy_workflow.owners import cp8

src = list(t.pack("positive"))
i = next(k for k, s in enumerate(src) if s.source_id == "prior_case")
s = src[i]
old = "Decision: Neutral action bias with Medium confidence on the Northbridge Term Loan."
new = "Decision: Neutral action bias on the Northbridge Term Loan; Highly uncertain, Lower conviction."
spans = tuple(Span(locator=sp.locator, text=sp.text.replace(old, new)) for sp in s.spans)
digest = hashlib.sha256("\f".join(sp.text for sp in spans).encode()).hexdigest()
src[i] = s.model_copy(update={"spans": spans, "sha256": digest})
lit = copy.deepcopy(t.SUBMISSIONS["positive"])
for f in ("action_bias", "confidence", "instrument"):
    lit["decision"][f]["quote"]["quote"] = new
for word in ("High", "Low"):
    lit["decision"]["confidence"]["text"] = word
    issues = cp8.validate_ledger(submission=t.submission(lit), upstream=t.upstream("positive"), pack=tuple(src))
    print(word, "-> decision.* issues:", [x for x in issues if x.startswith("decision")])
lit["decision"]["confidence"]["text"] = "High"
rep = cp8.decision_ledger(pack=tuple(src), submission=t.submission(lit), upstream=t.upstream("positive", ("Neutral", "Medium")))
for f in rep.facts:
    if f.fact_id in ("T7.1.decision.confidence", ) or f.fact_id.startswith("cp8.what_changed.decision"):
        print(f.fact_id, repr(f.text))
