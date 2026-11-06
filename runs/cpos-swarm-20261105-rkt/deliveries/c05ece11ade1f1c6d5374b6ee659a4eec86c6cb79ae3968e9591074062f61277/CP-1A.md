## Request

Module CP-1A (business and transaction context) for Rocket Companies, Inc. (issuer id rkt, NYSE: RKT), as of 2026-11-05, pathway credit_snapshot, case kind public. The context sets the cutoff at 2026-11-05, the current period at q3-2026 (quarter ended 2026-09-30), the prior period at fy-2025 (fiscal year ended 2025-12-31) and the reporting currency at USD. Amounts are US dollars in millions unless a cell says otherwise; the sources report in US dollars and in millions (Q3 10-Q page:5). The context file names no sponsor, parent, borrower, guarantors, ratings or research questions, and its blank fields are not read as zero. The reader question is which transaction, business, ownership and operating facts matter most to the creditor.

This module builds the fact pack from the filed sources and the two upstream handoffs. It gives no peer ranking, no instrument recommendation and no recovery conclusion; recovery appears only as a mechanic. It uses the CP-0 readiness handoff and the CP-1 financial base handoff. It does not correct either: the figures it repeats from CP-1 (senior notes principal 10,743, secured financing 14,187, undrawn revolver 2,500, cash 2,699, leverage 3.78x gross and 2.83x net on last-twelve-month adjusted EBITDA of 2,843) are carried unchanged, and it adds two new source differences (the date of the 2030 and 2033 note offering and the borrower under the revolving credit agreement, see Source conflicts).

Locator convention: `<source alias> page:N`, where N is the extracted chunk number of the pinned text file, not the printed page. Aliases are defined in the first table under Sources. Category tags used in tables: Documentary Fact, Management Language, Analyst Interpretation, Insufficient Information.

## Sources

### Issuer sources relied on

| Alias | Exact source name | sha256 | Document family and period |
| --- | --- | --- | --- |
| 10-K | 10-K_2025-12-31_rkt-20251231.htm.jsonl | 3f00d23a5a4d987299ba3ee372766fbda78de035096653b1d865a69d888922ae | Annual report, fiscal year ended December 31, 2025, audited, signed March 2, 2026 |
| Q1 10-Q | 10-Q_2026-03-31_rkt-20260331.htm.jsonl | 0a828436cfdb4cb6430873bcdf676f4a2758eb6f8aaf83bcd5c4c1bd9959be37 | Quarterly report, quarter ended March 31, 2026, unaudited |
| Q2 10-Q | 10-Q_2026-06-30_rkt-20260630.htm.jsonl | 4ca13e8689778101de80b67ba6d799666890bfd97332aef7adca82c2e094e90b | Quarterly report, quarter ended June 30, 2026, unaudited |
| Q3 10-Q | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | 59c56634da7bee8e5debdbfce480876851737d0b5ddf01b6f700d4f40ecd6bce | Quarterly report, quarter ended September 30, 2026, unaudited, signed October 30, 2026 |
| Q1 release | EX-99.1_2026-05-07_rkt-earningsrelease3312026.htm.jsonl | 7d218dea46aff3c8af9298dca5b852af49f0e5f073ef0f93c5f3b622d0854392 | Earnings release exhibit, first quarter 2026, dated May 7, 2026; furnished management document |
| Q2 release | EX-99.1_2026-08-06_rkt-063020268xkex991earnin.htm.jsonl | 6542f2db604c3ffa41383bd56c69d56492031f4ee91e3c42b828c315d7979477 | Earnings release exhibit, second quarter 2026, dated August 6, 2026; furnished management document |
| Q3 release | EX-99.1_2026-10-29_rkt-093020268xkex991earnin.htm.jsonl | 51281ba557de6ffcbe69b458cb58d0ccec82e27e457e960477651f50df28d346 | Earnings release exhibit, third quarter 2026, dated October 29, 2026; furnished management document |

The first line of each pinned text file quotes a different sha256: that is the hash of the original HTML document, not of the pinned text file. The hashes above are the pinned text-file hashes supplied by CP-OS.

### Run context

| Source | sha256 | Role |
| --- | --- | --- |
| context | 2c3b1fbba94f4a511900e452ab48c8c288b5d2472b9c175cb66b98c0de72d2ac | The user's dated settings for this run. Not issuer evidence. |

### Handoffs supplied

| Module | sha256 | Use in this module |
| --- | --- | --- |
| CP-0 | b5fd40886eeedd24c855cc4c21dd662543a58c822d0fb2b19a168fce8c895924 | Source readiness: effective source set, perimeter and presentation changes, and source gaps. All carried into this module. |
| CP-1 | 54e4775b2f314e2c41568ee11caf51c8cfb55f59fdffa205fe2c46e2c7684901 | Financial base view: the two debt layers, leverage, liquidity, maturities and claims outside funded debt. Figures repeated here match it. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Rocket is a founder-controlled US mortgage originator and servicer that added Redfin and Mr. Cooper through all-stock acquisitions in 2025 and refinanced part of its debt in 2026; control, rate sensitivity and Agency dependence drive the credit view. | Medium | Governance letter, indentures, restricted payment terms and named guarantors are not supplied, so creditor protections against owner actions cannot be assessed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Redfin and Mr. Cooper were bought mainly for stock, with cash settling target debt; the servicing portfolio is now 2,007,176 of unpaid principal. | Equity funding limited new debt, but servicing scale makes earnings depend on Agency relationships and mortgage rates. | High |
| Mr. Gilbert holds more than a majority of the voting power, and Rocket relies on controlled company exemptions from independent board requirements. | Creditors rely on contract protections rather than board independence; those contracts are not in the pack. | High |
| Documented capital actions are a 2025 special dividend of $120.1 million, termination of undrawn related party credit lines, and no dividends or buybacks in the 2026 cash flow statements. | Behaviour is mixed on the evidence available; legal capacity for distributions is unknown. | Low |
| The pack gives two dates for the 2030 and 2033 note offering, June 2025 and October 2025. | The date does not change the principal outstanding but weakens confidence in the note-by-note history. | Medium |
| Rocket Close faces a 175 verdict in the HouseCanary dispute with judgment not entered, and legal reserves rose to 216. | Litigation outcomes can reach liquidity and, above thresholds, can trigger facility defaults. | Medium |

