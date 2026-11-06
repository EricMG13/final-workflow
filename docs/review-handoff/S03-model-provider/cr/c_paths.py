"""Path scrubbing: prefix replacement without boundary, and session.error text not scrubbed."""
import tempfile
from pathlib import Path
import pytest
from deploy_workflow.model.copilot_adapter import _paths_in, _ABSOLUTE_PATH
from tests.model.test_copilot_adapter import Rig, Emit, wire, request, call

print("_paths_in:", _paths_in("cannot open /home/janet/project/x.js", ["/home/jan"]))
print("full chain:", _ABSOLUTE_PATH.sub("<path>", _paths_in("cannot open /home/janet/project/x.js", ["/home/jan"])))
mp = pytest.MonkeyPatch()
tmp = Path(tempfile.mkdtemp())
rig = Rig(tmp, mp)
msg = r"ENOENT: C:\Users\Jane Doe\AppData\Local\copilot\copilot.js and /home/jane/.copilot/x"
reply = call(rig.make([Emit(wire("session.error", {"errorType": "runtime", "message": msg}))], idle_s=2.0), request())
print("session.error reply:", reply.kind, reply.error_class, "|", reply.message)
rig.released()
mp.undo()
