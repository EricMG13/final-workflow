## Request

Module: financial base for Kodiak Gas Services, Inc. (issuer id kgs, NYSE: KGS), pathway credit_snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05. Reporting currency per the run context is USD. Current period is q2-2026 (three and six months ended June 30, 2026) and prior period is fy-2025 (year ended December 31, 2025). Filed statements are in USD thousands; the chart tables below are in the units their headers require (x or US$m). The scope is reported facts, labelled calculations, credit metrics, liquidity, debt structure, definition risks and gaps, for use by the business-context, credit-synthesis and evidence-trace modules that follow. No outside knowledge of the company is used; every figure is from the pinned sources or is a calculation shown in `## Calculations`.

## Sources

### Issuer sources relied on

| Source name | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_kgs-20251231.htm.jsonl | e6f626e8ec2572cfebf2e718e3182d92317f6b3aa59e3698f1eee834557c8791 | FY2025 and FY2024 audited statements, debt note, covenant terms, December 2024 and December 2025 balances |
| 10-Q_2025-09-30_kgs-20250930.htm.jsonl | 6db116b2f7c71c732775eba343378dd9074804cd017a46d662467d5ecc03a35b | September 30, 2025 balance sheet, ABL drawings and letters of credit, commitments after the September 2025 amendment |
| 10-Q_2026-03-31_kgs-20260331.htm.jsonl | b0c6d87ecc739135889320e66c86ebf276495d3e9a2db77ae4ac15158d5c70bd | March 31, 2026 balances, first quarter 2026 flows and reconciliations, subsequent events |
| 10-Q_2026-06-30_kgs-20260630.htm.jsonl | 5759bf9f234dd11e438ac1ffdc287279a37a411d788492589a0ab13b93ffe323 | June 30, 2026 statements, debt note and maturities, leases, commitments, segments, liquidity discussion, adjusted EBITDA and cash flow reconciliations |
| EX-99.1_2026-02-25_kgsq42025earningsrelease.htm.jsonl | ad11af9e19e3a760d7586680bcd6c48b50c7738da5c5d9535e8a17c6b9eb6e1f | Third and fourth quarter 2025 discrete figures, FY2025 adjusted EBITDA reconciliation, initial 2026 guidance |
| EX-99.1_2026-05-11_kgsq12026earningsrelease.htm.jsonl | 28d16a69c5b1c7a653a4d372cd4408de628fa59c0bf8c9e28886ae87b3878e62 | First quarter 2026 management leverage ratio and summary |
| EX-99.1_2026-08-06_kgsq22026earningsrelease.htm.jsonl | 1fc26851224dc87b9b00439921419ff667a90cf4a5077539afcc9f2e07b9ff72 | Second quarter 2026 summary, liquidity statement, management leverage ratio, revised 2026 guidance |

### Run context (settings, not issuer evidence)

| Item | sha256 |
| --- | --- |
| context file 1767042-kodiak-gas-services-inc-kgs.json | 45f2a3562d2dfb1c25d8d6636b278dfe41f8d48fe6d85e1a214b7248a9909e44 |

### Upstream handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 source readiness | 1490db53fcb453be1025254f11915cd1c064e8caa925cbc2f680c4e837a39f8b | Opened and consumed: source identities and periods, readiness status READY_WITH_LIMITATIONS for this module, differences D1 to D6 and gaps G1 to G13 are carried forward below (see Findings, Consumption of the source-readiness handoff) |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported leverage fell to 3.63x total debt to adjusted EBITDA at June 2026 after an equity raise funded much of the power acquisition. Liquidity is large, but 2026 commitments and guidance implying negative free cash flow will draw on it. | Medium | Adjusted EBITDA omits the acquired power business before April 2026, and covenant definitions are not supplied, so the 3.2x covenant leverage reported by management cannot be recomputed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Net debt to LTM adjusted EBITDA was 3.45x at June 2026, against 3.65x at FY2025 and 3.79x at March 2026. | Equity proceeds funded much of the acquisition, so debt rose modestly while adjusted EBITDA grew. | Medium |
| Liquidity at June 2026 was 1,742.0 US$m, mostly undrawn ABL; purchase commitments were $2.5 billion, with $587.9 million expected within twelve months. | Large commitments and implied negative free cash flow mean liquidity, not earnings, sets the 2026 funding risk. | Medium |
| Operating cash flow was 62.5% of LTM adjusted EBITDA, against 83.9% in FY2025, mainly because working capital absorbed cash. | Debt service leaned more on adjusted earnings than on cash generated in the first half of 2026. | Medium |
| Add-backs were 162,706 thousand USD, or 21.2% of LTM adjusted EBITDA; without them LTM total debt to EBITDA would be 4.61x. | Metrics built on adjusted EBITDA flatter cash earnings and need the add-back list beside them. | High |
| Management reports covenant leverage of 3.2x against a 5.25 to 1.00 maximum printed in the annual report, but current terms and definitions are not supplied. | Headroom looks wide but cannot be confirmed; the amended calculation applied only through June 30, 2026. | Low |

### Financial base view

The financial base is adequate for a bounded credit snapshot at the June 30, 2026 balance sheet date, with metrics that must be read as adjusted-EBITDA, principal-debt measures built from filed statements and company reconciliations. On those measures leverage has stepped down since December 2024: total debt to adjusted EBITDA is 4.31x at FY2024, 3.66x at FY2025, 3.92x on LTM March 2026 (when the notes refinancing had raised principal debt before the acquisition closed and before the May equity offering) and 3.63x on LTM June 2026. Interest cover on cash interest paid is 4.14x on LTM June 2026. Secured debt is small, because only the ABL is secured, and the next maturity of size is the ABL in 2030, followed by the unsecured notes from 2031. Three features temper that picture: the acquired power business contributes earnings only from April 1, 2026, so LTM EBITDA understates a full-year perimeter against debt and equity that already include its financing; operating cash conversion weakened in the first half of 2026; and purchase commitments rose sharply while guidance implies negative free cash flow in 2026. Covenant headroom is stated by management, not recomputed. No pension, retiree, factoring or supply-chain finance obligations were located in the 10-K or June 2026 10-Q.

