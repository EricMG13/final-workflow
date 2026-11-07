"""The independent data-flow checker, over a synthetic two-module run in the real layout."""

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "library_flow_check", ROOT / "apps/issuer-library/designs/flow_check.py"
)
flow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(flow)

CP0 = "# CP-0\n\nRevenue was 7,940.0 and margin 12%.\n"
CP1 = "# CP-1\n\nLeverage (1,234) against 7,940 and 4.2x.\n"
SOURCE = "Revenue 7,940.0. Margin 12%. Leverage (1,234). Multiple 4.2x.\n"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def make_run(tmp_path: Path) -> tuple[Path, Path]:
    run, sources = tmp_path / "run", tmp_path / "issuer"
    sources.mkdir()
    (sources / "annual.txt").write_text(SOURCE)
    (run / "inputs").mkdir(parents=True)
    (run / "inputs" / sha(SOURCE.encode())).write_text(SOURCE)
    handoffs = {"CP-0": CP0, "CP-1": CP1}
    for module, text in handoffs.items():
        (run / f"requests/{module}/fp").mkdir(parents=True)
        (run / f"requests/{module}/fp/1.response.md").write_text(text)
        (run / "deliveries/d1").mkdir(parents=True, exist_ok=True)
        (run / f"deliveries/d1/{module}.md").write_text(text)
    modules = {m: f"requests/{m}/fp/1.response.md" for m in handoffs}
    (run / "completed-abc.json").write_text(json.dumps({"modules": modules}))
    for module, upstream in (("CP-0", {}), ("CP-1", {"CP-0": CP0})):
        folder = run / "live/modules" / sha(module.encode())
        folder.mkdir(parents=True)
        request = {
            "module_id": module,
            "sources": {"annual.txt": sha(SOURCE.encode())},
            "handoffs": {
                u: {"sha256": sha(t.encode()), "markdown": t} for u, t in upstream.items()
            },
        }
        (folder / "0.request.json").write_text(
            json.dumps({"messages": [{}, {"text": json.dumps(request)}]})
        )
        tools = [{"call_id": "1", "name": "read_pages", "text": SOURCE}]
        tools.append({"call_id": "2", "name": "write_handoff", "text": "999,999"})
        (folder / "0.tools.json").write_text(json.dumps(tools))
    return run, sources


def test_numbers_normalises_and_ignores_digests_and_dates() -> None:
    assert flow.numbers("7,940.0") == {"7940"}
    assert flow.numbers("(1,234)") == {"1234"}
    assert flow.numbers("-3.50") == {"3.5"}
    assert flow.numbers("12%") == {"12"}
    assert flow.numbers("leverage 4.2x") == {"4.2"}
    assert (
        flow.numbers(
            "sha256 " + "ab12" * 16 + " on 2024-09-30 in report-v2.md and tdg-20240930.htm"
        )
        == set()
    )
    # Identifiers and lists are not quantities: run-20261105, a page list, a leading-zero label.
    assert flow.numbers("run-20261105 pp.38,54,106,109 OP01-02 057") == set()
    assert flow.numbers("1,198 | 1,057 and 2.5-3.0x") == {"1198", "1057", "2.5"}
    assert flow.numbers("see pp.3,105\u2013109,131,146 and p.35") == set()
    assert flow.numbers("sum(980,161)=1141 and Pp.52\u201354,106,109,142") == {"980", "161", "1141"}
    assert flow.numbers("as of 31 March 2025 and Mar 31, 2025 and 2,025") == {"2025"}
    assert flow.numbers("7 and 0.0 and 12") == {"12"}


def test_clean_synthetic_run_has_no_faults(tmp_path: Path) -> None:
    run, sources = make_run(tmp_path)
    assert flow.run_faults(run, sources) == []


def test_number_absent_from_what_the_module_read_is_a_fault(tmp_path: Path) -> None:
    run, sources = make_run(tmp_path)
    path = run / "requests/CP-1/fp/1.response.md"
    path.write_text(CP1 + "Planted 7,941.\n")
    (run / "deliveries/d1/CP-1.md").write_text(CP1 + "Planted 7,941.\n")
    faults = flow.run_faults(run, sources)
    assert len(faults) == 1 and "CP-1" in faults[0] and "7941" in faults[0]


