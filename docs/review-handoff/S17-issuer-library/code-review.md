SECTION: S17-issuer-library   PASS: code-review
COVERAGE: read fully: engine/store.py, engine/bridge.py, web/boot.js, web/actions.js, web/context-embed.js, web/report-adapter.js, web/index.html, validate.py, packaging/{build,runtime,smoke_test,sync_assets}.py, packaging/Smoke-test.ps1, designs/build.py, designs/fake_engine/{bridge,store}.py / skimmed: web/views.js, web/screen.js, designs/browser_check.py, web/screen.css, web/report-adapter.css, web/context-embed.css, web/context-form.html (checked by recomputing sync_assets output: byte-identical), web/brand.css (generated; matches sync output) / not read: none

Independence note: the code-review skill ran forked at effort `high` over all 24 files. Its output did not mention any adversarial findings. I did not read adversarial.md, repro/, a0*.py or docs/review-handoff/**. Two incidental exposures: a directory listing showed the file names inside this section's `work/` folder, and one grep printed the path `docs/review-handoff/S17-issuer-library/work/dedup_scan.py`. I opened neither. The skill did not verify anything, so I checked every finding myself. Scripts are in `<section>/cr/`. Run the .py files as `cd /home/user/final-workflow && PYTHONPATH=src:. .venv/bin/python <script>` and the .cjs files as `node <script>`.

### S17-issuer-library-C01  [medium] [CONFIRMED]  correctness
- Location: `apps/issuer-library/engine/store.py:17-18` (OUTPUT_SKIP / INPUT_NAME), used at `:380` (handoff_files) and `:401` (collect_runs)
- Defect: the output filter skips only instructions/prompt/calculations/verification names, so request files (`CP-*-request.md`, `CP-*-repair-request.md`) are listed as "Retained module output".
- Failure scenario: `runs/crc-liquidity-2020-001` contains `CP-3C-request.md`, the CP-OS instruction sent to CP-3C ("# CP-3C — consume the checked CRC liquidity handoff"). The app lists it as a second saved output of CP-3C, labelled "Request". As a result CP-3C gets no default output and its Overview card says "2 saved outputs. Choose one". `CP-2D-repair-request.md` is listed as a CP-2D output. In `tdg-valuation-2025-001`, `CP-2-request.md` leaves CP-2 with no default. INFORMATION-ARCHITECTURE.md:234 places requests in audit, not among outputs.
- Evidence: `cr/c01_request_as_output.py` prints `crc-liquidity-2020-001 CP-3C outputs= ['CP-3C-consumer.md', 'CP-3C-request.md'] default= None`, `crc-liquidity-2020-001/CP-3C-request.md -> ('Request', 'Retained module output')` and `tdg-valuation-2025-001 CP-2 outputs= ['CP-2-consumer.md', 'CP-2-request.md'] default= None`.
- Fix direction: add `request` to OUTPUT_SKIP, or classify request files as inputs/audit, so they are kept but never offered as module output.

### S17-issuer-library-C02  [medium] [CONFIRMED]  correctness
- Location: `apps/issuer-library/engine/store.py:551` (catalogue_reports -> built_from at `:493-494`)
- Defect: the documented per-deliverable fail-open `try` covers only the delivery.json/view.json reads. `built_from()` is outside it and hashes every `CP-*.md` beside the report with no `is_file` check and no error handling, so one unreadable handoff makes the whole store fail.
- Failure scenario: one deliverable folder holds a `CP-*.md` that cannot be read: a Windows scanner lock, a permission error, or a directory with that name. `workspace_store` raises and store.py exits non-zero. The app then opens with no runs and no reports, instead of hiding that one deliverable and listing it under Settings as the comment at `:514` promises.
- Evidence: `cr/c03_built_from_failopen.py` builds two deliverables, one with `CP-2.md` as a directory. Output: `workspace_store raised: IsADirectoryError [Errno 21] Is a directory: '.../deliverables/bad/CP-2.md'`. The good deliverable is lost too.
- Fix direction: build the whole report record, including `built_from` and `delivery["files"]["report.html"]`, inside the per-deliverable try, and skip non-regular files in `built_from` as `handoff_files` does.

### S17-issuer-library-C03  [medium] [CONFIRMED]  security
- Location: `apps/issuer-library/web/views.js:121` (comparisonChart `data-evidence="${module}:${p.row.line}"`; the same raw pattern is at `:142`, `:151`, `:158`)
- Defect: the output id is `<run folder>/<file name>`, taken from a file name in the workspace. It goes into an HTML attribute without `esc()` and is then assigned to `innerHTML`. comparisonChart draws every reader chart (`readerCharts`) and the Overview's `summaryCharts`.
- Failure scenario: a run folder on a shared or downloaded workspace contains a handoff with chart tables named `CP-1"><img src=x onerror=alert(document.domain)>.md`, which is a legal file name on macOS/Linux and needs no slash. store.py accepts it as CP-1's default output. Opening that run's Overview or CP-1 view injects the attacker's markup into the app shell. The app page's CSP (`script-src 'self'`, server.go:259) blocks the inline handler, so the impact is markup injection (spoofed links or controls, a broken view), not script execution. Any file name containing `"` also breaks the chart's evidence links.
- Evidence: `cr/c07_filename_xss.py` and then `cr/c07_filename_xss.cjs`. The store reports `output id: shared-run/CP-1"><img src=x onerror=alert(document.domain)>.md | charts: 4 | default: <same>`. The rendered chart HTML contains `<button class="chart-row" data-evidence="shared-run/CP-1"><img src=x onerror=alert(document.domain)>`.
- Fix direction: wrap the key in `esc()`, i.e. `data-evidence="${esc(`${module}:${p.row.line}`)}"`, in all four chart renderers. sourceLink already does this.

### S17-issuer-library-C04  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/engine/store.py:232-237` (output_label)
- Defect: when exactly one character follows the matched module code (for example `CP-2d.md` or `CP-1-.md`), `stem` is empty and `stem[0]` raises IndexError.
- Failure scenario: a run holds a valid `CP-0.md` and a hand-named `CP-2d.md`. The run-level fail-open hides the whole run, with every valid output in it, and Settings shows only `could not be read (IndexError(...))`.
- Evidence: `cr/c11_empty_stem.py` prints `runs shown: [] | issues: ["case-001: could not be read (IndexError('string index out of range'))"]`.
- Fix direction: label an empty stem from the file name, or skip only that file with an issue, so one odd name cannot hide the run.

### S17-issuer-library-C05  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/engine/store.py:360` (structured)
- Defect: handoffs are decoded with plain `utf-8`, so a UTF-8 byte-order mark stays in the text and the first heading fails to match.
- Failure scenario: a handoff saved with a BOM, which Windows editors and PowerShell 5 often add, is shown as one "Unstructured handoff" block with `parseError` "Body before first heading". Its reader summary and all chart tables are lost. visual_catalogue (`:558`) already uses `utf-8-sig`.
- Evidence: `cr/c08_bom.py` prints `no BOM: sections=12 ... summary=True charts=4` and `BOM: sections=1 first='Unstructured handoff' problem='Body before first heading' summary=False charts=0`.
- Fix direction: decode with `utf-8-sig` in both branches of `structured`.

### S17-issuer-library-C06  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/web/boot.js:20` (reload); also `web/actions.js:225` (Settings save/refresh)
- Defect: the guard asks for confirmation only while `#new-run` is visible. A prepared draft survives moving to other screens (browser_check checks this at designs/browser_check.py:327-334), so Reload clicked from any other screen discards it without asking. Settings "Save and reload" and "Refresh library" call `location.reload()` with no draft check at all.
- Failure scenario: the user loads a context, picks a folder and budget, then opens Help. The "workspace has changed" banner appears and they click Reload, or they save Settings. The run being prepared is cleared silently, although the comment at boot.js:19 says the reader is asked first.
- Evidence: `cr/c02_reload_guard.cjs` runs boot.js with stubs and prints `draft=1, new-run hidden -> confirm calls: 0 reloads: 1` and `draft=1, new-run shown  -> confirm calls: 1 reloads: 1`.
- Fix direction: test only `document.body.dataset.draft==='1'` in the guard, and send the Settings reloads through the same guard.

### S17-issuer-library-C07  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/web/views.js:102-106,121` (chartNumber / comparisonChart)
- Defect: any cell that chartNumber cannot parse is printed as a fixed "Not available". This drops the retained text, including the `Not supplied: <reason>` form that the launcher requires (src/deploy_workflow/owners/cpos_launch.py:371-382).
- Failure scenario: a web run's CP-1 chart row says `Not supplied: reported in EUR m`. The Overview shows charts without their tables (summaryCharts), so the reader sees only "Not available" and the reason is gone. Missing stays missing, so no value is invented, but the stated limitation is not shown. `(5.0%)` and a Unicode minus are also shown as missing.
- Evidence: `cr/c04_chart_number.cjs` prints `"Not supplied: reported in EUR m" -> Not available`, `"(5.0%)" -> Not available` and `"−1.2" -> Not available`. A scan of all real retained chart cells (`cr/c04_chart_scan.py`) found only one, a `'—'`, so the impact today is on new runs.
- Fix direction: when `n===null`, show the escaped cell text (for example `esc(p.value)`) instead of a fixed label, or show the `Not supplied:` reason.

### S17-issuer-library-C08  [low] [CONFIRMED]  security
- Location: `apps/issuer-library/validate.py:20` (KEYS / clean_env); same hard-coded list in `designs/browser_check.py:42` and `packaging/smoke_test.py:50`
- Defect: the gates remove only the OpenAI, Anthropic and OpenRouter keys. The provider map `KEY_VARIABLES` also has `copilot: COPILOT_GITHUB_TOKEN`, which passes straight through, so the docstring's promise "Provider keys are removed: no gate pays" is not enforced by the environment.
- Failure scenario: a developer with `COPILOT_GITHUB_TOKEN` exported runs `validate.py suite/full/browser`. Every pytest shard and the compiled app inherit the live token. The only protection left against a paid Copilot call is the `-m "not live"` marker; no gate path that pays was found.
- Evidence: `cr/c05_clean_env.py` prints `{'openai': False, 'anthropic': False, 'openrouter': False, 'copilot': True}` (present in the cleaned environment).
- Fix direction: build the strip list from `KEY_VARIABLES.values()` and the names in `deploy_workflow.model.redact`, instead of a hand-copied tuple, in all three scripts.

### S17-issuer-library-C09  [low] [CONFIRMED]  test-coverage
- Location: `apps/issuer-library/designs/browser_check.py:355` (new_run)
- Defect: `note("not set" in page.inner_text("#run-review") or True, ...)` always passes.
- Failure scenario: a regression that drops the "Cannot start · <KEY> is not set" warning in the review-only flow still prints PASS.
- Evidence: the expression ends in `or True`, so it is always truthy.
- Fix direction: remove `or True` and assert on the review-only server's actual warning text.

### S17-issuer-library-C10  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/web/screen.css:95` (`.ref`)
- Defect: `.ref` uses `var(--rb-ink-2)`, which is a Deploy VII report token. Neither screen.css nor any stylesheet loaded by index.html defines it; the `:root` at screen.css:5 defines `--muted`.
- Failure scenario: reference tokens such as T4.10 or F12, which `nameCodes` wraps in `<small class="ref">`, fall back to the body ink and lose the intended muted style.
- Evidence: `grep -n "rb-ink-2" web/screen.css web/brand.css` matches only the use at :95; index.html loads only screen.css.
- Fix direction: use `var(--muted)`.

### S17-issuer-library-C11  [low] [CONFIRMED]  efficiency
- Location: `apps/issuer-library/engine/store.py:383,385,405,419,420` (handoff_files / collect_runs)
- Defect: each output handoff is read in full 5 times per page load: sha256 twice in `handoff_files`, then sha256 twice more and `read_bytes` once in `collect_runs`. Inputs are read 4 times.
- Failure scenario: store.py runs as a new process on every page load, against a 120 s timeout. On a network share the I/O is about 5 times what is needed.
- Evidence: `cr/c10_reads.py` over the repo's runs prints `127 handoff files, 616 reads, 11.1 MB read vs 2.3 MB unique` and `reads per file: {5: 117, 4: 7, 1: 3}`.
- Fix direction: read each file once in `handoff_files`, then pass `(path, raw, digest)` on.

### S17-issuer-library-C12  [low] [PLAUSIBLE]  correctness
- Location: `apps/issuer-library/packaging/runtime.py:124-149` (bundle)
- Defect: `engine/runtime` is never cleared, and new wheels are extracted over the old `Lib/site-packages`. When a pin changes, the stale files and `*.dist-info` folders of the previous version stay in the shipped runtime. The reuse check (`:127-131`) also trusts the manifest without checking the extracted files.
- Failure scenario: `pydantic` is bumped in PINS. The rebuilt zip contains both `pydantic-2.14.1.dist-info` and the new dist-info, plus any modules the new version removed. `importlib.metadata` may then report the wrong version.
- Evidence: inspection of the code only. Reproducing it needs downloads from python.org and pypi.org, which the no-network rule forbids.
- Fix direction: when the manifest does not match, `rmtree(runtime)` before extracting.

### S17-issuer-library-C13  [low] [PLAUSIBLE]  simplification
- Location: `apps/issuer-library/web/report-adapter.js:64` (MODULE_NAMES)
- Defect: the module name map is a hand-copied duplicate of screen.js `groups`, `aliases` and the visual-catalogue aliases.
- Failure scenario: after a module is renamed or added in screen.js, or a catalogue alias is added, embedded reports show different names from the app around them. The static parts match today; `cr/c09_names_drift.cjs` finds only the extra alias entries that screen.js adds at runtime.
- Evidence: `cr/c09_names_drift.cjs` (no drift in the static parts today).
- Fix direction: generate the map in sync_assets.py, or have the server inject it from one source.

### Out of scope (one line each, optional)
- None found. The Go server's app CSP (server.go:259, `script-src 'self'`) is what turns C03 from script execution into markup injection; keep it.

### Checked and sound (short bullets: what you attacked that held)
- bridge.py: staged sources are rejected if symlinked, outside `sources/`, or changed since upload. `job` must sit in `<workspace>/intake/<id>`. The review id binds job, engine hash, sources, instructions and hold. Start re-runs the review, needs `provider_ready`, and writes its authorization once with `open("x")`. Errors pass through `Redactor.from_environ` plus a KEY_VARIABLES replace. A cap of NaN, Inf, 0, a negative or garbage is refused.
- bridge.py spend reporting: `Budget.spent` counts unknown charges at their full hold, so the shown spend does not understate a stopped run.
- actions.js: Start is gated on the server's `provider_ready`, the confirm checkbox and the busy/running flags. A lost Start response reconnects by id instead of starting again. All review and status values reach the DOM through `textContent`.
- context-embed.js and actions.js message bridge: the parent accepts only messages whose `event.source` is the sandboxed iframe, and the child answers only `parent`. The height value is bounded.
- sync_assets.py: recomputing its output in memory gives byte-identical context-form.html, brand.css and legacy-catalog.json. The template has exactly one `</head>` and one `</body>`.
- store.py: run folders must match SAFE_FOLDER, symlinked or non-regular handoffs are skipped, a curated pin that no longer matches is dropped and reported (not fatal), and a per-run exception hides only that run.
- designs/build.py: strict mode raises on a stale pin, and each report's built-from hash must match a shown run file.
- Smoke-test.ps1 and jobs.go: store.py and bridge.py run with `-I -B -X utf8`, so `ensure_ascii=False` output cannot raise on a Windows code page.
