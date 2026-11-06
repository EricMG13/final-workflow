## Request

Module CP-1A, business and transaction context, for Service Properties Trust (SVC, issuer id svc), as of 2026-11-05 (cutoff 2026-11-05), pathway credit_snapshot, reporting currency USD. Reader question: which transaction, business, ownership and operating facts matter most to the creditor. The module builds the business and operating-model fact pack, the company profile, the transaction summary and the governance read, from the pinned filings and the two upstream handoffs, and carries their limitations.

Perimeter: the registrant, Service Properties Trust, and its consolidated subsidiaries. No sponsor, parent or separate borrower exists in the run context. Amounts are USD thousands as the filings print them unless stated. Locators `page:N` are chunk numbers in the pinned extraction files, not printed pages. Short names: 10-K FY2025, 10-Q Q1, 10-Q Q2 and 10-Q Q3.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_svc-20251231.htm.jsonl | 15b3016df80eabdf6701b53b9a448339a1d5ae915a5566d3f751538a9f1cf080 | Business description, 2025 history, RMR termination terms, Series 2026-1 pricing note, zero coupon notes |
| 10-Q_2026-03-31_svc-20260331.htm.jsonl | ddc1e35889e90bee1694334ce247e9f387726f16b7ce89bd8b9a51b4f4bc89df | Read for Q1 2026 context; no figure relied on beyond the CP-1 handoff |
| 10-Q_2026-06-30_svc-20260630.htm.jsonl | da660527db0f1353ac545e91f43f35b2233d5df64df735bb0e6f23f04bc598ba | Read for Q2 2026 context; no figure relied on beyond the CP-1 handoff |
| 10-Q_2026-09-30_svc-20260930.htm.jsonl | f0504ddf51d9be829b263ff0aec5ab5ea7aa542d5518e107dbff10e9d9d5c34a | Leases and management agreements, related persons, equity offering, mortgage notes, hotel statistics, subsequent events |
| EX-99.1_2026-05-06_svc_033126xexhibitx991.htm.jsonl | 2f1a4993f8cd70e48576dc6e794111c2977d7a50e2e8b2ecb75d059468ae6628 | Announcement only; portfolio counts at March 31, 2026 |
| EX-99.1_2026-08-05_svc_063026xexhibitx991.htm.jsonl | fb76ab0c1c7105cbf6ef323f85f2c808f256d901d8e982c18e3c61667221ab25 | Announcement only; portfolio counts at June 30, 2026 |
| EX-99.1_2026-11-04_svc_093026xexhibitx991.htm.jsonl | 865a9819dca5454c3d53aca165a47efc28c6cf0685e35747e559ffc2c9cf026d | Announcement only; portfolio counts at September 30, 2026 and mention of an investor presentation that is not in the pack |

The context input (sha256 a72cf33ce12be07f9ed0051d7ed4f82ab1f3905d4d81ff0fe1a5919c08327fd3) holds the requester's settings and is not issuer evidence. It names no sponsor, parent, guarantor, deal term or rating.

### Handoffs

| Module | sha256 | Used for |
| --- | --- | --- |
| CP-0 | 0fbb7ad07aadbbd8b3c01b679bc383a79e711cd00b11da3f74ea1f9d0cbdcdab | Source readiness, document families, gaps. Read in full; its limitations are carried below. |
| CP-1 | 6a8c23e0c79168d7d90c853c411952c21d17df0c9783a68c6978b27d49e01d73 | Financial base, debt table, liquidity, covenant tests, leverage and cover. Read in full; its figures are used as stated there. |

