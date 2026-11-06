## Request

Evidence trace and research-integrity review for QXO, Inc., as of 2026-11-05, pathway credit_snapshot, reporting currency USD, covering the earlier modules for this run (source readiness, financial base, business and transaction context, credit synthesis) and their trace to the pinned filings. This module changes no upstream conclusion and repairs no earlier handoff; it records defects and their remediation.

## Sources

Issuer sources checked directly against the handoffs (exact names and sha256):

| Source file | sha256 |
| --- | --- |
| 10-K_2025-12-31_qxo-20251231.htm.jsonl | 1b7dee5c3907814ca02da7e5177715b488778f3cfe6a6a69dbb9a2d892ae7bd4 |
| 10-Q_2025-09-30_qxo-20250930.htm.jsonl | 38eff6a9b29b23e51b5e94454227cd801b8344fa3f2dbacbcff9586720ba1f5f |
| 10-Q_2026-03-31_qxo-20260331.htm.jsonl | f661446a2ae3c415c83c14493e42b107a6ed744b45a540466d49f9056424d438 |
| 10-Q_2026-06-30_qxo-20260630.htm.jsonl | 894ff623087578f719301215adbe097ad733e1b300a9d2d5bf4a10f19be9a21b |
| EX-99.1_2026-02-25_qxoq4-25earningsrelease.htm.jsonl | b326e55b305ddcd9c74b52354a08688ca3531d1057c5c1ee442c94d9779f5a35 |
| EX-99.1_2026-05-12_qxoq1-26earningsrelease.htm.jsonl | cb6d12c2f11a6aae12e16b22f726607cf654ffc6f9c813c160df8563f9de9aa2 |
| EX-99.1_2026-08-13_qxoq2-26earningsrelease.htm.jsonl | 67328156dff6e164d45723d576bcfc4e259ba15144552671032a5a2232707d03 |

Run settings (not issuer evidence): context, sha256 6a7b1beefd6814e2c0ed169307a2fa7c8234de27933b1d6c6e62ef434dbf5add.

Supplied handoffs:

| Module | sha256 |
| --- | --- |
| CP-0 | 517278b1d72fed537f71b31075de313413e0165b4db939225a68da51664f7aff |
| CP-1 | 0c4570b0cb02f79e4f6bc512ceeaaaa35a45ba07e203d0adcef2870aec1b148f |
| CP-1A | c18abc5e3bcca0ebf51a2c43e611becd725c810db3ea10aa7a3e536b97687d36 |
| CP-2 | 9cd3d241473c172544f322dce69cdc603aa9237eca38f08eb2a37719adf70d20 |

Run identity restated from the handoffs: run id qxo-2026-11-05-credit_snapshot-host, issuer id qxo, as-of 2026-11-05, current period Q2 2026, prior period FY2025, currency USD millions. Handoff envelopes: the earlier modules use the six canonical headings of the Markdown transport; they carry no YAML front matter, Evidence Trace or Source Registry headings, which is a property of the transport and is logged once below.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The earlier analysis traces well to the filings: figures recompute and locate. Evidence is traceable with remediation, and committee use should be restricted until four material points are cleared. | Medium | No TopBuild earnings, cash or accounting are reported, and executed debt documents are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every recomputed total and ratio matched the filings and the earlier modules. | Reported borrowings, liquidity and adjusted earnings at June 30, 2026 can be relied on. | High |
| Debt was measured at principal; on balance sheet carrying value gross leverage is 8.33x, not 8.43x. | The headline ratio is overstated by 0.10x against the balance sheet basis. | Medium |
| Two claims lacked proper locators: the Series C cash redemption right and management's plan to more than double EBITDA. | Both are supported by the filings but must be cited before committee use. | Medium |
| Covenant, ranking and put terms rest on note summaries because executed documents are not supplied. | Legal review is needed before relying on ranking or change-of-control terms. | Medium |
| The 1.27x cover floor rests on an assumed rate for the incremental term loan. | Treat it as a sensitivity, not an estimate. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 3 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is that TopBuild earnings, cash and purchase accounting are not reported, which matters because every post-closing leverage, cover and liquidity statement rests on pre-closing earnings and implies that committee use must stay restricted to pre-closing ratios. The strongest contrary point is that the figures themselves recompute exactly; the defects found are of citation, measurement basis and legal support, not of arithmetic.

### Analytical appendix — complete canonical registers

