## Request

Issuer: ELDORADO GOLD CORP /FI (Eldorado Gold Corporation, ticker EGO; the registrant on the 40-F is "ELDORADO GOLD CORPORATION"). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot, host mode, minimum module set. Reporting currency: USD. Current period: Q3 2026 (quarter ended September 30, 2026). Prior period: FY2025.

Question for this module: can the effective source set support the requested work, and what remains blocked? This is a source-readiness handoff. It gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalize, reconcile or calculate figures.

Selected downstream consumers assessed here: CP-1, CP-1A, CP-2 and CP-5. No upstream handoff was supplied; this is the first module of the run.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 (as pinned) | Pages | Document family |
| --- | --- | --- | --- |
| 40-F_2025-12-31_ego-20251231_d2.htm.jsonl | 2d84dc109f346979ffc12a8e05f174bb9ee3c9bd6fcc72c5f9456622e3a05ce3 | 15 | Annual report cover document, Form 40-F, FY2025 |
| 6-K-EX-99.1_2026-03-31_eldoradogoldreportsfirstqu.htm.jsonl | 3b31b8f45b42d214b8f1d541ff63602490ab0a53167940d88fa15730bc28a118 | 34 | Earnings release, Q1 2026 (dated April 30, 2026) |
| 6-K-EX-99.1_2026-03-31_unauditedcondensedconsolid.htm.jsonl | 6ab28f2649ba0274d424a4a577f9d317100b3de9ac89fbdc0f56e73f18e3f38e | 22 | Unaudited condensed interim financial statements, Q1 2026 |
| 6-K-EX-99.1_2026-06-30_eldoradogoldreportsq22026f.htm.jsonl | 1bf15cab552e9fcdd05ecc97d7c3b6b694607e1283203ea2fc40315ad381fe66 | 41 | Earnings release, Q2 2026 (dated July 30, 2026) |
| 6-K-EX-99.1_2026-06-30_unauditedcondensedconsolid.htm.jsonl | 8eec4357e5c66f092a21b76dc3bc3ec04482a3d8fa39d15deb38a763bed500e0 | 28 | Unaudited condensed interim financial statements, Q2 2026 |
| 6-K-EX-99.1_2026-09-30_eldoradogoldreportsq32026f.htm.jsonl | 6528e78e0161f7a2d85b02006c1c676359a3ab495a586ed79cf2e7d97da5afc6 | 43 | Earnings release, Q3 2026 (dated October 28, 2026) |
| 6-K-EX-99.1_2026-09-30_unauditedcondensedconsolid.htm.jsonl | f32fd44e1756d4bad20e63e1b631e75cf54a1931414a7ce2b1f905276f2ab561 | 29 | Unaudited condensed interim financial statements, Q3 2026 |

The run context (sha256 a8b2bf5acce83dbd54227ec6757e97e8686f295cadb3f91a9fecf63c4f1d9423) holds dated settings only and is not issuer evidence. Its blank deal terms, quotes, ratings and peer fields are not read as zero. The pack file _retrieval.json is ignored by the run and is not evidence.

Hash note: each source file opens with a line of the form "Visible text of <file>, sha256 <hash>". That embedded hash identifies the original HTML document and differs from the pinned hash of the extracted text file listed above. The pinned hash is the one used in this handoff. The difference is expected and is not a conflict.

### Supplied handoffs

