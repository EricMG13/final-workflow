"""Synthetic regressions for S04 low findings (A04-A07, C08, C10): hand-written CP-1 handoffs
through the real CP-OS layout and markdown_files; no retained model response, no analytical run.
Expected values are written out from the handoff text, not computed by the code under test."""

import hashlib
import json
from pathlib import Path

import pytest

from deploy_vii.charts import _categories
from deploy_vii.contracts import Run, View
from deploy_vii.report_view import ReportView
from deploy_workflow.handoff_delivery import DeliveryRequest, HandoffInput, physical_lines
from deploy_workflow.markdown_delivery import literal_module, markdown_files
from deploy_workflow.model_handoff_delivery import _AnnualReader
from deploy_workflow.owners.cpos_launch import _layout

RUN = Run.model_validate_json(
    json.dumps(
        {
            "schema_version": "run/2",
            "run_id": "x",
            "issuer_id": "ACME",
            "issuer_name": "Acme Corp",
            "as_of": "2024-12-31",
            "method_version": "deploy-v-r14",
            "case_kind": "public",
            "pathway": "credit_snapshot",
            "requested_modules": ["CP-1"],
        }
    )
)
HEAD = "| Period | {cols} | Reporting unit | Basis and limitation |\n| --- | {sep} | --- | --- |\n"


def chart(heading, cols, rows, unit):
    out = f"### {heading}\n\n" + HEAD.format(
        cols=" | ".join(cols), sep=" | ".join("---" for _ in cols)
    )
    for period, *vals in rows:
        out += f"| {period} | " + " | ".join(vals) + f" | {unit} | basis |\n"
    return out + "\n"


def handoff(leverage=None, liq=None, unit_liq="US$m", extra=""):
    leverage = leverage or [("FY2023", "4.1", "3.9"), ("FY2024", "3.8", "3.5")]
    liq = liq or [("FY2023", "100", "200"), ("FY2024", "150", "Not supplied: undisclosed")]
    return (
        "# CP-1 Acme Corp\n\n## Request\nAcme Corp historical analysis.\n\n## Sources\nsrc.pdf\n\n"
        "## Findings\n\n"
        + chart("Chart data: leverage", ["Total debt / EBITDA", "Net debt / EBITDA"], leverage, "x")
        + chart("Chart data: interest cover", ["EBITDA / cash interest"], [("FY2024", "2.7")], "x")
        + chart("Chart data: liquidity", ["Cash", "Undrawn committed facilities"], liq, unit_liq)
        + chart("Chart data: debt maturities", ["Debt maturing"], [("2025", "50")], "US$m")
        + "### Financials and credit metrics\n\n"
        + "| Metric | FY2024 |\n| --- | ---: |\n| Revenue | 1 |\n\n"
        + extra
        + "## Calculations\nNone.\n\n## Gaps\nNone.\n\n## Next module\nDelivery.\n"
    )


def deliver(tmp_path: Path, text: str):
    raw = text.encode()
    layout, _ = _layout(RUN, ("CP-1",), (), "cfg")
    (tmp_path / "CP-1.md").write_bytes(raw)
    spec = HandoffInput(path="CP-1.md", sha256=hashlib.sha256(raw).hexdigest())
    files = markdown_files(
        DeliveryRequest(run=RUN, handoffs={"CP-1": spec}, layout=layout), tmp_path
    )
    report = ReportView.model_validate_json(files["report-view.json"])
    figures = {f.fig_id: f for b in report.blocks for f in b.figures}
    return files, figures, View.model_validate_json(files["view.json"])


@pytest.mark.parametrize(
    ("rows", "expected"),
    [
        # Hand-derived: the x axis runs oldest to newest whatever order the rows were written in.
        (
            [("FY2024", "3", "3"), ("FY2023", "4", "4"), ("FY2022", "5", "5")],
            ["FY2022", "FY2023", "FY2024"],
        ),
        (
            [("FY2022", "5", "5"), ("FY2023", "4", "4"), ("FY2024", "3", "3")],
            ["FY2022", "FY2023", "FY2024"],
        ),
        (
            [("FY2023", "4", "4"), ("FY2024", "3", "3"), ("FY2022", "5", "5")],
            ["FY2022", "FY2023", "FY2024"],
        ),
        # Quarters of one year sort by quarter; a label with no year keeps the authored order.
        ([("Q3 2024", "1", "1"), ("Q1 2024", "2", "2")], ["Q1 2024", "Q3 2024"]),
        ([("LTM", "1", "1"), ("FY2023", "2", "2")], ["LTM", "FY2023"]),
    ],
)
def test_chart_periods_run_oldest_first(tmp_path, rows, expected):
    _, figures, _ = deliver(tmp_path, handoff(leverage=rows))
    assert _categories(figures["S.1"].chart) == expected


