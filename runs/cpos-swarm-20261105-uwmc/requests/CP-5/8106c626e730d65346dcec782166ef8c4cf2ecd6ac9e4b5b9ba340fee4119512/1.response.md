# CP-5 — Evidence trace and research integrity QA: UWM Holdings Corp (uwmc)

## Request

This audit covers the CP-0, CP-1, CP-1A and CP-2 handoffs for UWM Holdings Corp (UWMC) as of 2026-11-05, run `uwmc-2026-11-05-credit_snapshot-host` (pathway credit_snapshot, USD, current period Q2 2026, prior period FY2025). It checks claim-to-source lineage, locators, calculations, conflicts and cross-module consistency against the seven pinned filings, and grades what it finds. It does not rewrite any earlier handoff or any credit conclusion; where it corrects a statement it says so here.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_uwmc-20251231.htm.jsonl | 6df0e879c343753ce405aeb907aabeaeac058e835b89efb10be5b5f6ef447e2d | Audited annual report; opened for every annual figure, control, Tax Receivable Agreement and merger claim |
| 10-Q_2025-09-30_uwmc-20250930.htm.jsonl | 84f53b3c261a44ff2b63ce2fd8da76aab14001838b1a0e3a2f304e513f9c0145 | Q3 2025 Adjusted EBITDA cross-check |
| 10-Q_2026-03-31_uwmc-20260331.htm.jsonl | eb1fccb72198e8bd32b24af480098c49a4e103fa66da8e8b43ba0a46fdd7b8e3 | Q1 2026 statements, facility balances, merger termination |
| 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | cea2518652546d9284379186814d587a8012203f70fc41bfc3b1a399bf834746 | Primary source for the current period |
| EX-99.1_2026-02-26_irdeck4q25andfy2025-fina.htm.jsonl | 80372136ddaf727708bb7d020bd60e922c0bc6f80a8ff31bd92d35cba8e5b9c2 | Management presentation (supporting) |
| EX-99.1_2026-05-06_q12026ex-991pressrelease.htm.jsonl | 3516810c7f76bb754add7c9c09ef459031d4e398744e48f97ba6a9a478ed6c73 | Q1 2026 release (supporting) |
| EX-99.1_2026-08-05_q22026ex-991pressrelease.htm.jsonl | fce3d1caab58675ec9b80c128baca52e2510780e5b4d2dc29c8a0ea2b81bebde | Q2 2026 release (supporting) |
| context | 9e4b4c779a926897468f1dfd198d157aa081551eb0aa185c7568e6564f764c9f | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2571b7e9360f6c0ea273bba21e1fe841a47b3e684ddd02e1c3fe019c258d1214 | Audited: source readiness |
| CP-1 | e7bf0105a6381159660f32f084ad2d84b72887c85873222b32d56f78e390c03a | Audited: financial base |
| CP-1A | 21eb99c584632d91dd42b4835fe7a097eb792187905675c81a189cd2ba4929e0 | Audited: business and transaction context |
| CP-2 | 0c07843c9e5b2ee080f513bd7922e064b51bb784a582911dd98b898521572206 | Audited: fundamental credit synthesis |

Locators are `page:N` of the pinned `.jsonl` text and appear only in the appendix and calculation tables. Consistency with the audited handoffs: this answer confirms CP-0, CP-1, CP-1A and CP-2 on every figure it recomputed and corrects the two statements named in the findings below. The earlier handoffs cannot be edited, so each correction is stated here for the next reader.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The research traces to the filings and every recomputed figure matched. Committee use is restricted because two statements in the credit work go beyond the evidence on covenant capacity and preferred stock ranking. | Medium | Preferred stock terms and executed debt agreements are not supplied, so legal and covenant claims rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Recomputed leverage matched: 6.13x non-funding debt to equity and 7.64x last-twelve-months Adjusted EBITDA. | Headline leverage can be relied on as arithmetic from company-defined measures. | High |
| Interest cover of 2.92x uses accrued interest on non-funding debt, because cash interest is not reported separately. | Treat cover as a proxy; cash cover could differ. | Medium |
| The credit work suggested new debt would rely on permitted baskets and called the preferred junior to debt, without the indentures or certificate. | Debt capacity and ranking remain unsupported until the agreements are read. | Medium |
| Liquidity of 1,277.4 million recomputed, but 300.0 million of undrawn lines is uncommitted while the chart label says committed. | Headroom depends on lenders; the label should not be read literally. | Medium |
| Three source conflicts remain logged, including the 2.05 billion headline against 1.65 billion closed. | Model only the closed 1.65 billion until the documents are reconciled. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 is an insufficient-information item. Every figure recomputed from the filings matched, and each source conflict is logged rather than smoothed. The most important provenance gap is the missing certificate of designation and warrant terms for the August 5, 2026 preferred issue, which matters because redemption or protective rights could decide whether the 1,650.0 million is a buffer for creditors or a competing claim, and implies committee use stays restricted until those terms and the debt agreements are supplied. Two statements in the context and synthesis handoffs overreach on covenant capacity and preferred ranking; they are corrected here.

### Traceability summary

| Rank | Credit driver | Classification | Traceability status | Most important gap |
| --- | --- | --- | --- | --- |
| 1 | Leverage on equity and growth in non-funding debt | Directly Sourced | Committee-Ready | Indenture definitions of the incurrence ratios |
| 2 | Earnings quality: hedge losses excluded from Adjusted EBITDA | Calculated | Committee-Ready | Hedge intent and remaining position not described |
| 3 | Liquidity and funding structure | Calculated | Remediation Needed | Facility agreements; chart label says committed |
| 4 | August 5, 2026 preferred raise | Insufficient Information | Remediation Needed | Certificate of designation and warrants |
| 5 | Control and related-party structure | Directly Sourced | Committee-Ready | Agreements behind the revolver subordination and Tax Receivable Agreement |

### Audit summary and clearance

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 9. Committee Use: Restricted.

No finding changes a reported figure or the direction of the credit view, so none is Critical. Two Material findings (CP5-001 and CP5-002) are legal-meaning overreaches in the business-context and synthesis handoffs that must be disclosed or removed before committee use. The computed confidence score is 0 of 100 in the band Insufficient Information, with qa_status Restricted and committee status Restricted; the score is set by the method's penalty arithmetic (two Material findings at 15 each and nine Minor findings at 3 each, against a source gate of partial), not by any failed recomputation. See Calculations for the working.

### Corrections stated for earlier handoffs

