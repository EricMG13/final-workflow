## Request

Issuer: Magnera Corp (issuer id magn), NYSE ticker MAGN; registrant name in the filings "Magnera Corporation" (formerly Glatfelter Corporation). As-of date and cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, and the filings report in USD millions except per-share data; no other currency or scale applies to any monetary figure (euro appears only in cross-currency swap notionals). Current period per the context: Q3 FY2026, the quarterly period ended June 27, 2026, with the nine months (three quarterly periods) to that date. Prior period per the context: FY2025, the fiscal year ended September 27, 2025.

Task: CP-1 reported financial facts, labelled calculation bridges, the four chart-data selectors, the financials and credit metrics table, and an evidence-based reading of leverage, coverage, cash flow, liquidity, definitions and gaps. Reported facts and calculations are kept apart: every figure in a "Reported" table is copied from a filed statement or a release, every figure marked "calc" is computed in the Calculations section from cited inputs, and nothing is replaced by zero when it is missing. Adjusted EBITDA is the company's own non-GAAP segment measure as printed in the segment note; any other EBITDA is labelled.

Upstream handoff used: the CP-0 source-readiness handoff. Its conclusions carried here: READY_WITH_LIMITATIONS; executed debt documents, revolver availability, letters of credit, revolver covenants, ratings and anything dated after August 6, 2026 are not supplied; interim cash-paid interest and taxes are not supplied; prior-year periods are carve-out and part-period. Where this module corrects or refines CP-0 it says so under "Consistency with the CP-0 handoff".

## Sources

Issuer sources relied on (exact pinned names and sha256). A "page" is a text chunk of the extraction, not a printed page.

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-09-27_form10k.htm.jsonl | 8a2d31e8517added759c44fb832ba0e833b0182f88931d77ac8b15219681b6e7 | FY2025 audited statements, debt note, segment note, cash interest, claims outside debt |
| 10-Q_2025-12-27_form10q.htm.jsonl | fc18cf0b3124192f072f0a094fbc1605152c44349946b7208b65f0ac25d88f0f | Q1 FY2026 statements, debt table, segment note |
| 10-Q_2026-03-28_form10q.htm.jsonl | 00a31fc7f5573cbb41dba62ba9751e7ac35317c740673bba1de0ff348e567d96 | Q2 FY2026 and two-quarter statements, debt table, segment note |
| 10-Q_2026-06-27_form10q.htm.jsonl | 9bf0a737948e12b9a435299f2c1d5be9f80cbb7bbc87ba8bb4baa3f7134d16c0 | Q3 FY2026 and nine-month statements, debt table, liquidity, guidance, controls |
| EX-99.1_2026-02-05_ef20064605_ex99-1.htm.jsonl | 2c929f0530d2fad28d8d608f7ff32ddbeacac9282e05451c75240bd19f5fad90 | Q1 release: guidance, debt payments, management LTM measures |
| EX-99.1_2026-05-07_ef20072634_ex99-1.htm.jsonl | 35c908fa7ed7e14681927f2c36fd3b1ad0328d835bdae7fd06641846130d5ea2 | Q2 release: quarter free cash flow, management LTM measures |
| EX-99.1_2026-08-06_ef20079553_ex99-1.htm.jsonl | 907fd63efeb9c514c2f2ef515ae237b76f56ae49850c45b010a3ceaedd06a508 | Q3 release: management LTM and pro forma adjusted EBITDA, outlook wording |

Context (user settings, not issuer evidence): context, sha256 4a094c245ff44dd6e34e569a37f728533980efba9932af440a0d9b2f6b50325a.

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | a8b15cc07abfbb855ac56418114ac7639ccb07ec7eb0a78b02caf33e517da591 | Source readiness, coverage accounting, gap list, conflicts list |

Locator format below: `[source prefix page:N] "exact text"`, where the prefix is the date part of the source name.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| On filed figures, Magnera's leverage at June 27, 2026 was 5.28x gross and 4.53x net on LTM adjusted EBITDA, down from FY2025. Interest cover is 2.91x on a cash-interest proxy and free cash flow is thin. | Medium | Adjusted EBITDA is a company measure with large add-backs, interim cash interest is not reported, and revolver availability and covenants are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Gross debt was 1,966 and cash 280 at June 27, 2026, against LTM adjusted EBITDA of 372. | Leverage fell from 5.74x gross at FY2025 to 5.28x, from higher LTM EBITDA and 65 of debt repayments. | High |
| Operating income plus depreciation and amortization was 250 LTM, versus 372 adjusted. | On unadjusted earnings, gross leverage is 7.86x; add-backs of 122 carry a third of the adjusted figure. | Medium |
| LTM net interest expense was 151 against operating income of 63, and every period shows a net loss. | Earnings do not cover interest after depreciation; cover of 2.91x depends on adjusted EBITDA. | Medium |
| Nine-month free cash flow was 32 against fiscal 2026 guidance of 90 to 110, and the third quarter was negative. | Delivering guidance needs 58 to 78 in the fourth quarter; working capital absorbed cash in the third quarter. | Medium |
| No debt matures before October 2029 and cash plus the 350 revolver commitment totals 630, but availability is unconfirmed. | Runway is long, yet 500 falls due in 2029 and 1,466 in 2031, and borrowing base and letters of credit are unknown. | Medium |

### Financial base view

The filed statements support a reliable financial base for Magnera Corporation, one consolidated entity, in USD millions across four balance-sheet dates (September 27, 2025, December 27, 2025, March 28, 2026 and June 27, 2026) and the flow periods FY2025, each FY2026 quarter, the nine months to June 27, 2026 and the matching nine months of FY2025. Every total and reconciliation tested foots to the filed statement, and the by-function expense block reconciles to operating income in each tested period (see Calculations). The base is limited, not blocked: earnings are measured on the company's adjusted EBITDA, which carries add-backs of about one third of the adjusted figure on an LTM basis; prior-year comparatives are carve-out and part-period (the Glatfelter business is consolidated only from November 4, 2024); interim cash interest and cash taxes are not reported, so cover uses a labelled proxy that ties exactly to the one reported annual cash interest figure; and the revolver is known only by size, maturity and a no-borrowings statement. Leverage and cover use gross debt principal as printed before the discount line and LTM adjusted EBITDA built from filed figures. No guidance, pro forma or synergy-adjusted release figure enters any ratio.

### Source and definition review

