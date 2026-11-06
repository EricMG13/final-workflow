# CP-5 - Evidence trace and research-integrity grade: Clear Channel Outdoor Holdings, Inc. (cco)

## Request

Evidence trace and research-integrity grade for Clear Channel Outdoor Holdings, Inc. (issuer id cco), as of 2026-11-05, on the credit_snapshot pathway, run id cco-2026-11-05-credit_snapshot-host. It audits the four accepted upstream handoffs (source readiness, financial base, business and transaction context, credit synthesis) against the seven pinned issuer sources, in USD. It changes no credit conclusion and silently repairs no lineage; where it corrects an upstream statement it says so, because the earlier handoffs cannot be edited.

## Sources

Locator convention: "S4 page:12" is the retained text chunk numbered 12 in source S4, not a printed page. Every locator below was opened in the retained text and the figure, wording or note checked there.

Issuer sources relied on:

| Label | Exact source name | sha256 |
| --- | --- | --- |
| S1 | 10-K_2025-12-31_cco-20251231.htm.jsonl | 571124584b3bbe99a4fbff8adfaba5f0fb8933c5a0003d1ef35708c36c286d39 |
| S2 | 10-Q_2025-09-30_cco-20250930.htm.jsonl | 607e09a97951d1ad4c47649541e08f4b1e6c417cc3bd1376061667bd020f7126 |
| S3 | 10-Q_2026-03-31_cco-20260331.htm.jsonl | a3ad502aa08b83254f97c12e4f79050207a26c6003570b7bd60e33a1124d566c |
| S4 | 10-Q_2026-06-30_cco-20260630.htm.jsonl | fc57da6e0f4d7240050e6201742116917e571f4d11e190fcdcea84112429a51c |
| S5 | EX-99.1_2026-02-26_exhibit991-ccohearningsrel.htm.jsonl | 5cc1d0e97fcf82997c8a6a84c737a99df944d52765b5ff540d0441e7f806a5a6 |
| S6 | EX-99.1_2026-05-06_exhibit991-ccohearningsrel.htm.jsonl | d85dec563195c10f63eb072d829bbf7b6a81552ec09b651fb1bdefa50ffbbbd6 |
| S7 | EX-99.1_2026-08-05_exhibit991-ccohearningsrel.htm.jsonl | 86540d4f0d27c129f16354d25b76c67a8e72d707aa0c050724d976a7c4c17aa5 |

Supplied handoffs (each re-anchored to issuer name, as-of date and run id):

| Module | sha256 | Scope consumed |
| --- | --- | --- |
| CP-0 | c71e4b6220652757facb8cbe1e745147a9ea4d59240f1f57156457c376ee1b60 | Source readiness, seven sources, information boundary at August 5, 2026, gaps |
| CP-1 | fca9d4b8c375c5150877961d771a19c3bb05bdf148b7d27b2dc87fc69f48ca80 | Financial base, charts, registers, calculations C1 to C11 |
| CP-1A | e856477b20f063796951e436fe80db366086d45d4647096c504e5378286eadf2 | Business and transaction context, behaviour table, timeline, calculations C1 to C3 |
| CP-2 | 5649d186c5f31a78a89acbc6401a407f32af5d24c7818050c0ac8b22b38a06e5 | Credit synthesis, key findings, strengths and weaknesses, risks, calculations C1 to C10 |

Context file (settings only, not issuer evidence): sha256 de960bbc410d3388b8cf7496a6e161733b9fd5ffc09b25a54e06ffd5d05f0294. It leaves ratings, quotes and valuation blank.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream analysis is traceable: all 25 material claims tested have identified support and every calculation reproduces from printed inputs. Committee use is restricted because the merger outcome and the executed debt documents are not supplied. | Medium | Nothing after August 5, 2026 and no executed indenture or credit agreement is supplied, so the capital structure at the cutoff and legal terms cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of 25 material claims, 13 are directly sourced and 8 are calculated; every calculation reproduced exactly from printed inputs. | Headline leverage of 9.46x, cover of 1.40x and free cash flow of 84.3 can be relied on as arithmetic. | High |
| Three conclusions rest on analyst inference and one on an assumption: the credit view, the airport margin reading, the behaviour classification and the forward cover. | They shape the credit view but need executed documents and later filings to firm up. | Medium |
| The first outside date for the merger, November 9, 2026, falls after the cutoff and no source reports the outcome. | The owner and capital structure at the cutoff cannot be confirmed from the sources. | High |
| One statement in the business context credits the company with a funding representation that the filing attributes to the buyer. | No figure changes, but the buyer's funding assurance is the buyer's, not the company's. | High |
| The confidence score is 51, band Low, quality status Restricted. | Committee use needs disclosure of the two material findings. | High |

### Evidence trace view

The upstream analysis is traceable enough for restricted committee use, and the main provenance gap is that nothing after August 5, 2026 and no executed financing document is supplied. Of 25 material claims, 13 are directly sourced from filed statements and releases, 8 are calculated and each reproduced exactly when recomputed from the printed inputs, 1 rests on an assumption and 3 are analyst inference. The inference claims are the overall credit view, the airport margin reading and the issuer-behaviour classification. Two material findings and four minor findings remain open, giving a score of 51, a Low band and Restricted status. One mis-attribution in the business context was found and is corrected here, and one earlier search-scope question was closed by running the search across all seven sources.

