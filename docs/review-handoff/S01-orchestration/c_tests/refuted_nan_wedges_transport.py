"""C05: serve_json_lines parses NaN; the host records the call, _parse refuses it, and every
later invoke/submit in the session fails identity_mismatch."""
import json
from io import StringIO
from tests.test_source_workflow import api, make_pack


def test_nan_argument_wedges_session(tmp_path):
    module = api()
    workflow = module.SourceWorkflow.create(tmp_path / "execution", make_pack())
    good = {"operation": "invoke", "tool": "read_pages",
            "arguments": {"source_id": "identity", "first_page": 1, "last_page": 1}}
    lines = [
        '{"operation": "invoke", "tool": "read_pages", "arguments": {"source_id": "identity", "first_page": NaN, "last_page": 1}}',
        json.dumps(good),
        json.dumps({"operation": "submit_review", "payload": "{}"}),
    ]
    out = StringIO()
    module.serve_json_lines(workflow, StringIO("\n".join(lines) + "\n"), out,
                            destination=tmp_path / "r.json", participant="t")
    replies = [json.loads(x) for x in out.getvalue().splitlines()]
    print(replies)
    assert replies[0]["error_code"] == "bad_arguments"
    assert replies[1] == {"status": "refused", "error_code": "identity_mismatch"}  # a valid call now refused
