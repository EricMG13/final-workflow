# CP-0 — Source readiness: Caesars Entertainment, Inc. (czr)

## Request

- Issuer: Caesars Entertainment, Inc. (issuer id `czr`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025 (context).
- Run: `czr-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned page text of each source and wrote this answer. No provider was called.
- Question: can the supplied public filings and earnings releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles or calculates no figure.
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_czr-20251231.htm.jsonl | bc64a6b58a2e5481a0cfade7eea5b0ab2abc3801003c4d6cb677785a5aa59468 | Annual report on Form 10-K for the fiscal year ended December 31, 2025 (166 pages) |
| 10-Q_2026-03-31_czr-20260331.htm.jsonl | 5678521031e1645ef46bac311c4cabf43977488c6d11dfa25cc00a4f23b2d8a8 | Quarterly report on Form 10-Q for the quarter ended March 31, 2026 (51 pages) |
| 10-Q_2026-06-30_czr-20260630.htm.jsonl | c1584ea1247740f06c0dd4b0a8964b1753f8cc5c74266698804a67fd5a8dafb5 | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 (66 pages) |
| 10-Q_2026-09-30_czr-20260930.htm.jsonl | 020dbbd4c466f93db126b9e9ea0f09672470d3e5caa33fd667f739807400c48f | Quarterly report on Form 10-Q for the quarter ended September 30, 2026 (66 pages) |
| EX-99.1_2026-04-28_ex991-2026q1ceiearningsrel.htm.jsonl | 7471385a5ad76519a93a6fc4a1f0048a88c7bfb7676d6a0b6e78c8e1a9e19c13 | Exhibit 99.1 earnings release for the first quarter of 2026 (6 pages) |
| EX-99.1_2026-07-28_ex991-2026q2ceiearningsrel.htm.jsonl | 89cd5ad8c7a0d45cdf4a8f6462fc3964a9e7d04aae46811b1f50bebeb80c1762 | Exhibit 99.1 earnings release for the second quarter of 2026 (7 pages) |
| EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | 72e92043d95db7701dbaee10509a03094dd97f5a7811f25a956ad12661393bcd | Exhibit 99.1 earnings release for the third quarter of 2026 (6 pages) |
| context | fb12b9963cea633059e88f881abb925ca379a0e095eca4255a6e391fb14bd7dc | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists.

The pack also holds `_retrieval.json`, which the launcher ignores. It is not a source here.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough to run all four selected modules on the consolidated company, each with stated limits. Nothing blocks the work. | Medium | No credit agreements, indentures, leases, merger financing terms or filings after the third-quarter report are supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Annual and three quarterly reports give audited and unaudited statements, debt tables and covenant text with page locators. | Debt, liquidity and covenant work can be traced to filed statements. | Medium |
| Lease financing obligations sit outside the debt table, and the lease detail by landlord is only in the annual report. | Fixed lease claims are larger than the debt figure and need separate treatment. | Medium |
| The pending acquisition is described, but its financing and effect on existing debt are not supplied. | Post-closing leverage and debt treatment cannot be assessed from these sources. | Low |
| Covenant levels and compliance statements are printed, but no covenant ratio values or governing definitions are. | Headroom cannot be verified against the agreement definitions. | Low |

### Readiness view

Every selected consumer can proceed on the supplied filings, with bounded limitations; none is conditional or blocked. The 10-K and the three 10-Qs are original authority for statements, notes and covenant text, and the three earnings releases are management-prepared support. The recurring limits are that the governing debt and lease documents are not supplied, that the pending merger's financing and its effect on existing debt are not described, and that nothing dated after the October 27, 2026 filings is supplied.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 statements (page:99 to page:101 of the 10-K) and unaudited statements for the three interim periods of 2026 are located, with prior-year comparatives. Segment, Adjusted EBITDA, debt, cash-flow and supplemental cash-interest tables are present. Limit: the 10-Qs carry no lease note, so lease detail is at December 31, 2025 only. |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, properties, history, the pending merger, ownership of Caesars Virginia and the asset purchases are located. Limit: the Merger Agreement, the proxy statement and any merger financing papers are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Debt tables, maturities, guarantees, covenant levels, liquidity tables and lease financing obligations are located. Limit: no executed credit agreement, indenture or lease; no printed covenant ratio values. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable page locators, so claims can be traced. Limit: the text extraction was not compared with the filed HTML or XBRL, and no source is an image or chart that was inspected. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_czr-20251231.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited consolidated statements. Cover at page:1: `For the fiscal year ended December 31, 2025`.
- Audit: page:96 holds `REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM` on the financial statements; page:98 shows the report dated `February 17, 2026` and `We have served as the Company’s auditor since 2020.` A second report on internal control is at page:154.
- Statements: balance sheet at page:99; cash and restricted-cash reconciliation at page:101; notes from page:103. Lease note at page:115 to page:117; litigation note at page:120; long-term debt note at page:121 to page:122; segment note at page:147.
- Liquidity: the cash and borrowing capacity table is at page:79; Adjusted EBITDA discussion starts at page:77. Debt service requirements are at page:122.
- Other: the data-security event the filing defines as the `Data Incident` is described at page:39. The exhibit list names indentures and the VICI and GLPI lease amendments as `Previously filed`; their texts are not in the pack.
- Units: dollars in millions (balance sheet header at page:99). USD.
- Perimeter: consolidated Caesars Entertainment, Inc. and subsidiaries, including noncontrolling interests.

#### Form 10-Q for Q1 2026 (`10-Q_2026-03-31_czr-20260331.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited. Cover at page:1: `For the quarterly period ended March 31, 2026`; signed `Date: April 28, 2026` (page:50).
- Statements from page:2; debt note at page:11; covenant text at page:16; cash and borrowing capacity at page:41.
- The filing contains no mention of the pending merger (no occurrence of the word merger or of Fertitta). It was filed before the Merger Agreement.

#### Form 10-Q for Q2 2026 (`10-Q_2026-06-30_czr-20260630.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited. Cover at page:1: `For the quarterly period ended June 30, 2026`; signed `Date: July 28, 2026` (page:66).
- Statements from page:2; Note 1 with the first description of the merger at page:6 to page:8; debt note at page:15; covenant text at page:20; liquidity at page:50.

#### Form 10-Q for Q3 2026 (`10-Q_2026-09-30_czr-20260930.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited; the latest filing in the pack. Cover at page:1: `For the quarterly period ended September 30, 2026`; signed `Date: October 27, 2026` (page:66).
- Statements: balance sheet page:2; statements of operations page:2 to page:3; cash flows page:4 to page:5 with supplemental cash interest at page:5. Note 1 (merger, asset purchases) at page:6 to page:10. Note 5 (commitments) at page:15. Note 6 (debt, maturities, covenants, guarantees) at page:15 to page:21. Segment note at page:30 to page:34.
- MD&A: results from page:41; Adjusted EBITDA reconciliation at page:49 to page:50; liquidity at page:50 to page:53; market risk at page:54.
- Part II: risk factors on the merger at page:60 to page:65; exhibits at page:66, including the Merger Agreement as `Previously filed on Form 8-K filed on May 28, 2026.`
- Units: `(In millions)` throughout. USD. Statements are unaudited interim.

#### Earnings releases (three Exhibit 99.1 files)

- Family and authority: issuer press releases furnished as Exhibit 99.1, management-prepared and unaudited. They give attributed management figures and non-GAAP measures; they do not override the filings.
- Q3 release (`EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl`): dated `October 27, 2026` (page:1). Segment tables on page:1; balance sheet, net debt and liquidity on page:2; non-GAAP definition on page:3; statements of operations and Adjusted EBITDA reconciliation on page:5 to page:6.
- Q2 release (`EX-99.1_2026-07-28_ex991-2026q2ceiearningsrel.htm.jsonl`): net debt table on page:2; merger and no-call statement on page:3.
- Q1 release (`EX-99.1_2026-04-28_ex991-2026q1ceiearningsrel.htm.jsonl`): net debt table on page:2. It does not mention the merger.
- Net debt is a company non-GAAP measure: the Q3 release defines it as `Net debt is equal to total outstanding indebtedness less cash and cash equivalents.` Each release repeats the 10-Q statement of operations for its period, so a release is not independent corroboration of that 10-Q.

### Information-availability boundary

- Every source is dated on or before the cutoff. The latest are the Q3 10-Q and Q3 release, both dated October 27, 2026.
- Between October 27, 2026 and the as-of date 2026-11-05, nothing is supplied. Events in that window, for example regulatory approvals or merger financing, are Not supplied, not absent.
- Q3 10-Q page:1 gives the share count as of October 22, 2026, which is inside the supplied period.
- The Q3 10-Q (page:7) reports that stockholders approved the merger proposals on September 22, 2026, and gives May 27, 2027 as the initial end date, with extensions to August 27, 2027 and November 27, 2027 (page:8). These future dates are contract terms, not events.

### Identity and perimeter

- Registrant and reporting entity: Caesars Entertainment, Inc., a Delaware corporation, NASDAQ symbol CZR, Commission File No. 001-36629 (Q3 10-Q page:1). The context leaves borrower, parent and guarantor fields blank; blank is not evidence of absence.
- Holding company: `We are a holding company, and our only significant assets are ownership interests in our subsidiaries.` (Q3 10-Q page:50).
- Debt issuers: Caesars Entertainment, Inc. (CEI) is the borrower under the CEI Credit Agreement and the issuer of the CEI notes (Q3 10-Q page:17 and page:19 to page:20). CEI debt is guaranteed by `each existing and future material wholly owned domestic subsidiary` (page:21). The guarantor names and the restricted-group definition are not in the supplied text.
- Separate borrower group: Caesars Virginia, LLC is the borrower under the CVA facilities, which are secured by its assets; `CEI does not provide a guarantee of these facilities.` (Q3 10-Q page:21). CEI holds a `50.0% variable interest` in CVA Holdco, LLC and consolidates it as primary beneficiary, with a minority interest (page:29). Consolidated debt therefore includes debt that is not guaranteed by the parent.
- Lease counterparties: VICI Properties L.P. (the VICI Leases) and GLP Capital, L.P. (the GLPI Leases) (Q3 10-Q page:36). The leases are accounted for as failed sale-leasebacks and appear in `Long-term financing obligations`, separate from `Long-term debt` on the balance sheet (page:2).
- Acquirer: the Merger Agreement parties are Caesars, Fertitta Gaming Holdco, LLC and Empire Merger Sub, Inc. (Q3 10-Q page:6). The earnings releases instead name `Fertitta Entertainment, Inc.` as the company that will acquire Caesars (Q3 release page:4). The 10-Q heading also reads `Proposed Merger of Caesars Entertainment, Inc. with Fertitta Entertainment, Inc.` The relationship between Fertitta Entertainment, Inc. and Fertitta Gaming Holdco, LLC is not explained in the supplied text. It is an unresolved identity distinction, carried as a gap.
- Noncontrolling interests: shown in the statements (Q3 10-Q page:3 and page:4); the relevant partner is the Eastern Band of Cherokee Indians for Caesars Virginia (page:29).

### Version relationships and conflicts

- Each 10-Q is a separate period report; the Q3 10-Q does not restate the Q1 or Q2 reports. Each release duplicates statement tables from its own 10-Q. The 10-Q controls for statement facts; the release is supporting.
- Net debt and the debt split by bank debt and notes appear only in the releases (Q3 release page:2). The 10-Q debt note gives face value, book value and fair value by instrument (Q3 10-Q page:15 to page:16). The two are different presentations of different measures, and they are not treated as a conflict.
- Naming difference on the acquirer: see Identity and perimeter. Effect: CP-1A must name the signatory entity from the 10-Q and flag the releases' label as management wording.
- No draft, unsigned or superseded source is in the pack. All filings carry signature dates.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, segment results, Adjusted EBITDA reconciliation, debt, cash flows, cash interest | 10-K page:99 to page:101 and page:121 to page:122; Q3 10-Q page:2 to page:5, page:15 to page:16, page:30 to page:34, page:49 to page:50; releases page:1 to page:7 | Interim statements are unaudited. Financing obligations are a large liability class outside debt. Lease note exists only in the 10-K. Windsor consolidation from March 3, 2026 and the Grand Bazaar purchase limit comparability (Q3 10-Q page:10 to page:11). |
| CP-1A | Business, segments, properties, history, merger terms, ownership and joint ventures | Q3 10-Q page:6 to page:10, page:29 to page:31, page:36 to page:39; 10-K Business section from page:4 | Merger Agreement, proxy statement and merger financing not supplied. Acquirer naming difference unresolved. |
| CP-2 | Debt by instrument, maturities, guarantees, covenants, liquidity, lease burden | Q3 10-Q page:15 to page:21 and page:50 to page:53; 10-K page:79, page:115 to page:117 | No executed agreements. Covenant levels are printed but covenant ratio values are not. Lease payment schedule is at December 31, 2025 only. |
| CP-5 | Traceable claims across modules | All seven sources carry page locators | Text extraction only; no check against filed HTML or XBRL. |

### Source-profile review

- Financial reports: statements, period labels and units are present and consistent. The Q3 10-Q labels columns `Three Months Ended September 30` and `Nine Months Ended September 30`, so discrete-quarter and year-to-date figures are separable for Q3. Discrete Q2 figures come from the Q2 filing's own three-month column. Year-to-date cash-flow figures are cumulative, so a discrete quarter cash flow needs subtraction of earlier year-to-date reports; that step belongs to downstream modules.
- Debt table: Q3 10-Q page:15 to page:16 lists 12 debt lines by facility, with face value and book value, rate and final maturity. Facility-level carrying values are therefore present.
- Cash paid for interest and taxes: Q3 10-Q page:5 gives `Cash interest paid for debt`, cash interest paid for rent on the GLPI and VICI Leases, and `Income taxes paid, net`.
- Covenants: levels are printed for the CEI Revolving Credit Facility and Term Loan A, and for the CVA facilities, with a statement that the company `was in compliance with all of the applicable financial covenants` (Q3 10-Q page:21). The reported ratio values are not printed.
- Earnings releases: reported and adjusted figures, quarter and nine-month columns, an Adjusted EBITDA reconciliation and a net debt reconciliation are present. No guidance is given in the Q3 release text, and no conference call is held (page:4).
- Legal and financing sources: no executed credit agreement, indenture, lease or merger agreement is supplied. They are described in the filings only.
- Workbooks, scans, images and decks: none supplied. The pack has no presentation; the releases stand in for decks. The Q3 10-Q page:37 refers to a map of Caesars Digital presence; the map image is not in the text, which is recorded as a parse gap.

### Analytical read-through

- Usable coverage: one audited annual report, three unaudited interim reports and three releases cover FY2025 and the first three quarters of 2026 with prior-year comparatives. Together they support a financial foundation, a debt and lease map, and the merger narrative up to October 27, 2026.
- Strongest contrary evidence: the pending acquisition can change ownership and leverage. The Q3 10-Q lists `risks associated with increased leverage from the proposed transaction` (page:57) and `the risk that the financing required to fund the proposed transaction is not obtained on the terms anticipated or at all`. The supplied text does not say how the existing CEI debt or the CVA facilities are treated at closing.
- Source risk mechanism: lease payments to VICI and GLPI run through `Long-term financing obligations` and interest expense, not through the debt table, and Adjusted EBITDA `excludes the expense associated with certain of our leases` (Q3 release page:3). A consumer reading only total debt or Adjusted EBITDA would understate fixed claims and overstate coverage. Consequence: CP-1 and CP-2 must carry the lease obligations and the lease cash interest alongside debt.
- Second mechanism: the covenant definitions govern headroom, and the company states that its Adjusted EBITDA definition `may not be the same as the definitions used in any of our debt or lease agreements` (Q3 10-Q page:49). Consequence: CP-2 can report printed levels and the compliance statement but cannot verify headroom.
- What cannot proceed: merger financing analysis, post-closing capital structure, covenant headroom on agreement definitions, guarantor-level and restricted-group analysis, and any event after October 27, 2026.
- Next evidence action: supply the Merger Agreement (Form 8-K filed May 28, 2026, Exhibit 2.1), the merger proxy statement filed August 26, 2026, any financing commitment papers, the CEI Credit Agreement and indentures, and the VICI and GLPI lease agreements; and any filing dated October 28, 2026 to November 5, 2026.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Counts of pages and debt lines above are coverage counts taken from the pinned files and the debt table.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Merger Agreement, proxy statement and merger financing not supplied; treatment of existing debt at closing not described | High | CP-1A, CP-2 | Supply Form 8-K Exhibit 2.1 of May 28, 2026, the proxy statement filed August 26, 2026 and any financing commitments |
| Acquirer naming differs: Fertitta Gaming Holdco, LLC in the 10-Q, Fertitta Entertainment, Inc. in the releases and the 10-Q heading; relationship not explained | Medium | CP-1A, CP-2 | Confirm from the Merger Agreement or proxy statement |
| Executed credit agreement, indentures and VICI and GLPI leases not supplied | High for legal work; Medium for CP-2 | CP-2 | Supply executed documents and amendments |
| Covenant ratio values not printed; only thresholds and a compliance statement | Medium | CP-2 | Supply compliance certificates or agreement definitions |
| Lease note and payment schedule exist only in the 10-K at December 31, 2025; the 10-Qs show the aggregate financing obligation line only | Medium | CP-1, CP-2 | Label lease detail as of December 31, 2025 and carry the aggregate balance for later dates |
| Guarantor names and restricted-group definition not in the supplied text | Medium | CP-2 | Supply the exhibit of subsidiary guarantors and the indenture definitions |
| Nothing supplied between October 27, 2026 and 2026-11-05 | Medium | CP-1A, CP-2 | Supply any later Form 8-K or confirm none |
| Text extraction only; filed HTML and XBRL not compared; the Caesars Digital map is not in the text | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |
| No rating reports, market prices or peer data in the pack | Low for the selected modules | CP-2 | Not required for this scope; keep Not supplied |

## Next module

- CP-1: treat the 10-K and 10-Qs as controlling for statements; keep audited FY2025, unaudited Q1, Q2 and Q3 2026 and nine-month periods separate; keep debt, financing obligations and lease cash interest separate; label net debt and Adjusted EBITDA as company non-GAAP; note the March 3, 2026 Windsor consolidation and May 1, 2026 Grand Bazaar purchase as comparability breaks.
- CP-1A: carry the pending merger as the central transaction, with signing on May 27, 2026, announcement on May 28, 2026 and stockholder approval on September 22, 2026; name the signatory entity from the 10-Q and flag the acquirer naming difference; label anything after October 27, 2026 as Not supplied.
- CP-2 and CP-5: carry the missing merger financing, executed documents, covenant ratio values and the December 31, 2025 date of the lease schedule as restrictions; keep CVA debt separate because CEI does not guarantee it.
