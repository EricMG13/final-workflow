## Request

Issuer: Uniti Group Inc. (issuer id unit; Nasdaq ticker UNIT). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, in millions as the filings print. Current period named by the context: Q2 2026. Prior period named by the context: FY2025.

Task for this module: build the business and transaction context a credit committee reads first: the transaction and ownership structure, the business and operating model, and credit-relevant history, with issuer-level governance and behaviour read from documented actions only. Each material conclusion runs evidence, then risk mechanic, then credit implication. The context names no sponsor, parent, borrower, guarantor, deal terms or ratings; those blanks are treated as not supplied. No peer ranking, instrument recommendation or recovery conclusion is given. Financial figures are those of the accepted financial base handoff and are referred to, not recomputed.

## Sources

Each issuer file is one JSONL text extraction of an SEC filing. The locator `page:N` is the extraction chunk, not the printed page.

### Issuer sources relied on

| Source name | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_unit-20251231.htm.jsonl | 6d67619ba1ab3647c20a79710ac6373101e1f3efd1454ad58308edf1101a7a6b | Business, segments, merger, ownership, dividend policy, preferred stock terms and refinancing history (page:5-7, page:10, page:15, page:28, page:42-44, page:48, page:55-58) |
| 10-Q_2025-09-30_unit-20250930.htm.jsonl | 5887e391d2d0fd28ff7625b79ed82dcf62027435a26c54f6cbb097f48f8f2e90 | Read for the first post-merger quarter; not cited for a fact below |
| 10-Q_2026-03-31_unit-20260331.htm.jsonl | 6eef1c3a3881ef793ddfc9610c4d46208d57c3bb26c5a88a18ed1115bb75d5ba | Maturity table at 2026-03-31 (page:31) |
| 10-Q_2026-06-30_unit-20260630.htm.jsonl | 44ae41cd731221c3fab785c468962d8927f45d4ed20722ebe4d9e689ea9bcd05 | Merger consideration and settled relationships (page:9-10, page:16-18), debt and ABS structure (page:20-30), unrestricted subsidiaries (page:50), subsequent events (page:52-54), segments (page:47-48), customers (page:70) |
| EX-99.1_2026-03-02_unit-ex991202510xk.htm.jsonl | c7190cfa9cb627d04b3e648821ebf4356c56f99434b32385548463e0d9accab6 | Management characterisation of 2025, the hyperscaler contract and fiber build target (page:1) |
| EX-99.1_2026-05-11_unit-ex9911q26.htm.jsonl | cfd5a9da978c996627652ac9d3c7077c0533d727405c7b27dfe93c7e85d28fc5 | Read for Q1 2026 context; not cited for a fact below |
| EX-99.1_2026-07-30_unit-ex9912q26.htm.jsonl | 1d9925874068c008696dd366506144e0d697bf35f0c978f5473bf3052738ff6f | Management characterisation of Q2 2026 and the July 2026 financing (page:1-2) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | e531a4ec67bdeec3bf2b02e8047c90f4c69262abee202a8c1e2071ff24adf370 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 013c310c8396f81ac9f077f177c9c4e522274d65b9d75cc140acddd2c5a45803 | Source readiness: perimeter change at 2025-08-01, no executed debt documents, nothing after 2026-07-30 |
| CP-1 | 825e72c7214f02408d5dc6ffc79807be881b2e40ab76417f16f55955164b5b08 | Financial base: leverage, cover, liquidity, maturity profile and claims outside debt |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Uniti is a fiber network operator formed by the 2025-08-01 merger of Old Uniti and Windstream, with Elliott holding about 25.2%. It is funding a large fiber build with debt, increasingly through asset-backed notes held in unrestricted subsidiaries. | Medium | No executed indentures or credit agreements are supplied, so creditor protections and basket capacity on asset transfers are not verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The merger ended Old Uniti's role as Windstream's landlord and combined the two debt groups under one borrower with cross-guarantees. | Lease income from Windstream no longer appears as external revenue, and former separate creditor groups now share one credit group. | High |
| Elliott and affiliates own approximately 25.2% of common stock, hold board designation rights, and affiliates can require repurchase of the 575.0 million preferred after the tenth anniversary. | A concentrated holder influences strategy and holds a claim senior to common equity. | High |
| Fiber network assets and customer contracts have been moved into unrestricted asset-backed subsidiaries, in January 2026 and July 2026. | Value moves from the restricted group to separate non-recourse creditors, which can weaken other secured and unsecured holders. | Medium |
| The filings contain two internal inconsistencies, on the ranking of the 8.625% notes and on the year-by-year maturity table. | Ranking and maturity timing should be confirmed against the indentures before use. | Medium |

