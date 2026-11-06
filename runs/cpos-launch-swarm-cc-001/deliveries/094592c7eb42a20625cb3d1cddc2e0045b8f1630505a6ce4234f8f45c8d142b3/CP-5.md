## Request

Module CP-5 (evidence trace validator with the absorbed CP-5A research-integrity grade) for The Chemours Company (issuer id cc), as of 2026-11-05, pathway credit_snapshot, run cc-2026-11-05-credit_snapshot-host. Scope is the default Top 5 material credit drivers across the accepted CP-0, CP-1, CP-1A and CP-2 handoffs, each traced back to the pinned filings and re-checked for locators, calculations, conflicts and handoff consistency. This module changes no credit conclusion and repairs no lineage silently.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Document ID used in registers |
|---|---|---|
| 10-K_2025-12-31_cc-20251231.htm.jsonl | adf80f4588f501b9f797e1b55a5853888465c5d9b30aef8ff07b3cd4340b3957 | S1 |
| 10-Q_2026-03-31_cc-20260331.htm.jsonl | 544e858f14516405499b0793277b117ab856893d213de4bfdfd312ae33ddb9fd | S2 |
| 10-Q_2026-06-30_cc-20260630.htm.jsonl | 5934bf743b44e940824956ac90d2979f28da0477a0f669044693e5e59c78b62f | S3 |
| 10-Q_2026-09-30_cc-20260930.htm.jsonl | f23013a765ad5943b395240230ccfbe7a0cca417e186c8a1a82b34a215485de7 | S4 |
| EX-99.1_2026-05-05_cc-ex99_1.htm.jsonl | cf37012a81481ef001a376d207312af6444e1ec5683c9d45ff930f84bd36dd4e | S5 |
| EX-99.1_2026-08-04_cc-ex99_1.htm.jsonl | 5e0a77f0453e40d6a00670f0f971f2e2c0487e12a68a0222858c84133578166e | S6 |
| EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | d716a94a423338ae97b02c515014fccad1457c8952131fe6a67cf2f82a22b1e0 | S7 |

The context source (sha256 016f2454bb1a5018293508b6e2a82129a813baf9ca2bdc7dfff95d2a92314261) gives dates and identity only and is not issuer evidence. Locators are `page:N` of the converted-text source (an extraction chunk, not the printed page). S2 and S3 were read for period coverage only; no traced claim depends on them.

### Supplied handoffs

| Module | sha256 | Document ID |
|---|---|---|
| CP-0 | 6f03921afffdd59771f82c8fa703da2ea79a5f7ed0167c1aad309367f97b0c3b | H0 |
| CP-1 | 8032cefaee77bf66ebfb3f15d78f38711196a252e9f91cb50cd60ea920b9f970 | H1 |
| CP-1A | 7428ba38369c27a725cb9d0873d50a5f2041781f039ff357a4c83ef76bb98e8b | H1A |
| CP-2 | 776439306c032e9690d8f495b5129ce154c5f5791019a73465a71e5910a1df56 | H2 |

## Findings

### Traceability conclusion

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 3 are directly sourced, 1 is calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the missing revolver capacity after the October 7, 2026 maturity, together with the absent executed financing documents, which matters because liquidity and covenant headroom cannot be traced beyond filing summaries and implies research use is Restricted until those sources are added. One CP-2 timing statement is also wrong and needs correction.

Research QA status: Restricted. Committee status: Requires More Work before unrestricted committee use. The numeric Confidence Score is owned by a script that is not part of this transport, so it is Not supplied here rather than estimated.

### Analytical appendix — complete canonical registers

