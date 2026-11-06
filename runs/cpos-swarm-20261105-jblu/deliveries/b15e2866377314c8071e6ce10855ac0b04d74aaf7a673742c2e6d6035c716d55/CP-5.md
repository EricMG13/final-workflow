# CP-5 — Evidence trace and research-integrity QA: JETBLUE AIRWAYS CORP (jblu)

## Request

JETBLUE AIRWAYS CORP (jblu), as of 2026-11-05, pathway credit_snapshot, reporting currency USD, current period Q3 2026 and prior period FY2025. This handoff traces the claims of the four earlier handoffs (source readiness, financial base, business context and credit synthesis) to the pinned filings, recomputes their figures, and grades the result (absorbed CP-5A phase). The same host session wrote the four handoffs it checks, so this is a self-review, not an independent one, and no provider was called.

## Sources

Hashes are the sha256 of the pinned text extractions named by CP-OS. A locator `page:N` is the extraction chunk number, not the printed page.

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_jblu-20251231.htm.jsonl | 5eaf617accf854e4d3e9a550a2ff2955ebfa71253742ee07dd6faac0b2e32a8c |
| 10-Q_2026-03-31_jblu-20260331.htm.jsonl | 23aa04d969e5d0170c0af37c935f385dfb36e65e5eefd81c73b6d9abfad792fa |
| 10-Q_2026-06-30_jblu-20260630.htm.jsonl | 909f0d616195258039c6cade15d6ec9c2498b992386b681904fa4366c00d0fca |
| 10-Q_2026-09-30_jblu-20260930.htm.jsonl | acf402823b4f024901754bb305241f6c703d6a3c7b62a75b67703d555b0a8e99 |
| EX-99.1_2026-04-28_ex991-earningsreleaseq12026.htm.jsonl | d4d4219d15ba6a638e2373e8ae55aa1c8d909855e1454637cd8095dcf728854e |
| EX-99.1_2026-07-28_ex991-earningsreleaseq22026.htm.jsonl | 802f55be8bbdb2947fd6f1ea1be406ca4f8ca6aa8c3d778ecad7cf301e68ccf6 |
| EX-99.1_2026-10-26_ex991-earningsreleaseq32026.htm.jsonl | 698b07a0502ae526f90cdcc0cd39f907723cfed08c5317bc057549e3a8aec7de |
| context | 31c25d56081dda135cad8e796a84043b049461aaa2d0b6432dd4792f868c14f8 |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | 5f1fd6d78bb06a0ae2ac09089d15d4162bd31f1324bf5098e03d0142b1a1dcc0 |
| CP-1 | 58c5892d83fe67883e53348fce2c2bb7681059206834d241a6a44bac68076eb9 |
| CP-1A | a86f2f6e5a76d902727adc98a9a5a8baa4dddf9cd4339e005d871c5fe4f6f707 |
| CP-2 | 0c97bd29c11b1acc9d49b10cbb33edce3c7bee5fec6211913211c49302bd1daa |

Source ids used in the registers: S1 the FY2025 annual report, S2 the Q1 2026 quarterly report, S3 the Q2 2026 quarterly report, S4 the Q3 2026 quarterly report, S5 to S7 the Q1, Q2 and Q3 2026 earnings releases, S8 the context. Handoff versions checked: CP-0 attempt 1, CP-1 attempt 1, CP-1A attempt 1, CP-2 attempt 2 (attempt 1 was refused because one summary number did not appear in the body, and was repaired).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is traceable: every checked quotation and recomputed figure matches the filings. It omits an agreement naming the Icahn Group in its ownership and governance work, so committee use is restricted until that is corrected. | Low | One host wrote and checked all four earlier handoffs, so this review is not independent. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 63 quoted passages exist in the filings; 60 sit on the page cited and 3 carry no locator. | Wording can be relied on; only three page checks need extra effort. | High |
| All 95 cells of the financial table recompute from the statements, and 17 of 17 totals re-add. | Leverage, cover, liquidity and maturity figures can be used as stated. | High |
| The ownership and governance work misses a 2024 agreement with the Icahn Group on director nominations. | Sponsor alignment and the governance strength are incomplete until the agreement is read. | Medium |
| Six minor issues remain, none of which changes a credit conclusion. | Fixes are wording, locator or framing corrections. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 3 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 is an insufficient-information item. The most important provenance gap is the omission of the Director Appointment and Nomination Agreement with the Icahn Group (10-K exhibit index, page:177) from the ownership and governance analysis, which matters because a board nomination right held by a named activist group bears on sponsor alignment, and implies that the ownership conclusion and the governance strength must be restated, and committee use is restricted until then. The financial figures are not in doubt: they recompute exactly, and the covenant gap is a source gap that the earlier handoffs label correctly.

