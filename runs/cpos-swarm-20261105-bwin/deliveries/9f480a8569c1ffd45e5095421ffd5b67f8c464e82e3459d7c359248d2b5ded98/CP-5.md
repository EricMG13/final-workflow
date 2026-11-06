## Request

Issuer: Baldwin Insurance Group, Inc. (issuer id bwin); as-of date 2026-11-05; pathway credit_snapshot; run bwin-2026-11-05-credit_snapshot-host. Scope: an independent evidence-trace and research-integrity review of the four accepted upstream handoffs, with the pinned filings and releases reopened to check each material claim. The review audits and grades; it does not rewrite the credit view or add issuer analysis.

## Sources

### Issuer sources relied on

The locator `page:N` is the extraction chunk of the named file, not the printed page. The pages cited by the audited modules were reopened for this review.

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_bwin-20251231.htm.jsonl | 435ed820e1dedd05dae93bd87717be3ea65acd13ff9cfffaff7aef178e8494c0 |
| 10-Q_2025-09-30_bwin-20250930.htm.jsonl | 0c90579fda7c87633de78b7017eb30aa8347d6e49afceae9c9779736c12ef751 |
| 10-Q_2026-03-31_bwin-20260331.htm.jsonl | 5f7ff56cb35eb60658f5417d0bba0ed7cf98e6637612d04f68a150a621f88e2d |
| 10-Q_2026-06-30_bwin-20260630.htm.jsonl | c7872b5a0e467a855aa0647c334b01115eb4a8b78c766a2ae8d6dccc7348e147 |
| EX-99.1_2026-02-26_ex991bwinfy2025q4earningsr.htm.jsonl | a080932734c7e6f80d7856122b745700585d5721dda88f2356f627e5082d8b98 |
| EX-99.1_2026-05-04_ex99-1fy2026q1earningsrele.htm.jsonl | e172c6af59bf6e4ced5ad8c6113ef1f6cea50e4c9e4f92d7126f157d6d775038 |
| EX-99.1_2026-07-30_ex99-1fy2026q2earningsrele.htm.jsonl | cbd7cabcbf8fcf9cc1502cda8859930cd02f842bc6bfad19f57059a1a93bf562 |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 8078b6eb19ff2611ca7e63e8361807aa16e370931c16f21c4255d38d5faaa273 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 9bfff3ec79f0002a828742fed2ffc0e0ea83352ff5b4551aef0d1e1eea205802 | Audited: source readiness |
| CP-1 | a5458975838919042f71156b0976b8147a5aa9c8336e2bb8d1b2e7346480b7c9 | Audited: financial base |
| CP-1A | aaa4c70789cd3cfdc949fea5868f142411540baa1417b3f9ed8ec3146b9bc774 | Audited: business, transaction and governance context |
| CP-2 | 9f2ceff3415e82fd0bc498e77403ce681d6f4618dcfe50463eabb6b13b776197 | Audited: fundamental credit synthesis |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream analysis traces well to the filings: figures recompute and calculated ratios carry their inputs. It is usable with restrictions, because covenant support, one governance wording and two earlier uncorrected statements need remediation before committee use. | Medium | The executed debt documents are not supplied, so covenant and legal statements rest on filing summaries, and the file extraction was not fidelity reviewed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every financial figure checked recomputes from the cited pages, and the derived leverage ratios reproduce at 4.59x, 5.01x and 6.30x. | The leverage figures can be relied on as calculations, though not as covenant tests. | High |
| The governance text says the court reinstated the stockholders agreement and that approval rights are back in force, which the filings support only in part. | Insider control is real, but the mechanism is imprecise and needs rewording before committee use. | Medium |
| Two earlier handoffs hold statements corrected later: the legal proceedings summary omitted the stockholder lawsuit, and a Tax Receivable Agreement balance was shown as nil. | A reader of the early handoffs alone would miss a governance fact and a small liability. | High |
| Debt maturities after the January 2026 add-on are derived, not printed, and the quarterly filings word the amortization differently. | The maturity wall is approximate until the credit agreement is supplied. | Medium |
| Covenant headroom, ratings and market data are not supplied, and no module makes a relative value or recovery claim. | Committee use is restricted because leverage cannot be tested against its covenant. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the executed credit agreement and indenture, which matters because the only financial maintenance test, a 7.00x total first lien net leverage covenant, is known from a filing summary with no reported ratio or defined EBITDA, and implies that committee use of the leverage metrics must be restricted until the covenant definition and a compliance figure are supplied. The review found no Critical issue. It found five Material issues, led by an imprecise governance description and by earlier statements that were corrected only in a later handoff, and five Minor issues. The financial figures themselves are well traced: each was reopened on its cited page or recomputed, and the calculated ratios disclose their numerator, denominator, period and the limits on the earnings measure.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_bwin-20251231.htm.jsonl | High: filed, audited annual report | FY2025 with FY2024 and FY2023 | Consolidated Baldwin Insurance Group, Inc. including the operating company | Audited statements, debt note, covenant text, governance and related-party notes, subsequent events, exhibit list | Pre-2026 acquisitions; maturity table pre add-on; exhibits listed but not reproduced | Financial base, business context, synthesis |
| S2 | 10-Q_2025-09-30_bwin-20250930.htm.jsonl | Medium: filed, unaudited | Q3 2025 and nine months 2025 | Same | Interim statements and reconciliation | Not relied on for a cited figure | Background |
| S3 | 10-Q_2026-03-31_bwin-20260331.htm.jsonl | Medium: filed, unaudited | Q1 2026 | Same, including January 2026 acquisitions | Balance sheet, cash flow, debt note, liquidity | Unaudited | Financial base |
| S4 | 10-Q_2026-06-30_bwin-20260630.htm.jsonl | Medium: filed, unaudited; controlling source for 2026-06-30 | Q2 2026 and six months 2026 | Same | Statements, acquisitions, debt, segments, non-GAAP, liquidity, litigation outcome | No covenant text; no principal maturity table | Financial base, business context, synthesis |
| S5 | EX-99.1_2026-02-26_ex991bwinfy2025q4earningsr.htm.jsonl | Medium: management release | Q4 and FY2025 | Company | Pro forma adjusted EBITDA, adjusted free cash flow, repurchase authorization | Management-defined measures | Supporting claims |
| S6 | EX-99.1_2026-05-04_ex99-1fy2026q1earningsrele.htm.jsonl | Medium: management release | Q1 2026 | Company | Q1 highlights and management statements | Management language | Supporting claims |
| S7 | EX-99.1_2026-07-30_ex99-1fy2026q2earningsrele.htm.jsonl | Medium: management release | Q2 2026 | Company | Q2 highlights, reconciliations | Guidance without GAAP reconciliation | Supporting claims |
| C1 | context | Not issuer evidence | Run settings | Run | As-of, cutoff, currency, blank ratings and deal fields | Blanks are not zero | Scope only |

