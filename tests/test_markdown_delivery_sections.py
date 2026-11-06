"""Synthetic regressions for what a routed section carries across the handoff boundary.

Scope: hand-written CP-1B handoffs through markdown_files; no retained model response and no
analytical run. Expected texts are written out from the handoff text below, not computed.
"""

import hashlib
import json
from pathlib import Path

import pytest

from deploy_vii.contracts import Run
from deploy_vii.report_view import ReportView
from deploy_workflow.handoff_delivery import DeliveryRequest
from deploy_workflow.markdown_delivery import markdown_files, require_issuer

TAIL = "## Calculations\nNone.\n## Gaps\nNone.\n## Next module\nDelivery.\n"


def handoff(request: str, findings: str, tail: str = TAIL) -> str:
    return (
        "# CP-1B TransDigm Group Incorporated\n## Request\n"
        + request
        + "\n## Sources\nNone.\n## Findings\n"
        + findings
        + "\n"
        + tail
    )


def deliver(tmp_path: Path, text: str, routes: list[dict]) -> dict:
    raw = text.encode()
    path = tmp_path / "CP-1B.md"
    path.write_bytes(raw)
    request = DeliveryRequest.model_validate_json(
        json.dumps(
            {
                "run": {
                    "run_id": "r1",
                    "issuer_id": "TDG",
                    "issuer_name": "TransDigm Group Incorporated",
                    "as_of": "2024-12-28",
                    "case_kind": "public",
                    "pathway": "earnings_update",
                    "requested_modules": ["CP-1B"],
                },
                "handoffs": {
                    "CP-1B": {"path": str(path), "sha256": hashlib.sha256(raw).hexdigest()}
                },
                "layout": {
                    "blocks": ["headline-results"],
                    "routes": [
                        {"module_id": "CP-1B", "block_id": "headline-results", **r} for r in routes
                    ],
                    "scope": "synthetic regression",
                },
            }
        )
    )
    files = markdown_files(request, Path("/"))
    report = ReportView.model_validate_json(files["report-view.json"])
    return {"block": report.blocks[0], "files": files}


TABLE = "| Metric | FY2023 | FY2024 |\n|---|---:|---:|\n| Revenue | 1,000.5 | 1,200.0 |\n"
ROUTE = {"heading": "Financials", "kind": "table", "table_header": "Metric", "label": "Financials"}


def test_unit_and_limitation_sentences_of_the_routed_section_stay_with_the_table(tmp_path):
    # Hand-derived: the section's two paragraphs, one before and one after the table, are
    # joined in handoff order after the route label; the table is untouched.
    findings = (
        "### Financials\nAll amounts in EUR thousands.\n\n"
        + TABLE
        + "\nFY2024 is unaudited,\nsubject to restatement.\n"
    )
    got = deliver(tmp_path, handoff("Scope.", findings), [ROUTE])["block"]
    assert got.note == (
        "Financials · All amounts in EUR thousands. FY2024 is unaudited, subject to restatement."
    )
    assert got.columns == ("FY2023", "FY2024")
    assert [[c.text for c in r.cells] for r in got.rows] == [["1,000.5", "1,200.0"]]


def test_section_prose_is_not_removed_from_the_cited_evidence(tmp_path):
    findings = "### Financials\nAll amounts in EUR thousands.\n\n" + TABLE
    files = deliver(tmp_path, handoff("Scope.", findings), [ROUTE])["files"]
    view = json.loads(files["view.json"])
    facts = [f for m in view["modules"] for f in m["facts"] if f["table_id"].startswith("prose-")]
    cited = {f["text"]: [c["quote"] for c in f["citations"]] for f in facts}
    assert cited["All amounts in EUR thousands."] == ["All amounts in EUR thousands."]


def test_same_heading_in_two_sections_takes_only_its_own_prose(tmp_path):
    # Two "### Values" headings with different tables: each note holds its own section's line.
    findings = "### Values\nUnit one: USD millions.\n\n| Metric | A |\n|---|---|\n| X | 1 |\n"
    tail = (
        "## Calculations\n### Values\nUnit two: EUR thousands.\n\n"
        "| Item | B |\n|---|---|\n| Y | 2 |\n## Gaps\nNone.\n## Next module\nDelivery.\n"
    )
    text = handoff("Scope.", findings, tail)
    route = {"heading": "Values", "kind": "table", "table_header": "Metric"}
    assert deliver(tmp_path, text, [route])["block"].note == "Unit one: USD millions."
    route["table_header"] = "Item"
    assert deliver(tmp_path, text, [route])["block"].note == "Unit two: EUR thousands."


def test_table_section_without_prose_has_only_the_route_label(tmp_path):
    got = deliver(tmp_path, handoff("Scope.", "### Financials\n" + TABLE), [ROUTE])["block"]
    assert got.note == "Financials"
    unlabelled = {k: v for k, v in ROUTE.items() if k != "label"}
    got = deliver(tmp_path, handoff("Scope.", "### Financials\n" + TABLE), [unlabelled])["block"]
    assert got.note is None


