# CP-0 — Source readiness: Element Solutions Inc (esi)

## Request

- Issuer: Element Solutions Inc (issuer id `esi`, NYSE: ESI), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026; prior period FY2025 (context).
- Run: `esi-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host searched and opened the pinned page files and wrote this answer. No provider was called.
- Question: can the supplied public filings and earnings releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion is given; no figure is normalized, reconciled or calculated here.
- Scope of reading: the sources are page-chunked text (`page:N`); locators below are those chunks, not printed page numbers. This module opened the cover, statements, debt, liquidity, covenant, segment, transaction and subsequent-event pages of each source. Pages it did not open (for example most risk-factor, tax, pension and environmental pages of the annual report) are retained evidence that this module did not assess, not excluded evidence.

## Sources

| Source (exact name) | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_esi-20251231.htm.jsonl | e419be4a34b86cf3946781c81c9cf5167d1ce55ea947acb2e97a22e3ec33fbdc | Annual report on Form 10-K for the year ended December 31, 2025 (127 pages); locator tag K25 |
| 10-Q_2026-03-31_esi-20260331.htm.jsonl | 71ffb0652af7e069b88fd66093decc7d627d9409b00bd185ac2a68db72c238da | Quarterly report on Form 10-Q for the quarter ended March 31, 2026 (40 pages); tag Q1-26 |
| 10-Q_2026-06-30_esi-20260630.htm.jsonl | 9e356702c38010063835ed61e96bcc033abb0f0a3a4b5a9a1845d764f0bcd2b7 | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 (53 pages); tag Q2-26 |
| 10-Q_2026-09-30_esi-20260930.htm.jsonl | 1efce58ae7d1707b81e096f97ecf01dbf0104d1e81a25b95db794dfd861b04fe | Quarterly report on Form 10-Q for the quarter ended September 30, 2026 (50 pages); tag Q3-26 |
| EX-99.1_2026-04-28_aearningsreleaseex99120263.htm.jsonl | cb75b2ab3988a8e0ad3f68546b2df2a55172fd4900de7f7f14ec3436aa37dbbf | Exhibit 99.1 earnings release dated April 28, 2026 (16 pages); tag R1 |
| EX-99.1_2026-07-27_aearningsreleaseex99120266.htm.jsonl | c0a4eea4343eb189f65a5cb896e49cd67b1e5c372bfce79bfb18a89241f92f7e | Exhibit 99.1 earnings release dated July 27, 2026 (19 pages); tag R2 |
| EX-99.1_2026-10-21_aearningsreleaseex99120269.htm.jsonl | b36d51c2a20c56990c8361f520b238bac0611bf5a7dab66ba03c7922169d0001 | Exhibit 99.1 earnings release dated October 21, 2026 (18 pages); tag R3 |
| context | 1920ec84f7b9710e00bbaac803890d2695813e40c10637e35f2e7d8eaaf0285a | User run settings; not issuer evidence |

Supplied handoffs: none (CP-0 is the first module, so no upstream handoff exists). The pack also holds `_retrieval.json`, which the launcher ignores; it is not evidence.

Citation format: (tag pN: "exact substring") names the source tag and the page chunk, then a substring that appears on that page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents cover the annual report, three quarterly reports and three earnings releases through the third quarter of 2026. They support the four downstream analyses, with bounded limitations. | Medium | Credit agreement, indenture, merger and termination agreements are not supplied, so covenant definitions and termination terms cannot be checked. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Financial statements, debt note, liquidity and segment data are located for the annual period and each 2026 quarter. | Debt, liquidity and earnings analysis can start from filed figures. | High |
| The planned Solstice merger was signed and then terminated in the third quarter; the termination agreement is not supplied. | Any cost or fee from the termination cannot be confirmed from the supplied text. | Medium |
| The only maintenance-style covenant located is a springing first lien net leverage test; its definitions are not supplied. | Covenant headroom cannot be verified against the agreement definitions. | Medium |
| Nothing after the October 22, 2026 quarterly filing is supplied. | Events between that date and the as-of date are unknown rather than absent. | Medium |

### Readiness view

The effective source set is sufficient to start all four requested analyses, and each is READY_WITH_LIMITATIONS rather than READY. The limitations are missing governing documents and a gap after the last filing, not missing financial statements. Filed statements and notes control their respective facts; the earnings releases are attributed management presentations and are used only for what the filings do not print. None of the sources has blocked preparation, and none is a duplicate of another. This is source sufficiency only; it does not evaluate the downstream model input contract, and it does not state whether any downstream analysis is complete.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 with FY2024 and FY2023 comparatives, and unaudited Q1, Q2 and Q3 2026 statements with comparatives, are located. Discrete Q3 2026 cash flows are only in the Q3 release; the Q3 10-Q prints nine months. Text extraction flattens tables. |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, the 2026 acquisitions, the Solstice transaction and its termination, related-party and management-change disclosures are located. The Merger Agreement, Termination Agreement and any proxy or Form S-4 are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Debt note, covenant text, liquidity and availability are located in the 10-K and each 10-Q. The Credit Agreement and indenture are not supplied, so covenant definitions and guarantor terms rest on the notes' summaries. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable page chunks, so claims can be traced. The filed HTML, XBRL and any slide decks are not supplied, so visual and table-layout checks are not possible. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Information-availability boundary

- The latest supplied document is the Q3 2026 10-Q, signed on October 22, 2026 (Q3-26 p50: "October 22, 2026"). The Q3 release is dated October 21, 2026 (R3 p2: "October 21, 2026").
- Nothing dated between October 22, 2026 and the as-of date 2026-11-05 is supplied. Events in that window are Not supplied, not absent.
- No source is dated after the cutoff. Forward-looking dates inside the filings, such as the 3.875% USD Notes due 2028 maturity of September 1, 2028 (Q3-26 p18: "will mature on September 1, 2028"), are contract terms, not events.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_esi-20251231.htm.jsonl`, tag K25)

