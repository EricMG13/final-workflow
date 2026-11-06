## Request

Issuer: Allison Transmission Holdings Inc (issuer id alsn, NYSE: ALSN), as of 2026-11-05, evidence cutoff 2026-11-05. Pathway credit_snapshot, reporting currency USD, amounts in US$ millions as printed. Current period q3-2026, prior period fy-2025.

Task: build the business and transaction fact pack a credit committee reads first: what the company does and how it earns, who owns and controls it, what the January 2026 acquisition and its financing changed, how the issuer has behaved toward creditors and shareholders, and what the sources do not show. Figures that come from the financial base handoff are used exactly as stated there and are marked as such.

Perimeter: the reporting entity is Allison Transmission Holdings, Inc. (consolidated). Allison Transmission, Inc. (ATI) is its wholly-owned subsidiary and the issuer of the senior notes and borrower under the credit facility (S4 page:19). Context names no sponsor, parent or guarantor; the context fields are blank and are read as not supplied, not as none.

Locator convention: S1 to S7 are the sources listed below; `page:N` is the chunk number of the extracted text, not the printed page. Quotes are exact substrings of the page text with line breaks collapsed. Each fact row carries one category: Documentary Fact, Management Language, Analyst Interpretation or Insufficient Information.

## Sources

### Issuer sources relied on

| Id | Exact name | sha256 | Use in this handoff |
| --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_alsn-20251231.htm.jsonl | 4759ff666c33cf9b4aa9fc9af406b5ff948ca8c7e8b83ef1d1b8c3371ee474c1 | Business description, customers, suppliers, labor, licence, FY2025 debt and subsequent events |
| S2 | 10-Q_2026-03-31_alsn-20260331.htm.jsonl | be0a328aec24e49cdf0300569cba1bccab7cce3c7f95d5658c5db76418cb7b3d | First quarter 2026 acquisition note and pro forma information |
| S3 | 10-Q_2026-06-30_alsn-20260630.htm.jsonl | 0d35855e179d244457d2146b580b35b12b14abea216ea0bdfab3dfa942713609 | Second quarter 2026 acquisition note and pro forma information |
| S4 | 10-Q_2026-09-30_alsn-20260930.htm.jsonl | 45fe422f6a742d85a38f1278f190cb497541b353ed938208d565068e9ab989b0 | Primary source: segments, end markets, acquisition accounting, debt, ratings, shares |
| S5 | EX-99.1_2026-05-04_d138525dex991.htm.jsonl | fe207b266e861065ca33402f15b822e8bf63e3f1f6c76c7ba33719a7889867e5 | First quarter release: management leverage target, dividend and repayment statements |
| S6 | EX-99.1_2026-08-03_d95413dex991.htm.jsonl | 351a085e364488314b64d2b881181e5b5b95879fe010b71d75af6ac7e45fdd04 | Second quarter release: revolver repayment, guidance |
| S7 | EX-99.1_2026-11-02_d187329dex991.htm.jsonl | b8087f0341293bcafb0ca28c8fc71ee181a5c666b45fe74a0ca9cfe109b0ba65 | Third quarter release: segment results, seasonality, guidance |

Run settings, not issuer evidence: context file 1411207-allison-transmission-holdings-inc-alsn.json, sha256 f65312705cd8bb204fde9755509326ba975099b166b8d246c949fcd0ea955b5a.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 944a1fdb32b0e105bdb98bcce7fe9920a9ab8a1870c238bf911cb1860242755e |
| CP-1 | b27b50a0994fa47ab4bf54e7b8dd4dd25bcc010c8d3d2635214f68fda996a5d1 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Allison is a market-leading maker of commercial and defense transmissions that bought a lower-margin off-highway business on 2026-01-01 using 2,000 of new debt. It is publicly owned, has paid down debt since closing, and keeps returning cash to shareholders. | High | The sale agreement, credit agreement, indentures and the target leverage definition are not in the pack, so legal capacity and the pace of deleveraging rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The legacy transmission business earns a much higher margin than the acquired off-highway business, which is now 42.6% of third quarter net sales. | Consolidated margins have fallen and group earnings now depend more on a lower-margin, cyclical business. | High |
| The acquisition was financed with 500 of new notes, a 1,200 term loan and a 300 revolver draw, plus cash; the revolver has since been repaid. | Acquisition debt is largely long-dated and secured or fixed, with the first maturity in 2027. | High |
| Management has a net leverage target of 2.0x but the pack does not define it, while dividends and buybacks continue. | Deleveraging pace is a management intention, not a covenant; shareholder returns compete with debt reduction. | Medium |
| Earlier source-readiness and financial base notes said no pro forma figures existed; each quarterly report in fact gives unaudited pro forma net sales and net income. | Pro forma earnings before interest and depreciation are still missing, so combined leverage remains uncomputable. | High |

