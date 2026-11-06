## Request

Evidence trace and research-integrity review for Service Properties Trust (SVC, issuer id svc), as of 2026-11-05, pathway credit_snapshot, reporting currency USD. The module re-opens the pinned filings, checks the four upstream handoffs (source readiness, financial base, business and transaction context, credit synthesis) against them, recomputes every derived figure, grades what the trace finds, and states whether committee use is permitted, restricted or blocked. Amounts are USD thousands as the filings print them unless stated. A locator `page:N` is the chunk number in the pinned file, not a printed page.

## Sources

### Issuer sources re-opened for this trace

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_svc-20251231.htm.jsonl | 15b3016df80eabdf6701b53b9a448339a1d5ae915a5566d3f751538a9f1cf080 |
| 10-Q_2026-03-31_svc-20260331.htm.jsonl | ddc1e35889e90bee1694334ce247e9f387726f16b7ce89bd8b9a51b4f4bc89df |
| 10-Q_2026-06-30_svc-20260630.htm.jsonl | da660527db0f1353ac545e91f43f35b2233d5df64df735bb0e6f23f04bc598ba |
| 10-Q_2026-09-30_svc-20260930.htm.jsonl | f0504ddf51d9be829b263ff0aec5ab5ea7aa542d5518e107dbff10e9d9d5c34a |
| EX-99.1_2026-05-06_svc_033126xexhibitx991.htm.jsonl | 2f1a4993f8cd70e48576dc6e794111c2977d7a50e2e8b2ecb75d059468ae6628 |
| EX-99.1_2026-08-05_svc_063026xexhibitx991.htm.jsonl | fb76ab0c1c7105cbf6ef323f85f2c808f256d901d8e982c18e3c61667221ab25 |
| EX-99.1_2026-11-04_svc_093026xexhibitx991.htm.jsonl | 865a9819dca5454c3d53aca165a47efc28c6cf0685e35747e559ffc2c9cf026d |

The context input (sha256 a72cf33ce12be07f9ed0051d7ed4f82ab1f3905d4d81ff0fe1a5919c08327fd3) holds settings only and is not issuer evidence.

### Handoffs reviewed

| Module | sha256 | Role |
| --- | --- | --- |
| CP-0 | 0fbb7ad07aadbbd8b3c01b679bc383a79e711cd00b11da3f74ea1f9d0cbdcdab | Source readiness |
| CP-1 | 6a8c23e0c79168d7d90c853c411952c21d17df0c9783a68c6978b27d49e01d73 | Financial base and credit metrics |
| CP-1A | 2feb1e684c3fd2d1a7a9d3b4a1f7d7192451d1bd4e5335771ac3bf362e13b7b9 | Business and transaction context |
| CP-2 | ffe190e5ec4ede1ba9bd1b0a371b17c3a17e0e39e8d58d5dfccbc2398a308656 | Fundamental credit synthesis |

All four handoffs were read in full. Short names: S1 is the 10-K FY2025, S2 to S4 the 10-Q filings for Q1, Q2 and Q3 2026, and S5 to S7 the three EX-99.1 announcements in date order.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis traces to the filings: headline figures recompute and quotes match. One earlier claim is wrong and corrected here: the debt to adjusted assets test, not debt service cover, has the smaller cushion. Committee use is restricted. | Medium | The credit agreement, indentures, ratings and revolver covenant ratios are absent, and the company reports no EBITDA, so leverage rests on an analyst proxy. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every headline figure traced to a filing page and recomputed, including principal debt of 4,652,322, liquidity of 690,118, leverage of 9.78x and cash interest cover of 1.41x. | The core debt, liquidity and maturity view can be relied on as stated. | High |
| Two earlier summaries called debt service cover the tighter indenture test, but the cushion is 10.2% on adjusted assets and 18.0% on debt service cover. | The asset test binds first; debt service cover is the more earnings-sensitive test. | High |
| The split of each year's maturities by instrument is inferred from the instrument table, while the yearly totals are printed. | Yearly totals can be relied on; the instrument-level split is interpretation. | Medium |
| Revolver covenant terms appear only in the annual report and no reported ratio exists anywhere. | Headroom on the facility that supplies nearly all liquidity cannot be traced or calculated. | High |

### Evidence trace view