- CP-2 (Leverage scenarios table): the remark that the company's ratios suggest new non-funding debt would rely on permitted baskets is withdrawn. Capacity under the indenture tests is Not Calculable without the indenture definitions.
- CP-1A (Credit translations, Hybrid capital) and CP-2 (Reader summary, Weaknesses): the descriptions of the preferred as a junior claim to debt, and of its rights as possibly ranking ahead of creditor interests, are withdrawn. Ranking, redemption and protective terms are unknown because the certificate of designation is not supplied.
- CP-1A (Governance and sponsor behaviour): the 2025 exchange volume should read 65,953,003 units exchanged and sold, within 108,849,478 Class D shares converted.
- CP-1 (chart tables): the interest cover cells are accrual-based, the undrawn column includes uncommitted lines, and "total debt" in the leverage chart is non-funding debt.

### Remediation priority map

Must-fix before committee: CP5-001 (remove or label the inference that new non-funding debt would rely on permitted baskets, and show the indenture ratio definitions or mark capacity Not Calculable) and CP5-002 (state that the ranking, redemption and protective terms of the Series A-1 and A-2 preferred are unknown and that no ranking relative to debt is asserted).

Must-fix before the handoff is consumed downstream: CP5-003 (rename the interest cover chart cell or mark it Not supplied: cash interest on non-funding debt is not reported separately), CP5-004 (relabel the undrawn facilities column to show it includes 300.0 million of uncommitted lines and a revolver whose commitment status is not stated) and CP5-005 (label the leverage chart as non-funding debt and state both liquidity bases).

Monitoring follow-up: CP5-008 (read the indentures, facility agreements, Tax Receivable Agreement and certificate of designation when supplied), CP5-009 (add trading levels for the notes if a market view is later requested) and CP5-006 (restate the 2025 exchange volume).

Formatting and hygiene: CP5-007 (qualify or remove the unsupported adjectives), CP5-010 (add a YAML front-matter envelope if the downstream consumer needs one) and CP5-011 (remove repeated limitation text).

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_uwmc-20251231.htm.jsonl | Audited filing, primary (opinion dated February 25, 2026) | FY2025, FY2024, FY2023 | UWM Holdings Corporation, consolidated | Statements, notes, Adjusted EBITDA reconciliation, risk factors on control and Tax Receivable Agreement, merger note | Text extraction only; Adjusted EBITDA unaudited | Annual base, ownership, merger history |
| S2 | 10-Q_2025-09-30_uwmc-20250930.htm.jsonl | Unaudited filing, primary | Q3 2025 | Consolidated | Q3 2025 Adjusted EBITDA | Interim | Quarterly cross-check |
| S3 | 10-Q_2026-03-31_uwmc-20260331.htm.jsonl | Unaudited filing, primary | Q1 2026 | Consolidated | Statements, facility balances, merger termination wording | Interim; termination date and fee not stated | Q1 figures, LTM |
| S4 | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | Unaudited filing, primary | Q2 2026, H1 2026 | Consolidated | Statements, debt, covenants, liquidity, subsequent events | Interim; subsequent event summarised only | Current-period base |
| S5 | EX-99.1_2026-02-26_irdeck4q25andfy2025-fina.htm.jsonl | Management presentation, supporting | February 2026, FY2025 | Consolidated | Non-funding debt and Adjusted EBITDA appendix | Slide text only; charts not inspected | Dec 31, 2025 non-funding debt check |
| S6 | EX-99.1_2026-05-06_q12026ex-991pressrelease.htm.jsonl | Management release, supporting | Q1 2026 | Consolidated | Q1 2026, Q4 2025 and Q1 2025 Adjusted EBITDA; non-funding debt | Management prepared | LTM Adjusted EBITDA inputs |
| S7 | EX-99.1_2026-08-05_q22026ex-991pressrelease.htm.jsonl | Management release, supporting | Q2 2026 | Consolidated | Non-funding debt, liquidity claim, five-quarter addendum, Oaktree headline | Management prepared; headline differs from the filing | Cross-checks and conflict log |
| S8 | context | Run settings, not evidence | As of 2026-11-05 | Run | As-of date, currency, periods | Ratings, quotes, valuation blank | Scope |
| H0 | CP-0 handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Source readiness | Host authored | Scope and limits |
| H1 | CP-1 handoff | Analyst handoff | FY2025 to Q2 2026 | Consolidated | Financial base | Host authored | Audited here |
| H1A | CP-1A handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Business and transaction | Host authored | Audited here |
| H2 | CP-2 handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Credit synthesis | Host authored | Audited here |

