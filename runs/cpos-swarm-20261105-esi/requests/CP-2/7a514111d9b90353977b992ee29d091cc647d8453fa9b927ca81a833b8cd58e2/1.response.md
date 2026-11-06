# CP-2 — Fundamental credit synthesis: Element Solutions Inc (esi)

## Request

- Issuer: Element Solutions Inc (issuer id `esi`, NYSE: ESI), as of 2026-11-05, information cutoff 2026-11-05; pathway `credit_snapshot`, reporting currency USD, current period Q3 2026.
- Scope: the fundamental credit view, with the strengths, weaknesses, findings, risks and gaps that drive it, built only from the CP-0, CP-1 and CP-1A handoffs; it fills "Key findings" and "Strengths and weaknesses".
- Execution: host session; this synthesis quotes no source text, makes no peer ranking, instrument recommendation or recovery conclusion, and no provider was called.

## Sources

Issuer sources pinned for this run (read by the upstream modules, not quoted here):

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_esi-20251231.htm.jsonl | e419be4a34b86cf3946781c81c9cf5167d1ce55ea947acb2e97a22e3ec33fbdc |
| 10-Q_2026-03-31_esi-20260331.htm.jsonl | 71ffb0652af7e069b88fd66093decc7d627d9409b00bd185ac2a68db72c238da |
| 10-Q_2026-06-30_esi-20260630.htm.jsonl | 9e356702c38010063835ed61e96bcc033abb0f0a3a4b5a9a1845d764f0bcd2b7 |
| 10-Q_2026-09-30_esi-20260930.htm.jsonl | 1efce58ae7d1707b81e096f97ecf01dbf0104d1e81a25b95db794dfd861b04fe |
| EX-99.1_2026-04-28_aearningsreleaseex99120263.htm.jsonl | cb75b2ab3988a8e0ad3f68546b2df2a55172fd4900de7f7f14ec3436aa37dbbf |
| EX-99.1_2026-07-27_aearningsreleaseex99120266.htm.jsonl | c0a4eea4343eb189f65a5cb896e49cd67b1e5c372bfce79bfb18a89241f92f7e |
| EX-99.1_2026-10-21_aearningsreleaseex99120269.htm.jsonl | b36d51c2a20c56990c8361f520b238bac0611bf5a7dab66ba03c7922169d0001 |
| context | 1920ec84f7b9710e00bbaac803890d2695813e40c10637e35f2e7d8eaaf0285a |

Supplied handoffs consumed:

| Module | sha256 | Used for |
| --- | --- | --- |
| CP-0 | cdece14e2edef04df25761198b67e4d3c88f681db7a403c096bd0cf0d6bf17b7 | Readiness and restrictions: READY_WITH_LIMITATIONS for this module; Credit Agreement, indenture, Termination Agreement and events after October 22, 2026 not supplied |
| CP-1 | 0b784e0bff14bdc1d3f4b3894b4edcc8e5b0011eb0edb677c3ca72eb727a1ab8 | All figures: LTM and FY2025 metrics, leverage (C4), coverage (C5), free cash flow (C6), liquidity (C7), maturities, covenant text and the indicative first lien ratio (C12) |
| CP-1A | 422555478447d0a1f1c0dd50ad2be4b03b7ccdf29dc45553ba61539020c648b5 | Business rows, segment and metals dependence, the Solstice merger and its termination, financing of the 2026 acquisitions, governance behaviour, conflicts, credit translations |

