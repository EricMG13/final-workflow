## Request

This is the evidence trace and research-integrity review of WHIRLPOOL CORP /DE/ (whr) as of 2026-11-05, in the credit snapshot pathway. It traces the financial base, business and transaction, and credit view handoffs to the pinned filings and releases, reopens their locators, recomputes their derived figures and grades whether the work is traceable enough for a committee. Scope is the Top 5 credit drivers plus every figure that supports them; currency is USD millions as the filings print them; no credit conclusion is changed and no lineage is silently repaired.

## Sources

Issuer sources opened and checked against the handoffs (pinned text conversions; sha256 of the pinned files):

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_whr-20251231.htm.jsonl | 27a098d2b931085348926af17c6e4538b36a73e089a481d6d925c0a5bd60adf0 |
| 10-Q_2026-03-31_whr-20260331.htm.jsonl | 5783ae95bc8319fbfb22c4f191362ef3346933b47250adc51350041a7d65eb25 |
| 10-Q_2026-06-30_whr-20260630.htm.jsonl | 57ab0abdc8f8e7c0a637cefd99b1b301f38a688a23665ab4b79706c0322aee79 |
| 10-Q_2026-09-30_whr-20260930.htm.jsonl | fcb812ee3d689deda5b3b52e3e59247b14c895af1012121c618ce6f8160cb6a6 |
| EX-99.1_2026-05-06_exhibit991pressrelease0331.htm.jsonl | 95b2ef1bae0716bbeb58c9c34ddb215005331537ecf7f29431fb7a2c2c9fd7ca |
| EX-99.1_2026-08-03_exhibit991pressrelease0630.htm.jsonl | b491ad294927787c02725c1a866e27f9e64402f8ea8aae9c4fd1904e04af4f8b |
| EX-99.1_2026-10-26_exhibit991pressrelease0930.htm.jsonl | c58aa3164f5692dfdb8e88300126ff35ac0e51e9ac5dd75d63c08d88b2ba7c69 |

Run settings (not issuer evidence): `context` sha256 584c197fbf255cc4fcd3a144aa71822e32a12b1a0036ed5924f197ae8dd98251.

Supplied handoffs, all opened and audited:

| Module | sha256 |
| --- | --- |
| CP-0 (source readiness) | 57c8443c6c648363633bdf1bf18dc588ac6f20998e98976e8abae94edbb6ab9f |
| CP-1 (financial base) | 7fe5db14c86f462c1616290a0d889a11d8753a40945d90327ecf223fcaa814d6 |
| CP-1A (business and transaction) | 742365d2be576f9d9c7e15906a9181a669e85729010195f850b2b4d4bacef63c |
| CP-2 (credit view) | 54f7d6097db13a1bbb14764512d75101ae7c15de422a85d8c1e938b1da8180bf |

Locators use `file page:N`, the pinned source chunk, not the printed page. Module status: Ready with Limitations (all inputs available; executed financing documents, borrowing base and investor presentation are not). Traceability scope: Top 5. Entity key: issuer_id whr, available. Upstream re-anchor: every handoff names WHIRLPOOL CORP /DE/, as-of 2026-11-05, current period Q3 2026 and prior period FY2025, in USD millions, with matching run identity.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial, business and credit handoffs trace to filed pages: every figure checked matched its source and derived rows show their inputs. Committee use should be restricted because covenant headroom and usable liquidity cannot be traced. | Medium | The borrowing base, covenant definitions and executed financing documents are not supplied, and EBITDA is analyst-built rather than company-printed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every reported figure checked against the filings matched, including debt, cash, cash flow and the quarterly ongoing EBIT reconciliations. | Reported leverage, liquidity and maturity inputs can be relied on as filed. | High |
| Derived rows reproduce from their inputs, but the derived maturity profile exceeds balance sheet debt by 42 with no explanation in the sources. | The maturity wall should be treated as approximate in any refinancing analysis. | Medium |
| The 0.97x fixed charge figure is an analyst proxy, not the covenant, and the borrowing base is not disclosed. | Covenant headroom and usable liquidity cannot be confirmed and must stay open. | Medium |
| Two wording points in the credit view needed correction: the asset-based facility expiry is not supplied rather than absent, and the issuer of the 2028 euro note is not named. | Minor and corrected here; no conclusion changes. | High |
| Year-end net debt and the fourth-quarter inflow come from management guidance, so those rows rest on forecasts. | Deleveraging conclusions are only as reliable as that guidance. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 1 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the asset-based facility's borrowing base, Availability and covenant definitions, which matters because usable liquidity and covenant headroom are what break first when earnings fall further, and it implies that committee use is limited to descriptive statements on leverage, liquidity and maturities until those inputs are obtained. Over 160 figure and quote checks against the pinned pages found no mismatch, so the remediation is about what is missing and how derived rows are labelled, not about misquoted figures.

### Traceability summary

