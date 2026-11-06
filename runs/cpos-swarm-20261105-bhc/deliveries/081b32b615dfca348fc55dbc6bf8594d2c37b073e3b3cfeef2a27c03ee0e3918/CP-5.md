# CP-5 — Evidence trace and research integrity QA: Bausch Health Companies Inc. (bhc)

## Request

- Issuer: Bausch Health Companies Inc. (issuer id `bhc`), as of 2026-11-05, information cutoff 2026-11-05 (context), pathway credit_snapshot, run `bhc-2026-11-05-credit_snapshot-host`. Reporting currency USD, millions unless stated.
- Scope: Top 5 traceability (default) of the four accepted handoffs: the source readiness handoff (CP-0), the financial base (CP-1), the business and transaction context (CP-1A) and the credit synthesis (CP-2), plus the research integrity grade over them. This module is a governance layer: it changes no credit conclusion and repairs no lineage silently.
- Execution: host session. The host re-read the cited pages of the pinned sources, searched them for each checked figure, and recomputed the derived numbers. No provider was called. Information from outside the pinned sources was not used.
- Assertion: committee-use status is an audit of lineage and integrity, not an investment opinion.

## Sources

Issuer sources checked (page-numbered text extractions pinned by CP-OS; `page:N` is the extraction chunk, not a printed page):

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_bhc-20251231.htm.jsonl | dd4233546d8f09a0a7172210eae9b856cf06217c0da999f68b6e9a8283f6671d | Form 10-K for FY2025 (audited) |
| 10-Q_2026-03-31_bhc-20260331.htm.jsonl | 2ab4f9a58a29bd8e4f27c1aaa3b34a916ad63a6c5e24a2f2cf1f677d2bf1adb3 | Form 10-Q for Q1 2026 (unaudited) |
| 10-Q_2026-06-30_bhc-20260630.htm.jsonl | 9bd8cebbf75325a6e2424a90dc4ffd52c51b1a73535e612ffb413df53a0d5061 | Form 10-Q for Q2 2026 (unaudited) |
| 10-Q_2026-09-30_bhc-20260930.htm.jsonl | bbe6464eac7c28eba7ae73d3d4c1550a00ee295236fd32b72332e63bba1b2690 | Form 10-Q for Q3 2026 (unaudited) |
| EX-99.1_2026-04-29_ex991-q1x2026.htm.jsonl | a03142c8b51f52ce0bcea39df704d05d1ec6cd25d01c476f43f591aef5327135 | Q1 2026 earnings release (management, non-GAAP) |
| EX-99.1_2026-07-29_ex991-q22026.htm.jsonl | b572ec3ee8791446c7753f44c437564f85dc7c22a9282dc8fe3094943c7ca9ed | Q2 2026 earnings release (management, non-GAAP) |
| EX-99.1_2026-10-28_ex991-q32026.htm.jsonl | d176e2b2337e8c9ee765792690a4c9894f8e78c9eadadca91a11afce842a8bb9 | Q3 2026 earnings release (management, non-GAAP) |
| context | ce3ba040ad702f7a097a4705cf09e05a5541c48113a20eaf4b83ee334242bc43 | User run settings; not issuer evidence |

Supplied handoffs (audited):

| Module | sha256 | Status |
| --- | --- | --- |
| CP-0 | f3a9713066d902ea831e33ca5e21c7518220ff0fc6d8658f54808a4e8892a5bd | Accepted |
| CP-1 | 6416762ec0c950756779b461584b370e27dfe8cc5ec45b3b126353256df99610 | Accepted |
| CP-1A | 44d95c2186bb66af7e9424745c7b2701139cffc88c48dc61707f41e82211ccb3 | Accepted |
| CP-2 | 20c78a1ee985415cd9c49fcd5e8d2b2805d85b6892eb2114ceb6f78d5670f747 | Accepted |

Method of the check: for each cited page, the printed figures and phrases were searched in the page text (150 figures or phrases on 51 cited pages), and every derived number was recomputed from its inputs. One citation was off by one chunk in a search string (accrued interest sits on page:26, which CP-1 cites correctly). No audited figure failed to match its cited page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The figures and claims in the earlier analyses trace to the filings and releases with no critical defect. Committee use is restricted until debt documents, the covenant calculation and fourth quarter 2025 adjusted EBITDA are obtained. | Medium | Ranking, covenant and legal statements rest on the issuer's own summaries because no executed debt document is supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Figures sampled against the filings and releases matched, including derived EBITDA, leverage ratios, liquidity and maturity sums. | Core leverage, liquidity and maturity conclusions rest on printed figures and shown calculations. | High |
| Leverage and cover ratios use an EBITDA built from the statements, not the company's adjusted measure or the covenant measure. | Ratios support trend analysis but cannot be compared with covenant tests or adjusted leverage. | High |
| Ranking, sweep, change of control and covenant perimeter statements come from the issuer's summaries of its debt documents. | Creditor rights conclusions need legal review before reliance. | High |
| The credit synthesis took parent cash flow figures directly from the releases instead of from the earlier analyses. | The figures are correct, but their lineage should be recorded upstream. | High |
| Two source differences remain unreconciled: interest charged against premium and the current portion of debt. | The effects are small and do not change conclusions. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 3 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of executed debt documents, which matters because ranking, sweep, covenant-perimeter and revolver-maturity statements rest on the issuer's own summaries and implies restricted committee use for creditor-rights conclusions. No audited figure failed to match its cited page, and no defect changes a credit conclusion.

