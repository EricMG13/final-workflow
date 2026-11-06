## Request

Issuer: CCC Intelligent Solutions Holdings Inc. (ticker CCC, Delaware, Commission file number 001-39447). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot, host mode. Reporting currency: USD; the filings state amounts in thousands of US dollars, and the earnings releases mix thousands and millions as printed. Current period: Q3 2026 (three months and nine months ended 2026-09-30); prior period: FY2025 (audited, year ended 2025-12-31).

Question for this handoff: can the pinned source set support the four requested downstream consumers (CP-1 financial data, CP-1A business and transaction context, CP-2 fundamental credit synthesis, CP-5 evidence trace validation), and what remains blocked or bounded? This handoff gives a source-sufficiency view only. It gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalise, reconcile or model figures (SOURCE_SUFFICIENCY_ONLY; the downstream input contracts are not evaluated here).

Context file: the run context supplies no deal terms, quotes, ratings, peers, valuation inputs or research questions (all blank or empty), no sponsor, borrower or parent name, and states that no portfolio workbook, prior case, management bridge or legal documents are attached. Blank context values are treated as not supplied, never as zero.

## Sources

No upstream handoffs were supplied to this module (CP-0 is the first module; the handoff set in the request is empty).

Issuer sources relied on (name and sha256 as pinned by CP-OS; every file is a page-chunked text extraction, and `page:N` below means the extracted chunk N, not the printed page). Each extraction begins with a line giving the sha256 of the original HTML file; those are shown in the last column as extraction provenance.

| Source (exact name) | sha256 (pinned extraction) | Chunks | sha256 of original HTML stated in extraction |
| --- | --- | --- | --- |
| 10-K_2025-12-31_ccc-20251231.htm.jsonl | 59a1556351f7a7f353f0b9618ee7cf495b7ba17767f7cd6a5a0ded1621642fde | 186 | 4288ed4c7ec87a9375cf471c9bbf1fc80a69966da016a58e02c47d2835a2f593 |
| 10-Q_2026-03-31_ccc-20260331.htm.jsonl | 39b288dd8e81ee0fdda5870870b9bea592f01074d7af9763a85c294be03c88d4 | 50 | 23fb622675d97690e138eaab86c9d7d9a2b085f1d86ca0f881c339df472f34e8 |
| 10-Q_2026-06-30_ccc-20260630.htm.jsonl | eda11b6dbfa4719333004f220abf5cdc5bfe0e2df75fd21d1a6f0733cf5d331c | 47 | 3210a52b6937c6768ec482252094c45ce5817de379702a1664d14f16bc9a3528 |
| 10-Q_2026-09-30_ccc-20260930.htm.jsonl | 0c88b8b197fab954d1c3ff71345c0e05e9f10d1f3510025ad9548d8138ae8407 | 54 | a387f66e1f6b7a6886f0656f0ab4101c2dbec99aa0c1d92d9a38a4c9401878c2 |
| EX-99.1_2026-04-30_ccc-ex99_1.htm.jsonl | ae3848deb91163ab500fd7932cb28c39aab5b44b52f0fa623f872d5f723093a6 | 10 | 4f9d66a43432f8468e2027f62fbf0f3afaa6aa836a2275e57e097c39bb57154a |
| EX-99.1_2026-07-30_ccc-ex99_1.htm.jsonl | a2b1e7ba00fedac3bf32b37f93a1dd3c6ccb1a88c16f25d3354731a4f4c2fb7c | 10 | 1b1fb09d7e5c16dda813d6ad95bb0e3396c7120afd047e46d3a413cdde10426c |
| EX-99.1_2026-10-29_ccc-ex99_1.htm.jsonl | 6ea0ae7480d6fb5cada60e78aef6508a9d3b3ddbb6b2caecfdee6ff746b5c13f | 12 | f3c99353295a099eea7aa78f8538bc9db1ad209675825c4862a4873d4212ee90 |

