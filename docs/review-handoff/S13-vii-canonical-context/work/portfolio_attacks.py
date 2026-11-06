import io, sys, copy
sys.path.insert(0, "tests/product")
import openpyxl
# minimal copy of tests' valid() fixture (cannot import: test module needs missing `scripts`)
import importlib.util, types
src = open("tests/product/test_inputs_portfolio.py").read()
start = src.index("BRIEF_SHEETS: dict")
end = src.index("HOLDING = {")
ns = {"Any": object, "date": __import__("datetime").date}
exec("from typing import Any\n" + src[start:end], ns)
valid, BRIEF = ns["valid"], ns["BRIEF_SHEETS"]
from deploy_vii.inputs.portfolio import validate_portfolio_bytes, portfolio_facts
from deploy_vii.preparation import SourceRequest, prepare_source
from deploy_vii.inputs.portfolio import MEDIA_TYPE

def build(data, tweak=None):
    wb = openpyxl.Workbook(); wb.remove(wb.active)
    for name, cols in BRIEF.items():
        if name not in data: continue
        ws = wb.create_sheet(name)
        ws.append(list(cols))
        for row in data[name]:
            ws.append([row.get(c) for c in cols])
    if tweak: tweak(wb)
    b = io.BytesIO(); wb.save(b); return b.getvalue()

def facts(raw):
    s = prepare_source(SourceRequest(source_id="portfolio", path="p.xlsx", media_type=MEDIA_TYPE), raw)
    return portfolio_facts(s)

def run(label, data, tweak=None):
    raw = build(data, tweak)
    r = validate_portfolio_bytes("p.xlsx", raw)
    print(f"--- {label}: ok={r.ok}", [i.problem for i in r.issues][:4])
    return raw, r

run("baseline", valid())

# A: Exposure value in % NAV stored as percent-formatted fraction
d = valid(); d["Exposure_Summary"].append({"metric":"cash","value":0.025,"unit":"% NAV","as_of":"2026-05-29"})
def fmt(wb):
    wb["Exposure_Summary"]["B4"].number_format = "0.00%"
raw, r = run("A exposure %NAV percent-formatted", d, fmt)
if r.ok: print("   cash value read as", [e.value for e in facts(raw).exposures if e.metric=="cash"])

# B: hidden stale row in Top_Holdings
d = valid(); d["Top_Holdings"].append({"rank":3,"issuer":"Stale Old Holding","instrument":"TL","pct_nav":"9.9","rating":"B"})
def hide(wb): wb["Top_Holdings"].row_dimensions[4].hidden = True
raw, r = run("B hidden row", d, hide)
if r.ok: print("   holdings", [h.issuer for h in facts(raw).top_holdings])

# C: hidden sheet
def hides(wb): wb["Maturity_Profile"].sheet_state = "hidden"
run("C hidden sheet", valid(), hides)

# D: negative pct_nav and par
d = valid(); d["Maturity_Profile"][0]["pct_nav"] = "-40"; d["Maturity_Profile"][1]["pct_nav"]="140"
run("D negative maturity pct_nav", d)

# E: exposure nav as_of differs from mandate as_of; compliance checked a year earlier
d = valid(); d["Exposure_Summary"][0]["as_of"] = "2024-12-31"
for c in d["Compliance_Monitor"]: c["last_checked"] = "2025-01-15"
run("E date mismatch as_of", d)

# F: merged cell spanning rows of Top_Holdings rating
d = valid()
def merge(wb): wb["Top_Holdings"].merge_cells("E2:E3")
run("F merged", d, merge)

# G: Ratings sum check passes with negative bucket
d = valid(); d["Rating_Distribution"] = [{"rating_bucket":"B","pct_nav":"150","issuers":8},{"rating_bucket":"Unrated","pct_nav":"-50","issuers":0}]
run("G negative rating bucket", d)
