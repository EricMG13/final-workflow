## Request

Module CP-1A, business and transaction context, for OPENLANE, Inc. (issuer id opln, NYSE: OPLN), pathway credit_snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05, reporting currency USD. The module builds the fact pack a credit committee reads first: the business and operating model, ownership and control, dated history and transactions, new debt, sponsor-linked behaviour from documented actions, and the credit translations that follow. It gives no peer ranking, instrument recommendation or recovery conclusion. Periods follow the filings (Q3 2026, nine months 2026, FY2025); amounts are USD millions unless a line says otherwise. Figures that come from the financial base are those of the CP-1 handoff and are labelled as such.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Use |
| --- | --- | --- |
| 10-K_2025-12-31_opln-20251231.htm.jsonl | 26a1eb6e044eb7884447c1771579bc95b55527d93c8454714335cfb05faebcc7 | Business, history, customers, competition, risk factors on the Series A holders, segment and geographic notes, debt |
| 10-Q_2026-03-31_opln-20260331.htm.jsonl | c46e877ea2548ae22544a835acae1b3618984f266ca5c5f8d9f1ce170a2f3661 | Q1 2026 events (Canadian digital services tax reversal, subsequent event) |
| 10-Q_2026-06-30_opln-20260630.htm.jsonl | 47753528b639818941177074a5796fb5ee4c271e3e7cb89f9ddc4bf548a73b8f | Q2 2026 events (Series A conversion, Third Amendment exhibit) |
| 10-Q_2026-09-30_opln-20260930.htm.jsonl | 9682e191d9ec651d5722722ac8ff03e1ea87ff7ece0722d12fcb449d04d13357 | Q3 2026 operating results, securitization amendments, Series A, repurchases, subsequent event |
| EX-99.3_2026-05-05_q12026openlaneearningssl.htm.jsonl | 2fc56068f78381bd02bfbe329da47d9ab40d86ee26db869d39406949616dc5f0 | Q1 2026 slides (management language; not relied on for facts) |
| EX-99.3_2026-08-04_q22026openlaneearningssl.htm.jsonl | 458d3c1fac99aaeefe126a46b683e88ca11580e6032ddf67da49e980bf2bff5d | Q2 2026 slides (management language; not relied on for facts) |
| EX-99.3_2026-11-04_q32026openlaneearningssl.htm.jsonl | bc88d193632549ac9eb968d3349190fc1ffa3b0842d97894dce16151e37cfd9a | Q3 2026 slides: management letter, company description, revised guidance |

### Other pinned input

| Input | sha256 | Use |
| --- | --- | --- |
| context | 2fd2835b16fcd6e36fa06485261ee15d20c3a0b3f6cb56cfce407e6993d9ef70 | Run settings only; not issuer evidence. It names no sponsor, borrower, parent or guarantor, and no deal terms or ratings. Blank is not zero. |

### Handoffs

| Module | sha256 | Note |
| --- | --- | --- |
| CP-0 | 822af9f32f30d6c0feeb6f1f36ee177a40b0f0ee61b0286bf38226d8998cb018 | Source readiness. Opened and used: limitations on executed agreements, guarantors, deck charts and the December 31, 2025 collateral correction are carried here. |
| CP-1 | 27cde0aafcf9a133517adb102e5557dc8e810ad505a4dc1f22e1f42860aed45f | Financial base. Opened and used for the debt, liquidity and Adjusted EBITDA figures cited below; each such figure is labelled CP-1. |

Short names: 10-K FY2025, 10-Q Q1, 10-Q Q2, 10-Q Q3, Deck Q1, Deck Q2, Deck Q3, in the order of the source table. A locator `page:N` is the source chunk number in the pinned file, not the printed page. Quotes are exact substrings of the cited chunk. Category tags: Documentary Fact, Management Language, Analyst Interpretation, Insufficient Information.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| OPENLANE is a listed, fee-based wholesale used-vehicle marketplace with a floorplan lender attached and no sponsor named in the run context. Its main credit-relevant change is the 2025 debt-funded exit of the preferred holders, now fully converted. | Medium | Credit agreement terms, current holdings of the former preferred holders and the nature of Q3 2026 transaction costs are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Marketplace is 78% of FY2025 revenue and Finance 22%, with Finance funded largely through securitization. | Earnings come from two businesses with different risks: volume-driven fees and credit exposure to independent dealers. | High |
| Commercial vehicles sold rose 46% in Q3 2026, or 17% excluding the latest commercial customer, and yield fell to 2.5%. | Growth leans on a few commercial relationships that can be terminated for convenience, and mix shift dilutes fee yield. | Medium |
| The October 2025 term loan funded the repurchase of Series A preferred stock, and the remaining shares converted in May 2026. | Corporate debt rose but a cash-pay senior equity claim with board rights was removed. | High |
| Share repurchases continue and the program was enlarged in October 2026. | Cash returned to shareholders competes with deleveraging, and the covenant limits on distributions are not supplied. | Medium |

