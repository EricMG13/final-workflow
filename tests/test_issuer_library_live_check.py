"""live_check: refusals happen before anything exists, and live_evidence follows the answer key."""

import importlib.util
import json
import os
import subprocess
import sys
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


def refuse(tmp_path: Path, *args: str, key: bool = True) -> subprocess.CompletedProcess[str]:
    env = {k: v for k, v in os.environ.items() if k not in KEY_NAMES}
    env |= {"FW_PYTHON": sys.executable, "ISSUER_LIBRARY_BINARY": str(tmp_path / "missing-binary")}
    if key:
        env["OPENAI_API_KEY"] = "sk-test-not-a-real-key"
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


def test_rehearsal_needs_no_key_but_still_needs_a_cap(tmp_path: Path) -> None:
    done = refuse(tmp_path, "--rehearse", key=False)
    assert done.returncode == 2 and "--cap" in done.stderr


CP1 = "Net sales 7,940 and cash 6,261 (USD millions).\n"


def make_run(tmp_path: Path, rows: list[dict[str, str]], handoff: str = CP1) -> Path:
    run = tmp_path / "run"
    (run / "live").mkdir(parents=True)
    (run / "live/calls.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    (run / "CP-1.md").write_text(handoff)
    return run


def row(module: str = "CP-1", **changes: str) -> dict[str, str]:
    base = {
        "module_id": module,
        "requested_model": "gpt-6.1-sol",
        "reported_model": "gpt-6.1-sol",
        "request_id": "resp_1",
        "settled_usd": "0.50",
    }
    return base | changes


def evidence(run: Path, cap: str = "5", spent: str = "1.00", modules=frozenset({"CP-0", "CP-1"})):
    return live_check.live_evidence(run, Decimal(cap), spent, set(modules))


def test_live_evidence_clean(tmp_path: Path) -> None:
    run = make_run(tmp_path, [row("CP-0"), row("CP-1")])
    assert evidence(run) == []
    assert evidence(run, spent="1.0000") == []


@pytest.mark.parametrize(
    ("rows", "kwargs", "word"),
    [
        ([row("CP-0"), row("CP-1", reported_model="other")], {}, "reported"),
        ([row("CP-0", request_id=""), row("CP-1")], {}, "request_id"),
        ([row("CP-0"), row("CP-1")], {"cap": "0.99"}, "cap"),
        ([row("CP-0", settled_usd="0"), row("CP-1", settled_usd="0")], {"spent": "0"}, "spend"),
        ([row("CP-0"), row("CP-1")], {"spent": "0.99"}, "status"),
        ([row("CP-0"), row("CP-1")], {"modules": {"CP-0", "CP-1", "CP-1A"}}, "modules"),
    ],
)
def test_live_evidence_faults(tmp_path: Path, rows, kwargs, word: str) -> None:
    found = evidence(make_run(tmp_path, rows), **kwargs)
    assert found and any(word in f for f in found)


def test_live_evidence_requires_filed_literals(tmp_path: Path) -> None:
    run = make_run(tmp_path, [row("CP-0"), row("CP-1")], handoff="Net sales 7,940 only.\n")
    found = evidence(run)
    assert len(found) == 1 and "6,261" in found[0]
    assert evidence(run, modules={"CP-0", "CP-1A"}, spent="1.00") != []  # module set differs
