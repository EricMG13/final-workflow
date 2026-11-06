# CP-0 source readiness: GRAY MEDIA, INC (gtn)

## Request

Issuer: GRAY MEDIA, INC (ticker GTN, NYSE-listed Georgia corporation, Commission File Number 1-13796). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot, case kind public, run type research. Reporting currency per the run context: USD. Current period per the run context: q2-2026 (quarter ended June 30, 2026). Prior period: fy-2025 (year ended December 31, 2025).

Question answered by this handoff: can the pinned source set support the requested work, and what remains blocked. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize, reconcile or calculate figures.

Requested consumers, in run order: CP-1 (financial extraction), CP-1A (business and transaction context), CP-2 (fundamental credit synthesis) and CP-5 (evidence trace validator). The report sections selected for the minimum set are key findings, company operating model, model chart strip, financial and credit metrics, strengths and weaknesses, company profile and transaction summary.

The run context supplies no deal terms, no market quotes, no ratings, no peers, no valuation inputs, no management bridge, no prior case and no portfolio workbook, and it states legal documents as "none". Blank context values (borrower, parent, guarantors, sponsor, market capitalization, net debt, enterprise value) are not treated as zero or as evidence. The context is a user setting, not issuer evidence.

## Sources

### Issuer sources relied on

All seven issuer sources are text extractions (one JSON line per source chunk, cited here as `page:N`, which is the chunk number and not the printed page). The sha256 values below are those of the pinned `.jsonl` files named by the run. The `page:1` text of each file also states a hash of the original HTML filing; that hash is a different value and is not the pin used here.

| Label | Exact source name | sha256 (pinned) | Chunks |
| --- | --- | --- | --- |
| S-10K | 10-K_2025-12-31_gtn20251231_10k.htm.jsonl | 88cd2be27d00e9908e881a07fffdbfb7e9fbcb182cd4daa7213df1b4b5f00737 | 124 |
| S-Q3-25 | 10-Q_2025-09-30_gtn20250930_10q.htm.jsonl | b62445e5fe4a163fa362c47bf83e36bde2a987867496619de6fe27a40edfa171 | 45 |
| S-Q1-26 | 10-Q_2026-03-31_gtn20260331_10q.htm.jsonl | 3356f048b1cdb10c04c5b80b0d02babf79237e5dc24d851924643abb820dcebd | 34 |
| S-Q2-26 | 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | e96d90052b60b94fa2a12b7f9024364ed7aff9961690c651cc002284f695a02b | 41 |
| S-R-Feb | EX-99.1_2026-02-26_ex_924265.htm.jsonl | 178b7bc5710105291e494cc784bd65c8c9bce375e1552cc63408e1853ff6a993 | 12 |
| S-R-May | EX-99.1_2026-05-07_ex_956963.htm.jsonl | b04f43ebe7b79436fed34dc07bcf8f9f9fb0c9fac32a39299a3e02ac7ae325d8 | 11 |
| S-R-Aug | EX-99.1_2026-08-07_ex_998938.htm.jsonl | 1120ddd52748c4fbbc1c17f2a7297d8e7f38db5b861bb6f5b9064b68dbae4a0d | 13 |

### Other inputs

| Input | sha256 | Role |
| --- | --- | --- |
| context (43196-gray-media-inc-gtn-gtn-a.json) | 457b491e723cfaa80de6921ac6aa99b1d24251f7cfebd35fd33b60ef8d3cb70e | User settings for the run; not issuer evidence |

The pack folder also holds `_retrieval.json`, which the launcher ignored; it is retrieval metadata, not a source, and nothing here relies on it.

### Handoffs supplied

