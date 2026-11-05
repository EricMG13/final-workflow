# CP-2 — Fundamental credit synthesis: Caesars Entertainment, Inc. (czr)

## Request

- Issuer: Caesars Entertainment, Inc. (issuer id `czr`), as of 2026-10-02, information cutoff 2026-10-02.
- Run: `czr-2026-10-02-credit_snapshot-host`, pathway `credit_snapshot`. Fills "Key findings" and "Strengths and weaknesses".
- Execution: host session. This synthesis uses the supplied handoffs only; it quotes no source text. No provider was called.
- Reader question: what is the fundamental credit view, and which strengths, weaknesses, findings and risks drive it? No peer ranking, instrument recommendation or recovery conclusion.

## Sources

Issuer sources pinned for this run (read by upstream modules, not quoted here):

| Source | sha256 |
| --- | --- |
| CZR_FY2025_10K.txt | 172309048af2a6a2dab515d765f00a7c89bf8c874c6104a5e3a052b66cad4512 |
| CZR_Q2_2026_10Q.txt | f369ce5f1ebeddd9a0d4ce02ce3958112267d8701d1a348dfd6dc82d2034793a |
| CZR_Q2_2026_Earnings_Release.txt | b385f76ff631243d1053fa8073ebde4f8886b4a50c9ce34ce3498d6b2ac3e9f8 |

Supplied handoffs consumed:

| Module | sha256 | Used for |
| --- | --- | --- |
| CP-0 | c25e5a54d628dec4614d6d52f99b207b6b261bfcb442c3bed0d41c0af7f514a3 | Readiness and restrictions: READY_WITH_LIMITATIONS for CP-2; no merger financing, executed agreements or post-July 28, 2026 events |
| CP-1 | 61c83d3e3ee8df68a362930def996cf678e2e35924dc16aa46093cfd4d02ba30 | All figures: LTM and FY2025 metrics, leverage on three bases (C3 to C5), coverage (C6), free cash flow (C2), debt register, liquidity, covenant terms |
| CP-1A | 89de62ee6354c11acba13cac4ef871638c52f2ac6bcb8731ef91f99f58e5c17f | Business rows, merger terms, governance behaviour, timeline, credit translations |

Upstream status: all three accepted. Inherited limitations: CP-1A rates merger financing and debt treatment Insufficient Information; CP-1 rates covenant headroom Not calculable.

## Findings

### Credit assessment

Caesars is a large, diversified gaming operator whose credit profile is set by heavy fixed obligations: about 11.8 billion of debt and about 13.2 billion of lease financing obligations to VICI and GLPI (CP-1 debt and lease rows). Debt-only leverage of 3.29x (CP-1 C3) understates the burden; with the leases, leverage is 6.95x on carrying amounts (CP-1 C4) or 5.30x on debt over Adjusted EBITDA after cash rent (CP-1 C5), and Adjusted EBITDA covers total net interest only 1.57x (CP-1 C6). Near-term liquidity is adequate: about 2.9 billion of cash and revolver capacity, no large maturity before 2028, and free cash flow of about 0.6 billion over the last twelve months (CP-1 liquidity table, C2). The dominant open question is the pending take-private by Fertitta Gaming: the supplied documents do not show its financing or how existing debt and leases are treated, so the post-closing credit profile cannot be assessed (CP-1A transaction summary).

- Category: Analyst Interpretation, based on CP-1 figures and CP-1A Documentary Fact rows.
- Confidence: Medium. Reported figures are complete and reconcile; the merger financing is missing, which limits any view beyond the current capital structure.

Thesis: Caesars can service its current debt and leases from operations with adequate liquidity, but its lease-adjusted leverage is high, earnings are flat, and a pending change of control with unknown financing is the main credit risk.

### Key findings

