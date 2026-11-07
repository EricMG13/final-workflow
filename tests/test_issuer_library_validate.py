"""The validation gates must never run with a provider key present: no gate pays."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "library_validate", ROOT / "apps/issuer-library/validate.py"
)
validate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate)

# Every provider the launcher can pay, written here from the adapter's declared key variables.
PROVIDER_KEYS = [
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "OPENROUTER_API_KEY",
    "COPILOT_GITHUB_TOKEN",
]


@pytest.mark.parametrize("name", PROVIDER_KEYS)
def test_gates_run_without_the_provider_key(monkeypatch, name):
    monkeypatch.setenv(name, "secret")
    assert name not in validate.clean_env()
