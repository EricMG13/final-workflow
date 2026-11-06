## Request

Issuer: Magnera Corp (issuer id magn), NYSE ticker MAGN, registrant name in the filings "Magnera Corporation" (formerly Glatfelter Corporation). As-of date and cutoff: 2026-11-05. Pathway: credit_snapshot, public case. Reporting currency per the context: USD; the filings report in millions of US dollars. Current period per the context: Q3 FY2026, meaning the quarterly period ended June 27, 2026 (nine-month year-to-date "three quarterly periods" also reported). Prior period per the context: FY2025, the fiscal year ended September 27, 2025.

Question for this module: can the supplied source set support the requested downstream work (the four consumers CP-1, CP-1A, CP-2 and CP-5), and what remains blocked? This is a source-sufficiency review only. It gives no credit conclusion. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No figure is normalised or reconciled to a model here; the only arithmetic is footing checks on printed totals, shown under Calculations.

Context file settings relied on: no borrower, parent, guarantor, sponsor, rating, quote, deal-term or legal-document input is supplied (legal_documents is "none"). Blank context values are therefore not zero; they are absent inputs.

## Sources

Issuer sources relied on (exact pinned names and sha256). All are text extractions in which a "page" is a text chunk of at most 3000 characters, not a printed page; locators below use that `page:N`.

| Source (exact name) | sha256 | Family | Period or date located in the text |
| --- | --- | --- | --- |
| 10-K_2025-09-27_form10k.htm.jsonl | 8a2d31e8517added759c44fb832ba0e833b0182f88931d77ac8b15219681b6e7 | Annual report, audited | Fiscal year ended September 27, 2025; auditor report dated November 25, 2025 |
| 10-Q_2025-12-27_form10q.htm.jsonl | fc18cf0b3124192f072f0a094fbc1605152c44349946b7208b65f0ac25d88f0f | Quarterly report, unaudited | Q1 FY2026, quarter ended December 27, 2025 |
| 10-Q_2026-03-28_form10q.htm.jsonl | 00a31fc7f5573cbb41dba62ba9751e7ac35317c740673bba1de0ff348e567d96 | Quarterly report, unaudited | Q2 FY2026, quarter ended March 28, 2026 (two quarterly periods) |
| 10-Q_2026-06-27_form10q.htm.jsonl | 9bf0a737948e12b9a435299f2c1d5be9f80cbb7bbc87ba8bb4baa3f7134d16c0 | Quarterly report, unaudited | Q3 FY2026, quarter ended June 27, 2026 (three quarterly periods); signed August 6, 2026 |
| EX-99.1_2026-02-05_ef20064605_ex99-1.htm.jsonl | 2c929f0530d2fad28d8d608f7ff32ddbeacac9282e05451c75240bd19f5fad90 | Earnings release (stands in for a presentation) | Q1 FY2026 results |
| EX-99.1_2026-05-07_ef20072634_ex99-1.htm.jsonl | 35c908fa7ed7e14681927f2c36fd3b1ad0328d835bdae7fd06641846130d5ea2 | Earnings release (stands in for a presentation) | Q2 FY2026 results |
| EX-99.1_2026-08-06_ef20079553_ex99-1.htm.jsonl | 907fd63efeb9c514c2f2ef515ae237b76f56ae49850c45b010a3ceaedd06a508 | Earnings release (stands in for a presentation) | Q3 FY2026 results |

Context (user settings, not issuer evidence): context, sha256 4a094c245ff44dd6e34e569a37f728533980efba9932af440a0d9b2f6b50325a.

Not relied on: the pack file `_retrieval.json` is not a pinned source and was ignored by the run.

