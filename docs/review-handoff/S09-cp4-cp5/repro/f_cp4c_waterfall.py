from decimal import Decimal as D
from fractions import Fraction as F
from deploy_workflow.owners import cp4c as c
def cc(i, r, a): return c.ClassClaim(i, i, r, c.Val(D(a)) if a is not None else c.Val(None, "Not calculable: x"))
w = c.waterfall(classes=[cc("c01",1,"50"), cc("c02",2,"20"), cc("c03",2,"10")], enterprise_value=c.Val(D("60")))
for k,v in w.classes.items(): print(k, v.distribution.amount, v.recovery.amount, v.shortfall.amount)
print("residual", w.residual, "break", w.value_break, "through", w.break_through, "total", w.total_claims)
s = sum(F(v.distribution.amount) for v in w.classes.values()) + F(w.residual.amount)
print("conservation exact:", s == 60)
# EV exactly equal to all claims: no impairment -> equity break with residual 0
w = c.waterfall(classes=[cc("c01",1,"50"), cc("c02",2,"30")], enterprise_value=c.Val(D("80")))
print("EV==claims ->", w.value_break, w.residual)
# missing middle rank blocks lower ranks, never zero
w = c.waterfall(classes=[cc("c01",1,"50"), cc("c02",2,None), cc("c03",3,"5")], enterprise_value=c.Val(D("100")))
for k,v in w.classes.items(): print(k, v.distribution, v.recovery)
print("residual", w.residual, "break", w.value_break, w.break_reason)
# EV 0 -> c01 recovery 0, break at rank 1
w = c.waterfall(classes=[cc("c01",1,"50"), cc("c02",2,"30")], enterprise_value=c.Val(D("0")))
print("EV0", {k:(v.distribution.amount, v.recovery.amount) for k,v in w.classes.items()}, w.value_break)
