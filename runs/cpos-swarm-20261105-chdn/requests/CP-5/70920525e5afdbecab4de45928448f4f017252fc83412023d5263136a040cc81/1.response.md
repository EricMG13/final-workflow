## Request

Churchill Downs Incorporated (context name Churchill Downs Inc, ticker CHDN), as of 2026-11-05, pathway credit_snapshot, evidence cutoff 2026-11-05, USD. This module traces the claims in the source-readiness, financial-base, business-context and credit-synthesis handoffs back to the seven pinned sources, re-opens their locators, recomputes their derived numbers and grades whether the work can be relied on. Scope is the Top 5 material credit drivers; it changes no upstream conclusion.

## Sources

### Issuer sources relied on

Each source was searched and its cited pages were opened in this module.

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_chdn-20251231.htm.jsonl | 791973148b4d2826daf79f6e0ecd898b524ba905f6928d4b1fa58e745cfa58e6 |
| 10-Q_2026-03-31_chdn-20260331.htm.jsonl | 3d979cd66a5fd3c2d7447c580ef853c0c5a7867f89e2461cd6b817f9d370c641 |
| 10-Q_2026-06-30_chdn-20260630.htm.jsonl | 4eca3b557126cb1eb2e1c2c8c7ed3827f930ac9e114b1865fffc6dfad00959f1 |
| 10-Q_2026-09-30_chdn-20260930.htm.jsonl | 7fff97ce9977f2b2156048dbf8e8996f9058aaa73d34344c7b548ba853ea7229 |
| EX-99.1_2026-04-22_ex991pressrelease04-22x26.htm.jsonl | bbdcb62a4845e34e0fdd4338c48e18f02c4eceb2b21c6ecefed1bd7b13c21521 |
| EX-99.1_2026-07-29_ex991pressrelease07-29x26.htm.jsonl | 85b22b14ac2149df8072938d3dbc3e8d85579a1e2355ea8fce27bcd305c203d4 |
| EX-99.1_2026-10-28_ex991pressrelease10-28x26.htm.jsonl | ecea350f3f38425e2e2322d4e7d883986fb7f745d76fde798f61a64ba8bc0e4f |

The context file (sha256 7c4f52e55b5e23c0fba0c45fbf91c794297fbfceecf1db4e9e336166f978aca8) holds run settings only and is not issuer evidence.

### Supplied handoffs

| Module | sha256 | Run and attempt consumed |
| --- | --- | --- |
| CP-0 | 6a999e93b94cb197d54e29dcbbccb60dd67263d86ef14e45c08771399f8a861b | Run chdn-2026-11-05-credit_snapshot-host, attempt 1, period q3-2026 |
| CP-1 | 1ca790f594af2528c57d0f57a2e49328f2a2f28e48929edda12648fa238cae8e | Same run, attempt 2 (attempt 1 was refused for missing chart-data sections), period q3-2026 and fy-2025 |
| CP-1A | 58b7c4e716411a13ae913fdf5d9ce73307dea4c286e662bf4a8f02c7d00306b4 | Same run, attempt 2 (attempt 1 exceeded a word limit in the summary table) |
| CP-2 | 149d19fa0279e91faeca0674fed982bf0a86cf6bf310301bfb0ef9dcb095c8c0 | Same run, attempt 1 |

Re-anchor: every upstream handoff names Churchill Downs Incorporated, as of 2026-11-05, on the consolidated perimeter in USD millions, and the figures restated in this module (LTM Adjusted EBITDA 1,245.3, total debt 4,748, unrestricted cash 167, net leverage 3.68x) agree across CP-1, CP-1A and CP-2.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis traces well to the filings and its calculations reproduce, with one rounding slip and one wrong page reference. The portfolio review and covenant comfort rest on thin support, so committee use should be restricted. | Medium | Covenant figures after December 2025, executed debt documents and details of the property sale are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt, earnings, cash flow and liquidity figures were reopened in the filings and recomputed, and all matched except a 0.1 rounding difference. | The leverage and coverage base can be relied on. | High |
| The proposed sale of nine gaming properties is stated in one sentence in the latest quarterly report, and no other source gives its terms. | The earnings weight of 22.5% to 24.1% and break-even proceeds are illustrative, not sourced terms. | Medium |
| Wide covenant cushions are inferred from December 2025 ratios and the company's own definitions are not supplied. | Compliance after 2025 is not shown, so covenant comfort is an inference. | Medium |
| Post-redemption liquidity of USD 678 million is an illustration that assumes redemption at principal and no other cash movement. | The true buffer after the October 19, 2026 redemption may differ. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 3 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is that the sale of nine wholly owned gaming properties rests on a single sentence naming no properties, price, buyer or timing, which matters because its USD 280 to 300 million earnings weight and break-even proceeds drive the leverage outlook, and it implies committee use only with that item flagged. Locators and recomputations otherwise hold; covenant comfort after December 2025 is inferred, not shown.

