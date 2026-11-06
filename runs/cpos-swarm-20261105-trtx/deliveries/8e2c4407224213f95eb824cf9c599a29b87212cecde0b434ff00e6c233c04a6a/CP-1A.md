## Request

Issuer: TPG RE Finance Trust, Inc. (issuer id trtx; NYSE ticker TRTX). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. Current period named by the context: Q3 2026. Prior period: FY2025.

Task for this module: build the business, ownership, operating-model, transaction and governance fact pack that a credit committee reads first, from the pinned filings and releases, taking the financial figures from the accepted financial base. Every claim is tagged Documentary Fact, Management Language, Analyst Interpretation or Insufficient Information. No external material is used; nothing in this handoff comes from outside the pinned sources. The context names no sponsor, parent, borrower, guarantor, deal terms or research questions; those blanks are treated as not supplied. The filings do describe TPG as the sponsor of the external manager, so the sponsor fact comes from the filings, not the context.

Prohibited by the method and not done here: peer ranking, instrument recommendation, expected recovery outcome. Periods are labelled: Q3 2026 is the three months to 2026-09-30; 9M 2026 is the nine months to that date; balance sheet items are at the stated date.

## Sources

Locators are `page:N` chunks of the named file, not printed pages.

### Issuer sources relied on

| Source name | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_trtx-20251231.htm.jsonl | 7b7b804dc956c7ba20b8c615f59942074ed4837f19257133ae8d92323027d7ec | Audited annual report: business, manager, risk factors on conflicts, management agreement note, exhibit index |
| 10-Q_2026-03-31_trtx-20260331.htm.jsonl | 41f66a4a0f2f9734dca4554ee0dc2ef549772c06941cdfec976d06a5c1955d4c | Q1 2026 quarterly report |
| 10-Q_2026-06-30_trtx-20260630.htm.jsonl | 8f3da972b3575ac6703be3527817c87d3dc87cac2d5c8e1d4e7f81f5f78727e9 | Q2 2026 report: Term Loan B, Revolver, repurchase program history, exhibit list |
| 10-Q_2026-09-30_trtx-20260930.htm.jsonl | 4884d7a3b9e5f3a0f552349b7976aff0931070e9957fb8740966840f61145adc | Q3 2026 report: latest business, related party, funding, portfolio and subsequent events |
| EX-99.1_2026-04-28_trtx-20260428exhibit991.htm.jsonl | 1e95941ab9e70def087e8a13656b49994337a0e1c905b17c9ac6471bddea9d88 | Q1 2026 earnings release; management attribution |
| EX-99.1_2026-07-28_trtx-20260728exhibit991.htm.jsonl | 85e111cdb3f106d12964e884db844b225d24404d7815e760f617225c97335579 | Q2 2026 earnings release; management attribution |
| EX-99.1_2026-10-26_trtx-20261026exhibit991.htm.jsonl | 262caea8fdb587a93bfd4ce5d18d486a64c133d5eee9d2c7316a1e31375c2fe8 | Q3 2026 earnings release; management attribution |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | ef96ebbdf5dd00ebb7411d32513edde7f00e3900728e79b850efc1744349d270 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | f67c880ae13bd9b442ec32f542cac48afaa8a23c51c32c03c025a6a9e94e025f | Source readiness and limits: no executed agreements, no later filings, no presentations |
| CP-1 | d2958939fbb55f95e859a0d7163b8ff7248dbe00f5d7f7b77f17ee8c523f59b6 | Financial base: statements, funding stack, recourse, liquidity, covenants; its figures are referenced here and not recomputed |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| TRTX is an externally managed, floating-rate commercial real estate lender with a TPG-affiliated manager. The filings give a clear business and funding picture, but no sponsor support commitment, executed agreement or ownership percentage is supplied. | Medium | Executed agreements, shareholder ownership percentages and the use of proceeds of the October 2026 CLO are not supplied, so governance conclusions rest on filings alone. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| TRTX has no employees and is run by a TPG affiliate that earns a base fee of 1.50% of equity; no incentive fee was earned in 2026. | Fees are paid regardless of credit outcomes, so manager incentives align with creditors only loosely, though other related-party fees are small. | High |
| In May 2026 TRTX closed a 400.0 million Term Loan B and a 100.0 million Revolver, both fully recourse, and redeemed its 2022 CLO. | Funding shifted toward larger secured credit agreements and a recourse corporate layer secured on substantially all assets. | High |
| A 1.0 billion managed CRE CLO closed on 2026-10-02, after quarter end, and a new 50.0 million buyback was approved on 2026-10-26. | The CRE CLO type is described as non-recourse and non-marked, but its use of proceeds is not disclosed; buybacks reduce equity while leverage is higher. | Medium |
| The portfolio is 52.6% multifamily and 22.6% industrial, almost all floating rate; office rose to 7.9% after a new 212.0 million loan. | Collateral mix is mostly multifamily and industrial, but office exposure rose in the latest quarter and one foreclosure shows transition risk remains. | High |
| The 10-K expected total debt to equity to be generally below 3.75:1, while the latest printed total leverage ratio is 4.03x. | Leverage is above the company's own stated expectation on one measure, so leverage tolerance and the basis of the target need confirming. | Medium |

