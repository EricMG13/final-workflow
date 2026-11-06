## Request

Source-readiness review for AMERICAN AIRLINES, INC. (issuer id american-airlines-inc), as of 2026-11-05, pathway credit_snapshot, reporting currency USD, current period Q3 2026 against FY2025. The question is whether the supplied source set can support the requested downstream modules (CP-1, CP-1A, CP-2, CP-5) and what remains blocked. This module gives no credit conclusion and calculates nothing. The cutoff is 2026-11-05; the latest dated evidence is the Q3 2026 Form 10-Q signed 2026-10-22, so no source is dated after the cutoff.

The context file is the user's settings, not issuer evidence. It leaves ratings, quotes, deal terms, valuation inputs and research questions empty; none is treated as zero.

## Sources

### Issuer sources relied on

| Source file | sha256 | Document family and authority | Perimeter and period |
| --- | --- | --- | --- |
| 10-K_2025-12-31_aal-20251231.htm.jsonl | 241cb406125cf4a40a3dec4d315c7a8e709f73f5f12957d46a28f056de7b338c | Annual report on Form 10-K, filed statements, audited (KPMG LLP), controlling for FY2025 facts | Combined filing of American Airlines Group Inc. (AAG, parent) and American Airlines, Inc. (American, the issuer); AAG statements in Item 8A, American statements in Item 8B; FY2025 |
| 10-Q_2026-03-31_aal-20260331.htm.jsonl | bd54f0ef7be7c4905b1acb2a15d1e60b5211836b6a174b954a6d8e979771d4f3 | Quarterly report on Form 10-Q, unaudited filed statements | Combined AAG and American; quarter ended 2026-03-31 (Q1 2026) |
| 10-Q_2026-06-30_aal-20260630.htm.jsonl | e590d34e327bfac4cc2a446c7444656df89c4b6aac523f8df741e9c71b1ace9a | Quarterly report on Form 10-Q, unaudited filed statements | Combined AAG and American; quarter and six months ended 2026-06-30 (Q2 2026, H1 2026) |
| 10-Q_2026-09-30_aal-20260930.htm.jsonl | edb09356472b6a21c11979d0ace904761af85e302b5218542813aede49a0decc | Quarterly report on Form 10-Q, unaudited filed statements | Combined AAG and American; quarter and nine months ended 2026-09-30 (Q3 2026, nine months 2026) |
| EX-99.2_2026-04-23_earningspresentation.htm.jsonl | 9a2e0cf77a5348cca76e4e1fa089b91044513dded2916dcf498cbc76a4f142fe | Earnings presentation (Exhibit 99.2), management claims, non-GAAP | AAG consolidated only; Q1 2026 |
| EX-99.2_2026-07-23_earningspresentation.htm.jsonl | 60d450333d317c8f5bcb2c0834ff53272fd96fa253d4a67d36813c30742d7ee9 | Earnings presentation (Exhibit 99.2), management claims, non-GAAP | AAG consolidated only; Q2 2026 |
| EX-99.2_2026-10-22_earningspresentation.htm.jsonl | ce6723a4b2e59ac217d38de9b2fa855bbf5fa9fd11b713b0732222688fa7865b | Earnings presentation (Exhibit 99.2), management claims, non-GAAP | AAG consolidated only; Q3 2026 |

The pack also holds a retrieval index file, which CP-OS ignores; it is not evidence. The first page of each text file records a sha256 of the original HTML; the hashes above are those of the supplied text files and are the ones CP-OS pins. Identity, family and period below are taken from located content, not from file names.

### Context

| Item | sha256 |
| --- | --- |
| context (user settings, not issuer evidence) | 4315193a9d24f5f5ddc6f4bf134c08d91788bf1e14ed0a34e81f98521fa4fc9b |

### Handoffs

No upstream handoff is supplied to this module. It is the first module of the run.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings are enough to analyse the issuer itself: the annual report and three quarterly reports each carry separate statements and notes for American Airlines, Inc. Downstream work can proceed with stated limits. | Medium | No debt agreements, indentures or rating reports are supplied, and the earnings decks cover only the parent group. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The issuer files its own audited annual and unaudited quarterly statements inside combined filings with the parent. | Issuer-level debt, liquidity and earnings can be read directly; parent figures serve as context only. | High |
| Earnings decks and their net debt reconciliation describe the parent group, not the issuer. | Deck leverage and net debt must not be applied to the issuer without the filing figures. | High |
| Debt covenants are described only in summary form in the filings; no executed agreement is supplied. | Covenant headroom and collateral terms cannot be tested beyond management's compliance statement. | Medium |
| Slides were read as extracted text; charts and images were not inspected. | Chart-only data points in the decks stay unverified. | Medium |

