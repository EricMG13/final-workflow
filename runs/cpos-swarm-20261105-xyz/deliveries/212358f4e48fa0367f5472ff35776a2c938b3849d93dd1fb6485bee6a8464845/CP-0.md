## Request

Issuer: Block, Inc. (issuer id xyz, ticker XYZ, Class A common stock on the New York Stock Exchange; Commission File Number 001-37622). As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, with the filings stating amounts in thousands (the Q3 2026 shareholder letter tables are in thousands, its narrative in millions or billions). Current period: Q3 2026 (quarter ended September 30, 2026, plus nine months 2026); prior period: FY2025 (balance sheet December 31, 2025).

Question answered here: can the supplied source set support the requested downstream modules (credit snapshot minimum set: CP-1, CP-1A, CP-2, CP-5) and what remains blocked. This is a source-sufficiency review only. It gives no credit conclusion, normalizes no figure and does not evaluate any downstream input contract (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED). The context file holds the user's settings, not issuer evidence; it leaves the borrower, parent, guarantors, ratings, quotes, deal terms and market data blank, and blank is treated as not supplied, not as zero.

## Sources

### Issuer sources relied on

| Source | sha256 | Family and authority | Period and basis | Pages |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_xyz-20251231.htm.jsonl | 6d2723637c4e4692665dfc17c25cdb747bc058fa0efdacc637270724a986bc79 | Annual report, audited, filed statements control | FY2025, year ended December 31, 2025 | 219 |
| 10-Q_2026-03-31_xyz-20260331.htm.jsonl | fb16696ee2c760f5f516dd4d7d776ad2e1413e975d581b22e43bf743c804dffb | Quarterly report, unaudited | Q1 2026, three months ended March 31, 2026 | 136 |
| 10-Q_2026-06-30_xyz-20260630.htm.jsonl | 298a453eb61f62c2eadccf751942418cba8c13261b222b26c193276f0204df4e | Quarterly report, unaudited | Q2 2026, quarter and six months ended June 30, 2026 | 141 |
| 10-Q_2026-09-30_xyz-20260930.htm.jsonl | c3685fce2b8084b3b1277e2ff24d3b8912d57dba3d48bc4c00ef1cdf864ed3ba | Quarterly report, unaudited | Q3 2026, quarter and nine months ended September 30, 2026 | 144 |
| EX-99.1_2026-05-07_d132441dex991.htm.jsonl | d34a2a9e1d7a5617f1c2e6fc60dfac8b09244c4670a9cb13c493e5c88cddf1a8 | Q1 2026 shareholder letter furnished as exhibit, management presentation | Q1 2026 | 30 |
| EX-99.1_2026-08-05_d91486dex991.htm.jsonl | 804a5c312efc62e6ddd1ec8bbc4d12bb902bba131422b7373caf3f4ebbc3e21e | Q2 2026 shareholder letter, management presentation | Q2 2026 | 28 |
| EX-99.1_2026-11-03_q32026shareholderletter.htm.jsonl | a2c931043c84d33fdc40710a24c2e84aa25d66394cc76e294f6f9e8221b76b85 | Q3 2026 shareholder letter, management presentation | Q3 2026 | 33 |

Total retained text: 731 pages across seven sources (219 + 136 + 141 + 144 + 30 + 28 + 33). The pack index file `_retrieval.json` is a fetch log, not issuer evidence, and was not relied on.

### Context

| Source | sha256 | Role |
| --- | --- | --- |
| context (1512673-block-inc-xyz-bsqkz.json) | a90d836267c628949bea7547e85d546a29cc1dd93e2cdf0e9cf75961d7745ec4 | User settings for the run; not issuer evidence |

### Handoffs

None supplied. CP-0 is the first module of this run and has no upstream handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The supplied filings and shareholder letters are sufficient to start the debt, liquidity and covenant work for Block, Inc. at the latest quarter, with bounded gaps. | Medium | Executed indentures and the credit agreement are not supplied, and the leverage covenant level is not stated in the filings. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Annual report, three quarterly reports and three shareholder letters cover the year-end and each 2026 quarter, with a debt note in each report. | Debt and liquidity work can be built from filed statements for each period. | High |
| The revolving facility covenant is a maximum total net leverage ratio, but its level and the issuer's reported ratio are not printed. | Covenant headroom cannot be computed from the supplied sources. | Medium |
| Prior-period amounts were reclassified to the current revenue presentation in the latest quarterly report, and the shareholder letters give adjusted measures that are not filed audited figures. | Period comparisons should use the latest report's comparative columns, and adjusted profit figures stay management claims. | Medium |
| Notes guarantors, subsidiary roles and indenture terms are not in the pack; only the filing summaries are. | Structural subordination and guarantee analysis stays incomplete. | Low |

