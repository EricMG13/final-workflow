## Request

This is the evidence trace and research-integrity review of the Post Holdings, Inc. handoffs as of 2026-11-05 (cutoff 2026-11-05), pathway credit_snapshot, run post-2026-11-05-credit_snapshot-host. It checks that each material claim in the source-readiness, financial base, business and synthesis handoffs rests on the pinned sources, that calculations reproduce, and that the modules tell one story. It does not change any credit conclusion or silently repair an earlier handoff; defects are logged with the fix required.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-09-30_post-20250930.htm.jsonl | d988e0426964cfec01029656ef227ac10adca18ba413287c184f18404a876a74 |
| 10-Q_2025-12-31_post-20251231.htm.jsonl | e9cc6f62805c1b1bab9b7edb1afd055ae5b09d286a5f5385add48be2adcd1950 |
| 10-Q_2026-03-31_post-20260331.htm.jsonl | 6ed320d389c86598b7ad5f845098fe00ce2f7584e166c2976b8679a029b0c42b |
| 10-Q_2026-06-30_post-20260630.htm.jsonl | 5c5310f7f925e1ac072ebdb2eef5ec580787271894d731c4b0f244a823ad7595 |
| EX-99.1_2026-02-03_ex99-1q12026er.htm.jsonl | 38e17081ebfa3fafaf0505f1bd57fb738f074e8b7b4014662d7731549585d17b |
| EX-99.1_2026-05-05_ex99-1q22026er.htm.jsonl | c699bde5529dd39cf184dac3c7c6fd8e1af3530dddd1b671a659bdd669e9f846 |
| EX-99.1_2026-08-06_ex99-1q32026er.htm.jsonl | fa25c942bbdfd0499284c17eaea7c77be614d163d4c3ae3f0600195efb353a9c |
| context (settings, not issuer evidence) | 42de786351216298f80706a9245ba3397a337baef9248bdb3ddc19ef12ef23d8 |

Locators use `page:N` source chunks. "10-K" is the FY2025 annual report; "Q1 10-Q", "Q2 10-Q" and "Q3 10-Q" are the quarterly reports for December 31, 2025, March 31, 2026 and June 30, 2026; "Q1 release", "Q2 release" and "Q3 release" are the matching EX-99.1 earnings releases.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 0207225cf916a688a599956fca0dbd3a4cedfd539e02ef72ef73b2252d375b67 |
| CP-1 | c6b89a2a1531678b1e29d8ad7188e3515d0f6ea89db4e21750fe77692e66f2ac |
| CP-1A | 850147f7553883b0637d4aa06699942089857cd17afafc82af67f14c70101a44 |
| CP-2 | b948db02d6ba8cd38678e35667d4f8cbafa5c9944a5179ffcc9177517ca76c9d |

All four were re-anchored to run post-2026-11-05-credit_snapshot-host, issuer Post Holdings, Inc., current period the fiscal third quarter ended June 30, 2026 and prior period the fiscal year ended September 30, 2025.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The numbers in the earlier work trace to the filings and recompute correctly. One causal claim about Foodservice earnings and avian influenza pricing is not supported and needs restating before committee use. | Medium | Legal terms, covenant definitions and post-quarter data are not in the sources, so those points cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every debt, liquidity, leverage and cash flow figure checked matched the source or recomputed exactly. | The leverage, liquidity and cash allocation conclusions can be relied on as stated. | High |
| The claim that about USD 60 million of Foodservice earnings above run rate comes from avian influenza pricing has no source support. | Earnings durability is uncertain, and the cause of the above-run-rate earnings is not established. | Medium |
| One page reference for the Bob Evans lease guarantee was off by one page. | No effect on any figure or conclusion. | High |
| Covenant headroom, guarantor detail and legal capacity cannot be traced because the executed documents were not supplied. | Protection for creditors is unverified. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 3 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting or insufficient-information items. The most important provenance gap is the attribution of Foodservice earnings above run rate to avian influenza pricing, which matters because the sources show avian influenza pricing falling and lowering Foodservice results while management gives no cause for the above-run-rate earnings, and it implies that the earnings-durability driver should be restated as inference before committee use. Committee use is Restricted: figures are reliable, but legal capacity and covenant headroom are untraceable. The Top 5 scope was used.

