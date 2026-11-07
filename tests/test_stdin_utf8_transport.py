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


class _Pipe(io.RawIOBase):
    """A participant's pipe that hands over one line per read, as an interactive participant who
    waits for each answer does (a BytesIO hands over everything in one chunk)."""

    def __init__(self, lines: list[bytes]) -> None:
        self._lines = list(lines)

    def readable(self) -> bool:
        return True

    def readinto(self, buffer) -> int:  # type: ignore[no-untyped-def,override]
        if not self._lines:
            return 0
        line = self._lines.pop(0)
        buffer[: len(line)] = line
        return len(line)


def test_lines_before_a_bad_line_are_answered_and_the_stream_ends_at_it(tmp_path):
    # Review of S02-C02. Expected (hand-derived): line 1 is a well-formed request for an unknown
    # operation, answered not_permitted before line 2 is read; line 2 cannot be decoded, so it is
    # answered bad_arguments and the stream ends; line 3 is never read or answered.
    workflow = OwnerWorkflow.create(
        tmp_path / "store", make_pack(), publication_directory=tmp_path / "model"
    )
    out = io.StringIO()
    lines = [b'{"operation":"nope"}\n', b'{"operation":"\xff"}\n', b'{"operation":"nope"}\n']
    reader = io.TextIOWrapper(io.BufferedReader(_Pipe(lines)), encoding="utf-8")
    serve_json_lines(workflow, reader, out, destination=tmp_path / "r.json", participant="p")
    assert [json.loads(x) for x in out.getvalue().splitlines()] == [
        {"status": "refused", "error_code": "not_permitted"},
        {"status": "refused", "error_code": "bad_arguments"},
    ]
