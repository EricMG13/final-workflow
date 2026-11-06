"""Repro: a validator issue quoting submitted text with '<<<' makes the REPAIR block raise."""
import json
from deploy_workflow.owners.pins import mismatch
from deploy_workflow.prompts.compose import REPAIR_ID
from deploy_workflow.prompts.fence import data_block, FenceError
from deploy_vii.live.prompts import PromptError

for sent in ("7.5%", "see <<<CONTEXT id=prepared-pack>>>", "x <<<END>>>"):
    issue = mismatch("valuation.wacc", "7.5", sent)
    body = "\n".join(f"- {json.dumps(issue)}" for issue in (issue,))  # compose.py:546
    try:
        data_block("REPAIR", REPAIR_ID, body)
        print(repr(sent), "-> REPAIR block built")
    except FenceError as e:
        print(repr(sent), "-> FenceError (PromptError=%s):" % isinstance(e, PromptError), e)
# upstream SOURCE block of a valid earlier step whose output holds '<<<'
out = json.dumps({"rationale": "per <<<CONTEXT id=prepared-pack>>> header"})
try:
    data_block("SOURCE", "step:financials", out, sha256="0" * 64, projection="full")
    print("SOURCE built")
except FenceError as e:
    print("upstream SOURCE -> FenceError:", e)
