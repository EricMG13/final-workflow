## Request

Subject: Millicom International Cellular S.A. (issuer id tigo; Luxembourg société anonyme, Commission file number 001-38763, foreign private issuer filing Form 20-F, listed on Nasdaq as TIGO). As-of date: 2026-11-05 (cutoff 2026-11-05; current period q3-2026, prior period fy-2025; reporting currency USD per the run context). Pathway: credit_snapshot, public case, research run.

Question answered by this module (source readiness only): can the supplied source set support the requested downstream modules CP-1 (financials and credit metrics), CP-1A (business and transaction context), CP-2 (fundamental credit synthesis) and CP-5 (evidence trace validation), and what remains blocked or limited? This module gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize, reconcile or calculate figures. The assertion is SOURCE_SUFFICIENCY_ONLY.

Locator convention: "chunk N" is the `page` field of the converted-text file named in Sources (about 3,000 characters per chunk, not the printed page of the filing). Printed page labels are quoted only where visible in the text. Currency is USD millions unless stated.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Document family and authority | Perimeter and period | Chunks |
| --- | --- | --- | --- | --- |
| 20-F_2025-12-31_tigo-20251231.htm.jsonl | 13be2a8c900b103376e04c45e18282d28f2b1aac3516bfaed99fc02cc0e15f37 | Annual report on Form 20-F, "As filed with the Securities and Exchange Commission on March 24, 2026"; audited IFRS statements (KPMG LLP opinion, Miami, March 24, 2026; Ernst & Young S.A. opinion for the earlier year) plus management report; controls the audited year-end facts | Millicom International Cellular S.A. and subsidiaries, consolidated; Honduras joint venture equity-accounted; fiscal years 2025, 2024, 2023 | 298 |
| 6-K_2026-05-12_dp246578_6k.htm.jsonl | e31fa18185d3ceef7ba9e0133efc952dd4f43ccbd999e9a5f5b5af04d8dbf712 | Form 6-K furnishing unaudited IAS 34 interim statements for the three months ended March 31, 2026 and the Q1 2026 earnings release (statements dated May 12, 2026); no auditor review report present | Consolidated, Q1 2026 versus Q1 2025 (comparatives re-presented); Coltel consolidated from February 6, 2026 | 35 |
| 6-K_2026-08-06_dp251442_6k.htm.jsonl | 76b47ade3b6a5a2f060db2592b816c6ed584aa9ed405d036c0be893943dc1c51 | Form 6-K furnishing the half-year report for the six months ended June 30, 2026 (interim management report, responsibility statement, KPMG Audit S.à r.l. review report under ISRE 2410 dated August 6, 2026, unaudited IAS 34 statements), the Q2 2026 earnings release and a press release | Consolidated, H1 2026 and Q2 2026; 2025 comparative columns for the income statement are marked "Not reviewed" (chunk 8) | 50 |
| 6-K_2026-11-05_dp256407_6k.htm.jsonl | 6ab7c7e5e635829f16eb15a89301463e6131db3f5c0e68ee118ba6350801f894 | Form 6-K furnishing (Item 1) unaudited IAS 34 interim statements for the nine months ended September 30, 2026, (Item 2) the Q3 2026 earnings release and (Item 3) a press release dated November 5, 2026; no auditor review report present; signed November 5, 2026 (chunk 45) | Consolidated, 9M 2026 and Q3 2026; Board authorized issue on November 4, 2026 (chunk 6); Dec 31, 2025 balance sheet comparatives restated (chunk 4, chunk 12) | 45 |

### Run context (not issuer evidence)

| Item | sha256 | Use |
| --- | --- | --- |
| context (tigo.json, schema context/1) | 5b145622a49a1e38ec7885504ac944230be02601fefa1d2f3fb7d83ded83c956 | Dated user settings only. Ratings, quotes, deal terms, peers and assumptions are blank and are not treated as zero. Attachments declare portfolio_workbook false, prior_case false, management_bridge false, legal_documents "none". |

### Supplied handoffs

None. CP-0 is the first module; CP-OS supplied no upstream handoff for it.

### Coverage review by source

The converted text of every source was searched and the sections below were read. A successful text conversion is not a fidelity review: tables were read as text rows and no chart, image or spreadsheet content was inspected.

