# CP-1A Business and transaction context: CENTENE CORP (cnc)

## Request

- Issuer: CENTENE CORP (issuer id `cnc`), registrant "CENTENE CORPORATION", as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; amounts are USD millions unless a row says otherwise.
- Run `cnc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This handoff feeds CP-2, CP-5 and the report sections "Company and operating model", "Company profile" and "Transaction summary and new debt issues".
- Execution: host session; no provider call. Figures that also appear in CP-1 carry the same value, period and unit as CP-1. This module calculates nothing new.
- Question: which transaction, ownership, business and operating facts matter most to the creditor, and what governance behaviour is documented?
- Fact categories used in tables: Documentary Fact (the source states it), Management Language (management characterisation, quoted and qualified), Analyst Interpretation (this analyst's reading of cited evidence), Insufficient Information (evidence missing; a gap, never an adverse conclusion).
- Locators are `page:N` chunk numbers of the pinned extracts. Short names are defined in `## Sources`. Nothing here comes from outside the supplied sources.

## Sources

### Issuer sources relied on

| Short name | Exact source name | sha256 (pinned file) | Used for |
| --- | --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_cnc-20251231.htm.jsonl | 097062d4e055a3b7fe83b7f7a6e69a627cdfc677e170580a5543c61781d7f32c | Business description, segments, history, divestitures, ownership data, regulatory context |
| Q1 10-Q | 10-Q_2026-03-31_cnc-20260331.htm.jsonl | 6fdb16147461b8c90a892872b86f94619262dc29b1649522f12be59d50d43010 | Q1 2026 receivable sale and repurchases |
| Q2 10-Q | 10-Q_2026-06-30_cnc-20260630.htm.jsonl | 2be254120598acb867bfc89cb539dc675621975d5b2820213b11fde2ab54d522 | Q2 2026 risk adjustment benefit |
| Q3 10-Q | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | cfb19f79c82250660e2e3f3fc4242fe18840a50e06dfa54c4c173df9081f0994 | Latest business updates, regulatory trends, contracts, membership, legal matters, subsequent events |
| Q1 release | EX-99.1_2026-04-28_a20260428ex991pressrelease.htm.jsonl | 85e525be3f7df9445c1acc49590c58f56053e97a34531af048cb7fd64ca5f94b | Management narrative, April 28, 2026 |
| Q2 release | EX-99.1_2026-07-28_a20260728ex991pressrelease.htm.jsonl | ef848078ad02a5ade77bb7226070a38945f9e917a1e3e86d5abb0edd73e6d395 | Management narrative, July 28, 2026 |
| Q3 release | EX-99.1_2026-10-27_a20261027ex991pressrelease.htm.jsonl | 916ad849ec4d38de97614bebc7921009e1fad702ea222f32804d2cf10f3a8c80 | Management narrative and guidance, October 27, 2026 |

### Run settings

| Item | sha256 | Role |
| --- | --- | --- |
| context | 513a568e8f913d85d10b3279b6da71f4942d77c29169f956b5f35a2740b22b67 | Sector "Hospital & Medical Service Plans", country United States, ticker CNC; sponsor, parent, borrower and guarantor fields blank; no transaction terms, ratings or quotes. Not issuer evidence; blanks are not zero. |

### Supplied handoffs

| Module | sha256 | Consumed for |
| --- | --- | --- |
| CP-0 | 891bc08ab57345267c7df4471f2151a6318cc16f4e53da139e0a73bb24e6659d | Source readiness: filings control, releases are secondary, executed agreements and proxy statement not supplied, nothing after October 27, 2026 |
| CP-1 | d148eae49bfb36d490e6a47382af69ec58ed9ca91eec53f6c1c1514a18cb82bc | Financial base: debt of 15,542 at September 30, 2026, unregulated cash available for general corporate use of 175, undrawn revolver of 4,000, debt to capital of 41.1%, receivable sale proceeds of 970, front-loaded earnings |

