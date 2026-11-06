# CP-5 evidence trace and research integrity: MILLICOM INTERNATIONAL CELLULAR SA

## Request

Evidence trace and research-integrity audit of the source readiness, financial base, business and transaction context and credit synthesis for MILLICOM INTERNATIONAL CELLULAR SA as of 2026-11-05, pathway credit_snapshot, run tigo-2026-11-05-credit_snapshot-host, reporting periods Q3 2026 and FY2025, currency USD. Scope: Top 5 material credit drivers (default scope), with the research-integrity grade absorbed from the quality audit. This module changes no upstream conclusion; it audits, classifies and clears.

## Sources

### Issuer sources behind the audited handoffs

Each filing was re-opened to open the locators listed in the source lineage register below.


| Source file (exact name) | sha256 |
| --- | --- |
| 20-F_2025-12-31_tigo-20251231.htm.jsonl | 13be2a8c900b103376e04c45e18282d28f2b1aac3516bfaed99fc02cc0e15f37 |
| 6-K_2026-05-12_dp246578_6k.htm.jsonl | e31fa18185d3ceef7ba9e0133efc952dd4f43ccbd999e9a5f5b5af04d8dbf712 |
| 6-K_2026-08-06_dp251442_6k.htm.jsonl | 76b47ade3b6a5a2f060db2592b816c6ed584aa9ed405d036c0be893943dc1c51 |
| 6-K_2026-11-05_dp256407_6k.htm.jsonl | 6ab7c7e5e635829f16eb15a89301463e6131db3f5c0e68ee118ba6350801f894 |

The context file (sha256 34621752733871aa051ccd652227feabad1bb02852c10250971aa402ac335e7e) holds settings only and is not evidence.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 30231e20dd79cfa35c582673e23e65e617ff0d8fef136e9bbfd8bd339ed7d1e8 | Source readiness, audited as an input |
| CP-1 | 77360cbd8368dd54f4044c63fc9a5d94cd9bb6b03d46733b7253d1eb3eb1429c | Financial base, audited |
| CP-1A | e3856a654a2bfebe38f97f3f14b45a4cc61494b6a3d2e43b59ebbfadf28ec516 | Business and transaction context, audited |
| CP-2 | cffddc193423e19305ab4df3bad70036523f056e1661991b5674d45a225203ca | Credit synthesis, audited |

### Locator convention

Locators read `Sn page N`, where Sn is the source document id in the source register (S1 the 20-F, S2 the May 6-K, S3 the August 6-K, S4 the November 6-K) and N is the numbered text chunk of the pinned file, not the printed page. L-numbers refer to rows of the source lineage register. Issue IDs CP5-001 to CP5-009 refer to the consolidated issue log.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is largely traceable to the filings, but liquidity, legal protections and the funding of the acquisitions are not fully supported. Committee use is restricted, with no critical defect found. | Low | The mechanical confidence score is 5 of 100 because of two material and seven minor findings and a partial source gate. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of the five main credit drivers, two are directly sourced, one is calculated, one is an analyst inference and one rests on missing 2026 liquidity data. | Leverage and claims outside debt are well anchored; liquidity adequacy cannot be confirmed. | High |
| The credit view calls the acquisitions debt-funded, but the business context says sources and uses by deal are not supplied. | The funding mix of the acquisitions is unproven and the wording should be corrected before committee use. | High |
| Comments on structural subordination and creditor protection rely on filing summaries because no debt documents are supplied. | Ranking, guarantees and covenants need review of the actual documents. | High |
| Management leverage of 2.53x cannot be recomputed, and the plain trailing ratios of 2.32x and 2.14x use different inputs. | Leverage must always be quoted with its basis; neither version is pro forma for the acquisitions. | High |
| No critical defect was found; two material and seven minor issues remain. | Committee use is restricted until the material issues are fixed or disclosed. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 is calculated, 0 are assumption-based, 1 is an analyst inference, and 1 is a weak-lineage, untraced, conflicting, or insufficient-information item. The most important provenance gap is the absence of any 2026 statement of undrawn committed facilities, together with covenant levels and debt documents, which matters because liquidity adequacy and refinancing capacity cannot be tested for September 30, 2026 and implies that committee use of the liquidity and creditor-protection conclusions stays restricted until those documents are obtained.

The audit found no critical defect. Two material findings concern the "debt-funded" description of the acquisitions in the credit synthesis and the legal-review dependency of its structural comments; seven minor findings are listed in the issue log. The audited handoffs consume the same filings consistently, preserve the conflict on the Chile earn-out, and label management language and analyst interpretation.

### Audit summary