Module Status: Ready with Limitations (all four handoffs present; executed agreements, preferred terms and post-August 7, 2026 filings are not supplied). Traceability Scope: Top 5. Entity key: issuer_id uwmc available. Upstream re-anchor: run_id `uwmc-2026-11-05-credit_snapshot-host`, reporting period Q2 2026 with FY2025 comparatives, all four handoffs accepted by the launcher with the hashes listed in Sources.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage on equity and growth in non-funding debt: 6,040.4 million, 6.13x equity, 7.64x LTM Adjusted EBITDA | CP-1, CP-2 | Balance sheet lines and the company's non-funding debt table | Secured draws of 1,750.0 million lifted debt while equity fell, shrinking the cushion beneath refinancing and loss given default | Leverage tolerance and monitoring posture | S4 page:2, page:3, page:38; S7 page:5 to page:6 | Company non-GAAP measure; indenture ratio definitions not supplied |
| 2 | Earnings quality: Q2 2026 net loss of 451.9 million against Adjusted EBITDA of 185.9 million, and 526.8 million of excluded losses over the last twelve months | CP-1, CP-2 | Adjusted EBITDA reconciliation and statements of operations | Equity is exposed to hedge and valuation moves that the headline earnings measure removes | Which earnings measure to underwrite | S4 page:3, page:38, page:44 to page:45; S1 page:90 | Hedge intent and ratio not described |
| 3 | Liquidity and funding structure: 1,277.4 million of headroom, 300.0 million uncommitted, 900.0 million of committed warehouse capacity, cross-default across lines | CP-1, CP-2 | Facility notes and liquidity discussion | Short-dated, collateral-based funding can shrink in a rate shock, and 2,375.0 million of non-funding debt falls due in 2027 | Liquidity, refinancing | S4 page:14 to page:16, page:19, page:48 to page:55 | Facility agreements not supplied; availability depends on advance rates |
| 4 | August 5, 2026 preferred and warrant raise of 1,650.0 million with 10.0% cash or 13.0% non-cash dividends | CP-1A, CP-2 | Subsequent-event note | Adds loss-absorbing capital but also a fixed junior claim with unknown redemption rights | Whether the raise helps or competes with creditors | S4 page:32 to page:33; S7 page:1 | Certificate of designation, warrants, use of proceeds not supplied |
| 5 | Control and related-party structure: SFS Corp. holds 78.7% of Holdings LLC, lends the revolver, receives distributions and Tax Receivable Agreement payments | CP-1A, CP-2 | Ownership note, risk factors, related-party note | Owner interests can differ from creditors on distributions and change of control | Governance and sponsor alignment | S4 page:6, page:19, page:21, page:22 to page:23, page:27; S1 page:71, page:73 | Agreements not supplied; voting figure is as of the 10-K |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Non-funding debt 6,040.4, equity 985.3, ratio 6.13x | CP-1, CP-2 | `Total non-funding debt $ 6,040,429`, `Non-funding debt to equity 6.13` (S7 page:5 to page:6); balance sheet lines S4 page:2 to page:3 | Yes | Filing and release agree | Directly Sourced | Verified | High | Committee-Ready |
| Debt up 1,747.5 and equity down 608.3 in six months | CP-1, CP-2 | 6,040,429 less 4,292,940; 985,308 less 1,593,629 (S4 page:2 to page:3; S5 page:12) | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| LTM Adjusted EBITDA 790.6; 7.64x and 6.16x | CP-1, CP-2 | 697,336 + 346,787 - 253,485 (S1 page:90; S4 page:38) | Yes | Filing, company non-GAAP | Calculated | Recomputed | High | Committee-Ready |
| Cover 2.92x and 3.25x on accrued non-funding interest | CP-1, CP-2 | 790,638 / 271,195; 697,336 / 214,513 (S4 page:38; S1 page:90) | Yes | Filing | Calculated | Recomputed; accrual proxy | Medium | Remediation Needed |
| Q2 net loss 451.9, Adjusted EBITDA 185.9, derivative loss 603.2 | CP-1, CP-2 | S4 page:3, page:38 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Excluded valuation and derivative items net 526.8 (LTM) and 538.1 (Q2) | CP-1, CP-2 | 65,056 - 603,191; 312,953 - 741,389; FY2025 and H1 2025 items | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| Hedge programme lost money net in Q2 | CP-2 | Same figures; hedge ratio not stated | Partial | Filing | Analyst Inference | Labelled interpretation | Medium | Committee-Ready |
| H1 2026 operating cash flow -1,885.8; -1,084.8 with MSR sale proceeds | CP-1, CP-2 | S4 page:4 to page:5 | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| Secured draws exceeded servicing-rights growth, so part financed operations and distributions | CP-2 | 1,750.0 against 1,237.7 (S4 page:5, page:12) | Partial | Filing | Analyst Inference | Labelled interpretation | Medium | Committee-Ready |
| Liquidity 1,277.4 (company basis 1.3 billion) | CP-1, CP-2 | 477,407 + 125,000 + 175,000 + 500,000 (S4 page:2, page:15 to page:16, page:19; S7 page:1) | Yes | Filing and release agree | Calculated | Recomputed | Medium | Remediation Needed |
| 300.0 uncommitted; 900.0 committed warehouse; cross-default | CP-1, CP-2 | S4 page:15 to page:16, page:52, page:54 | Yes | Filing description | Directly Sourced | Verified | Medium | Committee-Ready |
| 2027 maturities 2,375.0; warehouse advances 5,090.8 expiring by May 14, 2027 | CP-1, CP-2 | S4 page:14, page:17, page:16 | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| SFS Corp. 78.7% of units and about 79% of votes | CP-1A, CP-2 | S4 page:23; S1 page:73 | Yes | Filing; voting figure dated to the 10-K | Directly Sourced | Verified | High | Committee-Ready |
| Tax Receivable Agreement 280.0 and change-of-control acceleration | CP-1A, CP-2 | S4 page:21; S1 page:71 | Yes | Filing summary | Directly Sourced | Verified | Medium | Committee-Ready |
| Cash paid to equity holders 321.8 against net loss 281.5 | CP-1A, CP-2 | 59,867 + 261,896 (S4 page:5) | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| Governance behaviour Neutral or Mixed | CP-1A, CP-2 | Documented actions in S4 page:19, page:32, page:59 | Yes | Filing | Analyst Inference | Labelled interpretation | Medium | Committee-Ready |
| Preferred 1,650.0, 10.0% or 13.0%, warrants, 400 contingent rights offering | CP-1A, CP-2 | S4 page:32 to page:33 | Yes | Filing note | Directly Sourced | Verified | Medium | Committee-Ready |
| Preferred redemption, ranking and protective terms | CP-1A, CP-2 | None in the sources | No | No source | Insufficient Information | Gap flagged | Low | Not Traceable |
| Pro forma leverage 2.29x, 1.67x, 4.46x | CP-2 | 6,040,429 and 985,308 with 1,650,000 | Yes | Arithmetic | Assumption-Based | Recomputed; labelled illustrative | Low | Remediation Needed |
| Preferred raise acts as a buffer for creditors | CP-2 | Depends on missing terms | Partial | Filing note | Analyst Inference | Labelled interpretation | Low | Remediation Needed |
| Two Harbors agreement terminated and fee received | CP-1A | S3 page:37, page:42 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Termination date, reason and fee amount | CP-1A | None in the sources | No | No source | Insufficient Information | Gap flagged | Low | Not Traceable |
| Agency minimums 743.6 and 343.9; equity gap 241.7 and cash gap 133.5 as proxies | CP-2 | S4 page:23 against consolidated figures | Yes | Filing; perimeter differs | Assumption-Based | Recomputed; labelled proxy | Low | Remediation Needed |
| Second-quarter run-rate cover 2.14x | CP-2 | 185,879 x 4 over 86,810 x 4 (S7 page:5) | Yes | Filing | Assumption-Based | Recomputed; single-quarter annualisation | Low | Committee-Ready |
| Incurrence tests suggest new debt would rely on baskets | CP-2 | S4 page:54 thresholds only; definitions absent | Partial | Filing summary | Analyst Inference | Flagged; overreach | Low | Remediation Needed |
| Headline 2.05 billion against 1.65 billion closed plus 400 contingent | CP-1A, CP-2 | S7 page:1; S4 page:32 to page:33 | Yes | Two spans differ | Conflicting | Logged by CP-1A, not reconciled | Medium | Remediation Needed |
| Conventional facility covenant set (maximum debt to net worth present or absent) | CP-0, CP-1 | S4 page:16; page:54 | Yes | Two spans differ | Conflicting | Logged, not reconciled | Medium | Remediation Needed |
| Q1 2026 purchase jumbo originations 1,443,526 or 1,143,526 | CP-1A | S6 page:2; S7 page:3; S4 page:40 | Yes | Two releases differ | Conflicting | Logged; the Q1 release and the 10-Q agree | Medium | Remediation Needed |
| Substantially all servicing in-house by October 2026 | CP-1A, CP-2 | S6 page:2 | Yes | Management release | Directly Sourced | Management statement, not adopted | Medium | Committee-Ready |
| Other interest rate derivatives 12,805.0 notional and exited positions | CP-1A, CP-2 | S4 page:11, page:60 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Senior notes: 4 series, carrying 2,984,328, principal 3,000,000, rates, maturities | packs/1783398-uwm-holdings-corp-uwmc/10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:17, Note 7 | CP-1 debt table | Sourced | Filing | Opened; sums to 3,000,000 |
| Warehouse lines 8,600,078 across 11 repurchase agreements and early funding; 900.0 million committed | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:14 to page:15, Note 6 | CP-1 debt table, expiries | Sourced | Filing | Opened; expiries sum 5,090,756 by May 14, 2027 |
| Conventional facility 1,875,000 drawn, limit 2.0 billion, July 15, 2027; Ginnie Mae 1,075,000, limit 1.25 billion, March 20, 2029 | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:15 to page:16 | CP-1 debt, liquidity | Sourced | Filing | Sum of drawn equals secured lines 2,950,000 |
| Q1 2026 limits 1.5 billion and 900.0 million | packs/.../10-Q_2026-03-31_uwmc-20260331.htm | 10-Q_2026-03-31_uwmc-20260331.htm.jsonl | S3 | page:14 to page:16 | CP-1 liquidity | Sourced | Filing | The Citibank warehouse line of 500 million (June 26, 2026) became nil with the combined 2.0 billion allocated to the servicing-rights facility, which supports the reallocation reading |
| Revolver 500.0 million, SFS Corp., undrawn, subordinated | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:19, page:27 | CP-1, CP-1A | Sourced | Filing | Agreement not supplied |
| Adjusted EBITDA Q2 185,879; H1 346,787; H1 2025 253,485; FY2025 697,336 | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4, S1 | S4 page:38; S1 page:90 | CP-1 | Sourced | Filing, non-GAAP | Reconciliation foots in each column |
| Adjusted EBITDA Q1 2025 57,803; Q4 2025 232,778; Q3 2025 211,073 | packs/.../EX-99.1_2026-05-06_q12026ex-991pressrelease.htm | EX-99.1_2026-05-06_q12026ex-991pressrelease.htm.jsonl | S6, S2 | S6 page:5 to page:6; S2 page:40 | CP-1 LTM cross-check | Sourced | Release; filing | Four-quarter sum differs by 1 |
| H1 2026 operating cash flow -1,885,842; MSR sale proceeds 801,013; dividends 59,867; distributions 261,896 | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:4 to page:5 | CP-1 cash flow | Sourced | Filing | Operating items bridge to the statement |
| FY2025 operating cash flow -2,647,557; cash paid for interest 496,248 | packs/.../10-K_2025-12-31_uwmc-20251231.htm | 10-K_2025-12-31_uwmc-20251231.htm.jsonl | S1 | page:129 | CP-1 | Sourced | Audited | Confirmed |
| Cash 498,407 including restricted 21.0 million | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:2 | CP-1 liquidity | Sourced | Filing | The Q1 10-Q prints 16.0 million for the December 31, 2025 comparative, against 21.0 million in the 10-K, noted in CP-1 |
| About 1.3 billion of available liquidity | packs/.../EX-99.1_2026-08-05_q22026ex-991pressrelease.htm | EX-99.1_2026-08-05_q22026ex-991pressrelease.htm.jsonl | S7 | page:1 | CP-1, CP-2 | Sourced (Management Language) | Release | Recomputed to 1,298.4 including restricted cash |
| UWMC 342,247,135 units (21.3%), SFS Corp. 1,261,862,603 (78.7%) | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:22 to page:23, Note 11 | CP-1A | Sourced | Filing | Confirmed |
| About 79% of voting power; 99% without the Voting Limitation | packs/.../10-K_2025-12-31_uwmc-20251231.htm | 10-K_2025-12-31_uwmc-20251231.htm.jsonl | S1 | page:73 | CP-1A, CP-2 | Sourced | Filing | Dated to the 10-K |
| Tax Receivable Agreement liability 279,995 and change-of-control payment | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4, S1 | S4 page:21; S1 page:71 | CP-1A, CP-2 | Sourced | Filing | Agreement not supplied |
| Preferred issue terms, warrants, investor rights, rights offering | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:32 to page:33, Note 18 | CP-1A, CP-2 | Sourced | Filing summary | Redemption terms described as existing but not given |
| Headline 2.05 billion equity investment | packs/.../EX-99.1_2026-08-05_q22026ex-991pressrelease.htm | EX-99.1_2026-08-05_q22026ex-991pressrelease.htm.jsonl | S7 | page:1 | CP-1A | Conflicting | Release | Logged in CP-1A |
| Merger Agreement December 17, 2025: 2.3328 shares, about 247 million shares | packs/.../10-K_2025-12-31_uwmc-20251231.htm | 10-K_2025-12-31_uwmc-20251231.htm.jsonl | S1 | page:140, page:74 | CP-1A | Sourced | Filing | Confirmed |
| Merger agreement terminated; fee received in Q1 2026 | packs/.../10-Q_2026-03-31_uwmc-20260331.htm | 10-Q_2026-03-31_uwmc-20260331.htm.jsonl | S3 | page:37, page:42 | CP-1A | Sourced | Filing | Date, fee and reason not stated |
| Agency minimums: net worth 743.6 million, liquidity 343.9 million, 6% capital | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:23, Note 12 | CP-1, CP-2 | Sourced | Filing | UWM-level actuals not printed |
| Cross-default; daily collateral evaluation; mandatory curtailments | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:50, page:52, page:54 to page:55 | CP-1, CP-2 | Sourced | Filing description | Agreements not supplied |
| Incurrence thresholds 3.0 to 1.0 and 2.0 to 1.0 | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:54 | CP-1, CP-2 | Sourced | Filing summary | Definitions absent |
| Servicing-rights roll-forward and sensitivities | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:12 to page:14, Note 5 | CP-1, CP-2 | Sourced | Filing | Roll-forward foots to 5,311,465 |
| Other interest rate derivatives notional 12,805,000; positions exited | packs/.../10-Q_2026-06-30_uwmc-20260630.htm | 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | S4 | page:11, page:60 | CP-1, CP-1A | Sourced | Filing | Hedge intent not described |
| Related-party net payments 32,921 in FY2025 | packs/.../10-K_2025-12-31_uwmc-20251231.htm | 10-K_2025-12-31_uwmc-20251231.htm.jsonl | S1 | page:161 | CP-1A, CP-2 | Sourced | Audited | Lines sum to 32,922; rounding of 1 |
| 65,953,003 units exchanged and sold in 2025; 108,849,478 Class D shares converted | packs/.../10-K_2025-12-31_uwmc-20251231.htm | 10-K_2025-12-31_uwmc-20251231.htm.jsonl | S1 | page:73; page:128 | CP-1A | Sourced; partially | Audited | CP-1A cites only the first figure as "exchanged" |
| Substantially all servicing in-house by October 2026 | packs/.../EX-99.1_2026-05-06_q12026ex-991pressrelease.htm | EX-99.1_2026-05-06_q12026ex-991pressrelease.htm.jsonl | S6 | page:2 | CP-1A | Sourced (Management Language) | Release | Not adopted |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Non-funding debt | CP-1, CP-2 | 2,984,328 + 2,950,000 + 83,660 + 22,441 (US$ thousands, June 30, 2026) | Sum of four balance sheet lines | Calculated | Recomputed: 6,040,429, equals printed | High | Leverage | S4 page:2; S7 page:5 to page:6 |
| Non-funding debt to equity | CP-1, CP-2 | 6,040,429 / 985,308; 4,292,940 / 1,593,629 | Division, June 30, 2026 and December 31, 2025 | Calculated | Recomputed: 6.13x and 2.69x, equal printed | High | Leverage | S4 page:2 to page:3; S5 page:12 |
| LTM Adjusted EBITDA | CP-1, CP-2 | 697,336 + 346,787 - 253,485 | FY2025 + H1 2026 - H1 2025 | Calculated | Recomputed: 790,638 | High | Leverage, coverage | S1 page:90; S4 page:38 |
| Non-funding debt / LTM Adjusted EBITDA | CP-1, CP-2 | 6,040,429 / 790,638; 4,292,940 / 697,336; 5,092,831 / 800,442 | Division | Calculated | Recomputed: 7.64x, 6.16x, 6.36x | High | Leverage | As above |
| Net non-funding debt / LTM Adjusted EBITDA | CP-1 | Unrestricted cash 477,407; 482,364; 402,996 | (Debt - cash less 21,000 restricted) / EBITDA | Calculated | Recomputed: 7.04x, 5.46x, 5.86x | Medium | Leverage | S4 page:2 |
| Adjusted EBITDA / interest on non-funding debt | CP-1, CP-2 | 790,638 / 271,195; 697,336 / 214,513 | Accrual interest from the reconciliation | Calculated | Recomputed: 2.92x, 3.25x; denominator is not cash interest | Medium | Coverage | S4 page:38; S1 page:90 |
| Excluded valuation and derivative items | CP-1, CP-2 | 65,056 - 603,191; 312,953 - 741,389; -435,267 + 298,126; -247,667 + 208,904 | Net of the two reconciling items | Calculated | Recomputed: -538,135 (Q2), -428,436 (H1 2026), -137,141 (FY2025), -38,763 (H1 2025), -526,814 (LTM) | High | Earnings quality | S4 page:38; S1 page:90 |
| LTM net loss | CP-1 | 244,023 - 281,528 - 67,451 | FY2025 + H1 2026 - H1 2025 | Calculated | Recomputed: -104,956 | High | Earnings | S1 page:128; S4 page:3 |
| Operating cash flow plus net MSR sale proceeds | CP-1, CP-2 | -1,885,842 + 801,013; 328,022 + 1,591,780 | Sum | Calculated | Recomputed: -1,084,829 and 1,919,802; not a company measure | High | Liquidity | S4 page:4 to page:5 |
| Cash paid to equity holders | CP-1A, CP-2 | 59,867 + 261,896 | Sum | Calculated | Recomputed: 321,763 | High | Distributions | S4 page:5 |
| Liquidity | CP-1, CP-2 | Cash 477,407; undrawn 125,000, 175,000, 500,000 | Cash (ex restricted) + limit - drawn by facility | Calculated | Recomputed: 1,277,407; company basis 1,298,407 | Medium | Liquidity | S4 page:2, page:15 to page:16, page:19 |
| 2027 maturities and 2027 repayments against liquidity | CP-1, CP-2 | 500,000 + 1,875,000; against 1,277,407 | Sum; ratio | Calculated | Recomputed: 2,375,000; 185.9% | High | Refinancing | S4 page:17, page:16 |
| Warehouse expiries by May 14, 2027 | CP-1, CP-2 | Eight advanced balances | Sum | Calculated | Recomputed: 5,090,756 (59.2% of 8,600,078) | High | Refinancing | S4 page:14 |
| Preferred dividends at stated rates | CP-2 | 1,650.0 million x 10.0% and 13.0% | Product on original issue price | Calculated | Recomputed: 165.0 and 214.5; not a reported figure | Medium | Debt service | S4 page:32 |
| Pro forma non-funding debt to equity | CP-2 | Three scenarios on 1,650.0 | Division with stated assumptions | Assumption-Based | Recomputed: 2.29x, 1.67x, 4.46x; fees and classification unknown | Low | Leverage | S4 page:32 to page:33 |
| Equity and cash against agency minimums | CP-2 | 985.3 - 743.6; 477.4 - 343.9 | Subtraction | Assumption-Based | Recomputed: 241.7 and 133.5; consolidated proxy for UWM | Low | Regulatory | S4 page:23 |
| Servicing-rights sensitivities as a share of equity | CP-2 | 207,202, 398,315, 200,467 over 985,308 | Division | Calculated | Recomputed: 21.0%, 40.4%, 20.3% | Medium | Equity risk | S4 page:13 to page:14 |
| Second-quarter run-rate cover | CP-2 | 185,879 x 4 / 86,810 x 4 | Annualise one quarter | Assumption-Based | Recomputed: 2.14x | Low | Coverage | S7 page:5 |
| Warrants against economic shares | CP-1A | 330 million / (342.3 + 1,261.9) million | Division | Calculated | Recomputed: 20.6% | Medium | Dilution | S4 page:1, page:32 |

