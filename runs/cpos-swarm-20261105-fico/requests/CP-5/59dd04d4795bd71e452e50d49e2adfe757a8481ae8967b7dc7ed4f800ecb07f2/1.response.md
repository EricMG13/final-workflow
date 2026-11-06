# CP-5 - Evidence trace validator: FAIR ISAAC CORP (fico)

## Request

- Issuer: FAIR ISAAC CORP (Fair Isaac Corporation, NYSE "FICO", issuer id `fico`), as of 2026-11-05, information cutoff 2026-11-05.
- Scope: independent review of the run's four analytical handoffs (readiness, financial base, business and transaction context, credit synthesis). Question: does each material claim rest on the evidence it names, and do the modules tell one consistent story? Then grade research integrity and say whether committee use is permitted, restricted or blocked.
- Method: the reviewer re-opened the cited pages of the pinned sources, searched the sources for contrary evidence, recomputed every derived figure from cited inputs, and compared figures across the four handoffs. This is a host-session review; no provider was called and no earlier handoff was edited.
- Periods and currency: USD; fiscal year ends September 30; fiscal Q3 2026 is the quarter ended June 30, 2026; LTM Q3 FY2026 is the twelve months to June 30, 2026.
- Out of scope: no new financial analysis, peer ranking, instrument recommendation or recovery conclusion.

## Sources

| Source (exact name) | sha256 | Use in this review |
| --- | --- | --- |
| 10-K_2025-09-30_fico-20250930.htm.jsonl | 2cd0fc2b16386652e87f31c986fda43ca1da2a923ef1840b57f765a69322682e | Locators and figures re-opened |
| 10-Q_2025-12-31_fico-20251231.htm.jsonl | 905bfc6e05d39d56e0eed3225e1079b7eb97528806ef0d9d2d8efa0e76893510 | Q1 FY2026 figures re-opened |
| 10-Q_2026-03-31_fico-20260331.htm.jsonl | 1d56011f469dd7f9f01c0afabb2cc5e52bf600c9b61e1e02a22c20a1382a76cb | Q2 FY2026 figures re-opened |
| 10-Q_2026-06-30_fico-20260630.htm.jsonl | 9928c89c8cd74e2a4ae5180bf504e58edee7d7a0cfbf531e71dc30f830e9f9a7 | Controlling source; locators and figures re-opened |
| EX-99.1_2026-01-28_exhibit991erq12026.htm.jsonl | 7ff326f8e766ed76e0e346c09be22d1a6689de853a63261725535c212fd1ea11 | Searched; not relied on for figures |
| EX-99.1_2026-04-28_exhibit991erq22026.htm.jsonl | 98fcf8141dae7e420bccc2579f8ef67af179818384ed4fb3d51d12d1c6831d98 | Searched; guidance history only |
| EX-99.1_2026-07-29_exhibit991erq32026.htm.jsonl | 4bcf15097cd5d352a02b7a02cc65369e0e3cdadccda74b9b84b0c06bd098be52 | Cross-check of quarter cash flow, free cash flow and statements |
| context | 67fd10ada0c60e1a58280c6938025b16a97aebcc1d2e25ac2914a3e17b05c7a0 | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Status found |
| --- | --- | --- |
| CP-0 | bf1dc2c14187a6208c7ecc4cc4dcd1ace42a402c8c8aa295e5e74d0134c7d3d4 | Accepted; readiness with limitations |
| CP-1 | 1a096021c0f3adbc74479c24fc532da87239b821a5817bc5b560d7c9fa7efb1f | Accepted; financial base |
| CP-1A | c0363d0389df16dda0832d378a73aa091a19e25a0b568900229c1c8a1dbf0f0d | Accepted; business and transaction context |
| CP-2 | 7e3b9a436be389d8c7e85fcdedf6bfb068c349171b11a220c93823f1079692fd | Accepted; credit synthesis |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial figures and business facts trace cleanly to the filings and recompute. Use is restricted because covenant headroom, guarantors and ownership rest on summary text and absent documents. | Medium | Credit agreement, indentures and proxy are not supplied; one margin statement needs a period label. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every cited quotation was found on its cited page, and every derived figure was recomputed from cited inputs with no difference. | The debt, liquidity and leverage figures can be relied on as stated. | High |
| The 0.95% cushion below the 4.5x covenant maximum is an analyst construction, not a covenant calculation. | It must not be read as covenant headroom. | High |
| The Scores operating margin of 91% in the credit synthesis is the June 2026 quarter figure; the FY2025 figure was 88%. | The earnings strength is slightly overstated if read as annual. | Medium |
| The statement that no creditor-adverse action is documented rests on filings read, not on executed documents. | Creditor protections cannot be confirmed. | Medium |
| The modules agree on every shared figure; the differences are rounding of thousands into millions. | The run tells one consistent story. | High |

