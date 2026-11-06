## Request

Module: business and transaction context (company, operating model, ownership, governance and sponsor behaviour, transactions and new debt, timeline, credit translations) for Brightstar Lottery PLC (issuer id brsl, NYSE: BRSL), pathway credit snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05. The context names USD as the reporting currency, current period q2-2026 and prior period fy-2025; it lists no transaction terms, quotes, ratings, sponsor or attached legal documents. Figures are US$ millions unless stated and reuse the financial base handoff; the euro is quoted where a contract is in euros.

This module consumes two handoffs. The readiness handoff limits it (nothing after the August 4, 2026 interim report; no concession agreement, sale agreements, indentures or credit agreements; decks read as text only). The financial base handoff supplies the figures, and this module corrects it in one place (see Conflicts and corrections): the unexplained 9 difference in December 31, 2025 net debt is explained by the 20-F itself. It also corrects the readiness handoff on one point: the ownership percentage of the Italian Lotto joint venture is stated in the 20-F (61.5%).

Short names in locators: 20-F is the FY2025 annual report; Q1 6-K and Q2 6-K are the interim reports for March 31, 2026 and June 30, 2026; Q4 deck, Q1 deck and Q2 deck are the earnings presentations. A locator reads (source page:N) with a verbatim quote where one is given.

## Sources

### Issuer sources relied on

| Short name | Source file (exact name) | sha256 | Use in this module |
| --- | --- | --- | --- |
| 20-F | 20-F_2025-12-31_igt-20251231.htm.jsonl | 1c18bf53e9995ce6c2aca12af6c18a64523551fba3492e8f989685fea08386fa | Business overview, risk factors, ownership, related parties, sale of the gaming business, debt note |
| Q3-25 6-K | 6-K_2025-09-30_brightstar-9302025xform6k.htm.jsonl | d46e904b239bdfcdf629b7154b5f837586e94b09f3d9adb6cf2a3a22cad2c307 | Read for context only; no fact in this module is taken from it |
| Q1 6-K | 6-K_2026-03-31_brightstar-3312026xform6k.htm.jsonl | bd68ab805934e86ab47882d408ef93ab3b6ce1b76f45e4a9303ec66c324fbd07 | Revolving facility refinancing and term loan prepayment in 2026 |
| Q2 6-K | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 59ad2951e3fb4482f8541a5bd23eebbb988b008e57b642801a0675f3dc319de2 | Latest operating results, final Lotto installment, restructuring, distributions, subsequent events |
| Q4 deck | 6-K-EX-99.2_2025-12-31_q425earningsslidedeck-fi.htm.jsonl | 52d9fd83276756c04d4933b539c2d599c1b0335f475eb7ae194b8d0285bb64ab | Revenue by geography, net debt figure (management claims) |
| Q1 deck | 6-K-EX-99.2_2026-03-31_q126earningsslidedeckfin.htm.jsonl | 904bf049bdca8cf2ecdea2a5b2e5271032b7a15662b32cecb7e8b6ac25de48c2 | Brightstar share of the final Lotto installment (management claim) |
| Q2 deck | 6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | 2e4571f9e2637bd424291bf68428c53b010290fd8734caabd6c6df90116096fc | Strategy, savings programme, outlook (management claims) |

The 20-F, Q1 6-K and Q2 6-K are filed statements and control their facts. The decks are issuer presentations and carry the category Management Language where used.

### Run settings (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context | 5dec6fdc4bf237796c486a0095b8a59b71b216970050467cf9aed314b06e0f82 |

### Handoffs

| Module | Handoff | sha256 |
| --- | --- | --- |
| CP-0 | Source readiness for Brightstar Lottery PLC | 2272d9d74d9d7f19568da51f3a2c80f84dc9432a75a7be1a1d26161cd2bf1768 |
| CP-1 | Financial base for Brightstar Lottery PLC | 015c9f0c9127b25cc24bccb61512f935749a711ecf6358ec0969afa9d5638e98 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Brightstar is a pure-play lottery operator with long government contracts, a controlling shareholder and a large Italian exposure. It has just paid for the new Italian Lotto license and renewal risk on the Scratch and Win license falls in 2028. | Medium | No concession agreement, consortium terms or reporting after August 4, 2026 is supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Italian Lotto and Scratch and Win licenses produced about 18% and 19% of FY2025 revenue; the Scratch and Win license expires in September 2028. | A renewal or upfront fee in 2028 would coincide with $798 million of 2028 debt maturities. | Medium |
| De Agostini holds 46.29% of the shares and 63.28% of the votes and controls the company. | Distribution, leverage and financing decisions sit with one holder; term loan caps limit distributions. | High |
| The sale of the gaming business on July 1, 2025 funded debt repayment and a plan to return $1.1 billion to shareholders. | Debt fell and distributions were large; the 2026 cash need for the Lotto license was met partly by partners and the revolver. | High |
| Partners share the Italian Lotto joint venture, and non-controlling interests took more income than the whole group earned in FY2025. | Consolidated EBITDA overstates cash available to the parent's own creditors. | Medium |
| Top ten customers outside Italy supplied about 35% of FY2025 revenue and one of them left in August 2025. | Customer losses and weak jackpot activity reduce revenue quickly. | Medium |

