"""CR-C02: read_cp1_envelope accepts a consistently rewritten envelope whose quality,
gap_limitations and registers_sha256 differ from what promotion recorded."""
import importlib, json, sys, tempfile
from pathlib import Path
sys.path.insert(0, "tests")
from deploy_vii.cp1_workflow import write_cp1_envelope, read_cp1_envelope
from deploy_vii.envelope import read_envelope, write_envelope
from deploy_vii.execution import Execution, text_sha256
fw = importlib.import_module("test_financial_workflow")
with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
    root = Path(d) / "case"
    fw.promoted_case(root)
    store = Execution(root / "store")
    out = Path(d) / "export"
    write_cp1_envelope(store, out)
    env = read_cp1_envelope(store, out)
    print("genuine: qa_status=%s score=%s gap_limitations=%d registers=%s" % (
        env.quality.confidence.qa_status, env.quality.confidence.confidence_score,
        len(env.gap_limitations), env.registers_sha256[:12]))
    conf = env.quality.confidence.model_copy(update={"confidence_score": 95, "confidence_band": "High"})
    forged = env.model_copy(update={
        "quality": env.quality.model_copy(update={"confidence": conf}),
        "gap_limitations": (),
        "registers_sha256": "0" * 64,
    })
    md, sc = write_envelope(forged)
    (out / "envelope.md").write_text(md, encoding="utf-8")
    (out / "envelope.json").write_text(sc, encoding="utf-8")
    receipt = json.loads((out / "complete.json").read_text())
    receipt["files"] = {"envelope.md": text_sha256(md), "envelope.json": text_sha256(sc)}
    receipt["registers_sha256"] = forged.registers_sha256
    receipt["quality_report_sha256"] = forged.quality.content_hash()
    (out / "complete.json").write_text(json.dumps(receipt))
    got = read_cp1_envelope(store, out)  # should raise EnvelopeRefused
    print("FORGED ACCEPTED: qa_status=%s score=%s band=%s gap_limitations=%d registers=%s" % (
        got.quality.confidence.qa_status, got.quality.confidence.confidence_score,
        got.quality.confidence.confidence_band, len(got.gap_limitations), got.registers_sha256[:12]))