Run context (not issuer evidence): `context`, sha256 b5d08a6a26eac33af88a5d18c45e48ca178e243a383ecb998014ab0c163dd60f. Also present in the pack folder and ignored by CP-OS: `_retrieval.json`; it is retrieval metadata, not evidence, and was not used for any figure.

Total retained: 369 of 369 extracted chunks across the seven sources are in the pack (186 + 50 + 47 + 54 + 10 + 10 + 12). Chunk count is not a proxy for readiness; the per-source and per-consumer assessment follows.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings and releases are sufficient to support the financial, business and transaction work, each with bounded limits. The pending take-private is documented only through the company's own summaries. | Medium | The credit agreement and the merger agreement are not in the pack, so covenant definitions and post-deal financing cannot be read at source. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report is audited and three quarterly reports with three releases follow it, so the periods needed for the current and prior year are covered. | Period coverage supports a quarter, nine-month and full-year view without gaps in the reporting chain. | High |
| The only debt is one senior secured term loan and an undrawn revolver, described consistently across the filings. | Facility-level debt work can proceed, but covenant terms can only be read from the company's summaries. | Medium |
| A take-private merger was signed after quarter end and is described only in the third quarter report and release. | The change of control and any refinancing of the existing debt cannot be assessed from the pack. | Medium |
| A few labels and small amounts differ between filings and releases, such as the guarantor name and the basis of total debt. | The differences are small but must be carried as limitations into any leverage or guarantor statement. | Medium |

### Readiness view

Overall view: READY_WITH_LIMITATIONS for all four requested consumers, with no consumer conditional or blocked and no command marked DO NOT RUN. The seven sources are a complete reporting chain for the requested periods: the FY2025 annual report (audited) and the Q1, Q2 and Q3 2026 quarterly reports (unaudited) each carry the primary statements and the debt, liquidity and covenant narrative, and each quarter has a furnished earnings release that is consistent with its quarterly report on the figures checked. The strongest contrary evidence is that the two documents that govern the creditor's position, the 2021 Credit Agreement with its five amendments and the Agreement and Plan of Merger dated 2026-10-14, are listed as exhibits incorporated by reference (10-K page:184; Q3 10-Q page:53) but are not in the pack. Covenant mechanics, change-of-control treatment of the term loan and the merger financing structure are therefore available only as the issuer's own summaries in the filings, which are attributed supporting claims, not the executed documents. This does not prevent any consumer from running; it bounds what they may assert. The next evidence action is to add the executed credit agreement and amendments and the merger agreement (and any later filing on the merger financing) before any covenant-headroom or pro forma statement is made.

### Source-by-source assessment

| Source | Document family and original authority | Entity and perimeter | Period and basis | Located content relied on | Limits |
| --- | --- | --- | --- | --- | --- |
| 10-K FY2025 | Annual report on Form 10-K with auditor's report (10-K page:125, "REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM"); highest authority for FY2025 and comparatives | CCC Intelligent Solutions Holdings Inc. and subsidiaries, consolidated; borrower CCC Intelligent Solutions Inc. is an indirect wholly owned subsidiary (10-K page:158) | FY2025, 2025-12-31, with 2024 and 2023 comparatives; USD thousands | Balance sheet (page:129), cash flows (page:132), debt Note 15 (pages:158-161), commitments Note 23 (page:174), Adjusted EBITDA reconciliation (page:111), covenant risk factor (page:81) | Audited consolidated view only; no tranche-level indenture or agreement text |
| 10-Q Q1 2026 | Quarterly report; unaudited; authority for Q1 2026 and balance at 2026-03-31 | Same consolidated perimeter | Three months ended 2026-03-31; USD thousands | Revenue (page:5), Adjusted EBITDA (page:41), Term Loan principal 1,287,732 (page:20), covenant text (page:20) | Unaudited; no subsequent-events note located |
| 10-Q Q2 2026 | Quarterly report; unaudited; authority for Q2 and six months | Same | Three and six months ended 2026-06-30 | Revenue (page:5), Adjusted EBITDA (page:41), Term Loan principal 1,284,474 (page:18) | Unaudited; no subsequent-events note located |
| 10-Q Q3 2026 | Quarterly report; unaudited; filed 2026-10-29 (signature page:54); authority for Q3, nine months, 2026-09-30 balance sheet and the merger subsequent event | Same; also Parent and Merger Sub for the merger | Three and nine months ended 2026-09-30 and balance at 2026-09-30; USD thousands | Statements (pages:5-8), debt Notes (pages:18-19), subsequent events Note 25 (pages:29-30), liquidity and debt MD&A (pages:45-46), merger risk factors (pages:50-53), Adjusted EBITDA (page:43) | Unaudited; merger terms summarised, exhibit 2.1 incorporated by reference with schedules omitted (page:53, page:54) |
| EX-99.1 2026-04-30 | Earnings release furnished with Form 8-K; management narrative and non-GAAP; subordinate to the filed 10-Q | Holdings consolidated | Q1 2026 | Adjusted EBITDA 120,198 (page:9), debt and cash statement (page:2) | Management attribution; no guidance table checked here |
| EX-99.1 2026-07-30 | Earnings release; same status | Same | Q2 2026 and six months | Adjusted EBITDA 115,478 (page:10), debt and cash statement (page:2) | Same |
| EX-99.1 2026-10-29 | Earnings release; same status | Same; names GTCR and Elliott (page:2) | Q3 2026 and nine months | Merger summary and enterprise value (page:2), guidance suspended (page:2), reconciliations (pages:11-12) | Sponsor names appear only here, not in the 10-Q sections read |