### Business and transaction view

TRTX is a REIT that originates and acquires floating-rate commercial real estate first mortgage loans, financed mainly by CRE CLOs, secured credit agreements and, since May 2026, a corporate Term Loan B and Revolver. It has no employees; its Manager, TPG RE Finance Trust Management, L.P., an affiliate of TPG, runs the business under a Management Agreement, and the chief executive officer, president and interim chief financial officer are TPG Real Estate professionals (10-K page:7-8, page:17). The creditor-relevant structure is therefore a levered, externally managed lender: income is the spread between floating-rate loan interest and floating-rate funding cost, protected in part by interest rate floors on the loans, and creditor protection depends on collateral quality, on how much of the funding is non-recourse or non-marked, and on how a manager paid on equity behaves as leverage grows.

The transaction story is a refinancing and liability-management story, not a sponsor transaction. In the quarter ended 2026-06-30 the company closed a 400.0 million Term Loan B and a 100.0 million Revolver, upsized the Wells Fargo and Goldman Sachs secured credit agreements, closed a new 500.0 million Citi secured credit agreement, let the Barclays agreement lapse and redeemed the 2022 CLO (TRTX 2022-FL5) (10-Q Q3 page:43-44, page:48, page:55-57). After quarter end it closed a 1.0 billion managed CRE CLO, TRTX 2026-FL8, on 2026-10-02 and approved a new 50.0 million share repurchase program on 2026-10-26 (10-Q Q3 page:74). There is no change of control, no acquisition of TRTX and no sponsor equity injection in the pack.

On the financial side, which comes from the accepted financial base and is not recomputed here, debt principal rose to 4,198,054 thousand at 2026-09-30 and the issuer's total leverage ratio to 4.03x, with liquidity of 291,634 thousand against unfunded loan commitments of 236,552 thousand (CP-1 handoff). Against that, the business has stable reported credit indicators: weighted average risk rating 3.0 unchanged, no loan on non-accrual at 2026-09-30, and an allowance of 147 basis points of commitments (10-Q Q3 page:34, page:37, page:88). The main business-model risks are the combination of rising leverage with continued buybacks and dividends, the concentration of refinancing in 2028, the dependence on lender discretion for secured credit agreement availability, and the manager conflicts described below.

### Company and operating model

