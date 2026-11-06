## Request

Issuer: Skeena Resources Ltd, a pre-production gold and silver developer (a mining company "in the development stage" building the Eskay Creek project, June 30, 2026 filing, page:4) (issuer id ske; registrant name on the filings is Skeena Resources Limited, a British Columbia corporation; NYSE and TSX ticker SKE). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot, public case. Reporting currency: CAD (Canadian dollars, thousands in the statements). Current period per context: q2-2026 (quarter and six months ended June 30, 2026); prior period per context: fy-2025.

Question for this module: can the supplied source set support the requested downstream modules (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize, reconcile or calculate figures. The context file holds the user's dated settings and is not issuer evidence; it leaves guarantors, borrower, parent, ratings, quotes and deal terms blank, and blank values are not treated as zero.

## Sources

### Issuer sources relied on

All pinned sources are page-chunked text extractions (jsonl) of filings; page numbers below are the extraction chunk `page:N`, not printed pages.

| Source (exact name) | sha256 | Pages retained | Document family |
| --- | --- | --- | --- |
| 40-F_2025-12-31_ske-20251231x40f.htm.jsonl | db53ff9f8d0ca28c9b2edfb7202c651bb5c9ec8c989c923bb91bcc11481dd65e | 9 | Form 40-F annual report wrapper, fiscal year ended December 31, 2025 |
| 6-K-EX-99.1_2026-03-24_exh_991.htm.jsonl | 2c276dba594c2df305ad125f0ece05f65167118a8d8060b6fa5d7edae3ae61ff | 3 | Press release, fourth quarter and annual 2025 results |
| 6-K-EX-99.1_2026-05-15_ske-20260515xex99d1.htm.jsonl | 232a824d9608ba6939a5237ea02786aae7b7f6f4a3ef441bec526b8439fdd718 | 4 | Press release, Q1 2026 results |
| 6-K-EX-99.1_2026-08-13_ske-20260813xex99d1.htm.jsonl | c4db22929f19fe544f88a7604e2308cdbc32700c4f1804f3c24f0271e5a2ab28 | 3 | Press release, Q2 2026 results |
| 6-K-EX-99.2_2025-11-13_ske-20251113xex99d2.htm.jsonl | a3b00c87d028f94b90bcea93f3fd8fe3b7d050af714766a40adae75d64ae2545 | 16 | Condensed interim consolidated financial statements, three and nine months ended September 30, 2025 and 2024 |
| 6-K-EX-99.2_2026-05-15_ske-20260515xex99d2.htm.jsonl | 23892a03c3bd6fd8f48bf0d8bc66e12cf89a073a244322844de1eee4158909d7 | 15 | Condensed interim consolidated financial statements, three months ended March 31, 2026 and 2025 |
| 6-K-EX-99.2_2026-08-13_ske-20260813xex99d2.htm.jsonl | f089cfed7c41a13c1124e873c8cf9d986ddb809584e80594413f338c0cb3dda8 | 19 | Condensed interim consolidated financial statements, three and six months ended June 30, 2026 and 2025 |

The retrieval index file in the pack folder (`_retrieval.json`) was ignored by the run and is not relied on.

### Context file (settings, not issuer evidence)

| Item | sha256 |
| --- | --- |
| context file for ske, as of 2026-11-05 | 74622c0ba0b18d4f8697485a569e78b3429cdc3e20d2499bc2bcfcfddaa82602 |

### Supplied handoffs

None. CP-0 is the first module of this run and CP-OS supplied no upstream handoff (the request lists an empty handoff set).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The pack supports a Canadian-dollar financing and liquidity review of this pre-production gold and silver developer through June 30, 2026, with limitations. Annual report exhibits, management commentary and the notes' legal terms are not in the pack. | Medium | No full-year 2025 statements, management discussion or Senior Secured Notes legal terms are supplied; the latest balance sheet date is June 30, 2026. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Three sets of unaudited condensed interim statements, in Canadian dollars, carry balance sheets, cash flows and debt notes. | Supports liquidity, debt and funding-need analysis as at June 30, 2026, with unaudited status carried forward. | Medium |
| The annual report filing is a cover wrapper; the audited statements, management discussion and annual information form it incorporates are absent. | Full-year 2025 flows cannot be sourced; December 31, 2025 balances come only from later interim comparatives. | High |
| Senior Secured Notes terms appear only as summarized in the financial statement notes; no indenture or covenant text is supplied. | Covenants, guarantors, security and fund-release conditions cannot be assessed from the pack, which limits headroom and recovery work. | High |
| Gold Stream financial covenants are described in earlier quarters but not in the latest quarter, after part of the stream was repurchased. | Whether those tests still bind is unresolved, which affects any covenant headroom conclusion. | Medium |
| The three press releases carry no financial results or reconciliations. | Results rest on the filed statements; management claims on timing carry only attributed weight. | High |

### Readiness view

The effective source set can support the requested downstream work for the current period (quarter and six months ended June 30, 2026) with bounded limitations, and no source is unusable. The latest statements are filed financial statements with complete primary statements and a notes set that covers financial instruments, long-term debt, the Project Financing Package, royalty liabilities, closure provisions and contingencies. The strongest contrary evidence is that the Form 40-F in the pack is only a wrapper: it incorporates the annual information form, the management discussion and the audited statements as exhibits that are not retained, so full-year 2025 flows and annual disclosures cannot be located. The legal documents for the April 2026 Senior Secured Notes, the Gold Stream and the royalty agreements are not supplied, so terms are available only as the notes summarize them. Because CP-0 does not assess downstream analytical handoffs as source conditions, CP-1 and CP-1A are assessed as READY_WITH_LIMITATIONS and CP-2 and CP-5 as READY_WITH_LIMITATIONS inheriting those limitations. This is a statement of source sufficiency only, not a finding on credit quality.

| Consumer | Status | Evidence demand and bounded limitation |
| --- | --- | --- |
| CP-1 (financial data) | READY_WITH_LIMITATIONS | Q2 2026 statements give the balance sheet, three-month and six-month income and cash flow, debt, lease, royalty, closure and maturity-table disclosures in CAD. Limits: no full-year 2025 income statement or cash flow, no management discussion, unaudited interim basis, no covenant text for the Senior Secured Notes. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Notes describe the Eskay Creek project, the April 2026 notes offering and use of proceeds, the Gold Stream repurchase and the royalty grants. Limits: the annual information form and technical report are absent, press releases are narrative only, and no executed transaction documents are supplied. |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Draws only on settled CP-1 and CP-1A output; inherits every limitation above. Whether upstream handoffs are complete is for the dependency planner, not a source condition. |
| CP-5 (evidence trace validation) | READY_WITH_LIMITATIONS | Can trace claims to retained pages; claims that depend on absent annual or legal documents must be carried as gaps, not supported. |

### Source assessments

| Source | Original authority and perimeter | Period and basis | Located evidence and limitation |
| --- | --- | --- | --- |
| Form 40-F (page:1 to page:9) | Filed annual report of the registrant, Skeena Resources Limited, signed by the CFO on March 24, 2026 (page:9). Single registrant; no subsidiaries, guarantors or restricted-group split named. | Fiscal year ended December 31, 2025; IFRS as issued by the IASB (page:4). | Cover states "The Registrant had 121,300,287 Common Shares issued and outstanding as of December 31, 2025." (page:1). Substantive documents are incorporated by reference: "The following documents, filed as Exhibits 99.1, 99.2 and 99.3 hereto, are incorporated herein by reference into this Annual Report" (page:2); exhibit index at page:8 and page:9. Those exhibits are not retained, so this source contributes identity, currency (page:4), controls (page:5) and governance only. |
| Press release, March 24, 2026 (page:1 to page:3) | Issuer press release, an attributed management document, not a statement. | Fourth quarter and year ended December 31, 2025. | Says "The financial statements, management’s discussion and analysis (“MD&A”), and annual information form (“AIF”) are available on Skeena’s website" (page:1). It carries no financial figures. Management timing claim: "initial production and cash flow in the second quarter of 2027" (page:1). |
| Press release, May 15, 2026 (page:1 to page:4; page:2 is a footer only) | Issuer press release, attributed management document. | Quarter ended March 31, 2026. | "reports interim financial results for the quarter ended March 31, 2026" (page:1). Forward-looking statements mention "statements relating to the intended use of proceeds from the Senior Secured Notes" (page:3). No figures. |
| Press release, August 13, 2026 (page:1 to page:3) | Issuer press release, attributed management document. | Quarter ended June 30, 2026. | "reports interim financial results for the quarter ended June 30, 2026" (page:1). Names risks including "failure to comply with debt covenants or other financing terms" and "inability to access restricted funds or other financing proceeds when required" (page:3). No figures. |
| Interim statements, September 30, 2025 (page:1 to page:16) | Filed unaudited statements of Skeena Resources Limited, consolidated; Board approval stated as "approved these condensed interim consolidated financial statements for issuance on November 12, 2025" (page:4). | Three and nine months ended September 30, 2025 and 2024; balance sheet at September 30, 2025 and December 31, 2024 (page:1). CAD thousands. | Primary statements at page:1 to page:3; Project Financing Package with Orion and the then-undrawn Senior Secured Term Loan facility in the notes (page:4, page:11, page:12). Pre-dates the notes offering and the Gold Stream repurchase. |
| Interim statements, March 31, 2026 (page:1 to page:15) | Filed unaudited statements, consolidated; approved "on May 15, 2026" (page:4). | Three months ended March 31, 2026 and 2025; balance sheet at March 31, 2026 and December 31, 2025 (page:1). CAD thousands. | Gold Stream terms and covenants at page:10 and page:11; liquidity maturity table at page:8; Subsequent Event note on the April 10, 2026 notes offering at page:15. Shows the Gold Stream stream percentage before the repurchase and covenant text that the later quarter does not repeat. |
| Interim statements, June 30, 2026 (page:1 to page:19) | Filed unaudited statements, consolidated; approved "on August 13, 2026" (page:4). Most recent financial period in the pack. | Three and six months ended June 30, 2026 and 2025; balance sheet at June 30, 2026 and December 31, 2025 (page:1). Presented "in Canadian dollars, and tabular values are rounded to the nearest thousand" (page:5). | Statements at page:1 to page:3; Senior Secured Notes terms in Note 6 (page:12 to page:14); Project Financing Package and Gold Stream (page:14, page:15); royalty liabilities (page:15, page:16); undiscounted maturity table (page:11); contingencies (page:19). No subsequent events note. |

### Version relationships and duplicates

- No source is a duplicate of another. The three interim statement sets are separate period filings and all remain active: the six-month filing contains the discrete three-month and six-month 2026 and 2025 columns, the March 2026 filing carries the first quarter, and the September 2025 filing carries nine-month 2025 and the December 31, 2024 balance sheet. None supersedes the others.
- The 40-F wrapper and the March 24, 2026 press release both point to the annual statements, but neither contains them. The annual statements, management discussion and annual information form are separate documents that are not in the pack.
- December 31, 2025 balances are available only as comparatives inside the March 2026 and June 2026 interim statements; they are not a substitute for audited full-year statements.

### Currency, units and basis

- Reporting currency is Canadian dollars: statements are "Unaudited - expressed in thousands of Canadian dollars" (June 30, 2026 filing, page:1) and the 40-F states that "$" or "C$" means Canadian dollars (page:4). This matches the context currency (CAD).
- The Senior Secured Notes are US dollar denominated: "$1,036,761,000 (US$750,000,000)" (June 30, 2026 filing, page:12). US dollar translations are printed alongside CAD in the notes; the exchange rates used differ by date and are not reconciled here.
- All interim statements are unaudited and prepared under IAS 34 (June 30, 2026 filing, page:4). The page footers on the 2026 interim statements read "Consolidated 2025 Financial Statements"; the period was taken from the statement headers, not from that footer.

### Observations and conflicts logged

| Item | Locators | Downstream effect |
| --- | --- | --- |
| Gold Stream financial covenants and security are described in the March 2026 statements (debt service coverage test and an unrestricted cash minimum, "General security and share pledge agreements in favour of Orion") but the June 2026 Gold Stream note does not repeat them after the repurchase of part of the stream. Not a numerical conflict; an unresolved continuity gap. | March 2026 filing, page:10 and page:11; June 2026 filing, page:14 and page:15 | CP-1 and CP-2 cannot state which covenants or security still apply; carry as Not supplied. |
| The balance sheet caption "COMMITMENTS (NOTE 4)" points to Note 4, where commitments appear only as a "Contractual commitments" row in the undiscounted maturity table, with no schedule by counterparty or project. | June 30, 2026 filing, page:1 and page:11 | Commitment detail is limited to the one table row. |
| The June 2026 statements carry no subsequent events caption or note, while the March 2026 statements do. | March 2026 filing, page:1 and page:15; June 2026 filing, page:1 | Events between June 30, 2026 and the cutoff cannot be located in the pack. |
| Note wording describes release of funds from the construction disbursement account as a condition: "Should the Company not be able to release the funds within the construction disbursement account provided by the Senior Secured Notes" (June 2026) versus "Should the Company not be able to draw the Senior Secured Notes" (March 2026). Reflects the later closing of the offering, not a conflict. | June 30, 2026 filing, page:4; March 2026 filing, page:4 | Conditions precedent and release mechanics sit in documents that are not supplied. |

### Coverage register

| Coverage unit | Disposition |
| --- | --- |
| Primary statements for the quarter and six months ended June 30, 2026 (financial position, loss, equity, cash flows) | Retained, located (June 2026 filing, page:1 to page:3) |
| Notes: financial instruments and maturity table, mineral property, long-term debt, Project Financing Package, royalty liabilities, closure provision, capital stock, supplemental cash flow, related parties, contingencies | Retained, located (June 2026 filing, page:8 to page:19) |
| Same statements for the quarter ended March 31, 2026 and for the quarter and nine months ended September 30, 2025 | Retained, located (March 2026 filing page:1 to page:15; September 2025 filing page:1 to page:16) |
| Narrative press releases (three) | Retained; narrative only, no figures |
| Annual audited statements for the year ended December 31, 2025 | Explicit gap: named in the 40-F exhibit index, not retained |
| Management discussion and analysis (annual and interim) | Explicit gap: referred to in all three press releases, not retained |
| Annual information form and technical report | Explicit gap: not retained |
| Senior Secured Notes indenture, Gold Stream agreement, royalty agreements | Explicit gap: not retained; context records legal documents as none |
| Quarter ended December 31, 2025 discrete statements | Explicit gap: not supplied |
| Presentations, workbooks, scans and images | None supplied; no image or chart coverage claimed from text extraction |

Extraction status is distinct from fidelity: all seven sources extracted to text, but no fidelity review of tables against the original filings was performed. Table cells arrive as one value per line, so column alignment was read from the statement layout and should be confirmed where a figure is used downstream.

## Calculations

No new calculation was performed. CP-0 does not normalize, reconcile or derive figures, and no figure in this handoff is derived.

Coverage counts only (retained extraction pages, not a readiness proxy): 9 + 3 + 4 + 3 + 16 + 15 + 19 = 69 pages across the 7 issuer sources.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Audited consolidated financial statements for the year ended December 31, 2025 not retained (Form 40-F Exhibit 99.3). Not supplied: full-year 2025 income statement, cash flow and notes. | High | CP-1, CP-2, CP-5 | Add the 40-F Exhibit 99.3 to the pack. |
| Annual and interim management discussion not retained. Not supplied: management's liquidity and capital resources discussion and non-IFRS content. | Medium | CP-1, CP-1A, CP-2 | Add the 40-F Exhibit 99.2 and the interim discussion filings. |
| Annual information form and technical report not retained. Not supplied: project description, reserves, schedule and capital budget detail. | Medium | CP-1A, CP-2 | Add the 40-F Exhibit 99.1 and the current technical report if filed. |
| No executed financing documents. Not supplied: Senior Secured Notes indenture terms, guarantors, security package, covenants, interest reserve and construction disbursement release conditions; Gold Stream and royalty agreements. | High | CP-1, CP-1A, CP-2 | Add the indenture and agreements, or treat note summaries as the only evidence and label them so. |
| Continuity of Gold Stream covenants and security after the repurchase not stated in the latest quarter. Not calculable: any covenant headroom. | Medium | CP-1, CP-2 | Locate the amending agreement or the management discussion that addresses it. |
| No events after June 30, 2026 in the pack. The latest filing is dated August 13, 2026 and the as-of date is November 5, 2026; nothing in the pack shows whether later filings exist. | Medium | All | Check for any later periodic filing or material report up to the cutoff. |
| Discrete fourth quarter 2025 statements not supplied; December 31, 2025 balances exist only as comparatives. | Low | CP-1 | Derive only after the annual statements are added. |
| Unaudited interim basis and reliance on text extraction without fidelity review. | Low | All | Confirm figures against the filed documents when used. |
| Counterparty detail for commitments, and the identity of the named royalty grantees ("certain third parties"), not stated. | Low | CP-1A, CP-2 | Not available from the pack. |

## Next module

Proceed to CP-1 for the quarter and six months ended June 30, 2026 in Canadian dollars, using the June 30, 2026 statements as primary source and the March 2026 and September 2025 statements for earlier periods. CP-1 should label every figure by period (three months, six months, balance sheet date), carry the unaudited status and the Senior Secured Notes' US dollar denomination, and record full-year 2025 flows, management discussion and legal terms as Not supplied. Then CP-1A for the Eskay Creek project and financing transactions, then CP-2, then CP-5. The next evidence action is to add the Form 40-F Exhibits 99.1, 99.2 and 99.3 and, if obtainable, the Senior Secured Notes indenture.
