## Request

Issuer: Wayfair Inc. (issuer id w), as of 2026-11-05, pathway credit_snapshot, reporting currency USD, evidence cutoff 2026-11-05. Scope: trace every material claim in the four accepted handoffs (source readiness, financial base, business and transaction context, credit synthesis) to the pinned filings, recompute the derived figures, check the handoffs against each other, and grade whether committee use is permitted, restricted or blocked. The review changes no credit conclusion and repairs no lineage silently.

## Sources

### Issuer sources used to trace claims

Each file is a JSONL text extraction of an SEC filing or exhibit; a locator `page:N` is the extraction chunk, not the printed page. The sha256 is the pinned file hash.

| Source name | sha256 | Short label | Period and kind |
| --- | --- | --- | --- |
| 10-K_2025-12-31_w-20251231.htm.jsonl | 8ef4121e11689a0c5565962f85cfafc125f39e54e08df2c3b6c79eaf68e84e4d | 10-K | FY2025 annual report, audited |
| 10-Q_2026-03-31_w-20260331.htm.jsonl | 79f74f0ba7972d92f75742a90568a879936b4ecf939af4026c967768203f5019 | Q1 10-Q | Quarter ended 2026-03-31, unaudited |
| 10-Q_2026-06-30_w-20260630.htm.jsonl | e52476a4ad53b4396b19ba631702cd30b522eb54aecabc978fa654467e46935a | Q2 10-Q | Quarter and six months ended 2026-06-30, unaudited |
| 10-Q_2026-09-30_w-20260930.htm.jsonl | 9224a05a14ec554aa7f19d7d2ae6869a07a996f1d60af972e32e1595aefdd8c3 | Q3 10-Q | Quarter and nine months ended 2026-09-30, unaudited |
| EX-99.1_2026-04-30_a2026-04x30ex991.htm.jsonl | a3debc23ce5c3027daa8862793a0e092539f933475881f34dd98f47a74a5cd40 | Q1 rel | Earnings release, Q1 2026 |
| EX-99.1_2026-08-04_a2026-08x04ex991.htm.jsonl | bd4c1a88b49b8e4441931ccafc159f4e1f6d02b8d8bf7918ce20a28d44352f87 | Q2 rel | Earnings release, Q2 2026 |
| EX-99.1_2026-11-04_a2026-11x04ex991.htm.jsonl | 2907d0c055207f89b1a08967b4ff5b2fe5bb05c815f0f3ad4e1479f1b9a353cb | Q3 rel | Earnings release, Q3 2026 |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | e3b6fe003758c2152693bc3785d916a8d51266f353efa91b71daa0110cb48520 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Role in this review |
| --- | --- | --- |
| CP-0 | 9ba2d9c1e2e60174eaacd93db71cc6938042323a45533114c80ae7273f5486a5 | Source readiness; gate input; claims about coverage and search results were re-tested |
| CP-1 | 8232ff967a14f3da33fdcbbd5e43b820265a70b6cbcc48e608407bb2c6fd17ec | Financial base; statements, debt schedule, ratios and chart data traced and recomputed |
| CP-1A | 1853762b5adae9ef3371bf0fa46be49dcaed340fc5da9c9072e41691e813cc31 | Business and transaction context; quotes, ownership and debt history traced |
| CP-2 | 23916e778d667e04e165fecfd7ca3e07c7e379472000a30367e3389b77e8d2d1 | Credit synthesis; every claim and calculation traced to CP-1 and CP-1A and then to the filings |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The figures and quotes in the four handoffs trace to the filings and recompute correctly, and the handoffs agree with each other. Committee use is restricted for covenant and legal-structure conclusions because executed documents are not supplied. | Medium | Covenant ratio, executed debt documents and ratings are not in the sources, and this review was done in the same session as the handoffs, so it is not independent. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 38 verbatim source quotes in the handoffs were found in the filings, and every derived figure recomputed to the stated value. | Statements attributed to the filings, and the numbers a committee would quote, can be relied on as worded. | High |
| Two statements are only partly supported as worded, and three page citations point to the wrong page for correct figures. | These are wording and citation issues; no figure and no direction of the credit view changes. | High |
| No contradiction between the four handoffs was found; leverage, liquidity and maturity figures are identical wherever they are repeated. | The set tells one consistent story to a committee. | High |
| Covenant ratio, indentures, guarantor list, ratings and guidance are absent and are carried as open by every handoff. | Covenant headroom, distribution capacity and ranking can only be stated as filing summaries, so committee use is restricted for those conclusions. | High |
| The review was done in the same session as the handoffs and used the same extracted text. | A separate reviewer should compare the handoffs with the original filings before external use. | High |

