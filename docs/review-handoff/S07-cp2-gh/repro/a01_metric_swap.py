"""CP-2G: when CP-2A stressed another base period, the analyst's break metric is unchecked, so a
leverage watch level is tested as interest coverage (and vice versa) with no issue."""
import sys, json, dataclasses
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp2g as T
from deploy_workflow.owners import cp2g
inp = T._inputs("positive")
ctx = inp.context
# CP-2A stressed the fourth quarter (an offered CP-1 period), not the LTM column
cp2a = dataclasses.replace(ctx.cp2a, base_period="Q4 2025: 2025-10-01 to 2025-12-31")
ctx2 = dataclasses.replace(ctx, cp2a=cp2a)
payload = T._bind_all(T._payload("positive"))
payload["break_metrics"] = [
    {"break_id": "b03", "metric": "interest_coverage"},  # CP-2A: total leverage 2.5x
    {"break_id": "b04", "metric": "net_leverage"},
    {"break_id": "b05", "metric": "total_leverage"},     # CP-2A: interest coverage 2.0x
]
sub = cp2g.ForwardSubmission.model_validate_json(json.dumps(payload))
issues = cp2g.content_issues(cp2g.ForwardInputs(ctx2, sub))
print("issues:", issues)
r = cp2g.compute(cp2g.ForwardInputs(ctx2, sub))
cells = {c.fact.fact_id: c.fact for c in r.cells}
for row in ("b03", "b05"):
    print(row, cells[f"T2H.7.{row}.test"].text, "| metric:", cells[f"T2H.7.{row}.metric"].text,
          "| level:", cells[f"T2H.7.{row}.level"].amount,
          "| base:", cells[f"T2H.7.{row}.base_first"].text, "| down:", cells[f"T2H.7.{row}.down_first"].text)
print([l for l in r.own_limitations if "could not be checked" in l])
