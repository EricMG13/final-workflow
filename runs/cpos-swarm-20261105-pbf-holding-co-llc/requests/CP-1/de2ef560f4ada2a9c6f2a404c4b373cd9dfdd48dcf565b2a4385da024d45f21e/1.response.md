## Request

Issuer: PBF Holding Co LLC (issuer id pbf-holding-co-llc). The filings name the registrant "PBF Holding Company LLC" and its co-registrant "PBF Finance Corporation". As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. Current period: Q3 2026 (quarter ended 2026-09-30); prior period: FY2025.

Task of this module: extract and organise the issuer's financial base from the pinned sources, show every derived figure with its inputs, and carry forward the limitations the source-readiness handoff recorded. The perimeter is PBF Holding Company LLC and its consolidated subsidiaries, as filed in its own 10-K and 10-Qs. All amounts are USD millions unless stated. The parent's earnings releases are a different perimeter and are used only as labelled context. Citations use the form (label page:N "exact substring"); labels are defined in the Sources table and N is the source chunk number, not the printed page.

Periods used: FY2024 and FY2025 (years ended 12/31), Q1 2026, Q2 2026 and Q3 2026 (three-month periods), 9M 2026 (nine months ended 2026-09-30), and LTM Q1 2026, LTM Q2 2026 and LTM Q3 2026 (last twelve months, each built as FY2025 plus the 2026 year-to-date minus the 2025 year-to-date, with the inputs shown in Calculations). Balance-sheet items are instants at period end.

## Sources

### Issuer sources relied on

| Label | Exact source name | sha256 | What it is |
| --- | --- | --- | --- |
| 10K | 10-K_2025-12-31_pbfh-20251231.htm.jsonl | d8cc408b78dbd581d058811f04c883343b35aff7d41a81cb7f7c9a865d63578a | Audited annual report, PBF Holding Company LLC and PBF Finance Corporation, FY2025 with FY2024 and FY2023 comparatives |
| Q1-10Q | 10-Q_2026-03-31_pbf-20260331.htm.jsonl | 5a4242ec4ab0800289f99b8fb8f699b2f54c974b4153ae81aa21ea53d5f7dce3 | Unaudited quarterly report, quarter ended 2026-03-31, same registrants |
| Q2-10Q | 10-Q_2026-06-30_pbf-20260630.htm.jsonl | 179cd47014072a6b74de2a12abf4417faacecc8413b4c8273ab1ec0f832d5c10 | Unaudited quarterly report, three and six months ended 2026-06-30 |
| Q3-10Q | 10-Q_2026-09-30_pbf-20260930.htm.jsonl | aa31b84f94b1c47f81c70abbb0ff7efeca9bcb80852596ec5368223e7eac72e3 | Unaudited quarterly report, three and nine months ended 2026-09-30, signed 2026-11-03 |
| Q1-PR | EX-99.1_2026-04-30_a991pressreleaseq1-26.htm.jsonl | 104828cb4c23629fde92b78b0620cad588c64bcdee91586fe5ba497364c7f993 | First quarter 2026 earnings release of PBF Energy Inc. (parent perimeter) |
| Q2-PR | EX-99.1_2026-07-30_a991pressreleaseq2-26.htm.jsonl | a7bd74033edd0eddbe8e027b1ef6a171c22d27094099293d640917935e8f4118 | Second quarter 2026 earnings release of PBF Energy Inc. (parent perimeter) |
| Q3-PR | EX-99.1_2026-10-29_a991pressreleaseq3-26.htm.jsonl | ceaca5528b0d3a91964868e4bbffe0689397a5fd5afc2bb6cfc13e308a461219 | Third quarter 2026 earnings release of PBF Energy Inc. (parent perimeter) |

Pinned run context: source `context`, sha256 e3f25603b3db519b8b37c6f17fae4507d987050b491cc8f2ad5a0c098cf08361 (user settings, not issuer evidence). The 10K, the three 10-Qs and the context carry the issuer figures. The releases are cited for context only; Q1-PR and Q2-PR are listed as read but supply no figure used below.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 6020d636d6339bed5f8cdb468a645c0df4a718ccb14e552b1c95eaddfd75b108 | Source readiness: READY_WITH_LIMITATIONS; perimeter map; gaps G1 to G10 carried below |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The issuer moved from a trough in FY2025 to strong earnings and net cash by 30 September 2026, but that rests on two strong refining quarters and on company-defined EBITDA. A further redemption followed quarter end. | Medium | Liquidity figures are rounded and cannot be rebuilt, and the covenant and legal documents are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Adjusted EBITDA was 29.5 in FY2025 and 3,505.2 for the twelve months to Q3 2026, almost all earned in Q2 and Q3 2026. | Leverage and cover metrics swing from not meaningful to very low leverage; the trailing figure depends on two quarters of strong margins. | Medium |
| Principal debt was 1,850.0 against cash of 2,510.6 at 30 September 2026, a net cash position of 660.6. | Balance-sheet leverage is minimal at quarter end and falls further after the 800.0 notes redemption on 26 October 2026. | High |
| The 2026 refinancing replaced 2028 and 2030 notes with 2032 exchangeable and 2034 notes and extended the revolver to 2031. | After the October redemption no drawn debt matures before 2032, and the revolver runs to 2031. | High |
| Cash interest paid was 162.3 for the twelve months to Q3 2026, and the figure is net of capitalised interest. | Reported interest cover is high, but the measure flatters cover because capitalised interest is excluded. | Medium |
| Obligations outside debt include leases, pension deficits, purchase commitments, environmental and emissions liabilities and unquantified Martinez investigations. | These claims rank alongside debt in downside cases and are not in the debt totals. | Medium |

