## Request

PITNEY BOWES INC /DE/ (Pitney Bowes Inc., issuer id pbi), as of 2026-11-05, pathway credit_snapshot, USD. This module traces the claims of the four accepted handoffs (source readiness, financial base, business context, credit synthesis) to the seven supplied filings and releases, checks locators, quotes and calculations, logs conflicts and grades research integrity. It does not change the underlying credit conclusion and does not repair lineage silently.

## Sources

### Issuer sources traced

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_pbi-20251231.htm.jsonl | 4f5deb57a07fe1eea64b3f9a9468185d34382c2ac8c5a94646c45747e0b2326e |
| 10-Q_2026-03-31_pbi-20260331.htm.jsonl | 624a80b6cca522410fd3993e4d3c4a11f7096c24a4986d50fced927a53e82f28 |
| 10-Q_2026-06-30_pbi-20260630.htm.jsonl | 1df859f2a36df1a95ab3c12f91757b26486c9d8b234afc186a635a7369a5958d |
| 10-Q_2026-09-30_pbi-20260930.htm.jsonl | 9ac96ecd84cbfc34b739239b40a8f155d4a7193f9d71c03e1504313a41bfda22 |
| EX-99.1_2026-05-05_q12026earningspressrelea.htm.jsonl | 429691f75b3fe167dac89bd697b030c14535bbbb0b53e2afaf1e37a0eeb21619 |
| EX-99.1_2026-07-29_q22026earningspressrelea.htm.jsonl | 0a144327096e38bc9546ab64951475ad37b63f71db5dc4f751be723ca256bc40 |
| EX-99.1_2026-10-28_ex991q32026earningspress.htm.jsonl | 42e81ba5c9c8e886a22fe22bd69da5cf53cfc84b55897aeb23cc53c06bbc9f1b |

The run context (sha256 c37c14ec550e9841f87339ac47485b30200b39c05673baeb478fd6400a5b7677) holds dates and currency only and is not issuer evidence.

### Supplied handoffs audited

| Module | sha256 |
| --- | --- |
| CP-0 (source readiness) | cad86cb0a3fd98500e899a766aea0470956626c6150c1885edf57ff710f357b9 |
| CP-1 (financial base) | bcde32ba969dc3f68634f56be69b4c3c438b14957c4d8e94474c2f62621f2491 |
| CP-1A (business and transaction context) | 2f340249f20dd5ea76d7bc9f7d6fd032d6b1dbcb1da7d821f7291bc2b14d414a |
| CP-2 (credit synthesis) | 0397e4d226105a1a3c485d35353415f77a122f6ca197352383bc29e7a73fe06d |

The sources are text extractions in page-sized chunks; `page:N` is a chunk, not a printed page. Both the source pages and the handoffs were opened, not only the handoffs' own citations. The business-context handoff was accepted on its second attempt after a number-consistency correction; the accepted version is the one audited.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The figures in the four handoffs trace to the filings, with one material limit and six minor defects. Committee use is restricted for covenant, springing-maturity and legal-structure conclusions because governing debt documents are not supplied. | Medium | No credit agreement, indenture or guarantor list is supplied, so covenant headroom, springing tests, ranking and legal capacity cannot be traced to governing documents. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of 20 material claims, 10 are directly sourced, 5 calculated, 2 assumption-based, 2 analyst inference and 1 insufficient; every stated figure reproduced from the cited pages or from printed inputs. | Debt, liquidity, maturity and segment figures can be relied on as filed facts. | High |
| Leverage recomputed from printed inputs matches: 3.24x gross and 2.79x net on principal, and 3.19x and 2.74x on carrying value. | The debt basis moves leverage by about 0.05x and does not change the view. | High |
| Covenant compliance and the springing-maturity tests rest on management statements and an undefined liquidity term. | Revolver access and early-maturity risk cannot be verified, so committee use is restricted. | High |
| Six minor defects were found, including a litigation party description and locator slips; none changes a figure. | They are logged for clean-up and do not alter the credit view. | High |

### Evidence trace view

The traced evidence is sound for the stated purpose of a fundamental, filings-based credit screen. Every dollar figure in the four handoffs was found on the cited page of the cited filing or release, or reproduces from printed inputs, with the exceptions logged in the issue register: two locators that point to the wrong page, one litigation description that goes slightly beyond the note, one coupon-timing explanation that generalizes from a single instrument, one customer description that goes beyond the release, and one date taken from a different page than the one cited. Calculated figures, including the Adjusted EBITDA built for FY2025, reproduce on the release method, which itself ties to the printed reconciliations for every quarter of 2026 and 2025. The weaknesses lie in what the sources cannot show: the covenant definitions and reported ratios, the credit-agreement meaning of liquidity in the springing-maturity test, the guarantee and security structure, the content of the Form 10-K/A that later filings cite, and the executed amendments. Because those gaps bear on committee conclusions about revolver access and legal capacity, the research is graded Restricted, not Passed, and the synthesis confidence of Medium is appropriate.

### Traceability conclusion

The analysis is traceable enough for a fundamental credit screen but not for covenant, springing-maturity, legal-structure or relative-value decisions. Supported claims dominate: the debt schedule, liquidity, maturity profile, segment results, distributions and claims outside debt all reproduce from filed pages, and leverage, cover and liquidity recompute from printed inputs. Inference is confined to labelled interpretation, such as the reading of mail decline, the supportive reading of debt actions and the pension-basis sensitivity. The most important provenance gap is the missing credit agreement: management states covenant compliance and the filings describe a springing maturity, but neither the reported ratios nor the credit-agreement definition of liquidity can be traced. The remediation is to obtain the credit agreement with all amendments, the latest compliance certificate and the indentures.

### Audit summary

| Field | Value |
| --- | --- |
| Committee status | Restricted: permitted for fundamental screening, liquidity and maturity review with the limitations disclosed; not for covenant headroom, springing-test, legal-capacity or ranking conclusions |
| QA status | Restricted (one MATERIAL finding, no CRITICAL) |
| Confidence score and band | 56, Low (computed with the canon script: E 81.5, C 100, S pass 1.0, P 33); the Medium confidence in the reader summary is confidence in the traceability conclusion, not the computed research score |
| Material claims by lineage | Directly Sourced 10, Calculated 5, Assumption-Based 2, Analyst Inference 2, Insufficient Information 1 |
| Findings | MATERIAL 1, MINOR 6 |
| Quote and locator audit | 78 quoted spans checked against the cited source text, all found; 242 printed figures checked against the page cited on their line, all matched; 107 further figures were reviewed and are derived results or are cited on another page, with two locator defects (I-02, I-03) |

