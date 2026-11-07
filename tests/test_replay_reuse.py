"""Replay reads the earlier run once: the plan carries the authenticated `_Earlier`."""

from pathlib import Path

import pytest

from deploy_workflow import replay


class _Stop(Exception):
    pass


class _Retained:
    # Hand-derived: replay_module must use this object (its pack check raises _Stop) and must not
    # construct a new _Earlier from the path (which would raise ReplayRefused: nothing there).
    class store:  # noqa: N801 - stand-in for the Execution
        @staticmethod
        def pack(snapshot):
            raise _Stop

    snapshot = None


def test_replay_module_uses_the_plans_retained_read(tmp_path: Path) -> None:
    with pytest.raises(_Stop):
        replay.replay_module(
            None, tmp_path / "gone", "CP-0", execution=tmp_path, retained=_Retained
        )  # type: ignore[arg-type]


def test_replay_module_without_retained_reads_the_directory(tmp_path: Path) -> None:
    with pytest.raises(replay.ReplayRefused):
        replay.replay_module(None, tmp_path / "gone", "CP-0", execution=tmp_path)  # type: ignore[arg-type]


def test_plan_retained_is_not_part_of_equality() -> None:
    a = replay.ReplayPlan(Path("x"), "r", ("CP-0",), ())
    b = replay.ReplayPlan(Path("x"), "r", ("CP-0",), (), (), retained=_Retained)  # type: ignore[arg-type]
    assert a == b and "retained" not in repr(b)
