"""A06: CP-1C _basis takes the first page:1 Basis line holding the supported clause pair and
ignores an earlier contradictory Basis line (other currency, thousands)."""
import hashlib
from deploy_vii.contracts import Source, Span
from deploy_workflow.owners import cp1c

p1 = "\n".join([
    "Basis: EUR; amounts in thousands.",
    "Basis: twelve months to the period end shown; USD; amounts in millions.",
    cp1c.P1_HEADER,
    "Issuer  2025-12-31  120.0  30.0  50.0  5.0  21.0",
    "Peer A  2025-12-31  200.0  52.0  104.0  8.0  41.6",
])
src = Source(source_id="peers", name="peers", status="ready",
             sha256=hashlib.sha256(p1.encode()).hexdigest(), media_type="text/plain",
             spans=(Span(locator="page:1", text=p1),), extraction_status="complete")
try:
    sheet = cp1c.parse_peer_source(src, issuer_name="Issuer", currency="USD")
    print("ACCEPTED:", sheet.currency, sheet.unit, sheet.scale, [r.amounts["revenue"] for r in sheet.peers])
except cp1c.PeerTableError as e:
    print("REFUSED", e)
