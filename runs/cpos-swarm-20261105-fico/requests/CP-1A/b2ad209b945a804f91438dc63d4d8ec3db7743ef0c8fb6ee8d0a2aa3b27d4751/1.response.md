# CP-1A - Business and transaction context: FAIR ISAAC CORP (fico)

## Request

- Issuer: FAIR ISAAC CORP (Fair Isaac Corporation, NYSE "FICO", issuer id `fico`), as of 2026-11-05, information cutoff 2026-11-05.
- Scope: the fact pack a committee reads first: transaction and ownership structure, business and operating model, credit-relevant history and change, issuer-level governance and capital allocation behaviour. Creditor perspective. No peer ranking, instrument recommendation or recovery conclusion.
- Transaction: the context lists no deal terms. The transactions in scope are the issuer's own 2026 financing and capital return events found in the filings: the term loan, the 2026 Senior Notes, the repayment of the 2018 Senior Notes and the accelerated share repurchase.
- Periods and currency: USD; fiscal year ends September 30. Fiscal Q3 2026 is the quarter ended June 30, 2026; FY2025 is the year ended September 30, 2025. Figures that appear here are references to accepted CP-1 figures or quoted source labels.
- Handoffs consumed: CP-0 (readiness and limitations) and CP-1 (financial base). CP-1 figures used: total debt US$5,582.4m at June 30, 2026 against US$3,055.7m at September 30, 2025; analyst total debt to EBITDA 4.46x; free cash flow US$750.0m and cash repurchases US$3,046.0m for nine months; cash US$248.4m; derived undrawn revolver US$290.0m.

## Sources

| Source (exact name) | sha256 | Use |
| --- | --- | --- |
| 10-K_2025-09-30_fico-20250930.htm.jsonl | 2cd0fc2b16386652e87f31c986fda43ca1da2a923ef1840b57f765a69322682e | Business description, customers, risk factors, governance exhibits, history |
| 10-Q_2025-12-31_fico-20251231.htm.jsonl | 905bfc6e05d39d56e0eed3225e1079b7eb97528806ef0d9d2d8efa0e76893510 | Q1 FY2026 interim context; Q1 debt and revolver terms |
| 10-Q_2026-03-31_fico-20260331.htm.jsonl | 1d56011f469dd7f9f01c0afabb2cc5e52bf600c9b61e1e02a22c20a1382a76cb | Q2 FY2026 interim context; 2026 Senior Notes issuance |
| 10-Q_2026-06-30_fico-20260630.htm.jsonl | 9928c89c8cd74e2a4ae5180bf504e58edee7d7a0cfbf531e71dc30f830e9f9a7 | Controlling source for the June 2026 financing, ASR, concentration, KPIs, litigation |
| EX-99.1_2026-01-28_exhibit991erq12026.htm.jsonl | 7ff326f8e766ed76e0e346c09be22d1a6689de853a63261725535c212fd1ea11 | Q1 FY2026 release; management language only |
| EX-99.1_2026-04-28_exhibit991erq22026.htm.jsonl | 98fcf8141dae7e420bccc2579f8ef67af179818384ed4fb3d51d12d1c6831d98 | Q2 FY2026 release; guidance history |
| EX-99.1_2026-07-29_exhibit991erq32026.htm.jsonl | 4bcf15097cd5d352a02b7a02cc65369e0e3cdadccda74b9b84b0c06bd098be52 | Q3 FY2026 release; management narrative and guidance |
| context | 67fd10ada0c60e1a58280c6938025b16a97aebcc1d2e25ac2914a3e17b05c7a0 | User run settings; not issuer evidence (ownership, deal, rating fields blank) |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | bf1dc2c14187a6208c7ecc4cc4dcd1ace42a402c8c8aa295e5e74d0134c7d3d4 | Readiness, located pages, gaps (no executed financing documents; no evidence after July 29, 2026) |
| CP-1 | 1a096021c0f3adbc74479c24fc532da87239b821a5817bc5b560d7c9fa7efb1f | Financial base: debt, leverage, interest, liquidity, maturities |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| FICO is a profitable, asset-light scoring and software business whose revenue leans on three credit bureaus and mortgage score pricing. It is a public company with no sponsor that now funds large buybacks with debt. | Medium | Ownership, proxy governance and executed financing documents are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Three consumer reporting agencies produced 63% of revenue in the June 2026 quarter, up from 54% a year earlier. | Revenue is concentrated in a few counterparties whose pricing practices can affect FICO. | High |
| Scores revenue growth in the quarter was primarily attributed to a higher mortgage origination scores unit price. | Earnings growth depends on pricing that regulators or the bureaus could change. | Medium |
| The 2026 financing events were a new term loan, new 2034 notes and an accelerated share repurchase, with the term loan proceeds used for the repurchase. | Debt-funded shareholder returns lower the cushion for creditors. | High |
| Software recurring revenue is shifting to the platform product while non-platform recurring revenue declines. | Software growth is modest and does not offset Scores dependence. | Medium |
| An antitrust class action over FICO Score distribution continues, with no amount or accrual stated. | A contingent claim exists without any quantified exposure. | Low |

