"""Native pathway runs never execute the superseded CP-8 decision-ledger post-mortem.

Scope: offline and synthetic. The walks are real ``_run_pathway`` walks over the o2 synthetic
case, cut to a CP-0 -> CP-8 plan, with CP-0 answered by the o2 scripted adapter (the frozen
readiness review, CP-8's judgement varied); no provider is called. A full portfolio_decision walk
reaches CP-8 only after CP-1 and the CP-MODEL publication (minutes, ``RUN_PROMOTION``).
"""

import hashlib
import json
from dataclasses import replace
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import o2_case
import pytest

from deploy_vii.execution import Execution
from deploy_vii.preparation import PreparationRequest, load_pack
from deploy_workflow import run_pathway as rp
from deploy_workflow.model.adapter import recorded_adapter
from deploy_workflow.model.turn import load_arguments
from deploy_workflow.owner_workflow import (
    OWNER_SPECS,
    OwnerRunReceipt,
    OwnerWorkflow,
    verify_owner_run_receipt,
)
from deploy_workflow.run_inputs import CheckedRun, RunOutcome, check_arguments, stage_sources

REFUSAL = (
    "native CP-8 is refused: the decision-ledger post-mortem is superseded; compare prior and "
    "current deliverables with CP-OS run_comparison (deploy_workflow.owners.cpos --compare)"
)
COMMANDED = "READY_WITH_LIMITATIONS"  # CP-0 writes T8 exact_command "Run CP-8"
NOT_COMMANDED = "BLOCKED"  # o2's frozen judgement: CP-0 writes "DO NOT RUN"
# opus-medium bills 4 USD per million input and 20 per million output tokens; o2's test usage is
# 1000 input and 200 output tokens: 0.004 + 0.004 for the one CP-0 call.
CP0_CALL_USD = Decimal("0.008")


class _CutReview(o2_case.ScriptAdapter):
    """The frozen o2 readiness review for a CP-0 -> CP-8 plan: one consumer, CP-8, judged
    ``readiness``. A runnable CP-8 borrows CP-6's located evidence and drops the CP-8 gap."""

    readiness = NOT_COMMANDED

    def _plan(self, step_id: str, reads: list[str]) -> list[tuple[str, dict[str, Any]]]:
        plan = super()._plan(step_id, reads)
        if step_id == "source_readiness":
            name, arguments = plan[-1]
            blocked = self.readiness == NOT_COMMANDED
            donor = "CP-8" if blocked else "CP-6"
            entry = next(c for c in arguments["consumers"] if c["module_id"] == donor)
            arguments = {
                **arguments,
                "pack_sha256": Execution(self._execution).read().pack_sha256,
                "consumers": [{**entry, "module_id": "CP-8", "readiness": self.readiness}],
                "gaps": [
                    g for g in arguments["gaps"] if blocked or g["gap_id"] != "missing-prior-record"
                ],
            }
            plan[-1] = (name, load_arguments(json.dumps(arguments)))
        return plan


def _checked(root: Path) -> tuple[CheckedRun, Path]:
    (root / "check").mkdir(parents=True)
    run_dir = root / "run"
    checked = check_arguments(
        case_id=o2_case.CASE_ID,
        sources=o2_case.case_sources(),
        context=o2_case.CASE / "context.json",
        pathway=o2_case.PATHWAY,
        model=o2_case.MODEL,
        adapter=recorded_adapter(o2_case.MODEL, root / "check"),
        cap_usd=o2_case.CAP,
        run_dir=run_dir,
        run_id=o2_case.RUN_ID,
    )
    run = checked.request.run.model_copy(update={"requested_modules": ("CP-0", "CP-8")})
    cut = PreparationRequest(run=run, sources=checked.request.sources)
    return replace(checked, request=cut), run_dir


def _walk(root: Path, readiness: str) -> tuple[RunOutcome, Path]:
    checked, run_dir = _checked(root)
    stage_sources(checked, run_dir)
    (root / "recordings").mkdir()
    script = _CutReview(
        root / "recordings", ("source_readiness",), run_dir / "execution", o2_case.MODEL
    )
    script.readiness = readiness
    return rp._run_pathway(checked, run_dir, script, o2_case.test_prompt_for), run_dir


def _records(run_dir: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in (run_dir / "calls.jsonl").read_text().splitlines()]