None. CP-0 is the first module in this run and received no upstream handoff, so there is no module and sha256 to list.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents support a credit snapshot of Eldorado Gold as of the third quarter of 2026, with limitations. Debt, covenants, the Foran acquisition and quarterly results are located in interim statements and releases. | Medium | The annual report is only a cover document. The audited FY2025 statements, annual report, management discussion and debt agreements are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Third quarter interim statements give a debt note listing senior notes, a revolving credit facility, project financing, Sprott and equipment facilities. | Debt by instrument can be taken from a filed note, but legal terms rest on summaries only. | Medium |
| The two financial covenant levels on the revolving facility are printed in the debt note. | Covenant levels are known; the issuer's reported ratios and headroom are not printed in the pack. | Medium |
| The annual report lists the audited statements, annual information form and management discussion as separate exhibits that were not supplied. | Full-year FY2025 income and cash flow figures cannot be sourced, which limits the prior-period comparison. | High |
| The Foran acquisition closed in April 2026 and its fair values are preliminary. | Acquired debt and goodwill figures may change within the measurement period, so they carry a limitation. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for the selected consumers, and no consumer is CONDITIONAL or BLOCKED. All seven sources are filed issuer documents with consistent identity (one registrant, one reporting perimeter, USD, IFRS interim statements under IAS 34), so no identity boundary is unresolved. The limitations are bounded and are listed below. Source sufficiency is not completion of downstream analysis; that is for the dependency planner and the later modules.

### Per-source assessment

| Source | Original authority and family | Entity and perimeter | Period and basis | Located content usable for the objective | Limitation |
| --- | --- | --- | --- | --- | --- |
| 40-F (FY2025) | Filed annual report on Form 40-F; cover document with forward-looking statements, controls, governance and exhibit index | Registrant Eldorado Gold Corporation, incorporated in Canada; no subsidiary or guarantor statements | Fiscal year ended December 31, 2025 | Currency statement and exchange rate, off-balance-sheet statement, exhibit index, auditor fee table | Contains no financial statements, debt note, liquidity or covenant text; those sit in exhibits not supplied |
| Q1 release | Issuer news release (management attributed) | Consolidated Eldorado Gold; segments Turkiye, Canada, Greece | Q1 2026 versus Q1 2025 | Production, costs, Skouries progress, non-IFRS reconciliations | Management narrative and non-IFRS measures; the management discussion it references is not supplied |
| Q1 statements | Filed interim statements (IFRS, IAS 34, unaudited) | Consolidated | Three months to March 31, 2026, with December 31, 2025 balance sheet | Debt note, derivative note, segment note, events after the reporting date (Foran completion) | Unaudited; condensed notes |
| Q2 release | Issuer news release | Consolidated | Q2 2026 and six months | Guidance update, Skouries and McIlvenna Bay, reconciliations | As above |
| Q2 statements | Filed interim statements | Consolidated, including Foran from April 14, 2026 | Three and six months to June 30, 2026 | Debt note including Foran acquired debt, commitments table, finance costs | Unaudited |
| Q3 release | Issuer news release | Consolidated | Q3 2026 and nine months; 2025 comparatives are continuing operations only | Highlights, guidance changes, Adjusted EBITDA reconciliation, corporate events | Non-IFRS measures; management discussion referenced but not supplied |
| Q3 statements | Filed interim statements; approved by the Board on October 28, 2026 | Consolidated | Three and nine months to September 30, 2026; balance sheet against December 31, 2025 | Full debt note, covenant text, commitments table, derivatives, segment debt, Foran purchase price allocation | Unaudited; Foran allocation provisional |

### Version relationships and duplicates

The three interim statement sets and three releases are successive period reports, not versions of one another. Each stays an active source. The Q3 statements carry the latest balance sheet and supersede earlier quarter-end positions only for facts as at September 30, 2026; earlier quarters remain the source for their own dates. No duplicate documents were found. Where a later quarter revises an earlier estimate (for example the McIlvenna Bay project capital estimate), both figures are retained with their dates.

### Original authority versus management claims

Filed interim statements control the balance-sheet, debt, covenant and commitment facts. The releases are management-attributed and control nothing against the statements. Where a release makes a statement about funding (for example that Skouries remains fully funded), it is recorded as a management claim.

### Coverage evidence by topic

