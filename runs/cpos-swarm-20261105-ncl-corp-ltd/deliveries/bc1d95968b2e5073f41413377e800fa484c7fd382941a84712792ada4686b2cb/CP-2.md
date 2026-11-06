# CP-2 — Fundamental credit synthesis: NCL CORP Ltd. (ncl-corp-ltd)

## Request

NCL CORP Ltd. (issuer id `ncl-corp-ltd`; the filings name the registrant NCL Corporation Ltd., "NCLC"), as of 2026-11-05, pathway `credit_snapshot`, asks for the fundamental credit view from the upstream financial base and business context. Scope is NCLC and its consolidated subsidiaries in USD millions for FY2025 and the first three quarters of 2026, with no peer ranking, instrument recommendation or recovery conclusion. Execution is a host session; no provider was called.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | 1590d4030e80abfbd09d00a74521526f72070052531a8716f865a880a8fa9501 | Instrument-level debt table at December 31, 2025, revolver terms and springing maturity, covenant text, maturities schedule |
| 10-Q_2026-03-31_nclc-20260331x10q.htm.jsonl | 1693fea3f52de137a2e148c9e6f9853be5398eb34944625b7e837b2bd396c943 | Q1 2026 cash, liquidity and repayment schedule |
| 10-Q_2026-06-30_nclc-20260630x10q.htm.jsonl | 2f18ccd1a947471efb9474a7bd377c5db5871d9445b97fe0a1fc7e783f6d645f | Q2 2026 cash, liquidity and repayment schedule |
| 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | 7769d1c310cec4c8e024523931f2cd599a487768128283054dca38ddd11d7d93 | Q3 2026 liquidity, debt, capital commitments, market risk, subsequent events |
| EX-99.1_2026-05-04_exh_991.htm.jsonl | 19e48d4c7cb2b40fb1bcbfbbe436e7e39f669c8965c4e705c327d948db3f04d8 | Parent press release; perimeter label only |
| EX-99.1_2026-07-30_exh_991.htm.jsonl | ffe75efbccd58bfc3c88fabf4a188883f7003d5a095dba1da47bbe08c4d94307 | Parent press release; perimeter label only |
| EX-99.1_2026-10-29_exh_991.htm.jsonl | 6f93f8906074ef388d05f277a1b3874ed298e830f3945372d3d73a8925dc791c | Parent press release; delivery timing and pro forma liquidity, labelled parent-level |
| context | 1eac4b587c5c6cd9d96c3f400eed0e70dc9aa1137a14c30469dde7d21791294f | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 240a9004c9f054e89ac320762ee0dbd447c416d5523fbbb0826a7a829f32f3c2 | Source readiness and limitations |
| CP-1 | 0d306e620183fe5605e53df2bfa6840225b9fdf3340d4d66074ce76c6547a7b6 | Financial base: debt, leverage, interest proxies, liquidity, maturities, claims outside debt |
| CP-1A | 3ea102b4043a2f05facc314042b53d7d4ce7ff98e5ddc43910a907daf003a111 | Business, parent linkage, fleet and financing context |

