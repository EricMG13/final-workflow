# CP-2 — Fundamental credit synthesis: SERVICE CORP INTERNATIONAL (sci)

## Request

SERVICE CORP INTERNATIONAL (issuer id `sci`), as of 2026-11-05, pathway credit_snapshot, current period Q3 2026 and prior period FY2025 in USD. This module synthesises the fundamental credit view from the CP-1 financial base and the CP-1A business context, using upstream handoffs only. It gives no peer ranking, instrument recommendation or recovery conclusion.

## Sources

CP-2 reads the two upstream handoffs and the readiness handoff; it quotes no source text. The issuer sources behind them are listed for traceability.

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_sci-20251231.htm.jsonl | 36f224c032003fbd2390907d9603b5b257c583b876df570b13d8b342fe4f5f00 | FY2025 annual report behind the upstream figures |
| 10-Q_2026-03-31_sci-20260331.htm.jsonl | e6b5e437aefdd3d93a7df7ee4a72da856eb2c3e8d8864dff282c77ac49311d26 | Q1 2026 quarterly report |
| 10-Q_2026-06-30_sci-20260630.htm.jsonl | 3f4554fa1a62f231e9dd455be55fe862d78b2b61391019d236799268dd70b592 | Q2 2026 quarterly report |
| 10-Q_2026-09-30_sci-20260930.htm.jsonl | 236742c90fb88a0fc6e3b830a1a819da8579c8436891d794242d5625f7bae113 | Q3 2026 quarterly report |
| EX-99.1_2026-04-29_exhibit991q126earningsrele.htm.jsonl | dc7d39675688d257986d7838f6da2271b0d5a328325d0081a47485a7f2412e53 | Q1 2026 earnings release |
| EX-99.1_2026-07-29_exhibit991q226earningsrele.htm.jsonl | 8ffbca4fd985e89d67fcf44643913b74684aa9a27e65aeca772948faf99925ff | Q2 2026 earnings release |
| EX-99.1_2026-10-28_exhibit991q326earningsrele.htm.jsonl | d5fe76c2497f82e8e53c22501a405cf8fb7df74cae0b9bd5b7f0b933f384c2b3 | Q3 2026 earnings release, revised outlook |
| context | 65d65475c254be68b493ea4436b1695cdda5a813079114b87a550c9ce00dd797 | Run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | a4424fa5ae507987bbabfc0ea081c1e6d0634859958366cc6d6a3e21db770495 | Source readiness and inherited limits |
| CP-1 | b2929721b6dd1fe38c8e3fe6a91d3ab13c7f3197b5f3265b7ede5c6f6e3cdc9f | Financial base, debt register, liquidity, covenant as reported, claims outside debt |
| CP-1A | b01abf4ad8bf7d83bda476fbd5b626e74996926a7ff4ea4e5b5602e926d1af16 | Business model, ownership, capital allocation behaviour, conflicts, readiness of this module |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The company looks like a stable, cash-generative credit with moderate-to-high leverage, ample liquidity and distant maturities. Its estimated leverage is above the reported covenant figure, and shareholder returns are the main discretionary use of cash. | Medium | The covenant definition, credit agreement and ratings are not supplied, so headroom and creditor protections cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Liquidity is 1,686.4 million US dollars and the revolver and term loan mature in November 2030. | Maturities through April 2027 and December 2027 are well covered. | High |
| Estimated gross leverage is 4.15x and net leverage 4.01x, against a reported covenant ratio of 3.69 and a maximum of 5.00. | Reported headroom is wide, but our estimate cannot be tied to the covenant. | Medium |
| Funeral volumes and gross profit are falling, cemetery earnings are rising, and the 2026 earnings outlook was lowered after the quarter. | Margins are under pressure from selling and healthcare costs. | Medium |
| Shareholder returns exceeded operating cash flow after capital expenditure in FY2025 and were covered by it in the nine months of 2026. | Debt reduction is not the priority; leverage stays near its target range. | Medium |

### Credit view

SERVICE CORP INTERNATIONAL is a stable, cash-generative credit with moderate-to-high leverage that its liquidity comfortably supports. Its strongest support is a USD 17.72 billion preneed backlog, USD 1,686.4 million of liquidity at September 30, 2026 and a revolver and term loan that do not mature until November 2030. The weakest point is margin pressure: funeral volumes are falling, selling and healthcare costs are rising and the issuer lowered its 2026 earnings outlook, while distributions to shareholders stay high. Our estimated gross leverage of 4.15x is above the reported covenant ratio of 3.69x, and the covenant definition is not supplied. What decides the outcome is whether cemetery growth and pricing keep offsetting funeral volume loss without more debt-funded buybacks.

### Key findings

