## Request

Magnera Corp (issuer id magn), as of 2026-11-05, pathway credit_snapshot, minimum module set. CP-5 traces the evidence behind the CP-0, CP-1, CP-1A and CP-2 handoffs to the pinned sources and grades the result (absorbed CP-5A phase). The same host wrote the four handoffs it checks, so this is a self-review, not an independent one; no provider was called. QA envelope: qa_status Passed; Confidence Score 44, band Low (from the supplied confidence script, see Calculations); committee_status Requires More Work.

## Sources

Issuer sources re-read to trace the handoffs (exact pinned names and sha256). A "page" is a text chunk of the extraction.

| Source ID | Source (exact name) | sha256 |
| --- | --- | --- |
| S1 | 10-K_2025-09-27_form10k.htm.jsonl | 8a2d31e8517added759c44fb832ba0e833b0182f88931d77ac8b15219681b6e7 |
| S2 | 10-Q_2025-12-27_form10q.htm.jsonl | fc18cf0b3124192f072f0a094fbc1605152c44349946b7208b65f0ac25d88f0f |
| S3 | 10-Q_2026-03-28_form10q.htm.jsonl | 00a31fc7f5573cbb41dba62ba9751e7ac35317c740673bba1de0ff348e567d96 |
| S4 | 10-Q_2026-06-27_form10q.htm.jsonl | 9bf0a737948e12b9a435299f2c1d5be9f80cbb7bbc87ba8bb4baa3f7134d16c0 |
| S5 | EX-99.1_2026-02-05_ef20064605_ex99-1.htm.jsonl | 2c929f0530d2fad28d8d608f7ff32ddbeacac9282e05451c75240bd19f5fad90 |
| S6 | EX-99.1_2026-05-07_ef20072634_ex99-1.htm.jsonl | 35c908fa7ed7e14681927f2c36fd3b1ad0328d835bdae7fd06641846130d5ea2 |
| S7 | EX-99.1_2026-08-06_ef20079553_ex99-1.htm.jsonl | 907fd63efeb9c514c2f2ef515ae237b76f56ae49850c45b010a3ceaedd06a508 |
| S8 | context (user settings, not issuer evidence) | 4a094c245ff44dd6e34e569a37f728533980efba9932af440a0d9b2f6b50325a |

Supplied handoffs:

| Module | sha256 |
| --- | --- |
| CP-0 | a8b15cc07abfbb855ac56418114ac7639ccb07ec7eb0a78b02caf33e517da591 |
| CP-1 | a78bacbb4723d5e8436e6fd7e6e91834e21d1b667c43041d9840bc2ad8acdf4e |
| CP-1A | dc1cfc41f7ccf460c47df520b4e07d54a6ff2eeaeab479e0167f855b94cb0f46 |
| CP-2 | 8cb9f4791859b68e77222586c5a18d25c7a4060bf008297d767fe2f79d1e5a8b |

Locators in this handoff are `page:N` of the pinned text, written `[source prefix page:N]`.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The Magnera analysis traces to the filings: all 308 verbatim citations sit on their cited pages and 46 recomputed figures match. It cannot yet support revolver access, covenant headroom or legal capacity, and it is a self-review. | Medium | Executed debt documents and revolver terms are not in the pack, and one host wrote and checked every handoff, so omissions are the likeliest undetected error. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 308 verbatim quotations match their cited pages; the other 58 quoted spans are search terms or labels. | Locators can be relied on; no citation attaches a figure to the wrong page. | High |
| 46 derived values and 4 tie-outs recomputed from the filings equal the handoffs, including leverage of 5.28x and cover of 2.91x. | Leverage, cover, free cash flow and liquidity figures can be used as stated. | High |
| Annual cash taxes of 22 are printed in the annual report, but an earlier handoff listed cash taxes as not supplied; later handoffs corrected it. | No conclusion changes; interim cash taxes remain unavailable and cash conversion is measured before any tax split. | High |
| Revolver availability, covenants, indentures and ownership terms have no source in the pack. | Usable liquidity, covenant headroom and legal capacity are unverified, which holds the credit view to Medium confidence. | High |
| The Confidence Score is 44, band Low, with five minor findings; committee status is Requires More Work. | Fit for screening and monitoring, not a committee-ready credit view until debt documents and an independent review are added. | Medium |

