## Request

This handoff builds the financial base for VSE CORP (registrant VSE Corporation, ticker VSEC, issuer id vsec) as of 2026-11-05, pathway credit_snapshot, reporting currency USD, current period Q3 2026 against FY2025, cutoff 2026-11-05. It extracts the reported statements, debt by instrument, liquidity, covenant disclosure, claims outside debt, the latest quarter and subsequent events, then calculates leverage, liquidity and cover on stated bases. Amounts are USD; statement figures are in thousands (USD k) and the chart tables are in US$m or x as their headings require. All figures come from the seven pinned sources below. No outside knowledge of the company is used.

## Sources

Issuer sources relied on, with the labels used in this handoff. Locators are `page:N`, the chunk of the converted file, not the printed page.

| Label | Exact source name | sha256 |
| --- | --- | --- |
| S1 | 10-K_2025-12-31_vsec-20251231.htm.jsonl | 83b072172f28f55aebaf3a6972f9c86687a4b113bdf988f323774cea0cf36aed |
| S2 | 10-Q_2026-03-31_vsec-20260331.htm.jsonl | f6b924ea5eba470e1f49667b84c48b593c43a380b95f687d6114875e8f37f39d |
| S3 | 10-Q_2026-06-30_vsec-20260630.htm.jsonl | fa3609d44d226dc8671529fb2fbfc175fcb641b5ffc98070769608107bc75600 |
| S4 | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | 68af0ce7093699c714a705843bb9cea05a028d2dd1bb6a0a12fdd362022c36f1 |
| S5 | EX-99.1_2026-05-05_vse-prxq1x2026earningsrele.htm.jsonl | 1a0b0741e0cb41d8d01fb77bba0765b0d91e0ee2d640c0871a3ef4c38f0e2f04 |
| S6 | EX-99.1_2026-08-05_vse-prxq2x2026earningsrele.htm.jsonl | 047a25aea3f55f6b12255c44556aba2d1cd8074d64427d9b3bf8fc3f0328e7e4 |
| S7 | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | 433c5d4af4ceef97f7133d6bf32c06676acee7a23adece5c52f374d8108500f0 |

Run settings (not issuer evidence): context sha256 40207d2127823884a7bc8082859719f4c4c78b2e88a9548b0c57178ea14b1746.

Supplied handoff: CP-0 (source readiness), sha256 2cdcc9415abc8726a2bd6013cc3fc6053fad1900f1d23a6661cbe4e6c3b944c9. It was opened and used: its status (READY_WITH_LIMITATIONS), the perimeter break at 2026-05-05, the missing credit agreement and first amendment, the missing 2026 cash interest, and the rule that filed statements control over release figures are all carried below. S1 to S4 are filed statements and control; S5 to S7 are management releases and are cited as attributed figures. This handoff reads S1, S3, S4 and S7 at the pages cited and S2, S5 and S6 at the pages cited; it makes no claim of a full read of every page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| VSE's financial base is usable but newly leveraged: debt rose to USD 978.8 million after the May 2026 acquisition, giving 3.26x debt to trailing EBITDA, while free cash flow this year is thin and covenant headroom cannot be measured. | Medium | Covenant levels, amended-facility margins and 2026 cash interest are not in the pack, and acquisition-adjusted earnings are a management figure with no schedule. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Net debt is 3.04x trailing adjusted EBITDA at September 2026, against 1.24x at December 2025, because the acquisition was financed with debt and equity. | Leverage is far higher than at December 2025; reduction depends on earnings growth and free cash flow rather than scheduled repayment. | Medium |
| Of the debt, 93.8 percent is secured bank debt at floating rates; the unsecured amortizing notes are the remainder. | Secured lenders rank ahead of the notes, and only part of the floating exposure is hedged by swaps. | High |
| Free cash flow was negative for the nine months to September 2026, with a positive third quarter; an inventory build absorbed cash. | Debt reduction this year leans on a strong fourth quarter that management expects but the filings do not yet show. | Medium |
| Liquidity is USD 479.2 million of unused revolver commitments plus USD 65.8 million of cash, and scheduled repayments before 2030 are small. | Near-term refinancing risk is low; the maturity wall sits in 2033 with the term loan. | High |
| The only cash interest figure is for FY2025; 2026 interest cover must rest on expense and contractual-rate estimates. | Coverage for 2026 is an estimate, not a cash measure, until cash interest is disclosed. | High |

### Financial base view

The financial base is sufficient for a credit snapshot, and it describes a business that changed shape during 2026. Revenue and earnings are strong and the filed statements are complete for every period needed, but the perimeter now includes the Precision Aviation Group business acquired on 2026-05-05, which contributed USD 173.7 million of the USD 541.0 million of Q3 2026 revenue, so FY2025 and Q3 2026 are not like-for-like. The acquisition took debt from USD 296.3 million to USD 978.8 million of principal while about USD 1.3 billion of net equity and tangible equity unit proceeds funded a portion of the cash price (S4 page:29); net debt over management's trailing adjusted EBITDA is 3.04x, or 2.35x if management's pre-acquisition earnings are accepted, against 1.24x at the end of 2025. Liquidity is adequate, and the debt is mostly secured floating-rate bank debt maturing in 2030 and 2033. The weak points are cash conversion (nine-month free cash flow negative after a large inventory build), a quarter with a non-cash earn-out gain inside operating income, add-backs of about a tenth of nine-month adjusted EBITDA, and the absence of covenant levels. Those points limit confidence in leverage trajectory and headroom, not in the reported balance sheet.