Supplied handoffs: none. This is the first module in the run; no upstream handoff exists, so none is listed.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases support a bounded credit snapshot of Magnera through the quarter ended June 27, 2026. Statements, debt table and segment data are well covered; executed debt documents, revolver terms and ratings are missing. | Medium | No credit agreements, indentures, borrowing base, letter of credit detail or revolver covenant terms are supplied, and nothing is dated after August 6, 2026. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Statements, notes and segment tables for FY2025 and three FY2026 quarters are present, and the printed debt tables foot. | Reported debt, cash and earnings can anchor leverage and liquidity work, subject to merger comparability. | High |
| Revolver size is printed, but borrowing base, letters of credit and revolver covenants are not. | Undrawn capacity and any springing test cannot be computed; liquidity is limited to cash and the stated facility size. | Medium |
| Prior-year periods mix carve-out and merger effects, and management adjusted and comparable measures are not filed figures. | Year-on-year trends and pro forma EBITDA need care; leverage should rest on filed figures with labelled adjustments. | Medium |
| Internal control material weaknesses persist and disclosure controls were not effective at June 27, 2026. | Raises reliability risk for reported numbers, partly offset by the unqualified audit opinion on the FY2025 statements. | Medium |
| No source is dated after August 6, 2026, so the fiscal 2026 year end and later events are absent. | Events up to the cutoff, including refinancing of the 2029 maturities, cannot be assessed. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for all four selected consumers. The audited annual report and three interim reports give a continuous statement run from FY2025 to Q3 FY2026, the notes give a facility-level debt table in each period, and the three releases add management's adjusted measures, guidance and reconciliations. That is adequate for a filing-based credit snapshot. It is not READY because the instruments that govern creditor rights are not in the pack (only an exhibit index naming them), the revolver is described only by size, maturity, margin range and a no-borrowings statement, and no source falls between August 6, 2026 and the cutoff. No consumer is CONDITIONAL or BLOCKED: identity is unambiguous and no extraction is unusable. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. A successful text extraction is not a fidelity review; no chart, image or workbook is part of this pack.

### Source-by-source assessment

Locator format is `[source prefix page:N] "exact text"`.

| Source | Authority and perimeter | Basis, units and what was located | Limitations |
| --- | --- | --- | --- |
| 10-K FY2025 | Filed annual report; controls audited facts. Registrant is the single filer Magnera Corporation, consolidated. [10-K_2025-09-27 page:1] "For the fiscal year ended September 27, 2025" | USD millions. Income statement, balance sheet, cash flow, equity, debt note, leases and contingencies, segments, pension, restructuring, controls, exhibit index located (audit reports on pages 20 to 22, statements on pages 23 to 25, debt on pages 32 to 34, leases and contingencies on pages 35 and 36, pension on page 39, restructuring on page 40, segments on pages 41 and 42, controls on pages 43 and 44, exhibit index on pages 46 to 48). | Prior-year columns are carve-out combined statements: [10-K_2025-09-27 page:26] "have been prepared on a carve-out basis". FY2024 and FY2023 notes are incorporated from an 8-K/A not supplied. |
| 10-Q Q1 FY2026 | Filed interim report; unaudited, consolidated. | USD millions, quarter to December 27, 2025. Statements, debt note, segments, MD&A, liquidity and controls located (page markers for statements on page 3 and 4). | Unaudited. Prior-year comparative contains merger effects from November 4, 2024. |
| 10-Q Q2 FY2026 | Filed interim report; unaudited, consolidated. | USD millions, quarter and two quarterly periods to March 28, 2026. Same content set located. | Unaudited. Comparatives as above. |
| 10-Q Q3 FY2026 | Filed interim report; controls the latest balance sheet. [10-Q_2026-06-27 page:1] "For the quarterly period ended June 27, 2026" | USD millions, quarter and three quarterly periods. All 21 text pages opened. Balance sheet (pages 3 and 4), cash flow (page 4), debt note (pages 8 and 9), contingencies (page 12), segments (page 11), MD&A and liquidity (pages 14 to 19), controls (pages 19 and 20). | Unaudited. Debt note carries no maturity schedule, guarantor list, revolver availability or letters of credit. No subsequent-events note was located. |
| Q1, Q2, Q3 releases | Issuer press releases furnished as EX-99.1; attributed management claims and non-GAAP measures, not controlling over filings. | Adjusted EBITDA, comparable-basis reconciliations, LTM and pro forma adjusted EBITDA, guidance, free cash flow. | Text extraction only; no slide deck or chart is supplied (releases stand in for presentations). Adjusted, comparable, LTM and pro forma figures are management-defined. |

