# CP-1A — Business and transaction context: MAXIMUS, INC. (mms)

## Request

- Issuer: MAXIMUS, INC. (issuer id `mms`; the registrant is "Maximus, Inc.", NYSE: MMS), as of 2026-11-05, information cutoff 2026-11-05.
- Periods. Maximus has a fiscal year ending September 30. Current period `q3-2026` is read as fiscal Q3 2026, the three months ended June 30, 2026, with the nine months to that date; prior period `fy-2025` is the fiscal year ended September 30, 2025. The quarter ended September 30, 2026 is fiscal Q4 2026 and is not supplied. Reporting currency USD (context).
- Question: which transaction, ownership, business and operating facts matter most to the creditor, and what do they imply for business risk, revenue visibility, cash conversion, liquidity and leverage tolerance? This is a business and transaction fact pack, not a credit rating, peer ranking, instrument recommendation or recovery conclusion.
- Perimeter: the registrant's consolidated statements. Maximus files alone; no parent, sponsor or separate borrower is named (context fields for parent, sponsor, guarantors and deal terms are blank, and blank is not read as zero or as absence).
- Upstream: CP-0 rated each consumer READY_WITH_LIMITATIONS; CP-1 supplied the financial base. Figures here are references to CP-1 where they come from it. Where this answer extends or corrects an upstream handoff it says so under `### Reconciliation to upstream handoffs`.
- Categories used on every fact row: Documentary Fact (the cited source states it), Management Language (management's characterisation, quoted and qualified, not adopted), Analyst Interpretation (a reading of cited evidence), Insufficient Information (evidence missing; the missing datapoint is stated).
- Execution: host session; no provider was called.

## Sources

Locators are `page:N` chunks of the pinned `.jsonl` text, not printed page numbers. "10-K" is the fiscal 2025 annual report; "Q1 10-Q", "Q2 10-Q" and "Q3 10-Q" are the quarterly reports for the quarters ended December 31, 2025, March 31, 2026 and June 30, 2026; "Q1 release", "Q2 release" and "Q3 release" are the Exhibit 99.1 earnings releases dated February 5, May 7 and August 6, 2026.

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-09-30_mms-20250930.htm.jsonl | 962786100737da7c8a25bf2c0b0d8b7bba5fc8fe85f1a63dc4a22607d3101fd0 | Business, risk factors, history, ownership facts, dividend and repurchase policy, divestitures, litigation |
| 10-Q_2025-12-31_mms-20251231.htm.jsonl | 1ece10b3b4a1f72edf52da31ebe99ab2543998f22e423edd0be2ded3496f545d | Q1 FY2026 dividend and subsequent event |
| 10-Q_2026-03-31_mms-20260331.htm.jsonl | 72c28dae66fdf3271ecd55284a1e9ffd02e932cd689052dff69253e7614fe8a8 | Q2 FY2026 dividend and subsequent event |
| 10-Q_2026-06-30_mms-20260630.htm.jsonl | e0ee49037a76362fa1359adeb6f1d6ec0af3bf048fce3d62f4b088d4d2e2d60b | Latest business drivers, divestitures, debt amendment, repurchases, customer modification, subsequent events |
| EX-99.1_2026-02-05_mms-2025x12x31x8kxex991.htm.jsonl | ff62eabdd3d1037513edc754533c1c20140d9d029aa9713e0d89283ab79659d9 | Q1 release: management narrative (attributed) |
| EX-99.1_2026-05-07_mms-2026x03x31x8kxex991.htm.jsonl | 3cc2b6ddbaacd127b88b399aaed54a4ba71be05c3b12c29939da2343ffcad4ec | Q2 release: guidance and repurchase program (attributed) |
| EX-99.1_2026-08-06_mms-2026x06x30x8kxex991.htm.jsonl | 78b1fb3302628c3c36cbd9a44260145bf92a755c30565ab852ed03fa9e5e9aa0 | Q3 release: management narrative, pipeline, guidance, leverage target (attributed) |
| context | 427dc9f0877ed950bde305fcdd6af025bde473794c90eea607afca11f0c6cd79 | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | b2c3bb0b1f4af634e0abd5fcab811ad35e641a5d0e7ca14dd9cdc832dae5d76e | Source readiness, identity and period conventions, limitations |
| CP-1 | 8829349e46633913828d697cb82b1a46f8bb93ac6c3f2be62bdafd8355e5278d | Financial base: debt, liquidity, covenants, leverage, cash flow, claims outside debt |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Maximus is a widely held government services contractor with no sponsor and a heavy U.S. federal concentration. Management has raised leverage through partly debt-funded buybacks while a major customer modification lowers earnings through December 31, 2026. | Medium | The proxy statement, Credit Agreement and customer-level contract terms are not supplied, so ownership percentages, creditor protections and renewal dates cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| About 55% of fiscal 2025 revenue came from the U.S. federal government, about 60% from the ten largest contracts and about one-fifth from a single federal agency. | Revenue and collections depend on a few government decisions, so one contract change or payment delay moves earnings and liquidity quickly. | High |
| No sponsor or controlling holder is disclosed; the 10-K reports 30 holders of record and about 151,000 beneficial owners. | No sponsor dividend-recapitalisation risk is evidenced, but control and related-party facts sit in an unsupplied proxy statement. | Medium |
| Share purchases of 447,482 thousand in fiscal 2025 and 204,919 thousand in nine months 2026 were partly funded by credit facility expansions, and the dividend rose from 0.30 to 0.33. | Management documents willingness to add debt for shareholder returns up to its 2x to 3x leverage target, so leverage can rise further. | Medium |
| Backlog was 15,327 million US dollars at September 30, 2025, down from 16,167 million, and the Outside the U.S. segment is guided to break even for fiscal 2026. | Visibility is long but contracts are terminable for convenience, and weak international profit gives consolidated margins no support. | Medium |
| On May 27, 2026 Term Loan B was increased by 325 million; no sponsor deal, bond issue or acquisition of the issuer is described. | Financing is ordinary-course bank debt; amendment terms are not documented beyond the amount. | High |

### Business and transaction view

MAXIMUS, INC. is an independent, widely held provider of outsourced government services: program operations (eligibility, enrollment and contact centers), clinical assessments and technology services, delivered through three segments, U.S. Federal Services, U.S. Services and Outside the U.S. (10-K page:7 to page:11). There is no sponsor, no pending transaction and no acquisition of the issuer in the supplied sources, so the transaction row is Insufficient Information rather than an adverse finding. The creditor-relevant facts are business concentration and capital allocation. Revenue is anchored in government programs with a long backlog, but the 10-K states that approximately 60% of fiscal 2025 revenue came from the ten largest contracts and about one-fifth from a single federal agency (10-K page:19), and that "almost all" contracts permit termination for convenience (page:17). Cash conversion is lumpy because payments from government customers can be delayed: the fiscal Q3 10-Q reports days sales outstanding of 98 days against 62 days and links the delay to "one of our large contracts with the U.S. federal government" (Q3 10-Q page:31). Capital allocation has been shareholder-oriented: buybacks and a higher dividend were funded partly by expanding the term loans, and the CP-1 financial base shows net debt to issuer-adjusted EBITDA of 2.25x at June 30, 2026 against 1.60x at September 30, 2025, with the reported covenant ratio at 2.00 against a 4.00 maximum. A temporary contractual modification by a major customer, effective July 1, 2026 through December 31, 2026, cut fiscal 2026 earnings and free cash flow guidance in August 2026. The only financing event in the period is a May 27, 2026 amendment that added 325 million US dollars to Term Loan B. The open items for monitoring are the proxy statement (ownership and related parties), the Credit Agreement, the identity of the customers behind the largest contracts, and everything after August 6, 2026.

### Company and operating model

| Item | Fact | Category | Locator | Risk mechanic and credit relevance |
| --- | --- | --- | --- | --- |
| Business description | "Maximus is a leading provider of tech-enabled services to government agencies" serving "more than 100 million American citizens" and citizens of the U.K., Canada and the Middle East | Management Language | Q3 10-Q page:23 | Self-description; the scale claim is unverified and the customer base is almost entirely government |
| Segments and mix, fiscal 2025 | U.S. Federal Services generated 56% of total revenue, U.S. Services 32%, Outside the U.S. 11% | Documentary Fact | 10-K page:7, page:8 to page:9, page:10 | Federal weight (C3) makes federal budget, procurement and shutdown risk the main driver |
| Services | Program operations 48.8%, clinical services 38.7%, employment and other 6.5%, technology solutions 6.0% of fiscal 2025 revenue | Documentary Fact | 10-K page:80 | Clinical services grew from 30.3% of revenue in fiscal 2023 to 38.7%, so earnings lean on veteran disability examinations and assessments |
| Customers | U.S. federal agencies 55.2%, New York state agencies 11.2%, other state agencies 21.2%, international governments 10.9% of fiscal 2025 revenue; "approximately 55%" federal and "approximately 33%" state and local in the risk factors | Documentary Fact | 10-K page:80, page:18 | A small number of governments fund the business; state revenue is "ultimately funded via the U.S. federal government" through cost sharing such as Medicaid (page:10) |
| Contract concentration | "approximately 60% of our revenue came from our ten largest contracts" and "approximately one-fifth of our revenue came from contracts with a single federal agency" | Documentary Fact | 10-K page:19 | Loss, rebid or modification of one large contract changes consolidated earnings; the customers and contracts behind these shares are not named |
| Named large programs | CMS Contact Center Operations (including 1-800-MEDICARE) awarded in 2022 with "annual option periods through 2031"; Department of Veterans Affairs medical disability examinations; Department of Education loan servicing support | Documentary Fact | 10-K page:7, page:98 | Option periods give visibility but each can be declined; the revenue per contract is Not supplied |
| Revenue model | Performance-based 54.4%, cost-plus 24.2%, fixed price 13.1%, time and materials 8.2% of fiscal 2025 revenue | Documentary Fact | 10-K page:80 | Performance-based and fixed-price work "provide a higher risk to us and, thus, typically have higher profit margins" (page:12), so volume shortfalls hit margin first |
| Cost structure | Cost of revenue is mostly labor: "approximately two-thirds, is labor, including subcontracted labor"; about 37,200 employees and 9,300 contingent workers at September 30, 2025 | Documentary Fact | Q3 10-Q page:24; 10-K page:13 | A labor-based cost base is variable only after redeployment; volume declines compress margin until headcount adjusts |
| Backlog | 15,327 million US dollars at September 30, 2025 (U.S. Federal Services 9,780; U.S. Services 3,916; Outside the U.S. 1,631) against 16,167 million a year earlier; average remaining contract life about 5.0 years including options | Documentary Fact | 10-K page:49, page:50 | Backlog is 2.82 times fiscal 2025 revenue (C1) but fell 5.2% (C2) and includes unexercised options and awarded but unsigned work; no later backlog is supplied |
| Pipeline | Year-to-date signed awards 1.25 billion, contracts pending 1.35 billion and a sales pipeline of 50.4 billion at June 30, 2026 (US dollars) | Management Language | Q3 release page:3 | Attributed management figures; conversion rates are not disclosed |
| Latest quarter drivers | Federal revenue decline reflects "year-over-year declines in volumes on our large, transaction-based contracts" and short-term disaster recovery work that "did not recur to the same extent"; U.S. Services "continues to experience lower volumes and demand"; consolidated organic effect was a 4.7% revenue decline in Q3 and 3.9% in nine months | Documentary Fact | Q3 10-Q page:26, page:28, page:25 | Volume-driven revenue loss with improving margin mix; management expects U.S. Services to "return to organic growth in the fourth quarter" (a forward claim, Management Language) |
| Margin drivers | Operating margin 12.6% in Q3 against 12.3%; the release credits "ongoing efficiency initiatives... including broader deployment of automation and AI-enabled tools" | Documentary Fact and Management Language | Q3 10-Q page:24; Q3 release page:2 | Margin gains are management-attributed and partly offset by fixed segment overhead; sustainability is unproven |
| Customer-directed modification | A major customer notified a temporary contractual modification effective July 1, 2026 through December 31, 2026, expected to reduce diluted EPS by about 0.35 per quarter through the remainder of fiscal 2026 and the first quarter of fiscal 2027 | Documentary Fact | Q3 10-Q page:27 | A single customer decision lowers earnings with little notice; the customer is not named and the program is not identified in the 10-Q |
| Seasonality and working capital | U.S. Federal Services has "no significant seasonality" apart from CMS open enrollment; U.S. Services "may experience seasonality"; the cash flow statement shows large outflows in the first nine months | Documentary Fact and Analyst Interpretation | 10-K page:8, page:10; CP-1 | Receivables build through the year and collect late, so liquidity is weakest at the end of the third quarter |
| Receivable sales | Wells Fargo agreement to sell U.S. receivables up to 350.0 million at any time | Documentary Fact | Q3 10-Q page:20 | Off-balance-sheet working capital funding; period-end balance outstanding is Not supplied |
| Legislative driver | OBBBA signed July 4, 2025: Medicaid redeterminations every six months and work requirements for the adult expansion population "scheduled to be effective December 31, 2026"; states "are permitted to request a delay... by up to two years" | Documentary Fact | 10-K page:17 | Potential volume for state programs; timing depends on state and federal rule decisions |
| Capital spending | Purchases of property, equipment and capitalized software 63,213 thousand in fiscal 2025; 28,752 thousand in nine months 2026 (CP-1); fiscal 2026 guidance reconciliation assumes 40 million | Documentary Fact and Management Language | CP-1; Q3 release page:6 | Light capital intensity supports free cash flow conversion once collections arrive |
| Customer-level and contract-level detail | Revenue, margin, expiry and recompete dates by contract | Insufficient Information | Not located in the sources read | Missing detail limits any test of renewal risk behind the ten largest contracts |

### Company profile

| Attribute | Value | Category | Locator |
| --- | --- | --- | --- |
| Registrant | Maximus, Inc.; Virginia corporation "founded in 1975"; commission file number 1-12997; principal executive offices 1600 Tysons Boulevard, McLean, Virginia | Documentary Fact | 10-K page:1, page:18 |
| Listing | New York Stock Exchange, symbol MMS; large accelerated filer; 52,357,763 shares outstanding at August 3, 2026 | Documentary Fact | 10-K page:1; Q3 10-Q page:1 |
| Sector and country (context) | Services-Business Services, NEC; United States (context fields, not issuer evidence) | Documentary Fact (context field) | context |
| Fiscal year | Ends September 30; the latest annual statements are for the year ended September 30, 2025 | Documentary Fact | 10-K page:1 |
| Employees and offices | About 37,200 employees and 9,300 contingent workers at September 30, 2025; about 130 leased offices in the U.S. and 102 in five other countries | Documentary Fact | 10-K page:13, page:42 |
| Geography | Services in the United States, the United Kingdom, Canada and the Middle East | Documentary Fact | 10-K page:11 |
| Shareholders | 30 holders of record at October 20, 2025 and about 151,000 beneficial owners; market value held by non-affiliates 3,801,184,315 US dollars at March 31, 2025 | Documentary Fact | 10-K page:42, page:2 |
| Auditor | KPMG LLP, auditor since 2024; Ernst & Young LLP audited fiscal 2024 and earlier (1996 to 2024); internal control over financial reporting assessed effective at September 30, 2025 | Documentary Fact | 10-K page:63, page:64, page:100 |
| Capital structure | One bank Credit Agreement with JPMorgan Chase Bank, N.A.: Term Loan A, Term Loan B and a 750 million US dollar revolver; no bonds in the supplied sources | Documentary Fact | 10-K page:52, page:83; Q3 10-Q page:29 |
| Parent, sponsor, guarantor names | Not named in the supplied sources | Insufficient Information | context; 10-K page:84 |
| Ratings | None supplied | Insufficient Information | context |

### Transaction summary and new debt issues

No acquisition of the issuer, sponsor investment, merger, spin-off, recapitalisation or tender offer is described in the supplied sources, and the context lists no deal terms, quotes or ratings. The transaction row is therefore Insufficient Information, not an adverse conclusion. The financing events in the period under review are ordinary-course bank debt. During fiscal 2025 the company expanded its credit facility by "a $250 million expansion" to support the purchase of 5.8 million shares (10-K page:51); the date and terms of that expansion are not stated in the supplied text. On May 27, 2026 the existing Credit Agreement with J.P. Morgan Chase Bank, N.A. was amended and Term Loan B was increased by 325 million US dollars (Q3 10-Q page:15); the Term Loan B principal moved from 491,250 thousand at March 31, 2026 to 814,173 thousand at June 30, 2026 while the revolver fell from 225,000 to 20,000 thousand (CP-1). Management states that "during fiscal years 2026 and 2025, we expanded our term loans to provide additional capital for our operations, as well as funds to support share repurchases" (Q3 10-Q page:31). The pricing, maturity and covenant terms of the amendment are Not supplied. New interest rate swaps took effect on June 1, 2026 (Q3 10-Q page:16). No bond, note or other debt issue appears in any source, and the Credit Agreement is described as secured by substantially all assets and guaranteed by wholly owned material domestic subsidiaries (10-K page:84). Asset sales are portfolio actions, not financings: the U.S. child support business was sold in December 2025 for approximately 15.0 million US dollars (Q3 10-Q page:15). Subsequent to June 30, 2026, the company declared a quarterly dividend of 0.33 per share on July 6, 2026 (about 17.3 million US dollars, payable August 31, 2026) and collected 245 million US dollars from a delayed federal customer (Q3 10-Q page:22, page:31). No transaction, refinancing or debt issue dated after August 6, 2026 is in the sources.

### Ownership, governance and capital allocation behaviour

| Item | Documented action or statement | Category | Locator | Legal capacity, willingness, feasibility and mechanic |
| --- | --- | --- | --- | --- |
| Ownership and control | 30 holders of record and about 151,000 beneficial owners; no holder above a disclosure threshold, controlling holder or sponsor is named in the supplied text; Part III is "incorporated by reference to our definitive proxy statement" | Insufficient Information | 10-K page:42, page:102 | Percentages and control rights are Not supplied; a dispersed base evidences no sponsor dividend recapitalisation risk, but nothing documents creditor protections or management ownership |
| Dividend policy | "We intend to continue paying regular cash dividends, although there can be no assurance"; quarterly dividends of 0.30 per share in fiscal 2025 and the first quarter of fiscal 2026, then 0.33 declared January 6, 2026 | Documentary Fact | 10-K page:42; Q1 10-Q page:19 | Willingness is documented and recurring; the dividend rose 10.0% (C4); the Credit Agreement covenants are described by management as not "a significant restriction on our ability... to pay dividends" (Q3 10-Q page:15), but the legal capacity under the unsupplied agreement is unverified |
| Share purchases | Fiscal 2025: 5.8 million shares at a cost of 456.6 million US dollars (cash flow 447,482 thousand); authorizations of 200 million in June 2024 and December 2024, 400 million in September 2025 and an increase in May 2026 to up to 400 million, with about 400.0 million available at June 30, 2026; nine months 2026: about 2.6 million shares at 192.4 million (cash flow 204,919 thousand) | Documentary Fact | 10-K page:93, page:66; Q3 10-Q page:19; CP-1 | Willingness is high: fiscal 2025 share purchases were 6.5 times dividends paid (C8; CP-1 shows 447,482 against 68,710 thousand). Feasibility depends on collections: nine-month free cash flow was an outflow of 208,615 thousand, so purchases were financed by borrowing (CP-1). Behaviour: Neutral or Mixed, shareholder-oriented and debt-funded, with no related-party leakage documented |
| Leverage policy | "The ratio remains within our target net leverage ratio of 2x to 3x" | Management Language | Q3 release page:4 | Management tolerates leverage up to 3x on the covenant definition from 2.00 today, so the stated policy leaves room for further leverage drift before any creditor-protective step; the 4.00 covenant maximum sits above that policy |
| Portfolio pruning | Divestitures of non-core Outside the U.S. businesses to reduce segment volatility, and the U.S. child support business in December 2025 | Documentary Fact | 10-K page:11, page:86; Q3 10-Q page:15 | Small proceeds (15.0 million for child support); reduces low-margin exposure; indemnification liability to the Australia and Korea buyer was 8,767 thousand at June 30, 2026 (CP-1) |
| Acquisitions | One small acquisition in the period: a vendor's IT services workforce for 18.0 million US dollars on February 14, 2024; the 2021 acquisition continues to carry 367.2 million of intangible assets supporting VA examination contracts | Documentary Fact | 10-K page:86; Q3 10-Q page:25 | Limited acquisition appetite is documented; the intangible carries impairment risk if the VA contracts change (management states the assets "may need to be adjusted") |
| Creditor-adverse actions | No priming, uptiering, drop-down, non-pro-rata exchange or collateral release is described in the supplied text; the Credit Agreement and indentures are not supplied | Insufficient Information | Searched sources | Absence of disclosure is not evidence of absence; legal capacity for such actions cannot be assessed without the agreement |
| Disclosure and controls | Internal control over financial reporting assessed effective at September 30, 2025; KPMG appointed auditor in 2024; the 10-K gives no reason for the change in the text read | Documentary Fact | 10-K page:100, page:63 | Controls are not a flagged weakness; the covenant EBITDA definition and add-backs are disclosed only in summary (CP-1) |
| Cybersecurity event | A "material cybersecurity incident" in the third quarter of fiscal 2023 through a third-party file transfer application; multidistrict litigation continues, the company is a bellwether defendant and has accrued "an amount within a range of possible outcomes" | Documentary Fact | 10-K page:39, page:96, page:97; Q3 10-Q page:21, page:22 | Contingent liability of unstated amount; adverse rulings could add cash outflow and contract risk with federal customers |
| Related parties | Item 13 is incorporated by reference to a proxy statement that is not supplied | Insufficient Information | 10-K page:102 | Related-party leakage cannot be assessed |

### Timeline

| Date | Event | Category | Locator | Note |
| --- | --- | --- | --- | --- |
| 1975 | Maximus, Inc. founded as a Virginia corporation | Documentary Fact | 10-K page:18 | Background |
| March 2023 | Sold the U.K. commercial practice (pre-tax loss 0.6 million) and the Swedish subsidiary | Documentary Fact | 10-K page:86 | Outside the U.S. pruning |
| Third quarter of fiscal 2023 | MOVEit-related cybersecurity incident disclosed; litigation consolidated in multidistrict proceedings from October 2023 | Documentary Fact | 10-K page:39, page:96, page:97 | Ongoing contingency |
| November 2023 | Sold the businesses in Italy and Singapore and the Canadian employment services business (loss 1.0 million) | Documentary Fact | 10-K page:86 | Outside the U.S. pruning |
| February 14, 2024 | Acquired part of an IT services vendor for 18.0 million US dollars | Documentary Fact | 10-K page:86 | Only acquisition in the period |
| Fiscal 2024 | KPMG LLP became auditor, succeeding Ernst & Young LLP | Documentary Fact | 10-K page:63, page:64 | Reason not stated in the text read |
| October and November 2024 | Subsidiary sued over a CMS solicitation for the Contact Center Operations contract; CMS cancelled the early reprocurement and the suit was dismissed without prejudice | Documentary Fact | 10-K page:98 | Contract retained, option periods to 2031 |
| December 2024 | Sold the Australia and Korea businesses for a nominal sum with up to 5.0 million of contingent consideration; divestiture-related charges of 39.5 million | Documentary Fact | 10-K page:86 | The charge sits in the nine-month fiscal 2025 comparatives (Q3 10-Q page:25) |
| Fiscal 2025 | Credit facility expanded by 250 million US dollars; 5.8 million shares purchased | Documentary Fact | 10-K page:51 | Debt-funded returns |
| July 4, 2025 | OBBBA enacted; Medicaid and SNAP provisions create demand drivers | Documentary Fact | 10-K page:17 | Timing depends on states |
| September 2025 | Board raised the repurchase authorization to up to 400 million US dollars | Documentary Fact | 10-K page:93 | Superseded two 200 million authorizations |
| November 20, 2025 | Fiscal 2025 10-K signed and filed | Documentary Fact | 10-K page:105 | Source date |
| December 2025 | Sold the U.S. child support business for about 15.0 million US dollars (annual revenue about 25.0 million; gain 10.1 million) | Documentary Fact | Q3 10-Q page:15 | Reduces U.S. Services scale |
| January 6, 2026 | Dividend of 0.33 per share declared, up from 0.30 | Documentary Fact | Q1 10-Q page:19 | Dividend raised |
| Second quarter of fiscal 2026 | 6.9 million capitalized software impairment after a client decision | Documentary Fact | Q3 10-Q page:28 | U.S. Services |
| Late May 2026 | Notification from a major customer of a temporary contractual modification | Documentary Fact | Q3 10-Q page:27 | Effective July 1, 2026 |
| May 2026 | Repurchase authorization increased to up to 400 million US dollars | Documentary Fact | Q3 10-Q page:19 | About 400.0 million available at June 30, 2026 |
| May 27, 2026 | Credit Agreement amended; Term Loan B increased by 325 million US dollars | Documentary Fact | Q3 10-Q page:15 | Terms not supplied |
| June 1, 2026 | New interest rate swap agreements effective on Term Loan A and Term Loan B | Documentary Fact | Q3 10-Q page:16 | Hedged notional 675,000 thousand (CP-1) |
| June 30, 2026 | Latest balance sheet date | Documentary Fact | Q3 10-Q page:5 | Period end |
| July 1, 2026 | Customer-directed modification takes effect (Subsequent event relative to the balance sheet) | Documentary Fact | Q3 10-Q page:27 | Runs through December 31, 2026 |
| July 6, 2026 | Dividend of 0.33 per share declared, payable August 31, 2026 (Subsequent event) | Documentary Fact | Q3 10-Q page:22 | About 17.3 million |
| After June 30, 2026 | 245 million US dollars collected from the delayed federal customer (Subsequent event) | Documentary Fact | Q3 10-Q page:31 | Further collections expected |
| August 6, 2026 | Fiscal Q3 10-Q and release issued; guidance lowered | Documentary Fact | Q3 10-Q page:39; Q3 release page:2 | Latest source |
| December 31, 2026 | Customer modification ends; OBBBA Medicaid provisions scheduled effective (future dates, labelled as such) | Documentary Fact | Q3 10-Q page:27; 10-K page:17 | States may request delays |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence or conflict |
| --- | --- | --- | --- | --- |
| Revenue durability | Backlog of 15,327 million US dollars with an average remaining life of about 5.0 years, and 60% of revenue from ten contracts (10-K page:49, page:50, page:19) | Long visibility comes from option periods that clients can decline, and almost all contracts allow termination for convenience (page:17) | Revenue is durable in aggregate but each large rebid is a binary event; leverage tolerance should be tested against the loss of a top contract | Backlog fell 5.2% (C2); conflict 3 below |
| Margin and cash-flow risk | Labor is about two-thirds of cost of revenue; performance-based work is 54.4% of revenue; days sales outstanding rose to 98 days (Q3 10-Q page:24, page:31; 10-K page:80) | Volume shortfalls on performance-based contracts hit margin before headcount adjusts, and delayed payments strand working capital for months | Free cash flow is back-end loaded; guidance requires 633,615 to 683,615 thousand of fourth-quarter free cash flow (CP-1), so liquidity is the near-term sensitivity | Q3 operating margin improved to 12.6% against 12.3% (Q3 10-Q page:24) |
| Concentration risk | About 55% of revenue from the U.S. federal government and about one-fifth from one agency (10-K page:18, page:19); a major customer's modification lowers EPS by about 0.35 per quarter (Q3 10-Q page:27) | A single customer's contractual or payment decision moves consolidated earnings and cash within a quarter | Earnings volatility is event-driven, not cyclical; the customer is unnamed, so exposure cannot be sized by contract | Conflict 2 below on the federal share definition |
| Sponsor alignment and capital allocation | No sponsor; buybacks of 447,482 thousand in fiscal 2025 and 204,919 thousand in nine months 2026 funded in part by credit facility expansions; leverage target 2x to 3x (10-K page:93; Q3 10-Q page:31; Q3 release page:4) | Management prefers shareholder returns to deleveraging while free cash flow is seasonal and negative until the fourth quarter | Leverage can drift toward 3x on the covenant definition, and the 4.00 maximum is looser than the policy; monitoring should track buybacks against collections | Conflict 1 below on the repurchase amount |
| Key uncertainties | Ownership percentages, Credit Agreement terms, amendment terms, contract-level detail and all events after August 6, 2026 are not supplied | Missing documents hide creditor protections, change-of-control terms and renewal dates | Any committee conclusion must carry these as open items | None |

### Conflicts logged

Conflicts are logged, not reconciled.

1. Share purchase amount for fiscal 2025. The 10-K MD&A says "We have utilized $447.5 million in fiscal year 2025 to purchase 5.8 million shares of our common stock" (10-K page:51) and the cash flow statement shows "(447,482)" (10-K page:66), while the equity note says "we purchased 5.8 million and 0.9 million of our common shares at a cost of $456.6 million and $73.1 million" (10-K page:93). The 10-K does not state the basis of the 456.6 figure (the nine-month 2026 text similarly gives "$192.4 million, which includes an additional charge from the 1% excise tax" against 204,919 thousand of cash in the cash flow statement, Q3 10-Q page:19). Effect: any analysis of capital returned must name which figure it uses.
2. U.S. federal share of revenue. The segment text says "Our U.S. Federal Services Segment generated 56% of our total revenue in fiscal year 2025" (10-K page:7), the risk factor says "approximately 55% of our total revenue was derived from the U.S. federal government" (10-K page:18) and the customer table shows 55.2% (10-K page:80). These are different definitions (segment, customer type) and the 10-K does not state which segment contracts are non-federal or which federal revenue sits in other segments. Effect: concentration should be quoted with its definition.
3. Outside the U.S. margin outlook. The 10-K says "We anticipate operating margins for the Outside the U.S. Segment in fiscal year 2026 to range between 3% to 5%" (10-K page:49) and the fiscal Q3 10-Q says "For fiscal year 2026, we anticipate a breakeven operating margin" (Q3 10-Q page:29). This is a change in management's outlook between filings, not a restatement. Effect: the segment's contribution to fiscal 2026 earnings is lower than the annual report implied.

### Consumer readiness

| Consumer | Readiness | What it should take from this module | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Business risk drivers (concentration, contract terminability, working-capital timing, customer modification), capital allocation behaviour (debt-funded buybacks, 2x to 3x leverage target), the three conflicts, and the absence of a sponsor | Business risk and governance determine how much weight the moderate leverage can bear | Ownership, Credit Agreement and contract detail are Not supplied; carry them as restrictions and do not infer creditor protections |
| CP-5 | READY_WITH_LIMITATIONS | Every row carries a category and a locator; Management Language rows are attributed; Insufficient Information rows state the missing datapoint | Independent review needs the category to separate fact from management claim | Check the three logged conflicts, especially the share purchase amounts and the federal revenue definitions, against the cited pages |

### Reconciliation to upstream handoffs

- CP-0 and CP-1 are consistent with this module on identity, periods and financing structure. CP-1 listed the May 27, 2026 amendment's terms as Not supplied; that is unchanged here.
- CP-1 recorded the nine-month share repurchase cost as 192.4 million including excise tax against a cash flow of 204,919 thousand and said the sources do not reconcile the two; this module logs the same pattern for fiscal 2025 (conflict 1) and does not reconcile it.
- CP-1 stated that Outside the U.S. is expected to break even for fiscal 2026 (Q3 release page:3); this module adds the earlier 3% to 5% outlook in the 10-K (conflict 3). Nothing in CP-0 or CP-1 is corrected.

## Calculations

All amounts are in the units printed. Inputs are cited printed figures or CP-1 figures.

- C1. Backlog to revenue: backlog 15,327 million US dollars (10-K page:49) / fiscal 2025 revenue 5,431.276 million (10-K page:64) = 2.82.
- C2. Backlog change: 15,327 / 16,167 − 1 = −5.2%. By segment: U.S. Federal Services 9,780 / 10,286 − 1 = −4.9%; U.S. Services 3,916 / 3,867 − 1 = 1.3%; Outside the U.S. 1,631 / 2,014 − 1 = −19.0% (10-K page:49).
- C3. Segment revenue shares of fiscal 2025 revenue of 5,431,276 thousand (10-K page:78): U.S. Federal Services 3,067,691 / 5,431,276 = 56.5%; U.S. Services 1,763,691 / 5,431,276 = 32.5%; Outside the U.S. 599,894 / 5,431,276 = 11.0%. The 10-K prints 56%, 32% and 11%. State and local agencies: 1,764,683 / 5,431,276 = 32.5% (10-K page:80).
- C4. Dividend change: 0.33 / 0.30 − 1 = 10.0% (Q1 10-Q page:19; 10-K page:42).
- C5. Employee tie-out: 15,000 + 13,600 + 6,900 + 1,700 = 37,200, equal to the printed total (10-K page:13).
- C6. Revenue effect of divestitures in the nine months: disposal of businesses (34,588) thousand, 0.8% of the prior-year nine-month revenue 4,112,861 thousand (Q3 10-Q page:25): 34,588 / 4,112,861 = 0.8%.
- C7. Clinical services share change: 38.7% in fiscal 2025 against 30.3% in fiscal 2023, a rise of 8.4 percentage points (10-K page:80).
- C8. Fiscal 2025 share purchases to dividends paid: 447,482 / 68,710 = 6.5 (CP-1; 10-K pages:65, 66).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Proxy statement not supplied: beneficial ownership percentages, board composition, management ownership and related-party transactions are Not supplied | High | CP-2, CP-5 | Supply the 2026 proxy statement |
| Credit Agreement, amendment terms, guarantor entities and change-of-control provisions not supplied | High | CP-2 | Supply the executed agreement and amendment |
| Contract-level detail for the ten largest contracts and the identity of the customer behind the modification are not supplied; the 10-K names CMS, the VA and the Department of Education only as program examples | High | CP-2 | Supply contract and recompete schedules or later disclosure |
| Backlog after September 30, 2025 and any book-to-bill measure are not supplied | Medium | CP-2 | Supply the fiscal 2026 10-K |
| All events from August 7, 2026 to the cutoff, including fiscal Q4 results, are not supplied | High | CP-2, CP-5 | Supply later filings or confirm none exist |
| The full-year earnings effect of the customer modification: the 10-Q gives about 0.35 of diluted EPS per quarter (Q3 10-Q page:27) and the releases give revised full-year ranges (adjusted diluted EPS 7.90 to 8.20 in August against 8.25 to 8.55 in May, Q3 release page:2; Q2 release page:4), with no bridge between them | Medium | CP-2 | Treat the two as separate attributed figures until a bridge is supplied |
| Reason for the 2024 auditor change, the date and terms of the fiscal 2025 credit facility expansion, and the use of proceeds of the May 2026 amendment beyond management's general statement are not supplied | Low | CP-2 | Supply the related 8-K filings |
| MOVEit litigation accrual amount and insurance recovery are not printed | Medium | CP-2 | Carry as an unquantified contingency |
| Releases are attributed management claims; earnings presentations are not supplied | Low | CP-5 | Supply decks if needed |
| Text extraction only; original HTML and images are not supplied | Low | CP-5 | Check flagged tables against filed HTML |

## Next module

- CP-2: use the business risk drivers, concentration facts and capital allocation rows with the CP-1 leverage, liquidity and covenant figures. Quote management claims as attributed, keep the three conflicts visible and carry the proxy, Credit Agreement and contract-detail gaps as restrictions. Treat fourth-quarter collections and the customer modification through December 31, 2026 as the central sensitivities.
- CP-5: trace each category-tagged row to its cited page; check conflicts 1 to 3 against the pages named, and keep the extraction-only limit visible.
