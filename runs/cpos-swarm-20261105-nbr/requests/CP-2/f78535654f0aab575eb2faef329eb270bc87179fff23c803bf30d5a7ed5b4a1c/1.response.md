## Request

- Issuer: NABORS INDUSTRIES LTD (issuer id nbr, NYSE: NBR), the Bermuda holding company that reports consolidated results including the SANAD joint venture.
- As-of date: 2026-11-05. Evidence cutoff: 2026-11-05.
- Pathway: credit_snapshot. Reporting currency: USD. Current period Q3 2026 and its LTM; prior period FY2025.
- Task for this module: the fundamental credit synthesis a committee reads first, built only from the settled upstream handoffs: business risk and transaction context from CP-1A, financial risk and liquidity from CP-1, and the gaps that limit both. No source text is quoted here; the evidence is upstream, and the issuer sources are listed because the upstream handoffs rest on them.
- Constraints honoured: no peer ranking, no instrument recommendation and no recovery conclusion. Recovery prospects appear only as a mechanic. Missing evidence is never treated as an adverse conclusion.
- Category tags used: Documentary Fact (an upstream Documentary Fact row or a CP-1 figure states it), Management Language (management's characterisation carried by an upstream row, qualified and not adopted), Analyst Interpretation (a reading of the cited basis) and Insufficient Information (the basis is missing; the missing datapoint is stated).
- Inherited signals: CP-1A records its readiness judgment for this module as READY_WITH_LIMITATIONS, not READY, and logs no Critical gap; CP-1 and CP-0 carry source limitations. Confidence in the assessment is therefore set below High.
- Settings file `context` is user input, not issuer evidence; ratings, quotes, valuation inputs and sponsor are blank and treated as not supplied, never as zero.

## Sources

### Issuer sources underlying the upstream handoffs

| Source name | sha256 | Role here |
| --- | --- | --- |
| 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | 427cc2fc64bcd723a27a6c2478a12093e219dc045e02d41b40eab49061568751 | Reached through CP-1 and CP-1A: audited FY2025 statements, business, customers, related parties |
| 10-Q_2026-03-31_nbr-20260331x10q.htm.jsonl | 11eb9a5886137a3201a1d5b34cd6e8ef50e247d641cd61ec9c9814adc458e187 | Reached through CP-1: March 31, 2026 debt and covenant |
| 10-Q_2026-06-30_nbr-20260630x10q.htm.jsonl | 6c2a6d1bdbcbd71ad95906094386639f0ffd409dc513dcadc487db645242cb3b | Reached through CP-1: June 30, 2026 debt and covenant |
| 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | 7e240e48875d03a0d84a20d6f741fc0c9988f286076c7c4d265721b0e0793ce2 | Reached through CP-1 and CP-1A: latest statements, debt, liquidity, SANAD |
| EX-99.1_2026-04-28_tm2612942d1_ex99-1.htm.jsonl | 811d6f2d82a109aad668cd621d65877dd4784a4f2a4d17ed4d8fd9b20e6f9b37 | Reached through CP-1 and CP-1A: Q4 2025 and Q1 2026 columns |
| EX-99.1_2026-07-28_tm2621313d2_ex99-1.htm.jsonl | 4fe99e5d4274f6274ec08f0c05beac58f1ab8c742acabe22ed57e9e2bd36a4e7 | Reached through CP-1 and CP-1A: Q2 2026 columns |
| EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | f9d4d37c25f2acc92f4bf176ff35ad6539e2f40b8c58a320a92c16c59d447e59 | Reached through CP-1 and CP-1A: Q3 2026 columns, guidance, rig suspensions (management statements) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 2447d4a661e92334753a8e1c6e3f04df86843d3399afe1ed1f2ac26814412213 | Run settings only; not issuer evidence |

### Upstream handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 01371c96badec91a1c024971fd80be337cc1aa2bfcd663093f556e7185d90614 | Source readiness and gaps |
| CP-1 | 52018b6902eb6b45bb6e53a2bf745847730117a063b22f7e4d05d077344c3098 | Financial base: leverage, coverage, liquidity, maturities, definitions |
| CP-1A | f02a6fc7d78a4d519e49400e20ea3798cf539d2c21918de4595f30dd43ae553c | Business, transaction, governance, conflicts, readiness judgment for this module |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Nabors has moderate leverage, no maturities before June 2029 and 825.1 US$m of liquidity, but earnings and receivables lean on Saudi Aramco and the SANAD venture. The credit view is balanced, with business risk the main weakness. | Medium | Cash interest for 2026, the covenant EBITDA definition, SANAD earnings and backlog are not available, and the October rig-suspension news is a management statement. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| About 30% of FY2025 revenue comes from Saudi Aramco, 41% of receivables are in Saudi Arabia, and management reports five suspended SANAD rigs. | One counterparty's rig program drives earnings, receivables and capital needs, so Saudi activity is the key monitoring item. | High |
| Net debt is 1.76x LTM adjusted EBITDA, notes at face value are 2,050.0 US$m, and the first maturity is in June 2029. | Leverage is moderate and near-term refinancing risk is low, but the gross debt reduction came from cash, not from surplus cash flow. | Medium |
| Liquidity fell to 825.1 US$m from 1,290.7 US$m, and 180.6 US$m of cash sits in the half-owned SANAD venture. | The parent-level cushion is smaller than the headline, which matters if the receivables facility is not renewed after April 1, 2027. | Medium |
| Free cash flow after net capital spending was 170.4 US$m LTM against annual note coupons of 156.8 US$m. | Fixed charges are covered with little spare cash, and the margin depends on the timing of SANAD capital spending. | Medium |
| No sponsor or creditor-adverse action is documented; related-party arrangements and unavailable ownership detail remain monitoring items. | Governance adds no identified risk, but it cannot be fully assessed without the proxy statement and the legal documents. | Medium |

### Credit view

The fundamental credit view of Nabors Industries Ltd as of 2026-11-05 is balanced, with financial risk moderate and business risk elevated, and the confidence is Medium because the evidence is complete enough to judge direction but several datapoints that would move the view are missing. On the financial side, notes at face value stand at 2,050.0 US$m, net debt is 1,574.9 US$m or 1.76x LTM adjusted EBITDA of 893.6 US$m, gross leverage is 2.29x, no note matures before the 250.0 US$m exchangeable notes in June 2029, the revolver is undrawn at 350.0 US$m, and the reported covenant interest coverage of 5.20x sits well above the 2.75x minimum. The weakening features are the use of cash to fund the deleveraging, which lowered liquidity from 1,290.7 to 825.1 US$m while net leverage stayed flat at 1.74x to 1.76x, and a free cash flow margin over fixed charges that is thin. On the business side, Saudi Aramco is about 30% of FY2025 operating revenues and the 50% partner in the consolidated SANAD venture, so revenue durability, receivables, a large newbuild capital program and a change-of-control call option all depend on one relationship; the filings show reactivations of Saudi rigs during 2026 and the October release reports five suspended SANAD rigs, which are management statements not yet in a filing. Governance evidence is neutral to supportive: debt has been repaid in cash, no sponsor or creditor-adverse action is documented, and the related-party arrangements are disclosed but only partly quantified. What would change the view: confirmed Saudi suspensions that cut earnings or collections, a non-renewal of the receivables facility, or evidence that SANAD cash and earnings are less accessible to creditors than the consolidated figures imply would weaken it; sustained free cash flow above fixed charges and further cash-funded debt reduction without eroding liquidity would strengthen it.

### Credit assessment

| Item | View | Category | Confidence | Basis |
| --- | --- | --- | --- | --- |
| Fundamental credit view | Balanced: moderate financial risk, elevated business risk from customer and joint venture concentration; no recovery outcome or relative value is stated | Analyst Interpretation | Medium | CP-1A: concentration, SANAD mechanics, governance behaviour, conflicts; CP-1: leverage, liquidity, maturity and covenant figures |
| Financial risk and liquidity | Moderate leverage, adequate liquidity with a smaller cushion than at FY2025, no near-term maturity | Documentary Fact | Medium | CP-1: Chart data leverage, liquidity and debt maturities; Financials and credit metrics |
| Business risk | Elevated by concentration in Saudi Aramco and SANAD, offset by diversified segments and technology revenue | Analyst Interpretation | Medium | CP-1A: customers, operating model, ownership rows |
| Limits on the view | Cash interest for 2026, covenant EBITDA, guarantor and ranking detail, SANAD earnings, backlog and beneficial ownership are not available | Insufficient Information | Not applicable | CP-0 and CP-1 gaps; CP-1A gaps |

### Credit thesis

| Thesis | Category | Basis |
| --- | --- | --- |
| Nabors is a moderately levered, diversified drilling contractor with a clear maturity runway and sound reported covenant headroom whose credit quality is set mainly by the durability of its Saudi Aramco and SANAD relationship and by whether free cash flow keeps pace with fixed charges. | Analyst Interpretation | CP-1 leverage, liquidity, maturity and cash flow figures; CP-1A concentration and SANAD rows |

### Key findings

The most important finding is concentration: Saudi Aramco accounted for about 30% of FY2025 consolidated operating revenues, the three largest contract drilling customers for about 41%, and about 41% of net receivables at September 30, 2026 were in Saudi Arabia. Because Aramco contracts are per rig and mainly run through SANAD, a customer decision to idle rigs cuts revenue and earnings without any contract termination, and the October release reports five suspended SANAD rigs against a quarter in which rig counts rose. That statement is management's, and until a filing confirms it the size of the effect cannot be stated.

The second finding is that leverage is moderate and has fallen on a gross basis only. Notes at face value fell from 2,529.1 to 2,050.0 US$m, gross leverage from 2.77x to 2.29x, but net debt moved only from 1,588.4 to 1,574.9 US$m, because the redemptions of the 2028 notes and part of the 2030 notes were paid from cash that fell from 940.7 to 475.1 US$m. Liquidity of cash plus the undrawn revolver therefore fell from 1,290.7 to 825.1 US$m. Third, the maturity profile is long: nothing matures before 250.0 US$m in June 2029, followed by 550.0, 550.0 and 700.0 US$m in 2030, 2031 and 2032, and the revolver runs to the earlier of June 17, 2029 and a springing date tied to the exchangeable notes; this limits refinancing risk for several years but concentrates 1,800.0 US$m in 2030 to 2032.

Fourth, free cash flow after net capital expenditures was 170.4 US$m on an LTM basis, 38.6 US$m for nine months 2026 and 74.5 US$m in Q3 2026, against annual coupons of 156.8 US$m on the notes outstanding; management guides full-year adjusted free cash flow of 100 to 110 US$m with SANAD newbuild spending included, and says Q3 spending was below forecast because milestones shifted. Fifth, SANAD is consolidated in full: 180.6 US$m of cash and 100% of its EBITDA are in the consolidated figures although Saudi Aramco owns half, redeemable noncontrolling interest of 502.7 US$m ranks as mezzanine equity, and Nabors has a disclosed backstop for its share of the first 25 rig purchases. Sixth, FY2025 earnings include Quail Tools, sold in August 2025, so LTM adjusted EBITDA of 893.6 US$m, against 912.7 US$m for FY2025, is the cleaner base; seventh, no sponsor, dividend recapitalisation or creditor-adverse action is documented, though related-party arrangements and the ownership gap remain to be monitored. Last, 2026 cash interest and the covenant EBITDA definition are not available, so coverage rests on interest expense (4.99x) and the reported covenant ratio.

### Strengths and weaknesses

Strengths. Moderate leverage with a long runway: net leverage of 1.76x on face value, the first maturity in June 2029, and a revolver that is undrawn and matures no earlier than that date. Reported covenant headroom is wide, with interest coverage at 5.20x against 2.75x and minimum guarantor value at 99.8% against 90%, though the covenant definition is not available to test. Diversification across four segments and across the U.S. and international drilling, with technology and equipment segments that sell to third parties. A demonstrated willingness to repay debt in cash and to refinance ahead of maturity, shown by the 2025 refinancing and the 2026 redemptions. Adjusted EBITDA on an LTM basis is above 890 US$m with interest cover on interest expense of 4.99x and falling coupons.

Weaknesses. Concentration in Saudi Aramco and in SANAD, which supplies about 30% of revenue and carries a rig-purchase backstop, a call option on Nabors' interest on a change of control, and a redeemable noncontrolling interest. A smaller liquidity cushion of 825.1 US$m, of which 180.6 US$m is SANAD cash, and a receivables facility of 168.0 US$m sold whose term may end on April 1, 2027. Thin free cash flow cover of fixed charges and dependence on the timing of SANAD capital spending. Heavy dependence on issuer-defined adjusted EBITDA that excludes certain cash expenses and includes all of SANAD. Information gaps on guarantors, ranking, covenant definitions, backlog and ownership. History distorted by gains and disposals in FY2025.

### Basis register

| Label | Type | Text | Category | Basis |
| --- | --- | --- | --- | --- |
| Leverage and runway | Strength | Net leverage 1.76x on face value; first maturity June 2029; revolver undrawn | Documentary Fact | CP-1: Chart data leverage, debt maturities; Financials and credit metrics |
| Covenant headroom | Strength | Reported interest coverage 5.20x against 2.75x minimum; guarantor value 99.8% against 90% | Documentary Fact | CP-1: covenants and reported compliance |
| Diversified segments | Strength | Four segments across U.S., international, technology and equipment | Documentary Fact | CP-1A: Company and operating model rows |
| Debt reduction record | Strength | Cash redemptions in 2025 and 2026 and a 2025 refinancing | Documentary Fact | CP-1A: governance (deleveraging) and transaction rows; CP-1 debt table |
| Customer and venture concentration | Weakness | Saudi Aramco about 30% of FY2025 revenue; SANAD per-rig contracts; change-of-control call option; backstop | Documentary Fact | CP-1A: customers, ownership and SANAD rows |
| Rig suspension news | Weakness | Release reports five SANAD rigs suspended after quarter end | Management Language | CP-1A: subsequent events and Saudi activity rows |
| Liquidity cushion | Weakness | 825.1 US$m including 180.6 US$m of SANAD cash; receivables facility term may end April 1, 2027 | Documentary Fact | CP-1: Chart data liquidity; funding and off-debt claims |
| Fixed charge cover | Weakness | LTM free cash flow after net capital expenditures 170.4 US$m against annual coupons 156.8 US$m | Analyst Interpretation | CP-1: cash flow and coverage calculations |
| Earnings definition | Weakness | Adjusted EBITDA is issuer-defined, excludes certain cash expenses and consolidates all of SANAD | Documentary Fact | CP-1: Definition review |
| Information gaps | Weakness | Guarantors, ranking, covenant definitions, backlog, SANAD earnings and ownership not in the pack | Insufficient Information | CP-0 gaps; CP-1 gaps; CP-1A gaps |

### Key credit risks

| Risk | Mechanic | Credit implication | Severity | Basis |
| --- | --- | --- | --- | --- |
| Saudi activity and counterparty concentration | Per-rig contracts let the customer idle rigs; suspensions cut revenue, EBITDA and receivable inflows together while newbuild commitments continue | Debt service capacity depends on one rig program; monitor SANAD rig counts and Saudi receivables each quarter | Material | CP-1A: customers, SANAD, Saudi activity, conflict on Aramco share; CP-1: receivables concentration |
| SANAD cash access and capital calls | Consolidation counts all SANAD cash and EBITDA, but cash reaches Nabors only through distributions, exchange of redeemable interests or agreement of the owners; a backstop for rig purchases exists | Parent-level liquidity and leverage are weaker than consolidated figures; contingent funding is unquantified | Material | CP-1A: SANAD rows, backstop gap; CP-1: Funding and off-debt claims |
| Liquidity erosion and receivables facility | Debt reduction used cash; the facility's term may end April 1, 2027 and funds a share of receivables | A non-renewal or a Saudi collection delay would draw on a smaller cushion | Material | CP-1: Chart data liquidity; receivables sold |
| Free cash flow after SANAD capital spending | Cash generation after net capital spending only just exceeds coupons; SANAD milestones have moved to later periods | Delayed spending could reverse into later-year cash needs; deleveraging beyond redemptions requires cash flow above coupons | Material | CP-1: cash flow and coverage; CP-1A: operating model rows |
| Cycle and pricing | Daywork contracts reprice with activity; U.S. dayrates were lower at the margin in Q3 2026 with higher rig counts; efficiency gains reduce rigs needed | Earnings are sensitive to U.S. activity and international pricing | Minor | CP-1A: operating model rows; CP-1 segment data |
| Refinancing of the 2030 to 2032 stack | 1,800.0 US$m of notes mature in 2030 to 2032 | Not near term; depends on access to capital markets and ratings, which are not supplied | Minor | CP-1: Chart data debt maturities; CP-0 gap on ratings |
| Structure and ranking | A secured first-lien revolver on U.S. land rigs sits alongside notes whose guarantee and security terms are not in the pack; recovery depends on collateral and guarantor detail that cannot be assessed; no recovery outcome is stated | Structural questions remain open until the indentures and credit agreement are read | Minor | CP-1: debt table and definition review; CP-0 gaps |
| Governance and related parties | Management-linked arrangements and ownership detail that is not available | No creditor-adverse action is documented, but monitoring is needed | Minor | CP-1A: governance and sponsor behaviour rows |

### Gaps ledger

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Cash paid for interest for 2026 and the covenant definition of EBITDA are not available | Coverage rests on interest expense and the reported ratio; covenant headroom cannot be turned into EBITDA headroom | Financial risk, covenants | Material | Add the credit agreement and cash flow supplement |
| SANAD stand-alone earnings, cash needs, backlog and contract terms are not disclosed | Concentration and cash access cannot be sized | Business risk, liquidity | Material | Request venture-level data |
| Guarantor lists, ranking and security of the notes, and call or put terms are not in the pack | Structural priority and refinancing flexibility | Structure, refinancing | Material | Add the indentures |
| Beneficial ownership, director independence and related-party detail are in the proxy statement, which is not in the pack | Control and alignment | Governance | Minor | Add the 2026 proxy statement |
| Release-only statements (five suspended rigs, guidance, run rate) are not in a filing | Management Language, not filed fact | Business risk | Minor | Confirm in the next filing |
| Inherited signal: the business handoff judges this module READY_WITH_LIMITATIONS, not READY | Confidence cannot be High | Whole assessment | Minor | Close the gaps above before raising confidence |
| Conflicts logged and not reconciled: Quail Tools sale size, exchangeable notes maturity label, Aramco share versus related-party revenue, Parker gain timing, domicile | Small effects on specific figures, none on direction | Evidence trace | Minor | Resolve in documents if they are added |
| Ratings, quotes and market data are not supplied | Market access and relative value cannot be assessed here | Refinancing | Minor | Not supplied in context |

## Calculations

All inputs are CP-1 figures in US$ thousands unless stated; no source text is used. These are relationships among settled figures, not new financial extraction.

| Item | Formula and inputs | Result |
| --- | --- | --- |
| Net debt on face value, check | 2,050,000 - 475,145 | 1,574,855, equal to CP-1 |
| Net leverage, check | 1,574,855 / 893,571 | 1.76x, equal to CP-1 |
| Liquidity, check | 475,145 + 350,000 | 825,145, equal to CP-1 |
| Liquidity relative to annual coupons | 825,145 / 156,750 | 5.26x |
| Liquidity excluding SANAD cash | 294,437 cash and cash equivalents outside SANAD + 350,000 undrawn revolver | 644,437 |
| Liquidity if the receivables facility amount sold were to be funded from cash (a stress, not a forecast) | 825,145 - 168,000 | 657,145 |
| SANAD share of cash and cash equivalents | 180,635 / 475,072 | 38.0% |
| LTM free cash flow after net capital expenditures relative to annual coupons | 170,444 / 156,750 | 1.09x |
| Saudi Aramco share of FY2025 revenue in amount (rounded input) | 30% x 3,184,693 | about 955,408 |
| Notes maturing 2030 to 2032 | 550,000 + 550,000 + 700,000 | 1,800,000 |
| Share of notes maturing 2030 to 2032 | 1,800,000 / 2,050,000 | 87.8% |
| Change in net debt at face value, December 31, 2025 to September 30, 2026 | 1,574,855 - 1,588,408 | decrease of 13,553 |
| Change in notes at face value | 2,050,000 - 2,529,146 | decrease of 479,146 |
| Change in cash and short-term investments | 475,145 - 940,738 | decrease of 465,593 |

## Gaps

| ID | Gap | Why it matters | Action |
| --- | --- | --- | --- |
| K1 | The synthesis uses issuer-defined adjusted EBITDA and reported covenant ratios; covenant EBITDA and 2026 cash interest are not available | Coverage and headroom conclusions are bounded | Add the credit agreement and supplemental cash flow data |
| K2 | SANAD stand-alone financials, backlog and the rig-purchase backstop terms after the first 25 rigs are not quantified | Concentration, cash access and contingent funding | Request venture data |
| K3 | Executed legal documents, ratings and market quotes are not supplied | Structure, ranking and market access | Add indentures and credit agreement |
| K4 | Ownership and proxy-based governance detail are not in the pack | Alignment cannot be assessed beyond documented actions | Add the proxy statement |
| K5 | Management statements dated after September 30, 2026 are not in a filing | They are carried as attributed | Confirm in the next filing |
| K6 | Confidence is capped below High by the READY_WITH_LIMITATIONS judgment of the business handoff and the gaps above | The view is directional, not precise | Revisit when gaps close |

## Next module

CP-5 follows. It should trace each claim in this handoff to the upstream rows it cites, check that every figure matches CP-1 exactly (net debt, leverage, liquidity, free cash flow and coupons), confirm that management statements remain tagged Management Language, and confirm that the conflicts logged in the business handoff are carried and not resolved. It should also confirm that this handoff states no recovery outcome, peer ranking or instrument recommendation, and that confidence stays below High while the gaps above remain.