### Financial base view

The issuer's financial base is the filed statements of PBF Holding Company LLC. They show a sharp turn from a trough to a strong position within three quarters. FY2025 was a loss year: a net loss of 481.3, income from operations of -292.6 even after an 832.5 gain on insurance recoveries, and company-defined Adjusted EBITDA of only 29.5 (10K page:123 "Adjusted EBITDA $ 29.5 $ (79.9) $ 2,408.0"). In the first nine months of 2026 net income was 3,269.6 and Adjusted EBITDA was 3,284.3 (Q3-10Q page:59 "Adjusted EBITDA $ 2,139.3 $ 91.5 $ 3,284.3 $ (191.4)"). Management attributes the increase to crack spreads and crude differentials affected by geopolitical conflict and to higher throughput after the Martinez restart (Q3-10Q page:43 "a significant increase in refining margins"); this is management language and is not adopted as a forecast. Q2 2026 and Q3 2026 supply 3,278.6 of the 3,505.2 LTM Adjusted EBITDA, so the trailing figure is exposed to whether those margins persist. Debt was reorganised during 2026: the 2028 6.00% and 2030 7.875% notes were redeemed, 500.0 of 2034 7.25% notes and 550.0 of 2032 exchangeable notes were issued, and the revolver was amended and extended; at 30 September 2026 principal debt was 1,850.0 against cash of 2,510.6, and on 26 October 2026, after the period, the 800.0 of 2030 9.875% notes were redeemed using cash on hand. Leverage on company Adjusted EBITDA is therefore distorted at both ends of the series: not meaningful at FY2024 and FY2025 because EBITDA is negative or near zero, and very low at LTM Q3 2026. Interest cover uses cash interest paid net of capitalised interest and so overstates cover relative to total interest. Debt is only part of the claim stack: lease, pension, purchase, environmental, emissions and legal claims sit outside it and are set out below. Liquidity is printed as rounded narrative amounts whose build cannot be reproduced from the pack. Perimeter discipline matters: the parent's releases print different cash, debt and operating income, and none of them is used for an issuer figure. This view is a financial extraction and a structured set of limitations; it is not a credit rating, a recommendation or a forecast.

### Financials and credit metrics

