## Request

Module CP-5, evidence trace and research-integrity review, for OPENLANE, Inc. (issuer id opln) as of 2026-11-05, pathway credit_snapshot. It traces the claims of the source-readiness, financial-base, business-context and credit-synthesis handoffs to the seven pinned filings and slide decks, recomputes the calculations, logs conflicts and sets the committee-use status. It changes no credit conclusion and silently repairs nothing; corrections are stated here.

## Sources

### Issuer sources re-opened for this trace

| ID | Source (exact name) | sha256 | Short name |
| --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_opln-20251231.htm.jsonl | 26a1eb6e044eb7884447c1771579bc95b55527d93c8454714335cfb05faebcc7 | 10-K FY2025 |
| S2 | 10-Q_2026-03-31_opln-20260331.htm.jsonl | c46e877ea2548ae22544a835acae1b3618984f266ca5c5f8d9f1ce170a2f3661 | 10-Q Q1 |
| S3 | 10-Q_2026-06-30_opln-20260630.htm.jsonl | 47753528b639818941177074a5796fb5ee4c271e3e7cb89f9ddc4bf548a73b8f | 10-Q Q2 |
| S4 | 10-Q_2026-09-30_opln-20260930.htm.jsonl | 9682e191d9ec651d5722722ac8ff03e1ea87ff7ece0722d12fcb449d04d13357 | 10-Q Q3 |
| S5 | EX-99.3_2026-05-05_q12026openlaneearningssl.htm.jsonl | 2fc56068f78381bd02bfbe329da47d9ab40d86ee26db869d39406949616dc5f0 | Deck Q1 |
| S6 | EX-99.3_2026-08-04_q22026openlaneearningssl.htm.jsonl | 458d3c1fac99aaeefe126a46b683e88ca11580e6032ddf67da49e980bf2bff5d | Deck Q2 |
| S7 | EX-99.3_2026-11-04_q32026openlaneearningssl.htm.jsonl | bc88d193632549ac9eb968d3349190fc1ffa3b0842d97894dce16151e37cfd9a | Deck Q3 |

### Other pinned input

| Input | sha256 | Use |
| --- | --- | --- |
| context | 2fd2835b16fcd6e36fa06485261ee15d20c3a0b3f6cb56cfce407e6993d9ef70 | Run settings only; not issuer evidence. Ratings, market data and peers are blank, and blank is not zero. |

### Handoffs reviewed

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 822af9f32f30d6c0feeb6f1f36ee177a40b0f0ee61b0286bf38226d8998cb018 | Source readiness; opened and re-anchored |
| CP-1 | 27cde0aafcf9a133517adb102e5557dc8e810ad505a4dc1f22e1f42860aed45f | Financial base; every figure re-traced |
| CP-1A | 47b5129c30bcd183ee2afab5505e28425411f08dbab77100718b6ed693727913 | Business and transaction context; quotes re-matched |
| CP-2 | 52caee617ef31eca8dbb74e9195aa7e967b4b0dd37e1a45dab0427051fcd89ec | Credit synthesis; claims re-traced |

A locator `page:N` is the source chunk number in the pinned file, not the printed page. Quotes are exact substrings of the cited chunk.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial base and credit view trace to the filings: headline figures recompute and quotes match. Four wording points need correction, and covenant, guarantor and securitization capacity claims rest on filing summaries. Committee use is restricted. | Medium | The credit agreement, securitization agreements and guarantor list are absent, so covenant definitions, headroom and ranking cannot be tested. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every headline figure traced to a filing page and recomputed, including total debt of USD 545.9 million, leverage of 1.43x and liquidity of USD 650.2 million. | The core leverage and liquidity view can be relied on as stated. | High |
| The December 31, 2025 collateral figure in the annual report was corrected by the 2026 quarterly filings. | Collateral coverage must use USD 2,448.2 million, and both figures stay logged. | High |
| The reported covenant ratio of 0.9x is sourced, but its definition rests on an agreement that is not supplied. | Headroom of 2.6x is the company's figure and cannot be independently tested. | Medium |
| Four wording points need correction: Canadian guarantor scope, customer exposure called spread, two leverage descriptors, and an undated dealer statistic. | No figure changes, but the statements need the stated qualification. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 3 are calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the executed credit and securitization agreements, which matters because covenant definitions, headroom and the position of corporate creditors behind the securitized receivables rest on the company's own summaries, and implies restricted committee use for covenant, guarantor and ranking statements. Headline leverage, liquidity and funding figures recompute from filed pages. Four minor wording points in earlier handoffs are corrected in this review.

