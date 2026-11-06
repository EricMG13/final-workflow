## Request

Subject: Millicom International Cellular S.A. (issuer id tigo; "MIC S.A."). As-of date: 2026-11-05 (cutoff 2026-11-05). Module: CP-5, evidence trace validator with the absorbed research-integrity QA phase, pathway credit_snapshot, run id tigo-2026-11-05-credit_snapshot-host, creditor perspective.

Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most? Scope: Top 5 material credit drivers from the accepted CP-1, CP-1A and CP-2 handoffs, plus the integrity audit of CP-0, CP-1, CP-1A and CP-2. Every figure below was re-checked against the converted source text by this module; the upstream conclusions are not altered and nothing is repaired silently. Findings use the severity scale CRITICAL, MATERIAL, MINOR only. Locator convention: "chunk N" is the `page` field of the named converted-text file; source labels are 20-F = 20-F_2025-12-31_tigo-20251231.htm.jsonl, Q1 6-K = 6-K_2026-05-12_dp246578_6k.htm.jsonl, Q2 6-K = 6-K_2026-08-06_dp251442_6k.htm.jsonl, Q3 6-K = 6-K_2026-11-05_dp256407_6k.htm.jsonl.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 |
| --- | --- |
| 20-F_2025-12-31_tigo-20251231.htm.jsonl | 13be2a8c900b103376e04c45e18282d28f2b1aac3516bfaed99fc02cc0e15f37 |
| 6-K_2026-05-12_dp246578_6k.htm.jsonl | e31fa18185d3ceef7ba9e0133efc952dd4f43ccbd999e9a5f5b5af04d8dbf712 |
| 6-K_2026-08-06_dp251442_6k.htm.jsonl | 76b47ade3b6a5a2f060db2592b816c6ed584aa9ed405d036c0be893943dc1c51 |
| 6-K_2026-11-05_dp256407_6k.htm.jsonl | 6ab7c7e5e635829f16eb15a89301463e6131db3f5c0e68ee118ba6350801f894 |

Run context (settings only, not issuer evidence): context, sha256 5b145622a49a1e38ec7885504ac944230be02601fefa1d2f3fb7d83ded83c956.

### Supplied handoffs

| Module | sha256 | Status |
| --- | --- | --- |
| CP-0 | 533a512a1f3bb7bc99ba007a510cec3fdee3aeab214040d4ea601266e7a3d9fd | Accepted; source readiness, consumers rated READY_WITH_LIMITATIONS |
| CP-1 | fe7d99399cef5dd86595e652b06e9adc0c0e7978006654d0393d9f885e47b23a | Accepted; financials and credit metrics |
| CP-1A | 8596dd7e17ec172b37486bf546dcfb005f6c7a6bd1a2256b504f11f560848eb5 | Accepted; business, transaction and behaviour fact pack |
| CP-2 | 603db548e62408a5ed9e37184469d36bae45df07ee1234514b18493d6ce902ab | Accepted; fundamental credit synthesis (second attempt) |

## Findings

### Traceability conclusion

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 is calculated, 0 are assumption-based, 2 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of covenant terms, indentures and an instrument-level debt schedule after December 31, 2025, which matters because distribution capacity, liquidity headroom and priming protection cannot be traced to a source and implies that committee use is Restricted until those documents are obtained. No CRITICAL finding was raised; the MATERIAL findings are listed in the issue log. QA status: Restricted. Committee status: Restricted.

### Re-performance summary

Every figure in the Top 5 drivers and in the CP-1 table that was tested against the converted source text was found at its cited chunk with the stated value (77 figure checks run; 73 found at the cited chunk, and the four that were not matched at the first attempted chunk were located at the adjacent chunk of the same statement or were wording differences, none with a different value). The quarter-sum, net debt and maturity tie-outs are in Calculations. Differences found are rounding differences inside the sources or source-to-source differences already logged by CP-1, CP-1A and CP-2, plus the cross-module items in the issue log.

