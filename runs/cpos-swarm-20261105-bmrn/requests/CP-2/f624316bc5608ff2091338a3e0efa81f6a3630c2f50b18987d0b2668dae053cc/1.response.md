## Request

BIOMARIN PHARMACEUTICAL INC (issuer id bmrn), as of 2026-11-05, pathway credit_snapshot, reporting currency USD. This module synthesizes the fundamental credit view from the accepted CP-1 financial base and CP-1A business and transaction pack, reopened against the pinned sources. It gives no peer ranking, instrument recommendation or recovery conclusion.

## Sources

### Issuer sources relied on

Upstream handoffs are the evidence basis; the sources below were reopened to check the upstream figures that drive the view. The locator `page:N` is the extraction chunk, not the printed page.

| Source name | sha256 | Use in this handoff |
| --- | --- | --- |
| 10-K_2025-12-31_bmrn-20251231.htm.jsonl | ea07c0b0ced62ce928418e33e7850bb4f7657797e8c0bf5f5000905677fe1e06 | FY2025 base figures and 2027 Notes terms, checked for CP-1 |
| 10-Q_2026-03-31_bmrn-20260331.htm.jsonl | 2a99ceccd25eef82b99d8805175210aaa89ec2399f72c136d49401e8ef68101d | Pre-close position, checked for CP-1 and CP-1A |
| 10-Q_2026-06-30_bmrn-20260630.htm.jsonl | ab3790f631c592e337d10380a75780f5e20242f4c9bb7ba84f7627e0f0826177 | Six-month figures and debt at 2026-06-30, checked for CP-1 |
| 10-Q_2026-09-30_bmrn-20260930.htm.jsonl | d37c2b4920de3198d70881c8f1da80a4e23e61a15cd3750a74ed566c3cf812ae | Latest balance sheet (page:8-9), debt (page:22-25), customers and products (page:28-29), commitments (page:32-33), liquidity and covenants (page:45-52) |
| EX-99.1_2026-05-04_earningsrelease-4may26ex991.htm.jsonl | 4342224974b87cfa461fd3f7cf30a3f9e47704c85d4929187beb8b8d81373433 | Context only |
| EX-99.1_2026-08-06_earningsrelease-6aug26ex991.htm.jsonl | 5716fe1e56e2ba465f10bd50a733773a00cfbe4f0196fc4b254c96006e5e867a | Management leverage target and definition (page:3, page:10) |
| EX-99.1_2026-11-02_earningsrelease-2nov26ex991.htm.jsonl | 9fad7cb025a49338e77589bbc1ee8b206ca16d3ad7a77a9450a90d585d60fed5 | Updated guidance and management claims (page:1-5) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 91b63adad7def6728b9cd684c48c1a1c49d1718a8dc5d8773455a7dcffcc69fa | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | How used |
| --- | --- | --- |
| CP-0 | 519d600f8cd9aa5d9447d6aad10dd44114b4ff6da47448fda0a16df0ed1715f3 | Source readiness: READY_WITH_LIMITATIONS; limits inherited |
| CP-1 | d41e5dce10b446024674125b584c0280188e041e8a33a5bd9ae252b58ca0d70d | Financial base: chart data, financials table, debt register, claims outside debt, covenants |
| CP-1A | 783b4b19878ec71a213658a8fa97d74ff3ca9a78d49c68c463e5b0c4d487b0b6 | Business and transaction pack: operating model, concentration, Amicus funding, management leverage target, behaviour |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| BioMarin is a profitable, cash-generative rare-disease company that took on USD 4,235 million of debt for Amicus. Liquidity is adequate, but leverage on filed earnings is high and the true run-rate is unproven. | Medium | No combined earnings base, covenant ratios, executed legal documents or ratings are supplied, so leverage and covenant headroom cannot be pinned down. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Liquidity is USD 1,336.0 million, USD 736.0 million of cash plus an undrawn USD 600.0 million revolver, against USD 660.0 million of debt due within twelve months. | Near-term debt service looks covered, but the revolver depends on covenant compliance and the May 2027 convertible is the first test. | Medium |
| Leverage is 11.18x on filed trailing EBITDA and 4.59x on an analyst-adjusted basis; neither is pro forma for a full year of Amicus. | Leverage is elevated and its true level is uncertain; the covenant maximum is 3.50x on an undisclosed definition. | Medium |
| Annualised Q3 coupon interest is USD 210.7 million, against trailing EBITDA on the company's own adjusted definition of USD 598.4 million. | Interest cover is thin on this basis and the minimum covenant is 3.00x on an undisclosed definition. | Low |
| Revenue is diversified by product but the top three customers are 34% of net product revenue and VOXZOGO and VIMIZIM are 45.0% of total revenue. | Concentration and order timing can move cash flow in a quarter. | High |
| Management targets gross leverage below 2.5x by mid-year 2027, yet continues to acquire research assets, with acquired IPR&D of USD 287.7 million in Q3 2026. | Deleveraging depends on projected earnings that are not supplied. | Medium |