| Source | Content read and retained | Content not retained or not supplied |
| --- | --- | --- |
| 20-F | Cover and cross-reference guide (chunks 1-5); liquidity and capital resources, cash repatriation, consolidated indebtedness by entity, covenant narrative, supplier finance (chunks 110-117); material contracts list (chunks 123-127); organizational structure (chunks 91-92); debt note C.3 including bond table, bank table, facility narratives, guarantees and covenants (chunks 244-258); liquidity maturity profile, currency split and capital management with Moody's and Fitch ratings (chunks 270-273); auditor reports (chunks 147, 193-194) | Risk factors, operating results by country, governance, tax and remaining notes located but not read line by line in this module; exhibits (indentures, credit agreements) are cited by the 20-F but are not supplied |
| 6-K 2026-05-12 | Income statement, cash flow, debt maturity analysis, financial obligations note, Q1 earnings release with net debt and leverage table (chunks 1, 3, 17-18, 20-25) | Segment, tax and per-country detail not read in this module |
| 6-K 2026-08-06 | Review report and responsibility statement (chunks 7-8); income statement (chunk 8); financial obligations, maturity table, fair value, derivatives (chunks 28-29); debt discussion and net debt table (chunks 35-36); litigation note (chunk 29) | Segment, tax and impairment notes not read in detail in this module |
| 6-K 2026-11-05 | Complete interim statements and notes 1 to 16 (chunks 1-28); earnings release including cash flow, debt, KPIs, country performance, non-IFRS reconciliations and FX rates (chunks 28-43); press release (chunks 43-45) | The "Financial & Operational Data Excel file" that the release says accompanies it (chunk 33) is not supplied |

## Findings

### Source-set summary

The set is one audited annual report (20-F for FY2025) and three furnished 6-K packages (Q1, H1 and 9M 2026), each combining IFRS interim statements with an earnings release. No presentation deck, indenture, credit agreement, rating report, covenant compliance certificate or workbook is supplied. The latest source (6-K dated November 5, 2026) is dated on the as-of date; nothing later is used.

Evidence to risk mechanism to consequence: the filed statements give consolidated debt, cash, leverage, cash flow and quarterly Adjusted EBITDA for five quarter-ends, so CP-1 can build period tables. The perimeter changed sharply in 2026, so every period comparison needs the perimeter caveats below. Facility-level and covenant terms stop at December 31, 2025, so any statement about current covenant headroom cannot be sourced and must stay a gap.

### Source-by-source assessment

- 20-F FY2025: filed annual report; controls audited year-end 2025 and 2024 facts. Issuer is the Luxembourg parent "MIC S.A." (chunk 91). Its debt note lists every bond by country and issuer (chunk 245-246) and every bank and DFI facility group (chunk 252). Total debt and financing is 6,886 at December 31, 2025 (chunk 245, chunk 110). The 20-F states "At December 31, 2025, there were no breaches of financial covenants and we do not anticipate any such breaches in the next twelve months" (chunk 258) but gives no covenant thresholds, ratios or headroom (chunk 116, chunk 258).
- 6-K Q1: interim statements dated May 12, 2026 re-present 2025 comparatives for discontinued operations. Gross debt 8,624 and net debt 7,609 at March 31, 2026 appear in the release table (chunk 25 per the table row "Gross Debt 8,624 6,886 6,260 5,912 5,772"). Not reviewed by the auditor (no report in the file).
- 6-K Q2: carries a KPMG Audit S.à r.l. review conclusion on the June 30, 2026 interim statements (chunk 8). Gross debt 8,742, net debt 8,075, leverage 2.73x (chunk 35-36). Prior-year income-statement columns are labeled "Not reviewed" (chunk 8).
- 6-K Q3: latest period. Gross debt 8,648, cash 848, derivatives and vendor financing 183, net debt 7,983, leverage 2.53x at September 30, 2026 (chunk 32). Maturity ladder: one year 872, one to two years 986, two to three 1,947, three to four 1,601, four to five 1,147, after five 2,094, total 8,648 (chunk 25). Financial obligations note lists the quarter's issuances and repayments by country but not a facility-level balance table (chunks 23-25). No review report is in the file; statements are described as unaudited.

