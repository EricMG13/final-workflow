## Request

Source readiness (CP-0) for BELDEN INC. (issuer id bdc, NYSE: BDC), as of 2026-11-05, pathway credit_snapshot, reporting currency USD, current period Q3 2026 (quarter ended September 27, 2026), prior period FY2025. Cutoff 2026-11-05. The question: can the pinned source set support the downstream modules CP-1, CP-1A, CP-2 and CP-5, and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion, and it calculates nothing. No upstream handoff exists for this module.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Family and authority |
| --- | --- | --- |
| 10-K_2025-12-31_bdc-20251231.htm.jsonl | 80ef274084e1c7703f38055c49f44de69b5a31dd5b2e660bad032bc466600517 | Annual report, FY2025, audited, filed SEC document (115 pages) |
| 10-Q_2026-03-29_bdc-20260329.htm.jsonl | 92ae5feb886f18c8068e6e144870a7ce7fe24ecefea2657b8f22ad10746ee6ac | Quarterly report, Q1 2026, unaudited, filed SEC document (27 pages) |
| 10-Q_2026-06-28_bdc-20260628.htm.jsonl | 60c04fb4ddf3b8e563e4be095f10f190f61691e26efdac7b09cb5561f0a211ee | Quarterly report, Q2 2026, unaudited, filed SEC document (31 pages) |
| 10-Q_2026-09-27_bdc-20260927.htm.jsonl | 7239af9a6f61de7f4eea5ba8a5ab17342b8c139514426ea01b365d68fd81dcfe | Quarterly report, Q3 2026, unaudited, signed October 29, 2026 (38 pages) |
| EX-99.1_2026-04-30_companynewsreleasedatedmar.htm.jsonl | 800b10b5a6acbba2ef9d00a1b953296d6d2a04b007b53040c5086b01b69c7caa | Earnings release, Q1 2026, dated April 30, 2026, management-attributed (8 pages) |
| EX-99.1_2026-07-30_companynewsreleasedatedjul.htm.jsonl | 97518bcedf20ecd151c6170017340147f2d2133733fbcb29ebcfd34f2604e982 | Earnings release, Q2 2026, dated July 30, 2026, management-attributed (9 pages) |
| EX-99.1_2026-10-29_companynewsreleasedatedoct.htm.jsonl | bd6ff1210615fc5d7c13577de667703f5a66b803e28876ed410b2fa777310433 | Earnings release, Q3 2026, dated October 29, 2026, management-attributed (9 pages) |

### Run settings (not issuer evidence)

| Source | sha256 | Use |
| --- | --- | --- |
| context (913142-belden-inc-bdc.json) | c6d9bea849396ac29c99bcba0cfe7683fa092d214ad8aab3fe1d1ba06b34ee33 | User settings: as-of and cutoff 2026-11-05, USD, current period q3-2026, prior period fy-2025. Ratings, quotes, deal terms, peers, legal documents and sponsor are blank; blank is not zero. |

### Supplied handoffs

None. CP-0 is the first module; no upstream handoff exists. The retrieval index `_retrieval.json` was ignored by CP-OS and is not a source.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents are enough for the planned financial, business and review modules, with limits. They cover the latest quarter and the new term loan, but not the term loan agreement itself. | Medium | No credit agreement or indenture is supplied, so covenant terms rest on short filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The July 2026 acquisition of Ruckus and its term loan changed the company in the latest quarter, and the annual report predates both. | Debt, interest, goodwill and earnings must be read from the latest quarterly filing, not the annual report. | High |
| The company moved from two reportable segments to one in 2026. | Segment history from the annual report cannot be matched to 2026 periods. | High |
| Covenant and liquidity detail is only partly supplied: a revolver springing fixed charge test is described, but the term loan terms are limited to pricing, amortisation and maturity. | Covenant headroom on the new term loan cannot be assessed from these sources. | Medium |

### Readiness view

The source set is READY_WITH_LIMITATIONS for CP-1, CP-1A and CP-2, and READY_WITH_LIMITATIONS for the CP-5 trace review. Every source is a text extraction of a filed SEC document or an issuer press release, with located content on every page listed in `## Sources`. The binding limitations are: (1) no executed credit agreement, indenture or Term Loan B document is supplied, so legal terms rest on the notes to the financial statements; (2) the FY2025 annual report is stale for the capital structure and business perimeter after the July 1, 2026 Ruckus acquisition; (3) the segment structure changed from two to one reportable segment from January 1, 2026; (4) Ruckus is consolidated only from July 1, 2026, with a preliminary purchase price allocation. None of these blocks the planned modules. This assertion concerns source sufficiency only; downstream analytical completion is not evaluated here.

### Source-by-source assessment

