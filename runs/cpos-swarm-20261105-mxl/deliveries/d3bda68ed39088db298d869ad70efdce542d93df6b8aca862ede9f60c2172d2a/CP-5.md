## Request

Module: evidence trace and research-integrity review for MAXLINEAR, INC (MaxLinear, Inc., Nasdaq: MXL, issuer id mxl), as of 2026-11-05, evidence cutoff 2026-11-05, run mxl-2026-11-05-credit_snapshot-host. Pathway: credit snapshot; reporting currency USD, amounts in thousands unless a label says millions; current period q3-2026, prior period fy-2025. Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most. Scope: Top 5 material credit drivers (default scope), with a full audit of the four supplied handoffs for citation support, calculation reproducibility, legal and structural claims, market claims, cross-module consistency and handoff integrity. This module is a governance layer: it changes no credit conclusion and repairs no lineage silently. Upstream re-anchor: the handoffs consumed are the readiness, financial base, business and transaction, and credit synthesis handoffs of this run, all for MaxLinear, Inc., consolidated, as of 2026-11-05, current period q3-2026 (nine months to 2026-09-30) and prior period fy-2025, USD thousands. Method note: the numeric confidence score and the quality-assurance status are computed by the runtime from the classification and severity counts given below; this handoff does not hand-derive a score.

## Sources

### Issuer sources relied on

Source document IDs are assigned by this module; locators are `page:N` extraction chunks, not printed pages.

| Source document ID | Source name | sha256 |
| --- | --- | --- |
| SRC-01 | 10-K_2025-12-31_mxl-20251231.htm.jsonl | 88c5a5c8ff6cf18541031ab4aef4feb9645b937db462a2943427cc48c137e1d9 |
| SRC-02 | 10-Q_2026-03-31_mxl-20260331.htm.jsonl | 42848ffc444d8c47a09304ae1148778a878e57d84c54fa74dc1f2b0e6e5d0dd8 |
| SRC-03 | 10-Q_2026-06-30_mxl-20260630.htm.jsonl | 01411c1534e3e0c0e916b41e14102517d827593ed353c6e2edbb7bcfabe4eb3d |
| SRC-04 | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | 75f4d013edbcd52763843513db2d44d0258392fcbcf7fab3f738307f7e5ec1a3 |
| SRC-05 | EX-99.1_2026-04-22_a03312026exhibit991.htm.jsonl | 80656f36f632a9814cfc0d89b1465026471d15c2a52a4f467e504c7d5e0b776a |
| SRC-06 | EX-99.1_2026-07-23_a06302026exhibit991.htm.jsonl | 513984500469e10cfb125419373d89d4b53d02f7f1ffe85723d32af0bb949f83 |
| SRC-07 | EX-99.1_2026-10-22_a09302026exhibit991.htm.jsonl | 2f6d78692e5e0106407183ea23f9296509641c88888df05a93887a904e78fabf |

Run context (not issuer evidence): context, sha256 39695f94e05534dbaa55be69eaec116e2e3f550f0af980e236d8132f5e5386f2.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 5befe5c880ee0e3433b442e8789a41a9cded34b374570aca05a9aef7730f3cef | Source readiness and entity roles, re-audited |
| CP-1 | 2832c94f6492e1df4076ecb5839e253635a2fd23b2e187e34996c901c739795e | Financial base, re-audited against sources |
| CP-1A | f533fc4fd71da72246347836548cfdc7ef38585fe6508619d7c09dfc4405a609 | Business and transaction context, re-audited against sources |
| CP-2 | 4ebbbc5436d29da37effcc60911120269e4bd89ebe4a63cf3b70fd356395209b | Credit synthesis, traced to its upstream basis |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four handoffs trace to filed sources with page locators and agree on their figures, but committee use should be restricted: covenant terms rest on conflicting issuer summaries and the Silicon Motion exposure has no source amount. | Low | The executed credit agreement is not supplied, so covenant definitions, guarantor coverage and headroom cannot be traced beyond issuer summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Figures repeated across the four handoffs are identical, including debt principal of 165,000, cash of 81,085 and leverage of 5.52x gross and 2.81x net. | Committee readers can rely on one consistent set of numbers. | High |
| Cited page locators for the main figures were reopened in the sources and matched the figures. | Directly sourced facts can be relied on at the cited level, subject to extraction fidelity not being reviewed. | High |
| Trailing EBITDA is an analyst proxy, and the depreciation basis for FY2025 is inferred from statement sums and a rounded filing input. | The leverage ratios are traceable but are not the covenant measure, so treat them as indicative. | Medium |
| Covenant wording differs across filings and quarter-end revolver commitments are implied, not printed. | Liquidity and leverage headroom cannot be confirmed from source. | High |
| No source gives an amount for the Silicon Motion exposure. | The downside from the claim can only be tested with sensitivity thresholds, not sized. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 is calculated, 0 are assumption-based, 0 are analyst inferences, and 2 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the executed credit agreement and its covenant EBITDA definition, which matters because default risk and liquidity headroom depend on covenant terms that the filings summarise in conflicting ways, and it implies that committee use is restricted to a credit snapshot with these limits stated, not covenant-compliance or loss-outcome statements.

