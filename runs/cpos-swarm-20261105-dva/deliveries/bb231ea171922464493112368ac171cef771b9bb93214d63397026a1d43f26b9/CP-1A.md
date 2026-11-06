# CP-1A — Business and transaction context: DAVITA INC. (dva)

## Request

- Issuer: DAVITA INC. (issuer id `dva`, ticker DVA), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026; prior period FY2025 (context).
- Run: `dva-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Question: which transaction, business, ownership and operating facts matter most to the creditor, and what do they mean for risk, liquidity and refinancing? Reader: a credit committee that has already read the financial base (CP-1).
- Scope: public filings and earnings releases only. No sponsor, no merger and no external material is used. Amounts are US$ millions unless a unit is stated; statement figures come from the CP-1 handoff or from the cited page.
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers. Tags: [10-K] annual report, [Q1 10-Q], [Q2 10-Q], [Q3 10-Q] quarterly reports, [Q1 ER], [Q2 ER], [Q3 ER] earnings releases. Quotes are exact substrings of the cited page. Fact categories: Documentary Fact, Management Language, Analyst Interpretation, Insufficient Information.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_dva-20251231.htm.jsonl | e8c363b79225d32d92e8856c1234363883b84595e0f356cf12128301c572a94b | Business, payors, ownership, Berkshire agreements, notes, risk factors |
| 10-Q_2026-03-31_dva-20260331.htm.jsonl | 7063ac673c62a3a12d361c8ab9f216c83e6406eb95937f85ad2f6c47a221fe01 | Elara Caring agreement, Q1 2026 results |
| 10-Q_2026-06-30_dva-20260630.htm.jsonl | 5aed5931f3b50f8efc4d5398264cb7a317623aeb269a49968c33246ed0273365 | Ninth Amendment, Elara closing, Q2 2026 results |
| 10-Q_2026-09-30_dva-20260930.htm.jsonl | 99b4bb0c8f87c03db2290c95cfd812d4622509e8fdbcdce46d84afcedef79236 | Operating review, payor mix, legal matters, share repurchases, Berkshire settlement |
| EX-99.1_2026-05-05_dva33126ex991.htm.jsonl | c5727d9383becddd69bf1cd80efadc8ee72012f8313405a8b1414b2f74143fa7 | Q1 2026 release (management language) |
| EX-99.1_2026-08-04_dva63026ex991.htm.jsonl | e55a9fe053fe9f69274156863d81212ffe989a931913bc64dfc65b70fd8151a2 | Q2 2026 release (management language) |
| EX-99.1_2026-10-29_dva93026ex991.htm.jsonl | b062a4dfa0aa9b3cce4ee385c1a8aad8546180810a3acbc585a968f93eadfc64 | Q3 2026 release: metrics, guidance (management language) |
| context | 888318ae2603a71d9f443112e6d0298861b2ea95d8c8a8118da68f80c88bfe70 | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 3ecf1492bb810c2e90133183ed7699bad1c56c1780a9f8736f0e2c4391db50f2 | Source readiness: all selected consumers ready with limitations |
| CP-1 | 3cfbf98d548042fd31ec6ebfe100057e48caebe480e0597af9abd9a0b0ee8fc9 | Financial base: debt, liquidity, maturities, covenant picture, claims outside debt |

Consistency with CP-0 and CP-1: this answer confirms both on the points it uses. CP-1 described the Berkshire repurchase obligation as settled on October 27, 2026; this answer confirms it and adds that the earlier December 31, 2025 obligation was settled on January 29, 2026 ([10-K] page:201). CP-1 wrote that the China impairment sits in the ancillary segment; this answer confirms it (the 62.2 charge is in International, [Q3 10-Q] page:41). No correction is needed.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| DaVita is a large kidney care provider with no sponsor and no pending deal. U.S. dialysis earns 97.3% of segment margin, and commercial payors drive profit. The creditor issues are reimbursement policy, unit-cost growth and buyback-led capital allocation. | Medium | No credit agreement, indenture, guarantor list, Berkshire agreement or proxy statement is supplied, and nothing after October 29, 2026 is available. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| U.S. dialysis supplied 97.3% of segment operating margin and 84.9% of segment revenue in 9M 2026. | Credit quality rests on one reimbursement-driven business, with ancillary services still small. | High |
| Non-hospital commercial payors were 26% of U.S. dialysis revenue and 11% of patients in FY2025 but generate nearly all profit. | Small shifts in commercial mix or rates move earnings; the expiry of enhanced premium tax credits already pressures mix. | High |
| Revenue per treatment rose 2.7% in 9M 2026 while patient care costs per treatment rose 3.0%. | Unit margin narrowed before any change in volume, which grew 0.5%. | Medium |
| Berkshire's stake is managed to 45.0% by a repurchase agreement and a standstill, and 9M 2026 buybacks were 5.8 million shares. | Owner influence is bounded, but capital allocation favours share repurchases over deleveraging. | Medium |
| A China impairment, open government inquiries and a new federal Kidney Care National Plan add policy and legal uncertainty. | Event risk is real but not quantified in the filings. | Low |

### Business and transaction view

DaVita Inc. is a listed, widely held provider of dialysis and related kidney care, with no private-equity sponsor and no pending acquisition or sale of the company described in the sources. The business is dominated by U.S. outpatient dialysis, a life-sustaining, recurring therapy paid mainly by Medicare and Medicare Advantage at about 57.7% of U.S. dialysis patient service revenue and by commercial insurers at about 31.9%, with the commercial segment generating nearly all profit. That makes earnings sensitive to commercial mix and to Medicare rate setting rather than to discretionary demand. In 9M 2026 volume was steady (treatments up 0.5%) and revenue per treatment rose, but patient care costs per treatment rose faster, and the integrated kidney care and international businesses are small and volatile. Ownership is public with a significant but capped holder, Berkshire Hathaway, whose position is managed through a repurchase agreement and a standstill; the company does not pay cash dividends and has returned capital through repurchases. The only transactions in the period are financing amendments, a 200.0 minority investment in Elara Caring, share repurchases and the settlement of the Berkshire repurchase obligation. For a creditor the central mechanics are therefore operating (reimbursement, commercial mix, labor and supply cost, litigation and policy risk) and capital allocation (buybacks funded partly by net debt issuance, per the financial base), not sponsor or merger risk. The sources give no governing debt documents, so control and priming risk can be judged only from documented actions, and none of a creditor-adverse kind was found.

### Company and operating model

| Area | Fact | Category | Locator | Credit relevance |
| --- | --- | --- | --- | --- |
| Core activity | DaVita is described as providing kidney care at every stage; "Our U.S. dialysis and related lab services (U.S. dialysis) business treats patients with chronic kidney failure, ESKD, in the United States, and is our largest line of business." | Documentary Fact | [10-K] page:5 | Life-sustaining, recurring therapy supports revenue visibility. |
| Scale | As of September 30, 2026 the company provided dialysis to approximately 298,100 patients at 3,269 outpatient dialysis centers, of which 2,671 were in the United States and 598 in 14 other countries. | Documentary Fact | [Q3 ER] page:3 | Network density supports payor contracting and fixed-cost absorption. |
| Segment mix | U.S. dialysis total revenues 9,004.0 of total net segment revenues 10,610.1 in 9M 2026 (84.9%); segment operating margin 1,588.1 of 1,632.4 (97.3%). FY2025: 2,084.2 of 2,176.6 (95.8%). | Analyst Interpretation | [Q3 10-Q] page:23 to page:24; [10-K] page:212 | Earnings depend on one segment; ancillary margin is thin and volatile. |
| Payors | Non-hospital commercial: "Approximately 26% of our U.S. dialysis patient service revenues and approximately 11% of our U.S. dialysis patients" for FY2025. "The payments we receive from commercial payors generate nearly all of our profits". "No single commercial payor accounted for more than 10% of total U.S. dialysis revenues". | Documentary Fact | [10-K] page:15 | Profit is concentrated in a minority of patients; loss of commercial mix compresses margin. |
| Payor mix trend | U.S. dialysis patient service revenue 9M 2026: Medicare and Medicare Advantage 57.7%, Medicaid 7.4%, other government 3.0%, commercial 31.9% (calculated). 9M 2025: 57.3%, 7.3%, 2.8% and 32.5%. Commercial revenue grew 1.2% against 4.0% for Medicare and Medicare Advantage. | Analyst Interpretation | [Q3 10-Q] page:7 to page:8 | Mix is shifting toward government payors at lower rates. |
| Pricing | Medicare pays an ESRD bundled rate; "CMS estimates that the overall impact of the rule will increase ESRD freestanding facilities' average reimbursement by 2.2%" for calendar year 2026. Phosphate binders moved into the bundle on January 1, 2025 with a transitional add-on payment that "currently is set to expire at the end of 2026". Commercial contracts "sometimes contain annual price escalator provisions". | Documentary Fact | [10-K] page:13, page:15 | Medicare rate updates are small and policy-set; commercial rates are negotiated. |
| 2027 rate rule | The Q3 10-Q reports a CMS rule for calendar year 2027 with a 2.7% estimated impact. The text calls it both a final rule and a proposed rule (see Conflicts). | Documentary Fact | [Q3 10-Q] page:37 | Next-year Medicare update is mildly positive but its status is unclear in the source. |
| Volume | Treatments 21,585,769 in 9M 2026, up 0.5%; Q3 normalized non-acquired growth 0.4%; the nine-month increase was "primarily driven by an increase in patient count". Risks named: mortality, missed treatments, GLP-1 and SGLT2 therapies. | Documentary Fact | [Q3 10-Q] page:36; [Q3 ER] page:1; [10-K] page:7 | Volume growth is low; demand risk is long-dated and therapy-driven. |
| Unit economics | Revenue per treatment 416.22 against 405.15 (up 2.7%); patient care costs per treatment 279.24 against 271.23 (up 3.0%) in 9M 2026. Cost drivers: compensation including wage rates, medical supplies, insurance and health benefits. | Documentary Fact | [Q3 10-Q] page:36 to page:38 | Cost per treatment grew faster than revenue per treatment, so unit margin narrowed. |
| Cost structure | Patient care costs 7,185.3 and general and administrative 1,254.1 against revenue 10,547.8 in 9M 2026 (68.1% and 11.9%, calculated). Union petitions have been filed at clinics in California. | Analyst Interpretation | [Q3 10-Q] page:2, page:33 | Labor and supply inflation are the main margin risk. |
| Capital spending | 9M 2026 maintenance capital expenditure 309 and development 122; acquisition expenditure 42. | Documentary Fact | [Q3 10-Q] page:44 | Maintenance spend is below depreciation, so free cash flow is not capex-starved. |
| Working capital and revenue estimates | Receivables 1.684 billion, about 51 days of revenue outstanding against 49 at year-end. "We generally expect the range of our U.S. dialysis revenue estimating risk to be within 1% of revenue, which can represent as much as approximately 5% of our U.S. dialysis business’s operating income and adjusted operating income." | Documentary Fact | [Q3 10-Q] page:44; [10-K] page:138 | Revenue is estimated and trued up over years, so period results can move. |
| Joint ventures | "revenues from joint ventures in which we have a controlling interest represented approximately 30% of our U.S. dialysis revenues"; third-party partners hold minority stakes, some with put rights. | Documentary Fact | [10-K] page:16 | Part of consolidated cash flow belongs to partners; see CP-1 for distributions. |
| Integrated kidney care | Approximately 80,800 patients in risk-based arrangements representing approximately 6.4 billion of annualized medical spend; IKC revenue 422 in 9M 2026 against 352, operating income 24 against a loss of 24. Q3 income fell on lower shared savings. | Documentary Fact | [Q3 ER] page:3; [Q3 10-Q] page:40 to page:41 | Risk-based contracts add medical-cost risk and lumpy shared-savings income. |
| International | 598 centers in 14 countries; 9M 2026 revenue 1,156 against 979, operating income 40 against 93 after a 62 China goodwill and other asset impairment. | Documentary Fact | [Q3 10-Q] page:39 to page:41 | Growth is acquisitive and carries foreign reimbursement risk. |
| Physicians and competition | "Nearly 5,200 nephrologists currently refer patients to our outpatient dialysis centers." The largest competitor, Fresenius Medical Care, also manufactures supplies and equipment. | Documentary Fact | [10-K] page:16, page:39 | Referral relationships and medical director contracts are a key dependency. |
| Workforce | Approximately 78,000 teammates at December 31, 2025, about 72% in the U.S. | Documentary Fact | [10-K] page:41 | Labor intensity ties margin to wage inflation. |
| Operating incident | A cybersecurity incident in the second quarter of 2025 caused "a temporary disruption of our operations"; 9M 2025 charges were about 24 in G&A and 1 in patient care costs. | Documentary Fact | [Q3 10-Q] page:38 | Event cost was modest, but billing disruption affects collections risk. |

### Company profile

| Item | Detail | Category | Locator |
| --- | --- | --- | --- |
| Legal name and form | DaVita Inc., a Delaware corporation; Commission File Number 1-14106; IRS Employer Identification No. 51-0354549 | Documentary Fact | [Q3 10-Q] page:1 |
| Headquarters | 2000 16th Street, Denver, CO 80202 | Documentary Fact | [Q3 10-Q] page:1 |
| Listing and filer status | Common stock traded on the NYSE under DVA; large accelerated filer; "approximately 62.9 million shares" outstanding at October 27, 2026 | Documentary Fact | [Q3 10-Q] page:1 |
| Sector and country | Services-Misc Health & Allied Services, NEC; United States (context) | Documentary Fact | context |
| Fiscal year and auditor | Fiscal year ended December 31; KPMG LLP, Seattle, report dated February 11, 2026 | Documentary Fact | [10-K] page:153 |
| Sponsor and parent | Context leaves sponsor, parent, borrower and guarantors blank; no sponsor or parent is named in the filings read | Insufficient Information | context; [10-K] page:4 |
| Borrower and guarantors | The borrower is DaVita Inc.; the guarantors are "certain of the Company’s domestic subsidiaries"; the list (Exhibit 21.1) is not supplied | Insufficient Information | [10-K] page:183, page:216 |
| Management | Javier J. Rodriguez, Chief Executive Officer and Director; Joel Ackerman, Chief Financial Officer and Treasurer (roles as signatories) | Documentary Fact | [10-K] page:218 |
| Reporting basis | US GAAP; US$ thousands in statements; fiscal quarters ending March 31, June 30, September 30 | Documentary Fact | [Q3 10-Q] page:3 |
| Ratings | Not supplied: the sources and the context contain no rating | Insufficient Information | context |

### Transaction summary and new debt issues

There is no sponsor transaction, merger or sale of the company in the sources, and the 10-Qs list no pending business combination of that kind. The period contains these completed financing and capital events. On November 24, 2025 the Eighth Amendment to the credit agreement refinanced the revolver and Term Loan A-1 into a new revolver and Term Loan A-2 ([10-K] page:181). On June 8, 2026 the Ninth Amendment added an incremental 500.0 of Term Loan B-2 and the proceeds repaid part of the revolver, at a cost of 2.0 of extinguishment and modification costs ([Q3 10-Q] page:12). The most recent new senior notes were the 6.75% Senior Notes due 2033, issued May 23, 2025 at 1,000.0 ([10-K] page:184); no senior notes were issued in 2026 in the sources. Net debt issuance was 490 in 9M 2026 ([Q3 10-Q] page:44). The use of proceeds of the June 2026 incremental was repayment of part of the revolver and related interest and fees; the sources read state no use of proceeds for the 6.75% notes and give no single sources-and-uses table.

Non-debt capital events: the company signed an agreement on February 2, 2026 to buy a noncontrolling minority interest in Elara Caring for approximately 200.0, which closed effective July 20, 2026 with a 200.0 cash payment subject to post-closing adjustments ([Q1 10-Q] page:17; [Q3 10-Q] page:10). The Berkshire repurchase obligation of 199.9 at December 31, 2025 was settled on January 29, 2026, and the 54.7 obligation at September 30, 2026 was settled on October 27, 2026 for 69.0 ([10-K] page:201; [Q3 10-Q] page:19). The status of each is complete; the effect on liquidity is the cash outflow and, for the revolver, the drawn balance of 80.0 at September 30, 2026 (CP-1). Between October 1 and October 27, 2026 the company repurchased a further 0.5 million shares for 87 ([Q3 ER] page:2), a subsequent event relative to the Q3 10-Q period. No change of control, delisting or deregistration is described. Creditor-relevant change-of-control terms exist in the notes (the 6.75% notes carry a 101% repurchase offer on certain change of control events, [10-K] page:184), but the indentures and credit agreement are not supplied, so their full terms are Insufficient Information.

### Ownership, governance and sponsor behaviour

| Behaviour or fact | Evidence | Category | Legal capacity, willingness and feasibility | Locator |
| --- | --- | --- | --- | --- |
| Public ownership with a capped large holder | Under the Berkshire repurchase agreement the company repurchases shares so that Berkshire's holding returns to 45.0% whenever it owns at least 45.0%; the percentage Berkshire owns today is not stated in the pages read | Documentary Fact | Capacity: contractual. Willingness: the company bought 3.1 million shares from Berkshire in 9M 2026 (419.3 of cash). Feasibility: funded from cash flow and borrowings | [10-K] page:200; [Q3 10-Q] page:18 |
| Standstill | Berkshire is bound by a standstill: "the standstill agreement requires Berkshire to vote any shares it beneficially holds in excess of 40% of the then-outstanding voting stock of the Company in accordance with the recommendation of the Board of Directors of the Company (Board)" | Documentary Fact | Capacity: restricts Berkshire's control actions. It "terminates automatically if the Company enters into or publicly announces a plan to enter into a definitive agreement concerning a transaction involving all or a controlling portion of the Company's equity securities" | [10-K] page:202 |
| No common dividends | "we have not declared or paid cash dividends to holders of our common stock since going public" | Documentary Fact | Capacity: limited by credit facility restrictions. Willingness: none | [10-K] page:108 |
| Share repurchases | Board authorization of 2,000 on September 5, 2024, increased by 2,000 effective August 21, 2025; 12.7 million shares repurchased for 1,788 in FY2025; 5.8 million shares for 862.5 in 9M 2026; about 1,212 available at October 27, 2026 | Documentary Fact | Capacity: limited by credit facility terms and by the 4.00:1.00 relief threshold (CP-1). Willingness: sustained. Feasibility: free cash flow after distributions was 672 in 9M 2026, below buybacks of 870.2 (CP-1) | [10-K] page:131, page:199 to page:200; [Q3 10-Q] page:18 to page:19 |
| Leverage policy | The leverage ratio "remained within our target range of 3.0x to 3.5x throughout 2025"; the sources print no 2026 target | Management Language | Willingness: stated range; feasibility: 3.38x at Q3 2026 on the company ratio (CP-1) | [10-K] page:114 |
| Debt-funded capital return | Net debt issuance of 490 in 9M 2026 alongside buybacks of 870.2; total debt principal up and cash down (CP-1) | Analyst Interpretation | Behaviour sits between Neutral or Mixed and Extraction-Oriented: capital is returned to holders while leverage rises, but within the stated range and with no related-party leakage found | [Q3 10-Q] page:4, page:44 |
| Related party | Berkshire repurchase payable recorded as "due to related party"; settled at market-based average prices | Documentary Fact | Small and settled; no leakage indicated | [Q3 10-Q] page:19 |
| Distributions to minority partners | Distributions to noncontrolling interests of 243.8 in 9M 2026 exceed their net income of 201.8 | Documentary Fact | Cash leaves the group to partners; subject to JV agreements not supplied | [Q3 10-Q] page:2, page:4 |
| Disclosure quality | Quarterly releases print Consolidated EBITDA, net debt and the leverage ratio with a reconciliation and the 5.00x maximum | Documentary Fact | Supportive of transparent reporting; definitions rely on an unsupplied agreement | [Q3 ER] page:15 to page:16 |
| Anti-takeover provisions | Charter provisions "may deter hostile takeovers"; Section 203 of the Delaware General Corporation Law applies | Documentary Fact | Capacity: change of control is hard to force; the standstill ends if the company announces a control transaction | [10-K] page:202 |
| Creditor-adverse transactions | No uptier, drop-down, priming, non-pro-rata exchange, unrestricted-subsidiary designation or collateral release was found in the sources read | Insufficient Information | The credit agreement and indentures are not supplied, so capacity cannot be assessed | not applicable |

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| 1994 | Initial public offering; no common cash dividends since | Documentary Fact | [10-K] page:108 |
| June 19, 2019 | Sale of the DaVita Medical Group business to a subsidiary of Optum, Inc.; reported as discontinued operations | Documentary Fact | [10-K] page:7 |
| August 12, 2019 | Date of the senior secured credit agreement (since amended) | Documentary Fact | [10-K] page:181 |
| February 9, 2022 | Berkshire standstill agreement amended and restated | Documentary Fact | [10-K] page:202 |
| April 30, 2024 | Berkshire share repurchase agreement | Documentary Fact | [10-K] page:200 |
| August 13, 2024 | Indenture for the 6.875% Senior Notes due 2032 (third-quarter 2024 issuance) | Documentary Fact | [10-K] page:213, page:126 |
| 2024 | Acquisition of DaVita Care Pte. Ltd. (international) | Documentary Fact | [10-K] page:203 |
| May 23, 2025 | 6.75% Senior Notes due 2033 issued | Documentary Fact | [10-K] page:184 |
| Second quarter 2025 | Cybersecurity incident disrupted operations temporarily | Documentary Fact | [Q3 10-Q] page:38 |
| July 17, 2025 | Seventh Amendment refinanced Term Loan B-1 into Term Loan B-2 | Documentary Fact | [10-K] page:181 |
| August 1, 2025 | Acquired Fresenius Medical Care's dialysis operations in Brazil for 94.3 | Documentary Fact | [10-K] page:203 |
| November 24, 2025 | Eighth Amendment: new revolver and Term Loan A-2 | Documentary Fact | [10-K] page:181 |
| January 29, 2026 | Berkshire repurchase obligation of 199.9 settled | Documentary Fact | [10-K] page:201 |
| February 2, 2026 | Agreement to acquire a minority interest in Elara Caring | Documentary Fact | [Q1 10-Q] page:17 |
| June 8, 2026 | Ninth Amendment: incremental 500.0 Term Loan B-2 | Documentary Fact | [Q3 10-Q] page:12 |
| July 20, 2026 | Elara Caring investment closed effective (200.0 cash) | Documentary Fact | [Q3 10-Q] page:10 |
| Third quarter 2026 | China goodwill and other asset impairment of 62.2 | Documentary Fact | [Q3 10-Q] page:10, page:41 |
| October 20, 2026 | HHS released a 2026 Kidney Care National Plan (subsequent event) | Documentary Fact | [Q3 10-Q] page:34 |
| October 27, 2026 | Berkshire obligation of 69.0 settled (subsequent event) | Documentary Fact | [Q3 10-Q] page:19 |
| October 28, 2026 | CMS rule for calendar year 2027 ESRD payment issued (subsequent event) | Documentary Fact | [Q3 10-Q] page:37 |
| October 29, 2026 | Q3 2026 Form 10-Q signed and earnings release issued | Documentary Fact | [Q3 10-Q] page:53; [Q3 ER] page:1 |

### Conflicts and unresolved distinctions

| Item | Span 1 | Span 2 | Effect |
| --- | --- | --- | --- |
| Status of the 2027 Medicare rule | [Q3 10-Q] page:37 "CMS) issued a final rule to update the Medicare ESRD Prospective Payment System (PPS) rate and policies for calendar year 2027" | [Q3 10-Q] page:37 "the overall impact of the proposed rule will increase ESRD freestanding facilities’ average reimbursement by 2.7% in 2027" | Logged, not reconciled. Whether the 2.7% is a final or proposed estimate cannot be fixed from this source; CP-2 should treat the 2027 update as an estimate. |
| Two net debt measures | [Q3 ER] page:13 "Net debt, net of cash and cash equivalents(6) $ 10,337" | [Q3 ER] page:15 "Consolidated net debt $ 10,269" | Different company definitions (cash only against cash and short-term investments, excluding deferred compensation amounts). Not a conflict of fact; not reconciled here; CP-1 uses both with labels. |
| Interest measures | [Q3 ER] page:15 "Interest expense 543 540" (last twelve months in Consolidated EBITDA) | [Q3 10-Q] page:2 "Debt expense (150,016) (150,557) (445,403) (431,674)" | Different measures and periods; the difference is not explained in the sources. Not reconciled; carried as a CP-1 gap. |
| Senior notes naming | [Q3 10-Q] page:11 "6.875% Senior Notes 1,000,000" | [10-K] page:213 "Indenture for 6.785% Senior Notes due 2032" | The debt table and exhibit index give different coupons for the notes due 2032. Probably a typographical difference, but logged, not reconciled; the indenture is not supplied. |
| Credit agreement version | [Q1 ER] page:15 "dated November 24, 2025" | [Q3 ER] page:15 "dated June 8, 2026" | Successive amendments to one credit agreement, not a conflict. The base agreement and each amendment are separate documents that are not supplied. |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence |
| --- | --- | --- | --- | --- |
| Revenue durability | U.S. dialysis is 84.9% of segment revenue and 97.3% of segment margin (9M 2026); treatments grew 0.5% | Dialysis is non-discretionary and recurring, so volume is stable, but pricing is set by Medicare and by negotiated commercial rates | High revenue visibility, low upside; earnings depend on reimbursement policy rather than demand | Volume growth is low (0.4% non-acquired in Q3 2026) and commercial revenue grew 1.2% |
| Margin and cash-flow risk | Costs per treatment up 3.0% against revenue per treatment up 2.7% in 9M 2026; expiry of enhanced premium tax credits [Q3 10-Q] page:32 "has had an adverse impact on enrollment in the Affordable Care Act exchanges and our commercial mix" | Wage, supply and insurance inflation outpace rate increases; commercial mix erodes the high-margin payor group | Margin pressure reduces cover on fixed debt service (CP-1) | The company reports it has "experienced productivity improvements" and raised the low end of adjusted operating income guidance ([Q3 10-Q] page:33; [Q3 ER] page:3) |
| Concentration risk | Non-hospital commercial payors are 26% of revenue, 11% of patients and nearly all profits; no payor above 10% | A change in commercial contracting or an adverse regulation of commercial rates hits profit disproportionately | Sensitivity of EBITDA to commercial mix is high even though revenue is diversified | No single commercial payor exceeds 10% of U.S. dialysis revenues |
| Sponsor and owner alignment | No sponsor; Berkshire held to 45.0% and bound by a standstill; large buybacks and no dividends | Equity holders are favoured through repurchases; leverage is managed to a range, not reduced | Alignment with creditors is moderate: no leakage, but no deleveraging priority | Leverage stayed inside the 3.0x to 3.5x range in 2025 and the company discloses its covenant ratio |
| Key uncertainties | HHS Kidney Care National Plan of October 20, 2026; transitional drug add-on payment ending 2026; open False Claims Act, California Department of Insurance, District of Columbia and Federal Trade Commission matters; China impairment | Policy changes can alter reimbursement and competition; legal outcomes are uncertain and unquantified | Event risk to earnings and liquidity, not measurable from the filings | Accruals for legal matters were immaterial at September 30, 2026 ([Q3 10-Q] page:14) |

### Monitoring gaps and consumers

| Item the source set lacks | Severity | Consumer affected |
| --- | --- | --- |
| Credit agreement, amendments and indentures (covenant definitions, baskets, change-of-control terms) | High | CP-2 |
| Subsidiary guarantor list and guarantor financial information | Medium | CP-2 |
| Covenant compliance certificate and Consolidated EBITDA add-back bridge to the agreement | High | CP-2 |
| Berkshire share repurchase agreement and Elara Caring purchase agreement | Low | CP-2, CP-5 |
| Proxy statement (board, beneficial ownership percentages) | Low | CP-5 |
| Ratings and market prices | Low for this scope | CP-2 |

| Consumer | Readiness | Take from this handoff | Why it matters | Gap and action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Segment concentration, commercial-payor profit dependence, unit-margin trend, capped Berkshire ownership, buyback-led capital allocation, and the 2030 and 2031 maturity wall from CP-1 | Capital structure and relative-value work needs the operating drivers behind EBITDA and the owner's behaviour | Obtain the credit agreement and indentures; treat change-of-control and priming capacity as unresolved |
| CP-5 | READY_WITH_LIMITATIONS | Every fact is tagged with a category and a page locator; the 2027 rule status conflict is logged | Claims need traceable evidence | Verify tagged quotes against the filed documents |

## Calculations

All figures are US$ millions from the cited pages unless a percentage or count; sums use unrounded thousands.

- U.S. dialysis share of total net segment revenues, 9M 2026: 9,004.0 / 10,610.1 = 84.9% (ancillary 1,606.1 / 10,610.1 = 15.1%). Share of segment operating margin: 1,588.1 / 1,632.4 = 97.3%; FY2025: 2,084.2 / 2,176.6 = 95.8%; ancillary 9M 2026 share: 44.2 / 1,632.4 = 2.7%.
- U.S. dialysis patient service revenue by payor, 9M 2026 (total 8,984.4): Medicare and Medicare Advantage 5,180.8 / 8,984.4 = 57.7%; Medicaid and managed Medicaid 667.9 / 8,984.4 = 7.4%; other government 271.7 / 8,984.4 = 3.0%; commercial 2,863.9 / 8,984.4 = 31.9%. 9M 2025 (total 8,698.4): 4,983.9 / 8,698.4 = 57.3%; 638.9 / 8,698.4 = 7.3%; 246.8 / 8,698.4 = 2.8%; 2,828.8 / 8,698.4 = 32.5%.
- Payor revenue growth, 9M 2026 over 9M 2025: Medicare and Medicare Advantage 5,180.8 / 4,983.9 - 1 = 4.0%; commercial 2,863.9 / 2,828.8 - 1 = 1.2%.
- Per-treatment growth: revenue 416.22 / 405.15 - 1 = 2.7%; patient care costs 279.24 / 271.23 - 1 = 3.0%.
- Cost ratios, 9M 2026: patient care costs 7,185.3 / 10,547.8 = 68.1%; general and administrative 1,254.1 / 10,547.8 = 11.9%.
- IKC revenue growth: 422 / 352 - 1 = 19.9%; international: 1,156 / 979 - 1 = 18.1% (both as printed rounded millions, [Q3 10-Q] page:40).
- Distributions to noncontrolling interests relative to their income: 243.8 / 201.8 = 121%.
- Berkshire repurchases in 9M 2026: 3,062 thousand shares for 419.3 ([Q3 10-Q] page:18); total repurchases 5,837 thousand shares for 862.5.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement, amendments and indentures not supplied; change-of-control, priming and restricted-payment capacity unknown | High | CP-2 | Supply the executed documents |
| Subsidiary guarantor list not supplied | Medium | CP-2 | Supply Exhibit 21.1 |
| Percentage of shares held by Berkshire and board detail not read or supplied (proxy statement) | Low | CP-5 | Supply the proxy statement |
| Status of the 2027 Medicare payment rule (final or proposed) unclear in the Q3 10-Q | Low | CP-2 | Check the CMS publication when available |
| Quantification of legal and regulatory matters not provided | Medium | CP-2 | Monitor; accruals were immaterial |
| Ratings, market prices and peer data not supplied | Low | CP-2 | Not required for this scope |
| Events after October 29, 2026 not supplied | Medium | CP-2 | Supply later 8-Ks or confirm none |

## Next module

- CP-2: use U.S. dialysis dependence, commercial-payor profit concentration, the unit-margin trend, buyback-led capital allocation and the capped Berkshire holding as drivers of leverage tolerance; carry the missing credit agreement and indentures as the main restriction; treat the 2027 Medicare update as an estimate.
- CP-5: trace each tagged fact to its `page:N` locator; the calculated shares and growth rates are analyst calculations, not source facts.