Module status: Ready with Limitations. Traceability scope: Top 5. Run id consumed: tigo-2026-11-05-credit_snapshot-host; reporting periods Q3 2026 (current) and FY2025 (prior); issuer id tigo; analysis date 2026-11-05. Confidence Score: 5 / 100 (Band: Insufficient Information), recomputed with the confidence-score script of the method (working shown under Calculations). qa_status: Restricted. committee_status: Restricted.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 20-F_2025-12-31_tigo-20251231.htm.jsonl | Primary filing; audited statements with KPMG LLP opinion for FY2025 and 2024 | FY2025, year ended December 31, 2025 | Millicom International Cellular S.A. and subsidiaries; Honduras joint venture equity-accounted | Audited statements, debt notes, ratings, liquidity text, ownership, business description | Year-end data only; subsequent events note covers January and February 2026 | Debt register, covenants, ratings, ownership in CP-1, CP-1A, CP-2 |
| S2 | 6-K_2026-05-12_dp246578_6k.htm.jsonl | Primary filing; unaudited, no review report | Three months to March 31, 2026 | Same group; Coltel from February 6, 2026 | Q1 statements and release | Unaudited; 2025 comparatives re-presented | March 31, 2026 balances in CP-1 |
| S3 | 6-K_2026-08-06_dp251442_6k.htm.jsonl | Primary filing; unaudited with KPMG Audit S.à r.l. review report | Six months to June 30, 2026 | Same group | H1 statements, Q2 release, guidance and dividend release | Review, not audit | June 30, 2026 balances and guidance in CP-1, CP-1A |
| S4 | 6-K_2026-11-05_dp256407_6k.htm.jsonl | Primary filing; unaudited, no review report | Nine months and Q3 to September 30, 2026 | Same group; Coltel since February 6, 2026; Uruguay and Ecuador since October 2025 | Statements, notes 1 to 16, Q3 release, reconciliations | Provisional acquisition accounting; no instrument-level debt table | Latest balances, net debt, cash flow and subsequent events in all modules |
| C1 | context/1 file for tigo | Settings file, not issuer evidence | Run settings, as of 2026-11-05 | Issuer identity only | Dates, currency, pathway, blank ratings, quotes and valuation | Blank fields are not zeros | Run parameters only |

