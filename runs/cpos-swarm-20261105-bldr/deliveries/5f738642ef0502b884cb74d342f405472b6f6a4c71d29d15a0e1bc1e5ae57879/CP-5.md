## Request

Evidence trace validation and research-integrity review (CP-5, with the absorbed CP-5A grade) of the accepted handoffs for Builders FirstSource, Inc. (issuer id bldr), as of 2026-11-05, pathway credit_snapshot, current period Q3 2026 against FY2025, in USD. Scope is the minimum module set: the source readiness review (CP-0), the financial extraction (CP-1), the business and transaction context (CP-1A) and the fundamental credit synthesis (CP-2), traced to the seven pinned sources, with a Top 5 traceability scope. This review governs provenance only: it changes no credit conclusion, assigns no rating and silently repairs nothing.

## Sources

### Issuer sources traced

Locators are written `label page:N`, where a page is the source chunk shown as `page:N`, not a printed page. Each pinned file was reopened for this review.

| Source name (exact) | Label | sha256 |
| --- | --- | --- |
| 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | 9bd0da5e45c4f2248ca4db64d57fc684925bf29516d1562226f10d757c9e4459 |
| 10-Q_2026-03-31_bldr-20260331.htm.jsonl | Q1 | 363b4992626af02adfa3367e60743e610fb97e980272b73e97926fb679323cd7 |
| 10-Q_2026-06-30_bldr-20260630.htm.jsonl | Q2 | 02ee03cdc0624d85cbcbf7a710722ddc9ac45fd9b91dc10f08e351fa9e01c57b |
| 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | eb3b1081f3726d9edfb8731ffaa8e1149a0312dcd5760fffdc5c5e326cc6f78d |
| EX-99.1_2026-04-30_bldr-ex99_1.htm.jsonl | R1 | 57b8b8fc9c442c401865b306d40dc3f4e8bf2c98e87e713da2af276f2efa22fe |
| EX-99.1_2026-07-30_bldr-ex99_1.htm.jsonl | R2 | d9ac22d1edd973fb8f940548ad5207a292c8d1318f8581d90b82000eb7ba1b98 |
| EX-99.1_2026-10-29_bldr-ex99_1.htm.jsonl | R3 | e8822f68613ed2eb08d6f6868127023f13ee8e8fe4e83662a7f4abe50d874bbc |

Other pinned input: context, sha256 26c088bea94d5b4a50b7398f335a28e56083f68ba3e62b9362de602502e2ae7e (settings only; blank entries stay Not supplied, never zero).

### Supplied handoffs

Upstream re-anchor: each handoff below is for Builders FirstSource, Inc., run bldr-2026-11-05-credit_snapshot-host, as-of 2026-11-05, current period Q3 2026 and prior period FY2025; none mismatches this run.

| Module | sha256 | Status found |
| --- | --- | --- |
| CP-0 | 823065622ac29ad63f87b66c10b3d798ab9303f8c970b85b92f36bc8eed37638 | Accepted; READY_WITH_LIMITATIONS for each consumer |
| CP-1 | 936bbb99fc4046541fbb62dacc6ef6d0c679a81360eaf50d71b4f0d7a89c15a8 | Accepted; second attempt; figures in USD thousands or USD millions as labelled |
| CP-1A | 2f81a875ac526d890607471397c083e1d1228c0083ca8bf0bfc74361c237ccb9 | Accepted; READY_WITH_LIMITATIONS for the synthesis and for this review |
| CP-2 | 67caba116dddcaf3e6bad59e4f6506b861a1bc02cce93e4e62d09604ca44169f | Accepted; upstream-only by design, quotes no source text |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Financial and business conclusions trace to filed sources with located quotes and shown calculations, supporting a fundamental credit discussion after minor wording fixes. Legal, guarantee and covenant claims rest on summaries and are not committee ready. | Medium | The credit agreement, indentures and guarantor list are not supplied, and EBITDA is built from reported lines, so structural and covenant claims cannot be traced to primary documents. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of the 5 top credit drivers, 2 are directly sourced, 2 are calculated and 1 is an analyst inference; none is untraced. | Core leverage, liquidity and cyclicality conclusions can be relied on within the stated limits. | High |
| Every figure reviewed recomputed from its cited inputs; 9 issues are logged, 0 critical. | No error changes the credit view; two wording fixes are needed. | High |
| Covenant, collateral, ranking and guarantee statements rest on filing summaries only. | Structural protection and creditor control cannot be confirmed; do not use for recovery or security choices. | Medium |
| Reported EBITDA is built and management Adjusted EBITDA is higher; both are labelled. | Leverage comparisons must name the basis; covenant EBITDA may differ. | Medium |
| Two footprint facts differ between sources and stay unresolved. | Immaterial to credit metrics; quote them with their source. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting or insufficient-information items. The most important provenance gap is the absence of the credit agreement, the indentures and the guarantor list, which matters because collateral, guarantee, ranking and covenant-basket statements then rest on issuer summaries, and it implies that structural, recovery and security-selection use is not committee ready while the fundamental credit view is usable with its stated limitations. Committee status: Draft Only. Confidence band: Medium; no numeric score is stated because the scoring script is outside this run.

