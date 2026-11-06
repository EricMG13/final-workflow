# CP-2 — Fundamental credit synthesis: LendingTree, Inc. (tree)

## Request

LendingTree, Inc. (issuer id `tree`), as of 2026-11-05 on the `credit_snapshot` pathway, with an information cutoff of 2026-11-05. This module synthesises the fundamental credit view from the accepted financial base and the business and transaction context, in USD. It gives no peer ranking, instrument recommendation or recovery conclusion.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_tree-20251231.htm.jsonl | 8cb6cb5e097dc2e8360d276758588e587f0ac910e30b439c9a6d5f22fdc532f1 | Audited FY2025 base; consulted only to confirm upstream locators |
| 10-Q_2025-09-30_tree-20250930.htm.jsonl | 249304d8f29fc14b902a9aacbb2c6a074e549655cafbbfa182447cab0a8e6bd0 | Pinned filing; reached through the upstream handoffs |
| 10-Q_2026-03-31_tree-20260331.htm.jsonl | 9f7be701e3beaeb193c8f4c45fa295df34640347810fab7e7e1868937c8317f9 | Pinned filing; reached through the upstream handoffs |
| 10-Q_2026-06-30_tree-20260630.htm.jsonl | 4c93c158274dd2856277ea5350526f695a8bcd4a41e0bedcd9b748ac31b890ae | Pinned filing; current-period authority; consulted for the interest-rate sensitivity and hedging search |
| EX-99.1_2026-03-02_tree-123125xer.htm.jsonl | 930047033d516e80ede0b1af19850b29c93444522e483a1dc8c6992d4283ee5d | Pinned release; reached through the upstream handoffs |
| EX-99.1_2026-04-30_tree-33126xer.htm.jsonl | 9b95e0c334507932b6d82bc72cf01d0a8f620ab6313637adea07e7f7ef2b4190 | Pinned release; reached through the upstream handoffs |
| EX-99.1_2026-07-29_tree-63026xer.htm.jsonl | b737e26fe71071d22f2d669bce2532cab38eb1e5741e87f2852ff6a85cf82520 | Pinned release; reached through the upstream handoffs |
| context | d200051bbc093266762c46db0da57fcc23aae21f45bdfa41362781dff2cb6e7d | User run settings; not issuer evidence |

| Handoff module | sha256 | Use |
| --- | --- | --- |
| CP-0 | c84ab10531b22ca79243cab80e778b189c7ae85ab40d1bc94cfa4d4426e74643 | Source readiness and gap list; limitations carried into the gaps below |
| CP-1 | 66d19075d0cda548fb908b11cbace236ac80961fccbfe892b5468b6b2cd9a36f | Financial base: statements, leverage, cover, liquidity and maturities; the basis for every financial figure here |
| CP-1A | 27aa6bb2d2a88e25a00702feb3dd400595805f473712abaaf922df6d060d8625 | Business, ownership, governance, transaction, timeline, conflicts and outlook history; the basis for every business claim here |

The evidence is upstream only: figures are those of CP-1 and CP-1A, whose locators (`page:N` in the pinned files) they carry. Short forms: 10-K (FY2025), 10-Q Q2 2026, release Q2 2026. New arithmetic is in `## Calculations`. The pinned files were searched only for hedging, derivative and interest-rate-exposure terms (10-K page:105, 10-Q Q2 2026 page:40).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| LendingTree's credit profile has strengthened: total debt to Adjusted EBITDA fell from 4.56x to 2.58x and liquidity is USD 185.8 million, but earnings are concentrated in Insurance and one partner, and the quality of EBITDA is unverified. | Medium | The credit agreement is not supplied, so covenant headroom, guarantors and letter of credit usage are unverified, and nothing after July 30, 2026 is included. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt to Adjusted EBITDA fell from 4.56x at December 31, 2024 to 2.58x for the twelve months to June 30, 2026. | Leverage tolerance has improved, but the ratio uses issuer-defined EBITDA; treating non-cash compensation as a cost gives 3.05x. | Medium |
| Cash was USD 110.8 million and the USD 75.0 million revolver was undrawn at June 30, 2026, against USD 4.0 million due within twelve months. | Near-term liquidity risk is low; the next large maturity is August 21, 2030. | High |
| Cash interest paid was USD 34.7 million over twelve months, covered 4.42x; free cash flow was USD 73.9 million. | Debt service is well covered at current earnings; interest floats, and each 100 basis points costs about USD 4.0 million a year. | High |
| Insurance was 66.8% of Q2 2026 revenue, one partner supplied 27% of FY2025 revenue, and Q2 2026 results fell below April guidance. | Earnings depend on carrier advertising budgets and media costs, so a downturn in either would reduce EBITDA before costs adjust. | Medium |
| Goodwill and intangibles are 45.7% of total assets and tangible equity is negative USD 96.3 million. | Protection for creditors rests on enterprise value and therefore on earnings durability, since hard assets are limited. | High |

