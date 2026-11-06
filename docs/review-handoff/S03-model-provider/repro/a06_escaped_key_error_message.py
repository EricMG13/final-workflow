"""Attack: a non-2xx body whose error is not {"error":{"message":...}} and carries a JSON-escaped
key: reply.message (-> CallRecord.error) keeps the escaped key; json.loads of it restores the key."""
import json, os, tempfile
from datetime import UTC, datetime
from decimal import Decimal
from pathlib import Path
from deploy_workflow.model.adapter import LiveAdapter
from deploy_workflow.model.transport import Response
from deploy_workflow.model.record import CallRecord, CallLog
from deploy_workflow.model.redact import Redactor
from tests.model.test_adapter import SPEC, FAKE_KEY, RULING_TEXT, FakeTransport, complete

S = os.environ["SCRATCH"]
root = Path(tempfile.mkdtemp(dir=S)); (root / "lift.md").write_text(RULING_TEXT)
escaped = FAKE_KEY.replace("-", "\\u002d", 1)
for status, body in [(500, '{"error":"invalid key ' + escaped + '"}'),
                     (401, '{"detail":"invalid key ' + escaped + '"}'),
                     (401, '{"error":{"message":"invalid key ' + escaped + '"}}')]:
    env = {"OPENAI_API_KEY": FAKE_KEY}
    a = LiveAdapter(SPEC, root / "lift.md", FakeTransport(Response(status, body.encode())), env, rulings_root=root)
    r = complete(a)
    decoded = json.loads('"' + (r.message or "") .replace('"', '\\"') + '"') if r.message else ""
    print(status, r.kind, r.error_class, "| message:", r.message, "| key after one JSON decode:", FAKE_KEY in decoded)
    if FAKE_KEY in decoded:
        red = Redactor.from_environ(env)
        rec = CallRecord.build(red, schema_version="model-call/1", run_id="r", case_id="c", pathway="p",
            module_id="m", step_id="s", attempt=0, call_index=0, config_id="sol-medium", provider="openai",
            requested_model="gpt-6.1-sol", reported_model=None, requested_effort="medium",
            invocation_digest="a"*64, request_id=None, http_status=r.http_status,
            started_at=datetime.now(UTC), first_byte_at=None, finished_at=None, input_tokens=None,
            cached_read_tokens=None, cache_write_tokens=None, output_tokens=None, reasoning_tokens=None,
            reserved_usd=Decimal(1), settled_usd=None if r.kind=="sent_unknown" else Decimal(0),
            cost_status="unknown" if r.kind=="sent_unknown" else "computed", tool_calls=(), submit_sha256=None,
            error_class=r.error_class, error=r.message)
        d = Path(tempfile.mkdtemp(dir=S)); CallLog(d, red).append(rec)
        line = (d / "calls.jsonl").read_text()
        print("   record accepted; calls.jsonl error field ->", json.loads(line)["error"])
