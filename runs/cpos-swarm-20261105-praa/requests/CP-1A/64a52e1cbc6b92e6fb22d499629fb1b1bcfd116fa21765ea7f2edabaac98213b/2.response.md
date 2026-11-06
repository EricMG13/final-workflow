# CP-1A — Business and transaction context: PRA GROUP INC (praa)

## Request

- Issuer: PRA GROUP INC (issuer id `praa`, ticker PRAA), as-of date 2026-11-05, information cutoff 2026-11-05 (context).
- Run `praa-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Current period q2-2026, prior period fy-2025, reporting currency USD (context settings).
- Task: build the business, ownership, transaction, timeline and governance fact pack a credit committee reads first, from the pinned filings and releases only. Creditor perspective. Documented issuer-level actions only; no view of individuals; no peer ranking, instrument recommendation or recovery conclusion.
- Execution: host session. No provider was called. Nothing dated after the cutoff is used; the latest source is the Q2 2026 10-Q signed August 7, 2026.
- Financial figures are taken from the CP-1 handoff and the cited filing pages and are not recalculated here, except where a table says otherwise.
- Upstream limits carried forward: the proxy statement, executed credit agreements and indentures, the amended European credit agreement and any 8-K are not supplied; nothing after August 7, 2026 is supplied; segment basis changed in Q4 2025.

## Sources

Locators are `page:N` of the pinned text files (source chunks, not printed page numbers). sha256 values are those CP-OS pins.

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_praa-20251231.htm.jsonl | acaea144d244584c3474f86549753d209ff125e0c5d293c88092a8b3609d005e | Business, strategy, competition, regulation, employees, holders, dividend policy, debt note, legal matters, segments |
| 10-Q_2025-09-30_praa-20250930.htm.jsonl | 929f20928dbfde158b90287ecb3f34f89e93248de03667dc981595cbc1f16f43 | Q3 2025 goodwill impairment, 2025 senior note retirement in 2024, single-segment basis |
| 10-Q_2026-03-31_praa-20260331.htm.jsonl | 5b8ee1fe62f8b0079ea63a2a1c4f92f69a59ebc645588dbcce6f190c45211b32 | European facility amendment as a subsequent event, market commentary |
| 10-Q_2026-06-30_praa-20260630.htm.jsonl | d7a354d31f5af038cbd610321c408a92f38ffbe0be4451883080ac13fa2cd5a8 | Executive overview, European forecast review, borrowings, segments, buyback, subsequent event, signatures |
| EX-99.1_2026-05-07_q12026earningsrelease.htm.jsonl | 0cafa2dd16d8fe170df8f95a181353ea848b2d370eaa0bad903e81ca9ab40ac1 | PRA 3.0 strategy language (management) |
| EX-99.1_2026-08-06_q22026earningsrelease.htm.jsonl | 90c4b9dc1bbbec8846231ce65b511117fe19795284263ee0dc2f0a68914940d4 | Management commentary on the European review, restructuring, buyback |
| EX-99.1_2026-02-26_q42025earningsrelease.htm.jsonl | ac28ac408106b5058aef5a7017ad24c9c2f1059768c1e80795f1a5ba0705218f | Not relied on for this module |

### Run settings (not issuer evidence)

| Source | sha256 | Role |
| --- | --- | --- |
| context (1185348-pra-group-inc-praa.json) | fb395d626a32c7d3e686eb338c55b901d79ab38a3782a023f0c732503b0056b3 | Dated user settings. Sector label, ticker and country come from here and are cross-checked to the filings below. Sponsor, parent and deal terms are blank, meaning unknown, not none. |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | ad930b06ca8dfafbd7d05aa59918ec9f5ec7345e1f274cfd0ac40c5b9907cbbd | Source readiness and limitations. |
| CP-1 | f504ebf424f2b6080338462ae74293629fc8293218527f27a4fbeb97c3179884 | Financial base: debt, leverage, liquidity, maturities and the Adjusted EBITDA definition. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| PRA Group is a widely held, listed buyer and collector of nonperforming loans with no sponsor or pending ownership change in the sources. Credit relevance centres on estimate-driven ERC, a 54.0% European weighting and debt-funded purchasing. | Medium | Seller concentration, executed debt documents and the proxy statement are not supplied, and nothing after August 7, 2026 is covered. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| No sponsor, controlling holder or pending transaction appears in the sources; there were 44 holders of record, and no dividends were paid in the three years to 2025. | Creditor alignment rests on public-company capital allocation, mainly repurchases, and not on sponsor behaviour. | Medium |
| Europe holds 54.0% of ERC, and the European facility was extended to April 30, 2031 with the maximum ERC ratio cut from 45.0% to 40.0%. | Refinancing risk on the largest drawn credit facility falls, but currency and fragmented regulation concentrate exposure. | Medium |
| The June 2026 European forecast review raised European ERC by $348.5 million; management links it to six years of cash overperformance. | ERC and ERC-based availability rest on model forecasts, so revisions can move both earnings and borrowing capacity. | Medium |
| A new CEO in 2025 led to a two-segment structure, cost reductions and call-centre consolidation, while U.S. legal collection expenses rose ahead of collections. | Margins depend on the cost plan outrunning higher upfront legal spend. | Medium |
| A $150 million share repurchase program was approved on August 3, 2026, after $20.0 million of repurchases in the first half of 2026. | Equity returns compete with debt reduction while purchases are debt funded; covenants cap capacity. | Medium |

### Business and transaction view

PRA Group, Inc. is a Delaware specialty finance company headquartered in Norfolk, Virginia that buys nonperforming consumer loans from banks, consumer finance companies, auto finance providers and other creditors, and collects on them over several years through call centers, external vendors, legal recovery and digital channels (10-K page:6 to page:8). It reports two segments, the U.S. and Europe, created in Q4 2025 after a new chief executive officer was appointed in 2025 (10-K page:103), plus smaller operations in South America, Canada and Australia. Revenue is accrued from the expected collections of each portfolio, so reported profit depends on management's collection forecasts; the filing itself calls Portfolio income the more predictable component and Changes in expected recoveries the estimate-driven one (Q2 10-Q page:29). The company is publicly listed with 44 holders of record and no sponsor, parent or controlling holder is disclosed in the supplied sources; the proxy statement that would give beneficial ownership is not supplied. No acquisition, take-private or other ownership transaction is described in the supplied sources. The transactions that are described are financing and portfolio events: the September 30, 2025 issue of euro-denominated 6.250% senior notes due 2032 by a Luxembourg subsidiary, the April 30, 2026 amendment and extension of the European revolving credit facility, the April 2025 sale of an 11.7% interest in a Brazilian servicing company, and the August 3, 2026 approval of a new share repurchase program. Creditor-relevant change is concentrated in three areas: the June 30, 2026 European forecast review that raised European ERC by $348.5 million; the cost and organisation programme under the "PRA 3.0" strategy (management's term); and capital returns through repurchases while portfolio purchases are financed with debt. Documented actions show no priming, uptiering, drop-down or related-party leakage, but the legal capacity under the credit agreements and indentures cannot be assessed because those documents are not supplied.

### Company and operating model

| Area | Fact | Category | Evidence and locator | Credit mechanism and implication |
| --- | --- | --- | --- | --- |
| Core activity | Purchase, collection and management of nonperforming loan portfolios, mainly Core accounts from originators who did not collect the full balance, and Insolvency accounts in bankruptcy or similar plans | Documentary Fact | 10-K page:6 and page:8: "Our primary business is the purchase, collection and management of nonperforming loan portfolios" | Cash comes from consumer repayment over years, so debt service depends on collection performance and on continued access to portfolios at acceptable prices |
| Ancillary activity | Fee-based class action claims recovery services in the U.S., not material to the U.S. segment | Documentary Fact | 10-K page:6; Q2 10-Q page:17 | Small contributor; no separate credit mechanism |
| Revenue model | Portfolio income plus Changes in expected recoveries; the latter is the difference between expected and prior recoveries, including collections above forecast and forecast revisions | Documentary Fact | 10-K page:63 definitions; Q2 10-Q page:9 and page:29 | Forecast revisions move reported revenue without moving cash in the period, so earnings and ERC-linked availability can change on estimate updates |
| Cash conversion | Collections applied to principal are shown in investing activities, so net cash used in operating activities is negative | Documentary Fact | Q2 10-Q page:44; CP-1 definition review | Operating cash flow and free cash flow built from it do not measure debt service capacity; the issuer's Adjusted EBITDA is cash-collections based and not the covenant measure |
| Geography | U.S. and Europe segments; operations in 12 countries and the United Kingdom; portfolios in 18 countries; U.S. 40.4% and Europe 54.0% of ERC at June 30, 2026 | Documentary Fact | 10-K page:6 and page:10; Q2 10-Q page:24 | Europe carries most future collections, so exchange rates, multiple national regulators and local legal processes drive value; the UK alone is the largest European block in ERC (Q2 10-Q page:37) |
| Supply and purchase flexibility | Portfolios are bought through spot sales and forward flows with terms of six to 12 months; very few forward flow agreements set a minimum purchase obligation; many allow termination or price renegotiation | Documentary Fact | 10-K page:6, page:55 and page:56; Q2 10-Q page:17 and page:42 | Purchase volume, the main use of cash, is largely discretionary, which gives management a lever to slow debt growth; the cost is lower future collections |
| Seller concentration | Seller identities and shares of purchases are not given in the pages read; the U.S. environment is described as having "a small number of sellers" | Insufficient Information | 10-K page:39 | Concentration among sellers could affect supply and pricing; the missing datapoint is the share of purchases from the largest sellers |
| Pricing and underwriting | Bids are placed in formal sales processes using proprietary models of projected collections, cost to collect and financing costs; internal investment committees approve purchases | Documentary Fact | 10-K page:6; model risk at 10-K page:18 | Returns depend on internal model accuracy; weak forecasts show up as later negative revisions |
| Collection channels | Call centers, external vendors and agencies, legal recovery, digital; roughly one-third of U.S. call center capacity moved offshore | Documentary Fact | 10-K page:7 and page:8 | Legal recovery needs upfront court costs, which are expensed before the related collections arrive |
| Cost structure | Largest lines are compensation and benefits, legal collection costs and fees, agency fees and professional services; U.S. legal collection expenses rose 40.6% in Q2 2026 against Q2 2025 while compensation fell 13.7% | Documentary Fact | Q2 10-Q page:3 and page:33 | Margin recovery depends on legal collections paying back faster than the cost is incurred |
| Cost programme | U.S. onshore agent headcount reduced by approximately 40% in 2025; second wave of cost reductions and call center consolidation in 2026 | Documentary Fact | 10-K page:39; Q2 10-Q page:24 | Supports margin if collections hold; restructuring charges of about $5 million were recorded in Q2 2026 (Q2 release page:3) |
| Capital spending | Property and equipment purchases are small relative to portfolio purchases, which are the main investment | Documentary Fact | 10-K page:70 | Capital intensity sits in portfolio purchases, not fixed assets; see CP-1 for amounts |
| Working capital | No trade receivables or inventory; finance receivables are the operating asset | Documentary Fact | 10-K page:68 | Conventional working capital metrics are not applicable |
| Funding model | Secured revolving facilities with an ERC-based borrowing base (35% of eligible Core ERC, 55% of Insolvency ERC), a term loan, senior unsecured notes, and interest-bearing deposits taken by the banking subsidiary AK Nordic AB | Documentary Fact | 10-K page:87 to page:92; Q2 10-Q page:41 and page:43 | ERC revisions change availability; see CP-1 for amounts |
| Regulation and litigation | Supervised by the CFPB in the U.S. and by national regulators in Europe; a multi-state Attorneys General investigation opened November 17, 2015 remains unresolved, with an estimated loss accrued | Documentary Fact | 10-K page:10 to page:13 and page:102 to page:103; Q2 10-Q page:17 | A settlement could cost cash and change collection practices; the accrued amount is not stated in the pages read |
| Competitive position | Management cites a diverse global presence and longstanding originator relationships as strengths | Management Language | 10-K page:10 | Self-assessment; not independently evidenced in the sources |

### Company profile

| Field | Value | Category | Locator |
| --- | --- | --- | --- |
| Legal name and form | PRA Group, Inc., Delaware corporation | Documentary Fact | 10-K page:1 |
| Headquarters | 120 Corporate Boulevard, Norfolk, Virginia | Documentary Fact | 10-K page:1 |
| Listing | Common stock, ticker PRAA, NASDAQ Global Select Market; Commission File Number 000-50058; large accelerated filer | Documentary Fact | 10-K page:1 and page:2 |
| Sector | Context label "Short-Term Business Credit Institutions"; the 10-K describes the company as a "specialty finance company" | Documentary Fact | Context; 10-K page:6 |
| Country | United States (domicile and headquarters); operations in Europe and other markets | Documentary Fact | 10-K page:1 and page:6 |
| Employees | 2,615 full-time employees worldwide at the 10-K date; 2,417 full-time equivalents at June 30, 2026 against 2,897 a year earlier | Documentary Fact | 10-K page:38; Q2 10-Q page:25 |
| Operating footprint | Five U.S. operational sites (three leased, two owned), eight leased European properties, five leased in other markets; new Charlotte hub from March 2026 | Documentary Fact | 10-K page:36 |
| Reportable segments | U.S. and Europe from Q4 2025; single segment before | Documentary Fact | 10-K page:9 and page:103; Q3 10-Q page:20 |
| Shares outstanding | 38,453,344 at February 20, 2026; 37,648,006 at July 31, 2026 | Documentary Fact | 10-K page:2; Q2 10-Q page:1 |
| Holders of record | 44 at February 20, 2026 | Documentary Fact | 10-K page:36 |
| Ownership | No sponsor, parent or controlling holder disclosed in the supplied sources; beneficial ownership is in the proxy statement, which is not supplied | Insufficient Information | 10-K page:3; context sponsor field blank |
| Dividend policy | No regular dividends; none paid in the three years ended December 31, 2025 | Documentary Fact | 10-K page:37 |
| Senior management | Martin Sjolund, President and Chief Executive Officer; Rakesh Sehgal, Executive Vice President and Chief Financial Officer; Steven D. Fredrickson, Executive Chairman and Director | Documentary Fact | Q2 10-Q page:49; 10-K page:114 |
| Auditor | Ernst & Young LLP, auditor since 2021 | Documentary Fact | 10-K page:68 |
| Fiscal year end and currency | December 31; USD | Documentary Fact | 10-K page:1; context |
| Credit ratings | Not supplied; context ratings field is blank | Insufficient Information | Context |

### Transaction summary and new debt issues

No acquisition, take-private, merger or other ownership transaction is described in the supplied sources, and the context holds no deal terms, so the transaction view is Insufficient Information for any pending or announced ownership event as of 2026-11-05; the sources end on August 7, 2026. The financing and portfolio transactions that are described are as follows. On September 30, 2025 the company completed a private offering of EUR 300.0 million (US$352.4 million at issuance) of 6.250% senior notes due September 30, 2032 through its wholly owned subsidiary PRA Group Europe Holding II S.à r.l.; the notes are senior unsecured obligations of that issuer, guaranteed on a senior unsecured basis by PRA Group, Inc. and by the domestic restricted subsidiaries that guarantee the North American facility, with interest payable on March 31 and September 30, a change of control put at 101%, and a call schedule at 103.125% from September 30, 2028 falling to par from 2030 (10-K page:90). The use of proceeds is not stated in the pages read, so it is Insufficient Information; the cash flow statement shows the proceeds within financing activities (10-K page:71) and the company describes the issue as its first euro-denominated senior notes (10-K page:38). On April 30, 2026 the company amended and restated its European revolving credit facility: the maturity moved from November 23, 2027 to April 30, 2031, the maximum ERC ratio fell from 45.0% to 40.0%, and, subject to conditions, borrowers may make investments in or loans to joint ventures up to EUR 100 million; the Q1 2026 10-Q reports the aggregate revolving borrowings available and funding costs as unchanged (Q1 10-Q page:17; Q2 10-Q page:11). The joint venture basket is a new permission that could move value outside the borrower group, but its use is not evidenced and the agreement is not supplied. Earlier debt history inside the sources: in 2024 the company issued 8.875% senior notes due January 31, 2030 ($400.0 million on May 20, 2024 and a further $150.0 million on November 25, 2024 at 103.625% of principal) and retired 2025 senior notes (10-K page:91; Q3 10-Q page:6; 10-K page:71). Other events: the April 2025 sale of the 11.7% interest in RCB Investimentos S.A. with a gain of $38.4 million, stated not to affect ownership of the portfolio investments in South America (10-K page:43); the Q3 2025 goodwill impairment, recognised after a quantitative test that compared fair value with market capitalization (Q3 10-Q page:12); and, as a subsequent event to the June 30, 2026 balance sheet, the August 3, 2026 board approval of a new share repurchase program of up to $150 million, subject to covenants and board discretion (Q2 10-Q page:21). The new program follows repurchases of $20.0 million in 2025 and $20.0 million in the first half of 2026 (10-K page:38; Q2 10-Q page:15). Amounts of each financing and the debt table are in the CP-1 handoff.

### Ownership and control

| Item | Evidence | Category | Implication |
| --- | --- | --- | --- |
| Owner class | Listed common equity; 44 holders of record; non-affiliate market value of $568,047,885 at June 30, 2025 on a $14.75 close | Documentary Fact | Widely held public company; no sponsor control rights in the sources (10-K page:2 and page:36) |
| Control rights | None disclosed; Part III information incorporated from the proxy statement, which is not supplied | Insufficient Information | Board composition, director independence and beneficial ownership cannot be read; the missing datapoint matters for control and alignment (10-K page:3) |
| Economic interests of others | Noncontrolling interests exist; distributions to them are made | Documentary Fact | Part of the cash generated leaks to minority holders; see CP-1 for amounts (10-K page:71; Q2 10-Q page:5) |
| Prior ownership and dividend recapitalisation | None described; no dividends paid in three years | Documentary Fact | No dividend recapitalisation in the period covered (10-K page:37) |

### Timeline

| Date | Event | Status | Locator |
| --- | --- | --- | --- |
| Nov 17, 2015 | Civil investigative demands from multiple state Attorneys General offices | Open, estimated loss accrued | 10-K page:102 and page:103 |
| May 20, 2024 | $400.0 million 8.875% senior notes due 2030 issued | Documentary Fact | 10-K page:90 and page:91 |
| Nov 25, 2024 | Additional $150.0 million of 2030 senior notes at 103.625% | Documentary Fact | 10-K page:91 |
| Apr 2025 | Sale of 11.7% interest in RCB Investimentos S.A., gain $38.4 million | Documentary Fact | 10-K page:43 and page:84 |
| 2025 | New chief executive officer appointed; business reorganized into U.S. and European segments in Q4 2025 | Documentary Fact | 10-K page:103 |
| Sep 30, 2025 | EUR 300.0 million 6.250% senior notes due 2032 issued through PRA Group Europe Holding II S.à r.l. | Documentary Fact | 10-K page:90 |
| Q3 2025 | Goodwill impairment of the debt buying reporting unit, $412.6 million | Documentary Fact | Q3 10-Q page:12 |
| Apr 30, 2026 | European revolving facility amended, extended to 2031, ERC ratio cap cut to 40.0% | Documentary Fact; subsequent event to the Q1 2026 balance sheet | Q1 10-Q page:17; Q2 10-Q page:11 |
| Jun 30, 2026 | Forecasts for the majority of European pools updated at the quarterly assessment | Documentary Fact | Q2 10-Q page:9 and page:24 |
| Aug 3, 2026 | New repurchase program of up to $150 million approved | Subsequent event to the June 30, 2026 balance sheet | Q2 10-Q page:21 |
| Aug 6 and Aug 7, 2026 | Q2 2026 release and 10-Q | Latest sources | Q2 release page:1; Q2 10-Q page:49 |

### Governance and capital-allocation behaviour

Assessed at issuer level on documented actions only. Legal capacity (what the documents permit), willingness (what was done) and feasibility (liquidity, leverage, market access) are kept separate.

| Documented action | Behaviour category | Mechanic | Legal capacity link | Evidence quality |
| --- | --- | --- | --- | --- |
| Repurchased $20.0 million of shares in 2025 and $20.0 million in the first half of 2026; new $150 million program approved; no dividends | Neutral or Mixed | Share repurchases are cash returned to equity while borrowings rose and portfolio purchases were debt funded | Capacity: repurchases are stated to be subject to covenants in the credit facilities and indentures (Q2 10-Q page:15); the North American facility caps dividends and distributions at $50.0 million per fiscal year (10-K page:87); baskets in the indentures are not supplied. Willingness: documented repurchases. Feasibility: see CP-1 for liquidity | High |
| Extended the European facility early, with a lower ERC ratio cap and a joint venture investment basket | Supportive on refinancing; Insufficient Information on the basket | Longer maturity lowers near-term refinancing risk; lower ERC ratio cap changes the leverage test; the basket adds an investment permission | Capacity: the amended agreement is not supplied | High for the terms stated; Low for effect |
| Sale of the 11.7% RCB interest; reorganisation into two segments; cost reduction programme | Neutral or Mixed | Disposal of a servicing stake and cost actions affect margins and reporting transparency, not creditor claims | No documents needed; actions are in the filings | High |
| Issued euro senior notes through a Luxembourg subsidiary guaranteed by the parent and U.S. restricted subsidiaries | Neutral or Mixed | Structure places an issuer outside the U.S. group with parent guarantees; guarantor coverage of European assets is not evidenced | Capacity: indenture not supplied; the 10-K states the guarantees (10-K page:90) | High for the structure stated |
| Reporting: reconciliations of non-GAAP measures, ERC by year and quarterly disclosure of forecast revisions | Supportive (transparent reporting) | Allows creditors to track ERC revisions and Adjusted EBITDA; the revision explanation is management's | None | High |
| No priming, uptiering, drop-down, non-pro-rata exchange or collateral release is described in the supplied sources | Insufficient Information | Absence in summary disclosures is not evidence of absence; the governing documents are missing | Capacity not assessable | Insufficient |

### Evidence-to-implication translations

| Theme | Evidence | Risk mechanic | Credit implication | Countering conflict or limit |
| --- | --- | --- | --- | --- |
| Revenue durability | Q2 10-Q page:9: forecasts for the majority of European pools were updated, giving a positive adjustment to changes in expected future recoveries of approximately $105 million, "partially offset" by lower forecasts on other pools | Revenue recognised from forecast revisions is an estimate of future cash; a reversal would reduce revenue and, through the ERC-based borrowing base, availability | Earnings and liquidity are sensitive to model accuracy; the cash collection trend in CP-1 is the cross-check | The release says the change in expected recoveries was "primarily driven by" the approximately $349 million ERC increase; the filing puts the income adjustment near $105 million. Different measures, not a numeric conflict |
| Margin and cash-flow risk | U.S. legal collection expenses rose 40.6% in Q2 2026 and U.S. compensation fell 13.7% (Q2 10-Q page:33) | Legal recovery costs are incurred before collections; a slower court process leaves cost without cash | Margin recovery in the U.S. depends on legal channel productivity; U.S. adjusted segment operating income was flat year on year in Q2 2026 (17,315 against 17,511 in thousands, Q2 10-Q page:33) | Management expects the legal spend to support future collections growth (Q2 release page:3), a Management Language claim |
| Concentration | Europe is 54.0% of ERC; the largest drawn credit facility is European; seller concentration is not disclosed | Currency moves and national regulation change collections and debt in the same currencies; the euro notes and European facility partly match the euro assets | Concentration is geographic and regulatory; the natural hedge is partial and not quantified in the sources | Seller concentration is Insufficient Information |
| Ownership alignment | Public company, no sponsor; repurchases and a new program; no dividends | Equity returns come from repurchases that compete with debt reduction | Alignment with creditors depends on leverage tolerance; no sponsor extraction behaviour is documented | Covenant capacity for repurchases and the indenture baskets are not supplied |
| Funding and refinancing | European facility extended to April 30, 2031; the next revolver maturities are October 2029 (CP-1) | Longer maturities lower rollover risk in the nearer years; 2029 holds the largest cluster in CP-1 | Refinancing sensitivity moves to 2029; ERC-based availability can change with revisions | Amended agreement not supplied |
| Key uncertainties | Covenant ratio levels are not printed; multi-state Attorneys General matter unresolved; CFPB direction uncertain per the 10-K | Unobserved headroom plus a possible cash settlement | Monitoring posture rather than a conclusion | Exact accrual not stated in the pages read |

### Conflicts

No factual conflict between sources was found that requires logging unreconciled. Two differences were checked and are not conflicts:

- European facility maturity: the 10-K states November 23, 2027 (page:89) and the Q2 10-Q states April 30, 2031 (page:11). The second follows an amendment dated April 30, 2026 (Q1 10-Q page:17), so they are sequential, not contradictory.
- European review size: the Q2 release speaks of an approximately $349 million ERC increase driving the rise in changes in expected recoveries (page:3), while the Q2 10-Q gives $348.5 million for the ERC increase (page:24) and approximately $105 million as the positive adjustment to changes in expected future recoveries (page:9). Different measures; a consumer must not treat the ERC increase as income.

### Monitoring gaps

| Missing item | Severity | Why it matters | Action |
| --- | --- | --- | --- |
| Executed credit agreements and indentures, including the amended European agreement | High | Covenant definitions, baskets, restricted group and legal capacity for distributions and investments | Supply the documents |
| Covenant compliance certificate or ratio levels | High | Headroom is not observable | Supply or keep Not supplied |
| Proxy statement | Medium | Beneficial ownership, board independence, compensation alignment | Supply if governance scoring is needed |
| Seller concentration | Medium | Supply, pricing and forward flow reliance | Supply disclosure if available |
| Debt maturity schedule at June 30, 2026 | Medium | Not printed; CP-1 derived it from instrument terms | Confirm with the issuer |
| Add-back bridge for covenant EBITDA | High | The issuer's Adjusted EBITDA is not the covenant measure | Supply credit agreement definitions |
| Events after August 7, 2026 | Medium | Financing, ratings and the quarter ended September 30, 2026 | Supply later filings |

### Consumer assessments

| Module | Readiness | Take from this handoff | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 | Ready with limitations | Business model and estimate-driven revenue, Europe weighting, funding model, the European facility amendment, repurchase behaviour, regulatory and litigation exposure | Frames which financial risks are structural and which are estimate-driven | Executed documents, covenant levels, seller concentration, ownership detail | Carry the gaps as restrictions; do not infer legal capacity |
| CP-5 | Ready with limitations | Every fact row carries a page locator and a category tag; management language is tagged | Lets the trace review separate documentary fact from management characterisation | Insufficient Information rows have no evidence by design | Check Management Language rows are not used as fact downstream |

## Calculations

No new calculation. Percentages quoted (40.6% and 13.7% change in U.S. legal collection expenses and compensation, 40.4% and 54.0% of ERC, 103.625% issue price) are as printed in the cited pages. Financial amounts are those in the CP-1 handoff.

## Gaps

| Gap | Severity | Affected use | Action |
| --- | --- | --- | --- |
| Executed credit agreements, indentures and the amended European agreement not supplied | High | Legal capacity, covenant definitions, restricted group | Supply documents |
| Covenant ratio levels not printed | High | Headroom | Supply compliance certificates |
| Proxy statement (beneficial ownership, board, compensation) not supplied | Medium | Ownership and governance | Supply |
| Seller concentration not disclosed in the pages read | Medium | Supply risk | Supply if disclosed |
| Use of proceeds of the 2032 senior notes not stated in the pages read | Low | Capital allocation | Check the 8-K cited in the 10-Q exhibit list, if supplied |
| Accrued amount for the multi-state Attorneys General matter not stated | Medium | Litigation exposure | Supply the contingencies disclosure with the amount |
| Ratings, market prices and sponsor information not supplied | Low | Context | Not required |
| Events after August 7, 2026 not supplied | Medium | Currency of the view | Supply later filings |

## Next module

- CP-2: carry the estimate-driven revenue and ERC-linked availability as the central risk, the Europe weighting, the European facility amendment and the repurchase behaviour; treat legal capacity, covenant headroom and ownership detail as Not supplied; use the CP-1 maturity and liquidity tables with their definition limits.
- CP-5: trace each Documentary Fact row to its page; treat Management Language rows (competitive strengths, PRA 3.0 characterisations, "record ERC levels") as management claims; verify the sequential, not conflicting, treatment of the European facility terms and the ERC versus income distinction.