### Entity, perimeter and instrument roles

- Issuer and perimeter: one consolidated reporting entity, Magnera Corporation, formerly Glatfelter Corporation. [10-K_2025-09-27 page:1] "Former name or former address, if changed since last report Glatfelter Corporation 4350 Congress Street, Suite 600 Charlotte, North Carolina 28209". The accounting acquirer was the carve-out business: [10-K_2025-09-27 page:5] "As Treasure was identified as the accounting acquirer". Pre-merger periods are therefore the carve-out business of the former parent (Berry); the acquired Glatfelter business is included only from the closing date, November 4, 2024.
- Borrower roles: the credit agreements named in the exhibit index list Treasure Holdco, Inc. as a party: [10-K_2025-09-27 page:47] "10.9 Asset-Based Revolving Credit Agreement, dated November 4, 2024, by and among Treasure Holdco, Inc., Magnera Corporation, certain subsidiaries of Magnera". Which entity is borrower versus guarantor, and which subsidiaries are restricted, is not resolved in the supplied text. The list of subsidiary guarantors is an exhibit that is named but not supplied: [10-K_2025-09-27 page:48] "22.1* List of Subsidiary Guarantors."
- Instruments printed in every debt note: term loan due November 2031, revolving credit facility due November 2029 (asset-based), 4.75 percent first priority senior secured notes due October 2029, 7.25 percent first priority senior secured notes due November 2031. [10-Q_2026-06-27 page:8] "7.25% First Priority Senior Secured Notes November 2031 760 800". Security and guarantee terms are not printed in the supplied text beyond the instrument names.
- Hedges: cross-currency swaps of euro 250 million and euro 425 million maturing November 2027 and November 2029: [10-Q_2026-06-27 page:9] "The swap agreements mature November 2027 (€250 million) and November 2029 (€425 million)." Non-USD amounts exist only in the swap notionals; reported figures are USD.
- Draft, executed and as-of status: all filings are filed final documents. The legal agreements are not supplied in any form, executed or draft.

### Cross-source conflicts and unreconciled points

