## Request

Issuer: BIOMARIN PHARMACEUTICAL INC (issuer id bmrn; Nasdaq ticker BMRN; Delaware registrant, SEC file number 000-26727). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. The financial statements are stated in thousands of US dollars and the MD&A and releases in millions (10-Q Q3 2026 page:8, page:45). Current period: Q3 2026 (quarter ended 2026-09-30). Prior period named by the context: FY2025.

Question for this module: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize, reconcile or calculate figures. Arithmetic below is limited to tie-outs that test source consistency.

The context file holds run settings and is not issuer evidence. Its deal terms, quotes, ratings, peers, precedents and research questions are empty, and it names no borrower, parent, guarantor or sponsor. Those blanks are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

Each file is a JSONL text extraction of an SEC filing or exhibit. The locator `page:N` is the extraction chunk, not the printed page. The sha256 below is the pinned file hash. Each file also prints a different hash for its underlying htm document in its first line; that one is not used here.

| Source name | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_bmrn-20251231.htm.jsonl | ea07c0b0ced62ce928418e33e7850bb4f7657797e8c0bf5f5000905677fe1e06 | Audited annual report, Form 10-K, 226 chunks; signed 2026-02-26 (page:177); auditor report KPMG LLP (page:178); filed statements control their facts | Fiscal year ended 2025-12-31; pre-Amicus perimeter; debt was the 2027 Notes only (page:99) |
| 10-Q_2026-03-31_bmrn-20260331.htm.jsonl | 2a99ceccd25eef82b99d8805175210aaa89ec2399f72c136d49401e8ef68101d | Unaudited quarterly report, Form 10-Q, 112 chunks; signed 2026-05-05 (page:112) | Q1 2026 (quarter ended 2026-03-31); 2034 Notes proceeds held in escrow, Amicus not yet closed (page:13, page:17) |
| 10-Q_2026-06-30_bmrn-20260630.htm.jsonl | ab3790f631c592e337d10380a75780f5e20242f4c9bb7ba84f7627e0f0826177 | Unaudited quarterly report, Form 10-Q, 120 chunks; signed 2026-08-06 (page:120) | Q2 2026 and six months; first report including Amicus (from 2026-04-27) |
| 10-Q_2026-09-30_bmrn-20260930.htm.jsonl | d37c2b4920de3198d70881c8f1da80a4e23e61a15cd3750a74ed566c3cf812ae | Unaudited quarterly report, Form 10-Q, 125 chunks; signed 2026-11-03 (page:125); latest filed statements | Q3 2026 and nine months; includes Amicus from 2026-04-27 and Alesta from 2026-08-31 (page:14, page:18) |
| EX-99.1_2026-05-04_earningsrelease-4may26ex991.htm.jsonl | 4342224974b87cfa461fd3f7cf30a3f9e47704c85d4929187beb8b8d81373433 | Earnings release exhibit, 11 chunks; management attribution, supporting claims only | Q1 2026; dated 2026-05-04 (page:1) |
| EX-99.1_2026-08-06_earningsrelease-6aug26ex991.htm.jsonl | 5716fe1e56e2ba465f10bd50a733773a00cfbe4f0196fc4b254c96006e5e867a | Earnings release exhibit, 13 chunks; supporting claims only | Q2 2026; dated 2026-08-06 (page:1) |
| EX-99.1_2026-11-02_earningsrelease-2nov26ex991.htm.jsonl | 9fad7cb025a49338e77589bbc1ee8b206ca16d3ad7a77a9450a90d585d60fed5 | Earnings release exhibit, 13 chunks; supporting claims only | Q3 2026; dated 2026-11-02 (page:1) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 91b63adad7def6728b9cd684c48c1a1c49d1718a8dc5d8773455a7dcffcc69fa | Run settings only; not issuer evidence |

### Supplied handoffs

None. CP-0 is the first module of this run, so the handoff set is empty.

### Ignored file

_retrieval.json sits in the pack folder and is not a pinned source. It is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The annual report, three quarterly reports and three earnings releases are enough to start the financial base, debt picture and business context. The April 2026 Amicus acquisition changes the company's perimeter and debt, so earlier periods are not comparable. | Medium | The credit agreement, indentures and covenant calculations are not in the pack, and no combined full-year or last-twelve-months base is supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The Amicus acquisition closed in April 2026 and was financed with new secured term loans, a new senior unsecured note issue and cash. The annual report precedes all of it. | Debt and interest figures in the annual report cannot be used as the current capital structure. | High |
| The latest quarterly report prints each debt instrument, balance, maturity and fair value, plus a revolver with nothing drawn. | Debt can be set out instrument by instrument from filed statements. | High |
| Covenant levels are described and compliance is stated, but the ratios and their definitions are not printed. | Covenant headroom cannot be measured from the pack, only the stated compliance. | High |
| Guarantor names, security packages and the executed legal documents are not supplied. | Structural ranking and guarantee coverage rest on filing summaries and stay a gap. | High |
| Only pro forma revenue and net loss are given, for three and nine months, and the purchase price allocation is preliminary. | A combined full-year or last-twelve-months earnings base is not available without derivation. | Medium |

