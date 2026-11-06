"""CP-0 attachment precheck: a gap about something else satisfies a declared attachment."""
from types import SimpleNamespace as NS
from deploy_workflow.owners.cp0_attachments import _issues

ctx = NS(attachments=NS(portfolio_workbook=True, prior_case=False, management_bridge=True,
                        legal_documents="executed"))
def review(*gaps, sources=()):
    return NS(gaps=[NS(kind="source", description=g) for g in gaps], sources=list(sources))
ready = frozenset({"annual_report"})

# 1. no gap at all -> all three issues expected
print("no gaps        :", _issues(ctx, review(), ready))
# 2. gaps that are about unrelated things but contain the common words
unrelated = review(
    "The annual report has no EBITDA bridge from reported to adjusted figures.",
    "Segment portfolio mix is not disclosed by geography.",
    "No illegal_documents_index was supplied.",   # substring of legal_documents? (no: 'illegal_documents')
)
print("unrelated gaps :", _issues(ctx, unrelated, ready))
# 3. substring for the legal rule
print("legal substring:", _issues(ctx, review("bridge", "portfolio", "nonlegal_documentsx"), ready))
