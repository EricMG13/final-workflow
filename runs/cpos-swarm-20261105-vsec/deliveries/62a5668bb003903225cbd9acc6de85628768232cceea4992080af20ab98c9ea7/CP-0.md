## Request

This handoff assesses source readiness for VSE CORP (registrant VSE Corporation, ticker VSEC, Delaware; issuer id vsec) as of 2026-11-05, pathway credit_snapshot, reporting currency USD, current period Q3 2026 against FY2025. The cutoff is 2026-11-05. The requested downstream work is CP-1, CP-1A, CP-2 and CP-5. This module answers one question: can the seven supplied filed sources support that work, and what stays blocked. It gives no credit conclusion and calculates no credit metric. The context file holds the run settings only, and its blank fields (ratings, quotes, deal terms, peers, research questions) are left blank, not read as zero.

## Sources

Issuer sources relied on. Each is a text conversion of an HTML filing, pinned by the sha256 below (the sha256 of the converted file CP-OS supplies). Labels S1 to S7 are used in the rest of this handoff. Locators are `page:N`, the chunk number in the converted file, not the printed page.

| Label | Exact source name | sha256 | Document family and period |
| --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_vsec-20251231.htm.jsonl | 83b072172f28f55aebaf3a6972f9c86687a4b113bdf988f323774cea0cf36aed | Annual report on Form 10-K, fiscal year ended 2025-12-31, 82 pages, audited |
| S2 | 10-Q_2026-03-31_vsec-20260331.htm.jsonl | f6b924ea5eba470e1f49667b84c48b593c43a380b95f687d6114875e8f37f39d | Quarterly report on Form 10-Q, quarter ended 2026-03-31, 28 pages, unaudited |
| S3 | 10-Q_2026-06-30_vsec-20260630.htm.jsonl | fa3609d44d226dc8671529fb2fbfc175fcb641b5ffc98070769608107bc75600 | Quarterly report on Form 10-Q, quarter ended 2026-06-30, 34 pages, unaudited |
| S4 | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | 68af0ce7093699c714a705843bb9cea05a028d2dd1bb6a0a12fdd362022c36f1 | Quarterly report on Form 10-Q, quarter ended 2026-09-30, 36 pages, unaudited |
| S5 | EX-99.1_2026-05-05_vse-prxq1x2026earningsrele.htm.jsonl | 1a0b0741e0cb41d8d01fb77bba0765b0d91e0ee2d640c0871a3ef4c38f0e2f04 | Earnings release dated 2026-05-05, Q1 2026, 10 pages, management document |
| S6 | EX-99.1_2026-08-05_vse-prxq2x2026earningsrele.htm.jsonl | 047a25aea3f55f6b12255c44556aba2d1cd8074d64427d9b3bf8fc3f0328e7e4 | Earnings release dated 2026-08-05, Q2 2026, 13 pages, management document |
| S7 | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | 433c5d4af4ceef97f7133d6bf32c06676acee7a23adece5c52f374d8108500f0 | Earnings release dated 2026-11-04, Q3 2026, 13 pages, management document |

Run settings (not issuer evidence): context sha256 40207d2127823884a7bc8082859719f4c4c78b2e88a9548b0c57178ea14b1746. The pack folder also holds `_retrieval.json`, which CP-OS ignored; it is retrieval metadata, not a filed source, and is not relied on.

Supplied handoffs: none. CP-0 is the first module of this run, so no earlier handoff exists to list.

