## Request

Module: source readiness for MAXLINEAR, INC (MaxLinear, Inc., Nasdaq: MXL, issuer id mxl), as of 2026-11-05. Evidence cutoff 2026-11-05. Pathway: credit snapshot, case kind public, reporting currency USD, current period q3-2026 (quarter ended 2026-09-30), prior period fy-2025 (year ended 2025-12-31). The context names no borrower, parent, guarantors, sponsor, ratings, quotes, deal terms or legal documents; blank fields are treated as unspecified, never as zero.

Question answered: can the effective source set support the requested downstream work, and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion, and it calculates and normalizes nothing.

Requested consumers: CP-1 (financial base), CP-1A (business and transaction context), CP-2 (credit synthesis) and CP-5 (evidence trace). The selected report blocks include a model chart strip, so source evidence for an HTML Model is also assessed. Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No normalized quarters, reconciliation or downstream input acceptance is asserted.

## Sources

### Issuer sources relied on

All seven issuer sources are pinned text extractions (one JSON line per source chunk, cited as `page:N`; a page is an extraction chunk of roughly three thousand characters, not a printed page). Amounts in the filings are in thousands of USD unless a sentence says millions.

| Source name | sha256 | Document family and authority | Chunks |
| --- | --- | --- | --- |
| 10-K_2025-12-31_mxl-20251231.htm.jsonl | 88c5a5c8ff6cf18541031ab4aef4feb9645b937db462a2943427cc48c137e1d9 | Annual report on Form 10-K, fiscal year ended 2025-12-31; audited statements; filed statement authority | 195 |
| 10-Q_2026-03-31_mxl-20260331.htm.jsonl | 42848ffc444d8c47a09304ae1148778a878e57d84c54fa74dc1f2b0e6e5d0dd8 | Quarterly report on Form 10-Q, quarter ended 2026-03-31; unaudited; filed statement authority | 126 |
| 10-Q_2026-06-30_mxl-20260630.htm.jsonl | 01411c1534e3e0c0e916b41e14102517d827593ed353c6e2edbb7bcfabe4eb3d | Quarterly report on Form 10-Q, quarter ended 2026-06-30; unaudited; filed statement authority | 66 |
| 10-Q_2026-09-30_mxl-20260930.htm.jsonl | 75f4d013edbcd52763843513db2d44d0258392fcbcf7fab3f738307f7e5ec1a3 | Quarterly report on Form 10-Q, quarter ended 2026-09-30, issued 2026-10-22; unaudited; filed statement authority | 66 |
| EX-99.1_2026-04-22_a03312026exhibit991.htm.jsonl | 80656f36f632a9814cfc0d89b1465026471d15c2a52a4f467e504c7d5e0b776a | Earnings release for the first quarter of 2026; management-issued, supporting claims | 10 |
| EX-99.1_2026-07-23_a06302026exhibit991.htm.jsonl | 513984500469e10cfb125419373d89d4b53d02f7f1ffe85723d32af0bb949f83 | Earnings release for the second quarter of 2026; management-issued, supporting claims | 11 |
| EX-99.1_2026-10-22_a09302026exhibit991.htm.jsonl | 2f6d78692e5e0106407183ea23f9296509641c88888df05a93887a904e78fabf | Earnings release for the third quarter of 2026, dated 2026-10-22; management-issued, supporting claims | 10 |

### Context and other inputs

| Input | sha256 | Role |
| --- | --- | --- |
| context (1288469-maxlinear-inc-mxl.json) | 39695f94e05534dbaa55be69eaec116e2e3f550f0af980e236d8132f5e5386f2 | Dated user settings for this run; not issuer evidence |

The pack folder also holds a `_retrieval.json` metadata file. It is not a pinned source and was not relied on.

### Supplied handoffs

None. This is the first module of the run and CP-OS supplied no upstream handoff, so there is no handoff module or hash to list.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings and releases support a bounded credit snapshot of MaxLinear on a consolidated US dollar basis through the third quarter of 2026 and the October 2026 credit agreement amendment, but not a review of legal terms. | Medium | The credit agreement and its three amendments are not supplied, so covenant definitions, letter of credit use and the reported leverage ratio cannot be verified from source. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited 2025 annual statements and unaudited statements for all three 2026 quarters are present, with earnings releases in place of presentations. | The financial base and quarterly trend can be built from filed statements. | High |
| Revolver size and covenant wording differ across filings, and the October 2026 amendment falls after quarter end. | Liquidity headroom must be shown at quarter end and after the amendment, separately. | Medium |
| The Silicon Motion arbitration and related suits carry no disclosed amount, and the arbitration is confidential. | The size of this contingent claim cannot be assessed from the sources. | Low |
| No ratings, market quotes or sponsor data are supplied, and nothing after the 2026-10-22 release is in the pack. | Market-based views and the last two weeks before the as-of date stay unobserved. | Medium |

