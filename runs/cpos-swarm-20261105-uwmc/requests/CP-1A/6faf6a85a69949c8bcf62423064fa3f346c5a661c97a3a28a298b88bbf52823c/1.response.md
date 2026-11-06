# CP-1A — Business and transaction context: UWM Holdings Corp (uwmc)

## Request

- Issuer: UWM Holdings Corp (UWM Holdings Corporation, NYSE "UWMC"), as of 2026-11-05, information cutoff 2026-11-05, pathway credit_snapshot, reporting currency USD.
- Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Question: which transaction, ownership, business and operating facts matter most to a creditor, and what has changed? Required drivers: transaction and ownership structure; business and operating model; credit-relevant history or change.
- Perimeter: UWM Holdings Corporation ("UWMC") and its consolidated subsidiaries; UWMC's only material direct asset is its Class A units of UWM Holdings, LLC ("Holdings LLC"), which owns 100% of United Wholesale Mortgage, LLC ("UWM"), the operating subsidiary (Q2 10-Q `page:6`).
- Fact categories used: Documentary Fact (the cited source states it), Management Language (management's characterisation, quoted and not adopted), Analyst Interpretation (the host's reading of cited evidence), Insufficient Information (the evidence is missing). Amounts are US$ and carry the units of the cited source; amounts that CP-1 accepted are repeated as in CP-1.
- Locators are `page:N` of the pinned `.jsonl` text. "10-K" is the annual report for FY2025; "Q1 10-Q" and "Q2 10-Q" are the Forms 10-Q for March 31 and June 30, 2026; "Q1 release" and "Q2 release" are the Exhibit 99.1 press releases of May 6 and August 5, 2026; "deck" is the February 2026 earnings presentation. All material is external to this host session and comes only from these pinned sources.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_uwmc-20251231.htm.jsonl | 6df0e879c343753ce405aeb907aabeaeac058e835b89efb10be5b5f6ef447e2d | Business, strategy, risk factors on control and the Tax Receivable Agreement, Two Harbors merger note, related-party note |
| 10-Q_2025-09-30_uwmc-20250930.htm.jsonl | 84f53b3c261a44ff2b63ce2fd8da76aab14001838b1a0e3a2f304e513f9c0145 | Read for history only (Q3 2025); no fact in this answer depends on it |
| 10-Q_2026-03-31_uwmc-20260331.htm.jsonl | eb1fccb72198e8bd32b24af480098c49a4e103fa66da8e8b43ba0a46fdd7b8e3 | Terminated Two Harbors merger, exchange transactions, Ginnie Mae facility amendment |
| 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | cea2518652546d9284379186814d587a8012203f70fc41bfc3b1a399bf834746 | Subsequent-event note on the August 5, 2026 capital transaction, ownership table, related parties, legal proceedings |
| EX-99.1_2026-02-26_irdeck4q25andfy2025-fina.htm.jsonl | 80372136ddaf727708bb7d020bd60e922c0bc6f80a8ff31bd92d35cba8e5b9c2 | Management presentation: strategy, the Two Harbors transaction as then pending (management claims only) |
| EX-99.1_2026-05-06_q12026ex-991pressrelease.htm.jsonl | 3516810c7f76bb754add7c9c09ef459031d4e398744e48f97ba6a9a478ed6c73 | Management release: in-house servicing progress, Bilt collaboration |
| EX-99.1_2026-08-05_q22026ex-991pressrelease.htm.jsonl | fce3d1caab58675ec9b80c128baca52e2510780e5b4d2dc29c8a0ea2b81bebde | Management release: Oaktree equity investment, dividend suspension |
| context | 9e4b4c779a926897468f1dfd198d157aa081551eb0aa185c7568e6564f764c9f | User run settings; not issuer evidence. Transaction, deal-term, quote and rating fields are empty, which is not evidence of absence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2571b7e9360f6c0ea273bba21e1fe841a47b3e684ddd02e1c3fe019c258d1214 | Source readiness: no transaction agreements, indentures or facility agreements supplied; nothing after August 7, 2026 |
| CP-1 | e7bf0105a6381159660f32f084ad2d84b72887c85873222b32d56f78e390c03a | Accepted financial base: non-funding debt of 6,040.4 million, LTM Adjusted EBITDA of 790.6 million, liquidity, maturities |