def _tree(run_dir: Path) -> dict[str, str]:
    return {
        str(p.relative_to(run_dir)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(run_dir.rglob("*"))
        if p.is_file()
    }


def test_a_commanded_cp8_stops_the_run_before_its_begin_and_spends_nothing_on_it(
    tmp_path: Path,
) -> None:
    outcome, run_dir = _walk(tmp_path, COMMANDED)
    snapshot = Execution(run_dir / "execution").read()
    cp0 = next(h for h in snapshot.heads if h.module_id == "CP-0")
    assert [(c.row_id, c.text) for c in cp0.commands] == [("CP-8", "Run CP-8")]  # the premise
    # The refusal is raised inside CP-0's submit, so the loop names it in its stop form.
    reason = f"WorkflowError: NativeCp8Refused: {REFUSAL}"
    assert (outcome.outcome, outcome.stopped_reason) == ("stopped", reason)
    body = json.loads((run_dir / "run.json").read_text())
    assert (body["outcome"], body["stopped_reason"]) == ("stopped", reason)
    assert [(a.module_id, a.status) for a in snapshot.attempts] == [("CP-0", "finished")]
    audit = run_dir / "execution" / "owner-run-audit"
    assert len(list((audit / "begins").iterdir())) == 1  # CP-0's; no CP-8 begin, no refusal
    assert not (audit / "refused-begin").exists()
    assert [r["step_id"] for r in _records(run_dir)] == ["source_readiness"]
    assert outcome.spent_usd == CP0_CALL_USD
    assert not (run_dir / "owner-run.json").exists() and not (run_dir / "delivery").exists()


def test_control_the_base_workflow_sends_the_decision_ledger_request(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The same walk on the plain owner workflow begins CP-8 and asks the model for the
    post-mortem: the request the guard removes."""
    monkeypatch.setattr(rp, "_NativeWorkflow", OwnerWorkflow)
    outcome, run_dir = _walk(tmp_path, COMMANDED)
    snapshot = Execution(run_dir / "execution").read()
    assert ("CP-8", "pending") in [(a.module_id, a.status) for a in snapshot.attempts]
    assert [r["step_id"] for r in _records(run_dir)] == ["source_readiness", "decision_ledger"]
    assert outcome.spent_usd > CP0_CALL_USD


def test_a_do_not_run_cp8_keeps_its_retained_refusal_and_the_run_finishes(
    tmp_path: Path,
) -> None:
    """CP-0 assesses every planned consumer, so it always writes a CP-8 command row; o2's frozen
    BLOCKED judgement writes ``DO NOT RUN``. That CP-8 never begins: the walk ends, the receipt
    is written and verifies, and the run stops at the renderer as o2's full walk does."""
    outcome, run_dir = _walk(tmp_path, NOT_COMMANDED)
    heads = Execution(run_dir / "execution").read().heads
    cp0 = next(h for h in heads if h.module_id == "CP-0")
    assert [(c.row_id, c.text) for c in cp0.commands] == [("CP-8", "DO NOT RUN")]
    assert (outcome.outcome, outcome.stopped_reason) == ("stopped", "render: owner_render_scope")
    receipt = OwnerRunReceipt.model_validate_json((run_dir / "owner-run.json").read_text())
    verify_owner_run_receipt(Execution(run_dir / "execution"), receipt, publication_directory=None)
    assert [(r.module_id, r.reason) for r in receipt.refusals] == [
        ("CP-8", "CP-0 has not authorized this consumer's source readiness")
    ]
    assert [h.module_id for h in receipt.heads] == ["CP-0"]
    assert [r["step_id"] for r in _records(run_dir)] == ["source_readiness"]


def test_reopening_the_refused_run_refuses_again_and_writes_nothing(tmp_path: Path) -> None:
    """CP-0 settled and CP-8 never begun (as a run killed there would be): reopening continues
    the walk into CP-8's begin, which is refused; the run's stop reason names it."""
    _, run_dir = _walk(tmp_path, COMMANDED)
    before = _tree(run_dir)
    with pytest.raises(rp.NativeCp8Refused):
        rp._NativeWorkflow.open(run_dir / "execution", publication_directory=None)
    pack = load_pack(run_dir / "pack")
    checked, _ = _checked(tmp_path / "again")
    fault = rp._opened(checked, run_dir, pack, True, rp.Redactor())
    assert isinstance(fault, rp._Fault) and fault.reason == f"workflow: {REFUSAL}"
    assert _tree(run_dir) == before


def test_a_cp8_attempt_an_earlier_run_left_pending_is_not_resumed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    with monkeypatch.context() as patched:  # an unguarded run leaves CP-8 pending
        patched.setattr(rp, "_NativeWorkflow", OwnerWorkflow)
        _, run_dir = _walk(tmp_path, COMMANDED)
    before = _tree(run_dir)
    with pytest.raises(rp.NativeCp8Refused):
        rp._NativeWorkflow.open(run_dir / "execution", publication_directory=None)
    assert _tree(run_dir) == before
    control = OwnerWorkflow.open(run_dir / "execution", publication_directory=None)
    assert (control.binding.module_id, control.binding.step_id) == ("CP-8", "decision_ledger")


@pytest.mark.parametrize("module", ["CP-0", "CP-1", "CP-3", "CP-5", "CP-6", "CP-L10"])
def test_other_modules_go_straight_to_the_base_begin(
    monkeypatch: pytest.MonkeyPatch, module: str
) -> None:
    calls: list[str] = []
    monkeypatch.setattr(OwnerWorkflow, "_begin", lambda self, m: calls.append(m) or True)
    workflow = object.__new__(rp._NativeWorkflow)
    workflow._store = SimpleNamespace(read=None)  # type: ignore[attr-defined]  # never read
    assert workflow._begin(module) is True
    assert calls == [module]


def test_the_refusal_is_a_named_fault_the_run_records_as_stopped() -> None:
    assert isinstance(rp.NativeCp8Refused(), rp._FAULTS)
    text = rp._fault_reason(rp.NativeCp8Refused(), rp.Redactor())
    assert text == f"NativeCp8Refused: {REFUSAL}"  # raised outside a tool call (from publish)


def test_fresh_and_resumed_native_runs_both_use_the_guarded_workflow(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    made: list[type] = []
    monkeypatch.setattr(
        OwnerWorkflow, "create", classmethod(lambda cls, *a, **k: made.append(cls) or cls)
    )
    monkeypatch.setattr(
        OwnerWorkflow, "open", classmethod(lambda cls, *a, **k: made.append(cls) or cls)
    )
    rp._enter(tmp_path, None, False)  # type: ignore[arg-type]
    rp._enter(tmp_path, None, True)  # type: ignore[arg-type]
    assert made == [rp._NativeWorkflow, rp._NativeWorkflow]


def test_the_registered_spec_and_the_comparison_route_stay_separate() -> None:
    from deploy_workflow.owners import cpos

    assert OWNER_SPECS["CP-8"].steps[0].step_id == "decision_ledger"  # kept for old receipts
    assert callable(cpos.run_comparison)
    assert "_NativeWorkflow" not in vars(cpos) and "OwnerWorkflow" not in vars(cpos)
