## Request

Module CP-1, financial base, for Weatherford International plc (issuer id wfrd). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot, public case. Reporting currency: USD, amounts in US$ millions unless a row says otherwise (per-share amounts in dollars, share counts in millions). Current period per context: q3-2026 (three months ended 2026-09-30, with nine months ended 2026-09-30); prior period: fy-2025 (year ended 2025-12-31). Consumers named by the run: CP-1A, CP-2 and CP-5, and the report sections for key findings, financials and credit metrics, model chart strip, strengths and weaknesses, company profile and transaction summary.

Scope: extract and label the reported financial statements, debt, liquidity, covenant text and cash flow of the consolidated group; separate reported facts from calculations; review definitions; and judge what the evidence supports for each consumer. Every figure comes from the pinned sources below. No outside knowledge of the company is used and nothing dated after the cutoff is used as fact. Amounts that look forward (the October 2026 redemption, the pending redomestication, the dividend payable December 2026) are labelled as announced or pending events.

## Sources

Issuer sources relied on (file name and sha256 as supplied by CP-OS):

| Source file | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_wfrd-20251231.htm.jsonl | dac00725a2c3d644200d2314099fff47d7f3eb762778ea3920935ae50ab28ce2 | FY2025 statements, debt and lease notes, maturity table, pension, cash interest |
| 10-Q_2026-03-31_wfrd-20260331.htm.jsonl | 9947bc5d7e7ed46ec27eb5be20182fefc783d1bcf9e98ead61e47e75e87e1802 | Q1 2026 balance sheet items, letters of credit, cash interest |
| 10-Q_2026-06-30_wfrd-20260630.htm.jsonl | 0659d6081747e0dbacebc77689bd519f07b2164e0adebad5354150ed075c3f19 | Q2 2026 letters of credit, six-month cash interest |
| 10-Q_2026-09-30_wfrd-20260930.htm.jsonl | 678145577a1f518a8936739eae48408772c69c0e9c66ea7073ec677a8f4ec5f5 | Q3 2026 and nine-month 2026 statements, debt note, liquidity text, subsequent events |
| EX-99.1_2026-04-21_a2026-q1ex991earningsrelea.htm.jsonl | 16b049423c2a0b3987004d0686dae44f41d8fe13554c66ab3742b5ef18204c19 | Company non-GAAP adjusted EBITDA, total debt, net debt at 2025-12-31 and 2026-03-31 |
| EX-99.1_2026-07-21_a2026-q2ex991earningsrelea.htm.jsonl | c318686e28c9fd3731b6593cf62a7f0973fd91c30668b11db34c9715af2ad0be | Same for 2026-06-30 |
| EX-99.1_2026-10-20_a2026-q3ex991earningsrelea.htm.jsonl | f95c1562ed4f41199ffe8f8d250788ec78ae6a54ea4c8df350ecd996b8e7fb5e | Same for 2026-09-30, adjusted EBITDA reconciliation, redemption notice |

Run settings (not issuer evidence): context sha256 01c56abd12b41461776f319879358e62715a2713d739e5e9f5f0984372acf97e. Blank context fields (market inputs, peers, ratings, deal terms) are not read as zero.

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 32ac84c9fe8120dabd000a3e4123c1abf4dbaa26e615a38753d7eb75f51a79f8 | Source readiness: READY_WITH_LIMITATIONS; limits on legal documents, covenant compliance, quarterly notes and table splits carried into this module |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| On the company's own adjusted EBITDA, leverage is low and has eased through 2026, and cash plus undrawn bank commitments exceed total debt. Covenant headroom cannot be sourced. | Medium | Adjusted EBITDA is a company-defined measure, and no covenant ratio or compliance figure is reported. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt was 1.48x trailing adjusted EBITDA at the Q3 2026 balance sheet date, and net debt was 0.28x. | Gross and net leverage are modest and net leverage fell each quarter of 2026. | Medium |
| Cash of 1,161 and undrawn commitments of 766 were reported or derived at Q3 2026. | Liquidity is large against near-term debt, though part of the cash cannot be moved freely. | Medium |
| Trailing adjusted EBITDA to cash interest was 9.02x at Q3 2026. | Interest burden is light, but the figure rests on company-defined EBITDA and lumpy coupon timing. | Medium |
| Operating cash flow rose in the nine months to Q3 2026 mainly through receivable collections while cash earnings before working capital fell. | The improvement is partly a working capital release and may not repeat. | Medium |
| The 2030 notes are shown as current debt and an October 2026 redemption from cash was announced. | Gross debt should fall by the carrying amount once completed, but completion is not evidenced. | Medium |

### Financial base view