### Credit view

BioMarin is a strong operating business that has become a leveraged acquirer, and its credit now depends on earnings catching up with debt. The strongest support is an 80.0% gross margin, nine marketed rare-disease products and USD 1,336.0 million of liquidity, with no large maturity before the May 2027 convertible. The weakest point is leverage: principal debt rose from USD 600 million to USD 4,235 million, and trailing EBITDA captures only five months of Amicus and large acquired-research charges. What decides the outcome is whether combined earnings reach roughly USD 1.4 billion to USD 1.7 billion, the level the management target implies, while cash keeps flowing to new acquisitions. Covenant headroom, guarantors and ratings are not supplied, so confidence is medium.

### Key findings

1. The balance sheet changed character in 2026. Principal debt rose from USD 600.0 million at 2025-12-31 to USD 4,235.0 million at 2026-09-30 to fund USD 5,323.6 million for Amicus, using USD 850.0 million of 5.5% senior unsecured notes, USD 2,800.0 million of senior secured term loans and cash on hand, with no equity issued [CP-1 debt register; CP-1A transaction summary; Documentary Fact]. Cash and investments fell from USD 2,052.9 million to USD 736.0 million [CP-1 liquidity; Documentary Fact]. The 65.8% of debt that is variable-rate is secured and amortizing, and the remaining 34.2% is fixed-rate (derived, Analyst Interpretation).

2. Earnings on the new perimeter are not yet visible in trailing figures. Filed LTM EBITDA of USD 378.8 million (operating income plus depreciation and amortization) implies total debt to EBITDA of 11.18x and net debt to EBITDA of 9.24x; adding back impairment, the ROCTAVIAN inventory write-off and acquired IPR&D, an analyst construct, gives USD 923.0 million, 4.59x and 3.79x [CP-1 chart data; Analyst Interpretation]. Amicus contributed revenue of USD 336.4 million and a net loss of USD 239.4 million from 2026-04-27 [CP-1; Documentary Fact]. No pro forma EBITDA is supplied, so combined run-rate leverage is Not calculable.

3. Management defines its target differently and points to a lower level. In August 2026 management targeted gross leverage below 2.5x by mid-year 2027, defined as undiscounted debt over projected four-quarter adjusted EBITDA before depreciation, amortization and stock-based compensation [CP-1A; Management Language]. A backward-looking approximation of that definition gives USD 598.4 million of LTM EBITDA and 7.08x gross leverage [CP-1A calculation; Analyst Interpretation]. Reaching the target would need projected EBITDA of about USD 1,436 million if the May 2027 notes are paid in cash and scheduled amortization is made, or USD 1,694 million at current principal, which is 2.40x to 2.83x the LTM approximation [CP-1A; illustrative arithmetic]. Whether projections support this is Not calculable.

4. Liquidity covers the near term but rests on the revolver. Cash of USD 736.0 million plus an undrawn USD 600.0 million revolver is USD 1,336.0 million, which is 2.02x the USD 660.0 million of debt due in the next twelve months on the derived schedule (USD 15.0 million of term loan amortization in Q4 2026, USD 45.0 million in the first three quarters of 2027 and the USD 600.0 million convertible); cash alone is 1.12x [CP-1; Analyst Interpretation]. Trailing operating cash flow less capex of USD 557.9 million adds funding capacity, but cash interest paid of USD 69.7 million understates the run-rate [CP-1; Documentary Fact]. The revolver is available only subject to compliance with the credit agreement [CP-1; Documentary Fact].