### Readiness view

The effective source set supports the requested work with limitations. All four requested consumers are assessed as READY_WITH_LIMITATIONS; none is CONDITIONAL and none is BLOCKED. The audited annual report, the three quarterly reports and the three earnings releases cover the periods the context names, in the reporting currency, up to the evidence cutoff, and the latest report was signed before the as-of date. The binding limitations are six. First, the perimeter changes in 2026: Amicus Therapeutics, Inc. is consolidated only from 2026-04-27 and Alesta Therapeutics B.V. from 2026-08-31, so the FY2025 annual base is a different business and a different capital structure from Q3 2026. Second, no executed legal document is in the pack, so covenant definitions, guarantor lists and security terms rest on filing summaries. Third, the reported covenant ratios are not printed, only a statement of compliance. Fourth, the purchase price allocation is preliminary and pro forma figures cover revenue and net loss only. Fifth, prior-period research and development was reclassified in 2026 to present acquired in-process research and development separately. Sixth, no fidelity review of the text extraction has been done and no image or chart content exists to inspect. None of these blocks a consumer from starting, and each carries forward as a stated limit.

### Source-by-source assessment

All seven sources identify BioMarin Pharmaceutical Inc. as the registrant or the announcing company (page:1 of each). No source is blocked, draft, unsigned or a duplicate of another. The quarterly statements are unaudited. The filed 10-K and 10-Qs control their own facts. The three releases are management claims and must not override the filings.

| Source | What it supports | Limit |
| --- | --- | --- |
| 10-K FY2025 | Audited statements (auditor report page:178-180); results of operations in millions (page:149, page:154); debt risk factor stating the 2027 Notes were all the debt at 2025-12-31 and the 2024 unsecured revolver existed (page:99) | Pre-Amicus; the 2034 Notes and the 2026 Credit Agreement came after year end |
| 10-Q Q1 2026 | Quarter ended 2026-03-31; 2034 Notes issued into escrow and restricted cash equivalents (page:13, page:17); the 2026 Revolving Facility (page:39); exhibit list (page:111) | Amicus had not closed; the balance sheet reflects escrow, not the final structure |
| 10-Q Q2 2026 | First statements with Amicus; June 2026 debt table with the term loans at original balances (page:20); termination of the 2024 revolver (page:43); segment table (page:24); exhibits including the credit agreement and supplemental indenture (page:118) | Superseded in balances by the Q3 report |
| 10-Q Q3 2026 | Latest balance sheet (page:8-9), cash flow (page:10), Note 2 acquisitions (page:14-18), Note 7 debt (page:22-25), segment note (page:27), revenue by product (page:28), restructuring (page:30), subsequent events (page:34), liquidity and covenants (page:45-50), exhibits (page:123-124) | Covenant ratios and legal documents not printed |
| EX-99.1 2026-05-04 | Q1 highlights and increased FY2026 revenue guidance (page:1) | Management claims; guidance superseded |
| EX-99.1 2026-08-06 | Q2 highlights, raised guidance (page:1) | Management claims; guidance superseded |
| EX-99.1 2026-11-02 | Q3 highlights, updated guidance, Ascendis settlement, synergy statement (page:1, page:3); non-GAAP tables (page:4); statement that forward non-GAAP guidance has no GAAP reconciliation (page:5) | Management claims; non-GAAP |

### Entity and perimeter

The registrant and reporting entity is BioMarin Pharmaceutical Inc. and its wholly owned subsidiaries, consolidated (Q3 10-Q page:11). The 2026 Credit Agreement names BioMarin Pharmaceutical Inc. as Borrower with Citibank, N.A. as administrative agent and collateral agent (Q2 10-Q page:118). The Q3 10-Q says obligations under it are "guaranteed by certain of our subsidiaries and secured by first-priority liens on substantially all of our and the guarantors' assets" (page:50), but no source names the guarantors. The exhibit lists show a supplemental indenture dated 2026-04-27 among the Company, "certain guarantors" and the trustee (Q2 10-Q page:118; Q1 10-Q page:111, which lists it after the 2026-02-12 indenture). The debt note describes the 2034 Notes as "senior unsecured" and does not state who guarantees them (Q3 10-Q page:25). Whether the supplemental indenture added guarantors to the 2034 Notes is therefore an inference the pack does not settle, and it stays a gap. Amicus became a wholly owned subsidiary at closing (page:14). The 2027 Notes are described as senior subordinated convertible notes (page:22). The issuer-versus-guarantor map and the ranking between the secured term loans, the unsecured 2034 Notes and the subordinated convertible notes are not resolved here. The context names no borrower, parent or guarantor.

