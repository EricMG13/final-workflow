"""CP-8 _labelled: the 'first figure after the label' rule binds another measure's figure."""
from deploy_workflow.owners import cp8
q1 = "Total leverage was not reported; interest cover was 6.00x and total leverage 1.80x."
print("leverage=6.00 accepted:", cp8._labelled("total_leverage", "6.00", q1), "| leverage=1.80 accepted:", cp8._labelled("total_leverage", "1.80", q1))
print("cover=6.00 accepted:", cp8._labelled("interest_cover", "6.00", q1))
q2 = "The offer side was indicative only; bid 98.50 and offer 99.25, as of March 2, 2026."
print("offer=98.50 accepted:", cp8._labelled("loan_offer", "98.50", q2), "| offer=99.25 accepted:", cp8._labelled("loan_offer", "99.25", q2))
print("token_once 98.50:", cp8._token_once("98.50", q2))

# End to end: the realized offer bound to the bid figure.
import copy, hashlib, sys
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp8 as t
from deploy_vii.contracts import Span
src = list(t.pack("positive"))
i = next(k for k, s in enumerate(src) if s.source_id == "market_update")
old = "Dealer quotation on April 29, 2026: bid 98.00 and offer 98.75, expressed as a percentage of par."
new = "Dealer quotation on April 29, 2026, offer side indicative: bid 98.00 and offer 98.75, expressed as a percentage of par."
s = src[i]
assert any(old in sp.text for sp in s.spans)
spans = tuple(Span(locator=sp.locator, text=sp.text.replace(old, new)) for sp in s.spans)
src[i] = s.model_copy(update={"spans": spans, "sha256": hashlib.sha256("\f".join(sp.text for sp in spans).encode()).hexdigest()})
lit = copy.deepcopy(t.SUBMISSIONS["positive"])
for o in lit["observations"]:
    if o["side"] == "realized" and o["metric"] in ("loan_bid", "loan_offer"):
        o["quote"]["quote"] = new
        if o["metric"] == "loan_offer":
            o["value_text"] = "98.00"
issues = cp8.validate_ledger(submission=t.submission(lit), upstream=t.upstream("positive"), pack=tuple(src))
print("issues with offer=98.00:", issues)
rep = cp8.decision_ledger(pack=tuple(src), submission=t.submission(lit), upstream=t.upstream("positive"))
for f in rep.facts:
    if f.fact_id.startswith(("T7.3.loan_offer.realized_value", "T7.4.loan_mid")):
        print(f.fact_id, f.amount if f.amount is not None else f.text)
