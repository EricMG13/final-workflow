SECTION: S04-delivery   PASS: adversarial
COVERAGE: read fully: markdown_delivery.py, handoff_delivery.py, model_handoff_delivery.py, reader_summary.py, render.py, table_markdown.py, shell.html, charts.py (line/columns/na/render_svg/mark paths) / skimmed: report_view.py (fact_spelling, _cell, _slot, _scale_of, _prose_lines, _call, _unplaced, ChartMark/ChartSpec, _chart_fact_cell, _figure_of_points), display.py, app.js (all DOM sinks, SVG import, links), rendering.py, financial_rendering.py, delivery.py, cp1_render.py / not read: statement_view.py, register_view.py, interface_view.py bodies (grep only: no HTML string building), app.css, tokens.css

Repro scripts: R/S04-delivery/t/ (harness.py builds a real CP-OS `_layout` for a CP-1 credit_snapshot run and calls `markdown_files`). Run each as
`cd /workspace/final-workflow && PYTHONPATH=src:. .venv/bin/python <R>/S04-delivery/t/<script>`.

### S04-delivery-A01  [high] [CONFIRMED]  units/limitations lost at the delivery boundary
- Location: `src/deploy_workflow/markdown_delivery.py:84-138` (literal_module, how prose is split from tables) and `:517-531` (markdown_files, table-route selection)
- Defect: when a section holds both a table and a paragraph, `literal_module` stores the paragraph as a separate "prose" table under the same heading. A `kind="table"` route then publishes only the table. The section's unit, scale and limitation sentence never reaches the block that shows the numbers.
- Failure scenario: CP-1 writes `### Financials and credit metrics` with "All amounts in EUR thousands; FY2024 is unaudited." followed by the table. The populated financials-credit-metrics block shows `Revenue 1,000.5 / 1,200.0` with `scale=None` and `note=None`, and no unit anywhere in the block. The page's strip charts are labelled US$m, so a reader will likely read these figures as US$m. The sentence appears only in the Evidence prose list. The CP-OS table selector asks for "exactly one populated Markdown table" and does not require the unit to be in the table header.
- Evidence: `t/attacks6.py` prints `{'title': 'Financials and credit metrics', 'note': None, 'scale': None, 'row_header': 'Metric', 'columns': ('FY2023','FY2024'), ...}` and `EUR thousands anywhere in financials block: False`, `blocks carrying it: []`.
- Fix direction: carry the routed section's own prose (or at least its unit and limitation lines) into the block note or meta. Otherwise refuse a table route whose section has prose but whose header states no unit.

### S04-delivery-A02  [medium] [CONFIRMED]  nonzero amounts shown as zero / fixed display precision ignores the source
- Location: `src/deploy_workflow/model_handoff_delivery.py:468` (build_model, `decimals=2 if tid == "ratios" else 0`); `src/deploy_workflow/markdown_delivery.py:381-383` (_numeric_observations, fixed `2`/`4` decimals when the token path is used)
- Defect: the display precision is hard-coded rather than taken from the source token. Sub-unit source amounts therefore render as "0" (HTML Model) or "0.00" (charts), and other values are rounded or padded.
- Failure scenario: an annual CP-1 row `| Cash paid ... income taxes | 0.4 | (0.3) | 220.5 |` (USD millions). calculation.json keeps `0.4 / -0.3 / 220.5` exactly. The HTML Model row shows `['221', '0', '0']`, so a nonzero cash tax displays as zero. In the strip charts, liquidity token `0.004` displays as `0.00` in the mark label, tooltip and table twin, cover `0.125` as `0.13x`, and `150` as `150.00` (false precision). By contrast, `_yield_observations` (line 253) does take decimals from the token.
- Evidence: `t/attacks4.py` (copies the retained runs/cpos-sol-medium-20261105 CP-1 to scratch and edits one row) prints `calculation.json tax_cash: {'FY2022': '220.5', 'FY2023': '-0.3', 'FY2024': '0.4'}` and `HTML Model row Tax Cash ['221', '0', '0']`. `t/attacks5.py` prints `('Cash','FY2023','0.004','0.00')` and `('EBITDA / cash interest','FY2023','0.125','0.13x')`.
- Fix direction: set `Fact.decimals` from the source lexeme's fractional digits (capped at 6), as the yield path already does. For calculated cells, use the maximum precision of their inputs.

