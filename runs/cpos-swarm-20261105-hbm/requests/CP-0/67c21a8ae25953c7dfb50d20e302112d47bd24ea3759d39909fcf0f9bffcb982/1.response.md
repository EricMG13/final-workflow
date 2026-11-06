## Request

Issuer: Hudbay Minerals Inc. (issuer id hbm; TSX and NYSE ticker HBM; Canadian registrant filing on Form 40-F, SEC file number 001-34244). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. Current period named by the context: Q2 2026 (quarter and six months ended 2026-06-30). Prior period named by the context: FY2025.

Question for this module: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize, reconcile or calculate figures. Arithmetic in `## Calculations` is limited to tie-outs that test whether sources agree with each other.

Assertion: SOURCE_SUFFICIENCY_ONLY. Source sufficiency is not completion of any downstream analysis.

The context file holds run settings and is not issuer evidence. Its deal terms, quotes, ratings, peers, precedents and research questions are empty, its borrower, parent and guarantor fields are blank, and its market capitalisation, net debt and EV fields are blank. Blanks are treated as not supplied, never as zero.

## Sources

Each issuer source is a JSONL text extraction of an SEC filing. The locator `page:N` is the extraction chunk, not the printed page. The sha256 below is the pinned file hash. Each file also prints a different hash for the underlying htm document in its first line; that one is not used here.

### Issuer sources relied on

| Source name | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 40-F_2025-12-31_form40f.htm.jsonl | 2e155789735b2bff45a2bcbe054290dc180366fb4697dc24f2f2d4f1c7050c41 | Annual report cover document, Form 40-F, 9 chunks. Filed document, signed "Date: March 26, 2026" (page:8). It incorporates its annual information form, audited statements and MD&A by reference to exhibits that are not in the pack. | Fiscal year ended 2025-12-31 (page:1) |
| 6-K-EX-99.1_2025-09-30_exhibit99-1.htm.jsonl | 55a93575304a5e2b953260f4e274c5a39ae30021f2c92b99af4427f537390e4f | Management's Discussion and Analysis, Exhibit 99.1 to a Form 6-K, 79 chunks, dated "November 11, 2025" (page:1). Filed management narrative with non-GAAP reconciliations. | Three and nine months ended 2025-09-30 (page:1) |
| 6-K-EX-99.1_2026-03-31_exhibit99-1.htm.jsonl | 532cee6ac6a8650d6600327aa510e9427055b8d19ea466fcd1e56834f9e80c49 | Unaudited condensed consolidated interim financial statements and notes, Exhibit 99.1 to a Form 6-K, 25 chunks. Board approval "April 30, 2026" (page:5). Filed statements control their own facts. | Three months ended 2026-03-31 and 2025; balance sheet at 2026-03-31 and 2025-12-31 |
| 6-K-EX-99.1_2026-06-30_exhibit99-1.htm.jsonl | 12a37c8778b0cbc30486cf54048199e1b52e4f3eeea4aa98f015138ba6c8b8ca | Unaudited condensed consolidated interim financial statements and notes, Exhibit 99.1 to a Form 6-K, 32 chunks. Board approval "July 28, 2026" (page:6). Filed statements control their own facts. | Three and six months ended 2026-06-30 and 2025; balance sheet at 2026-06-30 and 2025-12-31 |
| 6-K-EX-99.3_2025-12-31_exhibit99-3.htm.jsonl | 99f49739a1f92152e3b1a86a18c1ee2162a4da0c2cc8d427da3a3335818d9569 | News release dated "February 20, 2026" (page:1), Exhibit 99.3 to a Form 6-K, 55 chunks. Management-prepared; supporting claims and non-GAAP tables, not audited statements. | Fourth quarter and full year 2025; 2026 guidance |
| 6-K-EX-99.3_2026-03-31_exhibit99-3.htm.jsonl | ada0c26b16ac32d6f2b222633c4110e11a601b22fd66b81f76af348b97d3b4a8 | News release dated "May 1, 2026" (page:1), Exhibit 99.3 to a Form 6-K, 37 chunks. Management-prepared; supporting claims. | First quarter 2026 |
| 6-K-EX-99.3_2026-06-30_exhibit99-3.htm.jsonl | 5519d54c6ee343772d1472890091915c574ee3b20549bcd2dd8544703027a844 | News release dated "July 29, 2026" (page:1), Exhibit 99.3 to a Form 6-K, 37 chunks. Management-prepared; supporting claims. This is the latest dated document in the pack. | Second quarter 2026 |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 021d8bac1e30ca507d1d237248f47111a88bf0caf21c22980b85e1e72c6ea47c | Run settings only; not issuer evidence |

