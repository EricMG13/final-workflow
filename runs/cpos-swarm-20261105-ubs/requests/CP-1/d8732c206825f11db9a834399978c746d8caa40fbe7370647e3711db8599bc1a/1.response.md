# CP-1 financial base: UBS Group AG (ubs)

## Request

- Issuer: UBS Group AG (issuer id `ubs`), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; current period Q3 2026; prior period FY2025 (context).
- Question: build the reported financial base for UBS Group AG from the pinned sources: statements, debt, capital, liquidity and the 2026 interim evidence, with calculations shown separately, and state what the evidence cannot support.
- Perimeter: UBS Group AG consolidated, IFRS Accounting Standards, USD, unless a row says otherwise. UBS AG and other subsidiaries are named only where a source reports them separately.
- Assertion: this is a reported-fact summary with separately labelled calculations. It gives no credit conclusion on pricing or rating and no legal interpretation.

## Sources

Issuer sources relied on (pinned `.jsonl` text, locators are `page:N` extraction chunks):

| Source | sha256 | Used for |
| --- | --- | --- |
| 20-F_2025-12-31_ubs-20251231.htm.jsonl | c65ff0a03ee3c3df685c628425c6a0a7856867141560663149d32b58774d8f33 | Audited FY2025 statements and notes, key figures, capital, liquidity, debt notes, maturity analysis, provisions |
| 6-K_2026-03-31_edgarq1q26kubsgroupagc.htm.jsonl | 5ae425915ce6d8540a2dcbe4beb8ed52f974546cb1a0a776687e74bfb6a0ae6d | Capitalization table at 31.3.26 and 31.12.25 |
| 6-K_2026-03-31_investorpresotext2026.htm.jsonl | 84e6720eb0ad0ada288bec163d56547d8305bba53a01f71c7fcd5a3acd94f71a | First quarter 2026 call: attributed management metrics |
| 6-K_2026-06-30_investorpresotext2026.htm.jsonl | 671f7dde67986089a1c17da85500334fa96b51697d1642480c22e2b5d6422aa1 | Second quarter 2026 call: attributed management metrics |
| 6-K_2026-07-29_edgarq2q26kubsgroup.htm.jsonl | 88627f5322eed51bd548e2eb9daaa4bff0f8cc654e252b054c4865eeda3901ea | Capitalization table at 30.6.26 and 31.3.26 |
| 6-K_2026-09-30_edgar3q26kubsgroupc.htm.jsonl | faea893d4d4d07cf7975acc81d8e41156e0b136d2c529429a6c83f334ac28864 | Capitalization table at 30.9.26 and 30.6.26 |
| 6-K_2026-09-30_investorpresotext2026.htm.jsonl | 2ac25318ab8710edaece00656540a1c90de7efab36a24b488600ed02e222986e | Third quarter 2026 call: attributed management metrics |
| context | a67d394ad1fe0320e0c68be1bf7ef2da619705355c7aa8f5e62b6171bbf4fb2d | Run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2e54133f1b22d47b492e44c16bd40091878fdaaf285f1d8de08cc5d1ee03cf43 | Source readiness: READY_WITH_LIMITATIONS for this module; no quarterly reports, slides or audit-opinion text in the pack; debt disclosed by category |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The audited 2025 statements show a very large, deposit-funded bank balance sheet with capital and liquidity ratios above the stated requirements. Third-quarter 2026 evidence is management commentary plus a debt and equity table. | Medium | There are no interim financial statements for 2026, so current-quarter figures are rounded spoken claims. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Customer deposits are the largest funding source, with debt issued second. | Funding is mostly deposit based, while debt issued is a separate wholesale layer that includes subordinated and loss-absorbing instruments. | High |
| The common equity tier 1 ratio was 14.4% at year-end 2025 and 14.7% at the end of September 2026 on management's figure. | Capital sits above the management target of around 14%, and management guides the ratio back toward that level by year-end after buyback accruals. | Medium |
| Debt issued fell between mid-2026 and end of September 2026 in the capitalization table. | A lower debt stock is visible, but the table gives no maturity split or instrument detail for that date. | Medium |
| Swiss capital proposals and Credit Suisse legacy litigation are unquantified in the pack. | These can raise capital needs or cash costs, and their size cannot be measured from the sources. | Low |

### Financial base view

