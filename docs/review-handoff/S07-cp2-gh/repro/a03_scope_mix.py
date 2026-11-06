"""CP-2H: T2R.8 compares the two agencies' ratings in notches although they rate different
instruments (issuer rating vs secured notes); the instrument is never part of the comparison."""
import sys, hashlib
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_method_cp2h as T
from deploy_workflow.owners import cp2h
from deploy_vii.contracts import Source, Span
pk = T.pack("positive")
r = next(s for s in pk.sources if s.source_id == "ratings")
pages = [sp.text for sp in r.spans]
pages[0] = pages[0].replace("Brook Credit  Issuer rating  Ba3", "Brook Credit  Senior secured notes  Ba1")
sha = hashlib.sha256("\f".join(pages).encode()).hexdigest()
r2 = Source(source_id="ratings", name=r.name, status="ready", sha256=sha, media_type="text/plain",
            spans=tuple(Span(locator=s.locator, text=t) for s, t in zip(r.spans, pages)),
            extraction_status="complete")
pk2 = cp2h.PackScope(sources=tuple(r2 if s.source_id == "ratings" else s for s in pk.sources), names=pk.names)
src = cp2h.parse_ratings(cp2h.source_pages(r2))
print([(x.agency, x.instrument, x.rating, x.position) for x in src.register])
book, mech = cp2h._compose(r2, src, T.upstream("positive"), None)
for c in book.cells:
    if c.fact.table_id == "T2R.8":
        print(c.fact.field, c.fact.status, c.fact.text if c.fact.text else c.fact.amount, c.fact.limitation)