### Source register (T5B.1)

Module status: Ready with Limitations. Traceability scope: Top 5. Entity key: issuer_id bldr available. Missing required inputs: no stand-alone evidence-trace sections exist in the handoffs (they use the six-heading Markdown form), so lineage was read from each handoff's Sources, Findings and Calculations sections.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| K10 | 10-K_2025-12-31_bldr-20251231.htm.jsonl | High: audited annual report | FY2025 (year ended December 31, 2025) | Builders FirstSource, Inc. and subsidiaries, consolidated | Statements, debt note, leases, maturities, covenant description, business description | Legal documents only listed as exhibits; table text flattened | Debt, FY2025 base, business facts |
| Q1 | 10-Q_2026-03-31_bldr-20260331.htm.jsonl | High: unaudited filing | Q1 2026 | Same consolidated perimeter | Q1 statements, debt table, availability | Three-division segment basis | Quarterly liquidity and LTM inputs |
| Q2 | 10-Q_2026-06-30_bldr-20260630.htm.jsonl | High: unaudited filing | Q2 and six months 2026 | Same consolidated perimeter | Six-month statements, debt table, availability, segment realignment | Two-division segment basis | Quarterly liquidity and LTM inputs |
| Q3 | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | High: unaudited filing | Q3 and nine months 2026 | Same consolidated perimeter | Statements, debt, availability, MD&A, acquisitions, repurchases | No maturity table; no subsequent-events note found | Current-period facts, controlling source |
| R1 | EX-99.1_2026-04-30_bldr-ex99_1.htm.jsonl | Medium: management release | Q1 2026 | Same | Management narrative and non-GAAP reconciliations | Management attributed | Context only |
| R2 | EX-99.1_2026-07-30_bldr-ex99_1.htm.jsonl | Medium: management release | Q2 2026 | Same | Management narrative and non-GAAP reconciliations | Management attributed | Context only |
| R3 | EX-99.1_2026-10-29_bldr-ex99_1.htm.jsonl | Medium: management release | Q3 2026 and LTM | Same | Adjusted EBITDA, net debt ratio, guidance, free cash flow definition | Management attributed; add-backs not itemised | Management-basis leverage, guidance |