### Business and transaction view

Rocket Companies, Inc. is a Detroit-based, Delaware-incorporated holding company that originates and services US residential mortgages and, since 2025, also runs a real estate brokerage and search platform (Redfin) and personal finance businesses (Rocket Money and Rocket Loans) (Q3 10-Q page:8; 10-K page:5 to page:7). Revenue comes from four lines: gain on sale of loans, loan servicing income, interest income and other income. For the nine months of 2026 these were 3,609, 2,236, 1,640 and 1,524, summing to total revenue, net of 9,009 (Q3 10-Q page:5). The structural change in the last eighteen months is scale and mix. The June 30, 2025 Up-C Collapse removed the paired-interest structure and left only Class A and Class L common stock (10-K page:140). Redfin (July 1, 2025) and Mr. Cooper (October 1, 2025) were both bought for stock, with 1,742 and 16,973 of consideration respectively, of which cash of 252 and 3,113 repaid target debt (Q3 10-Q page:16 to page:17). The servicing portfolio is now 2,007,176 of unpaid principal, of which 1,201,476 is owned MSRs and 805,700 is subservicing and other (Q3 10-Q page:62).

The mechanics that matter for a creditor are these. First, revenue durability rests on servicing fee income, which was 3,181 in the nine months of 2026 and comes from a portfolio of agency and government loans serviced under contracts that the Agencies and subservicing clients can terminate on little or no notice (Q3 10-Q page:5; 10-K page:29). Second, margin resilience depends on interest rates through both channels: higher rates cut origination (the 30-year rate rose to 7.28% by the end of September 2026 and the market was smaller than in the second quarter, Q3 10-Q page:49) but raise MSR fair value, which flatters GAAP income and is removed from adjusted measures (Q3 release page:6). Third, liquidity and refinancing run through two layers: unsecured senior notes of 10,743 and an undrawn 2,500 revolver, and secured financing of 14,187, most of which sits on uncommitted lines (CP-1). Fourth, control sits with Mr. Gilbert, whose majority voting power lets the company use controlled company exemptions from independent director requirements (10-K page:86). The company renounced certain corporate opportunities in favour of RHI II parties (10-K page:83). The governance letter agreement of March 31, 2025 with Mr. Gilbert is listed as an exhibit but its terms are not in the pack (10-K page:222).

The credit-relevant history is acquisitive and equity-funded, followed by refinancing: stock paid for both targets, 4.0 billion of senior notes were raised in 2025, Mr. Cooper's legacy notes were tendered or assumed, and in 2026 1.5 billion of new notes were issued, 1,212 of notes were redeemed and a larger, longer revolver was put in place (see the transaction section). The view is Medium confidence: the documentary base for operations and transactions is strong, while the documents that would show what owners may do with cash and collateral (indentures, credit agreements, the governance letter and the proxy statement) are absent.

### Company and operating model

