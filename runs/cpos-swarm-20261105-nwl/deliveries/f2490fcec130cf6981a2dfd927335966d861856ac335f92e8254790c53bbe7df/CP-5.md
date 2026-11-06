## Request

NEWELL BRANDS INC. (issuer id nwl, ticker NWL), as of 2026-11-05, pathway credit_snapshot, public case. This module traces the claims in the four accepted handoffs (readiness, financial base, business context, credit synthesis) back to the seven pinned filings and releases, re-performs their calculations, and grades whether the analysis is traceable enough for committee use. Run id nwl-2026-11-05-credit_snapshot-host; consolidated registrant, USD millions, Q3 2026 current and FY2025 prior.

## Sources

### Issuer sources re-opened for this trace (pinned name and sha256 of the retained text)

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_nwl-20251231.htm.jsonl | dcc793cfdb2b8cc449076ad729ebed59fbf0fa17a270e35dd5b40e5638fe6453 |
| 10-Q_2026-03-31_nwl-20260331.htm.jsonl | e491b436993330fb987ef524b9f78ce96b1802f1285b9af80a913a9adee3f88d |
| 10-Q_2026-06-30_nwl-20260630.htm.jsonl | b3b449c8e355a64543631b4a3e69f0acef91c01cc896e4386758050640b5804b |
| 10-Q_2026-09-30_nwl-20260930.htm.jsonl | 8b58e3ae589a883e4dd1d132d51cbe5455a5976aebd62f8367be4b91ce06fe29 |
| EX-99.1_2026-05-01_exhibit991_q1xmarchx2026.htm.jsonl | 944b1e0aff94a38b463c337c910588c7aa29def150477cd6c4593c7400267ccd |
| EX-99.1_2026-07-31_exhibit991_q2xjunex2026.htm.jsonl | 5357537cee17090bbc993249463e8c84756e595916b24485d6cd92a469d185c7 |
| EX-99.1_2026-10-30_exhibit991_q3xseptemberx20.htm.jsonl | f28d7c981e9628280882affba403a5eab9c05f0b6a106f3147b334e29e9ba0d3 |

Run context (settings only, not issuer evidence): 814453-newell-brands-inc-nwl.json, sha256 6bed67ca32030e1461ea08189ab22687642083ba91fdd1b6bdf65186613803b0. No external source was used by any handoff or by this module.

### Supplied handoffs (run id nwl-2026-11-05-credit_snapshot-host, as-of 2026-11-05)

| Module | sha256 | Scope consumed |
| --- | --- | --- |
| CP-0 | 76b36ebebc3da26e35258cfc1d5238c4f31ac02f26874a5c908da1046b4e7b0c | Source readiness; coverage counts, gaps, version relationships |
| CP-1 | d5a9065811e44ca39f3fa15acd9d11f35ebd1ced370fa07658e63d3b51da3b1d | Financial base: statements, five chart tables, instruments, claims outside debt, covenants, events |
| CP-1A | 941c20e8a49b07fa5a41d2499a967e1852785616331c7ee2842448c4fc2bdb78 | Business and transaction context, timeline, governance behaviour, credit translations |
| CP-2 | 0d671c22d582c6a8b4b0a6f8e518b84b0b77d37205d6bb01ec8ebbedc993b2a9 | Credit synthesis: view, findings, strengths and weaknesses, risks, calculations |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is traceable: every quoted locator was found on its cited page and every derived number was recomputed. Five small defects were found, none changing a conclusion. Use is restricted on covenant headroom, cash interest and ownership. | Medium | Covenant levels, interim cash interest, executed agreements and ownership percentages are not in the pack, so those conclusions cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All quoted source locators in the four handoffs were located exactly, and all derived figures recompute. | The leverage, liquidity and cash-flow numbers a committee will rely on are reproducible. | High |
| The credit synthesis overstates additional secured drawing capacity: letters of credit were not deducted. | The correct figure is the printed net availability, a smaller capacity ahead of unsecured creditors. | High |
| Leverage rests on a management EBITDA with no covenant EBITDA or bridge to filed lines. | Reported leverage may understate underlying leverage; a filing-based ratio is higher. | Medium |
| Security is explicit for only two of the senior note series. | Statements that all notes are unsecured rest partly on rating wording. | Medium |

