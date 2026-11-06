"""Repro: CP-0 attachment gate accepts gaps that do not name the declared attachment."""
from types import SimpleNamespace as NS
from deploy_workflow.owners.cp0_attachments import _issues

ctx = NS(attachments=NS(portfolio_workbook=False, prior_case=False, management_bridge=False,
                        legal_documents="executed"))
review = lambda *texts: NS(sources=(), gaps=tuple(NS(kind="source", description=t) for t in texts))
ready = frozenset()
print("no gap                     ->", _issues(ctx, review(), ready))
print("'illegal_documents_index'  ->", _issues(ctx, review("No illegal_documents_index supplied"), ready))
print("'legal_documents_ok'       ->", _issues(ctx, review("legal_documents_ok: all present"), ready))
ctx2 = NS(attachments=NS(portfolio_workbook=False, prior_case=False, management_bridge=False,
                         legal_documents="executed"))
# same token-boundary rule the attachments use would refuse the first two:
import re
from deploy_workflow.owners.cp0_attachments import GAP_MATCH
pat = re.compile(GAP_MATCH.format(id="legal_documents"))
print("token rule on 'illegal_documents_index':", bool(pat.search("No illegal_documents_index supplied")))