### Supplied handoffs

None. CP-0 is the first module in the run, so the handoff set is empty.

### Ignored file

`_retrieval.json` sits in the pack folder and is not a pinned source. It is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The interim statements, releases and one MD&A are enough to start all four downstream modules, with limits. The audited annual statements, annual MD&A, debt documents and covenant levels are not supplied. | Medium | Full-year 2025 figures rest on a news release, and no covenant threshold or executed debt document is in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt, revolver draws, letters of credit and the April 2026 note repayment are printed in the latest interim statements. | Facility-level debt and liquidity can be set out from filed statements, not only from management tables. | High |
| Compliance with revolver covenants is stated, but no covenant level, ratio or headroom is printed anywhere in the pack. | Covenant headroom cannot be measured, only the stated compliance. | High |
| Reported liquidity includes cash that the company says is restricted to the Copper World project. | Liquidity available to the wider group is lower than the headline figure and needs separate treatment. | High |
| Two sources disagree on the 2025 year-end share count, and the company's free cash flow history changed between releases. | Per-share and cash flow comparisons need the version stated and the conflict carried forward. | Medium |
| The audited annual statements and annual MD&A named in the annual report are not in the pack. | The full-year 2025 base and the annual contractual obligations table are second-hand or stale. | High |

### Readiness view

The effective source set supports the requested work with limitations. All four requested consumers are assessed as READY_WITH_LIMITATIONS, none CONDITIONAL and none BLOCKED. The pack holds two sets of filed unaudited interim statements with notes (first and second quarter 2026), one filed MD&A (third quarter 2025), the annual report cover document, and three management news releases that together cover the fourth quarter and full year 2025 and the first and second quarters of 2026. All are in USD, the context's reporting currency, and all are dated on or before 2026-07-29, inside the cutoff. The binding limitations are five. First, the audited FY2025 statements, annual information form and annual MD&A are incorporated by the annual report but not supplied, so FY2025 income and cash flow figures come from a news release and the 2025-12-31 balance sheet comes from interim comparatives. Second, no indenture, credit agreement or other executed legal document is supplied, so covenant levels, guarantor lists, security and borrower identity rest on filing summaries. Third, nothing dated after 2026-07-29 is supplied, so events between that date and the cutoff are Not supplied, not absent. Fourth, the text extraction has had no fidelity review and charts or images were not inspected. Fifth, three cross-source conflicts (listed below) must be carried forward by name. None of these prevents a consumer from starting.

### Consumer assessment

| Consumer | Status | Evidence located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Interim balance sheets, income statements, cash flow statements and debt, lease, commitments and segment notes for Q1 and Q2 2026 (Q2 statements page:1-3, notes page:18-20, page:29, page:31-32); discrete Q3 2025 and nine-month data in the MD&A (page:9); Q4 and FY2025 headline figures in the release (page:10-11) | FY2025 statements not audited-statement sourced; quarterly MD&A for Q1 and Q2 2026 not supplied; contractual obligations table is dated 2025-09-30; FY2025 cash-paid interest and tax not printed |
| CP-1A | READY_WITH_LIMITATIONS | Reporting entity and operations (Q2 statements page:4-5), Arizona Sonoran acquisition (page:8), Copper World joint venture (page:9), Copper Mountain minority purchase (page:9-10), segment note (page:30-32), management narrative in the releases | Annual information form not supplied; Wheaton enhanced stream agreement is described as not yet consummated and its text is not supplied; no litigation or contingencies note in the interim statements |
| CP-2 | READY_WITH_LIMITATIONS | Can synthesise from CP-1 and CP-1A plus located liquidity, net debt, restricted cash, compliance statements and capital commitments | Covenant levels and headroom, ratings, market data and valuation inputs are Not supplied |
| CP-5 | READY_WITH_LIMITATIONS | Every source carries chunk locators and exact text, so claims can be traced and tied out across the three release versions and two interim statements | Extraction fidelity not reviewed; images and charts not inspected; three conflicts below limit cross-module identity checks |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source-by-source assessment