### Source register (T5B.1)

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-20F | 20-F_2025-12-31_tigo-20251231.htm.jsonl | High: audited annual report filed March 24, 2026 | Year ended December 31, 2025 (and 2024, 2023) | Millicom International Cellular S.A. consolidated; Honduras joint venture equity-accounted | Statements, debt note C.3, covenant statement, ownership, related parties, business description | Not re-presented for 2026 discontinued operations; December 31, 2025 balance sheet later restated; no covenant thresholds | CP-1, CP-1A, CP-2 |
| SRC-Q1 | 6-K_2026-05-12_dp246578_6k.htm.jsonl | Medium to High: unaudited statements and management release, no review report | Three months ended March 31, 2026 | Same consolidated group; Coltel from February 6, 2026 | Statements, maturity analysis, net debt and leverage at March 31, 2026, Q1 EFCF | Unreviewed; non-IFRS release measures are management claims | CP-1, CP-1A |
| SRC-Q2 | 6-K_2026-08-06_dp251442_6k.htm.jsonl | High: half-year report with a KPMG Audit S.à r.l. review conclusion (chunk 8) | Six months ended June 30, 2026 | Same consolidated group | Statements, maturity analysis, derivatives, litigation note, Q2 release | 2025 comparative income-statement columns marked "Not reviewed" (chunk 8) | CP-1, CP-1A |
| SRC-Q3 | 6-K_2026-11-05_dp256407_6k.htm.jsonl | Medium to High: unaudited statements and management release dated November 5, 2026 | Nine months and quarter ended September 30, 2026 | Same consolidated group | Statements, notes 1 to 16, release, reconciliations, KPIs | Unreviewed; provisional purchase accounting for Coltel and Ecuador | All modules |
| SRC-CTX | context (tigo.json) | Settings only, not issuer evidence | Run dated 2026-11-05 | Issuer identity fields | Ratings, quotes, deal terms, peers and assumptions all blank | Blank fields are not zero | Scope only |

### Top 5 material credit drivers (T5B.2)

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Net debt and management leverage after the Colombian consolidation: net debt 7,983, leverage 2.53x at September 30, 2026 against 2.17x at December 31, 2025 | CP-1, CP-2 | Release debt tables and balance sheet | Leverage drives default risk and refinancing tolerance; the denominator is management-defined | Sets the leverage view; target of below 2.5x is a management claim | Q3 6-K chunk 32; Q1 6-K chunk 25; Q3 6-K chunk 40 (definition) | Ratio cannot be reproduced from supplied tables; lease liabilities 3,190 sit outside it |
| 2 | Debt service coverage and cash generation: nine-month Adjusted EBITDA 2,958, interest on bonds and bank financing 472, equity free cash flow 867 | CP-1, CP-2 | Statements, release reconciliations, CP-1 Calculations 6 and 8 | Determines debt service capacity ahead of leases, spectrum, taxes and dividends | Supports debt service view on the reported period | Q3 6-K chunks 25, 31, 34, 41, 42 | Perimeter not pro forma; non-IFRS measures |
| 3 | Near-term liquidity and refinancing: cash 848 against debt due within one year 872; revolving credit facility of 600 due October 2027; 2027 SEK note | CP-1, CP-2 | Balance sheet, maturity ladder, 20-F material contracts | Cash does not cover current maturities, so liquidity depends on market and bank access | Monitoring posture and facility confirmation | Q3 6-K chunks 3, 25; 20-F chunks 124, 255, 272 | Facility availability and covenant terms not supplied |
| 4 | Acquisition-driven earnings base and Colombian integration: Coltel net loss since acquisition, restructuring above Adjusted EBITDA | CP-1A, CP-2 | Notes 3, 5 and the one-off summary | Perimeter, not organic growth, explains most of the growth; integration costs consume cash | Durability and margin resilience view | Q3 6-K chunks 9, 10, 41 | Pro forma Coltel Adjusted EBITDA not supplied; accounting provisional |
| 5 | Control, related-party exposure and distribution policy: Atlas about 42.2 percent, payable to Iliad Holding Group 195, dividends | CP-1A, CP-2 | 20-F ownership and related-party notes, dividend note 7 | Distributions and related claims compete with creditors for cash | Sponsor alignment and leakage monitoring | 20-F chunks 157-158, 295-296; Q3 6-K chunk 20 | Indentures and restricted payment terms not supplied; nature of the 195 payable not stated |

### Traceability map (T5B.3)

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net debt 7,983 and leverage 2.53x | CP-1, CP-2 | Release table row "Net Debt* 7,983 8,075 7,609 5,357 4,627" and "Leverage* 2.53x 2.73x 2.76x 2.17x 2.09x" (Q3 6-K chunk 32) | Yes | Medium to High (management non-IFRS measure in a filed release) | Directly Sourced | Management Language for the ratio; Documentary Fact for the figures | Medium | Committee-Ready |
| Coverage 6.27x and 4.20x; equity free cash flow after dividends 280 | CP-1, CP-2 | Statement and release figures (Q3 6-K chunks 25, 31, 4) with arithmetic in CP-1 Calculations 6 and 8 | Yes | High for statements | Calculated | Calculation | Medium | Committee-Ready |
| Liquidity depends on refinancing access | CP-1, CP-2 | Cash 848 and current debt 872 (Q3 6-K chunks 3, 25); revolving facility (20-F chunk 124) | Yes | High for balances; facility status not located | Analyst Inference | Analyst Interpretation | Medium | Remediation Needed |
| Growth is acquisition-driven and Colombian integration is a risk | CP-1A, CP-2 | Notes 3, 5 and release organic growth rows (Q3 6-K chunks 9, 10, 41) | Yes | High for notes, Medium for release | Directly Sourced | Documentary Fact; risk reading is Analyst Interpretation | Medium | Committee-Ready |
| Control and distribution behaviour is neutral to mixed | CP-1A, CP-2 | 20-F chunks 157, 295-296; Q3 6-K chunk 20 | Yes | High for facts | Analyst Inference | Analyst Interpretation | Low to Medium | Remediation Needed |

