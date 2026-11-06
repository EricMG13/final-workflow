# CP-1A business, ownership and transaction context: CHS INC (chscp)

## Request

CHS INC (issuer id chscp), the consolidated agricultural cooperative CHS Inc., as of 2026-11-05, credit_snapshot pathway. This module builds the fact pack a credit committee reads first: the company and its operating model, ownership and governance behaviour, the transactions and financing events of the period, and the points where the sources disagree. Currency is USD; the period is fiscal 2026 (year ended 2026-08-31) with fiscal 2025 comparatives. Figures come from the pinned sources or, where marked, from the CP-1 handoff. No sponsor, acquirer or financing transaction is on the table: the context lists no deal terms, and the sources describe none.

## Sources

### Issuer sources relied on

| Source name | sha256 | Used for |
| --- | --- | --- |
| 10-K_2026-08-31_chscp-20260831.htm.jsonl | 7af90f68bff1cc427159bcc12ffc87c427ce829f2621b0c4238922f45880492c | Business description, segments, joint ventures, governance, related parties, preferred stock, patronage, Renewable Fuel Standard exposure |
| 10-Q_2025-11-30_chscp-20251130.htm.jsonl | 3b343d46b4f667e29be99b08f7d799dc25471f06dbcbf91d62c596b40053bc50 | Segment realignment effective 2025-09-01 and recast (page:6) |
| 10-Q_2026-02-28_chscp-20260228.htm.jsonl | 335ab8ab1983479e957ab5bcc688bac42f2a8847cb6800ad1d72a83671457084 | Second quarter and six-month results, used to test the seasonality table |
| 10-Q_2026-05-31_chscp-20260531.htm.jsonl | d9720f91bf0c93fa122637a031df8f3b728863173bc1b8717d0a6e377caf2082 | Term loan drawdown, nine-month results |
| EX-99.1_2026-04-08_a2qfy26earningrelease.htm.jsonl | 33496a1570da087ac1976522b03589f92cee4a9a2670952160166094e3791034 | Second quarter release (management narrative) |
| EX-99.1_2026-07-08_a3qfy26earningrelease.htm.jsonl | 9732954cd83cfd2faab08d34c8a937435e86ab588c7e99ee653b9179d1961e0c | Third quarter release (management narrative) |
| EX-99.1_2026-11-04_a4qfy26earningrelease.htm.jsonl | cae53d4e6b095242a55a168a21c6d1a5d0c45880ba1e0b3a388701114a691f44 | Fiscal 2026 release: announced projects, planned owner distributions, management narrative |

Context file sha256 7441cd131643680d7cdd1713c448cca9698ae339b2ccfb6c0e8da281781f9451 supplies dates, currency and the blank sponsor, parent and guarantor fields; it is not issuer evidence.

### Supplied handoffs

| Module | sha256 | How used |
| --- | --- | --- |
| CP-0 | c5f6c43eadd719108e1a786ea324314e25d2bbf3d44f9ea676626928c1bc9d76 | Source readiness, gaps and conflicts |
| CP-1 | 528858c503c0f2423d9c2d1493f07a702d9a9b2cff8b46977b62e66b20b29170 | Financial base: debt, liquidity, derived EBITDA, quarterly view, claims outside debt |