| Item | What the source says | Locator | Treatment |
| --- | --- | --- | --- |
| Entity and perimeter | One consolidated registrant; pre-merger periods are a carve-out of the former parent's business | [10-K_2025-09-27 page:26] "have been prepared on a carve-out basis" | All figures are the consolidated registrant. FY2025 includes the acquired Glatfelter business from November 4, 2024 only |
| Currency and unit | Tables are in millions of dollars | [10-K_2025-09-27 page:26] "tables in millions of dollars, except per share data" | USD millions throughout |
| Adjusted EBITDA definition | Operating income adjusted for items management does not consider indicative of ongoing performance; the CODM's segment profit measure | [10-Q_2026-06-27 page:10] "The Company defines Adjusted EBITDA as operating income adjusted to eliminate the impact of certain items that the Company does not consider indicative of its ongoing operating performance." | Used as the EBITDA for ratios, always labelled "adjusted"; a second basis, operating income plus depreciation and amortization, is shown beside it |
| Add-back categories | Restructuring, transaction and business optimization; Argentina hyperinflation; corporate expense allocation; other non-cash charges (stock compensation, disposals, inventory step-up) | [10-Q_2026-06-27 page:11] "Restructuring, transaction, business optimization and other activities 16 13 52 64" | Add-backs shown as the difference between the two EBITDA bases; the line-by-line table is not re-extracted |
| LTM | Not a filed figure. Releases print LTM adjusted EBITDA; the filings allow the same build as fiscal year plus year-to-date less prior year-to-date | [EX-99.1_2026-08-06 page:6] "Adjusted EBITDA (1) $ 187 $ 95 $ 282 $ 181 $ 83 $ 264 $ 372" | LTM is rebuilt from filed figures and agrees with the release total |
| Release LTM components | The release prints LTM components that differ by one to two from filed-figure builds, offsetting in the total | [EX-99.1_2026-08-06 page:6] "Depreciation and amortization 95 55 150 107 62 169 186" and "Argentina hyperinflation 3 - 3 1 - 1 8" | Filing builds used (D&A 187, Argentina 6); release components are management figures and are not used |
| Gross debt | Debt table lists each instrument before a single discounts, fees and other line | [10-Q_2026-06-27 page:8] "Debt discounts, deferred fees and other (65 )" | Gross debt principal = sum of the instrument lines; carrying total shown beside it |
| Cash interest | Annual net cash interest is printed; interim cash interest is not | [10-K_2025-09-27 page:34] "Net cash interest was $124 million in fiscal 2025" | Interim cover uses interest expense, net less non-cash interest expense, a proxy that gives 124 for FY2025 |
| Instants and flows | Balance sheet items are dates; income and cash flow items are durations; cash flows are cumulative year to date | [10-Q_2026-06-27 page:4] "Three Quarterly Periods Ended" | Quarter cash flows are differences of cumulative columns and are labelled derived |

### Reported statement extracts

Reported income statement (USD millions; negatives in brackets). FY2025 is audited; interim periods are unaudited.

| Line | FY2025 | Q1 FY2026 | Q2 FY2026 | Q3 FY2026 | 9M FY2026 | 9M FY2025 | Locators |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales | 3,204 | 792 | 796 | 857 | 2,445 | 2,365 | [10-K_2025-09-27 page:23] "Net sales $ 3,204 $ 2,187 $ 2,275"; [10-Q_2025-12-27 page:3] "Net sales $ 792 $ 702"; [10-Q_2026-03-28 page:3] "Net sales $ 796 $ 824 $ 1,588 $ 1,526"; [10-Q_2026-06-27 page:3] "Net sales $ 857 $ 839 $ 2,445 $ 2,365" |
| Cost of goods sold | 2,867 | 695 | 701 | 745 | 2,141 | 2,116 | [10-K_2025-09-27 page:23] "Cost of goods sold 2,867 1,950 1,995"; [10-Q_2025-12-27 page:3] "Cost of goods sold 695 631"; [10-Q_2026-03-28 page:3] "Cost of goods sold 701 736 1,396 1,367"; [10-Q_2026-06-27 page:3] "Cost of goods sold 745 749 2,141 2,116" |
| Selling, general and administrative | 190 | 50 | 50 | 56 | 156 | 144 | [10-K_2025-09-27 page:23] "Selling, general and administrative 190 107 110"; [10-Q_2025-12-27 page:3] "Selling, general and administrative 50 47"; [10-Q_2026-03-28 page:3] "Selling, general and administrative 50 47 100 94"; [10-Q_2026-06-27 page:3] "Selling, general and administrative 56 50 156 144" |
| Amortization of intangibles | 50 | 11 | 12 | 11 | 34 | 41 | [10-K_2025-09-27 page:23] "Amortization of intangibles 50 48 51"; [10-Q_2025-12-27 page:3] "Amortization of intangibles 11 14"; [10-Q_2026-03-28 page:3] "Amortization of intangibles 12 14 23 28"; [10-Q_2026-06-27 page:3] "Amortization of intangibles 11 13 34 41" |
| Restructuring and other activities | 89 | 22 | 16 | 23 | 61 | 69 | [10-K_2025-09-27 page:23] "Restructuring and other activities 89 30 24"; [10-Q_2025-12-27 page:3] "Restructuring and other activities 22 32"; [10-Q_2026-03-28 page:3] "Restructuring and other activities 16 23 38 55"; [10-Q_2026-06-27 page:3] "Restructuring and other activities 23 14 61 69" |
| Corporate expense allocation and goodwill impairment | 3 and nil | nil | nil | nil | nil | Not supplied separately | [10-K_2025-09-27 page:23] "Corporate expense allocation 3 21 26"; [10-K_2025-09-27 page:23] "Goodwill and other impairment — 172 —" |
| Operating income (loss) | 5 | 14 | 17 | 22 | 53 | (5) | [10-K_2025-09-27 page:23] "Operating income (loss) 5 (141 ) 69"; [10-Q_2025-12-27 page:3] "Operating income (loss) 14 (22 )"; [10-Q_2026-03-28 page:3] "Operating income (loss) 17 4 31 (18 )"; [10-Q_2026-06-27 page:3] "Operating income (loss) 22 13 53 (5 )" |
| Other expense (income), net | 30 | 3 | (1) | 3 | 5 | 26 | [10-K_2025-09-27 page:23] "Other expense (income), net 30 (9 ) (3 )"; [10-Q_2025-12-27 page:3] "Other expense, net 3 21"; [10-Q_2026-03-28 page:3] "Other (income) expense, net (1 ) 5 2 26"; [10-Q_2026-06-27 page:3] "Other expense, net 3 — 5 26" |
| Interest expense, net | 141 | 40 | 35 | 37 | 112 | 102 | [10-K_2025-09-27 page:24] "Interest expense, net 141 3 —"; [10-Q_2025-12-27 page:3] "Interest expense, net 40 26"; [10-Q_2026-03-28 page:3] "Interest expense, net 35 39 75 65"; [10-Q_2026-06-27 page:3] "Interest expense, net 37 37 112 102" |
| Loss before income taxes | (166) | (29) | (17) | (18) | (64) | (133) | [10-K_2025-09-27 page:24] "Income (loss) before income taxes (166 ) (135 ) 72"; [10-Q_2025-12-27 page:3] "Loss before income taxes (29 ) (69 )"; [10-Q_2026-03-28 page:3] "Loss before income taxes (17 ) (40 ) (46 ) (109 )"; [10-Q_2026-06-27 page:3] "Loss before income taxes (18 ) (24 ) (64 ) (133 )" |
| Net income (loss) | (159) | (34) | (18) | (20) | (72) | (119) | [10-K_2025-09-27 page:24] "Net income (loss) $ (159 ) $ (154 ) $ 38"; [10-Q_2025-12-27 page:3] "Net loss $ (34 ) $ (60 )"; [10-Q_2026-03-28 page:3] "Net loss $ (18 ) $ (41 ) $ (52 ) $ (101 )"; [10-Q_2026-06-27 page:3] "Net loss $ (20 ) $ (18 ) $ (72 ) $ (119 )" |