- Family and authority: filed annual report; original authority for audited consolidated statements and notes. Cover (K25 p1: "For the fiscal year ended December 31, 2025"); signed February 18, 2026 (K25 p78: "Date: February 18, 2026").
- Audit: the auditor's report is on page 79 (K25 p79: "We have audited the accompanying consolidated balance sheets of Element Solutions Inc and its subsidiaries").
- Statements: operations (K25 p82: "CONSOLIDATED STATEMENTS OF OPERATIONS (dollars in millions, except per share amounts)"), balance sheet (K25 p83: "CONSOLIDATED BALANCE SHEETS (dollars in millions)") and cash flows (K25 p84: "CONSOLIDATED STATEMENTS OF CASH FLOWS (dollars in millions)").
- Debt: Note 12 with the principal-payment schedule (K25 p112: "Minimum future principal payments on long-term debt were as follows"); covenant sentence (K25 p113: "first lien net leverage ratio should not exceed 5.0 to 1.0, subject to a right to cure").
- Segments and subsequent events: Note 22 (K25 p124: "22. SEGMENT INFORMATION") and Note 23 (K25 p126: "23. SUBSEQUENT EVENTS"). Leases: operating leases only (K25 p120: "The Company primarily has operating lease agreements").
- MD&A liquidity discussion starts on page 66 (K25 p66: "Liquidity and Capital Resources").
- Perimeter and units: consolidated Element Solutions Inc and subsidiaries; USD millions.

#### Form 10-Q for the quarter ended March 31, 2026 (`10-Q_2026-03-31_esi-20260331.htm.jsonl`, tag Q1-26)

- Family and authority: filed quarterly report, unaudited. Cover (Q1-26 p1: "For the quarterly period ended March 31, 2026"); signed April 29, 2026 (Q1-26 p40: "April 29, 2026").
- Statements: operations (Q1-26 p4), balance sheet (Q1-26 p5), cash flows (Q1-26 p6), each titled "CONDENSED CONSOLIDATED" (Q1-26 p4: "CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS").
- Debt note (Q1-26 p12: "6. DEBT"), covenant (Q1-26 p14: "first lien net leverage ratio should not exceed 5.0 to 1.0"), segment note and Adjusted EBITDA reconciliation (Q1-26 p23: "The following table reconciles"), liquidity (Q1-26 p35: "Liquidity and Capital Resources").