### Credit view

LendingTree is a moderate credit that is improving, with leverage now low for a high yield issuer but earnings that are volatile and concentrated. The strongest support is the balance sheet: USD 110.8 million of cash, an undrawn USD 75.0 million revolver, one facility maturing August 21, 2030 and USD 73.9 million of free cash flow over the last twelve months. The weakest point is earnings quality and concentration: Adjusted EBITDA adds back non-cash compensation, Insurance is 66.8% of Q2 2026 revenue, one partner supplied 27% of FY2025 revenue, and management lowered its 2026 outlook. What decides the outcome is whether carrier advertising budgets and media costs hold; the credit agreement, which is not supplied, would show how much protection the covenants give.

### Key findings

First, LendingTree has deleveraged materially. Total debt principal fell from USD 474.7 million at December 31, 2024 to USD 397.0 million at June 30, 2026, and Adjusted EBITDA rose to USD 153.6 million for the twelve months to June 30, 2026, so total debt to Adjusted EBITDA fell from 4.56x to 2.58x and net debt to Adjusted EBITDA from 3.54x to 1.86x [CP-1]. Management's statement of net leverage of 2.4x at year-end 2025 agrees with the 2.39x computed here [CP-1, CP-1A].

Second, the improvement depends on the EBITDA definition. Adjusted EBITDA excludes non-cash compensation, which was about 22.0% of FY2025 Adjusted EBITDA, and litigation settlements; on EBITDA built from net income, interest, tax, depreciation and amortization the same debt is 3.10x for the twelve months to June 30, 2026 and 4.46x for FY2025 [CP-1]. The credit agreement's own EBITDA definition is not supplied, so covenant leverage cannot be computed.

Third, liquidity is strong and the maturity profile is clear. Cash was USD 110.8 million, the USD 75.0 million revolver had no borrowings, and only USD 4.0 million of the term loan falls due within twelve months; the final maturity of both facilities is August 21, 2030 [CP-1, CP-1A]. The financial covenant is a first lien net leverage ratio of 5.00 to 1.00 that is tested only when revolver usage exceeds USD 20.0 million, so with the revolver undrawn the term loan lenders have no routine maintenance test; this is the issuer's own summary, not a reading of the agreement [CP-1, CP-1A].

Fourth, earnings are sensitive to a single segment and a single partner. Insurance was 63.7% of FY2025 revenue and 66.8% of Q2 2026 revenue; Progressive Casualty Insurance supplied 27% of FY2025 revenue, about 42.4% of Insurance revenue on the rounded percentage [CP-1A]. Variable marketing spend was 70.8% of H1 2026 revenue, and variable marketing margin fell to 29.2% of revenue in H1 2026 from 33.8% in FY2024 [CP-1].

Fifth, momentum has softened. Q2 2026 Adjusted EBITDA of USD 35.2 million was 16.3% below Q1 2026 and below the USD 38 to 40 million guided in April, variable marketing margin was USD 87.3 million against a USD 93 to 97 million guide, and management cut its full-year 2026 Adjusted EBITDA outlook to USD 145 to 152 million from USD 152 to 162 million [CP-1, CP-1A]. These outlooks are management claims.

