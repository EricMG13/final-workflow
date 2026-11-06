SECTION: S08-cp3   PASS: adversarial
COVERAGE: read fully: src/deploy_vii/inputs/rv_quotes.py, src/deploy_vii/cp3_relative_value.py, src/deploy_workflow/owners/cp3.py / skimmed: src/deploy_workflow/owners/cp3d.py (schema, parsing, compose, validator, limitations, Stage 2 validate/submit read; table composer 1150-1950 skimmed), src/deploy_workflow/owners/cp3c.py (validator, calculation core, operand binding read; tables/claims/Stage 2 1100-3043 skimmed) / not read: none

Repro scripts (all in this folder): repro_cp3d.py, repro_cp3d_units.py, repro_cp3.py, repro_cp3c.py, repro_rv.py. Run as
`cd /workspace/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <script>` (repro_cp3d_units.py takes this folder as argv[1]).
Baseline: tests/test_method_cp3.py, test_method_cp3d.py, test_cp3_context_evidence.py pass (982 passed).
In every repro the baseline oracle submission passes first, then one field or page sentence is changed.

### S08-cp3-A01  [high] [CONFIRMED]  quote handling / conditional quote treated as executable
- Location: `src/deploy_workflow/owners/cp3d.py:816` (`_observation_level`), `:796` (`_labelled`), `:2008` (`own_limitations`)
- Defect: CP-3D accepts a `bid`/`offer` observation from a quote that calls itself indicative or "subject to confirmation". Nothing checks the quote for talk or conditional wording. CP-3 does have that check (`TALK_MARKERS`); CP-3D does not.
- Failure scenario: the page says "Indicative dealer quotation on January 9, 2026, subject to confirmation and not firm: bid 98.50 and offer 99.25". It is submitted as bid and offer. Validation passes, and T3E shows an observed mid of 0.98875, DM 28.3 bp and PD 3.68%. The only limitation is the single-dealer line, so a conditional level is presented as an executable quote.
- Evidence: `repro_cp3d.py` case A1 gives `issues=[]` and the same DM/PD as a firm quote. Limitations: only 'Indicative dealer talk is shown but is not used in any calculation', which is about the separate talk row.
- Fix direction: refuse a bid/offer whose quote (or its sentence on the page) carries talk or conditional markers (indicative, subject to, talk, guidance, not firm), as CP-3 `_market_row` does for `observed` rows.

### S08-cp3-A02  [high] [CONFIRMED]  wrong instrument passes validation (CP-3D)
- Location: `src/deploy_workflow/owners/cp3d.py:1112` (`submission_issues`), `:937` (`_check_observations`), `:979` (`_check_maturity`)
- Defect: only `instrument.quote` must contain the instrument name. Observation quotes, the maturity quote and the margin quote are never tied to that instrument.
- Failure scenario: a dealer sheet also prints "…for the Southgate Notes due 2027: bid 88.50 and offer 89.25". Those levels are bound to the "Northbridge Term Loan". The module then publishes DM 279.7 bp and PD 30.98%, where the correct figures are 28.3 bp and 3.68%. CP-3C reads these DM/PD values through `cp3d_reader`.
- Evidence: `repro_cp3d.py` case A5 gives `issues=[]`, `mid 0.88875 dm_mid 279.7 pd_mid 0.3098`.
- Fix direction: require the instrument name (or a listed alias) in each observation, maturity and margin quote, or in the sentence holding the quote on its page. Refuse otherwise.

### S08-cp3-A03  [high] [CONFIRMED]  price vs yield vs spread: units of a quoted level are not checked
- Location: `src/deploy_workflow/owners/cp3d.py:796` (`_labelled`), `:845` (bound `0 < value <= 200`), `:650` (`_point`)
- Defect: `_labelled` only needs "bid <number>" not followed by a digit. A level written "bid 6.25%" or "bid 175 bps" is therefore taken as a price in points of par. With one side only, the bid-exceeds-offer check never runs, so nothing catches it.
- Failure scenario: the quote is "bid 6.25% yield to maturity". It is stored as price 0.0625 of par, giving DM at bid 2356.7 bp and PD at bid 95.61%. With "bid 175 bps discount margin" the stored price is 1.75 and DM at bid is -1885.3 bp.
- Evidence: `repro_cp3d.py` cases A4 and A4b both give `issues=[]`, with `dm_bid 2356.7 pd_bid 0.9561` and `dm_bid -1885.3`.
- Fix direction: refuse a level followed by `%`, `bp`, `bps`, `basis points` or "yield"/"spread" wording. Better, require the quote or its page to state that levels are a percentage of par.