### Top 5 material credit drivers (T5B.2)

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage and cover erosion | CP-1, CP-2 | Reported EBITDA built from income from operations and depreciation and amortization; debt principal 4,658.904 million | Debt is largely non-amortizing notes, so leverage rises as EBITDA falls | Sets leverage tolerance and default sensitivity | Q3 page:2, Q3 page:3, Q3 page:13, K10 page:71, K10 page:72 | EBITDA is built, not printed; not the covenant definition |
| 2 | Liquidity and covenant trigger | CP-1, CP-2 | Net excess availability 1,459.1 million; minimum 173.2 million; cash 55.012 million | Liquidity absorbs a downturn before the springing test applies | Near-term default risk is low | Q3 page:27, Q3 page:2 | Qualified cash overlaps the borrowing base by up to 21.3 million |
| 3 | Housing-cycle exposure and margin compression | CP-1A, CP-2 | Net sales down and gross margin 27.8% from 30.4% in Q3 2026 on lower housing starts | Fixed costs magnify volume and price declines | Main driver of default risk | Q3 page:24, K10 page:59 | End-market mix not supplied |
| 4 | Maturity profile concentrated from 2030 | CP-1, CP-2 | Notes due 2030, 2032, 2034 and 2035; revolver due May 20, 2030 | No near-term refinancing; 2030 holds a note and the revolver | Refinancing monitoring date | K10 page:93, Q3 page:13, Q3 page:9 | Maturities derived from dates; other finance obligations unscheduled |
| 5 | Capital allocation against deleveraging | CP-1A, CP-2 | Repurchases of 303.519 million in nine months 2026 against free cash flow of 150.875 million; acquisitions of about 129.3 million | Cash returned to equity while leverage rose slows debt reduction | Governance and leverage tolerance | Q3 page:3, Q3 page:5, Q3 page:9 | The inference that returns compete with deleveraging is analyst judgement |

### Traceability map (T5B.3)

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 5.15x total and 5.09x net on a reported basis | CP-1 | Debt principal and statement lines recomputed from Q3 page:13, Q3 page:2, K10 page:71 | Yes | High | Calculated | Verified by recomputation | Medium | Committee-Ready with the definition stated |
| EBITDA to cash interest 3.18x | CP-1 | Cash interest 260,515 and 230,109 and 205,872 thousand on K10 page:73 and Q3 page:4 | Yes | High | Calculated | Verified by recomputation | Medium | Committee-Ready with the definition stated |
| Liquidity 1,514.1 million against a trigger of 173.2 million | CP-1, CP-2 | Q3 page:27 availability table and covenant sentence | Yes | High | Directly Sourced | Verified | High | Committee-Ready |
| Gross margin and net sales decline tied to housing starts | CP-1A, CP-2 | Q3 page:24 | Yes | High | Directly Sourced | Verified | High | Committee-Ready |
| First maturity 2030, with 747.0 million | CP-1, CP-2 | K10 page:93 maturities, Q3 page:13 amounts, Q3 page:9 revolver date | Yes | High | Calculated | Derived from dates | Medium | Committee-Ready with the derived label |
| Repurchases compete with deleveraging | CP-1, CP-2 | Q3 page:28 states both cash uses together | Yes | High | Analyst Inference | Inference, labelled | Medium | Committee-Ready as labelled inference |

### Source lineage register (T5B.4)

