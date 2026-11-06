## Request

Issuer: ENTEGRIS INC (Entegris, Inc. and subsidiaries; NASDAQ: ENTG; issuer id entg). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency USD, amounts in millions as filed. Task: build the business, ownership, operating-model and transaction fact pack that a credit committee reads first, with a creditor-side view of capital-allocation behaviour and the gaps that limit it. No peer ranking, instrument recommendation or recovery conclusion is given. Run context fields for parent, borrower, guarantors and sponsor are blank, so none is assumed; blank is not read as "none exists".

Locator abbreviations: `10-K` (annual report FY2025), `Q1 10-Q`, `Q2 10-Q`, `Q3 10-Q` (quarters ended March 28, June 27 and September 26, 2026), `Q1 release`, `Q2 release`, `Q3 release` (Exhibit 99.1 earnings releases dated April 30, August 4 and October 29, 2026). `page:N` is the chunk number of the pinned extraction, not the printed page. Fact categories are Documentary Fact, Management Language, Analyst Interpretation and Insufficient Information.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Relied on for |
| --- | --- | --- |
| `10-K_2025-12-31_entg-20251231.htm.jsonl` | `260dc4cc98d7ad114dcfe1b4d9e49beac9ed9f7c97f27f59e6df3a75c0628528` | Business, customers, history, divestitures, capital allocation, risk factors, exhibit list |
| `10-Q_2026-03-28_entg-20260328.htm.jsonl` | `3b83d32b0eaaaa1280f7799359a8f16448b715b610a83c1edceec0d49387802a` | First-quarter 2026 officer signature and subsequent events |
| `10-Q_2026-06-27_entg-20260627.htm.jsonl` | `5d06fd99ce42692b479a85d0b3d96bd08dbc1bdd295141cd5adf69b1988058ed` | Second-quarter 2026 restructuring, voluntary debt payment, officer signature |
| `10-Q_2026-09-26_entg-20260926.htm.jsonl` | `7b5685a1d8fe745548fe7c65968e18c36857c1e4dd7f2b8045f8166b689f4db9` | Latest operating model, customer categories, geography, working capital, subsequent events, controls |
| `EX-99.1_2026-04-30_entgq12026ex991.htm.jsonl` | `0e10b62e7e542aab19ae90b6d94252e94c7183b272237a1b5ecd040e7a3bb9d7` | Reviewed; no business fact beyond the filings used |
| `EX-99.1_2026-08-04_entgq22026ex991.htm.jsonl` | `729b6288fa7f91f06fa1d1330da9031db0436138ba5a59730b16535055ac78c0` | Reviewed; no business fact beyond the filings used |
| `EX-99.1_2026-10-29_entgq32026ex991.htm.jsonl` | `e35116403bbcb30c3a986093aa969493d265b238a073d77c0b1aa4aec9296a99` | Management commentary, fourth-quarter outlook, Capital Markets Day notice |

Run settings (not issuer evidence): `context`, sha256 `a75dcef49bab6da60dc1054c04d1bf4409ccb60667119c9ab2f0bfc98a4c262f`; it supplies the sector label, ticker and country.

### Upstream handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | `69484fc1896f94421c30f81bc1a11d139a430313a621007d9d0706850a8bf3c8` | Source readiness, document list, conflicts and gaps (no guarantor list, no financing contracts) |
| CP-1 | `82c71de6730d91491596125486a55b1b0f81a9f0dbf34c12db6c3b2214bb379a` | Financial base: leverage, liquidity, debt schedule, cash flow and definition limits; amounts below that repeat CP-1 figures are the same figures |

