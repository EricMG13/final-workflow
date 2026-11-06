"""C06: 'Reusing this directory rechecks retained answers' -- but a recheck whose verdict differs
from the stored review (checker fixed or tightened) dies in _put with identity_mismatch."""
from tests.test_cpos_handoffs import RESPONSES, job  # noqa: F401
from deploy_workflow.owners.cpos import HandoffPlan, HandoffTask, _handoff
from deploy_workflow.workflow import WorkflowError


def test_fixed_checker_cannot_accept_retained_answer(tmp_path):
    run = HandoffPlan.model_validate_json(job(tmp_path).read_bytes()).run
    task = HandoffTask(run, "CP-0", b"instr", {}, {}, 1, ())
    state = tmp_path / "state"
    false_reject = lambda t, r: ("false rejection by a buggy check",)
    try:
        _handoff(task, state, lambda t: RESPONSES["CP-0"], false_reject, 1)
    except ValueError as e:
        print("first run:", str(e)[:60])
    calls = []
    try:
        out = _handoff(task, state, lambda t: calls.append(1) or RESPONSES["CP-0"], lambda t, r: (), 1)
        print("accepted", len(out[0]))
    except WorkflowError as e:
        print("rerun with fixed checker raised WorkflowError:", e, "executor calls:", len(calls))
        raise
