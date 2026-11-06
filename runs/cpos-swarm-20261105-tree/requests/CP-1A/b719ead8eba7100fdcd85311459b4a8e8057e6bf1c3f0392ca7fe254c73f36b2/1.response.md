# CP-1A — Business and transaction context: LendingTree, Inc. (tree)

## Request

- Issuer: LendingTree, Inc. (issuer id `tree`; Nasdaq: TREE), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `tree-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This module builds the business, ownership, governance and transaction fact pack a committee reads first. It consumes the CP-0 readiness handoff and the CP-1 financial base. Later modules CP-2 and CP-5 consume it.
- Context settings: reporting currency USD; current period q2-2026; prior period fy-2025. Context leaves borrower, parent, guarantor and sponsor fields blank; blank is not evidence that none exists. Amounts below are US dollars; the statements are in thousands and the narrative and releases in millions.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Scope: facts tagged Documentary Fact, Management Language, Analyst Interpretation or Insufficient Information; governance and behaviour of the issuer (not individuals); timeline; conflicts; credit translations. No peer ranking, instrument recommendation or recovery conclusion. All figures come from the pinned sources or from the CP-1 handoff; derived figures are in `## Calculations`.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_tree-20251231.htm.jsonl | 8cb6cb5e097dc2e8360d276758588e587f0ac910e30b439c9a6d5f22fdc532f1 | Business, history, customers, risk factors, ownership and governance disclosure, debt note, exhibit list |
| 10-Q_2025-09-30_tree-20250930.htm.jsonl | 249304d8f29fc14b902a9aacbb2c6a074e549655cafbbfa182447cab0a8e6bd0 | Q3 2025 interim report; context for the August 2025 refinancing |
| 10-Q_2026-03-31_tree-20260331.htm.jsonl | 9f7be701e3beaeb193c8f4c45fa295df34640347810fab7e7e1868937c8317f9 | Q1 2026 interim report |
| 10-Q_2026-06-30_tree-20260630.htm.jsonl | 4c93c158274dd2856277ea5350526f695a8bcd4a41e0bedcd9b748ac31b890ae | Q2 2026 interim report; current-period authority |
| EX-99.1_2026-03-02_tree-123125xer.htm.jsonl | 930047033d516e80ede0b1af19850b29c93444522e483a1dc8c6992d4283ee5d | Q4 2025 earnings release; management commentary and initial 2026 outlook |
| EX-99.1_2026-04-30_tree-33126xer.htm.jsonl | 9b95e0c334507932b6d82bc72cf01d0a8f620ab6313637adea07e7f7ef2b4190 | Q1 2026 earnings release; management commentary and updated outlook |
| EX-99.1_2026-07-29_tree-63026xer.htm.jsonl | b737e26fe71071d22f2d669bce2532cab38eb1e5741e87f2852ff6a85cf82520 | Q2 2026 earnings release; management commentary and updated outlook |
| context | d200051bbc093266762c46db0da57fcc23aae21f45bdfa41362781dff2cb6e7d | User run settings; not issuer evidence |

| Handoff module | sha256 | Use |
| --- | --- | --- |
| CP-0 | c84ab10531b22ca79243cab80e778b189c7ae85ab40d1bc94cfa4d4426e74643 | Readiness verdict, source register and gap list; limitations carried forward |
| CP-1 | 66d19075d0cda548fb908b11cbace236ac80961fccbfe892b5468b6b2cd9a36f | Accepted financial base; segment shares, leverage, liquidity and concentration figures are referenced from it |