### Source lineage register (T5B.4)

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue 6,440 for nine months 2026 against 4,150 | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 1, income statement | CP-1 financials table | Sourced | High | Verified: "Revenue 5 6,440 4,150 2,276 1,415" |
| Adjusted EBITDA 1,092, 1,009, 857, 776, 693 by quarter | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 41, reconciliation | CP-1 table and Calculation 2 | Sourced | Medium to High | Verified; non-IFRS |
| Gross debt 8,648; net debt 7,983; derivatives and vendor financing 183; cash 848 | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 32, Debt | CP-1 table; CP-2 credit view | Sourced | Medium to High | Verified; ties arithmetically (Calculations) |
| Maturity ladder 872 / 986 / 1,947 / 1,601 / 1,147 / 2,094 | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 25, note 11B | CP-1 maturity table | Sourced | High | Verified; printed total 8,648 |
| Interest expense on bonds and bank financing 472 and on leases 232 for nine months | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 25, note 11 | CP-1 table; Calculation 6 | Sourced | High | Verified |
| Net cash provided by operating activities 2,028 for nine months | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 4, cash flow | CP-1 table | Sourced | High | The release reconciliation prints 2,019 (chunk 42); both carried |
| Equity free cash flow 867 for nine months; 316 for Q3 | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 31, Cash Flow | CP-1 table | Sourced | Medium to High | Non-IFRS measure |
| Lease liabilities 2,846 non-current and 344 current | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 3, balance sheet | CP-1 Calculation 3 | Sourced | High | Verified |
| Capex payables 1,644 non-current and 457 current against 758 and 440 | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 3 | CP-1 gap G9; CP-2 risks | Sourced | High | Verified |
| Financial statements of December 31, 2025 restated | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunks 3, 12 | CP-1 sources and gap G6 | Sourced | High | Verified |
| Total debt and financing 6,886 at December 31, 2025 by location | source-text/ | 20-F_2025-12-31_tigo-20251231.htm.jsonl | SRC-20F | chunk 245, note C.3 | CP-1 debt structure | Sourced | High | Verified |
| No covenant breach at December 31, 2025; covenant types named | source-text/ | 20-F_2025-12-31_tigo-20251231.htm.jsonl | SRC-20F | chunk 258, C.3.5 | CP-1 covenants; CP-2 gap S1 | Sourced | High | Qualitative only; thresholds Not supplied |
| Revolving credit facility 600 extended to October 15, 2027 | source-text/ | 20-F_2025-12-31_tigo-20251231.htm.jsonl | SRC-20F | chunks 124, 255 | CP-1 liquidity; CP-1A conflict C3 | Conflicting | High | Two descriptions inside the 20-F (565 versus full 600) |
| Atlas about 42.2 percent; Niel Family Group 44.1 percent | source-text/ | 20-F_2025-12-31_tigo-20251231.htm.jsonl | SRC-20F | chunks 157-158, 295 | CP-1A profile; CP-2 | Sourced | High | Different bases and dates; both carried |
| Payable to Iliad Holding Group 195 at December 31, 2025 | source-text/ | 20-F_2025-12-31_tigo-20251231.htm.jsonl | SRC-20F | chunk 296, note G.5 | CP-1A behaviour table; CP-2 risks | Sourced | High | Nature not stated |
| Chile earn-out up to 150 versus up to 490 | source-text/ | 20-F and Q1 6-K and Q3 6-K | SRC-20F; SRC-Q1; SRC-Q3 | 20-F chunks 7, 297; Q1 6-K chunk 8; Q3 6-K chunk 11 | CP-1A conflict C1 | Conflicting | High | Logged, not reconciled |
| EPM minority buy-out about $571 million, equity reduction 627 | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 8, note 3 | CP-1A transactions | Sourced | High | Verified |
| Coltel purchase consideration about $214.4 million; net loss 168 since acquisition | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunks 9, 10 | CP-1A transactions; CP-2 risks | Sourced | High | Provisional accounting |
| 7.375% notes due 2032 reopened for $87.5 million on April 14, 2026 | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 24, note 11 | CP-1A new debt issues | Sourced | High | Verified |
| Paraguay 5.875% notes due 2027 redeemed for about $139.7 million | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 25 | CP-1A new debt issues; CP-1 table | Sourced | High | Verified |
| Dividends: $3.00 per share cycle and $1.50 interim | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 20, note 7 | CP-1 liquidity; CP-2 finding 5 | Sourced | High | Verified |
| Management guidance of equity free cash flow around 1.1 billion and leverage below 2.5x | source-text/ | 6-K_2026-11-05_dp256407_6k.htm.jsonl | SRC-Q3 | chunk 29, 2026 Financial Targets | CP-1; CP-2 | Sourced | Low to Medium (management forward-looking claim) | Carried as Management Language |