| Point | Locators | Downstream effect |
| --- | --- | --- |
| Term loan SOFR reference differs within one filing: Item 7A states one rate and the debt note another. | [10-K_2025-09-27 page:19] "As of period end, the SOFR rate of approximately 4.19% was applicable to the Term Loan." against [10-K_2025-09-27 page:34] "which was approximately 4.16%" | Interest-rate sensitivity and pricing work should state which date or basis is used; immaterial to readiness. |
| The 4.75 percent notes are named "First Priority Senior Secured Notes" in the debt tables but "Senior Notes" in the exhibit index. | [10-Q_2026-06-27 page:8] "4.75% First Priority Senior Secured Notes October 2029 500 500" against [10-K_2025-09-27 page:46] "relating to the 4.750% Senior Notes due 2029" | Security ranking of this instrument cannot be confirmed without the indenture; the debt table (a filed statement) is used for the label and amount. |
| Exhibit 10.8 is dated November 4, 2024 but incorporated from an 8-K stated as filed in 2025. | [10-K_2025-09-27 page:47] "incorporated by reference to Exhibit 10.2 to the Current Report on Form 8-K filed on November 5, 2025" | Possible typographical error in the exhibit index; the agreement itself must be retrieved to confirm its date and terms. |
| Fiscal 2026 cash-from-operations and capex outlook changed between sources; the free cash flow range did not. | [EX-99.1_2026-02-05 page:2] "cash flow from operation of $170 - $190 million" and [10-K_2025-09-27 page:15] "free cash flow between $90 to $110 million"; later [10-Q_2026-06-27 page:13] "we project cash from operations between $150 to $170 million and free cash flow between $90 to $110 million" and "Projected fiscal 2026 free cash flow assumes $60 million of capital spending" | Use the latest dated guidance and label it management's; the earlier ranges are superseded, not errors. |
| Debt paydown is described as sixty-three million in MD&A and the releases but sixty-five million in the cash flow statement. | [10-Q_2026-06-27 page:18] "a $63 million prepayment of debt in the YTD" against [10-Q_2026-06-27 page:4] "Repayments on long-term borrowings (65 ) (434 )"; releases: [EX-99.1_2026-02-05 page:1] "we made $27 million in debt payments" and [EX-99.1_2026-05-07 page:1] "We made $36 million in debt repayments during the quarter" | A two million gap is not explained in the text (the debt table is consistent with the cash flow figure; see Calculations). Debt movements should use the cash flow statement and the debt tables. |
| Cross-currency swap liability is shown with a negative sign in some filings and positive in the latest. | [10-K_2025-09-27 page:35] "Cross-currency swaps Designated Other long-term liabilities $ (99 ) $ —" against [10-Q_2026-06-27 page:9] "Cross-currency swaps Designated Other long-term liabilities $ 78 $ 99" | Presentation sign only; both are liabilities. Carry the sign convention explicitly. |
| FY2025 free cash flow as reported by management adds pre-merger cash flow to the audited cash from operations. | [10-K_2025-09-27 page:17] "Cash flow from operating activities $ 103", "Pre-Transaction free cash flow from operating activities(1) 90", "Free cash flow $ 126" | The management free cash flow is not a GAAP-derived quantity; leverage and cash conversion work should start from the audited cash flow statement. |
| Management LTM and pro forma adjusted EBITDA exceed the filed segment adjusted EBITDA run rate by design. | [EX-99.1_2026-08-06 page:6] "Adjusted EBITDA (1) $ 187 $ 95 $ 282 $ 181 $ 83 $ 264 $ 372", "Synergies and cost reductions 35", "PF Adjusted EBITDA $ 405" | The release measures are attributed management claims; the filed adjusted EBITDA (segment note) controls, and pro forma or synergy-adjusted figures must stay labelled. |

No conflict was found between the filed statements and the release headline figures for the same periods (see Calculations).

### Coverage accounting

Every page is retained. The column "Opened" means the text of the page was read in this review; "Located by search" means the page was classified by its leading text and keyword searches across all sources, but not read line by line.

| Source | Pages (chunks) | Opened | Located by search only | What the search-only pages are |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | 49 | 31 (pages 1 to 5, 15 to 27, 32 to 36, 39 to 44, 46, 47) | 18 (pages 6 to 14, 28 to 31, 37, 38, 45, 48, 49) | Business and risk factor text, cybersecurity, accounting policies, goodwill and intangibles, tax notes, governance, exhibit tail and signatures |
| 10-Q Q1 FY2026 | 17 | 3 (pages 1, 7, 15) | 14 | Statements, segment, MD&A, controls, boilerplate; statements and notes located by heading and keyword |
| 10-Q Q2 FY2026 | 20 | 2 (pages 8, 18) | 18 | As above |
| 10-Q Q3 FY2026 | 21 | 21 | 0 | None |
| Release Q1 | 7 | 5 (pages 1, 2, 5 end, 6, 7) | 2 | Non-GAAP and forward-looking boilerplate |
| Release Q2 | 7 | 3 (pages 1, 6, 7) | 4 | Narrative continuation and boilerplate |
| Release Q3 | 7 | 5 (pages 1, 2, 3, 6, 7) | 2 | Forward-looking boilerplate |

Consumers that rely on a search-only page must open it before using it. No coverage unit is an evidenced exclusion except the ignored `_retrieval.json`. Images, charts and speaker notes: none exist in the extraction; unsupported visual content is a parse gap and no image coverage is claimed.

### Consumer assessment

