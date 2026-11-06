SECTION: S05-cp0-cp1   PASS: adversarial
COVERAGE: read fully: src/deploy_vii/cp0_workflow.py, src/deploy_vii/cp1_quality.py, src/deploy_vii/cp1_workflow.py, src/deploy_workflow/owners/cp1a.py, src/deploy_workflow/owners/cp1b.py / skimmed: src/deploy_workflow/owners/cp1c.py (about 2,600 of 3,376 lines: parsing, ratios, statistics, tie-out, valuation context T1C.9-11, validation, view, reader), src/deploy_workflow/owners/cp1d.py (about 1,900 of 2,573 lines: bridge parsing, basis-amount reading, outcome, totals, tie-outs, shares, conversion, validation, Stage 2 adapter) / not read: cp1c and cp1d Stage 2 submit/probe boilerplate after the validator. Targeted tests run: tests/test_method_cp1d.py, tests/test_owner_cp1b.py, tests/test_cp1c_valuation_context.py (712 passed, 4 skipped).

Repro scripts are in /tmp/claude-0/-workspace-final-workflow/10d71552-cdca-5952-86dc-d4ef0b76ab9e/scratchpad/review/S05-cp0-cp1/. Run each as: cd /workspace/final-workflow && PYTHONPATH=src:. .venv/bin/python <script> (repro_cp1_envelope_binding.py also takes the section folder as its first argument).

### S05-cp0-cp1-A01  [high] [CONFIRMED]  quantity family / currency of a model-cited amount
- Location: `src/deploy_workflow/owners/cp1d.py:588` (`_basis_amounts`), `:784` (`_shape_issue`), `:759` (`_outcome`), `:1061` (`_assessment_rows`)
- Defect: the CP-1D "accepted basis" amount is any single numeral in the cited quote. It is stamped as a source amount in the bridge's currency and MILLIONS, and nothing checks the numeral's unit, currency or quantity family.
- Failure scenario: the model marks "Procurement programme savings" (claimed 3.00) Partly supported and cites a quote whose only numeral is a percentage, a count, basis points or another currency's amount. The validator accepts it. T1D.2.a01.basis/accepted become USD 2 m, 2 m, 1 m or 1.50 m, and that number flows into supported EBITDA (T1D.3), the add-back shares (T1D.5) and restated leverage (T1D.6).
- Evidence: `repro_cp1d_basis_unit.py` adds four sentences to the positive bridge page:2 and cites each one:
  `percent ACCEPTED: basis 2 MILLIONS USD | accepted 2 MILLIONS | fraction 0.666...` ("cover 2% of supplier spend")
  `count ACCEPTED: basis 2 MILLIONS USD ...` ("cover 2 of the ten supplier categories")
  `currency ACCEPTED: basis 1.50 MILLIONS USD ...` ("cover EUR 1.50m of the saving")
  `bps ACCEPTED: basis 1 MILLIONS USD ...` ("improve margin by 1bps")
  `validation_issues` returns no issue for any of them. The `_one_whole_run` docstring explicitly lets `2.5m` and `25bps` through.
- Fix direction: accept a basis numeral only when the quote states it in the bridge's money unit and currency (or no unit), and refuse "%", "bps", count nouns, other ISO currencies and other scale suffixes.

### S05-cp0-cp1-A02  [medium] [CONFIRMED]  source/period identity in a tie-out
- Location: `src/deploy_workflow/owners/cp1c.py:1206` (`_tie_out`), `:1244` (`_tie_out_settled`)
- Defect: T1C.6 compares the issuer line on the peer source with CP-1's LTM ratio and never compares the two periods. The difference fact takes CP-1's period, and equal ratios read "Reconciled".
- Failure scenario: the peer sheet's issuer line is dated 2023-12-31 and CP-1's LTM column is 2025. T1C.6 shows "Reconciled" for every metric with period "LTM Q4 25". The module limitation then claims the issuer line "is tied to CP-1", which gives false assurance that the peer summary's definitions and period match the issuer's.
- Evidence: `repro_cp1c_tieout_period.py` -> `issues: ()` and `total_leverage_adjusted sheet period: Twelve months to 2023-12-31 | cp1 period: LTM Q4 25: 2025-01-01 to 2025-12-31 | diff period: LTM Q4 25... | result: Reconciled` (the margin gives the same result).
- Fix direction: when the issuer line's period end differs from the end of CP-1's LTM column, make the difference "Not compared" with a stated period-mismatch reason (or refuse the sheet).