How far each source was read: S4 and S7 were read in full (36 of 36 and 13 of 13 pages). S1, S2, S3, S5 and S6 were searched for debt, liquidity, covenant, acquisition, subsequent-event, definition and cash-flow content and read at the pages cited below; their remaining pages (S1 business, risk factors, tax, equity compensation and exhibit pages in particular) were located by heading but not read line by line. That is a bounded inspection, not a full fidelity review of those five sources.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed sources support financial, business and credit work on VSE through the third quarter of 2026, with limitations. They do not support covenant headroom or guarantor analysis, because the credit agreement and its amendment are absent. | Medium | Covenant levels, guarantor list and the amended credit agreement are not supplied; acquisition-adjusted earnings cannot be rebuilt from the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt by facility, maturities, liquidity and interest rates are disclosed at the latest quarter end in the filed quarterly report. | Facility-level debt, maturity and liquidity work can proceed from filed statements. | High |
| The filings say a maximum net leverage test and a minimum interest coverage test exist and were met, but give no levels or step-downs. | Covenant headroom cannot be measured until the credit agreement and its amendment are supplied. | High |
| The May 2026 acquisition added a large new business, and its purchase accounting is still preliminary. | Comparisons with 2025 mix different perimeters; trend and leverage work needs pro forma care. | High |
| Management leverage ratios use net debt after issuance costs and, for the lower ratio, earnings including pre-acquisition periods with no component schedule. | Reported leverage is a management measure, not covenant leverage, and part of it cannot be verified. | Medium |
| Cash paid for interest and taxes appears only in the annual report; the 2026 interim reports do not give it. | Cash interest cover for 2026 cannot be built from cash paid; only expense figures are available. | High |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for the requested work. Every period the run needs is covered by a filed statement: FY2025 audited (S1) and Q1, Q2 and Q3 2026 unaudited (S2, S3, S4), each with balance sheet, operations, cash flow and notes, plus three earnings releases (S5, S6, S7) that supply discrete quarters, non-GAAP reconciliations, net debt and leverage tables, and guidance. The strongest contrary evidence is that the legal documents behind the debt are absent: the registrant states a maximum Total Net Leverage Ratio and a minimum Interest Coverage Ratio but never prints a level, and the May 2026 amendment that created the USD 900.0 million term loan B is described only in the notes. That does not stop the financial, business or credit work, but it blocks covenant headroom, guarantor and security analysis and any claim about definitions in the credit agreement. The second limitation is perimeter: the Precision Aviation Group acquisition on 2026-05-05 contributed USD 173.7 million of Q3 2026 revenue of USD 541.0 million (S4 page:29 and page:30), so FY2025 and the first four months of 2026 describe a different business from Q3 2026, and the acquisition accounting is preliminary. The next evidence action is to obtain the credit agreement dated 2025-05-02, the first amendment dated 2026-05-05, and the amortizing-note terms, and to have each consumer use filed statements ahead of release figures wherever the two differ.

### Source assessment

| Label | Original authority and perimeter | Period and basis | Located evidence | Limitation carried forward |
| --- | --- | --- | --- | --- |
| S1 | Filed audited annual report of VSE Corporation, consolidated, with the auditor's opinion | FY2025, year ended 2025-12-31, USD thousands, continuing operations after the Federal and Defense and Fleet sales | S1 page:39 "present fairly, in all material respects, the financial position of the Company as of December 31, 2025 and 2024" | Pre-dates the 2026 acquisition and the new term loan B; describes the PAG deal as a subsequent event (S1 page:73) |
| S2 | Filed unaudited interim report, consolidated | Q1 2026, quarter ended 2026-03-31 | S2 page:4 "Cash and cash equivalents $ 1,239,407 $ 69,358" | Cash of that size is pre-closing; the acquisition and new facilities are subsequent events at this date |
| S3 | Filed unaudited interim report, consolidated | Q2 2026 and six months to 2026-06-30 | S3 page:15 "Principal amount of long-term debt 966,668 296,250" | First balance sheet after the acquisition; purchase accounting preliminary |
| S4 | Filed unaudited interim report, consolidated; latest filed statements | Q3 2026 and nine months to 2026-09-30 | S4 page:17 "Principal amount of long-term debt 978,793 296,250" | Signed 2026-11-05, the cutoff date (S4 page:36 "Date: November 5, 2026 By: /s/ John A. Cuomo"); purchase accounting preliminary |
| S5 | Management earnings release, furnished, not a filed statement | Q1 2026, with non-GAAP measures | S5 page:6 "Net Debt $ (878,432) $ 223,446" | Non-GAAP definitions differ from later releases; supporting claims only |
| S6 | Management earnings release | Q2 2026 and six months | S6 page:8 "Net Debt $ 871,597 $ 223,446" | Adjusted Net Income and Adjusted EPS definition changed; supporting claims only |
| S7 | Management earnings release | Q3 2026 and nine months | S7 page:7 "TTM Acquisition Adjusted EBITDA from continuing operations (2) $ 389,234 $ 209,128" | Latest management measures and guidance; supporting claims only; the accompanying call materials are not in the pack |

