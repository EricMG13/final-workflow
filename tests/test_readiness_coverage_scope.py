"""Absence claims are compared only with the pack sources they are about (S15 C01).

Before the fix a CONDITIONAL consumer's `missing_source` (about a source outside the pack) was
checked against the consumer's attached sources, or every ready paged source, and an uncited gap
description against every paged source. A true statement that pages of a document never supplied
are absent then counted as a contradiction of the pack's own coverage.

The pack: `annual-report` (ar.pdf), ready, pages 1-100 retained; `compliance-cert`, missing.
Expected issues are derived by hand from those page numbers.
"""

from datetime import date

from deploy_vii.contracts import Citation, Claim, Run, Source, Span
from deploy_vii.preparation import PreparedPack
from deploy_vii.readiness import (
    ConsumerReadiness,
    ReadinessGap,
    ReadinessReview,
    SourceAssessment,
    coverage_issues,
)

H = "a" * 64
AR = Source(
    source_id="annual-report",
    name="ar.pdf",
    status="ready",
    sha256=H,
    spans=tuple(Span(locator=f"page:{i}", text=f"p{i}") for i in range(1, 101)),
)
CC = Source(
    source_id="compliance-cert",
    name="cc.pdf",
    status="missing",
    limitation="Requested file is absent",
)
RUN = Run(
    run_id="r1", issuer_id="i1", issuer_name="Issuer", as_of=date(2026, 1, 1), case_kind="synthetic"
)
PACK = PreparedPack(run=RUN, sources=(AR, CC))
CITE = Citation(source_id="annual-report", source_sha256=H, locator="page:1", quote="p1")


def _contradiction(first: int, last: int) -> str:
    return (
        f"Absence claim contradicts extraction coverage: page:{first} to page:{last} retained in "
        "annual-report"
    )


def _review(
    *,
    missing_source: str = "Covenant certificate not supplied",
    source_ids: tuple[str, ...] = (),
    limitations: tuple[str, ...] = ("Covenant certificate absent",),
    gap: str = "Facility agreement not supplied",
    gap_citations: tuple[Citation, ...] = (),
) -> ReadinessReview:
    return ReadinessReview(
        pack_sha256=PACK.content_hash(),
        objective="x",
        reporting_period="FY25",
        issuer_confirmed=True,
        sources=(
            SourceAssessment(
                source_id="annual-report",
                document_family="AR",
                authority="filed",
                entity="I",
                period="FY25",
                version_relationship="final",
                fidelity="verified",
                citations=(CITE,),
            ),
        ),
        consumers=(
            ConsumerReadiness(
                module_id="CP-4",
                readiness="CONDITIONAL",
                evidence_demand="covenants",
                source_ids=source_ids,
                rationale="needs certificate",
                citations=(),
                missing_source=missing_source,
                limitations=limitations,
            ),
        ),
        gaps=(
            ReadinessGap(
                gap_id="g1",
                kind="source",
                severity="material",
                description=gap,
                affected_modules=("CP-4",),
                remediation="Upload it",
                citations=gap_citations,
            ),
        ),
        analysis=(
            Claim(claim_id="c1", text="Annual report is the only source.", citations=(CITE,)),
        ),
    )


def test_true_absence_of_documents_never_supplied_is_not_a_contradiction() -> None:
    review = _review(
        missing_source="Compliance certificate pages 1-20 not supplied",
        gap="Facility agreement pages 30-45 not supplied",
    )
    assert coverage_issues(PACK, review) == ()


def test_missing_source_is_not_read_against_the_consumers_attached_sources() -> None:
    # the consumer uses the annual report; its missing source is another document
    review = _review(
        source_ids=("annual-report",),
        missing_source="Compliance certificate pages 1-20 not supplied",
    )
    assert coverage_issues(PACK, review) == ()


def test_an_uncited_gap_that_names_a_pack_source_is_still_checked() -> None:
    # "Annual report" names annual-report as whole words; it retains pages 30-45
    review = _review(gap="Annual report pages 30-45 not supplied")
    assert coverage_issues(PACK, review) == (_contradiction(30, 45),)


def test_a_missing_source_that_names_a_pack_source_is_still_checked() -> None:
    review = _review(missing_source="ar.pdf pages 1-20 not supplied")
    assert coverage_issues(PACK, review) == (_contradiction(1, 20),)


def test_a_cited_gap_and_an_attached_limitation_keep_their_own_scope() -> None:
    # neither text names a source; the citation and the attachment still scope them
    review = _review(
        source_ids=("annual-report",),
        limitations=("pages 5-6 are absent",),
        gap="pages 30-45 not supplied",
        gap_citations=(CITE,),
    )
    assert coverage_issues(PACK, review) == (
        _contradiction(5, 6),
        _contradiction(30, 45),
    )


def test_a_page_range_past_the_pack_named_source_is_not_flagged() -> None:
    # annual-report holds pages 1-100, so pages 101-120 are truly absent
    review = _review(gap="Annual report pages 101-120 not supplied")
    assert coverage_issues(PACK, review) == ()
