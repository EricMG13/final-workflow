## Request

Source-readiness review (CP-0) for Victory Capital Holdings, Inc. (ticker VCTR, Delaware registrant, commission file number 001-38388), as of 2026-11-05, pathway credit_snapshot, public case, reporting currency USD, current period Q3 2026 against prior period FY2025. The cutoff is 2026-11-05. The requested downstream consumers are CP-1, CP-1A, CP-2 and CP-5 (minimum module set). The question is whether the supplied source set can support those consumers and what stays blocked. This handoff gives no credit conclusion, does not normalize or reconcile any figure, and asserts SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

Perimeter: the reporting entity is Victory Capital Holdings, Inc. "along with its wholly-owned subsidiaries" (consolidated); there is no separate borrower, parent or guarantor in the context file (borrower, parent and guarantor fields are blank, not zero). Units: filings state USD in thousands except per-share data; the earnings releases and parts of the 10-Q MD&A state USD in millions.

## Sources

### Issuer sources relied on

All seven are filed documents (SEC filings and furnished exhibits) retrieved to the pack. Every page of each was inspected as text; none is an image or a workbook.

| Source (exact name) | sha256 | Document family and original authority | Period and basis | Coverage |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_vctr-20251231.htm.jsonl | f6e853fafdad024596ae018622fdc2c105ae3123da9ff8c0ffc4cc35ba62a4c6 | Annual report on Form 10-K, audited consolidated statements; controls for FY2025 facts | FY ended 2025-12-31, consolidated, USD thousands | 165 of 165 pages |
| 10-Q_2026-03-31_vctr-20260331.htm.jsonl | 51ecb3082ef4b8f61e744997e8179f3f8048703f134354cd3a9232ffa5550840 | Quarterly report on Form 10-Q, unaudited | Q1 2026, consolidated | 37 of 37 pages |
| 10-Q_2026-06-30_vctr-20260630.htm.jsonl | dced821a8cf47e367f9af63545645defedd6eb1c20287807f650044bdd40db14 | Quarterly report on Form 10-Q, unaudited | Q2 2026 and six months 2026 | 46 of 46 pages |
| 10-Q_2026-09-30_vctr-20260930.htm.jsonl | f5b50500d26e0dc2485801a8df14aa064707215b873d8b5442ac072a0ef88f50 | Quarterly report on Form 10-Q, unaudited; latest filing in the pack | Q3 2026 and nine months 2026 | 50 of 50 pages |
| EX-99.1_2026-05-06_vctr-ex99_1.htm.jsonl | ce379672b7f1d4e69ae12e2fdf1e719857d5076de9696a4055a1b0edae6c5455 | Earnings release (Exhibit 99.1), management narrative plus non-GAAP reconciliation; supporting, not controlling | Q1 2026 | 13 of 13 pages |
| EX-99.1_2026-08-05_vctr-ex99_1.htm.jsonl | 981c5f312fef484f40e89934d8e4fda4e7cdfbbdce01c09bbd4ee44b7bfd4c62 | Earnings release (Exhibit 99.1); supporting | Q2 2026 and six months 2026 | 15 of 15 pages |
| EX-99.1_2026-11-04_vctr-ex99_1.htm.jsonl | e1350c6fc75fc57c66528cfff71a5ac81718d36de8c659965d370dbd5d1f67b9 | Earnings release (Exhibit 99.1); supporting | Q3 2026 and nine months 2026 | 17 of 17 pages |

Also supplied and not issuer evidence: the run context (sha256 9e96aec1be60fc30bd3853ebe28d82af5bc222a4621f74e4d59778dfc86b3113), which holds the user's dated settings; a retrieval index file in the pack folder was ignored by CP-OS and is not evidence. The page-one banner of each source quotes a "Visible text" sha256 of the original HTML; that differs from the pinned hash of the extracted file above, and the pinned hash is the one used in this handoff.

### Supplied handoffs

None. CP-0 is the first module; the handoffs list for this request is empty.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents give full text coverage of the annual report, three quarterly reports and three earnings releases. They support the four requested analyses with stated limits, mainly on the pending First Eagle acquisition and its financing. | Medium | The merger agreement, debt commitment letter, credit agreement and First Eagle financials are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt is one term loan under the 2019 Credit Agreement, plus an undrawn revolver, disclosed in the annual and quarterly reports. | Debt and liquidity inputs can be taken from audited and filed statements. | High |
| The First Eagle acquisition was signed after the second quarter and is described only in outline, with no amounts. | Pro forma leverage and the size of new debt cannot be built from this pack. | High |
| The covenant is described in words only, with no reported ratio or definition. | Covenant headroom cannot be computed from these sources. | High |
| Earnings releases give adjusted measures that the quarterly reports reconcile. | Adjusted figures are usable as attributed management measures, not as audited facts. | Medium |