Locators read `file page:N`: "10-K" is the fiscal 2026 annual report, "10-Q Q2" and "10-Q Q3" the quarterly reports for the quarters ended 2026-02-28 and 2026-05-31, "Release FY" the 2026-11-04 release. N is the extracted page chunk, not the printed page. Fact categories are Documentary Fact (the source states it), Management Language (management characterisation, quoted and not adopted), Analyst Interpretation (our reading of cited evidence) and Insufficient Information (the evidence is missing).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| CHS is a farmer-owned cooperative with no sponsor and no pending debt transaction. Its earnings are exposed to refining spreads, fuel-credit costs and one nitrogen venture, and owner distributions are board-discretionary. | Medium | Legal documents, restricted payment capacity and guarantor structure are not supplied, and two sections of the annual report disagree on fourth-quarter earnings. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Energy earnings depend on crack spreads, crude discounts and Renewable Fuel Standard costs, with a small refinery exemption benefit of approximately 205.0 million in fiscal 2026. | Earnings quality in the best year includes a regulatory benefit that is not assured to recur. | High |
| The CF Nitrogen venture produced 406,334 of equity income and 447.3 million of cash distributions in fiscal 2026. | Cash support is concentrated in one non-controlled venture whose results follow nitrogen prices. | High |
| Cash patronage and equity redemptions are decided by the board; cash patronage paid fell from 300,358 in fiscal 2025 to 30,000 in fiscal 2026 (USD thousands). | Owner distributions can be reduced in stress, which supports debt service, but the board decides. | High |
| A director's farm owed 10,260,441 past due at year end, under terms the Audit Committee approved. | Related-party credit exposure is small and disclosed, but shows member-patron overlap in governance. | Medium |
| The annual report's quarterly earnings table shows fourth-quarter pretax income at 36% of the year, while the audited year and the nine-month report imply a much larger share. | Quarterly seasonality cannot be relied on from that table; annual figures stand. | High |

### Business and transaction view

CHS is a member-owned cooperative with no sponsor, no common stock and no pending acquisition, sponsor transaction or new debt issue, so the creditor questions are operating durability and distribution discipline rather than transaction risk. Its three reportable segments are Energy, Grains and Agronomy, with a financing and hedging arm and two minority joint ventures in Corporate and Services; the realignment to a product-line model took effect on 2025-09-01 and recast prior periods. Fiscal 2026 earnings leaned on three things the sources identify: strong refining spreads in Energy, partly cancelled by record renewable fuel compliance costs and helped by a small refinery exemption; oilseed crush and ethanol margins in Grains; and CF Nitrogen in Agronomy, a 7.86% interest that is the largest single source of equity income and sits in a venture CHS does not control. Against that, owner distributions are discretionary, the board cut cash patronage sharply in fiscal 2026 and has authorized an increase for fiscal 2027, and the preferred stock carries no vote. The company announced two large projects, a phosphate joint venture and a soybean plant, both pending approvals and not expected to operate before late 2028; their funding is not described. What the sources do not give is the legal layer: restricted payment capacity, covenant levels, guarantors and ranking. The annual report also contains a seasonality table whose fiscal 2026 fourth quarter share of pretax income (36%) and second quarter share (positive 15%) cannot be reconciled to the filed quarterly statements, which weakens any quarterly trend reading until resolved.

### Company and operating model

