## Request

Issuer: PBF Holding Co LLC (issuer id pbf-holding-co-llc). The filings name the registrant "PBF Holding Company LLC" and its co-registrant "PBF Finance Corporation". The filings are the evidence for the identity; the context file only supplies the short name.

As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. Current period q3-2026, prior period fy-2025 (context). All filed amounts are in USD millions unless a source says otherwise.

Task of this module: source readiness only. It judges whether the pinned source set can support the four requested downstream modules (CP-1 financial extraction, CP-1A business and transaction context, CP-2 fundamental credit synthesis, CP-5 evidence trace and research integrity) and what remains blocked. It gives no credit conclusion, no legal interpretation and no investment opinion, and it normalises, reconciles and calculates no financial figure. Citations below use the form (label page:N "exact substring"), where the label is defined in the Sources table and N is the source chunk number, not the printed page.

Context inputs (not issuer evidence): the context file leaves deal terms, quotes, ratings, valuation inputs, peers, assumptions and research questions empty, names no borrower, parent or guarantors, and states no legal documents attached. Those blanks are not treated as zero.

## Sources

### Issuer sources relied on

| Label | Exact source name | sha256 | Document family and original authority | Period and perimeter | Chunks |
| --- | --- | --- | --- | --- | --- |
| 10K | 10-K_2025-12-31_pbfh-20251231.htm.jsonl | d8cc408b78dbd581d058811f04c883343b35aff7d41a81cb7f7c9a865d63578a | Annual report on Form 10-K, filed financial report (audited statements) | Fiscal year ended 2025-12-31; PBF Holding Company LLC and PBF Finance Corporation combined filing | 216 |
| Q1-10Q | 10-Q_2026-03-31_pbf-20260331.htm.jsonl | 5a4242ec4ab0800289f99b8fb8f699b2f54c974b4153ae81aa21ea53d5f7dce3 | Quarterly report on Form 10-Q, filed financial report (unaudited) | Quarter ended 2026-03-31; PBF Holding and PBF Finance | 59 |
| Q2-10Q | 10-Q_2026-06-30_pbf-20260630.htm.jsonl | 179cd47014072a6b74de2a12abf4417faacecc8413b4c8273ab1ec0f832d5c10 | Quarterly report on Form 10-Q, filed financial report (unaudited) | Quarter ended 2026-06-30; three and six months; PBF Holding and PBF Finance | 69 |
| Q3-10Q | 10-Q_2026-09-30_pbf-20260930.htm.jsonl | aa31b84f94b1c47f81c70abbb0ff7efeca9bcb80852596ec5368223e7eac72e3 | Quarterly report on Form 10-Q, filed financial report (unaudited) | Quarter ended 2026-09-30; three and nine months; PBF Holding and PBF Finance | 84 |
| Q1-PR | EX-99.1_2026-04-30_a991pressreleaseq1-26.htm.jsonl | 104828cb4c23629fde92b78b0620cad588c64bcdee91586fe5ba497364c7f993 | Earnings release exhibit; attributed management narrative with non-GAAP measures | First quarter 2026; issued by PBF Energy Inc., the indirect parent | 17 |
| Q2-PR | EX-99.1_2026-07-30_a991pressreleaseq2-26.htm.jsonl | a7bd74033edd0eddbe8e027b1ef6a171c22d27094099293d640917935e8f4118 | Earnings release exhibit; attributed management narrative with non-GAAP measures | Second quarter 2026; issued by PBF Energy Inc. | 19 |
| Q3-PR | EX-99.1_2026-10-29_a991pressreleaseq3-26.htm.jsonl | ceaca5528b0d3a91964868e4bbffe0689397a5fd5afc2bb6cfc13e308a461219 | Earnings release exhibit; attributed management narrative with non-GAAP measures | Third quarter 2026; issued by PBF Energy Inc. | 20 |

The run context is also pinned: source `context`, sha256 e3f25603b3db519b8b37c6f17fae4507d987050b491cc8f2ad5a0c098cf08361. It holds the user's dated settings and is not issuer evidence.

### Supplied handoffs

None. CP-0 is the first module of this run and CP-OS supplied no upstream handoff.

