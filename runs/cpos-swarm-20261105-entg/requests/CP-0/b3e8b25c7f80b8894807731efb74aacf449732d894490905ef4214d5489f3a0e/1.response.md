## Request

Issuer: ENTEGRIS INC (Entegris, Inc., Delaware registrant, NASDAQ: ENTG; issuer id entg). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency: USD; the filings report in US dollars, in millions except per-share data. Requested scope: can the seven supplied filings and releases support the follow-on work (financial data extraction, business and transaction context, fundamental credit synthesis and evidence-trace review), and what stays blocked. Current period is the quarter ended September 26, 2026 (Q3 2026) and the prior period is FY2025 (year ended December 31, 2025), as set in the context file. The context file holds the run settings only and is not issuer evidence; it names no borrower, parent, guarantor, sponsor, rating, quote or deal term, and none of those blank fields is treated as zero.

This module gives a source-readiness view only. It makes no credit conclusion, no legal interpretation and no new financial calculation (the method forbids normalizing or reconciling figures at this stage).

## Sources

### Issuer sources relied on

Each file is a text extraction of an EDGAR HTML document, split into numbered chunks. A `page:N` locator below means chunk N of that extraction, not the printed page. The sha256 is the pack file hash that CP-OS pinned. The first line of each chunk 1 carries a different hash, which is the hash of the original HTML document and not of the pack file.

| Source (exact name) | sha256 | Chunks |
| --- | --- | --- |
| `10-K_2025-12-31_entg-20251231.htm.jsonl` | `260dc4cc98d7ad114dcfe1b4d9e49beac9ed9f7c97f27f59e6df3a75c0628528` | 139 |
| `10-Q_2026-03-28_entg-20260328.htm.jsonl` | `3b83d32b0eaaaa1280f7799359a8f16448b715b610a83c1edceec0d49387802a` | 36 |
| `10-Q_2026-06-27_entg-20260627.htm.jsonl` | `5d06fd99ce42692b479a85d0b3d96bd08dbc1bdd295141cd5adf69b1988058ed` | 39 |
| `10-Q_2026-09-26_entg-20260926.htm.jsonl` | `7b5685a1d8fe745548fe7c65968e18c36857c1e4dd7f2b8045f8166b689f4db9` | 41 |
| `EX-99.1_2026-04-30_entgq12026ex991.htm.jsonl` | `0e10b62e7e542aab19ae90b6d94252e94c7183b272237a1b5ecd040e7a3bb9d7` | 9 |
| `EX-99.1_2026-08-04_entgq22026ex991.htm.jsonl` | `729b6288fa7f91f06fa1d1330da9031db0436138ba5a59730b16535055ac78c0` | 9 |
| `EX-99.1_2026-10-29_entgq32026ex991.htm.jsonl` | `e35116403bbcb30c3a986093aa969493d265b238a073d77c0b1aa4aec9296a99` | 10 |

Run settings (not issuer evidence): `context`, sha256 `a75dcef49bab6da60dc1054c04d1bf4409ccb60667119c9ab2f0bfc98a4c262f`. The file `_retrieval.json` in the pack folder was ignored by CP-OS and is not used.

### Upstream handoffs

None. CP-0 is the first module of this run; CP-OS supplied no handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and releases are sufficient for a credit snapshot of Entegris, with limitations. Statements, debt, segment and liquidity data through September 26, 2026 are located. Legal financing documents and covenant calculations are not supplied. | Medium | Executed credit agreement and indentures, revolver letters of credit, the covenant test threshold and guarantor details are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The latest debt note lists par debt of $3,295.0 million and no revolver borrowings at September 26, 2026. | Debt and maturity analysis can proceed from filed statements. | High |
| Annual report notes are captioned in thousands but show millions; the latest quarterly report says amounts are in millions. | Treat all amounts as USD millions and flag the caption conflict. | High |
| Revolver commitments are $750.0 million, but letters of credit and the threshold for the 5.20 to 1.00 leverage covenant are not printed. | Net revolver availability and covenant headroom cannot be calculated from the pack. | High |
| Quarterly results for the first three quarters of 2026 and prior-year comparatives are in the filings and releases. | Quarter, year-to-date and last-twelve-month views can be built from filed figures. | High |
| A January 2026 change in useful lives cut depreciation by $55.6 million over nine months. | Operating income and margin comparisons with 2025 are affected. | High |