### Evidence trace view

The analysis of NEWELL BRANDS INC. is traceable enough for committee use on what it states, and restricted on what the pack cannot support. Every locator quoted in the four handoffs was found verbatim on its cited page, and every derived figure recomputes from the quoted inputs. The most important claims, leverage, cash conversion, liquidity and the 2028 refinancing, trace to filed statements or to management reconciliations that are labelled as management claims. The most important provenance gap is that leverage uses management's normalized EBITDA, with no covenant EBITDA and no add-back bridge to filed lines, while covenant levels, interim cash interest and ownership are not in the pack at all. One calculation in the synthesis is wrong and is corrected below; the earlier handoff cannot be edited.

### Re-performance results

| Check | Population | Result |
| --- | --- | --- |
| Quoted substrings located on the cited page of the cited source | 32 in the readiness handoff, 59 in the financial base, 65 in the business context, 5 in the synthesis | All 161 found exactly as written |
| Figures in prose and tables not carried by a quote, compared with source pages (sampled across all seven sources) | Statement lines for every period, debt table, availability, segment table, release reconciliations, ladder | Agreed to source in every case sampled; no mismatch |
| Derived numbers recomputed | All items in the calculation sections of the financial base, business context and synthesis | All agree except one item in the synthesis (see Corrections) |
| Direction and superlative claims | Leverage fell, net debt rose, liquidity below the 2028 maturity, profit concentration | Each supported by two cited figures |
| Subsequent events and cutoff | Receivables Facility amendment effective 2026-10-02; results release 2026-10-30 | Both before the cutoff 2026-11-05 and flagged as post-period |

### Corrections to earlier handoffs

1. The credit synthesis (Key findings, item 4, and the calculation row for additional secured drawing capacity) states that drawn secured borrowings could rise by 526 from 215, computed as 741 - 215. That omits the 46 of letters of credit issued under the same facility, which also use availability. The correct additional drawing capacity is 741 - 215 - 46 = 480, which equals the net availability printed in the Q3 2026 report and used as liquidity in the financial base. The synthesis text should be read with 480 in place of 526; the mechanic it describes (more secured claims on current assets) is unchanged, and 480 also implies a smaller rise in the priority claim.
2. The credit synthesis calls the 1,252 maturity bucket the 2028 notes. The 2025-12-31 maturity ladder prints 1,252 for 2028, which the 10-K supports as 1,250 of 8.500% notes plus other debt; the principal of the notes is 1,250. The difference is 2, does not change any ratio and is a labelling matter.
3. The business context tags the sector label as a Documentary Fact sourced to the run context. The run context is a settings file, not issuer evidence, so the label should be read as context-supplied and Not independently sourced.
4. The credit synthesis describes unsecured notes ranking behind the secured facility generally. Only the 2028 and 2031 notes are stated as senior unsecured obligations in the pages read; for the 2029, 2030, 2032, 2036 and 2046 notes the security is not printed there, and the rating agencies' references to senior unsecured debt are the only wording. The conclusion is plausible but its lineage is Weak for those series.
5. The synthesis assessment table gives governance a confidence of "Not assessable beyond Medium", which is not one of the permitted values; it should read Not assessable.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_nwl-20251231.htm.jsonl | Audited annual report, filed | FY2025 with FY2024 and FY2023 comparatives | Newell Brands Inc. and subsidiaries, consolidated | Statements, debt note, maturity ladder at 2025-12-31, cash paid for interest and taxes, segments, customers | Maturity ladder and covenant description are superseded in part by 2026 events; pension tables not extracted | Financial base, business context, synthesis |
| S2 | 10-Q_2026-03-31_nwl-20260331.htm.jsonl | Unaudited quarterly report, filed | Q1 2026 | Consolidated | Statements, debt table, Credit Revolver availability | No cash interest or tax lines | Financial base |
| S3 | 10-Q_2026-06-30_nwl-20260630.htm.jsonl | Unaudited quarterly report, filed | Q2 2026 and six months | Consolidated | Statements, debt table, Credit Revolver availability, new facility as subsequent event | No cash interest or tax lines | Financial base |
| S4 | 10-Q_2026-09-30_nwl-20260930.htm.jsonl | Unaudited quarterly report, filed | Q3 2026 and nine months | Consolidated | Statements, facility-level debt, ABL terms, factoring, subsequent event, segments, litigation | No maturity ladder, covenant levels or cash interest | All modules |
| S5 | EX-99.1_2026-05-01_exhibit991_q1xmarchx2026.htm.jsonl | Management earnings release, furnished | Q1 2026 | Consolidated | Net debt and trailing-twelve-month normalized EBITDA reconciliation | Management non-GAAP | Financial base |
| S6 | EX-99.1_2026-07-31_exhibit991_q2xjunex2026.htm.jsonl | Management earnings release, furnished | Q2 2026 | Consolidated | Net debt, trailing-twelve-month normalized EBITDA, tariff recoveries | Management non-GAAP | Financial base, synthesis |
| S7 | EX-99.1_2026-10-30_exhibit991_q3xseptemberx20.htm.jsonl | Management earnings release, furnished | Q3 2026, nine months, trailing twelve months | Consolidated | Net debt, EBITDA reconciliation, outlook, intent to reduce debt and factoring | Management non-GAAP and forward-looking | All modules |
| C1 | 814453-newell-brands-inc-nwl.json | Run settings, not issuer evidence | as-of 2026-11-05 | Issuer identity labels | Ticker, sector label, currency, periods | Ratings, quotes and deal terms are blank | Identity only |