| Dimension | View | Basis and limitation |
| --- | --- | --- |
| Leverage | Lower than FY2024 and FY2025, on adjusted EBITDA | Company-defined adjusted EBITDA; principal debt only; no pro forma EBITDA for the acquired business (Not calculable, see Gaps) |
| Coverage | Adequate on cash interest, uneven by quarter | Quarterly cash interest is derived by subtraction and is lumpy |
| Liquidity | Large undrawn ABL plus cash | Upper bound: ABL availability depends on a borrowing base the pack does not give |
| Cash flow quality | Weaker in the first half of 2026 | Working capital absorbed cash; free cash flow was negative in the second quarter |
| Definitions | Material add-backs; covenant terms not supplied | See Definition risks and Gaps |

### Source basis and entity scope

All amounts are for the consolidated registrant, Kodiak Gas Services, Inc., which operates through Kodiak Gas Services, LLC (the senior notes issuer; 10-Q 2026-06-30 page:11, page:22-23). The same four strings apply in every period: currency USD, unit thousands (except where a table says US$m or x), consolidated perimeter of the registrant and its subsidiaries, US GAAP. Annual statements are audited (10-K page:97); quarterly statements are unaudited; earnings release figures are management-attributed non-GAAP or summary figures and yield to filed statements. The acquired power business is in the consolidated perimeter from April 1, 2026 only (10-Q 2026-06-30 page:12).

### Reported income statement and EBITDA

USD thousands. Annual columns use the two-segment basis of the 10-K (Contract Services, now renamed Compression Infrastructure); the June 2026 quarterly recasts 2025 quarter and half-year comparatives to three segments. The recast and the renaming do not alter consolidated totals (10-Q 2026-06-30 page:33).

| Line | FY2024 | FY2025 | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 | Locators |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 1,159,311 | 1,308,100 | 322,843 | 391,120 | 652,485 | 736,879 | 10-K page:99; 10-Q 2026-06-30 page:6 |
| Compression Infrastructure (FY: Contract Services) | 1,034,173 | 1,181,270 | 293,534 | 315,125 | 582,490 | 622,110 | same |
| Power Infrastructure | not a segment | not a segment | — | 32,891 | — | 32,891 | 10-Q 2026-06-30 page:6 |
| Other Services | 125,138 | 126,830 | 29,309 | 43,104 | 69,995 | 81,878 | same |
| Depreciation and amortization | 260,272 | 276,185 | 66,135 | 78,650 | 136,664 | 147,331 | 10-K page:99; 10-Q page:7 |
| Selling, general and administrative | 151,680 | 144,070 | 35,121 | 40,918 | 67,376 | 87,045 | same |
| Income from operations | 249,450 | 340,010 | 99,730 | 124,237 | 188,916 | 231,049 | 10-K page:100; 10-Q page:7 |
| Interest expense | 197,144 | 198,370 | 45,755 | 50,061 | 92,979 | 98,802 | same |
| Loss on extinguishment of debt | — | — | — | — | — | 36,512 | 10-Q page:7 |
| Net income | 50,334 | 81,588 | 39,984 | 52,144 | 71,020 | 70,004 | same |
| Adjusted EBITDA (company, non-GAAP) | 609,550 | 715,033 | 178,216 | 216,846 | 355,880 | 406,938 | release 2026-02-25 page:13; 10-Q page:56 |
| Adjusted EBITDA percentage | 52.6% | 54.7% | 55.2% | 55.4% | 54.5% | 55.2% | same |

FY2025 includes a loss on sale of assets of 61,566 (10-K page:100), of which the release shows 33,349 as loss on disposal of business and 28,217 as loss on sale of assets (release 2026-02-25 page:13), and other expense, net of 28,168 (10-K page:100).

### Reported balance sheet and cash flow

USD thousands.

| Line | Dec 31, 2024 | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 | Locators |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 4,750 | 3,179 | 94,363 | 137,553 | 10-K page:99; 10-Q 2026-03-31 page:5-6; 10-Q 2026-06-30 page:6 |
| Total current assets | 383,661 | 323,136 | 459,540 | 528,141 | same |
| Goodwill | 415,213 | 408,681 | 408,681 | 753,463 | same |
| Total assets | 4,435,123 | 4,318,017 | 4,494,642 | 5,500,629 | same |
| Total current liabilities | 319,369 | 385,942 | 359,973 | 365,000 | same |
| Long-term debt, net of unamortized debt issuance cost | 2,581,909 | 2,555,250 | 2,787,003 | 2,720,989 | same |
| Total liabilities | 3,061,516 | 3,110,621 | 3,319,636 | 3,336,205 | same |
| Total stockholders' equity | 1,373,607 | 1,207,396 | 1,175,006 | 2,164,424 | same |

| Cash flow line | FY2024 | FY2025 | H1 2025 | H1 2026 | Locators |
| --- | --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 327,987 | 599,740 | 291,500 | 170,647 | 10-K page:102; 10-Q 2026-06-30 page:9 |
| Purchase of property, plant and equipment | (336,956) | (315,472) | (160,171) | (318,579) | same |
| Acquisition of DPS, net of cash acquired | — | — | — | (575,965) | 10-Q 2026-06-30 page:9 |
| Dividends paid to stockholders | (133,886) | (159,557) | (76,593) | (92,601) | same |
| Repurchase of common shares | (40,000) | (103,968) | (19,956) | — | same |
| Proceeds from issuance of common stock, net | — | — | — | 836,132 | 10-Q 2026-06-30 page:9 |
| Cash paid for interest | 147,144 | 168,716 | 87,075 | 103,535 | 10-K page:102; 10-Q page:9 |
| Cash paid for taxes | 14,662 | 5,939 | 5,393 | 4,299 | same |