### Source-by-source assessment

**10K.** The cover names the registrants and the period: (10K page:1 "PBF HOLDING COMPANY LLC PBF FINANCE CORPORATION") and (10K page:1 "For the fiscal year ended: December 31, 2025"). The auditor's opinion covers the issuer's own statements: (10K page:151 "We have audited the accompanying consolidated balance sheets of PBF Holding Company LLC and subsidiaries"). Statements are at 10K page:153 to page:156, debt note at page:172 to page:181, guarantor summarized information at page:136, subsequent events at page:215. Audited statements control FY2025 and FY2024 facts. Observation: the cover prints (10K page:1 "Commission File Number: 001-35764") while the Q3 10-Q exhibit list attributes that number to PBF Energy Inc. current reports (Q3-10Q page:83 "(File No. 001-35764)"); the 10-Qs print file numbers 333-186007 and 333-186007-07. The registrant identity is clear from the cover and the signature block, so this is a labelling observation, not an identity break. A second observation: the page:153 audit report covers only the 2023 statements and is signed by a firm described as predecessor auditor; the FY2025 and FY2024 opinion is at page:151.

**Q1-10Q, Q2-10Q, Q3-10Q.** Each is a PBF Holding and PBF Finance combined 10-Q: (Q1-10Q page:1 "For the quarterly period ended: March 31, 2026"), (Q2-10Q page:1 "For the quarterly period ended: June 30, 2026"), (Q3-10Q page:1 "For the quarterly period ended: September 30, 2026"). The Q3 report was signed (Q3-10Q page:84 "Date: November 3, 2026"), which is before the cutoff. Q1 carries three-month columns, Q2 three- and six-month columns, Q3 three- and nine-month columns, so each quarter has its own three-month income statement. Cash flows are year-to-date only (Q3-10Q page:9 "Nine Months Ended September 30,"). The three 10-Qs are separate period reports, not versions of one another; none supersedes the 10-K. The Q3 10-Q repeats the 2025 year-end balance sheet column and it shows the same figures as the 10-K (Q3-10Q page:8 "Total liabilities and equity $ 15,795.1 $ 11,706.3" and 10K page:154 "Total assets $ 11,706.3 $ 11,231.8"). That agreement of the year-end total assets figure is a consistency observation only, not a reconciliation.

**Q1-PR, Q2-PR, Q3-PR.** These are earnings-release exhibits of the indirect parent, not of the issuer: (Q3-PR page:1 "PBF Energy Inc. (NYSE:PBF) today reported third quarter 2026 income from operations of $2,100.9 million"), (Q2-PR page:1 "PBF Energy Inc. (NYSE:PBF) today reported second quarter 2026 income from operations of $1,272.1 million"), (Q1-PR page:1 "PBF Energy Inc. (NYSE:PBF) today reported first quarter 2026 income from operations of $299.6 million"). They are management-attributed supporting claims and non-GAAP presentations at the parent perimeter. They cannot silently stand in for the issuer's filed statements. They are dated 2026-10-29, 2026-07-30 and 2026-04-30, all before the cutoff. They are used in the pack in place of quarterly presentations; the pack holds no presentation deck, so no slide coverage is claimed or needed.

### Pack-level notes

The retrieval manifest in the pack folder was ignored by CP-OS and is not a source. No duplicate sources are present: seven distinct filings, each for a different period or document type. No source in the pack is a draft; the filings are filed documents. Text extraction succeeded for all seven (each opens with its page:1 text); that is extraction status, not a fidelity review of tables, which are flattened to text lines.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed sources support the requested issuer-level financial, business and evidence-trace work with bounded limitations. The issuer's own filings, not the parent's earnings releases, should carry the numbers. | Medium | The executed notes and credit agreement are not in the pack, and the parent releases use a different perimeter and debt definition than the issuer. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The issuer files its own audited annual and unaudited quarterly statements, covering the 2025 year and the first three quarters of 2026. | Issuer-level debt, earnings and liquidity can be traced to filed statements. | High |
| The earnings releases belong to the parent and show different cash, debt and operating income figures than the issuer filings. | Parent figures could be mistaken for issuer figures if the perimeter is not kept separate. | High |
| Debt changed materially during 2026 and a further redemption followed the quarter end. | The debt picture needs period-end and post-period labelling; the maturity table is only in the annual report. | High |
| The executed indentures and the amended revolving credit agreement are only listed as exhibits. | Covenant and security terms rest on the notes to the filings, not on the legal documents. | Medium |

