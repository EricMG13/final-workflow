# CP-1 financial base: CHS INC (chscp)

## Request

CHS INC (issuer id chscp), the consolidated agricultural cooperative CHS Inc. and its subsidiaries, as of 2026-11-05, credit_snapshot pathway. This module builds the financial base: reported statements for fiscal 2026 (year ended 2026-08-31), fiscal 2025 and fiscal 2024, the fiscal 2026 quarters, the debt register, liquidity, claims outside debt, and the leverage, coverage, liquidity and maturity chart data. Currency is USD. Statement amounts are USD thousands as printed unless a row says USD millions; the chart tables are in the units their headings fix. The perimeter is CHS Inc. consolidated; the sources name no separate borrower, parent or guarantor entity. Nothing dated after the cutoff 2026-11-05 is used.

## Sources

### Issuer sources relied on

| Source name | sha256 | Used for |
| --- | --- | --- |
| 10-K_2026-08-31_chscp-20260831.htm.jsonl | 7af90f68bff1cc427159bcc12ffc87c427ce829f2621b0c4238922f45880492c | Audited statements, debt note, liquidity, segments, leases, pensions, commitments |
| 10-Q_2025-11-30_chscp-20251130.htm.jsonl | 3b343d46b4f667e29be99b08f7d799dc25471f06dbcbf91d62c596b40053bc50 | Fiscal Q1 2026 and prior-year quarter statements, balance sheet at 2025-11-30 |
| 10-Q_2026-02-28_chscp-20260228.htm.jsonl | 335ab8ab1983479e957ab5bcc688bac42f2a8847cb6800ad1d72a83671457084 | Fiscal Q2 2026 and six months, balance sheet at 2026-02-28 |
| 10-Q_2026-05-31_chscp-20260531.htm.jsonl | d9720f91bf0c93fa122637a031df8f3b728863173bc1b8717d0a6e377caf2082 | Fiscal Q3 2026 and nine months, balance sheet at 2026-05-31, facility detail |
| EX-99.1_2026-04-08_a2qfy26earningrelease.htm.jsonl | 33496a1570da087ac1976522b03589f92cee4a9a2670952160166094e3791034 | Second quarter release, cross-check of quarter and six-month earnings |
| EX-99.1_2026-07-08_a3qfy26earningrelease.htm.jsonl | 9732954cd83cfd2faab08d34c8a937435e86ab588c7e99ee653b9179d1961e0c | Third quarter release, cross-check of quarter and nine-month earnings |
| EX-99.1_2026-11-04_a4qfy26earningrelease.htm.jsonl | cae53d4e6b095242a55a168a21c6d1a5d0c45880ba1e0b3a388701114a691f44 | Fiscal 2026 release: segment earnings, announced projects, fiscal 2027 owner distributions |

Context file sha256 7441cd131643680d7cdd1713c448cca9698ae339b2ccfb6c0e8da281781f9451 supplies the dates and currency only; it is not issuer evidence.

### Supplied handoffs

| Module | sha256 | How used |
| --- | --- | --- |
| CP-0 | c5f6c43eadd719108e1a786ea324314e25d2bbf3d44f9ea676626928c1bc9d76 | Source readiness: perimeter, gaps and conflicts carried forward; see the consistency section |

Locators read `file page:N`, where N is the extracted page chunk, not the printed page. "10-K" is the fiscal 2026 annual report; "10-Q Q1", "10-Q Q2" and "10-Q Q3" are the quarterly reports for the quarters ended 2025-11-30, 2026-02-28 and 2026-05-31; "Release FY" is the 2026-11-04 release.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| At fiscal 2026 year end, total debt was 2,501,725 (USD thousands), 1.27x derived EBITDA, with 11.79x cash interest cover. Year-end borrowing is seasonally low: leverage was 2.57x on a last-twelve-months basis at May 2026. | Medium | EBITDA is derived, not reported, includes equity income and ignores major maintenance spending. Covenant levels, letter of credit usage and fiscal 2024 debt are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Fiscal 2026 income before income taxes was 1,128,719 against 614,772 a year earlier; Energy moved from a 19,015 loss to 554,590 of earnings. | Energy alone more than accounts for the group improvement, so the durability of Energy earnings is the central credit question. | Medium |
| The fourth quarter derived alone produced 739,295 of pretax income, after 389,424 in the first nine months. | Annual leverage depends on one quarter; quarterly detail is derived, not reported. | Medium |
| Notes payable were 449,002 at year end but 1,995,108 at February 2026. | Quarter-end borrowing was far above the year-end figure that annual leverage uses. | High |
| Free cash flow after major maintenance was 1,052,492 in fiscal 2026 and negative 364,168 in fiscal 2025. | After preferred dividends and owner distributions it was 753,391 in fiscal 2026 and negative 1,120,877 in fiscal 2025, so cash generation is volatile. | Medium |
| Preferred stock of 2,264,038 sits in equity with 168,668 of annual dividends; purchase obligations total 7,604,191. | These claims are outside the debt figure; the preferred dividend is a fixed annual charge and purchase obligations are large commitments. | Medium |

