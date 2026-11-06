from datetime import date
from deploy_vii.contracts import Run
from deploy_workflow.markdown_delivery import require_issuer
run = Run.model_validate_json('{"run_id":"r","issuer_id":"F","issuer_name":"Ford","as_of":"2024-12-28","case_kind":"public","pathway":"earnings_update","requested_modules":["CP-1B"]}')
lines = ["# CP-1B Stanford Health Care", "## Request", "Analyse Stanford Health Care bonds."]
try:
    require_issuer(run, (), "CP-1B", lines); print("ACCEPTED handoff about Stanford for issuer Ford")
except ValueError as e: print("refused", e)
lines2 = ["# CP-1B Acme Corp", "## Request", "Analyse Acme lab capacity."]
try:
    require_issuer(run.model_copy(update={"issuer_name": "Absolute Lab Inc"}), ("AB",), "CP-1B", lines2); print("ACCEPTED via alias 'AB' substring of 'lab'")
except ValueError as e: print("refused", e)