Module status: Ready with Limitations (all four earlier handoffs available; executed legal documents and post-closing data absent). Traceability scope: Top 5. Entity key status: issuer id qxo available. Confidence Score: not computed here because the scoring script is not available in this host run; under the severity engine qa_status is Restricted, so the band is Low and the score would be at most 59. committee_status: Restricted.

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_qxo-20251231.htm.jsonl | High (filed, audited) | FY2025, with 2024 comparative | QXO, Inc. and subsidiaries | Statements, notes, business, ownership, risk factors | Beacon from April 29, 2025 only; two auditors across the two years | FY2025 EBITDA, cash interest, ownership, suppliers |
| S2 | 10-Q_2025-09-30_qxo-20250930.htm.jsonl | High (filed, unaudited) | Q3 2025 | QXO, Inc. and subsidiaries | Beacon history | Not used for any cited figure | Period coverage only |
| S3 | 10-Q_2026-03-31_qxo-20260331.htm.jsonl | High (filed, unaudited) | Q1 2026 | QXO, Inc. and subsidiaries | Balance sheet, debt, ABL, Q1 EBITDA | One-decimal rounding | March 2026 liquidity and leverage |
| S4 | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | High (filed, unaudited) | Q2 2026 and six months | QXO, Inc. and subsidiaries; debt at QXO Building Products | Debt, equity, acquisitions, MD&A, liquidity | TopBuild accounting incomplete; whole-million rounding | Core June 2026 position |
| S5 | EX-99.1_2026-02-25_qxoq4-25earningsrelease.htm.jsonl | Medium (management release, attributed) | Q4 and FY2025 | QXO, Inc. | Headline results | Management non-GAAP measures | Period coverage only |
| S6 | EX-99.1_2026-05-12_qxoq1-26earningsrelease.htm.jsonl | Medium (management release, attributed) | Q1 2026 | QXO, Inc. | Headline results | Management non-GAAP measures | Period coverage only |
| S7 | EX-99.1_2026-08-13_qxoq2-26earningsrelease.htm.jsonl | Medium (management release, attributed) | Q2 2026 and six months | QXO, Inc. | Statements, reconciliations, cash flow | Management non-GAAP measures | Six-month EBITDA, cash interest |
| H0 | CP-0 handoff | Derived from S1 to S7 | As of 2026-11-05 | QXO, Inc. | Source readiness | Chunk counts, not printed pages | Perimeter and gaps |
| H1 | CP-1 handoff | Derived from S1 to S7 | FY2025 to LTM June 2026 | QXO, Inc. | Financials, ratios, charts | Principal debt basis; assumes cited figures | CP-1A, CP-2 |
| H2 | CP-1A handoff | Derived from S1 to S7 | To July 1, 2026 | QXO, Inc. | Business, transactions, governance | Some claims without locators | CP-2 |
| H3 | CP-2 handoff | Derived from H1 and H2 | As of 2026-11-05 | QXO, Inc. | Credit view | Illustrative sensitivities | Committee use |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Borrowings rose to 6,111 at June 30, 2026 and to 9,111 after the July 1, 2026 term loan, against earnings that exclude TopBuild | CP-1 | Debt table and incremental term loan note | Debt rises ahead of earnings, so leverage and cover are overstated or unmeasured | Determines the leverage view and monitoring trigger | S4 page:44, page:49, page:54 | TopBuild earnings, cash and accounting not reported |
| 2 | Adjusted EBITDA of 724.8 includes 379.1 of add-backs | CP-1 | FY2025 reconciliation, six-month reconciliations | Add-backs recur in each period, so leverage tolerance is weaker if they persist | Drives gross leverage of 17.68x before add-backs | S1 page:46, S7 page:11 | Management definition; recurrence is inference |
| 3 | Cash interest cover of 3.28x versus run-rate coupons of 401.0 | CP-1, CP-2 | Cash flow supplements and printed rates | Cash interest in the trailing period understates run-rate cost | Debt service capacity after the new debt | S1 page:65, S7 page:9, S4 page:44 | Incremental term loan margin not supplied |
| 4 | Liquidity of 4,704 and no scheduled principal before 2030 | CP-1 | Management liquidity statement and debt note | Near-term refinancing and covenant pressure low | Main support for the credit view | S4 page:62, page:49, page:51 | Cash after the TopBuild closing not reported |
| 5 | Preferred claims and change-of-control cash call | CP-1A, CP-2 | Equity note terms | Preferred dividends and a Series C cash redemption right compete with debt service | Group-level claims beyond the borrowings | S4 page:68, page:31, page:69 | Dividend ceiling assumes cash payment; executed terms not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Borrowings 6,111 and 9,111 | CP-1 | Debt table 6,100 plus 11; incremental loan 3.0 billion | Yes | High | Calculated | Supported | High | Committee-Ready |
| Adjusted EBITDA add-back dependence | CP-1 | FY2025 647.8 plus six-month 273 less 196; add-back items | Yes | High and Medium | Calculated | Supported | Medium | Committee-Ready |
| Cover of 3.28x and run-rate coupon 401.0 | CP-1 | Cash interest 138.0, 106, 23; rates 5.64%, 6.75%, 6.500%, 6.875%, 4.70% | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Liquidity 4,704 and maturity profile | CP-1 | Management liquidity statement, ABL note, debt note | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Preferred claims compete with debt service | CP-1A, CP-2 | Dividend rates; redemption terms | Partial (Series C redemption lacks a quote) | High | Analyst Inference | Partially Supported | Medium | Remediation Needed |
| Illustrative cover floor 1.27x | CP-2 | Assumed 5.64% rate on 3,000 | Yes (assumption stated) | Low | Assumption-Based | Partially Supported | Low | Remediation Needed |
| Management plan to more than double EBITDA | CP-2 | Release statement, cited to the wrong module | Partial | Medium | Weak Lineage | Partially Supported | Low | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Borrowings principal at June 30, 2026 is 6,111 (6,100 term debt plus 11 revolver) | 10-Q Q2 2026 > Debt note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:44 | CP-1 financial base, instruments table | Sourced | High (filed) | Quote: "Long-term debt, net $ 6,100 $ 6,029 $ 6,249 $ 3,100 $ 3,057 $ 3,209" |
| Unrestricted cash at June 30, 2026 is 2,774 | 10-Q Q2 2026 > Balance sheet | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:5 | CP-1 liquidity chart | Sourced | High (filed) | Quote: "Cash and cash equivalents $ 2,774 $ 2,362" |
| ABL borrowing capacity is 1.93 billion at June 30, 2026 | 10-Q Q2 2026 > Debt note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:49 | CP-1 liquidity chart | Sourced | High (filed) | Quote: "the Borrower had $1.93 billion borrowing capacity under the ABL Facility" |
| Standby letters of credit under the ABL are 62 | 10-Q Q2 2026 > Debt note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:51 | CP-1 liquidity chart, calculations | Sourced | High (filed) | Quote: "had $62 million in outstanding standby letters of credit issued under the ABL Facility" |
| Management states total liquidity of 4.70 billion | 10-Q Q2 2026 > MD&A liquidity | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:62 | CP-1 liquidity chart; CP-2 credit view | Sourced | High (filed) | Quote: "total liquidity was $4.70 billion as of June 30, 2026" |
| Restricted cash of 3,000 is held for the TopBuild closing | 10-Q Q2 2026 > Notes, cash | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:13 | CP-1 leverage chart basis | Sourced | High (filed) | Quote: "Restricted cash included in prepaid expenses and other current assets 3,000 4" |
| Incremental term loan of 3.0 billion matures July 1, 2033 | 10-Q Q2 2026 > Debt note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:49 | CP-1 maturities chart | Sourced | High (filed) | Quote: "The Incremental Term Loan Facility will mature on July 1, 2033" |
| TopBuild closing funded by escrow release, incremental term loan and Series C | 10-Q Q2 2026 > Recent developments | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:54 | CP-1A transaction summary | Sourced | High (filed) | Quote: "incurred an incremental term loan for $3.0 billion in gross proceeds" |
| FY2025 Adjusted EBITDA is 647.8 | 10-K > MD&A non-GAAP | 10-K_2025-12-31_qxo-20251231.htm.jsonl | S1 | page:46 | CP-1 LTM EBITDA | Sourced | High (filed) | Quote: "Adjusted EBITDA $ 647.8 $ (19.9)" |
| Six-month Adjusted EBITDA is 273 for 2026 and 196 for 2025 | Release Q2 2026 > Reconciliation | EX-99.1_2026-08-13_qxoq2-26earningsrelease.htm.jsonl | S7 | page:11 | CP-1 LTM EBITDA | Sourced | Medium (management release) | Quote: "Adjusted EBITDA(4) $ 272 $ 204 $ 273 $ 196" |
| FY2025 cash interest paid is 138.0 | 10-K > Cash flow supplement | 10-K_2025-12-31_qxo-20251231.htm.jsonl | S1 | page:65 | CP-1 interest cover | Sourced | High (filed) | Quote: "Interest $ 138.0 $ 0.1" |
| Six-month cash interest paid is 106 for 2026 and 23 for 2025 | Release Q2 2026 > Cash flow supplement | EX-99.1_2026-08-13_qxoq2-26earningsrelease.htm.jsonl | S7 | page:9 | CP-1 interest cover | Sourced | Medium (management release) | Quote: "Interest $ 106 $ 23" |
| FY2025 transaction cost add-back is 83.7 | 10-K > Reconciliation | 10-K_2025-12-31_qxo-20251231.htm.jsonl | S1 | page:46 | CP-1 add-back split; CP-2 key finding 2 | Sourced | High (filed) | Quote: "Transaction costs 83.7 12.8" |
| Series C dividend is 4.75% a year | 10-Q Q2 2026 > Equity note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:68 | CP-1A calculation 4; CP-2 preferred ceiling | Sourced | High (filed) | Quote: "at a rate of 4.75% per annum" |
| Convertible Preferred dividend is 9% a year | 10-Q Q2 2026 > Equity note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:31 | CP-1A calculation 4 | Sourced | High (filed) | Quote: "rate per annum of 9% per share" |
| Series C holders are offered cash redemption on a fundamental change | 10-Q Q2 2026 > Equity note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:69 | CP-1A credit translation 4 (no locator there) | Sourced; locator missing downstream | High (filed) | Quote: "the Company will be obligated to offer to redeem all of the Series C Preferred Stock for a price in cash" |
| Term loan interest rate is 5.64% at June 30, 2026 | 10-Q Q2 2026 > Debt note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:44 | CP-1 and CP-2 coupon run-rate | Sourced | High (filed) | Quote: "Interest rate of 5.64% and 5.72% as of June 30, 2026 and December 31, 2025, respectively." |
| ABL springing fixed charge coverage test of 1.0 to 1.0 | 10-Q Q2 2026 > Debt note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:50 | CP-1 covenants | Sourced | High (filed) | Quote: "maintain a minimum fixed charge coverage ratio of 1.0 to 1.0" |
| Three suppliers make up nearly 35% of purchases | 10-K > Risk factors | 10-K_2025-12-31_qxo-20251231.htm.jsonl | S1 | page:16 | CP-1A operating model; CP-2 weakness | Sourced | High (filed) | Quote: "represented nearly 35% of total purchases" |
| Chairman controls about 22.1% of voting power | 10-K > Risk factors | 10-K_2025-12-31_qxo-20251231.htm.jsonl | S1 | page:34 | CP-1A profile; CP-2 key finding 7 | Sourced (as of the 10-K) | High (filed) | Quote: "beneficially owns or controls approximately 22.1% of the voting power of our capital stock" |
| Kodiak net purchase price is 2.22 billion; 2.25 billion in the 10-K | 10-Q Q2 2026 > Acquisitions note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:22 | CP-1A conflict log | Sourced; conflict logged | High (filed) | Quote: "completed the Kodiak Acquisition for a net purchase price of $2.22 billion" |
| Management plans to more than double EBITDA by 2030 | Release Q2 2026 > Chief executive quote | EX-99.1_2026-08-13_qxoq2-26earningsrelease.htm.jsonl | S7 | page:1 | CP-2 weakness (attributed to CP-1A) | Sourced; wrong basis cited downstream | Medium (management release) | Quote: "our plan to more than double EBITDA by 2030" |
| One operating segment | 10-Q Q2 2026 > Segment note | 10-Q_2026-06-30_qxo-20260630.htm.jsonl | S4 | page:28 | CP-1A operating model | Sourced | High (filed) | Quote: "manages its business as a single operating segment" |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA at June 30, 2026 = 724.8 | CP-1, CP-2 | FY2025 647.8; six months 2026 273; six months 2025 196 | 647.8 + 273 - 196, USD millions, period July 2025 to June 2026, no normalisation | Calculated | Supported | High | Leverage, cover | S1 page:46; S7 page:11 |
| Borrowings 6,111; net debt 3,337 | CP-1 | Term debt 6,100; ABL 11; unrestricted cash 2,774 | 6,100 + 11; 6,111 - 2,774; principal basis, leases excluded | Calculated | Supported with basis caveat | High | Leverage | S4 page:44, page:5 |
| Total debt / EBITDA 8.43x; net 4.60x | CP-1 | 6,111; 3,337; 724.8 | 6,111 / 724.8; 3,337 / 724.8 | Calculated | Supported | High | Leverage | H1 |
| Same ratios on carrying value | This module | Carrying 6,029 + 11 = 6,040; unrestricted cash 2,774 | 6,040 / 724.8 = 8.33x; (6,040 - 2,774) / 724.8 = 4.51x | Calculated | Supported | Medium | Leverage | S4 page:44 |
| LTM cash interest 221.0; cover 3.28x | CP-1 | 138.0; 106; 23 | 138.0 + 106 - 23; 724.8 / 221.0 | Calculated | Supported | High | Interest cover | S1 page:65; S7 page:9 |
| Run-rate coupon on June 30, 2026 debt 401.0; cover 1.81x | CP-1, CP-2 | Principal by instrument and printed rates | 850 x 5.64% + 2,250 x 6.75% + 1,500 x 6.500% + 1,500 x 6.875% + 11 x 4.70% = 401.0; 724.8 / 401.0 | Calculated | Supported | Medium | Interest cover | S4 page:44 |
| Cover floor 1.27x | CP-2 | Assumed incremental loan rate 5.64% (existing term loan rate) | 3,000 x 5.64% = 169.2; 401.0 + 169.2 = 570.2; 724.8 / 570.2 | Assumption-Based | Partially Supported | Low | Interest cover | H3 |
| Leverage break-even EBITDA 1,518.5 and 1,822.2 | CP-2 | 9,111 and analyst-chosen 6.0x and 5.0x | 9,111 / 6.0; 9,111 / 5.0 | Assumption-Based | Partially Supported | Low | Leverage | H3 |
| Add-backs 379.1, 52.3% of 724.8; EBITDA before add-backs 345.7 | CP-1, CP-2 | Reconciliation items for FY2025, six months 2026 and 2025 | Sum of items; 379.1 / 724.8; 724.8 - 379.1 | Calculated | Supported | High | Earnings quality | S1 page:46; S7 page:11 |
| Preferred dividend ceiling 264.1 | CP-1A, CP-2 | 3,000 at 4.75%; 1,000 at 9%; 575 at 5.50% | 142.5 + 90.0 + 31.6 | Calculated | Supported, assumes cash payment | Medium | Debt service | S4 page:68, page:31 |
| Floating share 14.1% and 42.4%; 100 basis points = 38.6 | CP-1, CP-2 | Floating 861 of 6,111; 3,861 of 9,111 | Ratios; 3,861 x 1% | Calculated | Supported, incremental loan assumed floating | Medium | Rate risk | S4 page:49 |
| Liquidity 4,704 | CP-1 | Cash 2,774; ABL availability 1,930 | 2,774 + 1,930; agrees to stated 4.70 billion | Calculated | Supported | High | Liquidity | S4 page:62 |