### Business and transaction view

OPENLANE, Inc. is a stand-alone public company, formerly KAR Auction Services, that runs a digital wholesale used-vehicle marketplace in the United States, Canada and Europe and, through AFC, a short-term floorplan lender to independent dealers. Revenue is mostly fees on volume, with a small share of vehicles bought and resold; the lender adds interest and fees, funded mainly by receivable securitizations that the CP-1 handoff shows outside the corporate debt figure. The creditor-relevant transaction record is a sequence of capital-structure steps rather than an acquisition or a buyout: a term loan drawn in October 2025 to repurchase most of the Series A preferred stock held by affiliates of Apax and Periphas, the conversion of the rest into common stock in May 2026, securitization extensions to January 2030 in September 2026, and a larger share repurchase program in October 2026. No sponsor-led buyout, merger or pending acquisition is described in the sources, and the context names no sponsor. Operationally, the quarter shows strong volume growth led by commercial consignors and a lower fee yield, which makes revenue durability depend on a small number of large consignment relationships and on off-lease supply that management expects to grow. The main restrictions on this view are that the executed credit and securitization agreements are not supplied, that the present holdings and board rights of the former preferred holders are not stated after the conversion and the August 2026 secondary offering, and that the nature of the new Q3 2026 transaction-related costs is not explained.

### Company and operating model

