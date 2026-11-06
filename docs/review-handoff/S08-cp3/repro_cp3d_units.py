"""CP-3D: margin quoted in percent read as basis points; reference level in bps read as percent."""
import copy, json, sys
sys.path.insert(0, sys.argv[1])
from repro_cp3d import pages, run, base

pg = pages()
fin5 = pg["financial"]["page:5"]
pg["financial"]["page:5"] = fin5 + "\nThe term loan bears interest at SOFR plus a margin of 3.25% per annum. The SOFR fixing was 430 bps."
raw = copy.deepcopy(base)
raw["terms"]["margin"] = {"quote": {"source_id": "financial", "locator": "page:5",
    "quote": "SOFR plus a margin of 3.25% per annum"}, "bps_text": "3.25", "absence": None}
raw["terms"]["reference_rate"]["level"] = {"quote": {"source_id": "financial", "locator": "page:5",
    "quote": "The SOFR fixing was 430 bps."}, "percent_text": "430"}
raw["terms"]["reference_rate"]["absence"] = None
run("A6 margin 3.25% read as 3.25 bp; SOFR 430 bps read as 430%", pg, raw)
from deploy_workflow.owners import cp3d
sub = cp3d.MarketImpliedSubmission.model_validate_json(json.dumps(raw))
st = cp3d.compose(inputs=cp3d.inputs_from_submission(sub)).stored()
print("   margin_bp", st["margin_bp"], "yield_mid", st["yield_mid"], "dm_mid", st["dm_mid"])