### Evidence trace view

The trace holds. All 29 quotations in the financial base and business context handoffs were found, and each sits on the page it cites. In the readiness handoff every quotation of source text was found; its three other quoted strings are search terms or paraphrases, not source quotations. Every non-derived figure in those handoffs appears in the pinned sources, and every derived figure recomputes from its cited inputs. The four handoffs agree on every shared figure; differences are only the presentation of US$ thousands as US$m. Two qualifications matter for committee use. First, the leverage cushion, the interest run-rate, the undrawn revolver and the maturity schedule are analyst constructions: each is labelled as derived upstream, and each rests on inputs the filings summarise rather than on executed documents. Second, statements about the absence of creditor-adverse terms and about covenant headroom are absence-of-evidence claims and are bounded by the missing credit agreement, indentures and proxy. One wording defect was found in the credit synthesis (a quarter margin stated without its period), recorded below and corrected here. The run supports restricted committee use: permitted for the business description, reported financials, debt structure, liquidity and concentration facts; not permitted for covenant headroom, guarantor or security conclusions, or ownership and related-party conclusions.

### Verification performed

| Check | Result |
| --- | --- |
| Quotations re-found in the pinned sources and on the cited page (financial base, business context, credit synthesis) | All found; none misplaced |
| Quotations of source text in the readiness handoff found in the sources | All found; three quoted strings there are search terms, not source text |
| Reported figures in the handoffs present in the sources | All present; the numbers not found are derived figures |
| Derived figures recomputed from cited inputs | All reproduced (see Calculations) |
| Cross-module figure identity | No mismatch; unit presentation differs only |
| Subsequent events kept out of period figures | Yes: the expected ASR settlement and the September 30, 2026 instalment are labelled forward or Not supplied |
| Blocked or stale upstream inputs | None blocked; the latest evidence is dated July 29, 2026 |
| Search for contrary evidence | See Strongest contrary evidence |

### Claim support register