Version relationships: the three 10-Qs are successive cumulative reports, not duplicates and not amendments; each stays an active source for its own period. No restatement or amended filing is present (the only "restate" text in the pack is the 10-K cover check box about incentive compensation recovery, 10-K page:2 of the extraction). The releases are separate attributed documents; where a release and a 10-Q differ, the 10-Q controls.

Extraction fidelity: every source is a flattened text extraction in which tables appear as pipe-separated cell sequences. Charts, images, XBRL tags and any speaker notes were not inspected, and a successful extraction is not a fidelity review. No presentations are in the pack (the retrieval used earnings releases in their place), so no slide-coverage claim is made.

### Consumer assessment

| Consumer | Status | Evidence it demands | Located coverage | Bounded limitations carried forward |
| --- | --- | --- | --- | --- |
| CP-1 financial data (discrete quarters, nine months, fiscal year, add-backs, KPIs, debt, cash-paid interest and tax) | READY_WITH_LIMITATIONS | Statements, quarter versus year-to-date columns, Adjusted EBITDA reconciliations, Software NDR and GDR KPIs, debt table, cash paid for interest and taxes | Q1, Q2 and Q3 three-month columns and nine-month columns; FY2025 with two prior years; Adjusted EBITDA reconciled in each 10-Q and release; cash paid for interest 57,637 for nine months 2026 (10-Q Q3 page:8); Software NDR table (10-Q Q3 page:34); principal maturities by year at 2025-12-31 (10-K page:161) | Q4 2025 is not reported as a discrete quarter in any supplied source (no FY2025 fourth-quarter release in the pack); the covenant ratio, its EBITDA definition and the Adjusted EBITDA basis used by lenders are not in the pack; small tie-out differences listed under Conflicts |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business description, customers, ownership and sponsor, transaction terms, history of financing and acquisitions | Business description (10-K page:5 onward), EvolutionIQ acquisition (10-K Note 3), credit agreement amendments 1 to 5 (10-K pages:158-159), Series A preferred of CCC Cayman and its promissory note (10-Q Q3 pages:19-20), pending merger (10-Q Q3 pages:29-30, 33, 50-53; release 2026-10-29 page:2) | Merger agreement, financing commitments, the treatment of the existing term loan at closing, the pre-deal ownership table and sponsor roles are Not supplied; sponsor names come from the release only; the context carries no sponsor |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Settled upstream registers only; no source text | All source limits above pass through. Sequencing relies on the planner; the missing upstream handoffs are not a source condition | Cannot state covenant headroom or pro forma capital structure from sources; no ratings, quotes or peers in the context |
| CP-5 evidence trace validator | READY_WITH_LIMITATIONS | The prepared pack, to check every cited quote and figure | All 369 chunks are retained and addressable by file and `page:N` | Extraction fidelity not reviewed against the original HTML; the original HTML hashes in the Sources table are provenance only |

