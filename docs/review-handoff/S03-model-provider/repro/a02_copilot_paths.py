"""Attack: absolute/home paths in a Copilot session.error message reach reply.message and raw,
while the adapter scrubs the same paths from exception text (private_paths, _WINDOWS_PATH)."""
import os, tempfile
from pathlib import Path
import pytest
from tests.model.test_copilot_adapter import Rig, Emit, wire, said, usage, Idle, request, call

class MP:  # minimal monkeypatch stand-in
    def chdir(self, p): os.chdir(p)

tmp = Path(tempfile.mkdtemp(dir=os.environ["SCRATCH"]))
rig = Rig(tmp, MP())
home = "/home/jane.doe"
rig.environ = {**rig.environ, "HOME": home, "USERPROFILE": r"C:\Users\Jane Doe"}
msg = (f"ENOENT: open '{home}/.copilot/config.json' and C:\\Users\\Jane Doe\\AppData\\x.json")
script = [Emit(wire("session.error", {"errorType": "fs", "message": msg, "statusCode": 500}))]
a = rig.make(script)
r = call(a, request())
print("kind", r.kind, r.error_class, r.http_status)
print("message:", r.message)
print("raw has home:", home.encode() in (r.raw or b""), b"Jane Doe" in (r.raw or b""))
# Compare: exception path is scrubbed
class Boom:
    def __init__(self, o): self.o=o
    async def start(self): raise OSError(f"cannot open {home}/.copilot/x and C:\\Users\\Jane Doe\\y.js")
rig2 = Rig(Path(tempfile.mkdtemp(dir=os.environ["SCRATCH"])), MP())
rig2.environ = {**rig2.environ, "HOME": home, "USERPROFILE": r"C:\Users\Jane Doe"}
b = rig2.make([], client_factory=lambda o: Boom(o))
r2 = call(b, request())
print("exception path message:", r2.message)
a.close(); b.close()
