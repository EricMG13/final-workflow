# CP-2 — Fundamental credit synthesis: Bally's Corp (baly)

## Request

Bally's Corp (the filings name "Bally’s Corporation"), as of 2026-11-05, pathway `credit_snapshot`, reporting currency USD. This module synthesises the fundamental credit view from the financial base (CP-1) and the business and transaction fact pack (CP-1A), with the readiness limits of CP-0. It gives no peer ranking, no instrument recommendation and no recovery conclusion.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_baly-20251231.htm.jsonl | 2416bb6463c147a405baaa3764d6b99dd0f04403aa6bd66a1af2136569a6e954 | FY2025 annual report; opened only to confirm upstream locators |
| 10-Q_2025-09-30_baly-20250930.htm.jsonl | 56bb4ccb0d42545489eded0e33ef5cc1b6e43986515a8c8a0964234c0c5a1ad2 | Not cited in this module |
| 10-Q_2026-03-31_baly-20260331.htm.jsonl | 4cf63f6c58a65fd25da3815352379f245d409f7447d9868c7381e2ae8ff65e16 | Not cited in this module |
| 10-Q_2026-06-30_baly-20260630.htm.jsonl | 972ae065bf1c6675d8214b94858dd8284ab57f02cd1acc546c671e0cb75a811b | Latest periodic report; adjusted EBITDA reconciliation (page:48), going concern and waiver (page:11, page:38), revolver (page:33) |
| EX-99.1_2026-03-16_ex991q42025earningsrelease.htm.jsonl | 409058f48783e9f5b7a8a00d5cc7ac8351ce41c9bc84bcf81e7c679d11a21bfd | Not cited in this module |
| EX-99.1_2026-05-18_ex991q12026earningsrelease.htm.jsonl | 7a189d9a918a76f21f04890e1c9f027b4cb34b6b08652098f8604b464b20f405 | Not cited in this module |
| EX-99.1_2026-08-14_ex991q22026earningsrelease.htm.jsonl | d7b82a85199a3932febed54513d2e10fb96188bb07713475fd80698b0568c17c | Not cited in this module |
| context | 49e5852827798fdbde43be3fcd478e45f6e9875c774c07cb1f9810d5a929f053 | Run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 |
| --- | --- |
| CP-0 | e78906951f2c40cb4061b9e3feea4b5ce91ea92011923fb2276960d5a3adc0a6 |
| CP-1 | b0d407b2a44a391d85b9c2d55e319b7bcd4286ee61c05f22cd3ec3d9834794e8 |
| CP-1A | 1386e40b2e065e18f9281c455fe4927011fc9b3e45afc363833febc4176b895b |

Figures come from CP-1 and CP-1A unless a locator to the Q2 2026 10-Q is given. Brackets name the upstream section or the pinned page (`page:N` is the pinned chunk, not the printed page).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Bally's is a weak, stressed credit: debt is 9.57x Adjusted EBITDA, Adjusted EBITDA covers cash interest 1.15x, and the latest filing states substantial doubt about going concern. The outcome turns on unfinished financings and sponsor action. | Medium | Covenant definitions, waiver terms and all events after August 14, 2026 are not supplied, so headroom and the October 2026 revolver reduction cannot be tested. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Gross debt was USD 4,910.1 million, 9.57x last-twelve-month Adjusted EBITDA of USD 512.8 million; net leverage was 8.81x. | Repayment depends on refinancing or asset sales, because earnings after cash interest leave little to reduce debt. | Medium |
| Cash interest took 86.7% of Adjusted EBITDA, and earnings cover cash interest plus rent only 1.10x. | Little is left for capital spending or principal, so cash falls whenever operations or projects run ahead of earnings. | Medium |
| Cash and reported revolver availability were USD 586.0 million at June 30, 2026, against a six-month free cash outflow of USD 359.1 million. | Runway is measured in quarters, and the October 2026 revolver reduction shortens it. | Medium |
| The revolver covenant is waived only conditionally, and management states substantial doubt about going concern. | Failure of a waiver condition would reinstate the covenant and let lenders accelerate, so default risk depends on financing execution. | High |
| Parent-group debt is USD 2,898.3 million against USD 2,011.8 million at Bally’s Intralot, which gives no guarantee. Q2 2026 earnings outside the Intralot segments were USD 37.4 million. | Parent-level leverage is likely much higher than the group ratio, and Intralot cash may not be available to the parent. | Low |

