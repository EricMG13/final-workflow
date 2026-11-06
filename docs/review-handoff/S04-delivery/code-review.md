SECTION: S04-delivery   PASS: code-review
COVERAGE: read fully: markdown_delivery.py, handoff_delivery.py, model_handoff_delivery.py, rendering.py, financial_rendering.py, reader_summary.py, deploy_vii/render.py, delivery.py, cp1_render.py, display.py, interface_view.py, register_view.py, statement_view.py, table_markdown.py, assets/shell.html / skimmed: charts.py (axis, line, columns, waterfall, bullet, render_svg), report_view.py (Block/BlockTab/Cell/ChartSpec validators, _slot, _prose_lines, _call, _figure_of_points, presets), assets/app.js (DOM/text sinks, SVG sanitizer, routing/rail, module page), assets/app.css / not read: assets/tokens.css

Process note: the code-review skill ran (forked, at high) over all 20 files. Its report said it consulted docs/review-handoff/S04-delivery/adversarial.md to avoid duplicates. I did not read that file or any other section's material. I reproduced every finding below myself, and I dropped or downgraded the skill's claims that did not hold (for C08, the rows do still appear on the module page). Repro scripts are in /tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S04-delivery/cr/. Run each as: cd /home/user/final-workflow && PYTHONPATH=src:. .venv/bin/python <script>

### S04-delivery-C01  [high] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/markdown_delivery.py:590-604` (markdown_files, partial-selection bindings) with `:747-772` (table block assembly)
- Defect: when a route selects only some rows of a table, each selected row gets its own Binding, and every one carries the same label (`route.label or table.title`). The dense/keyvalue/period_grid branch then makes the first one the primary tab and the rest further tabs, and Block's validator rejects duplicate tab labels.
- Failure scenario: a handoff's `## Request` has the paragraphs "Earnings view: first…", "Earnings view: second…" and one other paragraph. The layout has a prose route with prefix "Earnings view" into `headline-results` (the shipped TDG earnings layout uses this exact route shape). markdown_files raises `ValidationError … Tab labels are distinct`, so the whole delivery fails. Each matching paragraph would also become its own tab instead of one register.
- Evidence: `cr/r01_dup_tabs.py` -> `ValidationError 1 validation error for Block  Value error, Tab labels are distinct`. With two paragraphs that both match, so the selection covers the whole table, it succeeds.
- Fix direction: make one binding per route (for example, one fact/row set per route), or give each binding a distinct label, instead of one binding per selected row.

### S04-delivery-C02  [medium] [CONFIRMED]  correctness (content silently dropped)
- Location: `src/deploy_workflow/markdown_delivery.py:86-95` (literal_module paragraph splitter) together with `model_handoff_delivery.py:309-316` (_literal_tables table detection)
- Defect: any line starting with `|` counts as a paragraph boundary and is never added to a paragraph. _literal_tables only lifts pipe lines that are followed by a `|---|` separator. Pipe lines that do not form a recognised table therefore belong to neither path and vanish from the view without an error. A line such as `#1 risk is …` is treated as a heading: its text becomes a section label and never becomes fact text.
- Failure scenario: a handoff table whose separator row is missing, or a stray `|caveat` line, publishes report.html/view.json without those rows. delivery.json still claims a literal delivery, which breaks "missing handoff content stays an explicit gap".
- Evidence: `cr/r09_pipe_lines_dropped.py` -> `DROPPED-ROW-ONE retained in any fact: False`, `DROPPED-ROW-TWO … False`, `DROPPED-CAVEAT … False`, and no table is created for "Covenants". `cr/r10_hash_line.py` -> the "#1 risk…" text appears in no fact; it only becomes the heading of an empty section.
- Fix direction: refuse, or keep as literal prose, every non-blank line that ends up in neither a table nor a paragraph. Treat only `#{1,6} ` with a following space as a heading.

### S04-delivery-C03  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/markdown_delivery.py:83-95` (literal_module: `paragraphs` keyed by heading text alone)
- Defect: paragraphs are grouped by the text of the nearest heading, with no parent section. Same-named subsections under different `##` sections are merged into one prose table, so a prose route has no way to select only one of them.
- Failure scenario: `### Notes` under `## Findings` ("Findings note one.") and `### Notes` under `## Calculations` ("Calculation note two") produce one table, prose-CP-1B-2 "Notes", with two paragraphs. A route `heading="Notes"` labelled "Findings notes" publishes the Calculations note under the Findings label.
- Evidence: `cr/r02_heading_merge.py` -> `prose-CP-1B-2 Notes ['Notes — paragraph 1', 'Notes — paragraph 2']` and watch-items lines `['Findings note one.', 'Calculation note two (different section).']`.
- Fix direction: key prose groups (and table metadata) by the full heading path or by the heading line number, and let routes address that path.