Definition drift flagged: the chart label "EBITDA / cash interest" is used for the accrual ratio (CP5-003); the chart label "Total debt" is used for non-funding debt (CP5-005); "undrawn committed facilities" includes uncommitted lines (CP5-004). No drift in the Adjusted EBITDA definition across modules.

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | New non-funding debt would rely on permitted baskets | Inferred from thresholds without definitions (CP5-001) | Analyst Inference | Debt capacity and creditor protection depend on indenture definitions; an unsupported inference could understate or overstate capacity | Remove, or mark Not Calculable and cite the indentures when supplied | CP-2 Leverage scenarios table |
| Material | Preferred is a fixed claim junior to debt and could rank ahead of creditor interests in practice | Ranking stated without the certificate of designation (CP5-002) | Analyst Inference | Ranking and redemption terms decide whether the raise supports or competes with creditors | State no ranking until terms are supplied | CP-1A Credit translations; CP-2 Reader summary and Weaknesses |
| Minor | Preferred redemption, ranking and protective terms | Terms not supplied; logged in CP-1A and CP-2 | Insufficient Information | Same as above | Obtain the 8-K exhibits | CP-1A, CP-2 gaps; tracked as CP-5-GAP-001 |
| Minor | Termination date, reason and fee amount of the Two Harbors agreement | Not in the sources; logged in CP-1A | Insufficient Information | Affects reading of capital allocation | Obtain the termination 8-K | CP-1A; tracked as CP-5-GAP-005 |
| Minor | Headline 2.05 billion against 1.65 billion plus 400 contingent | Two spans differ; logged | Conflicting | Wrong size would overstate closed capital | Use the filing split | CP-1A, CP-2 |
| Minor | Conventional facility covenant set | Two spans differ; logged | Conflicting | Wrong covenant set misstates restrictions | Obtain the agreement | CP-0, CP-1 |
| Minor | Q1 2026 jumbo originations | Two releases differ; the 10-Q arithmetic supports 1,443,526; logged | Conflicting | No credit metric affected | None beyond the log | CP-1A |
| Minor | Pro forma leverage scenarios and agency proxies | Assumptions labelled illustrative | Assumption-Based | Scenario figures could be mistaken for forecasts | Keep the labels | CP-2 |
| Minor | Hedge programme lost money net; hedge intent unknown | Interpretation of reconciled figures | Analyst Inference | Equity risk from hedging | Obtain management disclosure | CP-2 |