### Traceability summary

| Item | Result |
| --- | --- |
| Handoffs audited | Four, all accepted |
| Findings | 0 Critical, 4 Material, 9 Minor |
| Top 5 drivers by lineage | 1 directly sourced, 3 calculated, 1 analyst inference |
| Clearance | Pass with Remediation; committee use restricted |
| Confidence score | Not computed: the scoring script and its specification are not supplied in this transport; analyst band Medium |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_bhc-20251231.htm.jsonl | High: filed, audited | FY2025 | Bausch Health Companies Inc., consolidated incl. Bausch + Lomb | Statements, debt note, interest paid, lease note, customers, dividends | Text extraction; exhibits listed, not included | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_bhc-20260331.htm.jsonl | Medium: filed, unaudited | Q1 2026 | Same, consolidated | Statements, debt table, availability, perimeter cash split | Text extraction | CP-1 |
| S3 | 10-Q_2026-06-30_bhc-20260630.htm.jsonl | Medium: filed, unaudited | Q2 2026 | Same, consolidated | Statements, debt table, availability, perimeter cash split | Text extraction | CP-1 |
| S4 | 10-Q_2026-09-30_bhc-20260930.htm.jsonl | Medium: filed, unaudited | Q3 2026 | Same, consolidated | Statements, financing note, covenants, maturities, legal, subsequent events | Text extraction; subsequent events to October 29, 2026 | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-29_ex991-q1x2026.htm.jsonl | Medium: management release, unaudited | Q1 2026 | Bausch Health, Bausch + Lomb and Bausch Health (excl. B+L) | EBITDA and adjusted cash flow reconciliations | Non-GAAP; management definitions | CP-1, CP-2 |
| S6 | EX-99.1_2026-07-29_ex991-q22026.htm.jsonl | Medium: management release, unaudited | Q2 2026 | Same | Same | Non-GAAP | CP-1, CP-2 |
| S7 | EX-99.1_2026-10-28_ex991-q32026.htm.jsonl | Medium: management release, unaudited | Q3 2026 and nine months | Same | Adjusted EBITDA, segments, guidance | Non-GAAP; guidance is a forecast | CP-1, CP-1A, CP-2 |
| S8 | context | Not issuer evidence | Run settings 2026-11-05 | Bausch Health Companies Inc. | As-of date, currency, periods | Blank fields are not zero | All |

Module Status: Ready with Limitations. Traceability Scope: Top 5. Entity key: issuer_id `bhc` available.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Salix and Xifaxan concentration with a 2027 price reset and expected 2028 generics | CP-1A, CP-2 | Salix segment profit 1,789 of 3,779 and Xifaxan about 85% of Salix; negotiated price effective January 1, 2027; generics expected in 2028 | A price reset and volume loss hit the main profit source before 2028 maturities | Drives refinancing capacity and monitoring posture | S4 page:75, page:96, page:98, page:123 | Effect on revenue and profit is not quantified by the issuer |
| 2 | Leverage 5.15x gross and 4.51x net, cash interest cover 1.81x | CP-1, CP-2 | Principal debt 20,168; cash 2,485; LTM derived EBITDA before goodwill impairments 3,918; FY2025 interest paid 1,810 | Defines debt service tolerance | Leverage tolerance and default risk | S1 page:219 to page:221, page:319; S4 page:6, page:27; S7 page:24 | Derived EBITDA is not the covenant or adjusted measure |
| 3 | 2028 to 2031 maturities of 13,452 | CP-1, CP-2 | Maturity table 3,766; 1,667; 4,123; 3,896 | Concentrates refinancing risk | Refinancing and liquidity | S4 page:42, page:127 | Revolver trigger and covenant terms depend on unsupplied agreements |
| 4 | Bausch + Lomb shares pledged to the 2025 first-lien debt; other creditors structurally behind | CP-1A, CP-2 | 211,963,893 shares pledged; Existing Senior Secured Notes structurally subordinated; Bausch + Lomb outside the covenant calculation | Sets the order in which Bausch + Lomb value reaches creditors | Loss given default and creditor control | S4 page:31, page:37, page:39, page:40 | Issuer summaries only; executed documents not supplied |
| 5 | Liquidity of 2,485 cash plus 1,135 undrawn revolvers, parent 2,442, falling to about 1,799 pro forma after the notes redemption | CP-1, CP-2 | Balance sheet cash, revolver commitments less letters of credit, perimeter cash split, announced 643 redemption | Funds 2027 and 2028 repayments | Liquidity runway | S4 page:5, page:32, page:36, page:76, page:127 | Pro forma excludes premium, interest and cash generation after September 30, 2026 |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Refinancing capacity depends on Xifaxan cash flow surviving the reset | CP-2 | Dates and shares printed; effect inferred | Yes | Medium | Analyst Inference | Supported by cited facts; effect unquantified | Medium | Committee-Ready with disclosure |
| Debt to LTM derived EBITDA 5.15x gross, 4.51x net | CP-1, CP-2 | S4 page:27 debt 20,168, S4 page:5 cash 2,485, LTM EBITDA built from S1 page:219, S4 page:6, S4 page:7 | Yes | High | Calculated | Verified by recomputation | High | Committee-Ready |
| 2028 to 2031 maturities total 13,452 | CP-1, CP-2 | S4 page:42 maturity table | Yes | High | Calculated | Verified: 3,766 + 1,667 + 4,123 + 3,896 | High | Committee-Ready |
| First-lien claims at 126NumberCo hold the pledged shares; other notes rank structurally behind | CP-1A, CP-2 | S4 page:31, page:37, page:39: "structurally subordinated to" | Yes | Medium | Directly Sourced | Issuer description of documents; legal review dependency | Medium | Remediation Needed |
| Cash 2,485 plus undrawn 1,135 consolidated; parent 2,442 | CP-1, CP-2 | S4 page:5, page:32, page:36, page:127 | Yes | High | Calculated | Verified: 1,973 + 469 and 2,485 + 1,135 | High | Committee-Ready |

