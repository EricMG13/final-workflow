## Request

Issuer: Block, Inc. (issuer id xyz, ticker XYZ), consolidated registrant. As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Current period Q3 2026 and nine months 2026; prior period FY2025; currency USD. Task: build the business, ownership, operating-model and transaction fact pack a credit committee reads first, with governance behaviour assessed at issuer level only, and translate each material fact into a creditor mechanic.

Carried forward from the upstream handoffs. From the source readiness handoff: guarantors, executed indentures and the credit agreement are not supplied, charts and images in the shareholder letters are not covered by text extraction, and the context leaves borrower, parent, guarantors, sponsor, ratings and deal terms blank. From the financial handoff: filed-basis total debt to EBITDA is 4.67x and EBITDA to cash interest 3.99x at LTM Q3 2026, management's Adjusted EBITDA basis gives 1.69x, accrued legal contingencies are 980.6 and a separate 764 is accrued for a Department of Justice matter (the financial handoff says the 980.6 includes the 764; the filing's accrued-expenses table, 10-Q Q3 page:22, does not say which line holds it, so treat that as likely but unconfirmed, and this handoff corrects the wording to that extent), and the covenant level is not printed. No source in the pack describes a sponsor, a leveraged buyout or an acquisition financing in 2026; the transaction section says so rather than inventing one.

## Sources

### Issuer sources relied on

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_xyz-20251231.htm.jsonl | 6d2723637c4e4692665dfc17c25cdb747bc058fa0efdacc637270724a986bc79 | Ownership and voting (pages 92, 99, 107), ratings statement (page:130), debt issuance history (pages 111, 186 to 190), related-party lease (page:206), auditor (pages 139, 140) |
| 10-Q_2026-03-31_xyz-20260331.htm.jsonl | fb16696ee2c760f5f516dd4d7d776ad2e1413e975d581b22e43bf743c804dffb | Read for period coverage only; no fact below cites it |
| 10-Q_2026-06-30_xyz-20260630.htm.jsonl | 298a453eb61f62c2eadccf751942418cba8c13261b222b26c193276f0204df4e | Read for period coverage only; no fact below cites it |
| 10-Q_2026-09-30_xyz-20260930.htm.jsonl | c3685fce2b8084b3b1277e2ff24d3b8912d57dba3d48bc4c00ef1cdf864ed3ba | Business description (pages 9, 14), operating results (pages 43, 44), debt (pages 27 to 30), contingencies and subsequent events (pages 34 to 37), restructuring (page:40), liquidity (pages 55 to 60) |
| EX-99.1_2026-05-07_d132441dex991.htm.jsonl | d34a2a9e1d7a5617f1c2e6fc60dfac8b09244c4670a9cb13c493e5c88cddf1a8 | Not cited |
| EX-99.1_2026-08-05_d91486dex991.htm.jsonl | 804a5c312efc62e6ddd1ec8bbc4d12bb902bba131422b7373caf3f4ebbc3e21e | Not cited |
| EX-99.1_2026-11-03_q32026shareholderletter.htm.jsonl | a2c931043c84d33fdc40710a24c2e84aa25d66394cc76e294f6f9e8221b76b85 | Management operating metrics and commentary (pages 13 to 16); management language only |

### Handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | fde3c57d263f194f36b012cf6dac47111bd001036fc4309d336b4e5a15f1d35b | Source readiness and gaps |
| CP-1 | b07cf296fcccfced7fc39b3d89643e1dbe0b2cad1f07c4c884c441e049fe5ca0 | Accepted financial figures referenced here |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Block is a founder-controlled, dual-class payments and consumer-lending group with no sponsor, an undrawn revolver and no new bond issuance in 2026. Legal resolutions and lending growth are the main credit changes. | Medium | Guarantors, indentures and the credit agreement are not supplied, and the Department of Justice resolution is not final. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Class B holders control a majority of the votes, and no dividend has ever been declared. | Control sits with insiders, but no cash is paid out as dividends; buybacks remain the shareholder-return channel. | High |
| Revenue is led by commerce enablement and financial solutions, while bitcoin revenue is large but earns little gross profit. | Credit quality rests on payments and lending gross profit rather than bitcoin revenue. | High |
| Lending is growing and is partly funded by secured warehouse lines and new brokered certificates of deposit. | Funding for lending leans on secured and deposit-type sources outside the note stack, so note holders rank behind them on those assets. | Medium |
| A Department of Justice resolution and a derivative settlement were agreed in principle in October 2026. | The cash cost is accrued but unpaid and not final, so the payment is a claim outside the debt figures. | Medium |
| The 2026 maturities were paid in cash, the revolver was enlarged, and buybacks continued under a larger authorization. | Deleveraging from cash coexists with continued share repurchases, a mixed capital-allocation signal. | Medium |

