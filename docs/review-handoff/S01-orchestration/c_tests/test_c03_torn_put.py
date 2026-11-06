"""C03: workflow._put is not atomic; a torn response.md is taken as the retained answer on resume."""
import json
from tests.test_cpos_handoffs import RESPONSES, job, checked  # noqa: F401
from deploy_workflow.owners.cpos import HandoffPlan, HandoffTask, _handoff, _sha


def _task(tmp_path):
    run = HandoffPlan.model_validate_json(job(tmp_path).read_bytes()).run
    return HandoffTask(run, "CP-0", b"instr", {}, {}, 1, ())


def test_torn_response_accepted_as_complete(tmp_path):
    task = _task(tmp_path)
    full = RESPONSES["CP-0"]
    state = tmp_path / "state"
    # First run: kill the process while _put is writing the paid response.
    import deploy_workflow.owners.cpos as cpos
    real_put = cpos._put

    class Kill(BaseException):
        pass

    def torn_put(path, raw):
        if path.name.endswith(".response.md"):
            path.parent.mkdir(parents=True, exist_ok=True)
            cut = full.rindex(b"## Next module") + len(b"## Next module\n")
            path.write_bytes(raw[:cut])  # partial bytes on disk, then the kill
            raise Kill()
        real_put(path, raw)

    cpos._put = torn_put
    try:
        _handoff(task, state, lambda t: full, lambda t, r: (), 1)
    except Kill:
        pass
    finally:
        cpos._put = real_put
    calls = []
    out, path = _handoff(task, state, lambda t: calls.append(1) or full, lambda t, r: (), 1)
    print("executor called on resume:", bool(calls))
    print("full len", len(full), "accepted len", len(out), "equal:", out == full)
    assert out != full  # the truncated bytes were accepted as the module's handoff
