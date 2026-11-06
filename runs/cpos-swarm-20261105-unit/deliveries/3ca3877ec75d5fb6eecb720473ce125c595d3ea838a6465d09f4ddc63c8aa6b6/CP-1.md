## Request

Issuer: Uniti Group Inc. (issuer id unit; Nasdaq ticker UNIT). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, in millions as the filings print. Current period named by the context: Q2 2026 (quarter ended 2026-06-30). Prior period named by the context: FY2025.

Task for this module: build the financial base for Uniti Group Inc. from the supplied filings and releases: reported income statement, cash flow and balance sheet figures, Adjusted EBITDA, leverage, interest cover, liquidity and the debt maturity profile, with explicit perimeter, period and definition limits. The upstream readiness handoff is applied: the 2025-08-01 reverse merger changes the perimeter, no executed debt documents are supplied, and nothing after the 2026-07-30 filings is supplied. Leverage, cover and liquidity are computed from printed inputs and shown in `## Calculations`. This module gives no investment opinion.

## Sources

Each issuer file is one JSONL text extraction of an SEC filing. The locator `page:N` is the extraction chunk, not the printed page.

### Issuer sources relied on

| Source name | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_unit-20251231.htm.jsonl | 6d67619ba1ab3647c20a79710ac6373101e1f3efd1454ad58308edf1101a7a6b | Audited FY2025 statements (page:100-103), Adjusted EBITDA reconciliation (page:88), cash flow supplemental (page:192), revolver availability (page:77, page:141, page:143), leases (page:159), pension (page:172) |
| 10-Q_2025-09-30_unit-20250930.htm.jsonl | 5887e391d2d0fd28ff7625b79ed82dcf62027435a26c54f6cbb097f48f8f2e90 | Q3 2025 Adjusted EBITDA (page:120) for the quarterly cross-check only |
| 10-Q_2026-03-31_unit-20260331.htm.jsonl | 6eef1c3a3881ef793ddfc9610c4d46208d57c3bb26c5a88a18ed1115bb75d5ba | Q1 2026 statements (page:4-6), interest paid (page:12), debt (page:19), revolvers (page:23, page:25), liquidity (page:73), Adjusted EBITDA reconciliation (page:79) |
| 10-Q_2026-06-30_unit-20260630.htm.jsonl | 44ae41cd731221c3fab785c468962d8927f45d4ed20722ebe4d9e689ea9bcd05 | Q2 and six-month 2026 statements (page:4-6), interest paid (page:13), debt table (page:20-21), credit agreements (page:23-25), ABS (page:26-30), segments (page:47-49), subsequent events (page:52-54, page:63), liquidity (page:83), Adjusted EBITDA reconciliation (page:91) |
| EX-99.1_2026-03-02_unit-ex991202510xk.htm.jsonl | c7190cfa9cb627d04b3e648821ebf4356c56f99434b32385548463e0d9accab6 | Fourth quarter 2025 revenue, Adjusted EBITDA and net loss (page:1) |
| EX-99.1_2026-05-11_unit-ex9911q26.htm.jsonl | cfd5a9da978c996627652ac9d3c7077c0533d727405c7b27dfe93c7e85d28fc5 | Q1 2026 revenue, Adjusted EBITDA and net loss, matched against the 10-Q (page:1) |
| EX-99.1_2026-07-30_unit-ex9912q26.htm.jsonl | 1d9925874068c008696dd366506144e0d697bf35f0c978f5473bf3052738ff6f | Q2 2026 headline figures, financing transactions and 2026 outlook (page:1-2) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | e531a4ec67bdeec3bf2b02e8047c90f4c69262abee202a8c1e2071ff24adf370 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 013c310c8396f81ac9f077f177c9c4e522274d65b9d75cc140acddd2c5a45803 | Source readiness: perimeter change at 2025-08-01, no executed debt documents, nothing after 2026-07-30 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Uniti is highly leveraged and loss-making: total debt was 7.16x trailing Adjusted EBITDA at 2026-06-30, cash interest cover was 1.94x, and liquidity was 1,447.0 million. Heavy fiber capital spending is outspending operating cash flow. | Medium | Adjusted EBITDA is a company measure and trailing figures mix a smaller pre-merger company with the combined company. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt principal was 10,680.6 million at 2026-06-30, up from 9,540.5 million at 2025-12-31, as new asset-backed notes replaced revolver and term loan borrowings. | More debt is secured on subsidiary assets that sit outside the main credit group, which can matter for unsecured holders. | High |
| Operating cash flow was 339.4 million for the first half of 2026, against capital expenditures of 799.2 million. | The build-out is funded by debt issuance rather than internal cash flow. | High |
| Debt maturities are light in 2027 to 2028 and heavy from 2031, with 3,410.1 million due in 2031 and 2,595.0 million in 2032. | Near-term refinancing need is small; the later wall depends on market access. | Medium |
| A further 1,140.7 million of asset-backed notes was issued on 2026-07-15, after the quarter, with up to 500.0 million of secured debt repayment planned. | Reported quarter-end leverage does not reflect these post-quarter changes. | High |