Consistency with CP-0 and CP-1: this answer confirms both. It adds one conflict neither logged: the Q2 release prints first-quarter 2026 purchase "Jumbo and other" originations as 1,143,526 (US$ thousands) while the Q1 release prints 1,443,526, which is the figure that sums to the printed purchase total. No earlier statement is corrected.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| UWM is a wholesale-only mortgage originator controlled by SFS Corp., which holds 78.7% of the operating holding company. The August 2026 preferred raise of 1.65 billion adds junior capital, but its redemption terms are not supplied. | Medium | Transaction agreements, preferred terms and the Two Harbors termination terms are not supplied; only note and press-release summaries exist. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| SFS Corp. holds 78.7% of Holdings LLC and about 79% of voting power, so UWM is a controlled company. | Control sits outside the creditor group; the same owner lends a subordinated revolver and receives tax receivable payments. | High |
| The Two Harbors merger agreement of December 2025 was terminated in the first quarter of 2026 and a termination fee was received. | The planned 247 million share issuance and servicing acquisition did not happen, but deal costs still reached second-quarter expenses. | High |
| A 1.65 billion preferred and warrant raise closed on August 5, 2026, carrying 10.0% cash or 13.0% non-cash dividends; a 400 million rights offering is contingent. | Junior capital supports liquidity but adds a fixed dividend claim whose redemption rights are not supplied. | Medium |
| Cash paid to equity holders was 321.8 million in the first half of 2026, against a net loss of 281.5 million; the dividend was suspended after June 30, 2026. | Distributions to the controlling holder continued through a loss period; sponsor behavior reads as mixed. | Medium |
| Management says substantially all loans will be serviced in-house by October 2026; the 10-K says one sub-servicer services the portfolio. | Servicing transition is an execution and compliance risk on a 5,311.5 million asset. | Medium |

### Business and transaction view

UWM Holdings Corp is the listed top holding company of a wholesale-only residential mortgage lender, so its creditors are exposed to one volume-driven business that earns through gain on sale, a retained servicing portfolio and net interest, and that is controlled by a single holder. The operating subsidiary originates only through independent mortgage brokers, sells about 93% of loans into Fannie Mae, Freddie Mac or Ginnie Mae pools, and keeps the servicing rights on most of them, which is why the servicing-rights asset of 5,311.5 million and the borrowings against it dominate the funding story. Control rests with SFS Corp., an entity controlled by the CEO: it holds 78.7% of the economic units of Holdings LLC and, as the 10-K states, about 79% of voting power, and it is also the lender under the unsecured revolver, the counterparty to the Tax Receivable Agreement, and the recipient of member distributions. The decisive recent changes are two. First, the planned acquisition of Two Harbors Investment Corp., signed on December 17, 2025 and described in the 10-K as expected to close in the second quarter of 2026, was terminated in the first quarter of 2026 with a termination fee received, so the share issuance of roughly 247 million Class A shares and the added servicing portfolio did not occur. Second, on August 5, 2026, after a second quarter in which derivative losses drove a net loss of 451.9 million, the company closed a 1.65 billion preferred stock and warrant issue to Oaktree and a vehicle of the CEO's family, suspended the quarterly dividend, and announced a contingent 400 million rights offering. These actions add junior capital beneath the debt, but the filings supplied describe the preferred terms only in summary, and the effects are not in any reported financial statement. A creditor should therefore treat the capital raise as a material, documented positive for liquidity and loss absorption whose strength depends on terms that are not in the pack, while keeping the controlled-company structure, related-party flows and the in-house servicing transition as the main governance and execution uncertainties.

### Company and operating model

