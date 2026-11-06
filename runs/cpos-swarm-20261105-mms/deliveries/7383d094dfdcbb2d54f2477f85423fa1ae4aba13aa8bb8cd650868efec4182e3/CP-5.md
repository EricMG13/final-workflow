# CP-5 — Evidence trace and research integrity: MAXIMUS, INC. (mms)

## Request

MAXIMUS, INC. (issuer id `mms`), as of 2026-11-05, pathway credit_snapshot, current period fiscal Q3 2026 (three months ended June 30, 2026) and prior period fiscal 2025 (year ended September 30, 2025), in USD. This module traces the claims of the accepted CP-0, CP-1, CP-1A and CP-2 handoffs to the seven pinned filings and releases and grades the result. It changes no credit conclusion and silently repairs no lineage.

## Sources

CP-5 re-opened the cited pages of the pinned sources; locators are `page:N` chunks of the `.jsonl` text, not printed page numbers.

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-09-30_mms-20250930.htm.jsonl | 962786100737da7c8a25bf2c0b0d8b7bba5fc8fe85f1a63dc4a22607d3101fd0 | Fiscal 2025 annual report (S1) |
| 10-Q_2025-12-31_mms-20251231.htm.jsonl | 1ece10b3b4a1f72edf52da31ebe99ab2543998f22e423edd0be2ded3496f545d | Fiscal Q1 2026 quarterly report (S2) |
| 10-Q_2026-03-31_mms-20260331.htm.jsonl | 72c28dae66fdf3271ecd55284a1e9ffd02e932cd689052dff69253e7614fe8a8 | Fiscal Q2 2026 quarterly report (S3) |
| 10-Q_2026-06-30_mms-20260630.htm.jsonl | e0ee49037a76362fa1359adeb6f1d6ec0af3bf048fce3d62f4b088d4d2e2d60b | Fiscal Q3 2026 quarterly report (S4) |
| EX-99.1_2026-02-05_mms-2025x12x31x8kxex991.htm.jsonl | ff62eabdd3d1037513edc754533c1c20140d9d029aa9713e0d89283ab79659d9 | Fiscal Q1 2026 earnings release (S5) |
| EX-99.1_2026-05-07_mms-2026x03x31x8kxex991.htm.jsonl | 3cc2b6ddbaacd127b88b399aaed54a4ba71be05c3b12c29939da2343ffcad4ec | Fiscal Q2 2026 earnings release (S6) |
| EX-99.1_2026-08-06_mms-2026x06x30x8kxex991.htm.jsonl | 78b1fb3302628c3c36cbd9a44260145bf92a755c30565ab852ed03fa9e5e9aa0 | Fiscal Q3 2026 earnings release (S7) |
| context | 427dc9f0877ed950bde305fcdd6af025bde473794c90eea607afca11f0c6cd79 | Run settings; not issuer evidence (S8) |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | b2c3bb0b1f4af634e0abd5fcab811ad35e641a5d0e7ca14dd9cdc832dae5d76e | Source readiness; run `mms-2026-11-05-credit_snapshot-host`; as of 2026-11-05 |
| CP-1 | 8829349e46633913828d697cb82b1a46f8bb93ac6c3f2be62bdafd8355e5278d | Financial base, debt, liquidity, covenants as reported, claims outside debt |
| CP-1A | d9cda7603175483bcf5968a1f0a8042b7f967e0d08b03518175f22bf3206e24e | Business model, ownership, capital allocation, conflicts |
| CP-2 | ca53c85f8fbba8848ff44426d7e27941f92725419e6f434b266ec059bd65753b | Credit synthesis |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream figures trace to the filings and recompute correctly. Five minor wording, locator and labelling issues remain; none changes a figure, so the analysis can go to committee with its stated limitations. | Medium | The Credit Agreement, guarantor detail and filings after August 6, 2026 are not supplied, so covenant, ranking and fiscal 2026 claims cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every printed figure checked against its cited page matched the filings, and every derived figure recomputed. | Leverage, liquidity, covenant and cash flow figures can be relied on as stated and labelled. | High |
| Covenant cushions of 50.0% and 65.6% are arithmetic on issuer-reported components, not a verified capacity. | Quote the reported ratios 2.00 and 8.72; treat the cushions as illustrative until the Credit Agreement is supplied. | Medium |
| Concentration shares of about 60%, 55% and one-fifth are fiscal 2025 figures but appear in summaries without that period. | Read them as fiscal 2025; no June 30, 2026 equivalents are supplied. | Medium |
| Two source conflicts stay open: the fiscal 2025 buyback amount and the definition of the federal revenue share. | Capital returned and concentration must be quoted with their basis. | Medium |
| Revolver capacity is netted for letters of credit at September 30, 2025 only; later dates are as printed. | Liquidity of 786,953 thousand US dollars at June 30, 2026 may be overstated by unreported letters of credit. | Medium |

### Evidence trace view

The upstream analysis is traceable to the filings, with five minor defects and no material one. Of 20 material claims traced, 9 are directly sourced, 4 calculated, 1 assumption-based, 4 analyst inference and 2 conflicting. Every printed figure checked on its cited page matched, and every derived figure recomputed from its cited inputs. The weakest supported claim is the covenant cushion, which is arithmetic on the issuer's own reported ratio components while the Credit Agreement is not supplied. The two conflicting claims, the fiscal 2025 buyback amount and the federal revenue share definition, are preserved as logged. Committee status is Committee Ready, QA status Passed, with confidence 69 and band Medium. The most important remediation is supplying the Credit Agreement and its May 27, 2026 amendment, followed by the fiscal 2026 annual report.