### Readiness view

Overall view: READY_WITH_LIMITATIONS for the four selected downstream consumers. The effective source set is the annual report for FY2025, the three 2026 quarterly reports and the three 2026 shareholder letters. Each of the four filed reports carries a balance sheet, a statement of operations, cash flows and an indebtedness note, so the evidence a debt, liquidity and operating-trend analysis needs is located and retained. The strongest contrary evidence is that none of the executed legal documents are in the pack and the financial covenant level is not printed, so the legal terms of the debt rest on the issuer's own summaries in the notes. The Q3 2026 report is the latest filed document and controls any conflict with the shareholder letters. Nothing in the pack is dated after the cutoff; the latest filing is dated 2026-11-03.

### Source-by-source assessment

#### Annual report for FY2025

Audited annual report for Block, Inc. as the registrant. The cover reads "For the fiscal year ended December 31, 2025" (page:1). The auditor's reports are retained: "We have served as the Company’s auditor since 2019." (page:139). The indebtedness note is Note 14 (page:184) and the 2025 year-end note list includes the 2026 Senior Notes and 2026 Convertible Notes that were later repaid. Coupon terms are printed there, for example "bear interest at a rate of 6.50% payable semi-annually on May 15 and November 15 of each year" for the 2032 Senior Notes (page:190). The exhibit list names the indentures: "4.7 Indenture, dated as of May 20, 2021, by and between Square, Inc. and Bank of New York Mel" (page:215), which shows the notes were issued under the former corporate name; the indentures are incorporated by reference and not supplied. Extraction status is complete (219 of 219 pages), but a successful extraction is not a fidelity review.

#### Quarterly reports for Q1, Q2 and Q3 2026

All three are unaudited condensed consolidated statements of Block, Inc. and its consolidated subsidiaries. Period labels are confirmed in the text: "For the quarterly period ended September 30, 2026" (Q3 report, page:1), "For the quarterly period ended June 30, 2026" and "For the quarterly period ended March 31, 2026". The Q3 report carries the balance sheet at September 30, 2026 against December 31, 2025 (pages 4 to 5), the statements of operations for three and nine months (page:5), cash flows (pages 8 to 9), and Note 12 on indebtedness (pages 26 to 29). The Q1 and Q2 reports hold Note 12 at page:23 and page:25 respectively, which supports quarter-by-quarter debt movements. The Q3 report states the perimeter: "Block is comprised of two reportable segments, Square and Cash App." (page:9), with a corporate and other category in Note 17 (pages 38 to 39). The reports consolidate the Warehouse special purpose entities, which are separate legal entities whose assets "are not available to satisfy the claims of the Company or those of its creditors" (page:29); this is an entity-perimeter distinction that downstream work must preserve.

#### Shareholder letters furnished as Exhibit 99.1

The three letters are management presentations of the same quarters. They add guidance, non-GAAP measures and a quarterly series, for example a five-quarter Adjusted EBITDA row "Adjusted EBITDA 833 930 1,010 1,169 1,228" (Q3 letter, page:17), and condensed unaudited statements (Q3 letter, pages 25 to 26). They are attributed management claims; the filed reports control any conflict. They are text extractions; charts and images in the letters are not inspected and no claim of chart coverage is made. No separate slide presentation exists in the pack, and the letters stand in for presentations.

### Debt and liquidity evidence located

Notes, from the Q3 report Note 12: "Total $ 5,775,000 $ (51,973) $ 5,723,027" (page:27), listing the 2030, 2031, 2032 and 2033 Senior Notes and the 2027 Convertible Notes (in thousands). The 2026 Senior Notes and 2026 Convertible Notes were settled in cash in 2026 (page:27). Revolver: "As of September 30, 2026, no funds have been drawn and no letters of credit have been issued under the Restated Credit Agreement." (page:28). Warehouse Facilities: "None of the Warehouse Facilities contain corporate financial covenants." (page:29). Liquidity: "As of September 30, 2026, we had approximately $10.1 billion in available liquidity" (page:55), with a table by component (page:55). Cash interest: "Cash paid for interest $ 270,946 $ 124,220" (page:40, nine months 2026 and 2025, in thousands).

