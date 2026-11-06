SECTION: S17-issuer-library   PASS: adversarial
COVERAGE: read fully: engine/store.py, engine/bridge.py, web/actions.js, web/views.js, web/report-adapter.js, web/context-embed.js, web/boot.js, web/index.html, validate.py, packaging/build.py, packaging/runtime.py, packaging/sync_assets.py, packaging/Smoke-test.ps1, packaging/smoke_test.py, designs/build.py, designs/fake_engine/bridge.py, designs/fake_engine/store.py / skimmed: web/screen.js (lines 1-440 read, every template sink checked by a scan), web/context-form.html (HTML sinks and fill path only), designs/browser_check.py / not read: web/*.css (brand.css, context-embed.css, report-adapter.css, screen.css)
Callers read for context (out of scope): jobs.go, server.go (CSP and request guards), discovery.go (verifyDelivery, folders), cpos_launch.prepare, cpos delivery ids, budget.Budget.
Repro scripts are in R/S17-issuer-library/work/. Scratch output is in work/tmp. No repo file was changed (git status clean). No provider or network call was made. The only local server (work/xss/serve.py) was bound to 127.0.0.1 and has been stopped.

### S17-issuer-library-A01  [medium] [CONFIRMED]  money/limits: spend misreported after a failure
- Location: `apps/issuer-library/engine/bridge.py:206-233` (start) and `:260-273` (main)
- Defect: `start` writes `spent_usd` and the "retained work / no automatic paid retry" note only for `ValueError`/`RuntimeError`. Any other exception after paid calls (OSError, KeyError, TypeError) goes to `main`, which writes `{"state":"failed","message":...}` with no `spent_usd`.
- Failure scenario: CP-1 starts. `progress.json` records `spent_usd: "0"`. A paid call settles USD 7.42, then a Windows sharing violation (OSError) escapes `run_live_handoffs`. `status.json` has no spend, so the UI (`actions.js:105`, `status.spent_usd ?? status.progress?.spent_usd`) shows "Recorded spend: USD 0". The real spend is 7.42, and the "no automatic paid retry" note is also missing.
- Evidence: `work/bridge_failure_spend.py` patches only the collaborators of the real bridge `start`/`main`. Output: RuntimeError gives `{"state":"stopped",...,"spent_usd":"7.42"}`. OSError gives `{"state":"failed","message":"[Errno 32] The process cannot access the file..."}`, with progress.json still `"spent_usd": "0"`.
- Fix direction: in `start`, record `spent()` and the retained-work note for every exception (for example `except Exception`, then re-raise or write once), or add `spent_usd` in `main`'s start branch when `run_dir` exists.

### S17-issuer-library-A02  [medium] [CONFIRMED]  path containment: a symlinked or junctioned delivery folder escapes the run and the workspace
- Location: `apps/issuer-library/engine/store.py:371-387` (handoff_files)
- Defect: the code refuses only a symlinked leaf file. `run_dir.glob("deliveries/*/CP-*.md")` follows a symlinked or junctioned `deliveries/<sub>` directory, so regular files outside the run (and outside the workspace) are parsed and returned in `/api/workspace`. This breaks the code's own rule: "a link out of the run is not a handoff". On Windows, any user can create a directory junction (`mklink /J`), and `is_symlink()` does not detect one.
- Failure scenario: `runs/acme-001/deliveries/link -> /home/u/private/` holding `CP-9.md`. The app lists `acme-001/deliveries/link/CP-9.md` as a module output and renders its text. A file symlink in the same folder is correctly refused.
- Evidence: `work/symlink_escape.py` gives `outputs: ['acme-001/CP-1.md', 'acme-001/deliveries/link/CP-9.md']` and `outside text leaked: True`. The existing test `test_a_link_out_of_the_run_is_not_read` covers only a file link.
- Fix direction: resolve each candidate and require `path.resolve().is_relative_to(run_dir.resolve())`, and refuse symlinked or junctioned `deliveries/<sub>` directories (`is_symlink() or is_junction()`).

### S17-issuer-library-A03  [medium] [CONFIRMED]  fail-open boundary and provenance: built_from globs the folder instead of using the verified manifest
- Location: `apps/issuer-library/engine/store.py:490-501` (built_from), called at `:551` outside the try in `catalogue_reports`
- Defect: `built_from` hashes every `CP-*.md` it globs in a verified delivery folder. It skips no directories, broken links or unreadable files, it is not covered by the documented fail-open `try`, and it ignores `delivery.json["files"]`, the list Go actually verified.
- Failure scenario (a): a directory, broken symlink or unreadable entry named `CP-notes.md` inside a deliverable raises IsADirectoryError, FileNotFoundError or PermissionError. store.py exits 1, Go reports "the workspace could not be read", and every run and report disappears. (b): a `CP-2.md` dropped into a deliverable but not listed in its delivery.json is shown under "Built from ... byte-identical by SHA-256" as if the report was built from it.
- Evidence: `work/store_attacks.py`. Case B gives `rc 1 stdout empty`, `IsADirectoryError: ... deliverables/acme-report/CP-notes.md`. Case F gives `listed in delivery.json: ['report.html','view.json','CP-1.md']` and `builtFrom: [('CP-1',...), ('CP-2','acme-001/CP-2.md')]`.
- Fix direction: iterate the `CP-*.md` names in the already loaded `delivery["files"]` (hash = manifest value), and keep the per-report work inside the fail-open `try`.