Metric-definition drift flagged: debt is measured at principal in the financial base while the balance sheet carries net issuance costs and discounts (see CP5-003); the same revolver figure is labelled borrowing capacity, undrawn committed facilities and availability in different modules (see CP5-007).

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Preferred claims compete with debt service | The Series C cash redemption right is stated in the context handoff without a quote or locator; the filing supports it | Weak Lineage | A change-of-control cash call is a liquidity mechanic that a reader cannot verify from the handoff | Add the locator in the 10-Q Q2 2026 (equity note, mezzanine classification and fundamental change redemption) | CP-1A credit translation 4; CP-2 key finding 6 |
| Material | Management plan to more than double EBITDA | The credit synthesis attributes it to the context handoff, which does not carry it; the earnings release does | Weak Lineage | Management ambition is presented with the wrong basis; it could be read as analysed fact | Cite the Release Q2 2026 as management language or remove the sentence | CP-2 weakness on integration load |
| Minor | Cover floor 1.27x and leverage break-even | Assumption-Based results rest on an assumed rate and analyst-chosen thresholds | Assumption-Based | Readers may treat a sensitivity as an estimate | Keep the labels; do not carry into committee numbers | CP-2 key finding 3, calculations 5 and 6 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 to Q2 2026; executed indentures, credit agreements and TopBuild financials absent | Terms known only from note summaries | Ranking and covenant statements need legal review | Obtain exhibits and the September 2026 quarter report |
| Citation completeness | Ready with Remediation | 23 sampled statements located and quoted; two claims lack proper locators | Unverifiable claims weaken committee reliance | Limited to two named claims | Add locators (CP5-001, CP5-002) |
| Calculation traceability | Ready with Remediation | All sampled totals and ratios recomputed exactly; principal versus carrying basis not logged | Basis drift shifts headline leverage by 0.10x | Small effect on the leverage view | Log carrying value and delta (CP5-003) |
| Assumption transparency | Committee-Ready | Illustrative floor and thresholds are labelled as assumptions | Reader cannot mistake sensitivities for estimates | None beyond labelling | Keep labels |
| Markdown artifact integrity | Committee-Ready | Required headings and selectors present in each handoff; no YAML envelope under this transport | Transport limits the envelope checks | No downstream break | None |

