## Request

Module CP-0 (source readiness) for Carnival Corp Ltd. (issuer id ccl), as of 2026-11-05, pathway credit_snapshot, case kind public. The cutoff in the context is 2026-11-05, the current period is q3-2026 (quarter ended 2026-08-31), the prior period is fy-2025 (fiscal year ended 2025-11-30) and the reporting currency is USD. The question is whether the supplied source set can support the requested downstream work (CP-1, CP-1A, CP-2, CP-5) and what remains blocked. This module gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize or reconcile figures. The context file lists no deal terms, quotes, ratings, peers, assumptions or research questions, and states `legal_documents` as `none`; it is not issuer evidence.

Locator convention used throughout: `<source alias> page:N`, where N is the extracted chunk number of the pinned text file, not the printed page. Aliases are defined in the first table under Sources.

## Sources

### Issuer sources relied on

| Alias | Exact source name | sha256 | Document family and period |
| --- | --- | --- | --- |
| 10-K | 10-K_2025-11-30_ccl-20251130.htm.jsonl | 319fc4f2d973f28d585a1955a2d440c02d8b1b6dbc0973c191e2363a73060526 | Annual report, fiscal year ended November 30, 2025, filed 2026-01-27, 112 pages |
| Q1 10-Q | 10-Q_2026-02-28_ccl-20260228.htm.jsonl | 618bcc494da0b2893a6d142c3d1a9bab122d817be7203e48a24415f7863a4619 | Quarterly report, quarter ended February 28, 2026, filed 2026-03-27, 29 pages |
| Q2 10-Q | 10-Q_2026-05-31_ccl-20260531.htm.jsonl | 7f4c931117646bfadf44441c2cfafd9c06b54d8efce3cf617ece0b76c9969691 | Quarterly report, quarter ended May 31, 2026, filed 2026-06-26, 32 pages |
| Q3 10-Q | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | d3735109439ee392b1d7fba90666d820b500bbba0c767539cc84776ce14477e7 | Quarterly report, quarter ended August 31, 2026, filed 2026-09-29, 29 pages |
| Q1 release | EX-99.1_2026-03-27_a20261qearningsrelease8-k.htm.jsonl | 30b7e2e340d9ff04fd374426ee85a1b23f2a0ad36a11daf5d191cd2b3b5e65b3 | Earnings release exhibit, first quarter 2026, dated 2026-03-27, 15 pages |
| Q2 release | EX-99.1_2026-06-23_a20262qearningsrelease8-k.htm.jsonl | 5b3125d03084066ceb1281134ac06b53a255fd76fa75628f167339ceb2fd622a | Earnings release exhibit, second quarter 2026, dated 2026-06-23, 15 pages |
| Q3 release | EX-99.1_2026-09-29_a20263qearningsrelease8-k.htm.jsonl | a4d2ebb65632ec32cdeeba0842dfc488f9c01a40330706395f7804c9f49dd751 | Earnings release exhibit, third quarter 2026, dated 2026-09-29, 14 pages |

The first line of each pinned text file quotes a different sha256: that is the hash of the original HTML document, not of the pinned text file. The hashes in the table are the pinned text-file hashes supplied by CP-OS and are the ones relied on here.

### Run context

| Source | sha256 | Role |
| --- | --- | --- |
| context | 0ae02699c3e76f28ddabed001602c70760df4bfe5d4037c1d00e74d8c149ab79 | User's dated settings for this run. Not issuer evidence. |

### Handoffs supplied

None. CP-0 is the first module of this run and CP-OS supplied no upstream handoff, so there is no handoff module or hash to list.

