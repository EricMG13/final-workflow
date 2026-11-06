## Request

Issuer: DYCOM INDUSTRIES INC (ticker DY; Dycom Industries, Inc., SEC file number 001-10613). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency per the context: USD. The context names no sponsor, parent, borrower or guarantor list and supplies no ratings, quotes or deal terms; those are treated as not supplied.

Task: build the business and transaction fact pack a committee reads first: which transaction, business, ownership and operating facts matter most to the creditor. Required decision drivers: transaction and ownership structure; business and operating model; credit-relevant history or change. Each fact row carries one of four categories: Documentary Fact (the cited source states it), Management Language (management's characterization, attributed, never adopted), Analyst Interpretation (my reading of cited evidence) and Insufficient Information (evidence missing, with the missing datapoint and why it matters). No information outside the pinned sources is used. Where this handoff gives a financial figure it is the figure in the CP-1 financial base, and a figure that is only in a source is cited to the source. No peer ranking, instrument recommendation or recovery conclusion is made. Periods follow Dycom's fiscal labels: FY2026 is the 53 weeks ended January 31, 2026 and Q2 2027 is the quarter ended August 1, 2026.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Use in this handoff |
| --- | --- | --- |
| 10-K_2026-01-31_dy-20260131.htm.jsonl | d3cce30e8b33b40ee726fca361a4ac5af2d47cfff9b57a3f36d911b5b73b8e31 | Business description (Item 1), customers, backlog, acquisitions, equity and debt history, exhibits |
| 10-Q_2025-10-25_dy-20251025.htm.jsonl | 629b328324cc0ef5393e62b61d8db6e3a1e48e205e2a0f26575592aea3390dd7 | Power Solutions agreement and debt commitment letter of November 18, 2025 |
| 10-Q_2026-05-02_dy-20260502.htm.jsonl | 237d7d80121afc72a5bb1b73d79141b69d6396b9608af9b8f3dec2db64be0f4f | National Technology Integrators agreement of May 22, 2026 |
| 10-Q_2026-08-01_dy-20260801.htm.jsonl | 666dcd463f60ce7cc9d18464ad1e3020b3cf1f9ca79b66ed79bb20b35e9cbf79 | Latest business, customer, acquisition, capital stock and subsequent-event facts |
| EX-99.2_2026-03-04_q42026presentationmateri.htm.jsonl | 6988c6bbc189fb06cb090ad132fb7c67f67f6d428cb3b75cae839c0b2d040376 | Management narrative and outlook, Q4 2026 (Management Language) |
| EX-99.2_2026-05-27_q12027presentationmateri.htm.jsonl | fb3e1da73422f05d34562fe3208f0c4af7eb6fffd05db64f60aea98effba2a9e | Management narrative on National Technology Integrators and outlook, Q1 2027 (Management Language) |
| EX-99.2_2026-08-26_q22027presentationmateri.htm.jsonl | db5426dcb5222e08c260f53364ad7255c795bb75eba46ab3566a5906d530e4b2 | Management narrative and updated outlook, Q2 2027 (Management Language) |

### Run context (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (67215-dycom-industries-inc-dy.json) | c91849e9583c2227ff5d8a95aa89da364bfff0f885232cdd128e95fb51281f42 |

### Handoffs relied on

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 718647fe146a481414f4709c9a5b01ad4b5d904e03712717acf9f85199936a95 | Source readiness, authority ranking and logged conflicts |
| CP-1 | 2e646964e839fbbfdb014df8aa772f6b2ce96e116e3987210169134e31b290b6 | Financial base: debt, liquidity, leverage, segments, non-debt claims |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Dycom is a US specialty contractor to telecom, utility and data-center customers, now combining fiber construction with an acquired Building Systems segment. Revenue visibility is good, but customer concentration is high. | Medium | Ownership, board and restricted-payment capacity evidence is not in the pack, and acquisition documents are available only as filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| AT&T, Verizon and Lumen supplied 25.4%, 14.0% and 10.8% of fiscal 2026 revenue, and customers may terminate for convenience without volume commitments. | Backlog of 12,242 million gives visibility, but it depends on a few counterparties' capital spending decisions. | High |
| The Power Solutions acquisition at a 1.95 billion purchase price created the Building Systems segment, paid 15% in shares and the balance in cash raised through new term loan debt. | Leverage rose on the transaction, and deleveraging depends on acquired earnings and on limiting discretionary buybacks. | Medium |
| Building Systems contributed 397.5 million of revenue in Q2 2027, and National Technology Integrators was acquired on July 2, 2026 with a preliminary purchase price allocation. | Mix shifts toward data-center electrical work on fixed-price contracts, adding execution and integration risk to the earnings base. | Medium |
| Buybacks continue beside acquisitions: 36.0 million in Q1 2027 and a new 150.0 million authorization on August 26, 2026. No dividends are paid. | Shareholder returns compete with deleveraging, and the restricted-payment baskets that would limit them cannot be tested. | Medium |

### Business and transaction view

The business view is clear and well documented; the ownership and governance view is thin. Dycom is a publicly listed contractor, and the pack contains no ownership table or proxy, so control rights, major holders and economic interests are Insufficient Information rather than adverse. What the filings do show is a business whose cash flows come from multi-year master service agreements with a small set of telecom carriers (AT&T, Verizon including Frontier, Lumen), for which customers specify tasks and prices, are generally not committed to volumes and can terminate for convenience (10-K page:9). Evidence to mechanism to implication: the master-service model gives recurring, maintenance-heavy revenue (94.0% of Q2 2027 revenue came from multi-year master service agreements and other long-term contracts, 10-Q Q2 FY27 page:34), which supports revenue durability, but the lack of volume commitments and the concentration mean that a change in one carrier's capital budget, or the AT&T acquisition of Lumen's mass-markets fiber business that closed on February 2, 2026, moves Dycom's revenue and working capital directly. Seasonality, receivable build and unbilled work (1,334,390 thousand of unbilled receivables out of 2,281,043 thousand of gross receivables at August 1, 2026, 10-Q Q2 FY27 page:12) mean cash conversion lags growth, which links to the liquidity and supplier-finance points in the CP-1 financial base.

The transaction view is that FY2026 and FY2027 history is dominated by two acquisitions in a new segment. Power Solutions (agreed November 18, 2025, closed December 23, 2025) was priced at 1.95 billion on a cash-free, debt-free basis and was funded by roughly 85% cash and 15% Dycom shares at signing, with the cash raised through an enlarged Term Loan A, a short-term bridge facility and then a Term Loan B that refinanced the bridge on January 27, 2026 (10-Q Q3 FY26 page:25; 10-K page:99, page:112). National Technology Integrators (agreed May 22, 2026, closed July 2, 2026) added a low-voltage engineering business for a stated price of 275.0 million (10-Q Q1 FY27 page:26; 10-Q Q2 FY27 page:35). The mechanism is that debt-funded growth in a segment with fixed-price and modified fixed-price contracts changes the risk profile from carrier-capex cycle toward project execution, and brings preliminary purchase accounting (goodwill and intangibles now exceed total equity per the CP-1 financial base). The creditor implication is that the earnings base that supports the new leverage was assembled in under a year, is only partly in the trailing figures, and is not yet verified by a full year of combined results. Governance behaviour on the documented evidence is Neutral or Mixed: acquisitions were partly paid in stock, no dividends are paid and no related-party or priming action appears in the pack, but buybacks continued after the leveraging event and a new authorization followed on August 26, 2026. Legal capacity to make distributions cannot be assessed because the credit agreement and indenture are not supplied.

### Company and operating model

| Area | Fact | Category | Source and limitation |
| --- | --- | --- | --- |
| Core activities | Specialty contracting for digital infrastructure, telecommunications and utilities: program management, engineering and design, aerial, underground and wireless construction, maintenance, fulfillment and underground facility locating; electrical, energy management, security and fire safety systems for data centers and other critical facilities | Documentary Fact | 10-K page:4-6; 10-Q Q2 FY27 page:5 |
| Segments | Communications (aggregated operating segments) and Building Systems (added in the fourth quarter of FY2026 after Power Solutions); Building Systems revenue was 397.5 million of 2,005.9 million consolidated revenue in Q2 2027 | Documentary Fact | 10-K page:5-6; 10-Q Q2 FY27 page:26-27 |
| End markets and customers | Telephone companies, cable operators, wireless carriers, equipment providers, electric and gas utilities, and general contractors building data centers | Documentary Fact | 10-K page:8 |
| Customer concentration | AT&T 25.4%, Verizon 14.0% and Lumen 10.8% of FY2026 revenue; in Q2 2027 AT&T 20.1%, Verizon 10.4% and Lumen 5.3% | Documentary Fact | 10-K page:9; 10-Q Q2 FY27 page:25. Attribution is affected by Verizon's acquisition of Frontier (January 20, 2026, restated retrospectively) and AT&T's acquisition of Lumen's mass-markets fiber business (February 2, 2026, not restated for FY2026) |
| Geography | United States only; all 50 states, hundreds of field offices, 38 operating companies | Documentary Fact | 10-K page:4; 10-Q Q2 FY27 page:25 |
| Revenue model and pricing | Master service agreements and other contracts with discrete pricing for individual tasks; remainder project contracts; Building Systems on fixed-price and modified-fixed-price firm orders; customer retainage of 5% to 10% | Documentary Fact | 10-K page:9, page:11 |
| Contract protection | Customers may terminate for convenience in most cases; customers are generally not committed to specific volumes; all backlog contracts may be cancelled | Documentary Fact | 10-K page:9, page:11 |
| Volume drivers | Fiber-to-the-home programs, rural fiber programs, long-haul and middle-mile fiber, wireless modernization, data-center electrical and fiber demand, state and federal program spending | Management Language | 10-Q Q2 FY27 page:33; Q2 deck page:4. Management's expectation of demand, not independently verified |
| Backlog | 12,242 million total at August 1, 2026 (Communications 10,983, Building Systems 1,259), 6,472 million in the next twelve months; 9,542 million total at January 31, 2026 | Documentary Fact | 10-Q Q2 FY27 page:54-55. Estimate, not GAAP, cancellable, methodology may not be comparable |
| Growth | Q2 2027 revenue up 45.6% on Q2 2026, organic growth 16.7%; six-month organic growth 20.5% | Documentary Fact (revenue) and Management Language (organic measure) | 10-Q Q2 FY27 page:45; Q2 deck page:7. Organic growth is a non-GAAP deck measure |
| Cost structure | Costs of earned revenues are the largest cost line, general and administrative and depreciation and amortization follow; Dycom relies on subcontractors for a significant amount of work, and customers provide most materials for the majority of contracts | Documentary Fact | CP-1 statements; 10-K page:13, page:99. Subcontractor spend is not quantified |
| Capital spending | Fleet-heavy: vehicles are the largest property and equipment class; capital expenditures net of asset sale proceeds are in the CP-1 base | Documentary Fact | 10-Q Q2 FY27 page:14; CP-1. Maintenance versus growth capex split not supplied |
| Working capital | Days sales outstanding 101 at August 1, 2026 versus 108 a year earlier; receivables build absorbed cash in the six months to August 1, 2026; supplier finance program included in accounts payable | Documentary Fact | 10-Q Q2 FY27 page:29, page:49; CP-1 |
| Seasonality | Outdoor Communications work is weakest in fiscal quarters ending January and April | Documentary Fact | 10-K page:10 |
| Competition | Highly fragmented, few barriers to entry, some customers perform the work themselves | Documentary Fact | 10-K page:12 |
| Insurance retention | Retains risk of loss up to 1.0 million per occurrence for workers' compensation and 2.0 million per occurrence for the first 5.0 million of automobile and general liability coverage, with exposure also for losses between 5.0 and 10.0 million | Documentary Fact | 10-Q Q2 FY27 page:16 |
| Management outlook | Fiscal 2027 revenue outlook was 6.85 to 7.15 billion in March 2026, 7.38 to 7.65 billion in May 2026 and 7.48 to 7.66 billion in August 2026, with about 150 million of Communications wireless revenue deferred into fiscal 2028 | Management Language | Q4 deck page:5; Q1 deck page:6; Q2 deck page:5. Forward-looking; not actuals |

### Company profile

| Attribute | Value | Category | Source and limitation |
| --- | --- | --- | --- |
| Legal name and form | Dycom Industries, Inc., a Florida corporation incorporated in 1969 | Documentary Fact | 10-K page:1, page:4 |
| Listing | Common stock listed on the New York Stock Exchange under DY; large accelerated filer | Documentary Fact | 10-Q Q2 FY27 page:1 |
| Headquarters | West Palm Beach, Florida | Documentary Fact | 10-K page:1 |
| Sector and country | Water, sewer, pipeline, communications and power line construction (context sector); United States | Documentary Fact (country) and context input (sector, not issuer evidence) | 10-K page:4; run context |
| Employees | About 19,556 at January 31, 2026 | Documentary Fact | 10-K page:12 |
| Shares outstanding | 30,160,957 at August 24, 2026 | Documentary Fact | 10-Q Q2 FY27 page:1 |
| Fiscal year | Ends the last Saturday in January; FY2026 had 53 weeks, FY2027 has 52 | Documentary Fact | 10-K page:8 |
| Auditor | PricewaterhouseCoopers LLP, unqualified opinion on statements and internal control for FY2026 | Documentary Fact | 10-K page:127, page:139 (consent exhibit) |
| Ownership and control | Not supplied: beneficial ownership is incorporated by reference to a proxy statement that is not in the pack | Insufficient Information | 10-K page:134. Missing datapoint: holders above five percent and insider holdings; matters for control and for dividend or buyback influence |
| Sponsor or parent | None named in the context or sources | Insufficient Information | Run context. Not treated as absent control |
| Credit ratings | Not supplied: no rating appears in the context or in the sources searched | Insufficient Information | Run context; 10-K search. Matters for market access and pricing grids |
| Dividend policy | No cash dividends paid; intends to retain earnings for acquisitions and buybacks | Documentary Fact | 10-Q Q2 FY27 page:47 |
| Guarantors | Substantially all domestic subsidiaries guarantee the credit agreement and the 2029 notes; named list not supplied | Documentary Fact with Insufficient Information on names | 10-Q Q2 FY27 page:20-21 |

### Transaction summary and new debt issues

Power Solutions, LLC (Maryland, electrical infrastructure for data centers and other critical facilities, Greater Washington D.C., Maryland and Virginia area) was acquired under a Unit Purchase Agreement dated November 18, 2025 with Project Eastern Shore, LLC as seller. The preliminary purchase price was 1.95 billion on a cash-free, debt-free basis, payable as a mix of Dycom common stock (1,011,069 shares, 15% of the preliminary price, 292.5 million at signing) and cash, with a purchase price adjustment escrow, a termination right and an outside date of May 18, 2026 (10-Q Q3 FY26 page:25). The deal closed on December 23, 2025: cash of 1,644.9 million (1,628.6 million net of cash acquired), shares valued at 351.0 million at closing and assumed seller debt of 64.8 million, with total consideration of 1,995.9 million in the 10-K (the cash and share amounts together) and 2,008.7 million in the latest 10-Q after a 12.8 million working capital adjustment recorded in Q1 2027; the assumed seller debt is listed separately from total consideration (10-K page:99; 10-Q Q2 FY27 page:35). Status: completed, with the allocation of the purchase price still preliminary in the 10-Q.

Financing: on signing, Dycom obtained a debt commitment letter from Bank of America, N.A., BofA Securities, Inc. and Goldman Sachs Bank USA for a 1,000 million senior secured Term Loan A, a 700 million 364-day bridge facility and a 445 million Term Loan A backstop to refinance existing debt (10-Q Q3 FY26 page:25). The executed structure on December 23, 2025 differed: a 600.0 million 364-day secured bridge, Term Loan A increased from 440.0 million to 1,540.0 million, revolver commitments increased from 650.0 million to 800.0 million and maturities extended to December 23, 2030. On January 27, 2026 a First Amendment established an 800 million senior secured Term Loan B, due January 27, 2033, whose proceeds refinanced the bridge, paid fees and funded cash to the balance sheet (10-K page:112). The 4.50% senior notes due 2029 (500.0 million) were not touched. Effect on liquidity and leverage is in the CP-1 financial base: debt of 2,840.0 million at January 31, 2026 against 950.0 million a year earlier, cash of 709.2 million at January 31, 2026, and revolver availability of 746.4 million. Debt issuance costs of 33,870 thousand were paid and a loss on debt extinguishment of 7,268 thousand was recorded in FY2026 (10-K page:83, page:85).

National Technology Integrators, LLC (Maryland, low-voltage engineering and construction, in Building Systems) was agreed on May 22, 2026 for a stated total of 275.0 million, closed on July 2, 2026 for total consideration of 271.4 million (cash 226.4 million, 225.4 million net of cash acquired, plus 95,550 shares valued at 45.0 million), with seller debt of 12.3 million assumed in addition, on a preliminary allocation; it was paid in cash and shares, and no borrowings under the Credit Agreement appear in the six months to August 1, 2026 (10-Q Q1 FY27 page:26; 10-Q Q2 FY27 page:4, page:10, page:23, page:35). Management characterizes it as about 175 million of annual revenue run-rate with mid-to-high-teens Adjusted EBITDA margins (Q1 deck page:5); that is Management Language and an unaudited statement.

No new debt issue occurred after August 1, 2026 in the pack, and nothing dated after the cutoff is used. Subsequent event: on August 26, 2026 the Board authorized a new 150.0 million share repurchase program through February 2028, replacing the remaining 83.9 million of the prior authorization (10-Q Q2 FY27 page:30). Prior history: on April 1, 2021 Dycom issued the 4.50% senior notes due 2029; in FY2025 it made three smaller acquisitions of telecommunications contractors (a cash price of 16.0, 24.5 and 150.7 million, 10-K page:99); and the credit agreement was amended and restated in prior years, the latest earlier version dated May 15, 2024 (10-K page:139). The executed Credit Agreement, First Amendment, indenture and both purchase agreements are not in the pack; the terms above are filing summaries (Documentary Fact as described by the issuer, not verified against the executed text).

### Timeline

| Date | Event | Category | Source |
| --- | --- | --- | --- |
| 1969 | Incorporated in Florida | Documentary Fact | 10-K page:4 |
| April 1, 2021 | 500.0 million 4.50% senior notes due 2029 issued | Documentary Fact | 10-Q Q2 FY27 page:21 |
| May 15, 2024 | Prior amended and restated credit agreement dated | Documentary Fact | 10-K page:139 |
| November 2024 | Chief executive officer succession plan and transition completed, per management's non-GAAP footnote | Management Language | Q4 deck page:6 |
| FY2025 | Three telecommunications contractor acquisitions | Documentary Fact | 10-K page:99 |
| February 26, 2025 | Board authorized 150 million share repurchase program through August 25, 2026 | Documentary Fact | 10-Q Q2 FY27 page:22 |
| November 18, 2025 | Power Solutions agreement and debt commitment letter | Documentary Fact | 10-Q Q3 FY26 page:25 |
| December 23, 2025 | Power Solutions closed; credit agreement amended and restated; 600.0 million bridge | Documentary Fact | 10-K page:99, page:112 |
| January 20, 2026 | Verizon completed acquisition of Frontier | Documentary Fact | 10-K page:9 |
| January 27, 2026 | First Amendment and 800 million Term Loan B | Documentary Fact | 10-K page:112 |
| February 2, 2026 | AT&T completed acquisition of Lumen's mass-markets fiber business (subsequent to FY2026, a subsequent event for the 10-K) | Documentary Fact | 10-K page:9 |
| March 9, 2026 | Form 10-K for FY2026 filed | Documentary Fact | 10-Q Q2 FY27 page:6 |
| May 22, 2026 | National Technology Integrators agreement | Documentary Fact | 10-Q Q1 FY27 page:26 |
| July 2, 2026 | National Technology Integrators closed | Documentary Fact | 10-Q Q2 FY27 page:23 |
| August 26, 2026 | New 150.0 million repurchase authorization (subsequent event to Q2 2027) | Documentary Fact | 10-Q Q2 FY27 page:30 |

### Governance, capital allocation and disclosure

| Item | Evidence | Category | Mechanic and limitation |
| --- | --- | --- | --- |
| Issuer-level behavior category | Neutral or Mixed: equity used for part of acquisition consideration (1,011,069 shares at Power Solutions, 95,550 at National Technology Integrators) and no dividend, but buybacks resumed after the leveraging acquisition | Analyst Interpretation | Equity consideration limits cash leakage; buybacks of 36.0 million in Q1 2027 and a new 150.0 million authorization compete with deleveraging. Based on documented actions only, not on ownership identity |
| Creditor-adverse actions | None found in the pack (no priming, uptiering, drop-down, non-pro-rata exchange or collateral release described) | Insufficient Information | The credit agreement and indenture are not supplied, so absence of disclosure is not absence of capacity |
| Legal capacity | Restricted-payment, debt and lien covenants exist under the indenture and credit agreement, subject to exceptions | Documentary Fact | 10-Q Q2 FY27 page:21; baskets and amounts not supplied. Capacity to fund buybacks or acquisitions with debt cannot be sized |
| Willingness | Repurchases of 200,000 shares in FY2026 and 100,000 in Q1 2027; new authorization; stated priority of organic growth, then M&A, then buybacks | Documentary Fact and Management Language | 10-K page:119; 10-Q Q2 FY27 page:22; Q2 deck page:4 (capital allocation statement) |
| Feasibility | Liquidity and leverage per the CP-1 base: 1,086.5 million liquidity, constructed net leverage 2.61x at August 1, 2026 | Documentary Fact (inputs) and Analyst Interpretation | Not a covenant ratio; see CP-1 |
| Disclosure quality | Audited statements with unqualified opinions; disclosure controls effective at August 1, 2026; internal-control assessment excludes National Technology Integrators in its first year; ERP implementation in phases | Documentary Fact | 10-K page:127; 10-Q Q2 FY27 page:56-57. Evidence quality High (primary, dated, issuer-specific) |
| Related-party and sponsor leakage | None found in the sources searched | Insufficient Information | Related-party disclosures are in a proxy that is not in the pack |

### Logged conflicts

| Item | Span A | Span B | Status |
| --- | --- | --- | --- |
| Value of the 1,011,069 Power Solutions shares | "the value of which was equal to $292,500,000" at signing (10-Q Q3 FY26 page:25) | "valued at $351.0 million" at closing (10-K page:99) | Logged, not reconciled. A different measurement date is likely but not stated |
| Total consideration for Power Solutions | "Total consideration was $1,995.9 million" (10-K page:99) | "Total consideration was $2,008.7 million" after a 12.8 million working capital adjustment recorded in Q1 2027 (10-Q Q2 FY27 page:35) | Logged. The filings explain the later figure by the adjustment; the 10-Q is the later source |
| Debt commitment structure versus executed structure | Bridge 700 million, Term Loan A 1,000 million, backstop 445 million (10-Q Q3 FY26 page:25) | Bridge 600.0 million, Term Loan A 1,540.0 million, no backstop mentioned (10-K page:112) | Logged. Different documents at different stages; the executed amounts are from the later filing |
| Cash paid for National Technology Integrators net of cash acquired | 225.4 million (10-Q Q2 FY27 page:10) | 225.5 million (Q2 deck page:4) | Logged from CP-0; the filing controls |
| Extra-week revenue in the Q4 2026 organic growth reconciliation | 97.3 million for the quarter (Q4 deck page:7) | 90.8 million for the year (Q4 deck page:7) | Carried from CP-0; unresolved |

### Corrections to earlier handoffs

CP-1 described the National Technology Integrators total consideration of 271.4 million with assumed seller debt of 12.3 million listed in the same parenthesis as the cash and shares, which can be read as part of the total. The filing's total consideration is the cash and share amounts only (226.4 million plus 45.0 million); the assumed debt is additional and is not part of the total. The same holds for Power Solutions, where the total consideration is cash plus shares and the 64.8 million of assumed debt is separate. The CP-1 debt and liquidity figures are not affected. CP-0 and CP-1 otherwise stand.

### Credit translations

1. Revenue durability. Evidence: 94.0% of Q2 2027 revenue from multi-year master service agreements and other long-term contracts, with backlog of 12,242 million (10-Q Q2 FY27 page:34, page:55); counter-evidence: customers are not committed to volumes and can terminate for convenience (10-K page:9, page:11). Mechanic: recurring maintenance and program work supports base revenue, but optional volumes make realized revenue track customer capital budgets. Implication: revenue is more durable than a project contractor's but not contractually floored; backlog is an indicator, not a commitment.
2. Concentration. Evidence: AT&T, Verizon and Lumen at 25.4%, 14.0% and 10.8% of FY2026 revenue (10-K page:9), and a receivable-plus-contract-asset concentration in four customers (10-Q Q2 FY27 page:13). Mechanic: customer mergers (Verizon with Frontier, AT&T with Lumen's fiber business) reshuffle the customer set and change who controls build budgets and payment timing. Implication: cash collection and revenue timing depend on a few counterparties; a delay by one carrier shows up in days sales outstanding and liquidity.
3. Margin and cash-flow risk. Evidence: Communications margins are seasonal and depend on operating leverage (10-K page:10; 10-Q Q2 FY27 page:46); Building Systems margin is higher in the latest quarter (CP-1 segments) but is on fixed-price work with preliminary accounting (10-K page:11; 10-Q Q2 FY27 page:10). Mechanic: fixed-price contracts transfer cost overruns to Dycom, and receivable growth absorbs cash. Implication: margin and free cash flow can diverge from Adjusted EBITDA, which the CP-1 base shows through the six-month free cash flow figure.
4. Transaction leverage. Evidence: debt of 2,840.0 million at January 31, 2026 against 950.0 million a year earlier (CP-1). Mechanic: acquisition debt came before a full year of acquired earnings. Implication: constructed leverage is sensitive to pro forma earnings that are not supplied, and to buybacks that compete with repayment.
5. Sponsor alignment. Evidence: public company, no sponsor in the context, ownership not in the pack. Mechanic: no controlling-holder incentives can be identified or excluded. Implication: neutral on sponsor risk with an explicit information gap.
6. Key uncertainties: the executed documents, restricted-payment capacity, pro forma EBITDA, supplier finance terms and the covenant ratios. Counter-evidence logged above does not alter these; it concerns purchase accounting values.

### Monitoring inputs missing from the source set

| Item | Status | Severity |
| --- | --- | --- |
| Debt schedule | Partial: principal and carrying values are in the 10-Q; scheduled amortization after FY2027 is not printed | Medium |
| Maturity schedule | Partial: maturity dates are printed; annual amortization is not | Medium |
| Covenant compliance certificate | Not supplied: only "in compliance" is stated | High |
| Add-back bridge | Present for Adjusted EBITDA (management reconciliation); not present for covenant EBITDA | Medium |
| Pro forma EBITDA for acquired businesses | Not supplied | High |

### Consumers

| Consumer | Readiness | What to take from this handoff | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Business-risk rows, concentration, transaction and capital allocation facts and the credit translations | Business risk is one of the two drivers of the fundamental view | Ownership, restricted-payment capacity and pro forma earnings are missing; cite the Insufficient Information rows and do not infer from them |
| CP-5 evidence trace validation | READY_WITH_LIMITATIONS | Located quotes, the logged conflicts and the category tags | The validator needs one story across modules | Management Language rows must not be re-stated as fact; the conflict list should be traced to the filing as controlling source |

## Calculations

No new financial figure is derived in this handoff beyond simple restatement of source figures. The following are checks of source figures, shown with inputs:

- Power Solutions funding mix: stock consideration 292.5 million is stated by the 10-Q as 15% of the 1,950.0 million preliminary price (10-Q Q3 FY26 page:25); cash 1,657.5 million before the purchase price adjustment escrow is stated in the same passage. The 15% is the filing's statement, not a calculation here.
- Power Solutions consideration: cash 1,644.9 plus shares 351.0 equals 1,995.9, the 10-K total consideration (10-K page:99); adding the 12.8 working capital adjustment gives 2,008.7, the 10-Q total (10-Q Q2 FY27 page:35). The assumed seller debt of 64.8 is outside total consideration. National Technology Integrators: cash 226.4 plus shares 45.0 equals 271.4; assumed seller debt of 12.3 is outside the total (10-Q Q2 FY27 page:35).
- Combined top-three customer share of FY2026 revenue: 25.4% plus 14.0% plus 10.8% = 50.2% (10-K page:9). Lumen's share is reported before AT&T's acquisition of Lumen's fiber business, so the combined share is by customer name, not by economic exposure.
- Unbilled share of gross receivables at August 1, 2026: 1,334,390 over 2,281,043 = 58.5% (10-Q Q2 FY27 page:12).
- Fiscal 2027 outlook midpoints are not computed; ranges are quoted as printed.

Not calculable: any ownership percentage, pro forma EBITDA, restricted-payment capacity and covenant headroom, for the reasons given in the Gaps section.

## Gaps

| Gap | Severity | Effect | Remediation |
| --- | --- | --- | --- |
| Ownership, control rights, insider holdings, board composition and related-party transactions are not in the pack (incorporated by reference to a proxy statement). | Medium | Governance and sponsor alignment cannot be scored beyond documented actions | Obtain the proxy statement and beneficial ownership table |
| Executed Credit Agreement, First Amendment, 2029 indenture, Power Solutions Unit Purchase Agreement and National Technology Integrators purchase agreement are not supplied. | High | Restricted-payment, debt and lien capacity, guarantor names, escrow and indemnity terms are filing summaries only | Obtain the documents |
| No pro forma EBITDA for Power Solutions or National Technology Integrators. | High | Earnings base for the new leverage is unverified | Obtain acquisition-date financials or management bridge |
| No credit ratings in the pack. | Medium | Market access and pricing-grid context missing | Obtain rating reports if any |
| Subcontractor spend, maintenance versus growth capex, and non-recourse receivable sale volumes are not disclosed. | Medium | Cost flexibility and cash conversion cannot be sized | Obtain management disclosure |
| Management outlook ranges and the National Technology Integrators profile are forward-looking or unaudited statements. | Low | They must not be used as actuals | Keep as Management Language |
| Extraction fidelity of the text files and chart or image content in the decks were not reviewed. | Low | Residual transcription risk | Spot-check key rows |

## Next module

Proceed to CP-2 (fundamental credit synthesis) using the rows in this handoff and the CP-1 financial base, then CP-5. Carry forward: customer concentration and non-committed volumes; the acquisition-led leverage step-up with an unverified pro forma earnings base; buybacks as a competing use of cash; the Insufficient Information rows on ownership, ratings and restricted-payment capacity; and the preliminary status of both purchase price allocations. Do not describe Management Language rows as facts, and do not state covenant headroom.