| Area | Fact | Category | Source and locator | Credit translation |
| --- | --- | --- | --- | --- |
| Core activities | Holding company whose subsidiaries originate, sell and service mortgages, provide title, closing and appraisal services, operate Redfin real estate services, Rocket Money subscriptions and Rocket Loans personal loans | Documentary Fact | Q3 10-Q page:8; 10-K page:5 to page:7 | Several earnings streams share one funding and brand base; mortgage drives the credit |
| Origination channels | Direct to Consumer, plus Partner Network made of Wholesale (Rocket Pro), Premier Enterprise Partner and Correspondent; one reportable segment, Mortgage, from Q2 2026 | Documentary Fact | 10-K page:6; Q3 10-Q page:42 | Channel mix changes gain on sale margin; the Correspondent channel carries a low margin of 0.15% (Q3 10-Q page:57) |
| Market and geography | US residential mortgage and real estate; team members in the United States, Canada and India; demand driven by rates, property values and seasonality | Documentary Fact | 10-K page:11 | Earnings are cyclical and rate-driven; there is no geographic diversification of the revenue base |
| Customers | Consumers, broker partners, financial-institution partners and loan sellers; no single-customer concentration is disclosed (searched the 10-K for concentration and major customer wording) | Insufficient Information | 10-K page:6, page:86 | Counterparty concentration shows instead through Agency servicing contracts (below); consumer dispersion is high but unquantified |
| Revenue model, nine months 2026 | Gain on sale of loans, net 3,609; loan servicing income, net 2,236 (servicing fee income 3,181 less change in fair value of MSRs 945); interest income 1,640; other income 1,524; total 9,009 | Documentary Fact | Q3 10-Q page:5 | Servicing fees are recurring; gain on sale and MSR fair value move with rates and volume |
| Servicing scale | Total UPB 2,007,176: MSRs 1,201,476 and subservicing and other 805,700 at September 30, 2026; 60-plus day delinquency 1.52% against 1.50% at December 31, 2025 | Documentary Fact | Q3 10-Q page:25, page:62 | Large agency-heavy portfolio with stable delinquency; subservicing is held on contracts terminable with little notice |
| Servicing counterparties | Most loans are serviced for Fannie Mae, Freddie Mac and Ginnie Mae, which may terminate servicing and cause MSR sales; subservicing clients may terminate with or without cause | Documentary Fact | 10-K page:29 | Termination or fines would cut servicing income and MSR value, the largest balance sheet asset |
| MSR monetisation | Nine months 2026: MSRs with UPB of 115,187 sold, of which 79,156 retained as subservicer; net proceeds from MSR sales 1,750; management cites Q3 sales of 23 billion UPB for 379 of cash | Documentary Fact | Q3 10-Q page:7, page:24; Q3 release page:2 | MSR sales are a liquidity lever but reduce owned servicing income and keep subservicing exposure |
| Pricing and volume | Gain on sale margin 2.54% in Q3 2026 against 2.80% in Q3 2025; closed origination volume 43.6 billion against 32.4 billion | Documentary Fact | Q3 10-Q page:49, page:57 | Volume growth includes the acquired correspondent business; margin per loan is lower |
| Rate sensitivity | 30-year mortgage rate rose from 6.43% in early July to 7.28% at the end of September 2026; smaller market than Q2; MSR fair value sensitivities and hedges are disclosed | Documentary Fact | Q3 10-Q page:25 to page:26, page:34, page:49 | Rising rates hurt origination volume and help MSR valuation; hedge effectiveness is not shown |
| Cost structure | Nine months 2026: salaries, commissions and benefits 3,064; general and administrative 1,662; marketing 889; interest expense 1,082; depreciation and amortization 438; other 235; total 7,370 | Documentary Fact | Q3 10-Q page:5 | Compensation is largely variable with volume; interest expense is large because secured financing is carried |
| Capital spending | Purchase of property and equipment, net 120 in nine months 2026 against 51; net MSR purchases 475 against 244 | Documentary Fact | Q3 10-Q page:7 | Capital light; MSR purchases are the main investment outlay |
| Working capital and funding | Loans held for sale of 13,218 are funded on repurchase lines at advance rates of roughly 97% to 98% and usually stay on the lines for less than 45 days; advance receivables of 1,674 | Documentary Fact | Q3 10-Q page:4; 10-K page:120 | Self-funded margin on each loan and margin calls on collateral values create intra-quarter cash needs |
| Competition | Large financial institutions, independent mortgage banks and fintech companies compete on distribution, speed, service, pricing and access to capital | Documentary Fact | 10-K page:8 | Pricing competition limits margins; access to capital is itself a competitive factor |
| Market position claims | Rocket Mortgage described as the nation's largest originator by loan units and largest servicer, and as number one by volume per Inside Mortgage Finance rankings (an external publisher cited by management) | Management Language | 10-K page:5; Q3 release page:3 | Scale claims are management characterisations; they are not independently verified in the pack |
| Retention and AI claims | Net client retention of the servicing portfolio of 97% annually; AI voice platform handled 65% of inbound servicing calls | Management Language | 10-K page:5; Q3 release page:2 | Supports recapture narrative; no audited support in the pack |

### Company profile

| Item | Value | Category | Source and locator |
| --- | --- | --- | --- |
| Legal name and ticker | Rocket Companies, Inc.; Class A common stock RKT on the New York Stock Exchange | Documentary Fact | Q3 10-Q page:1 |
| Incorporation and headquarters | Incorporated in Delaware on February 26, 2020; principal offices at 1050 Woodward Avenue, Detroit, Michigan | Documentary Fact | Q3 10-Q page:1, page:8 |
| Country and sector | United States; Mortgage Bankers and Loan Correspondents (sector label from the run context, not issuer evidence) | Documentary Fact | context file; Q3 10-Q page:1 |
| Business description | Homeownership platform company with mortgage, real estate and personal finance businesses | Documentary Fact | Q3 10-Q page:8 |
| Filer status | Large accelerated filer, not a shell company; fiscal year ends December 31 | Documentary Fact | Q3 10-Q page:1 |
| Share classes outstanding | At October 23, 2026: Class A 1,913,456,820 shares and Class L 924,439,745 shares, each carrying one vote | Documentary Fact | Q3 10-Q page:1; 10-K page:140 |
| Controlling holder | Mr. Gilbert holds more than a majority of the combined voting power; the company is a controlled company under NYSE rules; exact percentage not disclosed in the pack | Documentary Fact | 10-K page:86 |
| Senior people | Chief Executive Officer Varun Krishna; founder and Chairman Dan Gilbert; Brian Brown President, Chief Financial Officer and Treasurer from February 26, 2026 | Documentary Fact | Q3 release page:1; 10-K page:5, page:218 |
| Board | Ten members after an independent director was appointed in August 2026 | Management Language | Q3 release page:3 |
| Principal subsidiaries | Rocket Mortgage, LLC, Rocket Close, Rocket Money, Rocket Loans, RTIC, Xome, Lendesk Technologies, Woodward Capital Management LLC, Redfin and others, held through Rocket Limited Partnership | Documentary Fact | Q3 10-Q page:8 |
| Non-controlling interest | 24.9% of Roosevelt held by a third party after a sale in Q2 2026; Roosevelt is consolidated | Documentary Fact | Q3 10-Q page:16 |
| Employees | About 23,500 team members at December 31, 2025, in the United States, Canada and India | Documentary Fact | 10-K page:11 |
| Auditor | Ernst & Young LLP, auditor since 1999, with an unqualified opinion on the 2025 statements and on internal control | Documentary Fact | 10-K page:131, page:135, page:215 to page:216 |
| Regulatory standing | Approved seller and servicer for Fannie Mae, Freddie Mac and Ginnie Mae; in compliance with net worth, liquidity and capital ratio requirements at September 30, 2026 | Documentary Fact | 10-K page:29 to page:30; Q3 10-Q page:42 |
| Tax structure | C corporation; Rocket Limited Partnership is a partnership for tax; tax receivable agreement with RHI II, LLC and Mr. Gilbert | Documentary Fact | Q3 10-Q page:32 to page:33 |
| Credit ratings | Not disclosed in the pack; context ratings list is empty | Insufficient Information | context file; CP-0 gap |
| Borrower, parent, guarantors | Context names none; guarantors of the senior notes are described as "our subsidiary guarantors" and not named | Insufficient Information | Q3 10-Q page:31 |
| Sponsor | Context names none; control rests with Mr. Gilbert, and RHI II, LLC is a party to the tax receivable agreement | Documentary Fact | 10-K page:86, page:156 |