| Driver | Class | Traceability status | Main provenance point |
| --- | --- | --- | --- |
| Leverage 9.52x on ongoing EBITDA | Calculated | Committee-Ready with caveat | Inputs sourced; EBITDA is analyst-built |
| Liquidity of 3,296 | Directly Sourced | Remediation Needed | Nominal; borrowing base not supplied |
| Refinancing and secured ranking | Calculated | Remediation Needed | Maturity profile derived; documents not supplied |
| Earnings decline | Directly Sourced | Committee-Ready | Ongoing EBIT is a management measure |
| Year-end deleveraging | Assumption-Based | Remediation Needed | Rests on guidance |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_whr-20251231.htm.jsonl | High: filed, audited (Ernst & Young LLP opinion February 11, 2026) | FY2025 with FY2024 and FY2023 | Whirlpool Corporation and consolidated subsidiaries | Statements, debt note, facilities, segments, leases, purchase obligations, ratings, business description | Text conversion flattens tables; no XBRL | Financial base, business, credit view |
| S2 | 10-Q_2026-03-31_whr-20260331.htm.jsonl | High: filed, unaudited | Q1 2026 | Same | Statements, facilities (3,500 less 290 drawn), May 2026 amendment | Unaudited | Financial base, liquidity series |
| S3 | 10-Q_2026-06-30_whr-20260630.htm.jsonl | High: filed, unaudited | Q2 and six months 2026 | Same | Statements, restricted cash of 212, ABL | Unaudited | Financial base, liquidity series |
| S4 | 10-Q_2026-09-30_whr-20260930.htm.jsonl | High: filed, unaudited; latest before cutoff | Q3 and nine months 2026 | Same | Statements, Notes 1, 5, 6, segments, MD&A liquidity | Unaudited; no post-refinancing debt table; no interim cash interest | All modules |
| S5 | EX-99.1_2026-05-06_exhibit991pressrelease0331.htm.jsonl | Medium: management release | Q1 2026 | Same | Outlook, balance sheet | Management measures | Outlook timeline |
| S6 | EX-99.1_2026-08-03_exhibit991pressrelease0630.htm.jsonl | Medium: management release | Q2 2026 | Same | Outlook, balance sheet | Management measures | Outlook timeline |
| S7 | EX-99.1_2026-10-26_exhibit991pressrelease0930.htm.jsonl | Medium: management release with non-GAAP reconciliations | Q3 2026 with Q4 2025 to Q3 2026, FY2024, FY2025 and FY2026 outlook | Same | Ongoing EBIT by quarter, guidance, India like-for-like | Non-GAAP and forecast figures are management measures | Ongoing EBITDA, guidance rows |
| C1 | context (run settings) | Not issuer evidence | Run | Whirlpool Corporation | As-of, cutoff, periods, USD | Ratings, quotes, valuation blank | Scope only |
| H0 | CP-0 handoff | Derived: readiness review | Run | Whirlpool Corporation | Source register and gaps G1 to G11 | Not a source of financial figures | Upstream anchor |
| H1 | CP-1 handoff | Derived: financial base | FY2024 to LTM Q3 2026 | Whirlpool Corporation | Metrics, chart tables, calculations | EBITDA analyst-built | Audited here |
| H1A | CP-1A handoff | Derived: business and transaction | Through 2026-10-27 | Whirlpool Corporation | Operating model, profile, governance, timeline | Management language labelled | Audited here |
| H2 | CP-2 handoff | Derived: credit view | As of 2026-11-05 | Whirlpool Corporation | Credit view, risks, liquidity, covenants | Proxy and guidance rows | Audited here |

