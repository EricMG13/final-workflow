"""live_check: refusals happen before anything exists, and live_evidence follows the answer key."""

import argparse
import hashlib
import importlib.util
import json
import os
import signal
import subprocess
import sys
import time
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
DESIGNS = ROOT / "apps/issuer-library/designs"
sys.path.insert(0, str(DESIGNS))
spec = importlib.util.spec_from_file_location("live_check", DESIGNS / "live_check.py")
live_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(live_check)
from faults import Faults

KEY_NAMES = ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "OPENROUTER_API_KEY", "COPILOT_GITHUB_TOKEN")
NOT_PROVIDER = ("GH_TOKEN", "GITHUB_TOKEN")


def test_provider_keys_are_the_adapters_key_variables() -> None:
    from deploy_workflow.model.adapter import KEY_VARIABLES

    assert set(live_check.PROVIDER_KEYS) == set(KEY_VARIABLES.values())


WITH_KEY = {"OPENAI_API_KEY": "sk-test-not-a-real-key"}


def refuse(
    tmp_path: Path, *args: str, extra: dict[str, str] = WITH_KEY, keep: bool = False
) -> subprocess.CompletedProcess[str]:
    env = {k: v for k, v in os.environ.items() if k not in KEY_NAMES + NOT_PROVIDER}
    env |= {"FW_PYTHON": sys.executable, "ISSUER_LIBRARY_BINARY": str(tmp_path / "missing-binary")}
    env |= extra
    out = tmp_path / "out"
    done = subprocess.run(
        [sys.executable, str(DESIGNS / "live_check.py"), *args, "--out", str(out)],
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    assert keep or not out.exists()
    assert "sk-test-not-a-real-key" not in done.stdout + done.stderr
    return done


BAD_CAPS = [(("--cap", c), WITH_KEY, "--cap") for c in ("0", "-1", "nan", "inf", "-inf", "abc")]


@pytest.mark.parametrize(
    ("args", "extra", "word"),
    [
        ((), WITH_KEY, "--cap"),
        *BAD_CAPS,
        (("--cap", "5"), {}, "provider key"),
        (("--cap", "5"), {"GH_TOKEN": "gh-test-token-123"}, "provider key"),
        (("--cap", "5", "--minutes", "0.5"), WITH_KEY, "--minutes"),
        (("--rehearse",), {}, "--cap"),  # a rehearsal needs no key, but a cap
    ],
)
def test_refuses_with_one_line_before_anything_exists(
    tmp_path: Path, args: tuple[str, ...], extra: dict[str, str], word: str
) -> None:
    done = refuse(tmp_path, *args, extra=extra)
    assert done.returncode == 2 and word in done.stderr and len(done.stderr.splitlines()) == 1


@pytest.mark.parametrize(
    "make", [lambda p: p.write_text("1"), lambda p: (p.mkdir(), (p / "x").write_text("1"))]
)
def test_refuses_an_out_that_is_a_file_or_a_used_folder(tmp_path: Path, make) -> None:
    make(tmp_path / "out")
    done = refuse(tmp_path, "--cap", "5", keep=True)
    assert done.returncode == 2 and "--out" in done.stderr and (tmp_path / "out").exists()
    out = tmp_path / "out"
    assert (out if out.is_file() else out / "x").read_text() == "1"


def test_stop_group_kills_the_whole_group() -> None:
    server = subprocess.Popen(["sh", "-c", "sleep 60 & sleep 60 & wait"], start_new_session=True)
    assert live_check.group_alive(server)
    assert live_check.stop_group(server) is None
    assert not live_check.group_alive(server)


def test_spend_of_sums_the_ledger_and_counts_unknown_cost_and_torn_rows(tmp_path: Path) -> None:
    intake = tmp_path / "intake/web-1"
    intake.mkdir(parents=True)
    (intake / "status.json").write_text(json.dumps({"spent_usd": "0.25"}))
    live = tmp_path / "runs/web-1/live"
    live.mkdir(parents=True)
    rows = [{"settled_usd": "0.10"}, {"settled_usd": "0.20"}]
    (live / "calls.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    assert live_check.spend_of(tmp_path) == ("0.25", Decimal("0.30"), 0)
    rows = [{"settled_usd": "0.05"}, {"settled_usd": None, "cost_status": "unknown"}]
    (live / "calls.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows) + '{"settled_u')
    assert live_check.spend_of(tmp_path) == ("0.25", Decimal("0.05"), 2)


def test_check_run_and_spend_of_read_the_same_intake_status(tmp_path: Path) -> None:
    for name, spent in (("web-1", "1"), ("web-2", "2")):
        (tmp_path / "intake" / name).mkdir(parents=True)
        (tmp_path / "intake" / name / "status.json").write_text(json.dumps({"spent_usd": spent}))
    last = live_check.intake_status(tmp_path)
    assert last and last.parent.name == "web-2" and live_check.spend_of(tmp_path)[0] == "2"


def test_stop_group_names_a_server_that_does_not_lead_its_group() -> None:
    child = subprocess.Popen(["sleep", "30"])
    message = live_check.stop_group(child)
    assert child.poll() is not None and message and "lead" in message


def test_watchdog_stops_the_group_when_its_pipe_closes() -> None:
    server = subprocess.Popen(["sh", "-c", "sleep 60 & sleep 60 & wait"], start_new_session=True)
    dog = live_check.arm_watchdog(server)
    assert dog.stdin and live_check.group_alive(server)
    dog.stdin.close()  # what the kernel does when live_check dies by any means
    for _ in range(100):
        if not live_check.group_alive(server):
            break
        time.sleep(0.1)
    assert not live_check.group_alive(server)
    dog.kill()
    dog.wait()


def review(modules: str, ids: list[str]) -> list[str]:
    args = argparse.Namespace(config="sol-medium", cap=Decimal(10), modules=modules)
    rows = {"Model": "openai gpt-6.1-sol · medium", "Maximum spend": "USD 10"}
    page = SimpleNamespace(evaluate=lambda _script: {"rows": rows, "ids": ids})
    return live_check.check_review(page, args)


def test_review_for_the_answer_key_case_must_list_exactly_its_modules() -> None:
    assert review("CP-1 CP-1A", ["CP-0", "CP-1", "CP-1A"]) == []
    assert review("CP-1 CP-1A", ["CP-0", "CP-1", "CP-1A", "CP-2"])
    assert review("CP-1 CP-1A", ["CP-0", "CP-1"])
    assert review("CP-1", ["CP-0", "CP-1", "CP-2"]) == []  # other cases: every requested module
    assert review("CP-1 CP-3", ["CP-0", "CP-1"])


def test_answer_key_case_follows_the_request_not_the_run() -> None:
    assert live_check.is_key_case(argparse.Namespace(config="sol-medium", modules="CP-1  CP-1A"))
    assert not live_check.is_key_case(argparse.Namespace(config="sol-high", modules="CP-1 CP-1A"))
    assert not live_check.is_key_case(argparse.Namespace(config="sol-medium", modules="CP-1"))


def test_answer_key_env_never_optimises_asserts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PYTHONOPTIMIZE", "1")
    assert "PYTHONOPTIMIZE" not in live_check.key_env()


CP0 = "CP-0 body\n"
MODS = {"CP-0", "CP-1", "CP-1A"}


def make_run(
    tmp_path: Path,
    rows: list[dict[str, str]],
    cp1: str | None = None,
    execution: str = "live-provider",
) -> Path:
    run = tmp_path / "run"
    (run / "live").mkdir(parents=True)
    (run / "live/calls.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    d0 = hashlib.sha256(CP0.encode()).hexdigest()
    cp1 = cp1 if cp1 is not None else f"Net sales 7,940 and cash 6,261. {d0}\n"
    d1 = hashlib.sha256(cp1.encode()).hexdigest()
    (run / "CP-0.md").write_text(CP0)
    (run / "CP-1.md").write_text(cp1)
    (run / "CP-1A.md").write_text(f"{d0} {d1}\n")
    (run / "completed-x.json").write_text(
        json.dumps({"execution": execution, "module_execution": dict.fromkeys(MODS, execution)})
    )
    return run


def row(module: str = "CP-1", **changes: str) -> dict[str, str]:
    base = {
        "module_id": module,
        "requested_model": "gpt-6.1-sol",
        "reported_model": "gpt-6.1-sol",
        "config_id": "sol-medium",
        "request_id": "resp_1",
        "settled_usd": "0.50",
    }
    return base | changes


def rows3(**changes: str) -> list[dict[str, str]]:
    return [row(m, **({"settled_usd": "0.30"} | changes)) for m in sorted(MODS)]


def evidence(run: Path, cap: str = "5", spent: str = "0.90", modules=frozenset(MODS), config=""):
    return live_check.live_evidence(run, Decimal(cap), spent, set(modules), config)


def test_live_evidence_clean(tmp_path: Path) -> None:
    run = make_run(tmp_path, rows3())
    assert evidence(run) == []
    assert evidence(run, spent="0.9000", config="sol-medium") == []


@pytest.mark.parametrize(
    ("rows", "kwargs", "word"),
    [
        (rows3(reported_model="other"), {}, "reported"),
        (rows3(requested_model="cheap", reported_model="cheap"), {}, "model"),
        (rows3(config_id="sol-high"), {"config": "sol-medium"}, "config"),
        ([row(m, request_id="", settled_usd="0.30") for m in sorted(MODS)], {}, "request_id"),
        (rows3(), {"cap": "0.89"}, "cap"),
        (rows3(settled_usd="0"), {"spent": "0"}, "spend"),
        (rows3(), {"spent": "0.99"}, "status"),
        (rows3(), {"modules": MODS | {"CP-2"}}, "modules"),
    ],
)
def test_live_evidence_faults(tmp_path: Path, rows, kwargs, word: str) -> None:
    found = evidence(make_run(tmp_path, rows), **kwargs)
    assert found and any(word in f for f in found)


def test_live_evidence_requires_live_execution_and_upstream_digests(tmp_path: Path) -> None:
    replay = evidence(make_run(tmp_path, rows3(), execution="offline-replay"))
    assert any("execution" in f for f in replay)
    run = tmp_path / "b"
    run.mkdir()
    unchained = evidence(make_run(run, rows3(), cp1="Net sales 7,940 and cash 6,261.\n"))
    assert any("CP-0" in f for f in unchained)


def test_live_evidence_requires_filed_literals(tmp_path: Path) -> None:
    d0 = hashlib.sha256(CP0.encode()).hexdigest()
    run = make_run(tmp_path, rows3(), cp1=f"Net sales 7,940 only. {d0}\n")
    found = evidence(run)
    assert len(found) == 1 and "6,261" in found[0]


def test_unknown_cost_row_is_a_fault_not_a_crash(tmp_path: Path) -> None:
    rows = [*rows3()[:2], row("CP-1A", settled_usd=None, cost_status="unknown")]
    found = evidence(make_run(tmp_path, rows), spent="0.60")
    assert any("unknown" in f for f in found)


def test_module_execution_must_name_exactly_the_accepted_modules(tmp_path: Path) -> None:
    run = make_run(tmp_path, rows3())
    record = next(run.glob("completed-*.json"))
    record.write_text(
        json.dumps({"execution": "live-provider", "module_execution": {"CP-0": "live-provider"}})
    )
    assert any("module_execution" in f for f in evidence(run))


def test_answer_key_names_the_return_code_of_a_runner_with_no_stderr(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("FW_PYTHON", sys.executable)
    killed = subprocess.CompletedProcess([], -9, "", "")
    monkeypatch.setattr(live_check.subprocess, "run", lambda *a, **k: killed)
    found = live_check.answer_key(tmp_path, Decimal(5))
    assert len(found) == 1 and "-9" in found[0]


def test_a_failure_before_the_signal_keeps_its_kind(monkeypatch, tmp_path) -> None:
    bc = SimpleNamespace(FAULTS=Faults(), results=[], secrets=list, scan_server_logs=lambda: None)

    def walk_then_signal(bc, args, out, summary, held) -> None:
        bc.FAULTS.add("live", "exception", "TimeoutError: before the signal")
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(1)

    saved = {s: signal.getsignal(s) for s in live_check.HALTING}
    monkeypatch.setitem(sys.modules, "browser_check", bc)
    monkeypatch.setattr(live_check, "run_walk", walk_then_signal)
    monkeypatch.setattr(os, "environ", {"FW_PYTHON": "x", "ISSUER_LIBRARY_BINARY": __file__})
    try:
        live_check.main(["--cap", "1", "--rehearse", "--out", str(tmp_path / "o")])
    finally:
        for sig, handler in saved.items():
            signal.signal(sig, handler)
    assert [f.kind for f in bc.FAULTS.items] == ["exception", "interrupted"]
