SECTION: S11-earnings-financial   PASS: adversarial
COVERAGE: read fully: earnings.py, statement_compose.py, unit_maps.py, pdf_headers.py, inline_xbrl.py, html_text.py, statement_lines.py, financial_series.py, liquidity_series.py, restructuring_series.py / skimmed: financial_workflow.py (unit location, header/column mapping 396-720, 1200-1720, expand_unit_maps), earnings_workflow.py (compose_delta, _column_periods, _source_issues, helpers 1000-1180, 1638-2266) / not read: the rest of financial_workflow.py and earnings_workflow.py (the receipt, verify, transport and seal machinery)

Repro scripts are in R/S11-earnings-financial/repro/. Run each as `cd /workspace/final-workflow && PYTHONPATH=src:. .venv/bin/python <script>`. earnings_leap.py also needs `tests` on PYTHONPATH.
Targeted baseline: tests/test_pdf_header_periods.py, test_statement_lines.py, test_html_text.py, test_inline_xbrl_fixed_zero.py and test_earnings.py gave 134 passed and 59 skipped (corpus absent).

### S11-earnings-financial-A01  [high] [CONFIRMED]  period / guard bypass
- Location: `src/deploy_workflow/financial_workflow.py:1582-1583` (`_hit`, "balance" spec), used by `_mapped_columns` 1697 and `_header_columns` 1280 (HTML/line path: `_ocr_header`)
- Defect: when a full date is the column header, every unit becomes a "balance" spec, including an income statement or cash-flow unit. That spec matches any non-LTM period ending on that date, so the R23.27.1 header check verifies an annual IS column mapped to a QUARTER (Q4) or PERIOD_END period.
- Failure scenario: a 52/53-week 10-K in HTML prints "Fiscal Year Ended" over "December 28, 2024 | December 30, 2023". The book declares fy-2024 and q4-2024, both ending 2024-12-28. The model maps column 0 to q4-2024. `_header_verifies` returns True, so `compose_unit` writes the full-year Net sales 1,234 as Q4-2024 revenue. The guard meant to catch exactly this model error lets it through.
- Evidence: `repro/is_header_balance.py` prints `headers: ('December 28, 2024  December 30, 2023',)`, then `mapped: (frozenset({'fy-2024', 'q4-2024'}), frozenset({'fy-2023'}))`, then `... -> verified: True`.
- Fix direction: pass the unit's statement kind into the HTML path's `_mapped_columns`. For IS/CFS, a bare date cell should be unsupported (or need a flow span), and for BS it should match only PERIOD_END periods.

### S11-earnings-financial-A02  [high] [CONFIRMED]  quantity scale (shares)
- Location: `src/deploy_workflow/statement_compose.py:226-246` (`_header_scale`), used by `resolve_typed_row` 207-208 and `validate_typed_statement_line`
- Defect: share counts are excepted from the monetary scale only by "shares in X" or "except [for] share(s)". Common phrasings such as "(in thousands, except per share and share data)", "except per share amounts and number of shares" and "... and share counts" therefore give the monetary scale to share rows.
- Failure scenario: an IS headed "(In thousands, except per share and share data)" prints weighted-average shares 41,234,567. If the model gives the correct `shares/UNITS`, the row is refused (`source_quantity_refused`). If it gives the wrong `shares/THOUSANDS`, the row composes and the gate re-check passes, a 1000x share-count error that then feeds per-share and dilution analysis.
- Evidence: `repro/header_scale.py` prints `BAD shares scale 'THOUSANDS' expected 'UNITS' (in thousands, except per share and share data)` and the same for two other phrasings. `repro/share_scale_compose.py` prints `model scale UNITS: composed=0 left=['source_quantity_refused', ...]` and `model scale THOUSANDS: composed=2`.
- Fix direction: look for a "share(s)/share data/number of shares/share counts" item anywhere in the "except ..." clause. When the share scale is ambiguous, return None (refuse) rather than inheriting the monetary scale.

### S11-earnings-financial-A03  [high] [CONFIRMED]  HTML parsing: silent row drop
- Location: `src/deploy_workflow/statement_lines.py:38-39,96-115` (`_NUMTOK`, `respace`), feeding `line_table`
- Defect: `respace` scans tokens from the right and stops at the first token that is not a number. It does not recognise the EDGAR split-parenthesis negative (`<td>(250</td><td>)</td>`, which `convert_html` turns into "(250 )") or a Unicode minus ("−45"). Those rows stay single-spaced, the extractor finds no values in them, and `line_table` drops them from the table with no flag.
- Failure scenario: an EDGAR HTML statement prints "Operating loss $ (250 ) $ (10 )" and "Other expense −45 −30". Neither row appears in `ExtractedTable.lines`. Coverage only demands the extracted rows, so negative lines such as an operating loss, capex or an investing total vanish from composition and coverage without any signal. When the investing total is the row that disappears, the CFS net-change check is skipped rather than failed.
- Evidence: `repro/html_rows.py` shows `'Operating loss $ (250 ) $ (10 )' -> unchanged`, and the extracted rows are only `2 'Revenue' (1234, 1100)` and `5 'Net loss' (-300, -40)`. Rows 3 and 4 are missing, with no flag.
- Fix direction: in `respace`, treat a "(N" token followed by a ")" token as one negative cell and accept U+2212 as a minus. A line that holds number-like tokens but gives no row should become a flagged row (left to the model), not disappear.