| Area | Fact | Category | Evidence locator | Creditor relevance |
| --- | --- | --- | --- | --- |
| Core activity | Originates, acquires and manages primarily first mortgage loans secured by institutional properties in primary and select secondary US markets; one operating and reportable segment | Documentary Fact | 10-Q Q3 page:11-12; release 2026-10-26 page:4 | Single-line lender: all earnings depend on loan performance and funding spread |
| Revenue model | Interest income on a floating-rate loan portfolio; 99.7% of loan commitments floating rate; real estate owned operations add rental revenue | Documentary Fact | 10-Q Q3 page:31, page:7-8, page:40 | Revenue visibility follows loan repayment and origination pace, not contract backlog |
| Asset pricing | Weighted average credit spread 3.1% and all-in yield 7.3% on the portfolio; weighted average interest rate floor 2.62% | Documentary Fact | 10-Q Q3 page:31, page:120 | Floors protect income if Term SOFR falls; all-in yield assumes Term SOFR at 2026-09-30 |
| Funding cost | CRE CLO financing weighted spread 1.75%; secured credit agreements Term SOFR plus 1.61%; secured revolver Term SOFR plus 2.00%; Term Loan B Term SOFR plus 2.75% | Documentary Fact | 10-Q Q3 page:45, page:90, page:52, page:56 | Corporate-level Term Loan B costs more than asset-level funding, narrowing the spread on any assets it funds |
| Rate sensitivity | Net floating-rate exposure 1,186,223 thousand; a 25 basis point rise adds 2,921 thousand and a 25 basis point fall removes 2,837 thousand to annual net interest income | Documentary Fact | 10-Q Q3 page:120 | Net income is positively exposed to rates; liabilities are index-matched and no derivatives are used |
| Volume drivers | 9M 2026: 13 loans originated and 1 acquired for 1.4 billion of commitments; repayments of 517.6 million; loan count 59 against 50 at 2025-12-31 | Documentary Fact | 10-Q Q3 page:31 | Portfolio grew about a fifth in commitments; growth is financed with debt |
| Prepayment and extension | 59.5% of loans by principal subject to yield maintenance or other prepayment restrictions; 40.5% open to repayment | Documentary Fact | 10-Q Q3 page:32 | Repayment timing drives CLO deleveraging and reinvestment |
| Asset mix | By commitment: multifamily 52.6%, industrial 22.6%, office 7.9%, hotel 7.6%, life science 6.5%, mixed-use 1.5%, self storage 1.3%; by category bridge 64.0%, moderate transitional 18.4%, light transitional 17.6% | Documentary Fact | 10-Q Q3 page:72-73 | Mostly transitional collateral that depends on borrower business plans |
| Geography | West 34.9%, South 23.4%, East 19.2%, Various 15.8%, Midwest 6.7%; all in the United States | Documentary Fact | 10-Q Q3 page:72 | Largest regional concentration is the West |
| Loan concentration | Largest loan 285.0 million (New York City multifamily); five largest loans 1,170.4 million | Documentary Fact with derived share | 10-Q Q3 page:115-116; Calculations | Top five loans are 22.6% of commitments |
| Credit indicators | Weighted average risk rating 3.0; rated 2: 173,354 thousand, rated 3: 4,622,896 thousand, rated 4: 120,125 thousand; weighted average loan-to-value 65.9% at origination or acquisition | Documentary Fact | 10-Q Q3 page:34, page:118-119 | LTV is a point-in-time underwriting measure, not a current valuation |
| Cost structure | No employees; base management fee 1.50% of Equity as defined; 15,983 thousand of management fees in 9M 2026; REO operating expenses 24,044 thousand | Documentary Fact | 10-K page:17; 10-Q Q3 page:62-63, page:8 | Fee base is not performance-linked |
| Capital spending | Capital expenditures on REO 7,138 thousand in 9M 2026; unfunded loan commitments 236,552 thousand, of which 26,740 thousand are due within a year | Documentary Fact | 10-Q Q3 page:10, page:71, page:108 | Future fundings are a call on liquidity |
| Working capital | Not disclosed as a metric; accrued interest and fees receivable 31,149 thousand | Insufficient Information | 10-Q Q3 page:6 | Not applicable to a lender; no working capital measure to monitor |
| Management characterisation | "continued successful execution of the business plan we communicated several years ago" | Management Language | release 2026-10-26 page:2 | Promotional; not adopted |
| Management characterisation | "securing highly durable, non-mark-to-market liquidity" | Management Language | release 2026-07-28 page:2 | The Term Loan B and Revolver are non-marked, but 52.6 million of cash is held for covenants (CP-1 handoff) |

### Company profile

