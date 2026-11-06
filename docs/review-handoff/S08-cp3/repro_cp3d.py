"""CP-3D adversarial repros: hostile market pages fed to the real validator and composer."""
import copy, json, sys
from datetime import date
from pathlib import Path
sys.path.insert(0, "tests")
from deploy_workflow.owners import cp3d

ROOT = Path(".")
CASE = ROOT / "cases" / "cp3d-owner"
SUB = json.loads((CASE / "submissions.json").read_text())
MAN = json.loads((CASE / "manifest.json").read_text())
FIN = json.loads((ROOT / "cases/financial/manifest.json").read_text())

def pages():
    p = {s["source_id"]: {x["locator"]: x["text"] for x in s["pages"]} for s in FIN["sources"]}
    m = MAN["market_source_pin"]
    p[m["source_id"]] = {x["locator"]: x["text"] for x in m["pages"]}
    return p

def ctx(pg, as_of="2026-01-10"):
    return cp3d.MarketContext(pages=pg, names={k: k for k in pg}, third_party=frozenset({"market"}),
        published=cp3d.publication_dates(pg), run_as_of=date.fromisoformat(as_of), context_quote_rows={})

def run(label, pg, raw, as_of="2026-01-10"):
    sub = cp3d.MarketImpliedSubmission.model_validate_json(json.dumps(raw))
    c = ctx(pg, as_of)
    issues = cp3d.submission_issues(submission=sub, context=c)
    print(f"== {label}: issues={list(issues)}")
    if not issues:
        res = cp3d.market_implied_result(submission=sub, context=c)
        st = res.derived.stored()
        print("   bid", st["bid"], "offer", st["offer"], "mid", st["mid"], "years", st["years"],
              "dm_mid", st["dm_mid"], "pd_mid", st["pd_mid"], "dm_bid", st["dm_bid"], "pd_bid", st["pd_bid"])
        lims = res.own_limitations
        print("   stale/indicative/conditional in limitations:",
              [l for l in lims if any(w in l.lower() for w in ("stale", "indicative", "conditional", "subject", "days before"))])

base = SUB["positive"]
P1 = MAN["market_source_pin"]["pages"][0]["text"]
QUOTE = "Dealer quotation on January 9, 2026: bid 98.50 and offer 99.25, expressed as a percentage of par."

def with_quote(new_quote, page_extra_replace=None):
    pg = pages()
    pg["market"]["page:1"] = P1.replace(QUOTE, new_quote)
    raw = copy.deepcopy(base)
    for o in raw["observations"][:2]:
        o["quote"] = new_quote
    return pg, raw

# baseline
run("baseline", pages(), base)

# 1. conditional / indicative quote presented as executable bid/offer
q = "Indicative dealer quotation on January 9, 2026, subject to confirmation and not firm: bid 98.50 and offer 99.25, expressed as a percentage of par."
pg, raw = with_quote(q)
run("A1 indicative/subject-to bid-offer accepted as observed", pg, raw)

# 2. stale sheet quote: seven years before the run as-of
q = "Dealer quotation on January 9, 2019: bid 98.50 and offer 99.25, expressed as a percentage of par."
pg, raw = with_quote(q)
for o in raw["observations"][:2]:
    o["as_of_text"] = "January 9, 2019"
run("A2 quote 7 years before run as-of", pg, raw)

# 3. quotation date AFTER the run as-of (look-ahead)
q = "Dealer quotation on January 9, 2027: bid 98.50 and offer 99.25, expressed as a percentage of par."
pg, raw = with_quote(q)
for o in raw["observations"][:2]:
    o["as_of_text"] = "January 9, 2027"
run("A3 quote one year after run as-of 2026-01-10", pg, raw)

# 4. yield-quoted single side accepted as a price in points of par
q = "Dealer quotation on January 9, 2026: bid 6.25% yield to maturity."
pg, raw = with_quote(q)
raw["observations"] = [dict(raw["observations"][0], quote=q, level_text="6.25"), raw["observations"][2]]
run("A4 bid quoted as yield 6.25% read as price", pg, raw)

# 4b. spread-quoted single side
q = "Dealer quotation on January 9, 2026: bid 175 bps discount margin."
pg, raw = with_quote(q)
raw["observations"] = [dict(raw["observations"][0], quote=q, level_text="175"), raw["observations"][2]]
run("A4b bid quoted as 175 bps read as price", pg, raw)

# 5. wrong instrument: page carries a second instrument's quotation
pg = pages()
other = "Dealer quotation on January 9, 2026 for the Southgate Notes due 2027: bid 88.50 and offer 89.25, expressed as a percentage of par."
pg["market"]["page:1"] = P1 + "\n" + other
raw = copy.deepcopy(base)
raw["observations"][0].update(quote=other, level_text="88.50")
raw["observations"][1].update(quote=other, level_text="89.25")
run("A5 other instrument's quotation bound to Northbridge Term Loan", pg, raw)
