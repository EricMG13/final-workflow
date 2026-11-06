# CP-2 fundamental credit synthesis: ESCO TECHNOLOGIES INC (ese)

## Request

ESCO TECHNOLOGIES INC (issuer id `ese`) is assessed as of 2026-11-05 on the `credit_snapshot` pathway. The scope is the fundamental credit view built only from the CP-0, CP-1 and CP-1A handoffs, with no source text re-read and no peer ranking, instrument recommendation or recovery conclusion.

## Sources

CP-2 works from upstream handoffs only. The issuer sources below are the files those handoffs rely on; this module did not reopen them, and every figure and fact here traces to CP-1 or CP-1A.

### Issuer sources relied on (through the handoffs)

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | fe80d5d10f35aaa7f1b7aa40e6d69aeaea7f501fabdde619947c03aa0fe69d71 |
| 10-Q_2025-12-31_ese-20251231x10q.htm.jsonl | 028e0b9aec25ecf720ca796f0beef13fd8b40ddc333348a8ba8153fe3b16e523 |
| 10-Q_2026-03-31_ese-20260331x10q.htm.jsonl | d207365eeea17e17e69c10625b481ddba582ee4861f7a9c60376e4bd5dffc806 |
| 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | 056428009193705ead08cb6828be9f20a62a9323946644ad69e280efbf618711 |
| EX-99.1_2026-01-30_tm264950d1_ex99-1.htm.jsonl | 73c00c863e8360707e7681c62537391b693f1632ac470f63ec94b54622dbc238 |
| EX-99.1_2026-05-07_tm2613615d1_ex99-1.htm.jsonl | 4483c93985a6b3ea98a959d8659fafa040f3230850186662a7c5bb7c5d2d8a1d |
| EX-99.1_2026-08-06_tm2621646d1_ex99-1.htm.jsonl | f683102e1a6a6e74cee756fd0639a64a1d810e0d5fd17fcb2dc502f25f716fb6 |

### Other inputs

| Input | sha256 |
| --- | --- |
| context (`contexts/866706-esco-technologies-inc-ese.json`; run settings, not issuer evidence) | da65696ce609dcf19999b44c58b8a10f43f7d7bc7cde7c4a3762d76affdde214 |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 7f46d3b1dbdad4b468a5bdd5db37f408dc8a1ce57aba77ff195a116822899d17 | Source readiness: READY_WITH_LIMITATIONS; gap list |
| CP-1 | 23a50d14b3104c2571d80147c88f81427457a9b11a2aa773f3459c4d026de1e7 | Financial base: leverage, cover, liquidity, maturities, claims outside debt |
| CP-1A | 7bb2aa7585c6ae63abcfb32f227dd60a79e423f35bf4601e20c348a72e1bc24b | Business, transaction, governance, conflicts, consumer judgments |

### Basis labels

Bracketed basis labels name the upstream section: CP-1 sections are "Chart data", "Financials and credit metrics", "Debt instruments and facilities", "Claims outside debt", "Covenants and definitions" and "Narrative review"; CP-1A sections are "Company and operating model", "Company profile", "Transaction summary and new debt issues", "Ownership, governance and sponsor behaviour", "Timeline", "Conflicts and document differences" and "Credit translations". Periods follow the fiscal year ending September 30: Q3 2026 is the quarter ended June 30, 2026, LTM is the twelve months to June 30, 2026. Currency is USD.

CP-2 consistency: this module carries the CP-1 and CP-1A figures unchanged and corrects neither. It repeats CP-1A's two logged conflicts (Megger consideration components; the wording of the current portion of debt) as limits on the maturity and transaction reading, without resolving them.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| ESCO is lightly levered today, with USD 85.0 million of borrowings and USD 515.536 million of liquidity at June 30, 2026, but the pending Megger acquisition will reset debt, covenants and ownership. | Medium | Covenant levels, the new credit agreement, Megger financials and anything after August 10, 2026 are not supplied, so the post-closing credit cannot be sized. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt to EBITDA was 0.278x and EBITDA covered cash interest 20.42x on a last-twelve-months basis to June 30, 2026. | Reported leverage and debt service capacity are strong before the acquisition financing. | High |
| Liquidity of USD 515.536 million is mostly an undrawn revolver, and only USD 20.000 million of debt falls due within twelve months. | Near-term refinancing and liquidity risk is low until the existing facility is replaced. | High |
| Backlog of USD 1,540.5 million and a diversified three-segment base support revenue, but the US Government is approximately 23% of revenue and contracts can be terminated for convenience. | Revenue is visible but exposed to defense budget and program timing in the largest segment. | Medium |
| The Megger purchase is approximately USD 2.35 billion, of which USD 0.9 billion is cash, funded with new term loans and a revolver of USD 500 million each. | Leverage and covenant terms will change at closing and cannot yet be tested. | Medium |
| Documented behaviour since fiscal 2025 is supportive of creditors, with debt repaid after the VACCO sale and no buybacks. | Past conduct is a positive signal, but post-closing behaviour and TBG AG's rights are unknown. | Medium |