### Business and transaction view

The business is a contracted, wager-linked lottery services company whose creditor-relevant features sit in four places. First, revenue visibility is high on paper, with about 92% of FY2025 revenue from long-term operating, facilities management and lottery management contracts, but U.S. contracts can be ended by the lottery authority at will with limited notice and the two Italian licenses together supplied about 37% of revenue. Second, the Italian licenses are the key transaction exposure: the new nine-year Lotto license cost an upfront fee of €2,230 million, paid in three installments ending April 24, 2026, and it is now amortized against revenue; the Scratch and Win license expires in September 2028. Third, control is concentrated in De Agostini with 63.28% of votes, and the documented behaviour since the sale of the gaming business on July 1, 2025 is debt reduction alongside large shareholder distributions, within term loan limits whose current text is not supplied. Fourth, the Italian Lotto structure shares cash flow with partners, so consolidated figures include cash that belongs partly to non-controlling interests. The evidence is adequate for a business-context fact pack, but the concession terms, the consortium agreements and any event after August 4, 2026 are not in the pack.

### Company and operating model

| Area | Fact | Category | Evidence | Credit mechanic and implication |
| --- | --- | --- | --- | --- |
| Revenue model | Fees are mainly a percentage of lottery wagers paid by the lottery authority | Documentary Fact | 20-F page:41, "service fees paid to the Company directly by the lottery authority" | Revenue moves with wagers and jackpot activity, not with fixed charges, so volume shocks pass straight to EBITDA and debt service |
| Contract share | Operating contracts, facilities management and lottery management agreements are the bulk of revenue | Documentary Fact | 20-F page:10, "equal to approximately 92% of its total consolidated revenues" | High contracted share supports revenue visibility, subject to termination rights and renewals |
| Contract length | Typical service contracts run five to ten years; remaining weighted term of facilities management contracts is 5.1 years at December 31, 2025 | Documentary Fact | 20-F page:38, "Typical service contracts range from five (5) to ten (10) years in duration"; 20-F page:41, "was 5.1 years (7.6 years including available extensions)" | Rolling renewal needs every year; a bid loss removes revenue and the invested equipment base |
| Termination rights | Many U.S. contracts permit termination at will | Documentary Fact | 20-F page:10, "permit the lottery authority to terminate the contract at will with limited notice" | Stated term overstates visibility for U.S. contracts; the filing gives no compensation on termination for many of them |
| Capital intensity | The company owns the technology and funds capital investment during the contract | Documentary Fact | 20-F page:41, "is responsible for capital investments throughout the duration of the contract"; Q2 6-K page:27, "Capital expenditures of $190 million are anticipated in the second half of 2026" | Capex front-loads cash needs on new wins and renewals, which competes with distributions and debt reduction |
| Italian concentration | Italian Lotto and Scratch and Win licenses each supplied a high share of FY2025 revenue | Documentary Fact | 20-F page:9, "approximately 18%, at both periods"; "approximately 19% and 17%, respectively" | One regulator (ADM) controls about 37% of revenue by license; annulment, early termination or non-renewal is a stated material risk |
| Italian license mechanics | Licenses run about nine years, are not renewable unless the license says so, and assets pass to the State free of charge at end or revocation | Documentary Fact | 20-F page:47, "are not renewable unless indicated in the licensing agreement"; "transfer to the State, free of charge, the assets that are necessary to operate the license" | Value of the license assets is lost at expiry, so the upfront fee is recovered only through the license term; this shapes recovery mechanics |
| Geography | FY2025 revenue by region: U.S. and Canada, Italy, Rest of world | Documentary Fact | Q4 deck page:8, "Italy 258 251 3% (6%) 1,018 968" | Italy and euro exposure also drives euro debt (about two thirds of principal); euro moves change dollar revenue and dollar debt together |
| Customer concentration | Top ten customers outside Italy supplied a stated share of FY2025 revenue | Documentary Fact | 20-F page:10, "top 10 customers outside of Italy accounted for approximately 35%" | Loss of any large customer lowers revenue sharply |
| Customer loss | The UK lottery moved to another supplier in August 2025 | Documentary Fact | 20-F page:10, "approximately $37 million and $54 million in revenues in 2025 and 2024" | Shows renewal risk in practice; Q2 6-K page:24 attributes a $15 million reduction in Q2 2026 service revenue to the UK transition |
| Incentive volatility | Lottery management agreements carry incentives and shortfalls tied to multi-state jackpots, accrued over a fiscal year ending June 30 | Documentary Fact | 20-F page:10, "In 2025, the change in the incentive payment was reduced by $51 million, mainly due to lower MSJP activity."; 20-F page:44, "fiscal year, which ends June 30" | Earnings depend on jackpot cycles outside management control; this is a margin and cash-flow risk |
| Upfront license fees | License fees are paid in cash and amortized as a deduction from revenue; Adjusted EBITDA adds the amortization back | Documentary Fact | 20-F page:53, "Upfront license fee amortization (223) (198)"; Q2 6-K page:12, "Italian Lotto 9 years December 2025 2,376 2,596" | Reported revenue and income are lower than cash-based revenue; the cash was spent in 2025 and 2026, so EBITDA and cash flow diverge |
| Joint venture economics | The Italian Lotto manager is 61.5% owned by the company's Italian subsidiary; partners hold the rest | Documentary Fact | 20-F page:40, "Lottoitalia is 61.5% owned by Brightstar Lottery S.p.A." | Partner share of profit and the capital they contributed leave the group as distributions; see credit translations |
| Partner profit share | Net income attributable to non-controlling interests from continuing operations exceeded total income from continuing operations in FY2025 | Analyst Interpretation | 20-F page:138, "Income from continuing operations 135 271 265" and "Less: Net income attributable to non-controlling interests from continuing operations 136 154 149" | Cash distributions to partners are a recurring claim on consolidated cash flow ahead of shareholders |
| Working capital | Trade receivables are sold under factoring agreements | Documentary Fact | Q2 6-K page:12, "We factored trade receivables of $264 million" | Factoring supports operating cash flow; a withdrawal would raise working capital needs |
| Foreign exchange | Euro/dollar movements affect revenue, net income and net debt | Documentary Fact | 20-F page:52, "The Company is particularly exposed to movements in the Euro/U.S. dollar exchange rate." | Euro debt makes dollar leverage move with the exchange rate |
| Cost programme | Management targets higher annual savings by 2028 under the restructuring programme | Management Language | Q2 deck page:7, "Accelerating & Upgrading OPtiMa Cost Savings to ~$100M by 2028" | Savings are a management target; restructuring cash is paid through 2032 per the Q2 6-K page:13 |
| Growth initiatives | Management cites digital lottery and Italy consumer growth | Management Language | Q2 deck page:5, "iLottery Wagers Up 22%" | Growth spending is a stated use of cash in FY2026; no incremental revenue is evidenced here |