Limitations carried forward from CP-0 and CP-1: no proxy statement (so board, ownership above the filings and executive pay are Not supplied); no executed credit agreement, indentures, receivable purchase agreement or Magellan sale agreement (so legal capacity cannot be assessed); the issuer reports no EBITDA; cash flow statements are cumulative only; nothing after October 27, 2026.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Centene is a large managed care insurer dependent on government rate setting, procurement and changing regulation, with a shrinking Marketplace book. Documented 2026 actions have been creditor-supportive, and no sponsor or leveraged transaction exists. | Medium | The proxy statement and the sale, receivable purchase and credit agreements are not supplied, so ownership detail and legal capacity are not assessed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Revenue depends on government payors: Medicaid was 57% of FY2025 external revenues, and Florida and New York each exceeded 10% of Medicaid premium revenues. | State rate setting and procurement outcomes in a few states drive revenue durability and margin. | High |
| Membership fell to 25,698,200 at September 30, 2026 from 27,968,100 a year earlier, led by Marketplace, which fell from 5,828,100 to 3,403,300. | Mix shifts toward Part D and Medicaid; Marketplace repricing supported margin but shrinks the book. | Medium |
| Dated headwinds are disclosed: Medicaid work requirements, a California transition in 2027, Hawaii contract loss and lower 2027 Star Ratings. | Revenue visibility into 2027 and 2028 weakens before any offset from dual-eligible integration. | Medium |
| No sponsor exists. Documented 2026 actions were deleveraging: note repurchases, a 970 receivable sale funding part of the 2027 redemption, and no common stock repurchases in the third quarter. | Behaviour is creditor-supportive on the record, but the sale funds redemption off debt and legal capacity is unverified. | Medium |

### Business and transaction view

CENTENE CORP is a publicly listed, widely held managed care organization with no sponsor, controlling owner or leveraged transaction in the supplied sources. Its credit-relevant facts are operating and regulatory. Revenue comes mainly from state Medicaid agencies and from the federal government through Medicare and the Marketplace, so margin is the spread between premium set by payors and medical costs, which the issuer measures as the health benefits ratio. Membership of 25,698,200 at September 30, 2026 was below the 27,968,100 of a year earlier, driven by a Marketplace decline, while stand-alone Part D membership grew. The record shows a company that spent 2026 reducing debt, repricing the Marketplace and absorbing severance costs, while facing dated regulatory changes in 2027 and 2028. The corporate transactions in the record are small relative to the group: the pending Magellan Health sale, a receivable sale facility with MUFG Bank, Ltd., and note repurchases. No new debt was issued in 2026. Ownership above the filings, board composition and the terms of the sale and financing agreements are Not supplied, so sponsor behaviour is judged on documented actions only and legal capacity is not assessed.

### Company and operating model

