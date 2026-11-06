# CP-1A — Business and transaction context: NCL CORP Ltd. (ncl-corp-ltd)

## Request

- Issuer: NCL CORP Ltd. (issuer id `ncl-corp-ltd`; the filings name the registrant NCL Corporation Ltd., "NCLC"), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; amounts are US$ millions (US$m) converted from the thousands the statements print, unless a filing prints dollars in words. Current period Q3 2026; prior period FY2025.
- Run: `ncl-corp-ltd-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Question: which transaction, business, ownership and operating facts matter most to a creditor of NCLC? The context names no deal, sponsor, borrower, guarantor or research question, so the answer rests on the filings.
- Perimeter: NCLC and its consolidated subsidiaries as filed. The parent Norwegian Cruise Line Holdings Ltd. ("NCLH") is a separate registrant; its press releases are labelled parent-level wherever used.
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers. Each fact row carries one category: Documentary Fact, Management Language, Analyst Interpretation or Insufficient Information.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | 1590d4030e80abfbd09d00a74521526f72070052531a8716f865a880a8fa9501 | Annual report for FY2025: business, fleet, ownership, human capital, debt history |
| 10-Q_2026-03-31_nclc-20260331x10q.htm.jsonl | 1693fea3f52de137a2e148c9e6f9853be5398eb34944625b7e837b2bd396c943 | Q1 2026 quarterly report: Norwegian Luna delivery |
| 10-Q_2026-06-30_nclc-20260630x10q.htm.jsonl | 2f18ccd1a947471efb9474a7bd377c5db5871d9445b97fe0a1fc7e783f6d645f | Q2 2026 quarterly report: exchangeable note settlement election, Oceania Sirena agreement |
| 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | 7769d1c310cec4c8e024523931f2cd599a487768128283054dca38ddd11d7d93 | Q3 2026 quarterly report: fleet optimization, October 2026 financing, newbuild program |
| EX-99.1_2026-05-04_exh_991.htm.jsonl | 19e48d4c7cb2b40fb1bcbfbbe436e7e39f669c8965c4e705c327d948db3f04d8 | Q1 2026 parent press release (management-prepared, parent-level) |
| EX-99.1_2026-07-30_exh_991.htm.jsonl | ffe75efbccd58bfc3c88fabf4a188883f7003d5a095dba1da47bbe08c4d94307 | Q2 2026 parent press release (management-prepared, parent-level) |
| EX-99.1_2026-10-29_exh_991.htm.jsonl | 6f93f8906074ef388d05f277a1b3874ed298e830f3945372d3d73a8925dc791c | Q3 2026 parent press release (management-prepared, parent-level) |
| context | 1eac4b587c5c6cd9d96c3f400eed0e70dc9aa1137a14c30469dde7d21791294f | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 240a9004c9f054e89ac320762ee0dbd447c416d5523fbbb0826a7a829f32f3c2 | Source readiness: perimeter conflict between issuer filings and parent releases; missing agreements |
| CP-1 | 0d306e620183fe5605e53df2bfa6840225b9fdf3340d4d66074ce76c6547a7b6 | Financial base: debt, liquidity, maturities, newbuild commitments and the October 2026 financing, all on the issuer's own perimeter |

Consistency with CP-0 and CP-1: this answer confirms both. It uses CP-1 only for financial context (debt, liquidity, newbuild commitments); figures are quoted from the filings again with their own locators. CP-1 gives no ship count; the fleet count is set out here, with the reason it moved from 34 to 33. No earlier statement is withdrawn.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| NCLC is a wholly owned cruise subsidiary of NCLH with three brands and 33 ships, funding a large newbuild program with export-credit loans while the parent runs a turnaround and sells older ships. No sponsor or distribution is documented. | Medium | Governance, ownership detail and the parent's plans are only in a reduced-disclosure annual report and parent press releases. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| NCLH owns all NCLC ordinary shares and guarantees the exchangeable notes; the notes exchange into NCLH shares. | Parent support and share-price linkage matter to the exchangeable notes; control sits with the parent. | Medium |
| The business is a three-brand cruise operator with seasonal demand, about 84% U.S.-sourced guests and advance ticket sales funding working capital. | Cash conversion depends on bookings and customer deposits, which are partly refundable. | Medium |
| Thirteen effective newbuild contracts carry large commitments, and three effective contracts are not yet financed. | Funding of later deliveries is not secured, and capital spending will keep debt high. | Medium |
| Older ships are being chartered or sold, and October 2026 brought a new notes issue and a larger revolver. | Asset sales and refinancing support liquidity, but loss of sold ships reduces the collateral and earnings base. | Medium |

### Business and transaction view

The credit-relevant structure is simple but concentrated. NCLC is the operating cruise subsidiary of a listed parent, owns three brands (Norwegian Cruise Line, Oceania Cruises and Regent Seven Seas Cruises) and ships them in one reportable segment, so there is no segment to diversify away from a weak brand. NCLH owns all NCLC ordinary shares, guarantees NCLC's exchangeable notes, receives NCLC's cash only subject to debt-agreement restrictions, and its equity price drives the value of the exchange option inside those notes. The operating model is a high fixed-cost, seasonal business that collects cash ahead of sailing: advance ticket sales are the main working capital funding and are partly refundable, so booking strength is the lead indicator of liquidity. Capital intensity is high and rising: the filings list 13 effective newbuild contracts, export-credit financing for roughly four fifths of most contracts, and three effective contracts that are not yet financed. In 2026 the company is actively reshaping the fleet, with long-term charters and sales of older ships, a new chief executive from February 2026, cost-saving programs and a booked position that management says remains below its optimal range. There is no sponsor, no merger and no dividend recapitalisation in the sources. The transaction content is therefore financing and fleet transactions, which are dated and described below. The sources lack governance papers for the issuer (the annual report uses a reduced disclosure format), the credit agreements, and any statement of how NCLH's strategy would be funded at NCLC. Those gaps limit, but do not block, the downstream work.

### Company and operating model

| Area | Fact | Category | Locator | Credit relevance |
| --- | --- | --- | --- | --- |
| Core activity | “We are a leading global cruise company, which operates the Norwegian Cruise Line, Oceania Cruises and Regent Seven Seas Cruises brands.” At September 30, 2026 the combined fleet was 33 ships with approximately 72,000 Berths. | Documentary Fact | Q3 10-Q page:5 | Revenue rests on discretionary leisure travel across three price tiers. |
| Fleet movement | The fleet was 34 ships with approximately 71,400 Berths at December 31, 2025; the decrease since June 30, 2026 is due to Norwegian Sky and Oceania Regatta commencing long-term charters to third parties. | Documentary Fact | 10-K page:9; Q3 10-Q page:5 | Chartered-out ships leave the operated fleet and the earnings base, but may be retained as assets. |
| Segment | The business has a single reportable segment; each brand is a business for which discrete information is available. | Documentary Fact | 10-K page:128 | No segment diversification inside the issuer. |
| Revenue model | Passenger ticket revenue (accommodation, meals, entertainment, taxes and port fees, air and land packages) and onboard and other revenue (casino, beverage, shore excursions, specialty dining, retail, spa, Wi-Fi and long-term ship charters). Nine months 2026 revenue was 5,217.8 passenger ticket and 2,700.7 onboard and other (US$m). | Documentary Fact | Q3 10-Q page:2 and page:31 | Onboard revenue carries direct costs and depends on guest spending on board. |
| Geography and customers | “Our revenue attributable to U.S.-sourced guests has approximated 84% of total revenue over the preceding three fiscal years.” is the concentration disclosed; revenue by destination for nine months 2026 is North America 4,991.7, Europe 2,104.9, Asia-Pacific 588.2 and Other 233.7 against 4,200.7, 2,386.5, 763.6 and 232.5 for nine months 2025 (US$m). | Documentary Fact | Q3 10-Q page:9 | A single source market dominates demand; Europe and Asia-Pacific revenue fell year on year while North America rose. |
| Pricing and inclusions | Norwegian prices typically include meals in certain dining facilities and many onboard activities; Oceania Cruises prices include specialty dining, Wi-Fi, laundry and gratuities; Regent fares are all-inclusive including unlimited shore excursions. | Documentary Fact | 10-K page:13 and page:10 | Brand positioning ranges from mass-premium to luxury; pricing is the main yield lever. |
| Volume and yield drivers | Capacity Days, occupancy and Net Yield: for Q3 2026 Net Yield per Capacity Day was 319.65 against 341.89 and occupancy 106.5% against 106.4%. | Documentary Fact | Q3 10-Q page:34 | Volume grew while yield fell, so earnings depend on price recovery. |
| Seasonality | “Our operations are seasonal and results for interim periods are not necessarily indicative of the results for the entire fiscal year.” Demand is strongest in the Northern Hemisphere summer. | Documentary Fact | 10-K page:13 | The third quarter carries most profit; interim leverage and liquidity swing seasonally. |
| Cost structure | Largest operating costs are payroll and related (including a third-party crew services contract), fuel, airfare, food and beverage, advertising and travel advisor services; fuel was approximately 48% hedged for the remainder of 2026. | Documentary Fact | 10-K page:13; Q3 10-Q page:33 | Fuel and payroll are the volatile cost lines; hedging covers part of the fuel risk only. |
| Capital spending | Non-cancelable ship construction contracts for 13 effective newbuilds; committed undrawn export-credit facilities of approximately 10.8 billion fund approximately 80% of most contracts. | Documentary Fact | Q3 10-Q page:20 and page:42 | Capital spending is contractual and euro-denominated; financing is mostly committed but not complete. |
| Working capital | “As of December 31, 2025, we had a working capital deficit of $4.4 billion” including $3.2 billion of advance ticket sales, which management describes as substantially like deferred revenue. | Management Language | 10-K page:84 | Customer deposits fund operations and are partly refundable, so a booking slowdown drains cash. |
| Employees and crew | Approximately 5,300 full-time shoreside employees and approximately 39,200 shipboard employees at December 31, 2025; Regent and Oceania ships use a third party for additional hotel and restaurant staffing; collective bargaining agreements cover certain crew members. | Documentary Fact | 10-K page:32 and page:57 | Labor cost and work disruption are disclosed risks. |
| Private destinations | The company operates Great Stirrup Cay in The Bahamas and Harvest Caye in Belize; the Great Tides Waterpark at Great Stirrup Cay opened in September 2026. | Documentary Fact | 10-K page:10; Q3 10-Q page:32 | Owned destinations support itineraries and onboard spend; their costs are capital items. |
| Competition | Primary competitors include Carnival and Royal Caribbean, as well as MSC Cruises, Viking Ocean Cruises and Virgin Voyages, and land-based vacation alternatives. | Documentary Fact | 10-K page:13 | Industry capacity and pricing are set by larger peers. |

### Company profile

| Item | Detail | Category | Locator |
| --- | --- | --- | --- |
| Legal name and form | NCL Corporation Ltd., a Bermuda exempted company; Commission File Number 333-128780 | Documentary Fact | Q3 10-Q page:1; 10-K page:17 |
| Filer status | Voluntary filer; non-accelerated filer; files the 10-K “with the reduced disclosure format permitted by General Instruction I(2)” | Documentary Fact | Q3 10-Q page:1; 10-K page:2 |
| Headquarters | 7665 Corporate Center Drive, Miami, Florida; registered office in Hamilton, Bermuda | Documentary Fact | Q3 10-Q page:1; 10-K page:9 |
| Sector and country | Water transportation and Bermuda per the context; cruise operations worldwide | Documentary Fact | context; 10-K page:8 |
| Ownership | “Norwegian Cruise Line Holdings Ltd. owns all of the outstanding ordinary shares of the registrant.” 31,164,004 ordinary shares outstanding at October 22, 2026. No market for the shares. | Documentary Fact | 10-K page:2; Q3 10-Q page:1 |
| Brands | Norwegian Cruise Line, Oceania Cruises, Regent Seven Seas Cruises | Documentary Fact | 10-K page:8 |
| Ship registry | Twenty-two ships registered in The Bahamas, eleven in the Marshall Islands and one U.S.-flagged ship (Pride of America) at the 10-K date | Documentary Fact | 10-K page:15 |
| History | Norwegian commenced operations in 1966; NCLH formed in February 2011; NCLH became owner of 100% of NCLC ordinary shares on its January 2013 initial public offering; acquisition of PCI in November 2014; late 2023 reorganization realigning operations into Bermuda | Documentary Fact | 10-K page:8 |
| Executive officers | The 10-K lists NCLH's executive officers; John W. Chidsey has been President and Chief Executive Officer since February 2026 and signed the NCLC 10-K in that role. | Documentary Fact | 10-K page:36, page:37 and page:117 |
| Auditor | PricewaterhouseCoopers LLP, report dated March 2, 2026 | Documentary Fact | 10-K page:121 |
| Ratings | Moody's long-term issuer rating B1 and senior unsecured B3; S&P Global issuer credit rating B+, revolver issue-level BB, senior unsecured B+ | Documentary Fact | Q3 10-Q page:39 |
| Beneficial ownership, board and executive compensation | Items 10 to 13 of the 10-K are omitted under the reduced disclosure format as a wholly owned subsidiary of NCLH | Insufficient Information | 10-K page:94 |

### Transaction summary and new debt issues

There is no acquisition, merger, sponsor transaction or leveraged buyout in the sources, and the context supplies no deal terms, so the transaction content is financing and fleet activity, with each item below at its stated status.

Completed in FY2025 (10-K page:141 to page:146): in January 2025 NCLC issued senior unsecured notes due 2032 and amended and restated the Revolving Loan Facility (the Seventh ARCA); in April 2025 it exchanged part of its 2025 exchangeable notes into new 2030 0.875% Exchangeable Notes; in June 2025 it amended the facility to raise commitments to approximately 2.5 billion; in September 2025 it issued 2030 0.750% Exchangeable Notes, 5.875% senior unsecured notes due 2031 and 6.250% notes due 2033 and used the exchangeable proceeds, together with the proceeds of an NCLH equity offering and cash, to repurchase most of the 2027 exchangeable notes. NCLH's equity offerings in April and September 2025 supplied cash used in those exchange and repurchase steps. Newbuild export-credit loans for Norwegian Aqua (March 2025) and Oceania Allura (July 2025) were also drawn.

Completed in 2026 (Q1 10-Q page:9; Q2 10-Q page:10; Q3 10-Q page:11 and page:32): delivery of Norwegian Luna in March 2026 with a €1.0 billion export-credit term loan at 1.91% maturing February 25, 2038; an irrevocable election in May 2026 to settle exchanges of both 2027 exchangeable note series in cash; the sale of Oceania Sirena in September 2026 with continued operation under a bareboat charter through spring 2028; the start of the Norwegian Sky bareboat charter in September 2026; and the start of a two-year time charter for Oceania Regatta in September 2026.

Executed and pending: a nine-year lease of Seven Seas Navigator executed in March 2026, commencing December 2027 (Q3 10-Q page:10); a ten-year bareboat charter for Norwegian Sun expected to commence in late 2027 (Q3 10-Q page:32); and a memorandum of agreement for the sale of Oceania Insignia, with closing in September 2027 (Q3 10-Q page:24). The sale price and the buyer are Not supplied.

New debt after the quarter and before the cutoff: on October 15, 2026 NCLC issued 950.0 of 8.750% senior unsecured notes due October 15, 2031, used with cash on hand to redeem all of the outstanding 6.125% senior notes due 2028, repay 380.0 of revolver borrowings and prepay about 42.2 of export-credit facilities, and entered into a third amendment that raised Revolving Loan Facility commitments from approximately 2.5 billion to approximately 2.8 billion and modified certain financial covenant definitions and collateral (Q3 10-Q page:11 to page:12; Q3 release page:1). The parent release adds a pro forma liquidity figure of 2.1 billion at September 30, 2026 (Q3 release page:3), which is parent-level and management-prepared. The indenture and amendment texts are Not supplied. Merger-related debt does not exist in the sources; the one liquidity effect described for the issuer is the October 2026 refinancing.

### Ownership, governance and sponsor behaviour

| Behaviour or fact | Evidence | Category | Legal capacity, willingness and feasibility | Locator |
| --- | --- | --- | --- | --- |
| Parent ownership | NCLH owns all outstanding ordinary shares; one record holder | Documentary Fact | Capacity: parent controls all corporate decisions. Willingness: see support and distributions below. | 10-K page:71 |
| Distribution restrictions | “our existing debt agreements restrict, and any of our future debt arrangements may restrict, among other things, the ability of NCLC to make distributions and/or pay dividends to NCLH” | Documentary Fact | Capacity: limited by debt agreements; the baskets are not supplied. | Q3 10-Q page:42 |
| Dividends to the parent | No dividend or distribution line appears in the cash flow statements for FY2025 or nine months 2026 | Documentary Fact | Willingness: no cash was upstreamed through distributions in those periods. | 10-K page:123; Q3 10-Q page:3 |
| Equity support from the parent | “Contribution from NCLH” of 145.0 in FY2025 and 145.3 in nine months 2025; no contribution line in nine months 2026 | Documentary Fact | Willingness: NCLH passed equity proceeds to NCLC in 2025. Feasibility in 2026 depends on parent access to equity. | 10-K page:123; Q3 10-Q page:4 |
| Parent guarantee | NCLH guarantees the exchangeable notes on a senior unsecured basis; the exchange obligation settles in cash up to principal and cash or NCLH shares for the remainder | Documentary Fact | Capacity: guarantee gives holders a claim on NCLH. The security and guarantee package for senior notes is not stated in the pages read. | 10-K page:144 |
| Intercompany balance | Current liability “Due to NCLH” at September 30, 2026 | Documentary Fact | Small balance; a related-party claim of the parent on NCLC. | Q3 10-Q page:3 |
| Parent equity awards funded by NCLC | NCLC pays net share settlement of restricted share units in cash, 31.1 in nine months 2026 against 23.8 | Documentary Fact | Cash leaves NCLC to settle taxes on parent-granted awards; small. | Q3 10-Q page:4 |
| Management change and cost program | President and Chief Executive Officer since February 2026; professional advisory fees tied to activist investor activity and restructuring costs were added back in nine months 2026 | Documentary Fact | Governance pressure sits at the parent; costs fall in NCLC's reported results. | 10-K page:37; Q3 10-Q page:7 and page:36 |
| Management description of strategy | “As we implement the next phase of our turnaround” (parent chief executive in the release); savings programs described as expected run-rate savings | Management Language | Quoted and not adopted as a result. | Q3 release page:1; Q3 10-Q page:33 |
| Asset monetisation | Sale of Oceania Sirena and charters of older ships; proceeds from sale of ships in nine months 2026 | Documentary Fact | Willingness: disposal proceeds sit inside NCLC; use of proceeds beyond the October 2026 debt actions is not stated. | Q3 10-Q page:3 and page:32 |
| Creditor-adverse transactions | No uptier, drop-down, priming, non-pro-rata exchange, unrestricted-subsidiary designation or collateral release by NCLC was found in the seven sources; the third amendment modified collateral | Insufficient Information | Absence in filings is not proof of absence in agreements; the amendment text is not supplied. | all sources; Q3 10-Q page:12 |

Behaviour category (issuer-level, documented actions only): Supportive or Neutral. The documented actions are equity contributions passed down by the parent in 2025, no distributions to the parent in the periods read, refinancing that extended maturities, and ship monetisation applied alongside debt reduction in October 2026. No extraction or creditor-adverse transaction is documented. Parent intentions are not assessable from these sources.

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| 1966 | Norwegian commences operations from Miami | Documentary Fact | 10-K page:8 |
| February 2011 | NCLH formed | Documentary Fact | 10-K page:8 |
| January 2013 | NCLH initial public offering; NCLH becomes owner of 100% of NCLC ordinary shares | Documentary Fact | 10-K page:8 |
| November 2014 | Acquisition of PCI | Documentary Fact | 10-K page:8 |
| Late 2023 | Reorganization realigning operations into Bermuda | Documentary Fact | 10-K page:8 |
| January 2025 | Senior unsecured notes due 2032 issued; Seventh ARCA | Documentary Fact | 10-K page:141 to page:142 |
| April to September 2025 | Exchangeable note exchanges and repurchases; June 2025 revolver upsizing; September 2025 senior notes due 2031 and 2033 | Documentary Fact | 10-K page:143 to page:146 |
| February 2026 | John W. Chidsey becomes President and Chief Executive Officer | Documentary Fact | 10-K page:37 |
| March 2026 | Norwegian Luna delivered with a €1.0 billion export-credit loan; lease of Seven Seas Navigator executed | Documentary Fact | Q1 10-Q page:9; Q3 10-Q page:10 |
| May 2026 | Cash settlement fixed for 2027 exchangeable notes | Documentary Fact | Q2 10-Q page:10 |
| July 2026 | Memorandum of agreement for sale of Oceania Sirena (subsequent event in the Q2 report) | Documentary Fact | Q2 10-Q page:21 to page:22 |
| September 2026 | Oceania Sirena sold and chartered back; Norwegian Sky bareboat charter and Oceania Regatta time charter begin; Great Tides Waterpark opens | Documentary Fact | Q3 10-Q page:32; Q3 release page:1 |
| October 2026 | 8.750% senior notes due 2031 issued; revolver third amendment; memorandum of agreement for sale of Oceania Insignia (subsequent events to the Q3 period) | Documentary Fact | Q3 10-Q page:11, page:12 and page:24 |
| Late December 2026 (expected) | Seven Seas Prestige delivery expected, delayed per the parent release (future, parent-level) | Management Language | Q3 release page:2 |
| 2027 and later | Scheduled newbuild deliveries; November 17, 2026 and later contractual dates in the debt documents are future contract terms | Documentary Fact | Q3 10-Q page:41; 10-K page:142 |

### Conflicts and unresolved distinctions

| Item | Span 1 | Span 2 | Effect |
| --- | --- | --- | --- |
| Meaning of "2031 Notes" | The 10-K defines "2031 Notes" as the “$1.2 billion aggregate principal amount of 5.875% senior unsecured notes due 2031” (10-K page:146) | The Q3 10-Q defines "2031 Notes" as the “8.750% senior unsecured notes due October 15, 2031” (Q3 10-Q page:11) | Logged, not reconciled. Two different instruments share a label. Downstream work must name coupon and issue date. |
| Issuer versus parent figures | The Q3 10-Q liquidity statement is the issuer's (Q3 10-Q page:6) | The Q3 release states liquidity on the parent's perimeter, including a pro forma figure (Q3 release page:3) | Logged, not reconciled. Only the issuer's filing is used as an issuer fact. |
| Fleet count | 34 ships at December 31, 2025 (10-K page:9) | 33 ships at September 30, 2026 (Q3 10-Q page:5) | Not a conflict of fact: two charters began in 2026; Oceania Sirena was sold in September 2026 and remained operated under charter, and the filing does not say how that vessel is counted. |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence |
| --- | --- | --- | --- | --- |
| Revenue durability | About 84% of revenue from U.S.-sourced guests; Net Yield lower in Q3 2026 and the booked position “remains below its optimal range” (Q3 10-Q page:9 and page:32) | Concentrated demand and lower yield reduce margin resilience and revenue visibility. | Earnings recovery is the main lever for leverage; it is unproven. | Pricing for 2027 is said to be ahead of the prior year (Q3 10-Q page:32). |
| Cash conversion and liquidity | Advance ticket sales fund a working capital deficit of $4.4 billion at FY2025 (10-K page:84) | Customer deposits are partly refundable, so a booking or sentiment shock can reverse inflows. | Liquidity is sensitive to demand; the revolver is the buffer. | Revolver capacity was increased in October 2026 (Q3 10-Q page:12). |
| Capital intensity and refinancing | 13 effective newbuilds; three effective contracts “Contract effective, but not yet financed” (Q3 10-Q page:41) | Delivery obligations arrive whether or not financing is secured. | Leverage is held high by growth capex; unfinanced deliveries are a future funding need. | About 10.8 billion of committed export-credit facilities fund most contracts (Q3 10-Q page:42). |
| Parent linkage | NCLH guarantees exchangeable notes that exchange into NCLH shares (10-K page:144) | Note value and settlement depend on the parent share price and NCLC's election between cash and shares. | The parent is a credit support and a dependency; the exchangeable notes are not purely NCLC debt risk. | Cash settlement of the 2027 series was fixed in May 2026 (Q2 10-Q page:10). |
| Asset base | Charters and sales of older ships, some with purchase options (Q3 10-Q page:32) | Disposal reduces owned earning capacity and may release collateral. | Collateral and earnings base shrink even as debt is reduced; the pledged asset values are not supplied beyond an aggregate net book value. | Sales proceeds and charter income offset part of the loss. |
| Key uncertainties | Covenant definitions amended in October 2026; amendment text not supplied | Headroom against maintenance tests cannot be verified. | Monitoring posture is cautious until agreements are read. | Compliance with covenants is stated at September 30, 2026 (Q3 10-Q page:13). |

### Monitoring gaps and consumers

| Item the source set lacks | Severity | Consumer affected |
| --- | --- | --- |
| Credit agreements, indentures, the October 2026 third amendment and covenant compliance certificate | High | CP-2 |
| Guarantor roster and security by debt instrument | Medium | CP-2 |
| Governance, board, executive compensation and beneficial ownership detail (omitted under reduced disclosure) | Medium | CP-5 |
| Price and buyer for the Oceania Insignia and Oceania Sirena sales; collateral released | Medium | CP-2 |
| Booking data beyond management statements | Low | CP-2 |

| Consumer | Readiness | Take from this handoff | Why it matters | Gap and action |
| --- | --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Parent linkage, newbuild commitments and unfinanced contracts, fleet disposals, October 2026 financing and the label ambiguity for the 2031 Notes | These drive structure, refinancing and recovery mechanics | Obtain the agreements; name each instrument by coupon and date; keep issuer and parent figures apart |
| CP-5 | READY_WITH_LIMITATIONS | Every fact here has a category and page locator; conflicts are logged and not reconciled | Claims need traceable evidence | Verify quoted spans against the filed documents; treat parent release statements as management-prepared |

## Calculations

No new calculation is made in this module. Figures are quoted from the filings (US$ thousands divided by 1,000 where the statement prints thousands). Direction statements rest on two printed figures each: Net Yield 319.65 against 341.89 and occupancy 106.5% against 106.4% (Q3 10-Q page:34); revenue by destination for nine months 2026 against nine months 2025 (Q3 10-Q page:9); equity contributions of 145.0 and 145.3 (10-K page:123; Q3 10-Q page:5); net share settlement of 31.1 against 23.8 (Q3 10-Q page:3). The count of 13 effective newbuilds and the three not yet financed come from the status column of the newbuild chart (Q3 10-Q page:41).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreements, indentures, the third amendment and compliance certificates are not supplied. | High | CP-2, CP-5 | Obtain from exhibit filings. |
| Guarantor roster and security package by instrument are not stated in the pages read. | Medium | CP-2 | Obtain the indentures or any exhibit listing guarantors. |
| Governance, board, beneficial ownership and executive compensation are omitted by the reduced disclosure format; officers listed are NCLH's. | Medium | CP-5 | Treat governance as parent-level; look to NCLH filings for detail. |
| Sale prices, buyers and collateral release for Oceania Sirena and Oceania Insignia are Not supplied. | Medium | CP-2 | Obtain Form 8-K or exhibits if filed. |
| Parent strategy and intentions are available only in management-prepared parent press releases. | Medium | CP-2 | Label as Management Language. |
| Events between October 29, 2026 and 2026-11-05 are Not supplied. | Low | All | State as Not supplied. |
| Text extraction was not compared with the filed HTML; tables are flattened. | Low | CP-5 | Re-check figures that drive a conclusion. |

## Next module

CP-2 should run next on the fundamental credit synthesis, consuming the debt, liquidity and maturity facts from CP-1 and the structure, parent linkage, newbuild funding and fleet disposal context from this handoff. Carry forward: the issuer-only perimeter, the two different instruments called "2031 Notes", the unfinanced effective newbuild contracts, the missing agreements, and the absence of any sponsor, merger or distribution in the sources.
