# Count whole-file reads per handoff during one workspace_store() page load over the repo's runs.
import importlib.util, time, collections
from pathlib import Path
REPO = Path("/home/user/final-workflow")
spec = importlib.util.spec_from_file_location("store", REPO / "apps/issuer-library/engine/store.py")
store = importlib.util.module_from_spec(spec); spec.loader.exec_module(store)
reads = collections.Counter(); orig = Path.read_bytes
def counting(self): reads[str(self)] += 1; return orig(self)
Path.read_bytes = counting
runs = sorted(p.name for p in (REPO / "runs").iterdir() if p.is_dir())
t = time.time(); s = store.workspace_store(REPO, {"real": [{"id": r, "name": r} for r in runs]}); dt = time.time() - t
md = {k: v for k, v in reads.items() if k.endswith(".md")}
print(f"{len(md)} handoff files, {sum(md.values())} reads, {sum(orig(Path(k)).__len__()*v for k,v in md.items())/1e6:.1f} MB read vs {sum(len(orig(Path(k))) for k in md)/1e6:.1f} MB unique; {dt:.2f}s")
print("reads per file:", collections.Counter(md.values()))
