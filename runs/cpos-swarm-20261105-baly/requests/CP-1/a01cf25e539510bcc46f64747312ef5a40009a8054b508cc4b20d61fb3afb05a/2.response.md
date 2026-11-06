# CP-1 — Financial base: Bally's Corp (baly)

## Request

- Issuer: Bally's Corp (issuer id `baly`; the filings name the registrant "Bally’s Corporation"), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD. Current period Q2 2026 (quarter and six months ended June 30, 2026); prior period FY2025.
- Run `baly-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This module builds the financial base for the report sections that need statements, debt, liquidity, maturities, leverage and interest cover.
- Execution: host session; no provider was called. Every figure below is printed in the pinned sources or calculated here from printed figures, with the formula shown under Calculations.
- Locators: `page:N` is the pinned source chunk, not the printed page. Labels: 10-K = FY2025 annual report; Q3-25 10-Q, Q1-26 10-Q, Q2-26 10-Q = quarterly reports; Q4-25 release, Q1-26 release, Q2-26 release = the Exhibit 99.1 files.
- Units: statement figures in US$ thousands unless a cell says US$m or x. Foreign-currency debt is shown in the filing's USD carrying amounts, with principal currency noted.
- Upstream: the source readiness handoff (CP-0) is consumed. It set the restrictions carried here: Successor and Predecessor periods are not comparable, parent group and Bally’s Intralot debt are separate borrower groups, and no credit agreement or filing after August 14, 2026 is supplied.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_baly-20251231.htm.jsonl | 2416bb6463c147a405baaa3764d6b99dd0f04403aa6bd66a1af2136569a6e954 | FY2025 audited statements, debt note, Adjusted EBITDA reconciliation |
| 10-Q_2025-09-30_baly-20250930.htm.jsonl | 56bb4ccb0d42545489eded0e33ef5cc1b6e43986515a8c8a0964234c0c5a1ad2 | September 30, 2025 balance sheet, Q3 2025 and nine-month 2024 and 2025 comparatives |
| 10-Q_2026-03-31_baly-20260331.htm.jsonl | 4cf63f6c58a65fd25da3815352379f245d409f7447d9868c7381e2ae8ff65e16 | March 31, 2026 balance sheet, Q1 2026 and Q1 2025 comparatives |
| 10-Q_2026-06-30_baly-20260630.htm.jsonl | 972ae065bf1c6675d8214b94858dd8284ab57f02cd1acc546c671e0cb75a811b | June 30, 2026 statements, debt note, going concern note, liquidity |
| EX-99.1_2026-03-16_ex991q42025earningsrelease.htm.jsonl | 409058f48783e9f5b7a8a00d5cc7ac8351ce41c9bc84bcf81e7c679d11a21bfd | Preliminary Q4 2025 release (supporting, not controlling) |
| EX-99.1_2026-05-18_ex991q12026earningsrelease.htm.jsonl | 7a189d9a918a76f21f04890e1c9f027b4cb34b6b08652098f8604b464b20f405 | Q1 2026 release (supporting) |
| EX-99.1_2026-08-14_ex991q22026earningsrelease.htm.jsonl | d7b82a85199a3932febed54513d2e10fb96188bb07713475fd80698b0568c17c | Q2 2026 release (supporting) |
| context | 49e5852827798fdbde43be3fcd478e45f6e9875c774c07cb1f9810d5a929f053 | Run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 |
| --- | --- |
| CP-0 | e78906951f2c40cb4061b9e3feea4b5ce91ea92011923fb2276960d5a3adc0a6 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| At June 30, 2026 gross debt was 9.57x last-twelve-month Adjusted EBITDA and net debt 8.81x. Adjusted EBITDA covered cash interest 1.15x. The latest filing carries a going concern warning and a covenant waiver. | Medium | Last-twelve-month figures add split merger periods and count Intralot debt in full but its lottery and Turkey earnings only from October 2025; leases sit outside debt. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Gross debt to last-twelve-month Adjusted EBITDA rose from 8.88x at September 30, 2025 to 9.57x at June 30, 2026. | Leverage is high and rests on a non-GAAP measure over a changing perimeter, so comparison across dates is indicative only. | Medium |
| Adjusted EBITDA cover of cash interest fell from 1.41x at September 30, 2025 to 1.15x at June 30, 2026. | Thin cover leaves little room for lower earnings or higher rates, and a pay-in-kind option exists on the new term loan. | Medium |
| Cash fell from 798.4 at December 31, 2025 to 390.2 at June 30, 2026 (US$m); the revolver is to shrink from October 2026. | Liquidity depends on financings not yet committed, and consolidated cash is not split between the parent group and Bally’s Intralot. | Medium |
| Q2 2026 revenue rose to 792.2 (US$m) while Adjusted EBITDA fell to 124.0 from 129.2. | Growth did not convert to earnings, which matters because the lender waiver and the going concern conclusion rest on forecast liquidity. | High |
| Lease liabilities of 2,392,267 thousand and the Bronx project sit outside the 4,910,068 thousand debt figure. | Fixed lease rent and uncommitted project funding rank alongside debt service as claims on cash. | High |

### Financial base view

The reported financial base is usable for leverage, cover, liquidity and maturity analysis, with firm limits. Debt, cash, maturities, cash paid for interest, Adjusted EBITDA and its reconciliation are all printed in filed documents, so the ratios below are calculated only from printed figures. The ratios are not like-for-like across dates. Reported 2025 amounts are split at the February 7, 2025 merger, so each last-twelve-month figure is a sum of a Predecessor stub and Successor periods. The Intralot group debt entered the balance sheet in the fourth quarter of 2025 and is counted in full at each later date, while the Intralot B2B earnings count only from October 8, 2025, so leverage at the later dates is higher than a pro forma view would show; the sources do not provide that view. Adjusted EBITDA is after cash rent on triple net operating leases, so operating lease liabilities are excluded from debt for consistency, and are shown separately. The June 30, 2026 liquidity position and the unfinished financing plans described in the going concern note are the main credit issue; the ratios describe the burden, not the headroom under any covenant, because the covenant definitions are not supplied.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| LTM Q3 2025 (September 30, 2025) | 8.88 | 8.54 | x | Total debt is contractual principal of 4,250,063 thousand (Q3-25 10-Q page:38). Net debt deducts unrestricted cash of 160,689 thousand. EBITDA is issuer Adjusted EBITDA, calculated as FY2024 plus nine months 2025 less nine months 2024; Predecessor stub and Successor period are summed. Intralot debt and earnings are not yet consolidated at this date. |
| FY2025 (December 31, 2025) | 9.84 | 8.25 | x | Total debt is principal of 4,943,767 thousand (10-K page:170). EBITDA is Successor period 478,009 plus Predecessor stub 24,390. Cash of 798,423 thousand sits alongside accrued liabilities of 500,000 thousand for the New York license fee and 115,000 thousand of contingent consideration, both paid in Q1 2026 (10-K page:162), and net debt excludes these claims. Intralot B2B earnings count only from October 8, 2025. |
| LTM Q1 2026 (March 31, 2026) | 9.32 | 8.24 | x | Total debt is principal of 4,828,826 thousand (Q1-26 10-Q page:48). Net debt deducts cash of 559,304 thousand. EBITDA is FY2025 combined plus Q1 2026 less Q1 2025 combined. Same perimeter and period-split limits. |
| LTM Q2 2026 (June 30, 2026) | 9.57 | 8.81 | x | Total debt is principal of 4,910,068 thousand (Q2-26 10-Q page:37). Net debt deducts cash of 390,184 thousand. EBITDA is FY2025 combined plus six months 2026 less six months 2025 combined. Cash includes Bally’s Intralot cash; the parent and Intralot split is not supplied. Leases are excluded. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| LTM Q3 2025 (September 30, 2025) | 1.41 | x | Issuer Adjusted EBITDA over cash paid for interest, net of amounts capitalized, both calculated as FY2024 plus nine months 2025 less nine months 2024 (Q3-25 10-Q page:6; 10-K page:110). |
| FY2025 (December 31, 2025) | 1.32 | x | Adjusted EBITDA 502,399 thousand over cash interest 379,808 thousand, each the sum of Successor period and Predecessor stub (10-K page:80, page:110). |
| LTM Q1 2026 (March 31, 2026) | 1.27 | x | Same basis, FY2025 combined plus Q1 2026 less Q1 2025 combined (Q1-26 10-Q page:5, page:71). |
| LTM Q2 2026 (June 30, 2026) | 1.15 | x | Same basis, FY2025 combined plus six months 2026 less six months 2025 combined (Q2-26 10-Q page:6, page:60). Cash interest excludes paid-in-kind interest of 9,518 thousand capitalized to debt in the six months and the 2026 term loan PIK option; it is net of capitalized interest. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| September 30, 2025 | 160.7 | Not supplied: availability net of letters of credit is not printed; commitments of 620.0 less 393.0 drawn is 227.0 before any letters of credit | US$m | Unrestricted cash only; restricted cash of 79.2 is excluded (Q3-25 10-Q page:2). Revolver commitment and drawn amount from page:38 and page:40. Bally’s Intralot not yet consolidated. |
| December 31, 2025 | 798.4 | 776.1 | US$m | Cash 798,423 thousand (Q2-26 10-Q page:2). Undrawn is 588.1 reported revolver availability (10-K page:64) plus Bally’s Intralot revolver 160.0 million euros converted at the implied rate in the 10-K, about 188.0. The 10-K itself states 190.0 million euros unused (about 223.2); the Q1-26 10-Q restates the December 31, 2025 figure as 160.0 million euros, which is used here. |
| March 31, 2026 | 559.3 | 367.0 | US$m | Cash 559,304 thousand. Undrawn is 183.6 reported revolver availability (Q1-26 10-Q page:41) plus Bally’s Intralot revolver 160.0 million euros, about 183.4 at the implied rate; no borrowings or letters of credit there (page:80). |
| June 30, 2026 | 390.2 | 304.3 | US$m | Cash 390,184 thousand (Q2-26 10-Q page:2). Undrawn is 195.8 reported revolver availability (page:33) plus Bally’s Intralot revolver 95.0 million euros, about 108.5, calculated as 160.0 commitments less 65.0 drawn. Letters of credit under the Intralot revolver at this date are not printed. Intralot cash and facilities are not available to the parent group by guarantee: page:11 states that Bally’s Intralot does not guarantee any of Bally’s Corporation’s debt. Restricted cash of 97.6 is excluded. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remaining 2026 | 95.670 | US$m | Contractual principal at June 30, 2026 (Q2-26 10-Q page:37). The revolver tranche split between October 2026 and October 2028 is not printed in the schedule. |
| 2027 | 45.688 | US$m | Same schedule. |
| 2028 | 282.323 | US$m | Same schedule. |
| 2029 | 1006.996 | US$m | Same schedule. The 1,109.518 term loans due February 11, 2031 mature March 1, 2029 instead if the 2029 Notes are still outstanding then (page:32 footnote 1); the Thereafter row appears to carry them: it equals the instruments due 2031 and later, including these loans, within 1 thousand. |
| 2030 | 74.243 | US$m | Same schedule; matches the Bally’s Intralot revolver drawn balance, whose maturity is July 1, 2030 (page:31). |
| Thereafter | 3405.148 | US$m | Same schedule. Total of all rows is 4,910.068, which equals the principal total. |

### Financials and credit metrics

| Line | Q2 2026 (three months) | Six months 2026 | FY2025 (Successor plus Predecessor, calculated) | LTM Q2 2026 (calculated) | Basis and locator |
| --- | --- | --- | --- | --- | --- |
| Revenue | 792,234 | 1,547,956 | 2,656,687 | 2,957,917 | Q2-26 10-Q page:3; 10-K page:76 (2,436,189 plus 220,498) |
| Adjusted EBITDAR | 187,515 | 366,446 | 677,296 | 722,846 | Q2-26 10-Q page:48; 10-K page:80 (637,237 plus 40,059) |
| Rent expense, triple net operating leases | (63,481) | (119,128) | (174,897) | (210,036) | Same pages (159,228 plus 15,669 for FY2025) |
| Adjusted EBITDA (issuer non-GAAP) | 124,034 | 247,318 | 502,399 | 512,810 | Q2-26 10-Q page:60; 10-K page:80 (478,009 plus 24,390) |
| Net loss | (163,982) | (324,839) | (716,563) | (796,458) | Q2-26 10-Q page:3; 10-K page:80 ((665,539) plus (51,024)) |
| Interest expense, net of interest income | 118,970 | 228,875 | 392,462 | 444,849 | Q2-26 10-Q page:3; 10-K page:80 (365,233 plus 27,229) |
| Cash paid for interest, net of amounts capitalized | Not supplied: cash flow statement is cumulative | 220,037 | 379,808 | 444,640 | Q2-26 10-Q page:6; 10-K page:110 (340,739 plus 39,069) |
| Net cash (used in) provided by operating activities | Not supplied: cumulative only | (265,936) | (91,200) | (335,749) | Q2-26 10-Q page:5; 10-K page:109 ((11,014) plus (80,186)). Six months 2026 includes up-front licensing payments of 98,906 |
| Capital expenditures | Not supplied: cumulative only | 73,954 | 184,293 | 162,401 | Q2-26 10-Q page:5; 10-K page:109 |
| Cash paid for capitalized software | Not supplied: cumulative only | 19,227 | 37,783 | 34,162 | Same pages |
| Cash and cash equivalents (balance sheet date) | 390,184 at June 30, 2026 | Not applicable: balance sheet date | 798,423 at December 31, 2025 | Not applicable: balance sheet date | Q2-26 10-Q page:2 |
| Restricted cash (balance sheet date) | 97,587 | Not applicable: balance sheet date | 108,263 | Not applicable: balance sheet date | Q2-26 10-Q page:2; unavailable for the company’s use (page:13) |
| Debt principal, all instruments | 4,910,068 | Not applicable: balance sheet date | 4,943,767 | Not applicable: balance sheet date | Q2-26 10-Q page:37; 10-K page:170 |
| Debt carrying amount, including current portion | 4,506,700 | Not applicable: balance sheet date | 4,500,657 | Not applicable: balance sheet date | After original issue discount of 51,969 and fair value adjustment of 351,399 (page:31) |
| Operating lease liabilities (current plus long-term) | 2,392,267 | Not applicable: balance sheet date | 1,933,837 | Not applicable: balance sheet date | Q2-26 10-Q page:2 (126,763 plus 2,265,504 at June 30, 2026; 104,647 plus 1,829,190 at December 31, 2025) |
| Non-controlling interest | 1,525,228 | Not applicable: balance sheet date | 1,550,172 | Not applicable: balance sheet date | Q2-26 10-Q page:2 |
| Total debt / EBITDA (x) | Not applicable: LTM metric | Not applicable: LTM metric | 9.84 | 9.57 | Calculated; see Calculations |
| Net debt / EBITDA (x) | Not applicable: LTM metric | Not applicable: LTM metric | 8.25 | 8.81 | Calculated |
| EBITDA / cash interest (x) | Not applicable: LTM metric | Not applicable: LTM metric | 1.32 | 1.15 | Calculated |

### Source and period basis

- Statements located: audited FY2025 statements in the 10-K (page:106 to page:110); unaudited interim statements at September 30, 2025, March 31, 2026 and June 30, 2026 (page:2 to page:6 of each 10-Q). Q2-26 10-Q page:10 sets the basis: "a Predecessor period, which includes the period from January 1, 2025 through February 7, 2025". The 10-K audit opinion at page:102 covers "from February 8, 2025 to December 31, 2025 (successor), from January 1, 2025 to February 7, 2025 (predecessor)".
- Controlling source: the filings. The Q4-25 release is labelled preliminary (page:1 "reported preliminary financial results"); the Q2-26 release repeats the 10-Q debt table (page:8) and adds only a pro forma combined view for six months 2025.
- Internal control: the 10-K auditor reports an adverse internal control opinion (10-K page:102 "expressed an adverse opinion on the Company's internal control over financial reporting because of a material weakness"). Figures remain audited statements with an unqualified financial statement opinion (10-K page:194).
- Currency: reporting USD. Intralot debt is in GBP and EUR, remeasured to USD (Q2-26 10-Q page:32); the USD amounts move with exchange rates. No separate currency or period conflict with the context was found.

### Segment base (Q2 2026 against Q2 2025)

| Segment | Revenue Q2 2026 | Revenue Q2 2025 | Adjusted EBITDAR Q2 2026 | Adjusted EBITDAR Q2 2025 |
| --- | --- | --- | --- | --- |
| Casinos & Resorts | 401,017 | 393,333 | 109,611 | 105,967 |
| Bally’s Intralot B2B | 79,488 | 7,046 | 21,931 | 7,046 |
| Bally’s Intralot B2C | 243,481 | 199,020 | 64,739 | 75,159 |
| North America Interactive | 66,064 | 56,502 | 2,994 | 2,484 |
| Corporate & Other | 2,184 | 1,633 | (11,760) | (17,506) |
| Total | 792,234 | 657,534 | 187,515 | 173,150 |

Source: Q2-26 10-Q page:48. In US$m, Q2 2026 revenue was 792.2 against 657.5 a year earlier, while Adjusted EBITDA was 124.0 against 129.2. Segment Adjusted EBITDAR is the issuer’s segment measure. Rent of 63,481 against 43,904 a year earlier takes Adjusted EBITDA to 124,034 against 129,246 (page:48, page:60). The Q2-26 release attributes about 39 million of gross negative B2C EBITDAR impact to the UK gaming tax change from April 1, 2026 (Q2-26 release page:3 "approximately $39 million in the quarter"); this is a management claim.

### Debt by instrument at June 30, 2026

| Instrument | Issuer or borrower | Principal (US$ thousands) | Rate | Maturity | Security and guarantors |
| --- | --- | --- | --- | --- | --- |
| 2026 Term Loans | Bally’s Corporation | 1,109,518 | Term SOFR (3.0% floor) plus 7.5%, or base rate plus 6.5%; up to 3.5% may be paid in kind (page:34) | February 11, 2031; March 1, 2029 if 2029 Notes outstanding (page:32) | Senior secured, pari passu with the revolver; guaranteed by certain restricted subsidiaries |
| Revolving Credit Facility | Bally’s Corporation | 303,750 drawn | SOFR or base rate plus margin; margins raised by Amendment No. 4 (page:33) | Tranches in October 2026 and October 2028 (page:33) | First-priority lien; guaranteed by restricted subsidiaries. Commitments about 519.3 million, 195.8 million available |
| 5.625% Senior Notes due 2029 | Escrow issuers, unrestricted subsidiaries of the company | 750,000 | 5.625% | September 1, 2029 | Guaranteed by certain restricted subsidiaries that guarantee the credit agreement (page:32) |
| 5.875% Senior Notes due 2031 | Same | 735,000 | 5.875% | September 1, 2031 | Same; 750.0 million was issued, 735.0 million is carried and the filing does not explain the difference |
| Intralot British Term Loan | Intralot Capital Luxembourg S.A. | 530,277 (GBP 400.0 million) | SONIA plus 5.5% | October 8, 2031 | First-ranking security including share pledges |
| Intralot Greek Term Loan | Intralot Capital | 228,441 (EUR 200.0 million) | 7.0% fixed; amortizing | October 8, 2029 | Secured by substantially all assets of Intralot Capital and guarantors |
| Intralot Revolving Credit Facility | Intralot Capital | 74,243 (EUR 65.0 million) | Reference rate plus 4.50% | July 1, 2030 | Super senior; commitments EUR 160.0 million |
| Intralot Greek Retail Bond | Bally’s Intralot | 148,487 (EUR 130.0 million) | 6.00% fixed | February 27, 2029 | Unsecured with a pledged collateral account; not guaranteed by subsidiaries |
| Intralot Fixed Rate Notes | Intralot Capital | 685,323 (EUR 600.0 million) | 6.75% | October 15, 2031 | Senior secured; guaranteed by Bally’s Intralot |
| Intralot Floating Rate Notes | Intralot Capital | 342,661 (EUR 300.0 million) | 3-month EURIBOR plus 4.500%; 6.824% at June 30, 2026 | October 15, 2031 | Same |
| Intralot Supplemental Indenture | Not stated | 2,368 (EUR 2.073 million) | Not supplied | September 15, 2050 | Not supplied |
| Total principal | | 4,910,068 | | | Less original issue discount 51,969 and fair value adjustment 351,399 gives carrying 4,506,700 |

Sources: Q2-26 10-Q page:31 to page:37. The Bally’s Intralot instruments are obligations of a majority-owned subsidiary; page:11 states "Bally’s Intralot does not guarantee any of Bally’s Corporation’s debt". Whether Bally’s Corporation or its restricted group guarantees Intralot debt is not stated in the pages read. Hedges: the Q2-26 release footnotes currency and rate swaps on the repaid Term Loan Facility (page:9); the current hedge position after the February 2026 repayment is not supplied.

### Claims outside the debt figure

- Operating leases. Lease liabilities are 2,392,267 thousand, all operating (Q2-26 10-Q page:39 "total operating lease liabilities of $2.39 billion"). Undiscounted minimum payments are 4.12 billion, of which 142.6 million falls in the current year (page:69). Rent on triple net operating leases is deducted in Adjusted EBITDA; cash paid for these leases was 133,561 thousand in six months 2026 (Q2-26 release page:8). The Bally’s Twin River sale-leaseback of February 11, 2026 added 56.0 million of annual rent (page:39). Chicago: the master lease starts at 20.0 million initial annual rent plus 8.5% of advances up to 940.0 million (page:69), with 274,034 thousand of advances received in six months 2026 (page:40).
- Non-debt obligations on the balance sheet at December 31, 2025 included the New York gaming license fee of 500,000 and contingent consideration of 115,000 thousand (10-K page:162); both were paid in Q1 2026 (Q2-26 release page:2). A conveyance liability of 183.6 million for Ferry Point capital improvements was recognized in 2026 (Q2-26 10-Q page:25), with improvements of about 161.0 million required (page:44). A bond or cash deposit of 5% of total project investment is required (page:44).
- Bronx project: the release describes a 4.0 billion project (Q2-26 release page:2 "The $4.0 billion Bally’s Bronx integrated casino project"). Funding beyond the license fee is not committed; a pre-construction loan term sheet is non-binding (Q2-26 10-Q page:11).
- Rhode Island: a 100.0 million investment commitment to 2043, with about 39.0 million remaining (page:44).
- Other: deferred payables 27.7 million (page:13); contingent consideration remaining 8.9 million (page:30); Bally’s Intralot total return swap for up to 50.0 million euros of its own shares (page:28); 11,619,725 penny warrants (page:41); litigation losses not material (page:43). Pensions: benefit plan balances in accumulated other comprehensive income are 18 thousand (page:42), so pensions are not material. Factoring and supply chain finance: a search of all seven sources found no such arrangement.

### Liquidity and covenant facts

- Revolver: commitments were reduced to about 519.3 million in February 2026; from October 2026 total availability falls to about 319 million; 195.8 million was available at June 30, 2026 (Q2-26 10-Q page:33). Commitments less borrowings is 215.55 million, so 19.75 million of commitments is neither drawn nor reported as available; the filing does not say why, and letters of credit are not named.
- Financial covenant: when utilization exceeds 25% of commitments, the revolver requires "a first lien secured net indebtedness to Adjusted EBITDA ratio of 4.00 to 1.00" (Q2-26 10-Q page:65). Utilization at June 30, 2026 was 303,750 of about 519,300, above the threshold. The Q2-26 10-Q page:37 describes it as a "maximum first lien net leverage ratio" and the 10-K had a 30% threshold (page:165). The reported covenant figure is not supplied, so headroom is Not calculable.
- Waiver: in May 2026 the required lenders conditionally waived the "consolidated net leverage ratio covenant" from the quarter ended March 31, 2026 to the Covenant Waiver Period (page:38). It depends on minimum liquidity, limits on additional secured debt and an agreement to amend the revolver. The minimum liquidity level is Not supplied.
- Going concern: Q2-26 10-Q page:11 states the conditions "raise substantial doubt about the Company’s ability to continue as a going concern", and management’s plans (asset monetization, an equity sale, debt financings) "do not alleviate substantial doubt". The company "does not project that it would satisfy the liquidity maintenance requirement" absent the financings. This language is not in the 10-K or the Q1-26 10-Q.
- Intralot covenants: a total net leverage ratio not exceeding 4.75:1.00 and a tested senior secured net leverage ratio (page:38); the company was in compliance at June 30, 2026 (page:38).
- Subsequent events dated before August 14, 2026: a sterling term facilities agreement of 261.8 million pounds signed July 27, 2026 by Intralot Capital (page:37); a non-binding Bronx loan term sheet in July 2026 (page:11); Fifth Amendment to the Credit Agreement dated July 29, 2026 (page:74), terms Not supplied.

### Definition review

- Adjusted EBITDA: issuer measure, earnings before interest, taxes, depreciation and amortization, non-operating items, transaction costs, share-based compensation and other items (Q2-26 release page:5). In the reconciliation it is Adjusted EBITDAR less rent on triple net operating leases (Q2-26 10-Q page:48). It is not a covenant EBITDA; the credit agreement definition is not supplied.
- EBITDA in the ratios above means this issuer Adjusted EBITDA. Total debt means contractual principal of all instruments in the debt note, including the revolver and the Bally’s Intralot instruments, and excludes lease liabilities. Net debt deducts unrestricted cash only.
- Covenant leverage tests (first lien net) use secured debt only and credit-agreement definitions; the metrics here are total and net consolidated measures and do not equal them.

## Calculations

All inputs are printed figures in US$ thousands unless stated. Locators are in the tables above.

### Adjusted EBITDA, last twelve months

- FY2025 combined: 478,009 + 24,390 = 502,399 (10-K page:80).
- LTM Q3 2025: FY2024 495,611 + nine months 2025 (343,113 + 24,390 = 367,503) − nine months 2024 384,261 = 478,853 (10-K page:80; Q3-25 10-Q page:70).
- LTM Q1 2026: 502,399 + 123,284 − (83,271 + 24,390 = 107,661) = 518,022 (Q1-26 10-Q page:71).
- LTM Q2 2026: 502,399 + 247,318 − (212,517 + 24,390 = 236,907) = 512,810 (Q2-26 10-Q page:60). Check: 123,284 + 124,034 = 247,318, which equals the six-month figure printed.

### Cash paid for interest, last twelve months

- FY2025 combined: 340,739 + 39,069 = 379,808.
- LTM Q3 2025: 314,245 + (243,341 + 39,069 = 282,410) − 256,161 = 340,494.
- LTM Q1 2026: 379,808 + 109,134 − (42,339 + 39,069 = 81,408) = 407,534.
- LTM Q2 2026: 379,808 + 220,037 − (116,136 + 39,069 = 155,205) = 444,640.

### Debt principal and net debt

- June 30, 2026: 1,109,518 + 530,277 + 228,441 + 303,750 + 74,243 + 148,487 + 750,000 + 735,000 + 685,323 + 342,661 + 2,368 = 4,910,068, equal to the maturity schedule total. Carrying: 4,910,068 − 51,969 − 351,399 = 4,506,700. Net debt: 4,910,068 − 390,184 = 4,519,884.
- December 31, 2025: 1,472,594 + 538,720 + 234,962 + 152,726 + 750,000 + 735,000 + 704,886 + 352,443 + 2,436 = 4,943,767. Net debt: 4,943,767 − 798,423 = 4,145,344.
- March 31, 2026: sum of the Q1-26 10-Q page:39 instruments = 4,828,826. Net debt: 4,828,826 − 559,304 = 4,269,522.
- September 30, 2025: 1,872,063 + 393,000 + 500,000 + 750,000 + 735,000 = 4,250,063. Net debt: 4,250,063 − 160,689 = 4,089,374.

### Ratios (x)

| Date | Total debt / EBITDA | Net debt / EBITDA | EBITDA / cash interest |
| --- | --- | --- | --- |
| September 30, 2025 | 4,250,063 / 478,853 = 8.88 | 4,089,374 / 478,853 = 8.54 | 478,853 / 340,494 = 1.41 |
| December 31, 2025 | 4,943,767 / 502,399 = 9.84 | 4,145,344 / 502,399 = 8.25 | 502,399 / 379,808 = 1.32 |
| March 31, 2026 | 4,828,826 / 518,022 = 9.32 | 4,269,522 / 518,022 = 8.24 | 518,022 / 407,534 = 1.27 |
| June 30, 2026 | 4,910,068 / 512,810 = 9.57 | 4,519,884 / 512,810 = 8.81 | 512,810 / 444,640 = 1.15 |

### Other last-twelve-month lines

- Revenue: 2,656,687 + 1,547,956 − (1,026,228 + 220,498 = 1,246,726) = 2,957,917. FY2025: 2,436,189 + 220,498 = 2,656,687.
- Adjusted EBITDAR: 637,237 + 40,059 = 677,296; LTM 677,296 + 366,446 − (280,837 + 40,059 = 320,896) = 722,846.
- Rent: 159,228 + 15,669 = 174,897; LTM 174,897 + 119,128 − (68,320 + 15,669 = 83,989) = 210,036. Check: 722,846 − 210,036 = 512,810.
- Net loss: (665,539) + (51,024) = (716,563); LTM (716,563) + (324,839) − ((193,920) + (51,024) = (244,944)) = (796,458).
- Interest expense, net: 365,233 + 27,229 = 392,462; LTM 392,462 + 228,875 − (149,259 + 27,229 = 176,488) = 444,849.
- Operating cash flow: (11,014) + (80,186) = (91,200); LTM (91,200) + (265,936) − (58,799 + (80,186) = (21,387)) = (335,749).
- Capital expenditures: 167,869 + 16,424 = 184,293; LTM 184,293 + 73,954 − (79,422 + 16,424 = 95,846) = 162,401. Capitalized software: 35,468 + 2,315 = 37,783; LTM 37,783 + 19,227 − (20,533 + 2,315 = 22,848) = 34,162.
- Adjusted EBITDA margin Q2: 124,034 / 792,234 = 15.7%; Q2 2025: 129,246 / 657,534 = 19.7%.

### Liquidity (US$m)

- Implied euro rate at June 30, 2026: 74,243 / 65,000 = 1.1422 (Intralot revolver carrying over euro principal). Intralot undrawn: (160.0 − 65.0) × 1.1422 = 108.5. Total undrawn: 195.8 + 108.5 = 304.3.
- March 31, 2026: implied rate 149,048 / 130,000 = 1.1465 (Greek Retail Bond). 160.0 × 1.1465 = 183.4; total 183.6 + 183.4 = 367.0.
- December 31, 2025: implied rate 152,726 / 130,000 = 1.1748. 160.0 × 1.1748 = 188.0; total 588.1 + 188.0 = 776.1. With the 10-K figure of 190.0: 223.2; total 811.3.
- Revolver: 519.3 − 303.75 = 215.55; less reported available 195.8 = 19.75 unexplained.
- Maturity rows in US$m are the printed thousands divided by 1,000.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement definitions, waiver terms, minimum liquidity level and the reported covenant ratio are not supplied; covenant headroom is Not calculable | High | CP-2 | Supply the Credit Agreement, Amendments No. 3 to No. 5 and the Conditional Waiver |
| Last-twelve-month ratios sum Predecessor and Successor periods and mix the Intralot debt and earnings perimeter; no pro forma is supplied | High | CP-2, CP-5 | Obtain pro forma Intralot earnings or label ratios indicative |
| Split of consolidated cash and undrawn facilities between the parent group and Bally’s Intralot is not supplied; Intralot letters of credit at June 30, 2026 not printed | High | CP-2 | Obtain group-level cash and facility balances |
| 10-K states 190.0 million euros unused under the Intralot revolver at December 31, 2025; the Q1-26 10-Q states 160.0 million euros for the same date | Medium | CP-2 | Confirm commitments at December 31, 2025 |
| 19.75 million between revolver commitments less borrowings and reported availability is unexplained | Medium | CP-2 | Confirm letters of credit and other usage |
| Revolver availability at September 30, 2025 net of letters of credit not printed | Low | CP-2 | Use December 31, 2025 onward |
| Cash interest excludes paid-in-kind interest and the 2026 term loan allows a 3.5% PIK portion; total interest burden at the full cash margin is not shown | Medium | CP-2 | Model PIK election |
| Nothing after August 14, 2026; Fifth Amendment terms, Bronx financing outcome, evoke consideration and any equity sale are Not supplied | High | CP-1A, CP-2 | Supply later filings |
| Hedge positions after the February 2026 term loan repayment, and the 2031 Notes difference between issued 750.0 million and carried 735.0 million, are not explained | Low | CP-2 | Check the Notes indenture and derivative note |
| Q4 2025 discrete quarter not built; the release is preliminary | Low | CP-1A | Calculate as FY2025 Successor less nine-month Successor if needed |

## Next module

- CP-1A: use the segment base above and the debt table for the corporate structure; carry the Intralot perimeter as the main structural fact and keep the terms of the going concern, waiver and financing plans as sourced statements.
- CP-2: start from the liquidity position, waiver conditions and October 2026 revolver reduction; do not treat the ratios here as covenant ratios; carry the gaps on definitions, perimeter, cash split and the euro revolver conflict.
- CP-5: verify the calculated rows against the cited pages; the calculated rows are LTM sums, ratios, implied euro conversions and the liquidity totals.