def test_reordered_chart_keeps_each_value_with_its_period(tmp_path):
    # FY2024 Total debt/EBITDA is 3 and FY2023 is 4, as written.
    _, figures, _ = deliver(
        tmp_path, handoff(leverage=[("FY2024", "3", "9"), ("FY2023", "4", "8")])
    )
    got = {(m.series, m.label): m.value for m in figures["S.1"].chart.marks}
    assert (
        got[("Total debt / EBITDA", "FY2024")] == 3 and got[("Total debt / EBITDA", "FY2023")] == 4
    )
    assert got[("Net debt / EBITDA", "FY2024")] == 9 and got[("Net debt / EBITDA", "FY2023")] == 8


@pytest.mark.parametrize("separator", [" ", " ", "\x0c", "\x0b", "\x85", "\x1c", "\r"])
def test_line_citations_count_newlines_only(tmp_path, separator):
    # The prose line holds one separator; every later citation must still name the line a reader
    # finds by counting "\n" (with "\r\n" and a lone "\r" being one newline each).
    text = handoff(extra=f"Revenue rose{separator} strongly.\n\nLater paragraph.\n\n")
    _, _, view = deliver(tmp_path, text)
    physical = physical_lines(text)
    checked = 0
    for fact in next(m for m in view.modules if m.module_id == "CP-1").facts:
        for c in fact.citations:
            assert physical[int(c.locator.split()[-1]) - 1] == c.quote
            checked += 1
    assert checked > 10


def test_crlf_handoff_cites_the_same_lines(tmp_path):
    text = handoff(extra="Later paragraph.\n\n")
    _, _, lf = deliver(tmp_path, text)
    crlf = text.replace("\n", "\r\n")
    assert physical_lines(crlf) == physical_lines(text)
    _, _, got = deliver(tmp_path, crlf)

    def cites(v):
        return [c.locator for m in v.modules for f in m.facts for c in f.citations]

    assert cites(got) == cites(lf)


def test_physical_lines_edges():
    assert physical_lines("") == []
    assert physical_lines("a\n") == ["a"] and physical_lines("a\n\n") == ["a", ""]
    assert physical_lines("a b\r\nc\rd") == ["a b", "c", "d"]


def prose_texts(text: str) -> list[str]:
    module = literal_module("CP-1", text.encode())[0]
    return [f.text for f in module.facts if f.text]


def _doc(body: str) -> str:
    return (
        "# CP-1 Acme Corp\n## Request\nR.\n## Sources\nS.\n## Findings\n"
        + body
        + "\n## Calculations\nC.\n## Gaps\nG.\n## Next module\nN.\n"
    )


def test_multiline_html_comment_is_not_published():
    shown = prose_texts(_doc("Visible one.\n<!--\nDRAFT: internal 999\nmore\n-->\nVisible two.\n"))
    assert "Visible one." in shown and "Visible two." in shown
    assert not [t for t in shown if "DRAFT" in t or "more" == t or "-->" in t]


def test_single_line_and_nested_comments():
    shown = prose_texts(_doc("<!-- one line -->\nA.\n<!-- open <!-- inner -->\nB.\n"))
    # The comment ends at its first `-->` (HTML rule); the later `-->` text never appears alone.
    assert (
        "A." in shown
        and "B." in shown
        and not [t for t in shown if "inner" in t or "one line" in t]
    )


def test_comment_markers_inside_a_fence_stay_text():
    shown = prose_texts(_doc("```\n<!--\nkept\n```\nAfter.\n"))
    assert any("kept" in t for t in shown) and "After." in shown


