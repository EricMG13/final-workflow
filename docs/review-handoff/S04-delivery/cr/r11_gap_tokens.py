import json, hashlib
from deploy_workflow.handoff_delivery import HandoffInput, ModelDelivery
from deploy_workflow.model_handoff_delivery import _AnnualReader
raw = b"### T4.10 dashboard\n| Metric | FY2024 |\n|---|---|\n| Revenue | Not supplied: undisclosed |\n| Cash | Not calculable: missing inputs |\n| Capex | \xe2\x80\x94 |\n"
spec = HandoffInput.model_validate_json(json.dumps({"path": "a.md", "sha256": hashlib.sha256(raw).hexdigest()}))
layout = ModelDelivery.model_validate_json(json.dumps({"periods": {"FY2024": {"start_date": "2024-01-01", "end_date": "2024-12-31", "balance_column": None}},
  "anchors": {"dashboard": "### T4.10 dashboard"}, "rows": {"revenue": {"table": "dashboard", "label": "Revenue"}, "cash": {"table": "dashboard", "label": "Cash"}, "capex_signed": {"table": "dashboard", "label": "Capex"}}}))
r = _AnnualReader(raw, spec, layout)
for key in ("capex_signed", "revenue", "cash"):
    try: c = r.read(key, "FY2024"); print(key, "->", c.value, c.reason)
    except ValueError as e: print(key, "-> ValueError:", e)
