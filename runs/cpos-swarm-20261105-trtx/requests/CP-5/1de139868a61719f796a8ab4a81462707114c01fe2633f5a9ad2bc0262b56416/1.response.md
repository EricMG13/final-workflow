## Request

- Issuer: TPG RE Finance Trust, Inc. (issuer id trtx), as of 2026-11-05, information cutoff 2026-11-05. Pathway credit_snapshot, reporting currency USD, current period Q3 2026, prior period FY2025.
- Scope: CP-5 checks the evidence trace of the four earlier handoffs (CP-0, CP-1, CP-1A, CP-2) against the seven pinned filings and releases and grades the result (absorbed CP-5A phase). Traceability scope is Top 5 material credit drivers, plus the 12 material claims listed in the traceability map.
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called and no external source was used.
- QA envelope: qa_status Passed; Confidence Score 40, band Low (from the repository script `confidence_score.py`, see Calculations); committee_status Requires More Work.

## Sources

### Issuer sources relied on

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_trtx-20251231.htm.jsonl | 7b7b804dc956c7ba20b8c615f59942074ed4837f19257133ae8d92323027d7ec |
| 10-Q_2026-03-31_trtx-20260331.htm.jsonl | 41f66a4a0f2f9734dca4554ee0dc2ef549772c06941cdfec976d06a5c1955d4c |
| 10-Q_2026-06-30_trtx-20260630.htm.jsonl | 8f3da972b3575ac6703be3527817c87d3dc87cac2d5c8e1d4e7f81f5f78727e9 |
| 10-Q_2026-09-30_trtx-20260930.htm.jsonl | 4884d7a3b9e5f3a0f552349b7976aff0931070e9957fb8740966840f61145adc |
| EX-99.1_2026-04-28_trtx-20260428exhibit991.htm.jsonl | 1e95941ab9e70def087e8a13656b49994337a0e1c905b17c9ac6471bddea9d88 |
| EX-99.1_2026-07-28_trtx-20260728exhibit991.htm.jsonl | 85e111cdb3f106d12964e884db844b225d24404d7815e760f617225c97335579 |
| EX-99.1_2026-10-26_trtx-20261026exhibit991.htm.jsonl | 262caea8fdb587a93bfd4ce5d18d486a64c133d5eee9d2c7316a1e31375c2fe8 |

### Context file

| Source name | sha256 |
| --- | --- |
| context | ef96ebbdf5dd00ebb7411d32513edde7f00e3900728e79b850efc1744349d270 |

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | f67c880ae13bd9b442ec32f542cac48afaa8a23c51c32c03c025a6a9e94e025f |
| CP-1 | d2958939fbb55f95e859a0d7163b8ff7248dbe00f5d7f7b77f17ee8c523f59b6 |
| CP-1A | e9ba717d917e30ef3c668cde0f21b63a9fea05354ce81f77b2059a6d35b0735a |
| CP-2 | 09a0122245e5629b0912ed636f0666479996d5ce423a4b43df8d4b99246cd5b2 |

Locators are `page:N` chunks of the named file, not printed pages. Source document ids S1 to S8 are defined in the source register.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is traceable to the filings for its main conclusions: every derived figure was recomputed and every quotation found. Covenant values, executed agreements and independent review are missing, so committee use should stay restricted. | Medium | Covenant test values, executed credit agreements and guarantor lists are not in the pack, so recourse and headroom findings rest on filing summaries and inference. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 106 derived figures recomputed from cited inputs matched the earlier analyses, and all 18 quoted passages were found word for word in the filings. | Reported leverage, liquidity and earnings figures can be relied on as faithful to the filings. | High |
| Six minor defects were found, mainly page or unit locators and one overstated statement that the loan book is entirely senior first mortgage loans. | None changes a credit conclusion; the seniority statement should reflect about 2.3% of commitments in mezzanine or subordinate pieces. | High |
| The cash held for the liquidity covenant matches five percent of computed recourse exposure only on one basis, so it is an inference. | Treat it as a monitoring indicator, not a covenant measurement. | Medium |
| All four reviewed analyses were written by the same analyst session as this check, so there is no independent review. | Omissions are the likeliest undetected error, so an independent repeat is advised. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 3 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of covenant test values and executed credit agreements, which matters because covenant headroom, the recourse base and the guarantor package can then be read only from filing summaries and inference, and it implies that committee use stays restricted until they are supplied. The unsupported claim to correct is that the loan book is entirely senior first mortgage loans; the affected decision is leverage tolerance; the remediation owner is the sourcing step.