### Period basis and version relationships

The perimeter changes across the pack. The 10-K covers FY2025 before any of the 2026 financing or acquisitions. Q1 2026 predates the Amicus close of 2026-04-27 (page:14), so Q1 carries the escrowed 2034 Notes proceeds and the bridge commitment (Q1 10-Q page:13, page:17), not the term loans. From Q2 2026 the statements include Amicus. Amicus contributed total revenue of 336,422 thousand and a net loss of 239,383 thousand from 2026-04-27 to 2026-09-30 (Q3 10-Q page:17). The Alesta acquisition closed on 2026-08-31 for total consideration of 303.4 million, with regulatory and sales milestones also provided for (page:18).

Pro forma results as if the Amicus acquisition occurred on 2025-01-01 are given only for the three and nine months ended 2026-09-30 and 2025-09-30, for revenue and net loss (page:17). No pro forma FY2025 figure, no pro forma Adjusted EBITDA and no pro forma interest are supplied. A last-twelve-months figure on the combined perimeter cannot be built from the pack without derivation, which is downstream work. The purchase price allocation is stated as preliminary (page:11, page:15).

Presentation changed in 2026: acquired in-process research and development, previously inside research and development, is now a separate line, and prior-period amounts were reclassified, including 221.0 million for the three and nine months ended 2025-09-30 (Q3 10-Q page:11). The FY2025 10-K shows research and development of 921.9 million on the older presentation (page:149). The 10-K and the Q3 report therefore present these lines on different bases.

The company reports one business segment (Q3 10-Q page:27), so no segment profit table exists. Revenue is disaggregated by product (page:28). GALAFOLD and POMBILITI + OPFOLDA revenue begins on 2026-04-27 (page:28).

The Q3 10-Q was signed 2026-11-03 (page:125) and the Q3 release is dated 2026-11-02 (page:1). Nothing dated after 2026-11-05 is relied on. Shares outstanding are stated as of 2026-10-26 (page:2).

### Debt and liquidity evidence present

The Q3 10-Q debt note (page:22) gives principal at 2026-09-30, in thousands: 1.25% senior subordinated convertible notes due May 2027, 600,000; 5.5% senior unsecured notes due February 2034, 850,000; Term Loan A, 790,000; Term Loan B, 1,995,000; total 4,235,000; unamortized discount and deferred offering costs (61,309); total debt, net 4,173,691. Fair values (Level 1 except Term Loan A at Level 2) total 4,167,757 (page:22-23). The balance sheet splits the net debt into a current portion of 658,717 and long-term debt of 3,514,974 (page:9). The 2026 Credit Agreement provides a 800.0 million senior secured Term Loan A, a 2.0 billion senior secured Term Loan B and a 600.0 million senior secured revolver (page:23). Term Loan A matures 2031-04-27 with quarterly repayments of 1.25% of original principal; Term Loan B matures 2033-04-27 with quarterly repayments of 0.25% of original principal (page:24). The revolver matures 2031-04-27, with no borrowings outstanding and the full 600.0 million available subject to compliance (page:25, page:48). The 2034 Notes pay interest semi-annually on February 15 and August 15 (page:25). The bridge commitment of up to approximately 3.7 billion was reduced to 2.8 billion on the notes issue and then to zero on entry into the term facilities (page:25). The 2024 unsecured 600.0 million revolver was terminated in April 2026 (Q2 10-Q page:43). Interest margins and the leverage-based step-downs on Term Loan A are described on page:49. Maintenance covenants on Term Loan A and the revolver are a maximum Total Net Leverage Ratio of 3.50 to 1.00, with a temporary increase to 4.00 to 1.00 in connection with certain acquisitions, and a minimum Interest Coverage Ratio of 3.00 to 1.00, with compliance stated at 2026-09-30 (page:50). Cash and cash equivalents are 736,007 thousand, with no short-term or long-term investments (page:8, page:45). Nine-month cash paid for interest is 66,048 thousand and for income taxes 74,378 thousand (page:10). Interest expense on debt for the nine months includes a bridge commitment fee of 22,813 thousand (page:23).