### Traceability summary

| Driver | Origin | Class | Traceability | Restriction | Cleared by |
| --- | --- | --- | --- | --- | --- |
| Leverage on adjusted and unadjusted EBITDA | Financial base | Calculated | Committee-Ready | Management EBITDA basis | Recomputation below |
| Liquidity and maturity wall | Financial base | Calculated | Committee-Ready | Post-quarter position unknown | Recomputation below |
| Interest burden and coverage | Financial base | Directly Sourced | Committee-Ready | Cash interest FY2025 only | Source match |
| Capital allocation versus free cash flow | Financial base, business context | Calculated | Committee-Ready | Legal capacity untested | Recomputation below |
| Earnings durability and Foodservice | Business context, synthesis | Analyst Inference | Remediation Needed | Causal claim unsupported | Restate (issue 1) |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

Module status: Ready with Limitations. Traceability scope: Top 5. Entity key: issuer id post, Post Holdings, Inc., available. Files used: the four handoffs and seven sources below; the pack file `_retrieval.json` is metadata and is not used.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-09-30_post-20250930.htm.jsonl | Audited filed annual report | FY2025, year ended Sep 30, 2025 | Post Holdings, Inc. consolidated | Statements, debt note, leases, pensions, business, segments, customers | Fiscal year ended more than a year before the as-of date | Financial base, business context, synthesis |
| S2 | 10-Q_2025-12-31_post-20251231.htm.jsonl | Unaudited filed quarterly report | Fiscal Q1, Dec 31, 2025 | Same | Balance sheet, revolver, debt table | Unaudited | Leverage and liquidity by date |
| S3 | 10-Q_2026-03-31_post-20260331.htm.jsonl | Unaudited filed quarterly report | Fiscal Q2, Mar 31, 2026 | Same | Balance sheet, revolver, debt table | Unaudited | Leverage and liquidity by date |
| S4 | 10-Q_2026-06-30_post-20260630.htm.jsonl | Unaudited filed quarterly report | Fiscal Q3, Jun 30, 2026 | Same | Latest statements, debt, covenant, MD&A, divestitures | Unaudited | Primary period source |
| S5 | EX-99.1_2026-02-03_ex99-1q12026er.htm.jsonl | Issuer earnings release | Fiscal Q1 | Same | Adjusted EBITDA for the quarter and prior-year quarter | Management non-GAAP; printed date February 5, 2026 differs from file label | LTM EBITDA at Dec 31, 2025 |
| S6 | EX-99.1_2026-05-05_ex99-1q22026er.htm.jsonl | Issuer earnings release | Fiscal Q2 | Same | LTM Adjusted EBITDA, net leverage, coverage | Management non-GAAP; printed date May 7, 2026 differs from file label | Leverage at Mar 31, 2026 |
| S7 | EX-99.1_2026-08-06_ex99-1q32026er.htm.jsonl | Issuer earnings release | Fiscal Q3 and nine months | Same | Adjusted EBITDA reconciliation, LTM, net leverage, coverage, guidance, segments | Management non-GAAP and guidance | Leverage, add-backs, guidance |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage of 4.59x net and 4.75x total on LTM Adjusted EBITDA of USD 1,615.9 million; 5.57x total on unadjusted EBITDA | CP-1 | Principal debt 7,676.0 and cash 265.6 from the debt note and balance sheet; Adjusted EBITDA from the release reconciliation | Debt service and refinancing tolerance depend on the earnings denominator | Sets the risk level and refinancing sensitivity | S4 page:17, page:3; S7 page:22 | Management EBITDA definition; add-backs 232.9 |
| 2 | Liquidity of USD 1,242.4 million and first maturity of USD 575.0 million in August 2027 | CP-1 | Cash 265.6; revolver 1,000.0 less letters of credit 23.2 and no borrowings; debt table | Determines near-term default risk and refinancing need | Low near-term liquidity risk | S4 page:3, page:17, page:21 | Position after June 30, 2026 not supplied |
| 3 | Interest burden: interest expense, net up 22% in nine months; coverage 3.8x | CP-1 | Statement of operations and release coverage reconciliation | Debt service capacity falls as cost rises with flat to lower earnings | Coverage is trending down | S4 page:2, page:30; S7 page:22 | Cash interest paid is available for FY2025 only |
| 4 | Buybacks of USD 916.1 million versus free cash flow of USD 401.5 million | CP-1, CP-1A | Cash flow statement and release free cash flow reconciliation | Leverage reduction depends on management discretion | Governance behaviour Neutral or Mixed | S4 page:4, page:41; S7 page:21 | Restricted payment capacity not supplied |
| 5 | Earnings durability: core volume decline, customer concentration, Foodservice above-run-rate earnings | CP-1A, CP-2 | Segment tables, customer percentages and volume statements in the 10-K and release | Margin and cash flow resilience drive leverage tolerance | Guided comparable entry level below FY2026 guidance | S1 page:16; S7 page:4, page:5, page:7 | Cause of Foodservice above-run-rate earnings not stated by the issuer |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net leverage 4.59x and total 4.75x at June 30, 2026 | CP-1 | 7,410.4 net debt and 1,615.9 LTM Adjusted EBITDA printed in S7 page:22; ratio divides them | Yes | Filed statements plus issuer release | Calculated | Verified by recomputation | High | Committee-Ready |
| Liquidity of 1,242.4 | CP-1 | Cash 265.6 (S4 page:3) plus available capacity 976.8 (S4 page:21) | Yes | Filed | Calculated | Verified | High | Committee-Ready |
| Interest expense, net up 22% in nine months; coverage 3.8x | CP-1 | S4 page:30 prints 317.3 against 259.6 and 22 %; S7 page:22 prints 3.8x | Yes | Filed and issuer release | Directly Sourced | Verified | High | Committee-Ready |
| Buybacks exceed free cash flow by 514.6 | CP-1 | 916.1 (S4 page:4) less 401.5 (S7 page:21) | Yes | Filed and issuer release | Calculated | Verified | High | Committee-Ready |
| Cereal and pet food were 51.6% of FY2025 net sales | CP-1A | 32.4% and 19.2% printed in S1 page:11 | Yes | Audited filing | Calculated | Verified | High | Committee-Ready |
| Walmart 17.4% of net sales; top-two customers 42.0% and 34.9% | CP-1A | S1 page:16 | Yes | Audited filing | Directly Sourced | Verified | High | Committee-Ready |
| About 60 million of Foodservice earnings above run rate is avian influenza pricing | CP-1A, CP-2 | S7 page:7 states the 60 million and the 500 million run rate without a cause; S7 page:4 and S4 page:34 say the lapping of prior-year avian influenza pricing lowers Q3 results | Partial | Issuer release and filing | Analyst Inference | Not supported as stated | Low | Remediation Needed |
| Covenant is a springing secured test not engaged at June 30, 2026 | CP-1 | S4 page:23 and page:41 give the test and trigger; usage 23.2 (S4 page:21) | Yes | Filed | Directly Sourced | Verified; headroom not traceable | Medium | Committee-Ready with restriction |
| Governance behaviour Neutral or Mixed | CP-1A | Documented repurchases and refinancing; no executed documents | Yes | Filed | Analyst Inference | Reasoned from documented actions | Medium | Committee-Ready with restriction |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 7,676.0 at June 30, 2026 | source-text | 10-Q_2026-06-30_post-20260630.htm.jsonl | S4 | page:17, Note 14 | Debt by instrument | Sourced | Filed | Matches release page:22 |
| Cash 265.6; total assets 12,852.7 | source-text | same | S4 | page:3 | Chart data: liquidity | Sourced | Filed | Matches |
| Revolver no borrowings, letters of credit 23.2, capacity 976.8 | source-text | same | S4 | page:21 | Chart data: liquidity | Sourced | Filed | Matches |
| Revolver matures February 20, 2029 | source-text | same | S4 | page:20 | Chart data: debt maturities | Sourced | Filed | Matches |
| Covenant 4.25:1.00, 30% trigger | source-text | same | S4 | page:23 | Covenants and definitions | Sourced | Filed | Matches |
| Net leverage 4.6x; coverage 3.8x; LTM Adjusted EBITDA 1,615.9 and 1,597.3 | source-text | EX-99.1_2026-08-06_ex99-1q32026er.htm.jsonl | S7 | page:22 | Adjusted EBITDA review | Sourced | Issuer release | Management non-GAAP |
| LTM add-backs table through 1,615.9 | source-text | same | S7 | page:21, page:22 | Adjusted EBITDA review | Sourced and Calculated | Issuer release | Sum recomputed to 1,615.9 |
| Mar 31, 2026 LTM 1,635.6; net leverage 4.5x; coverage 4.1x | source-text | EX-99.1_2026-05-05_ex99-1q22026er.htm.jsonl | S6 | page:23, page:24 | Chart data: leverage | Sourced | Issuer release | Matches |
| Q1 Adjusted EBITDA 418.2 and 369.9 | source-text | EX-99.1_2026-02-03_ex99-1q12026er.htm.jsonl | S5 | page:18 | Chart data: leverage | Sourced | Issuer release | Used for the December 2025 LTM |
| Dec 31, 2025 principal debt 7,507.2; revolver 430.0 and capacity 545.9 | source-text | 10-Q_2025-12-31_post-20251231.htm.jsonl | S2 | page:15, page:19 | Chart data | Sourced | Filed | Matches |
| Mar 31, 2026 principal debt 7,676.0; capacity 976.2 | source-text | 10-Q_2026-03-31_post-20260331.htm.jsonl | S3 | page:17, page:21 | Chart data | Sourced | Filed | Matches |
| FY2025 interest paid 370.1 | source-text | 10-K_2025-09-30_post-20250930.htm.jsonl | S1 | page:128 | Chart data: interest cover | Sourced | Audited | Only period with cash interest |
| FY2025 maturity schedule and revolver letters of credit 22.3 | source-text | same | S1 | page:139, page:141 | Chart data | Sourced | Audited | Matches |
| Purchase obligations 7,382.7; operating leases 277.9; pension funded status | source-text | same | S1 | page:80, page:131, page:144 | Claims outside the debt figure | Sourced | Audited | September 30, 2025 date |
| Bob Evans guarantee annual rent 13.5 on 129 properties | source-text | same | S1 | 129 properties page:142; rent page:143 | Claims outside the debt figure | Sourced | Audited | CP-1 cites page:142 for both; rent is on page:143 |
| Customer concentration percentages | source-text | same | S1 | page:16 | Company and operating model | Sourced | Audited | Matches |
| Product mix 32.4%, 29.6%, 19.2% | source-text | same | S1 | page:11 | Business and transaction view | Sourced | Audited | Matches |
| 8th Avenue purchase price 798.8 and leaseback assumed 111.4 | source-text | same | S1 | page:117, page:118 | Transaction summary | Sourced | Audited | Preliminary price |
| Pasta sale 375.0 and 378.5; Crystal Farms 50.0 and 45.7; Sparks gain 21.6 | source-text | S4 file | S4 | page:10, page:12 | Transaction summary | Sourced | Filed | Matches |
| 6.50% notes 1,300.0; 6.250% add-on 600.0 at 100.75% | source-text | S4 file | S4 | page:19, page:20 | Transaction summary | Sourced | Filed | Matches |
| Repurchase authorization 600.0; 490.7 remaining | source-text | S4 file and S7 file | S4, S7 | S4 page:48; S7 page:6 | Governance behaviour | Sourced | Filed and release | Matches |
| FY2026 guidance 1,560 to 1,570; Foodservice about 60 million above run rate; comparable entry about 1.48 billion | source-text | S7 file | S7 | page:2, page:6, page:7 | Credit translations | Sourced as Management Language | Issuer release | The cause of the 60 million is not stated |
| Foodservice Q3 decline reflects lapping of avian influenza pricing; nine-month egg pricing lower | source-text | S7 file and S4 file | S7, S4 | S7 page:4; S4 page:34 | Company and operating model | Sourced | Release and filing | Direction is the opposite of a current pricing boost |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM figures to June 30, 2026 | Financials and credit metrics | FY2025 + 9M FY2026 - 9M FY2025 | Sum and difference by line; period June 30, 2026 | Calculated | Verified: sales 8,412.5, operating profit 808.0, D&A 570.4, interest 419.1, net earnings 293.1, Adjusted EBITDA 1,615.9 (last four equal the release) | High | PD, liquidity | S1 page:94, page:96; S4 page:2, page:4; S7 page:22 |
| Net debt | Leverage chart | Principal debt less unrestricted cash | 7,676.0 - 265.6 = 7,410.4 (equals release) | Calculated | Verified | High | PD | S4 page:3, page:17; S7 page:22 |
| Total and net leverage by date | Leverage chart | Principal debt, cash, LTM Adjusted EBITDA | Debt / EBITDA; (debt - cash) / EBITDA; 4.84, 4.73, 4.69, 4.53, 4.75, 4.59 and December 4.73, 4.55 | Calculated | Verified; company ratios 4.5x and 4.6x reproduce on credit agreement EBITDA | High | PD, refinancing | S2, S3, S4, S5, S6, S7 pages above |
| December 2025 LTM Adjusted EBITDA | Leverage chart | 1,538.8 + 418.2 - 369.9 | = 1,587.1 | Calculated | Verified; not company-reported | Medium | PD | S5 page:18; S7 page:22 |
| Unadjusted EBITDA and leverage | Financials table | Operating profit + D&A | 808.0 + 570.4 = 1,378.4; 7,676.0 / 1,378.4 = 5.57 | Calculated | Verified; label is analyst normalisation | Medium | PD | S1, S4 |
| Add-backs 232.9, 14.4% | Adjusted EBITDA review | LTM reconciliation lines | 1,615.9 - 1,383.0 = 232.9; 232.9 / 1,615.9 = 14.4% | Calculated | Verified; listed add-backs 253.4 and other net items (20.5) | High | Earnings quality | S7 page:22 |
| Liquidity by date | Liquidity chart | Cash plus capacity | 1,242.4; 714.4; 825.2; 1,245.6 | Calculated | Verified | High | Liquidity | S2, S3, S4 |
| Maturity wall | Debt maturities chart | June 30, 2026 debt table by maturity date | Rows total 7,676.0; fiscal-year assignment by September 30 year end | Calculated | Verified; leaseback timing is a placement, disclosed | Medium | Refinancing | S4 page:17; S1 page:140, page:141 |
| Coupon run-rate 421.1; 3.84x | Calculation 9 of financial base | Principal x coupon for seven note issues | Sum of products; 1,615.9 / 421.1 | Calculated | Verified; excludes revolver fees, leaseback, amortisation | Medium | Debt service | S4 page:17 |
| Guidance-implied Q4 | Financial base and synthesis | 1,560 to 1,570 less 1,190.5; FY2025 1,538.8 less 1,113.4 | 369.5 to 379.5 against 425.4 | Calculated | Verified | Medium | Earnings trend | S7 page:2, page:19, page:22 |
| Buyback excess 514.6; net issuance 223.8 | Cash flow section | 916.1, 401.5, 2,265.0, 2,041.2 | Differences | Calculated | Verified; debt change 7,676.0 - 7,452.2 = 223.8 | High | Leverage direction | S4 page:4 |
| Synthesis sensitivities: 5.01x, 5.19x, 3.5x, 946.8, 2.2x, 13.0%, 7.2% | Credit risks and calculations | CP-1 figures and management comparable level 1,480 | Ratios recomputed here | Calculated and Assumption-Based | Verified; 1,480 is management language, 4.00x is a chosen reference | Medium | PD, liquidity | CP-1, S7 page:7 |
| Metric definition drift | Cross-module | Adjusted EBITDA (management), credit agreement EBITDA, unadjusted EBITDA | Three bases kept separate and labelled in CP-1 and CP-2 | Calculated | No drift: each ratio names its basis | High | PD | S7 page:22 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | About 60 million of Foodservice earnings above run rate is avian influenza pricing, and egg earnings are boosted by temporary pricing | Management gives the 60 million and the 500 million run rate without a cause. The filings say the lapping of prior-year avian influenza pricing reduced Q3 sales and profit, and nine-month egg pricing was lower, yet nine-month segment profit rose. The cause of the above-run-rate earnings is therefore not established | Analyst Inference | If the earnings are not tied to temporary pricing, their durability may differ from what the credit view implies. The risk is that the denominator of leverage is overstated or understated by an unknown amount | Restate as: management says guidance includes about 60 million above run rate; the cause is not stated; the lapping of prior-year avian influenza pricing explains the Q3 decline | Business context (reader summary, business view, credit translation 2); synthesis (reader summary, credit view, key findings, risks) |
| Minor | Bob Evans lease guarantee annual rent 13.5 | Rent is on page:143, not page:142; 129 properties is on page:142 | Weak Lineage | Locator accuracy only | Cite page:143 for the rent | Financial base, claims outside debt |
| Minor | Interest drivers (higher debt, higher rates, lower interest income) in the synthesis risk table | Stated in S7 page:5 but not carried by the financial base or business handoffs, which the method makes the only basis | Weak Lineage | Lineage runs outside the upstream registers | Cite S7 page:5 or carry the statement upstream | Synthesis, key credit risks |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven sources cover the annual report, three quarters and three releases; no executed financing documents, ratings or post-June 30, 2026 balance sheet | Legal and covenant claims have no executed document to trace to | Covenant headroom and legal capacity cannot be verified | Obtain indentures, credit agreement and compliance certificate |
| Citation completeness | Ready with Remediation | Every figure checked carries a locator; one locator off by a page; one lineage outside upstream registers | A wrong page slows verification | None on conclusions | Correct the two citations |
| Calculation traceability | Committee-Ready | All calculations show formula and inputs and recompute | Rounding differences only | Figures can be relied on | None |
| Assumption transparency | Committee-Ready | Unadjusted EBITDA, the 1.48 billion comparable level and the 4.00x reference are labelled as analyst or management constructs | Constructs could be mistaken for facts | Sensitivities stay illustrative | None |
| Markdown and export artifact integrity | Committee-Ready | Required headings and tables present in all four handoffs; handoff hashes recorded | A malformed table would break the report | None | None |