### Business and transaction view

FICO is a Delaware-incorporated, NYSE-listed analytics company with two segments. Scores sells the FICO Score mainly through Experian, TransUnion and Equifax, which pay FICO a fee for each score generated; Software sells decisioning products as SaaS or on-premises. Revenue is concentrated by counterparty (three bureaus), by end market (financial services) and by geography (the Americas), and recent growth is concentrated in Scores pricing on mortgage originations. The company has no sponsor and no controlling holder is evidenced in the supplied sources; ownership detail sits in a proxy statement that is not supplied. The creditor-relevant change in the period is financial policy: in FY2026 the company issued new notes, drew a term loan and funded a large accelerated share repurchase, taking analyst total debt to EBITDA to 4.46x per the financial base. The documented behaviour is debt-funded shareholder distribution within the permissions of an unsecured credit agreement and in compliance with its stated covenants; no priming, drop-down or non-pro-rata exchange is documented. The business is high-margin and cash generative, but its revenue depends on a small number of counterparties and on score pricing, so the credit rests on continued pricing power and on management's leverage choices, not on structural protection.

### Company and operating model

| Driver | What the source says | Evidence (locator) | Risk mechanic | Creditor implication | Category |
| --- | --- | --- | --- | --- | --- |
| Scores B2B revenue model | Scores are sold through consumer reporting agencies, which pay FICO a fee for each score generated | 10-K page:6: "Users of our scores generally pay the consumer reporting agencies a fee for each individual score generated by our algorithms, and the consumer reporting agencies pay an associated fee to us" | Revenue is per-score volume times a unit price set in bureau contracts; FICO does not hold the credit data or sell directly to most lenders | Volume (originations, applications) and price are the two drivers of the largest profit pool; the bureaus are intermediaries and customers | Documentary Fact |
| Bureau concentration | Experian, TransUnion and Equifax each exceed 10% of revenue | 10-Q page:15: "accounted for 63% and 54% of our total revenues in the quarters ended June 30, 2026 and 2025" | Loss, repricing or distribution change at one bureau hits a large share of revenue | Counterparty concentration raises revenue volatility; bureaus also compete with FICO scores | Documentary Fact |
| Mortgage pricing | B2B growth tied to mortgage origination score price | 10-Q page:26: "primarily attributable to a higher mortgage origination scores unit price" | Price actions on a regulated, mortgage-linked product drive margin; FHFA rules can change the score used | Growth of this size is not repeatable by volume alone and is exposed to policy change | Documentary Fact |
| Policy risk on mortgage use | FHFA, Fannie Mae and Freddie Mac approval of the FICO Score is ongoing, and a July 2025 FHFA change lets originators choose the score | 10-K page:36: "permitting mortgage originators to choose the credit score they submit" | Competing scores could take share of mortgage deliveries; the 10-Qs do not update this point | Downside tail for Scores revenue; current status after the 10-K is Not supplied | Documentary Fact |
| Scores margin | Scores segment operating margin rose in the quarter | 10-Q page:32: "increased to 91% from 88%" | Very low incremental cost means price changes drop through to EBITDA | High operating leverage cuts both ways for leverage ratios | Documentary Fact |
| Software revenue model | SaaS and on-premises software plus services; platform shift | 10-Q page:14: platform software 52% of quarter software revenue against 33% a year earlier | Recurring revenue grows on the platform product while non-platform declines (ARR page:24) | Modest software growth; a platform transition risk rather than a source of creditor cushion | Documentary Fact |
| Recurring revenue visibility | Software ARR and net retention are disclosed | 10-Q page:22: "Annual Recurring Revenue for our Software segment as of June 30, 2026 was $815.8 million" and net retention of 109% | Retention above 100% supports revenue visibility; non-platform retention is below 100% (page:25) | Visibility is bounded to Software, the smaller segment | Documentary Fact |
| Contract backlog | Remaining performance obligations | 10-Q page:16: "Revenue allocated to remaining performance obligations was $680.4 million as of June 30, 2026" | Backlog excludes usage-based and variable fees, so is not total future revenue | Limited coverage of Scores, which is largely usage-based | Documentary Fact |
| Cost structure and capex | By-function costs, light capital spend, deferred revenue billed in advance | 10-Q page:27: cost lines as a share of revenue; CP-1 free cash flow US$750.0m for nine months | Low capital intensity gives high cash conversion; annual billings in advance support working capital | Cash flow can fund debt service but is exceeded by buybacks | Documentary Fact |
| Management narrative | Management says it delivered "another quarter of strong performance" | Release page:1 | Promotional characterisation | Not adopted; figures come from the 10-Q | Management Language |