### Traceability summary

| Check | Result | Items |
| --- | --- | --- |
| Quotations compared to sources | 53 quoted source passages; 52 match and 1 differs in punctuation | Registers T5.2 and T5B.4 |
| Page locators opened | 37 checks; 1 wrong page | Register T5.2 |
| Derived numbers recomputed | All reproduce; 1 rounding difference of 0.1 | Registers T5.3 and T5B.5 |
| Top 5 drivers | 1 directly sourced, 3 calculated, 1 analyst inference | Register T5B.3 |
| Critical issues | None | Register T5.9 |
| Committee use | Restricted until the flagged items are cleared | Register T5.9 |

### Analytical appendix — complete canonical registers

Module Status: Ready with Limitations. Traceability Scope: Top 5. Source file path for every row below is the run folder's source-text folder.

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-01 | 10-K_2025-12-31_chdn-20251231.htm.jsonl | High: audited annual report | FY2025 | Churchill Downs Incorporated, consolidated | Statements, debt and covenant note, Adjusted EBITDA reconciliation, exhibit index | One-decimal units; defined covenant ratios only at December 31, 2025 | LTM base, covenant anchor |
| SRC-02 | 10-Q_2026-03-31_chdn-20260331.htm.jsonl | High: filed unaudited | Q1 2026 | Same | Statements, debt table, Preakness agreement | Whole millions | Quarterly leverage series |
| SRC-03 | 10-Q_2026-06-30_chdn-20260630.htm.jsonl | High: filed unaudited | Q2 and six months 2026 | Same | Statements, debt table, cash-paid lines | Portfolio review not stated | Quarterly leverage series |
| SRC-04 | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | High: filed unaudited | Q3 and nine months 2026 | Same | Statements, notes, MD&A, portfolio review sentence, subsequent events | Balance sheet pre-dates the October 19, 2026 redemption | Primary anchor for all drivers |
| SRC-05 | EX-99.1_2026-04-22_ex991pressrelease04-22x26.htm.jsonl | Medium: management release | Q1 2026 | Same | Quarterly Adjusted EBITDA, net bank leverage, growth announcements | Management attribution | Quarterly Adjusted EBITDA |
| SRC-06 | EX-99.1_2026-07-29_ex991pressrelease07-29x26.htm.jsonl | Medium: management release | Q2 2026 | Same | Quarterly Adjusted EBITDA, net bank leverage | No portfolio-review text in the extract | Quarterly Adjusted EBITDA |
| SRC-07 | EX-99.1_2026-10-28_ex991pressrelease10-28x26.htm.jsonl | Medium: management release | Q3 2026 | Same | Adjusted EBITDA, capital events, net bank leverage | Management attribution | Capital events |
| HO-0 | CP-0 handoff, response 1 | Medium: analyst work product | Q3 2026 | Same | Source readiness | Did not flag the portfolio review | Scope and gaps |
| HO-1 | CP-1 handoff, response 2 | Medium: analyst work product | FY2025 to Q3 2026 | Same | Financial base and calculations | Mixed units; omitted the portfolio review | Base figures |
| HO-1A | CP-1A handoff, response 2 | Medium: analyst work product | 2025 to Q3 2026 | Same | Business, governance, transactions | One arithmetic total off by 0.1 | Business drivers |
| HO-2 | CP-2 handoff, response 1 | Medium: analyst work product | Q3 2026 | Same | Credit synthesis | Covenant comfort inferred | Credit view |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Deleveraging: net debt to LTM Adjusted EBITDA 3.68x, down from 4.11x | CP-1 | Total debt 4,748 against 5,155; unrestricted cash 167; Adjusted EBITDA 1,245.3 | Sets default and refinancing risk; repayment funded by operating cash flow and lower buybacks | Supports credit; leverage tolerance | SRC-04 pages 2, 3, 13, 41; SRC-01 pages 65, 78 | Company definition of Adjusted EBITDA; mixed units |
| 2 | Portfolio review: sale of nine wholly owned gaming properties with USD 280 to 300 million annual Adjusted EBITDA | CP-1A, CP-2 | One sentence in the Q3 10-Q | Removes 22.5% to 24.1% of LTM Adjusted EBITDA; proceeds determine whether leverage falls | Largest swing factor in the outlook | SRC-04 page 32 | No properties, price, buyer, timing or use of proceeds |
| 3 | Refinancing structure: 2027 notes redeemed on the revolver, springing maturity tied to the 2028 notes | CP-1, CP-2 | Eighth amendment text summary and redemption notice | Cuts revolver availability and ties bank maturity to note refinancing around October 16, 2027 | Liquidity and refinancing monitoring | SRC-04 pages 14, 16, 28 | Executed amendment not supplied; dates computed from summary wording |
| 4 | Capital allocation: debt-funded outlays in FY2025, lower buybacks in 2026, new 750 million authorization | CP-1A, CP-2 | Cash flow statements and subsequent events | Buybacks can offset deleveraging | Governance and leverage tolerance | SRC-01 pages 78-79; SRC-04 pages 4, 28 | Restricted payment capacity not supplied |
| 5 | Earnings concentration and quality: Virginia, historical racing machines, Derby quarter and affiliate EBITDA | CP-1A, CP-2 | Revenue disaggregation and Adjusted EBITDA reconciliation | Single-state or single-quarter shocks hit cash flow; affiliate EBITDA is not all cash | Weight to place on leverage ratios | SRC-04 pages 18, 19, 26, 40, 41; SRC-05 and SRC-06 page 1 | Competition effects attributed by management |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net leverage 3.68x, gross 3.81x | CP-1 | Total debt 4,748; cash 167; LTM Adjusted EBITDA 1,245.3 | Yes | High | Calculated | Reproduced | High | Committee-Ready |
| Sale of nine gaming properties, USD 280 to 300 million annual Adjusted EBITDA | CP-1A | "exploring a sale of nine wholly owned regional gaming properties" | Yes | High (filed) with single-sentence support | Directly Sourced | Supported, terms absent | Medium | Remediation Needed |
| Springing maturity and October 16, 2027 test date | CP-1 | Springing maturity wording with a 91-day refinancing test | Yes | High for terms; date is computed | Calculated | Reproduced from summary | Medium | Remediation Needed |
| Debt-funded FY2025 outlays and mixed governance | CP-1A | Cash flow lines; net borrowings 216.4 | Yes | High | Analyst Inference | Supported by sums | Medium | Committee-Ready |
| Earnings concentration and affiliate EBITDA not all cash | CP-1A, CP-2 | Historical racing 780; Virginia 410; equity income 143 against distributions 106 | Yes | High | Calculated | Reproduced | Medium | Committee-Ready |
| Post-redemption liquidity 678 and availability 511 | CP-1, CP-2 | Revolver 79, letters of credit 10, 600 notes | Yes | High inputs, assumed funding | Assumption-Based | Illustrative | Medium | Remediation Needed |
| Covenant cushions wide | CP-1, CP-2 | December 2025 ratios 3.9x and 1.4x | Yes | High for 2025, none for 2026 | Analyst Inference | Not shown for 2026 | Low | Remediation Needed |
| Management net bank leverage 3.8x | CP-1, CP-1A | Q3 release statement | Yes | Medium | Conflicting definition against computed 3.68x | Undefined | Low | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 4,748 at September 30, 2026 and 5,155 at December 31, 2025 | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:13 | CP-1 debt register | Sourced | High | Opened and matched |
| Cash and cash equivalents 167 | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:2 | CP-1 balance sheet table | Sourced | High | CP-1 cites page 3; figure is on page 2 |
| Adjusted EBITDA 264, 998 and 958 for Q3 and nine months | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:41 | CP-1 Adjusted EBITDA | Sourced | High | Opened and matched |
| FY2025 Adjusted EBITDA 1,205.3 | source-text | 10-K_2025-12-31_chdn-20251231.htm.jsonl | SRC-01 | page:65 | CP-1 Adjusted EBITDA | Sourced | High | Opened and matched |
| Operating cash flow 660 and 674 for nine months | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:4 | CP-1 cash flow | Sourced | High | Opened and matched |
| Cash paid for interest 173 and 193 | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:4 | CP-1 coverage | Sourced | High | Opened and matched |
| Revolver availability $1.1 billion after 10 of letters of credit | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:14 | CP-1 liquidity | Sourced | High | Rounded to 0.1 billion in the filing |
| Springing maturity and 91-day wording | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:14 | CP-1 debt register | Sourced | High | Quote punctuation differs in CP-1 |
| 2027 notes redeemed on October 19, 2026 with revolver borrowings | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:28 | CP-1 subsequent events | Sourced | High | Subsequent event |
| Exploring a sale of nine wholly owned regional gaming properties, 280 to 300 million annual Adjusted EBITDA | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:32 | CP-1A transaction | Sourced | High | Single sentence |
| Covenant ratios 3.9x and 1.4x against 2.5x and 4.0x at December 31, 2025 | source-text | 10-K_2025-12-31_chdn-20251231.htm.jsonl | SRC-01 | page:69 | CP-1 leverage | Sourced | High | Anchor date only |
| FY2025 repurchases 427.8 | source-text | 10-K_2025-12-31_chdn-20251231.htm.jsonl | SRC-01 | page:79 | CP-1A governance | Sourced | High | Opened and matched |
| 750 million repurchase authorization approved October 27, 2026 | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:28 | CP-1A governance | Sourced | High | Subsequent event |
| Historical racing revenue 780 and Virginia 410 for nine months | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | pages 18-19 | CP-1A operating model | Sourced | High | Opened and matched |
| Virginia 5 million new tax expense from July 1, 2026 | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:40 | CP-1A operating model | Sourced | High | Management attributes competition |
| Gaming equity income 143 and affiliate adjustment 28 | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | pages 26, 41 | CP-1A, CP-2 earnings quality | Sourced | High | 143 = 115 + 28 |
| Distributions from affiliates 106 | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:4 | CP-1A, CP-2 | Sourced | High | Opened and matched |
| Q1 and Q2 Adjusted EBITDA 257 and 477 | source-text | EX-99.1 releases of April 22 and July 29, 2026 | SRC-05, SRC-06 | page:1 | CP-1 chart data | Sourced | Medium | Management release |
| Net bank leverage 3.8x at Q3 2026 | source-text | EX-99.1_2026-10-28_ex991pressrelease10-28x26.htm.jsonl | SRC-07 | page:1 | CP-1A | Sourced | Medium | Undefined metric |
| Note indentures name "the Guarantors (stated therein)" | source-text | 10-K_2025-12-31_chdn-20251231.htm.jsonl | SRC-01 | pages 136-138 | CP-1 debt register | Sourced | High | Guarantors not named |
| Preakness purchase price 85 million | source-text | 10-Q_2026-03-31_chdn-20260331.htm.jsonl | SRC-02 | page:20 | CP-1 subsequent events | Sourced | High | Closing status not stated |
| Project capital 160 to 180 million for 2026 | source-text | 10-Q_2026-09-30_chdn-20260930.htm.jsonl | SRC-04 | page:43 | CP-1 liquidity | Sourced | High | Management estimate |
| Leverage-neutral proceeds 1,030 to 1,104 | derived | Not a source figure | HO-1A, HO-2 | Calculations | CP-1A, CP-2 | Calculated | Medium | Illustrative threshold |
| Covenant cushion 35.9% and 42.4% | derived | Not a source figure | HO-2 | Calculations | CP-2 | Calculated | Low | Definitions not supplied |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA 1,245.3 | CP-1 base; all later modules | FY2025 1,205.3; nine months 2026 998; nine months 2025 958 | 1,205.3 + 998 - 958; FY2025 to one decimal, others whole | Calculated | Reproduced | High | PD, liquidity | SRC-01 p65; SRC-04 p41 |
| Net leverage 3.68x, gross 3.81x | CP-1, CP-2 | Debt 4,748; cash 167 | 4,581 / 1,245.3; 4,748 / 1,245.3 | Calculated | Reproduced | High | PD, refinancing | SRC-04 p3, p13 |
| Coverage 4.54x | CP-1, CP-2 | LTM cash interest 274.5 | 1,245.3 / 274.5 where 274.5 = 294.5 + 173 - 193 | Calculated | Reproduced | High | PD | SRC-01 p79; SRC-04 p4 |
| Free cash flow 529.9 | CP-1, CP-2 | CFO 755.8; capex 225.9 | 755.8 - 225.9 | Calculated | Reproduced | High | Liquidity | SRC-01 p78-79; SRC-04 p4, p27 |
| Liquidity 1,278 | CP-1, CP-2 | Commitment 1,200; drawn 79; letters of credit 10; cash 167 | 1,200 - 79 - 10 + 167 | Calculated | Reproduced | High | Liquidity | SRC-04 p3, p14 |
| Post-redemption liquidity 678 | CP-1, CP-2 | Assumes 600 redeemed at principal using the revolver, no other change | 511 + 167 | Assumption-Based | Illustrative | Medium | Liquidity | SRC-04 p28 |
| Springing test dates | CP-1, CP-2 | Maturity dates less 91 days | 15 January 2028 less 91 days = October 16, 2027 | Calculated | Reproduced from summary wording | Medium | Refinancing | SRC-04 p14, p16 |
| Leverage-neutral proceeds 1,030 to 1,104 | CP-1A, CP-2 | Net leverage 3.679x; 280 and 300 | 3.679 x 280; 3.679 x 300 | Assumption-Based | Illustrative | Medium | Recovery mechanic, leverage | SRC-04 p32 |
| FY2025 sources and uses gap 166.0 | CP-1A, CP-2 | FCF 494.9; outlays 660.9 | 494.9 - 660.9 | Calculated | CP-1A states a total of 661.0; the components sum to 660.9 | Medium | Governance | SRC-01 p79 |
| Equity-affiliate bridge 143 = 115 + 28 | CP-2 | Equity income 115; adjustment 28; distributions 106 | 115 + 28; 115 - 106 = 9 | Calculated | Reproduced | High | Earnings quality | SRC-04 p2, p4, p41 |
| Covenant cushions 35.9% and 42.4% | CP-2 | 3.9x vs 2.5x; 4.34x vs 2.5x | (3.9 - 2.5) / 3.9; 1 - 2.5 / 4.34 | Calculated | Reproduced; definitions differ | Low | PD, covenant | SRC-01 p69 |
| Management net bank leverage 3.8x | CP-1A, CP-2 | Release statement only | No formula supplied | Not Calculable | Management Language | Low | Monitoring | SRC-07 p1 |

