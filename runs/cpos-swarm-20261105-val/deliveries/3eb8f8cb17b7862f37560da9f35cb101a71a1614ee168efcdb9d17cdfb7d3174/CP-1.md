# CP-1 — Financial base view: Valaris Ltd (val)

## Request

- Issuer: Valaris Ltd (issuer id `val`; the filings name the registrant "Valaris Limited"), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD, in millions unless stated. Current period Q3 2026; prior period FY2025.
- Run: `val-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Execution: host session; the analyst read the pinned files and wrote this answer. No provider was called.
- Question: what do the reported statements, debt, liquidity, covenant and cash-flow facts support as a financial base for the credit view, on the consolidated perimeter of Valaris Limited and subsidiaries?
- Perimeter: consolidated Valaris Limited and subsidiaries. ARO (50/50 joint venture with Saudi Aramco) is not consolidated and is carried under the equity method (10-K page:122). ARO figures inside segment tables are 100 percent of ARO and are removed in "Reconciling Items" (Q3 release page:4, footnote 1). No parent or sponsor figures are used.
- Upstream handoff read: CP-0 (source readiness), all four consumers READY_WITH_LIMITATIONS. Its limitations are carried below: covenant levels, ratings, executed debt documents, the Business Combination Agreement and ARO's own statements are Not supplied.

## Sources

| Source | sha256 | Use in this answer |
| --- | --- | --- |
| 10-K_2025-12-31_val-20251231.htm.jsonl | b0f40796936a513fe6362c5f87d6a2a2819cd2f6e423112bfcf4a7c94647ac50 | Audited FY2025 statements, debt note, contractual obligations, cash interest and tax paid, ARO notes |
| 10-Q_2026-03-31_val-20260331.htm.jsonl | 856b19f20ceb9a456e4cf71dc5d1f96d12072575504148e1684cf5301164037f | Q1 2026 liquidity and revolver statements (page:20, page:23, page:44) |
| 10-Q_2026-06-30_val-20260630.htm.jsonl | d045ec4aa0f0c5450f1ffc05520139072532c8f88ec1804bd561ac63d9d380b7 | Q2 2026 liquidity and revolver statements (page:21, page:24, page:48) |
| 10-Q_2026-09-30_val-20260930.htm.jsonl | 73a1a96ecd1c9340e41638f2528ea86ae030d4c896022c1e422144610c8461ec | Q3 2026 and nine-month statements, debt, liquidity, commitments, ARO |
| EX-99.1_2026-05-04_a03312026ex991pressrelease.htm.jsonl | fb13914842f3e3a58a0b5ccdbd3cb04d0eb99161ae6d4b18bdfd3afa295e84b5 | Q1 2026 release: Adjusted EBITDA for Q1 2025 |
| EX-99.1_2026-08-05_a06302026ex991pressrelease.htm.jsonl | 21077052c215c76afaa6a29e3ea89e20e01ee6140be558608fa94290eaa87b1f | Q2 2026 release: Adjusted EBITDA for Q2 2025 and Q2 2026 |
| EX-99.1_2026-11-02_a09302026ex991pressrelease.htm.jsonl | 649e9df09c58fc28e42170873dd9e204e4698e7b6a16ba8868ab909251dcc271 | Q3 2026 release: five discrete quarters, Adjusted EBITDA, backlog, segments |
| context | 630c8480b8c6896f51051152fc8ca75c81e04a78fc5ea8aebca9a62a14a6fd8f | Run settings; not issuer evidence. Valuation, quotes, ratings and deal terms are blank, not zero |

| Handoff | sha256 | Use in this answer |
| --- | --- | --- |
| CP-0 | f373f490427bdb136b51b89f68fd080fb20b9ef4328505ea7636662606abf930 | Readiness view, perimeter, gap register and consumer limitations |

Locators are `page:N`, the chunk number in the pinned `.jsonl`, not the printed page. "Q3 release" is the November 2, 2026 release; "10-Q Q3" is the September 30, 2026 Form 10-Q. The filings are controlling for statement facts. Adjusted EBITDA and backlog appear only in the releases and are attributed management measures.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Valaris has one 8.375% second lien note series due 2030 and an undrawn $375.0 million revolver. Leverage on Adjusted EBITDA rose from 1.71 times at FY2025 to 2.68 times on a last-twelve-months basis to Q3 2026. | Medium | Covenant levels, ratings and 2026 cash interest paid are not supplied; Adjusted EBITDA is a company measure. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Adjusted EBITDA fell from 642.2 in FY2025 to 410.8 for the last twelve months to Q3 2026, then recovered to 150.6 in Q3 2026. | Leverage is higher than at FY2025 but the latest quarter is the strongest of the last four. | High |
| Cash was 525.1 at September 30, 2026 against 599.4 at December 31, 2025, with capital expenditure above operating cash flow in 2026. | Free cash flow is negative on a nine-month and last-twelve-months basis, funded from cash. | High |
| Liquidity is cash plus the undrawn $375.0 million revolver, 900.1 at September 30, 2026; no debt principal falls due before 2030. | Near-term refinancing risk is low; the revolver matures in April 2028. | High |
| The revolver carries three financial covenants but no level or reported figure is printed. | Covenant headroom cannot be assessed from these sources. | High |
| The pending Transocean combination and ARO funding commitments sit outside the reported debt figure. | The standalone figures may not describe the post-closing credit; ARO exposure is described only from Valaris disclosure. | Medium |

### Financial base view

The reported statements support a clear standalone financial base. Debt is one instrument: $1,100.0 million of 8.375% Senior Secured Second Lien Notes due April 30, 2030, issued by the Company and Valaris Finance Company LLC, with a carrying value of 1,088.5 at September 30, 2026. The $375.0 million revolver maturing April 3, 2028 has nothing drawn, and none of the letters of credit and surety bonds is issued under it. Cash was 525.1. On those inputs liquidity is 900.1 and net debt (principal less cash) is 574.9.

Earnings fell and then recovered. Issuer-defined Adjusted EBITDA was 642.2 in FY2025, 410.8 for the last twelve months to Q3 2026, and 150.6 in Q3 2026 against 96.5 in Q2 2026. Gross leverage on principal is 1.71 times at FY2025 and 2.68 times on the last-twelve-months basis; net leverage is 0.78 and 1.40 times. Operating cash flow of 155.3 for nine months 2026 did not cover capital expenditure of 328.0, so cash fell and free cash flow was negative. FY2025 net income of 979.1 includes a deferred income tax benefit of 515.1 and is not a measure of cash earnings.

The base is restricted in four ways. First, the covenant levels are not printed, so headroom is Not supplied. Second, cash interest paid is printed only for FY2025, so interest cover on cash interest is available for that year alone. Third, the 2026 figures are standalone while a combination with Transocean is expected to close on or about December 1, 2026. Fourth, ARO is outside consolidated debt and earnings and only Valaris's disclosure of it is supplied. Confidence is High for the reported statement facts and Medium for the credit conclusions that depend on them.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 1.71 | 0.78 | x | Principal 1,100.0 (10-K page:91) over FY2025 Adjusted EBITDA 642.2; cash 599.4 at December 31, 2025. Issuer-defined EBITDA; leases and pensions excluded from debt. |
| LTM Q1 2026 | 2.09 | 0.99 | x | Principal 1,100.0 over Adjusted EBITDA for Q2 2025 to Q1 2026, 527.6; cash 578.3 at March 31, 2026. Issuer-defined EBITDA. |
| LTM Q2 2026 | 2.60 | 1.32 | x | Principal 1,100.0 over Adjusted EBITDA for Q3 2025 to Q2 2026, 423.4; cash 541.2 at June 30, 2026. Issuer-defined EBITDA. |
| LTM Q3 2026 | 2.68 | 1.40 | x | Principal 1,100.0 over Adjusted EBITDA for Q4 2025 to Q3 2026, 410.8; cash 525.1 at September 30, 2026. Issuer-defined EBITDA; the October 30, 2026 coupon is after the balance date. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 7.10 | x | Adjusted EBITDA 642.2 over interest paid, net of amounts capitalized, 90.5 (10-K page:153). |
| LTM Q1 2026 | Not supplied: cash interest paid is not printed in the 2026 10-Qs or releases | x | Interest expense, net is printed quarterly; see Calculations for the accrual-based ratio, which is a different basis. |
| LTM Q2 2026 | Not supplied: cash interest paid is not printed in the 2026 10-Qs or releases | x | Same limitation as LTM Q1 2026. |
| LTM Q3 2026 | Not supplied: cash interest paid is not printed in the 2026 10-Qs or releases | x | Same limitation. The scheduled coupon of 92.1 for 2026 (10-K page:91) is a contractual amount, not interest paid. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q4 2025 (December 31, 2025) | 599.4 | 375.0 | US$m | Cash and cash equivalents; revolver commitment 375.0 with nothing drawn and no letters of credit issued under it (10-K page:129, page:146). Restricted cash excluded. |
| Q1 2026 (March 31, 2026) | 578.3 | 375.0 | US$m | Cash from the Q3 release page:8; revolver nothing drawn and no letters of credit under it (10-Q Q1 page:20, page:23). |
| Q2 2026 (June 30, 2026) | 541.2 | 375.0 | US$m | Cash from the Q3 release page:8; revolver nothing drawn and no letters of credit under it (10-Q Q2 page:21, page:24). |
| Q3 2026 (September 30, 2026) | 525.1 | 375.0 | US$m | Cash from 10-Q Q3 page:9; revolver nothing drawn and no letters of credit under it (page:22, page:26). Excludes restricted cash of 16.5. The revolver matures April 3, 2028, so it does not expire within twelve months. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0.0 | US$m | "no debt principal payments due until 2030" (10-Q Q3 page:51). Revolver undrawn. |
| 2027 | 0.0 | US$m | Same statement. Notes Receivable from ARO of 227.3 mature in October 2027 but are an asset, not debt. |
| 2028 | 0.0 | US$m | Revolver matures April 3, 2028 with nothing drawn (10-Q Q3 page:21 to page:22). |
| 2029 | 0.0 | US$m | Same statement as 2026. |
| 2030 | 1100.0 | US$m | Principal of the 2030 Second Lien Notes due April 30, 2030 (10-Q Q3 page:21; 10-K page:91 prints 1,100.0 in the 2029 and 2030 column). |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 | Nine months 2026 | Q3 2026 | LTM Q3 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- |
| Revenues, exclusive of reimbursable | 2,207.9 | 1,488.0 | 555.6 | 1,990.2 | 10-K page:105; 10-Q Q3 page:8; LTM = Q4 2025 (502.2) plus nine months |
| Total operating revenues | 2,369.0 | 1,598.2 | 593.6 | 2,135.6 | Same; LTM = Q4 2025 (537.4) plus nine months |
| Adjusted EBITDA (issuer measure) | 642.2 | 313.8 | 150.6 | 410.8 | Releases; sum of quarters; definition in Q3 release page:11 |
| Operating income | 477.0 | 152.4 | 81.3 | 191.8 | 10-K page:106; 10-Q Q3 page:8; Q3 release page:8 |
| Depreciation | 146.3 | 134.6 | 47.3 | 175.2 | 10-K page:105; 10-Q Q3 page:8 |
| Interest expense, net | 98.8 | 73.2 | 24.9 | 98.0 | 10-K page:106; 10-Q Q3 page:8; net of capitalized interest |
| Interest income | 70.8 | 49.6 | 16.3 | 68.3 | Same |
| Net income | 979.1 | 75.7 | 46.7 | 792.5 | FY2025 and Q4 2025 include deferred tax benefits |
| Net cash provided by operating activities | 546.2 | 155.3 | 67.2 | 227.5 | 10-K page:107; 10-Q Q3 page:10; Q3 release page:10 |
| Additions to property and equipment (outflow) | 343.5 | 328.0 | 121.6 | 434.3 | Same |
| Operating cash flow less capital expenditure | 202.7 | -172.7 | -54.4 | -206.8 | Calculated; not a company measure |
| Proceeds from disposition of assets | 137.9 | 102.6 | 42.3 | 104.2 | 10-K page:107; 10-Q Q3 page:10 |
| Share repurchases | 100.0 | None | None | 25.0 | 10-Q Q3 page:54; Q3 release page:10 |
| Cash paid for interest | 90.5 | Not supplied | Not supplied | Not supplied | 10-K page:153; no 2026 equivalent printed |
| Cash paid for income taxes, net | 61.5 | Not supplied | Not supplied | Not supplied | 10-K page:152; no 2026 equivalent printed |
| Cash and cash equivalents, period end | 599.4 | 525.1 | 525.1 | 525.1 | 10-K page:106; 10-Q Q3 page:9; stock at December 31, 2025 and September 30, 2026 |
| Debt principal (2030 Second Lien Notes) | 1,100.0 | 1,100.0 | 1,100.0 | 1,100.0 | 10-K page:91; 10-Q Q3 page:21 |
| Long-term debt, carrying value | 1,086.0 | 1,088.5 | 1,088.5 | 1,088.5 | 10-K page:106; 10-Q Q3 page:9 |
| Net debt (principal less cash) | 500.6 | 574.9 | 574.9 | 574.9 | Calculated; restricted cash excluded |
| Total debt / Adjusted EBITDA (x) | 1.71 | Not applicable: nine-month flow | Not applicable: quarterly flow | 2.68 | Calculated on principal |
| Net debt / Adjusted EBITDA (x) | 0.78 | Not applicable: nine-month flow | Not applicable: quarterly flow | 1.40 | Calculated |
| Adjusted EBITDA / cash interest (x) | 7.10 | Not supplied | Not supplied | Not supplied | Cash interest printed for FY2025 only |
| Adjusted EBITDA / interest expense, net (x) | 6.50 | Not applicable: nine-month flow | Not applicable: quarterly flow | 4.19 | Calculated; accrual basis, supplementary |
| Liquidity: cash plus undrawn revolver | 974.4 | 900.1 | 900.1 | 900.1 | Calculated; revolver 375.0 undrawn, no letters of credit under it |

### Source assessment

- 10-K for FY2025 (page:1, signed February 20, 2026; page:163): audited consolidated statements by KPMG LLP (page:104, page:105), USD millions, consolidated Valaris Limited and subsidiaries, US GAAP. Controlling for FY2025 and FY2024 statement facts.
- 10-Qs for Q1, Q2 and Q3 2026: unaudited condensed consolidated statements, same perimeter and currency. The Q3 10-Q (page:11) says "Certain previously reported amounts have been reclassified to conform to the current year presentation."; FY2025 comparatives are taken from the 10-K and Q3 comparatives from the Q3 10-Q.
- Releases: unaudited, management-prepared. The Q3 release repeats the Q3 10-Q statements and adds five discrete quarters, segment Adjusted EBITDA and backlog. Statement figures were matched to the 10-Q where both print them: revenues 555.6, net income 46.7, cash 525.1, operating income 81.3. No conflict found.
- All statement scopes use USD in millions, US GAAP, consolidated Valaris Limited and subsidiaries, with ARO under the equity method. The balance sheet is an instant (September 30, 2026 and December 31, 2025); flows carry their own start and end dates.

### Capital structure and debt, all instruments

| Instrument | Issuer and co-issuer | Amount | Rate | Maturity | Security and guarantors | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| 2030 Second Lien Notes | Valaris Limited and Valaris Finance Company LLC | $700.0 million issued April 2023 at par plus $400.0 million issued August 2023 at 100.75% of par; one series; 1,100.0 principal | 8.375% per annum, payable April 30 and October 30; effective rate 8.76% | April 30, 2030 | Senior secured second priority; guaranteed by "certain subsidiaries of the Company"; secured on a second-priority basis by the Collateral (as defined in the Indenture) | 10-Q Q3 page:21; 10-K page:127 |
| 2028 Credit Agreement (revolver) | Valaris Limited as borrower | Commitments of $375.0 million; accordion of $200.0 million; $150.0 million letter of credit sublimit; nothing drawn | Term SOFR plus 0.10% plus margin of 2.50% to 4.00%, or base rate plus 1.50% to 3.00%; commitment fee 0.375% to 0.75% | April 3, 2028 | First priority; guaranteed by Valaris Finance and certain other subsidiaries; first preferred ship mortgages over collateral vessels | 10-Q Q3 page:21 to page:22; 10-K page:128 to page:129 |

- Series count: the debt note lists the Initial and Additional notes as one series, so there is one note series and one revolver. No other borrowing, term loan or finance lease is listed in the debt note (10-Q Q3 page:21 to page:22).
- Fair value: the notes' estimated fair value is 1,125.2 against carrying value 1,088.5 at September 30, 2026, and 1,144.9 against 1,086.0 at December 31, 2025 (10-Q Q3 page:17; 10-K page:124). Quoted prices are Level 1 inputs per the filing.
- Redemption: from April 30, 2026 the notes are callable at 104.188% falling to 102.094% from April 30, 2027 and par from April 30, 2028 (10-K page:127). The notes carry a change-of-control offer at 101.0% of principal (10-K page:127). Whether the Transocean combination triggers it is not stated in the supplied sources.
- Maturity wall: nothing before 2030 (see the maturities table). Interest on the notes is 92.1 in 2026 and 184.3 for 2027 and 2028 together (10-K page:91).

### Claims outside the debt figure

| Item | Amount | Inside the debt figure? | Locator |
| --- | --- | --- | --- |
| Lease liabilities (current 27.9, noncurrent 41.3) | 69.2 at September 30, 2026; 72.9 at December 31, 2025 | No | 10-Q Q3 page:29 |
| Pension and other post-retirement benefits | 50.8 at September 30, 2026; 68.3 at December 31, 2025 | No | 10-Q Q3 page:29 |
| Unrecognized tax benefits, with interest and penalties | 136.6 at September 30, 2026 | No | 10-Q Q3 page:29 |
| Letters of credit and surety bonds (including an approximately $75.0 million customs bond) | 113.7; collateral deposits 14.8; none under the revolver | No (off balance sheet contingent) | 10-Q Q3 page:26, page:55 |
| Accrued interest | 38.4 at September 30, 2026; 15.4 at December 31, 2025 | No | 10-Q Q3 page:29 |
| Potential funding of ARO newbuild jackups | Commitment reduced to "$1.1 billion"; maximum aggregate contribution per partner up to $1.25 billion before reductions | No (contingent) | 10-Q Q3 page:56 |
| ARO borrowings: term loan of $359.0 million (8 years, 50% balloon) and revolving facility of up to $150.0 million with $50.0 million outstanding | At ARO, not consolidated | No | 10-Q Q3 page:55 |
| Termination fee payable to Transocean in specified circumstances | $173.0 million | No (contingent) | 10-Q Q3 page:12 |
| Malaysian tax assessment | About MYR117.0 million, about $29.0 million; $26.0 million paid and held in other assets | No | 10-Q Q3 page:56 |

- The 10-Q Q3 does not print a Valaris guarantee of ARO borrowings: a search of "guarant" across the 10-Q Q3 and 10-K finds guarantees only of the notes, the revolver and performance instruments. This is a search result, not a legal conclusion.
- Notes Receivable from ARO are an asset: principal 400.7, discount 37.3, carrying 363.4 at September 30, 2026; maturities of 227.3 in October 2027 and 173.4 in October 2028 (10-Q Q3 page:17, page:54). They are subordinated to ARO's term loan and credit facility (page:55). Valaris expects "to agree to extend the maturity" (page:54). Repayment is not assumed here.
- Not supplied: purchase commitments for rigs under construction at Valaris, factoring or supply-chain finance arrangements. A search of the 10-Q Q3 and 10-K for these terms found nothing relevant, so none is recorded and none is assumed to exist.

### Liquidity

- Inputs at September 30, 2026: cash and cash equivalents 525.1 (10-Q Q3 page:9); revolver commitment 375.0 with nothing drawn (page:22); letters of credit and surety bonds issued under the revolver: none (page:26). Restricted cash of 16.5 is excluded (page:30).
- Result: 900.1 (Calculations). The company states it "had $375.0 million available for borrowing" as of October 30, 2026 (page:51).
- The revolver matures April 3, 2028, outside twelve months. Availability is subject to the covenants and conditions of the agreement, which are not supplied.
- After the balance date: the semi-annual coupon is payable October 30, 2026. At 8.375% on 1,100.0 this is a scheduled payment of 46.1 (Calculations). Whether it was paid is not stated in the supplied sources, and no cash balance after September 30, 2026 is supplied.
- Uses of cash in 2026: capital expenditure guidance of $445.0 million to $470.0 million for 2026 (10-Q Q3 page:52), against 328.0 spent in nine months 2026. Merger and integration expenses of 40.5 for nine months (page:12) are cash costs that are not in Adjusted EBITDA.

### Covenants

- Revolver financial covenants: "a minimum book value of equity to total assets ratio, (ii) a minimum interest coverage ratio and (iii) a minimum amount of liquidity" (10-K page:129). Level, step-down, reported figure and headroom: Not supplied. Searches of all seven sources found no threshold or reported ratio.
- Company statement: in compliance "in all material respects" with the Indenture and the 2028 Credit Agreement at September 30, 2026 (10-Q Q3 page:21, page:22). This is a management statement, not a tested ratio.
- Indenture: incurrence-type limits on debt, liens, restricted payments, asset sales, affiliate transactions and mergers (10-K page:128); many are suspended at investment grade ratings from two agencies. No financial maintenance covenant is described for the notes.
- Definitions: the covenant interest coverage and liquidity definitions are not supplied, so Adjusted EBITDA, interest expense and liquidity as computed here may differ from the covenant definitions.

### Latest quarter and after

- Q3 2026 against Q2 2026 (Q3 release page:2, page:8): revenues exclusive of reimbursables 555.6 against 502.3; Adjusted EBITDA 150.6 against 96.5; net income 46.7 against 47.0. Management attributes the revenue increase to more operating days and higher average daily revenues for the floater fleet, with three drillships starting contracts during the second and third quarters.
- Middle East conflicts reduced Q3 Adjusted EBITDA by approximately $24 million against approximately $30 million in Q2 2026 (release page:2). This is a management estimate.
- Tax expense of 54.7 in Q3 included a discrete tax expense of $23 million, "primarily non-cash" (release page:2).
- Cash fell from 541.2 at June 30, 2026 to 525.1, "primarily due to capital expenditures" partly offset by operating cash flow and asset sale proceeds (release page:2).
- Backlog: 4,750.1 at November 2, 2026 against 4,585.2 at August 5, 2026 and 4,929.1 at May 4, 2026 (release page:11). Backlog is a management measure and may include contracts subject to final investment decision (release page:11, footnote).
- Fleet: VALARIS DS-15 started a contract in September (release page:3); VALARIS DS-18 started after quarter end and VALARIS MS-1 was sold for recycling (release page:1); VALARIS 250 and 116 resumed ARO bareboat charters in July and September (release page:2).
- Transaction: Business Combination Agreement with Transocean Ltd. dated February 9, 2026, exchange ratio of 15.235 Transocean shares per Valaris share; shareholder meetings on November 24, 2026; court hearing on November 26, 2026; expected close on or about December 1, 2026; the release says required regulatory approvals have been received (10-Q Q3 page:11, page:12; release page:1). Dates are expectations, not events. Merger and integration expenses were 15.5 in Q3 and 40.5 for nine months (10-Q Q3 page:12).
- ARO: Kingdom 5 and Kingdom 6 were ordered in August 2026 for about $360.0 million each; ARO's cash was $32.1 million at September 30, 2026 against $99.3 million at December 31, 2025 (10-Q Q3 page:54, page:56; 10-K page:90).
- No filing dated after November 3, 2026 is supplied.

### Segment and operating data

| Q3 2026 against Q2 2026 (US$m) | Floaters | Jackups | ARO (100%) | Other | Reconciling items | Consolidated |
| --- | --- | --- | --- | --- | --- | --- |
| Revenues exclusive of reimbursable, Q3 2026 | 346.0 | 171.2 | 144.9 | 38.4 | -144.9 | 555.6 |
| Revenues exclusive of reimbursable, Q2 2026 | 279.0 | 183.4 | 126.9 | 39.9 | -126.9 | 502.3 |
| Adjusted EBITDA, Q3 2026 | 157.6 | 43.1 | 45.5 | 16.7 | -112.3 | 150.6 |
| Adjusted EBITDA, Q2 2026 | 111.6 | 40.6 | 44.7 | 12.7 | -113.1 | 96.5 |

Source: Q3 release page:4. Reconciling items include onshore support costs, general and administrative expense and, for Adjusted EBITDA, the removal of ARO. Total fleet utilization was 67% in Q3 2026 and 67% in Q3 2025; average daily revenue was $200,000 against $176,000 (release page:12). The company reports revenue efficiency of 97% for Q3 2026 and 98% year to date (release page:1).

### Definition review and conflicts

- Adjusted EBITDA: the release defines it as "earnings before interest, tax, depreciation, other operating (income) loss, (gain) loss on sale of assets, merger and integration expenses and equity in (earnings) losses of ARO" (release page:11). The recomputation from reported lines reproduces the issuer figures for Q3 2026 (150.6), nine months 2026 (313.8) and FY2025 (642.2); see Calculations. It excludes the equity earnings of ARO and the merger costs, and it is not a covenant measure.
- Conflict, immaterial to the financial base: the Q3 release page:1 describes VALARIS 111 as sold "for conversion to a mobile offshore production unit", while the Q3 10-Q (page:18) says the rig was sold "for recycling" for $1.7 million. Both are quoted and neither is chosen. The 10-Q controls for the accounting; the proceeds are small.
- Correction of an upstream statement: CP-0 cited the FY2025 statement of operations at page:105. The statement runs from page:105 (revenues to depreciation) to page:106 (general and administrative to net income). No figure in CP-0 is affected.
- Prior-period comparability: the 2026 10-Qs state that certain previous amounts were reclassified. No difference between FY2025 totals in the 10-K and the Q4 2025 column plus nine-month 2025 figures was found: FY2025 operating cash flow of 546.2 equals nine months 2025 of 474.0 plus Q4 2025 of 72.2, and capital expenditure of 343.5 equals 237.2 plus 106.3.
- Net income quality: FY2025 net income of 979.1 includes a total income tax benefit of 426.8, of which a deferred benefit of 515.1 (10-K page:106), tied to reductions in valuation allowances on deferred tax assets (10-K page:142). Q4 2025 net income of 716.8 carries a benefit of 680.4 (Q3 release page:8). Earnings-based ratios should use Adjusted EBITDA or operating income, not net income.

## Calculations

All inputs are US$m from the cited pages. Results are rounded to one decimal for amounts and two for multiples.

1. Quarterly Adjusted EBITDA (issuer measure, "Valaris Total"): Q1 2025 181.3 (Q1 release page:10); Q2 2025 200.7 (Q2 release page:11); Q3 2025 163.2 and Q4 2025 97.0 (Q3 release page:11); Q1 2026 66.7, Q2 2026 96.5 and Q3 2026 150.6 (Q3 release page:10 to page:11).
2. FY2025 Adjusted EBITDA = 181.3 + 200.7 + 163.2 + 97.0 = 642.2.
3. Nine months 2026 = 66.7 + 96.5 + 150.6 = 313.8.
4. LTM Q1 2026 = 200.7 + 163.2 + 97.0 + 66.7 = 527.6. LTM Q2 2026 = 163.2 + 97.0 + 66.7 + 96.5 = 423.4. LTM Q3 2026 = 97.0 + 66.7 + 96.5 + 150.6 = 410.8.
5. Recomputation from reported lines, to check the issuer figure (operating income + depreciation + merger and integration expenses + other operating loss (income) - equity in earnings of ARO):
   - Q3 2026: 81.3 + 47.3 + 15.5 + 3.0 - (-3.5) = 150.6 (Q3 release page:8). Matches.
   - Nine months 2026: 152.4 + 134.6 + 40.5 + 0.2 - 13.9 = 313.8 (10-Q Q3 page:8). Matches.
   - FY2025: 477.0 + 146.3 + 27.3 - 8.4 = 642.2 (10-K page:105 to page:106). Matches, with the impairment of 27.3 as the other operating loss.
   - LTM Q3 2026 from the four quarters of the Q3 release page:8: operating income 39.4 + 20.0 + 51.1 + 81.3 = 191.8; depreciation 40.6 + 42.7 + 44.6 + 47.3 = 175.2; merger costs 0 + 13.6 + 11.4 + 15.5 = 40.5; other operating loss 19.5 - 2.8 + 0 + 3.0 = 19.7; equity in earnings of ARO 2.5 + 6.8 + 10.6 - 3.5 = 16.4. EBITDA = 191.8 + 175.2 + 40.5 + 19.7 - 16.4 = 410.8. Matches.
6. Debt principal: 700.0 + 400.0 = 1,100.0 (10-Q Q3 page:21). No redemption is reported. The 10-K contractual obligations table prints 1,100.0 (page:91).
7. Net debt: December 31, 2025 1,100.0 - 599.4 = 500.6; March 31, 2026 1,100.0 - 578.3 = 521.7; June 30, 2026 1,100.0 - 541.2 = 558.8; September 30, 2026 1,100.0 - 525.1 = 574.9.
8. Gross leverage: 1,100.0 / 642.2 = 1.71; 1,100.0 / 527.6 = 2.09; 1,100.0 / 423.4 = 2.60; 1,100.0 / 410.8 = 2.68. Net leverage: 500.6 / 642.2 = 0.78; 521.7 / 527.6 = 0.99; 558.8 / 423.4 = 1.32; 574.9 / 410.8 = 1.40. On carrying value 1,088.5 gross leverage at Q3 2026 is 2.65.
9. Sensitivity on operating income plus depreciation, which includes the equity result of ARO, merger costs and impairments: LTM Q3 2026 191.8 + 175.2 = 367.0, giving 1,100.0 / 367.0 = 3.00 gross and 574.9 / 367.0 = 1.57 net; FY2025 477.0 + 146.3 = 623.3, giving 1.76 gross and 0.80 net.
10. Interest cover, FY2025: 642.2 / 90.5 = 7.10. Accrual basis: 642.2 / 98.8 = 6.50; LTM Q3 2026 interest expense, net = 24.8 + 24.3 + 24.0 + 24.9 = 98.0 (Q3 release page:8), so 410.8 / 98.0 = 4.19. Against the scheduled 2026 coupon of 92.1 (10-K page:91) cover would be 410.8 / 92.1 = 4.46; this uses a contractual amount and is not interest paid.
11. Scheduled coupon: 1,100.0 x 8.375% / 2 = 46.1 (Indenture terms, 10-Q Q3 page:21). Annual: 92.1, which matches the 10-K contractual interest for 2026.
12. Operating cash flow less capital expenditure: FY2025 546.2 - 343.5 = 202.7; nine months 2026 155.3 - 328.0 = -172.7; Q3 2026 67.2 - 121.6 = -54.4. LTM operating cash flow = 72.2 + 155.3 = 227.5; LTM capital expenditure = 106.3 + 328.0 = 434.3; LTM = 227.5 - 434.3 = -206.8. Q4 2025 values come from the Q3 release page:10 and equal FY2025 less nine months 2025 (546.2 - 474.0 = 72.2; 343.5 - 237.2 = 106.3).
13. Other LTM sums: revenues exclusive of reimbursable 502.2 + 1,488.0 = 1,990.2; total operating revenues 537.4 + 1,598.2 = 2,135.6; interest income 18.7 + 49.6 = 68.3; net income 716.8 + 75.7 = 792.5; asset sale proceeds 1.6 + 102.6 = 104.2; share repurchases 25.0 + 0 = 25.0 (Q4 2025, Q3 release page:10).
14. Liquidity: December 31, 2025 599.4 + 375.0 = 974.4; March 31, 2026 578.3 + 375.0 = 953.3; June 30, 2026 541.2 + 375.0 = 916.2; September 30, 2026 525.1 + 375.0 = 900.1. Revolver availability is the commitment less drawn amounts (nil) less letters of credit issued under it (nil).
15. Lease liabilities: 27.9 + 41.3 = 69.2 (September 30, 2026); 35.6 + 37.3 = 72.9 (December 31, 2025) (10-Q Q3 page:29).

## Gaps

| Gap | Severity | Affected use | Action |
| --- | --- | --- | --- |
| Covenant levels, definitions, reported figures and headroom Not supplied | High | Covenant headroom, liquidity availability conditions | Obtain the 2028 Credit Agreement and compliance disclosures |
| Cash interest paid for 2026 Not supplied | Medium | Cash interest cover for LTM periods | Obtain the 10-K for FY2026 or cash flow disclosures; use accrual basis meanwhile, labelled |
| Cash taxes paid for 2026 Not supplied | Low | Cash conversion | Same |
| Cash balance after September 30, 2026, including the October 30, 2026 coupon, Not supplied | Medium | Current liquidity | Obtain later filings |
| Post-closing capital structure and treatment of the notes and revolver in the Transocean combination Not supplied | High | All forward credit views | Obtain the Business Combination Agreement, scheme document and any financing documents |
| Adjusted EBITDA is a company measure; no bridge from net income is printed in the 10-Qs, only the definition and segment rows | Medium | Leverage and cover | Label as issuer measure; recomputed here from reported lines |
| ARO standalone financial statements and any support obligations beyond the disclosed funding commitment Not supplied | Medium | ARO exposure | Obtain ARO statements |
| Ratings and market prices Not supplied (context empty) | Low | Pricing context | Keep Not supplied |
| Release and 10-Q disagree on the use of VALARIS 111 | Low | None for financials | Log only |

## Next module

- CP-1A: use the debt, liquidity and covenant facts above; carry the Transocean combination (agreement February 9, 2026; expected close on or about December 1, 2026; termination fee $173.0 million) and ARO as the central transaction and affiliate exposures. Label forward dates as expectations.
- CP-2: use the leverage, liquidity and cash flow results with their basis labels. Carry as restrictions: covenant levels Not supplied, 2026 cash interest paid Not supplied, issuer-defined Adjusted EBITDA, standalone perimeter.
- CP-5: trace each figure to the pages cited; the LTM figures are sums of quarters in Calculations items 1 to 4 and 12 to 13.
