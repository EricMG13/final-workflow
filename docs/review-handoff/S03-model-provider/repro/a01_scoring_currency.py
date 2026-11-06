"""Attack: scorer ignores currency. Golden USD 100 million; module says EUR 100 million."""
from datetime import date
from decimal import Decimal
from pathlib import Path
from deploy_vii.contracts import Fact, Module, Citation
from deploy_workflow.model_testing.cases import GoldenCase
from deploy_workflow.model_testing.mapping import Mapping, MappingEntry, Locator
from deploy_workflow.model_testing.scoring import score_module

golden = {"fact_id": "CP-1.fin.rev", "module": "CP-1", "subject": "Revenue", "status": "known",
          "value": "100", "value_type": "decimal", "unit": "USD", "scale": "millions",
          "evidence": []}
case = GoldenCase("c", "credit_snapshot", Path("."), Path("."), {"CP-1.fin.rev": golden}, {}, Path("."), "0"*64)
entry = MappingEntry(fact_id="CP-1.fin.rev", module="CP-1",
                     locator=Locator(table_id="t", row_id="rev", field="value", period="FY2025"))
mapping = Mapping(schema_version="golden-mapping/1", case_id="c", preparer="a", reviewer="b",
                  module_commits={"CP-1": "0"*40}, entries=(entry,), unmapped=())

cit = Citation(source_id="s1", source_sha256="a"*64, locator="p1", quote="Revenue 100")
for cur in ("USD", "EUR", "JPY", None):
    fact = Fact(fact_id="f1", label="Revenue", table_id="t", row_id="rev", field="value",
                amount=Decimal(100), unit="MILLIONS", scale=Decimal(1000000), currency=cur,
                period="FY2025", citations=(cit,))
    mod = Module(run_id="r", issuer_id="i", as_of=date(2026,1,1), module_id="CP-1", facts=(fact,))
    s = score_module(mod, "CP-1", "accepted", case, mapping, frozenset())
    print(f"module currency={cur!r:6} golden=USD -> outcome={s.facts[0].outcome} passed={s.passed}")