### Traceability summary

| Module | Claims tested | Directly sourced or calculated | Inference or assumption | Open issues |
| --- | --- | --- | --- | --- |
| CP-0 | Source coverage, boundary and gap statements | All located | None | 1 |
| CP-1 | Statements, ratios, registers, charts | All | None | 4 |
| CP-1A | Business facts, merger and debt actions, behaviour | Facts yes; behaviour reading no | 2 | 4 |
| CP-2 | Synthesis, sensitivities, risks | Figures yes; view and forward cover no | 2 | 4 |

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cco-20251231.htm.jsonl | High (filed, audited statements; MD&A unaudited) | FY2025 with FY2024 and FY2023 | Clear Channel Outdoor Holdings, Inc. and subsidiaries, consolidated, continuing operations | Statements, debt, leases, commitments, merger risk factors, dispositions | Part III deferred to a Form 10-K/A not supplied; text extraction only | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2025-09-30_cco-20250930.htm.jsonl | High (filed, unaudited) | Q3 2025 and nine months 2025 | Same | Q3 2025 revenue, Spain sale agreement | Original presentation; superseded by the 10-K at year end | CP-1, CP-1A |
| S3 | 10-Q_2026-03-31_cco-20260331.htm.jsonl | High (filed, unaudited) | Q1 2026 | Same | March 31, 2026 balance sheet, facility availability, merger wording | Quarterly columns only | CP-1, CP-1A |
| S4 | 10-Q_2026-06-30_cco-20260630.htm.jsonl | High (filed, unaudited) | Q2 2026 and H1 2026 with 2025 comparatives | Same | Latest balance sheet, statements, debt, liquidity, covenant text, merger status | Latest filing; nothing later is supplied | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-02-26_exhibit991-ccohearningsrel.htm.jsonl | Medium (issuer release, non-GAAP) | Q4 and FY2025 | Same, management presentation | Adjusted EBITDA, segments, AFFO | Non-GAAP; not independent of the 10-K | CP-1 |
| S6 | EX-99.1_2026-05-06_exhibit991-ccohearningsrel.htm.jsonl | Medium (issuer release, non-GAAP) | Q1 2026 | Same | Q1 2026 Adjusted EBITDA | Non-GAAP | CP-1 |
| S7 | EX-99.1_2026-08-05_exhibit991-ccohearningsrel.htm.jsonl | Medium (issuer release, non-GAAP) | Q2 2026 and H1 2026 | Same | Adjusted EBITDA reconciliation, display counts, issuer net debt | Non-GAAP | CP-1, CP-1A |

