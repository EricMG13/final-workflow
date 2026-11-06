"""The run-text figure guard (decision 0005 MC-2): S13 A04/C07.

Expected values are written out by hand from the rule text, not computed with `prose`.
"""

import pytest

from deploy_vii import prose

# --- A04/C07: "N of M", years before a quantity word, numbers in words ----------------------


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # "N of M" is a coverage label only with a pack noun after it.
        ("Covenant headroom was breached in 3 of 4 quarters.", ("3", "4")),
        ("The reader read 195 of 195 pages.", ()),
        ("It located 12 of 14 sources and 3 of 3 located spans.", ()),
        ("Amendment No. 5 of 2025 applies.", ("5",)),
        # A year followed by a quantity word is a figure, not a period label.
        ("EBITDA margin fell by 2024 basis points.", ("2024",)),
        ("Spreads widened 2024 bps.", ("2024",)),
        ("Margin rose 2025 %.", ("2025",)),
        ("Revenue in 2024 was flat against 2023.", ()),
        ("The 7.125% senior secured notes due 2032 rank first.", ()),
        # A number in words with a quantity word, "-fold" or a multiplying verb is a figure.
        (
            "Leverage rose to seven times EBITDA and revenue halved.",
            ("seven times", "halved"),
        ),
        ("Costs rose twenty-five percent.", ("twenty-five percent",)),
        ("Debt grew threefold while capex doubled.", ("threefold", "doubled")),
        ("Ten per cent of revenue is hedged.", ("Ten per cent",)),
        ("One of the notes carries a one-time fee.", ()),
        # Reading order across numeric and word figures.
        ("Revenue halved in 3 of 4 quarters.", ("halved", "3", "4")),
    ],
)
def test_bare_figures(text: str, expected: tuple[str, ...]) -> None:
    assert prose.bare_figures(text) == expected


def test_a_supplied_name_covers_a_number_word() -> None:
    # The issuer name is a supplied name: its words are not a figure.
    assert prose.bare_figures("Seven Times Media reported.", names=("Seven Times Media",)) == ()
    assert prose.bare_figures("Seven Times Media reported.") == ("Seven Times",)


def test_check_reports_each_bypass_as_a_bare_figure() -> None:
    found = prose.check(
        "Covenant headroom was breached in 3 of 4 quarters; margin fell by 2024 basis points.",
        refs=(),
        gaps=(),
    )
    assert found == ("Bare figure: 3", "Bare figure: 4", "Bare figure: 2024")