### Credit view

Bally's Corp is a weak, stressed credit whose debt exceeds what its earnings can carry without new financing. Its strongest support is a diversified, licensed operating base that produced Adjusted EBITDA of USD 512.8 million over the last twelve months to June 30, 2026, and a lender group that has granted a conditional covenant waiver. The weakest point is liquidity: debt of USD 4,910.1 million is 9.57x Adjusted EBITDA, Adjusted EBITDA covers cash interest only 1.15x, operations used cash, and the latest filing states substantial doubt about going concern. The outcome will be decided by whether asset sales, an equity sale or new debt close before the waiver conditions and the October 2026 revolver reduction bind, and by what the controlling sponsor does. Nothing after August 14, 2026 is supplied.

### Key findings

Leverage is high on every measure available and rests on a non-GAAP earnings measure. Total debt of USD 4,910.1 million is 9.57x last-twelve-month Adjusted EBITDA of USD 512.8 million, and net of unrestricted cash of USD 390.2 million it is 8.81x [CP-1 leverage chart data]. The ratio rose from 8.88x at September 30, 2025, although the intervening perimeter changes mean it is indicative rather than like-for-like [CP-1 Financial base view]. Operating lease liabilities of USD 2,392.3 million sit outside this debt figure and the fixed rent is deducted inside Adjusted EBITDA [CP-1 financials table].

Cash earnings are almost fully absorbed by financing and rent. Cash interest of USD 444.6 million is 86.7% of Adjusted EBITDA, so Adjusted EBITDA covers cash interest 1.15x. Adding the triple net rent expense of USD 210.0 million to cash interest, Adjusted EBITDAR of USD 722.8 million covers the total 1.10x. The 2026 term loans cost at least USD 105.4 million a year even at the 3.0% floor plus the lower 6.5% base-rate margin, and more under the 7.5% Term SOFR margin, and part of the interest may be paid in kind [CP-1A Transaction summary]. Operating cash flow was an outflow of USD 335.7 million over the last twelve months [CP-1 financials table].

Liquidity is the decisive issue. Cash of USD 390.2 million and reported revolver availability of USD 195.8 million total USD 586.0 million, compared with a six-month free cash outflow (operating cash flow less capital expenditures and capitalized software) of USD 359.1 million [CP-1 liquidity chart data; Q2 2026 10-Q page:5]. Revolver commitments are due to fall to about USD 319 million from October 2026 while USD 303.75 million is drawn, which leaves essentially no headroom once the reduction applies, before other usage of USD 19.75 million that CP-1 could not explain [Q2 2026 10-Q page:33]. Whether the reduction occurred, and how it was met, is Not supplied because the pack ends at August 14, 2026.

Covenant protection exists only through a conditional waiver. In May 2026 the required lenders conditionally waived the consolidated net leverage ratio covenant for each quarter from March 31, 2026 until the earlier of the company’s election or the day before the compliance certificate for the quarter ending March 31, 2027, subject to minimum liquidity, limits on additional secured debt and an agreement to amend the revolver [Q2 2026 10-Q page:38]. The company states that it does not project that it would satisfy the liquidity maintenance requirement or the reinstated covenant absent the financings under discussion, and that substantial doubt about going concern exists [Q2 2026 10-Q page:11]. The waiver level and the reported ratio are Not supplied, so headroom is Not calculable.

The structure divides the debt across two borrower groups. Parent-group debt is USD 2,898.3 million: USD 1,413.3 million of first lien revolver and 2026 term loans and USD 1,485.0 million of senior notes. Bally’s Intralot debt is USD 2,011.8 million, and Bally’s Intralot does not guarantee the parent’s debt [CP-1 debt table; CP-1A Transaction summary]. The two Intralot-linked segments produced USD 86.7 million of Q2 2026 segment Adjusted EBITDAR, leaving USD 37.4 million of Adjusted EBITDA from casinos, North America Interactive and corporate cost after rent [Q2 2026 10-Q page:48]. The mapping of segments to legal entities is not supplied, so parent-level leverage is only indicative; on this basis it is about 19.4x annualized Q2 2026 and 23.8x last twelve months.

