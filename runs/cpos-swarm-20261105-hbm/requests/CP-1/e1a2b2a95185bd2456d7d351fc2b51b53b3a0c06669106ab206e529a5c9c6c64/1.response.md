## Request

Issuer: Hudbay Minerals Inc. (issuer id hbm; TSX and NYSE ticker HBM), consolidated with its subsidiaries. As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, stated in millions of US dollars (US$m) unless a line says otherwise. Current period named by the context: Q2 2026 (quarter and six months ended 2026-06-30). Prior period named by the context: FY2025.

Task: build the financial base. That means reported statement values with period and perimeter labels, separately labelled calculation bridges, an evidence-based reading of leverage, coverage, cash flow quality and liquidity, the debt and claims register, and a short gap list. This is an intermediate artifact, not the final report.

Locator convention. `page:N` is the extraction chunk of the named source, not the printed page. Source short names are fixed in `## Sources`.

Reliance on the readiness handoff. The upstream handoff is relied on for its perimeter warnings, its gap list, its statement that no covenant level is supplied, and its five named conflicts. This answer re-checked those against the sources. It finds no correction needed to the readiness handoff. It adds four items the readiness handoff left for downstream work: the release that labels carrying value as principal, the pro forma view that removes ring-fenced Copper World items, the reconstruction of a December 2025 principal figure, and the facility-level liquidity limit (all in Findings and Gaps).

## Sources

### Issuer sources relied on

| Short name | Source name | sha256 | Used for |
| --- | --- | --- | --- |
| 40-F | 40-F_2025-12-31_form40f.htm.jsonl | 2e155789735b2bff45a2bcbe054290dc180366fb4697dc24f2f2d4f1c7050c41 | Share count on the cover (page:1); confirms audited annual exhibits are not in the pack (page:2-3) |
| Q3MDA | 6-K-EX-99.1_2025-09-30_exhibit99-1.htm.jsonl | 55a93575304a5e2b953260f4e274c5a39ae30021f2c92b99af4427f537390e4f | Q3 2025 and nine-month 2025 figures, liquidity text, contractual obligations at 2025-09-30, quarterly history |
| Q1FS | 6-K-EX-99.1_2026-03-31_exhibit99-1.htm.jsonl | 532cee6ac6a8650d6600327aa510e9427055b8d19ea466fcd1e56834f9e80c49 | Q1 2026 filed interim statements and debt note |
| Q2FS | 6-K-EX-99.1_2026-06-30_exhibit99-1.htm.jsonl | 12a37c8778b0cbc30486cf54048199e1b52e4f3eeea4aa98f015138ba6c8b8ca | Controlling source for Q2 2026 and six-month statements, notes, debt and liquidity |
| PR-FY25 | 6-K-EX-99.3_2025-12-31_exhibit99-3.htm.jsonl | 99f49739a1f92152e3b1a86a18c1ee2162a4da0c2cc8d427da3a3335818d9569 | Q4 2025 and FY2025 headline figures and non-GAAP tables (management release) |
| PR-Q1 | 6-K-EX-99.3_2026-03-31_exhibit99-3.htm.jsonl | ada0c26b16ac32d6f2b222633c4110e11a601b22fd66b81f76af348b97d3b4a8 | Q1 2026 non-GAAP tables and liquidity (management release) |
| PR-Q2 | 6-K-EX-99.3_2026-06-30_exhibit99-3.htm.jsonl | 5519d54c6ee343772d1472890091915c574ee3b20549bcd2dd8544703027a844 | Q2 2026 non-GAAP tables, liquidity, net debt, trailing metrics (management release) |

The run context (sha256 021d8bac1e30ca507d1d237248f47111a88bf0caf21c22980b85e1e72c6ea47c) supplies run settings only and is not issuer evidence. Its ratings, quotes, valuation, borrower, parent and guarantor fields are blank and are treated as not supplied, never as zero.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | e9dbd2ab9d4365edb1c5ad19429b023878f8b986a46fedd1e14735a884877657 | Source readiness: source classes, perimeter, five conflicts, gap list, locator convention |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported leverage is low: debt of 860.2 against trailing adjusted EBITDA of 1,271.6, or 0.68 times. Liquidity is now mostly cash, and part of that cash is ring-fenced. | Medium | No covenant level, full-year cash interest or audited FY2025 statement is supplied, and trailing earnings are a management measure. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Trailing adjusted EBITDA rose in each of the last three quarters, to 1,271.6, and total debt fell to 860.2 from 1,008.6. | Reported leverage is low and improving, but the earnings measure is the company's own non-GAAP definition. | Medium |
| Undrawn revolver fell to 153.7 from 425.2 after a 272.0 draw helped repay the 2026 notes; headline liquidity is 1,044.6. | Committed back-up liquidity is smaller, and the group now relies on cash, part of which is restricted. | High |
| Of cash of 890.9, an amount of 334.5 is held by Copper World LLC and restricted to that project. | Cash available to the wider group is lower than the headline, and net debt looks better than it is for the rest of the group. | High |
| The next scheduled funded debt maturities are 272.0 in 2028 and 542.4 in 2029. | There is no funded maturity before 2028, but the 2028 and 2029 maturities fall close together. | High |
| Capital spending of 293.1 took more than half of six-month operating cash flow of 508.3, which is already after taxes paid of 262.8. | Free cash flow is real but sensitive to tax and project spending, including the Copper World decision. | Medium |

### Financial base view

On reported figures Hudbay is lightly leveraged and strongly cash generative, but its liquidity structure changed materially in Q2 2026. Trailing adjusted EBITDA reached 1,271.6 at 2026-06-30, the highest of the five trailing quarter-ends in the pack (995.7, 932.3, 1,060.9, 1,195.6 and 1,271.6). Total long-term debt was 860.2, down from 1,008.6 at 2025-12-31, so the ratio of debt to trailing adjusted EBITDA was 0.68 times on carrying value, against 0.95 times at 2025-12-31. The company's own net debt was negative 80.5, which would read as net cash. That headline needs three qualifications. First, cash of 890.9 includes 334.5 held by Copper World LLC, which the company says is contractually restricted to the Copper World project. Second, the company deducts a further 49.8 of restricted bond proceeds. Third, those proceeds come from the 52.0 of municipal bonds, which are debt of Copper World LLC guaranteed by the company. If Copper World cash, the restricted proceeds and the bonds are all set aside, net debt for the rest of the group is 253.1, or 0.20 times (derived in Calculations). The composition of liquidity changed: undrawn revolver was 153.7 at 2026-06-30 against 425.2 at 2026-03-31, because the 2026 notes of 472.5 were repaid on 2026-04-01 using cash and a 272.0 revolver draw. Headline liquidity of 1,044.6 compares with 956.5 that the company gave for 2026-03-31 after the repayment (PR-Q1 page:6). The next funded maturities are the revolver draw at its November 2028 facility maturity and the 6.125% notes of 542.4 due April 2029. The earnings base is strong but not cheap to convert to cash: Q2 2026 tax expense was 102.3 on pre-tax income of 240.4, and six-month taxes paid were 262.8. Earnings fell between Q1 2026 and Q2 2026 (adjusted EBITDA 421.9 to 321.2), which management attributes to lower sales volumes after port closures in Peru delayed shipments that were delivered in July. The base has five limits. No covenant level or ratio is printed. The audited FY2025 statements are not supplied, so FY2025 figures come from a management release. Cash interest for a full year is not printed. Facility-level revolver availability is not printed. The free cash flow history differs between releases.

