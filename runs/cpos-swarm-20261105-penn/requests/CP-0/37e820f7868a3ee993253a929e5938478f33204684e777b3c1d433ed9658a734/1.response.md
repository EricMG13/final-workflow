## Request

Issuer: PENN Entertainment, Inc. (ticker PENN, Pennsylvania corporation, Commission file number 0-24206). As-of date and cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD; figures are in USD millions unless stated. Current period q3-2026 (quarter and nine months ended 2026-09-30); prior period fy-2025 (year ended 2025-12-31). Requested downstream modules: CP-1, CP-1A, CP-2, CP-5.

Question this handoff answers: can the supplied source set support the requested work, and what remains blocked? It gives no credit conclusion, legal interpretation or investment opinion. Source sufficiency is kept separate from completion of downstream analysis. The context file (sha256 de76f6d737b4f874d55cfe4efb68426523509ccefb05817de5c048370ec1b054) holds run settings, not issuer evidence. It leaves ratings, quotes, deal terms, valuation inputs, assumptions and research questions blank. Those blanks are not zero and are carried as gaps.

## Sources

### Issuer sources relied on

All seven are text extractions (JSONL, one record per `page:N` chunk). The sha256 is that of the supplied extraction file. Each extraction also prints its own inner "Visible text of ..." hash on `page:1`; the two differ and the file hash is the identifier used here.

| Source name | sha256 | Family and authority | Period and basis | Pages |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_penn-20251231.htm.jsonl | e6f090720b62a51573341a18254da71e5663d9a3ca11809ee32b87032414e4c4 | Annual report, filed audited statements (auditor opinion at page:101); controls filed facts | Year ended 2025-12-31, consolidated PENN Entertainment, Inc. | 200 |
| 10-Q_2026-03-31_penn-20260331.htm.jsonl | f74720e254c5d598fec44396bf0d01f4b1fcb35191eafe54dbae1433241cfe17 | Quarterly report, unaudited filed statements | Quarter ended 2026-03-31 | 68 |
| 10-Q_2026-06-30_penn-20260630.htm.jsonl | e4a4a68372f7e9e6e78807b6eaf280e8a90a9eb8c02165e49ee603cc73e74ba7 | Quarterly report, unaudited filed statements | Quarter and six months ended 2026-06-30 | 82 |
| 10-Q_2026-09-30_penn-20260930.htm.jsonl | 289bd66b2b3ba7c0442b90807e0166affa057570b7680ca91b89ac74aa566568 | Quarterly report, unaudited filed statements; latest filed statements | Three and nine months ended 2026-09-30 | 81 |
| EX-99.1_2026-04-23_pennex991-q12026.htm.jsonl | bd58a1d530bb3cf8b4081bd3c78bc172ec144332ab675d2b2c776af0b2ffd599 | Earnings release; management narrative and non-GAAP, supporting claims only | Quarter ended 2026-03-31, dated 2026-04-23 | 13 |
| EX-99.1_2026-08-06_pennex991-q22026.htm.jsonl | 29f1d9698d7fe07b2e827f80ed415692eef3a01380a671b91317aa4e3711e167 | Earnings release; management narrative and non-GAAP, supporting claims only | Quarter ended 2026-06-30, dated 2026-08-06 | 15 |
| EX-99.1_2026-11-05_pennex991-q32026.htm.jsonl | 9cd3b27bc143946725e283ad70f7a65c0842d014c7b12f2cd6670b5aee829c8c | Earnings release; management narrative and non-GAAP, supporting claims only; dated on the cutoff day | Three and nine months ended 2026-09-30, dated 2026-11-05 | 15 |

### Supplied handoffs

None. CP-0 is the first module; the run supplies no upstream handoff to it (`handoffs` is empty in the request).

### Not in the pack and not used

