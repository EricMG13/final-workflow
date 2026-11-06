# CP-0 — Source readiness: DAVITA INC. (dva)

## Request

- Issuer: DAVITA INC. (issuer id `dva`, ticker DVA), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025 (context).
- Run: `dva-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned page text of each source and wrote this answer. No provider was called.
- Question: can the supplied public filings and earnings releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles or calculates no figure.
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers. Quotes are exact substrings of that page text. Tags used below: [10-K] annual report, [Q1 10-Q], [Q2 10-Q], [Q3 10-Q] quarterly reports, [Q1 ER], [Q2 ER], [Q3 ER] earnings releases.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_dva-20251231.htm.jsonl | e8c363b79225d32d92e8856c1234363883b84595e0f356cf12128301c572a94b | [10-K] Annual report on Form 10-K for the fiscal year ended December 31, 2025 (218 pages) |
| 10-Q_2026-03-31_dva-20260331.htm.jsonl | 7063ac673c62a3a12d361c8ab9f216c83e6406eb95937f85ad2f6c47a221fe01 | [Q1 10-Q] Quarterly report on Form 10-Q for the quarter ended March 31, 2026 (46 pages) |
| 10-Q_2026-06-30_dva-20260630.htm.jsonl | 5aed5931f3b50f8efc4d5398264cb7a317623aeb269a49968c33246ed0273365 | [Q2 10-Q] Quarterly report on Form 10-Q for the quarter ended June 30, 2026 (48 pages) |
| 10-Q_2026-09-30_dva-20260930.htm.jsonl | 99b4bb0c8f87c03db2290c95cfd812d4622509e8fdbcdce46d84afcedef79236 | [Q3 10-Q] Quarterly report on Form 10-Q for the quarter ended September 30, 2026 (53 pages) |
| EX-99.1_2026-05-05_dva33126ex991.htm.jsonl | c5727d9383becddd69bf1cd80efadc8ee72012f8313405a8b1414b2f74143fa7 | [Q1 ER] Exhibit 99.1 earnings release for the first quarter of 2026 (20 pages) |
| EX-99.1_2026-08-04_dva63026ex991.htm.jsonl | e55a9fe053fe9f69274156863d81212ffe989a931913bc64dfc65b70fd8151a2 | [Q2 ER] Exhibit 99.1 earnings release for the second quarter of 2026 (19 pages) |
| EX-99.1_2026-10-29_dva93026ex991.htm.jsonl | b062a4dfa0aa9b3cce4ee385c1a8aad8546180810a3acbc585a968f93eadfc64 | [Q3 ER] Exhibit 99.1 earnings release for the third quarter of 2026 (20 pages) |
| context | 888318ae2603a71d9f443112e6d0298861b2ea95d8c8a8118da68f80c88bfe70 | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists.

The pack also holds `_retrieval.json`, which the launcher ignores. It is not a source here.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The annual report, three quarterly reports and three earnings releases are enough to run all four selected modules on the consolidated company, each with stated limits. Nothing blocks the work. | Medium | No credit agreement, indenture, guarantor list, rating report or filing after the third-quarter report is supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual and quarterly reports give audited and unaudited statements, a debt table, maturities and liquidity text with page locators. | Debt, liquidity and maturity work can be traced to filed statements. | Medium |
| The leverage covenant is summarized only in the annual report, and the reported leverage ratio appears only in the earnings releases; the credit agreement itself is not supplied. | Headroom rests on management-computed figures that cannot be checked against the governing definitions. | Low |
| Interest rate caps, an amended credit agreement, a Berkshire repurchase obligation and puttable noncontrolling interests sit beside the debt table. | These claims need separate treatment from reported debt. | Medium |
| The latest evidence is dated October 29, 2026, and nothing between that date and the cutoff is supplied. | Events in the last week before the cutoff are unknown, not absent. | Medium |

### Readiness view

Every selected consumer can proceed on the supplied filings, with bounded limitations; none is conditional or blocked. The 10-K and the three 10-Qs are original authority for statements, notes and the debt table, and the three earnings releases are management-prepared support that also carry issuer non-GAAP figures. The recurring limits are that the governing credit agreement, the indentures and the subsidiary guarantor list are not supplied, that no rating or market data is supplied, and that nothing dated after October 29, 2026 is supplied.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 statements ([10-K] page:153 to page:155) and unaudited statements for three interim periods of 2026 are located, with comparatives, together with segment notes, a long-term debt note and cash-flow statements. Limits: statements are in thousands while releases mix millions and thousands; the Q1 10-Q debt note prints no maturity schedule. |
| CP-1A | READY_WITH_LIMITATIONS | Business description ([10-K] page:4), segments ([10-K] page:211), center and patient counts ([Q3 ER] page:3), integrated kidney care, the Berkshire repurchase agreement and the Elara Caring minority investment are located. Limit: the subsidiary list (Exhibit 21.1), the Berkshire agreement and the Elara Caring agreement are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Debt table, maturities, guarantees and security, covenant summary, revolver availability, letters of credit, interest rate caps and the issuer-computed leverage ratio are located. Limit: no executed credit agreement or indenture, so covenant definitions and the Consolidated EBITDA add-backs cannot be verified. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable page locators, so claims can be traced. Limit: the text extraction was not compared with the filed HTML or XBRL, and no image or chart was inspected. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_dva-20251231.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited statements and notes. [10-K] page:1 "For the Fiscal Year Ended December 31, 2025" and "Commission File Number: 1-14106".
- Audit: [10-K] page:148 "In our opinion, the consolidated financial statements present fairly, in all material respects, the financial position of the Company as of December 31, 2025 and 2024". Auditor report date: [10-K] page:153 "/s/ KPMG LLP Seattle, Washington February 11, 2026". Signature date: [10-K] page:218 "February 11, 2026".
- Statements located: income statement and per-share data ([10-K] page:153 to page:154), balance sheet ([10-K] page:154), cash flows ([10-K] page:155). Units: [10-K] page:154 "DAVITA INC. CONSOLIDATED BALANCE SHEETS (dollars and shares in thousands, except per share data)". USD.
- Debt note: [10-K] page:178 "12. Long-term debt Long-term debt comprised the following"; maturities at [10-K] page:180; credit agreement terms, security and covenant summary at [10-K] page:183; senior notes at [10-K] page:184.
- Liquidity and obligations: [10-K] page:132 "Available liquidity" text; contractual obligations table at [10-K] page:135, including operating leases and puts. Segment note: [10-K] page:211 "24. Segment reporting".
- Perimeter: consolidated DaVita Inc. and subsidiaries. [10-K] page:4 "other similar terms refer to DaVita Inc. and its consolidated subsidiaries".
- Exhibits: the exhibit index at [10-K] page:213 to page:216 lists the indentures and credit agreement as exhibits, and [10-K] page:216 lists "21.1 List of our subsidiaries". The listed exhibits are not supplied.
- Extraction: the text is flattened HTML. Printed 10-K page numbers (for example F-5) appear inline and differ from `page:N` chunks.

#### Forms 10-Q for the quarters ended March 31, June 30 and September 30, 2026

- Family and authority: filed quarterly reports with unaudited condensed statements. [Q1 10-Q] page:1 "For the Quarterly Period Ended March 31, 2026"; [Q2 10-Q] page:1 "For the Quarterly Period Ended June 30, 2026"; [Q3 10-Q] page:1 "For the Quarterly Period Ended September 30, 2026". Signature dates: [Q1 10-Q] page:46 "Date: May 5, 2026"; [Q2 10-Q] page:48 "Date: August 4, 2026"; [Q3 10-Q] page:53 "Date: October 29, 2026".
- Statements: income statements at page:2, balance sheets at page:2 or page:3 and cash flows at page:3 or page:4 of each 10-Q. Units: [Q3 10-Q] page:3 "CONSOLIDATED BALANCE SHEETS (unaudited) (dollars and shares in thousands, except per share data)". USD.
- Debt note and maturities: [Q1 10-Q] page:9 "6. Long-term debt"; [Q2 10-Q] page:10 "Scheduled maturities of long-term debt at June 30, 2026"; [Q3 10-Q] page:11 "7. Long-term debt" and [Q3 10-Q] page:12 "Scheduled maturities of long-term debt at September 30, 2026". The Q1 10-Q debt note has no maturity schedule; its MD&A refers to the note for "the maturities and other terms of our long-term debt" ([Q1 10-Q] page:43).
- Covenant text: the three 10-Qs carry no leverage covenant or leverage ratio text (each was searched for the word leverage); the covenant summary is in the 10-K ([10-K] page:183) and the ratio is in the releases.
- Credit agreement amendment: [Q3 10-Q] page:12 "On June 8, 2026 (the Ninth Amendment Effective Date), the Company entered into the Ninth Amendment (the Ninth Amendment) to the Credit Agreement."
- Liquidity: [Q1 10-Q] page:40, [Q2 10-Q] page:42 and [Q3 10-Q] page:47 each carry an "Available liquidity" paragraph; [Q3 10-Q] page:14 gives the revolver and letter-of-credit position.
- Events: [Q2 10-Q] page:22 "14. Subsequent events Elara Caring"; [Q3 10-Q] page:19 describes the Berkshire repurchase obligation and share repurchases after September 30, 2026. The Q3 10-Q has no separate subsequent-events note.
- Quarter versus year-to-date: the Q2 and Q3 reports present three-month and year-to-date columns side by side ([Q3 10-Q] page:44 "Nine months ended September 30"). Consumers must keep quarter and nine-month figures apart.

#### Earnings releases (Exhibit 99.1)

- Family and authority: issuer press releases furnished as Exhibit 99.1, management-prepared and unaudited. [Q1 ER] page:1 "Denver, Colorado, May 5, 2026"; [Q2 ER] page:1 "Denver, Colorado, August 4, 2026"; [Q3 ER] page:1 "Denver, Colorado, October 29, 2026".
- Content: reported and adjusted figures, guidance, statements, supplemental data and non-GAAP reconciliations. [Q3 ER] page:3 "Current 2026 guidance Prior 2026 guidance" carries guidance; [Q3 ER] page:9 to page:11 repeat the condensed statements; [Q3 ER] page:12 to page:13 give segment and debt data; [Q3 ER] page:15 to page:16 give the leverage ratio calculation.
- Non-GAAP items that are not in the 10-Qs: adjusted operating income, adjusted net income, free cash flow, "Consolidated EBITDA" and the "Leverage ratio" ([Q3 ER] page:15). These are issuer non-GAAP presentations; a management claim does not override the filed statements.
- Version relationship: the releases repeat 10-Q statement data. Treat the 10-Q as controlling for statement facts and do not count a release as independent corroboration of them.
- Credit agreement versions: [Q1 ER] page:15 "Under our amended senior secured credit facilities (the Amended Credit Agreement) dated November 24, 2025"; [Q2 ER] page:15 "dated June 8, 2026 and our prior senior secured credit facilities"; [Q3 ER] page:15 "dated June 8, 2026". The leverage definitions in the three releases therefore refer to different agreement versions, and each release states the version that applied to its period.

### Information-availability boundary

- All sources are dated on or before October 29, 2026: the 10-K on February 11, 2026, the Q1 documents on May 5, 2026, the Q2 documents on August 4, 2026 and the Q3 documents on October 29, 2026. All precede the cutoff of 2026-11-05.
- Items dated after the quarter end but inside the supplied filings are subsequent events and must be labelled as such: [Q3 ER] page:2 "Subsequent to September 30, 2026 through October 27, 2026, the Company has repurchased 0.5 million shares of our common stock" and [Q3 10-Q] page:1 "As of October 27, 2026, the number of shares of the registrant’s common stock outstanding was approximately 62.9 million shares."
- Nothing dated between October 29, 2026 and the cutoff is supplied. Any current report, debt transaction or rating action in that window is Not supplied, not absent.

### Identity and perimeter

- Reporting entity: DAVITA INC., Delaware, NYSE ticker DVA ([10-K] page:1 "DAVITA INC. (Exact name of registrant as specified in charter)").
- Borrower and issuer: the senior secured credit facilities and senior notes are obligations of DaVita Inc. [10-K] page:183 "Borrowings under the Company's senior secured credit facilities are guaranteed and secured by substantially all of DaVita Inc.'s and certain of the Company’s domestic subsidiaries' assets". The 6.75% Senior Notes are described at [10-K] page:184 as "guaranteed by each of the Company’s domestic subsidiaries that guarantee its senior secured credit facilities".
- Guarantors: the supplied text does not name the subsidiary guarantors, and no guarantor or non-guarantor financial information is supplied. The context leaves borrower, parent and guarantor fields blank, which is not evidence of their absence.
- Non-wholly-owned perimeter: the consolidated statements include noncontrolling interests. [Q3 10-Q] page:3 "Noncontrolling interests subject to put provisions" sits between liabilities and equity on the balance sheet, and [Q3 ER] page:15 shows "Net income attributable to noncontrolling interests" as an add-back in Consolidated EBITDA. Statement figures are consolidated, not attributable to DaVita Inc. alone, unless a line says otherwise.
- Related party: [Q3 10-Q] page:19 "Berkshire share repurchase agreement" and a payable classified as "due to related party" on the balance sheet. The Berkshire agreement itself is not supplied.
- Currency and units: USD throughout. The filings state amounts in thousands, and the releases mix "(dollars in millions)" tables with "(dollars and shares in thousands" statements. Consumers must convert units explicitly.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt, liquidity, cash flow, non-GAAP | [10-K] page:153 to page:155, page:178 to page:184; [Q3 10-Q] page:2 to page:4, page:11 to page:14, page:44 to page:47; [Q3 ER] page:9 to page:16 | Unit mix; non-GAAP figures are issuer-computed; Q1 10-Q has no maturity schedule |
| CP-1A | Business, segments, history, ownership, transactions | [10-K] page:4, page:211; [Q3 ER] page:3; [Q2 10-Q] page:22; [Q3 10-Q] page:19 | Subsidiary list, Berkshire agreement and Elara Caring agreement not supplied |
| CP-2 | CP-1 and CP-1A outputs; maturities; covenant summary; liquidity; caps; leverage | [10-K] page:135, page:183 to page:184; [Q3 10-Q] page:12 to page:14, page:47; [Q3 ER] page:15 to page:16 | Executed agreements not supplied; Consolidated EBITDA definition and add-backs unverifiable |
| CP-5 | Traceable claims | All seven sources carry page locators | HTML and XBRL not supplied; extraction fidelity not reviewed |

### Analytical read-through

- Usable coverage: audited FY2025 statements, three sets of unaudited 2026 statements and three releases support a reported financial foundation, a FY2025 to Q3 2026 bridge and a last-twelve-months view. The Q3 ER shows the issuer's own last-twelve-months construction at [Q3 ER] page:15.
- Strongest contrary evidence: the covenant and the leverage ratio are summarized, not supplied in the governing document. [10-K] page:183 "the Credit Agreement requires compliance with a maximum leverage ratio covenant, tested quarterly, of 5.00:1.00 through December 31, 2028" and [Q3 ER] page:16 "Maximum leverage ratio permitted under the Credit Agreement". The measure that applies is "Consolidated EBITDA" with "pro forma adjustments", which the releases say are "determined according to specified criteria set forth in the Applicable Credit Agreement" ([Q3 ER] page:15). The credit agreement and the amendment are exhibits that are not supplied.
- Source risk mechanism: the covenant ratio uses funded debt less unrestricted cash over a credit-agreement EBITDA, a different construction from operating income or reported EBITDA. A consumer that equates the release's ratio with a GAAP-based ratio would misread headroom. The release states this itself: [Q3 ER] page:15 "should not be considered a substitute for the ratio of total debt to operating income".
- Debt-like claims outside the debt table: operating lease liabilities appear on the balance sheet ([Q3 10-Q] page:3 "Long-term operating lease liabilities"), puttable noncontrolling interests ([Q3 10-Q] page:3), the Berkshire repurchase obligation ([Q3 10-Q] page:19) and letters of credit under a separate facility ([Q3 10-Q] page:14 "letters of credit of approximately"). The 10-K contractual obligations table ([10-K] page:135) lists leases and puts separately from "Long-term debt". CP-2 must decide inclusion explicitly.
- Floating-rate exposure: the debt note describes interest rate caps with strikes and maturities ([Q3 10-Q] page:12 to page:13). The balance of floating debt not covered by caps is stated at [Q3 10-Q] page:12 "The remaining $814,456 outstanding principal balance of Term Loan A-2 and $80,000 balance outstanding on the revolving line of credit are subject to SOFR-based interest rate volatility."
- What cannot proceed: verification of covenant definitions and headroom against the credit agreement, guarantor-level analysis, intercreditor or security-package analysis, ratings-based or market-based work.
- Next evidence action: supply the Credit Agreement and its amendments, the indentures for each senior note series, Exhibit 21.1, the Berkshire share repurchase agreement and any filings dated October 30, 2026 to November 5, 2026.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit Agreement, its amendments and the note indentures not supplied; covenant and leverage definitions unverifiable | High | CP-2 | Supply the executed documents listed in the exhibit index at [10-K] page:213 to page:214 and the Ninth Amendment |
| Subsidiary guarantor list (Exhibit 21.1) and guarantor financial information not supplied | Medium | CP-1A, CP-2 | Supply Exhibit 21.1 and any guarantor disclosure |
| Filings and events dated October 30, 2026 to November 5, 2026 not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| Credit ratings, market prices and peer data not supplied (searched all seven sources for Moody, Standard & Poor, S&P, Fitch and credit rating: no match; context ratings and quotes are empty) | Low for the selected modules | CP-2 | Not required for this scope; keep Not supplied |
| Berkshire share repurchase agreement and Elara Caring purchase agreement not supplied | Low | CP-1A, CP-2 | Supply if obligation terms are needed |
| Q1 10-Q debt note prints no maturity schedule | Low | CP-1, CP-2 | Use the 10-K, Q2 10-Q and Q3 10-Q schedules; label the Q1 gap |
| Mixed units (thousands in statements, millions in releases) and issuer non-GAAP measures | Low | CP-1, CP-2 | Convert units explicitly and label non-GAAP figures as issuer-computed |
| Text extraction only; filed HTML and XBRL not compared; no images or charts inspected | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |

## Next module

- CP-1: use the 10-K and 10-Q statements as controlling; keep quarter, nine-month, last-twelve-month and FY2025 figures apart; convert thousands and millions explicitly; label adjusted figures, free cash flow, Consolidated EBITDA and the leverage ratio as issuer non-GAAP.
- CP-1A: carry the Berkshire repurchase obligation and the Elara Caring investment (closed effective July 20, 2026) as events; label anything after October 29, 2026 as Not supplied.
- CP-2: carry the missing credit agreement and indentures as the main restriction; treat leases, puts, letters of credit and the Berkshire payable as claims to classify explicitly; use the 6.75% notes and credit-facility guarantee text as the only supplied guarantor evidence.
- CP-5: trace each claim to a `page:N` locator and carry the extraction-fidelity limit.
