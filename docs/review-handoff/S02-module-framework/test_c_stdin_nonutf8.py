"""Repro: a short non-UTF-8 line on the JSON-lines transport crashes serve_json_lines."""
import importlib, io, sys
from pathlib import Path
import pytest
sys.path.insert(0, "tests")
guards = importlib.import_module("test_owner_guards")
financial = guards.financial
from deploy_workflow import owner_workflow as owner


@pytest.mark.parametrize("raw", [
    b'\xff{"operation":"nope"}\n',
    b'{"operation":"nope"}\n{"operation":"\xff"}\n',  # bad byte on line 2, same decode chunk
])
def test_short_non_utf8_line(tmp_path: Path, monkeypatch, raw):
    monkeypatch.setattr(financial, "start", guards._owner_start)
    workflow, _ = financial.start(tmp_path)
    out = io.StringIO()
    try:
        owner.serve_json_lines(workflow, io.TextIOWrapper(io.BytesIO(raw), encoding="utf-8"), out,
                               destination=tmp_path / "r.json", participant="p")
        outcome = "returned"
    except Exception as e:  # noqa
        outcome = f"raised {type(e).__name__}"
    print(f"\nRAW={raw!r} OUTCOME={outcome} ANSWERS={out.getvalue()!r} FAULTS={guards._faults(workflow)}")