| Area | Fact | Measure and period | Category | Locator | Credit relevance |
| --- | --- | --- | --- | --- | --- |
| Core activity | Originates, sells and services residential mortgage loans, exclusively through the wholesale channel; UWM does not work directly with the borrower | Single operating segment | Documentary Fact | 10-K `page:8`; Q2 10-Q `page:7` | One-business exposure; volume and margin set earnings |
| Market position claim | Describes itself as the largest overall and largest wholesale lender in the US by closed loan volume | Management claim; not tested against a third party | Management Language | Q2 10-Q `page:34`; 10-K `page:9` | Not adopted; no peer ranking is made here |
| Customers | Independent mortgage brokers: over 13,000 broker businesses, over 57,000 loan officers, about 35,000 of them submitted a loan in 2025 | 2025 | Documentary Fact | 10-K `page:9` | Distribution depends on broker loyalty; share of volume by largest broker is Not disclosed |
| Products and end markets | Primarily conforming and government loans in all 50 states and the District of Columbia; purchase 23,772,593 and refinance 15,929,671 of Q2 2026 originations (US$ thousands) | Q2 2026 | Documentary Fact | Q2 10-Q `page:34`, `page:40` | Refinance share moves with rates; purchase is described by management as less volatile |
| Revenue model | Loan production income (primary gain or loss, fees, capitalized servicing rights), loan servicing income and interest income | Q2 2026 revenue 888,003 (US$ thousands) | Documentary Fact | Q2 10-Q `page:3`, `page:35` to `page:36` | Capitalized servicing rights are a non-cash component of production income |
| Pricing and margin | Total gain margin is loan production income divided by origination volume | 1.33% in Q2 2026, 1.13% in Q2 2025 | Documentary Fact | Q2 release `page:2`; Q2 10-Q `page:40` | Margin competition is the main earnings sensitivity |
| Volume drivers | Originations flat year on year in Q2 2026 at 39.7 billion; refinance volume fell from the first quarter | Q2 2026 against Q2 2025 and Q1 2026 | Documentary Fact | Q2 release `page:1` | Rate-sensitive refinance share |
| Funding model | About 2-3% of each loan funded with own funds and the rest through warehouse lines; most loans stay on a line under one month; loans are pledged to the lender | Warehouse lines 8,600,078 (US$ thousands) at June 30, 2026 | Documentary Fact | Q2 10-Q `page:35`, `page:49` | Short-dated secured funding that must be renewed and can be margin-called |
| Servicing portfolio | Retains servicing on most production (95% servicing-retained in Q2 2026); sells servicing opportunistically in bulk | Servicing rights 5,311,465 (US$ thousands); UPB serviced 247,648,881 | Documentary Fact | Q2 10-Q `page:12`, `page:40`, `page:42` | Large asset financed by uncommitted secured lines |
| Servicing operations | One sub-servicer at the 10-K date; in-house servicing platform being built; 10-K expected substantially all loans to transition by the end of 2026; Q1 release says all new loans are on the platform and substantially all loans are on pace to be serviced in-house by October 2026 | As stated | Management Language | 10-K `page:17`, `page:45`; Q1 release `page:2` | Transition is an execution, licensing and agency-compliance risk; counterparty concentration in the sub-servicer is a stated risk factor |
| Hedging | Pipeline hedged mainly with forward agency TBA sales; separate interest rate derivatives used for the servicing portfolio | Other interest rate derivative notional 12,805,000 (US$ thousands) at June 30, 2026; loss 603,191 in Q2 2026 | Documentary Fact | Q2 10-Q `page:11`, `page:44` to `page:45`, `page:65` | Hedge results drive net income volatility outside Adjusted EBITDA |
| Cost structure | Salaries, commissions and benefits are the largest expense line; about 9,100 team members at December 31, 2025, nearly all at the Pontiac, Michigan campus | FY2025 salaries 851,213 of total expenses 2,152,351 (US$ thousands) | Documentary Fact | 10-K `page:22`, `page:127` | Largely fixed headcount against variable volume |
| Capital spending | Purchases of premises and equipment, including internal-use software | 74,048 in FY2025 and 28,525 in H1 2026 (US$ thousands) | Documentary Fact | 10-K `page:129`; Q2 10-Q `page:5` | Small relative to servicing-rights capitalization |
| Working capital | Mortgage loans at fair value 9,619,076 and servicing advances; margin deposits | June 30, 2026 (US$ thousands) | Documentary Fact | Q2 10-Q `page:2`, `page:11` | Inventory is financed by warehouse lines |
| Concentration | 93% of loans sold to GSEs or transferred to Ginnie Mae pools in Q2 2026; dependence on GSE and agency policy | Q2 2026 | Documentary Fact | Q2 10-Q `page:34`, `page:63` | Agency eligibility drives liquidity |
| Largest-broker concentration | Not disclosed in the sources | Not disclosed | Insufficient Information | Searched for top broker, largest client and concentration | Cannot size the loss of a large broker |

### Company profile

| Field | Value | Category | Locator |
| --- | --- | --- | --- |
| Registrant | UWM Holdings Corporation, a Delaware corporation; Commission file number 001-39189 | Documentary Fact | Q2 10-Q `page:1` |
| Operating subsidiary | United Wholesale Mortgage, LLC, a Michigan limited liability company, 100% owned by Holdings LLC | Documentary Fact | Q2 10-Q `page:6` |
| Listing | Class A common stock on the New York Stock Exchange, symbol UWMC; listed since January 22, 2021 | Documentary Fact | Q2 10-Q `page:1`; 10-K `page:8` |
| Sector and country | Mortgage bankers and loan correspondents; United States (context). The filings describe residential mortgage origination and servicing | Documentary Fact | context; 10-K `page:8` |
| Headquarters | 585 South Boulevard E., Pontiac, Michigan | Documentary Fact | Q2 10-Q `page:1` |
| History | Founded in 1986, privately owned for 35 years; business combination with Gores Holdings IV, Inc. completed January 21, 2021 | Documentary Fact | 10-K `page:8` |
| Employees | About 9,100 at December 31, 2025 | Documentary Fact | 10-K `page:22` |
| Shares outstanding at August 4, 2026 | 342,349,795 Class A and 1,261,862,603 Class D | Documentary Fact | Q2 10-Q `page:1` |
| Chairman, President and CEO | Mat Ishbia (title as stated in the 10-K risk factor and the Q2 release); CFO signing the Q2 10-Q is Rami Hasani, Executive Vice President | Documentary Fact | 10-K `page:44`; Q2 10-Q `page:72` |
| Auditor | Deloitte & Touche LLP, auditor since 2020; opinion that the FY2025 statements present fairly and an unqualified opinion on internal control | Documentary Fact | 10-K `page:123` to `page:125` |
| Filer status | Large accelerated filer; fiscal year ending December 31 | Documentary Fact | Q2 10-Q `page:1` |
| Sponsor | None named; the controlling holder is SFS Corp. (context sponsor field is blank) | Documentary Fact | Q2 10-Q `page:6`; context |
| Ratings | Not supplied: the context ratings list is empty and no filing prints a rating | Insufficient Information | context |