| Area | Fact | Category | Source |
| --- | --- | --- | --- |
| Core activity | "leading integrated agricultural cooperative, providing grain, food, agronomy and energy resources to businesses and consumers on a global basis" | Management Language | 10-K page:3 |
| Ownership of the business | "we are owned by farmers, ranchers and member cooperatives" | Documentary Fact | 10-K page:3 |
| Segments | Energy, Grains and Agronomy are the reportable segments; Corporate and Services holds financing, hedging, transportation and the Ventura Foods and Ardent Mills investments (10-K page:179) | Documentary Fact | 10-K page:4, page:179 |
| Energy: refining | Two refineries, Laurel, Montana (approximately 70,000 barrels per day capacity) and McPherson, Kansas (approximately 120,000); "Our Laurel refinery sources approximately 94% of its crude oil supply from Canada" | Documentary Fact | 10-K page:5, page:6 |
| Energy: throughput | "Total refinery throughput volumes 195,415 174,837" barrels per day for fiscal 2026 and fiscal 2025; fiscal 2025 was lower because of a planned shutdown at McPherson | Documentary Fact | 10-K page:63 |
| Energy: customers | "Cenex® branded retail stores in more than 1,000 communities"; "Approximately 75% of our refined fuel products are branded under our Cenex® brand" | Documentary Fact | 10-K page:5, page:6 |
| Energy: margin drivers | "Crack spreads and WCS crude oil discounts both increased in fiscal 2026"; Group 3 2:1:1 crack spread $35.15 per barrel in fiscal 2026 against $19.91 | Documentary Fact | 10-K page:64 |
| Energy: fuel credits | "we cannot generate enough RINs to meet the needs of our refining capacity; therefore, RINs must be purchased on the open market" | Documentary Fact | 10-K page:64 |
| Energy: regulation | "The new RVO represents the highest blending obligation ever issued by the EPA." | Documentary Fact | 10-K page:63 |
| Energy: exemption benefit | "Energy segment margin benefits of approximately $205.0 million in fiscal 2026 and $90.0 million in fiscal 2025"; "These benefits only partially offset our total RVO compliance obligation costs." | Documentary Fact | 10-K page:64 |
| Energy: exemption outlook | "We may be eligible for exemptions for compliance years 2026 and beyond"; eligibility depends on throughput and the EPA's evaluation | Documentary Fact | 10-K page:64 |
| Grains: position | "largest cooperative marketer of grain and oilseed based on volumes sold" | Management Language | 10-K page:9 |
| Grains: processing | Oilseed facilities crush "approximately 153 million bushels of soybeans and canola" a year and renewable fuels plants make 267 million gallons of ethanol a year | Documentary Fact | 10-K page:9 |
| Agronomy | Wholesale and retail crop nutrients, crop protection and seed; "approximate 7.86% membership interest, based on product tons, in CF Nitrogen" with a supply agreement "through calendar year 2097" | Documentary Fact | 10-K page:12 |
| CF Nitrogen earnings | "Earnings attributable to CHS Inc. 406,334 294,944 275,531" for fiscal 2026, 2025 and 2024 (USD thousands) | Documentary Fact | 10-K page:159 |
| CF Nitrogen cash | "We received cash distributions from CF Nitrogen for the years ended August 31, 2026, 2025 and 2024, in the amounts of $447.3 million, $304.4 million and $308.4 million, respectively." | Documentary Fact | 10-K page:158 |
| CF Nitrogen forward | "cash distributions are expected to exceed our share of CF Nitrogen earnings by approximately $35 million annually" | Management Language | 10-K page:158 |
| CF Nitrogen customers | "CF Nitrogen has three customers, which are CHS and two consolidated subsidiaries of CF Industries." | Documentary Fact | 10-K page:13 |
| Other joint ventures | "Ventura Foods is a joint venture between CHS and Mitsui & Co., Ltd., with each company owning a 50% interest"; Ardent Mills, 12% interest, "the largest flour miller in the United States" | Documentary Fact | 10-K page:15 |
| Financing arm | CHS Capital provides loans to member cooperatives and producers; its notes receivable grew by 332,609 in fiscal 2026 (CP-1) | Documentary Fact | 10-K page:15, page:146; CP-1 |
| Employees | "we had 10,422 full-time, part-time, temporary and seasonal employees" | Documentary Fact | 10-K page:16 |
| Seasonality | "Our revenues and IBIT generally trend lower during the second fiscal quarter and increase in the third fiscal quarter." | Documentary Fact | 10-K page:179 |
| Margin and cash conversion | Operating earnings are a small share of revenue; equity income and other income supply much of pretax income; free cash flow swings with working capital (CP-1 C3, C5) | Analyst Interpretation | CP-1 |
| Property-level, plant-level or customer concentration beyond CF Nitrogen | Not disclosed in the sources | Insufficient Information | Missing: customer concentration and segment cost structure limit a view of margin resilience |

### Company profile

