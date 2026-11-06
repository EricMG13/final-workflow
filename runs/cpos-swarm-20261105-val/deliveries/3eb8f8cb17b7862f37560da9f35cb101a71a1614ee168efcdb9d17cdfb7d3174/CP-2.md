# CP-2 — Fundamental credit synthesis: Valaris Ltd (val)

## Request

Credit synthesis for Valaris Ltd, issuer id `val`, as of 2026-11-05 (cutoff 2026-11-05), pathway `credit_snapshot`, reporting currency USD. Scope is the fundamental credit view built from the financial base view (CP-1) and the business and transaction context (CP-1A) on a standalone basis, with the pending Transocean combination treated as a transaction risk. No peer ranking, instrument recommendation or recovery conclusion is given.

## Sources

| Source | sha256 | Use in this answer |
| --- | --- | --- |
| 10-K_2025-12-31_val-20251231.htm.jsonl | b0f40796936a513fe6362c5f87d6a2a2819cd2f6e423112bfcf4a7c94647ac50 | Spot checks of upstream figures; deferred tax asset note (page:141) |
| 10-Q_2026-03-31_val-20260331.htm.jsonl | 856b19f20ceb9a456e4cf71dc5d1f96d12072575504148e1684cf5301164037f | Not cited directly; read for consistency |
| 10-Q_2026-06-30_val-20260630.htm.jsonl | d045ec4aa0f0c5450f1ffc05520139072532c8f88ec1804bd561ac63d9d380b7 | Not cited directly; read for consistency |
| 10-Q_2026-09-30_val-20260930.htm.jsonl | 73a1a96ecd1c9340e41638f2528ea86ae030d4c896022c1e422144610c8461ec | Spot checks of upstream figures; balance sheet (page:9), capital expenditure guidance (page:52) |
| EX-99.1_2026-05-04_a03312026ex991pressrelease.htm.jsonl | fb13914842f3e3a58a0b5ccdbd3cb04d0eb99161ae6d4b18bdfd3afa295e84b5 | Not cited directly; read for consistency |
| EX-99.1_2026-08-05_a06302026ex991pressrelease.htm.jsonl | 21077052c215c76afaa6a29e3ea89e20e01ee6140be558608fa94290eaa87b1f | Not cited directly; read for consistency |
| EX-99.1_2026-11-02_a09302026ex991pressrelease.htm.jsonl | 649e9df09c58fc28e42170873dd9e204e4698e7b6a16ba8868ab909251dcc271 | Spot checks of upstream figures (quarterly Adjusted EBITDA) |
| context | 630c8480b8c6896f51051152fc8ca75c81e04a78fc5ea8aebca9a62a14a6fd8f | Run settings; not issuer evidence |

| Handoff | sha256 | Use in this answer |
| --- | --- | --- |
| CP-0 | f373f490427bdb136b51b89f68fd080fb20b9ef4328505ea7636662606abf930 | Readiness and gap register |
| CP-1 | 553419305d3d0840e45db8a53a4ea08f11150ae95be0ecddbcfd829bc1c4363f | All financial figures, debt, liquidity and covenant facts |
| CP-1A | 61a5beb986ccdfab9790deef0d84544f4320e760e0bdde73d67cc33d45dcc986 | Business, transaction, ARO and governance rows |

The conclusions rest on the upstream handoffs. The source files were used only for the two supplementary checks marked in the calculations. Locators in the evidence trace are `page:N` chunks of the pinned files, not printed pages.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Valaris has low standalone refinancing risk, with liquidity of USD 900.1 million and no debt due before 2030, but earnings fell and spending exceeds cash flow. The pending Transocean takeover could change the credit before the standalone figures are tested. | Medium | Covenant levels, the combination terms and the treatment of the notes are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Liquidity of USD 900.1 million at September 30, 2026 and no principal due before 2030. | Near-term refinancing and liquidity risk is low on the reported figures. | High |
| Gross leverage rose from 1.71x at FY2025 to 2.68x on a last-twelve-months basis to Q3 2026. | Leverage is moderate but rose as Adjusted EBITDA fell; the latest quarter improved. | High |
| Operating cash flow less capital expenditure was USD -206.8 million over the last twelve months. | Cash is being used to fund upgrades, so liquidity depends on drillships earning higher day rates. | High |
| The Transocean combination is expected to close on or about December 1, 2026; its effect on the notes is not stated. | Standalone metrics may not describe the issuer after closing. | Medium |
| The revolver has three financial covenants and no level is printed. | Headroom cannot be assessed. | High |

### Credit view