### Traceability summary

| Measure | Result | Register |
| --- | --- | --- |
| Material claims traced | 20 | T5B.3 |
| Directly sourced or calculated | 13 | T5B.3 |
| Assumption-based or analyst inference | 5 | T5B.3 |
| Weak lineage or conflicting | 2 conflicting, 0 weak | T5B.3 |
| Findings open | 5 minor, plus 2 logged source conflicts | T5.9 |
| Committee status | Committee Ready | T5.9 |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

Module Status: Ready with Limitations (all seven pinned sources and four handoffs available; the Credit Agreement, ratings and the proxy statement are not supplied). Traceability Scope: Top 5 drivers plus the material claims in T5B.3. Entity key: issuer_id `mms`.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-09-30_mms-20250930.htm.jsonl | Primary, filed, audited | FY2025, FY2024, FY2023 (years ended September 30) | Maximus, Inc., consolidated | Statements, debt note, covenant tables, adjusted EBITDA, leases, receivable sales, litigation, business, risk factors | Text extraction; exhibits and proxy statement by reference only | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2025-12-31_mms-20251231.htm.jsonl | Primary, filed, unaudited | Q1 FY2026 (three months ended December 31, 2025) | Same consolidated perimeter | Statements, debt, covenant tables, adjusted EBITDA | Text extraction | CP-1, CP-1A |
| S3 | 10-Q_2026-03-31_mms-20260331.htm.jsonl | Primary, filed, unaudited | Q2 FY2026 and six months to March 31, 2026 | Same | Statements, debt, covenant tables, adjusted EBITDA | Text extraction | CP-1, CP-1A |
| S4 | 10-Q_2026-06-30_mms-20260630.htm.jsonl | Primary, filed, unaudited | Q3 FY2026 and nine months to June 30, 2026 | Same | Statements, debt, swaps, liquidity, covenants, segments, subsequent events | Text extraction; nine-month cash flow only | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-02-05_mms-2025x12x31x8kxex991.htm.jsonl | Issuer release, unaudited, management-prepared | Q1 FY2026 | Same, issuer presentation | Results, leverage statement, guidance | Management claims; the 10-Q controls | CP-1A |
| S6 | EX-99.1_2026-05-07_mms-2026x03x31x8kxex991.htm.jsonl | Issuer release, unaudited, management-prepared | Q2 FY2026 | Same | Results, prior guidance, repurchase program | Management claims | CP-1A, CP-2 |
| S7 | EX-99.1_2026-08-06_mms-2026x06x30x8kxex991.htm.jsonl | Issuer release, unaudited, management-prepared | Q3 FY2026 | Same | Results, discrete quarter cash flow, pipeline, leverage target, revised guidance | Management claims; non-GAAP measures | CP-1, CP-1A, CP-2 |
| S8 | context | Run settings, not issuer evidence | As of 2026-11-05 | Issuer identity and period labels | Identity, currency, periods | Ratings, quotes, deal terms, peers blank | All modules |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cash conversion and collection timing | CP-1, CP-2 | Nine-month operating cash flow of (179,863) thousand; days sales outstanding 98 against 62; 245 million US dollars collected after June 30, 2026; guidance of 425 million to 475 million US dollars of free cash flow | Fourth-quarter collections decide year-end liquidity and leverage | Near-term liquidity and leverage risk sits in one quarter | S4 page:6, page:31; S7 page:2, page:4 | Fiscal Q4 results are not supplied |
| 2 | Leverage trend | CP-1, CP-2 | Debt principal 1,653,548 thousand against 1,346,875 at September 30, 2025; unrestricted cash 56,953 against 222,351 | Net leverage rose from 1.60x to 2.25x in nine months | Direction of travel matters more than level | S4 page:5, page:15; S1 page:64, page:83 | Issuer-adjusted EBITDA is a non-GAAP measure |
| 3 | Covenant position | CP-1, CP-2 | Reported net total leverage 2.00 against 4.00 maximum; coverage 8.72 against 3.00 minimum | Only financial maintenance tests described | Headroom is wide as reported | S4 page:32, page:33 | Credit Agreement and EBITDA definition not supplied |
| 4 | Customer and contract concentration | CP-1A, CP-2 | About 60% of fiscal 2025 revenue from ten contracts; about one-fifth from one federal agency; modification effective July 1, 2026 through December 31, 2026 | One decision moves earnings and cash | Event-driven earnings volatility | S1 page:18, page:19; S4 page:27 | Contract-level detail not supplied |
| 5 | Debt-funded shareholder returns | CP-1A, CP-2 | Share purchases of 447,482 thousand in fiscal 2025 and 204,919 thousand in nine months 2026; dividend 0.30 to 0.33; leverage target 2x to 3x | Discretionary use of cash drives leverage drift | Policy risk without a sponsor commitment | S1 page:66, page:42; S4 page:6, page:31; S7 page:4 | Distribution restrictions in the Credit Agreement not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1 Debt principal 1,653,548 thousand, instrument balances and maturity table | CP-1, CP-2 | "Total debt principal 1,653,548 1,346,875" | Yes | Primary, filed | Directly Sourced | Supported | High | Committee-Ready |
| M2 Liquidity 786,953 thousand US dollars | CP-1, CP-2 | "Cash and cash equivalents $ 56,953" and "access to approximately $730.0 million" | Yes | Primary inputs | Calculated | Recomputed; letters of credit not stated | Medium | Committee-Ready |
| M3 LTM issuer-adjusted EBITDA 711,009 thousand and ratios 2.33x, 2.25x and 8.24x | CP-1, CP-2 | "Adjusted EBITDA (Non-GAAP) $ 701,554" and nine-month columns | Yes | Derived from primary inputs | Calculated | Recomputed | High | Committee-Ready |
| M4 Reported covenant ratios 2.00 and 8.72 against 4.00 maximum and 3.00 minimum | CP-1, CP-2 | "Consolidated Net Total Leverage Ratio (as defined by our Credit Agreement) 2.00" | Yes | Primary, filed | Directly Sourced | Supported; definition not supplied | Medium | Committee-Ready |
| M5 Covenant cushions 50.0% and 65.6% | CP-1, CP-2 | Arithmetic on reported components 1,596,595 and 798,419 | Yes | Derived from issuer-reported inputs | Assumption-Based | Recomputed; capacity is not verified without the Credit Agreement | Medium | Remediation Needed |
| M6 Nine-month operating cash outflow and free cash flow outflow; days sales outstanding 98 | CP-1, CP-2 | "Net cash used in operating activities (179,863) (220,000)" and "which were 98 days" | Yes | Primary, filed | Directly Sourced | Supported | High | Committee-Ready |
| M7 Fourth-quarter free cash flow implied by guidance 633,615 to 683,615 thousand | CP-1, CP-2 | Guidance "Free cash flow $ 425 $ 475" less nine-month outflow | Yes | Issuer guidance and filed actuals | Calculated | Recomputed; guidance is Management Language | Medium | Committee-Ready |
| M8 Share purchases 447,482 and 204,919 thousand; dividends 68,710 and 51,437 thousand | CP-1, CP-1A, CP-2 | "Purchases of Maximus common stock (204,919)" | Yes | Primary, filed | Directly Sourced | Supported | High | Committee-Ready |
| M9 Shareholder returns partly debt-funded | CP-1A, CP-2 | "we expanded our term loans to provide additional capital for our operations, as well as funds to support share repurchases" | Yes | Management statement with filed flows | Analyst Inference | Labelled as interpretation | Medium | Committee-Ready |
| M10 About 60% of revenue from ten contracts, about 55% federal, one-fifth from one agency | CP-1A, CP-2 | "approximately 60% of our revenue came from our ten largest contracts" | Yes | Primary, filed | Directly Sourced | Supported; fiscal 2025 period | Medium | Remediation Needed |
| M11 Backlog 15,327 million US dollars, 2.82 times fiscal 2025 revenue, down 5.2% | CP-1A, CP-2 | "Backlog $ 15,327 $ 16,167" | Yes | Primary, filed | Directly Sourced | Supported; the ratio and change are arithmetic | High | Committee-Ready |
| M12 Customer modification July 1 to December 31, 2026 and lowered guidance | CP-1, CP-1A, CP-2 | "reduce our diluted earnings per share by approximately $0.35 per quarter" | Yes | Primary, filed, and issuer release | Directly Sourced | Supported; effect on full-year earnings not bridged | Medium | Committee-Ready |
| M13 May 27, 2026 amendment and Term Loan B increase of 325 million US dollars | CP-1, CP-1A, CP-2 | "The Amendment increased our TLB by $325 million" | Yes | Primary, filed | Directly Sourced | Supported; terms not supplied | High | Committee-Ready |
| M14 Interest sensitivity of 9.8 million US dollars per 100 basis points | CP-2 | Unhedged principal 978,548 thousand | Yes | Derived from primary inputs | Analyst Inference | Labelled inference; assumes a full year at June 30, 2026 balances | Medium | Committee-Ready |
| M15 Claims outside debt: operating leases 94,883 thousand, receivable sales, performance bonds 33.2 million US dollars | CP-1, CP-2 | "Operating lease liabilities, current portion 38,280" and "performance bond commitments totaling $33.2 million" | Yes | Primary, filed | Directly Sourced | Supported; bonds dated September 30, 2025 | High | Committee-Ready |
| M16 Fundamental credit view and thesis | CP-2 | Synthesis of M1 to M15 | Yes | Analyst synthesis | Analyst Inference | Labelled as interpretation | Medium | Committee-Ready |
| M17 No sponsor, dispersed ownership, no documented creditor-adverse action | CP-1A, CP-2 | "there were 30 holders of record of our outstanding common stock" | Yes | Primary, filed, with absence of disclosure | Analyst Inference | Labelled; control rights and legal capacity not supplied | Medium | Committee-Ready |
| M18 Fiscal 2025 share purchases: 447.5 million against 456.6 million US dollars | CP-1A | "$447.5 million in fiscal year 2025" against "a cost of $456.6 million" | Yes | Primary, filed | Conflicting | Preserved as logged | Low | Remediation Needed |
| M19 Federal share of revenue: 56% against about 55% against 55.2% | CP-1A | "generated 56% of our total revenue" against "approximately 55% of our total revenue" | Yes | Primary, filed | Conflicting | Preserved as logged; definitions differ | Low | Remediation Needed |
| M20 Hedge coverage 675,000 thousand, 40.8% of principal | CP-1, CP-2 | Swap table of seven rows | Yes | Primary, filed | Calculated | Recomputed | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt principal 1,653,548; Term Loan A 819,375; Term Loan B 814,173; revolver 20,000 thousand at June 30, 2026 | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:15 | CP-1 debt register | Sourced | Primary, filed | Table 7.1; unamortized costs 16,613 |
| Future minimum principal payments 18,952; 75,809; 81,434; 690,184; 8,309; 778,860 thousand | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:15 | CP-1 maturities chart | Sourced | Primary, filed | Foots to 1,653,548 |
| Amendment of May 27, 2026 increased Term Loan B by 325 million US dollars | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:15 | CP-1 latest quarter; CP-1A transaction summary | Sourced | Primary, filed | Terms not stated |
| Seven swaps, notional 675,000 thousand | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:16 | CP-1 debt register | Sourced | Primary, filed | Effective rate 5.6% at page:17 |
| Revolver access of approximately 730.0 million US dollars | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:32 | CP-1 liquidity table | Sourced | Primary, filed | Equals 750.0 less 20.0 drawn |
| Covenant maximum 4.00 with step-up to 4.50 and minimum coverage 3.00 | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:32 | CP-1 liquidity and covenant | Sourced | Primary, filed | Step-up circumstances not defined |
| Covenant ratios 2.00 and 8.72; Consolidated EBITDA 798,419 thousand | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:33 | CP-1 liquidity and covenant | Sourced | Primary, filed | Credit Agreement definition |
| Unrestricted cash 56,953 and restricted cash 96,296 thousand | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:19 | CP-1 financials table | Sourced | Primary, filed | Table 10.1 |
| Nine-month operating cash flow (179,863), capital expenditure 28,752, dividends 51,437, share purchases 204,919 thousand | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:6 | CP-1 financials table | Sourced | Primary, filed | Cash flow statement |
| Discrete Q3 operating cash flow (124,987), capital expenditure 11,980, free cash flow (136,967) thousand | source-text | EX-99.1_2026-08-06_mms-2026x06x30x8kxex991.htm.jsonl | S7 | page:7, page:9 | CP-1 financials table | Sourced | Issuer release | Three-month columns |
| Adjusted EBITDA 192,327 for Q3 and 550,768 for nine months | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:36 | CP-1 financials table | Sourced | Primary, filed | Also S7 page:9 |
| Fiscal 2025 adjusted EBITDA 701,554 and fiscal 2024 615,044 thousand | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:59 | CP-1 financials table | Sourced | Primary, audited | Non-GAAP reconciliation |
| Fiscal 2025 operating cash flow 429,372, capital expenditure 63,213, dividends 68,710 thousand | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:65 | CP-1 financials table | Sourced | Primary, audited | Share purchases 447,482 at page:66 |
| Fiscal 2025 covenant ratios 1.51 and 9.25; Consolidated EBITDA 793,995 thousand | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:54 | CP-1 financials table | Sourced | Primary, audited | Cash offset capped at 150,000 |
| Interest payments 82,562 thousand for fiscal 2025 and 64,526 for nine months 2026 | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:93 | CP-1 interest cover | Sourced | Primary, audited | Nine months at S4 page:19 |
| Accounts receivable, net 1,382,014 against 898,095 thousand | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:5 | CP-1 latest quarter | Sourced | Primary, filed | Balance sheet |
| Days sales outstanding 98 against 62; 245 million US dollars collected after June 30, 2026 | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:31 | CP-1 latest quarter; CP-2 | Sourced | Primary, filed | Subsequent event |
| Receivable sales: 350.0 million US dollar limit; 1.28 billion transferred in nine months | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:20 | CP-1 claims table | Sourced | Primary, filed | Limit 250.0 million at S1 page:94 and S2 page:17 |
| Customer modification effective July 1, 2026 through December 31, 2026; about 0.35 per quarter | source-text | 10-Q_2026-06-30_mms-20260630.htm.jsonl | S4 | page:27 | CP-1A operating model | Sourced | Primary, filed | Customer not named |
| Guidance: adjusted EPS 7.90 to 8.20; free cash flow 425 to 475 million US dollars | source-text | EX-99.1_2026-08-06_mms-2026x06x30x8kxex991.htm.jsonl | S7 | page:2, page:6 | CP-1 latest quarter; CP-2 | Sourced | Issuer release | Prior range at S6 page:4 |
| Leverage target of 2x to 3x | source-text | EX-99.1_2026-08-06_mms-2026x06x30x8kxex991.htm.jsonl | S7 | page:4 | CP-1A governance; CP-2 | Sourced | Issuer release | Management Language |
| Ten largest contracts about 60%; one-fifth from one federal agency | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:19 | CP-1A operating model | Sourced | Primary, audited | Fiscal 2025 |
| Federal about 55% of revenue; segment 56%; customer table 55.2% | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:18, page:7, page:80 | CP-1A conflict 2 | Conflicting | Primary, audited | Different definitions |
| Backlog 15,327 against 16,167 million US dollars | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:49 | CP-1A operating model | Sourced | Primary, audited | At September 30, 2025 |
| Fiscal 2025 share purchases 447.5 million against 456.6 million US dollars | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:51, page:93 | CP-1A conflict 1 | Conflicting | Primary, audited | Basis of 456.6 not stated |
| Performance bonds 33.2 million US dollars at September 30, 2025 | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:98 | CP-1 claims table | Sourced | Primary, audited | Not updated in the 10-Qs |
| 30 holders of record and about 151,000 beneficial owners | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:42 | CP-1A governance | Sourced | Primary, audited | At October 20, 2025 |
| Credit Agreement secured by substantially all assets and guaranteed by wholly owned material domestic subsidiaries | source-text | 10-K_2025-09-30_mms-20250930.htm.jsonl | S1 | page:84 | CP-0 perimeter; CP-1 debt register | Sourced | Primary, audited | Not repeated in the 10-Qs |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM issuer-adjusted EBITDA 711,009 thousand | CP-1 C1; CP-2 | Fiscal 2025 701,554; nine months 550,768 and 541,313 | 701,554 + 550,768 − 541,313 | Recomputed, matches | Calculated | High | Basis for leverage and cover | S1 page:59; S4 page:36 |
| Gross and net leverage 2.33x and 2.25x | CP-1 C5; CP-2 | Principal 1,653,548; cash 56,953; EBITDA 711,009 | 1,653,548 / 711,009; 1,596,595 / 711,009 | Recomputed, matches | Calculated | High | Leverage level and trend | S4 page:5, page:15 |
| Cover 8.24x | CP-1 C6; CP-2 | LTM cash interest 86,279 | 711,009 / 86,279; 82,562 + 64,526 − 60,809 | Recomputed, matches | Calculated | High | Debt service capacity | S1 page:93; S4 page:19 |
| Liquidity 786,953 thousand | CP-1 C10; CP-2 | Cash 56,953; revolver access 730,000 | 56,953 + 730,000 | Recomputed, matches | Calculated | Medium | Near-term resilience; letters of credit not stated | S4 page:5, page:32 |
| Covenant cushions 50.0% and 65.6% | CP-1 C9; CP-2 | Net debt 1,596,595; EBITDA 798,419; interest 91,588 | 798,419 − 1,596,595/4.00; 798,419 − 3.00 × 91,588 | Recomputed, matches; assumes definitions as reported and debt unchanged | Assumption-Based | Medium | Illustrative only | S4 page:32, page:33 |
| Free cash flow LTM 433,230 thousand | CP-1 C3; CP-2 | Operating cash flow 469,509; capital expenditure 36,279 | 469,509 − 36,279 | Recomputed, matches | Calculated | High | Cash conversion | S1 page:65; S4 page:6 |
| Guidance-implied fourth-quarter free cash flow | CP-1 C13; CP-2 | Guidance 425,000 to 475,000; nine months (208,615) | 425,000 + 208,615; 475,000 + 208,615 | Recomputed, matches | Calculated | Medium | Liquidity sensitivity | S7 page:6; S4 page:34 |
| Prior-year fourth-quarter free cash flow 641,845 thousand | CP-1 C13 | Fiscal 2025 366,159; nine months (275,686) | 366,159 + 275,686 | Recomputed, matches | Calculated | High | Comparator for guidance | S1 page:51; S4 page:34 |
| Debt movement 306,673 and net debt movement 472,071 thousand | CP-1 C11; CP-2 | Principal 1,653,548 and 1,346,875; net 1,596,595 and 1,124,524 | Differences | Recomputed, matches | Calculated | High | Leverage drift | S4 page:15; S1 page:83 |
| Hedge coverage 40.8% | CP-1 C12; CP-2 | Notional 675,000; principal 1,653,548 | 675,000 / 1,653,548 | Recomputed, matches | Calculated | High | Rate exposure | S4 page:16 |
| Interest sensitivity 9,785 thousand per 100 basis points | CP-2 C1 | Unhedged 419,375 + 539,173 + 20,000 | 978,548 × 1% | Recomputed, matches; assumes a full year at June 30, 2026 balances | Analyst Inference | Medium | Interest cost sensitivity | S4 page:29 |
| Backlog ratios 2.82 and −5.2% | CP-1A C1, C2 | Backlog 15,327 and 16,167; revenue 5,431,276 thousand | 15,327 / 5,431.276; 15,327 / 16,167 − 1 | Recomputed, matches | Calculated | High | Revenue visibility | S1 page:49, page:64 |
| Share purchases to dividends 6.5 times | CP-1A C8; CP-2 | 447,482 and 68,710 thousand | 447,482 / 68,710 | Recomputed, matches | Calculated | High | Capital allocation | S1 page:65, page:66 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 credit view and reader summary: about 60% of revenue from ten contracts and about 55% federal | The shares are fiscal 2025 figures from the 10-K; the sentences carry no period label and no June 30, 2026 equivalent exists in the sources | Weak Lineage | A reader could take them as current | Read them as fiscal 2025 (S1 page:18, page:19) | CP-2 Credit view; CP-2 Reader summary |
| MINOR | CP-1 and CP-2: revolver capacity | CP-1 nets letters of credit of 3.0 million US dollars at September 30, 2025 (747.0) but prints later dates as reported without netting because letters of credit are not stated; the 10-K prints 750.0 | Weak Lineage | Capacity series mixes netted and gross dates | Read 747.0 as 750.0 less 3.0 and later dates as possibly overstated | CP-1 Chart data: liquidity; CP-2 Debt summary |
| MINOR | CP-1 and CP-2: covenant cushions of 50.0% and 65.6% | Arithmetic on issuer-reported ratio components with debt and definitions held fixed; the Credit Agreement is not supplied, so capacity is not verified | Assumption-Based | Presenting a cushion as capacity would infer covenant room | Label as illustrative; quote only the reported ratios | CP-1 C9; CP-2 Key findings |
| MINOR | CP-1 chart data: debt maturities | The displayed buckets 19.0, 75.8, 81.4, 690.2, 8.3 and 778.9 sum to 1,653.6 while the basis cell says the total is 1,653.5 | Calculated | Rounding difference of 0.1 million US dollars | Read from the thousand figures, which foot to 1,653,548 | CP-1 Chart data: debt maturities |
| MINOR | CP-1 latest quarter: AR and restricted cash movement | The restricted cash sentence cites Q3 10-Q page:32, which prints no amounts (38,108 and 96,296 sit at page:19), and the receivables sentence cites only calculation C14 (898,095 and 1,382,014 sit at page:5); the cash purchases of 204,919 in the capital returns bullet sit at page:6 | Weak Lineage | Locators do not carry the figures | Cite S4 page:5, page:6 and page:19 | CP-1 Latest quarter and after |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Citation coverage | Strong | Every figure in the registers carries a file and `page:N`; all printed figures in CP-0, CP-1 and CP-1A were found on the pinned sources, and the only figures not found in the text are calculations, sums or millions conversions | A missing locator blocks independent recomputation | Figures can be reproduced from the filings | Correct the locator in the fifth item of T5B.6 |
| Calculation reproducibility | Strong | All derived figures in CP-1, CP-1A and CP-2 recomputed and matched, including every LTM, ratio and guidance-implied figure | A wrong LTM would move every ratio | Leverage, cover and the fourth-quarter requirement are reliable as labelled | None for arithmetic |
| Definition control | Adequate | Issuer-adjusted EBITDA and Credit Agreement EBITDA are kept apart; the difference of 87,410 thousand ties to stock compensation 35,132 and pro forma adjustments 52,278 | Mixing the two would misstate leverage and headroom | Headroom must be quoted from the reported ratios only | Label the cushions illustrative |
| Conflict handling | Adequate | The buyback amount and the federal share definition are logged in CP-1A and carried to CP-2 without reconciliation | An unlogged conflict would be smoothed into one number | Capital returned and concentration carry a basis caveat | Quote each figure with its basis |
| Management language | Adequate | Pipeline, efficiency, leverage target and guidance claims are tagged Management Language | Promotional claims adopted as fact would inflate the view | The credit view does not depend on them | None |
| Period labelling | Adequate | Quarter, nine-month, LTM and fiscal year labels are used throughout; two concentration shares lack a period in the summaries | An unlabelled fiscal 2025 share can be read as current | Concentration evidence is a year older than the balance sheet | Add the period label downstream |
| Legal and structural lineage | Weak | The Credit Agreement, amendment, guarantors and receivable-sale agreement are not supplied; security and guarantee rest on one 10-K sentence | Ranking, covenant definitions and distribution limits cannot be traced | Legal conclusions must stay restricted | Supply executed documents |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Credit Agreement, May 27, 2026 amendment terms and Consolidated EBITDA definition | Executed agreement, amendment and compliance certificate | Headroom, baskets and distribution limits cannot be rebuilt | M4 and M5 rest on issuer statements | Caps lineage of M5 | Credit Agreement |
| G2 | Fiscal Q4 and fiscal 2026 results and events from August 7, 2026 to the cutoff | Fiscal 2026 10-K, any release or 8-K | Guidance depends on fourth-quarter collections | M7 cannot be tested against actuals | Date-bound view | EDGAR filings |
| G3 | Guarantor entities and collateral beyond one 10-K sentence | Guarantor schedule | Structural position of the bank debt | M1 ranking claims limited | Keeps legal lineage weak | Credit Agreement |
| G4 | Contract-level detail and the customer behind the modification | Contract and recompete schedules | Concentration cannot be sized | M10 and M12 are shares and effects only | Medium confidence on concentration | Issuer disclosure |
| G5 | Letters of credit, Canada and United Kingdom facilities, receivable-sale balance | Later liquidity disclosure | Liquidity may be overstated | M2 labelled with the limitation | Medium confidence on liquidity | Issuer filings |
| G6 | Ratings and market prices | Rating reports, quotes | No external opinion | CP-2 has no external anchor | Keeps the view at Medium | Rating agencies, dealer quotes |
| G7 | Proxy statement | 2026 proxy statement | Control rights and related parties untraced | M17 is an inference | Keeps governance at interpretation | Proxy statement |
| G8 | MOVEit accrual and insurance recovery | Later litigation disclosure | Contingent outflow unsized | M15 notes the omission | Minor | Issuer filings |