| Claim | Module | Verified against | Rating | Note |
| --- | --- | --- | --- | --- |
| Total debt rose from US$3,055.7m at September 30, 2025 to US$5,582.4m at June 30, 2026 | CP-1, CP-1A, CP-2 | 10-Q page:10 (debt table, "Total debt $ 5,582,389 $ 3,055,691") | Supported | Carrying value after issuance costs; face value is US$5,610.0m (10-Q page:10 to page:12) |
| Cash repurchases of US$3,046.0m in nine months against free cash flow of US$750.0m | CP-1, CP-1A, CP-2 | 10-Q page:4 (financing) and release page:5 (free cash flow) | Supported | The equity statement shows a different repurchase figure; see Conflicts |
| Term loan proceeds were used to fund an accelerated share repurchase | CP-1, CP-1A, CP-2 | 10-Q page:22 | Supported | |
| Covenant maximum 4.5x until December 30, 2026, 4.0x to December 30, 2027, 3.5x after | CP-1, CP-2 | 10-Q page:11 and page:37 | Supported | Step up to 4.0x after certain permitted acquisitions applies |
| Analyst total debt to EBITDA 4.46x; net 4.26x | CP-1, CP-2 | Recomputed | Supported as a calculation | EBITDA is operating income plus cash flow D&A; not a company or covenant measure |
| Cushion of 0.95% of EBITDA below the 4.5x maximum | CP-2 | Recomputed | Supported with qualification | Analyst construction; covenant definition not supplied; headroom Not calculable |
| Annualised contractual interest US$316.5m; cover 3.96x | CP-1, CP-2 | Recomputed from balances and rates (10-Q page:10 to page:12) | Supported with qualification | Floating rates and excluded fees; weighted-average and stated rates only |
| Derived undrawn revolver US$290.0m | CP-1, CP-1A, CP-2 | US$1.0bn commitment less US$710.0m drawn (10-Q page:10, page:11) | Supported with qualification | Letters of credit are not disclosed; stated as an upper bound |
| US$300.0m term loan amortisation within twelve months | CP-1, CP-2 | 10-Q page:33 and current maturities on page:2 | Supported | |
| US$1,987.5m maturing in FY2028 | CP-1, CP-2 | Derived from term loan terms (10-Q page:11) and notes (10-Q page:12) | Supported with qualification | Final balloon inferred from stated instalments and maturity; credit agreement not supplied |
| Bureaus produced 63% of revenue in the June 2026 quarter, 54% a year earlier | CP-1A, CP-2 | 10-Q page:15 | Supported | |
| Scores growth primarily attributed to a higher mortgage origination scores unit price | CP-1, CP-1A, CP-2 | 10-Q page:26 | Supported | Quarter statement; the nine-month text adds volume |
| Scores operating margin of 91% | CP-1A, CP-2 | 10-Q page:32 | Partly supported | 91% is the June 2026 quarter; FY2025 was 88% (10-K page:71). CP-2 states it without a period |
| Platform software retention above 100%; ARR US$815.8m; total retention 109% | CP-1A, CP-2 | 10-Q page:22, page:25 | Supported | |
| No creditor-adverse action documented | CP-1A, CP-2 | Filings read; no priming, drop-down or exchange in the 10-Qs read | Partly supported | Absence claim; executed documents not supplied |
| Debt is unsecured | CP-1, CP-2 | 10-Q page:11 (revolver and term loan "unsecured"); notes described as typical of unsecured obligations (page:12) | Supported for the bank debt; note security rests on management description | Indentures not supplied |
| Antitrust class action continues; no amount or accrual stated | CP-1, CP-1A, CP-2 | 10-Q page:43; page:20 | Supported | |
| Floating-rate borrowings US$2,210.0m | CP-1, CP-2 | 10-Q page:10, page:41 | Supported | Revolver plus term loan |
| Free cash flow US$960.9m for the last twelve months | CP-2 (CP-1: 960,878 thousand) | Recomputed | Supported | Operating cash flow less property and capitalised software |

### Cross-module figure identity

| Figure | CP-1 | CP-1A | CP-2 | Match |
| --- | --- | --- | --- | --- |
| Total debt at June 30, 2026 | US$5,582,389 thousand; US$5,582.4m | US$5,582.4m | US$5,582.4m | Yes |
| Total debt at September 30, 2025 | US$3,055,691 thousand; US$3,055.7m | US$3,055.7m | US$3,055.7m | Yes |
| Analyst total debt to EBITDA, LTM Q3 FY2026 | 4.46x | 4.46x | 4.46x | Yes |
| Net debt to EBITDA | 4.26x | Not stated | 4.26x | Yes |
| Cash | US$248.4m | US$248.4m | US$248.4m | Yes |
| Derived undrawn revolver | US$290.0m | US$290.0m | US$290.0m | Yes |
| Nine-month free cash flow | US$750.0m | US$750.0m | US$750.0m | Yes |
| Nine-month cash repurchases | US$3,046.0m | US$3,046.0m | US$3,046.0m | Yes |
| LTM cash interest | US$164.9m | Not stated | US$164.9m | Yes |
| Annualised contractual interest | US$316.5m | Not stated | US$316.5m | Yes |
| EBITDA to cash interest, reported and run-rate | 7.60x and 3.96x | Not stated | 7.60x and 3.96x | Yes |
| Total debt to EBITDA with share-based compensation added back | 3.91x | Not stated | 3.91x | Yes |
| FY2028 maturities | US$1,987.5m | Not stated | US$1,987.5m | Yes |
| Bureau share of June 2026 quarter revenue | 63% | 63% | 63% | Yes |
| LTM free cash flow and operating income | 960,878 and 1,236,298 thousand | Not stated | US$960.9m and US$1,236.3m | Yes, rounded to US$m |

### Conflicts and contradictions