Missing required inputs: none blocking. Citation limitations: no XBRL or native citations; page chunks only. Entity-key status: issuer_id available.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage of 9.52x total debt over ongoing EBITDA (7.98x net) for the twelve months to Q3 2026, against 6.11x in FY2025 | CP-1 and CP-2 | Total debt 6,852 (14 + 0 + 6,838) and ongoing EBITDA 720 (ongoing EBIT 338 + D&A 382) | Debt service and refinancing capacity depend on earnings, which fell while debt rose by 332 | Sets default and refinancing risk posture | S4 pages:5-7; S7 pages:11-18; S1 page:77 | EBITDA is not company-printed; India perimeter mismatch |
| 2 | Liquidity of 3,296: cash 1,103 plus undrawn commitments 2,193 | CP-1 and CP-2 | Cash and commitments printed; nothing drawn on the ABL or Brazil facilities | Funds the seasonal working capital swing and near-term maturities | Determines runway before the guided year-end release | S4 pages:6, 20-21, 54 | Borrowing base, Availability and letters of credit not supplied |
| 3 | Refinancing: 2,000 of second lien notes and a 2,000 first-lien ABL, with 14 due in the next twelve months and 585 in 2028 | CP-1, CP-1A, CP-2 | Issuance and ranking printed; maturity buckets derived from the 2025-12-31 schedule | Clears near-term maturities but subordinates unsecured notes | Drives refinancing and structural ranking view | S4 pages:17-22, 53; S1 page:101 | Maturity profile derived, 42 unexplained; indentures not supplied |
| 4 | Earnings decline: Q3 2026 ongoing EBIT 97 against 180, LTM ongoing EBITDA 720 against 1,067 in FY2025 | CP-1 and CP-2 | Quarterly ongoing EBIT reconciliations; FY2025 ongoing EBIT 729 | Fixed cost under-absorption and tariffs cut margin faster than sales | Primary driver of leverage and cover | S7 pages:11-17 | Non-GAAP; India included in comparatives |
| 5 | Year-end deleveraging: nine-month operating cash flow (826) against guidance of about 700 for the year | CP-1 and CP-2 | Nine-month cash flow printed; guidance in the release | Net debt below 4,500 needs a Q4 inflow of about 1,526 | Tests whether liquidity is adequate through the seasonal trough | S4 page:7; S7 pages:1-2 | Guidance is a forecast; implied inflow is derived |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 6,852 and cash 1,103 at 2026-09-30 | CP-1 | "Long-term debt 6,838 5,583", "Notes payable 14 351", "Cash and cash equivalents $ 1,103 $ 669" (S4 page:6) | Yes | High | Directly Sourced | Reproduced | High | Committee-Ready |
| Ongoing EBITDA 720 for the latest twelve months | CP-1 | Ongoing EBIT 135, 44, 62, 97 (S7 pages:11-14); D&A 338, 246, 290 (S1 page:77; S4 page:7) | Yes | Medium (non-GAAP plus statements) | Calculated | Reproduced | Medium | Committee-Ready with caveat |
| Leverage 9.52x and 7.98x | CP-1, CP-2 | 6,852 / 720 and 5,749 / 720 | Yes | Medium | Calculated | Reproduced | Medium | Committee-Ready with caveat |
| Liquidity 3,296 | CP-1, CP-2 | ABL "up to $2.0 billion", "no amount drawn" (S4 page:21); Brazil about 193 (S4 page:21) | Yes | High for commitments | Directly Sourced | Reproduced; usable availability not traceable | Medium | Remediation Needed |
| Maturity buckets 14 / 585 / 695 / 592 / 5,008 | CP-1, CP-2 | 10-K schedule (S1 page:101); "$14 million of debt maturing in the next twelve months" (S4 page:53); Secured Notes (S4 page:17) | Yes | Medium | Calculated | Derived; 42 unexplained | Medium | Remediation Needed |
| Second lien and first lien ranking on one collateral pool | CP-1, CP-1A, CP-2 | "second-priority basis" and "first-priority lien" (S4 page:22); "substantially all the assets" (S4 page:67) | Yes | High for the issuer summary | Directly Sourced | Reproduced; documents not supplied | Medium | Remediation Needed |
| Springing covenant at 1.00x with Availability trigger | CP-1, CP-2 | "greater of 10% of the Line Cap" and "$135 million" (S4 pages:20-21) | Yes | High | Directly Sourced | Reproduced | High | Committee-Ready |
| Fixed charge proxy 0.97x | CP-2 | (720 - 405) / 326 | Yes | Low | Analyst Inference | Labelled as proxy | Low | Remediation Needed |
| Lowe's about 15% of sales and about 44% of receivables | CP-1A, CP-2 | S1 pages:17, 20 | Yes | High | Directly Sourced | Reproduced | High | Committee-Ready |
| Implied fourth-quarter inflow of about 1,526 | CP-2 | Guidance about 700 (S7 page:2); nine-month (826) (S4 page:7) | Yes | Low | Assumption-Based | Derived from guidance | Low | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales FY2025 15,524 and FY2024 16,607 | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | page:75 income statement | CP-1 metrics table | Sourced | High | Matched |
| Operating profit FY2025 838 and FY2024 143; interest expense 341 and 358 | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | page:75 | CP-1 metrics table | Sourced | High | Matched |
| Total EBIT FY2025 824 and FY2024 63 (company definition) | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | page:133 segment note | CP-1 metrics table | Sourced | High | Matched |
| Depreciation and amortization 338 and 333; operating cash flow 470 and 835; capex 389 and 451; dividends paid 300 and 384; cash paid for interest 350 and 352; cash paid for taxes 136 and 181 | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | page:77 cash flow statement | CP-1 metrics, interest cover | Sourced | High | Matched |
| Balance sheet 2025-12-31: cash 669; notes payable 351; current maturities 586; long-term debt 5,583; equity 2,726 | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | page:76 balance sheet | CP-1 metrics, leverage | Sourced | High | Matched; FY2024 column 1,275, 18, 1,850, 4,758, 2,683 also matched |
| Debt table and maturities at 2025-12-31 (2026 586; 2027 702; 2028 585; 2029 695; 2030 592; thereafter 3,008; total 6,169) | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | pages:100-101 Note 6 | CP-1 debt stack and maturities | Sourced | High | Matched; instrument rows sum to 6,170 against 6,169 printed (rounding) |
| Facilities at 2025-12-31: 3,500, Brazil 182, 250 drawn; interest coverage covenant of at least 3.0 | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | page:104 | CP-1 liquidity chart, CP-2 covenants | Sourced | High | Matched |
| Net sales 10,467 and 11,426; operating profit 185 and 595; interest expense 241 and 256 (nine months) | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | page:5 income statement | CP-1 metrics | Sourced | High | Matched |
| Total EBIT nine months 34 and 590; segment net sales and EBIT by segment | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:43-44 Note 13 | CP-1 segment table | Sourced | High | Matched |
| Balance sheet 2026-09-30: cash 1,103; notes payable 14; current maturities nil; long-term debt 6,838; lease liabilities 863; pensions 83 and 91; equity 3,726 | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | page:6 | CP-1 metrics, CP-2 claims table | Sourced | High | Matched |
| D&A 290 and 246; operating cash flow (826) and (669); capex 255 and 239; dividends paid 81 and 248 | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | page:7 cash flow statement | CP-1 metrics, CP-2 | Sourced | High | Matched |
| ABL up to 2,000, nothing drawn; Brazil about 193 with tranches through 2027 and 2028; springing 1.00x test | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:20-21 Note 5 | CP-1 liquidity, CP-2 covenants | Sourced | High | Matched; ABL maturity date not printed |
| Secured Notes: 1,000 of 7.500% due 2031 and 1,000 of 7.875% due 2034, issued June 16, 2026; guarantors; liens; 101% change of control | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:17-18, 22 | CP-1 debt stack, CP-1A, CP-2 | Sourced | High | Matched |
| "We have $14 million of debt maturing in the next twelve months"; cash about 1.1 billion; US share of cash 3.7% of assets | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:53-54 MD&A liquidity | CP-1 maturities, CP-2 liquidity | Sourced | High | Matched |
| Equity issuance 524 and 557 net; dividend suspended; 8.50% preferred with 575 liquidation preference, convertible February 15, 2029 | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:6, 38-39, 52-53, 57 | CP-1A, CP-2 | Sourced | High | Matched |
| Supply chain finance 650 and 772; synthetic lease guarantees 96 and 504 with 147 letters of credit; receivables purchase capacity 250 and 157 serviced; guarantees about 1.2 billion; instruments of about 578 | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:10-12, 23, 28, 58 | CP-1 definition review, CP-2 claims | Sourced | High | Matched |
| Brazil tax assessments about 545, 88, 61 and 112 unreserved | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:24-25 Note 6 | CP-1, CP-2 | Sourced | High | Matched |
| Casas Bahia charge 54 (46 credit loss net of expected recoveries of 112 against 157 gross); India impairment 124 | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:14, 55 | CP-1, CP-1A, CP-2 | Sourced | High | Matched |
| Supsa closure costs and cash of about 75; restructuring of about 170 for 2026 | source-text/ | 10-Q_2026-09-30_whr-20260930.htm.jsonl | S4 | pages:41, 51 | CP-1A, CP-2 | Sourced | High | Matched |
| Facilities at 2026-03-31: 290 drawn, Brazil 192, May 2026 amendment cutting 3,500 to 2,250 and excluding Q1 from the coverage test | source-text/ | 10-Q_2026-03-31_whr-20260331.htm.jsonl | S2 | page:17 | CP-1 liquidity, CP-2 | Sourced | High | Matched |
| Cash 1,239 including 212 restricted at 2026-06-30; ABL nothing drawn; Brazil 193 | source-text/ | 10-Q_2026-06-30_whr-20260630.htm.jsonl | S3 | pages:6-7, 21 | CP-1 liquidity | Sourced | High | Matched |
| Ongoing EBIT: Q3 2026 97; Q2 2026 62; Q1 2026 44; Q4 2025 135; Q3 2025 180; Q2 2025 200; Q1 2025 214; FY2025 729; FY2024 887 | source-text/ | EX-99.1_2026-10-26_exhibit991pressrelease0930.htm.jsonl | S7 | pages:11-18 reconciliations | CP-1 ongoing EBITDA | Sourced (management non-GAAP) | Medium | Matched; quarters sum to 729 for 2025 |
| Total EBIT by quarter: Q3 2026 (128); Q2 154; Q1 9; Q4 2025 234; net sales Q4 2025 4,098 | source-text/ | EX-99.1_2026-10-26_exhibit991pressrelease0930.htm.jsonl | S7 | pages:11-14 | CP-1 quarterly path | Sourced | Medium | Matched |
| Guidance: net debt below 4,500; operating cash flow about 700; free cash flow about 300; ongoing EBIT about 293; interest expense about 350; Q4 interest about 103 | source-text/ | EX-99.1_2026-10-26_exhibit991pressrelease0930.htm.jsonl | S7 | pages:1-2, 19-20 | CP-2 | Management guidance | Medium | Matched; forecasts |
| Like-for-like 2025 ongoing EBIT about 688 and India about 41 | source-text/ | EX-99.1_2026-10-26_exhibit991pressrelease0930.htm.jsonl | S7 | page:24 | CP-1 gap, CP-2 gap | Sourced (management) | Medium | Matched |
| Outlook for 2026 earnings per share moved from 2.45 to 2.95, to 2.25 to 2.75, to (4.95) | source-text/ | EX-99.1 releases of May 6, August 3 and October 26, 2026 | S5, S6, S7 | page:1 each | CP-1A timeline | Management guidance | Medium | Matched |
| Lowe's about 15% of 2025 sales and about 44% of year-end receivables; no long-term sales contracts for most products | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | pages:17, 20 | CP-1A, CP-2 | Sourced | High | Matched |
| Ratings below investment grade at all three agencies; Moody's Ba3 and Fitch BB- in Q2 2026; S&P BB negative | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl; 10-Q_2026-09-30_whr-20260930.htm.jsonl | S1, S4 | S1 page:38; S4 page:53 | CP-1A, CP-2 | Sourced | High | Matched; outlooks for the later actions not stated |
| Operating lease liabilities 836 at 2025-12-31; purchase obligations 481 | source-text/ | 10-K_2025-12-31_whr-20251231.htm.jsonl | S1 | pages:96-97, 108-109 | CP-2 claims table | Sourced | High | Matched |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM net sales 14,565 | CP-1 metrics | 15,524; 11,426; 10,467 | FY2025 - 9M 2025 + 9M 2026 | Calculated | Reproduced | High | Monitoring | S1 p75; S4 p5 |
| LTM operating profit 428; LTM EBIT 268; LTM interest expense 326 | CP-1 metrics | 838, 595, 185; 824, 590, 34; 341, 256, 241 | Same LTM construction | Calculated | Reproduced | High | PD, liquidity | S1 pp75, 133; S4 pp5, 44 |
| LTM ongoing EBIT 338 | CP-1 | 135, 44, 62, 97; also 729 - 594 + 203 | Sum of four quarters; cross-check by LTM construction | Calculated | Reproduced | Medium | PD | S7 pp11-17 |
| LTM D&A 382 | CP-1 | 338, 246, 290 | 338 - 246 + 290 | Calculated | Reproduced | High | PD | S1 p77; S4 p7 |
| Ongoing EBITDA FY2024 1,220; FY2025 1,067; LTM 720 | CP-1, CP-2 | 887 + 333; 729 + 338; 338 + 382 | Ongoing EBIT + D&A; D&A may include accelerated depreciation already added back | Calculated | Reproduced; definition risk | Medium | PD, refinancing | S7; S1; S4 |
| Total debt 6,626; 6,520; 6,852 | CP-1 | 18 + 1,850 + 4,758; 351 + 586 + 5,583; 14 + 0 + 6,838 | Notes payable + current maturities + long-term debt | Calculated | Reproduced (6,626; 6,520; 6,852) | High | Refinancing | S1 p76; S4 p6 |
| Net debt 5,351; 5,851; 5,749 | CP-1 | Total debt less cash 1,275; 669; 1,103 | Subtraction | Calculated | Reproduced | High | Leverage | S1 p76; S4 p6 |
| Leverage 5.43x, 6.11x, 9.52x; net 4.39x, 5.48x, 7.98x | CP-1, CP-2 | Rows above | 6,626 / 1,220; 6,520 / 1,067; 6,852 / 720; 5,351 / 1,220; 5,851 / 1,067; 5,749 / 720 | Calculated | Reproduced to two decimals | Medium | PD | CP-1 |
| Operating-profit basis leverage 13.92x, 5.54x, 8.46x; net 11.24x, 4.98x, 7.10x | CP-1, CP-2 | EBITDA 476, 1,176, 810 | Total or net debt / (operating profit + D&A) | Calculated | Reproduced | Medium | PD | CP-1 |
| Cash interest cover 3.47x and 3.05x | CP-1 chart | 1,220 / 352; 1,067 / 350 | Ongoing EBITDA / cash paid for interest | Calculated | Reproduced | Medium | Debt service | S1 p77 |
| Interest-expense cover 3.41x, 3.13x, 3.28x, 2.05x, 2.21x | CP-1, CP-2 | 1,220/358; 1,067/341; 840/256; 493/241; 720/326 | Ongoing EBITDA / interest expense | Calculated | Reproduced | Medium | Debt service | CP-1 |
| Operating cash flow less capex (92) LTM; (908) and (1,081) nine months | CP-1 | 313 and 405; (669) - 239; (826) - 255 | OCF - capex | Calculated | Reproduced; company prints (907) for 9M 2025 | Medium | Liquidity | S4 p7; S7 p1 |
| Liquidity undrawn 3,432; 3,402; 2,193; 2,193 | CP-1 chart | 3,500 - 250 + 182; 3,500 - 290 + 192; 2,000 + 193 | Commitments - drawn + Brazil | Calculated | Reproduced; nominal | Medium | Liquidity | S1 p104; S2 p17; S3 p21; S4 p21 |
| Unrestricted cash 1,027 at 2026-06-30 | CP-1 chart | 1,239 - 212 | Subtraction | Calculated | Reproduced | High | Liquidity | S3 p7 |
| Maturity buckets 14 / 585 / 695 / 592 / 5,008 | CP-1, CP-2 | 10-K schedule; 3,008 + 1,000 + 1,000 | Rebuild from 2025-12-31 schedule plus Secured Notes | Calculated (derived) | Reproduced; sum 6,894 vs 6,852 | Medium | Refinancing | S1 p101; S4 pp17, 53 |
| Secured Notes coupon about 154; added coupon about 139 | CP-2 | 1,000 x 7.500% + 1,000 x 7.875%; 587 x 1.25% + 703 x 1.10% | 153.75 - 15.07 | Calculated (approximate) | Reproduced | Medium | Debt service | S4 p17; S1 p100 |
| Run-rate interest 408 and cover 1.76x; guided EBIT cover 0.84x | CP-2 | 102 x 4; 720 / 408; 293 / 350 | Annualise Q3; ratio | Calculated | Reproduced; illustrative | Low | Debt service | S4 p5; S7 p19 |
| Fixed charge proxy 0.97x | CP-2 | 720, 405, 326 | (EBITDA - capex) / interest expense | Calculated (proxy) | Reproduced; not the covenant | Low | Covenant headroom | CP-1 |
| Implied Q4 inflow 1,526; implied net debt reduction 1,249 | CP-2 | 700 - (-826); 5,749 - 4,500 | Subtraction | Assumption-Based | Reproduced; depends on guidance | Low | Liquidity, refinancing | S7 p2; S4 p7 |
| Unsecured notes about 4,900 (4,919) and 4,838 | CP-2 | 10-K carrying values; 6,852 - 2,000 - 14 | Sum; subtraction | Calculated | Reproduced; 81 unexplained | Low | LGD mechanic | S1 p101 |
| Back-loading 73% | CP-2 | 5,008 / 6,894 | Ratio | Calculated | Reproduced (72.6%) | Medium | Refinancing | CP-1 |
| US cash about 628; preferred dividend about 49 | CP-2 | 3.7% x 16,963; 575 x 8.50% | Product | Calculated | Reproduced; rounded percentage | Low | Liquidity | S4 pp6, 54 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | Usable liquidity and covenant headroom (CP-1, CP-2) | Borrowing base, Availability, Line Cap, letters of credit on the ABL and the covenant definition are not in the sources | Insufficient Information | Liquidity and covenant headroom decide near-term default risk; nominal undrawn commitments can overstate usable liquidity | Obtain the ABL agreement and latest borrowing base and compliance certificates | CP-1 liquidity chart; CP-2 liquidity and covenants tables |
| Material | Fixed charge proxy 0.97x (CP-2) | Analyst-built; excludes cash taxes, scheduled principal and distributions that a definition may include | Analyst Inference | A reader could take it as the covenant ratio | Keep the proxy label; replace with the reported ratio when available | CP-2 reader summary and covenants table |
| Material | Maturity profile (CP-1, CP-2) | Rebuilt from a pre-refinancing table; 42 unexplained against balance sheet debt | Calculated | Approximate wall could misstate 2028 to 2030 pressure | Obtain a post-refinancing debt table | CP-1 chart; CP-2 maturity table |
| Material | Ongoing EBITDA (CP-1, CP-2) | Analyst-built from ongoing EBIT plus cash flow D&A; accelerated depreciation may be counted twice; India included in Q4 2025 | Calculated | Leverage and cover move with the definition | State both bases (already done); obtain company EBITDA reconciliation | CP-1 metrics; CP-2 leverage |
| Material | Unsecured creditor ranking (CP-2) | Note 5 lists first-priority liens on eligible capital, receivables, inventory, intellectual property and machinery; the risk factor says second lien on "substantially all" assets | Directly Sourced (two descriptions) | Scope of collateral drives structural subordination | Obtain the security documents | CP-2 key findings; CP-1A |
| Minor | Year-end net debt and inflow (CP-2) | Based on management guidance | Assumption-Based | Forecast risk | Track Q4 results | CP-2 |
| Minor | Rating outlooks (CP-2 risks) | "Negative outlooks cited" holds for S&P and for the Moody's and Fitch actions up to early 2026; outlooks for the second-quarter actions are not stated | Directly Sourced (partial) | Wording slightly broader than the source | Say outlooks are stated only for some actions | CP-2 risks table |
| Minor | Issuer of the 0.50% 2028 euro note (CP-1A, CP-2) | The pack names a subsidiary issuer for the 2026 and 2027 notes and a general Company guarantee statement; the 2028 note's issuer is not named | Weak Lineage (limited) | Affects structural position of that series | Obtain the note terms | CP-2 debt table; CP-1A profile |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 and all three 2026 quarters (S1 to S7) | Missing financing documents leave legal terms issuer-summarised | Covenant and ranking statements are descriptive only | Obtain indenture, ABL agreement, borrowing base |
| Citation completeness | Committee-Ready | Over 160 figure and quote checks matched pinned pages; the handoffs cite page chunks | A page chunk is coarser than a native citation | Low | None beyond keeping locators |
| Calculation traceability | Ready with Remediation | Derived rows show inputs and reproduce (T5B.5) | Analyst-built EBITDA and proxies can be mistaken for reported figures | Leverage and cover are definition-dependent | Keep labels; obtain company EBITDA |
| Assumption transparency | Ready with Remediation | Guidance rows and the fixed charge proxy are labelled | Forecast-based rows could be read as outcomes | Year-end deleveraging is conditional | Track Q4 results |
| Markdown and export artifact integrity | Committee-Ready | Each handoff has the six required headings, reader summary and opening view; chart tables are well formed | A formatting fault would break report assembly | None found | None |