### Analytical appendix — complete canonical registers

#### T5.1 Handoff register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response 1; run pbi-2026-11-05-credit_snapshot-host | Source readiness of seven sources, four consumers | High: filed statements and releases | Six H2 headings and readiness view present | Restricted | Issues I-02, I-03 and I-04; verdicts READY_WITH_LIMITATIONS consistent with later work |
| CP-1 | requests/CP-1 response 1; same run | Financial base: statements, leverage, interest cover, liquidity, maturities, debt schedule, claims outside debt | High for printed figures; Calculated for Adjusted EBITDA for FY2025 and LTM | Six H2 headings, four chart tables and the financials table present | Restricted | Issues I-04, I-05 and I-06 |
| CP-1A | requests/CP-1A response 2; same run | Business, ownership, transaction and governance context, fact register F1 to F40 | High | Six H2 headings, operating model and profile tables, transaction prose present | Restricted | Accepted at attempt 2 after a summary-number correction; issues I-04 and I-07; legal capacity and ownership correctly marked Insufficient Information |
| CP-2 | requests/CP-2 response 1; same run | Credit synthesis from the upstream handoffs | High for figures; synthesis is Analyst Interpretation | Six H2 headings, prose-only key findings and strengths-and-weaknesses present | Restricted | Confidence Medium, below High as the method requires; inherits I-04 |

#### T5.2 Claim and section evidence issues

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-0, CP-1, CP-1A, CP-2 | Covenant compliance, springing-maturity tests and security (I-01) | Management statement only: "At September 30, 2026, we were in compliance with these financial covenants." (Q3 10-Q page:20) | Three maintenance tests are printed (page:20) but the reported ratios, the credit-agreement definitions of EBITDA, secured net debt and liquidity, and the amendments are not supplied | Obtain the credit agreement with all amendments, the compliance certificate and the indentures | Committee use restricted for covenant, springing-test and ranking conclusions |
| MINOR | CP-0 | Gap 5 on FY2025 comparatives (I-02) | Figures verified: debt 1,993,038 and total assets 3,168,951 agree between the 10-K and the 2026 filings | The locators cited (10-K pages 1-2, Q3 10-Q page:5, Q3 release page:4) support the 10-K/A reference, not the tied figures, which are on 10-K page:98 (debt) and page:66 (total assets), and Q3 10-Q page:19 and page:3 | Cite the pages that carry the tied figures | None on values |
| MINOR | CP-0 | Source-risk paragraph on adjusted-measure comparability (I-03) | Quote verified (Q3 10-Q page:9); the 23,125 add-back is on page:10 | The amount is cited to page:9 | Cite page:10 for the amount | None on values |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Litigation party description (I-04) | Amount verified: "more than $100 million" (Q3 10-Q page:24) | The handoffs describe the matter as a suit by, or dispute with, a former ecommerce vendor; the note describes a dispute with "a former vendor for GEC" and names Kingsbridge Holdings as parent of Trilogy Leasing without stating that Trilogy is that vendor | Reword to: suit by the parent of Trilogy Leasing, in a dispute over equipment supplements with a former vendor | None on the amount |
| MINOR | CP-1 | Interest cover chart note (I-05) | Cash interest figures verified (10-K page:96; Q1 10-Q page:24; Q2 10-Q page:26; Q3 10-Q page:26) | The note says cash interest is uneven "because coupons are semi-annual"; only the convertible notes' payment dates (February 15 and August 15, 10-K page:43) are printed | Say the timing of coupons and other payments is uneven, or cite only the convertible dates | None on values |
| MINOR | CP-1 | Interpretation of cash flow (I-06) | Release statement verified (Q3 release page:2) | The financial base calls the prepaying clients "new Presort customers"; the release says "new customers" and "a significant mail sortation competitor" | Reword to new customers of the sortation business, attributed to management | None |
| MINOR | CP-1A | Transaction summary on the February 2025 credit agreement (I-07) | Date verified: exhibit 10(bb) is "dated as of February 7, 2025" (10-K page:59) | The sentence cites 10-K page:42, which says first quarter of 2025 | Cite page:59 for the date | None |

#### T5.3 Metric and logic issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None (disclosed) | CP-1, CP-2 | FY2025 Adjusted EBITDA is calculated, not printed | Total adjusted segment EBIT less corporate expenses plus depreciation and amortization; the same method reproduces the printed nine-month and quarterly figures of both years (Calculations) | No Q4 2025 release is in the pack to compare | Keep labelled as calculated | LTM ratios rest on a derived base; the method is reproducible |
| None (disclosed) | CP-1, CP-2 | Pension basis: 2026 adds back terminated-plan pension expense, 2025 does not | Like-for-like sensitivity subtracts 23,125 (Q3 10-Q page:10) from LTM; assumes the 2025 base carried the equivalent cost | Prior periods were not recast (Q3 10-Q page:9) | Keep both bases visible | Leverage 3.24x against 3.38x gross and 2.79x against 2.90x net |
| None (disclosed) | CP-1, CP-2 | Leverage is stated on debt principal | Carrying value is lower by unamortized costs of 31,013 at 2026-09-30 | None | Show carrying-basis ratios beside principal ratios (Calculations) | 0.05x |
| None | CP-1 | Cash interest cover uses cash interest paid, which covers the whole group including the financing business | Total interest including allocated financing interest cover is shown separately | None | None | Bases are labelled |
| None (disclosed) | CP-1, CP-2 | Springing-test arithmetic uses cash plus capacity as liquidity | The credit-agreement definition is not supplied; labelled not a test result | None | Keep labelled | Cushion of 119.5 is indicative only |
| None | CP-1A | Margins and shares computed from printed inputs | 351,243 over 928,132 and similar recompute | None | None | None |