Earnings quality is limited by add-backs and by margin pressure. Add-backs for transaction, development, merger, share-based and other items were USD 106.4 million in the six months to June 30, 2026, 43.0% of Adjusted EBITDA of USD 247.3 million [Q2 2026 10-Q page:48]. Q2 2026 revenue rose to USD 792.2 million while Adjusted EBITDA fell to USD 124.0 million from USD 129.2 million, with gaming expenses at 52% of gaming revenue against 43% a year earlier [CP-1 segment base; CP-1A operating model].

Maturities are light until 2029 but the revolver and the 2029 wall matter. Debt maturing through 2027 is USD 141.4 million, 2028 is USD 282.3 million and 2029 is USD 1,007.0 million; the USD 1,109.5 million of 2026 term loans fall due in 2029 instead of 2031 if the 2029 Notes are still outstanding then, which would lift the 2029 amount to USD 2,116.5 million [CP-1 maturities chart data]. Refinancing of the 2029 Notes is therefore linked to the secured term loan maturity.

### Strengths and weaknesses

Strength, Documentary Fact: a diversified, licensed operating base. The company runs 19 US land-based casinos, a large online gaming business and a lottery technology business, with no customer above 10% of revenue, and holds Rhode Island master contracts to 2043, a New York gaming license and a Chicago development [CP-1A Company and operating model; Company profile]. This supports revenue durability, although segment cash earnings are not evenly distributed.

Strength, Documentary Fact: lender engagement and external funding for part of the capital programme. Lenders granted a waiver and amended the revolver in 2026, and GLPI has committed to advance up to USD 940.0 million for Chicago construction, which reduces the company’s own capital need there [CP-1A Transaction summary]. Lender engagement lowers near-term acceleration risk but does not remove the conditions.

Strength, Documentary Fact: contained near-term amortisation. Remaining 2026 and 2027 maturities total USD 141.4 million, and a parent revolver default has no implications under Bally’s Intralot’s debt documents [CP-1 maturities chart data; Q2 2026 10-Q page:11]. This limits contagion from a parent-level default to the Intralot group.

Strength, Analyst Interpretation: real estate and asset monetisation capacity. The Bally’s Twin River sale-leaseback realised USD 700.0 million of consideration, and the company lists asset monetisation among its plans [CP-1A Transaction summary]. This is also a weakness because each sale adds fixed rent, so I count it only as a source of liquidity, not of lower fixed charges.

Weakness, Documentary Fact: leverage and cover. Gross leverage of 9.57x, net leverage of 8.81x and cover of 1.15x leave little cushion, and the fixed-charge cover including rent is 1.10x [CP-1 charts; calculations below].

Weakness, Documentary Fact: liquidity and going concern. Operating cash flow is negative, cash fell from USD 798.4 million at December 31, 2025 to USD 390.2 million at June 30, 2026, and the latest filing states substantial doubt [CP-1 liquidity chart data; CP-1A Company profile].

Weakness, Analyst Interpretation: structure and control. A controlling sponsor holds 67.1%, no equity support is documented, parent creditors rank behind Intralot creditors at the Intralot level, and 42.1% of Intralot equity belongs to others [CP-1A Company profile; Governance]. The sponsor’s response is the key unknown.

Weakness, Documentary Fact: reporting quality and regulation. The 10-K reports an adverse opinion on internal control because of a material weakness, results were first issued as preliminary, and the Rhode Island regulatory agreement restricts payments and debt incurrence above a 5.50 to 1.00 leverage trigger whose definition and status are not supplied [CP-1A Company profile].

Weakness, Documentary Fact: uncommitted large projects. The USD 4.0 billion Bally’s Bronx project has a non-binding loan term sheet and a letter of intent with a potential equity investor, and construction at Chicago continues [CP-1A Transaction summary]. Funding competes with debt service.

### Credit assessment

| Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- |
| Weak and stressed fundamental credit: leverage of 9.57x, cover of 1.15x, negative operating cash flow and a going concern warning; near-term outcome depends on financing execution and the waiver | Analyst Interpretation | Medium | CP-1 leverage, interest cover and liquidity chart data; CP-1A Company profile (going concern); Q2 2026 10-Q page:11 |
| Thesis: a diversified, licensed gaming business has been levered and expanded faster than its cash earnings, so creditors depend on refinancing, asset sales and sponsor action rather than on free cash flow | Analyst Interpretation | Medium | CP-1 financials; CP-1A Transaction summary |

Confidence is Medium, not High, because CP-0 and CP-1A carry open High-severity gaps (no executed agreements, nothing after August 14, 2026, perimeter and cash split between the parent group and Bally’s Intralot not supplied) and CP-1 ratios are not like-for-like across dates.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity | Basis |
| --- | --- | --- | --- | --- |
| Liquidity shortfall and waiver failure | Cash used in operations, project spend and the October 2026 revolver reduction run ahead of financing; the waiver depends on a minimum liquidity level that management does not project it will meet | Reinstated covenant, possible acceleration of the Credit Agreement and a going concern outcome | Critical | CP-1 liquidity; Q2 2026 10-Q page:11, page:38 |
| Interest and rent burden | Cash interest takes 86.7% of Adjusted EBITDA and rent adds more; the 2026 term loans cost at least 9.5% | Debt cannot be reduced from cash earnings; refinancing at similar cost would leave cover near current levels | Material | CP-1 interest cover; CP-1A Transaction summary |
| Structure and cash trapping | Intralot debt does not guarantee the parent, 42.1% of Intralot equity is minority-owned, and earnings outside the Intralot segments were about 30% of group Adjusted EBITDA in Q2 2026 | Parent creditors rely on distributions that may be restricted; parent leverage is above the group ratio | Material | CP-1 debt table; CP-1A Company profile |
| Earnings pressure | UK gaming tax increase, gaming cost ratio up to 52% of gaming revenue, and add-backs of 43.0% of six-month Adjusted EBITDA | Adjusted EBITDA may overstate recurring cash earnings | Material | CP-1A Company and operating model; Q2 2026 10-Q page:48 |
| Capital programme and sponsor behaviour | Bronx, Chicago and Las Vegas spending without committed funding; a controlling sponsor with no documented support | Capital calls compete with debt service; outcomes depend on one holder | Material | CP-1A Transaction summary and Governance |
| Regulatory and reporting | Rhode Island 5.50 to 1.00 trigger, adverse internal control opinion, preliminary results | Payment and incurrence limits may apply; reported figures carry control risk | Material | CP-1A Company profile |

## Calculations

All amounts USD. Inputs are from CP-1 or CP-1A unless a page is given.

