## Request

Independent evidence trace and research-integrity review of the source-readiness, financials, business and credit-synthesis handoffs for Karman Holdings Inc., as of 2026-11-05, run krmn-2026-11-05-credit_snapshot-host, current period Q2 2026, prior period FY2025, USD. Scope: re-trace the material claims to the pinned filings, recompute every derived figure, compare the handoffs with each other, and set the clearance for committee use. Upstream datapoints re-anchored: all four handoffs name the same issuer, as-of date, run and periods; no mismatch.

## Sources

Handoffs reviewed (each re-read in full against the filings):

| Module | sha256 | Reviewed for |
| --- | --- | --- |
| CP-0 | a57f99fe9744b1d0aa04b0d88c379e009e0884b36967de895c5494d12f697fd7 | Source coverage, conflicts, gaps |
| CP-1 | dab20e128dd129496297d28f1337579e0a80ba39af03113d7b2358b600763190 | Figures, ratios, debt terms, cash flow |
| CP-1A | 28ed11e7d584586fbbac6842b224c8a4b267d4f3bfd755d319310336f5769e21 | Business and transaction facts, conflicts, governance |
| CP-2 | 7999ad7705a563517c64a7538adaa49810335ac2475e34a6310a41c0b53cbb71 | Credit view, strengths, weaknesses, risks |

Issuer sources relied on (opened and searched; exact names and pinned sha256):

| Short label | Exact source name | sha256 |
| --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_krmn-20251231.htm.jsonl | 0fa827dd0460c76061ba265dfd87fbc19a2ff56540ecb41c37d9f3ae753ab0f4 |
| 10-Q Q3 2025 | 10-Q_2025-09-30_ck0002040127-20250930.htm.jsonl | 3c5c231bfb04f1c42c8d20fbb250b7bc5ec74eb6d48f2a2710f27ad86ac72e05 |
| 10-Q Q1 2026 | 10-Q_2026-03-31_krmn-20260331.htm.jsonl | 90e7595a8902330282bb884d4c9fe273eb1e7942ed1a19578c022c6bcce120c0 |
| 10-Q Q2 2026 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | 0091a807b74b21f9dc6486123e810e38b8a9fe16000395d642b5d4795d6a739b |
| EX-99.1 Mar 2026 | EX-99.1_2026-03-25_krmn-ex99_1.htm.jsonl | d8dada3ee5d9e4a87e859de5d525ad9f209fd3e2ccf4f9e6160bc138d4722137 |
| EX-99.1 May 2026 | EX-99.1_2026-05-12_krmn-ex99_1.htm.jsonl | eb41cf051f38bdba1a51e6ba92cdb3c052ebd58f3bfe5c3fbce46f0b31a31145 |
| EX-99.1 Aug 2026 | EX-99.1_2026-08-06_krmn-ex99_1.htm.jsonl | fac245494ef462dbc8a40ade20b74f17ca4a459208d7f0a0a96a35a60656408d |

Run context: context, sha256 87b8658c174a3590ff5e4601d51c62bc2c7fbb0a3a422b7e215e4d8a8cf451b8 (settings, not issuer evidence). Locators are source-chunk pages (page:N). Nothing dated after the cutoff 2026-11-05 was used; the latest source is dated 2026-08-06.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial figures trace to the filings and recompute exactly. One statement about backlog in the business and credit views is wrong and is corrected here. Use is restricted, not blocked. | Medium | The credit agreement and ownership are not supplied, so legal and structural claims cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every ratio, last-twelve-month figure, margin and add-back in the financial tables recomputed to its printed inputs with no mismatch. | Leverage, interest cover and liquidity figures can be relied on as calculations. | High |
| The business and credit views say the backlog definition widened in 2026, but the annual report's own key-measure note already carries the broader wording. | Backlog is an attributed indicator; remaining performance obligations of 703.9 million are the narrower measure. | High |
| Debt terms rest on filing notes only; covenant headroom, guarantors and security cannot be traced. | No legal or structural conclusion is supported yet. | High |
| Five conflicts between filings remain open and one of them has a plausible disclosed cause. | Transaction and exposure figures must be cited with their basis. | Medium |