Overall auditability: Ready with Remediation, the lowest of the five dimensions.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Cause of the Foodservice earnings above run rate is not stated | Issuer explanation for the 60 million | Durability of earnings drives leverage tolerance | Business and synthesis earnings-durability statements | Medium impact | Earnings call remarks or prepared remarks (not in pack) |
| CP-5-GAP-002 | Covenant headroom cannot be traced | Secured net debt and credit agreement EBITDA definitions, compliance certificate | Protection and default risk | Covenants section and synthesis risk | Medium impact | Credit agreement and compliance certificate |
| CP-5-GAP-003 | Legal capacity for buybacks, debt incurrence and collateral release | Executed indentures and credit agreement | Creditor control and leakage | Governance behaviour | Medium impact | Indentures and credit agreement |
| CP-5-GAP-004 | Position after June 30, 2026 | Fiscal fourth-quarter results or later filings | Currentness of leverage and liquidity | All current-period figures | Low impact | Fiscal 2026 annual report when filed |
| CP-5-GAP-005 | Cash interest paid for interim periods | Supplemental cash flow disclosure in the 10-Qs | Cash-basis interest cover | Interest cover chart | Low impact | Company disclosure |
| CP-5-GAP-006 | Ownership table and ratings | 2026 Proxy Statement; rating agency reports | Control rights and external view | Company profile and synthesis | Low impact | Proxy statement; agency reports |

