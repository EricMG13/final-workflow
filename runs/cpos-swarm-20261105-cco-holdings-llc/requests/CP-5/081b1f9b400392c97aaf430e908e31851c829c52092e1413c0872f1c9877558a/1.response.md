# CP-5 — Evidence trace and research integrity QA: CCO HOLDINGS LLC (cco-holdings-llc)

## Request

CCO HOLDINGS LLC (issuer id `cco-holdings-llc`), as of 2026-11-05, pathway `credit_snapshot`. Scope: trace the five most material credit drivers of the earlier handoffs (CP-0, CP-1, CP-1A, CP-2) to the seven pinned filings and releases, recompute every derived figure, re-open the cited pages, and grade the research for committee use. Run `cco-holdings-llc-2026-11-05-credit_snapshot-host`; a host session, no provider call.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_ccoh-20251231.htm.jsonl | 98fc08971e7b602f253b4465dc2493c7d1fd2140d7f51b96e967ed5fb3218118 | Audited FY2025; debt table, Note 9, Item 7A, covenants, commitments |
| 10-Q_2025-09-30_ccoh-20250930.htm.jsonl | bf1745dd3dbecf91195f9fef9fea0cafc9d8a639b8157c8bb3d02dd7240529a1 | September 30, 2025 comparatives and LTM inputs |
| 10-Q_2026-03-31_ccoh-20260331.htm.jsonl | 213317fa77d5c45445d49d044bc961ab9dfa41083289474b65a9c5985c9bbe1b | March 31, 2026 comparatives, redemptions, availability |
| 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | 9af8d8232114d58e6ac96035eb67adc4aa9622876079128a14eacfcc389f347e | Latest statements, debt classes, MD&A cost and revenue drivers, guarantor text |
| EX-99.1_2026-01-30_chtrex991earningsrelease12.htm.jsonl | cb5b5ac26ab78f0a85b295e8b2969a94081a4aecc513efb234aeefb51019e762 | Parent-level release; January 2026 issuance confirmation |
| EX-99.1_2026-04-24_chtrex991earningsrelease33.htm.jsonl | 483c56fedf60126a16d804e1d36760024be2164b76b1c1509864a6a063bd22be | Parent-level release; not used for figures |
| EX-99.1_2026-07-24_chtrex991earningsrelease63.htm.jsonl | 07d1723b22b814c108cba78554e38a4e4a76d8f38c9cdfecbd3804011635822c | Parent-level release; repurchase cash cost and perimeter contrast |
| context | 1a68c05f8e4415af1307ec03597fe0b094afc35e94c83b63b62cbe99d897f95e | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 4b95775bd75ac91b4fbe8df3dddfba01cd62f5117bd68b1e969812d6f8d7022a | Audited: source readiness |
| CP-1 | ff0983c08cacf687da932db43c595db40bb04809c1727a1f0dd3c0f49ce24118 | Audited: financial base |
| CP-1A | 3048375e165e0ded201371434ad4c76f341e1547488630bb18fd2b88082c4ed7 | Audited: business and transaction context |
| CP-2 | 1b0ab50a201a948d815229106b0577d3717ce480f7a1e82d06bb66d47bee7d09 | Audited: credit synthesis |

Locators are `page:N` of the pinned `.jsonl` text of each source. Consistency with upstream: this answer re-anchors on all four handoffs, which share run `cco-holdings-llc-2026-11-05-credit_snapshot-host`, issuer, as-of date and period labels (FY2024, FY2025, Q2 2026, 6M 2026, LTM Q2 2026). It finds one statement in CP-1 and CP-2 that must be corrected by reading this answer (CP5-001) and three minor wording points (CP5-002 to CP5-004); the earlier handoffs cannot be edited. Every other figure recomputed here matches.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The research traces to the filings and its arithmetic recomputes, with one cause-of-decline statement to correct and three minor wording points. Committee use is restricted until the Cox financing and perimeter are supplied. | Low | The Cox agreements, executed debt documents, covenant ratios after December 31, 2025 and anything after July 24, 2026 are not in the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every recomputed ratio matched, including 4.22x total debt, 4.20x net debt, 3.02x secured debt and 4.43x cash interest cover on last-twelve-months Adjusted EBITDA of 22,251. | The leverage and cover figures can be relied on as arithmetic from company Adjusted EBITDA. | High |
| The Q2 2026 EBITDA fall was described as a revenue problem with falling underlying costs, but 184 of the 240 revenue fall is an allocation offset in programming cost. | Like-for-like revenue fell 56 and costs rose 165, so cost growth, including Cox transition expense, matters as much as customer trends. | High |
| Cox financing, the post-closing perimeter and approvals have no source evidence beyond the issuer's expectations. | The effect of Cox debt on the secured layer ahead of the unsecured notes cannot be traced or measured. | Low |
| One quotation drops the words "subject to certain exceptions", and three qualitative descriptions lack figures. | No number changes; the wording should be read with the corrections here. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 0 are directly sourced, 4 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the missing Cox financing, perimeter and approval evidence, which matters because Cox notes and part of the new debt are expected to join the guaranteed and secured group ahead of the issuer's unsecured notes, and it implies committee use stays restricted until the agreement and financing papers are supplied. One explanation of why Q2 2026 Adjusted EBITDA fell must also be read with the correction in CP5-001.

### Traceability summary

| Rank | Credit driver | Classification | Traceability status | Most important gap |
| --- | --- | --- | --- | --- |
| 1 | Leverage of 4.22x and cover of 4.43x on falling EBITDA | Calculated | Remediation Needed | Cause of the EBITDA decline misattributed in CP-1 and CP-2 |
| 2 | Unsecured notes of 26,734 behind secured debt of 67,111 | Calculated | Committee-Ready | Executed documents not supplied |
| 3 | Parent distributions of 5,898 above free cash flow of 5,070 | Calculated | Committee-Ready | Parent policy is a stated range, not a covenant |
| 4 | Liquidity of 3,985 and 21,147 due in 2029 and 2030 | Calculated | Committee-Ready | Availability printed to 0.1 billion; no facility split at June 30, 2026 |
| 5 | Cox closing structure and its effect on the secured layer | Insufficient Information | Not Traceable | No financing, perimeter or approval evidence |

### Audit summary and clearance

