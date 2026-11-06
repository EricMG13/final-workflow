## Request

Issuer: Skeena Resources Ltd (issuer id ske; registrant Skeena Resources Limited), a development-stage mining company building the Eskay Creek gold-silver project in British Columbia. As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit_snapshot. Reporting currency: CAD; the statements are in thousands of Canadian dollars ("CAD thousands" below) unless a US$ amount is printed. Current period per context: q2-2026 (three and six months ended June 30, 2026, balance sheet at June 30, 2026); prior period: fy-2025 (balance sheet at December 31, 2025).

Scope of this module: extract and label the reported financial base, build the leverage, interest cover, liquidity and maturity tables the report selectors require, list all debt and non-debt claims, and state what the sources do and do not support. Calculations are shown separately from reported facts. Abbreviations for locators: "Q2 FS" is the condensed interim statements for the three and six months ended June 30, 2026 (6-K Exhibit 99.2 filed 2026-08-13); "Q1 FS" is the same for the three months ended March 31, 2026 (filed 2026-05-15); "Q3 2025 FS" is the same for the three and nine months ended September 30, 2025 (filed 2025-11-13). Locators are extraction pages, `page:N`, not printed pages.

The upstream readiness handoff is consistent with this answer and is not corrected: it rated this module READY_WITH_LIMITATIONS, with full-year 2025 statements, management discussion and legal terms outstanding. Those remain gaps below.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Use in this module |
| --- | --- | --- |
| 6-K-EX-99.2_2026-08-13_ske-20260813xex99d2.htm.jsonl | f089cfed7c41a13c1124e873c8cf9d986ddb809584e80594413f338c0cb3dda8 | Primary: balance sheet June 30, 2026 and December 31, 2025; three and six month income and cash flows; notes on instruments, debt, financing package, royalties, closure |
| 6-K-EX-99.2_2026-05-15_ske-20260515xex99d2.htm.jsonl | 23892a03c3bd6fd8f48bf0d8bc66e12cf89a073a244322844de1eee4158909d7 | Three months ended March 31, 2026 cross-checks; Gold Stream terms and covenants; April 2026 notes event |
| 6-K-EX-99.2_2025-11-13_ske-20251113xex99d2.htm.jsonl | a3b00c87d028f94b90bcea93f3fd8fe3b7d050af714766a40adae75d64ae2545 | Earlier period context only (September 30, 2025); no figure from it is used in the tables |
| 40-F_2025-12-31_ske-20251231x40f.htm.jsonl | db53ff9f8d0ca28c9b2edfb7202c651bb5c9ec8c989c923bb91bcc11481dd65e | Currency convention and the fact that the audited statements are incorporated by reference but not in the pack |
| 6-K-EX-99.1_2026-03-24_exh_991.htm.jsonl | 2c276dba594c2df305ad125f0ece05f65167118a8d8060b6fa5d7edae3ae61ff | Reviewed; narrative only, no financial figures used |
| 6-K-EX-99.1_2026-05-15_ske-20260515xex99d1.htm.jsonl | 232a824d9608ba6939a5237ea02786aae7b7f6f4a3ef441bec526b8439fdd718 | Reviewed; narrative only, no financial figures used |
| 6-K-EX-99.1_2026-08-13_ske-20260813xex99d1.htm.jsonl | c4db22929f19fe544f88a7604e2308cdbc32700c4f1804f3c24f0271e5a2ab28 | Reviewed; narrative only, no financial figures used |

### Context file (settings, not issuer evidence)

| Item | sha256 |
| --- | --- |
| context file for ske, as of 2026-11-05 | 74622c0ba0b18d4f8697485a569e78b3429cdc3e20d2499bc2bcfcfddaa82602 |

### Supplied handoffs