| Item | Value | Category | Source |
| --- | --- | --- | --- |
| Legal name | CHS Inc. | Documentary Fact | 10-K page:1 |
| Entity type | "CHS is a nonexempt agricultural cooperative" | Documentary Fact | 10-K page:166 |
| Incorporation and headquarters | Minnesota; Inver Grove Heights, Minnesota | Documentary Fact | 10-K page:1 |
| Origins | "Our origins date back to the late 1920s with the founding of our predecessor companies, which became Cenex, Inc., and Harvest States Cooperatives." and "CHS Inc. emerged as the result of the merger of Cenex and Harvest States Cooperatives in 1998" | Documentary Fact | 10-K page:4 |
| Listed securities | Five series of cumulative redeemable preferred stock on Nasdaq: CHSCP, CHSCO, CHSCN, CHSCM, CHSCL; the registrant has no common stock outstanding | Documentary Fact | 10-K page:1, page:2 |
| Sector and country | Agricultural cooperative, grain, food, agronomy and energy; United States | Analyst Interpretation | 10-K page:3 |
| Fiscal year end | August 31 | Documentary Fact | 10-K page:1 |
| Auditor | PricewaterhouseCoopers LLP, Minneapolis, auditor since 1998 | Documentary Fact | 10-K page:144 |
| Filer status | Non-accelerated filer | Documentary Fact | 10-K page:1 |
| Reporting basis | U.S. GAAP, consolidated, USD thousands in the statements | Documentary Fact | 10-K page:144 |
| Sponsor, parent, guarantors, borrower entity | Context fields blank; the sources name no sponsor or parent, and the debt note names no guarantors | Insufficient Information | Missing: guarantor and borrower detail needs the debt agreements |
| Ratings | None in context or sources | Insufficient Information | Missing: no rating view possible |

### Transaction summary and new debt issues

No acquisition, sponsor transaction, merger or change of control is described in the sources, and the context lists no deal terms, so there is no transaction to summarize beyond the financing and project events below, each dated and classed by status. In fiscal 2026 the company issued no new notes: the debt table shows only the scheduled repayment of an 80,000 note and the sources state that "We repaid approximately $80.6 million and $331.6 million, respectively, of long-term debt consisting of scheduled debt maturities" for fiscal 2026 and fiscal 2025 (10-K page:164). The one new long-term borrowing was the drawing of the revolving term loan: in the third quarter report the company states "we drew $300.0 million on our revolving term loan facility (the "Facility") for long-term capital planning purposes and utilized the proceeds to reduce short-term amounts outstanding" (10-Q Q3 page:13). That facility is fully drawn, its revolving period ends 2026-10-29 and it then becomes a nonrevolving term loan payable 2029-10-29 (10-K page:165); the scheduled reversion is a subsequent event after the fiscal year end that no later document confirms. On 2026-08-26 the securitization and repurchase facilities were extended to 2027-08-25 (10-K page:164). These are completed events, not proposals. Two announced projects are proposed and conditional: a phosphate production facility of nearly 450 million in Louisiana in a joint venture with OCP North America, and a soybean processing facility of approximately 700 million in Evansville, Wisconsin, with the release stating "Pending project-related approvals, both facilities are expected to be operational in late 2028 or 2029." (Release FY page:2). The 10-K expects fiscal 2027 capital expenditures of approximately 850.8 million including the Evansville plant, and development costs for the phosphate venture, with no financing plan stated (10-K page:76). The company also exited the Producer Ag joint venture on 2025-12-31 for working capital and cash, with no effect on the statement of operations (10-K page:159). The amount of the Producer Ag consideration is not supplied. Use of proceeds, sources and uses, and any new debt issue beyond the term loan are Not supplied because none is described.

### Ownership and governance behaviour

Assessment is of issuer-level behaviour from documented actions, not individuals. Legal capacity, willingness and feasibility are kept separate.

