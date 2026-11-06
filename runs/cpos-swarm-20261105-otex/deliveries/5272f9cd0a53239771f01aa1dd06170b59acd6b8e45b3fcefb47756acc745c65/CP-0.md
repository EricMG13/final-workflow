## Request

Module CP-0, source readiness, for OPEN TEXT CORP (issuer id otex; registrant Open Text Corporation, Canada, NASDAQ and TSX ticker OTEX). As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency per the run context: USD. Current period per the run context: Q1 FY2027 (quarter ended September 30, 2026); prior period: FY2026 (year ended June 30, 2026). The fiscal year ends June 30.

The question answered here is whether the pinned source set can support the requested downstream modules (CP-1, CP-1A, CP-2, CP-5) and what remains blocked or limited. This module gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalize, reconcile or calculate figures. It assesses source sufficiency only; completion of downstream analysis is separate.

The run context (`context`) holds dated user settings. It contains no deal terms, quotes, ratings, peers, sponsor, borrower, parent or guarantor entries, and states legal documents as none. Blank context fields are treated as not supplied, not as zero.

## Sources

### Issuer sources relied on

Alias is used only for citations below. The hash is the sha256 of the extracted text file named in the first column. Each file is a page-chunked text extraction of the filed HTML document ("page:N" is the extracted chunk, not the printed page).

| Source file (exact name) | Alias | sha256 |
| --- | --- | --- |
| 10-K_2026-06-30_otex-20260630.htm.jsonl | 10-K | f68e5c975d736a5d60a932e22b4b1113b0dd717debe22c96d4297e49e4b48ad7 |
| 10-Q_2025-12-31_otex-20251231.htm.jsonl | 10-Q-Dec25 | c656e908af03f16a38fffb87df79cdeabf81b11c447b6307e4c89c53daecd451 |
| 10-Q_2026-03-31_otex-20260331.htm.jsonl | 10-Q-Mar26 | 337092207ee075518fbe18b12c9d6afe8e47e489c027bb48960c31b2c5742175 |
| 10-Q_2026-09-30_otex-20260930.htm.jsonl | 10-Q-Sep26 | 1fd82748eef70947f4a4d274b026606169ae599efc16f0e2194cf001bfe65e31 |
| EX-99.1_2026-05-07_q3-26pressreleaseexhibit991.htm.jsonl | PR-May26 | e697cff46a3e21a58ac9cf8d31a36bcb6270ad11a5dc8fdcfb37d685f98b9ffa |
| EX-99.1_2026-08-06_q4-26pressreleaseexhibit991.htm.jsonl | PR-Aug26 | 83f62f97a6b7c7e9bfc3742a4b7bc9c0199bd0f87ffa7a765f100c4602287036 |
| EX-99.1_2026-11-05_q1-27pressreleaseexhibit991.htm.jsonl | PR-Nov26 | f55be454dd27b1c15a5ec57d7bf7bf620ded41528eca4ef61bb9f128226efbcd |

### Run context (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (1002638-open-text-corp-otex.json) | cdf3e7e5d139751591ad9d995cdcdd0bad8e54e428f889bfd4cbcc1eae58ab70 |

### Supplied handoffs

None. CP-0 is the first module of this run, so no upstream handoff exists to list. The pack also contains a retrieval index (`_retrieval.json`) that CP-OS ignored; it was not used as evidence.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven issuer documents are complete, current to the cutoff and sufficient for the four requested downstream modules, each of which can proceed with stated limitations. | Medium | No executed debt documents, ratings, letters-of-credit detail or guarantor financials were supplied, and the covenant ratio value is not printed in any filing. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The latest quarterly report was filed on the cutoff date and describes an October 2026 refinancing after quarter end. | Period-end debt differs from the debt outstanding at the cutoff, so the two must be shown separately. | High |
| The only net leverage figure is a management statement in the latest earnings release. | It cannot be tied to the covenant definition, so covenant headroom cannot be taken from filings. | Medium |
| Product categories were reclassified in the latest quarter, and two businesses were sold during FY2026. | Revenue trends across periods need care about comparability. | High |
| No ratings, letters-of-credit amounts or guarantor financial information were supplied. | Facility availability and the structural position of lenders cannot be fully assessed. | High |

### Readiness view

The effective source set is sufficient for CP-1, CP-1A, CP-2 and CP-5 to run, each as READY_WITH_LIMITATIONS, and nothing is BLOCKED or CONDITIONAL. The set holds one annual report, three quarterly reports and three earnings-release exhibits, all dated on or before the cutoff and all issued by the registrant itself, which gives full statements, notes, debt and covenant descriptions, cash-flow supplements, adjusted EBITDA reconciliations and a post-quarter subsequent-events note. The limitations are the absence of executed financing documents and third-party material, the absence of a filed covenant calculation, and comparability breaks from reclassification and divestitures. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