#### T5.4 Legal and structural claims

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL (counted once under I-01) | CP-1, CP-2 | Borrowings under the credit facility are "secured by assets of the Company" and carry three maintenance covenants and springing maturity provisions (Q3 10-Q page:20) | Credit agreement, amendments and security documents | Company summary only | Obtain and review | Required before any covenant, ranking or security conclusion |
| MATERIAL (counted once under I-01) | CP-1, CP-1A, CP-2 | Convertible notes are senior unsecured and guaranteed by wholly owned U.S. subsidiaries that guarantee the credit agreement, senior notes or other capital market debt above 150 million (Q3 10-Q page:22) | Convertible indenture dated August 8, 2025 and guarantor list | Company summary; guarantors not named | Obtain the indenture and guarantor list | Required before any structural-subordination conclusion |
| None (disclosed gap) | CP-1, CP-1A | Secured or unsecured status of the 7.25%, 5.25% and 6.70% notes | Indentures (exhibits 4(a) to 4(f); first supplemental indenture dated March 2, 2026) | Exhibit list only (10-K pages 56-57; Q3 10-Q page:39) | Obtain the indentures | Ranking column in the debt schedule is unverified |
| None (disclosed gap) | CP-1A | Legal capacity to distribute, add debt or release collateral | Credit agreement and indentures | Not supplied | Obtain | CP-2 treats capacity as Insufficient Information |
| None | CP-1A | Ecommerce Restructuring: 81% of voting interests sold, 19% voting and 100% economic interest retained, debtor-in-possession balance fully reserved (10-K page:85) | Sale and restructuring support agreements (exhibits 10(y) to 10(aa)) | Described in the 10-K only | Obtain if the exposure is to be sized | Exposure described, not quantified |
| None | CP-1A | The Bank is a Utah industrial bank regulated by the state and the FDIC (10-K page:9) | Charter and regulatory filings | Not needed for the screen | None | Cash availability from the Bank is Insufficient Information |

#### T5.5 Market and relative-value claims

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-2 | No peer ranking, instrument recommendation or recovery conclusion is made | Not applicable | None | None | Compliant with the prohibitions |
| None | CP-1A, CP-2 | Ratings: none stated in the sources; the context lists none | Agency reports | Searched all sources | Obtain current agency reports before any rating-based view | No rating-based statement is made |
| None | CP-1 | Debt fair value 1,912.0 against carrying 1,887.4 is quoted as filed (Q3 10-Q page:18) | Trading levels | Not required | None | No market-implied statement is made |
| None | CP-1A | Peer group listed in the 10-K performance graph is not used | Not applicable | None | None | None |

#### T5.6 Data and claim conflicts, and version issues

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR (logged, not reconciled) | CP-0, CP-1, CP-1A, CP-2 | Term loan and revolver maturity: Q2 10-Q "to March 2031", Q3 10-Q "to May 2031" for the same Q2 extension (pages 20) | The Fifth Amendment of September 29, 2026 may explain it but is not supplied | Quote both; use the later filing and flag | Two months on the 294.5 term loan and the revolver; first maturity unchanged |
| MINOR (logged) | CP-1, CP-1A | Margin on the 2028 term loan: SOFR + 2.10% (10-K page:98) against SOFR + 1.85% (Q1 10-Q page:18) | Amendments between the two dates not supplied | Quote both | Cost of 0.25% on 150 to 300 of principal |
| MINOR (logged) | CP-1A | Repurchase authorization: 10-K "a new $500 million" plus "$250 million" increase; Q3 10-Q "$250 million share repurchase program to $750 million" | Both give 750 million in total | Quote both | Wording of the February 2026 addition only |
| MINOR (logged) | CP-1, CP-1A | Tender gain: "$5 million" in the Q3 10-Q text against (3,155) thousand in the table | The implied discount of 5,746 in the financial base is an inference | Use the table for statement lines | About 2 million of description |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Form 10-K/A cited by the 10-Qs and releases against the Form 10-K in the pack | Content of the amendment unknown; FY2025 figures tie to the 10-K in the 2026 comparatives | Obtain the 10-K/A | FY2025 labelled as per the Form 10-K |
| None | CP-1, CP-2 | Convertible notes conversion rate 70.4648 (Q3) against 70.1533 (10-K) and 70.2937 (Q1) | Dividend adjustments, as the notes state | None | Not a conflict |
| None | CP-1, CP-1A | Debt principal agrees across the 10-K, the 2026 10-Qs and the Q3 release (reductions of 108 and 148 million tie within rounding) | None | None | None |

#### T5.7 Other issues

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| None | All | Cutoff and subsequent events | All sources are dated on or before 2026-11-05 (Q3 10-Q signed October 29, 2026; Q3 release October 28, 2026). Subsequent events are flagged and kept out of period figures: pension lump sums of 66 million in October 2026, repurchases of 649,378 shares to October 23, 2026, and the dividend payable December 8, 2026 | None | Treatment is correct |
| None | All | Extraction fidelity | Text extraction only; no chart or image inspected and no table-fidelity review beyond the checked cells | Record as a parse limit | Table cells outside the checked set are not independently reviewed |
| None | CP-1A, CP-2 | Management attribution | Outlook, guidance, prepayment cause, new client wins, dividend increases and strategy are labelled Management Language or attributed | None | Attribution is clear |
| None | CP-2 | Prohibited conclusions | No peer ranking, instrument recommendation or recovery conclusion appears | None | Compliant |
| None | CP-1A | Individuals | Governance rows assess issuer behaviour only; the insider-affiliated holding is stated as a documented disclosure without inference | None | Compliant |
| None | CP-1, CP-1A | Perimeter | All figures are consolidated; Bank and financing-business statements are not supplied and are flagged | Obtain if needed | Leverage mixes industrial and financing debt |

#### T5.8 Handoff component defects

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR (I-02, I-03) | CP-0 | Gap 5 locators; source-risk paragraph | Locators on the wrong page | Cite the pages that carry the figures | None |
| MINOR (I-04) | CP-0, CP-1, CP-1A, CP-2 | Litigation party description | Slightly beyond the note | Reword | CP-2 inherits |
| MINOR (I-05, I-06) | CP-1 | Interest cover chart note; cash flow interpretation | Coupon timing generalized; customer type inferred | Reword | CP-2 repeats the prepayment cause without the Presort label |
| MINOR (I-07) | CP-1A | Transaction summary | Date cited to a page that says first quarter | Cite page:59 | None |
| None | CP-1A | Accepted at attempt 2 | The first attempt was rejected because a summary figure was not repeated in the body; the accepted text repeats it | None | None |
| None | CP-2 | Selector sections | Prose-only key findings and strengths and weaknesses are present; confidence is Medium | None | None |