### Traceability summary

| Check | Result |
| --- | --- |
| Quoted passages found in the pinned filings | 63 of 63 |
| Quoted passages on the cited page | 60 of 63; 3 carry no locator |
| Financial table cells recomputed from the statements | 95 of 95 equal |
| Totals and tie-outs re-added | 17 of 17 equal |
| Material claims by lineage | 3 Directly Sourced, 5 Calculated, 1 Analyst Inference, 2 Weak Lineage, 1 Insufficient Information |
| Open issues | 1 MATERIAL, 6 MINOR |

### Remediation priority map

- Must-fix before committee: CP5-001. Read the Icahn Group Director Appointment and Nomination Agreement (8-K dated February 16, 2024, exhibit 10.1, listed at 10-K page:177), restate the ownership, activism and governance rows of the business-context handoff, and restate the governance strength in the credit synthesis. The accepted handoffs cannot be edited, so this needs a new run folder.
- Must-fix before the handoff is consumed downstream: None beyond CP5-001.
- Monitoring follow-up: CP5-004 record the 10-K statement of a non-investment-grade credit rating and obtain the agency ratings; CP5-005 reconcile the payroll support loan rate table to the loan descriptions; CP5-006 restate the liquidity-versus-fixed-claims comparison with operating cash burn beside it.
- Formatting and hygiene: CP5-002 correct the stated purpose of the treasury stock line; CP5-003 mark the revolver letter-of-credit statement as an inference; CP5-007 add a locator to the registrant-name quotation.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 6. Committee Use: Restricted.

No credit conclusion is changed by the findings: the financial base, structure, liquidity and maturity view recompute exactly. The Material issue (CP5-001) is an omission in ownership and governance evidence that the committee must see before it relies on the reading that no sponsor extraction channel is documented. One further closed issue, the CP-2 attempt 1 refusal, is not counted.

### QA envelope

- qa_status: Restricted. Confidence Score 25, band Insufficient Information (from `scripts/confidence_score.py`; see Calculations). committee_status: Restricted.
- Source gate: partial, because the source pack holds no executed debt agreements, no presentations and no ratings (see the readiness handoff). Required fields: 6 of 6 headings present in every handoff checked.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_jblu-20251231.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | JetBlue Airways Corporation, consolidated | Statements, debt note and rates, covenants text, business, history, exhibit index | Text extraction of the filed HTML; tables flattened | All four handoffs |
| S2 | 10-Q_2026-03-31_jblu-20260331.htm.jsonl | High: filed, unaudited | Quarter ended March 31, 2026 | Same | Q1 2026 statements | Text extraction; unaudited | Financial base (discrete Q1) |
| S3 | 10-Q_2026-06-30_jblu-20260630.htm.jsonl | High: filed, unaudited | Quarter and six months ended June 30, 2026 | Same | Q2 2026 statements, six-month cash flow | Text extraction; unaudited | Financial base (discrete Q2) |
| S4 | 10-Q_2026-09-30_jblu-20260930.htm.jsonl | High: filed, unaudited | Quarter and nine months ended September 30, 2026 | Same | Statements, debt note, maturities, liquidity, commitments, covenant statement, subsequent events | Text extraction; unaudited | All four handoffs |
| S5 | EX-99.1_2026-04-28_ex991-earningsreleaseq12026.htm.jsonl | Medium: issuer press release | Q1 2026 | Same | Statement of operations, selected balance data | Management-prepared; repeats the 10-Q | Tie-out only |
| S6 | EX-99.1_2026-07-28_ex991-earningsreleaseq22026.htm.jsonl | Medium: issuer press release | Q2 2026 | Same | Statement of operations, 2028 earnings target | Management-prepared | Tie-out; Management Language |
| S7 | EX-99.1_2026-10-26_ex991-earningsreleaseq32026.htm.jsonl | Medium: issuer press release | Q3 2026 | Same | Statement, guidance, fare recapture and unencumbered asset claims | Management-prepared; forward-looking items | Tie-out; Management Language |
| S8 | context | User settings, not issuer evidence | Run date 2026-11-05 | Run identity | Period labels, currency, blank rating, quote and sponsor fields | Not issuer evidence | Period and currency labels |

