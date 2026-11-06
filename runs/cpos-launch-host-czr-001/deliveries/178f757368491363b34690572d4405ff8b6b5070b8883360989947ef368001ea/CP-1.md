# CP-1 — Financial statements and credit metrics: Caesars Entertainment, Inc. (czr)

## Request

- Issuer: Caesars Entertainment, Inc. (issuer id `czr`), as of 2026-10-02, information cutoff 2026-10-02.
- Run: `czr-2026-10-02-credit_snapshot-host`, pathway `credit_snapshot`. Feeds CP-1A, CP-2, CP-5 and the report section "Financials and credit metrics".
- Execution: host session. The host read the pinned text files and wrote this answer. No provider was called. Calculations were done separately from the extracted figures and are listed in `## Calculations`.
- Scope: reported FY2025, FY2024 and FY2023 statements; June 30, 2026 interim statements; last-twelve-months (LTM) figures to June 30, 2026 built from them; debt, lease financing obligations, liquidity, issuer non-GAAP measures and the covenant terms the 10-Q describes. No rating, forecast, valuation or merger pro forma.

## Sources

| Source | sha256 | Used for |
| --- | --- | --- |
| CZR_FY2025_10K.txt | 172309048af2a6a2dab515d765f00a7c89bf8c874c6104a5e3a052b66cad4512 | Audited FY2025 statements, debt note, Adjusted EBITDA reconciliation, liquidity |
| CZR_Q2_2026_10Q.txt | f369ce5f1ebeddd9a0d4ce02ce3958112267d8701d1a348dfd6dc82d2034793a | June 30, 2026 interim statements, debt note, covenants, liquidity |
| CZR_Q2_2026_Earnings_Release.txt | b385f76ff631243d1053fa8073ebde4f8886b4a50c9ce34ce3498d6b2ac3e9f8 | Issuer Adjusted EBITDA for the quarter and six months; issuer net debt |
| context | 70a1a94c5cc4a6bf8f11bf47e9f0a41d9be046e2bcfa93425809b6450d15d5c1 | Run settings: USD; current period q2-2026; prior period fy-2025 |

Supplied handoff consumed: CP-0 sha256 c25e5a54d628dec4614d6d52f99b207b6b261bfcb442c3bed0d41c0af7f514a3. Carried forward from CP-0: the 10-K and 10-Q control statement facts; the release is issuer non-GAAP and duplicates the 10-Q statement of operations; lease financing obligations are separate from debt; the pending merger and its financing are not described in figures; nothing after July 28, 2026 is supplied.

Locators: `10-K line N`, `10-Q line N` and `release line N` are lines of the pinned text files.

## Findings

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Caesars Entertainment, Inc., consolidated, with noncontrolling interests | Years ended December 31, 2025, 2024 and 2023; balance sheets at December 31, 2025 and 2024 | Audited | "(In millions, except per share data)" (10-K line 1728); USD |
| 10-Q Q2 2026 | Same consolidated perimeter | Three and six months ended June 30, 2026 and 2025; balance sheet at June 30, 2026 and December 31, 2025 | Unaudited condensed | "(In millions)" (10-Q line 66); USD |
| Release | Same perimeter, issuer presentation | Three and six months ended June 30, 2026 and 2025 | Unaudited, non-GAAP | Millions; USD |

### Financials and credit metrics

