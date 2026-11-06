## Request

Issuer: CIMPRESS plc (ticker CMPR; Irish-incorporated registrant, Dundalk, Co. Louth; Form 10-Q cover, `10-Q_2026-09-30_cmpr-20260930.htm.jsonl` page:1). As-of date and cutoff: 2026-11-05. Pathway: credit_snapshot, public case. Current period: Q1 FY2027 (three months ended September 30, 2026; fiscal year ends June 30). Prior period: FY2026 (year ended June 30, 2026). Reporting currency: USD, amounts in thousands unless a source states millions (context file, not issuer evidence). Selected consumers: CP-1, CP-1A, CP-2 and CP-5 (the minimum module set).

Question answered by this handoff: can the supplied source set support the requested work, and what remains blocked? This is a source-sufficiency review only. It gives no credit conclusion, performs no normalisation or reconciliation, and does not evaluate downstream input contracts (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED). Nothing dated after 2026-11-05 is used as fact.

## Sources

### Issuer sources relied on (all pinned, none blocked)

| Source name | sha256 | Family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2026-06-30_cmpr-20260630.htm.jsonl | 151f9f0c267c42ae21f0ccdb2698ae7b00f08c12c11ea93c9eead2d225985251 | Annual report; filed, audited financial statements (auditor report page:83; critical audit matter page:85). Controls for FY2026 facts. | Fiscal year ended June 30, 2026 (page:1); 151 pages retained |
| 10-Q_2025-12-31_cmpr-20251231.htm.jsonl | 5912ac914c426cabed13522689ed2e56011a6c1882bd27d73724a7b41632fcbe | Quarterly report; filed, unaudited | Three and six months ended December 31, 2025 (page:1); 58 pages |
| 10-Q_2026-03-31_cmpr-20260331.htm.jsonl | f9c2a0f9fab56a82d76e0a19184ee2eca64fd97201bf2165c7319cc1b208da3c | Quarterly report; filed, unaudited | Three and nine months ended March 31, 2026 (page:1); 60 pages |
| 10-Q_2026-09-30_cmpr-20260930.htm.jsonl | a95f01276eb1e8e5ae3ae14e80d4bc7b302a4218d45429f246acfed151ff64a5 | Quarterly report; filed, unaudited; latest balance sheet and debt note | Three months ended September 30, 2026 (page:1); signed October 29, 2026 (page:53); 53 pages |
| EX-99.1_2026-04-29_q3_fy26quarterlyearnings.htm.jsonl | a3c79968ecfa051f20fab57025394eb1344a953bc437c701ec4c06c5f40daff7 | Earnings release exhibit; extraction holds only a header line (page:1) | Content not retained |
| EX-99.1_2026-07-29_q4_fy26quarterlyearnings.htm.jsonl | b8846b3859a01d99986aba6cc0cb5d6c8ccc873cb9cf041c588ae8b2cd1b1c63 | Earnings release exhibit; extraction holds only a header line (page:1) | Content not retained |
| EX-99.1_2026-10-28_q1_fy27quarterlyearnings.htm.jsonl | 68106c8dfde50a0adfff0c65c56bcc6710e9d79d49953b8ae58fdbbcc7a5502c | Earnings release exhibit; extraction holds only a header line (page:1) | Content not retained |

The pack file `_retrieval.json` is ignored by CP-OS and is not evidence. The context file (sha256 cf0965bc4987df7eefe0cb235248c6be1e28043aa64bce321b3e4b9ac5045758) holds the user's dated settings; it is not issuer evidence and its blank fields (ratings, quotes, deal terms, peers, market data) are not treated as zero.

### Handoffs relied on