Consistency with upstream. This handoff agrees with CP-0 and CP-1 and corrects neither. It uses the CP-1 figures unchanged (par debt $3,295.0 million at September 26, 2026; LTM Q3 2026 Adjusted EBITDA $1,008.2 million) and carries forward the CP-0 and CP-1 limits: no covenant ratio, no letters of credit, no guarantor schedule.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Entegris is a widely held semiconductor materials supplier with no sponsor or parent identified. Customer concentration and cyclical demand drive business risk, while documented capital allocation favours debt repayment. Transaction evidence is limited to a revolver amendment. | Medium | Financing contracts, holder detail beyond a record count, credit ratings and customer concentration after FY2025 are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| TSMC was 16% of FY2025 net sales and the top ten customers were 50%; customers give non-binding forecasts without long-term purchase commitments. | Revenue visibility is short and concentrated, so one customer's capital plan can move cash flow. | High |
| Q3 2026 net sales rose 24.6% year on year, mainly on volume; Equipment and Engineering sales rose from $115.2 million to $192.1 million. | Growth includes more cyclical equipment-linked demand, which can reverse and weaken margin and leverage gains. | Medium |
| No sponsor, parent or controlling holder is identified; dividends were $0.10 per share each quarter and no shares were repurchased in FY2025. | No sponsor-driven extraction is documented, but legal capacity to distribute cannot be tested without the credit agreement. | Medium |
| The 2026 financing events in the pack are the April 29, 2026 revolver amendment and full term loan repayment; no new notes appear. | Financing activity reduced debt and extended the revolver rather than adding claims. | High |
| Raw materials include single-source inputs, China sales were flat, and $8.3 million of tariff refunds were received in Q3 2026. | Supply and trade shocks can hit margins; the refund is a one-off that lifts reported 2026 margins. | Medium |

### Business and transaction view

The business context is usable, with a clear picture of what the company does and a thin picture of who owns it and what it has contracted. Entegris sells consumable materials and purity equipment into semiconductor fabrication through two segments, Materials Solutions and Advanced Purity Solutions, and describes its revenue as predominantly unit-driven or recurring (management language, `10-K page:9`). The mechanism that matters to a creditor is demand linkage: sales follow wafer starts and fab build-outs, a few very large customers account for half of sales, and customers carry no long-term purchase commitments, so revenue visibility is short and a cut in one customer's capital plan transmits quickly into volume, operating leverage and debt service. The latest quarter shows the upside of that link: Q3 2026 net sales grew 24.6% on volume, but the equipment-linked customer category grew far faster than fabs, which is the more cyclical part of the mix. On ownership and transactions, the pack shows a publicly traded company with 907 holders of record, no sponsor, no parent, no acquisition disclosed and no new debt issue; the transaction history is a portfolio clean-up between 2023 and 2025 whose asset sales coincided with large debt repayments, and the 2026 financing events are an amended revolver and repayment of the term loan from cash flow. What the pack cannot show is who the large holders are, what the financing documents permit beyond summaries, and how the company is rated.

### Company and operating model

