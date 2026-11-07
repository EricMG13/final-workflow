"""live_check: refusals happen before anything exists, and live_evidence follows the answer key."""

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import time
from decimal import Decimal
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DESIGNS = ROOT / "apps/issuer-library/designs"
sys.path.insert(0, str(DESIGNS))
spec = importlib.util.spec_from_file_location("live_check", DESIGNS / "live_check.py")
live_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(live_check)

KEY_NAMES = ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "OPENROUTER_API_KEY", "COPILOT_GITHUB_TOKEN")
NOT_PROVIDER = ("GH_TOKEN", "GITHUB_TOKEN")


def test_provider_keys_are_the_adapters_key_variables() -> None:
    from deploy_workflow.model.adapter import KEY_VARIABLES

    assert set(live_check.PROVIDER_KEYS) == set(KEY_VARIABLES.values())


def refuse(
    tmp_path: Path, *args: str, key: bool = True, extra: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    env = {k: v for k, v in os.environ.items() if k not in KEY_NAMES + NOT_PROVIDER}
    env |= {"FW_PYTHON": sys.executable, "ISSUER_LIBRARY_BINARY": str(tmp_path / "missing-binary")}
    if key:
        env["OPENAI_API_KEY"] = "sk-test-not-a-real-key"
    env |= extra or {}
    out = tmp_path / "out"
    done = subprocess.run(
        [sys.executable, str(DESIGNS / "live_check.py"), *args, "--out", str(out)],
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    assert not out.exists()
    assert "sk-test-not-a-real-key" not in done.stdout + done.stderr
    return done


def test_refuses_without_cap(tmp_path: Path) -> None:
    done = refuse(tmp_path)
    assert done.returncode == 2 and "--cap" in done.stderr and len(done.stderr.splitlines()) == 1


@pytest.mark.parametrize("cap", ["0", "-1", "nan", "inf", "-inf", "abc"])
def test_refuses_non_positive_or_nan_cap(tmp_path: Path, cap: str) -> None:
    done = refuse(tmp_path, "--cap", cap)
    assert done.returncode == 2 and "--cap" in done.stderr and len(done.stderr.splitlines()) == 1


def test_refuses_without_any_provider_key(tmp_path: Path) -> None:
    done = refuse(tmp_path, "--cap", "5", key=False)
    assert done.returncode == 2 and "provider key" in done.stderr
    assert len(done.stderr.splitlines()) == 1


def test_github_tokens_are_not_provider_keys(tmp_path: Path) -> None:
    done = refuse(tmp_path, "--cap", "5", key=False, extra={"GH_TOKEN": "gh-test-token-123"})
    assert done.returncode == 2 and "provider key" in done.stderr


def test_refuses_short_minutes_and_used_out_folder(tmp_path: Path) -> None:
    assert "--minutes" in refuse(tmp_path, "--cap", "5", "--minutes", "0.5").stderr
    used = tmp_path / "out"
    used.mkdir()
    (used / "x").write_text("1")
    done = subprocess.run(
        [
            sys.executable,
            str(DESIGNS / "live_check.py"),
            "--cap",
            "5",
            "--rehearse",
            "--out",
            str(used),
        ],
        env={**os.environ, "FW_PYTHON": "x", "ISSUER_LIBRARY_BINARY": __file__},
        capture_output=True,
        text=True,
        check=False,
    )
    assert done.returncode == 2 and "--out" in done.stderr and (used / "x").exists()


def test_stop_group_kills_the_whole_group_and_reports_spend(tmp_path: Path) -> None:
    server = subprocess.Popen(["sh", "-c", "sleep 60 & sleep 60 & wait"], start_new_session=True)
    assert live_check.group_alive(server)
    assert live_check.stop_group(server) is None
    assert not live_check.group_alive(server)
    intake = tmp_path / "intake/web-1"
    intake.mkdir(parents=True)
    (intake / "status.json").write_text(json.dumps({"spent_usd": "0.25"}))
    (tmp_path / "runs/web-1/live").mkdir(parents=True)
    (tmp_path / "runs/web-1/live/calls.jsonl").write_text(
        json.dumps({"settled_usd": "0.10"}) + "\n" + json.dumps({"settled_usd": "0.20"}) + "\n"
    )
    assert live_check.spend_of(tmp_path) == ("0.25", Decimal("0.30"), 0)


def test_spend_of_counts_unknown_cost_and_torn_rows(tmp_path: Path) -> None:
    (tmp_path / "intake/web-1").mkdir(parents=True)
    (tmp_path / "intake/web-1/status.json").write_text(json.dumps({"spent_usd": "5.78"}))
    live = tmp_path / "runs/web-1/live"
    live.mkdir(parents=True)
    rows = [{"settled_usd": "0.05"}, {"settled_usd": None, "cost_status": "unknown"}]
    (live / "calls.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows) + '{"settled_u')
    assert live_check.spend_of(tmp_path) == ("5.78", Decimal("0.05"), 2)


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


class Page:
    def __init__(self, model: str, cap: str, ids: list[str]) -> None:
        self.shown = {"rows": {"Model": model, "Maximum spend": f"USD {cap}"}, "ids": ids}

    def evaluate(self, _script: str) -> dict:
        return self.shown


def review(modules: str, ids: list[str]) -> list[str]:
    args = argparse.Namespace(config="sol-medium", cap=Decimal(10), modules=modules)
    return live_check.check_review(Page("openai gpt-6.1-sol · medium", "10", ids), args)


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


def test_rehearsal_needs_no_key_but_still_needs_a_cap(tmp_path: Path) -> None:
    done = refuse(tmp_path, "--rehearse", key=False)
    assert done.returncode == 2 and "--cap" in done.stderr


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
