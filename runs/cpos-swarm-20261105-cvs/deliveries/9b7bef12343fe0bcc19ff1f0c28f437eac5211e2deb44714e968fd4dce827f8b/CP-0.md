## Request

Source-readiness review for CVS HEALTH Corp (issuer id cvs, ticker CVS, registrant name in the filings: CVS Health Corporation), as of 2026-11-05. Evidence cutoff 2026-11-05. Pathway credit_snapshot. Reporting currency USD, in millions unless a source states billions. Current period Q3 2026 (three months and nine months ended September 30, 2026); prior period FY2025 (year ended December 31, 2025).

Question answered: can the pinned source set support the requested downstream work (CP-1, CP-1A, CP-2 and CP-5, report sections key findings, company operating model, model chart strip, financial and credit metrics, strengths and weaknesses, company profile, transaction summary), and what remains blocked. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize or reconcile figures. The tie-outs in Calculations only test that sources agree with each other.

The run context is not issuer evidence. It leaves blank the borrower, parent, guarantors, deal terms, quotes, ratings, valuation inputs and research questions. Those blanks are treated as not supplied, never as zero or none.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Document family and period | Pages in extraction |
| --- | --- | --- | --- |
| 10-K_2025-12-31_cvs-20251231.htm.jsonl | 45f26810f483ed6fa03db93b8fdd124d91bc63cac5132d4d713dc9d4054186f0 | Annual report on Form 10-K, fiscal year ended December 31, 2025 | 291 |
| 10-Q_2026-03-31_cvs-20260331.htm.jsonl | 09079a76abcacddd5cfdc3d25ef71555f5dbfbfe17adfeaafb34285f1d52046e | Quarterly report on Form 10-Q, quarter ended March 31, 2026 | 58 |
| 10-Q_2026-06-30_cvs-20260630.htm.jsonl | aecbdbd6cbe4692d95cd67ddf7a9be39fdc845ab3dec9a5b7faf116db7070dfd | Quarterly report on Form 10-Q, quarter ended June 30, 2026 | 64 |
| 10-Q_2026-09-30_cvs-20260930.htm.jsonl | d4971bb26e82fba80a1b35b5490f32b4547bbc0a4ec7e55b11b12729167968b0 | Quarterly report on Form 10-Q, quarter ended September 30, 2026 | 70 |
| EX-99.1_2026-05-06_cvs_ex99x1q1-26.htm.jsonl | 55c42d02758692952d0d8a36a1d99162af082561033d921bab815599c14b2d61 | Earnings release dated May 6, 2026, three months ended March 31, 2026 | 15 |
| EX-99.1_2026-08-05_cvs_ex99x1q2-26.htm.jsonl | ce35d1c0fd861529f90d109402eed8bdc06bcac7900caa2304fcdfe0774a1f89 | Earnings release dated August 5, 2026, three months ended June 30, 2026 | 16 |
| EX-99.1_2026-11-04_cvs_ex99x1q3-26.htm.jsonl | 2d810cef4dc7931705e3bcaf85563bc175cc15e9e633d6a0cb9aa77c3361955f | Earnings release dated November 4, 2026, three months ended September 30, 2026 | 18 |

A page is the extraction chunk shown as page:N, not the printed page. Printed page numbers appear inline in the text and differ from the chunk number.

### Run context (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (/workspace/secdata/data/2026-11-05/contexts/64803-cvs-health-corp-cvs.json) | 5778dde57161baa53dd06c29b894f51171d7f5b790a52aed512e326c4ec302ef |

### Supplied handoffs