### Calculation and assumption register (T5B.5)

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last-twelve-month Adjusted EBITDA as printed | CP-1 Calculation 2; CP-2 | Q4 2025 776; Q1 2026 857; Q2 2026 1,009; Q3 2026 1,092 | 776 + 857 + 1,009 + 1,092 = 3,734; period Q4 2025 to Q3 2026; no pro forma adjustment | Calculated | Calculation | Medium | Leverage, coverage | Q3 6-K chunk 41; re-performed: 3,734 |
| Net debt to LTM Adjusted EBITDA | CP-1 Calculation 3 | Net debt 7,983; LTM 3,734 | 7,983 / 3,734 = 2.14x (numerator net debt; denominator LTM Adjusted EBITDA) | Calculated | Analyst Interpretation | Medium | PD, refinancing | Q3 6-K chunks 32, 41; re-performed: 2.138 |
| Lease-inclusive net financing obligations to LTM Adjusted EBITDA | CP-1 Calculation 3; CP-2 weaknesses | Net debt 7,983; lease liabilities 2,846 + 344 = 3,190; LTM 3,734 | (7,983 + 3,190) / 3,734 = 2.99x; numerator 11,173 | Calculated | Analyst Interpretation | Medium | PD, refinancing | Q3 6-K chunks 3, 32, 41; re-performed: 2.992 |
| Management leverage 2.53x | CP-1; CP-2 | Release leverage definition: net debt over LTM Adjusted EBITDA less right-of-use depreciation and lease interest, pro forma for acquisitions | Not reproducible: right-of-use depreciation by quarter and the pro forma bridge are not supplied | Not Calculable | Management Language | Medium | PD, covenant read-across | Q3 6-K chunk 40; implied denominator 7,983 / 2.53 = 3,155 (re-performed) |
| Interest coverage, nine months | CP-1 Calculation 6; CP-2 finding 3 | Adjusted EBITDA 2,958; interest on bonds and bank financing 472; lease interest 232; cash interest paid 463 + 216 | 2,958 / 472 = 6.27x; 2,958 / (472 + 232) = 4.20x; 2,958 / (463 + 216) = 4.36x; reported basis, no pro forma | Calculated | Calculation | Medium | Debt service | Q3 6-K chunks 4, 25, 41; re-performed |
| Equity free cash flow after dividends | CP-1 Calculation 8; CP-2 | EFCF 867; dividends paid 587 | 867 − 587 = 280 | Calculated | Calculation | Medium | Liquidity | Q3 6-K chunks 4, 31; re-performed |
| Adjusted EBITDA excluding reported one-offs | CP-1 Calculation 8 | 2,958 + 149 = 3,107; Q3 1,092 + 31 = 1,123 | Addition of the issuer's own one-off classification; normalization label: issuer classification, not verified | Calculated | Analyst Interpretation | Low to Medium | Earnings quality | Q3 6-K chunk 41; re-performed |
| Scheduled dividends after September 30, 2026 | CP-1 Calculation 7; CP-2 | 5 installments of $0.75; weighted average shares 167.717 million (Q3) | 5 × 0.75 × 167.717 = 628.9; assumption: share count constant; dividend payable on the balance sheet is 579 and the difference is unexplained | Assumption-Based | Analyst Interpretation | Low to Medium | Liquidity, distributions | Q3 6-K chunks 3, 20, 21; re-performed |
| Fiscal 2025 versus nine-month 2025 Adjusted EBITDA basis difference | CP-1 Calculation 2 | FY2025 2,749 (20-F); 9M 2025 1,964 (re-presented); Q4 2025 776 | 2,749 − 1,964 = 785 against Q4 2025 776, a difference of 9; discontinued Adjusted EBITDA for 9M 2025 is 8 (Q3 6-K chunk 31) | Calculated | Analyst Interpretation | Medium | Comparability | 20-F chunk 228; Q3 6-K chunks 31, 41; this module supports the CP-1 explanation with the printed 8 |
| Gearing (net debt over equity attributable plus net debt) | CP-1 Calculation 4 | 7,983; 2,238 | 7,983 / (2,238 + 7,983) = 0.78; 20-F printed 0.60 for December 31, 2025 (5,357 / 8,997) | Calculated | Calculation | Medium | Leverage | 20-F chunk 273; Q3 6-K chunk 4; re-performed |

