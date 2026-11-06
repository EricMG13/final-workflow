## Request

Module: source readiness for APi Group Corp (APG), issuer id apg, as-of date 2026-11-05, evidence cutoff 2026-11-05. Pathway credit_snapshot; current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025; reporting currency USD, stated in millions in the filings. Question: can the supplied source set support the selected downstream modules (CP-1, CP-1A, CP-2, CP-5), and what remains blocked. This module gives no credit conclusion, legal interpretation or investment opinion, and it performs no analytical calculation. Source sufficiency is distinct from completion of downstream analysis.

The run context (sha256 below) holds the dated run settings only; it is not issuer evidence. It leaves ratings, quotes, deal terms, valuation inputs and research questions blank, sets legal documents to "none" and names no borrower, parent or guarantors. Blank values are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Document family and original authority |
| --- | --- | --- |
| 10-K_2025-12-31_apg-20251231.htm.jsonl | 85e734a169388fec4ab633a5bed87c9c814f23738d0e6cf5a912dd14edbbba4e | Annual report (Form 10-K), FY2025, audited; filed statements control |
| 10-Q_2026-03-31_apg-20260331.htm.jsonl | 4f2797670271476a95f9547a3540ae303edaa5e40f3e3f08829817127f41c878 | Quarterly report (Form 10-Q), Q1 2026, unaudited; filed statements control |
| 10-Q_2026-06-30_apg-20260630.htm.jsonl | e90d6bf8c69051d7d18a0cfac2ae57b46434273469a8084102121b4455760a9f | Quarterly report (Form 10-Q), Q2 2026, unaudited; filed statements control |
| 10-Q_2026-09-30_apg-20260930.htm.jsonl | 0f3c88ef7de625d84cef8d9062b4481840371b9e18740b974653c45bd1fc951f | Quarterly report (Form 10-Q), Q3 2026, unaudited; latest filed statements |
| EX-99.1_2026-04-30_apg-20260331xexx991.htm.jsonl | 1e2bb7155c93f1d7180c8420214b4e920240b52127bf64099c673d664920aca5 | Earnings release (Exhibit 99.1), Q1 2026; management attributed, supporting only |
| EX-99.1_2026-07-30_apg-20260630xexx991.htm.jsonl | f112ae35c8090bbb1d28641903d8fabef87924332451d391abea2504360e0996 | Earnings release (Exhibit 99.1), Q2 2026; management attributed, supporting only |
| EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl | f776b9079a3057680b637f70cfc8304a121c49085a5098404f23ccab4852f2c3 | Earnings release (Exhibit 99.1), Q3 2026; management attributed, supporting only |

### Run input, not issuer evidence

| Input | sha256 | Role |
| --- | --- | --- |
| context (1796209-api-group-corp-apg.json) | 5361f531841cad8936701ac126679da0830e0b3a545fa6b1b9ab2f313f6dfc9d | Dated run settings |

### Handoffs supplied

None. CP-0 is the first module in this run and no upstream handoff exists, so none was consumed.

### Coverage method