def test_unterminated_html_comment_is_refused():
    with pytest.raises(ValueError, match="never closed"):
        literal_module("CP-1", _doc("Before.\n<!--\nhidden forever\n").encode())


def test_reporting_unit_other_than_the_chart_unit_is_refused(tmp_path):
    with pytest.raises(ValueError, match="reported in EUR m, not US\\$m"):
        deliver(tmp_path, handoff(unit_liq="EUR m"))
    with pytest.raises(ValueError, match="reported in GBP m"):
        deliver(tmp_path, handoff(unit_liq="GBP m"))


def test_gap_in_another_unit_row_is_still_a_gap_and_matching_unit_publishes(tmp_path):
    # Hand-derived: FY2024 Undrawn is "Not supplied", so it stays a gap even in a EUR m row.
    rows = [("FY2023", "100", "200"), ("FY2024", "Not supplied: n/a", "Not supplied: n/a")]
    _, figures, _ = deliver(tmp_path, handoff(liq=rows))
    cash = {m.label: m.value for m in figures["S.3"].chart.marks if m.series == "Cash"}
    assert cash["FY2023"] == 100 and cash["FY2024"] is None


def test_table_route_into_a_chart_strip_block_is_refused(tmp_path):
    raw = handoff().encode()
    layout, _ = _layout(RUN, ("CP-1",), (), "cfg")
    routes = list(layout.routes)
    routes[0] = routes[0].model_copy(update={"kind": "table", "figure_id": None})
    layout = layout.model_copy(update={"routes": tuple(routes)})
    (tmp_path / "CP-1.md").write_bytes(raw)
    spec = HandoffInput(path="CP-1.md", sha256=hashlib.sha256(raw).hexdigest())
    with pytest.raises(ValueError, match="chart strip block takes only chart routes"):
        markdown_files(DeliveryRequest(run=RUN, handoffs={"CP-1": spec}, layout=layout), tmp_path)


@pytest.mark.parametrize(
    "cell", ["Not supplied: undisclosed", "Not supplied", "Not calculable: missing inputs", "—", ""]
)
def test_model_reader_treats_every_chart_gap_spelling_as_a_gap(cell):
    # Hand-derived: each spelling is an explicit gap (NOT_STATED, no value), never an error.
    raw = f"### T4.10 dashboard\n| Metric | FY2024 |\n|---|---|\n| Revenue | {cell} |\n".encode()
    spec = HandoffInput.model_validate_json(
        json.dumps({"path": "a.md", "sha256": hashlib.sha256(raw).hexdigest()})
    )
    from deploy_workflow.handoff_delivery import ModelDelivery

    layout = ModelDelivery.model_validate_json(
        json.dumps(
            {
                "periods": {
                    "FY2024": {
                        "start_date": "2024-01-01",
                        "end_date": "2024-12-31",
                        "balance_column": None,
                    }
                },
                "anchors": {"dashboard": "### T4.10 dashboard"},
                "rows": {"revenue": {"table": "dashboard", "label": "Revenue"}},
            }
        )
    )
    got = _AnnualReader(raw, spec, layout).read("revenue", "FY2024")
    assert got.value is None and got.reason == "NOT_STATED"


def test_model_reader_still_refuses_a_malformed_number():
    raw = b"### T4.10 dashboard\n| Metric | FY2024 |\n|---|---|\n| Revenue | 12x |\n"
    spec = HandoffInput.model_validate_json(
        json.dumps({"path": "a.md", "sha256": hashlib.sha256(raw).hexdigest()})
    )
    from deploy_workflow.handoff_delivery import ModelDelivery

    layout = ModelDelivery.model_validate_json(
        json.dumps(
            {
                "periods": {
                    "FY2024": {
                        "start_date": "2024-01-01",
                        "end_date": "2024-12-31",
                        "balance_column": None,
                    }
                },
                "anchors": {"dashboard": "### T4.10 dashboard"},
                "rows": {"revenue": {"table": "dashboard", "label": "Revenue"}},
            }
        )
    )
    with pytest.raises(ValueError, match="unsupported source spelling 12x"):
        _AnnualReader(raw, spec, layout).read("revenue", "FY2024")
