"""CP-1 QA lineage ceilings and module status, from the module's own registers only.

Expected values are hand-derived from the docstring rule of `cp1_quality._lineage_basis` (an
absent calculated amount, or a check that could not be computed or blocks, is missing evidence)
and the QA ceiling table in METHODOLOGY (missing -> Insufficient Information, weight 0;
calculation -> Calculated, weight 9), not from the code under test.
"""

import hashlib
from decimal import Decimal

import pytest

from deploy_vii.cp1_quality import _lineage_basis
from deploy_vii.financial_reconciliation import Reconciliation, ReconciliationTerm
from deploy_vii.narrative import EvidenceRecord

H = hashlib.sha256(b"x").hexdigest()


def _term(amount: str | None) -> ReconciliationTerm:
    return ReconciliationTerm(
        label="Reported EBITDA",
        observation_id=None,
        original_amount=None,
        amount=None if amount is None else Decimal(amount),
        reason="Not reported in the source" if amount is None else None,
        citations=(),
    )


def _check(status: str, calculated: str | None) -> EvidenceRecord:
    check = Reconciliation(
        check_id="chk-ebitda-bridge-fy2025",
        period_id="fy-2025",
        check_type="EBITDA_BRIDGE",
        metric_id="ebitda",
        reported=_term(None),
        components=(_term(calculated),),
        reported_value=None,
        calculated_value=None if calculated is None else Decimal(calculated),
        difference=None,
        tolerance=None,
        status=status,
        formula="EBITDA = operating profit + D&A",
        explanation="Reported value or independent components are unavailable",
        context_citations=(),
    )
    return EvidenceRecord(
        evidence_id="narrative-evidence-source-check-x",
        kind="source_check",
        reference=check.check_id,
        artifact_sha256=H,
        record_sha256=check.content_hash(),
        record_json=check.model_dump_json(),
        citations=(),
    )


@pytest.mark.parametrize(
    ("status", "calculated", "expected"),
    [
        # No calculated amount: nothing was calculated, so the lineage is missing evidence.
        ("BLOCK", None, "missing"),
        ("WARN", None, "missing"),
        # A computed check that blocks disagrees with its reported value: conflicting evidence.
        ("BLOCK", "120", "missing"),
        # A computed check that passes (or warns within its own rule) is a Python calculation.
        ("PASS", "120", "calculation"),
        ("WARN", "120", "calculation"),
    ],
)
def test_a_check_caps_at_calculated_only_when_it_computed_and_does_not_block(
    status: str, calculated: str | None, expected: str
) -> None:
    assert _lineage_basis(_check(status, calculated)) == expected
