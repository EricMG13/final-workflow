from datetime import date
from deploy_vii.contracts import Run, Source, Span, Citation, Claim
from deploy_vii.preparation import PreparedPack
from deploy_vii.readiness import ConsumerReadiness, ReadinessGap, ReadinessReview, SourceAssessment, coverage_issues

H = "a" * 64
ar = Source(source_id="annual-report", name="ar.pdf", status="ready", sha256=H,
            spans=tuple(Span(locator=f"page:{i}", text=f"p{i}") for i in range(1, 101)))
cc = Source(source_id="compliance-cert", name="cc.pdf", status="missing", limitation="Requested file is absent")
run = Run(run_id="r1", issuer_id="i1", issuer_name="Issuer", as_of=date(2026, 1, 1), case_kind="synthetic")
pack = PreparedPack(run=run, sources=(ar, cc))
cite = Citation(source_id="annual-report", source_sha256=H, locator="page:1", quote="p1")
review = ReadinessReview(
    pack_sha256=pack.content_hash(), objective="x", reporting_period="FY25", issuer_confirmed=True,
    sources=(SourceAssessment(source_id="annual-report", document_family="AR", authority="filed",
                              entity="I", period="FY25", version_relationship="final",
                              fidelity="verified", citations=(cite,)),),
    consumers=(ConsumerReadiness(module_id="CP-4", readiness="CONDITIONAL", evidence_demand="covenants",
                                 source_ids=(), rationale="needs certificate", citations=(),
                                 missing_source="Compliance certificate pages 1-20 not supplied",
                                 limitations=("Covenant certificate absent",)),),
    gaps=(ReadinessGap(gap_id="g1", kind="source", severity="material",
                       description="Facility agreement pages 30-45 not supplied",
                       affected_modules=("CP-4",), remediation="Upload it"),),
    analysis=(Claim(claim_id="c1", text="Annual report is the only source.", citations=(cite,)),),
)
for issue in coverage_issues(pack, review):
    print(issue)