### Ownership and control

| Item | Fact | Category | Locator |
| --- | --- | --- | --- |
| Up-C structure | UWMC is the manager of Holdings LLC and holds its Class A units; SFS Corp. holds Class B units and an equal number of Class D shares ("Paired Interests"); Class D has ten votes per share and no economic rights | Documentary Fact | Q2 10-Q `page:6` |
| Economic interest | UWMC holds 342,247,135 units (21.3%); SFS Corp. holds 1,261,862,603 units (78.7%) at June 30, 2026, against 16.8% and 83.2% at December 31, 2025 | Documentary Fact | Q2 10-Q `page:22` to `page:23` |
| Voting control | SFS Corp. controls approximately 79% of combined voting power "based on the Voting Limitation", and 99% without it; it can determine corporate actions while it owns at least 10% of outstanding common stock | Documentary Fact | 10-K `page:73` |
| Controlled company | Controlled-company exemptions are available; three of ten directors independent, no majority of independent directors, no solely independent compensation or nominating committee | Documentary Fact | 10-K `page:74` |
| Exchange mechanics | SFS Corp. may exchange Paired Interests for Class B shares or cash at the company's option; 69,620,017 Class B shares were issued and converted to Class A in H1 2026 | Documentary Fact | Q2 10-Q `page:23` |
| Public float | SFS Corp. sold shares under Rule 10b5-1 plans adopted March 17 and September 16, 2025, "as part of its strategy to increase public float"; all plans were terminated, the latest effective May 8, 2026 | Documentary Fact | Q2 10-Q `page:71` |
| Tax Receivable Agreement | UWMC pays SFS Corp. 85% of realized cash tax savings from exchange-related basis increases and related items; liability 279,995 (US$ thousands); on a change in control or material breach UWMC must pay the present value of future payments | Documentary Fact | Q2 10-Q `page:8`, `page:21`; 10-K `page:71` |
| New investor | Oaktree gets the right to appoint two directors (one independent) for as long as it holds the Minimum Threshold of Series A-1 Preferred | Documentary Fact | Q2 10-Q `page:32` |
| Prior ownership and recapitalisation history | Privately owned before January 2021; no dividend recapitalisation is described in the sources | Insufficient Information | 10-K `page:8` |
| Voting power after 2025 and after the August 2026 transaction | The 79% and 99% figures are as of the 10-K date; the effect of exchanges since then and of the Series A-1 governance rights on voting power is not restated | Insufficient Information | 10-K `page:73` |

### Governance and sponsor behaviour

Assessment is of issuer-level behaviour from documented actions only, not of individuals, and the identity of the owner is not used as evidence of willingness. Legal capacity (what documents permit), willingness (what was done) and feasibility (liquidity, leverage, market access) are kept separate.