### Readiness view

The effective source set supports the requested work with bounded limitations; the overall view is READY_WITH_LIMITATIONS. The pack holds one audited annual report (FY2025), three unaudited quarterly reports (Q1 to Q3 2026) and three earnings releases, all for one reporting entity, Entegris, Inc. and subsidiaries on a consolidated basis. Filed statements control financial facts; the earnings releases are management documents that supply attributed non-GAAP measures and the fourth-quarter outlook, and they do not override the filings. No source is blocked, no extraction failure was seen, and no draft or unsigned document is in the pack. Each filing carries a signature block and the annual report carries an unqualified auditor opinion. The limits come from what the pack omits: no executed financing document, no covenant calculation, no letter-of-credit figure and no guarantor schedule. These bound the debt-terms, liquidity-headroom and creditor-structure work but do not stop it.

| Downstream owner | Readiness | Evidence supplied | Bounded limitation |
| --- | --- | --- | --- |
| CP-1 financial data | READY_WITH_LIMITATIONS | Statements, debt note, maturities, cash flow, segments and interim comparatives (see source review) | Letters of credit, covenant threshold and ratio, and interim lease detail are not supplied |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Annual business description, risk factors, segment and customer-concentration text, quarterly narrative, October 2026 release | No sponsor, parent, deal terms or ownership document; the context file names none |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Same evidence, through the upstream handoffs | Inherits all gaps below; no ratings, quotes or market data supplied |
| CP-5 evidence trace review | READY_WITH_LIMITATIONS | Pack text for quote checks | Inherits the unit-caption conflict and the gaps below |

A missing downstream handoff is not a readiness condition; the dependency order of CP-OS sequences it.

### Source-by-source review

| Source | Family and authority | Entity and period basis | Located content (chunks) | Limits |
| --- | --- | --- | --- | --- |
| Annual report (10-K) | Filed annual report; audited; controls FY2025 facts | Entegris, Inc. and subsidiaries, consolidated; year ended December 31, 2025, with 2024 and 2023 comparatives; auditor opinion dated February 10, 2026 (`page:105`); signed February 10, 2026 (`page:101`) | Business `page:4`; covenant risk factor `page:56`; MD&A liquidity and debt table `page:78`-`page:81`; cash-requirements table `page:81`; exhibit list `page:96`-`page:100`; balance sheet `page:105`-`page:106`; income statement `page:106`; Note 9 debt `page:120`-`page:121`; Note 13 leases `page:123`-`page:124`; Note 18 benefit plans `page:135`; Note 20 segments `page:136`; Notes 22 and 23 `page:139` | Table captions say thousands but show millions (conflict C1); contracts are listed as exhibits but not supplied |
| 10-Q for quarter ended March 28, 2026 | Filed interim report; unaudited | Same entity; three months ended March 28, 2026 and March 29, 2025; signed April 30, 2026 | Statements `page:4`-`page:7`; Note 5 debt `page:11`; Note 11 subsequent events `page:15` (revolver amendment of April 29, 2026); liquidity `page:25`-`page:28` | Compliance with the financial covenant is stated (`page:27`) but its level is not stated |
| 10-Q for quarter ended June 27, 2026 | Filed interim report; unaudited | Same entity; three and six months ended June 27, 2026; signed August 4, 2026 | Statements `page:4`-`page:7`; Note 5 debt `page:11`; revolver amendment `page:21`; Note 11 `page:17`; liquidity and covenant `page:28`-`page:31` | Six-month, not nine-month, basis |
| 10-Q for quarter ended September 26, 2026 | Filed interim report; unaudited; latest filed statements before the as-of date | Same entity; three and nine months ended September 26, 2026 and September 27, 2025; signed October 29, 2026 (`page:41`) | Balance sheet `page:4`; operations `page:5`; cash flows `page:6`-`page:7`; Note 1 unit statement and useful-life change `page:8`-`page:9`; Note 5 debt `page:11`-`page:12`; segments `page:14`-`page:16`; Note 11 `page:17`; liquidity, covenant and cash split `page:32`-`page:35`; non-GAAP reconciliations `page:38`-`page:39`; exhibits `page:41` | Interim notes omit leases, benefit plans and tax detail; the covenant threshold is not stated |
| Earnings release dated April 30, 2026 | Management document furnished as Exhibit 99.1; attributed claims and non-GAAP measures | Same entity; first quarter 2026 | Headline results, statements, reconciliations; printed pages 2 to 12 of 12 present | Text only; slides are not in the pack |
| Earnings release dated August 4, 2026 | Same | Same entity; second quarter 2026 | Same structure; printed pages 2 to 13 of 13 present | Same |
| Earnings release dated October 29, 2026 | Same | Same entity; third quarter 2026 | Results `page:1`; fourth-quarter outlook `page:2` and `page:10`; statements `page:5`-`page:6`; reconciliations `page:7`-`page:10`; end marker and printed page 13 of 13 present in `page:10` | Text only; outlook is management expectation; a Capital Markets Day on November 9, 2026 (`page:1`) is a future event after the as-of date |