All five checks of the 5-dimension audit were done by re-reading the pinned sources at the cited locators and by recomputing every calculation from its stated inputs.

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
|---|---|---|---|---|---|---|---|
| S1 | 10-K_2025-12-31_cc-20251231.htm.jsonl | High: filed and audited annual report | Fiscal year ended December 31, 2025, with FY2024 comparatives as revised | The Chemours Company, consolidated | Audited statements, debt note, covenant statement for the revolver, revision note, cash interest and tax paid, business description | Prior periods revised for immaterial errors; text converted from HTML | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_cc-20260331.htm.jsonl | High: filed unaudited interim report | Quarter ended March 31, 2026 | The Chemours Company, consolidated | Interim statements and notes | Not cited for any traced figure | Period coverage only |
| S3 | 10-Q_2026-06-30_cc-20260630.htm.jsonl | High: filed unaudited interim report | Quarter ended June 30, 2026 | The Chemours Company, consolidated | Interim statements and notes | Not cited for any traced figure | Period coverage only |
| S4 | 10-Q_2026-09-30_cc-20260930.htm.jsonl | High: filed unaudited interim report, latest | Quarter ended September 30, 2026 | The Chemours Company, consolidated | Statements, debt note, liquidity, contingencies, segment note | Unaudited; supplemental cash flow note lists non-cash items only | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-05-05_cc-ex99_1.htm.jsonl | Medium: issuer-authored unaudited release | Q1 2026 | The Chemours Company, consolidated | Results, Q1 outlook, net leverage at March 31 | Management non-GAAP measures; flattened tables | CP-1, CP-1A |
| S6 | EX-99.1_2026-08-04_cc-ex99_1.htm.jsonl | Medium: issuer-authored unaudited release | Q2 2026 | The Chemours Company, consolidated | Results, Q2 outlook, net leverage at June 30 | Management non-GAAP measures; flattened tables | CP-1, CP-1A |
| S7 | EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | Medium: issuer-authored unaudited release | Q3 2026 and trailing twelve months | The Chemours Company, consolidated | Results, reconciliation, LTM Adjusted EBITDA, outlook | Management non-GAAP measures; flattened tables obscure column dates | CP-1, CP-1A, CP-2 |
| H0 | CP-0 handoff (response file in run folder) | Derived: accepted upstream handoff | As of 2026-11-05 | The Chemours Company | Source readiness and gap list | Describes sources, adds no figures | All modules |
| H1 | CP-1 handoff | Derived: accepted upstream handoff | Q3 2026, nine months 2026, FY2025, FY2024 | The Chemours Company | Financial tables and calculation bridges | Calculations are analyst-made from reported inputs | CP-2 |
| H1A | CP-1A handoff | Derived: accepted upstream handoff | Through 2026-11-05 | The Chemours Company | Business model, transaction summary, timeline | Contains analyst interpretation rows | CP-2 |
| H2 | CP-2 handoff | Derived: accepted upstream handoff | As of 2026-11-05 | The Chemours Company | Credit view, risks, new calculations | Contains one timing misstatement (see T5B.6) | Report |