| Area | Fact or judgment | Category | Locator and quote |
| --- | --- | --- | --- |
| Core activity | Digital marketplace for wholesale used vehicles in the United States, Canada and Europe | Documentary Fact (the word leading is Management Language) | 10-K FY2025 page:4 "OPENLANE is a leading digital marketplace for wholesale used vehicles operating in the United States, Canada and Europe" |
| Segments | Marketplace 78% and Finance 22% of FY2025 revenues | Documentary Fact | 10-K FY2025 page:9 "Marketplace 78% and"; page:10 "Finance 22%" |
| Revenue model | Fees from buyers and sellers plus ancillary services; for most transactions the company does not take title | Documentary Fact | 10-K FY2025 page:10 "We generate revenue from fees paid by vehicle buyers and sellers, as well as through selling ancillary services" |
| Pricing | Buyer fees tiered with sale price; seller fees typically fixed | Documentary Fact | 10-K FY2025 page:10 "Our buyer fees are typically based on a tiered structure with fees increasing with the sale price of the vehicle, while seller fees are typically fixed" |
| Purchased vehicles | Vehicles bought and resold are about 2% of volume and are booked at gross price as revenue and cost of services | Documentary Fact | 10-K FY2025 page:11 "approximately 2% of the total volume of vehicles sold" |
| Volume mix | Commercial consignment about 52% of transactional volume and dealer consignment about 48% in the annual report | Documentary Fact | 10-K FY2025 page:8 "The commercial consignment business represents approximately 52% of our transactional volume" |
| Scale FY2025 | 1,472,000 vehicles sold and GMV of 28.8 billion | Documentary Fact | 10-K FY2025 page:58 "Total vehicles sold 1,472,000 1,446,000" and "GMV (in billions) $ 28.8 $ 27.1" |
| Q3 2026 volume | 475,000 vehicles sold against 372,000, GMV of 10.0 billion against 7.3 billion, auction and related fees yield 2.5% against 2.9% | Documentary Fact | 10-Q Q3 page:37 "Total vehicles sold 475,000 372,000" and "Auction and related fees yield 2.5% 2.9%" |
| Growth driver | Commercial growth came from onboarding a new private label customer and more off-lease vehicles | Documentary Fact | 10-Q Q3 page:38 "primarily due to the onboarding of a new private label customer and an increase in off-lease vehicles sold" |
| Concentration of growth | Commercial volume rose 46%, or 17% excluding the latest commercial customer | Management Language | Deck Q3 page:4 "a 46% increase in commercial volumes, or 17% excluding the addition of our latest commercial customer" |
| Yield mechanic | Lower yield from more commercial vehicles, which carry lower yields, and higher average vehicle values | Documentary Fact | 10-Q Q3 page:38 "an increased mix of commercial vehicles which carry lower yields than dealer consignment vehicles" |
| Customer terms | Customers make no binding long-term volume commitments and many agreements can be terminated for convenience; no single customer was 10% or more of revenue | Documentary Fact | 10-K FY2025 page:26 "Many of our customer agreements can be terminated by the customer for convenience on advance written notice" |
| Finance business | AFC provides inventory-secured floorplan loans to independent dealers through about 90 locations; typical loan terms are 30 to 90 days | Documentary Fact | 10-K FY2025 page:16 "Typical loan terms are 30 to 90 days" |
| Finance concentration | About 11,600 active dealers at December 31, 2025, no dealer above 2.5% of the portfolio | Documentary Fact | 10-K FY2025 page:15 "no one dealer representing greater than 2.5% of our portfolio" |
| Finance and marketplace link | About 88% of vehicles floorplanned by AFC in 2025 were bought on its marketplaces or through another wholesale channel | Documentary Fact | 10-K FY2025 page:14 "approximately 88% of the vehicles floorplanned by AFC were vehicles purchased by dealers on our marketplaces or through another wholesale channel" |
| Finance funding | About 70% to 75% of the receivable portfolio is funded through securitization facilities (see CP-1) | Documentary Fact | 10-Q Q3 page:60 "approximately 70% to 75% of AFC’s finance receivables portfolio is funded through its securitization facilities" |
| Finance quality, Q3 2026 | Delinquent receivables 0.6% of receivables managed against 0.3%; provision 1.1% of average receivables against 1.6% | Documentary Fact | 10-Q Q3 page:40 "Receivables delinquent as a percentage of total receivables managed 0.6% 0.3%" |
| Collateral sensitivity | A drop in wholesale vehicle prices would raise losses if dealers cannot meet obligations | Documentary Fact | 10-Q Q3 page:32 "A decrease in wholesale used car pricing could lead to increased losses if dealers are unable to satisfy their obligations" |
| Cost structure | About 4,800 employees; 14 vehicle logistics centers in Canada; capital spending guided at 55 to 60 for 2026 | Documentary Fact; guidance is Management Language | 10-K FY2025 page:18 "approximately 4,800 employees"; Deck Q3 page:5 "Capital Expenditures $55 to $60" |
| Asset-light claim | Management calls the model asset-light | Management Language | 10-K FY2025 page:7 "scalable and asset-light operating model" |
| Geography | FY2025 operating revenues of 1,109.2 in the U.S. and 825.3 foreign; about 52% of foreign revenue from Canada | Documentary Fact | 10-K FY2025 page:138 "Approximately 52%, 52% and 58% of our foreign operating revenues were from Canada" |
| Competition | Competition is strongest with Manheim for national commercial sellers in the U.S.; the company states it is the largest wholesale marketplace operator in Canada | Documentary Fact; the Canada statement is Management Language | 10-K FY2025 page:14 "competition is strongest with Manheim for the supply of used vehicles from national commercial sellers" |
| Seasonality | The fourth quarter typically has lower used vehicle volume | Documentary Fact | 10-Q Q3 page:33 "the fourth calendar quarter typically experiences lower used vehicle volume" |
| Tax change | Canada repealed the digital services tax retroactively on March 26, 2026; 9M 2026 Marketplace gross profit includes a 20.2 benefit, of which 15.9 is a reversal of prior periods | Documentary Fact | 10-Q Q3 page:46 "The $20.2 million benefit related to the rescission of the Canadian digital service tax" |
| Named commercial customers, contract terms and share of revenue by customer | Not supplied: the filings give no customer names or per-customer revenue | Insufficient Information | 10-K FY2025 page:26. This matters because commercial growth leans on onboarding events |

### Company profile

