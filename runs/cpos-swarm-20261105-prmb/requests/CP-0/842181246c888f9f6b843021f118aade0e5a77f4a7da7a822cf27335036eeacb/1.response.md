## Request

Source-readiness review for Primo Brands Corp (Primo Brands Corporation, Delaware registrant, NYSE ticker PRMB, issuer id prmb, SEC file number 001-42404), as of 2026-11-05. Pathway credit_snapshot, public case, reporting currency USD, current period Q3 2026, prior period FY2025. Evidence cutoff 2026-11-05: nothing dated after it is used. The filings state amounts in millions of US dollars (`page:4` of the Q3 10-Q: "($ in millions, except share and per share amounts)"), and this review keeps that unit.

The question: can the supplied source set support the selected downstream consumers CP-1, CP-1A, CP-2 and CP-5 (the minimum module set), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize or reconcile figures. The only arithmetic is a short set of tie-outs that test whether sources agree with each other (`## Calculations`). Source sufficiency only (SOURCE_SUFFICIENCY_ONLY); the model input contract is not evaluated (CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

The run context holds dated settings and is not issuer evidence. It leaves borrower, parent, guarantors, ratings, quotes, deal terms, peers, valuation inputs and research questions blank, and states `legal_documents` as "none". Blank values are Not supplied, never zero.

## Sources

`page:N` is the chunk of the converted text file, not the printed page. The sha256 below is the pinned file hash. Each file's first line also prints the sha256 of the underlying HTML document; that is a different hash and is not used as the file identity.

### Issuer sources relied on

| Source (exact name) | sha256 (pinned file) | Chunks | Document family and authority |
| --- | --- | --- | --- |
| 10-K_2025-12-31_prmb-20251231.htm.jsonl | 60d79b9ec8f05aed0d140a51b4d3f1d8eb015dd6743bb2699d0fee368bff051f | 192 | Annual report on Form 10-K for the fiscal year ended 2025-12-31, signed 2026-02-27 (`page:121`); audited |
| 10-Q_2026-03-31_prmb-20260331.htm.jsonl | 99681433894a4d7b14141909d74698aff6d2383b60283b0706ad04024190b1b8 | 54 | Quarterly report on Form 10-Q for Q1 2026, signed May 7, 2026 (`page:54`); unaudited |
| 10-Q_2026-06-30_prmb-20260630.htm.jsonl | f5f942b75f737f8af26039c159ca583ff2e512ee89a2478a6850a2d1b07a0f98 | 61 | Quarterly report on Form 10-Q for Q2 2026, signed August 5, 2026 (`page:61`); unaudited |
| 10-Q_2026-09-30_prmb-20260930.htm.jsonl | 95354dd1e2fc79683928b45ccb08e03d8e76291367a9171fad5aa8f4c5954c6b | 63 | Quarterly report on Form 10-Q for Q3 2026, signed November 5, 2026 (`page:63`); unaudited; latest filed statements |
| EX-99.1_2026-05-07_ex991.htm.jsonl | 5b4e5356c8a7dd33fff4d2ec1d2357c63bb85628f6a6619799a77852ce483032 | 12 | Earnings release exhibit for Q1 2026; management-attributed supporting claims |
| EX-99.1_2026-08-05_ex991.htm.jsonl | 56ee46b7abb25637a63476c674a59659d13c2eddb920ccd958837f11cba5c01d | 13 | Earnings release exhibit for Q2 2026; management-attributed supporting claims |
| EX-99.1_2026-11-05_ex991.htm.jsonl | 6dd2c90be990eaffd514267a4b4a0363cc3e49d4529fedc16d1ed91c51d7cb2d | 14 | Earnings release exhibit for Q3 2026; management-attributed supporting claims |

The file `_retrieval.json` sits in the pack folder, was ignored by CP-OS and is not evidence.

### Run context (not issuer evidence)

| Source | sha256 |
| --- | --- |
| context | 6c8ceb76224ccf7cca54dd0892bbd34fd084e5ce74d3140c5df58145b6c1160f |

### Supplied handoffs

None. CP-0 is the first module in this run, so CP-OS supplied no upstream handoff and no handoff module or sha256 is relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven documents cover the annual report, three quarterly reports and three earnings releases through the third quarter of 2026, which is enough to start all four planned analyses, with stated limits. | Medium | No credit agreement, indenture or presentation is supplied, so debt terms and covenant headroom rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report lists debt by instrument, but the quarterly reports print only a fair-value debt table, and the annual maturity ladder predates the March 2026 term loan refinancing. | The maturity wall must be rebuilt from the refinancing terms, and finance leases and other debt at the latest quarter are not itemized. | High |
| The revolver covenants are printed as a first lien net leverage test and an interest coverage test, but no reported ratio or headroom is printed. | Covenant headroom cannot be measured; only the stated levels and the compliance statement are available. | High |
| Credit ratings and outlooks are printed in the latest quarterly report even though the run context leaves ratings blank. | The filing figures are usable as an issuer-reported rating record, not as an independent rating source. | Medium |
| A securities class action, a consumer class action and a spring-water labelling class action are disclosed, with no estimate of possible loss beyond amounts accrued. | These are unquantified contingent claims that later work must carry as limits. | Medium |

### Readiness view

The supplied set supports the requested work with limitations. All four selected consumers are assessed as READY_WITH_LIMITATIONS, none is CONDITIONAL and none is BLOCKED. The audited annual report, the three quarterly reports and the three releases identify one registrant, Primo Brands Corporation, report one segment in USD, and cover FY2025 and the first three quarters of 2026 up to the cutoff. Four limitations bind. First, the pack holds no executed financing document, so covenant levels, guarantor lists, security and the springing maturity condition rest on filing descriptions. Second, the annual debt table and maturity ladder describe the position before the March 2026 refinancing, and the latest quarterly report gives only a fair-value debt table, so a current instrument-level debt schedule must be assembled from several sources. Third, three class actions are disclosed without an estimate of possible loss beyond amounts accrued. Fourth, text extraction was not reviewed for fidelity, and charts, images and the earnings presentations referred to in the releases are not in the pack. None of these stops a consumer from starting, and each is carried forward.

### Per-source assessment

| Source | Entity and perimeter | Period and basis | Version relationship |
| --- | --- | --- | --- |
| 10-K FY2025 | Primo Brands Corporation and wholly-owned subsidiaries, one reportable segment (`page:184`); the accounting acquirer for the 2024 combination was BlueTriton (`page:84`), so FY2023 reflects only BlueTriton and Primo Water is included from November 9, 2024 (`page:84`) | Fiscal year ended December 31, 2025 with 2024 and 2023 comparatives; USD millions; audited by PricewaterhouseCoopers LLP (`page:124`), with the FY2023 statements audited by Ernst & Young LLP (`page:125`) | Only full-year source; controls FY2025 and the December 31, 2025 balance sheet; the debt table and ladder are as of that date |
| 10-Q Q1 2026 | Same registrant; same single segment | Three months ended March 31, 2026 versus 2025; unaudited; first filing after the March 31, 2026 term loan amendment (`page:14` and `page:15`) | Separate active source |
| 10-Q Q2 2026 | Same registrant | Three and six months ended June 30, 2026; unaudited | Separate active source |
| 10-Q Q3 2026 | Same registrant; no operations outside North America (`page:11`) | Three and nine months ended September 30, 2026 versus 2025; balance sheet versus December 31, 2025; unaudited | Latest filed statements; controls Q3 2026 and nine-month facts |
| EX-99.1 Q1, Q2, Q3 2026 | Same consolidated perimeter; releases state a new comparable net sales basis that excludes the exited Eastern Canadian operations and the exited US Office Coffee Services business (Q3 release `page:13`) | Quarter and, in the Q3 release, nine-month and trailing figures; non-GAAP reconciliations | Each release is a separate active source; the filed report controls where both state a fact |

### Entity and perimeter map

The registrant is Primo Brands Corporation (cover, `page:1` of each report). The notes name different entities for debt. Under the First Lien Credit Agreement, Primo Brands is the parent borrower, Triton Water Holdings, Inc. and Primo Water Holdings Inc. are borrowers, and Morgan Stanley Senior Funding, Inc. is term loan administrative agent and collateral agent (10-Q Q3 `page:16`). The three series of senior notes are co-issued by Primo Water Holdings Inc. and Triton Water Holdings, Inc., described as indirect, wholly owned subsidiaries (10-K `page:158`). The 3.875% Senior Notes are described as secured and "guaranteed by the Company and substantially all of the Company's wholly-owned domestic subsidiaries" (10-K `page:160`), and the 6.250% Senior Notes as guaranteed "by the Company and certain subsidiaries" (10-K `page:159`). Security is described in the 10-K MD&A: the term loans are secured by a first-priority lien on substantially all of the issuers' and guarantors' current and fixed assets (`page:95`), the two secured note series rank pari passu with the credit agreement liens (`page:98`) and the 6.250% Senior Notes are "senior unsecured obligations" (`page:99`). No separate co-issuer or guarantor financial statements were located in the pack (searches for guarantor summarized financial information found none), so the consolidated statements are the only perimeter available. Whether the consolidated figures equal the restricted group is an unresolved distinction and is logged as a gap.

The 2024 combination makes FY2024 and FY2023 comparatives only partly like-for-like with FY2025 (10-K `page:84`). The context names FY2025 as the prior period, which sits wholly after the combination.

### Strongest usable coverage

- Statements. The Q3 10-Q carries the balance sheet (`page:4`), statements of operations (`page:5`), cash flows with cash paid for interest and income taxes (`page:6` and `page:7`) and equity (`page:7`). The 10-K carries the audited FY2025 statements (`page:126` onward).
- Debt. The 10-K debt note prints the instrument table (Term Loans, 6.250%, 3.875% and 4.375% Senior Notes, Revolving Credit Facility, finance leases, other, unamortized costs), principal maturities by year, and terms (`page:154` to `page:162`). The Q3 10-Q describes the March 31, 2026 refinancing into a term loan of $3,090.0 million maturing in March 2031 (`page:16`), the covenants (`page:17`), a fair-value debt table (`page:30`), $163.4 million of letters of credit (`page:38`), $750.0 million of revolving commitments (`page:51`) and credit ratings (`page:53`).
- Non-GAAP. The Q3 release reconciles net income from continuing operations to Adjusted EBITDA for the quarter and nine months (`page:11`), free cash flow (`page:12`) and the net leverage ratio build (`page:13` and `page:14`). The 10-K reconciles FY2025 Adjusted EBITDA (`page:86`).
- Narrative and outlook. The releases print a full-year outlook (Q3 release `page:2`) and the 10-Q MD&A gives drivers and liquidity (`page:40` to `page:54`).
- Contingencies and subsequent events. Note 14 sets out the litigation (`page:34` to `page:38`) and Note 16 the dividend and new repurchase program (`page:39`).

This supports CP-1 (document and financial read), CP-1A (financials and credit metrics inputs), CP-2 (debt structure, maturities and liquidity) and CP-5 (transaction and event read-through) at the located level.

### Strongest contrary evidence and limitations

1. Debt table and ladder are stale for the term loan. The 10-K ladder shows 2028 at "3,535.2" and a total of "5,078.3" (`page:155`), and the term loans then matured March 31, 2028 (`page:156`). The Q3 10-Q says the refinancing facility "will mature in March 2031" and amortizes 1.00% per annum (`page:16`). The 10-K ladder therefore cannot be used as the current wall. The Q3 report prints no new ladder (search of the Q3 10-Q for "maturities" found none), so a current ladder is a downstream derivation from the 10-K senior note maturities and the Q3 term loan terms.
2. Finance leases, other debt and revolver balance are not itemized at September 30, 2026. The Q3 fair-value table totals "5,017.5" (`page:30`) while the release prints "Total debt, excluding unamortized debt costs and discounts" of "5,249.7" (Q3 release `page:14`). The difference is tied out in `## Calculations` and is not described in the Q3 report. The Q3 10-Q does not state a revolver drawn balance; the 10-K table shows the revolver as "—" at December 31, 2025 (`page:154`) and the MD&A says the company had "access to $750.0 million of revolving loan commitments (without giving effect to $163.4 million of outstanding letters of credit)" (10-Q Q3 `page:51`).
3. No reported covenant ratio. The Revolving Credit Facility requires "a first lien net leverage ratio of less than or equal to 5.00 to 1.00" and "a minimum interest coverage ratio of 2.00 to 1.00" (10-Q Q3 `page:17`), and the company states it "was in compliance with all covenants" (`page:18`). Neither the first lien net leverage nor the interest coverage ratio as computed under the credit agreement is printed. The release's net leverage ratio of 3.32x (Q3 release `page:14`) is a management measure on total debt less unrestricted cash over TTM Adjusted EBITDA and is not stated to be the covenant definition.
4. Executed documents not supplied. The 10-K exhibit index lists the credit agreement and indentures by incorporation (`page:116` to `page:118`) and the pack contains none of their text. The springing maturity on the revolver is described only as "subject to a springing maturity based on conditions set forth in the Amended Credit Agreement" (10-Q Q3 `page:17`); the condition is not stated.
5. Management measures versus filings. Adjusted EBITDA, free cash flow, adjusted free cash flow and net leverage are non-GAAP and appear in the releases and the 10-Q MD&A; the filed statements control GAAP facts. The TTM Adjusted EBITDA of 1,436.1 combines a FY2025 figure, which the 10-K also prints (`page:86`), with nine-month figures from the Q3 release. For nine months 2026 the bridge runs from EBITDA of "977.6" to Adjusted EBITDA of "1,102.0", and its largest item is acquisition, integration and restructuring expenses of "91.2" (Q3 release `page:11`).
6. Comparability. The releases restate the 2025 comparison base to exclude exited operations (Q3 release `page:13`), and the discontinued operations line in 2025 (net loss of "(32.6)" for nine months 2025, Q3 10-Q `page:5`) has no 2026 counterpart. Prior-period amounts "have been reclassified to conform with the 2026 presentation" (Q3 10-Q `page:10`) without a reclassification schedule in the text read.
7. Contingent claims without estimates. The securities class action, the consumer class action and the Patane spring-water labelling class action are disclosed in Note 14 (`page:34` to `page:38`). The company states it is "unable to reasonably estimate the amount or range of possible loss, if any, in excess of the amounts accrued" (`page:34`). The Patane parties scheduled a second mediation for November 19, 2026 (`page:38`), after the cutoff, so any outcome is outside this pack.
8. Not supplied. Earnings presentations (the releases refer to a supplemental presentation on the company website, which is not in the pack), executed legal documents, market quotes, peers, valuation inputs, deal terms and a discrete Q4 2025 quarter. A Q4 2025 figure would be a downstream derivation from the 10-K and interim sources, not a source.
9. Extraction only. All seven files are text conversions; charts and images are not inspected, and successful extraction is not a fidelity review. Not every chunk was read line by line in this review; the chunks read are those cited.

### Consumer assessment

| Consumer | Status | Basis | Carried limitations |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Filed statements, notes, MD&A and releases for FY2025 and three 2026 quarters are present and located | Limitations 4, 6, 8, 9 |
| CP-1A | READY_WITH_LIMITATIONS | Statements, non-GAAP reconciliations, cash interest paid and cash taxes paid are present for quarter, nine months and FY2025 | Limitations 3, 5, 6, 8, 9 |
| CP-2 | READY_WITH_LIMITATIONS | Instrument table and ladder at December 31, 2025, refinancing terms, covenant levels, letters of credit, revolver commitments and ratings at September 30, 2026 | Limitations 1, 2, 3, 4, 7; no executed debt documents; guarantor and restricted-group perimeter unresolved |
| CP-5 | READY_WITH_LIMITATIONS | Subsequent-event disclosures (dividend and new repurchase program, Q3 10-Q `page:39`), the August 2026 secondary offering by Triton Water Equity Holdings (`page:61`), the Stock Purchase Agreement exhibit (`page:63`) and outlook | Limitations 4, 7, 8; the Stock Purchase Agreement text is not supplied |

No selected consumer is CONDITIONAL or BLOCKED on source grounds. These statuses do not assert that downstream analysis is complete or that any model input contract is accepted.

### Conflicts and checks between sources

No factual conflict between a filing and a release was found in the items compared. The Q3 release balance sheet matches the Q3 10-Q balance sheet line for line on the lines read (total assets "10,828.0", total liabilities "7,779.3", `page:4` of the 10-Q and `page:9` of the release). The release's "Unrestricted cash" of "477.2" differs from the balance sheet's "477.4" only by the "$0.2 million" of restricted cash that the release footnote and the 10-Q MD&A both state (Q3 release `page:14`; 10-Q `page:51`). The release and 10-Q Adjusted EBITDA for the quarter agree at "411.0" (release `page:11`; 10-Q `page:44`).

### Context fields that are blank

Ratings are blank in the context, but the Q3 10-Q prints ratings (`page:53`): Corporate / Family "B1" and "BB-", Senior Secured "Ba3" and "BB", Senior Unsecured "B3" and "B", with the row "Outlook Positive Neutral". The agency columns are read from the table header order (Moody's, then Standard and Poor's); the extraction does not show cell alignment, so the pairing of outlook to agency is by order only. These are company-reported statements as of September 30, 2026, not independent rating documents. Borrower, parent and guarantor fields are blank in the context while the filings name borrowers and guarantors (see the entity map).

## Calculations

No new analytical calculation is performed in this module. The tie-outs below test source consistency only and use figures copied from the cited sources. Units are USD millions.

| Check | Inputs | Result | Source locators |
| --- | --- | --- | --- |
| Total debt on the balance sheet | Current portion of long-term debt 74.4 plus long-term debt, less current portion 5,087.7 | 5,162.1, equal to "Total debt" of 5,162.1 in the release | 10-Q Q3 `page:4`; Q3 release `page:14` |
| Debt before unamortized costs | Total debt 5,162.1 plus unamortized debt costs and discounts 87.6 | 5,249.7, equal to the release figure | Q3 release `page:14` |
| Net debt | 5,249.7 less unrestricted cash 477.2 | 4,772.5, equal to the release figure | Q3 release `page:14` |
| TTM Adjusted EBITDA | FY2025 1,446.8 less nine months 2025 1,112.7 plus nine months 2026 1,102.0 | 1,436.1, equal to the release figure | 10-K `page:86`; Q3 release `page:11` and `page:14` |
| Net leverage ratio | 4,772.5 divided by 1,436.1 | 3.32x to two decimals, equal to the release | Q3 release `page:14` |
| Debt not in the fair-value table | Release debt before unamortized costs 5,249.7 less fair-value table carrying total 5,017.5 | 232.2; the Q3 report does not itemize it | 10-Q Q3 `page:30`; Q3 release `page:14` |
| Term loan principal roll | Refinanced principal 3,090.0 less "Repayment of Term Loans" of 7.7 in Q2 2026 and 7.8 in Q3 2026 | 3,090.0 less 15.5 is 3,074.5, equal to the term loan carrying value in the fair-value table; 1.00% per annum on 3,090.0 is 7.725 per quarter, consistent with the two payments | 10-Q Q3 `page:16`, `page:30`, `page:7`; 10-Q Q2 `page:7` |

The tie-outs show the release net leverage build reproduces from sources in the pack. They do not validate the Adjusted EBITDA adjustments and do not show the covenant ratio.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Citation |
| --- | --- | --- | --- | --- |
| Executed credit agreement, Fifth Amendment, indentures and other legal documents not supplied (context states none) | Medium | CP-2, CP-5 | Supply the executed documents for covenant definitions, springing maturity condition, guarantor lists, baskets and change-of-control terms | 10-K `page:116` to `page:118`; 10-Q Q3 `page:17` |
| No post-refinancing maturity ladder in a filing; 10-K ladder predates the March 2026 refinancing | Medium | CP-2 | Rebuild downstream from note maturities and the Q3 term loan terms, labelled as derived | 10-K `page:155`; 10-Q Q3 `page:16` |
| Finance leases, other debt and revolver drawn balance at September 30, 2026 not itemized | Medium | CP-2, CP-1A | Use the December 31, 2025 table as the last itemized view and label the 232.2 residual as unitemized | 10-Q Q3 `page:30`; 10-K `page:154` and `page:155` |
| Reported covenant ratios and headroom not printed | Medium | CP-2 | Not supplied; compute a management-basis proxy only and label that it is not the covenant definition | 10-Q Q3 `page:17`, `page:18` |
| Guarantor and restricted-group financial information not located | Medium | CP-2 | Supply guarantor disclosures if the restricted perimeter matters | 10-K `page:158` to `page:160` |
| Earnings presentations not in the pack | Low | CP-1, CP-1A | Not supplied; the releases and filings cover the reported facts | Q3 release `page:3` |
| Ratings, market quotes, peers, valuation inputs, deal terms blank in context | Medium | CP-2, CP-5 | Not supplied in the context; ratings are printed by the company in the 10-Q | context; 10-Q Q3 `page:53` |
| Discrete Q4 2025 quarter not supplied | Low | CP-1A | Derive downstream if needed; FY2025 less nine months 2025 | 10-K `page:126` |
| Estimates of possible loss beyond amounts accrued for the disclosed class actions not given | Medium | CP-1, CP-2 | None available in the pack | 10-Q Q3 `page:34` to `page:38` |
| Prior-period reclassification detail not located | Low | CP-1A | Check the statements note in the 10-K against the 10-Q comparatives | 10-Q Q3 `page:10` |
| Text-only extraction; images and charts not inspected; fidelity not reviewed | Low | All | Record as a parse limitation | All sources |

## Next module

Proceed to CP-1. Carry forward: the single registrant and one segment with co-issuer and guarantor entities named only in the debt notes; the pre-refinancing basis of the 10-K debt table and ladder; the absence of executed financing documents and of a reported covenant ratio; the company-reported ratings in the Q3 10-Q; the three disclosed class actions without loss estimates; and the non-GAAP basis of Adjusted EBITDA and net leverage. The next evidence action for the open gaps is to supply the credit agreement with the Fifth Amendment and the indentures if covenant headroom, the springing maturity or guarantor perimeter is to be analyzed.