| Module | sha256 | How used |
| --- | --- | --- |
| CP-0 | 23917a29a2f37939f380db919ecc804a68465820c252ef088859ee05682dfc5a | Source readiness: perimeter (single consolidated registrant, no guarantors or restricted group named), CAD thousands basis, unaudited interim status, and the list of absent documents (annual statements, management discussion, annual information form, indenture and agreements) |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| This pre-revenue developer funded construction with a US$750,000,000 note issue in April 2026. At June 30, 2026 unrestricted cash was 134,808 (CAD thousands) and restricted cash 500,853. No EBITDA exists, so leverage and cover ratios are not calculable. | Medium | Unaudited interim statements only; no full-year 2025 flows, no EBITDA, no cash interest paid for the half-year, and no legal terms for the notes. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Senior Secured Notes of US$750,000,000 at 8.50% due April 1, 2031 are carried at 1,055,969 (CAD thousands), net of an embedded derivative asset; gross amortized cost is 1,082,552. | Fixed-rate secured debt now anchors the capital structure; the gross amortized cost is the figure to use for debt comparisons. | High |
| Unrestricted cash of 134,808 sits beside restricted cash of 500,853 held in construction disbursement and interest reserve accounts. | Only the unrestricted amount is freely available; access to restricted funds depends on release conditions that are not supplied. | Medium |
| Six-month 2026 operating cash outflow was 30,235 and additions to mineral property were 203,600, funded by financing and not by operations. | Liquidity depends on the notes' proceeds and on the cost to complete, which the pack does not state. | High |
| Claims outside the notes include a Gold Stream derivative liability of 209,286, royalty liabilities of 78,709 and 136,009, leases of 66,483 and a closure provision of 104,777. | These add fixed and contingent claims on project cash flow; the notes rank pari passu with the Gold Stream obligations. | Medium |
| No revenue, EBITDA or cash interest paid is reported for the half-year. | Leverage and interest cover cannot be calculated; the credit view must rest on liquidity and funding coverage. | High |

### Financial base view

