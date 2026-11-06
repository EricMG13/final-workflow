## Request

Issuer: COLUMBUS MCKINNON CORP (issuer id cmco; Columbus McKinnon Corporation, New York corporation, Nasdaq: CMCO; the filing registrant and the only reporting entity in the pack). As-of date and cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency named by the run context: USD; the filings state amounts in thousands of US dollars and the earnings releases state amounts in millions or thousands of US dollars. Periods named by the run context: current period q2-2027 (the fiscal quarter ended September 30, 2026; the fiscal year ends March 31) and prior period fy-2026 (the fiscal year ended March 31, 2026). Both context periods are confirmed from document content, not file names, in the Sources section below.

Question for this module: can the supplied source set support the requested downstream modules (CP-1, CP-1A, CP-2, CP-5) and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion and does not normalize, reconcile or calculate figures. Source sufficiency is kept separate from completion of downstream analysis.

The run context holds no deal terms, quotes, ratings, peers, precedents, borrower or parent name, guarantors, sponsor, research questions or legal documents (`legal_documents` is "none"). Those blanks are not treated as zero or as evidence.

## Sources

### Issuer sources relied on

All seven files are text extractions of SEC-filed HTML (page chunks `page:N`). The hash below is the sha256 of the retained extraction that CP-OS pinned for this run.

| Source (exact name) | sha256 | Document family and authority | Entity and period (from content) | Pages retained |
| --- | --- | --- | --- | --- |
| 10-K_2026-03-31_cmco-20260331.htm.jsonl | 6c5bc84510574e2ec737bd05ee1fd8a3711e8a18e3afa84ac93b9ca09421f3b2 | Annual report on Form 10-K; audited filed statements, controlling for fiscal 2026 facts | Columbus McKinnon Corporation, consolidated; fiscal year ended March 31, 2026, with fiscal 2025 and fiscal 2024 comparatives | 164 |
| 10-Q_2025-12-31_cmco-20251231.htm.jsonl | 768e09ab99d2d57b573c1d7e611dcf23d35114d9f599e779b33b981ef5e2e322 | Quarterly report on Form 10-Q; unaudited filed statements | Consolidated; quarterly period ended December 31, 2025 (third quarter of fiscal 2026); before the Kito Crosby close | 61 |
| 10-Q_2026-06-30_cmco-20260630.htm.jsonl | 848d4b1e6de7319613096e948145f873979b72374e1b0adf1266c7e707ed74ea | Quarterly report on Form 10-Q; unaudited filed statements | Consolidated; quarterly period ended June 30, 2026 (first quarter of fiscal 2027) | 52 |
| 10-Q_2026-09-30_cmco-20260930.htm.jsonl | b3c5294b4e11dbda4ecee230ea30aa7939709362043cb1c68987937b3770044b | Quarterly report on Form 10-Q; unaudited filed statements; the current-period source | Consolidated; quarterly and six-month periods ended September 30, 2026 (second quarter of fiscal 2027) | 60 |
| EX-99.1_2026-06-04_exhibit9913312026.htm.jsonl | 8fe0fb89665018b65928f2f5ad1f43cd441cafa6d1887e5ab7c1c193c08194ed | Earnings release (Exhibit 99.1); management presentation of reported and non-GAAP figures, supporting only | Consolidated; fourth quarter and fiscal year ended March 31, 2026; dated June 4, 2026 | 17 |
| EX-99.1_2026-07-30_exhibit99107302026.htm.jsonl | 79d10e65644259bd7729bae3526568d114dc088282b163dea033ec227104fc0f | Earnings release (Exhibit 99.1); supporting only | Consolidated; first quarter of fiscal 2027; dated July 30, 2026 | 12 |
| EX-99.1_2026-11-03_exhibit9911132026.htm.jsonl | b37aa7a41882d117efc3cc33b70d5e18769d1bc6e6c1fb21bd10142444e39a78 | Earnings release (Exhibit 99.1); supporting only | Consolidated; second quarter of fiscal 2027; dated November 3, 2026 | 15 |

