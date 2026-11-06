"""A01: CP-1D accepted-basis quote: any lone numeral is read as a money amount in the
bridge's currency and unit (percent, count, other currency)."""
import copy, json
from decimal import Decimal
from pathlib import Path
from deploy_vii.contracts import Source, Span
from deploy_workflow.owners import cp1d

ROOT = Path(".")
CASE = ROOT / "cases" / "cp1d-owner"
MANIFEST = json.loads((CASE / "manifest.json").read_text())
SUBS = json.loads((CASE / "submissions.json").read_text())
FIN = json.loads((ROOT / "cases" / "financial" / "manifest.json").read_text())

def src(sid, name, pages, sha):
    return Source(source_id=sid, name=name, status="ready", sha256=sha, media_type="text/plain",
                  spans=tuple(Span(locator=p["locator"], text=p["text"]) for p in pages),
                  extraction_status="complete")

def cp1():
    cur = FIN["source_dimensions"]["currency"]
    f = {n: cp1d.Cp1Figure(fact_id=f"cp1:{n}", figure=n, label=v["label"], unit=v["unit"],
                           period=v["period"], amount=Decimal(v["amount_exact"]),
                           value_class=v["value_class"],
                           currency=cur if v["unit"] == "MILLIONS" else None)
         for n, v in MANIFEST["figures"].items()}
    return cp1d.Cp1Operands(adjusted_ebitda=f["adjusted_ebitda_ltm"], ebitda=f["ebitda_ltm"],
        cfo=f["cfo_ltm"], total_debt=f["total_debt_ltm"], net_debt=f["net_debt_ltm"],
        total_leverage=f["total_leverage_adjusted"], net_leverage=f["net_leverage_adjusted"])

syn = MANIFEST["synthetic_source"]
pages = copy.deepcopy(syn["positive"]["pages"])
SENT = {
  "percent": "Signed supplier contracts cover 2% of supplier spend.",
  "count": "Signed supplier contracts cover 2 of the ten supplier categories.",
  "currency": "Signed supplier contracts cover EUR 1.50m of the saving.",
  "bps": "Signed contracts improve margin by 1bps.",
}
pages[1]["text"] += "\n" + " ".join(SENT.values())
sha = syn["positive"]["sha256"]
frozen = tuple(src(s["source_id"], s["name"], s["pages"], s["sha256"]) for s in FIN["sources"])
bridge = src("bridge", syn["name"], pages, sha)
for kind, quote in SENT.items():
    pay = copy.deepcopy(SUBS["positive"]["earnings_quality"])
    a = pay["assessments"][0]
    a["accepted_basis"]["quote"] = quote
    a["evidence"][0]["quote"] = quote
    inputs = cp1d.EarningsQualityInputs(sources=(*frozen, bridge), cp1=cp1(),
        submission=cp1d.EarningsQualitySubmission.model_validate_json(json.dumps(pay)))
    issues = cp1d.validation_issues(inputs)
    if issues:
        print(kind, "REFUSED", issues[:3]); continue
    res = cp1d.compute(inputs)
    facts = {f.fact_id: f for f in res.facts}
    b = facts["T1D.2.a01.basis"]; acc = facts["T1D.2.a01.accepted"]
    print(kind, "ACCEPTED: basis", b.amount, b.unit, b.currency, "| accepted", acc.amount,
          acc.unit, "| fraction", facts["T1D.2.a01.applied_fraction"].amount)
