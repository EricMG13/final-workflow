## Request

This is the fundamental credit synthesis for OPENLANE, Inc. (issuer id opln) as of 2026-11-05, pathway credit_snapshot. It reads the financial base and the business and transaction context for the issuer, and gives a credit view, strengths, weaknesses, key findings and risks, with no peer ranking, instrument recommendation or recovery conclusion.

## Sources

### Issuer sources relied on

This module reads upstream handoffs, which rest on the seven sources below. Where a claim goes beyond the handoffs it cites the source page directly and says so.

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_opln-20251231.htm.jsonl | 26a1eb6e044eb7884447c1771579bc95b55527d93c8454714335cfb05faebcc7 |
| 10-Q_2026-03-31_opln-20260331.htm.jsonl | c46e877ea2548ae22544a835acae1b3618984f266ca5c5f8d9f1ce170a2f3661 |
| 10-Q_2026-06-30_opln-20260630.htm.jsonl | 47753528b639818941177074a5796fb5ee4c271e3e7cb89f9ddc4bf548a73b8f |
| 10-Q_2026-09-30_opln-20260930.htm.jsonl | 9682e191d9ec651d5722722ac8ff03e1ea87ff7ece0722d12fcb449d04d13357 |
| EX-99.3_2026-05-05_q12026openlaneearningssl.htm.jsonl | 2fc56068f78381bd02bfbe329da47d9ab40d86ee26db869d39406949616dc5f0 |
| EX-99.3_2026-08-04_q22026openlaneearningssl.htm.jsonl | 458d3c1fac99aaeefe126a46b683e88ca11580e6032ddf67da49e980bf2bff5d |
| EX-99.3_2026-11-04_q32026openlaneearningssl.htm.jsonl | bc88d193632549ac9eb968d3349190fc1ffa3b0842d97894dce16151e37cfd9a |

### Other pinned input

| Input | sha256 | Use |
| --- | --- | --- |
| context | 2fd2835b16fcd6e36fa06485261ee15d20c3a0b3f6cb56cfce407e6993d9ef70 | Run settings only; not issuer evidence. Ratings, market data and peers are blank, and blank is not zero. |

### Handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 822af9f32f30d6c0feeb6f1f36ee177a40b0f0ee61b0286bf38226d8998cb018 | Source readiness view and limitations |
| CP-1 | 27cde0aafcf9a133517adb102e5557dc8e810ad505a4dc1f22e1f42860aed45f | Financial base: leverage, cover, liquidity, maturities, debt stack, covenants, cash flow |
| CP-1A | 47b5129c30bcd183ee2afab5505e28425411f08dbab77100718b6ed693727913 | Business model, ownership, timeline, governance table, conflicts, credit translations |

Citations in brackets name the handoff and its section, for example [CP-1 leverage table]. A locator `page:N` is the source chunk number in the pinned file, not the printed page. Category tags are Documentary Fact, Management Language, Analyst Interpretation and Insufficient Information.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| OPENLANE has a sound corporate credit profile, with total debt at 1.43x LTM Adjusted EBITDA and liquidity of USD 650.2 million, but most funding is receivable-backed securitization and its performance decides the credit. | Medium | The credit and securitization agreements are not supplied, so covenant terms and undrawn securitization capacity are unverified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt is USD 545.9 million, one term loan with undrawn revolvers, against LTM Adjusted EBITDA of USD 382.7 million. | Corporate leverage is low, and the reported covenant ratio is 0.9x against a 3.5x maximum. | Medium |
| Securitization obligations are USD 2,084.4 million gross, outside the corporate debt figure. | The Finance book is funded largely by facilities not secured by the company's general assets, so its credit losses reach creditors through earnings and funding access. | High |
| Commercial volume growth of 46% in Q3 2026 falls to 17% excluding the latest customer. | Revenue visibility depends on consignors who can terminate for convenience, and fee yield is diluted. | Medium |
| Corporate net interest rose to USD 37.3 million LTM from USD 14.9 million in FY2025. | The October 2025 term loan raised fixed charges, though Adjusted EBITDA covers net interest 10.26x. | High |

### Credit view

