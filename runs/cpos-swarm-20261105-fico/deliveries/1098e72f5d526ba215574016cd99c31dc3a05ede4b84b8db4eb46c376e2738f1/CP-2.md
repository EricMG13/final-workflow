# CP-2 - Fundamental credit synthesis: FAIR ISAAC CORP (fico)

## Request

- Issuer: FAIR ISAAC CORP (Fair Isaac Corporation, NYSE "FICO", issuer id `fico`), as of 2026-11-05, information cutoff 2026-11-05.
- Scope: the fundamental credit view a committee reads first, synthesised from the settled upstream registers only: business risk from the business and transaction context, financial risk and liquidity from the financial base, and the gaps that limit both. Creditor perspective.
- Prohibited and not done: no peer ranking, no instrument recommendation, no recovery conclusion. Recovery appears only as a mechanic where relevant. No rating is assigned.
- Evidence rule: upstream only. This module re-read no source text and quotes nothing. Every row names its basis: rows of the business context register (ids F1 to F21, in Basis columns only) or CP-1 figures. Figures are CP-1 figures as written there.
- Periods and currency: USD; fiscal year ends September 30; fiscal Q3 2026 is the quarter ended June 30, 2026; LTM Q3 FY2026 is the twelve months to June 30, 2026.
- Inherited limitations (carried, not restated as findings): from CP-0 and CP-1, no company-defined EBITDA or covenant ratio, no executed financing documents, undrawn revolver derived without letters of credit, and no evidence dated after July 29, 2026. From the business context, the proxy statement is not supplied and the readiness judgment of this module is READY_WITH_LIMITATIONS, so confidence is below High.

## Sources

| Source (exact name) | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-09-30_fico-20250930.htm.jsonl | 2cd0fc2b16386652e87f31c986fda43ca1da2a923ef1840b57f765a69322682e | Reached through the handoffs; not re-read |
| 10-Q_2025-12-31_fico-20251231.htm.jsonl | 905bfc6e05d39d56e0eed3225e1079b7eb97528806ef0d9d2d8efa0e76893510 | Reached through the handoffs; not re-read |
| 10-Q_2026-03-31_fico-20260331.htm.jsonl | 1d56011f469dd7f9f01c0afabb2cc5e52bf600c9b61e1e02a22c20a1382a76cb | Reached through the handoffs; not re-read |
| 10-Q_2026-06-30_fico-20260630.htm.jsonl | 9928c89c8cd74e2a4ae5180bf504e58edee7d7a0cfbf531e71dc30f830e9f9a7 | Reached through the handoffs; not re-read |
| EX-99.1_2026-01-28_exhibit991erq12026.htm.jsonl | 7ff326f8e766ed76e0e346c09be22d1a6689de853a63261725535c212fd1ea11 | Reached through the handoffs; not re-read |
| EX-99.1_2026-04-28_exhibit991erq22026.htm.jsonl | 98fcf8141dae7e420bccc2579f8ef67af179818384ed4fb3d51d12d1c6831d98 | Reached through the handoffs; not re-read |
| EX-99.1_2026-07-29_exhibit991erq32026.htm.jsonl | 4bcf15097cd5d352a02b7a02cc65369e0e3cdadccda74b9b84b0c06bd098be52 | Reached through the handoffs; not re-read |
| context | 67fd10ada0c60e1a58280c6938025b16a97aebcc1d2e25ac2914a3e17b05c7a0 | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | bf1dc2c14187a6208c7ecc4cc4dcd1ace42a402c8c8aa295e5e74d0134c7d3d4 | Readiness and inherited source limitations |
| CP-1 | 1a096021c0f3adbc74479c24fc532da87239b821a5817bc5b560d7c9fa7efb1f | Financial base: debt, EBITDA construction, leverage, cover, liquidity, maturities |
| CP-1A | c0363d0389df16dda0832d378a73aa091a19e25a0b568900229c1c8a1dbf0f0d | Business and transaction context: concentration, pricing, governance, capital allocation, fact rows F1 to F21 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| FICO has strong, cash-generative earnings, but debt-funded buybacks lifted analyst leverage to 4.46x against a covenant maximum of 4.5x that steps down. The credit depends on pricing and on shareholder-return choices. | Medium | The covenant definition and executed financing documents are not supplied, so headroom cannot be measured. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt rose from US$3,055.7m to US$5,582.4m in nine months because buybacks exceeded free cash flow. | Leverage is a policy choice and can rise again. | High |
| Analyst EBITDA gives a cushion of only 0.95% below the 4.5x covenant maximum at June 30, 2026. | Little room before the step down to 4.0x on December 31, 2026. | Medium |
| Annualised contractual interest is US$316.5m against last twelve months cash interest of US$164.9m. | Cover falls to 3.96x on the run-rate from 7.60x as reported. | Medium |
| Bureau concentration and mortgage pricing drive earnings. | A pricing or policy change would cut EBITDA and leverage headroom together. | Medium |
| Free cash flow of US$960.9m for the last twelve months exceeds the US$300.0m of term loan amortisation due within twelve months. | Scheduled debt service is covered if earnings hold. | Medium |