### Readiness view

The effective source set is sufficient to start all four requested modules on the issuer perimeter, each with bounded limitations (READY_WITH_LIMITATIONS). The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This is a statement about sources, not about completion of downstream analysis, and no normalisation or reconciliation was done here. No consumer is CONDITIONAL or BLOCKED, because the issuer-level statements, debt notes, liquidity tables and subsequent-event disclosure are located; the missing items listed under Gaps narrow the work but do not prevent it.

### Source assessment

#### Combined-filing perimeter

The annual and quarterly reports are joint filings by the parent and the issuer, so every figure must be read with its perimeter. Evidence: the 10-K states the joint filing and its split. Mechanism: the same page of text carries parent and issuer numbers, so a careless read can attribute parent debt or earnings to the issuer. Consequence: downstream modules must take issuer figures from Item 8B of the 10-K and Item 1B of each 10-Q.

| Evidence | Locator | Quote |
| --- | --- | --- |
| Joint filing of parent and wholly-owned subsidiary | 10-K_2025-12-31_aal-20251231.htm.jsonl page:4 | "This report is filed by American Airlines Group Inc. (AAG) and its wholly-owned subsidiary American Airlines, Inc. (American)." |
| Issuer is a wholly-owned subsidiary of the parent | 10-K_2025-12-31_aal-20251231.htm.jsonl page:2 | "there were 1,000 shares of American Airlines, Inc. common stock outstanding, all of which were held by American Airlines Group Inc." |
| Issuer statements are separate in the annual report | 10-K_2025-12-31_aal-20251231.htm.jsonl page:3 | "Item 8B. Consolidated Financial Statements and Supplementary Data of American Airlines, Inc." |
| Issuer statements are separate in the Q3 10-Q | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:2 | "Item 1B. Condensed Consolidated Financial Statements of American Airlines, Inc." |
| Issuer balance sheet located (Q3 2026) | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:26 | "AMERICAN AIRLINES, INC. CONDENSED CONSOLIDATED BALANCE SHEETS" |
| Issuer audit report located (FY2025) | 10-K_2025-12-31_aal-20251231.htm.jsonl page:199 | "We have audited the accompanying consolidated balance sheets of American Airlines, Inc. and subsidiaries" |

The issuer statements for the other two quarters are at 10-Q_2026-03-31_aal-20260331.htm.jsonl page:21 to page:23 and 10-Q_2026-06-30_aal-20260630.htm.jsonl page:25 to page:26. The issuer's own debt note is at 10-K page:217 and 10-Q Q3 page:30 to page:31; the issuer's financing narrative for 2026 is at 10-Q Q3 page:32 to page:36.

#### Authority and extraction fidelity

Filed statements control their facts; the decks are attributed management support. The text extraction is complete enough to locate every statement named above; that is extraction status, not a fidelity review of table cells against the original filing. Tables arrive as flattened text, so column alignment (for example AAG versus American columns in the liquidity table) must be confirmed by the consumer from the column headers.

| Evidence | Locator | Quote |
| --- | --- | --- |
| Liquidity table carries AAG and American columns side by side | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:59 | "AAG American" |
| Issuer liquidity row with undrawn facilities and total | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:60 | "Total available liquidity $ 11,797 $ 9,233 $ 11,763 $ 9,213" |

The row above has four value columns: AAG at 2026-09-30 and 2025-12-31, then American at the same dates, per the headers on page:59. That ordering is read from the headers; it is not recomputed here.

#### Earnings presentations

The three decks are Exhibit 99.2 to the parent's results releases and are about AAG only. Evidence: the Q3 deck defines its net debt on a parent group basis. Mechanism: the reconciliation starts from group debt, leases and pensions and subtracts group cash, so it cannot be an issuer figure. Consequence: deck net debt, leverage targets and outlook are parent-level claims to be used as context and labelled so.

