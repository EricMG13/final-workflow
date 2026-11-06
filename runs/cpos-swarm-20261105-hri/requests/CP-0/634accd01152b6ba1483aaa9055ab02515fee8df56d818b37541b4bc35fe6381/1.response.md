## Request

Issuer: HERC HOLDINGS INC (issuer id hri; ticker HRI; Delaware registrant, Commission File Number 001-33139). As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency per the run context: USD; every supplied filing reports in US dollars, in millions except per-share data. Current period per the context: Q3 2026 (quarter ended 2026-09-30); prior period: FY2025.

Question answered by this handoff: can the supplied source set support the selected downstream modules (CP-1, CP-1A, CP-2, CP-5) and the HTML model and report sections CP-OS lists for this run, and what remains blocked or limited. This is a source-sufficiency review. It gives no credit conclusion, makes no legal interpretation and does not normalize, reconcile or calculate financial figures. Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

## Sources

### Issuer sources relied on

All seven sources are text extractions (page chunks, `page:N`) of filed SEC documents. The `Visible text` header inside each extraction carries the sha256 of the original HTML; the sha256 below is that of the pinned extraction file.

| Source (exact name) | sha256 (pinned file) | Family and authority | Period or date | Pages retained |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_hri-20251231.htm.jsonl | 1e4fc8e6ec5ecb19b2d87edd4dd39a4f8c262f1bbf4300e6c71728880e6a40f2 | Annual report on Form 10-K, audited, filed document (signed February 17, 2026, page:142) | FY2025 (year ended December 31, 2025) | 142 of 142 |
| 10-Q_2026-03-31_hri-20260331.htm.jsonl | 957fad2e7bcc77d998a4d47ace97dbbe723d0ae0ec8bb0e66ef9b0a24106db4a | Quarterly report on Form 10-Q, unaudited (signed April 28, 2026, page:37) | Q1 2026 (quarter ended March 31, 2026) | 37 of 37 |
| 10-Q_2026-06-30_hri-20260630.htm.jsonl | e3f28b820e10e5baa7e77b727c26f2b087fc86a20a6ecf0c0005cebe89eab4df | Quarterly report on Form 10-Q, unaudited (signed July 28, 2026, page:37) | Q2 2026 and six months 2026 | 37 of 37 |
| 10-Q_2026-09-30_hri-20260930.htm.jsonl | b4f098a700c1a9ded56e8016e540343e20a52efa45a322a642b6b1a64bf553ce | Quarterly report on Form 10-Q, unaudited (signed October 27, 2026, page:36) | Q3 2026 and nine months 2026 | 37 of 37 |
| EX-99.1_2026-04-28_herc2026q1-pressrelease.htm.jsonl | 6727d6749dee62dba3ecdf247326c2640487c30ff4e58831034efb2c2e6000e2 | Earnings release (Exhibit 99.1), issuer-attributed, with non-GAAP schedules | Q1 2026, dated April 28, 2026 | 10 of 10 |
| EX-99.1_2026-07-28_herc2026q2-pressrelease.htm.jsonl | 0768981a704e5281116cd18bf157f1264a3d3fbf5f9bb078071dab4e27ecc390 | Earnings release (Exhibit 99.1), issuer-attributed, with non-GAAP schedules | Q2 2026, dated July 28, 2026 | 11 of 11 |
| EX-99.1_2026-10-27_herc2026q3-pressrelease.htm.jsonl | aa1bf8bfd1f475ff27dc8e4345039b652970320635f5a3f0648d622e08bd7d29 | Earnings release (Exhibit 99.1), issuer-attributed, with non-GAAP schedules | Q3 2026, dated October 27, 2026 | 11 of 11 |

Run context (not issuer evidence): context sha256 5d9781ebccde905b27f5dd6b19356b8d3ac042aedfacbbb25d2f4ac0a0fab2ab, file 1364479-herc-holdings-inc-hri.json. It sets the dates, currency and pathway above. Its blank fields (borrower, parent, guarantors, ratings, quotes, deal terms, valuation inputs, research questions, legal documents "none") are blank, not zero.