### Income statement (US$m, filed, unaudited, consolidated)

Source: Q2FS page:1-2; Q1FS page:1. Three-month and six-month columns are as printed. Hudbay Minerals Inc. and subsidiaries, IFRS, consolidated; the Cactus project was acquired on 2026-06-24 and contributed no income or expense in the six-day stub (Q2FS page:30).

| Line | Q2 2026 | Q2 2025 | Six months 2026 | Six months 2025 | Q1 2026 (Q1FS) |
| --- | --- | --- | --- | --- | --- |
| Revenue | 631.3 | 536.4 | 1,388.6 | 1,131.3 | 757.3 |
| Mine operating costs | 273.5 | 263.5 | 562.9 | 519.0 | 289.4 |
| Depreciation and amortization in cost of sales | 88.8 | 96.4 | 188.7 | 204.5 | 99.9 |
| Gross profit | 269.0 | 176.5 | 637.0 | 407.8 | 368.0 |
| Selling and administrative expenses | 19.9 | 20.7 | 54.3 | 34.4 | 34.4 |
| Exploration expenses | 19.2 | 9.4 | 35.4 | 23.3 | 16.2 |
| Other operating expenses | 4.7 | 7.1 | 14.8 | 12.3 | 10.1 |
| Re-evaluation adjustment, environmental provision | 5.5 | (13.8) | 7.6 | (1.0) | 2.1 |
| Results from operating activities | 219.7 | 153.1 | 524.9 | 338.8 | 305.2 |
| Interest expense on long term debt | 13.3 | 15.6 | 27.7 | 31.5 | 14.4 |
| Accretion on streaming arrangements | 4.5 | 5.2 | 9.0 | 9.6 | 4.5 |
| Change in fair value of financial instruments | (48.7) | (4.1) | (111.6) | (9.3) | (62.9) |
| Other net finance expense (income) | 10.2 | (16.7) | 20.4 | (17.4) | 10.2 |
| Other (income) expenses | (20.7) | none | (54.5) | 14.4 | (33.8) |
| Income before tax | 240.4 | 153.1 | 579.4 | 324.4 | 339.0 |
| Tax expense | 102.3 | 38.4 | 249.8 | 110.5 | 147.5 |
| Net income | 138.1 | 114.7 | 329.6 | 213.9 | 191.5 |
| Attributable to owners | 137.4 | 117.7 | 327.8 | 218.1 | 190.4 |
| Non-controlling interest | 0.7 | (3.0) | 1.8 | (4.2) | 1.1 |

The Q2 2025 "Other (income) expenses" cell is printed as a dash in the filing and is shown as none; it is not carried into any calculation. The "Other (income) expenses" line is the subtotal of the four finance lines above it in each period (13.3 + 4.5 - 48.7 + 10.2 = -20.7), not an additional item; income before tax ties without it (Calculations).

### Balance sheet (US$m, filed, unaudited)

Source: Q2FS page:1; Q1FS page:1. The 2025-12-31 column is the audited year-end balance as shown in the interim comparatives; the audited statements themselves are not in the pack.

| Line | 2026-06-30 | 2025-12-31 |
| --- | --- | --- |
| Cash and cash equivalents | 890.9 | 568.9 |
| Trade and other receivables (current) | 204.0 | 377.8 |
| Inventories (current) | 189.8 | 199.2 |
| Other financial assets (current, includes restricted cash 50.1 and 0.2) | 53.3 | 0.8 |
| Total current assets | 1,356.3 | 1,163.1 |
| Receivables (non-current, includes deferred consideration 173.0) | 188.8 | 16.1 |
| Other financial assets (non-current, investments at fair value) | 153.9 | 130.9 |
| Property, plant and equipment | 6,196.5 | 4,693.9 |
| Total assets | 8,062.0 | 6,223.3 |
| Trade and other payables | 318.3 | 342.8 |
| Taxes payable | 63.9 | 117.4 |
| Other financial liabilities (current) | 95.0 | 122.9 |
| Lease liabilities (current) | 27.0 | 26.7 |
| Current portion of long-term debt | none (dash) | 472.1 |
| Deferred revenue (current) | 33.2 | 52.1 |
| Total current liabilities | 604.5 | 1,228.7 |
| Other financial liabilities (non-current) | 274.2 | 155.0 |
| Lease liabilities (non-current) | 26.0 | 29.3 |
| Long-term debt (non-current) | 860.2 | 536.5 |
| Deferred revenue (non-current) | 263.9 | 265.0 |
| Environmental and other provisions (non-current) | 327.5 | 312.6 |
| Total liabilities (as printed) | 2,801.4 | 2,992.3 |
| Equity attributable to owners | 4,797.2 | 3,231.0 |
| Non-controlling interest | 463.4 | none (dash) |

Working capital as the company states it was 751.8 at 2026-06-30 (PR-Q2 page:7) and negative 65.6 at 2025-12-31, the latter negative because the 2026 notes were current. Equity rose by the 1,135.6 of shares issued for Arizona Sonoran and by the 581.5 recorded for the sale of 30% of Copper World (Q2FS page:4, page:23).

### Cash flow (US$m, filed, unaudited)

Source: Q2FS page:2-3; Q1FS page:2-3.