Module Status: Ready with Limitations. Traceability Scope: Top 5. Entity key: issuer id bwin supplied. Missing required inputs: executed legal documents, ratings, any report after 2026-07-30. All four audited modules are accepted and carry the same issuer, as-of date and reporting currency.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage rose to 6.30x total debt to adjusted EBITDA for the last twelve months to 2026-06-30 from 5.01x at FY2025 | CP-1, CP-2 | Principal debt 2,495,045 thousand over Adjusted EBITDA 396,153 thousand | Debt grew with the January 2026 add-on while earnings hold about six months of acquired businesses; it sets tolerance for covenant and refinancing tests | Core of the leverage view | S4 page:38, page:61; S1 page:99, page:165 | Company-defined EBITDA; no pro forma acquired earnings; not the covenant ratio |
| 2 | Earnings quality: adjustments other than interest, amortization and depreciation are 48.6% of last-twelve-months adjusted EBITDA | CP-1, CP-2 | Reconciliation lines and statements | Ratios and cover depend on management addbacks including Tax Receivable Agreement expense and share-based compensation | Changes how leverage and cover are read | S4 page:61; S1 page:99; S7 page:11 | Covenant EBITDA definition not supplied |
| 3 | Liquidity of USD 184.5 million cash and USD 259.4 million undrawn revolver capacity at 2026-06-30 | CP-1, CP-2 | Company-stated figures and balance sheet | Near-term debt service and earnout capacity | Adequacy and narrowing from 477.0 at FY2025 | S4 page:5, page:25, page:74; S1 page:110 | Availability net of letters of credit; any covenant limit on drawing not supplied |
| 4 | Cash claims outside debt: earnouts 346,824, deferred payments 192,500 undiscounted and Tax Receivable Agreement 144,570 (thousand) | CP-1, CP-1A, CP-2 | Balance sheet and contractual obligations table | They compete with debt service and are partly due within one year | Fixed-claim burden exceeds debt total | S4 page:5, page:18, page:19, page:74 | Payment timing for the Tax Receivable Agreement not supplied; purchase accounting provisional |
| 5 | Covenant headroom and legal capacity, including holders' approval rights over debt and dividends | CP-1, CP-1A, CP-2 | 10-K covenant text and stockholders agreement description | Headroom and permitted debt decide default risk and creditor control | Cannot be tested | S1 page:73-75, page:162-164; S4 page:39 | Executed agreements not supplied; application of approvals not disclosed |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 4.59x, 5.01x and 6.30x | CP-1 | Debt and Adjusted EBITDA inputs on cited pages; ratio recomputed here | Yes | High inputs, management EBITDA | Calculated | Supported | Medium | Remediation Needed |
| Addbacks 42.5% and 48.6% of Adjusted EBITDA | CP-1 | Reconciliation lines recomputed to the printed total | Yes | High inputs, management EBITDA | Calculated | Supported | High | Committee-Ready |
| Cash 184.5 and undrawn capacity 259.4 (USD millions) | CP-1 | Company statements at S4 page:74 and arithmetic 600.0 less 302.0 less 38.6 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Earnouts, deferred payments, Tax Receivable Agreement | CP-1, CP-1A | Balance sheet and contractual obligations table | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Covenant headroom and legal capacity | CP-1, CP-1A, CP-2 | 10-K summary of a 7.00x test; no ratio; no agreement | Partial | Medium: summary only | Insufficient Information | Insufficient Information | Low | Remediation Needed |
| Supplementary: approval rights "back in force" after the court ruling | CP-1A, CP-2 | S4 page:39 and S1 page:74-75 | Partial | High source, imprecise reading | Analyst Inference | Partially Supported | Medium | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 2,193,045 and revolver 302,000 at 2026-06-30 | Note 16 fair value of other financial instruments | 10-Q_2026-06-30_bwin-20260630.htm.jsonl | S4 | page:38 | Financial base, chart data leverage | Sourced | High | Label says carrying amount net of discount but the figure equals gross principal; tie shown in Calculations |
| Principal debt 1,435,800 at 2024-12-31 | Fair value table | 10-K_2025-12-31_bwin-20251231.htm.jsonl | S1 | page:181 | Financial base, chart data leverage | Sourced | High | Ties to balance sheet 1,398,054 plus current portion 8,400 plus unamortized costs of about 29.3 million |
| Adjusted EBITDA 312,485, 341,472, 396,153 (LTM) | Adjusted EBITDA reconciliation | S1 and S4 | S1, S4 | S1 page:99; S4 page:61 | Financial base | Sourced and Calculated | Medium | LTM is FY2025 plus six months 2026 less six months 2025 |
| Cash paid for interest 111,397, 115,276, 76,315, 54,528 | Supplemental cash flow information | S1, S4 | S1, S4 | S1 page:135; S4 page:10 | Financial base, chart data interest cover | Sourced | High | Swap settlement treatment not stated |
| Revolver capacity 259.4 and cash 184.5 | Liquidity and capital resources | S4 | S4 | page:74 | Financial base, chart data liquidity | Sourced | High | Excludes fiduciary cash 426,189 |
| Term Loans quarterly payment 4.0 million | Note 10 | S4 | S4 | page:25 | Financial base, chart data debt maturities | Sourced | High | Q1 report words the 4.0 for the incremental loans (S3 page:23) |
| Covenant 7.00x total first lien net leverage | Note 12 | S1 | S1 | page:164 | Financial base, credit synthesis | Sourced | Medium | Summary only; no later compliance statement |
| 2024 Stockholders Agreement in effect after 2026-06-09 | Note 17 legal proceedings | S4 | S4 | page:39 | Business context, synthesis | Sourced | High | "Reinstated" is not the filing's word |
| Holders' approval rights over debt, dividends and bankruptcy filing | Risk factors | S1 | S1 | page:73-75 | Business context, synthesis | Sourced | High | Rights described in the 10-K; application not disclosed |
| Consent agreement terminated and independent committee disbanded | Note 17 | S4 | S4 | page:39-40 | Business context | Sourced | High | Page break splits the sentence |
| Acquisition consideration 1,559,612 and maximum earnout 544,855 | Note 3 | S4 | S4 | page:18 | Business context, synthesis | Sourced | High | Provisional purchase accounting |
| Tax Receivable Agreement liability 144,570 | Balance sheet | S4 | S4 | page:5, page:81 | Financial base, synthesis | Sourced | High | Page:81 prints 144.6 million |
| Tax Receivable Agreement liability 4.5 and 4.8 million before 2026 | Note 19 and tax discussion | S1 | S1 | page:114, page:177 | Business context correction | Sourced | High | Conflicts in wording with S4 page:72 |
| Two carriers about 17% of core commissions and fees | Clients and insurers | S1 | S1 | page:14 | Business context, synthesis | Sourced | High | Carrier names not given |
| Management: CAC integration ahead of plan | Q1 release | EX-99.1_2026-05-04_ex99-1fy2026q1earningsrele.htm.jsonl | S6 | page:1 | Business context | Sourced as Management Language | Medium | Correctly labelled in the audited module |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt / Adjusted EBITDA, LTM 2026-06-30 | CP-1 chart data, CP-2 | 2,495,045 over 396,153, period LTM to 2026-06-30, USD thousands, no normalization | (term loans and notes 2,193,045 plus revolver 302,000) divided by (341,472 plus 253,988 less 199,307) | Calculated | Supported; recomputed 6.298x, rounds to 6.30x | Medium | Leverage, refinancing | S1 page:99, page:165; S4 page:38, page:61 |
| Total debt / Adjusted EBITDA, FY2025 and FY2024 | CP-1, CP-2 | 1,710,606 over 341,472; 1,435,800 over 312,485 | Debt divided by FY Adjusted EBITDA | Calculated | Supported; 5.0095x and 4.5948x | Medium | Leverage | S1 page:99, page:165, page:181 |
| Net debt / Adjusted EBITDA | CP-1, CP-2 | Principal debt less cash and equivalents (fiduciary cash excluded): 2,310,546; 1,586,937; 1,345,755 | Net debt divided by Adjusted EBITDA | Calculated | Supported; 5.83x, 4.65x, 4.31x | Medium | Leverage | S1 page:131; S4 page:5 |
| Adjusted EBITDA / cash interest | CP-1, CP-2 | 312,485/111,397; 341,472/115,276; 396,153/137,063; 199,307/54,528; 253,988/76,315 | Adjusted EBITDA divided by cash paid for interest | Calculated | Supported; 2.81x, 2.96x, 2.89x, 3.66x, 3.33x | Medium | Debt service | S1 page:135; S4 page:10 |
| EBITDA before addbacks | CP-1 | Net income plus interest, income tax and depreciation and amortization | LTM: (131,788) plus 144,698 plus (143,393) plus 188,591 | Calculated | Supported; 58,108 | Medium | Earnings quality | S4 page:7, page:9 |
| Addbacks share of Adjusted EBITDA | CP-1, CP-2 | Adjusted EBITDA less net income, interest, amortization and depreciation | LTM 192,521 over 396,153 | Calculated | Supported; 48.6% | Medium | Earnings quality | S4 page:61 |
| Undrawn revolver capacity | CP-1 | Commitments less drawn less letters of credit | 600.0 less 302.0 less 38.6 | Calculated | Supported; equals the printed 259.4 | High | Liquidity | S4 page:25, page:74 |
| Debt maturity rows 2026 to 2031 | CP-1 chart data | Term Loan 1,593,045 derived; quarterly payments of 4.0; revolver and notes at stated maturities | Scheduled amortization plus bullets; no excess cash flow or prepayment | Assumption-Based | Partially Supported | Low | Refinancing | S4 page:25, page:38; S3 page:23 |
| Cash flow tie, six months 2026 | CP-1 | Operating, investing and financing lines | Sum equals 263,791 printed net increase | Calculated | Supported | High | Cash conversion | S4 page:9 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | Approval rights back in force after the court ruling | The court "reversed"; the filing does not say "reinstated"; the rights over debt and dividends were never reported invalid, and the change is that the consent agreement and independent committee ended | Analyst Inference | Misstates the mechanism behind insider control, a top driver | Reword to the filing's sequence | Business context and synthesis |
| MATERIAL | Maturity rows by year | Derived with a stated assumption; two filings word the 4.0 amortization differently | Assumption-Based | Maturity profile feeds refinancing risk | Confirm schedule from the credit agreement | Financial base chart data |
| MATERIAL | Covenant headroom | No ratio, no defined EBITDA, no agreement | Insufficient Information | Default-risk test cannot be run | Obtain agreement or compliance certificate | Financial base and synthesis |
| MINOR | Locator precision | Three cited pages print a rounded form of the figure cited | Weak Lineage | Reader may not find the exact figure on the page | Cite the page that prints the exact figure | Source readiness, business context, financial base |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | All seven pinned files cover FY2025 to Q2 2026; no executed legal document, rating or post-2026-07-30 report | Legal and market terms rest on summaries | Covenant and capacity claims cannot be verified | Supply executed documents |
| Citation completeness | Ready with Remediation | Every material figure carries a page locator; three locators point to a page printing a rounded form | Minor lookup friction | Does not change a conclusion | Tighten three locators |
| Calculation traceability | Ready with Remediation | Formulas, inputs, periods and tie-outs are shown and recompute; maturity rows rest on an assumption | Derived schedule can shift | Refinancing profile is approximate | Rebuild on the credit agreement |
| Assumption transparency | Committee-Ready | Derived items are labelled as derived; acquired-earnings mismatch disclosed in every module | Reader knows the limit | Leverage is an indicator, not a test | None |
| Markdown and export artifact integrity | Ready with Remediation | Required headings present; two earlier statements corrected only downstream | Consumers of early handoffs may repeat uncorrected text | Governance fact omitted in early handoff | Carry corrections into the report |

