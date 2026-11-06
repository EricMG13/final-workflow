"""CP-5 figure_identity flags CP-4C's verbatim cp2g_references / cp2a_references copies."""
import importlib
from datetime import date
from deploy_vii.contracts import Module
from deploy_vii.cp5_integrity import figure_identity
from deploy_workflow.owners import cp4c
t = importlib.import_module("test_method_cp4c")
inputs = t._inputs("positive")
result = cp4c.compute(inputs)
base = dict(run_id="r", issuer_id="i", as_of=date(2025, 1, 1))
for ref in result.references[1:3]:  # cp2g_references, cp2a_references
    placed = cp4c._placed_references(ref)
    originals = tuple(r.fact for r in ref.rows)
    producer = "CP-2G" if ref.table_id == "cp2g_references" else "CP-2A"
    up = Module(module_id=producer, facts=originals, **base)
    own = Module(module_id="CP-4C", facts=placed, **base)
    found = figure_identity([up, own])
    print(ref.table_id, "copies:", len(placed), "figure copies:", sum(f.amount is not None for f in placed), "findings:", len(found))
    for f in found[:2]:
        print("  ", f.subject, "|", f.detail)
