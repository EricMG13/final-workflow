## Request

This is the evidence trace and research-integrity review for Hudbay Minerals Inc., as of 2026-11-05, on the credit_snapshot pathway, with an evidence cutoff of 2026-11-05. It tests whether the source readiness, financial base, business and transaction register and credit synthesis handoffs rest on the filings they cite, recompute correctly and agree with each other. It changes no credit conclusion and repairs no lineage.

## Sources

Each issuer source is a JSONL text extraction of an SEC filing. The locator `page:N` is the extraction chunk, not the printed page. All seven sources were searched in full for quotes and figures. The sha256 values are the pinned file hashes.

### Issuer sources relied on

| Source name | sha256 | Document class |
| --- | --- | --- |
| 40-F_2025-12-31_form40f.htm.jsonl | 2e155789735b2bff45a2bcbe054290dc180366fb4697dc24f2f2d4f1c7050c41 | Annual report cover document (Form 40-F) |
| 6-K-EX-99.1_2025-09-30_exhibit99-1.htm.jsonl | 55a93575304a5e2b953260f4e274c5a39ae30021f2c92b99af4427f537390e4f | MD&A for Q3 2025 |
| 6-K-EX-99.1_2026-03-31_exhibit99-1.htm.jsonl | 532cee6ac6a8650d6600327aa510e9427055b8d19ea466fcd1e56834f9e80c49 | Unaudited interim statements, Q1 2026 |
| 6-K-EX-99.1_2026-06-30_exhibit99-1.htm.jsonl | 12a37c8778b0cbc30486cf54048199e1b52e4f3eeea4aa98f015138ba6c8b8ca | Unaudited interim statements, Q2 2026 |
| 6-K-EX-99.3_2025-12-31_exhibit99-3.htm.jsonl | 99f49739a1f92152e3b1a86a18c1ee2162a4da0c2cc8d427da3a3335818d9569 | News release, Q4 and FY2025 |
| 6-K-EX-99.3_2026-03-31_exhibit99-3.htm.jsonl | ada0c26b16ac32d6f2b222633c4110e11a601b22fd66b81f76af348b97d3b4a8 | News release, Q1 2026 |
| 6-K-EX-99.3_2026-06-30_exhibit99-3.htm.jsonl | 5519d54c6ee343772d1472890091915c574ee3b20549bcd2dd8544703027a844 | News release, Q2 2026 |

The run context (sha256 021d8bac1e30ca507d1d237248f47111a88bf0caf21c22980b85e1e72c6ea47c) supplies run settings only and is not issuer evidence. Its ratings, market data, valuation, borrower, parent and guarantor fields are blank and are treated as not supplied, never as zero.

### Supplied handoffs

| Module | sha256 | Status |
| --- | --- | --- |
| CP-0 | e9dbd2ab9d4365edb1c5ad19429b023878f8b986a46fedd1e14735a884877657 | Accepted; readiness gate |
| CP-1 | da8f8dbede6b46939301242ef9c6bcc579e27714e531f445631581d70f3523ab | Accepted; evaluated |
| CP-1A | 77f18427d7183f493b28a7833bd301e13f46ac3f9e2d8bdfc3348905ae80e888 | Accepted; evaluated |
| CP-2 | c6af3dd0ff01e0553ca8ad1fb61faacc803fa9ae66cad4752d8bd860fa2f0320 | Accepted (second attempt); evaluated |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The figures and quotes in the handoffs trace to the filings and recompute correctly, and the modules agree. Committee use is restricted because covenants, debt documents and audited annual statements are missing, not because tracing failed. | Medium | This review was done in the same session as the analysis, so it is not an independent second reviewer. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every quoted span in the business register was found on the page cited, and all checked ties and ratios recomputed to the printed or stated value. | The numbers a committee would quote can be relied on as labelled. | High |
| Six source conflicts remain unresolved and are carried by name, including a share count difference of 1,312,328 shares and a free cash flow history that changed between releases. | Per-share and cash flow series must name the source version, and no figure may splice versions. | High |
| Two statements are only partly supported: the explanation that half-year interest cover is timing-distorted, and cash of 556.4 described as available to the rest of the group. | These are wording limits; the figures are right, but the interpretations go slightly beyond what the filings state. | Medium |
| Several derived figures in the financial base are stated in text without a line in its calculations table, and one share issue value cites the wrong page. | The derivations are simple and reproduce, so this is a presentation defect, not a reliability defect. | High |
| The latest source is dated 2026-07-29, which is 99 days before the as-of date, and no covenant level or debt document is supplied. | Events and terms that decide the credit view are outside the evidence. | High |

