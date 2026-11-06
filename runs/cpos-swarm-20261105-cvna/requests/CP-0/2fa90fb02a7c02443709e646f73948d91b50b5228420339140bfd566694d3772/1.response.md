## Request

Issuer: CARVANA CO. (issuer id cvna, ticker CVNA, Delaware registrant, Commission File Number 001-38073). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit_snapshot, case kind public. Reporting currency: USD, with the filings stating amounts in millions unless a locator says otherwise. Current period: Q3 2026 (quarter ended September 30, 2026). Prior period: FY2025 (year ended December 31, 2025).

Question answered by this module: can the effective source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalize, reconcile or calculate figures. It separates source sufficiency from completion of downstream analysis. The context file carries no deal terms, quotes, ratings, valuation inputs, peers, attachments or research questions (its legal-documents attachment flag is "none"); those blanks are treated as not supplied, not as zero.

Citation form used below: [source label, page:N, "exact substring"]. A page is the source chunk shown as page:N, not a printed page number. Source labels are defined in `## Sources`.

## Sources

### Issuer sources relied on

| Label | Exact source name | sha256 |
| --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_cvna-20251231.htm.jsonl | e28106ced83e487c2b18b6b610810086a1c332c7b8604f85efce9667b5e6a76a |
| 10-Q Q1 2026 | 10-Q_2026-03-31_cvna-20260331.htm.jsonl | 8d6ff7213869775e0ae3673fa4f3f8504cd246dbeeab2abdd24aff1860443100 |
| 10-Q Q2 2026 | 10-Q_2026-06-30_cvna-20260630.htm.jsonl | 4b43d425f11176a90828e0a1b668c0134d6d4d593beed8283823a525740b768c |
| 10-Q Q3 2026 | 10-Q_2026-09-30_cvna-20260930.htm.jsonl | 2940535c20dfe242e3d91621f5af16ca08b2dcda177838339ceb7be2805a2b78 |
| EX-99.1 Q1 2026 | EX-99.1_2026-04-29_ex99_1q12026.htm.jsonl | 7e7abd08434c84563cd9ee9bcfd3c51c356bc5d08b4e44ad4a2ea187eaea5514 |
| EX-99.1 Q2 2026 | EX-99.1_2026-07-29_ex99_1q22026.htm.jsonl | c4afe91551db432e6e87ceefff8a20a7648db1422c05df5d4cc9109c7c95c8e2 |
| EX-99.1 Q3 2026 | EX-99.1_2026-10-28_ex99_1q32026.htm.jsonl | 77eff687ed065288e545b6eb14e96f0cbf7ef280db37fa826fb72985e87a5e82 |

### Run settings source

| Label | Exact source name | sha256 |
| --- | --- | --- |
| context | context | 3b0d728dae64d48f4491be2af6d53653b4803495916d71df1f3f2f764a94f8be |

The context holds the user's dated settings (run type, pathway, as-of date, cutoff, current and prior period, reporting currency, identity). It is not issuer evidence.

### Supplied handoffs

None. CP-0 is the first module of this run and CP-OS supplied no upstream handoff.

### Not relied on

The pack also holds a retrieval log named _retrieval.json, which the launcher ignored. It was not used as evidence.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed reports and shareholder letters are sufficient for the financial snapshot, with named limits. All four downstream consumers can run, each with limitations. | Medium | No executed financing documents, no updated maturity schedule after the August refinancing, and no ratings or market inputs are in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Seven issuer sources cover the latest annual report, three quarterly reports and three shareholder letters, all dated before the cutoff. | Statements, debt notes, liquidity tables and non-GAAP reconciliations can be read for the current and prior period. | High |
| Financing terms come from filing descriptions only, not from the indentures or credit agreements. | Basket capacity, covenant definitions and lien terms stay unverified until the documents are supplied. | High |
| The latest principal maturity table predates the term loan refinancing. | The maturity wall must be rebuilt from instrument terms, with that limitation carried forward. | High |
| A five-for-one stock split changes share data comparability across the sources. | Per-share and share-count figures need a split label before any cross-period use. | High |

### Readiness view