### Traceability summary

| Rank | Credit driver | Classification | Traceability status | Key gap |
| --- | --- | --- | --- | --- |
| 1 | Earnings inflection and trailing leverage | Calculated | Remediation Needed | EBITDA definition differs from the covenant |
| 2 | Negative cash conversion and revolver-funded growth | Directly Sourced | Committee-Ready | Letters of credit not supplied |
| 3 | Customer, supplier and order-basis concentration | Directly Sourced | Committee-Ready | Customer identities and backlog not disclosed |
| 4 | Covenant headroom and the 2028 debt structure | Conflicting | Remediation Needed | Executed agreement not supplied |
| 5 | Silicon Motion exposure | Insufficient Information | Not Traceable | No amount or range in any source |

### Top five material credit drivers

| Rank | Credit driver | Originating module | Source-supported basis | Why material | Committee relevance | Source trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Earnings inflection: income from operations 30,227 in Q3 2026 against negative 17,209 in Q1 2026; trailing EBITDA proxy 29,865; total debt / EBITDA 5.52x, net 2.81x, cover 3.51x | CP-1 | Operating income, revenue and cash flow lines from the 10-Q statements; D&A harmonised across filings | The ratios are carried by one quarter, so a demand pause reverses leverage and coverage within quarters | Sets the leverage tolerance and monitoring posture | SRC-04 `page:4`-`page:7`; SRC-02 `page:2`-`page:4`; SRC-03 `page:4`-`page:6`; SRC-01 `page:136`-`page:138`, `page:160`, `page:163`; SRC-06 `page:10`; SRC-07 `page:9` | Proxy is not the covenant EBITDA; FY2025 depreciation rounded |
| 2 | Cash conversion: nine-month operating cash flow negative 17,653, free cash flow negative 32,688, revolver drawn 40,000 | CP-1 | Cash flow statement and note 8 | Prepayments and purchase commitments precede revenue cash, so growth is revolver-funded | Liquidity is the binding constraint, not earnings | SRC-04 `page:6`, `page:19`-`page:20`, `page:62` | Letters of credit and borrowing conditions not supplied |
| 3 | Concentration and short visibility: ten largest customers 56% of nine-month 2026 revenue, no long-term purchase commitments, one supplier 52% of Q3 2026 purchases | CP-1A | MD&A and notes of the third quarter 10-Q and the 10-K | Fast revenue transmission from design wins or order pauses | Business risk driver for the credit view | SRC-04 `page:34`, `page:46`-`page:47`; SRC-01 `page:21`-`page:22`, `page:106` | Customer identities and backlog not disclosed |
| 4 | Covenant headroom and structure: liquidity floor 80.0 million then 60 million, total net leverage ceiling 3.50 to 1.00, all principal due 2028 | CP-1, CP-2 | Note 8 and subsequent event note of the third quarter 10-Q | Default and refinancing risk depend on these terms | Determines headroom and the 2028 refinancing window | SRC-04 `page:20`-`page:24`, `page:44`-`page:45`, `page:48`; SRC-03 `page:23`, `page:60` | Executed agreement not supplied; wording conflicts across filings |
| 5 | Silicon Motion arbitration and related suits, no amount, no accrual | CP-1A, CP-2 | Legal note of the third quarter 10-Q and the 10-K | A cash claim that could rival liquidity | Tail risk to liquidity and the 2028 refinancing | SRC-04 `page:38`-`page:43`; SRC-01 `page:37`-`page:38`, `page:98` | Amount not disclosed; arbitration confidential |

### Traceability map

