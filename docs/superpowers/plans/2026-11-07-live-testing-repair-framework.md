# Live Testing and Repair Framework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Detect faults in the Issuer Library's front and back end on every change, prove that data flows correctly (sources → module handoffs → delivered handoffs → rendered report) through a real provider run, and record every fault so it can be repaired test-first.

**Architecture:** The existing Playwright walk (`apps/issuer-library/designs/browser_check.py`) captures every fault class into `faults.json` with artifacts, and each walk is isolated so one failure no longer hides the rest. A stdlib-only checker (`designs/flow_check.py`) traces hashes and numbers through a run folder independently of production code. The offline fake-provider walk uses it on every gate run, and it can also run on retained runs. A new paid walk (`designs/live_check.py`) drives the real engine through the app with an explicit spend cap. CI runs the offline gates.

**Tech Stack:** Python 3.13 stdlib, Playwright for Python 1.64.0 (test-only), Go 1.26 server, Node 24 + jsdom 26.1.0 (test-only), GitHub Actions.

**Spec:** The owner's request in session (2026-11-07): "create a robust live testing and repair framework to detect faults and bugs" across the updated front end and back end; "include provider runs to test if data flowing correctly". The owner skipped design questions; the calls the controller made are marked *(controller's call)*.

## Baseline found before planning (main at e562c366)

- `validate.py quick`: `FAIL fixture`. `designs/build.py:41` calls `built_from(folder, sources)`, but b1970e81 changed it to `built_from(files: dict[str, str], sources)` (`engine/store.py:537`). `FAIL node` follows from that, because `artifacts/issuer-library/design-fixture/workspace-data.js` is never built.
- Browser walk (chromium and firefox): `FAIL fake-provider run finishes through the real bridge: stopped: cpos_live_not_accepted: CP-0 not accepted within bounds`. The checker's review issue was "Place ### Readiness view directly after ### Reader summary, once: prose that states the view, before any table." 2758841f added `OPENING` (`src/deploy_workflow/owners/cpos_launch.py:178`). The production instructions carry the new rule; the fake engine (`designs/fake_engine/bridge.py`) never writes it.
- That one exception aborted the rest of chromium's walks, including the whole stopped-run walk: 34 passed and 2 failed, with about 20 checks never run. `validate.py report()` prints only the last 40 lines, so the browser gate's output loses chromium's results.
- Neither gate runs in CI, which is why both regressions merged.

## Global Constraints

- No provider call from `validate.py`, pytest or CI. Paid execution happens only through `live_check.py`, run explicitly with `--cap`. Provider keys come only from the launching environment and are never written to a file or log: redact every captured log.
- `flow_check.py` and `faults.py` import only the stdlib, and nothing from `src/` or `engine/`. Expected values stay independent of production code.
- Never modify `runs/`, `deliverables/` or `data/` (the `validate.py` `retained` gate). Calibration on retained runs only reads them.
- No stub or fake value standing in for real behaviour. No catch-all that hides a failure unless the fail-open is documented and logged. Every expected HTTP 4xx and every ignored request failure is listed explicitly with a one-line reason.
- Each task has an answer key, which the implementer does not edit, and a comparison, which the implementer does not weaken. Named per task.
- Changed Python passes `uv run python tools/quality_gate.py` (ruff, format, complexity ≤ 15, strict mypy on changed code; `tests/` is excluded from mypy).
- Fast targeted runs only: pytest under `timeout 300`. The browser walk takes about 5 minutes; run it in the background. Two browser walks must not run at once, because they use fixed ports 53901–53910.
- The whole PR stays at ≤ 800 changed lines.
- Every task report ends with a `Not verified:` line.
- Gate environment, from the repo root:
  - `FW_PYTHON=$PWD/.venv/bin/python`
  - `ISSUER_LIBRARY_JSDOM=/private/tmp/issuer-library-dom-check/node_modules/jsdom`
  - `FW_PLAYWRIGHT_PYTHON="/Users/ericguei/Documents/DEPLOY VII/.venv/bin/python"` (Playwright 1.64.0). Use that interpreter only; never modify that repository.
  - Commands: `python3 apps/issuer-library/validate.py quick` and `… browser`.