| Documented action | Mechanic | Behaviour category | Legal capacity, willingness, feasibility | Evidence quality | Locator |
| --- | --- | --- | --- | --- | --- |
| September 2025 Amendment No. 1 subordinated the 500.0 million unsecured revolver from SFS Corp. to the senior notes and restricted payment and remedies on a senior note event of default | Owner credit ranked behind the senior notes; but the facility is undrawn, so its protective value depends on later use | Supportive | Capacity: the subordination is contractual (agreement not supplied). Willingness: signed by the owner. Feasibility: untested while undrawn | High | Q2 10-Q `page:19` |
| Member distributions to SFS Corp. and Class A dividends paid in loss periods: 321.8 million in H1 2026 against a net loss of 281.5 million; 126.2 million of distribution and 34.2 million of dividend approved in Q2 and paid July 9, 2026 | Cash leaves the group in step with dividends and for the owner's tax liabilities, while secured borrowing rose; the share that is tax distribution is not split out | Neutral or Mixed | Capacity: the operating agreement has the board choose proportional distributions with each dividend (10-K `page:85`) and generally requires tax distributions (Q2 10-Q `page:48`). Willingness: approved with the Q2 dividend and paid July 9, 2026. Feasibility: paid from cash and borrowings | High | Q2 10-Q `page:5`, `page:59` |
| Quarterly dividend suspended after June 30, 2026 | Reduces ongoing cash leakage to public holders; the release does not say whether distributions to SFS Corp. other than tax distributions also stop | Supportive | Capacity: board discretion. Willingness: stated in the release. Feasibility: follows a net loss quarter | Medium | Q2 release `page:3` |
| August 5, 2026: the CEO-affiliated SFS Group invested 150.0 million of the 1.65 billion preferred issue alongside Oaktree's 1.5 billion | Owner-side equity support, on the same instrument terms except that Series A-2 is subordinate to Series A-1 and has no governance protections | Supportive | Capacity: preferred stock authorised (100,000,000 shares, Q2 10-Q `page:2`). Willingness: invested. Feasibility: closed | High | Q2 10-Q `page:32` |
| Related-party arrangements: campus leases, aircraft leases, employee lease agreements, and a ten-year naming rights and sponsorship agreement of about 115 million with CEO-controlled entities, terminable by either party after two years; 32,921 of net related-party payments in FY2025 as printed (US$ thousands) | Fixed and discretionary payments to entities of the controlling individual | Neutral or Mixed | Capacity: contractual. Willingness: entered by the company; its approval process is not described in the sources. Feasibility: small against revenue | Medium | 10-K `page:161`; Q2 10-Q `page:27` |
| Exchange sales: SFS Corp. exchanged and sold shares to increase float (65,953,003 units exchanged in 2025) | Converts non-controlling interest to Class A and increases the Tax Receivable Agreement liability (Q2 10-Q `page:28`) | Neutral or Mixed | Capacity: exchange right. Willingness: sales under announced plans. Feasibility: ended May 8, 2026 | High | 10-K `page:73`; Q2 10-Q `page:71` |
| Two Harbors merger agreement signed and then terminated, with a fee received | Large equity-funded acquisition abandoned; costs incurred, fee received | Neutral or Mixed | Capacity and reason for termination: Insufficient Information | Medium | 10-K `page:140`; Q1 10-Q `page:37` |
| Priming, uptiering, drop-down, non-pro-rata exchange or collateral release | None found in the sources | Insufficient Information | The indentures and facility agreements are not supplied, so legal capacity for such actions cannot be tested | Insufficient | n/a |

The overall reading is Neutral or Mixed. Supportive documented actions (subordinated owner revolver, owner participation in the preferred issue, dividend suspension) sit beside distributions that continued while secured borrowing rose and a set of related-party payments. Governance dimensions are scored by Python, not here.

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| 1986 | Company founded | Documentary Fact | 10-K `page:8` |
| January 21, 2021 | Business combination with Gores Holdings IV, Inc. completed; Class A shares began trading January 22, 2021 | Documentary Fact | 10-K `page:8` |
| April 7, 2021 and November 22, 2021 | 2029 senior notes and 2027 senior notes issued by UWM | Documentary Fact | Q2 10-Q `page:17` |
| Third quarter 2022 | 500.0 million Revolving Credit Facility with SFS Corp. entered | Documentary Fact | Q2 10-Q `page:27` |
| 2022 and 2023 | Citibank and Goldman Sachs Bank USA servicing-rights facilities entered | Documentary Fact | Q2 10-Q `page:15` to `page:16` |
| April 2, 2024 | Weatherill class action filed against UWM, UWMC, SFS Corp. and the CEO alleging improper influence over brokers; July 20, 2026 order granted in part and denied in part the renewed motion to strike class allegations | Documentary Fact | Q2 10-Q `page:69` |
| December 10, 2024 | 2030 senior notes issued by Holdings LLC, guaranteed by UWM | Documentary Fact | Q2 10-Q `page:17` |
| 2025 | Strategic investment in BILT Technologies; the cash flow statement shows 100,000 of "investment in private company equity securities" (US$ thousands), which this answer links to the BILT investment by inference | Analyst Interpretation | 10-K `page:35`, `page:129` |
| September 8-9, 2025 | Revolver Amendment No. 1 (subordination) and issue of 1.0 billion 2031 senior notes; proceeds repaid the 800.0 million 2025 notes, which matured in November 2025 | Documentary Fact | Q2 10-Q `page:19`; 10-K `page:104`, `page:106`, `page:173` |
| October 9, 2025 | Cyberattack at a vendor, Mercadien, P.C., leading to class complaints filed June 12 and July 1, 2026 against UWM | Documentary Fact | Q2 10-Q `page:70` |
| December 17, 2025 | Merger Agreement with Two Harbors signed; 2.3328 Class A shares per Two Harbors common share; about 247 million shares to be issued | Documentary Fact | 10-K `page:140`, `page:74` |
| January 21, 2026 | Public and private warrants expired unexercised | Documentary Fact | Q2 10-Q `page:31` |
| First quarter 2026 | Two Harbors merger agreement terminated; termination fee received. The date, reason and fee amount are not stated; the 10-K (February 25, 2026) and deck (February 2026) still describe it as pending | Documentary Fact for the termination and fee; the date range is Analyst Interpretation | Q1 10-Q `page:37`, `page:42`; deck `page:7` |
| March 2026 | Ginnie Mae servicing-rights facility amended: uncommitted capacity to 900.0 million, draw period to March 20, 2028, maturity to March 20, 2029 | Documentary Fact | Q1 10-Q `page:16` |
| May 8, 2026 | SFS Corp. terminated its last Rule 10b5-1 trading arrangement | Documentary Fact | Q2 10-Q `page:71` |
| May 14, 2026 | Rocket Mortgage, LLC sued UWM in New York for breach of contract on servicing-rights sales between Nationstar and UWM; motion to dismiss filed July 31, 2026 | Documentary Fact | Q2 10-Q `page:70` |
| July 9, 2026 | Class A dividend of 0.10 per share (34.2 million) and 126.2 million member distribution paid | Documentary Fact | Q2 10-Q `page:59` |
| Subsequent event: August 5, 2026 | Preferred stock and warrant transaction closed; dividend suspended; Q2 results announced | Subsequent event | Q2 10-Q `page:32`; Q2 release `page:1`, `page:3` |
| Subsequent event: October 2 to 5, 2026 and November 12, 2026 | Rights offering record date, expected commencement and expiry as announced; whether it launched is Not supplied; expiry is after the cutoff | Subsequent event | Q2 10-Q `page:33` |

