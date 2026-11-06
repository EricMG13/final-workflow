# CP-1A — Business and transaction context: Valaris Ltd (val)

## Request

- Issuer: Valaris Ltd (issuer id `val`; the filings name the registrant "Valaris Limited"), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD. Current period Q3 2026; prior period FY2025.
- Run: `val-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Execution: host session; the analyst read the pinned files and wrote this answer. No provider was called.
- Question: which transaction, business, ownership and operating facts matter most to a creditor of Valaris, and what remains unsupported?
- Scope: business and operating model, ownership and governance behaviour, the pending combination with Transocean Ltd., ARO, and the dated timeline. No peer ranking, instrument recommendation or recovery conclusion. No sponsor exists in the supplied sources; the context leaves sponsor, parent, borrower and guarantors blank, which is not evidence that none exist.
- Upstream handoffs read: CP-0 (source readiness: all four consumers READY_WITH_LIMITATIONS) and CP-1 (financial base view). Figures below are those of CP-1 or are quoted from a located source; none is recalculated here.

## Sources

| Source | sha256 | Use in this answer |
| --- | --- | --- |
| 10-K_2025-12-31_val-20251231.htm.jsonl | b0f40796936a513fe6362c5f87d6a2a2819cd2f6e423112bfcf4a7c94647ac50 | Business, customers, risk factors, ARO, Business Combination Agreement terms, history |
| 10-Q_2026-03-31_val-20260331.htm.jsonl | 856b19f20ceb9a456e4cf71dc5d1f96d12072575504148e1684cf5301164037f | Q1 2026 business combination wording (page:11) |
| 10-Q_2026-06-30_val-20260630.htm.jsonl | d045ec4aa0f0c5450f1ffc05520139072532c8f88ec1804bd561ac63d9d380b7 | Q2 2026 business combination wording (page:11) |
| 10-Q_2026-09-30_val-20260930.htm.jsonl | 73a1a96ecd1c9340e41638f2528ea86ae030d4c896022c1e422144610c8461ec | Latest fleet, customers, backlog, ARO, transaction status |
| EX-99.1_2026-05-04_a03312026ex991pressrelease.htm.jsonl | fb13914842f3e3a58a0b5ccdbd3cb04d0eb99161ae6d4b18bdfd3afa295e84b5 | Q1 2026 release (not directly cited; read for trend and consistency) |
| EX-99.1_2026-08-05_a06302026ex991pressrelease.htm.jsonl | 21077052c215c76afaa6a29e3ea89e20e01ee6140be558608fa94290eaa87b1f | Q2 2026 release (not directly cited; read for trend and consistency) |
| EX-99.1_2026-11-02_a09302026ex991pressrelease.htm.jsonl | 649e9df09c58fc28e42170873dd9e204e4698e7b6a16ba8868ab909251dcc271 | Q3 2026 release: management commentary, fleet actions, backlog |
| context | 630c8480b8c6896f51051152fc8ca75c81e04a78fc5ea8aebca9a62a14a6fd8f | Run settings; sector label only; not issuer evidence |

| Handoff | sha256 | Use in this answer |
| --- | --- | --- |
| CP-0 | f373f490427bdb136b51b89f68fd080fb20b9ef4328505ea7636662606abf930 | Readiness view, perimeter, gaps |
| CP-1 | 553419305d3d0840e45db8a53a4ea08f11150ae95be0ecddbcfd829bc1c4363f | Financial figures, debt, liquidity, covenant gap, definitions |

Locators are `page:N`, the chunk number in the pinned `.jsonl`, not the printed page. "Q3 release" is the November 2, 2026 release; "10-Q Q3" is the September 30, 2026 Form 10-Q. Every fact row carries one of four categories: Documentary Fact, Management Language, Analyst Interpretation or Insufficient Information. No external material is used.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Valaris is an offshore driller whose standalone credit picture is overtaken by a pending share-for-share sale to Transocean, expected to close on or about December 1, 2026. Backlog is 4,750.1 and ARO adds off-balance-sheet exposure. | Medium | The combination agreement, financing terms and treatment of the notes and revolver are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Transocean will acquire all Valaris shares at 15.235 Transocean shares each by court-approved scheme, with shareholder meetings on November 24, 2026. | Ownership and covenant context change at closing; the filings do not say what happens to the notes or revolver. | High |
| Revenue rests on day rate contracts; backlog was 4,750.1 on November 2, 2026, and the largest customers are Petrobras, BP and Azule. | Contracted revenue gives visibility, but customer concentration and early termination rights limit its certainty. | Medium |
| ARO, a 50/50 joint venture with Saudi Aramco, owes Valaris notes receivable and may call on Valaris for newbuild funding. | Cash could be needed at ARO while distributions have never been made. | Medium |
| Valaris has paid no dividends and made no share repurchases in 2026, and the combination agreement restricts both and new debt. | Behaviour is not extractive on the documents, but restrictions end at closing or termination. | Medium |
| The Middle East conflict reduced operating income and added insurance cost in 2026. | The effect eased in Q3 2026 but could grow if hostilities widen. | Medium |

### Business and transaction view

Valaris is a Bermuda-incorporated offshore drilling contractor with a fleet of 41 rigs at September 30, 2026: 13 drillships, 21 jackups and 7 jackups leased to ARO. It earns fixed day rates under contracts that customers can terminate in specified circumstances. The credit case rests on contracted deepwater drillship work with a small number of large customers, and on a capital structure of one note series and an undrawn revolver, described in the financial base view.

The central transaction is the pending acquisition of Valaris by Transocean Ltd. under a Business Combination Agreement dated February 9, 2026. It is a share exchange at 15.235 Transocean shares for each Valaris share, implemented by a Bermuda court-approved scheme of arrangement, and no cash consideration is described. Valaris shareholders would own about 47% of the combined company on a fully diluted basis assuming conversion of Transocean's exchangeable bonds due 2029. Shareholder meetings are set for November 24, 2026, a court hearing for November 26, 2026, and closing is expected on or about December 1, 2026. These are expectations, not completed events. For a creditor the important point is what the sources do not say: no supplied document states whether the combination triggers the change-of-control offer in the Indenture, whether the notes or revolver stay in place, or what the combined capital structure is. Until closing, the agreement restricts dividends, share repurchases, asset encumbrance, acquisitions and dispositions, and new or guaranteed debt.

The business view is otherwise stable to improving on management's account, with specific exposures: customer concentration, termination and FID-contingency rights in contracts, Middle East operations, and ARO funding. The view is Medium confidence. The facts are documentary, but the effect of the combination on creditors is not assessable from the supplied sources.

### Company and operating model

| Dimension | Fact | Category | Locator | Risk mechanic and credit implication |
| --- | --- | --- | --- | --- |
| Core activity | Contract drilling of oil and gas wells offshore; rigs may also serve as accommodation units or for well workovers, interventions, plug and abandonment, decommissioning and carbon capture projects | Documentary Fact | 10-K page:9 | Ancillary uses are secondary; the revenue base is day rate drilling, so utilization and day rate drive cash flow |
| Fleet at September 30, 2026 | 41 Valaris rigs: 13 floaters (all drillships), 21 jackups, 7 jackups leased to ARO; ARO owns 9 further jackups and has ordered 4 newbuilds; 12 of 13 drillships are seventh-generation | Documentary Fact | 10-Q Q3 page:28, page:36 | A shrinking older fleet (46 rigs at December 31, 2025) and a modern drillship core support day rates; fewer rigs also mean less operating leverage |
| Segments | Floaters, Jackups, ARO (equity method) and Other (management services and ARO lease arrangements); FY2025 revenues exclusive of reimbursables: Floaters 1,224.1, Jackups 823.4, Other 160.4; ARO at 100 percent 571.0 | Documentary Fact | 10-K page:149; 10-Q Q3 page:28 | Floaters carry the largest revenue and the sharpest swing in utilization, so earnings follow drillship contracting |
| Revenue model | Fixed day rate per contracted day, with lower or zero rates during suspensions and repairs; lump sums for mobilization and upgrades; reimbursables passed through | Documentary Fact | 10-K page:10 | Revenue depends on operating days and uptime; revenue efficiency of 97% in Q3 2026 (management) shows how much contracted rate is earned |
| Termination rights | Contracts may allow early termination for loss, suspension, force majeure, failure of the customer to receive final investment decision, or customer convenience, in some cases without an early termination payment | Documentary Fact | 10-K page:10 | Backlog is not firm cash: it includes contracts subject to FID, so conversion to revenue depends on customer decisions |
| Backlog | 4,750.1 at November 2, 2026 (Floaters 2,904.1, Jackups 1,166.7, Other 679.3); at February 17, 2026 it was 4,672.3, of which 1,703.5 was scheduled for 2026, 1,807.9 for 2027 and 1,160.9 for 2028 and beyond; ARO backlog (100%) 2,198.6 at November 2, 2026 | Documentary Fact | 10-Q Q3 page:35; 10-K page:76; Q3 release page:11 | Visibility supports debt service; the by-year split is stale and the November 2, 2026 split is Not supplied |
| Customers | Five largest customers were 49% of FY2025 revenues; Petrobras 13%, BP 12% and Azule 10% in FY2025; nine months 2026 Petrobras 15%, BP 15%, Azule 13%, Equinor 8% | Documentary Fact | 10-K page:11, page:153; 10-Q Q3 page:30 | Concentration in oil majors and national companies raises loss-of-contract risk; 11 rigs were on national oil company contracts at the 10-K date |
| Geography | 86% of FY2025 revenues were from non-U.S. operations; Q3 2026 fleet: 17 rigs in Middle East and Africa, 13 in Europe, 8 in the Americas, 3 in Asia Pacific | Documentary Fact | 10-K page:11; 10-Q Q3 page:28 | Operations in the Middle East carry conflict, insurance and mobilization risk; see the Middle East row below |
| Utilization and pricing | Fleet utilization 67% in Q3 2026; drillship average daily revenue $469,000 and jackup $131,000 in Q3 2026; floater utilization 58% | Documentary Fact | Q3 release page:12; 10-Q Q3 page:42 | Rising drillship day rates against low utilization show recovery still depends on returning idle rigs to work |
| Middle East | Operating income was reduced by about $24.0 million in Q3 2026 and $62.0 million for nine months 2026, from shipyard delays for two ARO-chartered rigs and higher war-risk insurance | Documentary Fact | 10-Q Q3 page:34 | Escalation could raise insurance cost and cause downtime; the effect moderated in Q3 as both rigs resumed charters |
| Cost structure | Valaris pays rig operating expenses including crew labor, supplies and maintenance; contracts may allow some cost increases to be recovered through day rate adjustment; onshore support costs sit outside segments | Documentary Fact | 10-K page:10; Q3 release page:4 | Fixed costs on idle or stacked rigs weigh on margin; recovery clauses are not available on every contract |
| Capital spending | 2026 capital expenditure expected at $445.0 million to $470.0 million, mainly maintenance and upgrades including contract-specific projects; FY2025 was 343.5 | Documentary Fact | 10-Q Q3 page:52; CP-1 | Customer-specific upgrades commit cash ahead of revenue; spending exceeded operating cash flow in 2026 |
| Working capital | Accounts receivable of 538.1 and current contract liabilities of 129.9 at September 30, 2026 | Documentary Fact | 10-Q Q3 page:29 | Collections from national oil companies and mobilization prepayments move cash between periods |
| Management view | "Fleet utilization is increasing, and all ten of our active drillships are now on contract" | Management Language | Q3 release page:1 | Optimistic characterisation; the filings show utilization at 58% for floaters in Q3 2026, below the active-fleet rate |
| Insurance | Third-party liability cover up to $855.0 million; customers typically indemnify well-control events; limited loss-of-hire cover | Documentary Fact | 10-K page:11 | Uninsured liability above cover and rig damage are retained by Valaris |

### Company profile

| Field | Value | Category | Locator |
| --- | --- | --- | --- |
| Registrant | Valaris Limited, "Bermuda exempted company limited by shares (Bermuda No. 56245)" | Documentary Fact | 10-Q Q3 page:1; Q3 release page:5 |
| Ticker and listing | Common shares VAL and warrants VAL WS on the New York Stock Exchange | Documentary Fact | 10-Q Q3 page:1 |
| Country and sector | Bermuda; offshore contract drilling services. The context labels the sector "Drilling Oil & Gas Wells" | Documentary Fact (sector label from context) | 10-K page:108; context |
| Principal executive office | Richmond House, 12 Par-la-Ville Road, Hamilton, Bermuda in the Q3 2026 10-Q; Clarendon House, 2 Church Street, Hamilton, Bermuda in the FY2025 10-K | Documentary Fact | 10-Q Q3 page:1; 10-K page:1 |
| Commission file number | 1-8097 | Documentary Fact | 10-Q Q3 page:1 |
| Shares outstanding | 69,443,058 common shares at October 29, 2026; 63 shareholders of record at February 1, 2026 | Documentary Fact | 10-Q Q3 page:1; 10-K page:70 |
| Warrants | 5,470,742 outstanding at September 30, 2026, exercise price $131.88, expiring April 29, 2028 | Documentary Fact | 10-Q Q3 page:21 |
| Emergence | Emerged from bankruptcy in 2021; shares first traded on May 3, 2021; 75.0 million common shares and 5.6 million warrants issued on April 30, 2021 | Documentary Fact | 10-K page:50, page:72 |
| Auditor | KPMG LLP, Houston | Documentary Fact | 10-K page:104, page:105 |
| Fleet | 41 rigs at September 30, 2026 (13 drillships, 21 jackups, 7 jackups leased to ARO); 46 rigs at the date of the 10-K | Documentary Fact | 10-Q Q3 page:28; 10-K page:108 |
| Affiliate | ARO (Saudi Aramco Rowan Offshore Drilling Company), 50/50 unconsolidated joint venture with Saudi Aramco | Documentary Fact | 10-K page:108, page:122 |
| Workforce | Approximately 5,070 persons including contractors and approximately 3,800 excluding contractors at December 31, 2025 | Documentary Fact | 10-K page:15 |
| Ratings | Not supplied; the context ratings field is empty | Insufficient Information | context |

### Transaction summary and new debt issues

The one transaction in the sources is the pending business combination with Transocean Ltd., a Swiss corporation. The Business Combination Agreement was entered into on February 9, 2026 (10-Q Q3 page:11). Transocean will acquire all issued and outstanding common shares of Valaris in exchange for Transocean shares at an exchange ratio of 15.235 Transocean shares for each Valaris share, by a court-approved scheme of arrangement under section 99 of the Companies Act 1981 of Bermuda (10-K page:8). Outstanding warrants will be assumed by Transocean and remain exercisable for the Fundamental Transaction Consideration as defined in the Warrant Agreement dated April 30, 2021 (10-Q Q3 page:11). On a fully diluted basis assuming conversion of Transocean's exchangeable bonds due 2029, Transocean shareholders would own approximately 53% and Valaris shareholders 47% of the combined company (10-Q Q3 page:11). The type is a stock-for-stock acquisition of Valaris. There is no sponsor, no cash consideration and no use of proceeds in the sources.

Status. Closing is subject to Valaris and Transocean shareholder approvals, a Bermuda sanction order, NYSE listing of the new Transocean shares, regulatory approvals or expiry of waiting periods, no legal prohibition, and the absence of a material adverse effect (10-Q Q3 page:12). Shareholder meetings for both companies are scheduled for November 24, 2026 and the Bermuda sanction hearing for November 26, 2026; closing is expected on or about December 1, 2026 (10-Q Q3 page:12; Q3 release page:1). Management states that the combination "has received the required regulatory approvals" (Q3 release page:1). These dates are expectations at the cutoff; no document dated after November 3, 2026 is supplied.

Terms that matter to creditors. A termination fee of $173.0 million is payable by Valaris in specified circumstances; if Valaris shareholders fail to approve and that fee is not otherwise payable, Valaris must reimburse Transocean's transaction expenses up to $58 million (10-K page:22). Either party may terminate if the effective time has not occurred by February 9, 2027, subject to extension (10-K page:22). Valaris is restricted from soliciting alternative proposals and cannot terminate to accept a superior proposal (10-K page:23). Interim covenants restrict amending organizational documents, declaring dividends or repurchasing shares, encumbering assets, acquisitions and dispositions, incurring or guaranteeing indebtedness, and entering or amending material contracts (10-K page:24). Merger and integration expenses were 15.5 in Q3 2026 and 40.5 for nine months 2026 (10-Q Q3 page:12), per the financial base view.

Effect on debt: Not supplied. A search of all seven sources for refinancing, assumption of debt, and the Indenture's change-of-control provision found only the Indenture's 101.0% repurchase offer on a Change of Control Triggering Event (10-K page:127, as set out in the financial base view). No source states whether that event occurs on closing, whether the notes or revolver are repaid, assumed or amended, or what Transocean's own capital structure is. Transocean's financial statements and the Business Combination Agreement itself are not supplied. A creditor therefore cannot size the post-closing leverage, and the standalone figures are the only quantified base.

New debt issues. No new debt was issued in FY2025 or the first nine months of 2026: the cash flow statements show no debt issuance, and the only financing flows are share repurchases in 2025, tax withholdings and a small other item in 2026 (10-K page:107; 10-Q Q3 page:10). The outstanding notes were issued in 2023 and are described in the financial base view. Subsequent events after September 30, 2026 are limited to what the Q3 release and the 10-Q state: the start of the VALARIS DS-18 contract and the shareholder and court dates above.

### Ownership and governance behaviour

| Area | Fact | Category | Locator | Mechanic and implication |
| --- | --- | --- | --- | --- |
| Ownership class | Listed company; no controlling holder or sponsor is named in the supplied sources; 63 holders of record, many shares held through a nominee of the Depository Trust Company | Documentary Fact | 10-K page:70 | Control by a single holder cannot be inferred; major holders are Not supplied (proxy statement not in the pack) |
| Post-closing ownership | About 53% Transocean shareholders and 47% Valaris shareholders on a fully diluted basis assuming conversion of Transocean's exchangeable bonds due 2029 | Documentary Fact | 10-Q Q3 page:11 | Control of the combined group would pass to Transocean's existing holders on that basis; creditor control rights depend on documents not supplied |
| Distributions | "We have not paid or declared any dividends on our Common Shares"; the Indenture and revolver limit dividends and the combination agreement restricts them until completion or termination | Documentary Fact | 10-K page:70 | No debt-funded distribution is documented |
| Share repurchases | Repurchase program of up to $600.0 million; 100.0 repurchased in FY2025 (25.0 in Q4 2025) and none in the three and nine months of 2026; about $175.0 million remained available at September 30, 2026 | Documentary Fact | 10-Q Q3 page:24, page:54; 10-K page:130 | Repurchases used cash in 2025; the last printed repurchase was in Q4 2025 and none followed; the agreement bars them while in effect |
| Asset sales | Rig sales in 2025 and 2026 including VALARIS 104 for cash proceeds of $40.0 million (June 2026) and VALARIS DPS-1 for $10.1 million (Q2 2026) | Documentary Fact | 10-Q Q3 page:19 | Disposals recycle older rigs; asset sales are restricted by the Indenture and the combination agreement |
| Creditor-adverse actions | No priming, uptiering, drop-down, non-pro-rata exchange, liability management or collateral release is described in the supplied sources; a search of all seven for these terms found none | Insufficient Information | all sources | Absence of evidence in a limited pack; not a conclusion that none occurred |
| Disclosure | Quarterly 10-Q and release reporting continues; the Q3 release says no future earnings calls or guidance updates will be provided because of the pending combination | Documentary Fact | Q3 release page:5 | Reduced forward information for creditors until closing |
| ARO reporting | Valaris recorded $14.3 million of additional equity income from ARO's adjustments "during the completion of its 2025 financial statements subsequent to the issuance of our Annual Report" | Documentary Fact | 10-Q Q3 page:16, page:41 | ARO's statements were finalized after Valaris filed its 10-K; the 10-K risk factor notes ARO may be unable to produce timely and accurate statements (10-K page:39) |
| Anti-takeover and activism | Bye-law provisions could make acquisition of control harder; the 10-K cites risk from activist campaigns | Documentary Fact | 10-K page:56, page:57 | Limited relevance to creditors beyond management distraction cost |
| Behaviour category | Neutral or Mixed on documented actions: no distributions or creditor-adverse transactions found, offset by past repurchases and the limited information after signing | Analyst Interpretation | 10-K page:70, page:130; 10-Q Q3 page:54 | Assessment of willingness only; legal capacity under the debt documents is Not supplied and feasibility is described in the financial base view |

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| April 30 to May 3, 2021 | Emergence from bankruptcy; shares and warrants issued; shares first traded May 3, 2021 | Documentary Fact | 10-K page:50, page:72 |
| April 2023 | Issued $700.0 million of 2030 Second Lien Notes at par and entered into the 2028 Credit Agreement | Documentary Fact | 10-Q Q3 page:21 |
| May 3, 2023 | Redeemed the 2028 First Lien Notes for an aggregate redemption price of $571.8 million | Documentary Fact | 10-K page:126 |
| August 2023 | Issued a further $400.0 million of the same series at 100.75% of par | Documentary Fact | 10-Q Q3 page:21 |
| October 2023 | ARO entered into a $359.0 million term loan | Documentary Fact | 10-Q Q3 page:55 |
| 2024 | Three ARO drilling contracts (VALARIS 143, 147 and 148) were terminated and the rigs returned to Valaris and stacked | Documentary Fact | 10-K page:40 |
| 2025 | Sold VALARIS 247, 75, 102 and 145 and three semisubmersibles (DPS-3, DPS-5, DPS-6); in the fourth quarter approved a plan to retire VALARIS DPS-1 | Documentary Fact | 10-K page:80, page:125 |
| December 2025 | Interest of $24.1 million owed by ARO on the Notes Receivable from ARO was paid in kind | Documentary Fact | 10-K page:91 |
| February 9, 2026 | Business Combination Agreement signed with Transocean | Documentary Fact | 10-Q Q3 page:11 |
| February 20, 2026 | FY2025 10-K filed | Documentary Fact | 10-K page:163 |
| April 30, 2026 | Optional redemption of the notes becomes available at 104.188% | Documentary Fact | 10-K page:127 |
| Q2 2026 | Sold VALARIS 104 and VALARIS DPS-1; obtained an approximately $75.0 million customs bond for VALARIS DS-10 | Documentary Fact | 10-Q Q3 page:19, page:55 |
| August 2026 | ARO ordered Kingdom 5 and Kingdom 6 | Documentary Fact | 10-Q Q3 page:56 |
| September 2026 | Sold VALARIS MS-1 and VALARIS 111; VALARIS DS-15 started a new contract; no semisubmersibles remain | Documentary Fact | Q3 release page:3; 10-Q Q3 page:36 |
| November 2, 2026 | Q3 results released | Documentary Fact | Q3 release page:1 |
| After September 30, 2026 (Subsequent event) | VALARIS DS-18 started a contract | Documentary Fact | Q3 release page:1 |
| November 24 and 26, 2026 (forward) | Shareholder meetings and Bermuda sanction hearing | Management Language | 10-Q Q3 page:12 |
| On or about December 1, 2026 (forward) | Expected closing of the combination | Management Language | 10-Q Q3 page:12 |
| February 9, 2027 (forward) | Outside date for the agreement, subject to extension | Documentary Fact | 10-K page:22 |

### ARO and related-party exposure

| Item | Fact | Category | Locator | Mechanic and implication |
| --- | --- | --- | --- | --- |
| Structure | ARO owns and operates jackups in Saudi Arabia; at September 30, 2026 it owned 9 jackups, had ordered 4 newbuilds and leased 7 rigs from Valaris under bareboat charters | Documentary Fact | 10-Q Q3 page:15 | Seven Valaris rigs depend on ARO's Saudi Aramco contracts; a suspension of those contracts returned rigs to Valaris in 2024 |
| Notes Receivable from ARO | Principal 400.7, carrying value 363.4 at September 30, 2026, maturing October 2027 and October 2028, subordinated to ARO's term loan and credit facility, governed by Saudi law; enforcement requires the joint venture partner's consent; Valaris expects to extend maturities | Documentary Fact | 10-Q Q3 page:17, page:54, page:55; 10-K page:39 | Repayment depends on ARO's liquidity: ARO had cash of $32.1 million at September 30, 2026 and has never paid a distribution |
| Newbuild funding | Valaris may be required to contribute up to a maximum of $1.25 billion in aggregate to fund the newbuild program, reduced to $1.1 billion after Kingdom 2 | Documentary Fact | 10-Q Q3 page:56 | A contingent call on Valaris liquidity if ARO cannot raise third-party financing, outside the reported debt figure |
| ARO debt | $359.0 million term loan (eight years, 50% balloon) and a revolving credit facility of up to $150.0 million with $50.0 million outstanding | Documentary Fact | 10-Q Q3 page:55 | ARO's lenders rank ahead of the notes receivable; no Valaris guarantee of ARO borrowings is printed in the pages searched |
| Backlog link | ARO backlog (100%) 2,198.6 includes rigs leased from Valaris; Valaris recognizes 50% of ARO earnings as equity income | Documentary Fact | 10-Q Q3 page:35 | ARO earnings are a non-cash equity item that reaches Valaris only through distributions or repayment |

### Differences and conflicts between sources

| Item | Source A | Source B | Treatment |
| --- | --- | --- | --- |
| Use of VALARIS 111 | Q3 release page:1: sale of "long-term stacked jackup VALARIS 111 for conversion to a mobile offshore production unit" | 10-Q Q3 page:18: "we entered into an agreement to sell VALARIS 111, a rig within our Jackups segment, for recycling for $1.7 million" | Logged, not reconciled. The 10-Q controls the accounting; the amount is small |
| Regulatory approval status | 10-Q Q3 page:12: regulatory approvals "expected to be satisfied by November 3, 2026" | Q3 release page:1: the combination "has received the required regulatory approvals"; 10-Q Q3 page:32: all required approvals obtained and waiting periods "expected to expire or terminate" | Different wording of one status, not a numeric conflict. Logged; confirmation is Not supplied |
| Principal office | 10-K page:1: Clarendon House, 2 Church Street | 10-Q Q3 page:1: Richmond House, 12 Par-la-Ville Road | Change of address between filings, not a conflict of facts |
| Business Combination wording | 10-K page:8 and page:22 | 10-Q Q3 page:11 and page:12 | Consistent on ratio, ownership split and fee; the 10-Q adds the November 24 and 26, 2026 dates |

### Credit translations

- Revenue durability. Evidence: backlog of 4,750.1 at November 2, 2026 against 4,672.3 at February 17, 2026 (10-Q Q3 page:35), with contracts that may be terminated for convenience or lack of FID (10-K page:10). Mechanic: contracted day rates give revenue visibility for debt service, but termination rights and the FID contingency make part of the backlog conditional. Implication: contracted revenue supports near-term liquidity while the notes do not mature before 2030; the conditionality argues against treating backlog as committed cash. Counter-evidence: none logged; the backlog by year at November 2, 2026 is Not supplied.
- Margin and cash flow risk. Evidence: drillship average daily revenue rose to $469,000 in Q3 2026 while floater utilization was 58% (Q3 release page:12), and capital expenditure above operating cash flow in 2026 per the financial base view. Mechanic: idle or stacked rigs carry fixed cost, and contract-specific upgrades precede revenue. Implication: improving drillship contracting should lift cash flow, but liquidity depends on those rigs starting work on schedule.
- Concentration. Evidence: five customers at 49% of FY2025 revenues and 11 rigs on national oil company contracts (10-K page:11, page:45). Mechanic: loss or renegotiation of one contract is material, and national oil company terms can be non-negotiable. Implication: tail risk on any single contract; no customer credit assessment is supplied.
- Transaction and creditor control. Evidence: the stock-for-stock combination, the Indenture's change-of-control offer at 101.0%, and the silence of the sources on debt treatment. Mechanic: closing could trigger noteholder rights or change covenant tests, and interim covenants limit new debt until closing. Implication: standalone credit metrics may not describe the issuer after December 1, 2026. This is the key uncertainty.
- ARO. Evidence: notes receivable, newbuild funding commitment, and ARO's thin cash against rising newbuild orders (10-Q Q3 page:54 to page:56). Mechanic: an unconsolidated affiliate can draw on Valaris cash without appearing in debt. Implication: contingent liquidity use; the commitment is a maximum, not an expected call.
- Sponsor alignment. Evidence: no sponsor, no dividends, no repurchases in 2026. Mechanic: no extraction channel is documented. Implication: neutral; behaviour after closing is Not supplied.

### Consumer readiness

| Consumer | Readiness | What to take from this answer | Gap and action |
| --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Business risk drivers, the transaction as central uncertainty, ARO as contingent exposure, concentration and termination rights | Debt treatment in the combination and covenant levels are Not supplied; carry as restrictions |
| CP-5 | READY_WITH_LIMITATIONS | Locators for each row; conflicts logged as differences | Check the three differences above against the filed HTML if needed |

## Calculations

No new calculation. Figures are those of the financial base view (CP-1) or are quoted from located sources. The count of 41 Valaris rigs equals the table total in 10-Q Q3 page:28 (13 floaters, 21 jackups, 7 other). The post-closing ownership split of 53% and 47% is quoted, not derived.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Business Combination Agreement, scheme document and any proxy not supplied; treatment of the notes, revolver and change-of-control provision not stated | High | CP-2, CP-5 | Obtain the agreement and scheme or proxy documents |
| Transocean financial statements and capital structure not supplied | High | CP-2 | Obtain Transocean's filings |
| Backlog by year at November 2, 2026 not supplied (only the February 17, 2026 split) | Medium | CP-2 | Obtain backlog schedule from the next filing |
| Major shareholders and board composition detail not supplied (proxy statement not in the pack) | Low | Governance | Obtain the 2026 proxy statement |
| Customer credit quality and contract-level terms (day rates, durations, termination payments) not supplied | Medium | CP-2 | Obtain fleet status report and contract disclosures |
| ARO standalone financial statements and its debt documents not supplied; no ARO distribution history beyond the statement that none has been made | Medium | CP-2 | Obtain ARO statements |
| Events between November 3, 2026 and the cutoff not supplied (including shareholder voting outcomes, which fall after the cutoff) | Medium | CP-2 | Obtain later 8-Ks if available |
| Differences on VALARIS 111 and regulatory approval wording are logged, not resolved | Low | CP-5 | Confirm against filed documents |

## Next module

- CP-2: use the business and transaction view as the business-risk basis. Carry as restrictions: debt treatment in the combination Not supplied; covenant levels Not supplied; ARO exposure described from Valaris's disclosure only; backlog is a management measure including FID-contingent contracts.
- CP-5: trace each row to its locator; the CP-1 figures repeated here must match CP-1 exactly; treat the VALARIS 111 and regulatory wording differences as logged.
