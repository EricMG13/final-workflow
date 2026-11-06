SECTION: S11-earnings-financial   PASS: code-review
COVERAGE: The forked code-review skill says it read all 12 files in full. I read these myself in full: financial_series.py, statement_lines.py, pdf_headers.py, inline_xbrl.py, html_text.py, liquidity_series.py, restructuring_series.py, unit_maps.py / I skimmed earnings.py (period, delta and growth path), statement_compose.py (lines 400-909) and financial_workflow.py (unit location, inputs(), period matching) / I did not read earnings_workflow.py myself (only the growth-rendering lines 2085-2130); the skill covered it.

Independence note: I put the constraint line in my reply before calling the skill, but its forked reviewer read docs/review-handoff/S11-earnings-financial/adversarial.md anyway. It said it "left out the six findings already in adversarial.md (A01-A06)" and described one finding as "a different cause from A03". So which findings it kept was shaped by the adversarial pass. Any finding that overlaps A01-A06 may be missing from this report, and this pass is not fully independent. I did not open adversarial.md, the repro files or any other section. The fork also left a scratch script outside the section folder, at /tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/s11/series.py. Nothing was written to the repo. I re-checked every finding below with my own scripts in this section folder.

In the repro commands below, <dir> = /tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S11-earnings-financial, and each command runs from /home/user/final-workflow.

### S11-earnings-financial-C01  [high] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/financial_series.py:111-113` (_periods)
- Defect: Any T4.14 period of type YTD or LTM raises "Unsupported historical chart period type". The contract allows both types (financial_contracts.py:128). The CP-1 workflow in this section creates YTD periods ("Six"/"Nine months ended" -> YTD, financial_workflow.py:1495-1500), and model_interface writes one T4.14 row per book period.
- Failure scenario: A CP-1 book built from a Q2 or Q3 10-Q holds a six- or nine-month YTD period, or an LTM period used for leverage. cp1_chart_series raises ValueError. report_view._cp1_supplied, _cp1_strip and _cp1_period_figures do not catch it, so the whole report render fails. The docstring promises an explicit unsupported figure for incomplete coverage, not an exception.
- Evidence: `PYTHONPATH=src:.:tests .venv/bin/python <dir>/c01_series.py` gives: baseline -> all 5 figures; "plus YTD six-month period" -> RAISES ValueError Unsupported historical chart period type; "plus LTM period" -> same. Script: c01_series.py.
- Fix direction: Leave non-QUARTER/FY/PERIOD_END periods out of the chart projection, since only QUARTER rows are plotted and FY/QUARTER rows are used for the facility snapshot, and keep failing closed only on malformed identities.

### S11-earnings-financial-C02  [high] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/statement_lines.py:39,100-104` (_NUMTOK, respace)
- Defect: respace only knows `$` as a currency token. A line whose value cells carry `€`, `£` or another symbol is never re-spaced into cells, and line_table drops the row without a flag.
- Failure scenario: An HTML line source in EUR has "Revenue € 1,234 € 1,100" and "Operating profit € 434 € 400". line_table returns only "Cost of sales". Revenue and Operating profit are missing from the extraction, so composition never sees them and the coverage gate never asks for them. Statement lines are lost silently. DVII's extractor does read the same euro lines once they are double-spaced, so the cause is in respace.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <dir>/c04_euro_lines.py` gives: `$` -> 3 rows (Revenue, Cost of sales, Operating profit); `€` -> [('Cost of sales', ...)] only; `£` -> same; "DVII on pre-spaced euro lines: ['Revenue', 'Operating profit']". Script: c04_euro_lines.py.
- Fix direction: Make the currency-symbol handling in `_NUMTOK` and respace's standalone-symbol merge accept a set of currency symbols (at least $, €, £, ¥), or the book's currency symbol, instead of the literal `$`.

### S11-earnings-financial-C03  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/financial_series.py:269-272` (_maturity_figure)
- Defect: When a facility row exists for the selected QUARTER period but not for an FY period that ends on the same date, the function raises "Incomplete same-date facility snapshot alias" instead of using the selected quarter's snapshot or returning a reason.
- Failure scenario: The book has q4-2025 and fy-2025, both ending 2025-12-31, and the T4.18 register holds facility rows only for the latest quarter. Nothing upstream requires one facility row per same-date alias. cp1_chart_series raises and the whole CP-1 chart strip fails to render, as in C01.
- Evidence: c01_series.py case "plus FY alias ending 2025-12-31 (no FY facility rows)" -> RAISES ValueError Incomplete same-date facility snapshot alias.
- Fix direction: Compare terms only against aliases that do carry the facility, or return an unsupported S.4 reason, instead of raising when an alias row is absent.