Each source is a text extraction ("Visible text of ..." per page, retained as page:N chunks). Page chunks are extraction units, not printed page numbers. Retained units: 153 pages (annual report), 53, 65 and 66 pages (Q1, Q2, Q3 quarterly reports), 17, 15 and 15 pages (Q1, Q2, Q3 releases), which is 384 retained units. Readiness rests on full-text search of every retained unit and on direct reading of the units cited below. It does not rest on a page-by-page reading of all 384 units, and no source-count or page-count proxy is claimed as readiness. Extraction status is separate from fidelity: no check against the original HTML or the XBRL was possible, and charts, images and any slide content are not captured by the extraction.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and releases can support a credit snapshot of APi Group Corp as of 2026-11-05, with bounded limitations. Legal documents are not supplied, so covenant and guarantor terms rest on filing summaries. | Medium | No credit agreement, indentures or guarantor list is supplied; covenant EBITDA definition is not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report, three quarterly reports and three earnings releases cover FY2025 and the first three quarters of 2026, including the September 30, 2026 balance sheet and cash flows. | Leverage, liquidity and cash-flow work can start from filed statements rather than management claims. | High |
| Debt changed in 2026: a new senior note issue, a larger revolver, extended maturities for the term loan and revolver, and further revolver borrowing after quarter-end. | Debt and maturity analysis must use the latest quarterly report, because the annual report shows superseded terms. | High |
| Covenant definitions, guarantor identities and the issuer of record for the notes are not documented beyond filing summaries. | Covenant headroom and structural position can only be assessed with a stated limitation. | Medium |
| A stand-alone fourth quarter 2025 period and a last-twelve-months figure are not printed; they would need to be built from the annual and year-to-date figures. | Trailing leverage and coverage need a transparent build, and any result carries the caveat that it is derived. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for all four selected consumers. The filed statements, debt notes, liquidity discussion, segment notes, acquisition notes and subsequent-event notes needed for a credit snapshot are present and located in the latest quarterly report, with the annual report giving the FY2025 base and the releases giving attributed adjusted measures and guidance. No consumer is CONDITIONAL or BLOCKED: no source shows blocked preparation in the run output, no identity boundary is unresolved to the point of preventing the work, and every limitation below is bounded. The recurring limitations to carry forward are the absence of executed legal documents (credit agreement, amendments, indentures), the unenumerated guarantor group, the unresolved issuer-of-record wording for the notes, the covenant EBITDA definition that the sources only refer to, and the text-only extraction. This is a source-sufficiency assertion only (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED): it does not assert normalized quarters, reconciliation or acceptance of any downstream input.

| Consumer | Status | Located evidence | Limitations carried |
| --- | --- | --- | --- |
| CP-1 (financial data and credit metrics) | READY_WITH_LIMITATIONS | Statements, debt table, liquidity, covenant ratio, cash paid for interest, adjusted EBITDA and free cash flow reconciliations, segment data | Stand-alone Q4 2025 and LTM not printed; covenant EBITDA definition not supplied; lease note only in the annual report; text-only extraction |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, segments, 2026 acquisitions, financing events, related-party and preferred-stock facts | No acquisition agreements, credit agreement or indentures; guarantor group not enumerated; issuer-of-record wording differs between documents |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Draws on upstream CP-1 and CP-1A only; the underlying evidence is located as above | Inherits every CP-1 and CP-1A limitation; no ratings or market data supplied |
| CP-5 (evidence trace validation) | READY_WITH_LIMITATIONS | Every cited fact below carries an exact quote and page:N locator in a retained source | Pages are extraction chunks; releases are management claims; no original-HTML fidelity check |

### Source-by-source assessment

#### Annual report, FY2025

Identity and period: (10-K_2025-12-31_apg-20251231.htm.jsonl page:1: "For the fiscal year ended December 31, 2025") with (10-K_2025-12-31_apg-20251231.htm.jsonl page:1: "Commission File Number 001-39275"). Authority: audited filed statements (auditor signature (10-K_2025-12-31_apg-20251231.htm.jsonl page:85: "/s/ KPMG LLP")). Content located: balance sheet ((10-K_2025-12-31_apg-20251231.htm.jsonl page:85: "Cash and cash equivalents $ 912 $ 499")), operations ((10-K_2025-12-31_apg-20251231.htm.jsonl page:86: "Net revenues $ 7,911 $ 7,018 $ 6,928")), cash flows ((10-K_2025-12-31_apg-20251231.htm.jsonl page:88: "Cash paid for interest, net of interest income $ 136 $ 152 $ 150")), debt note ((10-K_2025-12-31_apg-20251231.htm.jsonl page:121: "2021 Term Loan January 3, 2029 $ 2,157 $ 2,157")), maturity table ((10-K_2025-12-31_apg-20251231.htm.jsonl page:123: "2029 2,771")), segment note and a lease note. It is the base for FY2025 and the superseded debt terms; later quarterly reports control any fact they restate.

