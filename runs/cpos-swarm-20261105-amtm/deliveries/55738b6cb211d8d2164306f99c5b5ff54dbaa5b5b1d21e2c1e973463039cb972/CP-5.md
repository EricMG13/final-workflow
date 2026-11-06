## Request

Amentum Holdings, Inc. (consolidated group), as of 2026-11-05, credit_snapshot pathway. Scope: trace the claims in the source-readiness, financial, business and synthesis handoffs back to the pinned filings and releases, re-perform their calculations, check the handoffs against each other, and grade whether the evidence supports committee use. Traceability scope is the Top 5 material credit drivers plus every statement the audit found defective; the conclusions of the upstream modules are not changed.

## Sources

### Issuer sources audited against

| Source name | sha256 (as pinned by CP-OS) |
| --- | --- |
| 10-K_2025-10-03_amtm-20251003.htm.jsonl | 8273d25a00529c2b44154e4079fb17aed384ffabfb0b6e916ff874e87d184e2c |
| 10-Q_2026-01-02_amtm-20260102.htm.jsonl | 53306aefcf67aafc6e963ada6d826aebfcc9ef2ae12c58e6020ff2739d2c4784 |
| 10-Q_2026-04-03_amtm-20260403.htm.jsonl | 39d2941eedc33b6b8a6975be5d0ab047229748e579ab149e336916a6515e4e3c |
| 10-Q_2026-07-03_amtm-20260703.htm.jsonl | e0cfefb75002bb2378240c82d12b55245568de0ae66e976bd3399e669ec7e5df |
| EX-99.1_2026-02-09_exhibit991-february92026.htm.jsonl | f4a0837903a2e7b5b24df97e0fe38362855d47b722b3db774277ece94a59d816 |
| EX-99.1_2026-05-11_exhibit991-may112026.htm.jsonl | 70874f67722755b78375d913af6706b9925581a1e0d597e3dc867f0ae2da1e41 |
| EX-99.1_2026-08-10_exhibit991-august102026.htm.jsonl | cf451c4e10bf61fb7f1fdcb128f9d46a9635fb48c3681eadc79c1a3f2194b093 |

### Context and handoffs reviewed

- Run context (settings, not issuer evidence): sha256 f35913dfc940216c52100a4ebad511585e07d7ab0e645bded7b78046135f5c43.
- Handoff CP-0 (source readiness), sha256 a73cd36f054f9d1f45a1a722b687f0bbcf428fae01c4dbd0e0acf28f5952073e. Identifier HO-0.
- Handoff CP-1 (financial base), sha256 3f7716d0288dc98301a065f43c1a1aafb7f2ca57911372ef5ca1732285e0a677. Identifier HO-1.
- Handoff CP-1A (business and transaction context), sha256 d5fb957740351fe382b18b816f2170cd01ce1de250ef7cfa5c0a7e961eb95b91. Identifier HO-1A.
- Handoff CP-2 (fundamental credit synthesis), sha256 63c4135cf049313f1699c30f7590c80b67fd898df69bdf26007da35bb98396d8. Identifier HO-2.

The source-readiness handoff (HO-0) was accepted with an error that cannot be edited; this review records it and the later correction (issue I-01).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The leverage, liquidity, cash flow and business findings trace to the filings and agree across the four analyses. Traceability is ready with remediation: a few statements are unsupported and the loan documents are missing. | Medium | No credit agreement, amendment, indenture or ratings are supplied, so covenant, payout and maturity conclusions cannot be traced to executed documents. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Net leverage of 3.03x, liquidity of USD 1,376 million and cash interest cover of 3.93x reproduce from filed statements and are identical in every analysis that uses them. | The committee can rely on these figures, subject to the management definition of Adjusted EBITDA. | High |
| An early analysis wrongly recorded cash-paid interest and taxes as not supplied; the filings print both and the financial analysis corrected this. | Cash interest cover rests on printed cash interest, so the correction is sound. | High |
| Three narrative statements are not supported by the sources: shutdowns delaying awards, the repricing lifting interest cover, and joint ventures explaining lower international revenue. | They affect narrative, not figures, and should be removed or qualified before committee use. | Medium |
| The maturity schedule, first lien headroom and implied fourth-quarter cash flow are calculations resting on stated assumptions. | Treat them as indicative; they cannot support covenant or refinancing conclusions. | Medium |
| Pay-cycle timing effects on quarterly operating cash flow were not carried into the cash conversion discussion. | Quarterly free cash flow comparisons may be distorted by timing, adding uncertainty to the conversion conclusion. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 2 are calculated, 0 are assumption-based, 1 is an analyst inference, and 1 is a weak-lineage, untraced, conflicting, or insufficient-information item. The most important provenance gap is the absence of the credit agreement, its April 24, 2026 amendment and the indenture, which matters because covenant headroom, payout capacity and collateral terms cannot be traced to an executed document, and implies that committee reliance on creditor-control and covenant conclusions is restricted. Figures for leverage, liquidity and cash flow were re-performed and match; five narrative statements need correction or qualification (issues I-02 to I-05 and I-14), and none changes a figure or the credit view.