### Weak lineage and missing citation flags (T5B.6)

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Distributions are bounded by creditor terms (CP-2 distribution risk) | No indenture, credit agreement or covenant certificate in the set; restricted payment capacity is not traceable | Insufficient Information | Without the terms, the mechanic from dividends to creditor headroom stays unsupported and committee cannot size cushion | Obtain the revolving credit agreement, indentures and compliance certificates | CP-2 key finding 5 and risk table; CP-1 covenants |
| Material | Management leverage 2.53x as the leverage anchor | Denominator not reproducible; carried correctly as Management Language | Weak Lineage | Headline ratio drives the leverage view and cannot be audited from supplied tables | Obtain the management bridge or use lease-inclusive ratios alongside it | CP-1 table; CP-2 credit view |
| Material | Liquidity view relies on revolving facility of 600 | Facility drawn amount and maturity at 2026 dates not stated; two 20-F descriptions differ | Conflicting | Changes the liquidity headroom by up to 600 | Obtain current facility status | CP-1 liquidity; CP-2 key finding 4 |
| Material | Chile contingent consideration | Up to 150 in the 20-F against up to 490 in the 6-Ks, not reconciled | Conflicting | Maximum non-recourse exposure of an associate that carries a related-party call option differs by 340 | Obtain the share purchase agreement summary | CP-1A conflict C1; CP-2 gap S5 |
| Minor | Country count | CP-1A cites eleven countries (20-F chunk 77) and CP-2 cites twelve (Q3 6-K note 5 includes the Chile associate) | Conflicting | Wording inconsistency; no figure depends on it | Align wording in a future version | CP-2 credit view; CP-1A company description |
| Minor | Cash covers current maturities | CP-2 says cash of 848 "equals" debt due within one year 872; the statement is 0.97x | Analyst Inference | Slight overstatement of liquidity cover | Reword as slightly below | CP-2 key finding 4 |

### Auditability assessment (T5B.7)

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Four filings and the run context cover statements, notes and releases through September 30, 2026 | Missing indentures, credit agreements and debt schedule leave legal capacity and instrument detail untraced | Conclusions on distributions and priming stay bounded | Obtain the documents listed in the gaps ledger |
| Citation completeness | Ready with Remediation | Chunk-level locators with figures; this module verified 77 figures against the text | Chunk numbers are not printed page numbers, so a reader must open the converted text to confirm | Traceable but slower to audit | Add printed page labels where the filing shows them |
| Calculation traceability | Ready with Remediation | CP-1 Calculations 1 to 9 show inputs and formulas and were re-performed | Management leverage and pro forma figures cannot be recomputed | Leverage anchor is auditable only at the reported-line level | Obtain the management bridge |
| Assumption transparency | Ready with Remediation | Only the dividend and one-off normalizations are assumption-based and both are labelled | The 629 estimate and the 579 payable differ without explanation | Liquidity call is approximate | Replace with the declared installment schedule and share count |
| Markdown and export artifact integrity | Committee-Ready | All four handoffs carry the six required headings, issuer name, as-of date, source hashes and handoff hashes; CP-2 was corrected on its second attempt to open with the credit view | None found beyond heading and hash checks | Downstream handoff is usable | None |

### Gaps ledger (T5B.8)

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Covenant terms and compliance | Credit agreements, indentures, compliance certificates | Headroom, restricted payments and change of control determine default risk and recovery mechanics | CP-1 covenants; CP-2 distribution and liquidity risks | High impact | Revolving credit agreement and indentures (20-F exhibits) |
| CP-5-GAP-002 | Instrument-level debt after December 31, 2025 | September 30, 2026 debt and maturity schedule | Refinancing walls and obligor mix cannot be traced | CP-1 debt structure; CP-2 liquidity | High impact | Financial and Operational Data file or debt schedule |
| CP-5-GAP-003 | Revolving credit facility availability | 2026 drawn amount and maturity | Liquidity depends on it | CP-1; CP-2 finding 4 | High impact | Facility notice or filing |
| CP-5-GAP-004 | Management leverage bridge | Right-of-use depreciation, pro forma EBITDA | Anchor ratio not auditable | CP-1; CP-2 finding 2 | Medium impact | Management bridge |
| CP-5-GAP-005 | Nature of payable to Iliad Holding Group | Related-party note at September 30, 2026 | Possible shareholder funding or deferred distribution | CP-1A behaviour; CP-2 finding 6 | Medium impact | Related-party disclosure |
| CP-5-GAP-006 | Chile contingent consideration size | Share purchase agreement summary | Conflicting maximum (150 or 490) | CP-1A conflict C1 | Medium impact | Share purchase agreement |
| CP-5-GAP-007 | Ratings at the as-of date | Agency reports after December 31, 2025 | Market access | CP-1A profile; CP-2 gap S6 | Medium impact | Rating agency actions |
| CP-5-GAP-008 | Unreconciled small source differences | Bridges for 2,028 versus 2,019; 507 versus 508; 1,663 versus 1,664; 1,550 versus 1,552; repatriation 79 versus 22 | Prevents a single audited figure for these items | CP-1 gap G5 | Low impact | Issuer reconciliation |
| CP-5-GAP-009 | Goodwill roll-forward for Costa Rica | 20-F shows 142 at December 31, 2025; the 6-K shows an impairment of about 32 and remaining goodwill of about 123, which is 13 above the arithmetic result | Possible foreign exchange effect not stated | CP-1A Costa Rica fact | Low impact | Intangible assets note |
| CP-5-GAP-010 | Pro forma Coltel, Ecuador and Uruguay results | Pro forma Adjusted EBITDA and cash flow | Perimeter break limits trend ratios | CP-1; CP-2 finding 1 | Medium impact | Management pro forma bridge |