Overall auditability: Ready with Remediation (lowest of the five).

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | accepted handoff, run bwin-2026-11-05-credit_snapshot-host | Source readiness for four consumers | Seven pinned files, High to Medium | Six transport headings, reader summary and readiness view present | Pre-audit: accepted | Legal-proceedings summary incomplete |
| CP-1 | accepted handoff, same run | Financial base and four chart tables | Same | Six transport headings, reader summary and financial base view present | Pre-audit: accepted | Tax Receivable Agreement row incomplete |
| CP-1A | accepted handoff, same run | Business, transaction, governance | Same | Six transport headings, reader summary and business and transaction view present | Pre-audit: accepted on second attempt | "Reinstated" wording |
| CP-2 | accepted handoff, same run | Fundamental credit synthesis | Upstream only | Six transport headings, reader summary and credit view present | Pre-audit: accepted | Repeats "back in force" |

Module Status: Ready with Limitations.

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-2 | Business view says the court "reinstated" the stockholders agreement; summaries say approval rights are "back in force" | Partially Supported | S4 page:39 says the court reversed the lower court and that the 2024 agreement has since sprung into effect; S1 page:74 shows the holders' consent was given under a consent agreement through the independent committee; S4 page:39-40 shows both ended. The change is the end of that override, not the reinstatement of rights over debt and dividends | Reword: holders' approval rights over debt, dividends and a bankruptcy filing apply directly again after the consent agreement and independent committee ended | Restricts Committee Use |
| MINOR | CP-0, CP-1, CP-1A | Cash 123,669 cited to a page printing 123.7 million; Tax Receivable Agreement 144,570 cited to a page printing 144.6 million; 9,805 assumed premium cited to a page printing 9.8 million | Partially Supported | The exact figure is on a different page (S1 page:131; S4 page:5; S4 page:20) | Cite the page that prints the exact figure | Formatting / Hygiene Only |

