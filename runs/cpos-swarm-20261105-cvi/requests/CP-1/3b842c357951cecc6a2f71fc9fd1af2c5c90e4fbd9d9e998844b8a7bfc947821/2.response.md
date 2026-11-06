## Request

Module CP-1, financial base, for CVR ENERGY INC (ticker CVI, issuer id cvi), as of 2026-11-05, pathway credit_snapshot, current period Q3 2026, prior period FY2025, reporting currency USD, in US$ millions unless a row says otherwise. The cutoff is 2026-11-05. The perimeter is CVR Energy, Inc. consolidated, which includes CVR Partners, LP as a variable interest entity (Q3 2026 10-Q page:13). The issuer is a holding company, not a subsidiary inside a combined filing, so no parent perimeter is substituted.

This handoff extracts the reported statement values, builds the debt, liquidity, maturity, leverage and cover bases, reviews the EBITDA definitions and sets out claims outside debt. It carries forward the CP-0 limits: no executed legal documents, no acquisition agreement, a segment re-cut in 2026, and text-extraction sources only. It gives no credit opinion; CP-1A and CP-2 do that.

## Sources

### Issuer sources relied on

| Source name | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_cvi-20251231.htm.jsonl | 11b2ae0e09456bfa771d4cab8a17d5e6eecebad270822a0aa27a6321ae3e1326 | FY2025 statements, debt note, facility table, leases, contractual obligations, Adjusted EBITDA reconciliation |
| 10-Q_2026-03-31_cvi-20260331.htm.jsonl | 0d5ec22f9043f7de61004c1d3fc3166812200367bbaae195e5e1fbdd81619bfc | Q1 2026 cash, debt, facilities, cash interest, Adjusted EBITDA |
| 10-Q_2026-06-30_cvi-20260630.htm.jsonl | 358aaec14a40e7fb2473ba1f5c1574588c88cdab98ea0a6156b8c6e07d430343 | Q2 2026 cash, debt, facilities, cash interest, Adjusted EBITDA |
| 10-Q_2026-09-30_cvi-20260930.htm.jsonl | c1bc2003ec1856161a58b4e8e6474dd136cd1e6864fe6be884dd4ce7689172a8 | Q3 2026 and nine-month statements, debt, facilities, liquidity, claims outside debt, acquisition note |
| EX-99.1_2026-04-29_exhibit991-cviq12026earnin.htm.jsonl | ec1426d7dc5a0e9978dd49bcfe1d59907ecfcc63064a0912a9028158f50040e7 | Management statement on crack spread swaps |
| EX-99.1_2026-07-29_exhibit991-cviq22026earnin.htm.jsonl | 1459a1187a6f9d055543784814ad9e46560c18ce90ff9327aed9062ea6d7d429 | Read for cross-check of Q2 Adjusted EBITDA; no figure taken from it |
| EX-99.1_2026-11-03_d897437dex991.htm.jsonl | a8afdbbc4ca0ef0b0aa3933661eb6fa3f49fab4f6b6643dc433309cf920a00ae | Cross-check of Q3 Adjusted EBITDA and debt; management language not adopted |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 1a8afb0886e9641787b9eba27d5f0b727ffb872f803108f1a4c711fde39ffcd9 | Source readiness, limitations and conflicts carried forward below |

Context file sha256 90a4adce7121ac13b0bc8c46b1ee93789832813a3c6223523e8f15963f3f61b5 holds the user's settings and is not issuer evidence. It leaves ratings, quotes and valuation inputs blank; none is used or treated as zero.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt is low against trailing Adjusted EBITDA, 1.94x gross and 0.55x net at the latest quarter, with liquidity of 1,853 million. The ratios exclude the pending acquisition financing and rest on a management EBITDA measure. | Medium | Covenant levels, the acquisition financing terms and the sustainability of the current earnings level are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Trailing Adjusted EBITDA rose from 393 million in FY2025 to 919 million, while total debt moved only from 1,765 million to 1,781 million. | Gross leverage fell from 4.49x to 1.94x; earnings level, not debt reduction, drove the change. | Medium |
| Cash rose to 1,278 million, including 158 million held in the consolidated CVR Partners entity, and 500 million must stay unrestricted until the acquisition closes. | Usable liquidity is lower than the headline figure of 1,853 million. | Medium |
| The 2026 refinancing replaced the 2029 notes and term loan with 2031 and 2034 notes; no note principal falls due before 2028. | Near-term maturity risk is low; 733 million falls due in 2028. | High |
| Claims outside debt grew: the RFS obligation, derivative liabilities and accrued income taxes sit in other current liabilities. | These near-term cash calls draw on the same liquidity and are not in net debt. | Medium |
| Adjusted EBITDA adds back unrealized derivative losses and removes RFS changes, so reported EBITDA of 964 million trailing differs from 919 million. | Definition choice moves leverage and cover; the basis must be named whenever a ratio is used. | Medium |

