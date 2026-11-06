# CP-1A business and transaction context: UBS Group AG (ubs)

## Request

- Issuer: UBS Group AG (issuer id `ubs`), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; current period Q3 2026; prior period FY2025.
- Question: which transaction, business, ownership and operating facts matter most to a creditor of UBS Group AG, and what do they mean through to credit implications?
- Perimeter: UBS Group AG consolidated unless a row names UBS AG or another entity. The context names no borrower, parent, sponsor or guarantor; blank fields are not evidence of none.
- Prohibited and not done here: peer ranking, instrument recommendation and recovery conclusion. Category tags follow the method: Documentary Fact, Management Language, Analyst Interpretation, Insufficient Information.

## Sources

Issuer sources relied on (pinned `.jsonl` text; locators are `page:N` extraction chunks, not printed pages):

| Source | sha256 | Used for |
| --- | --- | --- |
| 20-F_2025-12-31_ubs-20251231.htm.jsonl | c65ff0a03ee3c3df685c628425c6a0a7856867141560663149d32b58774d8f33 | Business, history, divisions, segment note, shareholders, capital, regulation, share programmes |
| 6-K_2026-03-31_edgarq1q26kubsgroupagc.htm.jsonl | 5ae425915ce6d8540a2dcbe4beb8ed52f974546cb1a0a776687e74bfb6a0ae6d | Capitalization at 31.3.26 |
| 6-K_2026-03-31_investorpresotext2026.htm.jsonl | 84e6720eb0ad0ada288bec163d56547d8305bba53a01f71c7fcd5a3acd94f71a | First quarter 2026 call (management language) |
| 6-K_2026-06-30_investorpresotext2026.htm.jsonl | 671f7dde67986089a1c17da85500334fa96b51697d1642480c22e2b5d6422aa1 | Second quarter 2026 call (management language) |
| 6-K_2026-07-29_edgarq2q26kubsgroup.htm.jsonl | 88627f5322eed51bd548e2eb9daaa4bff0f8cc654e252b054c4865eeda3901ea | Capitalization at 30.6.26 |
| 6-K_2026-09-30_edgar3q26kubsgroupc.htm.jsonl | faea893d4d4d07cf7975acc81d8e41156e0b136d2c529429a6c83f334ac28864 | Capitalization at 30.9.26 |
| 6-K_2026-09-30_investorpresotext2026.htm.jsonl | 2ac25318ab8710edaece00656540a1c90de7efab36a24b488600ed02e222986e | Third quarter 2026 call (management language) |
| context | a67d394ad1fe0320e0c68be1bf7ef2da619705355c7aa8f5e62b6171bbf4fb2d | Run settings (sector and country labels); not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2e54133f1b22d47b492e44c16bd40091878fdaaf285f1d8de08cc5d1ee03cf43 | Source readiness and limitations: quarterly reports, slides and audit-opinion text not in the pack |
| CP-1 | 685fa8e5832878fa7692e257450c83b45286cefc7233978ce033b37754932207 | Reported financial base: FY2025 statements, 2026 capitalization tables, capital and liquidity ratios, unquantified risks |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| UBS Group AG is a listed Swiss bank holding company with no sponsor or controlling holder disclosed. Its credit context is the Credit Suisse integration, a diversified fee-led model, and a pending Swiss capital-rule change that management opposes. | Medium | Transaction detail, new debt terms and the Swiss rule text are not in the pack; most 2026 facts are management statements. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Wealth management and the investment bank generate most divisional profit, and most revenue is not net interest income. | Earnings depend on fees and trading, so market conditions affect revenue durability more than lending margins do. | High |
| The 2023 Credit Suisse acquisition is nearly integrated, with cost savings and legacy wind-down on management's schedule. | Remaining execution, litigation and legacy exposure risks should fall, but the end state is a management claim until year-end. | Medium |
| Proposed Swiss rules would deduct foreign-subsidiary investments from capital; the company estimates about USD 22bn of extra CET1 at the bank subsidiary. | A large capital need could limit distributions or force structural change, but timing and final rules are unresolved. | Medium |
| No sponsor or controlling holder is disclosed; documented actions are capital returns within a stated ratio target. | Sponsor-style extraction or priming is not evidenced, but missing evidence is not proof it cannot happen. | Medium |

