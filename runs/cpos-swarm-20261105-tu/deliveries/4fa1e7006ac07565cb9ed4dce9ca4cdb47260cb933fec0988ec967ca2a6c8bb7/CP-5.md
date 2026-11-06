# CP-5 evidence trace and research-integrity QA: TELUS CORP (tu)

## Request

- Issuer: TELUS CORP (issuer id `tu`; registrant "TELUS Corporation"), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `tu-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, `minimum` module set. CP-5 checks the CP-0, CP-1, CP-1A and CP-2 handoffs against the seven pinned sources and grades the result (absorbed CP-5A phase).
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: `qa_status` Passed; Confidence Score 40, band Low (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.

## Sources

| Source (exact name) | sha256 |
| --- | --- |
| 40-F_2025-12-31_tu-20251231x40f.htm.jsonl | b0f2582e02ab1590b79f57963d19432006a5c182a75869a932135c754b75fcd3 |
| 6-K-EX-99.1_2025-09-30_tm2525674d1_ex99-1.htm.jsonl | 436bedaf1f4dce1c7e6eb59881bfd06b2eda28c728cd8f139c3e87e5b19f9141 |
| 6-K-EX-99.1_2026-02-12_tm261121d3_ex99-1.htm.jsonl | 86a3aab6322382ed8099639d74b8a5a665cd61822ab77656954f6c33682e6312 |
| 6-K-EX-99.1_2026-03-31_tm2610993d1_ex99-1.htm.jsonl | 786ff091c72b6c68ad509f7615fb77cb4d9d97ec151a629884165ec7501f67f6 |
| 6-K-EX-99.1_2026-05-08_tm2610993d2_ex99-1.htm.jsonl | 4a46a2ffd615b6354baf9f5fba0823218c2071cb4a3fa919c80e6fdbc83658f3 |
| 6-K-EX-99.1_2026-07-31_tm2615221d2_ex99-1.htm.jsonl | 159e10207755e982fc8e0761482d512b4d2a82246d4508c8eb2d2f1f129bbd5c |
| 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | df34bf40fbe3d3b13f773ae380315ed0a4e21b523c7736a3fcf69277289ecba4 |
| context | 444f0b1a3ec6fedd71ff422ee4a294e2ddb38e2b78bcbad2de66f2441a8d4efa |

| Supplied handoff (module) | sha256 |
| --- | --- |
| CP-0 | 544c6cab38ea7d4384375d826af7a24e93016625e263a47b8911621b1695f02d |
| CP-1 | 7a6e3bd7a6bb660a29791a2e6e8ec9a696df0f9a3647070b9101f36f2ca71b2f |
| CP-1A | d86c1edd876753e5e0065d9fb7daf913b8784d0ac8f86b51653a3589a93ef947 |
| CP-2 | 2140310e15ffaf3f226b0aab0cc772240a6bc46815e4ef15ead51c100cc23c86 |

Locators are `page:N`, the chunk number in the pinned text files. The checking scripts were run under `python3 -I` against the pinned `source-text` files in this run folder.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis traces well to the filings: every quotation checked is in its cited source and every recomputed figure matches. Gaps are missing documents and one self-review, not misquotation. | Medium | The same author wrote and checked the handoffs, and audited 2025 statements, agreements and ratings are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 52 derived figures in the financial base recompute exactly, and every figure in the credit synthesis appears in the two handoffs it rests on. | Leverage, cover and liquidity figures can be relied on as arithmetic from the filings. | High |
| Reported leverage of 3.5x rests on half equity credit for junior subordinated notes and unseen covenant definitions. | Covenant headroom of 0.70x is indicative, not verified. | Medium |
| Guarantee terms, Terrion governance and agency ratings are not supplied. | Structural position and loss given default cannot be traced to a source. | High |
| Connection counts and healthcare lives covered are not comparable across releases and one fell by 10.7 million without explanation. | Operating trends are untraceable, but no credit conclusion depends on them. | Medium |
| Six minor defects were found, none changing a conclusion. | Committee use needs more work and an independent review. | Medium |

### Evidence trace view

The run is traceable enough for a view of TELUS Corporation's financial position at June 30, 2026, and not for its structural position or covenant robustness. Every checked quotation sits on its cited page, every one of 52 derived figures recomputes exactly, and every figure in the credit synthesis appears in the two handoffs below it. Of 14 material claims, seven are directly sourced, three calculated, one an analyst inference, two Insufficient Information and one conflicting. The critical provenance gap is the absence of guarantee terms, Terrion terms, credit agreements and agency ratings, which holds the reported 3.5x and the 0.70x headroom to management definitions. The affected decision is any view of covenant robustness or ranking. Remediation owner: the sourcing step, then an independent reviewer.

| Traceability summary | Result |
| --- | --- |
| Bracketed quotations checked against cited pages | 93 of 93 found on the cited page (23 in the financial base, 70 in the business context) |
| Other quoted phrases in the four handoffs | All found in the pinned sources; locators match their stated pages |
| Derived figures recomputed | 52 of 52 equal |
| Source table figures re-read on the cited page | 42 page-level checks covering the financial table, chart inputs, debt register and non-debt claims; none wrong |
| Credit synthesis figures found in upstream handoffs | All |
| Material claims by lineage | 7 Directly Sourced, 3 Calculated, 1 Analyst Inference, 2 Insufficient Information, 1 Conflicting |
| Open findings | 6 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 40-F_2025-12-31_tu-20251231x40f.htm.jsonl | High: filed annual report cover document | Fiscal year ended December 31, 2025 | TELUS Corporation, registrant | Identity, auditor, exhibit list, controls statements | Financial statements are in an exhibit outside the pack | CP-0, CP-1, CP-1A |
| S2 | 6-K-EX-99.1_2025-09-30_tm2525674d1_ex99-1.htm.jsonl | High: filed, unaudited interim statements | Three and nine months ended September 30, 2025 | TELUS Corporation consolidated | Statements, debt and capital notes, TELUS Digital privatization, Terrion, Workplace Options | Text extraction; unaudited; earlier segment structure | CP-0, CP-1, CP-1A |
| S3 | 6-K-EX-99.1_2026-02-12_tm261121d3_ex99-1.htm.jsonl | Medium: issuer news release | Fourth quarter 2025 | TELUS Corporation consolidated | Quarter results, 2026 targets, CEO succession | Management-prepared; no full-year statements | CP-1, CP-1A |
| S4 | 6-K-EX-99.1_2026-03-31_tm2610993d1_ex99-1.htm.jsonl | High: filed, unaudited interim statements | Three months ended March 31, 2026; balance at December 31, 2025 | TELUS Corporation consolidated | Statements, debt register, maturities, provisions, capital structure | Text extraction; unaudited | CP-0, CP-1, CP-1A |
| S5 | 6-K-EX-99.1_2026-05-08_tm2610993d2_ex99-1.htm.jsonl | Medium: issuer news release | First quarter 2026 | TELUS Corporation consolidated | Quarter results, superseded guidance | Management-prepared | CP-1, CP-1A |
| S6 | 6-K-EX-99.1_2026-07-31_tm2615221d2_ex99-1.htm.jsonl | Medium: issuer news release | Second quarter 2026 | TELUS Corporation consolidated | Quarter results, dividend reset, guidance, segment reconciliation | Management-prepared | CP-1, CP-1A, CP-2 |
| S7 | 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | High: filed MD&A with statement-derived tables | Three and six months ended June 30, 2026 | TELUS Corporation consolidated | Eight-quarter table, balance sheet, liquidity, covenants, regulation | Unaudited; notes to the interim statements not included | CP-0, CP-1, CP-1A |
| S8 | context | Run settings, not issuer evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Reported leverage 3.5x against a 4.25x covenant, with half equity credit on junior subordinated notes | CP-1, CP-2 | Net debt 25,963 over EBITDA 7,315; covenant text | Sets covenant headroom and leverage tolerance | Core leverage metric | S7 page:59, page:61; S4 page:7, page:43 | Covenant definitions not supplied |
| 2 | Cash interest cover 4.62x, down from 5.31x | CP-1, CP-2 | LTM EBITDA over cash interest paid | Debt-service capacity | Direction of cover | S7 page:52; S2 page:3; S3 page:29; S4 page:3 | Cash interest includes lease interest and a premium |
| 3 | Liquidity and refinancing: cash 1,387, revolver 657, current maturities 3,802 including commercial paper | CP-1, CP-2 | Liquidity, facility and balance sheet text | Near-term default risk and market access | Monitoring horizon | S7 page:50, page:56, page:60, page:62, page:63 | Maturity schedule dated March 31, 2026 |
| 4 | Lower guidance, impairment of 2,135 and dividend reset | CP-1, CP-1A, CP-2 | Release guidance table; quarterly table | Deleveraging path | Forward leverage | S6 page:4, page:10, page:20; S7 page:29 | Asset sale terms not supplied |
| 5 | Structural position: Terrion minority equity and subsidiary obligations | CP-1A, CP-2 | Terrion note; debt note ranking text | Ranking of parent claims | Loss given default | S2 page:64, page:65; S4 page:39 | Guarantees and Terrion terms not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net debt 25,963, EBITDA 7,315, ratio 3.5x, covenant 4.25x and 4.9x versus 2.00x | CP-1, CP-2 | S7 page:59, page:61 | Yes | High | Documentary Fact | Supported | High | Traced |
| Gross debt 31,456 and 4.30x | CP-1, CP-2 | S7 page:50, page:51, page:59 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Cash interest cover 4.62x, 5.09x, 5.31x, 5.26x | CP-1, CP-2 | S2 page:3, page:14; S3 page:29; S4 page:3; S7 page:52 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Covenant headroom 0.70x and EBITDA cushion 1,206 | CP-1, CP-2 | S7 page:59, page:61 | Yes | High inputs; management measure | Calculated | Supported as indicative | Medium | Recomputed equal; definition unverified |
| Liquidity components 1,387, 657, 680, 344 | CP-1, CP-2 | S7 page:50, page:60, page:62, page:63 | Yes | High | Documentary Fact | Supported | High | Traced |
| Current maturities 3,802 include commercial paper | CP-1, CP-2 | S7 page:50, page:56; S4 page:43 | Yes | High | Documentary Fact | Supported | High | Traced |
| Guidance cut and dividend reset | CP-1, CP-1A, CP-2 | S6 page:2, page:4, page:10 | Yes | Medium: management release | Management Language | Supported as an attributed claim | Medium | Traced |
| Impairment 2,135 and net loss 1,830 | CP-1, CP-2 | S7 page:29; S6 page:1 | Yes | High | Documentary Fact | Supported | High | Traced |
| Terrion 50.1 per cent and net proceeds 1,246 | CP-1A, CP-2 | S2 page:64, page:65 | Yes | High | Documentary Fact | Supported | High | Traced |
| Guarantor structure and Terrion governance | CP-1A, CP-2 | No source in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Agency treatment of the junior subordinated equity credit | CP-1, CP-2 | No source in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Refinancing of low-coupon senior notes would raise interest | CP-2 | Coupon list in S4 page:40; no rate forecast | Partial | High inputs; inference | Analyst Inference | Labelled as inference | Low | Inference labelled, not quantified |
| Healthcare lives covered and connection counts | CP-1A | S3 page:7; S5 page:10; S6 page:5 | Yes | Medium | Conflicting | Open discrepancy | Low | Logged, not reconciled, not used as support |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net debt 25,963; EBITDA excluding restructuring 7,315; ratio 3.5 | run folder source-text | 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | S7 | page:59 | CP-1 financials table | Reported | High | Matches |
| Quarterly Adjusted EBITDA 1,777; 1,837; 1,839; 1,862 | run folder source-text | 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | S7 | page:29 | CP-1 financials table | Reported | High | Four-quarter sum 7,315 equals the printed LTM |
| Current maturities 3,802; long-term debt 26,429 | run folder source-text | 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | S7 | page:50, page:51 | CP-1 financials table | Reported | High | Sum 30,231 equals the printed LTM debt |
| Revolver 2,750 less backstop 2,093 leaves 657 | run folder source-text | 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | S7 | page:60 | CP-1 liquidity chart | Reported | High | Matches |
| Covenants 4.25 and 2.00; reported 3.5 and 4.9 | run folder source-text | 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | S7 | page:61 | CP-1 covenant section | Reported | High | Matches |
| Long-term debt composition 17,664; 1,643; 299; 7,322; 489; 2,714 | run folder source-text | 6-K-EX-99.1_2026-03-31_tm2610993d1_ex99-1.htm.jsonl | S4 | page:39, Note 26(a) | CP-1 debt register | Reported | High | Components re-added equal 30,131 |
| Maturity schedule 3,148 to 11,833 | run folder source-text | 6-K-EX-99.1_2026-03-31_tm2610993d1_ex99-1.htm.jsonl | S4 | page:46, page:47, Note 26(i) | CP-1 maturity chart | Reported | High | Buckets re-added equal 29,673 |
| Interest paid Q4 2025 306 and Q4 2024 319 | run folder source-text | 6-K-EX-99.1_2026-02-12_tm261121d3_ex99-1.htm.jsonl | S3 | page:29 | CP-1 interest cover | Reported | Medium | Twelve-month 1,397 at September 30, 2025 equals S2 page:14 |
| Terrion 50.1 per cent, net cash proceeds 1,246 | run folder source-text | 6-K-EX-99.1_2025-09-30_tm2525674d1_ex99-1.htm.jsonl | S2 | page:64, page:65 | CP-1A transaction summary | Reported | High | Matches |
| Privatization closed October 31, 2025 at US$4.50 per share | run folder source-text | 6-K-EX-99.1_2025-09-30_tm2525674d1_ex99-1.htm.jsonl | S2 | page:63, page:64 | CP-1A timeline | Reported | High | Matches |
| Dividend reset to 0.1875 per share | run folder source-text | 6-K-EX-99.1_2026-07-31_tm2615221d2_ex99-1.htm.jsonl | S6 | page:4 | CP-1A, CP-2 | Reported | Medium | Matches |
| Guidance table previous and updated | run folder source-text | 6-K-EX-99.1_2026-07-31_tm2615221d2_ex99-1.htm.jsonl | S6 | page:10 | CP-1, CP-2 | Management claim | Medium | Matches |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FY2025 and LTM flows | CP-1 table; CP-2 findings | Eight-quarter table | Four-quarter sums | Recomputed: 14 of 14 equal; FY2025 EBITDA, restructuring and Adjusted EBITDA tie to S4 page:8; LTM net loss and EBITDA tie to S7 page:59 | Supported | High | Basis of every ratio | S7 page:29; S4 page:8 |
| Cash interest paid, twelve months | CP-1 interest cover | Quarterly interest paid | Four-quarter sums | Recomputed: 4 of 4 equal; September 2025 sum ties to the printed 1,397 | Supported | High | Debt service | S2 page:3, page:14; S3 page:29; S4 page:3; S7 page:52 |
| Total debt and total debt / EBITDA | CP-1 charts; CP-2 | Long-term debt plus short-term borrowings over LTM EBITDA excluding restructuring | Sum and ratio | Recomputed: 8 of 8 equal | Supported | High | Gross leverage | S7 page:50, page:51, page:59; S4 page:1, page:2, page:39; S2 page:2, page:11 |
| Issuer net debt / EBITDA and (total debt less cash) / EBITDA | CP-1 charts | Printed net debt; cash | Ratios | Recomputed: 7 of 7 equal; December 31, 2025 correctly marked Not supplied | Supported | High | Leverage definitions | S7 page:59; S4 page:7; S2 page:11 |
| EBITDA / cash interest | CP-1 charts; CP-2 | LTM EBITDA; cash interest paid | Ratio | Recomputed: 4 of 4 equal | Supported | High | Debt service | As above |
| Covenant headroom | CP-1 covenant section; CP-2 | Reported ratio and limit; net debt | 4.25 minus 3.549; net debt over 4.25 | Recomputed: 4 of 4 equal | Supported as indicative | Medium | Acceleration risk | S7 page:59, page:61 |
| Pre-equity-credit net debt ratios | CP-1; CP-2 | Net debt plus equity credit | Sum over EBITDA | Recomputed: 4 of 4 equal | Supported, labelled illustrative | Medium | Sensitivity of reported leverage | S4 page:7; S2 page:11 |
| Liquidity reproduction, maturity total and lease sum | CP-1 | Printed components | Sums | Recomputed: 6 of 6 equal; 2,724 reproduces the issuer wording over 2.7 billion | Supported | High | Liquidity | S7 page:63; S4 page:46, page:47 |
| Confidence Score | This handoff | 14 material claims, 17 of 17 registers, partial gate, 6 MINOR | Script formula | 40, band Low | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 commercial paper backstop and debt register | The 1,643 backstop at March 31, 2026 (S4 page:44) and the debt note components carry section-level or no page locators | Imprecise locator | A reader checking the figure searches two pages | Cite S4 page:44 and page:39 | CP-1 handoff |
| MINOR | CP-1A Terrion, Workplace Options and tender figures | Several amounts (Terrion non-controlling interest 792, cash consideration 453 and 280) have no page locator | Missing locator | Slower verification; values are correct | Cite S2 page:65 and page:44 to page:45 | CP-1A handoff |
| MINOR | CP-2 credit view and key findings | The junior subordinated notes amount 7,322 is stated without its March 31, 2026 date | Period omitted | The reader may read it as a June 30, 2026 balance | Date the figure | CP-2 handoff |
| MINOR | CP-1A company profile | The sector description is taken from the run context and tagged Documentary Fact, although context is not issuer evidence | Mis-tagged category | Context is a user setting, not a filing | Tag as context-derived; the filing gives only code 4812 | CP-1A handoff |
| MINOR | CP-0 structural ranking | The phrase on subordination to subsidiary obligations is cited at S4 page:39 and page:45; the second occurrence is on S4 page:44 | Wrong page locator | A reader checking page:45 does not find the phrase | Cite S4 page:44 | CP-0 handoff |
| MINOR | CP-1A, CP-2 operating indicators | Connection counts and healthcare lives covered are not comparable across releases; the quarter movement of 10.7 million is unexplained | Open conflict | Operating trend claims cannot be traced | Obtain the issuer's reconciliation; keep out of credit conclusions | CP-1A conflicts table |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text and statement headings | A wrong document would change every figure | None found | None |
| Locator precision | Adequate | 93 of 93 bracketed quotations on the cited page; six handoff statements carry imprecise or missing locators | Slower checks; risk of a misplaced citation | None on conclusions | Exact page locators |
| Calculation reproducibility | Strong | 52 of 52 derived figures recomputed equal | Calculation errors would move leverage and cover | None found | None |
| Cross-module consistency | Strong | All CP-2 figures found in CP-1 or CP-1A; CP-1A and CP-2 cite current upstream hashes | Inconsistent figures mislead a committee | None found | One date label in CP-2 |
| Definition transparency | Adequate | Net debt, EBITDA and covenant measures defined and labelled; covenant definitions not supplied | A reported ratio can differ from the covenant ratio | Headroom indicative | Credit agreement |
| Reviewer independence | Weak | Host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Guarantor structure, Terrion terms, credit agreements and indentures | Executed agreements and partnership terms | Covenant robustness and ranking cannot be traced | CP-2 structure risk and covenant headroom | Holds the view to management measures | Credit agreements, indentures, Terrion partnership terms |
| G2 | Audited FY2025 statements and annual MD&A | Exhibit 99.4 of the Form 40-F | FY2025 flows are assembled from quarters | CP-1 annual comparisons | Lowers precision of annual figures | Exhibit 99.4 |
| G3 | June 30, 2026 interim notes | Interim statements with Notes 3, 18, 22, 26, 29 | Debt register and maturities are dated March 31, 2026 | CP-1 and CP-2 refinancing view | Lowers currency of the debt view | June 30, 2026 interim statements |
| G4 | Named ratings and agency treatment of the equity credit | Agency reports | The equity credit underpins reported leverage | CP-2 leverage view | Caps leverage confidence | Agency reports |
| G5 | Events after July 31, 2026 | Later filings including third-quarter 2026 results | Asset sale and deleveraging status at the as-of date unknown | Monitoring posture | Lowers currency of the view | Filings to the cutoff date |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / tu-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with one MINOR locator finding | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, debt, liquidity, covenants, ratios | High | Six headings; accepted | Passed with one MINOR locator finding | 52 of 52 derived figures equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, transaction, governance, conflicts | High | Six headings; accepted | Passed with three MINOR findings | Two locator or tag findings and one open conflict |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with one MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Structural ranking quotation, cited at page:39 and page:45 | Supported | Second page is S4 page:44 | Correct the page | None |
| MINOR | CP-1 | Commercial paper backstop 1,643 and debt note components | Supported | Missing page locator (S4 page:44, page:39) | Cite pages | None |
| MINOR | CP-1A | Terrion non-controlling interest 792; Workplace Options cash consideration 453 and 280 | Supported | Missing page locator (S2 page:65, page:44 to page:45) | Cite pages | None |
| MINOR | CP-1A | Sector description | Supported by context only | Context tagged as Documentary Fact | Re-tag as context-derived | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Cash interest paid as the cover denominator | Includes the interest component of lease payments and a Q2 2026 prepayment premium of 51; gross of interest received | None | Keep the issuer's net interest cost measure (4.9x) beside it, as CP-1 does | None |
| MINOR | CP-1, CP-2 | Reported net debt to EBITDA | Includes half equity credit for junior subordinated notes and hedging adjustments; the gross ratio is shown beside it | None | Keep both bases labelled, as the handoffs do | None |
| MINOR | CP-1 | Covenant headroom | Uses the management ratio, not the credit agreement definition; the issuer says minor differences exist | Covenant measure versus management measure | Label as indicative, as the handoffs do | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1A, CP-2 | Notes are effectively subordinated to subsidiary obligations; guarantees unknown; Terrion call option and outside equity | Indentures, supplemental trust indentures, Terrion partnership terms | Documents not supplied; claims correctly marked | Supply documents | Required before any ranking view |
| MINOR | CP-1 | Covenant thresholds 4.25 and 2.00 | Executed credit agreement | Description only | Supply agreement | Required for verified headroom |
| MINOR | CP-1 | Change-of-control repurchase at 101 per cent and rating-event repurchase at 102 per cent | Supplemental indentures | Summarized in the note | Supply indentures | Required for trigger terms |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; prices, spreads and named ratings are outside the minimum pack | Bond prices, spreads and agency ratings | Recorded by design | Add market data only with a sourced dataset | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | Junior subordinated notes 7,322 is a March 31, 2026 balance but is read in CP-2 beside June 30, 2026 ratios | CP-2 cites current CP-1 and CP-1A hashes | Add the date | None |
| MINOR | CP-1, CP-1A | Free cash flow guidance 2.45 billion (May) versus 1.8 billion (July); leverage target year 2027 versus 2028 | Later release controls; both carried as dated claims | None needed | None |
| MINOR | CP-1A, CP-2 | Healthcare lives covered 161.2, 169.6 and 158.9 million; connections 21.2 and 17.9 million | Definition change from January 1, 2026 explains connections only | Obtain issuer reconciliation | None on credit conclusions |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Financial position is traceable; structural position and covenant robustness are not; review is a self-review | Supply agreements, ratings and an independent review | Committee status Requires More Work |
| MINOR | CP-1, CP-1A | Duplication | The July release repeats the MD&A quarter figures; the MD&A is the filed source and the release is not counted as independent corroboration | None | None |
| MINOR | CP-2 | Restatement | CP-2 restates figures from CP-1 and CP-1A; all values match | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Chart data tables | Monetary cells read Not supplied because the issuer reports in C$ and the table asks for US$m; C$ amounts are in the basis column | Accept as designed; a C$ chart contract would remove the loss | Report charts for liquidity and maturities carry no plotted values |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Headings and Reader summary | All four accepted on attempt 1 with the required H2 headings, Reader summary and view sections | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-1 | Locator | Backstop 1,643 and debt note components lack page locators | Cite S4 page:44 and page:39 | None | Open |
| QA-2 | MINOR | CP-1A | Locator | Terrion 792, Workplace Options 453 and 280 lack page locators | Cite S2 page:65 and page:44 to page:45 | None | Open |
| QA-3 | MINOR | CP-2 | Period | 7,322 stated without its March 31, 2026 date | Date the figure | None | Open |
| QA-4 | MINOR | CP-1A | Category | Context-derived sector tagged Documentary Fact | Re-tag | None | Open |
| QA-5 | MINOR | CP-1A, CP-2 | Open conflict | Operating indicators not comparable; 10.7 million unexplained movement | Obtain issuer reconciliation | None | Open |
| QA-6 | MINOR | CP-0 | Locator | Subordination quotation cited at page:45; the second occurrence is S4 page:44 | Cite page:44 | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Bracketed quotation trace | Every `[LABEL page:N "quote"]` citation in CP-1 and CP-1A searched on its stated source page, whitespace normalized | 93 of 93 found on the cited page |
| Q2 | Other quoted phrases | Every other double-quoted phrase in CP-0, CP-1, CP-1A and CP-2 searched across all seven sources, and its stated page compared | All real quotations found in the sources. 11 spans that crossed quote boundaries were parser artifacts. 14 CP-0 quotations flagged by a nearest-page heuristic were inspected by hand: 13 carry the correct page and one (subordination quotation) cites page:45 for page:44 (QA-6) |
| Q3 | Derived figures | Each FY2025 and LTM sum, interest sum, total debt, ratio, headroom, pre-credit sensitivity, liquidity, maturity and lease sum in CP-1 recomputed from its printed inputs and searched in the CP-1 text | 52 of 52 equal |
| Q4 | Source figures | 42 page-level checks of the table figures in CP-1 against the cited page text | All present; three string mismatches were formatting only (footnote marker, section break, missing dollar sign) |
| Q5 | Cross-module figures | Every number in the CP-2 findings searched in the CP-1 and CP-1A text | None missing |
| Q6 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:7,Calculated:3,Analyst Inference:1,Insufficient Information:2,Conflicting:1" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:6` | E 72.14, C 100, S 0.7, P 18: score = clamp((0.6 x 72.14 + 0.4 x 100) x 0.7 - 18) = 40.3, rounded to 40; band Low; qa_status Passed |

## Gaps

- G1 Critical for the structural view: guarantor structure, Terrion terms, credit agreements and indentures are not supplied; the reported 3.5x and the 0.70x headroom remain management-measure figures.
- G2: audited FY2025 statements and annual MD&A not supplied.
- G3: June 30, 2026 interim notes not supplied; debt register dated March 31, 2026.
- G4: named ratings and the agency treatment of the equity credit not supplied.
- G5: events after July 31, 2026, including third-quarter 2026 results and the October 1, 2026 dividend and discount change, are not supplied; they are labelled as dated and not as outcomes.
- G6: no independent review; this CP-5 was written by the same host that wrote the four handoffs.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 40 (Low), committee status Requires More Work, and gap G1.
- Swarm review step: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: fetch Exhibits 99.3 and 99.4 of the Form 40-F, the June 30, 2026 interim statements, the credit agreements and indentures, and agency reports; then rerun the modules in a new run folder.