### Financial base view

The financial base is usable with limitations. Reported figures for Q1 2026, Q2 2026 and the first half of 2026 come from filed statements on the combined-company perimeter and tie to the releases. FY2025 holds the combined company only from 2025-08-01, so trailing and annual metrics are not like-for-like and are labelled that way. On the filed numbers, total debt principal of 10,680.6 million stood at 7.16x trailing-twelve-month Adjusted EBITDA of 1,492.2 million, and 6.75x after deducting 608.9 million of unrestricted cash. Trailing Adjusted EBITDA covered trailing cash interest paid of 768.6 million 1.94 times. Interest expense, net was 383.9 million in the first half of 2026 against GAAP operating income of 143.1 million, so the company reports a net loss of 226.2 million for the half. Operating cash flow of 339.4 million fell short of capital expenditures of 799.2 million, and the gap was funded by debt: 2,072.6 million of issuance against 930.0 million of repayments. Liquidity at 2026-06-30 was cash of 608.9 million plus 838.1 million of revolver availability. Four limits bind every metric: Adjusted EBITDA is a management measure defined to resemble debt agreement terms but not tested here; the trailing period includes July 2025 without Windstream; covenant levels are not printed; and quarter-end debt does not include the July 2026 asset-backed issue or the planned repayments.

### Perimeter and period basis

- Reporting entity: Uniti Group Inc. and subsidiaries, consolidated. Old Uniti is the accounting acquirer, so periods before 2025-08-01 show Old Uniti only and later periods show the combined company (Q2 10-Q page:11, page:19).
- FY2025: audited, with PricewaterhouseCoopers LLP's opinion (10-K page:95-99). It contains seven months of Old Uniti and five months of the combined company.
- 2026 quarters: unaudited, combined company. Their comparatives are Old Uniti only and recast for the reclassifications described in the Q2 10-Q (page:11-12). Year-on-year changes are therefore not organic. The Q2 10-Q states that Windstream contributed 795.9 million of the quarter's 909.7 million revenue (page:63).
- FY2025 net income of 1,304.7 million includes a gain on settlement of preexisting relationships of 1,683.9 million (10-K page:101, page:88). The gain is excluded from Adjusted EBITDA. FY2025 reported EBITDA of 2,620.6 million (page:88) includes it and must not be used as a leverage denominator.
- Fiber Infrastructure revenue fell from 300.7 million in Q2 2025 to 200.3 million of external revenue in Q2 2026 because Windstream lease revenue ended on the merger; the filing attributes the decrease to the settlement of the preexisting leasing relationships (Q2 10-Q page:47, page:70).

### Financials and credit metrics