### Handoff review

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | opln-2026-11-05-credit_snapshot-host, CP-0 response | Source readiness for the four consumers | High: quotes re-matched to filed pages | Six H2 headings present and in order | Accepted by structure check; content reviewed here | Gap list matches this review |
| CP-1 | opln-2026-11-05-credit_snapshot-host, CP-1 response | Financial base, four chart tables | High: filed statements and printed LTM tables | Six H2 headings present and in order | Accepted by structure check; content reviewed here | One wording point (E1); analyst maturity schedule labelled |
| CP-1A | opln-2026-11-05-credit_snapshot-host, CP-1A response | Business, ownership, timeline, governance | High for filed facts; Medium for deck statements | Six H2 headings present and in order | Accepted by structure check; content reviewed here | Dealer-concentration date carried only by CP-1A |
| CP-2 | opln-2026-11-05-credit_snapshot-host, CP-2 response | Credit synthesis | High where it cites CP-1 figures | Six H2 headings present and in order | Accepted by structure check; content reviewed here | Three wording points (E2 to E4) |

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_opln-20251231.htm.jsonl | High: filed, audited | Year ended December 31, 2025, with 2024 and 2023 comparatives | OPENLANE, Inc., consolidated | Statements, debt table, contractual obligations, business description, risk factors, quarterly 2025 EBITDA bridge | Flattened tables; executed agreements not attached | Financial base, business context |
| S2 | 10-Q_2026-03-31_opln-20260331.htm.jsonl | High: filed, unaudited | Quarter ended March 31, 2026 | Consolidated | Statements, debt table, liquidity, covenant ratio, LTM bridge | Flattened tables | Quarterly columns, LTM |
| S3 | 10-Q_2026-06-30_opln-20260630.htm.jsonl | High: filed, unaudited | Three and six months ended June 30, 2026 | Consolidated | Statements, debt table, liquidity, covenant ratio, LTM bridge | Flattened tables | Quarterly columns, LTM |
| S4 | 10-Q_2026-09-30_opln-20260930.htm.jsonl | High: filed, unaudited | Three and nine months ended September 30, 2026 | Consolidated | Statements, debt, securitization, liquidity, covenant, LTM bridge, subsequent event | Flattened tables; column headings split across chunks | Latest position |
| S5 | EX-99.3_2026-05-05_q12026openlaneearningssl.htm.jsonl | Medium: furnished, management | Q1 2026 | Consolidated and two segments | Reconciliations, guidance | Charts absent; non-GAAP measures | Cross-check only |
| S6 | EX-99.3_2026-08-04_q22026openlaneearningssl.htm.jsonl | Medium: furnished, management | Q2 2026 | Consolidated and two segments | Reconciliations, guidance | Charts absent; non-GAAP measures | Cross-check only |
| S7 | EX-99.3_2026-11-04_q32026openlaneearningssl.htm.jsonl | Medium: furnished, management | Q3 2026 | Consolidated and two segments | Segment Adjusted EBITDA by quarter, management letter, revised guidance | Charts absent; non-GAAP measures | Segment view, cross-check |

Module status: Ready with Limitations. All four upstream handoffs and all seven sources are available; the executed agreements, ratings and proxy content are not. Traceability scope: Top 5 drivers plus every figure that appears in a reader summary. Entity key: issuer id opln is present.

### Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Corporate leverage and covenant position | CP-1, CP-2 | Total debt 545.9 over LTM Adjusted EBITDA 382.7 gives 1.43x; reported covenant ratio 0.9 against a 3.5 maximum | Low leverage on a measure that already deducts securitization interest limits default risk from corporate debt | Supports a sound corporate profile; covenant headroom is the company's figure | S4 page:17, page:54, page:59 | Credit Agreement definitions not supplied |
| 2 | Securitization funding outside corporate debt | CP-1, CP-1A, CP-2 | Gross obligations 2,084.4 against receivables managed 2,763.5, 75.4% | Receivable-backed funding, not the term loan, is the largest funded claim, so credit losses and facility access drive refinancing risk | Decides whether the corporate view holds | S4 page:16, page:40, page:57 | Facility-level balances and undrawn capacity not supplied |
| 3 | Liquidity | CP-1, CP-2 | Cash 244.9 plus undrawn revolver availability 405.3 gives 650.2 | Revolvers have no borrowings and term-loan amortization is 5.5 a year, so near-term repayment does not depend on market access | Low liquidity risk to the revolver maturity in June 2028 | S4 page:2, page:20, page:21, page:56 | Securitization capacity excluded |
| 4 | Cash generation and receivable funding | CP-1, CP-2 | Nine-month free cash flow 268.8; 224.1 after receivable growth of 367.6 funded 322.9 by securitization | Operating cash flow excludes the funding of the receivable book, so the headline overstates cash retained | Cash available for debt reduction is lower than free cash flow | S4 page:4 | Quarterly timing of receivable funding not supplied |
| 5 | Revenue durability | CP-1A, CP-2 | Commercial vehicles sold up 46% in Q3 2026, 17% excluding the latest customer; yield 2.5% against 2.9%; customers can terminate for convenience | Volume rests on large consignment relationships and mix dilutes yield | Revenue visibility is moderate | S4 page:37, page:38; S7 page:4; S1 page:26 | No customer names or contract terms; the 17% is a deck statement |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 545.9 and LTM Adjusted EBITDA 382.7 give 1.43x | CP-1, CP-2 | S4 page:17 debt table; S4 page:59 LTM bridge; recomputed | Yes | High: filed | Calculated | Recomputed, agrees | High | Committee-Ready |
| Net debt over Adjusted EBITDA 0.79x | CP-1, CP-2 | Cash 244.9 at S4 page:2; restricted cash 34.7 excluded | Yes | High: filed | Calculated | Recomputed, agrees | High | Committee-Ready |
| Reported covenant ratio 0.9 against 3.5 maximum | CP-1, CP-2 | S4 page:54 | Yes | High: filed | Directly Sourced | Figure matches filing | Medium | Committee-Ready |
| Covenant headroom 2.6 | CP-1, CP-2 | 3.5 less 0.9; definitions in an unsupplied agreement | Partial | Medium: management-reported | Calculated | Arithmetic agrees; meaning unverified | Medium | Remediation Needed |
| Securitization gross obligations 2,084.4 and 75.4% of receivables managed | CP-1, CP-2 | S4 page:16, page:40 | Yes | High: filed | Directly Sourced | Recomputed, agrees | High | Committee-Ready |
| Dec 31, 2025 collateral 2,803.5 against 2,448.2 | CP-0, CP-1, CP-1A, CP-2 | S1 page:77; S4 page:16 | Yes | High: filed, two versions | Conflicting | Logged, not reconciled; corrected figure used | High | Committee-Ready |
| Liquidity 650.2 | CP-1, CP-2 | S4 page:2, page:21 | Yes | High: filed | Calculated | Recomputed, agrees | High | Committee-Ready |
| Free cash flow 268.8 and 224.1 after receivable funding | CP-1, CP-2 | S4 page:4 | Yes | High: filed | Calculated | Recomputed, agrees | High | Committee-Ready |
| Corporate net interest 37.3 and accrual cover 10.26 | CP-1, CP-2 | S4 page:59 | Yes | High: filed | Calculated | Recomputed, agrees | High | Committee-Ready |
| Finance is 48.3% of LTM Adjusted EBITDA | CP-1, CP-2 | S7 page:6, page:7 | Yes | Medium: management deck | Calculated | Recomputed, agrees | Medium | Committee-Ready |
| Commercial growth 46%, 17% excluding the latest customer | CP-1A, CP-2 | S4 page:38; S7 page:4 | Yes | High for 46%; Medium for 17% | Directly Sourced | 17% is Management Language | Medium | Committee-Ready |
| Debt maturity schedule by year | CP-1 | Installment of 0.25% on 550.0 and an assumption of quarter-end payments | Partial | Medium: analyst schedule | Assumption-Based | Labelled in CP-1 | Medium | Committee-Ready |
| Preferred repurchase classified Neutral or Mixed | CP-1A, CP-2 | S4 page:22 and the CP-1 debt table | Yes | High for actions | Analyst Inference | Labelled | Medium | Committee-Ready |
| Floating-rate term debt is unhedged | CP-2 | S1 page:88 | Yes | High: filed | Directly Sourced | Quote matches | High | Committee-Ready |
| Customer exposure is spread | CP-2 | S1 page:26 states only that no customer reached 10% | Partial | High for the threshold | Analyst Inference | Stronger than the source | Low | Remediation Needed |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt is 545.9 at September 30, 2026 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:17, Note 6 | CP-1 debt stack | Sourced | High | 10-Q Q3 page:17 "Total debt $ 545.9 $ 550.0" |
| Term loan matures October 8, 2032 at Adjusted Term SOFR plus 2.50% | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:17 | CP-1 debt stack | Sourced | High | 10-Q Q3 page:17 "Adjusted Term SOFR + 2.50% October 8, 2032" |
| Installments are 0.25% of original principal each quarter | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:18 | CP-1 maturities | Sourced | High | 10-Q Q3 page:18 "payable in quarterly installments equal to 0.25% of the original aggregate principal amount" |
| LTM Adjusted EBITDA is 382.7 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:59, LTM bridge | CP-1 leverage | Sourced | High | 10-Q Q3 page:59 "Adjusted EBITDA $ 76.0 $ 96.7 $ 103.2 $ 106.8 $ 382.7" |
| FY2025 Adjusted EBITDA is 332.6 | Pack 1395942-openlane-inc-opln | 10-K_2025-12-31_opln-20251231.htm.jsonl | S1 | page:79 | CP-1 leverage | Sourced | High | 10-K FY2025 page:79 "Adjusted EBITDA $ 82.8 $ 86.7 $ 87.1 $ 76.0 $ 332.6" |
| Cash and cash equivalents are 244.9 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:2, balance sheet | CP-1 liquidity | Sourced | High | 10-Q Q3 page:2 "Cash and cash equivalents $ 244.9 $ 141.5" |
| 405.3 is available under the revolvers after 42.6 of letters of credit | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:56 | CP-1 liquidity | Sourced | High | 10-Q Q3 page:56 "there was an additional $405.3 million available for borrowing under the Revolving Credit Facilities (net of $42.6 million in outstanding letters of credit)" |
| Covenant maximum is 3.5 and the reported ratio is 0.9 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:54 | CP-1 covenants | Sourced | High | 10-Q Q3 page:54 "Our Consolidated Senior Secured Net Leverage Ratio was 0.9 at September 30, 2026" |
| Gross securitization obligations are 2,084.4 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:16 | CP-1 securitization | Sourced | High | 10-Q Q3 page:16 "Obligations collateralized by finance receivables, gross $ 2,084.4 $ 1,771.7" |
| Total receivables managed are 2,763.5 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:40 | CP-1 securitization | Sourced | High | 10-Q Q3 page:40 "Total receivables managed $ 2,763.5 $ 2,489.3" |
| December 31, 2025 collateral was given as 2,803.5 and later corrected | Pack 1395942-openlane-inc-opln | 10-K_2025-12-31_opln-20251231.htm.jsonl; 10-Q_2026-09-30_opln-20260930.htm.jsonl | S1; S4 | S1 page:77; S4 page:16 | CP-0, CP-1, CP-1A, CP-2 | Conflicting | High | 10-K FY2025 page:77 "$2,803.5 million and $2,335.1 million, respectively"; 10-Q Q3 page:16 "reflects the correction of an error from the $2,803.5 million previously disclosed in the 2025 Form 10-K" |
| About 70% to 75% of the receivable portfolio is securitized | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:60 | CP-1A, CP-2 | Sourced | High | 10-Q Q3 page:60 "approximately 70% to 75% of AFC’s finance receivables portfolio is funded through its securitization facilities" |
| Operating cash flow was 309.5 for nine months 2026 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:4 | CP-1 cash flow | Sourced | High | 10-Q Q3 page:4 "Net cash provided by operating activities 309.5 266.4" |
| Finance receivables rose 367.6 and securitization obligations rose 322.9 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:4 | CP-1 cash flow | Sourced | High | 10-Q Q3 page:4 "Net increase in finance receivables held for investment (367.6) (196.1)" |
| LTM interest expense net of interest income is 37.3 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:59 | CP-1 interest cover | Sourced | High | 10-Q Q3 page:59 "Interest expense, net of interest income 9.6 9.7 9.0 9.0 37.3" |
| Cash paid for interest was 115.4 in FY2025 and 102.3 in nine months 2026 | Pack 1395942-openlane-inc-opln | 10-K_2025-12-31_opln-20251231.htm.jsonl; 10-Q_2026-09-30_opln-20260930.htm.jsonl | S1; S4 | S1 page:94; S4 page:5 | CP-1 interest cover | Sourced | High | 10-Q Q3 page:5 "Cash paid for interest $ 102.3 $ 85.6" |
| Commercial vehicles sold rose 46% in Q3 2026 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:38 | CP-1A, CP-2 | Sourced | High | 10-Q Q3 page:38 "a 46% increase in commercial vehicles sold" |
| 17% excluding the latest commercial customer | Pack 1395942-openlane-inc-opln | EX-99.3_2026-11-04_q32026openlaneearningssl.htm.jsonl | S7 | page:4 | CP-1A, CP-2 | Sourced | Medium | Deck Q3 page:4 "a 46% increase in commercial volumes, or 17% excluding the addition of our latest commercial customer" |
| Customers can terminate for convenience and no customer reached 10% of revenue | Pack 1395942-openlane-inc-opln | 10-K_2025-12-31_opln-20251231.htm.jsonl | S1 | page:26 | CP-1A, CP-2 | Sourced | High | 10-K FY2025 page:26 "no single customer accounted for 10% or more of our consolidated revenues in 2025" |
| Floating-rate debt is not hedged | Pack 1395942-openlane-inc-opln | 10-K_2025-12-31_opln-20251231.htm.jsonl | S1 | page:88 | CP-2 | Sourced | High | 10-K FY2025 page:88 "We do not currently use interest rate contracts to manage our exposure to interest rate changes" |
| After a termination event banks may take the stock of AFC Funding Corporation | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:57 | CP-2 | Sourced | High | 10-Q Q3 page:57 "the banks may, and could, cause the stock of AFC Funding Corporation to be transferred to the bank facility" |
| Series A was repurchased with term-loan proceeds | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:22 | CP-1A, CP-2 | Sourced | High | 10-Q Q3 page:22 "The shares of Series A Preferred Stock were repurchased primarily with proceeds from the 2025 Incremental Term Loans" |
| Canadian tax reversal of 15.9 and a 20.2 benefit in nine months 2026 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:46 | CP-1A, CP-2 | Sourced | High | 10-Q Q3 page:46 "The $20.2 million benefit related to the rescission of the Canadian digital service tax" |
| Segment Adjusted EBITDA by quarter gives Finance 185.0 of 382.7 | Pack 1395942-openlane-inc-opln | EX-99.3_2026-11-04_q32026openlaneearningssl.htm.jsonl | S7 | page:6, page:7 | CP-1, CP-2 | Calculated | Medium | Deck Q3 page:6 "Adjusted EBITDA $57.8 $49.0 $106.8"; page:7 "Adjusted EBITDA $31.6 $44.4 $76.0" |
| AFC has no dealer above 2.5% of its portfolio at December 31, 2025 | Pack 1395942-openlane-inc-opln | 10-K_2025-12-31_opln-20251231.htm.jsonl | S1 | page:15 | CP-1A, CP-2 | Sourced | High | 10-K FY2025 page:15 "no one dealer representing greater than 2.5% of our portfolio" |
| Third Amendment to the Credit Agreement is dated June 30, 2026 | Pack 1395942-openlane-inc-opln | 10-Q_2026-09-30_opln-20260930.htm.jsonl | S4 | page:68 | CP-1, CP-1A | Sourced | High | 10-Q Q3 page:68 "Third Amendment Agreement, dated as of June 30, 2026"; terms not described |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA at Q1, Q2 and Q3 2026 | CP-1 leverage | Four quarters of Adjusted EBITDA | Sum of last four quarters: 346.5, 363.0, 382.7 | Calculated | Equals company-printed LTM at each date | High | PD, leverage | S2 page:44; S3 page:56; S4 page:59 |
| Total debt / Adjusted EBITDA | CP-1, CP-2 | Debt 568.0, 547.2, 545.9 and 550.0 and 230.7; Adjusted EBITDA as above | Debt divided by LTM Adjusted EBITDA: 1.64, 1.51, 1.43, 1.65, 0.79 | Calculated | Recomputed, agrees | High | PD, leverage | S2 page:15; S3 page:17; S4 page:17; S1 page:122 |
| Net debt / Adjusted EBITDA | CP-1, CP-2 | Cash 180.1, 189.7, 244.9, 141.5, 143.0; restricted cash excluded | (Debt less cash) divided by LTM Adjusted EBITDA: 1.12, 0.98, 0.79, 1.23, 0.30 | Calculated | Recomputed, agrees | High | PD, liquidity | S2 page:2; S3 page:2; S4 page:2; S1 page:92 |
| LTM cash paid for interest | CP-1 interest cover | FY2025 115.4 less prior-year year-to-date plus current year-to-date | 122.7, 123.9, 132.1 | Calculated | Recomputed, agrees | High | Coverage | S1 page:94; S2 page:4; S3 page:5; S4 page:5 |
| EBITDA / cash interest | CP-1, CP-2 | LTM EBITDA 425.0, 440.2, 451.5 and 408.7 and 396.8 | EBITDA divided by cash interest: 3.46, 3.55, 3.42, 3.54, 2.82 | Calculated | Recomputed, agrees; perimeter matched (both before securitization interest) | High | Coverage | S4 page:59; S1 page:79 |
| Adjusted EBITDA / interest net of interest income | CP-1, CP-2 | 332.6 over 14.9; 346.5 over 21.2; 363.0 over 28.9; 382.7 over 37.3 | Quotient: 22.32, 16.34, 12.56, 10.26 | Calculated | Recomputed, agrees; perimeter matched (both after securitization interest) | High | Coverage | S1 page:79; S2 page:44; S3 page:56; S4 page:59 |
| Liquidity | CP-1, CP-2 | Cash plus revolver availability | 551.4, 588.3, 595.4, 650.2 | Calculated | Recomputed, agrees | High | Liquidity | S1 page:76; S2 page:35; S3 page:47; S4 page:50 |
| Free cash flow and after receivable funding | CP-1, CP-2 | 309.5, 40.7, 367.6, 322.9 | 309.5 less 40.7 is 268.8; less 367.6 plus 322.9 is 224.1 | Calculated | Recomputed, agrees | High | Cash conversion | S4 page:4 |
| Securitization share and collateral coverage | CP-1, CP-2 | 2,084.4; 2,763.5; 2,786.7; 1,771.7; 2,423.5; 2,448.2 | 75.4%, 73.1%, 1.34x, 1.38x | Calculated | Recomputed, agrees | High | Refinancing | S4 page:16, page:40 |
| Debt service cover | CP-2 | 382.7 over (37.3 plus 5.5) | 8.94x | Calculated | Recomputed, agrees; annual amortization 5.5 per S4 page:3 current maturities | High | Debt service | S4 page:3, page:59 |
| Debt maturity schedule by year | CP-1 | Assumption: installments of 1.375 on each quarter-end to September 30, 2032, no prepayment, balance on October 8, 2032 | 1.4, 5.5 for each of 2027 to 2031, 517.0 in 2032; sum 545.9 | Assumption-Based | Labelled as analyst schedule in CP-1 | Medium | Refinancing | S4 page:17, page:18 |
| Finance share of LTM Adjusted EBITDA | CP-1, CP-2 | 185.0 over 382.7 | 48.3% | Calculated | Recomputed, agrees | Medium | Earnings concentration | S7 page:6, page:7 |

### Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant headroom of 2.6 | Rests on a ratio whose definition is in an executed agreement that is not supplied | Weak Lineage | Headroom drives the view of default risk and distribution capacity | Obtain the Credit Agreement and compliance detail | CP-1 covenants table; CP-2 strengths |
| Material | Structural position of corporate creditors | Statements on security, guarantors and the AFC Funding Corporation shares rest on filing summaries | Weak Lineage | Loss given default for the term loan depends on what is pledged | Obtain security documents and guarantor schedule | CP-2 weaknesses and risks |
| Minor | Customer exposure is spread | Stronger than the source, which gives only a 10% threshold | Analyst Inference | Concentration below 10% can still be material | Reword to the threshold | CP-2 strengths |
| Minor | Canadian revolver guarantors | Wording implies all guarantors are limited to Canadian obligations | Directly Sourced | The limit applies to the Canadian subsidiaries only | Reword | CP-1 debt stack |
| Minor | Leverage descriptors | CP-2 uses moderately leveraged in the credit view and lightly levered in the thesis | Analyst Inference | The same figure should carry one descriptor | State one descriptor | CP-2 credit view and thesis |
| Minor | AFC dealer concentration | CP-2 omits the December 31, 2025 date given in the business context handoff | Directly Sourced | A year-end statistic read as current | Add the date | CP-2 strengths |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Committee-Ready | Seven filings and decks cover FY2025 and three 2026 quarters; every page was retained | Complete coverage removes selection risk for the financial base | Headline figures can be used | None for the base; agreements needed for legal claims |
| Citation completeness | Ready with Remediation | Every quoted passage matched its page; two inferences are stronger than their sources | Overstated wording can shift weight in a committee | Minor wording corrections | Apply E1 to E4 |
| Calculation traceability | Committee-Ready | Every ratio and sum recomputed from printed inputs and agrees; LTM sums equal printed LTM tables | Reproducible figures lower model risk | Leverage, cover and liquidity may be relied on | None |
| Assumption transparency | Committee-Ready | The only assumption, the maturity schedule, is labelled as analyst-owned | Unlabelled assumptions would pass as filed facts | Maturity timing is indicative | None |
| Markdown/export artifact integrity | Ready with Remediation | Six H2 headings in order in each handoff; text extraction flattens tables | A split column heading could misplace a figure, as in the liquidity table | Low risk after recomputation | Check flagged tables against filed HTML when available |