| Consumer and evidence demand | Status | Located evidence | Carried limitations |
| --- | --- | --- | --- |
| CP-1: reported financial facts, discrete periods, calculations | READY_WITH_LIMITATIONS | Statements for FY2025 and each FY2026 quarter; quarter versus year-to-date columns labelled; segment table [10-Q_2026-06-27 page:11] "Total adjusted EBITDA $ 99 $ 91 $ 282 $ 264" | Pre-merger comparatives are carve-out; interim cash-paid interest and taxes are not supplied; discrete Q4 FY2025 is not printed and would be derived. |
| CP-1A: business, transaction and ownership context | READY_WITH_LIMITATIONS | Business description and merger terms in the annual report [10-K_2025-09-27 page:5]; purchase price allocation [10-K_2025-09-27 page:32] "Debt (869 )" | Merger agreement, Form 10 and 8-K exhibits are named but not supplied; no ownership register; no sponsor. |
| CP-2: fundamental credit synthesis | READY_WITH_LIMITATIONS | Debt, cash, liquidity narrative, covenants statement, contingencies, guidance | No revolver availability, borrowing base or letters of credit; no ratings or market data; no legal documents; no post-August 6, 2026 information. |
| CP-5: evidence trace of the other modules | READY_WITH_LIMITATIONS | Every module claim can be traced to a page locator in the pinned text | Cannot test claims against executed documents or images; search-only pages must be opened before they are cited. |

### Read-through: evidence, source risk, consequence

Debt capacity evidence. The latest debt note lists four instruments and a footing total, and states that the term loan and secured notes carry no financial maintenance covenants: [10-Q_2026-06-27 page:9] "Despite not having financial maintenance covenants on our term loan and secured notes". The source risk is that the revolver is described separately as an asset-based facility with no borrowings, yet its covenant, availability and letter of credit terms are not printed anywhere in the pack. The consequence is that downstream liquidity can use cash and the stated revolver size but must present undrawn capacity as unconfirmed, and must not state that no covenant applies to the revolver. The compliance statement covers "all long-term debt covenants": [10-Q_2026-06-27 page:9] "We are in compliance with all long-term debt covenants as of June 27, 2026."

Refinancing evidence. Management says it intends to refinance, and the annual report states there are no maturities before 2029: [10-K_2025-09-27 page:34] "The Company has no future maturities of long-term debt until 2029, at which point $500 million and $1,531 million are due in fiscal year 2029 and 2031, respectively". The latest interim report repeats the intention: [10-Q_2026-06-27 page:19] "which we intend to refinance prior to maturity". Source risk: the maturity schedule is printed only in the annual report and as of September 27, 2025; interim notes give maturity dates but no schedule, and no source after August 6, 2026 can show a refinancing. Consequence: the maturity wall for the cutoff must be rebuilt from the interim debt table and labelled as derived, and any refinancing between August 6, 2026 and the cutoff is unknown.

Reporting reliability evidence. The annual audit has an unqualified opinion on the statements and an adverse opinion on internal control: [10-K_2025-09-27 page:20] "expressed an adverse opinion thereon". The latest interim report says: [10-Q_2026-06-27 page:20] "management has concluded that our disclosure controls and procedures were not effective as of the last day of the period covered by this report". Source risk: unaudited interim figures rest on controls the issuer itself calls ineffective, tied to merger accounting and legacy IT systems. Consequence: downstream modules should treat interim figures as filed but carry the control weakness as a standing limitation, and CP-5 should test interim totals against the printed foots.

Comparability evidence. Year-to-date FY2026 against prior year includes merger revenue in the comparison base: [10-Q_2026-06-27 page:17] "The net sales increase included revenue from the prior year merger of $112 million". Source risk: the prior-year interim and the FY2024 columns are carve-out or partial-period figures, so growth rates mix organic change, acquisition and currency. Consequence: CP-1 must not present unadjusted year-on-year growth as organic, and should use the releases' comparable-basis tables only as attributed management measures.

