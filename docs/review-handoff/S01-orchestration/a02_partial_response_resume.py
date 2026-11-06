"""Attack: a response write that fails midway (ENOSPC / kill) leaves a partial N.response.md;
resume treats those bytes as the complete retained answer and never calls the executor."""
import hashlib, json, shutil, sys
from pathlib import Path
import deploy_workflow.owners.cpos as cpos
from deploy_workflow import workflow as wf

ROOT = Path("/workspace/final-workflow")
S = Path(sys.argv[1]); w = S / "work" / "a02"; shutil.rmtree(w, ignore_errors=True); w.mkdir(parents=True)
ORDER = ["CP-0", "CP-1", "CP-1A", "CP-2"]
RESP = {"CP-0": (ROOT/"runs/tdg-001/CP-0.md").read_bytes(),
        "CP-1": (ROOT/"runs/tdg-002/CP-1-attempt-2.md").read_bytes(),
        "CP-1A": (ROOT/"runs/tdg-002/CP-1A-attempt-3.md").read_bytes(),
        "CP-2": (ROOT/"runs/tdg-002/CP-2-attempt-2.md").read_bytes()}
m = json.loads((ROOT/"runs/tdg-002/snapshot-inputs.json").read_text()); m.pop("handoffs")
m.update(execution="synthetic", sources={}, instructions={})
(w/"source").write_bytes(b"synthetic source")
m["sources"]["source"] = {"path": "source", "sha256": hashlib.sha256(b"synthetic source").hexdigest()}
for mod in ORDER:
    raw = f"instr {mod}".encode(); (w/f"{mod}.md").write_bytes(raw)
    m["instructions"][mod] = {"path": f"{mod}.md", "sha256": hashlib.sha256(raw).hexdigest()}
man = w/"workflow.json"; man.write_text(json.dumps(m))
state = w/"state"
calls = []
def execute(task):
    calls.append(task.module_id); return RESP[task.module_id]
def check(task, raw):  # an analytical checker that accepts the real answer; it cannot see truncation of tail content
    return ()
# 1st run: the CP-1A response write fails after half the bytes (disk full)
real_put = wf._put
def failing_put(path, raw):
    if path.name == "1.response.md" and "CP-1A" in path.parts:
        path.parent.mkdir(parents=True, exist_ok=True)
        cut = raw.rfind(b"## Next module") + len(b"## Next module\n")
        with path.open("xb") as s: s.write(raw[:cut])
        raise OSError(28, "No space left on device")
    return real_put(path, raw)
cpos._put = failing_put
try:
    cpos.run_handoffs(man, state, execute=execute, check=check)
except OSError as e:
    print("first run stopped:", e)
cpos._put = real_put
calls.clear()
report = cpos.run_handoffs(man, state, execute=execute, check=check)
print("resume executor calls:", calls)
kept = next(state.glob("requests/CP-1A/*/1.response.md")).read_bytes()
print("full answer bytes:", len(RESP["CP-1A"]), "retained/delivered bytes:", len(kept))
print("completed records:", [p.name for p in state.glob("completed-*.json")])
print("delivery holds truncated CP-1A:", kept != RESP["CP-1A"])