| Metric | LTM to June 30, 2026 | FY2025 | Basis and source |
| --- | --- | --- | --- |
| Net revenues (USD m) | 11,648 | 11,486 | LTM calculated, C1; FY reported, 10-K line 1734 |
| Operating income (USD m) | 1,857 | 1,858 | LTM calculated, C1; FY reported, 10-K line 1746 |
| Adjusted EBITDA, issuer-defined (USD m) | 3,592 | 3,624 | LTM calculated, C1; FY reported, 10-K line 1329 |
| Interest expense, net, incl. lease financing interest (USD m) | 2,293 | 2,304 | LTM calculated, C1; FY reported, 10-K line 1748 |
| Cash interest paid for debt (USD m) | 776 | 813 | LTM calculated, C1; FY reported, 10-K line 1867 |
| Cash interest paid for rent on VICI and GLPI leases (USD m) | 1,363 | 1,349 | LTM calculated, C1, label differs by period (see gaps); FY reported, 10-K line 1868 |
| Net cash provided by operating activities (USD m) | 1,297 | 1,302 | LTM calculated, C1; FY reported, 10-K line 1833 |
| Purchase of property and equipment (USD m) | (687) | (805) | LTM calculated, C1; FY reported, 10-K line 1835 |
| Free cash flow, CFO less capex (USD m) | 610 | 497 | Calculated, C2 |
| Cash and cash equivalents (USD m) | 965 | 887 | Reported, 10-Q line 69; 10-K line 1685 |
| Total debt, face value (USD m) | 11,807 | 11,905 | Reported, 10-Q line 507; 10-K line 2362 |
| Net debt, issuer-defined (USD m) | 10,842 | 11,018 | Reported non-GAAP, release line 78 |
| Long-term financing obligations, carrying (USD m) | 13,157 | 13,096 | Reported, 10-Q line 89; 10-K line 1705 |
| Total debt / Adjusted EBITDA (x) | 3.29 | 3.29 | Calculated, C3 |
| Net debt / Adjusted EBITDA (x) | 3.02 | 3.04 | Calculated, C3 |
| Debt plus financing obligations / Adjusted EBITDA (x) | 6.95 | 6.90 | Calculated, C4 |
| Total debt / Adjusted EBITDA after cash rent (x) | 5.30 | 5.23 | Calculated, C5 |
| Adjusted EBITDA / interest expense, net (x) | 1.57 | 1.57 | Calculated, C6 |
| Adjusted EBITDA after cash rent / cash interest paid for debt (x) | 2.87 | 2.80 | Calculated, C6 |
| Adjusted EBITDA margin (%) | 30.8 | 31.6 | Calculated, C7 |
| Total stockholders’ equity (USD m) | 3,552 | 3,686 | Reported, 10-Q line 98; 10-K line 1720 |

Which leverage basis to read: Adjusted EBITDA excludes the lease cost. The release says Adjusted EBITDA "excludes the expense associated with certain of our leases as these transactions were accounted for as financing obligations and the associated expense is included in interest expense" (release line 96). Total debt over Adjusted EBITDA therefore leaves out the lease burden. The two lease-inclusive bases (C4 and C5) are the fuller view of fixed obligations. None of these ratios is covenant leverage.

### Reported statements of operations

| Line (as printed) | Q2 2026 | Q2 2025 | Six months 2026 | Six months 2025 | FY2025 | FY2024 | FY2023 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net revenues | 2,993 | 2,907 | 5,863 | 5,701 | 11,486 | 11,245 | 11,528 |
| Depreciation and amortization | 355 | 364 | 702 | 721 | 1,417 | 1,324 | 1,261 |
| Operating income | 513 | 526 | 1,013 | 1,014 | 1,858 | 2,304 | 2,472 |
| Interest expense, net | (573) | (579) | (1,142) | (1,153) | (2,304) | (2,366) | (2,342) |
| Net loss / Net income (loss) | (41) | (65) | (124) | (163) | (437) | (211) | 828 |
| Net loss / Net income (loss) attributable to Caesars | (62) | (82) | (160) | (197) | (502) | (278) | 786 |

Sources: 10-Q lines 113 to 133; 10-K lines 1734 to 1756. Interest expense is printed in parentheses as a deduction and kept signed. FY2023 net income includes a tax benefit: the 10-K notes "the release of $940 million of valuation allowance against deferred tax assets" (10-K line 1333).

### Reported balance sheet (selected lines)

| Line (as printed) | June 30, 2026 | December 31, 2025 | December 31, 2024 |
| --- | --- | --- | --- |
| Cash and cash equivalents | 965 | 887 | 866 |
| Restricted cash | 96 | 85 | 95 |
| Total current assets | 1,977 | 1,803 | 1,747 |
| Goodwill | 10,441 | 10,441 | 10,601 |
| Total assets | 31,742 | 31,639 | 32,590 |
| Current portion of long-term debt | 114 | 114 | 109 |
| Total current liabilities | 2,322 | 2,253 | 2,272 |
| Long-term financing obligations | 13,157 | 13,096 | 12,899 |
| Long-term debt | 11,585 | 11,670 | 12,033 |
| Total liabilities | 28,190 | 27,953 | 28,214 |
| Total stockholders’ equity | 3,552 | 3,686 | 4,376 |

Sources: 10-Q lines 64 to 99; 10-K lines 1680 to 1722. Totals were checked against their printed components (C8).

### Reported cash flows (selected lines)

| Line (as printed) | Six months 2026 | Six months 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 675 | 680 | 1,302 | 1,075 |
| Purchase of property and equipment | (335) | (453) | (805) | (1,296) |
| Repurchase of common stock | — | (100) | (229) | (191) |
| Financing obligation payments | (19) | (8) | (26) | (8) |
| Distributions to noncontrolling interest owners | (41) | (30) | (102) | (16) |
| Cash interest paid for debt | 368 | 405 | 813 | 1,052 |
| Cash interest paid for rent on VICI and GLPI leases (10-Q label) / related to financing obligations (10-K label) | 686 | 672 | 1,349 | 1,324 |