Consistency with the handoffs: this answer confirms CP-1's figures and CP-1A's structure. It goes further in three places and corrects none. It adds the maturity dates of both 2027 exchangeable note series (February 15, 2027), which CP-1 listed only as 2027; it ties the springing revolver maturity of November 17, 2026 to those notes, which CP-1 recorded without the link; and it adds market-risk sensitivities from the Q3 10-Q that CP-1 did not use.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| NCL Corporation Ltd. is a leveraged cruise credit with adequate liquidity: net debt is 5.42x last-twelve-months Adjusted EBITDA, up from 5.26x, earnings are softening and a heavy newbuild program keeps free cash flow negative. | Medium | Covenant values, credit agreements and the outcome of the November 17, 2026 springing-maturity test are not supplied, and Adjusted EBITDA is a company measure. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt of 14,884.5 is 5.51x last-twelve-months Adjusted EBITDA of 2,700.1, and Q3 2026 Adjusted EBITDA was down 8.1%. | Leverage rose while earnings fell, so deleveraging depends on yield recovery. | Medium |
| Cash of 250.7 and revolver availability of about 1,100 compare with scheduled principal of 238.6 for the rest of 2026. | Near-term liquidity covers scheduled principal, before the October 2026 upsizing. | Medium |
| The revolver can mature on November 17, 2026, 12 days after the as-of date, unless the 2027 exchangeable notes are repaid or refinanced or a liquidity test is met. | A springing maturity on the main secured facility is the most time-critical open item. | Low |
| Committed ship payments are 19,421.2, with about 10,800 of export-credit facilities and three effective contracts not yet financed. | Growth spending is mostly financed but still adds debt and euro exposure. | Medium |
| Scheduled principal is 1,105.7 in 2027 and 4,134.3 in 2030. | A heavy 2030 wall follows a 2027 year in which funding needs roughly match operating cash flow. | Medium |

### Credit view

NCL Corporation Ltd. is a leveraged but liquid cruise credit whose deleveraging has stalled: net debt is 5.42x last-twelve-months Adjusted EBITDA at September 30, 2026, up from 5.26x at FY2025. The strongest support is liquidity of about USD 1,350.7 million (cash of USD 250.7 million and revolver availability of about USD 1,100 million), a revolver upsized in October 2026 and, on the December 31, 2025 debt table and the 2026 events described, no senior unsecured note maturity before 2029. The weakest point is cash generation: operating cash flow less additions to property and equipment was negative USD 582.7 million for nine months 2026 while Q3 2026 Adjusted EBITDA fell 8.1%. What decides the outcome is whether 2027 yield recovers and how the November 17, 2026 springing maturity and the amended covenants resolve; neither amendment text is supplied.

### Credit assessment

| Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- |
| Fundamental view: high leverage with adequate near-term liquidity, softening earnings, negative post-capex cash flow, long-dated mostly fixed-rate export-credit funding and an unresolved revolver springing-maturity test. Not a rating and not a recommendation. | Analyst Interpretation | Medium (below High because covenant values, agreements and the October 2026 amendment text are not supplied) | CP-1 leverage, liquidity, maturity and cash flow figures; CP-1A parent linkage, newbuild and fleet rows; Q3 10-Q market-risk and commitments pages |

### Key findings

First, leverage is high and has risen. NCLC carried balance-sheet debt of USD 14,884.5 million at September 30, 2026 against last-twelve-months Adjusted EBITDA of USD 2,700.1 million, which is 5.51x, and 5.42x net of USD 250.7 million of cash; at FY2025 the figures were 5.34x and 5.26x on USD 2,731.4 million of Adjusted EBITDA [CP-1]. Adjusted EBITDA for Q3 2026 was USD 936.7 million against USD 1,019.4 million, with Net Yield per Capacity Day at USD 319.65 against USD 341.89, so volume is growing while price per unit falls [CP-1; Q3 10-Q page:34]. The parent states net leverage of 5.5x on its own perimeter; that is a consistent but separate measure and is not used here (Documentary Fact and Analyst Interpretation).

Second, near-term liquidity is adequate on the issuer's own filings. At September 30, 2026 NCLC had cash of USD 250.7 million and revolver availability of about USD 1,100 million, which the filing totals as liquidity of about USD 1.4 billion [Q3 10-Q page:6]. Scheduled principal is USD 238.6 million for the rest of 2026 and USD 1,105.7 million in 2027 [CP-1]. In October 2026 NCLC issued USD 950.0 million of 8.750% senior unsecured notes due 2031, repaid USD 380.0 million of revolver borrowings, redeemed the 6.125% notes due 2028 and raised revolver commitments from about USD 2.5 billion to about USD 2.8 billion, which on printed figures lifts revolver availability to about USD 1,780 million (calculated); the parent's own pro forma figure is USD 1.8 billion and is parent-level [Q3 10-Q page:12; Q3 release page:3].