| Metric (USD millions) | FY2025 | Q1 2026 | Q2 2026 | H1 2026 | Basis, source and limitation |
| --- | --- | --- | --- | --- | --- |
| Total revenues and sales | 2,234.5 | 987.5 | 909.7 | 1,897.2 | Reported. 10-K page:101; Q1 10-Q page:4; Q2 10-Q page:4. FY2025 holds five months of Windstream. Q1 and H1 include 85.5 of incremental sales revenue from a dark fiber IRU with a hyperscaler (Q2 10-Q page:63) |
| EBITDA | 2,620.6 | 407.2 | 345.9 | 753.1 | Company reconciliation. 10-K page:88; Q1 10-Q page:79; Q2 10-Q page:91. FY2025 includes the 1,683.9 gain |
| Adjusted EBITDA | 1,173.8 | 441.6 | 357.1 | 798.7 | Company non-GAAP measure; same sources. Adds back stock-based compensation, transaction related and other costs and other items |
| Operating income | 262.0 | 110.9 | 32.2 | 143.1 | Reported. 10-K page:101; Q1 10-Q page:4; Q2 10-Q page:4 |
| Depreciation and amortization | 666.6 | 289.8 | 305.9 | 595.7 | Reported; same pages |
| Interest expense, net | 602.8 | 188.3 | 195.6 | 383.9 | Reported; includes non-cash amortization of financing costs (Q2 10-Q page:6: 5.4 for H1) |
| Net income (loss) | 1,304.7 | (70.3) | (155.9) | (226.2) | Reported. FY2025 includes the 1,683.9 gain |
| Net cash from operating activities | 350.2 | 260.9 | 78.5 | 339.4 | Reported for FY2025, Q1 and H1; Q2 is H1 less Q1 (calculated). 10-K page:102; Q1 10-Q page:6; Q2 10-Q page:6 |
| Capital expenditures | 787.8 | 349.2 | 450.0 | 799.2 | Reported cash flow line; Q2 also in segment table (Q2 10-Q page:48). Excludes grant-funded capital expenditures of 34.8 in H1 |
| Interest paid, net of capitalized | 660.7 | 138.8 | 229.3 | 368.1 | Reported for FY2025, Q1 and H1 (10-K page:192; Q1 10-Q page:12; Q2 10-Q page:13); Q2 is H1 less Q1 (calculated). Coupon timing makes single quarters uneven |
| Cash and cash equivalents (period end) | 53.5 | 982.6 | 608.9 | 608.9 | Reported unrestricted cash. Restricted cash is 80.6, 149.3 and 123.8 and is excluded |
| Total debt principal (period end) | 9,540.5 | 10,683.1 | 10,680.6 | 10,680.6 | Reported total principal amount. 10-K page:139; Q1 10-Q page:19; Q2 10-Q page:20 |
| Total debt / Adjusted EBITDA (x, LTM) | 8.13 | 7.75 | 7.16 | 7.16 | Calculated; see Calculations. LTM mixes perimeters |
| Net debt / Adjusted EBITDA (x, LTM) | 8.08 | 7.04 | 6.75 | 6.75 | Calculated; net of unrestricted cash only |
| Adjusted EBITDA / cash interest paid (x, LTM) | 1.78 | 2.34 | 1.94 | 1.94 | Calculated; FY2025 uses the year, others the trailing twelve months |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 8.13 | 8.08 | x | Total debt principal 9,540.5 and cash 53.5 over FY2025 Adjusted EBITDA 1,173.8, which holds five months of Windstream; the ratio overstates leverage on a combined basis. Company Adjusted EBITDA, not covenant EBITDA |
| LTM Q1 2026 | 7.75 | 7.04 | x | Debt principal 10,683.1 and cash 982.6 over LTM Adjusted EBITDA 1,377.6 (FY2025 less Q1 2025 plus Q1 2026). Includes two pre-merger Old Uniti months in the window; Q1 2026 holds IRU sales revenue |
| LTM Q2 2026 | 7.16 | 6.75 | x | Debt principal 10,680.6 and cash 608.9 over LTM Adjusted EBITDA 1,492.2 (FY2025 less H1 2025 plus H1 2026). July 2025 is Old Uniti only; excludes the July 2026 asset-backed issue and planned repayments. Excludes preferred stock, leases and pension |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 1.78 | x | Adjusted EBITDA 1,173.8 over interest paid 660.7; EBITDA holds five months of Windstream and interest paid reflects the debt as it stood during the year |
| LTM Q1 2026 | 2.34 | x | LTM Adjusted EBITDA 1,377.6 over LTM interest paid 587.7 (660.7 less 211.8 plus 138.8); coupon timing in Q1 2025 and Q1 2026 differs |
| LTM Q2 2026 | 1.94 | x | LTM Adjusted EBITDA 1,492.2 over LTM interest paid 768.6 (660.7 less 260.2 plus 368.1). Not a covenant test; interest expense, net would give a different ratio |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 2025-12-31 | 53.5 | 542.1 | US$m | Unrestricted cash; revolver availability is 499.7 (Uniti Revolver) plus 42.4 (Windstream Revolver) after 315.0 drawn and letters of credit of 117.6 (10-K page:141, page:143) |
| 2026-03-31 | 982.6 | 862.0 | US$m | Availability is 499.7 plus 362.3 after letters of credit of 112.7 (Q1 10-Q page:23, page:25, page:73); cash includes proceeds of the Kinetic ABS 2026-1 notes issued 2026-01-30 |
| 2026-06-30 | 608.9 | 838.1 | US$m | Availability is 499.7 plus 338.4 after letters of credit of 136.6 on the Windstream Revolver (Q2 10-Q page:23-24, page:83). Excludes restricted cash of 123.8 and the July 2026 asset-backed proceeds; the Windstream Revolver commitment steps down from 475.0 to 425.0 after 2027-01-23 and both revolvers mature 2027-12-30 |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remaining 2026 | Not supplied: no instrument matures in 2026; only term loan amortization is scheduled and the filing prints just the current portion of 10.0 | US$m | Amortization is 0.25 percent of the 1,000.0 initial 2025 Term Loan principal per quarter (Q2 10-Q page:25); no maturity table is printed |
| 2027 | 306.5 | US$m | 7.50% convertible senior notes due 2027-12-01. Both revolvers mature 2027-12-30 with nothing drawn at 2026-06-30 |
| 2028 | 570.0 | US$m | 4.75% senior secured notes due 2028-04-15 |
| 2029 | 1,110.0 | US$m | 6.50% senior unsecured notes due 2029-02-15 |
| 2030 | 1,289.0 | US$m | 6.00% senior unsecured notes 700.0 due 2030-01-15 plus Fiber Infrastructure ABS Series 2025-1 notes 589.0 due 2030-04-01 |
| 2031 | 3,410.1 | US$m | 8.25% senior secured notes 2,200.0 due 2031-10-01, Series 2025-2 Fiber ABS notes 250.0 due 2031-01-20 and Kinetic ABS 2026-1 notes 960.1 due 2031-02-01 |
| 2032 | 2,595.0 | US$m | 8.625% senior unsecured notes 1,600.0 due 2032-06-15 plus 2025 Term Loan 995.0 due 2032-10-06 |
| 2033 | 1,400.0 | US$m | 7.50% senior secured notes due 2033-10-15. The Kinetic ABS 2026-2 notes issued 2026-07-15 (anticipated repayment June 2033) are not included |