Valaris Ltd has a low standalone refinancing risk and moderate leverage, but its credit quality now depends on a takeover whose effect on creditors is not disclosed. The strongest support is liquidity of USD 900.1 million and no debt principal due before 2030. The weakest point is cash generation: over the last twelve months Adjusted EBITDA of USD 410.8 million was below capital expenditure of USD 434.3 million, and cash fell. Three things decide the outcome: whether idle drillships keep returning to work at higher day rates, how the combination treats the USD 1,100.0 million of notes, and whether ARO draws on Valaris cash. Confidence is Medium.

### Key findings

- Liquidity is the anchor. Valaris held cash of USD 525.1 million and an undrawn USD 375.0 million revolver at September 30, 2026, giving liquidity of USD 900.1 million. The only debt is USD 1,100.0 million of 8.375% second lien notes due April 30, 2030, and the revolver matures April 3, 2028 with nothing drawn. The notes' fair value of USD 1,125.2 million exceeded their principal, which does not point to market stress.
- Earnings fell and then turned. Adjusted EBITDA, the company's own measure, was USD 642.2 million in FY2025 and USD 410.8 million over the last twelve months to Q3 2026, but USD 150.6 million in Q3 2026 against USD 96.5 million in Q2 2026. Gross leverage on principal moved from 1.71x to 2.68x and net leverage from 0.78x to 1.40x. The latest quarter is the strongest of the last four, so the last-twelve-months ratios overstate the current run rate, though the sources give no forecast.
- Spending outruns cash flow. Nine-month 2026 operating cash flow of USD 155.3 million did not cover capital expenditure of USD 328.0 million, and the 2026 capital expenditure guidance is USD 445.0 million to USD 470.0 million. Operating cash flow less capital expenditure was USD -206.8 million over the last twelve months. The guidance describes maintenance and upgrade projects including contract-specific work, so part of the spending should earn revenue as rigs start work, but it is funded from cash until then.
- The takeover is the main unknown. Transocean Ltd. will acquire Valaris by share exchange, with closing expected on or about December 1, 2026. The sources do not state whether closing triggers the notes' change-of-control repurchase offer at 101.0%, whether the notes and revolver stay in place, or what the combined capital structure is. Until closing, the agreement restricts new debt, dividends and repurchases.
- Covenant headroom cannot be judged. The revolver carries minimum equity to total assets, minimum interest coverage and minimum liquidity tests with no printed level or reported figure. The company states only that it was in compliance in all material respects.
- ARO is an off-balance-sheet claim on liquidity. Valaris holds notes receivable from ARO with a carrying value of USD 363.4 million that mature in 2027 and 2028 and are subordinated, and it may have to fund ARO newbuilds up to about USD 1.1 billion. ARO had cash of USD 32.1 million and has never paid a distribution.
- Contracted revenue gives visibility but not certainty. Backlog was USD 4,750.1 million at November 2, 2026, concentrated in a few customers, and contracts can be terminated for convenience or if a customer fails to reach a final investment decision.

### Strengths and weaknesses

Strengths.

- Strong liquidity relative to debt service (Documentary Fact; basis: liquidity of USD 900.1 million, cash and revolver figures in the financial base view). Mechanic: cash and an undrawn revolver cover the scheduled interest of about USD 92.1 million a year and 2026 capital spending shortfalls without market access. Implication: low near-term default risk on the standalone figures.
- A short, simple maturity profile (Documentary Fact; basis: debt table and maturities in the financial base view). Mechanic: one note series, no principal before 2030, revolver undrawn. Implication: no principal falls due before 2030, ignoring the combination.
- Contracted revenue visibility (Documentary Fact for backlog; Management Language for the outlook; basis: backlog and operating model rows in the business context). Mechanic: signed day rate contracts and rising drillship day rates support operating cash flow as idle rigs return to work. Implication: supports recovery of earnings, subject to termination rights.
- Restrained shareholder behaviour (Documentary Fact; basis: governance rows). Mechanic: no dividends, no repurchases in 2026, and the combination agreement bars both until closing. Implication: no documented leakage of cash to shareholders.

Weaknesses.

