## Request

Issuer: MOLINA HEALTHCARE, INC. (ticker MOH; Delaware registrant; Long Beach, California). As-of date and cutoff: 2026-11-05. Pathway: credit snapshot, public case; reporting currency USD. Current period Q3 2026 (nine months and balance sheet at September 30, 2026); prior period FY2025.

Scope: build the business, operating-model, ownership, transaction and governance fact pack a credit committee reads first, from the creditor's perspective, using the pinned sources and the CP-1 financial base. Each fact row carries one category: Documentary Fact (the cited source states it), Management Language (management's characterisation, quoted and qualified, never adopted), Analyst Interpretation (my reading of cited evidence), or Insufficient Information (evidence missing; the missing datapoint and why it matters are stated). Figures that are CP-1 calculations are referenced to CP-1, not recalculated here. No peer ranking, instrument recommendation or recovery conclusion is given. No external material is used; every fact comes from the pinned sources.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Use in this handoff |
| --- | --- | --- |
| 10-K_2025-12-31_moh-20251231.htm.jsonl | c9fc11483fb4b7c19a024a1eea5a26db7d569aa891c87974935ef7d58e311c73 | Business, segments, contracts, strategy, capital management, legal, controls, debt note |
| 10-Q_2026-03-31_moh-20260331.htm.jsonl | 13a11f49b2609a371d7feaaf1fc732c450976bf0759ca520903d8cae2d01480e | Q1 2026 impairment, litigation status |
| 10-Q_2026-06-30_moh-20260630.htm.jsonl | 2e116fbc160064a31ee8ffdf3cb7b87c5a30be87614aee212f07d7cf0a47d671 | Q2 2026 contract awards and trends |
| 10-Q_2026-09-30_moh-20260930.htm.jsonl | 0eb181a17a96ec54e5242c30d2326e1cb431ceae3183b3fa8dd8bb665798cbdd | Latest segments, procurements, trends, legal resolution, liquidity |
| EX-99.1_2026-04-22_moh1q26_er.htm.jsonl | 209474d035cda2f89bcc2ac9abfc62e08120c0698a0cff7b05687b4b711891da | Q1 2026 management statements and guidance |
| EX-99.1_2026-07-22_moh2q26_er.htm.jsonl | fd72c687dc87193147ac248ab3371c514003ac36c928d56dc905298dfee99d6d | Q2 2026 management statements and raised guidance |
| EX-99.1_2026-10-21_moh3q26_er.htm.jsonl | f0ee0db37cb0340d37b34fde6c6107463ac060309062b86bfa3e7caa6f07a604 | Q3 2026 management statements, guidance, Florida and MAPD effects |

The context file (sha256 038deefd3d0187dee809d7ec7eb3f32548cc8a768b8a64a8e4dfbffc4bec802f) is run settings, not issuer evidence: sponsor, parent, borrower, guarantors, deal terms and ratings are blank in it, and none is treated as zero. The sector label comes from the context, not from a filing.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 9a38b7e81c8a9d34c66cf8ba2d88f056039593cb8ea14bd1234abdea53036afb | Source readiness; its gaps (no executed legal documents, no presentations, ratings only in the annual report) are carried forward |
| CP-1 | 9d11362d7487441f85b5fd6c0bd9f2e0a792068fa4a098f857b8fd19f913a548 | Financial base: EBITDA, leverage, liquidity and maturity figures, referenced rather than recalculated |

