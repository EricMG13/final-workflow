# CP-2 — Fundamental credit synthesis: PRA GROUP INC (praa)

## Request

PRA GROUP INC, as of 2026-11-05, pathway credit_snapshot: a fundamental credit synthesis built from the CP-1 financial base and the CP-1A business context. It uses the figures and cited pages of those handoffs, checked against the filings where this note says so, and gives no rating, relative value, instrument recommendation or recovery conclusion.

## Sources

Locators are `page:N` of the pinned text files (source chunks, not printed page numbers). sha256 values are those CP-OS pins.

### Issuer sources

| Source (exact name) | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_praa-20251231.htm.jsonl | acaea144d244584c3474f86549753d209ff125e0c5d293c88092a8b3609d005e | Opened directly: foreign exchange mitigation (page:65), note terms (page:92) |
| 10-Q_2026-06-30_praa-20260630.htm.jsonl | d7a354d31f5af038cbd610321c408a92f38ffbe0be4451883080ac13fa2cd5a8 | Opened directly: interest rate mix and sensitivity (page:46), next 12 months obligations (page:42), key metrics (page:25), borrowings (page:11) |
| 10-Q_2025-09-30_praa-20250930.htm.jsonl | 929f20928dbfde158b90287ecb3f34f89e93248de03667dc981595cbc1f16f43 | Used through the upstream handoffs only |
| 10-Q_2026-03-31_praa-20260331.htm.jsonl | 5b8ee1fe62f8b0079ea63a2a1c4f92f69a59ebc645588dbcce6f190c45211b32 | Used through the upstream handoffs only |
| EX-99.1_2026-02-26_q42025earningsrelease.htm.jsonl | ac28ac408106b5058aef5a7017ad24c9c2f1059768c1e80795f1a5ba0705218f | Used through the upstream handoffs only |
| EX-99.1_2026-05-07_q12026earningsrelease.htm.jsonl | 0cafa2dd16d8fe170df8f95a181353ea848b2d370eaa0bad903e81ca9ab40ac1 | Used through the upstream handoffs only |
| EX-99.1_2026-08-06_q22026earningsrelease.htm.jsonl | 90c4b9dc1bbbec8846231ce65b511117fe19795284263ee0dc2f0a68914940d4 | Used through the upstream handoffs only |

### Run settings (not issuer evidence)

| Source | sha256 | Role |
| --- | --- | --- |
| context (1185348-pra-group-inc-praa.json) | fb395d626a32c7d3e686eb338c55b901d79ab38a3782a023f0c732503b0056b3 | Dated user settings; blank fields are unknown, not zero. |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | ad930b06ca8dfafbd7d05aa59918ec9f5ec7345e1f274cfd0ac40c5b9907cbbd | Source readiness and limitations. |
| CP-1 | f504ebf424f2b6080338462ae74293629fc8293218527f27a4fbeb97c3179884 | Financial base: leverage, cover, liquidity, maturities, definitions. |
| CP-1A | 7ef973de3d6ffddb47e9f6283951b59270b39a7a5b808c9a73fc485a4265b73d | Business model, ownership, transactions, governance behaviour. Its readiness judgment of this module is "Ready with limitations". |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The fundamental credit view is adequate and stable: gross debt is 2.78x issuer Adjusted EBITDA and cash interest is covered 5.36x, but earnings, ERC and ERC-linked availability rest on internal forecasts, and purchases are debt funded. | Medium | Covenant ratios and executed debt documents are not supplied, and nothing after August 7, 2026 is covered, so headroom and the current position are unobserved. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Gross debt of USD 3,771.3 million is 2.78x last-twelve-months Adjusted EBITDA, and cash interest is covered 5.36x. | Leverage and cover are moderate on the issuer's own measure, which adds back collections applied to principal. | Medium |
| Liquidity is USD 132.4 million of cash plus USD 998.5 million of availability, of which USD 733.1 million depends on current ERC. | Liquidity covers the estimated next 12 months of interest, fees and principal 4.57x, but shrinks if ERC forecasts are cut. | Medium |
| No principal other than term loan payments falls due before February 2028, and 48.7% of principal falls due in 2029. | Near-term rollover risk is low; refinancing risk concentrates in 2029. | Medium |
| Portfolio purchases exceeded Adjusted EBITDA after cash interest and taxes by USD 190.7 million in FY2025 and USD 502.9 million in FY2024. | Leverage will drift up unless purchases slow or collections grow faster than the spend. | Medium |
| Secured credit facilities are 56.5% of debt principal and the senior notes are unsecured. | Noteholders rank behind secured lenders on the collateral; guarantor coverage of European assets is not evidenced. | Medium |

