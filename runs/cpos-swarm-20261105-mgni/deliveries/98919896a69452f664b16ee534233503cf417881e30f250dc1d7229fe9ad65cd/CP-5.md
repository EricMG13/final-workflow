# Evidence trace and research-integrity QA: MAGNITE, INC. (mgni)

## Request

- Issuer: MAGNITE, INC. (issuer id mgni), as of 2026-11-05, information cutoff 2026-11-05, pathway credit_snapshot, minimum module set. This module checks the source readiness, financial base, business context and credit synthesis handoffs and grades them (the absorbed research-integrity phase).
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: qa_status Passed; Confidence Score 43, band Low (from the confidence score script, see Calculations); committee_status Draft Only. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.

## Sources

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_mgni-20251231.htm.jsonl | f96c3c8e001359e3762f2fdcdb5fec62dc8b34a692251ca50bc2b0320cbc2a0a |
| 10-Q_2026-03-31_mgni-20260331.htm.jsonl | a236956e4f58c23dd0c7e9814923ff8c58122f0f2ffc4593ab7dcd2ac0165adf |
| 10-Q_2026-06-30_mgni-20260630.htm.jsonl | 796b488acb30e088707602178e4e306b131923e994381f8d88dd91dd9706c3bb |
| 10-Q_2026-09-30_mgni-20260930.htm.jsonl | c6922a9ebeac839059c55928b8190f39ac8376ff2e5306b6695aa910a9515bb4 |
| EX-99.1_2026-05-06_a991-earningsq12026.htm.jsonl | 1a65026a829ea6d3398cf84619845f6c5e542133314c7959aef5563816dda9a4 |
| EX-99.1_2026-08-05_a991-earningsq22026.htm.jsonl | 7a22ad7a167049f41876318b3adec058b3521559a35265d5009853f0eba7f49d |
| EX-99.1_2026-11-04_a991-earningsq32026.htm.jsonl | 9404d81beccd30783613c5d17e44e7f768a511dbf6b00a1825d39fa611f52e22 |
| context | add9e4e5fe29cabeba543552138279256276897be557a9b8ceef018e156869fc |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | 3b5491ad4792081e28ccae80a3f58279ef4978af29432bbcc0ff2472969d5e7a |
| CP-1 | cf0ec312bd9af098d8cd5dace46250f5fca56aeaabf079c0944d4e2f7db15241 |
| CP-1A | b1efedaebd7ef38fb9a661e7eae1a0c5ee6fc705e354b6c541cdd812e11c37e9 |
| CP-2 | 4e34195d7605cd99daf11db1b9ff8816019879fe8368e66cf17154c0e40344dc |