### Company profile

| Attribute | Value | Category | Evidence |
| --- | --- | --- | --- |
| Legal name and former name | Brightstar Lottery PLC, formerly International Game Technology PLC | Documentary Fact | 20-F page:4, "In July 2025, the Parent changed its corporate name from International Game Technology PLC to Brightstar Lottery PLC" |
| Legal form and listing | Public limited company under the laws of England and Wales, organized in 2014; NYSE: BRSL | Documentary Fact | 20-F page:37, "organized in 2014 as a public limited company under the laws of England and Wales" |
| Headquarters | London, with principal operating facilities in Providence, Rhode Island and Rome, Italy | Documentary Fact | 20-F page:37, "headquartered in London, United Kingdom" |
| Sector and country | Services - miscellaneous amusement and recreation (context); United Kingdom | Documentary Fact | context settings; 20-F page:37 |
| Business description | Pure-play global lottery operator: lottery management, instant ticket and iLottery services | Documentary Fact | 20-F page:37, "As a pure-play global lottery company" |
| Reporting | US GAAP, US dollars, single segment, fiscal year ending December 31 | Documentary Fact | 20-F page:4, "reports a single segment for the purposes of assessing performance and making operating decisions" |
| Customers | About 90 customers, including 37 of the 48 U.S. lotteries | Documentary Fact | 20-F page:38, "nearly 90 customers worldwide, including to 37 of the 48 U.S. lotteries" |
| Installed base | More than 350,000 point-of-sale devices | Documentary Fact | 20-F page:38, "more than 350,000 point-of-sale devices" |
| Employees | About 5,815 at December 31, 2025 | Documentary Fact | 20-F page:37, "approximately 5,815 employees at December 31, 2025" |
| Controlling shareholder | De Agostini S.p.A.: 46.29% of ordinary shares and 63.28% of votes at February 19, 2026 | Documentary Fact | 20-F page:90, "De Agostini S.p.A. 85,422,324 46.29% 85,422,324 63.28%" |
| Ultimate ownership of De Agostini | B&D Holding S.p.A. owns 61.69% of De Agostini | Documentary Fact | 20-F page:91, "owned 61.69% of De Agostini" |
| Italian Lotto license | Exclusive license to November 2034 through Lottoitalia | Documentary Fact | 20-F page:40, "for a term expiring in November 2034" |
| Scratch and Win license | Exclusive license to September 2028 through Lotterie Nazionali, 64.0% owned | Documentary Fact | 20-F page:40, "for a term expiring in September 2028"; "a joint venture 64.0% owned by" |
| Revenue weighted-average remaining term of Italian licenses | 5.6 years at December 31, 2025 | Documentary Fact | 20-F page:40, "the revenue weighted-average remaining term of these Italian licenses was 5.6 years" |
| Auditor | PricewaterhouseCoopers LLP, auditor since 2015, unqualified opinions at December 31, 2025 | Documentary Fact | 20-F page:121, "has been serving as the Company’s independent auditor since 2015" |
| Credit ratings at December 31, 2025 | Fitch BBB-, Moody's Ba1, S&P BB+ on the senior secured notes; no later ratings supplied | Documentary Fact | 20-F page:168, "rated BBB- by Fitch Ratings, Inc." |
| Sponsor | None; the controlling holder is a strategic shareholder, not a financial sponsor | Analyst Interpretation | 20-F page:91, "De Agostini controls the Parent" |

