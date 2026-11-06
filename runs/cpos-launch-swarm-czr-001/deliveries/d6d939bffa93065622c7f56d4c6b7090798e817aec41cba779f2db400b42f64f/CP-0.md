## Request

Source-readiness review (CP-0) for Caesars Entertainment, Inc. (ticker CZR, issuer id czr), as of 2026-11-05, pathway credit_snapshot, public case, reporting currency USD, current period Q3 2026, prior period FY2025. Cutoff 2026-11-05: no source dated after the cutoff is used. The selected downstream consumers are CP-1, CP-1A, CP-2 and CP-5 (the `minimum` module set). This review answers only whether the supplied source set can support that work and what remains blocked. It gives no credit conclusion, no legal interpretation and no investment opinion, and it does not calculate or normalize any figure.

The run context (`context`, sha256 0172f1f774353a9014a5593b1df2824463fdefe668659f701d2701a1f5a162de) holds dated settings only and is not issuer evidence. It leaves borrower, parent, guarantors, ratings, quotes, deal terms and market data blank; those blanks are Not supplied, not zero.

## Sources

### Issuer sources relied on

All seven sources were indexed page by page and located. Names are the converted-text files CP-OS pinned; the sha256 is that of the pinned converted file. Each file's own first line also carries the sha256 of the original HTML, listed in the last column.

| Source (exact name) | sha256 (pinned file) | Pages read in this review | Original HTML sha256 per first line of file |
|---|---|---|---|
| 10-K_2025-12-31_czr-20251231.htm.jsonl | bc64a6b58a2e5481a0cfade7eea5b0ab2abc3801003c4d6cb677785a5aa59468 | page index of pages 1-166; page 79 and page 80 (liquidity); exhibit index pages 158-165 | b6abdbfe75f9d7f250f7a884a48a9f4670cf6d9885cb62e16f280c73f645a60b |
| 10-Q_2026-03-31_czr-20260331.htm.jsonl | 5678521031e1645ef46bac311c4cabf43977488c6d11dfa25cc00a4f23b2d8a8 | page index of pages 1-51; page 3 (statements) | ed76cb7dc1366c7f2dfe2a338d009d3c4955bc1fee5fb92531eba82c83e405e9 |
| 10-Q_2026-06-30_czr-20260630.htm.jsonl | c1584ea1247740f06c0dd4b0a8964b1753f8cc5c74266698804a67fd5a8dafb5 | page index of pages 1-66; page 11 | f07359b284afb3640dd3d93070f249f9c04a4d980dd6ec551dd1b874a356943d |
| 10-Q_2026-09-30_czr-20260930.htm.jsonl | 020dbbd4c466f93db126b9e9ea0f09672470d3e5caa33fd667f739807400c48f | page index of pages 1-66; pages 5, 7-10, 15-21, 38, 51, 53, 54, 64, 66 | 0f41b4699ee5346de5f9e09d5e9d143ea3ef69b3f6184d0611d053f7acb8f1dc |
| EX-99.1_2026-04-28_ex991-2026q1ceiearningsrel.htm.jsonl | 7471385a5ad76519a93a6fc4a1f0048a88c7bfb7676d6a0b6e78c8e1a9e19c13 | pages 1-2 | 674b7e2ad96557a28bbcfdc426d129ff2ca18615c8de850ffea450f6de69f601 |
| EX-99.1_2026-07-28_ex991-2026q2ceiearningsrel.htm.jsonl | 89cd5ad8c7a0d45cdf4a8f6462fc3964a9e7d04aae46811b1f50bebeb80c1762 | pages 1-2 | c0a99f35ce0f9f6eda03e849737c7ebc1284abd95ef6e99ec9589f34f4ea351e |
| EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | 72e92043d95db7701dbaee10509a03094dd97f5a7811f25a956ad12661393bcd | pages 1-6 in full | cd0adbbb26dc7f4b00ccbcede490aa4dc79e2e708f043bb9e778f9756afa55c2 |

The file `_retrieval.json` was ignored by CP-OS and is not evidence.

### Run context (not issuer evidence)

| Source | sha256 |
|---|---|
| context (czr.json) | 0172f1f774353a9014a5593b1df2824463fdefe668659f701d2701a1f5a162de |

### Handoffs supplied

None. CP-0 is the first module in the run and CP-OS supplied no upstream handoff. No handoff module or sha256 is relied on.

## Findings

### Source readiness verdict

