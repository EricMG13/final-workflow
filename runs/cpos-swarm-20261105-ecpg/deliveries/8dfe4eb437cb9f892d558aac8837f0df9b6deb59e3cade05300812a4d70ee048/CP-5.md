## Request

Evidence trace and research-integrity review for ENCORE CAPITAL GROUP INC as of 2026-11-05 (pathway credit_snapshot, cutoff 2026-11-05, reporting currency USD), covering the four upstream handoffs: source readiness, financial base, business and transaction view, and fundamental credit synthesis. Scope is the Top 5 material credit drivers plus a statement-level lineage sample; this review changes no upstream conclusion and repairs no lineage silently.

## Sources

### Issuer sources traced

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_ecpg-20251231.htm.jsonl | 34ff88efcf361fa9aeafcc136a26a65107894a6eccc6d81525528ab9ff5d0d5d |
| 10-Q_2026-03-31_ecpg-20260331.htm.jsonl | 78afd13c000763f54a4aba736b73215614c4d9f919d4b8b0b086fe99e4f165ec |
| 10-Q_2026-06-30_ecpg-20260630.htm.jsonl | b9101ef4153230b6bac0c232b19beeb72b0be52512669a3b5f826ec55ac35d2f |
| 10-Q_2026-09-30_ecpg-20260930.htm.jsonl | 732e46e0fdf56804d0e4376f251fca05b1fb9b8a2542ea7489a917605ffcd2f2 |
| EX-99.1_2026-05-06_exhibit991ecpgq12026earnin.htm.jsonl | 52e6f2f8497b4c376deb09345bbca84227e91bc87999210c914e4332ca310a30 |
| EX-99.1_2026-08-05_exhibit991ecpgq22026earnin.htm.jsonl | c912421ecebbdeab115865e4c75e4397e60fc06977b32c09b5fe72e8026c1bc7 |
| EX-99.1_2026-11-04_exhibit991ecpgq32026earnin.htm.jsonl | 55d38b7d96066eb32a5cc33bf9d08102e9a0e050298f0028532e13cfed8c82ea |

The context file (sha256 fb9232dcd1631add7bbcdb6eec1a7bd4a0eec6466deb6a3148ebd7ee287099b7) holds run settings only and is not issuer evidence.

### Handoffs reviewed

| Module | sha256 |
| --- | --- |
| CP-0 | 5bceebdd4466b332506213f28eb141aebd7b80ad1c46615c0f3d948e9eb94d38 |
| CP-1 | ab3610ee01f0fa09c54f50e64a0bffd5255ff6bf09c099588a370bee5b40463a |
| CP-1A | 5dbcb538d13bbcbc9dec75ccc4fa14160823a451153ddae0cc3fd648d434d139 |
| CP-2 | 14da30495810a0652765d826ccb464cdf78439fe5a65273604fbc679fb5768a0 |

Locators are retained `page:N` spans of the source text. Method of review: every quotation in the financial base and business handoffs was located on its cited page; each ratio and last twelve months figure was recomputed from figures read directly from the source text, not from the handoffs; each handoff was compared with the others for figure identity.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is traceable: every sampled figure and quotation resolves to a cited page, and recomputed ratios match. Committee use is restricted for covenant headroom, legal ranking and market views, which have no source support. | Medium | No executed financing agreements, reported covenant ratios or ratings exist in the sources, so those items cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 84 quotations checked in the financial base and business handoffs were found on the cited page. | The cited facts can be relied on as filed statements. | High |
| Recomputing 15 ratios from the sources reproduced the leverage and cover figures in the financial base exactly. | The leverage and interest cover series are reproducible. | High |
| Covenant headroom cannot be traced because only limits and a compliance statement are printed. | Headroom for the tests that protect creditors is a gap. | High |
| Share repurchases and portfolio purchases each appear on two printed definitions across the handoffs. | The differences are definitional and logged, not reconciled. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 3 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of reported covenant ratios and executed financing agreements, which matters because covenant headroom, restricted payment capacity and ranking on shared collateral cannot be tested from the sources and implies that covenant-dependent conclusions are restricted in committee use. Committee status is Restricted: the leverage, interest cover, liquidity, maturity and operating model conclusions are traceable to filed statements, while management statements such as guidance and market commentary stay attributed as Management Language.

### Traceability summary