5. The interest burden is the sharpest pressure point. Q3 2026 coupon interest was USD 52.7 million, or USD 210.7 million annualised, compared with USD 598.4 million of LTM EBITDA on the company's adjusted definition (2.84x), USD 378.8 million on filed EBITDA (1.80x) and USD 923.0 million on the analyst-adjusted basis (4.38x) [CP-1; CP-1A; Analyst Interpretation]. A rise of 100 basis points adds about USD 27.9 million to annual interest expense on USD 2,785.0 million of variable-rate debt [CP-1; Documentary Fact]. The covenant minimum of 3.00x interest coverage uses a definition that is not supplied, so these ratios are not the covenant test.

6. Covenant compliance is stated but not measurable. The Term Loan A and the revolver carry a 3.50x maximum Total Net Leverage Ratio, temporarily 4.00x for certain acquisitions, and a 3.00x minimum Interest Coverage Ratio, with compliance stated at 2026-09-30 [CP-1 covenants; Documentary Fact]. Reported ratios and definitions are Not supplied, so headroom is Not calculable. The analyst-adjusted net leverage of 3.79x sits close to the leverage maximum but the covenant definition probably uses pro forma and other adjustments, an inference that cannot be tested.

7. Capital is still flowing to acquired research. Acquired IPR&D was USD 287.7 million in Q3 2026 against USD 221.0 million in Q3 2025; the Alesta acquisition (USD 303.4 million) and the BMN 450 license (USD 70.0 million upfront, up to USD 405.0 million in milestones) followed the leverage target, full-year guidance was cut on the two charges, and cash fell by USD 138.0 million in Q3 [CP-1A; Documentary Fact]. This is a pattern of three pipeline-led deals, Inozyme, Alesta and BMN 450, in about fifteen months beside the Amicus deal, which constrains deleveraging speed [Analyst Interpretation].

8. Claims outside debt are material but known. Firm purchase commitments are USD 768.8 million (USD 291.1 million in 2026); contingent milestones judged reasonably possible are USD 485.5 million, plus Dimerix up to USD 510.0 million and Alesta up to USD 215 million, listed separately and not summed; FY2025 lease liabilities were USD 45.7 million; restructuring accruals are USD 47.7 million [CP-1; Documentary Fact]. There is no pension, factoring or supply-chain finance disclosure.

### Strengths and weaknesses

Strengths. First, the franchise is profitable and cash-generative at the gross level: derived gross margin was 80.0% in Q3 2026, 78.3% in the nine months and 77.7% in FY2025, and trailing operating cash flow less capex was USD 557.9 million, which funds interest and amortization before new acquisitions [CP-1, CP-1A; Analyst Interpretation]. Second, revenue is spread over nine marketed products and several regions: the largest product, VOXZOGO, is 23.9% of Q3 2026 revenue, the United States is 36.8% and Europe 38.1% of company-marketed net product revenue, and Q3 2026 revenue grew 32% year on year, mainly from the acquired products [CP-1A; Documentary Fact]. Third, near-term liquidity is adequate: USD 1,336.0 million against USD 660.0 million of debt due within twelve months, and no maturity above USD 60.0 million a year between 2028 and 2030, which is amortization only [CP-1; Analyst Interpretation]. Fourth, the company has never paid a dividend, has no documented repurchases and funded Amicus with debt and cash instead of distributions, so no cash has been extracted by shareholders [CP-1A; Documentary Fact]. Fifth, most debt is long dated: USD 2,785.0 million of term loans mature in 2031 and 2033 and USD 850.0 million of notes in 2034 [CP-1; Documentary Fact].

