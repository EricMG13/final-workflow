# CP-5 evidence trace and research integrity QA: CHS INC (chscp)

## Request

CHS INC (issuer id chscp), the member-owned agricultural cooperative CHS Inc., as of 2026-11-05 on the credit_snapshot pathway. This module traces the claims and figures of the four earlier handoffs back to the pinned sources, re-computes the derived figures, audits consistency across the handoffs and grades research integrity. It changes no credit conclusion; where it finds a defect it logs it and does not repair the earlier handoff, which cannot be edited. Currency is USD; no source outside the pinned filings and releases was used.

## Sources

### Issuer sources relied on

| Source name | sha256 | Used for |
| --- | --- | --- |
| 10-K_2026-08-31_chscp-20260831.htm.jsonl | 7af90f68bff1cc427159bcc12ffc87c427ce829f2621b0c4238922f45880492c | Primary check of statements, notes, governance and MD&A figures |
| 10-Q_2025-11-30_chscp-20251130.htm.jsonl | 3b343d46b4f667e29be99b08f7d799dc25471f06dbcbf91d62c596b40053bc50 | Fiscal Q1 2026 statements and balance sheet |
| 10-Q_2026-02-28_chscp-20260228.htm.jsonl | 335ab8ab1983479e957ab5bcc688bac42f2a8847cb6800ad1d72a83671457084 | Fiscal Q2 2026 statements and balance sheet |
| 10-Q_2026-05-31_chscp-20260531.htm.jsonl | d9720f91bf0c93fa122637a031df8f3b728863173bc1b8717d0a6e377caf2082 | Fiscal Q3 2026 statements, balance sheet and facility detail |
| EX-99.1_2026-04-08_a2qfy26earningrelease.htm.jsonl | 33496a1570da087ac1976522b03589f92cee4a9a2670952160166094e3791034 | Cross-check of quarter and six-month earnings |
| EX-99.1_2026-07-08_a3qfy26earningrelease.htm.jsonl | 9732954cd83cfd2faab08d34c8a937435e86ab588c7e99ee653b9179d1961e0c | Cross-check of quarter and nine-month earnings |
| EX-99.1_2026-11-04_a4qfy26earningrelease.htm.jsonl | cae53d4e6b095242a55a168a21c6d1a5d0c45880ba1e0b3a388701114a691f44 | Cross-check of fiscal 2026 segment earnings and owner distribution plan |

Context file sha256 7441cd131643680d7cdd1713c448cca9698ae339b2ccfb6c0e8da281781f9451 supplies dates and currency only and is not issuer evidence.

### Supplied handoffs

| Module | sha256 | How used |
| --- | --- | --- |
| CP-0 | c5f6c43eadd719108e1a786ea324314e25d2bbf3d44f9ea676626928c1bc9d76 | Source readiness; audited |
| CP-1 | 528858c503c0f2423d9c2d1493f07a702d9a9b2cff8b46977b62e66b20b29170 | Financial base; audited and recomputed |
| CP-1A | 2825e4537054cb6945de7e804ee96d9b9eb967fcf7fc9626b5a114375cf74b0f | Business, governance and conflicts; audited |
| CP-2 | 3e276ce59daa3b5f606c7942a230d34193f6a721affb9a622df315eac8f3e02d | Credit view; audited and recomputed |

Locators read `file page:N`, where N is the extracted page chunk, not the printed page. Lineage classes are Directly Sourced, Calculated, Assumption-Based, Analyst Inference, Weak Lineage, Untraced, Conflicting and Insufficient Information. The review opened the cited page for each figure listed in the lineage register and re-ran the arithmetic from figures read directly out of the extracted text, not from the handoffs.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported figures in the earlier handoffs were found on the pages cited and the main derived figures recompute exactly. Four minor defects were logged, one already corrected downstream. Covenant, structure and quarterly conclusions are not traceable. | Medium | Review covered the cited pages, not every page of the filings, and text extraction fidelity was not reviewed beyond number matches. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Derived EBITDA of 1,969,497, leverage of 1.27 and cash interest cover of 11.79 recompute exactly from the annual report statements. | The core leverage and coverage figures can be relied on as calculated, subject to the derived EBITDA definition. | High |
| The remark that fiscal 2026 operating cash flow was helped by working capital is wrong: working capital used 184,007. | Cash generation was achieved despite a working capital outflow; the credit view handoff already corrects the remark. | High |
| The annual report's quarterly share table shows the fourth quarter at 36% against 66% implied by the filed statements, and the conflict stays unresolved. | Quarterly phasing of the recovery is unreliable; annual figures are unaffected. | High |
| No agreement, covenant level, guarantor list or letter of credit figure is in any source. | Covenant headroom and creditor structure cannot be traced and stay restricted. | High |
| The confidence score is 51, in the Low band, from 18 material claims, 4 minor findings and a partial source gate. | Use as a draft financial view; do not rely on it for covenant or structure decisions. | Medium |