None. CP-0 is the first module and no upstream handoff was supplied.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four filed reports (annual 2026 and three quarterlies) support the requested work with limitations. Statements, debt note, liquidity, covenant text and the Saxoprint acquisition are all retained and locatable. | Medium | The three earnings releases hold only a header line, and the credit agreement and indenture are not supplied, so covenant definitions rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt, liquidity, contractual obligations and covenant disclosure are retained in the annual report and latest quarterly report. | Supports downstream debt, maturity and liquidity work from filed numbers. | High |
| The three earnings releases carry no retained content. | No management guidance or adjusted-measure commentary from releases; filings must carry all of it. | High |
| Governing legal documents are only referenced by exhibit list, not supplied. | Covenant definitions, guarantor lists and indenture terms cannot be tested beyond the filing summaries. | High |
| The July 2026 Saxoprint acquisition is described differently in the annual and latest quarterly reports. | The later report controls acquisition and funding facts; its allocation is preliminary until the second quarter of fiscal 2027. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for each selected consumer: CP-1, CP-1A, CP-2 and CP-5. The four filed reports are complete, internally labelled by period, and retain the statements, the debt note, the liquidity discussion, the contractual-obligations table and the covenant text. The latest balance sheet date is September 30, 2026, which is before the cutoff. No consumer is CONDITIONAL or BLOCKED, because none depends on a document that is missing from the pack in a way that prevents its own method. The limitations travel with every consumer: earnings-release content is absent, governing legal documents are absent, and no non-GAAP covenant ratio is printed. Source sufficiency is distinct from completion of any downstream analysis, and no downstream input acceptance is asserted here.

### Source-by-source assessment

#### Annual report, fiscal year ended June 30, 2026

- Document family and authority: Form 10-K with audited statements and an auditor's report on the financial statements and internal control (page:83); it controls FY2026 facts.
- Entity and perimeter: consolidated Cimpress plc and subsidiaries (Note 2 basis of presentation in the 10-Q, page:6, same registrant). Cimpress plc is the single registrant; there is no separate borrower or parent entity in the context.
- Period and basis: year ended June 30, 2026 with FY2025 and FY2024 comparatives (income statement page:87; cash flow page:90 shows "Cash paid for interest 109,647 110,138 132,272"). Adjusted EBITDA is reconciled for three fiscal years (page:75: "Adjusted EBITDA $ 458,498 $ 433,167 $ 468,682").
- Debt (Note 10, pages:117-119): "7.375% Senior Notes due 2032 $ 525,000", "Senior secured credit facility 1,097,250", "Other (1) 14,154", total debt outstanding, net "1,611,981"; Restated Credit Agreement dated June 4, 2026 with a Term Loan B of "$1,097,250" and a "$250,000 senior secured revolving credit facility". Required principal payments by fiscal year to "Thereafter" are on page:140.
- Contractual obligations table: pages:70-71. Subsequent event, the Saxoprint acquisition: page:70 and Note 20, page:142.
- Quarterly detail: a search of the annual report text found no table of discrete fourth-quarter results (the only three-month references to June 30, 2026 are a noncontrolling-interest remark and the internal-control statement); the discrete fourth quarter is therefore not directly supplied by this filing.

#### Quarterly reports

- December 31, 2025 report: three-month and six-month columns (page:3 area, "Revenue $ 1,042,202 $ 939,159 $ 1,905,479 $ 1,744,128"). Quarter and year-to-date figures are separate columns and must not be mixed.
- March 31, 2026 report: three-month and nine-month columns ("Revenue $ 886,209 $ 789,468 $ 2,791,688 $ 2,533,596").
- September 30, 2026 report: three-month columns only, because it is the first quarter of FY2027 (page:3 income statement; "Revenue $ 934,052 $ 863,277"). It carries the latest balance sheet (page:2: "Cash and cash equivalents $ 120,127 $ 248,851"), debt note (page:20), compliance statement (page:21), liquidity and contractual obligations (pages:44-47) and the adjusted EBITDA and adjusted free cash flow reconciliations (page:49).
- Segment prior-year figures in the quarterly reports are described as adjusted for a revised inter-segment methodology (December 2025 report, segment footnote around page:43; annual report page:68, "The prior-year segment results have been adjusted to ensure comparability"). Prior-year segment numbers therefore differ in basis from figures originally filed in earlier years; the later filing controls.