### Income statement and operating drivers

- Revenue: Q2 2026 revenue was 909.7 million and Q1 2026 987.5 million. The Q1 figure includes the IRU sales revenue of 85.5 million for the first half; Q1 sales revenues were 98.5 million and Q2 56.8 million (Q1 10-Q page:4; Q2 10-Q page:4, page:63). Service revenues were 889.0 million in Q1 and 852.9 million in Q2, which is lower in Q2.
- Margins: Q2 2026 Adjusted EBITDA of 357.1 million was below Q1 2026 at 441.6 million, and the 2026 outlook issued 2026-07-30 is Adjusted EBITDA of 1,450 to 1,500 million, interest expense, net of 805 million and a net loss of 480 to 530 million (release page:2). That outlook is a management forward-looking statement. First-half Adjusted EBITDA of 798.7 million implies a second-half range of 651.3 to 701.3 million to reach it (calculated).
- Segments, Q2 2026 (Q2 10-Q page:47-49): Kinetic external revenue 528.2 and contribution margin 228.4; Fiber Infrastructure external revenue 200.3 and contribution margin 121.8; Uniti Solutions external revenue 181.2 and contribution margin 91.8; total segment contribution margin 442.0. Corporate and shared operating expenses were 86.7. Segment contribution margin is not Adjusted EBITDA.
- Kinetic fiber consumer broadband customers were 602.8 thousand and DSL customers 357.6 thousand at 2026-06-30 (page:70).

### Cash flow and funding

- H1 2026: operating cash flow 339.4; capital expenditures 799.2, of which Kinetic 602.8 (page:6, page:48). Operating cash flow less capital expenditures is negative 459.8 (calculated). Government grants were a separate offset: capital expenditures funded by grants 34.8 and grant funds received 11.9.
- Financing: debt issuance 2,072.6, repayments 930.0, financing costs 39.7 and preferred dividends paid 16.7, net financing inflow 1,077.8 (page:6). Cash plus restricted cash rose from 134.1 to 732.7.
- FY2025: operating cash flow 350.2 and capital expenditures 787.8, a negative 437.6 (calculated) (10-K page:102-103).

