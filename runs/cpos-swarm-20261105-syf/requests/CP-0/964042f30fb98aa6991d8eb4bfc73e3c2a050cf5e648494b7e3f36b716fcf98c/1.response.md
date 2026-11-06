## Request

Module: source readiness for Synchrony Financial (issuer id syf; NYSE ticker SYF; preferred depositary shares SYFPrA and SYFPrB), as of 2026-11-05, evidence cutoff 2026-11-05. Pathway credit_snapshot, public case, current period Q3 2026, prior period FY2025, reporting currency USD (all pinned sources report in US dollars; amounts are in millions unless a source says billions). Question: can the pinned source set support the requested minimum module set (CP-1, CP-1A, CP-2, CP-5) and what remains blocked. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles and calculates no financial figure. The assertion for any later model objective is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

The run context (sha256 b7d2667de27eee9eaad22a8f2531b97f3d412b9a580fc12af95f3529015a7aad) holds user settings only. It names no deal terms, quotes, ratings, peers, legal documents, research questions or attachments, and it is not issuer evidence. Blank context values are not zero.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Pages retained |
| --- | --- | --- |
| 10-K_2025-12-31_syf-20251231.htm.jsonl | 0b60c3e342553b852e824b86621a2fdaa6ad093dc06c4e55a2eed5e6cf19d9d4 | 221 of 221 |
| 10-Q_2026-03-31_syf-20260331.htm.jsonl | 25bad560fab9d89eaa95fa105d6deb566b793ff4487d93802c1c0d41e804e06c | 60 of 60 |
| 10-Q_2026-06-30_syf-20260630.htm.jsonl | e78db7390d45896274c6d04cfc239ed8817a6d1e34b0f8639e41e84d8aaaf93a | 67 of 67 |
| 10-Q_2026-09-30_syf-20260930.htm.jsonl | bb3d956d892f83bdc99a4d6e03538bf27003f138c169bcc3d1bc7e8f04cc2a06 | 68 of 68 |
| EX-99.1_2026-04-21_earningsrelease1q26.htm.jsonl | 0d50d951300ce2cbbde6c33a9c8f647888bd4c1a3c654b0abb8bb16574fa4c01 | 8 of 8 |
| EX-99.1_2026-07-21_earningsrelease2q26.htm.jsonl | 6450eda3e6d3c5e0b0af4323ee79065c818c4ce5b11bc0f800cb9d5d7e7bc639 | 7 of 7 |
| EX-99.1_2026-10-20_earningsrelease3q26.htm.jsonl | 79e5f3de157c7238c31f3c91c9d36532abc559b56d3ee90900d572761d0e13ee | 7 of 7 |

Also supplied and excluded as evidence: _retrieval.json, the pack's retrieval record (filing dates and accession numbers only, no issuer financial content; it carries no hash in this run and is not an issuer source). The first line of each extracted file states a sha256 of the original HTML; those differ from the extraction hashes above and the extraction hashes are the ones pinned by this run.

### Handoffs relied on

None. CP-0 is the first module and no handoff was supplied.

### Context

Run context file, sha256 b7d2667de27eee9eaad22a8f2531b97f3d412b9a580fc12af95f3529015a7aad (settings only, not evidence).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are complete, current to the third quarter of 2026 and sufficient to start the snapshot work, with bounded limitations on non-GAAP detail, indenture terms and interim cash-paid items. | High | No financial supplement, presentation, indenture or securitization document is in the pack, so covenant terms and non-GAAP reconciliations rest on filing summaries only. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filed statements and notes cover parent, bank and securitization-trust funding at the latest quarter end. | Debt, liquidity and capital work can be built from filed figures without management claims overriding them. | High |
| December 2025 capital ratios were recast in the latest quarterly filing, so the annual report and the latest quarter show different year-end ratios. | Any trend that mixes the two bases would misstate capital movement; the recast basis has to be used for comparisons. | High |
| Indenture covenants are described only generally, with no covenant terms or test levels. | Covenant headroom for the unsecured notes cannot be measured from this pack. | Medium |
| Cash paid for interest and taxes is printed for the full year only, not for interim periods. | Interim cash interest coverage cannot be built from filed cash-flow disclosure. | Medium |

### Readiness view

Readiness view: the pinned set supports the requested minimum module set with limitations. All four consumers are READY_WITH_LIMITATIONS and none is CONDITIONAL or BLOCKED, so the command sheet carries no DO NOT RUN entry. The strongest support is the latest quarterly report with its condensed statements, borrowing, capital and liquidity notes, backed by the annual report for full-year, parent-only and exhibit-index evidence and by two earlier quarterly reports for sequential periods. The strongest contrary evidence is that the filings summarise rather than reproduce the legal terms of the unsecured notes, that the earnings releases defer their detailed tables and non-GAAP reconciliation to a financial supplement that is not in the pack, and that year-end capital ratios were recast between the annual report and the latest quarterly report. Source sufficiency is not completion of downstream analysis; nothing here confirms that any later module will accept these inputs.