None. CP-0 is the first module in the run, so the request carries no upstream handoff. No handoff hash is listed because none exists.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings and earnings releases are sufficient to run the requested snapshot work with bounded limitations. Evidence ends with the August 2026 second-quarter release, and no governing debt documents are supplied. | Medium | No credit agreement or indentures and no third-quarter 2026 report, so covenant terms and post-June liquidity cannot be confirmed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report, three quarterly reports and three earnings releases cover statements, debt by instrument, covenant ratios and liquidity in USD millions. | Supports a reported-fact snapshot of the debt stack, liquidity and covenant ratios from primary filings. | High |
| Adjusted EBITDA appears only in the earnings releases, not in any filing; the covenant earnings denominator appears in both. | Earnings-based metrics rest on management-defined figures that no filed schedule corroborates. | Medium |
| Credit agreement, indentures and receivables purchase agreement are not supplied, and the filings describe a March 2026 amendment and restatement of the credit agreement. | Covenant triggers and guarantor terms rest on issuer summaries rather than executed text. | Medium |
| A July 2026 debt repurchase was funded partly by revolver borrowings, and the amount drawn is not disclosed. | June 2026 liquidity does not show the position after the repurchase. | Medium |
| The latest evidence is the August 2026 release; the quarter ended September 2026 is not covered at the November as-of date. | Current leverage and liquidity may differ from the last reported position. | High |

### Readiness view

Source sufficiency is READY_WITH_LIMITATIONS for all four selected consumers. No consumer is CONDITIONAL or BLOCKED: the issuer identity is unambiguous, every source carries usable located content, and no extraction failure was found. The limitations are bounded and are carried into each consumer below. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This handoff does not assert normalized quarters, reconciliation or downstream input acceptance. A successful text extraction is not a fidelity review, and no fidelity review of tables or figures was done here beyond the spot checks cited.

| Consumer | Source readiness | Located evidence | Carried limitations |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 statements and debt note (S-10K page:72 to page:76, page:91 to page:95); interim statements for Q3 2025, Q1 2026 and Q2 2026 (S-Q3-25 page:2, S-Q1-26 page:2, S-Q2-26 page:2 to page:5); leverage schedules in S-10K page:57, S-Q1-26 page:30, S-Q2-26 page:37 | Adjusted EBITDA only in releases; text-only extraction (tables flattened); Q3 2026 absent; covenant ratios are management calculations |
| CP-1A | READY_WITH_LIMITATIONS | Business, markets and strategy in S-10K page:4 to page:12; 2026 acquisitions, swap and divestitures in S-Q2-26 page:12, page:13, page:25; legal proceedings in S-10K page:109 | Part III governance and ownership incorporated from a proxy statement not supplied; acquisition agreements not supplied; pending regulatory approvals unresolved |
| CP-2 | READY_WITH_LIMITATIONS | Draws only on upstream CP-1 and CP-1A registers, which rest on the sources above | Inherits every CP-1 and CP-1A limitation; its dependency on upstream handoffs is sequenced by the planner and is not a source condition |
| CP-5 | READY_WITH_LIMITATIONS | Pack allows citation and quote checks against filings, with releases as attributed management claims | No independent third-party source (no rating report, no executed legal text) against which management claims can be tested |

### Source profiles

| Source | Document family and authority | Entity and perimeter | Period and basis | Version relationship | Extraction status |
| --- | --- | --- | --- | --- | --- |
| S-10K | Form 10-K, filed financial report; controls its own audited facts. Auditor opinion present (page:68). Signed February 26, 2026 (page:124). | Gray Media, Inc. and consolidated subsidiaries; holding company with no material independent assets or operations (page:55) | Year ended December 31, 2025 with 2024 and 2023 comparatives; audited; USD millions | Latest annual report; supersedes no other source; Q4 2025 results also in S-R-Feb | Text retained for 124 of 124 chunks; images and charts not inspected |
| S-Q3-25 | Form 10-Q, filed financial report; unaudited. Signed November 7, 2025 (page:45). | Same registrant and consolidation | Quarter and nine months ended September 30, 2025; unaudited; USD millions | Prior-year comparative period; retained as a separate active source | 45 of 45 chunks retained |
| S-Q1-26 | Form 10-Q, filed financial report; unaudited. Signed May 7, 2026 (page:34). | Same | Quarter ended March 31, 2026 with March 2025 comparatives; unaudited; USD millions | Separate period source; its quarter is also inside the six months in S-Q2-26 | 34 of 34 chunks retained |
| S-Q2-26 | Form 10-Q, filed financial report; unaudited. Signed August 7, 2026 (page:41). | Same | Quarter and six months ended June 30, 2026 with 2025 comparatives; balance sheet against December 31, 2025; unaudited; USD millions | Latest filed financial report in the pack; matches the run context current period | 41 of 41 chunks retained |
| S-R-Feb | Exhibit 99.1 earnings release dated February 26, 2026; management narrative, non-GAAP and statements; attributed supporting claims | Same | Fourth quarter and year ended December 31, 2025; unaudited release | Same-day companion to S-10K; the 10-K controls where they differ | 12 of 12 chunks retained |
| S-R-May | Exhibit 99.1 earnings release dated May 7, 2026; same status | Same | First quarter 2026 | Companion to S-Q1-26 | 11 of 11 chunks retained |
| S-R-Aug | Exhibit 99.1 earnings release dated August 7, 2026; same status | Same | Second quarter and six months 2026; includes guidance for the quarter ending September 30, 2026 | Companion to S-Q2-26; latest-dated evidence in the pack | 13 of 13 chunks retained |