Module Status: Ready with Limitations. Traceability Scope: Top 5. Missing required inputs: executed debt documents, rating-agency publications, market quotes. Entity-key status: issuer_id tigo available. Citation limitation: locators are text-chunk numbers, not printed pages. Research adoption: the context lists no research questions, so no research adoption rows apply.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage step-up after the 2025 and 2026 acquisitions | CP-1, CP-2 | Net debt 7,983 against 5,357 at year-end 2025; management leverage 2.53x against 2.17x | Higher leverage reduces tolerance for earnings or currency shocks and raises refinancing dependence | Bears on default risk, leverage tolerance and monitoring | L01, L02, L04, L29 | Management leverage not reproducible; not pro forma |
| 2 | Debt service capacity from operations | CP-1, CP-2 | Nine-month Adjusted EBITDA 2,958; cash interest including leases 648; equity free cash flow 867 against dividends 587 | Earnings cover interest and distributions, limiting near-term cash stress | Bears on debt service and distributions | L03, L10, L11, L12, L13, L14 | Non-IFRS measures; interim figures unaudited |
| 3 | Liquidity and refinancing visibility | CP-1, CP-2 | Cash 848 against 872 due within one year; revolving facility 565 undrawn at year-end 2025 | Cash is below one-year maturities, so rollover and the facility decide near-term liquidity | Bears on liquidity and refinancing | L05, L06, L07, L24 | 2026 facility status and covenant levels not supplied |
| 4 | Claims outside the debt figure | CP-1, CP-2 | Leases 3,190, capital expenditure payables 2,101, dividend payable 579, litigation and tax exposures | These are cash calls that rank beside debt service but sit outside net debt | Bears on real leverage and flexibility | L08, L09, L21, L28 | Nature of the payables increase not itemised |
| 5 | Shareholder distributions and sponsor behaviour | CP-1A, CP-2 | Dividend plan of 3.00 plus 1.50 per share; Niel Family Group 44.1%; no support commitment documented | Payouts compete with deleveraging and support willingness is untested | Bears on leverage tolerance and monitoring posture | L14, L15, L16, L27 | Debt-document limits on distributions not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage step-up | CP-1, CP-2 | S4 page 32 net debt table: Net Debt 7,983, Leverage 2.53x; S1 page 262 year-end 5,357 | Yes | High, management non-IFRS | Directly Sourced | Supported | High | Committee-Ready |
| Debt service capacity | CP-1, CP-2 | S4 page 42 finance charges 648; S4 page 34 Adjusted EBITDA 2,958; ratio 4.56x computed | Yes | High, non-IFRS inputs | Calculated | Supported | High | Committee-Ready |
| Liquidity and refinancing visibility | CP-1, CP-2 | S4 page 3 cash 848; S4 page 25 maturities; S1 page 255 facility at year-end 2025 only | Partial | High but dated for the facility | Insufficient Information | Partially supported | Low | Remediation Needed |
| Claims outside the debt figure | CP-1, CP-2 | S4 page 3 leases, payables, dividend payable; S4 pages 26 and 27 claims | Yes | High, unaudited | Directly Sourced | Supported | High | Committee-Ready |
| Distributions and sponsor behaviour | CP-1A, CP-2 | S4 page 20 dividends; S1 page 157 ownership; competition with deleveraging is the reading | Yes | High for facts, interpretive for the conclusion | Analyst Inference | Interpretation, tagged in CP-2 | Medium | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L01 Gross debt 8,648, derivatives and vendor financing 183, cash 848 and net debt 7,983 at Sep 30, 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 32 | CP-1 Balance sheet and net debt at period ends | Sourced | High: filed release, unaudited, non-IFRS net debt | Management definition of net debt |
| L02 Management leverage 2.53x at Sep 30, 2026, 2.76x at Mar 31, 2026 and 2.17x at Dec 31, 2025 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 32 | CP-1 Chart data: leverage; CP-2 Key findings | Sourced | High for the figure; management-defined | Pro forma inputs not printed |
| L03 Adjusted EBITDA 2,958 for nine months 2026 and 1,092 for Q3 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 34 | CP-1 Financials and credit metrics | Sourced | High: non-IFRS, post-IFRS 16 | Definition differs in wording from segment note |
| L04 Quarterly Adjusted EBITDA 776, 857, 1,009 and 1,092 for Q4 2025 to Q3 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 41 | CP-1 Calculations | Sourced | High: re-presented for discontinued operations | Feeds trailing sums |
| L05 Cash and cash equivalents 848; debt and financing 7,777 non-current and 872 current | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 3 | CP-1 Balance sheet and net debt at period ends | Sourced | High: unaudited interim statement | Rounds to 8,649 against 8,648 in the note |
| L06 Debt due within one year 872, in one to two years 986 and after five years 2,094 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 25 | CP-1 Chart data: debt maturities | Sourced | High: note 11B | Buckets sum to 8,647 |
| L07 Revolving credit facility of 600, with 565 extended to October 15, 2027, not drawn | source-text/20-F_2025-12-31_tigo-20251231.htm.jsonl | 20-F_2025-12-31_tigo-20251231.htm.jsonl | S1 | S1 page 255 | CP-1 Liquidity; CP-2 Key findings | Sourced | High but dated December 31, 2025 | No 2026 status in any filing searched |
| L08 Lease liabilities 2,846 non-current and 344 current at Sep 30, 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 3 | CP-1 Claims outside the debt figure | Sourced | High: unaudited interim statement | Sum 3,190 is calculated |
| L09 Payables and accruals for capital expenditure 1,644 non-current and 457 current; dividend payable 579 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 3 | CP-1 Claims outside the debt figure | Sourced | High: unaudited interim statement | Nature of the rise is not itemised |
| L10 Finance charges paid, net 648 for nine months 2026 including lease interest | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 42 | CP-1 Chart data: interest cover | Sourced | High: release reconciliation | Basis changed from the 20-F presentation |
| L11 Interest paid on debt 463, on leases 216 and interest received 31 for nine months 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 4 | CP-1 Reported cash flows | Sourced | High: unaudited cash flow statement | Includes discontinued operations |
| L12 Equity free cash flow 867 for nine months 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 31 | CP-1 Financials and credit metrics | Sourced | High: non-IFRS | Management definition |
| L13 Dividends paid to owners 587 for nine months 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 4 | CP-1 Reported cash flows | Sourced | High: unaudited cash flow statement | None |
| L14 FY2025 equity free cash flow 916, dividends paid 754 and share repurchases 119 | source-text/20-F_2025-12-31_tigo-20251231.htm.jsonl | 20-F_2025-12-31_tigo-20251231.htm.jsonl | S1 | S1 page 106, S1 page 197 | CP-2 Strengths | Sourced | High: audited statement and release table | EFCF is non-IFRS |
| L15 Niel Family Group holds 73,820,018 shares, 44.1%, on the 13D basis | source-text/20-F_2025-12-31_tigo-20251231.htm.jsonl | 20-F_2025-12-31_tigo-20251231.htm.jsonl | S1 | S1 page 157 | CP-1A Ownership and control | Sourced | High: 20-F, dated March 13, 2026 filing basis | Includes 3,350,000 shares expected to be bought |
| L16 AGM dividend of 3.00 per share in four installments and interim dividend of 1.50 per share | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 20 | CP-1A Governance and sponsor behaviour | Sourced | High: unaudited interim note | Capacity under debt documents not supplied |
| L17 Coltel contributed revenue of 1,127 and a net loss of 168 to September 30, 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 10 | CP-1A Credit translations; CP-2 Key findings | Sourced | High: unaudited note, provisional accounting | Purchase accounting provisional |
| L18 Segment Adjusted EBITDA for nine months 2026: Guatemala 737, Tigo Colombia 550, Coltel 409 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 17 | CP-1A Operating model; CP-2 Strengths and weaknesses | Sourced | High: segment note | Segments include Honduras and Chile at 100% |
| L19 Chile acquisition earn-out up to 490 in the November filing | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 11 | CP-1A Conflicts logged | Sourced | High: unaudited note | Conflicts with L20 |
| L20 Chile acquisition earn-out up to 150 in the annual report | source-text/20-F_2025-12-31_tigo-20251231.htm.jsonl | 20-F_2025-12-31_tigo-20251231.htm.jsonl | S1 | S1 page 297 | CP-1A Conflicts logged | Sourced | High: audited-period subsequent event note | Conflicts with L19 |
| L21 Guatemala settlement: expense 99, 31 paid, 68 outstanding over seven years | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 26 | CP-1 Claims outside the debt figure | Sourced | High: unaudited note | Outside debt |
| L22 Moody's Ba2 and Fitch BB+ at December 31, 2025 | source-text/20-F_2025-12-31_tigo-20251231.htm.jsonl | 20-F_2025-12-31_tigo-20251231.htm.jsonl | S1 | S1 page 273 | CP-1A Timeline; CP-2 Strengths | Sourced | High but dated | No 2026 rating action in the pack |
| L23 Operating-level debt of 4,470, 65% of 6,886, generally non-recourse to the holding company at Dec 31, 2025 | source-text/20-F_2025-12-31_tigo-20251231.htm.jsonl | 20-F_2025-12-31_tigo-20251231.htm.jsonl | S1 | S1 page 114 | CP-1 Debt register; CP-2 Key findings | Sourced | High for the statement; not a legal document | Structure needs indentures |
| L24 About 70% of gross debt at operating entities, 30% corporate; 61% local currency; average maturity 3.5 years | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 32 | CP-1 Debt register; CP-2 Strengths | Sourced | High: release narrative | Management narrative |
| L25 No breaches of financial covenants at December 31, 2025 | source-text/20-F_2025-12-31_tigo-20251231.htm.jsonl | 20-F_2025-12-31_tigo-20251231.htm.jsonl | S1 | S1 page 258 | CP-1 Covenants | Sourced | High but dated | Covenant levels not supplied |
| L26 Foreign exchange and other effects 18.6% and organic growth 5.4% of service revenue growth in Q3 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 41 | CP-2 Key findings | Sourced | High: release reconciliation | Management reconciliation |
| L27 Management guidance: 2026 equity free cash flow around 1.1 billion and year-end leverage below 2.5x | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 29 | CP-1A Timeline; CP-2 Strengths | Management language | Medium: forward-looking statement | Attributed to management |
| L28 Litigation claims 217 with provisions 91; tax exposure 378 with provisions 60 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 26, S4 page 27 | CP-1 Claims outside the debt figure | Sourced | High: unaudited note | Outside debt |
| L29 Coltel assumed other debt and financing 1,424 and lease liabilities 515 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 9 | CP-1A Transaction register; CP-2 Key findings | Sourced | High: provisional fair values | Provisional |
| L30 Postpaid subscribers 17,194 thousand at Q3 2026 | source-text/6-K_2026-11-05_dp256407_6k.htm.jsonl | 6-K_2026-11-05_dp256407_6k.htm.jsonl | S4 | S4 page 33 | CP-2 Strengths | Sourced | High: KPI table | KPIs exclude the Honduras joint venture |