The financial base is sound enough to support the downstream credit work, with a Medium confidence and named restrictions. On the filed balance sheet at 2026-09-30, total debt (current plus long-term, including finance leases, carrying value) was 1,480 against cash and cash equivalents of 1,161 and restricted cash of 37, giving net debt of 282. The company's trailing-twelve-month adjusted EBITDA was 1,001, so total debt was 1.48x and net debt 0.28x on that definition. The debt stack is two senior note series (the 8.625% notes due 2030 and the 6.75% notes due 2033) plus finance leases, with a 1,000 secured revolving and letter of credit facility that has zero borrowings. Near-term maturities are small until the 2030 notes, which the company has called for redemption from cash on 2026-10-30; completion is announced, not evidenced. The base also carries four restrictions. First, adjusted EBITDA adds back share-based compensation, restructuring, redomestication and other charges; on an unadjusted basis (operating income plus depreciation and amortization) the trailing figure is 867 and total debt is 1.71x, so the definition matters. Second, the credit agreement states a minimum interest coverage, a maximum total net leverage and a maximum secured net leverage, but the sources report no covenant ratio and do not define the covenant terms, so covenant headroom is Not supplied. Third, operating cash flow in the nine months to 2026-09-30 rose against the year-ago period only because of a working capital release; before working capital items it fell. Fourth, letters of credit, surety bonds, operating leases and a small supplier financing programme sit outside the debt total and are shown separately below. Revenue and segment profit are down year on year in 2026 on the effect of the Iran Conflict in the Middle East, North Africa and Asia region, while cost reductions held margins.

### Source context and extraction

| Source | Entity and perimeter | Period and statement kind | Units and currency | Version relationship |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Weatherford International plc and subsidiaries, consolidated (page:68 "WEATHERFORD INTERNATIONAL PLC AND SUBSIDIARIES") | Year ended 2025-12-31 with 2024 and 2023 comparatives; audited statements and notes | Dollars in millions, USD | Controls FY2025 and the 2025-12-31 balance sheet |
| 10-Q Q1 2026 | Same consolidated group | Three months ended 2026-03-31; unaudited; balance sheet at 2026-03-31 and 2025-12-31 | Dollars in millions, USD | Separate active source; controls Q1 2026 |
| 10-Q Q2 2026 | Same | Three and six months ended 2026-06-30; unaudited | Dollars in millions, USD | Separate active source |
| 10-Q Q3 2026 | Same | Three and nine months ended 2026-09-30; unaudited; balance sheet at 2026-09-30 and 2025-12-31 | Dollars in millions, USD | Latest filed; controls Q3 2026 and nine months 2026 |
| Releases Q1, Q2, Q3 2026 | Same consolidated group | Quarter, with trailing twelve months for non-GAAP leverage | "$ in Millions", USD | Management presentation; supports and never overrides the filings |

All amounts bind to one entity perimeter (the consolidated group of Weatherford International plc), one currency (USD) and one unit (millions); the pack contains no figures in another currency or scale. Balance sheet amounts are instants at the stated date; income and cash flow amounts are flows over the stated duration. Statements are on the basis of U.S. GAAP (Q3 10-Q page:4). Extraction is text only (see CP-0): several tables are split across page chunks (the 10-K balance sheet over page:68 and page:69, the Q3 10-Q segment tables over page:6 and page:7, the release leverage table over page:15 and page:16), and each split was stitched by reading both chunks.

### Reported statements: income statement

All amounts US$ millions; sign as printed (costs positive in the cost lines, charges negative in the other-expense block).

| Line | FY2025 | Nine months 2025 | Nine months 2026 | Q3 2025 | Q3 2026 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Total revenue | 4,918 | 3,629 | 3,400 | 1,232 | 1,143 | 10-K page:68; Q3 10-Q page:2 |
| Operating income | 756 | 557 | 383 | 178 | 153 | same |
| Interest expense, net of interest income | (91) | (70) | (48) | (23) | (15) | same |
| Interest income (memo, as printed in the caption) | 46 | 36 | 34 | 11 | 13 | same |
| Income before income taxes | 554 | 426 | 309 | 139 | 129 | same |
| Income tax provision | (97) | (108) | (33) | (52) | (4) | same |
| Net income | 457 | 318 | 276 | 87 | 125 | same |
| Net income attributable to Weatherford | 431 | 293 | 267 | 81 | 120 | same |
| Depreciation and amortization | 267 | 193 | 211 | 67 | 70 | 10-K page:70; Q3 10-Q page:3 and release page:12 |
| Company adjusted EBITDA (non-GAAP) | 1,067 (trailing twelve months at 2025-12-31) | 776 | 710 | 269 | 254 | Q1 release page:15; Q3 release page:15 |

Definition notes. The FY2025 adjusted EBITDA is the company's trailing twelve month figure at 2025-12-31, taken from the Q1 2026 release; the 10-K does not print adjusted EBITDA for the consolidated group (it prints segment adjusted EBITDA only, page:45). The nine-month 2025 operating income includes a 70 gain on sale of the Argentine pressure pumping business (Q3 10-Q page:2), which the company's adjusted EBITDA excludes (page:15 of the Q3 release shows "(70)").

### Reported statements: cash flow