#### T5B.4 Source lineage

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 20,168 and 20,232 | source-text | 10-Q Q3 2026 | S4 | page:27 | CP-1 balance sheet and debt position | Sourced | High | Printed total |
| Debt maturities 15; 701; 3,766; 1,667; 4,123; 3,896; 6,000 | source-text | 10-Q Q3 2026 | S4 | page:42 | CP-1 chart data: debt maturities | Sourced | High | Sums to 20,168 |
| Parent debt 15,103 and Bausch + Lomb debt 5,065 | source-text | 10-Q Q3 2026 | S4 | page:127 | CP-1 net debt by perimeter | Sourced | High | Sum 20,168 |
| Cash and cash equivalents 2,485; restricted cash 3 | source-text | 10-Q Q3 2026 | S4 | page:5 | CP-1 liquidity | Sourced | High | Balance sheet |
| Revenues 8,317 and 7,470; operating income 773 and 1,339 | source-text | 10-Q Q3 2026 | S4 | page:6 | CP-1 financials | Sourced | High | Nine months |
| FY2025 revenues 10,266; operating income 1,813; net income 120 | source-text | 10-K | S1 | page:219 | CP-1 financials | Sourced | High | Audited |
| Depreciation and amortization 1,208 (FY2025), 860 and 918 (nine months) | source-text | 10-K; 10-Q Q3 2026 | S1; S4 | page:220; page:7 | CP-1 derived EBITDA | Sourced | High | Cash flow statement lines |
| EBITDA 1,613, 2,397 and Q3 1,266 | source-text | Q3 release | S7 | page:24 | CP-1 derived EBITDA check | Sourced | Medium | Management non-GAAP, equals derived values |
| Interest paid 1,810 including 276 charged to premium | source-text | 10-K | S1 | page:319; page:320 | CP-1 interest cover | Sourced | High | FY2025 only |
| 2030 Revolving Credit Facility: no borrowings, 31 letters of credit | source-text | 10-Q Q3 2026 | S4 | page:32 | CP-1 liquidity | Sourced | High | Commitment 500 at page:29 |
| B+L 2030 revolver: 100 drawn, 34 letters of credit, 666 available | source-text | 10-Q Q3 2026 | S4 | page:36 | CP-1 liquidity | Sourced | High | Commitment 800 at page:35 |
| Revolver covenants 4.25:1.00, 5.75:1.00, minimum liquidity 400 | source-text | 10-Q Q3 2026 | S4 | page:34 | CP-1 covenants | Sourced | Medium | Issuer summary; step-up date not stated |
| Ratings Moody's Caa2, S&P B-, Fitch B | source-text | 10-Q Q3 2026 | S4 | page:131 | CP-1, CP-2 | Sourced | High | As of October 28, 2026 |
| Salix 2,228 revenue and 1,789 segment profit; total segment profit 3,779 | source-text | 10-Q Q3 2026 | S4 | page:75 | CP-1A operating model | Sourced | High | Nine months |
| Salix growth price 504, volumes (173) | source-text | 10-Q Q3 2026 | S4 | page:123 | CP-1A operating model | Sourced | High | Nine months |
| Xifaxan negotiated price effective January 1, 2027; generics expected 2028 | source-text | 10-Q Q3 2026 | S4 | page:96; page:98 | CP-1A, CP-2 | Sourced | High | Effect unquantified |
| Salix goodwill impairment 1,426 measured January 22, 2026 | source-text | 10-Q Q3 2026 | S4 | page:26 | CP-1A, CP-2 | Sourced | High | After failed Phase 3 trials |
| Bausch + Lomb holding 310,449,643 shares, about 87%; 126NumberCo 211,963,893 shares | source-text | 10-Q Q3 2026 | S4 | page:9; page:30 | CP-1A profile | Sourced | High | Remaining shares' holder not stated |
| Existing Senior Secured Notes structurally subordinated | source-text | 10-Q Q3 2026 | S4 | page:39 | CP-1A structure | Sourced | Medium | Issuer summary |
| Sweep of Bausch + Lomb share collateral proceeds, pro rata | source-text | 10-Q Q3 2026 | S4 | page:33; page:38 | CP-1A structure | Sourced | Medium | Issuer summary; exceptions apply to other asset sales |
| Redemption of 643 of 8.500% notes scheduled November 30, 2026 | source-text | 10-Q Q3 2026 | S4 | page:76 | CP-1, CP-1A, CP-2 | Sourced | High | Subsequent event |
| Customers Cencora 18%, McKesson 16%, Cardinal 14%; U.S. about 60% | source-text | 10-K | S1 | page:29 | CP-1A operating model | Sourced | High | FY2025 |
| No dividends in 2025, 2024 or 2023 | source-text | 10-K | S1 | page:127 | CP-1A governance | Sourced | High | |
| Adjusted cash flows from operations for Bausch Health (excl. B+L) 319; 471; 539 and guidance 1.600 to 1.675 billion | source-text | Q1, Q2, Q3 releases | S5; S6; S7 | page:1; page:1; page:1, page:27; page:4 | CP-2 calculations | Sourced | Medium | Not carried in CP-1 or CP-1A |
| Interest charged against premium 158 (filing) and 144 (release) | source-text | 10-Q Q3 2026; Q3 release | S4; S7 | page:126; page:27 | CP-1 conflicts | Conflicting | Medium | Logged, not reconciled |
| Current portion of debt 866 | source-text | 10-Q Q3 2026 | S4 | page:5 | CP-1 balance sheet | Sourced | High | Not reconciled to 716 principal due |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EBITDA (derived), nine months 2026 | CP-1 | Net loss (725); tax 316; net interest 1,196 less 34; D&A 860 | (725) + 316 + 1,162 + 860 = 1,613 | Calculated | Verified; equals release 1,613 | High | Leverage, cover | S4 page:6, page:7; S7 page:24 |
| EBITDA (derived), FY2025 | CP-1 | Net income 120; tax 247; interest 1,604 less 48; D&A 1,208 | 120 + 247 + 1,556 + 1,208 = 3,131 | Calculated | Verified | High | Leverage, cover | S1 page:219, page:220 |
| LTM derived EBITDA before goodwill impairments, Q3 2026 | CP-1, CP-2 | FY2025 3,131; nine months 2026 1,613; nine months 2025 2,397; goodwill impairments 145 and 1,426 | 3,131 + 1,613 − 2,397 = 2,347; plus 1,571 = 3,918 | Calculated | Verified | High | Leverage | As above; S7 page:24 |
| LTM derived EBITDA before goodwill impairments, Q1 and Q2 2026 | CP-1 | Q1: (667) and 577; six months: 347 and 1,476 | 3,131 − 667 − 577 + 1,571 = 3,458; 3,131 + 347 − 1,476 + 1,571 = 3,573 | Calculated | Verified; equals release EBITDA (S5 page:23; S6 page:25) | High | Leverage trend | S5, S6 |
| Gross and net leverage | CP-1, CP-2 | Debt 20,232; 20,212; 20,239; 20,168. Cash 1,309; 1,299; 1,825; 2,485 | Debt / LTM EBITDA: 6.18x; 5.84x; 5.66x; 5.15x. (Debt − cash) / EBITDA: 5.78x; 5.47x; 5.15x; 4.51x | Calculated | Verified | High | Leverage | S1 page:269; S2 page:26; S3 page:27; S4 page:27 |
| FY2025 cash interest cover | CP-1, CP-2 | EBITDA before goodwill impairments 3,276; interest paid 1,810 | 3,276 / 1,810 = 1.81x | Calculated | Verified | High | Coverage | S1 page:319 |
| Parent net debt by quarter | CP-1, CP-2 | Parent debt less parent cash incl. restricted | 15,126 − 928 = 14,198; 15,103 − 1,973 = 13,130; reduction 13,651 − 13,130 = 521 | Calculated | Verified | High | Deleveraging | S1 page:173; S3 page:123; S4 page:127 |
| Undrawn committed facilities | CP-1 | Commitments 500 and 800; borrowings; letters of credit | 500 − 0 − 31 = 469; 800 − 100 − 34 = 666; total 1,135 | Calculated | Verified; equals printed availability | High | Liquidity | S4 page:32, page:35, page:36 |
| Maturities 2028 to 2031 | CP-2 | 3,766; 1,667; 4,123; 3,896; parent 2,326; 1,639; 3,995; 462 | 13,452; parent 8,422; Bausch + Lomb 5,030 | Calculated | Verified | High | Refinancing | S4 page:42, page:127 |
| Pro forma parent liquidity | CP-2 | Parent cash 1,973; undrawn 469; redemption 643 | 1,973 + 469 − 643 = 1,799; 1,799 / 2,326 = 0.77x | Calculated | Verified arithmetic; excludes premium, interest, cash generation | Medium | Liquidity, refinancing | S4 page:76, page:127 |
| Salix shares of revenue and segment profit | CP-1A, CP-2 | 2,228 / 8,317; 1,789 / 3,779 | 26.8% and 47.3% | Calculated | Verified | High | Business risk | S4 page:75 |
| Parent adjusted cash flows from operations, nine months 2026 | CP-2 | 319; 471; 539 | 1,329; implied fourth quarter 271 to 346 against guidance 1,600 to 1,675 | Calculated | Verified to releases; not in upstream handoffs (CP5-001) | Medium | Cash generation | S5 page:1; S6 page:1; S7 page:1, page:4 |
| Illustrative parent leverage | CP-1 | 1,022 × 4 = 4,088; guidance midpoint 3,250 | 15,103 / 4,088 = 3.69x; 13,130 / 4,088 = 3.21x; 15,103 / 3,250 = 4.65x; 13,130 / 3,250 = 4.04x | Calculated | Verified; labelled illustrative, not LTM | Medium | Leverage | S7 page:28, page:4 |
| Reduction of principal in the December 2025 exchange | CP-1A | 797 + 886 = 1,683 exchanged for 1,600 | 1,683 − 1,600 = 83 | Calculated | Verified; equals printed 83 | High | Maturity extension | S4 page:83 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Parent cash generation 1,329 and guidance 1,600 to 1,675 (CP-2) | Figures read from the releases, not carried by upstream handoffs (CP5-001) | Directly Sourced | CP-2 states evidence is upstream only; a lineage rule is breached though the figures match | Record the figures upstream or label as direct reads | CP-2 Calculations |
| Material | Ranking, sweep, covenant perimeter and revolver trigger (CP-1A, CP-2) | Issuer summaries only; executed documents absent (CP5-003, CP5-004) | Directly Sourced | Creditor rights and loss given default depend on the clauses | Obtain executed documents and legal review | CP-1A structure table; CP-2 findings 4 and 7 |
| Material | Leverage and cover ratios (CP-1, CP-2) | Derived EBITDA basis differs from covenant and adjusted measures (CP5-002) | Calculated | Ratios may not be comparable with covenant tests or adjusted leverage elsewhere | Keep the basis label in every use; add adjusted LTM when available | CP-1 charts; CP-2 credit view |
| Minor | Holding structure history (CP-1A) | "Moved" wording partly inferred (CP5-005) | Weak Lineage | Dates the structure earlier than the filing states | Reword to the documented facts | CP-1A business and transaction view |
| Minor | Pending transactions (CP-1A) | "No acquisition pending at the issuer" omits a consolidated subsidiary deal (CP5-006) | Weak Lineage | Understates use of cash in the fourth quarter | Reword | CP-1A transaction summary |
| Minor | Premium accounting figure (CP-1, CP-2) | Conflict of 158 and 144 not reconciled (CP5-009) | Conflicting | Cash flow reading differs by 14 | Treat the filing as controlling | CP-1 conflicts table |
| Minor | Current debt reading (CP-1) | 866 against 716 not reconciled (CP5-008) | Weak Lineage | Balance sheet current portion could be read as near-term repayment | Read the debt note composition | CP-1 gaps |
| Minor | Covenant ratio and headroom | Not printed in any source; correctly stated as Not calculable | Insufficient Information | No headroom claim can be traced | Obtain compliance certificate | CP-1, CP-2 gaps |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filed documents cover FY2025 and three 2026 quarters; no executed debt documents or Bausch + Lomb filings | Legal and perimeter claims cannot be tested at clause level | Creditor-rights conclusions need legal review | Obtain the 2025 Credit Agreement, indentures and Bausch + Lomb Form 10-Q |
| Citation completeness | Ready with Remediation | Every audited figure matched its cited page; CP5-001 and two wording items found | A figure without upstream lineage cannot be traced by the next consumer | Low effect on conclusions | Record releases figures upstream; reword two sentences |
| Calculation traceability | Committee-Ready | All derived figures recomputed with inputs shown; releases agree with derived EBITDA | Inputs and formulas visible | Ratios can be rebuilt | None beyond keeping the basis label |
| Assumption transparency | Ready with Remediation | Derived EBITDA basis and pro forma exclusions are disclosed but not covenant measures | Readers may compare ratios across definitions | Possible misreading of headroom | Label every ratio and add adjusted LTM when supplied |
| Markdown and export artifact integrity | Ready with Remediation | Six required headings in all four handoffs; selector sections present; no YAML front matter in this transport | Downstream tools that expect the full envelope may not find fields | Minor | Map fields at export |