Locators are `page:N`, the source chunk number in each pinned file, not the printed page. Short forms: 10-K (FY2025), 10-Q Q2 2026, 10-Q Q1 2026, 10-Q Q3 2025, release Q4 2025, release Q1 2026, release Q2 2026. The 2026 proxy statement, which the 10-K incorporates for Items 10 to 14 (10-K page:156), is not supplied.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| LendingTree is a US online lead-generation marketplace with no sponsor identified. Insurance drives growth, one partner supplied 27% of FY2025 revenue, and the only debt is one facility. Management lowered its 2026 Adjusted EBITDA outlook on July 29, 2026. | Medium | The credit agreement, proxy statement and ownership detail are not supplied, and no document dated after July 30, 2026 is included. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Revenue is earned per consumer request from about 770 partners; Insurance was 63.7% of FY2025 revenue and 66.8% of Q2 2026 revenue. | Earnings depend on carrier advertising budgets and media costs rather than contracted revenue, so cyclicality is concentrated in one segment. | High |
| One partner, Progressive Casualty Insurance, supplied 27% of FY2025 revenue; two partners supplied 22% and 11% in FY2024. | Losing or shrinking one carrier relationship could remove a large share of Insurance revenue; contract terms are not supplied. | Medium |
| Founder and former CEO Doug Lebda died in October 2025 and Scott Peyree became CEO on October 13, 2025; his heirs collectively hold a substantial stake. | Succession and a concentrated holder group add governance uncertainty; no creditor-adverse action is documented. | Medium |
| On August 21, 2025 the company replaced two term loans with a US$400.0m term loan and a US$75.0m revolver, both maturing August 21, 2030. | The refinancing removed near-term maturities; without the agreement, restricted payment and incremental debt capacity are unknown. | Medium |
| Management cut full-year 2026 Adjusted EBITDA guidance to US$145 to US$152 million on July 29, 2026 from US$152 to US$162 million on April 30, 2026. | Q2 2026 Adjusted EBITDA came in below the range guided in April, so forward figures are management claims with execution risk. | Medium |

### Business and transaction view

LendingTree is a US online marketplace that matches consumers with lenders, insurers and other providers and is paid fees by those providers, mostly when a consumer request is delivered. It is a public company with no sponsor or controlling owner identified in the supplied sources. The business has three reportable segments, Home, Consumer and Insurance, and its recent growth has come from Insurance, where earnings depend on carriers' advertising budgets and on the cost of the online media LendingTree buys to attract consumers. The creditor-relevant structure is simple: one first lien credit facility, secured on substantially all assets and guaranteed by material domestic subsidiaries, no dividend in over ten years, no share repurchases in 2024, 2025 or the first half of 2026, and no pending acquisition or ownership transaction in the supplied documents. The main uncertainties are the concentration in Insurance and in one carrier, the loss of the founder in October 2025 with his heirs holding a substantial stake, a weaker Q2 2026 against the company's own guidance, and the absence of the credit agreement. Everything after July 30, 2026 is Not supplied.

### Company and operating model