### Reporting entity and perimeter

The reporting entity is VSE Corporation consolidated (S4 page:21, single reportable segment, Aviation); there is no stand-alone borrower, parent or sponsor statement, and the context names none. The borrower under the credit agreement is the Company, with subsidiary guarantors named only generically in the exhibit list (S1 page:81 "each subsidiary of the Company from time to time party thereto as guarantors"). Amounts are continuing operations unless marked. The cash flow statement still combines continuing and discontinued operations for 2025 comparatives (S7 page:12 "The cash flows related to discontinued operations and held-for-sale assets and liabilities have not been segregated"), so 2025 operating cash flow and free cash flow include the Fleet business until its April 2025 sale. Periods used: FY2025, Q1 to Q3 2026 and Q3 2025, nine months (9M) 2025 and 2026, and trailing twelve months (TTM) as management prints them.

### Debt by instrument

| Instrument | Obligor and guarantors | Principal at 2026-09-30 (USD k) | Rate | Maturity and amortization | Security and ranking | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| Term loan B (New Term Facility), original USD 900.0 million | Borrower: VSE Corporation. Guarantors: not named in the 10-Q; the 2025 credit agreement lists subsidiary guarantors (S1 page:81) and whether they guarantee the amended facility is not stated | 897,750 | Term SOFR or ABR plus a margin set by the Total Net Leverage Ratio; 5.90% at 2026-09-30; margin grid not supplied | 2033-05-05; USD 9.0 million a year in equal quarterly installments from September 2026 | Senior secured | S4 page:17 "interest rate on the Company's outstanding term loan borrowings and weighted average interest rate on its outstanding revolving facility borrowings were 5.90% and 5.65%"; S4 page:18; S2 page:13 |
| Revolving facility, USD 500.0 million commitment (upsized from USD 400.0 million) | Borrower: VSE Corporation; guarantors as above | 20,000 drawn | Weighted average 5.65% on the drawn amount | 2030-05-02 | Senior secured | S4 page:17; S4 page:18; S4 page:32 |
| Amortizing notes (part of 5.750% tangible equity units) | Issuer: VSE Corporation; no co-issuer or guarantor stated | 61,043 | 5.93% per annum, quarterly installments of principal and interest | Final installment 2029-02-01 | Senior unsecured | S4 page:19 "senior unsecured amortizing notes"; S4 page:19 maturity table |
| Total principal | | 978,793 | | | | S4 page:17 "Principal amount of long-term debt 978,793 296,250" |
| Less unamortized debt issuance costs | | (18,854) | | | | S4 page:17 |
| Carrying amount: current 32,344 plus long-term 927,595 | | 959,939 | | | | S4 page:17 |

Letters of credit outstanding were USD 0.8 million at 2026-09-30 (S4 page:17). Interest rate swaps designated as cash flow hedges hedge USD 250.0 million of notional: USD 150.0 million at 2.8% through 2027-10-31 and USD 100.0 million at 4.0% through 2029-07-31 (S4 page:19), against USD 917.75 million of floating-rate secured debt. The prepaid stock purchase contracts in the units are equity, settled in shares on 2029-02-01 (S4 page:26 and page:27), and carry no cash claim.

### Maturity wall

Principal by year at 2026-09-30, from S4 page:19: the remainder of 2026, USD 7.958 million; 2027, 32.691; 2028, 34.128; 2029, 15.516; 2030, 29.000 (term loan 9.000 plus the revolver draw 20.000); 2031, 9.000; 2032 and later, 850.500. The sum is 978.793, equal to total principal. Almost 87% of principal falls in 2032 or later (850.5 of 978.8, calculated below). No facility expires within twelve months; scheduled principal due within twelve months is the current portion of long-term debt, USD 32.344 million (S4 page:4). The chart table below carries the same buckets.

### Claims outside the debt figure

| Claim | Amount at 2026-09-30 | In or outside the debt figure | Locator and note |
| --- | --- | --- | --- |
| Long-term operating lease obligations | USD 75.817 million (current portion is inside accrued expenses and is not printed in the 10-Q; FY2025 current portion was USD 6.306 million) | Outside | S4 page:4; S1 page:68 "Less: current portion of lease liabilities (a) (6,306)" |
| Earn-out obligations (PAG seller USD 24.970 million fair value plus two assumed obligations USD 2.397 million) | USD 27.367 million carried; the seller earn-out can reach USD 125.0 million, payable in cash or equity at the Company's sole discretion | Outside | S4 page:4; S4 page:10; S4 page:24; S4 page:25 |
| PT6 fuel pump license purchase liability | USD 2.1 million remaining | Outside | S4 page:14 |
| Deferred compensation | USD 4.624 million | Outside | S4 page:4 |
| Exchangeable shares of a VSE subsidiary issued to the PAG seller | 1,415,752 shares, fair value USD 238.002 million, exchangeable one-for-one for Company common stock and automatically exchanged by 2029-05-05 | Outside (equity) | S4 page:10 |
| Pensions and retiree medical | Not supplied: none found; searched "pension" and "retiree" in all seven sources, where the only matches are inside the word "suspension" | Not applicable | Search result, not a statement by the Company |
| Factoring and supply chain finance; purchase and capacity commitments | Not supplied: none found; searched "factoring", "supply chain financ", "purchase commitments", "purchase obligations" in S1 and S4. S4 page:33 says there are no material changes to other obligations and commitments disclosed in S1 | Not applicable | S4 page:33 |
| Litigation | None disclosed: Part II Item 1 Legal Proceedings reads "None." | Not applicable | S4 page:35 |