### Entity and instrument roles located

| Role | Name as printed | Locator | Note |
| --- | --- | --- | --- |
| Registrant and reporting parent | CCC Intelligent Solutions Holdings Inc. | 10-Q Q3 page:1 | Listed equity (Nasdaq: CCC); 591,041,172 shares outstanding at 2026-10-27 (10-Q Q3 page:1) |
| Borrower | CCC Intelligent Solutions Inc., an indirect wholly owned subsidiary | 10-K page:158 | The release describes it as a subsidiary of the registrant (release 2026-10-29 page:3) |
| Facilities | Term Loan maturing 2032-01-23; 250.0 million 2021 Revolving Credit Facility maturing 2029-09-23 with a springing maturity of 2028-06-22 if more than 234.0 million of term loan remains | 10-Q Q3 page:18 | Revolver undrawn at 2026-09-30, with 1.0 million standby letters of credit reducing availability to 249.0 million (10-Q Q3 page:18) |
| Guarantor and security | Guaranteed by an intermediate holding company and certain other US subsidiaries; first-priority liens on the equity of the borrower and substantially all assets | 10-K page:160; 10-Q Q3 page:18 | Name of the intermediate holdco differs between filings; see Conflicts |
| Non-recourse subsidiary obligation | CCCIS Cayman Holdings Limited note payable to minority investor, 27.6 million at 2026-09-30, without recourse to the registrant | 10-Q Q3 page:19, page:20 | Interest 12.0% per annum, paid in kind |
| Merger counterparties | Mozart Parent, LLC; Mozart Merger Sub (DE), Inc. | 10-Q Q3 page:29 | Agreement dated 2026-10-14; announced 2026-10-15 per the release (page:2) |

### Conflicts and tie-out differences (with both locators and downstream effect)

| Item | Locator A | Locator B | Severity | Downstream effect |
| --- | --- | --- | --- | --- |
| Name of the intermediate holding company guarantor: "Cypress Holdings Intermediate Holdings II, LLC." versus "Cypress Intermediate Holdings II, LLC" | 10-K page:160 | 10-Q Q3 page:18 (same wording in 10-Q Q2 page:18) | Low | CP-1 and CP-1A must quote the guarantor name as printed with both variants; the credit agreement is needed to settle it |
| Covenant described three ways: "springing first lien leverage test" (10-K page:81), "leverage ratio ... cannot exceed 6.25 to 1.00" when revolver borrowings exceed 35% of commitments (10-K page:161; 10-Q Q3 page:18), "first lien net leverage ratio test" (10-Q Q3 page:46) | 10-K page:81, page:161 | 10-Q Q3 page:18, page:46 | Medium | The test level, 6.25 to 1.00, is consistent; whether the ratio is gross or net and the EBITDA definition are not settled in the pack, so headroom cannot be stated |
| Basis of "total debt" in the releases: 1.288 billion at 2026-03-31, 1.27 billion at 2026-06-30, 1.28 billion at 2026-09-30, against Term Loan principal of 1,287,732, 1,284,474 and 1,281,216 (thousands) and net-of-discount-and-fees amounts of 1,275,171, 1,272,378 and 1,269,596 | Releases 2026-04-30 page:2, 2026-07-30 page:2, 2026-10-29 page:2 | 10-Q Q1 page:20, 10-Q Q2 page:18, 10-Q Q3 page:19 | Low | The Q1 and Q3 release figures match principal; the Q2 figure matches the net carrying amount, not principal. Use the 10-Q debt tables, not the release headline, for debt |
| Depreciation: segment note 42,065 (nine months 2026) and 14,792 (Q3 2026) versus 42,120 and 14,811 (6,069 plus 36,051 in the Adjusted EBITDA reconciliation; cash flow statement 42,120) | 10-Q Q3 page:28 | 10-Q Q3 page:8, page:43 | Low | Small classification difference; use the cash-flow and reconciliation amounts for add-backs and flag the segment-note amounts as a different presentation |
| Year-to-date Adjusted EBITDA versus the sum of the quarters | 10-Q Q1 page:41 and 10-Q Q2 page:41 | 10-Q Q2 page:41 | Low | Reported six-month 2026 is 2 thousand above Q1 plus Q2; reported six-month 2025 is 1 thousand above; discrete quarters should be taken from the three-month columns and the difference disclosed |
| Date of the merger: agreement dated 2026-10-14; "On October 15, 2026, CCC announced" | 10-Q Q3 page:29 | Release 2026-10-29 page:2 | None (execution date versus announcement date) | State both dates correctly; the 8-K cited in 10-Q Q3 page:53 was filed on 2026-10-15 |