### Capital structure and debt detail

At 2026-06-30 (Q2 10-Q page:20-22): Uniti Revolver 500.0 commitment (undrawn); Windstream Revolver (undrawn); 2025 Term Loan 995.0; 4.75% secured notes 570.0 due 2028; 8.25% secured notes 2,200.0 due 2031; 7.50% secured notes 1,400.0 due 2033; 6.50% unsecured notes 1,110.0 due 2029; 6.00% unsecured notes 700.0 due 2030; 8.625% unsecured notes 1,600.0 due 2032; 7.50% convertible notes 306.5 due 2027; Fiber Infrastructure ABS notes 839.0 (six classes, 2030 and 2031); Kinetic ABS 2026-1 notes 960.1 due 2031. Principal totals 10,680.6; carrying value is 10,636.6 long-term plus 10.0 current after 34.0 of unamortized discount and costs.

- Change in H1 2026: the Windstream Term Loan of 500.0 was repaid in full on 2026-02-04 and 315.0 of Windstream Revolver borrowings repaid, using the proceeds of 1,000.0 of new 8.625% notes (principal rose from 600.0 to 1,600.0) and the 960.1 Kinetic ABS 2026-1 notes (page:21, page:24, page:26-27).
- Secured and structurally senior debt: the credit facilities and secured notes share first-priority collateral under an intercreditor agreement (page:25). The ABS notes are issued by bankruptcy-remote unrestricted subsidiaries (page:50), so their assets and cash flows sit outside the restricted group that supports the other debt. At 2026-06-30 unrestricted subsidiaries held total assets of 2,007.7 of 12,980.9 consolidated (page:50).
- Floating rate: only the 2025 Term Loan (995.0) and any revolver borrowings are variable; the Q2 10-Q reports a 7.65% weighted average rate on the term loan for the quarter (page:25) and four pay-fixed swaps: one of 200.0 assumed in the merger and three of 150.0 each (450.0) after a partial termination on 2026-01-28, 650.0 of notional in all against 995.0 of term loan (page:32, calculated sum).

### Claims outside the debt figure

| Claim | Amount and date | Inside the debt figure? | Source |
| --- | --- | --- | --- |
| Preferred stock issued to Windstream equityholders | Liquidation preference 575.0; 11% dividend for the first six years; dividends declared 31.2 in H1 2026, 16.7 paid in cash in Q2 | No; equity | Q2 10-Q page:5, page:10; page:6 |
| Operating lease obligations | 117.4 current plus 329.1 noncurrent at 2026-06-30 | No | Q2 10-Q page:5 |
| Finance lease obligations | 57.1 at 2025-12-31; not separately shown on the balance sheet | No | 10-K page:159 |
| Pension deficit | Funded status (89.5) at 2025-12-31; minimum employer contributions of 20.6 in 2026 | No | 10-K page:172; Q2 10-Q page:41 |
| Deferred revenue | 256.3 current plus 390.0 noncurrent at 2026-06-30 | No; largely customer prepayments, a non-cash obligation to deliver service | Q2 10-Q page:5 |
| Letters of credit | 136.9 at 2026-06-30, of which 136.6 under the Windstream Revolver | No; reduce revolver availability | Q2 10-Q page:23-24, page:83 |
| Warrants | About 17.6 million warrants at 0.01 dollar exercise price issued to Windstream equityholders | No; equity | Q2 10-Q page:10 |
| Accrued interest | 148.4 at 2026-06-30 | No; working capital | Q2 10-Q page:5 |

### Liquidity and covenants

Liquidity at 2026-06-30 was 1,447.0, from cash of 608.9 and availability of 838.1 (calculated; page:83). Both revolvers mature 2027-12-30, 18 months after the balance sheet date, so neither is current yet; the Windstream Revolver commitment steps down to 425.0 after 2027-01-23 (page:24). Cash at quarter end excludes the July 2026 asset-backed proceeds: of the 1,140.7 raised, 500.0 is planned for repayment of secured debt and the balance for reinvestment (page:52).

