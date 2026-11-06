# Business and transaction context: MAGNITE, INC. (mgni)

## Request

- Issuer: MAGNITE, INC. (issuer id mgni, Nasdaq MGNI), as-of date 2026-11-05, information cutoff 2026-11-05. Pathway credit_snapshot; reporting currency USD; current period Q3 2026, prior period FY2025.
- Question: which transaction, business, ownership and operating facts matter most to a creditor, and what is the credit-relevant history and change? Required decision drivers: transaction and ownership structure; business and operating model; credit-relevant history.
- Execution: host session reading the pinned text files; no provider call. Locators `key pN` are source chunks (`page:N`); quotes are exact substrings of the located chunk. Keys are listed in Sources. Fact categories: Documentary Fact, Management Language, Analyst Interpretation, Insufficient Information.
- Prohibited and not done: no peer ranking, no instrument recommendation, no recovery conclusion. Figures are cited from the filings or refer to the accepted financial base handoff; none is new.

## Sources

| Key | Source (exact name) | sha256 (pinned file) | Used for |
| --- | --- | --- | --- |
| 10K | 10-K_2025-12-31_mgni-20251231.htm.jsonl | f96c3c8e001359e3762f2fdcdb5fec62dc8b34a692251ca50bc2b0320cbc2a0a | Business description, risk factors, concentration, history, dividend policy |
| Q1Q | 10-Q_2026-03-31_mgni-20260331.htm.jsonl | a236956e4f58c23dd0c7e9814923ff8c58122f0f2ffc4593ab7dcd2ac0165adf | Convertible maturity timing |
| Q2Q | 10-Q_2026-06-30_mgni-20260630.htm.jsonl | 796b488acb30e088707602178e4e306b131923e994381f8d88dd91dd9706c3bb | Revolver draw in the quarter |
| Q3Q | 10-Q_2026-09-30_mgni-20260930.htm.jsonl | c6922a9ebeac839059c55928b8190f39ac8376ff2e5306b6695aa910a9515bb4 | Latest debt note, Google remedies, repurchases, subsequent event |
| ER1 | EX-99.1_2026-05-06_a991-earningsq12026.htm.jsonl | 1a65026a829ea6d3398cf84619845f6c5e542133314c7959aef5563816dda9a4 | Management narrative, Q1 2026 |
| ER2 | EX-99.1_2026-08-05_a991-earningsq22026.htm.jsonl | 7a22ad7a167049f41876318b3adec058b3521559a35265d5009853f0eba7f49d | Management narrative, Q2 2026 |
| ER3 | EX-99.1_2026-11-04_a991-earningsq32026.htm.jsonl | 9404d81beccd30783613c5d17e44e7f768a511dbf6b00a1825d39fa611f52e22 | Management narrative, guidance, Q3 2026 |
| context | context (run settings; not issuer evidence) | add9e4e5fe29cabeba543552138279256276897be557a9b8ceef018e156869fc | Dates; sponsor, parent and borrower fields blank, deal terms empty |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 3b5491ad4792081e28ccae80a3f58279ef4978af29432bbcc0ff2472969d5e7a | Source readiness: no credit agreement or proxy statement supplied; text extraction only. |
| CP-1 | cf0ec312bd9af098d8cd5dace46250f5fca56aeaabf079c0944d4e2f7db15241 | Financial base: leverage, cover, liquidity and maturities; cash-float, seasonality and one-off tax benefit qualifications. Referenced, not repeated. |

This answer corrects nothing in those handoffs. One scope note: CP-0 described the covenant as a description in the filings; this answer relies on the same description.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Magnite is a listed sell-side advertising platform with no named sponsor whose growth rests on connected TV. Demand is concentrated in a few buyers, the Google antitrust outcome is a possible upside, and no leveraged transaction is under way. | Medium | No ownership percentages, proxy, credit agreement or ratings are supplied; most operating claims are management's own. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Revenue is a percentage of ad spend, with lower fees on connected TV reserve auctions; the mix is shifting toward connected TV. | Growth is volume driven but take-rate pressure can offset it. | Medium |
| Two buyers were 40% and 12% of receivables at December 31, 2025, and no seller reached 10% of revenue. | Buyer credit and demand concentration can hit cash conversion quickly. | High |
| The convertible notes were repaid at maturity from cash and no new debt was issued; only a term loan repricing followed in October 2026. | Debt service and refinancing pressure are low; the actions are supportive of creditors. | High |
| A September 2026 court remedies opinion against Google is being appealed; management expects a significant positive impact. | Possible upside to display share, but timing and size are uncertain and not in guidance. | Low |