## Review Focus

1. Healthy real handoffs that round, scale (thousands/millions), negate with parentheses, or add `%` must not flood `flow_check` with "unsourced number" faults. Expected: normalisation is pinned by tests, and calibration on retained live runs lists every flagged number for a human to classify. Owned by Task 3.
2. Digits inside sha256 digests, ISO dates, file names and CSS values are not data. Expected: ignored. Owned by Task 3.
3. A provider key value printed by the server or engine must never reach `faults.json`, logs or artifacts. Owned by Task 2 (redact) and Task 4 (live server env).
4. A walk failing midway must still write `faults.json` and its artifacts; the next walk runs, and the gate exits non-zero. Owned by Task 2.
5. Run `live_check` without a key, without `--cap`, or with a non-positive or non-finite cap. Expected: exit 2 before any server or browser starts, with no spend. Owned by Task 4.

---

### Task 1: Fault capture in the browser walk

Agent: `mx-feature`. Review: `mx-precise`.

**Files:**
- Create: `apps/issuer-library/designs/faults.py` (stdlib only)
- Modify: `apps/issuer-library/designs/browser_check.py`
- Modify: `apps/issuer-library/validate.py` (`report()`, lines 63–68)
- Test: `tests/test_issuer_library_faults.py`. Add one `report()` test to `tests/test_issuer_library_gates.py`.

**Interfaces (produces):**
```python
# designs/faults.py
CRASH: re.Pattern[str]  # lines starting "panic: ", "fatal error: ", "Traceback (most recent call last):", "WARNING: DATA RACE"
IGNORED_FAILURES: tuple[str, ...] = ("net::ERR_ABORTED", "NS_BINDING_ABORTED")  # a navigation or frame swap cancels a load
def redact(text: str, secrets: Iterable[str]) -> str  # each secret of len >= 8 -> "[redacted]"
def crashes(log: str) -> list[str]  # each crash line plus up to 5 following lines
def http_fault(status: int, path: str, expected: frozenset[tuple[int, str]]) -> bool  # >=500 always; 400-499 unless expected
def request_fault(failure: str | None) -> bool
@dataclass
class Fault: walk: str; kind: str; detail: str; url: str = ""; artifacts: list[str] = field(default_factory=list)
# kind is one of: check, console, pageerror, http, requestfailed, server-log, flow, exception
class Faults:
    items: list[Fault]
    def add(self, walk: str, kind: str, detail: str, url: str = "", artifacts: list[str] | None = None) -> None
    def write(self, path: Path, scope: str, passed: int) -> None  # {"scope","passed","failed","faults":[asdict...]}
```
`browser_check.py` becomes importable: importing it has no side effects (no folder creation, no servers). The script runs through `main(argv: list[str]) -> int` under `if __name__ == "__main__"`. `serve()`, `sign_in()`, `SignedBrowser` and `errors_of()` keep their names; Task 4 imports them.

- [ ] **Step 1: Write the failing tests** in `tests/test_issuer_library_faults.py`. Load `faults.py` by path, as `tests/test_issuer_library_gates.py` loads `validate.py`.
  - `test_crashes_finds_go_panic_python_traceback_and_race`: a log holding benign lines, `panic: runtime error: index out of range`, `Traceback (most recent call last):`, `WARNING: DATA RACE` → 3 entries. Benign lines only → `[]`.
  - `test_redact_replaces_every_key_value`: `redact("a sk-abcdef123456 b", ["sk-abcdef123456", ""]) == "a [redacted] b"`.
  - `test_http_fault`:
    - `(500, "/api/workspace", frozenset())` → True
    - `(404, "/x", frozenset())` → True
    - `(404, "/x", frozenset({(404, "/x")}))` → False
    - `(200, …)` and `(304, …)` → False
  - `test_request_fault`: `"net::ERR_ABORTED"` → False; `"NS_BINDING_ABORTED"` → False; `"net::ERR_CONNECTION_REFUSED"` → True; `None` → False.
  - `test_faults_write_round_trips`: write, then read back `scope`, `passed`, `failed == len(items)` and each fault's fields.
  - In `test_issuer_library_gates.py`, `test_report_prints_every_fail_line`: `validate.report("x", False, "FAIL early\n" + "ok\n" * 60)` prints `FAIL early` (capsys).
