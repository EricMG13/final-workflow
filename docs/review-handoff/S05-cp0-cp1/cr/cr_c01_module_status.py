"""CR-C01: CP-1 QA module_status is 'restricted' even when narrative is a clean candidate."""
import importlib, sys, tempfile
from pathlib import Path
sys.path.insert(0, "tests")
from deploy_vii import cp1_quality
seen = []
orig = cp1_quality._module_status
def spy(n):
    r = orig(n)
    seen.append((n.status, len(n.gaps), len(n.limitations), r))
    clean = n.model_copy(update={'status': 'candidate', 'gaps': ()})
    seen.append((clean.status, len(clean.gaps), len(clean.limitations), orig(clean)))
    seen.append(('candidate', 0, 0, orig(clean.model_copy(update={'limitations': ()}))))
    return r
cp1_quality._module_status = spy
fw = importlib.import_module("test_financial_workflow")
with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
    fw.promoted_case(Path(d) / "case")
print("limitations text:", [l[:50] for l in clean_lims] if False else "")
for s in dict.fromkeys(seen):
    print("narrative.status=%s gaps=%d limitations=%d -> module_status=%s" % s)
