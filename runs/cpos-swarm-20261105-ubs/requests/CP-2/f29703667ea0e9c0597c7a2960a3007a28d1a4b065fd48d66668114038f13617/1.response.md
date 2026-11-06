# CP-2 fundamental credit synthesis: UBS Group AG (ubs)

## Request

UBS Group AG (issuer id `ubs`), as of 2026-11-05 (information cutoff 2026-11-05), pathway credit_snapshot, reporting currency USD. The scope is the fundamental credit view from the reported financial base and the business and transaction context, for a creditor of the group. Prohibited and not done: peer ranking, instrument recommendation and any expected recovery outcome.

## Sources

Issuer sources relied on (pinned `.jsonl` text; locators are `page:N` extraction chunks). The credit view rests on the upstream handoffs below; the issuer sources were opened to check the capital requirements, the Swiss proposals and the funding notes cited in this handoff.

| Source | sha256 | Used for |
| --- | --- | --- |
| 20-F_2025-12-31_ubs-20251231.htm.jsonl | c65ff0a03ee3c3df685c628425c6a0a7856867141560663149d32b58774d8f33 | Capital requirements and eligible capital (page:229), liquidity (page:245, page:246), Swiss proposals (page:88, page:89), resolution strategy (page:84), debt notes (page:432, page:433), maturity table (page:497, page:498) |
| 6-K_2026-03-31_edgarq1q26kubsgroupagc.htm.jsonl | 5ae425915ce6d8540a2dcbe4beb8ed52f974546cb1a0a776687e74bfb6a0ae6d | Debt issued and equity at 31.3.26 |
| 6-K_2026-03-31_investorpresotext2026.htm.jsonl | 84e6720eb0ad0ada288bec163d56547d8305bba53a01f71c7fcd5a3acd94f71a | First quarter 2026 management statements |
| 6-K_2026-06-30_investorpresotext2026.htm.jsonl | 671f7dde67986089a1c17da85500334fa96b51697d1642480c22e2b5d6422aa1 | Second quarter 2026 management statements |
| 6-K_2026-07-29_edgarq2q26kubsgroup.htm.jsonl | 88627f5322eed51bd548e2eb9daaa4bff0f8cc654e252b054c4865eeda3901ea | Debt issued and equity at 30.6.26 |
| 6-K_2026-09-30_edgar3q26kubsgroupc.htm.jsonl | faea893d4d4d07cf7975acc81d8e41156e0b136d2c529429a6c83f334ac28864 | Debt issued and equity at 30.9.26 |
| 6-K_2026-09-30_investorpresotext2026.htm.jsonl | 2ac25318ab8710edaece00656540a1c90de7efab36a24b488600ed02e222986e | Third quarter 2026 management statements |
| context | a67d394ad1fe0320e0c68be1bf7ef2da619705355c7aa8f5e62b6171bbf4fb2d | Run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2e54133f1b22d47b492e44c16bd40091878fdaaf285f1d8de08cc5d1ee03cf43 | Source limits: no quarterly reports, slides or audit-opinion text |
| CP-1 | 685fa8e5832878fa7692e257450c83b45286cefc7233978ce033b37754932207 | Reported financial base, capital, liquidity and debt figures |
| CP-1A | 7fa4d371e764e1152820b84955958152894dccaa744ff170272babe7d2e99475 | Business, ownership, transaction, governance behaviour and Swiss capital context |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| UBS Group AG looks like a strong, well-capitalized and liquid bank credit. Its main risks come from the pending Swiss capital rules and legacy litigation, not from weak earnings or debt service. | Medium | Interim 2026 statements and instrument terms are missing, and the Swiss rule outcome is unresolved. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Capital and loss-absorbing capacity sat well above Swiss requirements at the end of 2025. | A large buffer lowers near-term default risk and gives room to absorb losses before senior creditors are affected. | High |
| Liquidity is large against near-term debt maturities. | High-quality liquid assets exceed debt due within 12 months by a wide margin, which lowers refinancing risk. | Medium |
| The Swiss capital package could require around USD 22bn of extra CET1 at the bank subsidiary. | Distributions may slow or structure may change; the size is a company estimate and the final rules are unknown. | Medium |
| Operating profit rose about 30% in 2025, and management reports an underlying cost / income ratio of 68.7% for the third quarter of 2026. | Stronger earnings build capital, but 2026 results are rounded management statements with no interim statements. | Medium |