### Readiness view

The source set is READY_WITH_LIMITATIONS for each of CP-1, CP-1A, CP-2 and CP-5. Filed statements cover the current period (Q3 2026 and nine months 2026), the prior-period comparison (FY2025 audited, plus Q3 2025 and nine months 2025 comparatives in the Q3 report), and the debt note. The strongest contrary evidence is the pending First Eagle transaction: it is the largest forward credit event in the pack, yet its financing terms sit in documents that are listed in an exhibit index but not supplied, so any pro forma capital structure is blocked. No consumer is CONDITIONAL or BLOCKED, because each owner can perform its own method on the retained filings with the gaps carried forward. Status is source sufficiency only; it does not say downstream analysis is complete or accepted.

### Per-source assessment

#### Annual report (10-K, FY2025)

The cover page identifies the registrant and period: [10-K page:1] "For the fiscal year ended December 31, 2025". The debt note (Note 11) is on page:141 to page:143 and the single reportable segment disclosure is in Note 19. The 10-K gives the covenant wording and the year-end term loan at the pre-amendment margin: [10-K page:142] "SOFR plus a margin of 2.00% or an alternate base rate plus a margin of 1.00%". This margin was later lowered (see conflicts). The 10-K governs FY2025 facts; where a quarterly report restates a December 2025 balance, the 10-K is the original authority.

#### Quarterly reports (10-Q, Q1, Q2 and Q3 2026)

Each is a separate, active source; none supersedes another. The Q3 report states a prior-period revision: [Q3-10Q page:9] "Certain prior period amounts have been revised to conform to the current period presentation." That sentence says the revision had no effect on previously reported results, but the revised line items are not identified, so a prior-period comparison must read the Q3 comparatives rather than an earlier report where they differ. The Q3 report was filed on the cutoff date itself (retrieval index filing date 2026-11-05) and is inside the cutoff; its own cover states shares outstanding "as of October 30, 2026".

#### Earnings releases (Exhibit 99.1, Q1, Q2 and Q3 2026)

These are management presentations of reported and adjusted results and give attributed supporting claims only. The Q3 release states: [R3 page:4] "The total debt outstanding as of September 30, 2026 was approximately $975 million." and its non-GAAP measures are reconciled to GAAP in the Q3 10-Q: [Q3-10Q page:42] "Adjusted EBITDA$212,135$190,451$658,872$485,375". No guidance table was located in any release (the word "outlook" appears only in forward-looking-statement boilerplate). Release headlines use "Record" language (management characterisation, not adopted).

### Entity, perimeter and instrument roles

- Issuer and sole borrower named in the filings: Victory Capital Holdings, Inc. The 10-K exhibit index describes the original credit agreement with the Company "as borrower". Subsidiary guarantors are not enumerated in the supplied text: the filings say "the other loan parties party thereto" without naming them. Whether any restricted or unrestricted subsidiary distinction exists is Not supplied.
- Debt instrument: term loan and revolver under the 2019 Credit Agreement. [Q3-10Q page:20] "Due September 2032$975,150" under the heading "Term Loans". The revolver is undrawn: [Q3-10Q page:44] "which had approximately $100.0 million undrawn as of September 30, 2026".
- Amendment history is in the filings only as narrative: Fifth Amendment (2024), Sixth Amendment (2025-09-23) and Seventh Amendment (2026-05-18). The amendment documents themselves are not supplied.
- Regulated subsidiary constraint: [Q3-10Q page:45] "such subsidiaries of our Company may be restricted in their ability to transfer cash to their parents." This bears on how much consolidated cash is available at the parent; the split of cash by entity is Not supplied.
- Equity-linked holder: Amundi received common and preferred shares in the April 2025 acquisition [Q3-10Q page:11] "represented in the aggregate 26.1% of the Company’s fully diluted shares". Preferred stock is outside debt but within the capital structure the consumers must keep distinct.

### Version relationships and conflicts