### Readiness view

The effective source set is adequate for a credit snapshot with stated limitations, and no consumer is blocked. Seven issuer documents from a single registrant are present: one audited annual report, three quarterly reports and three quarterly earnings releases, covering fiscal 2025 and each quarter of 2026 through 2026-09-30. All are filed statements or issuer releases for MaxLinear, Inc. in USD, with consistent period labels, and the third quarter release agrees with the third quarter 10-Q on the figures checked (net revenue 218,057 on `page:7` of the release and `page:4` of the 10-Q; cash and cash equivalents 81,085 on `page:9` of the release and `page:4` of the 10-Q; long-term debt 164,062 on both). The strongest contrary evidence is on the financing side. The credit agreement, its three amendments and the security agreement are exhibits incorporated by reference and are not in the pack (10-K `page:131`; third quarter 10-Q `page:65`), so every covenant, basket, guarantor and collateral statement rests on the issuer's own note summaries. Those summaries differ between filings: the second quarter 10-Q describes the liquidity covenant two ways (`page:23`, `page:60`), the springing secured net leverage test appears in the 10-K and the first two quarterly reports but not in the third quarter note, and the third quarter MD&A states the revolver at its post-amendment size while reporting borrowings at quarter end (`page:60`). The Silicon Motion arbitration has no quantified exposure (`page:38`). Consequence: CP-1, CP-1A, CP-2 and CP-5 can run as READY_WITH_LIMITATIONS, and the limits must be carried into each handoff; CP-2 must not present covenant headroom as verified against the executed agreement. The next evidence action is to obtain the executed credit agreement with Amendments No. 1 to No. 3 and the 8-K filed 2026-10-22 that carries the third amendment, and any filing between 2026-10-22 and 2026-11-05.

### Source-by-source assessment

| Source | Entity and perimeter | Period and basis | Located content relied on | Limits |
| --- | --- | --- | --- | --- |
| 10-K | MaxLinear, Inc. (Delaware, Commission file number 001-34666) and its wholly-owned subsidiaries, consolidated (`page:1`; note 1 `page:139`) | Fiscal 2025, with 2024 and 2023 comparatives; USD thousands | Balance sheet `page:136`; operations `page:136`-`page:137`; cash flows `page:137`-`page:138` (cash paid for interest 8,598 on `page:138`); debt note `page:165`-`page:168`; contractual obligations `page:120`; commitments and litigation `page:188`-`page:194`; business `page:7`-`page:27`; audit report `page:134`-`page:136` | Revolver shown at 100.0 million maturing 2026-06-23 (`page:167`), superseded by the second amendment; legal exhibits listed but not supplied (`page:129`-`page:131`) |
| 10-Q, first quarter | Same registrant and perimeter (`page:1`) | Three months to 2026-03-31, unaudited; USD thousands | Statements `page:2`-`page:4` (cash paid for interest 1,935 on `page:4`); debt note `page:17`-`page:20`; second amendment `page:40`; liquidity `page:51`-`page:52`; full risk factors later in the file (for example `page:100`) | Still describes the pre-amendment covenant on `page:19`; the second amendment appears as a post-period event |
| 10-Q, second quarter | Same registrant and perimeter | Three months and six months to 2026-06-30, unaudited | Statements `page:4`-`page:7` (cash paid for interest 3,984 on `page:6`); debt note `page:21`-`page:24`; liquidity `page:58`-`page:61`; litigation `page:38`-`page:43` | Internal covenant wording conflict (`page:23` against `page:60`) |
| 10-Q, third quarter | Same registrant and perimeter; names Exar Corporation and MaxLinear Communications, LLC as wholly-owned subsidiary parties to the third amendment (`page:48`) | Three months and nine months to 2026-09-30, unaudited; USD thousands | Balance sheet `page:4`; operations `page:4`-`page:5`; cash flows `page:6`-`page:7` (cash paid for interest 6,425 on `page:7`); debt note 8 `page:20`-`page:24`; litigation `page:38`-`page:43`; segment note `page:43`-`page:44`; subsequent event `page:44`; contractual obligations `page:58`; liquidity `page:59`-`page:61`; exhibits `page:65` | Covenant description omits the springing leverage test (`page:23`-`page:24`); MD&A revolver size is post-amendment (`page:60`) |
| Release, first quarter | Same registrant, consolidated | Quarter to 2026-03-31, GAAP and non-GAAP; dateline April 23, 2026 though the file name carries 2026-04-22 | Management commentary and credit agreement announcement `page:2`; statements `page:7`-`page:9`; second quarter outlook `page:2` | Management claims only; no presentation slides exist |
| Release, second quarter | Same registrant, consolidated | Quarter and six months to 2026-06-30 | Statements `page:8`-`page:11` | Management claims only |
| Release, third quarter | Same registrant, consolidated | Quarter and nine months to 2026-09-30, with the second quarter of 2026 and third quarter of 2025 columns | Summary `page:1`; credit agreement and fourth quarter outlook `page:2`; non-GAAP reconciliation `page:7`-`page:8`; cash flows `page:8`-`page:9`; balance sheet `page:9`-`page:10` | Fourth quarter non-GAAP guidance has no reconciliation (`page:7`) |

