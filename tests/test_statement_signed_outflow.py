"""S12-A02 (user ruling B, fail closed): a positive `signed` amount on an outflow account is
refused for the model to repair, never flipped to minus its absolute value.

Hand-derived expectations (no production arithmetic): every reader of an outflow account takes
-abs(amount). A source printing "Income taxes refunded (paid), net | 15" recorded `signed` +15
would read -15, wrong by 2 x 15 = 30, so it is refused. The two repairs:
- the source prints the outflow as a positive magnitude: `outflow_magnitude` with `sign_citations`,
  read as -15;
- the source prints a net inflow (a refund): the value is `missing` with a reason, read as missing
  (never 0, never -15, never +15).
Zero is not positive and negative signed amounts are unchanged (-15 stays -15).
"""

from datetime import date
from decimal import Decimal

import pytest
from pydantic import ValidationError
from test_statement_quantities import SHA, book, cite, period

from deploy_vii.contracts import Citation, Run, Source, Span
from deploy_vii.financial_adapter import kernel_registers
from deploy_vii.financial_contracts import (
    Alternative,
    FinancialBook,
    FinancialPeriod,
    FinancialReview,
    Observation,
    StatementLine,
    StatementQuantity,
)
from deploy_vii.financial_reconciliation import Reconciliation, reconcile_financials
from deploy_vii.financial_validation import records, validate_financial_review
from deploy_vii.model import history
from deploy_vii.model._cells import Cell
from deploy_vii.model.history import OUTFLOW_METRICS
from deploy_vii.preparation import PreparedPack
from deploy_vii.statement_output import StatementCell, statement_report
from deploy_vii.statement_validation import ACCOUNT_LINKS, statement_issues

# Every statement item linked to an outflow account, by hand: (statement, item, account).
OUTFLOW_ITEMS = (
    ("IS", "cogs", "cogs"),
    ("IS", "depreciation_amortization", "depreciation_amortization"),
    ("IS", "opex_including_da", "opex_including_da"),
    ("IS", "operating_lease_cost", "operating_lease_cost"),
    ("CFS", "dividends_paid", "dividends_paid"),
    ("CFS", "cash_taxes_paid", "cash_taxes_paid"),
    ("CFS", "cash_interest_paid", "cash_interest_paid"),
    ("CFS", "lease_payments_in_financing", "lease_payments_in_financing"),
    ("CFS", "interest_paid_in_financing", "interest_paid_in_financing"),
    ("CFS", "capex_total", "capex_and_intangible_investment"),
)
REFUND = "Income taxes refunded (paid), net | 15"
WITHHELD = "The source prints a net income tax refund of 15; a refund is not an outflow"
ISSUE = "Positive signed amount on an outflow account"


def observation(oid: str, amount: Decimal | None, quote: str = REFUND) -> Observation:
    if amount is None:
        return Observation(
            observation_id=oid,
            status="missing",
            amount=None,
            citations=(cite(quote),),
            reason=WITHHELD,
        )
    return Observation(observation_id=oid, status="known", amount=amount, citations=(cite(quote),))


def outflow_line(  # noqa: PLR0913 - one keyword per field the cases vary
    statement: str,
    item: str,
    amount: Decimal | None,
    *,
    convention: str = "signed",
    period_id: str = "FY2024",
    line_kind: str = "detail",
    priority: int = 1,
) -> StatementLine:
    line_id = f"{statement.lower()}-{item.replace('_', '-')}"
    return StatementLine(
        line_id=line_id,
        statement=statement,
        item_id=item,
        label=item,
        period_id=period_id,
        display_priority=priority,
        line_kind=line_kind,
        value=observation(f"obs-{line_id}-{period_id}", amount),
        sign_convention=convention,
        sign_citations=(cite(REFUND),) if convention == "outflow_magnitude" else (),
        quantity=StatementQuantity(kind="monetary", scale="MILLIONS", citations=(cite("unit"),)),
    )


def refused(issues: tuple[str, ...]) -> list[str]:
    return [issue for issue in issues if ISSUE in issue]


def test_the_hand_list_is_every_item_linked_to_an_outflow_account() -> None:
    linked = {(s, i, m) for (s, i), m in ACCOUNT_LINKS.items() if m in OUTFLOW_METRICS}
    assert linked == set(OUTFLOW_ITEMS)