### Readiness view

Overall view: READY_WITH_LIMITATIONS for the effective source set. The pack supports the requested work on PBF Holding Company LLC because the issuer's own audited annual statements and three unaudited quarterly reports are present, they carry statements, debt, liquidity, covenant, guarantor, related-party and subsequent-event disclosure, and all are dated on or before the 2026-11-05 cutoff. The strongest contrary evidence is perimeter: the three earnings releases describe PBF Energy Inc., and the two perimeters report different cash, debt and operating income, so using the releases for issuer figures would mislabel the entity. A second limitation is that financing terms come only from the notes to the filings; no executed indenture or credit agreement is in the pack, which restricts any legal reading. Source sufficiency is not completion of downstream analysis. This view is source readiness only and does not assert normalised quarters, reconciliation or acceptance of any downstream input contract (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

| Consumer | Readiness | Basis and carried limitations |
| --- | --- | --- |
| CP-1 financial extraction | READY_WITH_LIMITATIONS | Issuer statements for FY2025, FY2024 and FY2023 in 10K page:154; three-month and year-to-date columns in each 10-Q; facility-level debt (Q3-10Q page:17); cash interest and tax paid (Q3-10Q page:10 "Interest (net of capitalized interest of $36.5 and $19.0 in 2026 and 2025, respectively) $ 155.5 $ 145.0"); issuer-level EBITDA reconciliation (Q3-10Q page:59). Limits: cash flows are year-to-date, so discrete quarterly cash flows are a downstream derivation; the debt maturity table is only in the 10-K; the releases are a different perimeter. |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Ownership chain, six-refinery operating model, 2026 refinancings, revolver amendment, hydrogen plants purchase, Martinez fire and insurance recoveries, and subsequent events are all described in the filings. Limits: executed transaction documents are not supplied; the context states no sponsor or deal terms; the 8 May 2026 Chalmette refinery fire is only named as a risk factor. |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Its upstream registers can be built from the evidence above. Limits: no current rating, market price, valuation input or peer set is supplied; the only rating statement is dated to the 10-K and predates the 2026 refinancing. Missing downstream handoffs are not a source condition. |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | Every source is text-chunked with locators, so claim-to-source tracing is possible. Limits: chunk numbers are extraction units, not printed pages; tables are flattened text; no XBRL or original table image is supplied to test table fidelity. |

### Entity and perimeter map

| Entity | Role in the evidence | Locator |
| --- | --- | --- |
| PBF Holding Company LLC | Issuer, "Operating Issuer"; registrant of the 10-K and 10-Qs; wholly owned by PBF Energy Company LLC | (Q3-10Q page:2 "100% of the membership interests of PBF Holding Company LLC were owned by PBF Energy Company LLC") |
| PBF Finance Corporation | Co-issuer and co-registrant; wholly owned by PBF Holding; no independent assets or operations | (Q3-10Q page:69 "The Co-Issuer has no independent assets or operations.") |
| PBF Energy Company LLC ("PBF LLC") | Direct parent of the issuer | (Q3-10Q page:3 "PBF Holding is a wholly owned subsidiary of PBF Energy Company LLC") |
| PBF Energy Inc. | Indirect parent, sole managing member of PBF LLC, consolidates it; issuer of the earnings releases; a party to the 2032 exchangeable notes indenture and registration rights agreement | (Q3-10Q page:3 "PBF Energy operates and controls all of the business and affairs and consolidates the financial results of PBF LLC and its subsidiaries") |
| Guarantor Subsidiaries | Eleven 100% owned subsidiaries guarantee the 2034 7.25%, 2032 exchangeable and 2030 9.875% notes; twelve consolidated subsidiaries are named as non-guarantors | (Q3-10Q page:69 "guarantee the obligations under the 2034 7.25% Senior Notes, the 2032 Exchangeable Notes and the 2030 9.875% Senior Notes") |
| PBF Logistics LP and St. Bernard Renewables LLC | Affiliates outside the issuer's consolidation, with related-party flows | (Q3-10Q page:3 "PBF Logistics GP LLC (“PBFX GP”) is a wholly owned subsidiary of PBF LLC") |