### Financial base view

CHS Inc. entered fiscal 2026 with modest year-end leverage and finished with a very strong second half, when pretax income was 1,021,508 against 107,211 in the first half (C9). Derived EBITDA of 1,969,497 against total debt of 2,501,725 gives 1.27x at the 2026-08-31 balance sheet date, down from 2.12x a year earlier, and cash paid for interest of 167,057 is covered 11.79x. That picture is flattering in four ways that the base keeps in view. First, the EBITDA is our derivation (pretax income plus interest expense plus depreciation and amortization, including amortization of deferred major maintenance) because the company reports no EBITDA, and it includes 569,231 of equity income from joint ventures and affiliates. Second, nine-month operating earnings were a loss of 12,222 and the fourth quarter derived alone supplied most of the year, so the annual figure is dominated by one quarter. Third, the improvement is concentrated in one segment: Energy improved by 573,605, which exceeds the group improvement of 513,947 because Corporate and Services and Agronomy declined (C16). Fourth, working capital debt is seasonal: notes payable fell from 1,995,108 in February to 449,002 at year end, and on a last-twelve-months basis total debt over derived EBITDA was 2.57x in May 2026. The funded debt is long-dated private placement notes and a term loan with no single fiscal year through 2031 above 450,000, while the short-term funding includes securitization and repurchase facilities that now run only to 2027-08-25. Covenants are described only as minimum consolidated net worth and other financial ratios with compliance reported, so headroom is not measurable from these sources. The base supports statement-based credit work; it does not support covenant, ranking or recovery work.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | Not supplied: balance sheet at 2024-08-31 is not in the pinned sources | Not supplied: balance sheet at 2024-08-31 is not in the pinned sources | x | Debt and cash for 2024-08-31 are not printed in the fiscal 2026 10-K balance sheet, which shows 2026 and 2025 only |
| FY2025 | 2.12 | 1.88 | x | Derived EBITDA 1,412,277 (C1); total debt 2,988,290 and net debt 2,660,464 (C5), USD thousands; EBITDA is not company-reported and includes equity income |
| FY2026 | 1.27 | 1.14 | x | Derived EBITDA 1,969,497 (C1); total debt 2,501,725 and net debt 2,238,122 (C5), USD thousands; year-end seasonal low in short-term borrowing, so interim leverage is higher |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 17.62 | x | Derived EBITDA 1,771,742 over cash paid for interest 100,542 (C1, C6); not company-reported EBITDA |
| FY2025 | 9.57 | x | Derived EBITDA 1,412,277 over cash paid for interest 147,583 (C1, C6) |
| FY2026 | 11.79 | x | Derived EBITDA 1,969,497 over cash paid for interest 167,057 (C1, C6); preferred dividends of 168,668 are not in the denominator |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 794.865 | Not supplied: borrowings under the revolving credit facility at 2024-08-31 are not in the pinned sources | US$m | Cash and cash equivalents at 2024-08-31 from 10-K page:148; excludes restricted cash of 78.997 |
| FY2025 | 327.826 | 2,620.0 | US$m | Revolver commitment 2,800.0 less 180.0 borrowed at 2025-08-31 (C7); commitment assumed unchanged from the stated 2,800.0; letters of credit not supplied; excludes restricted cash of 71.434 |
| FY2026 | 263.603 | 2,800.0 | US$m | Revolver commitment 2,800.0 with no borrowings at 2026-08-31 (10-K page:163); letters of credit drawn on it not supplied so availability may be lower; securitization and repurchase capacity excluded because the committed share is not separable; excludes restricted cash of 123.217 |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2027 | 58.562 | US$m | Long-term debt maturities excluding finance leases (10-K page:165); excludes notes payable of 449.002 and the securitization and repurchase facilities, which run to 2027-08-25 |
| FY2028 | 190.600 | US$m | Long-term debt maturities (10-K page:165) |
| FY2029 | 0.150 | US$m | Long-term debt maturities (10-K page:165) |
| FY2030 | 450.000 | US$m | Includes the 300.0 term loan, payable 2029-10-29, and the 150.0 note due fiscal 2030 (10-K page:165) |
| FY2031 | 200.000 | US$m | Long-term debt maturities (10-K page:165) |
| FY2032 and later | 1,105.000 | US$m | Printed as "Thereafter"; total ladder 2,004.312 excludes finance leases (51.845) and deferred financing costs |

### Financials and credit metrics