### Traceability summary

| Rank | Credit driver | Classification | Traceability status | Main defect |
| --- | --- | --- | --- | --- |
| 1 | Net leverage 3.03x and liquidity USD 1,376 million | Calculated | Committee-Ready | Management EBITDA definition; liquidity includes cash held in joint ventures (I-14) |
| 2 | Cash conversion: free cash flow USD 213 million, USD 93 million excluding receivable sales | Calculated | Committee-Ready | Pay-cycle timing not carried (I-09) |
| 3 | Federal funding conditionality: 81% U.S. Government revenue, USD 6.2 billion funded of USD 48.2 billion backlog | Directly Sourced | Remediation Needed | Unsupported statement that shutdowns delayed awards (I-02) |
| 4 | Earnings quality: estimate adjustments USD 83 million against USD 40 million | Analyst Inference | Remediation Needed | Inference stated with different strength in two handoffs (I-13) |
| 5 | Creditor control and loan documentation | Insufficient Information | Not Traceable | Executed documents not supplied (I-07) |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register and module status

Module status: Ready with Limitations (all four upstream handoffs and seven filings are available; loan documents, ratings and the covenant definition are not). Traceability scope: Top 5. Entity key: issuer_id amtm is available in the run. Citation limitation: the source files are text renderings, and locators are the pack page numbers, not printed page numbers.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | 10-K_2025-10-03_amtm-20251003.htm.jsonl | High: audited annual report | FY2025, 53 weeks ended October 3, 2025, with FY2024 and FY2023 comparatives | Amentum Holdings, Inc. and subsidiaries; FY2024 and FY2023 are the predecessor perimeter | Statements, debt note, covenants, leases, pensions, business description, risk factors, Transaction | Part III incorporated by reference and not supplied; no exhibits | Financial base, business context |
| SRC-2 | 10-Q_2026-01-02_amtm-20260102.htm.jsonl | High: filed, unaudited | Q1 2026, quarter ended January 2, 2026 | Amentum Holdings, Inc. and subsidiaries | Interest paid, capacity, pay-cycle commentary | Pre-amendment debt | Cash flow quality |
| SRC-3 | 10-Q_2026-04-03_amtm-20260403.htm.jsonl | High: filed, unaudited | Q2 2026, quarter ended April 3, 2026 | Same | Balance sheet, debt table, subsequent event for the April 24, 2026 amendment | Amendment text not supplied | Context period figures |
| SRC-4 | 10-Q_2026-07-03_amtm-20260703.htm.jsonl | High: filed, unaudited | Q3 2026, three and nine months ended July 3, 2026 | Same | Statements, debt, amendment summary, MARPA, segments, backlog, liquidity | No lease or pension detail; no maturity table | Latest figures |
| SRC-5 | EX-99.1_2026-02-09_exhibit991-february92026.htm.jsonl | Medium: management release | Q1 2026 | Same | Headline, net leverage, guidance, pay-cycle commentary | Management measures; rating headline inconsistent | Context |
| SRC-6 | EX-99.1_2026-05-11_exhibit991-may112026.htm.jsonl | Medium: management release | Q2 2026 | Same | Net leverage, guidance, pay-cycle commentary | Management measures | Context period leverage |
| SRC-7 | EX-99.1_2026-08-10_exhibit991-august102026.htm.jsonl | Medium: management release | Q3 2026 | Same | Reconciliations, net leverage, guidance, awards | Management measures and claims | Latest leverage, guidance |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Net leverage 3.03x, gross 3.44x, liquidity USD 1,376 million, cash interest cover 3.93x | HO-1 | Debt 3,875, cash 459, revolver capacity 917, LTM Adjusted EBITDA 1,128, LTM interest paid 287 | Sets debt service capacity and refinancing room | Leverage tolerance and liquidity | SRC-4 pages 2, 5, 10, 12; SRC-7 page 10; SRC-1 pages 115 and 116 | Management EBITDA; 53-week LTM; cash in joint ventures |
| 2 | Cash conversion: free cash flow 213 and 93 excluding receivable sales | HO-1 | Operating cash flow 235, capex 22, MARPA inflow 120 | Cash for deleveraging depends on working capital and receivable sales | Debt reduction pace; monitoring | SRC-4 pages 4, 5, 9 | Pay-cycle timing not quantified |
| 3 | Federal funding conditionality | HO-1A | 81% direct U.S. Government revenue; funded backlog 6,240 of 48,237 | Revenue timing and conversion depend on appropriations | Revenue durability; liquidity buffer | SRC-1 pages 8 and 133; SRC-4 pages 7, 27, 28 | Award-delay claim unsupported |
| 4 | Earnings quality: net favorable estimate adjustments 83 against 40, add-backs 76, equity earnings 73 | HO-1A, HO-2 | Printed adjustments; reconciliations | Reported margin may include non-recurring catch-up | Leverage sensitivity to margin | SRC-4 page 8; SRC-7 pages 11 and 12 | EBITDA effect not given |
| 5 | Creditor control and documentation | HO-1A, HO-2 | Covenant wording pre-amendment only; ownership at closing only | Payout, priming and collateral terms drive loss given default mechanics | Control and monitoring posture | SRC-1 pages 71, 128, 148; SRC-4 pages 13, 31 | Executed documents not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net leverage 3.03x; liquidity 1,376; cover 3.93x | HO-1 | Debt table "Total debt 3,875"; cash "$ 459"; "917 million"; Q3 release "Net Leverage was 3.0x" | Yes | High | Calculated | Verified by re-performance | High | Committee-Ready |
| Free cash flow 213 and 93 excluding receivable sales | HO-1 | Operating cash flow 235, capex 22, MARPA inflow of 120 | Yes | High | Calculated | Verified by re-performance; timing not controlled | Medium | Committee-Ready |
| 81% U.S. Government revenue; funded backlog 6.2 billion of 48.2 billion | HO-1A | "Approximately 81% of the Company's revenues"; funded backlog 6,240, total 48,237 | Yes | High | Directly Sourced | Verified | High | Remediation Needed (award-delay wording) |
| Estimate adjustments exceed Adjusted EBITDA growth | HO-1A, HO-2 | 83 against 40; 828 against 804 | Yes | High for inputs | Analyst Inference | Inference; EBITDA effect of adjustments not printed | Medium | Remediation Needed |
| Covenant headroom and payout capacity | HO-1, HO-1A, HO-2 | Pre-amendment 5.00x maximum for the revolver; Q3 text names term loan A | Partial | High for text, none for amended terms | Insufficient Information | Indicative headroom only | Low | Not Traceable |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 3,875 at July 3, 2026 | SRC-4 debt table | 10-Q_2026-07-03_amtm-20260703.htm.jsonl | SRC-4 | page:10 Note 8 | HO-1 financials table | Sourced | High | Matches release page:10 |
| Cash 459 at July 3, 2026 | SRC-4 balance sheet | same | SRC-4 | page:2 | HO-1 liquidity table | Sourced | High | Matches cash flow page:5 |
| Revolver capacity 917 net of 83 of letters of credit | SRC-4 Note 8 | same | SRC-4 | page:12 | HO-1 liquidity | Sourced | High | 1,000 less 83 |
| LTM Adjusted EBITDA 1,128 | SRC-7 non-GAAP section | EX-99.1_2026-08-10_exhibit991-august102026.htm.jsonl | SRC-7 | page:10 | HO-1 leverage | Sourced | Medium | Management measure; re-performed as 1,104 + 828 - 804 |
| Interest paid 306, 175, 194 | Supplemental cash flow | SRC-1 and SRC-4 | SRC-1, SRC-4 | 10-K page:116; 10-Q page:5 | HO-1 interest cover | Sourced | High | Corrects HO-0 |
| Operating cash flow 235; capex 22 | Cash flow statement | SRC-4 | SRC-4 | page:4 | HO-1 cash flow | Sourced | High | |
| MARPA net inflow 120; maximum 400; balance sold 300 | Note 5 | SRC-4 | SRC-4 | page:9 | HO-1 claims outside debt | Sourced | High | |
| Term loan A 1,400 due April 24, 2031; term loan B 1,591 due September 27, 2031; revolver 1,000 | Note 8 | SRC-4 | SRC-4 | page:11 | HO-1 debt table; HO-1A transaction summary | Sourced | High | Amendment itself not supplied |
| Floating-rate share 74% | Calculated 2,866 / 3,875 | SRC-4 | SRC-4 | page:10 | HO-1 calculation 9; HO-2 | Calculated | High | |
| Swaps 1.3 billion maturing through January 31, 2027 | Note 8 | SRC-4 | SRC-4 | page:13 | HO-1, HO-2 | Sourced | High | |
| Pre-amendment maximum first lien net leverage 5.25x stepping to 5.00x | Note 12 | SRC-1 | SRC-1 | page:148 | HO-1 covenants | Sourced | High | Pre-amendment, revolver only |
| About 81% of FY2025 revenue from direct U.S. Government contracts | Item 1 | SRC-1 | SRC-1 | page:8; customer table page:133 | HO-1A, HO-2 | Sourced | High | Cross-check (7,678 + 3,994) / 14,393 |
| Funded backlog 6.2 billion; total 48.2 billion | MD&A backlog | SRC-4 | SRC-4 | page:27, page:28 | HO-1A, HO-2 | Sourced | High | |
| Net favorable estimate adjustments 83 against 40 | Note 3 | SRC-4 | SRC-4 | page:8 | HO-1A, HO-2 | Sourced | High | EBITDA effect not printed |
| 722 of voluntary term loan payments in FY2025 | MD&A | SRC-1 | SRC-1 | page:98 | HO-1A, HO-2 | Sourced | High | 191 + 250 + 281 |
| Shutdowns delayed or slowed awards | None found | none | none | none | HO-1A, HO-2 | Untraced | Not rated | Sources show revenue and collections effects only (SRC-4 page:27; SRC-5 page:2); award delay only as a general risk (SRC-4 page:21) |
| Lower international revenue mainly from joint venture deconsolidation | MD&A | SRC-4 | SRC-4 | page:8, page:23, page:25, page:27 | HO-1A | Analyst Inference | Medium | Management attributes the total and Global Engineering Solutions decline to several causes, not specifically international |
| Equityholder nomination rights five of 13 directors at 25.1% or more | Risk factors | SRC-1 | SRC-1 | page:71 | HO-1A | Sourced | High | Current ownership not supplied |
| Sponsor-linked holder, closing allocation 58.5% and 37.0% | Note 4 | SRC-1 | SRC-1 | page:128 | HO-1A | Sourced | High | Later transfers not supplied |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA 1,128 | HO-1, HO-2 | 1,104; 828; 804 | FY2025 + 9M 2026 - 9M 2025 | Calculated | Re-performed; equals printed 1,128 | High | PD, leverage | SRC-1 page:157; SRC-7 pages 11, 12 |
| Net leverage 3.03x | HO-1, HO-2 | 3,875; 459; 1,128 | (debt - cash) / LTM Adjusted EBITDA | Calculated | Re-performed: 3,416 / 1,128 = 3.03x | High | PD, refinancing | SRC-4 pages 2, 10 |
| Gross leverage 3.44x | HO-1, HO-2 | 3,875; 1,128 | debt / LTM Adjusted EBITDA | Calculated | Re-performed | High | PD | SRC-4 page:10 |
| LTM interest paid 287; cover 3.93x | HO-1, HO-2 | 306; 175; 194; 1,128 | 306 + 175 - 194; 1,128 / 287 | Calculated | Re-performed | High | Debt service | SRC-1 page:116; SRC-4 page:5 |
| Liquidity 1,376 | HO-1, HO-2 | 459; 917 | cash + undrawn revolver | Calculated | Re-performed; includes 123 of cash in joint ventures | Medium | Liquidity | SRC-4 pages 2, 12, 13 |
| Free cash flow 213; excluding receivable sales 93 | HO-1, HO-2 | 235; 22; 120 | operating cash flow - capex; less MARPA inflow | Calculated | Re-performed | High | Cash conversion | SRC-4 pages 4, 9 |
| Indicative maturity profile, 92% in two years | HO-1, HO-2 | Terms on SRC-4 pages 11 and 12; assumptions: amortization on original principal, no cash sweep, term loan B amortization unchanged by the 125 prepayment, other debt of 9 excluded | Quarterly percentages by fiscal year | Assumption-Based | Re-performed; next-twelve-month amortization 50.91 against current portion 54 | Medium | Refinancing | SRC-4 pages 2, 11, 12 |
| Indicative first lien net leverage 2.13x | HO-1 | 1,400; 1,466; 459; 1,128; 5.00x | (term loans - cash) / LTM Adjusted EBITDA | Assumption-Based | Re-performed; covenant definition not supplied | Low | Covenant headroom | SRC-1 page:148; SRC-4 page:13 |
| Implied fourth-quarter free cash flow 312 to 362 | HO-1, HO-2 | Guidance 525 to 575; nine-month 213 | guidance less nine-month actual | Calculated | Re-performed from management guidance | Medium | Liquidity, deleveraging | SRC-7 page:4; SRC-4 page:4 |
| Net favorable adjustments rise 43 against EBITDA rise 24 | HO-1A, HO-2 | 83; 40; 828; 804 | differences | Analyst Inference | Arithmetic correct; equivalence of adjustments and EBITDA effect assumed | Medium | Margin quality | SRC-4 page:8; SRC-7 pages 11, 12 |
| Debt on carrying value: 3.39x gross, 2.98x net | This review | 3,825; 459; 1,128 | carrying value / LTM Adjusted EBITDA | Calculated | New reference calculation; see I-08 | High | Definition drift | SRC-4 page:10 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Shutdowns delayed or slowed contract awards | No source states that awards were delayed; the sources show revenue and collections effects | Untraced | Overstates the mechanism behind revenue timing; could mislead on backlog conversion | Delete or restate as revenue and collections timing | HO-1A operating model table and key findings text; HO-2 key findings |
| Minor | Repricing lifted interest cover | Causal attribution not quantified; LTM includes repricing only from April 24, 2026 | Weak Lineage | Overstates a driver of the improvement from 3.61x to 3.93x | Restate as concurrent with lower interest paid | HO-2 strengths |
| Minor | International revenue fell mainly from joint venture deconsolidation | Management attributes decline to several causes and does not single out international | Analyst Inference | Misattributes a driver of reported revenue decline | Qualify as analyst inference | HO-1A operating model table |
| Minor | First committed maturity in April 2031 | Scheduled amortization starts September 30, 2026 | Weak Lineage | Could be read as no principal due before 2031 | Reword to no facility or term loan matures before April 2031 | HO-2 strengths |
| Minor | Underlying EBITDA did not improve (HO-1A) against underlying growth was smaller (HO-2) | Same inference stated with different strength | Analyst Inference | Inconsistent confidence on one inference | Use the weaker wording | HO-1A, HO-2 |
| Minor | Liquidity of 1,376 | HO-2 omits that 123 of cash is in consolidated joint ventures | Weak Lineage | Overstates freely available cash | Add the caveat given in HO-1 | HO-2 |
| Material | Cash-paid interest and taxes Not supplied | Printed in all four reports | Conflicting | Would block cash interest cover and tax cash analysis | Already corrected in HO-1; HO-0 stays as accepted | HO-0 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 to July 3, 2026; credit agreement, amendment, indenture, tax matters agreement and ratings are absent | Covenant and control terms cannot be tested against executed documents | Covenant headroom and payout capacity remain indicative | Obtain the documents the exhibit list references |
| Citation completeness | Ready with Remediation | Every figure carries a locator; five statements lack support (T5B.6) | Unsupported narrative can mislead on revenue and interest drivers | Low effect on figures; moderate on narrative | Correct or qualify the five statements |
| Calculation traceability | Committee-Ready | All calculations in T5B.5 re-performed and reproduce to the stated precision | Arithmetic error risk is low | Figures usable | None; keep assumption labels on the maturity schedule |
| Assumption transparency | Ready with Remediation | Maturity schedule, first lien headroom and implied fourth-quarter cash flow state assumptions | Assumptions could be read as facts | Indicative outputs must not drive covenant or refinancing conclusions | Keep the indicative label in the report |
| Markdown artifact integrity | Committee-Ready | Each handoff has the six required headings, sources with hashes, and a reader summary before the view | Low | Low | None |

