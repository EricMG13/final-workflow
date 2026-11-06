"""A05: CP-1C T1C.6 ties the issuer line to CP-1 without comparing periods: an issuer line two
years older than CP-1's LTM column reads 'Reconciled' and the difference carries CP-1's period."""
import sys, json, copy, hashlib
sys.path.insert(0, "tests")
from deploy_vii.contracts import Span
from deploy_workflow.owners import cp1c
import test_method_cp1c as T

base = T.inputs("positive")
peers = next(s for s in base.sources if s.source_id == "peers")
old, new_ = "Northbridge Synthetic Group  2025-12-31", "Northbridge Synthetic Group  2023-12-31"
p1 = peers.spans[0].text.replace(old, new_)
sha = hashlib.sha256("\f".join([p1, peers.spans[1].text]).encode()).hexdigest()
src = peers.model_copy(update={"sha256": sha, "spans": (Span(locator="page:1", text=p1), peers.spans[1])})
srcs = tuple(src if s.source_id == "peers" else s for s in base.sources)
body = json.dumps(T.submissions()["positive"]["peer_benchmark"]).replace(peers.sha256, sha).replace(old, new_)
inputs = cp1c.PeerBenchmarkInputs(issuer_name=base.issuer_name, sources=srcs,
    cp1_metrics=base.cp1_metrics, submission=cp1c.PeerBenchmarkSubmission.model_validate_json(body))
print("issues:", cp1c.calculation_issues(inputs))
f = {x.fact.fact_id: x.fact for x in cp1c.compute(inputs).facts}
for k in ("total_leverage_adjusted", "adjusted_ebitda_margin"):
    print(k, "sheet period:", f[f"T1C.6.{k}.sheet"].period, "| cp1 period:", f[f"T1C.6.{k}.cp1"].period,
          "| diff period:", f[f"T1C.6.{k}.difference"].period, "| result:", f[f"T1C.6.{k}.result"].text)