### Business and transaction view

Magnite is a public company with no financial sponsor, no controlling holder identified in the supplied sources and a single operating segment. It sells technology that lets publishers, especially connected TV owners, monetize ad inventory to buyers and demand-side platforms, and earns a fee that is a percentage of the ad spend. The credit-relevant business facts are the dependence on a small number of large demand sources, the concentration of connected TV supply in a few large sellers, the lower fees on reserve auctions, seasonal fourth-quarter strength, and the effect of the Google antitrust ruling on open-web display competition. The credit-relevant history is the financing of the SpotX acquisition by a term loan and convertible notes, the 2024 refinancing and repricings, the repayment of the convertible notes in cash at maturity in March 2026, and the October 2026 repricing amendment. There is no pending acquisition, sponsor transaction or new debt issue in the supplied sources. Governance evidence is limited to documented actions: deleveraging by repayment, share repurchases under a board plan and no dividends. The financial consequences are in the accepted financial base handoff; the main limits here are that ownership percentages, the proxy statement and the executed financing documents are not supplied, and that operating claims in the releases are management language.

### Company and operating model

| Area | Fact | Category | Source | Credit relevance |
| --- | --- | --- | --- | --- |
| Core business | "provides technology solutions to automate the purchase and sale of digital advertising inventory"; operates one segment (sell-side platform with a connected TV ad server, SpringServe) | Documentary Fact | 10K p8; Q3Q p8 | Single-business concentration: no segment offsets a weak ad market. |
| Market position | "the world's largest independent omni-channel sell-side advertising platform" | Management Language | 10K p8 | Self-described; no independent source supplied, so not relied on. |
| Revenue model | "We generate revenue through our platform on a transactional basis where we are paid by a publisher each time an impression is monetized"; the fee is a percentage of spend, with some fixed CPM and fixed monthly fees | Documentary Fact | 10K p41; Q3Q p37 | Revenue moves with ad spend volume and take rate, so it is cyclical and has no contracted floor in the sources read. |
| Take-rate mechanics | "our take rate tends to be lower for reserve auctions compared to auctions with multiple bidders, and tends to be lower on CTV transactions"; "the majority of CTV transactions are currently executed through reserve auctions" | Documentary Fact | 10K p41 | Connected TV growth can lift volume faster than fees, which limits margin gain per dollar of spend. |
| Biddable shift | Management believes biddable CTV carries "a higher take-rate compared to reserve auctions" and would help growth | Management Language | 10K p10 | An expectation, not a result; treat as upside, not a base case. |
| Channel mix | Contribution ex-TAC reported for CTV, Mobile and Desktop; CTV is the growth channel (financial base handoff) | Documentary Fact | 10K p98; Q3Q p45 | Growth and mix risk both sit in connected TV. |
| Demand concentration | "ad spend is highly concentrated among relatively few DSPs"; "two buyers accounted for 40% and 12%, respectively, of consolidated accounts receivable, net" at December 31, 2025 | Documentary Fact | 10K p25; 10K p137 | Loss or credit stress at one demand platform would affect revenue and collections together. |
| Supply concentration | "No seller of advertising inventory accounted for 10% or more of revenue"; but "CTV inventory tends to be concentrated on a smaller number of larger sellers" | Documentary Fact | 10K p137; 10K p35 | No single seller dominates revenue, yet losing a large connected TV seller would remove material inventory. |
| Seller payables | At December 31, 2025 "one seller of advertising inventory accounted for 27% of accounts payable and accrued expenses" | Documentary Fact | 10K p137 | Payables to publishers are large and sit ahead of the cash; see the float qualification in the financial base. |
| Geography and people | Operations "in North America, Australia and Europe, and a developing presence in Asia and South America"; non-U.S. operations "perform primarily sales, marketing, and service functions"; "971 full-time employees" at December 31, 2025 | Documentary Fact | 10K p9; 10K p23 | Asset-light cost base; non-U.S. cash is partly held abroad (financial base handoff). |
| Seasonality | Results "higher in the fourth quarter than in other quarters" | Documentary Fact | 10K p29 | Quarter-end cash, leverage and cash flow depend on the date in the cycle. |
| Capital spending and cost structure | Technology and development, sales and marketing and general and administrative are the main expense lines; capex is property, equipment and capitalized software | Documentary Fact | 10K p120; 10K p121 | Capital intensity is low relative to Contribution ex-TAC; see the financial base for amounts. |
| Working capital | Magnite collects from buyers and pays sellers; payables exceed receivables at September 30, 2026 | Analyst Interpretation | Q3Q p2 | Cash is partly float; the amount that is free is Not supplied. |
| Contract terms with buyers and sellers | Master service agreement terms, contract lengths and termination rights | Insufficient Information | Not supplied | Revenue visibility cannot be assessed from the filings read. |