`_retrieval.json` is ignored by the run and is not evidence. No outside knowledge of the company is used.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied PENN filings and releases support financial extraction, business and transaction context, and later synthesis and review, with bounded limits. Debt, liquidity, segments and covenants are printed with locators. | Medium | Executed credit agreement, indentures and master leases are not supplied, so covenant definitions and headroom cannot be tested; text extraction only. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt by instrument, maturities, letters of credit and revolver availability are printed in the latest quarterly filing. | Facility-level debt and liquidity can be extracted from a filed source. | High |
| Covenant levels are printed but the reported covenant ratios are not; only a compliance statement is given. | Headroom to the leverage and coverage tests cannot be measured from these sources. | High |
| Lease obligations to the real estate landlords are large and are described in filings, but the executed lease documents are not supplied. | Lease terms, cross-default and cure mechanics rest on filing summaries only. | Medium |
| Earnings releases state management measures that differ in definition from the filed statements and from the covenant ratios. | Management leverage figures cannot stand in for covenant tests. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for the requested credit snapshot. The three quarterly filings and the audited annual report are filed statements for the same consolidated issuer, PENN Entertainment, Inc., and carry period labels, a debt note, a lease note, a segment note, supplemental cash-flow disclosure and a liquidity discussion. The releases add reconciliations and management narrative and are treated as attributed supporting claims. They never override a filing. No source is blocked, no identity boundary is unresolved, and no critical document is absent for a filing-based snapshot. The limits below are bounded and are carried to each consumer. Source sufficiency is asserted only (SOURCE_SUFFICIENCY_ONLY). No normalized quarters, reconciliation or downstream input acceptance is asserted here.

### Source-by-source assessment

| Source | Evidence located | Limitation carried forward |
| --- | --- | --- |
| 10-K FY2025 | Cover: "For the fiscal year ended December 31, 2025" (page:1). Item 8 (page:100), auditor opinion (page:101), critical audit matter on the Interactive reporting unit goodwill test (page:103). Debt note 10 with year-end 2025 table and repayment schedule (page:137). Covenants and compliance statement (page:90). Cash paid for interest in the cash-flow supplement (page:109). Exhibit index listing legal documents by reference (page:197). | Executed agreements are listed in the index, not supplied. |
| 10-Q Q1 2026 | Cover "quarterly period ended March 31, 2026" (page:1). Balance sheet with cash (page:2). Revolver availability and letters of credit (page:16). 6.75% notes issuance (page:16). | Unaudited; superseded for point-in-time balances by later quarters but needed for the quarter series. |
| 10-Q Q2 2026 | Cover "quarterly period ended June 30, 2026" (page:1). Balance sheet with cash (page:2). Third Amendment Agreement (page:18). Covenant compliance statement (page:21). | Unaudited. Six-month and quarter columns must stay separate. |
| 10-Q Q3 2026 | Balance sheet, operations, cash flows (pages 2-6). Note 4 revenue by segment (page:15). Note 5 debt table and repayment schedule (pages 15-16). Credit facility terms, covenants, letters of credit (pages 17-18). Note 6 leases (pages 20-22). Note 13 segments with Segment Adjusted EBITDAR and reconciliation to net income (pages 37-40). MD&A liquidity and cash flow (pages 69-70). | Unaudited; nine-month cash flow is year to date, with no discrete third-quarter cash-flow statement in the filing. |
| Release Q1 2026 | Retail highlights, total liquidity and traditional net debt, leverage table (pages 1-6). | Management measures, non-GAAP. Dated 2026-04-23. |
| Release Q2 2026 | Total liquidity, traditional net debt, leverage table (pages 3-8). | Management measures, non-GAAP. Dated 2026-08-06. |
| Release Q3 2026 | Segment table, reconciliation of net income to Consolidated Adjusted EBITDA, selected financial information and ratios, cash flow data, non-GAAP definitions (pages 3-12). | Management measures, non-GAAP. Dated the cutoff day, so it is the last permitted evidence date. |

### Entity, perimeter and instrument roles

