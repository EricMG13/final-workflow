"""A02: cp1_quality._lineage_basis gives a BLOCK reconciliation check with no calculated value
(components unavailable) the 'calculation' ceiling (Calculated, weight 9), while an absent
_VALUED amount gets 'missing' (Insufficient Information, weight 0)."""
import hashlib
from deploy_vii.financial_reconciliation import Reconciliation, ReconciliationTerm
from deploy_vii.narrative import EvidenceRecord
from deploy_vii.cp1_quality import _lineage_basis
from deploy_vii.quality import CEILINGS, WEIGHTS

H = hashlib.sha256(b"x").hexdigest()
term = ReconciliationTerm(label="Reported EBITDA", observation_id=None, original_amount=None,
                          amount=None, reason="Not reported in the source", citations=())
check = Reconciliation(check_id="chk-ebitda-bridge-fy2025", period_id="fy-2025",
    check_type="EBITDA_BRIDGE", metric_id="ebitda", reported=term, components=(term,),
    reported_value=None, calculated_value=None, difference=None, tolerance=None, status="BLOCK",
    formula="EBITDA = operating profit + D&A",
    explanation="Reported value or independent components are unavailable", context_citations=())
rec = EvidenceRecord(evidence_id="narrative-evidence-source-check-x", kind="source_check",
    reference=check.check_id, artifact_sha256=H, record_sha256=check.content_hash(),
    record_json=check.model_dump_json(), citations=())
basis = _lineage_basis(rec)
print("BLOCK check, calculated_value=None ->", basis, CEILINGS[basis], WEIGHTS[CEILINGS[basis]])