### Transaction summary and new debt issues

Sale of the gaming and digital business. On July 1, 2025 the company completed the sale of IGT Gaming to a holding company owned by funds managed by affiliates of Apollo Global Management, pursuant to agreements entered into on July 26, 2024. The 20-F records total consideration, net of $134 million of cash and restricted cash transferred, of $4.1 billion and a pre-tax gain of $112 million (20-F page:156). The business is a discontinued operation, so every continuing-operations comparative excludes it. Continuing involvement is limited to licensing between the two groups, a 60.0% interest in Rhode Island VLT Company LLC whose economic benefits were transferred to IGT Gaming, and a guarantee of a lease of IGT Gaming that expires September 30, 2032 with maximum base-rent exposure of $94 million at June 30, 2026 (Q2 6-K page:17 and page:18). A receivable from the buyer of $21 million at June 30, 2026 will be collected through 2027 (Q2 6-K page:17). De Agostini retained an investment in the combined private company (20-F page:156); its size is not stated in the text read.

Use of proceeds. The filings state two uses. First, debt repayment: on the sale the company redeemed the 4.125% dollar notes due April 2026 and the 3.500% euro notes due June 2026 and prepaid euro term loan and revolver amounts, and the interim notes say $2 billion of debt was required to be repaid within six months of closing (20-F page:170; Q2 6-K page:17). Second, shareholder returns: the 20-F describes a "previously announced plan to return $1.1 billion of net cash proceeds from the IGT Gaming divestiture to shareholders" (20-F page:58). Execution documented in FY2025 includes a special dividend of $600 million (Q4 deck page:6, management claim), a $250 million accelerated share repurchase and a total of $770 million of cash dividends and $271 million of repurchases for the year (20-F page:123 and page:139).

