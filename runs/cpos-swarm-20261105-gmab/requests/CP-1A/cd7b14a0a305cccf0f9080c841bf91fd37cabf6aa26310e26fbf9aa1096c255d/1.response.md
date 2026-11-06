## Request

Module: CP-1A business and transaction context for GENMAB A/S (issuer id gmab), as of 2026-11-05 (cutoff 2026-11-05). Pathway: credit_snapshot. Reporting currency USD (millions unless stated). Current period Q3 2026 (nine months ended September 30, 2026); prior period FY2025. Creditor perspective: which transaction, business, ownership and operating facts matter most.

Perimeter: Genmab A/S, the Danish parent, and its consolidated subsidiaries (the Genmab Group). The run context names no sponsor, borrower distinct from the issuer, parent or guarantor; blank context fields are not treated as zero. Where the notes are issued by Genmab A/S with Genmab Finance LLC and subsidiary guarantors, that is stated as found and flagged as unresolved where the pack does not say.

Prohibited and not done: no peer ranking, no instrument recommendation, no recovery conclusion. Figures are taken from the accepted financial handoff or the sources; none is newly calculated unless shown in Calculations.

## Sources

Issuer sources relied on (exact names and sha256):

| Source name | sha256 | Role |
| --- | --- | --- |
| 20-F_2025-12-31_gmab-20251231_d2.htm.jsonl | 041104aadf76e2dd3c99b07f2a5c8ca0092780880cc53f8276cda7db55a72e43 | Business, collaborations, risk factors, Merus acquisition narrative, ownership, governance, exhibits list. Cited as 20-F. Filed annual report; financial statements incorporated by reference but not supplied. |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | 864b19bf237a4d5a6460638b8680b6339157a3234e843d8e76bb977e4dc1d4f8 | Latest operating, legal and transaction updates, borrowings and subsequent events. Cited as Q3 2026 report. Unaudited. |
| 6-K-EX-99.1_2026-05-07_genmabinterimreportq12026.htm.jsonl | 4ecbe1ab5be0468827b42bbf43fa8fbdbec0fdd369b4737a86f629cb84e67e45 | Q1 2026 context on covenants and borrowings. Cited as Q1 2026 report. |
| 6-K-EX-99.1_2025-11-06_genmabinterimreportq32025.htm.jsonl | 06978ddb790610f6f32c0187b617be9da7c780d7403fa742ff98ba9049d5f051 | Merus announcement terms and financing intent as of November 6, 2025. Cited as Q3 2025 report. |

Run settings (not issuer evidence): context sha256 f11f6ebfef20e70f4d6999b74c1449c3a4d8535f2ef28448cb9cbb9dc6331b4f.

Supplied handoffs:

| Module | sha256 | How used |
| --- | --- | --- |
| CP-0 | c518aa6f06b65ffcd0e072d73cfda5aff3a009b2e75d7807c6be29ffdbca6911 | Source readiness: READY_WITH_LIMITATIONS. Limits carried: credit agreement, indentures and audited annual report not supplied; no rating source; guarantor and co-issuer detail beyond exhibit titles not supplied; 2026 interim data unaudited. |
| CP-1 | 470d2d1ddbdc4449f689b20b3d5a9b49f6d69c93c24a1bf1e1eda3c8703c07f5 | Financial base: borrowings 4,992, cash 1,860, net debt 3,132 at September 30, 2026 (carrying values, unaudited); nine-month revenue 3,238 with royalties 2,699 and DARZALEX royalties 2,057; interest cover and EBITDA-based leverage as given there. One CP-1 calculation is corrected below (Term B margin saving). |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Genmab is a royalty-funded antibody developer that borrowed $5.5 billion to buy Merus, so creditors rely on DARZALEX and Kesimpta royalties while a pipeline asset matures. Ownership is dispersed and there are no dividends. | Medium | The credit agreement, indentures, coupons, maturities, guarantors, covenant levels and ratings are not in the pack, so the debt terms cannot be matched to the royalty horizon. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| DARZALEX royalties are limited in time: Genmab's daratumumab patents expire in 2029 in the US, 2031 in Europe and 2030 in Japan, and J&J may terminate on 150 days' notice. | The largest cash stream supporting debt service has a finite disclosed horizon, but debt maturities are not supplied, so overlap cannot be tested. | High |
| Merus was bought at $97 per share, about $8.0 billion, closed December 12, 2025, and financed with $5.5 billion of borrowings plus cash on hand. | Creditors now lend against a pre-revenue pipeline asset that anchors the asset base; repayment relies on royalty cash flow. | High |
| Debt comprises Term A and Term B secured loans, $1.5 billion secured notes, $1.0 billion unsecured notes and a $500 million revolver. | Seniority and security are partly visible, but guarantors, coupons, maturities and revolver availability are not supplied. | Medium |
| No holder exceeds 5.80%, no dividends were paid in three years, yet buybacks continued, with $96 million spent in nine months 2026. | No sponsor control or distribution leakage is evident, but covenant room for further distributions is unknown. | Medium |
| AbbVie, the epcoritamab co-development partner, is also the plaintiff in a trade secret case over Rina-S; no provision is recorded and no amount is stated. | Contingent liability is unsized and could strain a key partnership; outcome and timing are not disclosed. | Medium |

