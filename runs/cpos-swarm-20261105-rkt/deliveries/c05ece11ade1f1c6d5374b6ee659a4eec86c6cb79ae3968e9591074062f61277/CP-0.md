## Request

Module CP-0 (source readiness) for Rocket Companies, Inc. (issuer id rkt, NYSE: RKT), as of 2026-11-05, pathway credit_snapshot, case kind public. The context sets the cutoff at 2026-11-05, the current period at q3-2026 (quarter ended 2026-09-30), the prior period at fy-2025 (fiscal year ended 2025-12-31) and the reporting currency at USD. All issuer sources report in US dollars; the filings state amounts in millions unless noted (Q3 10-Q page:5) and the earnings releases state "$ in millions" (Q3 release page:1). No other currency or period basis is used.

The question is whether the supplied source set can support the requested downstream work (CP-1, CP-1A, CP-2, CP-5) and what remains blocked. This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize, reconcile or model figures. The context file lists no borrower, parent, guarantors, deal terms, quotes, ratings, peers, valuation inputs, assumptions or research questions, and gives `legal_documents` as `none`. It is run configuration, not issuer evidence, and its blank fields are not read as zero.

Locator convention used throughout: `<source alias> page:N`, where N is the extracted chunk number of the pinned text file, not the printed page. Aliases are defined in the first table under Sources.

## Sources

### Issuer sources relied on

| Alias | Exact source name | sha256 | Document family and period |
| --- | --- | --- | --- |
| 10-K | 10-K_2025-12-31_rkt-20251231.htm.jsonl | 3f00d23a5a4d987299ba3ee372766fbda78de035096653b1d865a69d888922ae | Annual report, fiscal year ended December 31, 2025, signed March 2, 2026 (10-K page:223), 223 pages |
| Q1 10-Q | 10-Q_2026-03-31_rkt-20260331.htm.jsonl | 0a828436cfdb4cb6430873bcdf676f4a2758eb6f8aaf83bcd5c4c1bd9959be37 | Quarterly report, quarter ended March 31, 2026, signed May 11, 2026 (Q1 10-Q page:63), 63 pages |
| Q2 10-Q | 10-Q_2026-06-30_rkt-20260630.htm.jsonl | 4ca13e8689778101de80b67ba6d799666890bfd97332aef7adca82c2e094e90b | Quarterly report, quarter ended June 30, 2026, signed August 7, 2026 (Q2 10-Q page:68), 68 pages |
| Q3 10-Q | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | 59c56634da7bee8e5debdbfce480876851737d0b5ddf01b6f700d4f40ecd6bce | Quarterly report, quarter ended September 30, 2026, signed October 30, 2026 (Q3 10-Q page:71), 71 pages |
| Q1 release | EX-99.1_2026-05-07_rkt-earningsrelease3312026.htm.jsonl | 7d218dea46aff3c8af9298dca5b852af49f0e5f073ef0f93c5f3b622d0854392 | Earnings release exhibit, first quarter 2026, dated May 7, 2026 (Q1 release page:1), 13 pages |
| Q2 release | EX-99.1_2026-08-06_rkt-063020268xkex991earnin.htm.jsonl | 6542f2db604c3ffa41383bd56c69d56492031f4ee91e3c42b828c315d7979477 | Earnings release exhibit, second quarter 2026, dated August 6, 2026 (Q2 release page:1), 13 pages |
| Q3 release | EX-99.1_2026-10-29_rkt-093020268xkex991earnin.htm.jsonl | 51281ba557de6ffcbe69b458cb58d0ccec82e27e457e960477651f50df28d346 | Earnings release exhibit, third quarter 2026, dated October 29, 2026 (Q3 release page:1), 13 pages |

The first line of each pinned text file quotes a different sha256 ("Visible text of ... sha256 ..."): that is the hash of the original HTML document, not of the pinned text file. The hashes in the table are the pinned text-file hashes supplied by CP-OS and are the ones relied on here.

### Run context

| Source | sha256 | Role |
| --- | --- | --- |
| context | 2c3b1fbba94f4a511900e452ab48c8c288b5d2472b9c175cb66b98c0de72d2ac | The user's dated settings for this run. Not issuer evidence. |

### Handoffs supplied

None. CP-0 is the first module of this run and CP-OS supplied no upstream handoff, so there is no handoff module or hash to list.