Upstream status: all three accepted. Inherited limitations: CP-1A rates this module "Ready with limitations" because the termination terms, credit documents and ratings are not supplied; CP-1 rates covenant headroom Not calculable and states that LTM Adjusted EBITDA is not pro forma for the acquisitions.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Element Solutions has moderate reported leverage of 3.09x, strong earnings growth, cash interest cover of 7.85x and adequate liquidity of USD 702.9 million. Debt-funded acquisitions raised leverage, and cash conversion is weaker than earnings. | Medium | Covenant definitions, the terminated merger's terms and pro forma EBITDA for the acquisitions are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt rose to USD 2,082.1 million from USD 1,625.9 million after two acquisitions, lifting net leverage to 2.76x from 1.83x. | Leverage is above FY2025 but falling as earnings arrive, from 3.71x total at Q1 2026, leaving less room for further debt-funded deals. | High |
| Adjusted EBITDA reached USD 673.1 million over the last twelve months, but cash conversion fell as metals prices tied up working capital. | Earnings growth supports debt service only if cash flow follows; free cash flow was USD 182.9 million. | Medium |
| The first large maturity is USD 800.0 million of senior notes due September 1, 2028, above liquidity of USD 702.9 million. | Repayment relies on cash generation or refinancing, with time to act. | Medium |
| Electronics is 78.3% of net sales, and pass-through metals are 40.9% of its sales. | Earnings follow electronics demand and metals prices, so downturns and price swings affect coverage together. | Medium |
| The only covenant located is a springing 5.0 to 1.0 first lien test, with the revolver USD 15.0 million drawn. | The test is far from binding on disclosed figures, but its definitions are not supplied. | Medium |

### Credit view

Element Solutions is a specialty chemicals credit with moderate reported leverage that rose in 2026 and is still serviced comfortably. The strongest support is coverage and liquidity: Adjusted EBITDA of USD 673.1 million over the last twelve months covers cash interest paid of USD 85.7 million 7.85 times, and cash plus undrawn revolver is USD 702.9 million with no maturity before September 2028. The weakest point is the 2026 acquisition year: debt of USD 2,082.1 million is 3.09x LTM Adjusted EBITDA, cash conversion lagged earnings, and earnings depend on electronics demand and metal prices. What decides the outcome is whether earnings growth turns into free cash flow that reduces net leverage of 2.76x before the USD 800.0 million notes mature, and whether shareholder returns stay modest. [CP-1 C4, C5, C7; CP-1A transaction and governance rows]

- Category: Analyst Interpretation, based on CP-1 figures and CP-1A Documentary Fact rows.
- Confidence: Medium. The reported figures reconcile, but covenant definitions, termination terms and pro forma EBITDA are missing, and CP-1A rates this module Ready with limitations.

Thesis: Element Solutions can service its debt from growing earnings with adequate liquidity and a distant first maturity, but 2026 acquisitions lifted leverage, cash conversion is thinner than earnings, and unverified add-backs and covenant terms limit how much comfort the reported ratios give.

### Key findings

