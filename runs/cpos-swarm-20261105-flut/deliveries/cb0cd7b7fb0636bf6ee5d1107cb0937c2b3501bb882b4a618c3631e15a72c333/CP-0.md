# CP-0 — Source readiness: Flutter Entertainment plc (flut)

## Request

- Issuer: Flutter Entertainment plc (issuer id `flut`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025 (context).
- Run: `flut-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned page text of each source and wrote this answer. No provider was called.
- Question: can the supplied public filings and earnings releases support CP-1, CP-1A, CP-2 and CP-5 for the consolidated Flutter group, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles or calculates no figure.
- Locators are `page:N` of the pinned `.jsonl` text of each source (the chunk number in the file), not printed page numbers. Quotes are exact substrings of the cited page.
- Perimeter: the reporting entity in every financial source is the registrant, Flutter Entertainment plc, and its subsidiaries ("the Group"), on a consolidated basis. Debt-level issuers (see the source register) are subsidiaries or co-obligors inside that perimeter; no separate statements for any of them are supplied.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_flut-20251231.htm.jsonl | b88acc6499b34409bd63bcc7ad6ada664ea0aaf382ca0ec0d2118e7c35eb580e | Annual report on Form 10-K for the fiscal year ended December 31, 2025 (223 pages) |
| 10-Q_2026-03-31_flut-20260331.htm.jsonl | 350d396101c8e01e25e223f0670d3e0363c6d230399db566cd885841329d1dbe | Quarterly report on Form 10-Q for the quarter ended March 31, 2026 (62 pages) |
| 10-Q_2026-06-30_flut-20260630.htm.jsonl | a6a0f970aa3d51a04b3c201b89aaae4625c229c4c7864888e69ca9462e615826 | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 (76 pages) |
| 10-Q_2026-09-30_flut-20260930.htm.jsonl | cf209bd21d7ac9131f97943f724a2ebaf7232a79180602605a6b0908ae9a79a1 | Quarterly report on Form 10-Q for the quarter ended September 30, 2026 (83 pages) |
| EX-99.1_2026-05-06_d46069dex991.htm.jsonl | 5416128bf3b9f4328a754a5eff0673c01006c996c64b406795c193ccb390bdfa | Exhibit 99.1 earnings release for Q1 2026 (31 pages) |
| EX-99.1_2026-08-05_d127369dex991.htm.jsonl | 548ad754549966d85d0bb747ddc76468d7bd9635705b387877e25f59264aa63f | Exhibit 99.1 earnings release for Q2 2026 (31 pages) |
| EX-99.1_2026-11-04_d141532dex991.htm.jsonl | ec2552a07ebcbae61da4247ec9d467815436158552ee8c98ff284c26331c74c1 | Exhibit 99.1 earnings release for Q3 2026 (28 pages) |
| context | c092a23c8bebb5c5ed118bc16d3658aa4f2c0513c724b7304133213e545208aa | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists.

The pack also holds `_retrieval.json`, which the launcher ignores. It is not a source here.

The first line of each `.jsonl` names a sha256 for the original HTML document, which differs from the pack-file hash in the table. The pack-file hash is the one cited in this run; the HTML hash cannot be checked from the pack.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The annual report, three quarterly reports and three earnings releases are enough to run all four selected modules on the consolidated group, each with stated limits. Nothing blocks the work. | Medium | Credit agreement, indentures and the October 2026 amendment are not supplied, and covenant ratio values are not printed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual statements and three 2026 interim reports are present, with debt, segment, cash flow and covenant text. | Core financial and debt work can be traced to filed statements. | Medium |
| The October 2026 credit agreement amendment is described only in a note and a release, not supplied as a document. | Post-amendment maturities, margins and covenant terms cannot be checked against executed terms. | Low |
| Covenant compliance is stated, but no covenant ratio values are printed, and the company's own leverage ratio uses a different definition. | Covenant headroom cannot be measured from these sources. | Low |
| Brazil operations have ceased, and legal and tax matters with disclosed amounts are reported, some with no provision. | These items affect earnings and cash and need separate treatment downstream. | Medium |
| Sources are text extractions only. No investor presentations, ratings or market quotes are supplied. | Source fidelity and market-view work rest on text alone. | Medium |

### Readiness view

Every selected consumer can proceed on the supplied filings, with bounded limitations; none is conditional or blocked. The annual report and the three quarterly reports are original authority for statements, notes and covenant text, and the three earnings releases are management-prepared support whose non-GAAP measures are defined differently from the filings and the debt agreements. The recurring limits are that no executed credit agreement, indenture or amendment is supplied, that the October 2026 refinancing is known only from a subsequent-event note and the third-quarter release, that covenant ratio values are not printed, and that nothing dated after the November 4, 2026 filings is supplied.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 statements (`10-K page:145` to `page:149`) and unaudited statements for three interim periods of 2026 are located, with prior-year comparatives. Segment, Adjusted EBITDA, debt, cash-flow and supplemental cash-interest tables are present. Limits: the 10-Qs give cash flows year-to-date only (the Q3 release derives the quarter by subtraction); segment comparatives were not checked for recasts after the 2026 customer transfers between regions. |
| CP-1A | READY_WITH_LIMITATIONS | Business description, brands, two segments, acquisitions, the Fox option on FanDuel, the Brazil shutdown and the UKI restructuring are located. Limits: no investor presentations, no merger or acquisition agreements, and the Fox option terms are those summarised in the 10-K. |
| CP-2 | READY_WITH_LIMITATIONS | Debt tables, maturity table, rates and security text, revolver availability, covenant level, subsequent-event amendment, derivatives, leases, guarantees, purchase obligations and contingencies are located. Limits: no executed agreement or indenture; the Q3 debt table prints no rates, which come from the 10-K at December 31, 2025; no covenant ratio values; the maturity table pre-dates the amendment. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable page locators, so claims can be traced. Limit: text extraction was not compared with the filed HTML or XBRL, and no source is an image or chart that was inspected. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_flut-20251231.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited consolidated statements. Cover at `page:1`: `For the fiscal year ended December 31, 2025`. Registrant: `Flutter Entertainment plc (Exact name of registrant as specified in its charter)`.
- Audit: auditor's report at `page:142` to `page:145`, signed KPMG, Dublin, dated February 26, 2026 (`page:145`: `We have served as the Company’s auditor since 2018.`). It carries an opinion on internal control and two critical audit matters (Snai intangibles valuation and the Fox option valuation). Scope limit: `management excluded from its assessment of the effectiveness of the Company’s internal control over financial reporting as of December 31, 2025, Snai’s internal control over financial reporting`.
- Prior control history: `page:84`: `we previously identified material weaknesses in our internal controls over financial reporting for fiscal years 2024 and 2023`; `While no material weaknesses were identified as of December 31, 2025`.
- Statements: balance sheet `page:145` to `page:146`; statement of comprehensive income (loss) `page:146`; cash flows `page:148` to `page:149`. Notes: segments `page:166` to `page:168`; leases `page:186`; long-term debt `page:187` to `page:190`; commitments and contingencies `page:209`; subsequent events `page:212`.
- Liquidity and debt narrative: MD&A `page:125` to `page:130`, with rates, security, covenant and maturities of the credit agreement and the senior secured notes.
- Exhibits: `page:216` to `page:222` list the indenture, officer's certificates and the credit agreement with its amendments as incorporated by reference. Their texts are not in the pack. Exhibit 21.1 (`List of subsidiaries.*`) is listed at `page:222` but not supplied.
- Units and currency: US dollars in millions; debt also shown in pounds sterling and euros. Period: FY2025 with FY2024 and FY2023 comparatives.

#### Form 10-Q for Q1 2026 (`10-Q_2026-03-31_flut-20260331.htm.jsonl`)

- Family and authority: filed, unaudited interim report; cover at `page:1`: `For the quarterly period ended March 31, 2026`.
- Content: debt note at `page:19` to `page:20` (revolver draws and repayments, undrawn commitment, covenant compliance); segment note `page:11` to `page:12`; liquidity `page:54`.
- Subsequent events at `page:34`: `There were no events requiring disclosure.`
- Units and currency: US dollars in millions; three months ended March 31, 2026 with 2025 comparatives.

#### Form 10-Q for Q2 2026 (`10-Q_2026-06-30_flut-20260630.htm.jsonl`)

- Family and authority: filed, unaudited interim report; cover at `page:1`: `For the quarterly period ended June 30, 2026`.
- Content: debt note at `page:22` to `page:23`; segment note `page:11` to `page:12`; liquidity `page:67`; contingencies and subsequent events `page:37`.
- Subsequent event: delisting from the London Stock Exchange (`page:37`: `On June 12, 2026, the Group announced that it had requested and received approval from the London Stock Exchange`).
- Units and currency: US dollars in millions; three and six months ended June 30, 2026 with 2025 comparatives.

#### Form 10-Q for Q3 2026 (`10-Q_2026-09-30_flut-20260930.htm.jsonl`)

- Family and authority: filed, unaudited interim report, the latest periodic filing in the pack; cover at `page:1`: `For the quarterly period ended September 30, 2026`; signed November 4, 2026 (`page:83`).
- Statements: balance sheet `page:5` to `page:6`; comprehensive income (loss) `page:6` to `page:7`; equity statements `page:7` to `page:9`; cash flows `page:9` to `page:10` (nine months only).
- Notes: segments `page:13` to `page:18`; other income and interest `page:18` to `page:19`; business combinations `page:25` to `page:26`; long-term debt `page:26` to `page:27`; derivatives `page:27` to `page:31`; fair value `page:32` to `page:33`; commitments and contingencies `page:38` to `page:42`; subsequent events `page:42`.
- MD&A: results `page:43` onward; non-GAAP definitions `page:70` to `page:71`; liquidity, leases, purchase obligations and cash flows `page:74` to `page:76`.
- Units and currency: US dollars in millions; three and nine months ended September 30, 2026 with 2025 comparatives.
- Presentation fault to carry: the cash flow statement at `page:9` prints `NET DECREASE IN CASH, CASH EQUIVALENTS AND RESTRICTED CASH 137 138` with positive amounts under a "decrease" caption. Downstream use should take the caption-free beginning and ending balances on the same page and not infer a sign from the caption.

#### Earnings releases (three Exhibit 99.1 files)

- Family and authority: management-prepared press releases filed as Exhibit 99.1, not audited or reviewed statements. They supply attributed management narrative, guidance, non-GAAP reconciliations, the leverage ratio and net debt, and quarter-only cash flows.
- Q1 2026 (`EX-99.1_2026-05-06_d46069dex991.htm.jsonl`): `New York, May 6, 2026`; Adjusted EBITDA reconciliation `page:28`; guidance `page:15` to `page:16`.
- Q2 2026 (`EX-99.1_2026-08-05_d127369dex991.htm.jsonl`): `New York, August 5, 2026`; reconciliation `page:27`; guidance `page:13` to `page:14`.
- Q3 2026 (`EX-99.1_2026-11-04_d141532dex991.htm.jsonl`): `New York, November 4, 2026`; highlights and leverage ratio `page:1`; guidance `page:12`; non-GAAP definitions `page:20` to `page:21`; balance sheet `page:21` to `page:22`; cash flows `page:22` to `page:24`; reconciliation `page:24`. The quarter's cash flow statement is derived (`page:24`): `is derived by subtracting the cash flows from the six months ended June 30, 2026 from the cash flows for the nine months ended September 30, 2026`.
- Authority rule: where a release and a filing differ in definition or amount, the filing controls and the release is a supporting claim.

#### Context (`context`)

- User run settings. It leaves ratings, quotes, deal terms, valuation inputs, assumptions and research questions blank; blank values are not zero. It lists the country as `Netherlands`, while the filings give Ireland (`10-K page:1`: `Ireland 98-1782229`). The filings control; the context field is not issuer evidence.

### Debt and perimeter roles located in the sources

- Borrower group and agreement: `page:125` of the 10-K names the `TLA/TLB/RCF Agreement` of November 2023 with `J.P. Morgan SE as the administrative agent and Wilmington Trust (London) Limited, acting as the collateral agent`. The exhibit list (`10-K page:217`) names the borrowers, including PPB Treasury Unlimited Company, Betfair Interactive US Financing LLC, TSE Holdings Limited, FanDuel Group Financing LLC and Flutter Financing B.V.
- Notes issuer: `Flutter Treasury DAC (the “Issuer”)` issued the 2029 and 2031 senior secured notes (`10-K page:128`). Guarantors are described only generally: `guaranteed on a senior secured basis by the Group and certain of its subsidiaries (collectively, the “Guarantors”)` (`10-K page:128`). The guarantor list is not supplied.
- Facilities and series in the latest debt table (`10-Q Q3 page:26`): three first lien Term Loan A tranches due 2028, the revolving credit facility due 2028, Term Loan B due 2030, Term Loan B due 2032 and five senior secured note series. The table prints principal and carrying amounts but no rates, issuers or guarantors.
- Security: `first priority security interest (subject to permitted liens)` over shares held by an obligor in another obligor and, for United States obligors, substantially all United States assets (`10-K page:127`).

### Cross-source distinctions and conflicts

1. **Leverage definitions differ.** The Q3 release defines its ratio as `Leverage ratio is defined as net debt divided by last twelve months adjusted EBITDA` (`EX-99.1 Q3 page:21`) and reports `Net debt was $10,656m at the end of Q3, with a leverage ratio of 4.6x (3.7x at December 31, 2025)` (`page:11`). The covenant in the 10-K is `the ratio of consolidated net borrowings to consolidated EBITDA as defined therein (the net total leverage ratio) is not greater than 5.20:1 on a bi-annual basis` (`10-K page:128`). The 10-Q warns that `The definition of Adjusted EBITDA and Adjusted EBITDA Margin may not be the same as the definitions used in any of our debt agreements.` (`10-Q Q3 page:71`). Effect: the release ratio and the covenant ratio are not comparable, and the sources print no covenant ratio value.
2. **Covenant changes after quarter end.** The Q3 10-Q (`page:42`) says the amendment `replaces the net total leverage financial covenant with a net first lien leverage financial covenant and the financial covenant level increased to 5.70:1.00`. The 5.20:1 level in the 10-K applies to the pre-amendment test only. No source prints a first lien net leverage figure.
3. **Facility size statements are not reconciled.** The Q3 release says the refinancing is `increasing the overall facility size by approximately $240m and extending the maturity date from November 2028 to May 2032` (`page:12`). The Q3 10-Q says the committed revolving facility `has been increased to $1.86 billion` (`page:75`), and the 10-K described `the Group’s $1.48 billion (£1.1 billion) committed revolving credit facility` (`page:125`). The release figure covers an undefined set of facilities; the sources do not show how it relates to the revolver figures. Effect: CP-2 must use the filing figures and treat the release figure as unreconciled.
4. **Maturity table pre-dates the amendment.** The Q3 repayment schedule (`10-Q Q3 page:26`) is stated as of September 30, 2026, and the amendment of October 30, 2026 extends the term A and revolving maturities to `May 3, 2032` (`page:42`). The schedule therefore no longer matches the post-amendment structure for the term A and revolver amounts it places in 2028; the pro forma schedule is not supplied.
5. **Net debt basis.** The release defines net debt as `total debt, excluding premiums, discounts, and deferred financing expense, and the effect of foreign exchange that is economically hedged` less cash (`EX-99.1 Q3 page:20`); the 10-Q prints `Total debt` and `Total debt principal including accrued interest` on different bases (`10-Q Q3 page:26`). The three bases are not reconciled in the sources.
6. **Legal provision scope.** The 10-Q contingency note (`page:40`) gives a Fast Code provision of `$109 million (A$157.5 million)`, while the Adjusted EBITDA add-back for the quarter is `$105 million relates to a provision recognized to facilitate a potential resolution of the Fast Code Class Action, partially offset by an adjustment in connection with the Indian GST matter` (`page:16`). These are different scopes, not a conflict, and must not be added or substituted.
7. **Stated period labels.** Release highlights and the 10-Q use the same Q3 2026 figures for revenue and net loss (`3,874` and `(1,148)` on the Q3 10-Q `page:6` and release `page:22`). Quarterly Adjusted EBITDA of `360` is a release figure (`EX-99.1 Q3 page:24`); the 10-Q segment note gives segment totals for the quarter and nine months (`10-Q Q3 page:14`).

### Evidence assessment by need

- **Statements and periods.** Evidence: the Q3 10-Q prints `Three months ended September 30, Nine months ended September 30,` columns for 2026 and 2025 (`page:6`), and the 10-K prints three fiscal years. Risk: the cash flow statement is nine months only, so quarterly cash items rest on the release's subtraction. Consequence: CP-1 can build discrete quarters for income items from the three 10-Qs and releases, and must label the derived cash-flow quarter as management-derived.
- **Debt and liquidity.** Evidence: the latest debt table lists every facility and note series with principal and carrying value; the revolver note states `The Group had an undrawn revolving credit commitment of $782 million (£590 million) as of September 30, 2026` and `$13 million (£10 million)` reserved for guarantees (`10-Q Q3 page:27`). Risk: the amendment text is only summarised, and letters of credit other than the guarantee reserve are not tabulated against the revolver. Consequence: CP-2 can compute liquidity at September 30, 2026 from printed inputs and must state the pro forma revolver as a subsequent event.
- **Claims outside debt.** Evidence: operating leases (`10-Q Q3 page:75`: `the Group had operating lease obligations of $559 million with $142 million payable within 12 months`), purchase obligations (`page:75`: `totaled $4,998 million`), bank guarantees (`page:38`: `The maximum amount of the guarantees as of September 30, 2026 was $620 million`), the Fox option (`10-K page:132`: `Fox has until December 2030 to exercise the Fox Option`; fair value `Fox Option liability — — 100 100` at `10-Q Q3 page:33`), redeemable non-controlling interests and litigation and tax matters (`10-Q Q3 pages 38 to 42`). Risk: the 10-K lease note describes `Substantially all leases are long-term operating leases` and the 10-Qs carry no lease maturity table. Consequence: CP-2 can set out these claims with their locators; lease maturities are available at December 31, 2025 only.
- **Latest quarter and after.** Evidence: Brazil operations are `currently ceased` after the measure announced `September 25, 2026` (`10-Q Q3 page:14`); the UKI restructuring plan of `October 20, 2026` (`page:42`); the amendment of `October 30, 2026` (`page:42`); a paused repurchase programme (`page:75`); revised 2026 guidance (`EX-99.1 Q3 page:12`). Risk: guidance is management's claim and the restructuring cost is an estimate range. Consequence: CP-1 and CP-2 can cover the events up to the cutoff; none is dated after November 5, 2026.

## Calculations

None. CP-0 performs no calculation, normalisation or reconciliation. Every figure quoted above is copied from the cited page with its original period and unit. No source-count or page-count figure is used as a readiness proxy: readiness rests on the located content listed in the source register and the evidence assessment.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No executed credit agreement, indentures, officer's certificates or First Amendment and Restatement Agreement. Terms are known from filing summaries only. | Medium | CP-2 | Obtain the credit agreement, the amendment of October 30, 2026 and the indenture; until then state terms as summarised in the filings. |
| Covenant ratio values are not printed; only `the Group was in compliance with all debt covenants` (`10-Q Q3 page:27`). The pre-amendment level was 5.20:1 and the post-amendment first lien level is 5.70:1, with different definitions. | Medium | CP-2 | Obtain the covenant definitions and the compliance certificate; do not present the release leverage ratio as covenant headroom. |
| Guarantor list and the subsidiary list (Exhibit 21.1) are not supplied. | Medium | CP-2, CP-1A | Obtain Exhibit 21.1 and guarantor detail; describe guarantors only as "the Group and certain of its subsidiaries". |
| The Q3 debt table prints no interest rates, issuers, guarantors or security. Rates and security come from the 10-K at December 31, 2025. Whether any rate changed in 2026 is not shown for the term loans, other than the post-amendment margin range of 1.40% to 2.00% for term A and revolver loans. | Medium | CP-2 | Cite the 10-K for legacy terms, label them as of December 31, 2025, and state the post-amendment margin from the Q3 10-Q. |
| Pro forma maturity schedule after the amendment is not supplied; the Q3 schedule is pre-amendment. | Medium | CP-2 | Rebuild the schedule by moving term A and revolver amounts to May 2032 only after the amended principal amounts are confirmed (`€382 million of term A2 loans and $1,374 million of term A3 loans`, `10-Q Q3 page:42`). |
| Facility-size statements are not reconciled (release approximately $240m increase; 10-Q revolver $1.86 billion). | Low | CP-2 | Use the filing figures and flag the release figure as unreconciled. |
| Letters of credit are mentioned only inside the bank guarantee note (`third-party letter of credit facilities`, `10-Q Q3 page:38`), with a total guarantee amount and no split by facility. Whether any draws on the revolver is not stated; the only printed revolver deduction is a `$13 million (£10 million)` reservation for guarantees (`10-Q Q3 page:27`). | Low | CP-2 | State the reservation as the only printed deduction and the guarantee total as separate; do not infer further revolver usage. |
| Cash flows in the 10-Qs are year-to-date only; quarterly cash flows are management-derived in the release. The Q3 10-Q cash flow caption reads "decrease" over positive amounts. | Low | CP-1 | Use year-to-date figures from the filings and label release-derived quarters; take balances, not the caption, for direction. |
| Segment comparatives may have been recast for customer transfers between regions during 2026 (`beginning April 1, 2026, PokerStars’ North America operations formed part of the US region`, `10-Q Q3 page:14`). The sources do not say whether FY2025 segment figures were recast. | Medium | CP-1, CP-1A | Compare the 10-K FY2025 segment tables with the 2025 comparatives in the 10-Qs before any LTM segment build. |
| No Q4 2025 earnings release, no investor presentations, no market quotes and no peer data. The Q3 10-Q says the post-amendment margin depends on `corporate ratings from Moody’s, S&P and Fitch` (`page:42`), but no rating is stated in any source, and the context ratings field is blank. | Medium | CP-1A, CP-2 | Treat market, rating and peer content as Not supplied. Ratings and the applicable margin are not inferred. |
| The extraction was not compared with the filed HTML or XBRL; no chart or image content was inspected. | Low | CP-5 | Spot-check key figures against filed statements in the verification step. |
| The context lists the country as Netherlands; the filings state Ireland. | Low | CP-1A | Use the filings; note the context field as inconsistent. |
| Fox option: the option price and fair value are disclosed, but the Fox option agreement is not supplied; the 10-K states the exercise window to December 2030. | Low | CP-1A, CP-2 | Treat as a contingent claim described in filings only. |

Conflicts logged with locators are listed under "Cross-source distinctions and conflicts" above, each with its downstream effect. No source is blocked, no duplicate source is present, and no draft or unsigned material is supplied. The pack holds three earnings releases but no duplicates of any filing.

## Next module

CP-1 runs next on the 10-K, the three 10-Qs and the releases. It should take the filings as controlling, label release-derived quarters, carry the unreconciled leverage and net debt bases above, and check the segment recast question before building any LTM view. CP-1A and CP-2 follow on the same sources, with CP-2 treating the October 30, 2026 amendment as a subsequent event described only in the Q3 10-Q and release. CP-5 verifies locators and carries the extraction-fidelity limit. The next evidence action is to obtain the credit agreement amendment, the indenture and the covenant definitions.
