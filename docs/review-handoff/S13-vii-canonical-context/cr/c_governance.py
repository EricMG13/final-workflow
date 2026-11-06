from deploy_vii.business_context import GovernanceItem, governance_sponsor_score, DIMENSIONS

def row(direction, dim, quality="High", kind="behaviour_flag"):
    return GovernanceItem(kind=kind, topic="t", documented_fact="f", direction=direction,
        behaviour_type="dividend recap" if kind=="behaviour_flag" else None,
        amount_funding_source=None, legal_capacity_link=None, dimension=dim,
        risk_mechanic="m", credit_implication="c", evidence_quality=quality,
        category="Documentary Fact", citations=(), limitation=None)

adverse = row("Extraction-Oriented", None)
for n in (3, 4):
    rows = [adverse] + [row("Supportive", d, "Medium", "governance_topic") for d in DIMENSIONS[:n]]
    s = governance_sponsor_score(rows)
    print(n, "supportive dims ->", s.composite, s.risk_level, "high_action=", s.high_risk_action)