### S05-cp0-cp1-A03  [medium] [CONFIRMED]  wrong/impossible periods pass response validation
- Location: `src/deploy_workflow/owners/cp1c.py:335` (`_period_end`), `:2510`/`:2531` (`_assessment_set_issues`, `_content_issues`)
- Defect: a peer period end is checked only as a calendar date. A period end after the run as-of date, or years before the issuer's LTM period, is read and included, and it enters every median when the model calls the peer "Comparable" without a limitation.
- Failure scenario: a peers page has Alder Ridge at 2027-12-31 (after as-of 2026-01-10) and Brookmere at 2012-12-31. The oracle submission (both "Comparable") passes, both peers are Included, `T1C.4.total_leverage_adjusted.n` is 4, and no limitation mentions either period. By contrast, the EV comps in the same module are windowed (24 months), and the context file refuses dates after as-of.
- Evidence: `repro_cp1c_period_end.py` -> `issues: ()`, `p01 period_end 2027-12-31 included Included`, `p02 period_end 2012-12-31 included Included`, `median leverage n 4`.
- Fix direction: refuse a sheet with a period end after the run as-of date, and require "Partly comparable" or "Not comparable" plus a limitation (or add a Python limitation) when a peer's period end is outside a stated window around the issuer's LTM end.

### S05-cp0-cp1-A04  [medium] [CONFIRMED]  unknown treated as better than missing (QA ceiling)
- Location: `src/deploy_vii/cp1_quality.py:94-95` (`_lineage_basis`)
- Defect: every `_CALCULATED` register kind (`source_check`, `period_check`, `normalization`, `construction`, `basis`) gets the "calculation" ceiling (Calculated, weight 9) without the row being read. A BLOCK reconciliation check with `calculated_value=None` ("Reported value or independent components are unavailable") is therefore not treated as missing evidence. The function's own docstring says it should be ("an absent calculated amount is missing evidence"), and `_VALUED` kinds with no amount do get "missing" (weight 0).
- Failure scenario: a narrative finding cites a BLOCK `source_check` or `period_check` evidence id (narrative allows any catalogue id). The QA review may classify that lineage as "Calculated", which raises the CP-1 confidence score and band carried into the promoted envelope and the deliverable.
- Evidence: `repro_cp1q_block_check.py` builds a real `Reconciliation(status="BLOCK", calculated_value=None, ...)` record -> `BLOCK check, calculated_value=None -> calculation Calculated 9`.
- Fix direction: parse calculated-kind rows and return "missing" when the calculated value is None (and consider "missing" for a BLOCK status), as already done for `_VALUED` kinds.