### Credit view

ESCO Technologies currently has a strong, lightly levered credit profile, but the credit view depends on a pending acquisition that this evidence cannot size. At June 30, 2026 ESCO had USD 85.0 million of borrowings against LTM EBITDA of USD 305.677 million (total debt 0.278x, net debt 0.038x), liquidity of USD 515.536 million and backlog of USD 1,540.5 million [CP-1; CP-1A Company and operating model]. The weakest point is that this describes ESCO before the Megger purchase, which includes USD 0.9 billion of cash funded under new facilities whose terms, and Megger's own earnings, are not supplied [CP-1A Transaction summary]. What decides the outcome is whether closing has occurred, how much is drawn on the new term loans and what the covenants allow.

Confidence is Medium, not High, because CP-1A judged CP-2 ready only with limitations (see Gaps) and the covenant and transaction documents are missing.

### Key findings

ESCO has very low reported leverage and strong cover. Total borrowings were USD 85.0 million at June 30, 2026, down from USD 186.0 million at September 30, 2025, so total debt to EBITDA fell from 0.758x to 0.278x and net debt to EBITDA from 0.345x to 0.038x. EBITDA covered cash interest paid 20.42x on an LTM basis against 14.09x for FY2025 [CP-1 Chart data]. The mechanism was operating cash flow from continuing operations of USD 193.377 million in nine months 2026 funding net repayment and other uses, so the debt reduction came from cash generation, which supports debt service capacity [CP-1 Narrative review: leverage].

ESCO has ample liquidity and a short near-term maturity profile. Cash was USD 73.236 million and the revolver had USD 442.300 million undrawn after USD 12.7 million of letters of credit, together USD 515.536 million; USD 20.000 million of term loan A is current and USD 65.000 million falls due by August 30, 2028, which is the maturity of the existing revolver and term loan A [CP-1 Chart data]. The existing facility is secured by guarantees from material US subsidiaries and a pledge of equity of material foreign subsidiaries [CP-1 Debt instruments and facilities]. Because the facility is to be replaced at the Megger closing, this maturity profile is a pre-closing picture. The wording of the current portion changed from voluntary in Q1 2026 to obligated in Q2 and Q3 2026, a logged conflict the supplied documents do not explain [CP-1A Conflicts].

ESCO has diversified operations with a government-weighted core. Aerospace & Defense was approximately 44% of fiscal 2025 revenue, Utility Solutions Group approximately 35% and RF Test approximately 21%; the US Government and its contractors were approximately 23%, and no customer exceeded 10% [CP-1A Company and operating model]. Backlog of USD 1,540.5 million, with approximately 59% expected in the next twelve months, gives revenue visibility, but Government contracts are terminable for convenience and fixed-price contracts expose margins to cost overruns [CP-1A Credit translations].

ESCO's cash flow in the latest nine months may overstate a normal level. Continuing operating cash flow of USD 193.377 million benefited from customer advances, with contract liabilities up USD 71.5 million, and discontinued operations used USD 59.340 million, alongside approximately USD 59 million of cash tax paid on the VACCO gain. LTM free cash flow of USD 258.102 million is therefore a continuing-operations figure before that one-time outflow and before dividends [CP-1 Narrative review: cash flow quality]. Customer advances can reverse as projects deliver, which would lower operating cash flow.

ESCO's acquisition will change the credit. The Megger purchase has total consideration of approximately USD 2.35 billion, of which USD 0.9 billion is cash and approximately USD 1.4 billion is ESCO equity, with closing expected in the first quarter of fiscal 2027 [CP-1A Transaction summary]. Committed financing is a new senior secured revolver, term loan A and term loan B of USD 500 million each, effective only at closing and replacing the existing facility [CP-1 Debt instruments and facilities]. Megger's financials are not supplied, so post-closing leverage and cover are not calculable. As a bound only, CP-1 shows that if the full USD 0.9 billion cash consideration were borrowed on top of current debt, total debt would be about 3.22x ESCO-only LTM EBITDA before Megger earnings; this is an Analyst Inference, not a forecast [CP-1 Narrative review: leverage]. The 2026-11-05 as-of date falls after the start of the expected closing quarter, and nothing after August 10, 2026 is supplied, so closing status is unknown.