| Metric (USD m unless stated) | FY2024 | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | LTM Q3 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenues | 33,077.9 | 29,297.7 | 7,899.8 | 11,676.3 | 12,127.7 | 31,703.8 | 38,837.2 | Statements of operations: 10K page:154, Q1-10Q page:8, Q2-10Q page:8, Q3-10Q page:8; LTM derived |
| Income (loss) from operations | -833.3 | -292.6 | 245.9 | 1,193.8 | 1,988.3 | 3,428.0 | 3,526.4 | Same pages; includes insurance gains and the 2026 LCM reversal; LTM derived |
| Gain on insurance recoveries, net (within operating income) | nil | 832.5 | 106.5 | 250.0 | nil | 356.5 | 750.0 | Printed as a credit in operating costs; FY2024 and Q3 2026 printed as a dash; LTM derived |
| Net income (loss) | -895.9 | -481.3 | 211.7 | 1,151.9 | 1,906.0 | 3,269.6 | 3,324.5 | Same pages; LTM derived |
| Depreciation and amortization (EBITDA reconciliation basis) | 585.5 | 602.6 | 149.0 | 153.3 | 160.7 | 463.0 | 602.4 | EBITDA reconciliations: 10K page:123, Q1-10Q page:38, Q2-10Q page:49, Q3-10Q page:59; LTM derived |
| Interest expense, net | 70.7 | 186.7 | 42.5 | 42.5 | 27.6 | 112.6 | 153.9 | Same pages; net of interest income; LTM derived |
| EBITDA (company-defined) | -245.4 | 311.3 | 395.9 | 1,346.2 | 2,092.5 | 3,834.6 | 4,072.7 | Same pages; starts from net income, so includes insurance gains, the LCM reversal and derivative losses; LTM derived |
| Adjusted EBITDA (company-defined) | -79.9 | 29.5 | 5.7 | 1,139.3 | 2,139.3 | 3,284.3 | 3,505.2 | Same pages; excludes special items and adds back stock compensation; LTM derived |
| EBITDA excluding special items (company-defined) | -124.2 | -9.5 | -2.7 | 1,130.3 | 2,131.5 | 3,259.1 | 3,470.8 | Same pages; LTM derived |
| Net cash from operating activities | -136.8 | -274.3 | -371.2 | 1,520.2 | 1,921.6 | 3,070.6 | 3,372.2 | Cash flow statements are year to date: 10K page:156, Q1-10Q page:9, Q2-10Q page:9, Q3-10Q page:9; Q2 and Q3 derived by subtraction |
| Capital outlay: PP&E, turnaround and other assets | 1,001.8 | 1,144.0 | 507.8 | 242.2 | 183.8 | 933.8 | 1,327.5 | Sum of three investing lines before insurance proceeds; Q2, Q3 and LTM derived |
| Operating cash flow less that capital outlay | -1,138.6 | -1,418.3 | -879.0 | 1,278.0 | 1,737.8 | 2,136.8 | 2,044.7 | Derived; before distributions, insurance proceeds in investing and financing flows |
| Cash interest paid (net of capitalised interest) | 93.2 | 151.8 | 75.9 | 15.1 | 64.5 | 155.5 | 162.3 | Supplemental cash flow: 10K page:156, Q1-10Q page:9, Q2-10Q page:10, Q3-10Q page:10; Q2, Q3 and LTM derived |
| Cash and cash equivalents (period end) | 515.2 | 503.0 | 504.3 | 879.7 | 2,510.6 | n/a instant | n/a instant | Balance sheets: 10K page:153, Q1-10Q page:7, Q2-10Q page:7, Q3-10Q page:7 |
| Debt principal outstanding (face, per debt note) | 1,501.6 | 2,201.6 | 2,851.6 | 1,800.0 | 1,850.0 | n/a instant | n/a instant | Debt notes: 10K page:173, Q1-10Q page:15, Q2-10Q page:16, Q3-10Q page:17; before deferred costs and discount |
| Long-term debt, carrying value | 1,457.3 | 2,148.3 | 2,802.3 | 1,749.1 | 1,613.0 | n/a instant | n/a instant | Balance sheets; net of deferred financing costs and discount; the 174.0 discount at Q3 2026 includes the bifurcated exchange feature |
| Net debt (principal less cash) | 986.4 | 1,698.6 | 2,347.3 | 920.3 | -660.6 | n/a instant | n/a instant | Derived; negative means net cash; leases, derivative liability and other claims excluded |
| Total equity | 4,991.9 | 4,773.1 | 5,022.2 | 6,243.3 | 8,482.6 | n/a instant | n/a instant | Balance sheets |
| Total debt / LTM Adjusted EBITDA (x) | not calculable | 74.6 | 8.7 | 1.2 | 0.5 | n/a | 0.5 | Derived; FY2024 EBITDA negative; FY2025 ratio arithmetic only, on a near-zero denominator |
| Net debt / LTM Adjusted EBITDA (x) | not calculable | 57.6 | 7.2 | 0.6 | -0.2 | n/a | -0.2 | Derived; negative means net cash |
| LTM Adjusted EBITDA / LTM cash interest paid (x) | not calculable | 0.2 | 1.8 | 7.8 | 21.6 | n/a | 21.6 | Derived; cash interest is net of capitalised interest |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | Not supplied: Adjusted EBITDA is negative (-79.9), so the ratio is not meaningful | Not supplied: Adjusted EBITDA is negative (-79.9), so the ratio is not meaningful | x | Debt principal 1,501.6 and cash 515.2 (10K page:173 and page:153); Adjusted EBITDA is the company definition (10K page:123). |
| FY2025 | 74.6 | 57.6 | x | Principal 2,201.6 less cash 503.0 over Adjusted EBITDA of 29.5; arithmetically correct but distorted by trough EBITDA after the Martinez fire; leases and other claims excluded. |
| LTM Q1 2026 | 8.7 | 7.2 | x | Principal 2,851.6 and cash 504.3 at 2026-03-31 over LTM Adjusted EBITDA of 327.9 (derived); includes 750.0 drawn on the revolver. |
| LTM Q2 2026 | 1.2 | 0.6 | x | Principal 1,800.0 and cash 879.7 at 2026-06-30 over LTM Adjusted EBITDA of 1,457.4 (derived). |
| LTM Q3 2026 | 0.5 | -0.2 | x | Principal 1,850.0 and cash 2,510.6 at 2026-09-30 over LTM Adjusted EBITDA of 3,505.2 (derived); negative means net cash; before the 2026-10-26 redemption of 800.0, which is a subsequent event. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | Not supplied: Adjusted EBITDA is negative (-79.9), so the ratio is not meaningful | x | Cash interest paid was 93.2 (10K page:156); Adjusted EBITDA is the company definition. |
| FY2025 | 0.2 | x | Adjusted EBITDA 29.5 over cash interest paid 151.8; trough year. |
| LTM Q1 2026 | 1.8 | x | LTM Adjusted EBITDA 327.9 over LTM cash interest paid 178.9 (both derived). |
| LTM Q2 2026 | 7.8 | x | LTM Adjusted EBITDA 1,457.4 over LTM cash interest paid 187.4 (both derived). |
| LTM Q3 2026 | 21.6 | x | LTM Adjusted EBITDA 3,505.2 over LTM cash interest paid 162.3 (both derived); cash interest is net of capitalised interest of 36.5 in 9M 2026, which flatters the ratio; coupon timing makes single quarters uneven. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 2024-12-31 | 515.2 | Not supplied: the 10-K prints only an approximate total liquidity for 2024-12-31 with no availability split | US$m | Cash from the balance sheet (10K page:153). |
| 2025-12-31 | 503.0 | 1,800.0 | US$m | Availability is printed as "more than $1.8 billion" (a floor); revolver commitment 3,500.0, drawn 100.0, letters of credit 167.3; the 10-K facility table prints borrowing base availability of 2,296.6, and its borrowing base formula counts 100% of cash in controlled deposit accounts. |
| 2026-03-31 | 504.3 | 1,900.0 | US$m | Availability printed as "more than $1.9 billion" (a floor); drawn 750.0, letters of credit approximately 197.0. |
| 2026-06-30 | 879.7 | 2,700.0 | US$m | Availability printed as "approximately $2.7 billion"; revolver undrawn, letters of credit approximately 163.3. |
| 2026-09-30 | 2,510.6 | 3,100.0 | US$m | Availability printed as "approximately $3.1 billion"; revolver undrawn, letters of credit approximately 157.2, commitment 4,000.0 from 2026-09-30; availability is borrowing-base limited and rounded; whether it nets letters of credit and overlaps cash is not stated; the 2026-10-26 redemption of 800.0 for about 853.4 is not reflected. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0.0 | US$m | No instrument in the 2026-09-30 debt table matures in 2026; the 2028 and 2030 7.875% notes were redeemed earlier in 2026. |
| 2027 | 0.0 | US$m | No instrument in the 2026-09-30 debt table matures in 2027. |
| 2028 | 0.0 | US$m | The 2028 6.00% notes of 801.6 were redeemed on 2026-06-25; the old revolver expiry of August 2028 was replaced. |
| 2029 | 0.0 | US$m | No instrument matures in 2029; 2029 is only a call date for the 2034 notes. |
| 2030 | 800.0 | US$m | 2030 9.875% notes, outstanding at 2026-09-30 and redeemed on 2026-10-26 (subsequent event), so nil after that date. |
| 2031 | 0.0 | US$m | The revolver expires 2031-09-30 and is undrawn; no drawn amount matures. |
| 2032 | 550.0 | US$m | 2032 exchangeable notes mature 2032-01-15 at principal; exchangeable earlier under stated conditions; principal only, carrying value is lower. |
| 2033 | 0.0 | US$m | No instrument matures in 2033. |
| 2034 | 500.0 | US$m | 2034 7.25% senior notes; only the year is printed in the instrument title. |