Seller note receivable and earn-out receivable are assets, not claims: the USD 25.0 million seller note from the Fleet sale matures in July 2030 (S4 page:16), and the earn-out receivable of up to USD 65.0 million was carried at nil after a USD 29.2 million write-down in 2025, with preliminary results showing the threshold was not achieved (S4 page:25 "the earn-out performance threshold was not achieved").

### Liquidity

Liquidity at 2026-09-30 is cash of USD 65.8 million (S4 page:4, 65,786) plus unused revolver commitments of USD 479.2 million (S4 page:32 "$479.2 million of unused commitments under the Credit Agreement"), a total of USD 545.0 million. The unused figure is the USD 500.0 million commitment less USD 20.0 million drawn less USD 0.8 million of letters of credit, which reconciles to the printed 479.2 (calculated below). The revolver matures 2030-05-02, so none of it expires within twelve months. The prior quarter-ends were USD 69.4 million cash and USD 399.4 million unused at 2025-12-31 (S1 page:33 and page:41), USD 1,239.4 million and USD 399.3 million at 2026-03-31 (S2 page:4 and page:23), and USD 75.4 million and USD 499.3 million at 2026-06-30 (S3 page:4 and page:29). The 2026-03-31 cash was offering proceeds held for the 2026-05-05 closing and is not an operating liquidity level. Whether the revolver letter-of-credit sub-limit changed with the upsize is not stated (the 2025 agreement had USD 30.0 million, S1 page:62).

### Covenants

| Test | Level and step-downs | Issuer-reported figure | Headroom |
| --- | --- | --- | --- |
| Maximum Total Net Leverage Ratio | Not supplied: S4 page:19 says only that restrictive covenants include "a maximum Total Net Leverage Ratio and a minimum Interest Coverage Ratio" | Not supplied; the Company states it "was in compliance" at 2026-09-30 | Not calculable: no level |
| Minimum Interest Coverage Ratio | Not supplied | Not supplied; compliance stated | Not calculable: no level |
| Annual dividend limit | Not supplied: S4 page:33 says cash dividends are "subject to annual restrictions" | Dividends paid USD 7.952 million in 9M 2026 (S4 page:7) | Not calculable |

The metrics in this handoff differ from the covenant definitions. Management's Net Leverage Ratio of 3.0x and Adjusted Net Leverage Ratio of 2.3x (S7 page:7) deduct debt issuance costs from net debt, and S7 page:5 says they "differ from the Total Net Leverage Ratio as defined in the Company". This handoff's net debt is principal less cash, and its EBITDA is management's TTM Adjusted EBITDA, which is not the credit agreement's EBITDA. No covenant claim is made.

### Latest quarter and subsequent events

| Date | Event | Amount and effect | Locator |
| --- | --- | --- | --- |
| 2026-08-31 | Atech Turbine Components acquired | Cash consideration USD 64.1 million net of cash acquired of USD 1.4 million, funded by cash and revolver borrowings; goodwill USD 41.1 million, customer intangible USD 21.5 million; allocation preliminary | S4 page:9 |
| Q3 2026 | Revolver drawn | USD 20.0 million outstanding at 2026-09-30; none was outstanding at 2026-06-30 | S4 page:17; S3 page:16 |
| Q3 2026 | New pay-fixed swap | USD 100.0 million notional replaced a swap that matured 2026-07-31 | S4 page:20 |
| Q3 2026 | Scheduled repayments | Term loan 900,000 to 897,750; amortizing notes 66,668 to 61,043 (USD k) | S3 page:15; S4 page:17 |
| Q3 2026 | Earn-out fair value gain | USD 8.880 million non-cash gain inside operating income | S4 page:24 |
| 2026-11-04 | Guidance raised | FY2026 revenue growth 65% to 66.5% (prior 61% to 64%); Adjusted EBITDA margin 18.9% to 19.1% (prior 18.7% to 19.0%); management statement | S7 page:3 |
| 2026-10-05 | Subsequent event: Test Logic acquired | Funded with cash on hand; price not disclosed; not material per the Company | S4 page:27 |
| 2026-09-30 | Covenant compliance | Company states compliance with the required ratios | S4 page:19 |