| Evidence | Locator | Quote |
| --- | --- | --- |
| Deck presents the parent | EX-99.2_2026-10-22_earningspresentation.htm.jsonl page:1 | "American Airlines Group Inc. THIRD-QUARTER 2026 FINANCIAL RESULTS" |
| Net debt definition and reconciliation | EX-99.2_2026-10-22_earningspresentation.htm.jsonl page:10 | "net debt is defined as total debt, net of unrestricted cash and short-term investments" |
| Management target, attributed claim | EX-99.2_2026-10-22_earningspresentation.htm.jsonl page:6 | "Remain committed to achieving our 3.0x net debt1 to EBITDAR target." |
| Outlook, forward-looking | EX-99.2_2026-10-22_earningspresentation.htm.jsonl page:6 | "FY 2026E Adjusted loss per diluted share1" |

The Q1 2026 deck carries its own total and net debt table (EX-99.2_2026-04-23 page:11); the Q2 2026 deck has no total debt or net debt table (a search of its text for debt returns only forward-looking risk language and a special-items footnote). The decks give guidance on a forward fuel curve, which is management expectation, not fact.

#### Debt, liquidity and covenant evidence

The latest filing prints issuer liquidity, issuer financing activity for 2026 and a covenant summary. Evidence: the covenant paragraph names a minimum liquidity covenant, collateral coverage tests and a debt service coverage test on the AAdvantage financing, and states compliance at the latest measurement dates. Mechanism: the filing gives the existence of the tests but not the executed definitions, levels per facility or measured values. Consequence: the downstream liquidity and covenant work can state the tests and management's compliance statement but cannot compute headroom.

| Evidence | Locator | Quote |
| --- | --- | --- |
| Minimum liquidity covenant | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:61 | "contain covenants requiring us to maintain an aggregate of at least $2.0 billion of unrestricted cash and cash equivalents and amounts available to be drawn under revolving credit facilities" |
| Collateral coverage and LTV tests | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:61 | "contain loan to value (LTV) or collateral coverage ratio covenants" |
| Compliance statement | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:61 | "As of the most recent applicable measurement dates, we were in compliance with each of the foregoing covenants." |
| Cargo receivables facility expiry within twelve months of the cutoff | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:31 | "$50 million of available borrowing capacity under a cargo receivables facility that is scheduled to expire in December 2026" |
| Revolver extension in 2026 | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:46 | "extended the maturity of each facility from June 2029 to March 2031" |
| Debt refinancings during 2026 | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:45 | "prepaid in full $1.0 billion of the outstanding principal amount of the 8.50% senior secured notes" |

#### Subsequent events and cutoff

The annual report's subsequent-events note (10-K page:257, Note 16 for the issuer) describes first quarter 2026 events: the redemption notice on the 8.50% senior secured notes and the fourth amendment to the AAdvantage term loan. These are post year-end events, labelled as such, and are later reflected in the Q1 to Q3 10-Qs. The Q3 10-Q contains no subsequent-events note (a search of its text for the term returns nothing), and nothing in the pack is dated after 2026-10-22. Events between the Q3 10-Q date and the cutoff are therefore not covered by any supplied document.

| Evidence | Locator | Quote |
| --- | --- | --- |
| Post year-end events in the annual report | 10-K_2025-12-31_aal-20251231.htm.jsonl page:257 | "16. Subsequent Events 8.50% Senior Secured Notes In the first quarter of 2026, American sent irrevocable notice of redemption" |
| Q3 10-Q signature date | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:73 | "Date: October 22, 2026" |

### Consumer assessment

| Consumer | Status | Evidence demand and basis |
| --- | --- | --- |
| CP-1 (financial and credit data) | READY_WITH_LIMITATIONS | Needs issuer statements, debt and liquidity detail, period labels and quarter versus year-to-date distinctions. Located for FY2025 and each 2026 quarter at issuer level. Limits: tables are flattened text; letters of credit drawn on facilities at interim dates are not printed; executed facility terms are not supplied. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Needs ownership, operating model and recent change. The 10-K business section and the 10-Q management discussion supply these at parent and mainline level. Limits: no transaction documents; context lists no deal terms. |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Draws only on the CP-1 and CP-1A handoffs, so its source dependency is the same as theirs. It inherits their limits and the perimeter rule. |
| CP-5 (evidence trace) | READY_WITH_LIMITATIONS | Needs every cited locator to resolve in the pinned text. All pages are text-extracted and addressable by page number. It inherits the limits above. |