| Driver | Evidence | Category | Mechanism and credit implication |
| --- | --- | --- | --- |
| Revenue model | Medicaid, Medicare, Commercial and Other segments (10-K FY2025 page:13); Medicare Advantage MCOs "typically receive fixed monthly premium per member from CMS" (10-K FY2025 page:17) | Documentary Fact | Premium is set by payors, not by Centene, so revenue visibility depends on rate cycles and bids; margin depends on controlling medical costs against fixed premium |
| Segment mix | "57%, 21%, 19% and 3%, respectively, of our total external revenues" for Medicaid, Commercial, Medicare and Other in FY2025 (10-K FY2025 page:13) | Documentary Fact | Medicaid is the largest exposure; Medicaid premium tax pass-through inflates reported revenue relative to premium and service revenues |
| Concentration | "Florida and New York accounted for approximately 10% or more of our consolidated Medicaid premium revenues individually" (10-K FY2025 page:15); 12.5 million Medicaid members in 30 states | Documentary Fact | A rate or procurement decision in two states moves a large share of Medicaid revenue |
| Contract renewal risk | "we are currently protesting the Texas and Georgia Medicaid reprocurements in which we were not a successful bidder" (10-K FY2025 page:52); "we were not selected to continue providing services under the Florida Children's Medical Services (Florida CMS) program" (Q3 10-Q page:37) | Documentary Fact | Contract losses remove scale and cannot be offset quickly; outcomes of protests are Not supplied |
| Pricing | Marketplace "corrective pricing actions for 2026 covering 95% of Marketplace membership" (Q3 10-Q page:36); Medicare Advantage and PDP contracts are renewed for one-year terms each September, with bids filed in June (10-K FY2025 page:17) | Documentary Fact | Repricing restored Marketplace margin at the cost of membership; annual bids limit multi-year visibility |
| Volume drivers | Total membership 25,698,200 at September 30, 2026 against 27,968,100 at September 30, 2025; Marketplace 3,403,300 against 5,828,100; PDP 8,947,200 against 7,972,500 (Q3 10-Q page:38) | Documentary Fact | Volume is shifting from Marketplace toward PDP and Medicaid, changing the margin and seasonality mix |
| Medical cost structure | Health benefits ratio 92.7% in Q3 2026 and 89.9% for nine months; 91.9% for FY2025 against 88.3% for FY2024 (Q3 10-Q page:42; 10-K FY2025 page:107) | Documentary Fact | Medical costs are the dominant cost line; a small ratio change moves earnings by more than most other lines. FY2025 shows the downside |
| Seasonality | Medicare Advantage "higher percentage of earnings in the first half of the year" (10-K FY2025 page:17) | Management Language | Earnings are front-loaded, so LTM leverage in CP-1 overstates the third quarter run rate |
| Overheads and optimization | Severance and vendor costs "$297 million and $358 million" for the quarter and nine months (Q3 10-Q page:36) | Documentary Fact | Restructuring costs depress reported operating earnings; benefits are management claims until visible in the adjusted SG&A ratio |
| Capital spending | "approximately $800 million in capital expenditures" expected in 2026 at the 10-K date (10-K FY2025 page:112); "approximately $200 million in additional capital expenditures" for the remainder of 2026 (Q3 10-Q page:48) | Management Language | Forward-looking management statements; modest relative to operating cash flow in CP-1 |
| Subsidiary dividends | "we expect net dividends of approximately $20 million from our insurance subsidiaries" for the remainder of 2026 (Q3 10-Q page:48), after 1.7 billion of dividends received in nine months (Q3 10-Q page:49) | Management Language | Little upstream cash is expected in the fourth quarter, so parent liquidity of 175 plus the undrawn 4,000 revolver in CP-1 is the working buffer |
| Working capital | "pass-through payments from its state partners" of about 1,635 at September 30, 2026 and about 4,500 at June 30, 2026 (Q3 10-Q page:12) | Documentary Fact | Pass-through timing swings quarterly operating cash flow; do not read one quarter as run rate |
| Part D receivables and sale | Receivables for the 2025 plan year are expected from CMS "within a year after the plan year closes" (Q3 10-Q page:14); a participating interest of 1,000 was sold in March 2026 (Q3 10-Q page:15) | Documentary Fact | Cash timing risk sits with CMS settlement; the sale pulled cash forward |
| Regulated subsidiary structure | Operations conducted "through our subsidiaries" with dividends limited by state regulators (Q3 10-Q page:49) | Documentary Fact | Cash at the parent depends on regulated subsidiary dividends; headline cash is not parent liquidity |
| Regulatory calendar | OBBBA work requirements and provider-tax and state-directed-payment changes "beginning in 2028"; enhanced Marketplace subsidies expired at the end of 2025; dual-eligible integration beginning in 2030 (Q3 10-Q page:30, page:31, page:32) | Documentary Fact | Dated regulation changes eligibility and funding; effects are uncertain and phased |

### Company profile