### Business and transaction view

Block, Inc. is an operating company with two reportable segments, Square for sellers and Cash App for consumers, and a third revenue lens of commerce enablement, financial solutions and bitcoin ecosystem. It has no sponsor, no leveraged transaction and no acquisition financing in the sources. The transaction history that matters to creditors is a series of unsecured note issues (the 2032 notes in 2024, the 2030 and 2033 notes on August 18, 2025), the repayment in cash of two 2026 maturities, the January 14, 2026 amendment that enlarged the revolver and replaced its financial covenant with a maximum total net leverage ratio, a larger share repurchase authorization, and, after the quarter end but before the filing, agreements in principle on a Department of Justice deferred prosecution matter and a derivative-suit settlement. Control rests with Class B holders with ten votes per share, and the founder is described as controlling shareholder in the bank-regulatory commitments for Square Financial Services. Documented issuer behaviour is Neutral or Mixed: debt was repaid from cash and the revolver enlarged, but repurchases continue and 2025 issuance occurred in a year of large repurchases. No priming, uptiering, drop-down, non-pro-rata exchange or collateral release appears in the pages read. The creditor mechanisms to watch are lending growth funded by secured warehouse lines (which sit ahead of note holders on those receivables), the unpaid legal settlements, and the absence of the executed documents that would show restricted payments capacity.

### Company and operating model

| Area | Fact | Category | Locator | Creditor mechanic |
| --- | --- | --- | --- | --- |
| Segments | Two reportable segments, Square and Cash App, plus a corporate and other category; the chief operating decision maker uses revenue and gross profit | Documentary Fact | 10-Q Q3 page:38 | Credit view is built on segment gross profit, not segment cash flow; segment assets are not reviewed by the decision maker so segment leverage is Not disclosed |
| Revenue streams | Commerce enablement, financial solutions and bitcoin ecosystem; bitcoin ecosystem was 27% of Q3 2026 revenue but 2% of gross profit | Documentary Fact | 10-Q Q3 page:44 | Revenue growth is not a reliable cash proxy because bitcoin revenue is the gross sale amount; gross profit is the relevant base |
| Square volume driver | Square gross payment volume grew 14% in Q3 2026; processing revenue growth was approximately in line with volume growth | Documentary Fact | 10-Q Q3 page:44 | Seller payments earn on volume, so revenue is linked to small-business activity and card volumes |
| Cash App lending | Cash App Borrow revenue rose 193.6 in Q3 2026 and 844.1 in nine months 2026 against the prior-year periods (US$m) | Documentary Fact | 10-Q Q3 page:44 | Growth in short-duration consumer loans lifts revenue and also credit losses and funding needs |
| Credit losses | Transaction, loan and consumer receivable losses were 601.7 in Q3 2026 against 363.5 in Q3 2025 (US$m) | Documentary Fact | 10-Q Q3 page:5 | Loss growth is a direct draw on operating income; the metric tracks lending mix and volume |
| Management view of lending returns | Management says Consumer Lending variable profit margin was in line with Q3 2025 and Borrow risk loss rates remained healthy | Management Language | letter page:17 | Not independently verified; treat as management claim |
| Pricing | Management attributes the fall in bitcoin gross profit to a decision to reduce a fee charged on certain bitcoin transactions | Management Language | letter page:14 | Pricing choices can lower gross profit without lowering volume |
| Cost structure | A workforce reduction of more than 40% announced in February 2026 cost 495.0 in nine months 2026; management expects annualized net savings of 800 to 900 | Documentary Fact for the charge; Management Language for the savings | 10-Q Q3 pages 40, 43 | Savings are an expectation, not realized in full; execution risk applies to product and risk functions |
| Capital spending | Purchases of property and equipment were 128.0 in nine months 2026 (US$m) | Documentary Fact | 10-Q Q3 page:8 | Low capital intensity supports cash conversion before lending outflows |
| Working capital | Settlements receivable 1,454.2 against customers payable 7,700.1 at September 30, 2026; customers payable is larger because of Cash App stored funds, risk holds and chargebacks | Documentary Fact | 10-Q Q3 pages 4, 59 | Corporate cash can be partly owed to customers, which limits how much counts as surplus |
| Funding of lending | Secured warehouse borrowings of 1,543.5 through special purpose entities whose assets are not available to the company's creditors; brokered certificates of deposit of 381.4 began in Q3 2026 | Documentary Fact | 10-Q Q3 pages 29, 56 | Lending is funded ahead of note holders on those assets; renewal of deposits depends on the bank subsidiary remaining well capitalized |
| Bank subsidiary | Square Financial Services is the company's Utah state-chartered industrial loan company; the parent has capital-support commitments to the FDIC | Documentary Fact | 10-Q Q3 page:14; 10-K page:92 | Parent may have to fund the bank in stress, a contingent claim on parent liquidity |
| Segment-level debt, covenants by segment | Not disclosed | Insufficient Information | not applicable | Missing datapoint: segment debt allocation; it matters for structural ranking and is left for the debt module |