### Debt and capital structure at June 30, 2026

Principal amounts, USD thousands, from the debt note (10-Q 2026-06-30 page:19-24). The ABL is secured by essentially all the assets of the Company (page:21); the notes are described as senior unsecured (page:22-23). The issuer of the notes is Kodiak Gas Services, LLC; guarantors are not named in the located text (see Gaps).

| Instrument | Principal Jun 30, 2026 | Principal Dec 31, 2025 | Terms stated | Locator |
| --- | --- | --- | --- | --- |
| ABL Facility | 380,917 | 464,647 | Commitments of $2.0 billion; SOFR plus 1.75% to 2.50% or prime plus 0.75% to 1.50%; weighted average rate 6.03% at June 30, 2026; commitment fee 0.25% on unused; maturity September 5, 2030; $14.6 million letters of credit outstanding; lockbox if availability below $100.0 million for five consecutive business days | page:20-21 |
| 7.25% senior notes due 2029 | — | 750,000 | Issued February 2, 2024 (10-K page:122); legally defeased March 30, 2026 with a deposit of $785.5 million; redeemed April 10, 2026 at 103.625% | page:21-22 |
| 5.875% senior notes due 2031 | 1,000,000 | — | Issued March 20, 2026; make-whole before April 1, 2028; call at 102.938% from April 1, 2028 | page:22 |
| 6.50% senior notes due 2033 | 770,000 | 770,000 | $600.0 million issued September 5, 2025 plus $170.0 million add-on September 22, 2025; callable from October 1, 2028 | page:23 |
| 6.75% senior notes due 2035 | 630,000 | 630,000 | $600.0 million issued September 5, 2025 plus $30.0 million add-on; callable from October 1, 2030 | page:23 |
| Total debt outstanding | 2,780,917 | 2,614,647 | Printed total of the four lines above | page:19-20 |
| Other borrowings | 4,283 | 395 | Shown on a separate line, outside the printed total | page:20 |
| Interest rate swap | notional 325,000 | not extracted for this date | Cash flow hedge on ABL variable rate, matures September 5, 2030; asset of 10,128 at June 30, 2026 | page:24-25 |

Maturities as printed (page:24), USD thousands: remainder of 2026: 1,822; 2027: 2,461; 2028: nil; 2029: nil; 2030: 380,917; thereafter: 2,400,000; total 2,785,200. The note instruments mature in 2031, 2033 and 2035 per the MD&A contractual obligations paragraph (page:48). The indentures limit distributions, investments, debt, liens, asset sales, mergers, affiliate transactions and unrestricted subsidiaries, and most restrictions fall away on investment-grade ratings from two of three agencies (page:24). The 2029 notes are no longer outstanding, so the 10-K wording that the ABL maturity springs to November 16, 2028 if more than $200.0 million of 2029 notes remain (10-K page:121) is no longer engaged on the printed facts; the latest quarterly states only the 2030 date (page:21). This refines difference D4 of the source-readiness handoff.

Claims outside the debt total, USD thousands unless stated (10-Q 2026-06-30):

| Claim | Amount | Inside the debt figure? | Locator |
| --- | --- | --- | --- |
| Finance lease liabilities (current 2,621; noncurrent 45,625) | 48,246 | No | page:32 |
| Operating lease liabilities | 48,259 | No | page:32 |
| Future minimum finance lease payments, undiscounted | 80,841 | No | page:32 |
| Purchase commitments (new compression and power units; includes a multi-year Baker Hughes arrangement) | $2.5 billion, of which $587.9 million within twelve months | No | page:29 |
| Accrued capital expenditures | $48.0 million | No (in payables and accruals) | page:29 |
| Sales tax contingency (Texas portion) | $65.8 million; accrued liabilities line "Sales tax liability" 69,635 | No (settlement of earlier matters paid in the first quarter of 2026) | page:29, page:30-31 |
| Sanctions-related payments matter (self-reported to US authorities) | Not estimated; payments "not material" | No | page:30 |
| Letters of credit under the ABL | $14.6 million | Inside ABL availability, not drawn | page:21, page:30 |
| Pension, retiree medical, factoring, supply-chain finance | Not located | Not applicable | searched in both filings |

