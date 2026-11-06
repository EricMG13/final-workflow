# CP-0 — Source readiness: SERVICE CORP INTERNATIONAL (sci)

## Request

- Issuer: SERVICE CORP INTERNATIONAL (issuer id `sci`; the filings name the registrant "SERVICE CORPORATION INTERNATIONAL", NYSE ticker SCI), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `sci-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, current period Q3 2026, prior period FY2025, reporting currency USD (context). Requested modules: CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion. No figure is normalized, reconciled or calculated here.
- Context fields for borrower, parent, guarantors, ratings, quotes, deal terms, peers and research questions are blank. Blank is not evidence of absence and is not read as zero.

## Sources

Locators are `page:N` chunks of the pinned `.jsonl` text, not printed page numbers. Each file's first chunk also quotes the sha256 of the original `.htm` that it was extracted from; the table gives the sha256 of the pinned `.jsonl` file that CP-OS holds.

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_sci-20251231.htm.jsonl | 36f224c032003fbd2390907d9603b5b257c583b876df570b13d8b342fe4f5f00 | Form 10-K for the fiscal year ended December 31, 2025 (126 chunks; original `.htm` sha256 dff8ddd8970480036d878b11a30bc30268fe9b12b77230f1504b5a4ed7150371) |
| 10-Q_2026-03-31_sci-20260331.htm.jsonl | e6b5e437aefdd3d93a7df7ee4a72da856eb2c3e8d8864dff282c77ac49311d26 | Form 10-Q for the quarter ended March 31, 2026 (45 chunks; original `.htm` sha256 be9c45a7c6e680049e9a02ea52e7ecd1bae21fd2218bfe80ebfe9a482856834e) |
| 10-Q_2026-06-30_sci-20260630.htm.jsonl | 3f4554fa1a62f231e9dd455be55fe862d78b2b61391019d236799268dd70b592 | Form 10-Q for the quarter ended June 30, 2026 (52 chunks; original `.htm` sha256 ab083f26810899fbe63697aae82f5366a3398dbb698ffed09364a2626ca81417) |
| 10-Q_2026-09-30_sci-20260930.htm.jsonl | 236742c90fb88a0fc6e3b830a1a819da8579c8436891d794242d5625f7bae113 | Form 10-Q for the quarter ended September 30, 2026 (54 chunks; original `.htm` sha256 afb5e61d9de50f94df9c5955d1959b9b31ea918fae9295a055d39e4d63cc1b43) |
| EX-99.1_2026-04-29_exhibit991q126earningsrele.htm.jsonl | dc7d39675688d257986d7838f6da2271b0d5a328325d0081a47485a7f2412e53 | Exhibit 99.1 earnings release for Q1 2026, dated April 29, 2026 (14 chunks; original `.htm` sha256 8640a6aba254bcbd11199d69d61a42243a3741bacef0d0d5768da65b6f36e5d6) |
| EX-99.1_2026-07-29_exhibit991q226earningsrele.htm.jsonl | 8ffbca4fd985e89d67fcf44643913b74684aa9a27e65aeca772948faf99925ff | Exhibit 99.1 earnings release for Q2 2026, dated July 29, 2026 (17 chunks; original `.htm` sha256 f7433fb71e3b30d710070ffd838af4be58e69c2b50dffa7cebb371e64f7f6ed6) |
| EX-99.1_2026-10-28_exhibit991q326earningsrele.htm.jsonl | d5fe76c2497f82e8e53c22501a405cf8fb7df74cae0b9bd5b7f0b933f384c2b3 | Exhibit 99.1 earnings release for Q3 2026, dated October 28, 2026 (18 chunks; original `.htm` sha256 2dcdea37569b61d18387fa28c0b2cfe359b1d68d62fd8c0ed8b6d2bece93ec2c) |
| context | 65d65475c254be68b493ea4436b1695cdda5a813079114b87a550c9ce00dd797 | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module in this run, so there is no upstream handoff to list.

Ignored by the launcher: `_retrieval.json` (pack metadata, not issuer evidence). It records the filing dates and accession numbers that the host used only to confirm that no supplied document post-dates the cutoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and releases are enough to start all four downstream modules on the consolidated company, with stated limits. Filed statements control; releases are supporting claims. | Medium | Credit agreement, indentures, ratings and a covenant EBITDA definition are not supplied, so legal terms and covenant headroom cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Annual, quarterly and nine-month statements, debt tables and liquidity text are located for the current and prior periods. | Debt, liquidity and cash flow work can proceed on filed figures. | High |
| The only financial covenant described is a maximum leverage ratio, with a required level and reported actual, but no definition. | Headroom can be quoted as reported but not rebuilt or tested. | Medium |
| The annual maturity table appears to be on a different basis from its caption. | The maturity wall needs a basis label before use. | Medium |
| No ratings, executed debt documents, or guarantor detail for the senior notes are supplied. | Ranking, security and guarantee claims must stay as gaps. | Low |

### Readiness view

The effective source set can support the minimum module set for SERVICE CORP INTERNATIONAL with limitations. All seven issuer sources are filed SEC documents or furnished earnings releases of the single registrant, with text extracted from the original HTML. The audited FY2025 statements, three unaudited 2026 interim filings and three releases give a continuous record from December 31, 2025 to September 30, 2026. Nothing is blocked on identity. Each consumer is READY_WITH_LIMITATIONS. None is CONDITIONAL or BLOCKED. This is source sufficiency only; it does not say that downstream analysis is complete or that any model input contract is met.

### Information-availability boundary

- Every supplied document is dated on or before October 29, 2026, before the cutoff of 2026-11-05. The latest are the Q3 2026 release (Exhibit 99.1, "HOUSTON, Texas, October 28, 2026", `EX-99.1_2026-10-28…` page:2) and the Q3 2026 Form 10-Q, whose cover gives "The number of shares outstanding of the registrant’s common stock as of October 29, 2026 was 135,907,343" (`10-Q_2026-09-30…` page:1).
- Nothing dated between October 29, 2026 and the cutoff is supplied. Events in that window, for example new debt, acquisitions or rating actions, are Not supplied, not absent.
- The only post-balance-sheet event in the Q3 10-Q is a share repurchase: "Subsequent to September 30, 2026, we repurchased 232,968 shares for $18.2 million at an average cost per share of $78.21" (`10-Q_2026-09-30…` page:20). The 10-K likewise reports repurchases after December 31, 2025 (page:18, page:109).
- The Q3 10-Q text has no printed signature date in the extracted chunks (page:54 shows the signatory only). The date is taken from the cover and the release, not from a signature line.

### Identity and perimeter

- Reporting entity: Service Corporation International, a Texas corporation, "Commission file number 1-6402-1", listed on the New York Stock Exchange as SCI (`10-K_2025-12-31…` page:1; `10-Q_2026-09-30…` page:1). All statements are consolidated. The 10-Q defines the group as "companies owned directly or indirectly by Service Corporation International" (`10-Q_2026-09-30…` page:6).
- Units and currency: statements are in thousands of USD ("(In thousands, except per share amounts)", `10-Q_2026-09-30…` page:6). MD&A and the releases mix millions and thousands. No other currency is reported as a reporting currency. Canadian operations exist ("Due to cash balances residing in Canada", page:26), and a foreign currency translation line appears in comprehensive income (page:7). This matches the context currency USD.
- Debt perimeter: the bank credit agreement "is guaranteed by a majority of our domestic subsidiaries" (`10-Q_2026-09-30…` page:18; `10-K_2025-12-31…` page:102). Which subsidiaries guarantee, whether the senior notes carry guarantees, and the restricted or unrestricted split are not stated in the supplied text. The context leaves the guarantor list blank. This is an unresolved perimeter gap.
- Trust perimeter: merchandise, service and perpetual care trusts are consolidated and shown as "Deferred receipts held in trust" and "Care trusts’ corpus" (`10-Q_2026-09-30…` page:7); the notes say interests in the trusts "represent a liability to us" (page:12). Any consumer that reads total assets, liabilities or equity must separate trust balances from corporate balances.
- Auditor: PricewaterhouseCoopers LLP, Houston, "February 12, 2026", opinion on the financial statements and internal control, "We have served as the Company’s auditor since 1993" (`10-K_2025-12-31…` pages:68, 70). Interim statements are unaudited.

### Source register

#### Form 10-K for FY2025

- Family and authority: filed annual report, original authority for audited consolidated FY2025, FY2024 and FY2023 statements. Signed "Dated: February 12, 2026" (page:126).
- Located: statement of operations page:71, balance sheet page:72, cash flows pages:72 to 73, equity statement page:74, debt note pages:100 to 104 (debt components page:100, maturities page:101, bank credit agreement and activity pages:102 to 103, fair value pages:103 to 104), leases pages:105 to 107, commitments and contingencies pages:108 to 109, segments pages:115 to 116, liquidity and covenant table page:42, cash requirements pages:45 to 46, surety bonds page:46, business pages:7 to 18, risk factors pages:23 to 36.
- Period and basis: calendar years ended December 31, 2025, 2024 and 2023. Page:71 heads columns "2025 2024 2023".
- Limits: exhibits, including the credit agreement and indentures, are listed by reference only (pages:123 to 125); no exhibit text is supplied.

#### Forms 10-Q for Q1, Q2 and Q3 2026

- Family and authority: filed quarterly reports with unaudited condensed consolidated statements. Q1 signed "April 30, 2026", Q2 signed "July 30, 2026" (last chunks). Q3 shows no signature date in the text (see boundary above).
- Located in the Q3 10-Q: statement of operations page:6 (three and nine months ended September 30, 2026 and 2025), comprehensive income page:7, balance sheet page:7 (September 30, 2026 and December 31, 2025), cash flows pages:7 to 8 (nine months), equity pages:9 to 10, debt note pages:17 to 19, fair value pages:19 to 20, equity and repurchases page:20, segments pages:20 to 21, commitments and contingencies pages:22 to 23, liquidity and covenant table pages:25 to 26, financing activities and surety bonds pages:28 to 29, market risk page:51, Part II page:52.
- Located in the Q1 and Q2 10-Qs: statement of operations page:6, balance sheet page:7, cash flows page:7, debt note page:17, covenant table page:24, segments page:19.
- Period and basis: Q1 is three months; Q2 and Q3 carry both three-month and year-to-date columns. The cash flow statements are year-to-date, so a discrete quarter needs subtraction downstream. This module does not do it.

#### Earnings releases (Exhibit 99.1) for Q1, Q2 and Q3 2026

- Family and authority: issuer press releases furnished as Exhibit 99.1, unaudited and management-prepared. They give reported and "excluding special items" figures, guidance and comparable-location tables. Attributed claims only; the 10-Q controls where the two overlap.
- Located in the Q3 release: highlights and CEO comment page:2, key results table page:3, quarter narrative and outlook pages:4 to 6, balance sheet page:10, cash flows pages:10 to 11, comparable funeral results pages:12 to 15, comparable cemetery results page:16, non-GAAP reconciliation page:17, trust performance page:18. Q1 and Q2 releases have the matching tables (Q1: balance sheet page:8, operations page:9; Q2: balance sheet page:9, operations page:10).
- Non-GAAP: "Earnings excluding special items", "diluted earnings per share excluding special items" and "net cash provided by operating activities excluding special items" are the releases' own measures (page:4). No EBITDA, adjusted EBITDA or net debt measure appears in any supplied source; a search of all seven for "EBITDA" returned nothing.

### Document relationships and conflicts

- The releases repeat the 10-Q statement figures. For example the Q3 release states revenue "$ 1,107.3" and "$ 3,307.0" in millions (page:3), against 1,107,262 and 3,307,004 in thousands in the 10-Q (page:6). They agree after rounding. Treat the 10-Q as controlling and do not count the release as independent corroboration.
- Maturity-table basis conflict (10-K). The debt table lists components that sum to 5,177,893 thousand before "Unamortized debt issuance costs (38,076)" and shows "Total debt $ 5,139,817" after them (page:100). The maturity table is captioned "excluding unamortized premiums and debt issuance costs" yet totals "Total debt maturities $ 5,139,817" (page:101), the net figure. The MD&A also says the aggregate principal "excludes $38.1 million in unamortized non-cash debt issuance costs" (page:46). The two captions cannot both describe the same total. The effect falls on any consumer that builds a maturity wall or compares principal to carrying value. This note only records the conflict; the arithmetic is shown under Calculations.
- Liquidity text: the Q3 10-Q states "$1,513.7 million in borrowing capacity under the facility" and "we issued $1.3 million of letters of credit" (page:18). The 10-K states "$1,448.0 million" and "$47.0 million of letters of credit" at December 31, 2025 (page:102). Different dates, no conflict. The facility size ($1.75 billion revolving, $750.0 million term loan, "both due November 2030") is in the 10-K (page:102); the Q3 10-Q does not restate the revolver commitment.
- Covenant: the 10-K and each 10-Q give a "Per Credit Agreement 5.00 (Max)" level against an actual of 3.67 at December 31, 2025 (10-K page:42) and 3.69 at September 30, 2026 (Q3 10-Q page:25). The definition of the ratio is not in any supplied source.
- Terminology: the registrant refers to "Bank Credit Facility" (the revolver) and "Term Loan" separately, and to the combined "bank credit agreement". Consumers should keep them as separate instruments.

### Consumer evidence demand

| Consumer | Status | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Annual and interim statements, segments, debt, cash flow, non-GAAP | 10-K pages:71 to 74, 100 to 104, 115 to 116; Q3 10-Q pages:6 to 10, 17 to 22; releases pages:3 to 17 | No EBITDA in any source; discrete Q2 and Q3 cash flows need subtraction from year-to-date columns; maturity-table basis conflict; text extraction flattens tables |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, history, ownership, strategy, capital allocation | 10-K pages:7 to 18, 40 to 44; Q3 10-Q pages:24 to 29; Q3 release pages:2 to 6 | No proxy statement (Part III is incorporated by reference, 10-K page:2) and no transaction documents. A search of all seven sources for merger, acquired-company and tender-offer language found no pending merger or sale; ordinary-course business acquisitions appear in the cash flow statements |
| CP-2 | READY_WITH_LIMITATIONS | Debt stack, liquidity, covenant, interest, leases, trust and surety claims | 10-K pages:42, 45 to 46, 100 to 107; Q3 10-Q pages:18 to 20, 25, 28 to 29 | Credit agreement and indentures not supplied; covenant definition and guarantor detail not supplied; no ratings |
| CP-5 | READY_WITH_LIMITATIONS | Traceable claims across the filings | All seven sources carry page chunks; the filing facts above are locatable | Text only; no original HTML, XBRL or images are supplied for visual or table-layout checks |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Analytical read-through

- Usable coverage: the audited FY2025 statements, three 2026 interim 10-Qs and three releases support a reported-basis financial foundation for Q3 2026, nine months 2026, FY2025 and a last-twelve-months view built from FY2025 plus nine months 2026 less nine months 2025. All three components are located (10-K page:71; Q3 10-Q page:6).
- Strongest contrary evidence: the bank credit agreement carries the only financial covenant described, a maximum leverage ratio, and the supplied text gives no definition of that ratio. A downstream module that computes its own leverage would not match the reported 3.69 without that definition, and the source set cannot settle the difference. Separately, the remainder of the debt after the 79% fixed share ("Approximately 79% of our total debt had a fixed interest rate", Q3 10-Q page:18) is floating-rate, so that pricing exposure rests on the term loan and revolver, whose terms are not supplied.
- Source-risk mechanism: the maturity table and the debt table disagree on whether issuance costs are included. A reader who takes the maturity wall at face value could mix a net figure with gross principal. The 2027 bucket is the clearest case, because the 7.500% Senior Notes due April 2027 and the 4.625% Senior Notes due December 2027 both fall in it (10-K page:101, page:100).
- Perimeter risk: consolidated balances include trust assets and matching trust liabilities ("Deferred receipts held in trust", "Care trusts’ corpus"). Total assets of this size are not corporate liquidity.
- What cannot proceed: legal ranking, security, guarantor coverage and covenant testing on credit agreement definitions; any rating-based or market-price-based view, because no ratings, quotes or peers are supplied; anything after October 29, 2026.
- Next evidence action: supply the Bank Credit Agreement and its November 2025 amendment, the senior indentures and supplements, any rating reports, and filings dated after October 29, 2026 up to the cutoff. Until then carry each limitation above into the modules.

## Calculations

No new calculation is made for readiness. One arithmetic check supports the conflict recorded above and is not a normalized figure:

- Sum of the 10-K debt components before issuance costs, in thousands (10-K page:100): 136,924 + 550,000 + 750,000 + 850,000 + 800,000 + 800,000 + 750,000 + 255,000 + 54,766 + 151,061 + 80,142 = 5,177,893.
- Less unamortized debt issuance costs 38,076 = 5,139,817, which equals the printed "Total debt" (page:100) and the maturity-table total (page:101).
- Reading: the maturity-table total matches the net amount, not the 5,177,893 gross amount, despite its caption. Whether the individual annual buckets are net or gross is Not determinable from the text.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Bank credit agreement, amendment and ratio definition not supplied; no EBITDA in any source | High | CP-2 | Supply the executed credit agreement and the covenant compliance definition; keep reported 3.69 against 5.00 maximum as an attributed figure only |
| Senior note indentures and supplements not supplied; guarantor and security status of the notes not stated (only the 2032 notes are called "unsecured", 10-K page:102) | High | CP-2 | Supply the indentures and any guarantor schedule |
| Ratings, price quotes, peers and valuation inputs blank in context and absent from sources | Medium | CP-2 | Not required for source readiness; keep Not supplied |
| Maturity table basis conflicts with its caption (10-K pages:100 to 101) | Medium | CP-1, CP-2 | Label the basis in use; request the XBRL or HTML table to confirm |
| Events dated October 30, 2026 to the cutoff not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| Discrete Q2 and Q3 2026 cash flows are not printed; statements are year-to-date | Low | CP-1 | Derive downstream by subtraction and label the derivation |
| Text extraction only; original HTML, XBRL and images not supplied; page chunks are not printed page numbers | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |
| Exhibits (indentures, leases, plans) are listed by reference and not supplied; the 2026 proxy statement is incorporated by reference and not supplied | Low | CP-1A | Supply if governance or ownership detail is needed |
| Unclaimed property audits in about forty states have no estimable loss (Q3 10-Q page:22) | Medium | CP-2 | Carry as an unquantified contingency; request later disclosure |

## Next module

- CP-1: use the 10-K and 10-Q statements as controlling and the releases as attributed support. Keep thousands and millions apart. Keep annual, three-month and nine-month columns separate. Label "excluding special items" figures as issuer non-GAAP. Do not state EBITDA from these sources. Record the maturity-table basis conflict wherever a maturity wall is shown.
- CP-1A: describe the business from the 10-K and Q3 10-Q and attribute the releases. A search found no pending transaction; label anything after October 29, 2026 as Not supplied.
- CP-2: list every instrument from the debt tables (7.500% notes due April 2027, 4.625% due December 2027, 5.125% due June 2029, 3.375% due August 2030, 4.000% due May 2031, 5.750% due October 2032, the term loan, the revolver, the corporate headquarters facility due February 2037, finance leases, mortgage notes and other debt). Carry the missing indentures, credit agreement and covenant definition as restrictions.
- CP-5: all claims can be traced to page chunks. Keep the extraction-only and covenant-definition limits visible.