Overall auditability: Ready with Remediation (lowest of the five dimensions).

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | ABL borrowing base, Availability, Line Cap, letters of credit, maturity date | ABL Credit and Guaranty Agreement; borrowing base certificate | Usable liquidity and covenant headroom drive near-term default risk | CP-1 liquidity; CP-2 liquidity and covenants | High impact | ABL agreement and certificates |
| CP-5-GAP-002 | Covenant definitions and the reported fixed charge ratio | Credit agreement definitions; compliance certificate | The 0.97x proxy cannot be tied to the test | CP-2 covenants | High impact | ABL agreement |
| CP-5-GAP-003 | Post-refinancing debt table and maturity schedule | Debt note by instrument at 2026-09-30 | Maturity wall is derived; 42 unexplained | CP-1 chart; CP-2 | Medium impact | Next 10-K or a debt note |
| CP-5-GAP-004 | Interim cash paid for interest and taxes | Supplemental cash flow disclosure for 2026 quarters | Cash interest cover cannot be read | CP-1 chart; CP-2 | Medium impact | Quarterly supplemental data |
| CP-5-GAP-005 | Indentures for the Secured Notes and the pre-2026 unsecured notes | Indentures, supplemental indentures, guarantor list | Lien covenants, guarantee structure and equal and ratable security cannot be tested | CP-1A governance; CP-2 ranking | High impact | Indentures |
| CP-5-GAP-006 | Company EBITDA and net debt leverage reconciliation | Releases define but do not print them | EBITDA is analyst-built | CP-1; CP-2 | Medium impact | Company supplemental |
| CP-5-GAP-007 | Like-for-like financials excluding Whirlpool India | Full income statement and balance sheet without India | Trend and LTM perimeter mismatch | CP-1; CP-2 | Medium impact | Company supplemental |
| CP-5-GAP-008 | Rating-agency reports and market data | Reports, prices, spreads | No market-implied view; outlooks for later actions unknown | CP-2 | Low impact | Agency reports |
| CP-5-GAP-009 | Beneficial ownership above 5% and board data | Proxy statement | Control rights not assessable | CP-1A | Low impact | Proxy statement |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | whr-2026-11-05-credit_snapshot-host, sha256 57c8443c | Source readiness | High filings | Six required headings present; run transport, no YAML envelope | Cleared with limitations | Gaps G1 to G11 carried |
| CP-1 | whr-2026-11-05-credit_snapshot-host, sha256 7fe5db14 | Financial base | High filings, medium releases | Six headings, chart selectors and one metrics table present | Cleared with limitations | EBITDA analyst-built |
| CP-1A | whr-2026-11-05-credit_snapshot-host, sha256 742365d2 | Business and transaction | High filings | Six headings, selectors present | Cleared with limitations | Legal documents not supplied |
| CP-2 | whr-2026-11-05-credit_snapshot-host, sha256 54f7d609 | Credit view | Derived | Six headings, key findings and strengths and weaknesses present | Cleared with limitations | Proxy and guidance rows labelled |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Key findings: ABL "secured by substantially all assets" | Supported at S4 page:67 (risk factor); no locator given in the handoff | Locator omitted and wording differs from Note 5 (S4 page:22) | Cite both pages; read as two issuer descriptions | None on figures |
| Minor | CP-2 | Liquidity: "Facilities expiring within twelve months: none identified for the ABL" | Not supported as stated: the ABL maturity date is not printed | Reads as if the ABL does not expire soon, when the date is not supplied | Read as "ABL maturity not supplied" (corrected here) | None on figures |
| Minor | CP-1A, CP-2 | Euro notes "issued by a wholly owned subsidiary" applied to the 2028 series | Supported only for the 2026 and 2027 notes (S4 page:18) and the general guarantee statement (S1 page:101) | Overgeneralised to the 2028 series | Read as "issuer of the 2028 note not named" (corrected here) | None |
| Minor | CP-1 | Request: "no subsidiary issuer ... to separate" | Reporting perimeter is correct; subsidiary-issued guaranteed notes exist (S1 page:101; S4 page:18) | Wording could be read as no subsidiary debt | Read as "single consolidated reporting perimeter, with subsidiary-issued notes guaranteed by the Company" | None |
| Minor | CP-2 | Risks: "negative outlooks cited" | Partly supported (S1 page:38) | Outlooks for the second-quarter 2026 actions are not stated | Narrow the wording | None |
| Minor | CP-2 | Unsecured notes "about USD 4.8 billion" in findings and "About 4,900" in the debt table | Both derived; difference of 81 explained only in calculations | Two figures for one item | Read as 4.8 to 4.9 billion | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Ongoing EBITDA 720 and ratios | Ongoing EBIT plus cash flow D&A; the company does not print EBITDA; D&A may overlap with restructuring add-backs | None between sources; definition is analyst-built | Keep both bases; obtain company EBITDA | Restricts leverage to indicative |
| Material | CP-2 | Fixed charge proxy 0.97x | Excludes cash taxes, principal and distributions | None | Keep proxy label | Restricts covenant statements |
| Minor | CP-1 | Operating cash flow less capex (908) for 9M 2025 | Company prints (907) | 1 difference between computed and printed | Rounding in the source | None |
| Minor | CP-1 | Total EBIT LTM 268 against quarter sum 269 | Rounding of printed quarters | 10-Q nine-month 34 against quarters 35 | Rounding | None |
| Material | CP-1, CP-2 | Perimeter mixing: LTM ongoing EBIT and D&A include India in Q4 2025, debt excludes it | India deconsolidated December 1, 2025 | Release gives India FY2025 ongoing EBIT of about 41 | Disclosed in CP-1 gap G6; no adjusted ratio computed | Leverage slightly overstated in earnings, not adjusted |
| Minor | CP-2 | Unsecured notes 4,919 against 4,838 | Carrying values at different dates | 81 unexplained | Disclosed in calculations | None |

