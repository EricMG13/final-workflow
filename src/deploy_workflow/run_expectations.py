"""An offline, conservative guess of an issuer file's document kind from its name and first pages.

The guess feeds expectations only; it never blocks a run. A cover phrase on page 1 outranks later
pages and the file name; a page naming two kinds, or none, is `unrecognised`."""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from itertools import pairwise

KINDS = (
    "financial_report",
    "earnings_release",
    "credit_agreement",
    "indenture",
    "amendment",
    "intercreditor",
    "compliance_certificate",
    "covenant_review",
    "offering_memorandum",
    "prospectus",
    "lender_presentation",
    "information_memorandum",
    "term_sheet",
    "commitment_letter",
    "ratings",
    "market_quotes",
    "peer_data",
    "management_bridge",
    "portfolio",
    "prior_decision",
    "unrecognised",
)
# Documents that are signed or drafted; a report cannot be "executed" or "draft".
EXECUTABLE = frozenset(
    {
        "credit_agreement",
        "indenture",
        "amendment",
        "intercreditor",
        "offering_memorandum",
        "prospectus",
    }
)
UNRECOGNISED = "unrecognised"


@dataclass(frozen=True)
class Guess:
    kind: str
    signal: str  # What was found and where, for the reader; "" when unrecognised.
    executed: (
        bool | None
    )  # True: execution mark; False: draft mark; None: neither or not a deal document.
    period_end: str | None  # ISO date, financial reports only, when the cover states exactly one.


def _rx(pattern: str) -> re.Pattern[str]:
    return re.compile(pattern, re.IGNORECASE)


# A title line starts with the phrase, so a sentence that merely mentions a document does not count.
LINE_PHRASES: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "financial_report",
        _rx(r"(?:\d{4} )?annual report\b|form 10-[kq]\b|geschäftsbericht|konzernabschluss"),
    ),
    (
        "financial_report",
        _rx(r"(?:group )?consolidated (?:financial statements|statements? of|balance sheet)"),
    ),
    ("credit_agreement", _rx(r"(?:(?:the|this) )?(?:amended and restated )?credit agreement\b")),
    ("indenture", _rx(r"(?:(?:the|this) )?(?:(?:\w+ )?supplemental )?indenture\b")),
    ("amendment", _rx(r"amendment no\.? ?\d+|\w+ amendment to\b")),
    ("intercreditor", _rx(r"(?:(?:the|this) )?intercreditor agreement\b")),
    ("compliance_certificate", _rx(r"compliance certificate\b")),
    ("covenant_review", _rx(r"covenant review\b")),
    ("offering_memorandum", _rx(r"(?:(?:confidential|preliminary) )?offering memorandum\b")),
    (
        "prospectus",
        _rx(r"(?:(?:preliminary|base) )?prospectus\b|supplement no\.? ?\d+\b.*\bprospectus\b"),
    ),
    ("lender_presentation", _rx(r"lender presentation\b")),
    ("information_memorandum", _rx(r"information memorandum\b")),
    ("term_sheet", _rx(r"term sheet\b|summary of (?:indicative )?terms and conditions\b")),
    ("commitment_letter", _rx(r"commitment letter\b")),
    ("ratings", _rx(r"rating action\b")),
    ("market_quotes", _rx(r"(?:\w+ )?quotes as of\b|market quotes\b")),
    ("peer_data", _rx(r"peer (?:comparables|data)\b|comparable companies\b")),
    ("management_bridge", _rx(r"management bridge\b")),
    ("portfolio", _rx(r"portfolio holdings\b")),
    ("prior_decision", _rx(r"investment committee decision memo\b")),
)
# Cover wording that HTML filings run into one line, found anywhere on page 1. The SEC form title
# is upper case; the same words in a body sentence are not a cover.
COVER_PHRASES: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "financial_report",
        re.compile(r"\bFORM 10-[KQ]\b|\b(?:ANNUAL|QUARTERLY) REPORT PURSUANT\b"),
    ),
    (
        "earnings_release",
        _rx(
            r"reports? (?:first|second|third|fourth) quarter\b|"
            r"(?:fourth quarter and )?full[- ]year \d{4} results\b|"
            r"earnings (?:release|conference call)\b"
        ),
    ),
)
# A 10-K's contents list, used only when page 1 gives nothing (a cover the reader returns empty).
INDEX_PHRASE = _rx(r"item 1b\.? unresolved staff comments")
EXECUTION_MARK = _rx(r"(?:execution version|executed copy|conformed copy)\b")
DRAFT_MARK = _rx(r"draft\b|preliminary (?:offering memorandum|prospectus)\b")
DRAFT_ANYWHERE = _rx(r"subject to completion|not for execution")

