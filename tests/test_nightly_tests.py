"""The nightly runner splits the suite deterministically and fails only on new failures."""

from __future__ import annotations

from pathlib import Path

import pytest

from tools import nightly_tests as nightly

SIZES = {"tests/a.py": 50, "tests/b.py": 40, "tests/c.py": 30, "tests/d.py": 20, "tests/e.py": 10}


def test_shards_cover_every_file_once_with_balanced_size() -> None:
    shards = [nightly.shard_files(SIZES, 2, n) for n in range(2)]
    # Largest first onto the lightest shard: a(50)->0, b(40)->1, c(30)->1 (70), d(20)->0 (70),
    # e(10)->0 (80): shard 0 holds a, d, e; shard 1 holds b, c.
    assert shards == [["tests/a.py", "tests/d.py", "tests/e.py"], ["tests/b.py", "tests/c.py"]]
    assert sorted(name for shard in shards for name in shard) == sorted(SIZES)


def test_more_shards_than_files_leaves_empty_shards() -> None:
    assert [nightly.shard_files({"tests/a.py": 1}, 3, n) for n in range(3)] == [
        ["tests/a.py"],
        [],
        [],
    ]


def _shard(folder: Path, n: int, status: str, log: str) -> None:
    (folder / f"shard-{n}.exit").write_text(status)
    (folder / f"shard-{n}.log").write_text(log)


LOG0 = (
    "shard 0/2: 3 files\n"
    "FAILED tests/test_x.py::test_one - AssertionError: 1 != 2\n"
    "ERROR tests/product/test_y.py - ModuleNotFoundError: No module named 'scripts'\n"
    "==== 2 failed, 10 passed, 1 error in 12.50s ====\n"
)
LOG1 = "shard 1/2: 2 files\n==== 7 passed in 3.00s ====\n"


def test_report_fails_only_on_a_failure_not_on_the_known_list(tmp_path: Path) -> None:
    _shard(tmp_path, 0, "1", LOG0)
    _shard(tmp_path, 1, "0", LOG1)
    results = nightly.read_results(tmp_path)
    assert results.failures == {"tests/test_x.py::test_one", "tests/product/test_y.py"}
    assert results.summaries == {
        0: "2 failed, 10 passed, 1 error in 12.50s",
        1: "7 passed in 3.00s",
    }
    text, passed = nightly.report(results, {"tests/product/test_y.py"}, 2)
    assert not passed and "- `tests/test_x.py::test_one`" in text
    text, passed = nightly.report(results, set(results.failures) | {"tests/gone.py::t"}, 2)
    assert passed and "### Known failures now passing" in text and "tests/gone.py::t" in text


@pytest.mark.parametrize("status", ["timeout", "2", "4"])
def test_a_shard_that_did_not_finish_fails_the_run(tmp_path: Path, status: str) -> None:
    _shard(tmp_path, 0, "0", LOG1)
    _shard(tmp_path, 1, status, "shard 1/2: 2 files\n")
    text, passed = nightly.report(nightly.read_results(tmp_path), set(), 2)
    assert not passed and "1 shard(s) unfinished" in text


def test_a_missing_shard_fails_the_run(tmp_path: Path) -> None:
    _shard(tmp_path, 0, "0", LOG1)
    text, passed = nightly.report(nightly.read_results(tmp_path), set(), 2)
    assert not passed and "| 1 | missing | - |" in text


def test_known_list_ignores_comments_and_blank_lines(tmp_path: Path) -> None:
    known = tmp_path / "known.txt"
    known.write_text("# header\n\ntests/a.py::t  # why\ntests/b.py\n")
    assert nightly.known_failures(known) == {"tests/a.py::t", "tests/b.py"}
    assert nightly.known_failures(tmp_path / "absent.txt") == set()


def test_command_excludes_paid_and_browser_tests_and_keeps_going() -> None:
    command = nightly.pytest_command("python", ["tests/a.py"])
    assert command[command.index("-m", 3) + 1] == "not live and not browser"
    assert "--continue-on-collection-errors" in command and command[-1] == "tests/a.py"
    assert "tmp_path_retention_policy=failed" in command


def test_run_prints_the_log_tail_to_the_job_log(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    def fake(root: Path, shard: int, shards: int, out: Path, minutes: float) -> str:
        _shard(out, shard, "-11", "".join(f"line {n}\n" for n in range(nightly.TAIL + 5)))
        return "-11"

    monkeypatch.setattr(nightly, "run_shard", fake)
    code = nightly.main(["run", "--shard", "3", "--shards", "8", "--out", str(tmp_path)])
    printed = capsys.readouterr().out.splitlines()
    assert code == 1 and printed[-1] == "shard 3: pytest exit -11"
    assert printed[:-1] == [f"line {n}" for n in range(5, nightly.TAIL + 5)]