Reported balance sheet (USD millions at the date shown).

| Line | Sep 27, 2025 | Dec 27, 2025 | Mar 28, 2026 | Jun 27, 2026 | Locators |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 305 | 264 | 303 | 280 | [10-K_2025-09-27 page:24] "Cash and cash equivalents $ 305 $ 230"; [10-Q_2025-12-27 page:3] "Cash and cash equivalents $ 264 $ 305"; [10-Q_2026-03-28 page:3] "Cash and cash equivalents $ 303 $ 305"; [10-Q_2026-06-27 page:3] "Cash and cash equivalents $ 280 $ 305" |
| Accounts receivable | 522 | 553 | 536 | 531 | [10-K_2025-09-27 page:24] "Accounts receivable 522 359"; [10-Q_2025-12-27 page:3] "Accounts receivable 553 522"; [10-Q_2026-03-28 page:3] "Accounts receivable 536 522"; [10-Q_2026-06-27 page:3] "Accounts receivable 531 522" |
| Inventories | 474 | 476 (calc) | 472 (calc) | 498 (calc) | [10-K_2025-09-27 page:24] "Inventories 474 259"; [10-Q_2025-12-27 page:3] "Finished goods 301 303"; [10-Q_2025-12-27 page:3] "Raw materials 175 171"; [10-Q_2026-03-28 page:3] "Finished goods 297 303"; [10-Q_2026-03-28 page:3] "Raw materials 175 171"; [10-Q_2026-06-27 page:3] "Finished goods 297 303"; [10-Q_2026-06-27 page:3] "Raw materials 201 171" |
| Total current assets | 1,423 | 1,365 | 1,407 | 1,392 | [10-K_2025-09-27 page:24] "Total current assets 1,423 886"; [10-Q_2025-12-27 page:3] "Total current assets 1,365 1,423"; [10-Q_2026-03-28 page:3] "Total current assets 1,407 1,423"; [10-Q_2026-06-27 page:4] "Total current assets 1,392 1,423" |
| Accounts payable | 356 | 326 | 369 | 361 | [10-K_2025-09-27 page:24] "Accounts payable $ 356 $ 295"; [10-Q_2025-12-27 page:3] "Accounts payable $ 326 $ 356"; [10-Q_2026-03-28 page:4] "Accounts payable $ 369 $ 356"; [10-Q_2026-06-27 page:4] "Accounts payable $ 361 $ 356" |
| Total current liabilities | 601 | 556 | 605 | 569 | [10-K_2025-09-27 page:24] "Total current liabilities 601 457"; [10-Q_2025-12-27 page:3] "Total current liabilities 556 601"; [10-Q_2026-03-28 page:4] "Total current liabilities 605 601"; [10-Q_2026-06-27 page:4] "Total current liabilities 569 601" |
| Long-term debt (carrying) | 1,952 | 1,931 | 1,899 | 1,901 | [10-K_2025-09-27 page:24] "Long-term debt 1,952 —"; [10-Q_2025-12-27 page:4] "Long-term debt 1,931 1,952"; [10-Q_2026-03-28 page:4] "Long-term debt 1,899 1,952"; [10-Q_2026-06-27 page:4] "Long-term debt 1,901 1,952" |
| Other long-term liabilities | 281 | 276 | 258 | 255 | [10-K_2025-09-27 page:24] "Other long-term liabilities 281 94"; [10-Q_2025-12-27 page:4] "Other long-term liabilities 276 281"; [10-Q_2026-03-28 page:4] "Other long-term liabilities 258 281"; [10-Q_2026-06-27 page:4] "Other long-term liabilities 255 281" |
| Total liabilities | 2,925 | 2,855 | 2,857 | 2,817 | [10-K_2025-09-27 page:24] "Total liabilities 2,925 668"; [10-Q_2025-12-27 page:4] "Total liabilities 2,855 2,925"; [10-Q_2026-03-28 page:4] "Total liabilities 2,857 2,925"; [10-Q_2026-06-27 page:4] "Total liabilities 2,817 2,925" |
| Total equity | 1,064 | 1,038 | 1,039 | 1,017 | [10-K_2025-09-27 page:24] "Total equity 1,064 2,139"; [10-Q_2025-12-27 page:4] "Total equity 1,038 1,064"; [10-Q_2026-03-28 page:4] "Total equity 1,039 1,064"; [10-Q_2026-06-27 page:4] "Total equity 1,017 1,064" |

Reported cash flow (USD millions; cumulative year to date in each column).

| Line | FY2025 | Q1 FY2026 | 6M FY2026 | 9M FY2026 | 9M FY2025 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Net cash from operating activities | 103 | 2 | 89 | 76 | 7 | [10-K_2025-09-27 page:24] "Net cash from operating activities 103 192 257"; [10-Q_2025-12-27 page:4] "Net cash from (used in) operating activities 2 (58 )"; [10-Q_2026-03-28 page:4] "Net cash from (used in) operating activities 89 7"; [10-Q_2026-06-27 page:4] "Net cash from operating activities 76 7" |
| Additions to property, plant and equipment | (67) | (15) | (29) | (44) | (52) | [10-K_2025-09-27 page:24] "Additions to property, plant and equipment (67 ) (72 ) (88 )"; [10-Q_2025-12-27 page:4] "Additions to property, plant and equipment (15 ) (16 )"; [10-Q_2026-03-28 page:4] "Additions to property, plant and equipment (29 ) (39 )"; [10-Q_2026-06-27 page:4] "Additions to property, plant and equipment (44 ) (52 )" |
| Non-cash interest expense | 17 | 7 | 13 | 18 | 12 | [10-K_2025-09-27 page:24] "Non-cash interest expense 17 5 5"; [10-Q_2025-12-27 page:4] "Non-cash interest expense 7 3"; [10-Q_2026-03-28 page:4] "Non-cash interest expense 13 8"; [10-Q_2026-06-27 page:4] "Non-cash interest expense 18 12" |
| Repayments on long-term borrowings | (484) | (27) | (63) | (65) | (434) | [10-K_2025-09-27 page:25] "Repayments on long-term borrowings (484 ) (2 ) (4 )"; [10-Q_2025-12-27 page:4] "Repayments on long-term borrowings (27 ) (430 )"; [10-Q_2026-03-28 page:4] "Repayments on long-term borrowings (63 ) (432 )"; [10-Q_2026-06-27 page:4] "Repayments on long-term borrowings (65 ) (434 )" |
| Cash at end of period | 305 | 264 | 303 | 280 | 276 | [10-K_2025-09-27 page:25] "Cash and cash equivalents at the end of period $ 305 $ 230 $ 185"; [10-Q_2025-12-27 page:4] "Cash and cash equivalents at the end of period $ 264 $ 215"; [10-Q_2026-03-28 page:4] "Cash and cash equivalents at the end of period $ 303 $ 282"; [10-Q_2026-06-27 page:4] "Cash and cash equivalents at the end of period $ 280 $ 276" |

