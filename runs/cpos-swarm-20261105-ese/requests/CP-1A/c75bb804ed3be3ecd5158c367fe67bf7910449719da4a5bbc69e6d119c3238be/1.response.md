# CP-1A business and transaction context: ESCO TECHNOLOGIES INC (ese)

## Request

- Issuer: ESCO TECHNOLOGIES INC (issuer id `ese`, NYSE: ESE), consolidated with its subsidiaries, as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run `ese-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This is CP-1A. Its consumers are CP-2 and CP-5. Upstream handoffs: CP-0 (source readiness) and CP-1 (financial base).
- Execution: host session. The host read the pinned sources and wrote this answer. No provider was called.
- Periods: ESCO's fiscal year ends September 30 (10-K page:6 "Our fiscal year ends September 30."). Q3 2026 is the quarter ended June 30, 2026, FY2025 the year ended September 30, 2025. Currency is USD.
- Reader question: which transaction, business, ownership and operating facts matter most to a creditor, and what does the supplied evidence not show?
- Constraints carried from CP-0 and CP-1: the 10-K and 10-Qs control over the releases; the Megger purchase agreement, the shareholder agreement, the May 29, 2026 credit agreement, the 2025 Proxy Statement, rating reports and any filing dated after August 10, 2026 are Not supplied. The context carries no sponsor, parent, guarantor, rating or deal-term entries, which is not evidence that none exist.
- No peer ranking, no instrument recommendation and no recovery conclusion is given.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Use |
| --- | --- | --- |
| 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | fe80d5d10f35aaa7f1b7aa40e6d69aeaea7f501fabdde619947c03aa0fe69d71 | Business, segments, customers, backlog, history, acquisitions, officers, risk factors |
| 10-Q_2025-12-31_ese-20251231x10q.htm.jsonl | 028e0b9aec25ecf720ca796f0beef13fd8b40ddc333348a8ba8153fe3b16e523 | Q1 2026 debt wording |
| 10-Q_2026-03-31_ese-20260331x10q.htm.jsonl | d207365eeea17e17e69c10625b481ddba582ee4861f7a9c60376e4bd5dffc806 | Megger subsequent event, debt wording |
| 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | 056428009193705ead08cb6828be9f20a62a9323946644ad69e280efbf618711 | Megger terms, New Credit Facility, segments, exhibits |
| EX-99.1_2026-01-30_tm264950d1_ex99-1.htm.jsonl | 73c00c863e8360707e7681c62537391b693f1632ac470f63ec94b54622dbc238 | Q1 2026 release (management narrative) |
| EX-99.1_2026-05-07_tm2613615d1_ex99-1.htm.jsonl | 4483c93985a6b3ea98a959d8659fafa040f3230850186662a7c5bb7c5d2d8a1d | Q2 2026 release (Megger status, guidance) |
| EX-99.1_2026-08-06_tm2621646d1_ex99-1.htm.jsonl | f683102e1a6a6e74cee756fd0639a64a1d810e0d5fd17fcb2dc502f25f716fb6 | Q3 2026 release (Megger status, segment commentary, guidance) |

### Other inputs

| Input | sha256 | Use |
| --- | --- | --- |
| context (`contexts/866706-esco-technologies-inc-ese.json`) | da65696ce609dcf19999b44c58b8a10f43f7d7bc7cde7c4a3762d76affdde214 | Run settings; sector label and ticker only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 7f46d3b1dbdad4b468a5bdd5db37f408dc8a1ce57aba77ff195a116822899d17 | Source readiness and gap list |
| CP-1 | 23a50d14b3104c2571d80147c88f81427457a9b11a2aa773f3459c4d026de1e7 | Financial base: debt, liquidity, leverage, cash flow, claims outside debt |

### Labels and locators

Locators are `page:N` of the pinned text files. "10-K" is the FY2025 10-K; "10-Q Q1", "10-Q Q2" and "10-Q Q3" are the 10-Qs for the quarters ended December 31, 2025, March 31, 2026 and June 30, 2026; "Release Q1", "Release Q2" and "Release Q3" are the EX-99.1 releases dated February 5, May 7 and August 6, 2026. Figures taken from CP-1 are marked "CP-1". Fact categories are Documentary Fact, Management Language, Analyst Interpretation and Insufficient Information.

CP-1 consistency: this module uses the CP-1 debt, liquidity and claims figures unchanged and does not correct CP-1. It adds one document conflict CP-1 did not log, on the wording of the $20 million current portion of debt (see Conflicts).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| ESCO is a listed, sponsor-free aerospace, utility-testing and RF-testing group with a large backlog. Its pending Megger acquisition, with equity valued at about $1.4 billion and cash of $0.9 billion, is the main change for creditors. | Medium | The purchase agreement, shareholder agreement, new credit agreement and proxy statement are not supplied, so control, terms and post-closing structure cannot be sourced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Three segments serve aerospace and defense, electric utilities and RF testing; the US Government accounted for approximately 23% of fiscal 2025 revenue and no customer exceeded 10%. | Spread across segments, but defense budget and program timing risk is concentrated in aerospace and defense. | High |
| Backlog was $1,540.5 million at June 30, 2026, with approximately 59% expected to convert to revenue in the next twelve months. | Provides near-term revenue visibility, though contract termination for convenience limits certainty. | Medium |
| Megger, a named competitor of the utility segment, is to be bought from TBG AG for approximately $2.35 billion, and TBG AG will sign a shareholder agreement. | The equity issuance changes the shareholder base; TBG AG's stake and governance rights are not supplied. | Medium |
| Documented capital allocation since fiscal 2025 shows debt paydown after the VACCO sale and a small dividend, with no share repurchases and no creditor-adverse actions in the sources. | Behaviour to date is creditor-supportive, but the pending acquisition raises leverage tolerance questions. | Medium |
| The existing $500 million revolving facility and term loan A are to be replaced by new $500 million revolver and two $500 million term loans at closing. | Maturities and covenants will reset; terms are not supplied, so refinancing risk cannot be assessed. | Medium |

### Business and transaction view

ESCO is a publicly listed group with no sponsor or parent named in the context or the filings; material US subsidiaries guarantee the bank facility (10-K page:80). It reports three segments: Aerospace & Defense (A&D), Utility Solutions Group (USG) and RF Test & Measurement (Test). A&D has grown from 34% of continuing revenue in 2023 to 44% in 2025, reflecting Navy growth and the Maritime acquisition, which makes the group more dependent on US and UK naval programs and on government funding. The group sold its Space business (VACCO) in July 2025 and used the proceeds mainly to repay debt, so fiscal 2025 and the first nine months of fiscal 2026 show deleveraging rather than distributions.

The transaction that matters is the pending purchase of Megger Group Limited from TBG AG, signed April 15, 2026, with total consideration of approximately $2.35 billion, of which approximately $0.9 billion is cash and approximately $1.4 billion is ESCO equity. Megger, which the 10-K lists as a competitor of the USG segment, will join USG. The cash part is to be funded from cash and incremental debt, with a new $1.5 billion committed facility set agreed on May 29, 2026 that is effective only on closing. Closing was expected in the first quarter of fiscal 2027, which began October 1, 2026, so by the 2026-11-05 as-of date the transaction may have closed. No supplied source is dated after August 10, 2026, so closing status, the debt actually drawn and the size of TBG AG's resulting stake are Not supplied.

For a creditor the view is that the operating base is diversified and well covered by backlog, but the credit story is now event driven. The equity component limits the cash leverage needed, yet it creates a new significant shareholder whose agreement terms are unknown, and Megger's earnings and its effect on leverage are Not supplied. Evidence quality is High for ESCO's own filed facts and Low for anything about Megger beyond the purchase terms summarised in the 10-Q Q3.

### Company and operating model

| Dimension | Description | Evidence and locator | Category | Risk mechanic and credit implication |
| --- | --- | --- | --- | --- |
| A&D segment | Specialty filtration and fluid control, signature reduction, naval power management, machined components, miniature electro-explosive devices for aerospace and defense; about 44% of fiscal 2025 continuing revenue (34% in 2023) | 10-K page:7 "The A&D segment accounted for approximately 44%, 37% and 34% of our total revenue from continuing operations in 2025, 2024 and 2023, respectively."; 10-K page:8 | Documentary Fact | Navy and aerospace programs are long cycle and funded by government budgets; growth is partly acquired (Maritime), so organic durability is less certain |
| USG segment | Doble diagnostic testing and data for electric utilities; NRG decision tools for wind and solar; about 35% of fiscal 2025 revenue (40% in 2023) | 10-K page:8 "Our USG segment accounted for approximately 35%, 40% and 40% of our total revenue from continuing operations in 2025, 2024 and 2023, respectively." | Documentary Fact | Utility spend is steadier, but NRG depends on renewables demand: orders fell with the expiry of tax credits (Release Q3 page:2 "related to the expiration of U.S. renewables tax credits"). Megger will be added here |
| Test segment | ETS-Lindgren RF test and measurement, shielding and filters; about 21% of fiscal 2025 revenue | 10-K page:9 "Our Test segment accounted for approximately 21%, 23% and 26% of our total revenue from continuing operations in 2025, 2024 and 2023, respectively." | Documentary Fact | Project-based and exposed to electronics and wireless cycles; smallest segment and falling in mix |
| Customers and concentration | US Government direct and indirect sales were approximately 23% of fiscal 2025 revenue, primarily A&D; no customer exceeded 10% | 10-K page:9 "accounted for approximately 23%, 20% and 17% of our total revenue from continuing operations in 2025, 2024 and 2023, respectively"; 10-K page:86 "No customer exceeded 10% of consolidated sales in 2025, 2024 or 2023." | Documentary Fact | No single commercial customer risk, but government share has risen and contracts are terminable |
| Contract terms | Government prime contracts and nearly all subcontracts may be terminated at the Government's convenience; contracts include cost-plus and fixed-price | 10-K page:10 "All Government prime contracts and virtually all of our Government subcontracts provide that they may be terminated at the convenience of the Government or the customer." | Documentary Fact | Backlog is not a guarantee of revenue; fixed-price contracts expose margins to cost overruns (10-K page:18) |
| Revenue recognition and visibility | About 48% of A&D revenue is recognised over time; USG is mostly point in time; Test uses milestones | 10-K page:41 "Approximately 48% of the A&D segment’s revenue (21% of consolidated revenue) is recognized over time"; 10-K page:64 | Documentary Fact | Over-time recognition and customer progress payments drive contract assets and liabilities, so operating cash flow depends on billing timing (CP-1) |
| Backlog | Total backlog $1,540.5 million at June 30, 2026, with approximately 59% expected in the next twelve months | 10-Q Q3 page:16 "the Company had $1,540.5 million in remaining performance obligations of which the Company expects to recognize revenues of approximately 59% in the next twelve months" | Documentary Fact | Strong visibility; backlog excludes unexercised options and IDIQ potential (same page) |
| Geography | International customers were approximately 34% of fiscal 2025 revenue; US facilities dominate A&D | 10-K page:9 "Our sales to international customers accounted for approximately 34%, 31% and 33% of our total revenue from continuing operations in 2025, 2024 and 2023, respectively." | Documentary Fact | Currency and trade-policy exposure, including sanctions and tariffs named in risk language (10-K page:19) |
| Cost structure and suppliers | Several sole-source components and raw materials such as aerospace-grade titanium and helium; USG relies on contract manufacturers | 10-K page:12 "certain components and raw materials are supplied by sole source vendors" | Documentary Fact | Supply interruptions can delay deliveries and compress margin; no supplier concentration figures supplied |
| Pricing and margin | Segment commentary cites price increases and volume leverage, offset by inflation | Release Q3 page:2 "driven by leverage on higher volume and price increases, partially offset by inflationary pressures and unfavorable mix" | Management Language | Management attribution; margin durability not independently tested here |
| Capital spending and working capital | Capital spending and software investment are modest relative to operating cash flow; working capital swings with contract billings | CP-1 financial base; 10-Q Q3 page:24 "Contract liabilities increased $71.5 million primarily within the A&D segment (Globe and Maritime) due to timing of payments received from customers." | Analyst Interpretation | Customer advances flatter operating cash flow and can reverse |
| Business model risk | Government funding risk is named first in the risk factors | 10-K page:17 "Restrictions in authorized U.S. Government defense spending or changes in acquisition priorities could negatively impact our financial position and result of operations." | Documentary Fact | A budget shock would hit A&D, the largest and fastest-growing segment |

### Company profile

| Attribute | Value | Evidence and locator | Category |
| --- | --- | --- | --- |
| Legal name and ticker | ESCO Technologies Inc., NYSE: ESE | 10-Q Q3 page:1 "ESCO TECHNOLOGIES INC." | Documentary Fact |
| Country and incorporation | United States; incorporated in Missouri; headquartered in St. Louis, Missouri | 10-K page:1 "Missouri"; 10-K page:1 "St. Louis, Missouri" | Documentary Fact |
| Sector | Context label "Communications Equipment, NEC"; the filings describe aerospace and defense, utility diagnostics and RF test, so the label is a classification code, not a business description | context; 10-K page:5 "A global provider of highly engineered components and systems for aviation, Navy, defense and industrial customers" | Analyst Interpretation |
| Fiscal year end | September 30 | 10-K page:6 | Documentary Fact |
| Employees | 3,425 persons at September 30, 2025, 28% outside the USA | 10-K page:14 "we employed 3,425 persons, including 3,359 full time employees" | Documentary Fact |
| Facilities | A&D: nine in the US, two in the UK, one in Mexico; USG: eight in the US, one in Canada, ten elsewhere; Test: five in the US, eight outside | 10-K pages:7 to 9 | Documentary Fact |
| Ownership | Publicly traded; about 1,894 holders of record at November 14, 2025; shares outstanding 25,907,567 at July 31, 2026; no controlling holder or sponsor named | 10-K page:31 "approximately 1,894 holders of record"; 10-Q Q3 page:1 "25,907,567" | Documentary Fact |
| Beneficial ownership detail | Not supplied: Part III is incorporated from the 2025 Proxy Statement, which is not in the pack | 10-K page:47 "hereby incorporated by reference" | Insufficient Information |
| Management | Bryan H. Sayler, President and CEO since January 1, 2023; Christopher L. Tucker, SVP and CFO since April 2021 | 10-K pages:16 to 17 "President and Chief Executive Officer since January 1, 2023"; "Senior Vice President and Chief Financial Officer since April 2021" | Documentary Fact |
| Auditor | Grant Thornton LLP, auditor since 2021; unqualified opinion on FY2025 statements; ICFR opinion excludes Maritime | 10-K page:55 "We have served as the Company’s auditor since 2021."; 10-K page:56 | Documentary Fact |
| Credit ratings | Not supplied: the context lists none and no rating report is in the pack | context | Insufficient Information |
| Debt facilities | Bank facility only (revolver and term loan A); no notes or bonds in the debt table; security and guarantors per the 10-K | CP-1; 10-Q Q3 page:10 | Documentary Fact |

### Transaction summary and new debt issues

The pending transaction is the acquisition of Megger Group Limited from TBG AG. On April 15, 2026 ESCO signed a definitive agreement: 10-Q Q3 page:19 states "ESCO will acquire Megger for total consideration of approximately $2.35 billion, consisting of $0.9 billion in cash and ESCO equity valued at approximately $1.4 billion." The agreement is a share purchase agreement (10-Q Q3 page:30 "for the sale and purchase of the share capital of Megger Group Limited") with a Form of Shareholder Agreement to be executed concurrently with completion. The cash and equity components are each stated as approximate and do not sum to the stated total; the filing does not explain the difference, and it is logged below, not reconciled.

Status and timing. The transaction was signed after the March 31, 2026 balance sheet date and was reported as a "Subsequent Event" in the 10-Q Q2 (page:24). Management states that "All filings for regulatory approval are underway" and expects closing in the first quarter of fiscal 2027 (Release Q3 page:3 and 10-Q Q3 page:19). Whether approvals were received and whether it has closed by 2026-11-05 is Not supplied.

Financing and new debt. The cash portion "will be funded through existing cash on hand and incremental debt, with committed financing in place" (10-Q Q3 page:19). On May 29, 2026 ESCO and certain subsidiaries entered into a Credit Agreement, the New Credit Facility, with JPMorgan Chase Bank, N.A. as administrative agent. It provides a senior secured revolving credit facility of $500 million, a senior secured term loan A of $500 million and a senior secured term loan B of $500 million. It becomes effective only on, and substantially concurrently with, closing and replaces the Existing Credit Facility. The revolver and term loan A mature five years after the effective date and term loan B seven years after (10-Q Q3 page:12). Foreign subsidiaries may also draw. No notes, bonds or other capital-markets debt issue is described in any supplied source. The credit agreement is Exhibit 10.3 to the 10-Q Q3 and was filed with the Form 8-K of June 3, 2026 (10-Q Q3 page:30); it is not in the pack, so pricing, covenants, conditions to effectiveness, guarantors and collateral are Not supplied.

Ownership effect. The equity component means ESCO will issue shares to TBG AG at completion. The number of shares, the resulting percentage ownership, lock-up terms, board or consent rights and any standstill under the shareholder agreement are all Not supplied. No percentage is inferred here.

Use of proceeds and liquidity effect. Proceeds fund the purchase price; fees, expenses and any refinancing of the Existing Credit Facility are not itemised in the supplied sources. CP-1 shows $85.0 million of borrowings and $73.2 million of cash at June 30, 2026 before the transaction, and an illustrative bound of 3.22x on ESCO-only EBITDA if the full $0.9 billion were borrowed (CP-1, Analyst Inference, not a forecast). Megger financials are Not supplied, so the actual pro forma leverage and liquidity cannot be stated.

Costs already incurred. Approximately $7 million of debt financing costs were expensed in Q3 2026 interest expense (10-Q Q3 page:23), and acquisition costs at Corporate are excluded from adjusted EPS (Release Q3 page:6 "$0.20 of debt financing and $0.19 of acquisition costs"). These are Documentary Fact; they show the financing was committed before the 10-Q Q3 period end.

Creditor mechanics. A large acquisition funded partly by new term debt replaces an $85.0 million drawn facility with up to $1.5 billion of committed capacity (three tranches of $500 million, see Calculations). The creditor question is leverage tolerance, covenant terms and the term loan B tenor. Willingness is evidenced by the committed financing and the signed agreement; legal capacity (what the new agreement permits) and feasibility (post-closing cash flow of the combined group) are not shown.

Earlier financing for context: the Maritime acquisition in April 2025 for a cash purchase price of approximately $472 million, net of cash acquired (10-K page:74), was partly funded by the Incremental Facility (10-K page:80), which is the term loan A now outstanding.

### Ownership, governance and sponsor behaviour

| Item | Evidence | Category | Mechanic and implication |
| --- | --- | --- | --- |
| No sponsor, parent or controlling shareholder named | Context sponsor and parent blank; 10-K cover shows non-affiliate market value computed with the assumption that 13D/13G filers are not affiliates (10-K page:2) | Insufficient Information | Cannot confirm absence of a large holder; beneficial ownership is in the unsupplied proxy |
| Debt-funded distributions or dividend recapitalisation | None documented. Dividend $0.08 per share quarterly, $2.1 million each (10-Q Q3 page:25) | Documentary Fact | Distributions are small relative to cash flow (CP-1) |
| Share repurchases | None in 2025; none in Q3 2026 (10-K page:81 "We did not repurchase any shares in 2025"; 10-Q Q3 page:29 "The Company did not repurchase any shares during the third quarter of 2026."). A program of up to $200 million over three years to September 30, 2027 exists (10-K page:81) | Documentary Fact | Authorisation could be used after closing; capacity is limited by the credit agreements |
| Use of divestiture proceeds | VACCO proceeds: "used the proceeds from the sale to primarily pay down debt" (10-K page:32) | Documentary Fact | Deleveraging behaviour, supportive of creditors |
| Creditor-adverse actions (priming, uptiering, drop-downs, non-pro-rata exchanges, collateral release) | None found in the supplied sources | Insufficient Information | Absence in these sources is not proof; credit agreements are not supplied |
| Related parties | Two directors are officers at two customers of Doble; sales approximately $1.7 million and $3.9 million for three and nine months to June 30, 2026 on normal terms (10-Q Q3 page:18) | Documentary Fact | Small and disclosed; board deemed independence unimpaired |
| Controls | ICFR effective at September 30, 2025, with Maritime excluded from the audit scope (10-K page:56); disclosure controls effective at June 30, 2026 (10-Q Q3 page:29) | Documentary Fact | Recently acquired business not yet in tested scope at year end; the same will apply to Megger |
| Incoming shareholder | TBG AG shareholder agreement to be executed at completion (10-Q Q3 page:30) | Insufficient Information | Control rights unknown |

Behaviour category (issuer level, documented actions only): Supportive for the periods supplied, based on debt paydown after the VACCO sale, modest dividends, no buybacks and regular reporting. It is Insufficient Information for the post-closing period. Legal capacity, willingness and feasibility are kept separate: capacity under the existing agreement is Not supplied, willingness is evidenced by past actions, feasibility is shown by liquidity in CP-1.

### Timeline

| Date | Event | Locator | Category |
| --- | --- | --- | --- |
| January 1, 2023 | Bryan H. Sayler became President and CEO | 10-K page:16 | Documentary Fact |
| February 2023 | Acquired CMT Materials, LLC and Engineered Syntactic Systems, LLC | 10-K page:7 | Documentary Fact |
| August 30, 2023 | Amended and Restated Credit Agreement | 10-Q Q3 page:30 | Documentary Fact |
| November 9, 2023 | Acquired MPE Limited for approximately $56.2 million net of cash | 10-K page:76 | Documentary Fact |
| August 5, 2024 | Amendment No. 1: delayed-draw incremental term loan up to $375 million | 10-K page:80 | Documentary Fact |
| April 25, 2025 | Acquired Maritime for approximately $472 million net of cash | 10-K pages:6 and 74 | Documentary Fact |
| July 18, 2025 | Completed sale of VACCO for net proceeds of approximately $270 million | 10-K page:32 | Documentary Fact |
| December 1, 2025 | FY2025 10-K signed | 10-K page:51 | Documentary Fact |
| Q2 2026 | Paid approximately $59 million of cash taxes on the VACCO gain | 10-Q Q3 page:25 | Documentary Fact |
| April 15, 2026 | Megger share purchase agreement signed (Subsequent event to the March 31, 2026 balance sheet) | 10-Q Q2 page:24; 10-Q Q3 page:19 | Documentary Fact |
| May 29, 2026 | New Credit Facility signed, effective on Megger closing | 10-Q Q3 page:12 | Documentary Fact |
| June 3, 2026 | Form 8-K filed with the credit agreement as Exhibit 10.1 | 10-Q Q3 page:30 | Documentary Fact |
| July 17, 2026 | Dividend paid, after the June 30, 2026 period end (Subsequent event to that balance sheet) | 10-Q Q3 page:25 | Documentary Fact |
| August 6 and 10, 2026 | Q3 release and 10-Q Q3 | Release Q3 page:1; 10-Q Q3 page:31 | Documentary Fact |
| First quarter of fiscal 2027 | Expected Megger closing (a forward-looking management expectation, not an event) | Release Q3 page:3 | Management Language |
| After August 10, 2026 | Not supplied | n/a | Insufficient Information |

No rating event, regulatory event other than the pending approvals, or refinancing other than the above appears in the supplied sources.

### Conflicts and document differences

| Topic | Span 1 | Span 2 | Downstream effect |
| --- | --- | --- | --- |
| Megger consideration components | 10-Q Q3 page:19 "total consideration of approximately $2.35 billion" | 10-Q Q3 page:19 "$0.9 billion in cash and ESCO equity valued at approximately $1.4 billion" | The stated parts do not add to the stated total on their face. Rounding or other consideration is not explained. Logged, not reconciled; CP-2 must use the stated figures as management's |
| Current portion of debt | 10-Q Q1 page:9 "however, the Company has no contractual obligation to repay such amount during the next twelve months" | 10-Q Q3 page:11 "as obligated by the repayment terms of the Incremental Facility within the next twelve months" | The wording moved from voluntary to obligated between Q1 2026 and Q2 2026. The amendment or schedule behind it is not supplied. Logged, not reconciled; affects how CP-2 reads the maturity profile |
| Contract liabilities | 10-Q Q3 page:16 "$293.4 million" in the note | Balance sheet caption on 10-Q Q3 page:3 (288,142 thousand) | Presentation difference carried from CP-0 and CP-1 |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Countering conflict or limit |
| --- | --- | --- | --- | --- |
| Revenue durability | Backlog $1,540.5 million with approximately 59% in twelve months (10-Q Q3 page:16); US Government approximately 23% of revenue (10-K page:9) | Backlog converts to revenue on production and billing schedules; government contracts are terminable for convenience, and over-time recognition ties revenue to cost incurred | Supports near-term revenue visibility and debt service, but a budget or program shock concentrated in A&D would weigh on the largest segment | Termination for convenience (10-K page:10); backlog excludes options |
| Margin and cash-flow risk | Fixed-price contract risk (10-K page:18); working capital inflow from customer advances (10-Q Q3 page:24); CP-1 notes the nine-month discontinued tax outflow | Cost overruns reduce margin; advances reverse as projects deliver | Operating cash flow in the supplied period may overstate a normal level; free cash flow should be read with CP-1 caveats | Contract liabilities presentation difference |
| Concentration | USG and Test are commercial; A&D is government dominated; Megger would add to USG | Mix shifts toward A&D and, after closing, toward utility testing; Megger is a named competitor of the USG segment (10-K page:13) | Joins the USG segment with a named competitor, which can strengthen market position but adds integration risk | Megger financials not supplied |
| Sponsor and shareholder alignment | No sponsor; modest dividend; no buybacks; debt paid down with divestiture proceeds | Management behaviour has favoured balance sheet strength | Behaviour to date is supportive; TBG AG becomes a shareholder of unknown weight | Shareholder agreement not supplied |
| Key uncertainties | Pending closing, unknown pro forma leverage, unseen credit agreement | Debt rises from a low base to a level that depends on the amount drawn under the term loans | Leverage tolerance and covenant terms are the central credit questions; monitoring needs the executed agreements | Illustrative bound in CP-1 is Analyst Inference |

### Consumers

| Module | Readiness | Take from CP-1A | Why it matters | Gap | Action |
| --- | --- | --- | --- | --- | --- |
| CP-2 | Ready with limitations | Transaction terms, segment mix, backlog, governance behaviour, conflicts, and the facts that the post-closing structure and ownership are Not supplied | The credit synthesis must describe an event-driven structure without inventing post-closing figures | Agreements, Megger financials, closing status, proxy | Mark pro forma leverage, covenant terms and TBG AG stake as Not supplied; carry the two logged conflicts |
| CP-5 | Ready with limitations | Fact table with locators and categories, so each claim can be traced | The evidence review needs the category and locator for every row | Management Language rows (guidance, pricing commentary) are attributed claims | Test Management Language rows against the 10-K and 10-Q; confirm quotes by page |

### Monitoring gaps

| Missing item | Severity | Why it matters |
| --- | --- | --- |
| Megger purchase agreement, shareholder agreement and 8-Ks of April 15 and 16, 2026 | High | Conditions, termination rights, TBG AG governance and lock-up terms |
| May 29, 2026 Credit Agreement | High | Pricing, covenants, guarantors, collateral, amortisation |
| Existing Amended and Restated Credit Agreement and Amendment No. 1 | High | Covenant levels, baskets, restricted payments |
| Megger financial statements and pro forma information | High | Combined leverage and coverage |
| Debt schedule beyond the debt note, maturity schedule, covenant certificate | Medium | Maturity timing, headroom |
| 2025 Proxy Statement | Medium | Board, director independence, beneficial ownership |
| Filings after August 10, 2026 | High | Closing status and drawn amounts |
| Add-back bridge for adjusted EBITDA | Medium | Releases give adjusted measures; the full bridge to a lender definition is Not supplied |
| Rating reports | Low | None supplied; context blank |

## Calculations

One simple sum: the New Credit Facility commitments are $500 million + $500 million + $500 million = $1.5 billion (10-Q Q3 page:12). Otherwise CP-1A does not compute figures. Every other number is quoted from a located source or taken unchanged from CP-1, with the period each source gives. Also checked: the stated Megger components $0.9 billion + $1.4 billion = $2.3 billion, against the stated total of approximately $2.35 billion (see Conflicts). The only derived item mentioned, the 3.22x illustrative bound, is CP-1's own calculation (CP-1 Calculations: 85,000 + 900,000 = 985,000 divided by LTM EBITDA of 305,677), and it is labelled Analyst Inference there.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Megger purchase agreement, shareholder agreement and the April 15, April 16 and June 3, 2026 8-Ks not supplied | High | CP-2, CP-5 | Supply the 8-Ks with exhibits |
| May 29, 2026 Credit Agreement terms not supplied | High | CP-2 | Supply Exhibit 10.3 to the 10-Q Q3 |
| TBG AG resulting stake, governance rights and lock-up not supplied | High | CP-2 | Supply the shareholder agreement and any registration or proxy materials |
| Megger financials and pro forma data not supplied | High | CP-2 | Supply Megger statements or pro forma information |
| Closing status and events after August 10, 2026 not supplied | High | CP-2, CP-5 | Supply later 8-Ks or confirm none |
| Consideration components do not add to the stated total, unexplained | Medium | CP-2 | Obtain the 8-K of April 15, 2026 |
| Current-portion wording changed between Q1 2026 and Q2 2026, schedule not supplied | Medium | CP-2 | Supply Amendment No. 1 and any later amendment |
| 2025 Proxy Statement not supplied: board, independence, beneficial ownership not shown | Medium | CP-2 | Supply the proxy |
| No rating reports; context blank | Low | CP-2 | Not required for the minimum set |
| Management Language rows (guidance, pricing, margin commentary) rest on releases only | Low | CP-5 | Treat as attributed claims |
| No sponsor or parent in context; filings name none; absence of a large holder not shown | Low | CP-2 | Check the proxy |

## Next module

- CP-2: use the CP-1 figures for the reported base and this module for business, transaction and governance context. Describe the Megger transaction as signed and pending with closing expected in the first quarter of fiscal 2027; do not state post-closing leverage, interest cover, covenant headroom or TBG AG ownership as known. Carry the two logged conflicts (consideration components, current-portion wording) and the Supportive behaviour category with its limits. Keep recovery prospects as a mechanic only.
- CP-5: trace each fact row by locator and category; confirm each quote on its page; test the Management Language rows and the attributions to releases against the 10-K and 10-Qs; note that the TBG AG, covenant and Megger items are Not supplied rather than adverse.