Off-balance sheet evidence. Receivables are sold under customer programmes: [10-K_2025-09-27 page:27] "The Company participates in customer supply chain financing programs to collect certain receivables through third-party financial institutions." Source risk: no volume or balance is printed in any source. Consequence: operating cash flow and working capital cannot be adjusted for the programme, and CP-2 must show it as an unquantified item. Other claims outside the debt table that are located: unfunded frozen pension plans [10-K_2025-09-27 page:39] "all of which are frozen to new participants and existing participants from accruing additional benefits and are unfunded"; Fox River environmental liability [10-Q_2026-06-27 page:12] "outstanding balance of the environmental liability and corresponding escrow asset were $17 million and $9 million"; Brazilian tax claims [10-Q_2026-06-27 page:12] "not expected to exceed $66 million as of June 27, 2026"; operating leases [10-Q_2026-06-27 page:8] with finance leases described as not material in the annual report.

Perimeter evidence. The annual report presents one consolidated entity and the exhibit index names a separate borrower entity and an unsupplied guarantor list. Source risk: restricted and unrestricted group, guarantor coverage and structural subordination of the notes cannot be mapped. Consequence: CP-2 should not assert guarantor coverage or collateral scope beyond the instrument names.

Next evidence action: retrieve the term loan agreement, the asset-based revolving credit agreement and its amendment, the three indentures and the guarantor list (all exhibits named in the annual report index), plus any filing, release or report dated after August 6, 2026 up to the cutoff, before liquidity, covenant or refinancing conclusions are finalised.

## Calculations

These are footing and consistency checks on printed figures, to test source integrity. They do not normalise or reconcile figures to a model. All amounts are USD millions.

| Check | Inputs and locators | Result | Printed total | Outcome |
| --- | --- | --- | --- | --- |
| Debt table, June 27, 2026 | Term loan 706, revolver 0, 4.75% notes 500, 7.25% notes 760, discounts and fees (65); [10-Q_2026-06-27 page:8] | 706 + 0 + 500 + 760 - 65 = 1,901 | 1,901 | Foots |
| Debt table, September 27, 2025 | Term loan 731, revolver 0, 4.75% notes 500, 7.25% notes 800, discounts and fees (79); [10-K_2025-09-27 page:32] and [10-K_2025-09-27 page:33] | 731 + 0 + 500 + 800 - 79 = 1,952 | 1,952 | Foots |
| Maturity wall, annual report | Fiscal 2031: term loan 731 plus 7.25% notes 800; fiscal 2029: 4.75% notes 500; [10-K_2025-09-27 page:34] | 731 + 800 = 1,531; 500 | 1,531 and 500 | Agrees |
| Quarterly net sales to year-to-date | Q1 792 [EX-99.1_2026-02-05 page:1]; Q2 796 [EX-99.1_2026-05-07 page:1]; Q3 857 [EX-99.1_2026-08-06 page:1] | 792 + 796 + 857 = 2,445 | 2,445 [10-Q_2026-06-27 page:3] | Agrees |
| Quarterly adjusted EBITDA to year-to-date | Q1 93; Q2 90; Q3 99 (same release pages) | 93 + 90 + 99 = 282 | 282 [10-Q_2026-06-27 page:11] | Agrees |
| Management LTM adjusted EBITDA | FY2025 354 [10-K_2025-09-27 page:41]; year-to-date 282; prior year-to-date 264 | 354 + 282 - 264 = 372 | 372 [EX-99.1_2026-08-06 page:6] | Agrees with the release; the release measure remains management-defined |
| Debt reduction, September 27, 2025 to June 27, 2026 | Term loan 731 to 706 = 25; 7.25% notes 800 to 760 = 40 | 25 + 40 = 65 | Cash flow repayments 65 [10-Q_2026-06-27 page:4]; MD&A text 63; releases 27 + 36 = 63 | Debt tables agree with the cash flow; the text figure differs by 2, unexplained |
| Cash, latest balance sheet | Balance sheet date June 27, 2026 | Not recalculated | 280 [10-Q_2026-06-27 page:3] and MD&A text 280 | Agrees |

## Gaps

Each gap names the searches made across all seven sources (terms and synonyms) before concluding.