Overall auditability: Ready with Remediation (lowest of the five dimensions).

### Research integrity audit

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | handoff sha256 f3a97130…, run bhc-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six required headings present; no YAML envelope | Accepted by CP-OS | One wording item on note issuers corrected by CP-1 |
| CP-1 | handoff sha256 6416762e…, same run | Financial base, FY2025 to Q3 2026 | High | Six headings and five selectors present | Accepted by CP-OS | Derived EBITDA basis |
| CP-1A | handoff sha256 44d95c21…, same run | Business, ownership, transaction, governance | High | Six headings and three selectors present | Accepted by CP-OS | Two wording items |
| CP-2 | handoff sha256 20c78a1e…, same run | Credit synthesis | High | Six headings and two selectors present | Accepted by CP-OS | Direct release reads |

Module Status: Ready with Limitations (all four handoffs present; executed legal documents absent).

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 | Parent adjusted cash flows 319, 471 and 539 and guidance 1,600 to 1,675 in Calculations | Partially Supported | CP5-001. The figures match the Q1, Q2 and Q3 releases and the Q3 release outlook, but CP-2 is defined as upstream-only and neither CP-1 nor CP-1A carries them; the guidance column attribution to Bausch Health (excl. B+L) is read from release text. | Carry the figures in an upstream handoff or label them as direct reads with the release locator | Restricts Committee Use |
| MINOR | CP-1A | "Since 2022 the company has moved Bausch + Lomb shares into a holding company" | Partially Supported | CP5-005. The filing documents the November 29, 2022 designation of 126NumberCo and a transfer of 26,495,472 shares in December 2025, not an earlier movement of shares. | Reword to the documented facts | Monitoring Follow-Up |
| MINOR | CP-1A | "No acquisition or leveraged buyout is pending at the issuer" | Partially Supported | CP5-006. Bausch + Lomb, a consolidated subsidiary, agreed on October 8, 2026 to an acquisition for about 85 upfront, which CP-1A reports later in the same section. | Reword to "at the parent" or cite the subsidiary deal | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | CP5-002. Leverage and cover use LTM derived EBITDA before goodwill impairments (3,918; FY2025 3,276). | Not the company's adjusted EBITDA or the covenant EBITDA; includes the noncontrolling interest share of Bausch + Lomb and does not add back asset impairments; adjusted LTM is not calculable without fourth quarter 2025. | None; basis disclosed in both modules | Keep the basis label wherever a ratio appears; add adjusted LTM when supplied | Restricts Committee Use |
| MINOR | CP-1, CP-2 | CP5-007. Net debt uses cash and equivalents consolidated, perimeter tables use cash including restricted cash. | Two cash definitions in one handoff set; restricted cash is 3 consolidated and not split by perimeter | None | Label the cash definition in every table | Monitoring Follow-Up |
| MINOR | CP-1 | CP5-008. Current portion of debt 866 against 716 of principal due by end of 2027. | Difference of 150 is not reconciled; a plausible cause is premium reduction through scheduled interest payments classified as current (premium reduction of 42 in the remainder of 2026 is printed at S4 page:130), which is not verified. | Balance sheet against maturity table | Read the current portion composition in the debt note | Monitoring Follow-Up |
| MINOR | CP-1, CP-1A, CP-2 | CP5-009. Interest charged against premium for nine months 2026. | 158 in the filing against 144 in the release; the effect on the parent adjusted cash flows used by CP-2 is up to 14 on 1,329, about 1.1% (14 / 1,329 = 1.05%) | Q3 10-Q page:126 against Q3 release page:27 | Treat the filing as controlling; seek the issuer's reconciliation | Requires Source Reconciliation |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-2 | CP5-003. Structural subordination, pari passu and first-lien ranking, pro rata sweep of Bausch + Lomb share proceeds, 101% change of control, and exclusion of Bausch + Lomb from the covenant calculation; the governance reading of the 2022 and December 2025 exchanges as mixed. | 2025 Credit Agreement, indentures for the 2032, Existing Senior Secured and Senior Unsecured Notes, collateral and intercreditor documents, exchange offer documents | Only the issuer's note summaries are in the pack; participation terms and designation capacity are absent | Obtain executed documents and confirm each statement at clause level | Required before reliance on creditor-rights conclusions |
| MATERIAL | CP-1, CP-2 | CP5-004. The 2030 Revolving Credit Facility may mature early under a 91-day trigger linked to 2028 maturities of 2,326 at the parent. | 2025 Credit Agreement definitions of the trigger and of aggregate principal | The application of the aggregate test to the 2028 notes is an analyst inference, hedged in both modules | Confirm the test from the agreement | Required before using the revolver as a source of liquidity beyond 2027 |