Skeena is a development-stage company with no revenue line in any retained statement, so the financial base is a funding and liquidity base, not an earnings base. At June 30, 2026 the company had completed the April 10, 2026 offering of US$750,000,000 Senior Secured Notes (stated as 1,036,761 CAD thousands at issue), used part of the proceeds to repurchase 66.67% of the Gold Stream, and placed the interest reserve and construction disbursement proceeds in restricted accounts. The consolidated balance sheet at that date shows unrestricted cash of 134,808, restricted cash of 500,853, long-term debt carrying value of 1,055,969 and total liabilities of 1,746,295 against shareholders' equity of 170,801 (CAD thousands). The net loss for the six months ended June 30, 2026 was 139,677, including a 41,736 fair value loss on the Gold Stream derivative and a 17,684 foreign exchange loss; operating cash outflow was 30,235 and additions to mineral property, plant and equipment were 203,600 for the same six months. Because earnings measures do not exist, the report's leverage and interest cover chart cells are Not supplied, and the funding picture is read from cash, restricted cash, the maturity table and the construction commitments. The limits are material: the statements are unaudited, FY2025 full-year flows and the audited notes are not in the pack, cash interest paid for the half-year is not stated, and neither the legal terms of the notes nor the cost to complete is supplied. Debt figures that involve US dollar balances move with exchange rates, and the company states that it does not use derivatives to reduce exposure to foreign exchange risk (Q2 FS, page:10).

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q2 2026 (balance sheet June 30, 2026; six months ended June 30, 2026) | Not supplied: no EBITDA is reported and no revenue is presented, so the denominator does not exist | Not supplied: no EBITDA is reported and no revenue is presented, so the denominator does not exist | x | Numerators exist (gross notes 1,082,552 CAD thousands; see Calculations) but no earnings measure; six-month loss before tax was 139,677. Unaudited. Q2 FS page:1, page:2, page:7. |
| FY2025 (balance sheet December 31, 2025) | Not supplied: no EBITDA is reported and no full-year 2025 income statement is in the pack | Not supplied: no EBITDA is reported and no full-year 2025 income statement is in the pack | x | No long-term debt at December 31, 2025 (Q2 FS page:1); lease liabilities only. Annual statements are not in the pack. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q2 2026 (six months ended June 30, 2026) | Not supplied: no EBITDA is reported and cash interest paid for the period is not stated | x | Interest and finance fee expense was 19,851 CAD thousands (Q2 FS page:2). The Q1 FS states no interest on long-term debt was paid in the three months ended March 31, 2026 (page:15); the Q2 FS states no equivalent for the half-year. Part of interest is capitalized (Q2 FS page:11). |
| FY2025 (year ended December 31, 2025) | Not supplied: no EBITDA is reported and no full-year 2025 statements are in the pack | x | No borrowings were outstanding at December 31, 2025 (Q2 FS page:1). |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q2 2026 (June 30, 2026) | Not supplied: reported in CAD thousands | Not supplied: reported in CAD thousands; no undrawn committed facility is disclosed | US$m | Unrestricted cash and cash equivalents 134,808 CAD thousands; restricted cash 500,853 CAD thousands (current 453,925, non-current 46,928); total 635,661 (Calculation 2). The US$350,000,000 Senior Secured Term Loan was terminated on April 10, 2026 and the additional Gold Stream deposit option was cancelled (Q2 FS page:14; Q1 FS page:11). Q2 FS page:1, page:7. |
| FY2025 (December 31, 2025) | Not supplied: reported in CAD thousands | Not supplied: reported in CAD thousands; the US$350,000,000 term loan facility was undrawn but its availability conditions are not supplied | US$m | Cash and cash equivalents 121,889 CAD thousands; no restricted cash. The facility had no draws at March 31, 2026 (Q1 FS page:9) and was terminated on April 10, 2026. Q2 FS page:1. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Within 1 year of June 30, 2026 | Not supplied: reported in CAD thousands | US$m | Undiscounted long-term debt cash flows 88,581 CAD thousands; basis is the undiscounted financial liabilities table, which is not split between principal and interest (Q2 FS page:11). |
| 1 to 5 years from June 30, 2026 | Not supplied: reported in CAD thousands | US$m | Undiscounted long-term debt cash flows 1,428,200 CAD thousands; includes the US$750,000,000 principal due April 1, 2031, which falls inside this bucket, and interest (Q2 FS page:11, page:12). |
| More than 5 years from June 30, 2026 | Not supplied: reported in CAD thousands | US$m | No long-term debt cash flow is shown (the cell is a dash, Q2 FS page:11). |
| Maturity year 2031 (April 1, 2031) | Not supplied: reported in CAD thousands | US$m | Single bullet maturity of the Senior Secured Notes, principal US$750,000,000 stated as 1,036,761 CAD thousands at issue; non-callable for the first two years (Q2 FS page:12). Annual split of maturities is not given beyond the three buckets. |

### Financials and credit metrics