### Credit view

PRA Group's fundamental credit is adequate and stable, with moderate leverage that depends on forecast accuracy more than on a cash buffer. The strongest support is cash earning power: last-twelve-months Adjusted EBITDA of USD 1,358.9 million covers cash interest of USD 253.4 million 5.36x, gross debt is 2.78x that EBITDA, and no principal other than term loan payments is due before February 2028. The weakest point is that revenue, ERC and ERC-linked availability of USD 998.5 million all rest on internal collection forecasts, while purchases have exceeded post-interest cash earnings in each of the last two years. What decides the outcome is whether collections keep matching forecasts and whether purchasing is held to the cash the business generates. Covenant headroom cannot be observed.

### Key findings

First, the leverage and coverage position is moderate and has improved. Gross debt over Adjusted EBITDA was 2.93x in FY2024 and 2.78x for the last twelve months to June 30, 2026, because between FY2024 and the last twelve months to June 30, 2026 Adjusted EBITDA rose 19.5% while debt principal rose 13.0%. Cash interest cover was 5.08x in FY2025 and 5.36x for the last twelve months [CP-1 leverage and interest cover tables]. The measure is the issuer's own non-GAAP Adjusted EBITDA, which adds back collections applied to principal, so it is a cash-collections measure and is not the covenant definition; ratios should not be compared with the 3.50x and 2.50x limits.

Second, reported profit is more estimate-driven than cash. In Q2 2026 changes in expected recoveries were USD 96.9 million of USD 153.3 million income from operations, after a European forecast review raised European ERC by USD 348.5 million and added approximately USD 105 million to changes in expected future recoveries [CP-1; CP-1A revenue model row; Q2 10-Q page:9]. The USD 348.5 million is an ERC change and not income. Cash collections of USD 558.5 million in the quarter are the firmer measure.

Third, liquidity depends on the borrowing base. Cash is USD 132.4 million against availability of USD 998.5 million, of which USD 733.1 million, 73.4%, is based on current ERC at advance rates of 35% for Core and 55% for Insolvency pools [CP-1 liquidity tables; 10-K page:87]. A downward ERC revision would cut capacity at the moment it is most needed. Cash and availability total USD 1,130.9 million, 4.57x the USD 247.7 million of interest, unused fees and principal payments the company estimates for the next 12 months (Q2 10-Q page:42).

Fourth, purchasing, not operations, drives the debt trend. Adjusted EBITDA after cash interest, cash taxes and capital expenditure was short of cash spent on portfolio purchases by USD 190.7 million in FY2025 and USD 502.9 million in FY2024 [CP-1 bridge]. Borrowings rose in both years. Management says it can slow purchases without hurting current-year collections (10-K page:55), which is a management claim, but forward flow agreements carry few minimum obligations [CP-1A operating model], so the lever exists in the documents.

Fifth, refinancing risk is deferred and then concentrated. The European revolving facility now matures on April 30, 2031, the 2028 senior notes of USD 398.0 million fall due on February 1, 2028 (about 15 months after the as-of date), and USD 1,837.1 million, 48.7% of principal, matures in 2029 across both other revolvers, the 2029 notes and the term loan [CP-1 maturity table].

Sixth, structure and visibility are unresolved. Credit facilities of USD 2,130.6 million, 56.5% of principal, are secured by liens on U.S. and UK assets and on European subsidiary equity, and the USD 1,640.6 million of senior notes are unsecured [CP-1 debt table; 10-K page:87 to page:92]. About 60% of debt is fixed or hedged, and a 50 basis point move changes annual interest by an estimated USD 7.8 million (Q2 10-Q page:46). The notes' guarantor structure, the credit agreement definitions and the covenant ratios are not supplied.

