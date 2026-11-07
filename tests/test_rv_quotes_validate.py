"""`rv_quotes` row checks on numbers the template grammar accepts but Decimal cannot hold."""

from deploy_vii.contracts import Span
from deploy_vii.inputs.rv_quotes import COLUMNS, row_findings


def _grid(**cells: str) -> dict[tuple[int, int], Span]:
    row = {
        "provider": "Dealer",
        "as_of": "2026-01-02",
        "issuer": "Issuer",
        "facility_id": "TLB-2030",
        "instrument": "Term Loan B",
        "quote_kind": "observed",
        "currency": "USD",
    }
    row.update(cells)
    return {
        (index, 2): Span(locator=f"sheet:rv_quotes!A{index}", text=row[name], data_type="n")
        for index, name in enumerate(COLUMNS, 1)
        if name in row
    }


def test_an_exponent_decimal_cannot_hold_is_a_finding_not_a_crash() -> None:
    findings, _ = row_findings(_grid(bid="1", ask="1e999999999999999999999"), 2)
    assert [cell for cell, _, _ in findings] == ["K2"]
    assert "ask" in findings[0][1] and "not a number" in findings[0][1]


def test_a_small_exponent_still_compares_bid_with_ask() -> None:
    findings, _ = row_findings(_grid(bid="2e2", ask="1e2"), 2)
    assert [problem for _, problem, _ in findings] == ["bid 2e2 exceeds ask 1e2"]