Earlier 2026 financing events are in the perimeter break: the February 2026 common stock offering (USD 829.0 million net) and tangible equity unit offering (USD 444.9 million net) closed 2026-02-04 and 2026-02-05 (S4 page:26 and page:29), and on 2026-05-05 the first amendment created the USD 900.0 million term loan B and USD 500.0 million revolver, repaid the prior term loan, and funded the PAG purchase (S4 page:18).

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 1.62 | 1.24 | x | Principal debt 296,250 and net debt 226,892 (principal less cash 69,358) over management TTM Adjusted EBITDA 182,924 (S7 page:7). Management prints 1.2x on net debt after issuance costs. Pre-PAG perimeter. |
| Q1 2026 (2026-03-31) | 1.85 | Not supplied: cash 1,239,407 exceeded principal debt 366,342, so net debt is negative and the ratio is not meaningful (S5 page:6) | x | Principal 366,342 over TTM Adjusted EBITDA 198,001 (S5 page:6). Cash was offering proceeds held for the PAG closing. |
| Q2 2026 (2026-06-30) | 4.02 | 3.70 | x | Principal 966,668 and net debt 891,308 over TTM Adjusted EBITDA 240,573 (S6 page:8). The TTM includes only two months of PAG, so these ratios overstate run-rate leverage; on management's TTM Acquisition Adjusted EBITDA of 370,179 the ratios are 2.61 and 2.41. |
| Q3 2026 (2026-09-30) | 3.26 | 3.04 | x | Principal 978,793 and net debt 913,007 over TTM Adjusted EBITDA 300,387 (S7 page:7), which includes five months of PAG. On management's TTM Acquisition Adjusted EBITDA of 389,234 the ratios are 2.51 and 2.35; that figure has no component schedule. Covenant definitions not supplied. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 6.81 | x | Management Adjusted EBITDA 182,924 (S7 page:7) over cash paid for interest 26,849 (S1 page:44). Cash interest is a consolidated cash flow figure that includes discontinued operations in 2025. |
| Q1 2026 | Not supplied: cash paid for interest is not reported in the Q1 2026 10-Q or release | x | Interest expense, net was an income of 1,402 because of interest on offering cash (S5 page:5), so an expense-based ratio is not meaningful. |
| Q2 2026 | Not supplied: cash paid for interest is not reported in the Q2 2026 10-Q or release | x | Interest expense, net was 5,230, net of interest income (S6 page:7); no cash measure available. |
| Q3 2026 | Not supplied: cash paid for interest is not reported in the Q3 2026 10-Q or release | x | Expense-based substitute, not cash: Adjusted EBITDA 107,165 over interest expense, net 14,097 is 7.60x for the quarter; TTM Adjusted EBITDA over contractual annual interest at 2026-09-30 rates of 57,717 is 5.20x. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 69.358 | 399.4 | US$m | Cash from the balance sheet (S1 page:41); unused commitments net of USD 0.6 million letters of credit on the USD 400.0 million revolver (S1 page:33). |
| Q1 2026 | 1,239.407 | 399.3 | US$m | Cash (S2 page:4) was offering proceeds held for the 2026-05-05 closing and a majority was used to fund the PAG acquisition at closing (S5 page:3 "a majority was used to fund the PAG acquisition at closing on May 5"); unused commitments after USD 0.7 million letters of credit (S2 page:23). |
| Q2 2026 | 75.360 | 499.3 | US$m | Cash (S3 page:4); unused commitments on the USD 500.0 million revolver after USD 0.7 million letters of credit (S3 page:29). |
| Q3 2026 | 65.786 | 479.2 | US$m | Cash (S4 page:4); unused commitments after USD 20.0 million drawn and USD 0.8 million letters of credit (S4 page:32). Revolver matures 2030-05-02. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of 2026 | 7.958 | US$m | Principal at 2026-09-30: term loan 2.250 plus amortizing notes 5.708 (S4 page:19). |
| 2027 | 32.691 | US$m | Term loan 9.000 plus amortizing notes 23.691 (S4 page:19). |
| 2028 | 34.128 | US$m | Term loan 9.000 plus amortizing notes 25.128 (S4 page:19). |
| 2029 | 15.516 | US$m | Term loan 9.000 plus amortizing notes 6.516; the notes' final installment is 2029-02-01 (S4 page:19). |
| 2030 | 29.000 | US$m | Term loan 9.000 plus the revolver draw of 20.000 due at the 2030-05-02 maturity (S4 page:19). |
| 2031 | 9.000 | US$m | Term loan amortization only (S4 page:19). |
| 2032 and later | 850.500 | US$m | Term loan B balance including the 2033-05-05 final maturity (S4 page:19 "Thereafter"). Total of all rows 978.793, equal to principal. |

### Financials and credit metrics