#### Quarterly reports, Q1, Q2 and Q3 2026

Q3 identity and period: (10-Q_2026-09-30_apg-20260930.htm.jsonl page:1: "For the quarterly period ended September 30, 2026"). Statements present three-month and nine-month columns ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:3: "Net revenues $ 2,554 $ 2,085 $ 6,790 $ 5,794")) and the September 30, 2026 balance sheet against December 31, 2025 ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:2: "Cash and cash equivalents $ 373 $ 912")). The Q1 and Q2 reports give the intermediate quarter-end balance sheets, debt tables and covenant ratios, so discrete quarters and year-to-date amounts are separable by period label. Facility-level debt carrying values are in the Q3 debt note ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:23: "Total debt obligations 3,601 2,776")). Cash-paid interest is in the Q3 cash flow statement ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:5: "Cash paid for interest, net of interest income $ 98 $ 105")). The quarterly reports contain no lease note; operating and finance lease liabilities appear only as balance sheet lines ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:2: "Operating and finance leases 101 98")).

#### Earnings releases, Q1, Q2 and Q3 2026

These are management-attributed supporting sources. The Q3 release states (EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl page:1: "Record third quarter adjusted EBITDA of $350 million") and provides the reconciliation ((EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl page:11: "Adjusted EBITDA $ 350 $ 281 $ 896 $ 746")), the adjusted free cash flow reconciliation ((EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl page:15: "Adjusted free cash flow $ 240 $ 248 $ 468 $ 434")) and guidance ((EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl page:3: "Net revenues of $9,200 to $9,250 million")). Adjusted measures are non-GAAP and cannot override the filed statements. The Q1 and Q2 releases are retained as separate sources for the prior-quarter series and prior guidance; none is a duplicate of another, and none supersedes a filing.

### Entity and perimeter

The registrant and reporting entity is APi Group Corporation, with consolidated statements of "APi Group Corporation and subsidiaries" (context name: APi Group Corp; NYSE ticker APG shown on the cover). The borrower of the credit facilities is a subsidiary: (10-Q_2026-09-30_apg-20260930.htm.jsonl page:58: "a Credit Agreement by and among APi Group DE, Inc., our wholly-owned subsidiary, as borrower"), with the parent as guarantor and Citibank N.A. as administrative and collateral agent. The senior notes are described as guaranteed by the parent and "certain of our subsidiaries" ((10-K_2025-12-31_apg-20251231.htm.jsonl page:73: "fully and unconditionally guaranteed on a senior unsecured basis by us and certain of our subsidiaries")). No restricted or unrestricted subsidiary split, guarantor schedule or separate issuer financials is supplied; all supplied financials are consolidated. The 10-K and 10-Q describe a senior secured revolver ("Revolving Credit Facility") and a term loan under one Credit Agreement; the legal security package is not documented in the pack.

### Reporting periods and basis

All amounts are USD millions as printed, on a US GAAP basis; the sources use calendar fiscal quarters. Supplied periods: FY2025 (and FY2024 and FY2023 comparatives in the 10-K), Q1, Q2 and Q3 2026 with the prior-year comparatives, six and nine months 2026, and quarter-end balance sheets at December 31, 2025, March 31, June 30 and September 30, 2026. Geographic revenue is split United States, France and Other ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:12: "France 525 — — 525")). Not supplied as a stand-alone period: Q4 2025, because no fourth-quarter release is in the pack; a last-twelve-months figure is not printed anywhere in the sources (searched for LTM and trailing twelve months). All sources are dated on or before 2026-10-29, within the cutoff; the latest, the Q3 release and report, are dated October 29, 2026. One subsequent event is dated before the cutoff and is carried as such: (10-Q_2026-09-30_apg-20260930.htm.jsonl page:24: "Subsequent to September 30, 2026, the Company borrowed an additional $100 under the Revolving Credit Facility for general corporate purposes").