### S05-cp0-cp1-A05  [medium] [CONFIRMED]  envelope read-back does not bind QA, gap limitations or registers hash to the journal
- Location: `src/deploy_vii/cp1_workflow.py:601` (`cp1_binding_issues`), `:644` (`read_cp1_envelope`)
- Defect: the binding check compares the receipt's `registers_sha256` and `quality_report_sha256` with the envelope's own fields, which both come from the export files. Nothing compares them, `gap_limitations` or `journal` with the `CP1Handoff` the journal retains for the promoted quality step. A consistently rewritten Markdown + sidecar + receipt therefore passes, which the docstring says this function prevents.
- Failure scenario: an export directory (passed to `cp1_render.render_cp1_envelope` or `model_destination_html`) has its gap-register limitations dropped, its registers hash swapped or its QA report replaced. `read_cp1_envelope` returns it, and the page renders without the gaps or with the substituted QA.
- Evidence: `repro_cp1_envelope_binding.py` (a stub snapshot with a real `Module`/`Envelope`/`write_envelope`) -> `genuine ACCEPTED: gap_limitations= ('FY2024 comparatives absent...',)` and `forged ACCEPTED: gap_limitations= () registers= b39d7491ccc7`. The in-repo write-then-read callers (`financial_rendering.py:144`, `financial_workflow.py:2573`) are not exposed; the directory-taking renderers are.
- Fix direction: load the promoted attempt's `CP1Handoff` (as `write_cp1_envelope` and `_recheck_handoff` do) and require the envelope's registers hash, gap limitations, QA report hash and journal inputs to equal it.

### S05-cp0-cp1-A06  [low] [CONFIRMED]  contradictory unit/currency basis accepted
- Location: `src/deploy_workflow/owners/cp1c.py:349` (`_basis`)
- Defect: `_basis` returns on the first page:1 Basis line that holds the supported clause pair and ignores any other Basis line that states another currency or scale.
- Failure scenario: page:1 has "Basis: EUR; amounts in thousands." and then "Basis: ...; USD; amounts in millions.". The sheet is read as USD MILLIONS, and the T1C.2 source amounts are labelled USD millions although the source contradicts itself.
- Evidence: `repro_cp1c_basis_lines.py` -> `ACCEPTED: USD MILLIONS 1000000 [Decimal('200.0')]`.
- Fix direction: refuse the table (`Peer table not found`) when more than one Basis line is present or any Basis clause conflicts with the supported pair.

### Out of scope (one line each, optional)
- `src/deploy_workflow/owners/period_basis.py:209` `currency_basis` returns USD without reading the CP-1 register when there is no context (downstream earnings code then refuses a non-USD register, so it fails closed).

### Checked and sound (short bullets: what you attacked that held)
- cp0: duplicate or missing source assessments, unready source with non-blocked fidelity, `issuer_confirmed=false`, and a resubmitted different payload are all refused. Resume recomputes from the retained payload instead of trusting stored output.
- cp1_workflow: each stage is recomputed from raw payloads before registers, preview or promotion (`_stage_registers`). The financial stage must bind the retained source step hash. Stale inputs are refused. A QA "Blocked" verdict refuses promotion. `write_cp1_envelope` refuses an existing destination and writes the receipt last.
- cp1_quality: coverage marks only `known`/`not_applicable` facts present; an empty mandatory register, an unassessed dimension, missing story links and unassessed funding all stay absent (unknown is not treated as pass). Conflicting lineage for one evidence id raises.
- cp1c peer parsing: parenthesised or thousands-separated amounts, more than one decimal place, non-ASCII digits, a bad date, a repeated label (page:1 or page:2), a missing or duplicated issuer line, another currency or another unit all fail closed. Missing stays None; a non-positive denominator is `not_applicable`; a zero median is not a known 0 outlier count. The 38-digit half-even context is used throughout.
- cp1c valuation: dates after as-of are refused by the context rules. Non-positive EV/EBITDA is excluded. NTM is not applied to LTM EBITDA. CP-1 EBITDA must be a known positive MILLIONS amount, otherwise the implied EV is an explicit gap.
- cp1d: an unstated bridge amount is never treated as 0 (gaps propagate to totals, shares and conversion). Sums are exact (Inexact/Rounded traps). A zero or negative EBITDA basis gives `not_applicable`. Recurring forces 0. The basis must be above 0 and below the claimed amount. The CP-1 operands must share one period and the run currency, and the bridge Basis line pins the period, currency and unit.
- cp1b: only the two pinned period pairs are accepted; the comparison label is derived by Python; a context pair mismatch and an unresolved current period are refused; an unreadable fiscal year fails closed.