Each row's checked value, shown in backticks, was found on the cited page. Source Path is the pinned file under the run's source-text folder.

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt principal at September 30, 2026 | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:13, Note 8 | CP-1 debt table | Sourced | High | `4,658,904` |
| Debt principal at December 31, 2025 | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:91, Note 8 | CP-1 leverage chart | Sourced | High | `4,485,046` |
| Net excess availability at September 30, 2026 | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:27, MD&A liquidity | CP-1 liquidity chart | Sourced | High | `1,459.1` |
| Minimum excess availability for the fixed charge test | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:27, MD&A liquidity | CP-1 covenants | Sourced | High | `$173.2 million` |
| Cash at September 30, 2026 | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:2, balance sheet | CP-1 liquidity chart | Sourced | High | `55,012` |
| FY2025 income from operations | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:71, statement of operations | CP-1 financials table | Sourced | High | `786,276` |
| FY2025 depreciation and amortization | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:72, cash flow statement | CP-1 financials table | Sourced | High | `591,432` |
| Nine-month 2026 income from operations | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:2, statement of operations | CP-1 financials table | Sourced | High | `244,113` |
| Nine-month 2025 income from operations | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:2, statement of operations | CP-1 financials table | Sourced | High | `724,496` |
| Nine-month 2026 depreciation and amortization | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:3, cash flow statement | CP-1 financials table | Sourced | High | `447,167` |
| Cash paid for interest, FY2025 | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:73, supplemental cash flow | CP-1 interest cover chart | Sourced | High | `260,515` |
| Cash paid for interest, nine months 2026 | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:4, supplemental cash flow | CP-1 interest cover chart | Sourced | High | `230,109` |
| Management Adjusted EBITDA, LTM | source-text | EX-99.1_2026-10-29_bldr-ex99_1.htm.jsonl | R3 | R3 page:13, reconciliation | CP-1 financials table | Sourced, management | Medium | `1,129.1` |
| Net debt to LTM Adjusted EBITDA stated by management | source-text | EX-99.1_2026-10-29_bldr-ex99_1.htm.jsonl | R3 | R3 page:3 | CP-1 leverage chart basis | Sourced, management | Medium | `ratio of 4.1x` |
| Notes mature 2030, 2032, 2034 and 2035 | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:93, senior unsecured notes table | CP-1 maturities | Sourced | High | `5.00% notes due March 2030` |
| Revolver due May 20, 2030 | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:9, Note 2 | CP-1 maturities | Sourced | High | `due May 20, 2030` |
| Top ten customers 14% of net sales | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:6, Item 1 | CP-1A operating model | Sourced | High | `top 10 customers accounted for 14% of net sales` |
| Gross margin 27.8% from 30.4% | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:24, MD&A | CP-1A operating model | Sourced | High | `27.8% in the third quarter of 2026 from 30.4%` |
| Acquisitions of 1.1 billion in 2025 | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:60, MD&A | CP-1A transactions | Sourced | High | `$1.1 billion purchase price` |
| 2026 acquisitions of about 129.3 million | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:9, Note 2 | CP-1A transactions | Sourced | High | `$129.3 million` |
| First-quarter 2026 repurchase of 302.9 million | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:5, equity statement footnote | CP-1 cash uses | Sourced | High | `$302.9 million` |
| Covenant is a springing fixed charge test of 1.00 to 1.00 | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:93, Note 8 | CP-1 covenants | Sourced, summary of an unsupplied document | Medium | `of 1.00 to 1.00 if our excess availability falls below` |
| Guarantors are unnamed Debt Guarantors | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:93, Note 8 | CP-0, CP-1, CP-1A entity roles | Sourced, incomplete | Medium | `Debt Guarantors` |
| Footprint: 94 of the top 100 market areas | source-text | 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | K10 page:5, Item 1 | CP-1A conflicts | Conflicting | High | `94 of the top 100` |
| Footprint: 91 of the top 100 market areas | source-text | EX-99.1_2026-10-29_bldr-ex99_1.htm.jsonl | R3 | R3 page:5, About section | CP-1A conflicts | Conflicting | Medium | `91 of the top 100` |
| Construction defect claims, loss not estimable | source-text | 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | Q3 page:17, Note 11 | CP-1 non-debt claims | Sourced | High | `known and threatened construction defect legal claims` |

### Calculation and assumption register (T5B.5)