### Transaction summary and new debt issues

On August 5, 2026 UWMC closed a "strategic capital transaction" with affiliates of Oaktree Capital Management and entities affiliated with its Chairman, President and CEO, with gross proceeds of 1.65 billion (Q2 10-Q `page:32`). Oaktree invested 1.5 billion for 1.5 million shares of Series A-1 Preferred Stock plus warrants over 150 million Class A shares at 2.00 per share and over 150 million at 6.00 per share. SFS Group Capital, LLC invested 150.0 million for 150,000 shares of Series A-2 Preferred Stock plus warrants over 15 million shares at 2.00 and over 15 million at 6.00. Both series have an original issue price of 1,000 per share and accrue cumulative dividends of 10.0% per annum when paid in cash or 13.0% per annum when not paid in cash and added to stated value. Series A-2 is subordinate to Series A-1 in certain circumstances and has no governance protections. The certificate of designation includes redemption, governance and investor-protection rights for Series A-1 holders that the note does not describe, and an investor rights agreement lets Oaktree appoint two directors, one of them independent. In connection with the issue the company announced its intention to launch a 400 million rights offering to Class A holders "if needed", with the support of Oaktree and the Ishbia family, at a price equal to the greater of 2.00 and 85% of a ten-day volume-weighted average price, for up to 200 million Class A shares, with a record date of October 2, 2026 and expiry on November 12, 2026 (`page:33`). The filing states the effects are not reflected in the financial statements. The Q2 release headline calls the transaction a "$2.05 Billion Equity Investment"; the filing treats the 1.65 billion as closed and the 400 million as contingent, and the two are logged as a conflict below. Use of proceeds, issuance costs, balance sheet classification (equity or mezzanine), the redemption terms and the financing effect on the servicing-rights facilities are Insufficient Information. This is an equity-type transaction; it adds no new debt.

New debt issues in the period covered: the most recent senior note issue was the 1.0 billion 6.250% senior notes due March 15, 2031 issued on September 9, 2025 by Holdings LLC and guaranteed by UWM; its proceeds were used to repay the 800.0 million 2025 senior notes at maturity, temporarily pay down servicing-rights facilities and for working capital (Q2 10-Q `page:17` to `page:18`, `page:53`). Before that, 800.0 million of 6.625% notes due February 1, 2030 were issued by Holdings LLC on December 10, 2024. No senior notes were issued in the first half of 2026 (cash flow statement `page:5`). Debt capacity rose through facility changes: the Ginnie Mae servicing-rights facility was amended in March 2026 to 900.0 million of uncommitted capacity with later maturity, and by June 30, 2026 the two servicing-rights facilities show limits of 2.0 billion and 1.25 billion (Q1 10-Q `page:16`; Q2 10-Q `page:15` to `page:16`); the amendment that raised those limits in the second quarter is not described. Drawn balances on the servicing-rights lines were 2,950.0 million at June 30, 2026 against 1,200.0 million at December 31, 2025 (CP-1).