Run context (not issuer evidence): `context` sha256 6575122c1a10165e3e05cc3e66f366997e6fa4e2f6aa905298c07efcd7fba897. The pack folder also holds `_retrieval.json`; CP-OS ignored it and it is not used here.

Labels read from content, not file names: [10-K p:1] "For the fiscal year ended March 31, 2026"; [10-Q 2025-12-31 p:1] "For the quarterly period ended December 31, 2025"; [10-Q 2026-06-30 p:1] "For the quarterly period ended June 30, 2026"; [10-Q 2026-09-30 p:1] "For the quarterly period ended September 30, 2026". The file-name dates for the three releases are the release dates in the text (June 4, July 30 and November 3, 2026), all before the cutoff.

### Supplied handoffs

None. CP-0 is the first module of this run and CP-OS supplied no upstream handoff (handoffs object empty). Nothing is inherited.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and releases are enough to run the requested financial, business, synthesis and trace modules with stated limitations. Debt, liquidity, covenant and ownership detail comes only from filing notes and releases. | Medium | No credit agreement, indenture, preferred share terms, purchase agreement, ratings or market data are supplied, so legal terms rest on summaries in filing notes. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The current-period quarterly report and release are supplied and carry the post-acquisition debt, liquidity and leverage disclosure. | Current capital structure can be sourced from filed statements and notes. | High |
| The annual report contains only about two months of the acquired business, so full-year results are not a like-for-like run rate. | Trend and leverage work must label period and perimeter and use the pro forma and release data with care. | High |
| Several facts conflict or are unresolved: revolver maturity, sponsor ownership percentage, annual report filing date, and the revolver covenant trigger. | Analysts must log each conflict with both locators instead of choosing a value. | Medium |
| Legal documents are absent, and the amended receivables facility terms from late October 2026 are not described. | Covenant headroom, guarantor coverage and receivables-facility triggers cannot be verified against executed terms. | Medium |

### Readiness view

Overall view: READY_WITH_LIMITATIONS for the source set as a whole. The pinned filings and releases cover every document family needed for a public-company credit snapshot: an audited annual report for fiscal 2026, three quarterly reports bridging the Kito Crosby close and the current period, and three earnings releases with non-GAAP reconciliations. The current period (quarter ended September 30, 2026) and the prior fiscal year (ended March 31, 2026) named in the context are both directly covered by filed statements. Strongest contrary evidence: legal and financing documents are absent, the acquisition accounting is still preliminary, and the annual report mixes a short post-acquisition stub with full-year legacy results. This view is source sufficiency only (SOURCE_SUFFICIENCY_ONLY); CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. It does not assert that quarters are normalized or reconciled, or that any downstream input contract is met.

### Consumer assessments

| Consumer | Readiness | Basis and carried limitations |
| --- | --- | --- |
| CP-1 (financial data and canonical figures) | READY_WITH_LIMITATIONS | Statements, debt, liquidity, cash-flow and cash-paid data are located (see coverage below). Limits: acquisition stub period, preliminary purchase accounting, single reportable segment, discrete fourth quarter only via the June 2026 release, covenant levels for the current facilities only in summary. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, acquisition, financing, preferred equity and divestiture narrative are located in the annual report and quarterly notes. Limits: executed transaction documents absent; sponsor ownership percentage differs between sources; context names no sponsor or parent. |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Evidence for business and financial risk is located; it draws on the CP-1 and CP-1A handoffs once those exist, and their absence now is not a source condition. Inherits every limitation above; no ratings or market inputs are supplied. |
| CP-5 (evidence trace validator) | READY_WITH_LIMITATIONS | Every source is retained and addressable by page, so quotes can be traced. Inherits the conflicts and gaps below; it must treat extraction as text only. |