| Attribute | Detail | Source |
| --- | --- | --- |
| Business description | Managed care organization serving government-sponsored and commercial programs, focused on under-insured individuals; the issuer describes itself as the largest Medicaid and Marketplace insurer and the largest stand-alone PDP provider (management claim) | 10-K FY2025 page:13; Q3 10-Q page:28 |
| Country and sector | United States; Hospital and medical service plans (context); headquartered in St. Louis, Missouri | Context; Q3 10-Q page:1 |
| Legal entity and listing | Centene Corporation, Delaware; NYSE ticker CNC since October 16, 2003 | Q3 10-Q page:1; 10-K FY2025 page:91 |
| Origin | First health plan began in Wisconsin in 1984; organized in Wisconsin in 1993; reincorporated in Delaware in 2001 | 10-K FY2025 page:13 |
| Segments | Medicaid, Medicare, Commercial and Other (pharmacy, vision and dental, clinical healthcare, behavioral health, centralized services) | 10-K FY2025 page:13 |
| Footprint | Medicaid in 30 states; Medicare Advantage in 32 states; PDP in 50 states and the District of Columbia; Ambetter Health in 29 states in 2026 | 10-K FY2025 page:15, page:17, page:18; Q3 10-Q page:36 |
| Membership | 27.6 million at December 31, 2025; 25.7 million at September 30, 2026 | 10-K FY2025 page:13; Q3 10-Q page:33 |
| Employees | About 61,100 team members at December 31, 2025 | 10-K FY2025 page:40 |
| Management | Sarah M. London, Chief Executive Officer since March 2022; Andrew L. Asher, Executive Vice President, Chief Financial Officer | 10-K FY2025 page:41, page:42 |
| Auditor | KPMG LLP, auditor since 2005; audit report dated February 17, 2026 | 10-K FY2025 page:129 |
| Ownership | Listed equity; 944 holders of record at February 13, 2026; 495,068 thousand shares outstanding at October 23, 2026; no sponsor or controlling holder in the supplied sources | 10-K FY2025 page:91; Q3 10-Q page:1; context |
| Capital structure headline | Total debt 15,542 at September 30, 2026; revolver 4,000 undrawn; debt to capital 41.1% (CP-1) | Q3 10-Q page:20, page:47 |

### Ownership, control and economic interest

| Item | Evidence | Category | Implication |
| --- | --- | --- | --- |
| Owner class | Widely held NYSE-listed company; "944 holders of record of our common stock" (10-K FY2025 page:91) | Documentary Fact | No controlling shareholder is documented in the supplied sources |
| Beneficial holders above the filings | Item 12 is incorporated by reference to the proxy statement, which is not supplied | Insufficient Information | Percent ownership and control rights are Not supplied; no percentage is inferred |
| Sponsor or parent | Context leaves sponsor and parent blank | Insufficient Information | Blank is not evidence of absence; the filings describe a stand-alone listed registrant |
| Dividend recapitalisation history | No debt-funded distribution to shareholders is documented in the supplied sources; stock repurchases of 3,124 in 2024 and 475 in 2025 and 57 in the nine months of 2026 are in the cash flow statements (CP-1) | Analyst Interpretation | Shareholder returns were cut sharply as earnings fell; this is a cash allocation fact, not evidence of extraction |
| Share repurchase authority | "$1.8 billion remains as of December 31, 2025" and 1,830 remained at September 30, 2026 (10-K FY2025 page:91; Q3 10-Q page:52); "we made no repurchases under the stock repurchase program" in the third quarter (Q3 10-Q page:46) | Documentary Fact | Authority exists to resume repurchases; the board can choose at any time |
| Common dividend policy | No statement of a common dividend policy was located | Insufficient Information | Cannot assess shareholder-distribution restrictions beyond the credit agreement, which is not supplied |

### Timeline