The terminated Two Harbors transaction: under the Merger Agreement dated December 17, 2025, Two Harbors common stockholders would receive 2.3328 UWMC Class A shares per share, and each series of Two Harbors preferred stock would convert into a like UWMC preferred series (8.125% Series A, 7.625% Series B and 7.25% Series C), with closing expected in the second quarter of 2026 (10-K `page:140`). The 10-K expected about 247 million Class A shares to be issued (`page:74`). The deck described the transaction as adding servicing UPB and being accretive and "de-levering" (management claims, deck `page:7`). The agreement was later terminated, with a fee received in the first quarter of 2026 (Q1 10-Q `page:37`), and second-quarter general and administrative expense included costs "related to the terminated merger agreement" (Q2 10-Q `page:46`). Termination date, payer, fee amount and reason are Insufficient Information.

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence and conflicts |
| --- | --- | --- | --- | --- |
| Earnings durability and margin | Q2 2026 originations flat year on year with a higher gain margin; refinance share falling from Q1 2026 (Q2 release `page:1`); wholesale-only model (10-K `page:8`) | Gain margin and broker loyalty set production income; refinance volume reverses with rates | Earnings are volume- and margin-sensitive, with hedge volatility on top; monitoring should follow gain margin and purchase share | The year-on-year volume was flat while revenue rose |
| Cash conversion and funding | Capitalized servicing rights are non-cash revenue; secured borrowings against servicing rights rose to 2,950.0 million (CP-1); facilities are uncommitted (Q2 10-Q `page:15` to `page:16`) | Production income converts to cash only when servicing is sold or collected; a lender can limit advances on uncommitted lines | Liquidity depends on lender discretion and servicing-rights values; the August 2026 raise adds a buffer | The company states a belief that cash and sources are sufficient for twelve months (Q2 10-Q `page:49`) |
| Control and sponsor alignment | SFS Corp. controls about 79% of votes, lends the revolver, receives member distributions and the Tax Receivable Agreement payments (10-K `page:73`, `page:71`) | Owner interests can differ from creditors on distributions and on change of control, where Tax Receivable Agreement payments accelerate | Neutral or Mixed; the subordinated revolver and owner-side preferred participation are the supportive facts | Dividend suspension and subordination reduce extraction risk |
| Hybrid capital | 1.65 billion Series A-1 and A-2 preferred with 10.0% cash or 13.0% non-cash dividends, warrants over 330 million shares and board rights for Oaktree (Q2 10-Q `page:32`) | Cumulative dividends and redemption rights create a fixed claim junior to debt; warrants dilute common | Positive for loss absorption if redemption cannot be forced ahead of debt; terms not supplied, so monitoring posture is to obtain the certificate of designation | Press release headline of 2.05 billion differs from the filing split |
| Servicing transition | In-house servicing expected by October 2026 (Q1 release `page:2`); one sub-servicer (10-K `page:17`) | Compliance, systems and agency-approval risks on a 247.6 billion portfolio | Execution risk to servicing income and to servicing-rights value | Management says the transition is ahead of schedule (Management Language) |
| Legal and conduct | Class actions on broker influence, telemarketing and a vendor cyber incident; a contract suit by Rocket Mortgage (Q2 10-Q `page:69` to `page:71`) | Potential damages, injunctive relief and cost; no accrual or estimate is printed | Not currently expected to be material by the company; amounts unknown | Company statement of no expected material adverse effect |

### Conflicts

| Conflict | Quotes and locators | Downstream effect |
| --- | --- | --- |
| Size of the August 2026 equity raise | Q2 release `page:1`: "Announcement of $2.05 Billion Equity Investment" and "a $2.05 billion equity capital investment by Oaktree Capital Management and SFS Group Capital, LLC"; Q2 10-Q `page:32` to `page:33`: "aggregate gross proceeds of $1.65 billion" and a "$400 million rights offering to Class A shareholders, with the support of Oaktree and the Ishbia Family, if needed" | Logged, not reconciled. The headline equals the 1.65 billion plus the 400 million (arithmetic), so the difference is one of status, not size. CP-2 should model only the 1.65 billion as closed and treat the rights offering as contingent |
| Q1 2026 purchase "Jumbo and other" originations | Q1 release `page:2`: "Jumbo and other (1) 1,443,526" for Q1 2026; Q2 release `page:3`: "Jumbo and other (1) 1,143,526" for the same period; the Q1 release components sum to its printed purchase total of 18,664,834 and the Q2 release components do not; the Q2 10-Q six-month figure of 3,285,211 less the Q2 figure of 1,841,685 (`page:40`) also gives 1,443,526 | Logged, not reconciled. Affects no credit metric used here; the Q1 release figure is the one consistent with the printed total |
| Covenant set of the Conventional servicing-rights facility | Q2 10-Q `page:16` lists "maximum debt to net worth ratio"; `page:54` lists minimum tangible net worth, minimum liquidity and net income only (carried from CP-0 and CP-1) | Logged, not reconciled; facility agreement not supplied |

### Consumer readiness

| Consumer | Readiness | What to take from CP-1A | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Control structure; Tax Receivable Agreement change-of-control acceleration; August 2026 preferred terms as summarised; terminated Two Harbors transaction; related-party flows; the in-house servicing transition | Credit synthesis must weigh controlled-company governance, junior capital and liquidity reliance on uncommitted lines | Obtain the certificate of designation, warrant and investor rights agreements, the Tax Receivable Agreement and the debt agreements |
| CP-5 | READY_WITH_LIMITATIONS | Every row above carries a category and locator; management claims are tagged and not adopted | Evidence tracing needs the distinction between filings and releases | Press-release claims (market rank, in-house servicing timing) cannot be tested against third-party data |