1. Liquidity and maturities are the issuer's clearest strength. Cash of USD 172.7 million plus undrawn revolver capacity of USD 1,513.7 million gives USD 1,686.4 million, against current maturities of USD 195.1 million at September 30, 2026. The nearest bond maturity is USD 136.9 million of 7.500% notes due April 2027, then USD 550.0 million of 4.625% notes due December 2027. The revolver (USD 1,750.0 million commitment) and the term loan mature in November 2030 [CP-1 liquidity table and debt register].
2. The debt stack is simple and mostly fixed-rate: six series of senior notes totalling USD 3,886.9 million, a USD 735.9 million term loan, a USD 235.0 million revolver draw, a USD 110.9 million headquarters facility, USD 160.5 million of finance leases and USD 76.1 million of mortgage and other debt. Total debt is USD 5,172.9 million at carrying value and USD 5,205.4 million before issuance costs. About 79% is fixed-rate. Security and guarantor terms for the notes are not supplied, so ranking cannot be assessed [CP-1 debt register; CP-0 gaps].
3. Leverage is moderate-to-high on our estimate: 4.15x gross and 4.01x net on trailing EBITDA of USD 1,246.9 million built from printed operating income and depreciation and amortization, and interest cover of 4.87x on cash interest. The company reports a covenant leverage ratio of 3.69 against a maximum of 5.00 and targets 3.5x to 4.0x. No EBITDA appears in any source, so the covenant ratio cannot be rebuilt [CP-1 financials table].
4. Operating results are mixed. Nine-month 2026 revenue rose 3.4% and operating income rose 3.7%, but the gross margin fell to 25.2% from 25.9%, funeral gross profit fell 5.5% on 2.7% fewer comparable services, and cemetery gross profit rose 5.3% [CP-1 calculation C12; CP-1A operating model]. On October 28, 2026 the issuer lowered its 2026 adjusted earnings per share outlook to USD 3.94 to 4.04 from USD 4.10 to 4.30 and kept its operating cash flow outlook midpoint at USD 1,085 million [CP-1A timeline].
5. Cash generation is solid but is returned to shareholders. Operating cash flow less capital expenditure was USD 681.4 million for the last twelve months to Q3 2026 and USD 594.2 million in the nine months. Dividends and buybacks were USD 464.4 million in the nine months; in FY2025 they were USD 644.6 million, USD 90.3 million above operating cash flow less capital expenditure, while total debt rose USD 304.5 million [CP-1 calculations C3, CP-1A calculation C3].
6. Visibility is supported by the backlog, which grew to USD 17.72 billion from USD 17.01 billion, but USD 9.15 billion is insurance-funded and not on the balance sheet, and future revenue exceeds trust assets, so cash received can lag revenue recognised [CP-1A operating model].
7. Claims outside debt are modest relative to debt except trust and surety structures: operating leases (present value USD 50.8 million at December 31, 2025), unfunded retirement plans (USD 12.3 million), surety bonds of USD 498.3 million and unquantified unclaimed property audits in about forty states. Consolidated trust balances of USD 6,050.7 million and USD 2,448.4 million are matched by trust assets [CP-1 claims table].
8. Two source conflicts are unresolved: the floating-rate average of 4.1% against 5.68% in the debt note, and the annual maturity table, whose caption and total do not agree. Interest sensitivity and the maturity ladder rest on the debt note and carrying values meanwhile [CP-1A conflicts].

### Strengths and weaknesses

Strengths. Scale and diversification: the network of 1,491 funeral service locations and 506 cemeteries, with a cemetery segment protected by high barriers to entry, spreads local demand risk [Documentary Fact; CP-1A operating model]. Revenue visibility: the preneed backlog of USD 17.72 billion is recognised over time [Documentary Fact]. Liquidity and maturity profile: USD 1,686.4 million of liquidity and a bank facility maturing in November 2030 [Documentary Fact; CP-1]. Cash conversion: operating cash flow after capital expenditure of USD 681.4 million for the last twelve months to Q3 2026, equal to 13.2% of total debt [Analyst Interpretation; CP-1 C3 and C10]. Fixed-rate mix: about 79% of debt is fixed at a weighted average of 4.67%, which limits near-term interest cost swings [Documentary Fact; CP-1].