Third, the revolver carries a springing maturity that falls 12 days after the as-of date. The 10-K states that if on November 17, 2026 the 2027 1.125% or 2.5% exchangeable notes have not been repaid or refinanced with debt maturing after April 23, 2030 and a liquidity test is not satisfied, the commitments and loans mature on November 17, 2026 [10-K page:142]. Both series mature on February 15, 2027 and total USD 216.2 million of principal; NCLC states it expects to repay them in cash or refinance before maturity, and held USD 250.7 million of cash [Q3 10-Q page:38]. The liquidity test is not defined in the pages read, the Q3 10-Q does not restate the clause, and the October 2026 third amendment may have changed it. This is a missing datapoint, not an adverse finding, but it is the most time-sensitive item because the facility is the main liquidity backstop (Insufficient Information).

Fourth, capital commitments are large, mostly financed and partly open. Non-cancelable ship contracts total USD 19,421.2 million for 13 effective ships, with committed undrawn export-credit facilities of about USD 10.8 billion funding about 80% of most contracts; three effective contracts (Oceania Sonata Class 3 in 2032, Regent Prestige Class 3 in 2033 and Oceania Sonata Class 4 in 2035) are “Contract effective, but not yet financed” [Q3 10-Q page:20, page:41 and page:42]. Anticipated ship construction and growth spending is USD 1.1 billion for the rest of 2026, USD 3.1 billion in 2027 and USD 1.8 billion in 2028, against export-credit funding of USD 0.6 billion, USD 2.0 billion and USD 1.3 billion [Q3 10-Q page:40]. The unfunded part in 2027, USD 1.1 billion, plus scheduled principal of USD 1,105.7 million is USD 2,205.7 million, which is 1.02x last-twelve-months operating cash flow of USD 2,169.0 million (calculated, from printed rounded figures). Little room is left for deleveraging from internally generated cash in 2027 (Analyst Interpretation).

Fifth, the debt stack is long-dated and mostly fixed rate, which supports debt service but concentrates maturities. At September 30, 2026, 88% of debt was fixed and 12% variable, and a one percentage point rise in SOFR would raise annual interest expense by about USD 18.2 million [Q3 10-Q page:43]. Scheduled principal is USD 1,346.1 million in 2028, USD 1,370.0 million in 2029 and USD 4,134.3 million in 2030, which together are 44.2% of the USD 15,498.0 million total, and 2030 alone is 26.7% (calculated) [CP-1]. The October 2026 actions change those buckets: if the full USD 525.0 million of 6.125% notes was outstanding, 2028 falls to about USD 821.1 million; if the revolver sits in the 2030 bucket, repaying USD 380.0 million takes 2030 to about USD 3,754.3 million; and 2031 rises to about USD 2,825.1 million with the new notes (calculated, illustrative; the USD 42.2 million of export-credit prepayment is not allocated). The 2030 maturities include the revolver (stated maturity January 22, 2030), two exchangeable series and the 6.25% senior unsecured notes [10-K page:139 and page:142]. Interest expense, net fell to USD 564.5 million for nine months 2026 from USD 782.4 million, but about USD 202.5 million of the earlier amount was extinguishment loss, so the underlying fall was 2.7% (calculated) [CP-1].

Sixth, currency exposure is large on the capital side. Euro-denominated ship payments not hedged were EUR 14.1 billion (USD 16.0 billion) and unhedged euro debt about EUR 2.1 billion (USD 2.4 billion); a 10% change in the euro would change the dollar value of the unhedged payments by USD 1.6 billion and of the unhedged debt principal by USD 237.7 million [Q3 10-Q page:44]. The payments fall due over many years, so the effect on cash is gradual, but it moves the dollar cost of commitments that the export-credit loans only partly fund (Analyst Interpretation).