Reported segment adjusted EBITDA and net sales (USD millions).

| Line | FY2025 | Q3 FY2026 | Q3 FY2025 | 9M FY2026 | 9M FY2025 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Americas net sales | 1,833 | 476 | 473 | 1,353 | 1,366 | [10-K_2025-09-27 page:41] "Americas $ 1,833 $ 1,493 $ 1,531"; [10-Q_2026-06-27 page:11] "Americas $ 476 $ 473 $ 1,353 $ 1,366" |
| Rest of World net sales | 1,371 | 381 | 366 | 1,092 | 999 | [10-K_2025-09-27 page:41] "Rest of World 1,371 694 744"; [10-Q_2026-06-27 page:11] "Rest of World 381 366 1,092 999" |
| Americas adjusted EBITDA | 241 | 71 | 61 | 187 | 181 | [10-Q_2026-06-27 page:11] "Americas $ 71 $ 61 $ 187 $ 181" |
| Rest of World adjusted EBITDA | 113 | 28 | 30 | 95 | 83 | [10-Q_2026-06-27 page:11] "Rest of World 28 30 95 83" |
| Total adjusted EBITDA | 354 | 99 | 91 | 282 | 264 | [10-K_2025-09-27 page:41] "Total adjusted EBITDA $ 354 $ 282 $ 312"; [10-Q_2026-06-27 page:11] "Total adjusted EBITDA $ 99 $ 91 $ 282 $ 264" |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 5.74 | 4.88 | x | At September 27, 2025. Gross debt principal 2,031 and cash 305 over adjusted EBITDA of 354 for FY2025 (calc). FY2025 EBITDA includes the Glatfelter business from November 4, 2024 only; the carrying debt of 1,952 would give 5.51 and 4.65 |
| Q1 FY2026 | 5.52 | 4.79 | x | At December 27, 2025. Gross debt principal 2,004 and cash 264 over LTM adjusted EBITDA of 363 built as FY2025 plus Q1 FY2026 less Q1 FY2025 (calc). Carrying debt of 1,931 would give 5.32 and 4.59 |
| Q2 FY2026 | 5.41 | 4.58 | x | At March 28, 2026. Gross debt principal 1,969 and cash 303 over LTM adjusted EBITDA of 364 (calc). Carrying debt of 1,899 would give 5.22 and 4.39 |
| Q3 FY2026 | 5.28 | 4.53 | x | At June 27, 2026. Gross debt principal 1,966 and cash 280 over LTM adjusted EBITDA of 372 (calc). Carrying debt of 1,901 would give 5.11 and 4.36. On operating income plus depreciation and amortization of 250 the ratios would be 7.86 and 6.74. Excludes operating leases, swaps, pension, environmental and tax claims; all cash is netted although 58 percent is outside the U.S. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 2.85 | x | Adjusted EBITDA of 354 over reported net cash interest of 124 for FY2025 (calc). Debt was raised at the November 4, 2024 closing, so FY2025 interest covers part of the year |
| Q1 FY2026 | 2.71 | x | Proxy, not reported cash interest: LTM adjusted EBITDA of 363 over LTM interest expense, net of 155 less LTM non-cash interest of 21, which is 134 (calc). Interim cash interest paid is not supplied |
| Q2 FY2026 | 2.82 | x | Proxy: LTM adjusted EBITDA of 364 over 151 less 22, which is 129 (calc). Interim cash interest paid is not supplied |
| Q3 FY2026 | 2.91 | x | Proxy: LTM adjusted EBITDA of 372 over 151 less 23, which is 128 (calc). Over interest expense, net of 151 without the adjustment the ratio is 2.46. The same proxy reproduces the reported FY2025 cash interest of 124 exactly (141 less 17) |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 305 | 350 | US$m | At September 27, 2025. Undrawn is the asset-based revolver commitment of 350 with no borrowings; borrowing base, drawn letters of credit and availability are not supplied, so usable capacity may be lower. About 86 percent of cash was outside the U.S. |
| Q1 FY2026 | 264 | 350 | US$m | At December 27, 2025. Same revolver basis and limitation. Cash location stated only as primarily outside the U.S. |
| Q2 FY2026 | 303 | 350 | US$m | At March 28, 2026. Same revolver basis and limitation. About 64 percent of cash was outside the U.S. |
| Q3 FY2026 | 280 | 350 | US$m | At June 27, 2026. Same revolver basis and limitation. About 58 percent of cash was outside the U.S. Revolver matures November 2029; none of the facility expires within twelve months |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| CY2026 | 0 | US$m | At June 27, 2026. The annual report states no maturities before 2029 (position at September 27, 2025); interim reports print no schedule. Voluntary repayments since then reduce, not add, balances |
| CY2027 | 0 | US$m | Same basis as CY2026 |
| CY2028 | 0 | US$m | Same basis as CY2026 |
| CY2029 | 500 | US$m | 4.75% first priority senior secured notes due October 2029, principal as printed. The asset-based revolver (commitment 350, undrawn) also matures November 2029; any springing maturity terms are not supplied |
| CY2030 | 0 | US$m | No instrument in the debt table matures in 2030 |
| CY2031 | 1466 | US$m | Term loan 706 plus 7.25% first priority senior secured notes 760, both November 2031, principal as printed (calc). The annual report labels these as fiscal 2029 and fiscal 2031; if fiscal years end in late September as FY2025 and FY2026 do, October 2029 and November 2031 would fall in fiscal 2030 and fiscal 2032, so calendar years of the printed months are used (inference, not a printed statement). No scheduled amortization is printed in the supplied text |

### Financials and credit metrics

