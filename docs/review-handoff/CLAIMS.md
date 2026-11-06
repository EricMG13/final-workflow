# Claims checked before the final report (read at a313b50, no code changed)

## 1. "`cpos_handoffs.transport()` is only called from a test, so modules never get upstream handoffs"

Fact confirmed, conclusion refuted.

- `transport()` is defined at `src/deploy_workflow/cpos_handoffs.py:27` and sets the `ACTIVE`
  ContextVar. The only caller is `tests/test_cpos_app.py:375`. Nothing in `src/`, `apps/` or
  `workflow.py` sets `ACTIVE` any other way.
- Therefore `cpos_handoffs.prompt_messages()` (called from `prompts/factory.py:128`) always
  returns the messages unchanged in production, and `_render()` in `run_pathway.py:677` never
  takes the `deliver()` branch. The Markdown-transport path inside `cpos_handoffs.py`
  (`retain`, `prompt_messages`, `deliver`, `library_metadata`) is dead code outside that test.
- Production modules DO receive upstream handoffs, by a different path: `owners/cpos.py:347`
  builds each `HandoffTask` with the accumulated `handoffs` mapping (one entry per earlier module,
  checked against `retained_handoffs[*].upstream` hashes at `:345`), and
  `model/handoff.py:414-416` serialises `task.handoffs` into the module request. The launcher's
  `checker()` (`cpos_launch.py:588-590`) also requires each answer to cite every current
  handoff's sha256.
- Net: not a high-severity data-flow defect. Real finding: an unused second transport mechanism
  (maintainability, low). Severity of S02's claim should be lowered accordingly.

## 2. "The CP-8 run comparison has no code-level diff of the two bundles"

Confirmed for the `run_comparison` route.

- `owners/cpos.py:628 run_comparison` verifies both bundles only for integrity:
  `_comparison_bundle` (`:571-601`) checks receipt and file hashes, file-set completeness and
  that `report.html` re-renders from the retained View/ReportView. It then hands both bundles to
  the model as `sources` (`prior/...`, `current/...`) and accepts the answer through
  `handoff_delivery.comparison_files` (`:520-550`), which checks only the shape of the answer:
  exactly one "Dimension" table with the seven required row labels, plus the generic checker
  (`cpos_launch.checker`: as-of date present, source sha256 cited, reader-summary layout).
- No code compares prior `view.json` values with current `view.json` values on this route. A
  model answer that reports "Unchanged" for every dimension, with the right table shape and the
  right hashes cited, passes.
- The Decimal diff in `owners/cp8.py` (`LedgerInputs`, `ledger_inputs`, `MeasureDiff`,
  `:1004-1100`) belongs to the decision-ledger owner module (`DecisionLedgerSubmission`, used
  from `owner_workflow.py:373`). It diffs values the model quoted inside its own submission, not
  the two retained bundles, and it is not on the `run_comparison` path.
- Callers: `run_live_comparison` (`cpos.py:780`, used by the retained live run in
  `docs/rulings/2026-11-06-reader-cp8-comparison.md`) and the `--compare` replay CLI (`:813`,
  byte-equality check only).
- Net: S10's finding stands. AGENTS.md says CP-8 "compares deliverables from prior runs with the
  latest current run: values, periods, assumptions, ..."; today that comparison is entirely the
  model's text, validated for shape and citations, not for agreement with the bundle values.

Addendum (from S10 code review, verified): `cpos_handoffs.retain()` at line 55 reads `claim.plain`,
an attribute `deploy_vii.contracts.Claim` does not have. Any head with a claim would raise
AttributeError when the Markdown handoff is written. This confirms the transport path has never run
in production; it is dead and also broken.
