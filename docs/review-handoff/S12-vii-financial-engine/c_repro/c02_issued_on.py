"""C: financial_reconciliation._debt ignores issued_on; adapter reads 0 before issuance."""
from datetime import date
from decimal import Decimal as D
from test_cash_scope import book, cite, observation
from deploy_vii.financial_contracts import FacilityObservation, Observation, AccountObservation
from deploy_vii.financial_reconciliation import _debt
from deploy_vii.financial_adapter import _facilities

def nil(name):
    return Observation(observation_id=name, status="missing", amount=None, citations=(), reason="n/a")

def fac(fid, pid, amount, issued=None):
    c = cite(f"{fid} {amount}", "page:70")
    return FacilityObservation(
        facility_id=fid, facility_name=fid, period_id=pid, facility_type="TERM_LOAN",
        currency="USD", carrying_value=observation(f"cv-{fid}-{pid}", amount, c),
        principal=nil(f"p-{fid}-{pid}"), drawn_amount=nil(f"d-{fid}-{pid}"),
        commitment=nil(f"c-{fid}-{pid}"), secured_status="SECURED", seniority="SENIOR",
        lease_classification="NOT_LEASE", margin_or_coupon="Not stated", maturity_date=date(2030,1,1),
        maturity_limitation=None, rate_type="NOT_STATED", reference_rate="NOT_STATED",
        spread_bps=nil(f"s-{fid}-{pid}"), floor_bps=nil(f"f-{fid}-{pid}"),
        fixed_rate=nil(f"x-{fid}-{pid}"), annual_amortisation=nil(f"a-{fid}-{pid}"),
        terms_citations=(c,), issued_on=issued,
        issuance_citations=(cite("issued", "page:71"),) if issued else (),
    )

b = book()
pids = [p.period_id for p in b.periods if p.period_type == "PERIOD_END"]
print("balance periods:", pids)
facs = [fac("tl-a", pid, 100) for pid in pids]
# tl-b issued 2025-10-01: rows only at 2025-12-31 and 2026-06-30
facs += [fac("tl-b", pid, 50, issued=date(2025, 10, 1)) for pid in pids[2:]]
accts = [AccountObservation(metric_id="total_debt", period_id=pid,
                            value=observation(f"td-{pid}", 100, cite(f"Total debt 100 {pid}", "page:61")))
         for pid in pids[:2]]
b2 = b.model_copy(update={"facilities": tuple(facs), "accounts": tuple(accts)})
per = {p.period_id: p for p in b2.periods}
check = _debt(b2, per["bs-2025-06-30"], {})
print("financial_reconciliation DEBT_TOTAL_EX_LEASES at 2025-06-30:", check.status, check.calculated_value,
      [(t.label, t.amount, t.reason) for t in check.components], "|", check.explanation)
rows = [r for r in _facilities(b2) if r.period_id == "bs-2025-06-30"]
print("adapter facility rows at 2025-06-30:", [(r.facility_id, r.carrying_value) for r in rows])