The issuer and filer is PENN Entertainment, Inc.; the statements are consolidated ("PENN Entertainment, Inc. and its subsidiaries", 10-Q Q3 page:7). The senior notes are issued by the Company. The 10-Q Q3 states the 6.75% Notes are "not guaranteed by any of the Company’s subsidiaries except in the event that the Company, in the future, issues certain subsidiary-guaranteed debt securities" (page:18); the same wording is given for the 5.625% Notes. The 10-K states that gaming and related assets "collateralize our obligations under our Amended Credit Facilities" (page:64), and the index lists "guarantors party thereto" for the credit agreement (10-K page:197). The identity of those guarantors and the restricted perimeter is therefore not located in the supplied text and is carried as a gap. The real estate landlords are Gaming and Leisure Properties, Inc. (GLPI) and VICI Properties Inc. (VICI), who are counterparties and not issuers or guarantors. The AR PENN Master Lease and the 2023 Master Lease are "cross-defaulted, cross-collateralized, and coterminous, and subject to a parent guarantee" (10-Q Q3 page:21). No parent, sponsor or borrower distinct from the issuer is named in the context or sources.

### Version relationships and conflicts

The three quarterly filings and the annual report are sequential periods of the same issuer, not duplicates; each stays an active source. The facility structure changed during the run period: the Third Amendment of 2026-04-16 refinanced the revolver and Term Loan A to April 2031, and the Fourth Amendment of 2026-05-28 extended the Term Loan B to May 2033 (10-Q Q3 pages 17-18). The year-end 2025 debt table (revolver due 2027, Term Loan A due 2027, Term Loan B due 2029; 10-K page:137) therefore describes an earlier facility version and cannot be mixed with the 2026-09-30 table without labelling.

No conflict between a release and a filing was found in the items checked. Two figures that look alike are different measures. Cash paid for interest is 291.6 for the nine months in the cash-flow statement ("Cash paid for interest, net of amounts capitalized", 10-Q Q3 page:6). The release gives 100.9 for the same nine months as "Cash paid for interest on traditional debt" (release Q3 page:8). The release describes the narrower measure. A downstream user must not treat the two as the same quantity. Likewise the Q3 segment total of Segment Adjusted EBITDAR (483.5, 10-Q Q3 page:38) differs from the retail-only figure of 501.8 in the release (page:1) because the Interactive loss of 18.3 is netted in the first.

### Consumer assessments

| Consumer | Status | Evidence demand and basis | Limitations carried |
| --- | --- | --- | --- |
| CP-1 financial data extraction | READY_WITH_LIMITATIONS | Statements, discrete and year-to-date periods, facility-level debt with carrying and principal amounts, segment revenue and Segment Adjusted EBITDAR, add-backs in the release reconciliation, cash paid for interest and taxes, and lease balances are all located in the filings. | Covenant ratio values are not printed. A discrete third-quarter cash-flow statement is not in the filing. Lease cash rent comes from release or MD&A text only. Management measures are not covenant measures. |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business description and segment grid (10-Q Q3 pages 7-8, 10-K pages 6 onward), master lease structure, the 2026 refinancing events, the ESPN Sportsbook Agreement termination (10-Q Q3 page:12), the HG Vora cooperation agreement costs (10-Q Q3 pages 44 and 58), and post-period items are in the filings. No dedicated subsequent-events note was located in the Q3 10-Q on search. | Executed lease, credit and indenture documents are not supplied. Ownership detail beyond share counts is not supplied. |
| CP-2 fundamental synthesis | READY_WITH_LIMITATIONS | Consumes upstream registers only. Source sufficiency for its inputs is the same as for CP-1 and CP-1A. | Inherits every gap below. Its dependence on upstream handoffs is sequencing, not a source condition. |
| CP-5 evidence trace review | READY_WITH_LIMITATIONS | Cited quotes can be matched to the retained page chunks of seven sources. | Review of a locator is a check against extracted text, not against the rendered filing. Charts and images are not covered. |

## Calculations