#### T5.1 Module and handoff register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | Accepted CP-0 handoff; run `mms-2026-11-05-credit_snapshot-host` | Source readiness for four consumers | Primary filings, text extraction | Six canonical H2 headings present; no YAML envelope in the Markdown transport | Accepted by CP-OS; no findings here | Its trailing twelve month gap is closed by CP-1 |
| CP-1 | Accepted CP-1 handoff; same run | Financial base and chart data | Primary filings | Six H2 headings, reader summary, view and chart selectors present | Accepted by CP-OS; four minor findings here | Issuer-adjusted EBITDA throughout, Credit Agreement measure shown apart |
| CP-1A | Accepted CP-1A handoff; same run | Business, ownership, behaviour, conflicts | Primary filings and releases | Six H2 headings and required selectors present | Accepted by CP-OS; two logged conflicts | Management Language tagged |
| CP-2 | Accepted CP-2 handoff; same run | Credit synthesis | Upstream handoffs | Six H2 headings and required selectors present | Accepted by CP-OS; three minor findings here | Reuses CP-1 and CP-1A figures |

#### T5.2 Citation and evidence support issues

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Credit view and reader summary: ten-contract and federal shares | Weak Lineage | Fiscal 2025 shares without a period label | Read as fiscal 2025 | Clear with note |
| MINOR | CP-1 | Latest quarter: receivables and restricted cash movement | Weak Lineage | Restricted cash cited to page:32, which has no amounts, and receivables cited to a calculation only; the figures are at page:19 and page:5 | Cite the balance sheet and cash note pages | Clear with note |
| MINOR | CP-1, CP-2 | Revolver capacity series | Weak Lineage | Netted at one date, gross at others | Read the series with its basis cells | Clear with note |

