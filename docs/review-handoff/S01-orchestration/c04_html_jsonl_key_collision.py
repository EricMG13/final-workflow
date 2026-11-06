"""C04: _issuer_files keys an HTML file as '<name>.jsonl'; a sibling '<name>.jsonl' silently replaces it."""
import json, tempfile
from pathlib import Path
from deploy_workflow.owners.cpos_launch import _issuer_files

with tempfile.TemporaryDirectory() as t:
    folder = Path(t) / "issuer"; folder.mkdir()
    (folder / "10-K.html").write_bytes(b"<html><body><p>FY2025 revenue 1,234</p></body></html>")
    (folder / "10-K.html.jsonl").write_text(json.dumps({"page": 1, "text": "an older Q1 extract"}) + "\n")
    pinned, converted, ignored = _issuer_files(folder, Path(t) / "ctx.json", Path(t) / "out")
    print("pinned keys:", list(pinned))
    print("pinned path:", pinned["10-K.html.jsonl"].path)
    print("converted written but unreferenced:", list(converted))
    print("ignored:", ignored)