Seventh, covenant headroom cannot be measured. The 10-K names a loan to value ratio below 0.70 to 1.00, free liquidity of at least USD 250 million at all times, an EBITDA to consolidated debt service ratio of at least 1.25 to 1.00 unless free liquidity is at least USD 300 million, and a net funded debt to total capitalization ratio whose level is not printed [10-K page:41]. Compliance is stated at September 30, 2026 [Q3 10-Q page:13], but no ratio values are printed. Cash alone was USD 179.2 million at March 31, 2026 and USD 212.3 million at June 30, 2026, below the USD 250 million level, so the free-liquidity definition must count undrawn revolver capacity or similar sources; the definition is not supplied (Insufficient Information and Analyst Interpretation). The October 2026 amendment “also modified certain existing financial covenant definitions and the related collateral” [Q3 10-Q page:12].

Eighth, the issuer sits under a parent and the exchangeable notes link the two. NCLH owns all NCLC shares, guarantees the exchangeable notes on a senior unsecured basis, and the notes exchange into NCLH shares with cash up to principal and cash or shares for any excess [10-K page:144; CP-1A]. NCLH passed equity proceeds to NCLC in 2025 and no distribution to the parent appears in the periods read [CP-1A]. The Havana Docks matter names NCLH as defendant, was remanded to the Eleventh Circuit in June 2026 and is “reasonably possible but not probable” with no liability recorded; whether NCLC bears it is not stated [Q3 10-Q page:22] (Insufficient Information).

### Strengths and weaknesses

Strengths. (1) Liquidity and near-term maturities: cash of USD 250.7 million and revolver availability of about USD 1,100 million against USD 238.6 million of scheduled principal for the rest of 2026, with the revolver upsized after quarter-end (Documentary Fact; CP-1). (2) Funding model: most new ships are financed by long-dated fixed-rate export-credit loans, such as the 1.91% term loan maturing February 25, 2038 for Norwegian Luna, and about USD 10.8 billion of committed undrawn facilities remain (Documentary Fact; CP-1, Q3 10-Q page:42). (3) Fixed-rate profile: 88% of debt is fixed, so base-rate moves affect a small part of interest cost (Documentary Fact; Q3 10-Q page:43). (4) Parent support and no leakage: NCLH contributed equity proceeds in 2025 and no distributions to the parent appear in the periods read (Documentary Fact; CP-1A). (5) Operating cash flow of USD 1,709.3 million for nine months 2026 and seasonally strong third-quarter Adjusted EBITDA margin of 31.8% (Documentary Fact and calculation; CP-1). (6) Management cost and fleet actions, including run-rate savings programs and ship charters and sales, are described and under way, but are Management Language until they show in results (Management Language; CP-1A).

Weaknesses. (1) Leverage of 5.51x total and 5.42x net, higher than at FY2025 (Documentary Fact and calculation; CP-1). (2) Negative post-capex cash flow of USD 582.7 million for nine months 2026 and growth spending financed by debt (Documentary Fact and calculation; CP-1). (3) Earnings and yield softness: Q3 2026 Adjusted EBITDA down 8.1%, Net Yield lower, and a booked position that management says remains below its optimal range (Documentary Fact; CP-1, CP-1A). (4) Springing revolver maturity on November 17, 2026 with an undefined liquidity test (Insufficient Information; 10-K page:142). (5) Concentrated maturities in 2030 and an unfinanced part of the newbuild program (Documentary Fact; CP-1, Q3 10-Q page:41). (6) Currency exposure on unhedged euro payments and debt (Documentary Fact; Q3 10-Q page:44). (7) Demand concentration: about 84% of revenue from U.S.-sourced guests and customer deposits that are partly refundable (Documentary Fact; CP-1A). (8) Evidence gaps: no agreements, no covenant values, a reduced-disclosure annual report and a perimeter difference between the issuer's filings and the parent's releases (Insufficient Information; CP-0, CP-1, CP-1A).

