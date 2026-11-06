"""CR-C03: cp1b.submit (and cp1c/cp1d.submit) has no resume path when the process dies after the
valid step is retained but before store.finish. Drives cp1b.submit's real control flow on a real
journal; to avoid an 11-26 min CP-1 promotion the module identity/validator are pointed at CP-0's
one-step chain (same Execution.submit_step/finish protocol)."""
import sys, tempfile
from pathlib import Path
sys.path.insert(0, "tests")
import test_source_workflow as sw
from deploy_vii import cp0_workflow
from deploy_vii.contracts import Module
from deploy_vii.execution import Execution
from deploy_workflow.owners import cp1b

cp1b.MODULE_ID, cp1b.STEP_ID, cp1b.STEP_IDS = "CP-0", "source_readiness", ("source_readiness",)
cp1b.normalise = lambda schema, payload: (payload, ())
cp1b._validate_step = cp0_workflow._validate_review
cp1b._candidate = lambda output, attempt: Module.model_validate_json(output)

with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
    pack = sw.make_pack()
    store = Execution.create(Path(d) / "execution", pack)
    ticket = store.begin("CP-0").ticket_id
    payload = sw.readiness(pack)
    real_finish = Execution.finish
    Execution.finish = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("simulated crash"))
    try:
        cp1b.submit(store, ticket, "source_readiness", payload, None)
    except RuntimeError as e:
        print("first submit:", e)
    Execution.finish = real_finish
    att = next(a for a in store.read().attempts if a.ticket_id == ticket)
    print("journal after crash: attempt", att.status, [s.status for s in att.steps])
    try:
        cp1b.submit(store, ticket, "source_readiness", payload, None)
        print("retry settled")
    except ValueError as e:
        print("retry via cp1b.submit pattern RAISES:", e)
    done = cp0_workflow.submit_cp0_review(store, ticket, payload)
    print("submit_cp0_review on the same journal resumes:", done.status, done.issues)