### Top credit drivers and their traceability

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Earnings-led deleveraging: trailing Adjusted EBITDA 544.3 and total debt to Adjusted EBITDA 9.46x | CP-1, CP-2 | Release reconciliations and filed principal; calculated | Sets debt service capacity and refinancing access | Leverage tolerance and monitoring posture | S5 page:9; S7 page:9; S4 page:15 | Issuer-defined Adjusted EBITDA; covenant EBITDA not supplied |
| 2 | Thin cash interest cover of 1.40x and trailing free cash flow of 84.3 | CP-1, CP-2 | Filed cash flow statements and release; calculated | Cash left after interest and capital spending | Debt service resilience | S1 page:80; S4 page:5; S4 page:6 | Cash flow and cash interest include discontinued operations |
| 3 | Pending merger at 2.43 per share with outside date November 9, 2026 and merger-linked debt amendments and redemption notices | CP-1A, CP-2 | Filed merger description and risk factors | Determines owner, change-of-control terms and the 2028 and 2029 maturities | Capital structure at the cutoff | S4 page:8; S4 page:16; S4 page:17; S1 page:24 | Status after August 5, 2026 and executed documents not supplied |
| 4 | Maturity concentration: 1,324.6 in 2028 and 906.3 in 2029, 1,805.3 of unsecured notes behind 3,340.0 of secured debt | CP-1, CP-2 | Filed maturity schedule and debt table | Refinancing and ranking | Loss given default mechanics, refinancing risk | S1 page:117; S4 page:15; S1 page:114; S1 page:116 | Schedule dated December 31, 2025; guarantor list not supplied |
| 5 | Fixed airport rent: site lease expense 59.2% of airport revenue against 31.3% in America | CP-1A, CP-2 | Filed segment note and MD&A; calculated | Airport growth adds minimum-guarantee rent | Margin and cash conversion | S4 page:12; S4 page:28; S1 page:119 | Interim lease terms not supplied |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FY2025 and FY2024 revenue, operating income and Adjusted EBITDA 504.8 and 475.8 | CP-1 | S1 page:78; S5 page:9 | Yes | High; Adjusted EBITDA non-GAAP | Directly Sourced | Supported | High | Committee-Ready |
| H1 2026 and H1 2025 statements; Adjusted EBITDA 247.3 and 207.8 | CP-1 | S4 page:3; S7 page:9 | Yes | High; Adjusted EBITDA non-GAAP | Directly Sourced | Supported | High | Committee-Ready |
| Debt principal by instrument at June 30, 2026 | CP-1, CP-2 | S4 page:15 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Cash 192.1 and excess availability 205.5 | CP-1, CP-2 | S4 page:2; S4 page:33 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Springing covenant of 7.10x not in effect; compliance statement | CP-1, CP-2 | S4 page:34; S4 page:16; S1 page:109 | Yes | High (issuer assertion on compliance) | Directly Sourced | Supported | Medium | Committee-Ready |
| Merger at 2.43 per share, approvals, termination fees 39.8 and 92.9 | CP-1A, CP-2 | S4 page:8; S1 page:53; S1 page:54 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Outside date November 9, 2026 extendable to February 9, 2027 | CP-1A, CP-2 | S1 page:24 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Consents, amendments and conditional redemption notices tied to the merger | CP-1, CP-1A, CP-2 | S4 page:16; S4 page:17; S4 page:38; S4 page:39 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Spain sale completed August 4, 2026 for about 132.3 | CP-1, CP-1A | S4 page:9; S4 page:22 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Segment revenue, Segment Adjusted EBITDA and site lease expense | CP-1, CP-1A | S4 page:12; S4 page:13; S1 page:99; S1 page:60; S1 page:61 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Operating lease liabilities 1,361.9 and commitments 877.6 and 152.7 | CP-1 | S4 page:2; S1 page:117; S1 page:118 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Maturity schedule at December 31, 2025 totalling 5,148.9 | CP-1, CP-2 | S1 page:117 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| 2025 disposals, 605 million debt reduction, August 2025 refinancing | CP-1A | S1 page:55; S1 page:69; S1 page:93; S1 page:94; S1 page:102 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| LTM Adjusted EBITDA 544.3 | CP-1 | C1 from S5 page:9; S7 page:9 | Yes | High inputs; non-GAAP | Calculated | Supported with definition limitation | Medium | Committee-Ready |
| LTM cash paid for interest 390.1 | CP-1 | C2 from S1 page:80; S4 page:6 | Yes | High inputs | Calculated | Supported with perimeter limitation | Medium | Committee-Ready |
| Total debt to Adjusted EBITDA 9.46x; net 9.11x | CP-1, CP-2 | C3 from S4 page:15; S4 page:2 | Yes | High inputs | Calculated | Supported | High | Committee-Ready |
| Adjusted EBITDA to cash interest 1.40x (1.28x FY2025, 1.09x FY2024) | CP-1, CP-2 | C4 from S5 page:9; S1 page:80; S4 page:6 | Yes | High inputs | Calculated | Supported | Medium | Committee-Ready |
| Trailing free cash flow 84.3 | CP-1, CP-2 | C7 from S1 page:80; S4 page:5 | Yes | High inputs | Calculated | Supported with perimeter limitation | Medium | Committee-Ready |
| Secured debt 3,340.0, 6.14x and 64.9% of principal | CP-1, CP-2 | C3 from S4 page:15 | Yes | High inputs | Calculated | Supported | High | Committee-Ready |
| Segment margins 41.0% and 25.3%; site lease shares 31.3% and 59.2% | CP-1A, CP-2 | C1 from S4 page:12 | Yes | High inputs | Calculated | Supported | High | Committee-Ready |
| Break-even 28.3%; 10% EBITDA decline gives 10.51x and 1.26x; EBITDA less capital expenditure cover 1.20x | CP-2 | C1, C2, C7 from CP-1 inputs | Yes | High inputs; scenario arithmetic | Calculated | Supported | Medium | Committee-Ready |
| Forward cover 1.38x on the issuer's 2027 cash interest estimate of about 394 | CP-2 | S4 page:32 and CP-1 C-series | Yes | Medium (issuer estimate on June 30, 2026 debt) | Assumption-Based | Partially supported | Low | Remediation Needed |
| Overall view: highly leveraged and stabilising | CP-2 | Synthesis of rows above | Yes | Medium | Analyst Inference | Supported by cited basis | Medium | Committee-Ready |
| Airport growth adds fixed rent and dilutes consolidated margin | CP-1A, CP-2 | S4 page:12; S4 page:28; S1 page:119 | Yes | Medium (interpretation of cited facts) | Analyst Inference | Supported by cited basis | Medium | Committee-Ready |
| No creditor-adverse action documented; open-market repurchases classed Neutral or Mixed | CP-1A | S1 page:102; S1 page:111; S4 page:16 | Partial | Medium (summaries of legal documents) | Analyst Inference | Partially supported | Low | Remediation Needed |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt (carrying) 5,107.6 and principal components | source-text/10-Q_2026-06-30_cco-20260630.htm.jsonl | 10-Q_2026-06-30_cco-20260630.htm.jsonl | S4 | page:15 / Note 5 | Debt register | Sourced | High | Components plus finance leases add to principal 5,148.8 |
| Adjusted EBITDA 504.8 (FY2025) and 475.8 (FY2024) | source-text/EX-99.1_2026-02-26_exhibit991-ccohearningsrel.htm.jsonl | EX-99.1_2026-02-26_exhibit991-ccohearningsrel.htm.jsonl | S5 | page:9 / reconciliation | Financials table | Sourced | Medium | Non-GAAP; reconciliation columns add to the totals |
| Adjusted EBITDA 247.3 (H1 2026) and 207.8 (H1 2025) | source-text/EX-99.1_2026-08-05_exhibit991-ccohearningsrel.htm.jsonl | EX-99.1_2026-08-05_exhibit991-ccohearningsrel.htm.jsonl | S7 | page:9 / reconciliation | Financials table | Sourced | Medium | Same definition as S5 page:8 and S7 page:7 |
| Cash paid for interest 394.4, 434.5, 205.8 and 210.2 | source-text/10-K_2025-12-31_cco-20251231.htm.jsonl | 10-K_2025-12-31_cco-20251231.htm.jsonl | S1 | page:80 / cash flow supplemental; S4 page:6 | Interest cover | Sourced | High | Includes discontinued operations |
| Operating cash flow and capital expenditures | source-text/10-K_2025-12-31_cco-20251231.htm.jsonl | 10-K_2025-12-31_cco-20251231.htm.jsonl | S1 | page:80; S4 page:5 | Free cash flow | Sourced | High | Includes discontinued operations; continuing capital expenditures at S1 page:99 and S4 page:13 |
| Cash 192.1 and facility availability 205.5 | source-text/10-Q_2026-06-30_cco-20260630.htm.jsonl | 10-Q_2026-06-30_cco-20260630.htm.jsonl | S4 | page:2; page:33 | Liquidity | Sourced | High | Facility columns sum to 205.4; rounding footnote at S4 page:34 |
| Springing covenant 7.10x not in effect | source-text/10-Q_2026-06-30_cco-20260630.htm.jsonl | 10-Q_2026-06-30_cco-20260630.htm.jsonl | S4 | page:34 / Debt Covenants | Covenants | Sourced | High | Definitions in documents not supplied |
| Merger terms, approvals and fees | source-text/10-Q_2026-06-30_cco-20260630.htm.jsonl | 10-Q_2026-06-30_cco-20260630.htm.jsonl | S4 | page:8 / Note 1 | Transaction summary | Sourced | High | Agreement itself not supplied |
| Outside date November 9, 2026 and February 9, 2027 | source-text/10-K_2025-12-31_cco-20251231.htm.jsonl | 10-K_2025-12-31_cco-20251231.htm.jsonl | S1 | page:24 / Item 1A | Transaction summary | Sourced | High | Risk factor wording; not repeated in the 10-Qs |
| Maturity schedule 312, 297, 1,324,631, 906,301, 865,251, 2,052,105 (thousands) | source-text/10-K_2025-12-31_cco-20251231.htm.jsonl | 10-K_2025-12-31_cco-20251231.htm.jsonl | S1 | page:117 / Note 6 | Debt maturities chart | Sourced | High | Dated December 31, 2025 |
| Segment revenue, Segment Adjusted EBITDA, site lease expense | source-text/10-Q_2026-06-30_cco-20260630.htm.jsonl | 10-Q_2026-06-30_cco-20260630.htm.jsonl | S4 | page:12 / Note 3; S1 page:99 | Segment table | Sourced | High | Segment Adjusted EBITDA is GAAP; Adjusted EBITDA non-GAAP |
| Operating lease liabilities and commitments | source-text/10-K_2025-12-31_cco-20251231.htm.jsonl | 10-K_2025-12-31_cco-20251231.htm.jsonl | S1 | page:117; page:118 / Notes 7 and 8; S4 page:2 | Claims outside debt | Sourced | High | Undiscounted lease payments at December 31, 2025 |
| Debt amendments and conditional redemption notices | source-text/10-Q_2026-06-30_cco-20260630.htm.jsonl | 10-Q_2026-06-30_cco-20260630.htm.jsonl | S4 | page:16; page:17 / Note 5 | Transaction summary | Sourced | High | Supplemental indentures and amendments listed at S4 page:38 and page:39, not supplied |
| Disposals and debt activity 2023 to 2025 | source-text/10-K_2025-12-31_cco-20251231.htm.jsonl | 10-K_2025-12-31_cco-20251231.htm.jsonl | S1 | page:55; page:69; page:93; page:94; page:102 | Timeline | Sourced | High | Executed documents not supplied |
| Out-of-home share of U.S. advertising spend 2.3% | source-text/10-K_2025-12-31_cco-20251231.htm.jsonl | 10-K_2025-12-31_cco-20251231.htm.jsonl | S1 | page:6 / Item 1 | Operating model | External (Omnicom model cited by the company) | Low | Third-party data quoted by the issuer; not independently checked; not used in any ratio |
| Management claims: leading position, rate-setting ability | source-text/10-K_2025-12-31_cco-20251231.htm.jsonl | 10-K_2025-12-31_cco-20251231.htm.jsonl | S1 | page:6; page:12 | Operating model | Management Language | Low (promotional) | Tagged Management Language upstream; not adopted |