Consistency with upstream: nothing in CP-0 or CP-1 is contradicted. This handoff adds one source conflict neither covered (the Florida contract description, below) and notes that some CP-1 forward-looking items (Marketplace and Medicaid year-end 2026 membership expectations) were updated by the Q3 2026 report.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Molina is a pure-play government-sponsored managed-care payer with no sponsor and 75% of FY2025 premium revenue from Medicaid. Credit risk turns on margin recovery, the Florida start-up and the 2027 exit of one Medicare product. | Medium | Ownership and control rights are not in the sources, and profitability by state contract is not disclosed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Medicaid was 75% of FY2025 premium revenue, and four state contracts (California, New York, Texas, Washington) each exceeded 10% of Medicaid premium revenue. | Revenue is tied to a few state procurements and annual rate decisions, so rate lag or a contract loss would move earnings quickly. | High |
| Medical costs outran rates: the consolidated medical care ratio was 92.1% in 9M 2026 against 90.8% in 9M 2025, and management calls 2026 the trough year for Medicaid margins. | Margin recovery is a management claim not yet evidenced by results, so it should not be relied on for debt service. | Medium |
| Full-year guidance includes a $1.50 per share loss from the Florida contract start-up and a $1.00 loss from the Medicare product being exited for 2027. | Near-term earnings carry start-up and exit drags that delay recovery. | Medium |
| The company repurchased $1,000 million of stock in FY2025 and none in 9M 2026; $500 million of authorization remains through December 31, 2026. | Shareholder returns took priority while earnings fell, and the remaining authorization is a possible cash use to monitor. | Medium |
| The securities class action was dismissed with prejudice on October 20, 2026, and the derivative action dismissal notice was filed on October 6, 2026. | A legal and governance overhang has eased, though earlier filings could not estimate any loss. | High |

### Business and transaction view

Molina Healthcare, Inc. is a listed, sponsor-free managed-care organisation that "provides managed healthcare services under the Medicaid and Medicare programs, and through the state insurance marketplaces" (10-K, page:108), operating in 21 states with about 4.9 million members at September 30, 2026 (10-Q Q3, page:5). Its customers are government payers ("Our primary customers are state Medicaid agencies and the federal government", 10-Q Q3, page:31), so revenue is a fixed per-member-per-month premium that the health plan underwrites against medical cost, and the credit mechanism is the gap between rate updates (set annually by states and CMS) and medical cost trend. That gap is the central fact of the period: the 10-K describes a "rate and trend imbalance that we believe to be temporary" (page:86), the medical care ratio rose from 89.1% in FY2024 to 91.7% in FY2025 and 92.1% in 9M 2026 (CP-1), and earnings compressed accordingly (CP-1 operating income, EBITDA and leverage). The business is concentrated: Medicaid is 75% of FY2025 premium revenue (page:15), four state contracts (California, New York, Texas, Washington) each exceed 10% of Medicaid premium revenue, and Medicaid contracts run three to five years with either side able to terminate with or without cause (page:108), so each re-procurement is a revenue-durability event (Virginia was lost: contracts terminated June 30, 2025, page:12). Two portfolio actions are reshaping 2026 and 2027: the Marketplace book is being cut deliberately (9M 2026 Marketplace premium revenue 1,994 against 3,401, membership 267,000 against 713,000, 10-Q Q3 pages 31-34) and the traditional Medicare Advantage-Part D product will be exited for 2027 with a 93 impairment recognized in Q1 2026 (CP-1). Management's long-term growth targets (premium revenue growth of 11% to 13% and passing $50 billion in 2027, 10-K page:10) are Management Language and sit against FY2026 premium revenue guidance of approximately $42 billion, so they are not used as a base case. No sponsor, controlling holder, dividend recapitalisation or related-party leakage appears in the sources; the documented capital-allocation behaviour is a pattern of share repurchases funded by subsidiary dividends, assessed below as Neutral or Mixed. Debt is parent-level senior unsecured notes plus an undrawn revolver (CP-1); whether subsidiaries guarantee the notes is not stated in the sources. The evidence supports a business and transaction read at the level of Documentary Facts; it restricts conclusions on ownership, control rights and covenant capacity because the proxy-based ownership information and executed documents are not supplied.

### Company and operating model