- Cash interest share of Adjusted EBITDA: 444,640 / 512,810 = 86.7% (thousands).
- Fixed charge cover: Adjusted EBITDAR 722,846 / (cash interest 444,640 + rent expense 210,036 = 654,676) = 1.10x (thousands; CP-1 financials table). Rent is the expense line; cash rent paid in six months 2026 was 133,561 thousand (Q2 2026 release page:8).
- Liquidity: cash 390.2 + reported revolver availability 195.8 = 586.0 (USD million). Six-month free cash flow: (265,936) − 73,954 − 19,227 = (359,117) thousand, so an outflow of 359.1; ratio 359.1 / 586.0 = 61.3%. This excludes the license fee of 502.0 and the contingent payment of 115.0 paid in the period, and the sale-leaseback proceeds of 685.0 (Q2 2026 10-Q page:5).
- Revolver after the October 2026 reduction: commitments about 319 less drawn 303.75 = 15.25; less unexplained usage of 19.75 = (4.5). This is arithmetic on stated amounts, not a reported figure; drawings may have changed.
- 2026 term loan minimum cost: base-rate option 3.0% floor + 6.5% margin = 9.5%; 1,109.518 × 9.5% = 105.4 per year; Term SOFR option 3.0% + 7.5% = 10.5%, or 116.5 per year. Both are floors before any PIK election; the rate in effect is not in the pack (Q2 2026 10-Q page:34).
- 2029 maturities with springing date: 1,006.996 + 1,109.518 = 2,116.514 (CP-1 maturity chart; Q2 2026 10-Q page:32 footnote 1).
- Debt through 2027: 95.670 + 45.688 = 141.358.
- Borrower groups: parent group 303.750 + 1,109.518 + 750.000 + 735.000 = 2,898.268; Intralot group 530.277 + 228.441 + 74.243 + 148.487 + 685.323 + 342.661 + 2.368 = 2,011.800; total 4,910.068 (equals CP-1). Intralot share 41.0%.
- Segments: Intralot-linked B2B 21,931 + B2C 64,739 = 86,670 (thousands) of Q2 2026 segment Adjusted EBITDAR 187,515 (46.2%). Remainder of Adjusted EBITDA: 124,034 − 86,670 = 37,364.
- Indicative parent-level leverage: 2,898.268 / (37.364 × 4 = 149.456) = 19.4x. Last twelve months: Intralot-linked segments 361,497 (FY2025 B2B 38,489 plus B2C 323,008) + 188,878 (six months 2026) − 159,340 (six months 2025) = 391,035; remainder 512,810 − 391,035 = 121,775; 2,898.268 / 121.775 = 23.8x. Limits: segments are not legal entities, B2B includes the company’s licensing business, B2C includes a UK casino, corporate costs are not allocated by entity, and minority interests are ignored. Indicative only; Analyst Interpretation.
- First lien sensitivity (not a covenant test): first lien debt 303.750 + 1,109.518 = 1,413.268; net of consolidated cash 390.184 = 1,023.084; over consolidated LTM Adjusted EBITDA 512.810 = 2.0x; over the remainder excluding Intralot-linked segments 121.775 = 8.4x. The revolver test is 4.00 to 1.00 when utilization exceeds 25% (Q2 2026 10-Q page:65); the result swings across it depending on the EBITDA perimeter, which is why the covenant definition is a High gap.
- Add-backs, six months to June 30, 2026: transaction costs 28,568 + development costs 33,264 + share-based compensation 4,356 + merger and Intralot costs 10,953 + other 29,298 = 106,439; 106,439 / 247,318 = 43.0%. Q2 2026: 21,343 + 20,306 + 1,805 + 2,195 + 20,715 = 66,364; 66,364 / 124,034 = 53.5% (Q2 2026 10-Q page:48). The sale-leaseback gain of 105,845 is excluded from Adjusted EBITDA.

## Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Credit Agreement, Amendments No. 3 to No. 5, Conditional Waiver and 2026 Term Loan agreement not supplied; waiver level, minimum liquidity and reported ratio unknown | Headroom and the point of waiver failure cannot be tested; the first lien result swings between 2.0x and 8.4x on perimeter | Credit view, risks | High | Supply executed documents and the compliance certificate |
| Nothing after August 14, 2026, including the October 2026 revolver reduction, Fifth Amendment terms, Bronx loan, equity sale and evoke financing | The central question is whether financing closed | Credit view | High | Supply later 8-Ks and the Q3 2026 report if filed by the cutoff |
| Parent group versus Bally’s Intralot cash, earnings and intercompany restrictions; guarantor list | Parent leverage and access to Intralot cash cannot be measured | Structure risk | High | Supply guarantor schedules and entity-level accounts |
| Rhode Island regulatory leverage definition and status | Payments and incurrence may be restricted | Regulatory risk | Medium | Supply the agreement or certificate |
| Last-twelve-month ratios mix Successor and Predecessor periods and a changing perimeter | Trend in leverage is indicative | Leverage | Medium | Obtain pro forma figures |
| Sponsor intentions and any equity commitment | Decisive for outcome | Credit view | High | Supply sponsor statements or the proxy |
| Market prices, ratings and peer data | Not required for fundamental view; no relative value is given | None | Low | Keep Not supplied |

## Next module

- CP-5 should verify each cited locator and calculation in this answer, especially the borrower-group split, the indicative parent leverage, the first lien sensitivity and the add-back sums, and should carry the High gaps above as restrictions on any use of the credit view.