### S11-earnings-financial-C04  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/financial_series.py:157-165` (_quarter_figures)
- Defect: Exactly four contiguous quarters that are not Q1-Q4 of one fiscal year raise "Ambiguous or noncontiguous QUARTER identities" instead of getting the explicit unsupported reason that the len != 4 branch gives.
- Failure scenario: The register holds the trailing four quarters, for example Q4 FY2025 to Q3 FY2026 for a March year-end, or q2-2024 to q1-2025. These are valid and contiguous. All CP-1 charts fail, the S.4 maturity wall included, instead of S.1-S.3 and S.5 carrying a reason.
- Evidence: `PYTHONPATH=src:.:tests .venv/bin/python <dir>/c03_trailing.py` gives "trailing four quarters across FY boundary -> RAISES ValueError Ambiguous or noncontiguous QUARTER identities". Script: c03_trailing.py.
- Fix direction: Require contiguity only, or turn a cross-year set into a `reason`, and keep raising only for genuinely contradictory identities such as duplicates, overlaps or start > end.

### S11-earnings-financial-C05  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/statement_compose.py:616-641,689-703` (_sums / _checks)
- Defect: The CFS net-change check, and the BS checks, add the raw printed cells and ignore each row's sign_convention. Downstream (financial_reconciliation.py:535) negates outflow_magnitude rows.
- Failure scenario: A CFS prints "Net cash used in investing activities 250" and "... financing activities 100" as positive magnitudes, and the model maps them as outflow_magnitude. The check computes 400+250+100 = 750 against 50 and fails. The whole unit becomes UNIT_CHECK_FAILED and nothing is composed, although the statement is internally consistent.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <dir>/c07_cfs_sign.py` gives "lines composed: 0", "issues: ['check cfs_sections_eq_net_change failed in column 0 (fy-2025): ... 750 != 50', ...]", left: ['unit_check_failed']. Script: c07_cfs_sign.py.
- Fix direction: In _sums, negate the cells of CFS rows whose judgment is outflow_magnitude, which needs the judgment passed alongside each row. BS rows cannot be outflow_magnitude.

### S11-earnings-financial-C06  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/earnings.py:260-266` (_point)
- Defect: Growth is delta / prior with a signed denominator, so when the prior value is negative the growth has the wrong sign.
- Failure scenario: A distressed issuer's EBITDA goes from -10 to -5. delta = +5 and growth = -50%, an improvement shown as a decline. It is published as CP-1B "Growth (%)" (earnings_workflow.py:2092-2125) and given to the model and the deliverables. A zero base already becomes missing (ZERO_DENOMINATOR); a negative base gets no equivalent treatment.
- Evidence: `PYTHONPATH=src:.:tests .venv/bin/python <dir>/c06_growth.py` gives "EBITDA prior -10 current -5 delta 5 growth -0.5 known". Script: c06_growth.py.
- Fix direction: Treat prior <= 0 as growth "not meaningful" (missing or not_applicable with a reason such as NEGATIVE_DENOMINATOR), or divide by |prior| and change the published formula to match.