The supplied set is a filed-document set: one annual report (10-K, FY2025), three quarterly reports (10-Q for Q1, Q2 and Q3 2026) and three earnings-release exhibits (Exhibit 99.1 for Q1, Q2 and Q3 2026). It is sufficient, with bounded limitations, for the four selected consumers CP-1, CP-1A, CP-2 and CP-5. It is not sufficient for work that needs executed financing, lease or merger terms, because no credit agreement, indenture, lease or merger agreement text was supplied. Source sufficiency only (SOURCE_SUFFICIENCY_ONLY); the model input contract is not evaluated (CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

### Per-source assessment

| Source | Document family and authority | Entity and perimeter | Period and basis | Version relationship |
|---|---|---|---|---|
| 10-K FY2025 | Filed annual report with audited statements (page 96 opens "REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM"); highest authority for FY2025 facts | Consolidated Caesars Entertainment, Inc. and subsidiaries; segments Las Vegas, Regional, Caesars Digital, Managed and Branded, plus Corporate and Other | Fiscal year ended December 31, 2025 with 2024 and 2023 comparatives; USD millions | Only full-year source; interim facts are superseded by later 10-Qs |
| 10-Q Q1 2026 | Filed quarterly report, unaudited | Same consolidated perimeter | Three months ended March 31, 2026 versus 2025; balance sheet versus December 31, 2025 | Separate active source; not replaced by later quarters |
| 10-Q Q2 2026 | Filed quarterly report, unaudited; first filing to describe the merger | Same perimeter; adds the Caesars Windsor and Grand Bazaar asset purchases | Three and six months ended June 30, 2026 | Separate active source |
| 10-Q Q3 2026 | Filed quarterly report, unaudited; latest filed statements, signed "Date: October 27, 2026" | Same perimeter; comparability affected by the asset purchases | Three and nine months ended September 30, 2026; balance sheet at September 30, 2026 versus December 31, 2025 | Latest period; controls Q3 2026 and nine-month facts |
| EX-99.1 Q1, Q2, Q3 2026 | Earnings releases furnished as exhibits; issuer-attributed supporting claims, not audited; carry non-GAAP reconciliations and a net debt table | Same consolidated perimeter | Quarter and year-to-date, labelled "Three Months Ended" and "Nine Months Ended" or "Six Months Ended" | Each release is a separate active source; the filed 10-Q controls where both state a fact |

### Strongest usable coverage

The Q3 10-Q debt note gives facility-level detail in one table with final maturity, rate type, face value and book value for each instrument (for example "CEI Term Loan B 2030 variable 2,012 1,988 2,002"), a maturity ladder ("Annual maturities of long-term debt"), and covenant descriptions by credit group. The Q3 release gives the Adjusted EBITDA reconciliation to net loss attributable to Caesars, segment results, a liquidity table and net debt ("Net debt (a) $ 10,795 $ 11,018"). The Q3 10-Q cash flow page gives cash interest paid for debt, cash interest paid for rent related to GLPI and VICI leases, and income taxes paid. That evidence supports CP-1 (document and financial read), CP-1A (financials and credit metrics inputs), CP-2 (debt structure, maturities and liquidity) and CP-5 (transaction read-through) at the located level.

### Strongest contrary evidence and limitations

1. Pending change of ownership. The Q3 10-Q reports a merger agreement dated May 27, 2026 with Fertitta Gaming Holdco, LLC, stockholder approval on September 22, 2026, a termination fee of $200 million, a reverse termination fee of $450 million and end dates from May 27, 2027 to November 27, 2027. The Q3 release says "No Conference Call Due to the Company's pending definitive agreement to be acquired by Fertitta Entertainment, Inc." The 10-Q names Fertitta Gaming Holdco, LLC as party and the release names Fertitta Entertainment, Inc.; their relationship is not explained in the text read and stays an unresolved entity distinction. The merger agreement is described, not supplied: the 10-Q exhibit index says "Previously filed on Form 8-K filed on May 28, 2026", with schedules omitted. Consequence: CP-5 can describe the transaction as the filings disclose it, but cannot test conditions, financing sources or treatment of existing debt.
2. No executed financing documents. The 10-K exhibit index (pages 158-165) lists the credit agreement and indentures by reference only. The covenant evidence is the filed summary ("a maximum net total leverage ratio financial covenant of 6.50:1" and "a minimum fixed charge coverage ratio financial covenant of 2.0:1" for the CEI Revolving Credit Facility and CEI Term Loan A; "4:1" and "1.05:1" for the Caesars Virginia facilities) and "the Company was in compliance with all of the applicable financial covenants described above". Baskets, definitions, test mechanics, change-of-control provisions and call schedules are not located. Consequence: CP-2 can state disclosed covenant levels and the compliance statement but cannot compute headroom on contractual definitions.
3. No lease documents. The VICI and GLPI leases weigh heavily in cash obligations ("Cash interest paid for rent related to GLPI and VICI Leases 1,030" in the nine months) but only filed summaries are available. The 10-K lease note (pages 115-119) was located but not read in this module. Consequence: lease-related metrics in CP-1A and CP-2 depend on that note's definitions.
4. Release versus filing. Releases are management-attributed; the filing controls where both state a fact. At Q1 2026 the release headline says "GAAP net loss of $98 million" while its table and the 10-Q label that figure "Net loss attributable to Caesars"; the 10-Q comprehensive income statement shows a total "Net loss $ (83)". Downstream modules must keep attributable and total labels exactly as filed.
5. Comparability. The Q3 10-Q states that from March 3, 2026 the property's operations "are reported within the Regional segment" (Caesars Windsor, previously Managed and Branded) and that Grand Bazaar was acquired on May 1, 2026; the Q2 10-Q says periods after the asset purchases are "not fully comparable". Whether prior-period segment figures were restated was not determined.
6. Not supplied: a discrete Q4 2025 quarter, forward guidance (no guidance or outlook section was found in the three releases), ratings, market quotes, peers and valuation inputs. A Q4 2025 figure would be a downstream derivation from the 10-K and interim sources, not a source.
7. Text extraction only. All seven files are text conversions; charts and images are not inspected, and extraction success is not a fidelity review. Every file was indexed by page; not every page was read line by line in this module.

### Consumer assessment

| Consumer | Status | Basis | Carried limitations |
|---|---|---|---|
| CP-1 | READY_WITH_LIMITATIONS | Filed statements, notes, segment tables and MD&A for FY2025 and three 2026 quarters are present and located | Limitations 1, 2, 3, 7 |
| CP-1A | READY_WITH_LIMITATIONS | Segment, reconciliation, cash interest and tax paid disclosures present; Adjusted EBITDA reconciliations in all three releases | Limitations 3, 4, 5, 6 |
| CP-2 | READY_WITH_LIMITATIONS | Facility-level debt table with face and book values, maturity ladder, covenants and liquidity table at September 30, 2026 and December 31, 2025 | Limitations 1, 2, 3; no executed debt documents; change-of-control treatment not located |
| CP-5 | READY_WITH_LIMITATIONS | Merger terms described in the Q2 and Q3 10-Qs and the Q3 release | Limitation 1; merger agreement and financing commitments not supplied; two acquirer names unresolved |

No selected consumer is CONDITIONAL or BLOCKED on source grounds. None of these statuses asserts that downstream analysis is complete or that any model input contract is accepted.

## Calculations

Not calculable in CP-0: this module does not normalize, reconcile or calculate figures, so no new calculation was performed. Figures quoted above are copied from the cited sources only.

Coverage counts: 7 of 7 issuer sources located and indexed by page; handoffs supplied: 0 of 0.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Citation |
|---|---|---|---|---|
| Merger Agreement not supplied; only described (Exhibit 2.1 "Previously filed on Form 8-K filed on May 28, 2026") | Medium | CP-5, CP-2 | Supply the 8-K and Exhibit 2.1 if terms beyond the 10-Q description are needed | 10-Q Q3 2026 page 66 |
| Acquirer named Fertitta Gaming Holdco, LLC in the 10-Q and Fertitta Entertainment, Inc. in the release; relationship not explained | Low | CP-5 | Resolve from the merger agreement or proxy statement | 10-Q Q3 2026 page 38; EX-99.1 Q3 page 4 |
| Credit agreement, indentures and Caesars Virginia credit agreement not supplied | Medium | CP-2 | Supply executed documents for covenant definitions, baskets and change-of-control terms | 10-K pages 158-165 |
| Change-of-control or merger-driven debt treatment not located (the only 10-Q mention concerns third-party contracts) | Medium | CP-2, CP-5 | Not supplied; obtain merger agreement, proxy statement or indentures | 10-Q Q3 2026 page 64 |
| VICI and GLPI lease documents not supplied | Medium | CP-1A, CP-2 | Supply leases or rely on the 10-K lease note | 10-K pages 115-119 |
| Q4 2025 discrete quarter and forward guidance not supplied | Low | CP-1A | Derive downstream if needed; no guidance source | Releases pages 1-2 |
| Ratings, quotes, peers, deal terms, borrower, parent and guarantor fields blank in context | Medium | CP-2, CP-5 | Not supplied; do not treat as zero | context |
| Text-only extraction; images and charts not inspected; fidelity not reviewed | Low | All | Record as a parse limitation | All sources |
| Prior-period segment restatement for Caesars Windsor reclassification not determined | Low | CP-1A | Check segment note in the 10-Q before comparing segments | 10-Q Q3 2026 page 38 |

## Next module

Proceed to CP-1. Carry forward: the pending merger, absence of executed debt and lease documents, release-versus-filing label care, and the Caesars Windsor and Grand Bazaar comparability notes. The next evidence action for the open gaps is to supply the 8-K with Exhibit 2.1 and the credit agreement and indentures if covenant headroom or merger-driven debt treatment is to be analyzed.