- Negative free cash flow (Documentary Fact; basis: USD -206.8 million last twelve months, USD -172.7 million nine months 2026). Mechanic: upgrade spending is front-loaded against revenue. Implication: cash declined from USD 599.4 million to USD 525.1 million, so the liquidity cushion is being used.
- Earnings trough and idle capacity (Documentary Fact; basis: Adjusted EBITDA and utilization figures). Mechanic: floater utilization of 58% in Q3 2026 means rigs carry cost without revenue. Implication: leverage of 2.68x is above the FY2025 level of 1.71x and sensitive to timing of contract starts.
- Customer concentration and contract terms (Documentary Fact; basis: customer and contract rows). Mechanic: five customers were 49% of FY2025 revenues and some contracts can be ended for convenience. Implication: a single loss would reduce the visibility that supports leverage.
- ARO exposure (Documentary Fact; basis: ARO rows). Mechanic: subordinated notes receivable, newbuild funding commitment and ARO's low cash. Implication: a contingent call on cash outside the debt figure.
- Transaction uncertainty (Insufficient Information on creditor terms; basis: transaction rows). Mechanic: change-of-control terms, covenant tests and capital structure after closing are not supplied. Implication: the standalone view may be superseded; this limits confidence to Medium.
- Covenant and ratings opacity (Insufficient Information; basis: covenant gap). Mechanic: levels, definitions and ratings are not supplied. Implication: availability of the revolver under stress cannot be tested.

### Credit assessment

| Assessment | Category | Confidence | Limitation |
| --- | --- | --- | --- |
| Moderate standalone credit risk: low near-term liquidity and refinancing risk, moderate and recently higher leverage, negative free cash flow, and a pending takeover with undisclosed creditor terms | Analyst Interpretation | Medium | Covenant levels, ratings, the combination agreement and Transocean's capital structure are not supplied; upstream readiness for this module is limited, not full |

### Thesis

Valaris Ltd can service its debt from cash and an undrawn revolver while its drillship fleet returns to work at higher day rates, but the pending Transocean combination and ARO funding obligations mean creditors cannot rely on the standalone figures alone.

Category: Analyst Interpretation. Basis: liquidity, maturity, leverage and cash flow figures in the financial base view; transaction and ARO rows in the business context.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Treatment of the notes and revolver in the Transocean combination | Change-of-control repurchase offer at 101.0% may or may not be triggered; interim covenants limit new debt; combined capital structure is not supplied | Post-closing leverage, security and covenants are unknown; the standalone credit may be replaced | Critical |
| Cash consumption by upgrades while earnings recover | Capital expenditure above operating cash flow in 2026; guidance of USD 445.0 million to USD 470.0 million | Liquidity falls if contract starts slip or day rates fall | Material |
| Covenant headroom unassessable | Three financial covenants on the revolver with no printed level; compliance stated only in general terms | Revolver availability under stress cannot be tested; the revolver is USD 375.0 million of the USD 900.1 million of liquidity | Material |
| ARO funding and note recovery | Newbuild commitment up to about USD 1.1 billion; subordinated notes receivable; ARO cash of USD 32.1 million | A call on Valaris liquidity outside reported debt, or delayed repayment of the notes receivable | Material |
| Customer concentration and termination rights | Top customers hold a large share of revenue; termination for convenience and FID contingency | Backlog of USD 4,750.1 million is less firm than it appears | Material |
| Middle East conflict | Operating income reduced by about USD 62.0 million in nine months 2026 through delays and war-risk insurance | Wider hostilities could raise cost and cause downtime for jackups and ARO | Material |
| Quality of reported equity | Deferred tax assets of USD 1,298.9 million depend on future taxable income | The equity to total assets covenant may be less comfortable than book values suggest if deferred tax assets were impaired | Minor |

### Evidence trace

| Claim | Basis | Locator |
| --- | --- | --- |
| Liquidity 900.1; cash 525.1; revolver 375.0 undrawn; no principal before 2030 | Financial base view: liquidity chart, maturities chart | 10-Q Q3 page:9, page:22, page:51 |
| Notes fair value 1,125.2 against principal 1,100.0 | Financial base view: capital structure | 10-Q Q3 page:17 |
| Adjusted EBITDA 642.2, 410.8, 150.6 and 96.5; leverage 1.71x, 2.68x, 0.78x, 1.40x | Financial base view: chart data, calculations | Q3 release page:11 |
| Operating cash flow 155.3, capital expenditure 328.0, free cash flow -206.8 | Financial base view: financials table | 10-Q Q3 page:10 |
| Capital expenditure guidance 445.0 to 470.0 | Financial base view: liquidity section | 10-Q Q3 page:52 |
| Combination terms, interim covenants, change-of-control silence | Business context: transaction summary | 10-Q Q3 page:11, page:12; 10-K page:24, page:127 |
| Covenants named, no level | Financial base view: covenants | 10-K page:129 |
| ARO exposure | Business context: ARO table | 10-Q Q3 page:54, page:55, page:56 |
| Customers and termination rights | Business context: operating model | 10-K page:10, page:11 |
| Middle East impact 62.0 | Business context: operating model | 10-Q Q3 page:34 |
| Deferred tax assets 1,298.9; realization depends on future taxable income | Supplementary check against sources, not in upstream figures | 10-Q Q3 page:9; 10-K page:141 |