### Module register (T5.1)

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/6109e4cc67f485cb35bf2b91c71a66fdba8e23fe6719494ae967c06e9d76db49/1.response.md; run tigo-2026-11-05-credit_snapshot-host; sha256 533a512a1f3bb7bc99ba007a510cec3fdee3aeab214040d4ea601266e7a3d9fd | Source readiness for four filings | High | Six required headings present; issuer and as-of date stated | Passed with limitations | Accepted; consumer ratings READY_WITH_LIMITATIONS |
| CP-1 | requests/CP-1/94481948f66a35a2db3210e4ecd5b52acc20051918e49c613867472d92ff2ce9/1.response.md; same run; sha256 fe7d99399cef5dd86595e652b06e9adc0c0e7978006654d0393d9f885e47b23a | Financials, debt, liquidity, covenants as disclosed | High for statements, Medium for non-IFRS | Six headings; one financials table | Restricted | Material gaps G1 to G4; figures re-verified |
| CP-1A | requests/CP-1A/7102528ef5e16867eaaa2c48c0175295a183e4ea456fc7c42fd0982a02e1d01a/1.response.md; same run; sha256 8596dd7e17ec172b37486bf546dcfb005f6c7a6bd1a2256b504f11f560848eb5 | Business, ownership, transactions, behaviour | High | Six headings; two selector tables and prose transaction section | Restricted | Conflicts C1 to C3 logged |
| CP-2 | requests/CP-2/66017bdc03e391b567e36c1b9dcf2f915d37ba646a6decd9e2b6831f1ee51272/2.response.md; same run; sha256 603db548e62408a5ed9e37184469d36bae45df07ee1234514b18493d6ce902ab | Credit synthesis | Medium (upstream only) | Six headings; credit view opens the findings | Restricted | First attempt rejected for the opening section; second accepted |

### Citation and evidence support audit (T5.2)

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 | Distribution risk and thesis headroom | Weak: legal terms not supplied | Distribution capacity is argued from actions only; no restricted payment text | Obtain indentures and credit agreement | Restricted until documents are supplied |
| MINOR | CP-2 | Key finding 4: cash "equals" debt due within one year | Overstated: 848 against 872 | Imprecise wording | Reword | No clearance change |
| MINOR | CP-1 | Locators are converted-text chunks | Traceable | Chunk numbers differ from printed pages | Add printed page labels | No clearance change |

### Math, logic and definition audit (T5.3)

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | Management leverage 2.53x not reproducible | Release definition subtracts right-of-use depreciation and lease interest and is pro forma; inputs not supplied | Simple net debt over LTM Adjusted EBITDA is 2.14x and lease-inclusive 2.99x | Show both with the bridge request | Restricted for leverage-based sizing |
| MATERIAL | CP-1 | Nine-month operating cash flow | Statement 2,028 and release reconciliation 2,019 | Difference of 9 unexplained | Carry both; request bridge | Restricted for cash conversion precision |
| MINOR | CP-1 | Quarter sums | Equity free cash flow quarters sum to 868 against 867; capex 670 against 669; lease interest 233 against 232; tax 297 against 298 | Rounding inside the sources | None | No clearance change |
| MINOR | CP-1A | Costa Rica goodwill | 142 less an impairment of 32 gives 110, while the 6-K states about 123 remaining | Roll-forward not shown | Request note detail | No clearance change |
| MINOR | CP-1 | Dividend estimate | Estimate uses the Q3 weighted share count; balance sheet payable is 579 | Difference of about 50 unexplained | Replace with declared schedule | No clearance change |