### Credit view

FICO's business risk is strong on earnings quality but narrow on sources: a per-score fee model with very high segment margins, recurring Software revenue with net retention above 100%, light capital spending and consistent free cash flow. Its financial risk has moved sharply in fiscal 2026. Total debt rose from US$3,055.7m to US$5,582.4m while cash repurchases of US$3,046.0m for nine months far exceeded free cash flow of US$750.0m, and analyst total debt to EBITDA rose from 3.25x at FY2025 to 4.46x at June 30, 2026, which is 4.26x net. The stated covenant maximum is 4.5x until December 30, 2026, then 4.0x, then 3.5x, and on the analyst measure the cushion below 4.5x is thin; on a sensitivity that adds back share-based compensation the ratio is 3.91x. The covenant definition is not supplied, so headroom is Not calculable. Interest on the June 2026 debt is only partly in reported cash interest, so run-rate cover is about 3.96x against 7.60x reported. Liquidity is adequate for the near term but not generous: cash of US$248.4m plus a derived undrawn revolver of US$290.0m, against US$300.0m of term loan amortisation due within twelve months, which free cash flow comfortably covers. The next refinancing step is large: US$1,987.5m falls due in FY2028, when the term loan balance and the 2019 and 2021 notes mature. Because the debt is unsecured and no creditor-adverse action is documented, the creditor relies on covenants, cash generation and the board's financial policy, not on collateral or a sponsor. Overall the fundamental credit view is a high-quality earnings stream carrying a materially higher and still discretionary debt load; confidence is medium because covenant definitions, ownership detail and everything after July 29, 2026 are Not supplied.

### Key findings

The most important finding is that leverage is now set by shareholder-return policy rather than by operations. CP-1 shows total debt up from US$3,055.7m to US$5,582.4m over nine months and nine-month cash repurchases of US$3,046.0m against free cash flow of US$750.0m; the business context shows the term loan proceeds were used to fund an accelerated share repurchase and that a $2.0 billion repurchase authorisation is in place. The mechanism is direct: each repurchase round is financed by borrowing, so analyst total debt to EBITDA of 4.46x can rise or fall by board decision alone. The implication is that the creditor's leverage tolerance depends on a choice nobody has committed to constrain, other than the financial covenant.

The second finding is the covenant path. The stated maximum consolidated leverage ratio is 4.5x until December 30, 2026, 4.0x from December 31, 2026 and 3.5x from December 31, 2027. On the analyst measure of operating income plus depreciation and amortisation, total debt to EBITDA is 4.46x, which leaves a cushion of 0.95% of EBITDA below 4.5x (Calculations); on the sensitivity with share-based compensation added back it is 3.91x. The covenant definition is not supplied, so neither is the covenant ratio, and the compliance statement in the filings is the only evidence of headroom. The step down to 4.0x on December 31, 2026 requires EBITDA growth, debt reduction or a favourable definition; the quarterly term loan instalments and free cash flow provide the repayment capacity.

The third finding is interest burden. Cash interest paid in the last twelve months is US$164.9m but annualised contractual interest on June 30, 2026 balances is US$316.5m, because the term loan was drawn on June 5, 2026 and the 2026 notes in March 2026. Cover is 7.60x as reported and 3.96x on the run-rate. About US$2,210.0m of borrowings float over SOFR, so base rates feed straight into the burden.

The fourth finding is revenue concentration. Three consumer reporting agencies produced 63% of revenue in the June 2026 quarter, and Scores growth was primarily attributed to a higher mortgage origination scores unit price. The mechanism is that a per-score fee through three intermediaries, a regulated mortgage channel and a single price lever determine most of earnings and almost all of the incremental margin, given a Scores margin of 91%. A pricing, volume or policy change therefore hits EBITDA, interest cover and covenant headroom together.

The fifth finding is liquidity and maturities. Cash is US$248.4m, the derived undrawn revolver is US$290.0m before letters of credit, and US$300.0m of term loan amortisation falls due within twelve months, against last twelve months free cash flow of US$960.9m. The maturity profile is back-ended into FY2028, when US$1,987.5m falls due. The implication is that near-term liquidity is sufficient but refinancing will need market access at higher coupons, since the 2026 notes carry 6.25% against 5.25% on the repaid notes.

### Strengths and weaknesses