#### T5.1 Module handoff status

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response, run post-2026-11-05-credit_snapshot-host | Source readiness for seven sources | Filed statements and releases | Six H2 headings and reader summary present | Accepted with one wording defect corrected in later modules | The phrase "a different numerator" was imprecise and was corrected in the financial base |
| CP-1 | requests/CP-1 response, same run | Financial base and chart data | Filed statements and releases | Six H2 headings and all selectors present | Accepted | One integration-cost wording and one locator defect; see issues 3 and 4 |
| CP-1A | requests/CP-1A response, same run | Business, transaction and governance | Filed statements and releases | Six H2 headings and selectors present | Accepted | Contains the unsupported Foodservice attribution; see issue 1 |
| CP-2 | requests/CP-2 response, same run | Fundamental credit synthesis | Upstream handoffs | Six H2 headings and selectors present | Accepted | Repeats issue 1 and uses one lineage outside upstream |

#### T5.2 Claim and evidence defects

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1A, CP-2 | Foodservice above-run-rate earnings attributed to avian influenza pricing | Not supported by the sources | See T5B.6 | Restate as inference or cite a source | Blocks clearance of the earnings-durability driver until restated |
| Minor | CP-1 | Bob Evans rent locator | Supported on a different page | Page off by one | Cite page:143 | None |
| Minor | CP-2 | Interest drivers | Supported outside the upstream registers | Lineage | Cite the release | None |

