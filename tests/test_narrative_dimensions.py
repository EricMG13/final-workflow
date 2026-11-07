"""CP-1 narrative scope per financial dimension (ruling S13-vii-canonical-context-A07).

Expected values are hand-derived from the ruling, not from the code under test: leverage and
coverage are in scope only with an available ratio KPI of their own kind (a leverage multiple,
a coverage multiple); liquidity only with an available value KPI among cash_closing, liquidity,
undrawn_rcf, total_debt; cash_flow_quality only with fcf, ffo or cfo_adjusted. A bare revenue
value, an unavailable amount or a ratio of another family supports none of them.
"""

from decimal import Decimal
from types import SimpleNamespace

import pytest

from deploy_vii.canonical_kpis import CanonicalKpi
from deploy_vii.financial_model import MetricLeg
from deploy_vii.financial_periods import PeriodValue
from deploy_vii.narrative import financial_dimensions

LEG = MetricLeg(amount=None, operands=())


def _kpi(operation: str, key: str, amount: str | None = "1.5") -> CanonicalKpi:
    return CanonicalKpi(
        calculation_id=f"kpi-{operation}-{key}",
        display_basis_id="basis-fy2025",
        period_basis_id="basis-fy2025",
        key=key,
        operation=operation,  # type: ignore[arg-type]
        unit="MULTIPLE" if operation == "ratio" else "MILLIONS",
        currency="USD",
        input_scale="MILLIONS",
        formula=key,
        numerator=LEG,
        denominator=None,
        value=PeriodValue(
            amount=None if amount is None else Decimal(amount),
            stated_amount=None,
            value_class="calculated",
            calculation_status="Calculated" if amount else "Not Available",
            reason=None if amount else "NOT_SOURCED",
            note=None,
            observation_ids=(),
            issuance_facility_ids=(),
            citations=(),
        ),
    )


def _ledger(*kpis: CanonicalKpi | None) -> SimpleNamespace:
    """Only `ledger.kpis.kpis` is read; None stands for a ledger with no KPI report."""
    return SimpleNamespace(kpis=None if kpis == (None,) else SimpleNamespace(kpis=kpis))


@pytest.mark.parametrize(
    ("kpis", "want"),
    [
        # no KPI report at all, and a pack with only a revenue figure: none in scope
        ((None,), ()),
        ((_kpi("value", "revenue", "100"),), ()),
        # the revenue figure beside every unavailable ratio: still none
        (
            (
                _kpi("value", "revenue", "100"),
                _kpi("ratio", "total_leverage_reported", None),
                _kpi("ratio", "interest_coverage_reported", None),
            ),
            (),
        ),
        # only a leverage ratio (net leverage adjusted): leverage alone
        ((_kpi("value", "revenue", "100"), _kpi("ratio", "net_leverage_adjusted")), ("leverage",)),
        # only a coverage ratio: coverage alone
        ((_kpi("ratio", "ffo_interest_coverage"),), ("coverage",)),
        # only cash values: liquidity from cash_closing, nothing for cash flow
        ((_kpi("value", "cash_closing", "40"),), ("liquidity",)),
        ((_kpi("value", "total_debt", "900"),), ("liquidity",)),
        # cash-flow values: fcf alone supports cash_flow_quality
        ((_kpi("value", "fcf", "-3"),), ("cash_flow_quality",)),
        ((_kpi("value", "cfo_adjusted", "12"),), ("cash_flow_quality",)),
        # a ratio of another family (fcf_to_debt, liquidity_to_debt) supports neither dimension
        ((_kpi("ratio", "fcf_to_debt"), _kpi("ratio", "liquidity_to_debt")), ()),
        # a value row named like a ratio, or a ratio named like a value, is the wrong operation
        ((_kpi("value", "total_leverage_reported"), _kpi("ratio", "cash_closing")), ()),
        # growth rows of a supporting key do not count
        ((_kpi("growth", "fcf_growth"),), ()),
        # all of them, in dimension order
        (
            (
                _kpi("value", "liquidity", "75"),
                _kpi("value", "ffo", "10"),
                _kpi("ratio", "interest_coverage_adjusted"),
                _kpi("ratio", "senior_secured_leverage"),
            ),
            ("leverage", "coverage", "cash_flow_quality", "liquidity"),
        ),
    ],
)
def test_dimensions_follow_their_supporting_kpis(
    kpis: tuple[CanonicalKpi | None, ...], want: tuple[str, ...]
) -> None:
    assert financial_dimensions(_ledger(*kpis)) == want  # type: ignore[arg-type]