| Area | Item | Fact | Category | Locator | Credit relevance |
| --- | --- | --- | --- | --- | --- |
| Business | Core activity | Supplier of critical advanced materials and process solutions for the semiconductor and other high-technology industries, in two segments: Materials Solutions (deposition materials, CMP slurries and pads, implant gases, etch and clean materials) and Advanced Purity Solutions (filtration, purification, contamination control, wafer carriers, fluid handling) | Documentary Fact | `Q3 10-Q page:8`, `page:14`; `10-K page:4` | Mix of consumables and purity products ties revenue to wafer volume, not only to equipment orders |
| Revenue model | Unit-driven or recurring | In 2025 revenue was predominantly unit-driven or recurring from products consumed in manufacturing; no single product platform exceeded 3% of net sales | Management Language | `10-K page:9`, `page:10` | Supports revenue durability through a downturn if wafer volumes hold; the 3% platform statement is management's, not tested |
| Revenue model | Contract terms | Supply agreements typically carry no long-term purchase commitments; customers give non-binding forecasts and may cancel, adjust or delay | Documentary Fact | `10-K page:18` | Short visibility; no contracted backlog to underpin debt service |
| Customers | Concentration | TSMC 16% of net sales in 2025 and 2024 and 11% in 2023; top ten customers 50%, 48% and 43% in 2025, 2024 and 2023. FY2025 is the latest disclosure; quarterly reports do not update it | Documentary Fact | `10-K page:18`, `page:38` | One customer's capital plan or dual-sourcing decision can move sales and operating leverage |
| End markets | Customer category, Q3 2026 net sales | Fabs 589.8; Equipment and Engineering 192.1; Chemical and Materials 103.5; Semi Distributor and Other 70.7; Non-Semi 49.6; total 1,005.7 | Documentary Fact | `Q3 10-Q page:10` | Fabs are 58.6% and Equipment and Engineering 19.1% of the quarter (calculations C1) |
| End markets | Year-on-year movement, Q3 2026 against Q3 2025 | Fabs 589.8 against 494.5; Equipment and Engineering 192.1 against 115.2 | Documentary Fact | `Q3 10-Q page:10` | Equipment and Engineering rose 66.8% against 19.3% for Fabs (C2); this category tracks equipment shipments and is the more cyclical piece |
| Demand drivers | Volume | Q3 2026 net sales rose by 205.8 from volume, partly offset by 7.2 of foreign currency translation; management attributes the rise to demand across both segments, particularly advanced logic and memory and the fabs being built for them | Documentary Fact; attribution is Management Language | `Q3 10-Q page:23` | Growth is volume-led, not price-led; price effect is Not disclosed |
| Pricing | Price realisation | Not disclosed; the sales bridge shows only volume and currency | Insufficient Information | `Q3 10-Q page:23` | Margin durability cannot be separated into price and mix |
| Geography | Customer location, Q3 2026 (printed shares) | Taiwan 26%, China 18%, North America 17%, South Korea 13%, Japan 10%, Southeast Asia 9%, Europe 7%; China sales flat year on year; international sales were 82% of FY2025 net sales | Documentary Fact | `Q3 10-Q page:23`; `10-K page:33`, `page:34` | Concentration in Taiwan and East Asia exposes sales to export-control and cross-strait risk the company itself lists |
| Segments | Segment profit, nine months 2026 | Materials Solutions net sales 1,126.5 and segment profit 237.9; Advanced Purity Solutions 1,583.1 and 497.2 | Documentary Fact | `Q3 10-Q page:15` | Advanced Purity Solutions generates the larger share of segment profit and most of the profit growth (see the CP-1 segment table and C6) |
| Cost structure | Q3 2026 cost lines | Cost of sales 505.5, SG&A 136.5, ER&D 87.5, intangible amortization 45.6, on net sales of 1,005.7 | Documentary Fact | `Q3 10-Q page:5` | Cost of sales is 50.3% of sales (C3), against 56.5% a year earlier; operating leverage and lower depreciation drive the change |
| Cost structure | Supply risk | Certain filtration membranes, polymer resins, abrasive particles, specialty chemicals and petroleum coke come from a single source, a limited group of suppliers or a single country | Documentary Fact | `10-K page:22`, `page:31` | Supply interruption raises costs or limits shipments; re-qualification is slow |
| Capital spending | Level and direction | Capex of 124.0 in nine months 2026 against 241.2 in nine months 2025; 299.2 in FY2025; guidance of about 250.0 for 2026 given in the annual report; new facilities in Colorado Springs and Taiwan | Documentary Fact | `Q3 10-Q page:7`; `10-K page:9`, `page:82` | Capex fell year on year, which supports free cash flow; the growth plan implies it may rise again |
| Government support | CHIPS Act funding | Up to 77.0 under a December 2024 agreement for Colorado Springs, subject to milestones; 8.2 received through December 31, 2025 | Documentary Fact | `10-K page:9`, `page:138` | Funding is conditional and small against capex; it is not a debt substitute |
| Working capital | Build with sales | Trade receivables 625.2 against 458.7 and inventories 769.0 against 643.2 between December 31, 2025 and September 26, 2026; payables 262.4 against 171.5 | Documentary Fact | `Q3 10-Q page:4` | Growth absorbs working capital; a volume reversal would release it but the payables help is timing-based |
| Trade policy | Tariffs and refunds | Tariffs increased sourcing costs; 8.3 of IEEPA tariff refunds received in Q3 2026 for amounts incurred from April 2025 through February 2026 | Documentary Fact | `Q3 10-Q page:19`-`page:20`, `page:38` | The refund lifts 2026 reported gross margin and was excluded from non-GAAP results |
| Restructuring | Life Sciences Fluid Management | Second-quarter 2026 actions for the planned wind-down of the Life Sciences Fluid Management business, including a planned manufacturing facility closure; restructuring charges of 11.2 over nine months 2026 | Documentary Fact | `Q3 10-Q page:16` | Small exit that removes a non-core line; the size of the business is Not disclosed |

### Company profile