The pack also holds `_retrieval.json`, which CP-OS ignored as a source. It is retrieval metadata only and was not relied on for any finding.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The 7 filed or furnished sources cover statements, debt, covenants, liquidity and segments for the latest annual and three quarterly periods, so the four requested analyses can proceed, with bounded gaps. | Medium | No indentures, credit agreements, rating reports, market quotes or fiscal 2025 adjusted EBITDA are supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report covers the former two-company group; the latest quarterly report covers the single Bermuda company after the May 2026 unification. | Debt, earnings and equity comparisons across the change need care. | High |
| Debt, maturities, covenants and liquidity are printed in all 3 quarterly reports and the annual report. | Leverage and liquidity work can be sourced from filed notes. | High |
| Fiscal 2025 adjusted EBITDA and interim cash interest paid are not printed in the supplied sources. | A last-twelve-month adjusted leverage or cash interest cover figure cannot be read directly. | High |
| Rating levels, indentures and credit agreement terms are not in the pack. | Ranking, guarantees and covenant definitions rest on summary note text only. | High |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for each requested consumer (CP-1, CP-1A, CP-2 and CP-5). All 7 issuer sources are filed or furnished documents with extracted text on every page (246 of 246 pages carry text, 0 blank). The filed 10-K and 10-Qs hold the authority for statements, debt, covenants, commitments and legal matters; the earnings releases are furnished management documents and supply non-GAAP reconciliations, guidance and attributed narrative only. Nothing is blocked and no consumer is conditional: no critical identity boundary is unresolved, although the reporting entity changed in May 2026. The main restrictions are a perimeter change inside the series (a combined two-registrant group through the first quarter 2026, a single Bermuda registrant afterwards), the absence of fiscal 2025 adjusted EBITDA and of interim cash interest paid, the absence of any legal financing document or rating report, and possible release graphics that text extraction does not show. Source sufficiency here does not mean any downstream analysis is complete, and no extraction fidelity review has been done. The next evidence action is to obtain the fourth quarter 2025 earnings release or another source for fiscal 2025 adjusted EBITDA, and the debt documents, before leverage, coverage and ranking conclusions are drawn.

### Source assessment

| Alias | Original authority | Entity and perimeter | Period and basis | Key content located (locators) |
| --- | --- | --- | --- | --- |
| 10-K | Filed annual report; audited statements (auditor reports at 10-K page:98 to page:99 and page:102 to page:103; Item 9A at 10-K page:103) | Joint report of Carnival Corporation (Republic of Panama) and Carnival plc (England and Wales), statements titled "CARNIVAL CORPORATION & PLC" (10-K page:1, page:63) | Fiscal years ended November 30, 2025, 2024 and 2023, USD millions | Income statement 10-K page:63; balance sheet 10-K page:63 to page:64; cash flow 10-K page:64; debt note 10-K page:79 to page:82; ship commitments 10-K page:84; leases 10-K page:91; segments 10-K page:91 to page:94; pensions 10-K page:95 to page:97; cash paid for interest 10-K page:98; liquidity 10-K page:59; material cash requirements 10-K page:61; exhibit index 10-K page:107 to page:111 |
| Q1 10-Q | Filed interim report, unaudited | Joint Carnival Corporation and Carnival plc; statements titled "CARNIVAL CORPORATION & PLC" (Q1 10-Q page:2); unification described as proposed (Q1 10-Q page:21) | Quarter ended February 28, 2026, USD millions | Statements Q1 10-Q page:2 to page:4; debt Q1 10-Q page:9; covenants Q1 10-Q page:10; segments Q1 10-Q page:17; liquidity Q1 10-Q page:25 |
| Q2 10-Q | Filed interim report, unaudited | Carnival Corporation Ltd. (Bermuda), single registrant on the cover (Q2 10-Q page:1) and in the statements (Q2 10-Q page:2) | Quarter and six months ended May 31, 2026, USD millions | Statements Q2 10-Q page:2 to page:3; unification completed Q2 10-Q page:5; debt Q2 10-Q page:10; covenants Q2 10-Q page:10; segments Q2 10-Q page:17 to page:19; liquidity Q2 10-Q page:27 |
| Q3 10-Q | Filed interim report, unaudited | Carnival Corporation Ltd. (Bermuda); obligor group summary of Carnival Corporation Ltd. and Carnival UK Ltd. (Q3 10-Q page:26) | Quarter and nine months ended August 31, 2026, USD millions; comparatives November 30, 2025 and nine months 2025 | Statements Q3 10-Q page:2 to page:4; debt table Q3 10-Q page:9; maturities, revolver, undrawn export credit, covenants Q3 10-Q page:10; commitments Q3 10-Q page:13; segments Q3 10-Q page:16 to page:19; MD&A and liquidity Q3 10-Q page:20 to page:26; repurchases Q3 10-Q page:28 |
| Q1 release | Furnished management document; attributed claims | Carnival Corporation & plc (Q1 release page:1) | Quarter ended February 28, 2026 | Adjusted EBITDA reconciliation Q1 release page:11; guidance Q1 release page:5 to page:6; targets and buyback Q1 release page:3 to page:4 |
| Q2 release | Furnished management document; attributed claims | Carnival Corporation Ltd. (statements Q2 release page:8) | Quarter and six months ended May 31, 2026 | Adjusted EBITDA reconciliation Q2 release page:10; net debt to adjusted EBITDA ratio statement Q2 release page:3; guidance Q2 release page:4 to page:5 |
| Q3 release | Furnished management document; attributed claims | Carnival Corporation Ltd. (statements Q3 release page:8) | Quarter and nine months ended August 31, 2026 | Adjusted EBITDA reconciliation Q3 release page:10; guidance Q3 release page:4 to page:5; rating and redemption statements Q3 release page:3 |