| Credit driver / conclusion | Originating module | Source evidence | Citation present? | Source quality | Classification | Claim status | Confidence level | Traceability status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Earnings inflection and trailing leverage | CP-1 | Statement lines at SRC-04 `page:4`-`page:7` and EBITDA proxy computed from them | Yes | Filed statements, unaudited quarters | Calculated | Calculated, definition stated | Medium | Remediation Needed |
| Cash conversion and revolver-funded growth | CP-1 | Cash flow statement SRC-04 `page:6`; note 8 SRC-04 `page:19` | Yes | Filed statements | Directly Sourced | Documentary | High | Committee-Ready |
| Concentration and visibility | CP-1A | SRC-04 `page:46`-`page:47`, `page:34`; SRC-01 `page:106` | Yes | Filed statements and MD&A | Directly Sourced | Documentary | High | Committee-Ready |
| Covenant headroom and 2028 structure | CP-1, CP-2 | SRC-04 `page:23`-`page:24`; SRC-03 `page:23` against `page:60` | Yes | Issuer summaries of an unsupplied legal document | Conflicting | Conflict logged | Low | Remediation Needed |
| Silicon Motion exposure | CP-1A, CP-2 | SRC-04 `page:38`, `page:43` | Yes for existence, none for amount | Filed statements | Insufficient Information | Missing amount | Low | Not Traceable |
| Credit view and thesis | CP-2 | Upstream handoff sections only, by design | Partial | Synthesis of tagged upstream rows | Analyst Inference | Analyst Interpretation | Medium | Remediation Needed |

### Analytical appendix — complete canonical registers

#### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-01 | 10-K_2025-12-31_mxl-20251231.htm.jsonl | High: audited annual report | Fiscal 2025 with 2024 and 2023 comparatives | MaxLinear, Inc. consolidated | Statements, debt note, contractual obligations, litigation, business, risk factors | Revolver terms superseded by 2026 amendments; extraction fidelity not reviewed | Financial base, business context |
| SRC-02 | 10-Q_2026-03-31_mxl-20260331.htm.jsonl | High: unaudited quarterly filing | Quarter to 2026-03-31 | MaxLinear, Inc. consolidated | Statements, debt note, second amendment | Cash flow line includes lease amortization | Financial base |
| SRC-03 | 10-Q_2026-06-30_mxl-20260630.htm.jsonl | High: unaudited quarterly filing | Quarter and six months to 2026-06-30 | MaxLinear, Inc. consolidated | Statements, debt note, liquidity | Liquidity covenant wording conflict at `page:23` | Financial base |
| SRC-04 | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | High: unaudited quarterly filing | Quarter and nine months to 2026-09-30 | MaxLinear, Inc. consolidated | Statements, note 8, contingencies, subsequent event, liquidity | MD&A states revolver at post-amendment size | All modules |
| SRC-05 | EX-99.1_2026-04-22_a03312026exhibit991.htm.jsonl | Medium: management release | Quarter to 2026-03-31 | MaxLinear, Inc. consolidated | Results, outlook, credit agreement announcement | Management claims | Financial base cross-check |
| SRC-06 | EX-99.1_2026-07-23_a06302026exhibit991.htm.jsonl | Medium: management release | Quarter to 2026-06-30 | MaxLinear, Inc. consolidated | Results, non-GAAP bridge, discrete D&A | Management claims | Financial base D&A basis |
| SRC-07 | EX-99.1_2026-10-22_a09302026exhibit991.htm.jsonl | Medium: management release | Quarter to 2026-09-30 | MaxLinear, Inc. consolidated | Results, outlook, discrete quarter columns | Management claims | Financial base, business context |
| CTX-01 | context | Run settings, not evidence | As of 2026-11-05 | Run | Sector label; blanks for sponsor, ratings, legal documents | Blank fields not read as zero | Scope only |