Italian Lotto license. On July 16, 2025 the regulator notified that the consortium led by Brightstar had been awarded the Italian Lotto license for nine years from December 1, 2025. The upfront fee was €2,230 million, paid as €500 million on July 17, 2025, €300 million on November 28, 2025 and €1,430 million ($1,675 million) on April 24, 2026 (20-F page:163; Q2 6-K page:12). The Q1 deck states Brightstar's share of the final installment as €879 million or $1.03 billion (Q1 deck page:6, management claim); that share equals about 61.5% of €1,430 million, consistent with the stated ownership of Lottoitalia. Partners funded their share through non-controlling interest capital increases of $650 million in the first half of 2026 (Q2 6-K page:5). The license is amortized against revenue from December 2025 and the Q2 deck states that about $175 million of incremental Lotto-related service revenue amortization affects FY2026 reported growth (Q2 deck page:7, management claim).

New debt issues and refinancing. In September 2024 Brightstar Lottery Holdings B.V. issued €500 million of 4.250% notes at par (20-F page:170). In March 2025 the Parent and Brightstar Lottery S.p.A. entered into a facilities agreement for two €500 million term loans due September 2030, one used to repay revolver borrowings and one to fund the share of the Lotto fee (20-F page:171). In December 2025 the Parent and a subsidiary as co-issuers issued $750 million of 5.750% senior secured notes due January 2033 at par and used the proceeds and cash to redeem the $750 million 6.250% notes due January 2027 at 101.22%, with a $10 million loss on extinguishment (20-F page:169 and page:170). In March 2026 the company signed new senior secured revolving credit facilities of $650 million and €1.0 billion expiring March 2031, effective April 2026, cancelled both revolvers due July 2027 and amended the 2030 term loans to align provisions; in April 2026 it prepaid the remaining €200 million of the January 2027 term loan from revolver borrowings (Q2 6-K page:15). The June 30, 2026 principal is $4,383 million with the first maturity of $228 million in 2027 (see the financial base). Documented status of all items above: completed. No debt issuance is documented after June 30, 2026.

Subsequent events to the latest report: a dividend of $0.23 per share declared July 30, 2026, repurchases of $10 million to July 31, 2026, and the July 10, 2026 payment of a Mexican tax settlement (Q2 6-K page:17, page:18, page:19). Nothing after August 4, 2026 is supplied.

### Ownership, governance and sponsor behaviour

| Topic | Fact | Category | Evidence | Legal capacity, willingness and feasibility |
| --- | --- | --- | --- | --- |
| Control | De Agostini controls through special voting shares tied to its shares; it does not hold different voting rights except through that election | Documentary Fact | 20-F page:91, "De Agostini controls the Parent but does not have different voting rights from the Parent" | Capacity: it can approve dividends, indebtedness and mergers by vote. Willingness: no creditor-adverse action is documented. Feasibility: not applicable |
| Ownership change | De Agostini's stake was 45.7% of shares and 62.7% of votes at December 31, 2025 and 46.29% and 63.28% at February 19, 2026 | Documentary Fact | 20-F page:190, "economic interest of approximately 45.7%" and 20-F page:90 | Stake rose between the two dates as shares were repurchased; a later date is not supplied |
| Board access | De Agostini may appoint a board observer; renewed to the meeting reviewing third quarter 2027 results | Documentary Fact | 20-F page:63, "permitting De Agostini to appoint an observer to attend meetings of the Parent" | Information rights beyond voting; no creditor impact documented |
| Related parties | Transactions with De Agostini cover support services and rented office space; trade payables to it were 2 at December 31, 2025 | Documentary Fact | 20-F page:190, "payments for support services provided and office space rented" | Small and arm's-length by description; no leakage documented |
| Dividend policy | No formal policy; dividends need board approval | Documentary Fact | 20-F page:92, "has not yet implemented a formal policy on dividend distributions" | Capacity not constrained by policy; term loans cap distributions (below) |
| Distribution capacity | Term loan agreements limited dividends and repurchases to $400 million per year if two ratings are below Ba1/BB+, $550 million if at or above, and permitted amounts up to the sale proceeds less $2 billion until January 1, 2027 | Documentary Fact | 20-F page:171, "limits the aggregate amount that the Parent can pay with respect to dividends and repurchases of ordinary shares in each year" | Capacity at December 31, 2025; March 2026 amendment text is not supplied, so current capacity cannot be stated |
| Distributions made | FY2025 cash dividends 770 and repurchases 271; H1 2026 dividends 85 and repurchases 45 | Documentary Fact | 20-F page:139, "Dividends paid (770) (161) (160)"; Q2 6-K page:5, "Dividends paid (85) (81)" | Willingness: large payouts after the sale; see calculation below |
| Deleveraging | Carrying debt fell from 5,361 at December 31, 2024 to 4,178 at December 31, 2025 and was 4,354 at June 30, 2026 | Documentary Fact | 20-F page:168, "Total debt 4,203 (25) 4,178 5,396 (35) 5,361"; Q2 6-K page:14 | Supportive in 2025; debt rose in H1 2026 as the Lotto payment was financed with the revolver and partner capital |
| Funding of 2026 distributions | H1 2026 free cash flow was negative while shareholders received 130 | Analyst Interpretation | Q2 6-K page:5, "Net cash (used in) provided by operating activities from continuing operations (1,174) 473" | Feasibility: payouts were small against the Lotto payment, funded from cash, the revolver and partner capital; no creditor-adverse mechanic documented |
| Creditor-adverse actions | No priming, uptiering, drop-down, collateral release or non-pro-rata exchange is documented in the supplied sources | Insufficient Information | Not located in 20-F page:168 to page:176 or Q2 6-K page:14 to page:15 | Absence in the supplied text is not proof; indentures are not supplied |
| Behaviour category | Supportive or Neutral or Mixed: debt reduction and transparent reporting beside large payouts and partner leakage; no extraction mechanic documented | Analyst Interpretation | 20-F page:58, 20-F page:168 | Python scores the dimension; no score is stated here |