This answer corrects nothing in either handoff. It adds business and governance detail and one secured-share comparison that CP-1 did not state (see Calculations). CP-1 had already corrected CP-0 on the revolver covenant terms printed in the 10-K, and that correction stands.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Service Properties Trust is an externally managed REIT whose rent comes largely from one tenant, while its hotels, run mostly by an affiliated operator, are being sold. 2026 deleveraging was funded by equity and secured debt. | Medium | No investor presentation, rating or tenant financials are in the pack, and ownership beyond two holders near 6% is not disclosed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| TravelCenters of America pays 68.2% of annualized minimum rent under five leases that expire in 2033, backed by a capped guaranty from BP Corporation North America. | Rent durability rests on one tenant and one guarantor, and the leases expire one year after the 2032 notes mature. | High |
| Hotels were 74.7% of Q3 2026 revenue, and Sonesta, an affiliate controlled by the Chair, manages 62 hotels. | Hotel earnings are volatile and a related party sets the fees, so operating results and governance both matter to creditors. | High |
| The Trust has no employees and RMR manages it; terminating RMR without cause would require a fee based on the present value of 19 to 20 years of fees. | Management is hard to replace, and RMR ceasing to be manager is a change of control under the credit agreement. | High |
| 2026 financing replaced unsecured notes with secured and equity capital; the secured share of principal debt rose from 40.5% to 62.9%. | Remaining unsecured noteholders sit behind more secured claims, although equity raised and debt retired support the credit. | Medium |

### Business and transaction view

The business is a two-engine REIT with different risk profiles. About a quarter of revenue is contractual rent from service-focused retail net lease properties, and the rest is hotel operating revenue where the Trust carries the operating cost and pays managers. The net lease engine is concentrated: one tenant, TravelCenters of America, accounts for 68.2% of annualized minimum rent through five master leases that expire in 2033, with a limited BP guaranty and rent coverage on those leases of 1.32x to 1.61x, against 2.17x for the whole net lease portfolio and at least 2.18x for every other top ten brand. The hotel engine is being shrunk: 112 hotels were sold in 2025, more in 2026, and 53 Sonesta managed hotels plus 17 Hyatt and seven Radisson hotels are the stated retained set.

The Trust is externally managed. It has no employees, RMR provides all personnel, and the Chair, who is also a Managing Trustee, controls Sonesta and, through ABP Trust, the parent of RMR. That makes three related-party strands, manager, hotel operator and equity investee, which sit on both sides of fee, capital spending and asset-sale decisions. Documented behaviour in 2026 was supportive of creditors: the manager joined the equity offering, distributions were held at 0.05 per share per quarter, and the proceeds retired 1,550,000 of unsecured notes, and cash retired a 45,000 variable funding note. The same year raised the secured share of principal debt, which moves claim ranking against unsecured noteholders, although it was done through new, disclosed financings and not by amending existing notes; no non-pro-rata exchange, uptier or drop-down of existing noteholders is documented in the pack.

Evidence quality is high for filed facts and low-to-medium for manager-reported hotel statistics and tenant-reported rent coverage, which the company states it does not verify. The investor presentation referenced in the November 4, 2026 announcement is not in the pack, so management language beyond the filings is unavailable.

### Company and operating model