### Evidence trace view

The analysis is traceable enough for a restricted committee read, and the most important provenance gap is the missing credit agreement. Of the claims traced, the figures in the financials handoff are Directly Sourced or Calculated, and every calculated cell reproduced from its inputs. The business handoff is mostly Directly Sourced, with a small set of Analyst Interpretations that it tags as such. One claim failed the trace: the business and credit views treat the backlog definition as having widened between the annual report and the 2026 quarterly reports, when the annual report's own key-measure note already carries the 2026 wording and states that no historical amount changed (10-K FY2025 page:99), while a risk-factor paragraph in the same annual report still uses the narrower wording (10-K FY2025 page:35). That is an unsupported directional claim, not a numeric error, and its consequence is that backlog cannot be used as evidence of a definitional change; it remains a management-reported measure that exceeds remaining performance obligations by a growing margin. The other defects are smaller. The strongest contrary evidence to the overall credit view is the liquidity position, and what would make it win is a post-amendment cash interest run rate and a funded Walker closing, both outside the sources. Committee status is Restricted: the financial and business conclusions may be used with the corrections below, and legal, covenant and recovery conclusions may not, because the credit agreement is absent.

### Source register (traceability gate)

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K FY2025 | High: filed, audited | Year ended December 31, 2025 | Karman Holdings Inc., consolidated | Statements, debt and lease notes, business, risk factors, subsequent events | Ownership incorporated by reference to a proxy; two backlog descriptions | Financials, business, credit |
| S2 | 10-Q Q3 2025 | High: filed, unaudited | Quarter and nine months to September 30, 2025 | Same | Coverage and cross-checks | Not used for any tabled figure | Coverage |
| S3 | 10-Q Q1 2026 | High: filed, unaudited | Quarter to March 31, 2026 | Same | Balance sheet, debt, reconciliation | Seemann purchase accounting later revised | Financials |
| S4 | 10-Q Q2 2026 | High: filed, unaudited | Quarter and six months to June 30, 2026 | Same | Statements, debt, Walker, controls | No maturity table; cash flow cumulative | Financials, business, credit |
| S5 | EX-99.1 Mar 2026 | Medium: issuer release | Q4 and FY2025 | Same | Quarterly end-market revenue, backlog | Management and non-GAAP | Business |
| S6 | EX-99.1 May 2026 | Medium: issuer release | Q1 2026 | Same | Revolver upsizing | Management | Business |
| S7 | EX-99.1 Aug 2026 | Medium: issuer release | Q2 2026 | Same | Outlook, Walker, repricing | Management; outlook is a projection | Business |