Built from the Q3 debt note because the Q3 10-Q prints no maturity table. At 2025-12-31 the 10-K table showed 901.6 in 2028 and 1,300.0 in 2030 (10K page:181 "2028 901.6" and "2030 1,300.0"), total 2,201.6.

### Reported statements: expense bridge and perimeter

The income statement is by function. Cost of sales includes operating expenses and depreciation of the refineries; general and administrative expense, corporate depreciation, insurance gains and asset-sale results sit below gross profit. The bridge below reconciles revenues to income from operations for the three periods that matter most, with every input from the cited statements (Q3-10Q page:8, 10K page:154). Insurance gains are included in the FY2025 and 9M 2026 results.

| Line | Q3 2026 | 9M 2026 | FY2025 |
| --- | --- | --- | --- |
| Revenues | 12,127.7 | 31,703.8 | 29,297.7 |
| Cost of sales | -10,011.1 | -28,266.0 | -30,091.4 |
| Gross margin (derived) | 2,116.6 | 3,437.8 | -793.7 |
| General and administrative expenses | -125.0 | -358.3 | -322.0 |
| Depreciation and amortization (corporate) | -2.6 | -7.0 | -8.4 |
| Gain on insurance recoveries, net | nil | 356.5 | 832.5 |
| Loss on sale of assets | -0.7 | -1.0 | -1.0 |
| Income (loss) from operations (derived, ties to printed) | 1,988.3 | 3,428.0 | -292.6 |

The derived gross margin ties to the printed consolidated gross margin for Q3 2026 (Q3-10Q page:44 "Consolidated gross margin totaled $2,116.6 million") and for 9M 2026 (Q3-10Q page:51 "Consolidated gross margin totaled $3,437.8 million"). Operating drivers named in the 10-Q: gross refining margin per barrel of throughput (Q3-10Q page:44 "Gross refining margin totaled $2,937.5 million, or $34.56 per barrel of throughput for the three months ended September 30, 2026 compared to $721.1 million, or $9.00 per barrel"), and higher compliance cost (Q3-10Q page:45 "Total RFS compliance costs were $522.8 million for the three months ended September 30, 2026 compared to $169.0 million for the three months ended September 30, 2025"). These come from the issuer's filing and are management's explanation.

Perimeter and parent comparison. Issuer figures above are PBF Holding. For context only, the parent release prints different quarter figures: (Q3-PR page:1 "third quarter 2026 income from operations of $2,100.9 million"), (Q3-PR page:8 "Total debt 2,118.4 2,148.3") and parent Adjusted EBITDA (Q3-PR page:8 "Adjusted EBITDA $ 2,301.4"). The parent figures are not substituted for issuer figures anywhere in this handoff and the difference between 2,118.4 and the issuer's 1,850.0 principal remains unexplained by the sources.

### Debt instruments at 2026-09-30

| Instrument | Issuer and co-issuer | Principal | Rate and maturity | Security and guarantors | Status and locator |
| --- | --- | --- | --- | --- | --- |
| 9.875% senior notes due 2030 | PBF Holding and PBF Finance | 800.0 | 9.875%, 2030 | Senior unsecured; guaranteed by the Guarantor Subsidiaries | Redeemed 2026-10-26 at 106.67% for about 853.4 (Q3-10Q page:33). Principal in the debt table at Q3-10Q page:17. |
| 0.00% exchangeable senior notes due 2032 | PBF Holding and PBF Finance; PBF Energy is a party to the indenture | 550.0 | No regular interest; special interest up to 0.50% in stated cases; matures 2032-01-15 | Senior unsecured; guaranteed by certain PBF Holding subsidiaries; effectively subordinated to secured debt | Issued 2026-09-17; net proceeds about 533.2; exchange price about $96.80 per PBF Energy share; effective rate about 7.0% (Q3-10Q page:18 to page:20). |
| 7.25% senior notes due 2034 | PBF Holding and PBF Finance | 500.0 | 7.25%, 2034 | Senior unsecured; guaranteed by certain PBF Holding subsidiaries | Issued 2026-05-28, net proceeds 492.1; callable from 2029-06-01 (Q3-10Q page:21 to page:23). |
| Asset-based revolving credit facility | PBF Holding and certain subsidiaries as borrowers | 0.0 drawn | Commitment 4,000.0, extended to 2031-09-30 | Secured by liens on PBF LLC's equity in PBF Holding and on receivables, inventory and deposit accounts (10K page:181); guaranteed by domestic operating subsidiaries | Amended and restated 2026-09-30 (Q3-10Q page:24); drawn 100.0 at 2025-12-31 and 750.0 at 2026-03-31. |
| Redeemed in 2026: 6.00% senior notes due 2028 | PBF Holding and PBF Finance | 801.6 | Redeemed 2026-06-25 at 100% | Senior unsecured | Q3-10Q page:23. |
| Redeemed in 2026: 7.875% senior notes due 2030 | PBF Holding and PBF Finance | 500.0 | Redeemed 2026-09-24 at 103.938%, about 519.7 | Senior unsecured | Q3-10Q page:21. |