### Version relationships and changes between sources

These are amendments and updates, kept as separate active sources; the later filing controls a restated fact only where it says so.

| Item | Earlier source | Later source | Note |
| --- | --- | --- | --- |
| 2021 Term Loan maturity | (10-K_2025-12-31_apg-20251231.htm.jsonl page:121: "2021 Term Loan January 3, 2029 $ 2,157 $ 2,157") | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:22: "2021 Term Loan May 14, 2033 $ 2,147 $ 2,157") | Later report attributes the extension to the Ninth Amendment ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:24: "extended the maturity date of the 2021 Term Loan to May 14, 2033")); the amendment text itself is not supplied |
| Revolver size and maturity | $750 million, maturing May 20, 2030 per the 10-K debt table | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:24: "increased the Revolving Credit Facility by $250, from $750 to $1,000") and maturity May 14, 2031 | Availability after letters of credit moved from $745 million at year-end to $659 million at September 30, 2026 ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:56: "$1,032 million of total liquidity")) |
| Senior notes | Two series at year-end | A third series added in Q2 2026 ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:60: "On May 14, 2026, APi Group DE completed a private offering of $500 million aggregate principal amount of 5.750% Senior Notes due 2034")) | Indenture of May 14, 2026 not supplied |
| Pending acquisitions | (10-Q_2026-03-31_apg-20260331.htm.jsonl page:30: "Wtech will be acquired for approximately €324 in cash") (signed, April 17, 2026) | Closed: (10-Q_2026-09-30_apg-20260930.htm.jsonl page:8: "On July 1, 2026, the Company completed the acquisition of WTech Fire Group") | Purchase accounting is provisional ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:9: "The Company has not finalized its accounting for any of the acquisitions completed during 2026")) |

### Source differences and conflicts, with downstream effect

Each item is logged as found; none is reconciled or resolved here.

1. Letter-of-credit exclusion in the springing covenant. The annual report says (10-K_2025-12-31_apg-20251231.htm.jsonl page:73: "(excluding undrawn letters of credit up to $40 million)"); the Q3 report says (10-Q_2026-09-30_apg-20260930.htm.jsonl page:60: "excluding undrawn letters of credit up to $60 million"). Likely a result of the 2026 amendment, but the amendment is not supplied. Effect: CP-1 must use the Q3 wording for the current test and flag the change.
2. Term loan amortization. The annual report says (10-K_2025-12-31_apg-20251231.htm.jsonl page:72: "we do not owe any quarterly principal amounts for the remainder of the 2021 Term Loan"); the Q3 report says (10-Q_2026-09-30_apg-20260930.htm.jsonl page:59: "Principal payments on the 2021 Term Loan will be made in quarterly installments on the last day of each fiscal quarter"). The reason for the change is not stated in the supplied text. Effect: the debt schedule for CP-1 should follow the Q3 report and note the change as unexplained.
3. Issuer of record for the notes. The MD&A says (10-K_2025-12-31_apg-20251231.htm.jsonl page:73: "On June 22, 2021, APi Group DE completed a private offering of $350 million aggregate principal amount of 4.125% Senior Notes due 2029"), while the exhibit index lists the indenture as (10-K_2025-12-31_apg-20251231.htm.jsonl page:150: "Indenture, dated as of June 22, 2021, by and among APi Group Corporation, the guarantors party thereto and Computershare Trust Company, N.A."). The indentures are not supplied, so the legal issuer, co-issuer and guarantor roles remain unresolved. Effect: CP-1 and CP-1A must describe the notes as issued and guaranteed per the MD&A wording and mark issuer identity as a gap.
4. Share repurchase amount. The Q3 MD&A says (10-Q_2026-09-30_apg-20260930.htm.jsonl page:57: "we repurchased 6,338,563 shares of common stock for approximately $250 million") for the nine months, while the cash flow statement shows (10-Q_2026-09-30_apg-20260930.htm.jsonl page:5: "Repurchases of common stock (252)"). The basis difference (for example settlement timing) is not stated. Effect: minor; use the cash flow amount for cash and the MD&A for share count, with the difference noted.
5. Stale covenant wording. The Q1 report still carries (10-Q_2026-03-31_apg-20260331.htm.jsonl page:47: "(i) 4.00 to 1.00 for each fiscal quarter ending in 2021"), which is boilerplate for periods long past; the current test level in the same sentence is 3.75 to 1.00. Effect: none beyond citing the current level.
6. Location counts differ by date: (10-K_2025-12-31_apg-20251231.htm.jsonl page:8: "over 500 locations worldwide") in the annual report and (EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl page:4: "With more than 600 locations in over 20 countries") in the Q3 release, the latter management-attributed and after 2026 acquisitions. Effect: CP-1A should cite each with its date.

