# CP-1A - Business and transaction context: Clear Channel Outdoor Holdings, Inc. (cco)

## Request

- Issuer: Clear Channel Outdoor Holdings, Inc. (issuer id `cco`, NYSE: CCO), consolidated, as of 2026-11-05 (information cutoff 2026-11-05). Pathway `credit_snapshot`, module CP-1A (business and transaction context). Reporting currency USD (context).
- Reader question: which transaction, business, ownership and operating facts matter most to a creditor? Decision drivers: transaction and ownership structure; business and operating model; credit-relevant history or change.
- Perimeter: the continuing operations of the consolidated group (America and Airports segments, with Singapore in Other). The Spain business is a discontinued operation held for sale at June 30, 2026 and sold on August 4, 2026.
- Information boundary: the latest supplied documents are dated August 5, 2026 (CP-0). Anything after that date, including the outcome of the pending merger, is Not supplied, not absent.
- Locator convention: "S1 page:14" is the retained text chunk numbered 14 of source S1, not a printed page. Quotes are exact substrings of the named chunk once line breaks are read as spaces and curly quotes as straight quotes. Figures are in USD; amounts quoted from the statements are in thousands where marked, otherwise in USD millions as the filings print them, and they agree with the CP-1 handoff where they overlap.
- Category tags used on every fact row: Documentary Fact; Management Language; Analyst Interpretation; Insufficient Information.
- Scope limits: no peer ranking, no instrument recommendation, no recovery conclusion. External material is labelled as such. Governance is assessed at issuer level only, from documented actions.

## Sources

### Issuer sources relied on

| Label | Exact source name | sha256 | Use in this handoff |
| --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cco-20251231.htm.jsonl | 571124584b3bbe99a4fbff8adfaba5f0fb8933c5a0003d1ef35708c36c286d39 | Business description, segments, merger risk factors, dispositions, debt activity, commitments |
| S2 | 10-Q_2025-09-30_cco-20250930.htm.jsonl | 607e09a97951d1ad4c47649541e08f4b1e6c417cc3bd1376061667bd020f7126 | Spain sale agreement of September 2025 |
| S3 | 10-Q_2026-03-31_cco-20260331.htm.jsonl | a3ad502aa08b83254f97c12e4f79050207a26c6003570b7bd60e33a1124d566c | Merger description at March 31, 2026 |
| S4 | 10-Q_2026-06-30_cco-20260630.htm.jsonl | fc57da6e0f4d7240050e6201742116917e571f4d11e190fcdcea84112429a51c | Latest merger status, debt amendments, Spain completion, segments, exhibit list |
| S5 | EX-99.1_2026-02-26_exhibit991-ccohearningsrel.htm.jsonl | 5cc1d0e97fcf82997c8a6a84c737a99df944d52765b5ff540d0441e7f806a5a6 | Merger announcement wording, FY2025 results, no guidance |
| S6 | EX-99.1_2026-05-06_exhibit991-ccohearningsrel.htm.jsonl | d85dec563195c10f63eb072d829bbf7b6a81552ec09b651fb1bdefa50ffbbbd6 | Merger wording at May 6, 2026 |
| S7 | EX-99.1_2026-08-05_exhibit991-ccohearningsrel.htm.jsonl | 86540d4f0d27c129f16354d25b76c67a8e72d707aa0c050724d976a7c4c17aa5 | Q2 2026 narrative, display counts, merger wording at August 5, 2026 |

### Supplied handoffs

| Module | sha256 | Use in this handoff |
| --- | --- | --- |
| CP-0 | c71e4b6220652757facb8cbe1e745147a9ea4d59240f1f57156457c376ee1b60 | Source readiness: information boundary at August 5, 2026, missing legal documents, guarantor list and Part III |
| CP-1 | fca9d4b8c375c5150877961d771a19c3bb05bdf148b7d27b2dc87fc69f48ca80 | Financial base: leverage, cover, liquidity, maturities and debt register that this handoff cross-refers to |

### Run settings (not issuer evidence)