### Evidence trace view

The evidence trace holds. Each material claim in the source-readiness, financial-base, business-context and credit-synthesis handoffs was matched to a located source span or to a recomputation from located figures, and the four handoffs agree on every shared figure, period and perimeter label. Two statements are only partly supported as worded and three page citations point to the wrong page for a correct figure; none changes a figure or the direction of the credit view, which is cautious with Medium confidence and no higher than the upstream limits allow. The integrity verdict is Restricted for covenant, legal-structure and distribution-capacity conclusions, because the executed documents and the covenant ratio are not in the sources, and usable for screening of liquidity, maturities, earnings direction and business risk. The review is not independent of the authors.

### Evaluated set (inputs and status)

| Input | Status | Evaluated | Notes |
| --- | --- | --- | --- |
| CP-0 source readiness | Accepted; gate | Yes, for coverage claims and search results | Four consumers READY_WITH_LIMITATIONS; carries no legal documents, no covenant ratio, unnamed guarantors |
| CP-1 financial base | Accepted | Yes | USD millions, consolidated Wayfair Inc.; LTM and Q4 2025 labelled as derived |
| CP-1A business and transaction context | Accepted | Yes | Readiness judgment for the synthesis: READY_WITH_LIMITATIONS |
| CP-2 credit synthesis | Accepted | Yes | Confidence Medium, inside the cap set by the upstream limits |

All four are current for the as-of date 2026-11-05 and use USD in millions. No input is stale; the latest source is dated 2026-11-04 and nothing after the cutoff is used. Committee status: Restricted. No numeric confidence score is produced in host mode because the scoring script is not available to this session; the band is Medium.

### Top material credit drivers and traceability

| Rank | Credit driver | Originating module | Source-supported basis | Why material | Source trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Deleveraging led by earnings: total debt 2,799 at 2026-09-30 against 3,118 at 2024-12-31; LTM Adjusted EBITDA 853 against 453 in FY2024; total debt to Adjusted EBITDA 3.28x | CP-1, CP-2 | Q3 10-Q page:10-11; 10-K page:88, page:118; Q3 rel page:11 | Sets leverage tolerance | Supported by recomputation (Calculations) | Adjusted EBITDA is a management measure |
| 2 | Liquidity and maturity profile: cash 1,038, short-term investments 60, undrawn revolver 418; 229 due September 2027; secured notes from 2029 | CP-1, CP-2 | Q3 10-Q page:2, page:10-11, page:39 | Determines refinancing risk | Supported | Revolver availability not tested against covenants |
| 3 | Earnings quality: 293 of equity compensation and related taxes added back; unadjusted leverage 5.10x | CP-1, CP-2 | Q3 rel page:11; 10-K page:88, page:101 | Changes how moderate leverage looks | Supported | Covenant EBITDA definition not supplied |
| 4 | Rising fixed interest and secured claim stack: 2,600 of secured notes; run-rate coupons about 195 against LTM cash interest 170 | CP-1, CP-1A, CP-2 | Q3 10-Q page:5, page:10-11; 10-K page:121 | Sets debt service and ranking | Supported by recomputation | Indentures not supplied |
| 5 | U.S.-weighted, volume-led demand with negative working capital: U.S. 88% of FY2025 revenue; orders 11.0 million; payables 1,213 against inventories 89 | CP-1A, CP-1 | 10-K page:10; Q3 rel page:2; Q3 10-Q page:2 | Drives earnings and cash volatility | Supported | Release KPIs are management-calculated |

### Material claim register and support review

Verdicts: supported (the named evidence states the claim or the recomputation reproduces it), partly supported (carries part of it, or carries it only with a qualification the claim omits), unsupported (does not carry it).