### Transaction summary and new debt issues

All transactions below are completed unless stated. Figures are in US dollars in millions.

The Up-C Collapse closed on June 30, 2025. The previously outstanding Class D common shares and Holdings LLC Units were exchanged and retired for new Class L common stock, Class B and Class C stock were eliminated, and the company now holds indirectly all voting and economic interests in Rocket Limited Partnership (10-K page:140). It was accounted for as a common control transaction. The Tax Receivable Agreement was amended so that its terms do not apply to exchanges on or after March 9, 2025, including those made in the collapse (10-K page:156). Class L shares are subject to lock-up periods, with transfers barred until the first anniversary of closing and half of the shares until the second anniversary, and all Class L shares convert automatically on the later of June 30, 2027 and the date Class L falls below the stated voting share (10-K page:90). In the third quarter of 2026, 924,439,710 Class L shares were converted into Class A shares on a one-for-one basis (Q3 10-Q page:46). The filings do not say who converted them or whether any were sold; the timing follows the first anniversary of the collapse (Analyst Interpretation).

The Redfin acquisition was an all-stock transaction effective July 1, 2025 with consideration of 1,742: 1,466 of Class A stock, 24 of converted equity awards and 252 of cash that settled Redfin's term loan, accrued interest and prepayment premium. Redfin carried unsecured financing of 526 at acquisition (Q3 10-Q page:16 to page:17). The purchase price allocation was finalised in Q2 2026 with no measurement-period adjustments. The Mr. Cooper acquisition was an all-stock transaction effective October 1, 2025 with consideration of 16,973: 13,667 of Class A stock, 193 of converted awards and 3,113 of cash that settled Mr. Cooper's unsecured senior notes, accrued interest and fees (Q3 10-Q page:17). Liabilities assumed included secured financing of 6,461 and unsecured financing of 1,956. In Q3 2026 the allocation was finalised with a 75 increase to goodwill, arising from a 100 increase in litigation and regulatory accruals offset by a 25 decrease in net deferred tax liabilities, with no earnings impact (Q3 10-Q page:18). Goodwill from the two deals is 8,326 and 1,233 and is not tax deductible (Q3 10-Q page:16 to page:18). The 10-K states that revenue and net income since the acquisition dates cannot be separated (10-K page:165).

New debt in 2025: the note table lists 2,000 of 6.125% senior notes due 2030 and 2,000 of 6.375% senior notes due 2033 (10-K page:180), and the 2025 cash flow statement shows borrowings on senior notes of 4,000 (10-K page:138). An indenture dated June 20, 2025 with guarantors named therein is listed as an exhibit (10-K page:222), and the Q3 10-Q says the 4.0 billion offering completed in June 2025 (Q3 10-Q page:67). The note table footnotes instead say the offerings were completed in October 2025 (10-K page:181). This is logged as a conflict and not reconciled. Proceeds from the June 2025 issuance were used to fund the tender, redemption and consent solicitations for Nationstar notes (10-K page:165). In exchange offers, 738 of the 750 of 6.500% notes due 2029 and 955 of the 1,000 of 7.125% notes due 2032 were tendered and replaced by Rocket Companies notes, and tender offers bought 574 of 650 of 5.125% notes due 2030 and 536 of 600 of 5.750% notes due 2031. Rocket Mortgage, LLC assumed the notes not tendered. The company also redeemed 500 of 5.000% notes due 2026, 600 of 6.000% notes due 2027 and 850 of 5.500% notes due 2028 (10-K page:165 to page:166). A 364-day senior unsecured Bridge Facility is defined and its financing fees were expensed within acquisition-related expenses (Q3 10-Q page:2, page:55). The facility amount and any drawing are not printed in the pack, and it does not appear in the debt tables at either year-end or September 30, 2026.