Every row was checked by opening the cited page and confirming the figures and wording.

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 Trailing Adjusted EBITDA to Sep 30, 2026 | CP-1 Chart data: leverage | Q4 2025 776, Q1 2026 857, Q2 2026 1,009, Q3 2026 1,092 (L04) | 776 + 857 + 1,009 + 1,092 = 3,734; USD millions, four quarters to Sep 30, 2026; not pro forma for Coltel | Calculated | Reproduced | High | Leverage | L04 |
| C2 Total debt / EBITDA and net debt / EBITDA, Q3 2026 | CP-1 Chart data: leverage; CP-2 Key findings | Gross debt 8,648; net debt 7,983; C1 (L01) | 8,648 / 3,734 = 2.32x; 7,983 / 3,734 = 2.14x; excludes leases | Calculated | Reproduced | High | Leverage, refinancing | L01, L04 |
| C3 Management leverage 2.53x | CP-1, CP-2 | Net debt over LTM Adjusted EBITDA less right-of-use depreciation and lease interest, pro forma for acquisitions (S4 page 40) | Pro forma and lease inputs are not printed | Not Calculable (inputs not printed) | Not reproducible | Low | Leverage | L02 |
| C4 Cash interest cover including leases, nine months 2026 | CP-1 Chart data: interest cover; CP-2 | Adjusted EBITDA 2,958; finance charges paid, net 648 (L03, L10) | 2,958 / 648 = 4.56x; period nine months 2026; debt 463 plus leases 216 less received 31 | Calculated | Reproduced | High | Debt service | L03, L10, L11 |
| C5 Cash interest cover excluding lease interest, nine months 2026 | CP-1; CP-2 | 2,958; 463 less 31 (L11) | 2,958 / 432 = 6.85x | Calculated | Reproduced | High | Debt service | L03, L11 |
| C6 Lease liabilities | CP-1 Claims; CP-2 | 2,846 and 344 (L08) | 2,846 + 344 = 3,190 | Calculated | Reproduced | High | Leverage | L08 |
| C7 Net financing obligations | CP-1 Claims | Net debt 7,983 and C6 | 7,983 + 3,190 = 11,173 | Calculated | Reproduced | High | Leverage | L01, L08 |
| C8 Total debt plus leases / EBITDA | CP-1; CP-2 | 8,648; 3,190; 3,734 | (8,648 + 3,190) / 3,734 = 3.17x | Calculated | Reproduced | Medium | Leverage | L01, L08, L04 |
| C9 Cash less debt due within one year | CP-1 Liquidity; CP-2 | Cash 848; 872 (L05, L06) | 848 - 872 = -24 | Calculated | Reproduced | High | Liquidity | L05, L06 |
| C10 Distribution cover, nine months 2026 and FY2025 | CP-2 Calculations | 867 and 587 (L12, L13); 916, 754 and 119 (L14) | 867 - 587 = 280; 916 - (754 + 119) = 43 | Calculated | Reproduced | High | Debt service, distributions | L12, L13, L14 |
| C11 Combined Colombian Adjusted EBITDA | CP-1A; CP-2 | 550 and 409 (L18) | 550 + 409 = 959 against 737 | Calculated | Reproduced | High | Concentration | L18 |
| C12 Change in gross and net debt since year-end 2025 | CP-2 Calculations | 8,648 and 7,983 (L01); 6,886 and 5,357 (S4 page 32 and S1 page 262) | 1,762 (25.6%) and 2,626 (49.0%) | Calculated | Reproduced | High | Leverage | L01 |
| C13 Debt bridge for the leverage step-up (audit recomputation) | Not shown in CP-2 | Year-end gross debt 6,886; Coltel assumed debt 1,424 (L29); nine-month proceeds 1,131 less repayments 999 (S4 page 4) | 6,886 + 1,424 + 132 = 8,442 against 8,648; residual 206 not itemised | Calculated | Partially explained | Medium | Leverage, refinancing | L01, L29 |
| C14 Assumptions register | CP-0, CP-1, CP-1A, CP-2 | None: no forecast or scenario assumption appears in any audited module | Not applicable: balances are used as filed | Assumption-Based (none used) | No assumption to test | High | Monitoring | No assumption to trace |