#### T5.3 Metric and logic issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Leverage shown on three EBITDA bases | Adjusted, credit agreement and unadjusted are labelled separately; no drift found | None between sources | Keep labels in every downstream use | None |
| Minor | CP-1 | Maturity row for leaseback financial liabilities placed at fiscal 2040 | Principal schedule not printed; disclosed as a placement | None | Keep the disclosure | None |

#### T5.4 Legal and structural claims

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A, CP-2 | Notes are guaranteed by domestic subsidiaries; the 6.25% notes and revolver are secured; the covenant is a springing secured leverage test | Executed indentures, credit agreement and guarantee and collateral agreement | Handoffs rest on summary notes; guarantor names, release terms, baskets and definitions are not in the pack | Carry as summary-level and avoid statements on capacity or headroom | Counsel review before any legal or restricted-payment conclusion |

#### T5.5 Market and relative-value claims

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | No market or relative-value claim is made, which is correct; fair value of the notes (USD 7,526.2 million at June 30, 2026) is a company disclosure only | Bond prices, spreads, ratings and peer data | Not in the pack | None for this run | Relative value cannot be formed from these sources |

#### T5.6 Cross-module conflicts and versions

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1A | Release dates in file names (February 3 and May 5, 2026) against dates printed in the releases (February 5 and May 7, 2026). CP-0 directs use of the printed dates; CP-1A logs the conflict without choosing | Handoffs differ in handling | Treat as logged and not reconciled; no figure depends on either date | None |
| Minor | CP-0, CP-1 | CP-0 wording on the net leverage numerator | CP-1 corrects it | Rely on CP-1 | None |
| Minor | CP-1, CP-1A | CP-1 wording that integration costs recur in Weetabix East Africa; the releases attribute them to Post Consumer Brands and Refrigerated Retail | CP-1A corrects it | Rely on CP-1A | None |
| Material | CP-1A, CP-2 | Foodservice attribution to avian influenza pricing | Both modules carry it | See issue 1 | Earnings-durability driver restricted |