Other 2025 capital events: the company declared a special dividend of $0.80 per Class A share on March 10, 2025 in connection with the Up-C Collapse, paid $120.1 million on April 3, 2025 (10-K page:95). It terminated two lines of credit from RHI with capacities of 2,000 and 100 in 2025, neither drawn, and terminated a surplus debenture between RHI and RTIC (10-K page:181). A Revolving Credit Agreement dated April 30, 2025 with Rocket Mortgage, LLC as borrower and JPMorgan Chase Bank, N.A. as agent is listed in the 10-K exhibits (10-K page:222).

New debt in 2026: on June 9, 2026 the company issued 1,500 of senior notes, of which 900 are 6.125% notes due 2031 and 600 are 6.500% notes due 2034; management said the offering was more than seven times oversubscribed and upsized from 1,200, and that proceeds redeemed outstanding senior notes and repaid other debt (Q2 release page:3, Management Language). The Q3 10-Q table shows the 2.875% notes due 2026 (1,150) redeemed at 100% plus about 6 of accrued interest, and the 5.250% notes due 2028 (62) redeemed at 100% plus about 2 of accrued interest (Q3 10-Q page:30 to page:31). The revolving credit facility was increased from 2,300 to 2,500, fully committed, and extended to July 16, 2029 (Q2 10-Q page:28; Q3 10-Q page:30). The Q2 and Q3 10-Q exhibit lists name a Revolving Credit Agreement dated July 16, 2026 with Rocket Companies, Inc. as Borrower, guarantors and JPMorgan Chase Bank, N.A. as agent (Q3 10-Q page:71), whereas the 2025 agreement had Rocket Mortgage, LLC as borrower. The filings do not say whether the 2026 agreement amends and restates the 2025 one; the change of borrower is an open distinction that matters for ranking. Nationstar Mortgage was merged into Rocket Mortgage in the first quarter of 2026 (Q1 10-Q page:35). A personal loan funding facility was increased to 300 after September 30, 2026, and three repurchase facilities were extended and one matured after quarter end (Q3 10-Q page:29, Subsequent events). No debt transaction dated after the Q3 10-Q signature of October 30, 2026 is in the pack.

Liquidity effect and status: the 2025 and 2026 issuances replaced assumed and maturing notes, lengthened the revolver and left no senior note maturing before 2027 (CP-1). Total unsecured principal rose from 10,455 at December 31, 2025 to 10,743 at September 30, 2026 (Q3 10-Q page:30). The 2025 special dividend and RHI line terminations show owner-related cash and backstop moves before the acquisitions; no distribution to owners appears in the 2026 cash flow statements beyond distributions to other unit holders of 8 and taxes withheld on equity awards (Q3 10-Q page:7).

### Ownership, control and capital structure of equity

| Item | Fact | Category | Source and locator | Creditor mechanic |
| --- | --- | --- | --- | --- |
| Control | Mr. Gilbert holds more than a majority of combined voting power; so long as he owns a significant amount of equity he can substantially influence stockholder votes on transactions | Documentary Fact | 10-K page:86 | Controlling holder can approve or block corporate transactions; creditor protection depends on contracts |
| Control thresholds | The Gilberts can control all matters requiring stockholder approval until they cease to beneficially own at least 50% of voting power | Documentary Fact | 10-K page:83 | Control is stated as a threshold, not a percentage; actual ownership is Not disclosed in the pack |
| Governance exemptions | As a controlled company the company may omit majority-independent board and independent committee requirements | Documentary Fact | 10-K page:86 | Fewer structural checks on related party and capital allocation decisions |
| Corporate opportunities | Certificate of incorporation renounces opportunities in favour of RHI II parties | Documentary Fact | 10-K page:83 | Opportunities could be directed outside the credit group |
| Classes and voting | Class A and Class L carry one vote per share and identical dividend and residual rights; Class L converts one for one | Documentary Fact | 10-K page:140; Q3 10-Q page:46 | Voting control is spread over two classes; conversion changes the public float, not the debt |
| Lock-up and conversion | Class L lock-up barred transfers before the first anniversary and half of the shares before the second anniversary of the collapse; automatic conversion later of June 30, 2027 and the stated voting threshold | Documentary Fact | 10-K page:90 | Equity overhang is a market risk to equity, not directly to creditors |
| Dividend policy | The company expects to retain earnings; its credit facilities restrict declaring and paying cash dividends | Documentary Fact | 10-K page:95 | Legal capacity for distributions is limited by agreements that are not supplied |
| Tax receivable agreement | Pays 90% of realised cash tax savings to RHI II, LLC and Mr. Gilbert; liability 590 at December 31, 2025 | Documentary Fact | Q3 10-Q page:33; 10-K page:191 | A related party claim that ranks as an operating liability; current amount Not supplied |
| Related party leases | Lease agreements for offices including the Detroit headquarters with Bedrock affiliates; lease expense 56 in nine months 2026; other related party spend in general and administrative 43 and marketing 11 | Documentary Fact | Q3 10-Q page:31 | Ongoing payments to owner-affiliated entities; amounts are small against operating expenses of 7,370 |
| Percentages and prior recapitalisation | Gilbert beneficial ownership percentage, board independence detail and any dividend recapitalisation before 2025 are not disclosed in the pack | Insufficient Information | 10-K page:219 | Proxy statement missing; do not infer percentages |