### Top credit drivers and traceability

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Net leverage rose from 3.25x to 4.00x of LTM Adjusted EBITDA as acquisition debt was added | CP-1 | Debt principal 768,478 thousand against 506,767 thousand; LTM Adjusted EBITDA 179,068 thousand | Debt grew faster than earnings; LTM omits full-year contribution of acquired businesses | Sets leverage tolerance and refinancing capacity | S4 pages 2, 18, 35; S1 pages 101, 139 | Not pro forma; term loan size conflict |
| 2 | Negative operating and free cash flow | CP-1 | Operating cash flow (22,119) thousand FY2025 and (2,975) thousand six months 2026 | Contract assets absorb cash as revenue grows | Debt service depends on borrowing or earnings growth | S1 page:114; S4 pages 4, 38 | Cumulative statements only |
| 3 | Three largest customers about 51.5% of FY2025 revenue | CP-1A | Quote on S1 page:25 | One prime's decision moves revenue and receivables | Revenue durability | S1 page:25 | Customers not named |
| 4 | Liquidity and maturity profile | CP-1 | Cash 51.741 US$m plus revolver 150.0 US$m; term loan due April 1, 2032 | Limits near-term refinancing pressure; Walker is the main call | Liquidity and refinancing | S4 pages 2, 18; S1 pages 140, 141 | Maturity table pre-dates the amendments |
| 5 | Lender protection and ownership unknown | CP-1A | Springing 6.50x covenant; guarantors and owners not stated | Structure and control cannot be assessed | Recovery mechanics and monitoring | S4 page:19; S1 pages 140, 156 | Credit agreement and proxy not supplied |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage ratios 3.25x, 4.00x, 4.29x, 4.57x | CP-1 | Inputs on S4 pages 2, 18, 35 and S1 pages 101, 113, 139; recomputed | Yes | High | Calculated | Verified | High | Committee-Ready |
| Interest cover 3.37x, 2.97x, 2.74x | CP-1 | Cash interest S4 page:4 and S1 page:115; recomputed | Yes | High | Calculated | Verified; cash interest may include lease interest | High | Committee-Ready |
| Liquidity 201.741 US$m | CP-1 | S4 pages 2 and 18 | Yes | High | Calculated | Verified; letters of credit not disclosed | High | Committee-Ready |
| Debt maturities | CP-1 | S1 page:141 schedule; S4 page:2 current portion | Yes | High | Directly Sourced | Verified; pre-amendment | Medium | Remediation Needed |
| Negative free cash flow | CP-1 | S1 pages 114, 115; S4 page:4 | Yes | High | Calculated | Verified | High | Committee-Ready |
| Customer concentration 51.5% | CP-1A, CP-2 | S1 page:25 | Yes | High | Directly Sourced | Verified | High | Committee-Ready |
| Acquisition timeline and amendments | CP-1A | S1 pages 94, 140; S4 pages 15, 18, 19, 29 | Yes | High | Directly Sourced | Verified | High | Committee-Ready |
| Backlog definition widened in 2026 | CP-1A, CP-2 | S1 page:99 and page:35; S4 page:33 | Yes | High | Conflicting | Not supported as stated | Low | Remediation Needed |
| Seemann consideration | CP-1A | S1 page:152 against S4 page:15 | Yes | High | Conflicting | Logged, not reconciled | Medium | Remediation Needed |
| Term loan size | CP-1, CP-1A | S1 page:152 against S3 and S4 page:18 | Yes | High | Conflicting | Logged, not reconciled | Medium | Remediation Needed |
| Sole or single source positions | CP-1A, CP-2 | S1 pages 12 and 17 | Yes | Medium: management | Directly Sourced as management's statement | Tagged Management Language upstream | Medium | Committee-Ready |
| No debt-funded distribution found | CP-1A | S1 page:114 equity statement; S1 page:87 | Partial | Medium | Analyst Inference | Absence claim; funding source of FY2023 and FY2024 distributions not traced | Low | Remediation Needed |
| Ownership, covenant headroom, guarantors | CP-1A, CP-2 | S1 page:156; S4 page:19 | Partial | Not available | Insufficient Information | Correctly marked upstream | Low | Not Traceable |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Term note principal 763,962 thousand at June 30, 2026 | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:18 Note 7 | CP-1 debt table | Sourced | High | Matches |
| Revolver commitments 150.0 million, no balance | pack/10-Q_2026-06-30 | as above | S4 | page:18 | CP-1 liquidity | Sourced | High | Matches |
| Springing covenant 6.50x first lien net leverage | pack/10-Q_2026-06-30 | as above | S4 | page:19 | CP-1 covenant | Sourced | High | Matches; threshold not stated |
| Total notes payable 506,767 thousand at December 31, 2025 | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | page:139 Note 6 | CP-1 | Sourced | High | Matches |
| Principal repayment 5,050 thousand a year, thereafter 481,517 thousand | pack/10-K | as above | S1 | page:141 | CP-1 maturities | Sourced | High | Sum equals 506,767 |
| Citibank agreement April 1, 2025, term loan maturing April 1, 2032, revolver April 1, 2030 | pack/10-K | as above | S1 | page:140 | CP-1, CP-1A | Sourced | High | Matches |
| Third Amendment February 2, 2026, 265.0 million increase | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:18 | CP-1, CP-1A | Sourced | High | Matches |
| Fifth Amendment August 3, 2026 to SOFR plus 2.25% | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:19 | CP-1, CP-1A | Sourced | High | Matches |
| Walker, about 94.0 million, signed July 20, 2026, expected third quarter 2026 | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:29 | CP-1, CP-1A | Sourced | High | Funding not stated; matches |
| Seemann total consideration 232.9 million | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:15 | CP-1A | Sourced | High | Conflicts with S1 page:152 |
| Seemann revenue 37.8 million and 63.0 million | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:16 | CP-1A | Sourced | High | Matches |
| Revenue, gross profit, net income, Q2 and six months | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | pages 2-3 | CP-1 | Sourced | High | Matches |
| EBITDA and Adjusted EBITDA reconciliation, Q2 and six months | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:35 | CP-1 | Sourced | High | Components sum to totals |
| FY2025 EBITDA 119,826 thousand and Adjusted EBITDA 145,302 thousand | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | page:101 | CP-1 | Sourced | High | Components sum to totals |
| Cash paid for interest 44,823 thousand FY2025 | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | page:115 | CP-1 | Sourced | High | Matches |
| Operating cash flow (22,119) thousand FY2025 | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | page:114 | CP-1 | Sourced | High | Matches |
| Cash flow six months 2026 and 2025 | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:4 | CP-1 | Sourced | High | Matches |
| Q1 2026 term note 765,881 and total notes 769,848 thousand | pack/10-Q_2026-03-31 | 10-Q_2026-03-31_krmn-20260331.htm.jsonl | S3 | page:17 | CP-1 | Sourced | High | Matches |
| Q1 2026 Adjusted EBITDA 44,786 and Q1 2025 30,319 thousand | pack/10-Q_2026-03-31 | 10-Q_2026-03-31_krmn-20260331.htm.jsonl | S3 | page:30 | CP-1 | Sourced | High | Matches; sum with Q2 equals six months |
| Three largest customers 51.5% | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | page:25 | CP-1A | Sourced | High | Matches |
| No single program above 12% | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | page:10 | CP-1A | Sourced | High | On average |
| Secondary offering July 23, 2025, no company proceeds | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | page:107 | CP-1A | Sourced | High | Matches |
| Material weaknesses, controls not effective | pack/10-K and 10-Q | 10-K and 10-Q Q2 2026 files | S1, S4 | page:153; page:41 | CP-1, CP-1A, CP-2 | Sourced | High | Remediation progress omitted upstream |
| Remaining performance obligations 703.9 million | pack/10-Q_2026-06-30 | 10-Q_2026-06-30_krmn-20260630.htm.jsonl | S4 | page:7 | CP-1A | Sourced | High | Matches |
| Backlog 1.3 billion | pack/EX-99.1 Aug | EX-99.1_2026-08-06_krmn-ex99_1.htm.jsonl | S7 | page:1 | CP-1A | Sourced | Medium | Management; 1,322,124 thousand on S4 page:33 |
| End-market amounts FY2025 and shares | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | page:96; page:14 | CP-1A | Sourced | High | Item 1 percentages conflict with the table |
| Gross margin and add-back percentages | derived | derived | S1, S4 | pages 101, 113, 35 | CP-1, CP-2 | Calculated | High | Recomputed |
| Sole or single source positions | pack/10-K | 10-K_2025-12-31_krmn-20251231.htm.jsonl | S1 | pages 12 and 17 | CP-1A | Management Language | Medium | Tagged upstream |
| Backlog definition widened | pack/10-K and 10-Q | 10-K and 10-Q Q2 2026 files | S1, S4 | page:99, page:35, page:33 | CP-1A, CP-2 | Conflicting | High | Not supported; see issue log |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA 179,068 | CP-1 table; CP-2 | 145,302; 99,366; 65,600 | FY2025 + 6M 2026 - 6M 2025 | Calculated | Verified | High | Leverage, cover | S1 page:101; S4 page:35 |
| Total debt 768,478 | CP-1 | 763,962; 4,516; revolver nil | Sum of notes principal | Calculated | Verified | High | Leverage | S4 page:18 |
| Net debt / Adjusted EBITDA 4.00x | CP-1; CP-2 | 768,478; 51,741; 179,068 | (Debt - cash) / LTM Adjusted EBITDA | Calculated | Verified | High | Leverage | S4 pages 2, 18, 35 |
| Lease-inclusive net 4.57x | CP-1; CP-2 | Finance leases 102,139 | (Debt + finance leases - cash) / LTM Adjusted EBITDA | Calculated | Verified | High | Leverage | S4 page:2 |
| Interest cover 3.37x | CP-1; CP-2 | 179,068; 53,144 | LTM Adjusted EBITDA / LTM cash interest | Calculated | Verified | Medium | Debt service | S4 page:4; S1 page:115 |
| Cover after capex 2.74x | CP-1; CP-2 | 179,068; 33,532; 53,144 | (EBITDA - capex) / cash interest | Calculated | Verified | Medium | Debt service | S4 page:4 |
| LTM free cash flow (27,671) | CP-1; CP-2 | 5,861; 33,532 | Operating cash flow - capex | Calculated | Verified | High | Cash conversion | S1, S4 |
| Liquidity 201.741 US$m | CP-1; CP-2 | 51.741; 150.0 | Cash + undrawn revolver | Calculated | Verified | High | Liquidity | S4 pages 2, 18 |
| Walker share of liquidity 46.6% | CP-1; CP-2 | 94.0; 201.741 | 94.0 / 201.741 | Assumption-Based | Illustrative; funding unknown | Low | Liquidity | S4 page:29 |
| Debt growth 51.6% against LTM earnings growth 23.2% | CP-2 | 261,711; 506,767; 179,068; 145,302 | Percentage changes | Calculated | Verified | High | Leverage | S1, S4 |
| Rate sensitivity 7,640 thousand | CP-2 | 763,962 | 1% x principal | Assumption-Based | Analyst calculation, labelled | Medium | Debt service | S4 page:18 |
| End-market shares | CP-1A | 149,987; 149,825; 171,688; 471,500 | Amount / total | Calculated | Verified | High | Concentration | S1 page:96 |
| Backlog against remaining performance obligations (new in this review) | This review | Backlog 801,056 and 1,322,124 thousand; obligations 550.6 and 703.9 million | Differences and growth | Calculated | See Calculations | High | Revenue visibility | S1 pages 99, 120; S4 pages 7, 33 |

### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Backlog definition widened in 2026 | The annual report's key-measure note already uses the broader wording and says historical amounts did not change; only a risk-factor paragraph keeps the narrower wording. The claim is presented as a Documentary Fact or conflict, and is Analyst Inference at best | Conflicting | A false change in definition inflates the apparent revenue visibility concern and misdirects monitoring; the true concern is the size of backlog against remaining performance obligations | Replace with the corrected statement in the Calculations section | Business handoff: operating model table backlog row, fact register, conflict 5, credit translation 3, reader summary finding 3; credit handoff: backlog risk row |
| Minor | IPO net proceeds conflict | The text net proceeds of 147.3 million are stated after payments to Phantom Unit holders, which is a plausible disclosed cause for the difference from the 154,836 thousand cash flow line | Conflicting | Not a clean conflict; use of proceeds is stated on a stated basis | Cite both with the stated cause; do not treat as an unexplained conflict | Business handoff conflict 4 |
| Minor | No debt-funded distribution found | An absence claim; FY2023 and FY2024 distributions were small (788 and 156 thousand) and their funding was not traced | Analyst Inference | Governance reading depends on it | Label as not found in the sources read | Business handoff governance table |
| Minor | Material weaknesses described as not remediated | Correct, but the quarterly report also states that design and implementation of information technology general controls were completed and that adjustments were immaterial | Directly Sourced | Overstates unremediated scope slightly | Add remediation progress when carrying the finding | All handoffs |
| Minor | Term amortization of about 5.050 US$m a year | Taken from the December 31, 2025 schedule; the current portion at June 30, 2026 is 5.610 US$m | Directly Sourced | Stale after the term loan increase | Label as pre-amendment (already labelled in the financials handoff; the credit handoff states it as current) | Credit handoff key findings |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings cover the annual report, three quarters and three releases; no credit agreement, proxy or filing after August 6, 2026 | Debt terms and ownership rest on notes and are partial | Legal and structural conclusions unsupported | Obtain exhibits and proxy |
| Citation completeness | Ready with Remediation | All sampled figures carry a page locator and matched; one directional claim failed | A false directional claim can steer monitoring | Backlog view needs correction | Apply the correction |
| Calculation traceability | Committee-Ready | Every derived figure shows inputs and reproduced | No hand-derived value without inputs | Ratios reliable as calculations | None |
| Assumption transparency | Committee-Ready | Pro forma, Walker and rate sensitivity are labelled as illustrative or analyst calculations | Illustrations could be misread as forecasts | Low | None |
| Markdown and export artifact integrity | Committee-Ready | Headings, handoff names and hashes match across the four handoffs | None identified | None | None |

