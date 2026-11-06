# CP-5 — Evidence trace and research-integrity QA: LendingTree, Inc. (tree)

## Request

- Issuer: LendingTree, Inc. (issuer id `tree`), as of 2026-11-05, information cutoff 2026-11-05, pathway `credit_snapshot`, run `tree-2026-11-05-credit_snapshot-host`, minimum module set.
- Scope: CP-5 checks the accepted CP-0, CP-1, CP-1A and CP-2 handoffs against the seven pinned filings and releases and grades the result (absorbed CP-5A phase). The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: `qa_status` Restricted; Confidence Score 30, band Insufficient Information (from `scripts/confidence_score.py`, see Calculations); `committee_status` Restricted.

## Sources

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_tree-20251231.htm.jsonl | 8cb6cb5e097dc2e8360d276758588e587f0ac910e30b439c9a6d5f22fdc532f1 |
| 10-Q_2025-09-30_tree-20250930.htm.jsonl | 249304d8f29fc14b902a9aacbb2c6a074e549655cafbbfa182447cab0a8e6bd0 |
| 10-Q_2026-03-31_tree-20260331.htm.jsonl | 9f7be701e3beaeb193c8f4c45fa295df34640347810fab7e7e1868937c8317f9 |
| 10-Q_2026-06-30_tree-20260630.htm.jsonl | 4c93c158274dd2856277ea5350526f695a8bcd4a41e0bedcd9b748ac31b890ae |
| EX-99.1_2026-03-02_tree-123125xer.htm.jsonl | 930047033d516e80ede0b1af19850b29c93444522e483a1dc8c6992d4283ee5d |
| EX-99.1_2026-04-30_tree-33126xer.htm.jsonl | 9b95e0c334507932b6d82bc72cf01d0a8f620ab6313637adea07e7f7ef2b4190 |
| EX-99.1_2026-07-29_tree-63026xer.htm.jsonl | b737e26fe71071d22f2d669bce2532cab38eb1e5741e87f2852ff6a85cf82520 |
| context | d200051bbc093266762c46db0da57fcc23aae21f45bdfa41362781dff2cb6e7d |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | c84ab10531b22ca79243cab80e778b189c7ae85ab40d1bc94cfa4d4426e74643 |
| CP-1 | 66d19075d0cda548fb908b11cbace236ac80961fccbfe892b5468b6b2cd9a36f |
| CP-1A | 27aa6bb2d2a88e25a00702feb3dd400595805f473712abaaf922df6d060d8625 |
| CP-2 | a26786c8b16d447a4b82e98b27e6a57394ed700884bf431ab8a4cf793401c597 |

Locators are `page:N`, the source chunk number in each pinned file, not the printed page. The handoffs cite them as `page:N` next to a short file name (10-K, 10-Q Q2 2026, release Q4 2025 and so on). The check was made by script over the pinned page text, and every finding below was confirmed by hand against the page it names.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four prior analyses trace well to the filings: all 80 quotations and every reported figure were found, and every recomputed ratio matched. One unsupported market comparison in the credit view and the missing credit agreement restrict committee use. | Low | The credit agreement and any filing after July 30, 2026 are not supplied, and the review was written by the same host that wrote the four analyses. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 80 quotations in the first three analyses were found on their cited pages; the only misses were search terms and parsing artifacts. | Quoted facts about the business, debt and ownership can be relied on because the pinned files support them. | High |
| 64 of 64 recomputed ratios and 51 of 51 statement tie-outs equal the financial base. | Leverage of 2.58x, cover of 4.42x and free cash flow of USD 73.9 million can be relied on, subject to the EBITDA definition. | High |
| The credit view calls leverage low for a high yield issuer, but no peer or market data is supplied. | Treat that comparison as unsupported; the ratio itself is sourced and the rest of the credit view stands. | High |
| Covenant headroom, guarantors and letters of credit rest on issuer summaries because the credit agreement is not supplied. | Creditor protection cannot be verified, so any comfort from the covenant package is unverified. | High |
| The review is a self-review, and five minor locator and wording defects remain open. | Independent review is needed before committee use; the minor defects do not change a conclusion. | Medium |

### Evidence trace view

