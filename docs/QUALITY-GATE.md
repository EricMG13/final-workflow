# Quality gate for changed code

`tools/quality_gate.py` holds new and changed Python code to a readability,
maintainability, complexity and typing standard without requiring a rewrite of the
existing code. It runs on pull requests (`.github/workflows/quality-gate.yml`) and
locally:

```bash
uv run python tools/quality_gate.py            # compares with origin/main
uv run python tools/quality_gate.py --base main --json
```

## Scope: changed code, not changed files

The gate diffs the working tree against `--base`. In scope are every changed line and
the whole body of every function (decorators included) that a changed line falls in.
A new file is in scope whole. Findings outside that scope are dropped, so a one-line
edit in a 60-branch legacy function reports the function's complexity, while an edit
elsewhere in the same file does not. Standard library only (`ast`, `subprocess`,
`git diff -U0`); the checkers are the dev dependencies the repo already pins.

## Checks and thresholds

| Check | Threshold | Source of the threshold |
|---|---|---|
| `ruff check` with `tools/ruff-gate.toml` | the repo's rule set plus E501 (100 columns), C901, PLR0911, PLR0912, PLR0913, PLR0915 | repo `pyproject.toml`; pylint design limits at ruff's defaults (returns 6, branches 12, arguments 5, statements 50) |
| McCabe complexity (C901) | 15 | pydantic-ai (`mccabe max-complexity = 15`); ruff's default 10 is exceeded by 180 existing functions, Home Assistant uses 25 |
| `ruff format` | no change in scope | repo formatter settings |
| `mypy` | strict, errors in scope; `tests/` excluded | repo `[tool.mypy] strict = true`; tests are typed by convention only |

Comparable projects read for the thresholds: pydantic-ai (C90 at 15, mypy and pyright
strict), Home Assistant (PL and C selected, complexity 25, PLR09xx ignored), OpenBB
(PLR selected, max-args 8, max-branches 26, max-returns 9), LangChain core (`ALL`
minus C90 and PLR09), Code Climate defaults (complexity 5, 25-line methods, 4 arguments),
SonarQube S3776 cognitive complexity 15.

## Baseline this gate does not try to clear

Measured at `a313b50` on `src`, `apps` and `workflow.py`: 180 functions above
complexity 10 (62 above 15, 15 above 25); 160 with more than 5 arguments, 94 with
more than 12 branches, 56 with more than 50 statements, 33 with more than 6 returns;
356 lines over 100 columns; 46 files `ruff format` would change (27 of them in `src`);
mypy strict reports 33 errors in `src` and 110 with `apps/issuer-library/engine`.
That is why the gate is scoped to changed code. Reducing the baseline is separate work.

## Reading a report

```
src/x.py:120: ruff C901 `f` is too complex (17 > 15)
src/x.py:131: mypy return-value Incompatible return value type ...  [return-value]
src/x.py:140: format FMT ruff format would change
quality gate: 3 finding(s) in 2 changed file(s), 212 line(s) in scope
```

Exit 1 while findings remain, 2 when the gate itself could not run (unknown base ref,
tool missing). A `# noqa` or `# type: ignore[...]` with a reason is the escape hatch, and
the reviewer sees it in the diff.

## Fast tests while working, the full suite nightly

While working, run fast targeted tests only: the test files or `-k` selections that cover the
changed code, each run finishing within a few minutes (wrap it in `timeout 300`). Never run the
whole suite, the `test_owner_*` suites or anything whose fixture promotes CP-0/CP-1 during work.

The full suite, slow tests included, runs every night at 01:00 UTC in GitHub Actions
(`.github/workflows/nightly-tests.yml`, also startable by hand with "Run workflow"):

- six pytest shards (`tools/nightly_tests.py run`), balanced by test-file size, with the `live`
  and `browser` markers excluded and provider keys removed; each shard stops after 300 minutes;
- the Go server's `go vet` and `go test -race`;
- a report job (`tools/nightly_tests.py report`) that collects every FAILED and ERROR node id,
  compares them with `tests/nightly-known-failures.txt` and fails only on a failure that is not on
  that list or a shard that did not finish. The summary lists new failures and known failures that
  now pass; `failures.txt` is kept as an artifact for 30 days.

To accept a pre-existing failure, add its node id to the known list with a reason. Remove a line
once its test passes again. GitHub runs scheduled workflows from the default branch only, and on
this private repository the run uses the account's Actions minutes (several runner-hours a night).