Metric-definition drift flagged: management leverage and the plain trailing ratios use different numerators and denominators (CP5-004); Adjusted EBITDA is defined with slightly different wording in the segment note and the release (S4 page 18 and page 40); the FY2025 row uses audited 2,749 while quarter sums use re-presented quarters.

#### T5B.6 Missing citation and weak-lineage flags

These flags are the lineage view of the issues in the consolidated issue log (T5.9) and are not counted twice.

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 describes the expansion as debt-funded | Claim is not supported by sources and uses, which CP-1A records as not supplied; cash fell from 1,552 to 848 while net borrowing was 132 (CP5-001) | Weak Lineage | If the acquisitions were largely cash and operating-cash-flow funded, the credit view mislabels the leverage mechanism and the refinancing need | Reword or obtain sources and uses | CP-2 Credit view and Strengths and weaknesses |
| MATERIAL | Holding-company creditors depend on upstream cash and cannot test priming | Mechanism rests on a filing summary of non-recourse debt; no indenture or guarantee text (CP5-002) | Analyst Inference | Ranking and guarantor terms decide loss given default, which cannot be judged without the documents | Obtain the indentures and credit agreements; mark legal review required | CP-2 Key credit risks |
| MATERIAL | Liquidity is adequate or inadequate for the next twelve months | Total liquidity is not calculable because 2026 undrawn facilities are Not supplied; the gap is disclosed with a limitation flag, so it is not an orphan claim | Insufficient Information | Cash is below one-year maturities and the facility matures October 15, 2027, so the liquidity view is unconfirmed | Obtain 2026 facility status | CP-1 Liquidity; CP-2 Key findings |
| MINOR | Leverage step-up caused by acquired debt and local-currency borrowing | Bridge not shown; residual 206 (CP5-003) | Calculated | Mechanism is only partly evidenced | Show the bridge | CP-2 Key findings |
| MINOR | Management leverage 2.53x | Not reproducible; own-basis ratios differ (CP5-004) | Insufficient Information | Quoting one basis without the other can mislead | Quote both with basis | CP-1 and CP-2 |
| MINOR | Chile earn-out of 150 or 490 | Two filings give different caps; both logged in CP-1A | Conflicting | Contingent exposure cannot be sized, but it is without recourse and the conflict is preserved | Obtain the agreement | CP-1A Conflicts logged |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Four filings cover year-end 2025 and three 2026 interim dates; no debt documents, ratings or quotes (T5B.1) | Missing documents leave ranking, guarantees, covenants and facility availability unverified | Committee conclusions on creditor protection and liquidity stay restricted | Obtain indentures, credit agreements, rating reports |
| Citation completeness | Ready with Remediation | All 30 lineage statements open to a located page; CP-2 cites upstream sections by design; two claims lack a primary basis (CP5-001, CP5-002) | Unsupported wording could be repeated by readers | Funding mix and legal ranking are not evidenced | Reword and flag legal review |
| Calculation traceability | Ready with Remediation | 11 of the recomputed calculations reproduce; management leverage is not reproducible; one bridge is incomplete (T5B.5) | Two leverage bases may be conflated | Leverage tolerance could be misread | Quote basis; request pro forma bridge |
| Assumption transparency | Committee-Ready | No forecast assumptions are used; analyst interpretation is tagged in CP-1A and CP-2 | Hidden assumptions are absent | No assumption risk to the credit view | None |
| Markdown/export artifact integrity | Ready with Remediation | Six CP-OS headings and report selectors present; no YAML envelope or lineage filename under the transport (CP5-009) | Downstream tools expecting a YAML envelope would not find one | No credit effect; ingestion relies on CP-OS paths | Document the transport substitution |