The effective source set supports the requested snapshot work with limitations. Every consumer is assessed READY_WITH_LIMITATIONS: the owner of each workflow can perform its method on the located evidence, and no consumer is conditional on a missing source or blocked by unusable evidence. This is a statement about source sufficiency only; it is not a statement that downstream analysis is complete, and no normalized quarter, reconciliation or downstream input acceptance is asserted (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED). The evidence is filed financial statements and notes (audited for FY2025, unaudited for the 2026 quarters) plus unaudited management shareholder letters. The strongest contrary evidence is the absence of any executed legal or financing document, so every governing term below rests on the issuer's own description of it.

### Source register

| Source | Document family and authority | Entity and perimeter | Period and basis | Located coverage and status |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Annual report on Form 10-K; filed statements with an audit opinion; controls the facts it states | Carvana Co. and subsidiaries, consolidated | Year ended December 31, 2025, with comparatives; reporting unit is a single segment | Statements, debt note with principal maturities, liquidity table, leases, tax receivable agreement, related parties, litigation, exhibit list; text extracted from all pages, no fidelity review |
| 10-Q Q1 2026 | Quarterly report on Form 10-Q; unaudited filed statements | Carvana Co. and subsidiaries, consolidated | Three months ended March 31, 2026, versus the prior-year quarter and December 31, 2025 balances | Statements, debt note, liquidity table, non-GAAP reconciliation, supplemental cash flow; cash flow is year-to-date only |
| 10-Q Q2 2026 | Quarterly report on Form 10-Q; unaudited filed statements | Carvana Co. and subsidiaries, consolidated | Three and six months ended June 30, 2026 | Same profile; first filing to carry the stock split; includes a subsequent-events note on the Ally amendment |
| 10-Q Q3 2026 | Quarterly report on Form 10-Q; unaudited filed statements; current-period anchor | Carvana Co. and subsidiaries, consolidated | Three and nine months ended September 30, 2026 | Same profile plus the August term loan and bond redemption, the interest rate swap, the Root warrant exchange, the Ally amendment and the exhibit list |
| EX-99.1 Q1 2026 | Earnings release and shareholder letter; management attributed claims, unaudited | Carvana Co. and subsidiaries | Q1 2026 | Narrative, statements, liquidity table, non-GAAP reconciliation; no presentation deck in the pack |
| EX-99.1 Q2 2026 | Earnings release and shareholder letter; management attributed claims, unaudited | Carvana Co. and subsidiaries | Q2 2026 and first half 2026 | Same profile |
| EX-99.1 Q3 2026 | Earnings release and shareholder letter; management attributed claims, unaudited | Carvana Co. and subsidiaries | Q3 2026 and trailing quarters | Same profile plus outlook, a note on 2027 reporting, a quarterly trend table and a liquidity table |

Cover evidence for identity and period: [10-K FY2025, page:1, "For the fiscal year ended December 31, 2025"]; [10-Q Q1 2026, page:1, "For the Quarterly Period Ended March 31, 2026"]; [10-Q Q2 2026, page:1, "For the Quarterly Period Ended June 30, 2026"]; [10-Q Q3 2026, page:1, "For the Quarterly Period Ended September 30, 2026"]. The filing dates are in the pack's retrieval log, not in the extracted text: the latest filing is the Q3 report and its signature page is dated [10-Q Q3 2026, page:88, "Date: October 28, 2026"], before the cutoff. No source in the pack is dated after the cutoff.

Authority and extraction fidelity are separate. The FY2025 statements carry an auditor opinion: [10-K FY2025, page:96, "present fairly, in all material respects"]. The quarterly statements are unaudited: [10-Q Q3 2026, page:2, "Unaudited Condensed Consolidated Balance Sheets"]. The shareholder letters are management communications; where a letter and a filing differ, the filing controls. Extraction here is visible text per chunk; successful extraction is not a fidelity review, and no table was checked against an image.

### Entity roles and perimeter