| Area | Fact | Category | Locator | Credit relevance |
| --- | --- | --- | --- | --- |
| Core activity | "provides managed healthcare services under the Medicaid and Medicare programs, and through the state insurance marketplaces"; four segments: Medicaid, Medicare, Marketplace, Other | Documentary Fact | 10-K page:108 | Pure government-programme exposure: revenue depends on state and federal budgets and rate setting |
| Geography and scale | 21 states; about 4.9 million members at September 30, 2026 against 5,491,000 at December 31, 2025 | Documentary Fact | 10-Q Q3 pages 5 and 31 | Membership down by 629,000 (calculated) in nine months; scale is shrinking |
| Customers | "Our primary customers are state Medicaid agencies and the federal government" | Documentary Fact | 10-Q Q3 page:31 | Counterparty risk is sovereign-like but budget- and policy-driven |
| Revenue model | State Medicaid agencies pay per-member-per-month rates; "our health plans are at risk"; Medicare Advantage pays a "fixed PMPM premium payment" adjusted by risk score; Marketplace rates are filed annually | Documentary Fact | 10-K pages 16, 19, 22 | Medical cost overruns fall on Molina until rates reset |
| Segment mix FY2025 | Medicaid 32,240, Medicare 6,235, Marketplace 4,487, Other 90 of 43,052 premium revenue; Medicaid "constituted 75%" | Documentary Fact | 10-K pages 8, 15 | High reliance on Medicaid margin |
| Segment mix 9M 2026 | Medicaid 24,175, Medicare 4,698, Marketplace 1,994, Other 6 of 30,873 | Documentary Fact | 10-Q Q3 page:17 | Medicaid share rises as Marketplace shrinks (78.3%, calculated) |
| Concentration | California about 4,170 (13% of Medicaid premium revenue), New York about 3,221 (10%), Texas about 5,735 (18%), Washington about 4,194 (13%) in FY2025 | Documentary Fact | 10-K pages 15-16 | These four contracts are about 54% of Medicaid premium revenue (calculated): loss or repricing of one is material |
| Contract terms | Medicaid contracts three to five years, terminable by state or plan with or without cause; Medicare one to three years; Marketplace one-year | Documentary Fact | 10-K page:108; page:22 | Short contract tenor means revenue visibility depends on re-procurement success |
| Rate and trend | "rate and trend imbalance that we believe to be temporary" (management view); "state rate updates continue to lag increased cost trends and risk corridor protection is now limited" | Management Language | 10-K page:86 | Margin recovery depends on rate catch-up; unproven |
| Medical cost drivers | Higher utilization in "behavioral health services, high-cost drugs, long-term services and supports (LTSS)" and inpatient and outpatient settings; Medicaid MCR 91.8% in FY2025 against 90.3% | Documentary Fact | 10-K page:86 | Cost trend is the main earnings driver |
| Latest MCR | Medicaid MCR 93.0% in Q3 2026 against 92.0%; Medicare 93.0%; Marketplace 92.5%; consolidated 92.9% against 92.6% | Documentary Fact | Q3 release page:6 (segment table) | Margins still compressed |
| Cost structure | G&A ratio 6.8% in 9M 2026 against 6.5% "reflects the impact of lower premium revenues, partially offset by ... operating discipline"; IT services outsourced under a 2019 agreement extended in 2022 for seven years | Documentary Fact | 10-Q Q3 page:26; 10-K page:30 | Operating leverage works against the issuer when premium falls |
| Capital spending | Purchases of property, equipment and capitalized software of 94 in 9M 2026 | Documentary Fact | 10-Q Q3 page:4 | Capital-light; capex is small against operating cash flow swings |
| Working capital | Capitation is received monthly "in advance of payments for medical claims"; medical claims and benefits payable 4,988; amounts due government agencies 1,141; days in claims payable 44 | Documentary Fact | 10-Q Q3 pages 2, 38; Q3 release page:7 | Settlements with governments and risk-adjustment timing drive cash flow swings (CP-1) |
| Management view of cycle | "we believe we are likely observing the beginning of the turn in Medicaid margins" (CEO, October 21, 2026); "2026 is the trough year for Medicaid pretax margins" (July 22, 2026) | Management Language | Q3 release page:1; Q2 release page:1 | Promotional until margins improve |
| Competition | Primary Medicaid competitors named: Centene, CVS Health, Elevance Health, UnitedHealth Group and not-for-profit organisations; "increasing competition driven by renewed interest from large national health plans" | Documentary Fact | 10-K page:31 | Re-procurements are contested |
| Policy exposure | OBBBA expected to reduce Expansion enrollment (10-K: 15% to 20% by 2029 on 1.2 million members; 10-Q Q3: premium reduction at a compounded annual rate of 2% to 3% through 2029); provider tax limits begin in 2028 | Documentary Fact | 10-K page:23; 10-Q Q3 page:28 | Structural enrollment and funding headwind; estimates were restated between filings |
| Profitability by state contract | Not disclosed | Insufficient Information | Searched all sources | Cannot test which contracts earn the margin; matters for the contract-loss scenario |