| Area | Fact | Category | Locator and quote | Mechanism and credit implication |
| --- | --- | --- | --- | --- |
| Core activities | A REIT investing in service-focused retail net lease properties and hotels | Documentary Fact | 10-Q Q3 page:7 "invests in service-focused retail net lease properties and hotels" | Two cash-flow streams: contractual rent and operating hotel results; the mix is shifting toward rent, which lowers volatility of debt service coverage |
| Portfolio at September 30, 2026 | 740 net lease properties with 188 tenants at 97.6% occupancy; 87 hotels | Documentary Fact | 10-Q Q3 page:12 "we owned 740 service-focused retail properties net leased to 188 tenants"; page:55 "our net lease properties were 97.6% occupied" | High occupancy supports rent visibility; 18 vacant properties are the only unleased net lease assets |
| Net lease revenue model | Triple net leases with annualized minimum rent of 395,492 and a 7.0 year weighted remaining term | Documentary Fact | 10-Q Q3 page:12 "annual minimum rents of $395,492 with a weighted (by annual minimum rents) average remaining lease term of 7.0 years" | Fixed contractual rent with tenant-borne operating cost gives cash-flow visibility if tenants pay |
| Tenant concentration | TA leases 175 travel centers under five master leases; TA is 34.2% of total historical real estate investments and 68.2% of annualized minimum rent; BP guarantees the leases up to a cap of 2,782,917 | Documentary Fact | 10-Q Q3 page:12 "TA is our largest tenant, representing 34.2% of our total historical real estate investments"; page:57 "BP Corporation North America Inc. guarantees payment under each of the five master leases" | A single-name credit drives most rent; the BP guaranty is limited to a cap and its terms beyond the cap are not in the pack |
| Lease expiry profile | 69.4% of annualized minimum rent expires in 2033 | Documentary Fact | 10-Q Q3 page:58 "2033 203 5,338,721 274,609 69.4% 82.8%" | The TA lease expiry follows the 2032 notes by one year, so refinancing and re-leasing risk converge; renewal options held by TA are not a commitment |
| Rent coverage | Portfolio coverage 2.17x; TA lease coverage 1.35x, 1.43x, 1.53x, 1.61x and 1.32x for leases one to five | Management Language | 10-Q Q3 page:43 "Operating statements furnished by our tenants often are unaudited" | Coverage is tenant-reported and unaudited; the lowest coverage among the top ten brands is on the largest tenant, so it is the weakest-evidenced and most important input |
| Hotel operating model | 87 hotels leased to taxable REIT subsidiaries and run by four managers: Sonesta 62, Hyatt 17, Radisson 7, IHG 1 | Documentary Fact | 10-Q Q3 page:45 "We lease 87 hotels to our wholly owned TRSs that are managed by hotel operating companies"; page:12 "Sonesta (62 hotels), Hyatt Hotels Corporation, or Hyatt (17 hotels)" | The Trust bears hotel operating costs and fees, so hotel earnings are operationally levered and not contractual rent |
| Hotel pricing and volume | Retained hotels in Q3 2026: occupancy 72.6% against 69.3%, ADR 176.95 against 171.08, RevPAR 128.38 against 118.53 | Documentary Fact | 10-Q Q3 page:59 "Retained Hotels Total/Average 77 17,593 72.6 % 69.3 % 3.3 pts $176.95 $171.08 3.4 % $ 128.38 $ 118.53 8.3 %" | Improving RevPAR on retained hotels; manager-reported and unverified by the company |
| Hotel recovery driver | Management attributes part of the RevPAR gain to the weak 2025 comparison | Management Language | 10-Q Q3 page:35 "which we believe are partially a result of renovation disruption in the 2025 period" | Part of the gain is a base effect and may not repeat |
| Hotel cost structure | Retained Sonesta agreements pay base fees of 3.0% of gross revenues for full service and 5.0% for extended stay and select service, plus incentive, brand and other fees | Documentary Fact | 10-Q Q3 page:15 "a base management fee equal to 3.0% of gross revenues for full service hotels and 5.0% for extended stay and select service hotels" | Fees rank ahead of the Trust's return, so hotel margins are squeezed in a downturn |
| Capital spending | 73,498 funded above FF&E reserves in nine months 2026; 25,000 to 40,000 expected in the last three months | Documentary Fact | 10-Q Q3 page:45 "we funded $73,498 for capital improvements in excess of FF&E reserves available to our hotels" | Hotel capital needs absorb operating cash flow and the Trust must fund them under the Sonesta agreements |
| Working capital | 29,898 of initial working capital advanced to Sonesta | Documentary Fact | 10-Q Q3 page:17 "we had advanced $29,898 and $31,835, respectively, of initial working capital to Sonesta" | Cash tied up with a related-party manager; returned only on termination of the applicable agreements |
| Segment economics | Q3 2026 segment profit: net lease 36,414, hotels (52,142), total (15,728) | Documentary Fact | 10-Q Q3 page:31 "Segment profit (loss) 36,414 (52,142) (15,728) 47,206 6,909 54,115" | The hotel loss is driven by impairment of hotels held for sale; the segment is not yet self-supporting after impairments |
| Strategy | Reduce debt and shift to a majority net lease portfolio | Management Language | 10-Q Q3 page:34 "Our strategy continues to focus on reducing debt, transitioning to a company with the majority of our properties being service-focused retail net lease properties" | Credit-positive if executed, but asset sales depend on buyers and pricing |
| Geography | 827 properties in 46 states, the District of Columbia, Canada and Puerto Rico | Documentary Fact | 10-Q Q3 page:34 "we owned 827 properties in 46 states, the District of Columbia, Canada and Puerto Rico" | Diversified by location; concentration is by tenant rather than geography |
| Operating platform | No employees; all services provided by RMR | Documentary Fact | 10-Q Q3 page:26 "We have no employees." | Operating continuity depends on RMR and on the management agreements remaining in force |

