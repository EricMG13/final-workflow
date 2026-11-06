from deploy_vii.live.submission import STEPS
from deploy_vii.live.tools import _enums
from deploy_vii.live.schema import strict_schema
for sid in ("financials","source_context","business_context","legal_covenants","relative_value","source_readiness"):
    vals = sorted({(n,v) for n,v in _enums(strict_schema(STEPS[sid].schema)) if n in ("status","available","threshold_unit","event_scan","kind","availability","disclosure_status")})
    print(sid, vals)