| Metric | Period | Amount | Unit | Source and locator | Basis and note |
| --- | --- | --- | --- | --- | --- |
| Revenues | FY2025 | 1,112,275 | USD k | S1 page:42 | Reported. Continuing operations; audited |
| Revenues | 9M 2025 | 811,093 | USD k | S4 page:4 | Reported. Continuing operations; comparative as printed in the Q3 2026 10-Q |
| Revenues | Q1 2026 | 324,580 | USD k | S5 page:3 | Reported. Release; consistent with the nine-month total in S4 |
| Revenues | Q2 2026 | 449,137 | USD k | S6 page:4 | Reported. Release |
| Revenues | Q3 2025 | 282,909 | USD k | S4 page:4 | Reported. Continuing operations |
| Revenues | Q3 2026 | 541,006 | USD k | S4 page:4 | Reported. Includes USD 173.7m from the acquired PAG business (S4 page:30) |
| Revenues | 9M 2026 | 1,314,723 | USD k | S4 page:4 | Reported. Nine months; includes PAG from 2026-05-05 |
| Operating income | FY2025 | 89,595 | USD k | S1 page:42 | Reported. After a 29,200 earn-out receivable write-down |
| Operating income | Q3 2025 | 10,087 | USD k | S4 page:4 | Reported. After a 23,300 earn-out fair value charge |
| Operating income | Q3 2026 | 77,451 | USD k | S4 page:4 | Reported. Includes an 8,880 earn-out fair value gain (non-cash) |
| Operating income | 9M 2026 | 159,157 | USD k | S4 page:4 | Reported. Nine months |
| Interest expense, net | FY2025 | 20,556 | USD k | S1 page:42 | Reported. Net of interest income |
| Interest expense, net | Q3 2025 | 4,339 | USD k | S4 page:4 | Reported. Net of interest income |
| Interest expense, net | Q3 2026 | 14,097 | USD k | S4 page:4 | Reported. First full quarter on the amended facilities; net of interest income |
| Interest expense, net | 9M 2026 | 17,925 | USD k | S4 page:4 | Reported. Depressed by interest income on offering cash held before 2026-05-05 (S4 page:31) |
| Net income from continuing operations | FY2025 | 53,493 | USD k | S1 page:42 | Reported. Audited |
| Net income from continuing operations | Q3 2026 | 47,264 | USD k | S4 page:4 | Reported. Includes the 8,880 non-cash earn-out gain before tax |
| Net income from continuing operations | 9M 2026 | 104,842 | USD k | S4 page:4 | Reported. Nine months |
| Adjusted EBITDA (management) | FY2025 | 182,924 | USD k | S7 page:7 | Reported. Printed as the 2025-12-31 TTM figure; the 10-K carries no EBITDA reconciliation |
| Adjusted EBITDA (management) | Q1 2026 | 55,430 | USD k | S5 page:5 | Reported. Q1 definition; add-backs per S5 |
| Adjusted EBITDA (management) | Q2 2026 | 86,024 | USD k | S6 page:7 | Reported. Continuing operations |
| Adjusted EBITDA (management) | Q3 2025 | 47,351 | USD k | S7 page:7 | Reported. Continuing operations |
| Adjusted EBITDA (management) | Q3 2026 | 107,165 | USD k | S7 page:7 | Reported. Margin printed 19.8% against 16.7% for Q3 2025 |
| Adjusted EBITDA (management) | 9M 2025 | 131,156 | USD k | S7 page:7 | Reported. Nine months |
| Adjusted EBITDA (management) | 9M 2026 | 248,619 | USD k | S7 page:7 | Reported. Nine months |
| EBITDA from continuing operations (management) | 9M 2026 | 221,535 | USD k | S7 page:7 | Reported. Before the add-backs that lead to Adjusted EBITDA |
| TTM Adjusted EBITDA (management) | 2025-12-31 | 182,924 | USD k | S7 page:7 | Reported. Trailing twelve months |
| TTM Adjusted EBITDA (management) | 2026-03-31 | 198,001 | USD k | S5 page:6 | Reported. Trailing twelve months, no PAG |
| TTM Adjusted EBITDA (management) | 2026-06-30 | 240,573 | USD k | S6 page:8 | Reported. Trailing twelve months, two months of PAG |
| TTM Adjusted EBITDA (management) | 2026-09-30 | 300,387 | USD k | S7 page:7 | Reported. Trailing twelve months, five months of PAG |
| TTM Acquisition Adjusted EBITDA (management) | 2025-12-31 | 209,128 | USD k | S7 page:7 | Reported. Adds pre-acquisition EBITDA of acquired businesses; no component schedule |
| TTM Acquisition Adjusted EBITDA (management) | 2026-03-31 | 217,995 | USD k | S5 page:6 | Reported. As above; Q1 definition |
| TTM Acquisition Adjusted EBITDA (management) | 2026-06-30 | 370,179 | USD k | S6 page:8 | Reported. As above |
| TTM Acquisition Adjusted EBITDA (management) | 2026-09-30 | 389,234 | USD k | S7 page:7 | Reported. As above |
| Net cash from operating activities | FY2025 | 26,990 | USD k | S1 page:43 | Reported. Includes discontinued operations |
| Net cash from operating activities | Q3 2025 | 24,089 | USD k | S7 page:7 | Reported. Includes discontinued operations |
| Net cash from operating activities | Q3 2026 | 55,991 | USD k | S7 page:7 | Reported. Quarter |
| Net cash from operating activities | 9M 2025 | (10,652) | USD k | S4 page:6 | Reported. Includes discontinued operations |
| Net cash from operating activities | 9M 2026 | 21,284 | USD k | S4 page:6 | Reported. After a 148,409 inventory build (S4 page:6) |
| Capital expenditures (purchases of property and equipment) | FY2025 | (21,281) | USD k | S1 page:43 | Reported. Outflow |
| Capital expenditures (purchases of property and equipment) | Q3 2026 | (9,372) | USD k | S7 page:7 | Reported. Outflow |
| Capital expenditures (purchases of property and equipment) | 9M 2026 | (24,699) | USD k | S4 page:6 | Reported. Outflow |
| Free cash flow (management definition) | Q3 2026 | 46,619 | USD k | S7 page:7 | Reported. Operating cash flow less capital expenditures |
| Free cash flow (management definition) | 9M 2026 | (3,415) | USD k | S7 page:7 | Reported. Nine months |
| Free cash flow (management definition) | 9M 2025 | (25,165) | USD k | S7 page:7 | Reported. Includes discontinued operations |
| Cash paid for acquisitions, net of cash acquired | FY2025 | (394,144) | USD k | S1 page:43 | Reported. Outflow |
| Cash paid for acquisitions, net of cash acquired | 9M 2026 | (1,830,791) | USD k | S4 page:6 | Reported. Outflow; mainly PAG |
| Dividends paid | FY2025 | (8,263) | USD k | S1 page:43 | Reported. Outflow |
| Dividends paid | 9M 2026 | (7,952) | USD k | S4 page:7 | Reported. Outflow |
| Cash paid for interest | FY2025 | 26,849 | USD k | S1 page:44 | Reported. Only period in the pack with cash interest |
| Cash paid for income taxes | FY2025 | 16,114 | USD k | S1 page:44 | Reported. Only period in the pack with cash taxes |
| Cash and cash equivalents | 2025-12-31 | 69,358 | USD k | S4 page:4 | Reported. Balance sheet |
| Cash and cash equivalents | 2026-03-31 | 1,239,407 | USD k | S2 page:4 | Reported. Offering proceeds held before the 2026-05-05 closing |
| Cash and cash equivalents | 2026-06-30 | 75,360 | USD k | S3 page:4 | Reported. Balance sheet |
| Cash and cash equivalents | 2026-09-30 | 65,786 | USD k | S4 page:4 | Reported. Balance sheet |
| Principal amount of debt | 2025-12-31 | 296,250 | USD k | S4 page:17 | Reported. Term loan only |
| Principal amount of debt | 2026-03-31 | 366,342 | USD k | S2 page:12 | Reported. Term loan 294,375 plus amortizing notes 71,967 |
| Principal amount of debt | 2026-06-30 | 966,668 | USD k | S3 page:15 | Reported. Term loan B 900,000 plus amortizing notes 66,668 |
| Principal amount of debt | 2026-09-30 | 978,793 | USD k | S4 page:17 | Reported. Term loan B 897,750, revolver 20,000, amortizing notes 61,043 |
| Debt issuance costs | 2026-09-30 | (18,854) | USD k | S4 page:17 | Reported. Deducted in the carrying amount |
| Inventories | 2025-12-31 | 553,834 | USD k | S4 page:4 | Reported. Balance sheet |
| Inventories | 2026-09-30 | 893,006 | USD k | S4 page:4 | Reported. Includes acquired inventory (PAG 200,179 per S4 page:10) |
| Goodwill | 2026-09-30 | 1,853,509 | USD k | S4 page:4 | Reported. Balance sheet |
| Intangible assets, net | 2026-09-30 | 950,496 | USD k | S4 page:4 | Reported. Balance sheet |
| Total assets | 2025-12-31 | 2,028,578 | USD k | S4 page:4 | Reported. Balance sheet |
| Total assets | 2026-09-30 | 4,479,958 | USD k | S4 page:4 | Reported. Balance sheet |
| Total liabilities | 2026-09-30 | 1,497,267 | USD k | S4 page:4 | Reported. Balance sheet |
| Total stockholders' equity | 2026-09-30 | 2,982,691 | USD k | S4 page:4 | Reported. Balance sheet |
| Long-term operating lease obligations | 2026-09-30 | 75,817 | USD k | S4 page:4 | Reported. Outside the debt figure; current portion not printed |
| Earn-out obligations (current) | 2026-09-30 | 27,367 | USD k | S4 page:4 | Reported. Outside the debt figure |
| Total debt / TTM Adjusted EBITDA | 2025-12-31 | 1.62 | x | Calculated | 296,250 / 182,924 |
| Total debt / TTM Adjusted EBITDA | 2026-03-31 | 1.85 | x | Calculated | 366,342 / 198,001 |
| Total debt / TTM Adjusted EBITDA | 2026-06-30 | 4.02 | x | Calculated | 966,668 / 240,573 |
| Total debt / TTM Adjusted EBITDA | 2026-09-30 | 3.26 | x | Calculated | 978,793 / 300,387 |
| Net debt (principal less cash) | 2026-09-30 | 913,007 | USD k | Calculated | 978,793 - 65,786 |
| Net debt / TTM Adjusted EBITDA | 2026-09-30 | 3.04 | x | Calculated | 913,007 / 300,387 |
| Net debt / TTM Acquisition Adjusted EBITDA | 2026-09-30 | 2.35 | x | Calculated | 913,007 / 389,234 |
| Total debt / TTM Acquisition Adjusted EBITDA | 2026-09-30 | 2.51 | x | Calculated | 978,793 / 389,234 |
| Net debt as management defines it | 2026-09-30 | 894,153 | USD k | Calculated | 978,793 - 18,854 - 65,786; matches S7 page:7 |
| Secured debt share of principal | 2026-09-30 | 93.8 | % | Calculated | (897,750 + 20,000) / 978,793 |
| Free cash flow, FY2025 on the management definition | FY2025 | 5,709 | USD k | Calculated | 26,990 - 21,281 |
| Adjusted EBITDA / cash interest | FY2025 | 6.81 | x | Calculated | 182,924 / 26,849 |
| Adjusted EBITDA / interest expense, net | Q3 2026 | 7.60 | x | Calculated | 107,165 / 14,097 |
| Contractual interest at 2026-09-30 rates (annual, before swaps and fee amortization) | 2026-09-30 | 57,717 | USD k | Calculated | 897,750 x 5.90% + 20,000 x 5.65% + 61,043 x 5.93% |
| TTM Adjusted EBITDA / contractual annual interest | 2026-09-30 | 5.20 | x | Calculated | 300,387 / 57,717 |
| TTM Acquisition Adjusted EBITDA / contractual annual interest | 2026-09-30 | 6.74 | x | Calculated | 389,234 / 57,717 |
| Liquidity (cash plus unused revolver commitments) | 2026-09-30 | 544,986 | USD k | Calculated | 65,786 + 479,200 |
| Goodwill plus intangible assets, share of total assets | 2026-09-30 | 62.6 | % | Calculated | (1,853,509 + 950,496) / 4,479,958 |
| Earn-out obligations plus long-term operating leases | 2026-09-30 | 103,184 | USD k | Calculated | 27,367 + 75,817 |