Extraction observation (not an issuer conflict): the Q3 report's note heading splits across extraction units ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:28: "NOTE 13.") ends one unit and (10-Q_2026-09-30_apg-20260930.htm.jsonl page:29: "RELATED-PARTY TRANSACTIONS The Company incurred advisory fees") begins the next). Locators should name both units where a note spans them.

### Strongest contrary evidence and what cannot proceed

The strongest limit on readiness is that the executed financing documents are absent while the credit-relevant terms (covenant tests, guarantor group, note issuer, security) sit in them. The filings summarise a maintenance test that applies only when revolver usage passes a threshold ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:60: "is greater than 30% of the total revolving credit commitments thereunder subject to a right of cure")), report the ratio as (10-Q_2026-09-30_apg-20260930.htm.jsonl page:60: "Our first lien net leverage ratio as of September 30, 2026 was 1.6:1.0") (rounded to one decimal) and defer the covenant EBITDA definition to filings that do not contain it ((EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl page:7: "for the covenant EBITDA definition")). Consequence: CP-1 can state the reported ratio, the threshold and the printed revolver, letter-of-credit and commitment amounts, but cannot recompute covenant leverage or confirm whether the 30% usage trigger was met under the credit agreement's definitions. Source risk mechanism: a springing covenant whose trigger and EBITDA definition are outside the pack leaves covenant headroom a filing-summary claim, not a verified figure.

Other things that cannot proceed on this source set: rating-agency views (only an incidental mention appears, (10-K_2025-12-31_apg-20251231.htm.jsonl page:119: "ratings have remained stable at BB and Ba2 in 2025"), inside a lease discount-rate discussion), market-based valuation (context market inputs blank), peer comparison, and guarantor or structural-subordination analysis by legal entity.

### Context facts located for CP-1A

For the business and transaction consumer: the 2026 acquisitions are located with consideration ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:8: "On February 2, 2026, the Company completed the acquisition of CertaSite, LLC"); (10-Q_2026-09-30_apg-20260930.htm.jsonl page:8: "On June 8, 2026, the Company completed the acquisition of Onyx-Fire Protection Services, Inc."); WTech above), with Onyx-Fire acquired (10-Q_2026-03-31_apg-20260331.htm.jsonl page:30: "from funds managed by Blackstone Tactical Opportunities") per the Q1 report. Ownership and governance facts located: (10-Q_2026-09-30_apg-20260930.htm.jsonl page:29: "payable to Mariposa Capital, LLC") and Series A Preferred Stock that (10-Q_2026-09-30_apg-20260930.htm.jsonl page:29: "will be convertible into 6,000,000 shares of common stock upon conversion on the last day of 2026"), a future date stated as a contract term. Share repurchases after quarter-end are located ((10-Q_2026-09-30_apg-20260930.htm.jsonl page:37: "Subsequent to September 30, 2026, the Company repurchased 3,604,478 shares of common stock for approximately $143 under the 2025 SRP")). Contracted revenue visibility is located as remaining performance obligations ((10-K_2025-12-31_apg-20251231.htm.jsonl page:107: "was $3,605") at year-end, (10-Q_2026-09-30_apg-20260930.htm.jsonl page:12: "was $4,863") at September 30, 2026); these are accounting measures for in-process contracts and are not the same as backlog.

