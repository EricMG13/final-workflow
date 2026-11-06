# CP-2 — Fundamental credit synthesis: Bausch Health Companies Inc. (bhc)

## Request

This module synthesises the fundamental credit view of Bausch Health Companies Inc. (issuer id `bhc`) as of 2026-11-05, for the credit_snapshot pathway, from the CP-1 financial base and the CP-1A business and transaction context. It uses upstream handoffs only and adds no new source reading; it gives no peer ranking, instrument recommendation or recovery conclusion. Amounts are USD millions as reported by the issuer, and periods are labelled Q3 2026, nine months 2026, FY2025 and LTM Q3 2026.

## Sources

Issuer sources behind the upstream handoffs (page-numbered text extractions pinned by CP-OS; this module read none of them directly and relies on the handoffs below for every figure):

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_bhc-20251231.htm.jsonl | dd4233546d8f09a0a7172210eae9b856cf06217c0da999f68b6e9a8283f6671d | Form 10-K for FY2025 |
| 10-Q_2026-03-31_bhc-20260331.htm.jsonl | 2ab4f9a58a29bd8e4f27c1aaa3b34a916ad63a6c5e24a2f2cf1f677d2bf1adb3 | Form 10-Q for Q1 2026 |
| 10-Q_2026-06-30_bhc-20260630.htm.jsonl | 9bd8cebbf75325a6e2424a90dc4ffd52c51b1a73535e612ffb413df53a0d5061 | Form 10-Q for Q2 2026 |
| 10-Q_2026-09-30_bhc-20260930.htm.jsonl | bbe6464eac7c28eba7ae73d3d4c1550a00ee295236fd32b72332e63bba1b2690 | Form 10-Q for Q3 2026 |
| EX-99.1_2026-04-29_ex991-q1x2026.htm.jsonl | a03142c8b51f52ce0bcea39df704d05d1ec6cd25d01c476f43f591aef5327135 | Q1 2026 earnings release (management) |
| EX-99.1_2026-07-29_ex991-q22026.htm.jsonl | b572ec3ee8791446c7753f44c437564f85dc7c22a9282dc8fe3094943c7ca9ed | Q2 2026 earnings release (management) |
| EX-99.1_2026-10-28_ex991-q32026.htm.jsonl | d176e2b2337e8c9ee765792690a4c9894f8e78c9eadadca91a11afce842a8bb9 | Q3 2026 earnings release (management) |
| context | ce3ba040ad702f7a097a4705cf09e05a5541c48113a20eaf4b83ee334242bc43 | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | f3a9713066d902ea831e33ca5e21c7518220ff0fc6d8658f54808a4e8892a5bd | Source readiness and gaps |
| CP-1 | 6416762ec0c950756779b461584b370e27dfe8cc5ec45b3b126353256df99610 | Financial base, leverage, liquidity, maturities, premium accounting conflict |
| CP-1A | 44d95c2186bb66af7e9424745c7b2701139cffc88c48dc61707f41e82211ccb3 | Business, ownership, transaction, governance, legal items |

Consistency with the handoffs: the CP-1 correction to CP-0 on the Bausch + Lomb note issuers stands. This module repeats CP-1 and CP-1A figures without change and recomputes only the sums shown in `## Calculations`.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Bausch Health is a highly leveraged credit on an improving path: leverage and liquidity improved in 2026, but profit depends on Xifaxan ahead of a 2027 price reset and the 2028 to 2031 maturities remain large. | Medium | No debt documents, covenant calculation or fourth quarter 2025 adjusted EBITDA are supplied, so headroom, legal capacity and an adjusted leverage ratio cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Consolidated debt to derived EBITDA fell from 6.18x at FY2025 to 5.15x at Q3 2026, and net debt to EBITDA was 4.51x. | The direction is favourable, but leverage remains high for a group rated Caa2 and B- at the corporate level. | Medium |
| Salix produced about 47% of segment profit, and Xifaxan faces a negotiated price from January 1, 2027 and expected generics in 2028. | Refinancing capacity in 2028 depends on Xifaxan cash flow surviving the price reset. | High |
| Maturities total 13,452 across 2028 to 2031, and 643 of 2027 notes are to be redeemed from cash. | Cash used for the redemption reduces the buffer ahead of the 2028 maturities. | Medium |
| Bausch + Lomb shares are pledged to the 2025 first-lien debt, and Bausch + Lomb sits outside the covenant group. | Creditors outside that structure rank behind it for Bausch + Lomb value. | High |
| Cash interest cover was 1.81x in FY2025, and interim cash interest cover is not supplied. | Debt service capacity is modest and the 2026 improvement cannot be confirmed on a cash basis. | Medium |

