"""Native pathway runs never execute the superseded CP-8 decision-ledger post-mortem.

Synthetic stand-ins for the journal: these prove the guard's decisions, not a model run.
"""

from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

from deploy_workflow import run_pathway as rp
from deploy_workflow.owner_workflow import OWNER_SPECS, OwnerWorkflow

POINTER = "CP-OS run_comparison"


def _workflow(commands: list[tuple[str, str]] | None) -> rp._NativeWorkflow:
    """A workflow whose journal holds a CP-0 head with the given (row_id, text) commands,
    or no CP-0 head when ``commands`` is None."""
    heads = (
        []
        if commands is None
        else [
            SimpleNamespace(
                module_id="CP-0",
                commands=[SimpleNamespace(row_id=r, text=t) for r, t in commands],
            )
        ]
    )
    workflow = object.__new__(rp._NativeWorkflow)
    workflow._store = SimpleNamespace(read=lambda: SimpleNamespace(heads=heads))  # type: ignore[attr-defined]
    return workflow


@pytest.fixture
def parent_calls(monkeypatch: pytest.MonkeyPatch) -> list[Any]:
    calls: list[Any] = []
    monkeypatch.setattr(OwnerWorkflow, "_begin", lambda self, m: calls.append(("begin", m)) or True)
    monkeypatch.setattr(
        OwnerWorkflow, "_activate", lambda self, a, s, *, at=None: calls.append(("activate", a))
    )
    return calls


def test_a_commanded_cp8_is_refused_with_the_run_comparison_pointer_and_nothing_begins(
    parent_calls: list[Any], tmp_path: Path
) -> None:
    workflow = _workflow([("CP-8", "Run CP-8")])
    with pytest.raises(rp.NativeCp8Refused) as caught:
        workflow._begin("CP-8")
    assert POINTER in str(caught.value) and "superseded" in str(caught.value)
    assert parent_calls == []  # the journal never saw a begin
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("commands", [None, [], [("CP-5", "Run CP-5")]])
def test_an_uncommanded_cp8_keeps_its_ordinary_refusal_path(
    parent_calls: list[Any], commands: list[tuple[str, str]] | None
) -> None:
    assert _workflow(commands)._begin("CP-8") is True
    assert parent_calls == [("begin", "CP-8")]  # the base begin refuses it by command


@pytest.mark.parametrize("module", ["CP-1", "CP-3", "CP-5", "CP-6", "CP-L10"])
def test_other_modules_begin_as_before_even_when_cp8_is_commanded(
    parent_calls: list[Any], module: str
) -> None:
    assert _workflow([("CP-8", "Run CP-8"), (module, f"Run {module}")])._begin(module)
    assert parent_calls == [("begin", module)]


def test_a_resumed_cp8_attempt_is_refused_other_attempts_resume() -> None:
    cp8, cp5 = SimpleNamespace(module_id="CP-8"), SimpleNamespace(module_id="CP-5")
    workflow = _workflow(None)
    with pytest.raises(rp.NativeCp8Refused):
        workflow._activate(cp8, "decision_ledger")  # type: ignore[arg-type]
    seen: list[Any] = []
    OwnerWorkflow._activate = lambda self, a, s, *, at=None: seen.append(a)  # type: ignore[method-assign]
    try:
        workflow._activate(cp5, "integrity_review")  # type: ignore[arg-type]
    finally:
        del OwnerWorkflow._activate
    assert seen == [cp5]


def test_the_refusal_is_a_named_fault_the_run_records_as_stopped() -> None:
    assert isinstance(rp.NativeCp8Refused(), rp._FAULTS)
    text = rp._fault_reason(rp.NativeCp8Refused(), rp.Redactor())
    assert text.startswith("NativeCp8Refused: native CP-8 is refused") and POINTER in text


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