- [ ] **Step 2: Run them to see them fail**: `timeout 300 .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_issuer_library_faults.py tests/test_issuer_library_gates.py`. Expected: FAIL (no `faults.py`, and the report line is missing).
- [ ] **Step 3: Implement `faults.py`. In `validate.report()`, when failing, print every output line starting `FAIL ` before the existing last-40-lines tail.**
- [ ] **Step 4: Wire `browser_check.py`.**
  - `note(False, …)` also adds `Fault(kind="check")`.
  - `serve()` sends the server's stdout and stderr to `S/server-<port>.log` instead of DEVNULL. It still reads the launch line, without a pipe that can fill and block. In `main`'s `finally`, each log is redacted with every value of `KEYS` present in the environment plus the dummy key, then scanned with `crashes()`; each hit becomes `kind="server-log"`.
  - `errors_of(page)` also registers `page.on("response")` and `page.on("requestfailed")` (Playwright 1.64 sync API: `response.status`, `response.url`, `request.failure` is `str | None`). App-origin responses go through `http_fault` with a module-level `EXPECTED_HTTP: frozenset[tuple[int, str]]`, which starts empty. Add an entry only for a status the walk deliberately provokes, with a reason comment. Failed requests go through `request_fault`.
  - The main loop runs each walk in its own `try`: `real_workspace`, `new_run(start=True)`, and `new_run(start="stop")` for chromium. On an exception it adds `kind="exception"`, saves a screenshot and `page.content()` of that walk's last open page to `S/<walk>-failure.png|.html` as artifacts, and continues with the next walk. Track the pages through `SignedBrowser`.
  - Write `S/faults.json` with scope `"offline: retained workspace and fake-provider runs; no provider called"` and print `faults: <path>`. Exit 1 when any fault is recorded.
- [ ] **Step 5: Run the unit tests (Step 2 command).** Expected: PASS.
- [ ] **Step 6: Prove the capture on the live baseline**, with Task 2 not yet applied. Run `python3 apps/issuer-library/validate.py browser` in the background with `FW_BROWSER_OUT=<scratch>/t1`. Answer key: the baseline section above. Expected:
  - exit 1;
  - `faults.json` holds the `CP-0 not accepted` fault for chromium and for firefox;
  - the `stopped:` walk lines for chromium now appear, because the stopped-run walk ran;
  - the gate output lists every chromium `FAIL`;
  - any other fault is reported, not silenced.
- [ ] **Step 7: Run the quality gate and commit.** `git add` the four files, then `git commit -m "Browser walk records every fault in faults.json and isolates each walk"`.

### Task 2: Repair the two baseline regressions

Agent: `mx-feature`. Review: `mx-precise`, batched with Task 1's re-review if one is open.

**Files:**
- Modify: `apps/issuer-library/designs/build.py:40-41`
- Modify: `apps/issuer-library/designs/fake_engine/bridge.py` (the `## Findings` lines)

Answer keys, not edited: the existing failing gates.
- `validate.py quick` → `FAIL fixture` / `FAIL node`.
- Task 1's `faults.json` → the `CP-0 not accepted` fault.