#### T5B.6 Weak-lineage and missing-citation flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Sale of nine gaming properties and its 22.5% to 24.1% earnings weight | Single-sentence support; properties unnamed; the Q2 release extract has no announcement text, only risk wording about exploring strategic alternatives; the 280 to 300 figure is annual and includes sportsbook booked in another segment, while the 1,245.3 base is LTM | Directly Sourced for the event, Assumption-Based for the weight | The weight and break-even proceeds drive the leverage outlook and any mandatory prepayment or collateral release | Obtain the July 29, 2026 announcement and credit agreement sale terms | Credit view and key risks |
| Material | Covenant cushions are wide and covenant pressure is not evident | Based on December 31, 2025 ratios and computed ratios on non-covenant definitions; CP-1 itself shows computed secured leverage 1.54x against the reported 1.4x | Analyst Inference | Compliance after 2025 is not evidenced | Obtain September 30, 2026 compliance certificate | Strengths text in credit synthesis |
| Material | Post-redemption liquidity 678 and availability 511 | Assumes redemption at principal and no other cash or revolver movement; redemption price and cash at October 19, 2026 not supplied | Assumption-Based | Liquidity buffer may differ | Obtain next filing or 8-K | Credit view and risk table |
| Material | Net bank leverage 3.8x against computed 3.68x | Management metric undefined, so the two cannot be reconciled | Conflicting | Misreads of leverage direction | Treat management figure as attributed only | Leverage discussion |
| Minor | FY2025 outlays total 661.0 | Components 30.8, 427.8, 17.0 and 185.3 sum to 660.9 | Calculated | Rounding difference of 0.1; the gap of 166.0 is unaffected | Use 660.9 | Governance row in business context |
| Minor | Springing maturity quotation | CP-1 quotes "subject to an earlier springing maturity" without the quotation marks that the filing prints around springing maturity | Directly Sourced | Substance is the same; exact-quote discipline | Quote as printed | Debt register note |
| Minor | Balance sheet page reference | CP-1 cites page 3 for cash and restricted cash at September 30, 2026; they are on page 2 | Directly Sourced | Locator accuracy | Correct locator | CP-1 balance sheet table |
| Minor | Non-cash line "Debt exchanged in connection with refinancing" of 198 | Printed on page 5 of the Q3 10-Q; not explained or traced in CP-1 or CP-2 | Insufficient Information | Could change reading of gross borrowings and repayments in the refinancing | Read the refinancing note or next filing | Refinancing discussion |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven pinned filings and releases cover FY2025 to Q3 2026; executed credit agreement, indentures and proxy are absent | Legal terms rest on summaries, so structure and covenant claims are second-hand | Covenant and guarantor conclusions cannot be verified | Add executed documents |
| Citation completeness | Ready with Remediation | 37 locator checks and 53 quoted source passages tested; one wrong page and one punctuation difference | Locator errors slow review but do not change values | Low | Correct two citations |
| Calculation traceability | Committee-Ready | All derived numbers reproduce; one 0.1 slip | Formula and inputs are shown for each | Leverage and coverage base reliable | Correct the 660.9 total |
| Assumption transparency | Ready with Remediation | Post-redemption liquidity, leverage-neutral proceeds and covenant cushions are labelled illustrative but are repeated as findings | Readers may treat illustrations as facts | Overstates comfort | Keep labels in committee material |
| Markdown/export artifact integrity | Committee-Ready | Each handoff has the required headings, hashes and summary tables; one word-limit and one missing-section refusal were repaired | Structure is sound | None | None |