1. Leverage rose with the 2026 acquisitions. Total debt rose to USD 2,082.1 million at September 30, 2026 from USD 1,625.9 million at December 31, 2025, while cash fell to USD 224.9 million from USD 626.5 million, so net debt to LTM Adjusted EBITDA is 2.76x against 1.83x at FY2025 (CP-1 C4). Mechanism: EFC was paid from cash and Micromax from USD 450 million of add-on term loans plus revolver borrowings (CP-1A transaction summary), so gross debt rose while the acquired earnings enter LTM only from January 2 and February 2, 2026. Implication: LTM leverage overstates a full-year run rate and is falling as earnings arrive (3.71x at Q1 2026 to 3.09x), but the starting point is higher and the cushion for further debt-funded deals is smaller. Documentary Fact via CP-1; Analyst Interpretation on direction.
2. Coverage is strong. Adjusted EBITDA covers cash interest paid 7.85x and net interest expense 8.29x on the LTM basis (CP-1 C5), slightly below 7.98x on cash interest at FY2025. Mechanism: about 94% of debt is fixed through swaps and the 3.875% USD Notes due 2028, so higher floating rates have limited effect, although the euro-denominated swap legs add currency sensitivity (CP-1 debt register). Implication: low near-term debt service strain unless earnings fall sharply. Documentary Fact via CP-1.
3. Earnings are growing, but part of the growth is acquired or metals-driven. Nine-month 2026 Adjusted EBITDA of USD 536.8 million is above USD 411.3 million a year earlier (CP-1 C13), and quarterly Adjusted EBITDA rose each quarter of 2026. Reported Q3 2026 net sales growth of 52% compares with organic growth of 13% (CP-1), because acquisitions and pass-through metals pricing lifted reported sales (CP-1A operating rows). Mechanism: higher metal prices raise revenue and working capital without proportional profit, and gross margin fell to 34.4% from 42.2% (CP-1A A4). Implication: reported growth overstates underlying growth, and margin should be assessed on an ex-metals basis. Documentary Fact; Analyst Interpretation on quality.
4. Cash conversion lags earnings. Nine-month operating cash flow of USD 192.2 million was 35.8% of Adjusted EBITDA, against 48.3% in the same period of 2025, and below USD 198.7 million a year earlier despite higher earnings (CP-1 C13). Mechanism: receivables and inventories absorbed cash as metal prices rose; Q3 2026 alone produced USD 159.2 million after an outflow of USD 66.6 million in Q1 2026. Implication: free cash flow of USD 182.9 million LTM (CP-1 C6) is thinner than EBITDA suggests and is seasonal and metals-price dependent. Documentary Fact via CP-1.
5. Liquidity is adequate and the first maturity is distant, but larger than liquidity. Cash plus undrawn revolver is USD 702.9 million, of which USD 176 million of cash is held by foreign subsidiaries (CP-1 C7, narrative review). The USD 800.0 million of notes due September 1, 2028 exceed liquidity by USD 97.1 million (CP-1 C13), and term loans of USD 1,279.7 million mature on December 18, 2030. Implication: repayment depends on cash generation or refinancing, with about 22 months to act as at the as-of date; the first maturity is a monitoring point rather than a near-term constraint. Documentary Fact via CP-1.
6. The terminated Solstice merger leaves unanswered questions. A merger signed on July 6, 2026 was terminated on August 27, 2026 with a mutual release, and the Q2 10-Q disclosed a possible USD 376,000,000 termination fee in certain circumstances (CP-1A transaction summary). Whether any fee or cost arose is not stated, and the add-back for acquisition, integration and transaction expenses of USD 52.6 million for nine months 2026 may include process costs (CP-1). Implication: a potential cash cost is unquantified, and the change-of-control risk that would have applied is removed. Documentary Fact for the termination; Insufficient Information for any payment.
7. Shareholder returns and add-backs temper the quality of earnings. Dividends of USD 59.3 million and buybacks of USD 37.7 million in nine months 2026 total USD 97.0 million, with approximately USD 518 million of authorisation remaining (CP-1, CP-1A governance rows); Adjusted EBITDA adds back USD 37.1 million of 2025 executive share grants and USD 52.6 million of acquisition-related costs (CP-1 narrative review). Mechanism: discretionary distributions compete with debt reduction, and add-backs lift the earnings base that leverage ratios use. Implication: leverage tolerance should be read on cash earnings after these items; creditor limits on distributions are not supplied. Documentary Fact; Analyst Interpretation.
8. Covenant protection is thin on the facts supplied. The only financial covenant located is a springing first lien net leverage test of 5.0 to 1.0, applying when revolver borrowings exceed 30% of the USD 500.0 million commitment; USD 15.0 million is drawn (CP-1). The indicative first lien net leverage is 1.59x and USD 135.0 million of further drawing is possible before the test applies (CP-1 C12), but these are not covenant ratios. Implication: the facility offers little ongoing maintenance discipline while the revolver is lightly used, and headroom cannot be monitored without the Credit Agreement definitions. Documentary Fact; headroom Not calculable.

### Strengths and weaknesses

Strengths:

- Diversified, recurring customer base: no customer is 10% or more of net sales, products are consumed in customers' production, and the business serves electronics, semiconductor, automotive and offshore energy markets (CP-1A operating rows). This supports revenue durability, tempered by minimal order backlog. Documentary Fact.
- Earnings momentum and coverage: Adjusted EBITDA of USD 673.1 million LTM and cash interest cover of 7.85x (CP-1 C1, C5). Documentary Fact via CP-1; Adjusted EBITDA is an issuer non-GAAP measure.
- Liquidity and maturity profile: USD 702.9 million of cash and undrawn revolver, no maturity until the USD 800.0 million notes in September 2028, and about 94% of debt fixed (CP-1 C7, debt register). Documentary Fact via CP-1.
- Financial policy flexibility shown in 2025: USD 200 million of term loans prepaid with divestiture proceeds, and revolver borrowings repaid from USD 85.0 million at Q1 2026 to USD 15.0 million at Q3 2026 (CP-1A governance rows, CP-1). Documentary Fact.
- Reported compliance: the issuer states compliance with the Credit Agreement and indenture covenants at September 30, 2026 (CP-1 covenant table). Management Language; headroom is not verifiable.