None. CP-0 is the first module of this run, so no upstream handoff exists. The pack folder also holds a retrieval index file that CP-OS ignores; it was not used as evidence.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The pack supports a credit snapshot on a consolidated CVS Health Corporation basis. Statements, the debt table, liquidity and segment data are located and agree with each other. Gaps are bounded and none blocks the requested work. | High | No covenant levels, credit agreements, indentures, guarantor detail or letter-of-credit usage are supplied, and the latest instrument-level debt table is the December 31, 2025 annual filing. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filed statements for the latest quarter and prior year-end are present, and the earnings releases agree with them. | Leverage, coverage and liquidity inputs can rest on filed documents rather than management claims. | High |
| The only instrument-level debt table is at December 31, 2025. Later periods give debt totals and fair value only. | The maturity wall and coupon stack must start from the year-end table and be rolled forward with stated limits. | Medium |
| Back-up credit facility expiry dates moved out one year between the first and second quarter filings, and no amendment document is supplied. | Liquidity runway rests on filing wording alone; draw conditions and terms cannot be checked. | Medium |
| A separation into two public companies was announced on November 4, 2026, after quarter end. | Future debt allocation and guarantor structure are open; the sources give no financing or debt-assignment terms. | Medium |
| Covenant tests, levels and headroom are not disclosed beyond a compliance statement. | Headroom cannot be assessed, so covenant protection must be treated as unknown rather than ample. | High |

### Readiness view

Overall view: READY_WITH_LIMITATIONS. The effective source set is sufficient for the owners of CP-1, CP-1A, CP-2 and CP-5 to perform their methods on a consolidated CVS Health Corporation perimeter. The strongest contrary evidence is that the debt documents are not in the pack: the 2026 filings carry debt only as totals, so facility-level and covenant analysis is bounded by the annual filing and by what the quarterly filings state. No source is blocked, no critical identity boundary is unresolved, and no consumer is CONDITIONAL. Missing downstream analytical handoffs are not counted against source readiness. Where a model objective is assessed, the assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

| Consumer | Status | Evidence located | Bounded limitation carried forward |
| --- | --- | --- | --- |
| CP-1 (financial and credit metrics, model chart strip) | READY_WITH_LIMITATIONS | Statements of operations, balance sheet, cash flow, segment reconciliation, depreciation and amortization, interest paid and tax paid for all three 2026 quarters, plus FY2025 | Cash flow is year-to-date only, so discrete quarters need subtraction; instrument-level debt after December 31, 2025 and covenant levels not supplied |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Segment descriptions, operating drivers, announced separation, Omnicare matters, guidance in releases | Separation terms, debt allocation and Omnicare agreements are summarized only; no transaction documents |
| CP-2 (credit synthesis, strengths and weaknesses) | READY_WITH_LIMITATIONS | Debt table, maturities, liquidity, ratings and outlooks, litigation notes | No ratings-agency reports; ratings in the context are blank and come only from company statements |
| CP-5 (evidence trace) | READY_WITH_LIMITATIONS | Every located source above is retained and hashed | Depends on upstream modules; limitations in Gaps carry through |

### Source-by-source assessment

- 10-K FY2025 (original authority: audited annual report filed with the SEC). Cover at page:1 names CVS HEALTH CORPORATION, Commission file number 001-01011, fiscal year ended December 31, 2025. Note 10 Borrowings and Credit Agreements at page:235 and page:236 holds the full debt table, five-year repayments, back-up facilities and the FHLBB capacity. Debt covenants and ratings at page:153. Contractual obligations including operating and finance leases and Target lease obligations at page:155 and page:156. Lease note at pages 229 to 230.
- 10-Q Q1 2026 (unaudited interim). Balance sheet and cash flow at page:3 and page:4; fair value of long-term debt at page:16; facilities and covenants at page:52 and page:53.
- 10-Q Q2 2026 (unaudited interim). Balance sheet at page:3; six-month cash flow at page:4; fair value of long-term debt at page:17 and page:18; facilities, covenants and ratings at page:59.
- 10-Q Q3 2026 (unaudited interim, the most recent filing and the primary source for the current period). Statement of operations at page:2; balance sheet at page:3 and page:14 for investments; cash flow at page:4; restricted cash at page:10; fair value of long-term debt at page:18; lease guarantees at page:23; segment note with reconciliations to operating income at page:35 to page:37; Omnicare guarantee footnote at page:39; Note 10 Subsequent Event at page:40; liquidity at page:63; commercial paper, back-up facilities, FHLBB, covenants and ratings at page:64; medical benefit ratio discussion at page:54.
- Earnings releases (Exhibit 99.1; management presentation, supporting attributed claims, not controlling over filings). Q3 release: headline results, guidance and cash flow from operations at page:1, statement of operations at page:6, cash flow at page:7, non-GAAP reconciliations at page:11 to page:13. Q1 and Q2 releases give headline results and guidance on page:1 and operating commentary on page:2. No investor presentation is in the pack; the releases take that place.