Context file sha256 de960bbc410d3388b8cf7496a6e161733b9fd5ffc09b25a54e06ffd5d05f0294. It names the issuer, the as-of date, USD, the sector label "Services-Advertising" and a listed-equity ticker. Sponsor, parent, guarantors, ratings, deal terms and quotes are blank, and blank is not zero.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Clear Channel Outdoor is a U.S. roadside and airport advertiser with long-dated site contracts and heavy fixed rent. A take-private merger at 2.43 per share is pending, and its status after August 5, 2026 is unknown. | Medium | No source after August 5, 2026, and the merger agreement, debt documents and ownership table are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The merger agreement allows termination if the merger has not closed by November 9, 2026, extendable to February 9, 2027 if regulatory approvals are outstanding. | The cutoff falls four days before the first outside date, so the owner at the cutoff cannot be confirmed. | High |
| Amendments to the secured notes and credit agreement make the merger not a change of control, but they become operative only on closing. | Lender and noteholder protections depend on whether the merger closes; terms of consent payments are not supplied. | High |
| Airports Segment Adjusted EBITDA margin was 25.3% in H1 2026 against 41.0% for America, because airport site lease expense was 59.2% of revenue. | Airport growth adds fixed minimum-guarantee rent, so margins and cash flow are more exposed there than in roadside. | Medium |
| Substantially all international operations were sold in 2025 and 2026, and sale proceeds and cash reduced indebtedness by about 605 million in 2025. | The business is now almost wholly U.S., with few international assets left to sell as a deleveraging source. | Medium |
| Beneficial ownership is not in the supplied sources because the annual report defers it to an amendment that is not supplied. | Control, sponsor identity and any equity support after closing cannot be assessed. | High |

### Business and transaction view

Clear Channel Outdoor Holdings, Inc. is a listed U.S. out-of-home advertising operator with no controlling holder identified in the supplied sources, whose creditor story is a simplified, almost entirely domestic business sitting under a heavy, mostly unchanged debt stack while a take-private merger is pending. The operating base is roadside billboards and street furniture in the America segment and airport concessions in the Airports segment, together more than 64,500 displays at June 30, 2026, with digital displays a small share of inventory but a large share of revenue. Revenue is sold in short periods, mostly four weeks in roadside, against site leases and municipal and airport concessions that run for years with minimum guaranteed payments, so revenue visibility is short while the main cost is fixed or semi-fixed. That asymmetry is sharper in Airports, where site lease expense was 59.2% of revenue in H1 2026 against 31.3% in America (C1), so airport growth carries more fixed rent. Seasonality is steady: first quarter weakest and fourth quarter strongest. The credit-relevant history is a multi-year exit from international markets, completed with the sale of Spain on August 4, 2026, and a sequence of refinancings that moved secured maturities out to 2031 and 2033 while leaving the unsecured notes in 2028 and 2029. The transaction that matters most is the merger signed on February 9, 2026 with Madison Parent Inc., at 2.43 per share in cash, approved by stockholders on May 12, 2026 and expected, per the latest filing, to close by the end of the third quarter of 2026. The merger agreement lets either party terminate if closing has not happened by November 9, 2026, extendable to February 9, 2027 if regulatory approvals are outstanding, so the cutoff of November 5, 2026 falls four days before the first outside date, and the supplied sources do not say whether closing occurred. Debt amendments and conditional redemption notices tied to the merger exist, but they are described as pending. Ownership of the equity after closing, the merger financing, and the executed debt documents are not supplied. Documented issuer actions so far are mostly supportive or neutral for creditors, with disposal proceeds applied to debt and no dividends; none of the creditor-adverse actions in the method's checklist is documented in the supplied filings, which is a statement about the sources, not a finding about the executed documents.

### Company and operating model