### Business and transaction view

Uniti Group Inc. is a Delaware holding company that survived the 2025-08-01 merger of Windstream and Old Uniti as the ultimate parent. Old Uniti was a REIT that owned and leased communications infrastructure, with Windstream as its anchor tenant; after the merger it ceased to be a REIT and the company does not qualify as one. The combined business has three segments. Kinetic sells consumer and small business broadband and voice in incumbent markets. Fiber Infrastructure sells enterprise, carrier and wholesale connectivity, including to hyperscalers, and holds the legacy fiber and leasing assets. Uniti Solutions sells managed network, security and collaboration services to enterprises. The credit story is the build-out of fiber to the home at Kinetic and of wholesale fiber, funded by debt. The creditor-relevant mechanics are these. First, the perimeter changed, so history before the merger is Old Uniti. Second, all pre-merger debt of Old Uniti and Windstream was merged into one borrower, Uniti Services LLC, with cross-guarantees and the removal of restrictive covenants that kept the groups apart. Third, since 2026-01-30 the company has financed Kinetic through asset-backed notes issued by bankruptcy-remote unrestricted subsidiaries that hold the fiber assets and customer contracts, which places those assets and their cash flows ahead of other creditors for those noteholders. Fourth, Elliott and its affiliates hold about 25.2% of the common stock and have rights tied to the preferred stock. Fifth, the company states that it does not intend to pay common dividends. No sponsor is named in the context. Behaviour toward creditors is read as neutral or mixed on documented actions: refinancing that extended the maturity profile and transparent disclosure of unrestricted subsidiary results on one side, and transfers of assets from guarantor subsidiaries into unrestricted asset-backed structures on the other. Legal capacity for those transfers depends on indenture terms that are not supplied.

### Company profile

| Attribute | Fact | Category | Source |
| --- | --- | --- | --- |
| Registrant and incorporation | Uniti Group Inc., Delaware, incorporated 2024-04-19 as Windstream Parent, Inc. as a subsidiary of Windstream; renamed on the merger | Documentary Fact | 10-K page:5-6 |
| Listing and sector | Nasdaq Global Select Market, symbol UNIT; the context gives sector Telephone Communications (No Radiotelephone) and country United States (context, not issuer evidence) | Documentary Fact | Q2 10-Q page:1; context |
| Network scale | About 240,000 fiber route miles across 47 states, more than 1.0 million customers, more than 500,000 residential fiber customers, about 1.9 million fiber-equipped households | Documentary Fact (company statement in the filing) | 10-K page:5 |
| Segments | Kinetic, Fiber Infrastructure, Uniti Solutions | Documentary Fact | Q2 10-Q page:8; 10-K page:6 |
| Ownership at the merger | Old Uniti stockholders about 62% and Windstream stockholders about 38% of the company before convertible securities and warrants | Documentary Fact | 10-K page:6; Q2 10-Q page:9 |
| Concentrated holders | Two largest stockholders, directors and officers about 36.1%; Elliott Investment Management, L.P. and affiliates about 25.2% of common stock, before warrants or preferred conversion | Documentary Fact | 10-K page:42 |
| Governance rights | Elliott may designate two directors (or 20% of the board if the board exceeds nine) while holding at least 50% of its original shares, and one (or 10%) while holding at least 25% but less than 50% | Documentary Fact | 10-K page:42 |
| Preferred stock | 575.0 liquidation preference issued to Windstream equityholders; 11% dividend for the first six years, rising thereafter to a 16% cap; company redemption right; Elliott affiliates may require repurchase after the tenth anniversary, settled in cash or common stock | Documentary Fact | Q2 10-Q page:10; 10-K page:44 |
| Warrants | About 17.6 million warrants at a 0.01 dollar exercise price, about 6.9% fully diluted | Documentary Fact | Q2 10-Q page:10 |
| Dividend policy | No intention to pay common dividends for the foreseeable future | Documentary Fact | 10-K page:43 |
| Sponsor and parent | None named in the context or the sources; Elliott is a stockholder, not described as a sponsor in the sources | Insufficient Information (sponsor); matters because sponsor behaviour cannot be scored | Context; 10-K page:42 |
| Auditor | PricewaterhouseCoopers LLP for FY2025, auditor since 2025; KPMG LLP audited FY2024 and the year before | Documentary Fact | 10-K page:99-100 |
| Customer concentration | After the merger no single customer provides more than 10% of consolidated revenues and sales; a large hyperscaler signed a dark fiber IRU in Q1 2026 | Documentary Fact | Q2 10-Q page:47, page:63 |

