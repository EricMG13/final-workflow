"""Code-review repro: TDR.6 quote is any substring of the span; unit/currency/period unchecked."""
import copy, sys
sys.path.insert(0, "tests/research")
from cpdr_peers_support import peers_case
case = peers_case()
src = {s.source_id: s for s in case.sources}
print("span ev-1 line:11 =", repr(next(sp.text for sp in src["ev-1"].spans if sp.locator == "line:11")))
for q in ("20", "0.0", "00"):
    body = copy.deepcopy(case.body)
    body["peers"]["figures"][0]["citation"]["quote"] = q
    iss = case.issues(body)
    fact = next(f for f in case.composed(body).facts if f.fact_id == "TDR.6.p01.revenue.amount")
    print(f"quote={q!r}: issues={iss} -> amount={fact.amount} status={fact.status}")
# currency / unit not checked against span
body = copy.deepcopy(case.body)
body["peers"]["figures"][0]["unit"] = "thousands"
body["peers"]["figures"][0]["currency"] = "EUR"
iss = case.issues(body)
fact = next(f for f in case.composed(body).facts if f.fact_id == "TDR.6.p01.revenue.amount")
print("unit=thousands currency=EUR: issues=", iss, "->", fact.amount, fact.unit, fact.currency, fact.period)
# free-text currency with newline / pipe
for cur in ("USD\n", "USD|x", "usd"):
    body = copy.deepcopy(case.body)
    body["peers"]["figures"][0]["currency"] = cur
    try:
        iss = case.issues(body)
        print(f"currency={cur!r}: issues={iss}")
    except Exception as e:
        print(f"currency={cur!r}: parse/raise {type(e).__name__}: {str(e)[:120]}")