### Entity, perimeter and role map

- Issuer and parent: Millicom International Cellular S.A. ("MIC S.A.", Luxembourg). Borrower of the corporate notes and the revolving credit facility. Guarantor of selected subsidiary facilities (parent guaranty for the Uruguay Santander loan, chunk 256-257; for the El Salvador IDB Invest loan, chunk 124; guarantees of $629 million at December 31, 2025, chunk 258).
- Operating-level borrowers: Comunicaciones Celulares S.A. (Guatemala; $900 million 5.125% notes due 2032 issued through a trust with Guatemalan subsidiary guarantors, chunk 126), Telecomunicaciones Digitales, S.A. (Panama; 4.500% notes due 2030), Telefónica Celular del Paraguay S.A.E. (Paraguay; 5.875% notes due 2027, redeemed April 29, 2026 per chunk 25 of the Q3 6-K), UNE EPM Telecomunicaciones (Colombia bonds), Colombia Telecomunicaciones S.A. E.S.P. ("Coltel", acquired February 6, 2026; Q3 6-K chunk 9), and others. At December 31, 2025, 65 percent ($4,470 million) of debt was at operating level and generally non-recourse to MIC S.A. (chunk 114); the Q3 release states roughly 70 percent operating-entity and 30 percent corporate (chunk 32).
- Equity-accounted entities, not consolidated: Honduras joint venture (MIC S.A. holds 66.67 percent but joint control applies, chunk 92) and the Chile associate (49 percent through Celtel Chile, S.L., Q3 6-K chunk 11). Segment tables present both at 100 percent and eliminate them to reach group totals (Q3 6-K chunk 17).
- No restricted or unrestricted group definitions, guarantor groups or obligor perimeters for covenant tests are supplied; indentures are listed as exhibits in the 20-F (chunks 125-127) but are not in the source set.

### Period and basis relationships (versions kept separate)

- The 20-F balance sheet at December 31, 2025 is the original audited version. The Q3 6-K restates the December 31, 2025 comparatives for final Uruguay and updated Ecuador purchase accounting (chunk 4 footnote and chunk 12 table). Both versions stay active; the 20-F controls the audited figure and the Q3 6-K controls the restated comparative.
- 2025 income-statement comparatives in all three 6-Ks are re-presented to move Tigo Paraguay's mobile finance business to discontinued operations (Q3 6-K chunks 1, 12, 15); the 20-F FY2025 statements are not re-presented. Cash flow and balance sheet items are not re-presented (Q3 6-K chunk 41 footnote 5).
- Quarter versus year-to-date: the Q3 income statement gives both three-month and nine-month columns (chunk 1). The earnings release gives Adjusted EBITDA for Q3 2026, Q2 2026, Q1 2026, Q4 2025 and Q3 2025 (chunk 41), which supports discrete quarters. The Q4 2025 discrete cash flow, capex and tax are not given as a quarter in the 6-Ks.
- Perimeter: Coltel is consolidated from February 6, 2026, Tigo Uruguay and Tigo Ecuador from October 2025 (Q3 6-K chunks 1-2), so year-on-year growth is largely inorganic (the release gives organic growth of 4.8 percent revenue and 7.7 percent Adjusted EBITDA for Q3, chunk 41). Pro forma Coltel for 9M is stated only as incremental revenue $132 million and incremental net loss $34 million (chunk 10).
- Non-IFRS: Adjusted EBITDA, net debt, leverage, capex, OCF and equity free cash flow are management measures defined in the release (chunk 40) and reconciled in part (chunks 41-43). The statement definition of Adjusted EBITDA (note 5 footnote ii, chunk 18) and the release definition (chunk 40) are worded differently, and the leverage ratio is net debt over LTM Adjusted EBITDA after lease depreciation and lease interest, pro forma for acquisitions (chunk 40), so it is not a covenant ratio.
- Management claims (for example the guidance of equity free cash flow around $1.1 billion and year-end leverage below 2.5x, chunk 29) are attributed supporting claims and do not override the statements.

### Evidence available for the HTML-model demand

The set supports source-sufficiency review for these model inputs. This is source sufficiency only; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

