"""Fuzz load_context: every failure must be ContextRefused (a ValueError listing problems)."""
import json, random, copy
from pathlib import Path
from deploy_workflow.context import load_context, ContextRefused
base = json.loads(Path("/workspace/final-workflow/cases/pins-context-owner/context-credit_snapshot.json").read_text())
vals = ["", " ", "NaN", "1e5", "-0", "0x10", "1,000", "٣", "2026-02-30", "2026-13-01", "q5-2026", "fy-20255",
        None, 0, 1.5, True, [], {}, "a|b", "<<<", "x y", "\ud800", "9"*400, "-1", "100.001", "Infinity"]
def paths(o, p=()):
    if isinstance(o, dict):
        for k, v in o.items(): yield from paths(v, p + (k,))
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from paths(v, p + (i,))
    else: yield p
ps = list(paths(base)); random.seed(1); bad = {}
for _ in range(4000):
    doc = copy.deepcopy(base)
    p = random.choice(ps); v = random.choice(vals)
    t = doc
    for k in p[:-1]: t = t[k]
    t[p[-1]] = v
    raw = json.dumps(doc).encode("utf-8", "surrogatepass")
    try: load_context(raw)
    except ContextRefused: pass
    except Exception as e: bad.setdefault(type(e).__name__, (p, v, str(e)[:120]))
for t in ("schema", "run", "identity"):
    for v in vals[:8]:
        doc = copy.deepcopy(base); doc[t] = v
        try: load_context(json.dumps(doc).encode())
        except ContextRefused: pass
        except Exception as e: bad.setdefault(type(e).__name__ + "-top", (t, v, str(e)[:120]))
print(bad or "all failures were ContextRefused")