### Source register

Each row records document family, original authority, entity and perimeter, period and basis, unit, and coverage. Authority: the filed 10-K and 10-Qs control financial-statement and note facts; the earnings releases are furnished exhibits whose figures are issuer statements supporting, never overriding, the filings. Identity and period are taken from the located content, not from file names.

| Alias | Family and authority | Entity and perimeter | Period and basis | Unit | Extraction coverage |
| --- | --- | --- | --- | --- | --- |
| 10-K | Annual report, filed financial report (original authority for annual facts) | Open Text Corporation, consolidated; single reported segment | Fiscal year ended June 30, 2026, three-year income statement and cash flow, two-year balance sheet; signed August 6, 2026 | USD thousands in statements | 311 of 311 chunks retained as text, cover through signatures |
| 10-Q-Dec25 | Quarterly report, filed (original authority) | Open Text Corporation, consolidated | Three and six months ended December 31, 2025 (Q2 FY2026), unaudited; signed February 5, 2026 | USD thousands | 100 of 100 chunks retained, cover through signatures |
| 10-Q-Mar26 | Quarterly report, filed (original authority) | Open Text Corporation, consolidated | Three and nine months ended March 31, 2026 (Q3 FY2026), unaudited; signed May 7, 2026 | USD thousands | 105 of 105 chunks retained, cover through signatures |
| 10-Q-Sep26 | Quarterly report, filed (original authority) | Open Text Corporation, consolidated | Three months ended September 30, 2026 (Q1 FY2027), unaudited; signed November 5, 2026 | USD thousands | 90 of 90 chunks retained, cover through signatures and exhibit list |
| PR-May26 | Earnings release, exhibit 99.1 (issuer and management statements) | Open Text Corporation, consolidated | Q3 FY2026 and nine months, reported and non-GAAP | Headline in USD millions, tables in thousands | 28 of 28 chunks retained |
| PR-Aug26 | Earnings release, exhibit 99.1 | Open Text Corporation, consolidated | Q4 FY2026 and FY2026, reported and non-GAAP | Headline in USD millions, tables in thousands | 31 of 31 chunks retained |
| PR-Nov26 | Earnings release, exhibit 99.1, dated on the cutoff | Open Text Corporation, consolidated | Q1 FY2027, reported and non-GAAP | Headline in USD millions, tables in thousands | 20 of 20 chunks retained |

Identity evidence: the 10-Q for the latest quarter names the registrant on its cover [10-Q-Sep26 page:1 — "OPEN TEXT CORPORATION (Exact name of Registrant as specified in its charter)"] and the period [10-Q-Sep26 page:1 — "For the quarterly period ended September 30, 2026 OR"]. The annual report covers [10-K page:1 — "For the fiscal year ended June 30, 2026 OR"]. The two earlier 10-Qs cover [10-Q-Dec25 page:1 — "For the quarterly period ended December 31, 2025 OR"] and [10-Q-Mar26 page:1 — "For the quarterly period ended March 31, 2026 OR"]. The releases are headed by quarter, for example [PR-Nov26 page:1 — "Fiscal 2027 First Quarter Highlights (in millions)(1)"], [PR-Aug26 page:1 — "Fiscal 2026 Fourth Quarter Highlights (in millions)(1)"] and [PR-May26 page:1 — "Fiscal 2026 Third Quarter Highlights (in millions)(1)"].

The latest 10-Q was signed on the cutoff date itself [10-Q-Sep26 page:90 — "Date: November 5, 2026"]. It is treated as inside the cutoff; the same applies to PR-Nov26.

### Version relationships and perimeter