Sources: 10-Q lines 197 to 251; 10-K lines 1811 to 1868. The cash roll-forwards reconcile (C9).

### Debt register at June 30, 2026

| Instrument (as printed) | Final maturity | Rate | Face value | Book value |
| --- | --- | --- | --- | --- |
| CEI Revolving Credit Facility | 2028 | variable | 120 | 120 |
| CEI Term Loan A | 2028 | variable | 619 | 618 |
| CVA Delayed Draw Term Loan | 2029 | variable | 376 | 372 |
| CEI Term Loan B | 2030 | variable | 2,018 | 1,993 |
| CEI Term Loan B-1 | 2031 | variable | 2,835 | 2,808 |
| CEI Senior Secured Notes due 2030 | 2030 | 7.00% | 2,000 | 1,987 |
| CEI Senior Secured Notes due 2032 | 2032 | 6.50% | 1,500 | 1,487 |
| CEI Senior Notes due 2029 | 2029 | 4.625% | 1,200 | 1,193 |
| CEI Senior Notes due 2032 | 2032 | 6.00% | 1,100 | 1,088 |
| Special Improvement District Bonds | 2037 | 4.30% | 38 | 38 |
| Total debt | — | — | 11,807 | 11,705 |

Source: 10-Q lines 490 to 507. The CVA Revolving Credit Facility and "Long-term notes and other payables" rows are omitted here; the components add to the printed face total (C10). The release splits the face total into "Bank debt and loans | $5,968", "Notes | 5,800" and "Other long-term debt | 39" (release lines 74 to 76).

Maturities: "Annual maturities of long-term debt | $55 | $114 | $767 | $1,574 | $3,962 | $5,335 | $11,807" for the remainder of 2026, then 2027, 2028, 2029, 2030 and thereafter (10-Q, debt service table after line 507). The 2028 bucket includes the CEI Revolving Credit Facility and Term Loan A, which mature in 2028.

### Lease financing obligations

The VICI and GLPI leases are recorded as "Long-term financing obligations" of 13,157 at June 30, 2026 (10-Q line 89), larger than total debt. Their cash cost appears as cash interest for rent: 686 in the first six months of 2026 (10-Q line 250). The issuer estimates "lease payments to VICI and GLPI to be approximately $687 million for the remainder of 2026" (10-Q liquidity section, after line 1289). The 10-Q also says "The VICI Leases are subject to annual escalations ... based on the Consumer Price Index", so the lease cost rises over time.

### Liquidity at June 30, 2026

| Component (as printed) | Amount (USD m) |
| --- | --- |
| Cash and cash equivalents | 965 |
| CEI Revolving Credit Facility capacity, net of outstanding balance | 2,130 |
| CVA Revolving Credit Facility capacity | 25 |
| Revolver capacity committed to letters of credit | (96) |
| Revolver capacity committed to specific reserves | (40) |
| Revolver capacity committed as regulatory requirement | (56) |
| Total | 2,928 |

Source: 10-Q lines 1282 to 1289. The issuer estimates "debt service (including principal and interest) is approximately $425 million for the remainder of 2026" (10-Q liquidity section).

### Issuer non-GAAP measures

| Line (as printed) | Q2 2026 | Q2 2025 | Six months 2026 | Six months 2025 | FY2025 |
| --- | --- | --- | --- | --- | --- |
| Net loss / Net income (loss) attributable to Caesars | (62) | (82) | (160) | (197) | (502) |
| Interest expense, net | 573 | 579 | 1,142 | 1,153 | 2,304 |
| Depreciation and amortization | 355 | 364 | 702 | 721 | 1,417 |
| Transaction costs and other, net | 29 | 41 | 45 | 54 | 72 |
| Stock-based compensation expense | 23 | 24 | 47 | 50 | 95 |
| Adjusted EBITDA | 920 | 955 | 1,807 | 1,839 | 3,624 |

Sources: release lines 179 to 191; 10-K lines 1318 to 1329. Each reconciliation adds exactly from its printed lines (C11). FY2025 also has "Impairment charges" of 182 as an add-back (10-K line 1325). The 10-K says "The definition of Adjusted EBITDA may not be the same as the definitions used in any of our debt agreements" (10-K line 1315).

### Covenants described in the 10-Q

