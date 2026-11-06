"""C09: the helpers inputs() calls run _page_units (the per-page extractor) five times per source."""
from types import SimpleNamespace
from deploy_vii.contracts import Span
import deploy_workflow.financial_workflow as fw

calls = 0
orig = fw._page_units
def counting(spans):
    global calls
    calls += 1
    return orig(spans)
fw._page_units = counting
spans = (Span(locator="page:1", text="CONSOLIDATED BALANCE SHEETS\n2025  2024\nCash  10  9\nTotal assets  10  9"),)
src = SimpleNamespace(source_id="f", status="ready", media_type="application/pdf", spans=spans)
pack = SimpleNamespace(sources=(src,))
ids = ("f",)
fw._other_statement_rows(pack, ids, ())
fw._located_pdf_units(pack, ids)
fw._located_kinds(pack, ids)
fw._located_units(pack, ids)
print("_page_units calls for one source in the inputs() sequence:", calls)