### Evidence trace view

The evidence trace holds. Each material claim in the financial base, the business and transaction register and the credit synthesis was matched to a located source span or to a recomputation from located figures, and the three analytical handoffs agree on every shared figure, period and perimeter label. The synthesis view, a sound profile with Medium confidence and thin committed liquidity as the weak point, follows from the cited basis and is not overstated. Two claims are only partly supported, both as wording rather than figures: that half-year interest cover is distorted by coupon timing, which the filings do not state because coupon dates are not printed, and that cash outside Copper World is available to the rest of the group, which the filings do not say. No claim was found unsupported and no contradiction between modules was found. The integrity verdict for the evaluated set is Restricted, not Committee Ready, because the conclusions that matter most to a creditor rest on documents that are not in the sources: covenant levels and headroom, the indenture and credit agreements, the Copper World contract and plans, the audited FY2025 statements and anything dated after 2026-07-29. Six source conflicts remain open and are named below. The review itself is limited: it was done in the same session as the analysis, from the same extraction text, and page locators are extraction chunks rather than printed pages.

### Evaluated set (inputs and status)

| Input | Status | Evaluated | Notes |
| --- | --- | --- | --- |
| CP-0 source readiness | Accepted; gate | Quotes and figures rechecked only | Source classes, perimeter and conflicts carried by the other modules |
| CP-1 financial base | Accepted | Yes | Consolidated IFRS, USD millions; FY2025 figures from a management release and labelled |
| CP-1A business and transaction register | Accepted | Yes | Readiness judgment for the synthesis: ready with limitations |
| CP-2 credit synthesis | Accepted on the second attempt | Yes | Confidence Medium, inside the cap set by the upstream limits |

All four are current for the as-of date 2026-11-05 and use USD. The latest source is the Q2 2026 release dated 2026-07-29, 99 days before the as-of date. No input is stale against its own period.

### Material claim register and support review

Verdicts: supported (the named evidence states the claim), partly supported (carries part of it or only with a qualification the claim omits), unsupported (does not carry it).