Covenants: the debt agreements contain financial ratio covenants and the company reports compliance with all debt covenants at 2026-06-30 (page:22). Maintenance test names, levels, step-downs and reported ratios are Not supplied; the revolver margins and the term loan prepayment step-downs refer to leverage ratios whose levels are not printed (page:23-25). The company states that Adjusted EBITDA is calculated similarly to defined terms in its debt agreements (page:90-91). Headroom is therefore Not calculable.

### Subsequent events

All within the cutoff. Kinetic ABS Series 2026-2 notes of 1,140.7 (805.2 class A-2 at 5.834%, 134.2 class B at 6.224%, 201.3 class C at 7.536%) were issued on 2026-07-15 with anticipated repayment in June 2033; proceeds bought assets from subsidiary guarantors of the company's senior debt (Q2 10-Q page:52). A term loan prepayment offer of up to 167.8 on the 2025 Term Loan was issued 2026-07-23 and 19.8 was repaid on 2026-07-30; asset sale offers for up to 332.2 of the 4.75% and 7.50% secured notes opened 2026-07-23 (page:63; release page:2). The release gives an expiry of 2026-08-20 for the asset sale offers; their outcome is Not supplied. Pro forma for the prepayment of 19.8 and full use of 500.0, the figures above would change, but the amounts taken up are not supplied, so no pro forma leverage is computed.

### Definition and data-quality notes

- Adjusted EBITDA and EBITDA are company non-GAAP measures reconciled in each filing; the company excludes stock-based compensation, transaction related and other costs, the 1,683.9 gain and loss or gain on asset retirements (10-K page:88; Q2 10-Q page:91). They are not the covenant EBITDA of the executed agreements, which are not supplied.
- Quarterly cross-check: Q3 2025 Adjusted EBITDA 327.8 (Q3 2025 10-Q page:120) plus Q4 2025 365.6 (release page:1) plus Q1 2026 441.6 plus Q2 2026 357.1 equals 1,492.1, against 1,492.2 from the year-based method. The 0.1 difference is rounding in the printed figures.
- Releases match the filings: Q2 2026 net loss 155.9 and Adjusted EBITDA 357.1; Q1 2026 revenue 987.5 and Adjusted EBITDA 441.6. No conflict found.
- The FY2025 10-K also gives an unaudited pro forma table as if the merger occurred on 2024-01-01 (page:135). Pro forma Adjusted EBITDA is not printed in the sources read, so no pro forma leverage is computed.

## Calculations

All amounts in USD millions. Inputs are printed figures at the cited locators; results are calculated.

