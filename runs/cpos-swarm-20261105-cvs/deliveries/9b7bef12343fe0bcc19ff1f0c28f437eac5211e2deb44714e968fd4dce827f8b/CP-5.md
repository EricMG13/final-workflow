## Request

Evidence trace and research-integrity review for CVS HEALTH Corp (issuer id cvs, registrant CVS Health Corporation), as of 2026-11-05, pathway credit_snapshot, run cvs-2026-11-05-credit_snapshot-host, reporting period Q3 2026 against FY2025, currency USD. It audits the four accepted handoffs (readiness, financial base, business context and credit synthesis) for claim-to-source lineage, calculations, consistency and handoff integrity, and sets a clearance. Traceability scope is the Top 5 material credit drivers, with a full register of the other flags found. It changes no credit conclusion.

## Sources

### Issuer sources relied on

Every input figure used by the audited handoffs was re-extracted from these files and compared; the re-extraction is in Calculations.

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_cvs-20251231.htm.jsonl | 45f26810f483ed6fa03db93b8fdd124d91bc63cac5132d4d713dc9d4054186f0 |
| 10-Q_2026-03-31_cvs-20260331.htm.jsonl | 09079a76abcacddd5cfdc3d25ef71555f5dbfbfe17adfeaafb34285f1d52046e |
| 10-Q_2026-06-30_cvs-20260630.htm.jsonl | aecbdbd6cbe4692d95cd67ddf7a9be39fdc845ab3dec9a5b7faf116db7070dfd |
| 10-Q_2026-09-30_cvs-20260930.htm.jsonl | d4971bb26e82fba80a1b35b5490f32b4547bbc0a4ec7e55b11b12729167968b0 |
| EX-99.1_2026-05-06_cvs_ex99x1q1-26.htm.jsonl | 55c42d02758692952d0d8a36a1d99162af082561033d921bab815599c14b2d61 |
| EX-99.1_2026-08-05_cvs_ex99x1q2-26.htm.jsonl | ce35d1c0fd861529f90d109402eed8bdc06bcac7900caa2304fcdfe0774a1f89 |
| EX-99.1_2026-11-04_cvs_ex99x1q3-26.htm.jsonl | 2d810cef4dc7931705e3bcaf85563bc175cc15e9e633d6a0cb9aa77c3361955f |

### Run context (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (64803-cvs-health-corp-cvs.json) | 5778dde57161baa53dd06c29b894f51171d7f5b790a52aed512e326c4ec302ef |

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 00323e88451863ab6a85ac8d522cfd8eebec6841dd73889d6adb8761166481da |
| CP-1 | f4151359f3658a370d8b62dadc7eb07c7755fc8145b6d23fd94845f1ec56ffa7 |
| CP-1A | 6b56c7d0ef71dec1d88ce4dacb320988e80e1bad2403ddeaff63b72ded0138e6 |
| CP-2 | 1ee67e9b90149f0b626e7933a05b4120a5f3f096dedfc504bf80c3caaedd457a |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The earlier analysis is traceable: every input figure re-extracted from the filings matched, calculations reproduce, and no conclusion is orphaned. It supports a fundamental view, but protection and structure conclusions have no source. | Medium | EBITDA is analyst-defined, trailing figures combine annual and interim filings, and covenant, guarantor and separation terms are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Inputs for leverage, cover and liquidity were re-extracted from the filings and matched, and the derived ratios recomputed to the same values. | The core metrics can be relied on as arithmetic, subject to the EBITDA definition. | High |
| Leverage and cover rest on an EBITDA the company does not report, and trailing figures combine annual and interim filings. | Ratios are reproducible but cannot be compared with covenant tests, and any recast of 2025 comparatives cannot be checked. | Medium |
| Several characterizations go beyond the filings, including cash described as regulated, the home loan bank facility described as uncommitted and care delivery assets described as underperforming. | These are inferences, not facts, and should be worded as such. | Medium |
| Covenant, guarantor, letter of credit and separation terms are absent, so protection and structure claims have no source. | Committee use should be restricted to the fundamental view until the debt documents and the separation filing are obtained. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of covenant, guarantor and separation-allocation terms, which matters because headroom, ranking and the obligor after the separation cannot be traced to any source, and implies restricted committee use: the fundamental view can be used, protection and structure conclusions cannot. The calculated ratios also rest on an analyst-defined EBITDA that the company does not report, which the earlier handoffs disclose.

### Remediation priority map

- Must-fix before committee: CP5-001 (covenant terms), CP5-002 (ranking and structure statements), CP5-003 (facility expiry change), CP5-004 (EBITDA definition), CP5-007 (letter of credit usage). Obtain the credit agreements, indentures and the amendment; show covenant EBITDA when available; keep protection and ranking language conditional until then.
- Must-fix before the handoff is consumed downstream: CP5-005 (trailing-period construction), CP5-008 (free cash flow sustainability), CP5-009 (confidence score not computed). Label trailing figures as built on 2026 interim comparatives, qualify free cash flow with the working-capital effect, and compute the score with the module script when available.
- Monitoring follow-up: CP5-006 (working-capital float), CP5-010, CP5-011, CP5-014, CP5-015. Trend the payables float, show net leverage on both cash bases, and refresh the market value and ratings when new filings arrive.
- Formatting and hygiene: CP5-012, CP5-013, CP5-016, CP5-017, CP5-018, CP5-019. Reword inferences as inferences, remove repetition, and note the transport headings.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 9. Minor Issues: 10. Committee Use: Restricted.