| Gap | Search made | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| Executed debt documents not supplied (term loan agreement, asset-based revolving credit agreement and amendment, indentures, guarantor list); only the exhibit index names them. | Searched "guarant", "indenture", "covenant", "springing", "fixed charge", "availability" | High | CP-2, CP-5 | Retrieve the exhibits listed in the annual report index; context states legal_documents is none |
| Revolver availability, borrowing base, drawn letters of credit not supplied; only size, maturity, margin range and no borrowings are printed. | Searched "letters of credit", "standby", "LC", "borrowing base", "availability" (no matching text) | High | CP-2 | Obtain the revolver agreement and the lender compliance information; until then show undrawn capacity as unconfirmed |
| Revolver covenant terms not supplied; only the statement that term loan and secured notes have no maintenance covenants and that the issuer is in compliance. | Searched "maintenance", "covenant", "springing" | High | CP-2 | As above |
| Credit ratings not supplied. | Searched "rating", "Moody", "S&P" (hits were unrelated words) | Medium | CP-2 | Add agency reports if a rating view is required |
| Maturity schedule for the interim balance sheet not printed; only the annual report schedule as of September 27, 2025. | Searched "maturities" in all interim reports | Medium | CP-1, CP-2 | Rebuild from the interim debt tables, labelled derived |
| Accounts receivable supply chain financing volumes not supplied. | Searched "supply chain financ", "factoring" | Medium | CP-1, CP-2 | Obtain from issuer disclosure or call; treat as unquantified |
| Interim cash-paid interest and cash taxes not supplied (annual net cash interest is printed). | Searched "cash interest", "interest paid", "income taxes paid", "cash paid for" | Medium | CP-1, CP-2 | Derive only with labelled assumptions; annual cash interest [10-K_2025-09-27 page:34] "Net cash interest was $124 million in fiscal 2025" |
| No source dated after August 6, 2026; the fiscal 2026 year end (the interim report states the fiscal year ending September 26, 2026) and fourth-quarter results are not supplied; no subsequent-events note found. | Searched "subsequent" (only generic text) | High | all | Retrieve any later filings or releases up to the cutoff; until then, post-quarter events are unknown, not nil |
| Prior-year and FY2024 comparatives are carve-out combined statements; FY2024 and FY2023 notes sit in an 8-K/A that is not supplied. | Searched "carve-out" | Medium | CP-1, CP-2 | Retrieve the 8-K/A if multi-year history is needed |
| No presentation decks, charts or images; releases are text only. | Not applicable | Low | CP-1A | Treat releases as attributed management claims |
| Ownership register, sponsor, and merger agreement terms not supplied; context has no sponsor or parent. | Searched "sponsor" (no hit); the former parent appears only in transaction narrative | Medium | CP-1A | Retrieve proxy or Form 10 if ownership analysis is needed |
| Internal control material weaknesses and ineffective disclosure controls are an open limitation, not a source defect. | [10-K_2025-09-27 page:44] and [10-Q_2026-06-27 page:20] | Medium | all | Carry as standing limitation |
| Pages classified by search only (see Coverage accounting) are unread in this review. | Not applicable | Low | all | Open before citing |

## Next module

Proceed to CP-1 (reported financial facts and calculations), then CP-1A, CP-2 and CP-5 in the run order. Carry these instructions forward unchanged:

- Treat the quarter ended June 27, 2026 as the current period and the fiscal year ended September 27, 2025 as the prior period; keep quarter, nine-month year-to-date, LTM and fiscal-year figures labelled, and keep USD millions.
- Use filed statements and notes for debt, cash, earnings and covenants; use releases only as attributed management measures (adjusted, comparable, LTM, pro forma and synergy-adjusted EBITDA stay labelled).
- Do not state revolver availability, letters of credit, revolver covenants, guarantor coverage or security scope as facts; they are not supplied.
- Show the maturity wall at the interim date as derived from the debt table, and note that no source after August 6, 2026 exists.
- Carry the control weakness, the carve-out comparability and the unquantified receivables programme as standing limitations.
- Open any search-only page before citing it.