The supplied sources support a reported financial base for UBS Group AG on one audited year and one interim indicator set. FY2025 is fully audited and cross-checks to the key-figures table: revenues, expenses, profit, balance sheet, cash flow, capital, liquidity and debt notes all tie within rounding. For 2026 the pack holds only a capitalization table per quarter and call transcripts, so Q3 2026 figures other than debt issued and equity are management claims, stated rounded, with underlying measures that are not reconciled in the pack. The financial base is therefore firm for FY2025 and FY2024 and indicative only for Q3 2026. These sources report no EBITDA, no committed undrawn revolving facility and no covenant package, so industrial leverage, interest cover and facility liquidity metrics are Not supplied, and regulatory capital, loss-absorbing capacity and liquidity ratios carry the analysis.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | Not supplied: EBITDA is not a reported measure for this bank | Not supplied: EBITDA is not a reported measure for this bank | x | Debt issued of 328,501 USD m exists (capitalization table), but no EBITDA; net debt is not defined for a deposit-taking bank |
| FY2024 | Not supplied: EBITDA is not a reported measure for this bank | Not supplied: EBITDA is not a reported measure for this bank | x | Same limitation; debt issued is computed in Calculations |
| Q3 2026 | Not supplied: EBITDA is not a reported measure for this bank | Not supplied: EBITDA is not a reported measure for this bank | x | Debt issued 324,981 USD m at 30.9.26; no EBITDA or interim income statement supplied |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | Not supplied: EBITDA is not a reported measure for this bank | x | Interest paid in cash was 37,749 USD m, but it is a bank funding cost that includes deposit interest, not issuer debt service |
| FY2024 | Not supplied: EBITDA is not a reported measure for this bank | x | Interest paid in cash was 48,252 USD m; same limitation |
| Q3 2026 | Not supplied: EBITDA is not a reported measure for this bank | x | No interim cash flow or interest statement supplied |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 209858 | Not supplied: no committed undrawn facility is disclosed | US$m | Cash and balances at central banks (balance sheet); of cash and cash equivalents of 231,375 USD m, 19,118 USD m was not available for general use |
| FY2024 | 223329 | Not supplied: no committed undrawn facility is disclosed | US$m | Cash and balances at central banks (balance sheet) |
| Q3 2026 | Not supplied: no Q3 2026 balance sheet in the pack | Not supplied: no committed undrawn facility is disclosed | US$m | Management states a liquidity coverage ratio of 179% for Q3 2026, a ratio and not a cash amount |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 65300 | US$m | Debt issued measured at amortized cost due within 12 months (within 1 month, 1 to 3 months and 3 to 12 months), undiscounted and including future interest, from USD bn buckets to one decimal; excludes fair value debt of 48,400 USD m due within 12 months on the same basis |
| FY2024 | 58900 | US$m | Same basis as FY2025; fair value debt due within 12 months was 51,900 USD m |
| Q3 2026 | Not supplied: no maturity table after 31.12.25 | US$m | The 2026 capitalization tables give no maturity split after 31.3.26 |

### Financials and credit metrics