| Claim | Module | Evidence traced | Verdict | Reviewer note |
| --- | --- | --- | --- | --- |
| Total debt carrying 2,799 and principal 2,829 at 2026-09-30; 3,272 at 2025-12-31 | CP-0, CP-1, CP-2 | Q3 10-Q page:10-11; 10-K page:118 | Supported | Carrying and principal sums recomputed |
| Revolver 500, undrawn, letters of credit 82, availability 418 | CP-0, CP-1, CP-2 | Q3 10-Q page:11, page:39 | Supported | Arithmetic only; stated as such |
| LTM Adjusted EBITDA 853 and the Q1 and Q2 2026 LTM values 788 and 825 | CP-1, CP-2 | 10-K page:88; Q1 rel page:2; Q2 rel page:12; Q3 rel page:11 | Supported | Derived and labelled |
| Leverage ratios 6.88x, 4.40x, 3.77x, 3.44x, 3.28x and net ratios 3.85x, 2.33x, 2.42x, 2.05x, 1.99x | CP-1, CP-2 | Balance sheets and debt tables, pages as in CP-1; recomputed | Supported | Carrying total debt used throughout; basis stated |
| Interest cover 7.19x, 5.35x, 4.99x, 4.63x, 5.02x and run-rate cover 4.36x | CP-1, CP-2 | 10-K page:101; Q1 10-Q page:4; Q2 10-Q page:4; Q3 10-Q page:5, page:11 | Supported | Cash interest is gross of interest income; stated |
| Equity compensation and related taxes 293 (34.3%) of Adjusted EBITDA; 46.4% in FY2025 | CP-1, CP-2 | Q3 rel page:11; 10-K page:88 | Supported | Recomputed |
| Operating income plus D&A 549 and unadjusted leverage 5.10x and 3.10x | CP-1, CP-2 | 10-K page:100-101; Q3 10-Q page:3-4 | Supported | Calculated; not a company measure; labelled |
| LTM free cash flow 476 (55.8% of Adjusted EBITDA) | CP-1, CP-2 | 10-K page:89; Q3 rel page:12 | Supported | Recomputed from operating cash flow and capital expenditure |
| Working-capital inflow 64 against outflow 76; 140 of the 174 operating cash flow increase | CP-1, CP-2 | Q3 10-Q page:4, page:44 | Supported | The filing's 140 equals the recomputed difference |
| Free cash flow excludes 77 of share-settlement tax and 60 of buybacks, which sit in financing | CP-1, CP-2 | Q3 10-Q page:4 | Supported | Direction and amounts as printed |
| Capital structure is now all fixed-rate: 2,600 of secured notes and 229 of convertible notes | CP-1 | Q3 10-Q page:11; 10-K page:119-120 | Partly supported | True of drawn debt; the 500 revolver is variable-rate (Term SOFR plus margin) though undrawn, so the wording should say drawn debt |
| Debt schedule roles: Wayfair LLC borrower and issuer; Wayfair Inc. issuer of convertibles; guarantors partly named | CP-0, CP-1, CP-1A | 10-K page:119, page:121-122, page:125, page:130; Q2 10-Q page:12 | Supported | CP-1 notes that pari passu wording is printed for the earlier series only |
| All four secured series share first-priority liens with the revolver, so the unsecured notes rank behind them | CP-2 | 10-K page:130 (2029, 2030, 2032 series); Q2 10-Q page:12 (2034 described as senior secured) | Partly supported | CP-1 states the nuance; CP-2 generalises. Effect on the credit view is nil |
| Fair values 98.9% to 102.9% of principal imply continued secured-market access | CP-2 | Q3 10-Q page:15 | Supported as labelled | Tagged Analyst Interpretation; Level 2 prices are not issuance evidence |
| Four secured issues totalling 2,600 since October 2024 | CP-1A, CP-2 | 10-K page:121; Q2 10-Q page:12 | Supported | Equals secured principal outstanding |
| Use of proceeds: 2030 notes funded repurchases of 2026 and 2025 notes; 2034 notes funded redemption of the 2028 notes; 2029 and 2032 not stated | CP-1A | 10-K page:128; Q3 10-Q page:41 | Supported | Absence left as Insufficient Information |
| Convertible notes retired at cash above principal: 375 for 210 in 2025, 247 for 145 in 2026; losses 165 and 102 | CP-1A, CP-2 | 10-K page:128; Q3 10-Q page:14 | Supported | Cash includes accrued interest and fees; stated |
| 2027 notes convertible in the quarter ending 2026-12-31; if-converted excess 141; settlement at the company's election | CP-1, CP-1A, CP-2 | Q3 10-Q page:13, page:15 | Supported | |
| Founders hold 67.4% of voting power and 18.3% of economic interest at 2025-12-31; Class B 15.3% of shares and 64.4% of votes at 2026-10-28 | CP-1A, CP-2 | 10-K page:62, page:134; Q3 10-Q page:1 | Supported | Share and vote percentages recomputed; the vote percentage is Class B in aggregate |
| U.S. 88% of FY2025 revenue; orders 11.0 million against 9.8 million; average order value 311 against 317 dollars | CP-1A, CP-2 | 10-K page:10; Q3 rel page:2 | Supported | |
| International Adjusted EBITDA loss 54 and U.S. 683 in nine months 2026 | CP-1, CP-1A, CP-2 | Q3 rel page:11 | Supported | |
| Covenant level of no more than 4.0 to 1.0; no reported ratio | CP-0, CP-1, CP-1A, CP-2 | Q3 10-Q page:42; 10-K page:53, page:120 | Supported | Search of all sources found no reported ratio |
| No priming, uptiering, drop-down, related-party or recapitalisation evidence | CP-1A, CP-2 | Search of all seven sources | Supported | Correctly worded as absence in the pack |
| Ratings, guidance, pension, factoring and supply-chain finance not found | CP-0, CP-1, CP-2 | Search of all seven sources | Supported | Searches repeated by this review with the same results |
| Operating income covers net interest expense 1.81x LTM and 0.14x in FY2025 | CP-2 | 10-K page:100; Q3 10-Q page:3 | Supported | Recomputed: 283 / 156 and 17 / 119 |
| Cash and investments cover the 2027 principal 4.8 times | CP-2 | Q3 10-Q page:2, page:10 | Supported | 1,098 / 229 |
| Small unexplained variances: settlement of long-term debt 701 against 696; 247 against 245; 694 against 696; 2027 principal 230 to 229 | CP-1 | Q2 10-Q page:4; Q3 10-Q page:4, page:14; Q1 10-Q page:9 | Supported | Verified; the sources do not explain them |
| Cautious credit view with Medium confidence | CP-2 | CP-1 and CP-1A rows above | Supported | Not above what the basis carries |

