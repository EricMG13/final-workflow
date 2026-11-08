"""guess_kind against the hand-labelled key (tests/fixtures/run-expectations/document-key.json).

The key was written before the guess existed and is not edited here. Each entry's file goes through
the page reader the launcher uses, and the guess sees pages[:3]."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import pytest
from pypdf.errors import DependencyError

from deploy_workflow.model.handoff import _pages
from deploy_workflow.owners.cpos_launch import _html_page_rows
from deploy_workflow.run_expectations import KINDS, Guess, guess_kind

ROOT = Path(__file__).resolve().parents[1]
KEY = json.loads((ROOT / "tests/fixtures/run-expectations/document-key.json").read_text("utf-8"))
ENTRIES: list[dict[str, Any]] = KEY["entries"]
HTML = {".htm", ".html"}
# A file the launcher's own reader cannot open here is refused by the launcher before any guess.
# Only the optional AES dependency of pypdf is tolerated as the reason, and it is reported.
READER_GAP = "cryptography"


def first_pages(entry: dict[str, Any]) -> list[str]:
    path = ROOT / entry["path"]
    if entry["origin"] == "synthetic":
        body = path.read_text("utf-8").split("\n", 1)[1]  # line 1 is the banner, not page text
        return re.split(r"^=== PAGE ===$", body, flags=re.MULTILINE)[:3] if body.strip() else [""]
    raw = path.read_bytes()
    if path.suffix.lower() in HTML:
        return _pages(f"{path.name}.jsonl", _html_page_rows(path.name, raw))[:3]
    return _pages(path.name, raw)[:3]


def scored() -> tuple[list[tuple[dict[str, Any], Guess]], list[str]]:
    results: list[tuple[dict[str, Any], Guess]] = []
    unreadable: list[str] = []
    for entry in ENTRIES:
        try:
            pages = first_pages(entry)
        except (
            DependencyError
        ) as error:  # reported below; only pypdf's missing AES package is tolerated
            assert READER_GAP in str(error), f"{entry['path']}: {error}"
            unreadable.append(entry["path"])
            continue
        results.append((entry, guess_kind(Path(entry["path"]).name, pages)))
    return results, unreadable


RESULTS, UNREADABLE = scored()


def table() -> str:
    rows: dict[tuple[str, str], list[int]] = defaultdict(lambda: [0, 0, 0, 0])
    for entry, guess in RESULTS:
        row = rows[(entry["origin"], entry["kind"])]
        row[0] += 1
        if guess.kind == entry["kind"]:
            row[1] += 1
        elif guess.kind == "unrecognised":
            row[2] += 1
        else:
            row[3] += 1
    lines = ["origin     kind                    n  right  unrecognised  wrong"]
    lines += [
        f"{origin:<10} {kind:<22} {n:>2} {right:>6} {unrec:>13} {wrong:>6}"
        for (origin, kind), (n, right, unrec, wrong) in sorted(rows.items())
    ]
    lines.append(f"unreadable by the launcher reader here ({READER_GAP} missing): {UNREADABLE}")
    return "\n".join(lines)


def test_key_is_the_one_the_brief_describes() -> None:
    assert KEY["schema"] == "document-key/1"
    assert len(ENTRIES) >= 20
    assert {e["kind"] for e in ENTRIES} <= set(KINDS)
    assert len(UNREADABLE) <= 2  # HEICO and the KPMG report, both AES-encrypted PDFs


def test_no_recognised_kind_contradicts_the_key() -> None:
    print("\n" + table())
    wrong = [
        (e["path"], e["kind"], g.kind)
        for e, g in RESULTS
        if g.kind not in {e["kind"], "unrecognised"}
    ]
    assert not wrong, f"{wrong}\n{table()}"


def test_real_files_are_mostly_recognised() -> None:
    real = [(e, g) for e, g in RESULTS if e["origin"] == "real"]
    missed = [
        e["path"] for e, g in real if g.kind == "unrecognised" and e["kind"] != "unrecognised"
    ]
    assert len(missed) <= 0.10 * len(real), f"{missed}\n{table()}"


def test_synthetic_files_are_all_recognised() -> None:
    missed = [e["path"] for e, g in RESULTS if e["origin"] == "synthetic" and g.kind != e["kind"]]
    assert not missed, f"{missed}\n{table()}"


def test_focus_entries_match_exactly() -> None:
    focus = [(e, g) for e, g in RESULTS if "focus" in e]
    assert len(focus) >= 15
    bad = [
        (e["path"], (e["kind"], e["executed"], e["period_end"]), (g.kind, g.executed, g.period_end))
        for e, g in focus
        if (g.kind, g.executed, g.period_end) != (e["kind"], e["executed"], e["period_end"])
    ]
    assert not bad, f"{bad}\n{table()}"


def test_executed_never_contradicts_the_key() -> None:
    bad = [
        (e["path"], e["executed"], g.executed)
        for e, g in RESULTS
        if g.executed is not None and g.executed != e["executed"]
    ]
    assert not bad, bad


def test_period_end_is_the_key_or_none() -> None:
    bad = [
        (e["path"], e["period_end"], g.period_end)
        for e, g in RESULTS
        if g.period_end is not None and g.period_end != e["period_end"]
    ]
    assert not bad, bad


def test_signal_explains_a_recognised_kind() -> None:
    for entry, guess in RESULTS:
        assert bool(guess.signal) == (guess.kind != "unrecognised"), entry["path"]


def test_html_header_line_is_not_cover_text() -> None:
    header = "Visible text of FORM 10-K CREDIT AGREEMENT.htm, sha256 ab.\nSkip to content\n"
    assert guess_kind("page.htm", [header]).kind == "unrecognised"
    assert guess_kind("page.htm", [header + "CREDIT AGREEMENT\n"]).kind == "credit_agreement"


def test_preliminary_statements_is_never_a_draft_signal() -> None:
    page = "CREDIT AGREEMENT\ndated as of March 1, 2025\nPRELIMINARY STATEMENTS\nWHEREAS"
    assert guess_kind("a.txt", [page]).executed is None
    assert guess_kind("a.txt", ["EXECUTION VERSION\n" + page]).executed is True
    assert guess_kind("a.txt", ["DRAFT\n" + page]).executed is False


def test_a_page_naming_two_kinds_is_ambiguous() -> None:
    assert guess_kind("a.txt", ["CREDIT AGREEMENT\nINDENTURE\n"]).kind == "unrecognised"


def test_cover_outranks_later_pages_and_name() -> None:
    pages = ["COMPLIANCE CERTIFICATE\n", "INDENTURE\n"]
    assert guess_kind("Credit-Agreement.txt", pages).kind == "compliance_certificate"


def test_name_decides_only_when_the_pages_are_silent() -> None:
    assert guess_kind("notes.txt", ["no cover phrase here"]).kind == "unrecognised"
    named = guess_kind("Term-Sheet-draft.txt", ["no cover phrase here"])
    assert (named.kind, named.executed) == ("term_sheet", None)  # term sheets carry no mark
    guess = guess_kind("Indenture-executed.pdf", [""])
    assert (guess.kind, guess.executed) == ("indenture", True)
    assert guess_kind("Indenture-executed.pdf", ["COMPLIANCE CERTIFICATE"]).executed is None


def test_period_end_needs_one_unambiguous_date() -> None:
    two = "FORM 10-K\nFor the fiscal year ended June 30, 2025\nand the year ended June 30, 2024"
    assert guess_kind("a.txt", [two]).period_end is None
    assert (
        guess_kind(
            "a.txt", [two.split("\n")[0] + "\nFor the fiscal year ended February 30, 2025"]
        ).period_end
        is None
    )
    one = guess_kind("a.txt", ["FORM 10-K\nFor the fiscal year ended June 30, 2025"])
    assert one.period_end == "2025-06-30"


def test_no_pages_is_unrecognised() -> None:
    assert guess_kind("x.txt", []) == Guess("unrecognised", "", None, None)


@pytest.mark.parametrize("kind", KINDS)
def test_every_kind_name_is_a_string(kind: str) -> None:
    assert re.fullmatch(r"[a-z_]+", kind)