No consumer is CONDITIONAL or BLOCKED. No command in the downstream sheet is DO NOT RUN for source reasons.

### Source coverage by profile

Financial reports (annual and quarterly):

- Statements and period labels. Current-period statements are at [10-Q 2026-09-30 p:5] "Net sales $ 539,285 $ 261,047 $ 1,070,746 $ 496,967" (three and six months, current and prior-year columns). Annual statements and the cash-flow statement are in the annual report ([10-K p:78] "Interest paid $ 45,630 $ 30,054 $ 34,983").
- Debt notes with instrument terms. [10-Q 2026-09-30 p:27-31] cover the Senior Secured Notes, the 2026 Term Loan B, the 2026 Revolving Credit Facility, the AR Securitization Facility, other debt, one finance lease and non-U.S. lines. Annual equivalents are at [10-K p:110-115].
- Liquidity. [10-Q 2026-09-30 p:55] "Our liquidity as of September 30, 2026 was $531,980,000"; the prior year-end figure is stated in the same paragraph.
- Cash paid for interest and taxes. [10-Q 2026-09-30 p:8] "Interest paid $ 90,921 $ 16,114" and the income taxes paid line for the six months.
- Segments. [10-Q 2026-09-30 p:47] "The Company has one operating and reportable segment"; no segment table exists, so segment-level KPIs are not available. Reporting units and goodwill by reporting unit are given at [10-Q 2026-09-30 p:22].
- Acquisition. [10-Q 2026-09-30 p:9] "all-cash transaction valued at $2,821,907,000"; funding by senior secured notes, term loan and preferred shares is at [10-Q 2026-09-30 p:10]. Kito Crosby's contribution to net sales and operating income is stated for the current periods only at the same page. The annual report also carries unaudited pro forma information ([10-K p:90]).
- Financing events after year-end: [10-Q 2026-09-30 p:27] "The AR Securitization Facility was further amended on October 29, 2026" and the First Amendment of September 21, 2026 on the same page; these are subsequent to the quarter for the October event and are inside the cutoff.
- Preferred equity: [10-Q 2026-09-30 p:33] gives the preferred terms in summary and the dividend-in-kind accrual.
- Contingencies: [10-Q 2026-09-30 p:34-43] cover product liability, asbestos and Magnetek matters.

Earnings releases:

- Reported versus adjusted. [EX-99.1 2026-11-03 p:13] "Adjusted EBITDA $ 111,205 $ 40,217 $ 222,648 $ 72,828" with the reconciliation above it; quarter and six-month (year-to-date) columns are labelled separately.
- Credit Agreement leverage. [EX-99.1 2026-11-03 p:14] "Credit Agreement Net Leverage Ratio 4.9x 5.1x" (twelve months ended September 30, 2026 and March 31, 2026) with its Net Debt and trailing adjusted EBITDA build; the definition is at [EX-99.1 2026-11-03 p:15]. This is management's non-GAAP presentation of a defined credit agreement term and does not override filed statements.
- Guidance: [EX-99.1 2026-11-03 p:3] gives updated fiscal 2027 outlook against the prior outlook. It is management forward-looking language, not evidence of results.
- The June 2026 release gives the fourth quarter and fiscal year (three-month and year income statements at [EX-99.1 2026-06-04 p:7-8]; reconciliation at p:14) and is the only source for discrete fourth-quarter figures.

Legal and financing sources: none supplied as documents. The 2026 Credit Agreement, the Senior Secured Notes indenture, the First Amendment, the receivables agreement and amendments, the preferred share terms and the stock purchase agreement appear only as descriptions in filing notes and exhibit lists ([10-K p:113] "The 2026 Credit Agreement and the Senior Secured Notes Indenture (collectively the “Debt Agreements”)"). They remain separate, unsupplied active sources; no later filing collapses them.

Scans, images and decks: none supplied. Presentations are not in the pack; the three earnings releases are text exhibits. The extraction is text only, so charts, images or tables rendered as images, if any, are not inspected (parse gap).