### Company and operating model

| Area | What the evidence states | Risk mechanic and credit implication | Category | Source |
| --- | --- | --- | --- | --- |
| Kinetic | About 1,400 markets in 18 states; broadband internet, voice and Wi-Fi equipment leases to residential and small business; fiber consumer customers 602.8 thousand and DSL consumer customers 357.6 thousand at 2026-06-30; strategy is fiber build, penetration and churn reduction | Growth depends on fiber construction that costs capital before revenue; the DSL base is declining, so fiber ramp must outrun copper decline to hold cash flow. Capital spending of 602.8 in H1 2026 was the largest segment use of cash (see the financial base) | Documentary Fact | 10-K page:7; Q2 10-Q page:70 |
| Fiber Infrastructure | Enterprise and wholesale fiber connectivity to banks, schools, carriers, cable and hyperscalers; legacy Uniti fiber and leasing combined with Windstream's CLEC wholesale business; external revenue fell from 300.7 in Q2 2025 to 200.3 in Q2 2026 as Windstream lease income ended | The segment's contribution margin of about 52% in Q2 2026 exceeds Kinetic's about 42% and Uniti Solutions' about 50% (EX-99.1 2026-07-30 page:2), but the revenue base reset on the merger; new wholesale and IRU revenue must replace the former lease income. IRU sales revenue is recognised when control transfers, so it is lumpy | Documentary Fact; Analyst Interpretation on lumpiness | 10-K page:15; Q2 10-Q page:47, page:70, page:75 |
| Uniti Solutions | Managed network, security and collaboration for enterprises; Q2 2026 external revenue 181.2 and contribution margin 91.8 | Service revenue with high customer access costs; contribution margin is before corporate costs and depreciation | Documentary Fact | 10-K page:10; Q2 10-Q page:48 |
| Revenue model | Service revenues (broadband, voice, wholesale, managed services, lease income, USF and RDOF receipts) and sales revenues (dark fiber IRU sales-type leases, equipment) | Sales-type lease revenue is front-loaded and not recurring; service revenue carries the debt service | Documentary Fact | Q2 10-Q page:35-36, page:75 |
| Cost structure | Segment costs are compensation, network access and facilities, revenue-driven costs and customer access; corporate and shared costs, depreciation, transaction costs and interest sit outside segments | Corporate costs are not visible in segment margin, so segment margin overstates cash conversion | Documentary Fact | Q2 10-Q page:47-49 |
| Capital spending | Kinetic fiber build to 1.9 million homes at year-end 2025 with management's goal of 3.5 million homes passed by the end of 2029 | Funded by debt issuance while operating cash flow is below capital spending (see the financial base); the 2029 goal is a management claim, not a commitment shown in the filings | Management Language | EX-99.1 2026-03-02 page:1; EX-99.1 2026-07-30 page:1 |
| Working capital and deferred revenue | Deferred revenue current 256.3 and noncurrent 390.0 at 2026-06-30, largely customer prepayments | Non-cash obligation to deliver service; prepayments flatter early cash flow | Documentary Fact | Q2 10-Q page:5 |
| Pension and retiree | Pension plan assumed in the merger; minimum employer contributions of 20.6 in 2026 | Fixed cash claim outside debt | Documentary Fact | Q2 10-Q page:41 |

### Transaction summary and new debt issues

