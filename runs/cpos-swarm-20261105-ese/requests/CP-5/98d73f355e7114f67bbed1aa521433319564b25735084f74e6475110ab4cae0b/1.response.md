# CP-5 evidence trace validator and research integrity QA: ESCO TECHNOLOGIES INC (ese)

## Request

ESCO TECHNOLOGIES INC (issuer id `ese`) is audited as of 2026-11-05 on the `credit_snapshot` pathway, run `ese-2026-11-05-credit_snapshot-host`, reporting period Q3 2026 (quarter ended June 30, 2026) with FY2025 (year ended September 30, 2025) as the prior period. The scope is the evidence trace and research-integrity grade of the four upstream handoffs (CP-0, CP-1, CP-1A, CP-2) at Top 5 traceability scope, with claims re-checked against the seven pinned filings. It adds no new credit analysis and does not change any upstream conclusion.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | fe80d5d10f35aaa7f1b7aa40e6d69aeaea7f501fabdde619947c03aa0fe69d71 |
| 10-Q_2025-12-31_ese-20251231x10q.htm.jsonl | 028e0b9aec25ecf720ca796f0beef13fd8b40ddc333348a8ba8153fe3b16e523 |
| 10-Q_2026-03-31_ese-20260331x10q.htm.jsonl | d207365eeea17e17e69c10625b481ddba582ee4861f7a9c60376e4bd5dffc806 |
| 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | 056428009193705ead08cb6828be9f20a62a9323946644ad69e280efbf618711 |
| EX-99.1_2026-01-30_tm264950d1_ex99-1.htm.jsonl | 73c00c863e8360707e7681c62537391b693f1632ac470f63ec94b54622dbc238 |
| EX-99.1_2026-05-07_tm2613615d1_ex99-1.htm.jsonl | 4483c93985a6b3ea98a959d8659fafa040f3230850186662a7c5bb7c5d2d8a1d |
| EX-99.1_2026-08-06_tm2621646d1_ex99-1.htm.jsonl | f683102e1a6a6e74cee756fd0639a64a1d810e0d5fd17fcb2dc502f25f716fb6 |

### Other inputs

| Input | sha256 |
| --- | --- |
| context (`contexts/866706-esco-technologies-inc-ese.json`; run settings, not issuer evidence) | da65696ce609dcf19999b44c58b8a10f43f7d7bc7cde7c4a3762d76affdde214 |

### Supplied handoffs

| Module | sha256 | Run |
| --- | --- | --- |
| CP-0 | 7f46d3b1dbdad4b468a5bdd5db37f408dc8a1ce57aba77ff195a116822899d17 | `ese-2026-11-05-credit_snapshot-host` |
| CP-1 | 23a50d14b3104c2571d80147c88f81427457a9b11a2aa773f3459c4d026de1e7 | same |
| CP-1A | 7bb2aa7585c6ae63abcfb32f227dd60a79e423f35bf4601e20c348a72e1bc24b | same |
| CP-2 | e297e9a788228578ae850f917d4e33d0c320993e352e7c8e80e8fca511818320 | same |

### Labels

Locators are `page:N` of the pinned text files. "10-Q Q1", "10-Q Q2" and "10-Q Q3" are the 10-Qs for the quarters ended December 31, 2025, March 31, 2026 and June 30, 2026; "Release Q3" is the EX-99.1 dated August 6, 2026. Severities are CRITICAL, MATERIAL and MINOR only. Registers are in the appendix under Findings; the confidence score is script-owned and was not computed here, so only the rule-bound band is stated.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream analysis is largely traceable to the filings and its key figures recomputed correctly. One statement on cash interest is unsupported, and covenant, new financing and Megger documents are missing, so committee use is restricted. | Low | Executed credit agreements, Megger documents and any filing after August 10, 2026 are not supplied, so legal terms and post-closing leverage cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Key figures, including total borrowings of USD 85.0 million and LTM EBITDA of USD 305.677 million, matched the filings on independent recomputation. | The low reported leverage and strong liquidity conclusions rest on sound inputs. | High |
| One statement says the roughly USD 7 million of Megger financing costs is not in cash interest paid; the filings do not say so. | The cover ratio of 20.42x may be understated and should carry that caveat. | Medium |
| Covenant levels and the new credit agreement are not supplied. | Headroom cannot be traced or tested, so covenant statements remain management assertions. | High |
| The illustrative leverage bound of 3.22x is labelled an inference and omits Megger earnings. | It must not be read as pro forma leverage in committee material. | High |
| No source after August 10, 2026 is supplied. | Closing status and drawn debt at the as-of date cannot be traced. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the executed credit agreements (covenant levels and the New Credit Facility terms), which matters because covenant headroom and post-closing leverage cannot be traced to any source and implies that committee use must be restricted rather than approved.