### Entity, perimeter and instrument roles

- Reporting entity: Columbus McKinnon Corporation is the registrant, the Borrower under the 2026 Credit Agreement and the issuer of the Senior Secured Notes ([10-K p:111] "Columbus McKinnon Corporation (the “Borrower”) entered into a new credit agreement"). The statements are consolidated. No separate subsidiary issuer statements are supplied. The 10-Q describes "Columbus McKinnon EMEA GmbH and certain subsidiary guarantors" as parties to the First Amendment ([10-Q 2026-09-30 p:27]); the guarantor list itself is Not supplied, and the context names no guarantors.
- Acquired business: Kito Crosby Limited, acquired from funds associated with KKR ([10-Q 2026-09-30 p:9]); consolidated from February 3, 2026. [10-K p:57] "Please note that the Kito Crosby Acquisition closed on February 3, 2026 so fiscal 2026 includes approximately two months of Kito Crosby financial performance." The U.S. power chain hoist and chain operations were divested on March 4, 2026 (same page), so the annual report perimeter changes twice within the fiscal year.
- Ownership and control: the preferred shares are held by CD&R XII Keystone Holdings, L.P. (the "CD&R Investor", [10-Q 2026-09-30 p:33]). The context leaves sponsor and parent blank; the filings are the only source of this relationship.
- Restricted versus unrestricted entities: not identified in any supplied source (the indenture is absent).
- Currency and units: US dollars; the filings are in thousands and the releases mix millions and thousands, so figure transcription must keep the unit of each source.
- Draft, executed and as-of: all filings are filed statements; the quarterly statements are unaudited; the purchase price allocation is preliminary ([10-Q 2026-09-30 p:11] "The purchase price for the Kito Crosby Acquisition has been preliminarily allocated"). Guidance and "Legacy CMCO" measures are management constructs.

### Version relationships and duplicates

- The pack holds one annual report and three quarterly reports for different periods plus three different releases; none is a duplicate of another. Each quarterly report is a separate active source for its period.
- The December 2025 quarterly report predates the acquisition and describes the pre-acquisition Term Loan B and revolver structure; it does not carry the current capital structure. The annual report describes both the superseded first lien facilities and the 2026 facilities. [10-K p:118] "The key financial covenant is triggered only on any date when any Extension of Credit under the Amended and Restated Revolving Credit Facility is outstanding" describes the superseded revolver, not the 2026 revolver, and must not be read as a current covenant.
- Fiscal year-end quarter: no separate fourth-quarter 10-Q exists, as expected. The fourth quarter appears only in the June 2026 release.

### Conflicts and inconsistencies to carry forward

| ID | Conflict | Locators | Downstream effect |
| --- | --- | --- | --- |
| C1 | The 2026 Revolving Credit Facility maturity is given as 2028 in one annual report paragraph and in the first-quarter fiscal 2027 quarterly report, and as 2031 in the next annual report paragraph and in the first-quarter and second-quarter fiscal 2027 quarterly reports. | [10-K p:111] "Revolving Credit Facility maturing February 3, 2028"; [10-Q 2026-06-30 p:24] "Revolving Credit Facility maturing February 3, 2028"; [10-K p:112] "maturing February 3, 2031 governed by the 2026 Credit Agreement"; [10-Q 2026-09-30 p:28] "a $500,000,000 2026 Revolving Credit Facility with a group of financial institutions or Revolving Credit Facility maturing February 3, 2031" | Debt maturity profile and liquidity runway need the date logged as conflicting; the latest filing and the second annual paragraph agree on 2031 but the executed agreement is not supplied. |
| C2 | CD&R Investor as-converted ownership is stated as approximately 42% in the December 2025 quarterly report and approximately 43% in the 2026 reports. | [10-Q 2025-12-31 p:10] "approximately 42% of the Company's outstanding equity"; [10-Q 2026-09-30 p:33] "approximately 43% of the Company's outstanding equity following completion of the Kito Crosby Acquisition" | Ownership and control analysis must show both and note the later filing is the more recent statement, without reconciling them. |
| C3 | Annual report filing date: later filings say it was filed on June 2, 2026, but its signature page is dated June 8, 2026 and its cover share count is as of June 4, 2026. | [10-Q 2026-09-30 p:8] "filed with the SEC on June 2, 2026"; [10-K p:164] "Date: June 8, 2026"; [10-K p:2] "outstanding as of June 4, 2026" | Low severity for credit analysis; the as-of timing of annual facts is the March 31, 2026 balance sheet date, but the filing date cannot be fixed from the pack. |
| C4 | The annual report maturity table is introduced as covering three instruments but its total is larger than the three instruments it names. | [10-K p:115] "The principal payments obligated to be made as of March 31, 2026 on the 2026 Term Loan B, the Senior Secured Notes and AR Securitization are as follows:" and "$ 2,440,996" | The maturity wall must be rebuilt from the instrument table, not copied from this total; CP-1 must state what the total includes. Not reconciled here. |