| Area | Fact | Category | Source | Creditor mechanism |
| --- | --- | --- | --- | --- |
| Core activity and revenue model | Sells advertising on printed and digital out-of-home displays: roadside billboards and street furniture (America) and airport displays (Airports). Most America advertising is sold in four-week periods; Airports contracts typically run four weeks to one year. Q2 2026 revenue of 438,040 thousand split 388,985 thousand contracts with customers and 49,055 thousand leases | Documentary Fact | S1 page:12; S1 page:15; S4 page:14 | Short selling periods give little contracted revenue visibility, while costs are committed for years |
| Segment mix | America was 75% and Airports 25% of 2025 revenue from continuing operations. In H1 2026 America revenue was 602,803 thousand, Airports 208,827 thousand and Other 274 thousand | Documentary Fact | S1 page:11; S1 page:12; S4 page:12 | Roadside is the cash engine; Airports is the faster-growing, lower-margin segment |
| Footprint | At December 31, 2025: 48,220 America displays across 28 U.S. DMAs and 12,782 Airports displays of which 2,583 digital; operations in 81 DMAs including 43 of the top 50. At June 30, 2026: 64,521 displays in total, 5,145 of them digital | Documentary Fact | S1 page:11; S1 page:14; S1 page:15; S7 page:3 | Dense, permit-protected inventory is hard to replicate; permits and site rights are the asset base |
| Product mix | Bulletins were 76% of America revenue in 2025, posters 11%, spectaculars and wallscapes 5%, street furniture 3% | Documentary Fact | S1 page:12 | Revenue leans on large-format billboards, which the company says carry higher margins |
| Digital | Digital assets were "approximately 8% of our inventory but generated 44% of our revenue" in 2025; 71 large-format digital billboards were added in 2025; digital revenue in Q2 2026 was 195,426 thousand, 44.6% of revenue | Documentary Fact | S1 page:8; S4 page:24 | Digital conversion raises yield per structure but needs permits and capital spending |
| Customers and sales channel | No single advertiser was a material portion of consolidated revenue in 2025. National sales were 35.5% of America and 62.0% of Airports revenue in 2025; 33.9% and 57.8% in Q2 2026 | Documentary Fact | S1 page:11; S1 page:60; S1 page:61; S4 page:27; S4 page:28 | Diversified advertisers limit single-name risk; national budgets are cyclical and agency driven |
| Market concentration | Los Angeles was 12% of 2025 America revenue, New York 9% and San Francisco/Bay Area 7%. Q2 2026 growth cites the San Francisco/Bay Area and San Francisco International Airport with technology advertisers | Documentary Fact | S1 page:13; S4 page:24; S4 page:27; S4 page:28 | Sector and metro concentration (technology demand, large coastal markets) raises sensitivity to a local ad downturn |
| Contract tenor | Street furniture contracts with municipal and transit authorities generally run five to fifteen years; airport contracts five to ten years, each with a minimum fee and/or revenue share; roadside site leases generally one to twenty years | Documentary Fact | S1 page:16 | Long contracts lock in inventory but also fixed minimum payments |
| Cost structure | Site lease expense was 163,275 thousand of direct operating expenses of 196,178 thousand in Q2 2026. The company calls site lease payments its "most significant recurring operating cash requirement" | Documentary Fact | S4 page:24; S4 page:3; S4 page:30 | Rent dominates costs, so a revenue shortfall flows into margin quickly |
| Airport minimum guarantees | Airports site lease expense rose 12.0% in Q2 2026, reflecting "higher minimum guaranteed payments under certain airport contracts" and the renewal with the Metropolitan Washington Airports Authority, whose agreement carries 412.0 million of non-lease non-cancelable payments over 15 years | Documentary Fact | S4 page:28; S1 page:119 | Fixed airport rent rises with prior-period performance and persists if traffic or demand falls |
| Large contract | A 15-year contract with the New York Metropolitan Transportation Authority, effective November 1, 2024, has total undiscounted minimum lease payments of 390.0 million | Documentary Fact | S1 page:118 | A large fixed commitment inside the lease liabilities that sit outside the debt figure |
| Segment margins | Segment Adjusted EBITDA margin was 41.0% in America and 25.3% in Airports in H1 2026 (C1) | Analyst Interpretation | S4 page:12 | Airport growth dilutes consolidated margin unless site lease growth slows |
| Seasonality and cyclicality | Performance is typically weakest in the first quarter and strongest in the fourth; advertising spending generally correlates with gross domestic product | Documentary Fact | S1 page:16; S4 page:22; S4 page:23 | Liquidity is tightest in the first quarter; a recession hits both revenue and covenant-style metrics |
| Event-driven demand | Revenue growth in Q2 2026 reflected increased advertising activity associated with the 2026 FIFA World Cup, and in H1 2026 Super Bowl LX | Documentary Fact | S4 page:24 | Part of the 2026 growth is event driven and may not repeat |
| Capital spending | Capital expenditures of continuing operations were 61,784 thousand in FY2025 and 29,735 thousand in H1 2026; maintenance capital expenditures were 24,307 thousand in FY2025 | Documentary Fact | S1 page:99; S4 page:13; S5 page:10 | Capital needs are modest relative to EBITDA, so cash flow depends mainly on rent and interest |
| Working capital | Deferred revenue was 102,730 thousand at June 30, 2026 against 75,437 thousand at December 31, 2025 | Documentary Fact | S4 page:2 | Advance billings fund operations seasonally and reverse in weaker quarters |
| Competition and regulation | Competitors include Lamar Advertising Company and Outfront Media Inc.; billboard permits are regulated by state and local law and the Highway Beautification Act. External industry data cited by the company (an Omnicom model, not independently checked) puts out-of-home at 2.3% of U.S. advertising spend in 2025 | Documentary Fact | S1 page:6; S1 page:17 | Regulatory barriers protect incumbents but can delay digital conversions |
| Management characterisation | The company says "limited availability of our inventory generally allowing us to manage rates as demand increases" and calls itself the "leading airport advertising provider in the U.S. by traveler reach" | Management Language | S1 page:6; S1 page:12 | Promotional; not adopted as fact |