The context names no borrower, parent or guarantors; the filings fill those roles. Unresolved: the revolving credit facility borrower and guarantor set is described as "certain of its wholly owned subsidiaries, as borrowers or subsidiary guarantors" (Q3-10Q page:24 "the Company and certain of its wholly owned subsidiaries, as borrowers or subsidiary guarantors"), and "Excluded Subsidiaries" is defined only in the credit agreement (10K page:181 "Excluded Subsidiaries (as defined in the Revolving Credit Agreement)"), which is not supplied.

Three perimeters appear in the pack and must stay separate:

| Perimeter | Source | Printed items (as printed, not reconciled) |
| --- | --- | --- |
| PBF Holding consolidated | Q3-10Q page:7 and page:8 | (Q3-10Q page:7 "Cash and cash equivalents $ 2,510.6 $ 503.0"); (Q3-10Q page:7 "Long-term debt 1,613.0 2,148.3"); (Q3-10Q page:8 "Income (loss) from operations 1,988.3 158.6 3,428.0 (391.0)") |
| Operating Issuer plus Guarantor Subsidiaries, summarized | Q3-10Q page:70 | (Q3-10Q page:70 "Income from operations 2,632.8 623.7 5,131.8 1,005.3") |
| PBF Energy Inc. consolidated | Q3-PR page:8 and page:1 | (Q3-PR page:8 "Cash and cash equivalents $ 2,544.3 $ 527.9"); (Q3-PR page:8 "Total debt 2,118.4 2,148.3"); (Q3-PR page:1 "third quarter 2026 income from operations of $2,100.9 million") |

### Conflicts and differences to carry forward

1. Debt definition and perimeter at 2026-09-30. The issuer's balance sheet prints long-term debt of 1,613.0 (Q3-10Q page:7 "Long-term debt 1,613.0 2,148.3") and its debt table sums to 1,850.0 principal before deferred financing costs of 63.0 and discount of 174.0 (Q3-10Q page:17 "1,850.0 2,201.6"; "Unamortized discount (174.0) (12.3)"). The parent release prints total debt of 2,118.4 (Q3-PR page:8 "Total debt 2,118.4 2,148.3"). At 2025-12-31 both print 2,148.3, at 2026-09-30 they differ. The sources do not explain the difference. Downstream effect: any leverage, net debt or capitalisation figure must say which perimeter and definition it uses; the two are not reconciled here.
2. Cash at 2026-09-30: issuer 2,510.6 (Q3-10Q page:7) against parent 2,544.3 (Q3-PR page:8). Same effect as above.
3. Operating income for the third quarter of 2026: issuer 1,988.3 (Q3-10Q page:8), parent 2,100.9 (Q3-PR page:1) and summarized guarantor group 2,632.8 (Q3-10Q page:70). Three perimeters, no reconciliation supplied. The same split applies to the second quarter: issuer six-month and three-month columns at Q2-10Q page:8 (Q2-10Q page:8 "Income (loss) from operations 1,193.8 (6.4) 1,439.7 (549.6)") against the parent release (Q2-PR page:1 "second quarter 2026 income from operations of $1,272.1 million"), and for the first quarter (Q1-10Q page:8 "Income (loss) from operations 245.9 (543.2)") against (Q1-PR page:1 "first quarter 2026 income from operations of $299.6 million").
4. Management characterisation. The Q3 release states (Q3-PR page:1 "net debt reduction of 150% as compared to the second quarter of 2026") and (Q3-PR page:2 "approximately $2.1 billion of total debt, and $426 million of net cash"). These are attributed parent claims on the parent definition; they are not recomputed here and are not adopted.
5. Liquidity wording. The issuer states (Q3-10Q page:66 "approximately $3.1 billion of borrowing availability under our Revolving Credit Facility, which includes our cash on hand") and an operational liquidity "over $5.6 billion" made up of cash and availability. The phrase "which includes our cash on hand" leaves it unclear whether availability and cash overlap. The same wording appears at every period (10K page:130, Q1-10Q page:42, Q2-10Q page:54). No borrowing base certificate is supplied to settle it. Downstream effect: liquidity must be quoted as printed, with the ambiguity noted, and not rebuilt.
6. Ratings. The only rating statement is in the 10-K, dated before the 2026 refinancing: (10K page:77 "are rated B1 by Moody’s, BB by S&P, and BB by Fitch"). It lists the 2028 6.00%, 2030 7.875% and 2030 9.875% notes; the first two were redeemed in 2026 (Q3-10Q page:17 shows both at nil), so the statement is stale for the current notes. No rating of the 2034 7.25% notes or the 2032 exchangeable notes is in the pack.