#### T5.9 Issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | MATERIAL | CP-0, CP-1, CP-1A, CP-2 | Unverifiable covenant, springing-test and legal structure | Covenant compliance is a management statement; reported ratios, definitions, amendments, guarantees, ranking and the liquidity term are not traceable to governing documents | Obtain the credit agreement, amendments, compliance certificate and indentures | Restricts committee use | Open |
| I-02 | MINOR | CP-0 | Locator | Tie-out of FY2025 comparatives cited to pages that do not carry the figures | Cite 10-K page:98 and page:66 and Q3 10-Q page:19 and page:3 | None | Open |
| I-03 | MINOR | CP-0 | Locator | 23,125 add-back cited to page:9; it is on page:10 | Cite page:10 | None | Open |
| I-04 | MINOR | CP-0, CP-1, CP-1A, CP-2 | Overstatement | Claimant described as parent of a former ecommerce vendor; the note does not say so | Reword to the note | None | Open |
| I-05 | MINOR | CP-1 | Unsupported generalization | Semi-annual coupons cited for cash interest timing; only the convertible's dates are printed | Reword | None | Open |
| I-06 | MINOR | CP-1 | Overstatement | Prepaying clients called Presort customers; the release says new customers after a sortation competitor exited | Reword | None | Open |
| I-07 | MINOR | CP-1A | Locator | February 2025 date cited to page:42; it is on page:59 | Cite page:59 | None | Open |

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_pbi-20251231.htm.jsonl | High: filed, audited statements | FY2025, with FY2024 and FY2023 comparatives | Pitney Bowes Inc., consolidated | Statements, Note 13 debt, covenants, leases, pensions, segments, business description, risk factors, exhibit index | Text extraction; a Form 10-K/A is cited elsewhere and is absent | All modules |
| S2 | 10-Q_2026-03-31_pbi-20260331.htm.jsonl | High: filed, unaudited | Q1 2026 | Consolidated | Position at 2026-03-31, debt table, cash interest, segment results | Text extraction | CP-1, CP-1A |
| S3 | 10-Q_2026-06-30_pbi-20260630.htm.jsonl | High: filed, unaudited | Q2 and first half 2026 | Consolidated | Position at 2026-06-30, debt table, revolver capacity, amendments | Text extraction | CP-1, CP-1A |
| S4 | 10-Q_2026-09-30_pbi-20260930.htm.jsonl | High: filed, unaudited | Q3 and nine months 2026 | Consolidated | Statements, Note 10, Note 11, Note 13, segments, liquidity, exhibits | Text extraction; signed October 29, 2026 | All modules |
| S5 | EX-99.1_2026-05-05_q12026earningspressrelea.htm.jsonl | Medium: management release, attributed | Q1 2026 | Consolidated and segments | Adjusted EBITDA and free cash flow reconciliations | Management measures | CP-1 |
| S6 | EX-99.1_2026-07-29_q22026earningspressrelea.htm.jsonl | Medium: management release, attributed | Q2 and first half 2026 | Consolidated and segments | Same | Management measures | CP-1 |
| S7 | EX-99.1_2026-10-28_ex991q32026earningspress.htm.jsonl | Medium: management release, attributed | Q3 and nine months 2026 | Consolidated and segments | Same, guidance, capital allocation | Management measures; guidance | CP-1, CP-1A, CP-2 |

#### T5B.2 Top credit drivers by materiality

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Springing maturity tied to the 2029 notes and 2030 convertible, and liquidity | CP-1, CP-2 | Notes of 476,000 and convertible of 230,000; test at redemption amount plus 100 million; cash 268,514 and capacity 427 million | Early maturity of the 294,450 term loan and revolver borrowings if liquidity is thin | The key funding event; sets the cushion for distributions | S4 pages 3, 19, 20 | Liquidity definition absent (I-01) |
| 2 | Leverage and earnings basis | CP-1, CP-2 | Principal 1,918,434; LTM Adjusted EBITDA 591,456; 3.24x and 2.79x; 3.38x and 2.90x on the 2025 definition | Sets debt capacity; the pension add-back changes the trend | Leverage tolerance | S1 page:84; S7 pages 8-9; S4 pages 10, 19 | FY2025 EBITDA calculated; assumption in the sensitivity |
| 3 | Presort margin and segment concentration | CP-1A, CP-2 | Presort adjusted segment EBIT 91,045 against 123,345; gross margin 31.6% against 37.2%; SendTech 351,243 | Second earnings pillar weakening | Earnings durability | S4 pages 9-10, 31-32 | Management attributes causes |
| 4 | Cash-flow quality and distributions | CP-1, CP-1A, CP-2 | Operating cash flow 348,212 including finance receivables 87,499; buybacks 205,725 and dividends 40,599 against debt reduction 107,778 | Cash generation partly self-liquidating; distributions exceed debt reduction | Capital allocation and liquidity | S4 pages 4, 19, 24, 39; S7 page:9 | Legal limits on distributions absent |
| 5 | Covenant headroom and legal capacity | CP-1, CP-1A, CP-2 | Three tests printed; compliance stated; no ratios | Governs facility access | Restricts conclusions | S4 page:20 | Credit agreement absent (I-01) |