### Company profile

| Item | Value | Category | Locator and quote |
| --- | --- | --- | --- |
| Legal entity and form | Service Properties Trust, a Maryland REIT organized February 7, 1995 | Documentary Fact | 10-Q Q3 page:7 "organized on February 7, 1995 under the laws of the State of Maryland" |
| Listing | Common shares listed on the Nasdaq Stock Market under SVC | Documentary Fact | 10-Q Q3 page:1 "Common Shares of Beneficial Interest SVC The Nasdaq Stock Market LLC" |
| Headquarters and country | Newton, Massachusetts, United States; properties also in Canada and Puerto Rico | Documentary Fact | 10-Q Q3 page:1 "Two Newton Place, 255 Washington Street, Suite 300, Newton, Massachusetts" |
| Sector | Real estate investment trust; service-focused retail net lease and hotels | Documentary Fact | 10-Q Q3 page:7 "invests in service-focused retail net lease properties and hotels" |
| Filer status | Accelerated filer | Documentary Fact | 10-Q Q3 page:1 "Large accelerated filer ☐ Accelerated filer ☒" |
| Auditor | Deloitte & Touche LLP, Boston, for FY2025 | Documentary Fact | 10-K FY2025 page:171 "/s/ Deloitte & Touche LLP" |
| Shares outstanding | 129,813,906 at November 2, 2026, after the 1-for-5 reverse split | Documentary Fact | 10-Q Q3 page:1 "outstanding as of November 2, 2026: 129,813,906" |
| Ownership | Listed and widely held; RMR holds about 6.4% and Mr. Portnoy, including through ABP Trust, about 6.8%; no other holder is disclosed in the pack | Documentary Fact | 10-Q Q3 page:29 "RMR beneficially owned approximately 6.4% of our outstanding common shares and Mr. Portnoy, including through ABP Trust, beneficially owned approximately 6.8% of our outstanding common shares" |
| Sponsor | None named; the context leaves sponsor blank | Insufficient Information | Not applicable: no sponsor is identified in the sources or context; this is not an adverse finding |
| Manager | RMR provides business and property management under two agreements | Documentary Fact | 10-Q Q3 page:26 "We have two agreements with RMR to provide management services to us" |
| Manager termination terms | Terminating without cause or for performance requires a fee equal to the present value of future fees over 19 to 20 years, or ten years for performance | Documentary Fact | 10-K FY2025 page:100 "the sum of the present values of the monthly future fees"; "which, depending on the time of termination, would be between 19 and 20 years" |
| Manager change of control | RMR ceasing to act as business manager is a change of control under the credit agreement | Documentary Fact | 10-Q Q3 page:21 "a change of control of us, which includes The RMR Group LLC, or RMR, ceasing to act as our business manager" |
| Board leadership | Adam D. Portnoy is Chair and a Managing Trustee and controls ABP Trust, the controlling shareholder of RMR Inc. | Documentary Fact | 10-Q Q3 page:28 "Adam D. Portnoy, is the sole trustee, an officer and the controlling shareholder of ABP Trust" |
| Hotel operator affiliation | Sonesta is private and controlled by Mr. Portnoy; the Trust owns 34% of it | Documentary Fact | 10-Q Q3 page:28 "Sonesta is a private company of which Mr. Portnoy, one of our Managing Trustees, is a director and the controlling stockholder"; page:29 "we owned 34% of Sonesta" |
| Credit ratings | Not supplied: the context is blank and the filings discuss ratings only generically | Insufficient Information | Searched the 10-K and Q3 10-Q for ratings and downgrade language; the 10-Q Q3 page:53 mentions ratings only as an investment-grade release condition for subsidiary guarantees |
| Market capitalisation | Not supplied: the context is blank; the filings give only transaction-date prices such as 6.00 per share in the April 2026 offering | Insufficient Information | 10-Q Q3 page:25 "at $6.00 per share" |

### Transaction summary and new debt issues

No acquisition, buyout or sponsor transaction is present in the sources, so the transaction row for sponsor activity is Insufficient Information and not an adverse finding. The relevant transactions are financings and portfolio actions, all completed unless stated.