| Behaviour | Documented action | Category | Legal capacity, willingness, feasibility | Evidence quality |
| --- | --- | --- | --- | --- |
| Control | "Voting rights, including those in regard to director elections, arise by virtue of membership in CHS, not because of ownership of any equity or debt instruments" (10-K page:91); the board has 17 members with one seat vacant (10-K page:125) | Documentary Fact | Capacity: member-elected farmer directors control; preferred holders and creditors have no vote. Willingness and feasibility not applicable | High |
| Ownership concentration | "there is no person or group who is a beneficial owner of more than 5% of any class or series of our preferred stock" | Documentary Fact | No controlling holder of the listed preferred | High |
| Owner distributions | "The cash portion of the qualified patronage distribution, if any, is determined annually by the Board of Directors" and "Redemptions of outstanding equity are at the discretion of the Board of Directors." (10-K page:169, page:170). Cash patronage paid fell from 300,358 in fiscal 2025 to 30,000 in fiscal 2026 (CP-1) | Neutral or Mixed | Capacity: distributions are discretionary, restricted payment limits are Not supplied. Willingness: cut in fiscal 2026, raised for fiscal 2027. Feasibility: fiscal 2026 free cash flow after major maintenance of 1,052,492 (CP-1) exceeds the planned 300 million distribution, before the higher fiscal 2027 capital expenditure | High |
| Distributions against free cash flow | Owner and preferred distributions of 890,605, 756,709 and 299,101 in fiscal 2024, 2025 and 2026 against free cash flow after major maintenance of 441,369, negative 364,168 and 1,052,492 (CP-1 C3, D1) | Neutral or Mixed | In fiscal 2024 and fiscal 2025 distributions exceeded free cash flow; cash and short-term borrowing absorbed the difference (cash fell from 794,865 to 327,826 between fiscal 2024 and fiscal 2025) | High |
| Retention of earnings | "35% of the earnings from patronage business for fiscal 2026 and 2025, and 10% for fiscal 2024, be added to our capital reserves" | Supportive | The retained share was 10% for fiscal 2024 and 35% for fiscal 2025 and 2026 | High |
| Debt reduction | Total debt fell from 2,988,290 to 2,501,725 between fiscal 2025 and fiscal 2026 while no new notes were issued (CP-1 C5) | Supportive | Notes payable fell by 703,455 while long-term debt including current portion rose by 216,890 (D6), so the reduction is entirely short-term borrowing at its seasonal low (CP-1 C14) | Medium |
| Related-party dealings | "had $10,260,441 of accounts payable outstanding beyond the applicable payment dates and owing to CHS as of August 31, 2026"; repayment terms approved by the Audit Committee; "full payoff is due by June 30, 2027" (10-K page:124). The director notified resignation on 2026-10-02, effective 2026-12-02 (10-K page:85) | Neutral or Mixed | Disclosed and approved through a committee; amount small relative to the balance sheet; resolution pending | High |
| Preferred dividends | Preferred dividends of 168,668 paid in each of fiscal 2024, 2025 and 2026 (CP-1) | Supportive | Cumulative dividends were kept current in every year, including fiscal 2025 when free cash flow was negative | High |
| Creditor-adverse transactions | No priming, uptiering, drop-down, non-pro-rata exchange or collateral release is described in any source | Insufficient Information | Absence in these sources is not evidence of absence: the agreements that would show permissions are Not supplied | Insufficient |

### Timeline

