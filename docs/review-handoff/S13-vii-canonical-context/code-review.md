SECTION: S13-vii-canonical-context   PASS: code-review
COVERAGE: The forked code-review skill read all 14 files. I re-read these in full to verify: prose.py, canonical_kpis.py / I read the relevant parts of: canonical_audit.py, canonical_tables.py, canonical_gaps.py, business_context.py, quotes.py, narrative_projection.py, quality.py, inputs/portfolio.py / I did not open these myself (the skill covered them; no finding is rooted there): source_context.py, narrative.py, inputs/__init__.py, __init__.py

Independence note: I wrote the reviewer constraint line before calling the skill. The forked code-review run still read docs/review-handoff/S13-vii-canonical-context/adversarial.md. It said 4 of its findings matched adversarial A01, A02, A03 and A06 (C02, C01, C05 and C04 below), and it named A04 and A05 as well (A04 is close to C07). I did not read that file or any repro/a0* file. I re-derived and re-reproduced every finding below myself, with my own scripts in cr/. I dropped A05 (no check of the period written next to a figure reference) because it came only from the adversarial pass. Also, the skill's output contradicts itself: it says "the code-review skill was not run" but is labelled as the skill's forked execution. Its findings had no repro scripts; all the evidence below is mine.

All repro scripts are in /tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S13-vii-canonical-context/cr/ and run as `cd /home/user/final-workflow && PYTHONPATH=src:tests:. .venv/bin/python <script>`.

### S13-vii-canonical-context-C01  [high] [CONFIRMED]  correctness
- Location: `src/deploy_vii/canonical_kpis.py:311-342` (_kpi_rows); shown at `src/deploy_vii/canonical_tables.py:512` (T4.9 Period) and `:625` (T4.10 cell period)
- Defect: A trailing-twelve-month ratio on a QUARTER column (leverage, interest/capex coverage, ffo/cfo/dcf_to_debt) is computed from the rolling 4-quarter cells (`selected_basis`). But the row's `display_basis_id` is the quarter's own historical basis. So T4.9 "Period" and the T4.10 cell `period` give the single quarter's dates.
- Failure scenario: Q3 2025 column with quarter EBITDA 25, LTM EBITDA 100 and debt 500. `total_leverage_reported` = 5.0x (debt / LTM EBITDA), but its period reads "Q3 25 (2025-07-01 to 2025-09-30)". A reader or downstream consumer takes it as based on quarterly EBITDA. Period identity is lost at the CP-1 register boundary.
- Evidence: `cr/c_ltm_basis.py` prints `value: 5`, `display_basis is quarter basis: True`, `operands basis is rolling: True`.
- Fix direction: Label the T4.9/T4.10 period from the basis the operands actually use (the rolling basis for `scope != "own"` on QUARTER columns), or carry that basis id on CanonicalKpi.

### S13-vii-canonical-context-C02  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/canonical_audit.py:493-526` (absent_input_limitation); used at `canonical_audit.py:630-640` and `canonical_gaps.py:255`
- Defect: On a public pack, any BLOCK check with `difference is None` becomes a WARN "Absent input" limitation. The function never requires a term with `amount is None`. A structural blocker that suppressed a computable difference is therefore also downgraded: quarters that do not tile the FY dates, or unknown expense presentation.
- Failure scenario: FY revenue 150 and four quarters 20/25/30/35, all present, but the quarter dates do not span the FY (52/53-week calendar, or a gap or overlap). The check is BLOCK "Four dated discrete quarters do not span the reported FY" with difference None. It is recorded as WARN "Absent input ... (rulings item 82)" with no absent term listed. The 40 mismatch and the period misalignment are hidden, and QA becomes Restricted instead of Blocked.
- Evidence: `cr/c_absent.py`: both blockers print `BLOCK difference: None | sum of terms would be 110 vs reported 150` and then `-> Absent input, stated as a limitation ...`.
- Fix direction: Downgrade only when at least one term has `amount is None` (or when the blocker is a listed disclosure-absence blocker). A period-span or tiling blocker stays BLOCK.