Overall auditability is the lowest of the five dimensions: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Credit agreement, amendment and indenture not supplied | Executed documents with covenant levels, definitions, baskets, guarantor and collateral terms | Payout, priming and collateral capacity determine loss given default mechanics | Covenant and control sections restricted | High impact | Exhibits referenced by the 10-K and Q3 10-Q (Form 8-K of April 28, 2026) |
| CP-5-GAP-002 | Ratings and market data not supplied; Q1 release rating headline inconsistent | Agency reports | Ratings affect pricing grids and market access | No rating context | Medium impact | Agency reports |
| CP-5-GAP-003 | Current ownership not supplied | Proxy statement or beneficial ownership filings | Sponsor influence cannot be scored | Governance rows restricted | Medium impact | Part III proxy statement |
| CP-5-GAP-004 | Post-amendment maturity schedule not printed | Maturity table at July 3, 2026 | Refinancing profile is calculated under assumptions | Maturity chart is indicative | Medium impact | FY2026 annual report |
| CP-5-GAP-005 | EBITDA effect of estimate adjustments not given | Segment or contract disclosure | Underlying margin cannot be cleaned | Earnings quality remains an inference | Medium impact | Later filings |
| CP-5-GAP-006 | Pay-cycle timing not quantified | Management working capital detail | Quarterly cash flow comparisons are distorted | Cash conversion carries timing uncertainty | Medium impact | Management disclosure |
| CP-5-GAP-007 | Lease and pension balances dated October 3, 2025 | Annual report FY2026 | Claims outside debt are dated | Minor effect | Low impact | FY2026 annual report |
| CP-5-GAP-008 | Events after August 11, 2026 not in the pack | New filings | View ends at Q3 2026 | Fourth-quarter test outstanding | Medium impact | Filings after the cutoff |