| Metric | FY2026 | FY2025 | FY2024 | Basis and source |
| --- | --- | --- | --- | --- |
| Revenues (USD thousands) | 39,231,217 | 35,462,608 | 39,261,229 | Reported, 10-K page:144 |
| Gross profit (USD thousands) | 1,787,857 | 1,136,814 | 1,751,327 | Reported, 10-K page:144 |
| Operating earnings (USD thousands) | 591,882 | 90,755 | 584,358 | Reported, 10-K page:144 |
| Interest expense (USD thousands) | 163,633 | 146,079 | 104,064 | Reported, net of capitalized interest of 25.6 million, 32.2 million and 25.7 million; 10-K page:144, page:165 |
| Equity income from investments (USD thousands) | 569,231 | 569,665 | 479,863 | Reported, 10-K page:144 |
| Income before income taxes (USD thousands) | 1,128,719 | 614,772 | 1,097,787 | Reported, 10-K page:144 |
| Net income attributable to CHS Inc. (USD thousands) | 1,095,903 | 597,917 | 1,102,319 | Reported, 10-K page:144 |
| Depreciation and amortization incl. deferred major maintenance (USD thousands) | 677,145 | 651,426 | 569,891 | Reported, 10-K page:146 |
| EBITDA, derived: pretax income + interest expense + D&A (USD thousands) | 1,969,497 | 1,412,277 | 1,771,742 | Calculated, C1; not company-reported |
| Operating EBITDA, derived: operating earnings + D&A (USD thousands) | 1,269,027 | 742,181 | 1,154,249 | Calculated, C2; excludes equity income and other income |
| Cash paid for interest (USD thousands) | 167,057 | 147,583 | 100,542 | Reported, 10-K page:146 |
| Net cash provided by operating activities (USD thousands) | 1,584,009 | 635,787 | 1,272,880 | Reported, 10-K page:146 |
| Acquisition of property, plant and equipment (USD thousands) | (463,262) | (728,575) | (808,763) | Reported, 10-K page:146 |
| Expenditures for major maintenance (USD thousands) | (68,255) | (271,380) | (22,748) | Reported, 10-K page:146 |
| Free cash flow after major maintenance (USD thousands) | 1,052,492 | (364,168) | 441,369 | Calculated, C3 |
| Preferred stock dividends paid (USD thousands) | (168,668) | (168,668) | (168,668) | Reported, 10-K page:146 |
| Cash patronage dividends paid (USD thousands) | (30,000) | (300,358) | (366,012) | Reported, 10-K page:146 |
| Redemptions of equities (USD thousands) | (100,433) | (287,683) | (355,925) | Reported, 10-K page:146 |
| Free cash flow after owner and preferred distributions (USD thousands) | 753,391 | (1,120,877) | (449,236) | Calculated, C4 |
| Cash and cash equivalents (USD thousands) | 263,603 | 327,826 | 794,865 | Reported, 10-K page:144, page:148 |
| Notes payable (USD thousands) | 449,002 | 1,152,457 | Not supplied: 2024-08-31 balance sheet not in sources | Reported, 10-K page:144 |
| Long-term debt including current portion (USD thousands) | 2,052,723 | 1,835,833 | Not supplied: 2024-08-31 balance sheet not in sources | Reported, 10-K page:165; includes finance leases, net of deferred financing costs |
| Total debt (USD thousands) | 2,501,725 | 2,988,290 | Not supplied: 2024-08-31 balance sheet not in sources | Calculated, C5 |
| Net debt (USD thousands) | 2,238,122 | 2,660,464 | Not supplied: 2024-08-31 balance sheet not in sources | Calculated, C5; cash and cash equivalents only, restricted cash not netted |
| Total equities (USD thousands) | 11,644,845 | 11,080,174 | 10,761,924 | Reported, 10-K page:144, page:145 |
| Total debt / EBITDA (x) | 1.27 | 2.12 | Not supplied: 2024 debt not in sources | Calculated, C5 |
| Net debt / EBITDA (x) | 1.14 | 1.88 | Not supplied: 2024 debt not in sources | Calculated, C5 |
| Total debt / operating EBITDA (x) | 1.97 | 4.03 | Not supplied: 2024 debt not in sources | Calculated, C5 |
| EBITDA / cash paid for interest (x) | 11.79 | 9.57 | 17.62 | Calculated, C6 |
| Operating EBITDA / cash paid for interest (x) | 7.60 | 5.03 | 11.48 | Calculated, C6 |
| Total debt / (total debt + total equities) (%) | 17.7 | 21.2 | Not supplied: 2024 debt not in sources | Calculated, C8 |
| Working capital (USD thousands) | 3,792,719 | 2,803,865 | Not supplied: 2024 balance sheet not in sources | Reported, 10-K page:74 |
| Current ratio (x) | 1.7 | 1.5 | Not supplied: 2024 balance sheet not in sources | Reported, 10-K page:74 |

### Quarterly view

Reported quarters come from the 10-Qs; the fourth quarter is the fiscal year less the nine-month 10-Q amounts and is derived (C9). All amounts are USD thousands. EBITDA is the derived measure of C1 applied to each quarter, with quarterly depreciation and amortization taken as the difference of cumulative cash flow statement amounts (C9).

