## Request

Issuer: IRON MOUNTAIN INC (issuer id irm; registrant name in the filings: IRON MOUNTAIN INCORPORATED, NYSE ticker IRM). As-of date: 2026-11-05, which is also the evidence cutoff. Pathway: credit_snapshot, run id irm-2026-11-05-credit_snapshot-host. Current period: Q3 2026 (three months and nine months ended September 30, 2026); prior period: FY2025. Reporting currency named by the context: USD. The filings report in thousands of US dollars (balance sheet and statements headed "(IN THOUSANDS, EXCEPT SHARE AND PER SHARE DATA)"), so no currency or period mismatch with the context was found.

Question for CP-0: can the effective source set support the requested work, and what remains blocked? The requested downstream consumers are CP-1, CP-1A, CP-2 and CP-5 (minimum module set). The report sections selected are key findings, company operating model, model chart strip, financials and credit metrics, strengths and weaknesses, company profile and transaction summary. CP-0 gives no credit conclusion, no legal interpretation and no investment opinion, and it calculates no figures; it assesses source sufficiency only.

## Sources

Issuer sources relied on (file name as pinned, sha256 of the pinned text file):

| Source name | sha256 | Retained pages |
| --- | --- | --- |
| 10-K_2025-12-31_irm-20251231.htm.jsonl | 9c991d6cdd465558fe3d6c3b1ca180e1a4934be45256793a9fbd2c983d1c3d21 | 187 of 187 |
| 10-Q_2026-03-31_irm-20260331.htm.jsonl | c097a3f585d908ce47931b28757115d3a00ba271c949277b2995e2c2344465f7 | 43 of 43 |
| 10-Q_2026-06-30_irm-20260630.htm.jsonl | fe08302fa04f9d8c593cf06c79704bdfe3f3999447ef79511393f443f2e9e013 | 53 of 53 |
| 10-Q_2026-09-30_irm-20260930.htm.jsonl | c9d6cf1ac242db8c215c06c4487b7325abcfccb724b4417b8410eb43258ea1f1 | 55 of 55 |
| EX-99.1_2026-04-30_q12026earningspressrelea.htm.jsonl | 1ea5cf7035da8aa87dd1ad93c853ce455e98a75bb727fb04ac272e58d34c3493 | 13 of 13 |
| EX-99.1_2026-08-05_final-q22026earningspres.htm.jsonl | 0d0d4258db90617a30c1e3c9ffb5f20e0de342df888db740df22d17b30f2e886 | 18 of 18 |
| EX-99.1_2026-11-05_q32026earningspressrelea.htm.jsonl | 55477d582fc2c850f9912e2fa4b11c0af530fa7f8e752b29ae4633a58c75327b | 17 of 17 |

Run settings (not issuer evidence): context file 1020569-iron-mountain-inc-irm.json, sha256 9bee5f583dd9c7776f1152268ebe2d2da262ea2bd6a67a8712cdfef3c69af924. The pack folder also holds _retrieval.json, which the launcher ignores; it is a retrieval log, not evidence, and is not relied on.

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists.

Locator convention: `page:N` is the retained source chunk, not the printed page number. Quotes below are copied from the named chunk.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed sources are internally coherent, cover FY2025 to Q3 2026 and support all four requested downstream modules with stated limits. Debt, liquidity and covenant facts are in the filings. | Medium | No credit agreement, indentures, ratings or consolidated maturity table are supplied; covenant measures are not comparable to Adjusted EBITDA. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report and three quarterly reports are complete filed statements with notes, so debt, lease and liquidity analysis has primary authority. | Debt and liquidity work can rest on filed numbers rather than management claims. | High |
| The three earnings releases are management documents; they support attributed claims and non-GAAP reconciliations only. | Adjusted EBITDA and AFFO figures need the filing or reconciliation beside them before use. | Medium |
| No executed financing documents are supplied, and the covenant metrics use definitions that differ from Adjusted EBITDA. | Covenant headroom beyond the reported ratios cannot be rebuilt from the sources. | Medium |
| One internal inconsistency exists in the Q2 2026 quarterly report on the par call date of the 2035 notes. | The later Q3 2026 report is used for that term; other terms are unaffected. | High |