| Metric | FY2025 | Q1 FY2026 | Q2 FY2026 | Q3 FY2026 | 9M FY2026 | 9M FY2025 | LTM to Q3 FY2026 | Basis and locators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales | 3,204 | 792 | 796 | 857 | 2,445 | 2,365 | 3,284 | Reported; LTM is calc (FY2025 plus 9M FY2026 less 9M FY2025) |
| Operating income | 5 | 14 | 17 | 22 | 53 | (5) | 63 | Reported; LTM calc |
| Depreciation and amortization | 206 | 49 | 51 | 50 | 150 | 169 | 187 | Reported in segment notes; LTM calc |
| Operating income plus D&A (EBITDA before add-backs) | 211 | 63 | 68 | 72 | 203 | 164 | 250 | Calc; no goodwill impairment in FY2025 or the interim periods |
| Add-backs in adjusted EBITDA | 143 | 30 | 22 | 27 | 79 | 100 | 122 | Calc: adjusted EBITDA less operating income plus D&A |
| Adjusted EBITDA (company-defined, non-GAAP) | 354 | 93 | 90 | 99 | 282 | 264 | 372 | Reported in segment notes; LTM calc agrees with release |
| Adjusted EBITDA margin on net sales (percent) | 11.0 | 11.7 | 11.3 | 11.6 | 11.5 | 11.2 | 11.3 | Calc |
| Interest expense, net | 141 | 40 | 35 | 37 | 112 | 102 | 151 | Reported; Q2 and Q3 from cumulative columns; LTM calc |
| Non-cash interest expense | 17 | 7 | 6 | 5 | 18 | 12 | 23 | Reported cumulative; quarters calc |
| Interest expense, net less non-cash interest (cash interest proxy) | 124 | 33 | 29 | 32 | 94 | 90 | 128 | Calc; FY2025 equals reported net cash interest of 124 |
| Loss before income taxes | (166) | (29) | (17) | (18) | (64) | (133) | (97) | Reported; LTM calc |
| Net loss | (159) | (34) | (18) | (20) | (72) | (119) | (112) | Reported; LTM calc |
| Cash from operating activities | 103 | 2 | 87 | (13) | 76 | 7 | 172 | Reported FY2025 and cumulative; Q2 and Q3 derived by difference; LTM calc. FY2025 includes the carve-out period before November 4, 2024 |
| Additions to property, plant and equipment | 67 | 15 | 14 | 15 | 44 | 52 | 59 | Reported cumulative; quarters derived |
| Free cash flow (operating cash flow less capex) | 36 | (13) | 73 | (28) | 32 | (45) | 113 | Calc; the company's FY2025 free cash flow of 126 adds 90 of pre-merger cash flow and is not used |
| Cash at period end | 305 | 264 | 303 | 280 | 280 | 276 | 280 | Reported |
| Gross debt principal | 2,031 | 2,004 | 1,969 | 1,966 | 1,966 | Not supplied: 9M FY2025 debt table not in the pack | 1,966 | Calc: sum of instrument lines before discounts; revolver nil |
| Carrying long-term debt | 1,952 | 1,931 | 1,899 | 1,901 | 1,901 | Not supplied: 9M FY2025 balance sheet not in the pack | 1,901 | Reported |
| Net debt (gross principal less cash) | 1,726 | 1,740 | 1,666 | 1,686 | 1,686 | Not supplied: see gross debt | 1,686 | Calc |
| LTM adjusted EBITDA at period end | 354 | 363 | 364 | 372 | 372 | Not applicable: flow column | 372 | Calc |
| Gross debt / LTM adjusted EBITDA (x) | 5.74 | 5.52 | 5.41 | 5.28 | 5.28 | Not applicable: flow column | 5.28 | Calc |
| Net debt / LTM adjusted EBITDA (x) | 4.88 | 4.79 | 4.58 | 4.53 | 4.53 | Not applicable: flow column | 4.53 | Calc |
| Gross debt / LTM operating income plus D&A (x) | 9.62 | Not calculated | Not calculated | Not calculated | Not calculated | Not applicable: flow column | 7.86 | Calc; FY2025 uses 211; quarterly LTM bases not built |
| LTM adjusted EBITDA / cash interest proxy (x) | 2.85 | 2.71 | 2.82 | 2.91 | 2.91 | Not applicable: flow column | 2.91 | Calc; FY2025 uses reported cash interest |
| LTM operating income / interest expense, net (x) | Not calculated | Not calculated | Not calculated | Not calculated | Not calculated | Not applicable: flow column | 0.42 | Calc: 63 over 151 |
| Cash plus undrawn revolver commitment | 655 | 614 | 653 | 630 | 630 | Not supplied: 9M FY2025 revolver position not in the pack | 630 | Calc; availability unconfirmed |

### Interpretation: evidence, risk mechanism, credit implication

Leverage. Evidence: gross debt principal fell from 2,031 at September 27, 2025 to 1,966 at June 27, 2026 through repayments of the term loan (731 to 706) and the 7.25% notes (800 to 760) [10-Q_2026-06-27 page:8] "7.25% First Priority Senior Secured Notes November 2031 760 800", while LTM adjusted EBITDA rose from 354 to 372. Risk mechanism: both legs help, but the EBITDA is a company-defined measure and the gap to operating income plus D&A is 122 LTM. Credit implication: filed-basis leverage of 5.28x gross and 4.53x net is improving but remains above five times gross for a business that reports a net loss in every period shown. Higher LTM EBITDA contributed somewhat more of the improvement than debt repayment (calc: EBITDA change alone gives 5.46, debt change alone 5.55; see Calculations).

Add-backs and definition risk. Evidence: segment notes reconcile adjusted EBITDA to operating income through restructuring and integration charges, Argentina hyperinflation, carve-out allocation and other non-cash charges; the LTM restructuring and other activities charge was 81, and the nine-month charge of 61 splits into severance 13, facility exit 3, non-cash 10 and integration and other 35 [10-Q_2026-06-27 page:7] "Charges 13 3 10 35 61". The 10-K sized only the Project CORE capacity rationalisation at about 20 over two years [10-K_2025-09-27 page:15] "these actions are projected to cost approximately $20 million"; the charge line is therefore broader than that programme, and the integration and other component recurs each quarter, with a further 23 in Q3 including a loss on sale of a facility. Risk mechanism: add-backs that recur every quarter blur the line between non-recurring and operating cost; lenders and rating methodologies may haircut them. Credit implication: committee leverage should be shown on both bases (5.28x and 7.86x gross), and a covenant-style EBITDA cannot be inferred because no definition from an executed agreement is supplied.

Interest cover. Evidence: net interest expense was 151 LTM against operating income of 63, so operating income covers interest 0.42 times; adjusted EBITDA covers the cash-interest proxy 2.91 times and net interest 2.46 times. Risk mechanism: floating-rate term loan exposure (the filing says a change of 0.25 percent changes annual interest expense by about 2) [10-Q_2026-06-27 page:19] "A change of 0.25% on these floating interest rate exposures would increase our annual interest expense by approximately $2 million." Credit implication: cover is adequate only on the adjusted measure; lower SOFR (about 3.62 percent at June 27, 2026 against about 4.19 percent at September 27, 2025 per the filings) has helped the floating portion.

