# CP-1 — Financial base: CCO HOLDINGS LLC (cco-holdings-llc)

## Request

- Issuer: CCO HOLDINGS LLC (issuer id `cco-holdings-llc`), co-registrant with CCO Holdings Capital Corp., as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; every amount is US$ millions as the filings print them (`dollars in millions`) unless a row says otherwise. Context current period q2-2026; prior period fy-2025.
- Run: `cco-holdings-llc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Perimeter: CCO Holdings, LLC and its consolidated subsidiaries, as in the issuer's own 10-K and 10-Qs. This includes the Charter Operating group (the secured debt and the operating subsidiaries) and the consolidated equipment installment plan vehicle CCO EIP Financing, LLC. The parent's earnings releases are a different, larger perimeter (Charter Communications, Inc.) and are not used for any figure below.
- Question: what is the reported financial base for the credit view, with all debt, claims outside debt, liquidity, maturities, coverage, covenants and the latest-quarter events, for FY2024, FY2025 and the first half of 2026?
- Periods: FY2024, FY2025, Q1 2026, Q2 2026 (three months ended June 30, 2026), 6M 2026 and 6M 2025 (six months), and LTM. LTM Q2 2026 = FY2025 + 6M 2026 - 6M 2025; LTM Q1 2026 = FY2025 + Q1 2026 - Q1 2025; LTM Q3 2025 = FY2024 + 9M 2025 - 9M 2024. Balance-sheet dates are December 31, 2024, September 30, 2025, December 31, 2025, March 31, 2026 and June 30, 2026. Locators are `page:N` chunks of the pinned `.jsonl` text, not printed page numbers.

## Sources

| Source | sha256 | Use |
| --- | --- | --- |
| 10-K_2025-12-31_ccoh-20251231.htm.jsonl | 98fc08971e7b602f253b4465dc2493c7d1fd2140d7f51b96e967ed5fb3218118 | Audited FY2025, FY2024 and FY2023 statements, debt table and Note 9, covenants, leases, commitments, Adjusted EBITDA reconciliation |
| 10-Q_2025-09-30_ccoh-20250930.htm.jsonl | bf1745dd3dbecf91195f9fef9fea0cafc9d8a639b8157c8bb3d02dd7240529a1 | Unaudited September 30, 2025 balance sheet, 9M 2025 and 9M 2024 flows (LTM Q3 2025 inputs), availability |
| 10-Q_2026-03-31_ccoh-20260331.htm.jsonl | 213317fa77d5c45445d49d044bc961ab9dfa41083289474b65a9c5985c9bbe1b | Unaudited Q1 2026 statements, debt note, February 2026 redemptions, availability |
| 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | 9af8d8232114d58e6ac96035eb67adc4aa9622876079128a14eacfcc389f347e | Unaudited Q2 2026 and 6M statements, debt note, repurchases, availability, guarantor structure, Cox and Liberty Broadband text |
| EX-99.1_2026-01-30_chtrex991earningsrelease12.htm.jsonl | cb5b5ac26ab78f0a85b295e8b2969a94081a4aecc513efb234aeefb51019e762 | Parent-level release; read only to confirm the January 2026 issuance (not used for figures) |
| EX-99.1_2026-04-24_chtrex991earningsrelease33.htm.jsonl | 483c56fedf60126a16d804e1d36760024be2164b76b1c1509864a6a063bd22be | Parent-level release; not used for figures |
| EX-99.1_2026-07-24_chtrex991earningsrelease63.htm.jsonl | 07d1723b22b814c108cba78554e38a4e4a76d8f38c9cdfecbd3804011635822c | Parent-level release; read only for the repurchase cash cost and parent cash (labelled parent) |
| context | 1a68c05f8e4415af1307ec03597fe0b094afc35e94c83b63b62cbe99d897f95e | Run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 4b95775bd75ac91b4fbe8df3dddfba01cd62f5117bd68b1e969812d6f8d7022a | Source readiness: all four consumers ready with limitations; carries the missing executed documents, the lack of any filing after July 24, 2026, the parent perimeter of the releases and the Cox figure differences |

Consistency with CP-0: this answer confirms CP-0 on every point it checked and corrects none. CP-0 said the June 2026 10-Q carries no series list, maturity schedule, letters of credit figure or covenant ratio; confirmed. CP-0 said no discrete Q3 or Q4 2025 statements exist; that stands. This answer derives only the Q4 2025 Adjusted EBITDA (5,665) and cash interest (1,367) by difference, and labels them calculated.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt is 4.22x last-twelve-months Adjusted EBITDA at June 30, 2026 (4.17x at December 31, 2024), with cash interest cover of 4.43x. Free cash flow and revolver availability fell in 2026; distributions to parent exceeded free cash flow. | Medium | Adjusted EBITDA is a company non-GAAP measure; current series-level debt, covenant ratios and events after July 24, 2026 are not in the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Free cash flow was 2,492 in 6M 2026 against 3,249 in 6M 2025, because Adjusted EBITDA fell and capital spending rose. | Less internal cash to fund debt reduction; leverage depends on EBITDA holding up. | High |
| Distributions to parent were 2,460 in 6M 2026, close to free cash flow of 2,492, and 5,898 over the last twelve months against free cash flow of 5,070. | Cash is upstreamed to the parent, so debt paydown depends on parent choices, limited only by indenture tests. | Medium |
| Revolver availability was 3,700 at June 30, 2026 against 4,600 at March 31, 2026, while credit facility debt rose to 12,453 from 11,665. | The liquidity cushion is thinner, and a revolver tranche of about 960 matures August 31, 2027. | Medium |
| Secured debt of 67,111 ranks ahead of 26,734 of unsecured notes at the issuer, which are structurally subordinated; secured debt is 3.02x EBITDA. | Unsecured holders sit behind roughly three turns of secured leverage; expected Cox debt may join the secured group. | High |
| Debt maturing is 7,279 in 2029 and 13,868 in 2030 on the year-end schedule, after only 1,055 in 2026 and 3,555 in 2027. | Refinancing risk concentrates in 2029 and 2030; all 750 of the 2026 notes and 2,250 of the 2027 notes were redeemed in February 2026. | Medium |

### Financial base view

The issuer's own statements support a debt-only view of leverage at 4.22x total debt and 4.20x net debt to last-twelve-months Adjusted EBITDA of 22,251 at June 30, 2026, edging up from 4.17x and 4.16x at December 31, 2024. Cash interest cover is 4.43x on 5,024 of cash interest paid. These ratios use principal debt and company Adjusted EBITDA before the management fees that the covenants add back, so they are not covenant ratios; the filings print covenant figures only at December 31, 2025 (indenture leverage 4.0 against a 6.0 maximum, and 2.8 against 5.0 and 4.0 at Charter Operating). Operating performance is slipping slowly: Q2 2026 revenue was 13,526 against 13,766 and Adjusted EBITDA 5,428 against 5,668, with the video allocation and Cox transition costs of 65 in the quarter among the drivers the 10-Q gives. Capital spending of 5,713 in 6M 2026 against 5,273 pushed free cash flow down to 2,492 from 3,249, and distributions to parent of 2,460 took almost all of it. Three financing claims sit outside the debt figure and add to leverage if counted: the equipment installment plan facility (1,596), short-term borrowings under the deferred payment program (1,155) and operating leases (1,276 at December 31, 2025); counting the first two lifts leverage to 4.34x. The liability structure matters more than the headline ratio: 67,111 of secured debt, guaranteed by the issuer, ranks ahead of 26,734 of issuer-level unsecured notes, and the pending Cox Transactions are expected to add Cox notes to the guaranteed and secured group. Nothing after July 24, 2026 is supplied.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 4.17 | 4.16 | x | Principal debt 93,779 and net debt 93,525 (cash 254) at December 31, 2024 over FY2024 Adjusted EBITDA 22,476. Excludes the equipment installment plan facility (1,072) and short-term borrowings (758). Company non-GAAP EBITDA, before management-fee add-back; not a covenant ratio. |
| LTM Q3 2025 | 4.19 | 4.18 | x | Principal debt 95,023 and net debt 94,788 (cash 235) at September 30, 2025 over LTM Adjusted EBITDA 22,686 (calculated: 22,476 + 16,946 - 16,736). Same exclusions as FY2024. |
| FY2025 | 4.18 | 4.17 | x | Principal debt 94,617 and net debt 94,399 (cash 218) at December 31, 2025 over FY2025 Adjusted EBITDA 22,611. Excludes the equipment installment plan facility (1,447) and short-term borrowings (918). Not a covenant ratio; the filing prints indenture leverage of 4.0. |
| LTM Q1 2026 | 4.19 | 4.18 | x | Principal debt 94,302 and net debt 94,056 (cash 246) at March 31, 2026 over LTM Adjusted EBITDA 22,491 (calculated: 22,611 + 5,618 - 5,738). Same exclusions. |
| LTM Q2 2026 | 4.22 | 4.20 | x | Principal debt 93,845 and net debt 93,560 (cash 285) at June 30, 2026 over LTM Adjusted EBITDA 22,251 (calculated: 22,611 + 11,046 - 11,406). Including the equipment installment plan facility (1,596) and short-term borrowings (1,155) the ratio is 4.34x. Net debt deducts unrestricted cash only (restricted cash 90). |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 4.24 | x | FY2024 Adjusted EBITDA 22,476 over cash paid for interest 5,305 (10-K cash flow statement). Cash interest includes all consolidated borrowings; split by instrument not printed. |
| LTM Q3 2025 | 4.44 | x | LTM Adjusted EBITDA 22,686 over LTM cash interest 5,105 (calculated: 5,305 + 3,590 - 3,790). |
| FY2025 | 4.56 | x | FY2025 Adjusted EBITDA 22,611 over cash paid for interest 4,957. Net interest expense was 5,004. |
| LTM Q1 2026 | 4.48 | x | LTM Adjusted EBITDA 22,491 over LTM cash interest 5,025 (calculated: 4,957 + 1,060 - 992). |
| LTM Q2 2026 | 4.43 | x | LTM Adjusted EBITDA 22,251 over LTM cash interest 5,024 (calculated: 4,957 + 2,493 - 2,426). Operating lease cash (334 in FY2025) is not in cash interest. Not a covenant ratio. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 254 | Not supplied: availability under the Charter Operating credit facilities at December 31, 2024 is not printed in the pinned sources | US$m | Unrestricted cash and cash equivalents; restricted cash of 47 excluded. |
| Q3 2025 | 235 | 4000 | US$m | Cash at September 30, 2025 (restricted cash 57 excluded). Availability "approximately $4.0 billion" under the Charter Operating credit facilities, rounded to 0.1 billion as printed (10-Q Sep 2025 page:28). |
| FY2025 | 218 | 4400 | US$m | Cash at December 31, 2025 (restricted cash 121 excluded). Availability "approximately $4.4 billion" (10-K page:92, page:104). Letters of credit: 364 issued, of which 26 collateralised by revolver borrowings (10-K page:157, page:182); a rebuild from facility sizes gives 4,427 net of that 26, consistent with the printed figure. |
| Q1 2026 | 246 | 4600 | US$m | Cash at March 31, 2026 (restricted cash 105, calculated from 351 total). Availability "approximately $4.6 billion" (10-Q Mar 2026 page:11, page:24). |
| Q2 2026 | 285 | 3700 | US$m | Cash at June 30, 2026 (restricted cash 90 excluded). Availability "approximately $3.7 billion" (10-Q Jun 2026 page:11, page:27). Facility split and letters of credit at this date not printed. The equipment installment plan facility (capacity 2.0 billion, carrying 1,596) is not counted. A revolver tranche of about 960 matures August 31, 2027, within twelve months of the as-of date. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 1055 | US$m | Principal as of December 31, 2025 (10-K page:160): 750 of 5.500% notes due May 1, 2026 plus 305 of term loan amortisation. The 750 was redeemed in February 2026, so the remaining 2026 figure is about 305 before the unallocated repurchases (calculated, see roll-forward). |
| 2027 | 3555 | US$m | 3,250 of 5.125% notes due May 1, 2027 plus 305 amortisation (10-K page:160). 2,250 of the notes were redeemed in February 2026, leaving 1,000 (calculated). The Revolving Loan B of about 960 matures August 31, 2027; the tie-out implies it was undrawn at year-end. |
| 2028 | 5392 | US$m | Notes of 4,750 (5.000% CCO Holdings due February 1, 3.750% and 4.200% Charter Operating) plus Term A-6 final maturity August 31, 2028 and amortisation (derived by difference). |
| 2029 | 7279 | US$m | Notes of 7,000 (two CCO Holdings series and three Charter Operating series) plus amortisation of about 280. |
| 2030 | 13868 | US$m | CCO Holdings notes of 5,800 (4.750% and 4.500%) plus Term A-7, B-3 and B-4 finals and the Revolving Loan C drawn at 2.1 billion maturing March 15, 2030 (derived by difference). |
| Thereafter | 63468 | US$m | 2031 onward, including Term B-5 due December 15, 2031 and notes to 2063. Total of all periods 94,617 at December 31, 2025. The 3,000 of January 2026 issuance (due 2033 and 2036) and the 1,249 of repurchases (series not disclosed) are not allocated to years in this table; see the roll-forward. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2024 | FY2025 | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 | LTM Q2 2026 | Basis and locators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenues | 55,085 | 54,774 | 13,766 | 13,526 | 27,501 | 27,123 | 54,396 | Reported (10-K page:141; 10-Q Jun 2026 page:5). LTM calculated. |
| Operating costs and expenses (excl. D&A and other operating) | 33,260 | 32,836 | 8,255 | 8,236 | 16,474 | 16,418 | 32,780 | Reported; includes stock compensation, Cox transition expenses (Q2 2026 65; 6M 2026 89) and management fees. LTM calculated. |
| Adjusted EBITDA (company non-GAAP) | 22,476 | 22,611 | 5,668 | 5,428 | 11,406 | 11,046 | 22,251 | Reported reconciliation (10-K page:91; 10-Q Jun 2026 page:26). LTM calculated. |
| Adjusted EBITDA margin (%) | 40.80 | 41.28 | 41.17 | 40.13 | 41.47 | 40.73 | 40.91 | Calculated. |
| Depreciation and amortization | 8,643 | 8,681 | 2,169 | 2,189 | 4,342 | 4,393 | 8,732 | Reported. LTM calculated. |
| Other operating expenses, net | 117 | 432 | 86 | 51 | 209 | 66 | 289 | Reported (special charges, merger and acquisition costs, loss on disposals). LTM calculated. |
| Income from operations | 13,065 | 12,825 | 3,256 | 3,050 | 6,476 | 6,246 | 12,595 | Reported; reconciles to the lines above (see Calculations). |
| Interest expense, net | 5,192 | 5,004 | 1,254 | 1,270 | 2,485 | 2,515 | 5,034 | Reported. LTM calculated. |
| Net income attributable to CCO Holdings member | 7,406 | 7,440 | 1,930 | 1,973 | 3,767 | 3,779 | 7,452 | Reported; Q2 2026 includes a 243 gain on debt extinguishment. LTM calculated. |
| Net cash flows from operating activities | 15,882 | 16,865 | 4,184 | 4,016 | 8,475 | 8,367 | 16,757 | Reported (10-K page:141-142; 10-Q Jun 2026 page:6-7, page:26). LTM calculated. |
| Purchases of property, plant and equipment | 11,269 | 11,624 | 2,874 | 2,858 | 5,273 | 5,713 | 12,064 | Reported. LTM calculated. |
| Change in accrued expenses related to capital expenditures | 1,096 | 586 | 320 | (85) | 47 | (162) | 377 | Reported; sign as in the company's free cash flow reconciliation. LTM calculated. |
| Free cash flow (company definition) | 5,709 | 5,827 | 1,630 | 1,073 | 3,249 | 2,492 | 5,070 | Reported reconciliation; LTM calculated. |
| Cash paid for interest | 5,305 | 4,957 | 1,434 | 1,433 | 2,426 | 2,493 | 5,024 | Supplemental cash flow line; Q2 columns derived from 6M less Q1. LTM calculated. |
| Distributions to parent | 3,051 | 6,794 | 2,474 | 1,363 | 3,356 | 2,460 | 5,898 | Cash flow statements; Q2 columns from the equity statements (10-Q Jun 2026 page:6). LTM calculated. |
| Cash and cash equivalents (unrestricted) | 254 | 218 | Not supplied: June 30, 2025 balance sheet not in the pack | 285 | Not supplied: June 30, 2025 balance sheet not in the pack | 285 | 285 | Balance sheets (10-K page:140; 10-Q Jun 2026 page:5); instants. |
| Total debt, principal | 93,779 | 94,617 | Not supplied: June 30, 2025 balance sheet not in the pack | 93,845 | Not supplied: June 30, 2025 balance sheet not in the pack | 93,845 | 93,845 | Debt notes (10-K page:154; 10-Q Jun 2026 page:10). Carrying value: 93,933; 94,756; 93,959. |
| Equipment installment plan financing facility (outside the debt figure) | 1,072 | 1,447 | Not supplied: June 30, 2025 balance sheet not in the pack | 1,596 | Not supplied: June 30, 2025 balance sheet not in the pack | 1,596 | 1,596 | Separate balance sheet line (10-K page:141; 10-Q Jun 2026 page:5). |
| Net debt (principal less unrestricted cash) | 93,525 | 94,399 | Not supplied: June 30, 2025 balance sheet not in the pack | 93,560 | Not supplied: June 30, 2025 balance sheet not in the pack | 93,560 | 93,560 | Calculated. |
| Total debt / Adjusted EBITDA (x) | 4.17 | 4.18 | n/a (ratio) | n/a (ratio) | n/a (ratio) | n/a (ratio) | 4.22 | Calculated on LTM EBITDA at each date. |
| Net debt / Adjusted EBITDA (x) | 4.16 | 4.17 | n/a (ratio) | n/a (ratio) | n/a (ratio) | n/a (ratio) | 4.20 | Calculated. |
| Secured debt / Adjusted EBITDA (x) | 2.96 | 2.98 | n/a (ratio) | n/a (ratio) | n/a (ratio) | n/a (ratio) | 3.02 | Calculated: senior secured notes and debentures plus credit facilities (the guaranteed and secured group). |
| (Debt + equipment installment plan facility + short-term borrowings) / Adjusted EBITDA (x) | 4.25 | 4.29 | n/a (ratio) | n/a (ratio) | n/a (ratio) | n/a (ratio) | 4.34 | Calculated; short-term borrowings 758; 918; 1,155 (deferred payment program). |
| Adjusted EBITDA / cash interest (x) | 4.24 | 4.56 | n/a (ratio) | n/a (ratio) | n/a (ratio) | n/a (ratio) | 4.43 | Calculated. |
| Free cash flow / principal debt (%) | 6.09 | 6.16 | n/a (ratio) | n/a (ratio) | n/a (ratio) | n/a (ratio) | 5.40 | Calculated; FY2024 5,709 / 93,779. |

### Revenue by product line

| Product line (US$m) | FY2024 | FY2025 | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| Internet | 23,360 | 23,765 | 5,969 | 5,776 | 11,899 | 11,628 |
| Mobile service | 3,083 | 3,762 | 921 | 1,095 | 1,835 | 2,147 |
| Video | 15,129 | 13,703 | 3,488 | 3,149 | 7,068 | 6,401 |
| Voice | 1,437 | 1,350 | 346 | 331 | 702 | 669 |
| Residential revenue | 43,009 | 42,580 | 10,724 | 10,351 | 21,504 | 20,845 |
| Commercial revenue (small business and mid-market and large) | 7,254 | 7,315 | 1,836 | 1,865 | 3,658 | 3,704 |
| Advertising sales | 1,780 | 1,468 | 371 | 416 | 711 | 774 |
| Other | 3,042 | 3,411 | 835 | 894 | 1,628 | 1,800 |
| Total revenues | 55,085 | 54,774 | 13,766 | 13,526 | 27,501 | 27,123 |

The company has one reportable segment and manages on a consolidated basis (10-Q Jun 2026 page:14). Locators: 10-K page:162; 10-Q Jun 2026 page:13. Q2 2026 Internet fell 3.2% and video 9.7% while mobile service rose 18.9% (10-Q Jun 2026 page:21).

### Balance sheet and net debt by date

| Line (US$m) | Dec 31, 2024 | Sep 30, 2025 | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 254 | 235 | 218 | 246 | 285 |
| Restricted cash (in prepaid and other current assets) | 47 | 57 | 121 | 105 | 90 |
| Total assets | 148,371 | 150,739 | 151,982 | 152,670 | 153,439 |
| Current portion of long-term debt (carrying) | 1,799 | 750 | 750 | 0 | 999 |
| Long-term debt (carrying) | 92,134 | 94,413 | 94,006 | 94,414 | 92,960 |
| Total debt, principal | 93,779 | 95,023 | 94,617 | 94,302 | 93,845 |
| Equipment installment plan financing facility | 1,072 | 1,365 | 1,447 | 1,596 | 1,596 |
| Short-term borrowings (deferred payment program, in accrued liabilities) | 758 | 537 | 918 | 812 | 1,155 |
| Other long-term liabilities | 3,227 | 3,259 | 3,362 | 3,387 | 3,342 |
| Total member's equity | 39,261 | 39,500 | 40,707 | 41,625 | 42,605 |

Locators: 10-K page:140-141; 10-Q Sep 2025 page:5, page:10; 10-Q Mar 2026 page:5, page:10; 10-Q Jun 2026 page:5, page:9. Restricted cash at March 31, 2026 is calculated (351 total cash, cash equivalents and restricted cash less 246). The March 31, 2026 current portion is shown as a dash in the filing.

### Debt by instrument at December 31, 2025

The 10-K table lists 51 note and debenture series plus the credit facilities, totalling 94,617 of principal (10-K page:102-103). Principal by issuer: CCO Holdings 27,250; Charter Operating notes 44,500; TWC, LLC 9,918; TWCE 1,000; credit facilities 11,949 (calculated sum 94,617, equal to the printed total). Weighted average interest rate on the total was 5.1% (unsecured notes 4.9%, secured notes 5.1%, credit facilities 5.6%) (10-K page:154). Post-year-end changes are in the right-hand column and in the roll-forward below.

| Issuer | Instrument | Principal | Final maturity | Security and guarantors | Change after December 31, 2025 |
| --- | --- | --- | --- | --- | --- |
| CCO Holdings, LLC | 5.500% notes due 2026 | 750 | 5/1/2026 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | Redeemed in full February 2026 (10-Q Mar 2026 page:11) |
| CCO Holdings, LLC | 5.125% notes due 2027 | 3,250 | 5/1/2027 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | 2,250 redeemed February 2026; 1,000 remains (calculated) (10-Q Mar 2026 page:11) |
| CCO Holdings, LLC | 5.000% notes due 2028 | 2,500 | 2/1/2028 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 5.375% notes due 2029 | 1,500 | 6/1/2029 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 6.375% notes due 2029 | 1,500 | 9/1/2029 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 4.750% notes due 2030 | 3,050 | 3/1/2030 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 4.500% notes due 2030 | 2,750 | 8/15/2030 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 4.250% notes due 2031 | 3,000 | 2/1/2031 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 7.375% notes due 2031 | 1,100 | 3/1/2031 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 4.750% notes due 2032 | 1,200 | 2/1/2032 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 4.500% notes due 2032 | 2,900 | 5/1/2032 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 4.500% notes due 2033 | 1,750 | 6/1/2033 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| CCO Holdings, LLC | 4.250% notes due 2034 | 2,000 | 1/15/2034 | Senior unsecured. Co-issuer CCO Holdings Capital Corp. No subsidiary guarantee; structurally subordinated to all subsidiary obligations (10-K page:155; 10-Q Jun 2026 page:33) | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 3.750% notes due 2028 | 1,000 | 2/15/2028 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 4.200% notes due 2028 | 1,250 | 3/15/2028 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 2.250% notes due 2029 | 1,250 | 1/15/2029 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 5.050% notes due 2029 | 1,250 | 3/30/2029 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 6.100% notes due 2029 | 1,500 | 6/1/2029 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 2.800% notes due 2031 | 1,600 | 4/1/2031 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 2.300% notes due 2032 | 1,000 | 2/1/2032 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 4.400% notes due 2033 | 1,000 | 4/1/2033 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 6.650% notes due 2034 | 900 | 2/1/2034 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 6.550% notes due 2034 | 1,500 | 6/1/2034 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 6.384% notes due 2035 | 2,000 | 10/23/2035 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 5.850% notes due 2035 | 1,250 | 12/1/2035 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer Charter Communications Operating Capital Corp. (10-K page:155) | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 5.375% notes due 2038 | 800 | 4/1/2038 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 3.500% notes due 2041 | 1,500 | 6/1/2041 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 3.500% notes due 2042 | 1,350 | 3/1/2042 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 6.484% notes due 2045 | 3,500 | 10/23/2045 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 5.375% notes due 2047 | 2,500 | 5/1/2047 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 5.750% notes due 2048 | 2,450 | 4/1/2048 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 5.125% notes due 2049 | 1,250 | 7/1/2049 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 4.800% notes due 2050 | 2,800 | 3/1/2050 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 3.700% notes due 2051 | 2,050 | 4/1/2051 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 3.900% notes due 2052 | 2,400 | 6/1/2052 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 5.250% notes due 2053 | 1,500 | 4/1/2053 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 6.834% notes due 2055 | 500 | 10/23/2055 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 6.700% notes due 2055 | 750 | 12/1/2055 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer Charter Communications Operating Capital Corp. (10-K page:155) | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 3.850% notes due 2061 | 1,850 | 4/1/2061 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 4.400% notes due 2061 | 1,400 | 12/1/2061 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 3.950% notes due 2062 | 1,400 | 6/30/2062 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating | 5.500% notes due 2063 | 1,000 | 4/1/2063 | Senior secured, first-priority liens; guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries (10-K page:156). Co-issuer not named for this series in the pack | No series-level change disclosed after December 31, 2025 |
| TWC, LLC | 5.750% sterling notes due 2031 | 842 | 6/2/2031 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | Sterling: remeasured to 829 (625 pound sterling) at June 30, 2026 (10-Q Jun 2026 page:11) |
| TWC, LLC | 6.550% debentures due 2037 | 1,500 | 5/1/2037 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | No series-level change disclosed after December 31, 2025 |
| TWC, LLC | 7.300% debentures due 2038 | 1,500 | 7/1/2038 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | No series-level change disclosed after December 31, 2025 |
| TWC, LLC | 6.750% debentures due 2039 | 1,500 | 6/15/2039 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | No series-level change disclosed after December 31, 2025 |
| TWC, LLC | 5.875% debentures due 2040 | 1,200 | 11/15/2040 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | No series-level change disclosed after December 31, 2025 |
| TWC, LLC | 5.500% debentures due 2041 | 1,250 | 9/1/2041 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | No series-level change disclosed after December 31, 2025 |
| TWC, LLC | 5.250% sterling notes due 2042 | 876 | 7/15/2042 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | Sterling: remeasured to 862 (650 pound sterling) at June 30, 2026 (10-Q Jun 2026 page:11) |
| TWC, LLC | 4.500% debentures due 2042 | 1,250 | 9/15/2042 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | No series-level change disclosed after December 31, 2025 |
| TWCE | 8.375% debentures due 2033 | 1,000 | 7/15/2033 | Guaranteed by CCO Holdings, Charter Operating and substantially all Charter Operating subsidiaries other than the issuer; ranks equally with the liens on the collateral (10-K page:158-159); no co-issuer named in the pack | No series-level change disclosed after December 31, 2025 |
| Charter Operating (borrower) | Credit facilities, all tranches | 11,949 | 2027 to 2031 | Guaranteed by CCO Holdings and substantially all Charter Operating subsidiaries; secured by liens on substantially all assets and pledged equity (10-K page:157-158) | Principal 12,453 at June 30, 2026 (10-Q Jun 2026 page:10) |
| CCO Holdings, LLC | 7.000% notes due February 2033 | 1,750 | February 2033 | Senior unsecured; co-issuer CCO Holdings Capital Corp. | Issued January 2026 at par (10-K page:104, page:155) |
| CCO Holdings, LLC | 7.375% notes due February 2036 | 1,250 | February 2036 | Senior unsecured; co-issuer CCO Holdings Capital Corp. | Issued January 2026 at par (10-K page:104, page:155) |

The first 51 rows total 82,668 and the credit facilities add 11,949, matching the 94,617 total at December 31, 2025. The two January 2026 series are subsequent events and are not in that total. Credit facility tranches at December 31, 2025 (10-K page:157; approximate amounts as printed):

| Tranche | Principal or capacity | Maturity | Pricing and amortisation |
| --- | --- | --- | --- |
| Term A-6 | about 413 | August 31, 2028 | SOFR + 1.50%; 25 per loan year |
| Term A-7 | about 4,300 | March 15, 2030 | SOFR + 1.25%; 227 per loan year |
| Term B-3 | about 729 | March 31, 2030 | SOFR + 2.25%; 8 per loan year |
| Term B-4 | about 2,000 | December 7, 2030 | SOFR + 2.00%; 20 per loan year |
| Term B-5 | about 2,500 | December 15, 2031 | SOFR + 2.25%; 25 per loan year |
| Revolving Loan B | up to about 960 (no drawing stated) | August 31, 2027 | SOFR + 1.25%; commitment fee not above 0.20% |
| Revolving Loan C | 2,100 outstanding of up to 5,500 | March 15, 2030 | SOFR + 1.25%; commitment fee not above 0.20% |

### Debt maturity roll-forward since December 31, 2025

| Year | Reported at December 31, 2025 | Less February 2026 redemptions | Plus January 2026 issuance | Adjusted for stated events |
| --- | --- | --- | --- | --- |
| 2026 | 1,055 | 750 | 0 | 305 |
| 2027 | 3,555 | 2,250 | 0 | 1,305 |
| 2028 | 5,392 | 0 | 0 | 5,392 |
| 2029 | 7,279 | 0 | 0 | 7,279 |
| 2030 | 13,868 | 0 | 0 | 13,868 |
| Thereafter | 63,468 | 0 | 3,000 | 66,468 |
| Total | 94,617 | 3,000 | 3,000 | 94,617 |

The adjusted column is calculated and still excludes the 1,249 of open-market repurchases in Q2 2026 (series not disclosed), term loan amortisation paid in 2026 and net credit facility borrowings of 504 between December 31, 2025 and June 30, 2026. By class, unsecured notes fell 516 (27,250 to 26,734) and secured notes fell 733 after removing the 27 favourable sterling remeasurement (55,418 to 54,658) (calculated). The balance-sheet current portion of 999 at June 30, 2026 is consistent with the remaining 1,000 of 5.125% notes due May 1, 2027 (inference; at December 31, 2025 the current portion of 750 equalled only the 2026 notes and excluded term loan amortisation).

### Claims outside the debt figure

| Claim | Amount | Date | Inside or outside the debt figure | Locator and note |
| --- | --- | --- | --- | --- |
| Equipment installment plan financing facility (SPV borrower CCO EIP Financing, LLC) | 1,596 | Jun 30, 2026 | Outside: separate balance sheet line; included in the extended leverage line only | 10-Q Jun 2026 page:5, page:11-12. Capacity 2.0 billion, final maturity November 3, 2029 with a twelve-month revolving period subject to renewal; secured by 2.3 billion of pledged receivables and 90 of restricted cash; not guaranteed by the group |
| Short-term borrowings, deferred payment program | 1,155 | Jun 30, 2026 | Outside: inside accounts payable, accrued and other current liabilities | 10-Q Jun 2026 page:9-10; interest-bearing; cash outflows are financing activities |
| Supply chain finance obligations | 725 | Jun 30, 2026 | Outside: inside accounts payable and accrued capital expenditures | 10-Q Jun 2026 page:10; cash outflows are operating and investing |
| Operating lease liabilities | 1,276 (undiscounted 1,515) | Dec 31, 2025 | Outside | 10-K page:154; 2026 payments 331; cash paid FY2025 334; not repeated in the 10-Qs |
| Cross-currency derivative liability on the sterling notes | 442 | Jun 30, 2026 | Outside: other long-term liabilities | 10-Q Jun 2026 page:13; 406 at December 31, 2025; swaps mature June 2031 and July 2042 (10-K page:162) |
| Contractual obligations (programming, content, device, network) | 17,122; 4,503 due 2026 | Dec 31, 2025 | Outside | 10-K page:182; the table covers the company and its parent companies, so the issuer's share is not separable |
| Letters of credit and surety bonds | 364 letters of credit (26 under the facility); 474 surety bonds | Dec 31, 2025 | Outside; 26 reduces facility availability | 10-K page:157, page:182 |
| Mortgage note on the Stamford headquarters building, guaranteed by the Obligor Group | about 256 | Jun 30, 2026 | Not stated whether in the debt figure | 10-Q Jun 2026 page:34; issued by a single-asset special purpose entity |
| Unfunded unqualified pension plan | 17 | Dec 31, 2025 | Outside | 10-K page:184; the qualified plan was settled in 2025 |
| Accrued interest | 1,279 | Jun 30, 2026 | Outside | 10-Q Jun 2026 page:9 |
| Franchise fees and pole rentals (operating costs) | 526; 273 | FY2025 | Outside | 10-K page:182 |
| Legal proceedings | Not quantified | Dec 31, 2025 | Outside | Intellectual property suits with no estimated range; California waste investigation not expected to be material (10-K page:182-183) |

### Covenants and compliance

| Test | Level | Reported figure | Headroom | Note |
| --- | --- | --- | --- | --- |
| CCO Holdings indentures: maximum total leverage for incurrence, restricted payments and investments | 6.0 to 1.0 maximum | 4.0 at December 31, 2025 (10-K page:156); June 30, 2026: leverage ratio test "met", no figure (10-Q Jun 2026 page:36) | 2.0 turns; EBITDA could fall about one third with debt unchanged (calculated from rounded ratios) | An incurrence-style test that also gates distributions to a parent for parent notes principal, not a maintenance covenant; no step-down printed |
| Charter Operating credit facilities: consolidated leverage | 5.0 to 1.0, tested quarterly | about 2.8 at December 31, 2025 (10-K page:158) | 2.2 turns; EBITDA cushion about 44% (calculated) | Maintenance covenant at Charter Operating, not at CCO Holdings; a failure is an event of default under the facilities and "the debt of CCO Holdings"; cure right exists |
| Charter Operating credit facilities: first lien leverage | 4.0 to 1.0, tested quarterly | 2.8 at December 31, 2025 (10-K page:158) | 1.2 turns; EBITDA cushion 30% (calculated) | Same test dates; no figure printed after December 31, 2025 |
| Charter (parent) leverage target, not a covenant | 4.0 to 4.5 times net debt to Adjusted EBITDA | 4.18 at June 30, 2026; 4.15 at March 31, 2026 and December 31, 2025 (10-Q Jun 2026 page:27; 10-Q Mar 2026 page:25; 10-K page:93) | Not applicable | Parent-level metric quoted in the issuer's filings; long-term target after closing 3.5 times |

Definition differences: the covenants use Adjusted EBITDA excluding management fees paid to other Charter entities, which were about 1.4 billion in FY2025 and 1.5 billion in FY2024 and 702 in 6M 2026 against 732 in 6M 2025 (10-K page:91; 10-Q Jun 2026 page:26). The metrics in this answer do not add the fees back and use principal debt, so they overstate covenant leverage. A proxy at December 31, 2025 gives 2.81x for secured debt over Adjusted EBITDA plus 1,400 (reported 2.8) and 3.94x for total debt on the same basis (reported 4.0); adding the equipment installment plan facility gives 4.00x. The proxy is not the covenant calculation; the fee figure is rounded and the definition is not supplied.

### Events, comparability and subsequent events

- Financing events: January 2026, 1,750 of 7.000% notes due 2033 and 1,250 of 7.375% notes due 2036 issued at par by CCO Holdings and CCO Holdings Capital Corp. (10-K page:104). February 2026, redemption of 750 of 5.500% notes due 2026 and 2,250 of 5.125% notes due 2027, with a loss on extinguishment of about 4 (10-Q Mar 2026 page:11). Q2 2026, open-market repurchases of 1.2 billion principal of various series, with a gain on extinguishment of about 243 recorded in other income (10-Q Jun 2026 page:11); the parent release states the cost was 1.0 billion in cash for notes of both Charter Operating and CCO Holdings (release Jul 2026 page:1, parent perimeter). The equipment installment plan facility was amended in November 2025 to extend maturity and raise capacity to 2.0 billion (10-K page:161).
- Cox Transactions (parent-level, pending): Transaction Agreement of May 16, 2025; Charter pays 3.5 billion and Charter Holdings pays 650 million in cash plus 6.0 billion of convertible preferred units at 6.875%; the combined entity assumes about 12.4 billion of Cox net debt and finance leases (10-Q Jun 2026 page:8-9). The issuer's 10-Q states it is "required to fund approximately $4.2 billion of cash purchase price at the closing" (page:27) and that after closing Cox notes are expected to become guaranteed and secured debt with Cox entities becoming Obligors, and that all or part of the 4.2 billion of new indebtedness may do the same (page:34). The 10-K figures were 12.6 billion of assumed net debt and 4.0 billion of cash consideration (10-K page:64). Transition expenses were 65 in Q2 2026 and 89 in 6M 2026 in operating costs, plus 34 and 37 of transition capital expenditure (10-Q Jun 2026 page:14-15, page:37). Closing status after July 24, 2026 is not supplied.
- Liberty Broadband Combination (parent-level, pending): Merger Agreement of November 12, 2024; in May 2026 Charter advanced a term loan of about 359 to Liberty Broadband (10-Q Jun 2026 page:28, page:30).
- Management guidance changed direction: the 10-K said "we expect to increase the total amount of our indebtedness to maintain leverage within Charter's target leverage range" with a post-closing long-term target of 3.5 to 3.75 times (10-K page:93); the June 2026 10-Q says "We currently expect to decrease the total amount of our indebtedness to achieve Charter's target leverage" with a post-closing target of 3.5 times (10-Q Jun 2026 page:27). Full-year 2026 capital expenditure is expected at about 11.4 billion excluding Cox (10-Q Jun 2026 page:37).
- Comparability: the "seamless entertainment allocation" reduced Q2 2026 video revenue by 184 and 6M video revenue by 355 and lowers programming costs by the same amounts (10-Q Jun 2026 page:22, page:24), so on the 10-Q's description it moves revenue and costs equally and does not change Adjusted EBITDA (inference). Q2 2025 other revenue included a one-time 45 benefit (page:23). 6M 2025 other operating expenses included a 105 loss on disposal of assets (page:15).
- Events after June 30, 2026 up to the cutoff: none stated in the pinned sources; nothing after July 24, 2026 is supplied.

### Interpretation: data to risk to credit implication

- Earnings: Q2 2026 Adjusted EBITDA fell 240 to 5,428, equal to the 240 fall in revenue, because operating costs excluding stock compensation were unchanged at 8,098 in both quarters (calculated: 8,236 - 138 and 8,255 - 157). Costs held flat even with 65 of Cox transition expense, so underlying costs fell. Credit implication: the EBITDA decline is a revenue problem (Internet customers down 172,000 in the quarter, Internet revenue down 3.2%, video down 9.7%) that mobile growth of 18.9% does not yet offset; leverage rises mechanically as LTM EBITDA falls.
- Cash flow quality: free cash flow of 2,492 in 6M 2026 against 3,249 fell by 757, with Adjusted EBITDA down 360 and capital expenditure up 440 (10-Q Jun 2026 page:32). Capital expenditure is 21.06% of revenue in 6M 2026 against 19.17% (calculated). Credit implication: higher spending on network evolution and customer premise equipment, with rural construction at 391 in Q2 2026, is consuming the cash that would otherwise reduce debt.
- Cash leakage: distributions to parent were 2,460 in 6M 2026, 6,794 in FY2025 and 5,898 over the LTM, above free cash flow of 5,827 and 5,070 in FY2025 and the LTM. The indenture test gates distributions that fund parent note principal, with leverage at 4.0 against 6.0. Credit implication: creditors rely on the parent's leverage target, not on a hard cap; any change in parent buyback policy changes the issuer's net debt directly.
- Structure: of 93,845 principal debt, 54,658 of secured notes and 12,453 of credit facilities (67,111, 71.5% of the total, calculated) are guaranteed by the issuer and secured on the operating group, while 26,734 of unsecured notes sit at the issuer with no subsidiary guarantee. Credit implication: issuer unsecured holders are structurally and effectively subordinated; at 3.02x secured leverage the first call on operating cash is the secured group, and Cox notes are expected to join it.
- Liquidity: availability fell to 3,700 from 4,600 in the quarter while credit facility debt rose 788 (calculated: 12,453 - 11,665), in a quarter when distributions of 1,363 exceeded free cash flow of 1,073 and notes were repurchased (the filings do not tie the borrowing to a use); the nearest facility expiry is the Revolving Loan B of about 960 on August 31, 2027, and the equipment installment plan facility's revolving period is subject to renewal (inference: about twelve months from the November 2025 amendment, so around the as-of date). Credit implication: liquidity is adequate against 1,305 of adjusted 2027 maturities but is revolver-dependent; the 2030 year-end figure of 13,868 includes 2,100 drawn on the Revolving Loan C at December 31, 2025.
- Refinancing: early 2026 refinancing replaced 3,000 of 2026 and 2027 maturities with 7.000% and 7.375% notes due 2033 and 2036, coupons above the 5.500% and 5.125% retired. Cash paid for interest rose to 2,493 from 2,426 in 6M 2026, and the 10-Q attributes the rise in net interest expense (2,515 against 2,485) to higher weighted average debt. Credit implication: the run-rate coupon on refinanced maturities is higher, which would pressure cover as the 2029 and 2030 maturities are refinanced.
- Evidence quality: FY2025 statements are audited (KPMG LLP, report dated January 29, 2026, 10-K page:140); quarterly statements are unaudited; Adjusted EBITDA, free cash flow and availability are management presentations; the covenant ratios are printed only at December 31, 2025.

## Calculations

All inputs are US$ millions from the cited pages. Computed with exact arithmetic and rounded to the precision shown.

### LTM Adjusted EBITDA

- LTM Q3 2025: 22,476 + 16,946 - 16,736 = 22,686 (10-K page:91; 10-Q Sep 2025 page:27).
- LTM Q1 2026: 22,611 + 5,618 - 5,738 = 22,491 (10-Q Mar 2026 page:24).
- LTM Q2 2026: 22,611 + 11,046 - 11,406 = 22,251 (10-Q Jun 2026 page:26).
- Discrete quarters tie: Q1 2026 5,618 + Q2 2026 5,428 = 11,046; Q1 2025 5,738 + Q2 2025 5,668 = 11,406. Q4 2025 = 22,611 - 16,946 = 5,665.
- Cross-identity: Adjusted EBITDA = revenues - operating costs and expenses + stock compensation expense: FY2025 54,774 - 32,836 + 673 = 22,611; FY2024 55,085 - 33,260 + 651 = 22,476; 6M 2026 27,123 - 16,418 + 341 = 11,046; 6M 2025 27,501 - 16,474 + 379 = 11,406; Q2 2026 13,526 - 8,236 + 138 = 5,428; Q2 2025 13,766 - 8,255 + 157 = 5,668.

### LTM and discrete flow lines

- Revenues LTM: 54,774 + 27,123 - 27,501 = 54,396. Operating costs LTM: 32,836 + 16,418 - 16,474 = 32,780. D&A LTM: 8,681 + 4,393 - 4,342 = 8,732. Other operating expenses LTM: 432 + 66 - 209 = 289. Income from operations LTM: 12,825 + 6,246 - 6,476 = 12,595. Interest expense, net LTM: 5,004 + 2,515 - 2,485 = 5,034. Net income attributable LTM: 7,440 + 3,779 - 3,767 = 7,452.
- Operating cash flow LTM: 16,865 + 8,367 - 8,475 = 16,757. Purchases of property, plant and equipment LTM: 11,624 + 5,713 - 5,273 = 12,064. Change in accrued capital expenditure LTM: 586 + (-162) - 47 = 377. Free cash flow LTM: 16,757 - 12,064 + 377 = 5,070; cross-check 5,827 + 2,492 - 3,249 = 5,070. FY2025 free cash flow: 16,865 - 11,624 + 586 = 5,827; FY2024: 15,882 - 11,269 + 1,096 = 5,709; 6M 2026: 8,367 - 5,713 - 162 = 2,492; 6M 2025: 8,475 - 5,273 + 47 = 3,249; Q2 2026: 4,016 - 2,858 - 85 = 1,073; Q2 2025: 4,184 - 2,874 + 320 = 1,630.
- Cash paid for interest: Q2 2026 = 2,493 - 1,060 = 1,433; Q2 2025 = 2,426 - 992 = 1,434; Q3 2025 = 3,590 - 2,426 = 1,164; Q4 2025 = 4,957 - 3,590 = 1,367. LTM Q3 2025 = 5,305 + 3,590 - 3,790 = 5,105; LTM Q1 2026 = 4,957 + 1,060 - 992 = 5,025; LTM Q2 2026 = 4,957 + 2,493 - 2,426 = 5,024.
- Distributions to parent LTM: 6,794 + 2,460 - 3,356 = 5,898. Quarterly check: 6M 2026 1,097 + 1,363 = 2,460; 6M 2025 882 + 2,474 = 3,356.
- Adjusted EBITDA margin: FY2024 22,476 / 55,085 = 40.80%; FY2025 22,611 / 54,774 = 41.28%; Q2 2025 5,668 / 13,766 = 41.17%; Q2 2026 5,428 / 13,526 = 40.13%; 6M 2025 11,406 / 27,501 = 41.47%; 6M 2026 11,046 / 27,123 = 40.73%; LTM 22,251 / 54,396 = 40.91%.
- Capital expenditure to revenue: 6M 2026 5,713 / 27,123 = 21.06%; 6M 2025 5,273 / 27,501 = 19.17%.
- Growth check against the 10-Q: Q2 revenue 13,526 / 13,766 - 1 = -1.74% (printed (1.7)%); Q2 Adjusted EBITDA 5,428 / 5,668 - 1 = -4.23% (printed (4.2)%).
- Operating costs excluding stock compensation: Q2 2026 8,236 - 138 = 8,098; Q2 2025 8,255 - 157 = 8,098.

### Leverage, cover and ratios

- Total debt / Adjusted EBITDA: FY2024 93,779 / 22,476 = 4.17x; LTM Q3 2025 95,023 / 22,686 = 4.19x; FY2025 94,617 / 22,611 = 4.18x; LTM Q1 2026 94,302 / 22,491 = 4.19x; LTM Q2 2026 93,845 / 22,251 = 4.22x.
- Net debt: 93,779 - 254 = 93,525; 95,023 - 235 = 94,788; 94,617 - 218 = 94,399; 94,302 - 246 = 94,056; 93,845 - 285 = 93,560. Net debt / Adjusted EBITDA: 93,525 / 22,476 = 4.16x; 94,788 / 22,686 = 4.18x; 94,399 / 22,611 = 4.17x; 94,056 / 22,491 = 4.18x; 93,560 / 22,251 = 4.20x.
- Secured debt (secured notes and credit facilities): Dec 2024 56,195 + 10,334 = 66,529; Sep 2025 55,414 + 12,359 = 67,773; Dec 2025 55,418 + 11,949 = 67,367; Mar 2026 55,387 + 11,665 = 67,052; Jun 2026 54,658 + 12,453 = 67,111. Over Adjusted EBITDA: 66,529 / 22,476 = 2.96x; 67,367 / 22,611 = 2.98x; 67,111 / 22,251 = 3.02x. Share of total debt at June 30, 2026: 67,111 / 93,845 = 71.5%.
- Extended leverage: (debt + equipment installment plan facility + short-term borrowings) / Adjusted EBITDA: FY2024 (93,779 + 1,072 + 758) = 95,609 / 22,476 = 4.25x; FY2025 (94,617 + 1,447 + 918) = 96,982 / 22,611 = 4.29x; LTM Q2 2026 (93,845 + 1,596 + 1,155) = 96,596 / 22,251 = 4.34x. Operating leases (1,276 at December 31, 2025) are not added.
- Cash interest cover: 22,476 / 5,305 = 4.24x; 22,686 / 5,105 = 4.44x; 22,611 / 4,957 = 4.56x; 22,491 / 5,025 = 4.48x; 22,251 / 5,024 = 4.43x. For reference, FY2025 22,611 / 5,004 net interest expense = 4.52x.
- Free cash flow / principal debt: FY2024 5,709 / 93,779 = 6.09%; FY2025 5,827 / 94,617 = 6.16%; LTM Q2 2026 5,070 / 93,845 = 5.40%.
- Covenant proxy at December 31, 2025: secured 67,367 / (22,611 + 1,400) = 2.81x; total debt 94,617 / 24,011 = 3.94x; total plus equipment installment plan facility (94,617 + 1,447) / 24,011 = 4.00x. Headroom: indenture 6.0 - 4.0 = 2.0 turns and 1 - 4.0 / 6.0 = 33%; credit facility 5.0 - 2.8 = 2.2 turns and 1 - 2.8 / 5.0 = 44%; first lien 4.0 - 2.8 = 1.2 turns and 1 - 2.8 / 4.0 = 30% (debt held constant; printed ratios are rounded).

### Liquidity

- Liquidity (cash plus printed availability): Q3 2025 235 + 4,000 = 4,235; FY2025 218 + 4,400 = 4,618; Q1 2026 246 + 4,600 = 4,846; Q2 2026 285 + 3,700 = 3,985. Availability is printed to 0.1 billion, so each sum is accurate to about 50.
- Year-end rebuild: revolver capacity 960 + 5,500 = 6,460; implied drawn revolver = 11,949 principal - (413 + 4,300 + 729 + 2,000 + 2,500 = 9,942 term loans) = 2,007; availability 6,460 - 2,007 - 26 collateralised letters of credit = 4,427, consistent with the printed "approximately $4.4 billion". Using the printed 2,100 outstanding on the Revolving Loan C gives 4,334; the difference arises from rounded inputs.
- Change in credit facility principal March to June 2026: 12,453 - 11,665 = 788; fall in availability 4,600 - 3,700 = 900.

### Maturities and class movements

- Year-end ladder sum: 1,055 + 3,555 + 5,392 + 7,279 + 13,868 + 63,468 = 94,617.
- 2026 tie-out: 750 + (25 + 227 + 8 + 20 + 25 = 305) = 1,055. 2027: 3,250 + 305 = 3,555 (so the Revolving Loan B was undrawn). 2028 notes 2,500 + 1,000 + 1,250 = 4,750; remainder 642 less 280 of other amortisation = 362 for Term A-6 (413 - 25 - 25 = 363 by schedule). 2029 notes 1,500 + 1,500 + 1,250 + 1,250 + 1,500 = 7,000 plus about 280 amortisation = 7,279.
- Series tie-out: CCO Holdings 27,250; Charter Operating 44,500; TWC, LLC 9,918; TWCE 1,000; subtotal 82,668; plus credit facilities 11,949 = 94,617. Secured notes 44,500 + 9,918 + 1,000 = 55,418, matching the secured notes line.
- Class movement December 31, 2025 to June 30, 2026: unsecured 27,250 - 26,734 = 516 (3,000 issued and 3,000 redeemed net to zero); secured 55,418 - 54,658 = 760, of which the sterling notes were remeasured from 842 + 876 = 1,718 to 829 + 862 = 1,691, a 27 reduction, so repurchases were 733; total repurchases 516 + 733 = 1,249, consistent with the stated 1.2 billion. Total change 93,845 - 94,617 = -772 = -1,249 + 504 (credit facilities) - 27 (sterling remeasurement).

### Tie-outs

- Expense block to operating income: FY2025 32,836 + 8,681 + 432 = 41,949; 54,774 - 41,949 = 12,825. FY2024 33,260 + 8,643 + 117 = 42,020; 55,085 - 42,020 = 13,065. Q2 2026 8,236 + 2,189 + 51 = 10,476; 13,526 - 10,476 = 3,050. Q2 2025 8,255 + 2,169 + 86 = 10,510; 13,766 - 10,510 = 3,256. 6M 2026 16,418 + 4,393 + 66 = 20,877; 27,123 - 20,877 = 6,246. 6M 2025 16,474 + 4,342 + 209 = 21,025; 27,501 - 21,025 = 6,476. No unresolved difference.
- Adjusted EBITDA reconciliations: Q2 2026 1,973 + 0 + 1,270 + 16 + 2,189 + 138 - 158 = 5,428; Q2 2025 1,930 + 0 + 1,254 + 15 + 2,169 + 157 + 143 = 5,668; 6M 2026 3,779 + 1 + 2,515 + 30 + 4,393 + 341 - 13 = 11,046; 6M 2025 3,767 + 1 + 2,485 + 24 + 4,342 + 379 + 408 = 11,406; FY2025 7,440 + 1 + 5,004 + 20 + 8,681 + 673 + 792 = 22,611; FY2024 7,406 + 3 + 5,192 + 72 + 8,643 + 651 + 509 = 22,476.
- Revenue by product line, FY2025: 42,580 + 7,315 + 1,468 + 3,411 = 54,774; Q2 2026: 10,351 + 1,865 + 416 + 894 = 13,526.
- Carrying debt: Dec 2025 750 + 94,006 = 94,756; Jun 2026 999 + 92,960 = 93,959; Dec 2024 1,799 + 92,134 = 93,933.
- Balance sheet, June 30, 2026: total current liabilities 12,868 + long-term debt 92,960 + equipment installment plan facility 1,596 + deferred income taxes 68 + other long-term liabilities 3,342 + total member's equity 42,605 = 153,439 total assets.
- Cox figure differences: 12.6 - 12.4 = 0.2 billion; 4.2 - 4.0 = 0.2 billion; 3.5 billion + 650 = 4,150 against the stated 4.2 billion (rounded).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No filing or release after July 24, 2026: no September 30, 2026 balance sheet, leverage, liquidity or covenant figure, and no Cox closing status | High | CP-1A, CP-2, CP-5 | Supply the Q3 2026 10-Q and any 8-K to November 5, 2026, or confirm none |
| Current series-level debt and maturity ladder not supplied; 1,249 of repurchases are not mapped to series and amortisation paid in 2026 is not itemised | High | CP-2 | Supply a current debt schedule or the next 10-Q debt note |
| Covenant ratios after December 31, 2025 not printed; covenant EBITDA, management fees (rounded to 0.1 billion) and indenture definitions not supplied | High | CP-2, CP-5 | Supply compliance certificates, the Charter Operating credit agreement and the indentures |
| Facility-level availability and letters of credit at June 30, 2026 not printed; December 31, 2024 availability not printed | Medium | CP-2 | Supply the facility schedule at the latest date |
| Whether the 256 mortgage note is in the debt figure and the equipment installment plan facility's revolving-period renewal date are not stated | Medium | CP-2 | Supply the note terms and the facility amendment |
| Issuer share of the 17,122 contractual obligations (the table includes parent companies) and operating leases after December 31, 2025 not supplied | Medium | CP-2 | Supply issuer-level commitments |
| Whether the issuer or the parent funds the approximately 4.2 billion Cox cash price (the 10-Q says "we" but names Charter and Charter Holdings as payers) is ambiguous | Medium | CP-1A, CP-2 | Supply the Transaction Agreement financing terms and any commitment papers |
| Cox and Liberty Broadband agreements, the Cox EBITDA and any pro forma leverage not supplied, so no post-closing leverage is computed | Medium | CP-1A, CP-2 | Supply the agreements, the proxy statement and Cox financials |
| Adjusted EBITDA is a company non-GAAP measure with other add-backs ("Other, net" of 792 in FY2025); no reconciliation to covenant EBITDA | Medium | CP-2, CP-5 | Treat ratios as indicative |
| No discrete Q3 or Q4 2025 statements and no June 30, 2025 balance sheet; Q4 2025 values are derived by difference | Low | CP-1 | Use 9M and FY differences as labelled |
| Text extraction only; original HTML and XBRL not supplied | Low | CP-5 | Spot-check flagged tables against the filed documents |

## Next module

- CP-1A: take the single reportable segment, product-line revenue, customer trends, ownership chain, guarantor and collateral structure and the Cox and Liberty Broadband transactions from this handoff; show both the 12.6 and 12.4 billion Cox debt figures and the 4.0 and 4.2 billion cash figures with their dates; carry the Cox payer ambiguity and the lack of post-July 24, 2026 evidence.
- CP-2: start from the debt-by-instrument table, the maturity roll-forward, the liquidity table and the covenant table; treat 1,596 of equipment installment plan financing, 1,155 of short-term borrowings and the leases and commitments as claims outside the debt figure; do not compare the computed ratios with covenant levels; carry the missing indentures and credit agreement, the rounded management fees and the unmapped repurchases as limits.
- CP-5: trace every figure to the locators given; flag that LTM, derived-quarter, ratio, roll-forward and proxy rows are calculated, not reported, and that availability figures are rounded to 0.1 billion.