### S11-earnings-financial-A04  [high] [CONFIRMED]  period handling (leap year / quarter length)
- Location: `src/deploy_workflow/earnings.py:348-353` (`build_earnings_delta_in`)
- Defect: a prior/current pair must have exactly the same day count (`prior.end - prior.start != current.end - current.start` raises `incompatible_periods`). Any pair across a leap year therefore fails, and so do calendar Q1→Q2 and Q2→Q3.
- Failure scenario: a calendar-year issuer's fy-2024 → fy-2025, one of the two pair shapes CP-1B supports and the latest annual pair today, is refused as `incompatible_periods`. CP-1B returns that as a validator issue the model cannot fix, so no annual earnings delta can be produced. The same happens for fy-2023 → fy-2024, YoY Q1 2024 → Q1 2025, and Q1 → Q2 of any year.
- Evidence: `repro/earnings_leap.py` reuses the test_earnings fixture with literal dates and prints `fy-2024 fy-2025 REFUSED incompatible_periods`, `q1-2025 q2-2025 REFUSED incompatible_periods` and `q1-2024 q1-2025 REFUSED incompatible_periods`.
- Fix direction: compare period class and length window instead of exact days (the same `_DAY_WINDOWS` idea `financial_workflow._months` uses: QUARTER 84-98 days, FY 357-371), and keep the order and no-overlap checks.

### S11-earnings-financial-A05  [medium] [CONFIRMED]  iXBRL parsing aborts run staging
- Location: `src/deploy_workflow/inline_xbrl.py:155-158` (missing-id raise), `:166` (strict UTF-8 decode); caller `src/deploy_workflow/run_inputs.py:291-296`
- Defect: `run_inputs` calls `parse` only to get `period_lines`, yet `parse` aborts in two cases. It raises when an `ix:nonFraction` has no `id`, although the attribute is optional in the Inline XBRL spec. It also decodes strictly as UTF-8, although `convert_html` already accepted a declared windows-1252 or iso-8859-1 document.
- Failure scenario: an issuer 10-K whose iXBRL facts carry no `id`, or which is declared windows-1252 with a 0x92 apostrophe, makes the whole run launch raise an untyped `ValueError` / `UnicodeDecodeError` from `_case_files`. Nothing in `run_inputs` catches it. The HTML text was fine, and the facts are never used.
- Evidence: `repro/ixbrl.py` prints `fact without optional id html ok: True | parse -> ValueError missing or duplicate inline fact id` and `windows-1252 declared, 0x92 byte html ok: True | parse -> UnicodeDecodeError ...`.
- Fix direction: parse the contexts from the text `convert_html` already decoded, and do not require fact ids on the `period_lines` path (or make it skip facts). Turn any remaining failure into a typed refusal.

### S11-earnings-financial-A06  [low] [CONFIRMED]  currency guard gap
- Location: `src/deploy_workflow/statement_compose.py:249-258` (`_currency_matches`)
- Defect: only words and ISO codes count as a stated currency (plus € and £). "US$", "C$", "A$" and "$" state none, so any book currency passes.
- Failure scenario: a typed unit headed "(in millions of US$)" verifies against a EUR book.
- Evidence: `repro/header_scale.py` prints `EUR book, header '(in millions of US$)': True`.
- Fix direction: recognise `US$`, `C$`/`CA$` and `A$` as stated currencies, and treat a bare `$` as ambiguous unless the book is USD.

### Out of scope (one line each, optional)
- `earnings_workflow._source_issues:1157` (frozen EarningsWorkflow slice only): coverage compares `line.value.amount == value`, so a nil-dash cell (None) is never covered, unlike `financial_workflow._amount_matches`. It is not reached from CP-OS (cp1b imports only `compose_delta`, `_operands` and `_own_limits`).

### Checked and sound (short bullets: what you attacked that held)
- pdf_headers: a mixed "Three Months Ended / Year Ended" (Q4 release) header gives FY labels to every column, but `_mapped_columns` then sees repeated FY periods and returns None (fails closed, no wrong period). Day-first "31 March", 52/53-week complete-date year rows, interim BS with cross-line dates, and banners above the title all map correctly or refuse.
- `_mapped_columns` with a 52/53-week 10-Q dated header: the quarter and YTD periods overlap, so the map is refused.
- statement_compose: a repeated column period refuses the whole unit. Failed BS/CFS checks compose nothing. An OCR unit with vacuous (all-nil) checks is refused. A BS outflow_magnitude is refused. Footnote marker "(1)" next to "$" is dropped. Without "$" it is flagged (`more_values_than_header_years`) and left to the model.
- unit_maps: a unit repeated per book, a repeated row, an unknown book, an unlocated or unextracted unit, and a missing hash all compose nothing. Typed maps need authenticated book dimensions and PERIOD_END BS columns.
- respace year guard: "Senior notes due 2027 500 450" keeps 2027 in the label. "Balance at December 31, 2023 ..." does not take the year as a value.
- html_text: nbsp and zero-width characters are normalised, display:none and ix:header content is dropped, and a strict decode refuses undeclared non-UTF-8.
- financial_series, liquidity_series, restructuring_series: no zero-fill. Non-known facts become gap points. Repeated coordinates and identities, a mixed currency, and a foreign module all raise. CP-2D facts are constrained to MILLIONS upstream (cp2d.py:2152), so the fixed "MILLIONS" unit in liquidity_series is consistent.
- earnings.py: a zero prior gives a missing growth (ZERO_DENOMINATOR). Precedence among non-known statuses is kept. Fact-id duplicates and coordinate duplicates refuse. Decimal context is local at prec 38.