Other claims sampled and found Supported: leverage inputs, addback lines, debt terms, acquisition consideration, segment tables, carrier concentration, related-party amounts, the 7.00x test, the fiduciary balance tie and every quotation in the business context handoff.

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | Total debt / Adjusted EBITDA of 6.30x mixes full acquisition debt with about six months of acquired earnings and uses company-defined EBITDA | Differs from the covenant total first lien net leverage on defined Consolidated EBITDA (S1 page:163-164) | Pro forma adjusted EBITDA exists only for FY2025 and excludes the 2026 acquisitions (S5 page:15) | Label as an indicator; rebuild when pro forma EBITDA and the covenant definition are supplied | Requires Calculation Rebuild |
| MATERIAL | CP-1 | Debt maturity rows by year are derived | Assumes 4.0 per quarter with no prepayment; Q1 note words 4.0 for incremental loans (S3 page:23) and Q2 note for all Term Loans (S4 page:25); 10-K 2.5 per quarter (S1 page:165) | Amortization wording differs between quarters | Confirm the schedule from the executed agreement | Requires Source Reconciliation |
| MINOR | CP-2 | USD millions rounded to one decimal from thousands | 544,855 thousand shown as 544.9 million | None | State the rounding in each module | Formatting / Hygiene Only |

Recomputed without finding an error: leverage and net leverage, interest cover, LTM sums, EBITDA before addbacks, addback shares, undrawn revolver capacity at four dates, term loan principal on two routes, the cash flow tie and the unrestricted cash tie. The interest expense difference between the income statement and the reconciliation is disclosed in CP-1 and is not a defect.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-1A, CP-2 | Single financial maintenance covenant at 7.00x total first lien net leverage; first-lien ranking; guarantor and collateral description; holders' approval rights | Executed JPM Credit Agreement and Amendments 1 to 4, the 2024-05-24 indenture and the stockholders agreements (S1 page:196-200) | Only filing summaries are supplied; no compliance ratio after FY2025; test conditions and defined EBITDA unknown | Obtain the documents; until then label each as a filing summary | Legal review required before any covenant or creditor-rights conclusion |