### Company profile

| Attribute | Value | Evidence and category |
| --- | --- | --- |
| Legal name and listing | Fair Isaac Corporation; common stock on the New York Stock Exchange, symbol FICO | 10-Q page:1; Documentary Fact |
| Incorporation and headquarters | Delaware; Bozeman, Montana | 10-Q page:1; Documentary Fact |
| Sector and country | "Services-Business Services, NEC"; United States | Context (user setting, not issuer evidence) |
| Business | Global analytics software leader, founded 1956; two segments, Scores and Software | 10-K page:5; Documentary Fact |
| Customers and markets | Financial services is the largest market segment at 92% of FY2025 revenue; the Americas 87% of FY2025 revenue | 10-K page:15; Documentary Fact |
| Employees | 3,876 at the end of the June 2026 quarter | 10-Q page:27; Documentary Fact |
| Fiscal year end | September 30 | 10-K page:1; Documentary Fact |
| Auditor | Deloitte and Touche LLP | 10-K page:88; Documentary Fact |
| Chief executive and chief financial officer | William J. Lansing (CEO since January 2012); Steven P. Weber (CFO since May 2023) | 10-K page:30; Documentary Fact. Individuals are named for identification only; no assessment of them is made |
| Shares | 21,597,635 outstanding on July 17, 2026, with 67,259,148 held in treasury | 10-Q page:1; Documentary Fact |
| Ownership and control | Public company, large accelerated filer; no sponsor or controlling holder is evidenced; beneficial ownership is in the proxy statement, which is not supplied | 10-Q page:1; 10-K page:132; Insufficient Information on holders and percentages |
| Dividends | No cash dividends declared or paid since May 2017 | 10-K page:61; Documentary Fact |
| Ratings and market quotes | Blank in context | Insufficient Information |

### Transaction summary and new debt issues

There is no sponsor transaction, merger or acquisition in the supplied sources; the context lists no deal terms. The transactions that matter to a creditor are the issuer's own financing and capital return events in fiscal 2026. On March 20, 2026 the company issued senior notes carrying a 6.25% coupon and maturing September 15, 2034, in a private offering to qualified institutional investors, and on March 26, 2026 it used the proceeds to repay in full the 2018 Senior Notes before their May 2026 maturity (10-Q page:12). On June 5, 2026 it amended its credit agreement to provide a term loan borrowed in full that day and maturing May 15, 2028, with quarterly amortisation, and the 10-Q states that the proceeds were used to fund an accelerated share repurchase agreement (10-Q page:11, page:22). The same day it entered an accelerated share repurchase agreement with Wells Fargo Securities, paying $1.5 billion and receiving an initial delivery of shares equal to approximately 80 percent of the expected total, with $300.0 million treated as a prepayment pending settlement, which the company expects in the fourth quarter of fiscal 2026 (10-Q page:13). The June 2026 repurchase program authorises repurchases up to an aggregate cost of $2.0 billion, of which $800.0 million remained at June 30, 2026, including the prepayment awaiting settlement (10-Q page:36). In sum, the financing replaced a maturing note with a longer note and added a term loan whose proceeds were returned to shareholders, taking total debt from US$3,055.7m at September 30, 2025 to US$5,582.4m at June 30, 2026 per the financial base. Liquidity effect: cash is US$248.4m and the derived undrawn revolver is US$290.0m before letters of credit, and the term loan amortises at a quarterly rate with US$300.0m due within twelve months. The status of each event is completed except the settlement of the repurchase agreement, which is a stated expectation, and the September 30, 2026 instalment and later events are Not supplied because nothing after the July 29, 2026 filings is in the pack. The credit agreement, its June 5, 2026 amendment, the indenture for the 2026 notes and the repurchase agreement are not supplied, so the amortisation schedule, guarantor position, covenant definitions and any restrictions on distributions rest on the 10-Q summary text. The use of proceeds and debt raised are Documentary Facts; the characterisation of the repurchase as returning capital to stockholders is Management Language (10-K page:63).

