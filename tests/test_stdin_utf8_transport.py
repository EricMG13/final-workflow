"""S02-C02: a non-UTF-8 byte on the owner JSON-lines transport is answered, not a crash."""

import io
import json

import pytest
from test_financial_workflow import make_pack

from deploy_workflow.owner_workflow import OwnerWorkflow, serve_json_lines


# Expected (hand-derived): the line that cannot be decoded is answered bad_arguments and the
# stream ends. A TextIOWrapper decodes in chunks, so a bad byte on line 2 already fails the
# readline for line 1; both raw inputs therefore get exactly one bad_arguments answer.
@pytest.mark.parametrize(
    "raw",
    [b'\xff{"operation":"nope"}\n', b'{"operation":"nope"}\n{"operation":"\xff"}\n'],
)
def test_non_utf8_line_is_answered_bad_arguments(tmp_path, raw):
    workflow = OwnerWorkflow.create(
        tmp_path / "store", make_pack(), publication_directory=tmp_path / "model"
    )
    out = io.StringIO()
    serve_json_lines(
        workflow,
        io.TextIOWrapper(io.BytesIO(raw), encoding="utf-8"),
        out,
        destination=tmp_path / "r.json",
        participant="p",
    )
    assert [json.loads(x) for x in out.getvalue().splitlines()] == [
        {"status": "refused", "error_code": "bad_arguments"}
    ]