| Quarter | Revenues | Income before income taxes | Net income attributable to CHS Inc. | EBITDA, derived | Basis and source |
| --- | --- | --- | --- | --- | --- |
| Q1 FY2026 (to 2025-11-30) | 8,864,104 | 272,188 | 260,483 | 480,375 | Reported, 10-Q Q1 page:5; EBITDA calculated |
| Q2 FY2026 (to 2026-02-28) | 8,353,791 | (164,977) | (147,052) | 51,408 | Reported, 10-Q Q2 page:5; EBITDA calculated |
| Q3 FY2026 (to 2026-05-31) | 11,582,089 | 282,213 | 267,366 | 497,255 | Reported, 10-Q Q3 page:5; EBITDA calculated |
| Q4 FY2026 (derived) | 10,431,233 | 739,295 | 715,106 | 940,459 | Derived: fiscal year less nine months, C9 |
| FY2026 | 39,231,217 | 1,128,719 | 1,095,903 | 1,969,497 | Reported, 10-K page:144 |
| Q1 FY2025 | 9,294,112 | 258,837 | 244,790 | 434,169 | Reported as comparative, 10-Q Q1 page:5; EBITDA calculated |
| Q2 FY2025 | 7,796,191 | (84,712) | (75,754) | 95,521 | Reported as comparative, 10-Q Q2 page:5; EBITDA calculated |
| Q3 FY2025 | 9,766,421 | 258,855 | 232,184 | 462,334 | Reported as comparative, 10-Q Q3 page:5; EBITDA calculated |
| Q4 FY2025 (derived) | 8,605,884 | 181,792 | 196,697 | 420,253 | Derived: fiscal year less nine months, C9 |
| FY2025 | 35,462,608 | 614,772 | 597,917 | 1,412,277 | Reported, 10-K page:144 |

Pretax earnings by quarter are seasonal; the company states "Our revenues and IBIT generally trend lower during the second fiscal quarter and increase in the third fiscal quarter." (10-K page:179). The fourth quarter of fiscal 2026 is the largest quarter of that year, and its pretax income of 739,295 exceeds the first nine months combined (389,424); in fiscal 2025 the fourth quarter (181,792) was below the first (258,837) and third (258,855). The sources give no discrete fourth-quarter commentary, so the drivers of that quarter are not attributed here.

### Segment view

Segments were recast from fiscal 2026 to a product-line model (Energy, Grains, Agronomy, and Corporate and Services); fiscal 2025 and 2024 below are the recast figures in the 10-K (10-K page:67, page:181). USD thousands.

| Segment | Pretax earnings FY2026 | FY2025 | FY2024 | Revenues FY2026 | D&A FY2026 | Capex incl. major maintenance FY2026 |
| --- | --- | --- | --- | --- | --- | --- |
| Energy | 554,590 | (19,015) | 406,658 | 11,359,955 | 361,500 | 211,468 |
| Grains | 127,378 | 44,003 | 254,570 | 21,584,138 | 158,123 | 191,217 |
| Agronomy | 354,640 | 375,283 | 258,577 | 6,099,599 | 65,127 | 51,787 |
| Corporate and Services | 92,111 | 214,501 | 177,982 | 187,525 | 92,395 | 77,045 |
| Total | 1,128,719 | 614,772 | 1,097,787 | 39,231,217 | 677,145 | 531,517 |

Agronomy earnings include CF Nitrogen and are largely equity income: the segment's equity income from investments is 413,829 against pretax earnings of 354,640 in fiscal 2026 (10-K page:181), so the segment's other lines net to a loss of 59,189 (C16). Corporate and Services holds the Ventura Foods and Ardent Mills equity investments (10-K page:179).

### Debt register at 2026-08-31

All instruments are obligations of CHS Inc. or its subsidiaries as the notes describe them; the debt note names no co-issuers or guarantors and the notes are printed as unsecured. The governing agreements are listed in the exhibit index but are not supplied (see gaps). USD thousands unless stated.

