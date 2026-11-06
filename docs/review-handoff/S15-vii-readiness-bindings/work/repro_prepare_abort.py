"""One corrupt source aborts prepare() for every source instead of yielding an unreadable Source."""
import shutil, sys, tempfile, logging
from datetime import date
from pathlib import Path
logging.disable(logging.CRITICAL)
from deploy_vii.contracts import Run
from deploy_vii.preparation import PreparationRequest, SourceRequest, prepare
W = Path(__file__).parent
X = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
for bad, media in (("crash_error.xlsx", X), ("crash_AttributeError.pdf", "application/pdf"),
                   ("crash_LimitReachedError.pdf", "application/pdf"), ("crash_RuntimeError.xlsx", X)):
    with tempfile.TemporaryDirectory(dir=W) as tmp:
        root = Path(tmp) / "src"; root.mkdir()
        (root / "good.txt").write_text("Issuer Co revenue 100\n")
        shutil.copy(W / bad, root / ("bad" + Path(bad).suffix))
        req = PreparationRequest(
            run=Run(run_id="r1", issuer_id="i", issuer_name="Issuer Co", as_of=date(2026, 1, 1), case_kind="synthetic"),
            sources=(SourceRequest(source_id="good", path="good.txt", media_type="text/plain"),
                     SourceRequest(source_id="bad", path="bad" + Path(bad).suffix, media_type=media)))
        try:
            pack = prepare(req, root, Path(tmp) / "out")
            print(bad, "->", [(s.source_id, s.status) for s in pack.sources])
        except Exception as e:
            print(bad, "-> prepare raised", f"{type(e).__module__}.{type(e).__name__}", "; pack written:", (Path(tmp) / "out").exists())