### Traceability summary

| Check | Result |
| --- | --- |
| Quoted passages found in the filings | 18 of 18 |
| Derived figures recomputed from cited inputs | 106 of 106 equal |
| Statement and ratio tie-outs re-added | 38 of 38 equal |
| Statement-table numbers found verbatim in the sources | 418 of 432; the other 14 are derived and recomputed |
| Locator-bearing statements screened | 347; 6 imprecise, 341 resolve |
| Material claims by lineage | 4 Directly Sourced, 3 Calculated, 2 Assumption-Based, 2 Analyst Inference, 1 Insufficient Information |
| Open findings | 6 MINOR |
| Confidence Score and band | 40, Low |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_trtx-20251231.htm.jsonl | High: filed, audited annual report | Year ended 2025-12-31 with 2024 and 2023 comparatives | TPG RE Finance Trust, Inc., consolidated incl. VIEs | Statements, notes, manager terms, leverage expectation, liquidity | Text extraction; fidelity not reviewed | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_trtx-20260331.htm.jsonl | High: filed, unaudited interim report | Quarter ended 2026-03-31 | Same | Interim statements, funding, liquidity, covenants | Unaudited; text extraction | CP-0, CP-1 |
| S3 | 10-Q_2026-06-30_trtx-20260630.htm.jsonl | High: filed, unaudited interim report | Quarter and six months ended 2026-06-30 | Same | Statements, Term Loan B and Revolver, repurchase program | Unaudited; text extraction | CP-0, CP-1, CP-1A |
| S4 | 10-Q_2026-09-30_trtx-20260930.htm.jsonl | High: filed, unaudited interim report | Quarter and nine months ended 2026-09-30 | Same | Latest statements, funding, recourse, liquidity, covenants, subsequent events | Unaudited; text extraction | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-28_trtx-20260428exhibit991.htm.jsonl | Medium: issuer press release | Q1 2026 | Same | Headline results, Distributable Earnings, management statements | Management attribution; non-GAAP | CP-1, CP-1A |
| S6 | EX-99.1_2026-07-28_trtx-20260728exhibit991.htm.jsonl | Medium: issuer press release | Q2 2026 | Same | Headline results, covenant cash held, Term Loan B and Revolver | Management attribution; non-GAAP | CP-1, CP-1A |
| S7 | EX-99.1_2026-10-26_trtx-20261026exhibit991.htm.jsonl | Medium: issuer press release | Q3 2026 | Same | Headline results, liquidity, subsequent events, reconciliation | Management attribution; non-GAAP | CP-1, CP-1A, CP-2 |
| S8 | context | Run settings, not issuer evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Deal terms, ratings, peers, quotes empty | All modules |
| H0 | CP-0 handoff, attempt 1 | Derived: source readiness | As of 2026-11-05 | Same | Source map and limits | Self-review | CP-1, CP-1A, CP-2, CP-5 |
| H1 | CP-1 handoff, attempt 2 | Derived: financial base | Q3 2026, FY2025 | Same | Statements, funding, liquidity, ratios | Self-review | CP-1A, CP-2, CP-5 |
| H2 | CP-1A handoff, attempt 1 | Derived: business and transaction | Same | Same | Business, manager, transactions, governance | Self-review | CP-2, CP-5 |
| H3 | CP-2 handoff, attempt 1 | Derived: credit synthesis | Same | Same | Credit view, strengths, weaknesses, risks | Self-review | CP-5 |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage rose from 3.02x to 4.03x on higher debt and lower equity | CP-1, CP-2 | Issuer-printed debt principal, equity and ratios | Equity cushion beneath creditors shrinks as debt grows | Sets leverage tolerance and the comparison with the 3.75:1 expectation | S4 page:7, page:89, page:104-105; S1 page:15 | Basis of the 3.75:1 expectation after the Term Loan B is not stated |
| 2 | Thin usable liquidity against unfunded commitments | CP-1, CP-2 | Liquidity table, cash held for covenants, unfunded commitments | Funding promises are close to usable liquidity | Sets liquidity risk and dependence on repayments | S4 page:28, page:72, page:77, page:105, page:108 | Secured credit agreement availability depends on lender-approved collateral |
| 3 | Earnings below the dividend after realized losses | CP-1, CP-2 | Reconciliation of net income to Distributable Earnings and dividends declared | Distributions drawn from equity reduce the cushion | Sets earnings-cover view and equity trend | S4 page:7-9, page:81; S7 page:8 | Distributable Earnings is an issuer non-GAAP measure |
| 4 | Recourse layering and 2028 refinancing cluster | CP-1, CP-2 | Printed recourse percentages and maturity schedule | Parent-level claims and extension dependence drive refinancing risk | Sets claim structure and refinancing view | S4 page:56-57, page:89 | Executed agreements and guarantor list not supplied |
| 5 | Stable asset-quality indicators with rising office exposure | CP-1A, CP-2 | Risk ratings, non-accrual status, allowance, property-type tables | Loss emergence drives equity erosion | Sets collateral view | S4 page:34, page:37, page:72, page:116; S3 page:71 | Loan-to-value is measured at origination, not current |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total leverage 4.03x and debt-to-equity 3.64x | CP-1 | Printed ratios and principal balances | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Liquidity after covenant cash about equal to unfunded commitments | CP-1, CP-2 | Liquidity table less 52.6 million covenant cash against 236,552 thousand | Partial: unit and page precision | High | Calculated | Supported | Medium | Remediation Needed |
| Earnings and dividend cover below one after realized losses | CP-1, CP-2 | Reconciliation, dividends declared | Yes | High | Calculated | Supported | High | Committee-Ready |
| Recourse layering: 664,963 thousand fully recourse, 1,051,727 thousand nominal | CP-1 | Recourse percentages and principal | Yes | High | Calculated | Supported | High | Committee-Ready |
| 2028 maturity cluster of 1,130,841 thousand | CP-1, CP-2 | Maturity schedule | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Stable asset quality: rating 3.0, no non-accrual, allowance 147 bp | CP-1, CP-1A, CP-2 | Risk-rating and allowance tables | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Office exposure rose from 4.3% to 7.9% | CP-1, CP-1A | Property-type tables and loan 4 listing | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Covenant cash of 52.6 million is consistent with five percent of recourse exposure | CP-1, CP-2 | Computed exposure and printed cash held | Yes | Medium | Assumption-Based | Partially Supported | Medium | Remediation Needed |
| Indicative debt to assets 80.1% against 83.333% and a 3.9% asset cushion | CP-1, CP-2 | Principal over total assets; covenant level printed | Yes | Medium | Assumption-Based | Partially Supported | Low | Remediation Needed |
| Manager alignment is indirect; fee base exceeds GAAP equity | CP-1A, CP-2 | Fee terms and implied base | Yes | Medium | Analyst Inference | Supported | Medium | Committee-Ready |
| Overall credit view: adequate with a weakening trend | CP-2 | Synthesis of the rows above | Yes | Medium | Analyst Inference | Supported | Medium | Committee-Ready |
| Covenant headroom and EBITDA-based leverage | CP-1, CP-2 | No test values or EBITDA in any source | No | No source supplied | Insufficient Information | Insufficient Information | Low | Not Traceable |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt principal 4,198,054 thousand at 2026-09-30 | packs/1630472-tpg-re-finance-trust-inc-trtx-trtx-pc | 10-Q_2026-09-30_trtx-20260930.htm.jsonl | S4 | page:89 financing table | CP-1 Funding structure | Documentary Fact | High | Total indebtedness printed |
| Total leverage 4.03x, debt-to-equity 3.64x | Same | S4 file | S4 | page:104-105 | CP-1 Financials | Documentary Fact | High | Issuer definitions |
| Near-term liquidity 291,634 thousand | Same | S4 file | S4 | page:105 | CP-1 Liquidity | Documentary Fact | High | Issuer table |
| Cash held for covenants 52.6 million | Same | S4 file | S4 | page:28, page:77 | CP-1 Liquidity | Documentary Fact | High | Also release page:3 |
| Recourse: secured credit agreements 25%, secured revolver and Term Loan B 100%, HSBC 20% | Same | S4 file | S4 | page:47-48, page:52-53, page:56, page:89 | CP-1 Funding structure | Documentary Fact | High | Summaries, not executed documents |
| 2028 maturities 1,130,841 thousand | Same | S4 file | S4 | page:57 | CP-1 Chart data | Documentary Fact | High | CLO dates are fully extended collateral maturities |
| Covenant levels and compliance statement | Same | S4 file | S4 | page:54-57 | CP-1 Covenants | Documentary Fact | High | Test values not printed |
| Net income 9,366 thousand; Distributable Earnings 5,118 thousand | Same | S4 and S7 files | S4, S7 | S4 page:7-8, page:81; S7 page:8 | CP-1 Earnings measures | Documentary Fact; non-GAAP for Distributable Earnings | High | Issuer definition |
| Risk rating 3.0, no non-accrual, allowance 76,143 thousand | Same | S4 file | S4 | page:34-35, page:37 | CP-1 Credit quality | Documentary Fact | High | Unaudited |
| Office exposure 4.3% then 7.9% | Same | S3, S4 files | S3, S4 | S3 page:71; S4 page:72, page:116 | CP-1A Logged differences | Documentary Fact | High | Release statement of April 2026 is Management Language |
| Management fee 1.50% of Equity; no incentive fee | Same | S4 and S1 files | S4, S1 | S4 page:62-63; S1 page:232 | CP-1A Ownership and control | Documentary Fact | High | Equity definition not supplied |
| Leverage expectation below 3.75:1 | Same | S1 file | S1 | page:15 | CP-1A Logged differences | Management Language | High | Expectation, not a covenant |
| Term Loan B terms and security | Same | S4 file | S4 | page:56 | CP-1A Transaction summary | Documentary Fact | High | Guarantors not named |
| TRTX 2026-FL8 closing and 820.0 million placed | Same | S4 and S7 files | S4, S7 | S4 page:74; S7 page:4 | CP-1A Transaction summary | Documentary Fact; subsequent event | High | Use of proceeds not stated |
| Affiliate payments to TPG entities | Same | S4 file | S4 | page:63-65 | CP-1A Governance | Documentary Fact | High | Rounded to 0.1 million |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net debt over equity | CP-1, CP-2 | Principal 4,198,054, cash 70,826, equity 1,024,126 (thousand) | (principal - cash) / equity | Verified: 4.03x equals printed | Supported | High | Leverage level | S4 page:6-7, page:89, page:104 |
| LTM income statement figures | CP-1 | FY2025, 9M 2026, 9M 2025 amounts | FY2025 + 9M 2026 - 9M 2025 | Verified: 9 of 9 equal | Supported | High | Earnings trend | S1 page:178-181; S4 page:7-10 |
| Nominal recourse exposure | CP-1, CP-2 | Principal and printed recourse percentages | 0.25 x 1,522,156 + 0.20 x 31,125 + 264,963 + 400,000 = 1,051,727 | Verified arithmetic; percentages are caps with carve-outs | Partially Supported | Medium | Parent claim size | S4 page:89, page:92 |
| Cash covenant match | CP-1, CP-2 | Assumption: recourse indebtedness equals nominal exposure without the mortgage-loan guarantee | 5% x 1,051,727 = 52,586 against 52.6 million held | Inference: holds on one basis only | Partially Supported | Medium | Liquidity trap | S4 page:28 |
| Indicative debt to total assets | CP-1, CP-2 | Assumption: covenant uses GAAP principal and total assets | 4,198,054 / 5,242,861 = 80.1% against 83.333% | Inference: definition not supplied | Partially Supported | Low | Covenant headroom | S4 page:57 |
| Distance to 3.75x | CP-2 | Assumption: expectation measured on net debt over equity | 4,127,228 - 3.75 x 1,024,126 = 286,755 | Verified arithmetic; basis assumed | Partially Supported | Medium | Leverage tolerance | S1 page:15 |
| Distributable Earnings cover | CP-1, CP-2 | 55,256 and 42,250 against 56,667 declared (thousand) | Earnings / dividends declared | Verified: 0.98x and 0.75x | Supported | High | Dividend cover | S4 page:8-9, page:81; S5-S7 page:8 |
| Book assets above asset-level debt | CP-2 | Total assets less 3,798,054 of asset-level debt | 5,242,861 - 3,798,054 = 1,444,807 | Verified arithmetic; book values, not recovery | Supported | Medium | Claim structure | S4 page:7, page:46 |
| Implied management fee base | CP-1A, CP-2 | Q3 2026 fee 5,326 thousand | 5,326 / 0.375% = 1,420,267 | Verified arithmetic; Equity definition not supplied | Partially Supported | Medium | Manager alignment | S4 page:62-63 |
| Indicative termination fee | CP-1A | LTM management fee 21,257 | 3 x 21,257 = 63,771 | Indicative; contractual 24-month average not computed | Partially Supported | Low | Cost of changing manager | S4 page:64; S1 page:232 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 liquidity and unfunded commitments | Thousand-dollar figures cited to pages that print the rounded million: 236,552 to page:71 (printed on page:72 and page:108), 87,317 and 22,000 to page:77 (printed on page:105), 70,826 to page:28 (printed on page:6) | Imprecise locator | A reader checking the page finds a rounded figure | Cite page:72, page:105 and page:6 | CP-1 handoff |
| MINOR | CP-0 allowance tie-out | 73,955 cited to page:7; it is printed on page:6 | Imprecise locator | Slower verification | Cite page:6 | CP-0 handoff |
| MINOR | CP-2 loan seniority | "Entirely senior first mortgage loans" is not supported: 105.0 million and 11.3 million contiguous mezzanine loans and a 4.5 million subordinate loan are owned (page:115-120 of S4) | Partially Supported claim | Overstates collateral position by about 2.3% of commitments | Reword to senior loans including contiguous mezzanine pieces | CP-2 strengths |
| MINOR | CP-2 opening sentence | "Moderately leveraged" is an unsupported adjective beside leverage above the company's own expectation | Unsupported adjective | Adjective can be read as a conclusion on leverage | State the ratio instead | CP-2 credit view |
| MINOR | Covenant and legal terms | Recourse caps, security and covenant levels rest on filing summaries; executed documents not supplied | Source limitation | Legal meaning cannot be verified | Obtain the agreements | CP-0 to CP-2 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves on the cover and signature pages | A wrong document would change every figure | None found | None |
| Locator precision | Adequate | 341 of 347 locator-bearing statements resolve; 6 cite a rounded or neighbouring page | Slower checks and a risk of a misplaced citation | None on conclusions | Exact page locators for thousand-dollar figures |
| Calculation reproducibility | Strong | 106 of 106 derived figures and 38 of 38 tie-outs recomputed equal | Calculation errors would move leverage and liquidity | None found | None |
| Quotation fidelity | Strong | 18 of 18 quoted passages found word for word | Misquotation would change meaning | None found | None |
| Definition and perimeter discipline | Adequate | Issuer definitions labelled; GAAP and covenant bases kept apart; two inferences labelled | A definition drift would misstate headroom | Covenant headroom stays unverified | Obtain covenant definitions |
| Cross-module consistency | Strong | Leverage, liquidity, maturity and earnings figures agree across the four handoffs | Inconsistent figures mislead a committee | One seniority overstatement | Correct the CP-2 statement |
| Reviewer independence | Weak | The host wrote and checked every handoff | Shared blind spots go undetected | Omissions may remain | Independent review |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant test values and definitions | Compliance certificates or credit agreements | Headroom and the recourse base cannot be verified | Covenant and liquidity findings | Holds the view to filing summaries | Credit agreements and compliance certificates |
| G2 | Executed agreements and guarantor list | Term Loan B and Revolver agreements, secured credit agreements, Management Agreement | Legal terms and ranking cannot be verified | Recourse and claim-structure findings | Source gate partial | Exhibits to the 8-Ks and the 2026-05-14 credit agreement |
| G3 | Use of proceeds of the October 2026 CLO | 8-K of 2026-10-06 and offering terms | Post-quarter leverage and recourse unknown | Leverage and liquidity findings | Lowers currency of the view | The 8-K and the Q4 2026 filing |
| G4 | Events after 2026-10-26 | Later filings to the cutoff | Later events could change the view | All findings | Lowers currency | EDGAR filings to 2026-11-05 |
| G5 | Basis of the 3.75:1 expectation | Statement in the next annual report | Whether leverage is above range depends on the measure | Leverage finding | Medium confidence | Next annual report |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / trtx-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted at attempt 1 | Passed with one MINOR locator finding | All consumers READY_WITH_LIMITATIONS |
| CP-1 | requests/CP-1 attempt 2 / same run | Statements, funding, recourse, liquidity, covenants | High | Six headings; attempt 1 refused for a reader-summary figure not repeated in the body, attempt 2 accepted | Passed with one MINOR locator finding | All 106 derived figures recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, manager, transactions, governance | High | Six headings; accepted at attempt 1 | Passed with no defect of its own | Quotations 14 of 14 verbatim |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted at attempt 1 | Passed with two MINOR findings | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Liquidity paragraph and funding commentary | Supported | Thousand-dollar figures cited to pages that print the rounded million | Cite page:72, page:105, page:6 | None |
| MINOR | CP-0 | Total allowance tie-out | Supported | 73,955 cited to page:7; printed on page:6 | Cite page:6 | None |
| MINOR | CP-2 | Strength: collateral quality indicators, "entirely senior first mortgage loans" | Partially Supported | Contiguous mezzanine and subordinate pieces of 120.8 million, 2.3% of commitments, are owned | Reword to senior loans including contiguous mezzanine pieces | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Cash covenant match to five percent of recourse exposure | Holds only without the 25% guarantee on the 29,110 thousand mortgage loan; recourse indebtedness is not defined in the pack | None | Keep labelled as inference, as CP-1 and CP-2 do | None |
| MINOR | CP-1, CP-2 | Indicative debt to total assets 80.1% | Uses GAAP principal and total assets; covenant definitions not supplied | None | Keep labelled indicative, as CP-1 and CP-2 do | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Term Loan B guaranteed by certain subsidiaries and secured on a first-priority basis on substantially all assets | Executed Term Loan B credit agreement and security documents | Filing summary only; guarantors unnamed | Obtain the agreement | Required before any ranking view |
| MINOR | CP-1 | Secured credit agreements 25% recourse to Holdco, capped with carve-outs | Executed secured credit agreements and guarantees | Filing summary only | Obtain the agreements | Required for recourse analysis |
| MINOR | CP-1 | Covenant levels and the compliance statement | Executed credit agreements | Levels printed, test values and definitions not | Obtain compliance certificates | Required for headroom |
| MINOR | CP-1A | Termination fee of three times average annual fees | Executed Management Agreement | Filing summary only | Obtain the agreement | Required for manager-change analysis |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No price, spread, yield, rating, comparable or relative-value claim is made; the context ratings, quotes and peers are empty | Prices, spreads and ratings are not part of the minimum source pack | Recorded by design | Add relative-value work only with sourced market data | The run cannot support a relative-value view |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | CP-1A describes first mortgage lending without noting contiguous mezzanine pieces; CP-2 states the book is entirely senior first mortgage loans | CP-2 cites the accepted CP-1 (attempt 2, d2958939) and CP-1A (e9ba717d) hashes | Reword the CP-2 statement | Minor; no figure changes |
| MINOR | CP-0, CP-1 | CP-1 refines two CP-0 items (recourse terms and the book value per share deduction) and states so | CP-1 cites the accepted CP-0 hash | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Unsupported adjective | "Moderately leveraged" in the opening sentence of the credit view | State the ratio | None on figures |
| MINOR | Run | Committee readiness | Facts and funding structure are traceable; covenant headroom, guarantor package and the October 2026 CLO effect are not; review is self-review only | Supply agreements, compliance certificates, later filings and an independent review | Committee status Requires More Work |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Reader summary, attempt 1 | A reader-summary figure (21,993) was not repeated in the body and was refused; repaired in attempt 2 | Repeat every reader-summary figure in the body | Resolved; attempt 2 accepted |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-1 | Locator | Thousand-dollar figures cited to pages that print the rounded million (236,552; 87,317; 22,000; 70,826) | Cite page:72, page:105, page:6 | None | Open |
| QA-2 | MINOR | CP-0 | Locator | Allowance 73,955 cited to page:7; printed on page:6 | Cite page:6 | None | Open |
| QA-3 | MINOR | CP-2 | Partially Supported Claim | Loan book described as entirely senior first mortgage loans; 120.8 million (2.3% of commitments) is contiguous mezzanine or subordinate | Reword | None | Open |
| QA-4 | MINOR | CP-2 | Unsupported adjective | "Moderately leveraged" beside leverage above the company's stated expectation | State the ratio | None | Open |
| QA-5 | MINOR | CP-0 to CP-2 | Source Limitation | Recourse, security and covenant terms rest on filing summaries; two inferences labelled | Obtain executed agreements and compliance certificates | Restricts headroom conclusions | Open |
| QA-6 | MINOR | Run | Reviewer independence | One host session wrote and checked all handoffs | Independent review | Caps committee status | Open |

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 0. Minor Issues: 6. Committee Use: Restricted.