| Line | FY2025 | Nine months 2025 | Nine months 2026 | Q3 2025 | Q3 2026 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 676 | 408 | 503 | 138 | 192 | 10-K page:70; Q3 10-Q page:3; Q3 release page:13 |
| Capital expenditures | (226) | (175) | (141) | (44) | (45) | same |
| Proceeds from disposition of assets | 16 | 11 | 17 | 5 | 8 | same |
| Interest paid (supplemental) | 125 | 71 | 57 | Not supplied: quarterly cash interest is not printed for Q3 alone | Not supplied | 10-K page:70; Q3 10-Q page:4 |
| Income taxes paid, net of refunds | 157 | 122 | 127 | Not supplied | Not supplied | same |
| Changes in receivables, inventory, payables, accrued salaries and taxes payable (working capital items) | Not supplied: the 10-K prints a different caption without taxes payable | (116) | 65 | (69) | 27 | Q3 release page:13 |
| Dividends paid | (72) | (54) | (59) | (18) | (19) | 10-K page:70; Q3 10-Q page:4; Q3 release page:13 |
| Share repurchases | (101) | (94) | (54) | (7) | (28) | same |
| Repayments of long-term debt | (1,388) | (80) | (25) | (7) | (8) | same |
| Borrowings of long-term debt | 1,200 | Not supplied: no borrowing line printed | Not supplied | Not supplied | Not supplied | 10-K page:70 |

The Q3 2026 and Q3 2025 columns are three-month figures from the Q3 release page:13 where the 10-Q prints cumulative figures only. The working-capital line is the release's caption. The FY2025 interest paid of 125 and taxes paid of 157 are printed in the 10-K supplemental cash flow information.

### Reported statements: balance sheet and debt

| Line | 2025-12-31 | 2026-03-31 | 2026-06-30 | 2026-09-30 | Locators |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 987 | 1,012 | 1,100 | 1,161 | 10-K page:68; Q1 release page:15; Q2 release page:15; Q3 10-Q page:3 |
| Restricted cash | 55 | 38 | 37 | 37 | same |
| Current portion of long-term debt | 30 | 31 | 30 | 264 | 10-K page:69; Q1 10-Q page:3; Q2 10-Q page:3; Q3 10-Q page:3 |
| Long-term debt | 1,455 | 1,453 | 1,450 | 1,216 | same |
| Total debt (current plus long-term, as printed in releases) | 1,485 | 1,484 | 1,480 | 1,480 | Q1 release page:15; Q2 release page:15; Q3 release page:15 |
| Net debt (company-defined: total debt less cash and restricted cash) | 443 | 434 | 343 | 282 | same, page:16 for Q3 |
| Total assets | 5,197 | 5,085 | 5,102 | 5,336 | 10-K page:69; Q1 10-Q page:3; Q2 10-Q page:3; Q3 10-Q page:3 |
| Total shareholders' equity | 1,696 | 1,759 | 1,789 | 1,992 | same |
| Operating lease liabilities (current plus non-current) | 157 | 146 | 142 | 148 | 10-K page:69 and page:83; Q1 10-Q page:3; Q2 10-Q page:3; Q3 10-Q page:3 |

Total debt composition at 2026-09-30 (Q3 10-Q page:9 and page:10, carrying values): 6.75% senior notes due 2033, 1,183; 8.625% senior notes due 2030, 234 (shown as current); finance leases, 63 (30 current plus 33 non-current). These sum to 1,480, which equals the release total. At 2025-12-31 (10-K page:83): 2033 notes 1,181; 2030 notes 234; finance leases 70 (30 plus 40); total 1,485.

### Debt, security and obligors

| Instrument | Issuer and co-obligors (as printed) | Amount | Rate and maturity | Security and guarantees | Locator |
| --- | --- | --- | --- | --- | --- |
| 8.625% senior notes due 2030 | Weatherford International Ltd. ("Weatherford Bermuda") issuer; Weatherford US Holding, LLC ("Weatherford Delaware", formerly Weatherford International, LLC) co-issuer and co-obligor | Remaining principal 236, carrying 234 at 2026-09-30 | 8.625%, interest 1 June and 1 December, matures 2030-04-30; redemption notice 2026-10-20 for 236, expected 2026-10-30 at 100% plus accrued interest | Guaranteed by the plc and other subsidiary guarantors (not named); security not stated | Q3 10-Q page:10 and page:16; Q3 release page:5 |
| 6.75% senior notes due 2033 | Weatherford Bermuda issuer; Weatherford Delaware and, from 2026-09-25, Weatherford International Holding LLC (Texas) co-issuers and co-obligors | Remaining principal 1.2 billion (as printed), carrying 1,183 at 2026-09-30 | 6.75%, interest 15 April and 15 October from 2026-04-15, matures 2033-10-15 | Guaranteed by the plc and other subsidiary guarantors (not named); security not stated | Q3 10-Q page:10 |
| Finance leases | Not stated | 63 at 2026-09-30 | Not supplied: rate and maturity by lease not printed in the quarterly report | Lease assets | Q3 10-Q page:9 |
| Credit Agreement (revolving and letter of credit facility) | Borrowers: Weatherford Bermuda, Weatherford Delaware, Weatherford Canada Ltd., WOFS International Finance GmbH; the plc as parent | Commitment 1 billion (as printed); borrowings zero | Matures on the earlier of 2030-09-18 and, if more than 200 of the 2030 notes remain outstanding, 91 days before their maturity; the 10-K gives that earlier date as 2030-01-29, and it applies while 236 of the notes remain, so completing the redemption would remove the trigger | Guaranteed by the plc and certain subsidiaries; secured by substantially all personal property of the plc and those subsidiaries | Q3 10-Q page:11 |