### S04-delivery-C04  [medium] [CONFIRMED]  security / source identity
- Location: `src/deploy_workflow/markdown_delivery.py:429-446` (require_issuer); same pattern at `handoff_delivery.py:399` (prepare) and `model_handoff_delivery.py:400-405` (build_model, annual/current_synthesis)
- Defect: the issuer name and aliases are matched as plain casefolded substrings. Only issuer_id gets word boundaries. In the two other sites the substring search runs over the whole handoff text.
- Failure scenario: for an issuer named "Ford", a handoff titled "# CP-1B Stanford Health Care" passes the issuer check. A short alias such as "AB" matches "lab". The result is another issuer's analysis delivered under this run.
- Evidence: `cr/r04_issuer.py` -> `ACCEPTED handoff about Stanford for issuer Ford` and `ACCEPTED via alias 'AB' substring of 'lab'`.
- Fix direction: apply the same `(?<![a-z0-9])…(?![a-z0-9])` boundary match used for issuer_id to the name and aliases, in all three sites.

### S04-delivery-C05  [medium] [CONFIRMED]  correctness (chart display)
- Location: `src/deploy_vii/charts.py:88-89` (_tick_text), used by _axis_y (:233-251) and _bullet (:739-760)
- Defect: axis tick labels are formatted at the unit class's default precision (amount = 0 places, percent = 1 place) instead of the tick step's precision. Fractional steps round to wrong or duplicate labels, using ROUND_HALF_UP.
- Failure scenario: a US$m line chart with values 0.4 and 0.8 has ticks 0/0.5/1.0, labelled "0","1","1", so the 0.5 gridline reads 1. Values 0.03 and 0.05 give "0","0","0". A waterfall with a max of about 9 gets a 2.5 step, labelled "0","3","5","8","10". The mark labels are exact while the axis misstates the scale.
- Evidence: `cr/r03_ticks.py` -> `line ['0.4','0.8'] axis labels: ['0','1','1']`, `grouped ['0.03','0.05'] axis labels: ['0','0','0']`, `waterfall ['4','5'] axis labels: ['0','3','5','8','10']`.
- Fix direction: pass `decimals` derived from the tick step (the number of decimal places of step × the unit-class scale) to format_value in _tick_text.

### S04-delivery-C06  [medium] [CONFIRMED]  correctness (source attribution)
- Location: `src/deploy_workflow/model_handoff_delivery.py:307-311` (_literal_tables heading tracking)
- Defect: the table heading only updates on `### ` or `**` lines. A `## ` section change never resets it, and any bold-led prose paragraph becomes the "heading" of every later table.
- Failure scenario: in a current_synthesis/annual/quarter handoff, `**Assessment —** Leverage is high…` under Findings becomes the title of the Findings table and also of the Calculations and Gaps tables: "current_synthesis: Assessment — Leverage is high …". These titles are published in model.html and model-view.json. CP-MODEL routes in markdown_delivery select on these titles (`metadata["CP-MODEL"]`), and comparison_files falls back to them for any row header it does not map.
- Evidence: `cr/r08_literal_titles.py` -> all three tables (raw-…-0/1/2) are titled "current_synthesis: Assessment — Leverage is high and the long paragraph continues…".
- Fix direction: reset the heading on every `#…` heading line, and treat a `**…**` line as a heading only when the whole line is the bold label.

### S04-delivery-C07  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/markdown_delivery.py:86-95` (paragraph boundaries) and `:563-570` (prefix selection)
- Defect: list items and fenced code are not boundaries, so consecutive bullets and numbered items collapse into one "paragraph" fact. plain() then strips the backticks. A prefix route cannot target an item, because the text starts with "- " or "1. ".
- Failure scenario: under `### Watch`, the lines `- Track cash interest`, ``- Track `covenant` headroom``, `1. First`, `2. Second` become the single fact "- Track cash interest - Track covenant headroom 1. First 2. Second". A layout route with prefix "Track dated cash" (as in the shipped TDG watch-items route) matches nothing and raises "no unused content". Without a prefix, the whole list publishes as one run-on line.
- Evidence: `cr/r07_lists.py` -> `'- Track cash interest - Track covenant headroom 1. First 2. Second' ['line 8', 'line 9', 'line 10', 'line 11']`.
- Fix direction: start a new paragraph at each list-item line (`^\s*([-*+]|\d+\.)\s`) and at code fences, and keep each item as its own fact.

### S04-delivery-C08  [low] [CONFIRMED]  correctness (config accepted then ignored)
- Location: `src/deploy_workflow/markdown_delivery.py:465-470` (route guard) and `:660-701` (strip-chart block branch)
- Defect: a `table` or `prose` route whose block_id is a strip-chart block (metric-strip, model-chart-strip, maturity-wall) passes validation. Its rows are bound to the chart block and marked used, so they are kept out of the evidence binding. The chart branch builds the block only from strip_charts and ignores `bound`. The front page silently omits the routed content, and `unplaced` stays empty.
- Failure scenario: a covenant-notes table routed to metric-strip next to S.1–S.3 chart routes. The delivery succeeds, but the row is on no front-page block. It is reachable only on the CP-1B module page, and as an orphan passport quote.
- Evidence: `cr/r05_table_into_strip.py` -> blocks `[('metric-strip','chart')]`, `unplaced: []`, and the row appears in report-view.json only at `/passports[3]/fields[2]/value`.
- Fix direction: reject non-chart routes into chart blocks in the layout guard, with the same check used for prose blocks.