Overall auditability is the lowest of the five dimensions: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Portfolio review terms | Properties, price, buyer, timing, use of proceeds, announcement text | Decides whether leverage falls or rises | Credit view, risks | High impact | July 29, 2026 announcement; credit agreement |
| CP-5-GAP-002 | Covenant compliance after December 31, 2025 | Compliance certificate and covenant EBITDA definition | Compliance trend and headroom | Strengths text, risks | High impact | Compliance certificate |
| CP-5-GAP-003 | Executed credit agreement, eighth amendment and indentures | Executed documents | Springing maturity wording, restricted payments, collateral and guarantors | Refinancing risk, governance | Medium impact | 8-K exhibit 10.1 and indentures |
| CP-5-GAP-004 | Ownership and control rights | Proxy statement | Governance cannot be tested beyond actions | Governance | Medium impact | Proxy statement |
| CP-5-GAP-005 | Redemption price and cash at October 19, 2026 | 8-K or next filing | Post-redemption liquidity is illustrative | Liquidity | Medium impact | Next filing |
| CP-5-GAP-006 | Net bank leverage definition | Management reconciliation | Computed and management leverage cannot be reconciled | Leverage | Low impact | Earnings call or credit agreement |
| CP-5-GAP-007 | Preakness closing and funding | Later filing | Affects project cash needs | Growth capital | Low impact | Next filing |
| CP-5-GAP-008 | Non-cash refinancing exchange of 198 | Refinancing note detail | Reading of gross borrowing and repayment | Refinancing discussion | Low impact | Next filing |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/6dfd8435f3e821e204a09b72c9bb08513f6582581b6ae00d59669be20dfdb1e8/1.response.md; chdn-2026-11-05-credit_snapshot-host | Source readiness, seven sources | Medium: analyst work product | Required headings present; hashes listed | Accepted with limitations | Did not record the portfolio review |
| CP-1 | requests/CP-1/1b4cf732c5b04f61bcfda91f37010494c2399796617d9b2dcde22c5efb18064f/2.response.md; same run | Financial base, FY2025 to Q3 2026 | Medium: analyst work product | Required headings and chart sections present | Accepted with limitations | One wrong page reference, one quote punctuation difference |
| CP-1A | requests/CP-1A/158f2d54e085b204ff3f2ac724871b6821c7b3b6c71adca327d5da231336c961/2.response.md; same run | Business, governance, transactions | Medium: analyst work product | Required headings and selectors present | Accepted with limitations | One total off by 0.1 |
| CP-2 | requests/CP-2/2e079e7b7ce22438deeb1daa34c0e4953c152c4d492c17d73320482705115384/1.response.md; same run | Credit synthesis | Medium: analyst work product | Required headings and selectors present | Accepted with limitations | Covenant comfort inferred |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1A, CP-2 | Sale of nine gaming properties | Supported by one filed sentence | Not corroborated in the Q2 release extract; terms absent | Obtain announcement | Restrict committee use of the earnings weight |
| Minor | CP-1 | Debt register springing maturity quote | Supported | Quotation marks around springing maturity omitted | Quote as printed | None |
| Minor | CP-1 | Balance sheet table, cash and restricted cash at September 30, 2026 | Supported | Cited page 3; figures on page 2 | Correct locator | None |
| Minor | CP-2 | Basis statements for covenant cushions | Partly supported | Rests on December 2025 data | Label as inference | Restrict covenant statements |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | FY2025 outlays total 661.0 | Components sum to 660.9; the 166.0 gap is correct | None | Use 660.9 | None |
| Material | CP-1, CP-2 | Computed secured leverage against covenant ratio | Computed 1.54x at December 2025 against reported 1.4x; covenant definitions not supplied | Definition difference | Keep covenant statements to the reported ratios | Restrict covenant statements |
| Material | CP-1, CP-1A | Net bank leverage 3.8x against computed 3.68x | Management metric undefined | Definition difference | Treat as attributed claim | Monitoring note |
| Minor | CP-1 | Mixed units in LTM sums | FY2025 to one decimal, others whole | None | Carry rounding caveat | None |
| Minor | CP-1 | Interest estimate 149 read as interest plus amortization | Stated as analyst inference in CP-1 | None | Keep inference label | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Springing maturity ties revolver and Term Loan A to refinancing of notes 91 days before maturity | Executed eighth amendment | Only a 10-Q summary is supplied | Add the 8-K exhibit | Legal review of the amendment wording |
| Material | CP-1, CP-1A | Credit agreement is secured by substantially all wholly owned assets; notes are unsecured with guarantors not named | Credit agreement, security documents and indentures | Guarantor identity and carve-outs not supplied | Add executed documents | Legal review of guarantee and collateral release terms |
| Material | CP-1A, CP-2 | Capacity for restricted payments and asset-sale prepayments | Credit agreement covenants | Baskets not supplied | Add credit agreement | Legal review of baskets |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 to CP-2 | No relative value, spread, price or yield claim is made in any upstream handoff, and the context supplies no quotes, ratings or peers | Market quotes and spreads | None needed for the claims made | None | Relative value is outside this run's scope |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1 | The portfolio review sentence in the Q3 10-Q was not recorded | CP-1A supplements CP-1; CP-1 cannot be edited | Rely on CP-1A for this fact | CP-2 uses it |
| Minor | CP-1A, CP-2 | CP-1A reports a 37 difference between affiliate contribution and distributions; CP-2 splits it into 28 and 9 | CP-2 refines CP-1A | None | Consistent |
| Minor | CP-0, CP-1 | CP-0 expected net debt definition differences; CP-1 confirmed that the MD&A net debt does not net cash | None | None | Consistent |
| Minor | CP-1, CP-2 | CP-1 leverage series and CP-2 trend statement agree (gross 4.28x falling to 3.81x) | None | None | Consistent |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Duplication | The same illustrations (post-redemption liquidity, break-even proceeds) appear in the reader summary, credit view, key findings and risk table | Label each as illustrative once | Reader may overread illustrations |
| Minor | CP-2 | Wording | Undistributed equity income of 9 is described as not cash although it may be distributed later | Describe as not received in the period | Low |
| Material | CP-2 | Materiality | Portfolio review ranks among the top drivers but has the thinnest lineage | Flag in committee material | Restrict use |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Sources section | Lists the seven sources as underlying rather than directly cited, so lineage must be followed through the financial base and business context | Keep as stated; this module re-opened the pages | None |
| Minor | CP-1 | Revision history | First answer was refused for missing chart sections and repaired in attempt 2 | None | None |
| Minor | CP-1A | Revision history | First answer exceeded a word limit in the summary table and was repaired | None | None |
| Minor | CP-0 | Handoff content | Does not record the portfolio review sentence on the Q3 10-Q business page | Carry via CP-1A | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP-5-ISS-001 | Material | CP-1A, CP-2 | Evidence support | Portfolio review rests on one sentence with no terms | Obtain announcement and credit agreement terms | Restricts committee use of the earnings weight and break-even proceeds | Open |
| CP-5-ISS-002 | Material | CP-1, CP-2 | Inference | Covenant comfort after December 2025 is inferred | Obtain compliance certificate | Restricts covenant statements | Open |
| CP-5-ISS-003 | Material | CP-1, CP-2 | Assumption | Post-redemption liquidity is illustrative | Obtain redemption details | Restricts liquidity statements | Open |
| CP-5-ISS-004 | Material | CP-1, CP-1A | Definition | Net bank leverage undefined against computed 3.68x | Treat as attributed claim | Monitoring note | Open |
| CP-5-ISS-005 | Material | CP-1, CP-2 | Legal source | Springing maturity, guarantees and restricted payments rest on summaries | Add executed documents | Legal review dependency | Open |
| CP-5-ISS-006 | Minor | CP-1A | Calculation | FY2025 outlays total 661.0 against 660.9 | Use 660.9 | None | Open |
| CP-5-ISS-007 | Minor | CP-1 | Locator | Cash and restricted cash cited on page 3, found on page 2 | Correct locator | None | Open |
| CP-5-ISS-008 | Minor | CP-1 | Quotation | Springing maturity quotation lacks printed quotation marks | Quote as printed | None | Open |
| CP-5-ISS-009 | Minor | CP-1 | Gap | Non-cash debt exchange of 198 unexplained | Read refinancing note | None | Open |