#### T5B.3 Claim traceability register

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt principal 1,918,434 and carrying 1,887,421 at 2026-09-30 | CP-1 | S4 page:19, page:3 | Yes | High | Supported | Verified | High | Directly Sourced |
| Cash 268,514 and revolver capacity of 427 million | CP-1, CP-2 | S4 page:3, page:20 | Yes | High | Supported | Verified | High | Directly Sourced |
| Debt schedule by instrument and maturity wall | CP-1 | S4 page:19-20; S3 page:19; S2 page:18; S1 page:97-98 | Yes | High | Supported | Verified; labels conflict (T5.6) | High | Directly Sourced |
| Covenant tests and compliance statement | CP-1, CP-2 | S4 page:20 | Yes | High (attributed) | Supported | Verified as a statement; not testable (I-01) | Medium | Directly Sourced |
| Springing maturity provisions | CP-1, CP-2 | S4 page:20 | Yes | High | Supported | Verified; liquidity term undefined (I-01) | Medium | Directly Sourced |
| Segment results, nine months and Q3 | CP-1, CP-1A, CP-2 | S4 page:9-10, page:29-32 | Yes | High | Supported | Verified | High | Directly Sourced |
| Finance receivables 995,101 and run-off contribution 87,499 | CP-1, CP-1A, CP-2 | S4 page:3, page:4, page:11 | Yes | High | Supported | Verified | High | Directly Sourced |
| No client above 10% and USPS dependence | CP-1A, CP-2 | S1 page:51, page:12 | Yes | High | Supported | Verified | High | Directly Sourced |
| Ecommerce Restructuring and litigation claim | CP-1A, CP-2 | S1 page:85; S4 page:24 | Yes | High | Supported | Verified; party wording (I-04) | Medium | Directly Sourced |
| Claims outside debt: leases, pensions, deposits | CP-1, CP-2 | S1 page:102, 110, 116; S4 page:3 | Yes | High | Supported | Verified | High | Directly Sourced |
| FY2025 Adjusted EBITDA of 572,868 | CP-1, CP-2 | S1 page:84 and the release method | Yes | High | Derived | Reproduced | Medium | Calculated |
| LTM Adjusted EBITDA 591,456 and leverage 3.24x, 2.79x | CP-1, CP-2 | S5 page:7; S6 page:9; S7 page:9; S1 page:84 | Yes | High | Derived | Reproduced | Medium | Calculated |
| Cash interest cover 4.34x | CP-1, CP-2 | S1 page:96; S2 page:24; S3 page:26; S4 page:26 | Yes | High | Derived | Reproduced | Medium | Calculated |
| Buybacks and dividends against debt reduction | CP-1A, CP-2 | S4 page:4, page:19, page:24 | Yes | High | Derived | Reproduced | High | Calculated |
| Guidance implications for Q4 2026 | CP-2 | S7 page:2-3; derived Q4 2025 | Yes | Medium: management guidance | Derived | Reproduced; labelled implication | Medium | Calculated |
| Like-for-like Adjusted EBITDA excluding the pension add-back | CP-1, CP-2 | S4 page:9-10; S7 page:9 | Yes | High | Derived | Reproduced; assumes the 2025 base carried the cost | Low | Assumption-Based |
| Cushion of 119.5 against the springing threshold | CP-1, CP-2 | Cash plus capacity less 576.0 | Yes | n/a | Derived | Labelled not a test result | Low | Assumption-Based |
| Mail decline and slow predictable erosion of revenue | CP-1A, CP-2 | S4 page:30-31; S1 page:13 | Yes | High | Inferred | Reasonable reading of verified statements | Medium | Analyst Inference |
| Issuer behaviour on debt is supportive and on distributions mixed | CP-1A, CP-2 | S4 page:19-20; S1 page:31, 43 | Yes | High | Inferred | Reasonable reading of documented actions; capacity not assessable | Medium | Analyst Inference |
| Ownership and control rights | CP-1A, CP-2 | Absent; share count only (S4 page:1) | Yes | n/a | Gap | Insufficient evidence | Low | Insufficient Information |