### Evidence trace view

Magnera's analysis is traceable enough to support a view of its current debt, liquidity and earnings, and not yet a view of revolver access, covenant headroom or creditor legal capacity. Every citation quotation checked sits on the page it names, every derived figure recomputed from the filings equals the handoff, and unsupported claims are labelled as gaps rather than filled. The critical provenance gap is the executed debt documents and revolver terms: liquidity access, covenant headroom and legal capacity rest on no supplied source, and the credit view's Medium confidence depends on them. The affected decision is any view of usable liquidity or creditor control. The remediation owner is the sourcing step. Five minor defects need no change to any conclusion, and the review is a self-review by the host that wrote the handoffs.

| Traceability summary | Result |
| --- | --- |
| Quotations checked against cited pages | 308 verbatim citations, all on the cited page; 58 other quoted spans are search terms or labels |
| Derived values recomputed from source pages | 46 of 46 equal; 4 of 4 tie-outs equal |
| Expense-block reconciliations | 5 of 5 equal; 2 of 2 quarter sums equal |
| Calculation rows of CP-1A and CP-2 re-run | 15 of 15 and 12 of 12 equal |
| Material claims by lineage | 4 Directly Sourced, 7 Calculated, 2 Analyst Inference, 2 Insufficient Information |
| Open findings | 5 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-09-27_form10k.htm.jsonl | High: filed, audited annual report; adverse internal control opinion | Fiscal years ended September 27, 2025, September 28, 2024 and September 30, 2023 | Magnera Corporation, consolidated | Statements, debt note, segments, tax, pension, controls, exhibit index | Text extraction; FY2024 notes in an unsupplied 8-K/A | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2025-12-27_form10q.htm.jsonl | High: filed, unaudited interim report | Quarter ended December 27, 2025 | Same | Statements, debt table, segments | Unaudited | CP-1, CP-1A |
| S3 | 10-Q_2026-03-28_form10q.htm.jsonl | High: filed, unaudited interim report | Quarter and two quarters ended March 28, 2026 | Same | Statements, debt table, segments | Unaudited | CP-1, CP-1A |
| S4 | 10-Q_2026-06-27_form10q.htm.jsonl | High: filed, unaudited interim report | Quarter and three quarters ended June 27, 2026 | Same | Latest statements, debt table, liquidity, guidance, controls | Unaudited; no revolver availability or covenant terms | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-02-05_ef20064605_ex99-1.htm.jsonl | Medium: issuer press release | Q1 FY2026 | Same | Guidance, debt payments, management LTM and synergy measures | Issuer non-GAAP presentation | CP-1, CP-1A |
| S6 | EX-99.1_2026-05-07_ef20072634_ex99-1.htm.jsonl | Medium: issuer press release | Q2 FY2026 | Same | Quarter free cash flow, management LTM and synergy measures | Issuer non-GAAP presentation | CP-1, CP-1A |
| S7 | EX-99.1_2026-08-06_ef20079553_ex99-1.htm.jsonl | Medium: issuer press release | Q3 FY2026 | Same | LTM and pro forma adjusted EBITDA, outlook wording | Issuer non-GAAP presentation | CP-1, CP-1A |
| S8 | context | User settings, not issuer evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency, sector label | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Gross leverage 5.28x and net 4.53x on LTM adjusted EBITDA | CP-1, CP-2 | Debt table and segment adjusted EBITDA rebuilt to LTM | Sets leverage tolerance and the refinancing starting point | Core leverage metric | [10-Q_2026-06-27 page:8] [10-Q_2026-06-27 page:11] [10-K_2025-09-27 page:41] [10-Q_2026-06-27 page:3] | Adjusted EBITDA is a company measure |
| 2 | Add-backs of 122 within 372 LTM adjusted EBITDA; 7.86x gross unadjusted | CP-1, CP-2 | Operating income plus depreciation and amortization against adjusted EBITDA | One third of the earnings base rests on management classification | Downside test for leverage | [10-Q_2026-06-27 page:3] [10-Q_2026-06-27 page:11] [10-K_2025-09-27 page:41] | Line-by-line add-back bridge not supplied |
| 3 | Nine-month free cash flow 32 against guidance of 90 to 110 | CP-1, CP-2 | Cash flow statement and guidance paragraph | Deleveraging pace depends on fourth-quarter cash | Near-term monitoring trigger | [10-Q_2026-06-27 page:4] [10-Q_2026-06-27 page:13] | Quarter cash flows are differences of cumulative columns |
| 4 | Cash 280 plus undrawn revolver commitment 350; no maturity before October 2029 | CP-1, CP-2 | Balance sheet, liquidity text, debt table and annual maturity statement | Low near-term default risk if access holds | Liquidity and runway view | [10-Q_2026-06-27 page:3] [10-Q_2026-06-27 page:19] [10-Q_2026-06-27 page:8] [10-K_2025-09-27 page:34] | Availability, borrowing base and letters of credit not supplied |
| 5 | Executed debt documents and revolver terms absent | CP-0, CP-1, CP-2 | Exhibit index names the agreements | Covenant headroom, guarantor coverage and legal capacity cannot be assessed | Limits creditor-control conclusions | [10-K_2025-09-27 page:46] [10-K_2025-09-27 page:47] | Documents not in the pack |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gross leverage 5.28x, net 4.53x and the three earlier dates | CP-1, CP-2 | Debt tables and segment notes in S1 to S4 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Unadjusted leverage 7.86x and add-backs 122 | CP-1, CP-2 | Operating income, D&A, adjusted EBITDA in S1 and S4 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Interest cover 2.91x on a cash-interest proxy | CP-1, CP-2 | Interest expense, net and non-cash interest in S1 to S4 | Yes | High inputs | Calculated | Supported with proxy label | Medium | Recomputed equal; proxy ties to reported FY2025 cash interest |
| Free cash flow 32 and Q3 (28); fourth-quarter need 58 to 78 | CP-1, CP-2 | Cash flow statements in S2 to S4; guidance in S4 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| No maturity before October 2029; 500 in 2029; 1,466 in 2031 | CP-1, CP-2 | Debt table in S4; annual statement in S1 | Yes | High | Directly Sourced | Supported, zeros for 2026 to 2028 extended from a September 2025 statement | Medium | Traced |
| Cash 280 and undrawn commitment 350 | CP-1, CP-2 | Balance sheet and market-risk text in S4 | Yes | High | Calculated | Supported as a commitment | Medium | Traced |
| Customer concentration: top ten about 42 percent | CP-1A, CP-2 | S1 accounting policies | Yes | High | Directly Sourced | Supported | High | Traced |
| Merger terms, new debt, 1,111 distribution | CP-1A | S1 business, acquisition and debt notes, cash flow | Yes | High | Directly Sourced | Supported | High | Traced |
| Material weaknesses and ineffective controls | CP-1A, CP-2 | S1 controls and audit report; S4 controls | Yes | High | Directly Sourced | Supported | High | Traced |
| Documented behaviour supports deleveraging | CP-1A, CP-2 | Equity statements, repayments, release wording | Yes | High and Medium | Analyst Inference | Interpretation of cited actions | Medium | Traced to actions |
| Fundamental credit view and thesis | CP-2 | CP-1 and CP-1A registers | Basis labels | Derived | Analyst Inference | Judgment | Medium | Traced to handoff rows |
| Revolver availability, covenants, ownership, legal capacity | CP-0, CP-1, CP-1A, CP-2 | No source in the pack | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales nine months FY2026 2,445 | runs/cpos-swarm-20261105-magn/source-text | 10-Q_2026-06-27_form10q.htm.jsonl | S4 | page:3, statement of operations | CP-1 extracts | Reported | High | Matches |
| Adjusted EBITDA FY2025 354 | same | 10-K_2025-09-27_form10k.htm.jsonl | S1 | page:41, Note 11 segments | CP-1 metrics | Reported, company-defined | High | Matches |
| Term loan 706, 4.75% notes 500, 7.25% notes 760 | same | 10-Q_2026-06-27_form10q.htm.jsonl | S4 | page:8, Note 5 | CP-1 debt table | Reported | High | Foots to 1,901 |
| No maturities until 2029; 500 and 1,531 | same | 10-K_2025-09-27_form10k.htm.jsonl | S1 | page:34, Note 3 | CP-1 maturities | Reported | High | Components re-added equal |
| Cash 280, 58 percent outside the U.S. | same | 10-Q_2026-06-27_form10q.htm.jsonl | S4 | page:3 and page:19 | CP-1 liquidity | Reported | High | Matches |
| Guidance: cash from operations 150 to 170, free cash flow 90 to 110 | same | 10-Q_2026-06-27_form10q.htm.jsonl | S4 | page:13, MD&A outlook | CP-1 guidance | Management guidance | High as a statement | Matches |
| Top ten customers about 42 percent | same | 10-K_2025-09-27_form10k.htm.jsonl | S1 | page:27, Note 1 | CP-1A customers row | Reported | High | Matches |
| Annual cash taxes paid 22 | same | 10-K_2025-09-27_form10k.htm.jsonl | S1 | page:37, Note 6 | CP-1A governance row | Reported | High | Matches; earlier handoffs missed it |
| Merger closed November 4, 2024; 90 and 10 percent | same | 10-K_2025-09-27_form10k.htm.jsonl | S1 | page:5, Item 1 | CP-1A transaction | Reported | High | Matches |
| Distribution to Berry 1,111 | same | 10-K_2025-09-27_form10k.htm.jsonl | S1 | page:25, cash flow statement | CP-1A transaction | Reported | High | Matches |
| Synergy add-on 60, 48, 35 in pro forma EBITDA | same | Q1, Q2 and Q3 releases | S5, S6, S7 | page:6 in each | CP-1A transaction | Issuer non-GAAP | Medium | Matches; attributed to management |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM figures | CP-1 metrics; CP-2 | FY2025 plus current year-to-date less prior year-to-date | Sum and difference | Recomputed equal | Supported | High | Basis of every ratio | S1 pages 23, 24, 41, 42; S2 pages 3, 4, 9; S3 pages 3, 4, 10; S4 pages 3, 4, 11 |
| Gross debt principal | CP-1; CP-2 | Instrument lines of the debt table | Sum before the discounts line | Recomputed equal; differs from the balance sheet carrying value by the discounts line | Supported with a basis caveat | Medium | Leverage basis | S1 pages 32, 33; S2 page 7; S3 page 8; S4 page 8 |
| Leverage | CP-1; CP-2 | Gross debt, cash, LTM adjusted EBITDA | Debt over EBITDA; (debt less cash) over EBITDA | Recomputed: 5.74, 5.52, 5.41, 5.28 and 4.88, 4.79, 4.58, 4.53 equal | Supported | High | Leverage tolerance | As above |
| Cash-interest proxy and cover | CP-1; CP-2 | Interest expense, net; non-cash interest expense | EBITDA over (interest less non-cash interest) | Recomputed: 2.85, 2.71, 2.82, 2.91 equal; FY2025 proxy 124 equals reported cash interest | Supported with proxy label | Medium | Debt service | S1 pages 24, 34; S2 pages 3, 4; S3 pages 3, 4; S4 pages 3, 4 |
| Free cash flow | CP-1; CP-2 | Operating cash flow and capex | Operating cash flow less additions to property, plant and equipment; quarters by difference | Recomputed: 36, (13), 73, (28), 32, (45) equal | Supported | High | Cash conversion | S1 page 24; S2 page 4; S3 page 4; S4 page 4 |
| Unadjusted EBITDA and leverage | CP-1; CP-2 | Operating income plus D&A | 63 + 187 = 250; 1,966 over 250 | Recomputed equal | Supported | High | Downside leverage | S1 page 42; S4 pages 3, 11 |
| Fixed-rate share, sensitivity, tangible equity | CP-2 | Debt table; balance sheet | (500 + 760) over 1,966; 706 x 0.25 percent; 1,017 - 858 | Recomputed equal; the figure 858 is not in CP-1 | Supported; see QA-2 | Medium | Rate and equity quality | S4 pages 3, 4, 8 |
| Pro forma synergy series | CP-1A | Release rows | 363 + 60; 364 + 48; 372 + 35 - 2 | Recomputed equal to 423, 412, 405 | Supported as management figures | Medium | Direction of management measure | S5, S6, S7 page 6 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial gate, 5 MINOR | Script formula | 44, band Low | Script output | High | QA envelope | confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Cash taxes not supplied | CP-1 gap row says only the FY2025 net cash interest is printed and lists cash taxes as not supplied; the annual report prints cash taxes paid of 22, 9 and 29 for FY2025, FY2024 and FY2023 [10-K_2025-09-27 page:37] "The Company paid cash taxes of $22 million, $9 million, and $29 million in fiscal years 2025, 2024, and 2023" | Contradicted not-supplied claim | A gap the sources can fill is a defect; CP-0 search terms omitted "cash taxes" | Use the annual figure; keep interim cash taxes Not supplied | CP-1 Gaps; CP-0 Gaps |
| MINOR | Tangible equity 159 | CP-2 uses goodwill and intangible assets of 858, which CP-1 and CP-1A do not contain, and attributes the calculation to the balance sheet in CP-1; the line is on [10-Q_2026-06-27 page:4] "Goodwill and intangible assets 858 890" | Figure outside the upstream set | CP-2 is meant to rest on upstream figures only; the value itself is correct | Add the line to the CP-1 balance sheet extract or cite the source | CP-2 Strengths and weaknesses; Calculations |
| MINOR | Headline debt basis | CP-1 and CP-2 headline gross principal 1,966; the canon convention is balance-sheet carrying value (1,901) with the gross delta logged. CP-1 shows both and the 65 difference; CP-2 states "debt stack of USD 1,966 million" without the word gross | Definition label | Leverage differs by 0.17x between bases (5.28x gross, 5.11x carrying) | Label the headline as gross principal wherever used | CP-2 Credit view |
| MINOR | Metrics table cells | CP-1 shows Not calculated in 9 cells (unadjusted leverage at three quarter ends and the nine-month column; operating income over interest at FY2025 and three quarter ends and the nine-month column) though the inputs are in the sources | Incomplete calculation | A reader cannot see the trend of the downside measure | Supplied below under Calculations Q6 | CP-1 Financials and credit metrics |
| MINOR | Self-description quote | CP-1A Company and operating model quotes "A leading global supplier" in the fact cell; the source reads "The Company is a leading global supplier"; the evidence cell holds the exact sentence | Paraphrase in quotation marks | Slight; no figure affected | Drop the quotation marks in the fact cell | CP-1A |