Module Status: Ready with Limitations. All four upstream handoffs and all seven pinned sources are available. The limitations are the absent executed financing documents and the flattened table text. Traceability Scope: Top 5. Entity key status: issuer_id cc is available; no entity key is missing. Upstream re-anchor: each handoff carries run cc-2026-11-05-credit_snapshot-host, as-of 2026-11-05 and the current period q3-2026; no mismatch found.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
|---|---|---|---|---|---|---|---|
| 1 | High leverage with thin coverage: management net leverage about 4.3x, gross debt principal 3,872, LTM interest cover about 2.7x | CP-1 and CP-2 | Debt table, unrestricted cash, LTM Adjusted EBITDA 744 and LTM net interest 274 | Debt service capacity and tolerance for an earnings miss depend on the ratio | Sets financial risk assessment | S4 page:24, page:3; S7 page:13 | LTM Adjusted EBITDA is a management measure; FY2025 total not printed |
| 2 | Liquidity at September 30, 2026 and revolver tranche that matured on October 7, 2026 | CP-1 and CP-1A | Cash 698, availability 953, matured 220 tranche, springing maturity | Revolver is the only committed liquidity source beyond cash | Determines near-term liquidity view | S4 page:149, page:25, page:26 | Post-maturity availability not stated |
| 3 | Legacy PFAS and environmental settlements outside net debt | CP-1A and CP-2 | New Jersey 875 over 25 years, North Carolina 455 over 15 years, reserves 553 and 805 | Fixed-in-time cash calls compete with debt service and are excluded from the leverage ratio | Shapes adjusted leverage and monitoring | S4 page:155, page:116, page:153 | Cost-sharing cap under the MOU only partly quantified in the pack |
| 4 | Earnings quality: Adjusted EBITDA of 200 in Q3 2026 excludes large litigation, land-gain and insurance items | CP-1 and CP-2 | Reconciliation and segment table | Reported net income is 196 but includes a 150 insurance receipt and 50 gain | Determines how much weight to put on adjusted measures | S7 page:13, page:11; S4 page:2 | Segment build differs from reported Adjusted EBITDA for some comparative periods |
| 5 | Concentration of refinancing in 2028 and 2029 with a springing revolver maturity | CP-1A and CP-2 | Debt table by maturity and revolver springing provision | Market access at the current rating decides revolver availability and debt cost | Shapes refinancing risk | S4 page:24, page:25, page:149 | Executed documents not supplied; timing wording in CP-2 needs correction |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
|---|---|---|---|---|---|---|---|---|
| Leverage and coverage (driver 1) | CP-1, CP-2 | Debt table total principal 3,872; cash 698; LTM Adjusted EBITDA 744; LTM interest 274 | Yes | High for balances; Medium for the management EBITDA | Calculated | Supported with a management-defined input | Medium | Committee-Ready |
| Liquidity at the balance-sheet date | CP-1 | Cash 698 and availability 953 at September 30, 2026 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Revolver capacity after October 7, 2026 | CP-1, CP-1A, CP-2 | Filing says 220 tranche matured; availability afterwards is not stated | Partial | High for the maturity; no source for the result | Insufficient Information | Open gap, carried as a caveat | Low | Remediation Needed |
| Legacy settlements and reserves | CP-1A, CP-2 | Settlement terms and reserve balances in the contingencies note | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Earnings quality and Adjusted EBITDA | CP-1, CP-2 | Reconciliation lines, segment tables, SG&A footnote | Yes | Medium (management non-GAAP) | Directly Sourced | Supported as attributed management measure | Medium | Remediation Needed |
| Refinancing concentration in 2028 and 2029 | CP-2 | Maturity shares from the debt table; springing maturity wording | Yes | High for inputs | Analyst Inference | Reasoned reading of cited inputs; one timing phrase incorrect | Medium | Remediation Needed |
| Rating position | CP-1, CP-1A, CP-2 | Moody's B1 downgrade on July 17, 2026; S&P statement dated April 16, 2025 | Yes | High for the filing statement; S&P is stale | Directly Sourced | Supported; S&P stale | Medium | Committee-Ready |
| Management leverage trajectory (4.9x, 4.4x, 4.3x) | CP-1 | Three releases | Yes | Medium | Directly Sourced | Supported as management measure | Medium | Committee-Ready |
| Illustrative leverage including reserves (about 6.1x) | CP-2 | Net debt plus reserves over LTM Adjusted EBITDA | Yes | Medium | Assumption-Based | Sensitivity, labelled as such | Low | Committee-Ready |
| Business model and customer concentration | CP-1A | 10-K business section | Yes | High | Directly Sourced | Supported | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
|---|---|---|---|---|---|---|---|---|
| Total debt principal is 3,872 at September 30, 2026 and 4,182 at December 31, 2025 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:24, Note 15 Debt | CP-1 Debt composition | Sourced | High | Agrees with component sum |
| Unrestricted cash and cash equivalents are 698 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:3 balance sheet; page:149 | CP-1 Financials table | Sourced | High | Of which 410 held by foreign subsidiaries |
| Revolver availability is 953, net of 47 letters of credit | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:149; page:26 | CP-1 Liquidity bridge | Sourced | High | Dated September 30, 2026 |
| 220 of revolving commitments matured on October 7, 2026 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:25; page:149 | CP-1, CP-1A, CP-2 | Sourced | High | Subsequent to the balance-sheet date |
| Springing maturity applies if term loans or 2028 and 2029 notes are not refinanced in the prior 91 days | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:25 | CP-2 Key credit risks | Sourced | High | Summary of the agreement, not the agreement |
| Net debt of 3,174 and net leverage of approximately 4.3x | source-text/EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | S7 | page:4; page:13 | CP-1 Financials table | Sourced | Medium | Management definition at page:12 |
| LTM Adjusted EBITDA is 744 and LTM interest expense net is 274 | source-text/EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | S7 | page:13 | CP-1 Debt and leverage bridge | Sourced | Medium | Column dates inferred from layout |
| Q3 2026 net sales 1,540 and net income attributable to Chemours 196 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:2 | CP-1 Financials table | Sourced | High | Includes 150 SG&A credit |
| Nine-month cash from operations 263 and capex 144 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:5 | CP-1 Cash flow bridge | Sourced | High | Dividend lines are on page:6 |
| FY2025 cash from operations 264, capex 213, cash interest 251, cash taxes 74 | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K_2025-12-31_cc-20251231.htm.jsonl | S1 | page:163 | CP-1 Financials table | Sourced | High | Audited, as revised |
| Moody's downgraded to B1 from Ba3 on July 17, 2026; S&P BB- negative outlook affirmed April 16, 2025 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:149 | CP-1, CP-1A, CP-2 | Sourced | High | S&P statement stale |
| New Jersey consent order totals 875 over 25 years; remaining 176 on a net present value basis after the first 100 payment | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:155 | CP-1A Transaction summary | Sourced | High | Present value basis not defined in the pack beyond the filing |
| North Carolina settlement totals 455 over 15 years; first payment of 51 in October 2026 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:116 | CP-1A Transaction summary | Sourced | High | Subsequent event |
| Accrued litigation 553 (191 current) and environmental remediation 805 (116 current) | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:155; page:153 | CP-1 Obligations outside net debt | Sourced | High | Partly recoverable under the MOU |
| 7.875% senior notes due 2034 of 700 issued March 12, 2026; 2027 notes (495) and 188 of 2028 notes redeemed | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:27; page:24 | CP-1A Transaction summary | Sourced | High | Indenture not supplied |
| 10-K described the 2027 notes as not repayable at maturity absent refinancing | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K_2025-12-31_cc-20251231.htm.jsonl | S1 | page:170 | CP-1A Transaction summary | Sourced | High | Superseded by the March 2026 redemption |
| Full-year 2026 Adjusted EBITDA guidance moved from 800 to 900 (Q1) to 775 to 825 (Q2) to 775 to 800 (Q3) | source-text/EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | EX-99.1_2026-05-05, 2026-08-04 and 2026-11-02 releases | S5, S6, S7 | page:6 of each release | CP-1 Quarterly trajectory | Sourced | Medium | Management guidance |
| Segment Adjusted EBITDA Q3 2026: TSS 136, TT 85, APM 24 | source-text/EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | S7 | page:11 | CP-1 Segment results | Sourced | Medium | Agrees with the 10-Q segment note at page:133 |
| About 2,400 customers; no customer above 10% of net sales | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K_2025-12-31_cc-20251231.htm.jsonl | S1 | page:6 | CP-1A Company and operating model | Sourced | High | Dated December 31, 2025 |
| Quarterly dividend of 0.0875 per share declared October 27, 2026 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:156 | CP-1A, CP-2 | Sourced | High | Subsequent event |
| Restricted cash is 103 (41 current, 62 non-current) | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q_2026-09-30_cc-20260930.htm.jsonl | S4 | page:130 | CP-1 Financials table | Sourced | High | Of which 100 is PFAS insurance escrow |
| Revolver-only maximum senior secured net leverage ratio of 2.00 to 1.00 | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K_2025-12-31_cc-20251231.htm.jsonl | S1 | page:211 | CP-1 Debt composition | Sourced | High | Level after the quarter ended September 30, 2026 not stated |
| Prior periods revised for immaterial errors | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K_2025-12-31_cc-20251231.htm.jsonl | S1 | page:166 to page:168 | CP-1 Reported basis | Sourced | High | Revision tables show effect by line |
| Total debt principal comparative of 4,185 is a year-earlier balance | source-text/EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | S7 | page:13 | CP-1 Financials table | Inference | Weak: column header lost in flattened text | Dating is inferred from column order, not read from a header |
| Total debt principal of 3,872 is exceeded only modestly by the 2028 and 2029 maturities at 35% | not applicable as a single source | derived from S4 debt table | S4 | page:24 | CP-2 Key findings | Calculated | High for inputs | Analyst percentage |