#### T5.7 Other issues

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Presentation | Several summary sentences use "temporary pricing" for Foodservice; see issue 1 | Reword with the restated fact | Low |
| Minor | CP-1 | Completeness | Cash interest for interim periods is not in the sources, and the handoff says so after searching | None | None |

#### T5.8 Handoff component defects

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Claims outside debt table | Locator page:142 for rent that is on page:143 | Correct the citation | None |
| Minor | CP-2 | Key credit risks table | Interest-driver lineage outside upstream | Cite the release | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Material | CP-1A, CP-2 | Unsupported attribution | About 60 million of Foodservice earnings above run rate tied to avian influenza pricing without source support | Restate as management language with cause not stated | Restricts earnings-durability driver | Open |
| 2 | Minor | CP-1 | Locator | Bob Evans rent on page:143 | Correct citation | None | Open |
| 3 | Minor | CP-0 | Wording | Net leverage numerator wording imprecise | Corrected in CP-1 | None | Resolved in later handoff |
| 4 | Minor | CP-1 | Wording | Integration costs tied to acquisitions not named in the sources | Corrected in CP-1A | None | Resolved in later handoff |
| 5 | Minor | CP-2 | Lineage | Interest drivers outside upstream | Cite the release | None | Open |
| 6 | Minor | CP-0, CP-1A | Version | Release date conflict logged, not reconciled | Keep as logged | None | Open |