### Subsequent events and period discipline

Events after 2026-09-30 and before the cutoff must stay out of 30 September balances. The Q3 10-Q reports (Q3-10Q page:33 "On October 26, 2026, PBF Holding redeemed all $800.0 million in aggregate principal amount of its outstanding 2030 9.875% Senior Notes") at (Q3-10Q page:33 "The aggregate redemption price of the 2030 9.875% Senior Notes redeemed was approximately $853.4 million"), funded from cash on hand; the 800.0 is still in the 30 September debt table (Q3-10Q page:17). A dividend declared by the parent on 2026-10-29 is also reported at Q3-10Q page:33. Within the third quarter, the revolver was amended and restated on 2026-09-30 (Q3-10Q page:24 "increased the maximum commitment from $3.5 billion to $4.0 billion"). A fire at the Chalmette refinery on 2026-05-08 is named in the Q3 forward-looking factors (Q3-10Q page:5 "the fire on May 8, 2026 at our Chalmette refinery") and, in the Q2 10-Q, as a recent fire (Q2-10Q page:5 "the recent fire on May 8, 2026 at our Chalmette refinery"). Nothing dated after 2026-11-05 is used.

### Source profile checks

- Financial reports: statements, notes, period labels, debt, liquidity and covenants are present in the 10-K and 10-Qs. The segment position is a single reportable segment (Q3-10Q page:34 "Our six oil refineries are aggregated into one reportable segment"), so there is no segment table to extract. Year-end maturity table: (10K page:181 "Total debt outstanding $ 2,201.6"), which predates the 2026 refinancing and is not updated in any 10-Q.
- Covenant evidence: the only financial covenant description is in the 10-K, a springing test (10K page:181 "to be less than 1 to 1"; full text "Consolidated Fixed Charge Coverage Ratio, as defined in the Revolving Credit Agreement") that applies only below a minimum excess availability. The 10-Qs give compliance statements (Q3-10Q page:24 "the Company is in compliance with all covenants, including financial covenants, in all its debt agreements") but no ratio level or headroom. The Q3 10-Q does not restate the test after the 2026-09-30 amendment and says only that the interest rate, letter of credit fees, events of default and indemnification obligations are generally consistent with the prior agreement (Q3-10Q page:24 "customary events of default and indemnification obligations that are consistent with those in the Prior Credit Agreement").
- Earnings releases: reported and non-GAAP figures are at the parent perimeter; quarter versus year-to-date distinction is shown in the tables. The releases give guidance at the parent level (Q3-PR page:3 "Total 925,000 985,000" for fourth-quarter throughput).
- Legal and financing sources: no executed indenture, credit agreement, capped call confirmation or registration rights agreement is in the pack; the Q3 10-Q lists them as incorporated by reference (Q3-10Q page:83 "Amended and Restated Senior Secured Revolving Credit Agreement, dated September 30, 2026 (incorporated by reference"). Terms are therefore known from the filing notes only. No base agreement, amendment, waiver or supplement is collapsed because none is supplied.
- Workbooks, scans, decks: none supplied. No image, chart or speaker-note coverage is claimed.

## Calculations

No financial figure was normalised, reconciled or calculated in this module; the method forbids it. The only arithmetic is coverage counting.