Sixth, cash generation is good and interest is largely floating. Free cash flow was USD 73.9 million over the twelve months to June 30, 2026, about 48.1% of Adjusted EBITDA, after cash interest of USD 34.7 million [CP-1]. The term loan bears interest at Term SOFR plus 4.50% or 4.25%; the sources disclose no hedge, so a 100 basis point rise would cost about USD 4.0 million a year, 5.4% of LTM free cash flow (calculation P2).

Seventh, ownership and capacity for creditor-adverse action are not testable. There is no sponsor, no dividend in over ten years and no repurchase in 2024, 2025 or the first half of 2026, which is supportive behaviour; the founder died in October 2025, his heirs collectively hold a substantial stake, and incremental debt capacity under the facility is the greater of USD 58.0 million and 50% of consolidated EBITDA plus an unlimited amount if first lien net leverage does not exceed 3.10 to 1.00 [CP-1A]. On issuer-defined Adjusted EBITDA the ratio-based part alone could allow roughly USD 190.0 million of additional first lien net debt, illustrative only because the agreement's EBITDA definition is not supplied (calculation P5).

### Strengths and weaknesses

**Strength, deleveraging and cash conversion (Documentary Fact).** LendingTree cut total debt principal by USD 77.7 million (16.4%) between December 31, 2024 and June 30, 2026 while growing Adjusted EBITDA, and capital spending was 0.96% of LTM revenue, which leaves most operating cash flow available for debt service [CP-1]. The mechanism is a low-capital marketplace model whose costs are mostly variable advertising, so cash conversion is high when demand is stable.

**Strength, liquidity and maturity profile (Documentary Fact).** Cash of USD 110.8 million plus an undrawn USD 75.0 million revolver is USD 185.8 million, about 46.4 times the USD 4.0 million due within twelve months, and no maturity other than scheduled amortization falls before August 21, 2030 [CP-1]. This removes near-term refinancing risk and gives time for the earnings base to prove durable.

**Strength, creditor-friendly behaviour so far (Analyst Interpretation).** The company has paid no cash dividend in over ten years, repurchased no shares in 2024, 2025 or the first half of 2026 despite a USD 96.7 million authorization, repaid its convertible notes in cash at maturity, and has no identified sponsor [CP-1A]. Behaviour is documented, but legal capacity depends on the credit agreement, which is not supplied.

