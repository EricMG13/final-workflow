"""S09-A04 remainder: CP-4C selects CP-1's secured facility by its T4.18 secured status, not by
the id `term-loan`. Exactly one secured facility at the quarter period is that one; none or more
than one is an issue naming the count (a repairable validator issue and an empty view, never a
raise). Expected values are hand-derived from the rows each test writes.

Base rows (cp1_facts): at q4-2025 the row `term-loan` is SECURED and SENIOR; q3-2025 holds an
UNSECURED row; a FY alias row at fy-2025 is SECURED. T4.14 states q3-2025, q4-2025 and fy-2025,
so the quarter period is q4-2025 (the alias ends the same day).
"""

import importlib
from pathlib import Path
from typing import Any

import pytest

from deploy_vii.contracts import Fact
from deploy_workflow.owners import cp4c

conn: Any = importlib.import_module("test_connect_cp4c")
stage1: Any = importlib.import_module("test_method_cp4c")

Q4 = "q4-2025"


def _row(row: str, facility: str, secured: str, seniority: str = "SENIOR") -> tuple[Fact, ...]:
    """A T4.18 row at q4-2025 under its own fact ids."""
    return tuple(
        conn._text("T4.18", row, field, value, Q4)
        for field, value in (
            ("facility_id", facility),
            ("period_id", Q4),
            ("secured_status", secured),
            ("seniority", seniority),
        )
    )


def _without_current_row(facts: tuple[Fact, ...]) -> tuple[Fact, ...]:
    return tuple(f for f in facts if not (f.table_id == "T4.18" and f.row_id == "term-loan"))


def _upstream(tmp_path: Path, cp1: tuple[Fact, ...], cp4: tuple[Fact, ...] | None = None) -> Any:
    store, _, attempt = conn.seed(tmp_path, cp1=cp1, cp4=cp4)
    return store, attempt, cp4c.cp4c_upstream(store=store, attempt=attempt)


def _renamed(facts: tuple[Fact, ...], old: str, new: str) -> tuple[Fact, ...]:
    return tuple(f.model_copy(update={"text": new}) if f.text == old else f for f in facts)


def test_one_secured_facility_with_another_id_is_the_selected_one(tmp_path: Path) -> None:
    # The q4-2025 row is renamed 'senior-notes'; it is the only SECURED row at q4-2025.
    base = conn.cp1_facts()
    cp1 = tuple(
        f.model_copy(update={"text": "senior-notes"})
        if (f.table_id, f.row_id, f.field) == ("T4.18", "term-loan", "facility_id")
        else f
        for f in base
    )
    cp4 = _renamed(stage1._cp4("positive").facts, "term-loan", "senior-notes")
    _, _, upstream = _upstream(tmp_path, cp1, cp4)
    head = upstream.cp1
    assert head.facility_issue is None
    assert head.facility_id == "senior-notes"
    assert (head.secured_status.text, head.seniority.text) == ("SECURED", "SENIOR")
    assert cp4c.cp4_issue(upstream.cp4, head.facility_id) is None


def test_the_default_term_loan_is_still_selected(tmp_path: Path) -> None:
    _, _, upstream = _upstream(tmp_path, conn.cp1_facts())
    assert (upstream.cp1.facility_id, upstream.cp1.facility_issue) == ("term-loan", None)


ZERO = (
    "CP-4C: CP-1 T4.18 shows 0 secured facilities at q4-2025, not exactly one, so no secured "
    "facility can be selected"
)
TWO = (
    "CP-4C: CP-1 T4.18 shows 2 secured facilities at q4-2025 (term-loan, revolver), not exactly "
    "one, so no secured facility can be selected"
)


def test_no_secured_facility_is_an_issue_naming_the_count(tmp_path: Path) -> None:
    # The q4-2025 row is removed; the q3-2025 row is UNSECURED and the alias row is at fy-2025.
    _, _, upstream = _upstream(tmp_path, _without_current_row(conn.cp1_facts()))
    assert upstream.cp1.facility_issue == ZERO


def test_an_unsecured_row_at_the_quarter_is_not_secured(tmp_path: Path) -> None:
    cp1 = _without_current_row(conn.cp1_facts()) + _row("term-loan", "term-loan", "UNSECURED")
    _, _, upstream = _upstream(tmp_path, cp1)
    assert upstream.cp1.facility_issue == ZERO


def test_two_secured_facilities_are_an_issue_naming_the_count_and_ids(tmp_path: Path) -> None:
    cp1 = conn.cp1_facts() + _row("revolver", "revolver", "SECURED")
    _, _, upstream = _upstream(tmp_path, cp1)
    assert upstream.cp1.facility_issue == TWO


def test_an_unsecured_second_facility_does_not_change_the_selection(tmp_path: Path) -> None:
    cp1 = conn.cp1_facts() + _row("notes", "notes", "UNSECURED", "SUBORDINATED")
    _, _, upstream = _upstream(tmp_path, cp1)
    assert (upstream.cp1.facility_id, upstream.cp1.facility_issue) == ("term-loan", None)


@pytest.mark.parametrize("two", [False, True])
def test_the_validator_and_the_view_refuse_with_the_issue_and_never_raise(
    tmp_path: Path, two: bool
) -> None:
    cp1 = _without_current_row(conn.cp1_facts())
    if two:  # revolver then term-loan, both SECURED at q4-2025, in head order
        cp1 += _row("revolver", "revolver", "SECURED") + _row("term-loan", "term-loan", "SECURED")
    want = TWO.replace("term-loan, revolver", "revolver, term-loan") if two else ZERO
    store, _, upstream = _upstream(tmp_path, cp1)
    pack = store.pack()
    got = cp4c.content_issues(cp4c._inputs(pack, conn._submission(), upstream))
    assert got == (want,)
    block = cp4c.context_block(pack=pack, upstream=upstream)
    assert block["context_issue"] == want
    assert set(block) == {"upstream", "context_issue", "inherited_limitations"}


def test_a_paid_response_over_no_secured_facility_settles_rejected_not_pending(
    tmp_path: Path,
) -> None:
    # The retained step is validated by the journal: the issue is journaled and the attempt ends
    # rejected, where a raise would leave the step pending on every resume.
    store, _, attempt = conn.seed(tmp_path, cp1=_without_current_row(conn.cp1_facts()))
    conn._submit(store, attempt, conn.json.dumps(conn._payload("positive")))
    done = conn._finished(store, attempt)
    assert done.status != "pending"
    assert done.issues == (ZERO,)


def test_a_valid_head_composes_unchanged(tmp_path: Path) -> None:
    store, _, attempt = conn.seed(tmp_path)
    inputs = cp4c._inputs(
        store.pack(), conn._submission(), cp4c.cp4c_upstream(store=store, attempt=attempt)
    )
    assert cp4c.content_issues(inputs) == ()


def test_a_single_secured_row_without_a_facility_id_is_an_issue_not_a_raise(
    tmp_path: Path,
) -> None:
    cp1 = tuple(
        f
        for f in conn.cp1_facts()
        if (f.table_id, f.row_id, f.field) != ("T4.18", "term-loan", "facility_id")
    )
    _, _, upstream = _upstream(tmp_path, cp1)
    assert upstream.cp1.facility_issue == (
        "CP-4C: the one secured CP-1 T4.18 row at q4-2025 states no facility id or no terms"
    )