Overall auditability: Ready with Remediation (lowest of the five dimensions).

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed credit agreement and amendments | Covenant threshold and definition, guarantors, security, post-amendment amortization | Lender protection, structural position and covenant headroom cannot be traced | Covenant and structure rows | High impact | Exhibits to the filer's reports |
| CP-5-GAP-002 | Ownership and control | Proxy statement incorporated by reference | Control drives leverage tolerance and distribution risk | Governance rows | Medium impact | 2026 proxy statement |
| CP-5-GAP-003 | No evidence after 2026-08-06 | Walker closing and funding, third quarter results | Pro forma leverage and liquidity | Leverage and liquidity conclusions | Medium impact | Later filings |
| CP-5-GAP-004 | LTM earnings not pro forma | Acquired-business earnings before closing | Leverage probably overstated by an unknown amount | Leverage conclusions | Medium impact | Management pro forma, labelled |
| CP-5-GAP-005 | Conflicts open | Seemann consideration, term loan size, end-market shares | Transaction facts depend on basis | Business and credit text | Medium impact | Amendment and purchase agreements |
| CP-5-GAP-006 | Backlog correction | Corrected statement not yet in the upstream handoffs | Backlog statements in two handoffs are wrong | Business and credit text | Medium impact | This review |

### Consolidated issue log and clearance

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP-5-ISS-001 | Material | CP-1A and CP-2 | Unsupported directional claim | Backlog definition said to have widened in 2026 | Use the corrected statement | Restricts backlog statements | Open: correction stated here |
| CP-5-ISS-002 | Minor | CP-1A | Mislabelled conflict | IPO proceeds difference has a disclosed cause | Cite with the cause | None | Open |
| CP-5-ISS-003 | Minor | CP-1A | Absence claim | No debt-funded distribution found | Label as not found | None | Open |
| CP-5-ISS-004 | Minor | CP-0, CP-1, CP-2 | Omitted nuance | Remediation progress on controls not carried | Add when quoting | None | Open |
| CP-5-ISS-005 | Minor | CP-2 | Stale figure | Amortization stated as current | Label pre-amendment | None | Open |
| CP-5-ISS-006 | Material | All | Source gap | Credit agreement and ownership absent | Obtain sources | Restricts legal, covenant and recovery conclusions | Open |

