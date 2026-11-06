"""Code-review repro: one figure's free-text currency with a pipe/newline makes the whole pack unusable."""
import copy, sys
sys.path.insert(0, "tests"); sys.path.insert(0, "tests/research")
from cpdr_peers_support import peers_case
from deploy_vii.contracts import Module, validate_tables
from deploy_workflow.research import peers as p
import test_owner_cpdr_peers as T
case = peers_case()
for cur in ("USD", "USD|x", "USD\n", "USD "):
    body = copy.deepcopy(case.body)
    body["peers"]["figures"][0]["currency"] = cur
    print(f"currency={cur!r} review issues={case.issues(body)}")
    comp = case.composed(body)
    validate_tables(comp.tables, comp.facts) if False else None
    mod = T._dr_module(list(comp.facts))
    sheet = p.peer_sheet(mod, T.DEFAULT_BASIS, issuer_name=T._run().issuer_name)
    if isinstance(sheet, p.PackUnusable):
        print("   -> PackUnusable:", sheet.reason)
    else:
        print("   -> rows:", [r.label for r in sheet.peers], "not_admitted:", [(n.peer_id, n.reason) for n in sheet.not_admitted])