### Citation trace

| Check | Method | Result |
| --- | --- | --- |
| Verbatim quotes | Each double-quoted span in each handoff searched in the normalised text of all seven sources | 38 source quotes found in 38 (CP-0 24, CP-1 8, CP-1A 6, CP-2 none); quoted search terms in the gap notes (for example guarantor, held for sale, outlook) are not counted as quotes |
| Figures in the sources | Every comma-grouped number and decimal in CP-1, CP-1A and CP-2 searched in all source text | All present in the sources except derived figures (4 in CP-0, 63 in CP-1, 9 in CP-1A and 24 in CP-2), each located in a Calculations table or a stated formula |
| Page locators on figure-bearing lines | Each figure on a line searched on the pages named on that line | Figures sat on the cited pages except in three places (findings register) |
| Reported statement tables | Every numeric cell in the CP-1 statement, balance sheet, cash flow, reconciliation, segment and KPI tables checked on the pages cited | Matched, except the derived Q4 2025 row and the derived non-cash and working-capital subtotal lines, which are labelled derived |
| Cutoff | Dates after 2026-11-05 | Only labelled future dates (maturities in 2027 to 2034; convertibility from 2027-06-15; the 2026-12-31 convertibility quarter) |
| Currency and period labels | Each table header read | USD millions throughout; LTM, nine-month, quarter and year-end figures labelled; no nine-month amount used as a full-year figure |

### Figure identity across modules

| Figure | CP-0 | CP-1 | CP-1A | CP-2 | Result |
| --- | --- | --- | --- | --- | --- |
| Total debt carrying and principal at 2026-09-30 | 2,799; 2,829 | 2,799; 2,829 | 2,799; 2,829 | 2,799; 2,829 | Identical |
| LTM Adjusted EBITDA | Not stated | 853 | 853 | 853 | Identical |
| Total debt to Adjusted EBITDA | Not stated | 3.28x | 3.28x | 3.28x | Identical |
| Net debt to Adjusted EBITDA | Not stated | 1.99x | Not stated | 1.99x | Identical |
| Unadjusted total debt to EBITDA | Not stated | 5.10x | Not stated | 5.10x | Identical |
| Interest cover and run-rate cover | Not stated | 5.02x; 4.36x | 5.02x | 5.02x; 4.36x | Identical |
| Cash, short-term investments, undrawn revolver | 1,038; 60; 418 | 1,038; 60; 418 | 1,038 | 1,038; 60; 418 | Identical |
| Secured principal and share | Not stated | 2,600; 91.9% | 2,600; 91.9% | 2,600; 91.9% | Identical |
| Founder voting power and economic interest | Not stated | Not stated | 67.4%; 18.3% | 67.4%; 18.3% | Identical |
| 2027 notes principal and if-converted excess | 229 | 229; 141 | 229; 141 | 229; 141 | Identical |
| Equity compensation add-back | Not stated | 293 | Not stated | 293 | Identical |