All seven sources identify Hudbay Minerals Inc. as the registrant or the announcing company. No source is blocked, draft or unsigned, and none is a duplicate of another. The interim statements are unaudited and filed; the filed statements and the filed MD&A control their own facts. The three news releases are management claims and cannot override the statements. Document class was read from content, not from file names. The file names mislead on class: the two "EX-99.1" files for 2026 are financial statements, the "EX-99.1" file for 2025-09-30 is an MD&A, and the three "EX-99.3" files are news releases, whereas in the annual report exhibit index "99.3" is the annual MD&A (40-F page:3, page:8).

| Source | What it supports | Limit |
| --- | --- | --- |
| Annual report 40-F | Registrant identity, fiscal year, auditor named as "Deloitte LLP" (page:4), statement that there are "no off-balance sheet arrangements" material to investors (page:5), exhibit index (page:8-9) | Cover document only. Exhibits 99.1 (annual information form), 99.2 (audited statements) and 99.3 (annual MD&A) are listed but not supplied. Page references to "page 53 of Exhibit 99.3" cannot be opened (page:5) |
| MD&A Q3 2025 | Liquidity and capital resources (page:40-42), contractual obligations table at 2025-09-30 (page:46), quarterly trend table (page:47-50), non-GAAP reconciliations (page:51-55), nine-month cash flows (page:42-43) | Predates the April 2026 note repayment, the January 2026 Copper World joint venture closing and the June 2026 Arizona Sonoran acquisition, so its debt and obligations tables are stale for the current structure |
| Interim statements Q1 2026 | Three-month statements, long-term debt note (page:13-15), subsequent-event note on the repayment (page:25), equity and share note (page:17) | Predates June 2026 events. Quarter basis only |
| Interim statements Q2 2026 | Latest balance sheet (page:1), income statement (page:1-2), cash flows (page:2-3), notes 4 to 26 including debt (page:18-20), commitments (page:29), segments (page:30-32) | No contingencies or litigation note; no subsequent-events note; covenant levels not printed (page:19) |
| Release FY2025 | Q4 and FY2025 financial condition, performance, adjusted EBITDA and free cash flow reconciliations (page:10-11, page:41), 2026 guidance, liquidity (page:5) | Management document; the release links its MD&A and statements on a website (page:37) that are not supplied |
| Release Q1 2026 | Financial condition, liquidity after repayment (page:6), reconciliations (page:23-25) | Management claims |
| Release Q2 2026 | Financial condition and liquidity (page:6), net debt (page:24), trailing adjusted EBITDA and free cash flow (page:25), project and acquisition narrative (page:17-19) | Management claims; contains an internal inconsistency (conflict 3) |

Coverage: every chunk of every source was retained by the extraction (9, 79, 25, 32, 55, 37 and 37 chunks). Pages read in detail for this module: the whole of the Q2 2026 statements; the debt, liquidity, cash flow, contractual obligation and non-GAAP pages of the other sources. Operating reviews by mine, per-tonne cost build-ups, mineral reserve narrative and forward-looking statement boilerplate were classified by heading only. They are retained, not excluded, and are not needed to judge readiness. No chart, image or speaker-note content exists in this text extraction, and none was inspected.

### Entity and perimeter