### Business and transaction view

Genmab A/S is a Danish, Nasdaq Copenhagen and Nasdaq-listed biotechnology company that earns most of its revenue from royalties on antibodies it created or enabled and sold by partners (J&J, Novartis, Amgen), and a growing share from its own co-commercialized products (EPKINLY/TEPKINLY with AbbVie, and Tivdak with Pfizer). In December 2025 it completed the cash acquisition of Merus, funded with a debt package that turned a net cash balance sheet into one with substantial secured and unsecured debt. The credit logic for a creditor is therefore a transfer of cash flow from a mature royalty stream, whose contractual horizon is disclosed and finite, to service debt incurred to buy a late-stage pipeline asset that does not yet produce revenue. Ownership is public and dispersed with no controlling holder, the issuer pays no dividends, and the debt documents restrict distributions, so sponsor-style extraction is not evident in the evidence supplied; the unrestricted capacity and covenant levels are not supplied, so that remains open. The binding source gaps are the executed debt documents and the audited annual report. This handoff is a context and transaction fact pack; it states no credit rating, no recovery outcome and no relative view.

### Company and operating model

| Area | Fact | Category | Source locator | Credit relevance |
| --- | --- | --- | --- | --- |
| Core activity | International biotechnology company with a pipeline of antibody-based products and product candidates for cancer and other serious diseases; priorities are epcoritamab, Rina-S and petosemtamab | Documentary Fact | 20-F page:67 | Revenue today is not from wholly owned launched products; pipeline outcomes drive future cash flow |
| Revenue model | Royalties (nine months 2026: 2,699 of 3,238 revenue), net product sales 410, reimbursement 35, milestones 31, collaboration revenue 53, license revenue 10 | Documentary Fact | Q3 2026 report page:39 | Royalty-led revenue is high margin but outside issuer control |
| Largest royalty | DARZALEX royalties 2,057 in nine months 2026 on J&J net sales; tiered royalties of 12% to 20%, reduced for Halozyme payments and in territories without patent coverage | Documentary Fact | Q3 2026 report page:40; 20-F page:90, page:91 | Concentration in one product and one licensee |
| DARZALEX royalty term | J&J's royalty obligation expires country by country on the later of 13 years after first sale or expiry of the last relevant Genmab patent; issued US, European and Japanese patents expire in 2029, 2031 and 2030 after extensions; J&J may terminate on 150 days' notice | Documentary Fact | 20-F page:91 | Defines a finite horizon for the largest cash stream |
| Other royalties | Kesimpta (Novartis) 408 in nine months 2026 at a 10% royalty on net sales for non-cancer treatment; TEPEZZA (Amgen) 93 at a mid-single-digit royalty; amivantamab 8% to 10%, teclistamab and talquetamab mid-single-digit | Documentary Fact | Q3 2026 report page:40; 20-F page:91, page:92 | Diversifies the royalty base beyond DARZALEX but at lower rates |
| Own products | EPKINLY/TEPKINLY co-developed with AbbVie; Genmab books US and Japan sales (381 of 491 global net sales in nine months 2026) and AbbVie receives profit share of 184 in cost of product sales; Tivdak co-developed with Pfizer and Genmab records 50% of US gross profit | Documentary Fact | Q3 2026 report page:2, page:40, page:23, page:21 | Profit sharing reduces the margin on own-product sales |
| Cost structure | Nine months 2026: cost of product sales 234, R&D 1,329, SG&A 567, acquisition and integration charges 87, amortization of acquired intangibles 35; adjusted operating expenses rose 27% | Documentary Fact | Q3 2026 report page:5, page:2 | Spend is discretionary but front-loaded ahead of 2027 launches |
| Capital spending and working capital | Investment in tangible and intangible assets is small (19 in nine months 2026); working capital absorbed 354 including accrual settlements; third-party manufacturers and raw materials | Documentary Fact | Q3 2026 report page:35, page:29; 20-F page:81 | Cash generation is not capex-constrained; manufacturing is outsourced apart from a new U.S. facility lease |
| Manufacturing footprint | Lease of a U.S. manufacturing facility commenced in nine months 2026 with a non-cancelable period of about 21 years | Documentary Fact | Q3 2026 report page:49 | Long-dated lease commitment beside debt; lease liabilities 206 |
| Employees | 3,244 employees at September 30, 2026 versus 2,681 a year earlier | Documentary Fact | Q3 2026 report page:32 | Growth in fixed commercial and R&D cost base |
| Pipeline status | Rina-S and petosemtamab wholly owned and in Phase 3; October 2026 topline results reported for both and for epcoritamab EPCORE DLBCL-2 | Documentary Fact | 20-F page:67; Q3 2026 report page:4 | Post-quarter events; regulatory submissions and launches planned for 2027 by management |
| Management view of pipeline | "supporting multiple regulatory submissions and potential launches in 2027" | Management Language | Q3 2026 report page:1 | Forward-looking; not adopted |
| Operating segments | Managed and operated as one business unit; no separate lines of business identified | Documentary Fact | Q3 2026 report page:39 | No segment debt or entity split |
| Counterparty dependence | J&J accounts for 2,169 of 3,238 revenue in nine months 2026 | Documentary Fact | Q3 2026 report page:39 | Partner credit and licence risk |