The debt table total at 2026-09-30 is (Q3-10Q page:17 "1,850.0 2,201.6"), with deferred financing costs of 63.0 and a discount of 174.0 bringing the carrying value to 1,613.0. The fair value of the debt at 2026-09-30 is printed as (Q3-10Q page:31 "1,850.0 1,917.4 2,201.6 2,200.2"). The exchange feature is a separate derivative liability of 197.6 at fair value and a capped call asset of 29.0 (Q3-10Q page:29 "Exchangeable feature associated with the 2032 Exchangeable Notes — — 197.6 197.6 — 197.6"); these sit outside the debt principal. After the 2026-10-26 redemption the remaining principal is 1,050.0 (derived, below).

### Claims outside the debt figure

| Claim | Amount and date | Inside or outside debt | Locator |
| --- | --- | --- | --- |
| Operating lease liabilities, third party and affiliate | 712.3 at 2026-09-30 (derived from four lines); lease liabilities in total 1,019.5 at 2025-12-31 | Outside | Q3-10Q page:7, 10K page:198 (10K page:198 "Total lease liabilities $ 1,019.5 $ 1,175.2") |
| Financing lease liabilities | 28.9 at 2026-09-30 (long-term 16.1 plus current 12.8, derived) | Outside the debt table | Q3-10Q page:7, Q3-10Q page:16 |
| Hydrogen plants purchase effect | Operating lease liability of 139.7 and right-of-use asset of 140.2 derecognised; property of 388.4 recognised | Reduces leases, adds assets | Q3-10Q page:13 to page:14 |
| Pension and post-retirement medical | Funded status -89.8 pension and -16.4 medical at 2025-12-31 | Outside | 10K page:206 (10K page:206 "Funded status at end of year $ (89.8) $ (95.1) $ (16.4) $ (15.6)"); no interim update in the pack |
| Purchase and other fixed commitments | 642.9 fixed and determinable obligations at 2025-12-31, 201.6 of it in 2026 | Outside | 10K page:188 (10K page:188 "Total obligations $ 642.9") |
| Renewable energy credit and emissions obligations | 486.5 at 2026-09-30 against 574.8 at 2025-12-31; California emissions settlement deferred to 2029 | Outside | Q3-10Q page:16, page:17 |
| Environmental liabilities | 148.4 at 2026-09-30, of which Torrance remediation 108.7 | Outside | Q3-10Q page:27 |
| Martinez fire and catalyst release investigations | Unquantified | Outside | Q3-10Q page:14, page:27 (Q3-10Q page:14 "the full financial impact of this incident cannot reasonably be estimated") |
| Guaranty of the SBR term loan | Capped at 50% of obligations on a 100.0 term loan; performance considered remote | Contingent | Q3-10Q page:25 |
| Receivables purchase facility | 200.0 uncommitted; outstanding sold balance not printed | Outside | 10K page:181 |
| Insurance premium financing | Nine-month proceeds 158.7 and payments 122.2; outstanding balance not separately printed | Outside | Q3-10Q page:10 |
| Distributions to the parent chain | Member distributions 156.4 in 9M 2026; the company may distribute to fund the parent dividend | Outside | Q3-10Q page:9, page:33 |

### Liquidity and covenants

Liquidity. The issuer prints operational liquidity as cash plus revolver borrowing availability (Q3-10Q page:66 "our operational liquidity was over $5.6 billion"), made up of cash of about 2.5 billion and availability of about 3.1 billion, with letters of credit of about 157.2 (Q3-10Q page:66 "outstanding letters of credit totaled approximately $157.2 million"). These are rounded narrative figures; the build is shown in Calculations. Facility-by-facility, only one revolver is reported. The 10-K prints a facility table (10K page:129 "Revolving Credit Facility (a) $ 3,500.0 $ 100.0 $ 167.3 $ 2,296.6 August 2028") whose borrowing base includes 100% of cash in controlled deposit accounts; no later table is printed. The facility that expired in August 2028 was replaced by the amended revolver expiring 2031-09-30, so no facility expires within twelve months of the cutoff.

