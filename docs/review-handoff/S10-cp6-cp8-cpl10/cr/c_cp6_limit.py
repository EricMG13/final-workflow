"""code-review repro: CP-6 claim limitations keep raw {ref|unit} tokens; the table cell spells them."""
from datetime import date
from decimal import Decimal
from deploy_vii import cp6_committee as c6
from deploy_vii.contracts import Citation, Fact, Module, Run
from deploy_vii.preparation import PreparedPack

pack = PreparedPack(run=Run(run_id="run-1", issuer_id="acme", issuer_name="Acme",
    as_of=date(2026, 1, 1), case_kind="synthetic"), sources=())
fact = Fact(fact_id="T4.10.ebitda.fy2025", label="EBITDA FY2025", table_id="T4.10", row_id="ebitda",
    field="fy2025", status="known", amount=Decimal("120"), unit="MILLIONS", currency="USD",
    scale=Decimal(1000000), decimals=0, period="FY2025", calculation_id="calc-1")
def mod(mid, facts=()):
    return Module(run_id="run-1", issuer_id="acme", as_of=date(2026, 1, 1), module_id=mid, facts=facts)
from deploy_vii.contracts import Input
mods = {"CP-0": mod("CP-0"), "CP-1": mod("CP-1", (fact,)), "CP-2": mod("CP-2"), "CP-3": mod("CP-3"), "CP-5": mod("CP-5")}
inputs = tuple(Input(input_id=k, sha256=m.content_hash(), status="accepted") for k, m in mods.items())
up = c6.Upstream(bound=inputs, current=inputs, cp0=mods["CP-0"], cp1=mods["CP-1"], cp2=mods["CP-2"],
    cp3=mods["CP-3"], cp5=mods["CP-5"], optional={}, blocked=frozenset(), inherited=())
print("forced insufficient:", up.insufficient)
from deploy_vii import prose
bound = prose.bind(c6.referencable(up.cp1.facts))
print("bound refs:", list(bound))
ref = "{T4.10.ebitda.fy2025|US$ m}"
basis = c6.Basis(cp2_refs=(), cp3_refs=(), cp5_refs=())
sub = c6.CommitteeSubmission(
    recommendation=c6.Recommendation(action_bias="Insufficient Information",
        rationale="Market evidence is absent", conditions="Obtain a quotation",
        confidence="Insufficient Information", limitation=f"CP-1 shows EBITDA of {ref} only", basis=basis),
    thesis_challenges=(), recovery_view=(), risks=(), gaps=())
issues = c6.validate_committee(pack, sub, up)
print("issues:", issues)
if not issues:
    rep = c6.committee_challenge(pack, sub, up)
    t = next(t for t in rep.tables if t.table_id == c6.FINAL_BIAS_TABLE)
    facts = {f.fact_id: f for f in rep.facts}
    cell = [facts[i].text for i in t.rows[0].fact_ids]
    print("table limitation cell:", cell[-1])
    print("claim limitation:", rep.claims[0].limitation)

# efficiency: the _validate_step sequence (validate_committee, then committee_challenge) validates twice
calls = []
orig = c6.validate_committee
def counting(*a, **k):
    calls.append(1)
    return orig(*a, **k)
c6.validate_committee = counting
if not c6.validate_committee(pack, sub, up):
    c6.committee_challenge(pack, sub, up)
print("validate_committee calls per _validate_step:", len(calls))
