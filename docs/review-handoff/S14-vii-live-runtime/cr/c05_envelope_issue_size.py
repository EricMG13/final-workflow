from datetime import date
from deploy_vii.contracts import Run, Module, Input
from deploy_vii.envelope import Envelope, write_envelope, envelope_issues
from deploy_vii.execution import bounded_issues, MAX_ISSUE_CHARS
run = Run(run_id="r1", issuer_id="i1", issuer_name="Acme", as_of=date(2026, 1, 1), case_kind="public")
module = Module(run_id="r1", issuer_id="i1", as_of=date(2026, 1, 1), module_id="CP-1",
                inputs=(Input(input_id="pack", sha256="a" * 64),))
env = Envelope(run=run, module=module, registers_sha256="b" * 64)
md, sidecar = write_envelope(env)
print("clean round trip issues:", envelope_issues(md, sidecar))
big = "X" * 2_000_000
tampered = md.replace("| issuer_name | Acme |", f"| issuer_name | {big} |", 1)
issues = envelope_issues(tampered, sidecar)
print("issue count:", len(issues), "longest issue chars:", max(map(len, issues)), "cap elsewhere:", MAX_ISSUE_CHARS)