Covenants. The only maintenance test is springing (10K page:181 "PBF Holding will not permit the Consolidated Fixed Charge Coverage Ratio, as defined in the Revolving Credit Agreement and determined as of the last day of the most recently completed quarter, to be less than 1 to 1") and applies only when excess availability falls below the greater of 10% of the lesser of the borrowing base and commitments and 100.0. The issuer reports compliance (Q3-10Q page:24 "the Company is in compliance with all covenants, including financial covenants, in all its debt agreements") but prints no ratio and no headroom. The notes carry incurrence covenants limiting debt, equity issuances, payments and investments, which fall away on a covenant termination event such as an investment grade rating (Q3-10Q page:23). Definition difference: the test uses "Excess Availability" and a fixed charge coverage ratio defined in the credit agreement, which is not supplied, whereas this handoff uses company-defined Adjusted EBITDA and printed borrowing availability; they are different measures.

### Latest quarter and events after it

- Q3 2026 financing: 550.0 of exchangeable notes issued 2026-09-17 with a capped call costing 27.7 (Q3-10Q page:18 "The Issuers received net proceeds of approximately $533.2 million"); the 500.0 of 7.875% notes redeemed 2026-09-24 with a 26.1 difference to carrying value booked as a loss; loss on extinguishment of 28.0 in the quarter; unrealized loss on the exchange feature of 29.9 (Q3-10Q page:8).
- 2026-09-30: revolver amended and restated, commitment raised from 3,500.0 to 4,000.0 and extended to 2031-09-30, commitment fees reduced (Q3-10Q page:24).
- 2026-09-09: PBF LLC bought two Torrance hydrogen plants and contributed them to the issuer (property of 388.4; Q3-10Q page:13).
- Martinez: full operations returned in May 2026, cumulative insurance proceeds of 1.25 billion; no insurance gain and no fire expense in Q3 2026; planned Martinez hydrocracker and Paulsboro crude unit turnarounds started in September (Q3-10Q page:15; Q3-10Q page:44). The release states they were completed in October (Q3-PR page:3), which is management language at the parent perimeter.
- Subsequent events up to the cutoff: redemption of the 800.0 of 9.875% notes on 2026-10-26 for about 853.4 plus accrued interest from cash on hand, with a loss on extinguishment of 70.4 to be booked in Q4 2026; parent dividend of $0.325 per share declared 2026-10-29, payable 2026-11-24 (Q3-10Q page:33). These are not in any 30 September balance. The registration rights agreement requires a PBF Energy shelf filing by 2026-12-31, with special interest of 0.25% then 0.50% if missed (Q3-10Q page:20).
- Chalmette: the 2026-05-08 fire is named only as a risk factor; no amount, throughput effect or insurance position is printed (see Gaps).

### Consistency with CP-0 and conflicts

1. Covenant wording. CP-0 stated that the Q3 10-Q does not restate the covenant test and listed only rates, fees, defaults and indemnification as consistent with the prior agreement. The Q3 sentence in fact says (Q3-10Q page:24 "representations, warranties and covenants by PBF Holding and the other borrowers, as well as customary events of default and indemnification obligations that are consistent with those in the Prior Credit Agreement"). It does not print the fixed charge test again, but it does say the covenants are consistent with the prior agreement. This corrects the CP-0 phrasing; the CP-0 handoff itself is not edited.
2. Borrowing base. CP-0 recorded that no borrowing base figure was supplied for liquidity. The 10-K does print a facility table with borrowing base availability of 2,296.6 at 2025-12-31 (10K page:129). The 10-Qs do not. Liquidity for 2026 dates therefore still rests on rounded narrative amounts.
3. Issuer versus parent debt, cash and operating income (CP-0 conflicts 1 to 3) remain unreconciled and are not used.
4. Distributions to members in 9M 2026: the equity statement prints 156.4 (Q3-10Q page:9) and the cash flow statement prints 156.3 (Q3-10Q page:10); a rounding-level difference that does not affect any figure here.
5. Liquidity build. At 2025-12-31 the narrative availability of more than 1.8 billion plus cash of 503.0 is consistent with the table's 2,296.6, which suggests cash is inside the table figure; at 2026-09-30 the narrative total of 5.6 billion exceeds the 4,000.0 commitment less 157.2 of letters of credit, so the build cannot be reproduced. This is recorded as a limitation, not resolved.

## Calculations

All inputs are the printed figures cited. LTM = FY2025 + year-to-date 2026 - year-to-date 2025. Year-to-date 2025 comparatives are from the 2025 columns of the same 10-Qs.

### Last-twelve-month builds

| Item | Formula with inputs | Result |
| --- | --- | --- |
| LTM revenues Q3 2026 | 29,297.7 + 31,703.8 - 22,164.3 | 38,837.2 |
| LTM income from operations | -292.6 + 3,428.0 - (-391.0) | 3,526.4 |
| LTM net income | -481.3 + 3,269.6 - (-536.2) | 3,324.5 |
| LTM insurance gains | 832.5 + 356.5 - 439.0 | 750.0 |
| LTM D&A | 602.6 + 463.0 - 463.2 | 602.4 |
| LTM interest expense, net | 186.7 + 112.6 - 145.4 | 153.9 |
| LTM EBITDA Q3 2026 | 311.3 + 3,834.6 - 73.2 | 4,072.7 |
| LTM Adjusted EBITDA Q1 2026 | 29.5 + 5.7 - (-292.7) | 327.9 |
| LTM Adjusted EBITDA Q2 2026 | 29.5 + 1,145.0 - (-282.9) | 1,457.4 |
| LTM Adjusted EBITDA Q3 2026 | 29.5 + 3,284.3 - (-191.4) | 3,505.2 |
| LTM EBITDA excluding special items Q3 2026 | -9.5 + 3,259.1 - (-221.2) | 3,470.8 |
| LTM operating cash flow Q3 2026 | -274.3 + 3,070.6 - (-575.9) | 3,372.2 |
| LTM capital outlay Q3 2026 | (687.4 + 379.5 + 77.1) + (590.0 + 305.2 + 38.6) - (401.7 + 296.6 + 52.0) = 1,144.0 + 933.8 - 750.3 | 1,327.5 |
| LTM operating cash flow less capital outlay | 3,372.2 - 1,327.5 | 2,044.7 |
| LTM cash interest paid Q1 2026 | 151.8 + 75.9 - 48.8 | 178.9 |
| LTM cash interest paid Q2 2026 | 151.8 + 91.0 - 55.4 | 187.4 |
| LTM cash interest paid Q3 2026 | 151.8 + 155.5 - 145.0 | 162.3 |