### Timeline

| Date | Event | Category | Evidence |
| --- | --- | --- | --- |
| 1998 | Became exclusive licensee of the Italian Lotto (management began in 1994) | Documentary Fact | 20-F page:40, "Since 1998" |
| 2004 | Became exclusive Scratch and Win licensee, term to September 2028 | Documentary Fact | 20-F page:40, "Since 2004" |
| July 26, 2024 | Transaction Agreements signed for the sale of the gaming business | Documentary Fact | 20-F page:141, "entered into on July 26, 2024" |
| September 2024 | EUR 500 million 4.250% notes due March 2030 issued | Documentary Fact | 20-F page:170, "In September 2024, Brightstar Lottery Holdings B.V. issued €500 million of the 4.250% Notes at par." |
| March 2025 | Senior facilities agreement for two EUR 500 million term loans due September 2030 | Documentary Fact | 20-F page:171, "In March 2025, the Parent, Brightstar Lottery S.p.A." |
| July 1, 2025 | Sale of the gaming business completed; name changed to Brightstar Lottery PLC in July 2025 | Documentary Fact | 20-F page:141, "On July 1, 2025, the Company completed the sale" |
| July 16, 2025 | Notified of the Italian Lotto license award | Documentary Fact | Q2 6-K page:12, "On July 16, 2025, the Company was notified by the Agenzia delle Dogane e dei Monopoli" |
| August 2025 | UK lottery transitioned to another supplier | Documentary Fact | 20-F page:10, "In August 2025, Allwyn UK" |
| December 1, 2025 | New nine-year Italian Lotto license effective | Documentary Fact | Q2 6-K page:12, "effective as of December 1, 2025" |
| December 2025 | USD 750 million 5.750% notes due January 2033 issued; 6.250% notes due January 2027 redeemed December 16, 2025 | Documentary Fact | 20-F page:169, "issued $750 million of 5.750% Senior Secured Notes due January 2033" |
| February 24, 2026 | FY2025 annual report signed | Documentary Fact | 20-F page:133, "Dated: February 24, 2026" |
| March 2026 | New revolving credit facilities agreement; effective April 2026 | Documentary Fact | Q2 6-K page:15, "In March 2026, Brightstar Lottery PLC, together with certain of its subsidiaries" |
| April 24, 2026 | Final Italian Lotto installment paid | Documentary Fact | Q2 6-K page:12, "On April 24, 2026, LottoItalia paid the final installment" |
| Q2 2026 | Third phase of the restructuring programme started | Documentary Fact | Q2 6-K page:13, "During the second quarter of 2026, we initiated the third and final phase" |
| Subsequent event: July 30, 2026 | Dividend of $0.23 per share declared | Documentary Fact | Q2 6-K page:18, "On July 30, 2026, the Board declared a quarterly cash dividend of $0.23 per share." |
| Subsequent event: July 2026 | Repurchases of 0.9 million shares for $10 million to July 31, 2026 | Documentary Fact | Q2 6-K page:19, "As of July 31, 2026, the Parent repurchased 0.9 million ordinary shares" |
| Subsequent event: August 4, 2026 | Second quarter interim report signed | Documentary Fact | Q2 6-K page:31, "Dated: August 4, 2026" |
| September 2028 | Scratch and Win license expiry (future date) | Documentary Fact | 20-F page:40, "for a term expiring in September 2028" |
| November 2034 | Italian Lotto license expiry (future date) | Documentary Fact | 20-F page:40, "for a term expiring in November 2034" |

