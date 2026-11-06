"""Collect every section report into ALL-FINDINGS.md and a findings index (findings.json)."""
import json, re, sys
from pathlib import Path
R = Path(__file__).parent
secs = sorted(p for p in R.iterdir() if p.is_dir() and p.name[:1] == "S")
H = re.compile(r"^### (S\d\d-[\w-]+-(?:A|C)\d+)\s+\[(\w+)\]\s+\[(\w+)\]\s*(.*)$", re.M)
idx, out, missing = [], ["# All findings (adversarial + /code-review)", ""], []
for s in secs:
    for p in ("adversarial", "code-review"):
        f = s / f"{p}.md"
        if not f.exists():
            missing.append(f"{s.name}/{p}.md"); continue
        t = f.read_text()
        out += [f"\n\n---\n\n# {s.name} — {p}\n", t]
        for m in H.finditer(t):
            body = t[m.end():].split("\n### ", 1)[0]
            loc = re.search(r"Location:\s*(.+)", body)
            idx.append({"id": m[1], "section": s.name, "pass": p, "severity": m[2].lower(),
                        "verdict": m[3].upper(), "category": m[4].strip(),
                        "location": loc[1].strip() if loc else ""})
(R / "ALL-FINDINGS.md").write_text("\n".join(out))
(R / "findings.json").write_text(json.dumps(idx, indent=1))
from collections import Counter
print("reports missing:", missing)
print("findings:", len(idx), Counter((i["pass"], i["severity"]) for i in idx))