The filing gives two sales tax figures (65.8 million for the Texas portion in Note 13 and 69,635 for the accrued liabilities line) without a bridge; both are logged, neither is reconciled. Purchase commitments stood at $276.4 million at March 31, 2026 (10-Q 2026-03-31 page:34), so commitments rose sharply in the quarter. The filing states the commitments include a multi-year Baker Hughes power generation arrangement (page:29); the release separately announces a one gigawatt gas turbine order (release 2026-08-06 page:2); the pack does not say whether the two are the same.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 4.31 | 4.30 | x | Total debt is principal of ABL and senior notes at Dec 31, 2024 (2,625,097) over FY2024 company adjusted EBITDA (609,550); cash 4,750; excludes other borrowings and leases; adjusted EBITDA is non-GAAP |
| FY2025 | 3.66 | 3.65 | x | Principal 2,614,647 over FY2025 adjusted EBITDA 715,033; cash 3,179; management reports a credit agreement ratio of 3.5x on a different definition (release 2026-02-25 page:2) |
| LTM Mar-2026 | 3.92 | 3.79 | x | Principal 2,849,936 over LTM adjusted EBITDA 727,461 (FY2025 plus Q1 2026 less Q1 2025); cash 94,363; excludes acquired power EBITDA; the 2029 notes are excluded because they were defeased on March 30, 2026 though redeemed April 10, 2026 |
| LTM Jun-2026 | 3.63 | 3.45 | x | Principal 2,780,917 over LTM adjusted EBITDA 766,091; cash 137,553; excludes acquired power EBITDA before April 1, 2026 so leverage is overstated against a pro forma perimeter (pro forma EBITDA Not calculable); management reports 3.2x and 3.1x netting all cash on a covenant basis (release 2026-08-06 page:5) |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 4.14 | x | Adjusted EBITDA 609,550 over cash paid for interest 147,144 (10-K page:102); cash interest paid is a cash-timing measure and differs from interest expense |
| FY2025 | 4.24 | x | Adjusted EBITDA 715,033 over cash paid for interest 168,716; interest expense was 198,370, so cover on expense is lower (3.60x, see Calculations) |
| LTM Mar-2026 | 4.76 | x | LTM adjusted EBITDA 727,461 over LTM cash interest 152,735 (FY2025 plus Q1 2026 41,349 less Q1 2025 57,330) |
| LTM Jun-2026 | 4.14 | x | LTM adjusted EBITDA 766,091 over LTM cash interest 185,176 (FY2025 plus H1 2026 103,535 less H1 2025 87,075); the ABL covenant minimum is 2.5x on a defined basis not supplied |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2024 | 4.8 | Not supplied: ABL commitments before the September 2025 amendment are not printed in the pack | US$m | Cash 4,750 (10-K page:99); ABL drawn 1,875,097 (10-K page:119) |
| Sep 30, 2025 | 0.7 | 1,476.1 | US$m | Commitments 2,000,000 less drawn 521,492 less letters of credit 2,400 (10-Q 2025-09-30 page:6, page:16-17); upper bound, borrowing base not supplied |
| Dec 31, 2025 | 3.2 | 1,534.0 | US$m | Commitments 2,000,000 less drawn 464,647 less letters of credit 1,400 (10-K page:72, page:119); company states $1.5 billion available (10-K page:69); borrowing base not supplied |
| Mar 31, 2026 | 94.4 | 1,548.7 | US$m | Commitments 2,000,000 less drawn 449,936 less letters of credit 1,400 (10-Q 2026-03-31 page:11-12); company states $1.5 billion available (page:34) |
| Jun 30, 2026 | 137.6 | 1,604.5 | US$m | Commitments 2,000,000 less drawn 380,917 less letters of credit 14,600 (10-Q 2026-06-30 page:20-21); company states $1.6 billion available and $1.7 billion total liquidity (page:48; release 2026-08-06 page:5); the ABL matures September 5, 2030, so no facility expires within twelve months; borrowing base not supplied |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of 2026 | 1.8 | US$m | Other borrowings (equipment financing) per maturity table, 10-Q 2026-06-30 page:24 |
| 2027 | 2.5 | US$m | Other borrowings, page:24 |
| 2028 | 0.0 | US$m | Printed as nil, page:24 |
| 2029 | 0.0 | US$m | Printed as nil; the 2029 notes were redeemed April 10, 2026, page:22, page:24 |
| 2030 | 380.9 | US$m | ABL drawn balance at June 30, 2026; matures September 5, 2030; revolving, so repayment depends on cash generation or refinancing, page:21, page:24 |
| 2031 | 1,000.0 | US$m | 5.875% senior unsecured notes, page:22, page:48 |
| 2033 | 770.0 | US$m | 6.50% senior unsecured notes, page:23, page:48 |
| 2035 | 630.0 | US$m | 6.75% senior unsecured notes, page:23, page:48 |

### Financials and credit metrics

| Metric | FY2024 | FY2025 | LTM Jun-2026 | Basis and locator |
| --- | --- | --- | --- | --- |
| Revenue (USD thousands) | 1,159,311 | 1,308,100 | 1,392,494 | Reported; LTM is FY2025 plus H1 2026 less H1 2025 |
| Adjusted EBITDA (USD thousands) | 609,550 | 715,033 | 766,091 | Company non-GAAP; LTM is the sum of four reported quarters |
| Adjusted EBITDA percentage | 52.6% | 54.7% | 55.0% | Calculated for LTM; reported for years |
| Net income (USD thousands) | 50,334 | 81,588 | 80,572 | Reported; LTM calculated |
| Total debt, principal (USD thousands) | 2,625,097 | 2,614,647 | 2,780,917 | Debt notes |
| Cash (USD thousands) | 4,750 | 3,179 | 137,553 | Balance sheets |
| Net debt (USD thousands) | 2,620,347 | 2,611,468 | 2,643,364 | Calculated |
| Total debt / adjusted EBITDA (x) | 4.31 | 3.66 | 3.63 | Calculated |
| Net debt / adjusted EBITDA (x) | 4.30 | 3.65 | 3.45 | Calculated |
| Cash paid for interest (USD thousands) | 147,144 | 168,716 | 185,176 | Reported; LTM calculated |
| Adjusted EBITDA / cash interest (x) | 4.14 | 4.24 | 4.14 | Calculated |
| Operating cash flow (USD thousands) | 327,987 | 599,740 | 478,887 | Reported; LTM calculated |
| Operating cash flow / adjusted EBITDA | 53.8% | 83.9% | 62.5% | Calculated |
| Discretionary cash flow, company (USD thousands) | 373,281 | 461,684 | 518,932 | Company non-GAAP; LTM calculated |
| Free cash flow, company (USD thousands) | 122,319 | 229,581 | 61,538 | Company non-GAAP; LTM calculated |
| Unrestricted liquidity: cash plus undrawn ABL (US$m) | Not supplied: Dec 2024 commitments not printed | 1,537.1 | 1,742.0 | Calculated; borrowing base not supplied |
| Management-reported credit agreement leverage (x) | Not supplied: not in the pack for Dec 2024 | 3.5 | 3.2 | Attributed to management; release 2026-02-25 page:2 and 2026-08-06 page:5; definition not supplied |
| Add-backs in adjusted EBITDA (USD thousands) | Not calculated | 127,006 | 162,706 | Calculated from company reconciliations |