| Model input | Where located | Status |
| --- | --- | --- |
| Discrete quarters and fiscal years | Q3 6-K chunks 1, 41; 20-F audited statements (financial statements follow the auditor reports at chunks 193-194); Q2 6-K chunk 8 | Located for Q3 2026, Q2 2026 (via H1), Q1 2026 and FY2025; Q4 2025 and Q2 2025 discrete lines are not separately supplied as statements |
| Quarter versus YTD distinction | Q3 6-K chunk 1 (three- and nine-month columns); release tables chunks 28, 31, 34 | Located |
| Segments and Adjusted EBITDA by country | Q3 6-K chunks 17-19 (9M and 9M 2025 segment tables) and chunks 34-36 (Q3 country commentary) | Located for 9M and Q3 country commentary; Q3 discrete segment tables are not in the statements |
| Add-backs and one-offs | Q3 6-K chunk 41 reconciliation and one-off summary ("Total (31) (149)") | Located for Q3 and 9M 2026 only |
| KPIs | Q3 6-K chunk 33 (five-quarter KPI table) | Located; ARPU excludes Coltel |
| Facility-level debt and carrying values | 20-F chunks 245-246 and 252 at December 31, 2025 only | Not supplied after December 31, 2025; Q3 gives only maturity buckets, currency and fixed-rate shares, and movements |
| Cash-paid interest and tax | Q3 6-K chunk 4 (interest paid on leases 216, on debt and other financing 463, taxes paid 306 for 9M 2026) | Located for 9M; quarterly split only in the release reconciliation (chunk 42, Q3 finance charges paid 254) |
| Business and transaction narrative | 20-F business, history and Lati chunks 91; Q3 6-K notes 3, 4, 11, 12 (chunks 8-16) | Located |

### Consumer assessments

| Consumer | Status | Basis and carried limitations |
| --- | --- | --- |
| CP-1 (financials and credit metrics) | READY_WITH_LIMITATIONS | Statements, debt maturity ladder, net debt and leverage series, EFCF and quarterly Adjusted EBITDA are located for five quarter-ends. Limitations: no facility-level debt table after December 31, 2025; no covenant thresholds or headroom; Q1 and Q3 statements are unreviewed; perimeter and re-presentation breaks listed above; Dec 31, 2025 restated; Coltel and Ecuador purchase accounting provisional. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | 20-F business and organizational structure plus 6-K notes on Coltel, Tigo Colombia (EPM minority buyout), Chile, Uruguay, Ecuador, Lati and Paraguay MFS disposal. Limitations: no indentures or credit agreements; ownership detail beyond the 20-F (Atlas is described as the largest shareholder, chunk 150) was not traced in this module; legal_documents context is "none". |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Consumes only upstream registers. Its source-side limits are those of CP-1 and CP-1A. A missing upstream handoff is not a source condition. |
| CP-5 (evidence trace validator) | READY_WITH_LIMITATIONS | Needs the pinned pack and upstream claims to trace. Limitations as above; quote matching is mechanical and does not test fidelity of table extraction. |

No consumer is CONDITIONAL or BLOCKED: no identity boundary is unresolved and no source has blocked preparation.

## Calculations

None. The method forbids normalization, reconciliation and calculation in CP-0. Figures above are quoted as stated in the sources with their locators. No unit conversion or arithmetic was performed, and nothing was assumed to be zero.

## Gaps

### Gap and conflict register

