from datetime import date
from decimal import Decimal as D
from deploy_workflow.owners import valuation_basis as vb
from deploy_workflow.owners import pins
# window_start clamps
assert vb.window_start(date(2024,2,29),12) == date(2023,2,28)
assert vb.window_start(date(2025,3,31),1) == date(2025,2,28)
assert vb.window_start(date(2025,1,15),36) == date(2022,1,15)
# admission: zero / negative / nan / boundary date
R = lambda ev, eb, d=date(2025,1,1): vb.AdmittedRecord("user_comps","peer","x",d,"s",D(ev),D(eb))
a = vb.admit([R("0","1"),R("-1","1"),R("NaN","1"),R("10","0"),R("10","2",date(2024,1,1)),R("10","2",date(2023,12,31))], date(2025,1,1), 12)
print([(x.multiple, x.included, x.reason) for x in a])
assert a[4].included and not a[5].included and a[0].multiple is None and a[3].multiple is None
# selection limits
s = vb._chosen("u","u",D("99.994"),"r",D("100"))
print(s)
assert s.multiple == D("99.99") and s.implied_ev == D("9999.0000") or s.implied_ev == D("99.99")*100
s = vb._chosen("u","u",D("99.995"),"r",D("100")); print(s); assert s.multiple is None
s = vb._chosen("u","u",D("0.004"),"r",D("100")); print(s); assert s.multiple is None
s = vb._chosen("u","u",D("0.005"),"r",D("100")); print(s)  # half-even -> 0.00 -> gap
# pins _plain / _same
assert pins._plain(D("10.500")) == "10.5" and pins._plain(D("-0.0")) == "0" and pins._plain(D("1E+2")) == "100"
assert pins._same(D("0"), "-0") and not pins._same(D("1"), "1\n") and not pins._same(D("1"), " 1") and not pins._same(D("1"), "١")
assert not pins._same(D("1"), "1e0") and pins._same(D("0.1"), "0.10")
print("ok")