Weaknesses. First, leverage is high and its true level is unproven; trailing EBITDA includes five months of Amicus and every adjusted measure here is analyst-derived or management language, and the covenant definitions are unknown, so headroom cannot be shown [CP-1, CP-1A; Analyst Interpretation]. Second, earnings are volatile because of acquired IPR&D, which was USD 287.7 million in Q3 2026 and USD 221.0 million in Q3 2025, and Q3 2026 produced an operating loss of USD 82.1 million and a net loss of USD 122.8 million [CP-1; Documentary Fact]. Third, the interest burden is large against earnings, with annualised coupon interest of USD 210.7 million and USD 2,785.0 million of floating-rate debt [CP-1; Documentary Fact]. Fourth, concentration: the top three customers are 34% of Q3 2026 net product revenue, VOXZOGO and VIMIZIM together are 45.0% of total revenue, GALAFOLD and POMBILITI are made by single-source third parties, and large government orders shift between quarters, which management cited for the November 2026 revenue guidance cut [CP-1A; Management Language]. Fifth, the asset base is intangible-heavy: goodwill of USD 666.4 million and intangible assets of USD 4,777.2 million are 47.1% of total assets of USD 11,569.2 million, and equity less goodwill and intangibles is USD 812.4 million, so balance-sheet protection for creditors relies on the cash flows of the acquired products rather than tangible assets (derived, Analyst Interpretation). Sixth, the structure ranks the secured term loans first on substantially all assets, with unnamed subsidiary guarantors; the position of the unsecured 2034 Notes and the subordinated 2027 Notes against guarantor assets cannot be determined, a mechanic that bears on recovery prospects without implying an outcome [CP-1; Documentary Fact]. Seventh, the information base lacks executed legal documents, reported covenant ratios, projected EBITDA and ratings [CP-0, CP-1, CP-1A; Insufficient Information].

### Thesis and assessment

Thesis: a high-margin, diversified rare-disease franchise with adequate near-term liquidity, whose creditworthiness over the next twelve to eighteen months depends on integrating Amicus, containing acquired-research spend and converting a debt-funded purchase into combined earnings that support a lower leverage level [Analyst Interpretation]. Assessment confidence: Medium. It is below High because the CP-1A gaps that carry weight for this module are open: no executed financing documents, no projected adjusted EBITDA, and management language on leverage that cannot be tested. CP-1A judged this module READY_WITH_LIMITATIONS and logged no Critical gap.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Earnings do not reach the level implied by the leverage target | Trailing EBITDA covers five months of Amicus and absorbs repeated acquired-research charges; projected EBITDA is not supplied | Leverage stays above the covenant maximum on any stricter definition and delays deleveraging | Material |
| Interest burden and floating-rate exposure | Annualised coupon interest is USD 210.7 million; USD 2,785.0 million is variable rate | A rise of 100 basis points adds about USD 27.9 million a year; thin cover on the filed definition | Material |
| Covenant headroom unknown | Total net leverage maximum 3.50x and interest coverage minimum 3.00x on undisclosed definitions | A breach would put the revolver and Term Loan A at risk, the facilities carrying the tests; the consequences sit in the credit agreement, which is not supplied | Material |
| May 2027 convertible maturity | USD 600.0 million is payable in cash unless converted at USD 137.47 per share; the market price is not supplied | Cash use of USD 600.0 million in 2027 competes with amortization, interest and acquisitions | Material |
| Continued acquisitions and licensing | Three pipeline deals plus Amicus within about fifteen months; USD 485.5 million of contingent milestones judged reasonably possible | Cash and balance sheet capacity are consumed while leverage is high | Material |
| Customer, product and supply concentration | Top three customers 34%; VOXZOGO and VIMIZIM 45.0% of revenue; single-source manufacturing for the acquired products; Sanofi change-of-control terms | A disruption or a delayed order cuts cash flow in a quarter | Material |
| Integration and preliminary accounting | Purchase price allocation is preliminary; Amicus controls are being integrated | Goodwill, intangibles and deferred taxes may move; reporting errors would weaken monitoring | Minor |
| Legal | Unquantified DOJ subpoena on sponsored testing programs | Possible cost and disclosure; no estimate | Minor |

## Calculations

Amounts in the prose of this handoff are in USD millions, converted from the thousands in CP-1 and CP-1A. Ratios come from the cited upstream figures.