| Field | Value | Category | Locator |
| --- | --- | --- | --- |
| Registrant | Entegris, Inc., Delaware; Commission file number 001-32598; headquarters Billerica, Massachusetts | Documentary Fact | `Q3 10-Q page:1` |
| Listing | Common stock on the Nasdaq Stock Market, symbol ENTG; large accelerated filer | Documentary Fact | `Q3 10-Q page:1` |
| Country and sector | United States; the run context labels the sector "Plastics Products, NEC", while the filings describe semiconductor materials and process solutions (see conflict K1) | Documentary Fact for the business; the label is run context | `Q3 10-Q page:8`; context |
| Fiscal year | Calendar year ending December 31; quarters are 13 or 14 weeks ending on a Saturday, with 2026 quarters ending March 28, June 27, September 26 and December 31 | Documentary Fact | `Q3 10-Q page:18` |
| Size | About 7,700 employees at December 31, 2025, about 51% in North America; manufacturing in the U.S., Canada, China, Japan, Malaysia, Singapore, South Korea and Taiwan | Documentary Fact | `10-K page:22`, `page:21` |
| Shares and holders | 152.8 million shares outstanding at October 26, 2026; 907 shareholders of record at February 6, 2026 | Documentary Fact | `Q3 10-Q page:2`; `10-K page:65` |
| Ownership and control | No controlling holder, sponsor or parent is identified in the pack; holdings by institutions or insiders are not supplied | Insufficient Information | `10-K page:65`; context |
| Dividend and buyback | Quarterly dividend of $0.10 per share (61.1 declared in FY2025; next payable November 18, 2026); no publicly announced repurchase program and none executed in FY2025 | Documentary Fact | `10-K page:65`, `page:66`; `Q3 10-Q page:17` |
| Auditor and controls | KPMG LLP, Minneapolis, auditor since 1966, unqualified opinion on the FY2025 statements and on internal control over financial reporting; Q3 2026 disclosure controls concluded effective with no change in internal control | Documentary Fact | `10-K page:102`, `page:105`; `Q3 10-Q page:40` |
| Borrower, guarantors, restricted group | Issuer is the registrant; "certain subsidiaries" are parties to the indentures and guarantors under the credit agreement amendment; no list is supplied | Documentary Fact; list Insufficient Information | `10-K page:96`-`page:97` |
| Credit ratings | Not supplied; the annual report says ratings may change with earnings and payment performance but gives none | Insufficient Information | `10-K page:55`; context |
| Market capitalisation and equity value | Not supplied; the context fields are blank | Insufficient Information | context |

### Transaction summary and new debt issues

There is no sponsor transaction, acquisition, merger, recapitalisation or new debt issue in the supplied sources for 2026, and none is announced by the as-of date. The financing events in 2026 are two. First, on April 29, 2026 the company amended its senior secured revolving credit facility to raise commitments to $750.0 million from $575.0 million, extend the maturity to April 29, 2031 from July 6, 2027, and revise margins, commitment fees and certain negative covenants (`Q3 10-Q page:12`, `page:22`); the revised negative covenants are not described, and the amendment itself is not supplied. Second, the company repaid the term loans B in full during 2026 (50.0 in the first quarter, 200.0 in the second and 200.0 in the third, including a voluntary 25 on July 31, 2026), so that outstanding principal is now only fixed-rate notes of $3,295.0 million and an undrawn revolver (`Q1 10-Q page:11`; `Q2 10-Q page:12`, `page:17`; `Q3 10-Q page:11`, `page:12`). Cash flow statements for the nine months show repayments of $450.0 million and no proceeds from new long-term debt (`Q3 10-Q page:7`); the revolver was borrowed and repaid at 65.0 during the period. For use of proceeds and liquidity effect, the repayments were funded from operating cash flow of $606.0 million over nine months and reduced cash by little (cash $356.5 million against $360.4 million at December 31, 2025). Earlier history that shaped the balance sheet: the CMC Materials acquisition closed in July 2022 and was financed under the July 2022 credit agreement amendment and indenture supplements listed as exhibits (`10-K page:5`, `page:97`); debt payments of $848.3 million against proceeds of $224.5 million in FY2024 and payments of $300.0 million in FY2025 came after the asset sales listed in the timeline (`10-K page:108`). The nature of the FY2024 long-term debt proceeds is not described in the pack beyond a third amendment of the term loan facility in 2024 (`10-K page:76`, `page:98`). The dividend declared on October 14, 2026 ($0.10 per share, payable November 18, 2026) is a subsequent event after the quarter end (`Q3 10-Q page:17`). Management's Capital Markets Day on November 9, 2026 is a future event after the as-of date and no content from it is available (`Q3 release page:1`).

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| December 14, 2021 | Merger agreement to acquire CMC Materials, Inc. | Documentary Fact | `10-K page:96` |
| July 2022 | CMC Materials acquisition completed; credit agreement amended and restated and indentures supplemented on July 6, 2022 | Documentary Fact | `10-K page:5`, `page:97` |
| March 1, 2023 | Sale of QED Technologies International for $134.3 million | Documentary Fact | `10-K page:5` |
| June 5, 2023 | Alliance Agreement with MacDermid Enthone terminated; net proceeds about $191.2 million | Documentary Fact | `10-K page:5` |
| October 2, 2023 | Sale of the Electronic Chemicals business to Fujifilm for $675.3 million | Documentary Fact | `10-K page:5` |
| March 1, 2024 | Sale of the PIM business to SCF Partners for gross cash proceeds of $263.2 million plus up to $25.0 million earn-out tied to 2025 and 2026 performance | Documentary Fact | `10-K page:5` |
| March 28, 2024 | Amendment No. 3 to the credit agreement | Documentary Fact | `10-K page:98` |
| December 3, 2024 | CHIPS Act funding agreement for up to $77.0 million | Documentary Fact | `10-K page:138` |
| Fourth quarter 2025 | Sale of a small industrial specialty chemicals business; loss of $10.9 million | Documentary Fact | `10-K page:118` |
| January 2026 | Useful lives of property, plant and equipment extended; depreciation reduced by 55.6 in nine months 2026 | Documentary Fact | `Q3 10-Q page:9` |
| April 29, 2026 | Revolver amended: $750.0 million, maturity April 29, 2031 | Documentary Fact; subsequent event in the Q1 10-Q | `Q1 10-Q page:15`; `Q3 10-Q page:12` |
| Second quarter 2026 | Restructuring actions recorded for the planned wind-down of Life Sciences Fluid Management; equity investment impairment of 6.7 | Documentary Fact | `Q3 10-Q page:16`; `Q3 release page:9` |
| September 26, 2026 | Term loans B repaid in full | Documentary Fact | `Q3 10-Q page:12` |
| October 14, 2026 | Dividend of $0.10 per share declared; payable November 18, 2026 (subsequent event) | Documentary Fact | `Q3 10-Q page:17` |