Strengths. First, earnings power: segment margins are very high and Scores generates a 91% operating margin, so operating income of US$1,236.3m for the last twelve months converts into analyst EBITDA of US$1,252.4m on light capital spending; the mechanism is low incremental cost, which supports debt service. Second, cash conversion: free cash flow of US$960.9m for the last twelve months and US$750.0m for nine months, supported by billing in advance, means scheduled amortisation is covered by internal cash. Third, recurring visibility in Software: annual recurring revenue of US$815.8m and net retention of 109%, with platform retention well above 100%, supports a base of contracted revenue, though it is the smaller segment. Fourth, discretionary use of cash: because the leverage increase came from repurchases, not from a structural commitment, the board can slow repurchases to reduce debt; the revolver extends to 2030 and the term loan amortises. Fifth, simple structure: the debt is unsecured, with no sponsor, and no priming, drop-down or non-pro-rata exchange is documented, though the absence of such terms in executed documents is not established.

Weaknesses. First, leverage and covenant path: 4.46x on the analyst measure against a 4.5x maximum that steps to 4.0x and 3.5x; the mechanism is shrinking permitted leverage unless EBITDA grows or debt is repaid. Second, financial policy: debt-funded distributions of US$3,046.0m for nine months against free cash flow of US$750.0m, with a stockholders' deficit that carries no equity cushion. Third, concentration: bureaus at 63% of revenue, financial services at 92% and the Americas at 87% of FY2025 revenue, and mortgage-policy exposure. Fourth, interest burden: run-rate interest of US$316.5m is nearly double last twelve months cash interest, with floating-rate exposure. Fifth, disclosure limits: no company EBITDA, no covenant ratio, no executed documents, no proxy statement, no data after July 29, 2026; these restrict monitoring more than they signal risk, and missing evidence is not treated as adverse.

### Credit assessment

| Dimension | Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- | --- |
| Business risk | Strong earnings quality, narrow sources: three bureaus, one price lever, mortgage-linked | Analyst Interpretation | Medium | F1, F3, F4, F16, the operating model rows on mortgage pricing and policy, and CP-1 free cash flow |
| Financial risk | Elevated and rising: total debt to EBITDA 4.46x, cover 7.60x reported and 3.96x run-rate | Documentary Fact for the figures; Analyst Interpretation for the reading | Medium | CP-1 leverage and cover figures |
| Liquidity | Adequate near term, thin surplus: cash US$248.4m, derived undrawn revolver US$290.0m, US$300.0m amortisation within twelve months | Documentary Fact and derived figure | Medium | CP-1 liquidity and maturity figures |
| Governance and financial policy | Shareholder-return led; debt-funded repurchases; no creditor-adverse action documented | Analyst Interpretation | Medium | F11, F12, F13, F19 |
| Overall fundamental credit view | A high-quality earnings stream with a materially higher, discretionary debt load; headroom to the covenant is thin on the analyst measure | Analyst Interpretation | Medium | All of the above |

Thesis (one sentence): FICO's very profitable, cash-generative but concentrated Scores franchise supports its debt, while debt-funded buybacks and a stepping-down leverage covenant make the credit depend on pricing power and on the board's financial policy.

### Strengths and weaknesses register

| Item | Type | Text | Category | Basis |
| --- | --- | --- | --- | --- |
| S1 | Strength | High margins and cash conversion: free cash flow US$960.9m for the last twelve months | Documentary Fact | CP-1 free cash flow; operating model rows on Scores margin |
| S2 | Strength | Recurring Software visibility: annual recurring revenue and net retention above 100% overall | Documentary Fact | Business context operating model rows |
| S3 | Strength | Discretionary buybacks allow deleveraging by decision; revolver runs to 2030 | Analyst Interpretation | F11, F12; CP-1 maturities |
| S4 | Strength | Unsecured structure, no sponsor and no documented creditor-adverse action | Insufficient Information on executed terms | F8, F20 |
| W1 | Weakness | Leverage 4.46x against 4.5x maximum stepping to 4.0x and 3.5x | Documentary Fact for the figures | CP-1 leverage; F19 |
| W2 | Weakness | Debt-funded distributions exceeding free cash flow; stockholders' deficit | Documentary Fact | CP-1 financial base; F13 |
| W3 | Weakness | Bureau, sector, geographic and mortgage-policy concentration | Documentary Fact | F3, F4 and the operating model rows on mortgage pricing and policy |
| W4 | Weakness | Run-rate interest US$316.5m against LTM cash interest US$164.9m; floating-rate borrowings | Documentary Fact for the figures | CP-1 interest figures |
| W5 | Weakness | Missing covenant definition, executed documents, proxy and later events | Insufficient Information | F8, F10, F21 |