No analytical metric is derived in this module. The checks below only tie printed totals to their printed components, to show the extraction is internally consistent. Units are USD millions. They are not a credit calculation and do not normalize or reconcile any figure.

| Check | Inputs (locator) | Result |
| --- | --- | --- |
| Debt at 2026-09-30 | 441.3 + 957.5 + 400.0 + 400.0 + 600.0 + 7.8 (10-Q Q3 pages 15-16) | 2,806.6, equal to the printed "2,806.6" |
| Debt at 2025-12-31 | 570.0 + 453.8 + 965.0 + 400.0 + 400.0 + 106.7 + 8.6 (10-Q Q3 pages 15-16; 10-K page:137) | 2,904.1, equal to the printed "2,904.1" |
| Repayment schedule at 2026-09-30 | 8.1 + 433.1 + 33.1 + 433.2 + 33.2 + 1,865.9 (10-Q Q3 page:16) | 2,806.6, equal to the printed total minimum payments |
| Revolver availability at 2026-09-30 | 1,000.0 revolver less 23.9 letters of credit (10-Q Q3 pages 17-18; the 1.0 billion size is stated as "$1.0 billion Amended Revolving Credit Facility") | 976.1, equal to the printed "$976.1 million" |
| Three-month revenue by segment, Q3 2026 | 708.3 + 291.8 + 147.5 + 341.9 + 348.4 + 4.0 - 1.9 (10-Q Q3 page:15) | 1,840.0, equal to printed total revenues |
| Segment Adjusted EBITDAR to Consolidated Adjusted EBITDA, Q3 2026 | 208.1 + 108.3 + 50.9 + 134.5 - 18.3 = 483.5; less other category 31.6; less rent expense on triple net operating leases 167.9 (10-Q Q3 page:38; release Q3 pages 3-4) | 284.0, equal to the printed Consolidated Adjusted EBITDA |
| Nine-month version of the same bridge | 622.8 + 321.5 + 159.9 + 386.2 - 38.7 - 94.9 - 494.4 (release Q3 pages 3-4) | 862.4, equal to the printed total |
| Traditional net debt, 2026-09-30 | 2,806.6 less cash 1,044.8 (release Q3 page:7) | 1,761.8, equal to the printed figure |
| Total liquidity as the release describes it | cash 1,044.8 plus revolver availability 976.1 (10-Q Q3 pages 2 and 18) | 2,020.9, consistent with the release statement "Total liquidity as of September 30, 2026 was $2.0 billion" (page:2) |

Release ratios checked against their stated definitions (release Q3 pages 7, 11, 12). Lease-adjusted net leverage: (7,940.0 + 1,761.8) / (1,088.2 + 656.2) = 9,701.8 / 1,744.4, which rounds to 5.6x, the printed figure. Traditional net leverage: 1,761.8 / (1,088.2 + 656.2 - 992.5) = 1,761.8 / 751.9, which rounds to 2.3x, the printed figure, where 992.5 is 7,940.0 divided by 8, the trailing cash rent to REIT landlords. These ties confirm the extraction only. They are management definitions and are not the covenant ratio in the Second Amended and Restated Credit Agreement.