### Strongest contrary evidence and limitations (evidence, risk mechanism, consequence)

- Evidence: the covenant disclosure for the current facilities is a single summary sentence, [10-K p:113] "the key financial covenants prohibit the Consolidated First Lien Leverage Ratio for the reference period ended on such date from exceeding 7.75 to 1.00 as of any date of determination with step-downs for the first three years to 7.25 to 1.00, 6.75 to 1.00 and 6.25 to 1.00." Mechanism: the sources do not state whether the test applies at all times or only when revolver usage passes a threshold (the superseded facility had a usage trigger, [10-Q 2025-12-31 p:25]), nor the step-down dates. Consequence: covenant headroom analysis cannot be completed from the pack; the reported Credit Agreement Net Leverage Ratio is a different, net, all-debt measure from the first lien test and may not be used as covenant headroom.
- Evidence: [10-Q 2026-09-30 p:27] "The Company was in compliance with covenants under the AR Securitization Facility after receiving a waiver of the Delinquency and Default Ratios from the lender effective September 30, 2026." Mechanism: a waiver was needed to avoid breach at the quarter end and the facility was amended again on October 29, 2026, but the new ratio levels and the waived ratio levels are not stated. Consequence: receivables-facility trigger risk is visible but unquantifiable.
- Evidence: the annual report covers only a short post-acquisition stub ([10-K p:57]), and the quarterly reports show a large increase in net sales against prior-year columns. Mechanism: year-over-year and annual comparisons mix perimeters. Consequence: modules must label period and perimeter on every figure and use the pro forma and Legacy CMCO disclosures only as attributed management or unaudited pro forma data.
- Evidence: [10-Q 2026-09-30 p:11] preliminary purchase price allocation, with goodwill adjusted in the quarter. Mechanism: goodwill, intangibles and amortization may still change. Consequence: asset-based and amortization-sensitive measures carry a measurement-period limitation.

### Coverage accounting

- Retained: 381 of 381 extracted pages across the 7 sources (164, 61, 52, 60, 17, 12 and 15 pages). Every page is retained and addressable.
- Located and read for this assessment: the cover and contents pages of the annual report, its business, acquisition, debt, covenant and cash-flow pages, the current-period quarterly report front sections, statements, acquisition, debt, preferred equity, segment and liquidity pages, the signature pages, and the key reconciliation and guidance pages of the releases (page numbers are cited above). The remaining pages (risk factors, tax, pension, stock plan, legal proceedings, exhibits and similar) are retained but not individually reviewed in this module; their review belongs to the downstream modules that need them. No page is excluded and none is claimed as reviewed unless cited.
- Parse gaps: extraction is text only; image, chart and layout fidelity were not inspected, and extraction success is not a fidelity review.

## Calculations