All calculations were recomputed independently from the cited inputs; every result matched the upstream figure.

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reported EBITDA FY2025 | CP-1 C1; CP-2 | Income from operations 786,276; D&A 591,432 (USD thousands) | Numerator: sum; period FY2025; no normalization; result 1,377,708 | Calculated | Verified | Medium | PD, leverage | K10 page:71, K10 page:72 |
| Reported EBITDA LTM Q3 2026 | CP-1 C2 to C4; CP-2 | FY2025 plus nine months 2026 less nine months 2025 | 1,377,708 + 691,280 - 1,164,586 = 904,402; period LTM to September 30, 2026 | Calculated | Verified | Medium | PD, leverage | K10 page:71, Q3 page:2, Q3 page:3 |
| Total debt to EBITDA | CP-1 C5, C6; CP-2 | Debt principal 4,485,046 and 4,658,904 | Debt / EBITDA = 3.26x for FY2025 and 5.15x LTM; principal basis including other finance obligations and finance leases, excluding operating leases | Calculated | Verified | Medium | PD, refinancing | K10 page:91, Q3 page:13 |
| Net debt to EBITDA | CP-1 C5, C6; CP-2 | Debt less cash 181,753 and 55,012 | 3.12x for FY2025 and 5.09x LTM | Calculated | Verified | Medium | PD | K10 page:72, Q3 page:2 |
| EBITDA to cash interest | CP-1 C7; CP-2 | Cash interest 260,515; LTM 284,752 | 5.29x for FY2025 and 3.18x LTM | Calculated | Verified | Medium | Debt service | K10 page:73, Q3 page:4 |
| Free cash flow nine months 2026 | CP-1 C11; CP-2 | Operating cash flow 302,031; purchases 157,430; proceeds 6,274 | 302,031 - 157,430 + 6,274 = 150,875 (release prints 150.8 million from rounded inputs) | Calculated | Verified | High | Liquidity | Q3 page:3, R3 page:14 |
| Covenant headroom | CP-1 C15 | Availability 1,459.1; minimum 173.2 | 1,459.1 - 173.2 = 1,285.9 million | Calculated | Verified | Medium | Liquidity | Q3 page:27 |
| 2030 maturities | CP-1 C10; CP-2 | 5.00% notes 550.0; revolver drawn 197.0 | Sum = 747.0 million; derived from maturity dates | Calculated | Verified | Medium | Refinancing | K10 page:93, Q3 page:13 |
| Reported-to-management EBITDA bridge | CP-1 C9; CP-2 | 904.402 plus add-backs 149.0, 43.1, 6.0, 26.7 | Sum 1,129.2 against 1,129.1 printed; 0.1 rounding | Calculated | Verified | Medium | Earnings quality | R3 page:13 |
| FY2025 Adjusted EBITDA | CP-1 C8 | 1,129.1 less 854.2 plus 1,308.9 | 1,583.8 million; derived from rounded management figures | Calculated | Verified with rounding limit | Low | Earnings quality | R3 page:13 |
| Repurchases less free cash flow | CP-2 C3 | 303.519 less 150.875 | 152.644 million | Calculated | Verified | High | Capital allocation | Q3 page:3 |
| Definition drift between modules | CP-1, CP-2 | Reported EBITDA versus management Adjusted EBITDA | No drift: each figure is labelled by basis; no covenant EBITDA is available | Assumption-Based (basis choice) | Flagged, not a defect | Medium | Leverage comparisons | CP-1 covenants section |

### Missing-citation and weak-lineage flags (T5B.6)

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant, collateral and guarantee statements | Rest on the 10-K and 10-Q summaries; the executed documents are not supplied | Insufficient Information | Without primary documents, covenant baskets, guarantor perimeter and ranking cannot be confirmed, which limits creditor-control and loss-given-default reasoning | Obtain credit agreement, indentures and subsidiary list | CP-0, CP-1, CP-1A, CP-2 structural statements |
| Material | Business-risk sensitivity | End-market sales mix and beneficial ownership not supplied | Insufficient Information | Single-family sensitivity and control cannot be sized | Obtain mix and proxy statement | CP-1A, CP-2 |
| Minor | Net interest increase mechanism | Upstream wording links the increase to the 2035 notes and the revolver draw; the filing attributes the quarter's increase to other finance obligations and higher average debt balances | Analyst Inference | Cause of rising interest cost affects the debt-service outlook | Reword as analyst inference and cite the filing wording | CP-1 interpretation, CP-2 key findings |
| Minor | No scheduled principal payment before 2030 | Stated for the debt as a whole in one CP-2 sentence; true for notes and revolver, not for other finance obligations and finance leases | Weak Lineage | Overstates the absence of amortization by a small amount | Qualify as notes and revolver | CP-2 key findings |
| Minor | FY2025 Adjusted EBITDA | Derived from rounded management figures | Calculated | Precision of about 0.1 million | Keep derived label | CP-1 financials table |

### Auditability assessment (T5B.7)

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven sources cover FY2025 and the three 2026 quarters; legal documents, proxy statement and presentations are absent | Primary documents absent for structure and ownership | Structure and control claims stay provisional | Obtain the documents listed in the gaps ledger |
| Citation completeness | Committee-Ready | Every upstream quote in CP-0, CP-1 and CP-1A was matched to its page by search; every table value cited to a page was found there; CP-2 quotes none by design | Risk of misquotation is low | Figures can be relied on | None |
| Calculation traceability | Committee-Ready | Each calculation shows inputs and result and recomputed identically | Low risk of arithmetic error | Ratios can be relied on at the stated definition | None |
| Assumption transparency | Ready with Remediation | EBITDA is built, maturities and twelve-month periods are derived, all labelled | Definition choice drives ratio levels | Ratios are not covenant ratios | State definition in committee material |
| Markdown and export integrity | Committee-Ready | Each handoff has the six headings once in order, a Reader summary and the required view heading | Structural error unlikely | Handoffs can be consumed downstream | None |