### Debt and claims inventory

| Claim | Amount (US$m) | Date | Inside the debt figure? | Security, guarantors, maturity | Locator |
| --- | --- | --- | --- | --- | --- |
| Revolving Loan Facility (commitments approximately 2,500 at September 30, 2026; approximately 2,800 from October 2026) | 1,100.0 drawn at December 31, 2025; drawn amount at September 30, 2026 Not supplied; availability about 1,100 | Dec 31, 2025 and Sept 30, 2026 | Yes (drawn part) | Senior secured; subsidiary guarantors not named; stated maturity January 22, 2030, springing November 17, 2026 on conditions | 10-K page:139 and page:142; Q3 10-Q page:12 and page:38 |
| 1.125% exchangeable notes due 2027 | 192.0 principal; 188.3 carrying | Sept 30, 2026 | Yes | Senior unsecured; NCLH guarantor; February 15, 2027; cash settlement fixed May 2026 | Q3 10-Q page:12; 10-K page:148 |
| 2.5% exchangeable notes due 2027 | 24.1 principal; 23.7 carrying | Sept 30, 2026 | Yes | Senior unsecured; NCLH guarantor; February 15, 2027; cash settlement fixed May 2026 | Q3 10-Q page:12; 10-K page:149 |
| 0.875% exchangeable notes due 2030 | 353.9 principal; 306.2 carrying | Sept 30, 2026 | Yes | Senior unsecured; NCLH guarantor; April 15, 2030 | Q3 10-Q page:12; 10-K page:143 and page:144 |
| 0.750% exchangeable notes due 2030 | 1,407.0 principal; 1,127.2 carrying | Sept 30, 2026 | Yes | Senior unsecured; NCLH guarantor; September 15, 2030 | Q3 10-Q page:12; 10-K page:145 |
| Senior unsecured notes: 6.125% due 2028, 7.75% due 2029, 6.25% due 2030, 5.875% due 2031, 6.75% due 2032, 6.25% due 2033 | 5,237.6 carrying in total (522.6; 596.0; 311.5; 1,187.1; 1,779.6; 840.7) | Dec 31, 2025 | Yes | Senior unsecured; guarantors not stated; the 6.125% notes due 2028 were redeemed with October 2026 proceeds | 10-K page:140; Q3 10-Q page:11 |
| 8.750% senior unsecured notes due October 15, 2031 | 950.0 principal | Oct 15, 2026 (subsequent event) | Not in the September 30, 2026 figure | Senior unsecured; covenants limit liens, sale leasebacks and mergers; first call October 15, 2028 | Q3 10-Q page:11 |
| Export-credit newbuild and term loans (17 loans, including Leonardo, Seahawk, Breakaway, Vista, Allura and Prestige loans) | 6,312.1 carrying at December 31, 2025; plus the EUR 1.0 billion Norwegian Luna loan at 1.91% from March 2026 | Dec 31, 2025 and 2026 | Yes | Security by loan not stated; about USD 15 billion of net book value of assets pledged to certain debt; maturities 2027 to 2041 | 10-K page:140; Q3 10-Q page:11 and page:42 |
| Finance lease and license obligations | 8.7 | Dec 31, 2025 | Yes | Maturity 2028 | 10-K page:140 |
| Total balance-sheet debt | 14,884.5 carrying; 15,498.0 scheduled principal | Sept 30, 2026 | n/a | Instrument split at September 30, 2026 Not supplied | Q3 10-Q page:3 and page:12 |
| Operating lease liabilities | 940.3 (34.2 current, 906.1 non-current) | Sept 30, 2026 | No | Port facilities, offices, warehouses and equipment | Q3 10-Q page:10 |
| Non-cancelable ship construction contracts | 19,421.2 | Sept 30, 2026 | No | 13 effective ships; about 10.8 billion of undrawn export-credit facilities | Q3 10-Q page:20 and page:42 |
| Advance ticket sales | 3,142.0 | Sept 30, 2026 | No | Customer deposits; contract liabilities about 2.2 billion, approximately 45% refundable | Q3 10-Q page:3 and page:9 |
| Due to NCLH | 56.1 | Sept 30, 2026 | No | Parent intercompany balance | Q3 10-Q page:3 |
| Accrued interest | 181.2 | Dec 31, 2025 | No (inside accrued expenses) | Interest accrued on the debt table | 10-K page:150 |
| Shipboard Retirement Plan | Not supplied | Sept 30, 2026 | No | Unfunded defined benefit plan; obligation amount not in the pages read | Q3 10-Q page:29 |
| Litigation (Havana Docks) | Judgment of about 112.9 was entered in 2022; no liability recorded now | Sept 30, 2026 | No | Named defendant is NCLH; reasonably possible, not probable | Q3 10-Q page:22 |
| Factoring, supply-chain finance, other purchase commitments | Not supplied (searched; none found) | n/a | n/a | n/a | Q3 10-Q, whole source |