| Metric | Unit | FY2025 | FY2024 | Q3 2026 or 30.9.26 | Source and basis |
| --- | --- | --- | --- | --- | --- |
| Total revenues | USD m | 49,573 | 48,611 | Not supplied | 20-F page:371; Q3 revenue amount is not stated in the call |
| Operating expenses | USD m | 40,197 | 41,239 | Not supplied | 20-F page:371 |
| Credit loss expense | USD m | 524 | 551 | 114 (quarter, spoken) | 20-F page:371; Q3 call page:5 |
| Operating profit before tax | USD m | 8,853 | 6,821 | Underlying 4.1 bn (quarter, spoken) | 20-F page:371; Q3 figure is underlying, not reported, and is not comparable |
| Net profit attributable to shareholders | USD m | 7,767 | 5,085 | Reported net profit 2.7 bn (quarter, spoken) | 20-F page:372; Q3 call page:4 |
| Diluted earnings per share | USD | 2.36 | 1.52 | 0.85 (quarter, spoken as 85 cents) | 20-F page:372; Q3 call page:4 |
| Total assets | USD m | 1,617,427 | 1,565,028 | 1.7 trillion (spoken, rounded) | 20-F page:373; Q3 call page:5 |
| Loans and advances to customers | USD m | 653,846 | 579,967 | Not supplied | 20-F page:373 |
| Customer deposits | USD m | 788,367 | 745,777 | Not supplied | 20-F page:373 and page:432 |
| Debt issued (amortized cost plus fair value) | USD m | 328,501 | 322,128 (computed) | 324,981 | FY2025 and Q3 from capitalization tables; FY2024 computed from 20-F page:373 |
| Subordinated debt at amortized cost | USD m | 17,878 | 15,030 | Not supplied | 20-F page:433; high-trigger AT1 part 17,551 (FY2025) |
| Equity attributable to shareholders | USD m | 90,213 | 85,079 | 88,613 | 20-F page:374; Q3 capitalization table |
| Common equity tier 1 capital | USD m | 71,262 | 71,367 | Not supplied | 20-F page:37 |
| Risk-weighted assets | USD m | 493,397 | 498,538 | Not supplied | 20-F page:37 |
| Common equity tier 1 capital ratio | % | 14.4 | 14.3 | 14.7 (spoken) | 20-F page:37; Q3 call page:5 |
| Common equity tier 1 leverage ratio | % | 4.4 | 4.7 | 4.6 (spoken) | 20-F page:37; Q3 call page:5 |
| Leverage ratio denominator | USD m | 1,622,438 | 1,519,477 | Not supplied | 20-F page:37 |
| Total loss-absorbing capacity ratio | % | 38.0 | 37.2 | Capacity 187 bn (spoken, ratio not stated) | 20-F page:37; Q3 call page:5 |
| Liquidity coverage ratio | % | 182.6 (4Q average) | 188.4 (4Q average) | 179 (spoken, averaging basis not stated) | 20-F page:37 and page:246; Q3 call page:5 |
| Net stable funding ratio | % | 116.1 | 125.5 | 115 (spoken) | 20-F page:37; Q3 call page:5 |
| Cost / income ratio | % | 81.1 | 84.8 | Underlying 68.7 (spoken, not comparable) | 20-F page:37; Q3 call page:4 |
| Cash and balances at central banks | USD m | 209,858 | 223,329 | Not supplied | 20-F page:373 |
| Net cash flow from operating activities | USD m | 21,851 | 3,279 | Not supplied | 20-F page:379 |
| Interest paid in cash | USD m | 37,749 | 48,252 | Not supplied | 20-F page:379 and page:380 |
| Distributions paid on UBS Group AG shares | USD m | 2,866 | 2,256 | 4.8 bn repurchased and 2.8 bn dividend accrued year to date (spoken) | 20-F page:379; Q3 call page:3 |
| Total provisions and contingent liabilities | USD m | 5,035 | 8,409 | Not supplied | 20-F page:434 |

### Source context and perimeter

- Entity and basis: the 20-F covers UBS Group AG consolidated. Income statement page:371 is headed "Income statement For the year ended USD m Note 31.12.25 31.12.24 31.12.23", the balance sheet page:373 is "Balance sheet USD m Note 31.12.25 31.12.24", and the basis is IFRS Accounting Standards (page:3). All statements are in USD millions.
- Ownership: "UBS Group AG owns 100% of the outstanding shares in UBS AG" (20-F page:36). UBS AG standalone, UBS Switzerland AG, UBS Europe SE and UBS Americas Holding LLC report separately on regulatory bases (page:532) and are not part of the consolidated rows above.
- Capitalization table authority: filed 6-K tables, group consolidated, USD. The Q1 file (page:2) defines debt as issued "by UBS Group AG and its subsidiaries", and the later files (page:1 each) define debt issued as the sum of "Debt issued measured at amortized cost and Debt issued designated at fair value".
- Call transcripts are attributed management speech. They are not financial statements and do not override the 20-F; where a transcript figure and a filed table could be compared, they are compared below.
- Currency: group figures are USD. Division figures in the calls may be in Swiss francs (for example Personal & Corporate Banking, Q3 call page:7); none are used as group figures here.

### Audited FY2025 results