| Line | Period | Amount (CAD thousands unless stated) | Locator | Basis and limitation |
| --- | --- | --- | --- | --- |
| Cash and cash equivalents | June 30, 2026 | 134,808 | Q2 FS page:1 | Unrestricted; balance sheet date |
| Cash and cash equivalents | December 31, 2025 | 121,889 | Q2 FS page:1 | Balance sheet date |
| Restricted cash, current | June 30, 2026 | 453,925 | Q2 FS page:1 | Interest reserve and construction disbursement proceeds (Q2 FS page:12) |
| Restricted cash, non-current | June 30, 2026 | 46,928 | Q2 FS page:1 | Same; total restricted cash 500,853 (Q2 FS page:7) |
| Total current assets | June 30, 2026 | 612,167 | Q2 FS page:1 | Includes current restricted cash |
| Total current assets | December 31, 2025 | 158,992 | Q2 FS page:1 | Balance sheet date |
| Mineral property, plant and equipment | June 30, 2026 | 1,211,192 | Q2 FS page:1 | December 31, 2025: 559,573 |
| Total assets | June 30, 2026 | 1,917,096 | Q2 FS page:1 | December 31, 2025: 770,191 |
| Accounts payable and accrued liabilities | June 30, 2026 | 84,739 | Q2 FS page:1 | December 31, 2025: 70,057 |
| Long-term debt, current portion | June 30, 2026 | 89,352 | Q2 FS page:1, page:13 | Net of embedded derivative asset; none at December 31, 2025 |
| Long-term debt, non-current | June 30, 2026 | 966,617 | Q2 FS page:1, page:13 | Net of embedded derivative asset; none at December 31, 2025 |
| Long-term debt carrying value, net | June 30, 2026 | 1,055,969 | Q2 FS page:13 | Gross amortized cost 1,082,552 less embedded derivative asset 26,583 |
| Long-term debt, gross amortized cost | June 30, 2026 | 1,082,552 | Q2 FS page:7, page:13 | US$743,067 thousand of long-term debt in US dollars (Q2 FS page:10) |
| Fair value of the Senior Secured Notes | June 30, 2026 | 1,119,655 | Q2 FS page:8 | Estimated from trading value of the bonds; carrying amount stated as 1,055,969 |
| Embedded derivative asset in long-term debt | June 30, 2026 | 26,583 | Q2 FS page:13 | Fair value through profit or loss; inception value 15,953 |
| Lease liabilities, current | June 30, 2026 | 17,316 | Q2 FS page:1 | December 31, 2025: 15,751 |
| Lease liabilities, non-current | June 30, 2026 | 49,167 | Q2 FS page:1 | December 31, 2025: 47,333 |
| Gold Stream derivative liability | June 30, 2026 | 209,286 | Q2 FS page:1, page:8, page:15 | December 31, 2025: 421,902; Level 3 fair value |
| NSR Royalty liability (current 237, non-current 78,472) | June 30, 2026 | 78,709 | Q2 FS page:1, page:16 | Amortized cost; none at December 31, 2025 |
| Additional NSR Royalty liability | June 30, 2026 | 136,009 | Q2 FS page:1, page:16 | Amortized cost liability component of the option; none at December 31, 2025 |
| Provision for closure and reclamation | June 30, 2026 | 104,777 | Q2 FS page:1, page:16 | December 31, 2025: 46,227 |
| Total current liabilities | June 30, 2026 | 194,097 | Q2 FS page:1 | December 31, 2025: 87,470 |
| Total liabilities | June 30, 2026 | 1,746,295 | Q2 FS page:1 | December 31, 2025: 611,067 |
| Total shareholders' equity | June 30, 2026 | 170,801 | Q2 FS page:1 | December 31, 2025: 159,124 |
| Net loss and comprehensive loss | Three months ended June 30, 2026 | 35,220 | Q2 FS page:2 | Three months ended June 30, 2025: 36,033; unaudited |
| Net loss and comprehensive loss | Six months ended June 30, 2026 | 139,677 | Q2 FS page:2 | Six months ended June 30, 2025: 74,281; unaudited |
| General and administration expenses | Three months ended June 30, 2026 | 22,610 | Q2 FS page:1 | Three months ended June 30, 2025: 13,721; six months 2026: 43,418; six months 2025: 22,644 |
| Interest and finance fee expense | Three months ended June 30, 2026 | 14,102 | Q2 FS page:2 | Three months ended June 30, 2025: 634 |
| Interest and finance fee expense | Six months ended June 30, 2026 | 19,851 | Q2 FS page:2 | Six months ended June 30, 2025: 1,536 |
| Change in fair value of Gold Stream derivative liability | Three months ended June 30, 2026 | (12,653) | Q2 FS page:1 | Printed as a credit (gain); three months ended June 30, 2025: loss 29,794 |
| Change in fair value of Gold Stream derivative liability | Six months ended June 30, 2026 | 41,736 | Q2 FS page:1 | Loss; six months ended June 30, 2025: loss 60,004 |
| Foreign exchange loss | Six months ended June 30, 2026 | 17,684 | Q2 FS page:2 | Three months ended June 30, 2026: 17,416; six months ended June 30, 2025: 369 |
| Loss per share, basic and diluted | Six months ended June 30, 2026 | (1.14) | Q2 FS page:2 | CAD per share; six months ended June 30, 2025: (0.66) |
| Net cash used in operating activities | Three months ended June 30, 2026 | (15,057) | Q2 FS page:3 | Three months ended June 30, 2025: (1,685) |
| Net cash used in operating activities | Six months ended June 30, 2026 | (30,235) | Q2 FS page:3 | Six months ended June 30, 2025: (38,699) |
| Additions to mineral property, plant and equipment | Three months ended June 30, 2026 | (131,352) | Q2 FS page:3 | Three months ended June 30, 2025: (64,389) |
| Additions to mineral property, plant and equipment | Six months ended June 30, 2026 | (203,600) | Q2 FS page:3 | Six months ended June 30, 2025: (93,412); a further 75,178 of additions sat in accounts payable at June 30, 2026 (Q2 FS page:18) |
| Construction prepayments and deposits paid | Six months ended June 30, 2026 | (9,144) | Q2 FS page:3 | Three months ended June 30, 2026: (4,324) |
| Exercise of Gold Stream buy-down option | Three and six months ended June 30, 2026 | (254,352) | Q2 FS page:3 | Investing outflow, US$184,000 thousand |
| Proceeds from long-term debt | Three and six months ended June 30, 2026 | 353,593 | Q2 FS page:3 | Net of the amounts placed in restricted accounts (Q2 FS page:12) |
| Restricted cash released | Three and six months ended June 30, 2026 | 199,176 | Q2 FS page:3 | Presented in financing activities; US$145,000 thousand |
| Prepayment of royalty obligations | Three and six months ended June 30, 2026 | (25,000) | Q2 FS page:3 | Financing outflow |
| Lease payments | Six months ended June 30, 2026 | (8,521) | Q2 FS page:3 | Three months ended June 30, 2026: (4,296) |
| Net cash provided by financing activities | Six months ended June 30, 2026 | 510,221 | Q2 FS page:3 | Three months ended June 30, 2026: 514,403 |
| Cash interest paid | Six months ended June 30, 2026 | Not supplied | Q2 FS page:18 | The supplemental disclosure states income tax payments only; no cash flow line for interest paid. The Q1 FS (page:15) states none was paid in the three months ended March 31, 2026 |
| Revenue | Any period | Not supplied | Q2 FS page:1, page:2 | No revenue line is presented in any retained statement |
| EBITDA | Any period | Not supplied | Q2 FS, all pages | Not reported by the issuer; not calculated here (see Calculations) |
| Contractual commitments, total undiscounted | June 30, 2026 | 168,356 | Q2 FS page:11 | Within 1 year 138,109; 1-5 years 22,372; more than 5 years 7,875; may contain cancellation clauses |
| Total undiscounted financial liabilities and commitments | June 30, 2026 | 2,321,075 | Q2 FS page:11 | Within 1 year 316,513; 1-5 years 1,656,428; more than 5 years 348,134 |