#### T5B.2 Top credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage of 4.46x net and 4.70x gross on trailing-twelve-month normalized EBITDA, with net debt up 122 since FY2025 | CP-1, CP-2 | Net debt 4,592 and normalized EBITDA 1,030 in the Q3 release; net debt 4,470 and EBITDA 882 at FY2025 | Sets debt service and refinancing tolerance; the ratio fell on earnings, not repayment | Leverage is sustainable only if EBITDA is | S7 pages 17 and 18; S6 page 17; S5 page 15 | Management EBITDA; filing-basis ratio is higher at 5.51x |
| 2 | Thin cash conversion against interest and dividends | CP-1, CP-2 | Operating cash flow 254 less capex 201 equals 53 for the last twelve months, against net interest 341 and dividends 127 | Little internal cash for debt reduction | Reliance on refinancing | S1 page 82; S4 pages 2 and 3 | Cash interest for 2026 not supplied |
| 3 | 2028 refinancing and springing maturity of the asset-based facility | CP-1, CP-1A, CP-2 | 2028 ladder bucket 1,252; liquidity 729; facility matures earlier if material debt of 125 or more is outstanding 91 days before its maturity | Decides default risk if markets close | Key event for liquidity and monitoring | S1 page 107; S4 pages 20 and 50 | 2028 maturity date and executed agreement not supplied |
| 4 | Liquidity of 729 before factoring | CP-1 | Cash 249 and net ABL availability 480 | Bridges seasonality and the Q4 peak | Adequate near term, below the 2028 bucket | S4 pages 2 and 20 | Availability depends on the borrowing base |
| 5 | Customer concentration and weak pricing power | CP-1A, CP-2 | Amazon about 17% and Walmart about 13% of FY2025 net sales; retailer power limits price recovery | Revenue and margin shocks | Business risk anchor | S1 pages 9 and 10 | Contract terms not disclosed |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net debt 4,592 and normalized EBITDA 1,030 | CP-1 | "Net debt [1] $ 4,592 $ 4,470 $ 4,548" and "Normalized EBITDA $ 1,030 $ 882 $ 857" (S7 pages 17, 18) | Yes | Management release | Directly Sourced | Supported, management claim | High | Committee-Ready |
| Net debt / EBITDA 4.46x and gross 4.70x | CP-1, CP-2 | Division of the two printed figures above and gross debt 4,841 (S4 page 17) | Yes | Calculated from filed and management inputs | Calculated | Supported | High | Committee-Ready |
| Operating cash flow less capex 53 | CP-1, CP-2 | Cash flow lines in S1 page 82 and S4 page 3 | Yes | Filed statements | Calculated | Supported | High | Committee-Ready |
| Liquidity 729 | CP-1, CP-2 | Cash 249 and "resulting in a net availability of approximately $480 million" (S4 page 20) | Yes | Filed | Calculated | Supported | High | Committee-Ready |
| Derived maturity roll-forward to 2026-09-30 | CP-1, CP-2 | 2025-12-31 ladder (S1 page 107) adjusted for redemption and issuance (S4 pages 17, 18) | Yes | Derived | Assumption-Based | Supported with assumption that other principal is unchanged | Medium | Remediation Needed |
| Springing maturity of the asset-based facility | CP-1, CP-1A, CP-2 | Maturity clause (S4 page 20) | Yes | Filed description | Directly Sourced | Supported; effective date not computable | Medium | Remediation Needed |
| Customer concentration | CP-1A, CP-2 | S1 page 10 | Yes | Filed | Directly Sourced | Supported | High | Committee-Ready |
| Additional secured drawing capacity 526 | CP-2 | 741 - 215 (S4 page 20) | Yes | Calculated | Conflicting | Incorrect; correct value 480 | Low | Remediation Needed |
| All senior notes unsecured | CP-2 | Explicit for two series only (S1 page 105, S4 page 18) | Partial | Filed | Weak Lineage | Partly supported | Medium | Remediation Needed |
| Covenant headroom | CP-1, CP-2 | No levels in any source | No | Not applicable | Insufficient Information | Correctly stated as not calculable | High | Committee-Ready as a gap |

