"""A tool call the runtime never hands to a handler (name not offered): boundary never reached."""
import tempfile
from pathlib import Path
import pytest
from tests.model.test_copilot_adapter import Rig, Emit, wire, said, usage, Idle, request, call

mp = pytest.MonkeyPatch()
start = Emit(wire("tool.execution_start", {"toolCallId": "c1", "toolName": "read_page", "arguments": {"p": 1}}))
variants = {
    "runtime_silent": [said(""), usage(finishReason="tool_calls", numToolCalls=1), start],
    "runtime_continues": [said(""), usage(finishReason="tool_calls", numToolCalls=1), start,
                          said("sorry"), usage(), Idle()],
}
for name, script in variants.items():
    tmp = Path(tempfile.mkdtemp())
    rig = Rig(tmp, mp)
    reply = call(rig.make(script, idle_s=1.0, overall_s=20.0), request())
    print(name, "->", reply.kind, reply.error_class, reply.message)
    rig.released()
mp.undo()