### Company profile

| Attribute | Value | Category | Locator |
| --- | --- | --- | --- |
| Legal name and listing | MOLINA HEALTHCARE, INC.; common stock on the New York Stock Exchange under MOH; large accelerated filer | Documentary Fact | 10-K page:1 |
| Incorporation and HQ | Delaware; 200 Oceangate, Suite 100, Long Beach, California | Documentary Fact | 10-K page:1 |
| Sector and country | Hospital and medical service plans; United States (sector label from the run context) | Documentary Fact | Context file; 10-K page:1 |
| Fiscal year end | December 31 | Documentary Fact | 10-K page:1 |
| Employees | Approximately 19,000 at December 31, 2025 | Documentary Fact | 10-K page:35 |
| Chief executive and chief financial officer | Joseph M. Zubretsky (CEO); Mark L. Keim (CFO and Treasurer), signatories to the Q3 2026 report; the 10-K calls the business "highly dependent on the leadership of Mr. Zubretsky" | Documentary Fact | 10-Q Q3 page:44; 10-K page:70 |
| Auditor | Ernst & Young LLP, auditor since 2000; internal control over financial reporting concluded effective at December 31, 2025, with ConnectiCare excluded from the assessment | Documentary Fact | 10-K pages 105, 146 |
| Shares outstanding | Approximately 52.2 million at October 16, 2026 | Documentary Fact | 10-Q Q3 page:1 |
| Ownership and control rights | Not supplied: Part III of the 10-K is incorporated by reference to the 2026 proxy statement, which is not in the pinned set; no controlling holder is mentioned in the sources | Insufficient Information | 10-K page:2 |
| Sponsor and parent | None: a listed company with no sponsor or parent named; context fields blank | Documentary Fact | 10-K page:1; context file |
| Borrower and issuer | Molina Healthcare, Inc. (parent corporation) is the borrower and issuer of the senior notes | Documentary Fact | 10-Q Q3 page:15 |
| Subsidiary guarantors | Not stated in the sources | Insufficient Information | Searched for guarant |
| Debt ratings | Senior notes rated BB by S&P and Ba2 by Moody's (annual report date) | Documentary Fact | 10-K page:94 |
| Prior ownership and recapitalisation history | None disclosed; ConnectiCare was acquired from EmblemHealth, Inc. | Documentary Fact | 10-K page:12 |
| Premium revenue and membership | 43,052 FY2025; 5,491,000 members at December 31, 2025 | Documentary Fact | 10-K pages 8, 105 |
| Capital structure | Five senior unsecured notes (total principal 3,800) and a 1,250 revolver, undrawn (see CP-1) | Documentary Fact | 10-Q Q3 pages 14-15 |

### Transaction summary and new debt issues

There is no leveraged buyout, sponsor transaction or pending merger in the sources, and no financing transaction after the February 4, 2026 credit agreement amendment appears in the pinned sources up to the cutoff; the transaction history is organic growth through state procurements plus bolt-on acquisitions and refinancings. Status of each item below is as stated in the sources.