Recomputation result: all items in T5B.5 were recomputed from the cited figures and reproduced; no hand-derived value was found wrong.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | CP-1A, CP-2 | ABL first lien and Secured Notes second lien on one collateral pool, guaranteed by domestic and Canadian ABL obligors | Indenture, ABL agreement, security and intercreditor documents | Only issuer summaries (S4 pages:18, 22, 67) | Obtain documents | Legal review of lien scope and ranking |
| Material | CP-1A, CP-2 | Whether the lien grant complied with the pre-2026 unsecured notes' lien covenants | Existing indentures | Not supplied | Obtain indentures | Legal review of equal and ratable security |
| Material | CP-2 | Springing fixed charge test of 1.00x and its trigger | Credit agreement definitions | Definition of Availability, Line Cap and fixed charges not supplied | Obtain agreement | Covenant interpretation |
| Minor | CP-1A | Preferred ranking (senior to common, junior to indebtedness) | Certificate of designations | Issuer summary only (S4 page:39) | Obtain certificate | None critical |
| Minor | CP-1A, CP-2 | Change of control puts at 101% | Indentures | Issuer summary (S4 page:18) | Obtain indentures | None critical |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | None made: no spread, price, yield, peer or valuation claim appears in any handoff, as the module instructions require | Bond prices, spreads, ratings reports (the filings disclose a long-term debt fair value of 5.5 billion at 2026-09-30, S4 page:36, not used) | Context quotes, ratings and valuation are blank | None for this run | No market-implied view available to the committee |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Same EBITDA definition and the same figures (720; 9.52x; 7.98x; 8.46x; 7.10x) are used in both; no drift found | None; CP-2 cites CP-1 sha256 7fe5db14 | None | Consistent |
| Minor | CP-1A, CP-2 | Total debt 6,852, cash 1,103, undrawn 2,193, ongoing EBITDA 720 match across CP-1, CP-1A and CP-2 | None | None | Consistent |
| Minor | CP-0, CP-1 | CP-0 gap G8 says ratings appear only in the 10-Q Q3 narrative; CP-1A and CP-2 also cite the 10-K (S1 page:38) for S&P | CP-0 cannot be edited | Read CP-0 G8 as covering the 10-Q Q3; the 10-K also carries ratings | None |
| Minor | CP-1, CP-2 | CP-1 reports 4 chart periods for liquidity; CP-2 repeats the September and December rows only | None | None | Consistent |
| Minor | CP-1, CP-2 | Second-quarter-2026 maturity and liquidity statements agree with S3; no handoff overwrote a later source | None | None | Consistent |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Duplication | Leverage, liquidity and maturity tables are restated in CP-2 from CP-1; consistent and intentional | None | None |
| Material | CP-2 | Materiality | The reader summary gives the 0.97x proxy equal visibility to reported figures; labelled as a proxy | Keep label | Reader could over-weight it |
| Critical | All | Committee readiness | Usable liquidity and covenant headroom are untraceable | Obtain ABL documents | Committee use restricted to descriptive leverage, liquidity and maturity statements |