Note on the facility size. The 10-K states that the September 2025 amendment raised the commitment from 720 to 1 billion "comprised of $600 million to be used either for revolving loans or financial letters of credit and $400 million to be used for performance letters of credit", with an accordion to 1.15 billion (10-K page:55 and page:85). The 10-Qs state only the 1 billion total. The split is therefore sourced from the 10-K and is not restated in 2026.

Debt maturities by year at 2025-12-31 (10-K page:86), US$ millions: 2026, 29; 2027, 20; 2028, 9; 2029, 4; 2030, 238; thereafter, 1,206; total scheduled maturities 1,506, less unamortized issuance cost and discount (21), giving carrying value 1,485. The schedule includes finance lease payments. It is not updated in the 2026 quarterly reports.

### Claims outside the debt total

| Item | Amount | Inside or outside total debt | Locator |
| --- | --- | --- | --- |
| Financial letters of credit under the Credit Agreement | 1 at 2026-09-30 (7 at 2025-12-31) | Outside debt; reduces facility availability | Q3 10-Q page:11 |
| Performance letters of credit under the Credit Agreement | 233 at 2026-09-30 (245 at 2025-12-31) | Outside debt; reduces facility availability | Q3 10-Q page:11 |
| Letters of credit under uncommitted bilateral facilities | 297 at 2026-09-30, of which 31 cash collateral held in restricted cash (207, of which 47, at 2025-12-31) | Outside debt; separate lines | Q3 10-Q page:11 |
| Surety bonds | 534 at 2026-09-30 (629 at 2025-12-31) | Outside debt; may be called on breach of contractual or performance obligations | Q3 10-Q page:34 |
| Operating lease liabilities | 148 at 2026-09-30 (157 at 2025-12-31) | Outside the debt figure (finance leases are inside it) | Q3 10-Q page:3; 10-K page:83 |
| Pension and retiree plans | Net underfunded obligation of 21 at 2025-12-31 (41 underfunded less 20 funded); not updated in 2026 | Outside debt | 10-K page:88 |
| Supplier finance programme | About 19 outstanding at 2026-09-30, included in accounts payable | Outside debt | Q3 10-Q page:15 |
| Accounts receivable factoring | Receivables sold 16 in the nine months to 2026-09-30 (234 in the nine months to 2025-09-30) | Off balance sheet; proceeds in operating cash flow | Q3 10-Q page:32 |
| Foreign currency forwards and credit default swap | Forward notional 608 and swap notional 14 at 2025-12-31; swap expected to reach nil by 2026-12-31; not updated in the Q3 10-Q | Outside debt | 10-K page:54 and page:87 |
| Non-current taxes payable | 218 at 2026-09-30 | Balance sheet liability, outside debt | Q3 10-Q page:3 |
| Litigation | Not quantified: the note says an adverse outcome "could be material" | Outside debt | Q3 10-Q page:12 |

### Liquidity and covenants

Liquidity inputs (US$ millions, each with its locator): unrestricted cash 1,161 (Q3 10-Q page:3); Credit Agreement commitment 1,000, borrowings zero, financial letters of credit 1 and performance letters of credit 233 (Q3 10-Q page:11). The facility is a secured bank line that expires 2030-09-18 or earlier as described above; no facility expires within twelve months of 2026-09-30 on the sources. Uncommitted bilateral letter of credit lines are not counted as liquidity. The calculation is in the Calculations section.

Covenants stated in the Credit Agreement (Q3 10-Q page:11 and page:33; same text in the 10-K page:55 and page:86): a minimum liquidity covenant of 250 (which may increase up to 400 depending on transactions), a minimum interest coverage ratio of 2.50 to 1.00, a maximum total net leverage ratio of 3.50 to 1.00 and a maximum secured net leverage ratio of 1.50 to 1.00. No step-downs are stated. The sources report no covenant ratio, no compliance statement and no covenant definitions; a search of every source found only risk-factor language and the "Defaults Upon Senior Securities. None." item. Covenant headroom is therefore Not supplied. The company's reported net leverage of 0.28x (Q3 release page:16) uses a different definition from a net leverage covenant (the covenant definition is unseen), so it is shown as context and not as headroom. The senior note indentures carry negative covenants on debt, dividends, investments, liens and mergers (10-K page:86), with no levels given.

### Strengths and weaknesses (financial)

Strengths on the evidence: low leverage on the company's adjusted EBITDA; net leverage reported lower in each quarter of 2026 than at 2025-12-31; large cash balance against modest near-term debt; nine-month adjusted free cash flow of 379 against 244 a year earlier (Q3 release page:15); a refinancing in the fourth quarter of 2025 that replaced most of the 8.625% notes with the 6.75% notes, with interest expense falling from 106 to 82 in the nine months (Q3 10-Q page:22).