**Strength, diversified segments and flexible cost base (Management Language, qualified).** Management says it adjusts selling and marketing spend dynamically with partner demand; the three segments respond to different cycles, although Insurance was 49.5% of FY2025 segment profit and 56.3% in Q2 2026 [CP-1A] (10-Q Q2 2026 page:30 for management's statement). This is management's characterisation; the Q2 2026 results show the flex is partial, as variable marketing margin fell while revenue grew.

**Weakness, earnings quality and definitions (Documentary Fact).** Adjusted EBITDA is issuer-defined and drives every leverage and cover ratio; add-backs include non-cash compensation of USD 29.2 million in FY2025 [CP-1]. Treating LTM non-cash compensation as a cost raises total debt to EBITDA from 2.58x to 3.05x, so the deleveraging is real but flattered, and covenant EBITDA may differ from either measure.

**Weakness, concentration (Documentary Fact).** Insurance was 66.8% of Q2 2026 revenue and one carrier supplied 27% of FY2025 revenue, with two carriers at 22% and 11% in FY2024 [CP-1A]. Carriers set advertising budgets by their own underwriting results and can cut them quickly, so a budget cut reduces revenue at once while the speed of the cost response is not documented in the sources.

**Weakness, margin pressure and a weaker Q2 (Documentary Fact).** Variable marketing margin was 27.9% of revenue in Q2 2026 against 33.4% in Q2 2025, Q2 2026 Adjusted EBITDA was below guidance, and management expects advertising costs to stay elevated [CP-1, CP-1A]. If media costs keep rising faster than partner fees, cash flow weakens while the debt stays fixed at USD 397.0 million.

**Weakness, floating-rate debt and thin hard-asset cover (Documentary Fact).** The term loan is floating, no hedge is disclosed, and goodwill and intangibles are 45.7% of total assets with negative tangible equity of USD 96.3 million (calculation P6). Creditor protection therefore depends on enterprise value rather than hard assets, which is a mechanic and not a recovery conclusion.

**Weakness, governance transition and untested protections (Insufficient Information).** The founder died in October 2025, the CEO changed on October 13, 2025, and the heirs hold a substantial, unquantified stake; a single holder above 20% is not named [CP-1A]. The credit agreement, proxy statement and any change of control terms are not supplied, so restricted payment capacity, guarantor coverage and the effect of an ownership change on tax attributes are unknown.

### Credit assessment

| Dimension | View | Category | Confidence | Basis |
| --- | --- | --- | --- | --- |
| Business risk | Moderate: transactional marketplace revenue, three segments, concentration in Insurance and in one carrier | Analyst Interpretation | Medium | CP-1A operating model, customer concentration and credit translations |
| Financial risk | Improving: total debt to Adjusted EBITDA 2.58x, net 1.86x, cover 4.42x; 3.05x if non-cash compensation is a cost | Documentary Fact for the ratios; Analyst Interpretation for the view | Medium | CP-1 leverage, cover and definition review |
| Liquidity | Strong: USD 185.8 million before letters of credit; USD 4.0 million due within twelve months | Documentary Fact | High | CP-1 liquidity and maturity tables |
| Governance and creditor control | Supportive behaviour to date; protections untested | Analyst Interpretation | Low | CP-1A governance table; credit agreement not supplied |
| Overall fundamental credit view | Moderate credit, improving, with earnings that are volatile and concentrated | Analyst Interpretation | Medium | All of the above; confidence is below High because the credit agreement and later events are not supplied |

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Insurance advertising cycle and carrier concentration | Carriers set budgets from underwriting results; one carrier supplied 27% of FY2025 revenue; revenue is per delivered request with no contracted minimum in the sources | A budget cut reduces revenue before media spend is cut, lowering EBITDA and raising leverage against fixed debt | Material |
| Earnings quality and definition | Adjusted EBITDA adds back non-cash compensation and litigation; covenant definition unknown | Reported leverage of 2.58x may understate leverage on a stricter basis (3.05x or 3.10x) | Material |
| Margin compression from media costs | Variable marketing is 70.8% of H1 2026 revenue; advertising costs expected to stay elevated; margin down to 29.2% of revenue from 33.8% | Cash flow available for debt service falls faster than revenue in a weak quarter | Material |
| Covenant and debt capacity | Single springing covenant on the revolver; incremental first lien capacity; restricted payment terms unknown | Creditors could face additional first lien debt or distributions the sources neither confirm nor exclude | Material |
| Floating-rate exposure | Term Loan at Term SOFR plus a margin; no hedge disclosed | Each 100 basis points costs about USD 4.0 million a year | Minor |
| Founder succession and ownership concentration | CEO changed October 13, 2025; heirs hold a substantial stake; unnamed 20% holder | Possible board, strategy or ownership change; ownership changes can limit tax attributes | Minor |
| Regulatory and litigation | Heavily regulated lead generation; a USD 19.0 million TCPA class settlement was paid in instalments through Q2 2026 | Settlement and compliance costs can reduce cash flow; accruals were USD 0.9 million at June 30, 2026 | Minor |
| Refinancing | Final maturity August 21, 2030 for both facilities; USD 393.0 million of the term loan due after twelve months | Refinancing exposure is distant but depends on the earnings base then | Minor |

## Calculations

All inputs are printed amounts or accepted figures from the upstream handoffs, in US dollars in thousands unless a unit is given. Other derived figures are those of CP-1 (leverage, cover, free cash flow, liquidity, margins) and CP-1A (mix, guidance, concentration).

**P1. EBITDA sensitivity of total debt to EBITDA.** LTM Adjusted EBITDA 153,639 and total debt principal 397,000 at June 30, 2026 (CP-1). If EBITDA falls 10%: 397,000 / (153,639 × 0.9) = 2.871x. 20%: 397,000 / (153,639 × 0.8) = 3.230x. 30%: 397,000 / (153,639 × 0.7) = 3.691x. 40%: 397,000 / (153,639 × 0.6) = 4.307x. The fall in EBITDA that would raise total debt to EBITDA to 5.00x is 1 − 397,000 / (5 × 153,639) = 48.3%. This is a ratio on issuer-defined Adjusted EBITDA, not the covenant, whose definition and net basis are not supplied.

**P2. Interest-rate sensitivity.** 1% × 397,000 = 3,970 a year (the 10-Q states USD 4.0 million, 10-Q Q2 2026 page:40). As a share of LTM free cash flow of 73,877: 3,970 / 73,877 = 5.4%. Interest cover if EBITDA halves: 153,639 × 0.5 = 76,820; 76,820 / 34,740 = 2.21x on LTM cash interest paid.

**P3. Free cash flow after scheduled amortization.** 73,877 − 4,000 = 69,877. Cash build in H1 2026: 110,766 − 81,073 = 29,693.

**P4. Debt reduction.** 474,682 − 397,000 = 77,682; 77,682 / 474,682 = 16.4%. Liquidity coverage of near-term debt: 185,766 / 4,000 = 46.4 times.

**P5. Illustrative first lien incremental capacity.** 3.10 × 153,639 = 476,281; less net debt of 286,234 = 190,047, about USD 190.0 million. The term in the agreement is a first lien net leverage test on consolidated EBITDA as defined in the credit agreement, which is not supplied; the figure uses issuer-defined Adjusted EBITDA and total net debt, includes no netting rules and is not a capacity estimate.

**P6. Asset composition.** Goodwill 381,539 + intangible assets, net 35,516 = 417,055; 417,055 / total assets 911,631 = 45.7%. Tangible equity: 320,772 − 417,055 = −96,283. Deferred income tax assets of 114,737 are a further 12.6% of total assets (114,737 / 911,631).

**P7. Capital intensity.** LTM capital expenditures 12,200 / LTM revenue 1,268,169 = 0.96%.

**P8. Guidance arithmetic.** From CP-1A: full-year Adjusted EBITDA guide 145 to 152 (USD millions) less H1 2026 of 77.171 implies second-half 67.829 to 74.829; Q2 2026 Adjusted EBITDA of 35.162 was 2.838 below the low end of the 38 to 40 guide.

## Gaps

| Gap | Why it matters and what it affects | Severity | Action |
| --- | --- | --- | --- |
| 2025 Credit Agreement not supplied: covenant EBITDA definition, borrower and guarantor entities, restricted payments, incremental debt, change of control, letters of credit | Limits any statement on covenant headroom, creditor control and capacity for adverse action; lowers confidence below High | Material | Supply the agreement and compliance disclosure |
| Nothing after July 30, 2026, including Q3 2026 results and any current reports | The credit view is stale relative to the November 5, 2026 cutoff; guidance was already lowered once | Material | Supply later filings |
| 2026 proxy statement, holder list, unnamed 20% holder and heirs' arrangements not supplied | Ownership control and succession cannot be assessed | Minor | Supply the definitive proxy statement |
| Partner contracts and 2026 largest-partner share not supplied | Cannot size the 2026 Insurance concentration or termination rights | Material | Supply later disclosure |
| Hedging: none disclosed in the sources searched | The floating-rate exposure is taken as unhedged, but a hedge elsewhere cannot be excluded | Minor | Confirm in the credit agreement or later filings |
| Annual maturity split of the USD 393.0 million long-term portion not printed | Only the current portion and the final maturity are known | Minor | Use as printed |
| Upstream conflicts logged, not reconciled: release versus 10-K balance sheet classification; valuation allowance wording | Affects current assets at December 31, 2025 and the description of the tax benefit; the 10-K controls | Minor | Use the 10-K; keep the conflict open |
| Text extraction only; no XBRL or image review | Small risk of table misreads | Minor | Check against the filed HTML |
| Upstream status: CP-0 verdicts were READY_WITH_LIMITATIONS for all consumers; CP-1 and CP-1A carry the gaps above | The synthesis is restricted accordingly | Minor | Carry the limitations |

## Next module

- CP-5: trace each claim in the key findings and the strengths and weaknesses to the upstream locators; keep the two logged conflicts open; treat the outlook as management claims; do not read the illustrative incremental capacity as an estimate.
- Report assembly: present the credit view as moderate and improving, with confidence Medium, and state the missing credit agreement and the post-July 30, 2026 gap where they change a conclusion.
