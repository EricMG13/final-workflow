from decimal import Decimal as D
from deploy_workflow.owners.cp2e import Operands, derive_sensitivity, _row_decimal
for tok in ("45", "(45)"):
    op = Operands(total_debt=D(500), ebitda=D(200), interest=_row_decimal(tok), fcf=D(60),
                  facility_balance=D(300), rate_type="FLOATING", floor_bp=D(0),
                  debt_foreign=False, foreign_ebitda_share=None)
    s = derive_sensitivity(operands=op, rate_shocks_bp=[D(200), D(500)], fx_shocks=[D("0.1")], hedge_ratio=None)
    print("interest token", tok, "cov_base", s.cov_base)
    for r in s.rate:
        print("  shock", r.shock_bp.amount, "gross", r.gross.amount, "interest_after", r.interest_after.amount,
              "cov_after", r.cov_after.amount, r.cov_after.state, r.cov_after.reason if hasattr(r.cov_after,'reason') else '')
print("--- outflow-presented interest (20), 1000bp on 300 floating")
op = Operands(total_debt=D(500), ebitda=D(200), interest=_row_decimal("(20)"), fcf=D(60),
              facility_balance=D(300), rate_type="FLOATING", floor_bp=D(0), debt_foreign=False)
s = derive_sensitivity(operands=op, rate_shocks_bp=[D(1000)], fx_shocks=[D("0.1")], hedge_ratio=None)
r = s.rate[0]
print("cov_base", s.cov_base.state, s.cov_base.reason, "| interest_after", r.interest_after.amount, "| cov_after", r.cov_after.state, r.cov_after.amount)