### Calculation and assumption register

Each calculation was recomputed independently by parsing the printed inputs from the retained text of S1, S4, S5 and S7, not from the upstream handoff text.

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA | CP-1 C1; CP-2 | FY2025 504,790; H1 2026 247,279; H1 2025 207,815 (USD thousands) | 504,790 + 247,279 - 207,815 = 544,254; recomputed 544,254 | Calculated | Reproduced | Medium (non-GAAP) | Leverage, cover | S5 page:9; S7 page:9 |
| LTM cash paid for interest | CP-1 C2 | FY2025 394,429; H1 2026 205,848; H1 2025 210,220 | 394,429 + 205,848 - 210,220 = 390,057; recomputed 390,057 | Calculated | Reproduced | Medium (includes discontinued operations) | Debt service | S1 page:80; S4 page:6 |
| Debt principal including finance leases | CP-1 C3 | 425,000; 865,000; 1,150,000; 900,000; 899,311; 905,950; 3,489 | Sum 5,148,750; recomputed by parsing S4 page:15 | Calculated | Reproduced | High | Leverage | S4 page:15 |
| Total debt / Adjusted EBITDA; net | CP-1 C3 | 5,148,750; cash 192,138; 544,254 | 9.46 and 9.11; recomputed 9.46 and 9.11. FY2025 5,148,897 / 504,790 = 10.20 | Calculated | Reproduced | High | Leverage | S4 page:15; S4 page:2 |
| Adjusted EBITDA / cash interest | CP-1 C4 | 544,254 / 390,057; 504,790 / 394,429; 475,758 / 434,520 | 1.40; 1.28; 1.09; recomputed 1.40, 1.28 and 1.09 | Calculated | Reproduced | Medium | Coverage | S1 page:80; S4 page:6 |
| Free cash flow | CP-1 C7 | CFO 114,860 + 47,840 - 2,326; capex 82,879 + 35,323 - 42,080 | 160,374 - 76,122 = 84,252; recomputed 84,252 | Calculated | Reproduced | Medium (includes discontinued operations) | Liquidity | S1 page:80; S4 page:5 |
| Secured leverage | CP-1 C3 | 425,000 + 865,000 + 1,150,000 + 900,000 = 3,340,000 | 3,340,000 / 544,254 = 6.14; recomputed 6.14 | Calculated | Reproduced | High | Ranking | S4 page:15 |
| Segment margins and lease shares | CP-1A C1 | America 602,803, 188,736, 247,079; Airports 208,827, 123,589, 52,816 | 41.0%, 31.3%; 25.3%, 59.2%; recomputed by parsing S4 page:12 | Calculated | Reproduced | High | Margin structure | S4 page:12 |
| Equity consideration | CP-1A C2; CP-2 | 509,093,845 shares at July 31, 2026 x 2.43 | 1,237.1 million; recomputed 1,237.1 | Calculated | Reproduced | Medium (basic shares only) | Equity layer | S4 page:1 |
| Break-even, sensitivities and cover after capital expenditure | CP-2 C1, C2, C7 | 544,254; 390,057; 76,122; 5,148,750 | 28.3%; 10.51x and 1.26x at minus 10%; 1.20x; recomputed identically | Calculated | Reproduced | Medium | Resilience | CP-1 inputs |
| Forward cover | CP-2 C4 | 544,254 / 394,000 | 1.38; assumes the issuer's 2027 estimate and no refinancing or merger effect | Assumption-Based | Reproduced arithmetic; assumption partial | Low | Debt service | S4 page:32 |
| Maturity concentration and debt mix | CP-2 C6 | 1,324,631 + 906,301 = 2,230,932 of 5,148,897; 1,805,261 and 3,340,000 of 5,148,750 | 43.3%; 35.1%; 64.9%; recomputed | Calculated | Reproduced | High | Refinancing | S1 page:117; S4 page:15 |
| Maturity schedule composition | CP-1 C5 | 312 + 297 + 1,324,631 + 906,301 + 865,251 + 2,052,105 | 5,148,897; finance lease portions 320, 351, 251 and 2,105 add with 312 and 297 to 3,636 | Calculated | Reproduced | High | Refinancing | S1 page:117; S1 page:101 |

### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | Capital structure and owner at the cutoff | Merger outcome, redemptions and amendment effectiveness after August 5, 2026 are not in any source | Insufficient Information | Leverage, maturities and ownership at November 5, 2026 may differ from June 30, 2026 | Supply filings dated August 6, 2026 to November 5, 2026 | Credit view, maturity chart, transaction summary |
| MATERIAL | Ranking, change-of-control and covenant statements | Rest on issuer summaries; executed documents and guarantor list not supplied | Analyst Inference | Clause-level rights cannot be checked | Supply executed documents; legal review | Debt register, behaviour table, credit view |
| MINOR | Behaviour row on open-market repurchases | States purchases were not offered pro rata, which is inferred from the phrase open market | Analyst Inference | A presentation of inference as fact | Treat as inference; obtain the repurchase details | Behaviour table |
| MINOR | Forward cover 1.38x | Relies on the issuer's 2027 interest estimate and no refinancing | Assumption-Based | Forward view is not a forecast | Replace with post-cutoff data | Key findings |
| MINOR | Buyer funding assurance | Business context attributes a funding representation to the company | Weak Lineage | The filing attributes it to the buyer | Correct as recorded in F-04 | Transaction summary |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identification | Strong: every figure carries a source label and chunk locator | All upstream tables cite S1 to S7 pages | A reader can open the cited chunk | Low risk of orphan claims | None |
| Locator precision | Adequate: chunk numbers, not printed pages | Locator convention stated in each handoff | Chunk numbers differ from printed page numbers | Slows manual checks | State chunk-to-page mapping if exported |
| Calculation reproducibility | Strong: 13 of 13 register items reproduced | Calculation register above | Errors would change leverage or cover | None found | None |
| Separation of management claims from fact | Strong: tagged upstream | Management Language rows at S1 page:6 and page:12 | Promotional wording could be mistaken for fact | Handled | None |
| Version and subsequent-event control | Adequate: Spain sale and merger actions are kept as subsequent or pending; the maturity schedule is dated December 31, 2025 and used with June 30, 2026 balances | S4 page:9; S4 page:16; S1 page:117 | Mixing dates could misstate the profile | Principal unchanged between the two dates, so the effect is small | Replace with a June 30, 2026 schedule when printed |
| Legal-document support | Weak: summaries only | S4 page:38 and page:39 list exhibits not supplied | Rights and ranking cannot be clause-checked | Restricts legal conclusions | Add executed documents |

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| TG-1 | Merger outcome and events after August 5, 2026 | Filings and releases dated August 6, 2026 to November 5, 2026, including any closing or termination report | The owner, amendments and redemptions at the cutoff are unknown | Credit view, maturity chart, transaction summary | Caps status at Restricted | Form 8-K and Form 10-Q for the quarter ended September 30, 2026 if filed |
| TG-2 | Executed indentures, credit agreements and 2026 amendments | Exhibits cited at S4 page:38 and page:39 and S1 page:138 to page:139 | Ranking, change-of-control and covenant claims need clause support | Debt register, behaviour table, key risks | Caps status at Restricted | Exhibits to the cited Forms 8-K |
| TG-3 | Guarantor list and guarantor financial information | Guarantor schedule | Structural subordination of the unsecured notes cannot be quantified | Ranking statements | Lowers confidence | Annual report exhibit or guarantor schedule |
| TG-4 | Covenant EBITDA and covenant ratio | Credit agreement definitions | Headroom cannot be measured; the springing test was not in effect | Covenant view | Lowers confidence | Senior Secured Credit Agreement |
| TG-5 | Merger agreement, financing commitments and ownership | Merger agreement, financing letters, proxy statement, Form 10-K/A | Buyer capacity and intent, control and board are unknown | Sponsor alignment | Lowers confidence | Merger agreement exhibit, proxy, Form 10-K/A |
| TG-6 | Continuing-operations cash flow split | Company disclosure | Cover and free cash flow include discontinued operations | Trailing cash measures | Minor reduction | Company disclosure |