- Revenues were 49,573 USD m, up from 48,611 USD m in FY2024 (an increase of 962). Operating expenses fell from 41,239 USD m to 40,197 USD m. Credit loss expense was 524 USD m against 551 USD m (page:371).
- Operating profit before tax rose from 6,821 USD m to 8,853 USD m; the tax expense was 1,056 USD m, giving net profit of 7,797 USD m, of which 7,767 USD m is attributable to shareholders (pages:371 and 372). FY2023 operating profit of 28,255 USD m included negative goodwill of 27,264 USD m from the Credit Suisse acquisition (page:371), so FY2023 is not a run-rate comparative.
- The income statement mix is: net interest income 7,747 USD m, other net income from financial instruments at fair value through profit or loss 14,011 USD m, net fee and commission income 27,912 USD m and other income of negative 96 USD m (page:371). Interest income from amortized cost and fair value through other comprehensive income instruments was 27,948 USD m against interest expense of 26,544 USD m, so the net interest line depends on the fair value net interest line of 6,343 USD m as well (page:371).
- Key figures: the underlying cost / income ratio was 74.4% and the reported ratio 81.1% (page:37). Underlying measures are non-GAAP, defined in the 20-F appendix and not rebuilt here.
- Cash flow: net cash flow from operating activities was 21,851 USD m (3,279 USD m in FY2024); investing was an outflow of 22,802 USD m; financing was an outflow of 30,863 USD m; cash and cash equivalents ended the year at 231,375 USD m (pages:379 and 380). For a bank, operating cash flow is dominated by changes in loans, deposits and trading balances, so it is not a free cash flow measure.

### Balance sheet, funding and debt

- Total assets were 1,617,427 USD m at 31.12.25 against 1,565,028 USD m, an increase of 52,399. Customer deposits were 788,367 USD m against 745,777 USD m (page:373). Of customer deposits, 259,372 USD m were demand deposits and 256,764 USD m time deposits (page:432).
- Debt issued: amortized cost 214,706 USD m (page:433) plus designated at fair value 113,794 USD m (page:432). The fair value debt is 100% unsecured and is dominated by structured instruments (equity-linked 60,303 USD m).
- Amortized cost debt: short-term debt 33,870 USD m; senior unsecured debt 122,574 USD m of which 89,739 USD m contributes to total loss-absorbing capacity and 24,648 USD m is issued by UBS AG standalone with original maturity above one year; covered bonds 11,651 USD m; subordinated debt 17,878 USD m; debt issued through the Swiss central mortgage institutions 28,278 USD m; other long-term debt 456 USD m (pages:432 and 433).
- Subordination: of subordinated debt, 17,551 USD m is high-trigger loss-absorbing additional tier 1 and 207 USD m non-Basel III-compliant tier 2; "All of the subordinated debt instruments outstanding as of 31 December 2025 pay a fixed rate of interest" (page:433).
- Security: covered bonds and the Swiss mortgage institution debt are 100% secured and other long-term debt 97% secured; everything else is unsecured (page:433). The capitalization tables state 88% of debt issued unsecured at 31.3.26 and 30.6.26, and 87% at 30.9.26 (page:2 of the Q1 file, page:1 of the Q2 file and page:1 of the Q3 file).
- Guarantee found in the 20-F: "UBS Group AG, together with UBS AG, has fully and unconditionally guaranteed the outstanding US Securities and Exchange Commission (SEC)-registered debt securities of Credit Suisse (USA) LLC", a single issuance of 742 USD m maturing July 2032 (page:433).
- 2026 debt: the Q1 file shows short-term debt issued of 97,642 USD m and long-term of 246,279 USD m at 31.3.26 (page:2). Total debt issued was 343,922 USD m at 31.3.26, 343,551 USD m at 30.6.26 and 324,981 USD m at 30.9.26. The Q3 transcript links part of Q3 activity to "the repurchase of around 10 billion of high-cost Credit Suisse liabilities" (page:4), but it does not say how much of the fall in the table this explains, and currency effects are not split out.

### Debt maturity profile (FY2025, undiscounted, USD bn)

The 20-F reports the maturity of debt issued measured at amortized cost on an undiscounted basis including future interest (page:497): due within 1 month 9.4, 1 to 3 months 9.1, 3 to 12 months 46.8, 1 to 2 years 25.7, 2 to 5 years 66.5, over 5 years 82.6, perpetual or not applicable 17.6, total 257.6. For debt designated at fair value the buckets are 14.4, 10.6, 23.4, 31.5, 13.1 and 41.5, total 134.4 (page:497). The perpetual bucket holds AT1 instruments with interest counted over five years (page:498 footnote 2). The profile is by time bucket, not by year, and not by instrument; a maturity wall by calendar year is Not supplied. Calculated 12-month totals are in Calculations.