The analysis is traceable enough for restricted committee use: every headline figure in the four handoffs traces to a filing page or to arithmetic on cited inputs, and the recomputed ratios agree. The strongest support is that debt, cash, revolver availability and maturities come straight from the latest quarterly filing and tie to its printed totals. The most important provenance gap is the revolver: its covenant terms appear only in the annual report and no reported ratio exists, so headroom on the facility that supplies nearly all liquidity cannot be traced or calculated. One earlier statement is wrong and is corrected below: debt service cover is not the tighter indenture test; the debt to adjusted assets test has the smaller cushion.

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K FY2025 | High: filed, audited | Year ended December 31, 2025, with FY2024 and FY2023 comparatives | Service Properties Trust and consolidated subsidiaries | Statements, debt note, maturities, revolver terms, covenant tests, leases, business description, RMR terms | Text extraction; Schedule III heading in millions against notes in thousands; share data not split-adjusted | Annual base, covenants, history |
| S2 | 10-Q Q1 | High: filed, unaudited | Three months ended March 31, 2026 | Same | Statements, debt note, revolver availability, covenant tests | Share data not split-adjusted | Quarterly columns, LTM |
| S3 | 10-Q Q2 | High: filed, unaudited | Three and six months ended June 30, 2026 | Same | Statements, debt note, revolver draw, covenant tests | Share data split-adjusted | Quarterly columns, LTM |
| S4 | 10-Q Q3 | High: filed, unaudited | Three and nine months ended September 30, 2026 | Same | Statements, debt note, maturity table, fixed-rate debt table, liquidity, covenant tests, related persons, hotel statistics, subsequent events to November 2, 2026 | No investor presentation; manager-reported hotel data unverified | Latest position |
| S5 | EX-99.1 May 6, 2026 | Medium: furnished by the company | Q1 2026 announcement | Same | Announcement and portfolio counts only | No financial figures | Cross-check only |
| S6 | EX-99.1 August 5, 2026 | Medium: furnished by the company | Q2 2026 announcement | Same | Announcement and portfolio counts only | No financial figures | Cross-check only |
| S7 | EX-99.1 November 4, 2026 | Medium: furnished by the company | Q3 2026 announcement | Same | Announcement, portfolio counts, mention of an investor presentation | Presentation not in the pack | Cross-check only |

Module status: Ready with Limitations, because the credit agreement, indentures, tenant financials and ratings are not in the pack, but every handoff is complete and no source is blocked. Traceability scope: Top 5 drivers plus every figure in a reader summary. Entity key: issuer id svc is present.

### Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Liquidity and refinancing | CP-1, CP-2 | Cash 40,118 and undrawn revolver 650,000; revolver matures June 29, 2027; maturities 584,150 in 2027 and 1,002,775 in 2028 | One secured facility is nearly all liquidity and expires in the same window as the largest maturities | Drives default and refinancing risk | S4 page:2, page:20, page:47, page:49 | Revolver covenant ratios not reported |
| 2 | Leverage and cover | CP-1, CP-2 | Principal debt 4,652,322; calculated LTM core EBITDA 475,642; 9.78x gross, 1.41x cash interest cover | High debt against thin earnings sets the cushion for rent or hotel shocks | Sizes leverage tolerance | S1 page:172, page:174; S2 page:3, page:4; S3 page:3, page:5; S4 page:3, page:5, page:20 | Company reports no EBITDA; proxy includes sold hotels |
| 3 | Tenant concentration | CP-1A, CP-2 | TA is 68.2% of annualized minimum rent; leases expire 2033; BP guaranty capped at 2,782,917 | One tenant and a capped guarantor carry most rent | Rent durability and 2032 refinancing | S4 page:12, page:56, page:58 | Tenant financials absent; coverage tenant-reported |
| 4 | Indenture covenant headroom | CP-1, CP-2 | 53.9% against 60%; 33.9% against 40%; 1.83x against 1.50x | Reported compliance with cushion | Near-term breach unlikely on these tests | S4 page:51; S3 page:49; S1 page:138 | Revolver tests unreported; definitions differ from the proxy |
| 5 | Secured share and subordination | CP-1, CP-1A, CP-2 | Secured share of principal debt 62.9% against 40.5%; 1,225,000 of unsecured notes unguaranteed | Unsecured creditors rank behind more secured claims | Loss given default for unsecured notes | S4 page:20, page:22, page:53; S1 page:194, page:197 | Collateral of the 8.625% notes due 2031 not detailed |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 4,652,322 and revolver undrawn at 650,000 | CP-1, CP-2 | S4 page:20, page:49 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Cash 40,118 and liquidity 690,118 | CP-1, CP-2 | S4 page:2; sum of cash and revolver | Yes | High | Calculated | Supported | High | Committee-Ready |
| Maturities 584,150 (2027) and 1,002,775 (2028), yearly totals | CP-1, CP-2 | S4 page:49 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Instrument split inside each maturity year | CP-1 | S4 page:62 fixed-rate table, derived by matching maturity years | Partial | High | Analyst Inference | Partly supported | Medium | Remediation Needed |
| LTM core EBITDA 475,642; 9.78x; 9.70x; 1.41x | CP-1, CP-2 | Statement lines in S1 to S4; recomputed below | Yes | High | Calculated | Supported (arithmetic) | Medium | Committee-Ready with the proxy caveat |
| Cash interest LTM 336,491 | CP-1, CP-2 | S1 page:174; S2 page:4; S3 page:5; S4 page:5 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Indenture tests at September 30, 2026 | CP-1, CP-2 | S4 page:51 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Debt service cover is the tighter test | CP-1, CP-2 | Reported tests, cushions recomputed below | Yes | High | Calculated | Not supported | Low | Remediation Needed |
| Revolver minimum fixed charge coverage 1.30x and debt yield 10% | CP-1, CP-2 | S1 page:195 | Yes | High | Directly Sourced | Supported; no reported ratio | High | Committee-Ready |
| TA 68.2% of annualized minimum rent; 2033 expiry; BP cap | CP-1A, CP-2 | S4 page:12, page:56, page:58 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Secured share 62.9% and 40.5% | CP-1A, CP-2 | S4 page:20; S1 page:194 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Hotel share of revenue 74.7% and expense ratio 85.7% (Q3 2026) | CP-1A, CP-2 | S4 page:3 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Manager termination fee on 19 to 20 years of fees | CP-1A, CP-2 | S1 page:100 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| All debt fixed rate except the undrawn revolver, average coupon 5.65% | CP-1, CP-2 | S4 page:62 | Yes | High | Calculated | Supported; exposure view is interpretation | Medium | Committee-Ready |
| No sponsor and no ownership beyond two holders near 6% | CP-1A, CP-2 | Absence in all seven sources; S1 Part III incorporates the proxy by reference | Not applicable | High | Insufficient Information | Not a finding | Low | Remediation Needed: proxy statement |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt at September 30, 2026 | Debt note | 10-Q Q3 | S4 | page:20 "(1) $1,725,000 aggregate outstanding principal amount of senior unsecured notes" | CP-1 debt table | Sourced | High | Components 1,725,000, 1,580,155 and 1,347,167 sum to the printed total |
| Maturity total | Debt maturities | 10-Q Q3 | S4 | page:49 "$ 4,652,322" | CP-1 maturity chart | Sourced | High | Equals the sum of components |
| Cash 40,118 | Balance sheet | 10-Q Q3 | S4 | page:2 "Cash and cash equivalents 40,118 346,813" | CP-1 liquidity | Sourced | High | Restricted cash of 22,374 excluded |
| Revolver availability | Debt note | 10-Q Q3 | S4 | page:20 "The maturity date of our revolving credit facility is June 29, 2027" | CP-1 liquidity | Sourced | High | Two six-month extension options |
| Yearly maturities | Maturity table | 10-Q Q3 | S4 | page:49 "2027 584,150 2028 1,002,775 2029 427,038 2030 402,038 Thereafter 2,235,322" | CP-1 maturity chart | Sourced | High | Revolver not in the table |
| Fixed-rate debt by instrument | Market risk | 10-Q Q3 | S4 | page:62 "Senior secured notes 1,000,000 8.625 % 86,250 2031 Semi-Annually" | CP-1 debt table | Sourced | High | Annual interest 263,082 |
| December 31, 2025 principal | Debt maturities | 10-K FY2025 | S1 | page:198 "Total $ 5,504,809" | CP-1 leverage | Sourced | High | Components on page:194 sum to the total |
| Indenture tests | Debt covenants | 10-Q Q3 | S4 | page:51 "Total debt / adjusted total assets 53.9% Maximum of 60%" | CP-1 covenants | Sourced | High | Also "Secured debt / adjusted total assets 33.9% Maximum of 40%" |
| Debt service cover test | Debt covenants | 10-Q Q3 | S4 | page:51 "Consolidated income available for debt service / debt service 1.83x Minimum of 1.50x" | CP-1 covenants | Sourced | High | Indenture definition |
| Adjusted total assets | Debt covenants | 10-Q Q3 | S4 | page:51 "adjusted total assets for covenant purposes as defined in our senior notes indentures were $8,631,686" | CP-1 calculations | Sourced | High | Used in the cushion recomputation |
| December 31, 2025 tests | Debt covenants | 10-K FY2025 | S1 | page:138 "Total debt / adjusted total assets 58.7% Maximum of 60%" | CP-1 covenants | Sourced | High | Debt service cover 1.59x on the same page |
| Revolver covenant terms | Debt note | 10-K FY2025 | S1 | page:195 "change the required collateral property debt yield to 10%" | CP-1 covenants | Sourced | High | No reported ratio in any source |
| Unguaranteed unsecured notes | Supplemental guarantor information | 10-Q Q3 | S4 | page:53 "Our $1,225,000 of senior unsecured notes do not have the benefit of any guarantees." | CP-1 debt table | Sourced | High | Only the 2032 notes are guaranteed |
| TA share of rent | Net lease portfolio | 10-Q Q3 | S4 | page:56 "$ 269,547 68.2 %" | CP-1A operating model | Sourced | High | Excludes rents prepaid by TA |
| TA lease expiry | Lease expirations | 10-Q Q3 | S4 | page:58 "2033 203 5,338,721 274,609 69.4% 82.8%" | CP-1A operating model | Sourced | High | |
| BP guaranty cap | Note 6 | 10-Q Q3 | S4 | page:12 "limited to an aggregate cap which was $2,782,917" | CP-1A, CP-2 | Sourced | High | |
| Hotel revenue and expenses, Q3 2026 | Income statement | 10-Q Q3 | S4 | page:3 "Hotel operating revenues $ 298,379 $ 377,576 $ 883,025 $ 1,116,944" | CP-1A calculations | Sourced | High | Expense line 255,780 on the same page |
| Impairments | Income statement | 10-Q Q3 | S4 | page:3 "Loss on asset impairment 53,691 27,067 270,883 81,788" | CP-1, CP-2 | Sourced | High | |
| FY2025 revenue | Income statement | 10-K FY2025 | S1 | page:172 "Total revenues 1,814,838 1,896,928 1,873,863" | CP-1 EBITDA | Sourced | High | |
| FY2025 cash interest | Supplemental cash flow | 10-K FY2025 | S1 | page:174 "Cash paid for interest $ 379,566 $ 366,194 $ 314,323" | CP-1 cover | Sourced | High | |
| Nine-month cash interest | Supplemental cash flow | 10-Q Q3 | S4 | page:5 "Cash paid for interest $ 196,080 $ 239,155" | CP-1 cover | Sourced | High | |
| Equity offering proceeds | Liquidity | 10-Q Q3 | S4 | page:48 "Our net proceeds from this offering were approximately $541,798" | CP-1, CP-1A | Sourced | High | |
| RMR share purchase | Related persons | 10-Q Q3 | S4 | page:29 "purchased 8,333,333 common shares" | CP-1A governance | Sourced | High | |
| Sonesta share of investments | Hotel agreements | 10-Q Q3 | S4 | page:14 "comprised approximately 39.9% of our total historical real estate investments" | CP-1A, CP-2 | Sourced | High | |
| Retained hotel RevPAR | Hotel statistics | 10-Q Q3 | S4 | page:59 "$ 128.38 $ 118.53 8.3 %" | CP-1A | Sourced | Medium | Manager-reported, unverified by the company |
| Sonesta returns | Related persons | 10-Q Q3 | S4 | page:16 "$86,046 and $120,896" | CP-1A calculations | Sourced | High | Nine months 2026 and 2025 |
| Subsequent hotel sales | Liquidity | 10-Q Q3 | S4 | page:46 "combined sales price of $50,600" | CP-1, CP-2 | Sourced | High | After the quarter, to November 2, 2026 |
| Operating lease liabilities | Leases | 10-K FY2025 | S1 | page:191 "Present value of lease liabilities (1) $ 147,198" | CP-1 claims outside debt | Sourced | High | December 31, 2025 only |
| Carrying value of 2027 zero coupon notes | Fair value table | 10-Q Q3 | S4 | page:33 "Senior Secured Notes, due 2027 at zero coupon 533,897 542,636" | CP-1 maturity chart | Sourced | High | Principal at maturity 580,155 |
| Company reports no EBITDA | All filings | S1 to S4 | S1 to S4 | Searched each file for EBITDA; only EBITDAR rent coverage and a hotel incentive fee definition appear | CP-1 | Searched | High | Basis for the proxy |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Core EBITDA, FY2025 | CP-1, CP-2 | Revenues 1,814,838; hotel opex 1,226,542; net lease opex 21,597; G&A 40,667; transaction costs 14,698 | 1,814,838 - 1,226,542 - 21,597 - 40,667 - 14,698 | Calculated: 511,334, recomputed and agrees | Supported | Medium | Leverage, cover | S1 page:172 |
| LTM core EBITDA to Q3 2026 | CP-1, CP-2 | FY2025 511,334; nine months 2026 367,309; nine months 2025 403,001 | 511,334 + 367,309 - 403,001 | Calculated: 475,642, recomputed and agrees | Supported | Medium | Leverage, cover | S1, S4 page:3 |
| Gross leverage, LTM Q3 2026 | CP-1, CP-2 | 4,652,322 and 475,642 | 4,652,322 / 475,642 | Calculated: 9.78x, agrees | Supported | Medium | Leverage | S4 |
| Net leverage, LTM Q3 2026 | CP-1, CP-2 | 4,652,322, 40,118 and 475,642 | (4,652,322 - 40,118) / 475,642 | Calculated: 9.70x, agrees | Supported | Medium | Leverage | S4 |
| LTM cash interest | CP-1, CP-2 | 379,566; 196,080; 239,155 | 379,566 + 196,080 - 239,155 | Calculated: 336,491, agrees | Supported | High | Cover | S1, S4 |
| Cash interest cover | CP-1, CP-2 | 475,642 and 336,491 | 475,642 / 336,491 | Calculated: 1.41x, agrees | Supported | Medium | Cover | S4 |
| Liquidity | CP-1, CP-2 | 40,118 and 650,000 | 40,118 + 650,000 | Calculated: 690,118, agrees | Supported | High | Liquidity | S4 |
| Debt reduction | CP-1, CP-2 | 5,504,809 and 4,652,322 | 5,504,809 - 4,652,322 | Calculated: 852,487, agrees | Supported | High | Deleveraging | S1 page:198, S4 page:49 |
| Secured share, September 30, 2026 | CP-1A, CP-2 | 1,580,155 and 1,347,167 over 4,652,322 | 2,927,322 / 4,652,322 | Calculated: 62.9%, agrees | Supported | High | Subordination | S4 page:20 |
| Secured share, December 31, 2025 | CP-1A, CP-2 | 1,580,155, 604,654 and 45,000 over 5,504,809 | 2,229,809 / 5,504,809 | Calculated: 40.5%, agrees | Supported | High | Subordination | S1 page:194, page:197 |
| Hotel share of Q3 2026 revenue | CP-1A, CP-2 | 298,379 and 399,520 | 298,379 / 399,520 | Calculated: 74.7%, agrees | Supported | High | Revenue mix | S4 page:3 |
| Hotel expense ratio, Q3 2026 | CP-1A, CP-2 | 255,780 and 298,379 | 255,780 / 298,379 | Calculated: 85.7%, agrees | Supported | High | Margin | S4 page:3 |
| Adjusted assets cushion on the 60% test | CP-2 | Debt 4,652,322; adjusted assets 8,631,686 | 1 - (4,652,322 / 0.60) / 8,631,686 | Calculated: 10.2%, agrees | Supported | High | Covenant headroom | S4 page:51 |
| Debt service cover cushion | CP-2 | 1.83x and 1.50x | (1.83 - 1.50) / 1.83 | Calculated: 18.0%, agrees | Supported | High | Covenant headroom | S4 page:51 |
| Average coupon | CP-1, CP-2 | 263,082 and 4,652,322 | 263,082 / 4,652,322 | Calculated: 5.65%, agrees | Supported | High | Cost of debt | S4 page:62 |
| Maturities to the end of 2028 | CP-2 | 584,150 and 1,002,775 | 584,150 + 1,002,775 | Calculated: 1,586,925, agrees | Supported | High | Refinancing | S4 page:49 |
| EBITDA definition assumption | CP-1, CP-2 | Revenues less hotel opex, net lease opex, G&A and transaction costs | Not an issuer or covenant definition | Assumption-Based | Supported as a labelled proxy | Medium | Leverage, cover | CP-1 Calculations |

### Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Debt service cover is the tighter indenture test (CP-1 and CP-2 reader summaries) | The cushions do not support it. At September 30, 2026 adjusted assets could fall 10.2% before the 60% total debt test is reached, while debt service income could fall 18.0% before the 1.50x test. At December 31, 2025 the asset test was also tighter (58.7% against 60%, a cushion of about 2.2%, against 1.59x against 1.50x, about 5.7%). Debt service cover is the more earnings-sensitive test because hotel sales cut income, but it is not the tighter one | Calculated, with a wrong comparative statement | The reader would focus monitoring on the wrong test | Say the total debt to adjusted assets test has the smaller cushion and debt service cover is the more earnings-sensitive; this review is the correction | CP-1 reader summary third finding; CP-2 reader summary fourth finding |
| Minor | Maturity years are described by instrument, for example the 2028 year as the 3.95% notes plus a net lease mortgage note balloon | The yearly totals are printed; the instrument composition of each year is matched from the fixed-rate table and is not printed by year | Analyst Inference | The totals are reliable; the composition could be wrong if amortisation dates differ | Label the composition as inferred | CP-1 debt maturities chart basis cells |
| Minor | All debt is fixed rate, so interest cost is not exposed to rates in the near term (CP-2 strengths) | The statement holds for current principal. The revolver, which would be floating, is undrawn but expires June 29, 2027, and any refinancing would be at market rates | Analyst Inference | Overstates insulation from rate risk at refinancing | Qualify as exposure on current principal only | CP-2 strengths and weaknesses |
| Minor | The revolver covenant levels were not supplied (CP-0 gap) | The 10-K prints them; CP-1 already corrected this. No reported ratio exists in any source | Directly Sourced | Closes a CP-0 statement; headroom is still Not calculable | None beyond the CP-1 correction | CP-0 gaps |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation: four filings and three announcements, but no credit agreement, indentures, tenant financials or ratings | Source register | Ranking, covenant and tenant statements cannot be tested against primary documents | Headline view stands; legal and tenant claims are interpretations | Obtain the missing documents |
| Citation completeness | Committee-Ready: every figure has a file and page, and all quotes in the earlier handoffs matched their pages in this review | Lineage register | A claim without a page cannot be audited | Supports reliance on the headline view | None beyond the flags above |
| Calculation traceability | Committee-Ready: all ratios recompute from cited inputs | Calculation register | Wrong derived figures would mislead leverage and cover | Headline ratios stand | Label the EBITDA proxy wherever the ratios are quoted |
| Assumption transparency | Ready with Remediation: the EBITDA proxy is labelled, but later summaries drop the label in places | CP-1 Calculations; CP-2 text | Readers could take the proxy for a reported measure | Leverage could be over-read | Keep the label in any delivery |
| Markdown and export artifact integrity | Committee-Ready: headings, sources, hashes and selectors are present in the four handoffs | Handoff structure | A broken envelope blocks delivery | None | None |
| Contrary evidence | Strongest counter to the weak-credit view: indenture compliance with cushions of 10.2% and 18.0%, deleveraging of 852,487 and 97.6% occupied rent. It would win if hotel sales proceeds retire debt faster than EBITDA falls and the revolver is extended on similar terms | S4 page:51, page:20, page:55 | If it wins, the high leverage is transitional | Credit view would improve on a completed refinancing | Monitor the revolver outcome and the next two quarters' EBITDA |
| Downside logic | Initiating condition: refinancing market closes or TA payment stress. First break: revolver not extended before June 29, 2027. Transmission: loss of the only committed liquidity while 584,150 matures in 2027. Consequence: reliance on asset sales or secured debt. Observable trigger: no extension agreement by mid-2027, a fall in TA rent coverage, or a covenant ratio disclosure near its limit | S4 page:20, page:47, page:49, page:57 | A liquidity squeeze precedes any covenant breach | Refinancing is the key monitoring item | Track extension news and rent coverage |