### Company profile

| Item | Detail | Category | Locator |
| --- | --- | --- | --- |
| Legal entity and filer status | Block, Inc., Delaware, large accelerated filer, Class A shares on the New York Stock Exchange (XYZ) | Documentary Fact | 10-Q Q3 page:1 |
| Founded and location | Founded in 2009; distributed work model with no formal headquarters; principal executive office address in Oakland, California | Documentary Fact | 10-Q Q3 pages 2, 9 |
| Sector and country | Services-Prepackaged Software, United States | Documentary Fact from the run context, not issuer evidence | context |
| Ownership and control | Class B has ten votes per share and Class A one; Class B holders held approximately 53% of voting power at December 31, 2025 and can control matters put to stockholders | Documentary Fact | 10-K page:99 |
| Controlling shareholder | Jack Dorsey is described as the controlling shareholder in the context of the bank-regulatory agreements and agreed to cause the company to perform them | Documentary Fact | 10-K page:92 |
| Shares outstanding | 544,546 thousand Class A and 59,976 thousand Class B at October 30, 2026 | Documentary Fact | 10-Q Q3 page:2 |
| Sponsor | None; the run context leaves the sponsor blank and no source describes one | Insufficient Information | context; sources |
| Dividend policy | The company has never declared or paid cash dividends and does not expect to | Documentary Fact | 10-K page:107 |
| Share repurchases | Authorization raised in November 2025 by up to an additional 5 billion for a total of 9 billion; 4.4 billion repurchased cumulatively, of which 700.9 in 2026 | Documentary Fact | 10-Q Q3 page:43 |
| Ratings (issuer-stated) | During 2025 Fitch assigned investment grade BBB-, Moody's non-investment grade Ba1, and S&P affirmed BB+; no agency report is supplied | Documentary Fact as a company statement; not verified externally | 10-K page:130; 10-Q Q3 page:58 |
| Auditor | Ernst & Young LLP, auditor since 2019 | Documentary Fact | 10-K pages 139, 140 |
| Related party | A lease of office space in St. Louis from an affiliate of a co-founder and director | Documentary Fact | 10-K page:206 |
| Listing | Secondary listing in Australia following the Afterpay acquisition | Documentary Fact | 10-K page:78 |

### Transaction summary and new debt issues

There is no transaction document, sponsor, use-of-proceeds statement or acquisition financing for 2026 in the sources, so no transaction row is built beyond the financing history below; that absence is Insufficient Information, not an adverse conclusion.

New debt issues. In the nine months of 2026 the company issued no senior notes: the cash flow statement shows no proceeds from issuance of senior notes for 2026 (10-Q Q3 page:8). The last note issue was on August 18, 2025, when 2.2 billion of senior unsecured notes were issued, comprising 1.2 billion of 2030 Senior Notes at 5.625% and 1.0 billion of 2033 Senior Notes at 6.000% (10-K page:188). The 2032 Senior Notes, 2.0 billion at 6.50%, were issued on May 9, 2024 (10-K page:190). In 2025 the company recorded 2.3 billion of share repurchases alongside the 2.2 billion of cash received from that issuance (10-K page:111); the filing does not say the proceeds funded the repurchases, so the link is an Analyst Interpretation of timing only.

