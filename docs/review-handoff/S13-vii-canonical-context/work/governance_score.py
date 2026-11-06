"""Risk level is not monotone: a High-quality creditor-adverse action is High with 3 scored
dimensions and Low/Medium once a fourth supportive dimension is added."""
from deploy_vii.business_context import GovernanceItem, governance_sponsor_score

def row(dim, direction, kind="governance_topic"):
    return GovernanceItem(kind=kind, topic="t", documented_fact="f", direction=direction,
        behaviour_type="dividend recap" if kind == "behaviour_flag" else None,
        amount_funding_source=None, legal_capacity_link=None, dimension=dim,
        risk_mechanic="m", credit_implication="c", evidence_quality="High",
        category="Documentary Fact", citations=(), limitation=None)

recap = row("Shareholder extraction risk", "Extraction-Oriented", "behaviour_flag")
recap_unlabelled = row(None, "Extraction-Oriented", "behaviour_flag")
support = [row(d, "Supportive") for d in ("Support behavior", "Disclosure transparency", "Reporting quality", "Leverage tolerance")]
extra = row("Shareholder extraction risk", "Supportive")

for label, rows in [
    ("3 supportive dims + recap (labelled)", support[:3] + [recap]),          # 4 scored -> composite 5 High
    ("3 supportive dims + recap (no dimension)", support[:3] + [recap_unlabelled]),
    ("4 supportive dims + recap (no dimension)", support + [recap_unlabelled]),
    ("3 supportive + recap + supportive extraction row", support[:3] + [recap, extra]),
]:
    s = governance_sponsor_score(rows)
    print(f"{label}: composite={s.composite} level={s.risk_level} high_action={s.high_risk_action}")