### Cross-module consistency

The four handoffs tell one story with one exception. All use the same period labels (FY2025, Q1 to Q3 2026, nine months, LTM to Q3 2026), the same principal debt of 4,652,322, cash of 40,118, undrawn revolver of 650,000, LTM core EBITDA of 475,642 and ratios of 9.78x, 9.70x and 1.41x, and the same secured shares of 62.9% and 40.5%. The credit synthesis repeats the financial base and business context figures exactly. CP-1 corrected CP-0 on the revolver covenant terms and its correction is confirmed. The exception is the statement that debt service cover is the tighter test, repeated in CP-1 and CP-2 and corrected above. A definitional difference is recorded rather than resolved: the proxy EBITDA is not the indenture's income available for debt service, and the reported 1.83x test is not comparable with the 1.41x cover.

### Issue log and clearance

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | Material | CP-1, CP-2 | Direction error | Debt service cover called the tighter test; the asset test has the smaller cushion | Use the corrected statement | Restricts covenant statements | Open: corrected here |
| E2 | Minor | CP-1 | Inference stated as fact | Instrument composition of maturity years | Label as inferred | None | Open: corrected here |
| E3 | Minor | CP-2 | Overstatement | Rate insulation from fixed-rate debt | Qualify to current principal | None | Open: corrected here |
| E4 | Material | All | Evidence gap | Credit agreement, indentures, revolver ratios, tenant financials, ratings, proxy | Obtain documents | Restricts legal capacity, ranking and headroom statements | Open |
| E5 | Material | CP-1, CP-2 | Definition | EBITDA is an analyst proxy including sold hotels | Keep the label; obtain retained-asset earnings | Restricts leverage and cover statements to the proxy basis | Open |
| E6 | Minor | CP-0 | Superseded statement | Revolver covenant levels listed as not supplied | Already corrected in CP-1 | None | Closed |