| Date | Event | Category | Note |
| --- | --- | --- | --- |
| 1984 to 2003 | First health plan in Wisconsin 1984; Delaware reincorporation 2001; NYSE listing October 16, 2003 | Documentary Fact | 10-K FY2025 page:13, page:91 |
| December 2022 | Magellan Rx divestiture completed for $1.3 billion | Documentary Fact | 10-K FY2025 page:94 |
| January 12, 2024 | Circle Health divestiture completed for $931 million | Documentary Fact | 10-K FY2025 page:147 |
| October 4, 2024 | Collaborative Health Systems sale completed | Documentary Fact | 10-K FY2025 page:147 |
| March 5, 2025 | New Credit Agreement: 4,000 revolver and 2,000 term loan, maturing March 5, 2030 | Documentary Fact | 10-K FY2025 page:158, page:159 |
| July 2025 | OBBBA enacted; Securities Action filed July 9, 2025 | Documentary Fact | 10-K FY2025 page:16; Q3 10-Q page:27 |
| Third quarter 2025 | Goodwill impairment of $6.7 billion recorded; GAAP loss per share of 13.53 for FY2025 | Documentary Fact | 10-K FY2025 page:99 |
| December 2025 | Definitive agreement to sell remaining Magellan Health businesses; impairment of 513 | Documentary Fact | 10-K FY2025 page:148 |
| February 13, 2026 | Receivable purchase agreement with MUFG Bank, Ltd. (up to 4,250 outstanding) | Documentary Fact | 10-K FY2025 page:177; Q3 10-Q page:14 |
| March 2026 | Participating interest of 1,000 sold, net proceeds 970, used for partial redemption of the 2027 notes | Documentary Fact | Q3 10-Q page:15 |
| June 2026 | CMS final 2025 risk adjustment transfers, pre-tax benefit of 480; CMS interim rule on work requirements June 3, challenged by 26 states on June 29 | Documentary Fact | Q3 10-Q page:36, page:30 |
| July 2026 | Voluntary separation program; New York terminated its Essential Plan-5 | Documentary Fact | Q3 10-Q page:26, page:30 |
| September 2026 | Florida Children's Medical Services contract concluded; Hawaii Community Care Services program extended to October 31, 2026 | Documentary Fact | Q3 10-Q page:37 |
| October 2026 (subsequent event) | 2027 Medicare Advantage Star Ratings issued; remaining 2027 notes redeemed; repurchase authorization raised by 2,000 | Documentary Fact | Q3 10-Q page:38, page:21. After the September 30, 2026 balance sheet; not folded into period facts |
| January 1, 2027 (future-dated) | California Medi-Cal UIS transition to fee-for-service, about 175,000 at-risk members; Hawaii QUEST Integration transition; Illinois HealthChoice contract begins | Documentary Fact | Q3 10-Q page:30, page:37 |
| 2027 and later (future-dated) | Health Net commercial group exit with policy end dates from February 28, 2027 to December 28, 2027; Arizona long-term care contract effective October 2027 if awarded | Documentary Fact | Q3 10-Q page:38, page:37 |

### Governance and issuer behaviour

Assessment is of issuer-level documented actions only, not individuals, and not inferred from ownership. Evidence quality is High for items taken from filings and dated, and the category follows the behaviour definitions in the method.

| Behaviour | Documented action | Category | Legal capacity, willingness and feasibility |
| --- | --- | --- | --- |
| Deleveraging | Senior notes repurchased: 1,647 of 2027 notes and 200 of 2028 notes in the nine months; remaining 569 of 2027 notes redeemed in October 2026 (Q3 10-Q page:21) | Supportive | Willingness shown by action; feasibility supported by liquidity in CP-1; legal capacity under the indentures Not supplied |
| Funding of redemptions | Receivable sale proceeds of 970 "were used for the partial redemption of the Company's Senior Notes due December 15, 2027" (Q3 10-Q page:15) | Neutral or Mixed | Shifts funding from debt to a sale facility that has "specified repurchase obligations" (10-K FY2025 page:177); agreement not supplied |
| Shareholder returns | No repurchases under the stock program in the third quarter of 2026; 57 repurchased in nine months against 473 in the comparable 2025 period (CP-1) | Supportive | Capacity retained: 1,830 authority remains. The board can resume at will |
| Disclosure and reporting | Quarterly filings and releases with reconciliations; non-GAAP measures reconciled to GAAP (Q3 release page:6) | Supportive | Evidence quality High; no early warning on covenants because definitions are not supplied |
| Litigation and governance risk | Securities Action alleging false statements about 2025 guidance; "The Company denies any wrongdoing" (Q3 10-Q page:27) | Neutral or Mixed | Allegations only; amounts accrued are described as not material (Q3 10-Q page:26); no loss estimate is given |
| Creditor-adverse conduct | No priming, uptiering, drop-down or non-pro-rata exchange is documented in the supplied sources | Insufficient Information | Absence in the sources is not evidence of absence; indentures and credit agreement are not supplied |

### Capital allocation, acquisitions and disclosure

- Deleveraging and divestitures: since 2022 the record shows divestitures (Magellan Rx, Circle Health, Collaborative Health Systems) and a pending Magellan Health sale, and debt reduction in 2026. Mechanism: asset sales and note repurchases reduce debt and the Other segment's perimeter; proceeds and terms of the pending Magellan sale are Not supplied.
- Acquisitions: no acquisition is documented in 2026. The record does not support an inference about acquisition appetite.
- Monitoring documents the source set lacks: debt schedule by instrument at par (carrying amounts only), covenant certificate and definitions, add-back bridge (the issuer reports no EBITDA), the proxy statement, and the receivable and divestiture agreements. Severity: High for covenant definitions; Medium for the others.