- [ ] **Step 1: Confirm both fail.** Run `python3 apps/issuer-library/validate.py quick`. Expected: `FAIL fixture`, `FAIL node`.
- [ ] **Step 2: Fix `build.py`.** Pass the delivery's verified file map, `{str(n): str(h) for n, h in delivery["files"].items()}`, to `built_from`, as `engine/store.py:563` does.
- [ ] **Step 3: Fix the fake engine.** For every module with an entry in `deploy_workflow.owners.cpos_launch.OPENING` (import it; do not copy the mapping), write `### <OPENING[module]>` and one prose line, "A fake engine view only.", where `_opens_with` (`cpos_launch.py`) requires it. Read `_opens_with` to place it, and do the same for CP-1's fixture-based section. Do not edit `designs/reader-fixture/CP-1.md`.
- [ ] **Step 4: Verify.**
  - `python3 apps/issuer-library/validate.py quick` → every line PASS.
  - `validate.py browser` in the background → exit 0 and `faults.json` `"failed": 0`.
  - Report the browser passed count; it should be higher than the baseline's 34 per chromium, because the skipped walks now run.
- [ ] **Step 5: Run the quality gate and commit:** `git commit -m "Fix fixture build and fake engine for the built_from and opening-view changes"`.

### Task 3: Independent data-flow checker

Agent: `mx-feature`. Review: `mx-precise`.

**Files:**
- Create: `apps/issuer-library/designs/flow_check.py` (stdlib only)
- Create: `tests/test_issuer_library_flow_check.py`
- Modify: `apps/issuer-library/designs/browser_check.py` (wire it into the fake-run walk)

**Interfaces:**
- Consumes: Task 1's `Faults.add(..., kind="flow")`.
- Produces:
```python
def numbers(text: str) -> set[str]
def run_faults(run: Path, sources: Path | None = None) -> list[str]
def report_faults(report_text: str, handoffs: Iterable[str], context: str = "") -> list[str]
def main(argv: list[str]) -> int  # flow_check.py <run_dir> [--sources DIR]; one fault per line, then "flow: N fault(s)"; exit 1 if any
```

Run-folder facts, verified on `runs/cpos-launch-live-002`:
- `completed-<sha>.json` has `"modules": {"CP-0": "requests/CP-0/<fp>/1.response.md", …}`, which is the accepted handoff per module. With no completed record (a stopped app run), use `run/<M>.md` for `M` matching `CP-[A-Z0-9]+`.
- Each `live/modules/<digest>/0.request.json` has `messages[1].text`. It is JSON with `module_id`, `sources` (`{name: sha256}`; `context` is one entry) and `handoffs` (`{U: {"sha256", "markdown"}}`).
- `<n>.tools.json` is a list of `{call_id, name, text}`. The names seen are `calculate`, `search_source`, `read_pages`, `list_sources`, `write_handoff` and `score_governance`.
- Delivered copies are `deliveries/<id>/CP-*.md`.

`numbers()` rules, pinned by test:
- First remove ISO dates (`\d{4}-\d{2}-\d{2}`) and hex runs of 16 or more characters.
- Match standalone numbers with optional thousands commas and a decimal part, not inside a word or file name.
- Normalise by dropping commas, sign, parentheses and `%`, and trailing fractional zeros. `7,940.0` → `7940`, `(1,234)` → `1234`, `-3.50` → `3.5`, `12%` → `12`.
- Drop single-digit results.

`run_faults` reports, one string per fault, naming the module and the value:
- (a) A module's received upstream `sha256`/`markdown` does not equal the accepted upstream handoff's bytes and text.
- (b) A `sources` entry's hash matches neither `sources/<name>` (when `--sources` is given) nor `run/inputs/<sha>`.
- (c) A number in a module's accepted handoff is not in `numbers()` of that module's corpus, which is:
  - every non-`write_handoff` `tools.json` text from its invocations;
  - the upstream handoffs it received;
  - `run/context.json`;
  - UTF-8-decodable files under `sources`;
  - `run/source-text/*.jsonl`.
  Instructions are not evidence and are excluded.