| Line | Q2 2026 | Q2 2025 | Six months 2026 | Six months 2025 |
| --- | --- | --- | --- | --- |
| Operating cash flow before change in non-cash working capital | 210.1 | 193.9 | 418.8 | 357.4 |
| Taxes paid (inside the line above) | (108.9) | (43.9) | (262.8) | (161.4) |
| Change in non-cash working capital | 86.9 | 66.0 | 89.5 | 27.3 |
| Cash generated from operating activities | 297.0 | 259.9 | 508.3 | 384.7 |
| Acquisition of property, plant and equipment | (152.9) | (121.7) | (293.1) | (213.1) |
| Cash and cash equivalents acquired in acquisitions, net | 11.9 | none | 11.9 | none |
| Net purchase of investments | (7.2) | none | (38.7) | (13.8) |
| Cash used in investing activities | (154.5) | (100.6) | (321.1) | (184.9) |
| Proceeds from drawdown on revolving credit facility | 272.0 | none | 272.0 | none |
| Repurchase of senior unsecured notes, net of discount | (472.5) | (50.0) | (472.5) | (50.0) |
| Interest paid on long-term debt | (30.0) | (29.9) | (30.0) | (29.9) |
| Lease payments | (9.0) | (9.3) | (18.4) | (18.4) |
| Equipment financing payments | (7.4) | (4.6) | (14.1) | (8.9) |
| Proceeds from sale of Copper World non-controlling interest, net | none | none | 411.7 | none |
| Dividends paid | (2.8) | none | (5.7) | (2.8) |
| Cash (used in) generated from financing activities | (253.8) | (98.9) | 138.1 | (119.7) |
| Net (decrease) increase in cash | (112.9) | 62.9 | 322.0 | 83.7 |
| Cash at end of period | 890.9 | 625.5 | 890.9 | 625.5 |

Q1 2026 (Q1FS page:2-3): cash generated from operating activities 211.3, acquisition of property, plant and equipment (140.2), taxes paid (153.9), no interest-paid line, net increase in cash 434.9, cash at end 1,003.8. The "none" entries are dashes printed in the filing. The Q2 2026 repurchase line is the repayment at maturity of the 4.50% notes, described in the debt note as repaid at maturity (Q2FS page:18).

### Company non-GAAP measures by quarter (US$m, management release tables)

Adjusted EBITDA, net debt and free cash flow are company non-GAAP measures. Adjusted EBITDA adds back tax, the finance subtotal, other operating expenses, depreciation and amortization, environmental re-evaluation, inventory adjustments and share-based compensation and deducts amortization of deferred revenue (PR-Q2 page:24). Source: PR-Q2 page:24-25; PR-Q1 page:25; PR-FY25 page:41.

| Measure | Q2 2026 | Q1 2026 | Q4 2025 | Q3 2025 | Q2 2025 |
| --- | --- | --- | --- | --- | --- |
| Adjusted EBITDA | 321.2 | 421.9 | 385.9 | 142.6 | 245.2 |
| Adjusted EBITDA, last twelve months | 1,271.6 | 1,195.6 | 1,060.9 | 932.3 | 995.7 |
| Cash sustaining capital expenditures | 108.3 | 106.4 | 111.9 (Feb release: 108.7) | 86.4 (Feb release: 85.5) | 107.2 (Feb release: 106.1) |
| Free cash flow | 101.8 | 102.3 | 225.0 (Feb release: 228.2) | (16.1) (Feb release: (15.2)) | 86.7 (Feb release: 87.5) |
| Cash generated from operations (company table) | 297.0 | 211.3 | 209.4 (July release prints 290.4) | 113.5 | 259.9 (Feb release: 259.6) |

Free cash flow in the company table is cash generated from operations less change in non-cash working capital less cash sustaining capital expenditures (PR-Q2 page:25). Both versions include community agreement cash payments in sustaining capital. For Q4 2025 that line is 4.4 in the February release and 7.6 in the later releases (PR-FY25 page:41; PR-Q1 page:25), a difference of 3.2 that equals the difference in sustaining capital (108.7 and 111.9) and in free cash flow (228.2 and 225.0).

### Operating KPIs (management release, not audited)

Source: PR-Q2 page:7; PR-FY25 page:11. Cash cost is per pound of copper produced, net of by-product credits, a non-GAAP measure.

| KPI | Q2 2026 | Q1 2026 | Q4 2025 | Q3 2025 | Q2 2025 |
| --- | --- | --- | --- | --- | --- |
| Copper produced (tonnes) | 28,267 | 27,929 | 33,069 | 24,205 | 29,956 |
| Gold produced (ounces) | 51,234 | 61,700 | 84,298 | 53,581 | 56,271 |
| Payable copper sold (tonnes) | 23,780 | 29,544 | 34,132 | 18,280 | 30,354 |
| Payable gold sold (ounces) | 56,266 | 66,562 | 84,424 | 38,279 | 62,466 |
| Cash cost (US$ per pound) | (0.40) | (1.80) | (0.63) | 0.42 | (0.02) |
| Sustaining cash cost (US$ per pound) | 1.39 | 0.00 | 0.94 | 2.09 | 1.65 |
| All-in sustaining cash cost (US$ per pound) | 1.80 | 0.73 | 1.43 | 2.78 | 2.03 |

Payable copper sold in Q2 2026 (23,780 tonnes) was lower than copper produced (28,267 tonnes). The release attributes the gap to ocean swells that closed Peruvian ports and delayed about 10,000 dry metric tonnes of concentrate, delivered in the first half of July 2026 (PR-Q2 page:5, subsequent event).

### Segments (US$m, filed)

Source: Q2FS page:30-32. Gross profit is as printed per segment; Copper World and Cactus have no revenue.

| Segment | Q2 2026 revenue | Q2 2026 gross profit | Q2 2025 revenue | Q2 2025 gross profit | Six months 2026 revenue | Six months 2026 gross profit | Six months 2025 revenue | Six months 2025 gross profit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peru | 273.3 | 115.5 | 259.6 | 75.8 | 636.3 | 281.9 | 549.3 | 168.8 |
| Manitoba | 258.4 | 146.3 | 193.0 | 95.1 | 544.9 | 332.6 | 417.8 | 223.5 |
| British Columbia | 99.6 | 7.2 | 83.8 | 5.6 | 207.4 | 22.5 | 164.2 | 15.5 |
| Total | 631.3 | 269.0 | 536.4 | 176.5 | 1,388.6 | 637.0 | 1,131.3 | 407.8 |

Segment assets at 2026-06-30: Peru 2,373.6, Manitoba 417.5, British Columbia 1,384.0, Copper World 1,772.6, Cactus 1,371.6, Corporate and other 742.7 (total 8,062.0; Q2FS page:32). Copper World and Cactus carry 3,144.2 of assets (derived) with no revenue.

### Debt and financing register (US$m, as at 2026-06-30 unless stated)

Source: Q2FS page:15-20 unless stated. Issuer: the notes are described as the obligation of "the Company" (Hudbay Minerals Inc.); the borrower under each revolving facility and the issuers of the other instruments are not named beyond the descriptions below. No instrument is shown with a co-issuer in the supplied text.