### Business and transaction view

The pack describes a listed bank holding company whose main creditor-relevant change is the 2023 acquisition of Credit Suisse Group AG and the integration that management says will be substantially complete at the end of 2026. The group runs five divisions, of which Global Wealth Management and the Investment Bank carry most divisional profit, and non-interest income is the larger part of revenue. No sponsor or controlling owner is disclosed, and the only holders above 3% named in the 20-F are Norges Bank and BlackRock Inc., so sponsor-behaviour analysis reduces to documented capital-return conduct. The transaction set for 2025 and 2026 consists of disposals, entity mergers, capital instruments and a liability management action in the third quarter of 2026, for which the pack gives amounts and charges but no instrument terms. The Swiss capital proposals and the legacy litigation are the main credit uncertainties and are described but not quantified by any rule text or court document in the pack.

### Company and operating model

| Fact | Category | Detail | Source and limitation |
| --- | --- | --- | --- |
| Divisional structure | Documentary Fact | Five business divisions plus Group functions: Global Wealth Management, Personal & Corporate Banking, Asset Management, the Investment Bank, and Non-core and Legacy; all five are reportable segments | 20-F page:407 |
| Global Wealth Management scale | Documentary Fact | FY2025 total revenues 25,960 USD m, operating profit before tax 5,207 USD m; invested assets USD 4.8trn of which fee-generating USD 2.1trn; lending portfolio USD 327bn; deposits USD 479bn at 31.12.25 | 20-F page:409 and page:49 to page:50 |
| Global Wealth Management revenue model | Documentary Fact | Recurring net fee income linked to fee-generating assets, plus transaction-based income and net interest income from lending and deposits | 20-F page:49 to page:50; Q3 call page:7 gives the Q3 2026 mix as management language |
| Personal & Corporate Banking | Documentary Fact | FY2025 total revenues 9,154 USD m, net interest income 5,322 USD m, operating profit before tax 2,497 USD m; Swiss retail, corporate and institutional business | 20-F page:409 and page:407 |
| Asset Management | Documentary Fact | FY2025 total revenues 3,156 USD m, operating profit before tax 719 USD m | 20-F page:409 |
| Investment Bank | Documentary Fact | FY2025 total revenues 12,340 USD m, operating profit before tax 2,819 USD m; net interest income of negative 2,938 USD m | 20-F page:409; the negative net interest line is shown as printed and its cause (funding cost allocation) is not stated in the cited pages |
| Non-core and Legacy and Group Items | Documentary Fact | Non-core and Legacy: revenues 154 USD m, loss before tax of 1,199 USD m; Group Items: loss before tax of 1,190 USD m | 20-F page:409; Non-core and Legacy holds selected former Credit Suisse positions not aligned with long-term priorities (page:407) |
| Revenue mix | Analyst Interpretation | Net interest income 7,747 USD m against non-interest income 41,826 USD m, so revenue is mainly fees and trading rather than net interest | 20-F page:409; share calculated in Calculations |
| Geography | Documentary Fact | FY2025 revenue share: Americas 36%, Asia Pacific 16%, EMEA excluding Switzerland 17%, Switzerland 32%; Switzerland holds 49% of non-current assets | 20-F page:410 |
| Cost structure | Documentary Fact | Personnel expenses 27,861 USD m, general and administrative 8,807 USD m, depreciation, amortization and impairment 3,529 USD m | 20-F page:371 |
| Capital spending | Documentary Fact | Purchase of property, equipment and software 2,362 USD m in FY2025 | 20-F page:379 |
| Working capital | Insufficient Information | Not applicable in the industrial sense for a bank; operating cash flow is dominated by balance-sheet movements (see the financial base handoff) | 20-F page:379 |
| Management ambitions | Management Language | 2026 exit-rate targets: underlying return on CET1 capital of around 15% and underlying cost / income ratio below 70%; 2028 ambition: reported return on CET1 of around 18% | 20-F page:47 to page:48; targets, not results |
| Integration savings progress | Management Language | Cumulative gross cost savings 10.7bn at the end of 2025, 13.2bn delivered by Q3 2026 and about 13.7bn expected in total | 20-F page:41; Q3 call pages:4 and 5; management claims |
| Q3 2026 trading state | Management Language | Management calls Q3 2026 a strong quarter with year-on-year profit growth in each division and a record third quarter for the Investment Bank | Q3 call pages:2 to 9; no segment statements for Q3 2026 in the pack |