#### T5B.4 Source locator register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt table: 476,000; 230,000; 294,450; 584,029; 25,441; 308,514; principal 1,918,434; carrying 1,887,421 | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:19, Note 10 | CP-1 debt schedule and maturities | Note | High | Verified |
| Revolver 450 million, capacity 427 million, covenants, springing provisions, amendments narrative | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:20, Note 10 | CP-1, CP-1A, CP-2 | Note | High | Verified; same text on page:36-37 |
| Convertible terms and guarantee | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:21-22, Note 10 | CP-1 debt schedule | Note | High | Verified |
| Cash 268,514; deposits 576,949 and 71,000; leases 29,725 and 87,595; total assets 2,992,280; deficit (836,737) | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:3, balance sheet | CP-1, CP-1A, CP-2 | Statement | High | Verified |
| Revenue, costs, pre-tax and net income, nine months and Q3 | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:2, income statement | CP-1 financials table | Statement | High | Verified |
| Cash from operations 348,212; capital expenditures; repurchases (205,725); dividends (40,599); principal payments (402,032) | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:4, cash flow | CP-1 financials table, roll-forward | Statement | High | Verified |
| Segment tables and reconciliation to pre-tax income | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:9-10, Note 3 | CP-1 EBITDA, CP-1A operating model | Note | High | Verified; 23,125 is on page:10 (I-03) |
| Future performance obligations 624,428 | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:8, Note 2 | CP-1A operating model | Note | High | Verified |
| Finance receivables, aging and credit quality | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:11, 14, Note 6 | CP-1, CP-1A | Note | High | Verified |
| Pension lump sums of 66 million and buy-out intention | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:23, Note 11 | CP-1, CP-1A | Note | High | Verified |
| Vendor-related suit seeking more than 100 million | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:24, Note 13 | CP-1A, CP-2 | Note | High | Verified; I-04 |
| Cash interest paid 114,025 and 119,863 | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:26, Note 16 | CP-1 interest cover | Note | High | Verified |
| Segment MD&A, gross margins, transportation cost | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:29-32 | CP-1A, CP-2 | MD&A | High | Verified |
| Allocated finance interest 8,466 | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:33 | CP-1 | MD&A | High | Verified |
| Cash 269 million, foreign 64 million; outlook | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:34 | CP-1, CP-2 | MD&A | High | Verified |
| Repurchase authorization and share table | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:38-39 | CP-1, CP-1A | Part II | High | Verified |
| Fifth Amendment dated September 29, 2026; first supplemental indenture dated March 2, 2026 | source-text/10-Q_2026-09-30_pbi-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:39, exhibits | CP-0, CP-1A | Exhibit | High | Verified; documents not supplied |
| Third and Fourth Amendments | source-text/10-Q_2026-06-30_pbi-20260630.htm.jsonl | 10-Q Q2 2026 | S3 | page:40, exhibits | CP-0, CP-1A | Exhibit | High | Verified |
| Debt table at 2026-06-30; capacity 330 million; March 2031 maturity | source-text/10-Q_2026-06-30_pbi-20260630.htm.jsonl | 10-Q Q2 2026 | S3 | page:19-20, Note 10 | CP-1 liquidity, conflicts | Note | High | Verified |
| Cash interest paid 72,188 and 71,923 | source-text/10-Q_2026-06-30_pbi-20260630.htm.jsonl | 10-Q Q2 2026 | S3 | page:26 | CP-1 interest cover | Note | High | Verified |
| Debt table at 2026-03-31; margin 1.85% | source-text/10-Q_2026-03-31_pbi-20260331.htm.jsonl | 10-Q Q1 2026 | S2 | page:18, Note 10 | CP-1 conflicts | Note | High | Verified |
| Cash interest paid 46,021 and 49,273 | source-text/10-Q_2026-03-31_pbi-20260331.htm.jsonl | 10-Q Q1 2026 | S2 | page:24 | CP-1 interest cover | Note | High | Verified |
| Statements FY2025 and FY2024 | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:64-67 | CP-1 financials table | Statement | High | Verified |
| Segment reconciliation FY2025: 577,466; 116,173; 149,156; depreciation 111,575 | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:84, segment note | CP-1 Adjusted EBITDA | Note | High | Verified |
| Debt table 2,026,212 and annual maturities | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:97-98, 101, Note 13 | CP-1 | Note | High | Verified |
| Credit agreement, new term loans, revolver 400 million | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:42-43 | CP-1, CP-1A | MD&A | High | Verified; date on page:59 (I-07) |
| Letters of credit about 27 million | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:45 | CP-1 liquidity | MD&A | High | Verified |
| Exhibit index: credit agreement dated February 7, 2025; indentures | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:56-59 | CP-0, CP-1A | Exhibit | High | Verified |
| Cash interest paid 142,107 | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:96, Note 11 | CP-1 interest cover | Note | High | Verified |
| Pension funded status; retiree medical; leases | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:102, 110, 116 | CP-1 claims table | Note | High | Verified |
| Business description, USPS dependence, mail decline, activism, management change | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:5-9, 12-13, 17, 23 | CP-1A | Item 1, Item 1A | High | Verified |
| Ecommerce Restructuring and DIP Facility | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:85, Note 4 | CP-1A | Note | High | Verified |
| Insider-affiliated trading arrangement | source-text/10-K_2025-12-31_pbi-20251231.htm.jsonl | 10-K FY2025 | S1 | page:53, Item 9B | CP-1A | Item 9B | High | Verified |
| Adjusted EBITDA reconciliation, Q3 and nine months | source-text/EX-99.1_2026-10-28_ex991q32026earningspress.htm.jsonl | Q3 2026 release | S7 | page:9 | CP-1 | Reconciliation | Medium | Verified; management measure |
| Debt reduction 148 and 108 million; term loan repricing; dividend | source-text/EX-99.1_2026-10-28_ex991q32026earningspress.htm.jsonl | Q3 2026 release | S7 | page:1 | CP-1, CP-1A, CP-2 | Narrative | Medium | Verified |
| Guidance and prepayment statement | source-text/EX-99.1_2026-10-28_ex991q32026earningspress.htm.jsonl | Q3 2026 release | S7 | page:2-3 | CP-1, CP-2 | Narrative | Medium | Verified; attributed |
| Adjusted EBITDA reconciliation, Q2 and six months | source-text/EX-99.1_2026-07-29_q22026earningspressrelea.htm.jsonl | Q2 2026 release | S6 | page:9 | CP-1 | Reconciliation | Medium | Verified |
| Adjusted EBITDA reconciliation, Q1 | source-text/EX-99.1_2026-05-05_q12026earningspressrelea.htm.jsonl | Q1 2026 release | S5 | page:7 | CP-1 | Reconciliation | Medium | Verified |