## Calculations

No analytical calculation was performed. CP-0 does not normalize, reconcile or derive figures. Two extraction-fidelity tie-outs only, each comparing printed components with a printed total in the same table:

| Check | Inputs (all printed) | Result |
| --- | --- | --- |
| Q3 debt table foots | 2,147 + 335 + 337 + 277 + 500 + 5 (Q3 debt note, September 30, 2026) | 3,601, equals the printed total debt obligations |
| Q3 debt carried on the balance sheet | 3,601 less unamortized deferred financing costs 27 (Q3 debt note) | 3,574, equals current debt 361 plus long-term debt 3,213 on the balance sheet |

Both tie-outs confirm the extraction matches the filing arithmetic; they do not establish fidelity to the original HTML. Not calculated, and left to the named consumers: net debt, leverage, coverage, liquidity roll-forward, LTM figures, and the revolver usage percentage against the springing-covenant threshold.

## Gaps

| Gap | Reason it matters | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| Credit Agreement, all amendments including the Ninth Amendment, and indentures for the three note series: Not supplied (the 10-K exhibit index lists the earlier credit agreement documents and indentures, but the pack contains none of them, and the 2026 indenture and amendment are not in the pack either; run context sets legal documents to none) | Covenant terms, baskets, security, guarantors and note issuer roles cannot be verified | High | CP-1, CP-1A, CP-2, CP-5 | Add the executed documents or state filing-summary limits |
| Guarantor identities: Not supplied. Searched the sources for guarantor schedules; only generic "certain of our subsidiaries" wording was found | Structural position and guarantor coverage cannot be assessed | Medium | CP-1A, CP-2 | Add an exhibit or guarantor schedule |
| Covenant EBITDA definition and components of the reported ratio: Not supplied. Releases refer to the filings, whose text defines only the ratio level | Headroom cannot be recomputed; only the reported rounded ratio is available | Medium | CP-1, CP-2 | Add the credit agreement definition |
| Stand-alone Q4 2025 period and LTM figures: Not supplied as printed (no Q4 2025 release in pack) | Trailing metrics need a derived build from annual and year-to-date figures | Low | CP-1 | Derive transparently and label as derived |
| Lease detail for 2026 quarters: Not supplied; the quarterly reports show balance sheet lines only | Lease-adjusted metrics use year-end detail | Low | CP-1 | Use the annual lease note with its date |
| Ratings, market quotes, valuation, peers: Not supplied (context blank; incidental rating mention in annual report only) | No external credit or market view | Low for snapshot | CP-2 | Add agency reports if needed |
| Charts, images and any presentation content: not captured by the text extraction; the pack contains releases, not decks | Visual content cannot be claimed as inspected | Low | CP-1A | Add decks if needed |
| Original-HTML or XBRL fidelity check: not performed | Extraction success is not a fidelity review | Low | CP-5 | Spot-check key tables against the originals |
| Acquisition agreements and purchase accounting beyond provisional notes: Not supplied | Purchase accounting is unfinalized | Low | CP-1A | Track measurement-period updates |

## Next module

Proceed to CP-1 (financial data and credit metrics), then CP-1A (business and transaction context), then CP-2 and CP-5, in the order the planner sets. Carry forward, in each: use the Q3 2026 quarterly report as the controlling source for debt terms, the covenant level and availability; treat the releases as attributed claims; mark note issuer, guarantor group and covenant EBITDA as unresolved; label any derived LTM or leverage figure as derived; cite page:N locators; and treat the October 2026 revolver borrowing and share repurchase as subsequent events. The next evidence action is to obtain the Credit Agreement with the Ninth Amendment and the three indentures; until then every covenant and guarantor statement stays a filing-summary claim.