In September 2025 the Trust issued zero coupon senior secured notes due 2027 with 580,155 principal at maturity, raising net proceeds of approximately 490,000. The notes accrete at 7.50% per annum, are secured by first-priority liens on the equity of subsidiaries that own 36 travel centers, and have a one-time one-year extension option (10-K FY2025 page:196: "we issued $580,155 in aggregate principal amount at maturity of zero coupon senior secured notes due 2027"). On March 6, 2026 the Issuers, special purpose bankruptcy-remote subsidiaries, issued 745,000 of Series 2026-1 net lease mortgage notes in three classes with a 5.96% weighted coupon, maturing March 2031 (10-Q Q3 page:22: "issued $745,000 in aggregate principal amount of net lease mortgage notes in three classes"). The Trust contributed 158 properties to the collateral pool and the notes are non-recourse. The proceeds and cash on hand redeemed all 700,000 of the 8.375% senior guaranteed unsecured notes due 2029 with a make whole premium of 37,128. On April 2, 2026 the Trust sold 95,833,333 common shares at 6.00 per share after the reverse split, with net proceeds of approximately 541,798, which funded the redemption of the 450,000 5.50% guaranteed notes due 2027 and, with cash on hand, the 4.95% notes due 2027 (10-Q Q3 page:48). RMR, the manager, bought 8,333,333 shares in the offering at the public price (10-Q Q3 page:29). In September 2026 the 45,000 variable funding note was repaid and terminated using existing cash (10-Q Q3 page:23).

Liquidity effect, taken from the upstream debt and liquidity handoff: principal debt fell from 5,504,809 to 4,652,322 during the nine months, cash was 40,118 and the revolver was undrawn at 650,000 at September 30, 2026, but the revolver matures June 29, 2027. The Trust says it is exploring an extension or refinancing, and no replacement is agreed. The status of that exploration is pending and without assurance.

Portfolio transactions: in the nine months to September 30, 2026 the Trust sold 32 properties for 88,159, including six hotels in Q3 for 66,100, and acquired five net lease properties for 15,105 (10-Q Q3 pages:10 and 46). After the quarter, to November 2, 2026, it sold eight hotels with 1,509 keys for 50,600 and one net lease property for 295, acquired four net lease properties for 8,314, and agreed to sell one more net lease property for 655 subject to conditions. These are subsequent events and are not folded into September 30, 2026 figures. Eight of the ten exit hotels have therefore been sold and two remain for sale, which matches the 795 keys the filing says it is marketing; the retained set of 77 hotels is the earnings base going forward.

Related-party transaction in Q3 2026: in connection with a hotel sale, Sonesta waived an 11,035 termination fee in exchange for an extension of the management agreement for the remaining Sonesta retained hotels through June 30, 2043, and the Trust recorded the fee as an impairment loss (10-Q Q3 page:16). Creditor read: a cash fee was avoided, at the price of a longer commitment to an affiliated operator.

Use of proceeds is therefore stated and verifiable: debt retirement. No debt-funded distribution, dividend recapitalisation or asset drop-down to unrestricted subsidiaries is documented in the pack.

### Timeline