| Dimension | Fact | Category | Source | Credit relevance |
| --- | --- | --- | --- | --- |
| Core activity | Operates an online marketplace connecting consumers with lenders, insurers and other providers: "a nationwide network of approximately 770 partners (which we refer to as “Network Partners”)" | Documentary Fact | 10-K page:8 | Revenue is a function of consumer traffic and partner demand, not balance-sheet lending; LendingTree does not originate or hold the loans |
| Characterisation | "operates what we believe to be the leading online consumer platform" and "the nation's leading online financial services marketplace" | Management Language | 10-K page:8; release Q2 2026 page:1 | Promotional; not adopted as fact |
| Products and segments | Home: purchase mortgage, refinance mortgage, home equity loans and lines of credit. Consumer: credit cards, personal loans, small business loans, auto loans, deposit accounts and other credit products. Insurance: insurance quote products; the insurance agency business was exited in Q2 2025 | Documentary Fact | 10-K page:11; 10-Q Q2 2026 page:20, page:21 | Three segments with different cycles: mortgage rates, credit supply and carrier advertising |
| Revenue model | Fees paid by partners at delivery of a consumer request, plus click and call fees and closed-loan or approval fees in some Consumer products. "LendingTree does not charge consumers for the use of our services." Up to five match fees may be generated from one mortgage request | Documentary Fact | 10-K page:12 | Revenue is transactional and recurs only through continued partner demand; contracts "generally may be terminated for convenience by either party" for Home lenders |
| End market and geography | US consumers; "Other than a support services office in India, the Company's operations are geographically limited to and dependent upon the economic condition of the United States." Offices in Charlotte, Denver, Seattle, Ahmedabad and Hyderabad | Documentary Fact | 10-Q Q2 2026 page:8; 10-K page:76 | Single-country exposure to US credit and insurance cycles |
| Segment mix | Insurance revenue was 63.7% of FY2025 revenue and 66.8% of Q2 2026 revenue (CP-1 calculation C11); Home 151,764 and Consumer 253,370 of FY2025 revenue of 1,117,324 | Documentary Fact | 10-K page:11; CP-1 | Growth and margin sensitivity concentrate in Insurance |
| Customer concentration | FY2025: one partner, Progressive Casualty Insurance, 27% of consolidated revenue, all in Insurance. FY2024: Progressive Casualty Insurance 22% and Allstate Insurance Company 11%. FY2023: none above 10% | Documentary Fact | 10-K page:12 | Material single-name exposure |
| Largest partners in 2025 other than Progressive | The 10-K does not state Allstate Insurance Company's FY2025 share or any other partner's share | Insufficient Information | 10-K page:12 | Cannot size second-name exposure for FY2025 |
| Insurance volume and price drivers | Q2 2026 Insurance revenue up 42%: "a 22% increase in volume, representing $38.3 million of the increase, and a 16% increase in revenue earned per consumer, representing $23.8 million" | Documentary Fact | 10-Q Q2 2026 page:27 | Growth is partly volume bought through media and partly higher fees from carriers |
| Cost structure | Variable marketing expense was 70.8% of H1 2026 revenue (CP-1 calculation C11). "Our operating model is highly sensitive to the amount and efficiency of variable marketing expenditures" | Documentary Fact | 10-Q Q2 2026 page:35; CP-1 | Margin is set by media cost against partner pay; "We expect advertising costs to remain elevated for the remainder of 2026" (10-Q Q2 2026 page:35) |
| Capital spending | Capital expenditures were 12,423 in FY2025 and 5,935 in H1 2026, "primarily related to internally developed software" | Documentary Fact | 10-K page:99, page:112; 10-Q Q2 2026 page:40 | Low capital intensity supports cash conversion |
| Working capital | Contract asset for estimated variable consideration of US$41.0m at June 30, 2026 against US$33.5m at December 31, 2025, from closing fees and approval fees not yet contractually receivable; business loan renewal contract asset of US$28.0m at December 31, 2025 | Documentary Fact | 10-Q Q2 2026 page:11; 10-K page:29 | Part of reported revenue is estimated; renewal and close rates that miss estimates reverse into revenue |
| Seasonality | Home rises in spring and summer; Insurance dips in December and rises in spring; personal loans weaker in the fourth and first quarters | Documentary Fact | 10-K page:15 | Quarterly liquidity and covenant tests face seasonal swings |
| Competition | Competes with other online marketing companies and with lenders and insurance agents that source consumers directly; also search engines, AI-based services and content aggregators | Documentary Fact | 10-K page:16, page:39 | Disintermediation by large technology platforms is a stated risk |
| Management direction | "Become the #1 Destination to Shop For Financial Products"; AI tools and a redesigned homepage aimed at lifting organic traffic against paid channels | Management Language | release Q1 2026 page:1; release Q2 2026 page:1 | Unproven; paid-media dependence persists in the filed numbers |

### Company profile