| Instrument | Amount | Rate | Maturity | Security and guarantors as printed |
| --- | --- | --- | --- | --- |
| 6.125% senior notes (2029 notes) | Principal 542.4; carrying 539.4 | 6.125% | April 2029 | Senior unsecured; guaranteed by substantially all subsidiaries other than HudBay (BVI) Inc., excluded or unrestricted subsidiaries and the subsidiaries holding the Copper World, Mason and Cactus projects (page:18). Implied original issue size 600.0 (542.4 outstanding plus 57.6 repurchased and retired, Q1FS page:13; derived) |
| 4.50% senior notes (2026 notes) | Repaid 472.5 on 2026-04-01; nil outstanding | 4.50% | April 2026 | Repaid using cash and the revolver draw (page:18) |
| Senior secured revolving credit facilities (two: Canadian and Peruvian) | Commitments 450.0; drawn 272.0 (Canadian); letters of credit 24.3 (Canadian) and nil (Peruvian) | Rate not printed | November 2028; accordion of 150.0 | Secured against substantially all assets other than those of Copper World, Mason and Cactus (page:19) |
| Senior unsecured municipal bonds (Arizona Industrial Development Authority, Series 2026A) | Principal 52.0; carrying 50.7 | 4.50%, interest paid semi-annually | Initial mandatory tender date 2036-07-02; final maturity not stated | Senior unsecured obligations of Copper World LLC, guaranteed by the Company and its primary operating subsidiaries (page:20); proceeds restricted to the project (page:14) |
| Total long-term debt as printed | 860.2 (539.4 + 270.1 + 50.7) | | | The revolver carrying value of 270.1 is the 272.0 draw less 1.9 of deferred transaction costs (page:19) |

Other financing and fixed claims (US$m, 2026-06-30), shown inside or outside the debt figure of 860.2:

| Claim | Amount and terms | Inside or outside the 860.2 | Locator |
| --- | --- | --- | --- |
| Financing related to property, plant and equipment | 131.3 (31.6 current, 99.7 non-current); rates 2.25% to 7.55%; expire 2026 to 2032 | Outside, in other financial liabilities | Q2FS page:15 |
| Lease liabilities | 53.0 (27.0 current, 26.0 non-current); rates 2.50% to 8.49%; expire 2026 to 2037; secured by lessor title | Outside | Q2FS page:17 |
| Deferred land payments from the Arizona Sonoran acquisition | 102.8 (5.0 current, 97.8 non-current); 6% interest; 5.0 a year in 2026 to 2028 and 82.2 on 2029-08-28; secured vendor carryback loans with deeds of trust | Outside, in other financial liabilities | Q2FS page:15-16 |
| Deferred and contingent Copper Mountain consideration | 14.8 deferred (3.0 current) payable 2026 to 2032; 14.3 contingent payable 2029 to 2033 | Outside | Q2FS page:15-16 |
| Agreements with communities | 89.5 (47.2 current, 42.3 non-current); payments to 2040 | Outside | Q2FS page:15-16 |
| Wheaton refund liability and streaming deferred revenue | 8.3 refund liability; deferred revenue 297.1 (33.2 current, 263.9 non-current), settled in precious metals, not cash | Outside | Q2FS page:15, page:20-21 |
| Decommissioning, restoration and similar liabilities | 336.7 of 388.6 total environmental and other provisions | Outside | Q2FS page:21 |
| Pensions and other employee benefits | Pension obligations 3.7 non-current and 2.0 current; other employee benefits 82.4 non-current and 4.0 current | Outside | Q2FS page:1, page:15 |
| Letters of credit and surety bonds | Other letters of credit: Peru 145.3, British Columbia 0.3; C$130.0 million facility with 55.7 issued; surety bonds Arizona 23.2, British Columbia 46.2 and 1.5; Peru nil | Outside; contingent, no cash collateral | Q2FS page:19-20 |
| Capital commitments | Manitoba 54.9 (52.4 terminable), British Columbia 14.0 (none terminable), Peru 19.2 (all terminable), Arizona 114.5 (112.3 terminable); total 202.6 | Outside | Q2FS page:29 |
| Derivative liabilities | 8.2, fair value level 2 | Outside | Q2FS page:15, page:27-28 |
| Factoring, supply chain finance, take-or-pay, retiree medical and consent-decree funding | Not found: a search of all sources for these terms and synonyms found none; the only retiree-type item is other employee benefits above | Not applicable | search of all seven sources |

### Maturity wall and what is not in it