| Date | Event | Category | Locator and quote |
| --- | --- | --- | --- |
| February 7, 1995 | Trust organized in Maryland | Documentary Fact | 10-Q Q3 page:7 "organized on February 7, 1995 under the laws of the State of Maryland" |
| 2025 | 112 hotels with 14,631 keys sold | Documentary Fact | 10-K FY2025 page:7 "During 2025, we sold 112 hotels with a total of 14,631 keys" |
| March 9, 2025 | Mr. Murray ceased to be Managing Trustee and chief executive officer | Documentary Fact | 10-Q Q3 page:28 "until March 9, 2025" |
| August 1, 2025 | New Sonesta management agreements for the retained hotels take effect, expiring July 31, 2040 | Documentary Fact | 10-Q Q3 page:15 "Each Sonesta Retained Hotel agreement expires on July 31, 2040" |
| September 2025 | Zero coupon senior secured notes due 2027 issued | Documentary Fact | 10-K FY2025 page:196 "we issued $580,155 in aggregate principal amount at maturity of zero coupon senior secured notes due 2027" |
| January to May 2026 | 400,000 of 4.95% notes due 2027 redeemed | Documentary Fact | 10-Q Q3 page:21 "we redeemed all $400,000 of our outstanding 4.95% senior unsecured notes due 2027" |
| March 6, 2026 | Series 2026-1 net lease mortgage notes issued | Documentary Fact | 10-Q Q3 page:22 "issued $745,000 in aggregate principal amount of net lease mortgage notes in three classes" |
| April 2, 2026 | Equity offering at 6.00 per share, net proceeds about 541,798 | Documentary Fact | 10-Q Q3 page:25 "On April 2, 2026, we issued and sold 95,833,333 common shares" |
| July 6, 2026 | 1-for-5 reverse share split effective after the close of trading | Documentary Fact | 10-Q Q3 page:24 "we effected the Reverse Share Split" |
| September 2026 | Variable funding note repaid and terminated | Documentary Fact | 10-Q Q3 page:23 "we repaid and terminated the $45,000 variable funding note" |
| October 2026 (subsequent event) | Eight Sonesta hotels sold, 1,509 keys | Documentary Fact | 10-Q Q3 page:14 "In October 2026, we sold eight Sonesta branded hotels with a total of 1,509 keys" |
| October 8, 2026 (subsequent event) | Regular distribution of 0.05 per share declared | Documentary Fact | 10-Q Q3 page:26 "On October 8, 2026, we declared a regular quarterly distribution" |

### Governance and sponsor behaviour

This is issuer-level behaviour from documented actions, not a view of individuals. Legal capacity, willingness and feasibility are kept separate.

| Behaviour | Documented action | Category | Scoring dimension | Legal capacity, willingness and feasibility |
| --- | --- | --- | --- | --- |
| Equity support | Manager bought 8,333,333 shares in the April 2026 offering; net proceeds went to debt redemption | Supportive | Sponsor and manager alignment | Willingness shown by action; feasibility limited by RMR holding about 6.4%, so support is modest relative to debt |
| Deleveraging | Principal debt fell by 852,487 in nine months, as in the upstream handoff | Supportive | Financial policy | Willingness shown; feasibility depends on continued sales |
| Distributions | Quarterly distribution held at 0.05 per share; 14,627 paid in nine months 2026 against 101,150 in FY2024 | Supportive | Shareholder distributions | Distribution restraint is a policy choice; legal capacity under the indentures is not fully tested because the indenture covenant text is not in the pack |
| Related-party hotel operator | Sonesta manages 62 hotels, about 39.9% of total historical real estate investments, and is controlled by the Chair; the legacy agreement keeps pooling and cross-default provisions until its remaining hotels are sold | Neutral or Mixed | Related-party dealings | Capacity: the Trust may terminate the retained agreements for specified events; willingness: fee waiver exchanged for a longer term; the Trust owns 34% of Sonesta, so interests partly align |
| Manager fees | Net business management fees of 19,131 in nine months 2026; no incentive fee included; benchmark index for incentive fees changed from January 1, 2026 | Neutral or Mixed | Related-party dealings | The amended benchmark could change future incentive fees; the effect is not quantified in the pack |
| Secured financing | Secured share of principal debt rose from 40.5% to 62.9%; unsecured notes were redeemed at par plus make whole premiums | Neutral or Mixed | Financial policy | Capacity: indentures cap secured debt at 40% of adjusted total assets and reported 33.9% at September 30, 2026; willingness: secured issuance used to retire unsecured notes |
| Disclosure | Quarterly indenture covenant tables, rent coverage, and a statement that hotel data is not independently verified | Supportive | Reporting transparency | Transparent on tests; the credit agreement ratios are not reported |

No Extraction-Oriented or Creditor-Adverse behaviour (dividend recapitalisation, debt-funded distribution, priming of existing notes by amendment, uptiering or non-pro-rata exchange) is documented. Evidence quality is High for these filed actions; the absence of such behaviour in the pack is not proof that the indentures forbid it.

### Conflicts and differences logged

| Topic | Span one | Span two | Effect |
| --- | --- | --- | --- |
| Collateral added for the Series 2026-1 notes | 10-K FY2025 page:198 "that had an aggregate undepreciated book value of $761,508 and leases requiring annual minimum rents of $83,837" | 10-Q Q3 page:22 "we contributed to the Issuers 158 properties with an undepreciated book value of $757,616 and required minimum rents of $85,379 as of September 30, 2026" | The two figures describe the same 158 properties at different dates (expected at pricing, and at September 30, 2026). They are logged as stated and not reconciled. Collateral value used in any coverage statement should name the date. |