1. Term loan margin. The 10-K and Q1 10-Q give SOFR plus 2.00%; the Q2 and Q3 10-Q give SOFR plus 1.75% after the Seventh Amendment: [Q2-10Q page:18] "SOFR plus a margin of 1.75% or an alternate base rate plus a margin of 0.75%". This is a dated change, not a conflict; consumers must use the Q3 terms for current pricing and the 10-K for FY2025 expense.
2. Stale amendment text inside the Q3 report. The Q3 MD&A (page:44) still introduces the term loan as "(the “Existing Term Loans”)" at "$985.0 million" maturing September 2032, while Note 10 (page:20) shows the Repriced Term Loans at a September 2032 balance of "$975,150" thousand. Note 10 is the controlling statement of the carrying amount; the MD&A description is a presentation lag, not a second instrument. Downstream use should cite Note 10 for the balance.
3. Unit error in the Q1 MD&A. [Q1-10Q page:32] "aggregate principal amount of $985.0 billion" conflicts with the same figure in millions in the Q2 and Q3 reports and in the 10-K. Treat as a typographical error; the Q1 balance sheet and Note 10 control. Downstream effect: any extraction from that sentence must be rejected.
4. Long-term debt line. The balance sheet carries long-term debt net of unamortized costs and discount (the Long-term debt, net line at September 30, 2026 on page:5 of the Q3 10-Q), while the release states approximately $975 million of debt. These are net versus gross principal measures, not a conflict, but CP-1 must state which basis it uses.
5. Description of the First Eagle transaction differs in completeness across documents: the Q3 10-Q (pages:12 to 13) and Q3 release (page:2) state the outline; the Q2 documents pre-date it (agreement dated 2026-08-25, after the Q2 release of 2026-08-05) and the Q2 10-Q was filed on 2026-08-06 per the retrieval index. The Q2 sources therefore do not contain it and must not be read as saying the transaction did not exist at their own dates of reporting.

### Coverage of source profiles

- Financial statements and notes: balance sheet, operations, comprehensive income, equity, cash flows, debt, segment (one reportable segment), subsequent events and non-GAAP reconciliation are present in the Q3 report and the 10-K. The Q3 supplemental cash flow data gives cash paid for interest and for income taxes (nine months 2026 and 2025). Discrete quarters can be obtained for Q1, Q2 and Q3 2026 from the three quarterly reports; Q4 2025 as a discrete quarter is Not supplied as a source (it would be a derived annual-less-nine-months figure and no Q4 2025 release is in the pack).
- Segment and KPI: AUM, flows, revenue realization and investment performance are given in the releases and the Q3 10-Q MD&A. Segment profit tables are not applicable because one reportable segment is reported. Revenue by franchise is not separated except for Pioneer Investments: [Q3-10Q page:12] "Net income attributable to Pioneer Investments for the three and nine months ended September 30, 2026 is impractical to determine".
- Debt and facility level: one term loan tranche and one revolver; facility-level carrying value, rates, maturity and amortization (1% a year in the 10-K, [10-K page:143] "amortize at 1% per annum") are present. Letters of credit: the revolver has a sublimit, and the liquidity table shows the full commitment undrawn, so no letters of credit are shown as using it.
- Covenants: one financial maintenance covenant in words: [Q3-10Q page:20] "of no greater than 4.00 to 1.00". The wording makes it a test that applies only when revolver borrowings exceed 35.0% of commitments; the reported first lien leverage ratio and the definition of covenant EBITDA are Not supplied.
- Liquidity: the Q3 10-Q MD&A (page:43) gives a liquidity table with cash, receivables and undrawn commitment. Cash taxes and interest paid are in the cash flow statement.
- Presentations and decks: none in the pack; releases substitute for quarterly presentations. No image or chart content was relied on, and none is claimed as inspected.
- Workbooks and legal documents: none supplied (context legal_documents is none).

### Readiness by consumer

| Consumer | Status | Evidence located | Limitations carried forward |
| --- | --- | --- | --- |
| CP-1 (financial data extraction and metrics) | READY_WITH_LIMITATIONS | Three statements, notes, debt table, cash paid for interest and taxes, adjusted EBITDA reconciliation, discrete Q1, Q2 and Q3 2026 and FY2025 | Q4 2025 discrete quarter not supplied; covenant ratio and definition not supplied; Q1 unit typo; MD&A debt text lags Note 10; pro forma First Eagle figures not available |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description in the 10-K, Amundi US acquisition notes, First Eagle outline in Q3 note 3, Item 1 legal proceedings, subsequent events | Merger agreement, debt commitment letter, proxy statement and First Eagle financials not supplied; consideration split and cash amount not located; ownership detail beyond the Amundi stake limited |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Inherits CP-1 and CP-1A evidence | Cannot size post-transaction leverage or liquidity; no ratings or market data supplied |
| CP-5 (evidence trace validator) | READY_WITH_LIMITATIONS | Full text of all seven sources permits quote matching | Carries every limitation above; releases are management claims and must not override filings |