Funded debt maturities by year are in the chart table below. Other scheduled payments outside it, from the register: deferred land payments of 5.0 a year in 2026 to 2028 and 82.2 on 2029-08-28; deferred Copper Mountain consideration of 3.0 a year; PP&E financing, leases and community agreements amortising to 2032, 2037 and 2040. A current contractual obligations table is not supplied. The only one in the pack is dated 2025-09-30 and shows long-term debt obligations of 1,217.7 including scheduled interest, purchase obligations other than capital of 1,274.7, decommissioning of 491.2 undiscounted and a total of 3,564.5 (Q3MDA page:46). It predates the April 2026 repayment, the revolver draw, the municipal bonds and the Arizona Sonoran land payments and is not used to build the wall.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q2 2026 (2026-06-30) | 0.68 | -0.06 | x | Total long-term debt 860.2 and company net debt (80.5) over company LTM adjusted EBITDA 1,271.6 (PR-Q2 page:6, page:24-25). Carrying value, not principal (principal 866.4). Company net debt deducts all cash of 890.9, including 334.5 held by Copper World LLC. EBITDA is a non-GAAP management measure; no covenant definition is supplied |
| Q2 2026 excluding ring-fenced Copper World items | 0.64 | 0.20 | x | Derived: debt less municipal bonds 809.5; net debt 809.5 less cash excluding Copper World LLC 556.4 is 253.1; over 1,271.6. The 49.8 restricted bond proceeds are set aside with the bonds. Analyst view, not a company or covenant measure |
| Q1 2026 (2026-03-31) | 0.84 | 0.00 | x | Total long-term debt 1,009.4 and net debt 5.6 over LTM adjusted EBITDA 1,195.6 (PR-Q1 page:6; PR-Q2 page:25). Company prints 0.0. The 2026 notes of 472.5 were still outstanding. Cash included 370.7 held by Copper World LLC |
| FY2025 (2025-12-31) | 0.95 | 0.41 | x | Total long-term debt 1,008.6 and net debt 439.7 over LTM adjusted EBITDA 1,060.9 (PR-FY25 page:10, page:41). Company prints 0.4. Debt and EBITDA are from a management release; audited statements not supplied |
| Q3 2025 (2025-09-30) | 1.12 | 0.47 | x | Total long-term debt 1,047.0 and net debt 435.9 over LTM adjusted EBITDA 932.3 (Q3MDA page:9; PR-FY25 page:41). Company prints 0.5 |
| Q2 2025 (2025-06-30) | 1.06 | 0.44 | x | Total long-term debt 1,059.6 and net debt 434.1 (Q3MDA page:74) over LTM adjusted EBITDA 995.7 (PR-FY25 page:41; PR-Q2 page:25) |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| LTM Q2 2026 | Not supplied: cash interest paid for the second half of 2025 is not printed in any source | x | LTM adjusted EBITDA 1,271.6 is supplied; cash interest paid over the same twelve months is not. Interest paid appears only as a six-month 2026 line (30.0) and a nine-month 2025 narrative amount (30.2, Q3MDA page:43) |
| FY2025 | Not supplied: the FY2025 cash flow statement and full-year interest paid are not in the pack | x | Adjusted EBITDA 1,060.9 is supplied (PR-FY25 page:41) |
| Six months 2026 | 24.77 | x | Adjusted EBITDA 743.1 (321.2 + 421.9) over interest paid on long-term debt 30.0 (Q2FS page:3). Overstates cover on a full-year basis: the Q1 2026 statements print no interest-paid line and the whole 30.0 falls in Q2, so the window appears to hold one coupon date for the notes (coupon dates are not printed) |
| Q2 2026 | 10.71 | x | Adjusted EBITDA 321.2 over interest paid 30.0. Same timing limit; a single quarter containing the only payment of the half-year |
| Six months 2025 | 17.81 | x | Adjusted EBITDA 532.4 (245.2 + 287.2) over interest paid 29.9 (Q2FS page:3). Same timing limit |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 2026-06-30 | 890.9 | 153.7 | US$m | Company total liquidity 1,044.6 (PR-Q2 page:6). Undrawn is 450.0 less 272.0 drawn less 24.3 letters of credit. Cash includes 334.5 held by Copper World LLC and restricted to the project; excludes 49.8 of restricted municipal bond proceeds. The split of availability between the Canadian and Peruvian facilities is not printed |
| 2026-03-31 | 1,003.8 | 425.2 | US$m | Company total liquidity 1,429.0 before the April repayment, 956.5 after it (PR-Q1 page:6). Cash included 370.7 held by Copper World LLC (PR-Q1 page:6) |
| 2025-12-31 | 568.9 | 424.8 | US$m | Undrawn availability stated for 2025-12-31 (PR-FY25 page:5); cash from Q2FS page:1. The company's post-closing adjusted figures (992 of cash, over 1.4 billion of liquidity) add the January 2026 Copper World proceeds and are not used here |
| 2025-09-30 | 611.1 | 425.2 | US$m | Company total liquidity 1,036.3 (Q3MDA page:8). Cash label is "Cash and cash equivalents and short-term investments" in the financial condition table (page:9) |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| H2 2026 | 0.0 | US$m | No funded principal maturity printed after the 2026 notes were repaid on 2026-04-01 (Q2FS page:18). Amortising items (leases, equipment financing, deferred land payments) are outside this table |
| 2027 | 0.0 | US$m | No funded principal maturity printed in the debt note |
| 2028 | 272.0 | US$m | Canadian revolver draw; both facilities mature November 2028 (Q2FS page:19). Principal drawn, not carrying value of 270.1. No extension is printed |
| 2029 | 542.4 | US$m | 6.125% senior notes due April 2029, principal (Q2FS page:18) |
| 2030 to 2035 | 0.0 | US$m | No funded principal maturity printed in the debt note for these years |
| 2036 | 52.0 | US$m | Municipal bonds: initial mandatory tender date 2036-07-02 (Q2FS page:14, page:20). A tender date is not necessarily the final maturity, which is not stated |

### Financials and credit metrics

| Metric (US$m unless stated) | Q2 2026 | Q1 2026 | Q4 2025 | Q3 2025 | Q2 2025 | FY2025 | LTM Q2 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 631.3 | 757.3 | 732.9 | 346.8 | 536.4 | 2,211.0 | 2,468.3 (derived) |
| Cost of sales | 362.3 | 389.3 | 462.8 | 281.5 | 359.9 | 1,467.8 | 1,495.9 (derived) |
| Gross profit | 269.0 | 368.0 | 270.1 (derived) | 65.3 (derived) | 176.5 | 743.2 (derived) | 972.4 (derived) |
| Net income | 138.1 | 191.5 | 128.0 | 222.4 | 114.7 | 564.3 | 680.0 (derived) |
| Adjusted EBITDA (company, non-GAAP) | 321.2 | 421.9 | 385.9 | 142.6 | 245.2 | 1,060.9 | 1,271.6 |
| Adjusted EBITDA margin on revenue (%) | 50.9 (derived) | 55.7 (derived) | 52.7 (derived) | 41.1 (derived) | 45.7 (derived) | 48.0 (derived) | 51.5 (derived) |
| Operating cash flow before change in working capital | 210.1 | 208.7 | 336.9 | 70.3 | 193.9 | 764.3 | 826.0 (derived) |
| Cash generated from operating activities | 297.0 | 211.3 | 209.4 | 113.5 | 259.9 | 707.3 | 831.2 |
| Cash sustaining capital expenditures | 108.3 | 106.4 | 111.9 | 86.4 | 107.2 | 376.4 (Feb release basis) | 413.0 |
| Free cash flow (company) | 101.8 | 102.3 | 225.0 | (16.1) | 86.7 | 387.9 (Feb release basis) | 413.0 |
| Cash and cash equivalents (period end) | 890.9 | 1,003.8 | 568.9 | 611.1 | 625.5 | 568.9 | 890.9 |
| Total long-term debt (carrying) | 860.2 | 1,009.4 | 1,008.6 | 1,047.0 | 1,059.6 | 1,008.6 | 860.2 |
| Net debt (company) | (80.5) | 5.6 | 439.7 | 435.9 | 434.1 | 439.7 | (80.5) |
| Total debt / LTM adjusted EBITDA (x, derived) | 0.68 | 0.84 | 0.95 | 1.12 | 1.06 | 0.95 | 0.68 |
| Net debt / LTM adjusted EBITDA (x, derived) | -0.06 | 0.00 | 0.41 | 0.47 | 0.44 | 0.41 | -0.06 |
| Tax expense | 102.3 | 147.5 | 129.1 | 108.1 | 38.4 | 347.7 (derived) | 487.0 (derived) |
| Effective tax rate on income before tax (%) | 42.6 (derived) | 43.5 (derived) | 50.2 (derived) | 32.7 (derived) | 25.1 (derived) | 38.1 (derived) | 41.7 (derived) |

### Interpretation

#### Leverage