Clearance decision: committee_status Restricted. Financial figures and ratios are cleared for use as calculations. Business and credit conclusions are cleared with the corrections in this log. Legal, covenant, guarantor, security and recovery conclusions are not cleared. No confidence score is stated because the scoring script is not run in host mode, and no new analytical conclusion is added by this review.

## Calculations

Independent recomputation, from the cited inputs and not from the handoffs' own outputs, with the result of each check:

1. The financials table was recomputed by script from its own printed inputs. LTM cells (FY2025 + six months 2026 - six months 2025) for revenue, gross profit, net operating income, net interest, net income, EBITDA, Adjusted EBITDA, cash interest, cash taxes, operating cash flow, capex and acquisitions: no mismatch. Gross margin and Adjusted EBITDA margin for all seven columns, add-backs, and free cash flow for all five columns: no mismatch within rounding. Total debt, net debt and all nine ratio rows for FY2024, FY2025 and LTM June 2026: no mismatch.
2. Chart values: Q1 2026 LTM Adjusted EBITDA 145,302 + 44,786 - 30,319 = 159,769; total debt 769,848 / 159,769 = 4.82x; net (769,848 - 73,798) / 159,769 = 4.36x; cash interest 44,823 + 12,906 - 11,038 = 46,691; cover 159,769 / 46,691 = 3.42x. Matches.
3. Statement ties: FY2025 gross profit 190,026 - G&A 85,656 - D&A 31,428 = 72,942; Q2 2026 78,234 - 31,339 - 12,066 = 34,829; six months 2026 142,099 - 59,976 - 25,842 = 56,281. EBITDA 14,032 + 5,233 + 15,176 + 15,284 = 49,725; Adjusted 49,725 + 1,392 + 1,940 + 45 + 1,444 + 34 = 54,580. Matches.
4. Debt schedule: 5,050 x 5 + 481,517 = 506,767, equal to the printed total.
5. Business handoff: end-market amounts 149,987 + 149,825 + 171,688 = 471,500; Q2 2026 amounts 43,417 + 42,072 + 63,012 + 33,562 = 182,063; ex-Seemann growth (182,063 - 37,800) / 115,097 - 1 = 25.3%. Matches.
6. Credit handoff: debt growth 261,711 / 506,767 = 51.6%; LTM earnings growth (179,068 - 145,302) / 145,302 = 23.2%; rate sensitivity 763,962 x 1% = 7,640; 7,640 / 53,144 = 14.4%. Matches.
7. New for the backlog review. Backlog per the annual report key-measure table 801,056 thousand at December 31, 2025 (10-K FY2025 page:99) and 1,322,124 thousand at June 30, 2026 (10-Q Q2 2026 page:33): growth 1,322,124 / 801,056 - 1 = 65.0%, equal to the company's 65%. Remaining performance obligations 550.6 million at December 31, 2025 (10-K FY2025 page:120) and 703.9 million at June 30, 2026 (10-Q Q2 2026 page:7): growth 703.9 / 550.6 - 1 = 27.8%. Backlog exceeds remaining performance obligations by 801.056 - 550.6 = 250.456 million at December 31, 2025 and by 1,322.124 - 703.9 = 618.224 million at June 30, 2026. Remaining performance obligations were 723.3 million at March 31, 2026 (10-Q Q1 2026 page:7), so they fell by 723.3 - 703.9 = 19.4 million in the second quarter while quarterly bookings were reported as nearly 500 million (EX-99.1 Aug 2026 page:1). The sources do not explain the divergence; it may reflect contract types in backlog that are not remaining performance obligations, which is an interpretation and not a finding.