Research QA status: committee use is permitted only as Restricted, because no Critical issue exists but five Material issues limit conclusions on the portfolio review, covenants, liquidity after the redemption, leverage definition and legal terms. No numeric confidence score is stated in this handoff.

## Calculations

Recomputed in this module from the pinned sources, with results and match to the upstream handoffs.

1. LTM Adjusted EBITDA: 1,205.3 + 998 - 958 = 1,245.3. Matches.
2. LTM revenue 2,925.9 + 2,339 - 2,260 = 3,004.9; net interest expense 297.7 + 211 - 222 = 286.7; cash interest 294.5 + 173 - 193 = 274.5; operating cash flow 769.8 + 660 - 674 = 755.8; capital expenditures 274.9 + 176 - 225 = 225.9; free cash flow 755.8 - 225.9 = 529.9. All match.
3. Leverage: 4,748 / 1,245.3 = 3.81x; (4,748 - 167) / 1,245.3 = 3.68x; December 2025: 5,155.1 / 1,205.3 = 4.28x and (5,155.1 - 200.6) / 1,205.3 = 4.11x. Match.
4. Quarterly series: LTM EBITDA 1,217.3 and 1,243.3; ratios 4.07x, 3.90x, 3.86x, 3.70x; cover 4.16x, 4.31x, 4.54x. Match.
5. Secured debt 79 + 1,069 + 500 = 1,648; 1,648 / 4,748 = 34.7%; (1,648 - 167) / 1,245.3 = 1.19x; post-redemption (2,248 - 167) / 1,245.3 = 1.67x. Match.
6. Reconciliations: FY2025 385.5 + 233.1 + 297.7 + 146.9 + 30.2 + 11.7 + 10.1 + 5.1 + 47.5 + 38.6 - 1.1 = 1,205.3; nine months 2026 405 + 176 + 211 + 147 + 19 + 7 + 2 + 6 + 28 - 3 = 998. Match.
7. FY2025 sources and uses: 30.8 + 427.8 + 17.0 + 185.3 = 660.9 (CP-1A states 661.0); 494.9 - 660.9 = -166.0; net borrowings 1,098.1 - 881.7 = 216.4 equal to the change in total debt 5,155.1 - 4,938.7. Difference of 0.1 logged.
8. Shares: 1,148 / 2,339 = 49.1%; 780 / 2,339 = 33.3%; 410 / 2,339 = 17.5%; 477 / 998 = 47.8%; 143 / 384 = 37.2%. Match.
9. Equity-affiliate bridge: 115 + 28 = 143; 115 - 106 = 9; 143 - 106 = 37 = 28 + 9. Match.
10. Portfolio review: 280 / 1,245.3 = 22.5%; 300 / 1,245.3 = 24.1%; 3.679 x 280 = 1,030; 3.679 x 300 = 1,104. Match, illustrative.
11. Springing dates: 2028-01-15 less 91 days = 2027-10-16; 2030-04-01 less 91 days = 2029-12-31; 2031-05-01 less 91 days = 2031-01-30. Match.
12. Covenant cushions: (3.9 - 2.5) / 3.9 = 35.9%; 1 - 2.5 / 4.34 = 42.4%. Match, indicative.
13. Lineage tests: 56 double-quoted strings in the four handoffs were compared with the sources after whitespace and quotation-mark normalization; 3 were field names or placeholders rather than source quotations, 52 of the other 53 matched exactly and one differed only in the quotation marks printed around springing maturity. 37 page-level checks of figures and phrases were run; 36 matched the cited page and one cash figure was on a different page than cited.

## Gaps

| Gap | Consequence | Action |
| --- | --- | --- |
| Portfolio review terms and the July 29, 2026 announcement text are not supplied | Earnings weight and break-even proceeds stay illustrative | Obtain announcement and credit agreement sale terms |
| Covenant compliance after December 31, 2025 and covenant definitions are not supplied | Covenant comfort is an inference | Obtain compliance certificate |
| Executed credit agreement, eighth amendment, indentures and proxy are not supplied | Legal and governance claims rest on summaries | Add executed documents |
| Redemption price and cash at October 19, 2026 are not supplied | Post-redemption liquidity is illustrative | Check next filing |
| Net bank leverage definition is not supplied | Cannot reconcile to computed 3.68x | Treat as attributed claim |

Process note: this module did not run the external confidence-score and completeness scripts, which are not available in this repository; the registers above were completed by hand against the declared columns, and the status above is a judgement, not a computed score.

## Next module

None. CP-5 is the last module selected for this run; the next step is report assembly and a second reviewer comparing each handoff with the sources, with the flagged items in the issue log carried into committee material.