### Liquidity by facility

| Facility or source | Commitment | Drawn or used | Available (US$m) | Expiry | Locator |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | n/a | n/a | 250.7 | n/a | Q3 10-Q page:2 and page:6 |
| Revolving Loan Facility | about 2,500 at September 30, 2026 | Not supplied; about 1,400 implied by commitment less availability, including any letters of credit | about 1,100 | January 22, 2030 stated; springing November 17, 2026 on conditions | Q3 10-Q page:12 and page:38; 10-K page:142 |
| Letters of credit under the revolver | Not supplied (searched for letters of credit, LC and standby; no occurrence) | Not supplied | Not supplied | n/a | Q3 10-Q and 10-K, whole source |
| Committed undrawn export-credit facilities | about 10,800 | Not drawn | 0 usable for liquidity; restricted to ship construction | Tied to ship deliveries | Q3 10-Q page:42 |
| Liquidity, September 30, 2026 | n/a | n/a | about 1,350.7 (calculated; filing states about 1.4 billion) | n/a | Q3 10-Q page:6 |
| Pro forma October 2026 revolver availability | about 2,800 | after repaying 380.0 | about 1,780 (calculated); pro forma cash for NCLC Not supplied | n/a | Q3 10-Q page:12 and page:38 |
| Parent pro forma liquidity (parent-level, management-prepared) | n/a | n/a | 2.1 billion including about 1.8 billion of availability | n/a | Q3 release page:3 |

Facilities expiring within twelve months of the as-of date: no commitment has a stated maturity before January 22, 2030, but the revolver can spring to November 17, 2026 and the 2027 exchangeable notes (USD 216.2 million) mature on February 15, 2027.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Springing revolver maturity on November 17, 2026 | The clause accelerates the revolver if the 2027 exchangeable notes are not repaid or refinanced and a liquidity test is not met; the test and the amendment's effect are not supplied. | Loss of the main backstop would force reliance on cash of USD 250.7 million; cross-default and collateral consequences follow. | Material |
| High and rising leverage with softer earnings | Debt rose while Adjusted EBITDA fell, and yield per Capacity Day is lower. | Little cushion for further earnings decline before covenant or rating pressure; ratings are B1 and B+ per the filing. | Material |
| Negative post-capex cash flow | Operating cash flow did not cover additions to property and equipment for nine months 2026. | Debt grows with each delivery; deleveraging depends on EBITDA growth. | Material |
| Unfinanced newbuild contracts and euro exposure | Three effective contracts are not yet financed; EUR 14.1 billion of payments are unhedged. | Future funding need and dollar cost uncertainty. | Material |
| 2030 maturity concentration | USD 4,134.3 million of scheduled principal falls in 2030. | Refinancing depends on market access and ratings. | Material |
| Covenant opacity | Covenant values, definitions and the October 2026 amendment are not supplied. | Headroom cannot be monitored. | Material |
| Demand concentration and refundable deposits | About 84% of revenue from U.S.-sourced guests; customer deposits are partly refundable. | A booking shock would drain liquidity quickly. | Material |
| Parent linkage and share-price exposure of the exchangeable notes | Notes exchange into NCLH shares; NCLH guarantees them. | Settlement and support depend on the parent. | Minor |
| Contingent litigation and unfunded pension | Havana Docks exposure and the Shipboard Retirement Plan are not quantified for NCLC. | Possible claims outside debt. | Minor |