| Date | Event | Category | Source |
| --- | --- | --- | --- |
| Late 1920s; 1998 | Predecessor companies founded; Cenex and Harvest States Cooperatives merge | Documentary Fact | 10-K page:4 |
| 2014-03-11 | Series 2 preferred stock issued (CHSCN) | Documentary Fact | 10-K page:170 |
| Fiscal 2025 | Business acquisitions, net of cash acquired, of 237,174; target and terms Not supplied | Documentary Fact (amount only, CP-1 source) | 10-K page:146 |
| 2025-09-01 | Segment realignment to a product-line operating model; prior periods recast | Documentary Fact | 10-Q Q1 page:6 |
| 2025-10-10 | Announced intent with Mid-Kansas Cooperative to end the Producer Ag joint venture | Documentary Fact | 10-K page:159 |
| 2025-12-31 | Producer Ag exit finalized | Documentary Fact | 10-K page:159 |
| March 2026 | EPA final renewable volume obligation for 2026 and 2027, "the highest blending obligation ever issued" | Documentary Fact | 10-K page:63 |
| Fourth quarter fiscal 2026 | Small refinery exemption granted in full for compliance year 2025 | Documentary Fact | 10-K page:64 |
| 2026-08-26 | Securitization and repurchase facilities extended to 2027-08-25 | Documentary Fact | 10-K page:164 |
| 2026-08-31 | Fiscal year end | Documentary Fact | 10-K page:1 |
| 2026-10-02 | Director's notice of resignation, effective 2026-12-02 | Subsequent event | 10-K page:85 |
| 2026-10-29 | Revolving term loan period ends and balance reverts to a nonrevolving term loan payable 2029-10-29 | Subsequent event, scheduled | 10-K page:165 |
| 2026-11-04 | Fiscal 2026 results and annual report; intent to distribute 300 million to owners in fiscal 2027 | Subsequent event | Release FY page:1 |
| Late 2028 or 2029 | Expected operation of the phosphate and soybean facilities, pending approvals | Subsequent event, forward-looking | Release FY page:2 |

### Capital allocation and disclosure

Management states its capital allocation priorities as "paying interest on debt and preferred stock dividends, returning cash to our member-owners in the form of cash patronage and equity redemptions" alongside safety, compliance and strategic opportunities (10-K page:74). Mechanically, the listed order places interest and preferred dividends first and owner returns after, but the order is a management statement and no contractual priority is supplied. The fiscal 2027 plan raises owner cash returns while capital expenditures are expected to rise to approximately 850.8 million from 463.3 million (10-K page:76), so fiscal 2027 cash demands combine growth capital, 168.7 million of preferred dividends, the owner distributions and 58,562 of scheduled debt maturities (CP-1), against a fiscal 2026 operating cash flow of 1,584,009 that CP-1 shows was swollen by working capital timing. No acquisition appetite is inferred from the single phosphate and soybean announcements. What the source set lacks for monitoring is logged in the gaps with severity.

### Conflicts