Overall auditability, as the lowest of the five dimensions: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Undrawn committed facilities and letters of credit at September 30, 2026 | Revolving credit agreement amendments; 2026 liquidity statement | Liquidity and refinancing capacity cannot be sized | CP-1 Liquidity; CP-2 Key findings | High impact | Credit agreement and company liquidity disclosure |
| CP-5-GAP-002 | Covenant levels, definitions and compliance after year-end 2025 | Financing documents; covenant certificates | Headroom and leverage tolerance cannot be tested | CP-1 Covenants; CP-2 Key credit risks | High impact | Credit agreements and indentures |
| CP-5-GAP-003 | Guarantor, security and ranking terms for notes and loans | Indentures and guarantee documents | Structural ranking and loss given default cannot be assessed | CP-2 Key credit risks | High impact | Indentures |
| CP-5-GAP-004 | Sources and uses of the 2025 and 2026 acquisitions | Transaction agreements; company funding disclosure | The funding mix of the acquisitions is unproven | CP-2 Credit view; CP-1A Transaction register | Medium impact | Share purchase agreements; financing notes |
| CP-5-GAP-005 | Pro forma trailing Adjusted EBITDA and management leverage workings | Management bridge | Leverage is shown on two non-comparable bases | CP-1 Chart data: leverage; CP-2 | Medium impact | Management bridge |
| CP-5-GAP-006 | Ratings after December 31, 2025 and any market quotes | Agency publications; market data | Rating drift and relative value are outside the run | CP-2 Strengths | Medium impact | Rating agencies; market data vendor |
| CP-5-GAP-007 | Current shareholdings after June 30, 2026 and any support arrangements | Schedule 13D updates; shareholder agreements | Support willingness is untested | CP-1A Ownership; CP-2 Key findings | Low impact | Schedule 13D |
| CP-5-GAP-008 | Coltel and Ecuador purchase accounting still provisional | Final purchase price allocation | Balances and ratios may be revised | CP-1 Perimeter; all modules | Low impact | Next interim filing |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | CP-0 handoff sha256 30231e20dd79cfa35c582673e23e65e617ff0d8fef136e9bbfd8bd339ed7d1e8; run tigo-2026-11-05-credit_snapshot-host | Source readiness for four filings | Primary filings, mixed audit status | Six CP-OS H2 headings present; YAML envelope not used under the Markdown transport | Not previously audited | Status READY_WITH_LIMITATIONS; conflicts and gaps logged |
| CP-1 | CP-1 handoff sha256 77360cbd8368dd54f4044c63fc9a5d94cd9bb6b03d46733b7253d1eb3eb1429c; same run | Financial base to September 30, 2026 | Primary filings | Six H2 headings and report selectors present; no YAML envelope | Not previously audited | Locators on each table row |
| CP-1A | CP-1A handoff sha256 e3856a654a2bfebe38f97f3f14b45a4cc61494b6a3d2e43b59ebbfadf28ec516; same run | Business, ownership, transactions, governance | Primary filings with verbatim quotes | Six H2 headings and report selectors present; no YAML envelope | Not previously audited | Second attempt after selector rejection |
| CP-2 | CP-2 handoff sha256 cffddc193423e19305ab4df3bad70036523f056e1661991b5674d45a225203ca; same run | Credit synthesis from CP-1 and CP-1A | Upstream handoffs only | Six H2 headings and report selectors present; no YAML envelope | Not previously audited | Cites upstream sections, not locators, by method |