### Credit view

UBS Group AG is, on the evidence supplied, a strong and well-capitalized bank credit whose main risks are regulatory and legacy rather than earnings or liquidity. The strongest support is capital and liquidity: at 31 December 2025 CET1 capital was USD 71,262 million, 14.44% of risk-weighted assets against a Swiss requirement of 10.63%; the liquidity coverage ratio averaged 182.6% in the fourth quarter of 2025; and management reports a CET1 ratio of 14.7% at 30 September 2026. The weakest point is the Swiss capital package, which the company estimates would need around USD 22bn of extra CET1 at UBS AG, alongside unquantified Credit Suisse litigation. The outcome turns on the final Swiss rules and on how management balances buybacks against capital building.

### Key findings

First, capital is the anchor of the view. At 31 December 2025 eligible CET1 capital of USD 71,262 million exceeded the Swiss requirement of USD 52,448 million by USD 18,814 million, and eligible going concern capital of USD 91,176 million exceeded its requirement of USD 73,955 million by USD 17,221 million (Documentary Fact; 20-F page:229). Gone concern loss-absorbing capacity of USD 96,130 million exceeded its requirement of USD 52,917 million by USD 43,213 million (same page). On the leverage basis the cushions are thinner: CET1 of 4.39% of the leverage ratio denominator against 3.50%, and going concern capital of 5.62% against 5.00%. The mechanism is that losses are absorbed by CET1 and additional tier 1 before subordinated and senior unsecured creditors, so these cushions are the first protection for debt holders (Analyst Interpretation).

Second, funding and liquidity reduce refinancing risk. Customer deposits were USD 788,367 million at 31 December 2025, about 49% of total assets of USD 1,617,427 million, and loans and advances to customers were about 83% of deposits. High-quality liquid assets averaged USD 331.6 billion in the fourth quarter of 2025 and the liquidity coverage ratio was 182.6% against a floor of 100%, with USD 51.8 billion of assets excluded from the group figure as restricted in subsidiaries. Debt issued at amortized cost and fair value due within 12 months was USD 113.7 billion on an undiscounted basis including interest, which is below high-quality liquid assets by a factor of about 2.9 (Analyst Interpretation; a simple comparison, not a regulatory measure). Management reports a liquidity coverage ratio of 179% and a net stable funding ratio of 115% for the third quarter of 2026 (Management Language, rounded, averaging basis not stated).

Third, earnings are recovering from a low base but remain market-sensitive. Operating profit before tax was USD 8,853 million in FY2025 against USD 6,821 million in FY2024, an increase of about 30%, and net interest income was only USD 7,747 million of USD 49,573 million total revenues, so about 84% of revenue is non-interest income from fees and trading (Documentary Fact; 20-F page:371 and page:409). The reported cost / income ratio was 81.1% in FY2025. Management says the underlying ratio was 68.7% in the third quarter of 2026 and targets below 70% at the 2026 exit (Management Language, not reconciled in the pack). Because fee and trading income move with markets, profit and capital generation are exposed to market conditions, which weakens earnings-based protection but is cushioned by the capital above (Analyst Interpretation).

Fourth, the Swiss capital package is the largest identified risk. The 20-F states the company estimates UBS AG would need additional CET1 of around USD 22bn if all measures were implemented as proposed, which would raise the group CET1 ratio to around 18.5% from its target of around 14%, with a phase-in starting in 2028 at the earliest (Documentary Fact; 20-F page:88 and page:89). Management calls the September 2026 Upper House outcome very concerning (Management Language). The mechanism, in management's words, is that the capital would be trapped against foreign subsidiary investments, so it cannot support distributions or growth. The implication for creditors is mixed: a higher requirement strengthens loss absorption, but it can also reduce shareholder returns and prompt structural change whose effect on creditors is not assessable from the pack (Insufficient Information).

Fifth, legacy exposures and resolution mechanics matter for the holding company's creditors. The 20-F describes a single point of entry resolution strategy at UBS Group AG involving write-down of equity, AT1 and tier 2 and conversion of senior unsecured bonds of UBS Group AG to equity if required, and records Credit Suisse AT1 litigation in which UBS Group AG is a party as successor (20-F page:84 and page:113). Provisions for litigation, regulatory and similar matters were USD 2,200 million and acquisition-related contingent liabilities USD 531 million at 31 December 2025, and management says an appeal decision on the AT1 case is not expected before the first quarter of 2027. These are mechanics, not outcomes: no claim amount is supplied.