No orphan claim (VE-015) is triggered: every Insufficient Information and Analyst Inference conclusion above is either flagged in the audited handoff or listed here with remediation. The ranking statements in CP-2's key credit risks table (CP5-002) lacked a flag in that row and are corrected here.

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 to Q2 2026 and the August 5, 2026 event in summary; no agreements or later filings | Legal and covenant claims rest on filing descriptions | Covenant headroom and preferred ranking cannot be committee-grade | Supply agreements and the 8-K exhibits |
| Citation completeness | Ready with Remediation | Tables carry page locators; a few prose statements cite handoffs rather than pages | A reader cannot trace some narrative statements in one step | Slower committee challenge | Add page locators to narrative sentences when republishing |
| Calculation traceability | Committee-Ready | Every derived figure shows formula and inputs; all 19 register items recomputed | Low risk of arithmetic error | Leverage and liquidity figures can be relied on | Relabel the accrual cover and the committed column |
| Assumption transparency | Ready with Remediation | Scenarios and proxies are labelled; two inferences are not | Unlabelled inference can read as fact | Debt capacity and ranking could be misread | Remove CP5-001 and CP5-002 statements |
| Markdown/export artifact integrity | Ready with Remediation | Six H2 headings, reader summary and opening view present; no YAML front matter | Downstream parsers expecting an envelope would miss fields | Handoff consumption risk only | Add an envelope if required |