#### T5.1 Module and handoff register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | HO-0, run amtm-2026-11-05-credit_snapshot-host | Source readiness for seven sources | High | Six required headings present | Accepted with one open error (I-01) | Cash-paid interest and taxes wrongly Not supplied; corrected in HO-1 |
| CP-1 | HO-1, same run | Financial base, three balance sheet dates | High | Six required headings and chart selectors present | Accepted | Figures re-performed without difference |
| CP-1A | HO-1A, same run | Business and transaction context | High | Six required headings and three selectors present | Accepted with remediation items (I-02, I-03, I-13) | Two statements need qualification |
| CP-2 | HO-2, same run | Credit synthesis | High | Six required headings and selectors present | Accepted with remediation items (I-02, I-04, I-05, I-14) | Figures identical to HO-1 |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1A, CP-2 | Shutdowns delayed or slowed awards | Untraced | Not stated in any source | Delete or restate | Narrative correction before committee use |
| Minor | CP-1A | International revenue decline attributed mainly to joint ventures | Analyst Inference | Management attribution is not specific to international | Label as inference | None on figures |
| Minor | CP-2 | Repricing helped interest cover | Weak Lineage | Not quantified | Soften | None on figures |
| Minor | CP-2 | First committed maturity in April 2031 | Weak Lineage | Omits amortization from September 30, 2026 | Reword | None on figures |
| Minor | CP-2 | Liquidity of 1,376 without joint venture cash caveat | Weak Lineage | HO-1 gives the caveat; HO-2 omits it | Add the caveat | None on figures |
| Minor | CP-0 | Cash-paid interest and taxes Not supplied | Conflicting | Printed in all four reports | Corrected in HO-1 | None downstream |