Entity and perimeter. All seven sources report VSE Corporation consolidated (single reportable segment, Aviation: S4 page:21 "manages its business as a single reportable and operating segment"). No parent, sponsor or stand-alone borrower statements exist; the context names no borrower, parent or guarantors. The borrower under the credit agreement is the Company, with subsidiary guarantors, per the exhibit list (S1 page:81 "10.8 Credit Agreement, dated as of May 2, 2025"), but no source names the guarantors, so the restricted or guaranteeing group is an unresolved distinction. The seller of the acquired target was paid partly in newly issued equity of an unnamed VSE subsidiary (S4 page:10, 1,415,752 shares, exchangeable one-for-one into Company common stock by 2029-05-05); that subsidiary is not identified.

### Consumer readiness

| Consumer | Status | Evidence demand met | What is carried forward |
| --- | --- | --- | --- |
| CP-1 financial base | READY_WITH_LIMITATIONS | Annual and interim statements, discrete quarter data in releases, debt by facility in S4 page:17 and page:19, segment and revenue-type tables in S4 page:16 and page:17 | Perimeter break at 2026-05-05; Q4 2025 is not reported alone; no 2026 cash-paid interest or taxes; reconciliation of non-GAAP figures not performed here |
| CP-1A business and transaction | READY_WITH_LIMITATIONS | Acquisition notes for PAG, Atech, NorthStar, Aero 3 in S4 page:8 to page:15; financing offerings in S4 page:25 to page:27 | Preliminary purchase accounting; no executed purchase agreement, no pro forma EBITDA; Test Logic price not disclosed |
| CP-2 credit | READY_WITH_LIMITATIONS | Debt by facility, maturity table, liquidity, swaps, compliance statement | Covenant levels, definitions, margins on the amended facilities and guarantor structure not supplied; no ratings or market quotes in context |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | All seven sources are locatable by page | Must carry every gap below and the release-versus-filing precedence rule |

### Conflicts and version relationships

The three 10-Qs and the 10-K are successive periods, not versions of one another; each stays an active source. The three releases are management documents and each stays active. Where a release and a filing differ, the filing controls and the release is an attributed claim. The differences found are listed here with locators and their effect.

| Item | Source A | Source B | Effect downstream |
| --- | --- | --- | --- |
| PAG consideration | S2 page:20 "total upfront consideration of approximately $2.025 billion, consisting of $1.750 billion in cash" | S4 page:10 "Total purchase consideration $ 2,020,007" (thousands; cash paid 1,770,370, equity 238,002 and earn-out fair value 33,850, from S4 page:9 and page:10) | Different bases (headline upfront versus accounting consideration at fair value, with working-capital adjustments); not reconciled here. CP-1A must quote each with its basis |
| Revolver availability at 2026-06-30 | S6 page:3 "approximately $500.0 million available under its revolving credit facility" | S3 page:29 "$499.3 million of unused commitments under the Credit Agreement" | Release rounds; use the filing figure for liquidity |
| Term loan naming | S1 page:74 refers to a "New Term Loan A Facility" upsize under the debt commitment letter | S4 page:18 describes a new "senior secured term loan B facility" that "replaced the Company's previous term loan"; S5 page:2 "The new Term Loan B refinanced and replaced the Company's existing Term Loan A." | The commitment-stage structure in the 10-K was superseded by the executed structure; use S4 for the structure |
| Adjusted measures | S5 page:4 "Adjusted EBITDA margin represents estimated operating income before depreciation and amortization expenses as a percentage of revenue", and Adjusted Net Income there is adjusted only for acquisition-related costs and other discrete items | S6 page:1 "which reflect a change in the definition of Adjusted Net Income and Adjusted EPS (Diluted)"; S7 page:4 "Beginning with the second quarter of 2026, Adjusted Net Income from continuing operations and Adjusted EPS" | Q1 adjusted net income and EPS in S5 are not comparable with Q2 and Q3 figures; prior periods are restated retrospectively in S6 and S7 only |
| Leverage measures | S7 page:5 "differ from the Total Net Leverage Ratio as defined in the Company" (credit agreement) | S4 page:19 covenant is a "maximum Total Net Leverage Ratio" with no level | Reported net leverage ratios cannot be used as covenant headroom |

