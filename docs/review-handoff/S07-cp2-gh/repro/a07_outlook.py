"""CP-2H context register: outlooks are compared as raw strings, so 'Stable' and 'stable ' are
reported as Different outlooks."""
from deploy_workflow.context import Rating
from deploy_workflow.owners import cp2h
reg = cp2h.context_register((
    Rating(agency="S&P", scope="issuer", rating="BB", outlook="Stable", as_of="2025-11-01"),
    Rating(agency="Moody's", scope="issuer", rating="Ba2", outlook="stable ", as_of="2025-11-01")))
src = cp2h.RatingsSource(register=reg, triggers=(), register_published="not stated", terms_published="not stated")
b = cp2h._Book("0" * 64)
rows = {"S&P": "r01", "Moody's": "r02"}
for r, f in zip(rows.values(), ("agency", "outlook")):
    pass
for n, r in enumerate(reg, 1):
    for name in ("agency", "outlook"):
        b.text(("T2R.2", f"r{n:02d}", name), name, getattr(r, name))
    b.number(("T2R.2", f"r{n:02d}", "position"), "p", __import__("decimal").Decimal(r.position), "scale position", "x", period="p", source=True)
cp2h._divergence(b, src, rows)
print({c.fact.field: (c.fact.text or c.fact.amount) for c in b.cells if c.fact.table_id == "T2R.8"})