The pack file `_retrieval.json` is ignored by CP-OS and is not used.

### Supplied handoffs

None. CP-0 is the first module of this run; no upstream handoff exists to consume.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents cover the annual report, all three 2026 quarterly reports and all three 2026 earnings releases for one consolidated issuer, with debt, liquidity and covenant text. They support the next four modules with bounded limitations. | Medium | No executed credit agreements or indentures, no fourth-quarter 2025 release, and no proxy statement are supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Financial statements, debt notes, availability tables and covenant text are present for each 2026 quarter and for year-end 2025. | Debt, liquidity and cash-interest work can proceed from filed statements without relying on management slides. | High |
| Adjusted EBITDA for the full year 2025 and the pro forma trailing leverage basis are not supplied in the pack. | A trailing adjusted EBITDA and the reported net leverage cannot be rebuilt from these sources alone. | High |
| Springing fixed charge coverage trigger levels and borrowing base mechanics are described only in general terms, and no executed legal documents are supplied. | Covenant headroom and collateral availability can be reported as disclosed but not tested against contract text. | High |
| Ownership, governance and executive pay sit in a proxy statement that is not supplied. | Ownership and governance facts will be limited to what the filings state. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for the selected work. Every document is a filed SEC report or an Exhibit 99.1 issuer earnings release, so original authority for financial facts rests with the 10-K and the three 10-Qs, and the earnings releases are attributed management material that supports, and cannot override, the filings. All seven extractions are complete by page count (285 of 285 pages) and the pages read for this review (the statements, debt notes, liquidity and covenant sections, exhibit lists, and every release schedule) contained what their tables of contents promise; pages of narrative risk factors and other notes were located but not read in full. A successful text extraction is not a fidelity review: tables were read as text and no image, chart or slide content is retained in the pack, so no claim about charts or presentation slides is made. Nothing in the pack is dated after the 2026-11-05 cutoff; the latest items are the third-quarter 10-Q and release dated October 27, 2026. No conflict between filings was found that blocks a consumer (see the conflict log), and no source needs to be excluded.

The strongest contrary evidence is about what is missing, not what is present. The pack has no fourth-quarter 2025 earnings release and the 10-K carries no non-GAAP reconciliation, so adjusted EBITDA for the fourth quarter and for FY2025 is not sourced; the releases state net leverage on a basis that adds H&E's standalone pre-acquisition results, which are not supplied in a form that can be rebuilt. Executed legal documents are named only in exhibit lists (incorporated by reference), so covenant, guarantee and collateral terms rest on the filings' own descriptions. The proxy statement that carries Part III is incorporated by reference and not supplied. Because the company states one reportable segment and one entity-level financial statement set, there is no segment table to supply.

What can proceed: CP-1 (financial extraction for FY2025, Q1, Q2 and Q3 2026, six and nine months, and the year-end and quarter-end balance sheets), CP-1A (business, acquisition and operating model), CP-2 (synthesis from upstream registers) and CP-5 (trace validation of the run). What cannot proceed from this pack: a reproduction of the reported pro forma net leverage, a fourth-quarter 2025 discrete adjusted EBITDA, and any contract-level covenant or intercreditor test. Next evidence action: if the committee needs those, add the fourth-quarter 2025 earnings release, the 2026 proxy statement, and the ABL, term loan and indenture documents named in the exhibit lists.

### Source-by-source assessment

