"""code-review repro: CP-8 decision text that copies a page's em dash is rejected."""
import hashlib, sys
sys.path.insert(0, "tests")
import test_method_cp8 as t
from deploy_vii.contracts import Source, Span
from deploy_workflow.owners.cp8 import validate_ledger

def patched_pack(old, new):
    out = []
    for s in t.pack("positive"):
        if s.source_id == "prior_case":
            spans = tuple(Span(locator=p.locator, text=p.text.replace(old, new)) for p in s.spans)
            assert any(new in p.text for p in spans)
            sha = hashlib.sha256("\f".join(p.text for p in spans).encode()).hexdigest()
            s = s.model_copy(update={"spans": spans, "sha256": sha})
        out.append(s)
    return tuple(out)

for dash in ("-", "—"):
    role = f"Investment Committee {dash} Europe"
    packed = patched_pack("Decision-maker role: Investment Committee.", f"Decision-maker role: {role}.")
    lit = t.positive()
    lit["decision"]["decision_maker_role"] = {"text": role, "quote": {"source_id": "prior_case",
        "locator": "page:1", "quote": f"Decision-maker role: {role}."}}
    print(repr(dash), validate_ledger(submission=t.submission(lit), upstream=t.upstream("positive"), pack=packed))
