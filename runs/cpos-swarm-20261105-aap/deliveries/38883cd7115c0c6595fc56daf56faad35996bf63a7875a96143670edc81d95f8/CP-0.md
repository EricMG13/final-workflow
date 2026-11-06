## Request

Module CP-0, source readiness, for ADVANCE AUTO PARTS INC (issuer id aap, registrant Advance Auto Parts, Inc., NYSE: AAP), pathway credit_snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05, reporting currency USD. The run asks whether the pinned source set can support the selected downstream consumers CP-1, CP-1A, CP-2 and CP-5, and what remains blocked. This module gives no credit conclusion and calculates no financial figure. Source sufficiency is not completion of downstream analysis, and no downstream input contract is evaluated here (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

Period labelling in the context does not match the sources, and this module records the mismatch instead of relabelling. The context names current period q2-2027 and prior period fy-2026. The pack contains no period called q2-2027 or fy-2026. Its latest periodic filing covers the twelve weeks and forty weeks ended October 10, 2026 (third quarter of fiscal 2026), and its latest annual filing covers fiscal 2025, the fifty-three weeks ended January 3, 2026. Downstream modules should label figures with the periods the filings print (Q3 FY2026, forty weeks 2026, FY2025) and should not adopt the context labels without a correction from the requester. The currency is USD in millions throughout, which matches the context.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2026-01-03_aap-20260103.htm.jsonl | 88f0e66024a1a4e436956477a1b2bdacaf04082e37a839a013e4cf7b08a76ecc | Annual report on Form 10-K, filed statements; controlling for FY2025 audited facts | Fiscal year ended January 3, 2026, fifty-three weeks, consolidated, USD millions |
| 10-Q_2026-04-25_aap-20260425.htm.jsonl | b2dda8d971a035721b55c0b12971db6aed3046b92a0ea3374bd34ecc4d16e660 | Quarterly report on Form 10-Q, unaudited filed statements | Sixteen weeks ended April 25, 2026 (Q1 FY2026), consolidated |
| 10-Q_2026-07-18_aap-20260718.htm.jsonl | d30e886360cdf677d2862f5aa362e3322f6a90f56e6bf5994651f2a56dce1ba0 | Quarterly report on Form 10-Q, unaudited filed statements | Twelve and twenty-eight weeks ended July 18, 2026 (Q2 FY2026), consolidated |
| 10-Q_2026-10-10_aap-20261010.htm.jsonl | 32c4d101ba1517004b623cd5dd9218257b19e48552a751844ca10c65f72b2dcf | Quarterly report on Form 10-Q, unaudited filed statements; latest filed period | Twelve and forty weeks ended October 10, 2026 (Q3 FY2026), consolidated |
| EX-99.1_2026-05-21_aap-ex99_1.htm.jsonl | 281142b5117a0fb7df01ee4cf7cccfd81f8a80502e2274192453a4d9bcd9063f | Earnings release furnished as Exhibit 99.1; management presentation with non-GAAP measures | Q1 FY2026, release dated 2026-05-21 |
| EX-99.1_2026-08-20_aap-ex99_1.htm.jsonl | 6fa6d0f76f705af9a8078a4e1b4a20159ae0682aa896d374dffc425d834ff4a2 | Earnings release furnished as Exhibit 99.1; management presentation with non-GAAP measures | Q2 FY2026, release dated 2026-08-20 |
| EX-99.1_2026-11-05_aap-ex99_1.htm.jsonl | de47b06e79c571c89947b08d25437b94293b8641bb8475120032ad32f61878b9 | Earnings release furnished as Exhibit 99.1; management presentation with non-GAAP measures | Q3 FY2026, release dated 2026-11-05 |

### Other pinned input

| Input | sha256 | Use |
| --- | --- | --- |
| context (context sha256) | ffcc1267b075abb958b7ec70e65c9102a0d2613c38bcd4fb41ec20b2a4c808c3 | The requester's dated settings. It is not issuer evidence. It names no borrower, parent, guarantor, sponsor, deal term, quote, rating or peer, and it sets legal_documents to none. |

The pack also held a file named _retrieval.json, which CP-OS ignored and which this module did not use.

### Handoffs

| Module | sha256 | Note |
| --- | --- | --- |
| None supplied | Not applicable | CP-0 is the first module in this run. No upstream handoff exists, so none was consumed. |

### Short names used below

The short names 10-K FY2025, 10-Q Q1, 10-Q Q2, 10-Q Q3, Release Q1, Release Q2 and Release Q3 refer, in the order of the table above, to the seven issuer sources. A locator `page:N` is the source chunk number in the pinned file, not the printed page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases support the planned financial, business, synthesis and evidence-trace work for this issuer, with stated limits. Nothing is blocked on identity or extraction, and no source needs to be excluded. | Medium | No loan or bond agreements, guarantor list, credit ratings or investor presentations were supplied, so legal terms rest on the filings' summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Financial statements, debt note, liquidity and covenant description are present for the latest annual and all three quarterly periods. | Debt and liquidity work can start from filed statements rather than management claims. | High |
| The latest quarterly filing does not repeat the debt table by series after the repurchases. | The current debt stack must be rolled forward from the annual table and carries that limit. | Medium |
| The covenant is described as springing, with no reported ratio. | Covenant headroom cannot be shown from reported figures. | Medium |
| The context period labels do not match the filings. | Periods must follow the filings until the requester corrects the labels. | High |

### Readiness view

The effective source set can support CP-1, CP-1A, CP-2 and CP-5 for this issuer. The view for each is READY_WITH_LIMITATIONS: the owner can perform its method on located filed evidence, and the gaps below are bounded and carried forward rather than blocking. No consumer is CONDITIONAL or BLOCKED, because no identity boundary is unresolved, no source has blocked preparation, and every missing item (agreements, ratings, guarantor list, presentations) limits depth of legal or market analysis without preventing the owner's workflow. This view is source sufficiency only. It does not establish that CP-1 will find clean quarterly inputs, that any figure reconciles, or that downstream modules will accept their inputs.

| Consumer | View | Evidence it demands and what is present | Limitations carried forward |
| --- | --- | --- | --- |
| CP-1 (financial and credit data) | READY_WITH_LIMITATIONS | Statements of operations, balance sheets, cash flows, debt note, ABL description, leases, supplier finance and non-GAAP leverage reconciliation, for FY2025 and each of Q1, Q2 and Q3 FY2026 | Gaps G1 to G6, G9 and G10 |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, store base, trade names, restructuring, the Worldpac sale, the August 2025 notes issuance and ABL replacement, management commentary in the releases | Gaps G2, G3, G7 and G8; no sponsor or transaction documents exist or were supplied |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Draws only on upstream registers. The sources supply the evidence those registers need | Inherits every limitation of CP-1 and CP-1A. Missing ratings and market data are gaps, not adverse findings |
| CP-5 (evidence trace validator) | READY_WITH_LIMITATIONS | Seven pinned, fully paged text sources against which quotes can be matched | Extraction is text only, with flattened tables (gap G10), so figure placement is checked by order of cells |

### Coverage of the pack

Every page of every source was retained as extracted text: 226 of 226 pages across the seven sources (110 of 110, 26 of 26, 27 of 27, 29 of 29, 11 of 11, 12 of 12 and 11 of 11 pages in table order). Page numbering is continuous in each file. No image, chart, scan, workbook or speaker-note content exists in the pack, so no inspected-image coverage is claimed. Extraction status is not a fidelity review: tables arrive as one value per line, negatives are split across lines, and no layout check was possible.

### Source-by-source assessment

| Source | Document family and authority | Entity and perimeter | Period and basis | Version relationship | Locator and quote |
| --- | --- | --- | --- | --- | --- |
| 10-K FY2025 | Filed annual report with audited statements and an unqualified opinion on internal control; controlling for FY2025 | Advance Auto Parts, Inc. and subsidiaries, consolidated; Worldpac shown as discontinued operations | Fifty-three weeks; comparatives are two fifty-two week years | Base annual report; no amendment in the pack | 10-K FY2025 page:1 "For the fiscal year ended January 3, 2026" |
| 10-K FY2025 (week count) | Same | Same | Same | Same | 10-K FY2025 page:4 "included fifty-three weeks of operations" |
| 10-Q Q1 | Filed unaudited interim report | Same consolidated perimeter | Sixteen-week first quarter | Separate from the 10-K; not superseded by later 10-Qs because each covers a different period | 10-Q Q1 page:1 "For the quarterly period ended April 25, 2026" |
| 10-Q Q2 | Filed unaudited interim report | Same | Twelve-week quarter and twenty-eight weeks year to date | Separate period | 10-Q Q2 page:1 "For the quarterly period ended July 18, 2026" |
| 10-Q Q3 | Filed unaudited interim report; latest filed period; signed November 5, 2026 | Same | Twelve-week quarter and forty weeks year to date | Separate period; cutoff day equals signature day | 10-Q Q3 page:1 "For the quarterly period ended October 10, 2026" |
| Release Q1 to Release Q3 | Furnished earnings releases; management claims and non-GAAP measures, subordinate to the filings | Same consolidated perimeter | Quarter, year to date and four-quarter-ended bases, stated per table | Three separate releases, each retained; the Q3 release is dated on the cutoff day | Release Q3 page:1 "Advance Auto Parts Reports Third Quarter 2026 Results; Updates Full Year 2026 Guidance" |

### Perimeter and instrument roles

The registrant and the issuer of record is Advance Auto Parts, Inc., a Delaware corporation. It is also the borrower under the asset-based revolving facility, and its subsidiaries guarantee the senior unsecured notes. No parent, sponsor or separate borrower exists in the sources; the company is listed on the New York Stock Exchange.

| Role | Evidence | Locator and quote |
| --- | --- | --- |
| Notes guaranteed by subsidiaries | The notes are guaranteed on an unsubordinated, unsecured basis; guarantor identities are defined by the indentures, which are not in the pack | 10-K FY2025 page:89 "fully and unconditionally guaranteed, jointly and severally, on an unsubordinated and unsecured basis" |
| ABL borrower and guarantors | The company is the borrower; guarantors are the note guarantors plus certain Canadian subsidiaries | 10-K FY2025 page:91 "Advance Auto Parts, Inc. is the ABL Facility borrower" |
| Guarantor list | An exhibit listing the issuer and guarantor subsidiaries is indexed but not supplied | 10-Q Q3 page:28 "List of the Issuer and its Guarantor Subsidiaries" |

### Financing evidence present

| Item | Locator and quote | Readiness note |
| --- | --- | --- |
| Debt by series at fiscal year end 2025 | 10-K FY2025 page:87 "Total principal amount of long-term debt and current maturities of long-term debt" | Series, coupons, maturities and principal are printed for January 3, 2026 and December 28, 2024 |
| Maturity schedule | 10-K FY2025 page:89 "the aggregate future annual maturities of long-term debt instruments were as follows" | Printed as of January 3, 2026 only |
| 2025 issuance | 10-K FY2025 page:87 "the Company issued (i) $975 million in aggregate principal amount of 7.000% Senior Notes due 2030" | The paired 2033 notes are printed in the same paragraph and table |
| Repurchases and reclassification in FY2026 | 10-Q Q3 page:11 "reclassified $349 million of long-term debt to current liabilities" | Narrative only; see gap G1 |
| Principal due within twelve months | 10-Q Q3 page:26 "$350 million of outstanding principal due within the next twelve months" | Management discussion text |
| ABL availability | 10-Q Q3 page:12 "$894 million and $896 million of borrowing availability" | Includes letters of credit outstanding under the facility in the same sentence |
| ABL borrowings | 10-Q Q3 page:12 "had no outstanding borrowings under its asset-based loan revolving credit facility" | Both balance dates |
| Springing covenant | 10-K FY2025 page:91 "a springing financial covenant that would result in a fixed charge coverage ratio maintenance requirement" | Test level is printed; no reported ratio (gap G3) |
| Covenant level | 10-K FY2025 page:91 "which requires a minimum 1:1 coverage ratio to be maintained" | Definition is by reference to the ABL agreement |
| Availability conditions on qualified cash | 10-Q Q3 page:12 "maintaining excess availability under the ABL Facility of at least $400 million" | Qualified cash is described as unrestricted subject to these conditions |
| Supplier finance | 10-Q Q3 page:14 "were $2.6 billion and $2.5 billion, respectively" | Recorded in accounts payable; large relative to funded debt, so it matters to liquidity analysis |
| Lease liabilities in leverage metric | Release Q3 page:10 "Add: Operating lease liabilities" | Management's measure; the 10-Q balance sheet shows only the non-current portion |
| Management leverage metric | Release Q3 page:11 "The net leverage ratio calculated by the Company is a Non-GAAP measure" | Attributed to management; it does not override the filings |

### Business and transaction evidence present

| Item | Locator and quote | Readiness note |
| --- | --- | --- |
| Business description | 10-K FY2025 page:4 "leading automotive aftermarket parts provider in North America" | Full business section, store counts and trade names present |
| Single reportable segment | 10-Q Q3 page:15 "the Company has one operating segment" | No segment tables exist to extract, so CP-1 should not expect any |
| Worldpac disposal | 10-K FY2025 page:5 "the Company completed the sale of the Worldpac business for net proceeds of approximately $1.44 billion after transaction costs" | Completed transaction; a final working-capital payment is described in the FY2026 10-Qs |
| Post-quarter event before cutoff | Release Q3 page:2 "On October 26, 2026, the Company declared a regular cash dividend of $0.25 per share" | Subsequent to the quarter end, before the cutoff |
| Management goal on rating | Release Q3 page:11 "re-establish an investment grade rating" | Management language; no agency rating is in the pack |

### Control environment evidence

| Item | Locator and quote | Readiness note |
| --- | --- | --- |
| Internal control conclusion at fiscal year end | 10-K FY2025 page:60 "internal control over financial reporting was effective to accomplish their objectives at the reasonable assurance level" | Audited, with an unqualified attestation |
| Remediation cost reference | 10-K FY2025 page:46 "previously-disclosed material weaknesses in internal control over financial reporting" | The weaknesses are referred to as earlier disclosures and are not described in the pack (gap G8) |
| Latest quarter | 10-Q Q3 page:27 "disclosure controls and procedures were effective" | Quarter ended October 10, 2026 |

### Conflicts

No conflict between sources was found that changes a downstream figure. Three pairs look different but share one basis and are recorded so later modules do not treat them as conflicts. Debt is $3.4 billion of principal in the quarterly discussion and a smaller carrying amount on the balance sheet, which is principal against carrying value net of discounts. The release counts all operating lease liabilities while the balance sheet line is non-current only. Management's net leverage moved between the three releases on its own definition and four-quarter basis.

## Calculations

No financial figure, ratio or reconciliation was calculated in this module, as the method requires. The only counts are the coverage counts in the Findings section.

| Count | Inputs | Result |
| --- | --- | --- |
| Pages retained across the seven issuer sources | 110 + 26 + 27 + 29 + 11 + 12 + 11 | 226 |
| Pages that are continuous from 1 to the last page | One check per file, seven files | 7 of 7 files |
| Consumers assessed | CP-1, CP-1A, CP-2, CP-5 | 4 of 4, all READY_WITH_LIMITATIONS |

## Gaps

| ID | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | The 10-Q Q3 gives no debt table by series after the FY2026 repurchases of two note series. Principal per series at October 10, 2026 is not printed. Only total principal in the discussion, the repurchase narrative and the carrying amounts are. | Medium | CP-1, CP-2 | Roll forward from the FY2025 table, label it derived, and keep the narrative amounts as the cited support. |
| G2 | No indentures, supplemental indentures or ABL agreement text were supplied. The context sets legal_documents to none. Redemption terms, covenants other than those summarised, and the line cap definition rest on the 10-K summary. | Medium | CP-1, CP-1A, CP-2 | Obtain the exhibits listed in the exhibit index if legal depth is required. |
| G3 | The springing fixed charge test is described but no reported fixed charge ratio is printed, and no covenant headroom can be taken from the sources. The pack states compliance with ABL covenants. | Medium | CP-1, CP-2 | Treat headroom as Not supplied. Do not substitute management's leverage metric, which uses a different definition. |
| G4 | No credit ratings or agency actions appear in the pack. Only the management goal and risk text mention ratings. | Medium | CP-1A, CP-2 | Not supplied; obtain agency reports if rating context is needed. |
| G5 | The guarantor list exhibit is indexed but not supplied, so guarantor identities beyond the named issuer are not established from the pack. | Low | CP-1, CP-1A | Obtain exhibit 22.1. |
| G6 | The exact ABL maturity date and the applicable margin tier in use are not printed; only a five-year term and the replacement date of the earlier facility are. | Low | CP-1 | Mark as Not supplied. |
| G7 | No investor presentations or decks were supplied; the earnings releases stand in. Management narrative is therefore limited to the release text. | Low | CP-1A | None needed for readiness. |
| G8 | The 10-K refers to previously disclosed material weaknesses but does not describe them, and the pack holds no earlier filing that does. | Low | CP-1A, CP-5 | Treat as context only; do not infer a current weakness. |
| G9 | The search of all seven sources for pension, defined benefit and retiree terms found no match, so no pension or retiree medical obligation is evidenced either way. A search for the names of rating agencies found only an equity index name, so no agency rating text exists. | Low | CP-1 | Write Not supplied, not zero, for any such obligation. |
| G10 | Extraction is flattened text: one cell per line, negative amounts split across lines, and no layout or image check. Fidelity to the original tables was not reviewed. | Low | CP-1, CP-5 | Check cell order against totals in the source before relying on a figure. |
| G11 | The context period labels q2-2027 and fy-2026 do not match any period in the pack. | Medium | All | Use the filing labels; ask the requester to correct the context if a different period was meant. |

Draft, executed and as-of distinctions: all seven sources are filed or furnished documents, not drafts. The three 10-Qs are unaudited and the 10-K statements are audited. Nothing in the pack is dated after the cutoff; the latest items are dated on the cutoff day.

## Next module

CP-1 should run next on the same pinned sources, followed by CP-1A, CP-2 and CP-5 as the plan orders them. Hand CP-1 these instructions: use the 10-K FY2025 for annual and debt-by-series facts and the 10-Q Q3 for balance sheet, liquidity and the FY2026 repurchase narrative; label periods as Q3 FY2026, forty weeks 2026 and FY2025; derive discrete quarters only from the stated sixteen-week and twelve-week bases; take management's leverage ratio only as an attributed non-GAAP claim; write Not supplied for covenant headroom, ratings, guarantor list, pension and the exact ABL maturity date; and carry gaps G1 to G11 into its own gaps register.