### Input currency and scale

All inputs are USD in millions, as printed in every source; share counts are in units and per-share amounts in dollars, and each handoff states the unit. No scale mismatch was found, for example no value written as millions that the source prints as thousands.

### Gap propagation

| Upstream limitation | Carried by CP-0 | Carried by CP-1 | Carried by CP-1A | Carried by CP-2 |
| --- | --- | --- | --- | --- |
| Covenant ratio and EBITDA definition not supplied | Yes | Yes | Yes | Yes |
| Executed indentures, credit agreement and guarantor list not supplied | Yes | Yes | Yes | Yes |
| Ratings, market data and peers not supplied | Yes | Yes | Yes | Yes |
| Q4 2025 stand-alone quarter derived only | Yes | Yes | Not applicable | Yes |
| Revolver springing maturity trigger not printed | Yes | Yes | Covered by the executed-documents gap | Yes |
| Canada Border Services Agency matter described in the 10-K only | Yes | Yes | Yes | Yes |
| No management guidance | Not applicable | Yes | Yes | Yes |
| 2026 proxy statement and use of proceeds for two issues not supplied | Not applicable | Not applicable | Yes | Yes |

### Findings register

| Finding | Type | Severity | Modules | Effect |
| --- | --- | --- | --- | --- |
| The description of the capital structure as all fixed-rate omits that the undrawn 500 revolver is variable-rate | Partly supported claim | Minor | CP-1 | Wording; drawn debt is fixed-rate |
| The synthesis says all four secured series share first-priority liens with the revolver; the pari passu wording is printed for three series and the 2034 series is described as senior secured | Partly supported claim | Minor | CP-2 | CP-1 states the nuance; no effect on the view |
| The chart basis cells in the financial base cite the debt-note pages for cash and short-term investment figures that print on the balance sheet or liquidity table pages | Locator imprecision | Minor | CP-1 | Figures are right |
| The credit translation table in the business context cites 10-K pages for the Class B share count of 20,977,815, which prints on page 1 of the Q3 10-Q | Locator error | Minor | CP-1A | Figure is right |
| The coupon range 6.750% to 7.750% in the same table cites debt-history pages rather than the pages that print the coupons | Locator imprecision | Minor | CP-1A | Figures are right |
| Four small unexplained source variances in debt cash flow lines and 2027 principal | Source variance | Minor | CP-1 | Logged in the financial base and not reconciled; no effect on ratios |
| The review is not independent of the authors | Process limitation | Medium | All | A second reviewer is still needed |

### Cross-module contradictions

None found. Pairs examined and found consistent: no maturity before September 2027 in the synthesis against the 2026 notes paid on 2026-08-15 in the financial base; moderate leverage on Adjusted EBITDA against 5.10x unadjusted in the same handoffs; ample liquidity against negative working capital; the improving trend in leverage against rising run-rate interest; founder control in the business context against no documented extraction in the synthesis; and the cash premium on convertible repurchases in the business context against the extinguishment losses in the financial base.

### Verdict consistency

The verdicts agree across modules for every shared claim. The synthesis confidence of Medium is no higher than the business-context readiness judgment of READY_WITH_LIMITATIONS allows, and its listed gaps match the inherited gaps.

### Auditability assessment