#### T5B.4 Source lineage

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net debt and EBITDA at Q3 2026 | runs/cpos-swarm-20261105-nwl/source-text/ | EX-99.1_2026-10-30_exhibit991_q3xseptemberx20.htm.jsonl | S7 | pages 17 and 18, net debt and trailing-twelve-month reconciliation | CP-1 leverage chart | Management non-GAAP | Medium | Quoted verbatim |
| Total debt 4,841 and instruments | runs/cpos-swarm-20261105-nwl/source-text/ | 10-Q_2026-09-30_nwl-20260930.htm.jsonl | S4 | page 17, Footnote 8 | CP-1 debt table | Filed | High | Sum of rows agrees to 4,841 |
| ABL terms, availability and letters of credit | runs/cpos-swarm-20261105-nwl/source-text/ | 10-Q_2026-09-30_nwl-20260930.htm.jsonl | S4 | pages 19 and 20 | CP-1 liquidity, CP-1A transaction, CP-2 | Filed | High | Availability 741 less 215 less 46 equals 480 |
| Maturity ladder at 2025-12-31 | runs/cpos-swarm-20261105-nwl/source-text/ | 10-K_2025-12-31_nwl-20251231.htm.jsonl | S1 | page 107, Future Debt Maturities | CP-1 maturity chart | Filed | High | Total 4,718 |
| FY2025 cash interest and taxes | runs/cpos-swarm-20261105-nwl/source-text/ | 10-K_2025-12-31_nwl-20251231.htm.jsonl | S1 | page 82, supplemental disclosures | CP-1 interest cover | Filed | High | Only annual figures exist |
| Factoring outstanding | runs/cpos-swarm-20261105-nwl/source-text/ | 10-Q_2026-09-30_nwl-20260930.htm.jsonl | S4 | pages 9 and 10 | CP-1 claims outside debt, CP-2 | Filed | High | 300 plus 135 |
| Customer concentration | runs/cpos-swarm-20261105-nwl/source-text/ | 10-K_2025-12-31_nwl-20251231.htm.jsonl | S1 | page 10, Customers | CP-1A operating model | Filed | High | Percentages approximate |
| Segment results | runs/cpos-swarm-20261105-nwl/source-text/ | 10-Q_2026-09-30_nwl-20260930.htm.jsonl | S4 | pages 27 and 28, Footnote 13 | CP-1 segment base, CP-1A | Filed | High | Quarter and nine months |
| Tariff recoveries in Q2 2026 | runs/cpos-swarm-20261105-nwl/source-text/ | EX-99.1_2026-07-31_exhibit991_q2xjunex2026.htm.jsonl | S6 | page 2, highlights | CP-1 sensitivity, CP-2 | Management release | Medium | Also in S4 page 33 |
| Deleveraging intent and operating cash flow outlook | runs/cpos-swarm-20261105-nwl/source-text/ | EX-99.1_2026-10-30_exhibit991_q3xseptemberx20.htm.jsonl | S7 | pages 1 and 4 | CP-1A, CP-2 | Management language | Medium | Forward-looking |
| Ratings history | runs/cpos-swarm-20261105-nwl/source-text/ | 10-K_2025-12-31_nwl-20251231.htm.jsonl | S1 | page 107, Rating Downgrades | CP-1A profile | Filed | High | Latest rating action in pack is the fourth quarter of 2025 |
| Covenant description | runs/cpos-swarm-20261105-nwl/source-text/ | 10-K_2025-12-31_nwl-20251231.htm.jsonl | S1 | page 106 and page 57 | CP-1 covenants | Filed | High | Levels not printed |
| Subsequent event on the Receivables Facility | runs/cpos-swarm-20261105-nwl/source-text/ | 10-Q_2026-09-30_nwl-20260930.htm.jsonl | S4 | page 34, Footnote 15 | CP-1 events, CP-1A | Filed | High | Post-period, effective 2026-10-02 |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net debt / EBITDA, FY2025 to Q3 2026 | CP-1 chart, CP-2 | Net debt 4,470; 4,764; 4,797; 4,592; EBITDA 882; 881; 1,007; 1,030 | Net debt divided by trailing-twelve-month normalized EBITDA | Recomputed, matches: 5.07, 5.41, 4.76, 4.46 | Supported | High | Core leverage metric | S5, S6, S7 |
| Gross debt / EBITDA | CP-1 chart | Gross debt 4,673; 4,965; 5,006; 4,841 | Gross debt divided by the same EBITDA | Recomputed, matches: 5.30, 5.64, 4.97, 4.70 | Supported | High | Leverage | S5, S6, S7 |
| Cash interest cover FY2025 | CP-1 chart | EBITDA 882, cash paid for interest 354 | 882 / 354 | Recomputed, matches 2.49 | Supported | High | Debt service | S1 page 82 |
| Last-twelve-month income and cash flow | CP-1 table | FY2025 plus nine months 2026 less nine months 2025 | Addition and subtraction of printed lines | Recomputed, matches all 14 items | Supported | High | Base for ratios | S1, S4 |
| Discrete Q2 and Q3 cash flow | CP-1 table | Cumulative cash flow statements | Differences of cumulative amounts | Recomputed, matches: Q2 operating cash flow 29, Q3 297 | Supported | High | Seasonality | S2, S3, S4 |
| Liquidity totals | CP-1 chart, CP-2 | Cash plus printed net availability | 203+685; 201+327; 209+451; 249+480 | Recomputed, matches 888; 528; 660; 729 | Supported | High | Liquidity | S1 to S4 |
| Maturity roll-forward | CP-1 chart | Ladder 4,718; remove 130 and 500; add 600 and 215 | 4,718 - 130 - 500 + 600 + 215 | Recomputed, matches 4,903; assumes no other principal change | Supported with assumption | Medium | Maturity wall | S1 page 107, S4 pages 17 and 18 |
| Filing-basis EBITDA before impairment | CP-1 table, CP-2 | Operating income 72, D&A 314, impairment 447 | 72 + 314 + 447 = 833; net debt 4,592 / 833 | Recomputed, matches 5.51 | Supported | Medium | Alternative leverage | S1, S4 |
| Tariff recovery sensitivity | CP-1, CP-2 | 1,030 less 100 less 26 | 4,592 / 904 | Recomputed, matches 5.08; one-sided | Supported with caveat | Medium | Earnings quality | S6 page 2 |
| Factoring-inclusive leverage | CP-2 | Net debt 4,592 plus factoring 435 | 5,027 / 1,030 | Recomputed, matches 4.88 | Supported | Medium | Debt-like funding | S4 pages 9 and 10 |
| Additional secured drawing capacity | CP-2 | Availability 741, drawn 215, letters of credit 46 | 741 - 215 - 46 | Recomputed: 480; CP-2 states 526 | Not supported | High | Priority claims | S4 page 20 |
| Segment and product shares | CP-1A, CP-2 | Segment sales and product groupings | Division by 7,204 and 5,416 | Recomputed, matches 52%, 37%, 10%, 65%; 25.0%, 24.5%, 18.0%, 14.5%, 10.8%, 7.2% | Supported | High | Mix | S1, S4 |
| Equity less goodwill and intangibles | CP-2 | Equity 2,364, goodwill 3,082, intangibles 1,453 | 2,364 - 4,535 | Recomputed, matches -2,171 | Supported | High | Asset quality | S4 pages 2 and 3 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Additional secured drawing capacity of 526 | Letters of credit omitted; correct value 480 | Conflicting | Overstates the growth in priority claims | Read as 480; correct in any later revision | Credit synthesis, Key findings item 4 and calculations |
| MINOR | All senior notes are unsecured | Security explicit for the 2028 and 2031 notes only | Weak Lineage | Priority analysis depends on which notes are unsecured | Confirm in the indentures or the exhibit list | Credit synthesis, Key findings item 4 |
| MINOR | Maturity chart rows for 2026, 2027 and 2031 | Derived, not printed; assumes other principal unchanged | Assumption-Based | A reader may take the chart as a printed ladder | Keep the derived label in the basis column | Financial base, maturity chart |
| MINOR | Sector label | Sourced to run context but tagged as a documentary fact | Weak Lineage | Context is not issuer evidence | Treat as context-supplied | Business context, company profile |
| MINOR | Governance confidence label | Value outside the permitted set | Insufficient Information | Presentation integrity | Read as Not assessable | Credit synthesis assessment table |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Citation presence and locator precision | Strong | 161 quoted substrings located exactly on the cited page | A wrong page would hide an unsupported figure | Figures can be re-opened by a reviewer | None |
| Calculation reproducibility | Strong with one error | All other derived figures recompute from quoted inputs | An unreproducible ratio misleads leverage tolerance | Leverage and liquidity are reliable | Correct the one item |
| Source quality separation | Adequate | Management measures are labelled and kept apart from filed statements | A management EBITDA presented as filed would overstate comparability | Leverage is a management basis | Keep labels in the report |
| Definition consistency | Adequate | Net debt uses carrying value and excludes restricted cash; principal-based total is shown separately | Mixed bases could shift ratios by a few hundredths | Ratios are internally consistent | State basis next to each ratio |
| Cross-handoff consistency | Strong | Net debt, EBITDA, liquidity and factoring agree across all four handoffs | Inconsistent inputs would break the thesis | Single set of numbers | None beyond the corrections above |
| Extraction fidelity | Not independently reviewed | Text extraction only; no rendered-page review | A parsing error could alter a figure | Residual risk is low given exact matches | Keep as a stated limit |
| Forward-looking and management claims | Adequate | Outlook, savings and deleveraging intent labelled as management language | Unproven intentions treated as facts | Deleveraging is not yet evidenced | Keep attribution |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant levels and reported ratios | Credit Revolver covenant levels and the new facility's fixed charge test level | Headroom drives default risk | Covenant headroom cannot be traced | Restricts covenant conclusions | Credit agreements and compliance certificate |
| G2 | Interim cash interest and taxes | Cash paid lines in 2026 reports | Cash interest cover for 2026 | Expense-based cover only | Lowers confidence in debt service | Next filings or management data |
| G3 | 2028 notes maturity date, principal split of later notes, guarantors | Indentures and exhibits | Date the facility can spring; priority | Maturity wall is approximate | Lowers confidence in refinancing timing | Indentures |
| G4 | Ownership percentages and current ratings | Proxy statement and rating reports | Control and market access | Governance unassessed | Lowers confidence in governance | Proxy statement, agency reports |
| G5 | Add-back bridge from normalized EBITDA to filed lines | Management bridge beyond the release | Quality of earnings | Filing-basis ratio is the cross-check | Lowers confidence in leverage | Management bridge |
| G6 | Pension, contingent claim amounts and trapped cash | Notes not extracted | Debt-like claims | Claims outside debt incomplete | Lowers confidence in adjusted leverage | 10-K Footnotes 10 and 17 |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/.../1.response.md; nwl-2026-11-05-credit_snapshot-host | Source readiness for four consumers | Filed documents and releases | Six required headings present | Passed with no defect | Coverage and gaps agree with the sources |
| CP-1 | requests/CP-1/.../1.response.md; nwl-2026-11-05-credit_snapshot-host | Financial base and chart data | Filed statements and management reconciliations | Six required headings and five report selectors present | Passed with minor items | Maturity roll-forward derived |
| CP-1A | requests/CP-1A/.../1.response.md; nwl-2026-11-05-credit_snapshot-host | Business, transaction, governance | Filed documents | Six required headings and three report selectors present | Passed with minor items | Sector label tag |
| CP-2 | requests/CP-2/.../1.response.md; nwl-2026-11-05-credit_snapshot-host | Credit synthesis | Upstream handoffs | Six required headings and two report selectors present | Passed with one correction | Secured drawing capacity |