| Item | Fact | Category | Source |
| --- | --- | --- | --- |
| Legal entity and perimeter | LendingTree, Inc., Delaware; parent of LT Intermediate Company, LLC, which holds all the ownership interests of LendingTree, LLC, which owns several companies. Consolidated reporting entity | Documentary Fact | 10-K page:16, page:113; 10-Q Q2 2026 page:1 |
| Listing and filer status | Nasdaq "TREE"; accelerated filer; context sector "Loan Brokers", country United States | Documentary Fact | 10-K page:1; context |
| Headquarters and offices | Charlotte, North Carolina, about 129,000 square feet under a lease expiring in 2036; offices in Denver, Seattle, Ahmedabad and Hyderabad | Documentary Fact | 10-K page:76 |
| People | 926 employees at December 31, 2025, of which about 919 full-time; none under collective bargaining | Documentary Fact | 10-K page:19 |
| Leadership | Scott Peyree, President and CEO from October 13, 2025 (previously COO and President, LendingTree Marketplace); Jason Bengel, CFO; Steven Ozonian, Chairman of the Board | Documentary Fact | 10-K page:37, page:163 |
| Auditor | PricewaterhouseCoopers LLP, auditor since 2012; internal control over financial reporting effective at December 31, 2025 | Documentary Fact | 10-K page:109, page:155 |
| Shares and holders | 14,039,561 shares outstanding at July 27, 2026; about 397 holders of record at March 6, 2026; non-affiliate market value about US$411 million at June 30, 2025 | Documentary Fact | 10-Q Q2 2026 page:1; 10-K page:77, page:2 |
| Ownership | Founder and former CEO "beneficially owned approximately 18% of our common stock" before his death; "no single heir or successor currently claims beneficial ownership of 10% or more". A separate "single stockholder who owned in excess of 20% of the voting common stock" is assumed an affiliate for the market value calculation. No sponsor identified | Documentary Fact | 10-K page:68, page:2 |
| Unnamed large holder | The identity of the "single stockholder who owned in excess of 20% of the voting common stock" and its relationship to the founder's estate are not stated | Insufficient Information | 10-K page:2 |
| Credit rating | The 10-K says a corporate family rating of B2 (stable) or better from Moody's "was achieved in January 2026", lowering the term loan margin; no rating report is supplied | Documentary Fact (as stated by the issuer) | 10-K page:145 |
| Tax attributes | Federal NOLs of US$148.8m and state NOLs of about US$423.1m at December 31, 2025; a partial valuation allowance remains; use is limited by Sections 382 and 383 | Documentary Fact | 10-K page:56 |
| Dividends and buybacks | "We have not declared or paid a cash dividend on our common stock in over ten years"; about US$96.7m of repurchase authorization remains and none was used in 2024, 2025 or H1 2026; the credit facility limits repurchases; the US$50.0m at-the-market programme has had no sales | Documentary Fact | 10-K page:70, page:73, page:78; 10-Q Q2 2026 page:14, page:43 |

### Transaction summary and new debt issues

No acquisition, disposal, sponsor transaction or capital markets issue is described in any pinned document after the refinancing, so the transaction record is one financing event and a set of earlier changes; any transaction after July 30, 2026 is Not supplied. The refinancing is dated August 21, 2025, status closed. LendingTree entered into the 2025 Credit Agreement, a US$475.0 million first lien facility made up of a US$75.0 million revolving facility and a US$400.0 million term loan, both maturing August 21, 2030 (10-K page:144; 10-Q Q2 2026 page:18, page:39). The use of proceeds, as the filings state it, was to refinance the 2021 Credit Facility and the 2024 Term Loan, which collectively had US$402.8 million outstanding, with the US$400.0 million term loan and cash on hand at par plus accrued and unpaid interest, and for working capital and general corporate purposes (10-K page:97, page:144). The repayments were US$242.5 million of the 2021 term loan and US$160.3 million of the 2024 term loan; the 2021 revolver was terminated (10-K page:148). The company recognised a loss on extinguishment of US$7.9 million, incurred financing costs of US$8.6 million on the term loan of which about US$0.8 million was expensed, and paid US$3.9 million of original issue discount (10-K page:97, page:146). Earlier, the 0.50% Convertible Senior Notes due July 15, 2025, issued in July 2020 for US$575.0 million, were reduced by repurchases and the remaining US$95.3 million was repaid in cash at maturity on July 15, 2025, so no convertible debt, hedge or warrant remains and the warrants expired on February 11, 2026 (10-K page:142, page:144; 10-Q Q2 2026 page:14). The 2025 Term Loan is secured by substantially all assets including 100% of the equity in certain domestic subsidiaries and 65% of the voting equity of certain foreign subsidiaries, and guaranteed on a senior basis by material domestic subsidiaries; the revolver carries a US$30.0 million letter of credit sublimit; the financial covenant is a first lien net leverage ratio of 5.00 to 1.00 tested only when revolver usage exceeds US$20.0 million; and incremental capacity is the greater of US$58.0 million and 50% of consolidated EBITDA plus an unlimited amount subject to first lien net leverage of 3.10 to 1.00 (10-K page:145, page:146). Pricing is Term SOFR plus 4.50%, or 4.25% once a Moody's corporate family rating of B2 (stable) or better was achieved, which the 10-K says happened in January 2026; a 1.0% soft call premium applied during the first six months after closing (10-K page:145, page:146). The term loan balance was US$397.0 million at July 30, 2026 with no revolver borrowings and US$75.0 million available (10-Q Q2 2026 page:39, page:40). The liquidity effect, from CP-1, is cash of US$110.8 million and an undrawn US$75.0 million revolver at June 30, 2026, before any letters of credit, which are Not supplied. Sponsor and use-of-proceeds distributions: none documented; there is no sponsor and no distribution in the pinned sources. Which entity is the borrower, which subsidiaries guarantee and the exact covenant definitions are Not supplied because the credit agreement, exhibit 10.39 incorporated from a Form 8-K filed August 21, 2025, is not in the pack (10-K page:161).