Overall auditability is the weakest dimension: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | TopBuild earnings, balance sheet, debt assumed or repaid, cash acquired and purchase accounting | Third-quarter 2026 report, if filed on or before 2026-11-05 | Every post-closing ratio changes; leverage and liquidity after July 1, 2026 are Not calculable | CP-1, CP-2 leverage, cover and liquidity | High impact: caps confidence at Low for the enlarged group | Quarterly report for the period ending September 30, 2026 |
| CP-5-GAP-002 | Executed indentures, credit agreements, incremental term loan amendment, Series C certificate of designations | Exhibits listed in the June 2026 report | Covenant capacity, ranking, puts and redemption terms cannot be tested | CP-1 covenants, CP-2 claims | Medium impact | Exhibit filings of June 17 and July 1, 2026 |
| CP-5-GAP-003 | Incremental term loan margin and amortisation start | Amendment text | Run-rate interest above 401.0 cannot be stated | CP-2 key finding 3 | Medium impact | Incremental Assumption and Amendment Agreement No. 2 |
| CP-5-GAP-004 | Related-party arrangements and post-issuance ownership percentages | Proxy statement | Governance and control cannot be assessed beyond the annual report date | CP-1A, CP-2 key finding 7 | Medium impact | Proxy statement |
| CP-5-GAP-005 | Ratings, market quotes, spreads and valuation inputs | Run context fields blank | No market or relative-value view can be audited | None made by the modules | Low impact | Market data provider, outside the pack |
| CP-5-GAP-006 | Reported value of the ABL fixed charge ratio | Covenant certificate | Headroom measured on the availability trigger only | CP-1 covenants | Low impact | Compliance certificate |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | Handoff sha256 517278b1d72fed537f71b31075de313413e0165b4db939225a68da51664f7aff; run qxo-2026-11-05-credit_snapshot-host | Source readiness for seven sources | High | Six canonical headings present; no YAML envelope under this transport | Accepted by the structural check | Perimeter and gaps carried forward |
| CP-1 | Handoff sha256 0c4570b0cb02f79e4f6bc512ceeaaaa35a45ba07e203d0adcef2870aec1b148f; run qxo-2026-11-05-credit_snapshot-host | Financial base and chart selectors | High | Six headings and all selectors present | Accepted by the structural check | Debt at principal |
| CP-1A | Handoff sha256 c18abc5e3bcca0ebf51a2c43e611becd725c810db3ea10aa7a3e536b97687d36; run qxo-2026-11-05-credit_snapshot-host | Business, transactions, governance | High with management language tagged | Six headings and selectors present | Accepted after one repair | Some claims lack locators |
| CP-2 | Handoff sha256 9cd3d241473c172544f322dce69cdc603aa9237eca38f08eb2a37719adf70d20; run qxo-2026-11-05-credit_snapshot-host | Credit synthesis | Medium (analyst judgement) | Six headings and selectors present | Accepted by the structural check | Illustrative sensitivities labelled |