### Coverage of the evidence needed

| Evidence demand | Where it is located | Status |
| --- | --- | --- |
| Debt instruments, rates, maturities | Q3 10-Q Note 5 `page:11`; annual Note 9 `page:120` | Located: five instruments and an undrawn revolver; par total $3,295.0 million at September 26, 2026 against $3,745.0 million at December 31, 2025 |
| Maturity profile | Q3 10-Q `page:11`: $400.0 million in 2028, $2,000.0 million in 2029, $895.0 million in 2030 | Located |
| Revolver terms | Q3 10-Q `page:12`, `page:34`: $750.0 million commitments, maturity April 29, 2031, amended April 29, 2026 | Located; contract not supplied |
| Covenant | Q3 10-Q `page:34`: maximum first lien net leverage ratio 5.20 to 1.00, tested only above a specified revolver utilisation; compliance stated | Test level located; threshold and reported ratio not supplied |
| Cash and its location | Q3 10-Q `page:34`: $58.3 million U.S., $298.2 million non-U.S., total $356.5 million | Located |
| Cash flow and cash-paid interest and tax | Q3 10-Q `page:6`-`page:7` | Located for nine months 2026 and 2025 |
| Discrete quarters, year-to-date and prior year | Q1, Q2, Q3 statements and the three releases; FY2025 annual statements | Located; the fourth quarter of 2025 is not presented on its own |
| Segments and geography | Q3 10-Q `page:14`-`page:16`; annual Note 20 `page:136` | Located |
| Add-backs and non-GAAP bridges | Q3 10-Q `page:38`-`page:39`; Q3 release `page:7`-`page:10` | Located; management-defined |
| Leases, benefit plans, commitments | Annual Notes 13, 18, 22 | Located at December 31, 2025 only; the Q3 10-Q shows a long-term lease liability of $100.4 million on the balance sheet (`page:4`) with no interim lease note |
| Litigation and contingencies | Annual Note 22 `page:139`; Q3 10-Q Part II Item 1 `page:40` | Located; both state no material expected effect |
| Subsequent events to the as-of date | Q3 10-Q Note 11 `page:17`: dividend of $0.10 per share declared October 14, 2026 and payable November 18, 2026 | Located; no other subsequent event is disclosed |

### Conflicts and distinctions kept open