Not a conflict, noted for clarity: TA is 34.2% of total historical real estate investments (10-Q Q3 page:12) and 64.5% of net lease investment (10-Q Q3 page:56), because the denominators differ.

### Credit translations

Revenue durability. Evidence: net lease rental income of 101,141 in Q3 2026 is 25.3% of revenue, and 68.2% of annualized minimum rent is TA. Risk mechanic: contractual rent is stable while the tenant pays, but one tenant, on leases with the lowest portfolio coverage, makes the rent stream effectively a single credit with a BP guaranty capped at 2,782,917. Credit implication: debt service from rent is supported but concentrated; a TA payment problem would affect more than two thirds of net lease rent, and the 2033 expiry sits one year after the 2032 notes mature. A counter: portfolio rent coverage is 2.17x on tenant-reported data.

Margin and cash-flow risk. Evidence: hotel operating expenses were 85.7% of hotel revenue in Q3 2026 and the hotel segment lost 52,142 after impairments. Risk mechanic: the Trust carries hotel cost and pays fee layers ahead of its own return, so a revenue decline cuts margin more than revenue. Credit implication: hotel cash flow is the swing factor for cover; improving RevPAR on retained hotels helps, but 74.7% of revenue still comes from hotels.

Concentration and related-party risk. Evidence: Sonesta manages 62 hotels, about 39.9% of total historical real estate investments, and is controlled by the Chair; RMR runs the Trust with no employees. Risk mechanic: fees, capital spending and sale decisions are negotiated between related parties. Credit implication: monitoring of related-party flows is a standing requirement; the Q3 fee waiver for a longer term shows the trade-offs.

Sponsor alignment. Evidence: no sponsor exists, RMR bought shares in the offering, distributions were held at a low level. Risk mechanic: manager fees are asset and return based, not leverage based. Credit implication: alignment is moderate; support is modest in size and not a commitment.

Key uncertainties. The June 29, 2027 revolver expiry, the 2027 and 2028 maturities, the TA lease profile, and missing credit agreement ratios dominate. Counter-evidence: the equity raise and 2026 redemptions reduced principal debt to 4,652,322.

### Consumer read-through

| Consumer | Readiness | What to take from this module | Why it matters | Gap and action |
| --- | --- | --- | --- | --- |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Tenant and manager concentration, related-party structure, secured-share shift, strategy and timeline rows | Business risk side of the credit view | Carry unverified manager and tenant data limits; do not assert sponsor support beyond the documented actions |
| CP-5 (evidence trace) | READY_WITH_LIMITATIONS | Located quotes in every row; the logged collateral difference | Trace of business claims to filing text | Test that the 68.2%, 74.7% and secured-share figures resolve to the cited filings and the upstream debt table |

## Calculations

Inputs are USD thousands as printed; locators are page chunks.