Research QA status: Restricted. Committee status: Restricted use. The headline credit view on liquidity, debt, maturities, tenant concentration and covenant tests is supported and may be used; statements that debt service cover is the tighter test, on covenant headroom for the revolver, on forward leverage of the retained portfolio and on ranking beyond the printed debt table may not be used without the stated qualification. The confidence band is Medium.

## Calculations

Independent recomputation from the cited inputs, in USD thousands unless stated. Every result agrees with the upstream value except where stated.

| Check | Inputs | Result |
| --- | --- | --- |
| Principal debt at September 30, 2026 | 1,725,000 + 1,580,155 + 1,347,167 | 4,652,322, agrees |
| Principal debt at December 31, 2025 | 3,275,000 + 1,580,155 + 604,654 + 45,000 | 5,504,809, agrees |
| Principal debt at March 31, 2026 | 2,275,000 + 1,580,155 + 1,349,164 + 45,000 | 5,249,319, agrees |
| Principal debt at June 30, 2026 | 25,000 + 1,725,000 + 1,580,155 + 1,348,166 + 45,000 | 4,723,321, agrees |
| Fixed-rate table total | 580,155 + 400,000 + 603,186 + 425,000 + 400,000 + 743,981 + 1,000,000 + 500,000 | 4,652,322, agrees |
| Core EBITDA, nine months 2026 | 1,184,945 - 763,078 - 19,875 - 29,854 - 4,829 | 367,309, agrees |
| Core EBITDA, nine months 2025 | 1,417,385 - 963,111 - 16,303 - 30,831 - 4,139 | 403,001, agrees |
| Core EBITDA, quarters | 103,062 + 138,718 + 125,529 | 367,309, agrees to nine months |
| LTM core EBITDA | 511,334 + 367,309 - 403,001 | 475,642, agrees |
| Gross leverage | 4,652,322 / 475,642 | 9.781x, agrees at 9.78x |
| Net leverage | 4,612,204 / 475,642 | 9.696x, agrees at 9.70x |
| LTM cash interest | 379,566 + 196,080 - 239,155 | 336,491, agrees |
| Cash interest cover | 475,642 / 336,491 | 1.413x, agrees at 1.41x |
| FY2025 leverage and cover | 5,504,809 / 511,334; 511,334 / 379,566 | 10.766x and 1.347x, agree at 10.77x and 1.35x |
| Liquidity | 40,118 + 650,000 | 690,118, agrees |
| Cushion on the 60% total debt test | 1 - (4,652,322 / 0.60) / 8,631,686 = 1 - 7,753,870 / 8,631,686 | 10.2%, agrees |
| Cushion on the 40% secured test | 1 - (2,927,322 / 0.40) / 8,631,686 = 1 - 7,318,305 / 8,631,686 | 15.2%, agrees |
| Cushion on the 1.50x test | (1.83 - 1.50) / 1.83 | 18.0%, agrees |
| December 31, 2025 cushions | (60 - 58.7) / 60; (1.59 - 1.50) / 1.59 | 2.2% on assets and 5.7% on debt service cover; the asset test was also tighter then |
| Indenture ratio check | 4,652,322 / 8,631,686; 4,712,742 / 1,725,000 | 53.9% and 273.2%, agree to the reported tests |
| Secured share | 2,927,322 / 4,652,322; 2,229,809 / 5,504,809 | 62.9% and 40.5%, agree |
| Hotel share and expense ratio | 298,379 / 399,520; 255,780 / 298,379 | 74.7% and 85.7%, agree |
| TA share of rent | 269,547 / 395,492 | 68.2%, agrees |
| Maturities to the end of 2028 | 584,150 + 1,002,775 | 1,586,925, agrees |
| Average coupon | 263,082 / 4,652,322 | 5.65%, agrees |
| LTM operating cash flow less improvements | (117,808 + 132,226 - 136,305) - (224,833 + 110,062 - 148,154) | 113,729 - 186,741 = -73,012, agrees |