No conflict was found between the 10-Q Q3 and the release 2026-10-29 on the primary statements checked: revenue 294,093, cash 202,926, Adjusted EBITDA 130,539 and free cash flow 82,465 agree (10-Q Q3 pages:5, 8, 43; release pages:2, 9, 12).

### Evidence for the requested objective

Liquidity and debt: cash and cash equivalents were 202,926 thousand at 2026-09-30 (10-Q Q3 page:5); Term Loan principal 1,281.2 million with 13.0 million current; the 250.0 million revolver was undrawn with 249.0 million available after 1.0 million of letters of credit (10-Q Q3 page:18). Swaps fix $750.0 million notional at about 3.94% through 2027-07-31 (10-Q Q3 page:19). Other claims located: operating lease liabilities, long-term licensing agreement, purchase obligations (10-K Note 23, page:174, total 164,515 thousand at 2025-12-31; unchanged materially at 2026-09-30 per 10-Q Q3 page:25), and the non-recourse promissory note.

Merger terms located: cash consideration of $7.75 per share, expected close in the first quarter of 2027, no financing condition (10-Q Q3 pages:29-30); outside date 2027-04-14, company termination fee of $149.52 million and a parent fee of approximately $313.99 million (10-Q Q3 page:51); enterprise value of approximately $6.1 billion and guidance suspended (release 2026-10-29 page:2). The interim covenants restrict incurrence of certain debt, dividends and repurchases without Parent's consent (10-Q Q3 pages:22, 45, 52).

## Calculations

Source-consistency tie-outs only (no normalisation). All amounts in USD thousands unless stated.

| Check | Inputs | Result |
| --- | --- | --- |
| Revenue, Q1 + Q2 + Q3 2026 against nine months 2026 | 281,274 (10-Q Q1 page:5) + 285,931 (10-Q Q2 page:5) + 294,093 (10-Q Q3 page:5) | 861,298, equal to the nine-month revenue 861,298 (10-Q Q3 page:5) |
| Revenue, Q1 + Q2 against six months 2026 | 281,274 + 285,931 | 567,205, equal to the six-month revenue 567,205 (10-Q Q2 page:5) |
| Adjusted EBITDA, Q1 + Q2 against six months 2026 | 120,198 + 115,478 | 235,676 against reported 235,678: difference 2 |
| Adjusted EBITDA, six months 2026 + Q3 against nine months 2026 | 235,678 + 130,539 | 366,217, equal to the reported 366,217 (10-Q Q3 page:43) |
| Adjusted EBITDA, Q1 + Q2 against six months 2025 | 99,077 + 108,116 | 207,193 against reported 207,194: difference 1 |
| Term Loan carrying amount, 2026-09-30 | 1,281,216 - 912 - 10,708 (10-Q Q3 page:19) | 1,269,596, equal to the reported net amount; 13,033 current + 1,256,563 non-current = 1,269,596 |
| Revolver availability, 2026-09-30 | 250.0 million - 1.0 million of standby letters of credit (10-Q Q3 page:18) | 249.0 million, equal to the reported availability |
| 10-K principal maturities, 2025-12-31 | 13,033 x 4 (2026 to 2029) + 1,238,858 (2030, as printed) (10-K page:161) | 1,290,990, equal to the reported total; the printed 2030 bucket includes the balance due at the 2032 maturity as the filing shows it, which should be checked in CP-1 |
| Cash, 2026-09-30 | Balance sheet 202,926 (10-Q Q3 page:5); cash flow statement end of period 202,926 (page:8) | Equal |
| Share retirements, Q1 2026 | 16,565,982 (10-Q Q3 page:22) + 9,606,474 (10-Q Q3 page:23) | 26,172,456, equal to the 26,172,456 shares repurchased and retired in the equity statement (10-Q Q3 page:6) |
| Depreciation difference, nine months 2026 | 42,120 - 42,065 | 55 (Q3 2026: 14,811 - 14,792 = 19) |
| Page count | 186 + 50 + 47 + 54 + 10 + 10 + 12 | 369 |