#### T5B.5 Calculation register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adjusted EBIT equals segment EBIT less corporate expenses, all six quarters and nine-month totals | CP-1 | Q1: 152,708 and 22,331; Q2: 142,684 and 26,631; Q3: 146,896 and 32,980; 2025: 151,806 and 32,117; 137,195 and 34,902; 133,685 and 26,350 | 130,377; 116,053; 113,916; 119,689; 102,293; 107,335, each equal to the printed Adjusted EBIT | Reproduced | Verified | High | Validates the method for FY2025 | S5 page:7; S6 page:8-9; S7 page:8-9 |
| Adjusted EBITDA equals Adjusted EBIT plus depreciation and amortization | CP-1 | 130,377 + 25,641; 116,053 + 23,687; 113,916 + 22,734; 119,689 + 28,324; 102,293 + 28,762; 107,335 + 27,418 | 156,018; 139,740; 136,650; 148,013; 131,055; 134,753, each equal to the printed figure | Reproduced | Verified | High | Validates the method | S5 page:7; S6 page:9; S7 page:9 |
| FY2025 Adjusted EBITDA | CP-1, CP-2 | 577,466; 116,173; 111,575 | (577,466 - 116,173) + 111,575 = 572,868 | Reproduced | Verified | Medium | Leverage and cover denominator | S1 page:84 |
| FY2025 reconciliation to pre-tax income | CP-1 | 577,466; 116,173; 149,156; 58,392; 268; 14,072; 21,944; 12,758; 12,179 | 192,524 equal to printed | Reproduced | Verified | High | Supports the FY2025 method | S1 page:84, page:65 |
| LTM Adjusted EBITDA Q1, Q2, Q3 2026 | CP-1, CP-2 | 572,868 with 156,018 and 148,013; 295,758 and 279,068; 432,408 and 413,820 | 580,873; 589,558; 591,456 | Reproduced | Verified | Medium | Denominator | S5, S6, S7 |
| Leverage on principal | CP-1, CP-2 | Principal 2,026,212; 2,172,675; 2,066,839; 1,918,434; cash 284,887; 302,876; 266,833; 268,514 | 3.54x and 3.04x; 3.74x and 3.22x; 3.51x and 3.05x; 3.24x and 2.79x | Reproduced | Verified | Medium | Leverage | S1 page:98, 65; S2 page:18, 2; S3 page:19, 3; S4 page:19, 3 |
| Leverage on carrying value | This module | Carrying 1,993,038 and 1,887,421 | FY2025 3.48x and 2.98x; Q3 3.19x and 2.74x | Computed here | Verified | Medium | Basis check | S1 page:98; S4 page:19 |
| Leverage on the 2025 definition | CP-1, CP-2 | 591,456 less 23,125 = 568,331 | 3.38x and 2.90x | Reproduced | Labelled sensitivity | Low | Trend comparability | S4 page:10; S5 to S7 |
| Cash interest cover | CP-1, CP-2 | 572,868 and 142,107; 580,873 and 138,855; 589,558 and 142,372; 591,456 and 136,269 | 4.03x; 4.18x; 4.14x; 4.34x | Reproduced | Verified | Medium | Coverage | S1 page:96; S2 page:24; S3 page:26; S4 page:26 |
| Debt principal roll-forward | CP-1 | 2,026,212 + 150,000 + 150,000 - 346,700 - 9,550 - 4,538 - 6,225 - 40,765 | 1,918,434; implied discount 5,746 over 402,032 paid | Reproduced; discount inferred | Verified; inference labelled | Medium | Debt activity | S4 page:19, page:4 |
| Liquidity and springing-test arithmetic | CP-1, CP-2 | 268,514 + 427,000; 476,000 + 100,000; 230,000 + 100,000 | 695,514; 576,000; 330,000; cushions 119,514 and 365,514 | Reproduced | Labelled not a test result | Low | Cushion | S4 page:3, 20 |
| Distributions against debt reduction | CP-1A, CP-2 | 205,725 + 40,599; 378,361 + 51,059; 2,026,212 - 1,918,434 | 246,324; 429,420; 107,778 | Reproduced | Verified | High | Capital allocation | S4 page:4, 19; S1 page:67 |
| Guidance implications | CP-1, CP-2 | Guidance 380 to 420 and 450 to 470; nine-month 338,763 and 360,346; derived Q4 2025 211,944 and 131,976 | 41.2 to 81.2; 89.7 to 109.7; against 211.9 and 132.0 | Reproduced | Labelled implication | Medium | Q4 expectations | S7 page:2-3, 9; S1 page:67 |
| Revenue, segment and margin recomputes | CP-1A | 928,132 + 456,961; 351,243 over 928,132; 91,045 over 456,961 | 1,385,093; 37.8%; 19.9% | Reproduced | Verified | High | Operating model | S4 page:9 |
| Finance receivables quality | CP-2 | 956,675 and 12,753 over 1,256,473 | 76.1% and 1.0% | Reproduced | Verified | High | Asset quality | S4 page:11, 14 |
| Total interest and allocated finance interest | CP-1 | 80,556 + 27,077; 8,466 + 25,984; 149,156 - 101,460 | 107,633; 34,450; 47,696 (inferred split for FY2025) | Reproduced | Verified; FY2025 split inferred | Medium | Interest | S4 page:33; S1 page:84, 65 |
| Claims outside debt | CP-1 | 50,225 + 40,341 + 76,199; 29,725 + 87,595 | 166,765; 117,320 | Reproduced | Verified | High | Non-debt claims | S1 page:102, 110; S4 page:3 |

#### T5B.6 Weak, inferred or untraced items

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Like-for-like Adjusted EBITDA of 568,331 and ratios of 3.38x and 2.90x | Assumes the 2025 base carried the equivalent pension cost; prior periods not recast | Assumption-Based | It changes the earnings trend reading | Obtain recast 2025 figures | CP-1 leverage sensitivity; CP-2 key findings |
| MINOR | Cushion of 119.5 against the springing threshold | Uses cash plus capacity as liquidity; the definition is absent | Assumption-Based | Informs the funding-event reading | Obtain the credit agreement | CP-1 definitions table; CP-2 |
| MINOR | Revenue erodes slowly and predictably | Interpretation of verified statements and a management outlook | Analyst Inference | Frames business risk | None beyond labelling | CP-1A, CP-2 |
| MINOR | Supportive debt behaviour and mixed distribution behaviour | Reading of documented actions; legal capacity not assessable | Analyst Inference | Informs creditor alignment | Obtain debt documents | CP-1A governance table; CP-2 |
| MINOR | Implied discount of 5,746 on repurchased notes | Inference from cash paid against principal retired | Analyst Inference | Explains the tender gain wording | Obtain the tender results | CP-1 roll-forward |
| MINOR | Allocated financing interest of 47,696 for FY2025 | Inferred split; the 10-K prints no amount | Analyst Inference | Total interest basis | None | CP-1 calculations |
| MINOR | Ownership and control | No holder table or proxy | Insufficient Information | Alignment not assessable | Obtain the proxy statement | CP-1A, CP-2 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locator accuracy | Strong, three slips | 242 located figures matched; locator defects I-02, I-03, I-07 | A wrong page slows verification but not the figure | None on values | Fix the three locators |
| Quote fidelity | Strong | 78 of 78 quoted spans found in the cited source text | Misquoted language would misstate terms | Terms of the covenants and springing provisions are quoted correctly | None |
| Calculation reproducibility | Strong | All derived figures recompute, including FY2025 Adjusted EBITDA on a method that ties for six quarters | Reproducible inputs prevent silent drift | Leverage and cover can be relied on within stated bases | None |
| Perimeter consistency | Consistent | All figures consolidated; the Bank and financing business are flagged | A guarantor perimeter would differ | Structural position unassessed | Obtain guarantor data |
| Period labelling | Consistent | Fiscal years, LTM, nine months and quarters labelled | Mixed periods distort ratios | Comparisons are valid | None |
| Subsequent events | Correct | October 2026 lump sums and repurchases flagged | Blending would overstate period figures | Flagged, not blended | None |
| Management against filing | Clear | Release measures attributed; filings control | A management measure could override a filing | Guidance and the prepayment cause are attributed | None |
| Conflict handling | Adequate | Four conflicts logged, not reconciled | Smoothing would hide basis risk | Maturity and cost precision limited | Keep both readings |
| Currency and units | Consistent | USD; thousands converted to millions to one decimal | Unit slips distort ratios | None | None |