### Fact register

| ID | Area | Fact | Locator | Category |
| --- | --- | --- | --- | --- |
| F1 | Company | Scores B2B scores are "primarily distributed through major consumer reporting agencies worldwide" | 10-K page:6 | Documentary Fact |
| F2 | Company | "Most leading banks and credit card issuers rely on our solutions" | 10-K page:5 | Management Language |
| F3 | Customers | Revenue from Experian, TransUnion and Equifax was 51% of FY2025 revenue, 45% of FY2024 and 41% of FY2023 | 10-K page:15 | Documentary Fact |
| F4 | Customers | Three customers, up from two, each accounted for 10% or more of consolidated receivables at June 30, 2026 | 10-Q page:15 | Documentary Fact |
| F5 | Operating model | Usage-based fees were approximately 20% of annualised ACV bookings in the 10-Q; the 10-K says approximately 30% | 10-Q page:23; 10-K page:64 | Documentary Fact (logged as a difference, see Conflicts) |
| F6 | Ownership | Anti-takeover provisions may deter or delay a change of control | 10-K page:56 | Documentary Fact |
| F7 | Ownership | A shareholder rights plan "is no longer in effect"; no Series A preferred shares were issued | 10-K page:130 | Documentary Fact |
| F8 | Ownership | Beneficial owner percentages, board composition and related-party transactions are incorporated by reference to the 2026 Proxy Statement | 10-K page:132 | Insufficient Information: percentages, control rights and related-party dealings are missing; they matter for willingness assessments |
| F9 | Governance | 17 executives are party to a management agreement with payments on a qualified change in control followed by termination | 10-K page:126 | Documentary Fact |
| F10 | Governance | Restated Certificate of Incorporation dated March 4, 2026 is on the exhibit list; its content is not supplied | 10-Q page:45 | Insufficient Information: charter terms not read |
| F11 | Capital allocation | Board approved successive repurchase programs, most recently of $2.0 billion in June 2026 replacing the February 2026 program | 10-Q page:36 | Documentary Fact |
| F12 | Capital allocation | Borrowings may be used for "the repurchase of our common stock" under the credit agreement | 10-Q page:11 | Documentary Fact (legal capacity as summarised) |
| F13 | Capital allocation | The term loan proceeds "were used to fund an accelerated share repurchase agreement" | 10-Q page:22 | Documentary Fact |
| F14 | Acquisitions | The cash flow statements show no acquisition or disposal line in FY2024, FY2025 or the nine months of FY2026; a product line asset sale appears only in FY2023 | 10-K page:90; 10-Q page:4 | Documentary Fact |
| F15 | Restructuring | FY2025 includes restructuring charges, a one-off expense line | 10-K page:89 | Documentary Fact |
| F16 | Litigation | Putative class actions allege antitrust claims over FICO Score distribution; the court allowed a Sherman Act Section 2 claim and state claims against FICO to proceed through discovery | 10-Q page:43 | Documentary Fact |
| F17 | Litigation | "we have determined we do not have a material exposure, either individually or in the aggregate" for reasonably possible losses | 10-Q page:20 | Management Language |
| F18 | Regulation | FICO is subject to consumer credit reporting, privacy and related regulation | 10-K page:20 | Documentary Fact |
| F19 | Debt | Covenants: maximum consolidated leverage ratio of 4.5 to 1.0 through December 30, 2026, stepping down; compliance stated | 10-Q page:11, page:12 | Documentary Fact |
| F20 | Debt | The notes' indentures "contain certain covenants typical of unsecured obligations" | 10-Q page:12 | Management Language (characterisation; terms not supplied) |
| F21 | Disclosure | No debt schedule beyond the filed notes, no covenant certificate and no add-back bridge are supplied | CP-0 | Insufficient Information: monitoring inputs missing; severity Medium |

### Ownership and sponsor position