| Term | Description | Source |
| --- | --- | --- |
| CEI Revolving Credit Facility and Term Loan A | "a maximum net total leverage ratio financial covenant of 6.50:1" and "a minimum fixed charge coverage ratio financial covenant of 2.0:1" | 10-Q lines 595 to 596 |
| After Term Loan A is repaid | The revolver covenants "will be tested solely to the extent that certain testing conditions are satisfied" | 10-Q line 597 |
| Caesars Virginia facilities | "a maximum net total leverage ratio financial covenant of 4:1 and a minimum fixed charge coverage ratio financial covenant of 1.05:1, applicable to the operations of Caesars Virginia" | 10-Q line 599 |
| Compliance | "As of June 30, 2026, the Company was in compliance with all of the applicable financial covenants described above." | 10-Q line 600 |

Headroom is Not calculable: the agreements' definitions of net total leverage and fixed charges are not supplied, and the treatment of the lease obligations in them is unknown. The analytical ratios above are not compared with these thresholds.

### Narrative review

- Leverage: debt-only leverage is moderate at 3.29x on issuer Adjusted EBITDA, but that measure excludes the lease cost. Including the lease obligations, leverage is 6.95x on carrying amounts, or 5.30x on debt over Adjusted EBITDA after cash rent. Mechanism: fixed lease payments to VICI and GLPI rank alongside debt service for cash, and they escalate with inflation. Implication: Caesars should be read as a highly levered, lease-heavy credit; the debt-only ratio overstates its flexibility.
- Coverage: Adjusted EBITDA covers total net interest, which includes lease interest, only 1.57x. After cash rent, Adjusted EBITDA covers cash interest on debt 2.87x. Interest coverage is thin on the full basis and improving slowly as debt falls.
- Cash flow quality: LTM operating cash flow of 1,297 less capex of 687 leaves free cash flow of 610, up from 497 in FY2025 because capex fell. GAAP net losses persist in every period shown since FY2024 because interest, including lease interest, exceeds operating income.
- Liquidity: 2,928 of cash and available revolver capacity at June 30, 2026, against estimated debt service of about 425 and lease payments of about 687 for the rest of 2026. No large maturity before 2028, when the revolver and Term Loan A mature.
- Earnings trend: LTM net revenues grew to 11,648, but Adjusted EBITDA fell from 3,624 to 3,592 and the Adjusted EBITDA margin from 31.6% to 30.8%. Q2 2026 Adjusted EBITDA was 920 against 955 a year earlier.
- Data quality: audited annual and unaudited interim statements reconcile on every checked total (C8 to C11). Text conversion flattened tables; no layout errors were found in the rows used.
- Definition risks: issuer Adjusted EBITDA excludes lease costs and adds back transaction costs and stock compensation. Covenant definitions are not supplied.
- Key gaps: merger financing and post-closing capital structure; executed credit agreement and indentures; the lease agreements.

### Readiness for downstream modules

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1A | Sufficient for business and capital-structure description | Statements, debt register, leases and liquidity above |
| CP-2 | Sufficient with limitations | Credit metrics on three labelled bases; merger effects are Not supplied |
| CP-5 | Sufficient | Every figure has a line locator or a calculation ID |

### Quality review of claims

| Claim | Material | Lineage | Note |
| --- | --- | --- | --- |
| Debt plus financing obligations / Adjusted EBITDA is 6.95x | Yes | Calculated | Carrying amount of the obligations, not a capitalised rent multiple |
| Debt / Adjusted EBITDA after cash rent is 5.30x | Yes | Calculated | The LTM rent combines two labels (see gaps) |
| Adjusted EBITDA / net interest is 1.57x | Yes | Calculated | Net interest includes lease interest |
| In compliance with financial covenants | Yes | Directly Sourced | 10-Q line 600; management statement |
| Covenant headroom | Yes | Insufficient Information | Agreement definitions not supplied |

Open quality findings: one MATERIAL finding, the merger may change the debt structure and no merger financing is supplied. One MINOR finding, the cash-rent label differs between the 10-K and the 10-Q.

## Calculations

All inputs are USD millions copied from the cited lines. Ratios are rounded half up to two decimals and percentages to one decimal.