| Id | Severity | Gap or conflict | Locators | Affected consumers | Remediation |
| --- | --- | --- | --- | --- | --- |
| G1 | High | Covenant terms are not supplied. The 20-F says facilities carry net leverage, debt service coverage and debt-to-earnings covenants and that there were no breaches at December 31, 2025, with no thresholds, definitions, test dates or headroom. No 6-K updates the statement for 2026. | 20-F chunks 116, 258; 6-K chunks searched, none | CP-1, CP-2, CP-5 | Obtain the revolving credit agreement (20-F Exhibit 4.2 to 4.4 and 4.16), the El Salvador and Nicaragua credit and guaranty agreement (Exhibit 4.12), the indentures and any compliance certificates. Until then write "Not supplied". |
| G2 | High | No facility-level or instrument-level debt table after December 31, 2025. Q3 gives maturity buckets (total 8,648), a currency and fixed-rate split and period movements only. The remaining bond and loan balances at September 30, 2026 cannot be listed. | Q3 6-K chunks 25, 32; 20-F chunks 245-246, 252 | CP-1, CP-2 | Obtain the Financial and Operational Data Excel file named in the release or a debt schedule; otherwise treat December 31, 2025 instrument detail as dated and roll forward only the movements the notes state. |
| G3 | High | Current availability and maturity of the MIC S.A. $600 million revolving credit facility at September 30, 2026 is not stated in any 6-K. The 20-F says the full $600 million was extended to October 15, 2027 and was undrawn at December 31, 2025. The 20-F is internally worded two ways: note C.3.2 says maturity of $565 million was extended (chunk 255) while Material Contracts adds a joinder extending the full amount (chunk 124). | 20-F chunks 124, 255, 272 | CP-1, CP-2 | Treat the Material Contracts description as the later statement; confirm the drawn amount and any 2026 amendment in a source. A maturity within about twelve months of the as-of date is a liquidity item for the downstream modules. |
| G4 | Medium | Near-term maturities and refinancing: current debt of 872 and a one-to-two-year bucket of 986 at September 30, 2026. The 2027 SEK floating-rate bond (SEK 2.2 billion, swapped) matures in January 2027 (Q3 6-K chunk 25; 20-F chunk 247) and the El Salvador and Nicaragua $225 million facility is described as maturing September 12, 2027 (20-F chunk 124). Which instruments make up each bucket is not given. | Q3 6-K chunk 25; 20-F chunks 124, 247 | CP-1 | Obtain a bucket-by-instrument schedule. |
| G5 | Medium | Interim statements for Q1 and Q3 2026 carry no auditor review report; only the H1 package does, and its 2025 comparative income-statement columns are marked "Not reviewed". | Q2 6-K chunk 8; Q1 and Q3 files searched, none | CP-1, CP-5 | Label Q1 and Q3 figures as unaudited and unreviewed; do not describe them as reviewed. |
| G6 | Medium | Comparatives are not like-for-like. Dec 31, 2025 balance sheet is restated in the Q3 6-K (for example lease liabilities 2,273 non-current and 290 current, against 2,293 and 293 in the 20-F, Q3 chunks 3, 12; 20-F chunk 258). The 2025 income statement is re-presented for discontinued operations in the 6-Ks but not in the 20-F. | Q3 6-K chunks 3, 12; 20-F chunk 258 | CP-1, CP-5 | Keep both versions labeled by source; do not mix a 20-F income-statement figure with a re-presented 6-K comparative in one ratio without stating the basis. |
| G7 | Medium | Provisional accounting. Coltel purchase price allocation is provisional, with a measurement period that "will not exceed 12 months from the acquisition date" (chunk 9), and updated since the June package. Ecuador's measurement period ended October 30, 2026 and the accounting was still being finalized at issuance. | Q3 6-K chunks 9, 10, 14 | CP-1, CP-1A | Treat goodwill, intangibles and lease balances for these units as provisional. |
| G8 | Medium | Perimeter break. 9M and Q3 2026 include Coltel (from February 6, 2026), Uruguay and Ecuador (from October 2025); 2025 columns do not. Organic growth is management's calculation. Only incremental revenue and net loss for the pre-acquisition Coltel period are given, not pro forma Adjusted EBITDA or cash flow. Leverage is stated by management pro forma for acquisitions but the pro forma EBITDA bridge is not supplied. | Q3 6-K chunks 10, 40, 41 | CP-1, CP-2 | Do not compute LTM pro forma EBITDA from the supplied tables as if it were management's leverage denominator; request the Excel data file or a bridge. |
| G9 | Medium | Conflicting or unreconciled figures: (a) 9M 2026 net cash provided by operating activities is 2,028 in the cash flow statement (Q3 chunk 4) and 2,019 in the equity free cash flow reconciliation (chunk 42), with no stated bridge; (b) Dec 31, 2025 total debt is 6,886 in the 20-F, Q2 6-K and release tables but 6,887 in the Q3 6-K maturity table and fair value table (chunks 25, 26) (rounding is possible, not stated); (c) mobile customers at Q3 2026 are 55,845 thousand in the KPI table (chunk 33) but 47,510 thousand in the ARPU reconciliation, which excludes Coltel (chunk 41); (d) Adjusted EBITDA totals differ between segment tables at 100 percent of Honduras and Chile (3,485) and group totals (2,958) because of eliminations (chunk 17). | Q3 6-K chunks 4, 17, 25, 26, 33, 41, 42 | CP-1, CP-5 | Carry each figure with its locator and basis; CP-5 should not treat items (a) and (b) as agreed values. |
| G10 | Medium | Subsequent events within the window: Coltel loan with BTG Pactual for COP 40,000 million and a $12.5 million prepayment of the Santander loan on October 15, 2026; an October 2026 incentive plan of about $50 million contingent on $2 billion annual equity free cash flow; Ecuador finalization in October 2026; Paraguay MFS regulatory approval in October 2026. Tigo Guatemala settlement: $99 million expense, $68 million outstanding and payable over seven years (note 13). | Q3 6-K chunks 12, 14, 26, 28 | CP-1, CP-1A | Present as subsequent or post-period items; the dollar value of the Guatemala payable schedule beyond the stated amounts is not supplied. |
| G11 | Medium | Ratings are not supplied in the run context. The only rating evidence is in the 20-F: Moody's Ba2 (stable outlook affirmed October 21, 2025) and Fitch BB+ at December 31, 2025. No source states the position at the as-of date. | 20-F chunk 273 | CP-1A, CP-2 | Obtain current agency actions; otherwise state the dated rating and mark it stale. |
| G12 | Low | The earnings releases refer to a Financial and Operational Data Excel file, an investor presentation and a video conference; none is supplied. No presentation or workbook content is claimed, and none of the PDF or HTML layout, images or charts was inspected. | Q3 6-K chunks 33, 36, 45 | CP-1, CP-1A | Treat as unsupplied. |
| G13 | Low | Embedded "Visible text of ... sha256" lines at the head of each converted file (for example chunk 1 of the Q3 file) differ from the pack sha256 of the converted file. The pack hash identifies the jsonl evidence file used here; the embedded hash identifies the original text before conversion and was not independently checked. | chunk 1 of each source | CP-5 | Cite by pack sha256 and chunk number. |
| G14 | Low | Source description of the Q1 6-K: its interim statements are dated May 12, 2026 and the 6-K was furnished in May 2026; the filing date itself is not stated in the converted text beyond the document date. | Q1 6-K chunk 1 | CP-5 | Use the document date shown in the text. |
| G15 | Low | Legal and document-class gaps: no executed legal documents (indentures, credit agreements, guaranty agreements, intercreditor terms) are supplied, so no base, amendment, waiver or supplement chain can be built. Bond-level security, ranking and guarantor lists beyond the 20-F narrative are not supplied. Pledged assets: the 20-F says there were no pledged deposits for these debts at December 31, 2025 (chunk 258). | 20-F chunks 123-127, 258 | CP-1, CP-1A | Obtain exhibits if a legal analysis is required. |

### Duplicates and exclusions

The four issuer files are distinct documents and none is a duplicate of another. The Q2 6-K and the Q3 6-K overlap in content (cumulative periods) but are separate active sources; neither supersedes the other for its own period. The Q3 6-K press release (Item 3) repeats the earnings release highlights (chunks 43-44). The retained source for the Q3 headline numbers is Item 2 of the Q3 6-K. The cross-reference guide, forward-looking statement and signature pages are administrative and carry no analytical content. No source is excluded for blocked preparation.

### Limitations of this review

Extraction status is separate from fidelity. Table rows were read as flattened text; column alignment in multi-column tables (for example segment tables, chunk 17) was confirmed only where the row labels and totals read consistently. No figure was recomputed.

## Next module

Proceed to CP-1 (financials and credit metrics), then CP-1A, CP-2 and CP-5 in the dependency order CP-OS sets. The next evidence actions that would most improve readiness are the revolving credit agreement and its amendments, a September 30, 2026 debt schedule by instrument, covenant definitions and compliance certificates, current rating actions, and the accompanying Excel data file. None of these is needed for CP-1 to start; CP-1 should record each as Not supplied where a metric depends on it.