### Strengths and weaknesses

Strengths. The company has a long-dated, diversified liability stack: secured revolving facilities in several currencies, a term loan and unsecured notes, with no principal beyond term loan payments due for about 15 months and revolvers running to 2029 and 2031. Cash earning power is growing: cash collections of USD 558.5 million in Q2 2026 are 4.2% above Q2 2025, ERC is USD 8,894.5 million, 2.36x debt principal, and Adjusted EBITDA has risen 9.6% year on year. Purchasing is discretionary, which gives management a lever over debt growth. The European business is organised so that portfolio ownership and collections sit in the same entity, and the European and UK facilities are multi-currency to match funding by currency (10-K page:65). The company is widely held, with no sponsor, no dividends in three years and a documented early extension of its European facility, and it discloses reconciliations of its non-GAAP measures and ERC revisions.

Weaknesses. Earnings, ERC and the ERC-based part of availability depend on internal models and forecasts, and a USD 412.6 million goodwill impairment in Q3 2025 shows that valuations can reset sharply. Cash on hand is small, USD 132.4 million against USD 3,771.3 million of debt, so liquidity is a function of revolver access and covenant compliance, which cannot be observed. Debt has grown faster than cash after purchases in two consecutive years, and shareholder returns continue through repurchases, with a USD 150 million program approved on August 3, 2026. Europe is 54.0% of ERC, adding currency and fragmented regulatory exposure, and the U.S. segment's adjusted operating income was flat year on year in Q2 2026 as legal collection spending rose. A multi-state Attorneys General investigation open since 2015 remains unresolved. The 2029 maturity cluster and the structural position of unsecured noteholders behind secured facilities add refinancing and ranking sensitivity.

### Credit assessment

| Dimension | Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- | --- |
| Overall fundamental view | Adequate and stable, with estimate risk and unobserved covenant headroom | Analyst Interpretation | Medium | CP-1 leverage, cover and liquidity tables; CP-1A company and operating model and governance tables |
| Business risk | Moderate: recurring portfolio purchasing with multi-year collection, but revenue is forecast-based and Europe-weighted | Analyst Interpretation | Medium | CP-1A revenue model, geography and supply rows |
| Financial risk | Moderate: gross debt 2.78x and cash interest cover 5.36x on the issuer's own EBITDA | Documentary Fact for the ratios; Analyst Interpretation for the label | Medium | CP-1 calculations C1 to C4 |
| Liquidity | Adequate for 12 months, dependent on ERC-linked availability | Analyst Interpretation | Medium | CP-1 liquidity table; Q2 10-Q page:42 |
| Refinancing | Low before 2028; concentrated in 2029 | Analyst Interpretation | Medium | CP-1 maturity table |
| Governance and capital allocation | Neutral or Mixed: repurchases alongside debt-funded purchasing; no extraction documented | Analyst Interpretation | Medium | CP-1A governance table |
| Covenant headroom | Not assessable: ratio levels and definitions not supplied | Insufficient Information | Not assessable | CP-1 covenant table; CP-1A monitoring gaps |

### Thesis

PRA Group is an adequately financed, moderately levered collector of nonperforming loans whose debt service is supported by growing cash collections but whose reported earnings, ERC and ERC-linked liquidity rest on internal forecasts and whose debt keeps rising to fund portfolio purchases.

### Basis register for strengths and weaknesses

