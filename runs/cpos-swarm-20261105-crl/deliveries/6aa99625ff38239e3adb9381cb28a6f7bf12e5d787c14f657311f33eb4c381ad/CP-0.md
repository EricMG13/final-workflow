## Request

Source-readiness review for CHARLES RIVER LABORATORIES INTERNATIONAL, INC. (issuer id crl, ticker CRL, Delaware registrant, Commission File No. 001-15943). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit snapshot, reporting currency USD (the filings state amounts in thousands of US dollars, and the releases in millions). Current period: Q3 2026 (quarter ended September 26, 2026); prior period: FY2025 (fiscal year ended December 27, 2025).

The review answers one question: can the pinned source set support the four requested downstream modules (CP-1, CP-1A, CP-2, CP-5), and what remains blocked. It gives no credit conclusion and does no calculation. The run context (cff99a67390fb8a00e52ec6d7536d36a633f3fc1e25b95499fa40d9922d0e52d) holds dated settings only and is not issuer evidence. It leaves borrower, parent, guarantor, sponsor, ratings, quotes, deal terms and valuation inputs blank; those blanks are not treated as zero or as "none".

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Document family and period | Retained coverage |
| --- | --- | --- | --- |
| 10-K_2025-12-27_crl-20251227.htm.jsonl | 1833616d77a349706ceed059e95ca106726b27a607323742a0d24d0ce1bd17d1 | Form 10-K, fiscal year ended December 27, 2025, audited | pages 1-181 of 181 retained |
| 10-Q_2026-03-28_crl-20260328.htm.jsonl | 30ce4cd8c979bde919f80824be3ef5a888dee44b333e15ee580f2d9f9315788e | Form 10-Q, quarter ended March 28, 2026, unaudited | pages 1-50 of 50 retained |
| 10-Q_2026-06-27_crl-20260627.htm.jsonl | ab00acf6dd2054436ce66d64c08ef093e477a55198fcfd4def6687cf386bb91b | Form 10-Q, quarter ended June 27, 2026, unaudited | pages 1-54 of 54 retained |
| 10-Q_2026-09-26_crl-20260926.htm.jsonl | b6a425ac1c070f8d8fcdb26bed00199653a436bdea4f875341cd01e85bea3685 | Form 10-Q, quarter ended September 26, 2026, unaudited, signed November 4, 2026 | pages 1-56 of 56 retained |
| EX-99.1_2026-05-07_crl1q26earningsrelease.htm.jsonl | 02b23ff406fd6d3810c83441ea8f4a02420cc9d3e93a9afe30855067c289cf48 | Exhibit 99.1 earnings release, Q1 2026, dated May 7, 2026 | pages 1-14 of 14 retained |
| EX-99.1_2026-08-05_crl2q26earningsrelease.htm.jsonl | b13f468c10e832a502d66a5419cea878c35e9825584f1c67095a05ab2218878e | Exhibit 99.1 earnings release, Q2 2026, dated August 5, 2026 | pages 1-16 of 16 retained |
| EX-99.1_2026-11-04_crl3q26earningsrelease.htm.jsonl | 381e3491a7c1b96c48d03098031245e51a0342af55471093be9bdbfab773894f | Exhibit 99.1 earnings release, Q3 2026, dated November 4, 2026 | pages 1-16 of 16 retained |

The pack also holds a retrieval index file (_retrieval.json). CP-OS ignored it and it is not relied on. The pinned run context is the only other input (sha256 cff99a67390fb8a00e52ec6d7536d36a633f3fc1e25b95499fa40d9922d0e52d).

### Handoffs supplied

None. CP-0 is the first module in this run; CP-OS supplied no upstream handoff, so there is no handoff sha256 to list.

### How the sources were read