Module Status: Ready with Limitations. Traceability Scope: Top 5.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Earnings do not cover cash interest: LTM EBITDA excluding special items 149 against cash interest 493, cover 0.30x | CP-1, CP-2 | Operating loss, D&A, special items and cash interest from the statements | Debt service is met from liquidity, not earnings | Sets default risk and leverage tolerance | S1 page:113, page:114; S4 page:6, page:7 | Issuer reports no EBITDA; cash interest is net of interest income |
| 2 | Liquidity burn: unrestricted cash and investments 2,477 to 1,626, net debt 6,021 to 6,767, liquidity 2,226 | CP-1, CP-2 | Balance sheets and statement of cash flows | Cushion is shrinking while debt is not repaid | Sets liquidity and refinancing horizon | S1 page:112; S4 page:5, page:6, page:7, page:44 | Revolver covenant level not printed |
| 3 | Predominantly secured debt: 7,455 of 8,450 secured (88.22 percent); about 66 percent of owned property, equipment and intangibles pledged or committed | CP-2 | Debt table; pledged-asset statement | Secured lenders rank ahead of 995 of unsecured claims | Sets structure and later-financing capacity | S4 page:11, page:47 | Security packages and guarantors not supplied |
| 4 | 2029 maturity concentration: 1,835 in 2029, 4,691 after 2030, 629 through 2027 | CP-1, CP-2 | Scheduled maturities table | Refinancing clusters when the revolver also expires | Sets refinancing risk | S4 page:11, page:14 | Net of issuance costs |
| 5 | Covenant headroom cannot be measured | CP-1, CP-2 | Compliance statement; covenant descriptions | Minimum liquidity tests may bind first as cash falls | Sets monitoring posture | S4 page:47; S1 page:94, page:130 | Levels and definitions not printed |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM EBITDA excluding special items 149; cover 0.30x | CP-1, CP-2 | S1 page:113, page:114; S4 page:6, page:7 | Yes | High inputs | Calculated | Supported (recomputed equal) | High | Committee-Ready |
| Leverage 56.33x gross, 45.42x net | CP-1, CP-2 | S1 page:112; S4 page:5, page:6 | Yes | High inputs | Calculated | Supported (recomputed equal) | High | Committee-Ready |
| Net debt up 746; unrestricted cash down 851 | CP-1, CP-2 | S1 page:112; S4 page:5, page:6 | Yes | High inputs | Calculated | Supported (recomputed equal) | High | Committee-Ready |
| Liquidity 2,226 | CP-1, CP-2 | S4 page:5, page:14, page:44 | Yes | High | Calculated | Supported; agrees with management 2.2 billion | High | Committee-Ready |
| Secured share 88.22 percent | CP-2 | S4 page:11 | Yes | High | Calculated | Supported (recomputed equal) | High | Committee-Ready |
| 2029 maturity 1,835; thereafter 4,691 | CP-1, CP-2 | S4 page:11 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Fuel unhedged; 10 percent rise adds about 376 | CP-1A, CP-2 | S4 page:53 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Loyalty program is first-lien collateral for the TrueBlue notes and term loan | CP-1, CP-1A, CP-2 | S1 page:129, page:130 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Covenant headroom | CP-1, CP-2 | S4 page:47; levels not in the set | Partial | Management statement | Insufficient Information | Open gap, correctly labelled | Low | Gap correctly labelled |
| Unencumbered assets about 7 billion | CP-1, CP-1A, CP-2 | S7 page:2 against S4 page:11, page:47 | Yes | Management claim | Weak Lineage | Disclosed as unreconciled and excluded from the base case | Low | Remediation Needed (gap) |
| Fare recapture about 87 percent of higher fuel cost | CP-1A, CP-2 | S7 page:1 | Yes | Management claim | Weak Lineage | Labelled Management Language | Low | Remediation Needed (gap) |
| No sponsor or controlling holder; sponsor alignment risk low on the evidence supplied | CP-1A, CP-2 | S1 page:80, page:44; S1 page:177 not used | Partial | High filings, incomplete | Analyst Inference | Open: omits the Icahn Group agreement | Low | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total operating revenues FY2025 9,062 | runs/cpos-swarm-20261105-jblu/source-text | 10-K_2025-12-31_jblu-20251231.htm.jsonl | S1 | page:113, statement of operations | CP-1 financials table | Sourced | High | Matches |
| Operating loss FY2025 (368) and D&A 688 | same | same | S1 | page:113 | CP-1 financials table | Sourced | High | Matches |
| Operating loss nine months 2026 (509); D&A 548; special items 33 | same | 10-Q_2026-09-30_jblu-20260930.htm.jsonl | S4 | page:6 | CP-1 financials table | Sourced | High | Matches; quarters sum to nine months |
| Cash payments for interest, net 427 (FY2025) and 372 (nine months 2026) | same | S1 file and S4 file | S1, S4 | S1 page:114; S4 page:7 | CP-1 coverage | Sourced | High | FY label is net of interest income cash receipts (S1 page:136); nine-month label identical but not elaborated |
| LTM EBITDA excluding special items 149 | same | S1 and S4 files | S1, S4 | page:113; page:6 | CP-1 leverage and cover tables | Calculated | High | FY2025 plus nine months 2026 less nine months 2025 |
| Total debt carrying value 8,393 | same | S4 file | S4 | page:5, page:6, page:12 | CP-1, CP-2 | Sourced | High | 482 plus 7,911 |
| Debt table total 8,450 before issuance costs; secured 7,455; unsecured 995 | same | S4 file | S4 | page:11 | CP-2 capital structure | Calculated from sourced lines | High | Lines re-added equal |
| Scheduled maturities by year totalling 8,393 | same | S4 file | S4 | page:11 | CP-1 chart data, CP-2 | Sourced | High | Sum equals carrying value |
| Citibank revolver 600, undrawn, matures October 21, 2029 | same | S4 file | S4 | page:14 | CP-1, CP-2 | Sourced | High | No balance outstanding |
| Liquidity 2.2 billion including 600 undrawn line | same | S4 file | S4 | page:44 | CP-1, CP-2 | Sourced | High | Management statement agrees with computed 2,226 |
| Covenants: minimum balances of unrestricted cash, equivalents and unused commitments | same | S1 file | S1 | page:94 | CP-2 liquidity and covenants | Sourced | High | Level not printed |
| TrueBlue notes 9.875 percent due September 2031, co-issued with JetBlue Loyalty LP | same | S1 file | S1 | page:129 | CP-1, CP-2 debt table | Sourced | High | Guarantors named only generically |
| Pledged assets net book value 8.0 billion; about 66 percent pledged or committed | same | S4 file | S4 | page:11, page:47 | CP-2 key findings | Sourced | High | Different bases, both quoted |
| Spirit merger agreement terminated March 1, 2024; 69 million breakup fee | same | S1 file | S1 | page:161 | CP-1A transaction summary | Sourced | High | Matches |
| LaGuardia slots 22 for 58.5 million, completed October 2026 | same | S4 file | S4 | page:44 | CP-1A, CP-2 subsequent events | Sourced | High | Subsequent event, dated |
| Director Appointment and Nomination Agreement with the Icahn Group, February 16, 2024 | same | S1 file | S1 | page:177, exhibit index | Not carried into CP-1A or CP-2 | Sourced (omitted by the handoffs) | High | Triggers CP5-001 |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM figures | CP-1 tables; CP-2 | FY2025, nine months 2026, nine months 2025 | FY2025 + nine months 2026 - nine months 2025 | Calculated | Supported, recomputed equal for revenue, operating loss, D&A, special items, interest expense, cash interest, net loss, operating cash flow, capex and pre-delivery deposits | High | Basis of every LTM ratio | S1 page:113, page:114; S4 page:6, page:7 |
| EBITDA excluding special items | CP-1, CP-2 | Operating loss, D&A, special items | Operating loss + D&A + special items; LTM 149; numerator and period as stated; USD millions | Calculated | Supported; issuer reports no EBITDA, so definition is analyst-chosen | Medium | Leverage and cover | S1 page:113; S4 page:6 |
| Net debt | CP-1, CP-2 | Carrying debt; unrestricted cash and investment securities | Debt - (cash + current and non-current investment securities); 6,021 and 6,767 | Calculated | Supported (recomputed equal) | High | Leverage, liquidity | S1 page:112; S4 page:5, page:6 |
| Debt / EBITDA and net debt / EBITDA | CP-1, CP-2 | Carrying debt, net debt, LTM EBITDA excluding special items | 8,393 / 149 = 56.33; 6,767 / 149 = 45.42; FY2025 24.28 and 17.20; FY2024 15.19 and 8.17 | Calculated | Supported (recomputed equal) | Medium | Leverage tolerance | as above |
| Cash interest cover | CP-1, CP-2 | EBITDA excluding special items; cash interest paid, net | 149 / 493 = 0.30; FY2025 0.82; FY2024 2.44 | Calculated | Supported; cash interest is net of interest income | Medium | Debt service | S1 page:114, page:136; S4 page:7 |
| Free cash flow | CP-1, CP-2 | Operating cash flow, capex, pre-delivery deposits | Operating cash flow - capex - pre-delivery deposits; LTM (1,193) | Calculated | Supported (recomputed equal) | High | Liquidity burn | S1 page:114; S4 page:7 |
| Liquidity | CP-1, CP-2 | Cash and investments 1,626; undrawn revolver 600 | 1,626 + 600 = 2,226 | Calculated | Supported; agrees with management | High | Liquidity | S4 page:5, page:14, page:44 |
| Secured share | CP-2 | Debt table lines | 7,455 / 8,450 = 88.22 percent | Calculated | Supported (recomputed equal) | High | Structure | S4 page:11 |
| Maturities versus liquidity | CP-2 | 629 maturities through 2027; 570 committed flight equipment spending | 2,226 / 1,199 = 1.86 | Calculated | Arithmetic supported; ignores operating cash flow (see CP5-006) | Low | Liquidity horizon | S4 page:11, page:17 |
| Assumption: pledged-asset coverage not calculated | CP-2 | None | Not Calculable from Provided Materials: collateral values and security packages are not supplied | Not Calculable | Correctly withheld | High | Recovery mechanics | none |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | Sponsor alignment low; governance strength | Evidence set omits the Icahn Group Director Appointment and Nomination Agreement listed at S1 page:177; CP-1A states no specific activist is identified | Analyst Inference | A board nomination right held by a named activist group changes the ownership and governance reading and the strength cited in the credit synthesis | Read the agreement; restate in a new run | CP-1A governance section; CP-2 strengths |
| MINOR, disclosed | Unencumbered assets about 7 billion | Management claim not reconciled to the filing | Weak Lineage | Could overstate secondary liquidity if relied on | Already labelled and excluded from the base case; obtain appraisal basis | CP-1A conflicts; CP-2 key findings |
| MINOR, disclosed | Fare recapture about 87 percent | Management claim in the release only | Weak Lineage | Central recovery assumption is unverified | Already labelled Management Language | CP-1A; CP-2 |
| MINOR | Revolver has no letters of credit drawn | Inference from cash-collateralised letters of credit; no source states usage of the revolver | Analyst Inference | Availability of the 600 undrawn line is a liquidity input | State as inference or obtain the credit agreement | CP-1 liquidity table |
| MINOR | Ratings Not supplied | The 10-K states a non-investment-grade credit rating (S1 page:59) without agency or level | Weak Lineage | The statement is a creditor-relevant fact missing from the ratings rows | Record the statement; obtain agency ratings | CP-0, CP-1, CP-2 ratings rows |

