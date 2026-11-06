import hashlib, sys, traceback, json
from pathlib import Path
from deploy_workflow.handoff_delivery import DeliveryRequest
from deploy_workflow.markdown_delivery import markdown_files, literal_module

HERE = Path(__file__).resolve().parent

def deliver(md: str, blocks, routes, module="CP-1B", pathway="earnings_update", issuer_name="TransDigm Group Incorporated", aliases=(), name="h.md"):
    raw = md.encode()
    p = HERE / name
    p.write_bytes(raw)
    req = DeliveryRequest.model_validate_json(json.dumps({
        "run": {"run_id": "r1", "issuer_id": "TDG", "issuer_name": issuer_name, "as_of": "2024-12-28",
                "case_kind": "public", "pathway": pathway, "requested_modules": [module]},
        "handoffs": {module: {"path": str(p), "sha256": hashlib.sha256(raw).hexdigest()}},
        "layout": {"blocks": list(blocks), "routes": list(routes), "scope": "test scope", "issuer_aliases": list(aliases)},
    }))
    return markdown_files(req, Path("/"))