This is consistent with the auditability assessment in the appendix, where the lowest dimension is Ready with Remediation.

### Traceability conclusion

The upstream modules are traceable enough for restricted committee use but not for a clean pass. Every figure behind the leverage, liquidity and cover conclusions was recomputed from the filed statements and matched, and each quoted passage was found on its cited page. The weakest point is that the most decision-relevant item, covenant headroom after the Megger financing, rests on documents that were never supplied, so the handoffs correctly mark it Not supplied rather than estimate it. One cover-ratio caveat in the financial base is unsupported and should be corrected or restated as unknown. What decides committee use is whether the executed credit agreements, the Megger documents and filings after August 10, 2026 are added; until then the credit view can be used only with those limits.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 12. Committee Use: Restricted.

No Critical finding exists, so the grade is not Blocked, but one Material finding (CP5-001, an unsupported statement about cash interest in the financial base) and the missing executed legal documents keep committee use restricted. The research QA status is Restricted. Under the confidence rule that a Restricted status caps the score at 59, the band is Low. The Material issue must be disclosed with any committee use of the cover ratio.

### Remediation priority map

1. Must-fix before committee: CP5-001. Restate the LTM cash interest cover caveat as unknown, or show the cover on both bases, and disclose it with the 20.42x figure.
2. Must-fix before the handoff is consumed downstream: CP5-002 and CP5-013. Keep the 3.22x bound labelled as an Analyst Inference with its omitted inputs wherever reused, and keep relative value, ratings and market data out of the credit view.
3. Monitoring follow-up: CP5-003, CP5-007, CP5-008, CP5-009 and CP5-010. Obtain the April 15, 2026 8-K, the executed credit agreements and the explanation for the contract-liability difference and the current-portion wording; re-audit when they arrive.
4. Formatting and hygiene: CP5-004, CP5-005, CP5-006, CP5-011 and CP5-012. Tighten three wordings (undrawn revolver description, segment growth statement, "will reset"), remove repeated caveats, and note the transport envelope.

### Analytical appendix — complete canonical registers

#### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | High: filed, audited statements | FY2025 (year ended September 30, 2025), FY2024, FY2023 | ESCO Technologies Inc. and subsidiaries, continuing operations | Statements, debt note, segments, backlog, history, officers | Text extraction only; ICFR opinion excludes Maritime | CP-1, CP-1A |
| S2 | 10-Q_2025-12-31_ese-20251231x10q.htm.jsonl | High: filed, unaudited | Quarter ended December 31, 2025 | Same | Balance sheet, debt, interest paid | Unaudited | CP-1 |
| S3 | 10-Q_2026-03-31_ese-20260331x10q.htm.jsonl | High: filed, unaudited | Quarter and six months ended March 31, 2026 | Same | Debt, interest paid, Megger subsequent event | Unaudited | CP-1, CP-1A |
| S4 | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | High: filed, unaudited | Quarter and nine months ended June 30, 2026 | Same | Statements, notes, debt, leases, Megger, New Credit Facility, exhibits | Unaudited; nine-month cash flows only | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-01-30_tm264950d1_ex99-1.htm.jsonl | Medium: management release, unaudited | Quarter ended December 31, 2025 (release dated February 5, 2026) | Same | Quarterly EBITDA reconciliation | Filename date differs from release date | CP-1 |
| S6 | EX-99.1_2026-05-07_tm2613615d1_ex99-1.htm.jsonl | Medium: management release | Quarter ended March 31, 2026 | Same | Quarterly and six-month EBITDA | Management-defined adjusted measures | CP-1 |
| S7 | EX-99.1_2026-08-06_tm2621646d1_ex99-1.htm.jsonl | Medium: management release | Quarter ended June 30, 2026 | Same | EBITDA, adjusted measures, backlog, guidance, Megger status | Management-defined adjusted measures | CP-1, CP-1A |

Module Status: Ready with Limitations. Traceability Scope: Top 5. Missing required inputs: executed credit agreements, Megger documents, proxy statement and any filing after August 10, 2026. Entity key: issuer_id `ese` available; context leaves borrower, parent and guarantor blank. Coverage of this audit: the claims in all four handoffs were searched in the sources and every cited page was opened; pages of the 10-K and earlier 10-Qs not cited were not read in full.

#### Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Low reported leverage and strong cash interest cover | CP-1, CP-2 | Total borrowings of USD 85.0 million against LTM EBITDA of USD 305.677 million give total debt to EBITDA of 0.278x; cash interest cover is 20.42x | Sets debt service capacity and leverage tolerance before acquisition financing | Supports a lightly levered starting position | 10-Q Q3 pages 2, 3, 4, 10; 10-K pages 57, 59; Release Q3 page 7 | Reported basis, not covenant basis; cover caveat (CP5-001) |
| 2 | Liquidity and maturity profile | CP-1, CP-2 | Cash of USD 73.236 million plus undrawn revolver of USD 442.300 million; USD 20.000 million current and USD 65.000 million due by August 30, 2028 | Determines refinancing and liquidity risk | Near-term liquidity is ample until the facility is replaced | 10-Q Q3 pages 2, 10, 11 | Undrawn amount is calculated; repayment schedule not printed |
| 3 | Megger acquisition and new financing | CP-1A, CP-2 | Approximately USD 2.35 billion consideration, USD 0.9 billion cash, new USD 500 million revolver and two USD 500 million term loans effective at closing | Resets debt, covenants, maturities and ownership | Event-driven credit; the central uncertainty | 10-Q Q3 pages 12, 19, 30; Release Q3 page 3 | Agreements and Megger financials not supplied; closing status unknown |
| 4 | Covenant headroom | CP-1, CP-2 | Leverage and interest coverage covenants exist; compliance is stated by management | Governs default and restricted payment risk | Cannot be assessed | 10-K page 80; 10-Q Q3 page 11 | Levels and definitions not supplied |
| 5 | Revenue visibility and government concentration | CP-1A, CP-2 | Backlog of USD 1,540.5 million with approximately 59% in twelve months; US Government approximately 23% of revenue | Drives revenue durability and cash conversion | Visibility is high but contracts are terminable for convenience | 10-Q Q3 page 16; 10-K pages 9, 10 | Backlog excludes options; budget exposure concentrated in the largest segment |

#### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Low reported leverage and strong cover | CP-1, CP-2 | Filed statements and notes; recomputed | Yes | High | Calculated | Supported, with the CP5-001 caveat on the cover denominator | High for leverage, Medium for cover | Remediation Needed |
| Liquidity and maturities | CP-1, CP-2 | 10-Q Q3 pages 2, 10, 11 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Megger acquisition and new financing | CP-1A, CP-2 | 10-Q Q3 pages 12, 19, 30 | Yes | High for the summary, Low for terms | Directly Sourced | Supported as management's summary; terms not supported | Medium | Committee-Ready for the summary |
| Covenant headroom | CP-1, CP-2 | 10-K page 80; 10-Q Q3 page 11 | Yes for types and compliance | High for existence, none for levels | Insufficient Information | Insufficient Information, marked Not supplied upstream | Low | Not Traceable (disclosed) |
| Revenue visibility and government concentration | CP-1A, CP-2 | 10-Q Q3 page 16; 10-K pages 9, 10, 86 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |

#### Source lineage

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total borrowings USD 85,000 thousand at June 30, 2026 | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:10 Note 7 Debt | CP-1 Financials | Sourced | High | Verified |
| Total borrowings USD 186,000 thousand at September 30, 2025 | source-text | 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S1 | page:80 Note 7 | CP-1 Financials | Sourced | High | Same figure in S4 page:10 |
| Cash USD 73,236 thousand at June 30, 2026 | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:2 balance sheet | CP-1 Liquidity | Sourced | High | Verified |
| Revolver commitment USD 500 million, matures August 30, 2028 | source-text | 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S1 | page:80; S4 page:10 | CP-1 Debt | Sourced | High | Verified |
| Approximately USD 442 million available; letters of credit USD 12.7 million | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:11 | CP-1 Liquidity | Sourced | High | Recomputed 442,300 equals the stated approximation |
| Nine-month EBT 120,296 and interest expense, net 13,992 | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:2 | CP-1 Financials | Sourced | High | Verified |
| Nine-month D&A 80,073 and FY2025 D&A 75,021 | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl; 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S4, S1 | S4 page:3; S1 page:59 | CP-1 Financials | Sourced | High | Cash flow statement removes discontinued earnings before adding D&A, so continuing |
| Consolidated EBITDA 214,361 for nine months, 76,410 for Q3 2026 | source-text | EX-99.1_2026-08-06_tm2621646d1_ex99-1.htm.jsonl | S7 | page:7 | CP-1 Definitions | Sourced | Medium | Equals recomputed EBIT plus D&A |
| Interest paid 13,587 (nine months 2026), 16,038 (nine months 2025), 17,421 (FY2025) | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl; 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S4, S1 | S4 page:4; S1 page:59 | CP-1 Cover | Sourced | High | Total, not split by continuing and discontinued operations |
| Covenants are a leverage ratio and an interest coverage ratio | source-text | 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S1 | page:80 | CP-1 Covenants | Sourced | High | Levels not printed |
| Compliance with all covenants at June 30, 2026 | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:11 | CP-1 Covenants | Management assertion | Medium | Not independently testable |
| Megger consideration, cash and equity split, expected closing | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:19 | CP-1A Transaction | Sourced | High | Components stated as approximate |
| New Credit Facility three tranches of USD 500 million, effective at closing | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:12 | CP-1A Transaction | Sourced | High | Agreement not supplied |
| Backlog USD 1,540.5 million, approximately 59% in twelve months | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:16 | CP-1A Operating model | Sourced | High | Verified |
| US Government approximately 23% of FY2025 revenue; no customer above 10% | source-text | 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S1 | page:9; page:86 | CP-1A Operating model | Sourced | High | Verified |
| Segment shares of FY2025 revenue 44%, 35%, 21% | source-text | 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S1 | pages:7 to 9 | CP-1A Operating model | Sourced | High | Verified |
| VACCO sold July 18, 2025; proceeds mainly used to pay down debt | source-text | 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S1 | page:32 | CP-1A Timeline | Sourced | High | Verified |
| Operating lease liabilities 50,260 and finance lease liabilities 15,396 | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:17 | CP-1 Claims outside debt | Sourced | High | Verified |
| Contract liabilities 288,142 on the balance sheet and USD 293.4 million in the note | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:3; page:16 | CP-1 Data quality | Conflicting | High | Difference unexplained; logged |
| Operating cash flow from continuing operations 193,377; discontinued operations (59,340) | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:3 | CP-1 Cash flow | Sourced | High | Verified |
| Contract liabilities up USD 71.5 million due to timing of customer payments | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:24 | CP-1 Cash flow quality | Sourced | High | Verified |
| Current portion wording: no contractual obligation (Q1) versus as obligated (Q3) | source-text | 10-Q_2025-12-31_ese-20251231x10q.htm.jsonl; 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S2, S4 | S2 page:9; S4 page:11 | CP-1A Conflicts | Conflicting | High | Logged, not reconciled |
| Maritime excluded from the ICFR audit scope | source-text | 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | S1 | page:56 | CP-1A Governance | Sourced | High | Verified |
| Interest expense includes about USD 7 million of Megger debt financing costs | source-text | 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | S4 | page:23 | CP-1 Cover | Sourced | High | Cash settlement not stated (CP5-001) |

#### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EBIT, LTM | CP-1 Financials | EBT 179,863 + interest expense, net 19,121 (USD thousands, LTM to June 30, 2026) | EBT + interest expense, net; LTM = FY2025 + nine months 2026 - nine months 2025 | Calculated | Supported: recomputed 198,984 | High | PD, debt service | 10-K page 57; 10-Q Q3 page 2 |
| EBITDA, LTM | CP-1, CP-2 | EBIT 198,984 + D&A 106,693 | EBIT + D&A; D&A LTM = 75,021 + 80,073 - 48,401 | Calculated | Supported: recomputed 305,677 | High | PD, leverage | 10-K page 59; 10-Q Q3 page 3 |
| Total debt / EBITDA, LTM | CP-1, CP-2 | Borrowings 85,000; EBITDA 305,677 | 85,000 / 305,677 = 0.278x; borrowings only, excludes leases and letters of credit | Calculated | Supported | High | PD, leverage tolerance | 10-Q Q3 page 10 |
| Net debt / EBITDA, LTM | CP-1, CP-2 | Borrowings 85,000 less cash 73,236 = 11,764; EBITDA 305,677 | 11,764 / 305,677 = 0.038x | Calculated | Supported | High | PD | 10-Q Q3 pages 2, 10 |
| EBITDA / cash interest, LTM | CP-1, CP-2 | EBITDA 305,677; interest paid 14,970 (17,421 + 13,587 - 16,038) | 305,677 / 14,970 = 20.42x | Calculated | Partially Supported: the denominator may include financing costs (CP5-001) | Medium | Debt service | 10-K page 59; 10-Q Q3 page 4 |
| Undrawn revolver, June 30, 2026 | CP-1, CP-2 | Commitment 500,000; drawn 45,000; letters of credit 12,700 | 500,000 - 45,000 - 12,700 = 442,300 | Calculated | Supported: equals the stated approximation | High | Liquidity | 10-Q Q3 pages 10, 11 |
| Liquidity, June 30, 2026 | CP-1, CP-2 | Cash 73,236 + undrawn 442,300 | Sum = 515,536 | Calculated | Supported | High | Liquidity | as above |
| Free cash flow, LTM (continuing, before dividends) | CP-1, CP-2 | CFO 305,474; capex 36,672; software 10,700 | 305,474 - 36,672 - 10,700 = 258,102; excludes discontinued operations outflow | Calculated | Supported with disclosed caveat | Medium | Cash conversion | 10-K and 10-Q Q3 page 3 |
| Illustrative leverage bound | CP-1, CP-2 | Borrowings 85,000 + cash consideration 900,000; ESCO-only LTM EBITDA 305,677 | 985,000 / 305,677 = 3.22x | Assumption-Based | Labelled Analyst Inference; omits Megger EBITDA, fees, cash used | Low | Leverage tolerance | 10-Q Q3 pages 10, 19 |
| LTM EBITDA at December 31 and March 31, 2026 | CP-1 chart data | Quarterly EBITDA from releases | 269,202 and 292,617 recomputed from FY2025 plus year-to-date minus prior year | Calculated | Supported | High | Trend | Release Q1 page 6; Release Q2 page 7 |
| Pro forma post-closing leverage and interest cover | CP-2 | Megger EBITDA, new debt drawn, pricing | Not calculable | Not Calculable from Provided Materials | Correctly marked upstream | Not assessed: no calculation exists | Leverage tolerance | none |

#### Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | LTM cash interest cover of 20.42x | CP-1 states the roughly USD 7 million of Megger financing costs "is not cash interest paid in this measure"; no source says this, and interest paid rose from USD 2,269 thousand in Q2 2026 to USD 8,629 thousand in Q3 2026 | Weak Lineage | If financing costs are inside interest paid, the denominator is overstated and cover understated; the conclusion that cover is "about twenty times" would be conservative | Restate as unknown or show both bases | CP-1 Chart data: interest cover; CP-2 Key findings |
| MINOR | Illustrative leverage bound 3.22x | Assumption-based figure in committee-facing prose | Assumption-Based | Could be misread as pro forma leverage | Keep the label and omitted inputs with every reuse | CP-1 Narrative review; CP-2 Key findings |
| MINOR | A&D carries most growth, is fastest-growing | Derivable from CP-1 segment table but not stated with figures | Analyst Inference | Supports the government concentration risk | Add the segment sales comparison or soften | CP-2 Key credit risks, Strengths and weaknesses |
| MINOR | Megger "will reset" debt, covenants and ownership | Closing not confirmed | Analyst Inference | Overstates certainty | Use "is expected to" | CP-2 Reader summary |
| MINOR | "mostly an undrawn $500 million revolver" | Undrawn amount is USD 442.300 million after USD 45 million drawn and USD 12.7 million of letters of credit | Weak Lineage | Imprecise description of a precise figure | Reword | CP-1 Financial base view |
| MINOR | Consideration components | 0.9 plus 1.4 is 2.3, against approximately 2.35 stated | Conflicting | Likely rounding but unexplained | Obtain the 8-K | CP-1A Conflicts |

#### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings cover the audited year and each quarter; executed agreements and Megger documents are absent (CP-0) | Terms that govern the largest change are untraceable | Covenant and post-closing conclusions are bounded | Supply the agreements and later filings |
| Citation completeness | Committee-Ready | Every quote in the four handoffs was found on its cited page; locators are page level | Page-level locators allow re-checking | Claims can be re-verified | None |
| Calculation traceability | Ready with Remediation | All derived figures recomputed from located inputs; one caveat on the cover denominator (CP5-001) | A wrong denominator misstates debt service | Cover may be understated | Correct the caveat |
| Assumption transparency | Committee-Ready | The only assumption-based figure is labelled and its omitted inputs listed | Reuse without the label would mislead | Low risk while labelled | Keep the label |
| Markdown/export artifact integrity | Ready with Remediation | Six run headings and required view headings present; no YAML envelope under the CP-OS transport | Downstream tools rely on headings | Hygiene only | Note the transport |

Overall auditability: Ready with Remediation (the lowest of the five dimensions).

#### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Covenant levels and definitions | Amended and Restated Credit Agreement of August 30, 2023 and Amendment No. 1 | Headroom and restricted payment capacity cannot be traced | CP-1 Covenants; CP-2 risks | High impact | The executed agreements |
| CP-5-GAP-002 | New Credit Facility terms | Credit Agreement dated May 29, 2026 (Exhibit 10.3, Form 8-K of June 3, 2026) | Post-closing pricing, covenants, collateral and amortisation unknown | CP-1A Transaction; CP-2 | High impact | The executed agreement |
| CP-5-GAP-003 | Megger documents | Share purchase agreement, shareholder agreement, 8-Ks of April 15 and 16, 2026 | Conditions, TBG AG rights and exact consideration | CP-1A; CP-2 | High impact | The 8-Ks with exhibits |
| CP-5-GAP-004 | Megger financials | Statements or pro forma information | Post-closing leverage and cover not calculable | CP-2 | High impact | Megger financial statements |
| CP-5-GAP-005 | Events after August 10, 2026 | Any later filing | Closing status and drawn debt at the as-of date | All modules | High impact | Later 8-Ks |
| CP-5-GAP-006 | Composition of interest paid | Split between continuing and discontinued operations and between interest and financing costs | Cover denominator | CP-1 Chart data: interest cover | Medium impact | Filed notes or cash flow detail |
| CP-5-GAP-007 | Contract liabilities difference | Reconciliation of the note total to the balance sheet caption | Reading of customer advances | CP-1 Cash flow quality | Medium impact | Filed HTML |
| CP-5-GAP-008 | Beneficial ownership and board | 2025 Proxy Statement | Control and alignment | CP-1A Governance | Medium impact | The proxy statement |
| CP-5-GAP-009 | Adjusted EBITDA for LTM | Fiscal Q4 2025 release | No adjusted leverage measure | CP-1 Definitions | Low impact | The release |
| CP-5-GAP-010 | Extraction fidelity | Original HTML and XBRL | Tables checked in text form only | All modules | Low impact | Filed HTML |

#### Handoff envelope and schema audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Envelope and headings | The Deploy V YAML front matter and the six Deploy V headings are not used; the CP-OS transport uses its six run headings and view headings instead, which are all present and in order | Record the transport adaptation; no repair of accepted answers | None for CP-OS; hygiene only |

#### Module input register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response, sha256 7f46d3b1dbdad4b468a5bdd5db37f408dc8a1ce57aba77ff195a116822899d17; run `ese-2026-11-05-credit_snapshot-host` | Source readiness for four consumers, Q3 2026 | High | Six run headings and Readiness view present | Passed: no issue logged against this handoff | Statuses READY_WITH_LIMITATIONS; all quotes verified |
| CP-1 | sha256 23a50d14b3104c2571d80147c88f81427457a9b11a2aa773f3459c4d026de1e7; same run | Financial base, FY2024 to LTM June 30, 2026, USD thousands | High | Six run headings, Financial base view and chart selectors present | Restricted: one Material (CP5-001) | Figures recomputed and matched |
| CP-1A | sha256 7bb2aa7585c6ae63abcfb32f227dd60a79e423f35bf4601e20c348a72e1bc24b; same run | Business, transaction, governance | High | Six run headings and Business and transaction view present | Passed: Minor issues only | Megger terms from management summary only |
| CP-2 | sha256 e297e9a788228578ae850f917d4e33d0c320993e352e7c8e80e8fca511818320; same run | Fundamental credit synthesis | High | Six run headings and Credit view present | Passed: Minor issues only | Figures taken unchanged from CP-1 |

Module Status: Ready with Limitations (all four handoffs available, executed legal documents and later filings absent). External sources: none used by the audited modules. Citation discipline: page-level locators with quoted text.

#### Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | "Liquidity of $515.536 million is mostly an undrawn $500 million revolver" (Financial base view) | Partially Supported | The commitment is USD 500 million but the undrawn amount is USD 442.300 million after drawings and letters of credit | Reword to the undrawn amount | Formatting / Hygiene Only |
| MINOR | CP-2 | A&D is the "fastest-growing" segment and carries "most growth" | Partially Supported | True on the segment sales table but not stated with figures in CP-1 or CP-1A | Add the comparison or soften | Monitoring Follow-Up |
| MINOR | CP-2 | Megger "will reset debt, covenants and ownership" (Reader summary) | Partially Supported | Closing is expected, not confirmed, at the as-of date | Use "is expected to" | Formatting / Hygiene Only |

#### Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1 (used in CP-2) | LTM EBITDA / interest paid of 20.42x | The statement that Megger financing costs are outside interest paid is unsupported; the denominator composition is unknown | Interest expense, net includes about USD 7 million of financing costs (10-Q Q3 page 23); interest paid is a total (10-Q Q3 page 4) | Restate as unknown or show both bases | Requires Calculation Rebuild |
| MINOR | CP-1, CP-2 | Illustrative total debt bound of 3.22x | Lacks Megger EBITDA, fees and cash used, so it is not a pro forma ratio | none | Keep the label and omitted inputs with every reuse | Restricts Committee Use |
| MINOR | CP-1A | Consideration of approximately USD 2.35 billion against USD 0.9 billion cash and approximately USD 1.4 billion equity | Components sum to 2.3, below the stated total | 10-Q Q3 page 19 states all three as approximate | Obtain the 8-K | Requires Source Reconciliation |