### Cross-module consistency

The four handoffs tell one story and no figure conflicts. All use the same periods (FY2025, Q3 2026, nine months 2026, LTM Q3 2026), the same total debt of USD 545.9 million, Adjusted EBITDA of USD 382.7 million, liquidity of USD 650.2 million and securitization obligations of USD 2,084.4 million, and all carry the corrected December 31, 2025 collateral figure. The credit synthesis repeats the financial base ratios exactly and adds one calculation, which recomputes. One definitional difference is recorded rather than resolved: the company Adjusted EBITDA deducts securitization interest while the Credit Agreement covenant EBITDA is defined separately, and the financial base keeps the two apart. CP-0 states that guarantor names are not in the text read; CP-1 states the Canadian guarantor limit correctly in substance but with imprecise wording (E1). No handoff alters an upstream conclusion.

### Issue log and clearance

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | Minor | CP-1 | Wording | Canadian revolver guarantors described as limited to Canadian obligations; the filing limits only the Canadian subsidiaries among them (10-Q Q3 page:20) | Say that certain domestic and Canadian subsidiaries guarantee, and the Canadian ones guarantee only Canadian obligations | None | Open: corrected here |
| E2 | Minor | CP-2 | Inference stated as fact | Customer exposure called spread on the strength of a 10% threshold alone | Say only that no customer reached 10% of revenue | Restricts concentration statements | Open: corrected here |
| E3 | Minor | CP-2 | Descriptor inconsistency | Moderately leveraged in the credit view and lightly levered in the thesis for the same 1.43x | Use low corporate leverage on the company measure | None | Open: corrected here |
| E4 | Minor | CP-2 | Period label | Dealer concentration of 2.5% lacks its December 31, 2025 date | Add the date | None | Open: corrected here |
| E5 | Material | All | Evidence gap | Credit Agreement and amendments including the June 30, 2026 Third Amendment, securitization agreements and guarantor schedule are not supplied | Obtain the executed documents | Restricts covenant, ranking and guarantor statements | Open |
| E6 | Material | CP-1, CP-2 | Evidence gap | Undrawn securitization capacity and facility-level balances are Not calculable | Obtain facility reports | Restricts liquidity statements beyond the revolvers | Open |
| E7 | Minor | CP-0, CP-1, CP-1A, CP-2 | Conflict | December 31, 2025 collateral of 2,803.5 against 2,448.2 | Cite both; use the corrected figure | None | Closed: logged consistently |