### Event calendar after the as-of date

| Date | Event | Type | Locator |
| --- | --- | --- | --- |
| November 17, 2026 | Springing maturity test date for the Revolving Loan Facility | Contract term | 10-K page:142 |
| Late December 2026 | Seven Seas Prestige delivery, delayed to late December per the parent release | Parent-level expectation | Q3 release page:2; Q3 10-Q page:40 |
| December 31, 2026 | End of the remainder-2026 scheduled principal period | Schedule | Q3 10-Q page:12 |
| January 19, 2027 | Eleventh Circuit oral argument, Havana Docks | Court date | Q3 10-Q page:22 |
| February 15, 2027 | Maturity of both 2027 exchangeable note series | Contract term | 10-K page:148 and page:149 |
| 2027 | Scheduled deliveries of Norwegian Aura and Oceania Sonata; anticipated ship construction and growth spending | Schedule | Q3 10-Q page:40 |
| September 2027 | Closing of the Oceania Insignia sale; first call date of the 5.875% notes due 2031 on September 15, 2027 | Contract term | Q3 10-Q page:24; 10-K page:146 |
| Late 2027 | Norwegian Sun charter and Seven Seas Navigator lease commence | Contract term | Q3 10-Q page:10 and page:32 |
| February 1, 2028 | First call date of the 6.750% notes due 2032 | Contract term | 10-K page:141 |
| October 15, 2028 | First call date of the 8.750% notes due 2031 | Contract term | Q3 10-Q page:11 |
| January 22, 2030 | Stated maturity of the Revolving Loan Facility | Contract term | 10-K page:142 |

## Calculations

All inputs are as printed in US$ thousands, millions or billions; amounts in prose are converted to USD millions.

### Liquidity

- Liquidity at September 30, 2026: cash 250.7 + revolver availability about 1,100 = about 1,350.7. The filing states about 1.4 billion (Q3 10-Q page:6).
- Implied revolver use: commitments about 2,500 − availability about 1,100 = about 1,400. This includes any letters of credit and is derived from rounded figures.
- Pro forma availability after October 2026: about 1,100 + commitment increase about 300 (2,800 − 2,500) + repayment 380.0 = about 1,780, consistent with the parent's 1.8 billion; pro forma cash for the issuer is Not supplied.
- Cash against the free-liquidity minimum: cash 179.2 (March 31, 2026) and 212.3 (June 30, 2026) are below 250 (10-K page:41); cash 250.7 at September 30, 2026 is above it; the covenant definition is not supplied.

### Funding of 2027 needs

- 2027 anticipated ship construction and growth spending 3.1 billion − export-credit funding 2.0 billion = 1.1 billion unfunded (Q3 10-Q page:40). Rest of 2026: 1.1 billion − 0.6 billion = 0.5 billion, plus 0.1 billion of other capital expenditure. 2028: 1.8 billion − 1.3 billion = 0.5 billion.
- 2027 unfunded spending 1,100 + scheduled principal 1,105.7 = 2,205.7; against LTM operating cash flow 2,169.0 (CP-1) the ratio is 2,205.7 / 2,169.0 = 1.02x. Illustrative: uses printed rounded plans and a trailing cash flow, not a forecast.