The reporting entity is Hudbay Minerals Inc. ("HMI" or the "Company"), existing under the Canada Business Corporations Act, with its subsidiaries together referred to as "Hudbay" (Q2 statements page:4). The statements are consolidated. Subsidiaries named in the Q2 statements include "Copper Mountain Mine (BC) Ltd.", "HudBay Peru Inc.", "HudBay Peru S.A.C.", "HudBay (BVI) Inc." and "Hudbay Arizona ULC". Hudbay Arizona ULC "indirectly owns" Arizona Sonoran Copper Company Inc. and 70% of Copper World LLC; Mitsubishi Corporation owns the remaining 30% of Copper World (page:5). Non-controlling interest was 463.4 at 2026-06-30 against nil at 2025-12-31 (page:1). Group figures therefore mix a 70% owned, consolidated project entity with cash that the company says is not available to the rest of the group.

Debt perimeter evidence, as filed:

- Senior unsecured notes: guaranteed "by substantially all of the Company's subsidiaries, other than HudBay (BVI) Inc. and certain excluded or unrestricted subsidiaries, and subsidiaries that hold the Copper World, Mason and Cactus projects" (Q2 statements page:18). The first-quarter statements list the Copper World and Mason projects but not Cactus (Q1 statements page:13), so the Cactus exclusion is new with the June 2026 acquisition.
- Senior secured revolving credit facilities: two facilities, "secured against substantially all of the Company's assets, other than those associated with Copper World, Mason and Cactus projects" (page:19).
- Municipal bonds: "senior unsecured obligations of Copper World LLC and are guaranteed on a senior unsecured basis by the Company and its primary operating subsidiaries" (page:20). This is a project-entity debt with parent guarantee, and its proceeds are restricted to the project (page:14).
- Deferred land payments of 102.8 acquired with Arizona Sonoran are "secured vendor carryback loans" with deeds of trust over land held by "Cactus 110 LLC" (page:16).

Unresolved: the pack does not name the issuer of the senior notes beyond "the Company", the borrowers under the Canadian and Peruvian revolving facilities, the list of guarantors, the restricted-group definition, or which subsidiaries are "excluded or unrestricted". The context names no borrower, parent or guarantor, and that blank is not evidence of their absence.

### Period basis and currency

- Basis: IFRS Accounting Standards; the interim statements follow IAS 34 (Q2 statements page:5). Fiscal year ends December 31. Units: millions of US dollars unless noted (page:1).
- Canadian-dollar items that are not converted in the sources: the C$130.0 million bilateral letter of credit facility (page:20), the C$0.01 per share dividend (page:23, release page:22), and Manitoba and British Columbia unit costs per tonne in C$ (release page:12-13).
- Current period Q2 2026 is covered by filed three-month and six-month statements. Discrete Q1 2026 is covered by its own filed statements. Discrete Q3 2025 appears in the MD&A trend tables, and discrete Q4 2025 appears in the release (page:11). FY2025 income statement figures appear only in the release (page:11); the 2025-12-31 balance sheet appears in the Q1 and Q2 2026 statements as comparatives.
- Full-year 2025 cash flow detail beyond the release's headline lines is not supplied. The cash flow statement for the six months of 2026 prints "Interest paid on long-term debt" and "Taxes paid" (page:2-3); the first-quarter statement prints "Taxes paid" but no interest line (Q1 statements page:2), which implies no interest on long-term debt was paid in the first quarter. A full-year 2025 cash-paid interest or tax figure is Not supplied; the MD&A gives only a nine-month narrative amount for interest paid (page:43).
- Perimeter change: the Arizona Sonoran acquisition closed 2026-06-24 and is accounted for as an asset acquisition; "the Cactus project had no income or expenses recorded during the six day stub period" (Q2 statements page:30). Second-quarter income and cash flow therefore do not carry Cactus operating results, while the 2026-06-30 balance sheet carries its assets and the new deferred land payments. Comparing balance sheet items across 2025-12-31 and 2026-06-30 mixes perimeters.

### Version relationships and conflicts