### Company profile

| Item | Category | Detail | Source and limitation |
| --- | --- | --- | --- |
| Legal entity and domicile | Documentary Fact | UBS Group AG, Zurich, Switzerland; incorporated 10 June 2014 as the holding company of the UBS Group; owns 100% of UBS AG | 20-F page:36 and page:2 |
| Listing | Documentary Fact | Ordinary shares listed on the SIX Swiss Exchange and the New York Stock Exchange; ticker UBS | 20-F page:36 and page:2 |
| Reporting basis | Documentary Fact | IFRS Accounting Standards, USD presentation currency | 20-F page:3; capitalization 6-Ks page:2 and page:1 |
| Share capital | Documentary Fact | 3,341,581,714 ordinary shares, including 249,882,523 treasury shares, at 31 December 2025 | 20-F page:2 |
| Market capitalization | Documentary Fact | 155,760 USD m at 31.12.25 (shares issued multiplied by period-end share price) | 20-F page:37 and page:38 |
| Ownership class | Documentary Fact | No controlling holder or sponsor disclosed. Holders above 3% of voting rights at 31 December 2025: Norges Bank 4.90% (disclosed 22 January 2025) and BlackRock Inc. 5.01% (disclosed 30 November 2023) | 20-F page:262; Norges Bank disclosed a holding below 3% on 17 February 2026; the BlackRock notice is dated 2023 and may be stale |
| Control rights and economic interest | Insufficient Information | Voting and economic rights beyond one vote per share are not described in the pages read; percentages for other holders are not disclosed | Not inferred |
| Prior ownership | Documentary Fact | Treasury shares of 175,649,481 were transferred to Credit Suisse Group shareholders as consideration for the acquisition | 20-F page:377 and page:41 |
| Personnel | Documentary Fact | Internal and external personnel 119,589; internal full-time equivalents 103,177 at 31.12.25 | 20-F page:37 |
| Auditor | Documentary Fact | Ernst & Young Ltd, Basel, auditor of the consolidated accounts | 20-F page:14 |
| Capital guidance | Management Language | Maintain a CET1 ratio of around 14%, a CET1 leverage ratio above 4.0% and a UBS AG standalone CET1 ratio of between 12.5% and 13.0% | 20-F page:48 |
| Ratings | Insufficient Information | 2025 actions only: Moody's upgraded the long-term senior unsecured rating to A2 from A3 (stable outlook); Fitch outlook on the group Long-Term Issuer Default Rating changed to Positive; ratings in force at 2026-11-05 are not supplied | 20-F page:245 |
| Dividend and repurchase policy | Management Language | For FY2025 the Board intended to propose USD 1.10 per share; 2025 total capital returns of USD 6.4 billion | 20-F page:31 |

### Transaction summary and new debt issues