No defect changes a credit conclusion or a reported figure. Committee use is restricted because covenant headroom and the guarantor package cannot be verified and the review is a self-review; the six minor items should be disclosed with the report.

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Every double-quoted passage in the four handoffs searched, whitespace and quote marks normalised, in the seven source texts | 18 quoted passages parsed (CP-0 3, CP-1 1, CP-1A 14, CP-2 0); 18 found, one differing only in capitalisation ("maximum current availability" against the printed column heading) |
| Q2 | Metric recomputation | 106 derived figures (LTM sums, ratios, recourse exposure, cash covenant test at four dates, liquidity sums, maturity shares, dividend cover, scenario arithmetic, fee base, concentration, share counts) recomputed from the figures in the statement tables with a script and compared with the handoffs within rounding | 106 of 106 equal |
| Q3 | Tie-outs | Balance sheet liabilities, assets and liabilities plus equity at five dates (15); pre-tax income at six periods and net income to common at five periods (11); quarterly sums to nine months (5); liquidity tables at four dates (4); maturity schedule rows and columns (2); secured financing carrying value (1) | 38 of 38 equal |
| Q4 | Verbatim presence of statement numbers | 432 numeric cells in the CP-1 financial tables looked up as printed in the source texts | 418 found; 14 not found, all derived (LTM values, sums of quarters, ratios) and recomputed in Q2 |
| Q5 | Locator screen | Every statement carrying a `page:N` locator in CP-0 (108), CP-1 (122) and CP-1A (117) tested for its figures on the cited pages; flagged statements reviewed by hand | 347 screened; 35 flagged by the screen; after review 6 are imprecise (QA-1, QA-2) and 29 were derived values or figures cited to a second locator in the same sentence |
| Q6 | Confidence Score | `confidence_score.py --lineage "Directly Sourced:4,Calculated:3,Assumption-Based:2,Analyst Inference:2,Insufficient Information:1" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:6` | score = clamp((0.6 x 70.83 + 0.4 x 100) x 0.7 - 18) = 39.75, rounded to 40; band Low; qa_status Passed |

## Gaps

- G1 Material to the decision: covenant test values and definitions are not supplied, so headroom is unverified.
- G2: executed agreements and the Term Loan B guarantor list are not supplied; legal terms rest on filing summaries.
- G3: the use of proceeds and effect of the October 2026 CLO are not supplied.
- G4: events after 2026-10-26 up to the as-of date are not supplied.
- G5: the basis of the 3.75:1 leverage expectation after the Term Loan B is not stated.
- G6: no independent review; this check was written by the same host as the handoffs it checks.

## Next module

- Report delivery: carry qa_status Passed, Confidence Score 40 (Low), committee status Requires More Work, the six minor findings and gaps G1 and G2.
- Swarm review step: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: obtain the 2026-05-14 credit agreement, compliance certificates, the 8-K of 2026-10-06 and later filings, and rerun the affected modules in a new run folder; correct the CP-2 loan seniority statement and the thousand-dollar locators there.