### Maturity and structure shares

- 2030 share: 4,134.3 / 15,498.0 = 26.7%. 2028 to 2030: (1,346.1 + 1,370.0 + 4,134.3) / 15,498.0 = 6,850.4 / 15,498.0 = 44.2%.
- December 31, 2025 composition of USD 14,583.4 million of debt: senior unsecured notes 5,237.6 (35.9%), exchangeable notes 1,925.1 (13.2%), revolver 1,100.0 (7.5%), export-credit and term loans 6,312.1 (43.3%), finance leases 8.7 (0.1%). Sum of the 29 rows equals 14,583.4 (10-K page:140). Shares calculated; they total 100.0% within rounding.
- Variable-rate debt implied by the sensitivity: 18.2 / 1% = about 1,820, which is about 12% of 14,884.5, consistent with the stated 12% (Q3 10-Q page:43). The one percentage point rise adds 18.2 / 753.1 = 2.4% to LTM interest expense, net (CP-1).

### Pro forma maturity buckets (illustrative)

- 2028: 1,346.1 − 525.0 = 821.1 (assumes the full principal named in the 10-K debt table was outstanding at September 30, 2026; the Q3 10-Q does not state the amount redeemed).
- 2030: 4,134.3 − 380.0 = 3,754.3 (assumes the revolver is shown at its 2030 maturity in the schedule, as the 10-K schedule appears to do).
- 2031: 1,875.1 + 950.0 = 2,825.1. The USD 42.2 million of export-credit prepayment is not allocated to a year.

### Interest change net of extinguishment

- 9M 2025 interest expense, net 782.4 − extinguishment 202.5 = 579.9; 9M 2026 564.5 / 579.9 − 1 = −2.7% (CP-1).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| The Revolving Loan Facility credit agreement, its liquidity test, the third amendment and the effect on the November 17, 2026 springing maturity are not supplied. | High | CP-5 and committee | Obtain the agreement and amendment; confirm whether the 2027 exchangeable notes are repaid or refinanced before November 17, 2026. |
| Covenant ratio values, covenant EBITDA and free liquidity definitions are not supplied; headroom is Not calculable. | High | CP-5 | Obtain the compliance certificate and agreement definitions. |
| The instrument-level debt table at September 30, 2026 and the security and guarantors by instrument are not supplied. | Medium | CP-5 | Rebuild from the December 31, 2025 table and the described 2026 events, flagged as derived. |
| The revolver drawn amount, letters of credit and the issuer's pro forma cash after October 2026 are not supplied. | Medium | CP-5 | Use stated availability and label the pro forma as calculated. |
| Parent and issuer debt totals and net leverage do not reconcile in the supplied text; the parent's 5.5x is not used. | Medium | CP-5 | Keep perimeters separate. |
| Governance, beneficial ownership and executive compensation are omitted by the reduced-disclosure annual report. | Medium | CP-5 | Look to parent filings; treat as parent-level. |
| Pension obligation amount and the issuer's share of the Havana Docks exposure are not quantified. | Low | CP-5 | Carry as outside-debt items. |
| Events between October 29, 2026 and 2026-11-05 are Not supplied; for example whether the 2027 exchangeable notes were repaid early. | Low | All | State as Not supplied. |
| Text extraction was not compared with the filed HTML or XBRL. | Low | CP-5 | Re-check figures that drive a conclusion. |

## Next module

CP-5 should run next to trace every material claim here to its source page and to check consistency across CP-0, CP-1, CP-1A and this answer. Carry forward: the issuer-only perimeter, the springing revolver maturity of November 17, 2026 and its linkage to the February 15, 2027 exchangeable notes, the missing agreements and covenant values, the unfinanced newbuild contracts and the derived (not printed) status of the 2027 funding ratio, pro forma availability and maturity shares.