Locators `key pN` mean the chunk `page:N` of the named pinned text file; keys are S1 to S7 in the source register below.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis traces well to the filings: every checked quotation and recomputed figure matches. Seven small citation and wording defects remain, and the credit agreement behind the covenant view is not supplied. | Medium | This is a self-review by the same author, and the credit agreement is missing. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of 84 parsed quotation spans in the four analyses, 80 were found in the source chunks; the other 4 were parser artifacts, and no quotation is misquoted. | Quoted claims about debt, covenant, concentration and Google can be relied on. | High |
| All 16 tie-outs and every recomputed leverage and cover figure agree with the printed numbers, including 1.27x gross leverage at the last twelve months to September 30, 2026. | The leverage and cover figures are reproducible from the filings. | High |
| Covenant headroom cannot be certified: the springing test is described only in the filings, and the 61% indicator is an inference with unknown definitions. | Headroom should not be quoted as a covenant figure. | Medium |
| One pointer in the business analysis cites a financial line that does not exist, and the synthesis says no debt matures before 2029 despite small annual amortization. | Both are small and do not change the credit view. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 3 are directly sourced, 1 is calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting or insufficient-information items. The most important provenance gap is that the executed credit agreement and its covenant definitions are not supplied, which matters because the leverage test, restricted-payment capacity and guarantor terms rest on the filings' own description and implies that covenant headroom and legal capacity stay unverified for committee use. Seven minor citation and wording defects were found; none changes a figure or a conclusion, and they are logged below rather than repaired, because accepted handoffs cannot be edited.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_mgni-20251231.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | MAGNITE, INC., consolidated | Audited statements, debt note, Adjusted EBITDA reconciliation, business, concentration | Text conversion of HTML; tables flattened | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_mgni-20260331.htm.jsonl | High: filed, unaudited interim report | Quarter ended March 31, 2026 | Same | Interim statements, debt table, revolver availability | Text conversion; unaudited | CP-0, CP-1 |
| S3 | 10-Q_2026-06-30_mgni-20260630.htm.jsonl | High: filed, unaudited interim report | Three and six months ended June 30, 2026 | Same | Interim statements, debt table, revolver draw | Text conversion; unaudited | CP-0, CP-1, CP-1A |
| S4 | 10-Q_2026-09-30_mgni-20260930.htm.jsonl | High: filed, unaudited interim report | Three and nine months ended September 30, 2026 | Same | Interim statements, debt, covenant text, liquidity, subsequent event, Google remedies | Text conversion; unaudited | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-05-06_a991-earningsq12026.htm.jsonl | Medium: issuer press release | Quarter ended March 31, 2026 | Same | Adjusted EBITDA with prior-year comparative | Non-GAAP, unaudited | CP-1 |
| S6 | EX-99.1_2026-08-05_a991-earningsq22026.htm.jsonl | Medium: issuer press release | Three and six months ended June 30, 2026 | Same | Adjusted EBITDA with comparatives | Non-GAAP, unaudited | CP-1 |
| S7 | EX-99.1_2026-11-04_a991-earningsq32026.htm.jsonl | Medium: issuer press release | Three and nine months ended September 30, 2026 | Same | Adjusted EBITDA reconciliation, guidance, measure definitions | Non-GAAP, unaudited; management narrative | CP-1, CP-1A, CP-2 |
| S8 | context | Run settings, not issuer evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency, blank valuation and ratings fields | Not issuer evidence | All modules |