New debt and facilities (Documentary Fact, status: completed). On November 20, 2025 the company completed a private offering of $850 million of 6.500% senior notes due February 15, 2031, with interest payable semiannually on February 15 and August 15 from August 15, 2026 and deferred issuance costs of $12 million; net proceeds repaid $740 million of term loan debt under the prior credit agreement and funded general corporate purposes (10-K page:131). The same day the company entered a new credit agreement replacing the June 8, 2020 agreement, with a $1.25 billion revolver terminating November 20, 2030, a $15 million swingline, a $100 million letter-of-credit sub-facility and uncommitted incremental term loans of up to $800 million for acquisitions (10-K page:131); Truist Bank is administrative agent (10-K page:153). Earlier, $750 million of 6.250% notes due January 15, 2033 were issued in November 2024 (10-K pages 83, 130). The February 4, 2026 First Amendment temporarily reduced the minimum interest coverage ratio to 1.75 to 1.00 for quarters through December 31, 2026, then 2.00, 2.50 and 2.75 for the March, June and September 2027 quarters (10-K page:132); the amendment was agreed before the Q1 2026 reporting and is a subsequent event relative to the FY2025 balance sheet. During 2025 the company borrowed 950 of term loans and 150 under the credit facility and repaid all of them (10-K page:132). Liquidity effect: the notes refinanced the term loans and left the revolver undrawn; parent cash and investments are in CP-1. Use of proceeds, amounts and rates are stated in the filing; the executed indentures and credit agreement are not in the pinned set, so covenant baskets and restricted-payment capacity are Insufficient Information.

Acquisitions (Documentary Fact, status: completed). ConnectiCare Holding Company, Inc., "a wholly owned subsidiary of EmblemHealth, Inc.", was acquired effective February 1, 2025 for $350 million, serving about 140,000 members across Marketplace, Medicare and certain commercial products (10-K page:12); it is 4% of total assets and 4% of revenues in FY2025 and was excluded from the internal control assessment (10-K page:146). The 2024 Bright acquisition used $295 million of net cash (10-K page:92). The sources state that acquisition appetite remains ("we remain opportunistic about deploying capital to accretive acquisitions", Management Language, 10-K page:10), but the incremental term loan is uncommitted and no acquisition is announced; no inference is drawn from one deal.

Shareholder distributions (Documentary Fact). The company purchased about 1,679,000 shares for $500 million in Q1 2025 (average $297.83) and about 2,849,000 shares for $500 million in Q3 2025 (average $175.50) (10-K page:13); it made no purchases under the program in 9M 2026, and $500 million remained available through December 31, 2026 as of October 16, 2026 (10-Q Q3 page:40). Subsidiary dividends to the parent were 985 in 2025 (10-K page:90).

Subsequent events to the cutoff (Documentary Fact). The new Florida Kids Medicaid contract commenced on October 1, 2026 (10-Q Q3 page:29); the securities class action was dismissed with prejudice on October 20, 2026 and the plaintiff filed a dismissal of the derivative action on October 6, 2026 (10-Q Q3 pages 18-19); the Q3 release dated October 21, 2026 reaffirmed FY2026 guidance (Q3 release page:2). Nothing dated after the cutoff is used.

### Timeline