#### T5B.5 Calculation and assumption register

Every row below was recomputed independently from its stated inputs. All recomputed values agree with the handoff values unless stated.

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
|---|---|---|---|---|---|---|---|---|
| Net debt, September 30, 2026 | CP-1, CP-2 | Debt principal 3,872; unrestricted cash 698 | 3,872 less 698 = 3,174; period September 30, 2026; no normalization | Calculated | Agrees with source-printed 3,174 | High | Leverage, liquidity | S4 page:24; S7 page:13 |
| Net leverage on LTM Adjusted EBITDA | CP-1, CP-2 | Net debt 3,174; LTM Adjusted EBITDA 744 | 3,174 divided by 744 = 4.27x | Calculated | Consistent with the printed approximately 4.3x | Medium | Leverage | S7 page:13 |
| Gross leverage on LTM Adjusted EBITDA | CP-1 | 3,872 and 744 | 3,872 divided by 744 = 5.20x | Calculated | Supported | Medium | Leverage | S4 page:24; S7 page:13 |
| LTM interest coverage | CP-1, CP-2 | 744 and LTM net interest 274 | 744 divided by 274 = 2.72x | Calculated | Supported | Medium | Debt service | S7 page:13 |
| LTM cash from operations, capex and free cash flow | CP-2 | FY2025 264 and 213; nine months 2026 263 and 144; nine months 2025 127 and 168 | CFO 264 + 263 less 127 = 400; capex 213 + 144 less 168 = 189; FCF 400 less 189 = 211; 211 divided by 3,872 = 5.4% | Calculated | Supported; uses revised comparatives | Medium | Debt service, liquidity | S1 page:163; S4 page:5 |
| LTM EBITDA less capex over net interest | CP-2 | 744, 189, 274 | (744 less 189) divided by 274 = 2.03x | Calculated | Supported | Medium | Debt service | S7 page:13; S1 page:163 |
| Maturity shares (2028, 2029, 2032, 2033, 2034, other) | CP-2 | Instrument balances from the debt table | 748, 620, 1,041, 600, 700 and 163 over 3,872 = 19.3%, 16.0%, 26.9%, 15.5%, 18.1%, 4.2% (sum 100.0%) | Calculated | Supported | High | Refinancing | S4 page:24 |
| Secured term loans over LTM Adjusted EBITDA (proxy) | CP-2 | 1,194 gross; 496 net of cash; 744 | 1,194 divided by 744 = 1.60x; 496 divided by 744 = 0.67x | Calculated | Labelled proxy, not a covenant test | Low | Covenant context | S4 page:24; S7 page:13 |
| Illustrative leverage including reserves | CP-2 | Net debt 3,174; litigation 553; environmental 805; EBITDA 744 | (3,174 + 553 + 805) divided by 744 = 6.09x | Assumption-Based | Labelled sensitivity; mixes discounted and undiscounted items | Low | Leverage sensitivity | S4 page:155, page:153 |
| Free Cash Flows FY2025 and FY2024 | CP-1 | CFO and capex from the 10-K | 264 less 213 = 51; (633) less 360 = (993) | Calculated | Analyst application of the management definition to audited lines | Medium | Cash flow quality | S1 page:163 |
| Total liquidity and no-replacement arithmetic case | CP-1, CP-2 | 698; 953; 780; 47 | 698 + 953 = 1,651; 780 less 47 = 733; 698 + 733 = 1,431 | Calculated | Second case is bounded arithmetic, not a finding | Medium | Liquidity | S4 page:149, page:25 |
| Guidance-implied EBITDA less capex less interest | CP-2 | Guidance ranges for EBITDA, capex and interest | 775 less 230 less 280 = 265; 800 less 220 less 275 = 305 | Calculated | Supported; excludes taxes, settlements, dividends | Medium | Debt service | S7 page:6, page:18 |
| Segment build versus reported Adjusted EBITDA | CP-1 | Segment totals, other and corporate | Q3 2026 245 + 1 less 46 = 200; nine months 2026 746 + 6 less 136 = 616; nine months 2025 760 + 7 less 148 = 619 versus 614; Q3 2025 233 + 2 less 45 = 190 versus 189 | Calculated | Differences of 5 and 1 remain unexplained | Medium | Earnings quality | S4 page:133; S7 page:13 |
| Margins and conversion | CP-1 | Reported lines | 231/1,540 = 15.0%; 233/1,495 = 15.6%; 729/4,512 = 16.2%; 746/4,478 = 16.7%; 200/1,540 = 13.0%; 189/1,495 = 12.6%; 616/4,512 = 13.7%; 614/4,478 = 13.7%; 119/616 = 19.3% | Calculated | Supported | High | Margin resilience | S4 page:2; S7 page:13, page:17 |
| Dividend burden | CP-2 | 0.0875 per share; 150.5 million shares | 0.0875 times 150.5 times 4 = about 53 per year | Calculated | Agrees with the roughly 50 in the 10-K | Medium | Cash use | S4 page:156; S1 page:110 |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
|---|---|---|---|---|---|---|
| Critical | Liquidity view (CP-1, CP-2) | Revolver availability after the October 7, 2026 maturity of the 220 tranche has no source; the 953 figure is dated September 30, 2026 | Insufficient Information | Evidence: filing states the maturity and the availability. Mechanic: committed liquidity may be lower on the as-of date. Implication: liquidity adequacy is bounded, not confirmed | Obtain a post-period filing or issuer statement; until then keep the caveat | CP-1 Liquidity bridge; CP-2 Key findings |
| Critical | Covenant headroom (CP-1, CP-2) | Executed Credit Agreement not supplied; only a management compliance statement and a 10-K revolver test level | Insufficient Information | Evidence: summary text only. Mechanic: headroom cannot be calculated. Implication: default-risk and creditor-control views rest on summaries | Obtain the executed agreement and amendments | CP-1 Gaps; CP-2 Credit assessment |
| Material | Maturity timing (CP-2) | CP-2 states that the 2028 and 2029 debt falls due within about 25 months of September 30, 2026; the 2029 notes fall due in November 2029, about 38 months out, so the phrase is wrong for the 2029 notes | Conflicting | Evidence: debt table maturities. Mechanic: overstates the nearness of the 2029 maturity. Implication: refinancing urgency is overstated for part of the stack | Correct the sentence in a new run folder; the accepted answer is not edited | CP-2 Key credit risks table |
| Material | Leverage history (CP-1) | Segment build differs from management Adjusted EBITDA by 5 for nine months 2025 and by 1 for Q3 2025; FY2025 total Adjusted EBITDA is not printed | Conflicting | Evidence: segment note and release reconciliation. Mechanic: comparative base for trend is uncertain. Implication: improvement narrative relies on management's totals | Keep release figures as attributed; do not reconcile without a bridge | CP-1 Gaps |
| Material | Adjusted EBITDA add-backs (CP-1, CP-2) | Management measure excludes large litigation, environmental and land-gain items; Credit Agreement EBITDA definition not supplied | Weak Lineage | Evidence: reconciliation lines. Mechanic: add-backs may not map to covenant EBITDA. Implication: leverage on covenant terms is not derivable | Obtain the definition | CP-1, CP-2 leverage statements |
| Minor | Debt comparative (CP-1) | The 4,185 comparative debt principal is described as a year-earlier balance, inferred from column order in a flattened table | Weak Lineage | Evidence: table text lost its header. Mechanic: dating may be mistaken. Implication: no effect on the September 30, 2026 figure | Mark as inferred or drop the comparative | CP-1 Financials table notes |
| Minor | Cash flow locator (CP-1) | Nine-month dividends paid (39 and 63) are cited to page:5 but appear on page:6 | Weak Lineage | Evidence: page text. Mechanic: reader looks on the wrong page. Implication: figure is correct, locator off by one | Correct the locator in a new run | CP-1 Interpretation, capital returns |
| Minor | Debt paydown (CP-1A) | Euro term loan paydowns were logged as conflicting across releases, but the amounts reconcile: 140 in April sits within 230 for the second quarter, and 230 + 50 = 280 for nine months | Conflicting | Evidence: three source statements. Mechanic: a non-conflict was logged as a conflict. Implication: none for credit view; reduces clarity | Reclassify as consistent in a new run | CP-1A Conflicts logged |
| Minor | Tax wording (CP-2) | Text says full-year GAAP results include a 307 provision, which is a nine-month figure | Weak Lineage | Evidence: income statement page:2. Mechanic: period label slip. Implication: none for the conclusion | Correct the label | CP-2 Key findings |
| Minor | Illustrative leverage (CP-2) | The 6.09x figure mixes discounted and undiscounted reserves | Assumption-Based | Evidence: reserve balances. Mechanic: not a debt measure. Implication: could be misread as a metric | Keep the sensitivity label | CP-2 Calculations |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
|---|---|---|---|---|---|
| Source coverage | Ready with Remediation | Seven pinned filings cover FY2025, three 2026 quarters and three releases; no financing agreements, deck or market data are in the pack | Debt terms rest on note summaries | Covenant, guarantee and restricted-payment views cannot be verified | Obtain executed documents |
| Citation completeness | Committee-Ready | Every traced figure maps to a page locator and was re-read; one locator is off by one page | A wrong locator slows verification without changing the figure | Low | Correct the dividend locator |
| Calculation traceability | Committee-Ready | All 15 calculation groups recomputed and agree; inputs and formulas are shown | Analyst calculations rest on management and audited inputs | Leverage and coverage results are reproducible | Keep labels for proxies and sensitivities |
| Assumption transparency | Ready with Remediation | The only assumption-based items are the no-replacement revolver arithmetic and the reserves sensitivity, both labelled | Readers may treat sensitivities as measures | Moderate if mislabelled | Preserve labels in the report |
| Markdown/export artifact integrity | Ready with Remediation | Headings and tables parsed in each handoff; flattened source tables required inference once | Column dating inference can mislead | Minor | Mark inferred comparatives |

