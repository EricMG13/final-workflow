# CP-0 — Source readiness: Caesars Entertainment, Inc. (czr)

## Request

- Issuer: Caesars Entertainment, Inc. (issuer id `czr`), as of 2026-10-02, information cutoff 2026-10-02 (context).
- Run: `czr-2026-10-02-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion; no figures normalized, reconciled or calculated.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| CZR_FY2025_10K.txt | 172309048af2a6a2dab515d765f00a7c89bf8c874c6104a5e3a052b66cad4512 | Annual report on Form 10-K for the year ended December 31, 2025 (text, 3,401 lines) |
| CZR_Q2_2026_10Q.txt | f369ce5f1ebeddd9a0d4ce02ce3958112267d8701d1a348dfd6dc82d2034793a | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 (text, 1,557 lines) |
| CZR_Q2_2026_Earnings_Release.txt | b385f76ff631243d1053fa8073ebde4f8886b4a50c9ce34ce3498d6b2ac3e9f8 | Exhibit 99.1 earnings release dated July 28, 2026 (text, 194 lines) |
| context | 70a1a94c5cc4a6bf8f11bf47e9f0a41d9be046e2bcfa93425809b6450d15d5c1 | User run settings; not issuer evidence |

Supplied handoffs: none (CP-0 is the first module). Locators are line numbers of the pinned text files.

## Findings

### Readiness verdict

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025, FY2024 and FY2023 statements and unaudited June 30, 2026 interim statements with comparatives are located. Text conversion flattens tables; no original HTML or XBRL is supplied. |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, history, the pending merger and debt descriptions are located. The Merger Agreement, debt documents, leases and proxy statement are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | CP-2 can synthesise from CP-1 and CP-1A and the located covenant, lease and liquidity text. Merger financing terms and the post-closing capital structure are not supplied. |
| CP-5 | READY_WITH_LIMITATIONS | All sources are text with stable line numbers, so claims can be traced. Visual and table-layout checks against the filed HTML are not possible. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for FY2025 (`CZR_FY2025_10K.txt`)

- Family and authority: filed annual report, original authority for the audited consolidated statements. Line 1 onward: "FORM 10-K", "For the fiscal year ended December 31, 2025", "Commission File No. 001-36629 CAESARS ENTERTAINMENT, INC.".
- Audit: line 1625 "REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM"; line 1676 "We have served as the Company’s auditor since 2020." Signature date: line 3396 "February 17, 2026".
- Statements located: balance sheet from line 1680, statements of operations from line 1726, cash flows from line 1811. Debt note from line 2344 ("Note 9. Long-Term Debt"). Adjusted EBITDA reconciliation from line 1318, marked unaudited. Liquidity table at line 1353.
- Units: line 1682 "(Dollars in millions, except par value)"; line 1728 "(In millions, except per share data)". USD.
- Perimeter: consolidated Caesars Entertainment, Inc. with noncontrolling interests (line 1755 "Net income attributable to noncontrolling interests"). Line 1343: "We are a holding company, and our only significant assets are ownership interests in our subsidiaries."

#### Form 10-Q for the quarter ended June 30, 2026 (`CZR_Q2_2026_10Q.txt`)

- Family and authority: filed quarterly report with unaudited condensed statements. Line 1 onward: "For the quarterly period ended June 30, 2026". Signature: line 1552 "Date: July 28, 2026".
- Statements: balance sheet from line 64 (June 30, 2026 and December 31, 2025), statements of operations from line 104 (three and six months ended June 30, 2026 and 2025), cash flows from line 197 (six months). Debt note from line 490. Covenant text from line 587. Merger note from line 272. Liquidity from line 1273.
- Units: line 66 "(In millions)". USD.

#### Earnings release (`CZR_Q2_2026_Earnings_Release.txt`)

- Family and authority: issuer press release furnished as Exhibit 99.1, dated "(July 28, 2026)" (line 3). Management-prepared, unaudited. It repeats the 10-Q statement of operations (lines 142 to 178) and adds segment Adjusted EBITDA (lines 52 to 67), net debt (lines 70 to 80) and an Adjusted EBITDA reconciliation (lines 179 to 191).
- It states facts that are not in the 10-Q tables: "Net debt (a) | $10,842 | $11,018" (line 78) and a debt split by "Bank debt and loans" and "Notes" (lines 74 to 75). These are issuer non-GAAP presentations.
- Version relationship: its statement of operations duplicates the 10-Q. Treat the 10-Q as controlling for statement facts. Do not count the release as independent corroboration of them.

### Information-availability boundary

- All three documents are dated before the as-of date and the cutoff: the 10-K on February 17, 2026, and the 10-Q and release on July 28, 2026.
- Nothing dated between July 28, 2026 and the as-of date is supplied. Events in that window, for example the merger vote, regulatory approvals or merger financing, are Not supplied, not absent.

### Identity and perimeter

- Reporting entity: Caesars Entertainment, Inc., Delaware, NASDAQ "CZR" (10-K lines 1 to 92).
- Debt issuer and borrower: "CEI" credit facilities and notes (10-Q lines 494 to 505); Caesars Virginia facilities ("CVA") are a separate borrower group with their own covenants (10-Q line 599).
- Lease counterparties: VICI and GLPI; the leases are accounted for as financing obligations (10-K line 1705 "Long-term financing obligations"; release line 96).
- Pending owner: Fertitta Gaming Holdco, LLC under the Merger Agreement signed May 27, 2026 (10-Q line 273). The release says the agreement was "announced on May 28, 2026" (line 106). Signing and announcement are different events, not a conflict.
- Unresolved: guarantor and restricted-group detail is not in the supplied text; the context leaves borrower, parent and guarantor fields blank, which is not evidence of their absence.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt, liquidity, non-GAAP | 10-K lines 1680 to 1860, 2344 to 2370; 10-Q lines 64 to 250, 490 to 520; release lines 9 to 191 | Text conversion; financing obligations are a large liability class separate from debt |
| CP-1A | Business, segments, history, transaction, ownership | 10-K lines 88 to 100; 10-Q lines 272 to 305; release lines 9 to 70 | Merger Agreement, merger proxy and 2026 proxy statement not supplied |
| CP-2 | CP-1 and CP-1A outputs; covenants; lease burden; liquidity | 10-Q lines 587 to 600 and 1273 to 1300 | Executed agreements not supplied; covenant definitions not verifiable |
| CP-5 | Traceable claims | All three sources have line numbers | Original HTML and XBRL not supplied |

### Analytical read-through

- Usable coverage: audited FY2025 statements and June 30, 2026 interim statements support a reported financial foundation and a last-twelve-months view built from the year and the two six-month periods.
- Strongest contrary evidence: the pending take-private merger (10-Q line 273) can change ownership, leverage and the debt structure. The 10-Q lists "risks associated with increased leverage from the proposed transaction" (line 1391). The supplied set does not say how existing debt is treated at closing.
- Source risk mechanism: the leases with VICI and GLPI sit in "Long-term financing obligations", not in debt, and their cash cost runs through interest expense (10-K line 1868 "Cash interest paid for rent related to financing obligations"). A consumer that reads only "Total debt" understates fixed obligations.
- What cannot proceed: merger financing analysis, covenant headroom on agreement definitions, guarantor-level analysis.
- Next evidence action: supply the Merger Agreement (8-K of May 28, 2026, exhibit 2.1, per 10-Q line 305), any merger proxy and financing commitments, the CEI Credit Agreement and indentures, and the VICI and GLPI lease agreements.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Merger Agreement, merger financing and post-closing capital structure not supplied | High | CP-1A, CP-2 | Supply the 8-K exhibit 2.1 and any merger proxy or financing documents |
| Events between July 28, 2026 and the as-of date not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| Executed credit agreements, indentures and leases not supplied | High for legal work; Medium for CP-2 | CP-2 | Supply executed documents |
| 2026 proxy statement not supplied | Low | CP-1A governance | Supply if governance detail is needed |
| Text conversions only; original HTML and XBRL not supplied | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |
| No rating reports, market prices or peer data | Low for the selected modules | CP-2 | Not required for this scope; keep Not supplied |

## Next module

- CP-1: use the 10-K and 10-Q statements as controlling; keep debt, financing obligations and lease cash interest separate; keep annual, quarterly and six-month columns separate; label the release's net debt and Adjusted EBITDA as issuer non-GAAP.
- CP-1A: carry the pending merger as the central transaction, with signing on May 27, 2026 and announcement on May 28, 2026; label anything after July 28, 2026 as Not supplied.
- CP-2 and CP-5: carry the missing merger financing and executed documents as restrictions.