### Reconciliations and quality of earnings

Adjusted EBITDA is a management measure. For 9M 2026 it adds 27,084 to EBITDA of 221,535 to reach 248,619 (S7 page:7): acquisition, integration and restructuring costs 18,431, stock-based compensation 12,992, a loss on debt extinguishment 4,473 and divestiture-related costs 68, less an earn-out fair value gain of 8,880. The add-backs are about 10.9% of Adjusted EBITDA. In Q3 2026 the earn-out gain of 8,880 is deducted in the bridge from EBITDA of 107,581 to Adjusted EBITDA of 107,165, together with 4,059 of acquisition costs and 4,405 of stock compensation (S7 page:7), but it remains inside reported operating income of 77,451 and net income of 47,264. Q3 2025 shows the opposite: a 23,300 earn-out charge depressed reported operating income of 10,087 (S4 page:4). Comparing Q3 2026 with Q3 2025 reported earnings therefore overstates the underlying change; Adjusted EBITDA of 107,165 against 47,351 is the cleaner comparison but is still a management figure and still mixes perimeters (PAG contributed 173,666 of Q3 2026 revenue, S4 page:30). The retained quarters tie: Q1 55,430 plus Q2 86,024 equals H1 2026 of 141,454 (S6 page:7), and H1 plus Q3 107,165 equals the 9M 2026 figure of 248,619.