The modules correctly separate contractual provision, interpretation and implication, and make no recovery or ranking conclusion beyond what the filing states.

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | No audited module makes a price, spread, yield, rating or relative value claim; fair value of debt is quoted only as a filing fact | Ratings, quotes and peers are blank in the context | No market inputs supplied | None now; supply if relative value is wanted | Monitoring follow-up; no current effect |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-0, CP-1 against CP-1A | CP-0 says legal proceedings are ordinary course (S4 page:38) and omits the stockholder lawsuit at page:39; CP-1 shows Tax Receivable Agreement liabilities as nil at FY2025 although 4.5 million sits in accrued expenses (S1 page:177) and says they were first recognized as probable in 2026 | The accepted early handoffs cannot be edited; CP-1A states the corrections | Carry the corrections into the report; do not cite the early statements alone | A reader of CP-0 or CP-1 alone misses the lawsuit and a small liability |

The source-level wording conflict on whether Tax Receivable Agreement liabilities were recorded before 2026 (S1 page:114 against S4 page:72) is logged in the business context handoff with both spans and is preserved here, not reconciled; it is not a separate issue. Consistent across modules: issuer name, as-of date, currency, perimeter (consolidated, no stand-alone borrower statements), leverage, cover and liquidity figures, debt terms, acquisition consideration, claims outside debt, and the open gaps. No contradictory conclusion was found.

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Duplicative content | The leverage, claims-outside-debt and governance points are restated in each module's summary, narrative and risk list | Keep one statement in the report and refer to it | Length only |