Extraction status is separate from fidelity. The extractions are flattened text of HTML filings; the tables read cleanly and tie out (see Calculations), but no image, chart or layout inspection is claimed and none was needed because the pack holds no deck or scan.

### Perimeter and roles

- The reporting entity in every filing is CVS Health Corporation, consolidated, in USD. The notes table does not name the issuer or co-issuer of each series, any guarantor, or security. The 10-K and 10-Q covenant paragraphs describe the back-up revolving credit facilities and unsecured senior notes as carrying customary restrictive financial and operating covenants (page:153; page:64). Issuer-by-series, guarantor and subsidiary-level debt detail are therefore Not supplied.
- Cash is not all at the parent: of approximately $11.7 billion cash and cash equivalents at September 30, 2026, approximately $5.9 billion was held by the parent company or nonrestricted subsidiaries (page:63 of the Q3 10-Q). Restricted cash of $210 million sits in other assets (page:10).
- The Omnicare entities were deconsolidated in September 2025 (page:40, footnote 14). For Q3 2026 the Company recorded an estimated contingent guarantee liability, labelled Omnicare guarantee, of $193 million (page:36; footnote 7 at page:39). The agreements themselves are not in the pack.
- Dated ratings are company statements, not agency documents: at September 30, 2026 long-term debt rated BBB by Fitch, Baa3 by Moody's and BBB by S&P; outlook Negative by Fitch and Stable by S&P; in August 2026 Moody's changed its outlook from Stable to Positive (page:64).

### Evidence coverage for the requested objective

- Discrete quarters and fiscal years: Q1, Q2 and Q3 2026 income statements and balance sheets are present, with FY2025 from the 10-K. Q3 2025 and nine months 2025 comparatives are in the Q3 2026 10-Q (page:2). Q4 2025 is not a separate source; it would have to be derived as FY2025 less nine months 2025.
- Quarter versus year-to-date: the 10-Q cash flow statements are cumulative (three, six and nine months), so a discrete Q2 or Q3 cash flow needs subtraction of the earlier year-to-date figure. The releases do not remove that need.
- Segments and add-backs: four reportable segments, adjusted operating income by segment and a full reconciliation to GAAP operating income for three and nine months of both years (page:36 to page:37 of the Q3 10-Q). Depreciation and amortization is given by segment on the same pages.
- KPIs: medical benefit ratio discussion is at page:54 of the Q3 10-Q and page:17 of the Q3 release.
- Cash paid for interest and tax: nine months 2026 interest paid $2,586 million and income taxes paid $708 million (page:4 of the Q3 10-Q).
- Facility-level debt and carrying values: 49 senior note and junior subordinated note lines, finance leases and other at December 31, 2025 (page:235 to page:236 of the 10-K). At September 30, 2026 only totals: current portion of long-term debt $3,457 million and long-term debt $57,223 million (page:3), with fair value $54,977 million against carrying value $60,680 million (page:18).
- Liquidity: three $2.5 billion five-year unsecured back-up revolving credit facilities, no commercial paper and no borrowings under them at September 30, 2026; FHLBB capacity approximately $1.4 billion, no advances (page:64).
- Business and transaction narrative: separation announcement (page:40), operational updates and guidance in each release, litigation and contingencies in Note 8 (page:22 onward).

### Version relationships and conflicts