Cash conversion is the weak spot. Operating cash flow was 21,284 for 9M 2026 after inventory rose 148,409 in the cash flow statement (S4 page:6), while balance-sheet inventory rose from 553,834 to 893,006, which includes 200,179 of inventory acquired with PAG (S4 page:10). Free cash flow was negative 3,415 for 9M 2026 and positive 46,619 in Q3 2026 (S7 page:7); the Q3 figure alone cannot be annualised. Management expects "strong fourth quarter free cash flow" (S7 page:2), a forward statement the filings do not evidence.

### Consistency with the CP-0 handoff

The CP-0 handoff said the filed statements cover every needed period, the credit agreement and first amendment are missing, 2026 cash interest is missing and the net-debt definition in the releases deducts issuance costs. This handoff confirms each against the pages cited and corrects nothing in CP-0. It adds one detail CP-0 left open: unused revolver commitments are printed for every quarter-end (S1 page:33, S2 page:23, S3 page:29, S4 page:32), so liquidity by period is supplied.

## Calculations

All calculations use figures printed in the cited sources, in USD thousands unless stated. Net debt in this handoff is principal debt less cash and cash equivalents; management's net debt additionally deducts issuance costs.

| Calculation | Inputs | Result |
| --- | --- | --- |
| Total debt / TTM Adjusted EBITDA, 2025-12-31 | 296,250 / 182,924 | 1.62x |
| Net debt / TTM Adjusted EBITDA, 2025-12-31 | (296,250 - 69,358 = 226,892) / 182,924 | 1.24x |
| Total debt / TTM Adjusted EBITDA, 2026-03-31 | 366,342 / 198,001 | 1.85x |
| Net debt, 2026-03-31 | 366,342 - 1,239,407 | negative 873,065; ratio not meaningful |
| Total debt / TTM Adjusted EBITDA, 2026-06-30 | 966,668 / 240,573 | 4.02x |
| Net debt / TTM Adjusted EBITDA, 2026-06-30 | (966,668 - 75,360 = 891,308) / 240,573 | 3.70x |
| Same, on TTM Acquisition Adjusted EBITDA 370,179 | 966,668 / 370,179; 891,308 / 370,179 | 2.61x; 2.41x |
| Total debt / TTM Adjusted EBITDA, 2026-09-30 | 978,793 / 300,387 | 3.26x |
| Net debt / TTM Adjusted EBITDA, 2026-09-30 | (978,793 - 65,786 = 913,007) / 300,387 | 3.04x |
| Same, on TTM Acquisition Adjusted EBITDA 389,234 | 978,793 / 389,234; 913,007 / 389,234 | 2.51x; 2.35x |
| Management net debt check, 2026-09-30 | 978,793 - 18,854 - 65,786 | 894,153, equal to S7 page:7 |
| Management net leverage check | 894,153 / 300,387; 894,153 / 389,234 | 2.98x; 2.30x, printed as 3.0x and 2.3x |
| TTM identity, 2026-09-30 | 182,924 - 131,156 + 248,619 | 300,387, equal to S7 page:7 |
| H1 and 9M Adjusted EBITDA identity | 55,430 + 86,024; 141,454 + 107,165 | 141,454; 248,619 |
| Implied Q4 2025 Adjusted EBITDA (derived, not printed) | 182,924 - 131,156 | 51,768 |
| Secured share of principal | (897,750 + 20,000) / 978,793 | 93.8% |
| Share of principal due 2032 and later | 850,500 / 978,793 | 86.9% |
| Maturity buckets sum | 7,958 + 32,691 + 34,128 + 15,516 + 29,000 + 9,000 + 850,500 | 978,793, equal to principal |
| Unused revolver, 2026-09-30 | 500,000 - 20,000 - 800 | 479,200, equal to the printed 479.2 million |
| Liquidity, 2026-09-30 | 65,786 + 479,200 | 544,986 (USD 545.0 million) |
| Swap hedge ratio | (150,000 + 100,000) / 917,750 | 27.2% of floating-rate secured debt |
| Contractual annual interest at 2026-09-30 rates | 897,750 x 5.90% = 52,967; 20,000 x 5.65% = 1,130; 61,043 x 5.93% = 3,620 | 57,717, before swaps, fees and issuance cost amortization |
| TTM Adjusted EBITDA / contractual interest | 300,387 / 57,717; 389,234 / 57,717 | 5.20x; 6.74x |
| Adjusted EBITDA / cash interest, FY2025 | 182,924 / 26,849 | 6.81x |
| Adjusted EBITDA / interest expense, net, Q3 2026 | 107,165 / 14,097 | 7.60x |
| Free cash flow FY2025 on management's definition | 26,990 - 21,281 | 5,709 |
| Add-backs to 9M 2026 EBITDA | 248,619 - 221,535; 27,084 / 248,619 | 27,084; 10.9% |
| PAG share of Q3 2026 revenue | 173,666 / 541,006 | 32.1% |
| Goodwill plus intangibles share of total assets | (1,853,509 + 950,496) / 4,479,958 | 62.6% |
| Earn-out obligations plus long-term operating leases | 27,367 + 75,817 | 103,184 |