OPENLANE, Inc. is a moderately leveraged, cash-generative issuer whose corporate credit profile is sound, but whose balance sheet is dominated by receivable-backed funding. Its strongest support is a single term loan of USD 545.9 million, undrawn revolvers and USD 650.2 million of liquidity, which put total debt at 1.43x LTM Adjusted EBITDA of USD 382.7 million [CP-1 leverage and liquidity tables]. Its weakest point is that USD 2,084.4 million of securitization obligations sit outside that ratio and fund a dealer-credit book whose losses follow wholesale vehicle prices, while commercial volume growth rests on consignors who can leave on notice [CP-1A credit translations]. The outcome turns on floorplan credit quality, continued access to the securitization facilities committed to January 31, 2030, and covenant terms that cannot be checked.

### Key findings

OPENLANE, Inc. carries low corporate leverage on the company measure: total debt of USD 545.9 million is 1.43x LTM Adjusted EBITDA, against 1.65x for FY2025 and 0.79x for FY2024, and net of cash it is 0.79x [CP-1 leverage table; Analyst Interpretation]. The step from FY2024 to FY2025 came from the USD 550.0 million term loan drawn in October 2025 to repurchase most of the Series A preferred stock [CP-1A transaction summary; Documentary Fact]. The company reports a covenant ratio of 0.9x at September 30, 2026 against a 3.5x maximum that applies on quarters when revolver loans are outstanding, and the revolvers have no borrowings [CP-1 covenants table; Documentary Fact].

The funded balance sheet is larger than the corporate debt figure. Securitization obligations are USD 2,084.4 million gross, or 75.4% of USD 2,763.5 million of receivables managed, against collateral coverage of 1.34x [CP-1 securitization section; Documentary Fact and calculation]. Company Adjusted EBITDA is stated after deducting securitization interest, so its leverage ratio is a corporate-level measure, and the cash-interest cover of 3.42x on unadjusted EBITDA is the comparable all-in view [CP-1 interest cover table; Analyst Interpretation].

Liquidity is ample against near-term obligations. Cash of USD 244.9 million and undrawn revolver availability of USD 405.3 million total USD 650.2 million, term-loan amortization is USD 5.5 million a year, and the next scheduled maturity beyond amortization is the revolvers on June 23, 2028, followed by a term-loan balance of USD 512.9 million due on October 8, 2032 on the CP-1 analyst schedule, which assumes installments on each quarter-end and no prepayment [CP-1 liquidity and maturity tables; Documentary Fact and Analyst Interpretation]. The securitization facilities expire on January 31, 2030, which is the nearer refinancing event.

Cash generation is strong but flattered by classification. Free cash flow was USD 268.8 million for nine months 2026 and USD 379.6 million LTM, but receivable growth of USD 367.6 million sits in investing activities and was funded USD 322.9 million by securitization, leaving USD 224.1 million after both [CP-1 calculations; Documentary Fact and calculation].

The earnings base mixes two businesses. Marketplace is 78% of FY2025 revenue and Finance 22%, yet Finance is 48.3% of LTM Adjusted EBITDA [CP-1A company and operating model; CP-1 segment view]. In Q3 2026 commercial vehicles sold rose 46%, or 17% excluding the latest commercial customer, while yield fell to 2.5% from 2.9% on mix [CP-1A company and operating model; Management Language for the 17%].

Capital allocation is shifting to shareholders. Repurchases were USD 91.5 million for nine months 2026 against USD 35.8 million, and the program was raised to USD 400 million in October 2026, with restricted-payment baskets not supplied [CP-1 cash flow quality; CP-1A governance table; Documentary Fact].

### Strengths and weaknesses

Strengths. The corporate capital structure is simple and lightly levered: one secured term loan, revolvers with no borrowings and no maturity before June 23, 2028 other than USD 5.5 million of annual amortization [CP-1 debt stack; Documentary Fact]. Liquidity of USD 650.2 million and reported covenant headroom of 2.6x on a 3.5x test give room to absorb a downturn before the revolver is needed [CP-1 liquidity and covenants tables; Documentary Fact and Analyst Interpretation]. The securitization facilities were extended by two years to January 31, 2030 in September 2026 [CP-1A timeline; Documentary Fact]. Customer exposure is spread, since no single customer was 10% or more of revenue and AFC has no dealer above 2.5% of its portfolio [CP-1A company and operating model; Documentary Fact]. The conversion of the remaining Series A preferred in May 2026 removed a senior equity claim with a 7% cash dividend and class vote rights [CP-1A ownership and control; Documentary Fact].