#### T5.3 Calculation and logic audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Leverage on principal debt of 3,875 | Method basis is carrying value of 3,825 with the gross difference logged; HO-1 shows both values | None; management uses principal | Keep both bases visible; on carrying value leverage is 3.39x gross and 2.98x net | None |
| Minor | CP-1, CP-2 | Adjusted EBITDA is a management measure, and trailing period spans 53 weeks | Definition differs from company EBITDA of 1,013 and from the unsupplied covenant definition | None | Keep the definition labels | None |
| Minor | CP-1 | Indicative maturity profile | Assumptions on term loan B amortization after the 125 prepayment | Current portion 54 against computed 50.91 plus other debt | Keep indicative label | None |
| Minor | CP-1 | Interest paid versus expense | Cash interest may be net of swap settlements; not stated | None | Keep note | None |
| Minor | CP-1A | Estimate adjustments versus EBITDA growth | Assumes catch-up flows to EBITDA one for one | None | Keep as inference | None |

#### T5.4 Legal and structural claims

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Financial maintenance covenant: first lien net leverage 5.00x (pre-amendment); term loan A and revolver now carry a covenant | Credit agreement and first amendment | Amended level, trigger and definition not supplied | Keep indicative label; do not state headroom as fact | Required before any covenant conclusion |
| Material | CP-1, CP-1A | Guarantor and security package: substantially all wholly owned material domestic restricted subsidiaries; first-priority liens on substantially all assets; senior notes unsecured | Credit agreement, indenture, collateral documents | Documents not supplied; excluded assets and guarantor list unknown | Obtain the documents | Required for recovery mechanics |
| Minor | CP-1A | Tax-free merger restrictions and indemnity | Tax matters agreement | Contract term and amounts not supplied | Obtain the agreement | Needed for strategic flexibility |
| Minor | CP-1A | Board nomination rights by ownership tier | Stockholders agreement | Current ownership not supplied | Obtain proxy statement | Needed for sponsor influence |

