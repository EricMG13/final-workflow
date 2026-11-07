"""S16 A04/C06/C07: one source is one family however its label is spelled or its bytes repeated."""

from datetime import date
from pathlib import Path

import pytest

from deploy_workflow.research import review as r
from deploy_workflow.research.intake import intake, parse_rows

H1, H2 = "a" * 64, "b" * 64


def _issues(first: str, second: str, h2: str = H2) -> list[str]:
    family_of = {"ev-1": (r.family_key(first), H1), "ev-2": (r.family_key(second), h2)}
    return [i.text for i in r._family_issues("q1", ("ev-1", "ev-2"), family_of)]


# Hand-derived: each pair names one outlet; only a truly different name is independent.
@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("Reuters", "Reuters"),
        ("Reuters", "reuters"),
        ("Reuters", "Reuters "),
        ("Reuters", "  Reuters\t"),
        ("Reuters News", "Reuters   News"),
        ("Reuters", "Ｒｅｕｔｅｒｓ"),  # fullwidth, NFKC
        ("Reuters", "Reu\u200bters"),  # zero-width space
        ("Réuters", "RÉUTERS"),
        ("Straße", "STRASSE"),  # casefold, not lower
    ],
)
def test_label_variants_are_one_family(first: str, second: str) -> None:
    assert len(_issues(first, second)) == 1


@pytest.mark.parametrize(("first", "second"), [("Reuters", "Reuter"), ("Reuters", "Bloomberg")])
def test_different_families_stay_independent(first: str, second: str) -> None:
    assert _issues(first, second) == []


def test_distinct_accented_names_are_not_merged() -> None:
    assert _issues("Reuters", "Réuters") == []


def test_identical_content_is_one_source_under_two_families() -> None:
    # Hand-derived: same hash H1 under 'Wire A' and 'Wire B' -> one issue naming the content.
    assert _issues("Wire A", "Wire B", h2=H1) == [
        "families not independent: ev-1 and ev-2 hold identical content"
    ]


def test_same_file_twice_from_intake_is_not_independent(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("Alder Ridge said revenue rose.\n", encoding="utf-8")
    base = {"path": "a.txt", "locator": "L", "tag": "research", "published": "2025-01-01"}
    rows = parse_rows([{**base, "family": "Wire A"}, {**base, "family": "Wire B"}])
    day = date(2026, 1, 1)
    got = intake(rows, base_dir=tmp_path, dest_dir=None, as_of=day, cutoff=day, today=day)
    family_of = {i.item_id: (r.family_key(i.family), i.sha256) for i in got.accepted}
    assert len(r._family_issues("q1", ("ev-1", "ev-2"), family_of)) == 1