Identity, document class and period were read from the cover pages and body text, not from file names. Confirming quotes:

- [S-10K page:1] "GRAY MEDIA, INC." is the exact registrant name and the report is for "the fiscal year ended December 31, 2025".
- [S-Q2-26 page:1] "For the quarterly period ended June 30, 2026".
- [S-Q1-26 page:1] "For the quarterly period ended March 31, 2026".
- [S-Q3-25 page:1] "For the quarterly period ended September 30, 2025".
- [S-R-Aug page:1] "Gray Media (NYSE: GTN) today announced its financial results for the quarter ended June 30, 2026."
- [S-R-May page:1] "today announced its financial results for the first quarter that ended March 31, 2026."
- [S-R-Feb page:1] "today announced its financial results for the fourth quarter that ended December 31, 2025."

### Entity, perimeter and instrument roles

The issuer, the reporting registrant and the debt obligor are the same entity, Gray Media, Inc.; no separate borrower or parent is named in the context or in the filings. Guarantor roles as described in the filings:

- [S-Q2-26 page:35] "We are a holding company, and have no material independent assets or operations."
- [S-Q2-26 page:35] "substantially all of our subsidiaries (subject to certain limited exceptions) are joint and several guarantors of, and our ownership interests in those subsidiaries are pledged to collateralize, our obligations under our 2019 Senior Credit Facility, the 2029 1L Notes, the 2033 1L Notes and the 2032 2L Notes."
- [S-Q2-26 page:35] "the 2030 Notes and 2031 Notes have been fully and unconditionally guaranteed, on a joint and several, senior unsecured basis, by substantially all of our subsidiaries"
- [S-Q2-26 page:35] Non-guarantor subsidiaries "are not material or are designated as unrestricted under our 2019 Senior Credit Facility".

The restricted or unrestricted split is not itemized: the covenant schedules show an "Adjustments for unrestricted subsidiaries" line (S-Q2-26 page:37) but no list of unrestricted subsidiaries is supplied. A receivables special purpose vehicle (the SPV) is a separate legal entity: [S-10K page:78] "The SPV is a separate legal entity with its own separate creditors who will be entitled to access the SPV's assets before the assets become available to us."

### Currency, units and periods

The statements state "(in millions)" (for example [S-Q2-26 page:2]) and the run context fixes USD; the sources print no other currency. The context labels the current period q2-2026 and the prior period fy-2025. In the sources these map to the three and six months ended June 30, 2026 (S-Q2-26 page:3) and the year ended December 31, 2025 (S-10K). The balance sheet comparatives are December 31, 2025 in every 2026 interim report. Three period types must stay separate downstream: discrete quarters (three-month columns), year-to-date (six-month and nine-month columns) and the eight-quarter averaged covenant denominator, which [S-Q2-26 page:36] describes as "represents an average amount for the preceding eight quarters then ended."

### Debt, liquidity and covenant evidence located

Debt by instrument at June 30, 2026 is printed in S-Q2-26 page:15, with coupons stated in the note introduction on page:14 and maturities on page:16:

- [S-Q2-26 page:15] "Total outstanding principal, including current portion 5,867"
- [S-Q2-26 page:16] The maturity table totals "$ 739 $ 1,125 $ 790 $ 1,218 $ 1,150 $ 845 $ 5,867".
- [S-Q2-26 page:15] "Borrowing availability under Revolving Credit Facility $ 745 $ 745"
- [S-Q2-26 page:37] "Consolidated Total Net Leverage Ratio (maximum permitted incurrence is 7.00 to 1.00) 5.73"
- [S-Q2-26 page:16] "we were in compliance with all required covenants under all our debt obligations."
- [S-Q2-26 page:34] "we estimate that we will make approximately $465 million in debt interest payments over the twelve months immediately following June 30, 2026."