The pack does not give: the covenant calculations or reported ratios; the definition of Total Net Leverage Ratio, Interest Coverage Ratio or the temporary acquisition step-up beyond the summary; the guarantor names; the 2027 Notes conversion terms in the Q3 report (it refers to the 10-K, page:23); a combined last-twelve-months earnings base; or any credit rating. The context lists no ratings or quotes. A search of all seven pinned sources for rating agency names and credit rating terms found no rating of BioMarin or its debt; the only hits are the 10-K policy on counterparty ratings (10-K page:168-169).

### Quarter, subsequent events and contingencies

Evidence present for the latest quarter and the period after it: Amicus integration restructuring, with severance of 29,478 thousand in Q3 and 82,618 thousand for nine months (page:30); acquired IPR&D expense of 287,685 thousand in Q3 (page:8); the Alesta acquisition (page:18); the Ascendis settlement of 2026-08-30 with Ascendis to pay royalties of 20% of net sales of Yuviwel in the United States and 18% in the European Union, Brazil and South Korea until May 2030, per the Q3 release (page:3); the settlement agreement is listed as an exhibit to the Q3 10-Q (page:124) but its text is not in the pack; an October 2026 exclusive license with GC Biopharma Corp. and Hanmi Pharm Co., Ltd. for BMN 450, with an upfront payment of 70.0 million expected in Q4 2026 acquired IPR&D expense and up to a further 405.0 million of milestones plus royalties (page:34); a PDUFA action date of 2027-05-30 for VOXZOGO in hypochondroplasia (Q3 release page:1); and management's statement that the full-year guidance was updated for order timing and two acquired IPR&D charges (page:1). The company discontinued marketing of ROCTAVIAN (Q3 release page:5). The 10-Q states management found no other subsequent events requiring recognition or disclosure (page:12). No legal-proceedings dollar exposure is assessed here; downstream modules must read the contingencies note. The 2027-05-30 date and the 2027 note maturity are future dates stated as scheduled, not facts. No event dated after 2026-11-05 is relied on.

### Consumer assessment

| Consumer | Evidence demand | Status | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial base | Discrete quarters, annual base, quarter versus year-to-date, products, add-backs, facility-level debt, cash interest and taxes, business narrative | READY_WITH_LIMITATIONS | FY2025 is pre-Amicus; Q1 2026 is pre-close; pro forma covers revenue and net loss only; IPR&D reclassified in 2026; units differ between statements (thousands) and MD&A (millions); non-GAAP figures are management claims; SOURCE_SUFFICIENCY_ONLY, CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED |
| CP-1A business and transaction context | Business, ownership, transaction and history facts | READY_WITH_LIMITATIONS | Merger agreement, credit agreement, indentures and Ascendis settlement agreement are not supplied, only filing and release descriptions; context has no sponsor or deal terms; preliminary purchase price allocation |
| CP-2 fundamental synthesis | Settled upstream registers plus filings | READY_WITH_LIMITATIONS | Covenant calculations, guarantor map, security detail and ratings not supplied; combined earnings base not supplied; ranking among instruments unresolved |
| CP-5 evidence trace | Citations that resolve in pinned sources | READY_WITH_LIMITATIONS | Depends on page-chunk locators; extraction fidelity not reviewed |

Missing downstream analytical handoffs are not treated as source conditions. The dependency planner sequences them.

### Extraction status and fidelity

Every source was retrieved as text chunks and read by search and targeted page reads. Tables arrived as flattened text; column headers were checked against the period labels printed in each table. The releases are text only and no image, chart or slide content exists in the pack. A successful extraction is not a fidelity review of every table, and none is claimed. The pack holds earnings releases and no investor presentation or transcript; no presentation coverage is claimed.

## Calculations

These are source tie-outs only, in thousands of USD unless stated. No figure is normalized.