### Research integrity audit

Lane results. Unsupported claims: none found; the two material findings are stale-date and legal-document limits, not unsupported statements. One mis-attribution and one inference-as-fact were found (F-04, F-05). Calculation: no error found; perimeter and definition drift disclosed upstream (F-03). Legal and covenant: summary-only support (F-02). Market and relative value: no market or relative value claim exists in the upstream handoffs, and the context leaves quotes, ratings and valuation blank. Cross-module consistency: the shared datapoints agree. Evidence trace: no orphan claim found. Handoff envelope: all four handoffs carry the six required headings and anchors.

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-0, CP-1, CP-1A, CP-2 | Capital structure and owner at the cutoff (F-01) | Supported at June 30, 2026 only | Merger, amendments and redemptions are pending in the latest source; first outside date November 9, 2026 | Supply post-August 5, 2026 filings | Restricts Committee Use |
| MINOR | CP-1A | Funding representation (F-04) | Contradicted by the cited page | CP-1A states the company has represented that the buyer has sufficient funds; S1 page:24 says Parent has represented that it has sufficient funds | Read as a buyer representation; CP-1A cannot be edited | Monitoring Follow-Up |
| MINOR | CP-1A | Open-market repurchase row (F-05) | Partially Supported | Not pro rata is inferred, not stated | Treat as Analyst Inference | Monitoring Follow-Up |
| None | CP-0, CP-1, CP-1A, CP-2 | Figures cited to S1 to S7 | Supported | 25 claims traced; none unsupported | None | Monitoring Follow-Up |

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | LTM cash interest cover and free cash flow reproduced | Cash interest, operating cash flow and capital expenditures include discontinued operations while Adjusted EBITDA is continuing only; FY2024 debt includes the 375.0 CCIBV term loan (F-03) | None between sources; basis differs and is disclosed | Obtain a continuing-operations cash flow split | Monitoring Follow-Up |
| None | CP-1 | Leverage and cover reproduced | Principal including finance leases as total debt; operating leases excluded and disclosed | None | None | Monitoring Follow-Up |
| None | CP-1A, CP-2 | Segment margins, sensitivities and equity consideration reproduced | Analyst measures disclosed | None | None | Monitoring Follow-Up |

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-1A, CP-2 | Ranking and security of the term loan, secured notes and unsecured notes; guarantor perimeter (F-02) | Executed indentures, Senior Secured Credit Agreement, receivables-based credit agreement, intercreditor terms | Only the Note 6 summary at S1 page:104 to page:116 and S4 page:15 | Add documents; legal review | Legal Review Required |
| MATERIAL | CP-1A, CP-2 | Merger-linked amendments make the merger not a change of control; redemption notices are conditional (F-02) | Supplemental indentures dated April 9, 2026; Seventh Amendment dated April 10, 2026; Third Amendment dated May 15, 2026; redemption notices | Only the Note 5 summary at S4 page:16 and page:17 | Add documents; legal review | Legal Review Required |

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | All upstream modules | No market, spread, price or relative value claim is made | None required for the claims made | Context leaves quotes and valuation blank | None | Monitoring Follow-Up |

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| None | CP-1, CP-1A, CP-2 | Debt principal 5,148.8, trailing Adjusted EBITDA 544.3, leverage 9.46x, cover 1.40x, cash 192.1, availability 205.5, 3,340.0 secured and 1,805.3 unsecured agree across modules | None | None | Consistent |
| MINOR (F-06) | CP-1, CP-2 | Maturity chart uses a December 31, 2025 schedule with June 30, 2026 balances | Schedule printed only at year end; principal of every note and loan unchanged, finance leases down 0.1 | Replace when a June 30, 2026 schedule is printed | Small; disclosed in CP-1 |
| MINOR (resolved, F-07) | CP-0, CP-1 | CP-0 reported its search for pension, factoring and supply-chain finance as made in the annual report; CP-1 stated all seven sources | CP-0 cannot be edited; this audit ran the search across all seven sources | None further | Zero hits for factoring and supply-chain finance in all seven sources; pension appears only in a reclassification of translation losses on sold businesses, so CP-1 stands |
| None | CP-0, CP-1A | Buyer description differs across filings (with and without TWG Global) | Logged in CP-1A, not reconciled | None | Carried as a logged difference |

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Presentation | The financial base view is one long paragraph | None needed for the report; split if exported | Formatting / Hygiene Only |
| None | CP-1A, CP-2 | Duplication | Repeated ratios (9.46x, 1.40x) and the November 9, 2026 date appear in several sections for different purposes | None | None |

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| None | CP-0, CP-1, CP-1A, CP-2 | Six required headings, reader summary and opening view | None | None | Accepted by CP-OS |
| None | CP-1 | Chart tables | Headers and plain-number cells meet the report selectors | None | Charts populate |
| None | CP-1A, CP-2 | Prose-only sections | No tables under prose-only headings | None | Report sections populate |

#### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-01 | MATERIAL | CP-0, CP-1, CP-1A, CP-2 | Stale-Date Support Gap | Nothing after August 5, 2026 is supplied; merger outcome, outside date November 9, 2026, amendments and redemptions at the cutoff are unknown | Supply filings dated August 6, 2026 to November 5, 2026 | Restricts Committee Use | Open |
| F-02 | MATERIAL | CP-1, CP-1A, CP-2 | Legal Support Gap | Ranking, change-of-control, covenant and guarantor claims rest on issuer summaries; executed documents and guarantor list not supplied | Add documents; legal review | Requires Legal Review | Open |
| F-03 | MINOR | CP-1, CP-2 | Formula / Definition Drift | Cash interest, operating cash flow and capital expenditures include discontinued operations; FY2024 debt includes the CCIBV term loan | Obtain a continuing-operations split | Monitoring Follow-Up | Open |
| F-04 | MINOR | CP-1A | Misattributed Statement | Funding representation credited to the company; the filing attributes it to Parent | Read as a buyer representation; CP-1A cannot be edited | Monitoring Follow-Up | Open |
| F-05 | MINOR | CP-1A | Inference Presented as Fact | Open-market repurchases described as not offered pro rata without a source statement | Treat as Analyst Inference | Monitoring Follow-Up | Open |
| F-06 | MINOR | CP-1, CP-2 | Version Control | Maturity schedule dated December 31, 2025 used with June 30, 2026 balances | Replace with a June 30, 2026 schedule when printed | Monitoring Follow-Up | Open |
| F-07 | MINOR | CP-0, CP-1 | Citation Gap | Search scope for pension, factoring and supply-chain finance differed between CP-0 and CP-1 | Search run across all seven sources | Monitoring Follow-Up | Resolved |

#### Remediation priority

First, supply the filings dated August 6, 2026 to November 5, 2026 (closes F-01, TG-1). Second, add the executed financing documents, the merger agreement and the guarantor schedule (closes F-02, TG-2 to TG-5). Third, obtain a continuing-operations cash flow split and the June 30, 2026 maturity schedule (F-03, F-06, TG-6).

#### Clearance and score

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 4 open and 1 resolved. Committee Use: Restricted.

No claim in the upstream handoffs is miscalculated, and one statement is mis-attributed; committee use is restricted because two material findings (F-01 and F-02) limit capital-structure and legal-structure conclusions to what the filings summarise as of June 30, 2026. The resolved issue (F-07) is not counted as open.

Confidence score, from the script confidence_score.py with 25 material claims (13 Directly Sourced, 8 Calculated, 1 Assumption-Based, 3 Analyst Inference), all 17 required registers present, source gate pass, open findings 2 MATERIAL and 4 MINOR: E = 87.6, C = 100.0, S = 1.0, P = 42, score = clamp((0.6 x 87.6 + 0.4 x 100) x 1.0 - 42, 0, 100) = 50.56, rounded 51. Band Low. qa_status Restricted. committee_status Restricted.

