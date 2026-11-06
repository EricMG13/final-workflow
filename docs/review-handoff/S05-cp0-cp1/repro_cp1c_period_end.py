"""A04: CP-1C peer table: a peer period end after the run as-of date (and years before the
issuer's LTM period) is read, included and enters the medians with no issue or limitation."""
import sys
sys.path.insert(0, "tests")
import hashlib
from deploy_vii.contracts import Source, Span
from deploy_workflow.owners import cp1c
import test_method_cp1c as T

base = T.inputs("positive")
peers = next(s for s in base.sources if s.source_id == "peers")
p1 = peers.spans[0].text
p1 = p1.replace("Alder Ridge Holdings  2025-12-31", "Alder Ridge Holdings  2027-12-31")
p1 = p1.replace("Brookmere Industries  2025-12-31", "Brookmere Industries  2012-12-31")
texts = [p1, peers.spans[1].text]
sha = hashlib.sha256("\f".join(texts).encode()).hexdigest()
new = peers.model_copy(update={"sha256": sha, "spans": (Span(locator="page:1", text=p1), peers.spans[1])})
srcs = tuple(new if s.source_id == "peers" else s for s in base.sources)
import json, copy
body = copy.deepcopy(T.submissions()["positive"]["peer_benchmark"])
def fix(c):
    if c["source_id"] == "peers": c["source_sha256"] = sha
for a in body["assessments"]:
    for c in a["evidence"]: fix(c)
for c in body["overall"]["evidence"]: fix(c)
# Keep quotes valid: replace the changed dates in quotes too
s = json.dumps(body).replace("Alder Ridge Holdings  2025-12-31", "Alder Ridge Holdings  2027-12-31").replace("Brookmere Industries  2025-12-31", "Brookmere Industries  2012-12-31")
inputs = cp1c.PeerBenchmarkInputs(issuer_name=base.issuer_name, sources=srcs,
    cp1_metrics=base.cp1_metrics, submission=cp1c.PeerBenchmarkSubmission.model_validate_json(s))
issues = cp1c.calculation_issues(inputs)
print("issues:", issues)
if not issues:
    r = cp1c.compute(inputs)
    f = {x.fact.fact_id: x.fact for x in r.facts}
    print("p01 period_end", f["T1C.1.p01.period_end"].text, "included", f["T1C.1.p01.included"].text)
    print("p02 period_end", f["T1C.1.p02.period_end"].text, "included", f["T1C.1.p02.included"].text)
    print("median leverage n", f["T1C.4.total_leverage_adjusted.n"].amount)
    print("limitations mention period?", [l for l in r.limitations if "2027" in l or "2012" in l or "period" in l.lower()])