| Item | Value | Category | Locator and quote |
| --- | --- | --- | --- |
| Registrant | OPENLANE, Inc. (f/k/a KAR Auction Services, Inc.), Delaware | Documentary Fact | 10-K FY2025 page:4 "OPENLANE, Inc. (f/k/a KAR Auction Services, Inc.)" |
| Headquarters | Carmel, Indiana | Documentary Fact | 10-Q Q3 page:1 "11299 N. Illinois Street, Suite 500, Carmel, Indiana 46032" |
| Listing | Common stock on the New York Stock Exchange as OPLN; the symbol changed from KAR in December 2025 | Documentary Fact | 10-K FY2025 page:6 "the Company changed its NYSE ticker symbol from “KAR” to “OPLN,”" |
| Filer status | Large accelerated filer, fiscal year ending December 31 | Documentary Fact | 10-Q Q3 page:1 "Large accelerated filer ☒" |
| Sector and country | Retail-Auto Dealers & Gasoline Stations; United States (context classification, not issuer evidence) | Insufficient Information | Context |
| Shares outstanding | 121,414,234 common shares at October 31, 2026 | Documentary Fact | 10-Q Q3 page:1 "121,414,234 shares of the registrant's common stock" |
| Leadership | Peter Kelly is chief executive officer; Bradley Herring is executive vice president and chief financial officer | Documentary Fact | Deck Q3 page:4 "Peter Kelly, CEO"; 10-Q Q3 page:71 "Bradley Herring" |
| Auditor | KPMG LLP, Indianapolis; unqualified opinion on FY2025 statements | Documentary Fact | 10-K FY2025 page:88 "KPMG LLP, Indianapolis, IN, Auditor Firm ID: 185" |
| Employees | About 4,800 at December 31, 2025, none under collective bargaining agreements | Documentary Fact | 10-K FY2025 page:18 "None of our employees participate in collective bargaining agreements" |
| Credit agent | JPMorgan Chase Bank, N.A. is administrative agent under the Credit Agreement | Documentary Fact | 10-K FY2025 page:4 "JPMorgan Chase Bank, N.A., as administrative agent" |
| Sponsor | The context names none; the filings describe Apax and Periphas affiliates as former preferred holders, not as a controlling sponsor | Analyst Interpretation | 10-Q Q3 page:22 "an affiliate of Ignition Parent LP (“Apax”) and an affiliate of Periphas Capital GP, LLC (“Periphas”)" |
| Credit ratings | Not supplied: the context and filings give no rating | Insufficient Information | Context |

### Transaction summary and new debt issues

On October 8, 2025 the company entered into a Second Amendment to its Credit Agreement that added incremental term loans of 550.0, due October 2032, priced at Adjusted Term SOFR plus 2.50%, issued at a discount of 2.7 with about 6.1 of debt issuance costs capitalized, and repayable in quarterly installments of 0.25% of the original principal that began on March 31, 2026 (10-Q Q3 page:18). The proceeds were used to finance the repurchase of Series A preferred stock and related fees and expenses. In October 2025 the company repurchased 334,028 Series A shares from affiliates of Apax and Periphas for about 559.3, recorded a deemed dividend of about 242.2 against the carrying amount, and later paid 5.6 of excise tax in the second quarter of 2026 (10-Q Q3 page:22). In May 2026 the holders elected to convert the remaining 300,277 Series A shares into 17,103,116 shares of common stock, a non-cash transaction, and the series was eliminated (10-Q Q3 page:22 and page:23). The earlier debt events are a January 2024 First Amendment that added a C$175 million Canadian revolver, the June 2025 repayment at maturity of the 5.125% senior notes with 210.0 of cash, and the 2023 Credit Agreement with a $325 million revolver due June 23, 2028 (10-Q Q3 page:18; 10-K FY2025 page:4 and page:75). In September 2026 the U.S. securitization facility (committed liquidity of 2.0 billion) and the Canadian facility (C$500 million) were each extended from January 31, 2028 to January 31, 2030, with about 12.5 of costs capitalized, a 0.7 pretax loss on extinguishment recorded, and about 58 of incremental borrowing (10-Q Q3 page:15, page:56 and page:57). The exhibit index lists a Third Amendment to the Credit Agreement dated June 30, 2026 and a Second Amendment to the Tenth Amended and Restated Receivables Purchase Agreement dated September 25, 2026; the debt note does not describe the Third Amendment, so its terms are Not supplied (10-Q Q3 page:68 and page:69). The debt stack, maturities and leverage are in the CP-1 handoff and are not repeated. No acquisition, merger, sponsor transaction, new bond issue or rating event is described in the sources up to November 4, 2026. After the quarter, in October 2026, the board raised the share repurchase program from 250 to 400 and extended it to December 31, 2027, and 306,334 shares were repurchased for 11.1 (10-Q Q3 page:27). On November 4, 2026 management raised its 2026 Adjusted EBITDA guidance to 390 to 400 from 385 to 400, which is a management claim and not a filed fact (Deck Q3 page:5).