| Calculation | Inputs | Result |
| --- | --- | --- |
| Floating share of debt | 790,000 + 1,995,000 = 2,785,000 thousand; / 4,235,000 (CP-1 debt register) | 65.8% variable, 34.2% fixed |
| Liquidity cover of next-twelve-month maturities | (736.0 + 600.0) / 660.0; 736.0 / 660.0 (CP-1 liquidity and maturities) | 2.02x; 1.12x |
| Next-twelve-month maturities | Q4 2026 15.0 + Q1 to Q3 2027 amortization 45.0 + 2027 Notes 600.0 (CP-1 maturities) | 660.0 |
| EBITDA / annualised coupon interest | 378,821 / 210,732; 922,962 / 210,732; 598,418 / 210,732 (CP-1, CP-1A) | 1.80x; 4.38x; 2.84x |
| Intangible intensity | (666,367 + 4,777,247) / 11,569,231 (Q3 10-Q page:8-9) | 5,443,614 thousand, 47.1% of total assets |
| Equity less goodwill and intangibles | 6,256,032 - 666,367 - 4,777,247 (CP-1) | 812,418 thousand |
| Cash fall in Q3 2026 | 874,005 - 736,007 (CP-1A) | 137,998 thousand, USD 138.0 million |
| Implied EBITDA for the target | 4,235,000 / 2.5; (4,235,000 - 600,000 - 45,000) / 2.5 (CP-1A) | 1,694,000; 1,436,000 thousand; illustrative |
| Reopened upstream figures | Debt principal 4,235,000; cash 736,007; revolver 600,000; consideration 5,323,561; LTM EBITDA 378,821; adjusted 922,962; company-definition approximation 598,418 (CP-1, CP-1A, Q3 10-Q page:8, page:14, page:22, page:48) | All agree with the sources and with each other |

## Gaps

| Gap | Severity | Effect on this synthesis | Action |
| --- | --- | --- | --- |
| Executed merger agreement, credit agreement and indentures not supplied (inherited from CP-0 and CP-1A) | High | Covenant definitions, guarantors, baskets and priming capacity unknown; legal capacity cannot be assessed | Add the exhibits |
| Covenant ratios not printed; headroom Not calculable (CP-1) | High | The view cannot say how close the issuer is to the tests | Add the compliance certificate |
| No pro forma combined EBITDA and no projected adjusted EBITDA (CP-1, CP-1A) | High | Run-rate leverage and the achievability of the below-2.5x target are Not calculable | Obtain management projections or a pro forma bridge |
| Management leverage target stated once, on 2026-08-06, and not repeated in November (CP-1A) | Medium | Current status unconfirmed | Check the call transcript, not in the pack |
| Guarantors and structural ranking of the notes unresolved (CP-1, CP-1A) | Medium | Ranking of unsecured and subordinated debt against guarantor assets cannot be tested | Add the supplemental indenture |
| Ratings, quotes and market data not supplied (context) | Medium | No market-implied view or share price for the convertible | Supply or mark not supplied |
| CP-1 did not carry management's leverage target or its definition; CP-1A added them. This synthesis uses both and treats CP-1's leverage figures as filed-basis measures | Low | Leverage is shown on three bases, each labelled | None; stated here because the earlier handoff cannot be edited |
| Purchase price allocation preliminary (CP-0, CP-1A) | Medium | Intangibles, goodwill and taxes may change | Carry as provisional |
| Customers A, B and C not named; product pricing not disclosed (CP-1A) | Medium | Counterparty and price risk cannot be sized | None in the pack |
| Extraction fidelity not reviewed (CP-0) | Low | Locators rest on page chunks | Carry forward |

## Next module

Proceed to CP-5 (evidence trace), which should resolve each figure and citation in this handoff against the pinned sources, check that Management Language rows stay attributed, and confirm that derived figures (leverage on three bases, implied EBITDA, floating share, intangible share) remain labelled as analyst-derived. The next evidence action for the credit view is to obtain the 2026 Credit Agreement, the indentures and management's projected adjusted EBITDA.