- Repurchase figures with different roles: the cash flow statement shows repurchases of US$3,045,992 thousand for nine months (10-Q page:4) and the stockholders' deficit statement shows US$3,052,893 thousand (10-Q page:3). The roles differ: the equity statement is on an accrual basis including excise tax and unsettled repurchases, and unsettled repurchases rose from 18,416 at September 30, 2025 to 25,318 at June 30, 2026 (10-K page:91; 10-Q page:5), a rise of 6,902 against a gap of 6,901. The handoffs use the cash figure consistently; no mismatch. Neither figure was chosen over the other by the reviewer.
- Usage-based share of ACV bookings: logged in the business context as 20% in the 10-Q (page:23) and 30% in the 10-K (page:64); verified, not reconciled, immaterial to the credit view.
- Presentation difference: the release condenses captions (other assets; other expense, net) relative to the 10-Q; amounts agree (release page:3, page:4; 10-Q page:2, page:3).
- Correction to the credit synthesis: it states a Scores operating margin of 91% without a period. The 91% applies to the June 2026 quarter (10-Q page:32); FY2025 was 88% (10-K page:71). The synthesis conclusions do not depend on the 91% and are unchanged. The earlier handoff cannot be edited; this note is the correction.
- No contradiction between modules on direction: all four describe leverage as rising, cover as falling on a run-rate basis, and liquidity as adequate near term.

### Research integrity grade and committee use

Committee status: Restricted. Quality grade: the evidence trace is clean; the restriction arises from missing documents and the analyst-constructed nature of the covenant-related metrics, not from defects in the trace. Confidence band: Low under the Restricted cap; no numeric score is asserted by the reviewer.

| Use | Permitted | Basis |
| --- | --- | --- |
| Business description, segments, customer concentration | Yes | Filed 10-K and 10-Q text, verified |
| Reported financials, debt table, cash flow, interest | Yes | Filed statements, recomputed |
| Analyst leverage, cover, liquidity and maturities | Yes, as labelled constructions | Recomputed; definitions disclosed |
| Covenant headroom or compliance conclusions | No | Definition and executed agreement not supplied; headroom Not calculable |
| Guarantor, security, priming or distribution restriction conclusions | No | Indentures and credit agreement not supplied |
| Ownership, control and related-party conclusions | No | Proxy statement not supplied |
| Anything after July 29, 2026 | No | Not supplied |

### Strongest contrary evidence

- To the claim that headroom to the covenant is thin: the ratio is 3.91x if share-based compensation is added back, which would put the ratio below the 4.0x step-down level; free cash flow of US$960.9m for the last twelve months exceeds amortisation of US$300.0m; and the board can slow repurchases. What would make it win: a covenant EBITDA definition that adds back share-based compensation or other items, or a 10-K reporting a lower ratio. The reviewer cannot resolve this without the credit agreement; the confidence of the thin-headroom claim stays Medium.
- To the claim that earnings are concentrated and price dependent: Software retention of 109% and recurring revenue growth, and the nine-month text that adds mortgage volume to price as a driver. These reduce but do not remove the dependence.
- To the claim that distributions are creditor-negative: the company continues to report transparently, remained in stated compliance, and has no documented creditor-adverse action; this is why the behaviour label is mechanical, not intentional.

### Downside path and monitoring triggers

Initiating condition: a mortgage-score pricing or policy change, or a bureau pricing dispute, reduces Scores revenue per score. First operational break: segment operating income falls at a very high drop-through rate. Financial transmission: analyst EBITDA falls, which raises total debt to EBITDA from 4.46x toward the 4.5x maximum, while run-rate interest of US$316.5m is already above last twelve months cash interest of US$164.9m. Liquidity and refinancing consequence: cash of US$248.4m and a derived undrawn revolver of US$290.0m must meet US$300.0m of term loan amortisation within twelve months and, later, US$1,987.5m in FY2028. Observable triggers: the fiscal Q4 2026 release (leverage and the September 30, 2026 instalment), the pace of repurchases against free cash flow, the settlement of the accelerated share repurchase, any FHFA or bureau pricing change, and the step-down date of December 31, 2026. These triggers are monitoring items, not forecasts.

## Calculations

Independent recomputation by the reviewer from source figures (US$ thousands as printed).