| Dimension | Assessment | Evidence | Risk mechanic | Credit implication | Remediation |
| --- | --- | --- | --- | --- | --- |
| Traceability of figures | High | Every figure found in sources or in a stated calculation | A reviewer can reproduce each number | Numbers can be quoted as labelled | None |
| Calculation reproducibility | High | Every recomputation in the Calculations table matched | Formula and inputs are shown beside each result | Ratios can be rebuilt | None |
| Locator precision | Medium | Three imprecise or wrong pages for correct figures | A reviewer may open the wrong page first | Slower verification, no change in values | Correct the three citations |
| Legal and covenant support | Low | No executed documents; covenant described from filings | Legal capacity and headroom rest on filing summaries | Committee use restricted for those conclusions | Obtain executed documents |
| Independence | Low | Same session and same extraction text | Shared errors would pass unnoticed | Second review needed before external use | Independent reviewer against the original filings |

### Contrary evidence and what would change the view

The strongest evidence for a better credit view than the Medium-confidence synthesis is that Q3 2026 operating income of 106 is up from 38, Q3 2026 Adjusted EBITDA margin of 6.9% is up from 6.7%, orders delivered rose 12.2%, last-twelve-month free cash flow of 476 is 55.8% of Adjusted EBITDA, and liquidity of 1,516 including the revolver is large against 229 due in 2027. What would make that case win: last-twelve-month net income, a loss of 160, turning positive as extinguishment losses fall away, unadjusted leverage falling below 5.10x as operating income grows, and the 2027 notes settling without a large cash call.

The downside chain, with observable triggers, starts with a slowdown in U.S. demand (initiating condition). The first operational break would be falling orders delivered or lower average order value, which the release reports each quarter, forcing more advertising per order. The financial transmission is lower Adjusted EBITDA and a reversal of the 64 working-capital inflow as payables of 1,213 unwind against inventories of 89. The consequences are lower cash than the 1,038 held, less cover than 5.02x, and higher leverage, with the arithmetic reference points that LTM Adjusted EBITDA at the FY2025 level of 743 gives total debt of 3.77x and at the FY2024 level of 453 gives 6.18x (Calculations; these are reference levels, not forecasts). Refinancing then matters from 2029, when 800 of secured notes mature at market rates. Triggers to watch: quarterly orders and average order value, Adjusted EBITDA margin against 6.9%, cash against 1,038, the settlement election on the 2027 notes, and covenant certificates when obtained.

## Calculations

Independent recomputation of figures from the cited source inputs. All matched the stated value. USD millions unless stated.