### Company profile

| Attribute | Detail | Category | Source |
| --- | --- | --- | --- |
| Registrant | Clear Channel Outdoor Holdings, Inc.; Delaware; Commission File Number 001-32663; principal offices at 4830 North Loop 1604 West, San Antonio, Texas | Documentary Fact | S4 page:1 |
| Listing and filer status | Common stock listed on the New York Stock Exchange under the symbol CCO; accelerated filer | Documentary Fact | S4 page:1 |
| Sector and country | Out-of-home advertising; operations substantially all in the United States, with Singapore not material. The context labels the sector "Services-Advertising" | Documentary Fact | S4 page:14; S1 page:11; context file |
| Origin | Separated from iHeartCommunications, Inc. on May 1, 2019 | Documentary Fact | S1 page:85 |
| Shares outstanding | 509,093,845 common shares at July 31, 2026; 161 stockholders of record at February 23, 2026 (excluding street-name holders) | Documentary Fact | S4 page:1; S1 page:51 |
| Dividends | No dividends intended; under the merger agreement none may be paid without the buyer's consent | Documentary Fact | S1 page:51 |
| Employees | About 1,900 at December 31, 2025, about 1,700 in the U.S. and the remainder primarily in Spain | Documentary Fact | S1 page:18 |
| Executive officers | President and Chief Executive Officer Scott R. Wells; Executive Vice President and Chief Financial Officer David J. Sailer; Executive Vice President, Chief Legal and Administrative Officer and Corporate Secretary Lynn A. Feldman; Senior Vice President and Chief Accounting Officer Jason A. Dilger; Executive Vice President and Chief Revenue Officer Robert C. (Bob) McCuin, as of February 26, 2026 | Documentary Fact | S1 page:20 |
| Auditor | Ernst & Young LLP, auditor since 2005; audit report dated February 26, 2026 | Documentary Fact | S1 page:75; S1 page:77 |
| Controlling holder or sponsor | Insufficient Information: beneficial ownership and directors are incorporated by reference to a Form 10-K/A that is not supplied, and the context names no sponsor | Insufficient Information | S1 page:135 |
| Prospective owner | Madison Parent Inc., owned by an investor consortium of affiliates and/or certain funds advised by Mubadala Capital; ownership percentages are not disclosed | Documentary Fact | S4 page:8 |
| Credit ratings | Insufficient Information: no source states a rating and the context leaves ratings blank; the annual report says only that corporate ratings are speculative-grade | Insufficient Information | S1 page:44 |
| Self-description | "a leading provider of out-of-home" advertising solutions | Management Language | S1 page:4 |

### Transaction summary and new debt issues

The pending transaction is the take-private merger. On February 9, 2026 the company agreed to be acquired by an investor consortium of affiliates and/or certain investment funds advised by Mubadala Capital through Madison Parent Inc. and Madison Merger Sub Inc., with Merger Sub merging into the company, which would survive as a wholly owned subsidiary of Parent (S1 page:4; S4 page:8). Holders of common stock would receive 2.43 per share in cash. The Hart-Scott-Rodino waiting period expired on April 9, 2026 and stockholders approved the agreement on May 12, 2026 (S4 page:8). The latest filing says closing is expected by the end of the third quarter of 2026, subject to remaining customary conditions including review by the Committee on Foreign Investment in the United States (S4 page:8). The annual report adds termination rights if the merger is not consummated on or before November 9, 2026, extendable to February 9, 2027 if requisite regulatory approvals are not obtained, a termination fee payable by the company of 39.8 million, or 19.9 million during the go-shop period, and a fee payable by Parent of 92.9 million under certain other circumstances (S1 page:24; S1 page:53; S1 page:54). The company has represented that the buyer has sufficient funds, but it also warns that the equity and debt financing contemplated by the merger agreement must be funded or closed (S1 page:24). The financing amounts, the sources of the buyer's equity and the post-closing capital structure are Not supplied. Until closing, the agreement restricts the company from incurring certain debt, paying dividends, settling certain proceedings and incurring certain capital expenditures without the buyer's written consent (S1 page:25). The first outside date, November 9, 2026, falls four days after the cutoff of November 5, 2026, and nothing in the supplied sources reports whether the merger closed or the dates moved.