No promotional language was found; management claims are labelled Management Language.

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Envelope and headings | The older YAML envelope and legacy section names are replaced in this run by the transport's six headings, reader summary and a module-specific view heading; each audited handoff carries these | None under this transport | None |

Evidence trace: no orphan claim was found. Each material conclusion has a locator or is labelled Insufficient Information.

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1A, CP-2 | Partially Supported Claim | "Reinstated" and "back in force" misdescribe the mechanism behind holders' approval rights | Reword using the consent agreement sequence | Restricts Committee Use | Open |
| CP5-002 | MATERIAL | CP-0, CP-1 | Version Conflict | Early statements on legal proceedings and Tax Receivable Agreement corrected only in a later handoff | Carry corrections into the report | Requires Source Reconciliation | Open |
| CP5-003 | MATERIAL | CP-1, CP-1A, CP-2 | Legal Support Gap | Covenant, ranking, guarantor and approval-right statements rest on filing summaries | Obtain executed documents | Requires Legal Review | Open |
| CP5-004 | MATERIAL | CP-1, CP-2 | Formula / Definition Drift | 6.30x uses company EBITDA with partial acquired earnings, not the covenant definition | Label as indicator; rebuild with pro forma and covenant EBITDA | Requires Calculation Rebuild | Open |
| CP5-005 | MATERIAL | CP-1 | Source Quality Limitation | Maturity rows are derived and quarterly amortization wording differs between filings | Confirm schedule from the credit agreement | Requires Source Reconciliation | Open |
| CP5-006 | MINOR | CP-0, CP-1, CP-1A | Citation Gap | Three locators point to pages printing a rounded form | Cite the exact page | Formatting / Hygiene Only | Open |
| CP5-007 | MINOR | CP-1, CP-1A, CP-2 | Duplicative / Immaterial Content | Same points restated in several sections | Condense in the report | Formatting / Hygiene Only | Open |
| CP5-008 | MINOR | CP-0, CP-1, CP-1A, CP-2 | Markdown/export Consistency Defect | Transport headings replace the legacy envelope | None | Formatting / Hygiene Only | Open |
| CP5-009 | MINOR | CP-1, CP-1A, CP-2 | Market Data Gap | No ratings or market inputs; no market claim made | Supply if relative value is wanted | Monitoring Follow-Up | Open |
| CP5-010 | MINOR | CP-2 | Formula / Definition Drift | Millions rounded from thousands without a stated rule in each module | State the rounding | Formatting / Hygiene Only | Open |