The pack also holds `_retrieval.json`, which CP-OS ignored as a source. It is retrieval metadata only and was not relied on for any finding.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed or furnished sources cover statements, debt, liquidity and segments for the latest annual report and three quarters, so the four requested analyses can proceed with bounded gaps. | Medium | No indentures, credit agreements, rating reports or facility covenant levels are supplied, and the latest source is dated October 30, 2026. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Instrument-level debt tables are printed for the annual report and each quarter, and the latest ties to the balance sheet. | Debt and maturities can be sourced from filed notes. | High |
| The group changed in 2025 through two acquisitions, and segment and interest presentation changed in 2026. | Year-on-year and annual-to-quarter comparisons need labels for perimeter and presentation. | High |
| Facility covenant levels, guarantor names and rating levels are not printed. | Ranking, covenant headroom and rating-based conclusions cannot be sourced from this pack. | High |
| Interim cash paid for interest is not printed in the quarterly reports. | Cash interest cover cannot be read for 2026 periods. | High |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for each requested consumer (CP-1, CP-1A, CP-2 and CP-5). All seven issuer sources are filed or furnished documents with extracted text on every page (464 of 464 pages carry text, none blank). The filed annual report and quarterly reports hold the authority for statements, debt, commitments, legal matters and regulatory requirements. The earnings releases are furnished management documents and supply non-GAAP reconciliations, outlook and attributed narrative only. Nothing is blocked and no consumer is conditional: every source reports for one registrant, so no critical identity boundary is unresolved. The restrictions are a perimeter change inside the series (Redfin from July 1, 2025 and Mr. Cooper from October 1, 2025), a segment recast and an interest presentation change in 2026, no facility covenant levels or reported covenant ratios, no named guarantors or per-instrument issuer roles, no legal financing documents or rating reports, no interim cash-interest figure, and no source dated between October 30, 2026 and the cutoff. Source sufficiency here does not mean any downstream analysis is complete, and no extraction fidelity review has been done. The next evidence action is to obtain the debt documents and any rating publications, and to confirm whether any filing between October 30, 2026 and November 5, 2026 changes the debt, liquidity or legal position, before leverage, ranking or covenant conclusions are drawn.

### Source assessment