### S17-issuer-library-A04  [medium] [CONFIRMED]  swallowed error hides a whole run: output_label crashes on unusual file names
- Location: `apps/issuer-library/engine/store.py:230-245` (output_label)
- Defect: `stem = path.name[len(module)+1:-3]` assumes a one-character separator after the module code. An empty stem then hits `stem[0]` (IndexError). The filename-derived `prefix` is put into a regex without escaping (`re.fullmatch(rf"{module}-{prefix}attempt-...")`), which raises re.error or miscounts. Either error is caught by `workspace_store`'s broad except, which hides every module of the run.
- Failure scenario: a stray `CP-1x.md`, `CP-1-.md` or `CP-1-a(-attempt-1.md` beside valid handoffs makes the whole run vanish from the library (only a Settings issue line remains). `CP-1-[draft]-attempt-1.md` is labelled "attempt 1 of 0", and `CP-1(1).md` is labelled "1)".
- Evidence: `work/store_attacks.py` case A gives `runs: [] issues: ["acme-001: could not be read (IndexError('string index out of range'))"]`. Inline checks give `CP-1-a(-attempt-1.md -> PatternError missing )`, `CP-1-[draft]-attempt-1.md -> '[draft] · attempt 1 of 0'`.
- Fix direction: derive the stem by `removeprefix(module)` plus an optional separator, fall back to the file name when it is empty, and use `re.escape(prefix)`. A label failure should affect only that file.

### S17-issuer-library-A05  [medium] [CONFIRMED]  HTML injection of handoff values into the pinned CP-1 chart
- Location: `apps/issuer-library/web/screen.js:186-188` (trendChart: `${p.exact}`, `${p.label}`)
- Defect: the bar value (the T4.10 table cell) and the period label (the table header) go into `innerHTML` without `esc()`. Every other cell sink uses `esc()`/`rich()`.
- Failure scenario: a retained `runs/tdg-002/CP-1-attempt-2.md` whose Net sales cell contains markup (or an entity such as `&lt;5`) renders as live elements in the Performance chart. The chart can then show a figure different from the exact table cell beside it. The production CSP (`script-src 'self'`) blocks inline event handlers, so the confirmed impact is markup or value spoofing, not script execution.
- Evidence: `work/xss/make_ws.py`, `serve.py`, `check.cjs` (real Chromium against the real web/ files and the real store.py). Without CSP, `#CP-1/performance?c=tdg-002 __xss1 executed= true`. With the server.go CSP replicated, `executed= false` but `injected img elements: ["SPAN><img src=\"q\" onerror=...>"]`. A control payload in an ordinary handoff cell is escaped (`__ctl executed= false`, no element).
- Fix direction: wrap both in `esc()` (`${esc(p.exact)}`, `${esc(p.label)}`).

### S17-issuer-library-A06  [medium] [CONFIRMED]  identity collision: curated route keys and folder names override recorded identity
- Location: `apps/issuer-library/engine/store.py:590-600` (workspace_store `shown[key]`), `:524-531` (catalogue_reports)
- Defect: a curated run is keyed by its route key (`frontier-2020`, `tdg-guidance`, `ford-otosan-2024`, ...), while other runs are keyed by folder name. A run folder named like a route key overwrites the curated entry in `shown` with no issue line. A deliverable folder named like a curated report is relabelled "TransDigm Group · <curated label> · Latest", whatever issuer its `view.json` records.
- Failure scenario: a workspace with `runs/frontier-2020-001` and a new CLI run `runs/frontier-2020` shows only the new run, and the retained Frontier case disappears silently. `deliverables/tdg-fy2024-snapshot-7` holding a Ford Otosan delivery is shown as TransDigm, "CP-8 repairs applied", Latest.
- Evidence: `work/store_attacks.py` case C gives `runs: {'frontier-2020': ('frontier-2020', ['CP-2'])} issues: []`. Case D gives `issuer: TransDigm Group label: CP-8 repairs applied status: Latest` for a view.json issuer of "Ford Otosan".
- Fix direction: key runs by folder and keep the route key separate (or report a collision as an issue), and apply curated report labels only when `view.json` names the curated issuer.