On the company's definitions the group moved from net debt of 439.7 at 2025-12-31 to negative 80.5 at 2026-06-30. Total long-term debt fell by 148.4 while cash rose by 322.0. The cash rise came from financing as well as operations: the sale of a 30% interest in Copper World brought in 411.7 net of costs (Q2FS page:3), and the company reports 334.5 of cash held at Copper World LLC at 2026-06-30. Trailing adjusted EBITDA was 995.7 at Q2 2025, fell to 932.3 at Q3 2025, then rose to 1,060.9, 1,195.6 and 1,271.6, so the debt ratio fell through both a lower numerator and a higher denominator since the Q3 2025 low. The ratio uses company adjusted EBITDA, which adds back share-based compensation and deducts amortization of deferred revenue, and is not a covenant measure. The principal view is slightly higher than carrying: 866.4 at 2026-06-30. A reader using debt plus leases plus equipment financing plus deferred land payments gets 1,147.3 (860.2 + 53.0 + 131.3 + 102.8, derived), or 0.90 times trailing adjusted EBITDA. The company's net debt excludes all four of those claims.

The February release says "reduced total principal debt to $1,008.6 million as of December 31, 2025" (PR-FY25 page:22). That figure is the carrying value of total long-term debt (Q2FS page:18). The principal at that date reconstructs to 1,014.9: the Q1 2026 note shows 1,014.9 of notes principal at 2026-03-31 with no repurchases in the quarter (Q1FS page:13), and the revolver was undrawn. This is an inference, because no source prints the 2025-12-31 principal. The release's wording is a label error, not a different number.

#### Coverage

Interest cover on a cash basis cannot be built for a full year because full-year interest paid is not printed. The six-month ratio of 24.77 times is very high and is probably overstated by timing: the cash flow statements show 30.0 of interest paid in Q2 2026 and no interest-paid line in Q1 2026, so the half-year appears to contain one coupon date for the notes (dates are not printed). On an accrual basis, interest expense on long term debt was 27.7 for six months 2026, equal to 26.83 times six-month adjusted EBITDA of 743.1 (derived). Accretion on streaming arrangements of 9.0 is a further non-cash charge. The revolver draw of 272.0 (April 2026) and the municipal bonds of 52.0 (24 June 2026) add interest cost: the bonds carry 4.50%, about 2.3 a year (derived), and the 6.125% notes carry about 33.2 a year on 542.4 (derived). The revolver rate is not printed, so the run-rate cost of the draw cannot be stated. Coupon dates are not printed.

#### Cash flow quality

Six-month cash generated from operating activities was 508.3 against 384.7 a year earlier, helped by a working capital inflow of 89.5 (27.3 in 2025), of which trade and other receivables contributed 175.5 (Q2FS page:29). The receivables inflow reverses part of the year-end build and the Q2 port-closure effect: trade receivables fell from 343.8 to 163.1 "primarily due to a delay in scheduled shipments in Peru impacted by the temporary port closures" (Q2FS page:13). That makes Q2 operating cash flow of 297.0 a partly timing-driven figure; operating cash flow before working capital, 210.1, is the cleaner series and was essentially flat on Q1 (208.7). Taxes paid were 262.8 for six months against 161.4 a year earlier. Cash taxes equal 35.4% of six-month adjusted EBITDA (derived). Six-month capital spending on property, plant and equipment was 293.1 against 213.1. Free cash flow on the company definition was 101.8 in Q2 and 102.3 in Q1, so 204.1 for the half (derived). Net purchase of investments of 38.7 sits outside that definition (Q2FS page:3). Dividends are small, 5.7 for six months.

#### Liquidity

Company total liquidity of 1,044.6 is cash of 890.9 plus 153.7 of undrawn revolver. Of the cash, 334.5 is held by Copper World LLC under contractual restriction (PR-Q2 page:25) and is not available to the rest of the group. Cash excluding it is 556.4, and liquidity on the same basis is 710.1 (derived). Undrawn availability fell from 425.2 to 153.7 over the quarter and the facilities are now 65.8% used including letters of credit: (272.0 + 24.3) / 450.0 (derived). The sources do not say how the 450.0 divides between the Canadian and Peruvian facilities. Because the draw and the letters of credit sit on the Canadian facility, the company's 153.7 is an aggregate that holds only if the Canadian commitment exceeds 296.3 (derived) or the facilities can be combined; neither is printed. Neither facility matures within twelve months. Restricted municipal bond proceeds of 49.8 are classified as current and expected to be drawn within twelve months (Q2FS page:14). Near-term cash demands visible in the filings: about 30 million at Cactus and about 20 million of Mason evaluation spending in the second half of 2026 (PR-Q2 page:19, page:22), capital commitments of 202.6 of which 18.7 is not terminable (derived), and the July dividend declaration of C$0.01 per share (PR-Q2 page:22). The company states that current liquidity and operating cash flow should be sufficient for the remainder of 2026 (PR-Q2 page:6), a management statement.

The Copper World joint venture also carries a receivable: Mitsubishi is to contribute 180.0 within 18 months of closing, recorded at 173.0 at 2026-06-30 (Q2FS page:9, page:13). That inflow is contractual, belongs to Copper World, and is not counted in liquidity.

#### Latest quarter and events after quarter-end

Financing events in Q2 2026: repayment of 472.5 of 4.50% notes on 2026-04-01; 272.0 revolver draw; 52.0 municipal bond issue on 2026-06-24; Arizona Sonoran acquisition completed 2026-06-24 for 46,794,082 shares valued at 1,135.6 plus Hudbay's existing stake of 123.1, net identifiable assets 1,267.0 including 102.8 of deferred land payments assumed and cash acquired of 63.0 (Q2FS page:8). Closing payments of 49.3 were made by Arizona Sonoran between 2026-06-24 and 2026-06-30 (page:8). The Copper World joint venture closed in January 2026 with cash of 422.7 received (Q2FS page:9). Insurance business interruption recovery of 11.5 was recorded and fully received (Q2FS page:11). Subsequent to quarter-end the documents show only: delivery in the first half of July of the delayed concentrate (about 10,000 dry metric tonnes), the dividend declaration of 2026-07-28, executive appointments, and the statement that the Copper World sanctioning decision is on track for late 2026 (PR-Q2 page:4-5, page:15, page:22). Amounts or events after 2026-07-29 are Not supplied.

Disasters and legal items: the interim statements contain no litigation or consent-decree note. The wildfire insurance recovery relates to 2025 Manitoba evacuations. The judicial review application by the Lower Similkameen Indian Band against the New Ingerbelle permit amendment is disclosed only in release narrative (PR-Q2 page:19; PR-Q1 page:15) with no financial amount.

#### Earnings quality and definitions