The analysis is traceable for the fundamental view of LendingTree's current structure and earnings, and not for its covenant protection. All 80 quotations in the first three handoffs sit on their cited pages, every reported figure in the financial base is in the sources, and 64 of 64 ratios and 51 of 51 tie-outs recompute equal. Of 14 material claims, 5 are directly sourced, 5 calculated, 1 assumption-based, 2 analyst inference and 1 insufficient information. The critical provenance gap is the credit agreement, which sets covenant headroom, guarantors and letters of credit. One material defect, an unsupported comparison with high yield issuers in the credit view, and five minor locator and wording defects are open. The remedy owner is the sourcing step for the agreement and an independent reviewer for the rest.

### Traceability summary

| Check | Result |
| --- | --- |
| Quotations checked against cited pages | 80 in CP-0, CP-1 and CP-1A; none misquoted; 4 cells cite two files and were checked by hand |
| Reported figures in CP-1 found in the pinned sources | All; derived figures reproduced from them |
| CP-1 table ratios recomputed from its own inputs | 64 of 64 equal |
| Statement tie-outs re-added | 51 of 51 equal |
| CP-2 figures found in CP-1, CP-1A or CP-2 calculations | All; four are rounded restatements |
| Material claims by lineage | 5 Directly Sourced, 5 Calculated, 1 Assumption-Based, 2 Analyst Inference, 1 Insufficient Information |
| Open findings | 1 MATERIAL, 5 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_tree-20251231.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | LendingTree, Inc. and subsidiaries, consolidated | Statements, debt Note 13, Adjusted EBITDA reconciliation, business, ownership and risk disclosure, exhibit list | Text extraction; Items 10 to 14 incorporate a proxy statement that is not supplied | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2025-09-30_tree-20250930.htm.jsonl | High: filed, unaudited interim report | Three and nine months ended September 30, 2025 | Same | Q3 2025 statements, debt after the August 2025 refinancing | Unaudited | CP-1, CP-1A |
| S3 | 10-Q_2026-03-31_tree-20260331.htm.jsonl | High: filed, unaudited interim report | Three months ended March 31, 2026 | Same | Q1 2026 statements, cash flow, debt | Unaudited | CP-1, CP-1A |
| S4 | 10-Q_2026-06-30_tree-20260630.htm.jsonl | High: filed, unaudited interim report | Three and six months ended June 30, 2026 | Same | Statements, segments, debt, liquidity, market risk, Adjusted EBITDA | Unaudited; prior-period reclassification noted | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-03-02_tree-123125xer.htm.jsonl | Medium: issuer press release | Q4 2025 and FY2025 | Same | Q4 2025 non-GAAP reconciliations, management leverage statement, initial 2026 outlook | Management-prepared; balance sheet differs from the 10-K | CP-1, CP-1A |
| S6 | EX-99.1_2026-04-30_tree-33126xer.htm.jsonl | Medium: issuer press release | Q1 2026 | Same | Q1 2026 results, Q1 net leverage statement, updated outlook | Management-prepared | CP-1A |
| S7 | EX-99.1_2026-07-29_tree-63026xer.htm.jsonl | Medium: issuer press release | Q2 2026 | Same | Q2 2026 results, Q1 2026 comparatives, lowered outlook | Management-prepared | CP-1, CP-1A |
| S8 | context | User settings, not issuer evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage down from 4.56x to 2.58x on issuer-defined Adjusted EBITDA; 3.05x if non-cash compensation is a cost | CP-1, CP-2 | Gross principal and Adjusted EBITDA from S1 and S4; recomputed | Sets leverage tolerance and the credit view | Core metric | S1 page:96, page:149; S4 page:18, page:38 | EBITDA is issuer non-GAAP; covenant EBITDA not supplied |
| 2 | Liquidity of USD 185.8 million against USD 4.0 million due in twelve months; maturity August 21, 2030 | CP-1, CP-2 | Cash, revolver and current portion in S4 | Low near-term default and refinancing risk | Monitoring horizon | S4 page:2, page:18, page:19, page:39 | Letters of credit not supplied; status after July 30, 2026 not supplied |
| 3 | Insurance concentration: 66.8% of Q2 2026 revenue and a 27% partner | CP-1A, CP-2 | Segment tables in S4; partner share in S1 | Earnings depend on carrier budgets and media cost | Sets business risk | S4 page:21; S1 page:12 | Contracts and 2026 partner share not supplied |
| 4 | Margin pressure and lowered 2026 outlook; Q2 2026 below April guidance | CP-1A, CP-2 | S4 variable marketing margin; S6 and S7 outlook | Cash flow available for debt service falls faster than revenue in a weak quarter | Monitoring trigger | S4 page:36, page:38; S6 page:3; S7 page:3 | Outlooks are management claims |
| 5 | Covenant and debt capacity untested because the credit agreement is not in the pack | CP-1A, CP-2 | Issuer summary in S1 | Restricted payments, incremental debt and guarantors unknown | Limits creditor-control conclusions | S1 page:145, page:146, page:161 | Agreement not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 4.56x, 3.00x, 2.58x and net 3.54x, 2.39x, 1.86x | CP-1, CP-2 | S1 page:149; S4 page:18, page:38; calculation C5 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Liquidity of USD 185.8 million | CP-1, CP-2 | S4 page:2, page:19, page:39 | Yes | High | Calculated | Supported | High | Recomputed equal |
| Facility terms: first lien, August 21, 2030, 5.00 to 1.00 covenant, USD 20.0 million trigger | CP-1, CP-1A, CP-2 | S1 page:144 to page:146 | Yes | High; issuer summary of an agreement | Directly Sourced | Supported as a description | Medium | Traced |
| Debt structure and maturity: USD 4.0 million within twelve months, USD 393.0 million after | CP-1, CP-2 | S4 page:18 | Yes | High | Directly Sourced | Supported | High | Traced |
| Covenant headroom and covenant EBITDA | CP-1, CP-2 | Credit agreement not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Cash interest cover 4.42x | CP-1, CP-2 | S1 page:112; S4 page:4, page:38 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Free cash flow USD 73.9 million | CP-1, CP-2 | S1 page:111, page:112; S4 page:4 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Insurance 63.7% and 66.8% of revenue | CP-1A, CP-2 | S1 page:11; S4 page:21 | Yes | High | Calculated | Supported | High | Recomputed equal |
| Progressive Casualty Insurance 27% of FY2025 revenue | CP-1A, CP-2 | S1 page:12 | Yes | High | Directly Sourced | Supported | High | Traced |
| Founder's death, CEO change, heirs' stake of about 18% before death | CP-1A, CP-2 | S1 page:37, page:68 | Yes | High | Directly Sourced | Supported | High | Traced |
| Outlook lowered to USD 145 to 152 million of Adjusted EBITDA | CP-1A, CP-2 | S5 page:4; S6 page:3; S7 page:3 | Yes | Medium; management claim | Directly Sourced | Supported as a management statement | Medium | Traced |
| Floating-rate exposure with no hedge disclosed | CP-2 | S4 page:40; S1 page:105; search of all sources for swap, cap, hedging and derivative | Yes | High; absence of disclosure | Analyst Inference | Partially supported | Medium | Inference from absence, labelled |
| Illustrative incremental first lien capacity of USD 190.0 million | CP-2 | S1 page:145 and calculation P5 | Yes | High inputs, unsupplied definition | Assumption-Based | Partially supported | Low | Labelled illustrative; definition missing |
| Moderate and improving credit view | CP-2 | CP-1, CP-1A | Yes | High inputs | Analyst Inference | Partially supported: the phrase low for a high yield issuer has no source | Medium | Traced except one phrase |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue FY2025 1,117,324 | /workspace/secdata/data/2026-11-05/packs/1434621-lendingtree-inc-tree | 10-K_2025-12-31_tree-20251231.htm.jsonl | S1 | page:110, statement of operations | CP-1 income statement | Reported | High | Matches |
| Cash 81,073 and 106,594 | same | same | S1 | page:109, balance sheet | CP-1 balance sheet and liquidity | Reported | High | CP-1 cites page:110; rows are on page:109 (QA-2) |
| Gross term loan 399,000 | same | same | S1 | page:149, Note 13 table | CP-1 debt table | Reported | High | 4,000 plus 395,000 |
| Gross term loan 397,000 at Jun 30, 2026 | same | 10-Q_2026-06-30_tree-20260630.htm.jsonl | S4 | page:18, Note 10 | CP-1 debt table | Reported | High | 4,000 plus 393,000; carrying value ties after issuance costs and discount |
| Adjusted EBITDA FY2025 132,887 | same | S1 file | S1 | page:96 | CP-1 leverage | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Adjusted EBITDA H1 2026 77,171 and H1 2025 56,419 | same | S4 file | S4 | page:38 | CP-1 LTM | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Interest paid 37,203; 16,031; 18,494 | same | S1 and S4 files | S1, S4 | S1 page:112; S4 page:4 | CP-1 coverage | Reported | High | Matches |
| Operating cash flow 40,717 and capital expenditures 5,935 for H1 2026 | same | S4 file | S4 | page:4 | CP-1 free cash flow | Reported | High | Matches |
| Covenant 5.00 to 1.00 tested above USD 20.0 million of revolver usage | same | S1 file | S1 | page:145 | CP-1, CP-1A, CP-2 | Reported description | High | Issuer summary; agreement not supplied |
| Revolver USD 75.0 million, no borrowings at Jun 30, 2026 | same | S4 file | S4 | page:19; page:39 | CP-1 liquidity | Reported | High | Letters of credit not stated |
| Progressive Casualty Insurance 27% of FY2025 revenue | same | S1 file | S1 | page:12 | CP-1A concentration | Reported | High | Matches |
| Founder owned about 18% before his death | same | S1 file | S1 | page:68 | CP-1A ownership | Reported | High | Matches |
| Moody's B2 stable condition achieved January 2026 | same | S1 file | S1 | page:145 | CP-1, CP-1A | Reported | High | Rating document not supplied |
| Q2 2026 Adjusted EBITDA guide of USD 38 to 40 million | same | EX-99.1_2026-04-30_tree-33126xer.htm.jsonl | S6 | page:3 | CP-1A outlook table | Management outlook | Medium | Actual 35,162 on S4 page:38 |
| Q4 2025 release balance sheet prepaid 49,053 against 10-K 38,053 | same | EX-99.1_2026-03-02_tree-123125xer.htm.jsonl and S1 file | S5, S1 | S5 page:5; S1 page:110 | CP-1, CP-1A conflicts | Reported | Medium | Logged conflict, not reconciled |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM amounts | CP-1 C1; all later modules | FY2025, H1 2026, H1 2025 | FY2025 + H1 2026 − H1 2025 | Recomputed from the table inputs: 9 of 9 equal | Supported | High | Basis of every LTM ratio | S1 page:96, page:110 to page:112; S4 page:2 to page:4, page:38 |
| Unadjusted EBITDA | CP-1 C3 | Net income, interest, tax, depreciation, amortization | Sum | Recomputed: 7 of 7 equal | Supported | High | Leverage sensitivity | S1 page:110; S4 page:3 |
| Debt, cash and net debt | CP-1 C4 | Gross principal, carrying values, cash | Gross principal less cash | Recomputed: equal; carrying tie-out equal | Supported | High | Leverage numerators | S1 page:149; S4 page:2, page:18 |
| Leverage ratios | CP-1 C5; CP-2 | Debt, net debt, Adjusted EBITDA | Debt divided by EBITDA | Recomputed: 12 of 12 equal; management 2.4x and 3.5x agree | Supported | High | Core ratios | S5 page:2 |
| Coverage ratios | CP-1 C6 | Adjusted EBITDA, interest paid, interest expense | EBITDA divided by interest | Recomputed: 14 of 14 equal | Supported | High | Debt service | S1 page:112; S4 page:4 |
| Free cash flow and Q2 discrete derivations | CP-1 C7, C12 | Operating cash flow, capital expenditures, Q1 2026 values | Operating cash flow less capital expenditures; H1 less Q1 | Recomputed: 8 of 8 equal | Supported | High | Cash conversion | S3 page:3, page:4; S4 page:4 |
| Margins and mix | CP-1 C8, C11; CP-1A C1; CP-2 | Revenue, Adjusted EBITDA, variable marketing margin, segment revenue | Ratios | Recomputed: 14 of 14 margin checks equal; mix ratios equal | Supported | High | Mix and margin pressure | S4 page:21, page:36 |
| Add-back sensitivity | CP-1 C9 | LTM non-cash compensation 23,632 | Adjusted EBITDA less non-cash compensation | Recomputed: 3.054x and 2.202x equal | Supported | High | Definition risk | S1 page:96; S4 page:38 |
| Guidance arithmetic | CP-1A C2; CP-2 P8 | Guide ranges and actuals | Differences | Recomputed: equal | Supported | High | Q2 shortfall | S6 page:3; S4 page:36, page:38 |
| Progressive share of Insurance revenue 42.4% | CP-1A C3; CP-2 | Rounded 27% of revenue | 27% × revenue ÷ Insurance revenue | Recomputed: equal; approximate | Supported with rounding caveat | Medium | Concentration | S1 page:11, page:12 |
| EBITDA sensitivity | CP-2 P1 | LTM Adjusted EBITDA and principal | Debt ÷ (EBITDA × (1 − decline)) | Recomputed: 2.871x, 3.230x, 3.691x, 4.307x, 48.3% equal | Supported | High | Downside | CP-1 inputs |
| Interest sensitivity | CP-2 P2 | Principal 397,000 | 1% × principal | Recomputed: 3,970 equal; matches the 10-Q figure of USD 4.0 million | Supported | High | Rate risk | S4 page:40 |
| Illustrative incremental capacity | CP-2 P5 | 3.10 × Adjusted EBITDA less net debt | Ratio × EBITDA − net debt | Recomputed: 190,047 equal; definition not supplied | Assumption-based | Low | Debt capacity | S1 page:145 |
| Asset composition | CP-2 P6 | Goodwill, intangibles, total assets, equity | Sums and ratios | Recomputed: 45.7% and −96,283 equal | Supported | High | Hard-asset cover | S4 page:2 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial gate, 1 MATERIAL, 5 MINOR | Script formula | 30, band Insufficient Information | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 credit view | The opening sentence says leverage is low for a high yield issuer; no peer, market or ratings data is in the pack | Unsupported Claim | A comparative claim in the headline sentence without a source, in a module that prohibits peer ranking | Delete the phrase; state the ratio only | CP-2 handoff, Credit view and Reader summary context |
| MINOR | CP-1 balance sheet | Cash rows cited as page:110 are on page:109 | Imprecise locator | A reader checking the page finds the table midway | Cite page:109 and page:110 | CP-1 handoff |
| MINOR | CP-1 chart and metrics tables | Basis cells give the arithmetic but omit the page for Adjusted EBITDA (S1 page:96, S4 page:38) | Citation Gap | Slower verification | Add the pages to the basis cells | CP-1 handoff |
| MINOR | CP-1A governance table | Row on the refinancing says capacity was permitted by the new agreement and the refinancing was lender-agreed at par; the agreement is not supplied and the source says only repaid with the new loan and cash at par | Partially Supported Claim | Implies knowledge of agreement terms | Replace with the sourced statement | CP-1A handoff |
| MINOR | CP-2 key finding on incremental capacity | The USD 190.0 million figure is illustrative and uses issuer Adjusted EBITDA and total net debt | Formula / Definition Drift | Could be read as a capacity estimate | Keep the label illustrative; do not carry the figure downstream | CP-2 handoff |
| MINOR | CP-1 discrete quarters note | The sentence "The four quarters Q1 2025 to Q4 2025 are not all shown" is unclear; all four are used in the sum check | Clarity | Minor reading burden | Reword | CP-1 handoff |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; each filing identifies itself on its cover | A wrong document would change every figure | None found | None |
| Locator precision | Good | 80 of 80 quotations on cited pages; one balance sheet locator on the wrong page; four cells cite two files | Slower checks and a risk of misplaced citations | None on conclusions | Exact page ranges |
| Calculation reproducibility | Strong | 64 of 64 table ratios and 51 of 51 tie-outs recomputed equal; Adjusted EBITDA reconciliations re-added equal in 9 periods | Calculation errors would move leverage and cover | None found | None |
| Cross-module consistency | Good | CP-2 figures all found in CP-1, CP-1A or its own calculations; four are rounded restatements | Rounded restatements can drift from the source cell | None found | Reference exact cells |
| Claim discipline | Adequate | One unsupported comparative phrase in CP-2; other claims labelled by category | Unsupported comparatives mislead a committee | Headline view overstated by one phrase | Delete the phrase |
| Reviewer independence | Weak | The host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Credit agreement and covenant definitions | August 21, 2025 Credit Agreement (exhibit 10.39, S1 page:161) | Covenant headroom, guarantors, restricted payments, letters of credit unknown | Covenant and capacity rows in CP-1A and CP-2 | Caps committee status and lowers the score through the partial source gate | Form 8-K filed August 21, 2025, exhibit 99.1 |
| G2 | Events after July 30, 2026 | Q3 2026 10-Q and release, later 8-Ks | The view is stale against the November 5, 2026 cutoff; guidance was already lowered once | Whole run | Lowers currency of the view | Filings to the cutoff date |
| G3 | Ownership detail | 2026 proxy statement, holder list, unnamed 20% holder | Control and succession not assessable | Governance rows | Moderate | Definitive proxy statement |
| G4 | Partner concentration in 2026 | Partner contracts, later disclosure | Cannot size 2026 Insurance exposure | Concentration risk | Moderate | Later filings |
| G5 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Another agent or model |
| G6 | Extraction fidelity | Original HTML and XBRL | Small risk of table misreads | Figures from flattened tables | Slight | Filed HTML |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 3 / tree-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted on attempt 3 after two refusals for a word count and for numbers absent from the body | Passed with no open finding | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, chart data | High | Six headings; accepted | Passed with three MINOR findings | 64 of 64 ratios recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, ownership, governance, timeline, outlook | High | Six headings; accepted | Passed with one MINOR finding | Two conflicts logged, not reconciled |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Restricted: one MATERIAL and one MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 | Credit view: leverage now low for a high yield issuer | Unsupported | No peer, market or ratings data is supplied | Delete the phrase | Restricts Committee Use |
| MINOR | CP-1 | Balance sheet cash rows | Supported | Cited page:110, on page:109 | Cite page:109 | Formatting / Hygiene Only |
| MINOR | CP-1 | Leverage and cover basis cells | Supported | Adjusted EBITDA page omitted | Add S1 page:96 and S4 page:38 | Formatting / Hygiene Only |
| MINOR | CP-1A | Refinancing governance row | Partially Supported | Agreement terms implied | Use the sourced statement | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Illustrative incremental capacity of USD 190.0 million | Uses issuer Adjusted EBITDA and total net debt; the agreement tests first lien net leverage on its own EBITDA | None between sources; definition not supplied | Keep the illustrative label; do not carry the figure downstream | Monitoring Follow-Up |
| MINOR | CP-1 | Adjusted EBITDA as the leverage denominator | Issuer non-GAAP; adds back non-cash compensation and litigation | None | Keep the unadjusted ratios beside it, as CP-1 does | Monitoring Follow-Up |
| MINOR | CP-1 | Total debt to unadjusted EBITDA of 32.39x for FY2024 | FY2024 unadjusted EBITDA includes 54,162 of other expense | None | Keep the distortion note, as CP-1 does | Formatting / Hygiene Only |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-1A, CP-2 | Covenant test, security, guarantee, incremental debt and soft call terms | Executed 2025 Credit Agreement | Only the issuer's note summary is supplied; borrower and guarantor entities not named | Supply the agreement; keep descriptions labelled as summaries | Required before any covenant or capacity conclusion |
| MINOR | CP-1A | Anti-takeover provisions and change of control | Charter, by-laws and credit agreement | Summary from the 10-K only; the by-laws amended in November 2025 are not supplied | Supply by-laws | Not needed for the selected modules |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 | Leverage described as low for a high yield issuer | Peer leverage distribution or ratings data | No market or peer data in the pack | Delete the phrase | Committee cannot rely on the comparison |
| MINOR | All modules | No bond prices, spreads or ratings are used; the Moody's B2 condition is quoted from the 10-K only | Prices, spreads and rating reports | Outside the minimum source pack | Add market data only from a sourced step | Committee cannot judge relative value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Q4 2025 release balance sheet shows prepaid and other current assets of 49,053 and total current assets of 240,708; the 10-K shows 38,053 and 229,708 (S5 page:5; S1 page:110) | Release and 10-K are separate sources; the 10-K controls | Keep logged, do not reconcile | None on conclusions |
| MINOR | CP-1A | Release says the tax benefit reduced the "full valuation allowance"; the 10-K says a partial allowance remains (S5 page:1; S1 page:56, page:102) | Separate sources | Keep logged | None on conclusions |
| MINOR | CP-2 | Rounded restatements of CP-1 figures: 185.8, 474.7, 77.7 and 96.3 | CP-2 cites CP-1 hash 66d19075 and CP-1A hash 27aa6bb2, both current | Reference exact figures | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | Run | Committee readiness | The financial and business views trace; covenant protection does not, one headline phrase is unsupported, and the review is a self-review | Supply the credit agreement, remove the phrase, add an independent review | Committee status Restricted |
| MINOR | CP-1, CP-1A, CP-2 | Duplication | The Insurance concentration and the outlook are restated in all three modules | Keep one source of record, CP-1A | None |
| MINOR | Releases | Duplication | Releases repeat the 10-Q statements; handoffs treat the filings as controlling | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Reader summary | Attempt 1 refused for a 31-word finding; attempt 2 refused for two numbers (75.0 and 2030) missing from the body | Resolved in attempt 3 | Resolved; attempt 3 accepted |
| MINOR | CP-1, CP-1A, CP-2 | Reader summary and selectors | Accepted first time; word limits and number matches checked by script | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MATERIAL | CP-2 | Unsupported Claim | Leverage described as low for a high yield issuer without peer data | Delete the phrase | Restricts Committee Use | Open |
| QA-2 | MINOR | CP-1 | Citation Gap | Cash rows cited page:110, on page:109 | Cite page:109 | Formatting / Hygiene Only | Open |
| QA-3 | MINOR | CP-1 | Citation Gap | Adjusted EBITDA page omitted from chart basis cells | Add pages | Formatting / Hygiene Only | Open |
| QA-4 | MINOR | CP-1A | Partially Supported Claim | Refinancing row implies agreement terms | Use the sourced statement | Formatting / Hygiene Only | Open |
| QA-5 | MINOR | CP-2 | Formula / Definition Drift | Illustrative capacity could be misread | Keep the illustrative label | Monitoring Follow-Up | Open |
| QA-6 | MINOR | CP-1 | Clarity | Unclear sentence on quarters | Reword | Formatting / Hygiene Only | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Every double-quoted span of 12 or more characters in the CP-0, CP-1 and CP-1A handoffs searched in the pinned page text after normalising quotes and spacing; the page cited on the same line compared with the pages where the span is found | 85 spans parsed, 5 were search terms or parsing artifacts, 80 quotations; 80 found, none misquoted; 4 cells cite two files and were checked by hand; CP-2 quotes nothing |
| Q2 | Reported-figure trace | Every figure with a thousands separator in the CP-1 body (before its calculations) searched in the pinned page text | All reported figures found; the rest are calculated figures with a stated formula |
| Q3 | Locator check on figures | Each figure on a line with a page locator searched for the pages where it occurs | 21 figure and page pairs flagged; reviewed by hand: 1 real mislocation (QA-2), the Adjusted EBITDA rows that omit a page (QA-3), and the rest lines where a figure sits beside locators cited for other statements |
| Q4 | Ratio recomputation | CP-1 Financials and credit metrics table parsed; LTM, unadjusted EBITDA, free cash flow, margins, cover and leverage rows recomputed from the table's own base rows | 64 checks, 0 mismatches |
| Q5 | Tie-outs | Income statement identities (6 columns × 4); Adjusted EBITDA reconciliations (9 periods); segment sums (6); variable marketing margin (4); balance sheet identities (6); cash flow roll-forwards (2) | 51 of 51 equal |
| Q6 | CP-2 figures | Each CP-2 figure searched in CP-1, CP-1A and CP-2 calculations | All found; 185.8, 474.7, 77.7 and 96.3 are rounded restatements of 185,766, 474,682, 77,682 and 96,283 |
| Q7 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:5,Calculated:5,Assumption-Based:1,Analyst Inference:2,Insufficient Information:1" --fields-present 17 --fields-total 17 --source-gate partial --findings MATERIAL:1,MINOR:5` | E = 77.14, C = 100, S = 0.7, P = 30; score = clamp((0.6 × 77.14 + 0.4 × 100) × 0.7 − 30) = 30.4, rounded to 30; band Insufficient Information; qa_status Restricted |

## Gaps

- G1 Critical for covenant conclusions: the credit agreement is not supplied, so covenant headroom, guarantors, restricted payments and letters of credit rest on issuer summaries.
- G2: nothing after July 30, 2026 is supplied, including any Q3 2026 results.
- G3 and G4: the proxy statement, holder list, unnamed 20% holder and 2026 partner concentration are not supplied.
- G5: no independent review; this CP-5 was written by the same host as the four handoffs it checks.
- G6: text extraction only, with no original HTML or XBRL.

## Next module

- Report delivery: carry `qa_status` Restricted, Confidence Score 30, committee status Restricted, and gap G1; flag the unsupported phrase in the CP-2 credit view (QA-1) so the report does not repeat it.
- Repair: because accepted answers cannot be replaced, a new run folder is needed to correct QA-1 to QA-6; the first correction is to delete the comparison with high yield issuers.
- Independent review: another agent or model should repeat this check, starting with omissions.
- Sourcing: obtain the August 21, 2025 Credit Agreement, the 2026 proxy statement and any filing after July 30, 2026, then rerun CP-1A, CP-2 and CP-5.