- The three quarterly filings and the 10-K are separate active sources for different dates; none supersedes another. No duplicate sources.
- Back-up facility expiry wording changes. The 10-K (page:236) and the Q1 10-Q (page:52) say the facilities expire in May 2028, 2029 and 2030. The Q2 10-Q (page:59) and Q3 10-Q (page:64) say May 2029, 2030 and 2031. The cause (extension, renewal or replacement) is not stated in any supplied source, and no credit agreement is supplied. Downstream effect: the later date must be used for runway, labelled as filing wording, with the amendment as a gap.
- Rating outlook sequence is not a conflict: the Q1 10-Q (page:53) shows Negative at both Fitch and S&P and Stable at Moody's; the Q2 10-Q (page:59) records S&P moved to Stable in May 2026; the Q3 10-Q (page:64) records Moody's moved to Positive in August 2026.
- No filing-versus-release conflict was found. Headline cash flow from operations in each release matches the filing (see Calculations).

### Subsequent events and cutoff

- November 4, 2026: announced intention to separate into two independent publicly traded companies, intended to be tax-free; expected completion in the first half of 2028, subject to conditions including final Board approval, an effective Form 10 and a tax-free confirmation (Q3 10-Q page:40). This is a subsequent event to the September 30, 2026 balance sheet and is disclosed in a document filed on or before the cutoff. The completion date is a labelled future date, not a fact.
- Nothing in the pack is dated after 2026-11-05.

## Calculations

These are source-agreement tie-outs, not analytical calculations. All amounts in USD millions unless stated.

| Check | Inputs and locators | Result |
| --- | --- | --- |
| Debt carrying at September 30, 2026 | Current portion 3,457 plus long-term debt 57,223 (Q3 10-Q page:3) | 60,680, equal to carrying value of long-term debt in the fair value table (Q3 10-Q page:18) |
| Debt carrying at December 31, 2025 | Current portion 4,068 plus long-term debt 60,502 (Q3 10-Q page:3) | 64,570, equal to net total in 10-K Note 10 (page:236) |
| Debt principal bridge at December 31, 2025 | Total debt principal 65,035, plus premiums 156, less discounts and deferred financing costs 621 (10-K page:235 to page:236) | 64,570, equal to the line above |
| Five-year repayments at December 31, 2025 | 4,007 plus 3,379 plus 5,008 plus 3,758 plus 4,258 plus 43,299 gives 63,709; plus finance leases 1,326 (10-K page:236) | 65,035, equal to total debt principal |
| Q3 2026 adjusted operating income by segment | 912 plus 2,106 plus 1,635 less 459 (Q3 10-Q page:36) | 4,194, equal to the consolidated column |
| Q3 2026 reconciliation to GAAP | 4,194 less amortization 425, realized capital gains (3), integration costs 13 and Omnicare guarantee 193, which total 628 (page:36) | 3,566, equal to GAAP operating income (page:2) |
| Nine months 2026 adjusted operating income by segment | 6,379 plus 5,328 plus 4,307 less 1,513 (page:37) | 14,501, equal to the consolidated column |
| Nine months 2026 reconciliation to GAAP | 14,501 less 1,298, 26, 35 and 193, which total 1,552 (page:37) | 12,949, equal to GAAP operating income (page:2) |
| Nine months 2026 depreciation and amortization | 1,039 plus 760 plus 1,239 plus 335 (page:37) | 3,373, equal to the cash flow statement (page:4) |
| Q3 2026 depreciation and amortization | 351 plus 251 plus 418 plus 112 (page:36) | 1,132, equal to the consolidated column |
| Cash, equivalents and restricted cash at September 30, 2026 | 11,738 plus restricted cash in other current assets nil plus 210 (page:10) | 11,948, equal to the total shown on page:10 |
| Filing versus release, cash flow from operations | Q1 10-Q 4,249 and release 4.2 billion; Q2 10-Q six months 10,594 and release 10.6 billion; Q3 10-Q nine months 15,318 and release 15.3 billion (10-Q page:3, page:4, page:4; releases page:1) | Agree to the rounding shown |
| Filing versus release, Q3 revenue | Total revenues 108,399 (Q3 10-Q page:2); release 108.4 billion (page:1) | Agree to the rounding shown |
| Q3 revenue growth stated in release | 108,399 divided by 102,871 less 1 | 5.4 percent, equal to the release (page:1) |