Weaknesses on the evidence: revenue down 6% and operating income down 31% in the nine months to 2026-09-30 against the year-ago period (Q3 10-Q page:20), on Iran Conflict disruption in Middle East, North Africa and Asia (revenue down 191 in that region in the nine months); segment adjusted EBITDA down in WCC; a concentrated Mexican receivable (19% of net receivables, with the largest customer 14%) with a history of late payment (Q3 10-Q page:32); cash that cannot be moved freely (164 at 2026-09-30, Q3 10-Q page:31); and 128 of cash in Russia operations (page:19).

### Narrative review by dimension

Each item reads evidence, then risk mechanic, then credit implication. Figures are shown in the tables and calculations above or below.

Leverage. Evidence: total debt of 1,480 and company adjusted EBITDA for the trailing twelve months of 1,001 at 2026-09-30, against 1,485 and 1,067 at 2025-12-31. Risk mechanic: debt barely changed over nine months while trailing EBITDA fell, so gross leverage rose slightly even as net leverage fell on cash build. The decline in net leverage comes from cash, not from debt reduction, and cash includes trapped balances. Credit implication: leverage is moderate on any measure in the sources; it is sensitive to the EBITDA definition (1.48x on adjusted EBITDA, 1.71x on operating income plus depreciation and amortization), and the announced redemption would reduce gross debt without changing net debt materially because it uses cash.

Coverage. Evidence: trailing cash interest paid of 111 at Q3 2026 against 125 for FY2025. Risk mechanic: cash interest paid is lumpy because the coupons are semiannual and the 2033 notes paid their first coupon on 2026-04-15; the trailing figure still contains payments on the larger 2030 notes before their 2025 partial redemption. Credit implication: coverage of cash interest is strong on adjusted EBITDA, and the run-rate burden should be lower after the redemption (the company expects annualized cash interest to fall by about 20, Q3 release page:5), but the ratio is not a covenant test.

Cash flow quality. Evidence: operating cash flow of 503 against 408 in the nine months, but working capital items contributed 65 against (116). Risk mechanic: receivable collections released cash (186 against 22 a year earlier), which does not recur once balances normalise; the 10-Q attributes the increase to "increased cash from accounts receivable, partially offset by lower cash earnings and higher cash usage related to income taxes payable" (Q3 10-Q page:29). The Q3 tax provision of 4 includes a 56 valuation allowance release (Q3 10-Q page:14), so Q3 net income is not a clean earnings run-rate. Credit implication: free cash flow conversion is real but partly timing; adjusted free cash flow of 379 should be read with the working capital contribution.

Liquidity. Evidence: cash of 1,161 and a revolving and letter of credit facility with zero borrowings. Risk mechanic: availability is reduced by letters of credit; the 10-K split means only the revolving portion can fund cash needs, while other letters of credit and surety bonds could be called. Credit implication: liquidity covers the 2030 notes call and the near term, and the minimum liquidity covenant is far below cash, but definitions are unseen.

Data quality. Evidence: sources are filed statements plus attributed releases; extraction is text only. Risk mechanic: split tables and the absence of a printed full-year adjusted EBITDA in the 10-K mean the FY2025 adjusted EBITDA relies on a release. Credit implication: Medium confidence overall.

Definition risks. Adjusted EBITDA, net debt and net leverage are company-defined non-GAAP measures (Q3 release pages:14-15). Total debt includes finance leases and excludes operating leases, letters of credit, surety bonds, factoring and supplier finance. Covenant ratios are defined in the credit agreement, which is not supplied.

Key gaps. See the Gaps section.

### Subsequent events and pending items

- Redemption of the 2030 notes: notice issued 2026-10-20 for the remaining principal of about 236, expected 2026-10-30, funded with cash on hand (Q3 10-Q page:16). Announced, expected before the cutoff, completion not evidenced.
- Dividend: 0.275 per share declared 2026-10-15, payable 2026-12-03 to holders of record on 2026-11-06 (Q3 10-Q page:15). Record date is after the cutoff; labelled as a future term.
- Redomestication from Ireland to a Delaware corporation: approved by shareholders on 2026-09-03; subject to Irish High Court sanction and other steps; expected in the fourth quarter of 2026 (Q3 10-Q page:16). The company expects 20 to 30 of annual cash savings from 2027 (Q3 release page:6). The plan to move to Texas did not pass in June 2026 (Q2 release page:5). Intellectual property transition steps are being evaluated for accounting and tax implications.
- NCS Multistage Holdings, Inc. acquired 2026-09-01 for total consideration of 128 (13 cash net of cash acquired, 1.0 million shares valued at 101, and 7 of assumed equity awards), with tangible assets acquired 150 and liabilities acquired 34 (Q3 10-Q page:15). The Q3 10-Q does not describe any debt acquired.
- Supplemental indenture of 2026-09-25 adding Weatherford International Holding LLC as co-issuer of the 2033 notes (Q3 10-Q page:10 and page:39).