Module status: Ready with Limitations (all four handoffs present and accepted; credit agreement and proxy not supplied). Traceability scope: Top 5. Entity key: issuer_id mgni available.

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Low leverage on issuer Adjusted EBITDA: 1.27x gross, -0.13x net at LTM September 30, 2026; 1.81x gross on operating income plus D&A | CP-1, CP-2 | Principal 357,730; cash 392,862; LTM Adjusted EBITDA 280,586 (US$ thousands) | Sets default risk and leverage tolerance | Anchors the fundamental view | S4 p17, p2; S1 p100; S7 p13 | Adjusted EBITDA adds back stock compensation; LTM is derived |
| 2 | Single secured term loan; convertible notes repaid March 2026; no maturity wall before 2029 | CP-1, CP-1A, CP-2 | Term loan maturing February 2031, revolver February 2029, notes repaid with cash | Defines refinancing risk and debt service | Shows simple structure | S4 p14, p17, p19 | Only the filings' description of the credit agreement |
| 3 | Liquidity: cash plus undrawn revolver of 170.9 million | CP-1, CP-2 | Cash 392,862; availability net of 4.1 million letters of credit; no draw at quarter ends | Determines near-term solvency buffer | Supports the liquidity view | S4 p2, p20, p50 | Part of cash is publisher and customer float |
| 4 | Springing First Lien Net Leverage covenant, untested at September 30, 2026 | CP-1, CP-2 | 3.25 to 1.00, tested only above 35% revolver utilization; no revolver amount outstanding | Governs default trigger and lender control | Remoteness of covenant pressure | S4 p20 | No reported ratio, definitions or agreement text |
| 5 | Buyer concentration and seller payables create cash-float risk | CP-1A, CP-2 | Two buyers 40% and 12% of receivables at December 31, 2025; obligation to pay sellers on buyer default | Can move cash faster than earnings | Qualifies net cash | S1 p137; S4 p51, p2 | Float size and buyer identities not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.27x gross and -0.13x net leverage; 1.81x stricter base | CP-1, CP-2 | Principal, cash and LTM EBITDA inputs reproduced by script from S4 p17, p2 and S1 p100, S7 p13 | Yes | High, with Medium for the non-GAAP EBITDA | Calculated | Supported | High | Committee-Ready |
| Single term loan; notes repaid; maturities 2029 and 2031 | CP-1, CP-1A, CP-2 | "On March 15, 2026, the Convertible Senior Notes matured" (S4 p14); maturity table (S4 p17) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Cash 392,862 and availability 170.9 million | CP-1, CP-2 | Balance sheet (S4 p2); "$170.9 million, net of letters of credit outstanding in the amount of $4.1 million" (S4 p20) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Springing covenant at 3.25 to 1.00 and 35% trigger, untested at quarter end | CP-1, CP-2 | "springing financial covenant" text (S4 p20) | Yes | High for the description; no agreement | Directly Sourced | Supported as description only | Medium | Remediation Needed |
| Cash is partly float; net cash is a point-in-time figure | CP-1, CP-1A, CP-2 | Concentration (S1 p137); obligation to pay sellers (S4 p51); payables and receivables (S4 p2); negative first-quarter operating cash flow (S2 p47) | Yes | High facts, inference on size | Analyst Inference | Partly supported; size unquantified | Medium | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal 357,730 and carrying 349,950 at September 30, 2026 | runs/cpos-swarm-20261105-mgni/source-text | 10-Q_2026-09-30_mgni-20260930.htm.jsonl | S4 | page:17, Note 9 debt | CP-1 chart and metrics | Sourced | High | Carrying equals principal less discount and costs; tie-out passes |
| Maturities 908, 3,632 four times, 342,294 | same | same | S4 | page:17 | CP-1 maturities | Sourced | High | Sum equals principal |
| Cash 392,862; payables 1,738,299; receivables 1,432,233 | same | same | S4 | page:2 balance sheet | CP-1, CP-1A | Sourced | High | None |
| Availability 170.9 million net of 4.1 million letters of credit; covenant text | same | same | S4 | page:20 | CP-1, CP-2 | Sourced | High | Description only |
| Convertible notes matured and repaid 205.1 million | same | same | S4 | page:14 and page:18 | CP-1, CP-1A | Sourced | High | Cash flow shows 205,067 on page:5 |
| FY2025 Adjusted EBITDA 232,131 and FY2024 196,850 | same | 10-K_2025-12-31_mgni-20251231.htm.jsonl | S1 | page:100 reconciliation | CP-1 | Sourced | High for reconciliation, Medium as non-GAAP | Bridge to operating income ties |
| Nine months Adjusted EBITDA 196,817 and 148,362 | same | EX-99.1_2026-11-04_a991-earningsq32026.htm.jsonl | S7 | page:13 | CP-1 | Sourced | Medium | Quarters sum to nine months |
| Q1 and Q2 Adjusted EBITDA with 2025 comparatives | same | S5 page:11; S6 page:12 | S5, S6 | page:11; page:12 | CP-1 | Sourced | Medium | Used in LTM Q1 and Q2 |
| Cash paid for interest 28,159 FY2025; 19,064 and 21,674 nine months | same | S1; S4 | S1, S4 | page:122; page:6 | CP-1 | Sourced | High | None |
| Two buyers 40% and 12% of receivables; one seller 27% of payables | same | 10-K_2025-12-31_mgni-20251231.htm.jsonl | S1 | page:137 concentration note | CP-1A, CP-2 | Sourced | High | December 31, 2025 date |
| Obligation to pay sellers if a buyer defaults | same | 10-Q_2026-09-30_mgni-20260930.htm.jsonl | S4 | page:51 | CP-2 | Sourced | High | Quoted in CP-2 |
| Take rate lower for CTV and reserve auctions | same | 10-K_2025-12-31_mgni-20251231.htm.jsonl | S1 | page:41 risk factor | CP-1A | Sourced | High | Management risk language |
| Google remedies opinion September 2026; appeal intended; expected positive impact | same | 10-Q_2026-09-30_mgni-20260930.htm.jsonl | S4 | page:36 | CP-1A | Sourced as management language | Medium | Impact is management's expectation |
| Amendment No. 3 dated October 7, 2026 | same | 10-Q_2026-09-30_mgni-20260930.htm.jsonl | S4 | page:29 and page:30, Note 13 | CP-1, CP-1A, CP-2 | Sourced | High | Subsequent event, not folded into balances |
| Streamrai acquisition completed September 2025 | same | 10-K_2025-12-31_mgni-20251231.htm.jsonl | S1 | page:15 | CP-1A | Sourced | High | Price not in chunks read; CP-1A pointer to a CP-1 line is wrong (QA-1) |
| Revolver trigger level 61,250 and 61% headroom indicator | not applicable | Derived in CP-2 | S4 | page:20 inputs | CP-2 | Calculated, with inference | Medium | Definitions unknown; labelled indicator only |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA Q3 2026 | CP-1, CP-2 | 232,131; 196,817; 148,362 | FY2025 + 9M 2026 - 9M 2025 = 280,586; period LTM to September 30, 2026; US$ thousands; recomputed equal | Calculated | Supported | High | Leverage, cover | S1 p100; S7 p13 |
| LTM Adjusted EBITDA Q1 and Q2 2026 | CP-1 | 42,861 and 36,800; 113,461 and 91,191 | 238,192 and 254,401; recomputed equal | Calculated | Supported | High | Leverage trend | S5 p11; S6 p12 |
| LTM cash paid for interest | CP-1 | 28,159; 19,064; 21,674 and Q1 and Q2 analogues | 25,549; 26,615; 27,768; recomputed equal | Calculated | Supported | High | Interest cover | S1 p122; S4 p6; S3 p5; S2 p5 |
| Total debt / LTM Adjusted EBITDA | CP-1, CP-2 | Principal 357,730; 359,546; 358,638 (S2 p15, S3 p15, S4 p17) | 1.27, 1.51, 1.41; FY2025 2.44; FY2024 2.89; recomputed equal | Calculated | Supported | High | Leverage | As stated |
| Net debt / LTM Adjusted EBITDA | CP-1, CP-2 | Principal less cash 392,862 | -35,132 / 280,586 = -0.13 (-0.1252 unrounded); recomputed equal | Calculated | Supported | High | Net leverage | S4 p17, p2 |
| Adjusted EBITDA / cash interest | CP-1, CP-2 | 280,586; 25,549 | 10.98; FY2025 8.24; FY2024 5.34; recomputed equal | Calculated | Supported | High | Debt service | As stated |
| Stricter base: income from operations plus D&A | CP-1, CP-2 | 141,446 and 56,421 LTM | 197,867; 357,730 / 197,867 = 1.81; recomputed equal | Calculated | Supported | High | Leverage after stock compensation | S1 p120, p121; S4 p3, p5 |
| Revolver trigger | CP-2 | 35% and 175,000 | 61,250; Q2 draw 60,000 is 34.3% | Calculated | Supported | High | Covenant test | S4 p19, p20 |
| Headroom indicator | CP-2 | 357,730; 3.25; 280,586 | 357,730 / 3.25 = 110,071; fall of 60.8%; ignores cash netting and covenant EBITDA | Assumption-Based | Indicator only | Low | Covenant remoteness | S4 p20 |
| FY2024 undrawn revolver | CP-1 | 175.0 million less 5.2 million lease letters of credit | 169.8; assumes the letters of credit sit on the revolver, as in FY2025 and 2026 | Assumption-Based | Labelled derived | Medium | Liquidity | S1 p158, p102 |
| Amendment No. 3 saving | CP-1, CP-2 | 357,730 and 0.50% | about 1,789 a year before Term SOFR changes | Calculated | Illustrative | Medium | Interest cost | S4 p29 |
| Liquidity components | CP-2 | 392,862 and 170,900 | 563,762, not netted for float | Calculated | Supported | Medium | Liquidity | S4 p2, p20 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Streamrai outflow small relative to balance sheet (CP-1A) | Cites "financial base handoff, acquisitions line"; CP-1 has no such line. The only source figure is the cash flow line "Mergers and acquisitions, net of indemnification claims holdback (8,100)" (S1 p121) | Weak Lineage | A reader following the pointer finds nothing; the fact is true in the source but not linked | State the source line in a later run | CP-1A transaction summary |
| MINOR | Business sections located at 10K p4 to p6, p12 (CP-0) | Pages 4 to 6 are the forward-looking and risk summary; the business description is p8 to p13 | Directly Sourced, locator imprecise | Locator hygiene only | Cite p8 to p13 | CP-0 consumer demand table |
| MINOR | No debt matures before February 2029 (CP-2) | The term loan amortizes 3,632 a year and 908 remains in 2026 (S4 p17), which CP-2 states elsewhere | Directly Sourced, wording imprecise | Overstates the absence of near-term payments, which are small | Say no refinancing maturity before 2029 | CP-2 credit view |
| MINOR | FY2024 undrawn revolver 169.8 (CP-1) | Derived from a lease letter of credit amount, not a printed availability | Analyst Inference | Small liquidity figure rests on an assumption | Labelled derived in CP-1; keep | CP-1 liquidity chart |
| MINOR | Convertible interest is small (CP-1 cover note) | No locator in the sentence; source shows 107 and 385 of contractual interest (S4 p18) | Directly Sourced, locator missing | Supports the cover comparison across periods | Add S4 p18 | CP-1 interest cover chart |
| MINOR | No financial sponsor or controlling holder (CP-1A view) | Stated more firmly than the table, which says none is named in the sources read; ownership detail is in an unsupplied proxy | Analyst Inference | Absence of evidence is not evidence of absence for control | Keep the table wording | CP-1A view |
| MINOR | SpotX financing dates (CP-1A timeline) | The timeline says the acquisition date is Not supplied, which is right, but omits dated financing events that are supplied: March 2021 convertible notes (S4 p18) and the April 30, 2021 credit agreement (S4 p19) | Directly Sourced, omission | Timeline completeness | Add the two dates | CP-1A transaction summary |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 and three 2026 quarters; no credit agreement, proxy, ratings or decks | Missing legal documents leave covenant and distribution capacity as description only | Covenant headroom stays unverified for committee use | Retrieve credit agreement exhibits and proxy |
| Citation completeness | Ready with Remediation | 80 quotations found in sources; seven minor locator or pointer defects (T5B.6) | Imprecise pointers slow a reviewer but do not change a figure | None for the credit view | Correct in a later run |
| Calculation traceability | Committee-Ready | All LTM, leverage, cover and tie-out figures recomputed equal from parsed source text | Reproducible inputs remove arithmetic risk | Leverage and cover can be relied on | None |
| Assumption transparency | Committee-Ready | Derived items (FY2024 undrawn, headroom indicator, Q4 2025) are labelled in the handoffs | Labelled assumptions limit overstatement | Indicator not read as covenant figure | Keep labels |
| Markdown and export artifact integrity | Committee-Ready | All four handoffs accepted with required headings, tables and hashes | Structure checks passed; semantic quality is checked here | None | None |

