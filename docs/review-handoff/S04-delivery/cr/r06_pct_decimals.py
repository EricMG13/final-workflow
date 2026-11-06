import json
from deploy_workflow.handoff_delivery import MarkdownRoute
from deploy_workflow.markdown_delivery import _numeric_observations, literal_module
from deploy_vii.display import format_value
raw = b"# CP-3 TDG\n## Request\nTDG.\n## Sources\nS.\n## Findings\n### Yields\n| Instrument | ytm_fraction | amt |\n|---|---|---|\n| Note A | 0.0725 | 1234.567 |\n## Calculations\nNone.\n## Gaps\nT.\n## Next module\nD.\n"
module, _, _ = literal_module("CP-3", raw)
for col, unit, fid, blk in [("ytm_fraction", "%", "RV.1", "yield-against-maturity"), ("amt", "US$m", "S.3", "metric-strip")]:
    route = MarkdownRoute.model_validate_json(json.dumps({"module_id": "CP-3", "heading": "Yields", "kind": "chart", "block_id": blk,
        "figure_id": fid, "value_columns": [col], "chart_unit": unit}))
    m, _, pts = _numeric_observations(module, module.tables[0], route)
    f = next(x for x in m.facts if x.fact_id == pts[0].fact_id)
    uc = {"%": "percent", "US$m": "amount"}[unit]
    print(col, "token", f.amount, "decimals", f.decimals, "->", format_value(f.amount, uc, "known", decimals=f.decimals))