### Consumer readiness

| Consumer | View | Evidence cited and limits |
| --- | --- | --- |
| CP-1A | Sufficient with limits | Entity, perimeter, debt obligors and transaction facts above come from Q3 10-Q pages:10, 11, 15 and 16; limits are the unseen indentures and merger agreement. |
| CP-2 | Sufficient with limits | Statements, debt by instrument, liquidity and cash flow metrics above; limited by the company-defined EBITDA and no covenant headroom. |
| CP-5 | Sufficient with limits | Every figure is tied to a page locator in this handoff; split-table stitching and the release-sourced FY2025 adjusted EBITDA are the points to test. |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 1.39 | 0.42 | x | At 2025-12-31. Total debt of 1,485 (carrying, including finance leases) over company adjusted EBITDA of 1,067 for the trailing twelve months; net ratio matches the company's reported 0.42x. EBITDA is a company-defined non-GAAP measure. Analyst-calculated. |
| Q1 2026 | 1.42 | 0.41 | x | At 2026-03-31. Total debt of 1,484 over trailing adjusted EBITDA of 1,047; net ratio matches the reported 0.41x. Same definition limits. |
| Q2 2026 | 1.46 | 0.34 | x | At 2026-06-30. Total debt of 1,480 over trailing adjusted EBITDA of 1,016; net ratio matches the reported 0.34x. Same definition limits. |
| Q3 2026 | 1.48 | 0.28 | x | At 2026-09-30. Total debt of 1,480 over trailing adjusted EBITDA of 1,001; net ratio matches the reported 0.28x. The 2030 notes redemption announced after quarter end is not reflected. Same definition limits. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 8.54 | x | Company adjusted EBITDA of 1,067 over interest paid of 125 for the year (10-K page:70). Analyst-calculated; cash interest is timing-dependent and includes interest on the larger 2030 notes before the 2025 refinancing. |
| Q1 2026 | 8.44 | x | Trailing twelve months at 2026-03-31: adjusted EBITDA 1,047 over interest paid of 124 (125 less 2 plus 1). Analyst-calculated; the first 2033 notes coupon fell after quarter end. |
| Q2 2026 | 9.24 | x | Trailing twelve months at 2026-06-30: adjusted EBITDA 1,016 over interest paid of 110 (125 less 70 plus 55). Analyst-calculated. |
| Q3 2026 | 9.02 | x | Trailing twelve months at 2026-09-30: adjusted EBITDA 1,001 over interest paid of 111 (125 less 71 plus 57). Analyst-calculated; not the covenant interest coverage ratio, whose definition is unseen. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 987 | 748 | US$m | At 2025-12-31. Unrestricted cash; commitment 1000 less zero borrowings, financial letters of credit 7 and performance letters of credit 245. Of the undrawn amount, only the revolving portion (up to 600 less financial letters of credit) can fund cash needs per the 10-K. |
| Q1 2026 | 1012 | 736 | US$m | At 2026-03-31. Commitment 1000 less zero borrowings, 7 financial and 257 performance letters of credit. Same limit on the cash-drawable portion. |
| Q2 2026 | 1100 | 753 | US$m | At 2026-06-30. Commitment 1000 less zero borrowings, 4 financial and 243 performance letters of credit. Same limit. |
| Q3 2026 | 1161 | 766 | US$m | At 2026-09-30. Commitment 1000 less zero borrowings, 1 financial and 233 performance letters of credit; about 164 of the cash cannot be immediately repatriated. Same limit; uncommitted bilateral lines excluded. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 29 | US$m | Scheduled maturities at 2025-12-31 (10-K page:86), finance lease payments included. Not updated in 2026 reports. The announced redemption of the 2030 notes (about 236) would fall in 2026 if completed; it is not reflected. |
| 2027 | 20 | US$m | Same schedule; finance lease payments. |
| 2028 | 9 | US$m | Same schedule; finance lease payments. |
| 2029 | 4 | US$m | Same schedule; finance lease payments. |
| 2030 | 238 | US$m | Same schedule; includes the 8.625% notes due 2030-04-30 (principal 236) plus finance lease payments; the revolver is separate and undrawn. |
| 2031 and later | 1206 | US$m | Same schedule ("Thereafter"); includes the 6.75% notes due 2033-10-15 (1.2 billion as printed) plus finance lease payments. |

### Financials and credit metrics