Overall auditability: Ready with Remediation (the lowest assessment across the five dimensions).

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Preferred stock terms: ranking, redemption, protective rights, warrants | Certificate of designation, warrant agreements, investor rights agreement | Decides whether the raise is a buffer or a competing claim | CP-1A, CP-2 credit view and scenarios | High impact | Form 8-K exhibits for August 5, 2026 |
| CP-5-GAP-002 | Executed indentures, facility agreements, revolver and Tax Receivable Agreement | The agreements listed in the 10-K exhibit index | Covenant levels, definitions, baskets, cross-default and change-of-control terms | CP-2 covenant and legal claims | High impact | Exhibit documents |
| CP-5-GAP-003 | Use of proceeds, fees and balance sheet classification of the preferred | Next 10-Q or 8-K | Pro forma leverage and liquidity | CP-2 scenarios | High impact | Third quarter 2026 report |
| CP-5-GAP-004 | Events between August 7, 2026 and 2026-11-05 | Later filings, rights offering documents | Funding continuity and renewal of warehouse lines expiring September 29 and October 8, 2026 | All current-period conclusions | Medium impact | Later 8-Ks and 10-Q |
| CP-5-GAP-005 | Two Harbors termination date, reason and fee | Termination 8-K | Capital allocation reading | CP-1A | Low impact | Termination 8-K |
| CP-5-GAP-006 | Cash interest on non-funding debt | Not reported separately | Cash cover cannot be computed | CP-1, CP-2 coverage | Medium impact | Management disclosure |
| CP-5-GAP-007 | UWM-level net worth and liquidity against agency minimums | Not printed | Regulatory headroom proxy only | CP-2 | Medium impact | Agency compliance data |
| CP-5-GAP-008 | Hedge intent, ratio and remaining position | Not described | Hedge volatility cannot be sized | CP-2 | Medium impact | Management disclosure |
| CP-5-GAP-009 | Trading levels, spreads, yields, ratings | Context blank; none in sources | No market-implied view | None used | Low impact | Market data if later requested |
| CP-5-GAP-010 | Rights offering launch and result | Expiry November 12, 2026 is after the cutoff | Equity size beyond the closed 1.65 billion | CP-2 | Medium impact | Later filings |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/e9bbe5c7480f67ee43bc69ce1cae4eb4ff6015b30299ce9d55042e7ed77adf9c/1.response.md; uwmc-2026-11-05-credit_snapshot-host | Source readiness for four consumers | Filings, supporting releases | Six H2 headings, reader summary and readiness view present; no YAML front matter | Not previously audited | Verdicts READY_WITH_LIMITATIONS |
| CP-1 | requests/CP-1/055e8feb7bc4d7c5670ec32415468ca683f63d010bfa8500dfa7e80b77a78687/1.response.md; same run | Financial base FY2025 to Q2 2026 | Filings, company non-GAAP | Six H2 headings, reader summary, financial base view and four chart selectors present; no YAML | Not previously audited | Chart cells numeric |
| CP-1A | requests/CP-1A/6faf6a85a69949c8bcf62423064fa3f346c5a661c97a3a28a298b88bbf52823c/1.response.md; same run | Business, ownership, transaction | Filings; releases tagged Management Language | Six H2 headings, reader summary, business and transaction view, selector headings present; no YAML | Not previously audited | Three conflicts logged |
| CP-2 | requests/CP-2/478ca0f06af1b8a7f8c9dff4769a8f9df3fb53765214a63a468c4a959b17dfb6/1.response.md; same run | Fundamental credit synthesis | CP-1 and CP-1A, re-checked to filings | Six H2 headings, reader summary, credit view of 123 words, selector headings present; no YAML | Not previously audited | Inherited limitation: readiness judgment READY_WITH_LIMITATIONS |

Module Status: Ready with Limitations.

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A | Governance table: "SFS Corp. exchanged and sold shares ... (65,953,003 units exchanged in 2025)" | Partially Supported | The 10-K says 65,953,003 units were exchanged and sold; the equity statement shows 108,849,478 Class D shares converted in 2025 (S1 page:73; page:128). The handoff states only the smaller number as the exchange volume | Restate as 65,953,003 exchanged and sold, within 108,849,478 converted | Monitoring Follow-Up |