#### T5.3 Metric, logic and definition issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Covenant cushions 50.0% and 65.6% | Arithmetic on reported components, debt and definitions held fixed; capacity is not verified without the Credit Agreement | None; reported ratios 2.00 and 8.72 are consistent with the printed components | Label as illustrative; do not quote as capacity | Clear with note |
| MINOR | CP-1 | Debt maturities chart total | Rounded buckets sum to 1,653.6 against a stated 1,653.5 | None; thousand figures foot to 1,653,548 | Read from the thousand figures | Clear with note |
| MINOR | CP-1, CP-2 | Issuer-adjusted against Credit Agreement EBITDA | 711,009 thousand against 798,419 thousand differ by stock compensation and pro forma adjustments, as CP-1 shows | None | Keep both labelled | Clear with note |
| MINOR | CP-2 | Interest sensitivity of 9,785 thousand | Assumes a full year at June 30, 2026 balances and ignores the September 2026 swap expiry, as CP-2 states | None | Keep the label | Clear with note |

#### T5.4 Legal and structural claim issues

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-2 | Credit Agreement secured by substantially all assets and guaranteed by wholly owned material domestic subsidiaries | Executed Credit Agreement and security documents | Only one 10-K sentence; the 10-Qs do not repeat it; guarantors unnamed | Carry as stated in the 10-K only | Legal review of security and guarantees |
| MINOR | CP-1, CP-2 | Covenant levels 4.00, 4.50 step-up and 3.00 and the Consolidated EBITDA definition | Credit Agreement | Step-up circumstances and add-back limits not supplied | Quote as issuer description | Legal review of covenant definitions |
| MINOR | CP-1, CP-2 | Receivable sales are sales with no recourse and a limit of 350.0 million US dollars | Receivables Purchase Agreement | Agreement not supplied; balance outstanding not printed | Carry as issuer description | Legal review of the sale characterisation |
| MINOR | CP-1A, CP-2 | No creditor-adverse action documented | Credit Agreement and any amendments | Absence of disclosure is not evidence of absence | Keep as Insufficient Information on legal capacity | Legal review of permitted distributions |