### Version, perimeter and duplicate relationships

- Reporting entity changed inside the series. The 10-K and Q1 10-Q are joint reports and statements of Carnival Corporation & plc. The Q2 10-Q states: "In May 2026, we completed the unification of the dual listed company structure under a single company, Carnival Corporation Ltd." (Q2 10-Q page:5). The Q3 10-Q repeats this and states the migration of legal incorporation from Panama to Bermuda (Q3 10-Q page:5). Every period comparison that crosses February 28, 2026 and May 31, 2026 crosses this boundary. The Q3 10-Q equity statement shows the line "DLC unification share exchange and related costs" (Q3 10-Q page:4). The Q3 10-Q states "There have been no material changes to our business, including strategy, underlying assets and operations" (Q3 10-Q page:5); this is a management statement in a filed document and is not a fidelity review of the series.
- Release entity names move with the filings: the Q1 release is headed "CARNIVAL CORPORATION & PLC" and the Q2 and Q3 releases "CARNIVAL CORPORATION LTD." in their statements.
- No source is a duplicate of another. The three 10-Qs and three releases are distinct periods; the Q3 release statements repeat the Q3 10-Q statements and are not an independent source for the same figures. The 10-K is the retained source for fiscal 2025 figures; the Q3 10-Q repeats the November 30, 2025 balance sheet as a comparative, with presentation changes noted below.
- Issuer, borrower, guarantor roles: the context names no borrower, parent or guarantors. The Q3 10-Q debt table groups debt as "Unsecured Subsidiary Guaranteed" and "Unsecured (No Subsidiary Guarantee)" and states "all of our outstanding debt is issued or guaranteed by substantially the same entities with the exception of the $1.7 billion of export credit facilities of Sun Princess Limited and Sun Princess II Limited" (Q3 10-Q page:10). Individual issuers and guarantor lists per instrument are not in the pack; the entity-by-instrument mapping is an open distinction (see Gaps).

### Coverage by evidence need