Covenant headroom (the reported ratio and the Covenant Step Up Date) is not a finding here: CP-1 and CP-2 state both as Not supplied and make no capacity claim, so the item is carried in the gaps ledger.

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | All four | No price, spread, yield, comparable or relative-value claim is made; agency ratings are quoted from the Q3 10-Q (S4 page:131) | None required for the claims made | None | None | None; any relative-value use belongs to a later module and needs market data |

This row records the absence of a finding and is not counted in the issue log.

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A | CP5-010. CP-0 says Bausch + Lomb is "issuer of the B+L Senior Secured Notes"; the Q3 10-Q (page:35) shows Bausch + Lomb issued the 8.375% notes due October 2028 and its subsidiaries issued the floating rate notes due January 2031. | CP-1 and CP-1A correct it in text; CP-0 cannot be edited | Cite the correction wherever CP-0 is quoted | Low; no figure changes |

Cross-checked and consistent across the four modules: principal debt 20,168 and 20,232; cash 2,485; undrawn revolvers 1,135; maturities by year; 5.15x and 4.51x; 13,452; parent net debt 13,130; ratings; the 643 redemption; and the nine months 2026 interest-against-premium conflict, logged in CP-1, CP-1A and CP-2.

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Promotional or Non-Credit Language | CP5-011. Labels such as "Weak credit ratings" and "Highly leveraged" and the heading "Diversification outside Salix" are adjectives without an attached figure at the point of use. | Replace with the figure and its implication | Low |
| MINOR | CP-1, CP-1A, CP-2 | Duplicative / Immaterial Content | CP5-012. Liquidity, maturity and leverage figures are repeated across the four handoffs and in each reader summary. | Keep the repetition only where the handoff is read alone | Low |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | YAML front matter and CP-5 canonical headings | CP5-013. The handoffs use the CP-OS transport (six H2 headings, no YAML envelope fields such as confidence_score or committee_status). This follows the run instructions, but the envelope fields cannot be validated. | Map the fields at export | Low |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-2 | Evidence Trace Defect | Parent adjusted cash flows and guidance taken from releases, not carried upstream | Carry upstream or label as direct reads | Restricts Committee Use | Open |
| CP5-002 | MATERIAL | CP-1, CP-2 | Formula / Definition Drift | Ratios use a derived EBITDA, not covenant or adjusted EBITDA | Keep basis label; add adjusted LTM when supplied | Restricts Committee Use | Open |
| CP5-003 | MATERIAL | CP-1A, CP-2 | Legal Support Gap | Ranking, sweep, change of control and perimeter statements rest on issuer summaries | Obtain executed documents; legal review | Requires Legal Review | Open |
| CP5-004 | MATERIAL | CP-1, CP-2 | Covenant / Basket Overreach | Revolver early-maturity trigger applied to 2028 maturities by inference | Confirm in the agreement | Requires Legal Review | Open |
| CP5-005 | MINOR | CP-1A | Partially Supported Claim | "Moved shares into a holding company since 2022" partly inferred | Reword | Monitoring Follow-Up | Open |
| CP5-006 | MINOR | CP-1A | Partially Supported Claim | "No acquisition pending at the issuer" omits subsidiary deal | Reword | Formatting / Hygiene Only | Open |
| CP5-007 | MINOR | CP-1, CP-2 | Formula / Definition Drift | Two cash definitions across tables | Label the definition | Monitoring Follow-Up | Open |
| CP5-008 | MINOR | CP-1 | Citation Gap | Current debt 866 against 716 not reconciled | Read the debt note | Monitoring Follow-Up | Open |
| CP5-009 | MINOR | CP-1, CP-1A, CP-2 | Conflicting Evidence | Premium interest 158 against 144, logged | Treat filing as controlling | Requires Source Reconciliation | Open |
| CP5-010 | MINOR | CP-0 | Version Conflict | Wording on Bausch + Lomb note issuers corrected downstream | Cite the correction | Monitoring Follow-Up | Open |
| CP5-011 | MINOR | CP-2 | Promotional or Non-Credit Language | Adjectives without attached figures | Replace with figures | Formatting / Hygiene Only | Open |
| CP5-012 | MINOR | CP-1, CP-1A, CP-2 | Duplicative / Immaterial Content | Repeated liquidity, maturity and leverage figures | Trim | Formatting / Hygiene Only | Open |
| CP5-013 | MINOR | CP-0, CP-1, CP-1A, CP-2 | canonical Markdown Handoff Integrity Defect | Transport has no YAML envelope fields | Map at export | Formatting / Hygiene Only | Open |