| Claim | Module | Evidence traced | Verdict | Reviewer note |
| --- | --- | --- | --- | --- |
| Total long-term debt 860.2 at 2026-06-30 and 1,008.6 at 2025-12-31, with the instrument split | CP-1, CP-2 | Q2FS page:18; components sum to the printed totals | Supported | Carrying value, with principal 866.4 shown separately |
| Trailing adjusted EBITDA 1,271.6 and the five-point series 995.7, 932.3, 1,060.9, 1,195.6, 1,271.6 | CP-1, CP-2 | PR-Q2 page:25; PR-FY25 page:41; quarterly sum recomputed | Supported | A company non-GAAP measure, labelled |
| Leverage ratios 0.68x, 0.84x, 0.95x, 1.12x, 1.06x total and -0.06x, 0.00x, 0.41x, 0.47x, 0.44x net | CP-1, CP-2 | Inputs from PR-Q2, PR-Q1, PR-FY25, Q3MDA page:74; ratios recomputed | Supported | Company-printed rounded ratios (0.0, 0.4, 0.5) agree |
| Liquidity 1,044.6 and undrawn revolver 153.7 | CP-1, CP-2 | PR-Q2 page:6; Q2FS page:19; 450.0 - 272.0 - 24.3 recomputed | Supported | Facility-level split correctly flagged as not printed |
| 334.5 of cash is restricted to Copper World LLC | CP-1, CP-1A, CP-2 | PR-Q2 page:25; Q2FS page:9 | Supported | |
| Ring-fenced view 0.64x total and 0.20x net, net debt 253.1 | CP-1, CP-2 | Arithmetic on 860.2, 50.7, 890.9, 334.5 | Supported as arithmetic | Labelled an analyst view, not a company or covenant measure |
| Cash of 556.4 is available to the rest of the group | CP-2 | CP-1 derivation 890.9 - 334.5 | Partly supported | The filings say 334.5 is restricted; they do not say the rest is freely available |
| Funded maturities 272.0 (2028), 542.4 (2029), 52.0 (2036 tender); none earlier | CP-1, CP-2 | Q2FS page:14, page:18-20 | Supported | Zero rows rest on the note listing no other funded maturity; municipal final maturity correctly left open |
| Half-year interest cover 24.77x, 17.81x, 10.71x and accrual cover 26.83x | CP-1, CP-2 | Q2FS page:3, PR-Q2 page:24-25; recomputed | Partly supported | Arithmetic is right; the statement that the window holds one coupon date is an inference because coupon dates are not printed |
| Free cash flow and sustaining capital differ between releases (228.2 against 225.0 for Q4 2025) | CP-1, CP-1A, CP-2 | PR-FY25 page:41; PR-Q1 page:25; PR-Q2 page:25 | Supported | The 3.2 difference equals the community-payment difference, as CP-1 states |
| July release prints 290.4 for Q4 2025 cash generated from operations against 209.4 | CP-1 | PR-Q2 page:25; PR-Q1 page:25; the printed trailing total 831.2 sums with 209.4 | Supported | |
| Share count 395,521,903 (40-F) against 396,834,231 (interim note), a difference of 1,312,328 shares | CP-1, CP-1A | 40-F page:1; Q2FS page:23; difference recomputed | Supported | Unresolved in the sources |
| Gold share 38% (management) against 39.9% of contract revenue and 41.6% of reported revenue (derived) | CP-1A, CP-2 | PR-Q2 page:17; Q2FS page:10 | Supported | Management basis is not stated; logged not reconciled |
| First-half cash taxes paid 262.8 equal 35.4% of adjusted EBITDA; effective tax rate 43.1% | CP-1, CP-2 | Q2FS page:2, page:1; recomputed | Supported | |
| Capital commitments 202.6, of which 18.7 not terminable | CP-1 | Q2FS page:29; sums recomputed | Supported | |
| Claims outside debt: leases 53.0, equipment financing 131.3, deferred land payments 102.8, streams, provisions, letters of credit | CP-1 | Q2FS page:15-21 | Supported | Search for factoring, supply chain finance, take-or-pay and retiree medical found none, which I repeated |
| Note guarantees and revolver security exclude Copper World, Mason and Cactus | CP-1, CP-1A, CP-2 | Q2FS page:18-19 quoted | Supported | |
| Municipal bonds are Copper World LLC obligations guaranteed by the parent | CP-1A, CP-2 | Q2FS page:20 quoted | Supported | |
| Mitsubishi holds 30% of Copper World and owes 180.0 within 18 months | CP-1A | Q2FS page:5, page:9; PR-Q2 page:18 | Supported | |
| Arizona Sonoran acquired for 46,794,082 shares, net identifiable assets 1,267.0, land payments 102.8 | CP-1A | Q2FS page:8, page:16; tie recomputed | Supported | The 1,135.6 value cites page 8 in CP-1; it is printed on pages 4 and 23 |
| Mine lives, production outlook, guidance and the stated net debt ceiling | CP-1A, CP-2 | PR-Q1 page:17-18; PR-Q2 page:2; PR-FY25 page:27 | Supported | Tagged Management Language; not adopted as fact |
| Behaviour read Supportive to Neutral or Mixed; legal capacity not assessed | CP-1A, CP-2 | Rows on debt repurchases, dividend, acquisition funding and guarantee perimeter | Supported | Analyst Interpretation; absence of creditor-adverse actions is an absence statement |
| Sound fundamental credit view with Medium confidence | CP-2 | CP-1 tables and CP-1A rows | Supported | Not above what the basis carries |

### Citation trace

