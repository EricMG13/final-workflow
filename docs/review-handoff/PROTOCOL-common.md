# Common rules for every section reviewer

Repo: `/workspace/final-workflow` (git HEAD `a313b50`, branch `main`, clean tree).
Review dir root: `<REVIEW_ROOT>`
Your section folder is `<review root>/<SECTION>/`. Its `files.txt` lists the files in scope.

## What the app is
A local Python 3.13 workflow. Issuer source files go to CP-OS (the orchestrator), which
runs analytical modules ("owners", `src/deploy_workflow/owners/cp*.py`). The modules
exchange Markdown handoffs. A separate delivery process turns those handoffs into
HTML reports, an HTML Model, charts and calculation JSON. `src/deploy_vii` is the
older Deploy V-derived engine (calculations, live runtime, renderers). `apps/issuer-library`
is a local web app. Read `/workspace/final-workflow/AGENTS.md` (short) for the project
invariants. The invariants that matter most for findings:
- Preserve exact amounts, missing versus zero, quantity family, units, currency,
  periods/dates and source identities across every boundary.
- Delivery must not invent replacement analysis. Missing handoff content stays an
  explicit gap.
- Paid provider execution is bounded (budget caps, max attempts). Provider keys come
  only from the environment. No credential leakage into records or outputs.
- Never mutate historical run directories (`runs/`, `deliverables/`, `cases/`).

## Hard rules
1. READ-ONLY on the repo. Do not edit, create or delete any file under
   `/workspace/final-workflow`. Do not run git commands that change state. Put every
   scratch script and output in your section folder.
2. No network calls and no provider calls. Do not run tests marked `live`. Do not set
   or read API keys.
3. Run Python as: `cd /workspace/final-workflow && PYTHONPATH=src:. .venv/bin/python <script>`.
   Targeted tests: `.venv/bin/python -m pytest -q -p no:cacheprovider <test path> -x`.
   Do not run the whole suite (17k tests, other reviewers share the CPU).
4. Known baseline (do not re-report unless the cause is in your files): 6 test files fail
   collection: tests/product/test_inputs_portfolio*.py (no module `scripts`),
   tests/prompts (no module `o2_case`), tests/research/test_attach.py and
   test_consumer_block.py (no module `cpdr_consumers`), tests/test_owner_rendering.py
   (missing docs/OWNER-RENDERING-LEASE.md).
   Also already known (do not re-report): tests/test_method_cp5.py
   test_upstream_oracles_are_the_manifest_pins (methodology.json pin drift),
   tests/test_connect_cp2d.py test_module_trace_lists_every_offered_cp1_fact ("19 US$" vs
   "19 US$ m"), tests/research/test_contracts.py test_decision_amendment_states_two_anchors
   (missing docs/decisions/0007-*.md).
   Go (apps/issuer-library/*.go): a scratch copy that builds is at
   `<review root>/S18-issuer-library-server/gocopy/`. Copy it into your own section
   folder before you add test files, then run `go vet ./...` and `go test ./...` there
   (the go1.26 toolchain is cached). Never run go commands inside the repo folder.
5. Stay in scope. You may read code outside your section to understand callers and
   callees, but report only defects whose root cause is in your section's files. If you
   see a serious defect outside scope, list it in one line under "Out of scope".
6. Do not recommend removing or weakening authentication, scoping, money/quantity
   invariants, state-machine or idempotency guards, rollback/finally/locks, timeouts or
   retries. Do not report style, naming, formatting, missing docstrings or type-hint nits.
7. Docs in the repo (README, VERIFICATION.md, METHODOLOGY-REVIEW.md) can be stale.
   Trust the code. A broken documented contract is a finding only if callers rely on it.

## Finding format (your final message MUST use this; the parent agent sees only your final message)

```
SECTION: <SECTION>   PASS: <adversarial|code-review>
COVERAGE: <files read fully> / <files skimmed> / <files not read>

### <SECTION>-<A|C><nn>  [<critical|high|medium|low>] [<CONFIRMED|PLAUSIBLE>]  <category>
- Location: `path/to/file.py:LINE` (function name)
- Defect: one sentence.
- Failure scenario: concrete input/state -> wrong output/crash/leak.
- Evidence: repro command and the observed output (short), or for PLAUSIBLE the exact
  reason it could not be reproduced. Repro script path in your section folder.
- Fix direction: one sentence.

### Out of scope (one line each, optional)
### Checked and sound (short bullets: what you attacked that held)
```

Severity guide: critical = silent wrong financial figure/period/currency/source in a
final deliverable, credential leak, unbounded paid spend, or data destruction;
high = crash or wrong result on a realistic input, invented analysis, broken resume/
idempotency; medium = wrong result on an edge input, swallowed error that hides a
failure; low = minor robustness issue with a real trigger.
Use A for adversarial-pass IDs and C for code-review-pass IDs. Rank most severe first.
Report at most 15 findings. Quality over count: one reproduced defect beats five guesses.
Also write the same report to `<your section folder>/<pass>.md`.