### Readiness view

The effective source set is sufficient to start all four requested consumers. Every source was opened, its identity, period and unit were read from its own text and not from its file name, and every retained page is accounted for as a retained coverage unit. The set is READY_WITH_LIMITATIONS rather than READY because several items that a creditor would normally want are absent or not comparable, and none of them blocks a consumer. Nothing in the set is draft, unsigned or blocked at preparation. The filed annual and quarterly reports control their respective facts; the releases carry attributed management claims and must not override the filings. This is a statement of source sufficiency only (SOURCE_SUFFICIENCY_ONLY); it does not evaluate any downstream input contract (CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED) and asserts no normalized quarter, reconciliation or downstream acceptance.

### Source assessment

| Source | Document family and original authority | Entity and perimeter | Period and basis | Unit and currency | Usable coverage and limitation |
| --- | --- | --- | --- | --- | --- |
| 10-K FY2025 | Annual report on Form 10-K filed with the SEC; filed audited statements control. Auditor report is present. | Iron Mountain Incorporated and subsidiaries, consolidated. Parent notes are issued by the parent and guaranteed by named subsidiary guarantors; most other subsidiaries do not guarantee. | Fiscal year ended December 31, 2025, with FY2024 and FY2023 comparatives; audited. | Thousands of USD. | Business, risk factors, MD&A, statements, debt note, leases, commitments, segment note, exhibit index. No consolidated annual debt maturity table was located by search; instrument-level maturity dates are printed. |
| 10-Q Q1 2026 | Quarterly report on Form 10-Q; filed unaudited statements. | Same consolidated perimeter. | Three months ended March 31, 2026; unaudited. | Thousands of USD. | Statements, notes, MD&A, debt and covenant sections. Superseded for balances by later quarters but retained as an active source for quarterly trend. |
| 10-Q Q2 2026 | Quarterly report on Form 10-Q; filed unaudited statements. | Same consolidated perimeter. | Three and six months ended June 30, 2026; unaudited. | Thousands of USD. | Complete, with one internal inconsistency on a par call date (see conflicts). |
| 10-Q Q3 2026 | Quarterly report on Form 10-Q; filed unaudited statements; most recent filing in the set. | Same consolidated perimeter. | Three and nine months ended September 30, 2026; unaudited. | Thousands of USD. | Primary source for the latest balance sheet, debt table, liquidity, letters of credit, covenant ratios and cash flow. |
| Release Q1 2026 | Earnings release furnished as exhibit 99.1; management document. | Consolidated, with non-GAAP measures that include a share of unconsolidated joint ventures. | Quarter ended March 31, 2026 with comparatives; unaudited. | Thousands of USD in tables; headlines in billions. | Reported and adjusted figures with reconciliations. No debt table, no cash flow statement. |
| Release Q2 2026 | Earnings release exhibit 99.1; management document. | As above. | Quarter and year to date ended June 30, 2026. | Thousands of USD. | Page 1 of the retained text holds only the extraction header; the release text starts on page 2. No content is lost, but the chunk numbering is offset by one. |
| Release Q3 2026 | Earnings release exhibit 99.1; management document, dated on the cutoff day. | As above. | Quarter and year to date ended September 30, 2026. | Thousands of USD. | Includes guidance and a declared dividend. Guidance is a forward-looking management claim, not a filed fact. |

### Evidence citations

