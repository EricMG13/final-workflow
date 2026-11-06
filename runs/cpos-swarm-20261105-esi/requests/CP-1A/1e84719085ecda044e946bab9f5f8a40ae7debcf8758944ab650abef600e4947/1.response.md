# CP-1A — Business and transaction context: Element Solutions Inc (esi)

## Request

- Issuer: Element Solutions Inc (issuer id `esi`, NYSE: ESI), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; current period Q3 2026; prior period FY2025 (context).
- Run: `esi-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Feeds CP-2, CP-5 and the report sections "Company and operating model", "Company profile" and "Transaction summary and new debt issues".
- Execution: host session. The host read the pinned page files and the CP-0 and CP-1 handoffs and wrote this answer. No provider was called.
- Question: which transaction, business, ownership and operating facts matter most to a creditor, with each fact tagged as a Documentary Fact, Management Language, Analyst Interpretation or Insufficient Information.
- Scope limits: no peer ranking, no instrument recommendation and no recovery conclusion. External material is labelled as such; none is used in this answer.

## Sources

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_esi-20251231.htm.jsonl | e419be4a34b86cf3946781c81c9cf5167d1ce55ea947acb2e97a22e3ec33fbdc | Business description, segments, customers, competition, raw materials, history, related party (tag K25) |
| 10-Q_2026-03-31_esi-20260331.htm.jsonl | 71ffb0652af7e069b88fd66093decc7d627d9409b00bd185ac2a68db72c238da | Q1 2026 acquisitions and financing (tag Q1-26) |
| 10-Q_2026-06-30_esi-20260630.htm.jsonl | 9e356702c38010063835ed61e96bcc033abb0f0a3a4b5a9a1845d764f0bcd2b7 | Solstice merger terms as signed, termination fee risk, Advisory Services Agreement amendment (tag Q2-26) |
| 10-Q_2026-09-30_esi-20260930.htm.jsonl | 1efce58ae7d1707b81e096f97ecf01dbf0104d1e81a25b95db794dfd861b04fe | Solstice termination, acquisitions, segments, debt, management change (tag Q3-26) |
| EX-99.1_2026-04-28_aearningsreleaseex99120263.htm.jsonl | cb75b2ab3988a8e0ad3f68546b2df2a55172fd4900de7f7f14ec3436aa37dbbf | Q1 2026 results narrative (tag R1) |
| EX-99.1_2026-07-27_aearningsreleaseex99120266.htm.jsonl | c0a4eea4343eb189f65a5cb896e49cd67b1e5c372bfce79bfb18a89241f92f7e | Q2 2026 results and merger announcement narrative (tag R2) |
| EX-99.1_2026-10-21_aearningsreleaseex99120269.htm.jsonl | b36d51c2a20c56990c8361f520b238bac0611bf5a7dab66ba03c7922169d0001 | Q3 2026 results, guidance, management commentary on the terminated transaction (tag R3) |
| context | 1920ec84f7b9710e00bbaac803890d2695813e40c10637e35f2e7d8eaaf0285a | Run settings; not issuer evidence |

Supplied handoffs consumed:

- CP-0 sha256 cdece14e2edef04df25761198b67e4d3c88f681db7a403c096bd0cf0d6bf17b7. Carried forward: the Merger Agreement, Termination Agreement, proxy and Form S-4 are not supplied; the EFC and Micromax prices in the 10-K are estimates that the Q3 10-Q revises; nothing after October 22, 2026 is supplied.
- CP-1 sha256 0b784e0bff14bdc1d3f4b3894b4edcc8e5b0011eb0edb677c3ca72eb727a1ab8. Carried forward by reference (CP-1 Cn means calculation n there): total debt to LTM Adjusted EBITDA of 3.09x at Q3 2026 (C4); cash plus unused revolver of 702.9 (C7); LTM EBITDA is not pro forma for the acquisitions; the springing first lien net leverage covenant is 5.0 to 1.0 with the ratio not printed.

Citation format: (tag pN: "exact substring") names the source tag and page chunk; a cell naming only a tag and page cites the figure on that page. Categories are those of the method.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Element Solutions is a specialty chemicals supplier that changed shape in 2026: two acquisitions closed, funded by new debt and cash, and a proposed sale to Solstice was signed on July 6, 2026 and terminated on August 27, 2026. | High | The Merger Agreement, Termination Agreement and any payment under the termination are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Electronics produced 78.3% of net sales in Q3 2026, and pass-through metals were 40.9% of Electronics sales. | Revenue and margin ratios move with metal prices, and the segment depends on electronics and data centre demand. | Medium |
| No sponsor is identified; documented capital allocation mixes acquisitions with dividends and buybacks. | Leverage increases and buybacks are discretionary choices; creditor limits on them are not supplied. | Medium |
| Solstice would have paid 0.5 Solstice shares plus 10.00 in cash per share; a 376,000,000 termination fee was disclosed as possible. | The terminated deal removed a change-of-control event; whether any fee was owed is not stated. | Medium |
| No customer is 10% or more of net sales, and order backlog is minimal. | Diversified customers lower concentration risk, but short cycles limit revenue visibility. | High |
| Micromax and EFC added 161.2 of Q3 2026 net sales, and their purchase price allocations are preliminary. | Integration and valuation changes could still alter acquired balances and earnings. | Medium |

### Business and transaction view

Element Solutions is a Delaware specialty chemicals technology company with two segments: Electronics (MacDermid Alpha Electronics Solutions) and Specialties (Element Specialties). Its products are consumed in customers' production processes, which gives recurring replenishment demand, and no customer reaches 10% of net sales. The credit-relevant change in 2026 is structural. EFC (closed January 2, 2026) was paid for from cash on hand and Micromax (closed February 2, 2026) from $450 million of add-on term loans and revolver borrowings, so the business is larger, more Electronics-weighted and more exposed to precious-metal pass-through pricing than at FY2025. A proposed acquisition of the company by Solstice Advanced Materials Inc. was signed on July 6, 2026 and terminated on August 27, 2026 with a mutual release; the supplied filings do not say whether any termination fee or cost arose. The company is publicly listed and no sponsor is identified in the sources read, and the documented governance behaviour is mixed rather than adverse: a debt-funded acquisition year, continued dividends and buybacks, and a modest related-party advisory fee. The main creditor uncertainties are the integration and valuation of the acquisitions, metal-price-driven working capital, and the unsupplied terms of the terminated merger.

| Driver | View | Category |
| --- | --- | --- |
| Transaction and ownership | Merger signed then terminated; public company, no sponsor | Documentary Fact |
| Business and operating model | Two segments, recurring consumable products, no customer at 10% of net sales, metals pass-through | Documentary Fact |
| Credit-relevant change | Two 2026 acquisitions, add-on term loans of $450 million, revolver upsized to $500 million | Documentary Fact |

### Company and operating model

| Area | Fact | Category | Source |
| --- | --- | --- | --- |
| Core activity | "a leading global specialty chemicals technology company" whose solutions "enhance the performance of products people use every day" | Management Language | K25 p6 |
| Segments | "two reportable segments: Electronics (MacDermid Alpha Electronics Solutions) and Specialties (Element Specialties)" | Documentary Fact | Q3-26 p10 |
| Segment mix, FY2025 | Electronics and Specialties contributed "approximately 70% and 30%" of 2025 net sales | Documentary Fact | K25 p8 |
| Segment mix, Q3 2026 | Electronics 779.6 and Specialties 215.7 of net sales 995.3 (78.3% and 21.7%, calculated A1); Electronics Adjusted EBITDA 148.3 of 191.0 (77.6%, A1) | Documentary Fact with Analyst Interpretation | Q3-26 p26, p27 |
| Revenue model | Products are "consumed by customers as part of their production process", giving "reliable and recurring revenue" | Management Language | K25 p8 |
| Customers | "no customer representing 10% or more of our consolidated net sales in 2025, 2024 or 2023" | Documentary Fact | K25 p16 |
| Order visibility | "our order backlog levels are minimal" | Documentary Fact | K25 p16 |
| Seasonality | "Neither of our segments is subject to significant seasonality" | Management Language | K25 p8 |
| End markets, Electronics | Printed circuit boards, advanced semiconductor packaging, data centres, mobile communications, computers, automobiles and aerospace | Documentary Fact | K25 p8 |
| End markets, Specialties | Metal and plastic finishing, offshore energy fluids and, from 2026, high-purity gases from EFC | Documentary Fact | Q3-26 p10, p31 |
| Geography | 2025 net sales: China 557.9 (21.9%, A2), United States 524.3 (20.6%, A2), other countries 1,469.0; "approximately 77% of our net sales were generated from non-U.S. operations" for nine months 2026 | Documentary Fact | K25 p125; Q3-26 p44 |
| Metals pass-through | About half of Assembly Solutions net sales is metal content passed through; pass-through metals in Electronics net sales were 318.5 in Q3 2026 against 125.0 in Q3 2025 (40.9% and 26.9% of Electronics sales, A3) | Documentary Fact with Analyst Interpretation | K25 p9; R3 p8 |
| Cost structure | Cost of sales was 652.9 of Q3 2026 net sales of 995.3, a gross margin of 34.4% against 42.2% in Q3 2025 (A4); the metals pass-through and acquired mix both move this ratio | Analyst Interpretation | Q3-26 p5 |
| Capital intensity | Management describes "Stable Cash Flow and Low Capital Requirements"; capital expenditure guidance for 2026 rose to about 110 from about 75.0 in the 10-K, and capital expenditure was 83.4 for nine months 2026 against 45.2 | Management Language and Documentary Fact | K25 p13, p66; Q3-26 p44 |
| Working capital | Nine-month 2026 operating cash flow was lower than nine months 2025 "primarily driven by higher investment in working capital from rising metals prices" | Documentary Fact | Q3-26 p45 |
| Competition | Electronics' most significant competitors are named as MKS Instruments, Qnity Electronics, Inc., Henkel Corporation, Senju Metal Industry Co. and Uyemura International | Documentary Fact | K25 p20 |
| Raw materials | Raw materials are purchased "as-needed from outside sources"; tin is recycled in the company's own U.S. smelting and refining facility | Documentary Fact | K25 p20 |
| Segment profitability trend | Specialties Adjusted EBITDA was 42.7 in Q3 2026 against 45.4 in Q3 2025, down 6%, despite EFC | Documentary Fact | R3 p4; Q3-26 p27 |
| Pricing and volume split | Price against volume is not disclosed | Insufficient Information | The missing split limits a view of whether Electronics growth is volume, content or metals price |

### Company profile

| Item | Value | Category | Source |
| --- | --- | --- | --- |
| Legal name | Element Solutions Inc (f/k/a Platform Specialty Products Corporation) | Documentary Fact | Q3-26 p1; K25 p77 |
| Incorporation | Delaware, incorporated in January 2014 | Documentary Fact | Q3-26 p10 |
| Headquarters | 500 South Pointe Drive, Suite 200, Miami Beach, Florida 33139 | Documentary Fact | K25 p1 |
| Listing | Common stock on the New York Stock Exchange, symbol ESI | Documentary Fact | Q3-26 p1 |
| Sector and country | Specialty chemicals (context sector: Miscellaneous Chemical Products), United States | Analyst Interpretation | Q3-26 p10; context |
| Fiscal year end | December 31 | Documentary Fact | K25 p1 |
| Auditor | PricewaterhouseCoopers LLP, auditor since 2013 | Documentary Fact | K25 p82 |
| Employees | approximately 5,200 full-time employees at December 31, 2025, about 80% outside the U.S. | Documentary Fact | K25 p16, p17 |
| Leadership | Chief Executive Officer Benjamin H. Gliklich; Carey J. Dorman appointed President and Chief Financial Officer; Matthew Liebowitz Chief Operating Officer; Richard L. Fricke moved to special advisor effective October 19, 2026 | Documentary Fact | R3 p4; Q3-26 p49 |
| Ownership | Publicly traded; no controlling holder or sponsor is described in the pages read; ownership percentages are not disclosed in the supplied filings | Insufficient Information | Beneficial ownership data is not in the supplied pack |
| Related party | Advisory Services Agreement with Mariposa Capital, LLC, "an affiliate of one of its founder directors"; annual fee of $2.0 million, term to May 5, 2029 after an amendment on May 5, 2026 | Documentary Fact | Q3-26 p26 |
| Reporting basis | U.S. GAAP, consolidated, USD millions | Documentary Fact | CP-1 |
| Ratings | No rating report or rating event is supplied | Insufficient Information | Ratings are not in the pack; they affect borrowing cost and covenant-lite access |

### Transaction summary and new debt issues

Three transactions matter: the terminated Solstice merger, the two 2026 acquisitions and the February 2026 financing. All are Documentary Fact unless labelled.

Solstice merger. On July 6, 2026 the company entered into an Agreement and Plan of Merger with Solstice Advanced Materials Inc., Solar Merger Sub One Inc. and Solar Merger Sub Two LLC (Q3-26 p3: "dated as of July 6, 2026"). Under the terms disclosed in the Q2 10-Q, each share of common stock would convert into "0.5 shares of Solstice common stock" and "$10.00 in cash", with closing "expected to close in the first half of 2027" and conditions that included stockholder approval of both companies, an effective Form S-4, listing approval and expiry of the Hart-Scott-Rodino waiting period (Q2-26 p12). The Q2 10-Q disclosed that if the Merger Agreement were terminated "in certain circumstances, we could be required to pay to Solstice a termination fee of $376,000,000" and that the company might "use available cash, including by drawdown on our revolving credit facility" to do so (Q2-26 p50). On August 27, 2026 the parties entered into a Termination Agreement; the Q3 10-Q states the parties "mutually agreed to terminate the Merger Agreement which, subject to customary exceptions, mutually released the parties from any claims of liability" (Q3-26 p12). The Q3 10-Q does not state that any termination fee was paid or accrued and does not state the cost of the transaction; the Termination Agreement is listed as an exhibit to a Form 8-K filed on August 27, 2026 (Q3-26 p49) that is not in the pack. Management Language: the chief executive described the company's "standalone, independent trajectory" as having "only improved" (R3 p2). Insufficient Information: whether a termination fee or other cost arose, the cost of the terminated process within "Acquisition, integration and transaction expenses" of 21.9 in Q3 2026 (Q3-26 p27), and the reason for termination are not in the supplied sources. Liquidity effect: the Q2 10-Q summary does not describe how the company's debt would have been treated at closing (Insufficient Information); with the merger terminated, the existing Credit Agreement and 3.875% USD Notes due 2028 remain the capital structure (CP-1).

EFC and Micromax. EFC Gases & Advanced Materials was acquired on January 2, 2026 "for a purchase price of approximately $367 million, net of cash and subject to adjustments", plus a potential earn-out of "up to $30.0 million cash or 1.16 million shares", funded with cash on hand (Q3-26 p12). Micromax (US) Holdings LLC was acquired on February 2, 2026 "for a purchase price of approximately $494 million, net of cash and subject to adjustments", funded with the Add-on Term Loans of $450 million and revolver borrowings (Q3-26 p12). The 10-K's subsequent-events note estimated the prices at approximately $369 million and $500 million (K25 p126), logged as a conflict below; the later filing controls. Cash paid for acquisitions was 865.8 for nine months 2026 (CP-1). Goodwill of 128.9 for Micromax and 163.8 for EFC was recorded and the purchase price allocations are "preliminary" (Q3-26 p13, p14). The acquisitions were "not significant" so pro forma results were not presented (Q3-26 p14), which means no pro forma EBITDA is available (Insufficient Information; CP-1 gaps).

New debt issues and financing. No new bond was issued in 2026 in the supplied filings. On February 2, 2026 the company syndicated $450 million of Add-on Term Loans with "identical terms as the then existing term loans B-3, including a maturity date of December 18, 2030", and a "5-year $500 million senior secured revolving credit facility, which replaced its then existing $375 million revolving credit facility" with maturity extended to 2031 (Q3-26 p16). The term loans bear SOFR plus 1.75% and the revolver SOFR plus 1.50% (Q3-26 p15). Swaps convert "$350 million of the Add-on Term Loans" into fixed euro-denominated debt through December 2029 (Q3-26 p20). Liquidity effect, from CP-1: debt rose to 2,082.1 from 1,625.9 and cash fell to 224.9 from 626.5 between December 31, 2025 and September 30, 2026; total debt to LTM Adjusted EBITDA was 3.09x at Q3 2026 and the first large maturity is the 800.0 of 3.875% USD Notes due September 1, 2028. Revolver borrowings fell from 85.0 at Q1 2026 to 15.0 at Q3 2026. Analyst Interpretation: the financing was term-loan heavy, secured and floating-rate with partial swap fixation, so rate and euro-dollar movements affect interest cost and the net investment hedge position.

Subsequent events. After the balance sheet date the 10-Q reports a Kuprion milestone payment of $9.7 million made in the fourth quarter of 2026 (Q3-26 p15) and the management changes effective October 19, 2026 (Q3-26 p49). No other event between October 22, 2026 and 2026-11-05 is supplied (Insufficient Information).

### Ownership and governance behaviour

| Behaviour | Evidence | Category | Mechanic | Legal capacity, willingness, feasibility |
| --- | --- | --- | --- | --- |
| Neutral or Mixed: change-of-control proposal withdrawn | Merger signed July 6, 2026 and terminated August 27, 2026 (Q3-26 p3) | Documentary Fact | A sale to a larger company would have changed the obligor and its leverage; termination keeps the standalone structure | Capacity: change-of-control default is listed among Credit Agreement events (Q3-26 p18: "change of control provisions"); indenture terms are not supplied. Willingness: the board entered then exited the transaction. Feasibility: not assessable |
| Supportive: debt reduction in 2025 | A 200 million prepayment of term loans B-3 funded by the sale of MacDermid Graphics Solutions (K25 p113: "prepaid $200 million of its term loans B-3") | Documentary Fact | Lower term debt before the 2026 acquisitions | Willingness shown by action; capacity not tested |
| Neutral or Mixed: debt-funded acquisitions | 450 of add-on term loans and revolver borrowings funded Micromax (Q3-26 p12); CP-1 shows debt up 456.2 | Documentary Fact | Gross debt and interest cost rose while EBITDA contribution is partial in LTM | Capacity: Credit Agreement permits incremental debt on a pro forma first lien net leverage basis (K25 p41); willingness shown; feasibility supported by liquidity of 702.9 (CP-1 C7) |
| Neutral or Mixed: shareholder returns | Dividends of 59.3 and buybacks of 37.7 in nine months 2026 (CP-1); "approximately $518 million" remains authorised (Q3-26 p22) | Documentary Fact | Distributions compete with debt reduction; 97.0 is covered by nine-month operating cash flow less capital expenditure of 108.8 (CP-1 C6, C13) | Capacity: restricted-payment baskets are not supplied. Willingness: stated strategy is "prudent capital allocation" (Q3-26 p30) |
| Neutral or Mixed: related-party advisory fee | Mariposa Capital, LLC fee of $2.0 million a year, term extended to May 5, 2029 (Q3-26 p26) | Documentary Fact | A small recurring leakage to an affiliate of a founder director; term extended during the year of the merger | Willingness: extended on May 5, 2026; amount is small against Adjusted EBITDA |
| Neutral or Mixed: equity compensation | "2025 executive share grants" of 37.1 were added back to FY2025 Adjusted EBITDA (K25 p124) | Documentary Fact | Adjusted EBITDA excludes a cost that accrued to management | Disclosure: reconciled in the 10-K |
| Creditor-Adverse actions (priming, uptiering, drop-downs, non-pro-rata exchanges, collateral release) | None located in the pages read | Insufficient Information | Absence in the pages read is not evidence of absence | Capacity unknown without the executed documents |

Evidence quality: High for filed 10-K and 10-Q text; Medium for the earnings releases, which are issuer presentations and carry Management Language.

### Timeline

| Date | Event | Category | Source |
| --- | --- | --- | --- |
| January 2014 | Incorporated in Delaware | Documentary Fact | Q3-26 p10 |
| January 31, 2019 | Credit Agreement dated | Documentary Fact | Q3-26 p2 |
| August 18, 2020 | $800 million 3.875% senior notes due 2028 issued | Documentary Fact | Q3-26 p3 |
| May 19, 2023 | Kuprion acquisition | Documentary Fact | Q3-26 p2 |
| October 2024 | New term loans B-3 syndicated (about $1.04 billion), prepaying term loans B-2 | Documentary Fact | K25 p68 |
| February 28, 2025 | MacDermid Graphics Solutions sold for $320 million net of disposed cash | Documentary Fact | K25 p7 |
| March 31, 2025 | $200 million of term loans B-3 prepaid | Documentary Fact | K25 p113 |
| January 2, 2026 | EFC acquisition completed | Documentary Fact | Q3-26 p12 |
| February 2, 2026 | Micromax acquisition, Add-on Term Loans and upsized revolver | Documentary Fact | Q3-26 p12, p16 |
| February 18, 2026 | FY2025 10-K signed | Documentary Fact | K25 p78 |
| May 5, 2026 | Mariposa advisory agreement amended | Documentary Fact | Q3-26 p26 |
| July 6, 2026 | Merger Agreement with Solstice signed | Documentary Fact | Q3-26 p3 |
| July 28, 2026 | Q2 10-Q signed | Documentary Fact | Q2-26 p53 |
| August 27, 2026 | Termination Agreement signed | Documentary Fact | Q3-26 p3 |
| October 19, 2026 | Management responsibilities changed | Documentary Fact | Q3-26 p49 |
| October 21 and 22, 2026 | Q3 2026 release and 10-Q | Documentary Fact | R3 p4; Q3-26 p50 |
| After October 22, 2026 | Further events up to the as-of date | Insufficient Information | Not supplied |

Events after a source's period are subsequent events: the Solstice merger (July 6 to August 27, 2026) occurred after the June 30, 2026 balance sheet date but is discussed in the Q2 10-Q's notes; the termination is a subsequent event to the Q2 10-Q and a current-period event in the Q3 10-Q. The Kuprion payment in the fourth quarter of 2026 is a subsequent event to the Q3 balance sheet.

### Conflicts

| Item | Span A | Span B | Effect |
| --- | --- | --- | --- |
| EFC purchase price | K25 p126: "for a purchase price of approximately $369 million" | Q3-26 p12: "for a purchase price of approximately $367 million" | Logged, not reconciled; the Q3 10-Q is later and prints the allocation, and the 10-K figure was an estimate at its filing date |
| Micromax purchase price | K25 p126: "for a purchase price of approximately $500 million" | Q3-26 p12: "for a purchase price of approximately $494 million" | Logged, not reconciled; same reading |
| MGS gain | K25 p7: "The sale resulted in a gain of $66.5 million" | K25 p82: "Gain on divestitures 59.0 — —" | Not a conflict in substance: the 10-K states a loss of 7.5 on other immaterial divestitures in 2025 (K25 p63: "a loss on sale of $7.5 million"), which bridges the two (A5); logged for completeness |
| Merger status | Q2-26 p12: "Pending Transaction with Solstice" | Q3-26 p3: "mutually agreed to terminate" | Superseded by the later filing; the Q2 10-Q terms are history |

### Credit translations

- Revenue durability. Evidence: recurring consumable products, no customer at 10% of net sales and minimal backlog (K25 p8, p16). Mechanic: broad customer base lowers single-name loss risk, while minimal backlog means revenue follows customers' production in short cycles. Implication: debt service is supported by diversification, but earnings can fall quickly in an electronics downturn; the Q3 2026 organic growth of 13% (CP-1) is demand driven and could reverse.
- Margin and cash-flow risk. Evidence: pass-through metals were 40.9% of Q3 2026 Electronics sales against 26.9% a year earlier (A3) and the gross margin fell to 34.4% from 42.2% (A4). Mechanic: higher metal prices lift revenue and working capital without lifting profit proportionally and tie up cash in receivables and inventories (Q3-26 p45). Implication: reported revenue growth overstates operating growth, and cash conversion weakens when metals rise, as in nine months 2026 where operating cash flow fell while Adjusted EBITDA rose (CP-1).
- Concentration risk. Evidence: Electronics is 78.3% of Q3 2026 net sales and 77.6% of segment Adjusted EBITDA (A1); China is 21.9% of FY2025 net sales (A2). Mechanic: demand in AI infrastructure and high-performance electronics drives Electronics (R3 p2, Management Language), and China exposure adds trade-policy sensitivity named in the filing's forward-looking factors (Q3-26 p4). Implication: segment and country concentration raise cyclical and trade exposure; Specialties, which fell in Q3 2026, is a smaller offset.
- Owner and governance alignment. Evidence: no sponsor, a terminated sale, acquisition-led leverage and continued shareholder returns. Mechanic: a public company with discretionary buybacks can lever up for acquisitions or return cash; the Credit Agreement's springing test does not bind at the current revolver draw (CP-1). Implication: creditor protection depends on documents that are not supplied; behaviour to date is mixed, not adverse. The logged conflict on the acquisition prices does not alter this reading.
- Acquisition integration. Evidence: preliminary allocations, goodwill of 292.7 added (Q3-26 p14: "Acquisitions (2) 128.9 163.8 292.7"), and acquisition, integration and transaction expenses of 52.6 for nine months 2026 (CP-1). Mechanic: add-backs and fair value changes make acquired earnings harder to verify. Implication: leverage on LTM EBITDA should be monitored against a pro forma figure, which is not supplied.
- Key uncertainties: terms and any cost of the terminated merger, covenant and indenture definitions, post-October 22, 2026 events, ratings.

### Consumer readiness

| Consumer | Readiness | What to take from CP-1A | Gap and action |
| --- | --- | --- | --- |
| CP-2 | Ready with limitations | Business model, metals pass-through, acquisition financing, governance behaviour, merger history | Termination terms, credit documents and ratings not supplied |
| CP-5 | Ready | Every fact row has a category and a tag and page locator | Releases are issuer presentation; conflicts logged |
| Report delivery | Ready | The three selected sections: company and operating model, company profile, transaction summary | None for these sections beyond the gaps |

## Calculations

All inputs are USD millions copied from the cited pages; percentages are rounded half up to one decimal.

| ID | Formula | Inputs and locators | Result |
| --- | --- | --- | --- |
| A1 | Segment share of Q3 2026 net sales and Adjusted EBITDA | 779.6 / 995.3; 215.7 / 995.3; 148.3 / 191.0 (Q3-26 p26, p27) | 78.3%; 21.7%; 77.6% |
| A2 | Country share of FY2025 net sales | 557.9 / 2,551.2; 524.3 / 2,551.2 (K25 p125) | 21.9%; 20.6% |
| A3 | Pass-through metals share of Electronics net sales | Q3 2026: 318.5 / 779.6. Q3 2025: 125.0 / 465.2 (R3 p8; Q3-26 p26) | 40.9%; 26.9% |
| A4 | Gross margin | Q3 2026: 342.4 / 995.3. Q3 2025: 277.0 / 656.1 (Q3-26 p5) | 34.4%; 42.2% |
| A5 | MGS gain bridge | 66.5 gain less 7.5 loss on other divestitures (K25 p63); printed gain on divestitures 59.0 (K25 p82) | 59.0, equal to the printed line |
| A6 | Acquired net sales in Q3 2026 | Micromax 137.8 + EFC 23.4 (Q3-26 p26) | 161.2 |
| A7 | Goodwill added | 128.9 + 163.8 (Q3-26 p14) | 292.7, equal to the printed total |

## Gaps

| Gap | Severity | Effect | Action |
| --- | --- | --- | --- |
| Merger Agreement, Termination Agreement and any payment under the termination not supplied | Medium | The cost, if any, of the terminated transaction and the change-of-control mechanics are unknown | Supply the July 6 and August 27, 2026 Form 8-Ks and exhibits |
| Beneficial ownership, board composition and control rights not supplied (proxy statement) | Low | Ownership percentages and influence cannot be assessed | Supply the 2026 proxy statement |
| Credit Agreement and indenture not supplied | High for legal work | Capacity for priming, debt incurrence and restricted payments cannot be tested | Supply executed documents |
| Pro forma EBITDA for EFC and Micromax not supplied | Medium | LTM leverage is on a reported basis | Request from management or the compliance certificate |
| Price against volume split and customer-level data not disclosed | Low | Growth quality cannot be separated | Not required for this scope |
| Ratings and market data not supplied | Low | Market view of credit not available | Not required for this scope |
| Events between October 22, 2026 and 2026-11-05 not supplied | Medium | Position at the as-of date may differ | Supply later Form 8-Ks or confirm none |
| Business pages beyond Items 1 and 7 and the opened notes not read | Low | Some risk factors and legal matters are unassessed | Downstream modules open pages they need |

## Next module

- CP-2: use the segment and metals dependence, the acquisition financing and the governance table for liquidity and covenant work; carry the termination terms, the Credit Agreement and indenture, ratings and the post-October 22, 2026 window as Not supplied.
- CP-5: trace each fact row by its tag and page; keep the Management Language rows qualified and keep the logged acquisition price conflict visible.