### Quarterly trend and the latest quarter

USD thousands, discrete quarters from the Q4 2025, Q1 2026 and Q2 2026 releases and the June 2026 quarterly.

| Line | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | Locator |
| --- | --- | --- | --- | --- | --- |
| Total revenues | 322,744 | 332,871 | 345,759 | 391,120 | release 2026-02-25 page:3; release 2026-08-06 page:5 |
| Adjusted EBITDA | 174,702 | 184,451 | 190,092 | 216,846 | same |
| Adjusted EBITDA percentage | 54.1% | 55.4% | 55.0% | 55.4% | same |
| Net income (loss) | (14,197) | 24,765 | 17,860 | 52,144 | release 2026-02-25 page:12; 10-Q 2026-03-31 page:8; 10-Q 2026-06-30 page:7 |
| Net cash provided by operating activities | 113,378 | 194,862 | 71,182 | 99,465 | release 2026-02-25 page:14; release 2026-08-06 page:15 |
| Discretionary cash flow | 116,652 | 112,524 | 126,505 | 163,251 | same |
| Free cash flow | 33,463 | 78,609 | 36,962 | (87,496) | same |

The four quarters sum to the LTM June 2026 figures used above for revenue, adjusted EBITDA, net income, operating cash flow, discretionary cash flow and free cash flow, which cross-checks the LTM construction (Calculations C1).

Second quarter 2026 (three months ended June 30, 2026), by segment (10-Q 2026-06-30 page:34): Compression Infrastructure revenue 315,125 with adjusted gross margin 220,690 (70.0%, release page:6); Power Infrastructure revenue 32,891 with adjusted gross margin 21,205 (64.5%); Other Services revenue 43,104 with adjusted gross margin 4,869 (11.3%, against 24.5% in Q2 2025, release page:6). Compression Infrastructure fleet utilisation was 98.2% against 97.2% a year earlier; the power fleet was 405 MW with 89.6% utilisation (10-Q page:38). Revenue rose 21.1% against Q2 2025 (10-Q page:39), of which the power business supplied 32,891.

Financing events and milestones in the period, with amounts as printed:

| Event | Amount | Date | Locator |
| --- | --- | --- | --- |
| Fifth Amendment to the ABL credit agreement; modifies the leverage ratio calculation, allowing deduction of net proceeds of the 2031 notes through June 30, 2026 in addition to the $50.0 million cash netting cap | not applicable | April 2, 2026 | 10-Q 2026-06-30 page:21 |
| Issue of 5.875% notes due 2031 | $1.0 billion; fees $14.3 million | March 20, 2026 | page:22-23 |
| Defeasance and redemption of 7.25% notes due 2029; loss on extinguishment 36,512 (premium 27.2 million, deferred costs 7.8 million, accrued interest 1.5 million) | cash outlay $785.5 million | deposit March 30, redemption April 10, 2026 | page:21-22 |
| Acquisition of Distributed Power Solutions, LLC | cash $587.3 million and 2.4 million shares valued at $139.0 million; fair value of consideration 726,354; cash paid net of cash acquired 575,965; goodwill 344,782; preliminary allocation | closed April 1, 2026 | page:12-13; page:9 |
| Common stock offering | net proceeds about $836.1 million | closed May 15, 2026 | page:26 |
| Gas compression equipment buyout (operating lease options, about 43,000 horsepower) | about $32.8 million | July 2026 (subsequent event) | 10-Q page:35; release 2026-08-06 page:2 |
| Dividend declared, $0.49 per share, and equivalent unit distribution | not applicable | declared August 5, payable August 27, 2026 (subsequent event) | 10-Q page:29 |

No material event after August 6, 2026 appears in the pack (see Gaps, no filing for the quarter ended September 30, 2026).

### Cash flow quality and add-backs

Operating cash flow for H1 2026 was 170,647 against 291,500 for H1 2025; the MD&A attributes the decrease to working capital, which used 154.6 million in H1 2026 against 19.8 million in H1 2025, mainly an increase in receivables on revenue growth and collection timing (10-Q 2026-06-30 page:49). Free cash flow was negative in the second quarter at (87,496) because growth and other capital expenditure of 254,870 (including a 42.6 million non-cash finance lease addition, page:58) exceeded discretionary cash flow of 163,251.

Add-backs between GAAP net income and adjusted EBITDA (USD thousands; computed in C5):

| Add-back | FY2025 | LTM Jun-2026 | Nature |
| --- | --- | --- | --- |
| Loss on extinguishment of debt | — | 36,512 | Redemption premium 27.2 million, deferred financing costs written off 7.8 million, accrued interest 1.5 million (10-Q 2026-06-30 page:22); one-off refinancing |
| Loss on disposal of business | 33,349 | 33,349 | Loss of $33.3 million on the sale of the Mexico operations on September 30, 2025 (10-K page:113) |
| Sales tax reserve | 27,968 | 27,968 | Recorded in Q3 2025 as interest and penalties on a settlement offer (release 2026-02-25 page:13); the matters were settled and paid in full in the first quarter of 2026 (10-Q 2026-06-30 page:29), so it is a cash cost |
| Loss on sale of assets | 28,217 | 16,620 | Ordinary asset disposals |
| Equity compensation | 24,529 | 25,789 | Recurring, non-cash |
| Transaction expenses | 4,102 | 13,931 | Mainly the power acquisition in 2026 |
| Severance | 2,497 | 2,193 | Small |
| Long-lived asset impairment | 6,344 | 6,344 | Non-cash write-off of legacy software (10-K page:119) |
| Total add-backs | 127,006 | 162,706 | 21.2% of LTM adjusted EBITDA (C5) |