| Item | Type | Category | Basis |
| --- | --- | --- | --- |
| Long-dated diversified funding with no principal before February 2028 other than term loan payments | Strength | Documentary Fact | CP-1 debt and maturity tables; Q2 10-Q page:42 |
| Growing cash collections, ERC and Adjusted EBITDA | Strength | Documentary Fact | CP-1 financial table and leverage calculations |
| Discretionary purchasing | Strength | Documentary Fact | CP-1A supply row; Q2 10-Q page:17 |
| Management states it can slow purchases without hurting current-year collections | Strength (claim) | Management Language | 10-K page:55 |
| Currency matching through multi-currency facilities | Strength | Documentary Fact | 10-K page:65 |
| Forecast-dependent earnings, ERC and availability | Weakness | Documentary Fact | CP-1A revenue model row; Q2 10-Q page:9 |
| Thin cash against debt | Weakness | Documentary Fact | CP-1 liquidity table |
| Purchases above post-interest cash earnings; debt growth | Weakness | Documentary Fact | CP-1 calculation C8 |
| Europe weighting of ERC | Weakness | Documentary Fact | CP-1A geography row |
| Unsecured notes behind secured facilities | Weakness | Analyst Interpretation | CP-1 debt table; 10-K page:87 to page:92 |
| Covenant headroom unobservable | Weakness | Insufficient Information | CP-1 covenant table |

### Key credit risks

| Risk | Mechanic | Credit implication | Severity | Basis |
| --- | --- | --- | --- | --- |
| Forecast reversal | A downward ERC or collection forecast revision lowers revenue and, through the 35% and 55% advance rates, borrowing base availability together | Earnings and liquidity weaken at once; leverage on cash-based EBITDA rises only if collections also fall | Material | CP-1 liquidity table; CP-1A revenue model row |
| Debt-funded purchasing | Purchases exceed post-interest cash earnings; deficit is funded by borrowing | Leverage drifts up if collections growth slows; monitor debt over EBITDA each quarter | Material | CP-1 calculation C8 |
| Covenant opacity | Total leverage, senior secured leverage, fixed charge and ERC ratio tests exist but levels and definitions are not supplied; the European ERC ratio cap fell to 40.0% | Headroom cannot be observed; a breach would restrict drawing and distributions | Material | CP-1 covenant table; CP-1A timeline |
| 2029 maturity cluster | Both other revolvers, the 2029 notes and the term loan mature within a short window in 2029 | Refinancing must succeed in one period; market access matters | Material | CP-1 maturity table |
| Europe and currency | 54.0% of ERC is in Europe; euro and sterling assets and liabilities move with exchange rates; regulation is fragmented | Translation and conversion effects change debt and ERC; matching is partial and not quantified | Material | CP-1A geography row; 10-K page:65 |
| Structural ranking | Secured facilities of USD 2,130.6 million have first claim on pledged assets and subsidiary equity; the notes are unsecured | Noteholders' position depends on collateral value and guarantor reach, which are not evidenced | Material | CP-1 debt table |
| Regulatory and litigation | CFPB supervision, multi-state Attorneys General matter since 2015 with an accrual of undisclosed amount | A settlement or practice change could cost cash and slow collections | Material | CP-1A operating model row |
| Shareholder returns | Repurchases of USD 20.0 million in the first half of 2026 and a USD 150 million program | Competes with debt reduction while purchases are debt funded; covenant baskets cap it | Minor | CP-1A governance table |
| Floating rate exposure | About 40% of debt is not fixed or hedged; 50 basis points is about USD 7.8 million per year | Modest next to cash interest of USD 253.4 million | Minor | Q2 10-Q page:46 |

### Checks against the filings and the upstream handoffs

| Check | Result |
| --- | --- |
| Gross and net leverage and cover recomputed from CP-1 inputs (debt principal USD 3,771.3 million, cash USD 132.4 million, Adjusted EBITDA USD 1,358.9 million, cash interest USD 253.4 million) | 2.78x, 2.68x and 5.36x, as in CP-1 |
| Availability USD 998.5 million equals the sum of committed less drawn on the three revolvers (Q2 10-Q page:40 and page:41) | Agrees |
| Interest rate mix and sensitivity (Q2 10-Q page:46) and next 12 months obligations (page:42) | Opened; used in findings above |
| Foreign exchange mitigation (10-K page:65) | Opened; used as a strength |
| Corrections to upstream handoffs | None found. CP-1A's characterisation of the European review as ERC, not income, is retained and applied here |

## Calculations