The merger has direct debt consequences, all described as pending at August 5, 2026. In April 2026 the company completed consent solicitations with holders of its senior secured notes and with the lenders under its credit agreement, and in May 2026 with the lenders under its receivables-based credit agreement, entering into supplemental indentures and amendments dated April 9, April 10 and May 15, 2026 (S4 page:8; S4 page:9; S4 page:38; S4 page:39). These provide that the merger will not constitute a change of control under the debt documents; the supplemental indentures and the credit agreement amendment are effective but become operative only on consummation of the merger, and cease to be effective if it is not completed (S4 page:16). The receivables-based amendment, when effective, would extend the maturity of that facility to five years from the merger, raise revolving commitments from 200.0 million to 250.0 million, broaden the borrowing base and permit qualified securitisation financings (S4 page:16; S4 page:17). The company has also issued conditional notices of redemption for the 7.750% Senior Notes due 2028 and the 7.500% Senior Notes due 2029, conditional on closing (S4 page:17). Together these actions would remove the 2028 and 2029 unsecured maturities and keep the secured notes outstanding with changed change-of-control terms, but the consent terms, the redemption price and the source of redemption funds are Not supplied, and the executed supplemental indentures and amendments are cited in the exhibit list but not supplied (S4 page:38; S4 page:39). No new debt was issued in the first half of 2026: the six-month cash flow shows 145 thousand of debt repayments and no issuance line (S4 page:5).

Earlier new debt issues explain the current stack. In March 2024 the company issued 865.0 million of 7.875% Senior Secured Notes due 2030 and used part of the proceeds to prepay 835.0 million of its term loan, refinancing the remaining 425.0 million and extending its maturity to August 2028 (S1 page:69; S1 page:107). On August 4, 2025 it issued 1,150.0 million of 7.125% Senior Secured Notes due 2031 and 900.0 million of 7.500% Senior Secured Notes due 2033, and with cash on hand redeemed 1,250.0 million of 5.125% and 750.0 million of 9.000% senior secured notes; it paid 62.0 million of accrued interest, a 36.1 million redemption premium and 26.3 million of other fees, and recognised a 43.8 million loss on extinguishment (S1 page:69; S1 page:102). In June 2025 it extended the revolving and receivables-based facilities to June 12, 2030, reduced the revolver from 115.8 million to 100.0 million and raised the receivables-based facility from 175.0 million to 200.0 million (S1 page:102). In the second quarter of 2025 it repurchased 95.7 million of 7.750% and 134.1 million of 7.500% senior notes in the open market for 203.4 million including accrued interest and fees, recognising a gain of 28.8 million; the repurchased notes are held by the company and not cancelled (S1 page:102). The debt register, maturities and liquidity are in the CP-1 handoff: principal is 5,148.8 million at June 30, 2026 and no significant maturities fall before 2028.

The disposal programme is the other transaction thread. The company sold Switzerland, Italy and France in 2023, Mexico, Peru and Chile on February 5, 2025 for 34.0 million, the Europe-North segment to Bauer Radio Limited on March 31, 2025 for 625.0 million (net cash proceeds 572.0 million, part used to prepay the 375.0 million CCIBV term loan), and Brazil on October 1, 2025 for 15.0 million (S1 page:93; S1 page:94). It used proceeds and cash on hand to reduce indebtedness by approximately 605 million in 2025 (S1 page:55). The Spain sale agreed on September 7, 2025 for approximately 115 million euros (S2 page:9; S1 page:94) completed on August 4, 2026 for a purchase price of approximately 132.3 million dollars, with net proceeds subject to adjustments and fees; the company intends to use them to reduce debt, subject to the outcome of the merger (S4 page:9; S4 page:22). That completion is a subsequent event to the June 30, 2026 balance sheet and is not in the balance-sheet figures. At the offer price, equity consideration on 509,093,845 basic shares outstanding at July 31, 2026 is about 1,237.1 million before equity awards and any other dilutive instruments (C2); the supplied sources do not state the fully diluted equity value or the enterprise value.

### Ownership, control and governance