1. The lease obligations are larger than the debt. Long-term financing obligations of 13,157 exceed total debt of 11,807 at June 30, 2026 (CP-1). Mechanism: the leases are fixed, rise with inflation, and their cost sits in interest expense, outside Adjusted EBITDA. Implication: lease-adjusted leverage of 5.30x to 6.95x (CP-1 C4, C5), not the debt-only 3.29x, sets leverage tolerance. Analyst Interpretation.
2. A change of control is pending with unknown financing. The Merger Agreement was signed on May 27, 2026 at 31 US dollars per share in cash, subject to stockholder, antitrust and gaming approvals, with an end date that can extend to November 27, 2027 (CP-1A transaction summary). Mechanism: a private owner may add acquisition debt and change the capital structure; the issuer itself lists "increased leverage from the proposed transaction" as a risk (CP-1A Documentary Fact row). Implication: the current credit view may not hold after closing; monitoring posture is event-driven. Documentary Fact for the terms; Insufficient Information for the financing.
3. Coverage is thin on the full basis. Adjusted EBITDA covers total net interest, including lease interest, 1.57x over the last twelve months; after cash rent it covers cash interest on debt 2.87x (CP-1 C6). Mechanism: a fall in Adjusted EBITDA passes almost entirely to coverage because rent and interest are fixed. Implication: limited room for an earnings decline before debt service is strained. Analyst Interpretation.
4. Earnings are flat to slightly down. LTM Adjusted EBITDA of 3,592 is below the FY2025 figure of 3,624, and the margin fell from 31.6% to 30.8% (CP-1 C1, C7); Q2 2026 Adjusted EBITDA was below Q2 2025. Las Vegas declined while Regional grew (CP-1A segment rows). Mechanism: Las Vegas is the largest Adjusted EBITDA segment, so its decline weighs on group cash flow. Implication: deleveraging from earnings growth is not in evidence. Documentary Fact via CP-1 and CP-1A.
5. Liquidity and maturities are not a near-term constraint. Liquidity of 2,928 at June 30, 2026 compares with estimated remaining 2026 debt service of about 425 and lease payments of about 687 (CP-1 liquidity). The first large maturities are the revolver and Term Loan A in 2028 (CP-1 maturity row). Implication: low near-term default risk from liquidity, assuming the capital structure is unchanged. Documentary Fact via CP-1.
6. Debt has been reduced modestly. Total debt face value fell from 11,905 to 11,807, after the 2027 notes were redeemed in July 2025 and share repurchases stopped in 2026 (CP-1, CP-1A governance rows). Implication: the trend is supportive but small relative to the lease-adjusted burden. Documentary Fact.

### Strengths and weaknesses

Strengths:

- Scale and diversification: 52 properties in 18 states and a digital business in 34 jurisdictions spread revenue across markets (CP-1A business rows). This supports revenue visibility. Documentary Fact.
- Cash generation: LTM operating cash flow of 1,297 and free cash flow of 610 after capex (CP-1 C1, C2). Free cash flow is positive and rising as capex falls. Documentary Fact via CP-1.
- Liquidity runway: 2,928 of liquidity and no large maturity before 2028 (CP-1). Documentary Fact via CP-1.
- Reported covenant compliance: the issuer states compliance with all applicable financial covenants at June 30, 2026 (CP-1 covenant table). Management Language; headroom is not verifiable.

Weaknesses:

- Lease-heavy capital structure: financing obligations exceed debt, and rent is inflation-linked (CP-1 lease rows). Lease-adjusted leverage is high. Analyst Interpretation.
- Thin interest coverage: 1.57x on total net interest (CP-1 C6). Analyst Interpretation.
- Flat earnings and a falling Las Vegas segment (CP-1 C1; CP-1A segment rows). Documentary Fact.
- Persistent GAAP net losses since FY2024, because interest including lease interest exceeds operating income (CP-1 income statement). Documentary Fact.
- Ownership uncertainty: a pending take-private with unknown financing (CP-1A transaction summary). Insufficient Information on financing; the missing datapoint is the post-closing debt and lease structure.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Leveraged take-private | New owner funds the purchase with debt or changes the structure; existing creditors' ranking and covenants may change | Higher leverage and default risk after closing; possible change-of-control effects, terms Not supplied | Critical |
| Lease burden | Fixed, CPI-linked rent to VICI and GLPI absorbs a large part of Adjusted EBITDA | Lower leverage tolerance; less cash for debt service in a downturn | Material |
| Earnings decline in Las Vegas | Largest Adjusted EBITDA segment is falling | Coverage weakens because fixed charges do not fall | Material |
| Consumer spending cycle | Gaming and hospitality demand is discretionary | Earnings and coverage fall together in a recession | Material |
| Covenant definitions unknown | Net leverage and fixed-charge covenants of 6.50:1 and 2.0:1 apply to the revolver and Term Loan A; definitions not supplied | Headroom cannot be monitored | Minor |

### Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Merger financing and treatment of existing debt and leases | The post-closing credit profile is unknown | Assessment confidence, key finding 2, top risk | Critical | Supply the Merger Agreement and financing documents; rerun CP-2 when filed |
| Events after July 28, 2026 | Approval and financing status at the as-of date unknown | Monitoring posture | Material | Supply later filings |
| Executed credit agreement, indentures and leases | Covenant headroom, change-of-control and restricted-payment terms unknown | Covenant risk, governance capacity | Material | Supply documents and add CP-4 |
| No rating or market data | No external view of the credit | Not required for this scope | Minor | Add CP-2H or CP-3D only if sourced |

## Calculations

No new calculation. Every figure refers to a CP-1 row or calculation ID (C1 to C12).

## Gaps

- Critical: merger financing and post-closing structure Not supplied.
- Material: events after July 28, 2026 Not supplied; executed agreements Not supplied.
- Minor: no rating or market data in scope.

## Next module

- CP-5: trace each finding to its CP-1 row or calculation and its CP-1A row, and check that categories match the basis.
- Report delivery: "Key findings" and "Strengths and weaknesses" above; carry the Medium confidence and the Critical merger gap.