| ID | Formula | Inputs and locators | Result |
| --- | --- | --- | --- |
| C1 | LTM = FY2025 + six months 2026 − six months 2025 | Net revenues 11,486 + 5,863 − 5,701; operating income 1,858 + 1,013 − 1,014; Adjusted EBITDA 3,624 + 1,807 − 1,839; interest expense 2,304 + 1,142 − 1,153; operating cash flow 1,302 + 675 − 680; capex 805 + 335 − 453; cash interest for debt 813 + 368 − 405; cash rent 1,349 + 686 − 672 (10-K lines 1734, 1746, 1329, 1748, 1833, 1835, 1867, 1868; 10-Q lines 113, 124, 126, 218, 220, 249, 250; release line 64) | 11,648; 1,857; 3,592; 2,293; 1,297; 687; 776; 1,363 |
| C2 | Operating cash flow less capex | LTM 1,297 − 687; FY2025 1,302 − 805; six months 2026 675 − 335 | 610; 497; 340 |
| C3 | Total debt / Adjusted EBITDA; net debt / Adjusted EBITDA | June 30, 2026: 11,807 / 3,592; 10,842 / 3,592. December 31, 2025: 11,905 / 3,624; 11,018 / 3,624 | 3.29x; 3.02x. 3.29x; 3.04x |
| C4 | (Total debt + long-term financing obligations) / Adjusted EBITDA | (11,807 + 13,157) / 3,592; (11,905 + 13,096) / 3,624 | 6.95x; 6.90x |
| C5 | Total debt / (Adjusted EBITDA − cash rent) | 3,592 − 1,363 = 2,229, 11,807 / 2,229; 3,624 − 1,349 = 2,275, 11,905 / 2,275 | 5.30x; 5.23x |
| C6 | Adjusted EBITDA / interest expense, net; (Adjusted EBITDA − cash rent) / cash interest for debt | 3,592 / 2,293; 2,229 / 776. FY2025: 3,624 / 2,304; 2,275 / 813 | 1.57x; 2.87x. 1.57x; 2.80x |
| C7 | Adjusted EBITDA / net revenues | 3,592 / 11,648; 3,624 / 11,486 | 30.8%; 31.6% |
| C8 | Balance-sheet totals from components | June 30, 2026: current assets 965 + 96 + 485 + 49 + 382; total assets 1,977 + 124 + 14,125 + 10,441 + 3,959 + 68 + 1,048; current liabilities 290 + 222 + 1,696 + 114; total liabilities 2,322 + 13,157 + 11,585 + 57 + 1,069; plus equity 3,552. December 31, 2025 likewise (10-K lines 1685 to 1720) | 1,977; 31,742; 2,322; 28,190; 31,742 — all equal to printed totals; December 31, 2025 totals also equal |
| C9 | Cash roll-forward | Six months 2026: 675 − 411 − 171 = 93, 984 + 93 = 1,077. FY2025: 1,302 − 571 − 763 = −32, 1,016 − 32 = 984 | Equal to printed values |
| C10 | Debt face total | 120 + 619 + 0 + 376 + 2,018 + 2,835 + 2,000 + 1,500 + 1,200 + 1,100 + 38 + 1; bank debt 120 + 619 + 376 + 2,018 + 2,835; notes 2,000 + 1,500 + 1,200 + 1,100 | 11,807; 5,968; 5,800, equal to printed and release values; 11,807 − 965 = 10,842, equal to release net debt |
| C11 | Adjusted EBITDA reconciliations | Q2 2026: −62 + 21 − 12 − 7 + 573 + 355 + 29 + 23. Six months 2026: −160 + 36 + 0 − 5 + 1,142 + 702 + 45 + 47. FY2025: −502 + 65 − 11 − 2 + 4 + 2,304 + 182 + 1,417 + 72 + 95 | 920; 1,807; 3,624, equal to printed values |
| C12 | Revenue growth | Q2: 2,993 / 2,907 − 1; six months: 5,863 / 5,701 − 1 | 3.0%; 2.8%, equal to the release's 3.0% and 2.8% |

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Merger financing and post-closing capital structure not supplied | Leverage and ranking after the take-private are unknown | Supply the Merger Agreement, merger proxy and financing documents |
| Cash-rent label differs: 10-K "related to financing obligations"; 10-Q "related to GLPI and VICI Leases", with a separate "other financing obligations" line of 5 in 2026 | LTM cash rent may include a small amount of other obligations | Treat C5 and C6 after-rent ratios as approximate |
| Covenant definitions not supplied | Headroom Not calculable | Supply executed credit agreement |
| Lease agreements not supplied | Escalators and variable rent are described, not read | Supply the VICI and GLPI leases |
| Events after July 28, 2026 not supplied | Liquidity and debt at the as-of date may differ | Supply later filings |

## Next module

- CP-1A: carry the merger, the lease structure, the debt register and the liquidity table into the transaction and profile sections.
- CP-2: read leverage on the lease-inclusive bases; carry the merger and covenant-definition gaps.
- CP-5: trace every figure to its line or calculation ID above.