The defining transaction in the pack is the acquisition of Credit Suisse Group AG on 12 June 2023, after which UBS Group AG "succeeding by operation of Swiss law to all assets and liabilities of Credit Suisse Group AG" (20-F page:41). The 20-F states the acquisition followed a request from the Swiss Federal Department of Finance, the Swiss National Bank and FINMA (page:40). The consideration included UBS Group AG shares (treasury shares transferred, page:377) and the 20-F records negative goodwill of 27,264 USD m in FY2023 (page:371); no purchase agreement or term sheet is supplied, so deal terms beyond these statements are Not supplied. Integration is described as substantially complete at the end of 2026: UBS AG and Credit Suisse AG merged in May 2024, UBS Switzerland AG and Credit Suisse (Schweiz) AG in July 2024, and further US and EU entity mergers followed in 2025 (page:41). Management says all former Credit Suisse client migrations were complete in March 2026 (Q1 call page:3). Creditor mechanics: a simpler legal structure and decommissioned legacy systems reduce operational and resolution complexity, while the remaining Non-core and Legacy book and acquired litigation keep a tail of loss and cash-cost risk until wound down. The year-end 2026 completion claim is management language and not yet evidenced by a filed statement.

Disposals and exits around the transaction: the sale of Select Portfolio Servicing was completed in March 2025 with a gain of 97 USD m and a reduction of about USD 1.3bn in risk-weighted assets (20-F page:42); the 50% interest in Swisscard was sold to American Express with completion in January 2026, a subsequent event relative to the FY2025 period, with a gain expected in the first quarter of 2026 (page:42); the Q1 call attributes a limited tax charge to that gain (page:5); and the sale of O'Connor was completed in the first quarter of 2026 (Q1 call page:8, and "the O'Connor exit" in Q3 call page:8). Prices for these disposals are not given except where stated. Management also reports the conversion of UBS Bank USA to a national bank charter (Q1 call page:3) with product roll-out expected in 2027 (Q3 call page:12).

New debt issues and liability management: the pack does not list any individual new bond, with coupon, maturity, size or issuer; that detail is Not supplied. What it does show is (i) 2025 cash flows from issuance of debt designated at fair value and long-term debt at amortized cost of 131,476 USD m against repayments of 154,614 USD m (20-F page:379); (ii) in 2025, new issuances of AT1 capital instruments of USD 5.8 bn and a call of USD 3.2 bn equivalent of AT1 capital instruments, with loss-absorbing AT1 capital up by USD 3.5 bn to USD 19.9 bn (page:232); (iii) management's statement that the 2026 AT1 issuance plan was completed by mid-February 2026 (Q1 call page:6) and that further AT1 was pre-funded in the second quarter of 2026 (Q2 call page:5); (iv) total debt issued of 343,922 USD m at 31.3.26, 343,551 USD m at 30.6.26 and 324,981 USD m at 30.9.26; and (v) a third-quarter 2026 liability management transaction, "the repurchase of around 10 billion of high-cost Credit Suisse liabilities", which produced a charge of 346 million (Q3 call page:4). The sources do not say which instruments were repurchased, at what price, whether by tender or in the market, or whether holders were treated pro rata, so creditor treatment of that action is Insufficient Information and no conclusion is drawn on it. Management links it to lower funding drag in Non-core and Legacy and support for net interest income, which is its characterisation.

Capital returns act as a use of funds. The 20-F shows share repurchase programmes of USD 2,000 m each in 2024 and 2025 (page:377), an accrual of 3,449 USD m for the proposed 2025 dividend and a capital reserve of 3,000 USD m for expected 2026 repurchases (page:231). In 2026 management reports a USD 3 billion programme completed by the second quarter results, a further USD 3 billion programme to run to the end of the second quarter of 2027, 4.8 billion repurchased and 2.8 billion of dividend accrued year to date at Q3, and 1.2 billion more intended over the next three months (Q2 call page:3; Q3 call page:3). Management links the pace to maintaining a CET1 ratio of around 14% and to the Swiss Parliament's deliberations (Q2 call page:3). These are distributions funded from reported earnings and are conditioned on a stated capital ratio. The capital-return plan for 2027 is to be given with fourth quarter results (Q3 call page:3).

### Ownership, governance and behaviour