Overall auditability, the lowest of the five: Ready with Remediation.

### Gaps ledger (T5B.8)

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Credit agreement, indentures, intercreditor and collateral agreements not supplied | Executed documents | Covenant baskets, restricted-payment capacity and ranking drive creditor control and loss given default | Structural and covenant statements in CP-1, CP-1A, CP-2 | Medium impact: caps confidence at Medium | Exhibits 4.1 to 4.6 and 10.1 to 10.13 of the 10-K |
| CP-5-GAP-002 | Guarantor list not supplied | Subsidiaries of the Registrant exhibit | Guarantor perimeter determines structural subordination | Entity roles and ranking | Medium impact | 10-K Exhibit 21.1 |
| CP-5-GAP-003 | Beneficial ownership and end-market sales mix not supplied | Proxy statement; investor presentation | Control and single-family sensitivity cannot be sized | Governance and business-risk rows | Medium impact | Proxy statement; presentation |
| CP-5-GAP-004 | EBITDA not printed; fixed charge coverage ratio not reported | Covenant EBITDA definition | Leverage is not comparable to covenant tests | Leverage and covenant rows | Medium impact | Credit agreement definitions |
| CP-5-GAP-005 | No maturity schedule at September 30, 2026; no stand-alone fourth-quarter 2025 report | Quarter-end maturity table; Q4 2025 release | Maturity chart and trends are derived | Maturity and trend rows | Low impact | Next 10-K note; Q4 2025 release |
| CP-5-GAP-006 | Footprint conflicts unresolved | Source reconciling market-area ranking and location count | Facts need source labels | Business description | Low impact | Later filings |
| CP-5-GAP-007 | No subsequent-events note and no current reports after the Q3 filing in the pack | 8-K filings after October 29, 2026 | Events up to the cutoff cannot be ruled out | All modules | Low impact | EDGAR current reports |

### Module register (T5.1)

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | CP-0 handoff, run bldr-2026-11-05-credit_snapshot-host | Source readiness for 7 sources, minimum modules | High for filings; Medium for releases | Six headings once in order; reader summary and readiness view present | Accepted by CP-OS checks | Fully traced; no defects found |
| CP-1 | CP-1 handoff, run bldr-2026-11-05-credit_snapshot-host | Statements, debt, liquidity, covenant, derived ratios | High | Six headings, chart tables and financial table present | Accepted | Two wording issues and the definition limits |
| CP-1A | CP-1A handoff, run bldr-2026-11-05-credit_snapshot-host | Business, ownership, transactions, governance, conflicts | High for filings; Medium for releases | Six headings, two selector tables and prose selector present | Accepted | Gaps on ownership, mix and legal terms |
| CP-2 | CP-2 handoff, run bldr-2026-11-05-credit_snapshot-host | Credit synthesis from upstream only | Derived from CP-1 and CP-1A | Six headings, prose selectors present | Accepted | One wording issue; one inference to relabel |

### Citation and evidence support audit (T5.2)

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Interpretation, coverage: cost rose because of the 2035 notes and revolver draw | Partly supported | The filing says the Q3 increase came primarily from other finance obligations and higher average debt balances; the notes link is inference | Label as analyst inference and cite the filing sentence | None to clearance |
| Minor | CP-2 | Key findings: interest cost raised by the 2035 notes and the revolver draw | Partly supported | Same as above | Same fix | None to clearance |
| Minor | CP-2 | Key findings: no scheduled principal payment before 2030 for the debt | Partly supported | Other finance obligations have scheduled payments | Qualify as notes and revolver | None to clearance |
| Material | CP-1, CP-1A, CP-2 | Covenant, collateral, guarantee statements | Supported by summary only | Primary documents absent | Obtain documents | Restricts structural use |
| Minor | CP-1A | Sector label from the run context | Supported as a label | Context is not issuer evidence; tagged accordingly | None | None |