Cash flow and liquidity. Evidence: nine-month cash from operations was 76 and capex 44, so free cash flow was 32, up from (45) in 9M FY2025. Quarterly free cash flow was (13) in Q1, 73 in Q2 and (28) in Q3 (calc); working capital changes absorbed 54 in Q3 (calc: (34) cumulative against 20 at six months). Management guides fiscal 2026 free cash flow of 90 to 110, which needs 58 to 78 in the fourth quarter. Risk mechanism: large quarterly swings from working capital and raw-material inflation (raw materials inventory rose from 175 to 201 in the quarter); customer receivable programmes are off balance sheet and unquantified. Credit implication: debt reduction depends on a strong fourth quarter; liquidity is 280 of cash plus a 350 undrawn revolver commitment, but the revolver's availability, borrowing base and any covenant are not supplied and 58 percent of cash is outside the U.S. [10-Q_2026-06-27 page:19] "of which approximately 58% is located outside the U.S."

Maturities and refinancing. Evidence: no maturity before October 2029; 500 falls due then and 1,466 in November 2031; management says it intends to refinance prior to maturity [10-Q_2026-06-27 page:19] "which we intend to refinance prior to maturity". The book value of marketable debt exceeded fair value by 48 at June 27, 2026, against 136 at March 28, 2026, which is a narrower discount in the latest quarter [10-Q_2026-06-27 page:10] "The book value of our marketable long-term indebtedness exceeded fair value by $48 million as of June 27, 2026." Credit implication: runway is long, but two instruments mature within weeks of each other in 2029 (notes in October, revolver in November) and the 2031 stack is large; any springing maturity in the revolver is unknown.

Earnings quality. Evidence: Q3 adjusted EBITDA rose from 91 to 99 on a price-cost spread gain of 11 [10-Q_2026-06-27 page:15] "The operating income increase included a favorable price cost spread of $11 million", while net sales rose from 839 to 857 including favorable currency of 21 and a selling price decrease of 8. Rest of World adjusted EBITDA fell from 30 to 28 while Americas rose from 61 to 71. Risk mechanism: the Q3 gain is concentrated in one region and in price-cost timing during raw-material inflation; management says it is holding to the lower end of its adjusted EBITDA guidance range [EX-99.1_2026-08-06 page:1] "while holding to the lower end of our adjusted EBITDA guidance range". Credit implication: treat the 372 LTM base as not yet showing a clean upward trend, and note that the low end of the 380 to 410 range implies a fourth quarter of 98 against 90 a year earlier (calc).

### Claims outside the debt figure

None of the following is included in gross debt of 1,966 or in the leverage ratios.

| Claim | Amount and period | Locator | Inside the debt figure | Treatment |
| --- | --- | --- | --- | --- |
| Operating lease liabilities (current 18, noncurrent 42) | 60 at June 27, 2026 | [10-Q_2026-06-27 page:8] "Current operating lease liabilities Other current liabilities 18 18" and "Noncurrent operating lease liabilities Operating lease liabilities 42 45" | Outside | Leases are an operating cost in adjusted EBITDA; finance leases were stated as not material at FY2025 |
| Unfunded frozen pension benefit obligation | 27 at September 27, 2025 | [10-K_2025-09-27 page:39] "End of period $ 27" | Outside | Updated figure not supplied in interim reports |
| Fox River environmental liability and escrow | 17 liability and 9 escrow asset at June 27, 2026 | [10-Q_2026-06-27 page:12] "outstanding balance of the environmental liability and corresponding escrow asset were $17 million and $9 million" | Outside | Payable over 29 years |
| Brazilian tax claims | Not expected to exceed 66 at June 27, 2026 (40 to 59 at September 27, 2025) | [10-Q_2026-06-27 page:12] "not expected to exceed $66 million as of June 27, 2026" | Outside | Recorded in other long-term liabilities; payment timing expected beyond one year |
| Cross-currency swap liability | 78 at June 27, 2026 (euro 250 million to November 2027 and euro 425 million to November 2029) | [10-Q_2026-06-27 page:9] "Cross-currency swaps Designated Other long-term liabilities $ 78 $ 99" | Outside | Net investment hedge; settlement terms are not supplied |
| Receivables sold under customer programmes | Not supplied | [10-K_2025-09-27 page:27] "The Company participates in customer supply chain financing programs to collect certain receivables through third-party financial institutions." | Outside | Removed from receivables as true sales; unquantified |
| Purchase commitments | Not supplied | [10-K_2025-09-27 page:35] "The Company has various purchase commitments for raw materials, supplies and property and equipment incidental to the ordinary conduct of business." | Outside | Amount not printed |
| Restructuring accrual | 5 at June 27, 2026 | [10-Q_2026-06-27 page:7] "Balance at June 27, 2026 $ 5 $ — $ — $ — $ 5" | Outside | Cash outflow already largely paid |

### Instruments, liquidity build and covenants

Debt instruments as the notes print them at June 27, 2026 (and September 27, 2025). Issuer, co-issuer, guarantor lists and security grants are not printed in the supplied notes; the labels below are the table labels only.

| Instrument as printed | Maturity | Jun 27, 2026 | Sep 27, 2025 | Rate as printed | Locator |
| --- | --- | --- | --- | --- | --- |
| Term loan | November 2031 | 706 | 731 | Margin 4.25% plus SOFR (SOFR about 3.62% at June 27, 2026) | [10-Q_2026-06-27 page:8] "Term loan November 2031 $ 706 $ 731" and [10-Q_2026-06-27 page:19] "As of Quarter end, the SOFR rate of approximately 3.62% was applicable to the term loan." |
| Revolving credit facility (asset-based) | November 2029 | Nil drawn; commitment 350 | Nil drawn | SOFR margin 1.50% to 2.00% | [10-Q_2026-06-27 page:8] "Revolving credit facility November 2029 — —" and [10-Q_2026-06-27 page:19] "a $350 million revolving credit facility with no borrowings outstanding" |
| 4.75% First Priority Senior Secured Notes | October 2029 | 500 | 500 | 4.75% | [10-Q_2026-06-27 page:8] "4.75% First Priority Senior Secured Notes October 2029 500 500"; these are the retained Glatfelter notes per [10-K_2025-09-27 page:34] |
| 7.25% First Priority Senior Secured Notes | November 2031 | 760 | 800 | 7.25% | [10-Q_2026-06-27 page:8] "7.25% First Priority Senior Secured Notes November 2031 760 800" |
| Debt discounts, deferred fees and other | n/a | (65) | (79) | n/a | [10-Q_2026-06-27 page:8] "Debt discounts, deferred fees and other (65 ) (79 )" |

Liquidity build at June 27, 2026 (calc, USD millions): unrestricted cash is not separately printed, so total cash of 280 is used; undrawn revolver commitment 350; letters of credit drawn against the revolver: Not supplied (searched "letters of credit", "standby", "LC", "borrowing base" across all seven sources; no matching text); total 630 before any letters of credit or borrowing base limit. Facilities expiring within twelve months: none; the earliest facility maturity is November 2029.