| Source | Entity and perimeter | Basis and currency | Version relation | Retained evidence of note | Extraction limits |
| --- | --- | --- | --- | --- | --- |
| 10-K FY2025 | Herc Holdings Inc. and subsidiaries, consolidated | US GAAP, USD millions, audited (auditor report page:73) | Base annual report; the only audited source | Debt Note 11 (page:103-118), maturities (page:103-104), leases (page:103), pension (page:119-120), pro forma H&E data (page:99), cash paid for interest and tax (page:81) | Text only; Part III by reference to a proxy not supplied (page:2) |
| 10-Q Q1 2026 | Same consolidated perimeter | US GAAP, USD millions, unaudited | Separate period, not superseded by later 10-Qs | Statements, Note 8 debt (page:17), availability (page:20), covenants in MD&A | Text only |
| 10-Q Q2 2026 | Same | US GAAP, USD millions, unaudited, three and six months | Separate period | Note 8 debt (page:16), availability (page:17), cash paid for interest (page:6) | Text only |
| 10-Q Q3 2026 | Same | US GAAP, USD millions, unaudited, three and nine months | Latest filed report; comparatives for 2025 periods | Balance sheet (page:3-4), operations (page:4), cash flows (page:5-7), Note 8 debt (page:17-18), availability (page:18-19), fair value of debt (page:21), covenants (page:33) | Text only; no maturity table by year (the 10-K carries the year-end schedule) |
| Release Q1 2026 | Herc Holdings Inc. and subsidiaries | Non-GAAP schedules, USD millions, quarter and prior-year quarter | Attributed management material; filings control | Adjusted EBITDA reconciliation (page:7), free cash flow (page:9), leverage and liquidity text (page:3), outlook (page:3) | Net leverage on pro forma basis |
| Release Q2 2026 | Same | Quarter and six months | Same | Reconciliation (page:8), free cash flow (page:11), leverage (page:3), raised outlook (page:4) | Same |
| Release Q3 2026 | Same | Quarter and nine months | Same | Reconciliation (page:9), adjusted net income (page:10), free cash flow (page:11), leverage, liquidity and raised outlook (page:4), operating measure definitions (page:5) | Same |

### Entity and perimeter

| Role | Evidence | Status |
| --- | --- | --- |
| Registrant, party to the Senior Notes indentures, Term Loan Facility borrower and ABL borrower group member | Herc Holdings Inc. is the registrant (10-Q Q3 2026, page:1). The indenture exhibits are among Herc Holdings Inc., guarantors and the trustee; the June 2, 2025 indenture also names Herc Holdings Escrow, Inc. (10-K, page:136). The ABL agreement is among Herc Holdings Inc., Herc Rentals Inc., Matthews Equipment Limited and others (10-K, page:114 and page:137). | Documentary, from filings |
| Operating subsidiary | Herc Rentals Inc. ("Herc"); "The Company conducts substantially all of its operations through subsidiaries, including Herc Rentals Inc." (10-Q Q3 2026, page:7) | Documentary |
| Guarantors | Term Loan: each existing and future direct or indirect U.S. subsidiary, with exceptions including securitization subsidiaries (10-K, page:116). ABL: U.S. and Canadian subsidiaries, with exceptions (10-K, page:114). The guarantee scope for each series of Senior Notes was not read in executed form. | Described in filing; executed documents not supplied |
| Special-purpose entity | Herc Receivables U.S. LLC, a consolidated wholly-owned SPE for the AR Facility; its assets are not available to other creditors (10-K, page:117; 10-Q Q3 2026, page:32) | Documentary |
| Holdings versus Herc | The 10-Q states Herc Holdings' balance sheet is substantially identical to Herc's except for debt held at Herc Holdings (Notes, Term Loan Facility and ABL Credit Facility) and certain equity components, and the statements of operations are identical except interest on that debt (10-Q Q3 2026, page:33). | Documentary; separate Herc-only statements are not supplied |
| Parent, sponsor, borrower distinct from registrant | None named in the context or found; the issuer has listed equity | Not applicable |
| Restricted versus unrestricted entities | Not described in the sources read; the indenture covenants are described as applying to the Company "and its restricted subsidiaries" (10-K, page:105) | Open as a gap |

### Coverage against the HTML model objective

This table assesses source evidence only. It does not claim normalized quarters, reconciliation or acceptance by the model contract.