No consumer is conditional or blocked, so none is marked DO NOT RUN.

### Subsequent events and dated items

Inside the cutoff: the First Eagle agreement dated August 25, 2026 and the related proxy filings ([Q3-10Q page:47] "On October 2, 2026, Victory filed with the Securities and Exchange Commission (the “SEC”) a preliminary proxy statement") and stockholder litigation ([Q3-10Q page:48] "Wright v. Victory Capital Holdings, Inc., et al., Index No. 656101/2026"); the dividend approved on November 4, 2026 ([Q3-10Q page:25] "payable on December 23, 2026"). The expected close is a forward-looking term: [Q3-10Q page:13] "expected to close by the end of the first quarter of 2027". It is a contract expectation, not a fact that has occurred. Nothing in the pack is dated after 2026-11-05.

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. The page and source coverage counts are taken directly from the pack: the seven sources hold 165, 37, 46, 50, 13, 15 and 17 pages, and every page of each was inspected as text. No derived financial amount is stated in this handoff; every dollar figure above is quoted from a source at the locator given.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Agreement and Plan of Merger dated 2026-08-25 listed as Exhibit 2.1 in the Q3 10-Q exhibit index but not in the pack | High | CP-1A, CP-2, CP-5 | Add the Exhibit 2.1 text to the pack |
| Debt commitment letter for the cash portion of First Eagle consideration: referred to in Q3 note 3 (pages:12 to 13) with no amount, lenders, terms or pricing | High | CP-1, CP-2 | Obtain the commitment letter or the filing that describes it (current report or proxy statement) |
| Definitive proxy statement filed October 16, 2026 (referred to in Q3 10-Q Part II Item 1), not supplied; likely holds pro forma and consideration details | High | CP-1A, CP-2 | Add the proxy statement |
| First Eagle standalone financials, AUM and cash flow: Not supplied | High | CP-2 | Add the proxy statement or First Eagle financial statements |
| Credit agreement and the Fifth, Sixth and Seventh Amendments: not supplied; guarantors, collateral, security and covenant definitions unconfirmed | Medium | CP-1, CP-2 | Add the executed agreement and amendments |
| Reported first lien leverage ratio and covenant EBITDA definition: Not supplied | Medium | CP-1, CP-2 | Obtain compliance certificate data or the credit agreement |
| Q4 2025 discrete quarter: no source for the quarter alone | Low | CP-1 | Accept a derived annual-less-nine-months figure only if flagged as derived, or add the Q4 2025 release |
| Credit ratings, bond or loan price quotes, market capitalisation inputs: none supplied (context ratings and quotes are empty) | Medium | CP-2 | Supply ratings and quotes if a market view is required |
| Revised prior-period line items in Q3 report not identified | Low | CP-1 | Reconcile Q3 comparatives to the 10-K when extracting prior-period figures |
| Cash by legal entity, including the regulated broker-dealer: Not supplied | Low | CP-1, CP-2 | Note as a limitation on parent-level liquidity |
| Fidelity: extraction from HTML to text is complete in page count but table cell layout was flattened in places (numbers and signs split across lines); a successful extraction is not a fidelity review | Low | CP-1, CP-5 | Verify each extracted figure against the quoted locator before use |

## Next module

CP-1 (financial data and metrics) runs next, then CP-1A, CP-2 and CP-5 in dependency order. CP-1 should take FY2025 from the 10-K and Q1, Q2 and Q3 2026 and nine months from the quarterly reports; cite Note 10 for the term loan balance; label cash interest and cash taxes by period; treat release figures as attributed management measures; keep gross principal and net carrying value distinct; flag that covenant headroom and pro forma First Eagle leverage are Not calculable from this pack. CP-1A should carry the First Eagle gaps into the transaction summary, and CP-5 should check every claim against the cited page, rejecting extractions from the Q1 unit-error sentence.