#### Form 10-Q for the quarter ended June 30, 2026 (`10-Q_2026-06-30_esi-20260630.htm.jsonl`, tag Q2-26)

- Family and authority: filed quarterly report, unaudited. Cover (Q2-26 p1: "For the quarterly period ended June 30, 2026"); signed July 28, 2026 (Q2-26 p53: "July 28, 2026").
- Statements: operations (Q2-26 p5), balance sheet (Q2-26 p6), cash flows (Q2-26 p7) (Q2-26 p5: "CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS").
- Pending Solstice transaction as it stood on filing: terms (Q2-26 p12: "0.5 shares of Solstice common stock"), a termination-fee risk (Q2-26 p50: "a termination fee of $376,000,000"), debt note (Q2-26 p16: "6. DEBT"), liquidity (Q2-26 p44: "Liquidity and Capital Resources").
- Version relationship: this 10-Q describes the merger as pending; the Q3 10-Q supersedes it for the merger's status.

#### Form 10-Q for the quarter ended September 30, 2026 (`10-Q_2026-09-30_esi-20260930.htm.jsonl`, tag Q3-26)

- Family and authority: filed quarterly report, unaudited; the latest filed financial statements in the pack. Cover (Q3-26 p1: "For the quarterly period ended September 30, 2026").
- Statements: three- and nine-month operations (Q3-26 p5: "CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS"), balance sheet (Q3-26 p6) and nine-month cash flows (Q3-26 p7: "CONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS").
- Debt note (Q3-26 p15: "Total debt 2,082.1 1,625.9"), springing covenant (Q3-26 p17: "first lien net leverage ratio should not exceed 5.0 to 1.0"), compliance and revolver capacity (Q3-26 p18: "unused borrowing capacity of $478 million, net of letters of credit").
- Segments and Adjusted EBITDA reconciliation (Q3-26 p26: "13. SEGMENT INFORMATION"; Q3-26 p27: "Adjusted EBITDA $ 191.0 $ 146.9 $ 536.8 $ 411.3").
- Transaction status: the merger was terminated (Q3-26 p3: "On August 27, 2026 the parties mutually agreed to terminate the Agreement and Plan of Merger").
- Liquidity and capital resources (Q3-26 p44: "Liquidity and Capital Resources"); the first significant maturity (Q3-26 p44: "approximately $800 million is related to the maturity of our 3.875% USD Notes due 2028").
- Subsequent management change (Q3-26 p49: "Effective October 19, 2026").

#### Earnings releases (Exhibit 99.1; tags R1, R2, R3)

- Family and authority: issuer press releases furnished as Exhibit 99.1; management-prepared and unaudited; attributed supporting claims. R1 is dated April 28, 2026 (R1 p2: "April 28, 2026"), R2 July 27, 2026 (R2 p1: "July 27, 2026"), R3 October 21, 2026.
- They add what the 10-Qs do not print: a capital-structure table with net debt (R3 p9: "Net Debt $ 1,869.8"; R2 p10: "Net Debt $ 1,943.4"; R1 p9: "Net Debt $ 1,993.9"), selected financial data including interest paid and income taxes paid (R3 p9: "Interest paid 31.1 24.9 76.2 59.1"), discrete-quarter cash flow and free cash flow (R3 p2: "free cash flow of $135 million") and 2026 guidance (R3 p2: "approximately $720 million").
- Version relationship: each release repeats statement figures that the following 10-Q also prints. The 10-Q controls statement facts; a release figure is management presentation. Net debt and free cash flow are issuer non-GAAP measures.

### Identity and perimeter