#### T5.5 Market and relative value claims

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | No market, spread or relative value claim is made; the synthesis states no peer ranking | Prices, spreads and ratings are not supplied | None for this synthesis; context market fields are blank | None | Committee must obtain market data separately |

#### T5.6 Cross-module conflicts and version issues

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1 | Cash-paid interest and taxes Not supplied (CP-0) against printed amounts (CP-1) | Earlier accepted answer cannot be edited | Treat CP-1 as controlling | Interest cover uses CP-1 |
| Minor | CP-1A, CP-2 | Underlying EBITDA did not improve against underlying growth was smaller | Same inference, two strengths | Use the weaker wording | None on figures |
| Minor | All | Context period q2-2026 against Q3 2026 evidence | Context mismatch disclosed in each handoff | Keep the period labels | None |
| Minor | CP-1A | Rating headline says upgraded to Ba3 from Ba1, which is a lower rating | Logged, not reconciled | Keep logged; no rating-based conclusion | None |
| Minor | CP-1, CP-2 | Principal debt 3,875 against carrying value 3,825 | Definition difference, both disclosed in CP-1 | Keep both | None |

#### T5.7 Markdown and artifact integrity

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Chart tables | Debt maturity table values use indicative figures with one decimal; numbers are plain | None | None |
| Minor | CP-2 | Presentation | Credit view is 139 words with the view stated first | None | None |
| Minor | All | Locators | Locators are pack page numbers, not printed page numbers; each handoff says so | None | Reviewers should open the pack page |