### Remediation priority map

- Must-fix before committee: CP5-003 (obtain executed debt documents and complete legal review), CP5-004 (confirm the revolver trigger), CP5-001 (record the release figures upstream), CP5-002 (carry the EBITDA basis label with every ratio).
- Must-fix before the handoffs are consumed downstream: CP5-013 (map envelope fields at export), CP5-009 (treat the filing figure as controlling).
- Monitoring follow-up: CP5-005, CP5-007, CP5-008, CP5-010.
- Formatting and hygiene: CP5-006, CP5-011, CP5-012.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 4. Minor Issues: 9. Committee Use: Restricted.

No audited figure failed to match its cited page and no finding changes a credit conclusion. The four Material findings concern the unsupplied legal documents, the basis of the leverage measure and one lineage rule in the credit synthesis, so committee use is restricted to conclusions that do not depend on creditor-rights, covenant headroom or adjusted leverage. qa_status: Restricted.

## Calculations

Independent recomputation by this module, from printed inputs (USD millions). Each result matches the audited handoff.

- LTM derived EBITDA at September 30, 2026: FY2025 3,131 + nine months 2026 1,613 − nine months 2025 2,397 = 2,347; goodwill impairments 145 + 1,426 − 0 = 1,571; 2,347 + 1,571 = 3,918. At March 31, 2026: 3,131 + (667) − 577 = 1,887; 1,887 + 1,571 = 3,458. At June 30, 2026: 3,131 + 347 − 1,476 = 2,002; 2,002 + 1,571 = 3,573.
- Leverage at September 30, 2026: 20,168 / 3,918 = 5.15x; (20,168 − 2,485) / 3,918 = 17,683 / 3,918 = 4.51x. At FY2025: 20,232 / 3,276 = 6.18x; 18,923 / 3,276 = 5.78x.
- FY2025 cash interest cover: 3,276 / 1,810 = 1.81x.
- Maturities: 15 + 701 + 3,766 + 1,667 + 4,123 + 3,896 + 6,000 = 20,168. 2028 to 2031: 3,766 + 1,667 + 4,123 + 3,896 = 13,452.
- Liquidity: 2,485 + 1,135 = 3,620 consolidated; 1,973 + 469 = 2,442 parent; 2,442 − 643 = 1,799 pro forma.
- Share of revenue and segment profit: 2,228 / 8,317 = 26.8%; 1,789 / 3,779 = 47.3%.
- Premium interest conflict: 111 + 47 = 158 in the filing against 144 in the release; difference 14; 14 / 1,329 = 1.05% of the parent adjusted cash flows used in CP-2 (319 + 471 + 539 = 1,329).
- Current debt difference: 866 − (15 + 701) = 150.
- Confidence Score: Not calculable: the scoring script and specification are not supplied in this transport.