Flags marked disclosed are labelled correctly by the originating handoff and are not counted as issues.

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings pinned by hash; one filing-listed agreement (Icahn Group) and the 2026 proxy statement are not in the set or not read | A governance fact in the exhibit index was not carried into the analysis | Ownership reading is incomplete | Supply and read the agreement and proxy statement |
| Citation completeness | Ready with Remediation | 63 quotations all found; 60 on the cited page; 3 without a locator | Missing locators slow verification | None on conclusions | Add locators |
| Calculation traceability | Committee-Ready | 95 of 95 table cells and 17 of 17 totals recompute; formulas and periods stated | A calculation error would move leverage | None found | None |
| Assumption transparency | Committee-Ready | Computed EBITDA definition, net interest basis and illustrative coverage are labelled | A hidden definition would drift between modules | None found | None |
| Markdown and export artifact integrity | Committee-Ready | Six required headings in every handoff; one refusal repaired | A malformed handoff would break downstream ingestion | None found | None |
| Reviewer independence | Ready with Remediation | The same host wrote and checked the handoffs | Shared blind spots go undetected, as CP5-001 shows | Errors of omission may remain | Independent review |

Overall auditability is the lowest of the dimensions: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Terms of the Icahn Group Director Appointment and Nomination Agreement and the holding of that group | Agreement text and the 2026 proxy statement | Board influence by an activist holder bears on sponsor alignment and strategy | Ownership and governance rows; governance strength | High impact | 8-K dated February 16, 2024, exhibit 10.1; 2026 proxy statement |
| CP-5-GAP-002 | Covenant levels and headroom | Credit agreements, indenture, compliance certificates | Headroom drives liquidity and default view | Covenant risk rows | High impact | Executed agreements |
| CP-5-GAP-003 | Agency ratings | Rating reports; the 10-K states only a non-investment-grade rating | External check on the weak-credit reading | Ratings rows | Medium impact | Rating agency publications |
| CP-5-GAP-004 | Events from October 27, 2026 to 2026-11-05 | Later filings | Financing or litigation steps may be missing | Subsequent events | Medium impact | EDGAR filings to the cutoff |
| CP-5-GAP-005 | Unencumbered asset basis | Appraisal and encumbrance schedule | Secondary liquidity depends on it | Collateral rows | Medium impact | Management bridge |
| CP-5-GAP-006 | Independent review | A second reviewer | Self-review limits detection of omissions | Whole run | High impact | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / jblu-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with two MINOR findings (CP5-004, CP5-007) | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, covenants | High | Six headings; accepted | Passed with four MINOR findings (CP5-003, CP5-004, CP5-005, CP5-007) | 95 of 95 table cells recompute equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, transactions, governance | High filings, incomplete governance evidence | Six headings; accepted | Restricted: one MATERIAL (CP5-001) and three MINOR findings (CP5-002, CP5-005, CP5-007) | Omits the Icahn Group agreement |
| CP-2 | requests/CP-2 attempt 2 / same run | Credit synthesis | High inputs | Six headings; attempt 1 refused, attempt 2 accepted | Restricted by inheritance of CP5-001, plus three MINOR findings (CP5-004, CP5-005, CP5-006) | Governance strength inherits the omission |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-2 | No specific activist or demand is identified; no sponsor extraction channel documented | Partially Supported | The 10-K exhibit index lists a Director Appointment and Nomination Agreement dated February 16, 2024 by and among the Icahn Group and JetBlue (S1 page:177); the handoffs neither mention nor read it | Read the agreement and restate ownership, activism and governance rows | Restricts Committee Use |
| MINOR | CP-1A | Treasury stock line described as of unstated purpose | Partially Supported | S1 page:140 (Note 5) states the treasury stock represents shares returned to satisfy tax payments on vested crewmember stock compensation, for FY2025 | State the purpose with its period | Formatting / Hygiene Only |
| MINOR | CP-1 | No letters of credit are drawn on the revolver | Partially Supported | Sources state letters of credit are cash-collateralised in restricted cash (S4 page:18) but not how the revolver is used | Label as inference | Monitoring Follow-Up |
| MINOR | CP-0, CP-1, CP-2 | Ratings Not supplied | Partially Supported | S1 page:59 states a non-investment-grade credit rating; agency and level are not given | Record the statement and keep the gap | Monitoring Follow-Up |
| MINOR | CP-0, CP-1, CP-1A | Registrant name quotation in the Request section | Supported | Quoted name carries no locator; it is on the cover page of every filing | Add the cover-page locator | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Key finding states liquidity covers fixed claims through 2027 | The 1.86x comparison (2,226 / 1,199) excludes operating cash flow; last-twelve-months free cash outflow is 1,193 and committed spending is already part of capex | None | Show the comparison with operating burn beside it | Monitoring Follow-Up |
| MINOR | CP-1 | Cash interest cover mixes a net-of-interest-income annual basis with a nine-month line of the same label | Basis wording differs by period, disclosed in the handoff | None | Keep the disclosure | Monitoring Follow-Up |
| Pass (no finding) | CP-1, CP-2 | EBITDA excluding special items, net debt, debt basis | Same definition and carrying-value basis in both handoffs; no drift found | None | None | Formatting / Hygiene Only |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR, disclosed gap | CP-1, CP-2 | Security, guarantors, covenants and cross-default of the TrueBlue financings and the revolver | Executed indenture, term loan and credit agreements | Only filing summaries are available; the handoffs mark levels and guarantors as not supplied and make no capacity inference | Supply the agreements | Required before any covenant or ranking conclusion |
| MINOR, disclosed gap | CP-1A | Director nomination rights of the Icahn Group | The agreement filed with the 8-K of February 16, 2024 | Not in the pack and not read | Supply and read | Required for the governance reading |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All | No market, relative-value or recommendation claim is made; the 2.50% convertible conversion price is quoted from the filing and no share price is used | Prices, spreads, ratings | Outside the minimum source pack by design | Add market modules only with sourced market data | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Payroll support loan rates: the 10-K table shows 2.0 percent while the loan text gives 1.00 percent until 2025 or 2026 and SOFR plus 2.00 percent after; CP-1 reproduces the table, CP-1A is silent, only CP-2 logs the inconsistency | CP-2 attempt 2 is the accepted version | Reconcile or carry the note into every handoff | Low: 535 of debt |
| Pass (no finding) | CP-0, CP-1, CP-1A, CP-2 | Debt 8,393, liquidity 2,226, maturities, EBITDA basis, period labels and entity name agree across all four | All cite the current upstream hashes | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Financial base, structure, liquidity and maturities are traceable; the governance reading is incomplete and the review is a self-review | Restate governance in a new run; obtain independent review | Committee use restricted |
| MINOR | CP-2 | Unsupported adjective | The word adequate in the liquidity assessment rests on a management statement; it is tagged as such | Keep the tag | None |
| MINOR | CP-0, CP-1 | Duplication | The release repeats the 10-Q statements; both handoffs treat the 10-Q as controlling | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Reader summary, attempt 1 | One summary number (net debt of 6,021) was not in the body; the adapter refused the handoff | Add the number to the body; done in attempt 2 | Resolved; attempt 2 accepted |
| Pass (no finding) | CP-0, CP-1, CP-1A | Required headings and sections | Six headings in order, readiness or view section directly after the reader summary, sources with hashes | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1A, CP-2 | Unsupported Claim | Omits the Icahn Group Director Appointment and Nomination Agreement (S1 page:177); states no specific activist is identified | Read the agreement; restate ownership and governance in a new run | Restricts Committee Use | Open |
| CP5-002 | MINOR | CP-1A | Partially Supported Claim | Treasury stock line described as of unstated purpose; S1 page:140 states it | State the purpose | Formatting / Hygiene Only | Open |
| CP5-003 | MINOR | CP-1 | Partially Supported Claim | No letters of credit drawn on the revolver is an inference | Label as inference | Monitoring Follow-Up | Open |
| CP5-004 | MINOR | CP-0, CP-1, CP-2 | Citation Gap | Ratings recorded as not supplied; S1 page:59 states a non-investment-grade rating | Record the statement | Monitoring Follow-Up | Open |
| CP5-005 | MINOR | CP-1, CP-1A, CP-2 | Cross-Module Inconsistency | Payroll support loan rate inconsistency logged only in CP-2 | Reconcile or carry the note | Monitoring Follow-Up | Open |
| CP5-006 | MINOR | CP-2 | Formula / Definition Drift | Liquidity coverage of fixed claims shown without operating cash burn | Show burn beside the comparison | Monitoring Follow-Up | Open |
| CP5-007 | MINOR | CP-0, CP-1, CP-1A | Citation Gap | Registrant name quotation without locator | Add locator | Formatting / Hygiene Only | Open |
| CP5-008 | MINOR | CP-2 | canonical Markdown Handoff Integrity Defect | Attempt 1 summary number missing from body | Repaired in attempt 2 | Formatting / Hygiene Only | Closed |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Every double-quoted span of 8 or more characters in the four handoffs searched in all seven sources, and the cited page compared where a locator is given | 63 spans; 63 found; 60 on the cited page; 3 without a locator (the registrant name, one per earlier handoff) |
| Q2 | Financial table recomputation | Statements parsed from the sources for FY2024, FY2025, nine months 2025, nine months 2026; LTM, EBITDA, free cash flow, net debt and ratios recomputed and compared cell by cell with the financial base | 95 of 95 cells equal (88 numeric, 7 correctly marked not supplied or not calculable) |
| Q3 | Tie-outs | Quarters summed to nine months for revenue, operating loss, D&A, interest expense, net loss and fuel; debt table totals; issuance cost deductions; two maturity tables; three balance sheet debt sums; restricted cash; secured plus unsecured | 17 of 17 equal |
| Q4 | Figure trace | Numbers in the credit synthesis and business-context bodies searched in the earlier handoffs, the sources and their own calculations | Every figure found; exceptions are one sum shown with its addition (1,055) and hash fragments |
| Q5 | Confidence Score | `confidence_score.py --lineage 'Directly Sourced:3,Calculated:5,Insufficient Information:1,Weak Lineage:2,Analyst Inference:1' --fields-present 6 --fields-total 6 --source-gate partial --findings MATERIAL:1,MINOR:6` | E = 70.83 over 12 material claims, C = 100, S = 0.7, P = 33: raw 24.75, score 25, band Insufficient Information, qa_status Restricted |

## Gaps

- CP-5-GAP-001 Critical for the governance reading: the Icahn Group agreement and the 2026 proxy statement are not read.
- CP-5-GAP-002: covenant levels and headroom are not printed in any source.
- CP-5-GAP-003: agency ratings; the 10-K states only that the credit rating is non-investment grade.
- CP-5-GAP-004: events from October 27, 2026 to 2026-11-05 are not supplied.
- CP-5-GAP-005: the basis of the management unencumbered asset claim.
- CP-5-GAP-006: no independent review; this handoff was written by the host that wrote the four handoffs it checks.

## Next module

- Report delivery: carry qa_status Restricted, Confidence Score 25 (band Insufficient Information), committee status Restricted and issue CP5-001.
- Rerun: fetch the 8-K dated February 16, 2024 (exhibit 10.1) and the 2026 proxy statement, then rerun the business-context, credit synthesis and trace modules in a new run folder.
- Review: an independent agent or model should repeat this check, starting with omissions in the exhibit index and notes, which a self-review is least likely to find.