@pytest.mark.parametrize(("statement", "item", "account"), OUTFLOW_ITEMS)
def test_a_positive_signed_amount_on_an_outflow_account_is_refused(
    statement: str, item: str, account: str
) -> None:
    row = outflow_line(statement, item, Decimal(15))
    [issue] = refused(statement_issues(book((row,))))
    # The line, its period, the account and both repairs, in one sentence.
    assert f"{row.line_id} FY2024 ({statement} {item}, account {account})" in issue
    assert "`sign_convention: outflow_magnitude` with `sign_citations`" in issue
    assert "net inflow (a refund)" in issue and "status `missing`" in issue
    assert "`reason`" in issue and ". " not in issue


@pytest.mark.parametrize("line_kind", ["subtotal", "total"])
def test_a_positive_signed_subtotal_or_total_on_an_outflow_account_is_refused(
    line_kind: str,
) -> None:
    row = outflow_line("CFS", "capex_total", Decimal("2.5"), line_kind=line_kind)
    assert len(refused(statement_issues(book((row,))))) == 1


@pytest.mark.parametrize(
    "amount",
    [Decimal(0), Decimal("0.00"), Decimal(-15), Decimal("-0.01")],
    ids=["zero", "zero-two-places", "negative", "small-negative"],
)
@pytest.mark.parametrize(("statement", "item", "account"), OUTFLOW_ITEMS)
def test_zero_and_negative_signed_amounts_are_accepted(
    statement: str, item: str, account: str, amount: Decimal
) -> None:
    del account
    assert refused(statement_issues(book((outflow_line(statement, item, amount),)))) == []


@pytest.mark.parametrize(("statement", "item", "account"), OUTFLOW_ITEMS)
def test_a_magnitude_or_a_withheld_refund_is_accepted(
    statement: str, item: str, account: str
) -> None:
    del account
    magnitude = outflow_line(statement, item, Decimal(15), convention="outflow_magnitude")
    withheld = outflow_line(statement, item, None)
    assert refused(statement_issues(book((magnitude,)))) == []
    assert refused(statement_issues(book((withheld,)))) == []


def test_an_outflow_magnitude_without_sign_citations_is_still_refused_by_the_contract() -> None:
    data = outflow_line("CFS", "cash_taxes_paid", Decimal(15)).model_dump()
    data["sign_convention"] = "outflow_magnitude"
    with pytest.raises(ValidationError, match="outflow magnitude normalization requires"):
        StatementLine.model_validate(data)


@pytest.mark.parametrize(
    ("statement", "item"),
    [
        ("IS", "revenue"),  # an inflow account: +15 is a revenue, read +15
        ("CFS", "capex_maintenance"),  # not linked to an account: printed sign kept
        ("CFS", "debt_repayment"),
        ("CFS", "other:income-taxes-refunded-net"),  # issuer detail, not an account
        ("IS", "income_tax_total"),  # linked, but income_tax_expense is not an outflow account
    ],
)
def test_a_positive_signed_amount_off_the_outflow_accounts_is_not_caught(
    statement: str, item: str
) -> None:
    assert refused(statement_issues(book((outflow_line(statement, item, Decimal(15)),)))) == []


@pytest.mark.parametrize(
    "item", ["inventory", "lease_obligations", "total_debt", "other_current_liabilities"]
)
def test_a_balance_sheet_line_is_a_signed_balance_and_not_caught(item: str) -> None:
    bs = period("FY2024-END", 2024).model_copy(
        update={"period_type": "PERIOD_END", "start_date": None, "day_count": None}
    )
    row = outflow_line("BS", item, Decimal(15), period_id="FY2024-END")
    forged = book((row,)).model_copy(update={"periods": (*book().periods, bs)})
    assert refused(statement_issues(forged)) == []


def test_a_conflicting_observation_on_an_outflow_account_is_not_caught() -> None:
    conflict = Observation(
        observation_id="obs-conflict",
        status="conflicting",
        amount=None,
        citations=(cite(REFUND),),
        reason="Two figures are printed",
        alternatives=(
            Alternative(amount=Decimal(15), citations=(cite(REFUND),), explanation="table"),
            Alternative(amount=Decimal(-15), citations=(cite("note"),), explanation="note"),
        ),
    )
    row = outflow_line("CFS", "cash_taxes_paid", None).model_copy(update={"value": conflict})
    assert refused(statement_issues(book((row,)))) == []