- The filings are sequential periodic reports, not versions of one another. None supersedes another; each remains an active source for its own period. The 10-K covers the year to June 30, 2026, so the quarterly reports for Q2 and Q3 FY2026 are the only discrete-quarter filings for those quarters, and the Q4 FY2026 quarter appears as a discrete period only in PR-Aug26 and as a comparative in PR-Nov26.
- A Q1 FY2026 quarterly report and release were not supplied. The Q1 FY2026 figures exist only as the comparative column of 10-Q-Sep26 and PR-Nov26. No duplicate documents were found among the seven sources; overlapping facts (for example the Q3 FY2026 quarter in 10-Q-Mar26 and PR-May26) are different documents covering the same period, and the filing controls over the release.
- Entity roles: the registrant is the consolidated reporting entity and the only entity with supplied statements. Notes are issued by different group entities: the 2031 and 2030 senior notes by a subsidiary and guaranteed by the registrant [10-Q-Sep26 page:17 — "a subsidiary of the Company issued $650 million in aggregate principal amount of 4.125% senior notes due 2031 guaranteed by the Company"], and the annual report names that subsidiary [10-K page:117 — "OTHI merged with and into Open Text Inc. (OTI), a wholly-owned indirect subsidiary of the Company"]. The 2029 and 2028 senior notes were issued by the registrant itself [10-Q-Sep26 page:17 — "On November 24, 2021, the Company issued $850 million in aggregate principal amount of 3.875% senior notes due 2029"]. The secured instruments are guaranteed by certain subsidiaries [10-Q-Sep26 page:18 — "The Senior Secured Notes 2027 are guaranteed on a senior secured basis by certain of the Company’s subsidiaries"], and the term loan has subsidiary guarantors [10-Q-Sep26 page:21 — "The Acquisition Term Loan is unconditionally guaranteed by certain subsidiary guarantors, as defined in the Acquisition Term Loan"]. The identities of the guarantor group and any restricted or unrestricted split remain unresolved gaps (see Gaps).
- Perimeter changes inside the evidence window: the Vertica business was sold [10-Q-Sep26 page:38 — "On May 11, 2026, the Company completed the sale of its Vertica business to Rocket Software"] and the eDOCS business was sold [10-Q-Sep26 page:39 — "On January 12, 2026, the Company completed the sale of its eDOCS business to NetDocuments Software, Inc."]. Both are reported within income from operations until sale, not as discontinued operations, so FY2026 quarterly periods carry the divested results to different dates.

### Evidence by downstream demand

| Evidence demand | Located source evidence | Limitation carried forward |
| --- | --- | --- |
| Statements, discrete quarters, year-to-date and fiscal years | Income statements, balance sheets and cash flows in all four periodic reports; the latest quarter is in [10-Q-Sep26 page:3 — "Total revenues 1,236,634 1,288,135"]; the 10-K carries multi-year data | Q4 FY2026 discrete figures come from the release, and the filings give year-to-date totals for the December and March quarters, so discrete quarters need downstream derivation; none is derived here |
| Debt by facility | Principal by instrument at period end [10-Q-Sep26 page:16 — "Total principal payments due 5,827,563 5,836,525"], prior year-end in [10-K page:268 — "Total principal payments due 5,836,525 6,485,375"], and the December and March balances [10-Q-Dec25 page:19 — "Total principal payments due 6,467,450 6,485,375"] and [10-Q-Mar26 page:20 — "Total principal payments due 6,295,488 6,485,375"] | Unamortized discount and issuance costs are given in aggregate, not by facility, so facility-level carrying values are not supplied |
| Covenants and liquidity | The revolver test and compliance statement [10-Q-Sep26 page:19 — "we must maintain a “consolidated net leverage” ratio of no more than 4.50:1.00 at the end of each financial quarter"], [10-Q-Sep26 page:19 — "As of September 30, 2026, we are in compliance with the consolidated net leverage ratio."], and the undrawn position [10-Q-Sep26 page:19 — "As of September 30, 2026, we had no outstanding balance under the Revolver (June 30, 2026—nil)."] | The covenant ratio value and the covenant EBITDA are not printed in any filing; see the conflict and gap entries |
| Cash-paid interest and tax | [10-Q-Sep26 page:42 — "Cash paid during the period for interest $ 57,917 $ 79,500"]; annual [10-K page:306 — "Cash paid during the period for interest $ 321,694 $ 352,383 $ 533,866"] | Quarterly supplements are year-to-date in the December and March reports |
| Adjusted EBITDA and add-backs | Reconciliations in the release [PR-Nov26 page:15 — "Adjusted EBITDA $ 442,432"] and in the 10-Q segment note [10-Q-Sep26 page:40 — "The CODM uses these measures while deciding how to allocate resources"]; prior quarters in PR-May26 and PR-Aug26 | Adjusted EBITDA is a non-GAAP measure defined by the issuer and is not the covenant definition |
| Segments and KPIs | A single industry segment [10-Q-Sep26 page:40 — "Our operations are analyzed by the CODM as being part of a single industry segment"], with revenue by type and by product category [10-Q-Sep26 page:9 — "Total Revenues by Product Categories"], plus net renewal rates in MD&A | Only revenue-type and product-category breakdowns exist; no segment profit beyond the consolidated measure |
| Business and transaction narrative | 10-K Item 1 and Item 7; strategy, restructuring plan and enterprise assessment in MD&A | Management characterisations only; no independent source |
| Subsequent events and cutoff | Note 24 in the latest 10-Q and the latest release | Filed on the cutoff date; nothing later is supplied |

