"""A03: read_cp1_envelope accepts an export whose gap limitations and registers hash were
rewritten (Markdown, sidecar and receipt kept mutually consistent); nothing compares them with
the promoted handoff the journal retains."""
import hashlib, json, sys, tempfile
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from deploy_vii.contracts import Input, Module, Run
from deploy_vii.envelope import Envelope, write_envelope
from deploy_vii.execution import text_sha256
from deploy_vii.cp1_workflow import read_cp1_envelope, EnvelopeRefused

h = lambda s: hashlib.sha256(s.encode()).hexdigest()
run = Run(run_id="r1", issuer_id="iss", issuer_name="Issuer", as_of=date(2026, 1, 31),
          case_kind="synthetic", requested_modules=("CP-1",))
module = Module(run_id="r1", issuer_id="iss", as_of=date(2026, 1, 31), module_id="CP-1",
                status="restricted", inputs=(Input(input_id="pack", sha256=h("pack")),),
                limitations=("Q4 cash flow statement missing",))
head = SimpleNamespace(module_id="CP-1", status="restricted", result_sha256=module.content_hash(),
                       qualification=None)
snapshot = SimpleNamespace(heads=[head], run=run, pack_sha256=h("pack"),
                           content_hash=lambda: h("snap"))
store = SimpleNamespace(read=lambda: snapshot)

def export(env: Envelope, d: Path) -> None:
    md, sc = write_envelope(env)
    d.mkdir()
    (d / "envelope.md").write_text(md); (d / "envelope.json").write_text(sc)
    receipt = {"schema_version": "cp1-envelope/1", "module_sha256": head.result_sha256,
               "pack_sha256": snapshot.pack_sha256, "registers_sha256": env.registers_sha256,
               "quality_report_sha256": None, "status": head.status, "qualification": None,
               "files": {"envelope.md": text_sha256(md), "envelope.json": text_sha256(sc)}}
    (d / "complete.json").write_text(json.dumps(receipt))

genuine = Envelope(run=run, module=module, registers_sha256=h("registers"),
                   gap_limitations=("FY2024 comparatives absent: growth not calculable",))
forged = genuine.model_copy(update={"registers_sha256": h("other registers"), "gap_limitations": ()})
with tempfile.TemporaryDirectory(dir=sys.argv[1]) as t:
    for name, env in (("genuine", genuine), ("forged", forged)):
        d = Path(t) / name
        export(env, d)
        try:
            got = read_cp1_envelope(store, d)
            print(name, "ACCEPTED: gap_limitations=", got.gap_limitations,
                  "registers=", got.registers_sha256[:12])
        except EnvelopeRefused as e:
            print(name, "REFUSED", e.issues)