FICO is a listed company whose shares are widely held on the evidence available; the supplied sources give 208 holders of record at October 23, 2025 (10-K page:61), which is not a measure of beneficial ownership. No sponsor, parent or controlling shareholder is named, and the context leaves those fields blank, which is not evidence of absence. Control rights are the ordinary Delaware public-company provisions and anti-takeover features described in the 10-K (page:56). Prior ownership and any dividend recapitalisation history: none are disclosed; the company states that it has paid no cash dividends since May 2017 (10-K page:61). Percentages are not inferred.

### Governance and capital allocation behaviour

| Dimension | Documented action | Behaviour category | Legal capacity, willingness, feasibility |
| --- | --- | --- | --- |
| Debt-funded distributions | The term loan was drawn to fund an accelerated share repurchase, and cash repurchases far exceeded free cash flow in nine months (CP-1) | Extraction-Oriented in mechanics (debt-funded distributions to shareholders); no related-party leakage is documented | Capacity: the credit agreement permits use of borrowings for repurchases (10-Q page:11). Willingness: done, and a $2.0 billion program authorised (10-Q page:36). Feasibility: cash US$248.4m, derived undrawn revolver US$290.0m, free cash flow US$750.0m for nine months (CP-1) |
| Transparency | Quarterly 10-Q and release disclose debt, covenants, ASR terms and customer concentration | Supportive | Reporting is detailed; a covenant ratio value and add-back bridge are not given |
| Creditor-adverse actions | None documented: no priming, uptiering, drop-down, non-pro-rata exchange or collateral release | Insufficient Information on the absence of such terms (documents not supplied) | The debt is unsecured, so collateral release is not applicable on the filings read |
| Refinancing behaviour | Repaid the 2018 notes ahead of maturity with new notes; extended the revolver to May 13, 2030 in May 2025 | Neutral or Mixed | Extends maturities but at higher coupons: 6.25% for the 2026 notes against 5.25% on the repaid notes |

The row labels describe mechanics, not intent. The company is a listed corporation, so no inference is drawn from sponsor identity.

### Timeline

| Date | Event | Source | Note |
| --- | --- | --- | --- |
| 1956 | Company founded | 10-K page:5 | Documentary Fact |
| 1989 | FICO Score introduced in the U.S. | 10-K page:6 | Documentary Fact |
| May 8, 2018 | 5.25% senior notes issued, due May 15, 2026 | 10-K page:75 | Repaid March 26, 2026 |
| December 6, 2019 and December 17, 2021 | 4.00% senior notes and add-on, due June 15, 2028 | 10-K page:75 | Outstanding |
| May 13, 2025 | 6.00% senior notes due May 15, 2033 issued; term loans repaid; revolver increased and extended to May 13, 2030 | 10-K page:74, page:75 | FY2025 |
| July 2025 | FHFA director change permitting originators to choose the score | 10-K page:36 | Dated in the 10-K |
| November 7, 2025 | FY2025 audit report and 10-K | 10-K page:88 | Cutoff-safe |
| March 20 and 26, 2026 | 6.25% notes issued; 2018 notes repaid | 10-Q page:12 | FY2026 Q2 |
| June 5, 2026 | Credit agreement amended for a term loan; ASR agreement | 10-Q page:11, page:13 | FY2026 Q3 |
| July 29, 2026 | Q3 10-Q and release | 10-Q page:46 | Latest supplied |
| Fiscal Q4 2026 | Expected ASR settlement | 10-Q page:13 | Subsequent event, forward-looking; Not supplied beyond expectation |

### Conflicts

- Usage-based share of ACV bookings: the 10-Q states "ACV Bookings related to estimates of future usage-based fees was approximately 20% of the total ACV Bookings amount on an annualized basis" (10-Q page:23), while the 10-K states "approximately 30% of the total ACV Bookings amount on an annualized basis" (10-K page:64). The periods differ; both are logged and neither is chosen or reconciled. Effect: usage-based exposure of recurring software bookings is Not determinable as a single figure.
- No other conflict between filings and releases was found in the lines read.

### Credit translations

#### Revenue durability

- Evidence: bureau revenue was 63% of the June 2026 quarter (10-Q page:15) and the Scores segment growth was "primarily attributable to a higher mortgage origination scores unit price" (10-Q page:26).
- Mechanic: a per-score fee through three intermediaries means a small number of contract terms and one pricing lever set revenue; Software is a smaller, slower segment.
- Implication: revenue is durable while FICO Score use is required or preferred in mortgage and consumer credit decisions, but pricing and policy shifts can lower it quickly; a revenue shortfall hits debt service and the covenant ratio together. Counter: the retention rate above 100% in platform software (10-Q page:25) supports part of the base.

