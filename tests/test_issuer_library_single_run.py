"""single_run: the walk's per-run expectations, read from a run's own files, equal the key."""

import json
import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DESIGNS = ROOT / "apps/issuer-library/designs"
sys.path.insert(0, str(DESIGNS))
import single_run

FOLDER = "cpos-launch-cp2-reader-001"
KEY = json.loads((DESIGNS / "single-run-answer-key.json").read_text())


@pytest.fixture(scope="module")
def found(tmp_path_factory: pytest.TempPathFactory) -> dict:
    ws = tmp_path_factory.mktemp("ws")
    (ws / "runs").mkdir()
    shutil.copytree(ROOT / "runs" / FOLDER, ws / "runs" / FOLDER)  # the source stays read-only
    return single_run.expectations(ws, FOLDER)


def test_run_values_equal_the_key(found: dict) -> None:
    run = KEY["run"]
    assert found["folder_id"] == run["folder_id"]["value"]
    assert found["run_id"] == found["view_run_id"] == run["run_id"]["value"]
    for name, got in (
        ("issuer_name", "issuer_name"),
        ("as_of", "as_of"),
        ("pathway", "pathway"),
        ("title", "pathway_title"),
        ("requested_modules", "requested_modules"),
        ("scope", "scope_text"),
    ):
        assert found[name] == run[got]["value"], name
    assert [m["module_id"] for m in found["modules"]] == run["run_modules_in_order"]["value"]


def test_modules_and_delivery_equal_the_key(found: dict) -> None:
    for row, module in zip(found["modules"], KEY["modules"], strict=True):
        assert row["module_id"] == module["module_id"]
        assert row["title"] == module["title"]["value"]
        assert row["status"] == module["status"]["value"]
        assert row["facts"] == module["fact_count_in_view"]["value"]
        assert found["handoffs"][f"{row['module_id']}.md"] == module["handoff_sha256"]["value"]
    assert found["delivery_id"] == KEY["delivery"]["delivery_id"]["value"]
    built = KEY["delivery"]["built_from_files"]["value"]
    assert found["handoffs"] == {n: h for n, h in built.items() if n.startswith("CP-")}
    assert all(found["handoff_bytes_match"].values())


def test_evidence_line_equals_the_key(found: dict) -> None:
    want = KEY["evidence"]
    got = found["evidence"][0]
    assert got["module"] == want["handoff"]["value"]
    assert got["file"] == want["cited_source_name"]["value"]
    assert got["locator"] == want["locator"]["value"]
    assert got["line_text"] == got["quote"] == want["line_text"]["value"]
    assert got["source_sha256"] == want["cited_source_sha256"]["value"]
    assert got["key"] == f"{FOLDER}/deliveries/{found['delivery_id']}/CP-2.md:9"
    assert len({e["key"] for e in found["evidence"]}) == len(found["evidence"])


def test_the_fixture_records_no_events_and_no_spend(found: dict) -> None:
    activity = KEY["activity"]
    assert activity["events_jsonl_present"]["value"] is False
    assert found["activity"] == {"events": None, "spent_usd": None}  # missing is not zero


def test_a_missing_delivery_or_file_is_named_not_defaulted(tmp_path: Path) -> None:
    (tmp_path / "runs" / "r").mkdir(parents=True)
    with pytest.raises(single_run.Unreadable, match="cannot read"):
        single_run.expectations(tmp_path, "r")
    (tmp_path / "runs" / "r" / "workflow.json").write_text("{}")
    with pytest.raises(single_run.Unreadable, match="expected one delivery"):
        single_run.expectations(tmp_path, "r")


def test_events_and_spend_come_from_the_runs_own_log_and_status(tmp_path: Path) -> None:
    run = tmp_path / "runs" / "web-1"
    run.mkdir(parents=True)
    (run / "events.jsonl").write_text('{"event": "module_started"}\n{"event": "delivered"}\n')
    (tmp_path / "intake/a").mkdir(parents=True)
    (tmp_path / "intake/a/status.json").write_text('{"run_id": "web-1", "spent_usd": "0.0005"}')
    (tmp_path / "intake/b").mkdir()
    (tmp_path / "intake/b/status.json").write_text('{"run_id": "web-2", "spent_usd": "9"}')
    found = single_run.activity_of(tmp_path, run)
    assert [e["event"] for e in found["events"]] == ["module_started", "delivered"]
    assert found["spent_usd"] == "0.0005"