Committee status: Restricted. QA status: Restricted. No numeric confidence score is assigned because the scoring script is not a supplied input of this run; the traceability band is Medium for reported figures and Low for the proxy, guidance and usable-liquidity rows.

#### T5.8 Handoff and export integrity

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Envelope | No YAML front matter or filename convention; the run transport uses six H2 headings instead | Not a defect of the content; the run transport governs | None |
| Minor | CP-1 | Chart tables | LTM interest cover is Not supplied with a reason; the other cells are plain numbers in x or US$m | None | Chart will omit that point |
| Minor | CP-1A | Selectors | Company and operating model and Company profile hold one table each; the transaction section is prose | None | None |
| Minor | CP-2 | Selectors | Key findings and Strengths and weaknesses are prose only | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISS-001 | Critical | CP-1, CP-2 | Insufficient evidence | ABL borrowing base, Availability and covenant definition not supplied | Obtain ABL documents | Restricts committee use | Open |
| ISS-002 | Material | CP-2 | Proxy | Fixed charge proxy 0.97x is not the covenant | Keep label | Restricts covenant statements | Open |
| ISS-003 | Material | CP-1, CP-2 | Derived data | Maturity profile derived; 42 unexplained | Obtain debt table | Approximate wall | Open |
| ISS-004 | Material | CP-1, CP-2 | Definition | Analyst-built EBITDA and India perimeter | Obtain company reconciliation | Indicative leverage | Open |
| ISS-005 | Material | CP-2 | Source tension | Collateral scope described two ways in the same filing | Obtain security documents | Ranking is descriptive | Open |
| ISS-006 | Minor | CP-2 | Wording | ABL expiry stated as none identified; it is not supplied | Corrected in this module | None | Resolved here |
| ISS-007 | Minor | CP-1, CP-1A, CP-2 | Wording | 2028 euro note issuer not named (CP-1A, CP-2); CP-1 request wording on subsidiary issuers | Corrected in this module | None | Resolved here |
| ISS-008 | Minor | CP-2 | Wording | Negative outlooks cited only for some actions | Corrected in this module | None | Resolved here |
| ISS-009 | Minor | CP-1 | Rounding | 9M 2025 free cash flow 908 against 907 printed; total EBIT LTM 268 against 269 | Rounding in source | None | Closed |
| ISS-010 | Minor | CP-2 | Presentation | Unsecured notes 4.8 and 4.9 billion | Read as a range | None | Resolved here |