| Evidence need | Status | Locators and limitation |
| --- | --- | --- |
| Income statement, balance sheet, cash flow | Retained | 10-K page:63 to page:64; Q1 10-Q page:2 to page:4; Q2 10-Q page:2 to page:3; Q3 10-Q page:2 to page:4. Annual figures are for the combined group; Q2 and Q3 are for the single company. |
| Discrete quarters | Partly retained | First quarter, second quarter and third quarter 2026 adjusted EBITDA are separately printed (Q1 release page:11, Q2 release page:10, Q3 release page:10). A discrete fourth quarter 2025 is not printed: no fourth quarter 2025 release is in the pack. |
| Quarter versus year-to-date | Retained | Q3 10-Q page:2 and Q3 release page:8 print three-month and nine-month columns; Q2 release page:10 prints three-month and six-month columns. Cash flows in the 10-Qs are year-to-date only (Q3 10-Q page:3 to page:4). |
| Fiscal years | Retained | 10-K page:63 to page:64 print fiscal 2025, 2024 and 2023. |
| Segments | Retained | North America, Europe, Cruise Support, Tour and Other: 10-K page:91 to page:94; Q3 10-Q page:16 to page:19. Segment expense captions in the 10-Q tables are labelled adjusted and carry footnote definitions (Q3 10-Q page:17). |
| Add-backs and non-GAAP | Retained from releases | Adjusted net income to adjusted EBITDA reconciliation: Q3 release page:10. Management-defined; the filings do not print adjusted EBITDA. |
| Facility-level debt and carrying values | Retained | Instrument-level table with maturity, rate, principal and prior year: Q3 10-Q page:9; 10-K page:79. Net of unamortized issuance costs and discounts shown as a separate line. Guarantee and security status by instrument is in table captions and footnotes (Q3 10-Q page:9 to page:10). |
| Debt maturities | Retained | Q3 10-Q page:10; 10-K page:80; payments due including estimated interest: 10-K page:61. |
| Liquidity | Retained | Cash and undrawn revolver and export credit: Q3 10-Q page:25 and page:10; prior points Q1 10-Q page:25, Q2 10-Q page:27, 10-K page:59. |
| Covenants | Retained as note summary | Q3 10-Q page:10 lists the covenant types and levels; the 10-K gives the step-up of the interest coverage minimum (10-K page:82). The issuer's reported covenant ratios are not printed; only compliance statements are (Q3 10-Q page:11). |
| Cash-paid interest and tax | Partly retained | Fiscal 2025 cash paid for interest and tax: 10-K page:98 ("Cash paid for interest, net of capitalized interest, was $1.2 billion in 2025", rounded to $0.1 billion). Interim cash paid for interest is not printed in the Q1 10-Q, Q2 10-Q or Q3 10-Q: Q3 10-Q page:19 (Note 8) gives only the cash and restricted cash reconciliation. |
| Leases, pensions, commitments | Retained | Leases 10-K page:91 and balance sheet lines (Q3 10-Q page:3); pensions 10-K page:95 to page:97; ship commitments 10-K page:84 and Q3 10-Q page:13; undrawn export credit facilities Q3 10-Q page:10 and page:26. |
| Contingencies and litigation | Retained | Q3 10-Q page:11 to page:12; 10-K page:82 to page:83. |
| Business and transaction narrative | Retained | 10-K page:6 to page:32 (business), unification and redomiciliation 10-K page:7 to page:8, Q2 10-Q page:5, Q3 10-Q page:5; PROPEL targets and buyback Q1 release page:3 to page:4. |
| Subsequent events and post-quarter items | Retained, thin | Q3 10-Q page:26 states an expected Form S-3 filing on September 29, 2026 with Carnival UK Ltd. as possible guarantor; Q3 release page:3 states approximately $1.2 billion of repurchases year to date. No source is dated after 2026-09-29. |
| Legal financing documents | Not supplied | No indenture, credit agreement or amendment; the exhibit index lists them by reference only (10-K page:107 to page:111). Context `legal_documents` is `none`. |
| Ratings | Not supplied | Rating actions are mentioned (Q2 release page:3, Q3 release page:3) without agency levels or outlooks; context ratings list is empty. |

### Source conflicts and scope differences

| Item | Source A (locator) | Source B (locator) | Downstream effect |
| --- | --- | --- | --- |
| November 30, 2025 equity presentation | 10-K page:64: additional paid-in capital 17,267; no noncontrolling interest line; total shareholders' equity 12,284 | Q3 10-Q page:3: additional paid-in capital 17,253; noncontrolling interests 14; total shareholders' equity 12,284 | Same total, different split. The Q3 10-Q page:5 states that immaterial amounts were reclassified "to separately present amounts attributable to noncontrolling interests". The filed 10-K balance sheet governs the original presentation; the Q3 10-Q is the later presentation. Equity and net income attributable lines must be matched by presentation. |
| Net debt to adjusted EBITDA definition | Q1 release page:13: "total debt less cash and cash equivalents excluding a minimum cash balance divided by twelve-month adjusted EBITDA" | Q2 release page:13 and Q3 release page:12: "total debt less cash and cash equivalents divided by twelve-month adjusted EBITDA" | The company's published ratio is not on a constant definition across the three releases. The ratio is printed only in the Q2 release ("net debt to adjusted EBITDA1 ratio of 3.1x", Q2 release page:3). The minimum cash amount in the Q1 definition is not supplied. Total debt is not defined as principal or carrying value. |
| Share repurchases year to date | Q3 10-Q page:3: share repurchases (929) nine months; page:4 equity statement (939) | Q3 release page:3: "nearly $1.2 billion of share repurchases so far this year" | Scope difference. The release is dated 2026-09-29, after the 2026-08-31 period end, so the release figure appears to run beyond the quarter. The pack does not itemize the post-quarter purchases, so the difference is not confirmed by a filing. |
| Fiscal 2025 maturity table total | 10-K page:80: yearly amounts total 27,382 when added | 10-K page:79 and page:80: total debt 27,383 | One million rounding in the source table. No effect beyond rounding. |
| Possible release graphics | Q2 release page:1 and Q3 release page:1 to page:3 | The headings "Advance Sales" and "Capital Allocation" end a chunk and are followed directly by narrative text, with no table or chart data | Whether charts sit under these headings cannot be told from extracted text, so any chart content is treated as not inspected. The narrative text is retained. |