Aggregate back-up facility capacity from three facilities of 2.5 billion each is 7.5 billion, from the face amounts in Q3 10-Q page:64; no usage, letter of credit or availability condition is supplied. Not calculable: covenant headroom, because no covenant level is disclosed.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Covenant levels, definitions and reported covenant figures. Searched all sources for leverage ratio, financial covenant, maximum ratio and debt to capital; only the statement of customary restrictive financial and operating covenants and of compliance was found (10-K page:153; Q3 10-Q page:64). | High | CP-1, CP-2 | Obtain the credit agreements for the back-up facilities and the note indentures. Until then, headroom is Not calculable. |
| Credit agreements, indentures, amendment for the facility expiry change, security and guarantor terms. Issuer or co-issuer by series is not printed in the notes table. | High | CP-2, CP-1A | Obtain the facility agreement and the amendment filed as exhibits; keep the later expiry dates as filing wording. |
| Instrument-level debt after December 31, 2025. The 2026 filings give totals and fair value but no table. The 2026 cash flows show repayments of long-term debt of $4,057 million for nine months and no issuance (Q3 10-Q page:4), but the notes repaid are not named in the 10-Qs. | Medium | CP-1, CP-2 | Roll forward from the 10-K table using scheduled maturities and label the result as an inference; do not present it as a reported table. |
| Letters of credit drawn on facilities. Searched letter of credit, standby, LC and LCs in the 10-K and Q3 10-Q with no result. | Medium | CP-1 | Treat net availability as Not supplied. Do not assume zero usage beyond the stated no-borrowings fact. |
| Defined benefit pension and retiree medical plan figures. The 10-K has an accounting policy heading (page:208 to page:209) but no funded status table was located by searching funded status, projected benefit obligation and defined benefit. Matches for pension in the 10-Qs refer to large case pensions insurance contracts. | Low | CP-2 | Report as Not supplied unless a later search of the 10-K notes finds the table. |
| Omnicare agreements, bankruptcy court approval documents and the sale terms behind the Omnicare guarantee of $193 million (Q3 10-Q page:39). Amount and timing of any cash settlement is not stated beyond the footnote. | Medium | CP-1A, CP-2 | Treat as a contingent claim outside the debt figure; cite only the footnote and Note 8 text. |
| Separation terms: debt allocation, guarantees, financing plan and which entity inherits each series. Only the announcement paragraph is supplied (page:40). | Medium | CP-1A, CP-2 | Treat as an open event; avoid pro forma capital structure. |
| No Q4 2025 release or deck and no investor presentation. Q4 2025 is derivable only as FY2025 less nine months 2025. | Low | CP-1 | Label any Q4 2025 or LTM figure as derived; show inputs. |
| Cash flow statements are cumulative; no discrete Q2 or Q3 cash flow is printed in the filings. | Low | CP-1 | Subtract the prior year-to-date figure and show the inputs. |
| Ratings are from company statements only; the context ratings field is blank. | Low | CP-2 | Cite the company statement with its date and avoid agency commentary. |
| No image, chart or speaker-note coverage is claimed; none exists in the pack. | Low | None | None needed. |

## Next module

CP-1, the financial and credit metrics module. It should open the Q3 10-Q statements (page:2 to page:4), the segment note (page:35 to page:37) and the 10-K Note 10 debt table (page:235 to page:236). It must carry forward these limits: covenant levels and facility agreements are not supplied; instrument-level debt after December 31, 2025 is totals only; facility expiry dates changed between the first and second quarter filings with no amendment supplied; cash flows are cumulative so discrete quarters need subtraction; only part of the cash is held at the parent or nonrestricted subsidiaries; and the announced separation and the Omnicare guarantee are open items outside the debt figure.