| Attribute | Value | Category | Evidence locator |
| --- | --- | --- | --- |
| Legal name and state | TPG RE Finance Trust, Inc., a Maryland corporation; SEC file number 001-38156 | Documentary Fact | 10-Q Q3 page:1 |
| Listing | Common stock (TRTX) and 6.25% Series C Cumulative Redeemable Preferred Stock (TRTX PRC) on the New York Stock Exchange; common listed 2017-07-20 with the IPO closing 2017-07-25 | Documentary Fact | 10-Q Q3 page:1; 10-K page:115 |
| Sector and country | Commercial real estate finance REIT; assets secured by properties in the United States | Documentary Fact | 10-Q Q3 page:11, page:72 |
| Headquarters | 888 Seventh Avenue, 35th Floor, New York, New York | Documentary Fact | 10-Q Q3 page:1 |
| Structure | Holding company operating through TPG RE Finance Trust Holdco, LLC (wholly owned); CRE CLOs issued through TPG RE Finance Trust CLO Sub-REIT, whose common equity is owned through Parent LLC | Documentary Fact | 10-Q Q3 page:11, page:61, page:44 |
| Manager | TPG RE Finance Trust Management, L.P., a Delaware limited partnership, an affiliate of TPG | Documentary Fact | 10-Q Q3 page:6, page:74 |
| Sponsor scale | TPG had 303 billion of assets under management and TPG's Real Estate platform more than 38.2 billion at 2025-12-31; the TRECO Funds had 2.1 billion of commitments | Management Language (sponsor-stated scale) | 10-K page:7-8 |
| Employees | None; executive officers are employees of the Manager or its affiliates | Documentary Fact | 10-K page:17 |
| Board | Eight directors at 2025-12-31, three of whom are TPG employees; chairman Avi Banyasz | Documentary Fact | 10-K page:64, page:174 |
| Officers | Doug Bouquard, chief executive officer; Brandon Fox, interim chief financial officer and chief accounting officer | Documentary Fact | 10-Q Q3 page:136 |
| Auditor | Deloitte & Touche LLP, auditor since 2016; FY2025 opinion dated 2026-02-17 | Documentary Fact | 10-K page:177 |
| Filer status and year end | Accelerated filer; fiscal year ends 31 December | Documentary Fact | 10-Q Q3 page:1; 10-K page:1 |
| Common shares | 75,826,954 outstanding at 2026-10-23 | Documentary Fact | 10-Q Q3 page:2 |
| Preferred stock | Series C: 8,050,000 shares, 201,250 thousand liquidation preference; Series A: 125 shares; Series B redeemed in 2021 | Documentary Fact | 10-Q Q3 page:7; 10-K page:50 |
| Holders | Approximately 40 holders of record at 2026-02-17, excluding street name | Documentary Fact | 10-K page:115 |
| Ownership percentages of major holders, including TPG | Not supplied: Part III is incorporated by reference to a proxy statement that is not in the pack | Insufficient Information | 10-K page:168 |
| Parent, borrower and guarantor | No parent company is named. Term Loan B guarantors are "certain subsidiaries" and are not named | Insufficient Information | 10-Q Q3 page:56 |

### Transaction summary and new debt issues

All items below are completed unless labelled as a subsequent event. There is no transaction source for a sponsor deal, merger or change of control, and none is inferred; the pack describes financing and portfolio activity only.

In May 2026 TRTX closed a 400.0 million secured Term Loan B at a price of 99.75, bearing Term SOFR plus 2.75%, maturing May 2033, with quarterly amortization of 0.25% of the original principal from the last business day of December 2026. Obligations are guaranteed by certain subsidiaries and secured on a first-priority basis by substantially all assets of the company and certain subsidiaries (10-Q Q3 page:56). The filing says the Term Loan B and the Revolver are used "to repay outstanding indebtedness and for other general corporate purposes" (page:55); which indebtedness was repaid is not itemized, although the Q3 filing links the May 2026 redemption of TRTX 2022-FL5 to an upsized Wells Fargo agreement (page:44). At the same time TRTX closed a 100.0 million Revolver at Term SOFR plus 2.00% maturing May 2031, undrawn at 2026-09-30 (page:57). A Credit Agreement dated 2026-05-14 with Wells Fargo Bank, N.A. and other lenders is listed as an exhibit to the Q2 2026 10-Q (10-Q Q2 page:133); the filings do not say which facility it governs and the text is not supplied. The company also paid TPG Capital BD, an affiliate of TPG, 0.9 million for capital markets services on these facilities (10-Q Q3 page:65). The management characterised the closing as securing "highly durable, non-mark-to-market liquidity" (release 2026-07-28 page:2), which is Management Language; the Term Loan B and Revolver contain no margin calls, but they are fully recourse (CP-1 handoff).

Investment-portfolio financing also changed in 2026. On May 15, 2026 TRTX redeemed TRTX 2022-FL5, which had 597.8 million of investment-grade bonds outstanding, and refinanced 17 loans with an aggregate unpaid principal balance of 698.1 million primarily through the upsize of the Wells Fargo secured credit agreement (10-Q Q3 page:43-44). The Wells Fargo agreement was increased to 850.0 million and its maturity extended to May 12, 2028 on May 12, 2026, with no margin calls for one year from that date; the Goldman Sachs agreement was increased to 750.0 million on June 30, 2026; a new 500.0 million Citi agreement closed on June 30, 2026; the Bank of America maturity extension to June 6, 2029, executed in January 2026, took effect on June 6, 2026; and the Barclays agreement was allowed to expire on its initial maturity in May 2026 with no borrowings outstanding (page:48). In September 2026 a 29.1 million first mortgage loan from BMO Harris Bank on the Plano multifamily property replaced an asset-specific financing after the underlying loan converted to real estate owned through a non-judicial foreclosure on September 1, 2026, which crystallized a 13.0 million realized loss (page:39, page:54).