### Ownership and control

- Control rights: no controlling shareholder is documented. Anti-takeover provisions include blank-check preferred of up to 5,000,000 shares, no cumulative voting, board-only filling of vacancies and board sizing, board-called special meetings and no action by written consent (10-K page:69). Documentary Fact.
- Founder and heirs: the founder, Doug Lebda, died on October 12, 2025 and his death was announced on October 13, 2025; before it he owned about 18%, and his "heirs and successors collectively hold a substantial portion of our outstanding shares" and "would have substantial voting control" if they acted collectively (10-K page:37, page:68). The estate or heirs' individual holdings and any voting arrangement are Not supplied. Insufficient Information on the exact percentage after his death.
- Unnamed large holder: the 10-K cover assumes "a single stockholder who owned in excess of 20% of the voting common stock" is an affiliate (page:2); the holder is not named and the relationship to the estate is not stated. Insufficient Information; the 2026 proxy statement would normally name it.
- Prior ownership: acquired by IAC/InterActiveCorp in May 2003 and spun off in August 2008 (10-K page:16). The exhibit list includes an assignment agreement of November 2, 2017 involving Liberty USA Holdings, LLC and a registration rights agreement of August 20, 2008 with Liberty Media Corporation (10-K page:158); the current status of that holder is Not supplied.
- Dividend recapitalisation history: none documented. The company states no cash dividend in over ten years (10-K page:70).

### Governance and sponsor behaviour

Assessment is at issuer level. Legal capacity, willingness and feasibility are kept separate.

| Behaviour or action | Category | Legal capacity, willingness, feasibility | Evidence quality | Mechanic and implication | Source |
| --- | --- | --- | --- | --- | --- |
| Retired the 2025 Notes in cash: repurchased about US$20.0m of principal in Q1 2025 for US$19.7m and repaid the remaining US$95.3m at maturity, US$115.0m of cash in 2025 | Supportive | Willingness: documented repayments from cash. Feasibility: cash of 81,073 remained at December 31, 2025 | High | Reduced total debt principal while bank debt rose; lowers refinancing exposure but used liquidity | 10-K page:97, page:112 |
| Refinanced two term loans into one at par on August 21, 2025 | Neutral or Mixed | Capacity: first lien facility permitted by the new agreement. Willingness: lender-agreed at par. Feasibility: the facility was priced at Term SOFR plus 4.50% | High | Extended maturity to August 21, 2030 and costs a 7.9m extinguishment loss; documents not supplied | 10-K page:97, page:144, page:145 |
| No dividends in over ten years; no repurchases in 2024, 2025 or H1 2026 despite US$96.7m authorised; credit facility limits repurchases | Supportive | Capacity limited by the credit facility; willingness shown by non-use; feasibility: cash 110.8m at June 30, 2026 | High | Cash retained for creditors; authorisation remains a latent use of cash if the facility permits | 10-K page:70, page:78; 10-Q Q2 2026 page:14, page:43 |
| Equity distribution agreement for up to US$50.0m in July 2024 with no sales | Neutral or Mixed | Capacity exists; not used | High | Equity access is available but untested | 10-Q Q2 2026 page:14 |
| Foundation contribution of US$0.4m approved Q1 2026 and paid Q2 2026; officers serve as officers of the foundation | Neutral or Mixed | Small related-party item | High | Excluded from Adjusted EBITDA as an add-back; immaterial to liquidity | 10-Q Q2 2026 page:20, page:37 |
| Equity-linked pay: RSUs with market conditions with price hurdles of $69.15, $83.85 and $98.55 granted in 2026 | Neutral or Mixed | Alignment with equity value rather than debt | High | Incentives favour equity price; no creditor-adverse use documented | 10-Q Q2 2026 page:16 |
| Priming, uptiering, drop-downs, non-pro-rata exchanges, collateral release, debt-funded distributions, related-party leakage | Insufficient Information | Documents that would show capacity are not supplied; no such action is described in the pinned sources | Insufficient | Absence of disclosure is not evidence of absence; the credit agreement is needed to assess capacity | 10-K page:38 |