| Metric | Period or date | Value | Unit | Basis and locator |
| --- | --- | --- | --- | --- |
| Revenue | FY2025 | 4918 | US$m | Reported; 10-K page:68 |
| Revenue | Nine months 2026 | 3400 | US$m | Reported; Q3 10-Q page:2 (nine months 2025: 3629) |
| Revenue | Trailing twelve months at Q3 2026 | 4689 | US$m | Calculated: 4918 less 3629 plus 3400 |
| Operating income | Nine months 2026 | 383 | US$m | Reported; Q3 10-Q page:2 (nine months 2025: 557, including a 70 gain) |
| Company adjusted EBITDA | Trailing twelve months at Q3 2026 | 1001 | US$m | Company non-GAAP; Q3 release page:16 |
| Adjusted EBITDA margin | Q3 2026 | 22.2 | percent | Company non-GAAP; Q3 release page:15 |
| EBITDA before add-backs (operating income plus D&A) | Trailing twelve months at Q3 2026 | 867 | US$m | Calculated; see Calculations |
| Total debt | 2026-09-30 | 1480 | US$m | Reported in release (page:15), equals balance sheet lines (Q3 10-Q page:3) |
| Cash and cash equivalents | 2026-09-30 | 1161 | US$m | Reported; Q3 10-Q page:3 |
| Net debt | 2026-09-30 | 282 | US$m | Company-defined; Q3 release page:16 |
| Total debt / adjusted EBITDA | 2026-09-30 | 1.48 | x | Calculated |
| Net debt / adjusted EBITDA | 2026-09-30 | 0.28 | x | Calculated; equals the company-reported 0.28x |
| Total debt / EBITDA before add-backs | 2026-09-30 | 1.71 | x | Calculated |
| Adjusted EBITDA / cash interest paid | Trailing twelve months at Q3 2026 | 9.02 | x | Calculated |
| Net cash provided by operating activities | Nine months 2026 | 503 | US$m | Reported; Q3 10-Q page:3 (nine months 2025: 408) |
| Capital expenditures | Nine months 2026 | 141 | US$m | Reported; Q3 10-Q page:3 (nine months 2025: 175) |
| Company adjusted free cash flow | Nine months 2026 | 379 | US$m | Company non-GAAP; Q3 release page:15 (nine months 2025: 244) |
| Operating cash flow before working capital items | Nine months 2026 | 438 | US$m | Calculated; nine months 2025: 524 |
| Shareholder return (dividends plus repurchases) | Nine months 2026 | 113 | US$m | Company-stated; Q3 release page:5 |
| Liquidity: cash plus undrawn committed facilities | 2026-09-30 | 1927 | US$m | Calculated: 1161 plus 766 |
| Letters of credit under the Credit Agreement | 2026-09-30 | 234 | US$m | Calculated: 1 plus 233 |
| Covenant headroom (any test) | 2026-09-30 | Not supplied | Not applicable | No reported covenant ratio or definitions |

## Calculations

All inputs are reported figures from the cited pages, in US$ millions. Results are shown as calculated and rounded as stated. No result replaces a source-printed value.