#### T5.2 Citation and evidence support issues

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Key findings item 4: notes unsecured | Partial | Security explicit for two series only | Cite or soften | Does not block committee use |
| MINOR | CP-1A | Company profile: sector label | Context only | Tagged as a documentary fact | Re-tag as context | Does not block committee use |
| MINOR | CP-1 | Maturity chart rows 2026, 2027 and 2031 | Derived | Not printed in any source | Keep derived label | Does not block committee use |

#### T5.3 Math, logic and definition issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Additional secured drawing capacity stated as 526 | 741 - 215 omits 46 of letters of credit; correct 741 - 215 - 46 = 480 | Conflicts with the printed net availability of 480 | Read as 480 | Does not change the conclusion; correction stated above |
| MINOR | CP-2 | 1,252 labelled as the 2028 notes | Bucket includes other debt of 2 | Notes principal is 1,250 | Relabel as the 2028 maturity bucket | None |
| MATERIAL | CP-1, CP-2 | Leverage on management EBITDA | Normalized EBITDA is not a covenant EBITDA | Filing-basis ratio is 5.51x against 4.46x | Keep both ratios visible | Restricts use to leverage as a management-basis view |

#### T5.4 Legal and structural claim issues

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-1A, CP-2 | Springing maturity of the asset-based facility and lien overlap with the receivables purchaser | ABL credit agreement and receivables purchase agreement | Executed agreements not supplied; filing descriptions only | State as description, not interpretation | Counsel review before reliance |
| MINOR | CP-2 | Secured facility ranks ahead of unsecured notes on current assets | Indentures and security documents | Security of several note series not printed in pages read | Soften or cite | Counsel review |