Sixth, the integration is near completion, which should lower execution risk, but this is management's claim. Cumulative gross cost savings reached USD 13.2 billion by the third quarter of 2026 on management's figures, against USD 10.7 billion at the end of 2025, and Non-core and Legacy still reported a litigation charge of USD 275 million in the third quarter (Management Language; Q3 call).

### Strengths and weaknesses

Strengths. A capital base well above requirements on all three Swiss measures (Documentary Fact), with management guiding to a CET1 ratio of around 14%. A deposit-led balance sheet with large high-quality liquid assets and a liquidity coverage ratio of 182.6% (Documentary Fact). A diversified revenue base across five divisions and four regions, with Switzerland at 32% of FY2025 revenue and the Americas at 36% (Documentary Fact). Earnings that improved in FY2025 and, on management's account, in 2026 (Documentary Fact and Management Language). No sponsor or controlling holder is disclosed, so sponsor extraction is not an evident risk (Analyst Interpretation; the evidence is an absence in a limited pack).

Weaknesses. Dependence on one regulator's rule change: the company estimate of around USD 22bn of extra CET1 at UBS AG is large against CET1 capital of USD 71,262 million for the group (Documentary Fact for the estimate, Analyst Interpretation for the scale). Unquantified legacy litigation and an acquired-risk tail (Documentary Fact). Earnings that depend on fees and trading, with a reported cost / income ratio of 81.1% in FY2025 (Documentary Fact). Management plans to release the integration capital buffer from 2027 and continue buybacks, with USD 4.8 billion repurchased in 2026 to the third quarter and USD 1.2 billion more intended, and says it can build capital later from earnings (Management Language). The group's holding-company debt sits in the resolution path described above; terms by instrument are Not supplied (Insufficient Information).

Thesis. UBS Group AG's high capital and liquidity buffers support a strong credit view today, and the unresolved Swiss capital rules and legacy litigation, not near-term liquidity or debt service, are what could weaken it.

### Credit assessment

| Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- |
| Fundamental credit view: strong, well-capitalized, liquid; main risks regulatory and legacy | Analyst Interpretation | Medium | Capital and liquidity ratios (financial base handoff, 20-F page:229, page:246); Swiss proposals (20-F page:88, page:89); governance behaviour (business context handoff); confidence is Medium because 2026 interim statements, instrument terms and ratings in force are missing |
| Business risk: diversified fee-led model, near-complete integration, no sponsor | Analyst Interpretation | Medium | Business context handoff: segment mix, geography, timeline, ownership |
| Financial risk and liquidity: strong buffers, market-sensitive earnings | Analyst Interpretation | Medium | Financial base handoff; FY2025 audited, 2026 attributed and rounded |

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Swiss capital rules on foreign subsidiary investments | Deduction of investments from CET1 traps capital; company estimates around USD 22bn at UBS AG (20-F page:89) | Can cut distributions or force structural change; effect on creditors depends on final rules and timing | Material |
| Credit Suisse legacy and AT1 litigation | UBS Group AG is party as successor; provisions USD 2,200 million plus contingent liabilities USD 531 million at 31 December 2025 (20-F page:434) | Cash cost and capital use could exceed provisions; amounts beyond provisions are not supplied | Material |
| Market-dependent earnings | About 84% of FY2025 revenue is non-interest income (20-F page:409) | Earnings and capital generation fall in weak markets | Material |
| Capital return pace | USD 4.8 billion repurchased to the third quarter of 2026 and 1.2 billion more intended; integration buffer released from 2027 (Q3 call) | Distributions compete with building capital for the Swiss rules | Material |
| Holding-company loss absorption | Single point of entry strategy writes down equity, AT1 and tier 2 and converts senior unsecured bonds of UBS Group AG if required (20-F page:84) | Holding-company instruments sit in the loss-absorption path; instrument terms are not supplied | Material |
| Integration completion | Savings and decommissioning are management claims to year-end 2026 | Delay would raise costs and operational risk; evidence is not yet filed | Minor |
| Liquidity ratio drift | Fourth-quarter liquidity coverage fell to 182.6% from 188.4% a year earlier (20-F page:246) | Remains well above the 100% floor | Minor |

## Calculations