PARAGRAPHS = "Earnings view: first.\n\nEarnings view: second.\n\nScope note, not selected.\n"
PROSE = {"heading": "Request", "kind": "prose", "prefix": "Earnings view"}


def test_partial_row_selection_is_one_register_not_one_tab_per_row(tmp_path):
    # Hand-derived: two of three paragraphs match, so they form the block's one register of two
    # rows in handoff order; the third paragraph is not shown here (it stays in Evidence).
    findings = "### Financials\n" + TABLE
    got = deliver(tmp_path, handoff(PARAGRAPHS, findings), [{**PROSE, "label": "View"}])["block"]
    assert got.tabs == () and got.tab_label is None
    assert [[c.text for c in r.cells] for r in got.rows] == [
        ["Earnings view: first."],
        ["Earnings view: second."],
    ]
    assert got.note == "View"


def test_two_partial_routes_with_different_labels_stay_two_tabs(tmp_path):
    text = handoff("Alpha one.\n\nBeta one.\n\nAlpha two.\n", "### Financials\n" + TABLE)
    routes = [
        {"heading": "Request", "kind": "prose", "prefix": "Alpha", "label": "A"},
        {"heading": "Request", "kind": "prose", "prefix": "Beta", "label": "B"},
    ]
    got = deliver(tmp_path, text, routes)["block"]
    assert got.tab_label == "A" and [t.label for t in got.tabs] == ["B"]
    assert [[c.text for c in r.cells] for r in got.rows] == [["Alpha one."], ["Alpha two."]]
    assert [[c.text for c in r.cells] for r in got.tabs[0].rows] == [["Beta one."]]


def test_full_selection_still_binds_the_whole_table(tmp_path):
    text = handoff("Earnings view: first.\n\nEarnings view: second.\n", "### Financials\n" + TABLE)
    got = deliver(tmp_path, text, [{**PROSE, "label": "View"}])["block"]
    assert got.tabs == ()
    assert [r.cells[0].text for r in got.rows] == [
        "Earnings view: first.",
        "Earnings view: second.",
    ]


def test_unselected_prefix_still_refuses(tmp_path):
    text = handoff("Other.\n", "### Financials\n" + TABLE)
    with pytest.raises(ValueError, match="markdown_selector"):
        deliver(tmp_path, text, [PROSE])


def test_two_routes_on_one_table_with_one_label_share_a_register_in_route_order(tmp_path):
    # Hand-derived: rows follow route order (Gamma route first), and no row is shown twice.
    text = handoff("Alpha one.\n\nGamma one.\n\nAlpha two.\n\nBeta.\n", "### Financials\n" + TABLE)
    routes = [
        {"heading": "Request", "kind": "prose", "prefix": "Gamma"},
        {"heading": "Request", "kind": "prose", "prefix": "Alpha"},
    ]
    got = deliver(tmp_path, text, routes)["block"]
    assert got.tabs == ()
    assert [r.cells[0].text for r in got.rows] == ["Gamma one.", "Alpha one.", "Alpha two."]


# Second-model review adversarial cases. Expected values are written out from the handoff text.


def test_two_tables_in_one_section_carry_its_sentences_once(tmp_path):
    # Both registers sit under one "### Financials": its two paragraphs appear once, in handoff
    # order, after the route labels; nothing is repeated per tab.
    findings = (
        "### Financials\nAmounts in USD millions.\n\n"
        + TABLE
        + "\nRatios are historical.\n\n| Item | FY2024 |\n|---|---:|\n| Cover | 2.5x |\n"
    )
    routes = [
        {"heading": "Financials", "kind": "table", "table_header": "Metric", "label": "P"},
        {"heading": "Financials", "kind": "table", "table_header": "Item", "label": "Q"},
    ]
    got = deliver(tmp_path, handoff("Scope.", findings), routes)["block"]
    assert got.tab_label == "P" and [t.label for t in got.tabs] == ["Q"]
    assert got.note == "P · Q · Amounts in USD millions. Ratios are historical."
    assert [[c.text for c in r.cells] for r in got.tabs[0].rows] == [["2.5x"]]


def test_tables_from_two_sections_keep_route_order_in_the_note(tmp_path):
    findings = (
        "### Financials\nAmounts in USD millions.\n\n"
        + TABLE
        + "\n### Cover\nCover uses cash interest.\n\n"
        + "| Item | FY2024 |\n|---|---:|\n| Cover | 2.5x |\n"
    )
    routes = [
        {"heading": "Cover", "kind": "table", "table_header": "Item", "label": "Q"},
        {"heading": "Financials", "kind": "table", "table_header": "Metric", "label": "P"},
    ]
    got = deliver(tmp_path, handoff("Scope.", findings), routes)["block"]
    assert got.tab_label == "Q" and [t.label for t in got.tabs] == ["P"]
    # Each section's sentences are one note element; elements are joined by " · ".
    assert got.note == "Q · P · Cover uses cash interest. · Amounts in USD millions."