The annual equivalents are in S-10K page:92 to page:95 (debt table, 2025 refinancing, maturities) and S-10K page:57 (leverage schedule). Quarter-end leverage schedules are in S-Q3-25 page:38 and page:39, S-Q1-26 page:30 and S-Q2-26 page:37; the releases repeat them (S-R-Feb page:12, S-R-May page:10 and page:11, S-R-Aug page:13).

Items outside the debt principal that the sources print and that downstream modules must treat separately:

- Receivables securitization: [S-Q2-26 page:8] "The amount sold to the Purchasers was $400 million as of both June 30, 2026 and December 31, 2025, which was derecognized from the respective condensed consolidated balance sheets." The release debt summary footnote states [S-R-Aug page:4] "Excludes letters of credit, accounts receivable securitization facility and preferred stock."
- Series A Perpetual Preferred Stock is presented outside stockholders' equity (S-Q2-26 page:2, page:3).
- Network affiliation commitments: [S-10K page:61] "Our network affiliation agreements expire at various dates from mid-2027 through December 31, 2028."
- Pension: [S-Q2-26 page:26] "the Pension Plan will be terminated effective October 1, 2026, subject to regulatory approval".
- Litigation: the antitrust consent decree and the consolidated class action are described in S-10K page:109, which states the consent decree "does not subject the parties to any monetary damages or penalties", and [S-Q2-26 page:40] "there have been no additional material legal proceedings or material developments".

### Subsequent events and cutoff

Everything below is dated after the June 30, 2026 balance sheet date and on or before the cutoff. All of it is reported in S-Q2-26 Note 15 and Item 2, or in S-R-Aug; nothing in the pack is dated after August 7, 2026.

- [S-Q2-26 page:25] "On July 21, 2026, we repurchased, in a privately negotiated transaction, $100 million aggregate principal amount of our 2029 IL Notes and $20 million aggregate principal amount of our 2031 Notes" and [S-Q2-26 page:25] "The repurchase was funded using available liquidity, including cash on hand and borrowings under our existing revolving credit facility." The notes text spells the 2029 notes "2029 IL Notes" (typographical); the release names them "10.500% Senior Secured First Lien notes due in 2029" (S-R-Aug page:4).
- [S-Q2-26 page:25] "Securitization Facility. On July 15, 2026, we amended the Securitization Facility to clarify the treatment of receivables from certain customers under bankruptcy proceedings."
- Debt repurchase authorization of up to $250 million through December 31, 2027, approved August 6, 2026 (S-Q2-26 page:26; S-R-Aug page:5).
- First closings of the American Spirit Media and WHPM station acquisitions on July 1, 2026, with second closings pending regulatory approval (S-Q2-26 page:25).
- Quarter ending September 30, 2026 guidance: [S-R-Aug page:5] "Based on our current forecasts for the quarter ending September 30, 2026". This is forward-looking management content, not a result.

The quarter ended September 30, 2026 and its Form 10-Q are not in the pack. At the as-of date that period is already over, so the latest reported leverage and liquidity date from June 30, 2026. See Gaps.

### Document conflicts and internal inconsistencies