### Source assessment

Locators use the page number of the extracted source chunk (page:N), not the printed page. Coverage is of extracted text only; no chart, image or speaker-note content was inspected and text extraction is not a fidelity review.

| Source | Document family and authority | Entity and perimeter | Period and basis | Version relationship | Located evidence (exact quote) |
| --- | --- | --- | --- | --- | --- |
| 10-K FY2025 | Annual report on Form 10-K, filed statements; controls facts it states | Synchrony Financial consolidated, including Synchrony Bank and consolidated securitization entities; parent-only condensed statements are included | Fiscal year ended 2025-12-31, audited annual basis, USD millions | Original filing; the latest quarterly report recasts some December 2025 ratios | page:1 "For the fiscal year ended December 31, 2025" |
| 10-Q Q1 2026 | Quarterly report on Form 10-Q, unaudited filed statements | Synchrony Financial and subsidiaries, consolidated | Three months ended 2026-03-31 | Separate active source; not superseded by later quarters | page:1 "For the quarterly period ended March 31, 2026" |
| 10-Q Q2 2026 | Quarterly report on Form 10-Q, unaudited filed statements | Synchrony Financial and subsidiaries, consolidated | Three and six months ended 2026-06-30 | Separate active source; its capital table already shows December 2025 ratios recast for the software presentation change | page:1 "For the quarterly period ended June 30, 2026" |
| 10-Q Q3 2026 | Quarterly report on Form 10-Q, unaudited filed statements; latest filed period (signed 2026-10-22) | Synchrony Financial and subsidiaries, consolidated | Three and nine months ended 2026-09-30, with 2025-12-31 balance-sheet comparatives | Separate active source; supplies recast 2025-12-31 comparatives | page:1 "For the quarterly period ended September 30, 2026" |
| Earnings release Q1 2026 | Exhibit 99.1 earnings release; management narrative, attributed support | Synchrony Financial, consolidated | Three months ended 2026-03-31 | Narrative only; tables not included | page:1 "first quarter 2026 net earnings of $805 million" |
| Earnings release Q2 2026 | Exhibit 99.1 earnings release; management narrative, attributed support | Synchrony Financial, consolidated | Three months ended 2026-06-30 | Narrative only; tables not included | page:1 "second quarter 2026 net earnings of $885 million" |
| Earnings release Q3 2026 | Exhibit 99.1 earnings release; management narrative, attributed support, issued before the 10-Q | Synchrony Financial, consolidated | Three months ended 2026-09-30 | Narrative only; refers to a financial supplement not in the pack | page:1 "third quarter 2026 net earnings of $892 million" |

### Entity and instrument roles

The issuer is Synchrony Financial, the registrant and a savings and loan holding company. Its subsidiary Synchrony Bank is a separate obligor: the Bank issues its own senior unsecured notes and has its own capital tests. Consolidated securitization trusts (SYNCT, SFT, SYNIT) hold loan receivables and issue asset-backed notes owed to securitization investors. The filings state a single operating segment with five sales platforms, so no segment-level debt or restricted versus unrestricted entity split exists. There is no sponsor, guarantor or borrower distinct from the registrant in the context.

- Holding company status, page:29 of the annual report: "As a savings and loan holding company and financial holding company, Synchrony is subject to regulation, supervision and examination by the Federal Reserve Board."
- Parent-only statements exist, annual report page:193: "The following tables present parent company financial statements for Synchrony Financial"; page:194 notes "Includes investments in and amounts due from bank subsidiaries".
- Segment basis, latest quarterly report page:43: "Our single operating segment comprises a single reporting unit".
- Preferred stock, latest quarterly report page:1: "Series A SYFPrA"; Series C issuance, page:31: "in June 2026, we issued depositary shares representing $500 million of 7.250% fixed rate reset non-cumulative perpetual preferred stock, Series C".

### Conflicts, recasts and version distinctions

| Item | Source A and locator | Source B and locator | Downstream effect |
| --- | --- | --- | --- |
| Common equity Tier 1 at 2025-12-31 | Annual report page:188 "Common equity Tier 1 capital $ 13,242 12.6 %" | Latest quarterly report page:60 "Common equity Tier 1 Capital $ 14,290 13.5 % 4.5 %" | Disclosed recast, not an error. The latest quarterly report states at page:33 "Amounts and ratios at December 31, 2025 have been recast to reflect the change in presentation of internal-use capitalized software". CP-1 must label the basis and not mix the two year-end figures. The annual report is not edited by the recast and stays the authority for the originally reported ratio. |
| Prior-year ratios in the Q3 release | Release page:4 "Prior period amounts have been recast to reflect the change in presentation of internal-use capitalized software" | Annual report page:188 (original basis) | The release states recast comparatives that the pack cannot tie to a recast table, because the financial supplement is absent. |
| Net earnings, three quarterly sources | Releases page:1 of each (quoted above) | Matching condensed statements of earnings in each quarterly report | No conflict found in net earnings between release and filing for any of the three quarters; the filed statement controls if later differences arise. |