| Date | Event | Category | Locator | Credit relevance |
| --- | --- | --- | --- | --- |
| April 2024 | Virginia DMAS notice of intent excluded Molina; contracts terminated effective June 30, 2025 | Documentary Fact | 10-K page:12 | Contract loss precedent |
| November 2024 | $750 million 6.250% notes due 2033 issued | Documentary Fact | 10-K page:83 | Refinancing at higher coupon |
| February 1, 2025 | ConnectiCare acquisition closed, $350 million | Documentary Fact | 10-K page:12 | Added Marketplace and Medicare members |
| Q1 and Q3 2025 | $500 million share purchases in each quarter | Documentary Fact | 10-K page:13 | Cash returned while margins fell |
| July 2025 | OBBBA signed into law | Documentary Fact | 10-K page:22 | Enrollment and funding headwind |
| October 3, 2025 | Securities class action filed | Documentary Fact | 10-K page:140 | Litigation overhang |
| November 20, 2025 | $850 million 6.500% notes and new $1.25 billion revolver | Documentary Fact | 10-K page:131 | Term loans repaid, maturities extended |
| December 12, 2025 | Derivative suit filed | Documentary Fact | 10-K page:140 | Governance overhang |
| January 1, 2026 | MMP members transitioned to integrated dual plans (about $1.9 billion total revenue in 2025); several new contracts commenced | Documentary Fact | 10-K page:19; 10-Q Q3 page:29 | Product transition |
| February 4, 2026 | First Amendment to credit agreement (interest coverage relief) | Subsequent event to FY2025 | 10-K page:132 | Covenant relief signals pressure on headroom |
| Early February 2026 | Decision to exit the MAPD product for 2027 | Subsequent event to FY2025 | 10-K page:108 | Planned margin repair at near-term cost |
| Q1 2026 | $93 million impairment of MAPD intangible assets | Documentary Fact | 10-Q Q1 page:25 | Non-cash charge |
| July 22, 2026 | Adjusted EPS guidance raised by $0.25 to at least $5.25 | Management Language | Q2 release page:1 | Guidance, not result |
| October 1, 2026 | Florida Kids contract commenced | Subsequent event to Q3 quarter | 10-Q Q3 page:29 | Start-up losses guided for Q4 2026 |
| October 6 and 20, 2026 | Derivative dismissal notice; class action dismissed with prejudice | Subsequent event to Q3 quarter | 10-Q Q3 pages 18-19 | Overhang eased |
| October 21, 2026 | Q3 2026 results; guidance reaffirmed | Management Language | Q3 release page:2 | Guidance of at least $2.38 GAAP EPS |

### Governance and capital allocation behaviour

| Behaviour | Documented action | Category | Locator | Mechanic and implication |
| --- | --- | --- | --- | --- |
| Shareholder returns | $1,000 million of repurchases in FY2025 (average prices $297.83 and $175.50); none in 9M 2026; strategy includes "Returning excess capital to shareholders, for example, in the form of targeted share repurchase programs" | Analyst Interpretation: Neutral or Mixed | 10-K pages 8, 13; 10-Q Q3 page:40 | Repurchases were funded by subsidiary dividends of 985 and temporary borrowings that were later refinanced, with parent cash and investments falling from 445 to 223 in 2025 (10-K page:90); that reduced the parent cash buffer while medical cost trend was already rising (10-K page:86). Creditor impact is a lower parent cash buffer; the pause in 2026 is supportive, the remaining 500 authorization is a risk |
| Support for regulated subsidiaries | "We have the ability, and have committed, to provide additional capital to each of our health plans"; parent contributed 130 in 9M 2026 | Documentary Fact | 10-Q Q3 pages 35, 41 | Parent cash is a claim of the subsidiaries first: it must fund statutory capital before debt service |
| Debt management | Term loans repaid with notes proceeds; maturities extended to 2028-2033; covenant relief obtained in advance of a possible shortfall | Analyst Interpretation: Neutral or Mixed | 10-K pages 131-132 | Proactive amendment protects against technical default and may indicate limited headroom against the original 3.0 to 1.0 floor (inference only; headroom is not disclosed) |
| Reporting transparency | Effective internal control over financial reporting at December 31, 2025; past material weaknesses "subsequently been remediated" | Documentary Fact | 10-K pages 71, 146 | Reporting risk is low but not nil |
| Legal and disclosure | Securities and derivative suits alleged misleading earnings-guidance disclosures; dismissed in October 2026 | Documentary Fact | 10-Q Q3 pages 18-19 | Dismissal removes the overhang; guidance credibility remains a monitoring item because the suits concerned earnings-guidance disclosures, and the 2026 adjusted earnings guidance was reaffirmed in Q1, raised in Q2 and reaffirmed in Q3 (Q1, Q2, Q3 releases). The 10-K and the Q1 2026 report said the company could not predict the outcome or estimate a loss (10-K page:140; 10-Q Q1 page:18) |
| Creditor-adverse actions (priming, uptiering, drop-downs, collateral release) | None found; notes are unsecured and no such transaction appears | Documentary Fact | Searched all sources | No evidence of creditor-adverse behaviour; indentures are not supplied so legal capacity is Insufficient Information |