| Id | Observation | Locators | Downstream effect | Severity |
| --- | --- | --- | --- | --- |
| X1 | Covenant trigger wording differs between the annual report and the latest 10-Q. The 10-K says "(h) maintenance of the First Lien Leverage Ratio while any amount is outstanding under the Revolving Credit Facility". The Q2 10-Q says maintenance applies "in the event revolving loans are outstanding under the revolving credit facility or more than $50 million of undrawn letters of credit are outstanding that have not been cash collateralized". The credit agreement was amended and restated on March 31, 2026. | S-10K page:55; S-Q2-26 page:35; S-Q2-26 page:15 | The controlling text cannot be confirmed without the executed credit agreement. CP-1 and CP-2 must quote the issuer summary, not state a trigger as a legal fact. | Medium |
| X2 | The $10 million term loan balance carries different labels. The 10-K calls it "2024 Term Loan (1L) (matures June 4, 2029) 10 498"; the first-quarter 10-Q calls it "2026 1L Term Loan (pre-paid April 2, 2026) 10 10" and its text says "On April 2, 2026, we repaid the $10 million remaining balance on the 2024 term loan." | S-10K page:91; S-Q1-26 page:12; S-Q1-26 page:26 | Same balance, different name. A facility-level extraction must map both labels to one tranche and note it was repaid in April 2026. | Low |
| X3 | First-quarter 2026 total principal differs by one million between the debt note ("Total outstanding principal, including current portion 5,808 5,810") and the covenant schedule ("Total outstanding principal, including current portion $ 5,809"). The note components sum to 5,808. | S-Q1-26 page:12; S-Q1-26 page:30 | Immaterial rounding in a single filing, but exact-value comparison across modules will flag it. Use the note figure for the debt table and the schedule figure for covenant quotes. | Low |
| X4 | Typographical errors in covenant and notes text: the first-quarter 10-Q footnote refers to "2023 Notes (2L)" for the second lien notes that mature in 2032, and the second-quarter text says "2029 IL Notes". | S-Q1-26 page:30; S-Q2-26 page:25 | Label mapping only; the tranche is identifiable from amount, rate and maturity. | Low |
| X5 | Two net debt figures for June 30, 2026 are printed under different definitions: the release shows debt less cash of 5,691 and excludes letters of credit; the covenant schedule shows Consolidated Total Net Debt of 5,696 and adds 5 of letters of credit. | S-R-Aug page:4; S-Q2-26 page:37 | Not a conflict, a definition difference. Downstream modules must name which definition each net debt figure uses. | Low |

No conflict was found between the filings and the releases on the figures compared: cash of 176 and revolver availability of 745 at June 30, 2026 agree between S-Q2-26 page:2, page:15 and S-R-Aug page:5, and the leverage ratios of 2.55, 3.71 and 5.73 agree between S-Q2-26 page:37 and S-R-Aug page:5.

### Authority and management claims

Filed statements control their own facts. The earnings releases supply management narrative, guidance and the following items that are not in the filings:

- Adjusted EBITDA and its reconciliation: [S-R-Aug page:12] "Reconciliation of Adjusted EBITDA (Unaudited):", with "Adjusted EBITDA $ 214 $ 169 $ 368 $ 329". A text search of S-10K, S-Q3-25, S-Q1-26 and S-Q2-26 for "Adjusted EBITDA" returned no match, so the metric is a management claim supported by reconciling items that are themselves in the filings.
- Net Retransmission Revenue and its definition, which is also management-defined.
- Guidance, executive commentary and the political advertising comparisons.

The covenant ratios are management calculations under the credit agreement. [S-Q2-26 page:36] "Certain of the financial information related to the acquisitions, if applicable, has been derived from, and adjusted based on, unaudited, un-reviewed financial information prepared by other entities, which Gray cannot independently verify." The denominator includes synergies and acquisition adjustments, so it is not a GAAP or Regulation S-X measure.

### Coverage accounting

Retained: all text chunks of the seven sources, 280 chunks in total (124, 45, 34, 41, 12, 11 and 13). Every statement, note, MD&A table and exhibit index in these chunks is retained text. Explicit parse gaps: the sources are text extractions, so table layout is flattened, and no image, chart, logo or inline XBRL data was inspected; no coverage of those is claimed. Evidenced exclusions: none. Exhibits listed in the exhibit indexes (credit agreement, indentures, supplemental indenture, note purchase agreement, receivables purchase agreement amendments, S-10K page:118 to page:122; S-Q2-26 page:40 and page:41) are incorporated by reference or filed separately and are not part of this pack. Duplicates: the three releases repeat figures from the companion filings; they are retained as separate attributed sources and none is treated as a substitute for its filing.

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures, and this handoff reports figures as printed. Three arithmetic checks were made only to support coverage and consistency statements:

| Check | Inputs | Result |
| --- | --- | --- |
| Total source chunks | 124 + 45 + 34 + 41 + 12 + 11 + 13 | 280 |
| Q1 2026 debt note components, USD millions (S-Q1-26 page:12) | 739 + 10 + 1,125 + 775 + 1,150 + 790 + 1,219 | 5,808, which agrees with the printed note total and differs by 1 from the covenant schedule total of 5,809 (X3) |
| Age of latest evidence at the as-of date | August 7, 2026 to November 5, 2026 | 90 days |