Duplicates: the annual report and the quarterly reports overlap on balance-sheet comparatives (2025-12-31); the annual report is retained for the originally reported value and the latest quarterly report for the recast value. No hash duplicates exist among the seven sources.

### Coverage by source profile

- Financial reports: statements of earnings, comprehensive income, financial position, equity and cash flows, and notes, are all present in the latest quarterly report and the annual report (index at latest quarterly report page:2 and annual report page:202). Borrowings note, latest quarterly report page:57 "Total borrowings $ 17,025 $ 15,182"; balance sheet, page:39 "Total borrowings 17,025 15,182"; unsecured note ladder, page:28 "Total senior and subordinated unsecured notes $ 8,150"; securitized maturities, page:26 "Total borrowings—owed to securitization investors $ 3,900 $ 5,025 $ — $ — $ 8,925". Facility-level debt is therefore located. Carrying value and principal are shown on different bases (unamortised discounts, premiums and issuance costs), which CP-1 must keep apart.
- Liquidity and funding: latest quarterly report page:29 "$19.5 billion of liquid assets" and "we had an aggregate of $13.0 billion of available borrowing capacity through the Federal Reserve’s discount window"; annual report page:91 "we had an aggregate of $2.1 billion of undrawn credit facilities". Cash flows: page:41 "Total cash and equivalents, including restricted amounts, at end of period $ 16,697 $ 16,287".
- Capital: latest quarterly report page:60 "Synchrony Financial met all minimum capital requirements" and the capital table quoted above.
- Covenants: latest quarterly report page:28 "We were in compliance with all of these covenants at September 30, 2026"; annual report page:57 "we were not in default under any of our credit facilities". Only a general statement is supplied.
- Securitization triggers: latest quarterly report page:27 "No early amortization event has occurred". Subsequent event within the filing: page:27 "which matured and were repaid in October 2026".
- Business and transaction narrative: annual report page:9 "Home & Auto accounted for $5.7 billion, or 26%, of our total interest and fees on loans for the year ended December 31, 2025"; acquisition, latest quarterly report page:47 "In April 2026, we completed our acquisition of the Lowe's commercial co-branded credit card portfolio". No sponsor-led or merger transaction is in the sources.
- Earnings releases: reported and management-framed figures with year-on-year comparisons for a quarter only; no quarter versus year-to-date table, no guidance table and no reconciliation. Release page:7 "please see the detailed financial tables and information that follow", and page:4 "See the financial supplement for additional information", but the supplement is not in the pack.
- Legal and financing sources: none supplied as executed documents. Annual report page:202 lists "Indenture, dated as of August 11, 2014, between Synchrony Financial and The Bank of New York Mellon, as Trustee" by reference only. Legal proceedings: latest quarterly report page:65 "NOTE 15. LEGAL PROCEEDINGS AND REGULATORY MATTERS" (general disclosure).
- Interim cash paid: annual report page:151 "Cash paid during the year for interest $ (4,162)" and page:193 "Total income taxes paid $ 710" are full-year only; the quarterly cash-flow statement in the latest quarterly report (page:41) shows no supplemental cash-paid lines.
- Ratings: latest quarterly report page:28 "Senior unsecured debt BBB- BBB" is the issuer's own table of agency ratings; no agency report is in the pack, so ratings are an attributed issuer statement.

### Consumer readiness

| Consumer | Status | Evidence demand and basis | Carried limitations |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Financial statements, debt ladders, liquidity, capital, discrete and year-to-date periods are located in filings; facility-level debt and carrying values are present. | No financial supplement or non-GAAP reconciliation; no interim cash-paid interest and tax; no indenture terms; recast December 2025 capital basis. |
| CP-1A | READY_WITH_LIMITATIONS | Business model, five sales platforms, partner relationships, regulation, the Lowe's commercial portfolio acquisition and 2026 capital actions are located in the annual and quarterly reports. | No presentation or call transcript; partner agreements and contract terms not supplied; no ownership or sponsor structure applies (listed equity). |
| CP-2 | READY_WITH_LIMITATIONS | Consumes only CP-1 and CP-1A handoffs, so no source gap is added; the dependency planner sequences it. | Inherits the CP-1 and CP-1A limitations above. |
| CP-5 | READY_WITH_LIMITATIONS | Validates quotes and figures against the prepared pack; the filings supply locatable quotes for every material area. | Extracted text only, so chart or image content cannot be checked; inherits upstream limitations. |