Legal capacity, willingness and feasibility are kept separate: capacity (restricted payment and debt baskets) is defined by executed documents that are not supplied; willingness is shown by the repurchase and amendment record above; feasibility is in CP-1 (parent cash, earnings, covenant sensitivity).

### Source conflicts and superseded statements

| Item | Statement A | Statement B | Effect |
| --- | --- | --- | --- |
| Scale and start of the Florida contract (logged conflict, not reconciled) | 10-K page:12: "Florida Kids ... We are the sole plan selected and expect to serve approximately 120,000 enrollees. The contract start date has not been determined" | 10-K page:81: the award "is expected to cover approximately 120,000 enrollees and yield $6 billion in annual premium revenue and is expected to commence in the fourth quarter of 2026"; 10-Q Q3 page:29 later states the contract "commenced on October 1, 2026" | The start date is resolved by the Q3 report. The annual premium revenue of $6 billion for 120,000 enrollees in a children's programme is not reconciled with the Florida Kids description; the size of the Florida contribution (and of the guided Q4 start-up loss) cannot be sized from the sources |
| Marketplace year-end 2026 membership (superseded) | 10-K page:21: about 220,000 | 10-Q Q3 page:30: about 250,000 | The later filing controls for its date; not a conflict |
| Medicaid 2026 enrollment (superseded) | 10-K page:14: "flat in 2026 compared to 2025" | 10-Q Q3 page:30: decrease to 4.4 million members by year end, excluding the 120,000 Florida Kids members | Later filing controls |
| OBBBA timing (superseded) | 10-K page:23: provider tax limits "may take 5 to 15 years"; 15% to 20% reduction on 1.2 million Expansion members by 2029 | 10-Q Q3 page:28: "5 to 10 years"; premium reduction at a compounded annual rate of 2% to 3% through 2029 | Later filing controls; estimate basis changed from members to premium |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence or conflict |
| --- | --- | --- | --- | --- |
| Revenue durability | Medicaid is 75% of FY2025 premium revenue; four states are about 54% of Medicaid premium (calculated); contracts are three to five years and terminable (10-K pages 15, 16, 108) | Re-procurement or repricing of one large state contract removes a large block of premium while fixed G&A and debt service remain | Revenue is durable only as long as procurement wins continue; the track record cited (re-procurement win rate of 90%, Management Language, 10-K page:10) is not independently verified | Virginia loss (page:12) shows contracts can be lost; new wins (Florida, Illinois, Nevada, Wisconsin) offset |
| Margin and cash-flow risk | MCR 92.1% in 9M 2026 against 90.8%; rate and trend imbalance; Marketplace and Medicare adjustments (10-Q Q3 pages 33-34) | Cost trend outruns annually reset rates, so a point of MCR moves premium-scale earnings (CP-1: operating income of 172 LTM) | Debt service rests on a thin earnings base and on settlement-sensitive cash flow; EBITDA over interest expense is 1.56x on a simple LTM basis (CP-1) | Management says trend has plateaued and recent rate updates are strong for 2027 (Q3 release page:1), Management Language |
| Concentration | California, New York, Texas and Washington; Medicaid 78.3% of 9M 2026 premium (calculated) | Single-state policy or rate decisions drive group results | Event risk is state-specific, not diversified | Footprint across 21 states |
| Sponsor alignment | No sponsor; public equity; repurchases of 1,000 in FY2025 | Equity holders' returns compete with creditors for parent cash | Alignment is public-equity, not creditor-specific; monitor the remaining repurchase authorization | Repurchases paused in 2026 |
| Key uncertainties | Florida start-up loss of $1.50 per share and MAPD loss of $1.00 per share in guidance; OBBBA; Marketplace risk adjustment | One-off drags and policy shifts reduce earnings visibility through 2027 | Recovery timing is uncertain; covenant floor steps up in 2027 (CP-1) | Guidance reaffirmed October 21, 2026 (Management Language) |