#### Remediation priority map

- Must-fix before committee: CP5-001 (reword the governance mechanism), CP5-003 (obtain the executed debt documents), CP5-004 (label the leverage ratio as an indicator and rebuild with pro forma and covenant EBITDA).
- Must-fix before the canonical handoffs are consumed downstream: CP5-002 (carry the corrected legal proceedings and Tax Receivable Agreement statements into the report) and CP5-005 (confirm the maturity schedule).
- Monitoring follow-up: CP5-009 (ratings and market data if relative value is requested).
- Formatting and hygiene: CP5-006, CP5-007, CP5-008 and CP5-010.

#### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 5. Minor Issues: 5. Committee Use: Restricted.

No Critical issue was found, since every financial figure recomputes and no claim is fabricated, but five Material issues, led by the governance wording and the covenant evidence gap, require correction or disclosure. The quality status is Restricted under the severity rule for Material issues. A numeric confidence score is not emitted because the shared scoring script is outside this transport and no formula is invented; the band is Medium.

## Calculations

Independent recomputation performed in this review, in USD thousands unless stated, from the cited pages. Each result agrees with the audited module.

| Check | Inputs and locator | Result |
| --- | --- | --- |
| LTM Adjusted EBITDA | 341,472 + 253,988 - 199,307 (S1 page:99; S4 page:61) | 396,153 |
| LTM cash interest | 115,276 + 76,315 - 54,528 (S1 page:135; S4 page:10) | 137,063 |
| Principal debt including revolver | 1,435,800; 1,603,606 + 107,000; 2,193,045 + 302,000 (S1 page:165, page:181; S4 page:38) | 1,435,800; 1,710,606; 2,495,045 |
| Total debt / Adjusted EBITDA | 1,435,800/312,485; 1,710,606/341,472; 2,495,045/396,153 | 4.59x; 5.01x; 6.30x |
| Net debt / Adjusted EBITDA | (1,435,800 - 90,045)/312,485; (1,710,606 - 123,669)/341,472; (2,495,045 - 184,499)/396,153 | 4.31x; 4.65x; 5.83x |
| Adjusted EBITDA / cash interest | 312,485/111,397; 341,472/115,276; 396,153/137,063 | 2.81x; 2.96x; 2.89x |
| Reconciliation to printed Adjusted EBITDA | Net income plus every listed line, six periods (S1 page:99; S4 page:61) | Each equals the printed total |
| Gross debt tie, 2024-12-31 | 1,398,054 + 8,400 + about 29,300 of unamortized costs (S1 page:131, page:160, page:182) | About 1,435,800, equal to the fair value table |
| Gross debt tie, 2026-06-30 | 2,150,725 + 16,091 + 26,229 (S4 page:5, page:23, page:38) | 2,193,045 |
| Cash flow tie, six months 2026 | Sum of reported cash flow lines (S4 page:9) | 263,791 |
| Unrestricted cash tie | 263,791 - (426,189 - 223,228) | 60,830, equal to 184,499 - 123,669 |
| Consideration | 1,220,213 + 287,370 + 52,029 (S4 page:18) | 1,559,612 |