| Item | Inputs | Result |
| --- | --- | --- |
| Total text chunks in the seven issuer sources | 216 + 59 + 69 + 84 + 17 + 19 + 20 (chunk counts in the Sources table) | 484 chunks, each opened in the source files; coverage is by chunk, not a page-count proxy for readiness |
| Issuer-perimeter filings | 10K, Q1-10Q, Q2-10Q, Q3-10Q | 4 of 7 sources |
| Parent-perimeter releases | Q1-PR, Q2-PR, Q3-PR | 3 of 7 sources |
| Latest evidence date against cutoff | Q3 10-Q signed 2026-11-03; Q3 release 2026-10-29; cutoff 2026-11-05 | Both dates fall before the cutoff |

Values quoted in the Findings (for example 2,510.6, 1,613.0, 2,118.4) are copied as printed and are not derived. The difference between two perimeters is deliberately not computed here.

## Gaps

| ID | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | Executed 2034 7.25% notes indenture, 2032 exchangeable notes indenture, 2030 9.875% notes indenture and the amended and restated revolving credit agreement are not in the pack (Q3-10Q page:83). Covenants, security, guarantee mechanics and "Excluded Subsidiaries" cannot be read from the legal text. | Medium | CP-1A, CP-2, CP-5 | Add the executed documents; until then treat note-level descriptions as the only authority and make no legal interpretation. |
| G2 | The issuer-versus-parent differences in debt, cash and operating income are unexplained (Conflicts 1 to 3). | Medium | CP-1, CP-2, CP-5 | Use issuer filings for all issuer figures; label parent figures as parent context; do not mix. |
| G3 | The debt maturity table exists only for 2025-12-31 (10K page:181). The Q3 10-Q has no updated maturity table; maturities after the 2026 refinancings must be built from the Q3 note and the October redemption. | Low | CP-1, CP-2 | Build from the Q3 debt note and mark the October 2026 redemption as a subsequent event. |
| G4 | No revolver borrowing base, excess availability or fixed charge ratio figure is printed in the 10-Qs; liquidity wording on cash overlap is ambiguous (Conflict 5). | Medium | CP-1, CP-2 | Quote liquidity as printed; flag that availability net of letters of credit cannot be rebuilt from the pack. |
| G5 | No current rating, quote, valuation input, peer set or sponsor information is supplied; the 10-K rating statement is stale for the current notes (Conflict 6). | Medium | CP-2 | Treat relative-value inputs as Not supplied; do not infer from stale ratings. |
| G6 | Cash flow statements are year-to-date only; discrete quarterly cash flows and Q4 2025 are not printed. | Low | CP-1 | Derive downstream by subtraction with shown inputs, or state Not calculable. |
| G7 | The 8 May 2026 Chalmette refinery fire is named only as a risk factor; no quantified impact, insurance position or throughput effect was found after searching "May 8", "Chalmette" with fire, outage, incident and unplanned in the 10-Qs and releases. | Low | CP-1A, CP-2 | State Not supplied for impact; do not infer. |
| G8 | Martinez fire investigations and penalties are described as unquantified (Q3-10Q page:14 "the full financial impact of this incident cannot reasonably be estimated"). | Medium | CP-1A, CP-2 | Carry as an open contingency with no amount. |
| G9 | Table fidelity is untested: tables are flattened text, no XBRL or table images are supplied, and chunk numbers are not printed page numbers. | Low | CP-5 | Cite chunk locators as given and say they are extraction units. |
| G10 | The 10-K cover prints a file number that the 10-Q exhibit list attributes to PBF Energy Inc. (identity labelling observation). | Low | CP-5 | Rely on the registrant names and signature block; no action on the evidence. |

## Next module

Proceed to CP-1 on the issuer-perimeter filings (10K, Q1-10Q, Q2-10Q, Q3-10Q) as the figure sources, using the releases only as labelled parent context. CP-1 must carry G2 to G4 and G6: keep issuer and parent figures apart, quote liquidity as printed, treat the 800.0 of 2030 9.875% notes as outstanding at 2026-09-30 and redeemed on 2026-10-26, and keep year-to-date cash flows labelled as year-to-date. CP-1A, CP-2 and CP-5 then follow in the dependency order CP-OS sets, carrying G1, G5, G7 to G9 respectively. DO NOT RUN is not recommended for any consumer.
