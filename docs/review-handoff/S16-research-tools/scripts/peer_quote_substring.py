"""A11: TDR.6 amount quote is checked as a substring of the span, not as a whole figure token.
Span line:11 of ev-1 reads 'Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 200.0'.
Hand-derived expectation: the only figure the span states for revenue is 200.0; any other quote
must be an issue or a missing cell."""
import copy, sys
sys.path.insert(0, 'tests/research')
from cpdr_peers_support import peers_case
c = peers_case()
assert c.issues() == ()
for quote in ["20", "0.0", "2025", "-12", "12", "00.0"]:
    body = copy.deepcopy(c.body)
    body["peers"]["figures"][0]["citation"]["quote"] = quote
    issues = c.issues(body)
    fact = {f.fact_id: f for f in c.composed(body).facts}["TDR.6.p01.revenue.amount"]
    print(f"quote={quote!r:8} issues={[str(i) for i in issues]} status={fact.status} amount={fact.amount} unit={fact.unit} period={fact.period!r}")