### Legal and structural claim audit (T5.4)

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-2 | Absence of documented creditor-adverse actions; neutral to mixed behaviour | Indentures, revolving credit agreement and guaranty documents | No legal documents supplied (context legal_documents: none) | Obtain exhibits listed in 20-F chunks 123-127 | Legal review needed before relying on legal capacity |
| MATERIAL | CP-1 | 70 percent of debt at operating entities and generally non-recourse to MIC S.A.; guarantees of 629 at December 31, 2025 | Guarantor lists, indentures | Subsidiary guarantee structure and structural subordination not documented | Obtain guarantor schedules | Legal review needed for recovery mechanics |
| MINOR | CP-1A | Control statements differ between 20-F Item 7 and the related-party note | Articles, shareholder agreements | Change-of-control terms Not supplied | Request documents | Legal review optional |

### Relative value and market claim audit (T5.5)

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | No relative value, pricing or peer claim is made; the method prohibits peer ranking and instrument recommendation | Quotes, spreads, ratings at the as-of date and peer data are blank in the context | Market datapoints Not supplied | None for the current scope; supply them if CP-3 is requested | No effect on this snapshot |

### Cross-module consistency audit (T5.6)

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-1, CP-2 | Chile contingent consideration: up to 150 (20-F) versus up to 490 (6-Ks); logged as C1 in CP-1A and carried in CP-2; CP-1 does not mention it | 20-F issued March 24, 2026 and 6-Ks later in 2026 may reflect a revised agreement or a different measure | Keep both; request the agreement | Contingent obligation sizing |
| MATERIAL | CP-0, CP-1, CP-1A, CP-2 | Revolving facility: 565 extended or full 600 (C3) | Original facility amendment versus October 15, 2025 joinder | Keep both; use the later joinder with a flag | Liquidity headroom |
| MINOR | CP-1A, CP-2 | Eleven countries (20-F) versus twelve (Q3 6-K note 5 including the Chile associate) | Different dates and perimeter | Align wording | Presentation |
| MINOR | CP-1, CP-1A, CP-2 | Ownership 42.2 percent (Atlas at December 31, 2025) and 44.1 percent (Niel Family Group, March 2026 filing basis) | Different dates and inclusion of expected purchases | Keep both; CP-2 uses 42.2 percent consistently | None |

All shared figures were identical across modules: gross debt 8,648, net debt 7,983, cash 848, management leverage 2.53x, lease liabilities 3,190, nine-month Adjusted EBITDA 2,958, equity free cash flow 867, dividend estimate about 629, payable to Iliad Holding Group 195. Gap identifiers cited by CP-2 (G1 to G13 of CP-1 and A1 to A8 of CP-1A) exist in the upstream handoffs with matching meaning.

### Markdown and presentation audit (T5.7)

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Density | The financials table has eight columns and about forty rows, which is hard to read without a viewer | Split in a presentation version | Readability only |
| MINOR | CP-2 | Wording | Strengths such as "scale and diversification" are supported by cited rows but the word "strong" appears in headings; each use is followed by the supporting figure | Keep as is | None |

### Handoff integrity audit (T5.8)

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 to CP-2 | Envelope | Handoffs have no YAML front matter because the Markdown transport replaces it; the issuer, as-of date, source hashes and handoff hashes sit in the Request and Sources sections | Accept as transport | None |
| MINOR | CP-2 | Revision | First attempt was rejected for the opening section and corrected; the rejected file is retained unmodified | None | None |

### Consolidated issue log (T5.9)

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP-5-ISS-001 | MATERIAL | CP-2 | Unsupported legal capacity | Distribution and priming conclusions rest on actions only; no legal documents | Obtain indentures and credit agreements | Restricted | Open |
| CP-5-ISS-002 | MATERIAL | CP-1, CP-2 | Definition not reproducible | Management leverage 2.53x | Obtain bridge | Restricted | Open |
| CP-5-ISS-003 | MATERIAL | CP-1 | Source conflict | Operating cash flow 2,028 versus 2,019 | Request reconciliation | Restricted | Open |
| CP-5-ISS-004 | MATERIAL | CP-1A, CP-2 | Source conflict | Chile earn-out 150 versus 490 | Obtain agreement | Restricted | Open |
| CP-5-ISS-005 | MATERIAL | CP-1, CP-1A, CP-2 | Source conflict | Revolving facility 565 versus 600 and no 2026 status | Confirm | Restricted | Open |
| CP-5-ISS-006 | MATERIAL | CP-1, CP-2 | Unsupported legal structure | Operating-level non-recourse and guarantees untraced | Obtain guarantor schedules | Restricted | Open |
| CP-5-ISS-007 | MINOR | CP-1, CP-2 | Rounding | Quarter-sum differences of 1 | None | None | Open |
| CP-5-ISS-008 | MINOR | CP-1A | Roll-forward | Costa Rica goodwill 123 versus 110 | Request note | None | Open |
| CP-5-ISS-009 | MINOR | CP-1, CP-2 | Estimate | Dividend estimate about 629 versus payable 579 | Use declared schedule | None | Open |
| CP-5-ISS-010 | MINOR | CP-1A, CP-2 | Consistency | Eleven versus twelve countries | Align wording | None | Open |
| CP-5-ISS-011 | MINOR | CP-2 | Wording | Cash "equals" current debt (0.97x) | Reword | None | Open |
| CP-5-ISS-012 | MINOR | CP-1 | Locator | Chunk numbers, not printed pages | Add page labels | None | Open |
| CP-5-ISS-013 | MINOR | CP-1, CP-1A, CP-2 | Consistency | Ownership 42.2 versus 44.1 percent | Keep both | None | Open |