### Credit view

Bausch Health is a highly leveraged, structurally complex credit that is improving but not yet resilient. Its strongest support is liquidity and momentum: USD 2,485 million of consolidated cash and USD 1,135 million of undrawn revolvers at September 30, 2026, derived LTM EBITDA before goodwill impairments of USD 3,918 million, and debt to that EBITDA down from 6.18x to 5.15x [CP-1]. Its weakest point is dependence on Salix and Xifaxan, about 47% of segment profit, which faces a negotiated Medicare price from 2027 and expected generics in 2028, just before USD 3,766 million of debt falls due in 2028 [CP-1A, CP-1]. The outcome turns on how much Xifaxan cash flow survives 2027, and on whether USD 13,452 million due in 2028 to 2031 is refinanced inside a structure that ranks Bausch + Lomb value to the 2025 first-lien debt first.

### Credit assessment

| Element | Content | Category | Confidence | Basis |
| --- | --- | --- | --- | --- |
| Fundamental credit view | Highly leveraged and structurally complex, with improving earnings, cash and maturity profile, and concentrated product risk in 2027 and 2028 | Analyst Interpretation | Medium | CP-1 leverage, liquidity and maturities; CP-1A concentration, structure and timeline |
| Thesis | Bausch Health's debt service and refinancing capacity rest on Salix and Xifaxan cash flow holding through the 2027 price reset, while Bausch + Lomb value is committed first to the 2025 first-lien debt | Analyst Interpretation | Medium | CP-1A operating model, ownership and creditor structure; CP-1 maturities |
| Confidence limits | Medium, not High: the debt documents, the covenant ratio and its step-up date, the fourth quarter 2025 adjusted EBITDA and the participation terms of past exchanges are not supplied | Insufficient Information | Medium | CP-0 and CP-1 gaps; CP-1A gaps |

### Key findings