Covenants. Maintenance tests on the term loan and notes: none, as stated [10-Q_2026-06-27 page:9] "Despite not having financial maintenance covenants on our term loan and secured notes". Negative covenants limit debt incurrence, acquisitions, combinations, distributions and redemption; thresholds are Not supplied. The revolver's covenants, any springing test and its definition of EBITDA are Not supplied. The issuer states compliance with all long-term debt covenants as of June 27, 2026. Headroom: Not calculable, because no tested ratio or level is printed. The definition of EBITDA computed here (company adjusted EBITDA) may differ from any credit-agreement definition.

### Latest quarter and after

- Q3 FY2026 (quarter ended June 27, 2026): net sales 857, operating income 22, adjusted EBITDA 99, net loss (20) [10-Q_2026-06-27 page:3] "Net sales $ 857 $ 839 $ 2,445 $ 2,365".
- Financing: no new borrowings; cumulative repayments 65 at nine months against 63 at six months, so about 2 in the quarter (calc); Q1 repayments 27 and Q2 36 are confirmed by the releases [EX-99.1_2026-05-07 page:1] "We made $36 million in debt repayments during the quarter".
- Divestiture: a non-cash loss of 7 on the sale of a facility in Rest of World, with proceeds of 7 [10-Q_2026-06-27 page:8] "(a) Includes $7 million non-cash loss on divestiture of facility executed in the quarter in Rest of World."
- Restructuring (Project CORE): charges of 61 in nine months with accrual falling to 5.
- Guidance: fiscal 2026 cash from operations 150 to 170, free cash flow 90 to 110 on capex of about 60 [10-Q_2026-06-27 page:13] "Projected fiscal 2026 free cash flow assumes $60 million of capital spending." This replaces cash from operations of 170 to 190 on capex of 80 in the Q1 materials [EX-99.1_2026-02-05 page:6] "Additions to PPE (net) (80)".
- Controls: disclosure controls not effective at June 27, 2026 (see Gaps).
- Subsequent events and cutoff: no source is dated after August 6, 2026; no subsequent-events note was found; events from August 7, 2026 to the cutoff of 2026-11-05 are unknown, not nil. The fiscal year ending September 26, 2026 is not yet reported in the pack.
- Merger terms: the November 4, 2024 merger created the issuer; the 10-K reports 90 percent of shares to former parent shareholders and 10 percent to Glatfelter shareholders [10-K_2025-09-27 page:5] "pre-Transaction Treasure shareholders received shares of Magnera representing 90% of the combined company". No consent decree is reported in the supplied text; the winter storm disruption in North America in the second quarter is cited in the Q2 release and the Q3 narrative as a volume effect.

### Consistency with the CP-0 handoff

- CP-0 recorded a two million gap between the 63 repayment figure in the MD&A and the 65 in the cash flow statement as unexplained. With the Q2 10-Q cumulative figure of 63 at six months, the two million sits in Q3; the text still does not say what it was, so the item remains labelled derived. Debt tables agree with the 65 (25 on the term loan plus 40 on the 7.25% notes).
- CP-0 noted the 10-K's [10-K_2025-09-27 page:34] "fiscal year 2029 and 2031" wording for maturities without testing it. Here the printed months (October 2029 and November 2031) would fall in the following fiscal years if year-ends stay in late September, so the maturity chart uses calendar years and records the label question under Gaps.
- CP-0 said interim reports print no maturity schedule; confirmed. The chart therefore derives maturities from the debt table's final maturity dates.
- No CP-0 conclusion is reversed.

## Calculations

All amounts USD millions. Inputs are cited above; locators are the table rows named in the Findings extracts.

Expense-block reconciliation to operating income (by-function statement: cost of goods sold, then selling, general and administrative, amortization of intangibles, restructuring and other, then for FY2025 corporate expense allocation):

| Period | Calculation | Result | Printed operating income | Outcome |
| --- | --- | --- | --- | --- |
| Q3 FY2026 | 857 - 745 - 56 - 11 - 23 | 22 | 22 | Reconciles |
| 9M FY2026 | 2,445 - 2,141 - 156 - 34 - 61 | 53 | 53 | Reconciles |
| 9M FY2025 | 2,365 - 2,116 - 144 - 41 - 69 | (5) | (5) | Reconciles |
| FY2025 | 3,204 - 2,867 - 190 - 50 - 89 - 3 (goodwill and other impairment nil) | 5 | 5 | Reconciles |
| Q1 + Q2 + Q3 FY2026 operating income | 14 + 17 + 22 | 53 | 53 | Quarters sum to the nine months |
| Q1 + Q2 + Q3 FY2026 interest expense, net | 40 + 35 + 37 | 112 | 112 | Quarters sum to the nine months |

LTM builds (FY2025 plus current year-to-date less prior-year-to-date):

| Item | Calculation | Result |
| --- | --- | --- |
| LTM net sales at Q3 FY2026 | 3,204 + 2,445 - 2,365 | 3,284 |
| LTM operating income | 5 + 53 - (5 negative: -5) = 5 + 53 + 5 | 63 |
| LTM D&A | 206 + 150 - 169 | 187 |
| LTM adjusted EBITDA at Q3 | 354 + 282 - 264 | 372 |
| LTM adjusted EBITDA at Q2 | 354 + 183 - 173 | 364 |
| LTM adjusted EBITDA at Q1 | 354 + 93 - 84 | 363 |
| LTM interest expense, net at Q3 | 141 + 112 - 102 | 151 |
| LTM interest expense, net at Q2 | 141 + 75 - 65 | 151 |
| LTM interest expense, net at Q1 | 141 + 40 - 26 | 155 |
| LTM non-cash interest at Q3 / Q2 / Q1 | 17 + 18 - 12; 17 + 13 - 8; 17 + 7 - 3 | 23; 22; 21 |
| LTM cash interest proxy at Q3 / Q2 / Q1 | 151 - 23; 151 - 22; 155 - 21 | 128; 129; 134 |
| FY2025 cash interest proxy | 141 - 17 | 124, equal to reported net cash interest of 124 |
| LTM pre-tax loss | -166 + -64 - (-133) | (97) |
| LTM net loss | -159 + -72 - (-119) | (112) |
| LTM cash from operations | 103 + 76 - 7 | 172 |
| LTM capex | 67 + 44 - 52 | 59 |
| LTM free cash flow | 172 - 59 | 113 |
| LTM add-backs | 372 - (63 + 187) | 122 |
| Add-backs as share of adjusted EBITDA | 122 / 372 | 32.8 percent |

Debt and leverage:

| Date | Gross principal | Cash | Net debt | LTM adjusted EBITDA | Gross / EBITDA | Net / EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| Sep 27, 2025 | 731 + 500 + 800 = 2,031 | 305 | 1,726 | 354 | 2,031 / 354 = 5.74 | 1,726 / 354 = 4.88 |
| Dec 27, 2025 | 706 + 500 + 798 = 2,004 | 264 | 1,740 | 363 | 5.52 | 4.79 |
| Mar 28, 2026 | 706 + 500 + 763 = 1,969 | 303 | 1,666 | 364 | 5.41 | 4.58 |
| Jun 27, 2026 | 706 + 500 + 760 = 1,966 | 280 | 1,686 | 372 | 5.28 | 4.53 |