Research QA status: Restricted. Committee status: Restricted use. The headline credit view on leverage, liquidity, funding structure and cash flow is supported and may be used; statements on covenant headroom, the security and guarantor position of the term loan, undrawn securitization capacity, customer spread and the uniform leverage descriptor may not be used without the stated qualification. The confidence band is Medium; the numeric score was not computed because the confidence script is not available in this run.

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed agreements | Credit Agreement, three amendments, securitization and receivables purchase agreements | Covenant definitions, baskets and the pledge of AFC Funding Corporation shares decide headroom and loss given default | Covenant and ranking statements | High impact on confidence | Exhibits 10.1a to 10.1d, 10.10a to 10.10c, 10.11a to 10.11e |
| CP-5-GAP-002 | Guarantor list | Exhibit 21.1 and guarantor schedule | Structural analysis of the term loan | Guarantor statements | Medium impact | Annual report exhibit 21.1 |
| CP-5-GAP-003 | Securitization capacity | Facility-level balances, borrowing base and eligibility | Liquidity for the Finance book beyond the revolvers | Liquidity | Medium impact | Facility reports |
| CP-5-GAP-004 | Ownership after conversion | Current holdings of former preferred holders and any board right | Sponsor-alignment and control | Governance table | Medium impact | Proxy statement or beneficial ownership filings |
| CP-5-GAP-005 | Market data | Ratings, prices, peers | Market-implied view | Not used | Low impact | External sources if needed |
| CP-5-GAP-006 | Deck charts and events after November 4, 2026 | Chart data and later 8-Ks | Operating metrics and event completeness | Operating metrics | Low impact | Filed tables; later 8-Ks |