| Ref | Conflict or distinction | Locators | Downstream effect |
| --- | --- | --- | --- |
| C1 | The annual report captions debt maturities, fair value and lease tables "(In thousands)", but the values (for example total debt $3,745.0) match the millions used in the statements. The Q3 10-Q says the thousands captions were wrong, the amounts are millions and no revision is needed. | `10-K page:120`, `page:122`, `page:123`; `10-Q Q3 page:9` | Treat every amount as USD millions. CP-1 should record the caption conflict and not scale values. |
| C2 | The 10-K prints the 2029 maturity as "2,450" and the 2030 maturity as "895" without decimals. | `10-K page:120` | Display only; the total of $3,745.0 is consistent with the debt table. |
| C3 | Note rates are printed at three decimals in the annual report and at two in the Q3 10-Q (3.625% and 4.375% against 3.63% and 4.38%). | `10-K page:120`; `10-Q Q3 page:11` | Rounding of the same instruments; use the three-decimal form. |
| C4 | The 10-K was signed and audited on February 10, 2026, while the Q3 10-Q and the Q3 release say it was filed on February 11, 2026. | `10-K page:101`, `page:105`; `10-Q Q3 page:4`; `EX-99.1 Q3 page:5` | A signing date and a filing date can differ; no effect on figures. |
| C5 | The releases show "Interest expense, net" (for the third quarter of 2026, $43.9 million); the 10-Q shows interest expense of $45.4 million and interest income of $1.5 million separately. | `EX-99.1 Q3 page:5`; `10-Q Q3 page:5` | Presentation difference; the filing controls. |
| C6 | Useful-life change: from January 2026, depreciation fell by $17.9 million in the third quarter and $55.6 million over nine months, with an expected reduction of about $73.0 million for 2026. | `10-Q Q3 page:9`, `page:21` | 2026 operating income and margins are not like-for-like with 2025. Adjusted EBITDA adds depreciation back. |
| C7 | The third quarter includes $8.3 million of IEEPA tariff refunds recognised in cost of sales and excluded from non-GAAP results as out-of-period. | `10-Q Q3 page:38` | Reported and adjusted gross margin differ. |
| C8 | The term loan carried 5.43% at March 28, 2026 and 5.40% at June 27, 2026, against 4.88% at December 31, 2025; it was repaid in full by September 26, 2026. | `10-Q Q1 page:11`; `10-Q Q2 page:11`; `10-K page:120`; `10-Q Q3 page:12` | Dated rates, not a conflict. Revolver margins moved from 1.50% and 0.50% at June 27, 2026 to 1.25% and 0.25% at September 26, 2026 (`10-Q Q2` and `10-Q Q3`). |

Version relationships: the annual report and the three quarterly reports are separate periodic filings, not amendments of one another; the three releases are separate management documents, each dated the same day as the related 10-Q was signed. None replaces another. No duplicate documents are in the pack. The revolver amendment of April 29, 2026 is described in the Q1, Q2 and Q3 10-Qs; the amendment document itself is not supplied.

### Perimeter and roles

The reporting entity is Entegris, Inc. with its subsidiaries; the filings present consolidated figures only. The Q3 10-Q describes two operating segments, Materials Solutions and Advanced Purity Solutions (`page:14`). The annual exhibit list names "certain subsidiaries" as parties to the notes indentures and as guarantors under the 2022 credit agreement amendment (`10-K page:97`), but no guarantor list, restricted or unrestricted subsidiary split, or subsidiary schedule is supplied in text. Instrument roles that are printed: senior secured notes due 2029 (4.75%), senior unsecured notes due 2030 (5.95%), 2029 (3.625%) and 2028 (4.375%), the revolving credit facility due 2031, and the term loans B due 2029 (repaid). Whether co-issuers exist is not stated in the pack text.

## Calculations

No new financial calculation was made, as the method requires. The counts below are the only derived numbers.

| Item | Inputs | Result |
| --- | --- | --- |
| Source chunks in the pack | 139 + 36 + 39 + 41 + 9 + 9 + 10 | 283 chunks across seven sources |
| Issuer sources assessed | 10-K, three 10-Qs, three releases | 7 of 7 |
| Releases with the full printed page sequence | Q1 release pages 2 to 12 of 12; Q2 and Q3 releases pages 2 to 13 of 13 | 3 of 3 |

Figures quoted above are copied from the cited chunks, not recomputed.

## Gaps