### S13-vii-canonical-context-C03  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/business_context.py:858-866` (governance_sponsor_score)
- Defect: The High-quality adverse-action override (`high_action`) only applies when fewer than `MIN_SCORED_DIMENSIONS` dimensions are scored. With 4 or more, an adverse row that has no dimension label drops out of the composite. Adding favourable evidence therefore lowers the risk level from High to Low.
- Failure scenario: A behaviour flag "dividend recap" (Extraction-Oriented, High evidence, dimension null) plus 3 Supportive dimensions gives High. Add a 4th Supportive dimension and T2D.8 shows composite 1, "Sponsor / Governance Risk Level: Low", while `high_risk_action=True`.
- Evidence: `cr/c_governance.py` prints `3 supportive dims -> Not Scorable High high_action= True` and `4 supportive dims -> 1 Low high_action= True`.
- Fix direction: With 4 or more scored dimensions, set the composite to at least 5 (High) when `high_action` is true, or require adverse High-evidence rows to carry a dimension.

### S13-vii-canonical-context-C04  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/canonical_kpis.py:198-206` (_canonical_frame)
- Defect: Derived adjusted EBITDA adds every `addback:` cell in the column, including `NOT_SOURCED` ones (an add-back with no row for the column's periods). The Model's own derivation (`model/statements.py:210-215`) skips those cells, so the canonical value becomes COMPONENT_MISSING where the Model shows a figure.
- Failure scenario: A column with reported EBITDA 45, no stated adjusted EBITDA, and an add-back whose cell reads NOT_SOURCED there (for example a column over derived periods, or an LTM column). Canonical `adjusted_ebitda` is None/COMPONENT_MISSING with the note "derived from components", while the Model shows 45. Adjusted leverage, coverage, margin and trailing-4Q KPIs then go unavailable in CP-1 only. Note: the adapter (`financial_adapter._addbacks`) writes NOT_STATED placeholders for base periods, so this only triggers where a cell is genuinely NOT_SOURCED.
- Evidence: `cr/c_addback.py` prints `canonical adjusted_ebitda: None COMPONENT_MISSING Reported value unavailable; derived from components` and `model/statement adjusted_ebitda: 45 None`.
- Fix direction: Filter `cell.reason != "NOT_SOURCED"` in the adjustments tuple, as `statements._income` does.

### S13-vii-canonical-context-C05  [medium] [CONFIRMED]  security
- Location: `src/deploy_vii/quotes.py:110-123` (quoted)
- Defect: `quoted` accepts any normalised substring with no token or word boundary. A piece of a larger number, or a single letter, passes as a verified quote. It is the shared matcher behind citation checks (`readiness.py:161`) and the covenant threshold check (`cp4_legal.py:528,548`).
- Failure scenario: Quote "shall not exceed 12.50:1.00". `quoted("2.50:1.00", quote)` is True, so `cp4_legal._threshold_issues` accepts a threshold_text of 2.50:1.00, and threshold_value 2.50 is parsed from it. A 12.50x covenant is recorded as 2.50x. Likewise, `quoted("1.2 billion", "$11.2 billion")` and `quoted("a", page)` are True.
- Evidence: `cr/c_misc.py` prints `True` for all three cases.
- Fix direction: Require the match to start and end on a word or number boundary (no alphanumeric or digit-separator character just outside it), or give value-token callers a boundary-aware variant.

### S13-vii-canonical-context-C06  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/canonical_tables.py:322` (_constructed)
- Defect: T4.8 sorts operands into Full-Year / Current Stub / Prior-Year Stub by sign alone. Every negative term becomes "Prior-Year Stub", which is only right for LTM = FY + YTD - PYTD.
- Failure scenario: A derived Q4 = FY2024 - 9M YTD2024 lists the same-year 9M YTD under "Prior-Year Stub". Q2 = H1 - Q1 lists Q1 there, and a trailing 4-quarter LTM puts every quarter under "Current Stub". The register gives the wrong period role for each component.
- Evidence: `cr/c_t48.py` (TDG fixture plus a 9M YTD period). The Q4 24 row shows `field_2: +1 * FY2024`, `field_3: None`, `field_4 (Prior-Year Stub): -1 * YTD9M2024`.
- Fix direction: Choose the bucket from the referenced period's fiscal year compared with the construction's, not from the coefficient sign.

### S13-vii-canonical-context-C07  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/prose.py:136-145` ("coverage" label) and `:93` (bare-year label)
- Defect: The bare-figure guard treats any "N of M" as a pack-coverage label and any 19xx/20xx token as a year. Unsupported issuer figures in model prose therefore pass with no reference.
- Failure scenario: CP-1 or CP-1A prose saying "Covenant headroom was breached in 3 of 4 quarters." or "Margin fell by 2024 basis points." raises no issue and reaches the deliverable as an unreferenced figure.
- Evidence: `cr/c_misc.py`: `prose.check(...)` returns `()` for both, while "5x" is flagged.
- Fix direction: Limit the coverage label to pack nouns ("N of M pages/sources/spans") and refuse a year token that a quantity noun follows (basis points, %, bps).

### S13-vii-canonical-context-C08  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/narrative_projection.py:120-121` (_passage, IssuerPart), used for Claim.text at `:160-170`
- Defect: The raw issuer name goes into run text, where `[ ] { }` are reserved syntax.
- Failure scenario: With issuer name "Acme Holdings [UK] Ltd", "[UK]" parses as a chip, and `prose_issues` reports "Unresolved reference: UK", so CP-1 module validation fails. "Acme [Holdings Ltd" makes `Claim(...)` raise, which crashes `project_narrative`, and with it `canonical_tables`.
- Evidence: `cr/c_misc.py`: the first and third names give `('Unresolved reference: ...',)`, and the second makes the Claim raise a ValueError.
- Fix direction: Escape or strip the reserved characters from the issuer name when splicing it into claim text, or emit it as a chip run.

### S13-vii-canonical-context-C09  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/canonical_tables.py:806-824` (canonical_tables, projection-gap loop)
- Defect: The loop iterates over every InterfaceGap, including those that earlier rows in the same call created from null metadata cells (T4.12 gap rows with no periods, T4.11 rows with no periods, T4.13 rows with no gap ids). It turns them into new T4.12 WARN rows, which is the self-reference its comment says it avoids.
- Failure scenario: Every narrative or ledger gap with no periods writes T4.12 field_2=None. That adds the extra row "T4.12/<interface-row id>/field_2: Source does not supply this field", padding the gap register with self-referential WARN rows on every run.
- Evidence: `cr/c_t412.py` prints `gaps after upstream row: [('T4.12', 'field_2', ...)]` and then `T4.12 rows: 2`, the second row being the self-referential one.
- Fix direction: Snapshot `tables.gaps` before `_decisions`/`_dashboard` write register-metadata rows, or skip gaps whose table_id is T4.11/T4.12/T4.13.

### S13-vii-canonical-context-C10  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/business_context.py:721-728` (_shape_issues) and `:1765-1775` (register rule)
- Defect: `cp1a.credit_translation_has_evidenced_row` passes on a row with confidence "Insufficient Information" and no citations. `_shape_issues` never checks confidence at all, even though its own message says it does.
- Failure scenario: A CP-1A submission whose only credit translation is Insufficient Information, with no citations, satisfies the "evidenced row" rule and composes.
- Evidence: `cr/c_evidenced.py` prints `evidenced-row issue raised: False`.
- Fix direction: Require `confidence != "Insufficient Information"` and non-empty citations on at least one row (if the rule is meant to require evidence).

### S13-vii-canonical-context-C11  [low] [PLAUSIBLE]  efficiency
- Location: `src/deploy_vii/canonical_gaps.py:426-451`; `src/deploy_vii/canonical_kpis.py:399-420`
- Defect: `kernel_registers` (which re-validates the whole review) runs at least 4 times per gap build: directly, in `canonical_kpis` (directly and through `historical_report`), and in `reconcile_periods` (through `historical_report`). `normalize_facilities` and `_evidence` are also computed twice in `canonical_kpis` (lines 266-267 and 419-420).
- Failure scenario: Validation and frame building are repeated for every CP-1 gap or validation pass, and `validate_*` recomputes all of it again.
- Evidence: Static call trace only; I did not measure the cost.
- Fix direction: Compute the registers and the historical report once and pass them down.

### Out of scope (one line each, optional)
- `src/deploy_vii/cp4_legal.py:528,548`: uses the substring `quoted` as a numeric-token check for covenant thresholds (impact of C05).
- `src/deploy_vii/financial_model.py:247`: the Model KPI rows use the same quarter `display_basis_id` for LTM ratios (same pattern as C01).

### Checked and sound (short bullets: what you attacked that held)
- canonical_audit `optional_terms` exemptions (floor, fixed rate on FLOATING, spread on FIXED) keep conflicts as BLOCK.
- The child-difference and cash-scope blockers are correctly excluded from the absent-input downgrade (the unit tests pin this).
- `_preferred` never derives over a conflicting or not_applicable reported value.
- quality.py band rounding: `round(Fraction)` is half-even, but no boundary of 40, 60 or 80 changes band under it.
- inputs/portfolio.py `parse_number` keeps exact Decimal, with length and format guards; count/rank use exact integral checks.
- The adversarial-origin "period next to a figure not checked" item (A05) was not carried, because of the independence rule.