The Merger. On 2025-08-01 Windstream merged into the company, which survived as ultimate parent, and a merger subsidiary merged into Old Uniti, which survived as an indirect wholly owned subsidiary (Q2 10-Q page:9). Each Old Uniti share converted into 0.6029 shares of the company's common stock. Windstream's equityholders received about 90.1 million common shares, about 0.6 million preferred shares with a liquidation preference of 575.0, about 17.6 million warrants at a 0.01 dollar exercise price and 370.7 of cash, funded from Old Uniti's cash and revolver borrowings (page:10). The accounting is a reverse merger: Windstream was legal acquirer and Old Uniti was accounting acquirer (page:10). Total merger consideration was 2,376.6, made up of common stock 733.7, preferred stock 630.4, warrants 142.7, cash 370.7 and 499.1 attributed to the settlement of preexisting relationships (page:16). Those relationships were the Windstream Leases (an ILEC master lease and a CLEC master lease under which Old Uniti was Windstream's landlord), an asset purchase agreement and other leasing and supplier arrangements; they became intercompany and eliminated, and the leases were judged above market by 559.0 against an unfavourable asset purchase agreement of 60.0 (page:17-18). Status: complete; purchase price allocation finalised in Q2 2026 (page:18). Credit meaning: the Windstream lease payments that Old Uniti received as landlord ceased to be external revenue; creditors of the two former groups now rank in one structure.

Debt reorganisation. On 2025-08-04 Uniti Group LP, the borrower under Old Uniti's debt, was merged into Uniti Services LLC, formerly Windstream Services, LLC, the borrower under Windstream's debt. All debt became obligations of the same borrower, each subsidiary that guaranteed one group's debt guaranteed the other's, the Windstream revolver became pari passu with other first lien debt, and restrictive covenants that kept the groups apart were effectively eliminated (10-K page:56). Credit meaning: structural separation between the two creditor groups ended; the combined guarantor group supports all debt.

New debt issues, in date order, with status (all amounts in the financial base or the debt tables):
- October 2025: 1.4 billion of 7.50% senior secured notes due 2033 and a new seven-year 1.0 billion term loan due 2032; proceeds redeemed in full the 10.50% secured notes due 2028 and added more than 100.0 of liquidity; 250.0 of secured fiber network revenue term notes with anticipated repayment in January 2031 were also issued (10-K page:56). Status: complete.
- 2025: 600.0 of 8.625% senior unsecured notes issued 2025-06-24 under an indenture with Deutsche Bank Trust Company Americas as trustee (Q2 10-Q page:26). Status: complete.
- 2026-01-30: Kinetic ABS 2026-1 notes of 960.1, secured by fiber network assets and residential customer contracts in Texas, Arkansas, Kentucky, Ohio and Georgia that were sold to the ABS obligors, which are unrestricted subsidiaries; no recourse to the company or other subsidiaries (Q2 10-Q page:26-29). The notes pay interest monthly, have no scheduled principal before the anticipated repayment date in February 2031, and carry rapid amortization if a debt service coverage ratio is not maintained (page:28, page:30). The indenture also provides for a variable funding note facility and up to 14.0 of liquidity funding notes, none outstanding (page:28-29). Status: complete.
- 2026-02-04: 1.0 billion of 8.625% senior unsecured notes due 2032, expected to be exchanged for additional notes fungible with the existing 600.0; proceeds repaid the 500.0 Windstream Term Loan, revolver borrowings and funded general purposes including success-based capital expenditures (page:26). Gain on extinguishment of 1.2 (page:30). Status: complete.
- 2026-07-15 (subsequent event): Kinetic ABS 2026-2 notes of 1,140.7, anticipated repayment June 2033, bought assets held by subsidiary guarantors of the company's senior debt that were contributed to Kinetic ABS subsidiaries; the company intends 500.0 of net proceeds to repay senior secured debt through a term loan prepayment offer and asset sale offers, and the rest for reinvestment including growth capital spending (page:52). Status: complete for the notes; the repayment offers were open at the filing date and their uptake is not supplied.
- 2026-07-23 and 2026-07-30: term loan prepayment offer of up to 167.8, of which 19.8 was repaid on 2026-07-30, and asset sale offers for up to 332.2 of the 4.75% and 7.50% secured notes expiring 2026-08-20 unless extended (page:63; EX-99.1 2026-07-30 page:2). Status: outcome not supplied.

