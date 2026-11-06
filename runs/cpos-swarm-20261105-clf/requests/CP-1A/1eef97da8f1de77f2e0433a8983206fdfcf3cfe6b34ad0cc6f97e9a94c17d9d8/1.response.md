# CP-1A — Business and transaction context: CLEVELAND-CLIFFS INC. (clf)

## Request

- Issuer: CLEVELAND-CLIFFS INC. (issuer id `clf`, NYSE: CLF), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; amounts are US$ millions unless a row says otherwise. Current period Q3 2026; prior period FY2025 (context `run`).
- Run: `clf-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5. This is CP-1A, the business and transaction fact pack.
- Execution: host session. The analyst read the pinned page files and wrote this answer. No provider was called. No external (non-pack) material is used anywhere in this answer.
- Reader question: which transaction, business, ownership and operating facts matter most to the creditor? Decision drivers: transaction and ownership structure; business and operating model; credit-relevant history or change.
- Category tags used in tables: Documentary Fact (a cited source states it), Management Language (management's characterisation, quoted and qualified, not adopted), Analyst Interpretation (reading of cited evidence), Insufficient Information (evidence missing; the missing datapoint is named).
- Prohibited and not done: no peer ranking, no instrument recommendation, no recovery conclusion, no score.
- Locators: `page:N` is the source chunk number in the pinned `.jsonl` file, not the printed page number. "10-Q Q3" is the 10-Q for the quarter ended September 30, 2026; "Release Q3" is the Exhibit 99.1 dated October 19, 2026; "Release Q1" and "Release Q2" are the April 20 and July 23, 2026 releases.

## Sources

Issuer sources relied on (name and pinned sha256):

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_clf-20251231.htm.jsonl | 4c221bc0965bff2fddf7c4bff630fa79a69227de30709426ec9a8c89ce97e2df | Business description, strategy, markets, customers, raw materials, labor, legal proceedings, acquisitions, debt issuance, capital stock |
| 10-Q_2026-03-31_clf-20260331.htm.jsonl | cdb78421e299c29e406bbc729a020af9f5e9e2600a8725769f4fc9cce3f48238 | Strategy text on asset sale processes (page:34), Q1 2026 events |
| 10-Q_2026-06-30_clf-20260630.htm.jsonl | e0ba1bee447b92cbe2b9ad67268169c4ba2e392089bcf206be2b86a11c01f94b | Q2 2026 events, comparison of strategy wording |
| 10-Q_2026-09-30_clf-20260930.htm.jsonl | c3188e1da0b49175580c8c9484ba8f4a1c413725f4f518851b880884f79957d1 | Latest strategy text, steel market, POSCO, Middletown, fair value of the MinnTac option and employee benefit commitment, segment note |
| EX-99.1_2026-04-20_clf-202603318xkex991.htm.jsonl | b9c8fc8d9b4361337a220b73ac602738ac2f0a283bbd73c7b1429c171ac6000c | Management commentary, Q1 2026 |
| EX-99.1_2026-07-23_clf-202606308xkex991.htm.jsonl | 6e73622f8701012d98293b6d350054a601691c0c525be23eff4b4255d0c4ab32 | Management commentary, Q2 2026 |
| EX-99.1_2026-10-19_clf-202609308xkex991.htm.jsonl | e6cabc90a6962f04fc1da1253ad4fc1e70365df28408b401d69ed58092c0c0e1 | Management commentary, Q3 2026, outlook, Hamilton Works and Stelco wording |
| context | 9824d18b9e3851ae3ee2ee1eb294b36a7465c031f02ec1e26c0d1341d4ae46e3 | Run settings only; not issuer evidence. Sponsor, parent, guarantors, ratings and market data are blank, which is not evidence of their absence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | a3ac66d14ed58e324a2e51f64f8df6ffab5558cd2acad9a6736446039b68520e | Source readiness; logged differences 1 to 7 carried |
| CP-1 | febe06aea238831d2c068e9106ca38dc5907ecb1605c542b2cdb6b84313cc844 | Financial base; figures below that repeat it (debt principal 7,712; liquidity 3,246; LTM Adjusted EBITDA 972) are copied from it, not recomputed |

Corrections to earlier handoffs (they cannot be edited, so they are stated here):

- CP-0 and CP-1 said the property sale named in the Q3 release is not described in any filed source. That remains true of the specific sale, but the 10-K and the Q1 10-Q do describe general asset-sale processes: "we engaged J.P. Morgan as our advisor and launched sell-side processes to explore the potential sale of certain non-core operating assets" and "inbound inquiries" for idled facilities and inactive sites (10-K page:9; 10-Q Q1 page:34). The Q2 and Q3 10-Qs do not repeat that wording (see Conflicts). No buyer, price or timing is given in any source.
- CP-1's table of claims outside debt omitted two items found in the 10-Q Q3: an employee benefit commitment of 158 at September 30, 2026 (169 at January 1, 2026) with payments to 2042 (page:20), and the MinnTac purchase option at a price of 500 (page:20). Both are carried below. Neither changes a CP-1 ratio.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| A public, vertically integrated North American steelmaker whose credit story rests on steel pricing, trade protection and automotive contracts, plus three open items: a non-binding POSCO agreement, asset sales without detail and a $500 million MinnTac purchase option. | Medium | No ownership, customer concentration, sponsor or ratings data are supplied, and none of the pending transactions has definitive terms in the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Direct automotive was 30% of 2025 revenue, and about 35-40% of flat-rolled shipments are sold under fixed price contracts; the rest is spot or index-linked. | Earnings follow steel prices closely, so margin and cash flow are cyclical and debt capacity depends on the price cycle. | High |
| Iron ore, coke, scrap and direct reduced iron are largely sourced internally, and the slab contract that was about 10 percent of volume expired on December 9, 2025. | Input costs are more predictable and an unprofitable contract has ended, which supports margins, though idled sites carry idle costs. | Medium |
| The POSCO agreement is a non-binding Memorandum of Understanding subject to definitive terms, and asset sale processes were launched in Q3 2025 with no buyer or price disclosed. | Management links both to debt reduction, but neither can be counted as a source of repayment on the supplied sources. | High |
| Stelco, acquired on November 1, 2024 for $3,208 million, carries a $500 million MinnTac purchase option open until January 31, 2027 and a $158 million employee benefit commitment. | The option could draw on liquidity if exercised, and weak Canadian conditions have already led to idling at Hamilton Works. | Medium |
| Labor agreements at several steelmaking and mining sites expire in 2026 and USW negotiations are ongoing; a 2025 offering of 75 million shares repaid ABL borrowings. | Labor terms affect costs and continuity. Equity-funded ABL repayment in 2025 was a supportive action toward creditors. | Medium |

### Business and transaction view

Cleveland-Cliffs is a publicly listed, vertically integrated flat-rolled steel producer with no sponsor and no controlling owner identified in the supplied sources. Its credit-relevant business facts are a sizeable automotive franchise (30% of 2025 revenue), a mixed pricing model in which about 35-40% of flat-rolled shipments are on fixed price contracts and the rest follow spot or index prices, internal supply of most iron ore, coke, scrap and direct reduced iron, a unionized workforce with agreements expiring in 2026, and a footprint that management has already trimmed through idlings. The transaction picture is one of completed past actions and unfinished future ones. Completed: the Stelco acquisition on November 1, 2024, the 2025 note issues and the October 2025 redemption of all 2027 notes, and the October 31, 2025 share offering that repaid ABL borrowings. Unfinished: the POSCO Memorandum of Understanding, which is stated to be subject to negotiation of definitive terms; the asset sale processes and the property sale management cites for expected fourth-quarter debt reduction, none of which has a disclosed buyer, price or timing; the Middletown Works investment framework with the Department of Energy; and the MinnTac purchase option. Documented issuer behaviour is mixed to supportive for creditors: share repurchases stopped after 2024, equity was raised in 2025 to repay the ABL, and no priming, drop-down or non-pro-rata exchange appears in the supplied sources. Legal capacity is a separate question: management states approximately $3 billion of secured note capacity, which could place new secured debt ahead of the unsecured notes if used, and the indentures that govern it are not supplied. Management's own forward statements (fourth quarter outlook, 2027 outlook, leverage target) are attributed and not adopted.

### Company and operating model

| Area | Fact | Category | Locator | Limitation or credit relevance |
| --- | --- | --- | --- | --- |
| Business description | "We are a leading North America-based steel producer with focus on value-added sheet products, particularly for the automotive industry." Vertically integrated from iron ore mining, pellets and direct reduced iron and ferrous scrap through steelmaking and downstream finishing, stamping, tooling and tubing | Documentary Fact | 10-K page:6; 10-Q Q3 page:7 | The wording "leading" is the issuer's own characterisation |
| Country and sector | United States (Ohio incorporation, Cleveland headquarters); operations in the United States and Canada; sector metal mining and steel per context | Documentary Fact | 10-Q Q3 page:1, page:7; context | Context sector label is a run setting, not issuer evidence |
| Segments | Four operating segments (Steelmaking, Tubular, Tooling and Stamping, European Operations); one reportable segment, Steelmaking; Other Businesses combined | Documentary Fact | 10-Q Q3 page:11 | Segment detail beyond Steelmaking and Other Businesses is limited |
| Products | Hot-rolled, cold-rolled, coated, plate, stainless and electrical steel; slab; stamped components; tubing; by-products iron ore, HBI, scrap, coal and coke | Documentary Fact | 10-K page:11, page:12 | Q3 2026 shipments by product: hot-rolled 46%, coated 31%, cold-rolled 15% (volume basis, Release Q3 page:2); revenue by product is in 10-Q Q3 page:10 |
| End markets, 2025 (share of revenue) | Direct automotive 30%; infrastructure and manufacturing 29%; distributors and converters 28%; steel producers 13% (2024: 32%, 27%, 28%, 13%) | Documentary Fact | 10-K page:12 | Customer names and customer concentration percentages are Not disclosed in the pack |
| End markets, Q3 2026 (Steelmaking revenue) | Direct automotive 1,541; infrastructure and manufacturing 1,545; distributors and converters 1,829; steel producers 532; total 5,447 | Documentary Fact | 10-Q Q3 page:10 | Net of intersegment revenue |
| Geography, FY2025 revenue | United States 15,887; Canada 2,071; other countries 652; total 18,610 | Documentary Fact | 10-K page:130 | Canada includes Stelco |
| Customers and concentration | Risk factor: "we face risks arising from our relative concentration of sales to certain specific automotive manufacturers" | Documentary Fact | 10-K page:33 | Number of customers and top customer share: Not disclosed. Why it matters: loss of a fixed price automotive contract is a revenue and margin risk |
| Revenue model and pricing | "We sell approximately 35-40% of our flat-rolled steel shipments under fixed price contracts"; contracts are annual or multi-year, some with input cost surcharge mechanisms; the remainder is spot or index-linked | Documentary Fact | 10-K page:13 | Contract reset timing is not itemized. Management expects "the higher reset of fixed price contracts" (Management Language, Release Q2 page:2) |
| Price level | Domestic HRC averaged $851 per net ton in 2025 against $772 in 2024; $1,195 in Q3 2026, which management describes as "the highest quarterly average per net ton since the second quarter of 2022" | Documentary Fact; the superlative is Management Language | 10-K page:15; 10-Q Q3 page:28 | HRC is the index that drives Steelmaking revenue; price is the largest swing factor |
| Volume drivers | Steel shipments of 4,150 thousand net tons in Q3 2026 against 4,029 in Q3 2025, and 12,283 in nine months 2026 against 12,459 | Documentary Fact | 10-Q Q3 page:39 | Management guides about 16.5-17.0 million net tons for FY2026 (Release Q2 page:3), a Management Language item |
| Price and volume effect | Q3 2026 revenue up about 890 for Steelmaking, of which about 500 from pricing, about 130 from volume and about 100 from mix | Documentary Fact | 10-Q Q3 page:40 | Pricing drove most of the increase, which is the mechanism behind earnings recovery |
| Cost structure | Cost of goods sold 5,147 on revenue 5,612 in Q3 2026; internal sourcing of most iron ore pellets, partial self-supply of coke and coal; higher energy costs, repair and maintenance expense and product mix are the cost drivers named in MD&A | Documentary Fact | 10-Q Q3 page:4, page:40, page:41 | Fixed and variable split is Not disclosed |
| Raw materials | Ownership share of iron ore capacity of about 20.1 million long tons at December 31, 2025; five active cokemaking facilities, coke capacity 4.0 million net tons; metallurgical coal capacity 1.8 million net tons; scrap via FPT with 21 facilities | Documentary Fact | 10-K page:26 | Minorca idled and part of Hibbing idled. The internal sourcing claim "more predictable costs" is Management Language (10-K page:6) |
| Capacity and footprint | Seven blast furnaces and four electric arc furnaces, "configured capability" of about 20.0 million net tons of raw steel; during 2025 six operations were idled or closed | Documentary Fact | 10-K page:11, page:8, page:9 | Configured capability includes idled units, so it is not current output |
| Capital spending | FY2025 purchase of property, plant and equipment 561; full-year 2026 guidance "approximately $700 million" (releases) against "approximately $1.0 billion" over the next 12 months (10-Q Q3) | Documentary Fact; the guidance is Management Language | 10-K page:110; Release Q2 page:3; 10-Q Q3 page:44 | The two statements differ by horizon and are not reconciled (logged in CP-1) |
| Working capital | Accounts receivable rose from 1,442 at December 31, 2025 to 2,159 at September 30, 2026, a cash use of 723 in nine months 2026, attributed to "rising steel prices and the timing of sales" | Documentary Fact | 10-Q Q3 page:3, page:5, page:44 | Earnings recovery is partly absorbed by working capital in a rising-price phase |
| Labor | More than 90% of an approximately 20,000-person hourly workforce is represented by the USW, UAW and IAM; over 18,000 employees are under collective bargaining agreements; agreements expiring in 2026 include Burns Harbor, Cleveland, Coatesville, Columbus Coatings, Coshocton, Indiana Harbor, Mansfield, Toledo HBI, Warren and all iron ore mines; "We are currently engaged in good faith negotiations with the USW" | Documentary Fact | 10-Q Q3 page:7, page:34; 10-K page:58 | Outcome of negotiations Not disclosed. A stoppage or cost step-up would hit margin and continuity |
| Legacy slab contract | The five-year slab supply contract, initiated with the AM USA Transaction, "historically represented approximately 10 percent of our sales volume and was unprofitable in 2024 and 2025"; it expired on December 9, 2025 | Documentary Fact | 10-K page:8, page:16 | Supports mix improvement; effect on Q3 2026 revenue mix is described by management |
| Idled facilities | Indefinitely idled Steelton rail and Weirton tinplate lines carry accrued liabilities of 40 at September 30, 2026; Hamilton Works finishing indefinitely idled in Q3 2026 | Documentary Fact | 10-Q Q3 page:9, page:37 | Idle charges are excluded from Adjusted EBITDA, so they are cash costs not visible in that measure |

### Company profile

| Attribute | Value | Category | Locator |
| --- | --- | --- | --- |
| Legal name and ticker | CLEVELAND-CLIFFS INC.; common shares, par value $0.125, NYSE: CLF; Commission File Number 1-8944 | Documentary Fact | 10-Q Q3 page:1 |
| Incorporation and headquarters | Ohio; 200 Public Square, Cleveland, Ohio | Documentary Fact | 10-Q Q3 page:1 |
| Filer status | Large accelerated filer; not a shell company | Documentary Fact | 10-Q Q3 page:1 |
| Employees | Approximately 25,000 across the United States and Canada | Documentary Fact | 10-Q Q3 page:7 |
| Share count | 606,051,530 issued; 570,555,800 outstanding at September 30, 2026; 570,584,966 outstanding at October 20, 2026; 35,495,730 in treasury | Documentary Fact | 10-Q Q3 page:1, page:3 |
| Ownership and control | Public company; no sponsor, parent or controlling holder is identified in the supplied pages; holder list and voting control are Not supplied (Part III is incorporated from the proxy statement, which is not in the pack) | Insufficient Information | 10-K page:169; context |
| Independent auditor | Deloitte & Touche LLP, auditor since 2004; unqualified opinion dated February 9, 2026 | Documentary Fact | 10-K page:165, page:168 |
| Fiscal year | Calendar year, ended December 31 | Documentary Fact | 10-K page:1 |
| Primary sites | Steel and finishing facilities in Indiana, Michigan, Ohio, Pennsylvania and Ontario; iron ore mines in Michigan and Minnesota; direct reduction plant in Ohio; coal mine in West Virginia | Documentary Fact | 10-K page:11 |
| Credit ratings | Not supplied: context `ratings` is empty and no rating agency report is in the pack. The 10-K only warns that ratings downgrades could affect purchasing terms | Insufficient Information | context; 10-K page:43 |
| Market data | Not supplied: context market capitalization, quotes and peers are blank. A share offering price of $12.69 (October 31, 2025) and a grant-date price of $10.55 (Q1 2026) are filed facts, not market data as of the as-of date | Insufficient Information | context; 10-K page:157; 10-Q Q3 page:17 |
| Capital structure reference | Total debt principal 7,712 and cash 77 at September 30, 2026; liquidity 3,246; LTM Adjusted EBITDA 972 (from CP-1) | Documentary Fact | CP-1 handoff; 10-Q Q3 page:15 |

### Transaction summary and new debt issues

Stelco acquisition, completed. On November 1, 2024 the issuer completed the Stelco Acquisition under an Arrangement Agreement, as acquirer, paying total purchase consideration of $3,208 million, made up of cash of 2,450, share exchange consideration of 343 (25.9 million treasury shares) and debt consideration of 415 (US$ millions) (10-K page:124, page:157). The stated purpose was to expand the Canadian presence and diversify the customer base toward spot sales, and management says its exposure to the North American spot market "doubled" (10-K page:9, page:10). From a creditor view the mechanism is that the deal added debt and spot-price exposure at a time when Canadian conditions were weak: the Q3 10-Q says Canada imposed tariff-rate quotas on steel imports in the second half of 2025 and that weak demand for value-added sheet products in Canada led to the indefinite idling of finishing operations at Hamilton Works (10-Q Q3 page:29, page:37). Stelco holds an option to buy a 25% interest in the MinnTac iron ore mine from U. S. Steel for $500 million, exercisable until January 31, 2027, carried as a derivative with a fair value of 54 at January 1, 2026 and 16 at September 30, 2026 (10-Q Q3 page:20). If exercised, the cash call of $500 million would be a liquidity use; whether management intends to exercise is not stated in the sources, and January 31, 2027 is a future date, not an event of the reporting periods. Stelco also carries an employee benefit commitment recorded at $158 million at September 30, 2026 (169 at January 1, 2026) with fixed payments to 2042 plus a variable component (10-Q Q3 page:20).

New debt issues and repayments, completed. In 2025 the issuer issued 850 of 7.500% Senior Notes due 2031 at par under an indenture dated February 6, 2025, and 850 of 7.625% Senior Notes due 2034 at par under an indenture dated September 8, 2025, followed by a further 275 of the 7.625% notes on October 10, 2025 at 102.750% of principal (10-K page:133, page:134). On October 3, 2025 the net proceeds of the 7.625% notes were used to redeem all 685 of the 2027 notes outstanding (73 of 7.000% 2027 notes, 56 of 7.000% 2027 AK Steel notes and 556 of 5.875% 2027 notes), which removed the 2027 maturity wall (10-K page:140). All new notes are unsecured senior obligations guaranteed by the material domestic subsidiaries, are structurally subordinated to non-guarantor debt, and carry "no financial covenants" (10-K page:133, page:134). The issuer sold 75 million common shares in an underwritten offering at $12.69 per share on October 31, 2025 and used the net proceeds to repay ABL borrowings (10-K page:157). No senior notes were issued in the nine months ended September 30, 2026 and ABL borrowings rose by 383 over that period to fund general corporate requirements (10-Q Q3 page:45). The liquidity effect is that these actions extended the nearest note maturity to 2029 and used equity to reduce secured ABL borrowings in 2025, then 2026 working capital absorbed part of the benefit. Debt and liquidity figures are in CP-1 and are not repeated here.

Proposed or unfinished transactions. The POSCO Memorandum of Understanding was signed in the third quarter of 2025; POSCO seeks to use the issuer's U.S. footprint, UBS is financial advisor, and the arrangement "remains subject to negotiation of definitive terms" with no assurance that definitive agreements will be signed (10-Q Q3 page:37, page:38). Management expects "substantial proceeds that could be used to reduce our outstanding indebtedness" (Management Language), but the amount, structure and timing are Not disclosed, and the Q1 release says the Middle East situation "has not helped the timeline of a potential deal with POSCO" (Release Q1 page:2). Treat it as a non-binding, unquantified possibility, not a source of repayment. Asset sales: in the third quarter of 2025 the issuer engaged J.P. Morgan and launched sell-side processes for certain non-core operating assets, and received inbound inquiries about idled facilities and inactive sites, intending to use net proceeds to pay down debt (10-K page:9; 10-Q Q1 page:34). Gains on disposal of assets of 23 appear in nine months 2026 (10-Q Q3 page:47), and MD&A attributes part of the Miscellaneous, net change to a gain on sale of non-core assets (10-Q Q3 page:43). The Q3 release says "with amplified free cash flow in Q4 and property sale proceeds, we expect a major debt reduction in the fourth quarter" (Release Q3 page:1); no filing identifies the property, buyer, price or closing date. Middletown Works: in the third quarter of 2026 the Department of Energy established a framework to finalize negotiations on a rescoped investment, replacing the previously awarded 500 grant, as a 1,000 total project funded equally by the issuer and the DOE and expected to complete in 2030; the framework is not a signed award (10-Q Q3 page:38, page:39). Subsequent events: the 10-Q Q3 reports none in Note 19, and nothing between October 20, 2026 and 2026-11-05 is supplied. Those are Not supplied, not absent.

Sponsor and ownership transactions. There is no sponsor and no dividend recapitalisation, debt-funded distribution, related-party leakage, priming, uptiering, drop-down, non-pro-rata exchange or collateral release in the supplied sources. Share repurchases of 733 in 2024 (37.9 million shares) were followed by none in 2025 and none under the program in the first nine months of 2026, with 1.4 billion of authorization remaining at December 31, 2025 (10-K page:157; 10-Q Q3 page:61). The ABL covenants cover the payment of dividends and the repurchase of capital stock, but no dividend payment line appears in the cash flow statements, and a dividend policy statement is Not supplied (10-K page:139, page:110, page:111).

### Ownership, governance and creditor-behaviour register

| Behaviour or fact | Evidence | Category | Mechanic and implication | Dimension informed | Evidence quality |
| --- | --- | --- | --- | --- | --- |
| Public company, no identified sponsor | Context `sponsor` blank; no holder table in the pack | Insufficient Information | Control rights and shareholder support cannot be assessed beyond the equity raise; do not infer from the absence of a sponsor | Ownership | Insufficient |
| Equity issued to repay ABL | 75 million shares sold at $12.69 on October 31, 2025; net proceeds repaid ABL borrowings (10-K page:157) | Documentary Fact | Equity reduced secured borrowings and lifted liquidity, a supportive deleveraging action; outstanding shares rose from 493.9 million at December 31, 2024 to 569.8 million at December 31, 2025, mainly the 75.0 million shares issued (10-K page:111) | Capital allocation | High |
| Buybacks stopped after 2024 | 37.9 million shares for 733 in 2024; none in 2025 or the first nine months of 2026 (10-K page:157; 10-Q Q3 page:61) | Documentary Fact | Cash is retained for liquidity; the earlier buyback alongside debt-funded M&A is Neutral or Mixed behaviour | Capital allocation | High |
| Debt reduction intention | "we intend to utilize it to deleverage our balance sheet" (10-K page:10); leverage target stated differently in two releases (Release Q2 page:2; Release Q3 page:1) | Management Language | Stated willingness only; LTM net debt to Adjusted EBITDA of 7.85x (CP-1) is far above the stated target. Different numerator and timing wording between releases | Capital allocation | Medium |
| Secured note capacity | "approximately $3 billion of secured note capacity", subject to the indentures and ABL (10-Q Q3 page:46) | Management Language | Legal capacity to add secured debt exists; willingness to use it is not documented. If used, it would rank ahead of the unsecured notes | Legal capacity | Medium |
| ABL ranks ahead of notes on collateral | ABL has first priority on receivables, inventory and certain mobile equipment and second priority on substantially all other assets (10-K page:139) | Documentary Fact; the ranking reading is Analyst Interpretation | Unsecured noteholders rank behind ABL claims on both collateral pools; the guarantee structure is by domestic subsidiaries only | Structure | High |
| Reporting transparency | Releases carry non-GAAP reconciliations; 10-Q reports ABL capacity each quarter | Documentary Fact | Supportive of monitoring; covenant certificate and agreement terms are not available | Disclosure | High |
| Related-party or extraction behaviour | None found in the supplied sources; SunCoke Middletown is a consolidated variable interest entity from which the issuer purchases all coke and power | Insufficient Information | No evidence either way beyond the VIE note; not an adverse conclusion | Related parties | Low |

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| 2020 | Became a steel company; "our 2020 acquisitions" include the AM USA Transaction. AK Steel Corporation is now Cleveland-Cliffs Steel Corporation | Documentary Fact | 10-K page:6, page:8, page:132 |
| Nov 1, 2024 | Stelco Acquisition completed, total purchase consideration 3,208 | Documentary Fact | 10-K page:124 |
| Feb 6, 2025 | Indenture for 850 of 7.500% 2031 notes | Documentary Fact | 10-K page:134 |
| Q2 2025 | Steelton, Conshohocken and Riverdale decided to be idled or closed (wording differs, see Conflicts) | Documentary Fact | 10-K page:8; 10-Q Q3 page:14 |
| Q3 2025 | POSCO Memorandum of Understanding; J.P. Morgan engaged for sell-side processes | Documentary Fact | 10-K page:9 |
| Sep 8, 2025 | Indenture for 850 of 7.625% 2034 notes; 275 add-on on Oct 10, 2025 at 102.750% | Documentary Fact | 10-K page:133 |
| Oct 3, 2025 | All 685 of 2027 notes redeemed | Documentary Fact | 10-K page:140 |
| Oct 31, 2025 | 75 million shares sold at $12.69; proceeds repaid ABL | Documentary Fact | 10-K page:157 |
| Dec 9, 2025 | Slab supply contract expired | Documentary Fact | 10-K page:8 |
| Feb 9, 2026 | Audit opinion on the FY2025 statements dated | Documentary Fact | 10-K page:168 |
| Q1 2026 | Gain on sale of certain non-core assets; extreme cold weather energy cost impact described by management as 80 | Documentary Fact; the 80 is Management Language | 10-Q Q1 page:37; Release Q1 page:1 |
| Q2 2026 | Gary plate finishing line and one of two Burns Harbor plate mills idled | Documentary Fact | 10-Q Q3 page:37 |
| Q3 2026 | Hamilton Works finishing indefinitely idled; DOE framework for Middletown Works; leverage target restated | Documentary Fact | 10-Q Q3 page:37, page:38; Release Q3 page:1 |
| Oct 19-20, 2026 | Q3 release and 10-Q issued; no subsequent events reported | Documentary Fact | Release Q3 page:1; 10-Q Q3 page:27, page:63 |
| Oct 20, 2026 to 2026-11-05 | Not supplied | Insufficient Information | pack |
| Future dates as terms, not events | MinnTac option expires Jan 31, 2027; Mesabi Metallics trial set for May 2027; steel labor agreements expire during 2026 | Documentary Fact | 10-Q Q3 page:20; 10-K page:78, page:58 |

### Credit translations

- Revenue durability. Evidence: direct automotive was 30% of 2025 revenue and about 35-40% of flat-rolled shipments are on fixed price contracts, the rest spot or index-linked (10-K page:12, page:13). Mechanic: the fixed-price book gives some visibility and resets as contracts renew, while the spot and index book moves with HRC, which averaged $851 per net ton in 2025 and $1,195 in Q3 2026 (10-K page:15; 10-Q Q3 page:28). Implication: earnings and refinancing capacity are tied to the steel price cycle and to the renewal of a few automotive contracts; customer concentration data is Not disclosed, so the size of that exposure cannot be stated. Counter-evidence: no logged conflict changes the revenue picture, but the two leverage-target wordings (CP-0 conflict 2) limit how far management's deleveraging statements can be relied on.
- Margin and cash-flow risk. Evidence: Q3 2026 price effect of about 500 on Steelmaking revenue and an accounts receivable build of 723 in nine months 2026 (10-Q Q3 page:40, page:5). Mechanic: higher prices lift revenue before cash is collected, so the first half of a price recovery absorbs working capital. Implication: debt reduction lags earnings, and the management-expected fourth-quarter reduction depends on free cash flow and property sale proceeds that the filings do not quantify.
- Concentration and operating risk. Evidence: labor agreements at most major steel sites and all iron ore mines expire in 2026 and negotiations with the USW are ongoing (10-K page:58; 10-Q Q3 page:34); six operations were idled or closed in 2025 and further idlings occurred in 2026 (10-K page:8; 10-Q Q3 page:37). Mechanic: a work stoppage or a cost step-up hits an integrated system where internal supply is a stated advantage, and idle sites carry costs excluded from Adjusted EBITDA. Implication: monitor labor outcomes and idle-cost cash payments (accrued idle liabilities 40 at September 30, 2026).
- Sponsor alignment. Evidence: no sponsor; equity raise and buyback halt documented. Mechanic: management and public shareholders, not a financial sponsor, control creditor-relevant choices. Implication: behaviour so far leans supportive of creditors, but legal capacity for secured debt is wide and the governing documents are not supplied.
- Key uncertainties. The POSCO agreement terms, the identity and size of the property sale, whether the MinnTac option will be exercised, ownership and customer concentration, ratings, and any event after October 20, 2026. Conflicts that counter a clean reading: sell-side language dropped between the Q1 and Q2 10-Qs; "permanently close" versus "indefinitely idle" for Steelton, Conshohocken and Riverdale.

### Conflicts and differences logged (not reconciled)

| # | Items | Locators | Downstream effect |
| --- | --- | --- | --- |
| 1 | The 10-K says "We also made the decision to permanently close our Steelton, Conshohocken and Riverdale facilities" and later describes "the permanent closure of our Conshohocken, Pennsylvania, Riverdale, Illinois and Steelton, Pennsylvania steelmaking facilities"; the 10-Q Q3 says "we decided to indefinitely idle our Steelton, Conshohocken, and Riverdale facilities"; the 10-K also refers to "the indefinite idling of the Steelton rail production facility" | 10-K page:8, page:9, page:53, page:87; 10-Q Q3 page:14 | Closure versus idling changes asset recoverability and whether restart is possible. Not resolved; carry both |
| 2 | Asset-sale wording: the 10-K and Q1 10-Q say J.P. Morgan was engaged and sell-side processes launched; the Q2 and Q3 10-Qs list only a general potential to generate liquidity from the sale of non-core assets, idled facilities and inactive sites; the Q3 release cites "property sale proceeds" | 10-K page:9; 10-Q Q1 page:34; 10-Q Q2 page:44; 10-Q Q3 page:46; Release Q3 page:1 | Whether the sell-side processes continue is not stated. The expected fourth-quarter reduction rests on an unidentified property sale |
| 3 | Hamilton Works finishing operations (10-Q) versus galvanizing lines at Stelco (Release Q3) | 10-Q Q3 page:37; Release Q3 page:2 | Carried from CP-0; scope of the idling is not equated |
| 4 | Leverage target wording differs between releases | Release Q2 page:2; Release Q3 page:1 | Carried from CP-0; management language only |
| 5 | Capital expenditure outlook horizons differ | Release Q2 page:3; 10-Q Q3 page:44 | Carried from CP-1; not reconciled |
| 6 | 10-K page:138 labels the 7.375% 2033 notes as "7.375% 2029 Senior Notes" in the redemption text | 10-K page:138 | Carried from CP-1; indenture not supplied |

No conflict was found between the filings on the acquisition consideration (3,208), the note issuances or the share offering.

### Consumer readiness

| Consumer | Readiness | Take from CP-1A | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | The business risk drivers (automotive exposure, pricing mix, vertical integration, labor, idled sites), the Stelco option and benefit commitment, and the list of unfinished transactions | Fundamental synthesis needs business risk next to CP-1 financial risk | Ownership, customers, ratings and later events are Not supplied; carry the POSCO, property sale and MinnTac items as unquantified |
| CP-5 | READY_WITH_LIMITATIONS | Every row has a located citation and a category; management language is labelled | Integrity review needs claims traceable to pages | Check the permanent-closure versus idling wording and the sell-side wording conflicts rather than resolving them |

Monitoring gaps by severity: executed indentures and ABL credit agreement (High, not supplied); covenant certificate (Medium, not supplied; the 10-Q states only that the test was not applicable); add-back bridge (Low, the issuer's own reconciliation is in the 10-Q and releases, but no management bridge is supplied); debt and maturity schedules (available in the 10-Q Q3 Note 7).

## Calculations

No new calculation is produced. Figures repeated from CP-1 are copied: total debt principal 7,712, cash 77, liquidity 3,246, LTM Adjusted EBITDA 972 and total debt to Adjusted EBITDA of 7.93x. The only arithmetic shown is a tie-out of filed figures:

| Check | Computation | Result vs printed |
| --- | --- | --- |
| Stelco total consideration | 2,450 + 343 + 415 | 3,208, equals the printed total purchase consideration (10-K page:124) |
| 2025 note redemption | 73 + 56 + 556 | 685, equals the "$685 million" redemption (10-Q Q3 page:46; 10-K page:140) |
| FY2025 revenue by geography | 15,887 + 2,071 + 652 | 18,610, equals total revenues (10-K page:130) |
| Q3 2026 Steelmaking revenue by market | 1,541 + 1,545 + 1,829 + 532 | 5,447, equals printed total (10-Q Q3 page:10) |
| Net ABL borrowing, nine months 2026 | 834 - 452 | 382 against 383 printed in the cash flow statement (rounding) |
| Share offering gross proceeds | 75 million x $12.69 | about 952, against 951 shown as issuance of common shares in the equity statement (10-K page:111); the filing does not state net proceeds separately |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Ownership: holder list, control rights and economic interest not supplied (proxy statement not in the pack) | Medium | CP-2 | Supply the 2026 proxy statement |
| Customer names and concentration percentages not disclosed | Medium | CP-2 | Supply customer concentration disclosure if available outside the pack |
| POSCO Memorandum of Understanding and any definitive agreements not supplied | Medium | CP-2 | Supply the MoU and any later 8-K |
| Identity, price and timing of the property sale and any non-core asset sales not disclosed | Medium | CP-2 | Supply later 8-Ks or press releases |
| Whether Stelco will exercise the MinnTac option (500, until January 31, 2027) is not stated | Medium | CP-2 | Check later disclosure; treat as a potential liquidity use |
| Executed indentures, ABL credit agreement and covenant certificate not supplied | High for legal work | CP-2 | Supply executed documents |
| Events between October 20, 2026 and 2026-11-05 not supplied | Medium | CP-2, CP-5 | Supply later 8-Ks or confirm none |
| Ratings and market data not supplied | Low for this scope | CP-2 | Not required for this scope |
| Strategy wording changed between the Q1 and Q2 10-Qs (sell-side processes) and the closure wording differs between 10-K and 10-Q | Low | CP-5 | Keep as logged conflicts |
| Segment, product-line and customer profitability beyond Steelmaking and Other Businesses not disclosed | Low | CP-2 | None needed for this scope |

## Next module

- CP-2: combine the business risk drivers here with the CP-1 financial base. State that earnings, leverage and refinancing capacity depend on steel pricing and automotive contract resets; carry the POSCO, property sale and MinnTac items as unquantified, and the secured note capacity as a legal capacity item without evidence of use. Keep management outlook statements attributed.
- CP-5: trace each row to its locator and category. Check the permanent-closure versus idling wording, the sell-side wording change and the corrections to CP-0 and CP-1 stated in Sources.
