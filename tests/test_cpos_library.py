"""Tests for deploy_workflow.cpos_library: library.json backfill for host-session runs."""

import hashlib
import json
import pathlib
import re

import pytest

from deploy_workflow import cpos_library as lib

ROOT = pathlib.Path(__file__).resolve().parents[1]
NUMERIC_TOKEN = re.compile(r"-?[0-9][0-9,]*(?:\.[0-9]+)?")  # apps/issuer-library/discovery.go

CONTEXT = {
    "schema": "context/1",
    "run": {
        "pathway": "credit_snapshot",
        "as_of": "2026-11-05",
        "current_period": "q3-2026",
        "reporting_currency": "USD",
    },
    "identity": {
        "issuer_name": "EXAMPLE PARTS INC /DE/",
        "issuer_id": "exp",
        "ticker": "EXP",
        "sector": "Retail-Auto & Home Supply Stores",
    },
}
CP1 = """## Request

Module CP-1 for EXAMPLE PARTS INC.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Cash exceeds debt. | Medium | EBITDA includes restructuring charges. |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2026 guidance midpoint, indicative | 5.00 | 4.00 | x | Management guidance. |
| LTM Oct 10, 2026 | 6.67 | 0.60 | x | Derived LTM EBITDA of 508; debt 3,388. |
| FY2025 | 14.90 | 1.26 | x | Reported EBITDA of 229. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 3.01 | x | Reported EBITDA of 229 over interest paid of 76. |
| LTM Oct 10, 2026 | Not supplied: interest paid is not printed | x | No cash interest figure. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q3 FY2026 | 3,085 | 894 | US$m | Cash at October 10, 2026. |
| Q2 FY2026 | 3120 | 894 | US$m | Cash at July 18, 2026. |
| FY2025 | 3123 | 896 | US$m | Cash at January 3, 2026. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 (53 weeks) | Q3 FY2026 (12 weeks) | LTM Oct 10, 2026 |
| --- | --- | --- | --- |
| Net sales | 8,601 | 2,012 | 8,599 |
| EBITDA (operating income plus D&A, derived) | 229 | 105 | 508 |
| EBITDA / interest paid (x) | 3.01 | n/a | 2.54 |
| Net cash from operating activities | (46) | 59 | (12) |
"""
CP2 = """## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Liquidity is strong but earnings are thin. | Medium | No debt agreements were supplied. |
"""


def make_run(
    tmp_path: pathlib.Path, run_id: str = "cpos-swarm-test-exp", delivery: bool = True
) -> pathlib.Path:
    run = tmp_path / "runs" / run_id
    (run / "inputs").mkdir(parents=True)
    raw = json.dumps(CONTEXT, indent=2).encode()
    (run / "inputs" / hashlib.sha256(raw).hexdigest()).write_bytes(raw)
    (run / "inputs" / ("0" * 64)).write_bytes(b'{"schema": "other"}')
    (run / "identity.json").write_text(json.dumps({"run": {"issuer_id": "exp"}}))
    if delivery:
        folder = run / "deliveries" / ("d" * 64)
        folder.mkdir(parents=True)
        (folder / "CP-1.md").write_text(CP1, encoding="utf-8")
        (folder / "CP-2.md").write_text(CP2, encoding="utf-8")
    return run