Confidence Score: 34 / 100 (Band: Insufficient Information). qa_status: Restricted. committee_status: Restricted. The score is the canon formula run with the retained script: score = clamp((0.6 x 72 + 0.4 x 100) x 0.7 - 24, 0, 100) = 34.24, rounded to 34. The inputs are lineage of the five material drivers (four Calculated and one Insufficient Information, so E is 72), all 17 required registers present (C is 100), a partial source gate because executed agreements and Cox papers are missing (S is 0.7), and findings of 1 Material and 3 Minor (P is 24). The Material finding caps the score at 59 and sets Restricted; the score is below that cap. The low band reflects the missing evidence on the central open item and the penalty for four defects; it does not mean the recomputed arithmetic is unreliable.

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 3. Committee Use: Restricted.

No finding changes a ratio or the direction of the credit view. One committee-facing explanation (CP5-001) misstates the cause of the Q2 2026 EBITDA decline, so committee use is restricted until it is read with the correction in this answer and the Cox evidence gap is closed. The orphan claim protocol is not triggered: the one Insufficient Information driver is flagged as a missing datapoint in CP-1A and CP-2, so it carries a limitation.

### Remediation priority map

- Must-fix before committee: CP5-001 (read CP-1's Interpretation (Earnings) bullet and CP-2's second key finding as corrected in this answer: Q2 2026 like-for-like revenue fell 56 and like-for-like costs rose 165, because 184 of the revenue fall is the seamless entertainment allocation offset in programming cost).
- Must-fix before the handoff is consumed downstream: None. The correction travels with this answer.
- Monitoring follow-up: CP5-004 (use the CP-1A explanation of the Cox cash figures: the Charter Holdings cash component moved from 500 to 650) and the Cox evidence gap CP-5-GAP-001.
- Formatting and hygiene: CP5-002 (restore the words "subject to certain exceptions" to the Obligors quotation) and CP5-003 (support or soften "largely fixed" cost wording and the "largest open items" superlative).

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