Weaknesses. Margin pressure: higher selling compensation, advertising and healthcare costs against falling funeral volumes in a high fixed-cost business, with a lowered 2026 outlook [Documentary Fact and Management Language; CP-1A]. Leverage that is moderate-to-high on our estimate at 4.15x gross, with a covenant definition that is not supplied and a management target of 3.5x to 4.0x [Analyst Interpretation; CP-1]. Distributions: dividends and buybacks absorb most free cash flow, so debt reduction is unlikely without a policy change [Analyst Interpretation; CP-1A governance]. Concentration: 32.2% of locations are in California, Texas and Florida, which the issuer itself flags as exposed to natural disasters [Documentary Fact and Analyst Interpretation; CP-1A]. Preneed structure: surety bonds of USD 498.3 million and a USD 258.7 million trust-funding obligation if surety were not renewed at December 31, 2025 are contingent liquidity calls [Documentary Fact; CP-1A]. Missing creditor protections: the credit agreement restrictions, indentures, guarantor detail and ratings are not supplied [Insufficient Information].

### Credit assessment

| Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- |
| Fundamental credit view: stable, cash-generative operator with moderate-to-high leverage, ample liquidity and no refinancing pressure before 2027; margin pressure and shareholder-return policy are the main watch items | Analyst Interpretation | Medium | CP-1 financials, liquidity and debt register; CP-1A operating model and governance rows |
| Business risk: low to moderate, supported by scale, backlog visibility and a defensive demand pattern, offset by funeral volume decline and state concentration | Analyst Interpretation | Medium | CP-1A company and operating model |
| Financial risk: moderate to high on our estimated 4.15x gross leverage; liquidity strong | Analyst Interpretation | Medium | CP-1 financials table |
| Creditor protection and ranking | Insufficient Information | Insufficient Information | Credit agreement, indentures, guarantor and security detail and ratings are not supplied; this limits legal capacity, ranking and covenant conclusions |

Confidence is below High because the upstream readiness judgments for this module are READY_WITH_LIMITATIONS and the upstream gaps ledger lists a High-severity covenant-definition gap.

### Thesis

SERVICE CORP INTERNATIONAL is a defensive, scale-driven deathcare operator whose backlog, cash flow and long-dated bank facility support its moderate-to-high leverage, provided cemetery growth and pricing keep offsetting funeral volume loss and shareholder returns do not outrun cash flow.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity | Basis |
| --- | --- | --- | --- | --- |
| Margin compression | Selling compensation, advertising and healthcare costs rise ahead of preneed revenue recognition; fixed costs amplify volume loss | Coverage and leverage ratios could weaken even with stable revenue; the lowered outlook shows it has begun | Material | CP-1 C12; CP-1A operating model |
| Covenant and definition uncertainty | The only financial covenant is a maximum leverage ratio on an unsupplied definition; our estimate is above the reported figure | Headroom cannot be verified; a definition that is stricter than reported could change the picture | Material | CP-1 financials; CP-0 gap |
| Distribution policy | Dividends and buybacks sized to cash flow, partly debt-funded in FY2025; restrictions not supplied | Leverage can drift at the upper end of the stated range without a contractual limit evident | Material | CP-1A governance; CP-1 C3 |
| Regional concentration | A third of locations in three disaster-prone states | One event can disrupt cash flow and test insurance; revenue by state not supplied | Material | CP-1A concentration row |
| Preneed trust and surety calls | Surety bonds and trust funding rules; unquantified unclaimed property audits | A loss of surety capacity would require cash funding of trusts | Minor | CP-1A regulatory row; CP-1 claims table |
| Refinancing of 2027 maturities | USD 136.9 million due April 2027 and USD 550.0 million due December 2027 against liquidity of USD 1,686.4 million | Low near-term risk; any refinancing of the 4.625% notes would be at then-current rates, which the sources do not give | Minor | CP-1 debt register |
| Floating-rate exposure | About 21% of debt floats on the term loan, revolver and headquarters facility; a rate average in the 10-Q conflicts with the debt note | Interest cost sensitivity is unsettled; modest relative to cash flow | Minor | CP-1A conflicts |

### Debt, liquidity and covenant summary

| Item | Figure | Category | Basis |
| --- | --- | --- | --- |
| Total debt, carrying value, September 30, 2026 | USD 5,172.9 million (USD 5,205.4 million before issuance costs) | Documentary Fact | CP-1 debt register |
| Cash | USD 172.7 million, part of it encumbered | Documentary Fact | CP-1 liquidity table |
| Undrawn bank credit facility capacity | USD 1,513.7 million (commitment USD 1,750.0 million, drawn USD 235.0 million, letters of credit USD 1.3 million) | Documentary Fact | CP-1 liquidity table |
| Liquidity | USD 1,686.4 million | Analyst Interpretation | CP-1 C11 |
| Current maturities | USD 195.1 million | Documentary Fact | CP-1 maturities chart row |
| Fixed-rate share and rate | About 79% fixed; weighted average rate 4.88% on total debt | Documentary Fact | CP-1 debt register |
| Reported covenant leverage ratio | 3.69 against 5.00 maximum | Management Language (issuer-reported) | CP-1 liquidity and covenant table |
| Analyst gross and net leverage | 4.15x and 4.01x | Analyst Interpretation | CP-1 C7 |
| Analyst interest cover | 4.87x on cash interest; 4.84x on interest expense | Analyst Interpretation | CP-1 C8 |
| Fair value of debt instruments | USD 4,833.2 million against carrying value USD 5,172.9 million | Documentary Fact | CP-1 debt register |