def verify_like_the_library(root: pathlib.Path, manifest: dict) -> None:
    """The checks admitRun makes on sources and metrics, in apps/issuer-library/discovery.go."""
    sources = manifest["sources"]
    for source in sources.values():
        assert source["path"].startswith("runs/")
        raw = (root / source["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == source["sha256"]
        lines = raw.decode().replace("\r\n", "\n").split("\n")
        assert lines[source["line"] - 1] == source["quote"]
    run = manifest["run"]
    assert run["identity_source"] in sources
    if run["sector"] != "Unclassified":
        assert run["sector_source"] in sources
    for metric in run["metrics"].values():
        if metric is None:
            continue
        float(metric["value"])
        assert metric["unit"] and metric["period"] and metric["basis"]
        quote = sources[metric["source"]]["quote"]
        assert metric["value"] in [t.replace(",", "") for t in NUMERIC_TOKEN.findall(quote)]
        assert "provenance" not in metric


def test_manifest_pins_identity_and_latest_reported_periods(tmp_path):
    run = make_run(tmp_path)
    manifest = lib.build_manifest(run, {})
    verify_like_the_library(tmp_path, manifest)
    record = manifest["run"]
    assert record["id"] == "cpos-swarm-test-exp" and record["issuer"] == "exp"
    assert record["name"] == "Example Parts Inc"  # recased; the /DE/ suffix dropped
    assert record["sector"] == "Retail-Auto & Home Supply Stores"
    assert manifest["sources"]["context"]["quote"] == '    "issuer_name": "EXAMPLE PARTS INC /DE/",'
    assert manifest["sources"]["sector"]["line"] > manifest["sources"]["context"]["line"]
    assert record["date"] == "2026-11-05" and record["currency"] == "USD"
    assert record["period"] == "Q3 FY2026"  # the latest liquidity row, not the last one
    assert record["handoff"].endswith("/CP-2.md")
    assert record["summary"].startswith("Liquidity is strong but earnings are thin. ")
    assert "EXAMPLE PARTS INC /DE/" in record["summary"]
    assert manifest["checklist"] is None
    metrics = record["metrics"]
    # Guidance rows never count; the LTM row outranks FY2025 even though it is not the last row.
    assert (metrics["leverage"]["value"], metrics["leverage"]["period"]) == (
        "6.67",
        "LTM Oct 10, 2026",
    )
    # The latest period's cover cell is not a number, so the reported FY2025 cover is taken.
    assert (metrics["coverage"]["value"], metrics["coverage"]["period"]) == ("3.01", "FY2025")
    assert (metrics["cash"]["value"], metrics["cash"]["unit"]) == ("3085", "US$m")
    assert metrics["revenue"] == {
        "value": "8599",
        "unit": "US$m",
        "period": "LTM Oct 10, 2026",
        "basis": "Net sales, as the CP-1 table prints it.",
        "source": "cp1-revenue",
    }
    assert metrics["ebitda"]["value"] == "508"
    # A bracketed negative is not a token the library can match: null, never a wrong sign or zero.
    assert metrics["cashflow"] is None
    assert record["gaps"][0].startswith("Host session")
    assert "CP-1 main limitation: EBITDA includes restructuring charges." in record["gaps"]


def test_stopped_run_without_delivery_keeps_identity_only(tmp_path):
    run = make_run(tmp_path, "cpos-swarm-test-stop", delivery=False)
    manifest = lib.build_manifest(run, {})
    verify_like_the_library(tmp_path, manifest)
    record = manifest["run"]
    assert set(record["metrics"].values()) == {None}
    assert "handoff" not in record
    assert record["period"] == "q3-2026"
    assert "Stopped before publication: no report was delivered from this run." in record["gaps"]


def test_unit_must_be_explicit_for_table_metrics(tmp_path):
    run = make_run(tmp_path)
    cp1 = next(run.glob("deliveries/*/CP-1.md"))
    cp1.write_text(CP1.replace("| Metric (US$m unless stated) |", "| Metric |"), encoding="utf-8")
    metrics = lib.build_manifest(run, {})["run"]["metrics"]
    assert metrics["revenue"] is None and metrics["ebitda"] is None
    assert metrics["cash"]["value"] == "3085"  # the chart table states its unit


def test_long_format_table_prefers_whole_periods(tmp_path):
    run = make_run(tmp_path)
    cp1 = next(run.glob("deliveries/*/CP-1.md"))
    long = CP1.split("### Financials and credit metrics")[0] + (
        "### Financials and credit metrics\n\n"
        "| Metric | Period | Value | Unit | Kind | Source |\n| --- | --- | --- | --- | --- | --- |\n"
        "| Net sales | Nine months 2026 | 11,003,672 | USD thousands | Reported | Q3 page:2 |\n"
        "| Net sales | FY2025 | 15,190,638 | USD thousands | Reported | K10 page:71 |\n"
        "| Net sales | Q3 2026 | 3,854,048 | USD thousands | Reported | Q3 page:2 |\n"
    )
    cp1.write_text(long, encoding="utf-8")
    revenue = lib.build_manifest(run, {})["run"]["metrics"]["revenue"]
    assert (revenue["value"], revenue["unit"], revenue["period"]) == (
        "15190638",
        "USD thousands",
        "FY2025",
    )


@pytest.mark.parametrize(
    ("registrant", "funds", "expected", "how"),
    [
        ("Mativ Holdings, Inc.", [], "Mativ Holdings, Inc.", "context"),
        (
            "AMERICAN AIRLINES, INC.",
            ["AMERICAN AIRLINES INC", "American Airlines Inc", "American Airlines, Inc."],
            "American Airlines, Inc.",
            "funds",
        ),
        (
            "COLUMBUS MCKINNON CORP",
            ["Columbus McKinnon Corporation"],
            "Columbus McKinnon Corporation",
            "funds",
        ),
        ("GRAY MEDIA, INC", ["Gray Television, Inc."], "Gray Media, Inc", "recased"),
        ("DXP ENTERPRISES INC", [], "DXP Enterprises Inc", "recased"),
        ("GENESIS ENERGY LP", [], "Genesis Energy LP", "recased"),
        (
            "CHARLES RIVER LABORATORIES INTERNATIONAL, INC.",
            [],
            "Charles River Laboratories International, Inc.",
            "recased",
        ),
        ("WHIRLPOOL CORP /DE/", [], "Whirlpool Corp", "recased"),
        ("CLEVELAND-CLIFFS INC.", [], "Cleveland-Cliffs Inc.", "recased"),
        ("GENMAB A/S", [], "Genmab A/S", "recased"),
        ("MURPHY OIL CORP", [], "Murphy Oil Corp", "recased"),
        ("PRA GROUP INC", [], "PRA Group Inc", "recased"),
        ("VSE CORP", [], "VSE Corp", "recased"),
    ],
)
def test_display_names(registrant, funds, expected, how):
    assert lib.display_name(registrant, funds) == (expected, how)


@pytest.mark.parametrize(
    ("label", "rank"),
    [
        ("FY2026", (2026, 12, 0)),
        ("Q2 FY2027 (September 30, 2026)", (2026, 9, 0)),
        ("Q2 FY2027", (2027, 6, 0)),
        ("FY2026 (year to Mar 31, 2026)", (2026, 3, 0)),
        ("TTM to Sep 30, 2026 (calculated)", (2026, 9, 1)),
        ("LTM Q3 2026", (2026, 9, 1)),
        ("Q1 2026 (March 31, 2026)", (2026, 3, 0)),
        ("LTM to 2026-09-30", (2026, 9, 1)),
        ("FY2025 (31 Dec 2025)", (2025, 12, 0)),
        ("Nine months 2026", (2026, 9, 0)),
        ("LTM Q2 2027 (53 weeks to Aug 1, 2026)", (2026, 8, 1)),
    ],
)
def test_period_rank(label, rank):
    assert lib.period_rank(label) == rank


def test_main_writes_once_and_check_notices_a_change(tmp_path, capsys):
    run = make_run(tmp_path)
    assert lib.main([str(run)]) == 0
    target = run / "library.json"
    first = target.read_bytes()
    assert json.loads(first)["schema"] == "issuer-library-run/1"
    assert lib.main([str(run)]) == 0 and target.read_bytes() == first
    assert "exists cpos-swarm-test-exp" in capsys.readouterr().out
    assert lib.main(["--check", str(run)]) == 0
    next(run.glob("deliveries/*/CP-2.md")).write_text(
        CP2.replace("thin", "thick"), encoding="utf-8"
    )
    assert lib.main(["--check", str(run)]) == 1
    assert target.read_bytes() == first
    assert "DIFF cpos-swarm-test-exp" in capsys.readouterr().out


def test_context_and_identity_must_agree(tmp_path):
    run = make_run(tmp_path)
    (run / "identity.json").write_text(json.dumps({"run": {"issuer_id": "other"}}))
    with pytest.raises(lib.ManifestError, match="different issuers"):
        lib.build_manifest(run, {})


@pytest.mark.skipif(
    not (ROOT / "runs/cpos-swarm-20261105-aap/library.json").is_file(), reason="retained run absent"
)
def test_retained_swarm_manifest_matches_its_files():
    run = ROOT / "runs/cpos-swarm-20261105-aap"
    manifest = json.loads((run / "library.json").read_text(encoding="utf-8"))
    verify_like_the_library(ROOT, manifest)
    assert (
        manifest == lib.build_manifest(run, {})
        or manifest["run"]["name"] == "Advance Auto Parts Inc"
    )
    assert manifest["run"]["metrics"]["leverage"]["value"] == "6.67"


def test_unit_comes_from_a_note_column_or_the_line_above_the_table(tmp_path):
    run = make_run(tmp_path)
    cp1 = next(run.glob("deliveries/*/CP-1.md"))
    head = CP1.split("### Financials and credit metrics")[0]
    noted = head + (
        "### Financials and credit metrics\n\n"
        "| Metric | FY2025 | 9M 2026 | Basis, unit and locator |\n| --- | --- | --- | --- |\n"
        "| Net sales | 3,010 | 4,506 | US$m, reported; S1 page:80 |\n"
        "| Depreciation and amortization (EBITDA basis) | 88 | 70 | US$m |\n"
        "| Adjusted EBITDA, company-defined | 1,130 | 1,166 | US$m, non-GAAP as reported |\n"
    )
    cp1.write_text(noted, encoding="utf-8")
    metrics = lib.build_manifest(run, {})["run"]["metrics"]
    assert (metrics["revenue"]["value"], metrics["revenue"]["unit"]) == ("3010", "US$m")
    # The depreciation row names EBITDA only in a note: the EBITDA row is the one taken.
    assert metrics["ebitda"]["value"] == "1130"
    preamble = head + (
        "### Financials and credit metrics\n\nAmounts in USD thousands unless the row says x.\n\n"
        "| Line | Period | Amount | Unit | Type |\n| --- | --- | --- | --- | --- |\n"
        "| Revenues, net | FY2025 | 2,311,801 | USD thousands | Reported |\n"
        "| Revenues, net | LTM Jun 2026 | 2,246,166 | USD thousands | Calculated |\n"
        "| Revenues, net | Q2 2026 | 547,495 | USD thousands | Reported |\n"
    )
    cp1.write_text(preamble, encoding="utf-8")
    revenue = lib.build_manifest(run, {})["run"]["metrics"]["revenue"]
    assert (revenue["value"], revenue["period"]) == ("2246166", "LTM Jun 2026")


@pytest.mark.parametrize(
    ("label", "is_ebitda"),
    [
        ("Adjusted EBITDA (management, non-GAAP)", True),
        ("EBITDA, derived: pretax income + interest expense + D&A (USD thousands)", True),
        ("EBITDA excluding operating special items", True),
        ("Trailing Adjusted EBITDA", True),
        ("Depreciation and amortization (EBITDA reconciliation basis)", False),
        ("Nitrogen Fertilizer segment EBITDA (equals its Adjusted EBITDA)", False),
        ("EBITDA adjustments", False),
        ("Adjusted EBITDA margin", False),
        ("Total debt / EBITDA (x)", False),
        ("Adjusted EBITDAR", False),
    ],
)
def test_ebitda_is_the_head_noun(label, is_ebitda):
    assert lib._is_metric(label, lib.EBITDA) is is_ebitda


def gate_run(tmp_path, report_view_edit=None):
    """A run with a report view whose chart and section states the gate reads."""
    run = make_run(tmp_path)
    routes = [
        {"kind": "chart", "figure_id": "S.1", "value_columns": ["Total debt / EBITDA"]},
        {"kind": "prose", "figure_id": None, "value_columns": []},
    ]
    (run / "workflow.json").write_text(
        json.dumps({"layout": {"blocks": ["key-findings", "model-chart-strip"], "routes": routes}})
    )
    cell = {"state": "known", "text": "6.67x"}
    figure = {
        "fig_id": "S.1",
        "chart": {
            "table_twin": {"rows": [{"label": "Total debt / EBITDA · LTM", "cells": [cell]}]}
        },
    }
    view = {
        "blocks": [
            {"block_id": "key-findings", "state": "populated", "figures": []},
            {"block_id": "model-chart-strip", "state": "populated", "figures": [figure]},
        ]
    }
    if report_view_edit:
        report_view_edit(view)
    (next(run.glob("deliveries/*")) / "report-view.json").write_text(json.dumps(view))
    return run


def test_sections_and_charts_pass_when_every_series_is_plotted(tmp_path):
    assert lib._sections_and_charts(gate_run(tmp_path)) == []


def test_a_chart_series_of_not_supplied_cells_fails(tmp_path):
    def empty(view):
        rows = view["blocks"][1]["figures"][0]["chart"]["table_twin"]["rows"]
        rows[0]["cells"] = [{"state": "known", "text": "Not supplied: reported in CAD millions"}]

    assert lib._sections_and_charts(gate_run(tmp_path, empty)) == [
        "chart S.1 has no value for Total debt / EBITDA"
    ]


def test_an_unpopulated_section_or_undrawn_chart_fails(tmp_path):
    def gaps(view):
        view["blocks"][0]["state"] = "empty"
        view["blocks"][1]["figures"] = []

    assert lib._sections_and_charts(gate_run(tmp_path, gaps)) == [
        "section key-findings is not populated",
        "chart S.1 is not drawn",
    ]


@pytest.mark.skipif(
    not (ROOT / "runs/cpos-swarm-20261105-aap/workflow.json").is_file(),
    reason="retained run absent",
)
def test_a_retained_swarm_run_passes_the_whole_gate():
    assert lib.gate(ROOT / "runs/cpos-swarm-20261105-aap", {}) == []


def test_changed_instructions_are_not_the_current_method(tmp_path):
    source = ROOT / "runs/cpos-swarm-20261105-aap"
    if not (source / "workflow.json").is_file():
        pytest.skip("retained run absent")
    run = tmp_path / "runs" / source.name
    (run / "inputs").mkdir(parents=True)
    for name in ("workflow.json", "identity.json"):
        (run / name).write_bytes((source / name).read_bytes())
    context = lib._context_file(source)
    (run / "inputs" / context.name).write_bytes(context.read_bytes())
    assert lib._current_method(run) == []
    manifest = json.loads((run / "workflow.json").read_text())
    manifest["instructions"]["CP-2"]["sha256"] = "0" * 64
    (run / "workflow.json").write_text(json.dumps(manifest))
    assert lib._current_method(run) == ["CP-2 instructions are not the current launcher's"]


def packaged_runs(tmp_path, monkeypatch, count=3):
    monkeypatch.setattr(lib, "gate", lambda run_dir, fund_names: [])
    runs = [make_run(tmp_path, f"cpos-swarm-test-{i}") for i in range(count)]
    assert lib.main([str(r) for r in runs]) == 0
    return runs


def test_package_round_trips_whole_runs_in_capped_identical_parts(tmp_path, monkeypatch):
    import zipfile

    runs = packaged_runs(tmp_path, monkeypatch)
    one = lib._compressed_size(runs[0])
    parts = lib.package(runs, tmp_path / "a", one + 10, {})
    assert len(parts) == 3 and all(p.stat().st_size <= one + 10 for p in parts)
    again = lib.package(list(reversed(runs)), tmp_path / "b", one + 10, {})
    assert [p.read_bytes() for p in parts] == [p.read_bytes() for p in again]
    sums = (tmp_path / "a" / "SHA256SUMS.txt").read_text().splitlines()
    assert [line.split()[1] for line in sums] == [p.name for p in parts]
    out = tmp_path / "workspace"
    for part in parts:
        zipfile.ZipFile(part).extractall(out)
    for run in runs:
        for path in run.rglob("*"):
            if path.is_file():
                copy = out / "runs" / run.name / path.relative_to(run)
                assert copy.read_bytes() == path.read_bytes()
    assert lib.package(runs, tmp_path / "c", 10 * one, {})[0].name == "issuer-runs-part-1-of-1.zip"


def test_package_refuses_a_failing_missing_or_stale_manifest(tmp_path, monkeypatch):
    runs = packaged_runs(tmp_path, monkeypatch, count=1)
    (runs[0] / "library.json").write_text("{}")
    with pytest.raises(lib.ManifestError, match="differs from a fresh build"):
        lib.package(runs, tmp_path / "a", 10**9, {})
    (runs[0] / "library.json").unlink()
    with pytest.raises(lib.ManifestError, match="has no library.json"):
        lib.package(runs, tmp_path / "b", 10**9, {})
    monkeypatch.setattr(lib, "gate", lambda run_dir, fund_names: ["chart S.1 is not drawn"])
    with pytest.raises(lib.ManifestError, match="does not pass the gate"):
        lib.package(runs, tmp_path / "c", 10**9, {})
    assert not (tmp_path / "c").exists()