1. Leverage is falling but high. Consolidated principal debt of USD 20,168 million at September 30, 2026 (USD 20,232 million at December 31, 2025) over derived LTM EBITDA before goodwill impairments of USD 3,918 million gives 5.15x gross and 4.51x net, against 6.18x and 5.78x at FY2025 [CP-1]. Debt barely moved, so the improvement comes from earnings and from cash rising to USD 2,485 million. [Documentary Fact for the inputs; the ratio is a derived Analyst Interpretation, not a covenant measure.]
2. The parent group deleveraged in Q3 2026. Bausch Health (excl. B+L) net debt fell from USD 13,651 million to USD 13,130 million, a reduction of USD 521 million in the quarter, while its debt was USD 15,103 million [CP-1]. Bausch + Lomb debt was USD 5,065 million and its cash and revolver are generally not available to the parent [CP-1, CP-1A]. [Documentary Fact; the net debt figures are derived.]
3. Liquidity is adequate near term but thinner at the parent. Consolidated cash plus undrawn revolvers was USD 3,620 million; the parent's share was USD 2,442 million (cash USD 1,973 million including restricted cash, plus USD 469 million undrawn) [CP-1]. The USD 643 million 2027 notes will be redeemed from cash on November 30, 2026, which reduces parent liquidity to about USD 1,799 million pro forma [CP-1, calculation below]. [Analyst Interpretation.]
4. The maturity wall starts in 2028. Debt maturing is USD 15 million in the remainder of 2026, USD 701 million in 2027, USD 3,766 million in 2028, USD 1,667 million in 2029, USD 4,123 million in 2030 and USD 3,896 million in 2031, with USD 6,000 million thereafter [CP-1]. The parent's 2028 maturities of USD 2,326 million exceed its pro forma liquidity of about USD 1,799 million, so repayment relies on cash generation or refinancing; the revolver also has an earlier-maturity trigger tied to indebtedness above USD 1,000 million [CP-1, CP-1A]. [Analyst Interpretation.]
5. Earnings quality is price-led and concentrated. Salix revenue rose USD 343 million in nine months 2026 on price of USD 504 million, partly offset by volumes down USD 173 million, and Salix is about 27% of revenue but about 47% of segment profit [CP-1A]. Xifaxan is about 85% of Salix, faces a negotiated Medicare price from January 1, 2027 and expected generics in 2028, and the company impaired Salix goodwill by USD 1,426 million in January 2026 after failed Phase 3 trials [CP-1A]. [Documentary Fact; the concentration shares are derived.]
6. Cash interest absorbs a large share of earnings. FY2025 cash interest was USD 1,810 million against derived EBITDA before goodwill impairments of USD 3,276 million, about 55% of it and a cover of 1.81x, and the pack gives no interim cash interest [CP-1]. Premium accounting makes P&L interest lower than cash interest, so cover on a P&L basis (2.53x LTM Q3 2026) is flattered [CP-1]. [Documentary Fact for inputs; Analyst Interpretation on direction.]
7. Structure matters as much as leverage. The 2025 first-lien debt at 126NumberCo holds a lien on 211,963,893 Bausch + Lomb shares, and sales proceeds must prepay it pro rata with the 2032 notes; other secured and unsecured notes rank structurally behind, and Bausch + Lomb's earnings and net debt are outside the covenant [CP-1A]. Legal capacity and exchange terms cannot be tested without the debt documents. [Documentary Fact.]
8. Governance evidence is mixed rather than adverse. No dividends and a USD 50 million buyback authorised, a cash repurchase of near-par unsecured notes in 2025 and extended maturities weigh against overlapping leadership of two listed entities and unresolved terms of exchanges [CP-1A]. [Analyst Interpretation.]

### Strengths and weaknesses

Strengths:

- Earnings recovery with deleveraging. Derived LTM EBITDA before goodwill impairments rose from USD 3,276 million (FY2025) to USD 3,918 million (LTM Q3 2026) while principal debt stayed near USD 20,200 million, lowering gross leverage by about one turn [CP-1]. This reduces default risk on a going-concern basis. [Analyst Interpretation.]
- Refinancing already done. The 2025 refinancing and the December 2025 exchange extended about USD 6,870 million and USD 1,600 million of maturities to 2030 through 2032, so only USD 716 million falls due before 2028 on a consolidated basis, and USD 643 million of that is to be redeemed from cash [CP-1, CP-1A]. [Documentary Fact for the transactions; the 716 sum is derived.]
- Cash and parent deleveraging. Cash of USD 2,485 million and parent net debt down USD 521 million in Q3 2026 show cash generation reaching the parent group [CP-1]. [Documentary Fact.]
- Covenant exposure is limited and stated compliant. The revolver has two maintenance tests, and the company states compliance at September 30, 2026 [CP-1]. [Documentary Fact; the headroom is Not supplied.]
- Diversification outside Salix. International, Solta Medical and Bausch + Lomb grew in nine months 2026, and Bausch + Lomb produced about 27% of segment profit [CP-1A]. [Documentary Fact; the share is derived.]
- No shareholder leakage. No dividends in FY2025, FY2024 or FY2023, and restrictions in the debt documents [CP-1A]. [Documentary Fact.]

Weaknesses:

- Product concentration with dated erosion. Salix and Xifaxan dominate segment profit, and the negotiated price and generic entry are dated [CP-1A]. Mechanic: price-led growth meets a price cap, then volume loss. Implication: lower cash available for 2028 refinancing. [Documentary Fact for the dates; Analyst Interpretation on the effect.]
- High leverage and modest cash cover. 5.15x gross leverage and 1.81x FY2025 cash interest cover leave limited tolerance for a profit decline [CP-1]. [Analyst Interpretation.]
- Large 2028 to 2031 maturities, USD 13,452 million in total, with USD 8,422 million of it at the parent [CP-1, calculation below]. [Analyst Interpretation.]
- Structural subordination and a separate Bausch + Lomb silo. Value in the Bausch + Lomb stake serves the 2025 first-lien debt first, and its cash is generally trapped [CP-1A]. [Documentary Fact.]
- Weak credit ratings: Moody's Caa2 and S&P B- corporate, with a negative outlook at S&P and Rating Watch Evolving at Fitch [CP-1, CP-1A]. [Documentary Fact.]
- Litigation and regulatory exposure: antitrust class actions on the Xifaxan settlement, a Luxembourg tax assessment with no reserve, an FDA warning letter at a Bausch + Lomb plant, and talc claims backed by an indemnity from Johnson & Johnson whose performance the pack does not test [CP-1A]. [Documentary Fact; amounts of exposure are Not supplied.]
- Opaque adjusted measures. Adjusted EBITDA and adjusted cash flow are management-defined, and the fourth quarter of 2025 is missing, so no adjusted LTM leverage exists [CP-0, CP-1]. [Insufficient Information.]

### Key credit risks

| Risk | Mechanic | Credit implication | Severity | Category |
| --- | --- | --- | --- | --- |
| Xifaxan price reset and generic entry | Negotiated Medicare price from 2027 and expected generics in 2028 hit a product that supplies most of Salix profit, after price-led growth | Lower cash available for 2028 maturities; leverage tolerance falls | Critical | Documentary Fact for dates; Analyst Interpretation for effect |
| Refinancing of 2028 to 2031 maturities | USD 13,452 million falls due across four years while the revolver may mature earlier under its trigger, and cash is used for the 2027 notes redemption | Reliance on market access at a Caa2 and B- corporate rating; cost of debt may rise | Critical | Analyst Interpretation |
| Leverage and interest burden | 5.15x gross leverage, 1.81x FY2025 cash interest cover, premium accounting masks cash interest | Little tolerance for earnings decline; debt service sensitive to rates on variable debt | Material | Analyst Interpretation |
| Structural subordination and Bausch + Lomb silo | First-lien claims at 126NumberCo have priority on the pledged shares; Bausch + Lomb cash and earnings are outside the parent covenant | Recovery prospects for creditors outside the structure depend on residual value; no recovery outcome is stated | Material | Documentary Fact |
| Unsupplied covenant and document terms | Covenant ratio, step-up date, baskets and exchange terms are not in the pack | Headroom and creditor protection cannot be verified | Material | Insufficient Information |
| Legal and regulatory | Antitrust, tax, talc indemnity reliance, FDA findings | Cash payments or earnings loss if outcomes adverse; amounts not supplied | Material | Documentary Fact |
| Governance and separation path | Overlapping leadership; separation subject to leverage targets and approvals | Uncertain timing and form of any separation affects collateral value and creditor control | Minor | Analyst Interpretation |

## Calculations

Inputs are the figures stated in the CP-1 and CP-1A handoffs. All amounts USD millions.