Net debt as the releases define it deducts debt issuance costs as well as cash (S7 page:5 "Net debt is defined as principal amount of debt less debt issuance costs and less cash and cash equivalents"). That is a management definition and differs from principal less cash; consumers must state which they use.

### Evidence, risk mechanism and consequence

First, the debt: S4 page:19 gives the maturity table by facility, "Total $ 897,750 $ 20,000 $ 61,043 $ 978,793", which is a filed statement and fully supports the facility-level debt and maturity-wall work; the risk is only that the instrument terms behind it (guarantees, security, covenant levels) are not in the pack, so CP-2 must describe those as stated by the registrant and not test them. Second, liquidity: S4 page:32 states "$479.2 million of unused commitments under the Credit Agreement" and S4 page:17 gives letters of credit and interest rates, so liquidity can be built from filed inputs; the amount of any facility expiring within twelve months is answerable from the maturity dates in S4 page:18 (revolver 2030-05-02, term loan 2033-05-05). Third, earnings quality: the Q3 results are the first full quarter with the acquired business, so Q3 2026 is not a run-rate-comparable quarter to any 2025 quarter; the only acquisition-adjusted earnings measure is a management figure with no schedule (S7 page:5 "does not reflect all adjustments that would otherwise be required in connection with the preparation of pro forma financial statements"), so CP-1 and CP-2 must label it as management-attributed and not use it as audited or pro forma. Fourth, contingent items: the earn-out to the seller carries a maximum of USD 125.0 million payable in cash or equity at the Company's option (S4 page:10), and the Fleet sale earn-out receivable of up to USD 65.0 million was carried at nil after a USD 29.2 million fair value write-down in 2025, and its preliminary results show the threshold was not achieved (S4 page:25 "the earn-out performance threshold was not achieved"); both are note disclosures consumers must carry.

## Calculations

No credit metric, ratio, reconciliation or normalization is calculated in this handoff, as the method requires. Coverage counts only:

| Item | Inputs | Result |
| --- | --- | --- |
| Pages in the seven sources | 82 + 28 + 34 + 36 + 10 + 13 + 13 | 216 pages |
| Sources read in full | S4 36 of 36 pages; S7 13 of 13 pages | 2 of 7 sources |
| Sources searched and read at cited pages | S1, S2, S3, S5, S6 | 5 of 7 sources |
| Sources with blocked preparation | None; all 7 converted to text with extractable content | 0 of 7 |

## Gaps