### Discrete quarters from year-to-date columns

| Item | Formula with inputs | Result |
| --- | --- | --- |
| Q2 2026 operating cash flow | 1,149.0 - (-371.2) | 1,520.2 |
| Q3 2026 operating cash flow | 3,070.6 - 1,149.0 | 1,921.6 |
| Q2 2026 capital outlay | (472.7 + 242.4 + 34.9) - 507.8 = 750.0 - 507.8 | 242.2 |
| Q3 2026 capital outlay | 933.8 - 750.0 | 183.8 |
| Q1 2026 capital outlay | 347.7 + 136.9 + 23.2 | 507.8 |
| Q2 2026 cash interest paid | 91.0 - 75.9 | 15.1 |
| Q3 2026 cash interest paid | 155.5 - 91.0 | 64.5 |
| Q4 2025 Adjusted EBITDA (cross-check only) | 29.5 - (-191.4) | 220.9 |
| Q2 plus Q3 2026 Adjusted EBITDA | 1,139.3 + 2,139.3 | 3,278.6 |
| Adjusted EBITDA outside Q2 and Q3 2026 within the LTM | 3,505.2 - 3,278.6 (equals 220.9 + 5.7) | 226.6 |

Sum checks: Q1 + Q2 + Q3 2026 Adjusted EBITDA is 5.7 + 1,139.3 + 2,139.3 = 3,284.3, equal to the printed 9M figure; revenues 7,899.8 + 11,676.3 + 12,127.7 = 31,703.8; net income 211.7 + 1,151.9 + 1,906.0 = 3,269.6; operating capital outlay 507.8 + 242.2 + 183.8 = 933.8.

### Capital outlay and operating cash flow less outlay

| Period | Capital outlay formula | Operating cash flow less outlay |
| --- | --- | --- |
| FY2024 | 384.4 + 576.7 + 40.7 = 1,001.8 | -136.8 - 1,001.8 = -1,138.6 |
| FY2025 | 687.4 + 379.5 + 77.1 = 1,144.0 | -274.3 - 1,144.0 = -1,418.3 |
| Q1 2026 | 347.7 + 136.9 + 23.2 = 507.8 | -371.2 - 507.8 = -879.0 |
| Q2 2026 | 242.2 | 1,520.2 - 242.2 = 1,278.0 |
| Q3 2026 | 183.8 | 1,921.6 - 183.8 = 1,737.8 |
| 9M 2026 | 590.0 + 305.2 + 38.6 = 933.8 | 3,070.6 - 933.8 = 2,136.8 |

### Net debt and leverage

| Date | Principal | Cash | Net debt (principal less cash) | LTM Adjusted EBITDA | Total debt / EBITDA | Net debt / EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| 2024-12-31 | 1,501.6 | 515.2 | 986.4 | -79.9 | not calculable | not calculable |
| 2025-12-31 | 2,201.6 | 503.0 | 1,698.6 | 29.5 | 2,201.6 / 29.5 = 74.6 | 1,698.6 / 29.5 = 57.6 |
| 2026-03-31 | 2,851.6 | 504.3 | 2,347.3 | 327.9 | 2,851.6 / 327.9 = 8.7 | 2,347.3 / 327.9 = 7.2 |
| 2026-06-30 | 1,800.0 | 879.7 | 920.3 | 1,457.4 | 1,800.0 / 1,457.4 = 1.2 | 920.3 / 1,457.4 = 0.6 |
| 2026-09-30 | 1,850.0 | 2,510.6 | -660.6 | 3,505.2 | 1,850.0 / 3,505.2 = 0.5 | -660.6 / 3,505.2 = -0.2 |

### Interest cover

| Period | Adjusted EBITDA | Cash interest paid | Ratio |
| --- | --- | --- | --- |
| FY2025 | 29.5 | 151.8 | 29.5 / 151.8 = 0.2 |
| LTM Q1 2026 | 327.9 | 178.9 | 327.9 / 178.9 = 1.8 |
| LTM Q2 2026 | 1,457.4 | 187.4 | 1,457.4 / 187.4 = 7.8 |
| LTM Q3 2026 | 3,505.2 | 162.3 | 3,505.2 / 162.3 = 21.6 |

### Illustrative effects of the 2026-10-26 redemption (subsequent event, not a reported balance)

| Item | Formula with inputs | Result |
| --- | --- | --- |
| Remaining principal | 1,850.0 - 800.0 (equals 550.0 + 500.0) | 1,050.0 |
| Cash after the redemption price, before accrued interest and other flows | 2,510.6 - 853.4 | 1,657.2 |
| Net debt on that basis | 1,050.0 - 1,657.2 | -607.2 |
| Coupon run-rate removed | 800.0 x 9.875% | 79.0 per year |
| Remaining fixed cash coupon | 500.0 x 7.25% (the exchangeable notes bear no regular interest) | 36.25 per year |