### Key credit risks

| Risk | Mechanic | Credit implication | Severity | Basis |
| --- | --- | --- | --- | --- |
| Covenant step-down against rising leverage | Maximum falls to 4.0x on December 31, 2026 and 3.5x on December 31, 2027 while analyst leverage is 4.46x | Possible covenant pressure or forced slowing of buybacks; amendment cost; headroom Not calculable | Material | CP-1 leverage; F19 |
| Debt-funded shareholder returns | Repurchases financed by term loan and notes; authorisation of $2.0 billion | Leverage tolerance set by the board; renewed borrowing could reverse deleveraging | Material | F11, F12, F13; CP-1 financial base |
| Revenue concentration and pricing dependence | Three bureaus at 63% of the June 2026 quarter; Scores growth attributed to unit price | Earnings and covenant headroom fall together if price or policy changes | Material | F3, F4 and the operating model rows on mortgage pricing and policy |
| Interest burden step-up and floating rate | Run-rate interest US$316.5m; term loan and revolver float over SOFR | Cover falls to 3.96x on run-rate; rates feed through | Material | CP-1 interest figures |
| FY2028 refinancing | US$1,987.5m falls due in FY2028 | Needs market access at higher coupons than the repaid notes | Material | CP-1 maturities chart |
| Antitrust litigation | Class action over FICO Score distribution continues; no amount stated | Contingent claim not quantified | Minor | F16, F17 |
| Information gaps | No covenant definition, proxy, executed documents or post-July 2026 evidence | Restricts monitoring; not an adverse conclusion | Minor | F8, F10, F21 |

## Calculations

All inputs are CP-1 figures in US$ thousands as written there. These are new calculations in this module.

- EBITDA needed at the 4.5x covenant maximum on the analyst construction: 5,582,389 / 4.5 = 1,240,531. LTM Q3 FY2026 analyst EBITDA is 1,252,442. Difference 1,252,442 - 1,240,531 = 11,911, which is 0.95% of 1,252,442. This is the cushion under the analyst measure, not a covenant headroom.
- EBITDA needed at 4.0x at the same debt: 5,582,389 / 4.0 = 1,395,597; shortfall against 1,252,442 is 143,155. On the sensitivity with share-based compensation added back, EBITDA is 1,426,731, which exceeds 1,395,597, so the ratio is 3.91x (5,582,389 / 1,426,731). Neither is the covenant calculation; the definition is not supplied.
- Free cash flow against amortisation: LTM free cash flow 960,878 exceeds the 300,000 term loan principal due within twelve months (CP-1; the loan schedule is derived from 10-Q summary terms).
- Floating-rate borrowings: 710,000 + 1,500,000 = 2,210,000 (revolver plus term loan, CP-1 debt table).
- No other new figures. All other values are CP-1 figures as written: total debt 3,055,691 and 5,582,389; cash repurchases 3,045,992 and free cash flow 750,034 for nine months; cash interest 164,872; annualised interest 316,510; cover 7.60x and 3.96x; leverage 3.25x, 4.46x, 4.26x and 3.91x.

## Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Credit agreement, June 5, 2026 amendment and covenant definitions not supplied; reported leverage ratio not printed | Headroom to the maximum leverage ratio cannot be measured | Financial risk, covenant risk | Material | Obtain the executed documents; until then headroom is Not calculable |
| Indentures, guarantor structure and repurchase agreement terms not supplied | Distribution capacity and any guarantees cannot be verified | Governance, creditor control | Material | Obtain; guarantors Not supplied |
| 2026 Proxy Statement not supplied | Ownership, board and related-party dealings unknown | Governance, willingness | Medium | Obtain the proxy |
| Nothing after July 29, 2026: September 30, 2026 instalment, ASR settlement, fiscal Q4 and FY2026 results | Leverage and liquidity at the fiscal year end are unknown | All | Material | Add later filings |
| Letters of credit usage not disclosed | Undrawn revolver of US$290.0m is an upper bound | Liquidity | Medium | Obtain disclosure |
| FHFA policy status after July 2025 not updated in the 10-Qs | Mortgage score preference could change | Business risk | Medium | Monitor |
| Antitrust case outcome and exposure unknown | Contingent claim not quantified | Contingent claims | Minor | Monitor |
| Usage-based ACV share differs between filings (logged, not reconciled) | Software visibility slightly uncertain | Business risk | Minor | Note only |

## Next module

Run CP-5 next on this module with CP-1 and CP-1A. Review in particular: the cushion figure under the 4.5x covenant maximum, which is an analyst construction; the run-rate interest and cover figures; the derived undrawn revolver and maturity schedule; and the statements about creditor-adverse actions, which rest on the filings read and not on executed documents.