| Topic | Located evidence | Source and locator |
| --- | --- | --- |
| Cash and restricted cash | "Cash and cash equivalents $ 396,828 $ 869,356" | Q3 statements, page:1 |
| Restricted cash for the term facility reserve | "Restricted cash 8 71,898 —" | Q3 statements, page:1 |
| Debt total | "$ 1,985,426 $ 1,275,052" | Q3 statements, page:11 |
| Senior notes | "$500.0 million senior unsecured notes with a coupon rate of 6.25% due September 1, 2029" | Q3 statements, page:11 |
| Project financing security and recourse | "The Term Facility is non-recourse to Eldorado Gold Corporation and is secured by the Skouries Project and the Hellas Gold operating assets." | Q3 statements, page:12 |
| Term facility repayment schedule | "Repayment of the Term Facility will commence on December 31, 2026, with 13 semi-annual installments, through to December 31, 2032." | Q3 statements, page:13 |
| Revolving facility amendment | "On August 12, 2026, the Company amended the Credit Facility, increasing total availability from $450 million to $600 million, extending the maturity to March 1, 2029" | Q3 statements, page:14 |
| Interest coverage covenant | "not less than 3.00:1.00" | Q3 statements, page:14 |
| Net leverage covenant | "not more than 3.50:1.00" | Q3 statements, page:14 |
| Revolving facility availability | "available balance on the Credit Facility was $274.7 million" | Q3 statements, page:14 |
| Sprott facility security | "secured by the realizable value of the acquired Foran assets and are subject to a Company guarantee" | Q3 statements, page:15 |
| Contractual maturities | "Debt - Senior Credit Facility $ — $ — $ 325,000" | Q3 statements, page:19 |
| Debt by segment | "Debt $ — $ 350,475 $ 818,424 $ 816,527 $ 1,985,426" | Q3 statements, page:28 |
| Foran completion | "On April 14, 2026, the Company announced the completion of Eldorado’s acquisition" | Q1 statements, page:22 |
| Foran provisional measurement | "have been measured on a preliminary basis" | Q3 statements, page:10 |
| Dividend declared after quarter end | "On October 28, 2026, the Company declared a fourth quarter dividend of $0.075 per common share" | Q3 statements, page:18 |
| Skouries funding statement (management) | "the project remains fully funded through available cash, operating cash flow and existing debt facilities" | Q3 release, page:8 |
| Adjusted EBITDA reconciliation | "Adjusted EBITDA $275.2 $196.3 $892.0 $571.1" | Q3 release, page:24 |
| Continuing-operations basis of 2025 comparatives | "exclude the Romania segment which was carried as a discontinued operation" | Q3 release, page:24 |
| Off-balance-sheet statement | "The Company does not have any off-balance sheet financing arrangements or relationships with unconsolidated special purpose entities." | 40-F, page:13 |
| Annual information form is an exhibit | "The Company’s AIF filed as Exhibit 99.1 to this annual report on Form 40-F is incorporated by reference herein." | 40-F, page:7 |
| Management discussion is an exhibit | "filed as Exhibit 99.3 to this annual report on Form 40-F is incorporated by reference herein." | 40-F, page:7 |
| Audited statements are an exhibit | "are filed as Exhibit 99.2 to this annual report on Form 40-F, and are incorporated by reference herein." | 40-F, page:7 |

### Consumer readiness

| Consumer | Rating | Basis and carried limitations |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Interim statements and releases give business, segment and operating evidence for Q3 2026. Carried limitations: no annual information form, no annual management discussion. |
| CP-1A | READY_WITH_LIMITATIONS | Foran transaction terms, purchase price allocation, McIlvenna Bay and Skouries status are located in the interim statements and releases. Carried limitations: provisional allocation; no ownership table located; the acquisition agreement is not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Debt by instrument, covenants, maturities, cash and Adjusted EBITDA reconciliations are located for Q3 2026. Carried limitations: FY2025 full-year statements, issuer-reported covenant ratios and indenture and credit agreement text are not supplied; liquidity inputs must be assembled from the statements. |
| CP-5 | READY_WITH_LIMITATIONS | Located evidence supports tracing of claims to filed statements. Carried limitation: any claim that depends on an unsupplied exhibit cannot be traced and must stay a gap. |