## Calculations

Recomputations performed by this module, using only the cited figures:

1. Total debt: 18 + 1,850 + 4,758 = 6,626; 351 + 586 + 5,583 = 6,520; 14 + 0 + 6,838 = 6,852. Net debt: 6,626 - 1,275 = 5,351; 6,520 - 669 = 5,851; 6,852 - 1,103 = 5,749.
2. LTM figures: net sales 15,524 - 11,426 + 10,467 = 14,565; operating profit 838 - 595 + 185 = 428; D&A 338 - 246 + 290 = 382; interest expense 341 - 256 + 241 = 326; ongoing EBIT 135 + 44 + 62 + 97 = 338 and 729 - 594 + 203 = 338.
3. Ongoing EBITDA: 887 + 333 = 1,220; 729 + 338 = 1,067; 338 + 382 = 720. Ratios: 6,626 / 1,220 = 5.43; 5,351 / 1,220 = 4.39; 6,520 / 1,067 = 6.11; 5,851 / 1,067 = 5.48; 6,852 / 720 = 9.52; 5,749 / 720 = 7.98. Cash interest cover: 1,220 / 352 = 3.47; 1,067 / 350 = 3.05.
4. Operating-profit basis: 143 + 333 = 476; 838 + 338 = 1,176; 428 + 382 = 810; ratios 13.92, 11.24, 5.54, 4.98, 8.46 and 7.10, all reproduced.
5. Fixed charge proxy: 720 - 405 = 315; 315 / 326 = 0.966, shown as 0.97. Capital expenditures LTM 389 - 239 + 255 = 405.
6. Maturity buckets: 3,008 + 1,000 + 1,000 = 5,008; 14 + 585 + 695 + 592 + 5,008 = 6,894; 6,894 - 6,852 = 42; share 5,008 / 6,894 = 72.6%.
7. Implied Q4 inflow: 700 + 826 = 1,526. Net debt gap: 5,749 - 4,500 = 1,249.
8. Coupons: 1,000 x 7.500% = 75; 1,000 x 7.875% = 78.75; total 153.75; 587 x 1.25% = 7.34 and 703 x 1.10% = 7.73; difference 138.7.
9. Run-rate interest: 102 x 4 = 408; 720 / 408 = 1.76; guided 293 / 350 = 0.84.
10. Liquidity: 3,500 - 250 + 182 = 3,432; 3,500 - 290 + 192 = 3,402; 2,000 + 193 = 2,193; 1,103 + 2,193 = 3,296; 669 + 3,432 = 4,101; 1,239 - 212 = 1,027.
11. Unsecured notes: 586 + 697 + 600 + 300 + 298 + 300 + 600 + 299 + 249 + 497 + 493 = 4,919; 6,852 - 2,000 - 14 = 4,838; difference 81.
12. Statement-level checks: more than 160 figure and quote checks (statement lines, note text, release reconciliations and guidance) were run against the pinned pages. Every figure and quote in the handoffs that was checked matched its cited page. Checks that failed on the first attempt were only mis-specified search strings on the nine-month segment table, which sits on page 44; the handoffs cite pages 43-44 and are correct.