| Instrument | Rate | Outstanding 2026-08-31 | 2025-08-31 | Fiscal year due | Security | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Unsecured note, 58 million face | 4.69% | 58,000 | 58,000 | 2027 | Unsecured | 10-K page:164 |
| Unsecured note, 95 million face | 3.24% | 95,000 | 95,000 | 2028 | Unsecured | 10-K page:164 |
| Unsecured note, 95 million face | 4.74% | 95,000 | 95,000 | 2028 | Unsecured | 10-K page:164 |
| Unsecured note, 150 million face | 5.68% | 150,000 | 150,000 | 2030 | Unsecured | 10-K page:165 |
| Unsecured note, 100 million face | 3.48% | 100,000 | 100,000 | 2031 | Unsecured | 10-K page:165 |
| Unsecured note, 100 million face | 4.89% | 100,000 | 100,000 | 2031 | Unsecured | 10-K page:165 |
| Unsecured note, 150 million face | 5.84% | 150,000 | 150,000 | 2032 | Unsecured | 10-K page:165 |
| Unsecured note, 65 million face | 3.58% | 65,000 | 65,000 | 2033 | Unsecured | 10-K page:165 |
| Unsecured note, 100 million face | 4.71% | 100,000 | 100,000 | 2033 | Unsecured | 10-K page:165 |
| Unsecured note, 150 million face | 5.93% | 150,000 | 150,000 | 2034 | Unsecured | 10-K page:165 |
| Unsecured note, 115 million face | 3.73% | 115,000 | 115,000 | 2036 | Unsecured | 10-K page:165 |
| Unsecured note, 125 million face | 5.40% | 125,000 | 125,000 | 2036 | Unsecured | 10-K page:165 |
| Unsecured note, 150 million face | 6.05% | 150,000 | 150,000 | 2037 | Unsecured | 10-K page:165 |
| Unsecured note, 250 million face | 6.13% | 250,000 | 250,000 | 2039 | Unsecured | 10-K page:165 |
| Private placement debt subtotal (fourteen notes) | | 1,703,000 | 1,783,000 | | | 10-K page:165 |
| Unsecured term loan from cooperative and other banks (revolving term loan facility, readvanceable until 2026-10-29, then nonrevolving, payable 2029-10-29) | Variable, base rate plus margin | 300,000 | 0 (no balance) | 2030 | Unsecured | 10-K page:165 |
| Finance lease liabilities | 4.75% weighted average discount rate (4.24% at 2025-08-31) | 51,845 | 55,198 | Schedule in Note 19 | Lease | 10-K page:165, page:192 |
| Other notes and contracts | 3.9% to 4.0% | 1,312 | 1,529 | Not supplied | Not supplied | 10-K page:165 |
| Deferred financing costs | n/a | (3,434) | (3,894) | n/a | n/a | 10-K page:165 |
| Total long-term debt including current portion | | 2,052,723 | 1,835,833 | | | 10-K page:165 |
| Notes payable, other (international subsidiary lines of 182.5 million are outstanding; the note does not say which line they sit in) | 3.70% weighted average | 193,649 | 584,226 | Within 12 months | Not supplied | 10-K page:163, page:164 |
| CHS Capital notes payable | 4.02% weighted average | 255,353 | 568,231 | Within 12 months | Securitization is secured financing; surplus funds notes unsecured | 10-K page:163, page:164 |
| Total notes payable | | 449,002 | 1,152,457 | | | 10-K page:163 |

The 2025-08-31 column shows an 80,000 note at 4.82% that matured in fiscal 2026 and is not in the 2026 balance (10-K page:164); it is part of the 1,783,000 subtotal. The 175.0 million utilized under the Securitization Facility plus 80.4 million of surplus funds notes (10-K page:164) sum to 255.4 million, which agrees with CHS Capital notes payable of 255,353 within rounding; that agreement is our observation, not a company statement.

### Liquidity at 2026-08-31

| Source of liquidity | Amount | Status at 2026-08-31 | Expiry or term | Locator |
| --- | --- | --- | --- | --- |
| Cash and cash equivalents | 263,603 thousand | Unrestricted | n/a | 10-K page:144 |
| Restricted cash in other current assets | 123,217 thousand | Customer deposits for futures and options; not counted as liquidity | n/a | 10-K page:148 |
| Five-year unsecured revolving credit facility | 2.8 billion committed | No borrowings outstanding; letters of credit drawn on it not supplied | 2028-04-21 | 10-K page:163 |
| Revolving term loan facility | 300.0 million | Fully drawn, no undrawn amount | Reverts to nonrevolving term loan 2026-10-29, payable 2029-10-29 | 10-K page:165 |
| Securitization Facility | Committed portion up to 850.0 million; uncommitted portion up to 250.0 million; total availability 963.9 million | 175.0 million utilized | Extended to 2027-08-25 on 2026-08-26 | 10-K page:164 |
| Repurchase Facility | Maximum availability 250.0 million | No amount utilized | Extended to 2027-08-25 on 2026-08-26 | 10-K page:164 |
| Uncommitted bilateral facilities and international subsidiary lines | Not supplied (international lines outstanding 182.5 million) | Uncommitted | Not supplied | 10-K page:163, page:164 |

Management states that it believes "cash generated by operating and investing activities, along with available borrowing capacity under our credit facilities, will be sufficient to support our short-term (the next 12 months) and long-term (beyond the next 12 months) operations" (10-K page:76). The securitization and repurchase facilities expire within twelve months of the as-of date; the committed revolver does not (2028-04-21).

### Claims outside the debt figure

Total debt in C5 is notes payable plus long-term debt including current portion, so finance lease liabilities are inside it and everything below is outside it.