- (d) A delivered `CP-*.md` is not byte-equal to that module's accepted handoff.

`report_faults` reports each number in `report_text` that is not in the handoffs' or context's numbers.

- [ ] **Step 1: Write the failing tests.** A helper builds a two-module synthetic run (CP-0 → CP-1) in `tmp_path` with the layout above.
  - `test_numbers_normalises_and_ignores_digests_and_dates`: the examples above. A sha256 string and `2024-09-30` add nothing, `report-v2.md` adds nothing, and `7` is dropped.
  - `test_clean_synthetic_run_has_no_faults` → `[]`.
  - `test_number_absent_from_what_the_module_read_is_a_fault`: plant `7,941` in CP-1 → one fault naming `CP-1` and `7941`.
  - `test_upstream_hash_mismatch_is_a_fault`.
  - `test_source_hash_mismatch_is_a_fault`.
  - `test_delivered_copy_that_differs_is_a_fault`.
  - `test_report_number_not_in_handoffs_is_a_fault`, and `test_report_numbers_from_handoffs_pass`.
  - `test_main_exits_1_and_prints_count`.
- [ ] **Step 2: Run them to see them fail**: `timeout 300 .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_issuer_library_flow_check.py`. Expected: FAIL (module missing).
- [ ] **Step 3: Implement `flow_check.py`.**
- [ ] **Step 4: Run the tests.** Expected: PASS.
- [ ] **Step 5: Wire into the fake-run walk.**
  - The synthetic issuer folder gains `figures.md`, a copy of `designs/reader-fixture/CP-1.md`, so the fake engine's CP-1 figures have a source. Update the "3 files" expectation to 4.
  - After the `start=True` run completes, each `run_faults(workspace/"runs"/<id>, S/"issuer")` entry and each `report_faults(<report frame #view-root text excluding svg>, <delivered CP-*.md texts>)` entry becomes `note(False, …)` with `kind="flow"`.
  - Add one `note(True, "<browser>: data flows from sources to the report (flow check)")` when both are empty.
- [ ] **Step 6: Calibrate on retained real runs.** This only reads them and makes no assertions:
  - `.venv/bin/python apps/issuer-library/designs/flow_check.py runs/cpos-launch-live-002 --sources data/public-corpus/v1/TDG`
  - the same on `runs/cpos-sol-medium-20261105`; if its layout differs, say so.

  Report the fault count and the first 20 lines. For 5 flagged numbers, say whether each is genuinely absent from what the module read or is a normalisation gap. Change the normalisation only with a new test case; never loosen it to reach zero. Genuine findings on retained runs go to the owner.
- [ ] **Step 7: Verify, run the quality gate and commit.**
  - Browser walk in the background → exit 0 and the flow-check PASS line present for chromium and firefox.
  - `git commit -m "Independent data-flow check from sources to report"`.

### Task 4: Paid live walk through the app

Agent: `mx-feature`. Review: `mx-precise`, then `mx-adversary` (spend and keys).

**Files:**
- Create: `apps/issuer-library/designs/live_check.py`
- Create: `tests/test_issuer_library_live_check.py`
- Modify: `browser_check.serve()` only if it needs an option to keep the launching environment's provider keys. The default stays stripped.

**Interfaces:**
- Consumes:
  - `browser_check.serve/sign_in/SignedBrowser/errors_of` and `faults.Faults/redact/crashes` (Task 1);
  - `flow_check.run_faults/report_faults` (Task 3).
- Produces: `def live_evidence(run: Path, cap: Decimal, status_spent: str, modules: set[str]) -> list[str]` and `def main(argv: list[str]) -> int`.