Corrected backlog statement for downstream use: the annual report carries two descriptions of backlog. The risk-factor paragraph says "contracts for which funding is appropriated or otherwise authorized" (10-K FY2025 page:35). The key-measure note says contract types "include but are not limited to purchase orders, long term agreements and contractual authorization to proceed" and "Backlog was previously referred to as funded backlog. No change to the historical dollar amount presented to the table above." (10-K FY2025 page:99). The 2026 quarterly report repeats the key-measure wording (10-Q Q2 2026 page:33). Whether the measure itself changed is therefore not established, and the handoffs' statement that the definition widened between the annual report and 2026 is withdrawn.

## Gaps

| Gap | Severity | Consumers | Action |
| --- | --- | --- | --- |
| Executed credit agreement and amendments not supplied | Material | Committee, recovery and covenant users | Obtain exhibits before any legal or recovery conclusion |
| Ownership, sponsor and control rights not supplied | Medium | Governance users | Obtain the proxy statement |
| No evidence after 2026-08-06; Walker closing and funding unknown | Medium | Leverage and liquidity users | Obtain later filings |
| Earnings not pro forma for acquisitions | Medium | Leverage users | Obtain labelled management pro forma figures |
| Open conflicts: Seemann consideration, term loan size, end-market shares | Medium | All | Cite basis; resolve against the amendment and purchase agreements |
| Backlog statement corrected here but the accepted upstream answers cannot be edited | Medium | Anyone reading the earlier handoffs | Read the corrected statement in this review |
| Extraction fidelity of text files not reviewed against the original HTML; images and charts not inspected | Low | All | Spot-check key tables against the HTML filings |

## Next module

None remains in the selected set: this is the final module of the run. If the run is published, the report should carry the corrected backlog statement and the Restricted committee status from this review. Before any committee use of legal, covenant or recovery points, obtain the credit agreement with its amendments and the 2026 proxy statement, and re-run the affected modules.