1. Share count at 2025-12-31. The annual report cover states "As at December 31, 2025, 395,521,903 common shares were outstanding" (40-F page:1). The 2026 interim share capital note shows "Balance, beginning of year 396,834,231" and the same figure in the "Year ended Dec. 31, 2025" column (Q2 statements page:23; Q1 statements page:17). The MD&A reports 396,148,639 shares on 2025-11-10 (MD&A page:46). Downstream effect: per-share, dilution and any equity-value inputs depend on which count is used. The statement note is the filed IFRS source; the 40-F cover is a registrant representation. The sources do not explain the gap, so it is carried as an unresolved conflict.
2. Free cash flow history changed between releases. Fourth quarter 2025 free cash flow is 228.2 with cash sustaining capital expenditures of 108.7 in the February release (release FY2025 page:10-11 and page:41), but 225.0 with 111.9 in the May and July releases (release Q1 page:25; release Q2 page:25). The community agreement cash payments line moves from 4.4 to 7.6 for the same quarter. Third quarter 2025 free cash flow is (15.2) in the MD&A and the February release but (16.1) in the later releases. Downstream effect: any free cash flow series must name the release version and cannot splice versions.
3. Internal inconsistency in the July release. Its trailing table prints fourth quarter 2025 "Cash generated from operations" of 290.4 (release Q2 page:25), while the May release prints 209.4 for that quarter (release Q1 page:25) and the July release's own twelve-month total of 831.2 equals the sum using 209.4 (see Calculations). Its free cash flow of 225.0 for that quarter also agrees with 209.4. The 290.4 figure is therefore not usable until confirmed; the 209.4 figure is used as the consistent value.
4. Municipal bond maturity wording. The statements say the bonds have "an initial mandatory tender date of July 2, 2036" (Q2 statements page:14), while the July release says "solid waste disposal revenue bonds due July 2, 2036" (release Q2 page:18). The final legal maturity is not stated. Downstream effect: the maturity wall for these bonds cannot be placed without the bond terms.
5. Wheaton stream status. The November 2025 MD&A says Hudbay "agreed on terms with Wheaton Precious Metals Corp." to amend the Copper World streaming agreement (MD&A page:5). The February and July 2026 releases both list, among forward-looking items, "the ability to consummate the definitive agreement with Wheaton" and "the benefits, timing and consummation of the definitive agreement with Wheaton" (release FY2025 page:50; release Q2 page:32). The pack does not state whether the definitive agreement was signed. This is a stated uncertainty, not a numeric conflict.

### Debt, liquidity and obligations evidence present

Located in the Q2 2026 statements (amounts in USD millions): total long-term debt 860.2 at 2026-06-30 and 1,008.6 at 2025-12-31 (page:18), made up at 2026-06-30 of senior unsecured notes 539.4, senior secured revolving credit facilities 270.1 and senior unsecured municipal bonds 50.7. Principal outstanding on the 6.125% senior notes due April 2029 is 542.4 (page:18). The 4.50% notes due April 2026 of 472.5 were repaid on 2026-04-01 using cash and a 272.0 revolver draw (page:18). The two revolving facilities total 450.0, mature in November 2028, carry a 150.0 accordion, and had 24.3 of letters of credit outstanding under the Canadian facility and nil under the Peruvian facility (page:19). The municipal bonds are 52.0 at 4.50% (page:20). Other letters of credit and surety bonds, the C$130.0 million letter of credit facility with 55.7 drawn, lease liabilities of 53.0, financing related to property, plant and equipment of 131.3, deferred land payments, deferred and contingent Copper Mountain consideration, community agreements, a Wheaton refund liability of 8.3 and deferred revenue of 297.1 are printed (pages 15-21). Environmental and other provisions total 388.6 (page:21). Capital commitments by segment are printed (page:29).

Located in the July release: total liquidity of 1,044.6 comprising cash of 890.9 and undrawn availability of 153.7, net debt of (80.5) and a trailing adjusted EBITDA of 1,271.6 (release Q2 page:6, page:24-25). Footnote text states cash includes "$334.5 million in cash held by Copper World LLC" that is "contractually restricted for the advancement of the Copper World project and are not available to the general Hudbay group" (page:25). The statements add that the Copper World joint venture cash "is designated for exclusive use by Copper World" (Q2 statements page:9). The headline liquidity figure therefore includes cash the company itself describes as not available to the general group, and it excludes 49.8 of restricted municipal bond proceeds (release page:6).