### Ownership and control

| Holder or class | Fact | Category | Locator and quote |
| --- | --- | --- | --- |
| Common stock | 121,720,568 shares issued and outstanding at September 30, 2026 | Documentary Fact | 10-Q Q3 page:3 "September 30, 2026: 121,720,568" |
| Series A preferred, history | 550,000 shares sold in June 2020 for about 550 to affiliates of Apax and Periphas; 7% cumulative dividend; about 14% of common on an as-converted basis at December 31, 2025 | Documentary Fact | 10-K FY2025 page:43 "representing approximately 14% of our outstanding common stock"; 10-Q Q3 page:22 "an aggregate of 550,000 shares" |
| Control rights while outstanding | Separate class vote to amend organizational documents adversely or issue equal or senior securities; one board designee for Apax while it holds at least 50% of its initial shares on an as-converted basis | Documentary Fact | 10-K FY2025 page:44 "Apax and its affiliates will have the right to designate one director to our board of directors" |
| Series A status now | Eliminated by Certificate of Elimination in the second quarter of 2026; no shares outstanding at September 30, 2026 | Documentary Fact | 10-Q Q3 page:23 "there were no Series A Preferred Stock shares outstanding" |
| Apax secondary offering | In August 2026 an Apax affiliate sold shares in a registered secondary offering; the company repurchased 727,590 shares from the underwriter at 34.36 per share, about 25 | Documentary Fact | 10-Q Q3 page:66 "a registered public secondary offering by an affiliate of Apax" |
| Holdings and board seat after conversion | Not supplied: the percentage still held by Apax and Periphas affiliates and whether the board designation right continues are not stated in the pack | Insufficient Information | 10-Q Q3 page:66. This matters because the right depends on a holding threshold |
| Dividend recapitalisation history | None described; the preferred repurchase is a debt-funded payment to holders and is covered under behaviour below | Insufficient Information | Not applicable |
| Common dividends and management ownership | Not supplied: no common dividend policy or insider ownership appears in the text read; the proxy statement is not in the pack | Insufficient Information | Not applicable |

### Dated timeline