### Input module register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/.../1.response.md; cco-2026-11-05-credit_snapshot-host | Seven sources, boundary at August 5, 2026 | High | Six H2 headings and reader summary present | Accepted | Gap on post-August 5, 2026 events carried forward |
| CP-1 | requests/CP-1/.../1.response.md; cco-2026-11-05-credit_snapshot-host | Financial base, five report selectors | High | Six H2 headings, chart tables and metrics table present | Accepted | Perimeter and definition limits disclosed |
| CP-1A | requests/CP-1A/.../1.response.md; cco-2026-11-05-credit_snapshot-host | Business and transaction context, two tables and one prose section | High with one mis-attribution | Six H2 headings, selectors present | Accepted | F-04 and F-05 recorded here |
| CP-2 | requests/CP-2/.../1.response.md; cco-2026-11-05-credit_snapshot-host | Credit synthesis, two prose selectors | High | Six H2 headings, opening view of 116 words | Accepted | Forward cover is assumption-based |

## Calculations

C1. Independent recomputation. Inputs were parsed from the retained text of S1 (page 80), S4 (pages 1, 2, 5, 6, 12, 15), S5 (page 9) and S7 (page 9), not copied from the handoffs: Adjusted EBITDA 504,790, 475,758, 247,279 and 207,815; cash paid for interest 394,429, 434,520, 205,848 and 210,220; operating cash flow 114,860, 47,840 and 2,326; capital expenditures 82,879, 35,323 and 42,080; principal components 425,000, 865,000, 1,150,000, 900,000, 899,311, 905,950 and finance leases 3,489; cash 192,138 (USD thousands).
- LTM Adjusted EBITDA: 504,790 + 247,279 - 207,815 = 544,254.
- LTM cash interest: 394,429 + 205,848 - 210,220 = 390,057.
- LTM free cash flow: (114,860 + 47,840 - 2,326) - (82,879 + 35,323 - 42,080) = 160,374 - 76,122 = 84,252.
- Principal: 5,148,750. Total debt to Adjusted EBITDA: 5,148,750 / 544,254 = 9.46. Net: (5,148,750 - 192,138) / 544,254 = 9.11.
- Cash interest cover: 544,254 / 390,057 = 1.40; 504,790 / 394,429 = 1.28; 475,758 / 434,520 = 1.09.
- Secured leverage: 3,340,000 / 544,254 = 6.14.
All reproduce the figures in the financial base.

C2. Recomputation of the other handoffs. Segment margins and lease shares from S4 page:12: America 247,079 / 602,803 = 41.0% and 188,736 / 602,803 = 31.3%; Airports 52,816 / 208,827 = 25.3% and 123,589 / 208,827 = 59.2%. Equity consideration: 509,093,845 x 2.43 = 1,237,098,043. Sensitivity: 544,254 x 0.9 = 489,828.6; 5,148,750 / 489,828.6 = 10.51; 489,828.6 / 390,057 = 1.26; break-even (544,254 - 390,057) / 544,254 = 28.3%; EBITDA less capital expenditure cover (544,254 - 76,122) / 390,057 = 1.20; forward cover 544,254 / 394,000 = 1.38; maturity concentration (1,324,631 + 906,301) / 5,148,897 = 43.3%.

C3. Cross-module datapoint check: principal 5,148.8, trailing Adjusted EBITDA 544.3, 9.46x, 1.40x, cash 192.1 and availability 205.5 appear in CP-1 and CP-2 with identical values; the merger terms 2.43, 39.8 and 92.9 appear in CP-0, CP-1 and CP-1A with identical values; the outside date November 9, 2026 appears in CP-1A and CP-2.

C4. Claim counts: 13 + 8 + 1 + 3 = 25 material claims.

C5. Direction checks used upstream: leverage fell from 10.20x at FY2025 to 9.46x on the trailing basis (5,148,897 / 504,790 = 10.20); principal moved from 5,148,897 to 5,148,750, essentially flat; cover rose from 1.28x to 1.40x.

## Gaps

- Events after August 5, 2026 are not supplied: merger closing or termination, the November 9, 2026 outside date, amendment effectiveness and note redemptions (F-01, TG-1).
- Executed indentures, credit agreements, amendments, the merger agreement and the guarantor schedule are not supplied; legal and ranking claims rest on filing summaries (F-02, TG-2, TG-3, TG-5).
- Covenant EBITDA and the covenant ratio are not available; the springing test was not in effect (TG-4).
- Cash flow and cash interest include discontinued operations; a continuing-operations split is not supplied (F-03, TG-6).
- Chunk locators are not printed page numbers, and no image, chart or XBRL content was inspected, so presentation-only content could not be traced.
- The confidence script was run with the analyst's lineage classification and severity judgments; the arithmetic is script-owned, the classifications are not.

## Next module

This is the last module in the minimum set. The report should carry the Restricted status and the two material findings (F-01 and F-02) alongside the key findings, financial charts and transaction summary, and should read the buyer's funding assurance as the buyer's representation (F-04). The remediation list above is the follow-up needed to lift the restriction.