Weaknesses. Corporate creditors rank behind a bankruptcy-remote structure for the best collateral: the receivables are sold to a consolidated special purpose subsidiary, and the facilities are not secured by the general assets of the company, so the term loan's claim on the Finance book is to the value left after the securitization obligations; whether the AFC Funding Corporation shares are pledged to the term-loan lenders is not stated [CP-1 securitization section; Documentary Fact; Analyst Interpretation on the mechanic]. After a termination event under the U.S. facility the banks may cause the stock of AFC Funding Corporation to be transferred to them, although as a practical matter the bank facility would look to liquidation of the receivables as its primary remedy (10-Q Q3 page:57 "the banks may, and could, cause the stock of AFC Funding Corporation to be transferred to the bank facility"), a loss-of-control mechanic that the handoffs do not carry. The Finance book is credit sensitive: delinquent receivables were 0.6% of receivables managed against 0.3% a year earlier, and a fall in wholesale used-vehicle prices would raise losses if dealers cannot meet obligations [CP-1A company and operating model; Documentary Fact]. Revenue durability is only moderate, because customers make no binding volume commitments and many agreements can be ended for convenience, and the Q3 2026 commercial growth leaned on onboarding a new private label customer [CP-1A credit translations; Documentary Fact]. Earnings quality needs care: nine-month 2026 Marketplace gross profit includes a USD 20.2 million Canadian tax reversal benefit, of which USD 15.9 million relates to prior periods and is removed from Adjusted EBITDA, while the USD 4.3 million current-period part (10-Q Q3 page:46) is not [CP-1A company and operating model; CP-1 earnings quality; Documentary Fact]. Floating-rate term debt is not hedged: the company states it does not use interest rate contracts (10-K FY2025 page:88 "We do not currently use interest rate contracts to manage our exposure to interest rate changes"), which is a point not carried by the handoffs [Documentary Fact]. Unverifiable items include covenant EBITDA definitions, the Third Amendment of June 30, 2026, the share of the company still held by former preferred holders, and the nature of USD 1.7 million of Q3 2026 transaction-related costs [CP-1A gaps; Insufficient Information].

### Credit assessment

| Element | Content | Category | Confidence | Basis |
| --- | --- | --- | --- | --- |
| Fundamental credit view | Sound corporate credit with low reported leverage and ample liquidity; credit outcome tied to the performance and funding of the Finance receivable book and to commercial consignment volume | Analyst Interpretation | Medium | CP-1 leverage, liquidity and covenants tables; CP-1A company and operating model, ownership and control, credit translations |
| Limitation on confidence | Executed credit and securitization agreements, current holdings of the former preferred holders and facility-level securitization balances are not supplied; the CP-1A readiness for this module is READY_WITH_LIMITATIONS, not READY | Insufficient Information | Medium | CP-0 readiness view; CP-1A consumer readiness |

### Credit thesis