After the quarter, as a subsequent event, TRTX closed TRTX 2026-FL8, a 1.0 billion managed CRE CLO, on October 2, 2026, placing approximately 820.0 million of investment-grade securities with institutional investors (10-Q Q3 page:74; release 2026-10-26 page:4). Supporting exhibits (indenture, collateral interest purchase agreement, collateral management agreement and servicing agreement) were filed with an 8-K of October 6, 2026 that is not in the pack (page:135). The use of proceeds, the collateral, the retained interest, any related redemption of other debt and the effect on the secured credit agreements are not stated. The liquidity effect of the CLO cannot be assessed; the 2026-09-30 balance sheet does not include it. Also as a subsequent event, repayments of 72.2 million were received, including a full repayment of 61.5 million (page:74), and on October 26, 2026 the board approved a new share repurchase program of up to 50.0 million of common stock, which management described as "doubling our prior authorization" (release 2026-10-26 page:2); this is Management Language, and the prior authorization was a 25.0 million program announced on September 4, 2025 (10-Q Q2 page:132). Repurchases in 9M 2026 retired 3,021,254 shares for 24,613 thousand of cash (10-Q Q3 page:8-10; Calculations).

### Ownership and control

| Item | Evidence | Category | Locator |
| --- | --- | --- | --- |
| Control | External management; the Manager's investment committee is made up of senior TPG investment professionals, and investment decisions are approved there | Documentary Fact | 10-K page:7 |
| Board oversight | The Manager is "subject to the supervision and oversight of our board of directors"; investments above 300 million, or above 25% of Equity in one investment, need approval of a majority of independent directors | Documentary Fact | 10-K page:8, page:16 |
| Economic interest of TPG in TRTX equity | Not supplied: no TPG share ownership is stated in the pack | Insufficient Information | 10-K page:168 |
| Termination | A termination fee of three times the sum of average annual base and incentive fees over the prior 24 months is payable if TRTX terminates without cause or the Manager terminates for TRTX's material breach | Documentary Fact | 10-Q Q3 page:64 |
| Exclusivity | While the agreement is in effect and TPG controls the Manager, neither the Manager nor TPG Real Estate Management, LLC will form another US public vehicle to primarily originate performing commercial mortgage loans | Documentary Fact | 10-K page:65 |
| Prior ownership and recapitalisation history | No dividend recapitalisation, debt-funded distribution or change of control is described in the pack; the company went public in July 2017 | Documentary Fact (absence in the pack is not a conclusion about earlier years) | 10-K page:115 |
| Fee base | Base fee 1.50% of Equity as defined in the Management Agreement, with net proceeds of preferred stock included; incentive fee of 20% of Core Earnings above a 7% hurdle on Equity, none paid in 2023, 2024, 2025 or 9M 2026 | Documentary Fact | 10-Q Q3 page:62-63; 10-K page:232 |

### Governance and sponsor behaviour

This section assesses issuer-level documented behaviour only, not individuals, and draws no inference from the sponsor's identity or brand.

| Behaviour | Documented action | Category and translation to mechanics | Evidence quality | Locator |
| --- | --- | --- | --- | --- |
| Capital allocation to equity holders | Quarterly common dividend 0.24 per share maintained in each quarter of 2026; repurchases of 3,021,254 shares for 24,613 thousand of cash in 9M 2026; new 50.0 million program on 2026-10-26 | Neutral or Mixed. Distributions and buybacks use cash while leverage and covenant cash needs rose; earnings before realized losses roughly matched the dividend (CP-1 handoff) | High | 10-Q Q3 page:8-9, page:10; release 2026-10-26 page:2 |
| Affiliate fees | Base fee 15,983 thousand in 9M 2026 on a fee base not tied to performance; reimbursement of 1.1 million of manager expenses; 0.4 million to SOP 2 Management, LLC (a portfolio company owned by an affiliate of TPG) for REO asset management; 0.9 million to TPG Capital BD | Neutral or Mixed. Related-party payments are disclosed and small beside the management fee; fee base is not reduced by realized losses | High | 10-Q Q3 page:63-65 |
| Support and funding conduct | No equity injection, deleveraging commitment or guarantee by TPG appears in the pack; Holdco, a TRTX subsidiary, gives limited guarantees on secured credit agreements | Insufficient Information for sponsor support; mechanically, support rests on TRTX's own balance sheet | High | 10-Q Q3 page:89, page:92 |
| Creditor-adverse actions | No priming, uptiering, drop-down, non-pro-rata exchange or collateral release is described. The Term Loan B grants a first-priority lien over substantially all company assets, ranking ahead of equity holders; no other unsecured creditor is identified | Insufficient Information for adverse behaviour; none documented | High | 10-Q Q3 page:56 |
| Disclosure | Quarterly filings with a loan-by-loan schedule, risk ratings, recourse by facility and liquidity tables; covenant test values and executed agreements are not disclosed | Supportive for loan and funding transparency; limited for covenant values | High | 10-Q Q3 page:115-119, page:89, page:55 |
| Related-party conflicts acknowledged by the issuer | Conflicts with TPG and the TRECO Funds on opportunity allocation, personnel time and fee incentives; three of eight directors are TPG employees | Documentary Fact; the issuer itself says there is no guarantee conflicts will be resolved in its favour | High | 10-K page:64-66 |