### Conflicts and corrections

| Item | Spans | Effect | Treatment |
| --- | --- | --- | --- |
| December 31, 2025 debt carrying value | The debt note total is "Total debt 4,203 (25) 4,178 5,396 (35) 5,361" (20-F page:168) and the fair value note says "The carrying amount of long-term debt was $4,169 million and $5,361 million" (20-F page:164) | A 9 difference. The Q4 deck net debt of 2,723 equals 4,169 less cash of 1,446; the financial base used 4,178 and derived 2,732 | Logged, not reconciled; the financial base figure stays on the balance sheet value, and this module explains the earlier unexplained difference |
| 5.750% notes co-issuer name | "Parent/Brightstar Global Solutions Corporation" in the table and "Brightstar Lottery Global Solutions Corporation" in the paragraph (20-F page:169) | Entity naming unresolved; guarantor and issuer identity matter for structure | Logged; both spellings carried |
| De Agostini percentage | 62.7% of votes at December 31, 2025 (20-F page:190) and 63.28% at February 19, 2026 (20-F page:90) | Different dates, not a restatement | Both kept with dates |
| Readiness handoff statement on consortium ownership | The readiness handoff said the Italian Lotto ownership percentage was not located | The 20-F states 61.5% for Lottoitalia (20-F page:40) | Corrected here; the readiness handoff is not edited |
| Consortium member naming | The 20-F names the manager's partners as "Italian Gaming Holding a.s." (20-F page:40) and the license note names the consortium as Allwyn, Arianna 2001 and Novomatic Italia (20-F page:163) | Whether the two names refer to one group is not stated | Logged; no equivalence assumed. Allwyn UK is also named as a customer lost in August 2025 (20-F page:10) |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence |
| --- | --- | --- | --- | --- |
| Revenue durability | About 92% of FY2025 revenue is from long-term contracts; remaining weighted terms are 5.1 years for facilities management contracts and 5.6 years for the Italian licenses (20-F page:10, page:41, page:40) | Contract renewals and tenders arrive continuously; many U.S. contracts can be terminated at will; the UK loss shows a $37 million revenue loss in FY2025 | Revenue is visible but not locked; monitor renewals and tenders as an event risk to EBITDA | Analyst Interpretation: the Lotto license now runs to November 2034 |
| Italian license renewal and funding | Scratch and Win expires September 2028 and licenses are not renewable unless stated; the Lotto fee was €2,230 million (20-F page:40, page:47, page:53) | A new license may need a large upfront payment while 2028 debt maturities of $798 million are due; the Scratch and Win renewal terms are unknown | Refinancing and liquidity pressure could cluster in 2028; this is a mechanic, not a forecast | None in the sources on the renewal terms |
| Margin and cash-flow risk | Upfront fee amortization reduces revenue (223 in FY2025, 201 in H1 2026) and Adjusted EBITDA adds it back; partners take distributions (163 in H1 2026) | Reported EBITDA is not cash available to the parent's creditors; partner leakage and capex precede debt service | Net debt leverage of 3.24x understates the burden of partner claims | Management states $400M or more of annual free cash flow after the 2025-2028 capex cycle (Q2 deck page:5, Management Language) |
| Concentration | Italy about 37% of revenue by license, top ten non-Italian customers about 35% | One regulator or a few customers can change revenue quickly | Event risk with limited diversification | Revenue is spread over about 90 customers (20-F page:38) |
| Controlling holder alignment | De Agostini holds 63.28% of votes; large payouts followed the sale; debt fell in 2025 and rose in H1 2026 | Control lets one holder set distribution and leverage policy; term loan caps are the main creditor protection and their current text is unknown | Monitoring posture: distribution policy and ratings-linked caps | Debt reduction and the investment-grade rating from one agency support alignment (20-F page:168) |
| Key uncertainty | No reporting after August 4, 2026, no concession or consortium agreements, no covenant levels | Events and terms that drive refinancing cannot be seen | Committee readiness is limited | Not applicable |