| Evidence need | Located in | Coverage |
| --- | --- | --- |
| Discrete quarters, 2026 | Q1 10-Q and release; Q2 10-Q and release (three months columns); Q3 10-Q and release | Present for Q1, Q2 and Q3 2026 with prior-year quarter comparatives |
| Year-to-date versus quarter | Six months in the Q2 10-Q; nine months in the Q3 10-Q and release | Present; period labels must be kept apart in downstream tables |
| Fiscal years | 10-K statements for 2025 with 2024 and 2023 comparatives (cash paid for interest page:81) | Present for FY2025 and earlier years shown in the 10-K |
| Discrete fourth quarter 2025 | No fourth-quarter 2025 release or 10-Q exists for it | Not directly supplied; a derivation from FY2025 and nine months 2025 comparatives would be a downstream calculation |
| Segments | One operating and reportable segment: equipment rental (10-Q Q3 2026, page:23; 10-K Note 21, page:132) | Stated; no segment table exists |
| Add-backs | Adjusted EBITDA reconciliations in the three releases (Q3: page:9) | Present for 2026 quarters, six and nine months, and the 2025 comparatives; not present for FY2025 or Q4 2025 |
| KPIs | Dollar utilization, OEC, average fleet age, net rental capital expenditures (Q3 release, page:2-5) | Present in releases as management measures, with definitions (page:5) |
| Facility-level debt and carrying values | Debt tables with rate, maturity and amount by instrument (10-Q Q3 2026, page:17-18; 10-K, page:103); fair value by series (10-Q Q3 2026, page:21) | Present at year-end 2025 and each 2026 quarter-end |
| Maturity profile | Year-by-year schedule at December 31, 2025 only (10-K, page:103-104) | Present for year-end 2025; none for 2026 quarter-ends |
| Cash-paid interest and tax | Supplemental cash flow disclosure (10-Q Q3 2026, page:6; Q2 10-Q page:6; Q1 10-Q page:5; 10-K page:81) | Present as year-to-date figures; discrete-quarter amounts are a downstream difference |
| Business and transaction narrative | H&E acquisition note (10-Q Q3 2026, page:15-16; 10-K page:96-100), MD&A, release narrative | Present; the acquisition closed on June 2, 2025 |

### Consumer readiness

| Consumer | Status | Basis | Carried limitations |
| --- | --- | --- | --- |
| CP-1 (financial extraction) | READY_WITH_LIMITATIONS | Full statements, debt notes, availability, cash-paid interest and tax, and non-GAAP reconciliations for 2026 | FY2025 and Q4 2025 adjusted EBITDA not sourced; pro forma leverage basis not rebuildable; interim figures unaudited; maturity schedule only at year-end 2025 |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, H&E acquisition and financing, operating narrative in the 10-K, 10-Qs and releases | Ownership, control rights and governance detail sit in the unsupplied proxy statement; no sponsor |
| CP-2 (fundamental synthesis) | READY_WITH_LIMITATIONS | Source evidence suffices for the owner to run once CP-1 and CP-1A settle | Inherits every CP-1 and CP-1A limitation above; no ratings supplied |
| CP-5 (evidence trace validation) | READY_WITH_LIMITATIONS | All sources are retained with page-level locators for citation checks | Inherits all limitations; cannot verify contract text that is not supplied |

No consumer is CONDITIONAL or BLOCKED, so none is marked DO NOT RUN. Missing downstream analytical handoffs are not treated as source conditions.

### Conflict and discrepancy log

| Item | Locators | Downstream effect | Treatment |
| --- | --- | --- | --- |
| The 10-K debt table lists the AR Facility with maturity 2026, while the 10-K maturity schedule shows no amount labelled for it; the AR Facility is excluded from current maturities by intent and ability to refinance. | 10-K, page:103-104 and page:117 | CP-1 must not place the AR Facility in a maturity year without stating the basis. | Logged, not reconciled. The 10-Q for Q3 2026 later states the AR Facility maturity was extended to August 31, 2027 (page:18). |
| The AR Facility's stated maturity of August 31, 2027 falls within twelve months of the September 30, 2026 balance sheet date, yet it is shown within long-term debt. | 10-Q Q3 2026, page:17-18 | Liquidity and maturity-wall work must carry the filing's stated classification basis. | Logged as a disclosed classification, not a conflict between sources. |
| Releases give net leverage on a pro forma trailing basis including H&E standalone pre-acquisition results; the filings give no such leverage figure. | Q3 release, page:4; Q1 release, page:3; Q2 release, page:3 | A management-defined ratio cannot override figures derived from filings. | Logged; downstream modules label it attributed management data. |
| The quarterly releases and 10-Qs agree on the reported GAAP lines read for Q3 2026 (revenues, net income, interest expense, cash). | Q3 release page:7 and 10-Q page:4 | None | No conflict found on the lines read; this is not a full tie-out. |