## Gaps

| Ref | Gap | Effect on traceability |
| --- | --- | --- |
| T1 | The borrowing base, Availability, Line Cap, letters of credit and covenant definitions for the ABL are not supplied (CP-5-GAP-001, CP-5-GAP-002). | Usable liquidity and covenant headroom are not traceable; committee use is restricted. |
| T2 | No post-refinancing instrument table; maturity profile derived with an unexplained 42 (CP-5-GAP-003). | Maturity wall approximate. |
| T3 | Interim cash interest and taxes not printed (CP-5-GAP-004). | Cash cover not traceable for 2026 periods. |
| T4 | Indentures and security documents not supplied (CP-5-GAP-005). | Ranking and lien-covenant statements rest on issuer summaries. |
| T5 | EBITDA, India like-for-like and rating reports not supplied (CP-5-GAP-006 to CP-5-GAP-008). | Leverage indicative; perimeter and market views not available. |
| T6 | Ownership data not supplied (CP-5-GAP-009). | Control rights not assessable. |

Wording corrections stated in this module (no earlier handoff is edited): the ABL expiry is not supplied rather than absent; the issuer of the 0.50% 2028 euro note is not named in the pack; the reporting perimeter is a single consolidated group although some notes are issued by a wholly owned subsidiary and guaranteed by the Company; rating outlooks are stated only for some actions; and the 0.97x figure is a proxy only.

## Next module

The traceable core is ready for use as descriptive support: reported leverage inputs, liquidity components, maturity buckets and ranking as the issuer describes them. Before any committee use that depends on covenant headroom, usable liquidity or unsecured creditor ranking, obtain the ABL agreement and the latest borrowing base and compliance certificates, the post-refinancing debt table and the indentures, then rerun the financial base and credit view with those inputs.