### Entity and instrument roles

| Role | What the sources state | Locator | Unresolved |
| --- | --- | --- | --- |
| Issuer and borrower | MaxLinear, Inc. is the party to the June 23, 2021 Credit Agreement; Wells Fargo Bank, National Association is administrative agent and collateral agent | Third quarter 10-Q `page:21` | None |
| Parent and sponsor | None named in the sources or the context | Context; 10-K `page:1` | Not applicable on the evidence |
| Guarantors | Certain domestic subsidiaries meeting materiality thresholds guarantee the obligations; they are not named | Third quarter 10-Q `page:23` | Identity of guarantors; whether Exar Corporation and MaxLinear Communications, LLC are guarantors is not stated |
| Collateral | Obligations are secured by substantially all assets of the company and the subsidiary guarantors under a Security Agreement dated June 23, 2021 | Third quarter 10-Q `page:23` | Security agreement not supplied |
| Initial Term Loan | Senior secured term B loan, original principal 350.0 million, outstanding principal 125.0 million, due June 23, 2028 | Third quarter 10-Q `page:21`, `page:20` | Executed terms not supplied |
| Revolving Facility | Senior secured; 40.0 million drawn at 2026-09-30, maturity March 23, 2028 after the second amendment | Third quarter 10-Q `page:20`, `page:23` | Commitment total at quarter end is not printed as one figure |
| Restricted and unrestricted entities | Covenants refer to restricted subsidiaries; no designation list | Third quarter 10-Q `page:23` | Not supplied |

### Version relationships and conflicts

Each periodic filing and each release is a separate active source. Later filings control current-period facts; earlier filings are retained for history and for the superseded terms noted below. No source is a duplicate of another by content.