#### T5B.8 Gap register

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant ratios, definitions of liquidity, EBITDA and secured net debt, amendments | Credit agreement and all amendments, compliance certificate | Governs facility access and the springing tests | Headroom Not calculable; cushion indicative only | Restricts committee use (I-01) | Credit agreement |
| G2 | Guarantors, security and note terms | Indentures, guarantor list, security documents | Ranking and structural position | Ranking column unverified | Lowers confidence on structure | Indentures |
| G3 | Form 10-K/A | The amended annual report | Any amended FY2025 content | FY2025 labelled per the Form 10-K | Medium | Form 10-K/A |
| G4 | Ownership and control | Proxy statement, holder register | Alignment and control | Not assessable | Low | Proxy statement |
| G5 | Recast 2025 on the 2026 pension definition; Q4 2025 release | Recast figures; fourth-quarter release | Earnings trend and LTM base | Sensitivity only; FY2025 calculated | Medium | Issuer releases |
| G6 | Stand-alone Bank and financing statements; location of group cash | Segment-level cash and debt | Cash availability and perimeter | Consolidated basis only | Medium | Issuer data |
| G7 | Litigation accrual and pleadings; settlement documents for the vendor dispute | Court documents | Size and timing of the claim | Unquantified | Low | Court filings |
| G8 | Presentations and chart content | Decks and CEO letters | Visual content not reviewed | Parse limit | Low | Issuer presentations |

## Calculations

All amounts are in thousands of USD unless stated. Inputs are from the cited pages; results were recomputed in this module with a script that reads the printed values.

### Debt basis check

Balance-sheet carrying debt at 2026-09-30 is current portion 24,730 plus long-term debt 1,862,691, giving 1,887,421 (Q3 10-Q page:3), equal to principal 1,918,434 less unamortized costs 31,013 (page:19). On carrying value, 1,887,421 over LTM Adjusted EBITDA of 591,456 is 3.19x and net debt (1,887,421 less 268,514, or 1,618,907) over 591,456 is 2.74x, against 3.24x and 2.79x on principal; the basis moves each ratio by about 0.05x. At 2025-12-31: carrying 1,993,038 over 572,868 is 3.48x and net (1,993,038 less 284,887, or 1,708,151) over 572,868 is 2.98x, against 3.54x and 3.04x on principal.

### Adjusted EBITDA reproduction

The release method (total adjusted segment EBIT less corporate expenses, plus depreciation and amortization) reproduces every printed Adjusted EBITDA: Q1 2026 130,377 + 25,641 = 156,018; Q2 2026 116,053 + 23,687 = 139,740; Q3 2026 113,916 + 22,734 = 136,650; Q1 2025 119,689 + 28,324 = 148,013; Q2 2025 102,293 + 28,762 = 131,055; Q3 2025 107,335 + 27,418 = 134,753. The 2026 quarters sum to 432,408, equal to the nine-month figure; the 2025 quarters sum to 413,821 against 413,820, a rounding difference of 1. Applied to the 10-K, FY2025 is (577,466 - 116,173) + 111,575 = 572,868, and the same items reconcile to pre-tax income of 192,524. LTM Q3 2026 is 572,868 + 432,408 - 413,820 = 591,456.

### Leverage and cover recomputation

Principal over LTM Adjusted EBITDA: 2,026,212 over 572,868 is 3.54x; 2,172,675 over 580,873 is 3.74x; 2,066,839 over 589,558 is 3.51x; 1,918,434 over 591,456 is 3.24x. Net: 1,741,325 over 572,868 is 3.04x; 1,869,799 over 580,873 is 3.22x; 1,800,006 over 589,558 is 3.05x; 1,649,920 over 591,456 is 2.79x. Cash interest cover: 572,868 over 142,107 is 4.03x; 580,873 over 138,855 is 4.18x; 589,558 over 142,372 is 4.14x; 591,456 over 136,269 is 4.34x. All agree with the financial base.

### Locator audit

Seventy-eight quoted spans in the four handoffs were searched in the cited source text after normalizing whitespace and quotation marks; all were found on the pages named. Located figures were checked against the page cited on the same line: 242 matched, 107 did not match the cited page and were each reviewed. The 107 are derived results (sums, differences and ratios), figures cited on another page of the same row, or rounded forms of printed figures, except for the two numeric locator slips logged as I-02 and I-03; I-07 concerns a date and was found on a separate read of the exhibit index. Decimal figures in millions in the financial tables were checked against the printed thousands on the cited pages; all matched except derived rows. The pages named in the locator register were opened and the values listed there found.

### Confidence score

Formula: score equals (0.6 times E plus 0.4 times C) times S less P, clamped to 0 to 100 and capped by findings. E is the mean strongest lineage weight over 20 material claims: 10 Directly Sourced at 1.0, 5 Calculated at 0.9, 2 Assumption-Based at 0.5, 2 Analyst Inference at 0.4 and 1 Insufficient Information at 0.0, giving 81.5. C is 17 required registers present of 17, giving 100. S is 1.0 (source gate pass: all seven sources and the context were supplied and read). P is 15 for one MATERIAL finding plus 18 for six MINOR findings, giving 33. Score equals (0.6 times 81.5 plus 40) times 1.0 less 33, or 55.9, rounded to 56. A MATERIAL finding caps the score at 59 and sets Restricted; 56 is below the cap and falls in the Low band (40 to 59).

## Gaps

The open gaps are G1 to G8 in the gap register above. The ones that decide committee use are the credit agreement with all amendments and the compliance certificate (G1), the indentures and guarantor list (G2) and the Form 10-K/A (G3). The seven defects (one material, six minor) are listed in the issue log (I-01 to I-07); only I-01 restricts use, and none changes a figure. Nothing in the sources is dated after the cutoff of 2026-11-05, and the later filings that would address G1 to G3 cannot be used in this run if dated after it.

## Next module

This is the last selected module; CP-OS assembles the report from the accepted handoffs. Before relying on the report for covenant, springing-maturity, ranking or legal-capacity conclusions, obtain the credit agreement with all amendments, the latest compliance certificate, the indentures with the guarantor list and the Form 10-K/A, and apply fixes I-02 to I-07 in any rerun of the source-readiness, financial base and business-context handoffs.