#### T5.5 Market and relative-value claim issues

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | None made: the synthesis states no spread, yield, price, peer ranking, instrument or recovery conclusion | Quotes and peers are blank in the context | Market data not supplied by design | None | No market-implied or relative-value view is available to the committee |

#### T5.6 Cross-module conflicts and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Secured drawing capacity 526 in the synthesis against the printed net availability 480 used in the financial base | Same run, same sources | Treat 480 as controlling | Report text carries 526 in one finding |
| MINOR | CP-1, CP-0 | 2025-12-31 ladder and covenant description superseded by 2026 refinancing | Annual report versus Q3 2026 report | Use the Q3 2026 report for current balances | Already flagged in the handoffs |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Duplication | Leverage, liquidity and cash-flow figures repeat across handoffs and agree | None | Repetition does not add or alter evidence |
| MATERIAL | CP-2 | Materiality | The 2028 refinancing and cash conversion are correctly ranked as the key risks | None | Supports committee focus |

#### T5.8 Handoff and export integrity

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Assessment table confidence value | A label outside the permitted set | Read as Not assessable | Report table needs the permitted value |
| MINOR | CP-1 | Chart tables | Q3 2026 row uses trailing-twelve-month EBITDA, stated in the basis column | Keep basis text | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | MINOR | CP-2 | Calculation | Secured drawing capacity should be 480, not 526 | Read as 480 | Committee use permitted with correction | Open, correction stated |
| I-02 | MINOR | CP-2 | Labelling | 1,252 is the 2028 bucket, not the notes principal (1,250) | Relabel | None | Open |
| I-03 | MINOR | CP-2 | Lineage | Notes described as unsecured beyond the two explicit series | Cite or soften | None | Open |
| I-04 | MINOR | CP-1A | Lineage | Sector label from context tagged as documentary fact | Re-tag | None | Open |
| I-05 | MINOR | CP-2 | Presentation | Governance confidence label outside permitted set | Read as Not assessable | None | Open |
| I-06 | MATERIAL | CP-1, CP-2 | Definition | Leverage on management EBITDA with no covenant EBITDA | Keep management basis and filing basis visible | Restricts covenant conclusions | Open, source gap |
| I-07 | MATERIAL | CP-1, CP-2 | Gap | Covenant levels, interim cash interest, ownership not supplied | Obtain sources | Restricts those conclusions | Open, source gap |