### Consumers

| Module | Readiness | What to take from this module | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Italian license exposure and 2028 renewal, control by De Agostini, partner leakage, customer concentration, sale-funded deleveraging and payouts | These shape business risk and the quality of EBITDA behind leverage | Obtain the concession and consortium terms and any report after August 4, 2026; treat distribution caps as unknown after March 2026 |
| CP-5 evidence trace validator | READY_WITH_LIMITATIONS | Each row carries a category, page and quote; conflicts are logged, not reconciled | Lets the validator test quotes and see where management language is used | Deck rows cite text extracts only; check them against slide text, not charts |

## Calculations

| Calculation | Inputs and locators | Result |
| --- | --- | --- |
| Italian license share of FY2025 revenue | 18% (Lotto) + 19% (Scratch and Win) (20-F page:9) | 37%, a sum of two printed percentages |
| Regional share of FY2025 revenue | U.S. and Canada 1,176; Italy 1,018; Rest of world 317 over total 2,511 (Q4 deck page:8; 20-F page:138) | 46.8%; 40.5%; 12.6% |
| Brightstar share of the final Lotto installment | 879 / 1,430 (Q1 deck page:6; Q2 6-K page:12) | 61.5%, equal to the stated Lottoitalia ownership |
| Net debt on the fair value note carrying amount | 4,169 - 1,446 (20-F page:164, page:137) | 2,723, equal to the Q4 deck figure; filing-derived on the balance sheet value is 2,732 |
| Cash dividends and repurchases since July 1, 2025 to June 30, 2026 | (770 - 81) + 271 + 85 + 45 (20-F page:139; Q2 6-K page:5) | 1,090 |
| Indicative size of the permitted distribution amount to January 1, 2027 | 4,100 - 2,000 (20-F page:171) | 2,100; indicative arithmetic only, because the basket definition, what counts against it and the March 2026 amendment are not supplied, so headroom is Not calculable |
| Income attributable to non-controlling interests against total income, FY2025 | 136 against 135 (20-F page:138) | 136 exceeds 135 |
| Cost of services over revenue, FY2025 | 1,116 / 2,511 (20-F page:138) | 44.4% |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Not supplied: any report after August 4, 2026, including third-quarter 2026 results | High | Synthesis, validator | Obtain the latest 6-K and deck if filed by 2026-11-05 |
| Not supplied: Italian Lotto concession agreement, consortium or shareholder agreements, and Scratch and Win license terms and renewal conditions | High | Synthesis | Obtain from the issuer or registry; needed for partner distributions and the 2028 renewal |
| Not supplied: indentures, credit agreements, guarantor list and the March 2026 term loan amendment | High | Synthesis | Obtain to state distribution caps, security and priming protection |
| Not supplied: covenant certificate and covenant levels | High | Synthesis | Obtain the revolver agreement |
| Not located: size of De Agostini's investment in the combined private company that bought the gaming business | Low | Synthesis | Check related-party notes in later filings |
| Not located: consortium partner ownership in Lotterie Nazionali beyond the remainder owned by Scientific Games Corporation and Arianna 2001, and the identity link between "Italian Gaming Holding a.s." and Allwyn | Low | Validator | Resolve from the exhibits listed in the 20-F |
| Organization chart in the 20-F is a diagram and was not read; the subsidiary list is exhibit 8.1, not in the pack | Medium | Synthesis | Obtain exhibit 8.1 |
| Deck evidence is text extracts only; charts were not inspected | Low | Validator | Use filed statements where a deck figure is also filed |
| Ratings after December 31, 2025 not supplied | Medium | Synthesis | Obtain current ratings |

## Next module

The fundamental credit synthesis (CP-2) follows, then the evidence trace validator (CP-5). Carry forward: (1) leverage of 3.24x at June 30, 2026 on management's Adjusted EBITDA and 4.48x without the license-fee add-back, from the financial base; (2) the two Italian licenses at about 37% of revenue with Scratch and Win expiring in September 2028 beside $798 million of 2028 maturities; (3) De Agostini control with 63.28% of votes and ratings-linked distribution caps whose current text is unknown; (4) partner leakage through 61.5% ownership of Lottoitalia and 163 of non-controlling interest distributions in H1 2026; (5) the correction that the 9 difference in December 31, 2025 net debt comes from the 20-F carrying amount of 4,169 against 4,178; and (6) the evidence cut-off of August 4, 2026.