Module Status: Ready with Limitations. Traceability Scope: Top 5. Files used: seven pack sources, the context and four handoffs. Missing required inputs: executed indentures, Charter Operating credit agreement, intercreditor agreement, Exhibit 22.1, Cox Transaction Agreement and financing papers, Liberty Broadband merger agreement, any filing after July 24, 2026. External sources: none used by the upstream handoffs or by this answer. Entity key: issuer_id cco-holdings-llc available. Re-anchor: run `cco-holdings-llc-2026-11-05-credit_snapshot-host`, as-of 2026-11-05, current period q2-2026, prior period fy-2025, currency USD.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_ccoh-20251231.htm.jsonl | Audited filing, primary | FY2025, FY2024, FY2023 | CCO Holdings, LLC consolidated | Statements, debt table, Note 9, Item 7A, covenants, commitments, Cox risk factors | Text extraction only; entity chart is an image | CP-1 base, CP-2 maturity split |
| S2 | 10-Q_2025-09-30_ccoh-20250930.htm.jsonl | Unaudited filing, primary | Q3 2025, 9M 2025 | Consolidated | Balance sheet, 9M flows, availability, earlier Cox terms | Unaudited | LTM Q3 2025 and Cox term history |
| S3 | 10-Q_2026-03-31_ccoh-20260331.htm.jsonl | Unaudited filing, primary | Q1 2026 | Consolidated | Statements, debt note, redemptions, availability | Unaudited | LTM Q1 2026 |
| S4 | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | Unaudited filing, primary | Q2 2026, 6M 2026 | Consolidated | Statements, debt classes, MD&A drivers, guarantor text, Cox text | Unaudited; no maturity table or covenant ratio | Current-period base |
| S5 | EX-99.1_2026-01-30_chtrex991earningsrelease12.htm.jsonl | Management release, supporting | Q4 2025, FY2025 | Charter Communications, Inc. consolidated | January 2026 issuance statement | Parent perimeter | Issuance check |
| S6 | EX-99.1_2026-04-24_chtrex991earningsrelease33.htm.jsonl | Management release, supporting | Q1 2026 | Charter consolidated | Not used for figures | Parent perimeter | None |
| S7 | EX-99.1_2026-07-24_chtrex991earningsrelease63.htm.jsonl | Management release, supporting | Q2 2026 | Charter consolidated | Repurchase cash cost, parent cash and net income | Parent perimeter | Perimeter contrast |
| S8 | context | Run settings, not evidence | 2026-11-05 | Run | As-of date, currency, periods, sector | Not issuer evidence | Scope |
| H0 | CP-0 handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Source readiness | Host authored | Audited here |
| H1 | CP-1 handoff | Analyst handoff | FY2024 to Q2 2026 | Consolidated | Financial base | Host authored | Audited here |
| H1A | CP-1A handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Business and transaction context | Host authored | Audited here |
| H2 | CP-2 handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Credit synthesis | Host authored | Audited here |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Total debt of 93,845 at 4.22x last-twelve-months Adjusted EBITDA of 22,251 and cash interest cover of 4.43x, with EBITDA falling | CP-1, CP-2 | Debt note, Adjusted EBITDA reconciliations, cash interest lines | Leverage rises mechanically as EBITDA falls, and interest absorbs 22.58% of EBITDA | Direction and level of leverage drive the credit view | S4 page:10, page:26, page:7; S1 page:91, page:142; S2 page:27 | Company non-GAAP EBITDA; not a covenant ratio |
| 2 | Unsecured notes of 26,734 with no subsidiary guarantee behind secured debt of 67,111 | CP-1, CP-1A, CP-2 | Debt classes and guarantor text | Unsecured holders attach at 3.02x and detach at 4.22x of EBITDA | Ranking decides loss absorption order | S4 page:10, page:33 to page:34; S1 page:98 to page:99, page:155 | Executed documents not supplied |
| 3 | Distributions to parent of 5,898 against free cash flow of 5,070 over the last twelve months | CP-1, CP-1A, CP-2 | Cash flow statements, free cash flow reconciliations, buyback funding text | Cash leaves the group above internally generated cash | Debt reduction depends on parent policy | S4 page:7, page:26, page:32; S1 page:92, page:142 | Policy range is not a covenant |
| 4 | Liquidity of 3,985 and maturities of 7,279 in 2029 and 13,868 in 2030 | CP-1, CP-2 | Balance sheet, printed availability, maturity and Item 7A tables | Revolver-based liquidity must fund a 2029 and 2030 wall | Refinancing capacity and cost | S4 page:5, page:11, page:27; S1 page:105, page:160 | Availability printed to 0.1 billion; no facility split at June 30, 2026 |
| 5 | Pending Cox Transactions: expected guaranteed and secured Cox debt and unresolved perimeter | CP-1A, CP-2 | Issuer statements of expectation | New secured claims could rank ahead of the unsecured notes | Largest open structural item | S4 page:8 to page:9, page:27, page:34; S1 page:28, page:64 | No financing, perimeter or approval evidence |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue 13,526 against 13,766 and Adjusted EBITDA 5,428 against 5,668 in Q2 2026 | CP-1 | `Adjusted EBITDA $ 5,428 $ 5,668` (S4 page:26); revenues (S4 page:5) | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| LTM Adjusted EBITDA 22,251 | CP-1 | 22,611 + 11,046 - 11,406 (S1 page:91; S4 page:26) | Yes | Filing inputs | Calculated | Recomputed | High | Committee-Ready |
| Total debt / EBITDA 4.22x and net 4.20x | CP-1, CP-2 | 93,845 and 93,560 over 22,251 (S4 page:5, page:10) | Yes | Filing inputs, company non-GAAP EBITDA | Calculated | Recomputed | Medium | Committee-Ready |
| Cash interest cover 4.43x | CP-1, CP-2 | 22,251 over 5,024 (S1 page:142; S4 page:7) | Yes | Filing inputs | Calculated | Recomputed | Medium | Committee-Ready |
| Debt classes 26,734, 54,658 and 12,453; secured 67,111 and 3.02x | CP-1, CP-1A, CP-2 | `Senior unsecured notes $ 26,734` (S4 page:10); sum of two printed lines | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| Unsecured notes not guaranteed by subsidiaries and structurally subordinated | CP-1A, CP-2 | `(other than the CCO Holdings unsecured notes)` (S4 page:33); S1 page:155 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Distributions 5,898 against free cash flow 5,070 (LTM) | CP-1, CP-2 | 6,794 + 2,460 - 3,356 and 5,827 + 2,492 - 3,249 (S1 page:92, page:142; S4 page:7, page:26) | Yes | Filing inputs | Calculated | Recomputed | High | Committee-Ready |
| Issuer is the primary funding source for Charter buybacks | CP-1A, CP-2 | `the primary source for funding such purchases through distributions` (S4 page:32) | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Liquidity 3,985 (cash 285, availability about 3,700) | CP-1, CP-2 | `approximately $3.7 billion` and `$285 million` (S4 page:11, page:27, page:36) | Yes | Filing, rounded | Calculated | Recomputed | Medium | Committee-Ready |
| Year-end maturity ladder 1,055; 3,555; 5,392; 7,279; 13,868; 63,468 | CP-1, CP-2 | `2030 13,868 3,659` (S1 page:160); fixed and variable split (S1 page:105) | Yes | Audited | Directly Sourced | Verified | High | Committee-Ready |
| Adjusted 2026 and 2027 principal 305 and 1,305 | CP-1, CP-2 | 1,055 - 750; 3,555 - 2,250 (S3 page:11) | Yes | Filing inputs | Calculated | Recomputed, excludes amortisation paid and unallocated repurchases | Medium | Committee-Ready |
| Covenant ratios 4.0 against 6.0; 2.8 against 5.0 and 4.0 at December 31, 2025 | CP-1, CP-2 | S1 page:156, page:158 | Yes | Audited | Directly Sourced | Verified | High | Committee-Ready |
| Current covenant headroom | CP-1, CP-2 | No ratio printed after December 31, 2025 (S4 page:36 says the test was met) | Yes | Filing | Insufficient Information | Correctly marked as not measurable | Low | Remediation Needed |
| Covenant proxy 2.81x, 3.94x, 4.00x | CP-1, CP-2 | 67,367 and 94,617 over 22,611 + 1,400 (S1 page:91) | Yes | Rounded fee, definition not supplied | Assumption-Based | Labelled proxy | Low | Committee-Ready |
| EBITDA sensitivity 4.44x, 4.69x, 4.96x; floating-rate sensitivity about 125 | CP-2 | 93,845 over reduced EBITDA; 12,453 x 1.00% | Yes | Illustrative | Assumption-Based | Recomputed | Low | Committee-Ready |
| Coupon change of about 58 per year on the early 2026 refinancing | CP-2 | 1,750 x 7.000% + 1,250 x 7.375% less 750 x 5.500% + 2,250 x 5.125% (S1 page:155; S3 page:11) | Yes | Filing coupons | Calculated | Recomputed, gross | Medium | Committee-Ready |
| Cox terms: cash 4.0 and 4.2 billion; assumed debt 12.6 and 12.4 billion; Charter Holdings cash 500 and 650 | CP-1A | S1 page:28, page:64; S2 page:9; S3 page:9; S4 page:9, page:27 | Yes | Filings differ by date | Conflicting | Logged and explained by CP-1A, not reconciled | Medium | Remediation Needed |
| Cox notes expected to become guaranteed and secured debt; Cox entities to become Obligors | CP-1A, CP-2 | `will constitute Guaranteed and Secured Debt` (S4 page:34) | Partial | Filing, expectation | Directly Sourced | Verified; one quotation elides words | High | Remediation Needed |
| Cox financing, perimeter, approvals and closing status | CP-1A, CP-2 | None in the sources | No | No source | Insufficient Information | Gap flagged, not adverse | Low | Not Traceable |
| Q2 2026 EBITDA decline described as a revenue problem with falling underlying costs | CP-1, CP-2 | 240 revenue fall includes 184 allocation (S4 page:22, page:24); costs ex-allocation +165 (S4 page:23) | Partial | Contradicted by the filed breakdown | Conflicting | Corrected here | High | Not Traceable |
| Costs are largely fixed in the short run | CP-1A, CP-2 | No figure or text cited | No | No source | Weak Lineage | Flagged | Low | Remediation Needed |
| Behaviour category Neutral or Mixed | CP-1A | Distributions above free cash flow, debt reduction in 6M 2026, no creditor-adverse transaction found | Yes | Filings | Analyst Inference | Labelled interpretation | Medium | Committee-Ready |
| Customers: Internet 29,388 against 29,908; mobile 12,540 against 10,856 (thousands) | CP-1A, CP-2 | S4 page:19 to page:20 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Claims outside debt: equipment installment plan 1,596, short-term borrowings 1,155, supply chain finance 725, operating leases 1,276 | CP-1, CP-2 | S4 page:5, page:9 to page:10, page:12; S1 page:154 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Franchises and goodwill 63.34% of assets; fair-value cushion above 10% | CP-1A, CP-2 | `by more than 10%` (S4 page:21); balance sheet (S4 page:5) | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q2 2026 revenue 13,526 against 13,766 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:5; statement of operations | CP-1 Financials and credit metrics | Sourced | Unaudited filing | Matches page text |
| Adjusted EBITDA 5,428 and 5,668; 11,046 and 11,406 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:26; reconciliation | CP-1 Financials and credit metrics | Sourced | Unaudited filing, non-GAAP | Management defined |
| Adjusted EBITDA FY2025 22,611 and FY2024 22,476 | source-text | 10-K_2025-12-31_ccoh-20251231.htm.jsonl | S1 | page:91; reconciliation | CP-1 Financials and credit metrics | Sourced | Audited filing, non-GAAP section unaudited | Management defined |
| Principal debt 93,845 and classes | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:10; Note 4 | CP-1 Debt tables | Sourced | Unaudited filing | Carrying 93,959; fair value 83,550 |
| Cash 285 and restricted cash 90 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:5 and page:7 | CP-1 Liquidity | Sourced | Unaudited filing | Restricted cash in prepaid assets |
| Cash paid for interest 2,493 and 2,426; 4,957 and 5,305 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl; 10-K_2025-12-31_ccoh-20251231.htm.jsonl | S4; S1 | page:7; page:142 | CP-1 interest cover | Sourced | Filings | Supplemental cash flow line |
| Free cash flow 2,492 and 3,249; 5,827 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl; 10-K_2025-12-31_ccoh-20251231.htm.jsonl | S4; S1 | page:26; page:92 | CP-1 cash flow | Sourced | Filings, non-GAAP | Company definition |
| Distributions to parent 2,460, 3,356 and 6,794 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl; 10-K_2025-12-31_ccoh-20251231.htm.jsonl | S4; S1 | page:7; page:142 | CP-1 cash flow | Sourced | Filings | Financing activities |
| Availability of about 3.7 billion at June 30, 2026 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:11; page:27 | CP-1 Liquidity | Sourced | Unaudited filing | Rounded to 0.1 billion |
| Maturity ladder by year | source-text | 10-K_2025-12-31_ccoh-20251231.htm.jsonl | S1 | page:160; Note 9 | CP-1 Debt maturities | Sourced | Audited filing | As of December 31, 2025 |
| Fixed 82,668 and variable 11,949 by year | source-text | 10-K_2025-12-31_ccoh-20251231.htm.jsonl | S1 | page:105; Item 7A | CP-2 Key findings | Sourced | Audited filing | Confirms CP-1 derived components |
| Indenture leverage 4.0 against 6.0; Charter Operating 2.8 against 5.0 and 4.0 | source-text | 10-K_2025-12-31_ccoh-20251231.htm.jsonl | S1 | page:156; page:158 | CP-1 Covenants | Sourced | Audited filing | December 31, 2025 only |
| Test "met" at June 30, 2026 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:36; distributions | CP-1 Covenants | Sourced | Unaudited filing | No figure printed |
| Guarantee and collateral structure | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:33 to page:35 | CP-1A Company profile | Sourced | Unaudited filing | Issuer's summary of documents |
| Cox Transaction Agreement terms | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:8 to page:9 | CP-1A Transaction summary | Sourced | Unaudited filing | Summary only; agreement not supplied |
| Charter Holdings cash 500 in earlier filings | source-text | 10-K_2025-12-31_ccoh-20251231.htm.jsonl; 10-Q_2025-09-30_ccoh-20250930.htm.jsonl | S1; S2 | page:28; page:9 | CP-1A Conflicts | Conflicting | Filings | Later filings say 650 |
| Cox notes to become guaranteed and secured debt | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:34 | CP-1A Transaction summary | Sourced | Unaudited filing | Expectation |
| Primary funding source for Charter buybacks | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:32 | CP-1A Governance | Sourced | Unaudited filing | Quoted |
| Customer relationships and lines | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:19 to page:20 | CP-1A Operating model | Sourced | Unaudited filing | Approximate counts |
| Revenue by product line | source-text | 10-K_2025-12-31_ccoh-20251231.htm.jsonl; 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S1; S4 | page:162; page:13 | CP-1 Revenue by product line | Sourced | Filings | Sums to total |
| Equipment installment plan facility 1,596 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:5; page:11 to page:12 | CP-1 Claims outside debt | Sourced | Unaudited filing | Carrying value |
| Short-term borrowings 1,155 and supply chain finance 725 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:9 to page:10 | CP-1 Claims outside debt | Sourced | Unaudited filing | Note 3 |
| Operating lease liabilities 1,276 | source-text | 10-K_2025-12-31_ccoh-20251231.htm.jsonl | S1 | page:154; Note 8 | CP-1 Claims outside debt | Sourced | Audited filing | December 31, 2025 only |
| January 2026 issuance and February 2026 redemptions | source-text | 10-K_2025-12-31_ccoh-20251231.htm.jsonl; 10-Q_2026-03-31_ccoh-20260331.htm.jsonl | S1; S3 | page:155; page:11 | CP-1 Events | Sourced | Filings | Release S5 page:7 confirms issuance |
| Q2 2026 repurchases 1.2 billion and gain 243 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:11 | CP-1 Events | Sourced | Unaudited filing | Series not disclosed |
| Seamless entertainment allocation 184 | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:22; page:24 | CP-1 Events | Sourced | Unaudited filing | Described as netted within video revenue |
| Operating cost changes by function | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:23 | This answer, CP5-001 | Sourced | Unaudited filing | Total (19) |
| Franchises and goodwill and impairment cushion | source-text | 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | S4 | page:5; page:21 | CP-1A Operating model | Sourced | Unaudited filing | Fourth quarter 2025 test |
| Behaviour category Neutral or Mixed | source-text | CP-1A handoff | H1A | Ownership, governance and sponsor behaviour | CP-1A | Inference | Analyst handoff | Labelled Analyst Interpretation |
| Costs are largely fixed | source-text | none | none | none | CP-1A Operating model; CP-2 Key findings | Weak Lineage | Analyst handoff | No cited figure |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA, Q2 2026 | CP-1 chart data, metrics table; CP-2 | 22,611; 11,046; 11,406 | 22,611 + 11,046 - 11,406 = 22,251; period LTM to June 30, 2026; company non-GAAP, not normalised | Calculated | Recomputed | High | Leverage, cover | S1 page:91; S4 page:26 |
| Total debt / EBITDA | CP-1, CP-2 | 93,845; 22,251 | 93,845 / 22,251 = 4.22x; principal debt at June 30, 2026 | Calculated | Recomputed | Medium | Leverage | S4 page:10 |
| Net debt / EBITDA | CP-1, CP-2 | 93,845; 285; 22,251 | (93,845 - 285) / 22,251 = 4.20x; unrestricted cash only | Calculated | Recomputed | Medium | Leverage | S4 page:5, page:10 |
| Secured debt / EBITDA | CP-1, CP-2 | 54,658; 12,453; 22,251 | 67,111 / 22,251 = 3.02x | Calculated | Recomputed | Medium | Ranking | S4 page:10 |
| Cash interest cover | CP-1, CP-2 | 22,251; 5,024 | 22,251 / 5,024 = 4.43x; LTM cash interest 4,957 + 2,493 - 2,426 = 5,024 | Calculated | Recomputed | Medium | Debt service | S1 page:142; S4 page:7 |
| LTM free cash flow | CP-1, CP-2 | 5,827; 2,492; 3,249 | 5,827 + 2,492 - 3,249 = 5,070; also 16,757 - 12,064 + 377 = 5,070 | Calculated | Recomputed | High | Cash conversion | S1 page:92; S4 page:26 |
| LTM distributions to parent | CP-1, CP-2 | 6,794; 2,460; 3,356 | 6,794 + 2,460 - 3,356 = 5,898; excess over free cash flow 828 | Calculated | Recomputed | High | Leakage | S1 page:142; S4 page:7 |
| Liquidity | CP-1, CP-2 | 285; about 3,700 | 285 + 3,700 = 3,985; accurate to about 50 | Calculated | Recomputed | Medium | Liquidity | S4 page:5, page:11 |
| Liquidity / current portion of debt | CP-2 | 3,985; 999 | 3,985 / 999 = 3.99x | Calculated | Recomputed | Medium | Near-term coverage | S4 page:5 |
| 2029 and 2030 concentration | CP-2 | 7,279; 13,868; 94,617 | 21,147 / 94,617 = 22.35% | Calculated | Recomputed | High | Refinancing | S1 page:160 |
| Adjusted 2026 and 2027 principal | CP-1, CP-2 | 1,055; 3,555; 750; 2,250 | 1,055 - 750 = 305; 3,555 - 2,250 = 1,305; excludes amortisation paid and unallocated repurchases | Calculated | Recomputed | Medium | Refinancing | S1 page:160; S3 page:11 |
| EBITDA sensitivity at constant debt | CP-2 | 93,845; 22,251 | 93,845 / (22,251 x 0.95) = 4.44x; x 0.90 = 4.69x; x 0.85 = 4.96x | Assumption-Based | Recomputed, illustrative | Low | Leverage tolerance | S4 page:10, page:26 |
| Floating-rate sensitivity | CP-2 | 12,453 | 12,453 x 1.00% = 124.5; before floors; no hedges described | Assumption-Based | Recomputed, gross | Low | Rate risk | S4 page:10; S1 page:105 |
| Coupon change on refinancing | CP-2 | Coupons and amounts | 214.7 - 156.6 = 58.1 per year | Calculated | Recomputed, gross | Medium | Interest cost | S1 page:155; S3 page:11 |
| Covenant headroom | CP-1, CP-2 | 6.0 and 4.0; 5.0 and 4.0 and 2.8 | 2.0, 2.2 and 1.2 turns; cushions 33%, 44%, 30% at constant debt | Calculated | Recomputed, rounded ratios | Medium | Covenant | S1 page:156, page:158 |
| Covenant proxy | CP-1, CP-2 | 67,367; 94,617; 22,611; about 1,400 | 67,367 / 24,011 = 2.81x; 94,617 / 24,011 = 3.94x; (94,617 + 1,447) / 24,011 = 4.00x | Assumption-Based | Labelled proxy | Low | Covenant | S1 page:91, page:141 |
| Q2 2026 EBITDA bridge, like-for-like | This answer, CP5-001 | 240; 184; 19; 19 | Revenue -240 + 184 = -56; costs -19 + 184 = +165; stock compensation add-back -19; -56 - 165 - 19 = -240 | Calculated | Recomputed | High | Earnings quality | S4 page:22 to page:24, page:26 |
| Metric-definition drift | All modules | Adjusted EBITDA, free cash flow, net debt | Same company Adjusted EBITDA, same free cash flow definition and same principal-debt basis in all four modules; parent leverage 4.18 is labelled parent | Calculated | No drift found | High | Consistency | S4 page:26 to page:27 |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | The Q2 2026 EBITDA decline is a revenue problem and underlying costs fell | 184 of the 240 revenue fall is the seamless entertainment allocation, offset in programming cost; like-for-like revenue fell 56 and like-for-like costs rose 165 | Conflicting | The mechanism changes the monitoring focus from customers only to cost growth, including Cox transition expense, and affects confidence in the earnings trend | Read the CP-1 Interpretation (Earnings) bullet and the CP-2 second key finding as corrected here | CP-1 Interpretation; CP-2 Key findings; CP-1A Business view |
| Minor | Cox expected treatment of Cox entities | The quotation "and substantially all of its subsidiaries will become Obligors" omits ", subject to certain exceptions," | Directly Sourced | A legal qualifier is dropped from a structural statement | Restore the words when quoting | CP-1A Conflicts table |
| Minor | Costs are largely fixed; Cox and Liberty Broadband are the largest open items | No figure or text is cited for either characterisation | Weak Lineage | Unsupported adjectives can overstate operating leverage or rank items without a measure | Support with figures or soften | CP-1A Operating model; CP-2 Key findings and Key credit risks |
| Minor | Cox cash figures differ without explanation | CP-0 and CP-1 did not explain 4.0 against 4.2 billion; CP-1A found the cash component moved from 500 to 650 | Conflicting | Readers could treat the difference as unexplained | Use the CP-1A explanation | CP-0 Document conflicts; CP-1 Events |
| Material | Cox financing, perimeter and approvals | No source evidence | Insufficient Information | Decides ranking ahead of the unsecured notes | Obtain the agreement, proxy and financing papers; already flagged, not adverse | CP-1A, CP-2 credit view |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2024 to Q2 2026; no executed documents and nothing after July 24, 2026 | Missing indentures and Cox papers leave ranking and covenant definitions unverified | Ranking and headroom conclusions stay conditional | Supply executed documents and later filings |
| Citation completeness | Ready with Remediation | 73 figure-and-page checks passed; 87 quotations checked and 85 matched; one elision and one quotation from pack metadata | A dropped legal qualifier or uncited adjective weakens a structural statement | Minor wording risk; no figure risk | Restore the qualifier; support or soften adjectives |
| Calculation traceability | Committee-Ready | Every derived ratio recomputed from printed inputs and matched | None found | Arithmetic can be relied on | None |
| Assumption transparency | Ready with Remediation | Sensitivities and the covenant proxy are labelled illustrative or proxy; the cause statement in CP5-001 is not an assumption but an attribution | An unlabelled attribution can mislead the reader about cost control | Earnings trend mechanism needs the correction | Apply the CP5-001 correction |
| Markdown/export artifact integrity | Committee-Ready | Each handoff has the six H2 headings once in order and its required selectors once; single-table selectors hold one table | None found | Downstream consumption is safe | None |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Cox financing, perimeter, end date, approvals and closing status | Transaction Agreement, proxy statement, financing commitments, later 8-K filings | Cox debt may join the secured group ahead of the unsecured notes while Cox earnings may sit outside the issuer | CP-1A transaction summary; CP-2 credit view, risks | High impact on confidence | Cox agreements and filings after July 24, 2026 |
| CP-5-GAP-002 | Executed indentures, credit agreement, intercreditor agreement and Exhibit 22.1 | Executed documents | Covenant definitions, baskets, release and change-of-control terms cannot be tested | CP-1 Covenants; CP-2 Key findings | High impact on confidence | Executed documents |
| CP-5-GAP-003 | Covenant ratios and covenant EBITDA after December 31, 2025; management fee only to 0.1 billion | Compliance certificates | Current headroom is not measurable | CP-1, CP-2 covenant text | High impact on confidence | Compliance certificates |
| CP-5-GAP-004 | Current series-level debt schedule and mapping of 1,249 of repurchases | Debt schedule | Current ladder and coupon cost cannot be rebuilt exactly | Maturity chart; CP-2 refinancing | Medium impact on confidence | Current debt schedule |
| CP-5-GAP-005 | Facility-level availability and letters of credit at June 30, 2026; availability rounded | Facility schedule | Liquidity accurate to about 50 | Liquidity chart; CP-2 liquidity | Medium impact on confidence | Facility schedule |
| CP-5-GAP-006 | Entity ownership chart is an image | Chart content | Ownership percentages and debt by entity unconfirmed | CP-1A profile | Medium impact on confidence | Filed 10-K chart |
| CP-5-GAP-007 | No filing for the September 2026 quarter | Q3 2026 10-Q and release | Leverage and liquidity may have moved since June 30, 2026 | All modules | High impact on confidence | EDGAR filings to November 5, 2026 |
| CP-5-GAP-008 | Original HTML and XBRL not supplied | Filed documents | Table-layout fidelity cannot be checked from text | CP-5 lineage | Low impact on confidence | Filed documents |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/11c1e7b719fd9d28d876f9b5c0b35123c1ab72a5cfd54ad302afac8583a138b3/1.response.md; run cco-holdings-llc-2026-11-05-credit_snapshot-host | Source readiness for four modules | Analyst handoff over seven filings | Six H2 headings present once in order; Readiness view follows Reader summary | Accepted by CP-OS structural check | One minor point: Cox figures not explained (CP5-004) |
| CP-1 | requests/CP-1/45e32ae723e0ce0c05d9f05f74e1b68a94a209eb5b8b6ef47f0488aed6d19a3c/1.response.md; same run | Financial base FY2024 to Q2 2026 | Analyst handoff over filings | Six H2 headings present; five report selectors once each; one table under Financials and credit metrics | Accepted by CP-OS structural check | One Material point (CP5-001) |
| CP-1A | requests/CP-1A/c25f5b57df37989c695c0745c7a1ea5cf45f13d6cea413e57704539fbea1dbb9/1.response.md; same run | Business and transaction context | Analyst handoff over filings | Six H2 headings present; three selectors once each; one table each under the two table selectors; prose only under Transaction summary | Accepted by CP-OS structural check | Two minor points (CP5-002, CP5-003) |
| CP-2 | requests/CP-2/feb8b61034f3b55c9e1e622d339910d8e3f46af3dafccf07cca9c23f2002a34e/1.response.md; same run | Credit synthesis | Analyst handoff over CP-1 and CP-1A | Six H2 headings present; Key findings and Strengths and weaknesses are prose only | Accepted by CP-OS structural check | One Material point inherited (CP5-001); one minor (CP5-003) |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-0, CP-1, CP-1A, CP-2 | 73 figure-and-page checks on debt, cash flow, covenant, maturity, Cox and liquidity figures | Verified | Every checked string was on the cited page | None | None |
| Minor | CP-1A | Conflicts table quotation on Cox entities becoming Obligors | Partial | The words ", subject to certain exceptions," are dropped (S4 page:34) | Restore the words | No effect on figures; wording only |
| Minor | CP-1A, CP-2 | Costs largely fixed; largest open items | Unsupported | No cited support | Support or soften | No effect on figures |
| None | CP-0 | Quotation "3 of 3 quarters have a release, not a presentation, on EDGAR" | Verified against pack metadata | It comes from the retrieval record, not a pinned filing, and CP-0 says so | None | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Attribution of the Q2 2026 EBITDA fall: "costs held flat ... so underlying costs fell" | Adjusted EBITDA = revenue - operating costs + stock compensation holds, but the allocation moves revenue and programming cost together, so flat total costs hide 165 of like-for-like cost growth | Company says EBITDA fell "primarily due to lower revenue and higher transition expenses" (S4 page:19); programming fell "as a result of" the allocation (S4 page:24) | Read as corrected in Calculations | Restricts committee use until read |
| None | CP-1, CP-2 | Total, net and secured leverage; cash interest cover; free cash flow; liquidity; concentration; sensitivities | All recomputed and matched | None | None | None |
| None | CP-1, CP-2 | Definitions | Principal debt, unrestricted cash, company Adjusted EBITDA and company free cash flow used consistently; covenant EBITDA adds back management fees and is not computed | Parent leverage 4.18 against issuer 4.20 is a perimeter and definition difference, labelled | None | None |
| None | CP-2 | Variable-rate maturities (642; 279; 8,068) derived by difference in CP-1 | Confirmed by the Item 7A table (S1 page:105) | None | None | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A, CP-2 | Unsecured notes have no subsidiary guarantee and are structurally and effectively subordinated to 67,111 of secured debt | CCO Holdings and Charter Operating indentures, credit agreement, intercreditor agreement, Exhibit 22.1 | Only the issuer's summary in the 10-K and 10-Q | Obtain executed documents; keep the claim labelled as the issuer's description | Counsel review of ranking and guarantees |
| Material | CP-1, CP-2 | Covenant levels (6.0; 5.0; 4.0), definitions and the effect of a Charter Operating failure on CCO Holdings debt | Credit agreement and indentures | Ratios printed only at December 31, 2025; definitions not supplied | Obtain compliance certificates and definitions | Counsel and credit review of baskets |
| Material | CP-1A, CP-2 | Cox notes and new debt expected to become Guaranteed and Secured Debt and Cox entities Obligors | Transaction Agreement, supplemental indentures, security documents | Expectation only; perimeter and issuer of new debt not stated | Obtain documents; keep as expectation | Counsel review of post-closing structure |
| Minor | CP-1 | Distribution restrictions (leverage test gating payments for parent note principal) | Indentures | Test described, not tested | Obtain indentures | Counsel review of restricted payment capacity |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-0, CP-1, CP-1A, CP-2 | No relative value, spread, price or peer claim is made; CP-2 states no peer ranking, instrument recommendation or recovery conclusion | Market prices, spreads and peers were not required for this scope | Fair values of debt appear only as filing figures | No action: out of scope | None; relative value belongs to a later module |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A | Cox cash 4.0 and 4.2 billion; assumed debt 12.6 and 12.4 billion | CP-0 said the 10-Q components do not equal 4.0 billion without noting that the Charter Holdings cash moved from 500 to 650; CP-1A explains it and notes the 12.6 figure is pro forma | Use the CP-1A explanation | Reader of CP-0 alone could treat the difference as unexplained |
| Minor | CP-1A, CP-2 | Obligors quotation elision | CP-2 repeats the expectation correctly without the quotation | Restore words in CP-1A | None for figures |
| None | CP-1, CP-2 | Leverage, cover, liquidity and maturity figures | All CP-2 figures equal CP-1 figures or are recomputed from them | None | None |
| None | CP-1, CP-1A | Mortgage note 265 at December 31, 2025 and 256 at June 30, 2026 | Different dates | None | None |
| None | CP-0, CP-1 | Parent versus issuer figures (net income 1.3 billion against 1,973; cash 509 against 285) | Perimeters labelled in every handoff | None | None |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Unbenchmarked adjectives | "largest open items" and "largely fixed network cost base" lack a measure | Support or soften | None on figures |
| None | All | Duplication | Repeated references to executed documents and Cox papers appear once per module gap table, which the method requires | None | None |
| None | All | Materiality | Top 5 drivers cover leverage, ranking, leakage, liquidity and Cox; none is omitted | None | Committee-ready except the Cox driver |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| None | CP-0 | Headings, Sources, Reader summary, Readiness view | None | None | Consumed by CP-1 |
| None | CP-1 | Headings, chart selectors, single table selector, Sources with sha256 | None | None | Consumed by CP-1A and CP-2 |
| Minor | CP-1A | Conflicts table quotation | Elided qualifier | Restore words | None for figures |
| None | CP-2 | Headings, prose-only selectors, Credit view word range | None | None | Consumed here |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1, CP-2, CP-1A | Logic and attribution | Q2 2026 EBITDA decline attributed to revenue with underlying costs falling; like-for-like revenue fell 56 and costs rose 165 | Read as corrected in this answer | Restricts committee use | Open |
| CP5-002 | Minor | CP-1A | Citation | Quotation drops ", subject to certain exceptions," | Restore words | None for figures | Open |
| CP5-003 | Minor | CP-1A, CP-2 | Weak lineage | "Largely fixed" cost wording and "largest open items" lack support | Support or soften | None for figures | Open |
| CP5-004 | Minor | CP-0, CP-1 | Version consistency | Cox 4.0 and 4.2 billion differences not explained until CP-1A | Use CP-1A explanation | None for figures | Open |