Definition drift check: EBITDA is EBIT plus D&A in CP-1 and CP-2 and matches the release "Consolidated EBITDA" for the nine months; net debt and total debt use borrowings only in both modules; no drift found.

#### Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Covenants are a leverage ratio and interest coverage ratio, and the company is in compliance | Executed Amended and Restated Credit Agreement and Amendment No. 1 | Types and compliance are management statements; levels and definitions absent. No headroom was inferred upstream | None to the analysis; obtain the agreement | Legal review needed before any covenant conclusion |
| MINOR | CP-1, CP-1A | Existing facility secured by guarantees of material US subsidiaries and a pledge of foreign subsidiary equity; New Credit Facility "senior secured" | Executed agreements | Security statement comes from the 10-K only; New Credit Facility security, guarantors and collateral absent | None to the analysis; obtain the agreements | Legal review needed |

#### Market and relative value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | None: the credit view makes no spread, price, rating or relative-value claim | Market prices, spreads and ratings (context blank) | Not needed for the minimum set | None; keep relative value out of the credit view | Relative value cannot be assessed from these materials |

#### Cross-module consistency audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Current portion of debt of USD 20.000 million: Q1 2026 says no contractual obligation, Q3 2026 says as obligated by the repayment terms | Text changed between filings; no amendment supplied | Obtain Amendment No. 1 and later amendments | Maturity profile reading; logged consistently in all three modules |
| MINOR | CP-0, CP-1 | Contract liabilities: note USD 293.4 million against balance sheet 288,142 thousand | Presentation difference, unexplained | Locate the reconciliation | Cash flow quality reading; logged consistently |

Cross-module checks that passed: issuer name and id, periods, EBITDA definition, total debt, liquidity and maturities agree between CP-1 and CP-2; segment shares and the Megger terms agree between CP-1A and CP-2; no module contradicts another.

#### Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Duplicative Content | The Megger gaps and covenant limitation are restated in several sections of each module | State each limitation once where it changes a conclusion | None beyond reading effort |

No promotional language was found beyond attributed management language in CP-1A, which is tagged.

#### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1 | Formula / Definition Drift | Unsupported statement that Megger financing costs are not in cash interest paid; cover denominator uncertain | Restate as unknown or show both bases | Requires Calculation Rebuild | Open |
| CP5-002 | MINOR | CP-1, CP-2 | Partially Supported Claim | Illustrative 3.22x bound lacks Megger EBITDA, fees and cash used | Keep the label with every reuse | Restricts Committee Use | Open |
| CP5-003 | MINOR | CP-1A | Conflicting Evidence | Consideration components sum to less than the stated total | Obtain the 8-K | Requires Source Reconciliation | Open |
| CP5-004 | MINOR | CP-1 | Partially Supported Claim | Description of liquidity as "mostly an undrawn $500 million revolver" | Reword | Formatting / Hygiene Only | Open |
| CP5-005 | MINOR | CP-2 | Partially Supported Claim | A&D "fastest-growing" not stated with figures upstream | Add the comparison or soften | Monitoring Follow-Up | Open |
| CP5-006 | MINOR | CP-2 | Partially Supported Claim | "will reset" debt, covenants and ownership | Use "is expected to" | Formatting / Hygiene Only | Open |
| CP5-007 | MINOR | CP-1, CP-2 | Legal Support Gap | Covenant types and compliance rest on management statements; levels absent | Obtain executed agreements | Requires Legal Review | Open |
| CP5-008 | MINOR | CP-1, CP-1A | Legal Support Gap | Security and guarantor statements from the 10-K only; New Credit Facility security absent | Obtain executed agreements | Requires Legal Review | Open |
| CP5-009 | MINOR | CP-1, CP-1A, CP-2 | Cross-Module Inconsistency | Current-portion wording differs between filings | Obtain amendments | Monitoring Follow-Up | Open |
| CP5-010 | MINOR | CP-0, CP-1 | Conflicting Evidence | Contract liabilities note against balance sheet caption | Locate the reconciliation | Monitoring Follow-Up | Open |
| CP5-011 | MINOR | CP-1, CP-1A, CP-2 | Duplicative / Immaterial Content | Caveats restated across sections | State each once | Formatting / Hygiene Only | Open |
| CP5-012 | MINOR | CP-0, CP-1, CP-1A, CP-2 | canonical Markdown Handoff Integrity Defect | Transport envelope differs from the Deploy V envelope | Record the adaptation | Formatting / Hygiene Only | Open |
| CP5-013 | MINOR | CP-2 | Market Data Gap | No market, rating or relative-value data exists or is claimed | Keep out of the credit view | Requires Market Data Refresh | Open |