CLI: `<playwright python> apps/issuer-library/designs/live_check.py --cap USD [--config sol-medium] [--modules "CP-1 CP-1A"] [--minutes 60] [--out DIR]`. It also needs `FW_PYTHON` and `ISSUER_LIBRARY_BINARY`. Import Playwright inside the walk function, so the refusal paths and `live_evidence` run under `.venv` without it.

Behaviour:
1. **Refusals.** Before any server or browser starts, exit 2 with one line on stderr when:
   - `--cap` is missing, ≤ 0 or non-finite;
   - none of `KEYS` is set.
2. **Announce.** Print `PAID RUN: config=…, modules=… (dependencies added by the launcher), cap=USD …, case=TDG as of 2024-09-30, workspace=…` before starting.
3. **Serve.** Start a fresh workspace under `--out` (default `tempfile.mkdtemp(prefix="issuer-library-live-")`) on port 53920, with engine root `apps/issuer-library/engine`. The launching environment's provider keys pass through to the server process only. Logs are redacted before writing.
4. **Walk** in chromium:
   - load the context file `runs/cpos-launch-live-002/context.json`;
   - choose the folder `data/public-corpus/v1/TDG`;
   - select `--config`, set the budget to `--cap`, set Advanced modules to `--modules`;
   - run Validate and review. If Start stays disabled because the provider is not configured, stop with a fault before any spend;
   - check the confirm box and Start, then wait up to `--minutes` for `#open-run`;
   - require the status to start with `complete`;
   - open the report, and require the Built from row count to equal the accepted modules.

   A stopped run is a fault. No paid step is retried automatically.
5. **Checks**, each a `note`/`Fault`:
   - `run_faults(run, sources=data/public-corpus/v1/TDG) == []`;
   - `report_faults(...) == []`;
   - `live_evidence(...) == []`;
   - the app's "Recorded spend: USD x" equals `status.json` `spent_usd`.
6. **`live_evidence`** follows the answer key `assert_live_evidence` (`tests/test_cpos_launch.py:988-1021`); do not edit that test. It requires:
   - every `live/calls.jsonl` row has a non-empty `request_id` and `reported_model == requested_model`;
   - the set of row `module_id`s equals `modules`;
   - 0 < Σ `settled_usd` ≤ `cap` (Decimal);
   - `status_spent` equals that sum, compared as Decimal;
   - when CP-1 is in `modules`, the filed literals `7,940` and `6,261` appear in the CP-1 accepted handoff.

   The walk also checks those literals in the report text.
7. **Output.** Write `faults.json` with scope `"live provider: <config>, TDG as of 2024-09-30, modules <…>, spend USD <x>"` and `summary.json` (`run_id`, `spent_usd`, `failed`, `report`) to `--out`. Exit 1 on any fault.

- [ ] **Step 1: Write the failing tests** (offline, subprocess under `.venv/bin/python`, with provider keys removed from the environment).
  - `test_refuses_without_cap`, `test_refuses_non_positive_or_nan_cap`, `test_refuses_without_any_provider_key`: each exits 2 with a message. Set `ISSUER_LIBRARY_BINARY` to a nonexistent path, so a refusal that came too late would fail differently, and assert that no `--out` folder is created.
  - `live_evidence` on a synthetic `calls.jsonl` and CP-1 handoff:
    - clean → `[]`;
    - reported ≠ requested → fault;
    - missing `request_id` → fault;
    - Σ > cap → fault;
    - status mismatch → fault;
    - module set differs → fault;
    - missing literal → fault.
- [ ] **Step 2: Run them to see them fail**: `timeout 300 .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_issuer_library_live_check.py`. Expected: FAIL.
- [ ] **Step 3: Implement `live_check.py`.**
- [ ] **Step 4: Run the tests.** Expected: PASS. Also run Task 1's and Task 3's test files, plus `python3 apps/issuer-library/validate.py quick`.
- [ ] **Step 5: Do not run the paid walk.** The controller asks the owner. Run the quality gate and commit: `git commit -m "Paid live walk through the app with spend cap and data-flow checks"`.