| Id | Calculation | Inputs | Result | Check |
| --- | --- | --- | --- | --- |
| C1 | CET1 headroom, risk-weighted basis | 71,262 - 52,448 | 18,814 USD m | 20-F page:229; ratio 14.44% less 10.63% is 3.81 percentage points |
| C2 | Going concern headroom | 91,176 - 73,955 | 17,221 USD m | 20-F page:229; ratio 18.48% less 14.99% is 3.49 percentage points |
| C3 | Gone concern headroom | 96,130 - 52,917 | 43,213 USD m | 20-F page:229; ratio 19.48% less 10.73% is 8.75 percentage points |
| C4 | Leverage basis cushions | CET1 4.39% less 3.50%; going concern 5.62% less 5.00% | 0.89 and 0.62 percentage points | 20-F page:229 |
| C5 | Company capital estimate against group capital | 22,000 / 493,397 risk-weighted assets | 4.46 percentage points | 14 + 4.46 = 18.46, consistent with the company's around 18.5% (20-F page:89); also 22,000 / 71,262 = 30.9% of CET1 capital |
| C6 | Phase-in steps | 65% rising by 5 points a year to 100% | 7 steps | 20-F page:88 |
| C7 | Deposit share of assets | 788,367 / 1,617,427 | 48.7% | Financial base handoff, 20-F page:373 |
| C8 | Loans to deposits | 653,846 / 788,367 | 82.9% | Financial base handoff |
| C9 | Debt due within 12 months, FY2025 | amortized cost 65.3 + fair value 48.4 USD bn | 113.7 USD bn | 20-F page:497; undiscounted, includes interest; from bn buckets to one decimal |
| C10 | High-quality liquid assets against 12-month debt | 331.6 / 113.7 | 2.9 times | Simple comparison; the two are on different bases |
| C11 | Operating profit growth | (8,853 - 6,821) / 6,821 | 29.8% | 20-F page:371 |
| C12 | Non-interest share of revenue | 41,826 / 49,573 | 84.4% | 20-F page:409 |
| C13 | Liquidity coverage headroom | 182.6% less 100% | 82.6 percentage points | 20-F page:246 |
| C14 | Repurchase consistency (management, billion) | 4.8 + 1.2 | 6.0 | Q3 call; equals two 3.0 programmes if the first was executed in 2026 |
| C15 | Cost savings path (management, billion) | 10.7 + 0.8 + 1.1 + 0.6 | 13.2 | Q1, Q2 and Q3 calls; matches the stated 13.2 |

Not calculable: EBITDA-based leverage and interest cover, net debt, facility liquidity, any ratio from 2026 statements, and any recovery measure.

## Gaps

| Gap | Why it matters and what it affects | Severity | Action |
| --- | --- | --- | --- |
| No 2026 interim financial statements, only capitalization tables and call transcripts; 2026 figures are rounded and partly underlying | Limits confidence in the current-period view to Medium; affects earnings, capital and liquidity for Q3 2026 | High | Obtain the first, second and third quarter 2026 reports and slides |
| Instrument-level debt terms (issuer, ranking, coupon, maturity, call, guarantor) and the Q3 2026 liability management terms | Prevents any statement about ranking, maturity wall or treatment of particular creditors | High | Obtain prospectus supplements, capital instrument lists and the transaction announcement |
| Swiss capital rule text and final timing; company estimate is the only size marker | Decides the largest risk; scale and timing cannot be tested | High | Obtain the proposals and parliamentary outcome |
| Credit Suisse litigation amounts, including AT1 and merger-law claims | Cash and capital cost beyond provisions unknown | Medium | Obtain litigation notes and filings |
| Ratings in force at the as-of date | Ratings affect funding cost and collateral triggers; only 2025 actions are known | Medium | Obtain agency reports |
| Readiness of this module was judged limited upstream: the business context handoff rates it ready with limitations, and the source readiness handoff notes missing quarterly reports, slides and audit-opinion text | Confidence is below High; this restates the upstream limitation once | Medium | Resolve the gaps above |
| Events from 30 October 2026 to 5 November 2026 | Latest source is dated 29 October 2026 | Low | Obtain later filings |

## Next module

- The credit view, key findings and risk table are ready for CP-5 evidence review. CP-5 should test the Swiss capital estimate, the capital headroom calculations and each management-language item, and should carry the missing 2026 statements and instrument terms as restrictions.