## Calculations

No new calculations are made in this handoff; the method forbids normalizing, reconciling or calculating figures at this stage. Coverage counts are the page counts given in the source table above (15, 34, 22, 41, 28, 43 and 29 pages). Page outlines of all pages in all seven sources were reviewed. The financial statement, debt, covenant, acquisition, commitment, segment and reconciliation pages were read in full. Mine-level operating narrative pages and the forward-looking statement pages in the releases were reviewed at heading level only, and the corresponding text extraction has not had a fidelity review against the original documents.

Derived figures noted for later modules but not computed here: liquidity (cash plus undrawn revolving capacity, with the restricted reserve excluded), net debt, leverage and covenant headroom.

## Gaps

| ID | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | Audited FY2025 consolidated financial statements (40-F Exhibit 99.2) not supplied. Full-year FY2025 income statement and cash flow are not available; only the December 31, 2025 balance sheet appears as a comparative in the interim statements. | High | CP-2, CP-5 | Supply Exhibit 99.2, or state FY2025 comparisons as Not supplied |
| G2 | Annual MD&A (Exhibit 99.3) and the quarterly MD&A referred to in each release are not supplied, including the "Financial Condition and Liquidity" sections. | Medium | CP-1, CP-2, CP-5 | Supply the MD&A or treat liquidity discussion as Not supplied |
| G3 | Annual Information Form (Exhibit 99.1) not supplied: no risk factor text, ownership detail or mineral reserve tables. | Medium | CP-1, CP-1A | Supply the AIF |
| G4 | Executed legal documents are not supplied: senior notes indenture, revolving credit agreement and its August 12, 2026 amendment, project financing facility, Sprott credit facility, equipment finance agreement, Foran arrangement agreement. Covenant text is known only from the note summaries. The context records legal documents as none. | Medium | CP-2, CP-5 | Legal terms stay summary-level; do not infer definitions |
| G5 | The issuer's reported covenant ratios and headroom are not printed in the supplied interim statements, which state only compliance. The Term Facility covenants are described only as "debt service and leverage ratios" with no levels printed. | Medium | CP-2 | Mark as Not supplied unless found in a later source |
| G6 | Foran purchase price allocation is preliminary; the note allows adjustment within the measurement period of up to one year. | Medium | CP-1A, CP-2 | Carry as provisional |
| G7 | 2025 comparatives in the Q3 release are continuing operations only, excluding the Romania segment disposed in Q4 2025; periods and perimeters must be matched before comparison. | Low | CP-2 | Label perimeter |
| G8 | The pro forma revenue disclosed for the Foran acquisition in the Q3 statements equals reported nine-month revenue at the stated rounding. It is recorded as an item to check and not as a conflict. | Low | CP-1A | Check against the note |
| G9 | Text extraction only. Charts, images and any speaker notes are not inspected; the releases carry image captions and photographs that text extraction cannot represent. No fidelity review of the extraction was performed. | Low | All | Treat figures as located text only |
| G10 | Stale-risk: the latest statements are as at September 30, 2026, five weeks before the as-of date. Events between October 28, 2026 and November 5, 2026 are not covered by any supplied source. | Low | CP-1A, CP-2 | State the as-at date on all balance figures |

No conflicts between documents were found in the pages read. The McIlvenna Bay project capital estimate was revised between the Q2 and Q3 releases and is a dated update, not a conflict. No draft, unsigned or superseded financial statements were found; the Q3 statements state approval by the Board on October 28, 2026.

## Next module

Proceed to CP-1, then CP-1A, CP-2 and CP-5 in the order CP-OS sequences them. Carry gaps G1 to G10 forward. The next evidence action is to read the Q3 statements and release for the business and operating model, citing page locators from the source table. Later modules must label every figure with its period (Q3 2026, nine months 2026, FY2025 balance sheet date) and perimeter, write Not supplied where an exhibit listed in G1 to G4 is the only source, and assemble liquidity from printed inputs only.