### S11-earnings-financial-C07  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/pdf_headers.py:22,184-189` (_MONTH_DAY, mapping_headers)
- Defect: `_MONTH_DAY` has no boundary after the day digits, so in a month-and-year header such as "June 2024" it reads the first two digits of the year as the day.
- Failure scenario: A balance-sheet header "June 2024  June 2023" is mapped to "June 20, 2024 | June 20, 2023", a made-up period-end date. Usually it fails closed because no declared period ends on the 20th, but a book with a period ending on the 20th (for example a 52/53-week year) would bind the column to the wrong date.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <dir>/c05_month_year.py` gives "BS ['June 2024  June 2023', 'Assets'] -> ('June 20, 2024 | June 20, 2023',)". Control: "As at 30 June / 2024 2023" -> June 30. Script: c05_month_year.py.
- Fix direction: Add `(?!\d)` after the day group in `_MONTH_DAY`, and add a lookahead that rules out a following 2-digit year continuation.

### S11-earnings-financial-C08  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/financial_series.py:104-108,134,215,290,314` (_periods, _numeric, figure units)
- Defect: The chart projection hard-codes USD, "US$m" and IFRS, and raises for any other book currency or basis. The neighbouring modules were made currency-aware: earnings.build_earnings_delta_in(currency) and liquidity_series._axis via scale_label.
- Failure scenario: The CP-1 book of a EUR (or US GAAP) run has T4.14 currency EUR. cp1_chart_series raises "Unsupported chart currency, unit or perimeter", and the report render fails as in C01 instead of carrying an unsupported-figure reason. The module docstring declares USD/IFRS as its bounded scope, so this is low: the problem is that it crashes instead of returning a reason.
- Evidence: c03_trailing.py case "EUR book -> RAISES ValueError Unsupported chart currency, unit or perimeter".
- Fix direction: Return figures whose `reason` states the unsupported scope, or take the run currency and use scale_label as liquidity_series does, rather than raising.

### S11-earnings-financial-C09  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_workflow/financial_workflow.py:981-1007` (expand_unit_maps.inputs), 1441-1458 (_other_statement_rows), 908-939; also _evidence_issues at 1085+
- Defect: One inputs() call runs the per-page statement extractor (_page_units) five times for every financial source: _other_statement_rows 2x, _located_pdf_units, _located_kinds and _located_units. _evidence_issues repeats the same pattern on every submit.
- Failure scenario: The code's own note puts two passes at about 220 ms on the 107-page CZR 10-K, so about 550 ms per inputs() call plus the same again in _evidence_issues on each submit, all repeated work.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <dir>/c09_page_units_count.py` gives "_page_units calls for one source in the inputs() sequence: 5". Script: c09_page_units_count.py.
- Fix direction: Compute (locator -> text, kind) once per source per call and pass it to the four helpers.

### S11-earnings-financial-C10  [low] [CONFIRMED]  simplification
- Location: `src/deploy_workflow/pdf_headers.py:128-149, 154, 180, 287-296` (mapping_headers)
- Defect: Code that never runs or whose result is never used. The `years_line is None` branch needs a complete `_DATE` match whose year is not 19xx/20xx. The `is_year and complete_dates` block at 287-296 can never be reached, because every `is_year` path returns at 260-274. `residue` at 154 and `full` at 180 are assigned and then overwritten or never read.
- Failure scenario: About 35 dead lines in an already tangled header mapper, which invites fixes to code that never runs, as with C07.
- Evidence: Control flow: line 260 `if is_year:` returns or returns None in every branch before line 287. Confirmed by reading; no runtime effect.
- Fix direction: Delete the dead branches and assignments. Behaviour does not change.

### Out of scope (one line each, optional)
- src/deploy_vii/report_view.py:1915-2045 (_cp1_supplied/_cp1_strip): any ValueError from the producer takes down the whole report render instead of degrading the chart block. This is what turns C01, C03, C04 and C08 into render failures.

### Checked and sound (short bullets: what you attacked that held)
- liquidity_series: the hard-coded "MILLIONS" unit is safe, because report_view._chart_fact_cell refuses non-MILLIONS or non-1e6-scale facts. Gaps stay None (never 0), and mixed currencies fail closed.
- restructuring_series: equity recoveries must be not_applicable, scenario labels must be distinct, more than 3 scenarios is refused, and no value is zero-filled.
- inline_xbrl: nil versus fixed-zero versus dash is kept distinct (nil -> None), unsupported transforms and lexemes raise, dimensional contexts are left out of period_lines, and duplicate fact, context and unit ids raise.
- html_text: hidden and SKIP elements nest correctly through the open_names counter. Unicode line separators are folded to spaces before splitting (`\s` covers \x85, U+2028 and \x1c-\x1f), so no stray line breaks appear. Decoding is strict with an accepted-encoding allowlist and a NUL refusal.
- unit_maps.expand: inputs() is called at most once; maps to an unknown book, an unextracted unit, an unlocated unit or a repeated unit compose nothing; a header that does not verify blocks text-layer composition; typed-source/1 rows require authenticated book dimensions.
- earnings.build_earnings_delta_in: currency is checked on period rows and on every money fact; prior and current must have the same kind and length and must not overlap; a zero denominator gives missing growth, never 0.