| Date | Event | Category | Locator and quote |
| --- | --- | --- | --- |
| 2006 and 2009 | KAR was incorporated in 2006 and became public in 2009 | Documentary Fact | 10-K FY2025 page:5 "KAR, which was incorporated in 2006 and became public in 2009" |
| 2019 and 2022 | Tax-free spin-off of IAA in 2019; sale of ADESA’s U.S. physical assets in 2022 | Documentary Fact | 10-K FY2025 page:5 "a successful tax-free spin-off of IAA in 2019" |
| 2023 | Rebrand to OPENLANE; Credit Agreement dated June 23, 2023 | Documentary Fact | 10-K FY2025 page:5 "KAR rebranded to “OPENLANE,” in 2023" |
| December 2023 | Manheim Canada acquisition | Documentary Fact | 10-K FY2025 page:61 "December 2023 Manheim Canada acquisition" |
| December 2024 | Sale of the automotive key business, pretax gain of about 31.6 | Documentary Fact | 10-K FY2025 page:61 "In December 2024, the Company completed the sale of its automotive key business" |
| April 2025 | Sale of excess Montreal property, loss of about 7.0 in the second quarter of 2025 | Documentary Fact | 10-K FY2025 page:61 "In April 2025, the Company closed on the sale of excess property in Montreal" |
| June 2025 | Repayment of 210.0 of 5.125% senior notes at maturity | Documentary Fact | 10-K FY2025 page:75 "The Company repaid the outstanding $210.0 million of senior" |
| October 2025 | Second Amendment: 550.0 incremental term loans; repurchase of 334,028 Series A shares | Documentary Fact | 10-Q Q3 page:22 "In October 2025, OPENLANE completed the repurchase of 334,028 shares" |
| November 2025 | Canadian securitization commitment raised from C$375 million to C$500 million | Documentary Fact | 10-K FY2025 page:77 "from C$375 million to C$500 million" |
| December 2025 | Ticker changed from KAR to OPLN | Documentary Fact | 10-K FY2025 page:6 "In December 2025, the Company changed its NYSE ticker symbol" |
| March 26, 2026 | Canada enacted repeal of the digital services tax, retroactive | Documentary Fact | 10-Q Q3 page:46 "On March 26, 2026, Canada enacted a bill (C-15) including the repeal of the Canadian DST" |
| May 2026 | Remaining Series A converted into common stock | Documentary Fact | 10-Q Q3 page:22 "In May 2026, the holders of the Series A Preferred Stock elected to convert" |
| June 30, 2026 | Third Amendment to the Credit Agreement (terms not described) | Insufficient Information | 10-Q Q3 page:68 "Third Amendment Agreement, dated as of June 30, 2026" |
| August 2026 | Apax affiliate secondary offering; company repurchase from the underwriter | Documentary Fact | 10-Q Q3 page:66 "in connection with a registered public secondary offering" |
| September 2026 | U.S. and Canadian securitization facilities extended to January 31, 2030 | Documentary Fact | 10-Q Q3 page:15 "from January 31, 2028 to January 31, 2030" |
| October 2026 (subsequent event) | Repurchase program raised from 250 to 400 and extended to December 31, 2027 | Documentary Fact | 10-Q Q3 page:27 "an additional $150 million to $400 million" |
| November 4, 2026 | Q3 2026 results and revised 2026 guidance | Management Language | Deck Q3 page:5 "Revised Guidance (November 4, 2026)" |

### Governance and sponsor-linked behaviour

Assessment is of issuer-level actions, never individuals, and uses documented actions only. No score is stated.

| Documented action | Behaviour category | Mechanic | Legal capacity, willingness, feasibility | Evidence quality | Dimension informed |
| --- | --- | --- | --- | --- | --- |
| October 2025 term loan used to repurchase 334,028 Series A shares for about 559.3 (10-Q Q3 page:22 "The shares of Series A Preferred Stock were repurchased primarily with proceeds from the 2025 Incremental Term Loans") | Neutral or Mixed | A debt-funded payment to preferred holders raised senior secured corporate debt by 550.0 (CP-1 debt table), which is the pattern of a debt-funded distribution. It also retired a 7% cumulative senior equity claim with class votes and a board designation right, and a deemed dividend of about 242.2 shows the price exceeded carrying value | Capacity: permitted under the Second Amendment, whose text is not supplied. Willingness: documented. Feasibility: corporate leverage stayed low on the CP-1 measure | High (primary, dated, issuer-specific) | Financial policy |
| May 2026 conversion of the remaining 300,277 Series A shares into 17,103,116 common shares | Supportive, noting that it was the holders’ election | A non-cash conversion removed the liquidation preference and the cash dividend (5.3 paid in 9M 2026 against 33.3 in 9M 2025) without new debt | Capacity: holder right under the Certificate of Designations. Willingness: holder choice. Feasibility: not a company cash decision | High | Capital structure |
| Share repurchases of 91.5 in 9M 2026 against 35.8, including 727,590 shares from the underwriter in the August 2026 Apax secondary, and the October 2026 increase of the program to 400 | Neutral or Mixed | Cash returned to common holders competes with deleveraging and funds the exit of a large holder at the offering price of 34.36 | Capacity: restricted-payment baskets Not supplied. Willingness: authorization enlarged. Feasibility: cash 244.9 and undrawn revolver 405.3 (CP-1) | High | Financial policy |
| September 2026 extension of both securitization facilities to January 31, 2030 at a cost of about 12.5 | Supportive | Longer committed funding lowers refinancing risk for the Finance receivables | Capacity: lender consent obtained. Willingness: documented. Feasibility: committed liquidity of 2.0 billion and C$500 million | High | Refinancing |
| Disclosure: quarterly covenant ratio, Adjusted EBITDA reconciliations, and a correction of an error in the December 31, 2025 collateral figure first given in the annual report | Neutral or Mixed | Transparent reporting of the covenant ratio and LTM bridges supports monitoring; the correction (10-Q Q3 page:16) shows a disclosed error in a funding-related number | Capacity not applicable. Willingness: disclosed. Feasibility: not applicable | High | Disclosure |
| Priming, uptiering, drop-down, non-pro-rata exchange or collateral release | Insufficient Information | None is described in the text read, which is not a clean finding because the executed agreements are not supplied | Not supplied | Insufficient | Creditor protection |