1. Total debt. Current portion of long-term debt plus long-term debt. 2026-09-30: 264 plus 1,216 = 1,480 (Q3 10-Q page:3), equal to the release total debt (Q3 release page:15). 2025-12-31: 30 plus 1,455 = 1,485.
2. Debt composition check at 2026-09-30: 1,183 plus 234 plus 63 = 1,480 (Q3 10-Q page:9), where finance leases are 30 plus 33.
3. Net debt. Total debt less cash and cash equivalents less restricted cash. 2026-09-30: 1,480 less 1,161 less 37 = 282, equal to the company figure (Q3 release page:16).
4. Trailing twelve months adjusted EBITDA at 2026-09-30. FY2025 trailing figure 1,067 (Q1 release page:15) less nine months 2025 776 plus nine months 2026 710 = 1,001, equal to the company figure (Q3 release page:16). The Q3 reconciliation also ties: 153 plus 70 plus 4 plus 6 plus 6 plus 15 = 254 (operating income, depreciation and amortization, other charges, restructuring, redomestication, share-based compensation).
5. Leverage ratios. Total debt over trailing adjusted EBITDA: 1,485 / 1,067 = 1.39x (2025-12-31); 1,484 / 1,047 = 1.42x (2026-03-31); 1,480 / 1,016 = 1.46x (2026-06-30); 1,480 / 1,001 = 1.48x (2026-09-30). Net debt over the same: 443 / 1,067 = 0.42x; 434 / 1,047 = 0.41x; 343 / 1,016 = 0.34x; 282 / 1,001 = 0.28x. The net ratios equal the company-reported ratios in the releases (Q1 release page:15, Q2 release page:15, Q3 release page:16).
6. EBITDA before add-backs, trailing twelve months at 2026-09-30. Operating income plus depreciation and amortization: FY2025 756 plus 267 = 1,023; nine months 2025 557 plus 193 = 750; nine months 2026 383 plus 211 = 594. Trailing = 1,023 less 750 plus 594 = 867. The 70 gain on sale is in both the FY2025 and nine-month 2025 figures and cancels. Bridge to adjusted EBITDA: 1,001 less 867 = 134, equal to trailing share-based compensation 50 (38 less 26 plus 38) plus restructuring 35 (58 less 51 plus 28) plus redomestication 30 (none before 2026) plus other charges net 19 (18 less 19 plus 20) = 134. Total debt / 867 = 1.71x; net debt / 867 = 0.33x.
7. Trailing cash interest paid. FY2025 125 (10-K page:70). Q1 2026: 125 less 2 (Q1 2025) plus 1 (Q1 2026) = 124 (Q1 10-Q page:3). Q2 2026: 125 less 70 plus 55 = 110 (Q2 10-Q page:4). Q3 2026: 125 less 71 plus 57 = 111 (Q3 10-Q page:4). Interest cover = trailing adjusted EBITDA over trailing interest paid: 1,067 / 125 = 8.54x; 1,047 / 124 = 8.44x; 1,016 / 110 = 9.24x; 1,001 / 111 = 9.02x.
8. Undrawn committed facilities. Commitment 1,000 less borrowings 0 less financial letters of credit less performance letters of credit. 2025-12-31: 1,000 less 7 less 245 = 748. 2026-03-31: 1,000 less 7 less 257 = 736. 2026-06-30: 1,000 less 4 less 243 = 753. 2026-09-30: 1,000 less 1 less 233 = 766. Revolving portion available for cash borrowing, from the 10-K split, at 2026-09-30: 600 less 1 financial letter of credit = 599 (split not restated in the 10-Qs; assumes it is unchanged). Liquidity at 2026-09-30: 1,161 plus 766 = 1,927 (or 1,161 plus 599 = 1,760 on the cash-drawable basis). Cash net of the 164 stated as not immediately repatriable: 1,161 less 164 = 997; whether the Russian cash of 128 overlaps with the 164 is not stated.
9. Trailing flows at 2026-09-30. Revenue: 4,918 less 3,629 plus 3,400 = 4,689. Operating cash flow: 676 less 408 plus 503 = 771. Capital expenditures: 226 less 175 plus 141 = 192. Proceeds from disposition of assets: 16 less 11 plus 17 = 22. Company-definition adjusted free cash flow: 771 less 192 plus 22 = 601.
10. Cash flow before working capital items, nine months. 2026: 503 less 65 = 438. 2025: 408 less (116) = 524. Change 438 less 524 = (86), about 16 percent lower. The 65 and (116) are the release's working capital caption (Q3 release page:13); the components in the 10-Q (186, (19), (72), (7), (23)) sum to 65.
11. Illustrative pro forma for the announced redemption, not an evidenced result. Remove the 2030 notes carrying value of 234 from total debt (1,480 less 234 = 1,246) and 236 from cash and restricted cash (1,198 less 236 = 962) at 2026-09-30. Net debt 1,246 less 962 = 284 (the 2 difference is unamortized issuance cost and ignores accrued interest). Total debt / 1,001 = 1.24x. Completion of the redemption is not evidenced in the sources.
12. Shareholder distributions, nine months 2026: dividends 59 plus repurchases 54 = 113, equal to the release figure (Q3 release page:5). Adjusted free cash flow 379 less 113 = 266 before debt repayment of 25 and other financing items.

## Gaps

| Gap | Effect | Handling |
| --- | --- | --- |
| Covenant ratios and compliance for the minimum liquidity, interest coverage, total net leverage and secured net leverage tests are Not supplied; covenant definitions are not in the sources | Headroom is Not calculable | Levels stated; headroom left as Not supplied |
| Executed Credit Agreement, indentures and the 2026-09-25 supplemental indenture are not supplied; guarantor list and note security are not named | Obligor and structural analysis limited to filed summaries | Carry the limitation to CP-1A, CP-2 and CP-5 |
| Completion of the 2030 notes redemption is not evidenced; no source after 2026-10-21 | Gross debt at the redemption date not confirmed | Shown as announced; pro forma labelled illustrative |
| FY2025 consolidated adjusted EBITDA is taken from a release trailing figure, not the 10-K | Single-source management figure for the base year | Labelled company non-GAAP; the segment totals in the 10-K are consistent in direction |
| Undrawn facility is derived from the commitment and letters of credit; the 600 and 400 split is from the 10-K only | Cash-drawable availability uncertain | Both bases shown in Calculations |
| Quarterly cash interest for Q3 alone and discrete quarter tax paid are not printed | Quarterly cover is trailing only | Trailing basis used |
| Debt maturity schedule and lease detail not updated after 2025-12-31; pension and derivative notes not updated | Stale as to 2026 | Labelled at 2025-12-31 |
| Finance lease terms (rate, maturity) not supplied | Small portion of debt | Shown at carrying value |
| Quantification of litigation exposure not supplied | Contingent claims outside debt unquantified | Described only |
| No ratings reports; ratings are company-reported (Ba2 positive; BB positive from S&P and Fitch per Q3 10-Q page:31) | Attribution to company | Attribute |

## Next module

Proceed to CP-1A with this handoff: entity and obligor roles, debt stack, the pending redomestication, the NCS Multistage acquisition and the October 2026 redemption are the transaction facts to carry, each with the locators above. CP-2 should use the leverage, interest cover, liquidity and cash flow quality conclusions with their definition limits, and show covenant headroom as Not supplied. CP-5 should test the stitched tables, the trailing-period arithmetic and the release-sourced FY2025 adjusted EBITDA. If the executed credit agreement or any filing after 2026-10-21 and before the cutoff becomes available, add it as a separate source and revisit covenant headroom and the redemption status.