## Gaps

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed debt documents not supplied | 2025 Credit Agreement, indentures, intercreditor, collateral and exchange offer documents | Ranking, sweep, change of control, designation capacity and covenant terms cannot be tested; loss given default depends on them | Structure and governance findings in CP-1A and CP-2 | High impact | Exhibit list in the 10-K (S1 page:199 to page:211) |
| CP-5-GAP-002 | Reported covenant ratio, Covenant Step Up Date and liquidity covenant definition not supplied | Compliance certificate and credit agreement definitions | Headroom cannot be assessed; early-maturity trigger untested | Liquidity and refinancing findings | High impact | Issuer compliance calculation |
| CP-5-GAP-003 | Fourth quarter 2025 adjusted EBITDA not supplied | Q4 2025 earnings release | No adjusted LTM leverage; ratios use a derived measure | Leverage findings | High impact | Q4 2025 release |
| CP-5-GAP-004 | Interim cash interest paid not supplied | Cash flow supplemental disclosure for 2026 periods | Interim cash cover cannot be shown | Interest burden finding | Medium impact | Q4 2025 and later releases or supplemental note |
| CP-5-GAP-005 | Bausch + Lomb standalone filings and covenant levels not supplied | Bausch + Lomb Form 10-Q and credit agreement | Standalone credit and perimeter tests cannot be checked | Structure finding | Medium impact | Bausch + Lomb filings |
| CP-5-GAP-006 | Quantified effect of the 2027 Xifaxan price and generic entry not supplied | Issuer disclosure or management detail | The largest business risk cannot be sized | Concentration finding | High impact | Management detail; quarterly filings |
| CP-5-GAP-007 | Interest-against-premium difference and current debt composition not reconciled | Issuer reconciliation; debt note detail | Small effects on cash flow and near-term reading | Cash flow and liquidity reading | Low impact | Q3 10-Q debt note; issuer |
| CP-5-GAP-008 | Events after October 29, 2026 to 2026-11-05 not supplied | Later 8-Ks, litigation and tax outcomes | Outcomes such as the Luxembourg appeal judgment may change risk | Legal and tax findings | Medium impact | Later filings |
| CP-5-GAP-009 | Text extraction only; no check against filed HTML or XBRL | Original filings | Table layout and footnote fidelity not checked | All figures | Low impact | Original HTML or XBRL |

## Next module

CP-5 is the last module in the selected minimum set. Report assembly follows. The reader should carry forward: committee use restricted pending executed debt documents, the covenant calculation and fourth quarter 2025 adjusted EBITDA; the derived EBITDA basis label on every ratio; and the correction to the CP-0 wording on the Bausch + Lomb note issuers.