### Operating drivers and monitoring items

| Driver | Q3 2026 | Q3 2025 | Locator |
| --- | --- | --- | --- |
| Commercial vehicles sold | 270,000 | 185,000 | 10-Q Q3 page:37 |
| Dealer consignment vehicles sold | 205,000 | 187,000 | 10-Q Q3 page:37 |
| Marketplace GMV (billions) | 10.0 | 7.3 | 10-Q Q3 page:37 |
| Auction and related fees yield | 2.5% | 2.9% | 10-Q Q3 page:37 |
| Marketplace operating profit | 28.9 | 18.2 | 10-Q Q3 page:37 |
| Finance loan transaction units | 454,000 | 425,000 | 10-Q Q3 page:40 |
| Total receivables managed | 2,763.5 | 2,489.3 | 10-Q Q3 page:40 |
| Finance operating profit | 41.5 | 36.8 | 10-Q Q3 page:40 |

Monitoring items the source set lacks, with severity: debt maturity schedule at September 30, 2026 (Low, derived in CP-1); covenant compliance certificate and Credit Agreement definitions (High for legal work); securitization borrowing base and facility-level balances (Medium); the add-back bridge from company Adjusted EBITDA to covenant EBITDA (Medium); customer-level concentration for commercial consignors (Medium).

### Conflicts logged (not reconciled)

| Item | Source A and quote | Source B and quote | Downstream effect |
| --- | --- | --- | --- |
| Receivables serving as security at December 31, 2025 | 10-K FY2025 page:77 "$2,803.5 million and $2,335.1 million, respectively" | 10-Q Q3 page:16 "reflects the correction of an error from the $2,803.5 million previously disclosed in the 2025 Form 10-K" | Finance funding facts for that date use the later filing, with both logged; the annual report is not restated |
| Count of AFC dealers | 10-K FY2025 page:15 "AFC had approximately 11,600 active dealers" | 10-Q Q3 page:32 "approximately 15,000 unique independent dealers" | Different bases (active at year-end against unique during 2025); both are kept and neither is chosen |
| Annual vehicle scale | 10-K FY2025 page:4 "approximately 1.5 million annual vehicle transactions" | Deck Q3 page:4 "Total vehicles sold and gross merchandise value are TTM (trailing twelve months) data" | Different periods (FY2025 against trailing twelve months to September 30, 2026); the deck is management language and the filing controls |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence |
| --- | --- | --- | --- | --- |
| Revenue durability | Commercial consignors are about 52% of volume, customers can terminate for convenience, and 46% commercial growth falls to 17% excluding the latest customer (10-K FY2025 page:26; Deck Q3 page:4) | Volume rests on large consignment relationships without binding commitments, so one loss or win moves auction and SaaS revenue before costs adjust | Revenue visibility is moderate; monitor customer onboarding and loss events and the off-lease supply trend | No single customer was 10% or more of revenue (10-K FY2025 page:138) |
| Margin and cash conversion | Yield fell to 2.5% from 2.9% on commercial mix, while 9M 2026 gross profit includes a 20.2 Canadian tax benefit (10-Q Q3 pages:38, 46) | Mix dilutes fee per vehicle and the tax reversal is not repeatable, so reported margin overstates the run-rate | Margin resilience should be judged excluding the reversal; the CP-1 Adjusted EBITDA already removes the 15.9 prior-year part but not the 4.3 current-period part | Marketplace gross margin was 31.3% against 30.7% in Q3 2026 (10-Q Q3 page:39) |
| Funding structure | Finance is funded 70% to 75% through securitization and is 48.3% of LTM Adjusted EBITDA (CP-1) | Earnings depend on dealer credit quality and wholesale prices, and on continued access to committed securitization funding | Liquidity and refinancing risk sit in the facilities extended to January 31, 2030; credit losses are the swing factor | The Dec 31, 2025 collateral conflict above means collateral coverage must use the corrected figure |
| Sponsor alignment | Debt-funded preferred repurchase then conversion, and rising buybacks (10-Q Q3 pages:22, 66) | Capital returns compete with deleveraging and rely on baskets not supplied | Leverage tolerance is untested beyond the current low corporate leverage; monitor distributions | The conversion removed a cash-pay senior equity claim |
| Key uncertainties | Third Amendment terms, post-conversion holdings, nature of 1.7 of Q3 2026 transaction-related costs, and an unspecified change in the competitive landscape cited by management (Deck Q3 page:4) | Unknown terms and events could change covenant room or competitive position | Treat as open diligence items, not adverse conclusions | None |