Module Status: Ready with Limitations. The CP-5 evidence trace is this module.

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1A | Series C holders can require cash redemption on a fundamental change (credit translation 4, consumer table) | Partially Supported | The filing supports it (equity note, mezzanine classification and fundamental change redemption) but the handoff gives no quote or locator | Add the locator and quote | Must be cited before committee use |
| Material | CP-2 | Management plan to more than double EBITDA (weakness: integration load) | Partially Supported | Attributed to CP-1A, which does not carry it; the earnings release does | Cite the release as management language or remove | Must be corrected before committee use |
| Minor | CP-1A | Series C investors described as funds managed by affiliates of Apollo Global Management, Inc. | Partially Supported | The filing says a fund managed by Apollo affiliates and other investors | Reword to match | Disclosure only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1 | Debt and leverage at principal, not balance sheet carrying value | Carrying value is 6,040 at June 30, 2026 against principal 6,111 (delta 71); 3,057.3 against 3,100.0 at December 31, 2025 (delta 42.7); gross leverage is 8.33x on carrying value against 8.43x | None between sources; basis choice | Show carrying value and the delta beside principal | Disclose the basis for committee use |
| Minor | CP-1 | Inference that the December 31, 2025 borrowing base was below commitments | Stated capacity of 1.97 billion versus 2,000 less 21.2 = 1,978.8 may reflect truncation, so the inference is firmer than the evidence | None | Soften to a possibility | Disclosure only |
| Minor | CP-2 | Illustrative cover floor and leverage break-even | Rest on an assumed incremental loan rate and chosen thresholds | None | Keep as sensitivities, outside committee numbers | Disclosure only |