| Check | Result | Count | Severity | Status |
| --- | --- | --- | --- | --- |
| Quotations found on cited page | All found | 84 | None | Clear |
| Ratios recomputed from sources | All reproduced | 15 | None | Clear |
| Cross-module figure identity | No conflicts | 11 figures | Minor | Clear |
| Definition differences logged | Two logged | 2 | Minor | Remediation noted |
| Covenant headroom traceability | Not traceable | 1 | Material | Restricted |

### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_ecpg-20251231.htm.jsonl | Filed audited annual report, high | FY2025 and FY2024 comparatives | Encore Capital Group, Inc. consolidated | Statements, Adjusted EBITDA, borrowings, contractual obligations, business, legal | Exhibits not retained; no year-end 2024 total ERC table | Financial base, business view |
| S2 | 10-Q_2026-03-31_ecpg-20260331.htm.jsonl | Filed unaudited quarterly report, high | Q1 2026 | Same consolidated entity | Statements, Adjusted EBITDA, borrowings, capacity | Unaudited | Last twelve months build |
| S3 | 10-Q_2026-06-30_ecpg-20260630.htm.jsonl | Filed unaudited quarterly report, high | Q2 2026 and six months | Same | Statements, Adjusted EBITDA, borrowings, capacity | Six month column is year to date | Last twelve months build |
| S4 | 10-Q_2026-09-30_ecpg-20260930.htm.jsonl | Filed unaudited quarterly report, high | Q3 2026 and nine months | Same | Controlling debt, liquidity, commitments, hedging, legal | No contractual obligations table; no covenant ratios | All modules |
| S5 | EX-99.1_2026-05-06_exhibit991ecpgq12026earnin.htm.jsonl | Management release, medium | Q1 2026 | Same | Collections, ERC, reproduced statements | Attributed management claims | Supporting only |
| S6 | EX-99.1_2026-08-05_exhibit991ecpgq22026earnin.htm.jsonl | Management release, medium | Q2 2026 | Same | Collections, ERC, guidance, refinancing cost remark | Attributed management claims | Supporting only |
| S7 | EX-99.1_2026-11-04_exhibit991ecpgq32026earnin.htm.jsonl | Management release, medium | Q3 2026 | Same | Collections, ERC, Adjusted EBITDA, guidance | Attributed management claims | Supporting only |
| H0 | CP-0 handoff | Accepted upstream handoff, high | As of 2026-11-05 | Source set | Readiness and gaps | Source sufficiency only | Gap carry-forward |
| H1 | CP-1 handoff | Accepted upstream handoff, high | FY2024 to Q3 2026 | Consolidated | Financial series | Company-defined Adjusted EBITDA | Credit synthesis |
| H2 | CP-1A handoff | Accepted upstream handoff, high | FY2025 to October 2026 events | Consolidated | Business and transaction facts | Management language attributed | Credit synthesis |
| H3 | CP-2 handoff | Accepted upstream handoff, high | As of 2026-11-05 | Consolidated | Credit view | Built on H1 and H2 only | Committee |

### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage fell from 5.96x at FY2025 to 5.13x on a last twelve months basis at Q3 2026 | CP-1 | Principal debt 4,267,981 thousand over last twelve months Adjusted EBITDA 831,829 thousand | Sets debt service capacity and leverage tolerance | Core to default risk view | S4 page:19; S4 page:51; S1 page:62; S1 page:105 | Company-defined EBITDA, consolidated perimeter |
| 2 | Revolver availability fell from 814.3 to 510.2 US$m | CP-1 | Issuer-stated availability after covenants | Revolver funds purchases, refinancing and repurchases | Liquidity cushion | S4 page:20; S1 page:107 | Letters of credit and covenant headroom unmeasured |
| 3 | Adjusted EBITDA includes forecast-driven revenue | CP-1, CP-1A | Changes in recoveries 244,898 thousand of nine month Adjusted EBITDA 644,320 thousand | Revenue reversal would cut EBITDA while debt stays | Earnings quality | S4 page:3; S4 page:5; S4 page:51 | Forecast reliability not independently testable |
| 4 | 2029 maturity concentration: revolver and U.S. facility | CP-1 | Revolver 974.8 and U.S. facility 450.0 US$m both mature in 2029 | Single renewal event | Refinancing risk | S4 page:19; S4 page:20; S4 page:25 | Revolver tranche split for 2028 not supplied |
| 5 | Business risk: pricing, forecasts, legal channel, seller concentration | CP-1A, CP-2 | Operating model facts and legal cost trend | Drives collections and cost | Business risk view | S4 page:36; S4 page:47; S1 page:98 | Seller shares not disclosed |

### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 5.13x last twelve months | CP-1, CP-2 | Principal debt "4,267,981 4,033,394" (S4 page:19) and Adjusted EBITDA "Adjusted EBITDA $ 245,171 $ 184,756 $ 644,320 $ 489,449" (S4 page:51) | Yes | High | Calculated | Reproduced | High | Committee-Ready |
| Revolver availability 510.2 US$m | CP-1, CP-2 | "was approximately $510.2 million as of September" (S4 page:20) | Yes | High | Directly Sourced | Verified | High | Committee-Ready |
| Forecast-driven revenue share of Adjusted EBITDA | CP-1, CP-2 | "Changes in recoveries 111,043 63,636 244,898 140,699" (S4 page:3) | Yes | High | Calculated | Reproduced | High | Committee-Ready |
| 2029 maturity concentration | CP-1, CP-2 | "matures in September 2029" (S4 page:20) and "to extend its maturity from October 2028 to October 2029" (S4 page:25) | Yes | High | Calculated | Reproduced | High | Committee-Ready |
| Business risk reading | CP-1A, CP-2 | "Total cost of legal collections $ 286,220 $ 227,672 $ 58,548 25.7 %" (S4 page:47) | Yes | High | Analyst Inference | Interpretation of filed facts | Medium | Committee-Ready |
| Covenant headroom | CP-1, CP-2 | "A restrictive covenant that requires the Company to maintain a Fixed Charge Coverage Ratio" (S4 page:20), no reported ratio | Partial | Medium | Insufficient Information | Gap, not an adverse conclusion | Low | Remediation Needed |

### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt at 2026-09-30 is 4,267,981 thousand | pack folder 1084961-encore-capital-group-inc-ecpg | 10-Q_2026-09-30_ecpg-20260930.htm.jsonl | S4 | page:19, Note 7 | CP-1 leverage chart | Sourced | High | Matches stated components; discount and costs 30,181 give carrying 4,237,800 |
| Cash at 2026-09-30 is 158,425 thousand | same | 10-Q_2026-09-30_ecpg-20260930.htm.jsonl | S4 | page:2, statement of financial condition | CP-1 liquidity chart | Sourced | High | Includes vehicle and client cash, flagged in CP-1 |
| Last twelve months Adjusted EBITDA 831,829 thousand | same | 10-K and Q3 10-Q | S1, S4 | S1 page:62; S4 page:51 | CP-1 leverage chart | Calculated | High | 676,958 + 644,320 − 489,449 |
| Last twelve months cash interest 270,515 thousand | same | 10-K and Q3 10-Q | S1, S4 | S1 page:89; S4 page:6 | CP-1 interest cover chart | Calculated | High | 259,812 + 183,459 − 172,756 |
| Revolver availability 510.2 US$m and commitment 1,485.0 US$m | same | Q3 10-Q | S4 | page:20, Note 7 | CP-1 liquidity chart | Sourced | High | Availability equals commitment less drawn |
| Convertible notes settled 2026-09-24 for 367.9 US$m from revolver borrowings | same | Q3 10-Q | S4 | page:24, Note 7 | CP-1 events; CP-1A transaction summary; CP-2 | Sourced | High | Spread charged to equity |
| 2032 notes 750.0 US$m at 6.625% issued 2026-05-22 | same | Q3 10-Q | S4 | page:22, Note 7 | CP-1A transaction summary | Sourced | High | Loss on extinguishment 28.0 US$m |
| Forward flow minimum commitment 684.5 US$m | same | Q3 10-Q | S4 | page:30, Note 11 | CP-1A operating model | Sourced | High | Termination rights stated |
| Seller concentration not disclosed | same | 10-K | S1 | page:98, Note 1 | CP-1A operating model | Sourced | High | Absence of percentages is itself the finding |
| Cost of legal collections up 25.7% for nine months | same | Q3 10-Q | S4 | page:47, MD&A | CP-1A operating model | Sourced | High | Attributed to US legal placements |
| CFPB Stipulated Judgment expired October 2025 | same | 10-K | S1 | page:34, Item 1A | CP-1A profile | Sourced | High | History at issuer level |
| Share repurchases 73.4 US$m under program, 73,993 thousand in cash flow | same | Q3 10-Q | S4 | page:58 and page:5 | CP-1A governance; CP-1 | Sourced | High | Two printed definitions, see T5.6 |
| 2026 guidance raised | same | Q3 release | S7 | page:1 | CP-1A operating model | Sourced | Medium | Management forward-looking claim |
| 19 holders of record; no sponsor named | same | 10-K and context | S1 | page:45 | CP-1A profile | Sourced | High | Ownership above record holders not supplied |

### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last twelve months Adjusted EBITDA Q3 2026 | CP-1, CP-2 | 676,958; 644,320; 489,449 thousand | FY2025 + nine months 2026 − nine months 2025 = 831,829 | Reproduced | Calculated | High | Leverage denominator | S1 page:62; S4 page:51 |
| Last twelve months cash interest Q3 2026 | CP-1, CP-2 | 259,812; 183,459; 172,756 thousand | FY2025 + nine months 2026 − nine months 2025 = 270,515 | Reproduced | Calculated | High | Cover denominator | S1 page:89; S4 page:6 |
| Total debt over Adjusted EBITDA | CP-1, CP-2 | 4,267,981 and 831,829 thousand | 4,267,981 / 831,829 = 5.13x | Reproduced | Calculated | High | Leverage | S4 page:19 |
| Net debt over Adjusted EBITDA | CP-1, CP-2 | 4,267,981 − 158,425 = 4,109,556 thousand | 4,109,556 / 831,829 = 4.94x | Reproduced | Calculated | High | Net leverage | S4 page:2; S4 page:19 |
| Adjusted EBITDA over cash interest | CP-1, CP-2 | 831,829 and 270,515 thousand | 831,829 / 270,515 = 3.07x | Reproduced | Calculated | High | Cover | S1; S4 |
| Share of Adjusted EBITDA from changes in recoveries | CP-1, CP-2 | 244,898 and 644,320 thousand | 244,898 / 644,320 = 38.0% | Reproduced | Calculated | High | Earnings quality | S4 page:3; S4 page:51 |
| Revolver utilisation | CP-1, CP-2 | 974.763 and 1,485.0 US$m | 974.763 / 1,485.0 = 65.6% | Reproduced | Calculated | High | Liquidity, covenant trigger above 20% | S4 page:19; S4 page:20 |
| 2029 maturities | CP-1, CP-2 | 974.763 and 450.000 US$m | Sum = 1,424.763 US$m | Reproduced | Calculated | High | Refinancing concentration | S4 page:19 |
| Maturity total check | CP-1 | Seven maturity buckets | Sum = 4,267.981 US$m equals printed total | Reproduced | Calculated | High | Completeness of the schedule | S4 page:19; S4 page:21 |
| No assumptions or forward estimates are used by any upstream module | all | Not applicable as an input; guidance is cited as Management Language only | None | Verified | Directly Sourced | High | No assumption risk | S7 page:1 |

### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | Covenant compliance and headroom | Only limits and a compliance statement are cited; no reported ratio | Insufficient Information | Headroom against the tests that protect creditors is untraceable | Obtain compliance certificate and agreement definitions | CP-1 gap; CP-2 gap ledger |
| MINOR | Total ERC cell for FY2024 in the financial table | The cell reads Not supplied with the reason "not read"; the pinned sources do not print a year-end 2024 total ERC, so the reason should read not printed in the pinned sources | Insufficient Information | Wording only; no figure is affected | State the corrected reason here; no change to figures | CP-1 financial table |
| MINOR | Revolver availability at FY2025 and Q1 2026 | Commitment less drawn exceeds stated availability by 38.7 and 12.4 US$m, unexplained in the sources | Insufficient Information | True cushion at those dates uncertain | Obtain facility utilisation detail | CP-1 liquidity chart |
| MINOR | Management statements | Guidance, supply and pricing commentary are carried as Management Language and not adopted | Directly Sourced | Attribution check passed | None | CP-1A, CP-2 |

### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Citation resolvability | Strong | 84 quotations located on their cited pages | A misquote would misstate debt or liquidity | Facts can be relied on | None |
| Calculation reproducibility | Strong | 15 ratios and the last twelve months builds recomputed from source figures | An arithmetic error would shift leverage | Leverage and cover are reproducible | None |
| Cross-module consistency | Strong with two logged definition differences | Figures identical across modules for debt, EBITDA, liquidity, maturities | Mixed definitions could mislead | No conflict, two differences logged | Keep both definitions visible |
| Legal and covenant traceability | Weak | No executed agreement; note summaries only | Cannot test restricted payments or ranking | Covenant and legal ranking views are restricted | Obtain executed documents |
| Management language control | Adequate | Guidance and market commentary labelled as Management Language | Promotional text could be adopted as fact | Attribution held | None |
| Market data traceability | Not applicable to the conclusions drawn | No ratings, prices or relative value claims were made upstream | Market claims would be untraceable | No market-based conclusion should be drawn | Supply ratings and prices if needed |

### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant ratios not reported | Compliance certificate | Headroom unmeasurable | Liquidity and default risk views restricted | Caps confidence at Medium | Credit agreement and certificate |
| G2 | Executed agreements not supplied | Credit agreement, indentures, intercreditor | Legal capacity and ranking unverified | Governance and creditor control views restricted | Caps confidence at Medium | Executed documents |
| G3 | Seller concentration not disclosed | Top-seller shares | Supply risk cannot be sized | Business risk bounded | Medium | Issuer data |
| G4 | Ratings, prices, target leverage not supplied | Agency reports, market data | Market-implied view unavailable | No market conclusion | Medium | Rating agencies, market data |
| G5 | Letters of credit and unexplained availability difference | Facility utilisation detail | Liquidity cushion at FY2025 and Q1 2026 | Minor | Low effect | Issuer |
| G6 | Ownership above record holders and related parties | Proxy statement | Control and leakage unassessed | Governance bounded | Low effect | Proxy |

### T5.1 Module inventory

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | CP-0 response, run ecpg-2026-11-05-credit_snapshot-host | Source readiness for seven sources | High | Six H2 headings present | Accepted by CP-OS | Readiness READY_WITH_LIMITATIONS |
| CP-1 | CP-1 response, same run | Financial base FY2024 to Q3 2026 | High | Six H2 headings and four chart selectors present | Accepted by CP-OS | Quotations and ratios verified here |
| CP-1A | CP-1A response, same run | Business and transaction view | High | Six H2 headings and three selectors present | Accepted by CP-OS | Quotations verified here |
| CP-2 | CP-2 response, same run | Credit synthesis from upstream only | High | Six H2 headings and selectors present | Accepted by CP-OS | Figures identical to CP-1 |

### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Financial table, total ERC for FY2024 | Cell reason inaccurate | Reason given as not read; sources do not print the figure | Corrected here; wording only | Clear with remediation noted |
| MINOR | CP-1A | Operating model, revenue recognition row | Supported | Management conclusion on timing is quoted and labelled Management Language | None | Clear |
| MINOR | CP-2 | Key findings 1 to 7 | Supported by upstream references | No source text quoted, as the method requires | None | Clear |

### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Leverage on company-defined Adjusted EBITDA | Includes forecast-driven revenue; excludes portfolio purchases | None | Keep definition risk visible in committee material | Clear |
| MINOR | CP-1 | FY2024 ratios | FY2024 Adjusted EBITDA adds back impairments and carries negative changes in recoveries | None | Do not compare FY2024 like for like | Clear |
| MINOR | CP-1 | Debt basis | Principal used for ratios; carrying amount shown | None | Keep both visible | Clear |

### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | The revolver ranks ahead of the senior secured notes on enforcement of shared collateral | Executed intercreditor agreement | Only the issuer's note summary is available | Obtain the agreement before relying on ranking | Counsel review before any legal reliance |
| MATERIAL | CP-1, CP-1A | Covenant limits of 0.75, 0.275 and 2.0 | Executed credit agreement with definitions | Definitions and reported ratios are absent | Obtain agreement and certificate | Counsel review of definitions |

### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | No relative value, ranking or market claim is made, as the method prohibits | Ratings, prices, spreads | None needed for the claims made | Supply market data only if a later module needs it | No market-based conclusion should be drawn from this run |

### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Share repurchases appear as 73,993 thousand in the nine month cash flow (S4 page:5) and 73.4 US$m under the program (S4 page:58); for 2025, 90,402 thousand in cash flow and 89.5 US$m under the program | None | Keep both and name the basis; not reconciled | Capital allocation narrative uses the program figure; cash flow uses the statement figure |
| MINOR | CP-1, CP-1A | Nine month 2026 purchases 1,196,311 thousand by geography (S4 page:37) against 1,187,072 thousand net of put-backs in cash flow (S4 page:5) | None | Logged in CP-1A, not reconciled | Cash flow figure used in the financial table |
| MINOR | CP-1, CP-2 | The 2029 maturity amount is written 1424.8 in the chart table and USD 1424.8 million in the synthesis | None | Same value; formatting only | None |
| MINOR | CP-1, CP-1A | The 10-K describes several operating segments and the Q3 10-Q one reportable segment | 10-K and 10-Q presentation | Both state one reportable segment | None |

### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Duplication | Leverage, liquidity and maturity messages repeat across the reader summaries, views and findings | None needed; each repeats the same figures | No contradiction |
| MINOR | CP-2 | Materiality | The synthesis ranks business risk and financial risk in proportion to the upstream evidence | None | Appropriate |
| MATERIAL | CP-1, CP-2 | Committee readiness | Covenant headroom and legal ranking are not traceable | Obtain executed documents and certificate | Restricted use for those conclusions |

### T5.8 Handoff structure and export audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Six H2 headings, sources with sha256, handoff hashes | None found | None | Chain of hashes intact |
| MINOR | CP-1 | Chart selector tables | Each of the four chart tables is single and populated | None | Usable for report charts |
| MINOR | CP-1A | Selector tables and prose section | Two single tables and one prose section | None | Usable |

### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I1 | MATERIAL | CP-1, CP-2 | Missing evidence | Covenant ratios and executed agreements not supplied | Obtain compliance certificate and agreements | Restricts covenant and legal conclusions | Open |
| I2 | MINOR | CP-1 | Wording | FY2024 total ERC reason stated as not read; not printed in the pinned sources | Corrected in this handoff; the accepted handoff cannot be edited | None | Corrected here |
| I3 | MINOR | CP-1, CP-1A, CP-2 | Definition | Two printed bases for share repurchases | Name the basis when quoting | None | Open, logged |
| I4 | MINOR | CP-1, CP-1A | Definition | Two printed bases for nine month purchases | Name the basis when quoting | None | Open, logged |
| I5 | MINOR | CP-1 | Missing evidence | Availability difference at FY2025 and Q1 2026 unexplained | Obtain facility detail | None | Open |

## Calculations

Independent recomputation from the source text, in US$ thousands unless stated. Last twelve months Adjusted EBITDA: Q1 676,958 + 196,586 − 140,460 = 733,084; Q2 676,958 + 399,149 − 304,693 = 771,414; Q3 676,958 + 644,320 − 489,449 = 831,829. Last twelve months cash interest: Q1 259,812 + 37,343 − 41,303 = 255,852; Q2 259,812 + 148,719 − 133,830 = 274,701; Q3 259,812 + 183,459 − 172,756 = 270,515. Principal debt over Adjusted EBITDA: FY2024 3,710,018 / 332,928 = 11.14x; FY2025 4,033,394 / 676,958 = 5.96x; Q1 4,063,717 / 733,084 = 5.54x; Q2 4,213,379 / 771,414 = 5.46x; Q3 4,267,981 / 831,829 = 5.13x. Net: FY2024 10.54x; FY2025 5.73x; Q1 5.23x; Q2 5.22x; Q3 4.94x. Cover: FY2024 1.58x; FY2025 2.61x; Q1 2.87x; Q2 2.81x; Q3 3.07x. All 15 values equal the figures in the financial base handoff. Share of nine month Adjusted EBITDA from changes in recoveries: 244,898 / 644,320 = 38.0%. Revolver availability check: 1,485.0 − 974.763 = 510.237 US$m, equal to the stated 510.2. Figures compared across modules (11): principal debt, cash, last twelve months Adjusted EBITDA, last twelve months cash interest, leverage, net leverage, cover, availability, utilisation, the 2029 maturities and the 38.0% share; all identical. Quotation check: 36 quotations in the financial base handoff and 48 in the business view handoff, 84 in total, each located on its cited page.

## Gaps

The open items are the gaps and issues in the registers above: covenant ratios and executed agreements (restricting covenant and legal conclusions), seller concentration, ratings and market data, letters of credit and the availability difference, ownership and related parties, and the two definition differences. No upstream conclusion is changed by this review. Where this review corrects an upstream handoff, it does so plainly: the FY2024 total ERC cell in the financial table should read not printed in the pinned sources, rather than not read. The earlier handoff cannot be edited. The review rests on the pinned filings and releases only and uses no external source.

## Next module

The report can be assembled from these handoffs. Present covenant headroom, legal ranking and market views as unsupported, keep Management Language attributed, and name the basis when quoting share repurchases and portfolio purchases. Next evidence action: obtain the compliance certificate and the executed credit agreement, indentures and intercreditor agreement.