### S04-delivery-A03  [medium] [CONFIRMED]  reader-summary number check ignores sign, unit and scale
- Location: `src/deploy_workflow/reader_summary.py:15,84-92` (NUMBER, _unmatched_numbers)
- Defect: the check that summary "numbers must match the handoff exactly" compares only the unsigned digits. It drops `-`, parentheses, `%`/`x` and the thousand/million scale.
- Failure scenario: the handoff says `Revenue change (12.3)%`, and the Reader summary says "Revenue grew 12.3%". `reader_issues` returns no issues, so the CP-OS check accepts it and the sign-flipped sentence is published in the report through literal_module. "4.1x" restated as "4.1%" and "250 US$ thousands" restated as "US$250 million" are also accepted.
- Evidence: `t/attacks3.py` prints `sign flipped ... -> ACCEPTED (no issues)`, `unit swapped ... -> ACCEPTED`, `scale swapped ... -> ACCEPTED`. The control case (an absent 13.0) is flagged.
- Fix direction: match the signed token (leading `-`, `(...)`) together with its adjacent unit suffix (`%`, `x`, `bn`/`m`/`thousand`) against the same token family in the rest of the handoff.

### S04-delivery-A04  [low] [CONFIRMED]  chart period axis follows authoring order (reversed time)
- Location: `src/deploy_workflow/markdown_delivery.py:321-400` (_numeric_observations: categories in table-row order); drawn by `src/deploy_vii/charts.py:188-194,260-326`
- Defect: the order of strip-chart categories is the order of the handoff's rows. Nothing sorts or checks chronology.
- Failure scenario: a leverage table written newest-first (`FY2024 | FY2023 | FY2022`, common in issuer tables) draws S.1 with x = `['FY2024','FY2023','FY2022']`. A falling line then looks like rising leverage. The values and labels are correct, but the trend reads backwards.
- Evidence: `t/attacks1.py` section A1 prints `categories left->right: ['FY2024', 'FY2023', 'FY2022']`.
- Fix direction: require ascending period rows for chart routes (refuse otherwise), or add the ordering rule to the chart selector instructions and enforce it in delivery.

### S04-delivery-A05  [low] [CONFIRMED]  "line N" citations drift from physical lines
- Location: `src/deploy_workflow/model_handoff_delivery.py:280` (_literal_tables), `markdown_delivery.py:70` (literal_module), `handoff_delivery.py:208` (mapped_module): all use `str.splitlines()`
- Defect: `splitlines()` also breaks on U+2028/U+2029, `\x0b`, `\x0c`, `\x1c-\x1e` and `\x85`. Every locator after such a character points at the wrong physical (`\n`) line, and quotes become line fragments.
- Failure scenario: a prose line containing U+2028 (pasted from PDF-extracted issuer text) gives `locator line 47 quote ' strongly.'` while physical line 47 is empty. 6 of the citations in the synthetic handoff no longer match the file a reader opens. A table row containing one is split, and the delivery refuses it.
- Evidence: `t/attacks1.py` section A3 prints `citations whose 'line N' != physical newline-delimited line N: 6`.
- Fix direction: split on `\n` only (after normalizing `\r\n`), or refuse handoffs containing these separators.