- Reporting entity: Carvana Co., the registrant, consolidates Carvana Group, LLC as a variable interest entity of which it is the primary beneficiary: [10-Q Q3 2026, page:8, "Carvana Co. owned approximately 65.1% of Carvana Group"]. Non-controlling interests are therefore part of the consolidated equity: [10-Q Q3 2026, page:3, "Non-controlling interests 1,301 762"].
- Borrower and issuer roles: the term loan credit agreement is listed with Carvana Co. as a party and Barclays Bank PLC as administrative agent: [10-Q Q3 2026, page:88, "Credit Agreement, dated as of August 14, 2026, among Carvana Co., the lenders party thereto and Barclays Bank PLC, as Administrative Agent and Syndication Agent"].
- Guarantors: the senior secured notes are guaranteed by the domestic restricted subsidiaries with listed exceptions: [10-Q Q3 2026, page:25, "fully and unconditionally guaranteed on a senior secured basis, jointly and severally, by all of the domestic restricted subsidiaries"]. The pack contains no guarantor schedule naming the individual guarantors. The unsecured notes are described only as guaranteed by "certain" subsidiaries: [10-Q Q3 2026, page:28, "are guaranteed by certain of the Company's subsidiaries"].
- Unrestricted perimeter: [10-Q Q3 2026, page:28, "designated ADESA and its subsidiaries as unrestricted subsidiaries"] under the unsecured note indentures. The treatment of ADESA under the secured note indentures and the term loan is not stated in the located text.
- Special-purpose perimeter: the receivable financing subsidiaries are wholly owned special purpose entities whose assets are not available to the general creditors: [10-Q Q3 2026, page:24, "whose assets are not available to the general creditors of the Company"]. Securitization trusts are unconsolidated variable interest entities: [10-Q Q3 2026, page:21, "Total unconsolidated VIEs"].
- Preferred units mirror the notes: [10-Q Q3 2026, page:33, "For each $1,000 principal amount of Senior Notes that Carvana Co. repays or otherwise retires, one Class A Non-Convertible Preferred Unit is canceled and retired."].
- Related parties: DriveTime administers servicing and warranty functions and Ally is both a lender and a receivable purchaser: [10-Q Q3 2026, page:16, "DriveTime provides servicing and administrative functions associated with the Company's finance receivables."]; [10-Q Q3 2026, page:18, "Ally Master Purchase and Sale Agreement"].
- Segment basis: [10-Q Q3 2026, page:10, "one operating segment and therefore one reportable segment"]. No segment tables exist to read; revenue lines (retail, wholesale, other) are the available disaggregation.

### Coverage by source profile

- Financial reports: statements, period labels and notes are present for every period needed. The debt note lists each instrument class with a table: [10-Q Q3 2026, page:21, "Total debt 5,161 4,976"]. The senior secured and unsecured note tables, the term loan terms and the revolving facility descriptions are in the same note, pages 22 to 30. Cash interest and cash taxes are in the supplemental cash flow note of each report: [10-Q Q3 2026, page:54, "Cash payments for interest $ 443 $ 311"]. Cash flow statements are cumulative year-to-date, so discrete quarterly cash flow requires a subtraction that this module does not perform.
- Liquidity and covenants: a liquidity table is in each 10-Q, the FY2025 10-K and each letter: [10-Q Q3 2026, page:78, "Total liquidity resources $ 7,503 $ 6,739"]. The term loan has no financial maintenance covenant: [10-Q Q3 2026, page:27, "The credit agreement does not contain any financial maintenance covenants."]. Compliance is asserted without test levels: [10-Q Q3 2026, page:30, "the Company was in compliance with all debt covenants"]. The floor plan facility covenants are described only as "certain affirmative and negative covenants" [10-Q Q3 2026, page:22, "amend certain other affirmative and negative covenants"].
- Earnings releases: reported and adjusted figures, a reconciliation and attributed management narrative are present: [EX-99.1 Q3 2026, page:2, "Adjusted EBITDA totaled $800 million"]; the 10-Q reconciliation matches the line: [10-Q Q3 2026, page:77, "Adjusted EBITDA $ 800 $ 637 $ 2,241 $ 1,726"]. The Q3 letter states a forward range and says outlooks will stop: [EX-99.1 Q3 2026, page:3, "we do not plan to provide quarterly or annual financial outlooks"], and gives no reconciliation of forecast figures: [EX-99.1 Q3 2026, page:4, "We have not provided a quantitative reconciliation of forecasted GAAP measures"].
- Legal and financing documents: none is in the pack. Only exhibit lists identify them: [10-K FY2025, page:171, "Supplemental Indenture, dated as of May 9, 2022"], [10-Q Q3 2026, page:88, "First Amendment to Third Amended and Restated Master Purchase and Sale Agreement"].
- Workbooks: none supplied.
- Scans, images and decks: no deck is in the pack; the releases stand in for the quarterly presentations. No chart or image content was inspected, and no image coverage is claimed.