#### T5.8 Handoff consistency

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Sources | Lists CP-0 and CP-1 hashes correctly; both match the run record | None | None |
| Minor | CP-2 | Sources | Lists CP-0, CP-1 and CP-1A hashes correctly | None | None |
| Minor | CP-2 | Figures | Every figure matches CP-1 or CP-1A exactly (checked by comparing all numbers) | None | None |
| Material | CP-0 | Gaps | States a gap that the filings contradict | Superseded by CP-1 | CP-5 and report must use CP-1 |

#### T5.9 Issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Material | CP-0 | Conflict | Cash-paid interest and taxes recorded as Not supplied; printed at 10-K page:116, Q1 10-Q page:4, Q2 10-Q page:5, Q3 10-Q page:5 | Superseded by CP-1 | None once CP-1 is used | Resolved downstream |
| I-02 | Material | CP-1A, CP-2 | Untraced claim | Shutdowns delayed or slowed awards | Delete or restate as revenue and collections timing | Narrative correction | Open |
| I-03 | Minor | CP-1A | Analyst inference | International decline attributed to joint ventures | Label as inference | None | Open |
| I-04 | Minor | CP-2 | Weak lineage | Repricing helped interest cover | Soften | None | Open |
| I-05 | Minor | CP-2 | Weak lineage | First committed maturity in April 2031 | Reword | None | Open |
| I-06 | Material | CP-1, CP-2 | Assumption | Maturity profile rests on stated assumptions | Keep indicative label | Restricts refinancing conclusions | Open (cannot be closed from the pack) |
| I-07 | Material | CP-1, CP-2 | Missing source | Covenant level, definition and trigger after amendment not supplied | Obtain credit agreement and amendment | Restricts covenant and control conclusions | Open (cannot be closed from the pack) |
| I-08 | Minor | CP-1, CP-2 | Definition | Leverage on principal debt; carrying value basis gives 3.39x gross and 2.98x net | Keep both | None | Open |
| I-09 | Minor | CP-1, CP-2 | Omission | Pay-cycle timing: an additional pay cycle in Q1 2026 with shutdown collections timing (SRC-5 page:2; SRC-2 page:23), one less in Q2 (SRC-6 page:3), one additional in Q3 (SRC-7 page:3); net effect not quantified | Add timing caveat to cash conversion | Cash conversion carries timing uncertainty | Open |
| I-10 | Minor | All | Period | Context period q2-2026 against Q3 2026 evidence | Keep labels | None | Closed (disclosed) |
| I-11 | Minor | CP-1A | Conflict | Rating headline inconsistent | Keep logged | None | Closed (logged) |
| I-12 | Minor | CP-1A | Unexplained difference | Divestiture net proceeds 365 against purchase price 360 | Keep logged | None | Closed (logged) |
| I-13 | Minor | CP-1A, CP-2 | Inference strength | Same inference worded with different strength | Use the weaker wording | None | Open |
| I-14 | Minor | CP-2 | Omission | Liquidity of 1,376 omits that 123 of cash is held in consolidated joint ventures | Add the caveat | Modest effect on liquidity reading | Open |