Inputs are from the CP-1 and CP-1A handoffs and the cited pages, in thousands of USD unless stated.

- K1, maturity concentration: 2029 principal 1,837,149 / 3,771,251 = 48.7%. Principal due by end-2028: 5,000 + 10,000 + 408,245 = 423,245; 423,245 / 3,771,251 = 11.2%. The 2028 notes mature on February 1, 2028, 453 days after the as-of date of 2026-11-05 (about 14.9 months); the October 28, 2029 revolver maturity is 1,088 days after it (about 3.0 years).
- K2, secured share: credit facility borrowings 2,130,621 / 3,771,251 = 56.5%; senior notes 1,640,630 / 3,771,251 = 43.5%. Whether the Colombian facility (245) is secured is not stated and is immaterial to the share.
- K3, ERC-based share of availability: 733,096 / 998,468 = 73.4%.
- K4, liquidity cover of the next 12 months: cash 132,431 + availability 998,468 = 1,130,899; divided by the printed estimate of interest, unused fees and principal payments for the next 12 months of 247,700 (Q2 10-Q page:42) = 4.57x. Availability alone: 998,468 / 247,700 = 4.03x. Letters of credit drawn are Not supplied, so no deduction is made.
- K5, interest rate sensitivity: 7,800 / 253,430 (cash interest, CP-1 C4) = 3.1% of cash interest per 50 basis points, on the company's estimate (Q2 10-Q page:46).
- K6, illustrative cost-adjusted ERC cover (analyst construct, not an issuer measure): ERC 8,894,515 x Q2 2026 cash efficiency ratio 61.2% (Q2 10-Q page:25) = 5,443,443; divided by debt principal 3,771,251 = 1.44x. ERC is undiscounted, before interest and taxes, and assumes the cost ratio persists; the result is a sensitivity and not a coverage test.
- K7, growth rates used in findings: debt principal 3,771,251 / 3,337,541 − 1 = 13.0%; Adjusted EBITDA 1,358,913 / 1,137,552 − 1 = 19.5% (CP-1 C9). Cash collections 558,545 / 536,288 − 1 = 4.2%, matching the printed 4.2% (Q2 10-Q page:25).
- K8, funding shortfall after cash interest, taxes and capital expenditure: FY2025 −190,676 and FY2024 −502,881 (CP-1 C8, recomputed: 1,315,474 − 259,061 − 38,528 − 1,203,740 − 4,821 and 1,137,552 − 224,099 − 5,222 − 1,407,067 − 4,045).
- K9, share of income from operations: 96,924 / 153,282 = 63.2% (CP-1 C9).

## Gaps

| Gap | What it affects | Severity | Action |
| --- | --- | --- | --- |
| Covenant ratio levels and covenant EBITDA definition not supplied | Headroom, distribution capacity, drawing conditions; confidence capped below High | High | Supply the executed credit agreements and compliance certificates |
| Executed credit agreements and indentures, including the amended European agreement, not supplied (inherited from CP-0 and CP-1A) | Legal capacity, guarantor reach, ranking and the joint venture investment basket | High | Supply the documents |
| Nothing after August 7, 2026, including any report for the quarter ended September 30, 2026 | Current leverage, liquidity and ERC at the as-of date | Medium | Supply later filings or confirm none |
| Letters of credit drawn, and the maturity of interest-bearing deposits of USD 100.5 million | Liquidity net of usage, debt perimeter | Medium | Supply usage and deposit detail |
| Seller concentration, accrued amount for the Attorneys General matter, use of proceeds of the 2032 notes | Supply and litigation risk | Medium | Supply if disclosed |
| Ratings, market prices and valuation inputs | Market view | Low | Not required for this module |
| Proxy statement | Ownership and governance detail | Low | Supply if governance scoring is needed |

## Next module

CP-5: trace the figures in the Key findings and Calculations to their CP-1 tables and cited pages; check that every statement about covenant limits is framed as not comparable to the Adjusted EBITDA ratios; check that the European ERC increase is never presented as income; and treat the cost-adjusted ERC cover (K6) and the secured share (K2) as analyst constructs.