### Company profile

| Item | Detail | Source locator |
| --- | --- | --- |
| Legal name and form | Genmab A/S; a Danish public limited liability company (Aktieselskab); CVR no. 21023884 | 20-F page:65, page:66 |
| Incorporation and listing | Incorporated June 11, 1998; operations began February 1999; shares listed on Nasdaq Copenhagen and ADSs on the Nasdaq Global Select Market under GMAB | 20-F page:65, page:152 |
| Domicile and headquarters | Carl Jacobsens Vej 30, 2500 Valby, Denmark | 20-F page:1 |
| Sector and country (run context) | Pharmaceutical Preparations; Denmark | Run context (not issuer evidence) |
| Reporting basis | IFRS Accounting Standards (20-F); IAS 34 (interim); USD presentation since 2025, previously DKK | 20-F page:189; Q3 2026 report page:37 |
| Fiscal year end | December 31 | 20-F page:1 |
| Auditor | Deloitte Statsautoriseret Revisionspartnerselskab, auditor since 2024 | 20-F page:188 |
| Chief executive and chief financial officer | Jan van de Winkel (President and CEO); Anthony Pagano (Executive Vice President and CFO) | Q3 2026 report page:54 |
| Board | Five independent, one non-independent and three employee-elected members after the March 19, 2026 AGM | Q3 2026 report page:49 |
| Shares outstanding | 62,405,855 at September 30, 2026 | Q3 2026 report page:6 |
| Ownership | No controlling holder; BlackRock, Inc. 5.80% and Orbis Investment Management LTD. 5.80% (13G-based, as of the dates stated); directors and management as a group 1.27% | 20-F page:150, page:151 |
| Dividends | None paid in the last three financial years; credit agreement and indentures restrict dividends and other distributions | 20-F page:152 |
| Credit ratings | Not supplied: no rating source is in the pack | Gap |
| Sponsor, borrower, parent, guarantors (run context) | None named. Note issuers and guarantors: indenture parties are Genmab A/S, Genmab Finance LLC and "the guarantors named therein"; the guarantor list is not supplied | 20-F page:181 |
| Employees | 3,244 at September 30, 2026 | Q3 2026 report page:32 |