## Calculations

Re-performed from the pinned sources (US$ millions as printed). Every result agrees with the upstream handoff to the stated precision.

1. Debt at July 3, 2026: 1,400 + 1,466 + 1,000 + 9 = 3,875 (SRC-4 page:10). Net debt 3,875 - 459 = 3,416. Net leverage 3,416 / 1,128 = 3.03x; gross 3,875 / 1,128 = 3.44x. Management prints 3.0x on the same inputs (SRC-7 page:10).
2. LTM Adjusted EBITDA 1,104 + 828 - 804 = 1,128 (FY2025 from SRC-1 page:157; nine-month figures from SRC-7 pages 11 and 12; 828 = 263 + 275 + 290 and = 324 + 504).
3. LTM interest paid 306 + 175 - 194 = 287; cover 1,128 / 287 = 3.93x. FY2025 cover 1,104 / 306 = 3.61x.
4. Liquidity 459 + 917 = 1,376; revolver 1,000 - 83 = 917; FY2025 850 - 84 = 766.
5. Free cash flow 235 - 22 = 213; less the receivable-sales inflow of 120 (300 - 180) gives 93.
6. Floating share (1,400 + 1,466) / 3,875 = 74%. Funded backlog share 6,240 / 48,237 = 12.9%. U.S. Government share (7,678 + 3,994) / 14,393 = 81.1%.
7. Maturity schedule by year, from the stated terms: 12.73, 50.91, 59.66, 85.91, 94.66, 2,562.13 and 1,000, total 3,866 = 1,400 + 1,466 + 1,000. Share in the last two years (2,562.13 + 1,000) / 3,866 = 92%. Next twelve months of amortization 4 x 8.75 + 4 x 3.9775 = 50.91 against a current portion of debt of 54 (SRC-4 page:2).
8. Indicative first lien net leverage (1,400 + 1,466 - 459) / 1,128 = 2,407 / 1,128 = 2.13x.
9. Guidance-implied fourth quarter: free cash flow 525 - 213 = 312 and 575 - 213 = 362; prior-year fourth quarter 516 - 255 = 261.
10. New reference calculation, carrying-value basis (issue I-08): gross 3,825 / 1,128 = 3.39x; net (3,825 - 459) = 3,366; 3,366 / 1,128 = 2.98x. FY2025 carrying basis: 3,943 / 1,104 = 3.57x gross and (3,943 - 437) / 1,104 = 3.18x net.
11. Pay-cycle effect: Not calculable. The sources describe direction by quarter (additional in Q1 and Q3 2026, one fewer in Q2 2026 against the prior-year quarters) and give no amounts.
12. Number identity check across handoffs: every number in the synthesis handoff was compared with the financial and business handoffs; the only unmatched tokens were fragments of hashes.

## Gaps

Module status is Ready with Limitations. Committee use is permitted for the leverage, liquidity, cash flow and customer-concentration conclusions, and restricted for covenant headroom, the maturity profile, creditor-control and sponsor-behaviour conclusions until the executed documents are supplied. No finding is Critical; four are Material (I-01, I-02, I-06 and I-07), of which I-01 is resolved downstream and I-06 and I-07 cannot be closed from the pack.

The gaps are listed in the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-008). Confidence in the trace is Medium: figures are strong, narrative has five defects, and the legal layer is untraceable without the loan documents. No numeric confidence score is assigned because this transport has no scoring script; the band is a judgment.

## Next module

No further module is selected for this run. The report assembler should (1) use the financial base for all figures and treat the source-readiness gap on cash-paid interest as superseded, (2) remove or restate the claim that shutdowns delayed awards, (3) keep the indicative labels on the maturity profile, first lien headroom and implied fourth-quarter cash flow, (4) carry the liquidity caveat on joint venture cash and the pay-cycle timing caveat, and (5) not present covenant or sponsor-behaviour conclusions as established.