| Calculation | Formula and inputs | Result |
| --- | --- | --- |
| LTM Adjusted EBITDA, Q2 2026 | 1,173.8 (FY2025) - 480.3 (H1 2025) + 798.7 (H1 2026); 10-K page:88, Q2 10-Q page:91 | 1,492.2 |
| LTM Adjusted EBITDA, Q1 2026 | 1,173.8 - 237.8 (Q1 2025) + 441.6 (Q1 2026); Q1 10-Q page:79 | 1,377.6 |
| LTM cross-check | 327.8 + 365.6 + 441.6 + 357.1 | 1,492.1, within 0.1 of 1,492.2 |
| Total debt / Adjusted EBITDA, Q2 2026 | 10,680.6 / 1,492.2 | 7.16x |
| Net debt, Q2 2026 | 10,680.6 - 608.9 | 10,071.7 |
| Net debt / Adjusted EBITDA, Q2 2026 | 10,071.7 / 1,492.2 | 6.75x |
| Total debt / Adjusted EBITDA, Q1 2026 | 10,683.1 / 1,377.6 | 7.75x |
| Net debt / Adjusted EBITDA, Q1 2026 | (10,683.1 - 982.6) = 9,700.5; 9,700.5 / 1,377.6 | 7.04x |
| Total debt / Adjusted EBITDA, FY2025 | 9,540.5 / 1,173.8 | 8.13x |
| Net debt / Adjusted EBITDA, FY2025 | (9,540.5 - 53.5) = 9,487.0; 9,487.0 / 1,173.8 | 8.08x |
| Q2 2026 interest paid | 368.1 (H1) - 138.8 (Q1) | 229.3 |
| LTM interest paid, Q2 2026 | 660.7 - 260.2 + 368.1 | 768.6 |
| LTM interest paid, Q1 2026 | 660.7 - 211.8 + 138.8 | 587.7 |
| Cash interest cover, Q2 2026 LTM | 1,492.2 / 768.6 | 1.94x |
| Cash interest cover, Q1 2026 LTM | 1,377.6 / 587.7 | 2.34x |
| Cash interest cover, FY2025 | 1,173.8 / 660.7 | 1.78x |
| Q2 2026 operating cash flow | 339.4 - 260.9 | 78.5 |
| Operating cash flow less capital expenditures, H1 2026 | 339.4 - 799.2 | -459.8 |
| Operating cash flow less capital expenditures, FY2025 | 350.2 - 787.8 | -437.6 |
| Liquidity, 2026-06-30 | 608.9 + (499.7 + 338.4 = 838.1) | 1,447.0 |
| Liquidity, 2026-03-31 | 982.6 + (499.7 + 362.3 = 862.0) | 1,844.6 |
| Liquidity, 2025-12-31 | 53.5 + (499.7 + 42.4 = 542.1) | 595.6 |
| Maturity wall | 306.5 + 570.0 + 1,110.0 + 1,289.0 + 3,410.1 + 2,595.0 + 1,400.0 | 10,680.6, equal to total principal |
| 2030 maturities | 700.0 + (426.0 + 65.0 + 98.0) | 1,289.0 |
| 2031 maturities | 2,200.0 + (180.0 + 28.2 + 41.8) + 960.1 | 3,410.1 |
| 2032 maturities | 1,600.0 + 995.0 | 2,595.0 |
| Kinetic ABS 2026-2 notes | 805.2 + 134.2 + 201.3 | 1,140.7 |
| Swap notional, 2026-06-30 | 200.0 + (3 x 150.0); Q2 10-Q page:32 | 650.0 |
| Implied second-half Adjusted EBITDA for outlook | 1,450 - 798.7 and 1,500 - 798.7 | 651.3 to 701.3 |
| Total debt principal tie-out | 7,886.5 + 995.0 + 1,799.1 (Q2 10-Q page:20-21) | 10,680.6, equal to the printed total |
| Net loss, first half | -70.3 + -155.9 | -226.2, equal to the printed figure |

## Gaps

| Gap | Severity | Affected use | Remediation |
| --- | --- | --- | --- |
| Covenant tests, levels and reported ratios are not printed; headroom is Not calculable | High | Covenant analysis | Supply the credit agreement definitions and compliance certificate |
| Executed credit agreements and indentures not supplied, so the debt table rests on filing summaries | High | Capital structure, ranking | Supply the executed documents |
| No debt maturity schedule is printed; the maturity table is built from each instrument's printed due date and ignores term loan amortization | Medium | Maturity profile | Use as an instrument-level view; confirm against a maturity schedule if supplied |
| Pro forma Adjusted EBITDA for the combined company is not printed in the sources read; trailing figures include July 2025 without Windstream | Medium | Leverage and cover | Supply pro forma Adjusted EBITDA or Windstream July 2025 results |
| Outcome of the asset sale offers expiring 2026-08-20 and the final term loan prepayment are Not supplied | Medium | Post-quarter leverage and liquidity | Supply later filings up to the cutoff |
| No filing after 2026-07-30, including any third-quarter 2026 report | Medium | Currency of the base | Supply later filings or confirm none |
| Cash interest is printed for the year and cumulative periods; single quarters are derived and uneven because of coupon timing | Low | Interest cover | Treat quarterly cover as indicative only |
| Segment contribution margin is not reconciled to Adjusted EBITDA in the sources read, other than through the net income reconciliation (Q2 10-Q page:49) | Low | Segment profitability | Use contribution margin as a segment measure only |

## Next module

- CP-1A: carry the 2025-08-01 reverse merger, the three segments and the shift of Fiber Infrastructure revenue from Windstream lease income to external wholesale and fiber revenue, plus the unrestricted subsidiary structure behind the ABS notes.
- CP-2: take the leverage, cover and liquidity figures with their labels. Carry as restrictions the missing covenant levels, the company-defined Adjusted EBITDA, the mixed-perimeter trailing period, the 2031 and 2032 maturity concentration, capital expenditures that exceed operating cash flow, the 575.0 preferred stock liquidation preference and the July 2026 financing events not in quarter-end figures.
- CP-5: cite page chunks as given; label management outlook and release headlines as attributed claims.