### Transaction summary and new debt issues

On September 29, 2025 Genmab entered into a transaction agreement to acquire all shares of Merus N.V., which owned petosemtamab, for $97 per share in an all-cash transaction with a transaction value of approximately $8.0 billion, not subject to a financing condition, to be funded from cash on hand and approximately $5.5 billion of non-convertible debt backed by a funding commitment from Morgan Stanley Senior Funding, Inc. (Q3 2025 report page:3, page:40). The same report set a management target of gross leverage below 3x within two years after closing and said the package included a meaningful portion of prepayable debt (page:3); the leverage definition is not supplied. A wholly owned subsidiary commenced the tender offer on October 21, 2025 (page:3). The transaction closed on December 12, 2025, earlier than the early-2026 closing then expected (20-F page:125; Q3 2025 report page:40). It was accounted for as an asset acquisition because substantially all of the fair value was concentrated in petosemtamab (Q3 2026 report page:39); the auditor's critical audit matter cites an acquisition cost of USD 8.017 billion (20-F page:187).

Financing: in December 2025 Genmab entered into a $1 billion Term Loan A Facility, a $2 billion Term Loan B Facility and a $500 million revolving credit facility, issued $1.5 billion principal amount of Senior Secured Notes and $1.0 billion principal amount of Senior Unsecured Notes (20-F page:126), and states it incurred borrowings of $5.5 billion and used cash on hand (Q3 2026 report page:6). The term loans and notes sum to $5.5 billion on the facility sizes, which is consistent with the revolver having been undrawn at closing; this is an Analyst Interpretation, because no supplied source states the revolver balance. The indenture is dated December 3, 2025 among Genmab A/S, Genmab Finance LLC, the guarantors named therein and Wilmington Trust, National Association as trustee and notes collateral agent, and a first supplemental indenture is dated January 28, 2026 (20-F page:180, page:181); their terms are not supplied. At September 30, 2026 borrowings carried at amortized cost were Term A Loans (secured), Term B Loans (secured), Secured Notes and Unsecured Notes of 4,992 in total (Q3 2026 report page:45; CP-1). Four interest rate swaps of 406 each convert part of the floating-rate debt to fixed rates between 3.3355% and 3.4885% against 3-month SOFR to 6/30/2028 (Q3 2026 report page:47). In June 2026 an amendment to the credit agreement reduced the Term B margin from 3.00% to 2.00%, with a modification gain of 23 (page:46); financial covenants are stated for the Term A Loans, with compliance stated at March 31, 2026 and September 30, 2026 and no levels given (Q1 2026 report page:35; Q3 2026 report page:46).

Status and subsequent events: all of the above were executed before the cutoff. After the quarter, October 2026 topline results were reported for three Phase 3 trials (Q3 2026 report page:4); Note 15 reports no events that could significantly affect the statements (page:52). No new debt issue after September 30, 2026 appears in the pack. Correction to the financial handoff: it estimated a Term B margin saving of about 19 a year on a nominal of 1,900, which is the nominal immediately after the June 2026 amendment (Q3 2026 report page:46); because 250 of Term B principal was repaid in nine months 2026 (page:45), the nominal outstanding at September 30, 2026 is not printed and is lower, so the saving is lower than that estimate. The 19 figure should be read as an upper bound at the amendment date.

### Transaction, ownership and governance fact register

