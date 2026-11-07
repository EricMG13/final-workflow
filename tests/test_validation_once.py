"""The repeated-validation theme (S07-cp2-gh-C01 and its duplicates S07-cp2-gh-C02, S06-cp2-ade-C06,
S08-cp3-C10, S10-cp6-cp8-cpl10-C05): one `_validate_step` validates a submission once and composes
it once; the public composers keep their own guard.

Each count is a function that runs once per validation pass or once per composition. A full submit
runs `_validate_step` twice by design (the journal's step validation, then the trusted re-check
before settlement), so the expected counts below are 2 per submit: one validation and one
composition per `_validate_step`. Before the change they were 6 content checks (CP-2G), 6
validation passes and 8 composes (CP-2H), 6 (CP-2A), 6 (CP-2D), 2 per step (CP-2, CP-3, CP-6).
"""

import json
from collections import Counter
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest
import test_connect_cp2g as tc2g
import test_connect_cp2h as tc2h

from deploy_workflow.owners import cp2g, cp2h


def _count(monkeypatch: pytest.MonkeyPatch, module: Any, *names: str) -> Counter[str]:
    calls: Counter[str] = Counter()
    for name in names:
        original = getattr(module, name)

        def counted(*args: Any, __name: str = name, __f: Any = original, **kwargs: Any) -> Any:
            calls[__name] += 1
            return __f(*args, **kwargs)

        monkeypatch.setattr(module, name, counted)
    return calls


@pytest.fixture
def cp2g_seeded(tmp_path: Path) -> Iterator[tuple[Any, Any, Any]]:
    yield tc2g._case_seed(tmp_path, "positive")


def test_cp2g_submit_checks_content_once_per_step(
    cp2g_seeded: tuple[Any, Any, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    store, _, attempt = cp2g_seeded
    calls = _count(monkeypatch, cp2g, "content_issues", "_resolve", "_validate_step")
    tc2g._submit(store, attempt, json.dumps(tc2g._payload("positive")))
    finished = next(a for a in store.read().attempts if a.ticket_id == attempt.ticket_id)
    assert finished.status == "finished" and finished.issues == ()
    # two steps (journal + trusted re-check), one content check and one forecast each
    assert calls == Counter({"_validate_step": 2, "content_issues": 2, "_resolve": 2})


def test_cp2g_public_guards_still_refuse(cp2g_seeded: tuple[Any, Any, Any]) -> None:
    store, pack, attempt = cp2g_seeded
    payload = tc2g._payload("positive")
    payload["assessment"]["confidence"] = "High"  # HIGH_ISSUE, a content issue
    submission = cp2g.ForwardSubmission.model_validate_json(json.dumps(payload))
    upstream = cp2g.cp2g_upstream(store=store, attempt=attempt)
    assert cp2g.validate_forward(pack=pack, submission=submission, upstream=upstream) == (
        cp2g.HIGH_ISSUE,
    )
    with pytest.raises(ValueError, match="High is not allowed"):
        cp2g.forward_model(pack=pack, submission=submission, upstream=upstream)
    with pytest.raises(ValueError, match="CP-2G submission has issues"):
        cp2g.compute(cp2g._inputs(pack, submission, upstream))


def test_cp2h_submit_parses_the_register_once_and_validates_once_per_step(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    store, _, attempt = tc2h.seed(tmp_path, "positive")
    payload = tc2h._submission(store, "positive").model_dump_json()
    calls = _count(monkeypatch, cp2h, "register_source", "_compose", "_view_issues", "select_cp1")
    tc2h._submit(store, attempt, payload)
    finished = next(a for a in store.read().attempts if a.ticket_id == attempt.ticket_id)
    assert finished.status == "finished" and finished.issues == ()
    # per step: one register read, one validation pass, and two composes (the validation book
    # without the analyst tables, then the submission's book); was 8, 6 and 8 per submit
    assert (calls["register_source"], calls["_view_issues"], calls["_compose"]) == (2, 2, 4)
    # the CP-1 ratios are selected once per compose, not once per trigger (was 66 per submit)
    assert calls["select_cp1"] <= 18


def test_cp2h_public_guards_still_refuse(tmp_path: Path) -> None:
    store, pack, attempt = tc2h.seed(tmp_path, "positive")
    good = tc2h._submission(store, "positive")
    overall = good.overall.model_copy(update={"confidence": "High"})
    submission = good.model_copy(update={"overall": overall})
    upstream = cp2h.cp2h_upstream(store=store, attempt=attempt)
    issues = cp2h.validate_triggers(pack=pack, submission=submission, upstream=upstream)
    assert issues and all("High" in i for i in issues)
    with pytest.raises(ValueError, match="High is not allowed"):
        cp2h.rating_triggers(pack=pack, submission=submission, upstream=upstream)
    with pytest.raises(ValueError, match="High is not allowed"):
        cp2h.compute(cp2h._inputs(pack, submission, upstream))