### Version relationships and comparability

- The three 10-Qs and the 10-K are separate periodic reports, not versions of one another; each stays an active source. The Q3 10-Q repeats the December 31, 2025 balance sheet as its comparative: [10-Q Q3 2026, page:2, "December 31, 2025"]. Where the same period appears in two sources the filing controls the shareholder letter.
- Stock split: the five-for-one split took effect in May 2026 and later reports restate share data: [10-Q Q3 2026, page:9, "five-for-one forward stock split"]. The FY2025 10-K and the Q1 10-Q cover pages show pre-split counts: [10-K FY2025, page:2, "142,736,197 shares of Class A common stock outstanding"]; [10-Q Q1 2026, page:1, "143,257,677 shares of Class A common stock outstanding"], against [10-Q Q2 2026, page:1, "719,916,415 shares of Class A common stock outstanding"].
- Period mix: the Q3 10-Q gives three-month and nine-month columns; the Q1 and Q2 10-Qs and letters give discrete quarter columns, so discrete Q1 and Q2 2026 are located. A discrete Q4 2025 column is not printed and would need the FY2025 annual figures less the nine months to September 30, 2025, a derivation left to CP-1.
- Non-GAAP: the Adjusted EBITDA definition adds back share-based compensation, loss on debt extinguishment and others and subtracts warrant revenue: [10-Q Q3 2026, page:76, "minus revenue related to our Warrants"]. It is a company definition, not a covenant definition.

### Gaps and conflicts register

| ID | Gap or conflict | Severity | Affected consumers | Remediation | Citation |
| --- | --- | --- | --- | --- | --- |
| G1 | No executed indenture, term loan credit agreement, floor plan agreement, receivable facility agreement, Ally purchase agreement, loan purchase agreement or equipment loan agreement is in the pack; terms rest on the issuer's note descriptions | High | CP-1, CP-1A, CP-2, CP-5 | Supply the executed documents or the exhibits filed with the 8-K | [10-Q Q3 2026, page:88, "incorporated by reference to Exhibit 10.1 to Carvana Co.'s Current Report on Form 8-K"] |
| G2 | Super senior and pari passu debt capacity are issuer-stated basket capacity that depends on indenture and credit agreement terms not supplied | High | CP-1, CP-2 | Supply the indenture and credit agreement debt and lien covenants | [10-Q Q3 2026, page:79, "subject to the terms and conditions set forth in the indentures"] |
| G3 | The only principal maturity table is as of the FY2025 year-end and includes notes since redeemed; the 10-Qs print no updated table | Medium | CP-1, CP-2 | Rebuild from instrument terms in the Q3 debt note; flag the derivation | [10-K FY2025, page:140, "Principal Maturities"]; [10-K FY2025, page:141, "Thereafter 2,759"] |
| G4 | Floor plan covenant levels and tests are not printed; only compliance is asserted | Medium | CP-1, CP-2 | Supply the floor plan agreement and the amendments | [10-Q Q3 2026, page:30, "the Company was in compliance with all debt covenants"] |
| G5 | Letters of credit, standby or surety arrangements: searched all sources for "letters of credit", "standby" and "surety"; none found, so whether any liquidity is encumbered by them is not stated | Low | CP-1 | None required unless the issuer discloses them; carry as not found, not as zero | searched text of all seven sources |
| G6 | No credit ratings, market capitalization, quotes, peers or valuation inputs in the context | Medium for relative-value work, none for the selected modules | CP-2 | Supply a dated ratings and market input if later modules need it | context fields "ratings": [] and "quotes": [] |
| G7 | No presentation decks; releases substitute | Low | CP-1A | None required; slide-level content cannot be claimed | pack retrieval log |
| G8 | Pre-split and post-split share data coexist across the 10-K, Q1 10-Q and later reports | Medium | CP-1, CP-5 | Label every share figure with its split basis | [10-Q Q3 2026, page:9, "retroactively adjusted"] |
| G9 | The non-current tax receivable agreement liability prints the same value on the balance sheets of three consecutive quarter ends; the Q3 roll-forward ties to it, but the Q1 and Q2 prints should be rechecked against the rollforward before use | Low | CP-1, CP-5 | CP-1 to compare the three balance sheets with the Q3 roll-forward | [10-Q Q1 2026, page:2, "Tax receivable agreement liability, including $1,645 and $1,721, respectively, due to related parties 2,130 2,228"]; [10-Q Q3 2026, page:42, "TRA liability, net of current portion $ 2,130 $ 2,130"] |
| G10 | Guarantor entities are not named; the treatment of ADESA outside the unsecured note indentures is not stated | Medium | CP-1A, CP-2 | Supply the guarantor schedule or indenture | [10-Q Q3 2026, page:28, "are guaranteed by certain of the Company's subsidiaries"] |
| G11 | Cash flow statements are year-to-date only | Low | CP-1 | Derive discrete quarters by subtraction and label them derived | [10-Q Q3 2026, page:80, "Net cash provided by operating activities $ 900 $ 606"] |