Compliance statements located: "the Company was in compliance with its covenants under the revolving credit facilities" at 2026-06-30 (page:19), and equivalent wording at 2026-03-31 and 2025-09-30. The C$130.0 million letter of credit facility has "no financial covenants" per the September 2025 MD&A (page:41).

### Information-availability boundary

The latest dated document is the July release of 2026-07-29. The Q2 statements were approved on 2026-07-28. Nothing dated between 2026-07-29 and the cutoff of 2026-11-05 is supplied. The July release describes items as still to come: a Copper World sanctioning decision "on track for late 2026", a Cactus pre-feasibility study in the second half of 2027, a Mason pre-feasibility study, and a quarterly dividend payable on 2026-09-08 (release Q2 page:4, page:19, page:22). Whether any of these, or any third-quarter 2026 report, occurred before the cutoff is Not supplied. Events in that window are unknown, not absent.

### Analytical read-through

Evidence to source risk to downstream consequence:

- Usable coverage. Filed interim statements give facility-level debt, letters of credit, leases, commitments and segments at the latest quarter end, with a 2025-12-31 balance sheet beside them. This lets CP-1 build the balance sheet and debt table from filed statements and use the releases only for non-GAAP measures.
- Strongest contrary evidence. The headline liquidity of 1,044.6 and the net debt of (80.5) are management measures, and the company says part of the cash is restricted to one project (release Q2 page:25). A consumer that adopts the headline without that footnote overstates group liquidity. The same release misprints one trailing cash flow cell (conflict 3).
- Source risk mechanism. The annual figures for FY2025 come from a management release, and the audited statements and annual MD&A that the annual report incorporates are not supplied. The contractual obligations table that is supplied predates the 2026 note repayment, the revolver draw and the acquisition, so it understates the current debt and land payment profile. Free cash flow history changed between releases.
- What cannot proceed. Covenant headroom, because no level or ratio is printed. Guarantor-level and restricted-group analysis, because no debt document is supplied. A current maturity wall from a filed obligations table. Valuation, ratings and relative value, because the context's market and ratings fields are blank. Any view of events after 2026-07-29.
- Next evidence action. Supply the FY2025 audited statements and annual MD&A (Exhibits 99.2 and 99.3 of the annual report), the annual information form (Exhibit 99.1), the 6.125% senior notes indenture, the revolving credit agreements, the municipal bond documents, the Q1 and Q2 2026 MD&As that the releases link, and any filings dated 2026-07-30 to 2026-11-05.

## Calculations

No new analytical calculation. CP-0 does not normalize, reconcile or calculate figures. The following tie-outs test source consistency only. Amounts are USD millions.