#### T5.5 Market and relative-value claim issues

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A | Pipeline of 50.4 billion US dollars and contract awards of 1.25 billion | Conversion rates and win history | Management figures only | Keep the Management Language label | Context only; no instrument view |
| MINOR | CP-2 | No ratings, quotes or market-implied view | Rating reports, dealer quotes, spreads | Context fields blank | Keep as not supplied | Committee must source external ratings |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 | CP-0 listed trailing twelve month adjusted EBITDA as a gap; CP-1 derived it from printed quarterly and annual figures and said so | CP-0 is accepted and cannot be edited | Use CP-1; this handoff records the supersession | None on figures |
| MINOR | CP-1, CP-2 | Revolver capacity netted at September 30, 2025 in CP-1 and shown as printed at June 30, 2026 in both | None | Read each with its basis cell | None on figures |
| MINOR | CP-1A, CP-2 | Two source conflicts (buyback amount, federal share definition) logged in CP-1A and carried to CP-2 | None | Keep unreconciled | Caveat carried |

All carried figures agree across CP-1, CP-1A and CP-2: leverage 2.33x gross and 2.25x net, cover 8.24x, liquidity 786,953 thousand, guidance-implied fourth-quarter free cash flow of 633,615 to 683,615 thousand, share purchases 447,482 thousand against dividends 68,710 thousand, backlog 15,327 million US dollars. No version conflict exists: each module consumed the exact hash of its predecessors.

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Duplication | Debt, liquidity and leverage figures are repeated in CP-1 tables and CP-2 findings; they agree | None | None |
| MINOR | CP-2 | Materiality | Interest sensitivity and the covenant cushions rely on stated assumptions | Keep labelled | Low |
| MINOR | CP-2 | Committee readiness | Summaries carry fiscal 2025 shares without a period | Read the detailed sections | Low |

