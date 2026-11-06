SECTION: S13-vii-canonical-context   PASS: adversarial
COVERAGE: read fully: canonical_kpis.py, canonical_gaps.py, canonical_audit.py, canonical_tables.py, quotes.py, inputs/portfolio.py, inputs/__init__.py, source_context.py, narrative.py, narrative_projection.py, prose.py, quality.py, __init__.py / skimmed: business_context.py (contract, validation rules, governance score, composer, score registers; about 40%) / not read: rest of business_context.py (handoff/snapshot registers, submit path, context_block)
Repro scripts: R/S13-vii-canonical-context/work/*.py (run with `cd /workspace/final-workflow && PYTHONPATH=src:. .venv/bin/python <script>`)

### S13-vii-canonical-context-A01  [high] [CONFIRMED]  gap severity / hidden disagreement
- Location: `src/deploy_vii/canonical_audit.py:491-527` (absent_input_limitation); used at canonical_audit.py:626-638 and canonical_gaps.py:253-271
- Defect: on a public pack, any BLOCK check with `difference is None` is downgraded to WARN and labelled "Absent input", even when every term has an amount and the BLOCK comes from a structural blocker that suppressed the difference.
- Failure scenario: FY period with `expense_presentation="unknown"` (the FinancialPeriod default). Revenue 100, COGS -40, opex incl. D&A -30, D&A -10, so the bridge gives 40; reported EBITDA is 55, a real gap of 15. `_check` sets calculated=None because of the blocker "Expense presentation is unknown", so difference=None. `absent_input_limitation` returns "Absent input ... : Expense presentation is unknown" with no absent term, and the audit and gap ledger record WARN instead of BLOCK. QA goes to Restricted instead of Blocked, and T4.12 states an absent input that does not exist. The same applies to "Add-back bridge is incomplete or undisclosed", the NCF-structure blocker, "Four dated discrete quarters do not span the reported FY", node.limitation period blockers and others.
- Evidence: `work/absent_input.py` -> `status BLOCK difference None ... all inputs present: True; limitation -> 'Absent input, stated as a limitation on a public filed pack (rulings item 82): Expense presentation is unknown'; severity -> WARN`.
- Fix direction: downgrade only when at least one term actually has `amount is None` (and the explanation is the missing-input text), and keep structural blockers as BLOCK.

### S13-vii-canonical-context-A02  [high] [CONFIRMED]  wrong analytical conclusion (governance risk level)
- Location: `src/deploy_vii/business_context.py:844-873` (governance_sponsor_score); rendered at business_context.py:1500-1523 (T2D.8 composite)
- Defect: the High-quality creditor-adverse "documented action" override applies only when fewer than 4 dimensions are scored. With 4 or more scored dimensions, the action is ignored whenever it has no dimension label or shares a dimension with a Supportive row. Adding favourable evidence therefore lowers the risk level from High to Low.
- Failure scenario: a behaviour flag "dividend recap", Extraction-Oriented, evidence High, dimension null (validation allows null). With 3 supportive dimensions the result is level High. Add a fourth supportive dimension and the result is composite 1, "Sponsor / Governance Risk Level: Low", while `high_risk_action=True`. If the recap is labelled but a Supportive row shares its dimension, the result is Medium.
- Evidence: `work/governance_score.py` -> `3 supportive dims + recap (no dimension): composite=Not Scorable level=High high_action=True` / `4 supportive dims + recap (no dimension): composite=1 level=Low high_action=True` / `3 supportive + recap + supportive extraction row: composite=3 level=Medium high_action=True`.
- Fix direction: apply the High-quality adverse-action override as a floor (level High) whatever the number of scored dimensions, or require behaviour flags to carry a dimension so the rubric sees them.

### S13-vii-canonical-context-A03  [medium] [CONFIRMED]  citation verification accepts numeric fragments
- Location: `src/deploy_vii/quotes.py:105-118` (quoted)
- Defect: the shared matcher accepts any contiguous normalised substring with no token boundary, so a fragment cut out of a larger number, or a single letter, counts as a verified quote.
- Failure scenario: covenant text "shall not exceed 12.50:1.00". `quoted("2.50:1.00", quote)` is True. cp4_legal `_threshold_issues` then parses threshold_value 2.50 (unit multiple) from threshold_text and accepts it, so a 12.50x covenant can be recorded as 2.50x. Also `quoted("1.2 billion", "total debt of $11.2 billion")` is True, and `quoted("a", any_page)` is True (readiness.citation_issues and the cp2e/cp3d on_page checks have no minimum quote length). cp3d works around this with `_whole_on_page`; other callers do not.
- Evidence: `work/quotes_attacks.py` -> `'2.50:1.00' quoted in covenant text: True`, `'1.2 billion' accepted: True`, `one-letter quote accepted: True`, `multiple (Decimal('2.50'), None)`.
- Fix direction: add a boundary-anchored mode, so the match cannot start or end inside an alphanumeric run, and use it for value/threshold quotes, with a minimum visible length for citation quotes.

### S13-vii-canonical-context-A04  [medium] [CONFIRMED]  bare-figure guard bypass in run text
- Location: `src/deploy_vii/prose.py:139-147` ("coverage" label), `prose.py:94` (bare year label), `prose.py:215-229` (bare_figures)
- Defect: the "pack-coverage" label matches any "N of M" phrase, any 4-digit 19xx/20xx number passes as a year, and numbers written as words are never checked. Model prose can therefore state unsupported issuer figures that the MC-2 rule ("the model never supplies a number") is meant to refuse.
- Failure scenario: CP-1 narrative ProsePart or CP-1A claim text "Covenant headroom was breached in 3 of 4 quarters", "EBITDA margin fell by 2024 basis points", or "Leverage rose to seven times EBITDA and revenue halved" passes `prose.check`/`issues` with no reference, and goes straight into the deliverable claims.
- Evidence: `work/prose_attacks.py` -> all three return `() ()`; controls "18 months" and "6x" are flagged.
- Fix direction: anchor the coverage label to pack nouns (pages/spans/sources) instead of any "N of M", refuse a year token followed by a quantity word, and add a check for number words or multipliers ("times", "halved", "doubled").

### S13-vii-canonical-context-A05  [medium] [CONFIRMED]  period mislabelling of referenced figures
- Location: `src/deploy_vii/prose.py:282-323` (_fact_issues / issues); spelled in business_context.py:377-382 and narrative_projection chips
- Defect: a figure reference is checked for status, citation and unit, but the period label written beside it is never compared with the fact's `period`. The rendered figure drops the period.
- Failure scenario: fact rev-fy2023 (USD 812m, period FY2023). Run text "FY2025 revenue reached {rev-fy2023}, up from FY2024." passes with no issues and renders "FY2025 revenue reached 812 US$ m", a real number in the wrong period plus an unsupported trend.
- Evidence: `work/prose_period.py` -> `issues: ()`, `rendered figure: 812 US$ m | fact period: FY2023: 2023-01-01 to 2023-12-31`.
- Fix direction: when a period label sits next to a figure reference in the same clause, require it to match the fact's period, or have Python render the fact's period with the figure.

### S13-vii-canonical-context-A06  [medium] [CONFIRMED]  canonical adjusted EBITDA lost on period-absent add-backs
- Location: `src/deploy_vii/canonical_kpis.py:201-208` (_canonical_frame)
- Defect: the derived adjusted EBITDA sums every `addback:` cell, including add-backs with no row in this column (`account_frame` gives every add-back a `NOT_SOURCED` cell on every column). The Model statement derivation (`statements._income`) excludes these cells.
- Failure scenario: FY2023 with no stated adjusted EBITDA: revenue 100, COGS -40, opex -30, D&A -10, add-back restructuring 5, plus an add-back acquisition_costs disclosed only in FY2024. Statement adjusted EBITDA is 45 (hand-derived 40+5). Canonical adjusted EBITDA is None/COMPONENT_MISSING, with the note "Reported value unavailable; derived from components". Every adjusted-EBITDA KPI for the column, and every trailing-4Q basis containing it, becomes unavailable: total and net adjusted leverage, senior secured leverage, adjusted interest coverage, capex-adjusted coverage, FCF/adj. EBITDA, adj. margin and growth. The CP-1 canonical register then disagrees with the Model for the same period.
- Evidence: `work/addback_absent.py` -> `statement adjusted_ebitda: 45` / `canonical ebitda: 40  adjusted_ebitda: None COMPONENT_MISSING Reported value unavailable; derived from components`.
- Self-check: the reconciliation module also treats period-absent add-backs as "Not supplied", so this may be a deliberate conservative choice. Even so, the KPI layer and the Model disagree, and the note says the value was derived when it was not.
- Fix direction: apply the statement rule (skip `reason == "NOT_SOURCED"` add-backs) or record an explicit gap that names the absent add-back, and do not write a "derived" note on a missing value.

### S13-vii-canonical-context-A07  [low] [PLAUSIBLE]  financial-narrative gate is vacuous
- Location: `src/deploy_vii/narrative.py:233-235`, `narrative.py:244-249`, `narrative.py:286-287`
- Defect: scope "financial_synthesis" is granted when any CanonicalKpi has an amount. That includes the 22 `operation="value"` scalar rows (revenue, cash_closing ...), so leverage/coverage/liquidity findings are allowed, and the "No available KPI" gap is suppressed, even when every ratio KPI is unavailable.
- Failure scenario: a pack with only revenue sourced, and no debt or EBITDA, still gets scope financial_synthesis. A "leverage" finding validates, and no data-quality-only gap is raised.
- Evidence: from code: `_kpi_rows` (canonical_kpis.py:329-339) emits every `_SCALARS` key as a KPI row, and the scope predicate does not filter on `operation`. Not run end to end because it needs a full prepared pack and financial review.
- Fix direction: base the scope (or a per-dimension gate) on `operation in {"ratio","growth"}` KPIs relevant to the dimension.

### S13-vii-canonical-context-A08  [low] [CONFIRMED]  portfolio percent-of-NAV value 100x wrong
- Location: `src/deploy_vii/inputs/portfolio.py:96-98, 784-800` (PCT_COLUMNS / percent_findings)
- Defect: percent-formatted cells are refused only in pct columns and on % NAV Compliance rows. An Exposure_Summary row with unit "% NAV" and a percent-formatted value (stored as a fraction) is accepted as a fraction.
- Failure scenario: the cash row shows 2.50% in Excel (stored 0.025) and is accepted as `Decimal('0.025')` % NAV, 100x too small. There is no in-repo production consumer of `portfolio_facts` today, hence low.
- Evidence: `work/portfolio_attacks.py` -> `A exposure %NAV percent-formatted: ok=True []  cash value read as [Decimal('0.025')]`.
- Fix direction: treat Exposure_Summary `value` as a percent column when its row's unit is "% NAV".

### S13-vii-canonical-context-A09  [low] [CONFIRMED]  portfolio workbook accepts hidden stale rows/sheets and negative shares
- Location: `src/deploy_vii/inputs/portfolio.py:705-731` (load_table), `portfolio.py:845-860` (rating_rules)
- Defect: hidden rows and hidden sheets are read as live data, and negative pct_nav is accepted. A -50 bucket can offset 150 so that the rating sum check passes.
- Failure scenario: a hidden row in Top_Holdings ("Stale Old Holding", 9.9% NAV) becomes holding #3. A Rating_Distribution of B 150 and Unrated -50 passes the 99-101 sum check. Maturity buckets of -40 and 140 are accepted.
- Evidence: `work/portfolio_attacks.py` -> `B hidden row: ok=True ... 'Stale Old Holding'`, `C hidden sheet: ok=True`, `G negative rating bucket: ok=True`, `D negative maturity pct_nav: ok=True`.
- Fix direction: refuse negative pct_nav/issuer shares, and report hidden rows and sheets (state from the workbook XML) as issues.

### Out of scope (one line each, optional)
- `src/deploy_vii/cp4_legal.py:528,548` (`_direction_issues`/`_threshold_issues`) relies on `quoted(threshold_text, quote)` for a numeric threshold, so a 12.50x covenant can be stored as 2.50x (see A03). This needs a whole-token check like cp3d `_whole_on_page`. Severity high in that section.
- `src/deploy_vii/financial_reconciliation.py:267-285` ADJUSTED_EBITDA_BRIDGE treats period-absent add-backs as "Not supplied" (BLOCK), which diverges from `statements._income` (same convention split as A06).

### Checked and sound (short bullets: what you attacked that held)
- KPI ratios: denominators <= 0 refused (`ZERO_OR_NEGATIVE_DENOMINATOR`); outflow signs (cash interest, capex, D&A, dividends) agree with the statement conventions; FFO = adj. CFO - WC change equals the statement waterfall algebraically; missing operands give None, not 0; Conflicted is propagated only for a None value with a conflicting leaf.
- canonical_tables `_value`/`_Tables.row`: a None value with default status "known" becomes "missing" plus an InterfaceGap, so no missing figure is marked present; unit-to-scale mapping is limited to UNITS/THOUSANDS/MILLIONS (the full Unit literal).
- canonical_gaps: the gap ledger deduplicates only identical GapDetails; context `file-gate` stays BLOCK; Conflicted KPI values are BLOCK; a calculation_gate failure retains a BLOCK gap and does not proceed.
- quotes: `reading()` text equals `normalise`/`_joined` exactly, so `_variant` cannot hit StopIteration; `_longest_prefix` monotone; blank quotes refused by callers.
- quality: lineage ceilings block upgrades; inherited findings cannot be replaced; caps 39/59 applied before banker's rounding; no division by zero (coverage min_length 1).
- source_context: publication/as-of/scope-end/event chronology checks, cross-source citation refusal, entity dimension disagreements; XBRL exact-date binding.
- portfolio: formulas (no cached value), Excel errors and booleans, date serials, merged cells (become empty required cells), duplicate keys, total rows, header row exactness and percent-formatted pct columns are all refused correctly.
- Targeted tests: tests/product/test_context.py 163 passed.