### Timeline

| Date | Event | Type | Source |
| --- | --- | --- | --- |
| June 1996; July 1998 | Incorporated in Delaware; nationwide operations began | Founding | 10-K page:16 |
| May 2003; August 2008 | IAC acquired LendingTree, LLC; the company was spun off from IAC | Ownership change | 10-K page:16 |
| January 1, 2015 | Name changed from Tree.com, Inc. to LendingTree, Inc. | Corporate | 10-K page:16 |
| October 4, 2018 | Unit purchase agreement for QuoteWizard.com, LLC (exhibit 2.14); a December 20, 2018 stock purchase agreement for Value Holding Inc. (exhibit 2.15) | Acquisitions (terms not supplied) | 10-K page:158 |
| July 24, 2020 | Issued US$575.0 million of 0.50% Convertible Senior Notes due July 15, 2025, with hedge and warrants | Financing | 10-K page:142, page:144 |
| January 2022 | Acquired an equity interest in EarnUp Inc. for US$15.0 million; impaired in Q3 2024 | Investment | 10-K page:130 |
| Q2 2023; September 2023 | Shut down the Ovation credit repair business; workforce reduction of 14 employees | Disposal and restructuring | 10-K page:11, page:153 |
| March 27, 2024 | US$175.0 million 2024 Term Loan, US$125.0 million drawn, US$50.0 million drawn March 27, 2025 | Financing | 10-K page:148 |
| Q4 2024 | Decision to cease offering student loan products | Disposal | 10-K page:151 |
| Q2 2025 | Exited the insurance agency business | Disposal | 10-K page:11 |
| July 15, 2025 | Repaid the remaining US$95.3 million of 2025 Notes | Refinancing | 10-K page:142 |
| August 21, 2025 | 2025 Credit Agreement; 2021 and 2024 term loans of US$402.8 million repaid | Refinancing | 10-K page:97 |
| October 12 and 13, 2025 | Death of the founder and former Chairman and CEO (October 12) and its announcement; Scott Peyree appointed CEO (October 13) | Management change | 10-K page:37, page:68 |
| November 21, 2025 | Fifth Amended and Restated By-laws filed on Form 8-K (content not supplied) | Governance | 10-K page:158 |
| January 2026 | Moody's corporate family rating condition for the lower margin achieved | Rating event | 10-K page:145 |
| February 11, 2026 | Warrants expired | Corporate | 10-Q Q2 2026 page:14 |
| March 2, 2026; April 30, 2026; July 29, 2026 | Earnings releases with 2026 outlook issued, raised and then lowered (see outlook table) | Disclosure | releases |
| Q1 and Q2 2026 | Second and third instalments of a US$19.0 million litigation settlement (Mantha, a TCPA class action against QuoteWizard.com, LLC): paid in the first quarter and the second quarter of 2026 | Regulatory and litigation | 10-Q Q2 2026 page:20 |
| After July 30, 2026 | Subsequent events: Not supplied | Subsequent event | n/a |

### Management outlook history

These are management claims and forward-looking. They are not used as evidence of results. US$ millions as printed.

| Release | Full-year 2026 revenue | Full-year 2026 variable marketing margin | Full-year 2026 Adjusted EBITDA | Next-quarter guide |
| --- | --- | --- | --- | --- |
| March 2, 2026 (release Q4 2025 page:4) | 1,275 to 1,330 | 374 to 394 | 150 to 160 | Q1 2026 Adjusted EBITDA 39 to 41 |
| April 30, 2026 (release Q1 2026 page:3) | 1,300 to 1,350 | 378 to 395 | 152 to 162 | Q2 2026 Adjusted EBITDA 38 to 40 |
| July 29, 2026 (release Q2 2026 page:3) | 1,300 to 1,320 | 364 to 374 | 145 to 152 | Q3 2026 Adjusted EBITDA 34 to 36 |

Q2 2026 reported Adjusted EBITDA of 35.2 and variable marketing margin of 87.3 (10-Q Q2 2026 page:36, page:38) against the April guide of 38 to 40 and 93 to 97 (calculation C2). The CFO attributed the shortfall to "weaker than expected Consumer performance in Q2" and said small business demand "continued to deteriorate throughout the quarter" before stabilising (release Q2 2026 page:1). Management Language.

