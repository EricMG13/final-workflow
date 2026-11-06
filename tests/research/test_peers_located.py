"""S16 A01/C01: a TDR.6 quote is a whole figure of its cited span, never a fragment of one.

The key submission cites ``ev-1 line:11``, which reads (``cases/cpdr-peers-owner/manifest.json``)
``Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 200.0``. The only figure that
line states for revenue is ``200.0``: ``20`` and ``0.0`` cut it, ``2025``, ``12``, ``-12`` and
``31`` cut the date. Each must be the cut-figure issue, not a located amount. Expected values are
worked out by hand from that line and from the edited lines below.
"""

import copy
from typing import Any

import pytest
from cpdr_peers_support import Case, peers_case

from deploy_vii.contracts import Source
from deploy_workflow.research import peers as p


@pytest.fixture(scope="module")
def case() -> Case:
    return peers_case()


def _quoting(case: Case, quote: str) -> dict[str, Any]:
    body: dict[str, Any] = copy.deepcopy(case.body)
    body["peers"]["figures"][0]["citation"]["quote"] = quote  # p01 revenue, ev-1 line:11
    return body


def _with_line(case: Case, locator: str, text: str) -> tuple[Source, ...]:
    """The held sources with one ``ev-1`` span's text replaced (the item hash is kept, as a held
    item carries it; ``citation_issues`` compares the citation's hash with the source's)."""
    out = []
    for source in case.sources:
        if source.source_id == "ev-1":
            spans = tuple(
                s.model_copy(update={"text": text}) if s.locator == locator else s
                for s in source.spans
            )
            source = source.model_copy(update={"spans": spans})
        out.append(source)
    return tuple(out)


def _texts(case: Case, body: dict[str, Any], sources: tuple[Source, ...]) -> list[str]:
    pack = case.submission(body).peers
    return [str(i) for i in p.peer_issues(pack, case.brief, case.evidence, sources)]


@pytest.mark.parametrize("quote", ["20", "0.0", "00", "00.0", "2025", "12", "-12", "31"])
def test_a_fragment_of_the_span_is_the_cut_figure_issue(case: Case, quote: str) -> None:
    assert [str(i) for i in case.issues(_quoting(case, quote))] == [f"p01.revenue: {p.CUT_FIGURE}"]


def test_the_whole_figure_is_no_issue(case: Case) -> None:
    assert case.issues(_quoting(case, "200.0")) == ()


@pytest.mark.parametrize(
    ("line", "quote"),
    [
        ("Alder Ridge Holdings revenue for the twelve months to 2025-12-31: (12.3)", "12.3"),
        ("Alder Ridge Holdings revenue for the twelve months to 2025-12-31: -12.3", "12.3"),
        ("Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 1,200.0", "200.0"),
        ("Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 200.0bn", "200.0"),
        ("Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 12.5%", "12.5"),
        ("Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 12/15", "12"),
    ],
)
def test_a_sign_separator_unit_or_date_beside_the_quote_cuts_it(
    case: Case, line: str, quote: str
) -> None:
    """``12.3`` out of ``(12.3)`` or ``-12.3`` would drop the sign; ``200.0`` out of ``1,200.0``
    drops the thousands; a scale suffix, a percent or a date part is not the figure."""
    got = _texts(case, _quoting(case, quote), _with_line(case, "line:11", line))
    assert got == [f"p01.revenue: {p.CUT_FIGURE}"]


@pytest.mark.parametrize(
    ("line", "quote"),
    [
        ("Alder Ridge Holdings revenue for the twelve months to 2025-12-31: -12.3", "-12.3"),
        ("Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 200.0.", "200.0"),
        ("Alder Ridge Holdings revenue, twelve months to 2025-12-31, was 200.0, up.", "200.0"),
    ],
)
def test_a_whole_figure_with_its_sign_or_sentence_punctuation_holds(
    case: Case, line: str, quote: str
) -> None:
    assert _texts(case, _quoting(case, quote), _with_line(case, "line:11", line)) == []


def test_a_parenthesised_negative_quoted_whole_is_the_missing_cell(case: Case) -> None:
    """``(12.3)`` is not read by the table rule: no issue, a missing cell, never ``12.3``."""
    line = "Alder Ridge Holdings revenue for the twelve months to 2025-12-31: (12.3)"
    body = _quoting(case, "(12.3)")
    assert _texts(case, body, _with_line(case, "line:11", line)) == []
    fact = {f.fact_id: f for f in case.composed(body).facts}["TDR.6.p01.revenue.amount"]
    assert (fact.status, fact.amount, fact.limitation) == ("missing", None, p.UNREADABLE)