All other cited figures and quotes in the four handoffs were opened and found Supported or correctly labelled; the quotes in the CP-1A conflict table were matched to the page text exactly.

#### T5.3 Math / logic / definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 (used in CP-2) | Interest cover cells under the heading "EBITDA / cash interest" hold 2.92x, 3.40x and 3.25x | Denominator is accrued interest expense on non-funding debt, not cash interest; the basis text says so but the heading does not | None; cash interest on non-funding debt is not reported separately | Mark the cells "Not supplied: cash interest on non-funding debt is not reported separately" or rename the column in the report | Requires Calculation Rebuild |
| MINOR | CP-1 | Liquidity chart column "Undrawn committed facilities" holds 1,300.0, 900.0 and 800.0 | Includes uncommitted servicing-rights headroom (125.0 and 175.0 at June 30, 2026) and a revolver whose commitment status is not stated | None | Relabel as undrawn lines under the company's liquidity basis and state the uncommitted share | Monitoring Follow-Up |

#### T5.4 Legal / structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 | Reference to the indenture incurrence test: the company's ratios "sit on the wrong side of both numbers, which suggests new non-funding debt would rely on permitted baskets" | The four indentures with their definitions of Fixed Charge Coverage Ratio and Debt-to-Equity Ratio and the baskets | Definitions and baskets not supplied; the thresholds come from a filing summary (S4 page:54); the handoff already marks the test Not calculable and then infers capacity | Delete the inference; keep Not calculable | Yes: legal review of indentures |
| MATERIAL | CP-1A, CP-2 | CP-1A: preferred terms "create a fixed claim junior to debt"; CP-2: preferred is "a fixed junior claim" and its rights "could rank ahead of creditor interests in practice" | Certificate of designation and investor rights agreement | Ranking, redemption timing and protective provisions are described only as existing (S4 page:32); no ranking statement is supported either way | State that ranking and redemption terms are unknown and assert none | Yes: legal review of the certificate |
| MINOR | CP-1, CP-1A, CP-2 | Revolver subordination, Tax Receivable Agreement acceleration on change in control, cross-default and covenant sets | The revolver and its amendment, the Tax Receivable Agreement, the facility agreements | Supported by filing descriptions only (S4 page:19, page:52; S1 page:71); the handoffs disclose that agreements are not supplied | None beyond the existing disclosure | Yes: confirm against agreements |

#### T5.5 Relative value / market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Senior note fair value of 2,783.4 million against carrying 2,984.3 million, down 222.5 million from December 31, 2025 (S4 page:26) | Trading prices, spreads, yields, rating, comparables | These are the company's Level 2 estimates; no dated quotes are supplied and no relative value claim is made | Keep as a filing datapoint; add quotes if a market view is requested | None for the credit view; no RV conclusion exists |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | "Total debt" in the CP-1 leverage chart is non-funding debt, which excludes warehouse lines of 8,600.1 million; "liquidity" appears on two bases (1,277.4 with unrestricted cash and 1,298.4 with restricted cash) | No version conflict: the figures are consistent and each basis is disclosed | Label the leverage chart as non-funding debt and state both liquidity bases | Reader of the chart alone could read leverage as total-debt leverage |

No contradictory conclusions were found. Issuer name, perimeter (consolidated UWM Holdings Corporation, Up-C), period, Adjusted EBITDA definition, debt and liquidity figures, maturities, the three logged conflicts and the August 5, 2026 treatment agree across the four handoffs.

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Promotional or Non-Credit Language | "Large, agency-focused" and "Spread maturity profile" are used without immediate qualification; the scale is supported by origination volume but the adjective is not tied to it | Qualify with the figure or delete | Minor |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Duplicative / Immaterial Content | The preferred terms, the covenant conflict and the unsupplied agreements are restated in each handoff's gaps, view and summary | Keep one statement per handoff where it changes a conclusion | Minor |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Envelope | No YAML front matter and the six host-run H2 headings replace the canonical envelope headings; this follows the run's transport rule and the launcher accepted all four | Add an envelope only if a downstream consumer requires it | None for this run |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-2 | Covenant / Basket Overreach | Inference that new non-funding debt would rely on permitted baskets without indenture definitions | Delete the inference; keep Not calculable | Requires Legal Review | Open |
| CP5-002 | MATERIAL | CP-1A, CP-2 | Recovery / Ranking Overreach | Preferred described as junior to debt and as potentially ranking ahead of creditor interests, with no terms supplied | Assert no ranking; state terms unknown | Requires Legal Review | Open |
| CP5-003 | MINOR | CP-1 | Formula / Definition Drift | Accrual interest cover placed under a cash-interest heading | Mark Not supplied or rename | Requires Calculation Rebuild | Open |
| CP5-004 | MINOR | CP-1 | Formula / Definition Drift | Undrawn column labelled committed includes uncommitted lines | Relabel | Monitoring Follow-Up | Open |
| CP5-005 | MINOR | CP-1, CP-1A, CP-2 | Cross-Module Inconsistency | "Total debt" label for non-funding debt; two liquidity bases | Label both | Monitoring Follow-Up | Open |
| CP5-006 | MINOR | CP-1A | Partially Supported Claim | 2025 exchange volume stated as 65,953,003 units exchanged; 108,849,478 shares converted | Restate | Monitoring Follow-Up | Open |
| CP5-007 | MINOR | CP-2 | Promotional or Non-Credit Language | Unqualified adjectives | Qualify or delete | Formatting / Hygiene Only | Open |
| CP5-008 | MINOR | CP-1, CP-1A, CP-2 | Legal Support Gap | Revolver subordination, Tax Receivable Agreement acceleration, cross-default and covenant sets rest on filing descriptions | Confirm against agreements when supplied | Requires Legal Review | Open |
| CP5-009 | MINOR | CP-1 | Market Data Gap | Senior note fair values are issuer estimates; no quotes | Add quotes if a market view is requested | Requires Market Data Refresh | Open |
| CP5-010 | MINOR | CP-0, CP-1, CP-1A, CP-2 | canonical Markdown Handoff Integrity Defect | No YAML front matter; host-run headings | Add an envelope if needed | Formatting / Hygiene Only | Open |
| CP5-011 | MINOR | CP-0, CP-1, CP-1A, CP-2 | Duplicative / Immaterial Content | Repeated limitation text across handoffs | Reduce repetition | Formatting / Hygiene Only | Open |

#### Handoff envelope record for this answer

| Field | Value |
| --- | --- |
| module_id | CP-5 |
| run_id | uwmc-2026-11-05-credit_snapshot-host |
| issuer_id | uwmc |
| reporting_period | Q2 2026 (comparatives FY2025) |
| analysis_date | 2026-11-05 |
| confidence_score | 0 |
| confidence_band | Insufficient Information |
| qa_status | Restricted |
| committee_status | Restricted |
| limitation_flags | Preferred terms not supplied; executed agreements not supplied; no filing after August 7, 2026 |
| validation_warnings | Interest cover is an accrual proxy; liquidity chart label; two credit synthesis statements overreach |
| upstream_artifacts_used | CP-0, CP-1, CP-1A, CP-2 handoffs with the hashes in Sources |
| downstream_consumers | Report delivery for the credit snapshot |