### Conflicts

| Item | Span A | Span B | Downstream effect |
| --- | --- | --- | --- |
| Valuation allowance wording | Release Q4 2025 page:1: "inclusive of $146.4 million tax benefit to reduce the full valuation allowance against our net deferred tax assets" | 10-K page:56: "we maintain a partial valuation allowance on certain deferred tax assets"; 10-K page:102: a valuation allowance of $18.0 million at December 31, 2025 | The release says the allowance was fully reduced while the 10-K shows a remaining allowance; the two also give a Q4 amount of 146.4 and a full-year amount of 149.5 (10-K page:90). Logged, not reconciled; the 10-K controls the balance-sheet fact |
| Balance sheet classification at December 31, 2025 | Release Q4 2025 page:5: "Prepaid and other current assets 49,053" | 10-K page:110: 38,053 | Carried from CP-1; 10-K controls. Logged, not reconciled |

### Credit translations

1. Revenue durability. Evidence: revenue is fees per delivered consumer request (10-K page:12) and Insurance was 66.8% of Q2 2026 revenue (CP-1). Risk mechanic: carriers set advertising budgets by underwriting results, and the 10-Q says carriers "are broadly experiencing strong automotive underwriting results" (10-Q Q2 2026 page:24), so Insurance revenue is cyclical in carrier profitability and in rate competition; contracts for Home lenders can be terminated for convenience (10-K page:12). Credit implication: debt service capacity rests on one segment's demand cycle with no contracted revenue, so leverage tolerance should assume Insurance can reverse faster than fixed costs. Counter-evidence: the three segments have different cycles, and Insurance segment profit grew 25% in Q2 2026 (10-Q Q2 2026 page:31). No logged conflict counters this.
2. Margin and cash-flow risk. Evidence: variable marketing expense was 70.8% of H1 2026 revenue (CP-1) and management expects advertising costs to stay elevated (10-Q Q2 2026 page:35). Risk mechanic: media cost rising faster than monetisation compresses variable marketing margin before fixed costs, and the Q2 2026 variable marketing margin was 87.3 against 99.5 in Q1 2026 (CP-1). Credit implication: margin resilience is the key monitoring item, since Adjusted EBITDA for the covenant and for CP-1 leverage rests on it.
3. Concentration risk. Evidence: Progressive Casualty Insurance was 27% of FY2025 revenue (10-K page:12), which on the rounded percentage is about 42.4% of Insurance revenue (calculation C3). Risk mechanic: a carrier can cut its budget at short notice, and QuoteWizard's own risk factors list "concentration of customers with large insurance carriers" (10-K page:27). Credit implication: a single relationship change could move Adjusted EBITDA materially; the contract terms and the 2026 share are Not supplied, so the exposure cannot be sized for 2026. Counter-evidence: in FY2024 two partners together supplied 33%, so concentration has shifted between names, not fallen.
4. Sponsor and governance alignment. Evidence: no sponsor, no dividend in over ten years, no repurchases since at least January 1, 2024 (10-K page:70, page:78), a CEO succession on October 13, 2025 and heirs holding a substantial stake (10-K page:37, page:68). Risk mechanic: alignment is with public equity holders and a family estate whose intentions are not documented; a block of that size can influence board composition or a sale. Credit implication: no creditor-adverse behaviour is documented, but willingness cannot be tested without the credit agreement's restricted payment terms; a change of control provision, if any, is Not supplied.
5. Key uncertainties. The credit agreement, the 2026 proxy statement, the 2026 concentration, the unnamed 20% holder and anything after July 30, 2026. Credit implication: monitoring posture should treat leverage as improving on reported numbers but unverified against covenant definitions.

### Monitoring gaps

| Missing item | Severity | Why it matters |
| --- | --- | --- |
| Executed 2025 Credit Agreement and compliance certificate | High | Covenant definitions, baskets, guarantors, letters of credit |
| Debt schedule and annual maturity table | Low | Only the current portion and the August 21, 2030 maturity are printed (CP-1) |
| Add-back bridge in a covenant EBITDA definition | Medium | Adjusted EBITDA is issuer-defined (CP-1) |
| 2026 proxy statement and holder list | Medium | Ownership, board, related-party dealings, executive pay |
| Partner contracts and 2026 concentration | Medium | Sizes the Insurance exposure |
| Any filing after July 30, 2026 including Q3 2026 results | Medium | Cutoff is November 5, 2026 |