| Alias | Original authority | Entity and perimeter | Period and basis | Key content located (locators) |
| --- | --- | --- | --- | --- |
| 10-K | Filed annual report; audited statements with an Ernst & Young LLP report (10-K page:131 to page:135) and an internal control report (10-K page:215 to page:217) | Rocket Companies, Inc., a holding company, with consolidated subsidiaries (10-K page:139). Includes Redfin from July 1, 2025 and Mr. Cooper from October 1, 2025 (10-K page:159, page:162) | Fiscal years ended December 31, 2025, 2024 and 2023, USD millions, GAAP; two segments, Direct to Consumer and Partner Network (10-K page:139, page:206) | Business 10-K page:5 to page:12; risk factors page:13 to page:93; MD&A page:98 to page:122; adjusted EBITDA reconciliation page:103 to page:104; statements page:135 to page:138; acquisitions page:159 to page:166; borrowings page:176 to page:181; commitments and legal page:197 to page:201; regulatory net worth page:201 to page:203; segments page:204 to page:207; controls page:214 to page:217; exhibits page:219 to page:223 |
| Q1 10-Q | Filed interim report, unaudited | Rocket Companies, Inc. consolidated, with Redfin and Mr. Cooper for the whole quarter; Nationstar Mortgage merged into Rocket Mortgage in the quarter (Q1 10-Q page:35) | Quarter ended March 31, 2026 against 2025 comparatives, USD millions; two segments (Q1 10-Q page:6, page:35) | Statements page:4 to page:6; basis and reclassification page:8; borrowings page:24 to page:27; legal page:33 to page:34; regulatory page:34 to page:35; segments page:35 to page:38; MD&A page:48 to page:59 including liquidity page:59; controls page:61 |
| Q2 10-Q | Filed interim report, unaudited | Rocket Companies, Inc. consolidated | Quarter and six months ended June 30, 2026, USD millions; one segment, Mortgage, with prior periods recast (Q2 10-Q page:38) | Statements page:4 to page:7; borrowings page:25 to page:29, including a footnote that the revolving credit facility was increased to 2,500 and extended after quarter end (Q2 10-Q page:28); legal page:36 to page:37; regulatory page:37 to page:38; segments page:38 to page:41; liquidity page:64; exhibit 10.1 revolving credit agreement listed page:67 |
| Q3 10-Q | Filed interim report, unaudited | Rocket Companies, Inc. consolidated; wholly owned subsidiaries and VIEs where it is primary beneficiary (Q3 10-Q page:9); a 24.9% non-controlling interest in Roosevelt (Q3 10-Q page:16) | Quarter and nine months ended September 30, 2026, USD millions; one segment, Mortgage (Q3 10-Q page:8, page:42) | Statements page:4 to page:8; basis, reclassification and subsequent events page:9 to page:10; acquisitions and pro forma page:16 to page:19; fair value of senior notes page:23; borrowings page:27 to page:31; contingencies page:37 to page:41; regulatory page:41 to page:42; segments page:42 to page:45; MD&A page:47 to page:68; liquidity page:67; controls page:69 to page:70; exhibits page:70 to page:71 |
| Q1 release | Furnished management document; attributed claims | Rocket Companies, Inc. (Q1 release page:1) | Quarter ended March 31, 2026; Direct to Consumer and Partner Network segments (Q1 release page:4) | Summary and liquidity page:1; outlook page:3; balance sheet highlights page:4; statements page:5 to page:6; reconciliations page:6 to page:8 |
| Q2 release | Furnished management document; attributed claims | Rocket Companies, Inc. (Q2 release page:1) | Quarter and six months ended June 30, 2026; Mortgage segment with prior periods recast (Q2 release page:4) | Summary page:1; liquidity page:2; senior notes issued June 9 page:3; outlook page:4; statements page:5 to page:6; reconciliations page:7 to page:9 |
| Q3 release | Furnished management document; attributed claims | Rocket Companies, Inc. (Q3 release page:1) | Quarter and nine months ended September 30, 2026; Mortgage segment (Q3 release page:3) | Summary page:1; liquidity page:2; outlook page:3; balance sheet highlights page:4; statements page:5 to page:6; segment summary page:6; reconciliations page:6 to page:8; non-GAAP definitions page:9 to page:10 |

### Version, perimeter and duplicate relationships

- One registrant throughout. Every source is a report of Rocket Companies, Inc. The Q3 10-Q describes it as a holding company whose primary material assets are its equity interests in Rocket GP, LLC, Rocket LP, LLC and Redfin, with Rocket Mortgage, LLC among the entities wholly owned through Rocket Limited Partnership (Q3 10-Q page:8). Nationstar Mortgage was merged into Rocket Mortgage in the first quarter of 2026 (Q1 10-Q page:35; Q3 10-Q page:42).
- Perimeter change inside the series. The Q3 10-Q states "On July 1, 2025 and October 1, 2025, Rocket Companies completed the acquisitions of Redfin and Mr. Cooper, respectively" (Q3 10-Q page:8). The nine-month 2025 comparatives therefore hold Redfin for one quarter and no Mr. Cooper; the December 31, 2025 balance sheet holds both. The 10-K states that revenue and net income since the acquisition dates are not provided because legacy results cannot be distinguished (10-K page:165). Unaudited pro forma revenue and net income are printed for the full years 2025 and 2024 (10-K page:165) and for the third quarter and nine months of 2025 (Q3 10-Q page:19).
- Up-C structure collapsed on June 30, 2025; only Class A and Class L common stock are outstanding afterwards (Q3 10-Q page:8), and Class D common shares were retired on that date (Q3 release page:7). Per-share and non-controlling-interest comparisons for 2025 cross this boundary.
- Segment presentation changed. The 10-K and Q1 10-Q report two segments; from the second quarter of 2026 the company reports one segment, Mortgage, with an All Other category and prior periods recast (Q2 10-Q page:38; Q3 10-Q page:42). The Q1 release is on the old basis (Q1 release page:4); the Q2 and Q3 releases are on the new basis (Q2 release page:4; Q3 release page:3 and page:6). Fiscal 2025 segment results on the new basis are not printed; the recast covers 2025 quarters and year-to-date periods only.
- Income statement presentation changed. From the first quarter of 2026 interest items were reclassified and prior-period amounts conformed (Q3 10-Q page:9 to page:10). The Q3 10-Q prints reclassified amounts for the third quarter and nine months of 2025 only. The 10-K is on the earlier captions, "Interest income, net" and "Interest and amortization expense on non-funding debt" (10-K page:136, page:103).
- No source is a duplicate of another. The releases repeat figures that the 10-Qs later file, but they are separate furnished documents of earlier date and are not independent evidence of the same figures. The 10-K is the retained source for fiscal 2025 and the December 31, 2025 balances; each 10-Q repeats the December 31, 2025 balance sheet as a comparative. The Q3 release is dated October 29, 2026 and refers to a "forthcoming" Form 10-Q (Q3 release page:4); the Q3 10-Q is signed October 30, 2026 (Q3 10-Q page:71).
- Roles of issuer, borrower, guarantor and instrument. The context names no borrower, parent or guarantors. The notes state that the Senior Notes restrict "our subsidiary guarantors" but do not name them (Q3 10-Q page:31; 10-K page:177). The revolving credit agreement is listed as an exhibit with "the Guarantors party thereto" (Q3 10-Q page:71). The 10-K says Rocket Mortgage, LLC assumed the Nationstar notes that were not tendered (10-K page:165); the debt table does not label an issuer per line (Q3 10-Q page:30). The entity-by-instrument mapping is an open distinction.