### Governance and sponsor behaviour

| Behaviour | Documented action | Category | Dimension informed | Legal capacity, willingness, feasibility | Evidence quality | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Distribution | 2025 special dividend of $0.80 per Class A share, $120.1 million, paid April 3, 2025, in connection with the Up-C Collapse | Documentary Fact | Cash distributions | Capacity: facility restrictions exist but are not supplied. Willingness: one-off distribution before the acquisitions. Feasibility: liquidity at the time is not in this pack | High | 10-K page:95 |
| Distributions in 2026 | The 2026 cash flow statements show distributions to other unit holders of 8 and no dividends or share repurchases | Documentary Fact | Cash distributions | Willingness: none documented in 2026 to date; capacity unknown | High | Q3 10-Q page:7 |
| Backstop lines | Voluntary termination in 2025 of undrawn RHI lines of credit of 2,000 and 100 | Documentary Fact | Sponsor support | Willingness: owner liquidity backstop withdrawn, unused; feasibility of owner support is not assessed | High | 10-K page:181 |
| Structural simplification | Up-C Collapse; Tax Receivable Agreement amended to exclude collapse exchanges | Documentary Fact | Structure and related party claims | Reduces paired-interest complexity and limits new TRA payments from the exchange | High | 10-K page:140, page:156 |
| Acquisition funding | Both acquisitions paid in stock; cash used to settle target debt | Documentary Fact | Capital allocation | Equity funded the equity purchase price; leverage rose through assumed and refinanced debt, not through cash purchase | High | Q3 10-Q page:16 to page:17 |
| Debt refinancing | 2026 note issuance and redemptions, revolver upsized and extended | Documentary Fact | Liquidity and refinancing | Maturity extension with higher coupons; see the conflict on the 2025 note date | High | Q2 release page:3; Q3 10-Q page:30 |
| Related party dealings | Bedrock lease arrangements; RHI II tax receivable payments | Documentary Fact | Related party leakage | Recurring payments to owner-affiliated entities; amounts disclosed are small relative to expenses | Medium | Q3 10-Q page:31, page:33 |
| Creditor-adverse actions | No priming, uptier, drop-down or non-pro-rata exchange is documented in the pack; indentures and credit agreements are not supplied | Insufficient Information | Creditor protection | Legal capacity cannot be assessed without documents | Insufficient | CP-0 gap |
| Overall category | Neutral or Mixed on the documents available: one-off distribution and withdrawal of undrawn owner lines, offset by equity-funded acquisitions and no 2026 distributions. Not an extraction-oriented or creditor-adverse finding on this evidence | Analyst Interpretation | Behaviour overall | Willingness is read from actions only; sponsor identity is not used | Medium | Rows above |

### Timeline

| Date | Event | Category | Source and locator |
| --- | --- | --- | --- |
| February 26, 2020 | Rocket Companies, Inc. incorporated in Delaware; initial public offering in August 2020 | Documentary Fact | Q3 10-Q page:8; 10-K page:218 |
| March 10, 2025 | Special dividend declared; paid April 3, 2025 | Documentary Fact | 10-K page:95 |
| March 31, 2025 | Governance letter agreement between the company and Mr. Gilbert (terms not supplied) | Documentary Fact | 10-K page:222 |
| April 30, 2025 | Revolving credit agreement with Rocket Mortgage, LLC as borrower | Documentary Fact | 10-K page:222 |
| June 2025 | Senior note offering; indenture dated June 20, 2025; undrawn RHI credit lines terminated | Documentary Fact | 10-K page:179, page:222; Q3 10-Q page:67 |
| June 30, 2025 | Up-C Collapse | Documentary Fact | 10-K page:140 |
| July 1, 2025 | Redfin acquired | Documentary Fact | Q3 10-Q page:16 |
| October 1, 2025 | Mr. Cooper acquired; Nationstar note exchange and tender offers settled | Documentary Fact | 10-K page:165 |
| February 24, 2026 | Brian Brown appointed President, effective February 26, 2026 | Documentary Fact | 10-K page:218 |
| Q1 2026 | Nationstar Mortgage merged into Rocket Mortgage | Documentary Fact | Q1 10-Q page:35 |
| March 6, 2026 | HouseCanary retrial verdict of 175 against Rocket Close; judgment not entered | Documentary Fact | Q3 10-Q page:38 |
| Q2 2026 | Segment structure changed to one segment; Roosevelt non-controlling interest sold | Documentary Fact | Q3 10-Q page:16, page:42 |
| June 9, 2026 | 1,500 senior notes issued | Management Language | Q2 release page:3 |
| July 16, 2026 | Revolving credit agreement dated this day, borrower Rocket Companies, Inc.; facility 2,500 maturing in 2029 | Documentary Fact | Q3 10-Q page:30, page:71 |
| August 2026 | Independent director appointed, board of ten | Management Language | Q3 release page:3 |
| Q3 2026 | 924,439,710 Class L shares converted to Class A | Documentary Fact | Q3 10-Q page:46 |
| September 22, 2026 | HouseCanary filed Chapter 11 | Documentary Fact | Q3 10-Q page:38 |
| October 29 and 30, 2026 | Q3 results released; Q3 10-Q signed; post-quarter facility extensions (subsequent events) | Documentary Fact | Q3 release page:1; Q3 10-Q page:29, page:71 |