### Math, logic and definition audit (T5.3)

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Reported EBITDA is built from income from operations plus depreciation and amortization | Not the covenant or management definition; stock compensation and other items are not added back | Management Adjusted EBITDA differs by 224.7 million; both labelled | Keep basis label with every ratio | Restricts covenant comparisons |
| Minor | CP-1 | Twelve-month periods and maturities are derived | Derived from comparative columns and maturity dates | None | Keep derived label | None |
| Minor | CP-1 | Liquidity adds cash to availability | Qualified cash is part of the borrowing base | None; disclosed with 21.3 million at September 30, 2026 | None | None |
| Minor | CP-1 | Free cash flow 150.875 million against the release's 150.8 million | Rounded inputs in the release | Filing inputs control | None | None |
| Minor | CP-1 | FY2025 Adjusted EBITDA from rounded figures | Precision limit | None | Keep derived label | None |

### Legal and structural claim audit (T5.4)

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Revolver is secured first on revolving collateral and second on notes collateral; notes are senior unsecured | Credit agreement; indentures; intercreditor agreement | Summary text only | Obtain executed documents | Yes: legal review before structural reliance |
| Material | CP-1 | One springing fixed charge covenant at 1.00 to 1.00 below a minimum availability | Credit agreement definitions | Definitions and baskets not supplied | Obtain credit agreement | Yes |
| Material | CP-0, CP-1, CP-1A | Debt Guarantors guarantee the revolver and notes | Subsidiary list; supplemental indentures | Guarantors unnamed | Obtain list | Yes |
| Minor | CP-1A | No creditor-adverse action documented | Current reports; indenture amendments | Absence in the pack is not proof of absence; marked Insufficient Information | None beyond the gap | Yes, for confirmation |

### Relative-value and market claim audit (T5.5)

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | No market, spread, price, rating or peer claim is made; fair values of notes are reported in CP-1 only as filing facts | Ratings, quotes, valuation and peers are blank in the context | None for the modules reviewed | None | No relative-value use is possible or claimed |

### Cross-module consistency and version control (T5.6)

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Footprint: 94 of the top 100 market areas (10-K) versus 91 (Q3 release), and 585 versus 575 locations | Different source dates; logged, not reconciled | Quote with source | None on credit metrics |
| Minor | CP-1, CP-2 | Management 4.1x leverage versus built 5.15x and 5.09x | Different definitions, both labelled; consistent across modules | Name the basis | Avoid mixing bases |
| None | CP-0, CP-1, CP-1A, CP-2 | All reviewed numbers in CP-2 resolve to CP-1 or CP-1A figures or to its own three shown calculations; CP-1A figures resolve to the cited sources | Same run, same as-of date and periods | None | Consistent |

### Duplication, materiality and committee-readiness audit (T5.7)

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Duplication | Leverage and cover figures appear in the reader summary, credit view, key findings and risk table; consistent and intentional | None | None |
| Minor | CP-1 | Materiality | The financial table is long; it carries the full record and the committee reads the summary tables | None | None |
| Material | All | Committee readiness | Fundamental view usable; structure, covenant and recovery use not supported | Obtain legal documents | Draft Only |

### Handoff and export integrity audit (T5.8)

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Evidence Trace and Source Registry headings | The Markdown form uses six headings, so lineage is in Sources, Findings and Calculations rather than separate headings | None under the Markdown transport | None |
| None | All | Hashes, source names and as-of date | Source names and sha256 values match the pinned inputs; as-of date 2026-11-05 stated in each Request | None | None |