HTML_HEADER = "Visible text of "
_CELL = re.compile(r"^[A-Z]+\d+='")  # A workbook page prints cells as A1='text'.
_PREFIX = re.compile(
    r"^(?:L\d+: ?)?(?:ex(?:hibit)?[- ]?\d+(?:\.\d+)* )?", re.IGNORECASE
)  # captures, EDGAR
MONTHS = (
    *("january", "february", "march", "april", "may", "june", "july"),
    *("august", "september", "october", "november", "december"),
)
GERMAN = (
    *("januar", "februar", "märz", "april", "mai", "juni", "juli"),
    *("august", "september", "oktober", "november", "dezember"),
)
_MONTH = "|".join(MONTHS)
_ENGLISH_DATE = _rx(rf"\b(?:ended|at) ({_MONTH}) (\d{{1,2}}), (\d{{4}})")
_GERMAN_DATE = _rx(rf"\bzum (\d{{1,2}})\. ({'|'.join(GERMAN)}) (\d{{4}})")


def _lines(page: str, first: bool) -> list[str]:
    raw_lines = page.splitlines()
    if first and raw_lines and raw_lines[0].startswith(HTML_HEADER):
        raw_lines = raw_lines[1:]  # The file name is not cover text.
    lines = []
    for raw in raw_lines:
        line = _CELL.sub("", " ".join(raw.replace("\xa0", " ").split())).rstrip("'")
        line = _PREFIX.sub("", line).strip()
        if line:
            lines.append(line)
    return lines


def _hits(lines: list[str]) -> dict[str, str]:
    """Kind -> the text that matched, from title lines (a line, or a line joined to the next)."""
    found: dict[str, str] = {}
    for candidate in [*lines, *(f"{a} {b}" for a, b in pairwise(lines))]:
        for kind, rx in LINE_PHRASES:
            if match := rx.match(candidate):
                found.setdefault(kind, match.group(0))
    text = "\n".join(lines)
    for kind, rx in COVER_PHRASES:
        if match := rx.search(text):
            found.setdefault(kind, match.group(0))
    return found


def _kind(name: str, lines: list[str], pages: Sequence[str]) -> tuple[str, str]:
    if found := _hits(lines):
        if len(found) > 1:
            return UNRECOGNISED, ""  # Ambiguous cover.
        ((kind, text),) = found.items()
        return kind, f"found {text!r} on page 1"
    for number, page in enumerate(pages, 1):
        if match := INDEX_PHRASE.search(" ".join(page.split())):
            return "financial_report", f"found {match.group(0)!r} on page {number}"
    named = _hits([" ".join(re.split(r"[-_.]+", name))])
    if len(named) == 1:
        ((kind, text),) = named.items()
        return kind, f"file name contains {text!r}"
    return UNRECOGNISED, ""


def _executed(kind: str, name: str, lines: list[str]) -> bool | None:
    if kind not in EXECUTABLE:
        return None
    executed = any(EXECUTION_MARK.match(line) for line in lines)
    draft = any(DRAFT_MARK.match(line) or DRAFT_ANYWHERE.search(line) for line in lines)
    if executed != draft:
        return executed
    if executed:
        return None  # An execution mark and a draft mark together settle nothing.
    spaced = " ".join(re.split(r"[-_.]+", name)).lower()
    executed_name, draft_name = "executed" in spaced.split(), "draft" in spaced.split()
    return (
        True
        if executed_name and not draft_name
        else False
        if draft_name and not executed_name
        else None
    )


def _period_end(lines: list[str]) -> str | None:
    text = " ".join(lines)
    dates: set[str] = set()
    for month, day, year in ((m[0], m[1], m[2]) for m in _ENGLISH_DATE.findall(text)):
        dates.add(_iso(year, MONTHS.index(month.lower()) + 1, day))
    for day, month, year in _GERMAN_DATE.findall(text):
        dates.add(_iso(year, GERMAN.index(month.lower()) + 1, day))
    dates.discard("")
    return next(iter(dates)) if len(dates) == 1 else None


def _iso(year: str, month: int, day: str) -> str:
    try:
        return date(int(year), month, int(day)).isoformat()
    except ValueError:
        return ""  # An impossible date is no date.


def guess_kind(name: str, first_pages: Sequence[str]) -> Guess:
    """The likely kind of one file from its name and its first pages (page 1 is the cover)."""
    lines = _lines(first_pages[0], True) if first_pages else []
    kind, signal = _kind(name, lines, first_pages)
    if kind == UNRECOGNISED:
        return Guess(UNRECOGNISED, "", None, None)
    period = _period_end(lines) if kind == "financial_report" else None
    return Guess(kind, signal, _executed(kind, name, lines), period)