## Calculations

All inputs are from the cited pages, recomputed here from the pinned text and the handoffs; amounts are USD millions unless stated.

### Reproduction of upstream figures

- LTM Adjusted EBITDA: 22,611 + 11,046 - 11,406 = 22,251 (also 22,476 + 16,946 - 16,736 = 22,686 at Q3 2025 and 22,611 + 5,618 - 5,738 = 22,491 at Q1 2026). Matches.
- Leverage: 93,845 / 22,251 = 4.22x; (93,845 - 285) / 22,251 = 4.20x; 67,111 / 22,251 = 3.02x; December 31, 2024 93,779 / 22,476 = 4.17x; December 31, 2025 94,617 / 22,611 = 4.18x. Matches.
- Cover: 22,251 / 5,024 = 4.43x with 4,957 + 2,493 - 2,426 = 5,024; FY2025 22,611 / 4,957 = 4.56x; FY2024 22,476 / 5,305 = 4.24x. Matches.
- Free cash flow: 16,865 - 11,624 + 586 = 5,827; 8,367 - 5,713 - 162 = 2,492; 8,475 - 5,273 + 47 = 3,249; LTM 5,827 + 2,492 - 3,249 = 5,070. Matches the printed reconciliations.
- Expense block: 8,236 + 2,189 + 51 = 10,476 and 13,526 - 10,476 = 3,050; FY2025 32,836 + 8,681 + 432 = 41,949 and 54,774 - 41,949 = 12,825. Matches.
- Adjusted EBITDA identity: revenue - operating costs + stock compensation: 13,526 - 8,236 + 138 = 5,428; 13,766 - 8,255 + 157 = 5,668; 54,774 - 32,836 + 673 = 22,611. Matches.
- Debt: 26,734 + 54,658 + 12,453 = 93,845; 27,250 + 55,418 + 11,949 = 94,617; series sum 82,668 + 11,949 = 94,617; ladder 1,055 + 3,555 + 5,392 + 7,279 + 13,868 + 63,468 = 94,617; fixed and variable by year sum to 82,668 and 11,949 (S1 page:105).
- Liquidity: 285 + 3,700 = 3,985; 3,985 / 999 = 3.99x; 2029 and 2030 7,279 + 13,868 = 21,147, 22.35% of 94,617.
- Sensitivity: 93,845 / 21,138 = 4.44x; 93,845 / 20,026 = 4.69x; 93,845 / 18,913 = 4.96x; 12,453 x 1.00% = 124.5.
- Coupon change: 1,750 x 7.000% = 122.5; 1,250 x 7.375% = 92.2; 750 x 5.500% = 41.3; 2,250 x 5.125% = 115.3; 122.5 + 92.2 - 41.3 - 115.3 = 58.1.
- Covenant proxy: 67,367 / (22,611 + 1,400) = 2.81x; 94,617 / 24,011 = 3.94x; 96,064 / 24,011 = 4.00x.
- Revenue shares FY2025: 23,765 / 54,774 = 43.39%; 13,703 / 54,774 = 25.02%; 42,580 / 54,774 = 77.74%. Intangibles (67,471 + 29,710) / 153,439 = 63.34%.