## Calculations

Recomputations performed for this review from the cited source figures; each matched the handoff.

| Check | Inputs | Result | Handoff value |
| --- | --- | --- | --- |
| LTM sums | FY2025 + 9M FY2026 - 9M FY2025 for sales, operating profit, D&A, interest, net earnings, operating cash flow, capex | 8,412.5; 808.0; 570.4; 419.1; 293.1; 992.6; 439.5 | Same |
| Adjusted EBITDA LTM | 1,538.8 + 1,190.5 - 1,113.4 | 1,615.9 | 1,615.9 |
| LTM Adjusted EBITDA at March 31, 2026 from halves | 1,538.8 + 813.2 - 716.4 | 1,635.6 | 1,635.6 |
| LTM Adjusted EBITDA at December 31, 2025 | 1,538.8 + 418.2 - 369.9 | 1,587.1 | 1,587.1 |
| Leverage June 30, 2026 | 7,676.0 / 1,615.9; 7,410.4 / 1,615.9 | 4.75; 4.59 | 4.75; 4.59 |
| Leverage September 30, 2025 | 7,452.2 / 1,538.8; 7,275.5 / 1,538.8 | 4.84; 4.73 | 4.84; 4.73 |
| Company ratios | 7,410.4 / 1,597.3; 7,406.6 / 1,646.9; 1,597.3 / 419.1; 1,646.9 / 399.4 | 4.64; 4.50; 3.81; 4.12 | 4.6x; 4.5x; 3.8x; 4.1x |
| Add-backs | 1,615.9 - (293.1 + 419.1 + 100.4 + 570.4) | 232.9 | 232.9 |
| Listed add-backs | 83.0 + 43.3 + 29.8 + 27.6 + 22.0 + 17.5 + 12.0 + 9.0 + 9.2, less 20.5 other net | 232.9 | 232.9 |
| Liquidity | 265.6 + 976.8; 1,000.0 - 23.2 | 1,242.4; 976.8 | 1,242.4; 976.8 |
| Maturity rows | 576.3 + 0.5 + 1,385.4 + 980.6 + 1,000.0 + 1,200.0 + 1,200.0 + 1,300.0 + 33.2 | 7,676.0 | 7,676.0 |
| Coupon run-rate | 14.4 + 64.1 + 44.1 + 62.5 + 76.5 + 75.0 + 84.5 | 421.1 | 421.1 |
| Synthesis ratios | 7,410.4 / 1,480; 7,676.0 / 1,480; 1,242.4 / 575.0; 1,000.0 / 7,676.0; 553.1 / 7,676.0; 7,410.4 - 4.00 x 1,615.9 | 5.01; 5.19; 2.16; 13.0%; 7.2%; 946.8 | Same |
| Guidance-implied Q4 | 1,560 - 1,190.5; 1,570 - 1,190.5; 1,538.8 - 1,113.4 | 369.5; 379.5; 425.4 | Same |
| Segment net sales FY2025 | 4,024.6 + 542.2 + 2,641.0 + 953.3 - 3.0 | 8,158.1 | 8,158.1 |

## Gaps

The status of this review is Ready with Limitations and committee use is Restricted. The open items are the Foodservice attribution (issue 1), two minor citation fixes (issues 2 and 5), and the untraceable legal and covenant points in T5.4 and T5B.8. Revision history: the earlier wording on the covenant numerator and on integration costs was corrected in later handoffs, as logged in T5.6. This review made no change to any credit conclusion, and no earlier handoff was edited.

## Next module

No further module is selected in this run. The report assembled from these handoffs should carry the restatement in issue 1 wherever it describes the Foodservice earnings above run rate, and should show the legal and covenant restrictions in T5.4. The follow-up evidence is the issuer's explanation of the above-run-rate Foodservice earnings, the executed financing documents with the compliance certificate, and the fiscal 2026 annual report when it is filed.