#### Statement-level lineage

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net revenue Q3 2026 was 218,057 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:4`; also SRC-07 `page:7` | CP-1 Financials and credit metrics | Sourced | High | Reopened and matched |
| Income from operations Q3 2026 was 30,227 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:5` | CP-1 Financials and credit metrics | Sourced | High | Reopened and matched |
| Cash and cash equivalents 81,085 at 2026-09-30 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:4`; SRC-07 `page:9` | CP-1 chart data liquidity | Sourced | High | Release and 10-Q agree |
| Total debt principal 165,000 (term loan 125,000, revolver 40,000) | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:19`-`page:20` | CP-1 Debt schedule | Sourced | High | Carrying amount 164,062 reconciles |
| Revolver matures 2028-03-23; term loan 2028-06-23 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:20`, `page:23` | CP-1 chart data debt maturities | Sourced | High | Effect of the 2026-10-16 amendment on maturity not stated |
| Liquidity floor 80.0 million at 2026-09-30, reduced to 60 million on 2026-10-16 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:24`; `page:44`-`page:45` | CP-1 Covenants | Sourced | High | Subsequent event tagged |
| Total net leverage ceiling 3.50 to 1.00 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:23`-`page:24` | CP-1 Covenants | Sourced | Medium | Issuer summary of unsupplied agreement |
| Quarter-end revolver commitments 130,000 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl; EX-99.1_2026-04-22_a03312026exhibit991.htm.jsonl | SRC-04, SRC-05 | SRC-04 `page:44`; SRC-05 `page:2` | CP-1 chart data liquidity | Inference | Medium | Implied by 200 total less 70 increase and by 100 plus 30 |
| Nine-month operating cash flow negative 17,653 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:6` | CP-1 Financials and credit metrics | Sourced | High | Reopened and matched |
| Inventory purchase obligations 272,967 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:37`, `page:58` | CP-1 Claims outside the debt figure | Sourced | High | Total with other obligations 347,556 |
| Ten largest customers 56% of nine-month 2026 revenue; 65% in FY2025 | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl; 10-K_2025-12-31_mxl-20251231.htm.jsonl | SRC-04, SRC-01 | SRC-04 `page:46`; SRC-01 `page:106` | CP-1A Company and operating model | Sourced | High | Customers not named |
| Infrastructure 57% of Q3 2026 revenue against 32% | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:34`-`page:35` | CP-1A Company and operating model | Sourced | High | Table split across chunks |
| Silicon Motion arbitration unquantified; no loss accrued | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:38`, `page:43` | CP-1A, CP-2 | Sourced | High | Arbitration confidential |
| Stockholder suits two in the 10-K, three in the third quarter 10-Q | source-text/ | 10-K_2025-12-31_mxl-20251231.htm.jsonl; 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-01, SRC-04 | SRC-01 `page:98`; SRC-04 `page:38`, `page:40` | CP-1A Conflicts and version changes | Sourced | High | Version change logged |
| Ticking fee 18.3 million paid in August 2023 | source-text/ | 10-K_2025-12-31_mxl-20251231.htm.jsonl | SRC-01 | `page:158` | CP-1A Transaction summary | Sourced | High | Historical |
| FY2025 cash flow D&A of 43,992 includes lease amortization | source-text/ | 10-K_2025-12-31_mxl-20251231.htm.jsonl; EX-99.1_2026-07-23_a06302026exhibit991.htm.jsonl | SRC-01, SRC-06 | SRC-01 `page:137`; SRC-06 `page:10` | CP-1 Depreciation and amortization basis | Inference | Medium | Inferred from statement sums and the Q1 2026 restatement in SRC-06 |
| FY2025 depreciation 23.2 million and intangible amortization 13,313 | source-text/ | 10-K_2025-12-31_mxl-20251231.htm.jsonl | SRC-01 | `page:163`, `page:160` | CP-1 Depreciation and amortization basis | Sourced | High | Depreciation rounded to 0.1 million |
| Trailing EBITDA proxy 29,865 | source-text/ | Derived | SRC-01, SRC-04 | See calculation register | CP-1 Calculations | Calculated | Medium | Analyst-defined proxy |
| Trailing cash paid for interest 8,508 | source-text/ | 10-K and third quarter 10-Q | SRC-01, SRC-04 | SRC-01 `page:138`; SRC-04 `page:7` | CP-1 Calculations | Calculated | High | FY2025 plus nine months 2026 less nine months 2025 |
| Restricted cash 28,779, held as collateral for letters of credit | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl; 10-K_2025-12-31_mxl-20251231.htm.jsonl | SRC-04, SRC-01 | SRC-04 `page:4`; SRC-01 `page:141` | CP-1 Claims outside the debt figure | Sourced | High | Policy statement, not an amount of letters of credit issued |
| Share repurchases 20.0 million in 2025, 55.0 million remaining | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:44` | CP-1A Governance and capital allocation | Sourced | High | None in nine months 2026 |
| One supplier took 52% of Q3 2026 inventory purchases | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:34` | CP-1A Company and operating model | Sourced | High | Supplier not named |
| Q4 2026 revenue outlook 240 to 260 million | source-text/ | EX-99.1_2026-10-22_a09302026exhibit991.htm.jsonl | SRC-07 | `page:2` | CP-1, CP-1A | Sourced | Medium | Management language |
| 45 record holders and about 34,000 beneficial holders | source-text/ | 10-K_2025-12-31_mxl-20251231.htm.jsonl | SRC-01 | `page:103` | CP-1A Company profile | Sourced | High | As of 2026-01-22 |
| Note receivable from a supplier of 8.0 million | source-text/ | 10-Q_2026-09-30_mxl-20260930.htm.jsonl | SRC-04 | `page:18` | CP-1A Company and operating model | Sourced | High | Repayment conditional on utilization targets |

#### Calculation and assumption register

Every calculation below was recomputed in this module from the cited inputs; no difference from the upstream value was found.

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Depreciation and intangible amortization, trailing twelve months to 2026-09-30 | CP-1 Calculations | FY2025 23.2 million plus 13,313; nine months 2026 26,983; nine months 2025 27,572 | 36,513 + 26,983 - 27,572 = 35,924 | Calculated | Calculated with rounded input | Medium | Leverage, coverage | SRC-01 `page:163`, `page:160`; SRC-04 `page:6` |
| Trailing EBITDA proxy | CP-1 Calculations | Trailing income from operations negative 6,059; depreciation and amortization 35,924 | (6,059) + 35,924 = 29,865 | Calculated | Calculated, proxy definition | Medium | Leverage, coverage | SRC-01, SRC-04 statements |
| Total debt / EBITDA proxy | CP-1, CP-2 | 165,000 and 29,865 | 165,000 / 29,865 = 5.52x | Calculated | Calculated | Medium | Leverage | SRC-04 `page:19` |
| Net debt / EBITDA proxy | CP-1, CP-2 | Net debt 83,915 (165,000 less 81,085) and 29,865 | 83,915 / 29,865 = 2.81x | Calculated | Calculated | Medium | Leverage, covenant proxy | SRC-04 `page:4`, `page:19` |
| EBITDA / cash interest | CP-1, CP-2 | 29,865 and trailing cash interest 8,508 | 29,865 / 8,508 = 3.51x | Calculated | Calculated | Medium | Debt service | SRC-01 `page:138`; SRC-04 `page:7` |
| Liquidity covenant measure | CP-1, CP-2 | Cash 81,085, undrawn 90,000 (130,000 less 40,000), floor 80,000 | 81,085 + 90,000 - 80,000 = 91,085 | Calculated | Calculated, commitments inferred | Medium | Liquidity | SRC-04 `page:20`, `page:24`, `page:44` |
| Liquidity pro forma 2026-10-16 | CP-1, CP-2 | Cash 81,085 (not updated), undrawn 160,000, floor 60,000 | 81,085 + 160,000 - 60,000 = 181,085 | Calculated | Illustrative | Low | Liquidity | SRC-04 `page:44`-`page:45` |
| Leverage cushion on the proxy | CP-1 | Net debt 83,915; ceiling 3.50; EBITDA 29,865 | 29,865 - 83,915 / 3.50 = 5,889 | Calculated | Calculated, proxy definition | Low | Covenant headroom | SRC-04 `page:23`-`page:24` |
| Payment reaching the 3.50x ceiling | CP-2 | Same inputs | 3.50 x 29,865 - 83,915 = 20,613; with stock-based compensation added, 3.50 x 116,788 - 83,915 = 324,843 | Assumption-Based | Sensitivity, not a forecast | Low | Downside | CP-1 sensitivities |
| Discrete Q2 and Q3 2026 flows | CP-1 | Cumulative six- and nine-month columns less prior cumulative | For example operating cash flow (17,653) - (4,063) = (13,590) | Calculated | Matches release column | High | Trend | SRC-03 `page:6`; SRC-04 `page:6`; SRC-07 `page:9` |
| Expense block to operating profit | CP-1 | Gross profit and operating expense lines | Gross profit less R&D, SG&A and restructuring equals operating income, difference zero in six periods | Calculated | Recomputed | High | Earnings quality | SRC-01, SRC-02, SRC-03, SRC-04 statements |
| Trailing EBITDA excluding Q3 2026 | CP-1, CP-2 | 29,865 and Q3 2026 EBITDA proxy 39,080 | 29,865 - 39,080 = (9,215) | Calculated | Recomputed | Medium | Earnings durability | SRC-04 `page:4`-`page:5` |
| Indicative run-rate cover | CP-1 | Debt 165,000; weighted average effective rate 7.0%; EBITDA 29,865 | 165,000 x 7.0% = 11,550; 29,865 / 11,550 = 2.59x | Assumption-Based | Indicative | Low | Debt service | SRC-04 `page:19` |

#### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | Covenant headroom and compliance | Executed credit agreement, amendments and compliance certificate not supplied; wording conflicts across filings | Conflicting | Default risk and liquidity depend on covenant terms; headroom could be narrower or wider than the proxy | Obtain executed agreement and certificate | CP-1 Covenants; CP-2 Key findings |
| Critical | Silicon Motion exposure | No amount or range in any source | Insufficient Information | An unsized claim cannot be tested against liquidity and refinancing | Monitor filings; stress with thresholds only | CP-1A Transaction summary; CP-2 Key credit risks |
| Material | Trailing EBITDA proxy | Depreciation basis for FY2025 inferred; depreciation rounded | Analyst Inference | Moves trailing ratios by about 0.01x; definition differs from covenant | Obtain unrounded depreciation; state proxy label | CP-1 Chart data; CP-2 Credit view |
| Material | Quarter-end revolver commitments 130,000 | Implied by two consistent routes, not printed | Analyst Inference | Undrawn availability and the liquidity covenant measure depend on it | Obtain amendment text | CP-1 chart data liquidity |
| Material | Revolver availability | Letters of credit and borrowing conditions not supplied | Insufficient Information | Undrawn amount is gross | Obtain balances | CP-1 chart data liquidity; CP-2 |
| Minor | Sector label | Taken from the run context | Weak Lineage | Descriptive only | None | CP-1A Company profile |
| Minor | Credit synthesis | CP-2 cites upstream sections, not source pages, by design | Analyst Inference | Source trace runs through the other handoffs | None; trace in this module | CP-2 |

#### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven issuer sources cover fiscal 2025 and all 2026 quarters; no legal documents, proxy, ratings or post-2026-10-22 filings | Missing legal and proxy sources leave covenant and control facts on issuer summaries | Covenant-based conclusions are restricted | Add executed agreement, proxy and later filings |
| Citation completeness | Ready with Remediation | CP-0, CP-1 and CP-1A cite page locators throughout and the figures used by the top drivers were reopened and matched; CP-2 cites upstream sections | Chunk locators are not printed pages and extraction fidelity is unreviewed | Low risk of wrong citation; moderate risk of table-split misreads | Spot-check key tables against original files |
| Calculation traceability | Ready with Remediation | Formulas and inputs shown; recomputation matched; depreciation basis partly inferred | Proxy EBITDA is not the covenant measure | Ratios indicative, not compliance measures | Label proxy, obtain definitions |
| Assumption transparency | Ready with Remediation | Proxy definition, commitments inference and sensitivities are labelled | An unlabelled assumption would be read as fact | Sensitivities must not be quoted as forecasts | Keep labels in the report |
| Markdown and export artifact integrity | Committee-Ready | All four handoffs use the six required headings, tagged tables and the required selector headings | Table splits could mislead only if a heading were missing | None | None |

#### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed credit agreement, amendments, security agreement and compliance certificate | Legal source documents; the third amendment filing | Covenant definitions, baskets, guarantors and EBITDA definition drive default and liquidity risk | Covenants and liquidity sections of CP-1 and CP-2 | High impact | Credit agreement and 8-K exhibit |
| CP-5-GAP-002 | Silicon Motion exposure size | Any amount, range or reserve | Only identified claim that could rival liquidity | CP-1A, CP-2 downside | High impact | Future filings |
| CP-5-GAP-003 | Letters of credit issued and borrowing conditions | Balances and availability test | Undrawn availability is gross | Liquidity chart and covenant measure | Medium impact | Lender reports |
| CP-5-GAP-004 | Customer identities and order backlog | Customer data, bookings | Concentration and visibility cannot be tested | CP-1A, CP-2 business risk | Medium impact | Management disclosure |
| CP-5-GAP-005 | Proxy statement and holders above 5% | Ownership and board data | Control rights and change-of-control exposure | CP-1A profile | Medium impact | Proxy statement |
| CP-5-GAP-006 | Events 2026-10-22 to 2026-11-05 | Filings in that window | Cash, revolver draws and the Dish stay status are unobserved | All modules | Medium impact | Later filings |
| CP-5-GAP-007 | Reported leverage ratio and Consolidated EBITDA | Compliance certificate, definitions | Proxy cannot be tied to compliance | CP-1, CP-2 | High impact | Compliance certificate |
| CP-5-GAP-008 | Ratings and market data | Agency ratings, quotes | No market-implied cross-check | Context only | Low impact | Market data |
| CP-5-GAP-009 | Original-file fidelity of extracted tables | Spot-check against the original filings | Split tables could hide a misread | All modules | Low impact | Original filings |

#### Input module register

| Module | Handoff canonical file / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | CP-0 response / mxl-2026-11-05-credit_snapshot-host | Source readiness for seven sources | High filed sources, medium releases | Six required headings and view heading present | Accepted by runtime structural check | Analytical accuracy audited here |
| CP-1 | CP-1 response / mxl-2026-11-05-credit_snapshot-host | Financial base, four chart tables, metrics table | High, with analyst proxy | Six required headings, chart and metrics selectors present | Accepted by runtime structural check | Contains a garbled phrase noted in the handoff integrity audit |
| CP-1A | CP-1A response / mxl-2026-11-05-credit_snapshot-host | Business, ownership, transaction context | High | Six required headings and selectors present | Accepted after one repair | Word-count limit repaired in attempt 2 |
| CP-2 | CP-2 response / mxl-2026-11-05-credit_snapshot-host | Credit synthesis | Medium: upstream only | Six required headings and prose selectors present | Accepted by runtime structural check | No source citations by design |

#### Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1 | FY2025 and FY2024 depreciation and amortization basis | Inferred | Lease amortization inside the 10-K line is inferred from statement sums, not stated | State as inference in the report | Restricts precision of trailing EBITDA, not the direction |
| Material | CP-1 | Quarter-end undrawn revolver of 90,000 | Inferred | Commitments of 130,000 implied | Obtain amendment | Restricts liquidity precision |
| Minor | CP-1A | Sector label | Weak | From run context | Label as context | None |
| Minor | CP-2 | Source locators | Partial | Upstream sections only, by design | Trace through other handoffs | None |
| Minor | All | Locators | Complete | Chunk locators, not printed pages | State chunk basis | None |

#### Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Leverage and coverage ratios | Proxy EBITDA excludes stock-based compensation add-backs and differs from Consolidated EBITDA | Covenant EBITDA not supplied | Label proxy in the report | Ratios indicative only |
| Material | CP-1 | Depreciation basis drift | Lease amortization inside D&A in the 10-K and first quarter 10-Q, outside in later 10-Qs | First quarter 10-Q 10,939 against second quarter release 9,119 for the same quarter | Use the harmonised basis, as done | Resolved by documentation |
| Minor | CP-1 | Interest cover uses historical cash interest | Revolver draw not in full-year interest | None | Indicative run-rate cover shown | None |
| Minor | CP-2 | Breakeven payment | Strict-proxy threshold a lower bound | Definition unknown | Present range | None |

#### Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | CP-1, CP-2 | Covenant tests, levels and compliance | Executed credit agreement and amendments | Issuer summaries only | Obtain documents | Yes |
| Material | CP-1 | Collateral on substantially all assets; guarantors "certain domestic subsidiaries" | Security agreement and guarantor schedule | Guarantors not named | Obtain schedules | Yes |
| Material | CP-1A | Third amendment terms | The 8-K exhibit | Filing not supplied | Obtain exhibit | Yes |
| Material | CP-1A, CP-2 | Silicon Motion termination was proper and no break-up fee is owed | Merger Agreement and arbitration record | Company position only; arbitration confidential | Treat as management position | Yes |

#### Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | No relative value, spread, yield, price or peer claim appears in any handoff | Quotes, ratings, peer data | Context sets these blank | None needed for this scope | No market-implied cross-check available |

#### Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1, CP-1A, CP-2 | Liquidity covenant wording in the second quarter 10-Q (percentage of EBITDA against 80 million floor) | Same-filing inconsistency | Resolve against agreement; report both | Headroom unverified |
| Material | CP-0, CP-1, CP-2 | Springing secured net leverage test present in the 10-K and first two quarters, absent in the third quarter note | Version change | Resolve against agreement | Covenant package unresolved |
| Material | CP-0, CP-1, CP-2 | Revolver "up to 200 million" with 40,000 outstanding at quarter end | The 200 million is the post-2026-10-16 total | Show quarter-end and pro forma separately, as done | Handled consistently |
| Minor | CP-1A | Silicon Motion stockholder suits two in the 10-K, three in the third quarter 10-Q | Version change | None | Legal overhang widened |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Figures checked for identity across modules: debt 165,000, cash 81,085, purchase obligations 272,967, headroom 91,085, leverage 5.52x and 2.81x, cover 3.51x | No difference found | None | Consistent |

#### Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | Duplication | Covenant and Silicon Motion text repeats across three handoffs | Consolidate in the report | Reader fatigue only |
| Material | CP-2 | Materiality | The credit view depends on the proxy leverage and an unsized claim | Present with the stated limits | Restricts committee use |
| Minor | CP-1 | Presentation | Dense detail inside the metrics handoff | Keep chart and metrics tables as the report content | None |

#### Handoff structure and export integrity

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Calculations, trailing twelve months paragraph | Garbled phrase "(4,030) negative less 4,364" in the cash tax line; the result (2,602) is correct | Read as 5,792 + (4,030) - 4,364 | None |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Envelope | Runtime Markdown transport replaces the YAML envelope | None | None |
| Minor | CP-1A | Reader summary | First attempt exceeded the 40-word limit; repaired | None | None |

#### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISS-001 | Critical | CP-1, CP-2 | Legal source missing | Executed credit agreement, amendments and certificate not supplied | Obtain documents | Restricts committee use | Open |
| ISS-002 | Critical | CP-1A, CP-2 | Missing amount | Silicon Motion exposure unquantified | Monitor | Restricts committee use | Open |
| ISS-003 | Material | CP-1, CP-2 | Definition | Proxy EBITDA is not the covenant measure | Label proxy | Ratios indicative | Open |
| ISS-004 | Material | CP-1 | Inference | Depreciation basis for FY2025 inferred | State inference | Precision only | Open |
| ISS-005 | Material | CP-1 | Inference | Quarter-end revolver commitments implied | Obtain amendment | Liquidity precision | Open |
| ISS-006 | Material | All | Conflict | Covenant wording conflicts across filings | Resolve against agreement | Headroom unverified | Open |
| ISS-007 | Material | CP-1 | Gap | Letters of credit not supplied | Obtain balances | Liquidity precision | Open |
| ISS-008 | Minor | CP-1 | Presentation | Garbled phrase in a calculation line | None | None | Open |
| ISS-009 | Minor | CP-1A | Lineage | Sector from context | Label | None | Open |
| ISS-010 | Minor | CP-1A | Presentation | Word limit exceeded in attempt 1 | Repaired | None | Closed |

#### Clearance decision

Committee status: Restricted. The four handoffs may be used for a credit snapshot of MaxLinear, Inc. as of 2026-11-05 with the limitations above; they may not be used to assert covenant compliance or headroom, guarantor coverage, or any outcome of the Silicon Motion dispute. Severity counts for the runtime score, from the consolidated issue log: Critical 2, Material 5, Minor 2 open (one further minor item closed). Lineage of the Top 5 drivers: Directly Sourced 2, Calculated 1, Conflicting 1, Insufficient Information 1.

## Calculations

Independent recomputation performed in this module from the cited source figures, with no difference from the handoffs:

| Item | Inputs | Recomputed result |
| --- | --- | --- |
| Trailing income from operations to 2026-09-30 | (126,890) + 8,833 - (111,998) | (6,059) |
| Trailing depreciation and amortization on the harmonised basis | 36,513 + 26,983 - 27,572 | 35,924 |
| Trailing EBITDA proxy | (6,059) + 35,924 | 29,865 |
| Total debt / EBITDA proxy | 165,000 / 29,865 | 5.52x |
| Net debt / EBITDA proxy | (165,000 - 81,085) / 29,865 | 2.81x |
| EBITDA / cash interest | 29,865 / (8,598 + 6,425 - 6,515) | 3.51x |
| Liquidity covenant headroom | (81,085 + 130,000 - 40,000) - 80,000 | 91,085 |
| Payment reaching 3.50x | 3.50 x 29,865 - 83,915 | 20,613 |
| Cash reconciliation at 2026-09-30 | 81,085 + 1,359 + 27,420 | 109,864, equal to the printed total |
| Debt carrying amount | 165,000 - 226 - 712 | 164,062, equal to the balance sheet |

## Gaps

The nine gaps in the gaps ledger above stand. The most important is the executed credit agreement with its amendments and compliance certificate (CP-5-GAP-001); the second is any amount or range for the Silicon Motion exposure (CP-5-GAP-002). Neither can be closed from the supplied sources. No new evidence was introduced in this module and no upstream conclusion was changed.

## Next module

This is the last module of the selected set. The report should be assembled from the accepted handoffs with the restriction stated: present the leverage and coverage figures as indicative proxies, show quarter-end and post-2026-10-16 liquidity separately, present both covenant formulations, and carry the Silicon Motion exposure as unquantified. Follow-up evidence to obtain, in priority order: executed credit agreement with Amendments No. 1 to No. 3 and the 8-K carrying the third amendment; compliance certificate with the Consolidated EBITDA calculation; issued letter of credit balances; any filing dated 2026-10-22 to 2026-11-05; the proxy statement.