Overall auditability is the lowest of the five dimensions: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
|---|---|---|---|---|---|---|
| CP-5-GAP-001 | Revolver capacity after October 7, 2026 | Post-period availability statement | Evidence: matured 220 tranche. Mechanic: liquidity could be lower. Implication: liquidity conclusion is bounded | CP-1 and CP-2 liquidity | High impact | Later filing or issuer statement |
| CP-5-GAP-002 | Executed Credit Agreement, amendments, indentures and guarantor schedules | The documents themselves | Mechanic: covenant, collateral and guarantee terms known only through summaries. Implication: creditor-control view unverified | Debt terms, covenant statements | High impact | Executed documents from the filing exhibits |
| CP-5-GAP-003 | Credit Agreement EBITDA definition and covenant levels after the quarter ended September 30, 2026 | Definition and test schedule | Headroom not calculable | Covenant compliance statements | High impact | Credit Agreement |
| CP-5-GAP-004 | Interim cash paid for interest and taxes | Supplemental cash flow disclosure for 2026 periods | Cash-basis coverage not measurable | Cash flow quality | Medium impact | Later filing or issuer disclosure |
| CP-5-GAP-005 | FY2025 total Adjusted EBITDA not printed; segment build differences | Printed total and bridge | Comparative leverage base uncertain | Leverage trend | Medium impact | Release or filing reconciliation for FY2025 |
| CP-5-GAP-006 | Ownership and holder detail | Holder table or proxy statement | Support behaviour cannot be assessed beyond documented actions | Governance rows | Low impact | Proxy statement |
| CP-5-GAP-007 | Market data, quotes and spreads | Price and spread data | Relative-value claims are out of scope; none were made | None in this run | Low impact | Market data source if CP-3 is run |
| CP-5-GAP-008 | Cost structure split and contract share of revenue | Segment disclosures | Margin resilience to volume decline not quantifiable | Business risk | Medium impact | Investor materials or segment disclosures |
| CP-5-GAP-009 | Securitization and factoring balances and treatment | Quantified balances for debt-like analysis | Adjusted leverage may be understated | Leverage sensitivity | Medium impact | Receivables notes in later filings |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
|---|---|---|---|---|---|---|
| CP-0 | requests/CP-0 response file; run cc-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High inputs | Six required headings present | Accepted with limitations | All consumers READY_WITH_LIMITATIONS |
| CP-1 | requests/CP-1 response file; run cc-2026-11-05-credit_snapshot-host | Financial tables, debt and bridges | High for filings; Medium for releases | Six headings present; one table under the financials selector | Accepted with remediation | One locator off by one page; one inferred comparative |
| CP-1A | requests/CP-1A response file; run cc-2026-11-05-credit_snapshot-host | Business, transaction, governance, timeline | High | Six headings present; two selector tables and prose transaction section | Accepted with remediation | Debt paydown logged as a conflict that reconciles |
| CP-2 | requests/CP-2 response file; run cc-2026-11-05-credit_snapshot-host | Credit synthesis, risks, calculations | Medium to High | Six headings present; credit view opens the findings | Accepted with remediation | One timing statement wrong; one period label slip |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
|---|---|---|---|---|---|---|
| Minor | CP-1 | Capital returns: dividends paid 39 and 63 | Supported by S4 page:6 | Cited to page:5 | Correct the locator | None on conclusions |
| Material | CP-2 | Refinancing of 2028 and 2029 debt within about 25 months | Contradicted for the 2029 notes by S4 page:24 maturities | Timing phrase overstated | Correct the phrase in a new run | Restricts use of that risk row until corrected |
| Minor | CP-1 | Debt comparative 4,185 as a year-earlier balance | Inferred from column order | Header lost in flattened text | Mark as inferred | None on September 30, 2026 figures |
| Material | CP-1A | Euro term loan paydowns logged as conflicting | Supported by S5 page:4, S6 page:5, S4 page:26, which reconcile | Over-logged conflict | Reclassify as consistent | None on credit view |
| Critical | CP-1, CP-1A, CP-2 | Revolver availability after October 7, 2026 | No source states it | Gap carried as a caveat in all three handoffs, which is correct | Obtain a source | Liquidity conclusion stays bounded |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
|---|---|---|---|---|---|---|
| Material | CP-1 | Segment build differs from management Adjusted EBITDA for comparative periods | Management Adjusted EBITDA definition includes items beyond the segment totals | Differences of 5 (nine months 2025), 1 (Q3 2025), 8 (FY2025 against LTM-implied) | Keep as unexplained; do not reconcile | Restricts trend statements |
| Minor | CP-1 | Two D&A values for nine months 2025 (259 and 236) | Cash flow statement versus reconciliation presentation | Labelled in CP-1 | Keep labels | None |
| Material | CP-2 | Leverage including reserves | Mixes discounted and undiscounted items; not a debt measure | None found | Keep sensitivity label | None if labelled |
| Minor | CP-1 | Free cash flow for FY2025 and FY2024 | Management definition applied to audited lines | None found | Keep labelled as analyst calculation | None |
| Minor | CP-2 | Secured proxy ratios | Not the Credit Agreement test | None found | Keep proxy label | None |