- Hotel share of Q3 2026 revenue = 298,379 / 399,520 = 74.7% (10-Q Q3 page:3). Net lease share = 101,141 / 399,520 = 25.3%. Nine months 2026: 883,025 / 1,184,945 = 74.5%.
- Hotel operating expense ratio, Q3 2026 = 255,780 / 298,379 = 85.7%; Q3 2025 = 328,358 / 377,576 = 87.0%. Nine months 2026 = 763,078 / 883,025 = 86.4%; nine months 2025 = 963,111 / 1,116,944 = 86.2%.
- Hotel revenue less hotel operating expenses, Q3 2026 = 298,379 - 255,780 = 42,599; Q3 2025 = 377,576 - 328,358 = 49,218. Net lease rental income less net lease operating expenses, Q3 2026 = 101,141 - 6,389 = 94,752; Q3 2025 = 101,194 - 5,236 = 95,958 (10-Q Q3 page:3).
- TA share of annualized minimum rent = 269,547 / 395,492 = 68.2%, equal to the printed 68.2% (10-Q Q3 pages:56 and 12). TA rental income in Q3 2026 of 67,834 over total rental income of 101,141 = 67.1% (10-Q Q3 pages:12 and 3).
- Secured share of principal debt at December 31, 2025 = (1,580,155 senior secured + 604,654 mortgage + 45,000 variable funding note) / 5,504,809 = 2,229,809 / 5,504,809 = 40.5% (the revolver was undrawn). At September 30, 2026 = (1,580,155 + 1,347,167) / 4,652,322 = 2,927,322 / 4,652,322 = 62.9% (principal figures from the upstream debt table).
- RMR purchase in the offering = 8,333,333 shares at 6.00 = 49,999,998 US dollars, about 50.0 million; as a share of the offering = 8,333,333 / 95,833,333 = 8.7% (10-Q Q3 pages:29 and 25).
- Annual fixed coupon retired by the 2026 redemptions (illustrative, before amortisation) = 400,000 x 4.95% = 19,800; 450,000 x 5.50% = 24,750; 700,000 x 8.375% = 58,625; total 103,175. Annual interest on the new Series 2026-1 notes at September 30, 2026 is 44,341 (10-Q Q3 page:62). Net reduction in annual fixed coupon from these items = 103,175 - 44,341 = 58,834. This ignores the zero coupon notes' non-cash accretion and the variable funding note.
- Sonesta returns to the Trust, nine months 2026 = 86,046 against 120,896 in 2025; change = (86,046 - 120,896) / 120,896 = -28.8%, reflecting fewer Sonesta hotels (10-Q Q3 page:16).
- Exit hotels: 10 at September 30, 2026 with 2,304 rooms; eight sold in October 2026 with 1,509 keys leaves 2 hotels and 2,304 - 1,509 = 795 keys, equal to the 795 keys the filing says are being marketed (10-Q Q3 pages:60, 46). Retained hotels = 87 - 10 = 77, equal to the printed retained total of 77.
- Distributions: FY2024 101,150 and FY2025 6,683 (10-K FY2025 page:173); nine months 2026 14,627 (10-Q Q3 page:5).

## Gaps

| Gap | Severity | Effect | Remediation |
| --- | --- | --- | --- |
| No investor presentation or earnings release content in the pack; the three EX-99.1 files are announcements only. | Medium | Management narrative, guidance and any pro forma retained-hotel earnings are unavailable. | Obtain the November 2026 presentation if management claims are wanted. |
| Tenant financial statements for TravelCenters of America and BP guaranty terms beyond the cap are not in the pack; rent coverage is tenant-reported and unaudited. | High | The largest rent source cannot be independently tested. | Obtain the guaranty agreement and TA financials. |
| Ownership above two disclosed holders near 6% is not in the pack (proxy statement not supplied). | Low | Control and activist analysis is limited. | Obtain the proxy statement. |
| No credit ratings or market capitalisation; the context is blank. | Low | No agency view or market cross-check. | Supply if wanted. |
| Collateral and guarantors of the 8.625% secured notes due 2031 and the maturity month of the 2027 zero coupon notes are not stated in the pages read (as in the upstream handoff). | Medium | Ranking and 2027 timing remain uncertain. | Obtain indentures. |
| Covenant certificates and credit agreement ratios (fixed charge coverage, debt yield) are not reported against; no add-back bridge exists because the company reports no EBITDA. | High | Monitoring package for the revolver is incomplete. | Obtain the credit agreement and compliance reports. |
| Effect of the January 1, 2026 change in the incentive fee benchmark is not quantified. | Low | Future manager fees uncertain. | Monitor the next incentive fee determination, payable January 2027 if any. |
| Hotel statistics are manager-reported and the company states it has not independently verified them. | Medium | KPI reliability. | Cross-check to audited hotel revenue. |

## Next module

Proceed to CP-2 (fundamental credit synthesis) and then CP-5 (evidence trace). CP-2 should use the rows above for business risk and the CP-1 handoff for financial risk and liquidity, carry the limits stated in both handoffs (core EBITDA is an analyst proxy that includes sold hotels, the revolver expires June 29, 2027 with unreported covenant headroom, tenant data unverified), and state no recovery outcome or instrument recommendation. CP-5 should trace the 68.2%, 74.7%, 62.9% and 40.5% figures and the logged collateral difference back to the filings.