Adjusted EBITDA differs from IFRS earnings in several recurring ways: it deducts 9.5 of amortization of deferred revenue in Q2 (non-cash stream revenue), adds back 10.2 of share-based compensation, and starts from net earnings after a finance subtotal that was a net credit of 20.7 in Q2 because of 48.7 of fair-value gains on investments and share-based compensation instruments (Q2FS page:12-13 and PR-Q2 page:24). Mark-to-market gains of 38.2 are excluded from adjusted net earnings (PR-Q2 page:24), so reported net income of 138.1 includes gains that adjusted net earnings attributable to owners of 113.5 does not. The effective tax rate was 42.6% in Q2 2026 and 43.1% for six months (derived), reflecting mining taxes of 32.7 current and 1.4 deferred in Q2 alongside income tax (Q2FS page:22). Revenue includes pricing and volume adjustments of negative 36.7 in Q2, mark-to-market on provisionally priced sales (Q2FS page:10); the net position awaiting final pricing was a liability of 9.5 at 2026-06-30 (Q2FS page:29). Q2 gross profit ties to the segment note. Gold and silver stream deferred revenue of 297.1 is amortised into revenue without cash; 9.5 was amortised in Q2 (Q2FS page:10, page:20).

Definition risks carried forward: the free cash flow history differs between the February release and the May and July releases (CP-0 conflict 2); the July release prints 290.4 for Q4 2025 cash generated from operations against 209.4 elsewhere and its own trailing total of 831.2 supports 209.4 (CP-0 conflict 3); the share count at 2025-12-31 differs between the 40-F cover and the interim share note (CP-0 conflict 1); the municipal bond final maturity is not stated (CP-0 conflict 4).

## Calculations

Inputs are cited from filed statements and releases. "Derived" figures are my arithmetic. Amounts in US$m.