### Conflicts logged

| Topic | Source A | Source B | Effect |
| --- | --- | --- | --- |
| 2025 risk adjustment benefit recognized in 2026 | "the net pre-tax benefit recognized was $481 million in the six months ended June 30, 2026" (Q2 10-Q page:18) | "the net pre-tax benefit recognized was $480 million in the nine months ended September 30, 2026" (Q3 10-Q page:20) | The cumulative benefit appears one lower after a further quarter; not reconciled here. CP-1 earnings are unaffected as statements control |
| Receivable sale recourse | "without recourse for credit losses related to the financial condition of CMS" (Q3 10-Q page:14) | "specified repurchase obligations that would require us to repurchase the purchased receivable portions upon the purchaser's request if certain events occur" (10-K FY2025 page:177) | The two statements cover different risks (credit loss against repurchase events); the agreement is needed to know the contingent claim on liquidity |
| Medicare and Medicaid membership comparability | Medicare Advantage membership includes integrated plans as a result of the CMS transition in 2026 (Q3 10-Q page:39) | Medicare-Medicaid Plan members are shown in High Acuity Medicaid through December 31, 2025 (Q3 10-Q page:38) | Segment membership is not like-for-like across the year-end; a year-on-year change in either line mixes a reclassification with real change |

### Credit translations

1. Revenue durability. Evidence: Medicaid was 57% of FY2025 external revenues; Florida and New York are each about 10% or more of Medicaid premium revenues (10-K FY2025 page:13, page:15); the Florida CMS contract concluded and Hawaii contracts were not renewed (Q3 10-Q page:37). Mechanism: premiums and contracts are set by a small number of public payors through rate cycles and procurements, so a single loss or rate shortfall changes revenue and margin quickly. Implication: revenue is large but not locked in; the creditor should weight procurement outcomes and rate adequacy ahead of absolute scale. Countering fact: new and renewed contracts, for example Illinois beginning January 2027 (Q3 10-Q page:37).
2. Margin and cash-flow risk. Evidence: health benefits ratio of 91.9% for FY2025 against 88.3% for FY2024 and 92.7% in Q3 2026 after 87.3% in Q1 (10-K FY2025 page:107; Q1 10-Q page:32; Q3 10-Q page:40). Mechanism: with medical costs the dominant cost line and premiums fixed for the year, a small ratio drift removes most of the margin, and Medicare costs rise through the year as deductibles are met. Implication: LTM measures in CP-1 are flattering relative to the second half; monitor fourth quarter results and the 2027 rate cycle. Countering fact: the nine-month ratio of 89.9% was better than 91.1% a year earlier (Q3 10-Q page:42).
3. Regulatory and eligibility risk. Evidence: OBBBA work requirements and funding changes, expiry of enhanced Marketplace subsidies and a fall in Medicare Advantage Star Ratings coverage to about 42% of membership in plans rated 3.5 stars or higher from about 60% (Q3 10-Q page:30, page:31, page:38). Mechanism: eligibility and subsidy changes reduce membership and raise morbidity before rates adjust; lower Star Ratings flow into 2028 plan year revenues. Implication: expect membership and revenue pressure through 2027 and 2028 with an uncertain timing of rate offsets. Countering fact: the dual-eligible integration rule from 2030 favours Centene's overlapping Medicaid and Medicare footprint, as management states (Q3 10-Q page:32), which is Management Language.
4. Sponsor alignment and creditor control. Evidence: no sponsor; documented debt reduction and a pause in repurchases (Q3 10-Q page:21, page:46). Mechanism: with dispersed ownership, capital allocation is decided by the board and constrained by covenants not supplied. Implication: documented behaviour is creditor-supportive, but this is not a contractual protection. Counter: the receivable sale facility with repurchase obligations (see conflicts).
5. Key uncertainties. Magellan sale terms and timing; outcome of Texas and Georgia protests; the receivable agreement; covenant definitions; events after October 27, 2026. These are listed in `## Gaps`.