Cash taxes paid are low against tax expense (LTM cash taxes 4,845 against LTM expense 31,768; C5), because deferred tax provisions were 37,207 in H1 2026 (10-Q page:9); the filings do not explain the driver beyond the effective tax rate note (page:31).

### Covenants and definition risks

| Test | Level | Reported figure | Headroom | Locator and limitation |
| --- | --- | --- | --- | --- |
| Maximum Leverage Ratio (Total Indebtedness less the lesser of unrestricted cash and $50.0 million, over EBITDA, each as defined) | 5.25 to 1.00 | Management: 3.5x at Dec 2025, 3.6x Q1 2026, 3.2x Q2 2026, 3.1x netting all cash | On management's 3.2x, 2.05 turns, or an indicative 39.0% EBITDA cushion (C8); not recomputed | 10-K page:72; releases; the ABL agreement and Fifth Amendment are not supplied; the amended calculation applied "Through June 30, 2026" |
| Maximum Secured Leverage Ratio (Senior Secured Debt less the lesser of cash and $50.0 million, over EBITDA) | 3.25 to 1.00 | Not supplied: not reported | On this analysis secured debt (ABL drawn 380,917) is 0.50x LTM adjusted EBITDA (C8), indicative only | 10-K page:72; senior secured debt as defined is not supplied |
| Minimum interest coverage ratio | 2.5x | Not supplied: not reported | On this analysis 4.14x on cash interest, indicative only (not the covenant definition) | 10-K page:72 |
| Compliance statement | not applicable | "we were in compliance with all covenants under the ABL Facility" at June 30, 2026 | not applicable | 10-Q 2026-06-30 page:21 |

Definition risks, each with the difference it creates:

- Adjusted EBITDA is the company's non-GAAP measure with nine categories of add-back (10-Q 2026-06-30 page:55); the covenant EBITDA is a separate defined term not supplied, so the covenant ratio and the ratio computed here are different measures and are never mixed.
- Total debt here is principal of the ABL and notes. It excludes other borrowings (4,283), finance leases (48,246) and operating leases (48,259). Including all of them gives 3.76x on LTM adjusted EBITDA (C8).
- The September 2025 debt table in the earlier quarterly includes bond premium inside its total (10-Q 2025-09-30 page:16), unlike later tables; this module uses December 2024, December 2025, March 2026 and June 2026 debt tables, all on the later basis, and does not use the September 2025 total as a leverage input (difference D2 of the source-readiness handoff).
- Free cash flow and discretionary cash flow are company non-GAAP measures that add back severance, transaction expenses and (in 2025) the sales tax reserve (10-Q page:57), so they are not equal to operating cash flow less purchases of property, plant and equipment.

### Guidance and forward funding (management, attributed)

Revised 2026 guidance includes the power business for three quarters (release 2026-08-06 page:7), against initial guidance that excluded it (release 2026-02-25 page:4-5):

| Item (USD thousands) | Initial low | Initial high | Revised low | Revised high |
| --- | --- | --- | --- | --- |
| Adjusted EBITDA | 750,000 | 780,000 | 830,000 | 860,000 |
| Discretionary cash flow | 480,000 | 510,000 | 570,000 | 600,000 |
| Maintenance capital expenditures | 75,000 | 85,000 | 80,000 | 90,000 |
| Growth capital expenditures | 235,000 | 265,000 | 680,000 | 750,000 |
| Other capital expenditures | 40,000 | 50,000 | 45,000 | 55,000 |
| Total growth and other capital expenditures | 275,000 | 315,000 | 725,000 | 805,000 |

On revised guidance, discretionary cash flow less total growth and other capital expenditure spans (235,000) to (125,000) (C9), before dividends; the declared dividend of $0.49 per share on 101,104,031 shares outstanding at August 3, 2026 (10-Q page:1, page:29) is about 49,541 per quarter (C9). Management states it expects to fund dividends and growth capital expenditure from discretionary cash flow, with the ABL or lower growth spending as the fallback, and that dividends require pro forma ABL availability of at least $100,000,000 (10-Q page:48). The guidance is a management claim and does not constrain the figures above.

### Consumption of the source-readiness handoff

The source-readiness handoff was opened and its limitations are applied as follows. Its differences: D1 (acquisition price, announced approximately $675.0 million versus closing fair value 726,354) is carried; this module uses the closing figures from the June 2026 quarterly and treats the announced value as signing-date only. D2 is applied by not using the September 2025 total debt as an input. D3 is resolved by arithmetic here: the maturity table total 2,785,200 equals total debt outstanding 2,780,917 plus other borrowings 4,283 (C10), although the filing does not state that bridge. D4 is refined above. D5 is resolved in part: segment capital expenditures of 318,579 for six months equal the cash purchase of property, plant and equipment (page:9, page:34), while growth capital expenditure is a different company measure that includes accrual and non-cash items; the segment allocation of the accrual difference is not disclosed, so the power segment figures 118,012 and 134,371 are not bridged (C11). D6 is applied by labelling the segment basis in every table. Its gaps G1 and G2 (no credit agreement, no 2026 covenant levels) restrict the covenant table above; G6 (preliminary purchase accounting) and G7 (no three-segment annual recast) restrict the acquisition and segment content; G5 (no filing after the June 2026 quarter) fixes the latest balance sheet date; G11 (management ratios appear only in releases) is why the 3.5x, 3.6x and 3.2x are shown as attributed claims. The handoff does not contain a figure that this module contradicts.

## Calculations