### Capital, loss-absorbing capacity and liquidity

- Capital at 31.12.25 (Swiss systemically relevant bank framework): CET1 capital 71,262 USD m, risk-weighted assets 493,397 USD m, CET1 ratio 14.4%, going concern capital ratio 18.5%, total loss-absorbing capacity ratio 38.0%, leverage ratio denominator 1,622,438 USD m and CET1 leverage ratio 4.4% (page:37). Requirements: going concern capital 14.99% of risk-weighted assets and 5.00% of leverage ratio denominator; CET1 10.63% and 3.50%; eligible going concern capital 18.48% and 5.62% (page:229).
- Liquidity at 4Q25 average: high-quality liquid assets 331.6 USD bn, net cash outflows 181.7 USD bn, liquidity coverage ratio 182.6% against 188.4% in 4Q24 (page:246). The net stable funding ratio was 116.1% against 125.5% (page:37). USD 51.8bn of assets were excluded from group high-quality liquid assets because they are effectively restricted in subsidiaries and branches (page:246).
- Ratings sensitivity: on the ratings at 31.12.25, a one-notch downgrade would require USD 0.3bn of cash or collateral, two notches USD 0.6bn and three notches USD 0.9bn (page:245). The 2025 rating actions are an upgrade of Moody's long-term senior unsecured rating to A2 from A3 with a stable outlook, and Fitch outlook on the group's Long-Term Issuer Default Rating changed to Positive from Stable (page:245). The ratings in force at 2026-11-05 are Not supplied.
- 2026 path (all management statements, rounded as spoken): CET1 ratio 14.7% at end March, 14.4% at end June and 14.7% at end September; CET1 leverage ratio 4.4%, 4.4% and 4.6%; liquidity coverage ratio 178%, 177% and 179%; net stable funding ratio 117%, 115% and 115%; total loss-absorbing capacity 198, 194 and 187 USD bn (Q1 call page:6; Q2 call page:5; Q3 call page:5). The 20-F ratio for liquidity is a fourth-quarter average of 64 data points; the transcripts do not state their averaging basis, so the 2026 liquidity coverage figures are not strictly comparable with the year-end figure.
- UBS AG standalone fully applied CET1 ratio: 13.9% at end March (Q1 call page:6), 14.4% at end June (Q2 call page:5) and 14.5% at end September (Q3 call page:6, after a dividend accrual of 1.8 billion). This is a different perimeter from the group.
- Management capital intentions: a current programme completed in Q3 with "4.8 billion dollars" repurchased year to date, 1.2 billion more intended over the next three months, and a year-end CET1 ratio guided "at or very close to our target of around 14%" (Q3 call pages:3 and 5). Distributions are therefore planned to move the ratio down from 14.7%.

### Third quarter 2026 evidence and subsequent events

- Reported Q3 2026 (spoken, rounded): net profit 2.7 billion, earnings per share 85 cents, effective tax rate 24.7%, Group credit loss expense 114 million, integration costs 452 million, and a 346 million charge from the repurchase of around 10 billion of high-cost Credit Suisse liabilities (Q3 call pages:4 and 5). Underlying pre-tax profit 4.1 billion, up 14%, underlying return on CET1 capital 16.7% and underlying cost / income ratio 68.7%. These underlying figures are management measures with no reconciliation in the pack.
- Division items affecting the reported result: Non-core and Legacy pre-tax profit of 360 million after "275 million of litigation charges", and a Group Items reported pre-tax loss of 740 million that includes 265 million of own credit and hedging losses (Q3 call page:9).
- Integration: 13.2 billion of gross cost reductions delivered, with about 0.5 billion more expected in the fourth quarter and about 0.5 billion of integration-related expenses expected in the fourth quarter (Q3 call pages:4 and 5).
- Swiss capital rules: Q1 call page:4 states the announced measures "would require UBS to hold around 22 billion in additional capital in CET1 terms", on top of 15 billion already needed from the Credit Suisse acquisition under existing regulations. The Q3 call (page:3) calls the September outcome in the Upper House "very concerning", and states that the ordinance affects capital from 1 January 2029 and new rules for foreign subsidiaries probably no earlier than late 2027 (page:14). These are management statements; the rule text is not supplied.
- Credit Suisse AT1 litigation: the appeal decision is expected "not before Q1 of 2027" (Q3 call page:14). The 20-F states that the cumulative effects of acquired litigation "may have material adverse consequences for the combined Group" (page:113). Litigation provisions were 2,200 USD m and acquisition-related contingent liabilities 531 USD m at 31.12.25 (page:434); the 2026 provision level is Not supplied.
- Filing events: capitalization 6-Ks filed 29 April, 29 July and 28 October 2026 and call transcripts filed 30 April, 30 July and 29 October 2026. Nothing in the pack is dated after 29 October 2026; events from 30 October to 5 November 2026 are Not supplied.

