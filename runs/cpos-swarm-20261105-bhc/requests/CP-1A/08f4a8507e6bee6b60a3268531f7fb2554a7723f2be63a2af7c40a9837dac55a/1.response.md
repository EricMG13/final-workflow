# CP-1A — Business and transaction context: Bausch Health Companies Inc. (bhc)

## Request

- Issuer: Bausch Health Companies Inc. (issuer id `bhc`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD, millions unless stated. Current period Q3 2026, prior period FY2025 (context).
- Run: `bhc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This module builds the business, ownership, transaction and governance fact pack a credit committee reads first, from a creditor perspective. It gives no peer ranking, instrument recommendation or recovery conclusion.
- Execution: host session. The host searched and read the pinned files and wrote this answer. No provider was called.
- Categories used to tag every fact row: Documentary Fact (a cited source states it), Management Language (management's characterisation, quoted and qualified), Analyst Interpretation (this analyst's reading of cited evidence), Insufficient Information (the evidence is missing).
- Perimeter: consolidated Bausch Health Companies Inc., which includes about 87% owned Bausch + Lomb (Q3 10-Q page:9). Figures follow the CP-1 handoff; periods are labelled Q3 2026, nine months 2026, nine months 2025, FY2025 and LTM Q3 2026 as in that handoff.

## Sources

Issuer sources relied on (page-numbered text extractions pinned by CP-OS; `page:N` is the extraction chunk, not a printed page):

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_bhc-20251231.htm.jsonl | dd4233546d8f09a0a7172210eae9b856cf06217c0da999f68b6e9a8283f6671d | Form 10-K for FY2025: business, customers, employees, dividends, exhibits |
| 10-Q_2026-03-31_bhc-20260331.htm.jsonl | 2ab4f9a58a29bd8e4f27c1aaa3b34a916ad63a6c5e24a2f2cf1f677d2bf1adb3 | Form 10-Q for Q1 2026 (read for balance sheet and financing note only) |
| 10-Q_2026-06-30_bhc-20260630.htm.jsonl | 9bd8cebbf75325a6e2424a90dc4ffd52c51b1a73535e612ffb413df53a0d5061 | Form 10-Q for Q2 2026 (read for balance sheet and financing note only) |
| 10-Q_2026-09-30_bhc-20260930.htm.jsonl | bbe6464eac7c28eba7ae73d3d4c1550a00ee295236fd32b72332e63bba1b2690 | Form 10-Q for Q3 2026: business, segments, financing, legal, subsequent events |
| EX-99.1_2026-04-29_ex991-q1x2026.htm.jsonl | a03142c8b51f52ce0bcea39df704d05d1ec6cd25d01c476f43f591aef5327135 | Q1 2026 earnings release (management) |
| EX-99.1_2026-07-29_ex991-q22026.htm.jsonl | b572ec3ee8791446c7753f44c437564f85dc7c22a9282dc8fe3094943c7ca9ed | Q2 2026 earnings release (management) |
| EX-99.1_2026-10-28_ex991-q32026.htm.jsonl | d176e2b2337e8c9ee765792690a4c9894f8e78c9eadadca91a11afce842a8bb9 | Q3 2026 earnings release (management): segments, guidance, outlook |
| context | ce3ba040ad702f7a097a4705cf09e05a5541c48113a20eaf4b83ee334242bc43 | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | f3a9713066d902ea831e33ca5e21c7518220ff0fc6d8658f54808a4e8892a5bd | Source readiness: perimeter, missing executed debt documents, missing Bausch + Lomb filings |
| CP-1 | 6416762ec0c950756779b461584b370e27dfe8cc5ec45b3b126353256df99610 | Financial base: debt, liquidity, leverage derived on EBITDA before goodwill impairments, maturities, conflicts |

Consistency with the handoffs: this answer adopts CP-1's correction of CP-0 on the Bausch + Lomb note issuers (the 8.375% notes due October 2028 were issued by Bausch + Lomb; the floating rate notes due January 2031 by Bausch + Lomb Netherlands B.V. and Bausch & Lomb Incorporated, Q3 10-Q page:35). It repeats CP-1's debt and liquidity figures without change.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| A Xifaxan-dependent U.S. pharmaceutical business sits in one group with Bausch + Lomb through a collateralised holding structure; Salix growth is price-led and Xifaxan faces a Medicare price in 2027 and expected generics in 2028. | Medium | Indentures, the credit agreement and Bausch + Lomb's own filings are not supplied, so legal capacity and creditor rights are described only from filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Salix is about 27% of nine-month 2026 revenue but about 47% of segment profit, and Xifaxan is about 85% of Salix. | Cash generation depends on one product line facing a 2027 Medicare price and 2028 expected generic entry. | High |
| Salix revenue growth of 343 came from price of 504, partly offset by lower volumes of 173 after exiting certain channels. | Growth is price-led; sustainability depends on pricing power that the 2027 negotiated price will limit. | High |
| 211,963,893 Bausch + Lomb shares are pledged to the 2025 facilities and 2032 notes at 126NumberCo, which ranks ahead of other creditors' claims on those shares. | Creditors outside that structure rank behind it for Bausch + Lomb value. | High |
| Documented actions since 2022 include an unrestricted subsidiary designation, a distressed exchange and a 2025 exchange that extended maturities; participation terms are not in the pack. | Behaviour is mixed: maturities were extended, but value moved into a structure that ranks ahead of some holders. | Medium |
| The Bausch Health chief executive is also interim chief executive and chairman of Bausch + Lomb, and a 50 buyback was authorised. | Overlapping roles and distributions bear on governance and creditor control, but the amounts are small. | Medium |

### Business and transaction view

The business is a specialty pharmaceutical and medical device group that sells about 60% of its revenue in the U.S. (FY2025, 10-K page:29) and holds about 87% of Bausch + Lomb, an eye health company that generates nearly half of consolidated revenue (4,013 of 8,317 for nine months 2026, Q3 10-Q page:75). Profit is concentrated: Salix, which sells mainly Xifaxan, produced 1,789 of 3,779 segment profit in nine months 2026 on 2,228 of revenue. The company states that generic Xifaxan is expected in 2028 and that a negotiated Medicare price takes effect on January 1, 2027 (page:96, page:98), and that Salix reporting unit goodwill was impaired by 1,426 after two Phase 3 trials of a new formulation failed in January 2026 (page:26).

The transaction history that matters to creditors is structural. Since 2022 the company has moved Bausch + Lomb shares into a holding company, 126NumberCo, and in 2025 used those shares as collateral for new first-lien debt that extended maturities from 2025 through 2028 to 2030 through 2032 (page:82, page:83). The Existing Senior Secured Notes are structurally subordinated to liabilities of 126NumberCo and to debt secured by assets outside their collateral such as the Bausch + Lomb share collateral (page:39), and the Senior Unsecured Notes are not guaranteed by 126NumberCo or 153NumberCo (page:130). Bausch + Lomb's earnings and net debt are excluded from the parent's financial maintenance covenant (page:40). Creditors therefore hold a claim on a group whose most valuable subsidiary sits in a separate credit silo, and the company has described a full separation of Bausch + Lomb as subject to targeted leverage ratios and approvals (page:10). Net proceeds from any sale of the pledged shares must be applied to prepay the 2025 term loan and the 2032 notes pro rata (page:33, page:38).

Recent operating momentum is real but price-led, and the legal and regulatory calendar is dense. The main uncertainties for monitoring are the Xifaxan price and generic timeline, the Bausch + Lomb separation path, refinancing of the 2028 to 2031 maturities, and the unsupplied debt documents.

### Company and operating model

| Segment or driver | What it is | 9M 2026 revenue | 9M 2025 revenue | 9M 2026 segment profit | 9M 2025 segment profit | Driver and creditor relevance | Category | Locator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Salix | U.S. gastroenterology products; Xifaxan is "approximately 85%" of segment revenue | 2,228 | 1,885 | 1,789 | 1,396 | Revenue rose 343 on net realized pricing of 504 and discontinued products of 12, less volumes of 173 after exiting certain channels. Price-led growth; Xifaxan faces a negotiated Medicare price from January 1, 2027 and expected generics in 2028 | Documentary Fact | Q3 10-Q page:75, page:123, page:96, page:98 |
| International | Branded, branded generic and OTC products outside the U.S., excluding Bausch + Lomb and Solta Medical | 889 | 826 | 277 | 253 | Revenue rose 63, of which 41 foreign currency and 24 price; no product group is 10% or more of segment sales | Documentary Fact | Q3 10-Q page:75, page:124 |
| Solta Medical | Global aesthetic devices; Thermage is "over 85%" of segment revenue | 512 | 381 | 242 | 177 | Revenue rose 131; the Q3 2026 organic change was a decrease of 4% with acquisitions of 29 and the China distributor acquisition driving reported growth | Documentary Fact | Q3 10-Q page:75, page:124; Q3 release page:2 |
| Diversified | U.S. neuroscience, dermatology, generics and dentistry pharmaceuticals | 675 | 682 | 449 | 448 | Slight revenue decline; Generics goodwill assessments revised forecasts for increased generic competition | Documentary Fact | Q3 10-Q page:75, page:25 |
| Bausch + Lomb | Global Vision Care, Surgical and Pharmaceuticals eye health (about 87% owned) | 4,013 | 3,696 | 1,022 | 729 | Consolidated but its cash and revolver are generally not available to the parent; its debt is outside the parent's covenant group | Documentary Fact | Q3 10-Q page:75, page:127, page:40 |
| Total segments | Five reportable segments | 8,317 | 7,470 | 3,779 | 3,003 | Segment profit excludes corporate costs of 786 (9M 2026), amortization, goodwill impairments and restructuring | Documentary Fact | Q3 10-Q page:75 |
| Concentration | Ten products represented 53% of total revenues in nine months 2026 and 50% in nine months 2025 | n/a | n/a | n/a | n/a | Salix is about 27% of revenue and about 47% of segment profit (2,228 / 8,317 and 1,789 / 3,779); Xifaxan at about 85% of Salix is roughly 1,894, about 23% of revenue (approximate, from "approximately 85%") | Analyst Interpretation | Q3 10-Q page:76, page:75 |
| Customers | FY2025 direct customer concentration: Cencora 18%, McKesson 16%, Cardinal Health 14% | n/a | n/a | n/a | n/a | Three wholesalers account for 48% of FY2025 revenue; price appreciation credits and rebates depend on wholesaler contracts | Documentary Fact | 10-K page:29, page:70 |
| Geography | FY2025 U.S. about 60% of revenue; China about 5%; no other country above 5% | n/a | n/a | n/a | n/a | U.S. pricing and Medicare policy dominate the revenue base | Documentary Fact | 10-K page:29 |
| Cost structure | Nine months 2026 cost of goods sold 2,195, SG&A 2,602, R&D 477, capex 252 | n/a | n/a | n/a | n/a | Costs are about 26%, 31% and 6% of revenue (2,195, 2,602 and 477 over 8,317); capex is about 3% (252 / 8,317) | Analyst Interpretation | Q3 10-Q page:6, page:8 |
| Working capital and gross-to-net | Accrued product rebates 1,377 and product returns 321 at September 30, 2026; trade receivables 2,533; inventories 1,591 | n/a | n/a | n/a | n/a | Revenue is net of rebates, chargebacks and returns that rely on management estimates; the auditor listed Medicaid rebates and sales returns allowances as a critical audit matter | Documentary Fact | Q3 10-Q page:5, page:27; 10-K page:215 |

### Company profile

| Field | Fact | Category | Locator |
| --- | --- | --- | --- |
| Legal entity | Bausch Health Companies Inc., a British Columbia, Canada company; principal offices in Laval, Québec | Documentary Fact | Q3 10-Q page:1 |
| Business description | "global, diversified specialty pharmaceutical and medical device company" in gastroenterology, hepatology, neuroscience and dermatology, plus eye health through about 87% ownership of Bausch + Lomb; products marketed in about 90 countries | Documentary Fact | Q3 10-Q page:9 |
| Country and sector | Country Canada, sector Pharmaceutical Preparations (context); reporting currency USD | Documentary Fact | context; Q3 10-Q page:3 |
| Listing | Common shares on the New York Stock Exchange and Toronto Stock Exchange under BHC; 374,266,716 shares outstanding as of October 23, 2026 | Documentary Fact | Q3 10-Q page:1 |
| Ownership of the issuer | Widely listed; the pack names no controlling shareholder or sponsor (context sponsor blank); a beneficial ownership table is not in the pack | Insufficient Information | context; 10-K page:3 |
| Ownership of Bausch + Lomb | Indirect holding of 310,449,643 common shares, about 87%; 126NumberCo owns 211,963,893 shares, about 68% of the holding (211,963,893 / 310,449,643), pledged as collateral; the filing also says 126NumberCo "directly or indirectly" holds approximately 87% | Documentary Fact | Q3 10-Q page:9, page:30, page:31 |
| Remaining Bausch + Lomb shares | 98,485,750 shares (310,449,643 less 211,963,893). They may be held through subsidiaries of 126NumberCo (page:40), but which entity holds them and whether they are pledged is not stated in the pages read | Insufficient Information | Q3 10-Q page:9, page:30, page:40 |
| Management | Thomas J. Appio is Chief Executive Officer of Bausch Health and from October 12, 2026 interim Chief Executive Officer of Bausch + Lomb; appointed to its board and chairman in August 2026 | Documentary Fact | Q3 10-Q page:76, page:138 |
| Employees | About 20,300 at December 31, 2025, of which about 13,000 were Bausch + Lomb employees | Documentary Fact | 10-K page:32, page:33 |
| Auditor | PricewaterhouseCoopers LLP; auditor since 2012; FY2025 critical audit matters were Medicaid rebates and sales returns allowances and goodwill impairment assessments of Salix and Generics | Documentary Fact | 10-K page:218, page:215, page:217 |
| Dividends | None declared or paid in 2025, 2024 or 2023; no cash dividends intended; the 2025 Credit Agreement and indentures restrict dividends | Documentary Fact | 10-K page:127 |
| Ratings (October 28, 2026) | Moody's Caa2 corporate; S&P B- corporate; Fitch B corporate with Rating Watch Evolving | Documentary Fact | Q3 10-Q page:131 |
| Guidance (management, October 28, 2026) | Full year 2026 revenue 10.975 to 11.175 billion and adjusted EBITDA 4.315 to 4.415 billion consolidated; Bausch Health (excl. B+L) adjusted EBITDA 3.225 to 3.275 billion; management forecast, not reported | Management Language | Q3 release page:4 |
| Management view of the portfolio | "The Company remains committed to evaluating all options for unlocking shareholder value, including maximizing the value of our Bausch Health and Bausch + Lomb assets." | Management Language | Q3 release page:4 |

### Transaction summary and new debt issues

No acquisition or leveraged buyout is pending at the issuer; the transactions that matter are financing and structural, and all are described from filings, not from the executed documents, which are not supplied.

The 2022 Exchange closed on September 30, 2022: validly tendered senior unsecured notes of 5,594 were exchanged for 3,125 of new secured notes, a reduction of principal of 2,469, and the company concluded it met the criteria for a troubled debt restructuring under ASC 470-60 (Q3 10-Q page:40). On November 29, 2022 the company designated 126NumberCo, which holds Bausch + Lomb, as an unrestricted subsidiary, so Bausch + Lomb and its subsidiaries are outside the covenants of the Bausch Health debt documents (page:39, page:40). In March 2025, in connection with the April 2025 refinancing, 126NumberCo was re-designated a restricted subsidiary while Bausch + Lomb and its subsidiaries remained unrestricted (page:40).

The April 2025 Refinancing Transactions closed on April 8, 2025: 126NumberCo entered the 2025 Credit Agreement (a 500 five-year revolving credit facility due April 8, 2030 and a 3,000 term loan B due October 8, 2030) and issued 4,400 of 10.00% senior secured notes due April 15, 2032. Proceeds repaid or redeemed 6,870 of principal in total (the February 2027 term loan B of 2,156 and certain notes), which the company says extended approximately 6,870 of maturities from 2025 through 2028 to 2030 through 2032 (page:29, page:82, page:83). In August 2025 the company repurchased and retired 9.25% senior unsecured notes of about 602 par for about 601 of cash on hand (page:40). In December 2025 the company and 126NumberCo exchanged 797 of 4.875% senior secured notes due 2028 and 886 of 11.00% first lien notes due 2028 for 1,600 of new 10.00% senior secured notes due April 2032, which form one series with the earlier 2032 notes, reducing outstanding principal by 83; 26,495,472 Bausch + Lomb shares were transferred to 126NumberCo as part of the transaction and the exchange was accounted for as a modification, not a troubled debt restructuring (page:30, page:83, page:84).

At Bausch + Lomb, the June 2025 refinancing added an 800 revolving credit facility due June 26, 2030, a 2,325 term loan B due January 15, 2031 and EUR 675 floating rate notes due January 2031; in January 2026 a new 2,802 term loan facility due January 15, 2031 refinanced the 2028 and 2031 term loans in full (page:35, page:36, page:84). No new bond issue by the parent is described for 2026 in the pages read; nine months 2026 issuance of long-term debt of 2,930 is described as primarily the 2,802 of Bausch + Lomb refinancing proceeds and 75 of revolver borrowings (page:126).

After the quarter, the company announced on October 28, 2026 that its subsidiary Bausch Health Americas, Inc. will issue an irrevocable redemption notice on October 29, 2026 for all of its 8.500% senior notes due 2027, about 643 of principal, with redemption scheduled for November 30, 2026 and funded from cash on hand (page:76). This is a subsequent event and is not in any September 30, 2026 balance. The board also authorised a share repurchase of up to 50 on October 24, 2026, aimed at offsetting dilution from 2027 management equity vesting per the release (page:76; Q3 release page:1). Bausch + Lomb agreed on October 8, 2026 to buy ophthalmic surgical manufacturing businesses for about 85 upfront, due at closing in the fourth quarter of 2026 (page:18).

Other transactions affecting business risk: the December 2025 acquisition of the aesthetics distribution business of Solta's China distributor for about 87 aggregate consideration (page:15); the September 2025 DURECT acquisition for 84 with potential sales-based milestones of up to 350 (page:17); and a December 2025 Bausch + Lomb purchase of manufacturing equipment for about 75 upfront with up to 35 of milestones (page:17).

### Ownership, control and creditor structure

| Item | Fact | Category | Locator |
| --- | --- | --- | --- |
| Collateral for 2025 facilities and 2032 notes | First priority lien on substantially all assets of 126NumberCo, including 211,963,893 Bausch + Lomb shares (the Bausch + Lomb Share Collateral); guaranteed by the Company and subsidiaries with secured guarantees | Documentary Fact | Q3 10-Q page:31, page:37 |
| Ranking of other creditors | Existing Senior Secured Notes are structurally subordinated to liabilities of non-guarantor subsidiaries including 153NumberCo and 126NumberCo and to debt secured by assets outside their collateral such as the Bausch + Lomb Share Collateral | Documentary Fact | Q3 10-Q page:39 |
| Sweep and mandatory redemption | Net proceeds of sales of Bausch + Lomb Share Collateral, and dividends above 50, must be applied to prepay the 2030 term loan and redeem the 2032 notes pro rata | Documentary Fact | Q3 10-Q page:33, page:38 |
| Covenant perimeter | Bausch + Lomb earnings and net debt are excluded from the financial maintenance covenant | Documentary Fact | Q3 10-Q page:40 |
| Change of control | Holders of the Existing Senior Secured Notes, the 2032 notes and the Senior Unsecured Notes may require repurchase at 101% | Documentary Fact | Q3 10-Q page:38, page:39, page:40 |
| Separation | The B+L Separation is "subject to the achievement of targeted debt leverage ratios and the receipt of any applicable shareholder and other necessary approvals"; no separation is scheduled in the pack | Documentary Fact | Q3 10-Q page:10 |
| Voidable transfer litigation | A declaratory judgment action by opt-out securities plaintiffs alleged transfers of assets to Bausch + Lomb would be voidable; a settlement was reached in August 2025 and a consent order dismissed the claims with prejudice on January 21, 2026; the filing also says the Company is to give plaintiffs certain notice of the intended completion of a potential future distribution under certain circumstances, without identifying in the pages read the instrument that imposes it | Documentary Fact | Q3 10-Q page:68, page:69 |
| Legal capacity (indentures, credit agreement) | Debt capacity, restricted payment, asset sale and designation baskets are not in the pack | Insufficient Information | CP-0 handoff; 10-K page:199 to page:211 (exhibit list only) |

### Governance and sponsor behavior

Assessed at issuer level from documented actions. The legal capacity column states what the documents are known to permit, willingness what was done, feasibility the liquidity and market access shown in CP-1.

| Action | Category | Behaviour category | Legal capacity, willingness, feasibility | Locator |
| --- | --- | --- | --- | --- |
| Exchange of unsecured notes for fewer secured notes in 2022, treated by the company as a troubled debt restructuring | Documentary Fact | Neutral or Mixed | Capacity not in pack. Willingness: a negotiated concession by holders, with a reduction of principal of 2,469. Feasibility: the company was under pressure to restructure. | Q3 10-Q page:40 |
| Designation of 126NumberCo, holding Bausch + Lomb, as unrestricted in 2022, and re-designation as restricted in 2025 with Bausch + Lomb remaining unrestricted | Documentary Fact | Insufficient Information | The designation capacity and tests are not in the pack. The company's own statement is that Bausch + Lomb value and debt sit outside the covenant calculation. | Q3 10-Q page:39, page:40 |
| 2025 refinancing and December 2025 exchange that placed Bausch + Lomb shares as collateral for new first-lien debt and extended maturities | Analyst Interpretation | Neutral or Mixed | For holders who exchanged or were repaid, maturities were extended and cash needs reduced (company statement, page:84). For holders who stayed in notes outside the 126NumberCo structure, value in the Bausch + Lomb shares ranks behind the new debt (page:39). Whether the exchange offers were pro rata or restricted to selected holders is not stated, so it cannot be classed creditor-adverse. | Q3 10-Q page:30, page:39, page:84 |
| August 2025 repurchase of 9.25% senior unsecured notes at near par from cash | Documentary Fact | Supportive | Deleveraging from cash on hand: about 602 par retired for about 601 | Q3 10-Q page:40 |
| No dividends; dividends restricted by debt documents | Documentary Fact | Supportive | No cash leakage to shareholders in FY2025, FY2024 or FY2023 | 10-K page:127 |
| 50 share repurchase authorised October 24, 2026 | Documentary Fact | Neutral or Mixed | A small distribution aimed at dilution; flexible and may be suspended or discontinued at any time | Q3 10-Q page:76 |
| Chief executive serves also as interim chief executive and chairman of Bausch + Lomb | Documentary Fact | Neutral or Mixed | The company itself discloses that overlapping roles "may create competing demands on management time and attention" and potential conflicts of interest | Q3 10-Q page:138 |
| Lump-sum payment of about 75 to the former Bausch + Lomb chief executive on departure | Documentary Fact | Neutral or Mixed | A cash cost at Bausch + Lomb; equity awards forfeited and cancelled | Q3 10-Q page:76, page:133 |
| Disclosure: reconciliations of adjusted EBITDA and adjusted cash flow, and a separate "excl. B+L" view | Documentary Fact | Supportive | Transparent perimeter split; adjusted measures exclude items such as legacy legal settlements and interest charged against premium, which is Management Language | Q3 release page:22, page:27, page:28 |

No drop-down, uptier or collateral release is documented in the pages read. The pack does not contain the documents needed to test legal capacity for any of these actions. No individual's qualities are assessed.

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| August 6, 2020 | Plan announced to separate the eye health business | Documentary Fact | Q3 10-Q page:9 |
| May 10, 2022 | Bausch + Lomb initial public offering; 35,000,000 shares sold | Documentary Fact | Q3 10-Q page:81 |
| September 30, 2022 | 2022 Exchange of unsecured notes for secured notes | Documentary Fact | Q3 10-Q page:40 |
| November 29, 2022 | 126NumberCo designated an unrestricted subsidiary | Documentary Fact | Q3 10-Q page:39 |
| April 8, 2025 | April 2025 Refinancing Transactions | Documentary Fact | Q3 10-Q page:29 |
| August 2025 | Repurchase of 9.25% unsecured notes | Documentary Fact | Q3 10-Q page:40 |
| September 2025 | DURECT acquisition | Documentary Fact | Q3 10-Q page:17 |
| November 25, 2025 | CMS announced the finalized maximum fair price for Xifaxan, effective January 1, 2027 | Documentary Fact | Q3 10-Q page:96 |
| December 2025 | December 2025 Exchange; Shibo Zhenmei acquisition; Bausch + Lomb equipment acquisition | Documentary Fact | Q3 10-Q page:15, page:17, page:30 |
| January 2026 | Phase 3 RED-C trials failed their primary endpoints; Salix goodwill impairment of 1,426 measured as of January 22, 2026; Bausch + Lomb refinancing term loan | Documentary Fact | Q3 10-Q page:26, page:36 |
| March 19, 2026 | FDA letter filed with the DC Circuit advising that Actavis (Teva) received final approval for generic rifaximin 550 mg tablets | Documentary Fact | Q3 10-Q page:58 |
| June to September 2026 | FDA Official Action Indicated, then a warning letter, for Bausch + Lomb's Tampa facility; no required shutdown or recall | Documentary Fact | Q3 10-Q page:99 |
| October 8, 2026 | Bausch + Lomb agreement to acquire surgical manufacturing businesses | Subsequent event (after September 30, 2026) | Q3 10-Q page:18 |
| October 12, 2026 | Chief executive transition at Bausch + Lomb | Subsequent event | Q3 10-Q page:76 |
| October 24, 2026 | Share repurchase authorised | Subsequent event | Q3 10-Q page:76 |
| October 28, 2026 | Redemption notice for 8.500% notes due 2027 announced; redemption scheduled November 30, 2026 (future date) | Subsequent event | Q3 10-Q page:76 |

### Legal and regulatory items with credit relevance

- Xifaxan: settled Paragraph IV cases are noted; Norwich's first ANDA is enjoined from final FDA approval until October 2029 (page:57); a second Norwich ANDA is in litigation, with a summary judgment hearing on October 7, 2026 and no trial date set (page:58); a DC Circuit opinion of August 25, 2026 partly reversed a lower court on Norwich's forfeiture theory and remanded to the FDA, and Teva's rehearing petition was denied on October 28, 2026 (page:58). The company still lists Xifaxan loss of exclusivity as expected in 2028 (page:98). The effect on the 2028 date is not quantified in the pack.
- Antitrust class actions allege the 2018 Actavis Xifaxan settlement is anticompetitive (page:55); no amount is quantified.
- Talc: remaining Shower to Shower suits are "subject to full indemnification obligations of Johnson & Johnson" (page:62), and the company expects not to incur material losses (page:64). This rests on the indemnitor's performance, which the pack does not test.
- Tax: Luxembourg assessment of EUR 271.7 million excluding interest; unfavourable ruling in March 2026, appeal heard October 15, 2026; no reserve recorded (page:48). The judgment, expected within 90 days of the hearing, is not in the pack.
- Pricing policy: the IRA negotiated price for Xifaxan applies from 2027; the company says the impact is expected to be most significant during 2027 (page:96).

### Conflicts logged

| Conflict | Source A (quote) | Source B (quote) | Downstream effect |
| --- | --- | --- | --- |
| Interest payments charged against debt premium, nine months 2026 | Q3 10-Q page:126: "$158 million of contractual interest payments on the Remaining Secured Notes (as defined below) allocated to the reduction of the recorded premiums" | Q3 release page:27: "Interest payments charged against debt premium (44) (87) (144) (251)" | Not reconciled here. The filing governs the premium accounting; the release's adjusted cash flow from operations uses its own figure. Same item as logged in CP-1. |

No other disagreement between sources was found for items used in this module. Where the company says Xifaxan generics are expected in 2028 and Norwich's first ANDA is enjoined until October 2029, these concern different applicants and are not a conflict on the same fact.

### Credit translations

1. Revenue durability and concentration. Evidence: Salix is about 27% of revenue and about 47% of segment profit, Xifaxan is about 85% of Salix, growth was price-led (price 504, volumes down 173), a negotiated price starts January 1, 2027 and generic entry is expected in 2028 (Q3 10-Q page:75, page:123, page:96, page:98). Risk mechanic: the product that earns the largest share of segment profit faces a price reset and then volume erosion just as 2028 maturities of 3,766 become due (CP-1). Credit implication: refinancing capacity in 2028 depends on how much Xifaxan cash flow remains, which makes monitoring of Xifaxan sales, the 2027 price effect and the generic timeline a leading indicator for refinancing risk. Counter-evidence: Salix profit rose 28% in nine months 2026 and management raised guidance; neither tests the post-2027 level.
2. Structural subordination and the Bausch + Lomb silo. Evidence: first-lien claims at 126NumberCo hold the pledged Bausch + Lomb shares, and other secured and unsecured notes rank structurally behind (page:31, page:39); Bausch + Lomb's net debt and earnings are outside the covenant perimeter (page:40). Risk mechanic: value from the Bausch + Lomb stake flows first to the 2025 term loan and 2032 notes through the sweep (page:33, page:38). Credit implication: recovery prospects for notes outside that structure depend on residual value in the shares and on Bausch Health (excl. B+L) assets, with no expected recovery stated here.
3. Margin and cash-flow risk. Evidence: derived EBITDA before goodwill impairments rose to 3,918 on an LTM basis, while FY2025 cash interest cover was 1.81x on interest paid of 1,810 (CP-1). Risk mechanic: high cash interest and premium accounting mean P&L interest understates cash cost. Credit implication: cover is modest on a cash basis, so a decline in Salix profit would reduce cover quickly.
4. Sponsor and governance alignment. Evidence: no dividends and a small buyback, an issuer-level pattern of maturity extension, but unresolved participation terms in exchanges and overlapping leadership of two listed entities (page:127, page:76, page:138). Credit implication: mixed; the pack neither shows leakage nor tests the indentures' restrictions.
5. Key uncertainties. The covenant ratio and its step-up date, the debt document baskets, and the 2028 maturity wall (CP-0, CP-1).

### Consumer assessment

| Consumer | Readiness | What it should take from this module | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 | Ready with limitations | Product concentration, price-led growth, 2027 and 2028 Xifaxan timeline, structural subordination, governance observations, timeline of events | These drive the credit assessment and the thesis | Debt documents and Bausch + Lomb filings not supplied; fourth quarter 2025 adjusted EBITDA not supplied | Carry gaps into CP-2 gaps ledger; do not state a recovery outcome |
| CP-5 | Ready with limitations | All locators here are chunk numbers with quoted spans; derived percentages are labelled Analyst Interpretation | Evidence trace validation | Text extraction only | Check the derived shares (27%, 47%, 23%, 68%) against the cited figures |

## Calculations

Inputs are printed figures from the cited pages. All amounts US$ millions unless stated.

- Salix share of revenue, nine months 2026: 2,228 / 8,317 = 26.8%, stated as about 27%.
- Salix share of segment profit, nine months 2026: 1,789 / 3,779 = 47.3%, stated as about 47%.
- Xifaxan revenue, approximate: 0.85 × 2,228 = 1,894; 1,894 / 8,317 = 22.8%, stated as about 23%. The 85% is printed as "approximately".
- Bausch + Lomb share of revenue: 4,013 / 8,317 = 48.3%; of segment profit: 1,022 / 3,779 = 27.0%.
- Salix revenue change: 2,228 − 1,885 = 343, equal to price 504 plus discontinued products 12 less volumes 173 (504 + 12 − 173 = 343). Percent change 343 / 1,885 = 18.2%, printed as 18%.
- Pledged Bausch + Lomb shares: 211,963,893 / 310,449,643 = 68.3%; unpledged or elsewhere: 310,449,643 − 211,963,893 = 98,485,750 shares (holder not stated).
- Wholesaler concentration FY2025: 18% + 16% + 14% = 48%.
- Costs as percent of revenue, nine months 2026: 2,195 / 8,317 = 26.4%; 2,602 / 8,317 = 31.3%; 477 / 8,317 = 5.7%; capex 252 / 8,317 = 3.0%.
- Segment totals: revenue 2,228 + 889 + 512 + 675 + 4,013 = 8,317; segment profit 1,789 + 277 + 242 + 449 + 1,022 = 3,779. Prior year: 1,885 + 826 + 381 + 682 + 3,696 = 7,470; 1,396 + 253 + 177 + 448 + 729 = 3,003.
- Dec 2025 exchange: 797 + 886 = 1,683 exchanged for 1,600 new, a reduction of 83, as printed.
- Redemption of 643 of 2027 notes: see CP-1 for the pro forma maturity effect (701 − 643 = 58 consolidated).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Indentures, 2025 Credit Agreement, intercreditor and collateral documents not supplied: legal capacity for designations, exchanges, restricted payments and debt incurrence cannot be assessed | High | CP-2, CP-5 | Supply executed documents from the 10-K exhibit list (10-K page:199 to page:211) |
| Participation terms of the 2022 and December 2025 exchanges (pro rata or selective) not in the pack | High | CP-2 | Supply exchange offer documents and 8-Ks |
| Holder and pledge status of the 98,485,750 Bausch + Lomb shares outside the 126NumberCo holding | Medium | CP-2 | Supply the 2025 Credit Agreement collateral schedule or Bausch + Lomb disclosures |
| Beneficial ownership table and any controlling or significant shareholder | Medium | CP-2 | Supply the proxy statement |
| Bausch + Lomb standalone filings, covenants and governance | Medium | CP-2 | Supply Bausch + Lomb Form 10-Q and credit agreement |
| Quantified effect of the 2027 negotiated Xifaxan price and of generic entry on revenue and profit | High | CP-2 | Not disclosed in the pack; request management detail or monitor quarterly |
| Covenant certificate and covenant-definition add-back bridge not supplied | High | CP-2 | Supply compliance certificate and 2025 Credit Agreement definitions |
| Outcomes of legal and tax matters after October 29, 2026, including the Luxembourg appeal judgment and November 3, 2026 mediation | Medium | CP-2 | Supply later filings |
| Text extraction only; no check against filed HTML | Low | CP-5 | Supply original HTML or XBRL |

## Next module

CP-2 follows with the fundamental credit synthesis, taking from this module: the concentration of profit in Salix and Xifaxan, the price-led growth, the January 1, 2027 negotiated price and expected 2028 generic entry, the Bausch + Lomb collateral and covenant perimeter structure, the mixed governance observations and the unresolved legal capacity, and the logged conflict on interest charged against premium. CP-2 should keep CP-1's figures (LTM derived EBITDA before goodwill impairments 3,918; debt to EBITDA 5.15x; net 4.51x) and carry every gap above. CP-5 then traces the evidence.
