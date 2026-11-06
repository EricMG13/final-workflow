"""CP-2 synthesis: a Critical CP-1A gap is 'restated' by a gaps row of severity Minor, and the
module limitation is then 'Gap (Low): ...'. Also: a readiness row whose status cell is unsettled."""
import sys
from datetime import date
sys.path.insert(0, "tests")
import test_engine_blank_text as tb
from deploy_vii import cp2_synthesis as c2
from deploy_vii.contracts import Fact, Module, ReportTable, TableColumn, TableRow, Input

def tf(table, row, field, text, status="known"):
    return Fact(fact_id=f"{table}.{row}.{field}", label=field, table_id=table, row_id=row,
                field=field, text=text if status == "known" else None, status=status,
                limitation=None if status == "known" else "not stated")

facts = [tf("gaps_ledger", "g01", "gap", "No debt maturity schedule"),
         tf("gaps_ledger", "g01", "severity", "Critical"),
         tf("downstream_readiness", "r01", "status", "READY"),
         tf("downstream_readiness", "r01", "gap", "none")]
tables = (
    ReportTable(table_id="gaps_ledger", title="Gaps ledger", row_header="Item",
                columns=(TableColumn(field="gap", label="Gap"), TableColumn(field="severity", label="Severity")),
                rows=(TableRow(row_id="g01", label="Gap 1", fact_ids=("gaps_ledger.g01.gap", "gaps_ledger.g01.severity")),)),
    ReportTable(table_id="downstream_readiness", title="Downstream readiness", row_header="Module",
                columns=(TableColumn(field="status", label="Status"), TableColumn(field="gap", label="Gap")),
                rows=(TableRow(row_id="r01", label="CP-2", fact_ids=("downstream_readiness.r01.status", "downstream_readiness.r01.gap")),)),
)
cp1a = Module(run_id="run-1", issuer_id="acme", as_of=date(2026, 1, 1), module_id="CP-1A",
              facts=tuple(facts), tables=tables)
cp1 = tb._module("CP-1")
bound = (Input(input_id="CP-1", sha256=cp1.content_hash(), status="settled") if False else
         Input(input_id="CP-1", sha256=cp1.content_hash()),
         Input(input_id="CP-1A", sha256=cp1a.content_hash()))
up = c2.Upstream(bound=bound, current=bound, cp1=cp1, cp1a=cp1a, inherited=())
print("signals:", up.signals)
P = "Leverage is tight."
sub = c2.CreditSynthesisSubmission(
    assessment=c2.Assessment(rationale=P, category="Analyst Interpretation", confidence="Medium",
                             cp1a_refs=("gaps_ledger.g01",), limitation=None),
    thesis=c2.Thesis(text=P, category="Analyst Interpretation", cp1a_refs=("gaps_ledger.g01",), limitation=None),
    strengths=(), weaknesses=(),
    key_findings=(c2.Finding(text=P, cp1a_refs=("gaps_ledger.g01",)),),
    risks=(),
    gaps=(c2.SynthesisGap(gap="Minor wording point", why_it_matters=P, affected_analysis=P,
                          severity="Minor", action=P, cp1a_refs=("gaps_ledger.g01",)),),
)
pack = tb._pack()
print("issues:", c2.validate_credit_synthesis(pack, sub, up))
rep = c2.credit_synthesis(pack, sub, up)
print("limitations:", rep.limitations)