| Check | Method | Result |
| --- | --- | --- |
| Verbatim quotes in CP-1A | Each double-quoted span searched in the normalised text of all seven sources, then matched to the page named in its row | 44 of 44 found; each on the page cited |
| Verbatim quotes in CP-0 | Same method | 42 of 42 genuine quotes found; five other matches were pairing artefacts of surrounding text, not quotes |
| Figures in CP-1, CP-1A and CP-2 | Each decimal or comma-grouped number searched in all source text | CP-1: 28 of 456 not in the sources, all derived or reformatted (two are printed as 150 and 180 million); CP-1A: 1 of 45 (a reformatted 180 million); CP-2: 8 of 41, all derived from CP-1 |
| Page locators on figure-bearing lines | Each figure on a line searched on the pages named on that line | Figures sat on the cited pages except where a line mixes pages or sums components; one value (1,135.6) cites the wrong page |
| Derived figures | Each derived number located in a Calculations table | CP-1: seven derived figures sit in text only (148.4, 204.1, 296.3, 3,144.2, 600.0, and the 150.0 and 180.0 reformats); CP-1A: none; CP-2: three (204.1, 24.77, 253.1); the last two are in CP-1's calculations and 204.1 is stated only in CP-1 text |
| Cutoff | Dates after 2026-11-05 | Only labelled future dates (2028, 2029 and 2036 maturities and tender dates, the 18-month Mitsubishi payment, the late 2026 sanction decision) |
| Currency and period labels | Read every table header | USD millions throughout; Canadian-dollar items labelled; quarter, six-month, trailing and full-year labels consistent; no six-month amount used as a full-year figure |

### Figure identity across modules

| Figure | CP-1 | CP-1A | CP-2 | Result |
| --- | --- | --- | --- | --- |
| Total long-term debt 860.2; trailing adjusted EBITDA 1,271.6 | Printed | Not stated | Same | Identical |
| Total debt to trailing adjusted EBITDA | 0.68x | Not stated | 0.68x | Identical |
| Ring-fenced total and net ratios | 0.64x and 0.20x | Not stated | 0.64x and 0.20x | Identical |
| Liquidity 1,044.6 and undrawn revolver 153.7 | Printed | Not stated | Same | Identical |
| Copper World restricted cash | 334.5 | 334.5 | 334.5 | Identical |
| Municipal bonds | 52.0 principal, 50.7 carrying | 52.0 | 52.0 | Identical |
| Deferred land payments from Arizona Sonoran | 102.8 | 102.8 | 102.8 | Identical |
| Funded maturities 2028 and 2029 | 272.0 and 542.4 | Not stated | 272.0, 542.4 and 814.4 | Identical where stated |
| Trailing free cash flow | 413.0 | Not stated | 413.0 | Identical |
| Half-year interest cover | 24.77x | Not stated | 24.77x | Identical |
| Free cash flow version for Q4 2025 | 225.0 later version | 228.2 and 225.0 shown as a conflict | Not stated | Consistent; labelled |
| Gold share of revenue | Not stated | 38% against 39.9% | Disputed, as in CP-1A | Consistent |

### Input currency and scale

All inputs are USD. The statements and releases are stated in millions of US dollars; Canadian-dollar items (the C$130.0 million letter of credit facility and the dividend of C$0.01 per share) are labelled. No scale mismatch was found, for example no millions value written for a thousands source.

### Gap propagation

| Upstream limitation | Carried by CP-1 | Carried by CP-1A | Carried by CP-2 |
| --- | --- | --- | --- |
| Covenant levels not supplied | Yes | Yes | Yes |
| Debt documents and guarantor identity missing | Yes | Yes | Yes |
| Audited FY2025 statements and annual information form missing | Yes | Yes | Yes |
| Nothing dated after 2026-07-29 | Yes | Yes | Yes |
| Facility-level revolver availability not printed | Yes | Not applicable | Yes |
| Full-year cash interest not printed | Yes | Not applicable | Yes |
| Copper World cash restricted | Yes | Yes | Yes |
| Free cash flow version differences and misprinted cell | Yes | Yes | Yes |
| Share count conflict | Yes | Yes | Not stated |

### Findings register