All recomputations in T5B.5 agree with the handoffs.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
|---|---|---|---|---|---|---|
| Critical | CP-1, CP-2 | Revolver springing maturity linked to term loans and 2028 and 2029 notes | Credit Agreement | Only the filing summary | Obtain the agreement | Legal review needed before reliance on mechanics |
| Critical | CP-1, CP-2 | Compliance with covenants and revolver maximum senior secured net leverage of 2.00 to 1.00 | Credit Agreement and compliance certificate | Level after September 30, 2026 not stated | Obtain the agreement | Legal review needed |
| Material | CP-1A | Guarantees by domestic restricted subsidiaries; notes ranking | Indentures and guarantor schedules | Generic wording only | Obtain the documents | Legal review needed |
| Material | CP-1A, CP-2 | Settlement obligations and MOU cost-sharing cap | Settlement agreements and MOU | Summaries only | Obtain the agreements | Legal review needed |

#### T5.5 Relative-value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
|---|---|---|---|---|---|---|
| Minor | CP-2 | No relative-value, spread or price claim was made | Quotes, spreads, peer data | Context lists none | Keep CP-2 free of market claims | None; RV belongs to a module not selected here |
| Minor | CP-1A | Rating references are filing statements only | Current S&P rating | S&P statement dated April 16, 2025 | Treat as stale | Low |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
|---|---|---|---|---|---|
| Material | CP-1, CP-2 | Net leverage about 4.3x (management) versus recomputed 4.27x and gross 5.20x; consistent | None | Keep both bases visible | Report must state the basis |
| Material | CP-1, CP-1A, CP-2 | Revolver availability 953 at September 30, 2026 against the October 7, 2026 maturity: handled consistently as a caveat in all three | FY2025 10-K and Q3 10-Q state the same commitment structure at their dates | Obtain post-period source | Liquidity statements restricted |
| Minor | CP-1 and CP-0 | CP-0 said debt principal comparatives need care; CP-1 used an inferred year-earlier label | None | Mark as inferred | None |
| Minor | CP-1A and CP-1 | Euro term loan amounts consistent across the three sources | None | Reclassify the logged conflict | None |
| Minor | All | Same run id, as-of date and issuer id in each handoff | Handoffs are current versions of the run | None | None |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
|---|---|---|---|---|---|
| Minor | CP-1, CP-1A, CP-2 | Duplication | The matured revolver tranche and legacy settlements are restated in all three handoffs | Keep once in the report with a pointer | Low |
| Material | CP-2 | Materiality | The critical caveats (revolver, covenants) appear in the credit view and gaps; correctly prominent | None | Low |
| Material | CP-2 | Committee readiness | One factual timing phrase is wrong and one label slipped | Correct in a new run | Restricted until corrected |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
|---|---|---|---|---|---|
| Minor | CP-0 to CP-2 | Source and handoff listings with sha256 | None found; each lists issuer sources and upstream handoffs with sha256 | None | None |
| Minor | CP-1 | Single table under the financials selector | Table is wide and mixes flows and balances | Keep column notes | Readers must read column header carefully |
| Minor | CP-1A | Prose-only transaction section | Compliant | None | None |
| Minor | CP-2 | Opening view length | Credit view within the allowed length | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
|---|---|---|---|---|---|---|---|
| CP-5-ISS-001 | Critical | CP-1, CP-2 | Evidence gap | Revolver capacity after October 7, 2026 not sourced | Obtain later filing | Restricts liquidity conclusion | Open |
| CP-5-ISS-002 | Critical | CP-1, CP-2 | Evidence gap | Executed financing documents and covenant levels not supplied | Obtain documents | Restricts covenant and structure claims | Open |
| CP-5-ISS-003 | Material | CP-2 | Factual error | 2029 notes described as due within about 25 months | Correct in a new run | Restricts that risk row | Open |
| CP-5-ISS-004 | Material | CP-1 | Source difference | Segment build versus management Adjusted EBITDA differs for comparatives | Keep as attributed | Restricts trend statements | Open |
| CP-5-ISS-005 | Material | CP-1, CP-2 | Definition | Adjusted EBITDA add-backs not mapped to Credit Agreement EBITDA | Obtain definition | Restricts covenant statements | Open |
| CP-5-ISS-006 | Minor | CP-1 | Locator | Dividend lines cited to page:5, found on page:6 | Correct locator | None | Open |
| CP-5-ISS-007 | Minor | CP-1 | Weak lineage | Year-earlier dating of the 4,185 comparative inferred | Mark as inferred | None | Open |
| CP-5-ISS-008 | Minor | CP-1A | Over-logged conflict | Euro term loan paydowns reconcile | Reclassify | None | Open |
| CP-5-ISS-009 | Minor | CP-2 | Label | Nine-month tax provision described as full-year | Correct label | None | Open |