| Item | Inputs | Result | Matches handoff |
| --- | --- | --- | --- |
| Balance sheet total assets, June 30, 2026 | 881,563 + 56,093 + 90,988 + 23,087 + 791,815 + 92,384 + 101,443 | 2,037,373 | Yes (10-Q page:2) |
| Total liabilities | 745,191 + 5,282,389 + 15,621 + 91,307 | 6,134,508 | Yes |
| Stockholders' deficit | 2,037,373 - 6,134,508 | (4,097,135) | Yes |
| Cash reconciliation, nine months | 777,880 - 39,276 - 622,345 - 1,951 = 114,308; 134,136 + 114,308 | 248,444 | Yes (10-Q page:4) |
| Total debt | 300,000 + 1,200,000 + 710,000 + 900,000 + 1,500,000 + 1,000,000 - 27,611 | 5,582,389 | Yes (10-Q page:10) |
| Operating income, nine months | 1,877,824 - 878,682 | 999,142 | Yes |
| LTM operating income | 924,850 + 999,142 - 687,694 | 1,236,298 | Yes |
| LTM D&A | 14,952 + 12,123 - 10,931 | 16,144 | Yes |
| LTM EBITDA | 1,236,298 + 16,144 | 1,252,442 | Yes |
| Total debt / EBITDA | 5,582,389 / 1,252,442 | 4.457 (4.46x) | Yes |
| Net debt / EBITDA | (5,582,389 - 248,444) / 1,252,442 | 4.259 (4.26x) | Yes |
| LTM cash interest | 103,564 + 162,420 - 101,112 | 164,872 | Yes |
| EBITDA / cash interest | 1,252,442 / 164,872 | 7.597 (7.60x) | Yes |
| Annualised contractual interest | 36,000 + 90,000 + 62,500 + 40,065 + 87,945 | 316,510 | Yes |
| Run-rate cover | 1,252,442 / 316,510 | 3.957 (3.96x) | Yes |
| Free cash flow, nine months | 777,880 - (1,355 + 26,491) | 750,034 | Yes; release prints 750,035 (rounding of 1) |
| LTM free cash flow | 1,001,549 - 40,671 | 960,878 | Yes |
| Debt change, nine months | 5,582,389 - 3,055,691 | 2,526,698 | Yes |
| Maturity rows sum | 75,000 + 337,500 + 1,987,500 + 710,000 + 1,500,000 + 1,000,000 | 5,610,000 = face value | Yes |
| Cushion below 4.5x | 1,252,442 - (5,582,389 / 4.5 = 1,240,531) = 11,911; 11,911 / 1,252,442 | 0.95% | Yes |
| Scores margin, FY2025 | 1,026,243 / 1,168,575 | 87.8%, printed as 88% (10-K page:71) | New check supporting the correction |
| Scores margin, June 2026 quarter | 416,886 / 458,897 | 90.8%, printed as 91% (10-Q page:19, page:32) | New check |
| Repurchase accrual gap | 3,052,893 - 3,045,992; 25,318 - 18,416 | 6,901; 6,902 | New check |

## Gaps

| Gap | Severity | Affected | Action |
| --- | --- | --- | --- |
| Credit agreement, June 5, 2026 amendment, indentures and ASR agreement not supplied | Material | Covenant, guarantor, security and distribution conclusions | Obtain executed documents; keep Restricted until then |
| Covenant EBITDA and reported leverage ratio not printed | Material | Headroom | Headroom Not calculable |
| 2026 Proxy Statement not supplied | Medium | Ownership, board, related parties | Obtain |
| No evidence after July 29, 2026 | Material | Everything at fiscal year end | Add fiscal Q4 release and 10-K |
| Letters of credit not disclosed | Medium | Liquidity upper bound | Obtain |
| Reviewer did not inspect images, charts or XBRL; tables were read from text extraction | Low | Table fidelity | Spot-check against filed HTML |
| Credit synthesis margin wording | Minor | Wording only | Corrected in this handoff |

## Next module

This is the last module of the minimum set. Deliver with the stated restriction: the report may be used for business, reported-financial, debt-structure, liquidity and concentration facts and for labelled analyst constructions, but not for covenant headroom, guarantor, security or ownership conclusions until the credit agreement, indentures and proxy statement are obtained and the fiscal Q4 2026 results are added.