Sensitivities (labelled, not chart values): Jun 27, 2026 gross debt over operating income plus D&A of 250 is 1,966 / 250 = 7.86 and net 1,686 / 250 = 6.74; FY2025 gross 2,031 / 211 = 9.62; carrying basis gross 1,901 / 372 = 5.11 and net 1,621 / 372 = 4.36; the release's pro forma adjusted EBITDA of 405 (management, includes synergies of 35 and a divestiture adjustment) would give 1,966 / 405 = 4.85, and is not used.

Attribution of the leverage move at Q3 FY2026 from FY2025: debt change only, 1,966 / 354 = 5.55; EBITDA change only, 2,031 / 372 = 5.46; the combined move is 5.74 to 5.28. The earnings change contributes somewhat more than repayment (0.28 against 0.19 turn, the remainder an interaction); the prose states this qualitatively rather than as a precise split.

Cover: FY2025 354 / 124 = 2.85; Q1 363 / 134 = 2.71; Q2 364 / 129 = 2.82; Q3 372 / 128 = 2.91; Q3 over interest expense, net 372 / 151 = 2.46; operating income over interest 63 / 151 = 0.42; adjusted EBITDA less capex over interest (372 - 59) / 151 = 2.07.

Quarterly cash flow by difference: Q2 operating cash flow 89 - 2 = 87 and Q3 76 - 89 = (13); capex Q2 29 - 15 = 14 and Q3 44 - 29 = 15; free cash flow Q1 2 - 15 = (13), Q2 87 - 14 = 73 (equal to the release's 73), Q3 (13) - 15 = (28); nine months 76 - 44 = 32; Q3 working capital change (34) - 20 = (54). Q2 and Q3 interest and non-cash interest by difference: interest 75 - 40 = 35 and 112 - 75 = 37; non-cash 13 - 7 = 6 and 18 - 13 = 5.

Guidance arithmetic: free cash flow needed in Q4 = 90 - 32 = 58 to 110 - 32 = 78; adjusted EBITDA needed in Q4 at the low end of the 380 to 410 range = 380 - 282 = 98, against Q4 FY2025 of 354 - 264 = 90.

Inventory totals at interim dates: Dec 301 + 175 = 476; Mar 297 + 175 = 472; Jun 297 + 201 = 498.

Cash plus revolver commitment: 305 + 350 = 655; 264 + 350 = 614; 303 + 350 = 653; 280 + 350 = 630.

Maturity bucket: CY2031 = 706 + 760 = 1,466; CY2029 = 500; other years nil.

Release comparison (not used in ratios): the release LTM adjusted EBITDA of 372 equals the filing build; the release LTM D&A of 186 against 187 here, Argentina 8 against 6 and other non-cash 33 against 34 differ and offset (63 + 186 + 82 + 8 + 33 = 372; 63 + 187 + 82 + 6 + 34 = 372).

## Gaps

| Gap | Search or reason | Effect | Remediation |
| --- | --- | --- | --- |
| Interim cash interest paid and cash taxes paid: Not supplied | Searched "cash interest", "interest paid", "income taxes paid", "cash paid for"; only the FY2025 net cash interest is printed | Interim cover uses a proxy; cash tax drag on free cash flow cannot be measured | Obtain supplemental cash flow disclosure; keep the proxy labelled |
| Revolver borrowing base, letters of credit, availability and covenants: Not supplied | Searched "letters of credit", "standby", "LC", "borrowing base", "availability", "springing" | Undrawn facilities shown at the 350 commitment; true availability unconfirmed; covenant headroom Not calculable | Retrieve the asset-based revolving credit agreement and amendment |
| Debt maturity schedule at interim dates: Not supplied | Interim notes print final maturities only; the annual schedule is as of September 27, 2025 | Zeros for CY2026 to CY2028 rest on the annual statement | Confirm no amortization against the term loan agreement |
| Fiscal-year labels for maturities look inconsistent with the printed months if fiscal years end in late September | [10-K_2025-09-27 page:34] "are due in fiscal year 2029 and 2031, respectively" against October 2029 and November 2031 in the table; the fiscal year-end pattern is from September 27, 2025 and [10-Q_2026-06-27 page:6] "fiscal year ending September 26, 2026" | Maturity years in this module are calendar years | Confirm in the indentures and credit agreement |
| Customer receivable programme balances: Not supplied | Searched "supply chain financ", "factoring" | Cash from operations and working capital not adjusted | Obtain programme volumes from issuer |
| Unrestricted versus restricted cash: Not supplied | Cash printed in one line; 58 percent of cash is outside the U.S. at June 27, 2026 | Net debt nets all cash | Obtain cash by jurisdiction and any trapped-cash disclosure |
| Pension obligation update after September 27, 2025: Not supplied | Searched "pension", "retiree" in all sources; pension appears only in the 10-K | Pension obligation is a September 27, 2025 figure | Obtain FY2026 annual report when filed |
| Pre-merger comparatives are carve-out and part-period | [10-K_2025-09-27 page:26] and the Glatfelter inclusion from November 4, 2024 | FY2025 and 9M FY2025 trends are not like for like; LTM at Q1 and Q2 contains part-period effects only through the FY2025 base | Use comparable-basis release tables only as attributed management measures |
| Internal control: material weaknesses at September 27, 2025 and ineffective disclosure controls at June 27, 2026 | [10-Q_2026-06-27 page:20] | Interim figures carry control risk; no restatement is reported | Standing limitation; check the FY2026 annual report |
| Add-backs of 122 LTM rest on management's classification | Segment note reconciliation only; no add-back detail beyond category totals | Adjusted ratios could be lower on a lender definition | Obtain the credit-agreement EBITDA definition |
| No source after August 6, 2026 | Cutoff 2026-11-05 | Events to the cutoff, including any refinancing, are unknown | Retrieve later filings or releases |

## Next module

Pass to CP-1A, then CP-2 and CP-5, with these carry-forward instructions:

- Use the chart and metrics tables of this handoff for leverage, cover, liquidity and maturities; quote leverage on both the adjusted (5.28x gross, 4.53x net) and the unadjusted basis (7.86x gross) and never present a release pro forma or synergy-adjusted figure as a filed figure.
- Label interim cover as a proxy; label liquidity as cash plus the undrawn revolver commitment before any borrowing base or letters of credit.
- Keep the claims outside debt (leases, pension, environmental, Brazilian tax claims, cross-currency swap liability, receivable programmes) out of leverage and list them separately.
- State that maturities are by calendar year of the printed month and that the annual report's fiscal-year wording is inconsistent.
- Carry the standing limitations: prior-year carve-out comparatives, control weaknesses, no executed debt documents, nothing dated after August 6, 2026.
- CP-5 should recompute the LTM builds, the reconciliations and the ratios from the cited rows, and test the extract tables against the cited locators.