### Coverage by evidence need

| Evidence need | Status | Locators and limitation |
| --- | --- | --- |
| Income statement, balance sheet, cash flow | Retained | 10-K page:135 to page:138; Q1 10-Q page:4 to page:6; Q2 10-Q page:4 to page:7; Q3 10-Q page:4 to page:8. Interim cash flows are year-to-date only. The annual statements carry the pre-2026 interest captions. |
| Discrete quarters | Partly retained | Adjusted EBITDA for the first, second and third quarter of 2026 is printed (Q1 release page:8, Q2 release page:9, Q3 release page:8). A discrete fourth quarter of 2025 is not printed: no fourth quarter release is in the pack. |
| Quarter versus year-to-date | Retained | Q3 10-Q page:5 and Q3 release page:5 print three-month and nine-month columns; Q2 release page:6 prints three-month and six-month columns; Q1 release page:5 to page:6 prints the quarter only. |
| Fiscal years | Retained | 10-K page:136 to page:138 print 2025, 2024 and 2023. |
| Segments and KPIs | Retained, two bases | Old basis: 10-K page:204 to page:207, Q1 10-Q page:35 to page:38, Q1 release page:4. New basis: Q2 10-Q page:38 to page:41, Q3 10-Q page:42 to page:45, Q2 release page:6, Q3 release page:6. Volume, margin and servicing portfolio KPIs: Q3 10-Q page:49 to page:66; 10-K page:105 to page:117. |
| Add-backs and non-GAAP | Retained | Adjusted revenue, adjusted net income and adjusted EBITDA reconciliations: Q3 release page:6 to page:8; Q2 release page:7 to page:9; Q1 release page:6 to page:8; Q3 10-Q page:51 to page:56; 10-K page:100 to page:104. The 10-K prints fiscal 2025 adjusted EBITDA (10-K page:104). The definition includes interest on secured financing and excludes bond interest (Q3 release page:10). |
| Facility-level debt and carrying values | Retained | Secured facilities by line with collateral, maturity, line size, committed amount and outstanding balance: Q3 10-Q page:27 to page:29. Senior notes by instrument with rate, maturity and principal, plus premium, discount and issuance costs: Q3 10-Q page:30 to page:31. Fair value of senior notes: Q3 10-Q page:23. December 31, 2025 comparatives are in the same tables and in 10-K page:177 to page:181. |
| Debt maturities | Partly retained | Maturity dates by instrument are in the Q3 10-Q tables (page:28 to page:30). A maturities-by-year table for the senior notes is printed only as of December 31, 2025 (10-K page:181). |
| Liquidity | Retained | Total liquidity and its three components in Q1 10-Q page:59, Q2 10-Q page:64, Q3 10-Q page:67 and each release (Q1 release page:1, Q2 release page:2, Q3 release page:2). How the undrawn available MSR and advance line amount is derived is not stated (see Calculations and Gaps). |
| Covenants | Retained as note summary | Types only: minimum tangible net worth, minimum liquidity, maximum total debt or liabilities to net worth, pretax net income, other customary covenants, with compliance stated (Q3 10-Q page:27; 10-K page:176). Facility-level levels and the issuer's reported ratios are not printed. Regulatory minimums are printed: minimum net worth of approximately $3,500, minimum liquidity of approximately $1,500 and a 6% capital ratio (Q3 10-Q page:42). |
| Cash-paid interest and tax | Partly retained | Fiscal 2025 cash paid for interest and for income taxes is printed in the 10-K cash flow statement (10-K page:138). Not printed in the Q1, Q2 or Q3 10-Q: the cash flow statements end with non-cash investing items (Q3 10-Q page:7 to page:8). |
| Leases, purchase commitments, tax receivable agreement | Retained | Related party leases Q3 10-Q page:31; leases 10-K page:183 to page:184; purchase commitments 10-K page:122; tax receivable agreement 10-K page:79 to page:81 and page:190 to page:192, Q3 10-Q page:33 to page:34. |
| Contingencies and litigation | Retained | HouseCanary, the Mr. Cooper data breach class action and the real estate commission antitrust matters: Q3 10-Q page:38 to page:40; reserves and the judgment-default threshold in funding facilities: Q3 10-Q page:41. |
| Business, ownership and transaction narrative | Retained | Business 10-K page:5 to page:12; control by Mr. Gilbert and controlled company status 10-K page:83 to page:86; Class L conversion terms 10-K page:90; acquisitions Q3 10-Q page:16 to page:19. The proxy statement with ownership detail is incorporated by reference and not supplied (10-K page:219). |
| Subsequent events and post-quarter items | Retained, thin | Q3 10-Q page:10 refers to the borrowing note; page:29 lists facility extensions, one maturity and a personal loan facility increase after September 30, 2026. The latest source is signed October 30, 2026 (Q3 10-Q page:71). |
| Legal financing documents | Not supplied | No indenture, credit agreement or amendment. Long-term debt instruments are omitted under Item 601(b)(4)(iii) (Q3 10-Q page:70) and the revolving credit agreement is listed with partial redaction (Q3 10-Q page:71). Context `legal_documents` is `none`. |
| Ratings | Not supplied | Searched all seven sources for Moody's, S&P, Fitch, KBRA, DBRS and for rating, upgrade and downgrade wording. The only match is the regulatory requirement for servicer and corporate credit ratings from two agencies (Q3 10-Q page:42; 10-K page:203), with no agency, level or outlook. Context ratings list is empty. |
| Earnings presentation slides and call | Not supplied | The pack holds releases instead of slides. The Q3 release announces a call on October 29, 2026 (Q3 release page:4); no transcript is supplied. |

