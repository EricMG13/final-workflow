"""Synthetic S04 adversarial harness: real CP-OS layout + markdown_files."""
import hashlib, json, sys, tempfile
from pathlib import Path
from deploy_vii.contracts import Run, View
from deploy_vii.report_view import ReportView
from deploy_workflow.handoff_delivery import DeliveryRequest, HandoffInput
from deploy_workflow.markdown_delivery import markdown_files
from deploy_workflow.owners.cpos_launch import _layout

RUN = Run.model_validate_json(json.dumps({'schema_version':'run/2','run_id':'x','issuer_id':'ACME',
  'issuer_name':'Acme Corp','as_of':'2024-12-31','method_version':'deploy-v-r14','case_kind':'public',
  'pathway':'credit_snapshot','requested_modules':['CP-1']}))

HDR = "| Period | {cols} | Reporting unit | Basis and limitation |\n| --- | {sep} | --- | --- |\n"
def chart(heading, cols, rows, unit):
    out = f"### {heading}\n\n" + HDR.format(cols=" | ".join(cols), sep=" | ".join("---" for _ in cols))
    for period, *vals in rows:
        out += f"| {period} | " + " | ".join(vals) + f" | {unit} | basis |\n"
    return out + "\n"

def handoff(fin_table=None, leverage=None, cover=None, liq=None, mat=None, extra_findings="", unit_liq="US$m"):
    fin_table = fin_table or "| Metric | FY2023 | FY2024 |\n| --- | ---: | ---: |\n| Revenue | 1,000.5 | (12.3) |\n| EBITDA |  | 0 |\n"
    leverage = leverage or [("FY2023", "4.1", "3.9"), ("FY2024", "3.8", "3.5")]
    cover = cover or [("FY2023", "2.5"), ("FY2024", "2.7")]
    liq = liq or [("FY2023", "100", "200"), ("FY2024", "150", "Not supplied: undisclosed")]
    mat = mat or [("2025", "50"), ("2026", "Not supplied: none")]
    return ("# CP-1 Acme Corp\n\n## Request\nAcme Corp historical analysis.\n\n## Sources\nsrc.pdf\n\n## Findings\n\n"
        + chart("Chart data: leverage", ["Total debt / EBITDA", "Net debt / EBITDA"], leverage, "x")
        + chart("Chart data: interest cover", ["EBITDA / cash interest"], cover, "x")
        + chart("Chart data: liquidity", ["Cash", "Undrawn committed facilities"], liq, unit_liq)
        + chart("Chart data: debt maturities", ["Debt maturing"], mat, "US$m")
        + "### Financials and credit metrics\n\n" + fin_table + "\n" + extra_findings
        + "## Calculations\nNone.\n\n## Gaps\nNone.\n\n## Next module\nDelivery.\n")

def deliver(text, raw=None):
    raw = raw if raw is not None else text.encode()
    layout, _ = _layout(RUN, ("CP-1",), (), "cfg")
    d = Path(tempfile.mkdtemp())
    (d / "CP-1.md").write_bytes(raw)
    req = DeliveryRequest(run=RUN, handoffs={"CP-1": HandoffInput(path="CP-1.md", sha256=hashlib.sha256(raw).hexdigest())}, layout=layout)
    files = markdown_files(req, d)
    return files, ReportView.model_validate_json(files["report-view.json"]), View.model_validate_json(files["view.json"])

if __name__ == "__main__":
    files, rv, view = deliver(handoff())
    for b in rv.blocks:
        print(b.block_id, b.kind, b.state)
        for f in b.figures:
            print("  ", f.fig_id, f.chart.unit, [(m.series, m.label, m.value, m.text) for m in f.chart.marks])
        for r in b.rows:
            print("  ", r.label, [c.text for c in r.cells])