#### Earnings releases (three EX-99.1 exhibits)

Each extracted file is one page with a header line only, for example the October 28, 2026 file: "EX-99.1 2 q1_fy27quarterlyearnings.htm EX-99.1". Extraction succeeded technically but retained no body text. No claim about release content, guidance, or any reconciliation inside the releases can be made. Management narrative is available only through the 10-Q and 10-K MD&A sections.

#### Legal and financing documents

Not supplied as sources. The 10-K exhibit list references the Amendment and Restatement Agreement dated June 4, 2026 (exhibit 10.28, page:150), whose borrowers are Cimpress plc, Vistaprint Limited, Cimpress Schweiz GmbH, Vistaprint B.V., Vistaprint Netherlands B.V. and Cimpress USA Incorporated, with JPMorgan Chase Bank, N.A. and J.P. Morgan SE as administrative agents, and the indenture for the 7.375% senior notes due 2032 with certain subsidiaries as guarantors (exhibit 4.1, page:147). Both are incorporated by reference to Form 8-K filings that are not in the pack. Their roles are therefore known only from the exhibit list and the debt note; the full guarantor list, definitions and baskets are unresolved gaps.

### Coverage by area the selected consumers need

| Evidence area | Retained | Locator | Limitation |
| --- | --- | --- | --- |
| Primary statements | Balance sheet, operations, cash flow, equity, comprehensive income | 10-Q Sep 2026 pages:2-5; 10-K pages:86-90 | Quarter versus year-to-date columns must be kept apart |
| Debt by facility | 2032 Notes, senior secured facility, other debt, issuance costs | 10-Q Sep 2026 page:20; 10-K page:117 | Facility-level carrying value is net of costs only at total level |
| Maturities | Required principal payments by fiscal year at June 30, 2026 | 10-K page:140 | September 30, 2026 schedule by year is not printed; only the contractual-obligations table on page:45 |
| Liquidity | Cash, revolver capacity | 10-Q Sep 2026 pages:44, 46 | Letters of credit drawn on the revolver are not itemised separately |
| Covenants | Springing leverage test text and compliance statement | 10-Q Sep 2026 pages:21, 47 | Reported ratio and headroom are not printed |
| Segments | Five reportable segments with revenue and segment EBITDA | 10-Q Sep 2026 pages:25-27, 40-43 | Prior-year bases adjusted by the issuer |
| Non-GAAP | Adjusted EBITDA and adjusted free cash flow reconciliations | 10-Q Sep 2026 page:49; 10-K page:75 | Defined by the issuer; differs from covenant definition |
| Acquisition and funding | Saxoprint purchase price allocation | 10-Q Sep 2026 pages:18-19 | Preliminary |
| Off-debt claims | Supply chain finance, purchase obligations, leases, pensions | 10-Q Sep 2026 pages:20, 29, 45-47 | Inside or outside the debt figure is for the downstream module to set |
| Ratings, quotes, peers, market data | Not supplied in context | Context file | Blank context fields are not zero |

### Version relationships and conflicts

- Saxoprint: the 10-K (filed after the July 2 closing) states the price as "€120,000" in thousands, "subject to a post-closing adjustment", and that "no definitive agreement has been executed" for a sale-leaseback (pages:70, 142). The September 2026 10-Q states total purchase consideration "$141,081 (€123,996 based on the exchange rate on the acquisition date)", a plan approved to market and execute a sale-leaseback, held-for-sale assets of "$46,303" on the balance sheet, and a preliminary allocation to be finalised "during the second quarter of fiscal year 2027" (pages:18-19, 2). These are different dates of the same transaction, not a contradiction of fact. The later 10-Q controls the amount and funding (cash and the revolver, with "$35,000" of revolver borrowings, page:21). No executed sale-leaseback is evidenced.
- Restated Credit Agreement: the 10-K describes a Term Loan B of "$1,097,250" at June 30, 2026 and no revolver borrowings; the 10-Q describes "$1,094,500" and revolver borrowings of "$35,000" at September 30, 2026 (page:21). Different balance sheet dates; both remain active evidence for their own dates.
- Maturity: the 10-Q adds that the Term Loan B is subject to an earlier maturity of June 16, 2032 if the 2032 Notes have not been repaid, refinanced or extended as specified (page:21); the 10-K states a final maturity of June 4, 2033 (page:118). The 10-Q wording is the more complete statement of that term; the executed agreement is not supplied to confirm it.
- Duplicates: none identified. No source is a hash duplicate of another.