### S04-delivery-A06  [low] [CONFIRMED]  hidden multi-line HTML comments are published as prose
- Location: `src/deploy_workflow/markdown_delivery.py:87-95` (literal_module paragraph loop)
- Defect: only the line that begins with `<!--` is treated as a boundary. The following lines of a multi-line comment, including `-->`, become a published paragraph.
- Failure scenario: `<!--\nDRAFT: internal estimate 999 not for publication\n-->` produces the fact `'DRAFT: internal estimate 999 not for publication -->'`, which appears in report.html. Markdown viewers hide this text.
- Evidence: `t/attacks1.py` section A4 prints the fact and `in report.html: True`.
- Fix direction: skip lines through the closing `-->`, or refuse unterminated or multi-line comments.

### S04-delivery-A07  [low] [CONFIRMED]  delivery ignores the chart table's own Reporting unit
- Location: `src/deploy_workflow/markdown_delivery.py:341-356` (_numeric_observations token path)
- Defect: for handoff-sourced charts, the unit comes only from `route.chart_unit`. The row's `Reporting unit` cell is never compared with it.
- Failure scenario: a liquidity table with `Reporting unit = EUR m` is published by `markdown_files` as US$m figures (100 / 200 / 150). In the CP-OS launch path the separate check `cpos_launch.chart_issues` flags this before delivery. A direct or replayed `delivery_files` manifest with a layout has no such guard.
- Evidence: `t/attacks1.py` section A2 prints `US$m [('Cash','FY2023',Decimal('100')),...]`, and chart_issues returns three unit issues for the same text.
- Fix direction: in `_numeric_observations`, when the table has a `Reporting unit` column, require it to equal `chart_unit` for every numeric cell. Otherwise treat the cell as a gap.

### Out of scope (one line each, optional)
- `owners/cpos_launch.py:331` PLAIN_NUMBER accepts malformed groupings (`1,2,3`) that the delivery regex rejects, so the launch check passes while delivery refuses after a paid run.
- `model_handoff_delivery._annual_cells:235` reads `cash` (an instant) from the duration column label while debt uses `balance_column`. A layout that selects cash from the balance table silently gets a NOT_SOURCED gap. This is a design question, not reproduced as wrong.

### Checked and sound (short bullets: what you attacked that held)
- HTML/JS injection: `</script><img onerror>`, `"><svg onload>`, `&amp;` and `<!--` in cells, row labels, period labels and headings. The JSON payload escapes `<` as `<` with ensure_ascii (U+2028/2029 escaped). Nothing reaches markup outside the data block. app.js builds the DOM with textContent and setAttribute only, and imports SVG through DOMParser with an element allowlist, stripping on*/href/style. charts.py serialises through ElementTree, and all 4 SVGs were well-formed with allowed tags and no on* attributes. The Model href is regex-guarded. The scope banner is html.escape'd.
- Missing versus zero: blank cells become `missing` with "not zero", and literal `0` stays known in tables. Chart gaps ("Not supplied:", "—", blank) are value=None marks with G# references. The line chart lifts the pen and the bars draw an n/a slot, never a 0. An all-gap figure draws the n/a frame.
- Signs: parenthesised negatives are parsed exactly (`(12.3)` -> -12.3). A Unicode minus or en dash in a chart or Model cell is refused, not silently re-signed. Capex with a positive sign is refused.
- Table parsing: escaped pipes inside cells, alignment rows, ragged rows (refused), empty first cell (refused), CRLF handoffs (accepted, same output), duplicate period labels or columns (refused), duplicate (series, category) marks (refused by ChartSpec).
- calculation.json keeps exact Decimal strings, unit, scale, currency, quantity family, period dates and the source locator and cell text. Model reconciliation (EBIT, issuer bridge) refuses on mismatch.
- Yield path: requires future ISO maturities, both price bases, no duplicates, and a numeric token only. Sorting by ISO date string is chronological.
- CP-6 posture: needs exactly one cited terminal choice. Trailing qualifiers or duplicates are refused, and nothing is inferred.
- table_markdown round trip: markdown_cell and read_table_markdown are injective for pipes, `<br>`, entities and backslashes.
