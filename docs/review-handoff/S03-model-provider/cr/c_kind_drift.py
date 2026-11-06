"""Copilot refusal (ModelMismatch) with a token-less usage event: live kind vs exported/replayed kind."""
import json, tempfile
from decimal import Decimal
from pathlib import Path
import pytest
from tests.model.test_copilot_adapter import Rig, Emit, wire, said, Idle, request, call, SPEC, _run_and_export
from deploy_workflow.model.adapter import recorded_adapter
from deploy_workflow.model.record import CallLog
from deploy_workflow.model.redact import Redactor

mp = pytest.MonkeyPatch()
tmp = Path(tempfile.mkdtemp())
rig = Rig(tmp, mp)
script = [said("x"), Emit(wire("assistant.usage", {"model": "other-model", "finishReason": "stop"})), Idle()]
live = call(rig.make(script, idle_s=2.0), request(), digest="e" * 64)
print("live direct:", live.kind, live.error_class, live.usage, live.billed_usd)
rig.released()
rig2 = Rig(tmp / "b", mp) if (tmp / "b").mkdir() is None else None
adapter = rig2.make(script, idle_s=2.0)
run, exported = _run_and_export(rig2, tmp / "b", adapter)
(rec,) = CallLog(run, Redactor()).records()
print("record:", rec["error_class"], rec["http_status"], rec["cost_status"])
print("exported response kind:", exported["response"]["kind"])
(out := tmp / "b" / "rec").mkdir()
(out / "r.jsonl").write_bytes((tmp / "b" / "out.jsonl").read_bytes())
rep = recorded_adapter(SPEC, out).complete(request(), invocation_digest=exported["invocation_digest"], call_index=exported["call_index"], reservation_id="r")
print("replayed:", rep.kind, rep.error_class)
rig2.released()
mp.undo()