### Governance, capital allocation and disclosure

| Behaviour or topic | Documented action | Category | Locator | Mechanic and limit |
| --- | --- | --- | --- | --- |
| Deleveraging | Term loan reduced from 750.0 at December 31, 2024 to nil at September 26, 2026; par debt from 4,045.0 to 3,295.0; management states an intention to continue paying down debt | Documentary Fact; intention is Management Language | `10-K page:10`, `page:120`; `Q3 10-Q page:11` | Supportive: cash applied to debt, lowering interest cost and refinancing exposure. Evidence quality High; the repayments are voluntary and the intention is not binding |
| Shareholder distributions | Dividend of $0.10 per share each quarter; 46.2 paid in nine months 2026; no repurchases in FY2025 and none shown in nine months 2026 cash flows | Documentary Fact | `10-K page:66`; `Q3 10-Q page:7` | Neutral: modest and steady relative to operating cash flow of 606.0; the board may change it and the credit agreement may restrict it (`10-K page:66`) |
| Creditor-adverse actions | No priming, uptier, drop-down, non-pro-rata exchange or collateral release appears in the pack | Insufficient Information | pack as a whole | Absence in summaries is not proof; executed documents are not supplied |
| Legal capacity | Incremental loans and commitments up to the greater of $1.1 billion or 100% of EBITDA, plus amounts under a secured net leverage test; the indentures carry limited covenants on secured debt, sale-leasebacks and restricted subsidiary debt | Documentary Fact | `10-K page:54`, `page:56` | Capacity to add secured debt is wide in principle; willingness is shown by repayments, feasibility by the leverage and liquidity in CP-1. The three are kept separate |
| Management and reporting continuity | Management agreements listed as exhibits include an offer letter (May 11, 2025), an executive chair agreement (July 30, 2025) and a separation agreement (January 19, 2026) with the officer who signed the annual report as chief financial officer; the Q1 2026 report was signed by the chief accounting officer as interim chief financial officer and the Q2 and Q3 2026 reports by a chief financial officer | Documentary Fact | `10-K page:100`; `Q1 10-Q page:36`; `Q2 10-Q page:39`; `Q3 10-Q page:41` | Issuer-level continuity: the Q3 10-Q cover confirms all required reports were filed in the preceding 12 months (`page:1`), controls were concluded effective with no change in internal control (`page:40`); no inference about individuals is made |
| Disclosure quality | Non-GAAP reconciliations to GAAP are given; the annual report's table captions say thousands for millions amounts, which the Q3 10-Q corrects | Documentary Fact | `Q3 10-Q page:9`, `page:38`; `10-K page:120` | Minor; handled in CP-1 |