For a later HTML Model objective the sources cover three discrete 2026 quarters (the three 10-Qs, each with year-to-date amounts), FY2025 from the 10-K, special items, facility-level debt and carrying values in the debt notes, and cash-paid interest (the issuer cash flow statement prints interest paid, net, at 10-Q Q3 page:27). Cash-paid tax was not located and is not assumed. Source sufficiency only is asserted; no quarter is normalised here.

## Calculations

None. CP-0 does not normalise, reconcile or calculate. Every amount quoted above is reproduced from its cited locator without arithmetic.

## Gaps

### Source gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No executed debt documents (credit and guaranty agreements, indentures, EETC documents) are supplied; the 10-Q exhibit list only incorporates some by reference to Current Reports on Form 8-K, which are not in the pack. Context lists legal documents as none. | Medium | CP-1, CP-2, CP-5 | Supply the credit agreements and indentures if covenant definitions, guarantors and collateral are needed. |
| Covenant levels and measured values are summarised only; no compliance certificate or per-facility test. | Medium | CP-1, CP-2 | Obtain facility documents or state headroom as Not calculable. |
| Letters of credit outstanding under revolving facilities at interim dates are not printed in the 10-Qs. A text search of the Q3 10-Q for letters of credit and standby returns nothing; the 10-K reports none outstanding under the 2013 and 2014 revolving facilities at 2025-12-31 (page:162 and page:163). | Low | CP-1 | Use undrawn facility totals as printed and flag the date gap. |
| The decks are parent only; deck net debt, leverage target and outlook are not issuer measures. | Medium | CP-1, CP-2 | Label as parent context; use filing figures for the issuer. |
| Slides were read as extracted text only. Chart and image content, and speaker notes, were not inspected. | Low | CP-1, CP-5 | Use the filings for the same data. |
| Table layout is flattened; side-by-side AAG and American columns need header-based reading. | Low | CP-1, CP-5 | Confirm each issuer figure against column headers. |
| No documents cover 2026-10-23 to the cutoff 2026-11-05 (no Form 8-K or other filing in the pack after the Q3 10-Q). | Low | CP-1A, CP-2 | Treat events after the Q3 10-Q as Not supplied. |
| No credit ratings, market quotes or valuation inputs in the context; none appear in the pack as a rating-agency source. | Low | CP-2 | Do not infer ratings; state Not supplied. |

### Conflicts and identity points

| Item | Locators | Downstream effect |
| --- | --- | --- |
| The context names the country as Cayman Islands, but the filings state that American Airlines, Inc. is a Delaware registrant with principal offices in Fort Worth, Texas. | 10-K_2025-12-31_aal-20251231.htm.jsonl page:1 ("Delaware 13-1502798" and "1 Skyview Drive, Fort Worth, Texas 76155") | Domicile in the filings controls; the context country is not issuer evidence and should not appear in the report as a fact. |
| The context leaves parent_name, guarantors and borrower blank. The filings identify AAG as parent. Guarantor identities per instrument are not supplied in the pack. | 10-K page:2; context | Parent named from the filing; guarantors stay a gap. |
| The 10-K reports AAG and American separately with slightly different figures (total operating revenues differ between the AAG and American selected data tables). | 10-K_2025-12-31_aal-20251231.htm.jsonl page:105 and page:107 | Use the Item 8B figures for the issuer; do not mix the two columns. |

### Version relationships

Each source is a distinct period and none supersedes another: the 10-K covers FY2025, and the three 10-Qs cover Q1, Q2 and Q3 2026 with year-to-date amounts that include earlier quarters. No amendment (10-K/A or 10-Q/A) is in the pack. No duplicate documents were found; the three decks are different quarters.

## Next module

Proceed to CP-1 on the issuer perimeter. Instruct it to take issuer figures from Item 8B of the 10-K and Item 1B of each 10-Q, to label parent figures as context, to keep quarter, year-to-date and FY2025 amounts separate, to cite page numbers as chunks of the pinned text, and to carry forward the gaps above: no executed debt documents, no per-facility covenant levels, no interim letters of credit and no events after the Q3 10-Q.