### S08-cp3-A04  [high] [CONFIRMED]  bp vs percent: margin and reference-rate units not checked
- Location: `src/deploy_workflow/owners/cp3d.py:958` (`_check_quoted_numeral`), `:1025-1034` (reference level), `:710` (`inputs_from_submission`)
- Defect: `bps_text` is read as basis points and `percent_text` as percent. Neither check looks at the unit the quote prints, and `_NUMERAL` allows decimals and three integer digits.
- Failure scenario: the financial page states "margin of 3.25% per annum" and "The SOFR fixing was 430 bps". With `bps_text "3.25"` and `percent_text "430"`, both pass. The output shows a margin of 3.25 bp instead of 325 bp, DM mid 31.5 bp, and an all-in yield of 4.3032 as a fraction, i.e. 430%.
- Evidence: `repro_cp3d_units.py` case A6 gives `issues=[]`, `margin_bp 3.25 yield_mid 4.3032 dm_mid 31.5`.
- Fix direction: require the token after the figure in the quote to match the field's unit (bps/basis points for margin, % for the reference level). Refuse a mismatch or a missing unit.

### S08-cp3-A05  [high] [CONFIRMED]  stale or future-dated sheet quotations accepted (period integrity)
- Location: `src/deploy_workflow/owners/cp3d.py:852` (`_observation_date`), `:402` (`_stale_lines`, context rows only), `:671` (`compose`)
- Defect: a pack (sheet) quotation date is never compared with `run_as_of`. Only context-file rows get the 30-day stale line. Years to maturity are counted from the quotation date.
- Failure scenario: (a) The quotation is dated January 9, 2019 in a run as of 2026-01-10. It is accepted with no stale limitation, years = 10.98 and DM mid 10.2 bp, where today's tenor would give about 28 bp. (b) The quotation is dated January 9, 2027, after the run as-of. It is accepted with years = 2.98 and DM 37.8 bp, which is look-ahead evidence.
- Evidence: `repro_cp3d.py` cases A2 and A3 both give `issues=[]`, and neither adds a stale line to the limitations.
- Fix direction: refuse a quotation date after `run_as_of`, and apply the same STALE_DAYS limitation (and its text) to sheet observations as to context rows.

### S08-cp3-A06  [high] [CONFIRMED]  CP-3 market-evidence `as_of` is model text, unchecked, shown as the quote date
- Location: `src/deploy_vii/cp3_relative_value.py:1060` (`_market_row`, no `as_of` check), `:1557` (`_market`, `out.said(row.as_of)`)
- Defect: `MarketEvidence.as_of` is never parsed and never compared with the quoted span or the run as-of. Pack quotes have no staleness cap at all; only context rows do (`STALE_DAYS`).
- Failure scenario: the quote reads "Dealer quotation on January 9, 2026…". The model writes `as_of` "January 9, 2031", or "the close". T3.3 "As of" shows that text, the row stays Observed and the preference is uncapped.
- Evidence: `repro_cp3.py` cases A and A2 give `issues=[]`, and T3.3 m01 shows 'January 9, 2031' and 'the close' respectively.
- Fix direction: require `as_of` to be a date that occurs in the quoted span (as CP-3D `_observation_date` does) and is not after `run.as_of`. Add the stale cap and limitation for pack quotes older than STALE_DAYS.

### S08-cp3-A07  [high] [CONFIRMED]  CP-3 accepts another facility's context quote as an instrument's market basis
- Location: `src/deploy_vii/cp3_relative_value.py:1099` (`_basis_issues`), `:1138` (`_instrument_issues`)
- Defect: `basis.context_rows` is checked only for existence. The row's `facility_id` (known to Python) is never compared with the instrument's `facility_id`.
- Failure scenario: CP-1 lists `term-loan` and `notes-2031`, and the context quotes c01/c02 are for `notes-2031`. The `term-loan` instrument writes a market observation and cites c01/c02. T3.1 shows "Market evidence context c01 (observed)" as the Term Loan's basis, and its claim carries the notes' citations.
- Evidence: `repro_cp3.py` case C gives `issues=[]`, with T3.3 c01 'notes-2031: bid 98.50, …' and T3.1 i01 Northbridge Term Loan basis '…Market evidence context c01 (observed); …context c02…'.
- Fix direction: in `_instrument_issues`, refuse a context row whose `facility_id` differs from the instrument's.

### S08-cp3-A08  [medium] [CONFIRMED]  CP-3 talk marker check bypassed by quoting a sub-span
- Location: `src/deploy_vii/cp3_relative_value.py:1091-1095` (`_market_row` talk check on `quote.quote` only)
- Defect: the rule "an observed row never quotes indicative talk" is checked only on the quoted text, not on the sentence or span it comes from.
- Failure scenario: page:2 reads "Dealers describe the indicative fair value … as around 99.75. This is talk and not a quotation or a trade." The model quotes "the Northbridge Term Loan as around 99.75" as `observed`. T3.3 then shows Observed. The "indicative talk only" confidence cap and its limitation disappear, and the talk-as-level wording guard is skipped.
- Evidence: `repro_cp3.py` case B gives `issues=[]`, with T3.3 m01 'Observed', 'the Northbridge Term Loan as around 99.75'.
- Fix direction: run `_TALK` over the enclosing sentence (or the whole span) of the quote, not only the quoted substring.