| Topic | Fact | Category | Source | Mechanic and limit |
| --- | --- | --- | --- | --- |
| Current control | No controlling holder, class structure or sponsor is identified in the supplied sources; there were 161 stockholders of record at February 23, 2026 | Insufficient Information | S1 page:51; S1 page:135 | Control rights, any large holder and board composition are in a Form 10-K/A and a proxy that are not supplied |
| Post-closing ownership | The company would become a wholly owned subsidiary of Madison Parent Inc.; the buyer is described as affiliates and/or funds advised by Mubadala Capital; percentages and any co-investor are not disclosed | Insufficient Information | S4 page:8 | A private owner could change leverage tolerance and distributions; nothing supplied shows its intent |
| Merger conduct covenants | Until closing the company has agreed to refrain from, among other things, incurring certain debt, paying dividends, settling certain legal proceedings and incurring certain capital expenditures without the buyer's consent | Documentary Fact | S1 page:25 | Limits new debt and distributions before closing; applies only while the agreement stands |
| Termination mechanics | Outside date November 9, 2026, extendable to February 9, 2027; company fee 39.8 million (19.9 million in the go-shop period); buyer fee 92.9 million in other circumstances | Documentary Fact | S1 page:24; S1 page:53; S1 page:54; S4 page:8 | The buyer fee is a contingent receivable and its collection is untested; the date sits four days after the cutoff |
| Disclosure posture | The company will not host an earnings call and is not providing financial guidance in light of the merger | Documentary Fact | S7 page:1; S5 page:1 | Less forward information for monitoring; filings remain the evidence base |
| Control environment | Disclosure controls were concluded effective at June 30, 2026, and the auditor expressed an unqualified opinion on internal control over financial reporting at December 31, 2025 | Documentary Fact | S4 page:37; S1 page:75 | No control weakness is reported in the supplied sources |
| Legacy regulatory matter | In 2024 the company made a 13.1 million payment to the SEC related to the resolution of the investigation of its former indirect, non-wholly-owned subsidiary, Clear Media Limited | Documentary Fact | S1 page:67 | A resolved legacy cost of a sold business; the sources do not describe current exposure |

### Issuer behaviour and creditor-relevant actions

| Action | Documented fact | Behaviour category | Source | Mechanic, and legal capacity, willingness and feasibility |
| --- | --- | --- | --- | --- |
| Disposals applied to debt | Used net proceeds from international sales and cash on hand to reduce indebtedness by approximately 605 million in 2025, including full prepayment of the 375.0 million CCIBV term loan | Supportive | S1 page:55 | Willingness shown by action; feasibility limited because substantially all international assets are now sold |
| Spain proceeds | Intends to apply net proceeds to reduce debt, subject to the outcome of the merger | Neutral or Mixed | S4 page:22 | An intention that the company ties to the merger, so willingness is conditional and the amount is not yet known |
| Discounted open-market repurchases | Bought 229.7 million of senior unsecured notes at a discount in the second quarter of 2025, recognising a 28.8 million gain; notes held, not cancelled | Neutral or Mixed | S1 page:102 | Reduces unsecured debt at less than face value, but purchases were not offered pro rata to all holders; later treatment of the held notes is not supplied |
| Secured refinancing | Extended secured maturities to 2031 and 2033 in August 2025 using new secured notes and cash; paid a 36.1 million redemption premium | Neutral or Mixed | S1 page:102 | Added maturity runway at a cash cost; pari passu secured structure continued |
| Merger consent solicitations | Obtained consents so that the merger is not a change of control under the secured notes and credit agreements | Neutral or Mixed | S4 page:16 | Removes a change-of-control trigger; consent consideration and holder rights under the executed documents are Not supplied |
| Conditional redemption of unsecured notes | Issued conditional notices to redeem the 2028 and 2029 unsecured notes if the merger closes | Insufficient Information | S4 page:17 | Redemption price and funding source are not supplied |
| Distributions | No dividends intended; none permitted without buyer consent | Supportive | S1 page:51 | No cash leakage to equity is documented in the supplied period |
| Other liability management | No priming, uptiering, drop-down, non-pro-rata exchange or collateral release is documented in the supplied filings | Insufficient Information | S1 page:111 | Indenture covenants limit liens, restricted payments and designation of unrestricted subsidiaries (S1 page:111), but baskets and executed terms are Not supplied, so legal capacity is not assessed |

### Timeline