- Reporting entity: Element Solutions Inc, a Delaware corporation (Q3-26 p1: "Element Solutions Inc (Exact name of Registrant as specified in its charter)"). The statements are consolidated for the company and its subsidiaries, with non-controlling interests shown separately (Q3-26 p6: "Net income attributable to non-controlling interests").
- Borrowers and guarantors under the senior secured Credit Agreement are the company and MacDermid, Incorporated, guaranteed by certain domestic subsidiaries (Q3-26 p16: "among, inter alia, Element Solutions and MacDermid, Incorporated, as borrowers"; Q3-26 p16: "guaranteed, jointly and severally, by certain of their domestic subsidiaries"). The senior notes are guaranteed on a senior unsecured basis by generally the same subsidiaries (Q3-26 p18: "fully and unconditionally guaranteed on a senior unsecured basis"). The context leaves borrower, parent and guarantor fields blank; that is not evidence they do not exist, and the guarantor list itself is not supplied.
- Related party: the Advisory Services Agreement with Mariposa Capital, LLC (Q3-26 p26: "Mariposa Capital, LLC, an affiliate of one of its founder directors").
- Other parties: the terminated counterparty is Solstice Advanced Materials Inc.; the acquired businesses are EFC Gases & Advanced Materials and Micromax (US) Holdings LLC (Q3-26 p2: "Micromax (US) Holdings LLC").
- Currency and units: USD; statements are in millions except per-share data. About 77% of nine-month 2026 net sales are from non-U.S. operations (Q3-26 p44: "approximately 77% of our net sales were generated from non-U.S. operations"), and the term loans are swapped into euro-denominated exposure (Q3-26 p20: "into fixed-rate euro-denominated debt"). Reporting currency is USD in every source; no other reporting currency is used.

### Conflicts and basis differences (with locators)