### Source conflicts and scope differences

| Item | Source A (locator) | Source B (locator) | Downstream effect |
| --- | --- | --- | --- |
| Segment basis for fiscal 2025 versus 2026 | 10-K page:139 and page:206: two reportable segments, Direct to Consumer and Partner Network | Q3 10-Q page:42: "it has one reportable segment, Mortgage", with prior periods recast | No fiscal 2025 figures on the new basis are printed. Segment trends must use either the old basis (to the first quarter of 2026) or the new basis (from the second quarter of 2026, with 2025 quarters recast) and say which. |
| Interest captions in adjusted EBITDA | 10-K page:103: "Interest and amortization expense on non-funding debt" in the adjusted EBITDA reconciliation | Q3 release page:8 and page:10: "Bond interest expense", with interest on secured financing left inside the measure | Labels differ and the Q3 10-Q prints reclassification amounts for 2025 quarters only (page:10). Whether fiscal 2025 adjusted EBITDA of $1,281 (10-K page:104) is on the identical basis as the 2026 reconciliations is not stated; the definitions read alike but are not confirmed identical. |
| Undrawn availability on MSR and advance lines | Q3 10-Q page:67: "$6.2 billion of undrawn available MSR and advance lines of credit" | Q3 10-Q page:28: MSR and advance facilities total line amount $8,825, committed $4,475, outstanding $1,801 | The note does not print an undrawn or available column and the printed amount cannot be reproduced from it (Calculations). Liquidity built from the note and liquidity as stated may differ. |
| Fiscal 2025 maturity table versus current notes | 10-K page:181: 2026 maturity of 1,150 and 2028 maturity of 62 | Q3 10-Q page:30 to page:31: both notes redeemed during the nine months; new notes of 900 due 2031 and 600 due 2034 issued | The December 31, 2025 maturity table is stale for the 2026 and 2028 rows. A current maturity profile must come from the Q3 10-Q instrument table. |
| Class L share counts | Q3 10-Q page:1: 924,439,745 Class L shares outstanding at October 23, 2026 | Q3 10-Q page:46: 924,439,710 converted in the quarter | Not a conflict: 1,848,879,455 at December 31, 2025 less 924,439,710 converted equals 924,439,745 (Q3 10-Q page:4). Recorded to show it was checked. |
| Release and 10-Q for the same quarter | Q3 release page:5 to page:6 statements | Q3 10-Q page:4 to page:5 statements | Balance sheet and income statement lines compared are identical. Release liquidity figures repeat Q3 10-Q page:67. The release is attributed management communication; the filing governs. |