### Debt and financing instruments

- **Senior Secured Notes.** Issuer Skeena Resources Limited; no co-issuer is named in the retained pages. Principal US$750,000,000 ("$1,036,761,000 (US$750,000,000)" at issue), 8.50% per annum payable semi-annually, maturing April 1, 2031, non-callable for the first two years, senior secured and ranking pari passu with the Gold Stream obligations (Q2 FS page:12). Redemption: before April 1, 2028 at 100% plus the greater of 1% and a make-whole premium of 50 basis points over the treasury yield, up to 10% at 103%, and up to 40% with equity proceeds at 108.5%; from April 1, 2028 at 104.25% until March 31, 2029, 102.125% until March 31, 2030 and 100% thereafter; change of control put at 101%; asset sale excess proceeds offer (Q2 FS page:12, page:13). Effective interest rate 8.57% (Q2 FS page:13). Guarantors, collateral package, financial covenants and the release conditions for restricted cash: Not supplied (the indenture is not in the pack, and a search of every source for "guarantor", "covenant", "indenture" and "collateral" found none for the notes).
- **Senior Secured Term Loan facility.** US$350,000,000, no draws, terminated April 10, 2026 (Q2 FS page:14). Not a current source of liquidity.
- **Gold Stream.** Derivative liability at fair value through profit or loss. After the April 10, 2026 buy-down of 66.67% for US$184,000,000 (254,352 CAD thousands), the Stream Percentage is 3.52% of payable gold for the life of the mine, rising if the completion test is not met by September 30, 2027 (Q2 FS page:14). Before the buy-down the percentage was 10.55% (Q1 FS page:10). Counterparty is named Orion in the Q1 FS (page:10). Security and covenants are described in the Q1 FS (page:10, page:11) and are discussed under Covenants below.
- **NSR royalty and Additional NSR Royalty Option.** A 1% NSR royalty subject to a minimum paid value of 100,000 CAD thousands and capped at the first 5,000,000 gold equivalent ounces sold, and an option to elect an additional 1.5% royalty, or common shares (2,900,001), or mixed combinations (Q2 FS page:15). Liability components are at amortized cost (Q2 FS page:16). A prepayment of 25,000 was made in the quarter (Q2 FS page:16).
- **Leases and equipment loans.** Lease liabilities 66,483 in total at June 30, 2026. The company also entered into "various vehicle and equipment leases and loan financing" (Q2 FS page:12); the balance of any equipment loans is not separately stated.
- **Co-issuers, other guarantors and subsidiary-level debt:** Not supplied. The statements are consolidated for a single registrant and name no restricted or unrestricted subsidiary group.