- Maturities 2028 to 2031, consolidated: 3,766 + 1,667 + 4,123 + 3,896 = 13,452. Parent only: 2,326 + 1,639 + 3,995 + 462 = 8,422. Bausch + Lomb only: 1,440 + 28 + 128 + 3,434 = 5,030. Check: 8,422 + 5,030 = 13,452.
- Maturities before 2028, consolidated: 15 + 701 = 716; after the 643 redemption: 716 − 643 = 73.
- Parent liquidity, September 30, 2026: cash, cash equivalents and restricted cash 1,973 + undrawn 2030 Revolving Credit Facility 469 = 2,442. Pro forma for the redemption of 643 funded from cash: 2,442 − 643 = 1,799. The pro forma ignores any redemption premium, accrued interest, fourth quarter interest of about 561 consolidated, capital expenditure and cash generation after September 30, 2026.
- Pro forma parent liquidity against 2028 parent maturities: 1,799 / 2,326 = 0.77x.
- Parent cash generation, nine months 2026, management's adjusted cash flows from operations for Bausch Health (excl. B+L): 319 (Q1) + 471 (Q2) + 539 (Q3) = 1,329. Full year 2026 guidance for this measure is 1,600 to 1,675, which implies 271 to 346 for the fourth quarter (1,600 − 1,329 and 1,675 − 1,329). These are non-GAAP management figures and a forecast.
- Parent net debt reduction in Q3 2026: 13,651 − 13,130 = 521, from CP-1.
- FY2025 cash interest relative to derived EBITDA before goodwill impairments: 1,810 / 3,276 = 55.2%, and the inverse 3,276 / 1,810 = 1.81x.

## Gaps

Revision history: first answer for this module; no earlier attempt. Readiness: CP-0 judged all four consumers READY_WITH_LIMITATIONS; CP-1 and CP-1A are accepted with the gaps below carried forward.

| Gap | Severity | Affected | Action |
| --- | --- | --- | --- |
| Credit agreement, indentures, intercreditor terms and collateral documents not supplied: covenant definitions, baskets, designation tests and legal capacity cannot be assessed | High | Assessment, risks on structure and documents | Supply executed documents from the exhibit list |
| Reported Blended First Lien Leverage Ratio, liquidity covenant figure and Covenant Step Up Date not supplied; headroom Not calculable | High | Confidence in liquidity and covenant conclusions | Supply compliance certificate and the credit agreement |
| Fourth quarter 2025 adjusted EBITDA not supplied; no LTM adjusted leverage; ratios use a derived measure | High | Leverage findings | Supply the fourth quarter 2025 release |
| Interim cash interest paid not supplied; interim cash cover Not supplied | High | Interest burden risk | Supply the cash flow supplemental disclosure |
| Quantified effect of the 2027 Xifaxan price and of generic entry on revenue and profit not supplied | High | Xifaxan risk | Request management detail; monitor quarterly |
| Participation terms of the 2022 and December 2025 exchanges and legal capacity for them not supplied | High | Governance finding | Supply exchange documents |
| Bausch + Lomb standalone filings and its covenant levels not supplied | Medium | Structure and perimeter | Supply Bausch + Lomb Form 10-Q and credit agreement |
| Holder and pledge status of the Bausch + Lomb shares outside the 126NumberCo holding not stated | Medium | Structural subordination | Supply collateral schedule |
| Legal and tax outcomes after October 29, 2026 not supplied, including the Luxembourg appeal judgment | Medium | Legal risk | Supply later filings |
| Operating lease and pension balances at September 30, 2026 not supplied | Medium | Fixed obligations outside debt | Use December 31, 2025 lease table as latest |
| Current debt of USD 866 million against USD 716 million of principal due by end of 2027 not reconciled (CP-1) | Medium | Near-term liquidity reading | Read the current portion composition in the debt note |
| Conflict on interest charged against premium for nine months 2026 (USD 158 million in the filing, USD 144 million in the release) not reconciled | Medium | Cash flow reading | Treat the filing as controlling |

## Next module

CP-5 follows to trace the evidence behind the material claims in CP-0, CP-1, CP-1A and this module. It should check in particular the derived EBITDA basis and LTM construction, the 5.15x and 4.51x ratios, the parent and Bausch + Lomb splits, the 13,452 and 8,422 sums, the pro forma parent liquidity of 1,799, and the correction of CP-0 on the Bausch + Lomb note issuers.