### Consumer readiness

| Consumer | Status | Evidence demand and carried limitations |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Needs statements, debt table, maturities, liquidity, adjusted EBITDA and interest inputs by period. All are located for fiscal 2025 and each 2026 quarter. Limitations: perimeter change; segment recast and interest caption change; no discrete fourth quarter 2025; no interim cash paid for interest; undrawn MSR and advance line availability not derivable; covenant levels not printed; adjusted EBITDA is management-defined and is printed in the releases and in the MD&A of the filings, not in the audited statements. |
| CP-1A | READY_WITH_LIMITATIONS | Needs business model, ownership, transaction and governance facts. The business section, the Up-C collapse, the Redfin and Mr. Cooper acquisitions, control by Mr. Gilbert and the Class L conversion terms are located. Limitations: ownership percentages and board detail sit in an unsupplied proxy statement; no sponsor in context; no guarantor list; the 10-K internal control assessment excludes the acquired businesses (10-K page:214). |
| CP-2 | READY_WITH_LIMITATIONS | Needs the upstream registers only. The source set supports strengths, weaknesses and risks from filings. Limitations: no ratings, market quotes or peers (context blank, not zero); management claims in the releases are attributed and cannot override the filings; CP-1 limitations carry over. |
| CP-5 | READY_WITH_LIMITATIONS | Needs located quotes for every cited fact. All seven sources have page-numbered text. Limitations: tables are flattened in extraction, so row and column alignment must be checked against each quote; charts or images in the releases, if any, are not visible in text; extraction fidelity is not reviewed. |

For any later HTML model objective the source assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This module asserts no normalized quarters, no reconciliation and no acceptance of downstream inputs.

## Calculations

No financial metric was calculated or normalized in this module. The following are footing and tie checks of printed figures, made to test extraction fidelity and to locate gaps. They are not analysis. Amounts are USD millions unless stated.