### Evidence trace view

The analysis is traceable enough for a draft financial view of CHS Inc., but not for conclusions on covenants, structure or quarterly phasing. Every reported figure checked in the earlier handoffs was found on the page cited, and the main derived figures, namely derived EBITDA, leverage, cash interest cover, free cash flow and the working capital lines, recompute exactly from the filings. The most material provenance gap is the missing legal layer: no agreement is supplied, so covenant compliance rests on a one-line management statement. The strongest contrary evidence is an annual report table of quarterly earnings shares that cannot be reconciled to the filed statements; it does not change annual figures but leaves the derived fourth quarter contested. Four minor defects were found and one was already corrected downstream. Remediation owners are the issuer, for the agreements, and the next filing, for the table.

### Traceability summary

| Measure | Result |
| --- | --- |
| Material claims traced | 18 |
| Directly Sourced / Calculated / Assumption-Based / Analyst Inference / Conflicting | 7 / 8 / 1 / 1 / 1 |
| Findings by severity | 0 critical, 0 material, 4 minor |
| Confidence score and band | 51, Low |
| QA status and committee status | Passed; Draft Only, with covenant, structure and quarterly phasing claims restricted |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2026-08-31_chscp-20260831.htm.jsonl | High: audited annual report | Fiscal 2026, with 2025 and 2024 comparatives | CHS Inc. and subsidiaries, consolidated | Statements, notes, debt, segments, governance, MD&A | No agreements; extraction is text only | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2025-11-30_chscp-20251130.htm.jsonl | High: unaudited quarterly report | Quarter ended 2025-11-30 | Same | Q1 statements, balance sheet, segment recast | Unaudited | CP-1 quarterly view and interim leverage |
| S3 | 10-Q_2026-02-28_chscp-20260228.htm.jsonl | High: unaudited quarterly report | Quarter and six months ended 2026-02-28 | Same | Q2 statements, balance sheet | Unaudited | CP-1 quarterly view and interim leverage |
| S4 | 10-Q_2026-05-31_chscp-20260531.htm.jsonl | High: unaudited quarterly report | Quarter and nine months ended 2026-05-31 | Same | Q3 statements, balance sheet, facility detail | Unaudited | CP-1, CP-1A |
| S5 | EX-99.1_2026-04-08_a2qfy26earningrelease.htm.jsonl | Medium: management release | Second quarter fiscal 2026 | Same | Segment earnings, narrative | Contains a mislabelled quarter | Cross-check |
| S6 | EX-99.1_2026-07-08_a3qfy26earningrelease.htm.jsonl | Medium: management release | Third quarter fiscal 2026 | Same | Segment earnings, narrative | Management claims | Cross-check |
| S7 | EX-99.1_2026-11-04_a4qfy26earningrelease.htm.jsonl | Medium: management release | Fiscal 2026 | Same | Segment earnings, owner distribution plan, projects | Redemption wording differs from the 10-K | CP-1, CP-1A, CP-2 |
| S8 | Context file (user settings) | Not issuer evidence | As of 2026-11-05 | Run settings only | Dates, currency, blank sponsor fields | Not evidence | Scope only |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Low year-end leverage, higher at the seasonal peak | CP-1 | Debt and cash on the balance sheet, derived EBITDA, interim balance sheets | Sets leverage tolerance and the working capital funding need | Frames debt capacity | S1 page:144, page:146, page:165; S2 page:4; S3 page:4; S4 page:4 | EBITDA derived, not reported |
| 2 | Energy drives the earnings improvement | CP-1, CP-1A | Segment tables and Renewable Fuel Standard disclosures | Earnings durability depends on spreads and regulation | Key volatility driver | S1 page:67, page:181, page:63, page:64 | Quarterly phasing contested |
| 3 | CF Nitrogen concentration | CP-1A | Equity method note, distributions and segment table | Largest single source of equity income and non-controlled cash | Concentration risk | S1 page:158, page:159, page:181 | Venture not controlled |
| 4 | Fiscal 2027 cash demand against fiscal 2026 operating cash flow | CP-2 | Capital expenditure, preferred dividends, owner returns, maturities, interest | Tests self-funding | Liquidity planning | S1 page:76, page:77, page:146, page:170 | Forward-looking management figures |
| 5 | Absent legal layer and covenant levels | CP-0, CP-1 | Debt note statement and exhibit index | Headroom and ranking cannot be tested | Limits committee use | S1 page:163, page:133, page:134 | Agreements not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt / EBITDA 1.27 and net 1.14 at fiscal 2026 | CP-1 | S1 page:144, page:146 | Yes | High | Calculated | Supported, recomputed equal | High | Traced |
| EBITDA / cash interest 11.79 | CP-1 | S1 page:146 | Yes | High | Calculated | Supported, recomputed equal | High | Traced |
| Energy improvement exceeds group improvement | CP-1 | S1 page:67 | Yes | High | Calculated | Supported, recomputed equal | High | Traced |
| Derived fourth quarter pretax 739,295 | CP-1 | S1 page:144; S4 page:5 against S1 page:60 | Yes | High | Conflicting | Arithmetic supported, contested by the 10-K quarterly share table | Low | Conflict logged, unresolved |
| Revolver 2.8 billion committed, no borrowings at 2026-08-31 | CP-1 | S1 page:163 | Yes | High | Directly Sourced | Supported; letters of credit not supplied | High | Traced |
| Undrawn revolver at 2025-08-31 of 2,620.0 | CP-1 | S1 page:163 and S4 page:12 | Yes | High | Assumption-Based | Supported if commitment unchanged | Medium | Traced with assumption |
| Debt register and maturity ladder | CP-1 | S1 page:164, page:165 | Yes | High | Directly Sourced | Supported, rows re-added equal | High | Traced |
| Covenants met, levels not printed | CP-0, CP-1 | S1 page:163, page:76 | Yes | High | Directly Sourced | Supported as a statement only | Medium | Traced |
| Refinery exemption benefit of about 205.0 million | CP-1A | S1 page:64 | Yes | High | Directly Sourced | Supported | High | Traced |
| CF Nitrogen earnings 406,334 and distributions 447.3 million | CP-1A | S1 page:158, page:159 | Yes | High | Directly Sourced | Supported | High | Traced |
| CF Nitrogen is 71% of equity income | CP-1A | S1 page:159, page:144 | Yes | High | Calculated | Supported, recomputed equal | High | Traced |
| Discretionary distributions and cash patronage cut | CP-1A | S1 page:146, page:169, page:170 | Yes | High | Directly Sourced | Supported | High | Traced |
| Related-party past due 10,260,441 | CP-1A | S1 page:124 | Yes | High | Directly Sourced | Supported | High | Traced |
| Quarter-end leverage 2.92 in February 2026 | CP-1 | S3 page:4, page:5; S2 page:4, page:5 | Yes | High | Calculated | Supported, recomputed equal | High | Traced |
| Fixed charge cover 5.87 | CP-2 | S1 page:146 | Yes | High | Calculated | Supported, recomputed equal | High | Traced |
| Fiscal 2027 identified demands 1,536.1 million | CP-2 | S1 page:76, page:77, page:170 | Yes | High | Calculated | Supported; inputs partly management forecasts | Medium | Traced |
| Working capital used 184,007 in fiscal 2026 | CP-2 | S1 page:146 | Yes | High | Calculated | Supported, recomputed equal | High | Traced |
| Overall view: solid but cyclical | CP-2 | Synthesis of rows above | Yes | Not applicable | Analyst Inference | Reasoned from supported rows | Medium | Traced to rows |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total assets 20,112,875; no common stock outstanding | /workspace/secdata/data/2026-11-05/packs/823277-chs-inc-chscp-chsco-chscn-chscm-chscl | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:144 balance sheet; page:2 cover | CP-0 source assessment | Reported | High | Matches |
| Revenues 39,231,217; income before income taxes 1,128,719; interest expense 163,633 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:144 statement of operations | CP-1 financials table | Reported | High | Matches |
| D&A 677,145; cash paid for interest 167,057; operating cash flow 1,584,009 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:146 cash flows | CP-1 financials table | Reported | High | Matches |
| Long-term debt including current portion 2,052,723; notes payable 449,002 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:165 and page:144 | CP-1 debt register | Reported | High | Matches |
| Maturities 58,562; 190,600; 150; 450,000; 200,000; thereafter 1,105,000 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:165 note 9 | CP-1 maturity chart | Reported | High | Matches; total 2,004,312 re-added equal |
| Revolver 2.8 billion expiring April 21, 2028 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:163 note 9 | CP-1 liquidity | Reported | High | Matches |
| Securitization availability 963.9 million, 175.0 million utilized; extension to August 25, 2027 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:164 note 9 | CP-1 liquidity | Reported | High | Matches |
| Second quarter pretax loss (164,977); nine months 389,424 | same | 10-Q_2026-02-28_chscp-20260228.htm; 10-Q_2026-05-31_chscp-20260531.htm | S3, S4 | page:5 statements of operations | CP-1 quarterly view | Reported | High | Matches; releases agree |
| Refinery exemption benefits about 205.0 million and 90.0 million | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:64 MD&A | CP-1A operating model | Reported | High | Matches |
| CF Nitrogen distributions 447.3, 304.4, 308.4 million; earnings attributable 406,334 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:158 and page:159 note 6 | CP-1A operating model | Reported | High | Matches |
| Quarterly share table: fourth quarter 36% and second quarter 15% for fiscal 2026 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:60 MD&A | CP-1A conflicts | Reported | High | Matches the page; conflicts with statements |
| Fiscal 2027 capital expenditures 850.8 million; interest payments 101,271; redemptions 150.0 plus 15.0 million | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:76, page:77, page:170 | CP-2 funding table | Reported and management estimate | High | Matches |
| Related-party past due 10,260,441; payoff by June 30, 2027 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:124 Item 13 | CP-1A governance | Reported | High | Matches |
| Working capital lines (150,562), (455,758), 359,133, 63,180 | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:146 cash flows | CP-2 correction | Reported | High | Matches |
| Plan to return 300 million to owners in 2027 | same | EX-99.1_2026-11-04_a4qfy26earningrelease.htm | S7 | page:1 headline | CP-1A conflict | Management claim | Medium | Matches; differs from 10-K detail |
| Operating lease liabilities 237,487; purchase obligations 7,604,191; guarantees 110.4 million | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:192, page:77, page:190 | CP-1 claims table | Reported | High | Matches |
| Voting rights arise by membership; no 5% holder of preferred | same | 10-K_2026-08-31_chscp-20260831.htm | S1 | page:91, page:123 | CP-1A governance | Reported | High | Matches |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Derived EBITDA | CP-1 C1; CP-2 | Pretax income, interest expense, D&A for three years | Pretax + interest + D&A | Recomputed: 1,969,497; 1,412,277; 1,771,742 equal | Supported | High | Basis of every ratio | S1 page:144, page:146 |
| Leverage and net leverage | CP-1 C5 | Notes payable, long-term debt, cash | Debt / EBITDA; (debt - cash) / EBITDA | Recomputed: 1.27, 2.12, 1.14, 1.88 equal | Supported | High | Leverage tolerance | S1 page:144, page:165 |
| Interest cover | CP-1 C6 | Derived EBITDA, cash paid for interest | EBITDA / cash interest | Recomputed: 11.79, 9.57, 17.62 equal | Supported | High | Debt service | S1 page:146 |
| Free cash flow | CP-1 C3 | Operating cash flow, acquisition of PP&E, major maintenance | CFO - capex - major maintenance | Recomputed: 1,052,492; (364,168); 441,369 equal | Supported | High | Cash generation | S1 page:146 |
| Derived fourth quarter | CP-1 C9 | Fiscal year and nine-month statements | Year - nine months | Recomputed: revenues 10,431,233; pretax 739,295 equal | Supported arithmetic, contested by the quarterly share table | Low | Quarterly phasing | S1 page:144; S4 page:5; S1 page:60 |
| Interim LTM leverage | CP-1 C14 | Interim balance sheets and cumulative D&A | FY + year-to-date - prior year-to-date | Recomputed: 2.53, 2.92, 2.57 equal | Supported | High | Seasonal peak | S2 page:4, page:5; S3 page:4, page:5; S4 page:4, page:5 |
| FY2025 undrawn revolver | CP-1 C7 | Assumption: commitment of 2.8 billion unchanged at 2025-08-31 | 2,800.0 - 180.0 | Assumption-Based; labelled in CP-1 | Supported with assumption | Medium | Liquidity trend | S1 page:163; S4 page:12 |
| Fixed charge cover | CP-2 E1, E2 | EBITDA, cash interest, preferred dividends | EBITDA / (cash interest + preferred dividends) | Recomputed: 5.87, 4.47, 6.58; 3.78, 2.35, 4.29 equal | Supported | High | Fixed charges | S1 page:146 |
| Lease and preferred adjusted leverage | CP-2 E3, E4 | Lease liabilities, preferred redemption values | Adjusted debt / EBITDA | Recomputed: 1.39, 2.29, 2.42 equal | Supported | High | Analytical adjustment only | S1 page:192, page:170 |
| Fiscal 2027 demands | CP-2 E5 | Management forecasts and scheduled amounts | Sum of listed demands | Recomputed: 1,536.133 equal | Supported; forecast inputs | Medium | Funding test | S1 page:76, page:77, page:170 |
| Working capital change | CP-2 E6 | Four cash flow lines per year | Sum | Recomputed: (184,007); (464,397); (324,360) equal | Supported | High | Corrects CP-1A | S1 page:146 |
| Share calculations | CP-1A D3, D4; CP-2 E7, E10 | Segment and equity income figures | Ratios | Recomputed: 71%, 37%, 50.4%, 49.1%, 44.9% equal | Supported | High | Concentration | S1 page:144, page:159, page:165, page:181 |
| Confidence Score | This handoff | 18 material claims, 17 of 17 registers, partial source gate, 4 minor findings | Script formula | 51, band Low, qa_status Passed | Script output | High | QA envelope | confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A capital allocation remark | Says fiscal 2026 operating cash flow was swollen by working capital timing; the cash flow statement shows a net outflow of 184,007 | Contradicted claim | A reader could overstate the quality of cash generation | Corrected in CP-2 corrections section; none further | CP-1A capital allocation text; not a report block |
| MINOR | CP-0 conflict log | Did not log the quarterly share table in the annual report, found later by CP-1A | Incomplete conflict log | The table bears on the derived fourth quarter | Carry the CP-1A conflict forward | CP-0 handoff |
| MINOR | CP-2 key findings | Says management says the exemption benefit may not recur; the 10-K says eligibility for later years depends on throughput and EPA evaluation and that offsetting liabilities may arise | Overstated attribution | Slightly stronger than the source | Read as analyst inference; no change to figures | CP-2 key findings |
| MINOR | Derived fourth quarter figures | Arithmetic from audited year and nine-month statements disagrees with the annual report's quarterly share table | Unresolved source conflict | Quarterly phasing and fourth quarter EBITDA are contested | Ask issuer or check next filing; use annual figures | CP-1 quarterly view; CP-1A conflicts; CP-2 key findings |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locator quality | Good: every figure carries a file and page chunk; some cells cite two pages | Lineage register above | A reader can re-open each figure; page chunks differ from printed pages | Low risk of misreading | State chunk versus printed page in later runs |
| Derived figures | Good: formulas and inputs are shown and recompute | Calculation register | Errors would propagate to every ratio | Leverage and cover are reliable as calculated | None |
| Definitions | Weak: EBITDA is derived and includes equity income | CP-1 definition table | Lender definitions may differ | Headroom and comparability not established | Obtain lender EBITDA definition |
| Source conflicts | Fair: two conflicts logged, one unresolved | Conflicts tables in CP-1A | Unresolved table undermines quarterly trend | Annual conclusions stand; quarterly do not | Resolve with issuer |
| Legal and covenant evidence | Absent | Exhibit index lists agreements not supplied | Covenant compliance rests on one sentence | Structure and headroom untraceable | Obtain agreements |
| Upstream consistency | Good after correction: one contradicted remark corrected in CP-2 | Corrections section of CP-2 | Uncorrected text remains in earlier handoffs | Minor | None |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Credit and note purchase agreements | The agreements listed in the exhibit index | Covenants, guarantors, security, restricted payments | Structure and ranking not traceable | Caps committee use | Issuer filings or data room |
| G2 | Covenant levels and compliance figures | Compliance certificate | Headroom | Not calculable | Caps committee use | Issuer |
| G3 | Letters of credit drawn on the revolver | Facility utilization detail | Revolver availability | Liquidity gross of letters of credit | Lowers liquidity precision | Issuer |
| G4 | Quarterly share table conflict | Issuer explanation | Fourth quarter phasing | Quarterly reading contested | Lowers confidence in quarterly claims | Issuer or next filing |
| G5 | Fiscal 2024 debt and revolver balances | Fiscal 2024 annual report | Three-year leverage series | Two year-ends only | Minor | Prior annual report |
| G6 | EBITDA definition used by lenders | Management bridge | Comparability | Derived EBITDA only | Medium | Issuer |
| G7 | Funding for announced projects | Project financing detail | Cash demand beyond fiscal 2027 | Demands exclude the projects | Medium | Issuer |
| G8 | Text extraction fidelity | Image or chart inspection of filings | Table alignment | Numbers matched, charts not inspected | Minor | Original filings |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response, run chscp-2026-11-05-credit_snapshot-host, hash c5f6c43e | Source readiness for seven sources | High | Six headings present, accepted | Ready with limitations | Conflict log incomplete on the quarterly table |
| CP-1 | requests/CP-1 response, same run, hash 528858c5 | Financial base, chart data, debt register | High | Six headings and chart selectors present, accepted | Accepted | Derived EBITDA labelled; fourth quarter derived |
| CP-1A | requests/CP-1A response, same run, hash 2825e453 | Business, governance, conflicts | High | Six headings and selectors present, accepted | Accepted | One contradicted remark |
| CP-2 | requests/CP-2 response, same run, hash 3e276ce5 | Fundamental credit view | High for figures, analyst inference for view | Six headings and selectors present, accepted | Accepted | Corrects CP-1A remark |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Exemption benefit may not recur | Partly supported | Attribution stronger than source | Treat as analyst inference | None |
| MINOR | CP-1A | Working capital remark | Contradicted | Statement does not match cash flow statement | Corrected in CP-2 | None after correction |
| MINOR | CP-0 | Conflict log | Incomplete | Quarterly share table not logged | Carried by CP-1A | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | All recomputed ratios equal the handoffs | EBITDA is derived, not company-reported, and adds back amortization of deferred major maintenance | None | Keep the derived label in every later use | None |
| MINOR | CP-1, CP-1A | Derived fourth quarter | Year less nine months | Disagrees with the annual report quarterly share table | Resolve with issuer | Quarterly claims restricted |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Notes are unsecured and printed as such | Note purchase agreements | Agreements not supplied; co-issuers and guarantors unknown | Obtain agreements | Needed for any ranking or covenant claim |
| MINOR | CP-1A | No creditor-adverse transaction described | Debt agreements and later filings | Absence in these sources is not evidence of absence | Obtain agreements | Needed before relying on the statement |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | No market, rating or relative value claim is made | Ratings, prices, peers | Out of scope for the minimum module set | None here; CP-3 owns relative value | None |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | Operating cash flow described as helped by working capital in CP-1A, shown as hurt by it in CP-2 | CP-2 later and correct; CP-1A cannot be edited | CP-2 correction stands | Readers should use CP-2 |
| MINOR | CP-0, CP-1, CP-1A | Quarterly share table logged only in CP-1A | Later module found it | Carry forward | Quarterly claims contested |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Fiscal 2027 redemptions: release headline against 10-K detail | Consistent across handoffs; filing figure used | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Duplication | Seasonal leverage, Energy concentration and CF Nitrogen concentration recur across modules with consistent figures | None | None |
| MINOR | CP-2 | Committee readiness | View is a draft: structure, covenants and quarterly phasing are restricted | State restriction when presented | Draft Only |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Chart selectors | Four chart tables present; one FY2024 row is Not supplied by design | None | Report charts show a gap for FY2024 |
| MINOR | CP-1A, CP-2 | Report selectors | All present once; prose-only sections contain no table | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I1 | MINOR | CP-1A | Contradicted claim | Working capital remark | Corrected in CP-2 | None | Resolved downstream |
| I2 | MINOR | CP-0 | Incomplete conflict log | Quarterly share table not logged | Carried by CP-1A | None | Resolved downstream |
| I3 | MINOR | CP-2 | Overstated attribution | Exemption benefit recurrence | Treat as analyst inference | None | Open |
| I4 | MINOR | CP-1, CP-1A | Unresolved source conflict | Derived fourth quarter against quarterly share table | Resolve with issuer | Quarterly claims restricted | Open |