## Calculations

Independent recomputation from the cited filing pages, in USD millions unless stated. Every result agrees with the upstream value.

| Check | Inputs | Result | Upstream value | Agrees |
| --- | --- | --- | --- | --- |
| Total debt / Adjusted EBITDA, LTM Q3 2026 | 545.9 over 382.7 | 1.4264, rounded 1.43x | 1.43x | Yes |
| Net debt / Adjusted EBITDA, LTM Q3 2026 | (545.9 less 244.9) over 382.7 | 0.7865, rounded 0.79x | 0.79x | Yes |
| Total debt / Adjusted EBITDA, FY2025 and FY2024 | 550.0 over 332.6; 230.7 over 293.4 | 1.6536x; 0.7863x | 1.65x; 0.79x | Yes |
| EBITDA / cash interest, LTM Q3 2026 | 451.5 over (115.4 less 85.6 plus 102.3 = 132.1) | 3.4179x | 3.42x | Yes |
| Adjusted EBITDA / interest net of interest income, LTM Q3 2026 | 382.7 over 37.3 | 10.2601x | 10.26x | Yes |
| Debt service cover | 382.7 over (37.3 plus 5.5 = 42.8) | 8.9416x | 8.94x | Yes |
| Liquidity, September 30, 2026 | 244.9 plus 405.3 | 650.2 | 650.2 | Yes |
| Nine-month free cash flow and after receivable funding | 309.5 less 40.7; less 367.6 plus 322.9 | 268.8; 224.1 | 268.8; 224.1 | Yes |
| Securitization share of receivables managed | 2,084.4 over 2,763.5 | 75.43% | 75.4% | Yes |
| Collateral coverage | 2,786.7 over 2,084.4 | 1.3369x | 1.34x | Yes |
| LTM revenue and net income | 1,934.5 less 1,440.2 plus 1,643.7; 177.7 less 118.2 plus 137.9 | 2,138.0; 197.4 | 2,138.0; 197.4 | Yes |
| Finance share of LTM Adjusted EBITDA | (44.4 plus 45.1 plus 46.5 plus 49.0) over 382.7 | 48.34% | 48.3% | Yes |
| Maturity schedule sum | 1.375 plus 27.5 plus 4.125 plus 512.875 | 545.875 | 545.9 | Yes |
| Covenant headroom | 3.5 less 0.9 | 2.6 | 2.6 | Yes |

## Gaps

The material gaps are in the ledger above (CP-5-GAP-001 to CP-5-GAP-006). The two that restrict committee use are the executed agreements (CP-5-GAP-001) and the guarantor list (CP-5-GAP-002). Undrawn securitization capacity (CP-5-GAP-003) is Not calculable from the pack. Inherited from earlier modules: deck charts are not extracted, table headings are split across chunks in places, and nothing after November 4, 2026 is supplied. Readiness: CP-0 judged every consumer READY_WITH_LIMITATIONS, and this review agrees; module status is Ready with Limitations.

## Next module

This is the last module selected in this run. The committee questions that need executed agreements (CP-5-GAP-001) go to the first diligence request; apply corrections E1 to E4 when the earlier handoffs are next reissued, and use the corrected December 31, 2025 collateral figure of 2,448.2 in any downstream work.