### Consumer readiness

| Consumer | Status | Evidence demand and carried limitations |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Needs statements, debt table, maturities, liquidity, EBITDA and interest inputs by period. Statements, debt, maturities and liquidity are located for fiscal 2025 and each 2026 quarter. Limitations: fiscal 2025 adjusted EBITDA is not printed; interim cash paid for interest is not printed (annual only, rounded); perimeter change at May 2026; the published net debt ratio definition varies; GAAP operating income and D&A are printed for building an EBITDA series. |
| CP-1A | READY_WITH_LIMITATIONS | Needs business model, ownership and transaction facts. The 10-K business section, the unification and redomiciliation text and the PROPEL and buyback disclosures are located. Limitations: no legal financing documents; the context names no sponsor, parent or guarantors; the obligor group summary is filed but its form S-3 status after 2026-09-29 is not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Needs the upstream registers only. The source set supports strengths, weaknesses and risks from filings. Limitations: no ratings levels, market quotes or peers (context blank, not zero); management claims in the releases are attributed and cannot override the filings. |
| CP-5 | READY_WITH_LIMITATIONS | Needs located quotes for every cited fact. All 7 sources have page-numbered text. Limitations: tables are flattened in extraction, so row and column alignment must be checked against the quote; any graphics in the releases are not inspected; extraction fidelity is not reviewed. |

For any later HTML model objective the source assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This module asserts no normalized quarters, no reconciliation and no acceptance of downstream inputs.

## Calculations

No financial metric was calculated or normalized in this module. The following are footing checks of printed totals, made to test extraction fidelity of the located tables; they are not analysis.

| Check | Inputs (locator) | Result | Printed total |
| --- | --- | --- | --- |
| Debt table foots, August 31, 2026, USD millions | Unsecured Subsidiary Guaranteed 10,953 plus Unsecured (No Subsidiary Guarantee) 13,606 (Q3 10-Q page:9) | 24,559 | Total Debt 24,559 (Q3 10-Q page:9) |
| Debt maturities foot, USD millions | 301 + 2,517 + 3,961 + 3,631 + 2,885 + 11,264 (Q3 10-Q page:10) | 24,559 | Total 24,559 (Q3 10-Q page:10) |
| Fiscal 2025 maturities foot, USD millions | 2,615 + 2,518 + 3,962 + 4,133 + 2,886 + 11,268 (10-K page:80) | 27,382 | Total 27,383 (10-K page:80); one million rounding |
| Liquidity as printed, August 31, 2026 | Cash and cash equivalents 1,220 (Q3 10-Q page:2) plus 4.5 billion available under the revolver (Q3 10-Q page:10) | 5,720 million | "$5.7 billion of liquidity" (Q3 10-Q page:25); consistent at printed rounding |
| Discrete quarter adjusted EBITDA ties to nine months 2026, USD millions | 1,267 (Q1 release page:11) + 1,582 (Q2 release page:10) + 2,993 (Q3 release page:10) | 5,842 | Nine months 5,842 (Q3 release page:10) |
| Discrete quarter adjusted EBITDA ties to nine months 2025, USD millions | 1,205 (Q1 release page:11) + 1,508 (Q2 release page:10) + 2,993 (Q3 release page:10) | 5,706 | Nine months 5,706 (Q3 release page:10) |
| Dividends year to date | 414 (Q2 release page:3, year to date to May 2026) + 204 (Q3 release page:3, third quarter) | 618 | 618 (Q3 10-Q page:3 and Q3 release page:3) |
| November 30, 2025 equity split | 17,267 less 17,253 | 14 | Noncontrolling interests 14 (Q3 10-Q page:3) |
| Coverage counts | 112 + 29 + 32 + 29 + 15 + 15 + 14 pages | 246 of 246 pages with extracted text | Page counts from the pinned files |