## Gaps

- Credit agreement of 2025-05-02 and first amendment of 2026-05-05: Not supplied. Covenant levels and step-downs, covenant definitions, post-amendment margin grid, guarantor names, security details, dividend limit amount: Not supplied. Covenant headroom is Not calculable. Searched all seven sources for "maximum Total Net", "Interest Coverage", "guarant" and "applicable margin"; only the generic statements cited above were found. Carried from CP-0.
- Cash paid for interest and income taxes in 2026: Not supplied. Searched "interest paid", "cash paid for interest", "paid for interest" and "taxes paid" in S2, S3, S4 and the three releases; only S1 page:44 has them, for FY2025 and earlier. The interim supplemental cash flow disclosure lists non-cash items only (S4 page:7). EBITDA / cash interest is therefore supplied for FY2025 only.
- Acquisition-adjusted EBITDA: management's TTM Acquisition Adjusted EBITDA is not reconcilable from the pack; there is no pre-acquisition schedule, and the pro forma tables are revenue and net income only (S4 page:11). The 2.35x and 2.51x ratios rest on it and are management-attributed.
- FY2025 EBITDA: no EBITDA reconciliation in the 10-K; FY2025 Adjusted EBITDA of 182,924 comes from the Q3 2026 release (S7 page:7). Q4 2025 alone is not printed; 51,768 is derived. The 2025 comparatives are restated for definitions in the 2026 releases (S6 page:1), so S5's Q1 2025 adjusted figures are not comparable with later ones.
- Cash flow perimeter: 2025 operating cash flow and free cash flow include discontinued operations (S7 page:12).
- Current operating lease liabilities at 2026-09-30 are inside accrued expenses and not printed; total lease obligations at that date are Not supplied. FY2025 total present value was 49,999 (S1 page:68).
- Instrument terms not supplied: amortizing note indenture, revolver letter-of-credit sub-limit after the upsize, term loan B margin and call protection.
- Purchase accounting for PAG, Atech, NorthStar and Aero 3 is preliminary (S4 page:9 to page:15); the Test Logic price is not disclosed (S4 page:27).
- Customer concentration after the acquisition is not updated in the 2026 10-Qs; S1 page:11 gives about 20% for FY2025.
- Ratings, market prices and peer data: Not supplied (context blank, not zero).
- Extraction fidelity: text conversions of HTML; tables are flattened; no check against the original or inline XBRL. Figures here were matched to the cited page text.
- Dates and currency: nothing after the cutoff is used as fact; the Q3 10-Q is signed on the cutoff date (S4 page:36). All figures are USD, matching the context.

## Next module

CP-1A (business and transaction) should use the debt table, perimeter break, latest-quarter table and claims-outside-debt table above, and should state the PAG consideration on both bases CP-0 flagged. CP-2 should take the leverage, liquidity and maturity charts, state that net debt here is principal less cash, and treat covenant headroom as Not supplied until the credit agreement and first amendment are provided. CP-5 should carry the gaps above and trace each figure to its S-label and page.