## Calculations

Recomputation was done from figures read directly from the extracted text of the cited pages. Amounts are USD thousands unless stated.

| Id | Recomputation | Inputs read from the sources | Result and comparison |
| --- | --- | --- | --- |
| R1 | EBITDA = pretax income + interest expense + D&A | Pretax 1,128,719; 614,772; 1,097,787. Interest 163,633; 146,079; 104,064. D&A 677,145; 651,426; 569,891 (S1 page:144, page:146) | 1,969,497; 1,412,277; 1,771,742, equal to CP-1 C1 |
| R2 | Total debt, net debt and leverage | Notes payable 449,002 and 1,152,457; current portion 70,072 and 90,447; long-term debt 1,982,651 and 1,745,386; cash 263,603 and 327,826 (S1 page:144) | Total debt 2,501,725 and 2,988,290; net 2,238,122 and 2,660,464; 1.27, 2.12, 1.14, 1.88, equal to CP-1 C5 |
| R3 | Interest cover | EBITDA from R1; cash paid for interest 167,057; 147,583; 100,542 (S1 page:146) | 11.79; 9.57; 17.62, equal to CP-1 C6 |
| R4 | Free cash flow after major maintenance | Operating cash flow 1,584,009; 635,787; 1,272,880; capex 463,262; 728,575; 808,763; major maintenance 68,255; 271,380; 22,748 (S1 page:146) | 1,052,492; (364,168); 441,369, equal to CP-1 C3 |
| R5 | Working capital lines | Receivables (150,562), 6,999, (335,974); inventories (455,758), (53,184), 147,764; payables 359,133, (276,114), (213,788); other 63,180, (142,098), 77,638 (S1 page:146) | (184,007); (464,397); (324,360), equal to CP-2 E6 |
| R6 | Fourth quarter derived | Year 1,128,719 less nine months 389,424 (S4 page:5); share 739,295 / 1,128,719 | 739,295; 66% against the table's 36% (S1 page:60); conflict stands |
| R7 | Interim leverage | Debt at quarter ends from balance sheets (S2 page:4, S3 page:4, S4 page:4) over LTM derived EBITDA | 2.53; 2.92; 2.57, equal to CP-1 C14 |
| R8 | Maturity ladder | 58,562 + 190,600 + 150 + 450,000 + 200,000 + 1,105,000 (S1 page:165) | 2,004,312, equal to the printed total; plus finance leases 51,845 less deferred financing costs 3,434 gives 2,052,723, equal to the balance sheet long-term debt |
| R9 | Fixed charge cover and fiscal 2027 demands | See T5B.5; inputs from S1 page:76, page:77, page:146, page:170 | 5.87, 4.47, 6.58; 1,536.133 million, equal to CP-2 E1 and E5 |
| R10 | Confidence score | Lineage counts: Directly Sourced 7, Calculated 8, Conflicting 1, Assumption-Based 1, Analyst Inference 1; 17 of 17 registers; source gate partial; findings 4 minor | Script output: E 83.89, C 100, S 0.7, P 12, score 51, band Low, qa_status Passed |

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Credit agreements, covenant levels and the compliance certificate absent | Legal, covenant and ranking claims untraceable; committee use of those restricted | Obtain agreements |
| Quarterly share table conflict unresolved | Fourth quarter and quarterly phasing contested | Ask issuer or check the next filing |
| Review depth: the review opened the pages cited by the handoffs, not every page of the 349 extracted pages | An uncited error elsewhere would not be found | Sample further pages if the report is used beyond the cited claims |
| Extraction fidelity: text only, charts and images not inspected | Table alignment risk on flattened tables; number matches mitigate | Spot check original filings |
| Letters of credit, fiscal 2024 debt, lender EBITDA definition and project funding not supplied | Liquidity precision and trend limits | See T5B.8 |
| Committee status | Draft Only; covenant, structure and quarterly phasing claims restricted | State the restriction when presented |

## Next module

None: CP-5 is the last module in the minimum set, and the report can be assembled from the accepted handoffs. Before committee use, request the credit agreements and compliance certificate and resolve the quarterly share table with the issuer; use the corrected working capital statement in CP-2 and not the CP-1A remark.