The first quarter 2026 figure in the tie-out comes from the combined Carnival Corporation & plc perimeter and the second and third from the single company; they tie arithmetically, which is a footing result and does not establish comparability.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Fiscal 2025 adjusted EBITDA and a discrete fourth quarter 2025 are not printed in any supplied source (the 10-K prints no adjusted EBITDA; covenant text mentions it only, 10-K page:82). A last-twelve-month adjusted EBITDA at August 31, 2026 is not directly supplied. | Medium | CP-1, CP-2 | Obtain the fourth quarter 2025 earnings release, or build the series from GAAP operating income and depreciation and amortization, which are printed (10-K page:63; Q3 10-Q page:2), and label it as not the company's adjusted measure. |
| Interim cash paid for interest is not printed for the quarterly periods; fiscal 2025 is printed only as "$1.2 billion" (10-K page:98). | Medium | CP-1 | Use fiscal 2025 cash interest as the only cash-basis point and show interest expense (Q3 10-Q page:2) as a separate accrual-basis measure; do not present them as one series. |
| Perimeter change: combined two-registrant group through the first quarter 2026; single Bermuda registrant from the second quarter 2026. | Medium | CP-1, CP-1A, CP-2, CP-5 | Label each figure with its filing and perimeter; read the Q3 10-Q page:5 reclassification note when comparing November 30, 2025 balances. |
| No indentures, credit agreement, amendments or guarantor lists; covenant definitions are summarized only and the issuer's reported covenant ratios are not printed. Entity-by-instrument issuer and guarantor roles remain unresolved. | Medium | CP-1A, CP-2 | Obtain the revolving facility agreement, key indentures and the guarantor exhibit before any ranking or covenant headroom conclusion. |
| No rating agency, level or outlook; context ratings empty. Releases state a Moody's upgrade (Q2 release page:3) and an S&P upgrade (Q3 release page:3) without levels. | Medium | CP-2 | Obtain agency publications dated on or before 2026-11-05. |
| The company's published net debt to adjusted EBITDA ratio is printed only for the second quarter (3.1x, Q2 release page:3) and its definition changes between releases; total debt basis (principal 24,559 or carrying 23,912, Q3 10-Q page:9 and Q3 release page:9) is not stated. | Low | CP-1, CP-2 | Compute any leverage from printed components with the basis stated. |
| Possible graphics under "Advance Sales" and "Capital Allocation" in the 3 releases are not visible in text extraction and are not inspected. | Low | CP-1A, CP-2 | Treat them as uninspected; rely on the surrounding text bullets only. |
| No document dated after 2026-09-29 is in the pack although the cutoff is 2026-11-05. Any October 2026 filing, the Form S-3 status, post-quarter repurchases beyond the release wording and any later debt or ratings event are unverified. | Medium | CP-1A, CP-2, CP-5 | Obtain the filing list from 2026-09-30 to 2026-11-05 and confirm whether any event requires an update. |
| No earnings presentation slides; the release says the presentation is on the company website (Q3 release page:5). | Low | CP-1A | None needed for filings-based work; slides would be attributed management claims. |
| No extraction fidelity review has been performed on any source; flattened tables could misalign columns. | Low | CP-5 | Check each quote against the table rows before use. |

## Next module

CP-1 may run on the current source set as READY_WITH_LIMITATIONS, carrying the limitations in Gaps (perimeter change, no fiscal 2025 adjusted EBITDA, no interim cash interest). CP-1A, CP-2 and CP-5 follow in the planned order and consume the CP-1 and CP-1A handoffs; none is a source-readiness condition. The next evidence action is to obtain the fourth quarter 2025 earnings release, the debt documents and any filing dated 2026-09-30 to 2026-11-05.