## Gaps

| Id | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | Third-quarter 2026 report and release are not in the pack. The latest balance sheet is June 30, 2026 and the latest release is dated August 7, 2026. Nothing reported after that date is available to the pack. | High | CP-1, CP-1A, CP-2, CP-5 | Add the Form 10-Q and Exhibit 99.1 for the quarter ended September 30, 2026 if filed on or before the cutoff; otherwise state the staleness in every module. |
| G2 | Executed credit agreement (as amended and restated March 31, 2026, S-Q2-26 page:15), indentures, collateral documents and the receivables purchase agreement with its amendments are not supplied; the context states legal documents as none. Covenant triggers, baskets, definitions, step-downs and release mechanics rest on issuer summaries. | Medium | CP-1, CP-1A, CP-2, CP-5 | Add the executed documents; until then label every covenant statement as issuer-described (X1). |
| G3 | The amount of revolver borrowings used on and after July 21, 2026 is not disclosed (S-Q2-26 page:25), and no later balance sheet is supplied. Revolver availability after June 30, 2026 is Not calculable from the pack. | Medium | CP-1, CP-2 | Obtain the September 30, 2026 balance sheet or an 8-K that discloses the draw. |
| G4 | Adjusted EBITDA is available only in earnings releases and has no filed counterpart. | Medium | CP-1, CP-2, CP-5 | Label it management-reported and attributed to the release; use the filed statements for GAAP lines. |
| G5 | Part III governance, ownership and compensation are incorporated by reference from the 2026 proxy statement (S-10K page:116), which is not supplied. Ownership and control detail beyond the cover share counts and the equity note is Not supplied. | Medium | CP-1A, CP-2 | Add the 2026 proxy statement. |
| G6 | Acquisition, swap and divestiture agreements are not supplied (Scripps swap, Allen Media Group, Block, Sagamore Hill, American Spirit Media, WHPM). Second closings for American Spirit Media and WHPM depend on regulatory approval (S-Q2-26 page:25). Pro forma figures for closed deals are only the unaudited adjustments inside the covenant denominator. | Medium | CP-1A, CP-2 | Add the purchase agreements or 8-K summaries; treat pending closings as unresolved. |
| G7 | No inspection of images, charts, inline XBRL or table layout; no fidelity review of extracted figures beyond the spot checks cited here. No investor presentation is in the pack. | Low | CP-1, CP-5 | Check cited figures against the page text before use; add presentations if narrative slides are needed. |
| G8 | Label inconsistencies X2 to X4 need explicit tranche mapping in a facility-level extraction. | Low | CP-1, CP-5 | Map labels by amount, rate and maturity and record the mapping. |
| G9 | No third-party ratings, quotes, peers or valuation inputs are supplied (context fields are blank). Market-based and relative-value work cannot be sourced from this pack. | Low for the selected minimum set | CP-2 | Not needed for the selected reports; keep out of scope. |

## Next module

Proceed with CP-1 (financial extraction), then CP-1A, CP-2 and CP-5 in the run order. Carry these instructions forward:

1. Extract from the filed statements first. Use S-Q2-26 for the current period (three and six months ended June 30, 2026 and the June 30, 2026 balance sheet), S-10K for the audited year ended December 31, 2025, S-Q3-25 and S-Q1-26 for the other quarters. Keep discrete quarters, year-to-date columns and the eight-quarter covenant denominator separate.
2. Treat Adjusted EBITDA, Net Retransmission Revenue and guidance as management claims from the releases, with locators (G4).
3. Present debt by instrument from S-Q2-26 page:15 and page:16, with the securitization facility, letters of credit, preferred stock and operating leases reported outside the debt principal and labelled as such (X5). State the revolver availability as of June 30, 2026 only, and mark the position after the July 21, 2026 repurchase Not calculable (G3).
4. Quote covenant statements as issuer-described and mention X1 and G2 wherever a trigger or level is used.
5. Carry G1 into every module as a staleness limitation at the as-of date of 2026-11-05.
6. CP-1A should use S-10K page:4 to page:12 for the business, S-Q2-26 Notes 3 and 15 for 2026 transactions, and mark ownership and governance Not supplied beyond the filings (G5, G6).
