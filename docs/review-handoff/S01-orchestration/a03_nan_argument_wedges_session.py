"""Attack: a JSON-lines participant sends a NaN tool argument (json.loads accepts the NaN literal).
host._json_arguments accepts float('nan'); the session records the call, then workflow._parse
(allow_nan=False) fails, so the workflow never records it -> every later call and the submission
are refused identity_mismatch for the rest of the step."""
import sys, json
from io import StringIO
from pathlib import Path
sys.path.insert(0, "/workspace/final-workflow/tests")
from test_source_workflow import make_pack
from deploy_workflow import workflow as wf
S = Path(sys.argv[1]); d = S / "work" / "a03"
import shutil; shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
w = wf.SourceWorkflow.create(d / "exec", make_pack())
lines = [
    '{"operation":"invoke","tool":"search_pack","arguments":{"query":"Northbridge","source_id":"identity","limit":NaN}}',
    '{"operation":"invoke","tool":"search_pack","arguments":{"query":"Northbridge","source_id":"identity"}}',
    '{"operation":"submit_review","payload":"{}"}',
]
out = StringIO()
wf.serve_json_lines(w, StringIO("\n".join(lines) + "\n"), out, destination=d / "r.json", participant="t")
for line in out.getvalue().splitlines():
    print(line)