### Credit translations

| Theme | Evidence | Risk mechanic | Credit implication | Counter-evidence or conflict |
| --- | --- | --- | --- | --- |
| Revenue durability | Unit-driven consumables, no platform above 3% of sales, but no long-term purchase commitments (`10-K page:10`, `page:18`) | Sales follow wafer volume and customer forecasts that can be cancelled, so revenue can fall quickly with fab utilisation | Debt service depends on volume holding; downturn protection comes from margin and low capex, not contract cover | FY2025 sales fell from 3,241.2 to 3,196.6 (CP-1) while Adjusted EBITDA margin held near 28%, which shows some resilience |
| Margin and cash-flow risk | Q3 2026 gross margin 49.7% against 43.5% a year earlier, helped by volume, lower depreciation and tariff refunds (`Q3 10-Q page:24`-`page:25`) | Part of the gain is accounting (useful lives) and one-off (refund), part is operating leverage | Run-rate margin is lower than the reported 2026 figure if volume normalises; Adjusted EBITDA is less affected than operating income | Adjusted EBITDA margin also rose to 30.2% in the quarter (CP-1) |
| Concentration | TSMC 16% and top ten 50% of FY2025 sales; Taiwan 26% of Q3 2026 sales (`10-K page:18`; `Q3 10-Q page:23`) | A single customer or region sets a large part of volume; export controls, tariffs or cross-strait tension hit several customers at once | Tail risk to cash flow that leverage ratios do not show | Customer share after FY2025 is Not supplied |
| Sponsor and ownership alignment | No sponsor or parent; steady dividends, no buyback, debt repayment (`10-K page:65`, `page:66`) | No documented extraction or related-party leakage; distributions are small against cash flow | Governance risk is not elevated on documented behaviour; capacity limits are untested | Holder detail and executed covenants are Not supplied |
| Key uncertainties | Covenant ratio, letters of credit, guarantor list, ratings, content of the November 9, 2026 Capital Markets Day | Unknown contract terms and market view of credit | Monitoring posture should be to confirm documents before relying on headroom | See gaps below |

### Conflicts and distinctions

| Ref | Spans | Locators | Effect |
| --- | --- | --- | --- |
| K1 | The run context labels the sector "Plastics Products, NEC"; the filings say "a leading supplier of critical advanced materials and process solutions for the semiconductor and other high-technology industries" | context; `Q3 10-Q page:8` | Logged, not reconciled. The filing description is used for the business; the label is a classification code in the run context |
| K2 | The annual report says the company expects to continue pursuing strategic acquisitions and partnerships; no acquisition, agreement or pending deal appears in 2026 sources | `10-K page:13`; sources as a whole | Acquisition appetite is not inferred from the statement; no transaction is assumed |
| K3 | The annual report's thousands captions on millions amounts against the Q3 10-Q correction | `10-K page:120`; `Q3 10-Q page:9` | Carried from the earlier modules; amounts are millions |

### Monitoring items the source set lacks

| Item | Status | Severity |
| --- | --- | --- |
| Debt schedule and maturity schedule | Available (CP-1) | Low |
| Add-back bridge | Available: non-GAAP reconciliation in the Q3 10-Q and releases | Low |
| Covenant compliance certificate and ratio | Not supplied | Medium |
| Executed credit agreement, April 2026 amendment and indentures | Not supplied | Medium |
| Letters of credit under the revolver | Not supplied | Medium |
| Guarantor and subsidiary list | Not supplied | Medium |
| Credit ratings and rating-agency commentary | Not supplied | Medium |
| Customer concentration after FY2025 | Not supplied | Low |

### Consumers