| Item | Statement A | Statement B | Downstream effect |
| --- | --- | --- | --- |
| Quarterly share of fiscal 2026 pretax income | 10-K MD&A seasonality table: "Q4 36 % 30 % 8 % 24 %" and "Q2 15 % (14) % 17 % 6 %" for fiscal 2026, 2025, 2024 and the three-year average (10-K page:60) | 10-Q Q2 reports a second quarter pretax loss of 164,977 (10-Q Q2 page:5) and the 10-Q Q3 reports nine-month pretax income of 389,424 (10-Q Q3 page:5) against the audited year of 1,128,719 (10-K page:144), implying a fourth quarter of 739,295 (CP-1 C9). The same table's fiscal 2026 first and third quarter shares, 24% and 25%, match the filed statements and so does its fiscal 2025 column. The fiscal 2026 second quarter share is printed as positive 15% against a loss of about 15% in the statements (possibly a missing parenthesis), and the fourth quarter as 36% against 66% (D2) | The fourth quarter share, and the sign of the second quarter share, cannot be reconciled with the filed statements; logged, not reconciled. The filed statements and audited year control. Any reading of quarterly seasonality or of Q4 strength must state the conflict |
| Fiscal 2027 equity redemptions | Release FY: "Company Intends to Return $300 Million Cash to Owners in 2027" (Release FY page:1), described as 150 million cash patronage and up to 150 million redemptions | 10-K Note 12 authorizes 150.0 million of fiscal 2026 redemptions plus an additional 15.0 million for fiscal 2025, both distributed in fiscal 2027 (10-K page:170) | Carried from CP-0 and CP-1: the filing controls; the release headline understates by the additional 15.0 million |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Conflict that counters it |
| --- | --- | --- | --- | --- |
| Margin and cash-flow risk in Energy | Crack spreads of $35.15 against $19.91 per barrel and wider crude discounts; refinery throughput of 195,415 against 174,837 barrels per day; exemption benefits of approximately 205.0 million; renewable fuel costs described as record-high | Refining earnings move with crack spreads and crude differentials, and the fuel credit bill (RINs bought on the open market, a rising blending obligation) takes a large share of the margin; a one-off exemption inflates the best year and may not recur or may be clawed back through reallocation | Energy delivered the whole of the fiscal 2026 earnings improvement (CP-1 C16), so debt service capacity and leverage tolerance depend on spreads and regulatory outcomes that management does not control; monitoring posture should track crack spreads, RIN prices and exemption decisions | The seasonality table conflict limits any quarterly read of how the Energy recovery phased |
| Concentration in one non-controlled venture | CF Nitrogen equity income of 406,334 within total equity income of 569,231 (CP-1) and cash distributions of 447.3 million; three customers, one of them CHS | Upstream cash depends on distributions set under the venture's LLC agreement and on urea and UAN prices; CHS does not control the venture and its debt service is not a claim on the venture's assets | Equity income and distributions support coverage, but they are not controlled cash flows; a nitrogen price fall would reduce earnings and the distribution that supports the owners' and preferred payments | None logged |
| Distribution flexibility | Board discretion over cash patronage and redemptions; cash patronage cut from 300,358 to 30,000; retention of 35% of patronage earnings | The largest discretionary outflow can be cut without a default event, and equity certificates are redeemed only at board discretion | Distribution flexibility is a liquidity buffer for debt service in a downturn, subject to member relations and the board's choices | The fiscal 2027 plan raises distributions while capital expenditures rise |
| Sponsor and control alignment | No sponsor; member-elected board; preferred holders have no vote; related-party dealings customary and disclosed | Control sits with patron-members whose interests as suppliers and customers of CHS are not those of creditors; no leveraged-buyout style extraction is documented | Alignment with creditors is neutral; absence of a sponsor removes recapitalisation risk but also any sponsor support | None logged |
| Key uncertainties | Covenant levels, guarantors, restricted payments and ranking Not supplied; project funding not described | Without the agreements, permissions for distributions, priming or debt incurrence cannot be tested; unfunded growth projects add cash demand beyond fiscal 2027 | Credit conclusions on structure, covenants and ranking are not possible from these sources | The 10-K quarterly table conflict |

### Consumer readiness

| Consumer | Readiness | Take from this module | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 credit view | Ready with limitations | Energy exemption and fuel-credit exposure, CF Nitrogen concentration, discretionary distributions, project cash demands, the quarterly conflict | These drive the durability of the earnings and cash that CP-1 shows | Legal documents, restricted payment capacity, guarantors, ratings, project funding not supplied | Treat structure, covenant and ranking points as Not supplied and do not read quarterly seasonality from the 10-K table |
| CP-5 evidence trace | Ready | The two logged conflicts with locators, the categorisation of each fact and the quotes | Allows quote and locator checks | Fiscal 2025 acquisition target and Producer Ag consideration Not supplied | Re-open the cited pages for every figure used in the final report |

### Consistency with upstream handoffs

CP-1 stated that the sources give no discrete fourth-quarter commentary and presented the derived fourth quarter of 739,295 without noting that the 10-K contains a quarterly pretax earnings table (10-K page:60) whose fiscal 2026 second and fourth quarter shares disagree with it. That omission is corrected here: the table exists, the disagreement is logged above, and CP-1's derived figures are unchanged because they follow arithmetically from the audited year and the filed nine-month statements. CP-0 recorded the redemption difference between the release and the 10-K; it is carried above. CP-0 and CP-1 noted that no covenant levels or guarantors are supplied; that stands.

## Calculations