| Date | Event | Status | Source |
| --- | --- | --- | --- |
| May 1, 2019 | Separation from iHeartCommunications, Inc. | Historical | S1 page:85 |
| March 31, May 31 and October 31, 2023 | Sales of Switzerland, Italy and France | Completed | S1 page:93 |
| March 2024 | 865.0 million 7.875% Senior Secured Notes issued; term loan partly prepaid and refinanced | Completed | S1 page:69 |
| November 1, 2024 | New York Metropolitan Transportation Authority 15-year contract effective | In force | S1 page:118 |
| February 5, 2025 | Sale of Mexico, Peru and Chile | Completed | S1 page:93 |
| March 31, 2025 | Sale of Europe-North to Bauer Radio Limited; CCIBV term loan prepaid | Completed | S1 page:94 |
| Second quarter 2025 | 229.7 million of unsecured notes repurchased | Completed | S1 page:102 |
| June 12, 2025 | Revolver and receivables-based facility extended to June 12, 2030 | Completed | S1 page:102 |
| August 4, 2025 | New 7.125% and 7.500% secured notes issued; 5.125% and 9.000% secured notes redeemed | Completed | S1 page:69 |
| September 7, 2025 | Spain sale agreement signed | Completed August 4, 2026 | S2 page:9; S4 page:9 |
| October 1, 2025 | Brazil sold | Completed | S1 page:94 |
| February 9, 2026 | Merger Agreement signed | Pending at August 5, 2026 | S1 page:4; S4 page:8 |
| April 9, 2026 | HSR waiting period expired; supplemental indentures dated this day | Subsequent to March 31, 2026 balance sheet | S4 page:8; S4 page:38 |
| May 12, 2026 | Stockholders approved the merger | Completed | S4 page:8 |
| August 4, 2026 | Spain sale completed | Subsequent event to June 30, 2026 | S4 page:9 |
| End of third quarter 2026 | Expected merger closing, per the latest filing | Status after August 5, 2026 Not supplied | S4 page:8 |
| November 9, 2026 | First outside date for terminating the merger agreement, extendable to February 9, 2027 (a contract term dated after the cutoff) | Future contract term | S1 page:24 |

### Conflicts and differences logged

| Item | Spans | Handling |
| --- | --- | --- |
| Description of the buyer | S3 page:7 and S6 page:1 say the consortium is "in partnership with TWG Global"; S4 page:8 describes "an investor consortium comprised of affiliates and/or certain investment funds advised by Mubadala Capital" without that phrase | Logged, not reconciled. The role of TWG Global after the Q1 2026 filings is Not supplied |
| Spain price in dollars | S2 page:9 gives approximately 134.9 million dollars at September 30, 2025 for about 115 million euros; S1 page:94 gives approximately 135.1 million dollars at December 31, 2025; S4 page:9 gives approximately 132.3 million dollars at completion | Exchange-rate translations of a euro price, not a conflict of fact; amounts received depend on adjustments and are Not supplied |
| Spain timing | S1 page:94 says the sale "is expected to close in the first half of 2026"; S4 page:9 says it completed on August 4, 2026 | Timeline drift, logged as a fact |
| Merger timing | S4 page:8 says closing is expected "by the end of the third quarter of 2026"; S1 page:24 gives November 9, 2026 as the first outside date | Both stand; no source reports the outcome |

### Credit translations

| Translation | Evidence | Risk mechanic | Credit implication | Counter-evidence |
| --- | --- | --- | --- | --- |
| Revenue durability | Short selling periods in roadside, long fixed site and concession contracts, a diversified advertiser base and 8.7% revenue growth in Q2 2026 (S1 page:12; S1 page:16; S1 page:11; S4 page:23) | Revenue resets every few weeks while rent is committed for years, so a demand dip hits margin before contracts roll | Operating leverage helps in recoveries and hurts in downturns; debt service depends on advertising demand holding | Event-driven growth in 2026 (S4 page:24) |
| Margin and cash-flow risk | Site lease expense is the largest cost; Airports lease expense was 59.2% of revenue in H1 2026 against 31.3% in America (C1) | Airport minimum guarantees rise with prior-period performance and persist when traffic falls | Faster airport growth adds fixed rent, so consolidated margin and cash conversion are more exposed than the roadside base suggests | Airports revenue grew 16.2% in H1 2026 (S4 page:28) |
| Concentration | America is 75% of revenue; Los Angeles is 12% of America revenue; technology advertisers in the San Francisco Bay Area and airport drove 2026 growth (S1 page:11; S1 page:13; S4 page:24) | A downturn in a few metros or one advertiser sector reaches a large share of revenue | Local demand shocks matter more than the national picture suggests | No single advertiser is material (S1 page:11) |
| Sponsor and owner alignment | The prospective owner is a consortium of funds advised by Mubadala Capital; no equity commitment, financing amount or post-closing capital plan is supplied | Willingness cannot be inferred from sponsor identity; capacity and feasibility are unknown | Treat ownership change as an unquantified risk to leverage tolerance and distributions; monitoring posture stays high | The debt amendments are designed to keep existing secured debt in place on closing (S4 page:16) |
| Key uncertainties | Merger status after August 5, 2026, executed debt documents, guarantor list and ownership table are not supplied | Closing would trigger redemption of unsecured notes, amended facility terms and a new owner; termination would leave the amendments without effect | The capital structure at the cutoff may differ materially from June 30, 2026; keep all conclusions dated | The merger-related documents are stated to cease to be effective if the merger is not completed (S4 page:16) |

### Consumer readiness

