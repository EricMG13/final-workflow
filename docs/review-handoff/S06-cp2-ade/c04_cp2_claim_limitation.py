import sys
sys.path.insert(0, "tests")
from decimal import Decimal
from deploy_vii import cp2_synthesis as cs
from deploy_vii.contracts import Fact, Citation, Input
import test_engine_blank_text as tb
pack = tb._pack()
src = None
fact = Fact(fact_id="T4.10.lev", label="Total leverage", amount=Decimal("4.2"), unit="MULTIPLE",
            period="LTM Q3 2025",
            calculation_id="calc.lev")
cp1 = tb._module(cs.CP1).model_copy(update={"facts": (fact,)})
cp1a = tb._module(cs.CP1A)
inputs = (Input(input_id=cs.CP1, sha256=cp1.content_hash()), Input(input_id=cs.CP1A, sha256=cp1a.content_hash()))
up = cs.Upstream(bound=inputs, current=inputs, cp1=cp1, cp1a=cp1a, inherited=())
lim = "Leverage of {T4.10.lev|x} rests on LTM figures only."
sub = cs.CreditSynthesisSubmission(
    assessment=cs.Assessment(rationale="Credit profile is weak.", category="Insufficient Information",
                             confidence="Low", cp1a_refs=(), limitation=lim),
    thesis=cs.Thesis(text="Thesis text.", category="Insufficient Information", cp1a_refs=(), limitation="No evidence."),
    strengths=(), weaknesses=(), key_findings=(cs.Finding(text="Leverage stands at {T4.10.lev|x}.", cp1a_refs=()),), risks=(), gaps=())
print("issues:", cs.validate_credit_synthesis(pack, sub, up))
rep = cs.credit_synthesis(pack, sub, up)
claim = next(c for c in rep.claims if c.claim_id == "T2.1.assessment")
print("claim.limitation :", claim.limitation)
print("own limitation   :", [l for l in rep.limitations if "Leverage" in l])
cells = [f.text for f in rep.facts if f.table_id == "T2.1" and f.field == "limitation"]
print("T2.1 limitation cell:", cells)