ESCO's covenants cannot be tested. The existing facility has a leverage ratio and an interest coverage ratio, and management reported compliance at June 30, 2026, but levels, definitions and the reported ratios are not supplied, and the New Credit Facility terms are not supplied [CP-1 Covenants and definitions]. Headroom is therefore not calculable, and the reported ratios in this credit view are not covenant ratios.

ESCO's observed conduct supports creditors, and ownership will change. VACCO proceeds were used mainly to pay down debt, dividends are small, there were no buybacks in fiscal 2025 or Q3 2026 and no creditor-adverse action appears in the supplied sources. TBG AG will receive ESCO shares and sign a shareholder agreement at completion; its stake, governance rights and lock-up terms are not supplied [CP-1A Ownership, governance and sponsor behaviour].

### Strengths and weaknesses

ESCO's strengths start with its balance sheet. Reported leverage is low (total debt to EBITDA 0.278x) and cash interest cover is high (20.42x) on LTM figures, giving the issuer capacity to absorb a cost or volume shock before the acquisition financing [CP-1 Chart data; Documentary Fact and Analyst Interpretation]. Liquidity of USD 515.536 million is dominated by an undrawn revolver that matures August 30, 2028, so near-term refinancing risk is low [CP-1 Chart data; Documentary Fact]. Backlog of USD 1,540.5 million and a three-segment mix with no customer above 10% of sales support revenue visibility and limit single-customer risk [CP-1A Company and operating model; Documentary Fact]. Capital allocation since fiscal 2025 has favoured creditors, with debt repaid from divestiture proceeds, small dividends and no buybacks [CP-1A Ownership, governance and sponsor behaviour; Documentary Fact]. Cash generation from continuing operations was strong in the latest period [CP-1 Narrative review; Documentary Fact, qualified by working capital timing].

ESCO's weaknesses concentrate on the pending transaction and on missing documents. The Megger purchase is large relative to the existing debt, is funded partly with new term debt, and its terms and Megger's earnings are not supplied, so the leverage that creditors will face is unknown [CP-1A Transaction summary; Insufficient Information, with the missing datapoints being the credit agreement, Megger financials and closing status]. Covenant levels and headroom are missing for both the existing and the new facility [CP-1 Covenants and definitions; Insufficient Information]. Government funding concentration in Aerospace & Defense, termination for convenience and fixed-price cost risk could affect the largest and fastest-growing segment [CP-1A Credit translations; Documentary Fact and Analyst Interpretation]. Operating cash flow was lifted by customer advances and the reported free cash flow excludes a discontinued-operations outflow, so cash conversion is flattered in the nine months [CP-1 Narrative review: cash flow quality; Analyst Interpretation]. TBG AG's resulting stake and governance rights are unknown, which limits the view of control and alignment after closing [CP-1A Ownership, governance and sponsor behaviour; Insufficient Information]. Smaller weaknesses are renewables exposure in the utility segment, sole-source suppliers, and internal-control scope that excludes recently acquired businesses until they are tested [CP-1A Company and operating model; Documentary Fact].

### Key credit risks

| Risk | Mechanic | Credit implication | Severity | Basis |
| --- | --- | --- | --- | --- |
| Acquisition financing and leverage step-up | Cash consideration of USD 0.9 billion is funded from cash and new term loans effective at closing | Debt rises from USD 85.0 million to a level that depends on draws; leverage tolerance and debt service capacity are untested | Material | CP-1 Debt instruments; CP-1A Transaction summary |
| Covenant and documentation opacity | Leverage and coverage tests exist but levels and definitions are not supplied | Headroom and restricted payment capacity cannot be assessed; monitoring posture is limited | Material | CP-1 Covenants and definitions |
| Government funding and termination concentration | About 23% of revenue from the US Government, terminable for convenience; A&D is the largest segment | A budget or program shock reduces revenue in the segment that now carries most growth | Material | CP-1A Company and operating model |
| Cash flow reversal | Customer advances and a working capital inflow lifted operating cash flow | Normal cash conversion may be lower, reducing debt paydown capacity | Material | CP-1 Narrative review |
| Ownership and control change | Equity consideration issued to TBG AG with a shareholder agreement at completion | Governance rights and influence over distributions or further transactions are unknown | Material | CP-1A Ownership and governance |
| Refinancing and maturity reset | Existing facility replaced; new tenors of five and seven years; amounts drawn unknown | Maturity wall and amortisation cannot be built; current portion wording is unexplained | Material | CP-1 Chart data; CP-1A Conflicts |
| Fixed-price contract and margin risk | Cost overruns reduce margin on fixed-price work | Lower EBITDA cover if cost inflation persists | Minor | CP-1A Credit translations |
| Renewables and supplier concentration | NRG orders fell with tax credit expiry; sole-source components exist | Segment earnings and delivery timing could weaken | Minor | CP-1A Company and operating model |
| Integration and control scope | Maritime was excluded from the internal control audit scope at year end; Megger will be a further integration | Reporting risk during integration | Minor | CP-1A Ownership, governance and sponsor behaviour |

