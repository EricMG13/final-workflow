"""A02: TDR.6 unit/currency/duration are model text, never bound to the cited span; the period
label 'Twelve months to' is written by Python for every figure.
The span is edited (source hash kept, as a held item would carry) to state a quarterly figure in
EUR thousands. Hand expectation: a review issue, or a fact that does not claim USD MILLIONS over
twelve months."""
import copy, sys
sys.path.insert(0, 'tests/research')
from cpdr_peers_support import peers_case
from deploy_workflow.research import peers as p
c = peers_case()
src = []
for s in c.sources:
    if s.source_id == 'ev-1':
        spans = list(s.spans)
        i = next(k for k, sp in enumerate(spans) if sp.locator == 'line:11')
        spans[i] = spans[i].model_copy(update={"text": "Alder Ridge Holdings revenue for the three months to 2025-12-31, EUR thousands: 200.0"})
        s = s.model_copy(update={"spans": tuple(spans)})
    src.append(s)
body = copy.deepcopy(c.body)
pack = c.submission(body).peers
issues = p.peer_issues(pack, c.brief, c.evidence, src)
fact = {f.fact_id: f for f in c.composed(body).facts}["TDR.6.p01.revenue.amount"]
print("issues:", [str(i) for i in issues])
print("fact:", fact.amount, fact.unit, fact.currency, fact.scale, repr(fact.period))
