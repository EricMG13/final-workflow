# Repro: a UTF-8 byte-order mark makes store.structured() show a valid handoff as one unstructured block.
import importlib.util
from pathlib import Path
REPO = Path("/home/user/final-workflow")
spec = importlib.util.spec_from_file_location("store", REPO / "apps/issuer-library/engine/store.py")
store = importlib.util.module_from_spec(spec); spec.loader.exec_module(store)
raw = (REPO / "apps/issuer-library/designs/reader-fixture/CP-1.md").read_bytes()
for label, data in [("no BOM", raw), ("BOM", b"\xef\xbb\xbf" + raw)]:
    sections, problem = store.structured(data, strict=False)
    fields = store.reader_fields(sections)
    print(f"{label}: sections={len(sections)} first={sections[0]['heading'][:30]!r} problem={problem!r} summary={fields['summary'] is not None} charts={len(fields['charts'])}")