No new calculations. This module does not normalize, reconcile or calculate financial figures. The only arithmetic is the page count: 164 + 61 + 52 + 60 + 17 + 12 + 15 = 381 retained pages across the seven sources.

## Gaps

| ID | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | Executed 2026 Credit Agreement, the First Amendment, the Senior Secured Notes indenture, the AR Securitization Facility agreement and its October 29, 2026 amendment: Not supplied. Covenant trigger, step-down dates, guarantor list, restricted-entity definitions and receivables ratio levels are Not supplied. | High for covenant and structure analysis | CP-1, CP-1A, CP-2, CP-5 | Obtain the exhibits (credit agreement, indenture, amendments) from the filer's exhibit list or its current reports; until then treat debt terms as management description in filing notes. |
| G2 | Preferred share terms (certificate of designations) and the stock purchase agreement for the acquisition: Not supplied; the filings give a summary only. | Medium | CP-1A, CP-2 | Obtain the corresponding exhibits; carry the 42% versus 43% conflict until then. |
| G3 | Discrete fourth-quarter fiscal 2026 statements: no quarterly filing; only the June 2026 release supplies fourth-quarter figures, and the year-to-date quarterly reports supply first and second quarter fiscal 2027 comparatives. Prior-year quarters (first and second quarter fiscal 2026) appear only as comparative columns in the fiscal 2027 reports. | Medium | CP-1 | Use labelled discrete or year-to-date columns; state when a discrete quarter is derived and from which sources. |
| G4 | Kito Crosby stand-alone historical financial statements before the close: Not supplied in the pack beyond the unaudited pro forma note ([10-K p:90]) and Kito Crosby's contribution disclosures. | Medium | CP-1, CP-2 | Treat pre-close comparisons as pro forma or management-normalized; do not present them as audited. |
| G5 | Ratings, quotes, market capitalization, peer and precedent data, portfolio inputs: Not supplied; the context leaves them blank. | Medium for relative value and portfolio work; none for the requested modules | CP-2 | Label as external or not supplied; do not infer. |
| G6 | Image and chart content of the filings and releases: not inspected (text extraction only). | Low | CP-1, CP-5 | Inspect source HTML or PDF if a chart or image-rendered table is relied upon. |
| G7 | Segment detail: the company reports one segment, so no segment table exists; revenue by product line or geography is only partly given (for example the U.S. share of sales). | Low | CP-1, CP-1A | Use the disclosed geographic and reporting-unit data and say where finer splits are absent. |
| G8 | Pages not individually reviewed in this module (see coverage accounting). | Low | all | Downstream modules open and cite each page they use. |
| G9 | Conflicts C1 to C4 are unresolved and logged, not reconciled. | Medium | CP-1, CP-1A, CP-5 | Quote both spans; request the executed documents or filing index to settle them. |

## Next module

Proceed to CP-1 on the full source set with these instructions carried forward:

- Label every figure with period (quarter ended September 30, 2026; six months ended September 30, 2026; fiscal 2026; the twelve-month Credit Agreement basis) and perimeter (pre-acquisition legacy, approximately two months of Kito Crosby in fiscal 2026, full quarters from fiscal 2027).
- Build debt by instrument from the notes ([10-Q 2026-09-30 p:27-31] and [10-K p:110-115]); log C1 and C4 where they matter; do not use the superseded first lien covenant as a current covenant.
- Take the covenant text only as summarized in [10-K p:113]; state that the trigger, step-down dates and the receivables-facility ratios are Not supplied.
- Use the earnings releases as attributed management non-GAAP presentation; filed statements control any conflict.
- Keep the SOURCE_SUFFICIENCY_ONLY assertion: nothing here is a normalized quarter or accepted model input.

CP-1A follows on the same sources with the ownership conflict (C2) and the absent executed documents (G1, G2) as stated limitations; CP-2 and CP-5 follow from the CP-1 and CP-1A handoffs.
