"""C01: a run started with through= that is killed is resumed with no through: the resume walk
has no stop point (cap.json does not record through, run_pathway refuses through+resume)."""
import json
import pytest
from deploy_workflow.model.budget import Budget
from tests.test_run_pathway import args, no_network  # noqa: F401 (fixtures)
from tests.test_run_pathway import Kill, kill_at_reserve, read_s1, scripted_complete, run_pathway, rp


def test_resume_of_a_through_run_drops_through(args, monkeypatch):
    scripted_complete(monkeypatch, [read_s1()])
    real = Budget.reserve
    kill_at_reserve(monkeypatch, 2)
    with pytest.raises(Kill):
        run_pathway(**args, through="CP-0")          # user asked to stop after CP-0
    monkeypatch.setattr(Budget, "reserve", real)
    run_dir = args["run_dir"]
    print("cap.json:", json.loads((run_dir / "cap.json").read_text()))
    with pytest.raises(rp.UnknownThrough):
        run_pathway(**args, through="CP-0", resume=True)  # cannot restate it
    seen = {}
    real_walk = rp._run_pathway

    def spy(*a, **k):
        seen["through"] = k.get("through")
        seen["resume"] = k.get("resume")
        raise Kill()

    monkeypatch.setattr(rp, "_run_pathway", spy)
    with pytest.raises(Kill):
        run_pathway(**args, resume=True)               # the only accepted resume
    print("resume walk kwargs:", seen)
    assert seen == {"through": None, "resume": True}