| Claim | Amount | Inside or outside total debt | Locator |
| --- | --- | --- | --- |
| Finance lease liabilities | 51,845 thousand | Inside (in long-term debt) | 10-K page:165 |
| Operating lease liabilities, present value | 237,487 thousand | Outside | 10-K page:192 |
| Future operating lease payments including interest | 251,234 thousand | Outside | 10-K page:77 |
| Purchase obligations, within one year / thereafter / total | 6,500,640 / 1,103,551 / 7,604,191 thousand | Outside; legally binding commitments | 10-K page:77 |
| Long-term unconditional purchase obligations (pipeline and grain handling take-or-pay) | 305,824 thousand total | Outside | 10-K page:190 |
| Guarantees of lines of credit and performance obligations of nonconsolidated companies | 110.4 million outstanding; covenants allow up to 1.1 billion | Outside; no liability recorded | 10-K page:190 |
| CHS Capital commitments to extend credit | 1.0 billion additional available credit to customers | Outside | 10-K page:190 |
| Pension and other postretirement funded status: qualified +4,041, nonqualified (32,742), other benefits (21,610) | Net shortfall 50,311 thousand (C10) | Outside | 10-K page:173 |
| Preferred stock, five Nasdaq-listed series, carrying value | 2,264,038 thousand; redemption values total 2,273.3 million (C11) | Outside debt; reported within equities | 10-K page:144, page:170 |
| Preferred dividends | 168,668 thousand paid per year; about 168.7 million expected in fiscal 2027 | Outside debt; fixed cumulative quarterly dividends | 10-K page:146, page:76 |
| Dividends and equity payable (patronage, redemptions, preferred dividend accrual) | 363,215 thousand at 2026-08-31 against 120,000 a year earlier | Outside; current liability | 10-K page:166 |
| Derivative liabilities | 546,562 thousand against 178,017 a year earlier | Outside; Note 15 derivative positions | 10-K page:166 |

No factoring, supply-chain finance, litigation or consent-decree funding obligation was found: the sources describe litigation as ordinary course with no material effect expected (10-K page:189), and a search for factoring and supply chain financing found no occurrence. CHS Capital sells notes receivable under a participation agreement without retained interests (10-K page:155).

### Covenants

The only maintenance disclosure is "Our notes payable and long-term debt are subject to various restrictive requirements for maintenance of minimum consolidated net worth and other financial ratios. We were in compliance with our debt covenants as of August 31, 2026." (10-K page:163), and management expects "continued covenant compliance" on its fiscal 2027 projections (10-K page:76). One covenant level is printed: bank covenants allow maximum guarantees of 1.1 billion, of which 110.4 million was outstanding (10-K page:190), leaving 989.6 million of that allowance (C12). Net worth and ratio levels, step-downs, the reported covenant figures and definitions are Not supplied: the agreements are not in the sources. Headroom is Not calculable, and none of the ratios in this module is a covenant ratio.

### Latest quarter and after

The latest period is fiscal Q4 2026 and the year to 2026-08-31, reported in the 10-K and release both dated November 4, 2026.

| Event or fact | Amount | Date | Locator |
| --- | --- | --- | --- |
| Securitization and repurchase facilities amended to extend terms to 2027-08-25 | Securitization 850.0 committed plus 250.0 uncommitted maximum; repurchase 250.0 maximum (USD millions) | Amended 2026-08-26 | 10-K page:164 |
| Revolving term loan: readvance period ends and balance reverts to a nonrevolving term loan payable 2029-10-29 | 300.0 million outstanding | 2026-10-29 (scheduled in the 10-K; occurrence not separately confirmed) | 10-K page:165 |
| Intended fiscal 2027 distribution to owners | 300 million: 150 million cash patronage and up to 150 million equity redemptions (release); 10-K adds 15.0 million of fiscal 2025 redemptions | Release 2026-11-04 | Release FY page:1; 10-K page:170 |
| Expected fiscal 2027 capital expenditures | 850.8 million against 463.3 million in fiscal 2026 | 10-K 2026-11-04 | 10-K page:76 |
| Expected fiscal 2027 major maintenance | 41.8 million against 68.3 million in fiscal 2026 | 10-K 2026-11-04 | 10-K page:76 |
| Proposed phosphate production facility in Louisiana, joint venture with OCP North America | Nearly 450 million; pending approvals; operational late 2028 or 2029 | Announced by 2026-11-04 | Release FY page:2; 10-K page:76 |
| Soybean processing facility, Evansville, Wisconsin | Approximately 700 million; pending approvals; operational late 2028 or 2029 | Announced by 2026-11-04 | Release FY page:2 |

### Definition risks

| Item | Issue | Effect |
| --- | --- | --- |
| EBITDA | Not reported by the company; derived here (C1). It adds back amortization of deferred major maintenance, which the company capitalizes and pays in investing cash flow (68,255 in fiscal 2026, 271,380 in fiscal 2025) | EBITDA exceeds a measure after major maintenance; free cash flow in C3 deducts it |
| Equity income | 569,231 of fiscal 2026 pretax income (10-K page:144) is equity income from investments; cash received is shown only net as "Equity income from investments, net of distributions received" 25,371 (10-K page:146) | EBITDA and operating EBITDA bracket the range; the second excludes equity income |
| Total debt | Includes CHS Capital funding (255,353), international subsidiary lines and finance leases, and is net of deferred financing costs; CHS Capital funds a notes receivable book (investing outflow of 332,609 in fiscal 2026) | Leverage on a basis excluding the finance arm is Not calculable from the sources |
| Capital expenditures | Management discussion quotes 463.3 million for fiscal 2026 (acquisition of property, plant and equipment); the segment note total of 531,517 includes major maintenance (10-K page:181) | The two totals reconcile: 463,262 plus 68,255 equals 531,517 (C13) |
| Segments | Recast from fiscal 2026; fiscal 2025 and 2024 are the recast figures | Do not compare with pre-recast fiscal 2025 reports, which are not in the sources |
| Fiscal 2027 redemptions | The release says up to 150 million; the 10-K authorizes 150.0 million for fiscal 2026 plus an additional 15.0 million for fiscal 2025, and the equity statement carries 165,000 of estimated redemptions | Use the filing figure of 165,000 for the redemption accrual |