### Source conflicts

| Item | Source A (verbatim) | Source B (verbatim) | Effect |
| --- | --- | --- | --- |
| Date of the 2030 and 2033 senior note offerings | 10-K page:181: "In October 2025, the Company completed the offering of $2,000 of unsecured senior notes due 2030." | Q3 10-Q page:67: "the Company's $4.0 billion senior notes offering completed in June 2025"; 10-K page:222: "Indenture, dated as of June 20, 2025" | Logged as unreconciled. Principal outstanding is unaffected, but the mapping of the June 2025 offering to the 2030 and 2033 notes is not confirmed. |
| Borrower under the revolving credit facility | 10-K page:222: "Revolving Credit Agreement, dated as of April 30, 2025, by and among Rocket Mortgage, LLC, as Borrower" | Q3 10-Q page:71: "Revolving Credit Agreement, dated as of July 16, 2026, by and among Rocket Companies, Inc., as Borrower" | Whether the 2026 agreement replaces or amends the 2025 one is not stated; the borrower entity (operating subsidiary or holding company) matters for structural ranking. |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence or conflict |
| --- | --- | --- | --- | --- |
| Revenue durability | Servicing fee income of 3,181 in nine months 2026 and a servicing portfolio of 2,007,176 (Q3 10-Q page:5, page:62); management claims 97% annual client retention (10-K page:5) | Recurring fees on a large portfolio support revenue visibility, but contracts are terminable and subservicing is held for others | Supports debt service capacity; termination or fines by an Agency would cut income and MSR value | Agency termination rights (10-K page:29); retention is Management Language |
| Margin and cash-flow risk | Gain on sale margin fell to 2.54% from 2.80%; mortgage rates rose to 7.28% and the market was smaller (Q3 10-Q page:49, page:57); fourth-quarter adjusted revenue guided to 2.1 billion to 2.3 billion (Q3 release page:3) | Lower volumes and margins reduce origination income; MSR value gains offset in GAAP but not in adjusted measures | Last-twelve-month leverage of 3.78x is not a forward run-rate; headroom depends on rates | CP-1 notes the leverage anchor; no forecast is supplied |
| Funding and refinancing | Secured financing of 14,187 against committed secured lines of 7,400; unsecured notes with no maturity before 2027 (CP-1) | Warehouse and MSR lines need renewal and carry margin calls and cross-default terms | Recurring rollover exposure; failure to renew would hit origination liquidity | Revolver extended to 2029; stated liquidity of 11.4 billion is not fully tied to the filings (CP-1) |
| Concentration | Agencies are the main servicing counterparties; loans are sold to the Agencies and private investors (10-K page:29, page:32) | Dependence on Agency programmes and guidelines for sale outlets and servicing | A change in Agency role, fees or eligibility would affect both origination sale and servicing | No customer concentration disclosed; consumer dispersion is high but unquantified |
| Sponsor alignment and control | Mr. Gilbert controls the vote; controlled company exemptions; renounced corporate opportunities; governance letter terms not supplied (10-K page:83, page:86, page:222) | Few board-level checks on related party and capital allocation; protections sit in unsupplied documents | Creditor protection depends on indenture and credit agreement terms that this pack cannot show | Documented behaviour is mixed, not extraction-oriented; 2026 shows no distributions |
| Litigation and contingent claims | Legal reserves of 216 against 74; HouseCanary verdict of 175 with judgment not entered and plaintiff in Chapter 11; Mr. Cooper data breach class action (Q3 10-Q page:38, page:40, page:41) | Large unpaid judgments above facility thresholds could default funding facilities | Event risk to liquidity and covenants; reserve allocation unknown | Management states no material adverse effect is expected beyond reserves (Q3 10-Q page:37) |
| Key uncertainties | Covenant levels, guarantors, ratings, restricted payment terms, entity-level net worth and the basis of secured availability are not supplied | Headroom and ranking cannot be sized | Monitoring posture should be cautious until documents are obtained | CP-0 and CP-1 gaps carry forward |

### Consumer readiness

| Consumer | Status | What it should take from this module | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | The category-tagged rows above, the credit translations, the governance behaviour category and the two logged conflicts | Business risk and control drive the fundamental view alongside CP-1 financial risk | No documents on restricted payments, guarantors or covenants; label governance as Neutral or Mixed on documented actions and avoid recovery conclusions |
| CP-5 | READY_WITH_LIMITATIONS | Locators for each row and the verbatim conflict quotes | The trace review checks each claim against its cited page | Management Language rows must stay attributed; the two conflicts must not be reconciled |

### Monitoring items the source set lacks

| Item | Status | Severity |
| --- | --- | --- |
| Debt schedule | Available from the Q3 10-Q tables (page:27 to page:31) | Low |
| Maturity schedule | Notes by maturity date available; year table only at December 31, 2025 (10-K page:181) | Low |
| Covenant certificate or levels | Not supplied | High |
| Add-back bridge | Adjusted EBITDA reconciliation available in releases and filings (Q3 release page:8) | Low |
| Indentures, credit agreements, governance letter, proxy statement | Not supplied | High |

## Calculations

No new financial metric is created in this module. These are footing and tie checks of printed figures used in the tables. Amounts are USD millions unless stated.

