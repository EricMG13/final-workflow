"""CP-3C: a positive CP-1 cash_interest (interest received / sign anomaly) through compose_operands."""
from datetime import date
from decimal import Decimal as D
from deploy_workflow.owners import cp3c as c

M = "MILLIONS"
def f(amount, period="LTM Q4 2025", table="T4.10"):
    return c.Cp1Fact(table_id=table, period=period, status="known", amount=D(amount), unit=M, currency="USD")
def t(text):
    return c.Cp1Fact(table_id="T4.18", period="Q4 2025", status="known", text=text)
def d(fid, amount=None, text=None, unit=M):
    return c.Cp2dFact(fact_id=fid, status="known", amount=None if amount is None else D(amount), text=text, unit=unit,
                      currency="USD" if unit == M else None)

def run(interest):
    cp1 = c.Cp1Operands(cash_closing=f("100"), undrawn_rcf=f("50"), adjusted_ebitda=f("200"),
        cash_interest=f(interest),
        facilities=(c.FacilityTerms("tlb", "USD", t("TLB"), t("SECURED"), t("SENIOR"),
                                    c.Cp1Fact(table_id="T4.18", period="Q4 2025", status="known", amount=D("0"), unit=M, currency="USD")),))
    cp2d = c.Cp2dOperands(horizon=d("h", "24", unit="months"), run_rate=d("rr", "20"), minimum_cash=d("mc", "10"),
        funding_gap=d("fg", "0"),
        wall=(c.WallRow("tlb", d("p", "1000"), d("m", text="2027-06-30", unit=None), d("mo", "18", unit="months"), d("in", text="Yes", unit=None)),))
    ops = c.compose_operands(cp1=cp1, cp2d=cp2d, balance_date=date(2025, 12, 31), currency="USD")
    r = c.compose_refinancing(operands=ops, step_up_bps=500)
    print(f"cash_interest={interest}: paid={r.cash_interest_paid} added={r.added_interest} "
          f"pro_forma={r.pro_forma_interest} cover={r.interest_cover} pro_forma_cover={r.pro_forma_interest_cover}")

run("-40")   # normal outflow
run("40")    # positive figure: no refusal, paid becomes -40