| Finding | Type | Severity | Modules | Effect |
| --- | --- | --- | --- | --- |
| The explanation that half-year interest cover is timing-distorted is an inference because coupon dates are not printed | Partly supported claim | Minor | CP-1, CP-2 | Wording; the ratios recompute and the caveat is cautious |
| Cash of 556.4 described as available to the rest of the group goes beyond the filings, which say only that 334.5 is restricted | Partly supported claim | Minor | CP-2 | Wording; the figure is right as cash outside Copper World |
| Derived figures stated in CP-1 text with no Calculations line (148.4, 204.1, 296.3, 3,144.2, 600.0) | Presentation | Minor | CP-1 | Each reproduces from cited components |
| The 1,135.6 value of shares issued for Arizona Sonoran cites page 8; it is printed on pages 4 and 23 | Locator imprecision | Minor | CP-1 | Figure is right |
| The balance sheet row "Total liabilities (as printed)" is an unlabelled subtotal in the statement; the label appears in the segment note | Labelling | Minor | CP-1 | Figure is right |
| Free cash flow history differs between the February and later releases; the July release misprints one trailing cell; share count differs between the cover and the interim note; municipal bond maturity wording differs; Wheaton stream status unconfirmed; gold share differs from the filed note | Source conflicts, unresolved | Medium | CP-1, CP-1A, CP-2 | Series and per-share inputs must name the version; none is reconciled |
| FY2025 principal debt is reconstructed as 1,014.9 by inference because the February release calls the carrying value 1,008.6 principal | Inferred figure | Minor | CP-1 | Labelled an inference in CP-1 |
| Latest source is 99 days before the as-of date; no Q3 2026 results, sanction decision or later financing is supplied | Information boundary | Medium | All | Conclusions are as of 2026-07-29 evidence |
| Covenant levels, executed debt documents and the Copper World contract are not supplied | Missing decision-critical input | Medium | CP-1, CP-1A, CP-2 | Covenant headroom and legal capacity cannot be assessed; carried as limits |
| The review is not independent of the authors | Process limitation | Medium | All | A second reviewer should compare the handoffs with the sources before external use |

### Cross-module contradictions

None found. Pairs examined and found consistent: low leverage in CP-1 against thin committed liquidity in CP-2 (both rest on the same 860.2, 1,271.6, 153.7 and 1,044.6); no funded maturity before 2028 in CP-2 against the 272.0 revolver draw at the November 2028 facility maturity in CP-1; the ring-fence described in CP-1A against the ring-fenced ratios in CP-1 and CP-2; the supportive behaviour read in CP-1A against the municipal bond parent guarantee it also records; and the cautious Medium confidence in CP-2 against management's reaffirmed guidance, which CP-1A tags as Management Language and does not adopt.

### Verdict and committee use

Committee status: Restricted. The set may be used by a committee as a source-traced starting view with its stated limits, but not as a basis for conclusions on covenant headroom, legal capacity, project funding or events after 2026-07-29. Nothing was found that blocks use: no unsupported claim, no unresolved cross-module contradiction and no figure that fails to recompute. No numeric confidence score is stated here; the review judges lineage as Directly Sourced for statement and release figures, Calculated for derived figures with inputs shown, and Analyst Inference for the ring-fenced view, the interest timing explanation and the behaviour read. The strongest contrary evidence to the Restricted verdict is that every checkable item passed; what would make it win is receipt of the credit agreements, indenture and Copper World contract, which would convert the open legal and covenant items into checked ones.

## Calculations

Re-performed at review time from the cited figures. All ties matched the printed or stated value.