| Behaviour observed | Category | Evidence | Mechanic and legal-capacity link |
| --- | --- | --- | --- |
| No sponsor or controlling holder disclosed; only two holders above 3% | Documentary Fact | 20-F page:262: only two holders above 3% | No sponsor-led dividend recapitalisation or fee leakage is evidenced; sponsor alignment is not applicable. Legal capacity under governing documents is not assessed |
| Capital returns within a ratio target | Analyst Interpretation | 20-F page:48 guidance of around 14% CET1; Q3 call page:5 expects year-end ratio "at or very close to our target of around 14%" | Supportive-to-neutral: distributions are tied to a capital buffer and earnings; feasibility is shown by the ratios in the financial base handoff; willingness to reduce buybacks if capital rules tighten is stated by management only |
| Release of the integration capital buffer from 2027 | Management Language | Q3 call page:14: management intends to free up the buffer over minimum requirements from 1 January 2027 | Mixed: it can raise distribution capacity before the Swiss rule outcome is known. Management says earnings capacity allows capital to be built later (page:19). Willingness is stated, outcome not evidenced |
| Opposition to Swiss capital proposals | Management Language | Q1 call page:4 and Q3 call pages:3 and 4: proposals "not proportionate", shareholders called the "first line of defense" | Management positioning. It signals that distributions and structure may be protected against creditor-relevant capital builds; no action on this is evidenced |
| Contingency planning | Insufficient Information | Q3 call pages:10 and 17: management declines to discuss contingency plans | Not an adverse conclusion; the question was asked by analysts and not answered |
| Creditor-adverse actions (priming, uptiering, drop-downs, non-pro-rata exchanges) | Insufficient Information | None found in the sources read; the Q3 liability management action's terms are not supplied | Absence in a limited pack is not evidence of absence. Debt documents are not supplied |

### Timeline

| Date | Event | Category | Source |
| --- | --- | --- | --- |
| 10 June 2014 | UBS Group AG incorporated as holding company | Documentary Fact | 20-F page:36 |
| 12 June 2023 | Acquisition of Credit Suisse Group AG completed | Documentary Fact | 20-F page:41 |
| May and July 2024 | UBS AG merged with Credit Suisse AG; UBS Switzerland AG merged with Credit Suisse (Schweiz) AG | Documentary Fact | 20-F page:41 |
| October 2024 | Agreement to sell 50% of Swisscard to American Express | Documentary Fact | 20-F page:42 |
| March 2025 | Sale of Select Portfolio Servicing completed | Documentary Fact | 20-F page:42 |
| Fourth quarter 2025 | Gross cost-saving ambition raised to about USD 13.5bn from about USD 13bn | Management Language | 20-F page:41 to page:42 |
| January 2026 | Swisscard sale completed (subsequent to FY2025) | Documentary Fact | 20-F page:42 |
| 9 March 2026 | Annual report on Form 20-F filed | Documentary Fact | 6-K Q1 capitalization file page:2 |
| Mid-February 2026 | 2026 AT1 issuance plan completed | Management Language | Q1 call page:6 |
| March 2026 | Migration of Swiss-booked former Credit Suisse clients completed | Management Language | Q1 call page:3 |
| April 2026 (week before the 29 April call) | Announcements on bank capital regulation, as described by management | Management Language | Q1 call page:4 |
| Second quarter 2026 | New USD 3 billion repurchase programme announced | Management Language | Q2 call page:3 |
| September 2026 | Swiss Upper House outcome on capital proposals described as "very concerning" | Management Language | Q3 call page:3 |
| Third quarter 2026 | Repurchase of around 10 billion of high-cost Credit Suisse liabilities, charge of 346 million | Management Language | Q3 call page:4 |
| 28 and 29 October 2026 | Third quarter results and call; 6-Ks filed | Documentary Fact | Q3 files page:2 and page:1 |
| Not before first quarter 2027 | Decision expected on Credit Suisse AT1 litigation appeal | Management Language | Q3 call page:14; future, not a fact as of the cutoff |
| February 2027 | Strategic update with fourth quarter results | Management Language | Q3 call page:20; future |
| 1 January 2029 | Capital ordinance affects UBS capital per management | Management Language | Q3 call page:14; future |

### Regulatory and capital-rule context