## Calculations

All inputs are US$m from the upstream handoffs unless marked as a supplementary source check.

1. Q4 2026 cash outlay before operating inflows (indicative, not a forecast). Remaining 2026 capital expenditure from guidance: 445.0 - 328.0 = 117.0 and 470.0 - 328.0 = 142.0. Scheduled October 30, 2026 coupon: 1,100.0 x 8.375% / 2 = 46.1 (from the financial base view). Outlay = 117.0 + 46.1 = 163.1 to 142.0 + 46.1 = 188.1. Cash after these outlays and with no operating cash flow, asset sale proceeds or merger costs: 525.1 - 163.1 = 362.0 to 525.1 - 188.1 = 337.0. Adding the undrawn revolver: 362.0 + 375.0 = 737.0 to 337.0 + 375.0 = 712.0. Q3 2026 operating cash flow was 67.2, which is excluded here. Whether the coupon was paid is not stated in the sources.
2. Adjusted EBITDA less capital expenditure: last twelve months to Q3 2026, 410.8 - 434.3 = -23.5; nine months 2026, 313.8 - 328.0 = -14.2; FY2025, 642.2 - 343.5 = 298.7. Inputs are from the financial base view.
3. Notes fair value over principal at September 30, 2026: 1,125.2 - 1,100.0 = 25.1; 1,125.2 / 1,100.0 = 102.3% of principal. Quoted prices are Level 1 inputs per the filing. The redemption price schedule is 104.188% until April 30, 2027 and 102.094% from then until April 30, 2028 (financial base view).
4. Cash fall: 599.4 - 525.1 = 74.3 from December 31, 2025 to September 30, 2026. Over the same nine months operating cash flow was 155.3, capital expenditure 328.0 and asset sale proceeds 102.6.
5. ARO capacity comparison: the maximum funding commitment of about 1.1 billion exceeds liquidity of 900.1 at September 30, 2026. This is a maximum under the Shareholder Agreement, not an expected call.
6. Supplementary source check, equity to total assets (the first covenant named, level Not supplied): total Valaris shareholders' equity 3,271.0 / total assets 5,482.5 = 59.7% at September 30, 2026 (10-Q Q3 page:9); 3,169.6 / 5,304.8 = 59.7% at December 31, 2025. These are reported book values; the covenant definition may differ. Deferred tax assets 1,298.9 are 23.7% of total assets at September 30, 2026 (1,298.9 / 5,482.5). The 10-K states that realization of substantially all deferred tax assets depends on future taxable income (10-K page:141).

## Gaps

| Gap | Severity | Affected use | Action |
| --- | --- | --- | --- |
| Treatment of the notes, revolver and change-of-control provision in the Transocean combination not supplied; the business context records the combination agreement as Not supplied | Critical | Post-closing credit view | Obtain the Business Combination Agreement, scheme document and Transocean's filings |
| Covenant levels, definitions and reported figures not supplied | High | Revolver availability, liquidity under stress | Obtain the 2028 Credit Agreement and compliance disclosures |
| Transocean capital structure not supplied | High | Combined credit profile | Obtain Transocean's filings |
| Ratings and market prices not supplied (context empty) | Low | Pricing context; no rating-based view possible | Keep Not supplied |
| Cash interest paid for 2026 not supplied | Medium | Cash interest cover on a last-twelve-months basis | Use accrual basis, labelled, until supplied |
| Cash balance after September 30, 2026, including the October 30, 2026 coupon, not supplied | Medium | Current liquidity | Obtain later filings |
| ARO standalone statements not supplied | Medium | ARO exposure | Obtain ARO statements |
| Backlog by year at November 2, 2026 not supplied | Medium | Revenue visibility | Obtain backlog schedule from the next filing |
| Upstream signals: the business context judged this module READY_WITH_LIMITATIONS, not ready, and logs High gaps on the combination documents and Transocean's statements | High | Confidence is held below High | Restated here; resolve through the first two actions above |
| Contract-level terms and customer credit quality not supplied | Medium | Revenue durability | Obtain contract disclosures |

## Next module

- CP-5: trace the claims in the key findings and strengths and weaknesses to the financial base view and the business context. Check that the liquidity, leverage and cash flow figures match the financial base view exactly. Carry the supplementary source check (equity to total assets and deferred tax assets) as a figure that is not in the upstream handoffs.
- Any later committee work: carry the Critical gap on the combination and the covenant gap as restrictions on every conclusion above.