### Conflicts and comparability breaks

1. Product-category restatement. The latest 10-Q reclassified categories and restated the comparative quarter [10-Q-Sep26 page:9 — "Prior period amounts have been reclassified to conform to the current period presentation."]. The bridge shows the prior presentation and the effect [10-Q-Sep26 page:9 — "Cybersecurity (Enterprise) 180,747 (71,410) 109,337"]. Earlier filings and releases therefore show product-category revenue on the old basis. Both bases are retained; neither controls the other. Downstream effect: product-category trends across PR-May26, PR-Aug26 and the latest quarter are not comparable without the bridge, and the bridge covers only the Q1 FY2026 quarter.
2. Net leverage. The only stated ratio is a management statement [PR-Nov26 page:3 — "Our net leverage ratio is 2.55x as of September 30, 2026."]. The covenant is defined differently in the filing (total debt less unrestricted cash, including guarantees and letters of credit, over trailing-twelve-month adjusted earnings before interest, taxes, depreciation, amortization, restructuring, share-based compensation and other charges). The release does not state its definition or inputs. This is a definitional gap rather than a numerical conflict; it must not be presented as the covenant ratio. A management claim does not override the filing, which states only compliance.
3. Debt at the cutoff versus debt at period end. The balance sheet debt is as of September 30, 2026, while the same report records an October 2026 refinancing: [10-Q-Sep26 page:43 — "On October 1, 2026, the Company issued $500 million in aggregate principal amount of 6.70% senior secured notes due 2031"] and [10-Q-Sep26 page:44 — "On October 2, 2026, the Company purchased and cancelled $300.0 million of the aggregate outstanding principal amount of the Senior Notes 2028"]. The contractual-obligation table states it excludes these events [10-Q-Sep26 page:84 — "The information presented herein does not give effect to the issuance of the Senior Secured Notes 2031"]. The release states the same events [PR-Nov26 page:3 — "In October, OpenText completed a $1.0 billion senior secured notes offering"]. The documents are consistent with each other; the consequence is that two debt registers (period end and pro forma for the subsequent events) are needed and must be labelled.
4. Revolver maturity. The period-end filing describes the revolver as maturing in December 2028 and then records an amendment on October 1, 2026 extending it, subject to conditions [10-Q-Sep26 page:44 — "extend its maturity from December 19, 2028 to October 1, 2031, subject to certain conditions"]. Both are retained as dated facts.
5. Rounding. Release headlines are in millions and release tables in thousands; the filings are in thousands. Differences of that kind are rounding, not conflicts.

### Subsequent events and cutoff check

All seven sources are dated on or before the 2026-11-05 cutoff. Post-quarter facts in the latest report are subsequent events, kept separate from period-end balances. The dividend declared on November 3, 2026, with record date December 4, 2026 and payment date December 18, 2026, is a future contract term, labelled as such. The release also announces an investor day on February 10, 2027, a future event that is not evidence.

### Consumer assessment

| Consumer | Status | Evidence demand and carried limitations | Command sheet |
| --- | --- | --- | --- |
| CP-1 (financial base) | READY_WITH_LIMITATIONS | Statements, debt table, covenant text, cash flow supplements, adjusted EBITDA reconciliations all located. Limits: no covenant ratio value or covenant EBITDA, facility-level carrying values absent, quarterly cash-paid items are year-to-date for two quarters, period-end versus October 2026 debt must be separated | RUN |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, strategy, history (acquisition financing, divestitures, restructuring plan, enterprise assessment) located in the 10-K and MD&A. Limits: management language only, no investor presentation or call transcript supplied, no ownership data beyond listed equity, no sponsor | RUN |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Sources adequate for the synthesis; it uses upstream registers only. Carries every CP-1 and CP-1A limitation, including absent ratings and absent third-party views | RUN after CP-1 and CP-1A |
| CP-5 (evidence trace validator) | READY_WITH_LIMITATIONS | Pinned filings allow quote and figure tracing. Limit: the pack has no independent third-party evidence, so cross-checking is within one issuer's documents | RUN last |

### Model objective source sufficiency