| Check | Inputs and locator | Result |
| --- | --- | --- |
| Long-term debt at 2026-06-30 | Notes 539.4 + revolver 270.1 + municipal bonds 50.7 (Q2 statements page:18) | 860.2, equals printed total 860.2 |
| Long-term debt at 2025-12-31 | Current notes 472.1 + non-current notes 538.8 + revolver (2.3) (page:18) | 1,008.6, equals printed total 1,008.6 |
| Notes principal at 2026-03-31 | 472.5 + 542.4 (Q1 statements page:13) | 1,014.9, equals printed 1,014.9 |
| Undrawn revolver at 2026-06-30 | 450.0 commitments - 272.0 drawn - 24.3 letters of credit (page:19) | 153.7, equals printed 153.7 (release Q2 page:6) |
| Total liquidity at 2026-06-30 | Cash 890.9 + undrawn 153.7 (release Q2 page:6) | 1,044.6, equals printed 1,044.6 |
| Total liquidity at 2026-03-31 after repayment | Cash 1,003.8 + (450.0 - 24.8) = 1,429.0, less 472.5 (Q1 statements page:3, page:14; release Q1 page:6) | 956.5, equals printed 956.5 |
| Net debt at 2026-06-30 | 860.2 - 890.9 - 49.8 (release Q2 page:24) | (80.5), equals printed (80.5) |
| Trailing adjusted EBITDA | 321.2 + 421.9 + 385.9 + 142.6 (release Q2 page:25) | 1,271.6, equals printed 1,271.6 |
| Trailing cash generated from operations | 297.0 + 211.3 + 209.4 + 113.5 (release Q2 page:25) | 831.2, equals printed 831.2 |
| Same, using the printed 290.4 | 297.0 + 211.3 + 290.4 + 113.5 | 912.2, does not equal printed 831.2, so 290.4 is inconsistent |
| Q4 2025 free cash flow, May release version | 209.4 + 127.5 - 111.9 (release Q1 page:25) | 225.0, equals printed 225.0 |
| Share count roll to 2026-06-30 | 396,834,231 + 46,794,082 + 516,447 (Q2 statements page:23) | 444,144,760, equals printed 444,144,760 |
| Share count gap at 2025-12-31 | 396,834,231 less 395,521,903 (Q2 statements page:23; 40-F page:1) | 1,312,328 shares unexplained |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Audited FY2025 financial statements, annual MD&A and annual information form named in the annual report are not supplied | High | CP-1, CP-1A, CP-2, CP-5 | Supply Exhibits 99.1, 99.2 and 99.3 of the annual report |
| No indenture, credit agreement, municipal bond document or other executed legal document; covenant levels, step-downs, reported ratios and headroom are Not supplied (search of all sources found only compliance statements) | High | CP-1, CP-2 | Supply the debt documents and the compliance certificates or the MD&A covenant section |
| Issuer, borrower and guarantor identity, restricted group and the excluded or unrestricted subsidiaries not named | High | CP-1, CP-1A, CP-2 | Supply the indenture, credit agreements and subsidiary list |
| Headline liquidity and cash include cash restricted to Copper World LLC (334.5 at 2026-06-30) | High | CP-1, CP-2 | Carry the restriction forward; supply Copper World funding terms |
| Nothing dated 2026-07-30 to 2026-11-05 is supplied, including any Q3 2026 results, Copper World sanction decision, Wheaton definitive agreement or dividend payment | High | CP-1A, CP-2 | Supply filings in that window or confirm none exist |
| Q1 and Q2 2026 MD&As are linked by the releases but not supplied | Medium | CP-1, CP-1A | Supply the two MD&As |
| Contractual obligations table is dated 2025-09-30 and predates the April 2026 repayment, the revolver draw, the municipal bonds and the Arizona Sonoran deferred land payments | Medium | CP-1, CP-2 | Supply the FY2025 MD&A table and a mid-2026 update; the drawn and scheduled amounts in the Q2 statements can be set out as a partial substitute |
| Conflicts 1 to 5 above (share count, free cash flow history change, misprinted trailing cell, municipal bond maturity wording, Wheaton status) are unresolved | Medium | CP-1, CP-2, CP-5 | Carry by name; supply the audited statements and bond terms |
| FY2025 full-year cash-paid interest and cash taxes are Not supplied | Medium | CP-1 | Supply the FY2025 cash flow statement |
| No litigation, contingencies or subsequent-events note in the interim statements; the judicial review application against the New Ingerbelle permit is disclosed only in release narrative (release Q2 page:19) | Medium | CP-1A, CP-2 | Supply the annual information form and annual statements contingencies note |
| Ratings, quotes, market capitalisation, peers and precedents: the context fields are blank | Medium | CP-2 | Supply or confirm out of scope |
| Extraction fidelity not reviewed; charts, images and any speaker material not inspected; operating reviews classified by heading only | Low | CP-5 | Fidelity check against filed htm if the committee needs it |

## Next module

CP-1 runs next, followed by CP-1A, CP-2 and CP-5, per the command sheet above. Each consumer must carry forward these limitations: FY2025 figures rest on a management release; no covenant levels or executed debt documents; headline liquidity includes cash restricted to Copper World; the five named conflicts; the 2025-09-30 contractual obligations table; and the absence of any document after 2026-07-29. CP-1 should prefer the filed interim statements for balance sheet, debt and cash flow facts and use the releases only for non-GAAP measures, naming the release version for any free cash flow figure. CP-5 should treat the 40-F cover share count and the interim note share count as a known conflict, not a tracing failure.