| Item | Source A | Source B | Effect downstream |
| --- | --- | --- | --- |
| Revolver maturity and size | 10-K `page:167`: matures June 23, 2026; 10-K `page:118`: up to 100.0 million, undrawn | Second quarter 10-Q `page:22`-`page:23` and third quarter 10-Q `page:22`-`page:23`: second amendment on April 22, 2026 moved maturity to March 23, 2028 and added 30.0 million of commitments; release first quarter `page:2`: increased to 130 million | Version change, not a conflict; CP-2 must use the amended terms for 2026-09-30 |
| Revolver size at quarter end | Third quarter 10-Q `page:60`: revolver "of up to $200.0 million, under which $40.0 million in borrowings were outstanding as of September 30, 2026" | Third quarter 10-Q `page:44` and `page:48`: the 70 million of incremental commitments were effected on October 16, 2026, after quarter end | The 200.0 million is a post-quarter figure; quarter-end commitments are implied, not printed; show quarter-end and pro forma liquidity separately |
| Liquidity covenant wording | Second quarter 10-Q `page:23`: unrestricted cash plus available undrawn commitments "not to exceed 100% of the Consolidated EBITDA for the most recently ended Test Period" | Second quarter 10-Q `page:60`, first quarter 10-Q `page:40` and third quarter 10-Q `page:23`-`page:24`: not less than 80 million | The weight of the sources is a floor of 80 million; the outlier is unresolved because the agreement is not supplied |
| Springing secured net leverage test | 10-K `page:167`, first quarter 10-Q `page:19` and second quarter 10-Q `page:24`: secured net leverage not above 3.50 to 1.00 (3.75 to 1.00 after certain acquisitions) if revolver borrowings exceed 1% of commitments | Third quarter 10-Q `page:23`-`page:24`: total net leverage ratio not above 3.50 to 1.00 and the liquidity floor; no mention of the springing test | Whether the springing test survives the second amendment is unresolved; CP-2 must name both formulations |
| Liquidity covenant threshold | Third quarter 10-Q `page:24`: 80.0 million, in compliance at 2026-09-30 | Third quarter 10-Q `page:44`-`page:45`, `page:48`, `page:61`: reduced to 60 million by the third amendment of October 16, 2026 | Subsequent event; test dates after 2026-09-30 use 60 million per the issuer |
| Commitment fee | 10-K `page:166`: 0.175% to 0.25% | Third quarter 10-Q `page:23`: 0.25% | Version change after the second amendment |
| Sale arrangement liability | First quarter 10-Q `page:20`: proceeds of 6.0 million | Third quarter 10-Q `page:24`: proceeds of 8.0 million; cash flow line "Proceeds from funding arrangement" 8,000 (`page:6`) | Consistent progression |

### Readiness by requested consumer

| Consumer | Rating | Evidence located | Limitations carried |
| --- | --- | --- | --- |
| CP-1 financial base | READY_WITH_LIMITATIONS | Three annual periods in the 10-K; each 2026 quarter in a 10-Q and a release; quarter-to-date and year-to-date columns; end-market revenue (third quarter 10-Q `page:34`-`page:35`, `page:50`-`page:51`); debt and covenants (`page:20`-`page:24`); cash paid for interest and tax (year-to-date only in 10-Qs) | Discrete fourth quarter 2025 and discrete quarterly cash interest require subtraction downstream; no Consolidated EBITDA as defined in the agreement or reported leverage ratio; table rows split across chunks |
| CP-1A business and transaction | READY_WITH_LIMITATIONS | Business description in the 10-K; terminated Silicon Motion merger and arbitration (third quarter 10-Q `page:14`, `page:38`-`page:40`); credit agreement amendments; sale arrangement; competitor and customer litigation (`page:41`-`page:43`); share repurchase program (`page:44`) | Arbitration is confidential and unquantified; no ownership or sponsor information; executed amendments not supplied |
| CP-2 credit synthesis | READY_WITH_LIMITATIONS | Debt table (`page:58`), liquidity discussion (`page:59`-`page:61`), covenant summaries, subsequent event | No executed credit agreement; letter of credit use not found; no ratings or market data; conflicting covenant wording |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | Every source above supports quote and figure tracing by `page:N`; releases and filings overlap on core figures | Trace quality depends on upstream handoffs, not yet supplied; extraction fidelity not reviewed |
| HTML Model source evidence | Sufficient for source purposes only | Discrete quarters, fiscal years, quarter and year-to-date columns, end-market revenue, non-GAAP add-back reconciliations (releases, for example third quarter `page:8`), facility-level debt and carrying value (`page:4`, `page:20`, `page:58`), cash-paid interest and tax, business narrative | SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED |

### Coverage statement

Every chunk of every source was listed by its opening text (195 of 195, 126 of 126, 66 of 66, 66 of 66, 10 of 10, 11 of 11 and 10 of 10 chunks). Each chunk cited above was opened and checked for the figure or wording it is cited for; the remaining chunks (mainly risk factors, equity compensation, tax and accounting policy text) were inventoried by opening text but not read line by line, and are retained as available evidence rather than excluded. No presentation slides, scans, images, charts or workbooks exist in the set, so no slide, image or speaker-note coverage is claimed. Extraction status is separate from fidelity: the text was extracted successfully, but no fidelity review against the original documents was performed, and some tables are split across chunks (for example the end-market table, whose first row is at the end of third quarter 10-Q `page:34` and whose percentages are at the start of `page:35`).

## Calculations