| Check | Inputs | Result |
| --- | --- | --- |
| Debt ties | 539.4 + 270.1 + 50.7; 472.1 + 538.8 - 2.3; 472.5 + 542.4 | 860.2; 1,008.6; 1,014.9, equal to the stated totals |
| Undrawn revolver and liquidity | 450.0 - 272.0 - 24.3; 890.9 + 153.7; 1,003.8 + 425.2 - 472.5 | 153.7; 1,044.6; 956.5, equal to the stated values |
| Net debt | 860.2 - 890.9 - 49.8 | -80.5, equal to the printed value |
| Trailing sums | 321.2 + 421.9 + 385.9 + 142.6; 297.0 + 211.3 + 209.4 + 113.5; 101.8 + 102.3 + 225.0 - 16.1 | 1,271.6; 831.2; 413.0, equal to the printed values |
| Misprinted cell test | 297.0 + 211.3 + 290.4 + 113.5 | 912.2, not equal to the printed 831.2, so 290.4 is inconsistent, as CP-1 states |
| Income and cash flow ties | 219.7 - 13.3 - 4.5 + 48.7 - 10.2; 272.0 - 472.5 + 1.0 - 3.0 - 30.0 - 5.9 - 18.4 - 14.1 + 3.0 + 411.7 - 5.7; 508.3 - 321.1 + 138.1 - 3.3 | 240.4; 138.1; 322.0, equal to the printed values |
| Tax | 912.0 - 564.3; 72.1 + 38.4 + 108.1 + 129.1; 240.4 + 339.0 + 257.1 + 330.5 | 347.7; 347.7; 1,167.0 |
| Acquisition and equity ties | 63.0 + 0.4 + 0.4 + 1,357.0 - 31.0 - 20.0 - 102.8; 396,834,231 + 46,794,082 + 516,447; 422.7 + 169.8 - 461.6 - 11.0 | 1,267.0; 444,144,760; 119.9, equal to the printed values |
| Segment ties | 273.3 + 258.4 + 99.6; 636.3 + 544.9 + 207.4 | 631.3; 1,388.6 |
| Ratios | 860.2 / 1,271.6; -80.5 / 1,271.6; 809.5 / 1,271.6; 253.1 / 1,271.6; 743.1 / 30.0; 532.4 / 29.9; 321.2 / 30.0; 743.1 / 27.7; 296.3 / 450.0; 262.8 / 743.1; 102.3 / 240.4; 249.8 / 579.4 | 0.68x; -0.06x; 0.64x; 0.20x; 24.77x; 17.81x; 10.71x; 26.83x; 65.8%; 35.4%; 42.6%; 43.1%, all as stated |
| Maturity and sensitivity | 272.0 + 542.4; 814.4 / 413.0; 1 - 860.2 / 1,271.6; 528.4 / 27.7 | 814.4; 1.97 times; 32.4%; 19.08x, as stated in CP-2 |
| Gold share | 262.4 / 658.4; 262.4 / 631.3; 289.6 / 739.5 | 39.9%; 41.6%; 39.2%, as stated in CP-1A |
| Source age | 2026-11-05 less 2026-07-29 | 99 days |

## Gaps

| Gap | Missing evidence | Why it matters | Consequence for confidence | Follow-up |
| --- | --- | --- | --- | --- |
| Covenant levels and headroom | Credit agreements and compliance certificates | Headroom is the main test of the low leverage reading | Confidence cannot exceed Medium | Obtain the credit agreements |
| Legal capacity and project recourse | Indenture, credit agreements, Copper World contract, Wheaton agreement | Distributions, asset transfers and project guarantees cannot be tested | The behaviour read rests on actions only | Obtain the executed documents |
| Audited FY2025 statements and annual information form | Exhibits 99.1, 99.2 and 99.3 of the annual report | FY2025 base is second-hand; share count unresolved; ownership and litigation unknown | FY2025 comparisons stay labelled | Obtain the exhibits |
| Evidence after 2026-07-29 | Q3 2026 results and filings to the cutoff | The sanction decision and new financing would change the view | Conclusions are dated | Supply later filings |
| Independent review | A second reviewer | This review shares the authors' session and extraction text | A second reviewer should repeat the trace | Assign a reviewer |
| Extraction fidelity | Comparison against the filed htm | Tables were read from text extraction | Residual table-layout risk | Spot-check against the filings |

## Next module

None. CP-5 is the last requested module. Before external use, a second reviewer should compare the handoffs with the sources, the partly supported statements and presentation defects in the findings register should be corrected in any rerun (new run folder), and the credit agreements, indenture, Copper World documents, audited FY2025 statements and later filings should be added to clear the Restricted status.