| Ref | Fact | Category | Evidence quality | Locator | Verbatim span |
| --- | --- | --- | --- | --- | --- |
| F1 | Merus price and value | Documentary Fact | High | Q3 2026 report page:39 | for $97 per share in an all-cash transaction representing a transaction value of approximately $8.0 billion |
| F2 | Acquisition financing | Documentary Fact | High | Q3 2026 report page:6 | Genmab incurred borrowings of $5.5 billion and utilized cash on hand. |
| F3 | Facility and note sizes | Documentary Fact | High | 20-F page:126 | Genmab also issued $1.5 billion principal amount of Senior Secured Notes and $1.0 billion principal amount of Senior Unsecured Notes |
| F4 | Asset acquisition accounting | Documentary Fact | High | Q3 2026 report page:39 | The transaction was accounted for as an asset acquisition |
| F5 | Deleveraging target | Management Language | Medium | Q3 2025 report page:3 | target of gross leverage <3x within two years after the closing |
| F6 | Royalty horizon | Documentary Fact | High | 20-F page:91 | expire in 2029, 2031, and 2030, respectively |
| F7 | Licensee termination right | Documentary Fact | High | 20-F page:91 | J&J may fully or partially terminate the agreement at any time upon 150 days’ prior written notice to us. |
| F8 | Dividends | Documentary Fact | High | 20-F page:152 | have not paid out any dividends within the last three financial years |
| F9 | Distribution restrictions | Documentary Fact | High | 20-F page:152 | restrict our ability to make certain restricted payments |
| F10 | Maintenance covenants exist | Documentary Fact | High | 20-F page:65 | our credit agreement requires us to comply with certain financial maintenance covenants |
| F11 | Board composition | Documentary Fact | High | Q3 2026 report page:49 | five independent board members, one non-independent board member, and three employee-elected board members |
| F12 | Share buyback programme | Documentary Fact | High | Q3 2026 report page:44 | As announced on February 17, 2026, Genmab initiated a share buy-back program to honor our commitments under the RSU program. |
| F13 | Largest holders | Documentary Fact | High | 20-F page:150 | BlackRock, Inc.(1) 3,707,346 5.80% |
| F14 | AbbVie litigation | Documentary Fact | High | Q3 2026 report page:34 | AbbVie has now resumed its case in the district court which had been stayed during the ITC investigation. |
| F15 | Management on pipeline | Management Language | Medium | Q3 2026 report page:1 | supporting multiple regulatory submissions and potential launches in 2027 |
| F16 | Revolver existence | Documentary Fact | High | 20-F page:126 | a $500 million revolving credit facility |

### Governance and sponsor behaviour (issuer level)

Assessment: Neutral or Mixed, with Insufficient Information on distribution capacity. Evidence from documented actions only: no controlling shareholder and no sponsor (F13, run context); no dividends in three years (F8); no material related-party transactions (Q3 2026 report page:49); principal repayments of 288 in nine months 2026 (CP-1; Q3 2026 report page:35), which is Supportive of deleveraging; against that, continued share buybacks of 96 in nine months 2026 (F12; Q3 2026 report page:44) and two large acquisitions since 2024 (ProfoundBio in the second quarter of 2024 per Q3 2026 report page:41, and Merus), which does not by itself establish an appetite for further acquisitions. No creditor-adverse transaction such as priming, uptiering, drop-down or non-pro-rata exchange appears in the pack. Not supplied: restricted payment baskets, debt incurrence capacity and covenant certificates, which are in the executed documents. Evidence quality: High for the actions listed; Insufficient for covenant capacity. Evidence limits: this reads issuer behaviour only; it makes no statement about any individual.

### Credit translations