### Consumer readiness

| Consumer | Readiness | What it should take from this handoff | Gap | Action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Two-segment structure, customer terms, yield mechanics, the sequence of capital actions, governance table and the logged conflicts | Executed agreements and the current holdings of the former preferred holders are Not supplied | Carry the gaps as restrictions on covenant and sponsor statements |
| CP-5 | READY_WITH_LIMITATIONS | Quotes with locators for every documentary fact; categories separate management language from filed fact | Deck charts are not extracted | Trace deck claims only to the cited text |

## Calculations

No new financial calculation is made in this module, apart from the sum of the two securitization amendment costs: 10.7 for the U.S. facility plus 1.8 for the Canadian facility is 12.5 (10-Q Q3 page:15). Figures that originate in the CP-1 handoff (the 48.3% Finance share of LTM Adjusted EBITDA from 185.0 over 382.7, the debt stack, the 70% to 75% funding range and the 650.2 liquidity) are cited as CP-1 facts and not recomputed. Two derived reads are stated in words only: commercial vehicles were 270,000 of 475,000 sold in Q3 2026 and 185,000 of 372,000 in Q3 2025 (10-Q Q3 page:37), so the commercial share is higher in Q3 2026 than a year earlier; and the 46% commercial growth in the deck falls to 17% when the latest commercial customer is excluded, a deck claim the filings do not break out.

## Gaps

| ID | Gap | Severity | Affected | Action |
| --- | --- | --- | --- | --- |
| G1 | The executed Credit Agreement and amendments, including the Third Amendment of June 30, 2026, and the securitization agreements are not supplied. Restricted-payment and incurrence baskets are Not supplied. | High for legal work | Governance, covenant context | Supply the executed agreements |
| G2 | Current holdings of Apax and Periphas affiliates after the conversion and the August 2026 secondary offering, and any continuing board designation right, are not stated. | Medium | Ownership and control | Supply the 2026 proxy statement or Schedule 13D and 13G filings |
| G3 | The nature of the 1.7 of Q3 2026 transaction-related costs and of the change in the competitive landscape management cites is not explained. | Low to Medium | Transactions, competitive position | Supply the Q3 2026 earnings call transcript or 8-K |
| G4 | No customer names, concentration or contract terms for commercial consignors, beyond the statement that no customer reached 10% of revenue. | Medium | Revenue durability | Supply customer disclosure if available |
| G5 | Deck charts and per-quarter operating metrics are not in the extracted text. | Low | Operating metrics | Use the 10-Q tables |
| G6 | The December 31, 2025 collateral figure conflict is logged, not reconciled. | Medium | Finance funding facts | Cite both |
| G7 | Sector and country come from the context and not from issuer evidence; no ratings, market prices or peers are supplied. | Low | Profile | Keep Not supplied |
| G8 | Nothing after November 4, 2026 is supplied. | Low | Events to the cutoff | Supply later 8-Ks or confirm none |

## Next module

- CP-2: use the two-segment model, the volume and yield mechanics, the capital-action sequence and the governance table as inputs; keep the preferred repurchase and rising buybacks as Neutral or Mixed behaviour; carry G1, G2 and G4 as limits on covenant, sponsor and revenue-durability statements; use the corrected December 31, 2025 collateral figure.
- CP-5: trace each documentary fact to its locator and quote; treat deck statements (guidance, the 46% and 17% commercial growth, the competitive-landscape remark) as management language.