Weaknesses:

- Higher leverage after acquisitions: 3.09x total and 2.76x net on LTM Adjusted EBITDA, not pro forma, with tangible stockholders' equity of negative USD 663.4 million after goodwill and intangibles (CP-1 C4, C11). Analyst Interpretation.
- Cash conversion and working capital: operating cash flow was 35.8% of Adjusted EBITDA for nine months 2026, and metals prices drive working capital (CP-1 C13, CP-1A operating rows). Analyst Interpretation.
- Concentration and cyclicality: Electronics is 78.3% of Q3 2026 net sales and 77.6% of segment Adjusted EBITDA, China is 21.9% of FY2025 net sales, and Specialties Adjusted EBITDA fell in Q3 2026 (CP-1A A1, A2). Documentary Fact; Analyst Interpretation on risk.
- Metals pass-through and margin: pass-through metals are 40.9% of Electronics sales and gross margin fell to 34.4% from 42.2% (CP-1A A3, A4). Documentary Fact.
- Acquisition integration and add-backs: purchase price allocations are preliminary, goodwill of USD 292.7 million was added, and Adjusted EBITDA excludes large acquisition and share-grant items (CP-1A, CP-1). Analyst Interpretation.
- Unverified legal protections: Credit Agreement, indenture and termination terms are not supplied. Insufficient Information; the missing datapoints are covenant definitions, restricted-payment capacity and any payment under the termination, and they matter for headroom and distributions.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Debt-funded acquisition strategy | Add-on term loans and revolver funded Micromax; further deals could add leverage before earnings catch up | Leverage tolerance narrows; a downturn would raise net leverage quickly | Material |
| Electronics and metals dependence | Electronics is the bulk of sales and profit, and pass-through metals inflate sales and working capital | Earnings, coverage and cash conversion fall together if demand or metal prices turn | Material |
| 2028 notes maturity | USD 800.0 million falls due above current liquidity | Refinancing or cash build is needed; market access risk grows as the date nears | Material |
| Shareholder distributions | Dividends and buybacks are discretionary and creditor limits are not supplied | Cash that could repay debt may leave the group | Minor |
| Quality of Adjusted EBITDA | Large add-backs and non-pro forma LTM make leverage ratios less comparable | Reported leverage may understate or overstate cash earnings | Minor |
| Covenant definitions unknown | A springing 5.0 to 1.0 test applies only above 30% revolver use; definitions not supplied | Headroom cannot be monitored | Minor |
| Terminated merger terms | Possible termination fee or costs not stated | Unquantified cash cost | Minor |

### Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Credit Agreement and indenture not supplied | Covenant headroom, incurrence capacity, restricted payments and change-of-control terms unknown | Covenant risk, governance capacity, key finding 8 | Material | Supply executed documents and add legal review |
| Termination Agreement and any payment not supplied | A possible USD 376,000,000 fee or other cost is unquantified | Key finding 6, liquidity | Material | Supply the August 27, 2026 Form 8-K and exhibit |
| Pro forma EBITDA for EFC and Micromax not supplied | LTM leverage is on a reported basis | Key findings 1 and 2, assessment confidence | Material | Obtain management pro forma or compliance certificate |
| Events after October 22, 2026 not supplied | Position at the as-of date may differ | Monitoring posture | Minor | Supply later filings or confirm none |
| No rating or market data | No external view of the credit | Not required for this scope | Minor | Add only if sourced |

## Calculations

No new calculation. Every figure refers to a CP-1 row or calculation ID (C1 to C13) or a CP-1A calculation (A1 to A7); the 22 months to the 2028 notes is counted from November 5, 2026 to September 1, 2028 and is a date count, not a financial figure.

## Gaps

- Material: the Credit Agreement and indenture, the Termination Agreement and any payment, and pro forma EBITDA for the acquisitions are Not supplied.
- Minor: events after October 22, 2026 are Not supplied; no rating or market data is in scope.
- Restrictions inherited: CP-1A rates this module Ready with limitations, so confidence is Medium rather than High.

## Next module

- CP-5: trace each finding to its CP-1 row or calculation and its CP-1A row, and check that the categories match the basis.
- Report delivery: "Key findings" and "Strengths and weaknesses" above; carry the Medium confidence and the Material gaps.