### QA decision

Severity engine: no CRITICAL finding is open; six MATERIAL findings are open, so qa_status is Restricted. Committee status is Restricted: the credit view may be used with the stated limitations and may not be used to size covenant headroom, restricted payment capacity or recovery mechanics. The numeric confidence score is script-owned and was not computed in this host run; under the rule for Restricted status it is capped at 59 and the band is Low.

## Calculations

All re-performed by this module from the quoted inputs; no value is carried from the upstream handoffs without a check.

### Quarter-sum tie-out, nine months 2026

| Item | Q1 2026 | Q2 2026 | Q3 2026 | Sum of quarters | Nine months printed | Difference |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue | 1,985 | 2,179 | 2,276 | 6,440 | 6,440 | 0 |
| Adjusted EBITDA | 857 | 1,009 | 1,092 | 2,958 | 2,958 | 0 |
| Operating profit | 416 | 462 | 600 | 1,478 | 1,478 | 0 |
| Profit before taxes | 154 | 204 | 213 | 571 | 571 | 0 |
| Net profit attributable to owners | 109 | 109 | 98 | 316 | 316 | 0 |
| Net cash from operating activities | 590 | 711 (derived: 1,301 − 590) | 727 | 2,028 | 2,028 | 0 |
| Equity free cash flow | 225 | 327 | 316 | 868 | 867 | 1 (rounding) |
| Capex excluding spectrum | 193 | 234 | 243 | 670 | 669 | 1 (rounding) |
| Interest expense on bonds and bank financing | 135 | 164 | 173 | 472 | 472 | 0 |
| Interest expense on leases | 68 | 78 | 87 | 233 | 232 | 1 (rounding) |
| Tax expense | 78 | 104 | 115 | 297 | 298 | 1 (rounding) |

### Net debt and maturity tie-outs

- Net debt = gross debt + derivatives and vendor financing − cash: September 30, 2026: 8,648 + 183 − 848 = 7,983 (printed 7,983); June 30, 2026: 8,742 + 194 − 861 = 8,075 (printed 8,075); March 31, 2026: 8,624 + 162 − 1,177 = 7,609 (printed 7,609); December 31, 2025: 6,886 + 23 − 1,552 = 5,357 (printed 5,357); September 30, 2025: 6,260 + 30 − 1,664 = 4,626 (printed 4,627; rounding).
- Maturity ladders summed: September 30, 2026: 872 + 986 + 1,947 + 1,601 + 1,147 + 2,094 = 8,647 (printed 8,648); June 30, 2026: 8,742 (printed 8,742); March 31, 2026: 8,626 (printed 8,624); December 31, 2025: 6,885 (printed 6,886 and 6,887). All differences are 2 or less.
- Quarterly Adjusted EBITDA for 2025: Q1 633 + Q2 638 + Q3 693 + Q4 776 = 2,740 against FY2025 2,749 in the 20-F; the difference of 9 matches the Adjusted EBITDA of discontinued operations (8 for nine months 2025, Q3 6-K chunk 31) within rounding, and supports the CP-1 explanation that the 20-F is not re-presented.
- Top 5 classification count: Directly Sourced 2, Calculated 1, Assumption-Based 0, Analyst Inference 2, Weak Lineage, Untraced, Conflicting or Insufficient Information 0 (drivers 1 and 4; 2; none; 3 and 5; none).

## Gaps

The gaps ledger above (CP-5-GAP-001 to CP-5-GAP-010) is the gap record of this module. In summary: covenant terms and legal documents, instrument-level debt after December 31, 2025, revolving facility availability, the management leverage bridge, the Iliad Holding Group payable, the Chile earn-out size, current ratings, small unreconciled source differences, the Costa Rica goodwill roll-forward and pro forma acquired-business results are not supplied. They restrict the committee use of the upstream conclusions as set out in the QA decision; none changes a figure.

## Next module

This is the last module in the selected set. The report can be assembled from CP-0, CP-1, CP-1A, CP-2 and this review. Before committee use beyond the restricted purpose, obtain the revolving credit agreement and indentures, the September 30, 2026 debt and maturity schedule, the management leverage bridge, current ratings and the explanation of the Iliad Holding Group payable, then rerun CP-1, CP-1A, CP-2 and CP-5.