| Consumer | Readiness | What it should take from CP-1A | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Segment margin asymmetry, contract tenor and fixed rent, concentration, merger timeline and pending debt amendments, behaviour table and the logged differences | Business risk and the merger outcome shape how CP-1 leverage and cover are read | Merger status after August 5, 2026, merger financing and executed documents are Not supplied; carry them as restrictions |
| CP-5 | READY_WITH_LIMITATIONS | Locators for every fact row, the category tags, the logged differences and the dated timeline | Each claim must trace to a page chunk and stay within the cutoff | Check that no row states a post-August 5, 2026 event as fact; the outside date is labelled a future contract term |

## Calculations

All inputs are printed figures cited above, in USD thousands unless stated. Results are rounded half up to one decimal.

C1. Segment economics.
- Segment Adjusted EBITDA margin, H1 2026: America 247,079 / 602,803 = 41.0%; Airports 52,816 / 208,827 = 25.3%. Q2 2026: America 142,377 / 324,316 = 43.9%; Airports 29,890 / 113,601 = 26.3%. FY2025: America 501,038 / 1,196,824 = 41.9%; Airports 95,219 / 407,127 = 23.4%.
- Site lease expense over segment revenue, H1 2026: America 188,736 / 602,803 = 31.3%; Airports 123,589 / 208,827 = 59.2%. FY2025: America 376,908 / 1,196,824 = 31.5%; Airports 247,130 / 407,127 = 60.7%. Inputs from S4 page:12 and page:13 and S1 page:60, page:61 and page:99.
- Segment share of FY2025 revenue: America 1,196,824 / 1,604,140 = 74.6%, Airports 407,127 / 1,604,140 = 25.4%, equal to the printed 75% and 25% (S1 page:11; S1 page:12).
- Digital share of Q2 2026 revenue: 195,426 / 438,040 = 44.6%, equal to the printed percentage (S4 page:24).

C2. Implied equity consideration at the offer price, basic shares only: 509,093,845 shares at July 31, 2026 x 2.43 per share = 1,237,098,043, or about 1,237.1 million. It excludes equity awards, appraisal rights and any other dilutive instruments; the fully diluted figure is Not supplied. Shares issued less treasury at June 30, 2026: 527,979,483 - 18,967,026 = 509,012,457, consistent with the July 31 count (S4 page:3).

C3. Cross-checks to CP-1: debt principal 5,148.8 million at June 30, 2026 and no first-half 2026 issuance (145 thousand of repayments) reproduce the CP-1 position; the unsecured notes subject to conditional redemption total 899,311 + 905,950 = 1,805,261 thousand (S4 page:15).

## Gaps

- Merger status after August 5, 2026: closing, termination, the outside date of November 9, 2026 and any extension are Not supplied. High severity for CP-2 and CP-5. Remediation: filings and releases dated August 6, 2026 to November 5, 2026.
- Merger Agreement, financing commitments and post-closing capital structure: not supplied; the buyer's equity sources and the debt financing contemplated by the agreement are unknown.
- Ownership and board: beneficial ownership, directors and any controlling holder are in a Form 10-K/A and proxy that are not supplied. Control rights and prior ownership cannot be assessed.
- Executed indentures, credit agreements, the April 2026 supplemental indentures and amendments and the May 2026 receivables-based amendment: cited in exhibit lists, not supplied. Legal capacity for liability management, change-of-control terms and consent consideration are Not supplied.
- Redemption price and funding source for the conditional redemption of the 2028 and 2029 unsecured notes: not supplied.
- Guarantor list and guarantor financial information: not supplied (CP-0).
- Net proceeds of the Spain sale and their application: not supplied; the company ties application to the merger outcome.
- Top customers by name, advertiser sector split and contract-level renewal dates: not disclosed beyond national and local shares and the contracts named above.
- Ratings, market quotes and peers: blank in the context and not in any source; no peer comparison is made.
- Debt schedule at the cutoff, covenant certificate and add-back bridge for monitoring: the maturity schedule and Adjusted EBITDA bridge exist at June 30, 2026 (CP-1); no covenant certificate is supplied and the springing test was not in effect.

## Next module

- CP-2: read business risk as short-cycle revenue against long-dated fixed rent, with a sharper fixed-cost burden in Airports; read the merger as an unresolved event with a first outside date of November 9, 2026, four days after the cutoff; carry the missing executed documents, ownership and financing terms as restrictions; use CP-1 for leverage of 9.46x, cover of 1.40x and the debt register.
- CP-5: trace each fact row to its page chunk; confirm that nothing dated after August 5, 2026 is stated as fact; confirm that the outside date and the expected closing are labelled as contract terms or expectations; and check the logged differences against the quoted spans.