1. Revenue durability (Evidence, Risk Mechanic, Credit Implication). Evidence: F6 and F7 and nine-month DARZALEX royalties of 2,057 out of revenue of 3,238 (CP-1). Risk mechanic: royalties are earned country by country until the later of a fixed term after first sale or the last Genmab patent expiry, which the filing places in 2029 to 2031 for the issued daratumumab patents, and are reduced where biosimilars launch or there is no patent coverage; J&J can terminate on 150 days' notice but then Genmab gains rights. Credit implication: debt service in later years must increasingly come from epcoritamab, Rina-S and petosemtamab, not from DARZALEX royalties. Whether that matters depends on debt maturities, which are not supplied (gap G1). Management Language on 2027 launches is not adopted.
2. Asset base and recovery mechanics (no recovery conclusion). Evidence: F1, F4 and CP-1 figures: goodwill and intangibles 9,197 including acquired IPR&D 8,237 against total assets 12,936. Risk mechanic: collateral value for the secured debt, as reflected on the balance sheet, is dominated by a pre-revenue pipeline asset acquired at a price set in 2025 rather than by cash-generating assets. Credit implication: if the pipeline asset underperforms, balance-sheet cover for creditors falls without any change in royalty cash flows; the security package is not supplied, so lien coverage is Not assessable.
3. Concentration and partner risk. Evidence: J&J accounts for 2,169 of revenue (Q3 2026 report page:39); AbbVie is the epcoritamab co-development partner, receives profit share of 184 on EPKINLY (page:23) and is the plaintiff in the Rina-S case (F14). Risk mechanic: relationship friction with a profit-sharing partner could affect co-commercialization decisions; litigation unquantified with no provision. Credit implication: contingent liability and partnership risk are unsized; this is an open item, not an adverse conclusion.
4. Sponsor alignment. Evidence: no sponsor, dispersed ownership, no dividends, buybacks continuing. Risk mechanic: equity holders are public investors rather than a financial sponsor, so distribution decisions are governed by the board and by the restricted payment covenants. Credit implication: leakage risk is low on documented actions but capacity for buybacks under the covenants is unknown (gap G4).
5. Counter-evidence logged: the Merus value appears as both "approximately $8.0 billion" and "USD 8.017 billion" (conflict C1). It does not weaken these translations.

### Timeline

| Date | Event | Type | Source locator |
| --- | --- | --- | --- |
| June 11, 1998 | Incorporated in Denmark; operations from February 1999 | History | 20-F page:65 |
| 2012 | J&J daratumumab license agreement | Collaboration | 20-F page:90 |
| June 2020 | AbbVie collaboration for epcoritamab | Collaboration | 20-F page:87 |
| Second quarter 2024 | ProfoundBio acquisition | Acquisition | Q3 2026 report page:41 |
| September 29, 2025 | Merus transaction agreement | Transaction | Q3 2025 report page:40 |
| October 21, 2025 | Tender offer commenced | Transaction | Q3 2025 report page:3 |
| December 3, 2025 | Indenture for the new notes | Financing | 20-F page:181 |
| December 12, 2025 | Merus acquisition completed | Transaction | 20-F page:125 |
| December 2025 | Acasunlimab development discontinued | Pipeline | 20-F page:90 |
| January 28, 2026 | First supplemental indenture | Financing | 20-F page:181 |
| January and February 2026 | Four interest rate swaps entered | Hedging | Q3 2026 report page:47 |
| February 17, 2026 | 20-F signed; share buy-back programme announced | Reporting, capital allocation | 20-F page:185; Q3 2026 report page:44 |
| March 19, 2026 | Annual general meeting; board re-elected | Governance | Q3 2026 report page:49 |
| April 17, 2026 | Cancellation of 1,900,000 treasury shares completed | Capital allocation | Q3 2026 report page:45 |
| June 2026 | Term B margin reduced from 3.00% to 2.00% | Financing | Q3 2026 report page:46 |
| July 2026 | ITC final determination ended the AbbVie complaint investigation; district court case resumed | Legal | Q3 2026 report page:33, page:34 |
| July and September 2026 | Epcoritamab plus R2 approved in Europe and Japan for relapsed or refractory FL | Regulatory | Q3 2026 report page:11 |
| August 6, 2026 | 2026 financial guidance published, maintained November 5, 2026 | Guidance | Q3 2026 report page:6 |
| October 2026 (subsequent) | Topline results for EPCORE DLBCL-2, RAINFOL-02 and LiGeR-HN1 | Subsequent event | Q3 2026 report page:4 |

### Conflicts and consistency log

