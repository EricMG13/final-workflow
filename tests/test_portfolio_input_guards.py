"""S13-A08/A09: percent-formatted % NAV values, negative shares and hidden cells are refused.

The valid workbook comes from `valid()` of tests/product/test_inputs_portfolio.py, whose module
cannot be imported where `scripts.build_templates` is absent; its source is read instead. Expected
issues are hand-derived from the edited cell.
"""

import io
from collections.abc import Callable
from pathlib import Path
from typing import Any

import openpyxl
import pytest

from deploy_vii.inputs.portfolio import MEDIA_TYPE, portfolio_facts, validate_portfolio_bytes
from deploy_vii.preparation import SourceRequest, prepare_source

_SOURCE = (Path(__file__).parent / "product" / "test_inputs_portfolio.py").read_text()
_NAMESPACE: dict[str, Any] = {"date": __import__("datetime").date}
exec(
    "from typing import Any\n"
    + _SOURCE[_SOURCE.index("BRIEF_SHEETS: dict") : _SOURCE.index("HOLDING = {")],
    _NAMESPACE,
)
valid, SHEETS = _NAMESPACE["valid"], _NAMESPACE["BRIEF_SHEETS"]

Tweak = Callable[[openpyxl.Workbook], None]


def _workbook(data: dict[str, list[dict[str, Any]]], tweak: Tweak | None = None) -> bytes:
    book = openpyxl.Workbook()
    book.remove(book.active)
    for name, columns in SHEETS.items():
        if name in data:
            sheet = book.create_sheet(name)
            sheet.append(list(columns))
            for row in data[name]:
                sheet.append([row.get(column) for column in columns])
    if tweak is not None:
        tweak(book)
    stream = io.BytesIO()
    book.save(stream)
    return stream.getvalue()


def _problems(data: dict[str, list[dict[str, Any]]], tweak: Tweak | None = None) -> list[str]:
    return [
        issue.problem for issue in validate_portfolio_bytes("p.xlsx", _workbook(data, tweak)).issues
    ]


def test_the_untouched_workbook_is_accepted() -> None:
    assert _problems(valid()) == []


def test_a_percent_formatted_nav_share_on_a_percent_nav_exposure_row_is_refused() -> None:
    # By hand: cash is 2.5 % NAV, shown 2.50 % in Excel and stored 0.025; read as a plain number it
    # would be 0.025 % NAV, 100 times too small, so the cell is refused instead.
    data = valid()
    data["Exposure_Summary"].append(
        {"metric": "cash", "value": 0.025, "unit": "% NAV", "as_of": "2026-05-29"}
    )
    cash_row = len(data["Exposure_Summary"]) + 1

    def percent(book: openpyxl.Workbook) -> None:
        book["Exposure_Summary"][f"B{cash_row}"].number_format = "0.00%"

    assert _problems(data, percent) == ["value '0.025' is formatted as a percentage"]
    data["Exposure_Summary"][-1]["value"] = "2.5"
    assert _problems(data) == []  # the plain 2.5 is accepted
    data["Exposure_Summary"][-1]["unit"] = "USD"
    assert _problems(data, percent) == []  # a currency amount may be percent-formatted text only


@pytest.mark.parametrize(
    "sheet,index",
    [("Maturity_Profile", 0), ("Top_Holdings", 0), ("Sector_Exposure", 0)],
)
def test_a_negative_pct_nav_is_refused(sheet: str, index: int) -> None:
    # By hand: -40 % NAV is not a share of NAV.
    data = valid()
    data[sheet][index]["pct_nav"] = "-40"
    assert "pct_nav '-40' is negative" in _problems(data)


def test_a_negative_rating_bucket_cannot_offset_another() -> None:
    # By hand: buckets 150 and -50 sum to 100, inside 99 to 101; the -50 is refused instead.
    data = valid()
    data["Rating_Distribution"] = [
        {"rating_bucket": "B", "pct_nav": "150", "issuers": 5},
        {"rating_bucket": "Unrated", "pct_nav": "-50", "issuers": 1},
    ]
    assert _problems(data) == ["pct_nav '-50' is negative"]


def test_a_hidden_row_and_a_hidden_sheet_are_refused() -> None:
    # By hand: row 2 of Top_Holdings is hidden (one issue at its first cell); Maturity_Profile is
    # hidden whole (one issue for the sheet).
    def hide_row(book: openpyxl.Workbook) -> None:
        book["Top_Holdings"].row_dimensions[2].hidden = True

    def hide_sheet(book: openpyxl.Workbook) -> None:
        book["Maturity_Profile"].sheet_state = "hidden"

    assert _problems(valid(), hide_row) == ["row 2 holds hidden cells"]
    assert _problems(valid(), hide_sheet) == ["sheet Maturity_Profile is hidden"]
    raw = _workbook(valid())
    source = prepare_source(
        SourceRequest(source_id="portfolio", path="p.xlsx", media_type=MEDIA_TYPE), raw
    )
    assert portfolio_facts(source).top_holdings  # the visible workbook still yields its holdings
