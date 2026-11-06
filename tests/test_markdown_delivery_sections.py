"""Synthetic regressions for what a routed section carries across the handoff boundary.

Scope: hand-written CP-1B handoffs through markdown_files; no retained model response and no
analytical run. Expected texts are written out from the handoff text below, not computed.
"""

import hashlib
import json
from pathlib import Path

from deploy_vii.report_view import ReportView
from deploy_workflow.handoff_delivery import DeliveryRequest
from deploy_workflow.markdown_delivery import markdown_files

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