| Ref | Gap | Severity | Consumers affected | Remediation |
| --- | --- | --- | --- | --- |
| G1 | Executed credit agreement, the April 29, 2026 revolver amendment, the indentures and the equal-priority intercreditor agreement are listed as exhibits (`10-K page:96`-`page:97`) but not supplied. Terms are known only from the filings' summaries. | Medium | CP-1, CP-2, CP-5 | Add the EDGAR exhibits if legal terms (baskets, guarantees, security) are needed. Not supplied. |
| G2 | The revolver utilisation threshold that triggers the 5.20 to 1.00 first lien net leverage test, and the reported ratio, are not printed. A search of all seven sources found only the compliance statement (`10-Q Q3 page:34`). | Medium | CP-1, CP-2 | Covenant headroom is Not calculable from the pack. Obtain the credit agreement or the compliance certificate. |
| G3 | Letters of credit issued under the revolver are not supplied. A search of all seven sources for "letter of credit", "letters of credit", "standby" and "LC" found only a risk-factor mention (`10-K page:56`). Undrawn revolver availability net of letters of credit is therefore Not calculable; the $750.0 million commitment and zero borrowings are printed (`10-Q Q3 page:12`). | Medium | CP-1, CP-2 | Obtain the letter-of-credit balance from the credit agreement notices or a later filing. |
| G4 | No guarantor list, subsidiary schedule or restricted and unrestricted split is in the pack text (`EX-21` is filed with the annual report but not supplied). | Medium | CP-1A, CP-2 | Add EX-21 and the guarantee terms if structural analysis is requested. |
| G5 | Interim reports carry no lease, benefit-plan, tax or commitments notes. The latest detail is at December 31, 2025 (leases total $114.4 million, `10-K page:124`; cash requirements `10-K page:81`). The Q3 10-Q states no material change to cash requirements outside the ordinary course except the term loan repayment (`page:35`). | Low | CP-1, CP-2 | Label these items as of December 31, 2025. |
| G6 | The caption conflict C1 remains unresolved in the annual report text; only the Q3 10-Q statement resolves it. | Low | CP-1, CP-5 | Carry as a stated limitation. |
| G7 | Quarterly slide presentations are not in the pack; the Q3 release says slides are posted on the company website (`EX-99.1 Q3 page:2`). Management commentary beyond the release text is Not supplied. No claim is made about charts or images. | Low | CP-1A | Use release text as attributed management language only. |
| G8 | The fourth quarter of 2025 is not presented on its own; a last-twelve-month view needs FY2025 plus nine months 2026 less nine months 2025, all of which are printed. | Low | CP-1 | CP-1 may derive it and show the inputs. |
| G9 | No ratings, market quotes, peer data, valuation inputs or sponsor facts are in the pack or the context file (all blank). | Low for the snapshot; higher for valuation work | CP-2 | Not supplied; do not treat as zero. |
| G10 | The fourth-quarter outlook and the Capital Markets Day (November 9, 2026) are management statements about the future, dated before the cutoff but describing later dates. | Low | CP-1A, CP-2 | Carry as management expectation, not fact. |

## Next module

Proceed to CP-1 (financial data extraction), then CP-1A, CP-2 and CP-5, each marked READY_WITH_LIMITATIONS. Instructions for the next modules:

- Treat all amounts as USD millions and record conflict C1 as a stated limitation.
- Build the debt table from `10-Q Q3 page:11`-`page:12`, with FY2025 from `10-K page:120`, and show the maturity wall from `10-Q Q3 page:11`.
- Do not state revolver availability net of letters of credit or covenant headroom; write Not calculable with the reason (G2, G3).
- Use filed statements for facts and the releases only as attributed management language, including the outlook.
- Label lease, benefit-plan and commitment figures as of December 31, 2025 (G5), and show the inputs for any last-twelve-month figure (G8).
- Flag the useful-life change (C6) and the tariff refund (C7) wherever 2026 margins are compared with 2025.
- Do not describe any guarantor, security package or co-issuer beyond what the supplied text prints (G1, G4).