### Claims outside the debt figure

| Claim | Amount (CAD thousands) | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Gold Stream derivative liability | 209,286 | Outside long-term debt of 1,082,552 gross; a separate fair value liability | Q2 FS page:1 |
| NSR Royalty liability | 78,709 | Outside; separate amortized cost liability | Q2 FS page:16 |
| Additional NSR Royalty liability | 136,009 | Outside; separate amortized cost liability | Q2 FS page:16 |
| Lease liabilities | 66,483 | Outside the notes; shown as a separate line | Q2 FS page:1 |
| Provision for closure and reclamation | 104,777 | Outside; undiscounted reclamation and mine closure of 212,959 is in the maturity table | Q2 FS page:1, page:11 |
| Contractual commitments (undiscounted) | 168,356 | Outside; disclosed commitments, some with cancellation clauses | Q2 FS page:11 |
| Pensions, retiree medical, factoring or supply-chain finance, letters of credit, surety bonds | Not supplied | A search of the retained sources found none of these terms in the interim statements | All sources |
| Litigation | Not supplied | Contingencies note states no material adverse effect expected in aggregate | Q2 FS page:19 |

### Liquidity

Unrestricted cash and cash equivalents were 134,808 at June 30, 2026 and no committed undrawn facility is disclosed, because the term loan was terminated. Restricted cash totals 500,853, of which 453,925 is current. Of the proceeds placed in the interest reserve and construction disbursement accounts (683,168, US$494,208 thousand), 199,176 (US$145,000 thousand) had been released by June 30, 2026 (Q2 FS page:12). The company states that its anticipated funding is sufficient to commercial production in 2027 only "As long as the Company meets the conditions precedent to the Senior Secured Notes", and that it will need additional financing if the release of funds is not possible or the proceeds are insufficient (Q2 FS page:4; the Q1 FS wording is similar). The company discloses a going concern dependency on executing its business plan (Q2 FS page:4). The cost to complete construction is Not supplied.

### Covenants

No financial maintenance covenant for the Senior Secured Notes is stated in the retained pages. Gold Stream covenants were described in the Q1 FS: a debt service coverage ratio of no less than 1.25:1 for the six months ended on the last date of each quarter after the completion test and a grace period, and minimum unrestricted cash and cash equivalents of at least 25,000 CAD thousands at all times following the full drawdown or cancellation of the Senior Secured Term Loan commitments and the additional deposit, both until the Security Release Date (Q1 FS page:10, page:11). Both commitments were cancelled by April 10, 2026. The Q2 FS does not repeat these terms after the buy-down, so whether they still apply is Not supplied. If the cash minimum still applied, unrestricted cash would exceed it by 109,808 (Calculation 15). The debt service coverage test cannot be computed because no definition inputs or earnings exist. The debt service coverage ratio, the cash minimum and the notes' covenants use definitions that are not supplied and differ from any metric computed in this module.

### Latest quarter and subsequent events