### Consumer assessments

| Consumer | Readiness | What to take from CP-1A | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Segment and state concentration, dated regulatory headwinds, the receivable sale and Magellan perimeter, documented deleveraging, no sponsor | Business risk and revenue visibility drive the fundamental credit view | Proxy, agreements and procurement outcomes not supplied | Treat conclusions as based on filings only; carry the conflicts and gaps |
| CP-5 | READY_WITH_LIMITATIONS | Every row has a locator and a category; subsequent and future-dated events are labelled | Evidence trace depends on locators and on respecting dates | Releases duplicate filings; the proxy is not supplied | Check figures against CP-1 values and keep Management Language labelled |

### Transaction summary and new debt issues

There is no sponsor, acquisition or leveraged buyout in the supplied sources, and no new debt was issued in 2026. The cash flow statement shows no proceeds from long-term debt in the nine months ended September 30, 2026, against 750 in the same period of 2025 (CP-1). The transactions that matter to a creditor are three. First, the pending sale of the remaining Magellan Health businesses, agreed in December 2025: its buyer, price, expected closing date and use of proceeds are Not supplied, and held-for-sale assets and liabilities of 312 each are on the September 30, 2026 balance sheet. Second, the February 13, 2026 master receivable purchase agreement with MUFG Bank, Ltd. for up to 4,250 of 2025 plan year stand-alone Part D risk-sharing receivables: a participating interest of 1,000 was sold in March 2026 for net proceeds of 970, which funded part of the redemption of the 2027 notes, with 3,250 of purchase capacity remaining at September 30, 2026 and settlement of the sold interest expected in the fourth quarter of 2026. Third, debt reduction through the senior note repurchase program, whose authorization was raised in February, May and October 2026, and the October 2026 redemption in full of the remaining 569 of 2027 notes; this is a subsequent event after the September 30, 2026 balance sheet. The credit agreement dated March 5, 2025, with a revolver of 4,000 and a term loan, is described in the 2026 filings without any amendment. The next scheduled note maturity on the debt register in CP-1 is the 2028 notes. Terms of the agreements are Not supplied, so legal capacity, baskets and covenants are not assessed here.

## Calculations

No new calculation. Every figure is quoted from a located chunk or carried from CP-1 with the same value, period and unit. Where a share is stated (57% of FY2025 external revenues) it is printed in the 10-K FY2025 (page:13), not computed.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Proxy statement not supplied: board, beneficial owners, control rights, executive pay and clawback | Medium | CP-2, CP-5 | Supply the proxy statement referenced by Part III of the 10-K |
| Magellan Health sale agreement: buyer, price, closing conditions and proceeds not supplied | Medium | CP-2 | Supply the agreement or its 8-K |
| Receivable purchase agreement and performance guaranty not supplied; repurchase triggers unknown | Medium | CP-2 | Supply Exhibits 2.1 and 2.2 |
| Credit agreement and indentures not supplied; covenant definitions, baskets, guarantors and restricted payment capacity unknown | High for legal and covenant work | CP-2, CP-5 | Supply executed documents |
| Outcomes of Texas and Georgia protests and Arizona rebid not supplied | Medium | CP-2 | Supply later disclosures |
| Common dividend policy not located | Low | CP-2 | Confirm in the full 10-K or proxy |
| Events after October 27, 2026 not supplied | Medium | CP-2, CP-5 | Supply later 8-Ks |
| Releases duplicate the filings; no investor presentation, rating report or market data | Low | CP-2 | Not required for this scope |

## Next module

- CP-2: use the segment and state concentration, dated regulatory headwinds and the front-loaded earnings pattern as business-risk drivers alongside CP-1 figures; treat the sponsor as none; carry the receivable-agreement and covenant-definition gaps; do not infer creditor-adverse or supportive intent beyond the documented actions.
- CP-5: trace each row to its locator; check that figures match CP-1 exactly (total debt 15,542; unregulated cash available for general corporate use 175; revolver 4,000; debt to capital 41.1%; net receivable sale proceeds 970); keep the subsequent and future-dated labels; keep Management Language rows labelled.