Legal capacity, willingness and feasibility are kept apart. Legal capacity: the board-approved investment guidelines and the covenants limit concentration and leverage, but the 10-K leverage expectation of "generally be less than 3.75:1" is an expectation, not a covenant, and the company reserves the right to adjust the range without advance notice (10-K page:15); the covenant maximum for total debt to total assets is 83.333% (10-Q Q3 page:57). Willingness: documented actions are dividends, buybacks and refinancing, with no creditor-adverse transaction. Feasibility: liquidity of 291,634 thousand and 52.6 million of cash held for covenants (CP-1 handoff). The overall behaviour reading is Neutral or Mixed on documented actions, evidence quality High. No score is stated.

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| 2017-07-20 and 2017-07-25 | Common stock listed on the NYSE; IPO closed; Management Agreement dated 2017-07-25 | Documentary Fact | 10-K page:115, page:169 |
| 2020-05-28 | 225.0 million of 11% Series B preferred stock issued | Documentary Fact | 10-K page:50 |
| 2021-06-14 | 201.3 million of 6.25% Series C issued and all Series B redeemed | Documentary Fact | 10-K page:50 |
| 2022-02-16 and 2022-02-22 | TRTX 2022-FL5 CLO issued; secured revolving credit facility of 250.0 million closed | Documentary Fact | 10-Q Q3 page:43, page:52 |
| FY2023 | Net loss of 116,630 thousand with credit loss expense of 189,912 thousand and 241,868 thousand of loans converted to real estate owned | Documentary Fact | 10-K page:178-179, page:181 |
| FY2024 | 89,499 thousand of loans converted to real estate owned; reinvestment period of the 2022 CLO had ended on 2024-02-09 | Documentary Fact | 10-K page:181; 10-Q Q3 page:43 |
| 2025-03-28 | TRTX 2025-FL6 issued; secured revolver extended three years and upsized to 375.0 million in Q1 2025 | Documentary Fact | 10-Q Q3 page:43, page:52 |
| 2025-09-04 | 25.0 million share repurchase program announced | Documentary Fact | 10-Q Q2 page:132 |
| 2025-11-17 | TRTX 2025-FL7 issued; HSBC asset-specific facility closed | Documentary Fact | 10-Q Q3 page:43, page:53 |
| 2026-02-17 | FY2025 10-K signed | Documentary Fact | 10-K page:173 |
| 2026-05 | Term Loan B and Revolver closed; Wells Fargo agreement upsized; TRTX 2022-FL5 redeemed on 2026-05-15 | Documentary Fact | 10-Q Q3 page:43, page:48, page:55-57 |
| 2026-06-30 | New Citi secured credit agreement; Goldman Sachs upsize | Documentary Fact | 10-Q Q3 page:48 |
| 2026-09-01 | Plano multifamily property acquired through non-judicial foreclosure; 13.0 million realized loss | Documentary Fact | 10-Q Q3 page:39 |
| 2026-09-24 | 212.0 million San Francisco office loan originated | Documentary Fact | 10-Q Q3 page:116 |
| 2026-10-02 (subsequent event) | TRTX 2026-FL8 closed | Documentary Fact | 10-Q Q3 page:74 |
| 2026-10-26 (subsequent event) | New 50.0 million repurchase program; Q3 10-Q signed | Documentary Fact | 10-Q Q3 page:74, page:136 |

### Source conflicts and consistency checks

No true conflict between sources was found on a transaction size, a date or a party. Three differences in statements are logged, with the quoted spans, and are not reconciled.