# --- end to end: validation, the statement report, the reconciliation and the history/LTM ------

QUARTERS = (
    ("q1-2025", 1, date(2025, 1, 1), date(2025, 3, 31), 90),
    ("q2-2025", 2, date(2025, 4, 1), date(2025, 6, 30), 91),
    ("q3-2025", 3, date(2025, 7, 1), date(2025, 9, 30), 92),
    ("q4-2025", 4, date(2025, 10, 1), date(2025, 12, 31), 92),
)


def quarter(pid: str, number: int, start: date, end: date, days: int) -> FinancialPeriod:
    return period(pid, 2025).model_copy(
        update={
            "period_type": "QUARTER",
            "fiscal_quarter": number,
            "start_date": start,
            "end_date": end,
            "day_count": days,
        }
    )


def flow_book(statement: str, item: str, q2: StatementLine) -> FinancialBook:
    """One outflow item over four calendar 2025 quarters and FY2025: Q1 a printed magnitude 1
    (read -1), Q2 the case, Q3 a printed (1) (signed -1), Q4 zero, FY a printed (2) (signed -2)."""
    fy = period("fy-2025", 2025).model_copy(
        update={"start_date": date(2025, 1, 1), "end_date": date(2025, 12, 31), "day_count": 365}
    )
    lines = (
        outflow_line(
            statement, item, Decimal(1), convention="outflow_magnitude", period_id="q1-2025"
        ),
        q2,
        outflow_line(statement, item, Decimal(-1), period_id="q3-2025"),
        outflow_line(statement, item, Decimal(0), period_id="q4-2025"),
        outflow_line(statement, item, Decimal(-2), period_id="fy-2025"),
    )
    return book(lines).model_copy(update={"periods": (*(quarter(*q) for q in QUARTERS), fy)})


def case(book_value: FinancialBook) -> tuple[PreparedPack, FinancialReview]:
    """A pack whose one source `filing` holds every quote the book cites, and its review."""
    run = Run(
        run_id="signed-outflow",
        issuer_id="issuer",
        issuer_name="Signed Outflow Fixture",
        as_of=date(2026, 6, 30),
        case_kind="synthetic",
    )
    review = FinancialReview(
        pack_sha256=SHA,
        run_id=run.run_id,
        issuer_id=run.issuer_id,
        as_of=run.as_of,
        books=(book_value,),
        analysis=(),
    )
    spans: dict[str, set[str]] = {}
    for citation in records(review, Citation):
        spans.setdefault(citation.locator, set()).add(citation.quote)
    source = Source(
        source_id="filing",
        name="Signed outflow fixture",
        status="ready",
        sha256=SHA,
        spans=tuple(
            Span(locator=locator, text="\n".join(sorted(quotes)))
            for locator, quotes in sorted(spans.items())
        ),
        extraction_status="complete",
    )
    pack = PreparedPack(run=run, sources=(source,))
    return pack, review.model_copy(update={"pack_sha256": pack.content_hash()})


def _downstream(
    statement: str, item: str, account: str, amount: Decimal | None, convention: str = "signed"
) -> tuple[StatementCell, Reconciliation, Cell, Cell]:
    """The Q2 statement cell, the FY_QUARTERS check, the Q2 history cell and the LTM at Q4."""
    q2 = outflow_line(statement, item, amount, convention=convention, period_id="q2-2025")
    pack, review = case(flow_book(statement, item, q2))
    assert validate_financial_review(pack, review) == ()
    cell = next(
        c
        for c in statement_report(pack, review, "book").cells
        if c.item_id == item and c.period_id == "q2-2025"
    )
    check = next(
        c
        for c in reconcile_financials(pack, review, "book").checks
        if c.check_type == "FY_QUARTERS" and c.metric_id == account
    )
    regs = kernel_registers(pack, review, "book")
    columns = history.historical_columns(regs)
    frame = history.account_frame(regs, columns)
    ltm = history.ltm_frames(regs, columns)
    q2_column = next(c.column_id for c in columns if c.period_id == "q2-2025")
    q4_column = next(c.column_id for c in columns if c.period_id == "q4-2025")
    key = f"acct:{account}"
    return cell, check, frame[q2_column][key], ltm[q4_column][key]


