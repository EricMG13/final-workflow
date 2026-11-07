"""A printed value the extraction rules do not read is never silent (review of
S12-vii-financial-engine-A04/C04).

- A row of minus-signed (`-1,234`, U+2212 `−123`), percent (`12.5%`),
  split-parenthesis (`(250 )`) or decimal-comma (`1.234,5`) values is not data and is
  listed in `omitted`, whatever the sign of its last column. Reading such cells as values is
  an open ruling; until then they are recorded, not read.
- A minus-signed value left in a data line's label flags it `label_ends_numeric`.
"""

from decimal import Decimal

from deploy_vii.statement_extract import (
    LABEL_ENDS_NUMERIC,
    extract_statement_lines,
)

HEADER = "                                   2025        2024"


def _page(*rows: str) -> str:
    return "\n".join(("CONSOLIDATED STATEMENTS OF OPERATIONS", HEADER, *rows))


def test_minus_percent_and_split_rows_are_omitted_never_silent() -> None:
    rows = (
        "Revenue                           1,200       1,100",
        "Net loss                         -1,234        -567",
        "Other expense                     −123         −45",
        "Tax rate                          12.5%       11.0%",
        "Operating loss                   (250 )       (80 )",
        "Margin                            12.5 %      11.0 %",
        "Umsatz                          1.234,5       987,0",
        "Margin change                    (2.5)%      (0.4)%",
        "Operating result                 -1,234       2,345",
        "Other result                      2,345      -1,234",
        "Operating income                    300         250",
    )
    table = extract_statement_lines(_page(*rows), "p1")
    assert [line.label for line in table.lines] == ["Revenue", "Operating income"]
    # Lines 4-12 of the page (two lines above the rows), every unread row, in page order.
    assert [o.line_no for o in table.omitted] == list(range(4, 13))
    assert [o.text for o in table.omitted] == list(rows[1:10])


def test_read_values_are_unchanged() -> None:
    table = extract_statement_lines(
        _page(
            "Revenue                           1,200       1,100",
            "Net loss (alt)                    (120)        (80)",
            "Cash                            $ 1,234.5     $ 987",
        ),
        "p1",
    )
    assert [(line.label, line.values, line.flags) for line in table.lines] == [
        ("Revenue", (Decimal(1200), Decimal(1100)), ()),
        ("Net loss (alt)", (Decimal(-120), Decimal(-80)), ()),
        ("Cash", (Decimal("1234.5"), Decimal(987)), ()),
    ]
    assert table.omitted == ()


def test_prose_ending_in_a_year_or_word_is_not_a_candidate() -> None:
    page = (
        "The company was founded in 2001 and listed on December 31, 2025.\n"
        "See note 7 for the impact of COVID-19\n"
        "Commitments and contingencies (Note 8)\n"
        "Commitments and contingencies (Note 8          )\n"
        "Auditor Firm ID: 185)\n"
        "                    December 31,2024         December 31,2025\n"
        "Page 12"
    )
    table = extract_statement_lines(page, "p1")
    assert table.lines == ()
    # "Page 12" ends in a numeric cell and was already a candidate; the prose lines are not.
    assert [o.text for o in table.omitted] == ["Page 12"]


def test_minus_value_left_in_the_label_is_flagged() -> None:
    # "-120" stops the right-to-left scan, so (80) and (70) are the values and
    # "Net loss  -120" the label: flagged, so the row is not composed unseen.
    table = extract_statement_lines(
        _page("Net loss                -120        (80)        (70)"), "p1"
    )
    (line,) = table.lines
    assert line.values == (Decimal(-80), Decimal(-70))
    assert LABEL_ENDS_NUMERIC in line.flags