#### T5.8 Structured export and handoff defects

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | YAML envelope | The Markdown transport carries no YAML front matter, filename check or script-run validation block | Rely on CP-OS hashes and checks | None for this run |
| MINOR | CP-1 | Chart data selectors | Maturity chart periods are year buckets as of June 30, 2026 rather than a single reporting period | Keep the basis note | Report renders as printed |
| MINOR | CP-1A, CP-2 | Selector tables and prose sections | Required selectors are present once each | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISS-01 | MINOR | CP-2 | Weak lineage | Ten-contract and federal shares shown without the fiscal 2025 period | Read as fiscal 2025 | Clear with note | Open |
| ISS-02 | MINOR | CP-1, CP-2 | Weak lineage | Revolver capacity netted at September 30, 2025 only | Read with basis cells | Clear with note | Open |
| ISS-03 | MINOR | CP-1, CP-2 | Assumption labelled as headroom | Covenant cushions are illustrative arithmetic | Label as illustrative | Clear with note | Open |
| ISS-04 | MINOR | CP-1 | Rounding | Maturity chart buckets sum to 1,653.6 against 1,653.5 | Read from thousands | Clear with note | Open |
| ISS-05 | MINOR | CP-1 | Locator | Restricted cash cited to a page without amounts; receivables cited to a calculation only | Cite page:5, page:6 and page:19 | Clear with note | Open |
| ISS-06 | MINOR | CP-1A, CP-2 | Source conflict | Fiscal 2025 share purchases 447.5 against 456.6 million US dollars | Quote with basis | Clear with note | Open (logged conflict, no penalty) |
| ISS-07 | MINOR | CP-1A, CP-2 | Source conflict | Federal share 56% against about 55% against 55.2% | Quote with definition | Clear with note | Open (logged conflict, no penalty) |
| ISS-08 | MINOR | CP-0 | Version | Trailing twelve month adjusted EBITDA gap superseded by CP-1 | None | None | Closed |