- Credit agreement and first amendment: Not supplied. The pack holds no legal document (context attachment field `legal_documents` is none). The credit agreement of 2025-05-02 appears only as an exhibit list entry (S1 page:81) and the first amendment of 2026-05-05 only in the notes (S4 page:18); the 10-Q exhibit list (S4 page:36) carries only certifications and XBRL files. Missing: covenant levels and step-downs, definitions of Total Net Leverage Ratio and Interest Coverage Ratio, post-amendment margin grid, commitment fee, security package, guarantor names, dividend limit amount, mandatory prepayment terms. Searched for "maximum Total Net", "not exceed", "Interest Coverage" and "guarantor" across all seven sources; only the generic statement at S4 page:19 was found. Affects CP-2 (covenants), CP-1A (structure). Remediation: supply both documents.
- Amortizing notes terms: the notes' interest rate (5.93 percent), installments and final date (2029-02-01) are in S4 page:19, but no indenture or supplemental indenture is supplied; ranking is described only as "senior unsecured amortizing notes".
- Cash paid for interest and income taxes in 2026: Not supplied. Searched "interest paid", "cash paid for interest", "paid for interest", "income taxes paid" and "taxes paid" in all seven sources. Only S1 page:44 has them ("Cash paid for interest $ 26,849 $ 37,076 $ 35,039"), for FY2025, FY2024 and FY2023. The interim supplemental disclosure (S4 page:7) lists only non-cash items. Affects CP-1 and CP-2.
- Q4 2025 discrete quarter: not reported alone in any source. S1 gives FY2025; S4 and S7 give the nine months to 2025-09-30. Any Q4 figure would be derived downstream. The nine-month 2025 comparatives in S4 carry reclassifications (S4 page:8 "Certain reclassifications have been made to the prior year consolidated financial statements"), so a derived Q4 needs a perimeter check.
- Cash flow perimeter in 2025 comparatives: the cash flow statement combines continuing and discontinued operations (S7 page:12 "The cash flows related to discontinued operations and held-for-sale assets and liabilities have not been segregated"); free cash flow comparatives for 2025 therefore include the Fleet business.
- Acquisition-adjusted earnings: the TTM Acquisition Adjusted EBITDA (S7 page:7) includes pre-acquisition earnings with no component schedule; the only pro forma figures in the filing are revenue and net income from continuing operations (S4 page:11), not EBITDA. Not calculable from the pack: pre-acquisition EBITDA of the acquired businesses.
- Purchase accounting: the allocation for PAG, Atech, NorthStar, Aero 3 and the PT6 fuel pump license is preliminary (S4 page:8 to page:15). The Test Logic acquisition on 2026-10-05 is a subsequent event with no price disclosed (S4 page:27).
- Customer concentration after the acquisition: S1 page:11 states a group of affiliated customers was "approximately 20% of the Company" revenue for FY2025; the 2026 interim reports contain no updated concentration disclosure (searched "customer group" and "concentration" in S2, S3, S4).
- Entity identity: guarantors, restricted group and the VSE subsidiary that issued the exchangeable shares are unnamed (see Sources). Hierarchy of claims across the parent and subsidiaries cannot be mapped.
- Ratings, market prices, yield, peer and precedent data: Not supplied (context lists none); outside this pack.
- Call materials: the Q3 release says presentation materials will accompany the 2026-11-05 call (S7 page:8 "accompanying presentation materials will be available"); no presentation or transcript is in the pack, and no slide or chart coverage is claimed. The three releases stand in for presentations.
- Extraction fidelity: all sources are text conversions of HTML. Tables are flattened into lines and footnote markers sit inline; no fidelity review against the original filing or the inline XBRL (listed in S4 page:36) has been done. Consumers should confirm any figure they depend on against the quoted row.
- Dates: the Q3 10-Q is signed on the cutoff date, so nothing in the pack is later than the cutoff; the 2026-11-05 call is an event on the cutoff date and its content is not in the pack. Future dates in the sources (maturities, settlement, earn-out period) are contract terms, not events.
- Currency and period: all figures are USD, in thousands in the statements and in millions in narrative; no foreign-currency reporting basis differs from the context (the foreign currency translation line in S4 page:5 is a small other-comprehensive-income item). Periods match the context: current period Q3 2026, prior period FY2025.

## Next module

CP-1 follows, then CP-1A, CP-2 and CP-5. Each should rely on filed statements first (S4 for the latest balance sheet, debt and liquidity; S1 for FY2025), use the releases only as attributed management measures, state the perimeter break at 2026-05-05, and carry the covenant, guarantor, cash-interest and acquisition-adjusted-earnings gaps above. Any module that needs covenant headroom must write Not supplied and name the credit agreement and first amendment as the missing inputs.