OPENLANE, Inc. is a lightly levered, liquid corporate borrower whose creditworthiness is driven less by its USD 545.9 million of term debt than by the credit quality and continued securitization funding of a dealer-finance book of USD 2,763.5 million of receivables managed and by the durability of commercial consignment volume.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity | Basis |
| --- | --- | --- | --- | --- |
| Dealer credit and wholesale price cycle in Finance | A fall in used-vehicle prices or dealer demand lowers collateral value and raises defaults; delinquent receivables were 0.6% of receivables managed in Q3 2026 against 0.3% | Finance is 48.3% of LTM Adjusted EBITDA, so loss severity reduces earnings and could tighten securitization eligibility; monitor delinquency and provision rate | Material | CP-1A company and operating model; CP-1 segment view |
| Securitization funding access and structural position | Corporate creditors have no claim on securitized receivables beyond the residual, and termination events let banks take the AFC Funding Corporation stock; facilities are committed to January 31, 2030 | Refinancing and liquidity risk for the Finance book sits at the facilities; recovery for corporate creditors would depend on residual value, a mechanic only | Material | CP-1 securitization section; 10-Q Q3 page:57 |
| Commercial consignor concentration and yield dilution | Customers can terminate for convenience; growth leaned on a new customer; yield fell to 2.5% from 2.9% | Revenue visibility is moderate and fee income per vehicle is diluted by mix | Material | CP-1A company and operating model, credit translations |
| Higher fixed charges and unhedged floating rate | Corporate net interest was USD 37.3 million LTM against USD 14.9 million in FY2025; term loan floats on Adjusted Term SOFR plus 2.50% | Cover remains high at 10.26x on Adjusted EBITDA, but a rate rise or EBITDA fall reduces it | Minor | CP-1 financials table, debt stack |
| Capital returns ahead of deleveraging | Repurchases of USD 91.5 million for nine months 2026 and an enlarged program; basket limits not supplied | Leverage tolerance is untested above the current level; monitor distributions | Minor | CP-1 cash flow quality; CP-1A governance table |
| Unverified covenant definitions and amendments | Covenant EBITDA differs from company Adjusted EBITDA and the Third Amendment is undescribed | Headroom of 2.6x on reported terms cannot be tested independently | Material | CP-1 covenants table and gaps |

## Calculations

One new calculation is made here. Debt service cover on corporate obligations for LTM Q3 2026: Adjusted EBITDA of USD 382.7 million divided by the sum of LTM interest expense net of interest income of USD 37.3 million and annual term-loan amortization of USD 5.5 million, which is USD 42.8 million, gives 8.94x [CP-1 financials table and maturity schedule]. It is a corporate-level measure, because Adjusted EBITDA is after securitization interest. All other figures are quoted from the CP-1 handoff and are not recomputed. The term-loan balance of USD 512.9 million in 2032 is the CP-1 schedule figure of 512.875, rounded.

## Gaps

| ID | Gap | Why it matters | Severity | Action |
| --- | --- | --- | --- | --- |
| G1 | The Credit Agreement, its amendments including the Third Amendment of June 30, 2026, and the securitization agreements are not supplied | Covenant definitions, restricted-payment baskets and guarantor scope cannot be tested; headroom is as reported by the company | High | Supply the executed agreements |
| G2 | Undrawn securitization capacity and facility-level balances are Not calculable | Liquidity for the Finance book beyond the revolvers cannot be sized | Medium | Obtain facility reports |
| G3 | Current holdings of the former preferred holders, any board designation right and the nature of USD 1.7 million of Q3 2026 transaction-related costs are not stated | Ownership control and unexplained events may change sponsor-alignment views | Medium | Supply proxy, ownership filings or call transcript |
| G4 | Cash paid for interest is a single figure that includes securitization interest | Corporate cash cover cannot be isolated; the accrual cover is the cross-check | Medium | Use accrual cover as cross-check |
| G5 | Customer-level data for commercial consignors is not supplied | Concentration beyond the statement that no customer reached 10% of revenue cannot be sized | Medium | Supply if available |
| G6 | No credit ratings, market prices or peer data are supplied | Market-implied views cannot be compared; none are inferred | Low | Keep Not supplied |
| G7 | Deck charts are not in the extracted text and nothing after November 4, 2026 is supplied | Operating metrics rely on the 10-Q tables; later events are Not supplied, not absent | Low | Use filed tables; supply later 8-Ks |
| G8 | The December 31, 2025 collateral figure of USD 2,803.5 million in the 10-K was corrected to USD 2,448.2 million in the 2026 10-Qs | Collateral coverage uses the corrected figure; the conflict is logged, not reconciled | Medium | Cite both |

Inherited signals: the CP-1A readiness judgment of this module is READY_WITH_LIMITATIONS and not READY, so confidence is below High. The upstream readiness view from the source check is READY_WITH_LIMITATIONS for every consumer. These limits are stated once here and not repeated in the findings.

## Next module

- CP-5 (evidence trace): trace each figure to its CP-1 table and each business claim to its CP-1A row; trace the 10-K FY2025 page:88 and 10-Q Q3 page:57 statements used here to their pages; treat the deck statements as management language.
- No further module is selected after CP-5 in this run; the committee questions that need executed agreements (G1) go to the first diligence request.