### Readiness for downstream modules

| Consumer | View | Reason |
| --- | --- | --- |
| CP-1A business and transaction | Limited | Segment, operating model and project facts are present; transaction terms for the announced projects are Not supplied |
| CP-2 credit view | Limited | Debt register, liquidity, maturities and cash flow support a statement-based view; covenant levels, letters of credit, ratings and fiscal 2024 debt are Not supplied |
| CP-5 evidence trace | Sufficient for located figures | Every figure carries a page locator; derived figures are labelled and shown in the calculations |

### Consistency with the CP-0 handoff

CP-0 carried an open item that the management discussion capital expenditure total and the segment note total differ; this module resolves it: the segment total includes major maintenance (C13). CP-0 noted that no discrete fourth quarter is reported; this module derives it from the fiscal year and nine-month amounts and labels it derived (C9). CP-0 recorded that letters of credit, EBITDA and ratings were searched for and not found; that stands, and the same searches were not repeated with different results. CP-0 flagged the fiscal 2027 redemption difference between the release and the 10-K; it is carried above, with the filing figure used. No CP-0 statement is corrected by this module.

## Calculations

All inputs are USD thousands from the cited locators unless stated; ratios are rounded to two decimals.

| Id | Calculation | Inputs | Result |
| --- | --- | --- | --- |
| C1 | EBITDA, derived = income before income taxes + interest expense + D&A | FY2026: 1,128,719 + 163,633 + 677,145; FY2025: 614,772 + 146,079 + 651,426; FY2024: 1,097,787 + 104,064 + 569,891 | 1,969,497; 1,412,277; 1,771,742 |
| C2 | Operating EBITDA, derived = operating earnings + D&A | FY2026: 591,882 + 677,145; FY2025: 90,755 + 651,426; FY2024: 584,358 + 569,891 | 1,269,027; 742,181; 1,154,249 |
| C3 | Free cash flow after major maintenance = operating cash flow - acquisition of PP&E - major maintenance | FY2026: 1,584,009 - 463,262 - 68,255; FY2025: 635,787 - 728,575 - 271,380; FY2024: 1,272,880 - 808,763 - 22,748 | 1,052,492; (364,168); 441,369 |
| C4 | C3 less preferred dividends, cash patronage and redemptions | FY2026: 1,052,492 - 168,668 - 30,000 - 100,433; FY2025: (364,168) - 168,668 - 300,358 - 287,683; FY2024: 441,369 - 168,668 - 366,012 - 355,925 | 753,391; (1,120,877); (449,236) |
| C5 | Total debt = notes payable + long-term debt including current portion; net debt = total debt - cash and cash equivalents; ratios over C1 or C2 | FY2026: 449,002 + 2,052,723 = 2,501,725; less 263,603 = 2,238,122; FY2025: 1,152,457 + 1,835,833 = 2,988,290; less 327,826 = 2,660,464 | Total debt / EBITDA 1.27 and 2.12; net 1.14 and 1.88; total debt / operating EBITDA 1.97 and 4.03 |
| C6 | Cover = EBITDA / cash paid for interest | 1,969,497 / 167,057; 1,412,277 / 147,583; 1,771,742 / 100,542; operating: 1,269,027 / 167,057; 742,181 / 147,583; 1,154,249 / 100,542 | 11.79; 9.57; 17.62; operating 7.60; 5.03; 11.48 |
| C7 | Undrawn revolver = committed amount - borrowings | FY2026: 2,800.0 - 0 (no borrowings); FY2025: 2,800.0 - 180.0 (USD millions) | 2,800.0; 2,620.0 |
| C8 | Debt / (debt + total equities) | 2,501,725 / (2,501,725 + 11,644,845); 2,988,290 / (2,988,290 + 11,080,174) | 17.7%; 21.2% |
| C9 | Quarterly derivation: Q4 = fiscal year - nine months; quarterly D&A = difference of cumulative cash flow D&A; quarterly EBITDA = pretax + interest + D&A | FY2026 nine months: revenues 28,799,984, pretax 389,424, net income attributable 380,797, interest 130,833, D&A 508,781; Q1 D&A 170,836, six-month D&A 343,464 so Q2 172,628 and Q3 165,317; Q4: revenues 39,231,217 - 28,799,984 = 10,431,233; pretax 1,128,719 - 389,424 = 739,295; net income attributable 1,095,903 - 380,797 = 715,106; interest 163,633 - 130,833 = 32,800; D&A 677,145 - 508,781 = 168,364; prior year: nine months revenues 26,856,724, pretax 432,980, attributable 401,220, interest 96,962, D&A 462,082; Q1 D&A 147,684, six-month 302,712 | Q4 FY2026 EBITDA 739,295 + 32,800 + 168,364 = 940,459; Q4 FY2025 EBITDA 181,792 + 49,117 + 189,344 = 420,253; quarterly EBITDA sums equal the annual C1 amounts; second-half pretax 282,213 + 739,295 = 1,021,508; first-half pretax 272,188 + (164,977) = 107,211 |
| C10 | Net pension and other postretirement shortfall | 4,041 - 32,742 - 21,610 | (50,311) |
| C11 | Preferred redemption values in USD millions | 306.8 + 536.5 + 420.0 + 492.5 + 517.5 | 2,273.3 |
| C12 | Remaining guarantee allowance | 1.1 billion - 110.4 million = 1,100.0 - 110.4 (USD millions) | 989.6 |
| C13 | Capital expenditure bridge | 463,262 + 68,255 | 531,517 |
| C14 | Interim last-twelve-months EBITDA and leverage | LTM = FY2025 EBITDA 1,412,277 + current-year-to-date EBITDA - prior-year-to-date EBITDA. May 2026: nine months 389,424 + 130,833 + 508,781 = 1,029,038 less 432,980 + 96,962 + 462,082 = 992,024, so 1,412,277 + 1,029,038 - 992,024 = 1,449,291. Total debt at 2026-05-31: 1,589,756 + 149,663 + 1,983,919 = 3,723,338. Also November 2025: LTM 1,458,483, debt 1,859,159 + 89,882 + 1,740,200 = 3,689,241. February 2026: LTM 1,414,370, debt 1,995,108 + 149,064 + 1,983,616 = 4,127,788 | Total debt / LTM EBITDA: 2.53 at 2025-11-30; 2.92 at 2026-02-28; 2.57 at 2026-05-31; compare 1.27 at 2026-08-31 |
| C15 | Maturity ladder reconciliation | 58,562 + 190,600 + 150 + 450,000 + 200,000 + 1,105,000 = 2,004,312; plus finance leases 51,845 less deferred financing costs 3,434 = 2,052,723; plus notes payable 449,002 = 2,501,725 | Agrees with the long-term debt balance and C5 total debt |
| C16 | Segment improvement and Agronomy equity income | Group: 1,128,719 - 614,772 = 513,947; Energy: 554,590 - (-19,015) = 573,605; Agronomy: 354,640 - 375,283 = -20,643; Corporate and Services: 92,111 - 214,501 = -122,390; Grains: 127,378 - 44,003 = 83,375; Agronomy pretax 354,640 - equity income 413,829 | Energy 573,605 exceeds group 513,947; Agronomy excluding equity income (59,189) |