#### Margin and cash-flow risk

- Evidence: Scores operating margin of 91% (10-Q page:32) and free cash flow of US$750.0m for nine months (CP-1).
- Mechanic: high operating leverage means revenue changes flow almost fully to EBITDA; cash conversion is high because capital spending is light.
- Implication: cash flow could service the new debt if price and volume hold, but the interest run-rate is far above LTM cash interest per CP-1, so margin of safety depends on revenue holding.

#### Concentration and policy risk

- Evidence: bureau concentration (10-Q page:15), financial services 92% and Americas 87% of FY2025 revenue (10-K page:15), and FHFA policy exposure (10-K page:36).
- Mechanic: single-counterparty, single-sector and single-policy exposures are correlated with the mortgage cycle.
- Implication: tail risk of loss of score preference, not covered by diversification.

#### Sponsor alignment and financial policy

- Evidence: no sponsor; debt-funded repurchases with a $2.0 billion authorisation (10-Q page:36).
- Mechanic: shareholder-return policy sets leverage; the board can reverse it, but nothing in the supplied documents commits it to a leverage target.
- Implication: leverage tolerance is a management and board choice; creditors rely on covenants (4.5x stepping to 4.0x on December 31, 2026) not on sponsor support. Monitoring: watch repurchase pace against free cash flow and the covenant step-downs.

#### Key uncertainties

- Ownership and board detail (proxy), executed financing documents, the status of FHFA policy after July 2025, the antitrust case outcome, and all events after July 29, 2026 are Not supplied.

### Consumers

| Consumer | Readiness | What it should take from this module | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Fact rows F3, F11 to F13, F16, F19; the credit translations on revenue durability, concentration and financial policy | The fundamental credit view needs business risk beside the financial risk in CP-1 | Ownership, executed documents and post-July 2026 events | Keep Insufficient Information rows as gaps; do not treat absence of creditor-adverse terms as established |
| CP-5 | READY_WITH_LIMITATIONS | Citations to 10-K pages 6, 15, 36, 61 and 10-Q pages 11 to 13, 15, 20, 22, 23, 26, 36, 43 | The integrity review traces each claim to a page | The logged ACV difference; Management Language rows are not factual claims | Check Management Language rows are not used as fact |

## Calculations

None new. CP-1A calculates nothing. Figures are quoted source labels or references to accepted CP-1 figures: total debt US$3,055.7m and US$5,582.4m, analyst total debt to EBITDA 4.46x, cash US$248.4m, derived undrawn revolver US$290.0m, free cash flow US$750.0m and cash repurchases US$3,046.0m for nine months, amortisation of US$300.0m within twelve months. Percentages (63%, 54%, 51%, 92%, 87%, 91%, 88%) are printed in the sources.

## Gaps

| Gap | Severity | Affected | Action |
| --- | --- | --- | --- |
| 2026 Proxy Statement not supplied: beneficial owners, board, related-party transactions, executive pay | Medium | Ownership and governance | Obtain the proxy; until then treat control and related-party leakage as Not supplied |
| Credit agreement, June 5, 2026 amendment, indentures and ASR agreement not supplied | Medium | Transaction summary, covenants, distributions capacity | Obtain executed documents; restrictions on repurchases and guarantors are Not supplied |
| Nothing after July 29, 2026: ASR settlement, September 30, 2026 instalment, fiscal Q4 results and FHFA developments | Medium | All | Add later filings when available |
| No debt maturity schedule beyond the notes' stated dates, covenant certificate or add-back bridge | Medium | Monitoring | As in CP-0 |
| Antitrust case: no loss estimate; outcome unknown | Low | Contingent claims | Monitor the docket via later filings |
| Restated charter content not read | Low | Governance | Obtain Exhibit 3.1 to the March 2026 Form 8-K |
| Usage-based ACV share differs between filings | Low | Software visibility | Logged, not reconciled |

## Next module

Run CP-2 next on the CP-1 and CP-1A registers, then CP-5. Carry forward: bureau concentration, mortgage pricing dependence and FHFA policy exposure; debt-funded repurchases and the 2026 financing events; the covenant path from 4.5x to 4.0x on December 31, 2026; and the missing proxy, executed documents and post-July 29, 2026 evidence.