## Calculations

None. CP-0 performs no normalisation, reconciliation or derivation, and no figure in this handoff is computed. Every number above is quoted from a retained source span with its locator. Unknown values are left unknown, not zero.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| The three EX-99.1 earnings releases retain only a header line | Medium | CP-1A, CP-2 | Re-extract the release bodies; until then use 10-K and 10-Q MD&A for management narrative and do not attribute any statement to a release |
| Amendment and Restatement Agreement (June 4, 2026), the credit agreement text and the 2032 indenture are not supplied | Medium | CP-2, CP-5 | Obtain the Form 8-K exhibits listed at pages:147 and 150; until then covenant definitions, baskets, full guarantor list and the earlier-maturity springing term are filing summaries only |
| The reported Consolidated Leverage Ratio and headroom are not printed; the test applies only if revolving usage exceeds 20% of commitments at a quarter end (page:21) | Medium | CP-2 | Treat as Not supplied; do not infer headroom from adjusted EBITDA, whose definition differs from the covenant definition |
| Letters of credit under the revolver are not itemised; the filing gives "available borrowing capacity ... was $197.7 million" and "$4.5 million" of lease-related bank guarantees and letters of credit (page:46) | Low | CP-2 | Use the printed availability figure and cite it; do not derive a letter of credit total as a printed fact |
| Required principal payments by year are printed only at June 30, 2026 (page:140); at September 30, 2026 only bucketed contractual obligations are printed (page:45) | Low | CP-2 | Use the June 30, 2026 schedule labelled as such, and the September 30, 2026 buckets labelled as such |
| No separate discrete fourth-quarter FY2026 statement is retained; only the annual report and the first three quarterly reports | Low | CP-1 | Any fourth-quarter or trailing figure is a downstream derivation and must show its inputs and periods |
| Saxoprint purchase price allocation is preliminary and no sale-leaseback agreement is evidenced | Medium | CP-1A, CP-2 | Carry as preliminary; check for finalisation in the next quarterly report, which is after the cutoff and not available |
| No presentations; the pack substitutes earnings releases, which are unreadable | Low | CP-1A | None available inside the cutoff; management claims are drawn only from filings |
| Ratings, market quotes, peer data, deal terms and research questions are blank in the context | Low | CP-2, CP-5 | Not supplied; do not treat as zero |
| Image, chart and speaker-note content is not covered because the sources are text extractions | Low | All | Not applicable to filings of this form; recorded as a parse limitation |
| Currency and units: statements are USD in thousands; the Saxoprint price is also stated in euros; MD&A uses millions | Low | All | Quote units with each figure |

## Next module

Proceed to CP-1 and CP-1A, then CP-2 and CP-5, in the order CP-OS sets. All four are READY_WITH_LIMITATIONS and none is DO NOT RUN. Carry forward: use only filings for management narrative; label every figure with its period (Q1 FY2027, FY2026, six or nine months, as printed); cite the 10-Q for September 30, 2026 balances and the 10-K for June 30, 2026 balances; treat the Saxoprint allocation as preliminary; treat covenant headroom, guarantor lists and indenture terms as Not supplied; and do not use any earnings-release content. Next evidence action: obtain the release bodies and the June 4, 2026 credit agreement and 2032 indenture exhibits.