### Assessment

| Element | Content | Category | Confidence | Basis |
| --- | --- | --- | --- | --- |
| Fundamental credit view | Lightly levered with strong liquidity and cover today; event-driven by the pending Megger acquisition; post-closing credit not sizeable from supplied evidence | Analyst Interpretation | Medium | CP-1 Chart data and Financials and credit metrics; CP-1A Transaction summary and Credit translations |
| Thesis | ESCO's strong liquidity, low reported leverage, backlog and creditor-supportive conduct support its credit today, while the unseen terms of the Megger financing, its covenants and its ownership change decide the credit once the acquisition closes | Analyst Interpretation | Medium | CP-1; CP-1A |

## Calculations

No new calculation. CP-2 carries the CP-1 figures unchanged: leverage, cover, liquidity and maturity figures come from CP-1 Chart data, the free cash flow from CP-1 Financials and credit metrics, and the 3.22x bound from CP-1 Calculations (an Analyst Inference there). The percentages for revenue by segment and for the US Government are CP-1A figures taken from the 10-K. Nothing here is recomputed or replaced with zero.

## Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Covenant levels, definitions and reported ratios not supplied (CP-1) | Headroom, restricted payment capacity and any covenant-driven acceleration cannot be assessed | Leverage and liquidity conclusions | High | Supply the 2023 Amended and Restated Credit Agreement, Amendment No. 1 and a compliance certificate |
| New Credit Facility terms (pricing, covenants, conditions, guarantors, collateral) not supplied (CP-1, CP-1A) | Post-closing debt service, security and covenant terms are unknown | Refinancing and structure | High | Supply the May 29, 2026 Credit Agreement |
| Megger financials and pro forma data not supplied (CP-1, CP-1A) | Post-closing leverage and cover cannot be calculated | Financial risk after closing | High | Supply Megger statements or pro forma information |
| Closing status and events after August 10, 2026 not supplied (CP-0, CP-1, CP-1A) | The as-of date is after the start of the expected closing quarter; debt may already be different | All conclusions | High | Supply later 8-Ks or confirm none |
| TBG AG stake, governance rights and lock-up not supplied (CP-1A) | Control and alignment after closing | Governance and ownership | High | Supply the shareholder agreement |
| Consideration components do not add to the stated total (CP-1A conflict, logged not reconciled) | Size of the transaction and equity issued is uncertain | Transaction reading | Medium | Obtain the April 15, 2026 8-K |
| Current portion of debt: wording changed from voluntary to obligated (CP-1A conflict, logged not reconciled) | Maturity and amortisation profile of term loan A | Maturity profile | Medium | Supply Amendment No. 1 and later amendments |
| Term loan A repayment schedule and fiscal-year maturity split not supplied (CP-1) | Maturity wall cannot be built beyond two buckets | Refinancing | Medium | Supply the credit agreement schedule |
| CP-1A judged CP-2 as ready with limitations, not ready (CP-1A Consumers) | Inherited signal: the synthesis must treat post-closing structure and ownership as Not supplied | Confidence capped below High | Medium | Resolve the High gaps above |
| Release adjusted EBITDA cannot be extended to LTM (FY2025 adjusted not supplied) (CP-1) | No adjusted leverage measure is available | Definitions | Medium | Supply the fiscal Q4 2025 release |
| Contract liabilities note and balance sheet caption differ (CP-0, CP-1) | Reading of customer advances and working capital | Cash flow quality | Medium | Locate the explanation in the filed HTML |
| Pension, retiree medical, purchase commitments and factoring: nothing found in the supplied text (CP-1) | Possible claims outside the debt figure | Leverage | Low | Treat as Not supplied |
| No ratings or market data in the context | No external credit signal is available | Context | Low | Not required for the minimum set |

## Next module

- CP-5: trace each CP-2 conclusion to its CP-1 figure or CP-1A row; confirm that the 3.22x bound is marked an Analyst Inference and that no covenant ratio, post-closing leverage or TBG AG stake is stated as known; carry the two logged conflicts and the Medium confidence into the evidence review.
- Report assembly: use the credit view, key findings, strengths and weaknesses, risks and gaps as written; keep all figures as given by CP-1 and CP-1A.
