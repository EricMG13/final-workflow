"""Earnings delta: equal-length guard vs leap year and calendar quarters."""
import hashlib, sys
sys.path.insert(0, "tests")
import test_earnings as t

def basis(kind, pid):
    col = f"{kind}:{pid}"
    payload = "".join(f"{len(p)}:{p}" for p in ("historical", col))
    return "model-basis:" + hashlib.sha256(payload.encode()).hexdigest()

t.DATES = {
    "fy-2024": ("FY", None, "2024-01-01", "2024-12-31", "FY24"),
    "fy-2025": ("FY", None, "2025-01-01", "2025-12-31", "FY25"),
    "q1-2025": ("QUARTER", "1", "2025-01-01", "2025-03-31", "Q1 25"),
    "q2-2025": ("QUARTER", "2", "2025-04-01", "2025-06-30", "Q2 25"),
    "q1-2024": ("QUARTER", "1", "2024-01-01", "2024-03-31", "Q1 24"),
}
t.BASES = {pid: basis("FY" if v[0] == "FY" else "Q", pid) for pid, v in t.DATES.items()}
fy = t.VALUES["fy-2025"]
t.VALUES = {pid: fy for pid in t.DATES}
m = t.fixture()
for prior, current in [("fy-2024", "fy-2025"), ("q1-2025", "q2-2025"), ("q1-2024", "q1-2025")]:
    try:
        r = t.build(m, prior, current)
        print(prior, current, "OK revenue delta", t.point(r, "revenue").delta)
    except ValueError as e:
        print(prior, current, "REFUSED", e)