### Company profile

| Attribute | Detail | Category | Source |
| --- | --- | --- | --- |
| Legal name and domicile | MAGNITE, INC., Delaware; principal office New York, New York | Documentary Fact | 10K p1 |
| Sector and country | Services-Computer Programming, Data Processing, Etc.; United States (context) | Documentary Fact | context |
| Listing | Common stock on the Nasdaq Global Select Market, symbol MGNI | Documentary Fact | 10K p1 |
| Ownership | "approximately 42 holders of record of our common stock"; no sponsor or controlling holder is named in the sources read; holder percentages are in a proxy statement that is Not supplied | Insufficient Information | 10K p80; 10K p3 |
| Dividend policy | "We have never declared or paid any dividends"; the credit facility restricts dividends | Documentary Fact | 10K p80 |
| Auditor | Deloitte & Touche LLP; unqualified opinion on FY2025 and FY2024 statements | Documentary Fact | 10K p115; 10K p119 |
| Fiscal year and filings | Year ended December 31; FY2025 10-K and three 2026 10-Qs supplied | Documentary Fact | 10K p1; Q3Q p1 |
| Debt | Secured term loan maturing February 2031; revolver maturing February 2029, undrawn; amounts in the financial base | Documentary Fact | Q3Q p19 |
| Ratings | Context ratings list is empty; no agency report supplied | Insufficient Information | context |
| Issuer, guarantor and restricted-group names | Subsidiary guarantors are mentioned but not named | Insufficient Information | 10K p64 |
| Governance and sponsor behaviour | Repaid the convertible notes at maturity from cash; repurchased shares under a board plan; no dividends; no related-party or sponsor payments identified in the sources read | Analyst Interpretation | Q3Q p14; Q3Q p50 |

### Transaction summary and new debt issues

No acquisition, sponsor transaction, merger, dividend recapitalisation or new debt issue is described in the supplied sources for FY2025 or 2026 to date, other than the items below. Where a transaction source is missing for a topic, the topic is Insufficient Information rather than an adverse conclusion.

Timeline, by date:

- Financing of SpotX: the 10-K risk factor states "significantly increased our leverage, which may put us at greater risk of defaulting on our debt obligations" and that the cash portion of the acquisition was financed by a term loan and convertible senior notes (10K p63). The acquisition date is not stated in the chunks read; treat it as Not supplied here.
- February 6, 2024: refinancing into the 2024 Credit Agreement, a seven-year term loan and a five-year revolver (Q3Q p19). Amendments in September 2024 and March 2025 repriced the term loan to Term SOFR plus 3.00% (Q3Q p19). These are borrower-favourable repricings; they are debt terms, not changes of control.
- September 2025: completed the acquisition of Streamrai, Inc., a generative-AI video-ad tool for connected TV (10K p15). The cash outflow was small relative to the balance sheet (financial base handoff, acquisitions line); purchase terms and price allocation are Not supplied in the chunks read.
- September 16, 2025: filed a lawsuit against Google in the Eastern District of Virginia seeking damages and other remedies; no recovery is recorded and none is quantified (Q3Q p24, p36).
- March 15, 2026: the convertible senior notes matured and were repaid in cash; no convertible notes remain (Q3Q p14). No new debt was raised for this.
- Second quarter 2026: a short-term draw on the revolver was borrowed and repaid within the quarter (Q2Q p18); the revolver was undrawn at quarter ends.
- February 23, 2026 and nine months 2026: the board approved a share repurchase plan, and shares were repurchased under it in the period (Q3Q p50). This returns cash to equity holders; the repurchase capacity under the credit agreement is Not supplied.
- September 2026: the Court issued its remedies opinion against Google ("mandating that Google undertake certain behavioral remedies and appointing a six-year independent compliance monitor"); "Google has indicated its intent to appeal the decision" (Q3Q p36). Management says it expects "a significant positive impact on our industry and business prospects" (Management Language, Q3Q p36). The 2027 outlook is stated "not including upside from Google remedies" (ER3 p1).
- Subsequent event, October 7, 2026: Amendment No. 3 lowered the term loan margin and the revolver margin range (Q3Q p29). It post-dates the September 30, 2026 balance sheet and is not folded into that period's facts.