### Latest quarter and after

Q3 2026 revenue was USD 1,107.3 million and operating income USD 252.9 million, including an USD 11.2 million divestiture gain; excluding that line operating income rose 6.6%. The revolver was reduced by USD 130.0 million in the quarter, the company repurchased 658,460 shares and paid a quarterly dividend of USD 0.36 per share. After quarter end it repurchased 232,968 shares for USD 18.2 million and lowered its 2026 earnings outlook on October 28, 2026 [CP-1 latest quarter; CP-1A timeline]. Nothing dated after October 29, 2026 is supplied.

## Calculations

Inputs are the upstream handoff figures cited. Results are rounded as shown.

- **C1, coverage of near-term maturities.** Liquidity USD 1,686.4 million (CP-1 C11) / current maturities USD 195.06 million (195,060 thousand) = 8.6x. Liquidity / the April 2027 and December 2027 notes, 136.924 + 550.000 = USD 686.924 million = 2.5x.
- **C2, notes at fair value.** Fair value of the six senior note series at September 30, 2026 (thousands): 138,043 + 544,087 + 731,062 + 767,049 + 725,776 + 770,896 = 3,676,913; face value 3,886,924 (CP-1 debt register); 3,676,913 / 3,886,924 = 94.6%. The fair values are Level 2 market-price estimates (Q3 10-Q page:19, page:20).
- **C3, leverage illustration (analyst definitions, not the covenant).** Carrying total debt 5,172,948 thousand / 5.00 = 1,034,590 thousand of EBITDA; against analyst LTM EBITDA of 1,246,945 thousand (CP-1 C1) this is a fall of 17.0%. The reported covenant ratio is on an unsupplied definition, so this is not covenant headroom.
- **C4, floating-rate sensitivity (inference).** Treating the term loan, revolver and headquarters facility as the floating-rate debt, 735,938 + 235,000 + 110,852 = 1,081,790 thousand (CP-1 C11); a 100 basis point rise adds 1,081,790 x 1% = 10,818 thousand, USD 10.8 million, on an annual basis, or 4.2% of LTM cash interest of USD 256.3 million (CP-1 C4). The 10-K shows a 10% proportional rise adding USD 5.9 million at December 31, 2025 (10-K page:66). The instruments' floating status is inferred, not listed in the sources.
- **C5, upstream figures reused.** Gross leverage 4.15x, net leverage 4.01x, cover 4.87x, operating cash flow less capex USD 681.4 million and 13.2% of debt, distributions and shortfalls, and mix and concentration percentages are taken from CP-1 (C7, C8, C3, C10) and CP-1A (C1 to C3) and are not recomputed.

## Gaps

| Gap | Why it matters | Severity | Action |
| --- | --- | --- | --- |
| Covenant ratio definition and credit agreement terms (payment restrictions, baskets, guarantors) not supplied; no EBITDA in any source | Headroom, legal capacity for distributions and ranking cannot be verified | High | Supply the credit agreement and covenant compliance definition |
| Indentures, security and guarantor detail for the senior notes not supplied | Ranking and structural position of USD 3,886.9 million of notes unassessed | High | Supply the indentures and guarantor schedule |
| Ratings and market prices other than fair values not supplied | No external credit opinion to compare against | Medium | Supply rating reports or keep Not supplied |
| Ownership percentages, board and related-party detail (proxy statement not supplied) | Governance and control rights cannot be assessed | Medium | Supply the 2026 proxy statement |
| Floating-rate and maturity-table conflicts | Interest sensitivity and the maturity ladder are on a stated basis only | Medium | Confirm in the filed HTML or with the issuer |
| Revenue and profit by state; customer and supplier concentration | Regional concentration risk unquantified | Medium | Request disclosure |
| Unclaimed property audits unquantified; part of cash encumbered | Contingent claim and liquidity are not fully measured | Medium | Carry as limits; request amounts |
| Events from October 30, 2026 to the cutoff | New financing or ratings could change the view | Medium | Supply later filings or confirm none |

## Next module

- CP-5: check every figure here against its upstream table; the key attributed items are the reported covenant ratio, the outlook change and the market share claim. Keep the estimated leverage labelled as an analyst estimate on the printed operating income and depreciation and amortization lines.