Every source is a text extraction (page chunks, shown as page:N) of an HTML filing. Extraction status is not a fidelity review: no image, chart or slide content is claimed, and none of these sources is a deck, scan or workbook. Each extracted file begins with its own "Visible text of ..." line quoting a sha256 of the original HTML; that value differs from the pinned file sha256 above, and the pinned file hashes are the ones this handoff relies on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases cover the latest quarter, the prior year and the debt notes well enough for the requested modules to run, with bounded limitations. | Medium | No credit agreement, indentures or rating reports are supplied, and interim covenant compliance is not stated. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The registrant is a single reporting entity, with no separate borrower, parent or guarantor in the context. | Debt analysis can use consolidated statements, but note guarantor identity cannot be confirmed from these sources. | Medium |
| The debt note lists the revolver and three senior note series, with the maturities, rates and revolver terms. | Facility-level debt can be sourced from the filings, but the legal terms stay summarized rather than executed. | High |
| Financial covenant levels and compliance are stated only in the annual report, not in the quarterly reports. | Covenant headroom at the latest quarter cannot be shown from the pack and needs a stated limitation downstream. | Medium |
| Two May 2026 divestitures and two acquisitions change the perimeter between periods. | Period comparisons need care, so downstream modules must separate reported and organic movements. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for all four requested consumers. The owner of each workflow can perform its method from the located filings and releases, but bounded gaps must be carried into every consumer: no executed legal documents, no ratings or market inputs, no presentation decks, and covenant disclosure only as of FY2025. No consumer is CONDITIONAL or BLOCKED. This is a statement of source sufficiency only. It does not say that any downstream analysis, normalized quarter, reconciliation or model input has been completed or accepted (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

### Source-by-source assessment

| Source | Document family and original authority | Entity and perimeter | Period and basis | Located content relevant to the objective |
| --- | --- | --- | --- | --- |
| Form 10-K, FY2025 | Filed annual report; controls audited FY2025 facts. Auditor report at page:111; filing date February 18, 2026 is stated in the Q3 10-Q at page:10 | Registrant CHARLES RIVER LABORATORIES INTERNATIONAL, INC., consolidated | Fiscal year ended December 27, 2025, with FY2024 and FY2023 comparatives | Balance sheet (page:116), debt note 11 with maturities and covenants (pages 151-153), exhibit list including the credit agreement and indentures (pages 179-180), business and risk text |
| Form 10-Q, Q1 2026 | Filed quarterly report, unaudited | Same registrant, consolidated | Quarter ended March 28, 2026 | Divestiture and held-for-sale disclosure (page:14), letters of credit (page:24, 22.0 million), market-risk section (page:42) |
| Form 10-Q, Q2 2026 | Filed quarterly report, unaudited | Same | Quarter ended June 27, 2026 | Letters of credit (page:25), market-risk section (page:48) |
| Form 10-Q, Q3 2026 | Filed quarterly report, unaudited, signed November 4, 2026 (page:56) | Same | Quarter ended September 26, 2026, with nine-month and prior-year columns | Income statement (page:5), balance sheet and cash flow (pages 6-7), acquisitions (pages 13-14), divestitures (pages 16-17), segments (pages 20-21), debt note 12 (page:26), liquidity and financing (pages 46-49), legal proceedings (pages 51-53) |
| Earnings release, Q1 2026 | Furnished Exhibit 99.1; management presentation of reported and non-GAAP figures. Does not override the 10-Q | Same | Q1 2026 | Management narrative and non-GAAP bridges, supporting only |
| Earnings release, Q2 2026 | Furnished Exhibit 99.1, as above | Same | Q2 2026 | Same |
| Earnings release, Q3 2026 | Furnished Exhibit 99.1, as above; dated November 4, 2026, before the cutoff | Same | Q3 2026 and nine months | Guidance table (end of page:4) and footnotes (page:5), non-GAAP reconciliations (pages 6, 13-16), condensed statements (pages 10-12) |

### Identity and perimeter

The registrant is the only legal entity named as issuer. The context leaves borrower, parent and guarantors blank, and the filings give no parent. The Credit Facility is described as an agreement among the registrant and "Subsidiary Borrowers" (10-K exhibit list, page:180), but the subsidiary borrowers and the note guarantors are not named in any retained page. The 10-K exhibit list refers to "the Guarantors" in the First Supplemental Indenture of March 23, 2021 (page:179). Whether guarantors are restricted subsidiaries, and which subsidiaries are borrowers, is therefore an unresolved distinction, kept as a gap and not inferred.

The consolidated perimeter changed during the periods in scope. The Q3 10-Q describes the sale of certain European Discovery Services businesses on May 22, 2026 and the sale of the CDMO and Cell Solutions businesses on May 6, 2026 (page:16), and the acquisitions of the Cambodian NHP Supplier on January 14, 2026 and PathoQuest on April 17, 2026 (pages 13-14). The Q1 2026 10-Q (page:14) reports the CDMO and Cell Solutions sale as completed, which post-dates the March 28, 2026 quarter end, so it is a subsequent event in that report.

### Debt, liquidity and covenant evidence located

The Q3 10-Q debt note (page:26) lists, at September 26, 2026 and December 27, 2025: the revolving facility, 4.25% Senior Notes due 2028, 3.75% Senior Notes due 2029, 4.00% Senior Notes due 2031, other debt and finance leases. The 10-K note (page:152) states that the 2.0 billion revolver matures in December 2029, that the facility obligations are collateralized by substantially all assets of the Company, and that the notes were issued in unregistered offerings. The 10-K principal maturities table is at page:153. Letters of credit outstanding are stated at 21.7 million (Q3 10-Q, pages 26 and 49). Cash held in US and non-US entities is at page:46, and restricted cash at page:22.

Covenants are stated in the 10-K only (page:152): a minimum ratio of EBITDA less capital expenditures to consolidated cash interest expense and a maximum ratio of consolidated indebtedness plus permitted receivables financing to consolidated EBITDA, both over four consecutive fiscal quarters, with compliance stated as of December 27, 2025. A search of all three 10-Qs and three releases found no covenant level, covenant calculation or compliance statement as of a 2026 date.

### Source conflicts

No conflict between sources was found in the items checked. The December 27, 2025 debt table in the Q3 10-Q (page:26) shows the same line items as the 10-K debt table (page:151). The Q3 total revenue and income before income taxes lines in the 10-Q (page:5) and the Q3 release (page:10) are the same. These are consistency observations, not reconciliations.

### Consumer assessment

| Consumer | Rating | Evidence located | Limitations carried |
| --- | --- | --- | --- |
| CP-1 (intake and financial extraction) | READY_WITH_LIMITATIONS | Statements, segment tables, cash flow, debt note and non-GAAP bridges in all periods | Perimeter changes from divestitures and acquisitions; non-GAAP measures are management claims; no reported EBITDA figure was found (EBITDA appears only in the covenant definitions and the divestiture funding terms), and no discrete Q4 2025 quarter is presented in the pack |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description and risk factors (10-K), transaction notes (10-Q Q3 pages 13-17) | Contingent consideration and future-funding terms of the divestitures are summarized in notes, not in executed agreements |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Debt, liquidity, cash flow and covenant description | No executed credit agreement or indentures; covenant status only as of FY2025; no ratings or market data; availability under the revolver net of letters of credit is not stated |
| CP-5 (evidence trace validation) | READY_WITH_LIMITATIONS | Every locator can be traced to a retained page | Extraction is text-only and was not checked against rendered originals |

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. Coverage counts only: seven issuer sources were retained, with 181, 50, 54, 56, 14, 16 and 16 pages respectively, each fully retained in the extraction. Figures quoted above are copied from the cited pages and carry the units printed there.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed Tenth Amended and Restated Credit Agreement (dated December 13, 2024 per 10-K exhibit list, page:180) is not supplied; only summaries in notes | Medium | CP-2, CP-1A | Obtain the exhibit from EDGAR; until then treat covenant, pricing-grid and baskets as unverified |
| Indentures for the three senior note series are not supplied (exhibit list, pages 179-180); guarantor and restricted-subsidiary identity not stated in retained pages | Medium | CP-2 | Obtain indentures and subsidiary list; keep guarantor structure unresolved |
| Covenant levels and compliance appear only for December 27, 2025; no 2026 compliance statement or covenant calculation was found in 10-Qs or releases | Medium | CP-2 | State covenant headroom as not calculable from the pack for 2026 |
| Whether letters of credit reduce revolver availability is not stated in the located text; undrawn commitment cannot be derived without that | Low to medium | CP-2 | Search again in the credit agreement or ask the company; do not assume |
| Quarterly presentation decks are not in the pack; the Q3 release says a slide presentation is on the company website (page:5) | Low | CP-1, CP-1A | Treat release narrative as attributed management claims |
| No ratings, market quotes, peer, valuation or deal-term inputs in the context | Medium | CP-2 and any later module needing them | Record as Not supplied; do not infer from the filings |
| The pack holds the 10-K and three 10-Qs, so a discrete Q4 2025 quarter is not separately presented; any such figure would need derivation downstream | Low | CP-1 | Flag derived figures as derived |
| Text extraction only; tables flattened and no rendered check done | Low | all | Spot-check key tables against the originals when a figure is critical |
| Releases are management documents; non-GAAP adjusted figures cannot override filed GAAP figures | Low | CP-1, CP-2 | Cite filings first |

## Next module

CP-1 may proceed first, using the Q3 10-Q (statements, notes 2, 3, 12 and segment note) as the primary authority, the 10-K for FY2025 comparatives and the releases as supporting claims. Carry the limitations in the Gaps table into CP-1, CP-1A, CP-2 and CP-5. Next evidence action: obtain the credit agreement, indentures and subsidiary list from EDGAR if a stricter legal read is needed, and confirm covenant status for 2026 periods.