## Gaps

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Revolver covenant ratios and credit agreement absent | Reported fixed charge coverage and debt yield; credit agreement and amendments | The revolver supplies nearly all liquidity and its availability is conditional | Headroom Not calculable; refinancing view is interpretation | Confidence capped at Medium | Credit agreement and compliance certificates |
| CP-5-GAP-002 | Indentures absent | Definitions of adjusted total assets and income available for debt service; collateral and guarantors of the 8.625% notes due 2031; maturity month of the 2027 zero coupon notes | Ranking, covenant definitions and 2027 timing cannot be tested | Ranking statements beyond the printed tables are interpretations | Lower for ranking claims | Indentures filed as exhibits |
| CP-5-GAP-003 | No issuer EBITDA | Company-defined EBITDA or retained-asset earnings | Leverage and cover rest on a proxy that includes sold hotels | Forward leverage uncertain | Confidence capped at Medium | Company disclosure |
| CP-5-GAP-004 | Tenant financials and guaranty terms absent | TravelCenters of America statements; BP guaranty beyond the cap | The largest rent source cannot be independently tested | Rent durability is tenant-reported | Lower for rent claims | Tenant filings and the guaranty |
| CP-5-GAP-005 | Ratings, market data and ownership beyond two holders near 6% absent | Agency reports, market capitalisation, proxy statement | No agency view or market cross-check; sponsor alignment untested | Insufficient Information, not adverse | Lower | Agency reports, proxy statement |
| CP-5-GAP-006 | Investor presentation and earnings release content absent | The Q3 2026 presentation and results document | Management guidance and any pro forma retained-hotel earnings unavailable | Management Language cannot be added | No further reduction | Company website |
| CP-5-GAP-007 | Text extraction only | Layout check of original tables, including the Schedule III heading in millions against notes in thousands | Cell-order errors are possible though totals tie | Figures cross-checked to totals | No further reduction | Original filings |

## Next module

This is the last selected module. Delivery should present the credit view with the corrections above applied: describe the total debt to adjusted assets test, not debt service cover, as the one with the smaller cushion, label the maturity-year composition as inferred, qualify the fixed-rate insulation to current principal, keep the EBITDA proxy label on every leverage and cover figure, and keep committee use Restricted until the revolver covenant ratios, the credit agreement and indentures, tenant financials and ratings are obtained.