def test_subsection_after_the_table_is_its_own_section(tmp_path):
    # "#### Other" starts a new section: its line is not in the note and stays cited in Evidence.
    findings = "### Financials\n**USD millions.**\n\n" + TABLE + "\n#### Other\nUnrelated line.\n"
    out = deliver(tmp_path, handoff("Scope.", findings), [ROUTE])
    assert out["block"].note == "Financials · USD millions."
    view = json.loads(out["files"]["view.json"])
    facts = [f for m in view["modules"] for f in m["facts"]]
    texts = [f["text"] for f in facts if f["table_id"].startswith("prose-")]
    assert "Unrelated line." in texts and "USD millions." in texts


def test_merged_register_rows_keep_their_own_citations(tmp_path):
    # Request lines: 3 Alpha one, 5 Beta one, 7 Gamma one, 9 Alpha two, 11 Omega.
    # Routes Alpha->X, Beta->Y, Gamma->X: X holds Alpha one, Alpha two, Gamma one (route order);
    # Y holds Beta one. Each cell cites its own paragraph line.
    request = "Alpha one.\n\nBeta one.\n\nGamma one.\n\nAlpha two.\n\nOmega.\n"
    routes = [
        {"heading": "Request", "kind": "prose", "prefix": "Alpha", "label": "X"},
        {"heading": "Request", "kind": "prose", "prefix": "Beta", "label": "Y"},
        {"heading": "Request", "kind": "prose", "prefix": "Gamma", "label": "X"},
    ]
    out = deliver(tmp_path, handoff(request, "### Financials\n" + TABLE), routes)
    got = out["block"]
    assert got.tab_label == "X" and [t.label for t in got.tabs] == ["Y"]
    assert got.note == "X · Y"
    report = json.loads(out["files"]["report-view.json"])
    fact_of = {ref: e["coord"]["fact_id"] for e in report["index"]["facts"] for ref in e["ref_ids"]}
    view = json.loads(out["files"]["view.json"])
    line_of = {
        f["fact_id"]: [c["locator"] for c in f["citations"]]
        for m in view["modules"]
        for f in m["facts"]
    }

    def shown(rows):
        return [(r.cells[0].text, line_of[fact_of[r.cells[0].ref_id]]) for r in rows]

    assert shown(got.rows) == [
        ("Alpha one.", ["line 3"]),
        ("Alpha two.", ["line 9"]),
        ("Gamma one.", ["line 7"]),
    ]
    assert shown(got.tabs[0].rows) == [("Beta one.", ["line 5"])]


def test_one_label_on_two_different_tables_still_refuses(tmp_path):
    # The merge is per table: the same label on registers of two tables is a real clash.
    findings = "### Financials\nAlpha f.\n\nOther f.\n\n" + TABLE
    routes = [
        {"heading": "Request", "kind": "prose", "prefix": "Alpha", "label": "X"},
        {"heading": "Financials", "kind": "prose", "prefix": "Alpha", "label": "X"},
    ]
    with pytest.raises(ValueError, match="Tab labels are distinct"):
        deliver(tmp_path, handoff("Alpha r.\n\nBeta r.\n", findings), routes)


ISSUER_RUN = Run.model_validate_json(
    json.dumps(
        {
            "run_id": "r1",
            "issuer_id": "FRD",
            "issuer_name": "Ford",
            "as_of": "2024-12-28",
            "case_kind": "public",
            "pathway": "earnings_update",
            "requested_modules": ["CP-1B"],
        }
    )
)


@pytest.mark.parametrize(
    ("issuer", "aliases", "title", "body"),
    [
        # "Ford" is the last four letters of "Stanford" and "AB" the middle of "lab": a name
        # touching a letter on either side is another word, not this issuer.
        ("Ford", (), "# CP-1B Stanford Health Care", "Analyse Stanford bonds."),
        ("Ford", (), "# CP-1B Fordham Capital", "Analyse Fordham bonds."),
        ("Absolute Lab Inc", ("AB",), "# CP-1B Acme Corp", "Analyse Acme lab capacity."),
    ],
)
def test_issuer_name_or_alias_inside_another_word_is_refused(issuer, aliases, title, body):
    run = ISSUER_RUN.model_copy(update={"issuer_name": issuer})
    lines = [title, "## Request", body]
    with pytest.raises(ValueError, match="markdown_issuer"):
        require_issuer(run, aliases, "CP-1B", lines)


@pytest.mark.parametrize(
    ("aliases", "title", "body"),
    [
        ((), "# CP-1B Ford Motor", "x"),
        ((), "# CP-1B Analysis", "Credit view of FORD,\nthe automaker."),
        (("AB",), "# CP-1B Analysis", "AB (the issuer) reported."),
    ],
)
def test_issuer_name_or_alias_as_whole_words_is_accepted(aliases, title, body):
    lines = [title, "## Request", *body.splitlines()]
    run = ISSUER_RUN if aliases == () else ISSUER_RUN.model_copy(update={"issuer_name": "Other"})
    require_issuer(run, aliases, "CP-1B", lines)