Repayments and facility changes. The 2026 Convertible Notes (575.0) were paid in cash at maturity on May 1, 2026 and the 2026 Senior Notes (1,000.0) on June 1, 2026 (10-Q Q3 page:27), leaving note principal of 5,775.0 across the 2027 Convertible Notes and the 2030, 2031, 2032 and 2033 Senior Notes. On January 14, 2026 the revolving credit agreement was amended and restated, raising commitments from 775 to 900, extending maturity to January 14, 2031 with a springing earlier date if liquidity would fall below 250 after repaying existing notes at maturity, and replacing the prior financial covenant with a maximum total net leverage ratio tested quarterly; the revolver is undrawn (10-Q Q3 page:28). Warehouse borrowings stood at 1,543.5, with a total of 2.4 billion of capacity and 809.3 available, and final maturities through July 2029 (10-Q Q3 page:29). Brokered certificates of deposit of 381.4 par began in Q3 2026 at a weighted average rate of 4.09% (10-Q Q3 page:56).

Subsequent events and pending items (after the September 30, 2026 balance sheet date, before the November 3, 2026 filing and the cutoff). In October 2026 the company and the Department of Justice reached an agreement in principle to resolve the Bank Secrecy Act inquiry by a three-year deferred prosecution agreement, with a gross monetary component of approximately 964 million and a net payment of approximately 764 million after credit for prior regulatory resolutions; 764 million was accrued at September 30, 2026, and the resolution remains subject to a final agreement and court approval (10-Q Q3 page:34). The filing says losses in excess of the accrual are reasonably possible (10-Q Q3 page:35). Also in October 2026 the parties to the shareholder derivative actions agreed in principle to a global resolution including a 150 million payment from the defendants' insurers to the company, subject to court approval (10-Q Q3 page:36). The securities class action remains pending after the motion to dismiss was denied on January 6, 2026, with an accrual that the filing calls not material and a possible loss in excess that could be material (10-Q Q3 page:35). These items are subsequent events or pending matters and are not folded into period facts.

### Governance and capital allocation

Scope: issuer-level behaviour from documented actions only; no individuals are assessed and no willingness is inferred from ownership structure.

| Dimension | Documented action | Category | Locator | Legal capacity, willingness, feasibility |
| --- | --- | --- | --- | --- |
| Distributions | No cash dividend ever declared; repurchases of 700.9 in the first and second quarters of 2026 under a 9 billion authorization | Documentary Fact | 10-K page:107; 10-Q Q3 pages 28, 43, 60, 109 | Capacity: the credit agreement and indentures contain customary limits on restricted payments, dividends and repurchases but the terms are not supplied. Willingness: repurchases continued in 2026 while repaying maturities. Feasibility: liquidity of 10,064.0 against no bond maturity until November 2027 |
| Deleveraging | 1,575.0 of 2026 maturities repaid from cash; notes principal fell from 7,350.0 to 5,775.0 | Documentary Fact | 10-Q Q3 page:27 | Willingness shown by repayment rather than refinancing; feasibility supported by cash of 7,859.3 |
| Creditor-adverse conduct | No priming, uptiering, drop-down, non-pro-rata exchange or collateral release found in the pages read | Insufficient Information as the executed documents are not supplied | not applicable | Capacity to designate unrestricted subsidiaries or incur debt is not assessable without the indentures |
| Disclosure and compliance | Quarterly filings with reconciled non-GAAP measures; company states covenant compliance; regulatory matters accrued and disclosed | Documentary Fact | 10-Q Q3 pages 28, 34, 51 | Add-back definitions are broad (see the financial handoff); covenant certificate not supplied |
| Bank-subsidiary support | Commitments to the FDIC to support capital and to maintain a 50 million reserve deposit at an unaffiliated bank | Documentary Fact | 10-K page:92 | Parent liquidity may be called on in bank stress |

Assessed behaviour category: Neutral or Mixed, with Medium evidence quality (primary dated filings; no executed legal documents).

### Credit translations

1. Revenue durability. Evidence: bitcoin ecosystem was 27% of Q3 2026 revenue and 2% of gross profit, while commerce enablement and financial solutions revenue grew 16% and 31% in the quarter (10-Q Q3 page:44). Mechanic: revenue volatility from bitcoin prices does not transmit to gross profit, which depends on payments volume and lending. Implication: debt service capacity rests on payments and lending gross profit, so monitoring should use gross profit and loss rates, not headline revenue. Counter: no logged conflict.
2. Funding structure. Evidence: warehouse borrowings of 1,543.5 secured on receivables held in special purpose entities, and 381.4 of brokered certificates of deposit (10-Q Q3 pages 29, 56). Mechanic: lending growth is financed ahead of unsecured note holders on those assets and by deposit funding conditional on the bank staying well capitalized. Implication: recovery prospects for unsecured notes on the lending assets are weaker than headline asset totals suggest; no recovery conclusion is drawn here. Counter: no logged conflict.
3. Legal claims. Evidence: an accrual of 764 million for the Department of Justice resolution and the statement that losses in excess are reasonably possible (10-Q Q3 pages 34, 35). Mechanic: an unpaid, non-debt cash claim reduces liquidity when settled and is excluded from debt leverage ratios. Implication: net leverage and liquidity on the filed basis overstate headroom until the payment is made; monitor court approval and payment timing. Counter: the 150 million insurer receipt, if approved, is a partial offset, not logged as a conflict.
4. Capital allocation. Evidence: 2025 issuance of 2.2 billion beside 2.3 billion of repurchases, and 2026 repayment of 1,575.0 from cash alongside 700.9 of repurchases. Mechanic: shareholder returns compete with deleveraging for the same cash. Implication: leverage tolerance appears to be managed with cash buffers; no leverage target was located in the pages read, and the covenant level is not printed. Counter: no logged conflict.