### Consumer assessment

| Consumer | Status | Evidence located | Limitations carried |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Business and segment description, revenue and gross profit by segment (Q3 report pages 38 to 39), debt note | Prior-period amounts reclassified in the Q3 report (page:10); adjusted measures only in letters |
| CP-1A | READY_WITH_LIMITATIONS | Statement of operations, cash flows, segment tables, quarterly series in letters, Q1 to Q3 reports for discrete quarters | Q2 and Q3 discrete quarters need subtraction from year-to-date or the three-month columns; Q4 2025 discrete not in a quarterly filing (derivable only from FY2025 less nine months, which needs the FY2025 and prior Q3 data) |
| CP-2 | READY_WITH_LIMITATIONS | Note 12 debt tables for each period, revolver terms, warehouse facilities, liquidity table, restricted cash | Indentures and credit agreement not supplied; guarantors not named; covenant level not printed |
| CP-5 | READY_WITH_LIMITATIONS | Cash flow statement, interest paid, liquidity and covenant compliance statement | Compliance is stated by management without a computed ratio |

## Calculations

None performed. CP-0 does not normalize, reconcile or calculate figures. The only arithmetic is the coverage count of retained pages: 219 + 136 + 141 + 144 + 30 + 28 + 33 = 731 pages across seven sources.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed legal documents are not supplied: the indentures for the Senior Notes and Convertible Notes and the Restated Credit Agreement are listed as exhibits but not in the pack (annual report page:215) | Medium | CP-2, CP-5 | Obtain the exhibits from EDGAR; until then rely on the notes summaries and label them as issuer summaries |
| The maximum total net leverage ratio covenant is described only as "a maximum total net leverage ratio, measured quarterly" (Q3 report page:109); the level, step-downs, definition and reported ratio were searched for and not found | Medium | CP-2, CP-5 | Obtain the Restated Credit Agreement; headroom is Not calculable from the pack |
| Guarantors and the borrower-entity roles for the notes are not stated in the pack text searched; the context leaves borrower, parent and guarantors blank; the 2021 indenture names Square, Inc. | Medium | CP-2 | Check the indentures and subsidiary list; state obligor as the registrant only where the notes say so |
| No ratings agency reports are supplied; the Q3 report mentions agency ratings in management discussion (page:58) | Low | CP-2, CP-5 | Treat ratings as issuer-stated, unverified |
| Revenue presentation was reclassified: "Certain prior period amounts reported in our condensed consolidated statements of operations and notes thereto have been reclassified to conform to the current year presentation." (Q3 report page:10). The annual report already uses the three revenue categories (page:7), but earlier 2026 quarterly reports and 2025 quarterly comparatives were not tested for the conformed presentation | Medium | CP-1, CP-1A | Use the Q3 2026 report's comparative columns for 2025 quarters and check each earlier report's revenue lines against them before combining periods |
| Non-GAAP measures (Adjusted EBITDA, Adjusted Operating Income) appear in the letters; their reconciliations are management-prepared | Low | CP-1A, CP-5 | Cite as management claims; compute credit metrics from filed statements |
| Charts, images and speaker content in the letters are not covered by text extraction | Low | CP-1 | No claim of chart coverage is made |
| No market data, peer set, quotes or deal terms are in the context | Low | Not selected modules | Relative value and portfolio fit modules are omitted from this run |
| The shareholder letters and all three quarterly reports are unaudited | Low | All | Filed annual statements control for FY2025; quarterly figures stay unaudited |

## Next module

Proceed with CP-1 (company profile and operating model). Carry forward: perimeter is Block, Inc. consolidated, with Warehouse SPE assets outside creditor reach; use the latest report's comparative columns for revenue lines; adjusted measures are management claims; the covenant level, guarantors and executed documents are open gaps; amounts in USD thousands in filings. Next evidence action: obtain the indentures and Restated Credit Agreement exhibits if debt terms must go beyond the notes summaries.