### S08-cp3-A09  [medium] [CONFIRMED]  CP-3C: positive cash interest is silently negated; pro forma cover nets new interest against it
- Location: `src/deploy_workflow/owners/cp3c.py:1087` (`compose_operands`, `interest.copy_negate()`), `:836-848` (`compose_refinancing`)
- Defect: the code assumes CP-1 `cash_interest` is a negative outflow and negates it with no sign check.
- Failure scenario: a positive figure (net interest received, or a CP-1 sign anomaly) of +40 becomes paid = -40. Interest cover is then "not meaningful", but pro forma interest = -40 + 50 = 10, giving a pro forma cover of 20.0000x. A reader sees a strong pro forma cover where the base cover is n.m.
- Evidence: `repro_cp3c.py` gives `cash_interest=40: … cover=Gap(…not meaningful…) pro_forma_cover=20.0000`. With -40 it gives cover 5.0000 and pro forma 2.2222.
- Fix direction: raise (invariant) or gap the interest operands when the CP-1 cash interest is positive, rather than netting it into the pro forma total.

### S08-cp3-A10  [low] [CONFIRMED]  rv_quotes validator crashes on a large exponent
- Location: `src/deploy_vii/inputs/rv_quotes.py:90` (`NUMBER` allows any exponent), `:344` (`Decimal(bid) > Decimal(ask)`)
- Defect: `NUMBER` accepts `1e9999999999999999999999`, but `Decimal()` raises `InvalidOperation` on it. The error escapes `validate_rv_bytes` instead of becoming an `Issue`.
- Failure scenario: a bid cell holding text `1e9999999999999999999999` with ask `1` makes `deploy-vii validate-input rv` die with a traceback.
- Evidence: `repro_rv.py` case R3 gives `CRASH InvalidOperation`.
- Fix direction: drop exponents from `NUMBER` (the FIX text already says "plain number"), or catch `InvalidOperation` and report the cell.

### S08-cp3-A11  [low] [CONFIRMED]  rv_quotes: zero or negative price passes; duplicate key check is case- and space-sensitive
- Location: `src/deploy_vii/inputs/rv_quotes.py:322` (`column_problem`), `:168-176` (duplicate key)
- Defect: a price of `0` (often a blank exported as zero) or `-5` counts as a valid level. A duplicate quote that differs only in letter case passes ("Dealer A"/"dealer a", "TLB-2030"/"tlb-2030").
- Failure scenario: a workbook with price 0 and a case-variant duplicate reports `OK: 2 rows`.
- Evidence: `repro_rv.py` cases R1 and R2 both report `ok=True`.
- Fix direction: refuse a price at or below zero, and fold case and whitespace (`folded`) on the provider and facility_id key parts.

### S08-cp3-A12  [low] [CONFIRMED]  rv_quotes fix text points to a template that does not exist
- Location: `src/deploy_vii/inputs/rv_quotes.py:33` (`TEMPLATE`), used in FIX "empty"/"header"/"sheet"
- Defect: `docs/templates/rv-quotes.template.xlsx` is not in the repo (`git ls-files docs/templates` lists only README.md, context-form.html and portfolio.template.xlsx). The user-facing fix messages tell users to copy from it.
- Evidence: `repro_rv.py` prints `template exists: False`.
- Fix direction: restore the template, or change the FIX text to spell out the header row.

### Out of scope (one line each, optional)
- None confirmed.

### Checked and sound
- CP-3D: refuses bid > offer, different bid and offer dates, a missing bid/offer date, a maturity on or before the quotation date, a level outside (0, 200], more than 4 decimals, a leading zero, and a token that is signed, accounting-parenthesised or cut at the quote edge (`_tokens`, `_whole_on_page`). Missing operands stay None and never become 0 in `compose`; dm <= 0 gives not_applicable, not a PD.
- CP-3D context rows: a model-written `context` source is refused, a bid/offer must come from the same context quote row, mixed context facilities are refused, and context rows get the stale line.
- CP-3: no market evidence forces Insufficient Information; talk-only evidence, a non-accepted CP-2 or a blocked bound input caps confidence below High. A span quoted twice under two kinds is refused, and a model `context` row is refused. Context JSON gets duplicate-key refusal and figure citation as one unique span (an escaped value is not cited).
- CP-3C: missing operands propagate as Gap in formula order; zero or negative denominators give n.m.; maturity before D0 is a Gap, not negative months; an FX or unstated currency facility is gapped, not summed; currency consistency and a duplicate facility_id raise; step-up bps is bounded 0-1000.
- rv_quotes: Excel date serials, formulas, non-canonical locators, header drift and an issuer named as provider are all refused with cell-level issues.