| Check | Inputs (locator) | Result | Printed total |
| --- | --- | --- | --- |
| Senior notes principal foots, September 30, 2026 | 503 + 750 + 12 + 738 + 2,000 + 76 + 1,250 + 900 + 64 + 45 + 955 + 2,000 + 850 + 600 (Q3 10-Q page:30) | 10,743 | Total Senior Notes 10,743 (Q3 10-Q page:30) |
| Senior notes carrying value | 10,743 + 39 premium net of discount - 66 issuance costs (Q3 10-Q page:30) | 10,716 | Total Senior Notes, net 10,716 (Q3 10-Q page:30; balance sheet page:4) |
| Senior notes principal foots, December 31, 2025 | 1,150 + 503 + 62 + 750 + 12 + 738 + 2,000 + 76 + 1,250 + 64 + 45 + 955 + 2,000 + 850 (Q3 10-Q page:30) | 10,455 | Total Senior Notes 10,455 (Q3 10-Q page:30; 10-K page:181) |
| December 31, 2025 maturity table foots | 1,150 + 503 + 62 + 1,500 + 2,076 + 5,164 (10-K page:181) | 10,455 | Total 10,455 (10-K page:181) |
| Secured financing foots, September 30, 2026 | 12,042 mortgage loan funding + 1,801 MSR and advance + 344 personal loan (Q3 10-Q page:28 to page:29) | 14,187 | Total Secured Financing 14,187 (Q3 10-Q page:29; balance sheet page:4) |
| Secured financing foots, December 31, 2025 | 13,851 + 3,781 + 304 (Q3 10-Q page:28 to page:29) | 17,936 | 17,936 (Q3 10-Q page:29; balance sheet page:4) |
| Facility line and committed amounts foot | Line 27,750 + 8,825 + 950; committed 2,250 + 4,475 + 675 (Q3 10-Q page:28 to page:29) | Line 37,525; committed 7,400 | 37,525 and 7,400 (Q3 10-Q page:29) |
| Mortgage loan funding rows foot | Eighteen printed outstanding balances (Q3 10-Q page:27 to page:28; two facilities show N/A) | 12,042 | Total Mortgage loan funding 12,042 (Q3 10-Q page:28) |
| Liquidity components as stated | 2.7 + 2.5 + 6.2 billion (Q3 10-Q page:67) | 11.4 billion | "total liquidity of $11.4 billion" (Q3 10-Q page:67; Q3 release page:2) |
| Cash component against balance sheet | Cash and cash equivalents 2,699 (Q3 10-Q page:4) | 2.7 billion at printed rounding | $2.7 billion (Q3 10-Q page:67) |
| Undrawn lines of credit component | Revolving credit facility committed 2,500 less outstanding 0 (Q3 10-Q page:30) | 2,500 | $2.5 billion (Q3 10-Q page:67) |
| Undrawn available MSR and advance lines, attempted tie | Line 8,825 less outstanding 1,801; committed 4,475 less outstanding 1,801 (Q3 10-Q page:28) | 7,024 and 2,674 | $6.2 billion (Q3 10-Q page:67) matches neither; basis not stated |
| Cash and restricted cash | 2,699 + 240 (Q3 10-Q page:11) | 2,939 | 2,939 (Q3 10-Q page:11) |
| Adjusted EBITDA, discrete quarters tie to nine months 2026 | 738 (Q1 release page:8) + 766 (Q2 release page:9) + 748 (Q3 release page:8) | 2,252 | 2,252 (Q3 release page:8) |
| Adjusted EBITDA, discrete quarters tie to nine months 2025 | 169 (Q1 release page:8) + 172 (Q2 release page:9) + 349 (Q3 release page:8) | 690 | 690 (Q3 release page:8) |
| Total revenue, net, 2026 | 2,941 (Q1 release page:1) + 2,784 (Q2 release page:1) + 3,284 (Q3 release page:1) | 9,009 | 9,009 (Q3 release page:1; Q3 10-Q page:5) |
| Total revenue, net, 2025 | 1,101 (Q1 release page:1) + 1,451 (Q2 release page:1) + 1,695 (Q3 release page:1) | 4,247 | 4,248 (Q3 release page:1); one million rounding, which the releases say may not foot (Q3 release page:1) |
| Net income, 2026 | 297 (Q1 release page:1) + 229 (Q2 release page:1) + 709 (Q3 release page:1) | 1,235 | 1,235 (Q3 release page:1; Q3 10-Q page:5) |
| Legacy notes not tendered against residual lines | 750 - 738 = 12; 1,000 - 955 = 45; 650 - 574 = 76; 600 - 536 = 64 (10-K page:165) | 12, 45, 76 and 64 | Lines of 12, 45, 76 and 64 in the Q3 10-Q table (page:30); suggests, but does not state, which lines are the assumed legacy notes |
| Class L shares | 1,848,879,455 less 924,439,710 converted (Q3 10-Q page:4, page:46) | 924,439,745 | 924,439,745 outstanding (Q3 10-Q page:4) |
| Goodwill | 10,057 Mortgage + 629 other (Q3 10-Q page:32) | 10,686 | 10,686 (Q3 10-Q page:4) |
| Acquisition consideration | Mr. Cooper 13,667 + 193 + 3,113; Redfin 1,466 + 24 + 252 (Q3 10-Q page:16 to page:17) | 16,973 and 1,742 | 16,973 and 1,742 (Q3 10-Q page:16 to page:17) |
| Coverage counts | 223 + 63 + 68 + 71 + 13 + 13 + 13 pages | 464 of 464 pages with extracted text | Page counts from the pinned files |