## Calculations

The host recomputed every derived figure in the audited handoffs from located inputs. Inputs were re-read from the pinned text, and the key statement lines were also extracted by script and compared. All results are in USD thousands unless stated.

- EBIT = earnings before income taxes + interest expense, net. FY2025: 152,853 + 17,502 = 170,355. FY2024: 130,953 + 15,247 = 146,200. Nine months 2026: 120,296 + 13,992 = 134,288. Nine months 2025: 93,286 + 12,373 = 105,659. LTM: (152,853 + 120,296 - 93,286) + (17,502 + 13,992 - 12,373) = 179,863 + 19,121 = 198,984. Matches CP-1.
- EBITDA = EBIT + D&A. FY2025: 170,355 + 75,021 = 245,376. FY2024: 146,200 + 52,155 = 198,355. Nine months 2026: 134,288 + 80,073 = 214,361. Nine months 2025: 105,659 + 48,401 = 154,060. LTM: 245,376 + 214,361 - 154,060 = 305,677. Release Q3 page 7 shows 214,361 and 154,060. Matches CP-1.
- Total debt / EBITDA: 85,000 / 305,677 = 0.278x; 186,000 / 245,376 = 0.758x; 122,000 / 198,355 = 0.615x. Net debt / EBITDA: 11,764 / 305,677 = 0.038x; 84,650 / 245,376 = 0.345x; 56,037 / 198,355 = 0.283x. Matches CP-1.
- Interest cover: 305,677 / 14,970 = 20.42x; 245,376 / 17,421 = 14.09x; 198,355 / 14,535 = 13.65x. LTM interest paid: 17,421 + 13,587 - 16,038 = 14,970. Matches CP-1 arithmetic; the denominator caveat is CP5-001.
- Discrete interest paid used in CP5-001: Q2 2026 = 4,958 - 2,689 = 2,269 (10-Q Q2 page 4 and 10-Q Q1 page 3); Q3 2026 = 13,587 - 4,958 = 8,629 (10-Q Q3 page 4). The jump is consistent with, but does not prove, inclusion of the roughly USD 7 million of financing costs.
- Liquidity: 500,000 - 45,000 - 12,700 = 442,300; 73,236 + 442,300 = 515,536; at September 30, 2025: 500,000 - 25,000 - 10,100 = 464,900. Matches CP-1.
- Free cash flow: LTM 305,474 - 36,672 - 10,700 = 258,102. Operating cash flow LTM: 200,396 + 193,377 - 88,299 = 305,474. Matches CP-1.
- Illustrative bound: (85,000 + 900,000) / 305,677 = 3.22x. Matches CP-1; it is Assumption-Based.
- Consideration check: 0.9 + 1.4 = 2.3 billion against approximately 2.35 billion stated.
- Quote check: all quoted passages in the four handoffs were matched as exact substrings of the pinned text, apart from labels.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed credit agreements (existing and May 29, 2026) not supplied; covenant and structure claims cannot be traced to clauses | High | Committee use, CP-2 | Supply the agreements |
| Megger agreements and financials not supplied | High | Committee use | Supply the 8-Ks, exhibits and financials |
| No source after August 10, 2026 | High | All modules | Supply later filings or confirm none |
| Composition of interest paid (CP5-001) | Medium | CP-1, CP-2 | Obtain cash flow detail or restate the caveat |
| Contract liabilities reconciliation | Medium | CP-1 | Locate the explanation |
| Proxy statement, ratings and market data not supplied | Medium | CP-1A, CP-2 | Supply if required |
| Audit coverage: all quoted passages and figures checked; pages of sources not cited by any handoff were not read in full | Low | CP-5 | Re-audit if a downstream claim cites other pages |
| Confidence score is script-owned and was not computed here; only the rule-bound band is stated | Low | Delivery | Run the scoring script when available |

## Next module

- Delivery: the report may be assembled from CP-0, CP-1, CP-1A and CP-2 with committee use Restricted. Disclose CP5-001 with the 20.42x cover figure, keep the 3.22x bound labelled as an Analyst Inference, and carry the Not supplied items for covenant headroom, post-closing leverage and TBG AG's stake.
- Re-audit trigger: any of the executed credit agreements, the Megger documents, Megger financials or a filing after August 10, 2026 is added, or CP-1 is re-run with a corrected cover caveat.