Committee use: Restricted for covenant headroom, cash interest cover for 2026, ownership and the exact springing date of the asset-based facility; permitted with the corrections above for leverage, liquidity, cash conversion, customer concentration and the refinancing view. Confidence: High that quoted evidence is traceable, Medium overall. The numeric confidence score is Not computed because its script is not available in host mode; none is invented.

## Calculations

Re-performed independently from the quoted inputs. USD millions.

| Item | Inputs | Result | Agrees with handoff |
| --- | --- | --- | --- |
| Net debt / EBITDA | 4,470/882; 4,764/881; 4,797/1,007; 4,592/1,030 | 5.07; 5.41; 4.76; 4.46 | Yes |
| Gross debt / EBITDA | 4,673/882; 4,965/881; 5,006/1,007; 4,841/1,030 | 5.30; 5.64; 4.97; 4.70 | Yes |
| Cash interest cover FY2025 | 882/354 | 2.49 | Yes |
| Expense-basis cover | 882/321; 881/333; 1,007/338; 1,030/341 | 2.75; 2.65; 2.98; 3.02 | Yes |
| Last-twelve-month net sales, operating income, net loss | 7,204+5,416-5,307; 39+344-311; -285-8-30 | 7,313; 72; -323 | Yes |
| Operating cash flow, capex, dividends, last twelve months | 264+93-103; 247+131-177; 120+97-90 | 254; 201; 127 | Yes |
| Free cash flow after capex and dividends | 254-201-127 | -74 | Yes |
| Liquidity | 249+480 | 729 | Yes |
| Availability checks | 852-130-37; 789-425-37; 969-470-48; 741-215-46 | 685; 327; 451; 480 | Yes |
| Maturity roll-forward | 4,718-130-500+600+215; 1,252+500+750+815+1,586 | 4,903; 4,903 | Yes |
| Carrying value of instruments | 1,242+475+744+215+592+495+418+658+2 | 4,841 | Yes |
| Tariff recovery sensitivity | 4,592/904; 4,841/904 | 5.08; 5.36 | Yes |
| Factoring-inclusive leverage | (4,592+435)/1,030; (4,841+435)/1,030 | 4.88; 5.12 | Yes |
| Filing-basis EBITDA | 39+311+346; 72+314+447 | 696; 833 | Yes |
| Filing-basis net leverage | 4,470/696; 4,592/833 | 6.42; 5.51 | Yes |
| Segment total, nine months 2026 | 9+553-17 | 545 | Yes |
| Equity less goodwill and intangibles | 2,364-3,082-1,453 | -2,171 | Yes |
| Additional secured drawing capacity | 741-215-46 | 480 | No: the synthesis states 526 (741-215); correction in Findings |
| 2028 bucket | 1,250+2 | 1,252 | Yes (labelled as notes in the synthesis) |