### Business and transaction view

The credit is a leading but cyclical industrial supplier that has become materially larger and more diversified through a debt-funded acquisition. The legacy Allison Transmission unit makes fully automatic transmissions for medium- and heavy-duty commercial vehicles and for medium and heavy tactical defense vehicles, sells mainly through long-term agreements with a concentrated group of OEMs, and earns margins far above the acquired Allison Off-Highway unit. The January 2026 acquisition of Dana Incorporated's off-highway business was paid for with new notes at ATI, a new secured term loan, a revolver draw and cash on hand, and added two reportable segments, a much larger global manufacturing footprint and a lower-margin, more cyclical earnings stream. For creditors, the mechanics that matter are: a high-margin core with long-term customer agreements and an aftermarket cushion; a customer base where the top five OEMs were over half of sales before the acquisition; a lower-margin acquired unit with preliminary purchase accounting and open integration costs; and secured acquisition debt that sits ahead of fixed-rate unsecured notes. The issuer is publicly held with no sponsor in the pack, and its documented behaviour since closing is to repay debt (revolver repaid, partial note redemption) while continuing dividends and buybacks, which is mixed rather than extraction-oriented. Legal capacity to change that behaviour cannot be judged because the debt documents are not supplied. This handoff also corrects the earlier handoffs on pro forma information, set out in the correction section below.

### Company and operating model

| Dimension | Description | Category | Locator and exact quote | Credit relevance |
| --- | --- | --- | --- | --- |
| Core activities | Designs and manufactures fully automatic transmissions and, since 2026-01-01, off-highway drivetrain and motion systems | Documentary Fact | S1 page:5: "We are the world’s largest manufacturer of fully automatic transmissions for medium- and heavy-duty commercial vehicles" | Market position supports pricing and share retention; the claim is the company's own |
| Business units | Two reportable segments: Allison Transmission and Allison Off-Highway | Documentary Fact | S4 page:5: "operates through two operating and reportable segments" | Segment results diverge sharply, so consolidated ratios hide mix |
| Legacy end markets | North America on-highway, outside North America on-highway, global off-highway, defense, service parts and support equipment; 9M 2026 segment sales 2,474, of which North America on-highway 1,267 and defense 280 | Documentary Fact | S4 page:13: "North America On-Highway $ 462 $ 327 $ 1,267 $ 1,179" | North America trucks drive the cycle; defense is a counter-cycle cushion |
| Acquired end markets | Construction and material handling, agriculture, industrial, mining, service parts and specialty; third quarter 653 of segment sales | Documentary Fact | S4 page:13 end-market table and S4 page:43 segment table | Adds exposure to construction, agriculture, industrial and mining cycles |
| Demand tone | Management says demand in the industrial and agriculture end markets remained subdued | Management Language | S7 page:1: "demand within the Industrial and Agriculture end markets remained subdued" | Management characterisation; two of the acquired unit's five end markets |
| Geography | About 76% of FY2025 revenue in North America before the acquisition; acquired plants widen the footprint | Documentary Fact | S1 page:5: "approximately 76% of our revenues being generated in North America in 2025" | Acquisition lowers North American concentration; the post-acquisition split is not supplied |
| Customers | Top five OEM customers 52% of FY2025 net sales; Daimler AG 18%, PACCAR Inc. 11%, Traton SE 10% | Documentary Fact | S1 page:28: "our top five OEM customers accounted for approximately 52%, 55% and 52% of our net sales, respectively" | Concentration risk; figures are before the acquisition and not updated |
| Revenue model | Sales of propulsion solutions, service parts, support equipment, defense kits, engineering services, royalties and extended coverage to OEMs, distributors and the U.S. government | Documentary Fact | S1 page:58: "We generate our net sales primarily from the sale of vehicle propulsion solutions, service and component parts, support equipment, defense kits, engineering services, royalties and extended transmission coverage" | Diversified revenue lines but volume driven |
| Revenue visibility | OEM long-term agreements covering over 90% of North American on-highway unit volume, typically three to five years, with pricing and commodity cost sharing | Documentary Fact | S1 page:8: "OEM customers representing over 90% of our North American on-highway unit volume participated in long-term agreements" | Supports pricing and cost pass-through; agreements set commitment levels, not committed volume |
| Pricing | Price increases on certain products cited as a driver in 2026 quarters | Documentary Fact | S4 page:35: "price increases on certain products" | Pricing offsets material cost pressure; sustainability not evidenced |
| Aftermarket | Service parts, support equipment and other, described by management as a relatively stable source of revenue | Management Language | S1 page:12: "relatively stable source of revenues" | Cushion in downturns; stability is management's characterisation |
| Cost structure | Direct material about 65%, overhead about 29%, direct labor about 6% of cost of sales for 9M 2026 | Documentary Fact | S4 page:34: "direct material costs were approximately 65%, overhead costs were approximately 29%, and direct labor costs were approximately 6% of cost of sales" | Material-heavy cost base; commodity exposure managed by agreements |
| Suppliers | About $1,022 million of direct materials and components bought from outside suppliers in FY2025 | Documentary Fact | S1 page:15: "we purchased approximately $1,022 million of direct materials and components from outside suppliers" | Supply disruption risk; figure pre-acquisition |
| Labor | About 49% of U.S. employees union-represented; UAW Local 933 agreement effective through November 2027 | Documentary Fact | S1 page:28: "Our current collective bargaining agreement with UAW Local 933 is effective through November 2027." | Contract expiry in 2027 coincides with the first debt maturity |
| Capital spending | Additions of long-lived assets 149 for 9M 2026 against 101 for 9M 2025; full-year guidance 240 to 260 | Documentary Fact | CP-1 handoff financial table; S7 page:4 for guidance | Capex rising with the larger asset base |
| Seasonality | Acquired unit's third quarter is customarily its softest, affected by European holidays | Management Language | S7 page:1: "represents the softest quarter of the year" | Third quarter understates the acquired unit's run rate |
| Margin profile | Third quarter Adjusted EBITDA margin 37.8% for Allison Transmission and 12.7% for Allison Off-Highway | Documentary Fact | S7 page:10 segment reconciliation | Mix shift is the main driver of lower group margin |