def test_write_handoff_text_is_not_evidence(tmp_path: Path) -> None:
    run, sources = make_run(tmp_path)
    path = run / "requests/CP-1/fp/1.response.md"
    path.write_text(CP1 + "Only in the draft 999,999.\n")
    (run / "deliveries/d1/CP-1.md").write_text(path.read_text())
    assert any("999999" in f for f in flow.run_faults(run, sources))


def test_upstream_hash_mismatch_is_a_fault(tmp_path: Path) -> None:
    run, sources = make_run(tmp_path)
    for file in (run / "live/modules").glob("*/0.request.json"):
        outer = json.loads(file.read_text())
        request = json.loads(outer["messages"][1]["text"])
        if request["module_id"] == "CP-1":
            request["handoffs"]["CP-0"]["sha256"] = "0" * 64
            outer["messages"][1]["text"] = json.dumps(request)
            file.write_text(json.dumps(outer))
    faults = flow.run_faults(run, sources)
    assert len(faults) == 1 and "CP-1" in faults[0] and "CP-0" in faults[0]


def test_source_hash_mismatch_is_a_fault(tmp_path: Path) -> None:
    run, sources = make_run(tmp_path)
    (sources / "annual.txt").write_text(SOURCE + "changed\n")
    (run / "inputs" / sha(SOURCE.encode())).unlink()
    faults = flow.run_faults(run, sources)
    assert faults and all("annual.txt" in f for f in faults)


def test_delivered_copy_that_differs_is_a_fault(tmp_path: Path) -> None:
    run, sources = make_run(tmp_path)
    (run / "deliveries/d1/CP-0.md").write_text(CP0 + "edited\n")
    faults = flow.run_faults(run, sources)
    assert len(faults) == 1 and "CP-0" in faults[0]


def test_report_number_not_in_handoffs_is_a_fault() -> None:
    faults = flow.report_faults("Revenue 7,941 and 7,940", [CP0, CP1])
    assert len(faults) == 1 and "7941" in faults[0]


def test_report_numbers_from_handoffs_pass() -> None:
    assert flow.report_faults("Revenue 7,940 margin 12% 2030", [CP0], "year 2030") == []


def test_main_exits_1_and_prints_count(tmp_path: Path, capsys) -> None:
    run, sources = make_run(tmp_path)
    assert flow.main([str(run), "--sources", str(sources)]) == 0
    assert "flow: 0 fault(s)" in capsys.readouterr().out
    (run / "deliveries/d1/CP-0.md").write_text("edited")
    assert flow.main([str(run), "--sources", str(sources)]) == 1
    assert "flow: 1 fault(s)" in capsys.readouterr().out


def test_superseded_attempt_is_not_checked_against_the_accepted_upstream(tmp_path: Path) -> None:
    run, sources = make_run(tmp_path)
    stale = run / "live/modules" / sha(b"stale")
    stale.mkdir()
    request = {
        "module_id": "CP-1",
        "sources": {},
        "handoffs": {"CP-0": {"sha256": "0" * 64, "markdown": "old"}},
    }
    (stale / "0.request.json").write_text(
        json.dumps({"messages": [{}, {"text": json.dumps(request)}]})
    )
    (stale / "0.tools.json").write_text("[]")
    assert (
        flow.run_faults(run, sources) != []
    )  # no draft says which attempt produced CP-1: all checked
    (run / "live/modules" / sha(b"CP-1") / "1.draft.md").write_text(CP1)
    assert flow.run_faults(run, sources) == []


def test_rounded_long_results_cover_their_printed_roundings_only() -> None:
    long = "4.5068296189791516894320632638389647735"
    known = flow.rounded(flow.numbers(long))
    assert {"4.51", "4.507", "4.5068"} <= known
    assert "4.52" not in known and "4.6" not in known
    assert flow.rounded({"4.51"}) == {"4.51"}  # a reported two-decimal figure is not expanded
    assert flow.report_faults("ratio 4.51x and 4.52x", [long]) == [
        "report: number 4.52 is not in the handoffs or context"
    ]