### Conflicts and consistency

No conflict between sources was found in the facts used. Presentation differences were checked and are not conflicts: the Q3 2026 balance sheet shows other current assets at December 31, 2025 of 4,107.7 (10-Q Q3 page:4), while the FY2025 annual report shows 3,589.9 plus short-term debt securities of 517.8 (10-K page:140), which sum to the same figure (3,589.925 + 517.777 = 4,107.702, in thousands). Shares outstanding at September 30, 2026 (544,541 thousand Class A) and October 30, 2026 (544,546 thousand) differ by dates. The Department of Justice gross (964 million) and net (764 million) amounts are explained in the filing as before and after credit for prior resolutions. The financial handoff's 764 matches.

### Consumer readiness

| Consumer | Readiness | What to take from this module | Gap and action |
| --- | --- | --- | --- |
| CP-2 | Ready with limitations | Note and facility history, warehouse and deposit funding, bank-subsidiary support, non-debt claims including the Department of Justice accrual | Indentures, credit agreement and guarantor list not supplied; obtain the exhibits |
| CP-5 | Ready with limitations | Timeline of subsequent events, governance behaviour category, control structure | Covenant certificate and agency reports not supplied; request before final committee use |

## Calculations

No new numeric calculation is performed. Figures cited are as printed or are the accepted figures of the financial handoff (total debt to EBITDA 4.67x and 1.69x on Adjusted EBITDA, EBITDA to cash interest 3.99x, note principal 5,775.0, warehouse 1,543.5, liquidity 10,064.0, accrued legal contingencies 980.6). Two arithmetic checks on printed figures: (1) 2026 maturities repaid in cash = 575.0 + 1,000.0 = 1,575.0, and note principal 7,350.0 - 1,575.0 = 5,775.0, which equals the September 30, 2026 principal (10-Q Q3 page:27); (2) other current assets presentation check 3,589.925 + 517.777 = 4,107.702 (thousands).

## Gaps

| Gap | Severity | Affected consumers | Action |
| --- | --- | --- | --- |
| Guarantors, obligor entities and unrestricted-subsidiary mechanics not supplied | Medium | CP-2 | Obtain indentures and credit agreement |
| Executed documents absent, so legal capacity for restricted payments, liens and debt incurrence is not assessable | Medium | CP-2, CP-5 | Obtain the exhibits listed in the annual report index |
| Covenant level and compliance certificate not supplied | Medium | CP-2, CP-5 | Obtain the Restated Credit Agreement and compliance certificate |
| Department of Justice resolution is an agreement in principle, subject to final terms and court approval; payment timing not stated | Medium | CP-2, CP-5 | Monitor filings after the cutoff; no post-cutoff evidence is used |
| No sponsor, transaction document or use-of-proceeds statement for 2026 financing | Low | CP-2 | None needed unless a new financing is announced |
| Rating agency reports not supplied; ratings are company statements | Low | CP-5 | Obtain reports if rating sensitivity is required |
| Acquisition dates and prior-ownership history (for example the timing of the Afterpay acquisition) were not located in the pages read | Low | CP-1A | Search the annual report business note if the timeline is needed |
| Shareholder letters are management language, and charts are not covered by text extraction | Low | CP-1A | Use filed statements to verify any management claim before reliance |

## Next module

CP-2 should take the funding structure (note series, revolver, warehouse capacity, brokered certificates of deposit), the bank-subsidiary commitments and the non-debt claims listed above, and should treat the Department of Justice and derivative matters as subsequent events. Carry forward that the governance category is Neutral or Mixed with Medium evidence, that executed documents are the main missing evidence, and that no recovery conclusion has been drawn.
