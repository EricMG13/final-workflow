"""Code-review repro: NUL path raw ValueError; duplicate file -> two 'independent' items; family label variants."""
import sys
from datetime import date
from pathlib import Path
from deploy_workflow.research.intake import parse_rows, intake, IntakeError
from deploy_workflow.research import review

work = Path(sys.argv[1]); work.mkdir(exist_ok=True)
(work / "a.txt").write_text("Alder Ridge said revenue rose.\n", encoding="utf-8")
kw = dict(base_dir=work, dest_dir=None, as_of=date(2026, 1, 1), cutoff=date(2026, 1, 1), today=date(2026, 1, 1))

rows = parse_rows([{"path": "a\x00b.txt", "family": "Wire", "locator": "L1", "tag": "research", "published": "2025-01-01"}])
try:
    intake(rows, **kw); print("NUL path: no raise")
except IntakeError as e:
    print("NUL path: IntakeError", e)
except Exception as e:
    print("NUL path: RAW", type(e).__name__, e)

rows = parse_rows([
    {"path": "a.txt", "family": "Wire A", "locator": "L1", "tag": "research", "published": "2025-01-01"},
    {"path": "a.txt", "family": "Wire B", "locator": "L2", "tag": "research", "published": "2025-01-01"},
])
res = intake(rows, **kw)
print("duplicate file:", [(a.item_id, a.family, a.sha256[:12]) for a in res.accepted])
fam = {a.item_id: a.family for a in res.accepted}
print("  family issues for [ev-1, ev-2]:", review._family_issues("q1", ("ev-1", "ev-2"), fam))

for f1, f2 in (("Reuters", "Reuters"), ("Reuters", "reuters"), ("Reuters", "Reuters ")):
    print(f"families {f1!r}/{f2!r}:", review._family_issues("q1", ("ev-1", "ev-2"), {"ev-1": f1, "ev-2": f2}))
