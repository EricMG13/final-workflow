"""Feed the full launcher checker (which also runs the report adapter) a CP-1 answer whose leverage
chart has (a) no data rows or (b) no separator and a non-numeric first row."""
import sys, json, hashlib, shutil
from pathlib import Path
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_cpos_launch as T
from deploy_workflow.owners.cpos_launch import prepare, checker
from deploy_workflow.owners.cpos import HandoffTask
from deploy_workflow.handoff_delivery import DeliveryRequest, HandoffInput
from deploy_workflow.markdown_delivery import markdown_files
S = Path(sys.argv[1]); d = S / "work" / "a07"; shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
ctx = T.context_file(d, "credit_snapshot"); folder = T.issuer_folder(d)
p = prepare(ctx, folder, d / "out", config="sol-medium", cap="50", modules=("CP-1",))
routes = list(p.plan.layout.routes)
sources = {n: hashlib.sha256((d / "out" / s.path).resolve().read_bytes()).hexdigest() for n, s in p.plan.sources.items()}
good = T.answer({"module_id": "CP-1", "sources": sources, "handoffs": {}}, routes)
lev = T.CHART_TABLES["Chart data: leverage"]
head, sep = lev.splitlines()[:2]
variants = {
    "good": good,
    "a-no-rows": good.replace(lev, head + "\n" + sep),
    "b-no-separator": good.replace(lev, head + "\n| FY2024 | about four | n/a | x | |\n| FY2023 | 4.20 | 3.85 | x | Synthetic. |"),
}
srcbytes = {n: (d / "out" / s.path).resolve().read_bytes() for n, s in p.plan.sources.items()}
chk = checker(p.plan.layout)
for name, text in variants.items():
    task = HandoffTask(p.plan.run, "CP-1", b"", srcbytes, {}, 1, ())
    issues = chk(task, text.encode())
    print(name, "issues:", issues)
    if not issues:
        (d / f"{name}.md").write_text(text)
        req = DeliveryRequest(run=p.plan.run, handoffs={"CP-1": HandoffInput(path=f"{name}.md", sha256=hashlib.sha256(text.encode()).hexdigest())}, layout=p.plan.layout)
        files = markdown_files(req, d)
        rv = json.loads(files["report-view.json"])
        fig = [b for b in rv["blocks"] if "leverage" in json.dumps(b)][:1]
        print("   delivered leverage block:", json.dumps(fig)[:600])
