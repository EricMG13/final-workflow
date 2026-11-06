# CP-0 - Source readiness: Clear Channel Outdoor Holdings, Inc. (cco)

## Request

- Issuer: Clear Channel Outdoor Holdings, Inc. (issuer id `cco`, NYSE: CCO), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q2 2026; prior period FY2025 (context).
- Run: `cco-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Requested downstream modules: CP-1, CP-1A, CP-2 and CP-5 (the `minimum` set).
- Execution: host session. The host read the pinned source text and wrote this answer; no provider was called.
- Question: can the seven pinned filings and releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion. No figure is normalized or reconciled here. Locators are `page:N` chunks of the pinned `.jsonl` text, not printed page numbers.
- Reading depth, stated plainly: the Q2 2026 10-Q and the Q2 2026 release were read in full. For the other five sources the statements, debt, liquidity, covenant, segment, discontinued-operation, commitment, subsequent-event and exhibit-list pages were read; the remaining pages (for example risk factors and business description in the annual report) were located by their contents index and sampled, not read line by line. Extraction status is not a fidelity review.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Pages | Role |
| --- | --- | --- | --- |
| 10-K_2025-12-31_cco-20251231.htm.jsonl | 571124584b3bbe99a4fbff8adfaba5f0fb8933c5a0003d1ef35708c36c286d39 | 145 | Annual report, fiscal year ended December 31, 2025, filed February 26, 2026 (audit report signed February 26, 2026) |
| 10-Q_2025-09-30_cco-20250930.htm.jsonl | 607e09a97951d1ad4c47649541e08f4b1e6c417cc3bd1376061667bd020f7126 | 48 | Quarterly report, quarter ended September 30, 2025 |
| 10-Q_2026-03-31_cco-20260331.htm.jsonl | a3ad502aa08b83254f97c12e4f79050207a26c6003570b7bd60e33a1124d566c | 36 | Quarterly report, quarter ended March 31, 2026 |
| 10-Q_2026-06-30_cco-20260630.htm.jsonl | fc57da6e0f4d7240050e6201742116917e571f4d11e190fcdcea84112429a51c | 39 | Quarterly report, quarter ended June 30, 2026, signed August 5, 2026 |
| EX-99.1_2026-02-26_exhibit991-ccohearningsrel.htm.jsonl | 5cc1d0e97fcf82997c8a6a84c737a99df944d52765b5ff540d0441e7f806a5a6 | 16 | Earnings release, fourth quarter and full year 2025, dated February 26, 2026 |
| EX-99.1_2026-05-06_exhibit991-ccohearningsrel.htm.jsonl | d85dec563195c10f63eb072d829bbf7b6a81552ec09b651fb1bdefa50ffbbbd6 | 12 | Earnings release, first quarter 2026, dated May 6, 2026 |
| EX-99.1_2026-08-05_exhibit991-ccohearningsrel.htm.jsonl | 86540d4f0d27c129f16354d25b76c67a8e72d707aa0c050724d976a7c4c17aa5 | 12 | Earnings release, second quarter 2026, dated August 5, 2026 |

### Run settings (not issuer evidence)

| Source | sha256 | Role |
| --- | --- | --- |
| context | de960bbc410d3388b8cf7496a6e161733b9fd5ffc09b25a54e06ffd5d05f0294 | User run settings. Ratings, quotes, deal terms, peers and research questions are blank; blank is not zero. `legal_documents` is "none". |

### Supplied handoffs

None. CP-0 is the first module in this run, so no upstream handoff exists.

### Excluded file

`_retrieval.json` is listed by CP-OS as ignored. It is harness metadata, not issuer evidence, and nothing below relies on it.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough to build the financial, business and trace work for the four requested modules, with limits. Nothing after August 5, 2026 is supplied. | Medium | The merger and debt actions pending at the latest filing have no later evidence. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual statements, three quarterly reports and three releases cover every quarter from the first quarter of 2025 to the second quarter of 2026 on one continuing-operations basis. | Supports quarterly and trailing-twelve-month work from filed figures. | Medium |
| The pending take-private merger and the related debt amendments were still pending at the latest filing. No source says whether the merger closed. | Debt treatment at closing, including redemption of unsecured notes, cannot be confirmed. | High |
| The executed indentures, credit agreements, merger agreement and amendments are cited by exhibit lists but not supplied. | Legal terms rest on the issuer's own summaries, so covenant definitions cannot be checked. | High |
| The guarantor group is described only as certain domestic subsidiaries, with no list or guarantor financials. | Structural subordination and guarantor coverage cannot be assessed from these sources. | Medium |

### Readiness view

The effective source set can support CP-1, CP-1A, CP-2 and CP-5 with bounded limitations, so each consumer is READY_WITH_LIMITATIONS and none is CONDITIONAL or BLOCKED. The limitations are about what happened after the latest supplied filing and about legal documents that are only summarised, not about the quality of the financial statements. Source sufficiency is a statement about evidence, not a completed analysis, and it does not evaluate any CP-MODEL input contract.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 with FY2024 and FY2023 comparatives (10-K page:78, page:79, page:80), and unaudited interim statements to June 30, 2026 with comparatives (Q2 10-Q page:2 to page:6). Debt, liquidity and cash interest are located. Limitation: text extraction flattens tables; no original XBRL is supplied. |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, disposition history and the merger are located (10-K page:4, page:5; Q2 10-Q page:8, page:9, page:22). Limitation: the Merger Agreement, merger proxy and financing documents are not supplied, and nothing after August 5, 2026 is supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Synthesis can rest on CP-1 and CP-1A plus the located debt, covenant, lease and liquidity text. Limitation: guarantor detail, executed covenant definitions and post-merger capital structure are not supplied. |
| CP-5 | READY_WITH_LIMITATIONS | Every claim can be traced to a page chunk of a filed document. Limitation: only text extractions are supplied, so table layout cannot be checked against the filed HTML or XBRL. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Information-availability boundary

- The latest supplied documents are dated August 5, 2026: the Q2 10-Q ("Date: August 5, 2026", page:39) and the Q2 release ("August 5, 2026", page:1).
- The window from August 6, 2026 to the cutoff of November 5, 2026 is not covered. Anything that happened in that window is Not supplied, not absent. This matters because the 10-Q states the merger "is expected to close by the end of the third quarter of 2026" (page:8), and the Spain sale closed on August 4, 2026, one day before the filing (page:9).
- No document for the quarter ended September 30, 2026 is supplied. The latest balance sheet date is June 30, 2026.
- Current period per context is q2-2026; the supplied set matches it. The prior period fy-2025 is matched by the 10-K.

### Source register

#### Form 10-K, fiscal year 2025 (10-K_2025-12-31_cco-20251231.htm.jsonl)

- Family and authority: filed annual report, original authority for audited consolidated statements. page:1 "FORM 10-K"; "FOR THE FISCAL YEAR ENDED DECEMBER 31, 2025"; Commission File Number 001-32663.
- Audit: page:75 auditor's report, signed Ernst & Young LLP, San Antonio, February 26, 2026 (page:77); one critical audit matter, goodwill valuation of the America and Airports reporting units (page:76).
- Statements: balance sheet page:77 and page:78; income statement page:78 (three years); cash flows page:79 and page:80; cash paid for interest and taxes page:80.
- Notes located: dispositions and discontinued operations page:93; segments page:98 to page:100; revenue page:100; long-term debt page:100 to page:117 (debt table page:100 and page:101, notes and facilities page:104 to page:116, maturities page:116 and page:117); leases page:117; commitments and contingencies page:118; asset retirement obligations page:125; subsequent events page:131.
- MD&A: liquidity and capital resources from page:62 (debt service and cash on hand page:66); credit-facility availability table page:68; debt covenants page:70.
- Units: thousands of USD in statements ("(In thousands, except per share data)", page:78); MD&A text in millions.
- Perimeter: Clear Channel Outdoor Holdings, Inc. and subsidiaries, consolidated, including noncontrolling interests. Spain is a discontinued operation held for sale at year end; the former Europe-North segment and Latin American businesses (sold in 2025) are also in discontinued operations (page:4; Q2 10-Q page:7).
- Version relationship: the Part III items are "incorporated by reference from our Form 10-K/A" (page:135, page:136). That amendment is not supplied, so executive pay, ownership and related-party detail are Not supplied.
- Wording difference carried forward: the 10-K describes the buyer as an investor consortium of Mubadala Capital "in partnership with TWG Global" (page:4); the Q2 10-Q and Q2 release name Mubadala Capital funds without that phrase (Q2 10-Q page:8). This is a description difference, not a conflict of fact.

#### Form 10-Q, quarter ended September 30, 2025 (10-Q_2025-09-30_cco-20250930.htm.jsonl)

- Family and authority: filed unaudited interim report. Gives the third-quarter 2025 and nine-month 2025 and 2024 income statements (page:3), segment data (page:13), Spain sale agreement (page:9, "approximately €115 million"), the Brazil sale on October 1, 2025 (page:9, page:10), letters of credit and availability (page:20) and cash (page:40).
- Role: the only source for the third quarter 2025 three-month columns. The fourth quarter of 2025 is given in the February 2026 release (page:1), and the annual figure is in the 10-K, so a discrete third-quarter and fourth-quarter 2025 series can be located without a derived residual for revenue.
- Perimeter at that date: Brazil was still within discontinued operations as an asset held until its October 1, 2025 sale (page:10). It is superseded in time by the 10-K, which controls for December 31, 2025.

#### Form 10-Q, quarter ended March 31, 2026 (10-Q_2026-03-31_cco-20260331.htm.jsonl)

- Family and authority: filed unaudited interim report. First-quarter 2026 and 2025 income statement (page:3), discontinued operations (page:9), segments (page:11), letters of credit and the April 2026 consent solicitation as a subsequent event (page:15), credit-facility availability (page:30).
- Role: the only filed source for the first-quarter 2025 comparative columns on the current continuing-operations basis.

#### Form 10-Q, quarter ended June 30, 2026 (10-Q_2026-06-30_cco-20260630.htm.jsonl)

- Family and authority: filed unaudited interim report, the latest and controlling source for June 30, 2026 balances and the three and six months ended June 30, 2026 and 2025. Cover page:1; signature "Date: August 5, 2026" (page:39).
- Statements: balance sheet page:2 and page:3; income statement page:3; cash flows page:5 and page:6 (six months only; discontinued-operation cash flows are included and not separately presented, page:7 and page:8).
- Notes: basis of presentation and pending merger page:7 to page:9; dispositions and discontinued operations page:9 to page:11; segments page:12 to page:14; revenue page:14 and page:15; long-term debt and merger-related debt actions page:15 to page:17; commitments and contingencies page:17.
- MD&A: page:21 onward; liquidity page:29 to page:33; credit facilities table page:33 and page:34; debt covenants page:34.
- Units: thousands of USD in statements; credit-facility table in millions (page:33).
- Exhibit list page:38 and page:39 cites supplemental indentures dated April 9, 2026, a Seventh Amendment to Credit Agreement dated April 10, 2026 and a Third Amendment to Credit Agreement dated May 15, 2026. Those documents are incorporated by reference and are not supplied.

#### Earnings releases, Exhibit 99.1 (three files)

- Family and authority: issuer-prepared, unaudited, furnished releases. They give attributed management narrative and the issuer's non-GAAP measures: Adjusted EBITDA, Adjusted Corporate expenses, FFO and AFFO, with reconciliations (Q2 release page:8 to page:10; Q4 release page:9).
- The Q2 release adds an issuer-computed net debt line in its debt table (page:6, "Net debt $ 4,915,491 $ 4,912,971") and the Q1 release does the same (page:5). Net debt and the non-GAAP measures are issuer presentations, not filed GAAP statements. The statements inside the releases duplicate the matching 10-Q or 10-K and do not corroborate them independently. Where a release and a filing differ in wording or scope, the filing controls.
- Each release says the company "is not providing financial guidance" because of the merger (Q2 release page:1; Q4 release page:1), so no management outlook exists in the supplied set.

### Identity and perimeter

- Reporting entity: Clear Channel Outdoor Holdings, Inc., a Delaware corporation (10-K page:1). It is the issuer of every note and the borrower under the senior secured credit facilities; the receivables-based facility has the company and certain subsidiaries as borrowers (10-K page:104, page:107).
- Subsidiary guarantors: the notes and facilities are guaranteed by "certain" wholly owned domestic subsidiaries (10-K page:108, page:110). No guarantor list, no guarantor or non-guarantor financial information and no restricted or unrestricted subsidiary split is supplied. The context leaves borrower, parent and guarantor fields blank, which is not evidence that none exist.
- Pending owner: Madison Parent Inc., with Madison Merger Sub Inc. merging into the company, which would survive as a wholly owned subsidiary of Parent; the buyer is described as affiliates and funds advised by Mubadala Capital (Q2 10-Q page:8). Parent and Merger Sub are counterparties to the merger, not obligors on the existing debt as far as the supplied text shows.
- Operating perimeter on the current basis: two reportable segments, America and Airports, with Singapore in Other (Q2 10-Q page:12). Substantially all continuing revenue is from the U.S. (Q2 10-Q page:14). Spain is held for sale as of June 30, 2026 and sold on August 4, 2026 (Q2 10-Q page:9).
- Currency: USD throughout. No other reporting currency is used for continuing operations; the Spain price was set in euros (10-K page:73 and 10-Q Q3 2025 page:9) and is a discontinued-operation item.

### Period and basis map

| Period | Where located | Basis and caution |
| --- | --- | --- |
| FY2025, FY2024, FY2023 | 10-K page:78 to page:80 | Audited, continuing operations, Spain in discontinued operations; segment data page:98 to page:100 |
| Q1 2025 and Q1 2026 | Q1 10-Q page:3, page:11; Q1 release | Unaudited; Q1 2025 appears only as a comparative column |
| Q2 2025 and Q2 2026, six months 2025 and 2026 | Q2 10-Q page:3, page:12, page:13; Q2 release page:1 | Unaudited; three-month and six-month columns must stay separate |
| Q3 2025, nine months 2025 | Q3 2025 10-Q page:3, page:13 | Unaudited; original presentation |
| Q4 2025 | Q4 release page:1, page:2 | Issuer release; the 10-K does not print a fourth-quarter column |
| Balance sheets | December 31, 2024 and 2025 (10-K page:77); June 30, 2026 (Q2 10-Q page:2); March 31, 2026 and September 30, 2025 in the matching 10-Qs | Dated point-in-time; September 30, 2026 is not supplied |
| Cash interest and taxes | 10-K page:80 (annual); Q2 10-Q page:6 (six months) | Includes discontinued operations in cash flows (Q2 10-Q page:7) |

### Debt, liquidity and covenant evidence located (no calculation)

- Instruments at June 30, 2026 (Q2 10-Q page:15): term loan facility due August 2028; 7.875% Senior Secured Notes due April 2030; 7.125% Senior Secured Notes due February 2031; 7.500% Senior Secured Notes due March 2033; 7.750% Senior Notes due April 2028; 7.500% Senior Notes due June 2029; finance leases; the receivables-based and revolving facilities are shown with no balance, both maturing June 2030.
- Facility availability at June 30, 2026 (Q2 10-Q page:33): revolving facility limit $100.0 million, receivables-based facility limit $200.0 million, letters of credit $7.0 million and $87.6 million, excess availability $93.0 million and $112.4 million. The revolver letter of credit related to Spain and "was canceled" on August 4, 2026 (page:34). The receivables-based limit is capped by a borrowing base (page:34).
- Maturity schedule at December 31, 2025 by year is printed (10-K page:117). A June 30, 2026 schedule is not printed; the Q2 10-Q says the next significant maturities are in 2028 (page:32).
- Springing covenant: first lien net leverage ratio of less than 7.10 to 1.00, applicable only if the revolver is drawn or undrawn letters of credit exceed $10 million; "these conditions were not met and the covenant was not in effect" at June 30, 2026 (Q2 10-Q page:34; 10-K page:109 for the full carve-outs). The reported ratio is therefore not presented. The receivables-based facility has a fixed charge coverage test that applies only in a Covenant Trigger Period (10-K page:106).
- Compliance: "the Company was in compliance with all covenants" at June 30, 2026 (Q2 10-Q page:16).
- Non-debt claims located: operating leases (10-K page:117, maturities table), non-lease non-cancelable contracts and capital expenditure commitments (10-K page:118), surety bonds and bank guarantees (Q2 10-Q page:16), asset retirement obligations (10-K page:125). A search for pension, retiree medical, factoring and supply-chain finance in the 10-K found no program of the issuer; the only pension reference is a reclassification of pension-related translation losses on sold businesses (10-K page:78). Treat these as not found in the supplied text, not as confirmed absent.

### Pending merger and debt actions at the latest filing

- Merger Agreement dated February 9, 2026, $2.43 per share in cash, stockholder approval on May 12, 2026, Hart-Scott-Rodino waiting period expired April 9, 2026, closing "expected to close by the end of the third quarter of 2026" subject to remaining conditions including review by the Committee on Foreign Investment in the United States (Q2 10-Q page:8, page:9).
- Termination fees: company pays Parent $39.8 million in specified circumstances; Parent pays the company $92.9 million in other circumstances (Q2 10-Q page:8).
- Debt documents: consent solicitations completed April and May 2026; supplemental indentures and amendments make the merger not a change of control; those for the senior secured notes and the Senior Secured Credit Agreement are "effective but will become operative only upon consummation of the Merger"; the receivables-based amendment becomes effective on consummation and would extend maturity to five years from closing and raise commitments from $200.0 million to $250.0 million (Q2 10-Q page:16, page:17).
- Conditional notices of redemption were issued for the 7.750% Senior Notes due 2028 and 7.500% Senior Notes due 2029, conditional on the merger closing (Q2 10-Q page:17).
- Spain sale: price approximately $132.3 million, completed August 4, 2026, net proceeds subject to adjustments and fees, intended to "further reduce our outstanding debt, subject to the outcome of the Merger" (Q2 10-Q page:22, page:33); completion and price are in Note 2 (page:9). The 10-K had expected closing in the first half of 2026 (page:4); the sale completed after that window.
- Consequence for readiness: the supplied set describes these events as pending. Any statement about the merger closing, notes redeemed, the receivables-based amendment taking effect or Spain proceeds applied to debt would be an inference, and downstream modules must label it Not supplied.

### Conflicts, differences and source-quality notes

| Item | Locators | Downstream effect |
| --- | --- | --- |
| Cash of $202.3 million in MD&A versus $192.1 million on the balance sheet | Q2 10-Q page:32 and page:2 | Not a conflict: MD&A includes $10.1 million held by discontinued operations in Spain (page:32, page:10). Use the labelled figure. |
| Credit-facility table totals differ by $0.1 million from the sum of its columns | Q2 10-Q page:33, footnote on page:34 "Due to rounding" | Presentation rounding only. Use facility-level figures. |
| Revenue mix between contracts with customers and leases shifts sharply year over year | Q2 10-Q page:14, page:15 (explained as changed contract terms, not a change in volume) | Do not use the mix as a trend in underlying business without the stated explanation. |
| Q4 2025 not printed in the 10-K | Q4 release page:1 | The discrete quarter comes from a release, not a filed statement. |
| Three-month and six-month 2025 columns are on a recast continuing basis | Q2 10-Q page:3, page:7 | Do not mix with pre-recast original reports. |
| Buyer description differs in wording | 10-K page:4; Q2 10-Q page:8 | Carry both wordings; do not resolve the TWG Global role from these sources. |
| 10-K said Spain sale expected in first half of 2026; it closed August 4, 2026 | 10-K page:4; Q2 10-Q page:9 | Timeline drift is a fact, not an error; no other conflict found. |

### Analytical read-through

- Usable coverage: the 10-K, three 10-Qs and three releases together cover audited FY2025, FY2024 and FY2023, every quarter from the first quarter of 2025 through the second quarter of 2026 on one continuing-operations basis, and the two segments, digital and total revenue, site lease expense, debt by instrument, facility availability, cash interest and the springing covenant.
- Strongest contrary evidence: the filings describe a take-private merger whose closing, debt amendments and note redemptions were all still pending on the last supplied date. The source risk is that the capital structure in the supplied balance sheet may not be the structure that exists at the cutoff. The downstream consequence is that leverage, interest burden and maturity profile are valid at June 30, 2026 only, and a user of CP-2 must not present them as the structure at the cutoff.
- Source risk mechanism, legal documents: the notes, credit agreements and their amendments are described only in the issuer's own notes and exhibit lists. The covenant and change-of-control mechanics therefore rest on management summary. The consequence is that CP-2 can report the stated covenant level and compliance statement but cannot test definitions, baskets or guarantor release terms.
- Source risk mechanism, guarantor perimeter: guarantors are "certain" domestic subsidiaries with no list. The consequence is that structural subordination and guarantor coverage cannot be assessed.
- What cannot proceed: any statement about events after August 5, 2026; document-level legal interpretation; guarantor-level analysis; a covenant headroom figure (the test was not in effect, so no ratio is printed); post-merger capital structure.
- Next evidence action: supply filings dated August 6, 2026 to November 5, 2026, including any report on the merger closing or termination, redemption of the senior unsecured notes, the quarter ended September 30, 2026 if filed by the cutoff, and the Form 10-K/A. Supply the indentures, the Senior Secured Credit Agreement with its seventh amendment, the receivables-based credit agreement with its third amendment, and the Merger Agreement, which the exhibit lists cite.

## Calculations

No new calculation is made; CP-0 does not normalize, reconcile or calculate figures. The checks below are coverage counts and footing checks of printed totals, shown with their inputs.

- Page chunks retained: 145 + 48 + 36 + 39 + 16 + 12 + 12 = 308 of 308 pages across the seven sources. Every page is retained text; none is an evidenced exclusion. Coverage of the document universe is not proven by this count.
- Debt table footing, June 30, 2026 (Q2 10-Q page:15), thousands of USD: 425,000 + 865,000 + 1,150,000 + 900,000 + 899,311 + 905,950 + 3,489 - 2,967 - 38,154 = 5,107,629, equal to the printed "Total debt".
- Debt table footing, December 31, 2025 (10-K page:101), thousands of USD: 425,000 + 865,000 + 1,150,000 + 900,000 + 899,311 + 905,950 + 3,636 - 3,605 - 42,299 = 5,102,993, equal to the printed "Total debt".
- Issuer-printed net debt check (Q2 release page:6): 5,107,629 - 192,138 = 4,915,491, equal to the printed figure. This is a footing check of an issuer presentation only.
- Facility columns, June 30, 2026 (Q2 10-Q page:33), millions: letters of credit 7.0 + 87.6 = 94.6 against 94.5 printed; excess availability 93.0 + 112.4 = 205.4 against 205.5 printed. The footnote attributes the difference to rounding (page:34).
- Annual to quarterly series, revenue, thousands of USD: nine months 2025 of 1,142,625 (Q3 2025 10-Q page:3) plus fourth quarter 2025 of 461,515 (Q4 release page:1) = 1,604,140, equal to the printed FY2025 revenue (10-K page:78). This is a footing check on source consistency, not a normalized series.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No source dated after August 5, 2026; merger closing or termination, note redemptions and amendment effectiveness are Not supplied | High | CP-1A, CP-2, CP-5 | Supply filings and releases dated August 6, 2026 to November 5, 2026 |
| No document for the quarter ended September 30, 2026; latest balance sheet is June 30, 2026 | Medium | CP-1, CP-2 | Supply it if filed by the cutoff; otherwise label June 30, 2026 as the latest balance |
| Executed indentures, credit agreements, amendments, supplemental indentures and Merger Agreement not supplied; context `legal_documents` is none | High for legal work; Medium for CP-2 | CP-1A, CP-2 | Supply the executed documents cited in the 10-K and Q2 10-Q exhibit lists |
| Guarantor list and guarantor or non-guarantor financial information not supplied | Medium | CP-2 | Supply the guarantor schedule or exhibit; label guarantor coverage Not supplied |
| Covenant ratio not printed because the springing test was not in effect; fixed charge coverage test applies only in a trigger period | Medium | CP-1, CP-2 | Treat headroom as Not calculable; do not use an Adjusted EBITDA based ratio as the covenant measure |
| Form 10-K/A with Part III information not supplied | Low | CP-1A | Supply if governance or ownership detail is needed |
| Fourth quarter 2025 appears only in an issuer release, and the Q1 2025 comparative only in the Q1 2026 10-Q | Low | CP-1 | Cite the release and label the basis; do not call these audited |
| Text extraction only; no original XBRL or rendered tables | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |
| No credit ratings, market quotes, peers or precedents; context blanks are not zero. The 10-K gives only a generic "speculative-grade" statement (page:44) | Low for these modules | CP-2 | Keep Not supplied |
| Pages not read in full: risk factors and business pages of the 10-K, and parts of the Q1 and Q3 2025 10-Qs | Low | CP-1A | Downstream modules must open the pages they cite |

## Next module

- CP-1: use the 10-K for annual figures and the June 30, 2026 10-Q for the latest balances and six-month figures; keep three-month, six-month and annual columns separate; keep fourth quarter 2025 as a release figure; treat net debt, Adjusted EBITDA, Adjusted Corporate expenses, FFO and AFFO as issuer non-GAAP; keep leases (operating lease liabilities, current and non-current) outside the debt total as the balance sheet does (Q2 10-Q page:2); show the revolver and receivables-based facility letters of credit by facility; carry discontinued-operation cash inside the cash-flow statement.
- CP-1A: carry the pending merger as the central transaction with every status labelled "pending as of August 5, 2026"; carry the Spain sale as completed August 4, 2026; label the unresolved buyer wording and everything after August 5, 2026 as Not supplied.
- CP-2: carry the stale-structure restriction (June 30, 2026 balances only), the unsupplied legal documents, the missing guarantor perimeter and the not-in-effect covenant as stated restrictions.
- CP-5: trace claims to page chunks; flag any figure taken from a release rather than a filing; confirm no claim relies on a post-August 5, 2026 event.