Governance and sponsor behaviour (issuer level, documented actions only): the repayment of the convertible notes from cash is deleveraging; share repurchases and the prior-period repricings are neutral to supportive; there is no evidence of dividend recapitalisation, debt-funded distribution, priming, uptiering, drop-down or collateral release in the sources read. Legal capacity (what the credit agreement permits for restricted payments, incurrence and liens), willingness (what was done) and feasibility (liquidity and leverage in the financial base) are kept separate: willingness and feasibility are evidenced, legal capacity is not because the credit agreement is Not supplied. Evidence quality is High for the dated filings and Low for management claims in the releases.

Conflicts logged: none. No two supplied documents state a different amount or date for the same fact in the chunks read. The FY2025 10-K debt note first states a 4.50% term loan margin and then the amendments that reduced it to 3.00%; that is a history of terms, not a conflict.

### Credit translations

1. Revenue durability. Evidence: revenue is a percentage of ad spend and the take rate "tends to be lower on CTV transactions" (10K p41); results are higher in the fourth quarter (10K p29). Mechanic: growth is volume driven and exposed to ad budgets and to fee compression as connected TV reserve auctions grow. Implication: cash flow is cyclical and seasonal; the financial base shows strong recent growth, but revenue visibility is not contractually evidenced (Insufficient Information on contract terms). The Google remedies are a possible counter-force but are unquantified and under appeal.
2. Concentration risk. Evidence: "two buyers accounted for 40% and 12%" of receivables (10K p137) and demand is "highly concentrated among relatively few DSPs" (10K p25). Mechanic: a payment delay or volume shift at one platform hits both collections and revenue, and Magnite pays sellers regardless. Implication: liquidity and the cash-float qualification matter more than the leverage ratio alone.
3. Sponsor alignment. Evidence: no sponsor named; no dividends; notes repaid from cash. Mechanic: no sponsor extraction channel is evidenced. Implication: monitor share repurchases against the credit agreement restrictions, which are not supplied.
4. Key uncertainties: executed financing documents, proxy ownership, contract terms and the outcome and timing of the Google remedies and damages claim.

### Consumer readiness

| Consumer | Readiness | What to take from this module | Why it matters | Gap and action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Single-term-loan structure, October 2026 amendment, repayment of the convertible notes, no new issue, buyer concentration | Sets the liquidity and refinancing context and the cash-float caveat | Credit agreement and covenant definitions are Not supplied; retrieve exhibits if headroom matters. |
| CP-5 | READY_WITH_LIMITATIONS | Fact categories, management-language flags and the Insufficient Information rows | Lets the evidence review test claims that rest on management statements | Operating claims are not independently corroborated; check each locator. |

## Calculations

None. This module performs no calculations. Figures are cited as printed (percentages of receivables and payables, the 971 employee count) or refer to the financial base handoff.

## Gaps

| Gap | Severity | Effect | Action |
| --- | --- | --- | --- |
| Executed 2024 Credit Agreement, amendments and indenture: Not supplied | Medium | Restricted-payment, incurrence and guarantor terms (legal capacity) cannot be assessed | Retrieve from EDGAR exhibits if needed |
| Proxy statement and ownership percentages: Not supplied | Low | Control rights and holder concentration are Insufficient Information | Retrieve the proxy statement |
| Contract terms with demand platforms and large sellers: Not supplied | Medium | Revenue visibility and termination risk not assessable | None available in the filings read |
| SpotX acquisition date and purchase terms are not stated in the chunks read | Low | Timeline detail only | Search the earlier 10-K if required |
| Streamrai purchase price and terms | Low | Small relative to the balance sheet; terms Not supplied | None |
| Google damages claim: no quantified amount, no recovery recorded; remedies under appeal | Medium | Upside and timing unquantified | Monitor the final judgment |
| Ratings: none supplied | Medium | External credit view unavailable | None in the sources |
| Market position claims are management language | Low | Not relied on | Attributed above |

## Next module

Proceed to CP-2 (capital structure, liquidity and covenants) and then CP-5 (evidence review). Carry forward: no sponsor and no pending transaction; the single-term-loan structure and the October 7, 2026 amendment as a subsequent event; buyer concentration and the cash-float qualification; the Google remedies as an unquantified, appealed possibility; and the absence of the credit agreement, proxy and ratings.