@pytest.mark.parametrize(("statement", "item", "account"), OUTFLOW_ITEMS)
def test_a_positive_signed_refund_fails_the_whole_review_closed(
    statement: str, item: str, account: str
) -> None:
    q2 = outflow_line(statement, item, Decimal(15), period_id="q2-2025")
    pack, review = case(flow_book(statement, item, q2))
    [issue] = validate_financial_review(pack, review)
    assert issue.startswith(f"book: {ISSUE}: {q2.line_id} q2-2025 ({statement} {item}, account")
    for build in (statement_report, reconcile_financials, kernel_registers):
        with pytest.raises(ValueError, match=ISSUE):
            build(pack, review, "book")


@pytest.mark.parametrize(("statement", "item", "account"), OUTFLOW_ITEMS)
def test_a_printed_magnitude_is_read_as_the_negative_outflow(
    statement: str, item: str, account: str
) -> None:
    cell, check, q2_cell, ltm_cell = _downstream(
        statement, item, account, Decimal(15), "outflow_magnitude"
    )
    # Source 15 printed as a magnitude: normalized -15.
    assert (cell.source_amount, cell.normalized_amount) == (Decimal(15), Decimal(-15))
    assert cell.normalization == "negative absolute source amount"
    # FY_QUARTERS: Q1 -1, Q2 -15, Q3 -1, Q4 0 sum to -17 against the reported FY -2.
    assert [t.amount for t in check.components] == [-1, -15, -1, 0]
    assert check.calculated_value == Decimal(-17) and check.reported_value == Decimal(-2)
    # History: Q2 reads -15; the LTM at Q4 is -1 - 15 - 1 + 0 = -17.
    assert (q2_cell.value, ltm_cell.value) == (Decimal(-15), Decimal(-17))


@pytest.mark.parametrize(("statement", "item", "account"), OUTFLOW_ITEMS)
def test_a_withheld_refund_is_read_as_missing_downstream(
    statement: str, item: str, account: str
) -> None:
    cell, check, q2_cell, ltm_cell = _downstream(statement, item, account, None)
    # Statement report: missing, no source or normalized figure, the reason as the limitation.
    assert (cell.status, cell.source_amount, cell.normalized_amount) == ("missing", None, None)
    assert (cell.normalization, cell.limitation) == ("identity", WITHHELD)
    # Reconciliation: the Q2 term has no amount (never 0, -15 or +15) and carries the reason, so
    # the quarters do not sum.
    q2_term = check.components[1]
    assert (q2_term.original_amount, q2_term.amount, q2_term.reason) == (None, None, WITHHELD)
    assert check.calculated_value is None and check.status == "BLOCK"
    # History and LTM: Q2 has no figure; the LTM at Q4 cannot be summed.
    assert q2_cell.value is None and q2_cell.reason == "NOT_STATED"
    assert ltm_cell.value is None and ltm_cell.reason == "COMPONENT_MISSING"


@pytest.mark.parametrize(("statement", "item", "account"), OUTFLOW_ITEMS)
def test_zero_and_a_negative_signed_amount_read_unchanged_downstream(
    statement: str, item: str, account: str
) -> None:
    zero_cell, zero_check, zero_q2, zero_ltm = _downstream(statement, item, account, Decimal(0))
    # Zero is not positive: no normalization; Q1 -1, Q2 0, Q3 -1, Q4 0 = -2, the reported FY.
    assert (zero_cell.normalization, zero_q2.value, zero_ltm.value) == ("identity", 0, -2)
    assert zero_check.calculated_value == Decimal(-2)
    cell, check, q2_cell, ltm_cell = _downstream(statement, item, account, Decimal(-15))
    # -15 printed as (15): unchanged, no normalization; Q1 -1, Q2 -15, Q3 -1, Q4 0 = -17.
    assert (cell.source_amount, cell.normalized_amount) == (Decimal(-15), Decimal(-15))
    assert cell.normalization == "identity"
    assert check.calculated_value == Decimal(-17)
    assert (q2_cell.value, ltm_cell.value) == (Decimal(-15), Decimal(-17))