The first-quarter 2026 figures in the 2026 ties come from the first quarter release, which is on the earlier segment basis; the tie is arithmetic on consolidated totals and does not establish comparability of segments.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Facility-level covenant levels and the issuer's reported covenant ratios are not printed; only covenant types and compliance statements appear (Q3 10-Q page:27; 10-K page:121 and page:176). All seven sources were searched for covenant wording; the releases contain none. | Medium | CP-1, CP-2 | Obtain the revolving credit agreement and key repurchase agreements before any headroom statement. Until then cite compliance statements and the regulatory minimums only. |
| No indentures, credit agreement text, amendments or guarantor lists. Named guarantors and per-instrument issuer roles are unresolved; the debt table has no issuer column (Q3 10-Q page:30). | Medium | CP-1A, CP-2 | Obtain the indentures and guarantor exhibit. Treat the Rocket Mortgage, LLC assumption of legacy notes as stated in 10-K page:165 and not mapped to lines. |
| No rating agency, level or outlook; context ratings empty. | Medium | CP-2 | Obtain agency publications dated on or before 2026-11-05. |
| Interim cash paid for interest and taxes is not printed in the quarterly reports; fiscal 2025 is printed (10-K page:138). Searched all seven sources for "paid for interest", "interest paid", "taxes paid" and "paid for income tax". | Medium | CP-1 | Use fiscal 2025 as the only cash-basis point and show interest expense (Q3 10-Q page:5) separately on an accrual basis. |
| Fiscal 2025 segment results on the new Mortgage basis and the fiscal 2025 income statement on the 2026 interest captions are not printed; reclassification amounts are printed for 2025 quarters and year-to-date periods only. | Medium | CP-1, CP-2 | Compare 2026 with 2025 quarters on the recast basis; do not mix the 10-K segment tables or interest captions with 2026 figures without a label. |
| Perimeter: nine-month 2025 comparatives hold one quarter of Redfin and no Mr. Cooper; pro forma figures are unaudited and cover revenue and net income only (10-K page:165; Q3 10-Q page:19). | Medium | CP-1, CP-1A, CP-2, CP-5 | Label every year-on-year comparison with its perimeter. Use pro forma figures only as labelled supporting data. |
| No discrete fourth quarter 2025 and no fourth quarter release in the pack. Fiscal 2025 adjusted EBITDA is printed in the 10-K, so a last-twelve-month figure can be built from printed components, subject to the basis point under conflicts. | Low | CP-1 | Build any last-twelve-month figure from fiscal 2025 plus nine months 2026 less nine months 2025, with the basis stated, or obtain the fourth quarter 2025 release. |
| The basis of "undrawn available MSR and advance lines" ($6.2 billion) is not stated and cannot be reproduced from the note. Cash of $2.7 billion includes buy-down funds and margin cash held for counterparties, and those amounts are not printed (Q3 10-Q page:27 and page:67). | Medium | CP-1, CP-2 | Present liquidity as the company states it, attributed, and show the note-based figures separately. Ask for the availability basis before using the amount for coverage. |
| No source is dated after October 30, 2026 although the cutoff is 2026-11-05. Any filing in that window, further facility changes, the HouseCanary judgment (not yet entered, Q3 10-Q page:38), and rating or financing events are unverified. | Medium | CP-1A, CP-2, CP-5 | Obtain the filing list for October 30 to November 5, 2026 and confirm whether any event requires an update. |
| The proxy statement is not supplied, so ownership percentages, board independence detail and related party terms beyond the notes are not available (10-K page:219). | Low | CP-1A | Obtain the 2026 proxy statement if governance weight is needed. |
| Internal control over financial reporting for the 2025 annual report excludes Redfin and Mr. Cooper (10-K page:214). The Q3 10-Q reports no change in internal control that materially affected it (Q3 10-Q page:69). | Low | CP-5 | Carry as an inherited limitation on the 10-K's acquired-business figures. |
| Possible charts or images in the releases are not visible in text extraction and are not inspected. No earnings call transcript or slides are supplied. | Low | CP-1A, CP-2 | Rely on release text only; treat any slide content as unseen. |
| No extraction fidelity review has been performed on any source; flattened tables could misalign columns. | Low | CP-5 | Check each quote against the table rows before use. |

## Next module

Proceed to CP-1 (financial base view) on the filings and releases in this pack, carrying every gap above. It should use the Q3 10-Q instrument tables for debt, label each figure with its period and perimeter, use the recast Mortgage segment basis from the second quarter of 2026, keep the company's stated liquidity attributed and separate from note-based figures, and record covenant levels, guarantors, ratings and interim cash interest as not supplied. CP-1A, CP-2 and CP-5 follow in dependency order. No consumer is marked DO NOT RUN.