All other sampled calculations recomputed exactly from cited inputs (see the calculation register); sign conventions, periods and units matched, and no pro forma adjustment was applied other than the labelled 9,111.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Ranking of the 2031 and 2034 notes as unsecured behind secured debt; incremental term loan carrying the term loan's security; 101% put on change of control; covenant compliance | Executed indentures, term loan credit agreement and incremental amendment | Only note summaries in the quarterly report are supplied; the security of the incremental loan is inferred from its being incurred under the same agreement | Mark as Source Limitation; obtain the executed documents | Legal review required before any ranking or put statement is relied on |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | No relative value, spread, price or ranking claim is made | Ratings, quotes, spreads and peers (blank in the run context) | Nothing to audit; the absence is correctly stated as Not supplied | None; keep Not supplied | None; market data cannot support or contradict the view |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | The Kodiak share-count conflict (13.2 million versus 13.3 million) omits the 10-Q Q2 2026 footnote showing 13.2 million consideration shares plus 0.1 million rollover shares, which may explain the difference; the 2.25 billion versus 2.22 billion size conflict stands | Annual report versus quarterly report | Add the footnote to the conflict entry without reconciling the size | Share count used for dilution |
| Minor | CP-1, CP-2 | The same revolver figure of 1,930 is labelled undrawn committed facilities, borrowing capacity and availability | Naming drift only | Use one label | Reader confusion only |

