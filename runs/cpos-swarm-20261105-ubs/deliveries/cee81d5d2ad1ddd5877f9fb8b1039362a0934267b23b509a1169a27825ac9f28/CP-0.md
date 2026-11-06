# CP-0 source readiness: UBS Group AG (ubs)

## Request

- Issuer: UBS Group AG (issuer id `ubs`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026; prior period FY2025.
- Run: `ubs-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned source text and wrote this answer. No provider was called.
- Question: can the supplied filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion; no figure is normalized, reconciled or calculated here.

## Sources

Issuer sources, as pinned by CP-OS (the `.jsonl` text extraction of each filing). Locators are `page:N`, the extraction chunk, not the printed page. Each extraction starts with the sha256 of the original HTML, shown in the last column.

| Source | sha256 (pinned text) | Role | sha256 of original HTML (from extraction header) |
| --- | --- | --- | --- |
| 20-F_2025-12-31_ubs-20251231.htm.jsonl | c65ff0a03ee3c3df685c628425c6a0a7856867141560663149d32b58774d8f33 | Annual report on Form 20-F, fiscal year ended 31 December 2025, filed 9 March 2026; 558 chunks | 36bec97b7eb5fd59b0b7662315606cd2cbd2ceb80e0c38bb731595006f6a5672 |
| 6-K_2026-03-31_edgarq1q26kubsgroupagc.htm.jsonl | 5ae425915ce6d8540a2dcbe4beb8ed52f974546cb1a0a776687e74bfb6a0ae6d | Form 6-K dated 29 April 2026: capitalization table at 31.3.26 and 31.12.25; 3 chunks | f830084883c117fee9cfa7da84ba2c965cd806823b638168d828023dcba960cb |
| 6-K_2026-03-31_investorpresotext2026.htm.jsonl | 84e6720eb0ad0ada288bec163d56547d8305bba53a01f71c7fcd5a3acd94f71a | Form 6-K dated 30 April 2026: first quarter 2026 earnings call transcript; 24 chunks | fbd895cfd49256c10ef81f005967d701cc05eb0a48a778d6dbb352350311e9f6 |
| 6-K_2026-06-30_investorpresotext2026.htm.jsonl | 671f7dde67986089a1c17da85500334fa96b51697d1642480c22e2b5d6422aa1 | Form 6-K dated 30 July 2026: second quarter 2026 earnings call transcript; 20 chunks | 8a2918459456435305e173a644e41f4e9d8e588725e477db72198798d771b3e1 |
| 6-K_2026-07-29_edgarq2q26kubsgroup.htm.jsonl | 88627f5322eed51bd548e2eb9daaa4bff0f8cc654e252b054c4865eeda3901ea | Form 6-K dated 29 July 2026: capitalization table at 30.6.26 and 31.3.26; 1 chunk | 997e9c4369e477224a14a527b62886342fcfddd6dac093d33cae22c53ff29e9f |
| 6-K_2026-09-30_edgar3q26kubsgroupc.htm.jsonl | faea893d4d4d07cf7975acc81d8e41156e0b136d2c529429a6c83f334ac28864 | Form 6-K dated 28 October 2026: capitalization table at 30.9.26 and 30.6.26; 1 chunk | abe5d2565f7ee4265c9172d2a23a3d7583569b156ce8384fd8d84d2ec9979023 |
| 6-K_2026-09-30_investorpresotext2026.htm.jsonl | 2ac25318ab8710edaece00656540a1c90de7efab36a24b488600ed02e222986e | Form 6-K dated 29 October 2026: third quarter 2026 earnings call transcript; 23 chunks | f190338240b51b161285084a7efa96e40bfd6cb9c817701d090e2d6aad271da0 |
| context | a67d394ad1fe0320e0c68be1bf7ef2da619705355c7aa8f5e62b6171bbf4fb2d | User run settings; not issuer evidence | not applicable |

`_retrieval.json` is ignored by CP-OS and is not issuer evidence. It was used only to read the filing dates above, which agree with the dates printed inside each 6-K.

Supplied handoffs: none (CP-0 is the first module, so no upstream handoff exists).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The annual report gives a full audited base for the group, and the three latest quarters are covered only by short capitalization tables and management call transcripts. All four downstream analyses can proceed with stated limits. | Medium | The three quarterly reports themselves and the results slides are not in the pack, so current-quarter statements are not available. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual statements, debt notes, capital and liquidity sections are all present for the group. | Year-end balance sheet, funding and loss-absorbing capacity can be traced to the filing. | High |
| Current-quarter evidence is management speech plus a debt, equity and capitalization table. | Current-quarter earnings and capital figures are attributed claims, not audited or interim statement lines. | Medium |
| Debt is disclosed by category, not by individual instrument. | Instrument-level terms, maturities and holding-company versus bank issuer cannot be fully mapped from this pack. | Medium |
| Swiss capital rule changes and Credit Suisse legacy litigation are discussed only in narrative. | Their size and timing are not quantified in the supplied sources. | Medium |

### Readiness view

The supplied set is sufficient to start all four requested analyses, each with stated limitations, and none is blocked or conditional. The 20-F supplies audited consolidated statements, notes, capital, liquidity and legal-entity disclosure for the UBS Group AG consolidated group in USD under IFRS Accounting Standards. For 2026 the pack holds three one-table capitalization 6-Ks and three earnings-call transcripts, which are management statements and not the quarterly reports they refer to. Source sufficiency here does not mean downstream analysis is complete.

### Command sheet

| Consumer | Status | Command |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | RUN |
| CP-1A | READY_WITH_LIMITATIONS | RUN |
| CP-2 | READY_WITH_LIMITATIONS | RUN |
| CP-5 | READY_WITH_LIMITATIONS | RUN |

### Source register

#### 20-F for fiscal year 2025 (`20-F_2025-12-31_ubs-20251231.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited facts. page:2: "For the fiscal year ended December 31, 2025", "UBS Group AG Commission file number: 1-36764". page:3: "International Financial Reporting Standards as issued by the International Accounting Standards Board ☑".
- Structure: page:3 explains the cross-reference table: "Annual Report refers to the Annual Report 2025 of UBS Group AG annexed hereto, which forms an integral part hereof" and "Supplement refers to certain supplemental information contained in this forepart of the Form 20-F". Financial Statements are the consolidated statements of UBS Group AG.
- Statements located: income statement page:371 ("Income statement For the year ended USD m Note 31.12.25 31.12.24 31.12.23"), statement of comprehensive income page:372, balance sheet page:373 ("Balance sheet USD m Note 31.12.25 31.12.24 Assets"), statement of changes in equity page:374. The cash flow statement is at page:378 ("Statement of cash flows For the year ended USD m 31.12.25 31.12.24 31.12.23").
- Debt: page:432 "Note 15 Debt issued designated at fair value USD m 31.12.25 31.12.24" and "Note 16 Debt issued measured at amortized cost USD m 31.12.25 31.12.24"; page:433 "Subordinated debt" with "of which: eligible as high-trigger loss-absorbing additional tier 1 capital instruments". These are category tables.
- Capital, liquidity and ratings: total loss-absorbing capacity page:227 to page:234; liquidity and funding page:244 to page:247; ratings page:244 "Credit ratings Credit ratings can affect the cost and availability of funding" and page:245 "During 2025, rating agencies took the following actions regarding UBS Group AG’s ratings". Material cash requirements page:253.
- Resolution framework: page:84 "FINMA’s preferred strategy for UBS is a single point of entry (SPE) strategy involving write-down of the Group’s remaining equity and additional tier 1 (AT1) and tier 2 instruments, conversion of senior unsecured bonds of UBS Group AG to equity, if required".
- Legal entities: page:515 "Note 27 Interests in subsidiaries and other entities a) Interests in subsidiaries". Significant regulated subsidiary and sub-group data page:532 and page:535 ("UBS Switzerland AG (standalone) UBS Europe SE (consolidated) UBS Americas Holding LLC (consolidated)"; "Credit Suisse International (standalone)").
- Litigation and contingencies: page:113 ("numerous cases have been lodged against the Swiss Financial Market Supervisory Authority (FINMA) in respect of the write-down of the Credit Suisse Group’s additional tier 1 (AT1) bonds"); provisions and contingent liabilities discussed from page:434 to page:449.
- Auditor: page:14 "Independent Auditors Ernst & Young Ltd , Aeschengraben 27, 4051 Basel, Switzerland , PCAOB number 1460".
- Extraction gap on the audit reports: page:371 says "The accompanying reports of the independent registered public accounting firm ... are included in our filing on 9 March 2026 with the Securities and Exchange Commission on Form 20-F". It is followed only by running headers "Consolidated financial statements 241 Annual Report 2025 | Financial statements | Consolidated financial statements 242" through 245, with no opinion text. The audit opinion wording is therefore not located in the pinned text. Page:370 does state that management's internal control assessment was audited and "expresses an unqualified opinion", which is a description of the opinion, not the opinion itself.
- Units: USD millions in the statements (page:373 "USD m"). Printed page numbers (for example 248) are annual-report pages; the locators in this answer are extraction chunks.

#### Capitalization 6-Ks (three files)

- Family and authority: filed 6-K extracts furnished for registration-statement incorporation. Q1 file page:2: "Capitalization of UBS Group AG The table below presents the consolidated capitalization of UBS Group AG in accordance with IFRS Accounting Standards in US dollars, the presentation currency of UBS Group AG."
- Q1 file (page:2) has the only short-term versus long-term split: "Short-term debt issued 1 97,642 92,096 Long-term debt issued 2 246,279 236,405", and the high-trigger AT1 subline.
- Q2 file (page:1) and Q3 file (page:1) show a single line: "Debt issued 1 343,551 343,922" and "Debt issued 1,2 324,981 343,551". The short-term and long-term split is not repeated, and the footnote definitions differ between files. The Q3 file's footnote reads "As of 30 September 2026, 87% of Debt issued was unsecured."
- Perimeter: consolidated UBS Group AG, USD. The Q1 footnote defines debt as issued "by UBS Group AG and its subsidiaries", so it is not holding-company-only debt.
- Naming: the file-name date (for example 2026-03-31) is the report period, not the filing date; the printed cover dates are 29 April, 29 July and 28 October 2026.
- Authority: these tables are filed issuer disclosure, but they are only a capitalization extract. They carry no income statement, cash flow, capital ratio or liquidity data.

#### Earnings-call transcripts (three files)

- Family and authority: management speeches and analyst Q&A furnished on 6-K, attributed supporting claims and not financial statements. Q3 file page:2: "This Form 6-K consists of the transcripts of the of UBS Group 3Q26 Earnings call remarks and Analyst Q&A". Co-registrants: "UBS Group AG ... Commission File Number: 1-36764" and "UBS AG ... Commission File Number: 1-15060". The transcript perimeter is therefore the group, with some UBS AG standalone remarks.
- Slides are not supplied. page:2 of each file: "Numbers for slides refer to the third quarter 2026 results presentation" (and the first and second quarter equivalents). Slide-level tables, charts and footnotes cannot be inspected; only spoken text is present.
- Content located in the Q3 file: group results and capital ratios page:4 to page:5 ("Our CET1 capital ratio at the end of September was 14.7%"; "total loss-absorbing capacity of 187 billion, a net stable funding ratio of 115% and an LCR of 179%"); division results page:6 to page:9; Swiss capital-rule discussion page:3 to page:4 ("September’s outcome in the Upper House is very concerning") and Q&A page:10 to page:14; Credit Suisse AT1 litigation timing page:14 ("decision not before Q1 of 2027"); UBS AG standalone capital page:5 to page:6.
- Q1 and Q2 files cover the same structure for their quarters (page:2 onward); Q2 page:5 carries "a net stable funding ratio of 115% and an LCR of 177%" and "Our CET1 capital ratio at the end of June was 14.4%".
- Currency: the speakers mix USD and CHF (for example Personal & Corporate Banking is stated in Swiss francs, Q3 file page:7). Any figure used must carry its stated currency.

### Information-availability boundary

- Every supplied source is dated on or before 29 October 2026, before the as-of date and cutoff of 2026-11-05. Nothing in the pack is dated after the cutoff.
- Nothing dated between 29 October 2026 and 5 November 2026 is supplied. Events in that window are Not supplied, not absent.
- The Q3 transcript mentions future events (a fourth-quarter results update and a strategic update, a 2027 capital-return plan, Swiss parliamentary deliberations). These are management statements about the future, not facts as of the cutoff.

### Identity and perimeter

- Reporting entity: UBS Group AG, Switzerland, consolidated, IFRS Accounting Standards, presentation currency USD (6-K Q1 page:2 above; 20-F page:3).
- Related entities named in the sources: UBS AG (co-registrant on the transcripts, page:2; standalone CET1 discussed Q3 page:5 to page:6), UBS Switzerland AG, UBS Europe SE, UBS Americas Holding LLC, Credit Suisse International (20-F page:532, page:535), and Credit Suisse Group AG and Credit Suisse AG as former entities (20-F page:38 definitions). The sources describe UBS Group AG as the holding company in the resolution strategy (page:84). Which entity issued which instrument, and who guarantees what, is Unresolved from category-level debt tables; the guarantor field in the context is blank, which is not evidence of none.
- Segment and consolidation differences: 20-F page:532 shows significant regulated subsidiaries and sub-groups on their own bases ("Swiss SRB rules", "EU regulatory rules", "US Basel III rules"), which differ from the group IFRS statements. Do not mix these perimeters.
- Bank sector note: this is a deposit-taking bank holding group (customer deposits are the main liability on page:373). The method's industrial-style debt, leverage and covenant analysis does not map directly; the relevant measures are regulatory capital, total loss-absorbing capacity and liquidity ratios, which the sources do contain. This is a note on source fit, not a conclusion.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt, liquidity, capital, non-GAAP measures | 20-F page:371 to page:374 and page:378 (statements), page:432 to page:433 (debt), page:227 to page:247 (capital and liquidity); capitalization tables for the three 2026 quarter-ends; transcripts for 2026 quarterly commentary | No quarterly report or interim statements; no results slides; "underlying" and adjusted measures in the transcripts have no reconciliation in the pack |
| CP-1A | Business, divisions, history, integration, ownership, transactions | 20-F cross-reference page:3 to page:5 and business sections cited there; transcripts for divisional commentary and integration status | Credit Suisse integration and regulatory narrative is management-attributed; no shareholder register or transaction documents |
| CP-2 | Capital structure, debt by instrument, maturities, ranking, covenants, liquidity | 20-F debt notes page:432 to page:433; maturity analysis cited at page:253; capitalization tables | Instrument-level terms, indentures, maturities by issue and guarantor structure not supplied; no covenant concept appears in the sources at the level of an industrial credit agreement |
| CP-5 | Traceable claims | Every source has stable chunk numbers | Text extraction only; slides, charts and audit reports are not evidenced |

### Analytical read-through

- Usable coverage: the 20-F gives audited FY2025 statements with FY2024 comparatives (and FY2023 for the income statement and cash flows), with notes, and sections on capital, loss-absorbing capacity, liquidity and funding, ratings actions, resolution strategy, subsidiaries and litigation. It is enough to build a reported financial foundation for FY2025 on the group perimeter.
- Strongest contrary evidence: the evidence for Q3 2026 is thin. The quarterly reports referred to on the 6-K covers ("UBS Group AG’s third quarter 2026 report, submitted to the SEC on Form 6-K on October 28, 2026", Q3 capitalization file page:1) are named but not supplied. The only Q3 balance-sheet line in a filed table is the capitalization extract. Every Q3 earnings, capital and liquidity figure therefore rests on transcript speech. A management claim cannot override the 20-F, and it has no filed statement to reconcile against in this pack.
- Source risk mechanism: the capitalization tables change presentation between the Q1 file (short-term and long-term split) and the Q2 and Q3 files (single debt line), so a consumer that wants maturity profile at Q3 cannot take it from the supplied tables; the consequence is that the 2026 maturity split stops at 31.3.26 and must be labelled as stale for later quarters. Debt notes in the 20-F are by category (senior unsecured, covered bonds, subordinated, Swiss central mortgage institutions), so a consumer that needs instrument-level ranking or issuer must mark it Not supplied.
- What cannot proceed: instrument-level capital structure and covenant analysis; interim statement tables for 2026; slide-based charts; audit opinion wording; quantified effect of pending Swiss capital rules (the transcripts discuss alternatives without a supplied rule text).
- Next evidence action: supply the first, second and third quarter 2026 reports (the documents the capitalization 6-Ks point to), the results presentations, the 20-F audit reports, and any prospectus supplements or Pillar 3 report that list individual debt and capital instruments.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Figures quoted above are shown only as exact substrings of the sources, to locate them.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| First, second and third quarter 2026 reports (income statement, balance sheet, cash flow, notes) are not supplied; only capitalization extracts and call transcripts | High | CP-1, CP-2, CP-5 | Supply the three quarterly reports referenced on the capitalization 6-K covers |
| Results presentations (slides) are not supplied; the transcripts refer to slide numbers | Medium | CP-1, CP-1A, CP-5 | Supply the slide decks for the three quarters |
| Audit opinion text on the consolidated statements and on internal control is not in the pinned 20-F text (page:371 gives only a cross-reference and empty running headers) | Medium | CP-1, CP-5 | Supply the auditor reports pages or the full filed document |
| Debt is disclosed by category only; no instrument-level listing, issuer or guarantor mapping, or maturity ladder by issue was located | High | CP-2 | Supply instrument lists, indentures or a prospectus supplement; keep Not supplied otherwise |
| 2026 debt maturity split stops at 31.3.26; later capitalization files show a single debt line | Medium | CP-1, CP-2 | Use the quarterly reports when supplied |
| Transcript "underlying" and adjusted measures have no reconciliation to reported figures in the pack | Medium | CP-1 | Supply the quarterly reports with their reconciliations |
| Swiss capital-rule proposals and Credit Suisse AT1 litigation are narrative only; rule text, court filings and provision amounts for 2026 are not supplied | Medium | CP-1A, CP-2 | Supply the proposals, and the quarterly litigation note when available |
| Events from 29 October 2026 to 5 November 2026 are not supplied | Low | CP-1A, CP-2 | Supply later 6-Ks or confirm none |
| Credit rating levels as of the as-of date are not supplied; the 20-F reports 2025 actions and the context has no ratings | Medium | CP-2 | Supply current agency reports |
| The Q2 capitalization 6-K and three transcript 6-Ks appear in `_retrieval.json` with URL paths under a different numeric CIK than the issuer; the document text names UBS Group AG as registrant, so identity is unaffected, but the path difference is not explained in the sources | Low | CP-5 | Note only |

## Next module

- CP-1: use the 20-F statements (page:371 to page:374) as controlling for FY2025. Treat the transcripts as attributed management claims. Keep the group perimeter separate from UBS AG and the significant subsidiaries. Label every Q3 2026 figure by its source type and currency. Do not draw a short-term and long-term debt split after 31.3.26 from the supplied tables.
- CP-1A: carry the Credit Suisse integration, Swiss capital-rule debate and AT1 litigation as management-attributed or 20-F narrative; mark anything after 29 October 2026 Not supplied.
- CP-2 and CP-5: carry the missing instrument-level debt terms, the missing quarterly reports and slides, and the audit-report extraction gap as restrictions. Treat the category debt tables as the limit of the capital-structure evidence.