Credit meaning of the new issues: they extended the maturity profile and moved the funding of the Kinetic build to asset-level debt. The ABS structure ranks the noteholders first against the transferred assets, and the asset sale offers show that part of the proceeds is required to repay secured debt because the assets came from guarantor subsidiaries. How much cushion the restricted group retains depends on indenture terms that are not supplied.

### Ownership, control and behaviour

| Behaviour area | Documented action | Category and scoring dimension | Legal capacity, willingness, feasibility | Evidence quality | Source |
| --- | --- | --- | --- | --- | --- |
| Debt combination | One borrower and cross-guarantees after 2025-08-04; restrictive covenants separating the groups removed | Neutral or Mixed; creditor protection | Capacity: documents permitted it; willingness: done within days of closing; feasibility: not tested | High | 10-K page:56 |
| Asset transfers to unrestricted subsidiaries | Fiber assets and customer contracts sold or contributed to Kinetic ABS entities in January 2026 and July 2026, including assets from subsidiary guarantors; ABS notes non-recourse to the company; part of proceeds directed to repay secured debt | Neutral or Mixed; asset movement. Not classed as Creditor-Adverse because the basket capacity and consent terms are not supplied | Capacity: not verifiable without indentures; willingness: documented; feasibility: depends on market access, which was open for ABS | High for the facts, Insufficient for capacity | Q2 10-Q page:28-29, page:50, page:52 |
| Shareholder distributions | No common dividends intended; preferred dividends declared and mostly paid in cash, with a small amount paid in kind in Q2 2026 | Supportive on common; preferred is a cash claim | Capacity: not verifiable; willingness: stated; feasibility: cash flow after capital spending is negative (see the financial base) | High | 10-K page:43; Q2 10-Q page:6, page:7 |
| Refinancing | Redeemed the 10.50% secured notes due 2028 in October 2025 and repaid the Windstream Term Loan in February 2026 | Supportive; maturity profile | Feasibility demonstrated by market access | High | 10-K page:56; Q2 10-Q page:26 |
| Reporting | Condensed balance sheet and income statement of unrestricted subsidiaries are published each quarter | Supportive; transparency | Not applicable | High | Q2 10-Q page:50-51 |
| Elliott | Elliott affiliates hold the repurchase right on the preferred stock and board designation rights; Elliott has other investments in FCC-licensed companies and Crown Castle | Neutral or Mixed; control. No action toward creditors is documented | Capacity: board and stockholder rights per the stockholder agreement, which is not supplied; willingness: Insufficient Information | Medium | 10-K page:42, page:44 |

### Timeline

| Date | Event | Type | Source |
| --- | --- | --- | --- |
| 2020 | Settlement agreement between Old Uniti and Windstream with cash installments over 20 consecutive quarters starting October 2020; final installments paid January, April and July 2025 | History | Q2 10-Q page:12 |
| 2024-04-19 | Registrant incorporated as Windstream Parent, Inc. | History | 10-K page:5 |
| 2025-08-01 | Merger completed; Old Uniti ceases to be a REIT | Ownership change | Q2 10-Q page:9 |
| 2025-08-04 | Uniti Group LP merged into Uniti Services LLC; debt combined | Refinancing | 10-K page:56 |
| 2025-10 | 7.50% secured notes due 2033, 2032 term loan, 250.0 fiber ABS notes, redemption of 10.50% notes | Refinancing | 10-K page:56 |
| 2026-01-30 | Kinetic ABS 2026-1 notes | Financing | Q2 10-Q page:26 |
| 2026-02-04 | 8.625% notes due 2032; Windstream Term Loan repaid | Financing | Q2 10-Q page:26 |
| 2026-03-02 | FY2025 10-K and results; largest customer contract announced by management | Reporting | EX-99.1 2026-03-02 page:1 |
| 2026-07-15 | Kinetic ABS 2026-2 notes (subsequent event) | Subsequent event | Q2 10-Q page:52 |
| 2026-07-23 to 2026-07-30 | Term loan prepayment and asset sale offers | Subsequent event | Q2 10-Q page:63 |

### Conflicts logged