Quarter ended June 30, 2026 events: completion of the notes offering on April 10, 2026 and use of proceeds (Q2 FS page:12); exercise of the Gold Stream buy-down option (Q2 FS page:14); termination of the term loan (Q2 FS page:14); grant of the NSR Royalty and Additional NSR Royalty Option with 266,950 of initial recognition for the option (Q2 FS page:16); royalty prepayment of 25,000 (Q2 FS page:3); closure provision increase to 104,777 with an estimate change of 58,120 in the six months (Q2 FS page:16). The Q2 FS has no subsequent events note. No event between June 30, 2026 and the cutoff is supplied; the pack contains no filing after August 13, 2026 and no Q3 2026 results.

### Definition review

- The issuer reports no EBITDA, adjusted EBITDA or free cash flow. No definition is supplied. This module does not invent one.
- "Total debt" here means the Senior Secured Notes only at gross amortized cost (1,082,552) or net carrying value (1,055,969); leases are shown separately. The embedded derivative asset of 26,583 is netted on the balance sheet but is not a cash resource.
- Restricted cash is excluded from "cash" in the liquidity table. It is shown separately because release depends on conditions not supplied.
- The first six months' interest expense is partly capitalized: interest expense on long-term debt, lease and other liabilities, net of interest income on proceeds, was capitalized at 5,402 to mineral property and 13,328 to construction-in-progress (Q2 FS page:11). Gross interest incurred is therefore larger than the 19,851 expensed, and cash interest cannot be derived.

## Calculations

All amounts CAD thousands unless stated. Inputs are the reported figures cited above.