Overall auditability (lowest of the five): Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed credit agreement, amendments and covenant definitions not supplied | 2024 Credit Agreement and Amendments No. 1 to 3 (10-K exhibit index S1 p179 to p182) | Covenant definitions and baskets decide headroom and distribution capacity | Covenant and legal-capacity statements are description only | High impact on confidence in covenant view | EDGAR exhibits |
| CP-5-GAP-002 | Reported First Lien Net Leverage Ratio and headroom not supplied | Compliance certificate or filing figure | A computed headroom would be a guess | Headroom indicator is labelled only | Medium impact | Credit agreement and compliance certificate |
| CP-5-GAP-003 | Free cash versus customer and publisher float not supplied | Working-capital split of cash | Overstated liquidity if float is large | Liquidity treated as upper bound | Medium impact | Company disclosure or call |
| CP-5-GAP-004 | Ownership percentages, guarantor names and board control detail | Proxy statement, Exhibit 21 | Control and guarantee structure | CP-1A ownership rows are Insufficient Information | Low impact | Proxy and Exhibit 21 |
| CP-5-GAP-005 | Contract terms with demand platforms and large sellers | Master service agreements | Revenue visibility and termination risk | Revenue durability not testable | Medium impact | Not available from filings |
| CP-5-GAP-006 | Ratings, market prices, peers | Context fields blank | Relative value outside scope | No market claim is made | Low impact for this set | Rating agency and market data |
| CP-5-GAP-007 | Discrete Q4 2025 and events from November 5, 2026 | No Q4 2025 release; nothing dated after November 4, 2026 | Seasonality and recent events | Q4 2025 only derivable by subtraction | Low impact | Q4 2025 release |
| CP-5-GAP-008 | Independent review | Same author for all modules | Self-review misses omissions | Committee status Draft Only | Medium impact | A second reviewer |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / mgni-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with one MINOR locator finding | All consumers READY_WITH_LIMITATIONS |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, leverage, cover, liquidity, maturities | High | Six headings; accepted | Passed with two MINOR findings | Metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, concentration, timeline, governance | High | Six headings; accepted | Passed with three MINOR findings | Pointer and omission defects |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with one MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A | Streamrai outflow small | Partially Supported | Pointer to a CP-1 line that does not exist; source line exists in S1 p121 | Cite S1 p121 | None |
| MINOR | CP-1A | SpotX financing timeline | Supported | Dated 2021 financing events supplied but not listed | Add the March 2021 and April 30, 2021 dates | None |
| MINOR | CP-1A | No financial sponsor | Partially Supported | Absence of a named sponsor stated as absence of a sponsor | Keep the table wording | None |
| MINOR | CP-1 | Convertible interest small | Supported | No locator in the sentence | Cite S4 p18 | None |
| MINOR | CP-0 | Business section locators | Supported | Page range points to risk summary | Cite p8 to p13 | None |
| MINOR | CP-2 | No debt matures before 2029 | Supported | Omits small scheduled amortization | Reword | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Adjusted EBITDA as leverage denominator | Issuer non-GAAP measure adds back stock compensation; both modules show the stricter base beside it | None | Keep both bases | None |
| MINOR | CP-1 | Release operating cash flow versus statement cash flow | Release defines operating cash flow as Adjusted EBITDA less capital expenditures (S7 p2); the statement reports net cash provided by operating activities | Definition difference, not a value conflict | Keep the labels used in CP-1 | None |
| MINOR | CP-2 | Headroom indicator | Gross term loan leverage over unadjusted LTM EBITDA, not the covenant ratio | None | Keep labelled as an indicator | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-1A, CP-2 | Springing covenant at 3.25 to 1.00 above 35% utilization; security over substantially all assets; guarantors | Executed 2024 Credit Agreement and amendments | Description in filings only | Supply the agreement | Needed before any headroom or capacity statement |
| MINOR | CP-1, CP-2 | Amendment No. 3 margins | Executed Amendment No. 3 | Description in S4 p29 only | Supply the amendment | Not needed for the credit view |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; no peer ranking or instrument recommendation appears | Prices, spreads, ratings | Outside the minimum source pack | Add market data only with sourced inputs | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | CP-2 figures (357,730; 392,862; 1.27x; 1.81x; 10.98x; 61,250; 1,789) all match CP-1 or its stated calculation; no conflict | CP-2 cites CP-1 hash cf0ec312 and CP-1A hash b1efedae; versions current | None | None |
| MINOR | CP-0, CP-1 | CP-0 stated that Q1 and Q2 statements were assessed only at register level; CP-1 added the locators | CP-1 adds to CP-0 and corrects nothing | None | None |
| MINOR | CP-1A, CP-2 | CP-2 says no pension, factoring or consent-decree obligation found in sections read; a full-text search of all seven sources in this check found none (only a 2023 finance lease repayment line, S1 p122) | CP-2 wording is now confirmed | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Financial base is traceable; covenant and legal capacity are not verifiable; review is by the same author | Supply credit agreement; independent review | Committee status Draft Only |
| MINOR | CP-1, release | Duplication | The releases repeat the 10-Q statements and are not counted as corroboration | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | All | Required headings, tables, hashes and reader summaries | No structural defect beyond QA-1 to QA-7; no module codes or hashes in the four reader summaries; word limits met | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-1A | Citation | Streamrai pointer to a non-existent CP-1 line | Cite S1 p121 | None | Open |
| QA-2 | MINOR | CP-0 | Locator | Business locators point to the risk summary | Cite p8 to p13 | None | Open |
| QA-3 | MINOR | CP-2 | Wording | No debt matures before 2029 omits small amortization | Reword | None | Open |
| QA-4 | MINOR | CP-1 | Derivation | FY2024 undrawn revolver derived | Keep label | None | Open |
| QA-5 | MINOR | CP-1 | Locator | Convertible interest sentence without locator | Cite S4 p18 | None | Open |
| QA-6 | MINOR | CP-1A | Wording | Sponsor absence stated firmly | Keep table wording | None | Open |
| QA-7 | MINOR | CP-1A | Omission | 2021 financing dates not listed | Add dates | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted phrase in the four handoffs searched in the pinned source chunks; locator pages checked for CP-0 and CP-1A | 84 spans parsed; 4 were parser artifacts; of 80 quotations none is misquoted and all are on the cited source |
| Q2 | Metric recomputation | Inputs parsed from the source chunks by a script, not retyped; LTM, leverage, cover and the stricter base recomputed | All equal: LTM Adjusted EBITDA 238,192, 254,401, 280,586; LTM cash interest 27,768, 26,615, 25,549; leverage 1.51, 1.41, 1.27; cover 8.58, 9.56, 10.98; stricter base 197,867 and 1.81 |
| Q3 | Tie-outs | 16 sums re-added: quarter sums to nine months for revenue and Adjusted EBITDA, maturity table to principal, FY2025 principal, revolver availability, three Adjusted EBITDA bridges to operating income, D&A parts, carrying value, channel and Contribution ex-TAC totals | 16 of 16 equal |
| Q4 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:3,Calculated:1,Analyst Inference:1" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:7` | score = clamp((0.6 x 86 + 0.4 x 100) x 0.7 - 21) = 43.12, rounded to 43; band Low; qa_status Passed |

## Gaps

- G1 Material to covenant use: the executed credit agreement and covenant definitions are not supplied (CP-5-GAP-001, -002).
- G2: cash float and buyer identities are not supplied (CP-5-GAP-003).
- G3: ownership, guarantors, ratings, contract terms and discrete Q4 2025 are not supplied (CP-5-GAP-004 to -007).
- G4: this is a self-review by the author of all four handoffs; an independent check should start with omissions (CP-5-GAP-008).
- G5: seven minor defects are open because accepted handoffs cannot be edited.

## Next module

- Report delivery: carry qa_status Passed, Confidence Score 43 (Low), committee status Draft Only, and gap G1.
- Independent review: a second analyst should repeat the quotation and recomputation checks and look for omissions, for example other 10-K sections on commitments and leases.
- Sourcing: fetch the credit agreement and amendments, Exhibit 21 and the proxy statement from EDGAR, then rerun in a new run folder.