- The 20-F states that proposed legislation would require deduction of investments in foreign subsidiaries of systemically important banks from CET1 capital, entering into force in 2028 at the earliest, with a 65% deduction in the first year rising by 5-percentage-point steps to 100% (page:88).
- The company states: "We currently estimate that UBS AG would be required to hold additional CET1 capital of around USD 22bn if all capital measures were implemented as proposed by the Swiss Federal Council" and that this would raise UBS Group AG's CET1 ratio to around 18.5% from its target of around 14% (page:89). The Q1 call gives the same order of magnitude, "around 22 billion", on top of 15 billion already required (page:4).
- The 20-F states FINMA's preferred resolution strategy is a single point of entry at UBS Group AG, with write-down of equity, AT1 and tier 2 and conversion of senior unsecured bonds of UBS Group AG to equity if required (page:84). This is a description of the stated strategy, not a legal interpretation of creditor ranking.
- Credit Suisse AT1 litigation: cases lodged against FINMA over the AT1 write-down, with UBS Group AG a party as successor (20-F page:113); management says no decision is expected before the first quarter of 2027 (Q3 call page:14). Provisions are in the financial base handoff; no claim amount is supplied.

### Conflicts and unreconciled items

| Item | Spans | Effect | Resolution as logged |
| --- | --- | --- | --- |
| Cost-to-achieve figure | Q1 call page:5: "we've incurred costs to achieve of around 13.7 billion at constant FX"; Q1 call page:5: cumulative gross savings of 11.5 billion and a 1.1 times multiple; Q3 call page:5: "total to around 13.7 billion" for gross cost reductions | The same figure appears for costs incurred in one call and for total gross savings in another; the multiple is not defined in the pack, so the two cannot be reconciled | Logged, not reconciled. Do not use either as a cost-to-achieve amount |
| Headcount measures | 20-F page:37: internal and external personnel 119,589 and internal full-time equivalents 103,177; Q3 call page:5: "Total headcount at quarter-end was 110 thousand" | Different bases; the call does not say which base it uses | Logged, not reconciled |

### Credit translations

- Revenue durability. Evidence: net interest income is 7,747 USD m of 49,573 USD m total revenues and Global Wealth Management earns recurring net fee income on fee-generating assets (20-F pages:409 and 49 to 50). Mechanic: revenue depends on market levels, client activity and asset flows more than on loan margins, so revenue moves with markets. Implication: debt service capacity for a group of this size rests on earnings volatility and capital buffers, not on contractual interest cover; the financial base handoff gives the capital and liquidity figures. A logged conflict that counters part of this: none on revenue; the headcount measure conflict only affects cost-per-head analysis.
- Margin and cash flow risk. Evidence: operating expenses of 40,197 USD m and a reported cost / income ratio of 81.1% for FY2025, with management targeting below 70% underlying by year-end 2026 (20-F pages:371, 37, 47). Mechanic: integration cost savings are the planned margin driver, but they require integration expenses (Q3 call page:5). Implication: the margin path depends on completing the integration; the target is management language and the cost-to-achieve conflict above limits how far the savings economics can be checked.
- Concentration risk. Evidence: Switzerland provides 32% of revenue and 49% of non-current assets, and the wealth and bank divisions carry most divisional profit (20-F pages:410, 409). Mechanic: Swiss regulation, the Swiss economy and the Swiss capital rules touch both the largest region and the group's legal structure. Implication: a Swiss rule change has outsized effect on distributions and structure; the company's own estimate of around USD 22bn extra CET1 at the bank subsidiary is the size marker.
- Sponsor alignment. Evidence: no sponsor or controlling holder disclosed (20-F page:262) and capital returns tied to a ratio target. Mechanic: there is no sponsor incentive for debt-funded extraction, but shareholder distributions compete with capital builds. Implication: monitor distribution decisions against the Swiss rule outcome; no extraction behaviour is evidenced and no conclusion on willingness is drawn.
- Key uncertainties. Swiss capital rules and timing; Credit Suisse AT1 and merger-law litigation; the unverified year-end integration completion; the unknown terms of the Q3 liability management; and ratings in force at the as-of date.

### Consumer assessments

