"""Manifest writer against the hand-written answer key (tests/fixtures/library-manifest/writer)."""

import copy
import importlib.util
import json
import shutil
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
KEYS = ROOT / "tests/fixtures/library-manifest/writer"
spec = importlib.util.spec_from_file_location(
    "library_manifest", ROOT / "apps/issuer-library/engine/library_manifest.py"
)
lm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lm)
CASES = ["synthetic", "retained", "edge"]


def workspace(case: str, tmp_path: Path) -> tuple[Path, str]:
    shutil.copytree(KEYS / case / "workspace", tmp_path, dirs_exist_ok=True)
    plan = KEYS / case / "copy.json"
    for item in json.loads(plan.read_text()) if plan.exists() else []:
        source = ROOT / item["from"]
        if not source.is_file():
            pytest.skip(f"{item['from']} is absent")
        (tmp_path / item["to"]).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, tmp_path / item["to"])
    (run_id,) = [p.name for p in (tmp_path / "runs").iterdir()]
    return tmp_path, run_id


def key(case: str) -> dict:
    return json.loads((KEYS / case / "expected-library.json").read_text())


def without_chart_rows(manifest: dict) -> dict:
    manifest = copy.deepcopy(manifest)
    manifest["run"]["metrics"] = {}
    manifest["sources"] = {k: v for k, v in manifest["sources"].items() if not k.startswith("cp1_")}
    return manifest


@pytest.mark.parametrize("case", CASES)
def test_build_matches_key_except_chart_rows(case, tmp_path):
    root, run_id = workspace(case, tmp_path)
    assert lm.build(root, run_id) == without_chart_rows(key(case))


@pytest.mark.xfail(strict=True, reason="R-24: chart-row rule awaits the owner")
@pytest.mark.parametrize("case", CASES)
def test_build_matches_full_key(case, tmp_path):
    root, run_id = workspace(case, tmp_path)
    assert lm.build(root, run_id) == key(case)


@pytest.mark.parametrize("case", CASES)
def test_row_metrics_match_key(case, tmp_path):
    root, run_id = workspace(case, tmp_path)
    expected = key(case)
    doc = lm._doc(root, f"runs/{run_id}/CP-1.md")
    tables = lm._chart_rows(doc)
    for table, rows in tables.items():
        if table not in expected["sources"]:
            continue
        pinned = expected["sources"][table]
        (row,) = [r for r in rows if r.line == pinned["line"]]
        assert lm._pin(doc, row.line) == pinned
        got = lm._row_metrics(table, row)
        want = {k: v for k, v in expected["run"]["metrics"].items() if v["source"] == table}
        assert got == want and want


def test_chosen_row_is_pending_r24():
    assert (
        lm._chosen_row([lm._Row(1, {"Period": "2025-06-30"})], "2025-06-30", "fy-2025", False)
        is None
    )


@pytest.mark.parametrize("cell", ["Not supplied: x", "-3", "abc", "1.2.3", ""])
def test_row_metrics_omit_unusable_cells(cell):
    cells = {"Period": "p", "Basis and limitation": "b", "Reporting unit": "x"}
    cells |= {"Total debt / EBITDA": cell, "Net debt / EBITDA": "1,250.5"}
    got = lm._row_metrics("cp1_leverage", lm._Row(3, cells))
    assert list(got) == ["net_leverage"] and got["net_leverage"]["value"] == "1250.5"
    assert lm._row_metrics("cp1_leverage", lm._Row(3, cells | {"Reporting unit": "US$m"})) == {}


@pytest.mark.parametrize("case", CASES)
def test_write_is_atomic_and_matches_build(case, tmp_path):
    root, run_id = workspace(case, tmp_path)
    path = lm.write(root, run_id)
    text = path.read_text(encoding="utf-8")
    assert text.endswith("}\n") and json.loads(text) == lm.build(root, run_id)
    assert sorted(p.name for p in path.parent.glob(".library-*")) == []


def test_missing_expectations_raises(tmp_path):
    root, run_id = workspace("missing-expectations", tmp_path)
    wanted = (KEYS / "missing-expectations/expected-error.txt").read_text().strip()
    with pytest.raises(lm.ManifestError, match="expectations.json") as err:
        lm.build(root, run_id)
    assert wanted in str(err.value)


def test_missing_identity_name_raises(tmp_path):
    root, run_id = workspace("synthetic", tmp_path)
    path = root / "runs" / run_id / "context.json"
    path.write_text(path.read_text().replace('"issuer_name"', '"issuer_name_x"'))
    with pytest.raises(lm.ManifestError, match="issuer_name"):
        lm.build(root, run_id)