All inputs are USD thousands from the cited sources unless stated; LTM means the 12 months ended on the date shown. Results are rounded for presentation only after computing.

- C1. LTM June 2026 construction. Revenue: 1,308,100 (FY2025, 10-K page:99) + 736,879 (H1 2026, 10-Q page:6) - 652,485 (H1 2025) = 1,392,494. Adjusted EBITDA: 715,033 (release 2026-02-25 page:13) + 406,938 (10-Q page:56) - 355,880 = 766,091. Check by four quarters: 174,702 + 184,451 + 190,092 + 216,846 = 766,091. Net income: 81,588 + 70,004 - 71,020 = 80,572; four quarters (14,197) + 24,765 + 17,860 + 52,144 = 80,572. Operating cash flow: 599,740 + 170,647 - 291,500 = 478,887; four quarters 113,378 + 194,862 + 71,182 + 99,465 = 478,887. Discretionary cash flow: 461,684 + 289,756 - 232,508 = 518,932; four quarters 116,652 + 112,524 + 126,505 + 163,251 = 518,932. Free cash flow: 229,581 + (50,534) - 117,509 = 61,538; four quarters 33,463 + 78,609 + 36,962 + (87,496) = 61,538 (H1 values from 10-Q page:57-58).
- C2. LTM March 2026 adjusted EBITDA: 715,033 + 190,092 - 177,664 (Q1 2025, 10-Q 2026-03-31 page:43) = 727,461; check Q2 2025 178,216 + Q3 2025 174,702 + Q4 2025 184,451 + Q1 2026 190,092 = 727,461. Cash interest: 168,716 + 41,349 - 57,330 (10-Q 2026-03-31 page:8) = 152,735.
- C3. LTM June 2026 cash interest: 168,716 + 103,535 - 87,075 = 185,176. Quarterly cash interest by subtraction: Q2 2026 = 103,535 - 41,349 = 62,186; Q2 2025 = 87,075 - 57,330 = 29,745. Revenue LTM March 2026 = 1,308,100 + 345,759 - 329,642 = 1,324,217.
- C4. Leverage. FY2024: 2,625,097 / 609,550 = 4.31x; net (2,625,097 - 4,750) = 2,620,347 / 609,550 = 4.30x. FY2025: 2,614,647 / 715,033 = 3.66x; net 2,611,468 / 715,033 = 3.65x. LTM March 2026: 2,849,936 / 727,461 = 3.92x; net (2,849,936 - 94,363) = 2,755,573 / 727,461 = 3.79x. LTM June 2026: 2,780,917 / 766,091 = 3.63x; net (2,780,917 - 137,553) = 2,643,364 / 766,091 = 3.45x. Interest cover on cash interest: 609,550 / 147,144 = 4.14x; 715,033 / 168,716 = 4.24x; 727,461 / 152,735 = 4.76x; 766,091 / 185,176 = 4.14x. Cover on interest expense: FY2025 715,033 / 198,370 = 3.60x; FY2024 609,550 / 197,144 = 3.09x; LTM June 2026 interest expense 198,370 + 98,802 - 92,979 = 204,193, 766,091 / 204,193 = 3.75x.
- C5. Unadjusted EBITDA and add-backs. FY2025: net income 81,588 + interest 198,370 + tax 31,884 + depreciation and amortization 276,185 = 588,027; add-backs 6,344 + 24,529 + 2,497 + 4,102 + 27,968 + 33,349 + 28,217 = 127,006; 588,027 + 127,006 = 715,033, equal to the reported figure. LTM June 2026: net income 80,572 + interest 204,193 + tax (31,884 + 23,853 - 23,969 = 31,768) + D&A (276,185 + 147,331 - 136,664 = 286,852) = 603,385; add-backs: loss on extinguishment 36,512; disposal of business 33,349; sales tax reserve 27,968; loss on sale of assets 28,217 + 4,220 - 15,817 = 16,620; equity compensation 24,529 + 14,529 - 13,269 = 25,789; transaction expenses 4,102 + 11,615 - 1,786 = 13,931; severance 2,497 + 72 - 376 = 2,193; impairment 6,344; total 162,706; 603,385 + 162,706 = 766,091 (equal to C1). Share of add-backs: 162,706 / 766,091 = 21.2%. Unadjusted leverage: 2,780,917 / 603,385 = 4.61x; net 2,643,364 / 603,385 = 4.38x. Cash taxes LTM: 5,939 + 4,299 - 5,393 = 4,845; tax expense LTM 31,768 as above.
- C6. Cash conversion. Operating cash flow / adjusted EBITDA: FY2024 327,987 / 609,550 = 53.8%; FY2025 599,740 / 715,033 = 83.9%; LTM June 2026 478,887 / 766,091 = 62.5%. Adjusted EBITDA percentage LTM: 766,091 / 1,392,494 = 55.0%. Purchase of PP&E LTM: 315,472 + 318,579 - 160,171 = 473,880. Dividends LTM: 159,557 + 92,601 - 76,593 = 175,565.
- C7. Liquidity. Undrawn = 2,000,000 - drawn - letters of credit. Sep 30, 2025: 2,000,000 - 521,492 - 2,400 = 1,476,108. Dec 31, 2025: 2,000,000 - 464,647 - 1,400 = 1,533,953; with cash 3,179 gives 1,537,132. Mar 31, 2026: 2,000,000 - 449,936 - 1,400 = 1,548,664. Jun 30, 2026: 2,000,000 - 380,917 - 14,600 = 1,604,483; with cash 137,553 gives 1,742,036. The December 2025, March 2026 and June 2026 results agree with the company statements of about $1.5 billion, $1.5 billion and $1.6 billion available; no statement was checked for September 2025. Purchase commitments within twelve months 587,900 / 1,742,036 = 33.7% of June 2026 liquidity (shown for scale; not used elsewhere).
- C8. Covenant-related indications. Management 3.2x against 5.25x: 5.25 - 3.2 = 2.05 turns; EBITDA cushion 1 - 3.2 / 5.25 = 39.0%. Secured debt: ABL drawn 380,917 / 766,091 = 0.50x. Lease-inclusive total debt: 2,780,917 + 4,283 + 48,246 + 48,259 = 2,881,705; / 766,091 = 3.76x. Secured leverage and interest cover here use analyst definitions and are not the covenant calculations.
- C9. Guidance and dividend. Low-case discretionary cash flow less high-case capital expenditure: 570,000 - 805,000 = (235,000). High-case: 600,000 - 725,000 = (125,000). Quarterly dividend: $0.49 x 101,104,031 shares = 49,541 thousand (rounded); excludes the corresponding Kodiak Services distribution on OpCo Units, paired with 224 thousand preferred shares at June 30, 2026 (10-Q page:9, page:26, page:35).
- C10. Maturity table check: 2,780,917 + 4,283 = 2,785,200, equal to the printed total on page:24. Other borrowings 4,283 equals remainder-2026 1,822 plus 2027 2,461.
- C11. Capital expenditure bridge, Q2 2026: growth and other capital expenditure 254,870 (release 2026-08-06 page:6) less non-cash finance lease addition 42,600 less increase in accrued capital expenditure 32,000 (10-Q page:58) = 180,270; cash purchase of PP&E for the quarter 200,209 (318,579 - 118,370 for Q1 2026, 10-Q 2026-03-31 page:8) less maintenance capital expenditure 19,947 = 180,262; the 8 difference is rounding of the 42.6 million and 32.0 million disclosed in millions. Expense block reconciliation, Q2 2026: revenue 391,120 less cost of operations (94,435 + 11,686 + 38,235 = 144,356) less depreciation and amortization 78,650 less SG&A 40,918 less loss on sale of assets 2,959 = 124,237, equal to reported income from operations. FY2025: 1,308,100 less cost of operations (373,493 + 106,432 = 479,925) less 276,185 less impairment 6,344 less SG&A 144,070 less loss on sale of assets 61,566 = 340,010, equal to reported.