| Source | Content located (page locators are source chunks, not printed pages) | Perimeter and period | Notes |
| --- | --- | --- | --- |
| 10-K FY2025 | Cover page:1; business and segments pages 3-6; risk factors pages 16-31; MD&A pages 37-47 (liquidity page:45-47, contractual obligations page:47); audit opinion pages 57-59; statements pages 60-62; Note 5 segments pages 82-84; leases page:88; Note 15 debt pages 92-94; Note 18 pensions pages 98-102; Note 23 contingencies and letters of credit page:107; Note 25 subsequent events page:107 | Belden Inc. consolidated, FY2025 (year ended December 31, 2025), USD thousands | Two reportable segments (Smart Infrastructure Solutions, Automation Solutions) at page:4 and page:82. Debt table at page:92 shows three euro senior subordinated notes and an undrawn revolver. |
| 10-Q Q1 2026 | Statements pages 2-4; segment realignment page:5; debt page:13-14; subsequent events including the Ruckus agreement page:16; MD&A pages 17-24 | Belden Inc. consolidated, three months to March 29, 2026 | Ruckus is only a signed agreement here (April 29, 2026). The 2033 Notes issuance and the 2027 Notes repurchase appear in debt pages 13-14. |
| 10-Q Q2 2026 | Statements pages 2-4; debt pages 14-16; subsequent events page:18; MD&A pages 19-29; adjusted EBITDA reconciliation page:26-27 | Belden Inc. consolidated, three and six months to June 28, 2026 | Ruckus closed July 1, 2026 and is described as a subsequent event (Note 14, page:18); the Term Loan is disclosed in outline only. |
| 10-Q Q3 2026 | Statements pages 2-5; Note 3 Ruckus purchase accounting pages 11-13 including pro forma at page:13; leases pages 16-17; Note 9 debt pages 17-20; MD&A pages 23-34; adjusted EBITDA reconciliation page:32; legal proceedings and risk factors page:36 | Belden Inc. consolidated, three and nine months to September 27, 2026, USD thousands; Ruckus included from July 1, 2026 | Primary source for the latest balance sheet (page:2), cash flow (page:3), debt (page:17) and liquidity (pages 32-34). Purchase price allocation is stated to be preliminary (page:12). |
| EX-99.1 April 30, 2026 | Highlights page:1, guidance page:2, balance sheet page:3, non-GAAP reconciliation pages 4-5 | Q1 2026 | Management attribution; supports but does not override the filings. Q2 guidance is stated excluding Ruckus. |
| EX-99.1 July 30, 2026 | Highlights page:1, balance sheet page:3, cash flow page:4, reconciliation pages 4-6 | Q2 2026 | Management attribution. |
| EX-99.1 October 29, 2026 | Highlights pages 1-2, statements pages 2-3, cash flow page:4, reconciliation page:6 | Q3 2026 | Management attribution; states Q4 2026 guidance, which is forward-looking management language, not fact. |

### Entity and instrument roles located

The reporting entity is Belden Inc., a Delaware corporation (10-Q Q3 page:1). All euro notes were issued by Belden Inc. (10-K page:94, Note 16). Security for the Revolver is not stated in the located text. The 2028, 2031 and 2033 senior subordinated notes are guaranteed on a senior subordinated basis by current and future domestic subsidiaries and rank below the senior debt, including the Revolver (10-Q Q3 page:18 and page:20). The Revolver has a borrowing base of receivables, inventory and property, plant and equipment of subsidiaries in several jurisdictions (10-Q Q3 page:18). The guarantors and security of Term Loan B are not described in the located text; this is an unresolved distinction carried as a gap. No separate parent, sponsor or restricted/unrestricted group exists in the context (parent, borrower and guarantor fields are blank), and none is named in the filings located.

### Coverage by downstream consumer

| Consumer | Evidence demanded | Located | Verdict |
| --- | --- | --- | --- |
| CP-1 financial extraction | Statements, debt and liquidity by facility, EBITDA reconciliation, cash flow, leases, contingencies | Balance sheet, income statement and cash flow for Q3 2026 and FY2025 (10-Q Q3 pages 2-3; 10-K pages 60-62); debt table page:17; revolver availability page:18; adjusted EBITDA page:32; lease table pages 16-17 | READY_WITH_LIMITATIONS |
| CP-1A business and transaction | Business model, ownership, transaction history | Business description (10-K pages 3-10); Ruckus purchase accounting (10-Q Q3 pages 11-13); releases for management narrative | READY_WITH_LIMITATIONS |
| CP-2 credit synthesis | CP-1 figures and CP-1A registers only | Depends on the two modules above; no direct source demand | READY_WITH_LIMITATIONS (inherits their limits) |
| CP-5 evidence trace | Quote and figure checks of every claim against the pack | All seven sources retained with located text | READY_WITH_LIMITATIONS |

### Conflicts and version relationships