Clearance decision: Restricted. The report may be used for committee discussion with the stated caveats, but not as an unrestricted basis for decisions on liquidity after October 7, 2026 or on covenant headroom. Priority remediation: first obtain the executed financing documents and post-period revolver information (issues 001, 002 and 005); second correct the CP-2 timing phrase (003); then the minor locator and label fixes. Accepted answers are not edited in this run; fixes belong in a new run folder.

## Calculations

Independent recomputation performed by CP-5 for every calculation in the CP-1 and CP-2 handoffs. Inputs are as shown in T5B.5; each was read again from the cited page.

| Check | Inputs | Result | Agreement with handoff |
|---|---|---|---|
| Debt table sum, September 30, 2026 | 1,041 + 153 + 595 + 620 + 600 + 700 + 43 + 91 + 12 + 17 | 3,872 | Agrees |
| Debt table sum, December 31, 2025 | 1,050 + 488 + 495 + 783 + 620 + 600 + 39 + 88 + 10 + 9 | 4,182 | Agrees |
| Carrying value bridge | 3,872 less 15 less 24 | 3,833 = 50 + 3,783 | Agrees |
| Net debt and ratios | 3,872 less 698 = 3,174; 3,174 / 744; 3,872 / 744; 744 / 274 | 4.27x; 5.20x; 2.72x | Agrees |
| LTM free cash flow | 264 + 263 less 127 = 400; 213 + 144 less 168 = 189; 400 less 189 | 211; 5.4% of 3,872 | Agrees |
| EBITDA less capex coverage | (744 less 189) / 274 | 2.03x | Agrees |
| Maturity shares | 748, 620, 1,041, 600, 700, 163 over 3,872 | 19.3%, 16.0%, 26.9%, 15.5%, 18.1%, 4.2%; combined 2028 and 2029 is 35.3% | Agrees |
| Secured proxies | 1,194 / 744; 496 / 744 | 1.60x; 0.67x | Agrees |
| Reserves sensitivity | 4,532 / 744 | 6.09x | Agrees |
| Liquidity | 698 + 953; 780 less 47; 698 + 733 | 1,651; 733; 1,431 | Agrees |
| Segment builds | 245 + 1 less 46; 746 + 6 less 136; 760 + 7 less 148; 233 + 2 less 45 | 200; 616; 619; 190 | Agrees; differences to reported 614 and 189 are 5 and 1 |
| Margins | As in T5B.5 | 15.0%, 15.6%, 16.2%, 16.7%, 13.0%, 12.6%, 13.7%, 13.7% | Agrees |
| Guidance-implied range | 775 less 230 less 280; 800 less 220 less 275 | 265 and 305 | Agrees |
| Q1 derived capex and FCF | 144 less 44 less 51; 119 less 114 less 98 | 49; (93) | Agrees |
| Maturity timing from the balance-sheet date | September 30, 2026 to November 15, 2029 | About 38 months | Disagrees with the handoff phrase "about 25 months" for the 2029 notes (issue CP-5-ISS-003) |
| Top 5 classification counts | Driver 1 calculated; drivers 2, 3 and 4 directly sourced; driver 5 analyst inference | 3, 1, 0, 1, 0 | Used in the traceability conclusion |

## Gaps

Gaps are carried in T5B.8 (CP-5-GAP-001 to CP-5-GAP-009) and the issue log in T5.9 (CP-5-ISS-001 to CP-5-ISS-009). The gaps that change a conclusion are: revolver capacity after the October 7, 2026 maturity, the executed financing documents with the covenant definitions, and the Adjusted EBITDA definition. These restrict liquidity, covenant and structure statements; they do not restrict the traced balance-sheet, debt-table and settlement facts. Limitations of this run: the Confidence Score script and the YAML front-matter envelope of the full CP-5 method are not part of this Markdown transport, so the score is Not supplied; no legal or market evidence exists in the pack to audit beyond the filing summaries.

## Next module

None. CP-5 is the last selected module; CP-OS assembles the report from the accepted handoffs. The report should carry the Restricted status, the revolver and covenant caveats, and should not repeat the CP-2 timing phrase; the corrections listed in T5.9 belong in a new run folder.