### Consumer assessment

| Module | Readiness | What to take from this handoff | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Facility terms, security and guarantee description, covenant summary, refinancing facts, governance behaviour table, outlook history | Liquidity, refinancing and covenant analysis must use the facility terms and the Insurance concentration | Credit agreement, letters of credit and 2026 concentration not supplied | Describe terms as summarised in the notes; carry the gaps as restrictions; use only dated management outlook as a claim |
| CP-5 | READY_WITH_LIMITATIONS | Tagged fact rows, locators, logged conflicts | Claim tracing and conflict handling | Text extraction only; two logged conflicts unreconciled | Trace each claim to a `page:N`; keep conflicts open |

## Calculations

All inputs are printed amounts or CP-1 values. No figure is invented.

**C1. Segment shares (from CP-1 calculation C11).** Insurance share of revenue: FY2025 711,880 / 1,117,324 = 63.7%; Q2 2026 209,263 / 313,422 = 66.8%. Variable marketing expense / revenue, H1 2026: 453,803 / 640,689 = 70.8%.

**C2. Guidance versus Q2 2026 actual (US$ millions).** Adjusted EBITDA: guided range 38 to 40; reported 35.162 (35,162 thousands); shortfall to the low end 38 − 35.162 = 2.838. Variable marketing margin: guided 93 to 97; reported 87.339; shortfall to the low end 93 − 87.339 = 5.661. Revenue guided 305 to 325; reported 313.4, inside the range. Full-year Adjusted EBITDA guide of 145 to 152 less H1 2026 of 77.171 implies second-half Adjusted EBITDA of 67.829 to 74.829. Net leverage tie-out at March 31, 2026: principal 394,000 + 4,000 = 398,000 less cash 85,518 = 312,482; trailing Adjusted EBITDA 132,887 + 42,009 − 24,626 = 150,270; 312,482 / 150,270 = 2.08x against the CFO's statement of 2.1x (release Q1 2026 page:1).

**C3. Progressive share of Insurance revenue (rounded input).** 27% × 1,117,324 = 301,677 (thousands); 301,677 / 711,880 = 42.4%. The 27% is a rounded percentage, so the result is approximate to about plus or minus 0.5 percentage points of revenue. Analyst Interpretation. FY2024: 22% + 11% = 33% of revenue.

**C4. Debt repaid in the refinancing.** 242.5 + 160.3 = 402.8 (US$ millions), equal to the "collectively had $402.8 million outstanding" (10-K page:97, page:148).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement (exhibit 10.39) not supplied; borrower and guarantor entities, restricted payment terms, change of control and covenant definitions are Not supplied | High for legal and covenant work; Medium otherwise | CP-2 | Supply the August 21, 2025 Credit Agreement |
| 2026 proxy statement not supplied; holder list, unnamed 20% holder, heirs' voting arrangements and board details Not supplied | Medium | CP-2, CP-5 | Supply the definitive proxy statement |
| Partner contracts and 2026 share of the largest partner Not supplied; Allstate's FY2025 share Not stated | Medium | CP-2 | Supply later filings |
| Acquisition terms for QuoteWizard and Value Holding Inc. are Not supplied (exhibit list only) | Low | CP-2 | Not required for this scope |
| No transaction source after the refinancing; any event after July 30, 2026 Not supplied | Medium | CP-2 | Supply later filings including a Q3 2026 10-Q |
| No rating report; Moody's B2 stable corporate family rating is mentioned in the 10-K only | Low | CP-2 | Not required for this scope |
| Logged conflicts: valuation allowance wording; Q4 2025 release balance sheet classification | Low | CP-2, CP-5 | Use the 10-K; do not reconcile |
| Text extraction only; no XBRL or image review | Low | CP-5 | Check flagged tables against the filed HTML |

## Next module

- CP-2: use the facility terms, covenant summary, security and guarantee description, refinancing facts, the governance behaviour table and the outlook history; treat the outlook as management claims; carry the missing credit agreement, letters of credit gap and 2026 concentration as restrictions; do not infer sponsor or holder intent.
- CP-5: trace each tagged row to its locator; keep the two logged conflicts open; do not use management characterisations as fact.