## Calculations

### Recomputation record

Each handoff figure below was recomputed from the cited source lines (US$ thousands unless stated) and compared. The recomputation used the printed lines directly and did not use the handoffs' derived values.

| Figure | Source inputs | Recomputed | Handoff value | Match |
| --- | --- | --- | --- | --- |
| Non-funding debt, June 30, 2026 | 2,984,328 + 2,950,000 + 83,660 + 22,441 | 6,040,429 | 6,040,429 | Yes |
| Non-funding debt to equity | 6,040,429 / 985,308; 4,292,940 / 1,593,629 | 6.13x; 2.69x | 6.13x; 2.69x | Yes |
| Change in debt and equity | 6,040,429 - 4,292,940; 985,308 - 1,593,629 | +1,747,489; -608,321 | 1,747.5; 608.3 million | Yes |
| LTM Adjusted EBITDA | 697,336 + 346,787 - 253,485 | 790,638 | 790,638 | Yes |
| Non-funding debt / LTM Adjusted EBITDA | 6,040,429 / 790,638; 4,292,940 / 697,336 | 7.64x; 6.16x | 7.64x; 6.16x | Yes |
| Accrual cover | 790,638 / (214,513 + 157,537 - 100,855); 697,336 / 214,513 | 2.92x; 3.25x | 2.92x; 3.25x | Yes |
| Excluded valuation and derivative items, LTM | (-435,267 + 298,126) + (312,953 - 741,389) - (-247,667 + 208,904) | -526,814 | 526.8 million loss | Yes |
| LTM net income | 244,023 - 281,528 - 67,451 | -104,956 | 105.0 million loss | Yes |
| Operating cash flow plus MSR sale proceeds, H1 2026 | -1,885,842 + 801,013 | -1,084,829 | 1,084.8 million negative | Yes |
| Cash paid to equity holders, H1 2026 | 59,867 + 261,896 | 321,763 | 321.8 million | Yes |
| Liquidity | 498,407 - 21,000 + (2,000,000 - 1,875,000) + (1,250,000 - 1,075,000) + 500,000 | 1,277,407 | 1,277.4 million | Yes |
| Warehouse advances expiring by May 14, 2027 | 990,038 + 153,287 + 256,929 + 963,193 + 506,673 + 1,314,608 + 661,696 + 244,332 | 5,090,756 | 5,090.8 million | Yes |
| 2027 maturities | 500,000 + 1,875,000 | 2,375,000 | 2,375.0 million | Yes |
| Servicing-rights sensitivities over equity | 207,202, 398,315, 200,467 each over 985,308 | 21.0%, 40.4%, 20.3% | Same | Yes |
| Pro forma non-funding debt to equity | 6,040.4 / (985.3 + 1,650.0); (6,040.4 - 1,650.0) / (985.3 + 1,650.0); (6,040.4 - 1,650.0) / 985.3 | 2.29x; 1.67x; 4.46x | Same | Yes |
| Preferred dividends | 1,650.0 x 10.0%; 1,650.0 x 13.0% | 165.0; 214.5 | Same | Yes |
| Equity statement bridge, H1 2026 | -281,528 - 65,589 - 255,922 + 27,086 - 32,368 | -608,321 | Total equity change | Yes |
| Related-party payments FY2025 | 20,831 + 11,053 + 600 + 438 | 32,922 | 32,921 as printed | Rounding of 1, disclosed |
| Four-quarter Adjusted EBITDA | 211,073 + 232,778 + 160,909 + 185,879 | 790,639 | 790,638 | Rounding of 1, disclosed |

Direction checks: debt rose and equity fell (checked); the 2.92x cover is below the 3.25x of FY2025 (checked); fair value of the senior notes fell from 3,005,945 to 2,783,429 (checked); equity fell 615.6 million in Q2 2026 from 1,600.9 to 985.3 (checked). No superlative in the audited handoffs relies on an unsourced comparison except the management market-position claims, which CP-1A tags as Management Language and does not adopt.

### Confidence score

| Input | Value | Basis |
| --- | --- | --- |
| Material claims by strongest lineage (30) | Directly Sourced 9, Calculated 8, Assumption-Based 3, Analyst Inference 5, Conflicting 3, Insufficient Information 2 | T5B.3 rows |
| Required fields | 13 present of 13 | Handoff envelope record for this answer |
| Source gate | partial | Readiness is READY_WITH_LIMITATIONS; agreements and preferred terms absent |
| Findings | MATERIAL 2, MINOR 9 | T5.9 |
| Working (script) | score = clamp((0.6*65.67 + 0.4*100) * 0.7 - 57, 0, 100) = -1.42, so 0 | confidence_score.py output below |

Script output for the inputs above: E = 65.67 (19.7 weighted over 30 claims), C = 100, S = 0.7, P = 57 (2 x 15 + 9 x 3), raw score = -1.42, confidence_score = 0, band Insufficient Information, qa_status Restricted.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Preferred stock certificate of designation, warrants and investor rights agreement are not supplied (CP-5-GAP-001) | MATERIAL | CP-1A, CP-2 | Obtain the Form 8-K exhibits; until then assert no ranking or redemption position |
| Executed indentures, facility agreements, revolver and Tax Receivable Agreement are not supplied (CP-5-GAP-002) | MATERIAL | CP-2 | Obtain the agreements; legal review of covenant, cross-default and change-of-control terms |
| Use of proceeds, fees and classification of the preferred (CP-5-GAP-003) | MATERIAL | CP-2 | Third quarter 2026 report |
| No filing after August 7, 2026 and no outcome for the rights offering (CP-5-GAP-004, CP-5-GAP-010) | MINOR | All | Later filings |
| Cash interest on non-funding debt, UWM-level agency headroom, hedge intent, Two Harbors termination terms, trading levels (CP-5-GAP-005 to CP-5-GAP-009) | MINOR | CP-1, CP-1A, CP-2 | Follow-up sources as listed in the gaps ledger |
| This answer rests on the pinned text only; chart and image content of the February 2026 presentation was not inspected | MINOR | CP-5 | None needed for the figures audited |

## Next module

None; this is the last module of the selected set. Carry into delivery: committee use is restricted; present the interest cover as an accrual proxy, the undrawn column as including uncommitted lines, and the leverage chart as non-funding debt; assert no covenant capacity and no preferred ranking; model only the 1.65 billion as closed; and keep the three source conflicts logged.
