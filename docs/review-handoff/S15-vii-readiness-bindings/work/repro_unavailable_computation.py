"""_evidence_tags must not tag unavailable numeric evidence (its docstring). A computation whose
value.amount is None (operation 'unavailable') is still tagged 'computation', which is the only
group `calculation_register` needs (and one of the two `fcf_build` needs)."""
import json
from deploy_vii.downstream_readiness import _evidence_tags, _EVIDENCE_GROUPS, EvidenceRecord
H = "0" * 64
def rec(kind, data):
    return EvidenceRecord(evidence_id="e1", kind=kind, reference="r", artifact_sha256=H,
                          record_sha256=H, record_json=json.dumps(data), citations=())
comp = {"computation_id": "c1", "operation": "unavailable", "operands": [],
        "value": {"amount": None, "stated_amount": None, "value_class": "calculated",
                  "calculation_status": "Not Available", "reason": "missing input", "note": None,
                  "observation_ids": [], "issuance_facility_ids": [], "citations": []},
        "formula": "unavailable"}
kpi = {"key": "fcf", "value": {"amount": None}}
t_comp = _evidence_tags(rec("computation", comp)); t_kpi = _evidence_tags(rec("kpi", kpi))
print("unavailable kpi tags:", t_kpi, "(expected empty)")
print("unavailable computation tags:", t_comp, "(expected empty)")
groups = _EVIDENCE_GROUPS["calculation_register"]
print("calculation_register satisfied by unavailable computation:",
      not any(t_comp.isdisjoint(g) for g in groups))
