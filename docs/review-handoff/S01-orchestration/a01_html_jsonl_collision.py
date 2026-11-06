"""Attack: issuer folder holding a.html and a.html.jsonl -> both map to source key 'a.html.jsonl'."""
import shutil, sys, json
from pathlib import Path
from deploy_workflow.owners import cpos_launch
S = Path(sys.argv[1])
w = S / "work" / "a01"; shutil.rmtree(w, ignore_errors=True)
src = w / "issuer"; src.mkdir(parents=True)
(src / "a.html").write_text("<html><body><p>Annual report revenue USD 100 million</p></body></html>")
(src / "a.html.jsonl").write_text(json.dumps({"page": 1, "text": "Unrelated note: revenue USD 999 million"}) + "\n")
ctx = Path("cases/pins-context-owner/context-credit_snapshot.json").resolve()
p = cpos_launch.prepare(ctx, src, w / "out", config=sys.argv[2], cap="1000", modules=["CP-1"])
srcs = {k: v.path for k, v in p.plan.sources.items()}
print("pinned sources:", srcs)
print("converted written:", sorted(x.name for x in (w/"out"/"source-text").iterdir()))
print("HTML filing present as a source:", any(v.startswith("source-text/") for v in srcs.values()))