### CP5-001: like-for-like bridge of the Q2 2026 Adjusted EBITDA change

- Reported revenue change 13,526 - 13,766 = -240, of which the seamless entertainment allocation reduced video revenue by 184 (S4 page:22). Like-for-like revenue change -240 + 184 = -56.
- Reported operating cost change 8,236 - 8,255 = -19. By line (S4 page:23): programming -218, other costs of revenue +186, field and technology operations +21, customer operations +8, marketing and residential sales -31, transition expenses +65, other -50; sum -19. The 10-Q says programming fell "as a result of" the 184 allocation among other factors (S4 page:24), so like-for-like programming change is -218 + 184 = -34 and like-for-like operating cost change is -19 + 184 = +165 (inference that the allocation nets fully).
- Stock compensation fell 138 - 157 = -19, which lowers the add-back. Adjusted EBITDA change = -56 (revenue) - 165 (costs) - 19 (add-back) = -240, equal to 5,428 - 5,668.
- Cash operating costs excluding stock compensation were 8,098 in both quarters (8,236 - 138 and 8,255 - 157), but like-for-like they rose by 184 (0 + 184), of which 65 is Cox transition expense and 186 is other costs of revenue that the 10-Q ties to mobile device sales, mobile service direct costs and advertising costs on political revenue (S4 page:24).
- Reading: the filing attributes the EBITDA decline to "lower revenue and higher transition expenses" (S4 page:19). The like-for-like view shows weaker customer-driven revenue and higher cash costs together; "underlying costs fell" is not supported.