| Consumer | Readiness | What it should take from this handoff | Gap and required action |
| --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Segment profit mix, capital-return policy and amounts, the Swiss capital estimate of around USD 22bn, resolution strategy, the Credit Suisse (USA) LLC guarantee from the financial base handoff, and the liability management action | Instrument terms, debt documents, ratings in force and rule text are not supplied; obtain them before any structural or ranking statement |
| CP-5 | READY_WITH_LIMITATIONS | Category tags and locators for every row; list of management-language items | Quarterly reports and slides are not supplied; treat every 2026 call figure as spoken and unaudited |

## Calculations

| Id | Calculation | Inputs | Result | Check |
| --- | --- | --- | --- | --- |
| C1 | Non-interest share of revenue | 41,826 / 49,573 | 84.4% | Net interest income 7,747 + non-interest income 41,826 = 49,573 (20-F page:409) |
| C2 | Personnel expense share of revenue | 27,861 / 49,573 | 56.2% | Page:371 |
| C3 | Segment profit sums to group | 5,207 + 2,497 + 719 + 2,819 - 1,199 - 1,190 | 8,853 USD m | Matches group operating profit before tax; segment revenues sum to 49,574 against 49,573, rounding |
| C4 | Four core divisions' profit before tax | 5,207 + 2,497 + 719 + 2,819 | 11,242 USD m | Non-core and Legacy and Group Items together are a loss of 2,389 USD m (1,199 + 1,190) |
| C5 | Cumulative gross cost savings path (management, bn) | 10.7 (year-end 2025) + 0.8 = 11.5; 11.5 + 1.1 = 12.6; 12.6 + 0.6 = 13.2; 13.2 + 0.5 = 13.7 | Consistent | 20-F page:41; Q1 call page:5; Q2 call page:4; Q3 call page:4 and page:5 |
| C6 | Repurchases consistency (management, bn) | 3.0 programme completed + 1.8 of the next programme = 4.8 year to date; 4.8 + 1.2 = 6.0 | Consistent with two programmes of 3.0 | Assumes the first programme was executed within 2026; Q2 call page:3 and Q3 call page:3 |
| C7 | Debt issued change, 30.9.26 against 30.6.26 | 324,981 - 343,551 | -18,570 USD m | Capitalization files; reported in the financial base handoff |
| C8 | Cost-to-achieve check | 11.5 x 1.1 = 12.65 against a stated 13.7 | Does not reconcile | The multiple is not defined in the pack; see conflicts |

Not calculable: sponsor leakage, ownership percentages beyond the two disclosed holders, new-issue terms, cost-to-achieve, and any recovery measure.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Instrument-level terms of new debt and AT1 issued in 2026 and of the Q3 2026 liability management action | High | CP-2 | Supply prospectus supplements, tender documents or press releases |
| Swiss capital rule text and final proposal; company estimate is the only size marker | High | CP-2 | Supply the proposals and parliamentary documents |
| Credit Suisse acquisition documents, merger-law and AT1 claim amounts | Medium | CP-2 | Supply litigation notes and court filings |
| Quarterly reports and slides for 2026; management claims cannot be tied to statements | Medium | CP-5 | Supply the reports and decks |
| Ratings in force at the as-of date | Medium | CP-2 | Supply agency reports |
| Cost-to-achieve and headcount figures are unreconciled | Low | CP-5 | Obtain slide definitions |
| Control rights and detail of holders below the 3% threshold | Low | CP-2 | Supply the share register disclosure if governance detail is needed |
| Events from 30 October 2026 to 5 November 2026 not supplied | Low | CP-2 | Supply later filings |

## Next module

- CP-2: take the capital structure from the financial base handoff, add the Swiss capital estimate, the resolution strategy description and the capital-return commitments from this handoff, carry the Q3 2026 liability management action as terms-unknown, and treat the Credit Suisse (USA) LLC guarantee as the only guarantee located so far.
- CP-5: trace every management-language row to its call page and keep it separate from 20-F facts; carry the two logged conflicts as unresolved.