No conflict between two sources was found in the figures read for this module. The check compared the Adjusted EBITDA line and the liquidity table across the Q3 10-Q and the Q3 letter and found them to agree: [EX-99.1 Q3 2026, page:12, "Total liquidity resources (4) $ 7,503 $ 6,739"]. This is a spot check, not a reconciliation.

### Consumer assessments

| Consumer | Assessment | Evidence demand and what is located | Limitations carried |
| --- | --- | --- | --- |
| CP-1 financial data | READY_WITH_LIMITATIONS | Statements, discrete quarters, debt by instrument, liquidity, cash interest and non-GAAP reconciliation are located for FY2025 and Q1 to Q3 2026 | G1 to G4, G8, G9, G11 |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business description, related-party arrangements, the August refinancing, the Ally and loan purchase arrangements and litigation are located in the 10-K, the Q3 10-Q and the letters | G1, G7, G10 |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Draws only on upstream handoffs; source evidence behind them is adequate with the same limits | G1 to G4, G6, G10 |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | Reviews the other modules against the pack; the pack is intact and pinned | G8, G9 |

No consumer is marked CONDITIONAL or BLOCKED, so no consumer receives a DO NOT RUN instruction. A missing downstream handoff is not a source condition.

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. Figures appear only inside quotes. The two spot comparisons above (Adjusted EBITDA line and liquidity table in the Q3 10-Q against the Q3 letter) are visual agreement checks of printed values, not new calculations.

## Gaps

The gaps are logged in the gaps and conflicts register under `## Findings` (G1 to G11). The first four limit the creditor-protection analysis most: the absence of executed financing documents, the unverified basket capacity, the stale maturity table and the unstated floor plan covenant levels. Where the sources cannot fill a gap it stays a gap: no letters of credit were found (Not supplied), no ratings are supplied (Not supplied), and no covenant test levels are printed for the floor plan facility (Not supplied). Nothing is treated as zero.

## Next module

CP-1 runs next. It should use the Q3 10-Q debt note and liquidity table as the current anchor, the FY2025 10-K as the prior-period anchor, the Q1 and Q2 10-Qs for discrete 2026 quarters, and the letters for attributed management claims only. It must carry limitations G1 to G4, G8, G9 and G11, label derived quarters as derived, label every share figure with its split basis, and rebuild the maturity profile from instrument terms rather than from the stale FY2025 table. CP-1A, CP-2 and CP-5 follow in the planner's order.