No calculation was performed; this module is forbidden to normalize, reconcile or calculate figures. Counts used above: 7 issuer sources, 0 supplied handoffs, 4 requested consumers. The cross-source agreement checks quoted in the readiness view compare printed figures only (net revenue 218,057; cash and cash equivalents 81,085; long-term debt 164,062) and derive nothing.

## Gaps

| Gap | Severity | Affected consumers | Evidence | Remediation |
| --- | --- | --- | --- | --- |
| Executed Credit Agreement of June 23, 2021, Security Agreement and Amendments No. 1 to No. 3 not supplied; the context sets legal documents to none | High | CP-2, CP-1A, CP-5 | Exhibit list 10-K `page:131`; third quarter 10-Q `page:65` (third amendment incorporated from an 8-K filed 2026-10-22) | Add the executed agreement, amendments and the 8-K |
| Covenant description conflicts: liquidity covenant wording in the second quarter 10-Q; springing leverage test present in earlier filings and absent in the third quarter note | High | CP-2, CP-5 | Second quarter 10-Q `page:23`, `page:24`, `page:60`; third quarter 10-Q `page:23`-`page:24` | Resolve against the executed agreement; until then state both formulations |
| Quarter-end revolver commitments not printed as a single figure; MD&A states the post-amendment 200.0 million alongside quarter-end borrowings | Medium | CP-2, CP-1 | Third quarter 10-Q `page:60`, `page:44`, `page:48` | Obtain the amendment text or a compliance certificate |
| Letters of credit outstanding under the revolver: not found after searching "letter of credit", "LC" and "standby"; only a 10.0 million Letter of Credit Commitment (`page:22` of the second and third quarter 10-Qs) and restricted cash held as collateral for letters of credit (10-K `page:141`) | Medium | CP-2 | Same pages | Obtain issued letter of credit balances |
| Reported total net leverage ratio and Consolidated EBITDA as defined are not printed; no EBITDA measure appears in the releases; only compliance statements exist | Medium | CP-1, CP-2 | Third quarter 10-Q `page:24`; non-GAAP reconciliation third quarter release `page:8` | Compliance certificate or agreement definitions |
| Silicon Motion arbitration and related suits: no amount or range; "no material loss contingencies have been accrued"; unfavorable outcome reasonably possible, range not estimable | High | CP-2, CP-1A | Third quarter 10-Q `page:38`-`page:40`, `page:43` | Monitor disclosures; no source can size it |
| Events after 2026-10-22 are not in the pack, including the status of the Dish action stayed until November 2, 2026 | Medium | CP-1A, CP-2 | Third quarter 10-Q `page:42` | Add filings dated through 2026-11-05 |
| No ratings, quotes, valuation inputs, peers, sponsor or ownership data in the context | Low for this snapshot | CP-2 | Context | Supply if relative value is later requested |
| Three releases replace presentations; no slide content exists | Low | CP-1A | Release first, second and third quarters | None needed for the selected report |
| Fourth quarter 2025 has no release; discrete fourth quarter 2025 and 2024 figures depend on subtraction from annual and nine-month comparatives | Low | CP-1 | 10-K `page:136`; third quarter 10-Q `page:5` | Derive downstream with stated inputs |
| Cash-paid interest and tax are cumulative in each 10-Q; discrete quarters need subtraction | Low | CP-1 | First quarter `page:4`, second quarter `page:6`, third quarter `page:7` of the 10-Qs | Derive downstream |
| Extraction fidelity not reviewed; tables flattened and split across chunks | Low | All | Third quarter 10-Q `page:34`-`page:35` | Spot-check key tables against the original files |

## Next module

Proceed to CP-1 with every consumer rated READY_WITH_LIMITATIONS, and carry these limitations forward: use the amended revolver terms and show quarter-end and post-October 16, 2026 liquidity separately; present the liquidity covenant at 80 million for 2026-09-30 and 60 million afterwards, flagging the conflicting second quarter wording; name both the total net leverage and the springing secured net leverage formulations without asserting a ratio the sources do not print; treat the Silicon Motion exposure as unquantified; derive discrete quarters from cumulative columns only with inputs and locators shown; label every figure as quarter, year-to-date or fiscal year. CP-1A should follow CP-1, then CP-2, then CP-5. Evidence still to obtain: the executed credit agreement and amendments, the 8-K of 2026-10-22, any filing through 2026-11-05, letter of credit balances, and the compliance leverage calculation.