Not calculable in this module: covenant total net leverage and interest coverage, because the covenant definitions are in the credit agreement, which is not supplied, and no reported covenant ratio value was found.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed Second Amended and Restated Credit Agreement and its amendments (including the Third Amendment of 2026-04-16 and the Fourth Amendment of 2026-05-28) are not supplied. The filings describe the covenants as "as defined within the Second Amended and Restated Credit Agreement". The covenant levels printed are a maximum total net leverage ratio of 4.50 to 1.00 with a step up to 5.00 to 1.00 for certain significant acquisitions, and a minimum interest coverage ratio of 2.00 to 1.00 (10-Q Q3 page:17). | Moderate | CP-1, CP-2, CP-5 | Obtain the agreement and amendments and the compliance certificate. |
| Reported covenant ratio values are not printed. A search of the Q3 10-Q and the 10-K for "interest coverage" and "net leverage ratio" found only the covenant levels and the statement "the Company was in compliance with all required financial covenants" (10-Q Q3 page:20). Headroom is Not supplied. | Moderate | CP-1, CP-2 | Obtain the compliance certificate or compute under the agreement definitions. |
| Indentures for the 5.625% Notes due 2027, 4.125% Notes due 2029 and 6.75% Notes due 2031 are not supplied; the filings summarize redemption terms and no subsidiary guarantees. | Low to moderate | CP-1, CP-1A | Obtain the indentures if covenant or ranking detail is needed. |
| Master leases (AR PENN, 2023, Pinnacle, VICI, Morgantown) and the Master Development Agreement are described in Note 6 and the 10-K but not supplied. Cross-default, cure and parent guarantee terms rest on filing summaries. | Moderate | CP-1A, CP-2 | Obtain the executed leases. |
| Guarantor identity and the restricted-group perimeter of the credit facilities are not located in the supplied text. | Moderate | CP-1, CP-2 | Obtain the credit agreement and guarantor schedule. |
| The management presentation is referenced in release Q3 page:12 but not supplied, so no slide-level evidence exists. The releases serve instead. No claim of slide or chart inspection is made. | Low | CP-1A | Obtain the presentation if narrative slides are needed. |
| Extraction is text only. Tables are flattened and images, charts and exhibits are not inspected; a successful extraction is not a fidelity review. | Low | all | Spot check the rendered filings for any figure that will drive a conclusion. |
| Guidance figures: the releases refer to "the guidance" and to a "full-year Adjusted EBITDA target in our Interactive segment" (release Q3 pages 1 and 13) but a search of the three releases found no guidance amount. Guidance is Not supplied. | Low | CP-1A, CP-2 | Obtain the guidance slides or the earlier outlook release. |
| Ratings, market prices, peer data, deal terms and research questions are blank in the context. Blank is not zero. | Low for a filing-based snapshot | CP-2 | Supply if relative value or rating context is wanted. |
| A discrete third-quarter cash-flow statement is not in the 10-Q, which gives nine months (10-Q Q3 page:6). The release gives some discrete third-quarter cash items (page:8). | Low | CP-1 | Derive only with labelled year-to-date differences, or use the release items. |
| Non-GAAP and management measures (Consolidated Adjusted EBITDA, traditional net debt, lease-adjusted leverage, cash paid for interest on traditional debt) are not the covenant or GAAP measures. | Low | CP-1, CP-2 | Label every use. |
| Facility terms changed during 2026, so the 10-K debt table is a prior facility version. | Low | CP-1 | Use the 2026-09-30 table for current structure and the 10-K only as the prior period. |
| The 5.625% Notes due 2027 are classified as long-term although "scheduled to mature within the next twelve months", based on "intent and ability to refinance on a long-term basis" (10-Q Q3 pages 18-19). This is a classification matter for the liquidity consumer, not a source gap. | Note | CP-1, CP-2 | Carry the statement in the liquidity analysis. |

No document is dated after the 2026-11-05 cutoff. The latest evidence is the release and the Q3 10-Q, both on the cutoff date. Events after 2026-09-30 in the Q3 10-Q (for example the 2026-10-15 notice to redeem exchangeable shares on or about 2026-12-15, page:31) are subsequent events and are labelled as such. A future date such as the 2027 maturity of the 5.625% Notes is a contract term, not a fact after the cutoff.

## Next module

Proceed to CP-1 (financial data) on the 10-Q Q3 filing and the 10-K as primary sources, with the releases as supporting claims. Carry forward: the facility version change, the distinction between management and covenant measures, the cash-paid-for-interest definition difference, the absence of covenant ratio values and guarantor detail, and year-to-date versus discrete period labels. CP-1A, CP-2 and CP-5 follow in the run order. Next evidence action for the owner: obtain the credit agreement with compliance certificate, the indentures and the executed master leases.