### Monitoring gaps

| Item | Severity | Why it matters |
| --- | --- | --- |
| Debt schedule at instrument level with guarantors (the indentures) | High | Guarantor and restricted-group scope for the 2027 and 2029 notes (UWM) and the 2030 and 2031 notes (Holdings LLC, UWM guarantor) is not stated beyond the notes |
| Maturity schedule for the warehouse lines after their stated expiries | Medium | Two lines with expiry dates before the as-of date have no renewal evidence |
| Covenant certificate or compliance calculation | High | Only compliance statements are printed |
| Add-back bridge for management adjusted measures | Low | Adjusted EBITDA reconciliation is printed; no management bridge is supplied |
| Preferred stock terms and the effect on liquidity and leverage | High | Redemption rights could create a cash claim that ranks outside the debt terms |
| Rights offering outcome | Medium | Expiry is after the cutoff |

## Calculations

All inputs are from the cited locators.

| Measure | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Warrant shares issued | 150 + 150 + 15 + 15 million | Oaktree 150 million at 2.00 and 150 million at 6.00; SFS Group 15 million at 2.00 and 15 million at 6.00 (Q2 10-Q `page:32`) | 330 million shares |
| Warrant shares against economic shares outstanding | 330 / (342.3 + 1,261.9) | Class A 342,349,795 and Class D 1,261,862,603 at August 4, 2026 | 20.6%; dilution only if exercised, which depends on the Class A price against the 2.00 and 6.00 strikes |
| Preferred dividend at stated rate on original issue price, cash | 1,650.0 million x 10.0% | Gross proceeds 1,650.0 million | 165.0 million a year; arithmetic on the issue price, not a figure the filing states |
| Same, non-cash accrual | 1,650.0 million x 13.0% | | 214.5 million a year, added to stated value; not stated by the filing |
| Rights offering at the minimum price | 200 million shares x 2.00 | Q2 10-Q `page:33` | 400 million; larger if the price is above 2.00 (85% of the ten-day volume-weighted average price exceeds 2.00) |
| SFS Corp. economic share | 1,261,862,603 / 1,604,109,738 | Q2 10-Q `page:23` | 78.7% |
| Cash paid to equity holders, H1 2026 | 59,867 + 261,896 (US$ thousands) | Q2 10-Q `page:5` | 321,763 (321.8 million), against a net loss of 281,528 (281.5 million) |
| Dividend and distribution approved in Q2 and paid July 9, 2026 | 34.2 + 126.2 million | Q2 10-Q `page:59` | 160.4 million, equal to accrued distributions and dividends payable of 160,411 (US$ thousands) |
| Total related-party net payments, FY2025 | 20,831 + 11,053 + 600 + 438 (US$ thousands) | 10-K `page:161` | 32,922 by addition; the filing prints 32,921 (rounding of 1) |
| Servicing-rights asset | Accepted in CP-1 | Fair value 5,311,465 (US$ thousands) | 5,311.5 million |
| Class A shares to be issued for Two Harbors | Stated in the 10-K | 10-K `page:74` | About 247 million; not issued after termination |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Certificate of Designation, warrant agreements and investor rights agreement for the August 5, 2026 transaction are not supplied; redemption, governance and protective rights are described only as existing | High | CP-2 | Supply the Form 8-K and exhibits |
| Two Harbors termination agreement, date, reason and fee amount are not supplied | Medium | CP-2 | Supply the termination Form 8-K |
| Indentures and facility agreements are not supplied, so legal capacity for priming, drop-down, collateral release or restricted payments cannot be tested | High | CP-2 | Supply the agreements named in the 10-K exhibit index |
| Rights offering launch and result are Not supplied; expiry is after the cutoff | Medium | CP-2 | Supply later filings |
| Voting power after exchanges since February 2026 and after the Series A-1 rights is not restated | Low | CP-2 | Supply the proxy statement or a later 10-K |
| Largest-broker concentration is not disclosed | Low | CP-2 | None available in the pinned set |
| Approval process for related-party transactions is not described in the sources | Low | CP-2 | Supply the proxy statement |
| No ratings or market quotes are supplied | Low | CP-2 | Supply if a ratings or relative-value view is later requested |

## Next module

CP-2, then CP-5. Carry forward: the controlled-company and Tax Receivable Agreement change-of-control structure; the closed 1.65 billion preferred and warrant transaction (and the contingent 400 million rights offering) with terms not supplied; the terminated Two Harbors merger; related-party flows and the suspended dividend; the in-house servicing transition as a management claim; and the three logged conflicts. Do not model the 2.05 billion headline as closed.
