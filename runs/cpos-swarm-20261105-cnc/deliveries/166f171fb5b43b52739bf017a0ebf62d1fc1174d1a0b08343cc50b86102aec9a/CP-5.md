# CP-5 Evidence trace and research-integrity QA: CENTENE CORP (cnc)

## Request

- Issuer: CENTENE CORP (issuer id `cnc`), as of 2026-11-05, information cutoff 2026-11-05, pathway `credit_snapshot`, run `cnc-2026-11-05-credit_snapshot-host`.
- Scope: CP-5 checks CP-0, CP-1, CP-1A and CP-2 against the pinned sources and grades the result (absorbed CP-5A phase). Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- Execution: host session, no provider call. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. QA envelope: `qa_status` Passed; Confidence Score 45, band Low (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.

## Sources

### Issuer sources

| Short name | Exact source name | sha256 (pinned file) |
| --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_cnc-20251231.htm.jsonl | 097062d4e055a3b7fe83b7f7a6e69a627cdfc677e170580a5543c61781d7f32c |
| Q1 10-Q | 10-Q_2026-03-31_cnc-20260331.htm.jsonl | 6fdb16147461b8c90a892872b86f94619262dc29b1649522f12be59d50d43010 |
| Q2 10-Q | 10-Q_2026-06-30_cnc-20260630.htm.jsonl | 2be254120598acb867bfc89cb539dc675621975d5b2820213b11fde2ab54d522 |
| Q3 10-Q | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | cfb19f79c82250660e2e3f3fc4242fe18840a50e06dfa54c4c173df9081f0994 |
| Q1 release | EX-99.1_2026-04-28_a20260428ex991pressrelease.htm.jsonl | 85e525be3f7df9445c1acc49590c58f56053e97a34531af048cb7fd64ca5f94b |
| Q2 release | EX-99.1_2026-07-28_a20260728ex991pressrelease.htm.jsonl | ef848078ad02a5ade77bb7226070a38945f9e917a1e3e86d5abb0edd73e6d395 |
| Q3 release | EX-99.1_2026-10-27_a20261027ex991pressrelease.htm.jsonl | 916ad849ec4d38de97614bebc7921009e1fad702ea222f32804d2cf10f3a8c80 |

### Run settings

| Item | sha256 |
| --- | --- |
| context | 513a568e8f913d85d10b3279b6da71f4942d77c29169f956b5f35a2740b22b67 |

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 891bc08ab57345267c7df4471f2151a6318cc16f4e53da139e0a73bb24e6659d |
| CP-1 | d148eae49bfb36d490e6a47382af69ec58ed9ca91eec53f6c1c1514a18cb82bc |
| CP-1A | b424537d11dcd254a7af7693435323947bafa3093bd7c03ee29384233220e0f2 |
| CP-2 | e33c9f94a776b759042559b9488d785c7d20000b41f642db18c4dd8334bd2842 |

Locators are `page:N` chunk numbers of the pinned `.jsonl` extracts, as in the handoffs. Each handoff was read in the accepted form named by the hash above.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four upstream handoffs are traceable: every quotation checked is verbatim in its source and every figure recomputed from the filings matches. The defects found are minor locator and wording points that change no conclusion. | Medium | Executed agreements and the proxy are not supplied, and one host wrote and checked all modules, so the confidence score is 45, in the Low band. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 83 source quotations in the four handoffs were found verbatim in a source chunk, and cited chunk numbers resolve. | Statements attributed to the filings can be relied on as accurate quotations. | High |
| Every checked figure equals the handoff: 21 of 21 credit metrics, 50 of 50 balance sheet cells and 60 of 60 cash flow cells. | Leverage of 3.62x and cover of 6.85x are arithmetically sound, though they rest on an analyst-defined EBITDA. | High |
| Five minor defects were found: partial page locators, an ambiguous regulatory date, and a conflicts entry that is a comparability note. | None changes a figure or a conclusion; they slow verification only. | High |
| Covenant headroom, guarantors, the receivable purchase agreement and the Magellan sale terms have no source in the set. | These stay Insufficient Information and cap committee use until executed documents are supplied. | High |

### Evidence trace view

The analysis is traceable enough for a view of Centene's current financial position and business risks, and not for covenant, guarantor or contract-level conclusions. All 83 source quotations in the four handoffs were found verbatim in a source chunk, and every figure recomputed from the filings equals the handoff, including 21 of 21 credit metrics. The strongest support is that leverage of 3.62x, cover of 6.85x and parent liquidity of USD 4,175 million reproduce exactly. The weakest point is that these ratios rest on an analyst-defined EBITDA, because the issuer reports none, and that covenant definitions and agreements are not supplied. Five minor locator and wording defects need no change to any conclusion. Committee status: Requires More Work.

### Traceability summary

| Measure | Result |
| --- | --- |
| Source quotations checked against chunks | 83 of 83 found verbatim |
| Credit metrics recomputed from source rows | 21 of 21 equal |
| Balance sheet cells (50) and cash flow cells (60) compared | 110 of 110 equal |
| Statement tie-outs re-added | 55 of 55 equal |
| Material claims by lineage | 10 Directly Sourced, 6 Calculated, 3 Analyst Inference, 3 Insufficient Information |
| Open findings | 5 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cnc-20251231.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | Centene Corporation and subsidiaries, consolidated; parent-only schedule | Statements, debt note, maturities, segments, business, history | Text extract; original HTML and XBRL not supplied | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_cnc-20260331.htm.jsonl | High: filed, unaudited interim report | Three months ended March 31, 2026 | Same | Statements, debt note, liquidity, HBR | Text extract; unaudited | CP-0, CP-1, CP-1A |
| S3 | 10-Q_2026-06-30_cnc-20260630.htm.jsonl | High: filed, unaudited interim report | Three and six months ended June 30, 2026 | Same | Statements, debt note, liquidity, risk adjustment benefit | Text extract; unaudited | CP-0, CP-1, CP-1A |
| S4 | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | High: filed, unaudited interim report | Three and nine months ended September 30, 2026 | Same | Statements, debt note, covenant, liquidity, segments, regulatory and contract updates, subsequent events | Text extract; unaudited | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-28_a20260428ex991pressrelease.htm.jsonl | Medium: issuer press release | Quarter ended March 31, 2026 | Same, issuer presentation | Cash available for general corporate use, guidance | Management-prepared; repeats the 10-Q | CP-1 |
| S6 | EX-99.1_2026-07-28_a20260728ex991pressrelease.htm.jsonl | Medium: issuer press release | Quarter ended June 30, 2026 | Same | Cash available for general corporate use, guidance | Management-prepared; repeats the 10-Q | CP-1 |
| S7 | EX-99.1_2026-10-27_a20261027ex991pressrelease.htm.jsonl | Medium: issuer press release | Quarter ended September 30, 2026 | Same | Adjusted EPS, guidance, regulated and unregulated split, debt to capitalization | Management-prepared; non-GAAP; repeats the 10-Q | CP-1, CP-1A |
| S8 | context | Run settings, not issuer evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency USD | Blank ratings, market and sponsor fields are not zero | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Deleveraging: total debt of 15,542 and calculated LTM leverage of 3.62x against 6.86x for FY2025 | CP-1, CP-2 | Debt table and statements; ratio recomputed from rows | Sets debt service and refinancing capacity | Core leverage view | S4 page:20, page:8, page:9, page:11; S1 page:130, page:131 | EBITDA is analyst-defined; the issuer reports none |
| 2 | Thin parent liquidity: 175 available for general corporate use plus an undrawn 4,000 revolver | CP-1, CP-2 | Unregulated cash disclosure and revolver terms | Debt service depends on the revolver and on regulated subsidiary dividends | Liquidity tolerance | S4 page:46, page:47, page:48, page:49 | Revolver conditions and covenant definitions not supplied |
| 3 | Front-loaded earnings: calculated EBITDA of 2,568, 1,933 and 325 in Q1, Q2 and Q3 2026 | CP-1, CP-2 | Quarterly statements; HBR of 87.3%, 89.6% and 92.7% | LTM ratios flatter the run rate | Monitoring of fourth quarter results | S2 page:7, page:8; S3 page:8; S4 page:9; S2 page:32; S3 page:37; S4 page:40 | Quarter derived by subtraction where cumulative |
| 4 | Government payor dependence and dated regulatory change | CP-1A, CP-2 | Segment mix, state concentration, contract losses, OBBBA, Star Ratings | Drives revenue visibility and margin | Business risk | S1 page:13, page:15; S4 page:30 to page:38 | Protest outcomes and later events not supplied |
| 5 | Cash flow distortion from pass-through timing and the receivable sale | CP-1, CP-1A | Operating cash flow includes net sale proceeds of 970 | Free cash flow is not a recurring measure | Cash conversion view | S4 page:11, page:12, page:14, page:15 | Receivable purchase agreement not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 15,542 at September 30, 2026 | CP-1, CP-2 | S4 page:20 debt table; page:8 balance sheet | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Cash available for general corporate use 175; revolver 4,000 with no borrowings | CP-1, CP-1A, CP-2 | S4 page:46, page:47 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Debt to capital 41.1% against 0.60 maximum | CP-1, CP-2 | S4 page:47 | Yes | High; issuer-defined ratio | Directly Sourced | Supported as an issuer statement | Medium | Committee-Ready |
| Medicaid 57% of FY2025 external revenues; Florida and New York each about 10% or more of Medicaid premium revenues | CP-1A, CP-2 | S1 page:13, page:15 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Membership 25,698,200 against 27,968,100; Marketplace 3,403,300 against 5,828,100 | CP-1A, CP-2 | S4 page:38 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Net receivable sale proceeds 970 funded part of 2027 note redemption | CP-1, CP-1A, CP-2 | S4 page:15 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| October 2026 redemption of the remaining 2027 notes | CP-1, CP-1A, CP-2 | S4 page:21 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Medicare Star Ratings coverage about 42% against about 60% | CP-1A, CP-2 | S4 page:38, page:37 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Health benefits ratio 87.3%, 89.6%, 92.7% by quarter | CP-1, CP-1A, CP-2 | S2 page:32; S3 page:37; S4 page:40 | Yes | High; issuer-defined | Directly Sourced | Supported | High | Committee-Ready |
| LTM leverage 3.62x and net leverage 3.53x | CP-1, CP-2 | Calculations C1, C2, C4 in CP-1 from S1 and S4 rows | Yes | High inputs; analyst definition | Calculated | Supported, recomputed equal | Medium | Committee-Ready with definition caveat |
| EBITDA over cash interest 6.85x | CP-1, CP-2 | CP-1 C4; S1 page:132; S4 page:11 | Yes | High inputs | Calculated | Supported, recomputed equal | Medium | Committee-Ready with definition caveat |
| Quarterly EBITDA 2,568, 1,933, 325 | CP-1, CP-2 | CP-1 C7 from S2, S3, S4 rows | Yes | High inputs | Calculated | Supported, recomputed equal | High | Committee-Ready |
| Parent-level liquidity 4,175 | CP-1, CP-2 | CP-1 C9: 175 + 4,000 | Yes | High inputs | Calculated | Supported | Medium | Committee-Ready with definition caveat |
| LTM operating cash flow less capital expenditures 3,943; 2,973 excluding the sale | CP-1, CP-2 | CP-1 C3, C11 | Yes | High inputs | Calculated | Supported | Medium | Committee-Ready with timing caveat |
| Overall credit view adequate and improving | CP-2 | Synthesis of CP-1 and CP-1A | Yes, by section name | Derived | Analyst Inference | Judgement, labelled as such | Medium | Remediation Needed only if gaps close |
| Issuer behaviour creditor-supportive | CP-1A, CP-2 | S4 page:21, page:46, page:15 | Yes | High | Analyst Inference | Judgement on documented actions | Medium | Committee-Ready with caveat |
| Front-loaded earnings overstate the run rate | CP-1, CP-2 | CP-1 C7; S1 page:17 | Yes | High | Analyst Inference | Judgement | Medium | Committee-Ready with caveat |
| Covenant headroom | CP-1, CP-2 | Credit agreement definition not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Guarantors, restricted payment capacity, legal capacity | CP-1A, CP-2 | Indentures and credit agreement not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Magellan sale terms and receivable agreement repurchase triggers | CP-1A, CP-2 | Agreements not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 15,542 and long-term debt 15,454 | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:20, Note 8 Debt | CP-1 debt register | Sourced | High | Components re-added equal |
| Total stockholders' equity 22,283 | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:9, balance sheet | CP-1 metrics and balance sheet tables | Sourced | High | CP-1 cites page:8; row is on page:9 (QA-1) |
| Unregulated cash 376 of which 175 available for general corporate use | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:46, Liquidity | CP-1 liquidity; CP-1A model | Sourced | High | Matches |
| Revolver 4,000, no borrowings, covenant 0.60 to 1.00, debt to capital 41.1% | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:47, Liquidity | CP-1 covenants | Sourced | High | Matches |
| Interest paid 438 and income taxes paid 15 for nine months | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:11, cash flows | CP-1 metrics | Sourced | High | Matches |
| FY2025 revenues 194,777 and operating loss 7,623 | runs/cpos-swarm-20261105-cnc/source-text | 10-K_2025-12-31_cnc-20251231.htm.jsonl | S1 | page:130, statements of operations | CP-1 metrics | Sourced | High | Matches |
| Maturity schedule total 17,493 | runs/cpos-swarm-20261105-cnc/source-text | 10-K_2025-12-31_cnc-20251231.htm.jsonl | S1 | page:160, Note 10 | CP-1 chart data | Sourced | High | Differs from debt table lines by 3, logged in CP-1 |
| Medicaid 57% of external revenues | runs/cpos-swarm-20261105-cnc/source-text | 10-K_2025-12-31_cnc-20251231.htm.jsonl | S1 | page:13, Item 1 | CP-1A model | Sourced | High | Matches |
| Receivable sale of 1,000 with net proceeds 970 | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:15, Note 3 | CP-1 and CP-1A transaction summary | Sourced | High | Matches |
| Receivable purchase agreement with MUFG Bank, Ltd. | runs/cpos-swarm-20261105-cnc/source-text | 10-K_2025-12-31_cnc-20251231.htm.jsonl | S1 | page:177, Item 9B | CP-1A timeline | Sourced | High | Matches; repurchase obligations quoted |
| Remaining 569 of 2027 notes redeemed in October 2026 | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:21, Note 8 | CP-1 debt register; CP-1A timeline | Sourced, subsequent event | High | Labelled as after the balance sheet date |
| Magellan assets and liabilities held for sale 312 each | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:13, Note 2 | CP-1 claims; CP-1A transaction | Sourced | High | Matches |
| Net dividends of about 20 expected from insurance subsidiaries for the rest of 2026 | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:48, Liquidity | CP-1A model; CP-2 | Sourced, management expectation | High | Management Language, labelled |
| LTM EBITDA 4,292 | runs/cpos-swarm-20261105-cnc/source-text | 10-K and 10-Q rows | S1, S4 | page:130; page:9 | CP-1 C2 | Calculated | High inputs | Recomputed equal; analyst definition |
| Securities Action filed July 9, 2025 | runs/cpos-swarm-20261105-cnc/source-text | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | S4 | page:27, Note 11 | CP-1A timeline | Sourced | High | Matches |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM to September 30, 2026 | CP-1 C1; CP-2 findings | FY2025, nine months 2026 and nine months 2025 rows | FY2025 + nine months 2026 - nine months 2025 | Recomputed from parsed rows: equal for revenue, operating earnings, investment income, depreciation, amortization, impairment, interest, net earnings, interest paid, operating cash flow and capital expenditures | Supported | High | Basis of every LTM ratio | S1 page:130 to page:132; S4 page:9, page:11 |
| EBITDA, analyst-defined | CP-1 C2; CP-1A; CP-2 | Operating earnings + investment and other income + depreciation + amortization of acquired intangibles + impairment | Sum; debt extinguishment excluded | Recomputed: FY2024 6,213; FY2025 2,535; nine months 4,826; LTM 4,292; LTM Q1 2,872; LTM Q2 4,523 | Supported with definition caveat | Medium | Leverage and cover | S1 page:130; S2 page:7, page:8; S3 page:8; S4 page:9 |
| Leverage | CP-1 C4 | Carrying total debt over EBITDA, and net of unregulated cash | Total debt / EBITDA | Recomputed: 2.98x, 6.86x and 3.62x; net 2.94x, 6.65x, 3.53x | Supported | Medium | Debt capacity | S1 page:158; S4 page:20, page:46 |
| Cash interest cover | CP-1 C4 | EBITDA over interest paid | EBITDA / interest paid | Recomputed: 9.03x, 3.92x, 6.85x | Supported | Medium | Debt service | S1 page:132; S4 page:11 |
| Parent-level liquidity | CP-1 C9 | Cash available for general corporate use and undrawn revolver | 175 + 4,000 | Recomputed: 4,175 | Supported, analyst construct | Medium | Liquidity | S4 page:46, page:47 |
| Debt to capital | CP-1 C5 | Debt 15,542, equity 22,283 | Debt / (debt + equity) | Recomputed: 41.1%, equal to the issuer's ratio | Supported | High | Covenant context | S4 page:8, page:9, page:20, page:47 |
| Operating cash flow excluding sale proceeds | CP-1 C11 | LTM 4,724 and 970 | 4,724 - 970; 3,754 - 781 | Recomputed: 3,754 and 2,973 | Supported | Medium | Cash conversion | S4 page:11, page:15 |
| Gross versus carrying debt | CP-1 debt register | Senior notes 13,646, Term Loan 1,963, issuance costs (67) | Gross principal less issuance costs equals carrying 15,542 | Recomputed equal; the gross-to-carrying difference of 67 is visible but not named as a delta in CP-1 (QA-3) | Supported | High | Leverage basis | S4 page:20 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial gate, 5 MINOR | Script formula | 45, band Low | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 statement and balance sheet figures | Locators are partial: the Q1 10-Q statement of operations is cited as page:7 but premium tax expense, operating earnings and net earnings sit on page:8; Q2 10-Q equity is on page:8, cited as page:7; Q3 10-Q equity and part of total liabilities are on page:9, cited as page:8 | Imprecise locator | A reader checking the cited chunk will not find the row | Cite both chunks in a later run | CP-1 tables for operations, balance sheet and metrics |
| MINOR | CP-1A regulatory calendar row | "beginning in 2028" belongs to provider-tax and state-directed-payment changes, but the row lists work requirements first; the filing dates the work-requirement morbidity effect as largely from 2027 (S4 page:30). CP-2 repeats the generic "2027 and 2028" | Ambiguous wording | A reader may read 2028 as the work-requirement date | Separate the dates in a later run | CP-1A Company and operating model; CP-2 Key findings |
| MINOR | CP-1 leverage basis | Ratios use carrying debt; the gross-to-carrying difference is shown as an issuance cost line but not named | Unstated delta | Canon asks for the gross delta to be logged | Name the difference of 67 in a later run | CP-1 Debt register |
| MINOR | CP-1A Conflicts logged | The Medicare and Medicaid membership entry is a comparability note, not two sources in conflict; the benefit entry (481 and 480) is a true mismatch of two cumulative figures | Classification | Conflicts register mixes two kinds of item | Label the first as a comparability note | CP-1A Conflicts logged |
| MINOR | CP-0 source register | One abbreviated quotation ("Visible text of ...") is an ellipsis, not a literal span | Abbreviated quote | A parser cannot match it | Quote the full opening or paraphrase | CP-0 Provenance note |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text; hashes in all handoffs match the accepted files | A wrong document would change every figure | None found | None |
| Quotation accuracy | Strong | 83 of 83 source quotations found verbatim in a source chunk | A misquotation would misstate a fact | None found | None |
| Locator precision | Adequate | Cited chunks resolve; some rows sit on the neighbouring chunk (QA-1) | Slower checks | None on conclusions | Exact page locators |
| Calculation reproducibility | Strong | 21 of 21 metrics recomputed from parsed source rows; 110 of 110 table cells equal; 55 of 55 tie-outs | A calculation error would move leverage | None found | None |
| Definition discipline | Adequate | EBITDA defined and labelled analyst-calculated; a second basis shown | Definition drift would mislead a committee | Leverage depends on including investment income | State the choice in any committee use |
| Cross-module consistency | Strong | Every CP-2 figure appears in CP-1 or CP-1A; CP-1A new figures trace to quoted chunks | Inconsistent figures mislead | None found | None |
| Reviewer independence | Weak | The host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant definitions, indentures and guarantors | Executed credit agreement and indentures | Headroom and structural ranking cannot be confirmed | CP-1 covenant table; CP-2 risk row | Covenant view rests on an issuer statement | Credit Agreement of March 5, 2025 and the indentures |
| G2 | Receivable purchase agreement terms | Exhibits 2.1 and 2.2 to the 10-K | Repurchase triggers are a contingent claim on liquidity | CP-1 claims table; CP-2 minor risk | Liquidity view slightly lower | The agreement and performance guaranty |
| G3 | Magellan sale terms | Sale agreement or 8-K | Proceeds and timing unknown | CP-1A transaction summary | Perimeter view bounded | Sale agreement |
| G4 | Proxy statement | Board, beneficial owners, control rights | Governance assessed on documented actions only | CP-1A ownership and governance | Governance view bounded | Proxy statement |
| G5 | Events after October 27, 2026 | Later 8-Ks and filings | Fourth quarter and later events may change the view | All modules | Lowers currency of the view | EDGAR filings to the cutoff |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |
| G7 | Issuer-defined EBITDA | Issuer or agency definition | Analyst definition may differ from lender definitions | CP-1 leverage and cover | Ratios carry a definition caveat | Issuer, agency or lender definitions |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / cnc-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted attempt 1 | Passed with one MINOR finding | All consumers READY_WITH_LIMITATIONS |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, covenants | High | Six headings and chart selectors; accepted attempt 1 | Passed with two MINOR findings | All metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, regulation, timeline, governance, transactions | High | Six headings and selectors; accepted attempt 1 | Passed with two MINOR findings | Every new figure traces to a quoted chunk |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings and selectors; accepted attempt 1 | Passed with one MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Operations, balance sheet and metrics tables | Supported | Partial page locators (QA-1) | Cite both chunks | None |
| MINOR | CP-1A | Regulatory calendar row | Supported | Ambiguous date wording (QA-2) | Separate dates | None |
| MINOR | CP-0 | Provenance note | Supported | Abbreviated quotation (QA-5) | Quote in full | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Leverage on carrying debt | Gross-to-carrying difference of 67 not named (QA-3) | None | Name the delta | None |
| MINOR | CP-1 | EBITDA definition | Includes investment and other income and adds back impairment; secondary basis excluding investment income gives 5.66x against 3.62x | Issuer reports no EBITDA | Keep both bases labelled, as CP-1 does | None |
| MINOR | CP-1 | Maturity schedule | Printed total 17,493 against 15,490 + 2,000 = 17,490 | Unreconciled difference of 3, logged by CP-0 and CP-1 | Confirm with issuer | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-2 | Covenant headroom against 0.60 to 1.00 | Executed Credit Agreement | Definition not supplied; claims correctly labelled Insufficient Information | Supply the agreement; add CP-4 | Required before any covenant view |
| MATERIAL as a gap, not a defect | CP-1A, CP-2 | Guarantors, restricted payments, legal capacity | Indentures and Credit Agreement | Not supplied; stated as not assessed | Supply documents | Required for creditor-control view |
| MINOR | CP-1A | Receivable sale repurchase obligations | Receivable Purchase Agreement | Terms known only from a filing sentence | Supply Exhibit 2.1 | Required for contingent liquidity |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; CP-2 gives no peer ranking, instrument recommendation or recovery conclusion | Prices, spreads and ratings are outside the minimum pack | Recorded by design | Add relative-value modules only with sourced market data | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A | Benefit of 481 (six months) and 480 (nine months) from two 10-Qs logged as a conflict; the membership entry is a comparability note | CP-1A accepted attempt 1; CP-2 cites its hash b424537d | Label entry types (QA-4) | None |
| MINOR | CP-1, CP-1A, CP-2 | All shared figures agree: debt 15,542, leverage 3.62x, cover 6.85x, available cash 175, revolver 4,000, debt to capital 41.1%, sale proceeds 970 | Each handoff cites the current upstream hashes | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Financial base and business risks are traceable; covenant, guarantor and contract-level views are not; review is a self-review | Supply executed documents and an independent review | Committee status Requires More Work |
| MINOR | CP-1, releases | Duplication | The releases repeat the 10-Q statements; CP-0 and CP-1 treat the 10-Qs as controlling and do not count releases as corroboration | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Report selectors | No export defect: chart tables, Financials and credit metrics, Company and operating model, Company profile and Transaction summary selectors were accepted by the launcher checks | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-1 | Locator | Partial page locators for statement of operations (Q1), equity (Q2, Q3) | Cite both chunks | None | Open |
| QA-2 | MINOR | CP-1A, CP-2 | Wording | Regulatory dates not separated | Separate work-requirement and provider-tax dates | None | Open |
| QA-3 | MINOR | CP-1 | Definition | Gross-to-carrying debt delta not named | Name the delta | None | Open |
| QA-4 | MINOR | CP-1A | Classification | Comparability note logged as a conflict | Label entry types | None | Open |
| QA-5 | MINOR | CP-0 | Quote | Abbreviated quotation | Quote in full | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted source span in the four handoffs searched for verbatim (whitespace-normalised) in the pinned chunks; spans with an adjacent locator were also searched in the cited chunk | 83 source quotations (CP-0 41, CP-1 16, CP-1A 26, CP-2 0); all found; the other quoted strings are section names, a context field and one ellipsis |
| Q2 | Metric recomputation | Rows parsed from the pinned chunks by label (10-K statements; Q3 10-Q statements and cash flows); LTM, EBITDA, ratios recomputed independently of the handoffs | 21 of 21 equal: eight LTM statement lines, four EBITDA values, four LTM cash lines, five ratios; LTM Q1 and Q2 EBITDA 2,872 and 4,523 and interest paid 664 and 629 also equal |
| Q3 | Table comparison | CP-1 balance sheet table (10 lines by 5 dates) and cash flow table (10 lines by 6 periods) compared with parsed source rows; 13 cash flow cells that the parser mismatched on repeated labels were read by eye | 110 of 110 equal (50 of 50 balance sheet cells and 60 of 60 cash flow cells) |
| Q4 | Tie-outs | Statements of operations (13 period columns by three identities) and balance sheets (8 columns by two identities) re-added from parsed rows | 39 of 39 and 16 of 16 equal (55 of 55) |
| Q5 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:10,Calculated:6,Analyst Inference:3,Insufficient Information:3" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:5` | score = clamp((0.6 * 75.45 + 0.4 * 100) * 0.7 - 15) = 44.69, rounded to 45; band Low; qa_status Passed |

## Gaps

- G1 covenant definitions, indentures and guarantors are not supplied; covenant headroom and legal capacity remain Not calculable.
- G2 and G3 the receivable purchase agreement and the Magellan sale terms are not supplied.
- G4 the proxy statement is not supplied, so governance rests on documented actions.
- G5 events after October 27, 2026 are not supplied.
- G6 no independent review: this CP-5 was written by the same host that wrote the checked handoffs.
- G7 the issuer reports no EBITDA, so every leverage and cover ratio carries a definition caveat.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 45 (Low), committee status Requires More Work, and gaps G1 and G6.
- Swarm review: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: fetch the Credit Agreement and indentures, the receivable purchase agreement, the Magellan sale agreement, the proxy statement and later 8-Ks, then rerun CP-1A, CP-2 and CP-5 in a new run folder.