| Item | Source A | Source B | Downstream effect |
| --- | --- | --- | --- |
| EFC purchase price | K25 p126: "for a purchase price of approximately $369 million" | Q3-26 p12: "for a purchase price of approximately $367 million" | The 10-K figure is a subsequent-event estimate; the Q3 10-Q is later and prints the allocation table. CP-1A and CP-2 should use the Q3 10-Q and say so. |
| Micromax purchase price | K25 p126: "for a purchase price of approximately $500 million" | Q3-26 p12: "for a purchase price of approximately $494 million" | Same treatment: the later filing controls. |
| Debt measure | Q3-26 p15: "Total debt 2,082.1 1,625.9" (carrying value, net of discounts and costs) | R3 p9: "Total Debt 2,094.7" (issuer table) | The two are different bases (net carrying value against the release's debt table). CP-1 must state the basis it uses and reconcile in its own calculations. |
| Revolver capacity | Q3-26 p18: "unused borrowing capacity of $478 million, net of letters of credit" | Q3-26 p46: "totaled $506 million at September 30, 2026" | The first is the revolving credit facility alone; the second adds other lines of credit and overdraft facilities. CP-1 and CP-2 must not mix them. |

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, segment and non-GAAP tables, facility-level debt, cash-paid interest and tax | K25 p82 to p84, p112 to p113, p124; Q1-26 p4 to p6, p12, p23; Q2-26 p5 to p7, p16; Q3-26 p5 to p7, p15 to p16, p26 to p27; R3 p9 | Q3 2026 discrete cash flows only in the Q3 release; interim cash flows are year-to-date; FY2025 is the only audited period; prior-year interim amounts carry a reclassification note (Q3-26 p12: "Certain prior year amounts have been reclassified") |
| CP-1A | Business description, segments, history, acquisitions, transaction, ownership and management | K25 p6 (Item 1 Business starts here) and p124; Q3-26 p10 to p14, p26 to p31, p49; R3 p2 | Merger Agreement, Termination Agreement, proxy or Form S-4 not supplied; no investor presentation deck; ownership beyond the Mariposa disclosure not read |
| CP-2 | Debt note, maturities, covenant, liquidity, availability, hedges, claims outside debt | K25 p66 to p70, p112 to p113, p120 to p121; Q3-26 p15 to p21, p44 to p46 | Credit Agreement and indenture not supplied; covenant definitions and the compliance ratio are not printed; no ratings, prices or peer data |
| CP-5 | Traceable claims across the other three | All seven sources have page chunks | Filed HTML, XBRL and decks not supplied; image and chart content cannot be inspected |

### Analytical read-through

- Usable coverage: audited FY2025 statements and unaudited statements for each 2026 quarter let the downstream modules build a reported foundation and a last-twelve-months view from the year and the nine-month periods (nine months 2026 against nine months 2025), with discrete quarters available from the three-month columns.
- Strongest contrary evidence: 2026 is a year of structural change. Two acquisitions closed in the first quarter and the company borrowed to fund one of them (Q3-26 p12: "funded with the proceeds from the Add-on Term Loans of $450 million"), so FY2025 balances and ratios are not a base for the current structure. The Q3 purchase price allocations are preliminary (Q3-26 p14: "the purchase price allocation for each of the Acquisitions is preliminary"). A consumer that reads only the FY2025 balance sheet misses these.
- Source risk mechanism: the Solstice merger was signed in July and terminated in August with a mutual release (Q3-26 p12: "mutually released the parties from any claims of liability"). The Q2 10-Q disclosed a potential $376,000,000 termination fee in certain circumstances; the Q3 10-Q does not state whether any fee was owed or paid and the Termination Agreement is not supplied. Transaction-cost lines, such as the acquisition, integration and transaction expense row (Q3-26 p27: "Acquisition, integration and transaction expenses 21.9 11.0 52.6 22.6"), cannot be split between the acquisitions and the terminated merger from the supplied text.
- What cannot proceed: covenant headroom against the agreement's own definitions, guarantor-level or restricted-group analysis, any treatment of the termination terms beyond the filing's summary, and any view after October 22, 2026.
- Next evidence action: supply the Credit Agreement and the 3.875% USD Notes due 2028 indenture, the Form 8-K of August 27, 2026 with the Termination Agreement (listed as Exhibit 2.1 at Q3-26 p49), the Merger Agreement 8-K of July 6, 2026, and any later 8-K, then rerun source readiness.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. The differences in the conflicts table are shown as printed and are left for CP-1 to reconcile.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit Agreement and 3.875% USD Notes due 2028 indenture not supplied; covenant definitions, baskets and guarantor schedules rest on note summaries | High for covenant work; Medium for the rest | CP-2 | Supply the executed Credit Agreement, amendments and indenture |
| Termination Agreement and Merger Agreement not supplied; whether any termination fee or cost arose is not stated in the supplied text | Medium | CP-1A, CP-2 | Supply the August 27, 2026 and July 6, 2026 Form 8-Ks and exhibits |
| No filing or release between October 22, 2026 and 2026-11-05 supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| Discrete Q3 2026 cash flow is only in the release; the 10-Q prints nine months | Low | CP-1 | Use the release as an attributed source and label it |
| Compliance ratio for the springing first lien net leverage test is not printed; the covenant applies only above 30% revolver utilization | Medium | CP-2 | Treat as Not calculable from the supplied text; request the compliance certificate if needed |
| No investor presentations in the pack; the releases stand in for them | Low | CP-1A, CP-5 | Supply the decks if segment commentary beyond the releases is needed |
| Text extraction only; filed HTML, XBRL and images not supplied; table layout may be flattened | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |
| No credit ratings, market prices (other than the release's September 30, 2026 closing price), peers or precedent data | Low for the selected modules | CP-2 | Not required for this scope; keep Not supplied |
| Pages not opened by this module (risk factors, tax, pension, environmental, most 10-K business pages) | Low | all | Downstream modules open the pages they need |

## Next module

- CP-1: treat the 10-K and 10-Qs as controlling for statement facts; label the releases' net debt, Adjusted EBITDA and free cash flow as issuer non-GAAP; keep three-month, nine-month and annual columns apart; state whether debt is carrying value or the release's debt table; carry the 2026 acquisitions and the preliminary purchase price allocation as a comparability limit.
- CP-1A: carry the Solstice merger as signed on July 6, 2026 and terminated on August 27, 2026, with the termination terms Not supplied; use the Q3 10-Q purchase prices for EFC and Micromax and note the 10-K estimates differ.
- CP-2: carry the missing Credit Agreement and indenture, the springing 5.0 to 1.0 first lien net leverage test with no printed ratio, the 2028 notes maturity and the revolver and other-lines availability difference as restrictions.
- CP-5: carry every limitation above; label anything after October 22, 2026 as Not supplied.