| Check | Inputs and locator | Result |
| --- | --- | --- |
| Debt principal adds to total | 600,000 + 850,000 + 790,000 + 1,995,000 (Q3 10-Q page:22) | 4,235,000, equal to the printed total |
| Net debt ties to the balance sheet | 4,235,000 - 61,309 (page:22); 658,717 + 3,514,974 (page:9) | 4,173,691 both ways, equal |
| Fair values add to total | 585,884 + 792,872 + 789,013 + 1,999,988 (page:22) | 4,167,757, equal to the printed total |
| Term loan repayments tie to cash flow | Term Loan A 800,000 - 790,000 = 10,000; Term Loan B 2,000,000 - 1,995,000 = 5,000 (Q2 10-Q page:20; Q3 10-Q page:22); repayments of borrowings (15,000) (Q3 10-Q page:10) | 15,000, equal; consistent with 1.25% of 800,000 and 0.25% of 2,000,000 per quarter (page:24) |
| Current debt is consistent with stated amortization | 600,000 (2027 Notes) + 4 x 10,000 + 4 x 5,000 = 660,000 before discount, against current portion 658,717 (page:9, page:22, page:24) | Consistent within the unallocated discount of 1,283; this is an inference, not a printed figure |
| Aggregate debt rise is as stated | 600,000 + 850,000 = 1,450,000 at 2026-03-31 versus 4,235,000 at 2026-09-30; filing says approximately 1.5 billion rising to approximately 4.2 billion (page:47) | Consistent |
| Total consideration adds up | 4,563,463 + 142,636 + 62,946 + 121,596 + 432,920 (page:14) | 5,323,561, equal to the printed total and to "$5.3 billion" |
| Revenue by product adds to total | Q3: 1,013,080 + 11,566; nine months: 2,757,551 + 23,011 (page:28) | 1,024,646 and 2,780,562, equal to the income statement (page:8) |
| Q1 revenue by difference | Six months 1,755,916 - Q2 989,708 (Q2 10-Q page:24) | 766,208, consistent with "$766 million" in the Q1 release (page:1) |
| Nine months from quarters | 1,755,916 + 1,024,646 (Q2 10-Q page:24; Q3 10-Q page:8) | 2,780,562, equal to the nine-month total |
| Q3 pro forma equals reported | Pro forma Q3 2026 revenue 1,024,646 (page:17) versus reported 1,024,646 (page:8) | Equal, as Amicus was owned for the whole quarter |
| Release growth claims | 1,024,646 / 776,133 (page:8) | About 32 percent, matches the Q3 release headline (page:1) |
| Cash ties between sections | 736,007 thousand (page:8, page:10) versus 736.0 million (page:45) | Equal after the unit change |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed 2026 Credit Agreement, 2034 Notes indenture, supplemental indenture and 2027 Notes indenture are not in the pack | High | CP-1, CP-1A, CP-2 | Add the exhibits; until then use only filing summaries and name that limit |
| Reported Total Net Leverage Ratio and Interest Coverage Ratio are not printed; only compliance is stated (Q3 10-Q page:50) | High | CP-2 | Add the compliance certificate or use only the stated test levels without headroom |
| Guarantor names and the guarantee status of the 2034 Notes are not stated (page:25, page:50) | Medium | CP-1A, CP-2 | Add the supplemental indenture or a subsidiary list |
| No pro forma FY2025 or last-twelve-months combined earnings, interest or Adjusted EBITDA (page:17) | High | CP-1, CP-2 | Derive downstream from reported quarters and label as derived, or obtain a pro forma filing |
| Purchase price allocation is preliminary (page:11, page:15) | Medium | CP-1, CP-1A | Carry as provisional |
| Prior-period IPR&D reclassified to a separate line (page:11) | Medium | CP-1 | Use the Q3 presentation for 2025 comparatives; the 10-K lines differ |
| Credit ratings, bond and loan quotes and peer data are not supplied; the context fields are empty | Medium | CP-2 | Supply or mark not supplied |
| Merger agreement, Alesta purchase agreement and Ascendis settlement agreement are exhibits incorporated by reference or filed with the 10-Q but not in the pack text (page:123-124) | Low | CP-1A | Add if terms are needed |
| Conversion terms of the 2027 Notes are in the 10-K note, not the Q3 report (page:23) | Low | CP-1, CP-2 | Read the 10-K debt note downstream |
| Extraction fidelity not reviewed; no presentation or transcript in the pack | Low | CP-5 | State the limit |
| Non-GAAP measures and guidance in the releases are management claims without a GAAP reconciliation for forward figures (Q3 release page:5) | Low | CP-1 | Prefer filed figures; attribute non-GAAP |

## Next module

Proceed to CP-1 (financial base) with the status READY_WITH_LIMITATIONS, then CP-1A, CP-2 and CP-5 in the order the dependency planner sets. CP-1 must open the Q3 10-Q debt note (page:22-25), liquidity and covenant section (page:45-50), cash flow (page:10) and acquisition note (page:14-18), keep the 2026 perimeter break explicit, label any derived last-twelve-months figure as derived, carry the covenant and guarantor gaps forward, and not treat the FY2025 debt as the current structure. The next evidence action is to add the executed credit agreement and indentures if downstream work needs guarantee, security or covenant-definition detail.