No finding changes a headline number, and no claim lacks a filing behind it, but nine Material issues bear on covenant capacity, ranking, the facility package, the EBITDA definition and the sustainability of the cash flow that supports deleveraging. The nine Material issues must be disclosed with any committee use. qa_status is Restricted, so the confidence score ceiling of 59 and the Low band apply; the module script that computes the score is not available in this host run, so no numeric score is stated.

### Analytical appendix — complete canonical registers

Module Status: Ready with Limitations. Traceability Scope: Top 5. Upstream re-anchor: the four handoffs consumed are CP-0, CP-1, CP-1A and CP-2 of run cvs-2026-11-05-credit_snapshot-host, as of 2026-11-05, current period Q3 2026, prior period FY2025; the datapoints restated for the audit are total debt of USD 60,680 million, cash of USD 11,738 million, LTM adjusted EBITDA of USD 19,837 million, total debt to adjusted EBITDA of 3.06x, adjusted EBITDA to cash interest of 6.51x and undrawn facilities of USD 7,500 million. No period or run mismatch was found.

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cvs-20251231.htm.jsonl | High: audited annual report | FY2025 | CVS Health Corporation, consolidated | Statements, segment reconciliation, debt table and maturities, contractual obligations, business description | Part III incorporated by reference to a proxy statement not supplied | FY2025 base, instrument-level debt, claims outside debt |
| S2 | 10-Q_2026-03-31_cvs-20260331.htm.jsonl | High: unaudited interim filing | Q1 2026 with Q1 2025 comparatives | CVS Health Corporation, consolidated | Statements, segments, liquidity text | Condensed notes; no instrument-level debt table | LTM Q1 2026 build |
| S3 | 10-Q_2026-06-30_cvs-20260630.htm.jsonl | High: unaudited interim filing | Six months 2026 with 2025 comparatives | CVS Health Corporation, consolidated | Statements, segments, liquidity text, facility expiry wording | Cash flow is cumulative | LTM Q2 2026 build, facility change |
| S4 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | High: unaudited interim filing, most recent | Q3 and nine months 2026 with 2025 comparatives | CVS Health Corporation, consolidated | Statements, segments, liquidity, ratings, litigation, subsequent event | Condensed notes; no instrument-level debt table | Current period base, separation, outside-debt claims |
| S5 | EX-99.1_2026-05-06_cvs_ex99x1q1-26.htm.jsonl | Medium: management earnings release | Q1 2026 | CVS Health Corporation | Headline results, guidance | Management presentation, not controlling over filings | Cross-check only |
| S6 | EX-99.1_2026-08-05_cvs_ex99x1q2-26.htm.jsonl | Medium: management earnings release | Q2 2026 | CVS Health Corporation | Headline results, guidance, operational updates | As above | Cross-check only |
| S7 | EX-99.1_2026-11-04_cvs_ex99x1q3-26.htm.jsonl | Medium: management earnings release | Q3 2026 | CVS Health Corporation | Headline results, guidance, medical benefit ratio table | As above | Cross-check, guidance as Management Language |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage and cover improvement: total debt to adjusted EBITDA 3.78x at FY2025 to 3.06x on LTM Q3 2026; adjusted EBITDA to cash interest 5.71x to 6.51x | CP-1 | Debt carrying value and cash from balance sheets; adjusted operating income, D&A, amortization, interest paid from statements and segment notes | Debt service capacity and leverage tolerance move with both the numerator and denominator | Core of the fundamental credit view | S1 page:138, page:174, page:175; S4 page:3, page:4, page:37 | EBITDA is analyst-defined; no covenant definition |
| 2 | Earnings concentration in Health Care Benefits, which supplied more than the net rise in adjusted operating income | CP-2 | Segment adjusted operating income by period | A reversal in the medical benefit ratio would feed straight into leverage | Determines the downside case | S1 page:138; S4 page:37, page:54, page:55 | Implied Q4 2025 uses FY2025 and 2026 interim comparatives |
| 3 | Liquidity: cash USD 11,738 million, about USD 5,900 million at the parent or nonrestricted subsidiaries, USD 7,500 million of undrawn facilities expiring May 2029, 2030 and 2031 | CP-1 | Balance sheet, liquidity text and facility paragraph | Near-term debt, dividends and settlement payments are covered only with the facilities at parent level | Liquidity runway and refinancing | S4 page:3, page:63, page:64 | Letter of credit usage not supplied |
| 4 | Announced separation into two public companies, expected in the first half of 2028 | CP-1A | Note on subsequent event and MD&A overview | Changes the obligor and possibly the guarantors of existing debt | Monitoring item and structural uncertainty | S4 page:40, page:44 | Event is proposed, not completed |
| 5 | Protection, ranking and allocation terms cannot be assessed: no covenant levels, guarantors, indentures or separation allocation | CP-0, CP-1, CP-2 | Compliance statement only; debt table lists series without issuer or guarantor | Headroom, structural subordination and post-separation treatment are unknown | Restricts committee use | S1 page:153, page:235; S4 page:64 | Absence of evidence, not adverse evidence |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 3.06x and cover 6.51x on LTM Q3 2026 | CP-1 | Debt 3,457 + 57,223; adjusted EBITDA 17,098 + 4,520 - 1,781; interest paid 3,048 (S4 page:3, page:4, page:37; S1 page:138, page:174, page:175) | Yes | High inputs, analyst definition | Calculated | Supported with definition caveat | Medium | Remediation Needed |
| Health Care Benefits drove the improvement | CP-2 | Segment adjusted operating income 6,379 against 3,615 for nine months (S4 page:37) | Yes | High | Calculated | Supported | High | Committee-Ready |
| Liquidity of USD 11,738 million cash and USD 7,500 million undrawn facilities | CP-1 | Cash S4 page:3; facilities and no borrowings S4 page:64; parent-held about 5.9 billion S4 page:63 | Yes | High | Directly Sourced | Supported; letters of credit not supplied | Medium | Remediation Needed |
| Separation announced November 4, 2026 for completion in the first half of 2028 | CP-1A | Subsequent event note (S4 page:40, page:44) | Yes | High | Directly Sourced | Supported; a future date, not a fact | High | Committee-Ready |
| Protection, ranking and allocation terms cannot be assessed | CP-0, CP-1, CP-2 | Compliance statement S4 page:64; series listed without issuer or guarantor S1 page:235 | Yes | High | Insufficient Information | Supported as a gap | High | Remediation Needed |
| Opioid accrual about 3.4 billion dollars outside debt | CP-1 | Remaining accrual statement S4 page:28; obligations table S1 page:155 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Federal government about 20 percent of revenue | CP-1A | S1 page:11 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Operating cash flow lifted by working-capital timing | CP-1 | Cash flow statement and commentary (S4 page:4, page:63) | Yes | High | Directly Sourced | Supported; effect unquantified | Medium | Remediation Needed |
| Care delivery assets underperformed the price paid | CP-1A | Goodwill impairment of the Health Care Delivery reporting unit (S4 page:39, page:45) | Partial | High for the impairment, none for the price inference | Analyst Inference | Partially supported | Low | Remediation Needed |
| Ratings BBB, Baa3, BBB with outlooks | CP-1, CP-1A | Company statement S4 page:64 | Yes | Medium: company statement of agency ratings | Directly Sourced | Supported as a company statement | Medium | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Current portion of long-term debt 3,457 and long-term debt 57,223 at September 30, 2026 | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:3 balance sheet | CP-1 Chart data: leverage | Sourced | High | Sum 60,680 equals carrying value at page:18 |
| Cash and cash equivalents 11,738 | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:3 | CP-1 Chart data: liquidity | Sourced | High | Re-extracted, matches |
| About 5.9 billion of cash held by the parent or nonrestricted subsidiaries | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:63 liquidity | CP-1 Financial base view | Sourced | High | Approximate as printed |
| Three 2.5 billion back-up facilities, expiries May 2029, 2030 and 2031, no borrowings, no commercial paper | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:64 | CP-1 Liquidity by facility | Sourced | High | 7,500 is the sum of the three face amounts |
| Facility expiries May 2028, 2029 and 2030 earlier | pack/10-Q Q1 | 10-Q_2026-03-31_cvs-20260331.htm.jsonl | S2 | page:52 | CP-1A Timeline | Sourced | High | No amendment document supplied |
| Debt table, 47 series with a balance, principal 65,035 at December 31, 2025 | pack/10-K | 10-K_2025-12-31_cvs-20251231.htm.jsonl | S1 | page:235 to page:236 Note 10 | CP-1 Debt instruments | Sourced | High | Re-parsed: 49 lines, 47 with a balance |
| Required repayments 4,007; 3,379; 5,008; 3,758; 4,258; 43,299 | pack/10-K | 10-K_2025-12-31_cvs-20251231.htm.jsonl | S1 | page:236 | CP-1 Chart data: debt maturities | Sourced | High | Schedule as of December 31, 2025 |
| Adjusted operating income 14,443 for FY2025 and amortization 1,976 | pack/10-K | 10-K_2025-12-31_cvs-20251231.htm.jsonl | S1 | page:138 | CP-1 EBITDA review | Sourced | High | Re-extracted |
| Interest paid 2,991, operating cash flow 10,639, capex 2,832 for FY2025 | pack/10-K | 10-K_2025-12-31_cvs-20251231.htm.jsonl | S1 | page:174 | CP-1 Financials | Sourced | High | Re-extracted |
| Adjusted operating income 14,501 and 11,846 for nine months | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:37 | CP-1 Segment drivers | Sourced | High | Segments sum to totals |
| Medical benefit ratio 87.8 percent against 90.0 percent for nine months | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:55 | CP-1A Company and operating model | Sourced | High | Also release page:2 |
| Federal government about 20 percent of consolidated revenues | pack/10-K | 10-K_2025-12-31_cvs-20251231.htm.jsonl | S1 | page:11 | CP-1A Company and operating model | Sourced | High | FY2025 |
| Separation announced November 4, 2026, expected first half of 2028 | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:40 Note 10 | CP-1A Transaction summary | Sourced | High | Labelled future date |
| Opioid remaining accrual about 3.4 billion dollars | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:28 | CP-1 Claims outside the debt figure | Sourced | High | Payment timing not supplied |
| Opioid settlement obligations 3,975 including 648 current at December 31, 2025 | pack/10-K | 10-K_2025-12-31_cvs-20251231.htm.jsonl | S1 | page:155 | CP-1 Claims; CP-2 Calculations | Sourced | High | Older date than the 3.4 billion accrual |
| Omnicare guarantee charge 193 | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:36, page:39 | CP-1 Claims | Sourced | High | Terms not supplied |
| Operating lease liabilities 1,920 and 12,697 | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:3 | CP-1 Claims | Sourced | High | Sum 14,617 |
| Nine-month operating cash flow 15,318 attributed to timing of receipts and payments and Health Care Benefits performance | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:4, page:63 | CP-1 Cash flow quality | Sourced | High | Attribution is management's |
| Ratings BBB (Fitch), Baa3 (Moody's), BBB (S&P) and outlooks | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:64 | CP-1 Latest quarter | Sourced | Medium | Company statement |
| Covenant compliance statement | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:64 | CP-1 EBITDA review | Sourced | High | No levels disclosed |
| Dividend 0.665 dollars per quarter, no repurchases in nine months | pack/10-Q Q3 | 10-Q_2026-09-30_cvs-20260930.htm.jsonl | S4 | page:21, page:4 | CP-1A Governance table | Sourced | High | Absence of a line is read as no repurchases |
| 2026 guidance raised | pack/EX-99.1 Q3 | EX-99.1_2026-11-04_cvs_ex99x1q3-26.htm.jsonl | S7 | page:1 | CP-1 Latest quarter | Management Language | Medium | Management claim |
| Non-affiliate market value about 86.4 billion dollars at June 30, 2025 | pack/10-K | 10-K_2025-12-31_cvs-20251231.htm.jsonl | S1 | page:2 cover | CP-1A Company profile | Sourced | Low for current use | Stale, flagged by CP-1A |
| Implied Q4 2025 Health Care Benefits adjusted operating income loss of 676 | derived | 10-K and 10-Q Q3 | S1, S4 | page:138; page:37 | CP-1 Segment drivers | Calculated | Medium | Combines annual and 2026 interim comparatives |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adjusted EBITDA, LTM Q3 2026 | CP-1, CP-2 | Adjusted operating income 17,098, D&A 4,520, amortization 1,781 (USD millions) | AOI + D&A - amortization of intangibles; LTM = FY2025 + nine months 2026 - nine months 2025; 17,098 + 4,520 - 1,781 = 19,837 | Calculated | Reproduced exactly | Medium | PD, liquidity, refinancing | S1 page:138, page:175; S4 page:4, page:37 |
| Reported EBITDA, LTM Q3 2026 | CP-1 | Operating income 15,061, D&A 4,520 | Operating income + D&A = 19,581 | Calculated | Reproduced exactly | Medium | PD | S1 page:173, page:175; S4 page:2, page:4 |
| Total debt / adjusted EBITDA | CP-1, CP-2 | Debt 60,680; EBITDA 19,837 | 60,680 / 19,837 = 3.06x; FY2025 64,570 / 17,073 = 3.78x | Calculated | Reproduced exactly | Medium | PD, leverage tolerance | S4 page:3; S1 page:174 |
| Net debt / adjusted EBITDA | CP-1, CP-2 | Net debt 48,942 (60,680 - 11,738) | 48,942 / 19,837 = 2.47x; FY2025 56,117 / 17,073 = 3.29x | Calculated | Reproduced; consolidated cash basis | Medium | Leverage | S4 page:3 |
| Net debt / adjusted EBITDA on parent cash | CP-1, CP-2 | Parent-held cash about 5,900 | (60,680 - 5,900) / 19,837 = 2.76x | Calculated | Reproduced; approximate input | Medium | Leverage, liquidity | S4 page:63 |
| Adjusted EBITDA / cash interest | CP-1, CP-2 | Interest paid 3,048 | 19,837 / 3,048 = 6.51x; FY2025 17,073 / 2,991 = 5.71x | Calculated | Reproduced exactly | Medium | Debt service | S1 page:174; S4 page:4 |
| Free cash flow | CP-1, CP-2 | Operating cash flow 18,708; capex 3,141 | 18,708 - 3,141 = 15,567 LTM; less dividends 3,423 = 12,144 | Calculated | Reproduced; working-capital timing unquantified | Low | Liquidity, deleveraging capacity | S1 page:174; S4 page:4 |
| Segment decomposition of the change in adjusted operating income | CP-2 | LTM segment totals | Health Care Benefits +2,764, Health Services +100, Pharmacy & Consumer Wellness +178, Corporate/Other -387, net +2,655 | Calculated | Reproduced exactly | Medium | Concentration | S1 page:138; S4 page:37 |
| Sensitivity: Health Care Benefits at zero (hypothetical) | CP-2 | LTM Health Care Benefits adjusted operating income 5,703 | EBITDA 19,837 - 5,703 = 14,134; 60,680 / 14,134 = 4.29x | Assumption-Based | Labelled hypothetical, not a forecast | Medium | Downside leverage | CP-2 Calculations |
| Indicative twelve-month uses | CP-2 | 3,457; 3,423; 648 | Sum 7,528; parent liquidity 13,400 / 7,528 = 1.78x | Calculated | Reproduced; mixes dates (September 2026 and December 2025) | Low | Liquidity | S4 page:3; S1 page:155 |
| Implied Q4 2025 segment results | CP-1 | FY2025 and nine months 2025 | 2,939 - 3,615 = (676) for Health Care Benefits | Calculated | Reproduced; basis comparability untested | Medium | Concentration | S1 page:138; S4 page:37 |
| Debt bridge at December 31, 2025 | CP-1 | Principal 65,035, premiums 156, discounts and costs 621 | 65,035 + 156 - 621 = 64,570 | Calculated | Reproduced exactly | High | Gross to carrying delta | S1 page:235 to page:236 |
| Segment and reconciliation tie-outs | CP-0, CP-1 | Segment columns, reconciling items | All sums reproduced (see Calculations) | Calculated | Reproduced exactly | High | Data integrity | S4 page:36, page:37 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Protection, ranking and allocation terms | No covenant levels, guarantors or indentures in the pack, so any protection claim has no source | Insufficient Information | Headroom and ranking determine loss given default and refinancing flexibility | Obtain debt documents; keep language conditional | CP-1, CP-1A, CP-2 |
| Material | Leverage and cover | EBITDA is analyst-defined; trailing figures combine annual and interim filings | Calculated | A covenant or agency definition may differ and change the ratio | Show both reported and adjusted bases and the definition | CP-1, CP-2 |
| Material | Undrawn facilities USD 7,500 million | Letter of credit usage not supplied | Weak Lineage | Net availability could be lower, reducing liquidity | Obtain the facility terms or later filing | CP-1, CP-2 |
| Material | Free cash flow supports deleveraging | Working-capital timing effect unquantified | Weak Lineage | Part of the cash build may reverse, lowering debt service capacity | Normalize before extrapolating | CP-1, CP-2 |
| Minor | Cash in regulated subsidiaries; home loan bank capacity uncommitted | Characterizations not stated in the filings | Analyst Inference | Wording overstates what the source says | Reword as inference | CP-1 |
| Minor | Care delivery assets underperformed the price paid | Inferred from a goodwill impairment | Analyst Inference | Wording overstates what the source says | Reword as inference | CP-1A |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 and three 2026 quarters; no debt documents, proxy statement or 2025 interim filings | Missing documents leave protection, ownership and recast questions untested | Fundamental view usable; protection analysis restricted | Obtain indentures, credit agreements, proxy statement |
| Citation completeness | Ready with Remediation | Every material figure has a page locator in the financial base and business context; the synthesis cites upstream handoffs by module | A two-hop trace is needed for the synthesis | No loss of support, small audit cost | State source locators in later syntheses |
| Calculation traceability | Committee-Ready | Formulas, inputs and results shown; all recomputed to the same values | Arithmetic risk is low | Ratios can be relied on as arithmetic | None beyond definition labelling |
| Assumption transparency | Ready with Remediation | EBITDA definition, trailing-period construction and hypothetical sensitivities are labelled | Definition drift against a covenant is untestable | Comparison with covenant tests is not possible | Add covenant EBITDA when available |
| Markdown and export artifact integrity | Committee-Ready | Each handoff carries the six required headings, sources with hashes and the required view sections | Low | None | None |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Covenant levels and definitions | Credit agreements and indentures | Headroom and default triggers cannot be assessed | Protection analysis, leverage tolerance | High impact | Facility agreement and indentures |
| CP-5-GAP-002 | Guarantor, issuer and security by series | Indentures, guarantee schedules | Ranking and structural subordination unknown | Recovery mechanics, separation analysis | High impact | Indentures |
| CP-5-GAP-003 | Separation allocation and financing | Form 10 and any amendments | Obligor and guarantor structure after completion | Refinancing view | High impact | Form 10 and indenture amendments |
| CP-5-GAP-004 | Letters of credit on facilities | Facility terms | Net availability of the facilities | Liquidity | Medium impact | Facility agreement |
| CP-5-GAP-005 | Facility amendment that moved expiries | Amendment document | Terms and conditions of the extended facilities | Liquidity runway | Medium impact | Exhibits to quarterly filings |
| CP-5-GAP-006 | Working-capital float trend | Quarterly trend of payables and claims liabilities | Cash flow quality | Free cash flow sustainability | Medium impact | Q3 10-Q page:3 and prior quarters |
| CP-5-GAP-007 | 2025 interim filings | Prior-year quarterly filings | Recast of comparatives cannot be tested | Trailing figures | Low impact | 2025 Forms 10-Q |
| CP-5-GAP-008 | Confidence score computation | Module script output | Numeric score and band cannot be stated | Handoff envelope | Medium impact | Module script when available |
| CP-5-GAP-009 | Market data | Prices, spreads, yields, peer set | No current relative-value conclusion is possible | Relative-value work outside this run | Low impact | Market data vendor |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | CP-0 handoff, sha256 00323e88451863ab6a85ac8d522cfd8eebec6841dd73889d6adb8761166481da, run cvs-2026-11-05-credit_snapshot-host | Source readiness, seven sources | High filings, medium releases | Six required headings and reader summary present | Accepted by the run's structure check | Correctly states gaps; note-line count corrected by CP-1 |
| CP-1 | CP-1 handoff, sha256 f4151359f3658a370d8b62dadc7eb07c7755fc8145b6d23fd94845f1ec56ffa7, same run | Financial base and credit metrics | High filings, analyst EBITDA | Six required headings, chart tables and financial table present | Accepted by the run's structure check | Inputs re-extracted and matched |
| CP-1A | CP-1A handoff, sha256 6b56c7d0ef71dec1d88ce4dacb320988e80e1bad2403ddeaff63b72ded0138e6, same run | Business and transaction context | High filings, medium releases | Six required headings, two tables and prose section present | Accepted by the run's structure check | Two inferences flagged |
| CP-2 | CP-2 handoff, sha256 1ee67e9b90149f0b626e7933a05b4120a5f3f096dedfc504bf80c3caaedd457a, same run | Credit synthesis | Derived from upstream handoffs | Six required headings, prose sections present | Accepted by the run's structure check | Cites upstream by module, not by source locator |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | Undrawn committed facilities of USD 7,500 million | Partially Supported | The face amounts and absence of borrowings are sourced, but letter of credit usage is not supplied, so availability assumes none | State availability as face amount less unknown letters of credit; obtain facility terms | Restricts Committee Use |
| MATERIAL | CP-2 | LTM free cash flow of USD 15,567 million and USD 12,144 million after dividends as the funding of deleveraging | Partially Supported | The cash flow figures are sourced, but the 2026 working-capital timing effect is unquantified and the strengths paragraph is less qualified than the key findings | Qualify with the working-capital effect wherever the figure supports capacity | Restricts Committee Use |
| MINOR | CP-1 | Remaining cash described as in regulated or restricted subsidiaries; home loan bank capacity described as uncommitted | Partially Supported | The filings say only that part of the cash is held by the parent or nonrestricted subsidiaries and that advances are subject to collateral requirements | Reword as inference | Formatting / Hygiene Only |
| MINOR | CP-1A | Acquired care delivery assets underperformed the price paid | Partially Supported | Source states a goodwill impairment of the Health Care Delivery reporting unit; the price inference is the analyst's | Reword as an interpretation tied to the impairment | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | Leverage and cover use adjusted EBITDA | The company reports no EBITDA and no covenant definition; the measure is adjusted operating income plus D&A less amortization of intangibles, which is applied consistently in both modules (no definition drift) | None between modules; covenant definition absent | Keep the definition on every use; add covenant EBITDA when obtained | Restricts Committee Use |
| MATERIAL | CP-1, CP-2 | Trailing periods and implied Q4 2025 results | FY2025 from the annual report is combined with 2025 comparatives printed in 2026 interim filings; the 2025 interim filings are not in the pack, so recasts cannot be tested | None found; sums of 2025 quarters equal the nine-month figures | Label as built on filed comparatives; obtain 2025 interim filings if possible | Requires Source Reconciliation |
| MATERIAL | CP-1 | Working-capital float | Pharmacy claims and discounts payable, health care costs payable and accounts payable are not trended although nine-month operating cash flow depends on timing (balance sheet S4 page:3) | None | Trend the float lines by quarter before extrapolating cash flow | Requires Calculation Rebuild |
| MINOR | CP-1, CP-2 | Headline net leverage 2.47x uses consolidated cash | A parent-basis figure of 2.76x is shown in the same handoffs, so the choice is disclosed; the conservative case is not the headline | None | Show both next to each other in summaries | Formatting / Hygiene Only |
| MINOR | CP-1, CP-2 | Parent-held cash is approximate | The source prints about 5.9 billion; a ratio to two decimals implies more precision than the input | None | State the ratio as approximate | Formatting / Hygiene Only |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | Covenant protection: only a compliance statement and customary-covenant wording exist; headroom reported as not calculable | Facility credit agreements and note indentures | No levels, definitions or certificates | Keep headroom Not Calculable; no inference of capacity | Legal review required for any covenant conclusion |
| MATERIAL | CP-1A, CP-2 | Ranking and structural statements: unsecured senior notes, two junior subordinated series, and structural questions on separation | Indentures, guarantee schedules, the separation Form 10 | Issuer, co-issuer and guarantor by series not printed in the note | Keep ranking language conditional; do not state recovery effects | Legal review required before any ranking or recovery view |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | No relative-value, price, spread or peer claim is made; ratings are company statements of agency ratings | Prices, spreads, yields and a comparable set; the run context quotes and ratings fields are blank | Market data not in the pack | None for this output; any later relative-value work needs market data | Restricts any current relative-value conclusion |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-0, CP-1, CP-1A, CP-2 | Back-up facility expiries moved from May 2028, 2029 and 2030 to May 2029, 2030 and 2031 between the Q1 and Q2 filings; all four modules use the later dates consistently | No amendment or credit agreement in the pack explains the change | Obtain the amendment; keep the later dates labelled as filing wording | Liquidity runway rests on filing wording |
| MINOR | CP-0, CP-1 | CP-0 counted 49 note lines; CP-1 corrected this to 47 with a balance and two nil lines, and CP-1A and CP-2 carry the correction | Correction recorded in the later handoff because the earlier one cannot be edited | None; closed | None |
| MINOR | CP-1A | Non-affiliate market value of about 86.4 billion dollars is as of June 30, 2025 | Stale relative to the as-of date; CP-1A flags this | Do not use for current market capitalization | None for credit conclusions |

Cross-module checks that found no conflict: issuer name and id, reporting period, total debt 60,680, cash 11,738, adjusted EBITDA 19,837, leverage 3.06x and 2.47x, cover 6.51x, facilities 7,500, ratings and outlooks, opioid accrual, Omnicare 193 and the separation date.

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Duplicative content | Leverage, liquidity and claims figures are repeated across the financial base view, the credit view and the key findings; promotional wording appears only inside attributed Management Language rows | Keep the credit view as the single committee entry point | Formatting only |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-5 | Confidence score and qa_status fields | The module script that computes the numeric score and band is not available in this host run, so no score is stated; qa_status is set to Restricted by the severity rule | Run the script when available and record the score | Restricted committee use until recorded |
| MINOR | CP-2 | Evidence trace | Key findings cite upstream handoffs by module in brackets, so a source locator needs a second hop through the financial base or business context | Add source locators in the next synthesis | Small audit cost |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Handoff envelope | The handoffs use the run's six transport headings and no separate YAML front matter, as the run instructions require | Note only | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1, CP-2 | Legal Support Gap | Covenant levels, definitions and certificates absent; compliance statement only | Obtain credit agreements and indentures; keep headroom Not Calculable | Requires Legal Review | Open |
| CP5-002 | MATERIAL | CP-1A, CP-2 | Recovery / Ranking Overreach | Ranking and structural statements without indentures or guarantee schedules | Keep conditional; no recovery effects | Requires Legal Review | Open |
| CP5-003 | MATERIAL | CP-0, CP-1, CP-1A, CP-2 | Version Conflict | Facility expiries moved one year with no amendment supplied | Obtain amendment | Requires Source Reconciliation | Open |
| CP5-004 | MATERIAL | CP-1, CP-2 | Formula / Definition Drift | EBITDA is analyst-defined; no covenant definition | Show definition; add covenant EBITDA when available | Restricts Committee Use | Open |
| CP5-005 | MATERIAL | CP-1, CP-2 | Period Mismatch | Trailing figures combine annual and interim filings; recasts untested | Label as built on filed comparatives | Requires Source Reconciliation | Open |
| CP5-006 | MATERIAL | CP-1 | Calculation Error | Working-capital float not trended (omitted analysis, not an arithmetic error) | Trend float lines by quarter | Requires Calculation Rebuild | Open |
| CP5-007 | MATERIAL | CP-1, CP-2 | Partially Supported Claim | Undrawn facilities assume no letter of credit usage | Obtain facility terms | Restricts Committee Use | Open |
| CP5-008 | MATERIAL | CP-2 | Partially Supported Claim | Free cash flow presented as funding deleveraging without full working-capital qualification | Qualify wherever used | Restricts Committee Use | Open |
| CP5-009 | MATERIAL | CP-5 | canonical Markdown Handoff Integrity Defect | Numeric confidence score not computed | Run the module script when available | Blocks canonical Markdown Handoff / Downstream Grounding | Open |
| CP5-010 | MINOR | CP-1, CP-2 | Source Quality Limitation | Headline net leverage uses consolidated cash | Show parent basis alongside | Formatting / Hygiene Only | Open |
| CP5-011 | MINOR | CP-1, CP-2 | Source Quality Limitation | Parent-held cash is approximate | State ratio as approximate | Formatting / Hygiene Only | Open |
| CP5-012 | MINOR | CP-1 | Partially Supported Claim | Regulated cash and uncommitted home loan bank wording | Reword as inference | Formatting / Hygiene Only | Open |
| CP5-013 | MINOR | CP-1A | Partially Supported Claim | Care delivery underperformance inference | Reword as interpretation | Formatting / Hygiene Only | Open |
| CP5-014 | MINOR | CP-1, CP-1A, CP-2 | Market Data Gap | No market data; ratings are company statements | None now; market data for later work | Requires Market Data Refresh | Open |
| CP5-015 | MINOR | CP-1A | Source Quality Limitation | Stale non-affiliate market value | Do not use as current | Monitoring Follow-Up | Open |
| CP5-016 | MINOR | CP-0, CP-1 | Cross-Module Inconsistency | Note-line count 49 corrected to 47 with a balance | None | Formatting / Hygiene Only | Closed |
| CP5-017 | MINOR | CP-1, CP-1A, CP-2 | Duplicative / Immaterial Content | Figures repeated across sections | Keep the credit view as the entry point | Formatting / Hygiene Only | Open |
| CP5-018 | MINOR | CP-2 | Evidence Trace Defect | Upstream cited by module, locators need a second hop | Add locators next time | Monitoring Follow-Up | Open |
| CP5-019 | MINOR | CP-0, CP-1, CP-1A, CP-2 | canonical Markdown Handoff Integrity Defect | Transport headings instead of front matter | Note only | Formatting / Hygiene Only | Open |

## Calculations

The audit re-extracted every input from the source files by label and period, independently of the audited handoffs, and recomputed the derived values. Amounts in USD millions.

| Input | Re-extracted value and locator | Used by handoffs | Result |
| --- | --- | --- | --- |
| FY2025 revenue, operating income, interest expense | 402,067; 4,660; 3,119 (S1 page:173) | Same | Match |
| FY2025 interest paid, operating cash flow, capex | 2,991; 10,639; 2,832 (S1 page:174) | Same | Match |
| FY2025 D&A, dividends paid | 4,606; 3,397 (S1 page:175) | Same | Match |
| FY2025 adjusted operating income, amortization | 14,443; 1,976 (S1 page:138) | Same | Match |
| Q1 2026 and Q1 2025 operating income, interest expense | 4,680 and 3,374; 774 and 785 (S2 page:2) | Same | Match |
| Q1 adjusted operating income, amortization, D&A | 5,150 and 4,579; 442 and 499; 1,115 and 1,154 (S2 page:32 to page:33, page:4) | Same | Match |
| Q1 interest paid, capex, dividends | 1,091 and 1,012; 849 and 743; 847 and 840 (S2 page:3, page:4) | Same | Match |
| Six months operating income, interest expense | 9,383 and 5,755; 1,531 and 1,548 (S3 page:2) | Same | Match |
| Six months adjusted operating income, amortization, D&A | 10,307 and 8,387; 873 and 993; 2,241 and 2,325 (S3 page:35, page:4) | Same | Match |
| Six months interest paid, capex, dividends | 1,551 and 1,484; 1,540 and 1,350; 1,725 and 1,706 (S3 page:4) | Same | Match |
| Nine months operating income, interest expense | 12,949 and 2,548; 2,278 and 2,332 (S4 page:2) | Same | Match |
| Nine months adjusted operating income, amortization, D&A | 14,501 and 11,846; 1,298 and 1,493; 3,373 and 3,459 (S4 page:37, page:4) | Same | Match |
| Nine months interest paid, capex, dividends | 2,586 and 2,529; 2,357 and 2,048; 2,578 and 2,552 (S4 page:4) | Same | Match |
| Debt and cash at four dates | Debt 4,068 + 60,502; 2,580 + 60,531; 1,958 + 59,452; 3,457 + 57,223; cash 8,453; 9,542; 11,329; 11,738 (S1 page:174; S2, S3, S4 page:3) | Same | Match |
| 2025 quarter sums | Operating income 3,374 + 2,381 + (3,207) = 2,548; adjusted operating income 4,579 + 3,808 + 3,459 = 11,846; D&A 1,154 + 1,171 + 1,134 = 3,459 (S2, S3, S4) | Nine-month 2025 values | Sums equal the nine-month figures |
| 2026 quarter sums | Operating income 4,680 + 4,703 + 3,566 = 12,949; adjusted operating income 5,150 + 5,157 + 4,194 = 14,501 | Nine-month 2026 values | Sums equal the nine-month figures |
| LTM adjusted EBITDA | Q1 15,014 + 4,567 - 1,919 = 17,662; Q2 16,363 + 4,522 - 1,856 = 19,029; Q3 17,098 + 4,520 - 1,781 = 19,837 | CP-1 | Match |
| Ratios | 64,570 / 17,073 = 3.78; 63,111 / 17,662 = 3.57; 61,410 / 19,029 = 3.23; 60,680 / 19,837 = 3.06; net 3.29, 3.03, 2.63, 2.47; cover 5.71, 5.75, 6.22, 6.51 | CP-1 chart data | Match to two decimals |
| Parent-basis net leverage | (60,680 - 5,900) / 19,837 = 2.76 | CP-1, CP-2 | Match |
| Sensitivities and uses | 14,134; 60,680 / 14,134 = 4.29; 17,073 and 3.55; 7,528 and 1.78 | CP-2 | Match |
| Debt table | 47 of 49 lines with a balance; sum 63,414; plus 1,326 plus 295 = 65,035; maturity-year sums 4,000; 3,372; 5,000; 3,750; 4,250; 43,042 against the printed 4,007; 3,379; 5,008; 3,758; 4,258; 43,299, difference 295 | CP-1 | Match; difference equals the other line |
| Working-capital float lines at September 30, 2026 | Accounts payable 17,875; pharmacy claims and discounts payable 26,296; health care costs payable 16,858 against 17,641; 26,344; 15,399 at December 31, 2025 (S4 page:3) | Not used by handoffs | Reference for the float trend requested in CP5-006 |

Counts for the clearance: 0 Critical, 9 Material, 10 Minor, total 19, equal to the rows of the consolidated issue log.

## Gaps

| Gap | Severity | Remediation |
| --- | --- | --- |
| No covenant levels, indentures, credit agreements, guarantor schedules or facility amendment are in the pack, so protection, ranking and the facility change cannot be traced. | Material | Obtain the documents; keep headroom Not Calculable. |
| The numeric confidence score and band are not stated because the module script is unavailable in this host run; qa_status is Restricted by rule. | Material | Run the script when available and record the score. |
| The 2025 interim filings are not in the pack, so recasts of the 2025 comparatives used in trailing figures cannot be tested. | Material | Obtain the 2025 Forms 10-Q if a recast check is needed. |
| The working-capital float is not trended; nine-month operating cash flow depends on timing. | Material | Trend payables and claims liabilities by quarter. |
| No market data, and the context ratings and quotes fields are blank, so no relative-value conclusion is audited. | Minor | Supply market data for later relative-value work. |
| The separation terms are the subject of a future filing; this audit tests only what was announced. | Material | Re-audit when the Form 10 is available. |

## Next module

None. CP-5 is the last module in this run. The run should proceed to delivery with committee use Restricted and the nine Material issues disclosed; the next re-audit triggers are receipt of the debt documents, the facility amendment, the separation Form 10 and the next quarterly filing.
