"""CP-2H context register: (a) an agency's issuer and facility rows refuse the whole register as
'Rating register not found'; (b) an issuer row and another agency's facility row are compared in
notches as if both rated the issuer."""
from deploy_workflow.context import Rating
from deploy_workflow.owners import cp2h
rows = (Rating(agency="S&P", scope="issuer", rating="BB", outlook="Stable", as_of="2025-11-01"),
        Rating(agency="S&P", scope="facility", rating="BB+", outlook="Stable", as_of="2025-11-01"),
        Rating(agency="Moody's", scope="issuer", rating="Ba2", outlook="Stable", as_of="2025-11-01"))
try:
    cp2h.context_register(rows)
except cp2h.SourceIssue as e:
    print("(a) refused:", e)
reg = cp2h.context_register((rows[0], Rating(agency="Moody's", scope="facility", rating="Ba1", outlook="Stable", as_of="2025-11-01")))
print("(b)", [(r.agency, r.scope, r.rating, r.position) for r in reg], "notches:", abs(reg[0].position - reg[1].position))