### Downstream consumers

| Consumer | Readiness | What it should take from this handoff | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 (credit synthesis) | Ready with limitations | Revenue concentration, margin mechanics, capital-allocation record, litigation resolution, Florida and MAPD drags, conflict log | Business risk is a decision driver for the fundamental view | Ownership and indenture terms not supplied; treat management recovery claims as unproven; resolve the Florida scale conflict if sizing is needed |
| CP-5 (evidence trace review) | Ready with limitations | Locators for every row, the logged Florida conflict and the superseded estimates | The review must test that figures carry consistent periods and sources | Check CP-1 reference figures and note that 10-K statements about Florida conflict internally |

## Calculations

| Item | Inputs | Result |
| --- | --- | --- |
| Medicaid share FY2025 | 32,240 / 43,052 (10-K page:8) | 74.9%, printed as 75% (10-K page:15) |
| Medicaid share 9M 2026 | 24,175 / 30,873 (10-Q Q3 page:17) | 78.3% |
| Four large state contracts, FY2025 | California 4,170 + New York 3,221 + Texas 5,735 + Washington 4,194 (10-K pages 15-16) | 17,320, or 53.7% of Medicaid premium revenue of 32,240 (printed shares 13% + 10% + 18% + 13% = 54%) |
| Membership change | 4,862,000 less 5,491,000 (December 31, 2025); less 5,628,000 (September 30, 2025) | -629,000 (-11.5%); -766,000 (-13.6%, printed as 14% in 10-Q Q3 page:24) |
| Marketplace premium revenue change 9M | 1,994 less 3,401 (10-Q Q3 page:17) | -1,407 (-41.4%) |
| MAPD share of Medicare premium revenue 2025 | 1,566 / 6,235 (10-K page:21) | 25.1% (printed as 25%) |
| Weighted average coupon (CP-1) | Annual coupon 191.4 over principal 3,800 | 5.04%; the 10-K states "weighted average cost of fixed debt is at 5.0%" (page:13), consistent |

CP-1 derived figures (EBITDA, leverage, interest cover, liquidity) are referenced, not recalculated.

## Gaps

| Gap | Search performed | Severity | Effect | Action |
| --- | --- | --- | --- | --- |
| Ownership, control rights and major holders not supplied (proxy statement not in pinned set) | Searched for beneficial owner, controlling and holder | Medium | Cannot assess control or alignment beyond "no sponsor" | Add the 2026 proxy statement |
| Indentures and credit agreement not supplied; restricted-payment and debt baskets unknown | Searched for indenture and credit agreement | Medium | Legal capacity for distributions and additional debt not assessable | Add executed documents |
| Subsidiary guarantees of the notes not stated | Searched for guarant | Low | Structural subordination of noteholders to subsidiary claims is unconfirmed | Read the indentures |
| Profitability by state contract and re-procurement calendar beyond Washington and Georgia/Texas not disclosed | Searched concentration and contract tables | Medium | Cannot test contract-loss scenarios | Request state-level data |
| Florida contract scale conflict (120,000 enrollees against $6 billion annual premium revenue) | Compared 10-K pages 12 and 81 | Medium | Size of new contract and start-up loss not verifiable | Obtain the contract award or management clarification |
| Management targets (premium revenue passing $50 billion in 2027; growth of 11% to 13%) are not supported by evidence in the pack | Reviewed strategy text | Low | Not used as base case | Label as Management Language |
| No investor presentation slides | Reviewed source list | Low | Management narrative limited to releases | None for the minimum set |

## Next module

Proceed to the fundamental credit synthesis (CP-2) with CP-1 and this handoff. Carry forward: Medicaid concentration and the four large state contracts; the unproven margin-recovery claim; Florida start-up and MAPD exit drags; the logged Florida conflict; the repurchase record and remaining authorization; unsupplied ownership, indentures and guarantees. The evidence-trace review (CP-5) follows once CP-2 is accepted.