### Consolidated issue log (T5.9)

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-1 | Material | CP-1, CP-1A, CP-2 | Legal and structural support | Covenant, collateral, ranking and guarantee statements rest on summaries | Obtain executed documents | Restricts structural use | Open |
| I-2 | Material | CP-1, CP-2 | Definition | EBITDA is built and is not the covenant or management definition | Label basis with each ratio | Restricts covenant comparison | Open |
| I-3 | Material | CP-1A, CP-2 | Evidence gap | End-market mix and beneficial ownership not supplied | Obtain mix and proxy | Limits business-risk sizing | Open |
| I-4 | Minor | CP-1, CP-2 | Evidence support | Interest-cost mechanism goes beyond the filing's wording | Relabel as inference | None | Open |
| I-5 | Minor | CP-2 | Evidence support | No scheduled principal payment before 2030 applies to notes and revolver only | Qualify | None | Open |
| I-6 | Minor | CP-1 | Derived data | Twelve-month periods, maturities and FY2025 Adjusted EBITDA are derived | Keep label | None | Open |
| I-7 | Minor | CP-1 | Disclosure | Qualified cash overlaps cash and borrowing base in liquidity | Keep disclosure | None | Open |
| I-8 | Minor | CP-1A | Conflict | Footprint facts differ by source | Quote with source | None | Open |
| I-9 | Minor | All | Coverage | No current reports after the Q3 filing in the pack | Obtain 8-K filings | None | Open |

Counts: 9 issues, 0 Critical, 3 Material, 6 Minor.

### Remediation priority map

| Priority | Issue IDs | Action | Owner | Effect on clearance |
| --- | --- | --- | --- | --- |
| 1 | I-1 | Obtain the credit agreement, indentures and guarantor list | Source retrieval | Lifts the restriction on structural and covenant use |
| 2 | I-2 | Add the basis label to every ratio in committee material and test the add-back bridge | Analyst | Removes comparison risk |
| 3 | I-3 | Obtain the proxy statement and the investor presentation | Source retrieval | Allows ownership and mix assessment |
| 4 | I-4, I-5 | Edit the two wording points in a later run; accepted handoffs cannot be replaced | Analyst | Wording only |
| 5 | I-6 to I-9 | Keep labels; refresh when the next filing arrives | Analyst | None |

### Clearance decision

Committee status: Draft Only. The fundamental credit view in CP-2 is traceable and may be discussed with the limitations above. Structural, covenant, recovery and security-selection conclusions are not cleared, because they rest on summaries of unsupplied legal documents. QA status: Restricted for structural use only; no Critical issue is open. This review states no numeric confidence score, because the scoring script is outside this run, and does not alter any upstream credit conclusion.

## Calculations

No new financial calculation is made. The review recomputed the upstream figures from the cited inputs and found them equal:

| Check | Inputs | Result |
| --- | --- | --- |
| Reported EBITDA FY2025 and LTM | 786,276 + 591,432; (786,276 + 244,113 - 724,496) + (591,432 + 447,167 - 440,090), USD thousands | 1,377,708 and 904,402 |
| Total and net debt to EBITDA | 4,485,046 and 4,658,904 principal; cash 181,753 and 55,012 | 3.26x and 5.15x total; 3.12x and 5.09x net |
| EBITDA to cash interest | 1,377,708 / 260,515; 904,402 / 284,752 | 5.29x and 3.18x |
| Covenant headroom and liquidity | 1,459.1 - 173.2; 55.012 + 1,459.1, USD millions | 1,285.9 and 1,514.1 |
| Repurchases less free cash flow | 303.519 - 150.875, USD millions | 152.644 |
| Bridge to management EBITDA | 904.402 + 149.0 + 43.1 + 6.0 + 26.7, USD millions | 1,129.2 against 1,129.1 printed |
| Debt composition | 197.0 + 4,300.0 + 161.174 + 0.730, USD millions | 4,658.904 |

## Gaps

The provenance gaps are in the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-007). In summary: legal documents, guarantor list, beneficial ownership, end-market mix, covenant EBITDA, a quarter-end maturity schedule and current reports after the Q3 filing are not in the pack. None is estimated or filled here. Upstream handoffs cannot be edited, so the two wording issues (I-4, I-5) are corrected in this review only, and a later run should restate them.

## Next module

This is the last module in the minimum set. The run can publish its report. A reader of the report should keep the limitations above with the leverage and cover figures, and should not use the material for structural, covenant, recovery or security-selection decisions until the executed legal documents and the guarantor list are obtained.