### Liquidity cross-checks

| Date | Commitment less drawn less letters of credit | Printed availability | Cash plus printed availability | Printed total |
| --- | --- | --- | --- | --- |
| 2025-12-31 | 3,500.0 - 100.0 - 167.3 = 3,232.7 | more than 1,800.0 (table 2,296.6) | 503.0 + 1,800.0 = 2,303.0 | about 2,300 |
| 2026-03-31 | 3,500.0 - 750.0 - 197.0 = 2,553.0 | more than 1,900.0 | 504.3 + 1,900.0 = 2,404.3 | about 2,400 |
| 2026-06-30 | 3,500.0 - 0.0 - 163.3 = 3,336.7 | about 2,700.0 | 879.7 + 2,700.0 = 3,579.7 | over 3,500 |
| 2026-09-30 | 4,000.0 - 0.0 - 157.2 = 3,842.8 | about 3,100.0 | 2,510.6 + 3,100.0 = 5,610.6 | over 5,600 |

The commitment-based figure is an upper bound, not an availability: printed availability is lower than commitment less usage on every date, consistent with a borrowing base limit. The covenant trigger cross-check: the largest possible testing amount is 10% of 4,000.0 = 400.0 (the lesser of borrowing base and commitments cannot exceed the commitment), above the 100.0 floor; printed availability of about 3,100.0 is about 2,700.0 above that, so the springing test appears not to be in effect at 2026-09-30. This is an Analyst Interpretation resting on the printed approximate availability and on a definition of Excess Availability that is not supplied.

### Derived fact checks

- Leases: operating 163.0 + 60.1 + 399.0 + 90.2 = 712.3 (Q3-10Q page:7); financing 16.1 + 12.8 = 28.9. At 2025-12-31 operating 184.2 + 141.2 + 541.4 + 114.7 = 981.5; with financing 25.8 + 12.2 = 38.0 the total is 1,019.5, matching the printed total lease liabilities.
- Adjusted EBITDA definition check, Q3 2026: EBITDA 2,092.5 + stock compensation 7.8 + RBI costs 11.0 + loss on extinguishment 28.0 = 2,139.3, equal to the printed figure. The 29.9 unrealized loss on the exchange feature is not added back, so Adjusted EBITDA is stated after that loss.
- Expense bridge: Q3 2026 12,127.7 - 10,011.1 - 125.0 - 2.6 - 0.7 = 1,988.3; 9M 2026 31,703.8 - 28,266.0 - 358.3 - 7.0 + 356.5 - 1.0 = 3,428.0; FY2025 29,297.7 - 30,091.4 - 322.0 - 8.4 + 832.5 - 1.0 = -292.6.

## Gaps

| ID | Gap | Severity | Consumers | Action |
| --- | --- | --- | --- | --- |
| H1 | Executed indentures, the amended revolving credit agreement and the definition of Excess Availability and the fixed charge ratio are not supplied (CP-0 G1); covenant headroom is Not calculable. | Medium | CP-2, CP-5 | Obtain the documents; until then use note descriptions only and make no legal reading. |
| H2 | Liquidity is printed as rounded narrative amounts; cash overlap, letters of credit netting and the 2026-09-30 build cannot be reproduced (CP-0 G4). | Medium | CP-2 | Quote as printed; request a borrowing base report. |
| H3 | Issuer total debt of 1,850.0 principal and parent total debt of 2,118.4 are unreconciled (CP-0 G2); no parent figure is used. | Medium | CP-2, CP-5 | Keep perimeters separate. |
| H4 | Company-defined EBITDA and Adjusted EBITDA include or exclude insurance gains, the LCM reversal and derivative effects in different ways; no covenant EBITDA is supplied. | Medium | CP-2 | Show both EBITDA and Adjusted EBITDA when quoting leverage. |
| H5 | Pension, purchase commitments and leases are not updated for the interim dates except the lease lines on the balance sheet. | Low | CP-2 | Use the 2025-12-31 pension and commitment figures and label them. |
| H6 | Chalmette fire of 2026-05-08: no amount, insurance position or throughput effect printed after searching the 10-Qs and releases (CP-0 G7). | Low | CP-1A, CP-2 | State Not supplied. |
| H7 | Martinez fire and catalyst release investigations are unquantified (CP-0 G8). | Medium | CP-1A, CP-2 | Carry as open contingencies with no amount. |
| H8 | Outstanding balances of the receivables facility and insurance premium financing are not printed. | Low | CP-2 | State Not supplied; flows only. |
| H9 | The Q3 release says net debt fell by 150% from Q2; this is a parent claim at another definition and was not recomputed. | Low | CP-5 | Do not adopt. |
| H10 | The 2029 call dates, change of control put and other note terms are known only from the 10-Q note text. | Low | CP-1A | Read the indentures when supplied. |

## Next module

Proceed to CP-1A. It should take the 2026 refinancing sequence, the revolver amendment, the hydrogen plants purchase, the Martinez fire and insurance history, the ownership chain and the subsequent events from the Findings above, and carry H1, H6, H7 and H10. CP-2 and CP-5 follow. CP-2 must keep the issuer perimeter, present leverage on both EBITDA definitions, state that the trailing figures depend on two quarters of strong margins, and carry H1 to H5 and H8. CP-5 should trace each derived number in Calculations to the cited statement lines and test H3, H4 and H9.