| Item | Formula and inputs | Result | Perimeter and period |
| --- | --- | --- | --- |
| Total debt tie, 2026-06-30 | 539.4 + 270.1 + 50.7 (Q2FS page:18) | 860.2, equals printed | Consolidated |
| Total debt tie, 2025-12-31 | 472.1 + 538.8 - 2.3 (Q2FS page:18) | 1,008.6, equals printed | Consolidated |
| Principal debt, 2026-06-30 | 542.4 + 272.0 + 52.0 | 866.4 | Consolidated |
| Principal debt, 2025-12-31, reconstructed | 472.5 + 542.4 (Q1FS page:13; no 2026 repurchases) | 1,014.9, inference | Consolidated |
| Net debt, company, 2026-06-30 | 860.2 - 890.9 - 49.8 (PR-Q2 page:24) | -80.5, equals printed | Consolidated |
| Undrawn revolver | 450.0 - 272.0 - 24.3 (Q2FS page:19) | 153.7, equals PR-Q2 page:6 | Two facilities combined |
| Total liquidity | 890.9 + 153.7 | 1,044.6, equals printed | Consolidated |
| Liquidity excluding Copper World LLC cash | 890.9 - 334.5 + 153.7 | 710.1 | Derived |
| Cash excluding Copper World LLC cash | 890.9 - 334.5 | 556.4 | Derived |
| Debt excluding municipal bonds | 860.2 - 50.7 | 809.5 | Derived |
| Net debt excluding ring-fenced items | 809.5 - 556.4 | 253.1 | Derived |
| Leverage ratios | 860.2 / 1,271.6; -80.5 / 1,271.6; 809.5 / 1,271.6; 253.1 / 1,271.6 | 0.676, -0.063, 0.637, 0.199, shown as 0.68, -0.06, 0.64, 0.20 | LTM Q2 2026 |
| Leverage ratios, prior dates | 1,009.4 / 1,195.6 and 5.6 / 1,195.6; 1,008.6 / 1,060.9 and 439.7 / 1,060.9; 1,047.0 / 932.3 and 435.9 / 932.3; 1,059.6 / 995.7 and 434.1 / 995.7 | 0.844 and 0.005; 0.951 and 0.414; 1.123 and 0.468; 1.064 and 0.436 | Q1 2026, FY2025, Q3 2025, Q2 2025 |
| LTM adjusted EBITDA tie | 321.2 + 421.9 + 385.9 + 142.6 (PR-Q2 page:25) | 1,271.6, equals printed | LTM Q2 2026 |
| LTM revenue | 631.3 + 757.3 + 732.9 + 346.8 | 2,468.3 | LTM Q2 2026 |
| LTM cost of sales | 362.3 + 389.3 + 462.8 + 281.5 | 1,495.9; gross profit 972.4 | LTM Q2 2026 |
| LTM net income | 138.1 + 191.5 + 128.0 + 222.4 | 680.0 | LTM Q2 2026 |
| LTM operating cash flow before working capital | 210.1 + 208.7 + 336.9 + 70.3 | 826.0 | LTM Q2 2026 |
| LTM cash generated from operations | 297.0 + 211.3 + 209.4 + 113.5 | 831.2, equals printed; with 290.4 it would be 912.2 | LTM Q2 2026 |
| LTM free cash flow | 101.8 + 102.3 + 225.0 - 16.1 | 413.0, equals printed | LTM Q2 2026 |
| Q4 2025 free cash flow, later version | 209.4 + 127.5 - 111.9 (PR-Q1 page:25) | 225.0, equals printed | Q4 2025 |
| Q2 2026 free cash flow tie | 297.0 - 86.9 - 108.3 | 101.8, equals printed | Q2 2026 |
| Adjusted EBITDA margins | 321.2 / 631.3; 421.9 / 757.3; 385.9 / 732.9; 142.6 / 346.8; 245.2 / 536.4; 1,060.9 / 2,211.0; 1,271.6 / 2,468.3 | 50.9, 55.7, 52.7, 41.1, 45.7, 48.0, 51.5 per cent | As labelled |
| Gross profit, derived columns | 732.9 - 462.8; 346.8 - 281.5; 2,211.0 - 1,467.8 | 270.1, 65.3, 743.2 | Q4 2025, Q3 2025, FY2025 |
| FY2025 tax expense | 912.0 - 564.3 (PR-FY25 page:11) | 347.7 | FY2025 |
| LTM tax expense | 102.3 + 147.5 + 129.1 + 108.1 | 487.0 | LTM Q2 2026 |
| LTM income before tax | 240.4 + 339.0 + 257.1 + 330.5 | 1,167.0 | LTM Q2 2026 |
| Effective tax rates | 102.3 / 240.4; 147.5 / 339.0; 129.1 / 257.1; 108.1 / 330.5; 38.4 / 153.1; 347.7 / 912.0; 487.0 / 1,167.0; six months 249.8 / 579.4 | 42.6, 43.5, 50.2, 32.7, 25.1, 38.1, 41.7 and 43.1 per cent | As labelled |
| Revenue growth | 631.3 / 536.4 - 1; 1,388.6 / 1,131.3 - 1 | 17.7% and 22.7% | Q2 and six months 2026 against 2025 |
| Adjusted EBITDA change | 321.2 / 421.9 - 1; 321.2 / 245.2 - 1 | -23.9% against Q1 2026; +31.0% against Q2 2025 | Quarter |
| Income before tax tie, Q2 2026 | 219.7 - 13.3 - 4.5 + 48.7 - 10.2 | 240.4, equals printed | Q2 2026 |
| Finance subtotal tie | 13.3 + 4.5 - 48.7 + 10.2; 27.7 + 9.0 - 111.6 + 20.4 | -20.7; -54.5, equal the "Other (income) expenses" lines | Q2 and six months 2026 |
| Financing cash flow tie, six months 2026 | 272.0 - 472.5 + 1.0 - 3.0 - 30.0 - 5.9 - 18.4 - 14.1 + 3.0 + 411.7 - 5.7 | 138.1, equals printed | Six months 2026 |
| Net change in cash tie, six months 2026 | 508.3 - 321.1 + 138.1 - 3.3 | 322.0, equals printed | Six months 2026 |
| Cash taxes against adjusted EBITDA | 262.8 / 743.1 | 35.4% | Six months 2026 |
| Six-month adjusted EBITDA | 321.2 + 421.9; 245.2 + 287.2 | 743.1; 532.4 | Six months 2026; six months 2025 |
| Interest cover | 743.1 / 30.0; 321.2 / 30.0; 532.4 / 29.9; accrual 743.1 / 27.7 | 24.77, 10.71, 17.81, 26.83 times | As labelled, with timing limit |
| Lease-adjusted debt, indicative | 860.2 + 53.0 + 131.3; plus 102.8 | 1,044.5; 1,147.3; 1,147.3 / 1,271.6 = 0.90 times | Derived |
| Revolver utilisation | (272.0 + 24.3) / 450.0 | 65.8% | 2026-06-30 |
| Capital commitments | 54.9 + 14.0 + 19.2 + 114.5; terminable 52.4 + 0.0 + 19.2 + 112.3 | 202.6 total; 183.9 terminable; 18.7 not terminable | 2026-06-30 |
| Share count roll | 396,834,231 + 46,794,082 + 516,447 (Q2FS page:23) | 444,144,760, equals printed | 2026-06-30 |
| Funded debt maturities | 272.0 (2028); 542.4 (2029); 52.0 (tender 2036) | 866.4, equals principal debt above | 2026-06-30 |
| Municipal bond interest, indicative | 52.0 x 4.50% | 2.34 a year | Run-rate |
| 6.125% notes interest, indicative | 542.4 x 6.125% | 33.22 a year | Run-rate |
| Segment ties | 273.3 + 258.4 + 99.6; 115.5 + 146.3 + 7.2; 636.3 + 544.9 + 207.4 | 631.3; 269.0; 1,388.6, equal printed totals | Q2 and six months 2026 |

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Covenant levels, step-downs, definitions, reported ratios and headroom for the revolving credit facilities are Not supplied (searched covenant, leverage ratio, coverage ratio, financial covenant across all seven sources); only compliance statements exist (Q2FS page:19; Q1FS page:14; Q3MDA page:41) | Covenant headroom is not calculable; the company ratios above are not covenant measures | Obtain the credit agreements and compliance certificates |
| Audited FY2025 statements and annual MD&A are not supplied; FY2025 figures rest on PR-FY25 | FY2025 cash flow detail, full-year interest and cash taxes paid and FY2025 principal debt are Not supplied; the February release mislabels carrying value as principal | Obtain Exhibits 99.2 and 99.3 of the annual report |
| Full-year or LTM cash interest paid is not printed; coupon payment dates are not printed | Cash interest cover over twelve months is Not calculable; half-year ratios are timing-distorted | Obtain the FY2025 cash flow statement and the indenture |
| Facility-level split of the 450.0 commitments and of the 153.7 availability between the Canadian and Peruvian facilities is not printed; revolver pricing is not printed | Availability could be lower than the aggregate if the Canadian facility is smaller than 296.3; revolver cost is not calculable | Obtain the credit agreements |
| 334.5 of cash is restricted to Copper World LLC; the terms of the restriction are not supplied | Group liquidity and net debt for creditors outside the project are overstated by the headline | Carry the restriction; obtain the Copper World joint venture agreement |
| Municipal bond final maturity not stated; only an initial mandatory tender date | Placement of 52.0 in the maturity wall is uncertain | Obtain the bond terms |
| No current contractual obligations table; the only one is dated 2025-09-30 | Scheduled interest, purchase obligations and mid-2026 amortisation are not available | Obtain the FY2025 MD&A table and a mid-2026 update |
| Issuer, borrower and guarantor identities, restricted-group definition and the list of excluded subsidiaries are not named | Structural subordination analysis rests on filing summaries | Obtain the indenture and credit agreements |
| Free cash flow and cash sustaining capital expenditure history differ between releases; one trailing cell is misprinted | Any series must name the release; Q4 2025 free cash flow is 225.0 or 228.2 | Use the latest consistent version (225.0) and say so |
| Share count at 2025-12-31 conflicts: 395,521,903 (40-F cover) and 396,834,231 (interim note) | Per-share and equity-value inputs are uncertain | Obtain the audited statements |
| Nothing dated after 2026-07-29 is supplied | Q3 2026 results, the Copper World sanction decision, the Wheaton definitive agreement and later financings are Not supplied | Supply later filings if any exist |
| Ratings, market data and valuation fields in the context are blank | No rating or market-based leverage is included | None for this base |
| Operating-lease cost, purchase obligations other than capital, and royalties are not separately quantified at 2026-06-30 | A fixed-charge view is incomplete | Obtain the FY2025 MD&A contractual obligations |

## Next module

Proceed to CP-1A for business and transaction context, carrying forward: the Copper World joint venture (30% to Mitsubishi, 422.7 received, 180.0 receivable within 18 months, cash restricted to the project); the Arizona Sonoran acquisition and the new deferred land payments of 102.8; the April 2026 repayment of the 2026 notes funded by a 272.0 revolver draw; the 52.0 municipal bonds issued by Copper World LLC; the pending Copper World sanction decision and Wheaton stream status; the New Ingerbelle judicial review application; and the port-closure timing effect in Q2. CP-2 and CP-5 should keep the covenant, facility-level availability, full-year cash interest and audited-base gaps open, should use the ring-fenced view alongside the company net debt, and should not cite the half-year interest ratios as full-year cover.
