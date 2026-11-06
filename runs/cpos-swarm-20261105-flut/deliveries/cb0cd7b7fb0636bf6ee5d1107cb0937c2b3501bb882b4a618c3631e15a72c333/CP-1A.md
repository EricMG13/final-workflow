# CP-1A — Business and transaction context: Flutter Entertainment plc (flut)

## Request

- Issuer: Flutter Entertainment plc (issuer id `flut`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026; prior period FY2025 (context).
- Run: `flut-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, module CP-1A (business, ownership, transaction and governance context). Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Question: which transaction, business, ownership and operating facts matter most to a creditor of Flutter Entertainment plc, how do they transmit to credit risk, and what is missing?
- Perimeter: Flutter Entertainment plc and its subsidiaries, consolidated. Debt issuers inside the group (Flutter Treasury DAC and the credit agreement borrowers) are described in CP-2, not here.
- Locators are `page:N` of the pinned `.jsonl` text of each source. Fact categories used: Documentary Fact (a filing states it), Management Language (management's characterisation, quoted and not adopted), Analyst Interpretation (this host's reading of cited evidence) and Insufficient Information (evidence missing). No external material is used.
- Figures in this answer are quoted from the sources or are references to the accepted CP-1 handoff; no new calculation is made. Out of scope by method: peer ranking, instrument recommendation and any recovery conclusion.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_flut-20251231.htm.jsonl | b88acc6499b34409bd63bcc7ad6ada664ea0aaf382ca0ec0d2118e7c35eb580e | Business description, history, products, segments, Fox option, risk factors, debt narrative |
| 10-Q_2026-03-31_flut-20260331.htm.jsonl | 350d396101c8e01e25e223f0670d3e0363c6d230399db566cd885841329d1dbe | Q1 2026 interim report (no events requiring disclosure after the period) |
| 10-Q_2026-06-30_flut-20260630.htm.jsonl | a6a0f970aa3d51a04b3c201b89aaae4625c229c4c7864888e69ca9462e615826 | Q2 2026 interim report; LSE delisting subsequent event |
| 10-Q_2026-09-30_flut-20260930.htm.jsonl | cf209bd21d7ac9131f97943f724a2ebaf7232a79180602605a6b0908ae9a79a1 | Q3 2026 interim report; business environment, Brazil, contingencies, subsequent events |
| EX-99.1_2026-05-06_d46069dex991.htm.jsonl | 5416128bf3b9f4328a754a5eff0673c01006c996c64b406795c193ccb390bdfa | Q1 2026 release; management narrative |
| EX-99.1_2026-08-05_d127369dex991.htm.jsonl | 548ad754549966d85d0bb747ddc76468d7bd9635705b387877e25f59264aa63f | Q2 2026 release; CEO transition announcement |
| EX-99.1_2026-11-04_d141532dex991.htm.jsonl | ec2552a07ebcbae61da4247ec9d467815436158552ee8c98ff284c26331c74c1 | Q3 2026 release; priorities, repurchase pause, refinancing, guidance |
| context | c092a23c8bebb5c5ed118bc16d3658aa4f2c0513c724b7304133213e545208aa | User run settings; not issuer evidence |

| Handoff | Module | sha256 |
| --- | --- | --- |
| Source readiness | CP-0 | 6f50887cad81d339bbf86e29e4ef6f91bcf17a0cb9e2b4e94873f1133c5fcfda |
| Financial base | CP-1 | 66391e220a2b7cec03d544f3a1d1fc0013df4fc46ecfb1bf241b39dae37b49a9 |

Both handoffs were opened and used. CP-0 supplies the source limits (no executed credit documents, no investor presentations, no ownership schedule). CP-1 supplies the accepted financial references used below: LTM Adjusted EBITDA of 2,331, total debt of 12,313, cash of 1,708, total debt to Adjusted EBITDA of 5.28x and net debt to Adjusted EBITDA of 4.55x at Q3 2026, and nine-month Adjusted EBITDA of 1,499 against 2,013. This answer adds no figure of its own to those.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Flutter is an online betting group with no identified sponsor or controlling owner, earning 43% of FY2025 revenue in the US and 57% in International. Debt-funded 2025 acquisitions, UK tax rises and the Brazil ban now pressure leverage. | Medium | No credit documents, ownership schedule or investor presentations are supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Revenue is spread across the US and many International markets, and 88% of FY2025 revenue was online. | Diversification cushions single-market shocks, but regulatory and tax changes move earnings quickly. | High |
| UK remote gaming duty rose from 21% to 40% in April 2026, and Brazil banned online betting on September 25, 2026. | Margins and earnings fall in the affected markets, and Brazil assets were impaired. | High |
| 2025 acquisitions of Snai, NSX and the Boyd stake in FanDuel were financed with new debt. | Leverage rose, and management has paused share repurchases to deleverage. | High |
| Fox holds an option to buy 18.6% of FanDuel units until December 2030. | A sale would bring cash but cut the Group's FanDuel stake and could add consent rights. | Medium |
| The October 2026 credit agreement amendment extends maturities to May 2032 and changes the leverage covenant. | Near-term maturity pressure eases, but covenant terms cannot be checked against the executed document. | Medium |

### Business and transaction view

Flutter is an Ireland-incorporated, New York-headquartered online sports betting and iGaming group whose shares trade on the NYSE, with no sponsor and no controlling shareholder identified in the pack. Its revenue base is large and diversified by geography and product, with about 88% of FY2025 revenue earned online and the rest mainly through retail shops in the UK, Ireland, Italy and Serbia. Sportsbook revenue depends on the margin Flutter earns on fixed-odds bets, so it moves with sports results and with the sporting calendar; iGaming revenue is less dependent on the calendar. Both are exposed to gaming taxes that governments change at short notice, and the last year shows how fast this transmits: the UK raised remote gaming duty sharply in April 2026, Brazil's executive ban closed Flutter's Brazilian operations within days in September 2026, and India's 2025 ban ended Junglee. In India and Brazil Flutter took impairments, and in the UK it announced a restructuring.

The transaction history matters more to a creditor than the operating model. In 2025 the Group bought Snai in Italy, a 56% stake in NSX in Brazil, and the 5% of FanDuel held by Boyd, funding them with bridge loans refinanced by new term loan B and senior secured notes issued in June and August 2025. Total debt rose as a result (CP-1), while Brazil, bought with NSX in May 2025, was shut down within sixteen months and carries a large impairment. Management has since paused share repurchases to prioritise deleveraging and set a target leverage range, but earnings fell in 2026 and leverage is well above that range (CP-1). The contingent claim of Fox on FanDuel, a new CEO from October 1, 2026, a UKI restructuring and a credit agreement amendment on October 30, 2026 are subsequent changes that the debt and covenant modules must treat as post-period events. The amendment is known only from filing summaries.

### Company and operating model

| Area | Fact | Category | Evidence and locator | Credit mechanic and implication |
| --- | --- | --- | --- | --- |
| Business | Online sports betting and iGaming operator with sportsbook, iGaming and other products (exchange, pari-mutuel, daily fantasy sports, prediction markets). | Documentary Fact | `These products are offered by FanDuel (sportsbook, iGaming and other products), Sky Betting & Gaming (sportsbook and iGaming products), Sportsbet (sportsbook products), PokerStars (iGaming products)` (10-K `page:8`) | Many brands in many regulatory regimes spread licence and tax risk, but each market has its own cost of sales and tax rate. |
| Scale claim | The Group describes itself as the largest operator by revenue. | Management Language | `Flutter is the world’s leading online sports betting and iGaming operator based on revenue.` (10-K `page:8`) | Scale supports marketing efficiency and negotiating power; the claim is management's and not independently verified here. |
| Product mix | Sportsbook is the largest product, iGaming second, and most revenue is online. | Documentary Fact | `For fiscal 2025, 53% of our revenue was derived from sportsbook, 44% of our revenue was derived from iGaming, and 3% of our revenue was derived from other products, while 88% of our revenue at the Group level was generated from our online businesses.` (10-K `page:10`) | Sportsbook revenue carries outcome variance; iGaming is steadier but more heavily taxed in some markets. |
| Revenue model | Sportsbook earns a spread on fixed odds; iGaming earns hold; poker and exchange earn rake or commission. | Documentary Fact | `We generate revenue by setting odds in a manner that includes a theoretical spread to be earned on each contest less winnings paid and expenses associated with promotional activity.` (10-K `page:10`) | Revenue is exposed to sports results in any period, so a run of customer-favourable results reduces earnings without changing volumes. |
| Geographic mix | Two reportable segments: US and International. | Documentary Fact | `The U.S. segment is our fastest growing and our largest region, constituting $6,967 million (or 43%) of our revenue for fiscal 2025.` (10-K `page:11`); `Our International segment constituted $9,416 million (or 57%) of our revenue for fiscal 2025.` (10-K `page:11`) | International carries the larger share of earnings; the US is the growth and investment segment, so the two segments pull Adjusted EBITDA in different directions (CP-1: US 241 against 612 for nine months). |
| International regions | UKI, Southern Europe and Africa, Asia Pacific, CEE, Brazil and other regions. | Documentary Fact | `Our UKI region constituted $3,547 million (or 22%) of our Group total revenue for fiscal 2025.` (10-K `page:12`); `Our Brazil region constituted $227 million (or 1%) of our Group total revenue for fiscal 2025.` (10-K `page:12`) | The UK is the largest single international tax exposure; Brazil was small in revenue terms, so the ban's direct revenue loss is limited even though the impairment was large. |
| US market position | Management states leading shares in the states where FanDuel is live. | Management Language | `we had an approximately 41% share of the online sports betting market in the states where FanDuel sportsbook was live` (10-K `page:11`) | A leading share lowers customer acquisition risk in existing states but not the state tax risk. |
| Retail | Retail betting shops complement online. | Documentary Fact | `Our online operations are complemented by 1,127 retail shops, mainly in the United Kingdom, Ireland, Italy and Serbia.` (10-K `page:10`) | A small fixed-cost retail base; closures in the UKI restructuring would reduce fixed costs but not remove the UK tax. |
| Seasonality | US revenue follows major league calendars; one-off events affect volumes. | Documentary Fact | `a majority of our current U.S. sports betting and DFS revenue is and will continue to be generated from bets placed on, or contests relating to, the NFL, the NBA, MLB and the NCAA` (10-K `page:12`) | Quarterly cash flow is uneven, so liquidity should be tested at quarter ends, not only at year end. |
| Gaming tax | UK remote gaming duty rises from 21% to 40% and betting duty from 15% to 25%; some US states raise rates. | Documentary Fact | `an increase in remote gaming duty from 21% to 40% effective April 2026; and, an increase in betting duty (excluding horseracing and land-based) from 15% to 25% effective April 2027` (Q3 10-Q `page:48`) | Higher cost of sales in the UK reduces margin; the Group reports the UK duty as the main driver of the rise in International cost of sales (CP-1). A further rise in April 2027 is not yet in reported results. |
| Brazil | Online betting and iGaming banned by executive order; Flutter stopped operating. | Documentary Fact | `Flutter ceased operating sports betting and iGaming in Brazil on September 26, 2026` (Q3 10-Q `page:49`) | Loss of the Brazilian revenue stream and a non-cash impairment (CP-1: 873); legal exposure remains (class action and NSX investigation, below). |
| Cost structure | Payments to US market access partners vary with revenue. | Documentary Fact | `We make variable payments to the majority of our market access partners, typically based on a percentage of our revenue generated in the market where we use such market access partner’s skins.` (10-K `page:20`) | Part of the US cost base flexes with revenue, which cushions a revenue fall but not a margin squeeze from tax. |
| Capital spending | Capital spending is mainly capitalized software and intangible purchases. | Analyst Interpretation | `Capitalized software (397) (313)` (Q3 10-Q `page:9`, nine months 2026 against 2025) | Product development is a recurring cash call that competes with debt service (CP-1: capital expenditure LTM 817). |
| Working capital and player funds | Player deposits are held as cash and as a liability. | Documentary Fact | `Player deposit liability 1,987 1,859` (Q3 10-Q `page:6`) | These balances are not available for debt service and move operating cash flow; liquidity should exclude them (CP-1 excludes them). |
| Prediction markets | A new product line launched in partnership with CME. | Documentary Fact | `In December 2025, we launched FanDuel Predicts in partnership with CME Group (“CME”) in five states.` (Q3 10-Q `page:46`) | New product spend lowered US Adjusted EBITDA in Q3 2026 (release `page:1`); regulatory outcome is open (Supreme Court petition `page:47`). |
| Customer concentration | The sources give player counts, not customer concentration measures. | Insufficient Information | `Total Group AMPs 1 13,669 14,133` (Q3 10-Q `page:50`) | The consumer base is dispersed, but no concentration measure or retention data is disclosed beyond monthly players; this is not an adverse conclusion. |

### Company profile

| Attribute | Value | Category | Evidence and locator | Note |
| --- | --- | --- | --- | --- |
| Legal name and form | Flutter Entertainment plc, a public limited company incorporated in Ireland | Documentary Fact | `The Company’s legal name is Flutter Entertainment plc.` (10-K `page:7`); `Ireland 98-1782229` (10-K `page:1`) | The context lists the country as Netherlands; the filings state Ireland. Logged as a conflict below. |
| Headquarters | Operational headquarters in New York | Documentary Fact | `The Company’s global operational headquarters is One Madison Avenue, New York, New York 10010, United States.` (10-K `page:7`) | US reporting registrant under US GAAP, in US dollars. |
| Listing | NYSE primary listing since May 31, 2024; LSE listing ended August 3, 2026 | Documentary Fact | `On May 31, 2024, the Company moved its primary listing to the NYSE` (10-K `page:7`); `on August 3, 2026, it delisted from the LSE` (Q2 10-Q `page:37`) | Equity market access is single-venue; the filing expects no material financial impact. |
| Sector | Online sports betting and iGaming | Documentary Fact | `Flutter Entertainment plc (the “Company” or “Flutter”) and its subsidiaries (together referred to as the “Group”) is a global online sports betting and iGaming entity` (Q3 10-Q `page:11`) | The context sector label is a generic classification, not issuer evidence. |
| Operating footprint | Approximately 100 countries | Documentary Fact | `As of September 30, 2026, the Group offers its products in approximately 100 countries.` (Q3 10-Q `page:11`) | Licence and tax regimes differ by country; the Brazil closure shows the exposure. |
| Controlling owner or sponsor | None identified; no sponsor in the context | Insufficient Information | `Item 12. Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters 142` (10-K `page:2`) | Item 12 is incorporated by reference to a proxy statement that is not supplied, so shareholders above any threshold are not known. Do not infer ownership percentages. |
| FanDuel ownership | The Group holds all of FanDuel, subject to the Fox option | Documentary Fact | `The acquisition brings the Group’s holding in FanDuel to 100% (subject to the Fox Option).` (10-K `page:9`) | The 100% holding supports cash upstream from the largest growth business; the option is a contingent sale of 18.6%. |
| Fox option | Fox may buy 18.6% of the FanDuel units until December 2030 | Documentary Fact | `As of December 31, 2025, the Fox Option price for the Fastball Units was $4.8 billion.` (10-K `page:29`); `Fox has until December 2030 to exercise the Fox Option.` (10-K `page:29`) | See the credit translation below. The option agreement itself is not supplied. |
| Other minority interests | Non-controlling interests in Sisal and CME; redeemable interests in MaxBet, Junglee and Betnacional | Documentary Fact | `net income (loss) attributed to the non-controlling interest in Sisal and CME, and the net income (loss) attributed to the redeemable non-controlling interest in MaxBet, Junglee and Betnacional` (Q3 release `page:26`) | Leakage to minorities and put and call rights on NSX (10-K `page:9`: `call and put options which allows us to acquire the remaining interest in year five and year ten`) are claims outside debt. |
| Management | CEO changed from Peter Jackson to Dan Taylor on October 1, 2026 | Documentary Fact | `Peter Jackson to transition from CEO role, with Dan Taylor, President of Flutter and CEO of Flutter International, succeeding him as CEO of Flutter on October 1, 2026` (Q2 release `page:1`) | Announced in August 2026 and effective after quarter end; the new CEO sets priorities of organic investment and deleveraging (Q3 release `page:1`). No view is taken on individuals. |
| Auditor | KPMG, Dublin | Documentary Fact | `We have served as the Company’s auditor since 2018.` (10-K `page:145`) | Unqualified opinion and effective internal control at December 31, 2025, with Snai excluded from the internal control assessment (CP-0). |
| Shares and distributions | 173,871,245 shares outstanding at October 30, 2026; no dividends since May 2020 | Documentary Fact | `the number of shares of the registrant’s ordinary shares outstanding is 173,871,245` (Q3 10-Q `page:1`); `We have not paid dividends on our ordinary shares since May 2020` (10-K `page:85`) | Distributions to equity have been through repurchases, now paused. |
| Reporting basis | US GAAP, US dollars, December year end | Documentary Fact | `prepared in accordance with accounting principles generally accepted in the United States of America` (Q3 10-Q `page:11`) | Matches the context; sterling and euro debt is translated into dollars. |

### Transaction summary and new debt issues

In 2025 Flutter completed three acquisitions. On April 30, 2025 it bought 100% of Pluto (Italia) S.p.A, the holding company of Snai, for approximately `$2.6 billion (€2.3 billion)` (Q3 10-Q `page:25`). On May 14, 2025 it acquired a 56% interest in NSX for `$674 million (BRL 3,799 million)` with call and put options over the remainder (10-K `page:9`). It also acquired the 5% redeemable non-controlling interest in FanDuel held by Boyd for `$1,553 million`, taking its holding to 100% subject to the Fox option (10-K `page:9`). The accounting for Snai and NSX was finalised in the second quarter of 2026 (Q3 10-Q `page:25`, `page:26`). All three are documentary facts with status completed. The sources give acquisition terms only in these summaries, and no acquisition agreements are supplied.

The acquisitions were financed in stages. A `€2.5 billion` bridge term loan drawn on April 29, 2025 funded Snai, and a `$1.75 billion` bridge drawn on July 30, 2025 funded the Boyd transaction (10-K `page:125`, `page:126`). They were repaid with new `$1,250 million` of Term Loan B due June 4, 2032 (`$750 million` on June 4 and `$500 million` on August 7, 2025) and with the 2031 senior secured notes issued in the same two tranches: `$1,625 million of 5.875%`, `€850 million of 4.000%` and `£700 million of 6.125%` (10-K `page:126`, `page:127`, `page:128`). The 2029 notes of `$525 million` at 6.375% and `€500 million` at 5.000% had been issued by Flutter Treasury DAC on April 29, 2024 (10-K `page:127`). The use of proceeds was repayment of the bridges, general corporate purposes and costs (10-K `page:126`). Liquidity effect: the debt table shows total debt rising over 2025 (CP-1), and the Group states it believes it has sufficient capacity through cash, internal funds and the revolver (Q3 10-Q `page:74`, a management statement).

After the quarter, on October 30, 2026, the Group signed the First Amendment and Restatement Agreement to the November 2023 credit agreement (Q3 10-Q `page:42`). It extends the term A and revolver maturities to `May 3, 2032`, raises the revolver commitment to `$1.86 billion` with a US dollar base currency, redenominates term A into `€382 million of term A2 loans and $1,374 million of term A3 loans`, replaces the net total leverage covenant with a net first lien leverage covenant at `5.70:1.00`, and prices term A and revolver loans at a margin of `1.40% to 2.00%` set by corporate ratings (Q3 10-Q `page:42`). The revolver increase took effect on November 3, 2026 (Q3 10-Q `page:74`). Status: completed, a subsequent event after September 30, 2026, described only in a note and in the Q3 release (`page:12`); the executed document is not supplied. The liquidity effect is an enlarged revolver, but the undrawn amount after the amendment is not disclosed. The Q3 release describes the facility increase as approximately `$240m` for the refinanced facilities without defining the set, which is not reconciled to the revolver figure (see conflicts).

Other transactions and structural changes: the Group delisted from the LSE on August 3, 2026 (Q2 10-Q `page:37`); it paused the share repurchase programme during Q3 2026 (`paused the 2024 Share Repurchase Program to prioritize deleveraging`, Q3 10-Q `page:75`), having repurchased shares under the `$5 billion` authorisation (Q3 10-Q `page:75`); on October 20, 2026 it committed to a UKI restructuring plan affecting up to `1,400 employees` with charges of `$80 million to $90 million` (Q3 10-Q `page:42`); and Brazil operations were closed in September and October 2026 (Q3 10-Q `page:14`). There is no sponsor, no dividend recapitalisation and no disposal described in the sources. No new debt issue is described after the October 30, 2026 amendment, and nothing is dated after the cutoff of November 5, 2026.

### Governance, capital allocation and creditor behaviour

| Documented action | Category | Behaviour reading | Mechanic | Evidence and locator |
| --- | --- | --- | --- | --- |
| Debt-funded acquisitions in 2025 (Snai, NSX, Boyd stake) | Documentary Fact | Neutral or Mixed | Acquisitions lifted debt and then leverage; the Group states that Snai and NSX were finalised in Q2 2026. Whether synergies appear is not evidenced. | `The acquisition of Snai was funded by the net proceeds from the issuance of the Senior Notes due 2031, and the Term Loan B due 2032 borrowings` (Q3 10-Q `page:25`) |
| Share repurchases while leverage was rising, then paused | Documentary Fact | Neutral or Mixed, moving to Supportive | Repurchases used cash that could have repaid debt; the pause redirects cash to deleveraging. Stated intent only; cash effect arrives in later periods. | `paused the 2024 Share Repurchase Program to prioritize deleveraging` (Q3 10-Q `page:75`); `Prioritizing organic investment and deleveraging; share repurchase program paused for the foreseeable future` (Q3 release `page:1`) |
| Stated leverage target | Management Language | Supportive (stated, not yet achieved) | A target range gives a reference for deleveraging policy, but timing is open-ended. | `We are committed to returning within our target leverage range of 2.0 - 2.5x over the medium-term` (Q3 release `page:12`) |
| Transparent reporting | Documentary Fact | Supportive | Quarterly detail on debt, segments and subsequent events; but the 10-K discloses prior material weaknesses, since remediated. | `While no material weaknesses were identified as of December 31, 2025` (10-K `page:84`) |
| Fox option and consent rights | Documentary Fact | Insufficient Information on willingness | The Group and Fox may interpret rights differently, so a future sale could limit actions the Group wishes to take, including financing. | `Fox’s interpretation of its rights in relation to the Fox Option may differ from that of Flutter.` (10-K `page:30`) |
| Priming, uptiering, drop-downs, non-pro-rata exchanges, collateral release | Insufficient Information | Not assessable | No such action is described in the sources. Legal capacity under the indenture and credit agreement cannot be tested because neither is supplied. Absence of evidence is not a favourable conclusion. | Not applicable: no source describes any such action |

Legal capacity (what the documents permit) is not assessable from the pack; willingness is shown by the documented repurchase pause and acquisition funding; feasibility is addressed by CP-1 (leverage and liquidity at Q3 2026) and CP-2.

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| November 24, 2023 | Credit agreement entered (term loans and revolver) | Documentary Fact | 10-K `page:125` |
| April 29, 2024 | 2029 senior secured notes issued by Flutter Treasury DAC | Documentary Fact | 10-K `page:127` |
| May 31, 2024 | Primary listing moved to the NYSE | Documentary Fact | 10-K `page:7` |
| September 25, 2024 | Board authorised the share repurchase programme | Documentary Fact | 10-K `page:130` |
| April 30, 2025 | Snai acquisition completed | Documentary Fact | Q3 10-Q `page:25` |
| May 14, 2025 | NSX 56% interest acquired | Documentary Fact | Q3 10-Q `page:25` |
| June 4 and August 7, 2025 | Term Loan B 2032 and 2031 notes issued; bridges repaid | Documentary Fact | 10-K `page:126`, `page:127` |
| Third quarter of 2025 | Boyd transaction bridge drawn on July 30; Boyd 5% stake acquired (cash flow line in the 2025 third quarter) | Documentary Fact | 10-K `page:9`, `page:126`; Q3 10-Q `page:9` |
| August 22, 2025 | India ban on online real money gaming; Junglee ceased | Documentary Fact | 10-K `page:12` |
| November 13, 2025 | New Italian gaming concessions effective, valid nine years | Documentary Fact | Q3 10-Q `page:48` |
| December 2025 | FanDuel Predicts launched with CME | Documentary Fact | 10-K `page:9` |
| February 26, 2026 | FY2025 annual report filed | Documentary Fact | Q3 10-Q `page:5` |
| April 2026 | UK remote gaming duty increase takes effect | Documentary Fact | Q3 10-Q `page:48` |
| June 2026 | IRS notices of proposed adjustments on fantasy sports | Documentary Fact | Q3 10-Q `page:41` |
| August 3, 2026 | LSE delisting (subsequent event in the Q2 10-Q) | Documentary Fact | Q2 10-Q `page:37` |
| September 25 and 26, 2026 | Brazil executive ban announced; operations ceased | Documentary Fact | Q3 10-Q `page:49` |
| October 1, 2026 | New CEO takes office (as announced in August) | Management Language | Q2 release `page:1` |
| October 20, 2026 | UKI restructuring committed (subsequent event) | Documentary Fact | Q3 10-Q `page:42` |
| October 30, 2026 | Credit agreement amendment (subsequent event); revolver increase effective November 3 | Documentary Fact | Q3 10-Q `page:42`, `page:74` |
| November 4, 2026 | Q3 2026 results; repurchase programme paused; 2026 guidance updated | Documentary Fact | Q3 release `page:1`, `page:12` |

### Conflicts

| Item | Source A | Source B | Effect |
| --- | --- | --- | --- |
| Country of the issuer | Context lists the country as `Netherlands` (context) | `Ireland 98-1782229` (10-K `page:1`) and `incorporated and domiciled in the Republic of Ireland` (Q3 10-Q `page:11`) | Logged, not reconciled. The filings are the issuer's own statements and are used; the context field is not issuer evidence. |
| Size of the October 2026 facility increase | `increasing the overall facility size by approximately $240m` (Q3 release `page:12`) | `has been increased to $1.86 billion` (Q3 10-Q `page:75`) against `$1.48 billion (£1.1 billion)` before (10-K `page:125`) | Logged, not reconciled. The release figure covers an undefined set of facilities. CP-2 must use the filing figures and carry the difference as unresolved. |
| Boyd stake: consideration against cash flow line | `for a consideration of $1,553 million` (10-K `page:9`) | `Acquisition of redeemable non-controlling interests — (1,620)` (Q3 10-Q `page:9`, nine months 2025) | Logged, not reconciled. The sources do not explain the difference between the stated consideration and the cash flow line (which may include other items); CP-2 should not use either as a debt-funding amount without the acquisition agreement. |
| Fast Code provision | `a provision of $109 million (A$157.5 million)` (Q3 10-Q `page:40`) | `$105 million relates to a provision recognized to facilitate a potential resolution of the Fast Code Class Action, partially offset by an adjustment in connection with the Indian GST matter` (Q3 10-Q `page:16`) | Different scopes (balance sheet provision against quarterly Adjusted EBITDA add-back net of a GST adjustment); not substituted for each other. |

### Credit translations

1. **Revenue durability.** Evidence: the revenue mix and regional split above (10-K `page:10`, `page:11`, `page:12`). Risk mechanic: revenue is spread over two segments, about 100 countries and many brands, so no single market is decisive; but sportsbook margin moves with sports results and tax rates are set by governments. Credit implication: diversification reduces the chance that one regulatory event impairs debt service, while regular tax and regulatory shocks reduce visibility of EBITDA and leave less room for leverage. Counter-evidence: the Brazil ban removed a region that was only 1% of FY2025 revenue, so geographic spread has so far limited revenue loss from individual bans.
2. **Margin and cash flow risk.** Evidence: UK remote gaming duty from 21% to 40% (Q3 10-Q `page:48`) and the UKI restructuring of up to 1,400 jobs with charges of `$80 million to $90 million` (Q3 10-Q `page:42`). Risk mechanic: the duty is charged within cost of sales, which lowered International margin in 2026 (CP-1); mitigation costs are cash and excluded from Adjusted EBITDA. Credit implication: cash conversion falls before savings arrive, which weighs on interest cover in the next twelve months (CP-1: LTM cover on cash interest of 3.67x), and a further duty rise is scheduled for April 2027.
3. **Concentration risk.** Evidence: US 43% of FY2025 revenue and the seasonality statement (10-K `page:11`, `page:12`). Risk mechanic: US earnings depend on league calendars, state tax changes (`North Carolina, where the sports betting tax rate increased from 18% to 23%`, Q3 10-Q `page:48`) and prediction market investment. Credit implication: the segment that the Group calls its largest growth opportunity (`We believe that our U.S. segment is the largest growth opportunity for the Group.`, Q3 10-Q `page:47`) currently produces the weakest earnings (CP-1: US Adjusted EBITDA of 241 for nine months 2026), so debt service relies on International for now. No customer concentration is disclosed.
4. **Ownership, sponsor alignment and the Fox option.** Evidence: no sponsor, no controlling holder identified; a Fox call option over 18.6% of FanDuel units at `$4.8 billion` as of December 31, 2025, compounding 5% a year, exercisable until December 2030 (10-K `page:29`, `page:132`). Risk mechanic: exercise requires cash payment to the Group, which would bring cash but reduce the Group's economic interest in FanDuel and could give Fox consent rights over matters such as acquisitions and debt incurrence if the former Fastball rights carry over; the filing says it `has not been determined what specific rights Fox may receive`. Credit implication: a possible deleveraging event with a loss of control over the largest growth asset; the timing is at Fox's choice and Fox must be licensed to exercise (10-K `page:132`). Fair value of the liability fell from 560 at December 31, 2025 to 100 at September 30, 2026 (Q3 10-Q `page:33`), a change that reflects management's valuation assumptions; the sources do not explain it in the pages read here. Counter-evidence: none logged.
5. **Capital allocation and leverage tolerance.** Evidence: debt-funded acquisitions, repurchases under the `$5 billion` programme, and the pause (Q3 10-Q `page:75`; Q3 release `page:1`). Risk mechanic: leverage at Q3 2026 is well above the stated range (CP-1), repurchases continued in the first half of 2026 before the pause (Q3 10-Q `page:7`, share repurchases in the first and second quarters), and the amendment raised the covenant level (`5.70:1.00`). Credit implication: leverage tolerance is high and the deleveraging path depends on earnings recovery and cash generation, which management has guided but not delivered (CP-1: net debt to Adjusted EBITDA of 4.55x against the 2.0 to 2.5x target).
6. **Key uncertainties.** Legal and tax matters with amounts disclosed (Indian GST demand of `₹50.6 billion ($527 million)` against a recorded `$54 million`, IRS proposed adjustments of about `$181 million` with no provision, and the Brazilian class action and NSX investigation; Q3 10-Q `page:41`, `page:49`, `page:50`) and the unavailability of the executed credit documents. Credit implication: these are claims outside the debt figure that could use cash or restrict financing; their size cannot be tied to covenant definitions from this pack.

### Monitoring items the source set lacks

| Missing item | Why it matters | Severity |
| --- | --- | --- |
| Executed credit agreement, indenture and the October 30, 2026 amendment | Terms, baskets, guarantor perimeter, restricted payment capacity and covenant definitions cannot be tested | Medium |
| Covenant compliance certificate and covenant EBITDA bridge | Headroom against the 5.20:1 and 5.70:1.00 tests is not calculable | Medium |
| Maturity schedule after the amendment | The reported schedule is pre-amendment | Medium |
| Shareholder register or proxy statement | Ownership and any significant holder are unknown | Low |
| Fox option agreement and FanDuel LLC agreement | Rights on exercise are described only as unresolved | Low |
| Investor presentations and rating agency reports | Management targets and ratings, which set the term A and revolver margin, are not stated | Low |

## Calculations

None. This module makes no calculation. Every figure is quoted from a cited source page or referenced from the accepted CP-1 handoff (LTM Adjusted EBITDA 2,331, total debt 12,313, cash 1,708, total debt to Adjusted EBITDA 5.28x, net debt to Adjusted EBITDA 4.55x, LTM cash interest cover 3.67x, nine-month US Adjusted EBITDA 241, capital expenditure LTM 817, impairment 873).

## Gaps

| Gap | Severity | Affected use | Action |
| --- | --- | --- | --- |
| No sponsor or controlling owner; shareholder detail is in a proxy statement not supplied. Ownership percentages are not inferred. | Low | Ownership, governance | Obtain the proxy statement if shareholder concentration matters. |
| Executed credit agreement, indenture, amendment and Fox option documents not supplied; legal capacity to prime, uptier, drop down or release collateral cannot be assessed. | Medium | Governance, CP-2 | Obtain documents; until then record behaviour as Insufficient Information. |
| No investor presentations; management targets are taken from releases only. | Low | Management Language | Treat targets as management claims. |
| Segment comparatives not recast for 2026 customer transfers (see CP-1). | Medium | Segment trends | Obtain recast comparatives. |
| Facility-size statements are unreconciled (approximately $240m against $1.86 billion). | Low | Liquidity | Use filing figures. |
| Country in the context differs from the filings. | Low | Profile | Use the filings. |
| Brazil and India legal exposures are open (class action, NSX investigation, GST demand); amounts beyond the stated provisions cannot be estimated. | Medium | Claims outside debt | Cover in the debt and claims module. |

## Next module

CP-2 runs next on the debt structure and should take from this answer: the transaction history behind the debt (the 2025 acquisition financing and the 2029 and 2031 notes), the October 30, 2026 amendment as a subsequent event described only in filing summaries, the unreconciled facility-size statements, the Fox option and minority put and call rights as claims outside debt, the open legal and tax matters, and the absence of any documented creditor-adverse action together with the absence of the documents needed to assess legal capacity. CP-5 should verify the locators and quotes in this answer, and in particular the conflicts table and the credit translations that cite CP-1 references. The next evidence action is to obtain the credit agreement amendment, the indenture and the covenant definitions.