No new analytical figure is introduced; the only departure from the handoffs is the corrected drawing capacity.

## Gaps

| Gap | Effect on the trace | Action |
| --- | --- | --- |
| Covenant levels, reported covenant ratios and executed agreements are not in the pack. | Covenant and springing-date claims cannot be traced beyond filing descriptions. | Obtain the credit agreements and compliance certificates. |
| Interim cash interest and taxes are not printed; the add-back bridge from normalized EBITDA to filed lines is not supplied. | Debt service and earnings quality rest on expense-based cover and the filing-basis cross-check. | Obtain management data. |
| Ownership percentages, current ratings and market quotes are not supplied. | Governance and market views cannot be traced. | Obtain the proxy statement and rating reports. |
| Extraction was text only and no rendered page or chart was reviewed. | A parsing error remains possible although every quote matched exactly. | Keep as a stated limit. |
| The numeric confidence score was not computed. | Confidence is stated qualitatively. | Compute with the governed script outside host mode if required. |

## Next module

This is the last module in the run. The report is composed from the accepted handoffs; read the corrections in `### Corrections to earlier handoffs` with it, in particular the secured drawing capacity of 480. Before committee reliance on covenant headroom, 2026 cash interest cover, ownership or the exact springing maturity date, obtain the sources listed in the gaps.