| Id | Calculation | Inputs | Result |
| --- | --- | --- | --- |
| D1 | Owner and preferred distributions paid = preferred dividends + cash patronage + redemptions of equities (USD thousands, from CP-1 inputs at 10-K page:146) | Fiscal 2024: 168,668 + 366,012 + 355,925; fiscal 2025: 168,668 + 300,358 + 287,683; fiscal 2026: 168,668 + 30,000 + 100,433 | 890,605; 756,709; 299,101 |
| D2 | Seasonality table check: quarterly pretax share = quarter pretax income / fiscal year pretax income (USD thousands) | Fiscal 2026 year 1,128,719; Q1 272,188 gives 24%; Q2 (164,977) gives (15)%; Q3 282,213 gives 25%; Q4 739,295 gives 66%. Fiscal 2025 year 614,772; Q1 258,837 gives 42%; Q2 (84,712) gives (14)%; Q3 258,855 gives 42%; Q4 181,792 gives 30% | Fiscal 2026 Q4 (66% against the printed 36%) does not match; Q2 matches in size but not in sign (the table prints 15% with no parentheses); all other cells match |
| D3 | CF Nitrogen share of equity income = 406,334 / 569,231 | CF Nitrogen earnings attributable 406,334 (10-K page:159); total equity income 569,231 (10-K page:144) | 71% |
| D4 | Exemption benefit as a share of Energy pretax earnings = 205.0 million / 554.6 million | Benefit approximately 205.0 million (10-K page:64); Energy pretax earnings 554,590 thousand (10-K page:181) | 37%, approximate |
| D5 | Change in cash patronage paid = 300,358 - 30,000 | 10-K page:146 | Decrease of 270,358 |
| D6 | Change in borrowings between 2025-08-31 and 2026-08-31 (USD thousands) | Notes payable 1,152,457 - 449,002; long-term debt including current portion 2,052,723 - 1,835,833; total 2,988,290 - 2,501,725 | Notes payable down 703,455; long-term debt up 216,890; total down 486,565 |

The percentages in D2 to D4 are rounded to whole numbers; D4 uses an approximate benefit and is indicative only.

## Gaps

| Gap | Severity | Affected consumers | Action |
| --- | --- | --- | --- |
| Credit agreements, note purchase agreements and amendments not supplied | High | CP-2, CP-5 | Obtain agreements: they carry covenants, guarantors, security, restricted payment and debt incurrence baskets |
| Covenant certificate or covenant levels and headroom not supplied | High | CP-2 | Obtain compliance certificate or the agreement definitions |
| Debt schedule and maturity schedule: supplied in the 10-K note (CP-1), complete for long-term debt; short-term facility terms beyond the securitization and repurchase facilities Not supplied | Medium | CP-2 | Obtain terms of the uncommitted bilateral facilities |
| Add-back bridge or EBITDA reconciliation not supplied; the company reports none | Medium | CP-2 | Obtain management bridge or lender EBITDA definition |
| Conflict in the 10-K seasonality table (fiscal 2026 fourth quarter share and second quarter sign) unresolved | Medium | CP-2, CP-5 | Ask the issuer or check the next filing; use filed statements meanwhile |
| Funding plan and approvals for the phosphate and soybean projects not supplied | Medium | CP-2 | Obtain project financing detail |
| Fiscal 2025 acquisition target and terms, and Producer Ag exit consideration, not supplied | Low | CP-2 | Obtain from the fiscal 2025 annual report or filings |
| Customer concentration beyond CF Nitrogen not disclosed | Low | CP-2 | Obtain from issuer if material |
| Ratings, market prices and peers not supplied | Medium | CP-2 | Out of scope for this module |
| Currency and unit: the statements are USD thousands and the narrative USD millions; no other currency is reported | Low | CP-5 | Carry units with each figure |

## Next module

Proceed to CP-2 with these carried items: Energy margin and fuel-credit exposure including the approximately 205.0 million exemption benefit; CF Nitrogen concentration and distributions; the discretionary distribution lever and the fiscal 2027 plan, with the filing figure for redemptions; the pending, unfunded projects; the unresolved seasonality table conflict; and the absence of the legal layer. CP-5 should trace every figure and quote used in CP-2 to the pages cited here and re-check the conflicts table.
