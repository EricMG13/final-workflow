## Request

- Issuer: PRECISION DRILLING Corp (issuer id pds), as of 2026-11-05, evidence cutoff 2026-11-05. Run `pds-2026-11-05-credit_snapshot-host`, pathway credit_snapshot, minimum module set, reporting currency CAD.
- Scope: CP-5 checks the four accepted handoffs (CP-0, CP-1, CP-1A, CP-2) against the pinned filings and grades the result (absorbed CP-5A phase). Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- QA envelope: `qa_status` Passed; Confidence Score 46, band Low (computed with `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 |
| --- | --- |
| 40-F_2025-12-31_pds-20251231.htm.jsonl | 370dd908e02517a9c6fdef15ebd1f7cb116b5559c399f640ba611cac38448995 |
| 6-K-EX-99.1_2026-03-31_exh_991.htm.jsonl | dea56c7134da9a355171c554a1de2c864262ee500671edb8950e5a8046055900 |
| 6-K-EX-99.1_2026-07-28_exh_991.htm.jsonl | 36192463cc83167a35ad5734c404a3c626d50b0ad4594b8a7f2194bea3a8cff9 |
| 6-K-EX-99.1_2026-10-27_exh_991.htm.jsonl | fee608b6431a2965784fc76b2de265f5506a117164e5844d50a088bea40f38a4 |
| 6-K-EX-99.2_2026-03-31_exh_992.htm.jsonl | d96a5e5808d43b7099d6d8e58ef62238fb3bf3aa05ae6b50ff5d6edaea1184fb |
| 6-K-EX-99.2_2026-06-30_exh_992.htm.jsonl | d0dc4f680eda414a6085125595dd65a3350a1093a614c44804e7f758bd709179 |
| 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | 2be96c22c1511c1bfacc2dbbfc1299a96c6051c24999485cd2efd4fef772c85e |

The run context (sha256 f0dfb9848210a0a45d246b6d35647f4b02f9221b88bb774a3f1ed2c749bd4a06) supplies identity and dates only; it is not issuer evidence.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 49f6e9db4a704d9d945403e846ab65374ee34682a74a406c40b71660295ca903 |
| CP-1 | f1af7a3c0eb1d39669e5863733ef0479a3a5abea685533a4b39052fc3d180876 |
| CP-1A | e397a83de0bb84677861884814e4412334228c42bc17691d1608e23067b4bf77 |
| CP-2 | 599fb06a102d8ff715cafe2551bec2f4b070d48982968765d419a5c6c93a33eb |

Locators use the source keys of the handoffs: F40 is the annual report cover; R1, R2 and R3 are the Q1, Q2 and Q3 2026 management reports; S1, S2 and S3 are the Q1, Q2 and Q3 2026 statements. A page is the extraction chunk, not a printed page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four analyses trace to the filings: all 22 quotations are verbatim, all 223 statement figures tie, and all 58 recomputed values match. Four minor findings are open. | Medium | The debt agreements and audited annual statements are not supplied, and the host reviewed its own work, so covenant headroom and legal terms remain unverified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every checked figure and quotation traces to a cited page; no misquotation and no unsupported number was found. | The reported leverage, liquidity, cash flow and covenant figures can be relied on as stated in the filings. | High |
| Covenant headroom, guarantors, security and distribution capacity rest on summary disclosure only. | The strongest credit protections cannot be verified until the credit agreement and indenture are supplied. | High |
| Four minor wording and labelling issues remain in the credit synthesis and the business context. | None changes a conclusion; they affect precision of attribution and conflict logging. | High |
| This review was done by the same host that wrote the handoffs. | Shared blind spots could remain, so an independent check is advised before committee use. | Medium |

### Evidence trace view

The four handoffs are traceable enough to support the current-quarter credit view of Precision Drilling, but not a committee-ready view of its legal structure. Every checked quotation sits in its cited source, every cited page exists, all 223 statement figures tie to the filings, and all 58 recomputed values equal the handoff figures. Of the 16 material claims, 6 are directly sourced, 5 calculated, 2 analyst inferences and 3 flagged as insufficient information. The critical provenance gap is the absence of the debt agreements and the audited annual statements, which leaves covenant headroom, guarantors and distribution capacity unverified. Four minor findings are open, and the review is a self-review by the host that wrote the handoffs.

### Traceability summary

| Check | Result |
| --- | --- |
| Quotations checked against the sources | 22 of 22 found verbatim |
| Page locators opened | 173 of 173 exist |
| CP-1 statement figures tied to the filings | 223 of 223 found |
| Calculation rows recomputed from the sources | 44 rows, 58 values, all equal |
| Material claims by lineage | 6 Directly Sourced, 5 Calculated, 2 Analyst Inference, 3 Insufficient Information |
| Open findings | 4 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F40 | 40-F_2025-12-31_pds-20251231.htm.jsonl | High: filed annual report cover | Fiscal year ended December 31, 2025 | PRECISION DRILLING CORPORATION, registrant | Identity, share count, auditor, exhibit list | Cover only; exhibits not supplied | CP-0, CP-1A |
| R1 | 6-K-EX-99.1_2026-03-31_exh_991.htm.jsonl | Medium: issuer management report | Three months ended March 31, 2026 | Consolidated, two segments | Operating KPIs, liquidity, covenants, outlook | Management commentary; no statements | CP-0, CP-1, CP-1A |
| R2 | 6-K-EX-99.1_2026-07-28_exh_991.htm.jsonl | Medium: issuer press release | Three and six months ended June 30, 2026 | Consolidated, two segments | Results, strategy, embedded statements | No notes, liquidity table or covenant table | CP-0, CP-1, CP-1A |
| R3 | 6-K-EX-99.1_2026-10-27_exh_991.htm.jsonl | Medium: issuer management report | Three and nine months ended September 30, 2026 | Consolidated, two segments | Results, liquidity, covenants, contingency, quarterly summary | Management commentary; non-IFRS measures | CP-0, CP-1, CP-1A, CP-2 |
| S1 | 6-K-EX-99.2_2026-03-31_exh_992.htm.jsonl | High: filed unaudited interim statements | Quarter ended March 31, 2026 | Consolidated | Statements, debt note, covenants | Unaudited | CP-0, CP-1 |
| S2 | 6-K-EX-99.2_2026-06-30_exh_992.htm.jsonl | High: filed unaudited interim statements | Six months ended June 30, 2026 | Consolidated | Statements, debt note, covenants | Unaudited | CP-0, CP-1 |
| S3 | 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | High: filed unaudited interim statements | Nine months ended September 30, 2026 | Consolidated | Statements, notes, contingency | Unaudited | CP-0, CP-1, CP-1A |
| CTX | context | User settings, not evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Moderate, stable leverage of 1.28x net and 1.33x total debt to LTM Adjusted EBITDA | CP-1, CP-2 | Quarterly summary and balance sheets | Sets leverage tolerance and the debt service base | Core leverage metric | R3 page:14; S3 page:1; S2 page:1; S1 page:1 | LTM and FY2025 assembled from quarters; unaudited |
| 2 | Free cash flow of CAD 55.7 million for nine months against CAD 104.7 million, below capital allocation | CP-1, CP-2 | Cash flow statement | Cash fell while repayments and buybacks continued | Cash generation and deleveraging capacity | S3 page:2; S3 page:3 | Q4 2025 flows not supplied |
| 3 | Liquidity of CAD 462.5 million, revolver-dependent, with cash of CAD 23.2 million | CP-1, CP-2 | Liquidity table and balance sheet | Near-term default risk | Monitoring horizon | R3 page:4; R3 page:12; R3 page:13; S3 page:1 | Facility tables missing for two dates |
| 4 | Refinancing concentrated in 2028 and 2029 | CP-1, CP-2 | Debt note and liquidity table | Window for market access | Refinancing risk | S3 page:9; R3 page:12; R3 page:13 | Redemption terms not supplied |
| 5 | Contested Canada Revenue Agency reassessment of about CAD 155 million excluding interest | CP-1, CP-2 | Contingency note | Possible cash call ahead of resolution | Liquidity and tax risk | S3 page:12; S3 page:13; R3 page:12 | Outcome and timing unknown |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reported statement lines (balance sheet, earnings, cash flow) | CP-1 | S1, S2, S3 page:1 to page:3 | Yes | High | Directly Sourced | Supported | High | Traced, 223 of 223 figures found |
| Covenant ratios of 0.14x and 10.27x | CP-1, CP-2 | R3 page:13; S3 page:9 | Yes | High; issuer statement | Directly Sourced | Supported as a statement | Medium | Traced |
| Debt instruments, maturities and carrying values | CP-1, CP-2 | S3 page:8 and page:9; R3 page:12 and page:13 | Yes | High | Directly Sourced | Supported | High | Traced |
| Contingent tax matter, maximum about CAD 155 million | CP-1, CP-2 | S3 page:12; R3 page:12 | Yes | High | Directly Sourced | Supported | High | Traced |
| Term contract coverage and international contracts | CP-1A, CP-2 | R3 page:7 and page:8; R1 page:8 | Yes | Medium; management report | Directly Sourced | Supported as management statements | Medium | Traced |
| LTM Adjusted EBITDA and leverage ratios | CP-1 | R3 page:14 with balance sheets | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Interest cover of 7.44x and 6.03x | CP-1, CP-2 | S3 page:2 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Free cash flow and use of cash | CP-1, CP-2 | S3 page:2 and page:3 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Liquidity recomputation of CAD 462.5 million | CP-1, CP-2 | R3 page:12 and page:13 with closing rate on R3 page:13 | Yes | High inputs; rounded rate | Calculated | Supported within rounding | Medium | Recomputed equal |
| Half-payment cash call of about CAD 77.5 million | CP-1, CP-2 | S3 page:12 and page:13 | Yes | High inputs | Calculated | Supported as an upper bound under stated assumptions | Medium | Recomputed equal |
| Semi-annual coupon timing explains uneven interest paid | CP-1 | S1 page:2; S2 page:2; S3 page:2 | Yes | Pattern only | Analyst Inference | Labelled as inference in the handoff | Low | Correctly labelled |
| Fundamental credit view of CP-2 | CP-2 | CP-1 and CP-1A rows | Yes | Upstream handoffs | Analyst Inference | Supported by cited rows | Medium | Traced to upstream rows |
| No transaction, sponsor or new debt issue | CP-1A | All sources searched | Absence of evidence | Not available in the set | Insufficient Information | Open gap, correctly labelled | Low | Gap correctly labelled |
| Ownership, control and customer concentration | CP-1A, CP-2 | No source in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap, correctly labelled | Low | Gap correctly labelled |
| Covenant headroom verification | CP-1, CP-2 | Covenant EBITDA definition not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap, correctly labelled | Low | Gap correctly labelled |
| Fourth-quarter margin step change in the United States | CP-1A, CP-2 | R3 page:7 | Yes | Medium; management guidance | Directly Sourced | Attributed claim, not adopted | Medium | Traced as Management Language |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue Q3 2026 531,652 | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | S3 | page:1, statement of net earnings | CP-1 earnings table | Reported | High | Matches |
| Long-term debt 629,116 and cash 23,177 | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | S3 | page:1, financial position; page:9, Note 5 | CP-1 debt and liquidity | Reported | High | Matches; reconciliation re-added equal |
| Quarterly revenue and Adjusted EBITDA, eight quarters | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.1_2026-10-27_exh_991.htm.jsonl | R3 | page:14, quarterly financial summary | CP-1 LTM bases | Reported | Medium | Parsed from the source and recomputed |
| Covenant 0.14 and 10.27 | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | S3 | page:9, Note 5(a) | CP-1 covenant table | Reported | High | Matches R3 page:13 |
| Revolver US$375 million, October 31, 2028, and notes due January 15, 2029 | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.1_2026-10-27_exh_991.htm.jsonl | R3 | page:12 and page:13, liquidity | CP-1 debt table | Reported | Medium | Matches |
| Interest paid 46,525 and 60,245 | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | S3 | page:2, cash flows | CP-1 interest cover | Reported | High | Matches |
| Maximum tax liability about CAD 155 million | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | S3 | page:12, Note 12 | CP-1 and CP-2 contingency | Reported | High | Matches R3 page:12 |
| Average rigs under term contract 54 and 40 | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.1_2026-10-27_exh_991.htm.jsonl | R3 | page:8, contracts | CP-1 KPIs; CP-1A | Reported | Medium | Matches |
| Term-contracted share of days 26% and 34% | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.1_2026-03-31_exh_991.htm.jsonl | R1 | page:8, segment review | CP-1A operating model | Reported | Medium | Matches |
| Canada about 59% of nine-month revenue | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | S3 | page:7, Note 3(b) | CP-1A operating model | Reported | High | Matches |
| Auditor named in the annual report and in the interim reports | runs/cpos-swarm-20261105-pds/source-text | 40-F_2025-12-31_pds-20251231.htm.jsonl | F40 | page:2; S3 page:13 | CP-0, CP-1A conflicts | Reported | High | Conflict logged, not reconciled |
| Foreign exchange adjustment on debt 22,896 | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | S3 | page:9, Note 5 movement | CP-1 and CP-2 | Reported | High | Reconciliation re-added equal |
| Shares outstanding 12,538,736 and 12,585,648 | runs/cpos-swarm-20261105-pds/source-text | 6-K-EX-99.1_2026-10-27_exh_991.htm.jsonl | R3 | page:14; S3 page:10 | CP-1A profile | Reported | High | Matches |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM revenue, Adjusted EBITDA, cash from operations and net earnings at four dates | CP-1 financials table; CP-2 | Eight quarterly rows | Sum of four consecutive quarters | Recomputed from parsed source rows: equal | Supported | High | Base of every ratio | R3 page:14 |
| Total and net debt to LTM Adjusted EBITDA | CP-1 chart table; CP-2 | Long-term debt less cash; LTM Adjusted EBITDA | Debt divided by EBITDA | Recomputed: 1.33x and 1.28x equal; other dates equal | Supported | High | Leverage tolerance | S3 page:1; S2 page:1; S1 page:1; R3 page:14 |
| Interest cover | CP-1; CP-2 | Nine-month Adjusted EBITDA and interest paid | EBITDA divided by interest paid | Recomputed: 7.44x and 6.03x equal | Supported | High | Debt service | S3 page:1; S3 page:2 |
| Free cash flow | CP-1; CP-2 | Cash from operations less purchases of property, plant and equipment | Subtraction | Recomputed: 55,690 and 104,719 equal | Supported | High | Cash generation | S3 page:2 |
| Liquidity | CP-1; CP-2 | Cash, revolver, letters of credit, operating facilities, rounded closing rate | Sum of cash and undrawn availability | Recomputed: 462.5 and 431.5 equal | Supported within rounding | Medium | Liquidity adequacy | R3 page:12; R3 page:13; R1 page:9 |
| Sensitivities and ratios in CP-2 | CP-2 | Principal, blended rate, trough quarter | Quotients as stated | Recomputed: all equal; labelled as analyst references | Supported | Medium | Stress context | R3 page:13; R3 page:14 |
| Market capitalization and equity cushion | CP-1A; CP-2 | Shares outstanding and Toronto close | Product; quotient | Recomputed: equal; closing-date assumption stated | Supported with assumption | Medium | Equity cushion | S3 page:10; S3 page:13 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial source gate, 4 MINOR | Script formula | 46, band Low | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 key finding on liquidity | A figure of about CAD 382 million of undrawn revolver is attributed to CP-1 but is derived in CP-2 from the CP-1 inputs | Restated figure | A reader looking for the figure in CP-1 will not find it; the inputs are there | Reference the CP-2 calculation or add the figure to CP-1 | CP-2 handoff |
| MINOR | CP-2 strengths list | Improved coverage is attributed to lower debt; interest paid fell by more than interest expense on long-term debt, so timing also contributes | Causal attribution | Overstates one driver of the improvement | State interest expense and interest paid separately | CP-2 handoff |
| MINOR | CP-1 and CP-2 target comparison | The calculated 1.28x net leverage is described as above the issuer's own target of below 1.0x; the issuer's ratio value and period basis are not printed | Comparison basis unverified | Comparison may differ on the issuer's basis | Label as a comparison to the target level | CP-1, CP-2 handoffs |
| MINOR | CP-1A conflicts table | Service rig counts differ across sources and labels (end of period or registered) and are not logged as a conflict | Unlogged inconsistency | Counts of 145, 146 and 150 for 2026 and 143, 135 and 148 for the 2025 comparatives are not on one basis | Log the label change in a later run | CP-1A handoff |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; hashes in all four handoffs match the pinned files | A wrong document would change every figure | No effect found | No action |
| Locator precision | Strong | 173 of 173 page locators exist; 22 of 22 quotations verbatim; row-level figures found on the cited pages except calculated values | A wrong page slows verification | No effect on conclusions | No action |
| Calculation reproducibility | Strong | 58 values in 44 rows recomputed equal from parsed source rows | Calculation errors would move leverage and liquidity | No effect found | No action |
| Cross-module consistency | Strong | CP-1A and CP-2 use CP-1 figures unchanged except the minor restatement noted | Inconsistent figures mislead a committee | No effect on conclusions | Keep figure references exact |
| Legal and covenant verification | Weak | No debt agreement is supplied; covenant EBITDA is undisclosed | Headroom and distribution capacity cannot be tested | Limits conviction on structure | Supply credit agreement and indenture |
| Reviewer independence | Weak | The host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Debt agreements | Credit agreement, amendments and note indenture | Covenant EBITDA, guarantors, security, restricted payments and redemption terms unknown | CP-1 covenant table, CP-2 structure and distribution view | Caps committee status | Credit agreement and indenture |
| G2 | Audited FY2025 statements and annual MD&A | 40-F exhibits | FY2025 flows, Q4 2025 interest paid and capital expenditure, cause of the Q4 2025 loss | LTM cash interest and LTM free cash flow not calculable | Lowers confidence in annual trends | 40-F exhibits 99.1 to 99.3 |
| G3 | Ownership, control, customers | Annual information form, proxy circular | Sponsor alignment and concentration not assessable | CP-1A and CP-2 business risk | Moderate | Annual information form |
| G4 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |
| G5 | Revenue visibility after Q1 2026 | Term-contracted share of days for later quarters | Current contract cover unknown | CP-1A operating model | Moderate | Later management reports or calls |
| G6 | Auditor identity | Audit report and consent | Governance question carried from CP-0 | CP-1A profile | Low | 40-F exhibit 23.1 and 99.3 |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / pds-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed | READY_WITH_LIMITATIONS for all consumers; all quotations found |
| CP-1 | requests/CP-1 attempt 2 / same run | Statements, LTM, debt, liquidity, covenants, cash flow | High | Six headings; attempt 1 refused because three summary numbers were not in the body; attempt 2 accepted | Passed with one open MINOR finding (shared with CP-2) and one closed | All metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, ownership, behaviour, conflicts | High | Six headings; accepted | Passed with one MINOR finding | Management Language rows labelled |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with three MINOR findings | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Undrawn revolver of about CAD 382 million | Supported | Attributed to CP-1 but derived in CP-2 | Reference the CP-2 calculation | No effect on clearance |
| MINOR | CP-1A | Service rig fleet of 150 registered rigs | Supported | Other reports give different counts on a different label | Log the label change | No effect on clearance |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Coverage improvement attributed to lower debt | Interest paid fell by 22.8%; interest expense on long-term debt fell by 16.7% (S3 page:9) | Timing of payments contributes | State both measures | No effect on clearance |
| MINOR | CP-1, CP-2 | Comparison of 1.28x to the issuer target of below 1.0x | Issuer ratio value and basis not printed | No value conflict | Label as comparison to the target level | No effect on clearance |
| MINOR | CP-1 | Adjusted EBITDA used as the leverage denominator | After cash-settled share-based compensation; excludes disposal gains; covenant EBITDA undisclosed | Definitions differ and are labelled | Keep labels, as CP-1 does | No effect on clearance |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-2 | Covenant headroom and notes incurrence test | Credit agreement and indenture | Documents not supplied; claims correctly labelled as reported figures and descriptions | Supply the agreements | Required before any statement on headroom |
| MATERIAL as a gap, not a defect | CP-1A, CP-2 | Distribution capacity, guarantors and security | Credit agreement, indenture, security documents | Not supplied; correctly marked Insufficient Information | Supply the documents; add legal modules | Required before any structure view |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; the market capitalization calculation uses a filing-reported close | Bond prices, spreads and ratings | Outside the minimum source pack by design | Add sourced market data in a later run | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A | Service rig counts differ across the Q1, Q2 and Q3 reports and labels | CP-1A cites the Q3 count only | Log the label change | No effect on conclusions |
| MINOR | CP-1, CP-2 | CP-2 cites accepted CP-1 attempt 2 and CP-1A attempt 1 by hash; the refused CP-1 attempt 1 is not used | No version conflict | Keep citing the accepted hashes | No effect |
| MINOR | CP-0, CP-1A | The auditor-name conflict and the Q2 2026 per-share anomaly are carried consistently | No version conflict | Obtain the audit report | No effect on conclusions |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | The financial base is traceable; covenant, structure and distribution views are not; review is a self-review | Supply the debt agreements and an independent review | Committee status Requires More Work |
| MINOR | CP-1, R2 | Duplication | The Q2 release repeats the Q2 statements; CP-0 and CP-1 treat the statements exhibit as controlling and do not count the release as corroboration | No fix needed | No effect |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Reader summary, attempt 1 | Three summary numbers written in millions were not present in the body; refused by the adapter | Repaired in attempt 2 by stating the same figures in the calculation table | Resolved; attempt 2 accepted |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-2 | Restatement | Undrawn revolver of about CAD 382 million attributed to CP-1 but derived in CP-2 | Reference the derivation | No effect on clearance | Open |
| QA-2 | MINOR | CP-2 | Causal attribution | Coverage improvement attributed to lower debt; timing also contributes | State both measures | No effect on clearance | Open |
| QA-3 | MINOR | CP-1, CP-2 | Comparison basis | Comparison to the issuer target level rests on an unprinted basis | Label the comparison | No effect on clearance | Open |
| QA-4 | MINOR | CP-1A | Conflict logging | Service rig count labels differ across reports and are not logged | Log in a later run | No effect on clearance | Open |
| QA-5 | MINOR | CP-1 | Export | Reader summary numbers missing from body in attempt 1 | Repaired in attempt 2 | No effect on clearance | Closed |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each backtick quotation in the four handoffs searched in the pinned source text with whitespace normalised | 22 quotations, 22 found verbatim |
| Q2 | Locator trace | Each `page:N` locator in the four handoffs checked to exist in the named source; CP-1, CP-1A and CP-2 rows with figures checked for the figure on the cited pages | 173 locators, all exist; the only figures not found on cited pages are calculated values |
| Q3 | Statement tie-out | Every comma-separated figure in the CP-1 statement tables searched in the pinned text | 223 of 223 found |
| Q4 | Metric recomputation | Quarterly rows and balance sheet lines parsed from the sources; LTM sums, net debt, leverage, interest cover, free cash flow, liquidity, covenant headroom, debt reconciliation, market capitalization and CP-2 sensitivities recomputed and compared with the printed results | 44 calculation rows, 58 values, all equal within the printed rounding |
| Q5 | Hash check | sha256 of each pinned file, of the context file and of each accepted handoff recomputed and compared with the hash printed in the handoffs and by the launcher | All equal |
| Q6 | Confidence Score | `confidence_score.py` with lineage 6 Directly Sourced, 5 Calculated, 2 Analyst Inference, 3 Insufficient Information; fields 17 of 17; source gate partial; findings 4 MINOR | score = clamp((0.6 x 70.62 + 0.4 x 100) x 0.7 - 12, 0, 100) = 45.66, rounded 46; band Low; qa_status Passed |
| Q7 | Interest paid against interest expense | 46,525 / 60,245 - 1; 33,361 / 40,063 - 1 (S3 page:2; S3 page:9) | -22.8% and -16.7% |

## Gaps

- G1 Critical for the decision: the debt agreements are not supplied, so covenant EBITDA, headroom, guarantors, security, restricted payments and redemption terms cannot be verified.
- G2: the audited FY2025 statements and annual MD&A are not supplied, so Q4 2025 flows and annual trends are assembled or missing.
- G3: ownership, control and customer concentration are not supplied.
- G4: this review was written by the same host as the handoffs it checks; no independent reviewer saw it.
- G5 and G6: later term-contract shares and the auditor identity are open.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 46 (Low), committee status Requires More Work, and gap G1.
- Review step: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: fetch the credit agreement, the note indenture and the 40-F exhibits, then rerun CP-1, CP-1A, CP-2 and CP-5 in a new run folder.