| Source | Locator | Exact quote |
| --- | --- | --- |
| 10-K FY2025 | page:1 | "For the Fiscal Year Ended December 31, 2025" |
| 10-K FY2025 | page:1 | "IRON MOUNTAIN INCORPORATED (Exact name of Registrant as Specified in Its Charter)" |
| 10-Q Q1 2026 | page:1 | "For the Quarterly Period Ended March 31, 2026" |
| 10-Q Q2 2026 | page:1 | "For the Quarterly Period Ended June 30, 2026" |
| 10-Q Q3 2026 | page:1 | "For the Quarterly Period Ended September 30, 2026" |
| Release Q1 2026 | page:1 | "Iron Mountain Reports First Quarter 2026 Results" |
| Release Q2 2026 | page:2 | "Iron Mountain Reports Second Quarter 2026 Results" |
| Release Q3 2026 | page:1 | "Iron Mountain Reports Third Quarter 2026 Results" |
| 10-Q Q3 2026 | page:2 | "CONDENSED CONSOLIDATED BALANCE SHEETS (IN THOUSANDS, EXCEPT SHARE AND PER SHARE DATA) (UNAUDITED)" |
| 10-Q Q3 2026 | page:20 | "Total Long-term Debt 18,096,426 (124,224) 17,972,202" |
| 10-Q Q3 2026 | page:21 | "The remainder of our subsidiaries do not guarantee the Parent Notes." |
| 10-Q Q3 2026 | page:23 | "we have outstanding letters of credit totaling $61,252, of which $12,282 reduces our borrowing capacity under the Revolving Credit Facility" |
| 10-Q Q3 2026 | page:24 | "not directly comparable to Adjusted EBITDA as presented herein" |
| 10-Q Q3 2026 | page:50 | "Net total lease adjusted leverage ratio 4.8 Maximum allowable of 7.0" |
| 10-Q Q3 2026 | page:50 | "Fixed charge coverage ratio 2.5 Minimum allowable of 1.5" |
| 10-Q Q3 2026 | page:52 | "Frankfurt JV $ 74,323 20 %" |
| 10-K FY2025 | page:141 | "not to exceed $2,750,000 in United States dollars" |
| 10-K FY2025 | page:151 | "Thereafter 6,185 $ 234,027" |
| 10-K FY2025 | page:179 | "4.1 Senior Indenture, dated as of September 18, 2017" |
| 10-Q Q2 2026 | page:21 | "61/4% Notes due 2035 $ 1,500,000 January 15, 2035 January 15 and July 15 July 15, 2031" |
| 10-Q Q2 2026 | page:47 | "61/4% Notes due 2035 $ 1,500,000 January 15, 2035 January 15 and July 15 July 15, 2029" |
| 10-Q Q3 2026 | page:22 | "61/4% Notes due 2035 $ 1,500,000 January 15, 2035 January 15 and July 15 July 15, 2031" |
| Release Q3 2026 | page:10 | "Adjusted EBITDA $2,182,915 $1,868,673 16.8 %" |
| 10-Q Q3 2026 | page:42 | "Adjusted EBITDA $ 2,182,915 $ 1,868,673 $ 314,242 16.8 %" |
| 10-K FY2025 | page:57 | "Adjusted EBITDA $ 2,573,950 $ 2,236,380" |

### Source relationships and conflicts

The three quarterly reports and the annual report are separate active sources for different dates; none replaces another. The balance sheet date of the Q1, Q2 and Q3 2026 reports differ, and each carries the December 31, 2025 balance sheet as comparative, which can be checked against the annual report. The three releases duplicate content that also appears in the matching quarterly reports (revenue, net income, Adjusted EBITDA). The filing controls where they overlap; the Q3 2026 release (page:10) and the Q3 2026 quarterly report (page:42) show the same Adjusted EBITDA for the nine months, as quoted above, so no value conflict was found on that item.

Conflict 1, severity low. The Q2 2026 quarterly report prints the par call date of the 2035 notes as July 15, 2031 in its debt note (page:21) but as July 15, 2029 in its MD&A debt table (page:47). The Q3 2026 quarterly report prints July 15, 2031 in its note (page:22) and in its MD&A (page:49). The later filing and the Q2 note agree, so the 2029 entry is treated as an error in the Q2 MD&A table. Downstream effect: any call-date statement on those notes should cite the Q3 2026 report and not the Q2 MD&A table.

No other conflict between sources was found in the items searched: debt table totals, revolver availability, letters of credit and covenant ratios were each read in the Q3 2026 report and compared where an earlier report printed the same item.

### Consumer assessments

