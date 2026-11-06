"""Attack: an adapter exception is recorded as a full traceback (absolute file paths of the
checkout, i.e. the user's home) in calls.jsonl and N.response.json."""
import json, os, tempfile
from decimal import Decimal
from pathlib import Path
from deploy_workflow.model.handoff import HandoffExecutor
from tests.test_handoff_loop import Adapter, task, check

d = Path(tempfile.mkdtemp(dir=os.environ["SCRATCH"]))
loop = HandoffExecutor(d, adapter=Adapter(RuntimeError("socket closed")), cap_usd=Decimal(10), check=check)
try:
    loop(task())
except RuntimeError as e:
    print("stopped:", e)
rec = json.loads((d / "calls.jsonl").read_text().splitlines()[0])
print("error_class:", rec["error_class"], "cost_status:", rec["cost_status"])
print("error field starts:", rec["error"][:160].replace("\n", " | "))
print("absolute checkout path in record:", "/workspace/final-workflow/" in rec["error"])