### S17-issuer-library-A07  [low] [CONFIRMED]  attribute injection from folder and file names (macOS/Linux builds)
- Location: `apps/issuer-library/web/views.js:121,142,151,158` (`data-evidence="${module}:..."` with output id), `views.js:206-212` (routeHref puts `section` = report id into `href` without escaping, used at `views.js:340`, `screen.js:285`, workspace tabs)
- Defect: output ids (which include `deliveries/<sub>/` and the file name) and report ids (deliverable folder names) are placed in double-quoted attributes without escaping. Run folders are checked against SAFE_FOLDER; these names are not.
- Failure scenario: on the darwin build or a Linux dev run, a folder named `x"><img src=q onerror=...>` under `runs/<r>/deliveries/` or `deliverables/` breaks out of the attribute and injects elements on Overview or Reports. Windows file names cannot contain `"<>`, so the Windows builds are not affected, and the production CSP blocks inline script.
- Evidence: the same harness as A05. Without CSP, `#W-Overview/overview?c=acme-001 __xss2 executed= true` and `#W-Reports/list __xss3 executed= true`. With CSP, no script runs but injected `BUTTON>/A><img ...>` elements are present.
- Fix direction: `esc()` the output id and key in `data-evidence`, and `encodeURIComponent` the module and section segments in `routeHref` (or `esc()` the whole href at each sink).

### S17-issuer-library-A08  [low] [CONFIRMED]  packaging: a re-pinned runtime keeps stale wheels in the shipped ZIP
- Location: `apps/issuer-library/packaging/runtime.py:79-106` (bundle) together with `build.py:16-36` (the target is reused and every file is zipped)
- Defect: when the manifest does not match (a pin changed), new wheels are extracted over the existing `Lib/site-packages` without removing it first. Old `*.dist-info` folders and modules removed upstream survive and are zipped into `Issuer-Library-<arch>.zip`.
- Failure scenario: a pin is bumped and the build rerun into `artifacts/issuer-library/windows-amd64`. The package then holds both `pypdf-OLD.dist-info` and `pypdf-NEW.dist-info`, plus the stale module, so `importlib.metadata` and imports can resolve to old code that the manifest does not list.
- Evidence: `work/runtime_stale.py` uses offline fake downloads with the real `bundle` and prints `['pypdf', 'pypdf-NEW.dist-info', 'pypdf-OLD.dist-info'] stale module present: True`.
- Fix direction: `shutil.rmtree(runtime)` (and remove the manifest) before extracting a new runtime when the manifest does not match.

### Out of scope (one line each, optional)
- `tests/test_issuer_library_store.py::test_one_unreadable_run_or_report_does_not_take_the_library_down` fails here only because the reviewer runs as root, so `chmod 0` does not block reads. This is environmental, not a product defect (42 of the 43 related tests pass).
- go.mod requires go 1.26.0 while this host has go 1.24.7 with GOTOOLCHAIN=local, so the Go server could not be built here. Browser checks used a stub server replicating the server.go CSP.

### Checked and sound (short bullets: what you attacked that held)
- The bridge surface is only `review` and `start` on a Go-validated `intake/web-<32hex>` folder. `read_job` confirms the job is in its workspace intake, refuses symlinked or escaping staged sources and re-hashes each one. No arbitrary path or command reaches the bridge from the page.
- `review_id` binds the job (cap, modules, sources), the engine revision, the run id, the source hashes (including the context.json hash via CONTEXT_SOURCE_ID) and the instruction hashes. `start` recomputes and compares it, the authorization is one-shot (`open("x")` plus the Go `start.claim`), and an unconfigured provider is refused.
- Cap parsing refuses NaN, sNaN, Infinity, zero, negative and garbage values. `write_file` is atomic (mkstemp, fsync, replace). The stopped and failed messages are redacted (Redactor plus an exact key replace).
- `actions.js` renders every server and review value with textContent. The context form iframe has an opaque origin, both sides check postMessage sources, and its innerHTML sinks use constants only (loaded context values go through `.value`).
- `esc()`/`rich()` are correct (the bold and code substitutions run after escaping), and an ordinary hostile handoff cell is escaped (control in the A05 harness). The report iframe is sandboxed without allow-same-origin.
- Store file links use `quote()`. Run keys are restricted by SAFE_FOLDER. File-symlink handoffs are refused. A malformed table, body before the first heading or a BOM marks the handoff unstructured and visibly flagged rather than hiding it. Retained `runs/` show no cross-module hash dedup loss and no label crash (`work/dedup_scan.py`).
- `sync_assets.py` output matches the committed `context-form.html` byte for byte, and every replacement token is unique. The bundle copies no credential files (src, prompts and docs contain no .env, key or credential files). Smoke-test.ps1 and smoke_test.py use temporary roots, never start a run and remove their temporary folders.
- validate.py removes the OpenAI, Anthropic and OpenRouter keys, and the browser check uses the fake engine for Start. It does not remove COPILOT_GITHUB_TOKEN, but no gate starts a copilot config, so I found no paid path.
