"""CP-2H: a view's evidence need not concern its agency: Brook Credit's view cites only Alder's
register line (and Alder's view cites only the identity/financial source)."""
import sys, json, copy
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp2h as T
from deploy_workflow.owners import cp2h
payload = copy.deepcopy(T.raw_payload("positive"))
for v in payload["views"]:
    print(v["agency"], [ (e["source_id"], e["locator"], e["quote"][:60]) for e in v["evidence"]])
pk = T.pack("positive")
ratings = next(s for s in pk.sources if s.source_id == "ratings")
fin = next(s for s in pk.sources if s.source_id == "financial")
alder_line = "Alder Ratings  Issuer rating  BB  Negative  2025-11-14"
payload["views"][1]["evidence"] = [{"source_id": "ratings", "source_sha256": ratings.sha256, "locator": "page:1", "quote": alder_line}]
span = fin.spans[0]
payload["views"][0]["evidence"] = [{"source_id": "financial", "source_sha256": fin.sha256, "locator": span.locator, "quote": span.text.split("\n")[0]}]
print("issues:", cp2h.validate(T.inputs("positive", payload)))