Observations that are disclosed in the handoffs and are not counted as findings: the interest cover chart fills a cash-interest column with a proxy and says so in each row; maturity zeros for 2026 to 2028 extend the September 27, 2025 statement of no maturities and say so; the annual report's "fiscal year 2029 and 2031" wording is flagged as inconsistent with the printed months; release LTM components differ by one or two from filing builds, with offsetting totals; management pro forma and synergy figures are labelled Management Language.

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text | A wrong document would change every figure | None found | None |
| Locator precision | Strong | 308 of 308 verbatim citations on the cited page | A misplaced locator slows verification or misattributes a figure | None on conclusions | None |
| Calculation reproducibility | Strong | 46 of 46 derived values, 4 of 4 tie-outs and 5 of 5 expense reconciliations recomputed equal | A calculation error would move leverage | None found | None |
| Gap labelling | Adequate | Missing revolver, covenant, ownership and later-event evidence labelled Not supplied or Insufficient Information; one Not supplied claim was wrong (QA-1) | A wrongly labelled gap hides evidence | Cash taxes only; no conclusion moved | Search all source text for a term and its synonyms before writing Not supplied |
| Cross-module consistency | Strong | CP-1A and CP-2 cite the accepted CP-1 hash; CP-2 figures found upstream except 1,260, 5.95 and 858 | Inconsistent figures mislead a committee | 858 untraced upstream (QA-2); 1,260 and 5.95 are CP-2 calculations from upstream figures | See QA-2 |
| Reviewer independence | Weak | The host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Executed debt documents and revolver terms | Term loan agreement, asset-based revolving credit agreement and amendment, indentures, guarantor list | Availability, covenant headroom, guarantor coverage and legal capacity cannot be assessed | CP-2 liquidity and creditor-control conclusions | Holds the credit view to Medium confidence | Exhibits named in the annual report index |
| G2 | Events after August 6, 2026 | Later filings and releases to the cutoff | Refinancing and results to the as-of date unknown | Monitoring posture | Lowers currency of the view | EDGAR filings to 2026-11-05 |
| G3 | Interim cash interest and cash taxes | Supplemental cash flow disclosure | Cover uses a proxy; cash tax drag unmeasured | CP-1 cover and free cash flow | Moderate | Issuer disclosure |
| G4 | Ownership, control rights, transition services terms | Proxy statement, agreement | Governance and related-party leakage unassessed | CP-1A, CP-2 governance | Moderate | Proxy statement and exhibits |
| G5 | Add-back bridge by line | Credit-agreement EBITDA definition | Lender-basis EBITDA unknown | Leverage on a lender basis | Moderate | Credit agreement |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / magn-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 2 / same run | Statements, LTM, debt, liquidity, charts | High | Six headings; attempt 1 refused for a Reader summary number (2.9) absent from the body, attempt 2 accepted | Passed with two MINOR findings (QA-1, QA-4) | All derived values recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, transaction, governance | High | Six headings; accepted | Passed with one MINOR finding (QA-5) | Corrects the cash taxes gap |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with two MINOR findings (QA-2, QA-3) | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Gap row for cash interest and cash taxes | Contradicted for annual cash taxes | Not supplied claim wrong for FY2025 (QA-1) | Use the annual figure | None |
| MINOR | CP-2 | Tangible equity | Value correct, lineage outside the upstream set | 858 not in CP-1 or CP-1A (QA-2) | Cite the source or extend CP-1 | None |
| MINOR | CP-1A | Self-description row | Supported by the evidence cell | Paraphrase in quotation marks (QA-5) | Remove quotation marks | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Headline debt is gross principal | Canon convention is balance-sheet carrying value with the gross delta logged; both shown in CP-1 (QA-3) | None | Label the headline basis | None |
| MINOR | CP-1 | Adjusted EBITDA as leverage denominator | Company-defined; add-backs 122 LTM; unadjusted shown beside | None | Keep both bases, as CP-1 and CP-2 do | None |
| MINOR | CP-1 | Interim cover | Proxy in a cash-interest column | None | Keep the proxy label in each row, as done | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-0, CP-1, CP-2 | Covenants, availability, collateral and guarantor coverage of the term loan, notes and revolver | Credit agreements, indentures, guarantor list | Documents not supplied; claims correctly marked Not supplied or Insufficient Information | Supply the documents | Required before any covenant or legal-capacity view |
| MINOR | CP-1 | Term loan and notes carry no financial maintenance covenants | Executed agreements | Management statement in the notes | Supply agreements | Required for baskets |
| MINOR | CP-1A | Related-party agreements with the former parent | Transition services, tax matters and employee matters agreements | Named in the exhibit index only | Supply agreements | Required for leakage view |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; the only price signal is the filed statement that book value exceeded fair value by 48 | Prices, spreads and ratings are outside the minimum source pack | Recorded by design | Add sourced market data in a later relative-value module | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A | Cash taxes: CP-1 says not supplied, CP-1A shows annual cash taxes of 22 and states the correction | CP-1A cites the accepted CP-1 hash a78bacbb; correction carried into CP-2 gaps | Use the annual figure going forward | None |
| MINOR | CP-1, CP-2 | CP-2 uses 858, absent from CP-1 | CP-2 cites CP-1 hash a78bacbb and CP-1A hash dc1cfc41 | Extend CP-1 extract or cite source | None |
| MINOR | CP-1A, CP-2 | CP-2 restates CP-1A figures (45 facilities, two thirds of adjusted EBITDA, 42 percent) consistently | None | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Debt, liquidity and earnings are traceable; revolver access, covenants and legal capacity are not; review is a self-review | Supply debt documents and an independent review | Committee status Requires More Work |
| MINOR | CP-1, releases | Duplication | The releases repeat 10-Q figures; the filings control and the releases are used for management measures only | None | None |
| MINOR | CP-1, CP-1A, CP-2 | Repetition | The add-back and control-weakness limitations appear in several handoffs by design | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Reader summary, attempt 1 | Stated cover as about 2.9x; the body number is 2.91; refused and repaired in attempt 2 | Quote body numbers exactly | Resolved; attempt 2 accepted |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Required headings and selectors | None: six H2 headings, the module view heading after the Reader summary, and every selector heading once | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-1 (CP-0 search) | Contradicted gap | Annual cash taxes of 22 printed; listed as not supplied | Use the annual figure | None | Open, corrected downstream |
| QA-2 | MINOR | CP-2 | Lineage | Goodwill and intangible assets 858 absent from CP-1 and CP-1A | Cite source or extend CP-1 | None | Open |
| QA-3 | MINOR | CP-1, CP-2 | Definition | Headline debt is gross principal, not carrying value | Label the basis | None | Open |
| QA-4 | MINOR | CP-1 | Completeness | Nine cells marked Not calculated though inputs exist | Calculated in Q6 | None | Open |
| QA-5 | MINOR | CP-1A | Quotation | Paraphrase in quotation marks | Remove marks | None | Open |
| QA-6 | MINOR | CP-1 | Export | Reader summary number 2.9 not in body | Repaired in attempt 2 | None | Closed |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Every double-quoted span that follows a locator in the four handoffs searched on the page the locator names | CP-0 76 spans, 47 verbatim on the cited page; CP-1 177 spans, 160; CP-1A 113 spans, 101; CP-2 none. Total 308 verbatim citations, all on the cited page. The other 58 spans are search terms, table labels or short descriptive phrases (29 in CP-0, 17 in CP-1, 12 in CP-1A); none is presented as a source quotation except the paraphrase in QA-5 |
| Q2 | Derived-value recomputation | Inputs parsed from the source pages by pattern, not from the handoffs: LTM sales, operating income, D&A, cash from operations, capex, free cash flow, net loss (7); LTM adjusted EBITDA, interest and non-cash interest at three dates (9); gross debt at four dates (4); gross and net leverage at four dates (8); cover at four dates and on reported FY2025 cash interest (5); free cash flow FY2025, Q1, Q2, Q3, nine months and prior nine months (6); EBITDA before add-backs, add-backs, unadjusted gross and net leverage, carrying-basis leverage (5); operating income over interest, cover over net interest (2) | 46 of 46 equal to the CP-1 values: for example LTM adjusted EBITDA 363, 364, 372; gross leverage 5.74, 5.52, 5.41, 5.28; net 4.88, 4.79, 4.58, 4.53; cover 2.85, 2.71, 2.82, 2.91; LTM free cash flow 113 |
| Q3 | Tie-outs | June 2026 debt table 706 + 500 + 760 - 65; September 2025 debt table 731 + 500 + 800 - 79; LTM adjusted EBITDA against the release; FY2025 cash-interest proxy against reported net cash interest | 1,901 equals the printed total; 1,952 equals the printed total; 372 equals the release; 141 - 17 = 124 equals the reported 124 |
| Q4 | Expense-block reconciliations | Net sales less cost of goods sold, selling, general and administrative, amortization of intangibles and restructuring, then corporate allocation for FY2025 | Q3 FY2026 22, Q3 FY2025 13, nine months FY2026 53, nine months FY2025 (5), FY2025 5 (8 less 3): all equal printed operating income; quarter sums 14 + 17 + 22 = 53 and 40 + 35 + 37 = 112 equal the nine-month figures |
| Q5 | CP-1A and CP-2 calculation rows | All 15 CP-1A and 12 CP-2 calculation rows recomputed | 15 of 15 and 12 of 12 equal (for example 187 / 282 = 66.3 percent; 1,260 / 1,966 = 64.1 percent; 1,017 - 858 = 159) |
| Q6 | Fill for QA-4 (computed by CP-5, not in CP-1) | LTM operating income at Q1 and Q2 = 41 and 54 (FY2025 5 plus year-to-date less prior year-to-date: 5 + 14 + 22 and 5 + 31 + 18); LTM D&A = 202 and 195 (206 + 49 - 53; 206 + 100 - 111); matched to the release rows [EX-99.1_2026-02-05 page:6] "Operating Income $ 10 $ 4 $ 14 $ (7 ) $ (15 ) $ (22 ) $ 41" and [EX-99.1_2026-05-07 page:6] "Depreciation and amortization 63 37 100 72 39 111 195" | EBITDA before add-backs: Q1 243, Q2 249, Q3 250. Gross debt over it: 2,004 / 243 = 8.25; 1,969 / 249 = 7.91; 1,966 / 250 = 7.86. LTM operating income over interest expense, net: FY2025 5 / 141 = 0.04; Q1 41 / 155 = 0.26; Q2 54 / 151 = 0.36; Q3 63 / 151 = 0.42 |
| Q7 | Confidence Score | `confidence_score.py --lineage "Directly Sourced:4,Calculated:7,Analyst Inference:2,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:5` | E = 74.0, C = 100, S = 0.7, P = 15; score = clamp((0.6 x 74 + 0.4 x 100) x 0.7 - 15) = 44.08, rounded to 44; band Low; qa_status Passed |

## Gaps

- G1, critical for the decision: executed debt documents and revolver terms are not in the pack, so usable liquidity, covenant headroom, guarantor coverage and legal capacity are unverified.
- G2: nothing is dated after August 6, 2026, so events to the cutoff are unknown.
- G3: interim cash interest and cash taxes are not supplied; annual FY2025 cash taxes (22) and cash interest (124) are.
- G4: ownership, control rights and transition services terms are not supplied.
- G5: the add-back bridge by line and any credit-agreement EBITDA definition are not supplied.
- G6: no independent review; this CP-5 was written by the same host that wrote the handoffs it checks.

## Next module

- Report delivery: carry qa_status Passed, Confidence Score 44 (Low), committee status Requires More Work, and gap G1.
- Fixes for a later run: use annual cash taxes of 22 (QA-1), cite or add goodwill and intangibles of 858 (QA-2), label the headline debt as gross principal (QA-3), use the QA-4 fill (Q6), drop quotation marks around the paraphrase (QA-5).
- Independent review: another agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: fetch the credit agreements, indentures and guarantor list named in the annual report exhibit index, the 2026 proxy statement, and any filing or release dated after August 6, 2026, then rerun CP-1A, CP-2 and CP-5 in a new run folder.