### Company profile

| Item | Value | Category | Locator |
| --- | --- | --- | --- |
| Legal name | Allison Transmission Holdings, Inc. | Documentary Fact | S4 page:1 |
| Listing | Common stock, NYSE, symbol ALSN | Documentary Fact | S4 page:1 |
| Headquarters and founding | Indianapolis, Indiana; business founded in 1915 | Documentary Fact | S1 page:56: "The business was founded in 1915 and has been headquartered in Indianapolis, Indiana since inception." |
| Sector and country | Motor Vehicle Parts and Accessories; United States (context setting, not issuer evidence) | Documentary Fact | Context file |
| Fiscal year end and currency | 31 December; USD | Documentary Fact | S1 page:1; S4 page:51 |
| Shares outstanding | 82,133,940 at 2026-10-22 | Documentary Fact | S4 page:1 |
| Ownership | Public company; holders of five percent or more are in the proxy statement, which is not in the pack | Insufficient Information | S1 page:123: "Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters" |
| Sponsor | None named in context or sources | Insufficient Information | Context file |
| Employees | About 4,000 at 2025-12-31, 87% in the U.S., before the acquisition; post-acquisition headcount not supplied | Documentary Fact | S1 page:115 |
| Acquisition footprint | About 46 manufacturing and assembly plants acquired | Documentary Fact | S1 page:15: "approximately 46 manufacturing and assembly plants" |
| Intellectual property | Perpetual royalty-free licence from General Motors, exclusive for certain fully automatic transmissions and hybrid products in specified vocational, defense and off-road uses | Documentary Fact | S1 page:41: "irrevocable, perpetual, royalty-free, worldwide license" |
| Credit ratings | Corporate Ba1 (Moody's) and BB+ (Fitch); term loans Baa2 and BBB-; notes Ba2 and BB+; unchanged at 2025-12-31, 2026-03-31 and 2026-09-30; outlook Not supplied | Documentary Fact | S4 page:46; S1 page:66; S2 page:38 |
| Fiscal 2026 guidance (management) | Net sales 5,975 to 6,075; Adjusted EBITDA 1,530 to 1,580 | Management Language | S7 page:4: "Consolidated net sales in the range of $5,975 to $6,075 million" |
| Management leverage target | 2.0x net leverage; definition Not supplied | Management Language | S5 page:1: "2.0x net leverage target" |

### Transaction summary and new debt issues

Transaction. On June 11, 2025 Allison entered into a stock purchase agreement with Dana Incorporated to acquire its off-highway business (S1 page:56). The acquisition closed on January 1, 2026. The final purchase price is 2,628 (S4 page:7), after a 34 reduction for net deficiency in cash, indebtedness and working capital against a preliminary closing payment (S4 page:7); the annual report gave approximately 2,732 as a preliminary figure (S1 page:118). The sources disagree on the price at different dates and the disagreement is logged below, not reconciled. The acquired business forms the whole Allison Off-Highway segment (S4 page:7). Preliminary purchase accounting allocates goodwill of 770, of which 132 to Allison Transmission and 638 to Allison Off-Highway, and identifiable intangibles of 875 (S4 page:7 and page:8); the fair values are subject to change up to one year from closing (S4 page:8). The company expects the acquisition to be accretive to net income and diluted earnings per share in 2026, a management expectation (S7 page:4).

Financing and use of proceeds. The price was paid with cash on hand, 500 of proceeds from 5.875% senior notes due December 2033 issued by ATI, 1,200 of an incremental term loan under the credit agreement, and 300 of borrowings on ATI's revolving credit facility (S4 page:6). Lenders had also committed to a 364-day senior unsecured bridge facility of up to 2,000; it was reduced to 500 by December 31, 2025, was never drawn and was terminated at closing (S4 page:6). The notes were issued in November 2025 as a private placement and the proceeds were designated for the acquisition (S1 page:104). Debt raised for the acquisition is therefore 2,000 on the printed components (calculation A1), against a net cash outlay for the acquisition of 2,563 in the first quarter, reduced to 2,529 for the nine months after the price adjustment (S5 page:8, S4 page:3). Cash on hand covered the balance, and cash fell from 1,495 at 2025-12-31 to 311 at 2026-03-31 (financial base handoff).

New debt issues and amendments. (1) 5.875% senior notes due December 2033, 500, issued November 2025 by ATI, unsecured; redeemable before December 1, 2028 at par plus an applicable premium (S4 page:23). (2) Amendment No. 5 to the credit agreement, entered January 2026 (dated January 2, 2026 in the annual report), added an incremental term loan of 1,200 maturing January 2, 2033 with a springing maturity to the term loan date if that is earlier, raised revolver commitments from 750 to 1,000 and extended the revolver maturity from March 2029 to January 2031 (S4 page:20, S1 page:119). The incremental term loan pays Term SOFR plus 1.75%, an all-in 5.54% at 2026-09-30 (S4 page:20). (3) Amendment No. 6, June 2026, lowered the margin on the original term loan by 0.25% (S4 page:20). (4) 300 was drawn on the revolver at closing, 150 was repaid in the first quarter and the remaining 150 in the second quarter (S5 page:1, S6 page:1). Deferred financing fees recorded on the amendment were 3 on the revolver increase and 12 on the incremental term loan (S4 page:20). Secured debt after the transaction is the two term loans, 1,699, against 2,300 of unsecured notes; the revolver is undrawn (financial base handoff). Liquidity effect: liquidity at 2026-09-30 is 1,493 on the financial base handoff, compared with 2,240 at 2025-12-31.

Status and gaps. The transaction is completed; integration and purchase accounting are open. The sale agreement, the credit agreement and its amendments, the note indentures and the commitment letter are not in the pack (context records legal documents as none), so conditions, indemnities, purchase price adjustment mechanics and any earn-out or deferred consideration are Not supplied. The 2.0x net leverage target stated by management is not defined in the pack, and the financial base handoff computes net leverage of 2.47x on a trailing reported basis that mixes perimeters, so the two are not comparable and no gap to target is stated here.

### Pro forma information and corrections to earlier handoffs

The source-readiness handoff stated that a search of all seven sources found no pro forma disclosure, and the financial base handoff stated that no filing gave results of the acquired business for 2025. Both statements are wrong in part. Each quarterly report has a note headed Supplemental Pro-Forma Information (unaudited) that gives net sales and net income as if the acquisition had occurred on January 1, 2025 (S2 page:9, S3 page:9, S4 page:9). The search that missed it matched the unhyphenated spelling only. What is supplied: pro forma net sales and net income for the first, second and third quarters of 2025, and the nine months; what is still not supplied: pro forma Adjusted EBITDA, pro forma interest, any fourth quarter 2025 or full-year 2025 pro forma figure, and balance sheet data of the acquired business. Consequences: pre-acquisition net sales of the acquired business for 2025 can be derived by subtracting reported net sales from pro forma net sales (calculation A2), and its sales trend can be read; a pro forma trailing Adjusted EBITDA, and therefore pro forma leverage and cover, remain Not calculable, so the financial base handoff's leverage conclusion (trailing, mixed perimeter, overstated against a combined year) stands. Net debt over trailing EBITDA from that handoff is unchanged.

### Fact register, ownership and governance behaviour

| Area | Fact | Category | Locator and exact quote | Evidence quality |
| --- | --- | --- | --- | --- |
| Ownership | Widely held public company; the pack lists no controlling holder, sponsor or class with special control rights; stock is one class of common plus authorized but unissued non-voting and preferred | Insufficient Information | S4 page:2 (balance sheet equity captions); beneficial ownership is in the proxy, not supplied | Insufficient |
| Ownership history | Prior ownership and any dividend recapitalisation history are not in the pack | Insufficient Information | None in S1 to S7 | Insufficient |
| Distribution policy | Quarterly dividend of $0.29 per share in the third quarter of 2026; management refers to the seventh consecutive annual increase | Management Language | S5 page:1: "seventh consecutive annual increase to our quarterly dividend" | High |
| Repurchases | 124 repurchased for nine months 2026 under a program with 1,068 remaining authorization | Documentary Fact | S4 page:28: "the Company repurchased approximately $57 million and $124 million, respectively, of its common stock under the Repurchase Program" | High |
| Deleveraging action | Remaining 150 of revolver repaid in the second quarter; 100 of the 4.75% notes redeemed in September 2026 | Documentary Fact | S4 page:22: "In September 2026, the Company made a $100 million redemption payment on the 4.75% Senior Notes." | High |
| Leverage intention | Management says year-to-date repayment is advancing the company toward its leverage target | Management Language | S7 page:1: "advancing the Company toward our leverage target" | High |
| Legal capacity | Credit agreement restricts additional debt, liens, investments, acquisitions, dividends and repurchases, subject to exceptions; the baskets are not supplied | Insufficient Information | S4 page:22: "customary restrictions (subject to certain exceptions)" | Medium |
| Collateral and guarantees | Term loans and revolver secured by substantially all assets of Holdings, ATI and certain guarantors; the notes are unsecured; the guarantor roster is unresolved | Documentary Fact | S4 page:20: "collateralized by a lien on substantially all assets of the Company, ATI and certain existing and future U.S. subsidiary guarantors, as provided in the Credit Agreement" | High |
| Reporting transparency | The company reconciles non-GAAP measures to GAAP and discloses pro forma information; internal control report for FY2026 will exclude the acquired unit | Documentary Fact | S4 page:53: "will include a scope exception that excludes Allison Off-Highway" | High |
| Creditor-adverse actions | No priming, uptiering, drop-down, non-pro-rata exchange or collateral release is described in S1 to S7; absence in a filing summary does not establish absence under the documents | Insufficient Information | None | Medium |
| Behaviour category | Documented actions are debt-funded acquisition, voluntary reduction of bridge commitments, debt repayment and continued shareholder distributions; this reads as Neutral or Mixed leaning Supportive, not Extraction-Oriented | Analyst Interpretation | S4 page:6, page:22, page:28 | Medium |
| Feasibility link | Capacity to keep both: adjusted free cash flow 662 and distributions 195 for nine months, from the financial base handoff | Analyst Interpretation | CP-1 handoff calculations | Medium |

### Timeline

| Date | Event | Type | Locator |
| --- | --- | --- | --- |
| 1915 | Business founded; headquartered in Indianapolis | History | S1 page:56 |
| 2025-06-11 | Stock purchase agreement with Dana; 364-day bridge commitment up to 2,000 | Transaction | S1 page:56 |
| 2025-11 | 500 of 5.875% senior notes due December 2033 issued | Refinancing | S1 page:104 |
| 2025-12-31 | Bridge commitment reduced to 500; year-end cash 1,495 | Financing | S1 page:56; CP-1 handoff |
| 2026-01-01 | Acquisition closes | Acquisition | S4 page:5 |
| 2026-01 | Amendment No. 5: incremental term loan 1,200, revolver 1,000 to January 2031; 300 drawn | Refinancing | S4 page:20 |
| 2026-02-24 | Annual report for FY2025 filed with the SEC | Reporting | S4 page:31 |
| 2026-03 to 2026-06 | Revolver repaid in two steps of 150 | Deleveraging | S5 page:1; S6 page:1 |
| 2026-06 | Amendment No. 6 lowers term loan margin 0.25% | Refinancing | S4 page:20 |
| 2026-09 | 100 of 4.75% notes redeemed | Deleveraging | S4 page:22 |
| 2026-11-02 | Third quarter release; guidance raised | Subsequent to quarter end | S7 page:4 |
| 2026-11-04 | Third quarter 10-Q signed | Subsequent to quarter end | S4 page:54 |

No ratings change appears in the filings (the rating tables are unchanged). Events dated after 2026-09-30 are subsequent events and are not folded into third quarter facts.

### Conflicts

| Topic | Span A | Span B | Status |
| --- | --- | --- | --- |
| Purchase price | S1 page:118: "for a purchase price of approximately $2,732 million" | S4 page:7: "a final purchase price of $2,628 million" | Logged, not reconciled; different dates; the later quarterly figure describes the closed transaction and S4 page:7 explains an adjustment of 34 against a preliminary cash payment of 2,664; the step from 2,732 to 2,664 is not explained in the pack |
| Pro forma availability | CP-0 handoff: pro forma disclosure "found none" | S4 page:9: "Supplemental Pro-Forma Information (unaudited)" | Earlier handoff was wrong; corrected above |
| Guarantors | S4 page:20: "existing and future U.S. subsidiary guarantors" | S4 page:22: "None of ATI’s domestic subsidiaries currently guarantee its obligations under the Senior Secured Credit Facility" | Logged, not reconciled |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence |
| --- | --- | --- | --- | --- |
| Margin and cash-flow risk | Third quarter Adjusted EBITDA margin 37.8% for Allison Transmission and 12.7% for Allison Off-Highway (S7 page:10) | The acquired unit lowers group margin and adds cyclical agriculture and industrial exposure; stepped-up inventory and intangible amortization reduce reported earnings in 2026 | Less operating cushion per unit of debt than the legacy business alone; stress would first hit the lower-margin unit | The unit is consolidated for only the 2026 quarters, and purchase accounting is preliminary |
| Revenue durability | Long-term agreements covering over 90% of North American on-highway volume (S1 page:8); aftermarket described as stable (S1 page:12) | Agreements fix pricing and commodity sharing but not volumes; aftermarket follows the installed base | Supports earnings stability through a cycle, but volume risk remains in medium-duty and Class 8 vocational trucks | Defense and aftermarket grew in 2026 quarters, which limits the downside |
| Concentration | Top five OEMs 52% of FY2025 net sales; Daimler AG 18% (S1 page:28) | Loss or consolidation of one customer, or a model discontinuation, cuts volume | Concentration is an uncertainty for volumes and bargaining power | The acquisition dilutes concentration, but a post-acquisition customer split is not supplied |
| Structure and recovery mechanics | Secured term loans 1,699 and revolver 1,000 sit ahead of unsecured notes 2,300 (S4 page:19, page:20) | Secured lenders hold liens on substantially all assets of Holdings, ATI and certain guarantors; the notes are structurally and contractually behind them | Recovery mechanics favor secured lenders; no recovery outcome is concluded | Guarantor roster unresolved |
| Shareholder alignment | Continued dividends and buybacks alongside acquisition debt (S5 page:1, S4 page:28) | Cash returned to shareholders is not available for debt reduction | Willingness to deleverage is shown but not contractually bound | Revolver repaid and notes partly redeemed |
| Key uncertainties | Legal documents, leverage target definition and post-acquisition customer data are not in the pack | Unknown covenant baskets and target definition limit forward view | Monitoring posture should require the documents before sizing capacity for distributions | None |

### Consumer readiness

| Consumer | Readiness | What it should take from this handoff | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 fundamental credit synthesis | Ready with limitations | Business risk rows, transaction facts, structure, governance behaviour and the pro forma correction | Business risk is a required driver beside financial risk | Obtain legal documents; carry the perimeter caveat on all trailing metrics |
| CP-5 evidence trace | Ready with limitations | The conflicts and corrections, and every quote with its locator | Reviewers must check the pro forma correction and purchase price conflict against S2 to S4 | Compare each row with the cited page |

## Calculations

| Id | Calculation | Inputs and locators | Result |
| --- | --- | --- | --- |
| A1 | Debt raised for the acquisition | Notes 500 plus incremental term loan 1,200 plus revolver draw 300 (S4 page:6) | 2,000 |
| A2 | Implied pre-acquisition net sales of the acquired business, 2025 | Pro forma net sales less reported net sales: Q1 1,367 less 766; Q2 1,475 less 814; Q3 1,320 less 693 (S2 page:9, S3 page:9, S4 page:9; reported 766 and 814 and 693 from S2, S3, S4 reconciliations) | Q1 601; Q2 661; Q3 627; sum 1,889, equal to nine months 4,162 less 2,273 |
| A3 | Sales trend of the acquired unit, third quarter | 2026 segment sales 653 (S4 page:30) over implied 2025 sales 627 (A2) | 1.0415, an increase of 4.1% on a derived basis |
| A4 | Sales trend of the acquired unit, nine months | 2,032 (S4 page:30) over implied 1,889 (A2) | 1.0757, an increase of 7.6% on a derived basis |
| A5 | Acquired unit share of net sales | Third quarter 653 / 1,534; nine months 2,032 / 4,506 (S4 page:30) | 42.6% and 45.1% |
| A6 | Acquired unit share of segment Adjusted EBITDA before central costs | Nine months 285 / (927 + 285) (S7 page:10) | 23.5% |
| A7 | Goodwill and intangibles share of assets | (2,828 + 1,582) / 8,789 (S4 page:2) | 50.2% |
| A8 | Net acquisition outlay tie | Cash consideration 2,664 less cash acquired 101 less price adjustment received 34 (S4 page:7) | 2,529, equal to the cash flow line (S4 page:3) |
| A9 | Pro forma net income direction | Nine months 2025 pro forma 441 against reported 524 (S4 page:9, S4 page:2) | Lower by 83 |

## Gaps

| Gap | Severity | Affected consumers | Action |
| --- | --- | --- | --- |
| Stock purchase agreement, credit agreement and amendments, note indentures, commitment letter and any security documents are Not supplied | Medium | CP-2, CP-5 | Obtain before relying on any statement of legal capacity, baskets or recovery |
| Management's 2.0x net leverage target has no definition, date or measurement basis in the pack | Medium | CP-2 | Treat as intention; do not compare with computed ratios |
| Pro forma Adjusted EBITDA, interest and 2025 fourth quarter pro forma data for the combined business are Not supplied | High | CP-2 | Derive only net sales trends; keep combined leverage Not calculable |
| Ownership above five percent and board control are in the proxy statement, Not supplied | Low | CP-2 | Obtain the proxy statement |
| Customer concentration and geography after the acquisition are Not supplied | Medium | CP-2 | Treat FY2025 concentration as pre-acquisition |
| Synergy and cost savings amounts are not stated; management refers to a synergy capture target without a figure (S5 page:1) | Medium | CP-2 | Do not credit synergies |
| Rating outlook is Not supplied; only ratings are in the filings | Low | CP-2 | Obtain agency reports if needed |
| Purchase accounting is preliminary | Medium | CP-2, CP-5 | Treat goodwill and intangibles as provisional |

## Next module

CP-2, fundamental credit synthesis. Carry forward: the acquisition closed 2026-01-01 at 2,628 and added a lower-margin unit that is now 42.6% of third quarter net sales; debt raised for it is 2,000 of which 1,699 of term loans are secured; management has a 2.0x net leverage target without a definition; the earlier statements that no pro forma information existed are corrected (pro forma net sales and net income exist, pro forma Adjusted EBITDA does not); and the legal documents, guarantor roster and post-acquisition customer data remain open.