### Definition risks

- Underlying versus reported: the 20-F reports an underlying cost / income ratio of 74.4% and a reported ratio of 81.1% for FY2025 (page:37); the Q3 underlying ratio of 68.7% is on the same management concept but is not reconciled in the pack.
- Debt issued is a group-wide measure covering the holding company and all subsidiaries, including structured notes at fair value. It is not holding-company debt and not an index-eligible bond count.
- Liquidity and capital ratios use the Swiss framework and different averaging bases; they are not comparable with ratios from other jurisdictions.
- The capitalization tables switch from a short-term and long-term split at 31.3.26 to a single line from 30.6.26, and the footnote wording changes, so a debt stock series by maturity class is not available after 31.3.26.
- Rounding: the pack's sub-totals carry differences of 1 USD m, shown in Calculations.

### Corrections to the readiness handoff

- The readiness handoff recorded guarantor structure as unresolved from category-level debt tables. The 20-F does disclose one guarantee: UBS Group AG and UBS AG guarantee the SEC-registered debt of Credit Suisse (USA) LLC (page:433). The wider guarantor mapping by instrument is still not supplied.
- The readiness handoff treated UBS Group AG as the holding company on the basis of the resolution description; the 20-F also states directly that it owns 100% of UBS AG (page:36).

## Calculations

All inputs are reported figures from the cited pages. Results are calculated here and were not printed by the sources unless marked.