| Check | Inputs (locator) | Result | Printed total |
| --- | --- | --- | --- |
| Revenue lines, nine months 2026 | 3,609 + 2,236 + 1,640 + 1,524 (Q3 10-Q page:5) | 9,009 | Total revenue, net 9,009 |
| Loan servicing income, nine months 2026 | 3,181 less 945 (Q3 10-Q page:5) | 2,236 | Loan servicing income, net 2,236 |
| Expense lines, nine months 2026 | 3,064 + 1,662 + 889 + 1,082 + 438 + 235 (Q3 10-Q page:5) | 7,370 | Total expenses 7,370 |
| Servicing portfolio UPB | 1,201,476 + 805,700 (Q3 10-Q page:62) | 2,007,176 | Balance at end of period 2,007,176 |
| Redfin consideration | 1,466 + 24 + 252 (Q3 10-Q page:16) | 1,742 | 1,742 |
| Mr. Cooper consideration | 13,667 + 193 + 3,113 (Q3 10-Q page:17) | 16,973 | 16,973 |
| Stock and award consideration in 2025 cash flow | 1,466 + 13,667 and 24 + 193 (Q3 10-Q page:16 to page:17) | 15,133 and 217 | Issuance of common stock as consideration 15,133; share-based compensation as consideration 217 (10-K page:138) |
| Goodwill from the two deals | 8,326 and 1,233 (Q3 10-Q page:16 to page:18); Mortgage and other segment goodwill 10,057 and 629 (Q3 10-Q page:32) | Not summed: segment goodwill includes earlier goodwill | 10,686 on the balance sheet (Q3 10-Q page:4) |
| Measurement-period adjustment | 100 increase in accruals less 25 decrease in deferred tax liabilities (Q3 10-Q page:18) | 75 | 75 increase to goodwill |
| Legacy notes tendered | 738 of 750; 955 of 1,000; 574 of 650; 536 of 600 (10-K page:165) | Not tendered 12, 45, 76 and 64 | Lines of 12, 45, 76 and 64 in the Q3 10-Q note table (page:30) |
| Notes redeemed in 2026 | 1,150 and 62 (Q3 10-Q page:30 to page:31) | 1,212 | Repayments of Senior Notes 1,212 (Q3 10-Q page:7) |
| Class L conversion | 1,848,879,455 less 924,439,710 (Q3 10-Q page:4, page:46) | 924,439,745 | 924,439,745 |
| Senior notes principal and secured financing | Repeated from CP-1 (Q3 10-Q page:29 to page:30) | 10,743 and 14,187 | 10,743 and 14,187 |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Governance letter agreement of March 31, 2025, indentures, credit agreements and the proxy statement are Not supplied; restricted payment, lien, guarantee and change-of-control terms cannot be assessed (10-K page:222, page:219). | High | CP-2, CP-5 | Obtain the documents; until then do not state legal capacity for distributions or ranking. |
| Mr. Gilbert's voting percentage and economic interest are Not disclosed in the pack; only a more than majority control statement and a 50% threshold appear (10-K page:83, page:86). | Medium | CP-2 | Obtain the 2026 proxy statement. |
| Named guarantors and the issuer of each senior note line are Not supplied; the borrower under the revolving credit facility changed from Rocket Mortgage, LLC (2025 agreement) to Rocket Companies, Inc. (2026 agreement) with no statement on amendment (10-K page:222; Q3 10-Q page:71). | Medium | CP-2 | Obtain the revolver and indenture exhibits and the guarantor list. |
| Unreconciled date of the 2030 and 2033 note offering: October 2025 in the note table footnotes against June 2025 elsewhere (10-K page:181, page:222; Q3 10-Q page:67). | Low | CP-2, CP-5 | Confirm against the indenture dated June 20, 2025 and the Form 8-K; do not choose between the two. |
| The Bridge Facility amount and any drawing are Not supplied; it is defined and its fees were expensed but it is not in the debt tables (Q3 10-Q page:2, page:55). | Low | CP-2 | Confirm that no bridge balance existed at any reporting date. |
| Customer and counterparty concentration is Not disclosed beyond the Agencies; revenue by counterparty is not printed. | Low | CP-2 | Use qualitative Agency dependence only. |
| Ratings, market quotes and peer data are Not supplied; context lists none. | Medium | CP-2 | Obtain agency publications dated on or before 2026-11-05. |
| No source is dated after October 30, 2026 although the cutoff is 2026-11-05; post-quarter events are only those in Q3 10-Q footnotes. | Medium | CP-2, CP-5 | Obtain the filing list for October 30 to November 5, 2026. |
| Management Language rows (market position, retention, AI, number-one rankings from an external publisher, board size) are attributed and unaudited. | Low | CP-5 | Keep attributed; do not use as independent evidence. |
| Governance assessment rests on documented actions only; no evidence on individuals or intent is used, and sponsor identity is not used to infer willingness. | Low | CP-2 | None; this is a method boundary. |

## Next module

Proceed to CP-2 (fundamental credit synthesis) on the CP-1A rows and the CP-1 figures, carrying: the two debt layers and leverage anchor from CP-1; the equity-funded acquisitions and servicing scale; Agency counterparty dependence and rate sensitivity; founder control with unseen protective documents; the mixed documented sponsor behaviour with no creditor-adverse action; the HouseCanary and data breach legal exposure; and the two unreconciled source differences (note offering date and revolver borrower). CP-5 then traces each claim to its page. No recovery conclusion, peer ranking or instrument recommendation is made here.