| Module | Readiness | Take from this handoff | Why it matters | Gap | Action |
| --- | --- | --- | --- | --- | --- |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Business risk: concentration, cyclical demand mix, unit-driven model, single-source inputs; governance: debt repayment and steady dividends; the absence of sponsor | Business risk is a required driver of the credit view next to the CP-1 financial risk | No covenant, rating, holder or contract evidence | State covenant headroom and recoveries as Not calculable or Not supplied; mark sponsor behaviour as Insufficient Information where relevant |
| CP-5 evidence trace review | READY_WITH_LIMITATIONS | Locators for every fact row and the category tags | Checks that claims rest on cited evidence | Management Language rows carry no independent check | Test the Management Language rows (unit-driven revenue, intention to repay debt, growth attribution) against their quoted spans |

## Calculations

| Ref | Calculation | Inputs | Result |
| --- | --- | --- | --- |
| C1 | Q3 2026 customer category shares | 589.8 / 1,005.7; 192.1 / 1,005.7; 103.5 / 1,005.7; 70.7 / 1,005.7; 49.6 / 1,005.7 | 58.6%; 19.1%; 10.3%; 7.0%; 4.9% |
| C2 | Year-on-year change, Q3 2026 | Equipment and Engineering 192.1 / 115.2 − 1; Fabs 589.8 / 494.5 − 1; total net sales 1,005.7 / 807.1 − 1 | +66.8%; +19.3%; +24.6% (the last as printed in the Q3 10-Q) |
| C3 | Cost of sales ratio, Q3 2026 and Q3 2025 | 505.5 / 1,005.7; 455.8 / 807.1 | 50.3%; 56.5% (both as printed in `Q3 10-Q page:22`) |
| C4 | Term loan and par debt change since December 31, 2024 | Term loan 750.0 at December 31, 2024 (`10-K page:120`) less nil at September 26, 2026; par debt 4,045.0 − 3,295.0 | 750.0 repaid; par debt down 750.0 |
| C5 | Nine-month 2026 repayments against operating cash flow | Debt repaid 450.0 and dividends 46.2 against operating cash flow 606.0 | 496.2 of debt repayment and dividends against 606.0 of operating cash flow |
| C6 | Nine-month segment profit change | Advanced Purity Solutions 497.2 − 322.2; Materials Solutions 237.9 − 212.7; total 175.0 + 25.2 | 175.0; 25.2; 200.2, so Advanced Purity Solutions is 87.4% of the increase |

All other figures above are copied from the cited locators or from CP-1; no other calculation is made.

## Gaps

| Ref | Gap | Why it matters | Action |
| --- | --- | --- | --- |
| B1 | Ownership detail: holders above reporting thresholds, insider holdings and any controlling holder are not supplied (only 907 holders of record). | Control rights and sponsor-like behaviour cannot be assessed; the conclusion of no sponsor rests on the absence of any mention. | Add the proxy statement or beneficial ownership data if ownership matters. |
| B2 | Credit ratings and agency commentary are not supplied. | Market view of credit and ratings-linked triggers are unknown. | Obtain agency reports, labelled as external. |
| B3 | Customer concentration is disclosed for FY2025 only; interim reports give categories and regions, not named customers. | The Q3 2026 growth mix may have changed concentration. | Treat FY2025 as the latest named-customer view. |
| B4 | Price realisation, backlog, and the size of the Life Sciences Fluid Management business are Not disclosed. | Margin durability and the effect of the exit cannot be sized. | None available in the pack. |
| B5 | The nature of the FY2024 long-term debt proceeds and the content of the revised revolver covenants are not described. | Capacity and history of financing actions are incomplete. | Obtain the Third Amendment and the April 2026 amendment. |
| B6 | Executed financing documents, covenant certificate, letters of credit and the guarantor list remain unsupplied (carried from CP-0 and CP-1). | Legal capacity, structural priority and availability cannot be tested. | As in the earlier modules. |
| B7 | The pack contains no information after October 29, 2026, so developments between that date and the November 5, 2026 cutoff are Not supplied. | Possible events in the final week are unknown. | None. |

## Next module

Pass to the fundamental credit synthesis and then the evidence trace review. The synthesis should use this handoff for business risk (concentration, cyclical equipment-linked demand, short revenue visibility, single-source inputs, trade exposure) and capital-allocation behaviour (repayment of the term loan, steady dividends, no repurchases, no documented creditor-adverse action), and CP-1 for financial risk and liquidity. It should not state covenant headroom, net revolver availability, a sponsor view, ratings or recovery outcomes, and should label Management Language rows as such. The evidence review should test the Management Language rows and the figures repeated from CP-1 against their sources and against each other.