Checks that passed: issuer id, entity names, period labels, EBITDA of 724.8, borrowings of 6,111, liquidity of 4,704 and maturities agree across modules; the logged Kodiak size conflict is carried and not silently resolved.

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Duplicative content | The add-back share (52.3%) and the run-rate cover (1.81x) are each restated in two or three sections of the credit synthesis | Keep one statement and refer to it | Reading effort only |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | YAML front matter, Evidence Trace and Source Registry headings | Absent under the Markdown transport, which prescribes six other headings; not a defect of the authors | Record once; no change | None for the downstream consumer in this run |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1A | Missing citation | Series C cash redemption right lacks quote and locator | Add locator | Must-fix before committee | Open |
| CP5-002 | Material | CP-2 | Wrong attribution | Management plan to more than double EBITDA cited to a module that does not carry it | Cite release or remove | Must-fix before committee | Open |
| CP5-003 | Material | CP-1 | Definition basis | Debt at principal; carrying value and delta not logged; 8.33x versus 8.43x | Show both | Disclose for committee use | Open |
| CP5-004 | Material | CP-1, CP-2 | Legal source limitation | Ranking, put and covenant statements rest on note summaries; incremental loan security inferred | Obtain executed documents; label | Legal review required | Open |
| CP5-005 | Minor | CP-1 | Logic overreach | December 31, 2025 borrowing base inference firmer than evidence | Soften | Disclosure only | Open |
| CP5-006 | Minor | CP-2 | Assumption-based figure | Cover floor 1.27x and break-even thresholds rest on assumptions | Keep labelled | Disclosure only | Open |
| CP5-007 | Minor | CP-1A | Wording | Series C investor description more specific than the filing | Reword | Disclosure only | Open |
| CP5-008 | Minor | CP-1A | Conflict handling | Kodiak share-count conflict omits explanatory footnote | Add footnote | Downstream dilution input | Open |
| CP5-009 | Minor | CP-1, CP-2 | Label drift | Revolver figure labelled three ways | Use one label | Reader confusion only | Open |
| CP5-010 | Minor | CP-1, CP-1A, CP-2 | Market data absent | No market or relative value claim; inputs blank | Keep Not supplied | None | Open |
| CP5-011 | Minor | CP-2 | Duplication | Add-back and coupon figures repeated | Keep one statement | Reading effort only | Open |
| CP5-012 | Minor | All | Envelope | No YAML envelope or trace headings under this transport | Record once | None | Open |