### Task 5: CI, docs and the verification record

Agent: `mx-feature`. Review: `mx-feature`, scoped (config and docs).

**Files:**
- Modify: `.github/workflows/quality-gate.yml` (new job)
- Modify: `.github/workflows/nightly-tests.yml` (new job on its existing schedule and `workflow_dispatch`)
- Modify: `docs/QUALITY-GATE.md` (section "Live testing and repair")
- Modify: `apps/issuer-library/README.md` (a pointer of five lines or fewer)
- Modify: `VERIFICATION.md` (one concise entry)

- [ ] **Step 1: Add the PR job `issuer-library-quick`.**
  - Steps: checkout (`fetch-depth: 0`); `astral-sh/setup-uv@v5` at 0.12.5; `uv sync --group dev`; `actions/setup-go@v5` with `go-version-file: apps/issuer-library/go.mod`; `actions/setup-node@v4` with node 24; `npm install --no-save --prefix "$RUNNER_TEMP/dom" jsdom@26.1.0`.
  - Run: `python3 apps/issuer-library/validate.py quick`, with `FW_PYTHON=$PWD/.venv/bin/python` and `ISSUER_LIBRARY_JSDOM=$RUNNER_TEMP/dom/node_modules/jsdom`.
- [ ] **Step 2: Add the scheduled job `issuer-library-browser`.**
  - Steps: the same setup, then `uv venv "$RUNNER_TEMP/pw"`, `uv pip install --python "$RUNNER_TEMP/pw" playwright==1.64.0`, and `"$RUNNER_TEMP/pw/bin/python" -m playwright install --with-deps chromium firefox`.
  - Run: `validate.py browser` with `FW_PLAYWRIGHT_PYTHON=$RUNNER_TEMP/pw/bin/python` and `FW_BROWSER_OUT=$RUNNER_TEMP/browser`.
  - `actions/upload-artifact@v4` of `$RUNNER_TEMP/browser` when `failure()`, kept 14 days. No provider key is set in any job.
- [ ] **Step 3: Docs.** `docs/QUALITY-GATE.md` "Live testing and repair" covers:
  - the offline commands;
  - the `faults.json` fields and kinds;
  - `flow_check.py` on a retained run;
  - the paid `live_check.py`:
    - it is an explicit command and never runs in CI;
    - the key comes from the environment;
    - the cap must cover the per-call hold (5.73 for sol-medium), so use 12;
    - the cost recorded for CP-0..CP-1A was about USD 0.93 in `runs/cpos-launch-live-002`;
  - the repair loop:
    1. read `faults.json` and its artifacts;
    2. write a test that fails for the reported cause at the surface where it was seen. The walk's own FAIL line counts when it already fails;
    3. fix;
    4. rerun the gate or walk;
    5. a pre-existing fault left unfixed goes to the owner.

  Add a decision record: jsdom 26.1.0 and Playwright 1.64.0 are the test-only tools `validate.py` already requires; CI installs pinned versions outside the project lock, and they are not runtime dependencies. Add a README pointer, and one `VERIFICATION.md` entry listing the actual results of Tasks 1–4.
- [ ] **Step 4: Verify.** Parse both workflow files with the YAML parser available (e.g. `ruby -ryaml -e 'YAML.load_file(ARGV[0])' <file>`), and check the job and step names. Under `Not verified:` record that the CI jobs run only on GitHub.
- [ ] **Step 5: Commit**: `git commit -m "Run the issuer library's offline gates in CI; document live testing and repair"`.

### After Task 5 (controller)

- Whole-branch review by `mx-architect`, including `confidence-review` and `rewrite-tournament` on the branch diff, and `uv run python tools/quality_gate.py`.
- Ask the owner for the paid run, giving config, modules, cap and expected cost. Then run `live_check.py`, triage its `faults.json` through the repair loop, and record the result in `VERIFICATION.md`.