| Conflict | Span A | Span B | Downstream effect | Resolution |
| --- | --- | --- | --- | --- |
| Ranking of the 1.0 billion 8.625% notes issued 2026-02-04 | 10-K page:28: "issuance of $1.0 billion of 8.625% secured notes" | 10-K page:57: "$1.0 billion aggregate principal amount of 8.625% Senior Notes due 2032 (the “2026 Unsecured Notes”)"; Q2 10-Q page:26: "unsecured 8.625% Senior Notes due 2032" | The secured or unsecured ranking of this tranche changes the amount of debt ranking behind secured creditors | Logged, not reconciled. The debt tables and the Q2 10-Q describe the notes as senior unsecured; the risk factor wording differs |
| Debt maturity table versus instrument due dates, Q2 10-Q | Q2 10-Q page:30: "Remainder of 2026 $ 10.0 2027 886.5 2028 1,120.0 2029 1,299.0 2030 1,220.1 Thereafter 6,145.0" | Q2 10-Q page:20-21 gives due dates 2028-04-15 (4.75% notes 570.0), 2029-02-15 (6.50% notes 1,110.0), 2030 (6.00% notes and Fiber ABS 2025-1) and 2031 (Fiber ABS 2025-2 and Kinetic ABS 2026-1); Q1 10-Q page:31: "Remainder of 2026 $ 7.5 2027 316.5 2028 580.0 2029 1,120.0 2030 1,299.0 Thereafter 7,360.1" | Years 2027 to 2030 differ by one year between the Q2 table and the due dates; totals agree at 10,680.6. The Q2 remainder-of-2026 figure (10.0) also differs from the Q1 figure (7.5) | Logged, not reconciled. The financial base handoff said no maturity table was printed and built its maturity chart from instrument due dates; that statement is corrected here: a table is printed at Q2 10-Q page:30, and it conflicts with the due dates for 2027 to 2030. The financial base chart follows the due dates. The table printed in the Q1 10-Q agrees with the due dates |

## Calculations

No new calculation. Financial amounts are those printed in the filings or in the accepted financial base handoff. Two tie-outs on this module's own text:

| Check | Inputs | Result |
| --- | --- | --- |
| Total merger consideration | 733.7 + 630.4 + 142.7 + 370.7 + 499.1 (Q2 10-Q page:16) | 2,376.6, equal to the printed total |
| Maturity table total | 10.0 + 886.5 + 1,120.0 + 1,299.0 + 1,220.1 + 6,145.0 (Q2 10-Q page:30) | 10,680.6, equal to the printed total and to total principal |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed indentures, credit agreements, ABS base indenture and series supplements are not supplied, so basket capacity for asset transfers to unrestricted subsidiaries, ranking and guarantor lists are unverified | High | CP-2, CP-5 | Supply the executed documents |
| Elliott Stockholder Agreement and preferred stock certificate of designation not supplied | Medium | CP-2 | Supply the documents |
| Conflicts on the 8.625% notes ranking and the maturity table are logged but unresolved | Medium | CP-2, CP-5 | Confirm against the indenture and a corrected schedule |
| Outcome of the asset sale offers and term loan prepayment not supplied | Medium | CP-2 | Supply later filings |
| Merger Agreement and Windstream Leases not supplied; only filing descriptions | Low to Medium | CP-2 | Supply if transaction detail is needed |
| No ratings, sponsor, valuation or peer data in the context | Low for the selected modules | CP-2 | Not required for this scope |
| Debt schedule, covenant certificate and add-back bridge not supplied | Medium | CP-2 | Supply compliance certificate and definitions |
| Management claims in releases (fiber build target, record bookings) are not independently supported | Low | CP-5 | Carry as management language |

## Next module

- CP-2: take the perimeter change, the single borrower with cross-guarantees, the growing share of debt in non-recourse asset-backed subsidiaries, Elliott's holdings and the preferred stock as structural inputs. Carry the two logged conflicts as restrictions: use the due dates for the maturity wall and treat the ranking of the 1.0 billion 8.625% notes as unsecured per the debt tables and the Q2 10-Q until the indenture is supplied. Carry the correction to the financial base: a maturity table is printed at Q2 10-Q page:30 and disagrees with the due dates.
- CP-5: cite page chunks as given; label the fiber build target, record bookings and customer contract statements as management language; do not cite the 10-K risk factor for the ranking of the 8.625% notes.