## Gaps

Readiness status: Ready with Limitations. Revision history: no earlier CP-5 attempt. The ledger below is the gaps ledger for this review.

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed credit agreement, indenture and stockholders agreements not supplied | Clause-level support for the 7.00x test, definitions, baskets, guarantors, collateral and approval rights | Covenant and creditor-rights conclusions cannot be verified | Leverage view and governance view | High impact | Documents named in S1 page:196-200 |
| CP-5-GAP-002 | Covenant ratio and compliance after FY2025 not reported | Compliance certificate or filing statement | Headroom unmeasured | Leverage and liquidity | High impact | Credit agreement and compliance certificate |
| CP-5-GAP-003 | Pro forma adjusted EBITDA for the 2026 acquisitions not supplied | Management pro forma or run-rate figure | The 6.30x cannot be adjusted | Leverage | High impact | Company disclosure |
| CP-5-GAP-004 | Principal maturity table at 2026-06-30 and exact amortization schedule not printed | Maturity table or agreement schedule | Maturity wall approximate | Chart data debt maturities | Medium impact | Credit agreement |
| CP-5-GAP-005 | How holders' approval rights were applied to the 2025 and 2026 debt additions not disclosed | Proxy or board disclosure | Legal capacity to add debt unclear | Governance | Medium impact | Proxy statement |
| CP-5-GAP-006 | Ratings, quotes and peers blank in the context | Rating reports and market data | No external cross-check | Assessment | Medium impact | Rating agencies and market data |
| CP-5-GAP-007 | No report after 2026-07-30 | Later filings if filed before the cutoff | Events to 2026-11-05 are not covered | All modules | Medium impact | Later filings |
| CP-5-GAP-008 | Extraction fidelity not reviewed; chunk locators are not printed page numbers | Spot check against the original htm | Table flattening could hide an error | All figures | Low impact | Original filings |
| CP-5-GAP-009 | Segment adjusted EBITDA and Tax Receivable Agreement payment timing not supplied | Segment disclosure and payment schedule | Segment cash earnings and cash-call timing unknown | Business and liquidity view | Medium impact | Later filings |

## Next module

No further analytical module follows. The report is composed from the four accepted handoffs. It should carry the Restricted committee use, state the five Material issues and the corrections to the legal proceedings and Tax Receivable Agreement statements, describe the governance mechanism using the consent agreement sequence, present the leverage ratios as indicators on company-defined earnings, and keep the covenant headroom, executed documents, ratings and later-period events as open gaps.