### Financial base view

The financial base is usable. Reported statements for the annual report and the three 2026 quarters give consistent debt, cash and facility data, and the consolidated Adjusted EBITDA bridge ties to net income in every period checked. On a trailing basis to Q3 2026, gross debt is about two times Adjusted EBITDA, net debt is about half a turn, and cash interest is covered about seven times. All three are far better than at FY2025 because trailing Adjusted EBITDA more than doubled, not because debt fell: total debt including finance leases moved little across the four balance sheet dates. The February 2026 refinancing cleared the 2027 term loan and the 2029 notes and pushed the first principal maturity to 2028. Three limits govern use. First, the ratios are on the consolidated perimeter, which includes the CVR Partners entity, its cash and its secured notes. Second, the trailing figure includes a quarter that management calls its best in company history, so the ratio shows capacity at current cracks and not a through-cycle level. Third, none of the ratios includes the pending acquisition, its bridge or its equity, and the target's earnings are not supplied. Covenant levels are not supplied, so headroom is not calculable.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (December 31, 2025) | 4.49 | 3.19 | x | Total debt 1,765 including finance leases (carrying) over FY2025 Adjusted EBITDA 393; net of cash 511. Management Adjusted EBITDA; consolidated perimeter incl. CVR Partners. |
| LTM Q1 2026 (March 31, 2026) | 4.39 | 3.13 | x | Total debt 1,784 over LTM Adjusted EBITDA 406 (FY2025 plus Q1 2026 less Q1 2025); cash 512. Quarter-end ABL and note balances as printed. |
| LTM Q2 2026 (June 30, 2026) | 3.45 | 2.02 | x | Total debt 1,783 over LTM Adjusted EBITDA 517; cash 737. LTM built from FY2025, six months 2026 and six months 2025. |
| LTM Q3 2026 (September 30, 2026) | 1.94 | 0.55 | x | Total debt 1,781 over LTM Adjusted EBITDA 919; cash 1,278 includes 158 of consolidated VIE cash; excludes pending acquisition debt and 500 minimum cash condition. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 (December 31, 2025) | 2.77 | x | Adjusted EBITDA 393 over cash paid for interest 142 (10-K supplemental cash flow note). |
| LTM Q1 2026 | 3.01 | x | Adjusted EBITDA 406 over LTM cash interest 135 (FY2025 plus Q1 2026 less Q1 2025). |
| LTM Q2 2026 | 4.01 | x | Adjusted EBITDA 517 over LTM cash interest 129. |
| LTM Q3 2026 | 6.96 | x | Adjusted EBITDA 919 over LTM cash interest 132. Coupons are semi-annual, so cash interest is lumpy by quarter, and the window mixes pre- and post-refinancing coupon timing (the new notes' first coupon was due August 15, 2026). |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (December 31, 2025) | 511 | 296 | US$m | Undrawn is CVR Energy ABL available 248 (capacity 258 less 10 letters of credit) plus CVR Partners ABL 48. Company states total liquidity of 807. |
| Q1 2026 (March 31, 2026) | 512 | 589 | US$m | ABL available 539 (550 less 11 letters of credit) plus CVR Partners ABL 50. Company states about 1.1 billion. |
| Q2 2026 (June 30, 2026) | 737 | 590 | US$m | ABL available 540 (550 less 10 letters of credit) plus CVR Partners ABL 50. Company states about 1.3 billion. |
| Q3 2026 (September 30, 2026) | 1,278 | 575 | US$m | ABL available 530 (550 less 20 letters of credit) plus CVR Partners ABL 45. Cash includes 158 of consolidated VIE cash; 500 must stay unrestricted until acquisition close; neither facility is drawn. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0 | US$m | Principal of notes at September 30, 2026; no note or drawn facility matures. Finance lease current portion of 12 is excluded; its timing at that date is not supplied. |
| 2027 | 0 | US$m | The term loan that matured in December 2027 was repaid in February 2026. |
| 2028 | 733 | US$m | 183 of 5.750% notes (February 2028, CVR Energy) plus 550 of 6.125% senior secured notes (June 2028, CVR Partners). The CVR Partners ABL also matures September 2028 and is undrawn. |
| 2029 | 0 | US$m | The 8.500% notes due 2029 were redeemed in February 2026. |
| 2030 | 0 | US$m | No instrument matures. |
| 2031 | 600 | US$m | 7.500% senior notes due February 2031. The CVR Energy ABL matures February 2031 and is undrawn. |
| 2032 | 0 | US$m | No instrument matures. |
| 2033 | 0 | US$m | No instrument matures. |
| 2034 | 400 | US$m | 7.875% senior notes due February 2034. Total principal across rows is 1,733; carrying value differs by issuance costs. Call and change-of-control terms not applied. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | LTM Q3 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales | 7,162 | 3,281 | 1,944 | 8,000 | 5,352 | 9,810 | Statements of operations; 10-K page:132, 10-Q Q3 page:9 |
| Operating income | 182 | 724 | 512 | 657 | 277 | 562 | Same pages |
| Interest expense, net | 108 | 21 | 25 | 105 | 79 | 134 | Same pages; 9M 2026 includes a 28 loss on extinguishment (10-Q Q3 page:17) |
| Net income including noncontrolling interest | 90 | 563 | 401 | 449 | 206 | 333 | Same pages |
| Net income attributable to CVR Energy stockholders | 27 | 570 | 374 | 375 | 137 | 265 | Same pages |
| Depreciation and amortization (EBITDA bridge) | 403 | 79 | 111 | 237 | 258 | 382 | 10-K page:115; 10-Q Q3 page:56 |
| EBITDA (reported bridge) | 591 | 804 | 625 | 913 | 540 | 964 | Same pages |
| Changes in RFS obligation adjustment | (262) | (314) | (471) | (190) | (271) | (181) | Same pages; negative is a favorable change removed from EBITDA |
| Adjusted EBITDA (management) | 393 | 582 | 180 | 828 | 302 | 919 | Same pages; consolidated, unaffected by the segment re-cut |
| Nitrogen Fertilizer segment EBITDA (equals its Adjusted EBITDA) | 211 | 20 | 71 | 205 | 191 | 225 | 10-K page:116; 10-Q Q3 page:57 |
| Cash from operations | 144 | 655 | 163 | 1,026 | 144 | 1,026 | Cash flow statements; Q3 figures derived as nine months less six months |
| Capital expenditures | 185 | Not supplied discretely | Not supplied discretely | 152 | 130 | 207 | Cash flow statements; cash basis |
| Turnaround expenditures | 197 | Not supplied discretely | Not supplied discretely | 2 | 196 | 3 | Cash flow statements |
| Free cash flow after capex and turnaround | (238) | Not calculable discretely | Not calculable discretely | 872 | (182) | 816 | Calculated; before dividends and distributions to noncontrolling holders |
| Cash paid for interest | 142 | 46 | 43 | 106 | 116 | 132 | Supplemental cash flow notes; Q3 derived as nine months less six months |
| Cash and cash equivalents (period end) | 511 | 1,278 | 670 | 1,278 | 670 | 1,278 | Balance sheets; Q3 2025 from cash flow statement closing cash |
| Total debt and finance leases incl. current portion (carrying) | 1,765 | 1,781 | Not supplied | 1,781 | Not supplied | 1,781 | Note 6; Q3 2025 balance sheet is not in the pack |
| Net debt (total debt less cash) | 1,254 | 503 | Not supplied | 503 | Not supplied | 503 | Calculated |
| Total liquidity (cash plus undrawn facilities) | 807 | 1,853 | Not supplied | 1,853 | Not supplied | 1,853 | Calculated; matches company statements |
| Total equity | 898 | 1,257 | 1,041 | 1,257 | 1,041 | 1,257 | Balance sheet and statement of changes in equity |
| Total debt / LTM Adjusted EBITDA (x) | 4.49 | 1.94 | Not supplied | 1.94 | Not supplied | 1.94 | Calculated |
| Net debt / LTM Adjusted EBITDA (x) | 3.19 | 0.55 | Not supplied | 0.55 | Not supplied | 0.55 | Calculated |
| LTM Adjusted EBITDA / cash interest (x) | 2.77 | 6.96 | Not supplied | 6.96 | Not supplied | 6.96 | Calculated |

### Debt by instrument at September 30, 2026

| Instrument | Issuer or borrower | Principal or capacity | Rate | Maturity | Security and guarantee as printed |
| --- | --- | --- | --- | --- | --- |
| 7.500% Senior Notes | CVR Energy | 600 | 7.500% fixed | February 15, 2031 | Senior unsecured; guaranteed by domestic subsidiaries other than CVR Partners and listed exclusions (10-K page:151) |
| 7.875% Senior Notes | CVR Energy | 400 | 7.875% fixed | February 15, 2034 | Same as above |
| 5.750% Senior Notes | CVR Energy | 183 (400 at December 31, 2025; 217 redeemed at par February 17, 2026) | 5.750% fixed | February 2028 | Senior unsecured; guarantee text in 10-K page:153 |
| 6.125% Senior Secured Notes | CVR Partners and finance co-issuer | 550 | 6.125% fixed | June 2028 | Secured; guaranteed by CVR Partners domestic subsidiaries (10-K page:157) |
| CVR Energy ABL | CVR Energy subsidiaries | 550 capacity, 0 drawn, 20 letters of credit, 530 available | Not supplied for 2026 | February 12, 2031 | Borrowing base facility; commitments may rise to 700 |
| CVR Partners ABL | CVR Partners | 45 capacity, 0 drawn, 0 letters of credit | Not supplied for 2026 | September 26, 2028 | Borrowing base facility |
| Finance leases | Segments | 49 net of current portion (4 CVR Energy, 25 Petroleum, 20 Nitrogen); current portion of total debt 12 | Not supplied | Not supplied at September 30, 2026 | Included in total debt |

Repaid in 2026: the Petroleum segment term loan (154 at December 31, 2025, maturity December 30, 2027) on February 12, 2026, and the 8.500% notes due 2029 (600) on February 13, 2026 at 104.250 percent of principal. The count of series is taken from the note 6 table: four note series carried a balance at September 30, 2026, no term loan, two ABL facilities.

### Claims outside debt

| Claim | Amount | Date | Inside or outside total debt | Locator |
| --- | --- | --- | --- | --- |
| Finance lease obligations | 49 net of current portion | September 30, 2026 | Inside | 10-Q Q3 page:16 |
| Operating lease liabilities | 64 total | December 31, 2025 | Outside; Q3 2026 total not supplied, only current portion 17 | 10-K page:150; 10-Q Q3 page:15 |
| Accrued RFS obligation | 230 (72 at December 31, 2025) | September 30, 2026 | Outside; in other current liabilities | 10-Q Q3 page:15 and page:24 |
| Derivative liabilities | 160 current and 18 long-term; gross liability subject to rating-trigger terms 294, collateral posted 98 | September 30, 2026 | Outside | 10-Q Q3 page:19 |
| Accrued income taxes | 132 (nil at December 31, 2025) | September 30, 2026 | Outside | 10-Q Q3 page:15 |
| Transportation agreements | 995 total, 84 within a year | December 31, 2025 | Outside; Q3 says no material change outside ordinary course | 10-K page:121; 10-Q Q3 page:61 |
| Purchase commitments | 165 total, 62 within a year | December 31, 2025 | Outside | 10-K page:121 |
| 45Q fees guaranteed by CVR Partners | Up to 15 per year, cap 45 | September 30, 2026 | Outside, contingent | 10-Q Q3 page:22 |
| Guaranty Dispute, ammonia release suits, Kansas claims, call option coverage appeal | Not quantified in the filing | September 30, 2026 | Outside, contingent | 10-Q Q3 page:24 and page:25 |
| Pending acquisition: cash consideration about 4.2 billion, bridge up to 2.5 billion, equity subscriptions 800 plus up to 500, termination fee of 6%, 4% or 2% of base price | As printed | Entered November 2, 2026, not closed | Outside, subsequent event | 10-Q Q3 page:11, page:12, page:32 |
| Distributions to CVR Partners noncontrolling holders | 70 in nine months 2026 | Nine months 2026 | Outside; cash leaves the consolidated group | 10-Q Q3 page:10 |
| Pension and retiree medical; factoring and supply chain finance | None located | n/a | Not supplied: term searched in the annual report and the latest quarterly report; only generic investor sentiment text mentions pension funds | 10-K page:65 |

### Definition review

Adjusted EBITDA is management's measure: EBITDA less favorable changes in the RFS obligation, plus unrealized derivative losses, adjusted for inventory valuation impacts (10-Q Q3 page:56; 10-K page:115). Three points matter for credit use. The RFS adjustment removes the 2025 and 2026 waiver gains (the 2026 waiver is described at about 253 and the 2025 waiver at about 488), so the measure is conservative on that item, but it also removes ongoing RFS revaluation. The derivative add-back of 278 for nine months 2026 removes mark-to-market losses on crack spread swaps while the derivative liabilities of 160 current and 18 long-term remain on the balance sheet, so a cash settlement against those positions is not in Adjusted EBITDA. The inventory valuation line removes a favorable 173 in nine months 2026 on a FIFO basis. Reported EBITDA, trailing, is 964 against 919 adjusted, and leverage on the reported basis would be lower, but the reported figure includes the waiver gains. Cash interest cover is computed on Adjusted EBITDA only. Covenant EBITDA is not defined in the supplied text; the covenant basis differs from this measure and is Not supplied.

### Consistency with CP-0

CP-0 stated that covenant levels were not located and that a discrete Q4 2025 is not reported. Both hold. This handoff derives Q4 2025 Adjusted EBITDA only implicitly through the trailing sums. CP-0's note that the release rounds segment debt to 570 against the note's 569 is not used here; the note value governs. No CP-0 statement is corrected.

### Evidence register

Quotes are exact substrings of the cited chunk.

| Source | Locator | Quote | Supports |
| --- | --- | --- | --- |
| 10-K FY2025 | page:132 | Net sales $ 7,162 $ 7,610 $ 9,247 | FY2025 net sales |
| 10-K FY2025 | page:132 | Operating income 182 58 1,123 | FY2025 operating income |
| 10-K FY2025 | page:132 | Net income 90 45 878 | FY2025 net income |
| 10-K FY2025 | page:132 | Net income attributable to CVR Energy stockholders $ 27 $ 7 $ 769 | FY2025 attributable income |
| 10-K FY2025 | page:115 | EBITDA 591 394 1,435 | FY2025 EBITDA |
| 10-K FY2025 | page:115 | Adjusted EBITDA $ 393 $ 317 $ 1,164 | FY2025 Adjusted EBITDA |
| 10-K FY2025 | page:115 | Changes in RFS liability, (favorable) (262) (89) (284) | RFS adjustment |
| 10-K FY2025 | page:116 | Nitrogen Fertilizer Segment EBITDA and Adjusted EBITDA $ 211 $ 179 $ 281 | Nitrogen EBITDA |
| 10-K FY2025 | page:133 | Net cash provided by operating activities 144 404 948 | FY2025 cash from operations |
| 10-K FY2025 | page:133 | Capital expenditures (185) (179) (205) | FY2025 capex |
| 10-K FY2025 | page:133 | Turnaround expenditures (197) (53) (57) | FY2025 turnaround |
| 10-K FY2025 | page:177 | Cash paid for interest $ 142 $ 112 $ 95 | FY2025 cash interest |
| 10-K FY2025 | page:151 | Total long-term debt and finance lease obligations, including current portion $ 1,765 $ 1,919 | FY2025 total debt |
| 10-K FY2025 | page:151 | $ 258 $ — $ 10 $ 248 June 30, 2027 | FY2025 ABL capacity, letters of credit, availability |
| 10-K FY2025 | page:155 | scheduled maturity date of December 30, 2027 | Term loan maturity |
| 10-K FY2025 | page:121 | Transportation agreements (6) 84 911 995 | Commitment outside debt |
| 10-K FY2025 | page:121 | Purchase commitments (5) 62 103 165 | Commitment outside debt |
| 10-K FY2025 | page:150 | Total lease liability $ 64 $ 66 | Operating and finance lease liabilities |
| 10-K FY2025 | page:119 | we had total liquidity of approximately $807 million | FY2025 liquidity |
| 10-Q Q1 2026 | page:14 | Total long-term debt and finance lease obligations, including current portion $ 1,784 $ 1,765 | Q1 total debt |
| 10-Q Q1 2026 | page:14 | $ 550 $ — $ 11 $ 539 February 12, 2031 | Q1 ABL availability |
| 10-Q Q1 2026 | page:14 | $ 50 $ — $ — $ 50 September 26, 2028 | Q1 CVR Partners ABL |
| 10-Q Q1 2026 | page:7 | Cash and cash equivalents (including $128 and $69, respectively, of consolidated variable interest entity (“VIE”)) $ 512 $ 511 | Q1 cash |
| 10-Q Q1 2026 | page:25 | Cash paid for interest 40 47 | Q1 cash interest |
| 10-Q Q1 2026 | page:49 | Adjusted EBITDA $ 37 $ 24 | Q1 Adjusted EBITDA |
| 10-Q Q2 2026 | page:13 | Total long-term debt and finance lease obligations, including current portion $ 1,783 $ 1,765 | Q2 total debt |
| 10-Q Q2 2026 | page:14 | $ 550 $ — $ 10 $ 540 February 12, 2031 | Q2 ABL availability |
| 10-Q Q2 2026 | page:7 | Cash and cash equivalents (including $137 and $69, respectively, of consolidated variable interest entity (“VIE”)) $ 737 $ 511 | Q2 cash |
| 10-Q Q2 2026 | page:25 | Cash paid for interest 60 73 | Six months cash interest |
| 10-Q Q2 2026 | page:49 | Adjusted EBITDA $ 209 $ 99 $ 246 $ 122 | Q2 and six month Adjusted EBITDA |
| 10-Q Q2 2026 | page:52 | $737 million of consolidated cash and cash equivalents, $540 million available under the CVR Energy ABL, and $50 million available | Q2 liquidity inputs |
| 10-Q Q3 2026 | page:8 | Cash and cash equivalents (including $158 and $69, respectively, of consolidated variable interest entity (“VIE”)) $ 1,278 $ 511 | Q3 cash and VIE cash |
| 10-Q Q3 2026 | page:9 | Net sales $ 3,281 $ 1,944 $ 8,000 $ 5,352 | Net sales |
| 10-Q Q3 2026 | page:9 | Operating income 724 512 657 277 | Operating income |
| 10-Q Q3 2026 | page:9 | Interest expense, net (21) (25) (105) (79) | Interest expense |
| 10-Q Q3 2026 | page:9 | Net income 563 401 449 206 | Net income |
| 10-Q Q3 2026 | page:9 | Net income attributable to CVR Energy stockholders $ 570 $ 374 $ 375 $ 137 | Attributable income |
| 10-Q Q3 2026 | page:10 | Net cash provided by operating activities 1,026 144 | Nine month cash from operations |
| 10-Q Q3 2026 | page:10 | Capital expenditures (152) (130) | Nine month capex |
| 10-Q Q3 2026 | page:10 | Turnaround expenditures (2) (196) | Nine month turnaround |
| 10-Q Q3 2026 | page:10 | Cash and cash equivalents, end of period $ 1,278 $ 670 | Cash at both dates |
| 10-Q Q3 2026 | page:10 | Distributions to CVR Partners noncontrolling interest holders (70) (53) | Leakage to noncontrolling holders |
| 10-Q Q3 2026 | page:10 | Balance at September 30, 2025 100,629,209 $ 1 $ 1,508 $ (667) $ (2) $ 840 $ 201 $ 1,041 | Q3 2025 equity |
| 10-Q Q3 2026 | page:16 | Total long-term debt and finance lease obligations, including current portion $ 1,781 $ 1,765 | Q3 total debt |
| 10-Q Q3 2026 | page:16 | 5.750% Senior Notes, due February 2028 183 400 | 2028 notes balance |
| 10-Q Q3 2026 | page:16 | 7.875% Senior Notes, due February 2034 400 — | 2034 notes balance |
| 10-Q Q3 2026 | page:16 | $ 550 $ — $ 20 $ 530 February 12, 2031 | Q3 ABL availability |
| 10-Q Q3 2026 | page:16 | $ 45 $ — $ — $ 45 September 26, 2028 | Q3 CVR Partners ABL |
| 10-Q Q3 2026 | page:17 | redeemed all of its outstanding 8.500% Senior Notes, due January 2029 | 2029 notes redeemed |
| 10-Q Q3 2026 | page:17 | repaid the aggregate principal balance of the senior secured term loan facility | Term loan repaid |
| 10-Q Q3 2026 | page:27 | Cash paid for interest 106 116 | Nine month cash interest |
| 10-Q Q3 2026 | page:27 | Cash paid, net of refunds (received, net of payments) for income taxes $ — $ (3) | No cash taxes paid in nine months 2026 |
| 10-Q Q3 2026 | page:56 | EBITDA 804 625 913 540 | EBITDA bridge |
| 10-Q Q3 2026 | page:56 | Adjusted EBITDA $ 582 $ 180 $ 828 $ 302 | Adjusted EBITDA |
| 10-Q Q3 2026 | page:56 | Unrealized loss on derivatives, net 127 8 278 6 | Derivative add-back |
| 10-Q Q3 2026 | page:56 | Inventory valuation impacts, (favorable) unfavorable (35) 18 (173) 27 | Inventory add-back |
| 10-Q Q3 2026 | page:57 | Nitrogen Fertilizer EBITDA and Adjusted EBITDA $ 20 $ 71 $ 205 $ 191 | Nitrogen EBITDA |
| 10-Q Q3 2026 | page:59 | we had total liquidity of approximately $1.9 billion | Liquidity statement |
| 10-Q Q3 2026 | page:59 | maintain at least $500 million of unrestricted cash and cash equivalents | Minimum cash |
| 10-Q Q3 2026 | page:15 | Accrued Renewable Fuel Standard (“RFS”) obligation $ 230 $ 72 | RFS obligation |
| 10-Q Q3 2026 | page:15 | Derivative liabilities 160 — | Derivative liability |
| 10-Q Q3 2026 | page:15 | Accrued income taxes 132 — | Accrued tax |
| 10-Q Q3 2026 | page:19 | Other long-term liabilities — 18 — — | Long-term derivative liability |
| 10-Q Q3 2026 | page:19 | was $294 million, or $276 million after the effect of master netting arrangements, for which the Company has posted collateral of $98 million | Rating-trigger exposure |
| 10-Q Q3 2026 | page:22 | subject to an overall $45 million cap | 45Q fee cap |
| 10-Q Q3 2026 | page:24 | reduced by more than 118 million RINs, representing approximately $253 million | 2026 waiver |
| 10-Q Q3 2026 | page:25 | disputing the validity of an alleged 1993 guaranty | Guaranty Dispute |
| 10-Q Q3 2026 | page:11 | for aggregate cash consideration of approximately $4.2 billion | Acquisition |
| 10-Q Q3 2026 | page:12 | termination fee of 6%, 4% or 2% of the aggregate base purchase price | Termination fee |
| 10-Q Q3 2026 | page:32 | a senior secured 364-day bridge loan facility of up to $2.5 billion | Bridge |
| 10-Q Q3 2026 | page:33 | all prior period Renewables activity has been consolidated within “Other” | Segment re-cut |
| Release Q3 2026 | page:1 | the best quarterly results in the Company’s history | Management language, not adopted |
| Release Q1 2026 | page:2 | totaling $447 million expected to be realized through 2027 | Management statement on swaps |

## Calculations

All inputs are quoted above. US$ millions. Amounts are rounded to the nearest unit as printed; ratios to two decimals.

### Trailing Adjusted EBITDA

LTM = FY2025 + current year to date − prior year to date, from the Adjusted EBITDA reconciliations.

| Period | FY2025 | Year to date 2026 | Year to date 2025 | LTM |
| --- | --- | --- | --- | --- |
| Q1 2026 | 393 | 37 | 24 | 393 + 37 − 24 = 406 |
| Q2 2026 | 393 | 246 | 122 | 393 + 246 − 122 = 517 |
| Q3 2026 | 393 | 828 | 302 | 393 + 828 − 302 = 919 |

Tie-outs: nine months 2026 EBITDA 913 − 190 + 278 − 173 = 828; Q3 2026 EBITDA 804 − 314 + 127 − 35 = 582; FY2025 591 − 262 − 4 + 66 + 2 = 393; nine months 2025 540 − 271 + 6 + 27 = 302. Quarterly sum 37 + 209 + 582 = 828. Implied Q4 2025 Adjusted EBITDA is 393 − 302 = 91.

### Trailing cash interest

| Period | FY2025 | YTD 2026 | YTD 2025 | LTM |
| --- | --- | --- | --- | --- |
| Q1 2026 | 142 | 40 | 47 | 142 + 40 − 47 = 135 |
| Q2 2026 | 142 | 60 | 73 | 142 + 60 − 73 = 129 |
| Q3 2026 | 142 | 106 | 116 | 142 + 106 − 116 = 132 |

Q3 2026 alone: 106 − 60 = 46; Q3 2025 alone: 116 − 73 = 43.

### Debt, net debt, leverage and cover

Total debt is the printed carrying total of long-term debt and finance lease obligations including the current portion. Net debt = total debt − cash.

| Date | Total debt | Cash | Net debt | LTM Adj. EBITDA | Total debt / EBITDA | Net debt / EBITDA | EBITDA / cash interest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| December 31, 2025 | 1,765 | 511 | 1,765 − 511 = 1,254 | 393 | 1,765 / 393 = 4.49 | 1,254 / 393 = 3.19 | 393 / 142 = 2.77 |
| March 31, 2026 | 1,784 | 512 | 1,784 − 512 = 1,272 | 406 | 1,784 / 406 = 4.39 | 1,272 / 406 = 3.13 | 406 / 135 = 3.01 |
| June 30, 2026 | 1,783 | 737 | 1,783 − 737 = 1,046 | 517 | 1,783 / 517 = 3.45 | 1,046 / 517 = 2.02 | 517 / 129 = 4.01 |
| September 30, 2026 | 1,781 | 1,278 | 1,781 − 1,278 = 503 | 919 | 1,781 / 919 = 1.94 | 503 / 919 = 0.55 | 919 / 132 = 6.96 |

Sensitivities, not charted: LTM reported EBITDA at Q3 2026 is 591 + 913 − 540 = 964; 964 / 132 = 7.30. Principal-only notes outstanding are 183 + 600 + 400 + 550 = 1,733, and 1,733 / 919 = 1.89. Removing consolidated VIE cash of 158 gives cash of 1,278 − 158 = 1,120; the 569 of CVR Partners debt net of current portion is also in the consolidated total, and Nitrogen Fertilizer LTM EBITDA is 211 + 205 − 191 = 225. No split leverage for CVR Energy excluding CVR Partners is stated, because CVR Partners' current portion of debt and its cash interest are not supplied.

Run-rate coupon on notes outstanding at September 30, 2026, not a cash forecast: 600 × 7.500% = 45.00; 400 × 7.875% = 31.50; 183 × 5.750% = 10.52; 550 × 6.125% = 33.69; total 120.71. This excludes ABL commitment fees, letter of credit fees and finance lease interest.

### Liquidity

| Date | Cash | ABL available | CVR Partners ABL available | Undrawn | Total |
| --- | --- | --- | --- | --- | --- |
| December 31, 2025 | 511 | 258 − 0 − 10 = 248 | 48 | 248 + 48 = 296 | 511 + 296 = 807 |
| March 31, 2026 | 512 | 550 − 0 − 11 = 539 | 50 | 589 | 1,101 |
| June 30, 2026 | 737 | 550 − 0 − 10 = 540 | 50 | 590 | 1,327 |
| September 30, 2026 | 1,278 | 550 − 0 − 20 = 530 | 45 | 575 | 1,853 |

The Q3 2026 total agrees with the stated approximately 1.9 billion and the December 2025 total with the stated 807. Facilities expiring within twelve months of September 30, 2026: none (earliest is September 26, 2028). Headroom after the 500 minimum cash condition: 1,278 − 500 = 778 of cash, or 778 + 575 = 1,353 including undrawn facilities, while the acquisition is pending.

### Free cash flow

Free cash flow = cash from operations − capital expenditures − turnaround expenditures, before dividends and distributions.

| Period | Cash from operations | Capex | Turnaround | Result |
| --- | --- | --- | --- | --- |
| FY2025 | 144 | 185 | 197 | 144 − 185 − 197 = −238 |
| Nine months 2026 | 1,026 | 152 | 2 | 1,026 − 152 − 2 = 872 |
| Nine months 2025 | 144 | 130 | 196 | 144 − 130 − 196 = −182 |
| LTM Q3 2026 | 1,026 | 185 + 152 − 130 = 207 | 197 + 2 − 196 = 3 | 1,026 − 207 − 3 = 816 |

LTM cash from operations is 144 + 1,026 − 144 = 1,026. Q3 2026 cash from operations alone is 1,026 − 371 = 655, and Q3 2025 is 144 − (−19) = 163, using the six month figures 371 and −19 from the Q2 2026 10-Q. Nine months 2026 cash from operations includes working capital effects the filing attributes to higher commodity prices and a larger RFS obligation (10-Q Q3 page:63), and no cash taxes were paid in the period.

### Other trailing sums

| Item | FY2025 | YTD 2026 | YTD 2025 | LTM |
| --- | --- | --- | --- | --- |
| Net sales | 7,162 | 8,000 | 5,352 | 7,162 + 8,000 − 5,352 = 9,810 |
| Operating income | 182 | 657 | 277 | 562 |
| Net income | 90 | 449 | 206 | 333 |
| Net income attributable to CVR Energy stockholders | 27 | 375 | 137 | 265 |
| Interest expense, net | 108 | 105 | 79 | 134 |
| Depreciation and amortization | 403 | 237 | 258 | 382 |
| Changes in RFS obligation adjustment | −262 | −190 | −271 | −262 − 190 + 271 = −181 |

### Maturity total

Principal due by year at September 30, 2026: 2028 is 183 + 550 = 733; 2031 is 600; 2034 is 400; total 733 + 600 + 400 = 1,733. Carrying total including finance leases and net of issuance costs is 1,781.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Covenant levels, definitions and the issuer-reported fixed charge ratio are Not supplied; the ABL test applies only "in certain circumstances" and no trigger is printed. | Covenant headroom is Not calculable. | Obtain the executed ABL and indentures if headroom is required. |
| Pending acquisition: Purchase Agreement, commitment letter and subscription agreements are not in the pack; pro forma debt, interest and EBITDA are Not calculable because the target's earnings are not supplied. | All ratios here exclude the acquisition; leverage after closing is unknown. | Treat ratios as standalone; CP-1A and CP-2 must not imply pro forma strength. |
| Q3 2025 balance sheet (debt, liquidity) is not in the pack. | Year-on-year leverage and liquidity at Q3 2025 are Not supplied. | Use FY2025 as the prior comparison. |
| Discrete Q3 capex and turnaround are not printed on a cash basis; the segment note shows accrual-basis capex that differs from the cash flow statement. | Discrete Q3 free cash flow is Not calculable. | Use nine month and LTM figures. |
| Interest rates on the CVR Energy ABL and CVR Partners ABL for 2026 and the 2026 finance lease maturity profile are Not supplied; ABL margin text is in the 10-K only for the pre-amendment facility. | Forward cash interest on facilities is Not calculable. | State the run-rate on notes only. |
| Operating lease liabilities at September 30, 2026 other than the current portion are Not supplied. | Lease-adjusted leverage is Not calculable at Q3 2026. | Use FY2025 operating lease liability of 64 as context only. |
| Segment re-cut: the 10-K shows three segments; 2026 reports show two with Renewables in Other. | Segment figures across FY2025 and 2026 are not like-for-like; consolidated figures here are unaffected. | Use only consolidated figures for trend; label segment rows by source basis. |
| CVR Partners' separate cash interest, current debt and cash are not supplied. | Leverage excluding the consolidated VIE is Not calculable. | Present only the consolidated view and the VIE cash and debt amounts as printed. |
| Adjusted EBITDA is management-defined and tied to the RFS adjustments; the sustainability of current cracks is outside the sources. | Trailing ratios may overstate through-cycle capacity. | CP-2 to weigh the definition risk; no external data added here. |
| Extraction fidelity of flattened tables was not reviewed against the rendered documents. | Table values rest on text extraction. | Each figure was checked against its cited chunk. |

No source dated after 2026-11-05 is used. The acquisition (November 2, 2026) and the dividend declaration (November 3, 2026) are subsequent events inside the cutoff; later contract dates are terms.

## Next module

CP-1A may proceed on the business and transaction context. It should use this handoff's debt, liquidity and claims-outside-debt tables, carry the unquantified contingencies and the pending acquisition as unknowns, and not treat the acquisition financing as completed. CP-2 should name the Adjusted EBITDA basis for every ratio, show net debt both with and without the VIE cash, and treat the 500 minimum cash condition as a restriction while the acquisition is pending.