| Entry | Span A | Span B | Effect |
| --- | --- | --- | --- |
| Office exposure | "Currently, our total office loan exposure has been reduced to less than 5%" (release 2026-04-28 page:2) | "Office 407,360 71,143 7.9" in the property-type table at 2026-09-30 (10-Q Q3 page:72) | The statements are dated differently; the later filed table shows a higher office share. Logged, not reconciled; the filed table controls for 2026-09-30 |
| Leverage expectation | "We currently expect that our leverage, measured as the ratio of total debt to equity, will generally be less than 3.75:1" (10-K page:15) | "Total leverage ratio(2) 4.03x 3.02x" (10-Q Q3 page:104) | Different dates and an unstated basis for the expectation. The printed debt-to-equity ratio of 3.64x is below 3.75:1 and the total leverage ratio of 4.03x is above it. Logged, not reconciled |
| Series B preferred stock | "redeemed all of our outstanding shares of Series B Preferred Stock" (10-K page:50) | "issuance of Series B Preferred Stock treated as temporary equity" in the capitalization narrative (10-Q Q3 page:104) | The balance sheet shows no Series B (10-Q Q3 page:7); the 10-Q sentence is historical capitalization wording. No effect on figures |

Consistency with the earlier handoffs: this handoff agrees with the CP-0 source map and with the CP-1 funding stack, and does not change any CP-1 figure. It adds the 10-K leverage expectation, which CP-1 did not mention, and the manager fee and affiliate arrangements.

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter or limit |
| --- | --- | --- | --- | --- |
| Revenue durability | 99.7% floating-rate loans, weighted floor 2.62%, 59.5% with prepayment protection (10-Q Q3 page:31-32, page:120) | Floors and index matching hold income if rates fall, but income falls with rates below the floor and depends on repayments being redeployed | Net interest income is steady to rates in a narrow range but depends on origination pace; a slowdown in repayments or originations reduces earnings | Net income already fell in Q3 2026 (CP-1 handoff) |
| Margin and cash-flow risk | Term Loan B at Term SOFR plus 2.75% against CLO funding at 1.75% weighted spread and secured credit agreements at 1.61% | Corporate debt costs more than asset-level funding; leverage including it is 4.03x | Funding cost mix worsens as corporate debt is added, thinning spread and increasing fixed corporate claims | Corporate debt is non-marked and long-dated, reducing liquidity risk |
| Concentration | Multifamily 52.6%, industrial 22.6%, office 7.9%; top five loans 22.6% of commitments; West 34.9% | Transitional assets depend on sponsor business plans; one loan default could move reserves | Moderate diversification; office share rose in Q3 2026 after falling in Q2 2026 | Weighted average risk rating 3.0, no non-accrual (10-Q Q3 page:34, page:37) |
| Sponsor alignment | Base fee on Equity, no incentive fee earned, TPG affiliate fees disclosed; three of eight directors from TPG (10-K page:64) | Fee income for the Manager does not fall with credit losses, and the Manager may favour growth in Equity | Alignment with creditors is indirect; no TPG support obligation is documented | Related-party payments beyond the management fee are small (Calculations) |
| Key uncertainties | 1.0 billion CLO closed 2026-10-02 with undisclosed use of proceeds; covenant test values not disclosed; leverage above the 10-K expectation on one measure | Post-quarter funding may change recourse and liquidity materially | Monitoring posture: watch Q4 2026 filings for CLO effects, repurchases and covenant disclosure | Logged conflict on leverage expectation above |

### Consumer assessment

| Consumer | Readiness | Take from this handoff | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-1 | Ready; this handoff is consistent with the financial base | Business context, recourse layers and event dates | Keeps ratios tied to the lender model | None new | None |
| CP-2 | Ready with limitations | Manager and fee structure, leverage expectation, timeline, subsequent events, conflicts log | Synthesis needs governance and refinancing context and must carry the unresolved leverage basis | Executed agreements, shareholder percentages and CLO use of proceeds not supplied | Carry as restrictions; do not infer sponsor support |
| CP-5 | Ready with limitations | Locators for every row, the conflicts log and the Management Language tags | Evidence trace needs located claims | Extraction fidelity not reviewed; 8-K of 2026-10-06 not in pack | Trace to the `page:N` locators; label management claims |

## Calculations

Derived values only; reported figures are quoted with locators above. USD thousands unless stated.