Module Status (quality audit gate): Ready with Limitations.

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 (with CP-1A) | Credit view and Weakness 1: the expansion is debt-funded | Partially Supported | CP5-001: CP-1A records sources and uses by deal as not supplied, and the November cash flow shows acquisition cash of 924 against net borrowing of 132 (1,131 raised less 999 repaid) while cash fell from 1,552 to 848 (S4 page 4); debt rose mainly through assumed Coltel debt of 1,424 (S4 page 9) | Reword as acquisition-led growth with debt assumed and higher borrowing, or obtain sources and uses | Requires Source Reconciliation |
| MINOR | CP-2 | Key finding 1: acquired debt and local-currency borrowing drove the increase | Partially Supported | CP5-003: no bridge is shown; 6,886 + 1,424 + 132 = 8,442 against 8,648, leaving 206 not itemised | Show the bridge and label the residual | Monitoring Follow-Up |
| MINOR | CP-2 | Strength 1: operates in twelve countries | Partially Supported | CP5-005: the count includes the Honduras joint venture and the Chile associate, which are equity-accounted and outside group revenue, debt and EBITDA | Say that two of the twelve are equity-accounted | Monitoring Follow-Up |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | CP5-004: leverage appears as 2.53x (management), 2.32x (total debt) and 2.14x (net debt) | Management leverage deducts right-of-use depreciation and lease interest and is pro forma; the plain ratios do not; the FY2025 row uses audited 2,749 while quarter sums use re-presented quarters totalling 2,740 for 2025 | No source conflict; inputs for management leverage are not printed | Always quote basis; request the management bridge before any leverage covenant comparison | Requires Calculation Rebuild |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 | CP5-002: holding-company creditors depend on upstream cash and cannot test priming or release permissions; operating-level debt is generally non-recourse; guarantors not supplied | Indentures, credit agreements and guarantee documents; clause-level support | Only a filing summary (S1 page 114, page 116) and a guarantee total of 629 (S1 page 258) are available | Mark the comment as interpretation requiring legal review; do not infer ranking | Legal review required before committee use |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | CP5-007: no market, price, spread, yield, peer or relative-value claim is made; ratings are quoted only as of December 31, 2025 | Market quotes, spreads, yields, peers and any 2026 rating action [Market Data Not Provided] | Context quotes, ratings and peers fields are blank, so current relative value cannot be assessed in this run | Obtain market data and agency publications before any relative-value work | Requires Market Data Refresh |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 | CP5-006: CP-0 records the 9 difference between operating cash flow of 2,028 (cash flow statement) and 2,019 (release) as unexplained; CP-1 attributes 6 to discontinued operations (S4 page 16), leaving 3 | CP-1 corrects CP-0; the accepted CP-0 handoff cannot be edited | Use the CP-1 statement and treat CP-0 as superseded on this point | Consumers must read CP-1 for cash flow reconciliation |