Committee status: Committee Ready. QA status: Passed. Confidence score 69, band Medium.

## Calculations

- **Confidence score (script `confidence_score.py`).** Lineage of 20 material claims by strongest evidence: Directly Sourced 9, Calculated 4, Assumption-Based 1, Analyst Inference 4, Conflicting 2. Required fields present 17 of 17 (the 17 required registers). Source gate pass (all seven sources and four handoffs available). Findings: MATERIAL 0, MINOR 5 (ISS-01 to ISS-05). Script output: E = 73.5, C = 100.0, S = 1.0, P = 15, score = clamp((0.6 x 73.5 + 0.4 x 100) x 1.0 − 15) = 69.1, rounded 69, band Medium, qa_status Passed. ISS-06 and ISS-07 are logged source conflicts and ISS-08 is closed, so none carries a penalty.
- **Recomputation of upstream figures (each from the cited inputs, thousands of USD).** LTM adjusted EBITDA 701,554 + 550,768 − 541,313 = 711,009. Net debt 1,653,548 − 56,953 = 1,596,595; 1,653,548 / 711,009 = 2.33x; 1,596,595 / 711,009 = 2.25x. Cash interest LTM 82,562 + 64,526 − 60,809 = 86,279; cover 711,009 / 86,279 = 8.24x. Liquidity 56,953 + 730,000 = 786,953. LTM operating cash flow 429,372 + (−179,863) − (−220,000) = 469,509; capital expenditure 63,213 + 28,752 − 55,686 = 36,279; free cash flow 433,230. Guidance-implied fourth-quarter free cash flow 425,000 + 208,615 = 633,615 and 475,000 + 208,615 = 683,615. Prior fourth quarter 366,159 + 275,686 = 641,845. Covenant: 1,596,595 / 798,419 = 2.00; 798,419 / 91,588 = 8.72. Hedge 675,000 / 1,653,548 = 40.8%. Backlog 15,327 / 5,431.276 = 2.82; 15,327 / 16,167 − 1 = −5.2%. Share purchases 447,482 / 68,710 = 6.5. Maturity buckets foot: 18,952 + 75,809 + 81,434 + 690,184 + 8,309 + 778,860 = 1,653,548. All matched the upstream figures.
- **Rounding check.** The displayed maturity chart values 19.0 + 75.8 + 81.4 + 690.2 + 8.3 + 778.9 = 1,653.6 against 1,653.548 million, a difference of 0.1 from rounding (ISS-04).
- **Tie-out of the two EBITDA measures.** 798,419 − 711,009 = 87,410 = stock compensation 35,132 + pro forma and other adjustments 52,278 (S4 page:33).
- **Printed-figure check.** Every comma-formatted amount in the CP-0, CP-1 and CP-1A bodies was searched in the pinned source text; the amounts not found are the calculated results, sums and conversions listed in the calculation registers above.

## Gaps

Gaps G1 to G8 in the T5B.8 register above are the gaps of this handoff. The two that decide the reach of committee use are G1 (the Credit Agreement, amendment and EBITDA definition) and G2 (the fiscal fourth quarter and everything after August 6, 2026). Both sit in documents outside the supplied pack and nothing in this module can fill them; legal, covenant-capacity and fiscal 2026 conclusions therefore stay restricted even though the traced figures are sound.

## Next module

This is the last module in the minimum set. The report delivery should carry the Committee Ready status with the stated limits, use the detailed sections over the summary wording for concentration periods and revolver capacity, quote covenant results as reported ratios only, and treat the covenant cushions as illustrative until the Credit Agreement is supplied.