### S04-delivery-C09  [low] [CONFIRMED]  correctness (display precision)
- Location: `src/deploy_workflow/markdown_delivery.py:383-385` (_numeric_observations decimals)
- Defect: for token-sourced cells the decimals are fixed (4 for "%", 2 otherwise), and the percent formatter applies them after ×100. A fraction token "0.0725" therefore displays as "7.2500%" (false precision) in the mark label, tooltip and table twin. A US$m token "1234.567" displays as "1,234.57". The yield path (:253) correctly derives decimals from the token.
- Failure scenario: an RV.1 chart route over a `*_fraction` column prints "7.2500%", while the figure summary promises at most six decimals of the source.
- Evidence: `cr/r06_pct_decimals.py` -> `ytm_fraction token 0.0725 decimals 4 -> 7.2500%`, `amt token 1234.567 decimals 2 -> 1,234.57`.
- Fix direction: derive decimals from the token's fractional digits (minus 2 for percent, capped at 6), as _yield_observations does.

### S04-delivery-C10  [low] [CONFIRMED]  correctness (inconsistent gap handling)
- Location: `src/deploy_workflow/model_handoff_delivery.py:216-222` (_AnnualReader.read) compared with `markdown_delivery.py:345-350`
- Defect: the Model reader accepts only `""`, `—`, "Insufficient Information" and "Not reconstructed" as gaps. The chart path also accepts "Not supplied…" and "Not calculable…". The copied number regex and gap set have diverged.
- Failure scenario: the CP-1 cell "Not supplied: undisclosed" renders as an explicit gap in a strip chart, but makes build_model raise "model_number: unsupported source spelling". That refuses the whole Model publication instead of recording NOT_STATED.
- Evidence: `cr/r11_gap_tokens.py` -> `capex_signed -> None NOT_STATED`, `revenue -> ValueError: model_number: unsupported source spelling Not supplied: undisclosed`, `cash -> ValueError: … Not calculable: missing inputs`.
- Fix direction: share one parse_source_number/is_gap helper between the two paths.

### S04-delivery-C11  [low] [PLAUSIBLE]  simplification / UI correctness
- Location: `src/deploy_workflow/markdown_delivery.py:797-801`, `handoff_delivery.py:478-482`, `model_handoff_delivery.py:637-649` (string patching of the rendered app.js DEST literal), and `src/deploy_vii/assets/app.js:704-707` (destOf)
- Defect: the Model destination is changed by text-replacing the source fragment `["model", "Model", "#CP-1"]` of app.js inside the rendered HTML, and the scope banner is spliced in by string replacement. destOf() maps only CP-1 to the "model" rail entry, so on model.html, whose rail link was patched to `#CP-MODEL`, the rail highlights "Analysis" instead of "Model".
- Failure scenario: any reformatting of DEST in app.js makes all three delivery paths refuse with "model_shell…", and the Model page always shows the wrong active rail item.
- Evidence: the code paths are deterministic, but I did not run a browser, so the rail highlight is unverified at runtime.
- Fix direction: pass the Model href and scope banner through the render payload (or as render() parameters) instead of patching the output, and let destOf map CP-MODEL to "model".

### Out of scope (one line each, optional)
- None found with root cause outside S04 that I verified.

### Checked and sound (short bullets: what you attacked that held)
- render.py data embedding: JSON uses `ensure_ascii`, `allow_nan=False`, and `<` is escaped to `<` inside a `type=application/json` script. The one-pass re.sub template stops payload text that contains `/*SCRIPT*/` from being substituted again. `--` is neutralised in the license comment. The CSP is `default-src 'none'` with no connect.
- app.js: every data value goes through textContent or attributes. Chart SVG is parsed as image/svg+xml with an element allowlist that strips on*, href, xlink:href and style. The only dynamic href is regex-checked (`^[A-Za-z0-9._-]+$`) or a `#`-fragment.
- Scope banner and layout.scope are html.escaped. The nav/anchor replacement targets cannot appear in the DATA payload (compact separators, escaped `<`).
- Handoff sha256 is checked before use in markdown_files, prepare and build_model, including for extra handoffs and forecast_exact. forecast_exact must bind the annual sha.
- Missing versus zero: blank cells become status missing with an explicit limitation, "0" stays known (literal_module, _literal_tables, _numeric_observations). Non-finite and exponent tokens are refused.
- rendering.py / financial_rendering.py: they re-authenticate before and after rendering, stage in a temp directory and rename atomically, refuse existing destinations, and never write into execution directories.
- table_markdown.markdown_cell / read_table_markdown round-trip, including pipes, `<br>`, backslashes and empty or space-padded cells. Parity validation is applied before writing.
- reader_summary number matching (whole-number boundaries, internal codes stripped) and its section-placement regex.