## Calculations

No financial figure was calculated, normalized or reconciled in this module, by design. Page-coverage counts only:

| Item | Inputs | Result |
| --- | --- | --- |
| Pages retained | 142 (10-K) + 37 + 37 + 37 (three 10-Qs) + 10 + 11 + 11 (three releases) | 285 of 285 pages |
| Latest source date against cutoff | October 27, 2026 (Q3 10-Q signature and release) compared with 2026-11-05 | 9 days before the cutoff; no source after it |

## Gaps

| Gap | Severity | Affected consumers | Why it matters | Remediation |
| --- | --- | --- | --- | --- |
| No fourth-quarter 2025 earnings release; the 10-K has no non-GAAP reconciliation, so FY2025 and Q4 2025 adjusted EBITDA are Not supplied | Material | CP-1, CP-2, CP-5 | Trailing adjusted EBITDA and any leverage built on it cannot be sourced from the filings; Not calculable from this pack | Add the Q4 2025 release |
| Pro forma net leverage in the releases relies on H&E standalone pre-acquisition results that are not supplied; 10-K pro forma data (page:99) covers revenues and pretax income only | Material | CP-1, CP-2 | The management leverage ratio cannot be reproduced; it must be carried as attributed | Add H&E standalone filings or the release's pro forma bridge |
| Executed credit agreements, indentures, guarantee and collateral agreements are not supplied (exhibit lists only, 10-K page:136-137) | Material | CP-1, CP-2, CP-5 | Guarantor scope per series, borrowing base mechanics and the ABL springing trigger levels rest on filing descriptions; legal interpretation is out of scope | Add the documents named in the exhibit list |
| The ABL fixed charge coverage trigger ("certain levels" of liquidity or excess availability) is not quantified in the filings | Material | CP-1, CP-2 | Covenant headroom against the trigger is Not calculable | Add the executed ABL agreement |
| Proxy statement (Part III) not supplied | Minor | CP-1A, CP-2 | Ownership, control and governance detail unavailable; not inferable | Add the 2026 proxy statement |
| Maturity schedule by year only at December 31, 2025 | Minor | CP-1 | 2026 quarter-end maturity walls need a roll-forward from disclosed amendments and repayments | Treat as a downstream calculation with stated inputs |
| Separate Herc Rentals Inc. statements not supplied; the filing states Holdings and Herc are substantially identical except for the Holdings debt (10-Q Q3 2026, page:33) | Minor | CP-1, CP-2 | Perimeter between Holdings-level debt and operating-company cash flows is as described, not independently shown | None needed for the consolidated view |
| No credit ratings, market quotes or valuation inputs (context blank) | Minor | CP-2 | Market and rating views are outside this pack and must not be invented | Supply if wanted |
| Interim periods are unaudited; no image, chart or slide content is retained | Minor | CP-1, CP-5 | Fidelity of text tables was not independently reviewed | None |

## Next module

Proceed to CP-1 (financial extraction). Inputs for it: the three 2026 10-Qs and the 10-K for statements and debt notes, the three releases for non-GAAP schedules and management measures. Carry forward: label every figure by period (Q3 2026, nine months 2026, FY2025, year-end 2025); keep the AR Facility classification basis; do not present the pro forma net leverage as filing-derived; treat FY2025 and Q4 2025 adjusted EBITDA, the springing covenant trigger levels and executed legal terms as Not supplied.