The 10-K maturity row is a tie-out of the printed table only. Its 2030 bucket sits oddly against the stated 2032-01-23 maturity of the term loan (10-Q Q3 page:18); this is flagged as a presentation question for CP-1, not resolved here.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| 2021 Credit Agreement and Amendments 1 to 5 not supplied (listed at 10-K page:184); definitions of leverage ratio, EBITDA, first lien net indebtedness, mandatory prepayment trigger of leverage above 3.5 (10-K page:159) and change-of-control terms are Not supplied | High for covenant headroom; medium for the others | CP-1, CP-1A, CP-2, CP-5 | Add the executed agreement and amendments; until then covenant statements rest on issuer summaries |
| Agreement and Plan of Merger (exhibit 2.1 to the 8-K of 2026-10-15) not supplied; schedules omitted (10-Q Q3 page:54); financing sources and amounts, the treatment of the existing term loan and revolver at closing and the sponsor consortium are Not supplied beyond the release and risk factor text | High for pro forma and change-of-control work | CP-1A, CP-2, CP-5 | Add the 8-K and merger agreement; pro forma leverage is Not calculable from this pack |
| Q4 2025 as a discrete quarter is Not supplied as reported (no FY2025 fourth-quarter release in the pack); it could only be derived by difference between FY2025 and nine months 2025 | Low | CP-1 | Add the release for the fourth quarter of 2025 or label any derived quarter as derived |
| Proxy statement for the merger is not yet filed (release 2026-10-29 says it will be filed); pre-deal ownership and background of the merger are Not supplied; the context carries no sponsor | Medium | CP-1A | Add the proxy statement when filed, if before the cutoff; nothing after 2026-11-05 may be used |
| Ratings, quotes, peers and valuation inputs: blank in the context, so Not supplied | Not relevant to these four consumers | None of the four | Supply only if a later module needs them |
| Images, charts and XBRL tags not inspected; extraction fidelity not reviewed | Low | CP-5 | Use the original HTML for any table that looks flattened |
| No Subsequent events note located in the Q1 and Q2 2026 10-Qs or as a numbered note in the 10-K (searched for "SUBSEQUENT" in each) | Low | CP-1A | None required; the Q3 10-Q Note 25 carries the merger |
| Guarantor name, covenant wording, total-debt basis and depreciation presentation differences (see Conflicts) | Low to medium | CP-1, CP-1A, CP-2 | Quote as printed, prefer the 10-Q debt tables, and disclose the differences |

## Next module

Proceed with CP-1 (financial data) first, then CP-1A, CP-2 and CP-5 in the order the planner sets; none is blocked. Carry forward these instructions: take debt from the 10-Q and 10-K debt tables (principal 1,281,216 and carrying 1,269,596 at 2026-09-30), not from release headlines; take discrete quarters from three-month columns; label FY2025 as audited and 2026 periods as unaudited; quote the guarantor name and covenant wording as printed; treat the merger as a subsequent event of 2026-10-14 with the agreement itself Not supplied; and treat covenant headroom and pro forma capital structure as Not calculable until the credit agreement and merger agreement are added.