| Figure | Inputs | Recomputed | Stated in handoffs |
| --- | --- | --- | --- |
| Total debt carrying | 227 + 791 + 693 + 693 + 395 (Q3 10-Q page:10-11) | 2,799 | 2,799 |
| Principal | 229 + 800 + 700 + 700 + 400 | 2,829 | 2,829 |
| Secured share of principal | (800 + 700 + 700 + 400) / 2,829 | 91.9% | 91.9% |
| LTM net revenue | 12,457 + 9,870 - 9,120 (10-K page:100; Q3 10-Q page:3) | 13,207 | 13,207 |
| LTM Adjusted EBITDA | 743 + 629 - 519 (10-K page:88; Q3 rel page:11) | 853 | 853 |
| LTM Adjusted EBITDA at Q1 and Q2 2026 | 743 + 151 - 106; 743 + 393 - 311 | 788; 825 | 788; 825 |
| Q4 2025 Adjusted EBITDA | 743 - 519 | 224 | 224 |
| LTM operating income plus D&A | (17 + 199 + 67) + (305 + 195 - 234) | 549 | 549 |
| LTM equity compensation and related taxes; share | 345 + 209 - 261; 293 / 853 | 293; 34.3% | 293; 34.3% |
| LTM operating cash flow, capital expenditure, free cash flow | 534 + 506 - 332; 205 + 175 - 148; 708 - 232 | 708; 232; 476 | 476 |
| Free cash flow share of Adjusted EBITDA | 476 / 853 | 55.8% | 55.8% |
| LTM cash interest | 139 + 129 - 98 (10-K page:101; Q3 10-Q page:5) | 170 | 170 |
| Leverage, total and net, LTM | 2,799 / 853; (2,799 - 1,038 - 60) / 853 | 3.28x; 1.99x | 3.28x; 1.99x |
| Leverage, unadjusted, LTM | 2,799 / 549; 1,701 / 549 | 5.10x; 3.10x | 5.10x; 3.10x |
| Leverage, FY2024 and FY2025 | 3,118 / 453; 1,746 / 453; 3,272 / 743; 1,730 / 743 | 6.88x; 3.85x; 4.40x; 2.33x | Same |
| Leverage at Q1 and Q2 2026 | 2,970 / 788; 1,908 / 788; 2,836 / 825; 1,693 / 825 | 3.77x; 2.42x; 3.44x; 2.05x | Same |
| Interest cover, five periods | 453 / 63; 743 / 139; 788 / 158; 825 / 178; 853 / 170 | 7.19x; 5.35x; 4.99x; 4.63x; 5.02x | Same |
| Run-rate coupons and cover | 229 x 3.250% + 800 x 7.250% + 700 x 7.750% + 700 x 6.750% + 400 x 7.125%; 853 / 195.44 | 195.44; 4.36x | About 195; 4.36x |
| Liquidity | 1,038 + 60; 500 - 82; 1,098 + 418 | 1,098; 418; 1,516 | Same |
| Principal bridge | 3,308 - 39 - 251 - 589 + 400 | 2,829 | 2,829 |
| Working capital, nine months | -36 - 18 - 70 + 188; 33 + 7 + 18 - 134; 64 - (-76) | 64; -76; 140 | 64; -76; 140 (Q3 10-Q page:44 states 140) |
| LTM interest expense, net and cover | 119 + 120 - 83; 283 / 156; 17 / 119 | 156; 1.81x; 0.14x | Same |
| Cash and investments over 2027 principal | 1,098 / 229 | 4.8x | 4.8x |
| Class B shares and votes | 20,977,815 / 136,839,940; 209,778,150 / 325,640,275 | 15.3%; 64.4% | 15.3%; 64.4% |
| Premium on convertible repurchases | 375 - 210; (99 + 148) - (56 + 89); 43 + 59 | 165; 102; 102 | 165; 102; 102 |
| Fair value over principal | 812 / 800; 720 / 700; 692 / 700; 398 / 400; 376 / 229 | 101.5%; 102.9%; 98.9%; 99.5%; 164.2% | Same |
| Debt and earnings change since FY2024 | 2,799 / 3,118 - 1; 853 / 453 - 1 | -10.2%; +88.3% | Same |
| Q3 2026 operating metrics | 3,420 / 3,117 - 1; 11.0 / 9.8 - 1; 106; 38 | 9.7%; 12.2%; 106; 38 | 9.7%; 12.2% in the Q3 10-Q (page:30); 106 and 38 as printed |
| Leverage reference levels (this review only) | 2,799 / 743; 2,799 / 453 | 3.77x; 6.18x | Not stated in the handoffs; used in the downside chain above |

## Gaps

| Gap | Severity | Affects | Action |
| --- | --- | --- | --- |
| Covenant definition of Consolidated EBITDA, the reported senior secured leverage ratio and any other financial covenant are not supplied | High | CP-1, CP-2; any covenant work | Obtain the credit agreement and compliance certificate |
| Executed indentures, credit agreement, guarantor list and restricted-subsidiary detail are not supplied | High | CP-1A, CP-2; structural priority and distribution capacity | Obtain the executed documents or their 8-K exhibits |
| Ratings, market prices, peers and management guidance are not supplied | Medium | CP-2; relative value and conversion likelihood | Supply dated market data |
| 2026 proxy statement and use of proceeds for the 2029 and 2032 issues are not supplied | Medium | CP-1A, CP-2 | Obtain the proxy statement and offering releases |
| The review is not independent of the authors; same extraction text; locators are extraction chunks | Medium | All | A second reviewer compares the handoffs with the original filings |
| Three citations point to the wrong or an imprecise page for correct figures; two statements are partly supported as worded | Low | CP-1, CP-1A, CP-2 | Correct the citations and wording in any reuse |
| Tables were read as extracted text; no fidelity review of the extraction | Low | All | Spot-check key tables against the original filings |
| Four small source variances in debt cash flow lines and 2027 principal remain unexplained | Low | CP-1 | Check against the indenture or the next report |

## Next module

None remains in the selected set. The integrity verdict is Committee use restricted: the research may support a screening view of liquidity, near-term maturities, earnings direction, leverage on stated definitions and business risk, with its stated labels, but should not support covenant, structural-priority, distribution-capacity, recovery or rating-based conclusions until the gaps above are closed. Next actions in order: obtain the executed credit agreement and indentures and the compliance certificate; obtain the 2026 proxy statement; add dated ratings and market data; correct the three citations and two wordings noted in the findings register; and have a second reviewer compare the handoffs with the original filings before external use.