### Confidence score

- Lineage of the five material drivers: four Calculated (0.9 each) and one Insufficient Information (0): E = (4 x 0.9 + 0) / 5 x 100 = 72.
- Required registers present: 17 of 17, so C = 100. Source gate partial (executed documents and Cox papers missing): S = 0.7. Findings: 1 Material (15) and 3 Minor (9): P = 24.
- Score = (0.6 x 72 + 0.4 x 100) x 0.7 - 24 = 83.2 x 0.7 - 24 = 34.24, rounded to 34. Band Insufficient Information (below 40). Material cap (59) not binding; qa_status Restricted.

### Check counts

- Figure-and-page checks: 73 of 73 strings found on the cited pages. Quotation checks: 87 quoted spans in CP-0, CP-1, CP-1A and CP-2, 85 found in the pinned sources, one found only in the pack retrieval record (CP-0, labelled as such) and one elided (CP5-002).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Cox financing, perimeter, approvals and closing status not supplied (CP-5-GAP-001) | High | Committee use, relative value, committee challenge | Supply the agreement, proxy statement, financing commitments and later 8-K filings |
| Executed indentures, credit agreement, intercreditor agreement and covenant values after December 31, 2025 not supplied (CP-5-GAP-002, CP-5-GAP-003) | High | Legal and covenant review | Supply the executed documents and compliance certificates |
| No filing for the September 2026 quarter or later (CP-5-GAP-007) | High | All consumers | Supply the Q3 2026 10-Q and release or confirm none exists |
| Current series-level debt schedule, facility-level availability and entity chart image (CP-5-GAP-004 to CP-5-GAP-006) | Medium | Refinancing and structure analysis | Supply a current schedule and the chart |
| Original HTML and XBRL not supplied (CP-5-GAP-008) | Low | Table fidelity checks | Spot-check against filed documents |
| The correction in CP5-001 lives only in this handoff; CP-1 and CP-2 cannot be edited | Medium | Any reader of CP-1 or CP-2 alone | Read CP-5 with them |

## Next module

- Downstream use: carry the Restricted committee status, the CP5-001 correction (like-for-like revenue -56 and costs +165 in Q2 2026), the unresolved Cox structure and the missing executed documents as restrictions; do not treat the principal-debt ratios as covenant ratios; make no recovery, instrument or relative-value conclusion from these handoffs.
- Remediation owner: the author of CP-1, CP-1A and CP-2 should read the four issue-log items before re-issuing; no figure needs to change.