Interim leverage points of C14 use balance sheet debt at each quarter end and derived LTM EBITDA; they are not covenant measures.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Credit agreements, note purchase agreements and amendments not supplied (listed at 10-K page:133 and page:134) | Co-issuers, guarantors, security, covenant levels and definitions, events of default and baskets are Not supplied | Obtain the agreements before any covenant or ranking work |
| Covenant levels and reported covenant figures not printed | Headroom Not calculable | Obtain from the agreements or a compliance certificate |
| Letters of credit drawn on the revolver, factoring and supply-chain finance: searched all seven sources, no occurrence | Undrawn committed revolver of 2,800.0 is gross of any letters of credit | Obtain facility utilization detail |
| Debt and revolver balances at 2024-08-31 not in the sources | Fiscal 2024 leverage and undrawn liquidity Not supplied | Obtain the fiscal 2024 annual report if a three-year leverage series is wanted |
| No company-reported EBITDA or adjusted EBITDA | All EBITDA and leverage are derived (C1, C2) and not comparable to lender-defined measures | Obtain management bridge or covenant EBITDA definition |
| No discrete fourth-quarter statements; Q4 is derived (C9) | Fourth-quarter detail beyond the derived lines (segments, cash flow) is Not supplied | Treat as derived; no quarterly segment release for Q4 is supplied |
| Interim intra-quarter debt peaks not available | Quarter-end balances only; daily or monthly peaks Not supplied | Request borrowing base or monthly debt data |
| Uncommitted bilateral facilities and the committed share of securitization capacity not separable | Liquidity excludes them | Obtain facility terms |
| Revolving term loan reversion on 2026-10-29 not confirmed by a later document | Treated as scheduled per the 10-K | Check the next quarterly report |
| Ratings, market prices and peer data not supplied | No market or rating view in this module | Out of scope for this module |
| Prior-year segment data is recast; original fiscal 2025 report not in the sources | No pre-recast comparison | Use recast data only |

## Next module

Proceed to CP-1A with these inputs: the segment table and recast caveat, the Q4 FY2026 derived strength, the announced phosphate and soybean projects with their pending approvals, the fiscal 2027 capital expenditure expectation of 850.8 million against 463.3 million, and the owner distribution plan. CP-2 should carry the derived-EBITDA caveat, the seasonal debt profile (C14), the near-term facility expiry of 2027-08-25, and the covenant and letter-of-credit gaps.