For the report's chart and model strip, the pack supplies discrete-quarter evidence for Q1 FY2027, Q3 FY2026 and Q2 FY2026 in the periodic reports and for Q4 FY2026 in the release; fiscal years FY2026, FY2025 and FY2024 for income and cash flow in the 10-K; add-back reconciliations; revenue by type and product category; instrument-level principal; cash-paid interest and tax; and business narrative. Gaps for that use: facility-level carrying values, covenant EBITDA, and a Q1 FY2026 original filing. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No normalized quarters, reconciliation or input acceptance is asserted.

## Calculations

No new calculation is performed in CP-0. Figures shown above are quoted from the sources inside citations, unchanged, and none is derived. The only counts are coverage counts: 311 of 311 chunks for the annual report, 100 of 100, 105 of 105 and 90 of 90 for the three quarterly reports, and 28 of 28, 31 of 31 and 20 of 20 for the three releases, which is 685 of 685 chunks. A chunk count establishes extraction completeness only; it is not a readiness proxy and does not show fidelity.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed financing documents (indentures, credit agreement and amendments, security and pledge agreements) are not supplied; the 10-K exhibit list names agreements, for example [10-K page:224 — "Restated Security and Pledge Agreement, dated as of December 16, 2013"], but only filing summaries are available. Context states legal documents as none | Medium | CP-1, CP-2, CP-5 | Obtain the filed exhibits if covenant definitions, baskets or guarantor terms are needed; otherwise use filing summaries and label them as such |
| Covenant ratio value and covenant-defined earnings are not printed in any supplied filing; only compliance is stated. The management ratio in the release lacks a definition | Medium | CP-1, CP-2 | Treat management ratio as an attributed claim; do not present headroom as filed fact |
| Credit ratings are not supplied (the context ratings list is empty; the 10-K mentions ratings only generically in risk factors [10-K page:64 — "credit ratings of our outstanding debt securities could lead to losses for shareholders and debt holders"]) | Medium | CP-1A, CP-2 | Obtain agency reports if ratings are needed; otherwise mark Not supplied |
| Letters of credit and guarantees are described only generically [10-Q-Sep26 page:29 — "guarantees relating to taxes and letters of credit on behalf of parties with whom we conduct business"]; no amount, and no statement of revolver capacity used, was found after searching for letters of credit, standby and bank guarantee wording | Medium | CP-1 (liquidity) | Revolver availability can be stated only as undrawn commitment, with the letters-of-credit effect Not supplied |
| Guarantor and non-guarantor financial information and the restricted or unrestricted split were not found (searched for guarantor financial information and summarized financial wording) | Medium | CP-1, CP-2 | Structural position analysis must label this as not assessable |
| Facility-level carrying values not supplied; only aggregate unamortized discount and issuance costs, plus per-facility principal and effective-rate narrative | Low | CP-1 | Use principal by facility and label carrying value as aggregate |
| Original Q1 FY2026 10-Q and release, and the Q2 FY2026 release, were not supplied; Q1 FY2026 appears only as a comparative (on the new product-category basis for categories) | Low | CP-1 | Use comparative columns and label basis |
| Discrete Q4 FY2026 and quarterly cash flows must be taken from the release or derived downstream from year-to-date data | Low | CP-1 | Derive with shown inputs, or cite the release |
| No investor presentation, call transcript or slide deck supplied; the release says one was posted on the company website but it is not in the pack. No slide coverage is claimed | Low | CP-1A | Use management language from the releases and MD&A, attributed |
| Non-text content (charts, images, hyperlinks, XBRL) was not extracted; extraction fidelity of tables was not independently reviewed. Source quality and extraction status are distinct | Low | All | Spot-check figures against the filings when cited |
| Currency and unit: the filings are in USD thousands and the release headlines in USD millions; the reporting currency matches the context (USD). Foreign-currency exposure is disclosed (revenue and expense currency mix in the release) but is not a unit problem | Info | All | Keep units explicit |
| Post-cutoff information (anything after November 5, 2026) is not in the pack and none was used | Info | All | None |

## Next module

Proceed to CP-1 (financial base), then CP-1A (business and transaction context), then CP-2 (credit synthesis), then CP-5 (evidence trace) last. Instruct CP-1 to keep period-end debt (September 30, 2026) and post-quarter debt (October 2026 refinancing) as separate labelled registers, to treat the management net leverage statement as attributed and not as the covenant ratio, to state revolver availability as undrawn commitment with letters of credit Not supplied, to label the product-category basis, and to carry the perimeter changes from the Vertica and eDOCS sales into any period comparison. Next evidence action if ratings, covenant detail or guarantor structure are wanted: obtain the executed financing exhibits and agency reports, which are outside this pack.