| Item | Inputs and locator | Result |
| --- | --- | --- |
| Five largest loans | 285.0 + 256.3 + 222.6 + 212.0 + 194.5 million (10-Q Q3 page:115-116) | 1,170.4 million; 1,170.4 / 5,168.7 = 22.6% of commitments; largest loan 285.0 / 5,168.7 = 5.5% |
| Property type shares sum | 52.6 + 22.6 + 7.9 + 7.6 + 6.5 + 1.5 + 1.3 (page:72) | 100.0%, equal to printed |
| Geography shares sum | 34.9 + 23.4 + 19.2 + 15.8 + 6.7 (page:72) | 100.0%, equal to printed |
| Shares retired 9M 2026 | 556,592 + 1,301,644 + 1,163,018 (page:8-9) | 3,021,254 shares; cash paid 24,613 (page:10) |
| Common share count roll | 78,318,722 + issued (39,079 + 485,625 + 4,782) - retired 3,021,254 | 75,826,954, equal to printed (page:8-9) |
| Series C liquidation preference per share | 201,250 thousand / 8,050,000 shares (page:7) | 25.00 per share; 6.25% of 25.00 divided by four is 0.3906, equal to the quarterly dividend printed in release 2026-10-26 page:2 |
| Fee base implied by the Q3 2026 management fee | 5,326 / 0.375% (page:62-63) | About 1,420,267 of fee base, against stockholders' equity of 1,024,126; the Equity definition in the Management Agreement is not supplied, so the difference cannot be explained |
| Fee at 1.5% of GAAP equity | 1,024,126 x 0.375% | About 3,840 per quarter against 5,326 incurred |
| Related-party payments beyond the management fee, 9M 2026 | 1.1 + 0.4 + 0.9 million (page:63-65) | 2.4 million, about 15% of the 15,983 thousand management fee; amounts are rounded in the filing |
| Indicative termination fee | 3 x 21,257 where 21,257 = FY2025 management fee 20,858 + 9M 2026 15,983 - 9M 2025 15,584 (10-K page:232; page:63) | About 63,771; indicative only because the contractual 24-month average and any incentive fees are not computed from the pack; no incentive fee was earned in the periods shown |
| Placed share of stated CLO size | 962.5 / 1,100.0 (FL6); 957.0 / 1,100.0 (FL7); 820.0 / 1,000.0 (FL8) (page:43, page:74) | 87.5%; 87.0%; 82.0%. The basis of the 1.0 billion for FL8 is not defined, so the comparison is indicative |
| Rate sensitivity as share of LTM net interest income | 2,921 / 101,510 (page:120; CP-1 handoff) | 2.9% per 25 basis point rise |
| Leverage versus the 10-K expectation | Printed debt-to-equity 3.64x and total leverage 4.03x against 3.75:1 (page:104) | 3.64x below and 4.03x above the expectation |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Shareholder ownership percentages, including any TPG holding, not supplied (Part III by reference) | Medium | CP-2 | Obtain the proxy statement |
| Management Agreement and definitions of Equity and Core Earnings not supplied; the fee base cannot be reconciled to GAAP equity | Medium | CP-2 | Obtain the agreement |
| Executed Term Loan B, Revolver and secured credit agreement documents and guarantor list not supplied | High for legal terms | CP-2 | Obtain the 2026-05-14 Credit Agreement and others |
| Use of proceeds and retained interests for TRTX 2026-FL8 not supplied; the 8-K of 2026-10-06 is not in the pack | Medium | CP-1A, CP-2 | Obtain the 8-K and offering terms |
| Basis of the 10-K leverage expectation of 3.75:1 not stated for the post-Term Loan B structure | Medium | CP-2 | Confirm in the Q4 2026 10-K |
| No sponsor support commitment, equity cure or keepwell documented | Medium | CP-2 | Treat as Not supplied; do not infer |
| No events after 2026-10-26 supplied up to 2026-11-05 | Medium | CP-1A, CP-2 | Treat as Not supplied |
| No prior ownership or recapitalisation history beyond the 2017 listing in the pack | Low | CP-1A | Not needed for this module |
| Quarterly presentations referred to by the releases not supplied | Low | CP-5 | Supply if slide claims are needed |

## Next module

- CP-2: use the lender model, recourse layering and funding mix from the financial base; carry the manager fee structure, the leverage expectation versus the 4.03x ratio, the 2028 refinancing cluster, the October 2026 CLO and the logged conflicts as stated; do not infer sponsor support or ownership percentages; keep Management Language labelled.
- CP-5: trace each row to its `page:N` locator; the derived shares, fee base and sensitivity percentages appear only in Calculations; label the three logged differences as differences, not errors.
