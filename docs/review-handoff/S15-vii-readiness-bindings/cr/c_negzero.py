from decimal import Decimal
from types import SimpleNamespace
from deploy_vii.model_interface import _observed
from deploy_vii.financial_contracts import Observation
from deploy_vii.contracts import Citation, Fact
c = Citation(source_id="s", source_sha256="a"*64, locator="page:1", quote="Dividends paid 0")
for raw in ("0", "0.00", "-12.5"):
    obs = Observation(observation_id="o", status="known", amount=Decimal(raw), citations=(c,))
    cell = _observed(obs, SimpleNamespace(unit="MILLIONS", currency="USD"), outflow=True)
    f = Fact(fact_id="f", label="v", amount=cell.value, unit="MILLIONS", period="FY25",
             value_class=cell.value_class, source_amount=cell.source_amount)
    print(raw, "->", f.model_dump_json(include={"amount", "value_class", "source_amount"}), "formula:", cell.formula)
from deploy_vii.render import display
for amt in ("-0", "0", "-0.00"):
    print(amt, "display ->", repr(display(Fact(fact_id="f", label="v", amount=Decimal(amt), unit="MILLIONS", currency="USD", period="FY25"))))