Command sheet: no consumer is CONDITIONAL or BLOCKED, so no DO NOT RUN entry arises.

### Evidence to risk to consequence

- Evidence: the latest quarterly report gives funding by instrument family (securitized, unsecured, deposits) and a covenant compliance statement, but the indentures are only incorporated by reference. Source risk: the unsecured notes' covenant package, events of default and any cross-default or acceleration terms cannot be read, only the issuer's compliance statement. Consequence: covenant headroom and legal ranking are recorded as Not supplied, and CP-1 must not present covenant tests as measured.
- Evidence: year-end capital ratios differ between the annual report and the latest quarterly report because of a disclosed presentation change. Source risk: a trend line that joins the two bases would show a spurious capital change. Consequence: CP-1 and CP-2 must state the basis of each ratio and use the recast basis for sequential comparison.
- Evidence: the releases name a financial supplement and a non-GAAP reconciliation that are absent. Source risk: tangible common equity, return on tangible common equity and the recast comparatives rest on management statements. Consequence: these metrics stay attributed management claims, and a filing figure controls whenever the two differ.
- Evidence: full-year cash paid for interest and taxes appears only in the annual report. Source risk: interim coverage measures lack a cash-paid input. Consequence: such measures are Not calculable for Q3 2026 and the nine-month period from filed cash-paid data.
- Evidence: the entity roles span holding company, bank and consolidated trusts. Source risk: trust assets support trust notes and bank deposits fund the bank, so consolidated totals can hide structural subordination. Consequence: downstream debt work should split parent, bank and securitization claims and not rely on a single consolidated total.

### Subsequent events and cutoff

The latest filing was signed 2026-10-22, before the cutoff of 2026-11-05, and the latest release is dated 2026-10-20. The latest quarterly report records an October 2026 securitized repayment (quoted above) and states at page:60 "There are no conditions or events subsequent to September 30, 2026" that changed capital category. No source in the pack is dated after the cutoff. Events between 2026-10-22 and 2026-11-05 are not covered by any pinned source.

## Calculations

No financial figure was calculated, normalized or reconciled in this module, in line with the method. Coverage counts only:

| Item | Inputs | Result |
| --- | --- | --- |
| Extracted pages retained across the seven issuer sources | 221 + 60 + 67 + 68 + 8 + 7 + 7 | 438 of 438 pages |
| Sources with blocked preparation | None observed in the seven sources | 0 |
| Consumers rated CONDITIONAL or BLOCKED | CP-1, CP-1A, CP-2, CP-5 all READY_WITH_LIMITATIONS | 0 |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Financial supplement and non-GAAP reconciliation referenced by the Q1, Q2 and Q3 2026 releases are not supplied; the releases carry narrative only (Not supplied) | Medium | CP-1, CP-5 | Add the supplements or treat tangible metrics as attributed management claims |
| Indentures and supplemental indentures (incorporated by reference in the annual report exhibit index and the Q3 2026 report) and securitization documents are not supplied; covenant terms and tests are Not calculable | Medium | CP-1, CP-2 | Add the executed notes documents if covenant analysis is required |
| Cash paid for interest and taxes is printed for FY2025 only; interim amounts are Not supplied | Low | CP-1 | Use full-year figures only, or add interim disclosure if it exists elsewhere |
| Recast December 2025 capital ratios differ from the annual report; the recast reconciliation table is not in the pack | Medium | CP-1, CP-2, CP-5 | Label basis on every capital figure; add the supplement for the recast bridge |
| Earnings presentations, call transcripts and partner agreements are not supplied | Low | CP-1A, CP-2 | Business narrative relies on the annual report and quarterly reports only |
| Agency rating reports are not supplied; ratings come from the issuer's own table | Low | CP-1, CP-2 | Treat ratings as attributed issuer statements |
| Charts, images and tables rendered as graphics in the filings are not inspected; extraction is text only | Low | CP-5 | Do not claim chart-based figures |
| The pack has no source dated 2026-10-23 to 2026-11-05 | Low | All | Subsequent events in that window are Not supplied |

## Next module

CP-1 (financial and capital structure data), using the Q3 2026 quarterly report as the primary period source, the FY2025 annual report for the full-year and prior-period basis, and the two earlier 2026 quarterly reports for sequential quarters. It must carry forward the recast capital basis, the carrying value versus principal distinction in debt, and the absent covenant terms and non-GAAP reconciliation. CP-1A can proceed in parallel on the business and transaction narrative.