| Id | Calculation | Inputs | Result | Check |
| --- | --- | --- | --- | --- |
| C1 | Debt issued FY2025 | 214,706 (page:433) + 113,794 (page:432) | 328,500 USD m | Capitalization table prints 328,501; difference 1 is rounding |
| C2 | Debt issued FY2024 | 214,219 (page:433) + 107,909 (page:432) | 322,128 USD m | Not printed in the pack as a total |
| C3 | Debt issued change, 30.9.26 against 31.12.25 | 324,981 - 328,501 | -3,520 USD m | Both from capitalization tables |
| C4 | Debt issued change, 30.9.26 against 30.6.26 | 324,981 - 343,551 | -18,570 USD m | Both from capitalization tables |
| C5 | Debt issued change, 31.3.26 against 31.12.25 | 343,922 - 328,501 | +15,421 USD m | Q1 table |
| C6 | Debt issued change, 30.6.26 against 31.3.26 | 343,551 - 343,922 | -371 USD m | Q2 table |
| C7 | Equity attributable to shareholders, 30.9.26 against 31.12.25 | 88,613 - 90,213 | -1,600 USD m | Capitalization tables |
| C8 | Q1 table foots | 97,642 + 246,279 = 343,921; 92,096 + 236,405 = 328,501 | 343,921 against printed 343,922 | Difference 1 is rounding |
| C9 | Total capitalization 31.12.25 | 328,501 + 90,213 + 271 | 418,985 against printed 418,984 | Difference 1 is rounding; 31.3.26, 30.6.26 and 30.9.26 foot exactly (436,424; 432,981; 413,871) |
| C10 | Revenue growth, FY2025 against FY2024 | 49,573 - 48,611 | +962 USD m | Page:371 |
| C11 | Operating profit growth | 8,853 - 6,821 | +2,032 USD m | Page:371 |
| C12 | Income statement foots | 7,747 + 14,011 + 27,912 - 96 = 49,574; 49,573 - 524 - 40,197 = 8,852; 8,853 - 1,056 = 7,797; 7,797 - 30 = 7,767 | Within 1 USD m of printed totals | Operating expenses 27,861 + 8,807 + 3,529 = 40,197 exactly |
| C13 | Effective tax rate | 1,056 / 8,853 | 11.9% | Matches printed 11.9% |
| C14 | Cost / income ratio | 40,197 / 49,573 | 81.1% | Matches printed 81.1% |
| C15 | Balance sheet foots | 1,617,427 - 1,526,944 = 90,483 against printed total equity 90,484 | Difference 1 is rounding | Total assets growth 1,617,427 - 1,565,028 = 52,399 |
| C16 | CET1 ratio | 71,262 / 493,397 | 14.44% | Matches printed 14.4% and 14.44% (page:229) |
| C17 | CET1 leverage ratio | 71,262 / 1,622,438 | 4.39% | Matches printed 4.4% |
| C18 | Total loss-absorbing capacity ratio | (91,176 + 96,130) / 493,397 = 187,306 / 493,397 | 37.96% | Matches printed 38.0%; eligible amounts from page:229 |
| C19 | Liquidity coverage ratio | 331.6 / 181.7 | 182.5% | Printed 182.6%, the difference comes from rounding of the bn inputs |
| C20 | Loans to deposits | 653,846 / 788,367 | 82.9% | Both at 31.12.25, page:373 |
| C21 | Debt maturing within 12 months, amortized cost, FY2025 | 9.4 + 9.1 + 46.8 USD bn | 65.3 USD bn = 65,300 USD m | Undiscounted, includes interest; buckets sum to 257.7 against printed 257.6 |
| C22 | Same, FY2024 | 10.4 + 11.6 + 36.9 USD bn | 58.9 USD bn = 58,900 USD m | Page:498 |
| C23 | Fair value debt within 12 months | FY2025: 14.4 + 10.6 + 23.4 = 48.4 USD bn; FY2024: 12.1 + 11.7 + 28.1 = 51.9 USD bn | 48,400 and 51,900 USD m | Page:497 and page:498 |
| C24 | Provisions foot | 347 + 371 + 2,200 + 531 + 1,586 | 5,035 USD m | Matches printed total, page:434 |
| C25 | Reported net profit, three quarters 2026 (spoken, rounded) | 3.0 + 2.8 + 2.7 billion | About 8.5 billion | Approximate only: Q1 is spoken as "3 billion"; not an audited or filed nine-month figure |

Not calculable: leverage and interest cover on EBITDA (no EBITDA reported by this bank), net debt (not defined for a deposit-taking bank), any Q3 2026 ratio built from statements (no interim statements), debt maturing by calendar year, and 2026 debt maturity.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No 2026 interim financial statements or notes; Q3 2026 income and cash flow are spoken, rounded and partly underlying | High | CP-2, CP-5 | Supply the first, second and third quarter 2026 reports |
| Debt by instrument, issuer and guarantor, and maturity by calendar year, are not supplied; debt notes are by category | High | CP-2 | Supply instrument lists, prospectus supplements or the Pillar 3 capital instruments disclosure |
| Debt maturity split after 31.3.26 not supplied | Medium | CP-2 | Quarterly reports |
| Underlying and adjusted measures have no reconciliation to reported figures | Medium | CP-2, CP-5 | Quarterly reports and results slides |
| Ratings in force at the as-of date not supplied | Medium | CP-2 | Agency reports |
| Quantified effect of Swiss capital proposals and acquired litigation cannot be measured from the pack | Medium | CP-2 | Rule text, court filings, 2026 litigation note |
| Audit opinion text not in the extracted 20-F (see readiness handoff) | Medium | CP-5 | Supply the auditor reports |
| Events from 30 October 2026 to 5 November 2026 not supplied | Low | CP-2 | Later 6-Ks |

## Next module

- CP-1A: use the 20-F business and integration narrative with the attributed call statements; carry the Credit Suisse integration milestones (13.2 billion gross savings delivered, about 13.7 billion expected) as management claims.
- CP-2: take FY2025 as the audited base and 30.9.26 debt issued and equity as the latest filed figures; use category-level debt only; carry the Credit Suisse (USA) LLC guarantee; carry the Swiss capital proposals and AT1 litigation as unquantified risks; do not build EBITDA-based leverage, interest cover or facility liquidity for this bank.
- CP-5: trace every Q3 2026 figure to a transcript page and label it as spoken and rounded; label 20-F items by chunk locator.