| ID | Conflict | Span A | Span B | Treatment |
| --- | --- | --- | --- | --- |
| C1 | Merus transaction size stated at two precisions | Q3 2026 report page:39: "approximately $8.0 billion" | 20-F page:187: "USD 8.017 billion" | Logged as found, not reconciled; quote both when used |
| C2 | Closing date versus earlier expectation | Q3 2025 report page:40: "anticipated to close by early in the first quarter of 2026" | 20-F page:125: "On December 12, 2025, we completed the Acquisition of Merus" | Timing difference, not a figure conflict; the completed date controls |
| C3 | Term B nominal used in the financial handoff | CP-1 used nominal 1,900 for the margin saving | Q3 2026 report page:45 shows Term B principal repaid of 250 in nine months 2026 | Corrected above; current Term B nominal not supplied |

### Consumer readiness

| Consumer | Readiness | What to take from this handoff | Gap and action |
| --- | --- | --- | --- |
| CP-2 | READY_WITH_LIMITATIONS | Business-risk basis: royalty horizon, concentration, asset base, sponsor behaviour, litigation | Confidence stays below High while debt documents, maturities, covenants and ratings are Not supplied; add the debt documents and Annual Report 2025 |
| CP-5 | READY_WITH_LIMITATIONS | Fact register F1 to F16 with verbatim spans and locators for tracing | Chunk-based page locators; text extraction only |

## Calculations

None newly calculated. Facts restated from the accepted financial handoff: borrowings 4,992; cash 1,860; net debt 3,132; nine-month revenue 3,238; royalties 2,699; DARZALEX royalties 2,057; goodwill and intangibles 9,197; acquired IPR&D 8,237; total assets 12,936. One arithmetic observation from facility sizes, labelled Analyst Interpretation: 1.0 billion Term Loan A Facility plus 2.0 billion Term Loan B Facility plus 1.5 billion Secured Notes plus 1.0 billion Unsecured Notes equals 5.5 billion, equal to the borrowings of $5.5 billion stated for the acquisition. No Term B nominal at September 30, 2026 is calculated: the timing of the 250 of nine-month Term B repayments relative to the June 2026 amendment is not stated.

## Gaps

| Gap | Severity | Affects | Action |
| --- | --- | --- | --- |
| G1: Debt maturity schedule, coupons, call protection, amortization, security package and guarantors not supplied (credit agreement, indentures, Note 4.8) | High | CP-2, CP-5 | Add executed documents. Cannot test royalty horizon against debt maturities. |
| G2: Revolver balance and availability not supplied | High | CP-2 | Not supplied; add Note 4.8 |
| G3: Credit ratings and rating agency views not supplied | Medium | CP-2 | Not supplied; external material to be labelled if added |
| G4: Covenant levels, definitions and restricted payment capacity not supplied | High | CP-2 | Not supplied; add executed documents |
| G5: Management's gross leverage target definition and measurement date not supplied | Medium | CP-2 | Not supplied |
| G6: Litigation exposure (AbbVie Rina-S, Chugai patents) unquantified, no provisions | Medium | CP-2 | Not supplied |
| G7: Milestone and commitment obligations (Note 5.3) and other annual-report notes not supplied | Medium | CP-2 | Add Annual Report 2025 |
| G8: Genmab Finance LLC role (co-issuer or finance subsidiary) and subsidiary guarantors not resolved | Medium | CP-2, CP-5 | Only exhibit titles and the term "the Issuers" in a risk factor (20-F page:65) |
| G9: Purchase price allocation and fee detail for Merus beyond headline figures (audited notes not supplied) | Low | CP-2 | Add Annual Report 2025 |
| G10: Text extraction only; no fidelity review | Low | all | Spot check key spans |

## Next module

Proceed to CP-2 (fundamental credit synthesis) and then CP-5 (evidence trace). Carry forward: the finite disclosed horizon for DARZALEX royalties (patents expiring 2029 US, 2031 Europe, 2030 Japan) against debt maturities that are Not supplied; the single-asset concentration of the Merus acquisition; the sponsor-free, dividend-free governance picture with continuing buybacks; AbbVie as both partner and litigant; and the correction that the Term B margin saving is an upper bound. Next evidence action: add Annual Report 2025 (Exhibit 15.3), the credit agreement and both indentures.