#### Remediation priority map

1. Must-fix before committee: CP5-001 (add the locator for the Series C redemption right); CP5-002 (cite the earnings release for the EBITDA ambition as management language, or remove it); CP5-003 (show carrying value 6,040 beside principal 6,111, and the 8.33x ratio); CP5-004 (obtain the executed documents or label the ranking and put statements as Source Limitation).
2. Must-fix before the handoff is consumed downstream: none beyond the items above; no later module in this run depends on a corrected value.
3. Monitoring follow-up: CP5-006, CP5-008 and the gaps CP-5-GAP-001 to CP-5-GAP-004; re-audit when the September 2026 quarter report is available.
4. Formatting and hygiene: CP5-005, CP5-007, CP5-009, CP5-010, CP5-011, CP5-012.

#### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 4. Minor Issues: 8. Committee Use: Restricted.

No finding changes the direction of the credit view, but four material points (two unsupported attributions, the debt measurement basis and the absence of executed legal documents) must be cleared or disclosed, and post-closing leverage, cover and liquidity remain Not calculable. qa_status is Restricted under the severity engine.

## Calculations

New calculations in this module, from inputs already in the handoffs; US dollars in millions.

1. Debt on carrying value: June 30, 2026 long-term debt net 6,029 plus revolver 11 = 6,040 (principal 6,111; delta 71). Gross leverage 6,040 / 724.8 = 8.33x; net leverage (6,040 - 2,774) / 724.8 = 3,266 / 724.8 = 4.51x. December 31, 2025: carrying 3,057.3 against principal 3,100.0 (delta 42.7), gross leverage 3,057.3 / 647.8 = 4.72x. March 31, 2026: carrying 3,058.6 against 3,100.0 (delta 41.4), gross leverage 3,058.6 / 658.0 = 4.65x. Difference at June 30, 2026: 8.43x - 8.33x = 0.10x.
2. Recomputation checks, all agreeing with the handoffs: LTM Adjusted EBITDA 647.8 + 273 - 196 = 724.8; cash interest 138.0 + 106 - 23 = 221.0; cover 724.8 / 221.0 = 3.28x; liquidity 2,774 + 1,930 = 4,704; borrowings 6,100 + 11 = 6,111 and 6,111 + 3,000 = 9,111; add-backs 127.5 + 48.6 + 78.7 + 68.9 + 51.7 + 3.7 = 379.1; coupon run-rate 47.9 + 151.9 + 97.5 + 103.1 + 0.5 = 401.0; floating share 861 / 6,111 = 14.1% and 3,861 / 9,111 = 42.4%.
3. Revolver arithmetic: 2,000 - 21.2 = 1,978.8 (December 2025 and March 2026 letters of credit) against stated capacities of 1.97 billion and 1.98 billion; 2,000 - 11 - 62 = 1,927 against 1.93 billion at June 30, 2026.
4. Counts for the issue log: Critical 0, Material 4, Minor 8, total 12.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| TopBuild earnings, cash, debt treatment and purchase accounting not reported (CP-5-GAP-001) | Post-closing leverage, cover and liquidity Not calculable; confidence capped at Low for the enlarged group | Re-run after the September 2026 quarter report if filed by the cutoff |
| Executed legal documents not supplied (CP-5-GAP-002) | Ranking, covenant and put statements remain Source Limitation | Obtain exhibits |
| Incremental term loan margin (CP-5-GAP-003), related-party and ownership updates (CP-5-GAP-004) | Run-rate interest and control assessment incomplete | Obtain amendment and proxy statement |
| Ratings and market data blank (CP-5-GAP-005); revolver ratio not reported (CP-5-GAP-006) | No market-based audit; covenant headroom on the trigger only | Not supplied |
| Confidence Score not computed here | Band stated as Low from the Restricted status; numeric score unavailable | Run the scoring script in the full pipeline |
| Audit sample | Twenty-three statements were opened and quoted; the remaining statements in the handoffs were checked for consistency and arithmetic but not each quoted | Extend the sample if the committee requires a full trace |

## Next module

No further module is requested in this run. The report should show the four material points as disclosures, carry the clearance statement above, and be re-audited when the September 2026 quarter report is available.