Other shared data points agree across modules: issuer name, net debt 7,983, gross debt 8,648, management leverage 2.53x, cash 848, the 565 revolving facility extended to October 15, 2027, the Niel Family Group 44.1% and the Chile earn-out conflict.

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Duplicative / Immaterial Content | CP5-008: the liquidity and documentation caveats are restated in the reader summary, credit view, key findings, weaknesses, risks and gaps, and the adjectives sound, strong and comfortably are used, although each is supported by figures | State each limitation once and replace adjectives with the figures | Dilutes the message; no effect on conclusions |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | YAML front-matter envelope and [IssuerID]_[ModuleID]_[date] filename | CP5-009: the CP-OS Markdown transport uses six H2 headings and CP-OS-owned paths and hashes instead of a YAML envelope, confidence fields and lineage filenames | Record the transport substitution; no change inside CP-OS | None inside CP-OS; external tools expecting the YAML envelope would need an adapter |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-2, CP-1A | Partially Supported Claim | Expansion described as debt-funded although sources and uses are not supplied and cash fell by 704 | Reword or document funding | Requires Source Reconciliation | Open |
| CP5-002 | MATERIAL | CP-2 | Legal Support Gap | Structural subordination and creditor-protection comments rest on filing summaries with no legal documents | Flag legal review; obtain documents | Requires Legal Review | Open |
| CP5-003 | MINOR | CP-2 | Partially Supported Claim | Leverage step-up attribution lacks a bridge; 206 residual | Show bridge | Monitoring Follow-Up | Open |
| CP5-004 | MINOR | CP-1, CP-2 | Formula / Definition Drift | Management leverage 2.53x not reproducible; plain ratios 2.32x and 2.14x use other inputs and mixed period bases | Quote basis; obtain pro forma bridge | Requires Calculation Rebuild | Open |
| CP5-005 | MINOR | CP-2 | Entity / Perimeter Mismatch | Twelve-country count includes two equity-accounted entities | Clarify perimeter | Monitoring Follow-Up | Open |
| CP5-006 | MINOR | CP-0, CP-1 | Version Conflict | Operating cash flow gap of 9 is unexplained in CP-0 and partly explained in CP-1 | Use CP-1 statement | Requires Source Reconciliation | Open |
| CP5-007 | MINOR | CP-1, CP-1A, CP-2 | Market Data Gap | No quotes, spreads, peers or 2026 ratings supplied | Obtain before relative-value work | Requires Market Data Refresh | Open |
| CP5-008 | MINOR | CP-2 | Duplicative / Immaterial Content | Caveats repeated across sections; generic adjectives | Trim | Formatting / Hygiene Only | Open |
| CP5-009 | MINOR | CP-0, CP-1, CP-1A, CP-2 | canonical Markdown Handoff Integrity Defect | No YAML envelope or lineage filename under the CP-OS transport | Record substitution | Formatting / Hygiene Only | Open |

#### Remediation priority map

Must-fix before committee: CP5-001 (reword the debt-funded description, or document sources and uses) and CP5-002 (mark the structural comments as interpretation requiring legal review and obtain the indentures and credit agreements). The accepted CP-2 handoff cannot be replaced inside this run, so these corrections are recorded here and must be carried into any use of CP-2.

Must-fix before the canonical Markdown handoff is consumed downstream: None.

Monitoring follow-up: CP5-003 (debt bridge), CP5-004 (pro forma leverage bridge), CP5-006 (use the CP-1 cash flow reconciliation) and CP5-007 (market data and 2026 ratings).

Formatting / hygiene: CP5-005 (perimeter wording), CP5-008 (repetition and adjectives) and CP5-009 (transport substitution).

#### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 7. Committee Use: Restricted.

No critical defect changes the credit conclusion, but the credit synthesis describes the acquisitions as debt-funded without support (CP5-001) and comments on structural ranking without legal documents (CP5-002). Both must be disclosed or corrected for committee use, and the liquidity conclusion remains unconfirmed until 2026 facility data are supplied.

## Calculations

Audit recomputations of the upstream figures are in register T5B.5 (C1 to C14). The confidence score was computed with the method script, which owns the arithmetic.


| Calculation | Inputs | Result |
| --- | --- | --- |
| E: mean strongest lineage weight over the five material claims | Directly Sourced 2 at 1.0, Calculated 1 at 0.9, Analyst Inference 1 at 0.4, Insufficient Information 1 at 0.0 | (2.0 + 0.9 + 0.4 + 0.0) / 5 = 0.66, so E = 66 |
| C: required registers present | 17 of 17 required registers (T5B.1 to T5B.8 and T5.1 to T5.9) | C = 100 |
| S: source gate | Source readiness status READY_WITH_LIMITATIONS, so the gate is partial | S = 0.7 |
| P: findings penalty | 2 MATERIAL at 15 and 7 MINOR at 3 | P = 30 + 21 = 51 |
| Score | (0.6 x 66 + 0.4 x 100) x 0.7 - 51 | raw 4.72, score 5, band Insufficient Information, qa_status Restricted (a Material finding caps the score at 59 and sets Restricted) |
| Debt bridge | 6,886 + 1,424 + 132 | 8,442 against 8,648 printed; residual 206 |
| Cash decline, nine months 2026 | 1,552 - 848 | 704 |

## Gaps

Gaps are listed in register T5B.8 and the issue log T5.9. The ones that restrict committee use are the missing 2026 facility and covenant data (CP-5-GAP-001, CP-5-GAP-002), the missing debt documents (CP-5-GAP-003) and the unsupported funding description (CP-5-GAP-004). The context lists no research questions, so no research adoption applies.

## Next module

This is the last selected module of the run; the report assembles from the accepted handoffs. Before committee use, apply the two material corrections above to any use of the credit synthesis, obtain the 2026 revolving facility status, covenant certificates and the indentures, and re-run the audit on a new run folder if the upstream handoffs are revised.