1. Restricted cash: 453,925 + 46,928 = 500,853. Agrees to the financial instruments table (Q2 FS page:7).
2. Total cash including restricted: 134,808 + 500,853 = 635,661.
3. Debt carrying value: 89,352 + 966,617 = 1,055,969. Also 1,082,552 - 26,583 = 1,055,969. Both agree to the printed carrying value.
4. Gross debt less unrestricted cash: 1,082,552 - 134,808 = 947,744. This is a net debt figure on a gross-notes basis, not a ratio, because no EBITDA exists.
5. Gross debt less all cash including restricted: 1,082,552 - 635,661 = 446,891. Restricted funds are earmarked for construction and interest, so this understates net funding need.
6. Leases: 17,316 + 49,167 = 66,483 at June 30, 2026; 15,751 + 47,333 = 63,084 at December 31, 2025. Gross notes plus leases: 1,082,552 + 66,483 = 1,149,035.
7. Working capital: 612,167 - 194,097 = 418,070 including restricted current cash. Excluding current restricted cash: 612,167 - 453,925 = 158,242; 158,242 - 194,097 = -35,855.
8. Cash used before financing, six months ended June 30, 2026: operating outflow 30,235 + additions to mineral property, plant and equipment 203,600 + construction prepayments and deposits 9,144 = 242,979. Three months ended June 30, 2026: 15,057 + 131,352 + 4,324 = 150,733. These are analyst sums, not reported free cash flow; they exclude the 254,352 buy-down and treat the sums as outflows.
9. Cross-checks of the six-month figures against the first quarter (Q1 FS page:1 to page:3): net loss 139,677 - 104,457 = 35,220 (agrees to the three-month loss); additions 203,600 - 72,248 = 131,352 (agrees); operating outflow 30,235 - 15,178 = 15,057 (agrees).
10. Gold Stream derivative roll-forward: 421,902 - 254,352 + 41,736 = 209,286. Agrees to the printed balance (Q2 FS page:15).
11. Notes proceeds allocation: 254,352 + 130,228 + 552,940 + 99,241 = 1,036,761, agrees to the principal. Restricted deposits: 130,228 + 552,940 = 683,168, agrees to the printed total. Cash proceeds: 99,241 + 254,352 = 353,593, agrees to the printed proceeds (Q2 FS page:12).
12. Restricted cash roll: 683,168 - 199,176 = 483,992 against reported restricted cash of 500,853, a difference of 16,861. In US dollar thousands: 494,208 - 145,000 = 349,208 against 352,442 reported (Q2 FS page:10), a difference of 3,234. The sources do not explain either difference; it is not attributed to interest income or exchange.
13. Debt roll-forward: 1,036,761 + 15,953 - 19,601 = 1,033,113; then 1,033,113 + 20,102 + 171 + 29,166 = 1,082,552. Agrees to the printed balance. Embedded derivative: 15,953 + 10,630 = 26,583.
14. Coupon sizing from printed terms: US$750,000,000 x 8.50% = US$63,750,000 a year, US$31,875,000 per semi-annual payment. Three payments are US$95,625,000, compared with the interest reserve deposit of US$94,208,000, a shortfall of US$1,417,000 against three full coupons that the sources do not explain. At the issue-date ratio of 1,036,761 / 750,000 = 1.382348 CAD per US$, the annual coupon is 63,750 x 1.382348 = 88,125 (rounded). The undiscounted within-one-year long-term debt figure is 88,581 (Q2 FS page:11); the two bases differ and are not reconciled.
15. Gold Stream cash minimum, if it still applied: 134,808 - 25,000 = 109,808 of excess over the minimum.
16. Maturity table checks (Q2 FS page:11): within one year 46,187 + 25,142 + 88,581 + 15,589 + 72 + 2,833 + 138,109 = 316,513; one to five years 114,281 + 1,428,200 + 86,432 + 419 + 4,724 + 22,372 = 1,656,428; more than five years 6,729 + 121,062 + 212,468 + 7,875 = 348,134; total 316,513 + 1,656,428 + 348,134 = 2,321,075. All agree to the printed totals.
17. Shares issued in the six months: 2,272,608 + 508,737 + 1,057,703 = 3,839,048, equal to 125,139,335 - 121,300,287 = 3,839,048 (Q2 FS page:2).
18. Leverage and interest cover: Not calculable. No EBITDA or revenue is reported, and cash interest paid for the half-year is not stated.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Audited annual statements for FY2025 are not in the pack | Full-year 2025 income, cash flow and annual notes cannot be sourced; the FY2025 chart rows carry the December 31, 2025 balance sheet only | Add the Form 40-F financial statements exhibit |
| No EBITDA, revenue or earnings measure | Leverage and interest cover are Not supplied | Do not substitute a derived measure; rely on liquidity and funding coverage |
| Cash interest paid for the six months ended June 30, 2026 is not stated | Interest cover and the first coupon timing cannot be tested | Locate the management discussion or note disclosure |
| Legal terms of the Senior Secured Notes (guarantors, collateral, covenants, release of restricted cash) | Covenant headroom, structural ranking and access to 500,853 of restricted cash cannot be assessed | Add the indenture and disbursement account terms |
| Whether Gold Stream covenants and security still apply after the buy-down | Covenant compliance is Not supplied | Add the amending agreement or later disclosure |
| Cost to complete construction, project budget and schedule | Funding adequacy against remaining spend cannot be sized; only contractual commitments of 168,356 are stated | Add the management discussion and technical report |
| Unexplained restricted cash and interest reserve differences (Calculation 12 and 14) | Immaterial to the base view but unreconciled | Confirm in the management discussion |
| Interim statements are unaudited and extracted as text | Figures carry no audit assurance and table alignment was read from the layout | Confirm key figures against the filed documents |
| No events after June 30, 2026 | Liquidity after the balance sheet date is unknown | Check later periodic filings up to the cutoff |
| Equipment loan balances and any currency hedging detail | Debt may be understated by equipment loans; the company states no derivatives are used for currency exposure | Not available from the pack |

## Next module

Pass to the business and transaction context module (CP-1A) with these limits: reported figures are CAD thousands, unaudited, and for the quarter and six months ended June 30, 2026 unless labelled otherwise; the notes' legal terms and the Gold Stream covenant status are Not supplied; and restricted cash of 500,853 is not freely available. That module should describe the Eskay Creek financing structure (notes, Gold Stream buy-down, royalties) using the notes' own wording and carry the missing project budget as a gap. The synthesis module should treat leverage and interest cover as Not supplied rather than as favourable or adverse, and the evidence review should check that no downstream figure uses restricted cash as liquidity.