The three 10-Q filings, the 10-K and the three releases are separate periods and separate documents; none supersedes another, and all stay active. The releases are management documents and are subordinate to the filings where they differ.

Observed inconsistencies between sources, both to be handled downstream:

- The 2027 Notes repurchase consideration is stated as €450.0 million ($535.9 million) in 10-Q Q1 page:13 and 10-Q Q3 page:18, but as €450.0 million ($537.3 million) in 10-K page:107 (Note 25). The 10-Q Q3 page:20 states $537.3 million as the issuance amount of the 2033 Notes. The conflict is in the USD translation only; the filings control and the 10-Q figures post-date the 10-K.
- The Ruckus consideration is described as approximately $1.846 billion in 10-Q Q1 page:16, approximately $1.9 billion in 10-Q Q2 page:18, and $1,869.6 million net of cash acquired in 10-Q Q3 page:11. These are a signed price, a rounded figure and a closing amount net of cash; the Q3 filing controls for the closing amount.
- The 10-K contractual obligations text (page:47) and debt table (page:92) show the capital structure at December 31, 2025, before the January 2026 notes, the 2027 Notes repurchase and the July 2026 Term Loan B; they are stale for the current capital structure.

## Calculations

None. CP-0 does not normalize, reconcile or compute figures. Page counts above are the number of retained chunks per source as supplied.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Term Loan B credit agreement not supplied. Located text gives size, pricing (term SOFR plus 2.25% or base rate plus 1.25%), 0.25% quarterly amortisation and July 1, 2033 maturity (10-Q Q3 page:20), but no covenants, guarantors, security, call protection or mandatory prepayment terms. | High | CP-1, CP-1A, CP-2 | Obtain the executed credit agreement and any amendment from the issuer's filings; until then, record legal terms as Not supplied. |
| Revolver credit agreement and notes indentures not supplied; the only covenant described is a springing fixed charge coverage ratio, triggered if borrowing exceeds 90% of the combined borrowing base or availability falls below $27.0 million (10-Q Q3 page:18). The test level is not stated. | Medium | CP-1, CP-2 | Obtain the revolver agreement and indentures. |
| Letters of credit drawn against the Revolver are not separately stated; the filings give standby letters of credit, surety bonds and bank guaranties as a total (10-Q Q3 page:7) and an available borrowing capacity (10-Q Q3 page:18). | Low | CP-1 | Use the stated available capacity; do not derive a facility-level split. |
| Segment history: two reportable segments in FY2025 (10-K page:82); one reportable segment from January 1, 2026 (10-Q Q3 page:6). No recast 2025 data by the new structure is located. | Medium | CP-1, CP-1A | Treat FY2025 segment data as a prior structure; use consolidated figures across periods. |
| Ruckus purchase price allocation is preliminary and in-process R&D has no fair value yet (10-Q Q3 page:12); Ruckus contributes from July 1, 2026 only, so no standalone Ruckus history or LTM pro forma EBITDA is supplied. A pro forma revenue, net income and EPS table exists (10-Q Q3 page:13) but no pro forma EBITDA. | High | CP-1, CP-2 | Treat Ruckus-related intangibles, goodwill and deferred taxes as provisional; LTM EBITDA on a combined basis is Not calculable from these sources. |
| No discrete fourth quarter FY2025 or LTM figures are printed. FY2025 is annual only. | Low | CP-1 | Derive downstream from annual and nine-month figures, labelled by period. |
| Ratings, market quotes, peer set, valuation inputs, sponsor and legal documents are blank in the context. | Medium | CP-2 | Not supplied; keep as explicit gaps. No external source is used. |
| Extraction fidelity not reviewed: each source is a text extraction; table layout and any images or charts were not inspected. Source quality and extraction status are distinct. | Low | all | Spot-check figures against the located text before use. |
| Management claims in the releases (for example record results, data center agreement, Q4 2026 guidance) are attributed management language, not filed fact. | Low | CP-1A, CP-2 | Tag as Management Language. |

Currency and units: USD throughout; filings report in thousands, the releases and MD&A text in millions. Euro-denominated notes are translated to USD in the filings. No period or currency mismatch with the context was found: Q3 2026 is the quarter ended September 27, 2026, and the prior period is FY2025 ended December 31, 2025.

## Next module

CP-1 may run first on the full source set. Priorities for it: the Q3 2026 balance sheet, debt table, revolver availability and liquidity from the latest 10-Q; the FY2025 10-K for the prior-period comparison; and period labels kept separate (Q3 2026, nine months 2026, FY2025). CP-1A should use the 10-K business description for the pre-acquisition company and the Q3 10-Q Note 3 for Ruckus. CP-2 and CP-5 follow in order. Each must carry the gaps above, in particular the missing Term Loan B agreement and the preliminary purchase accounting.