Not calculable: pro forma LTM adjusted EBITDA including the acquired power business for the three months before April 1, 2026 (the pack gives pro forma revenue and earnings only, 10-Q 2026-06-30 page:15); a recomputed covenant leverage or coverage ratio (covenant definitions not supplied); leverage at September 30, 2025 on a common basis is not used (D2).

## Gaps

| Id | Gap | Effect and handling | Remediation |
| --- | --- | --- | --- |
| H1 | Pro forma adjusted EBITDA for the acquired power business before April 1, 2026 is Not calculable | LTM June 2026 leverage of 3.63x is overstated against a full-year perimeter; guidance for 2026 includes three quarters of the business | Obtain the acquired business's earnings from the April 1, 2026 current report or later filings |
| H2 | Covenant definitions, the ABL credit agreement, the Fifth Amendment and 2026 covenant levels are Not supplied (carries G1, G2) | Covenant ratios stay management claims; headroom shown is indicative | Add the credit agreement and amendments |
| H3 | ABL borrowing base and availability limits are Not supplied | Undrawn commitment is an upper bound; the company's own availability statements agree at each date | Add borrowing base disclosures if filed |
| H4 | Guarantor identities and note guarantee structure not located (carries G3) | Structural analysis of claims on subsidiaries is not possible | Add indentures and guarantor schedules |
| H5 | No pension, retiree medical, factoring or supply-chain finance disclosure located | Treated as not disclosed, not as zero; absence of such obligations is not established | Confirm in later filings |
| H6 | Annual 2025 and 2024 segment data are on the two-segment basis; Q3 and Q4 2025 segment figures are not recast (carries G7) | Segment trends across the April 2026 change use the June 2026 recast comparatives only | Add a recast annual table if filed |
| H7 | No filing or release for the quarter ended September 30, 2026 (carries G5) | Latest balance sheet is June 30, 2026; subsequent events are limited to those printed to August 6, 2026 | Add any later periodic filing dated on or before 2026-11-05 |
| H8 | Purchase price allocation for the acquisition is preliminary | Goodwill 344,782 and acquired asset values may change within the measurement period | Monitor later filings |
| H9 | Sales tax liability appears as 65.8 million (Texas portion) and 69,635 (accrued liabilities line) without a bridge | Both reported; the contingency is treated as a claim outside debt | None available from the pack |
| H10 | Cash interest by quarter is derived by subtraction and quarterly cash interest is uneven | LTM measures are used for cover; single-quarter cover is not shown | None |
| H11 | Sanctions-related payments matter has no estimated penalty (carries G10) | Unquantified contingency | Monitor |
| H12 | Management ratios (3.5x, 3.6x, 3.2x, 3.1x) are in releases only (carries G11) | Shown as attributed claims | None |
| H13 | Market data, ratings and peer data are blank in the context (carries G4, G12) | No market-implied or relative metrics are produced | Supply if wanted |

## Next module

Proceed to CP-1A (business and transaction context), which should consume this handoff for the figures that frame the transaction: the April 1, 2026 acquisition (closing consideration 726,354 and the D1 signing-date difference), the March 2026 notes refinancing, the May 2026 equity offering, the 2026 guidance, the purchase commitments and the segment recast. It must carry forward: leverage 3.63x total and 3.45x net on LTM June 2026 adjusted EBITDA, with the pro forma caveat; liquidity 1,742.0 US$m with the borrowing base caveat; add-backs of 21.2%; covenant terms Not recomputed; the sanctions-related matter unquantified; and gaps H1 to H13. CP-2 and CP-5 follow in the order CP-OS sets and must cite this handoff's figures by their table and calculation labels.