| Consumer | Status | Evidence demand and located support | Bounded gaps carried forward |
| --- | --- | --- | --- |
| CP-1 financial base | READY_WITH_LIMITATIONS | Needs income statement, balance sheet, cash flow, debt by instrument, liquidity, covenant ratios, leases and cash interest. All are in the filed reports, with the debt table on page:20 of the Q3 2026 report and covenant ratios on page:50. | G1 maturity table, G2 covenant definition, G3 letters of credit scope, G4 quarterly cash flow is year to date only, G6 unconsolidated joint venture. |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Needs business, segments, ownership and recent transactions. Item 1 and segment note of the annual report, the segment note of each quarterly report and the release narrative cover this. | G5 no transaction documents or sponsor material; the issuer is a listed company with no sponsor named in the context; G7 deferred purchase obligation terms are only summarized. |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Consumes CP-1 and CP-1A only. Source sufficiency is the same as for those two. | G8 no credit ratings or agency reports in the set. |
| CP-5 evidence trace validator | READY_WITH_LIMITATIONS | Checks quotes and figures against the pinned sources; the pinned text is searchable and complete for all retained pages. | Inherits all gaps above. A missing downstream handoff is not a readiness condition. |

### Gap log

| ID | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | No consolidated annual debt maturity table was found in the annual report or the quarterly reports after searching for maturities, thereafter, principal payments and scheduled maturities. Instrument-level maturity dates are printed in the debt notes. | Medium | CP-1, CP-2 | Build the maturity wall from instrument maturity dates and label it as derived; do not call it a company-reported schedule. |
| G2 | Covenant measures are defined on EBITDAR and EBITDA bases with adjustments, and the filings say these are not directly comparable to Adjusted EBITDA. No credit agreement or indenture is supplied. | Medium | CP-1, CP-2, CP-5 | Use the reported ratios only; do not recompute headroom from Adjusted EBITDA; ask for the credit agreement if headroom is needed. |
| G3 | Letters of credit are reported in total and in the part that reduces revolver capacity; the revolver commitment is printed in the annual report and not restated in the latest quarterly note. | Low | CP-1 | Use the annual commitment with the quarterly availability figure and state the basis. |
| G4 | Cash flow is reported year to date in the quarterly reports; discrete quarters need differencing. | Low | CP-1 | Difference year to date figures and label them derived. |
| G5 | No executed transaction documents, sponsor material, investor presentation or ratings reports are supplied. The context lists no legal documents. | Medium | CP-1A, CP-2 | State as Not supplied where a transaction term is needed. |
| G6 | One joint venture is unconsolidated and carried under the equity method; non-GAAP measures include a share of it. | Low | CP-1 | Keep the consolidated perimeter for debt and state the joint venture share where Adjusted EBITDA is used. |
| G7 | Deferred purchase obligations are reported as fair value balances and rollforwards; the underlying acquisition agreements are not supplied. | Low | CP-1A, CP-1 | Cite the fair value note; do not infer payment dates. |
| G8 | No credit ratings, agency reports or market prices are in the set, and the context holds no quotes or ratings. | Medium | CP-2 | Mark rating and relative value inputs as Not supplied. |
| G9 | The pack holds no investor presentation; the earnings releases stand in for presentations. Only extracted text exists, so no chart or image content is claimed as inspected. | Low | CP-1A | Treat the releases as management claims. |
| G10 | The Q2 2026 release has an offset in chunk numbering (page:1 is only the extraction header). | Low | CP-5 | Cite page:2 onward for that release. |

### Next evidence action

If the committee needs covenant headroom or priority of claims, obtain the credit agreement and the senior indentures listed in the annual report exhibit index, together with any agency rating reports. For the downstream modules the next step is CP-1 on the Q3 2026 quarterly report and the annual report, with the debt table, revolver availability, letters of credit and covenant ratios cited from the page:20, page:23 and page:50 chunks of the Q3 2026 report.

## Calculations

CP-0 performs no financial calculation. Coverage counts only: retained pages per source are 187, 43, 53, 55, 13, 18 and 17 for the seven sources in the order listed in Sources, total 386 of 386 retained pages assessed as retained coverage units, 7 of 7 issuer sources assessed. These counts come from the number of retained page chunks in each pinned text file.

## Gaps

The gaps are logged as G1 to G10 in the Gap log under Findings. No required document is blocked. No source is stale, draft or unsigned. Extraction status is not a fidelity review: the retained text is extracted from the filed documents, and no image or chart was inspected.

## Next module

CP-1, financial base, followed by CP-1A, CP-2 and CP-5 in dependency order. Carry forward G1 to G10 and the Q2 2026 par call date inconsistency.
