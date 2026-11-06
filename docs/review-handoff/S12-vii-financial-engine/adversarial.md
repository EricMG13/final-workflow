SECTION: S12-vii-financial-engine   PASS: adversarial
COVERAGE: read fully: model/{__init__,_cells,dates,frame,registers,periods,history,metrics,debt,statements}.py, financial_reconciliation.py, period_reconciliation.py, financial_periods.py, financial_model.py, financial_adapter.py, financial_validation.py, financial_contracts.py, statement_validation.py, statement_output.py, statement_history.py, statement_extract.py, cash_bridge.py, balance_movement.py, expense_composition.py, facility_fx.py, distressed_figures.py, calculation_trace.py, audit_basis.py / skimmed: none / not read: none
Repro scripts: R/S12-vii-financial-engine/repro/ (R = review root). Run each as
`cd /workspace/final-workflow && PYTHONPATH=src:. .venv/bin/python <script>`.

### S12-vii-financial-engine-A01  [critical] [CONFIRMED]  period arithmetic / balance summed as flow
- Location: `src/deploy_vii/statement_history.py:226-247` (statement_history: every non-BS item goes through `history._Series("flow", ...)` / `history._flow`)
- Defect: CFS `opening_cash` and `closing_cash` (listed CFS items in `statement_validation.OPTIONAL_ITEMS`) are balances, but statement_history builds derived columns for every T4.5 item as flow arithmetic. Only T4.6 (BS) items get `_closing`.
- Failure scenario: a 10-Q CFS gives YTD-only figures, so Q2 is derived as H1 - Q1 (the normal case). Q1 closing cash = 500 and H1 closing cash = 520 give a derived Q2 24 `closing_cash` of 20, which should be 520. Opening cash comes out as 0 where it should be 500. Values are status "Calculated" with no limitation. The same wrong arithmetic gives an LTM closing cash of FY_close + YTD_close - PYTD_close. `canonical_tables.py:765`, `statement_view.py` and `interface_view.py` take these values into the T4.5 deliverable tables.
- Evidence: `repro/cfs_closing_cash_history.py` prints `('Q2 24','QUARTER') closing_cash 20 Calculated` and `opening_cash 0 Calculated`. Expected values worked by hand: 520 and 500.
- Fix direction: in statement_history, treat CFS `opening_cash` and `closing_cash` (and any balance-type CFS item) as balances. Read closing cash at the column end date and opening cash at the day before it starts, as `_closing` does, and never use `_flow`.

### S12-vii-financial-engine-A02  [high] [CONFIRMED]  sign convention / explicit signed inflow flipped
- Location: `src/deploy_vii/statement_output.py:113-118` (`_cell`), `src/deploy_vii/statement_validation.py:404-411` (`account_outflow`), `src/deploy_vii/model/history.py:220-231` (`_row`), `src/deploy_vii/financial_reconciliation.py:128` (`_term`)
- Defect: any amount on an account in `OUTFLOW_METRICS` (cash_taxes_paid, cash_interest_paid, capex, dividends, the leases and interest in financing, and others) becomes minus its absolute value. This happens even when the StatementLine is explicitly `sign_convention="signed"` and the source prints a net inflow.
- Failure scenario: a CFS prints "Income taxes refunded (paid), net | 15" (a net refund, common in loss or CARES-Act years). The model records it as signed +15. The statement report shows -15 ("negative absolute source amount"), the reconciliation term is -15, and the kernel reads -15 into FFO and the LTM. The figure is 2x15 too low with no flag. Validation cannot catch it: `statement_issues` normalizes both sides the same way, so no disagreement is raised.
- Evidence: `repro/signed_refund_flip.py` prints `statement_output: source 15 normalized -15 negative absolute source amount` and `reconciliation term: original 15 amount -15`.
- Fix direction: negate only rows declared `outflow_magnitude`. For a `signed` row of an outflow account, keep the source sign. Or reject a positive signed amount on an outflow account as needing an explicit conflict or limitation, and never flip it silently.

### S12-vii-financial-engine-A03  [medium] [CONFIRMED]  reconciliation tolerance widened by Decimal exponent
- Location: `src/deploy_vii/financial_reconciliation.py:166-168` (`_check`), `src/deploy_vii/period_reconciliation.py:122-126` (`_compare`), `src/deploy_vii/model/_cells.py:41-45` (`beyond_rounding`)
- Defect: tolerance is half a unit in the last place of the parsed Decimal's exponent. The live path (`live.schema.json_object` -> `exact_json` -> `model_validate_json`) passes amounts as JSON numbers, and Pydantic drops their trailing zeros (`1234.0` -> `Decimal('1234')`, `12.30` -> `12.3`). Printed precision is lost, so the tolerance becomes 10x (or more) too loose. A stored string such as `"1.2E+3"` gets a tolerance of 50.
- Failure scenario: a total printed `1,234.0` (millions, one decimal) and components 1,000.0 + 233.6 = 1,233.6 differ by 0.4 against a hand tolerance of 0.05. The check reports PASS "Agrees within half the last reported decimal place". The kernel's DIFFERS note (`beyond_rounding`) is missed the same way.
- Evidence: `repro/tolerance_trailing_zero.py` prints `parsed total: Decimal('1234') exponent 0` and `tolerance 0.5 difference -0.4 status PASS`.
- Fix direction: carry the printed precision explicitly (raw printed text or a declared decimals field) and use it for the tolerance. Failing that, take the tolerance from the finest precision among the reported and component amounts and refuse positive exponents.

### S12-vii-financial-engine-A04  [medium] [CONFIRMED]  statement extraction drops minus-signed rows silently
- Location: `src/deploy_vii/statement_extract.py:93-97` (`_NUMBER`/`_NUMERIC_CELL`), `:426-434` (`_is_omitted_candidate`)
- Defect: a leading-minus negative (`-1,234`, or U+2212 `−123`) is not a numeric cell. A row whose values are all minus-signed therefore fails as a data line, and because its last token is not a "numeric cell" it is also not an `omitted` candidate. The row vanishes from both lists. That breaks the module's claim that a line it cannot parse is recorded in `omitted`.
- Failure scenario: "Net loss   -1,234   -567" and "Other expense   −123   −45" on a statement page give no data line and no omitted line. `statement_compose` builds rows only from the extraction, so the issuer's net loss row is silently absent from the model's input. The result shows up later as a missing item or an incomplete identity, and the cause is hidden.
- Evidence: `repro/extract_attacks.py`: only Revenue, Umsatzerlöse and Operating income are returned. `OMITTED` prints nothing.
- Fix direction: accept a leading ASCII or Unicode minus as a negative in `_NUMBER`, or at least treat a minus-number token as an omitted candidate.

### S12-vii-financial-engine-A05  [medium] [CONFIRMED]  European thousands separator parsed as decimal
- Location: `src/deploy_vii/statement_extract.py:93` (`_NUMBER` alternative `\d+(?:\.\d+)?`)
- Defect: `1.234` (dot used as the thousands separator, common in EUR issuer filings) is parsed as `Decimal('1.234')` with no flag. `statement_compose.py:486` uses `ExtractedLine.values` directly as the amount.
- Failure scenario: "Umsatzerlöse   1.234   987" extracts as 1.234 and 987. Revenue becomes 1000x too small in one period, and no unit warning or `label_ends_numeric`-style flag is raised. Only a later identity BLOCK might catch it.
- Evidence: `repro/extract_attacks.py` prints `DATA 6 'Umsatzerlöse' ('1.234', '987') (Decimal('1.234'), Decimal('987')) ()`. Reachability depends on a European-format source in scope (not shown for current cases).
- Fix direction: flag a cell with exactly three digits after a single dot (and integer-looking peer cells in the same row or table) as ambiguous separator usage instead of returning a value without a flag.

### S12-vii-financial-engine-A06  [low] [PLAUSIBLE]  DR.2 rows grouped by display name
- Location: `src/deploy_vii/distressed_figures.py:88-100` (`_cp4c_figures`, DR.2 branch)
- Defect: DR.2 table rows are grouped by the class display name (`point.category`), not by class id. Two creditor classes with the same name merge into one row holding 2xN cells for N scenario columns.
- Failure scenario: two CP-4C classes both named "Senior notes" make `Block.state_matches_content` raise "Row cells do not match the block's columns", which stops the front page delivery. If the validator were relaxed, cells would be mislabelled.
- Evidence: code reading. `restructuring_series._recovery` sets `category` to the T4E.2 name text, `by_category` dedups with `dict.fromkeys`, and `report_view.py:459-462` enforces the cell count. No repro was built because constructing a settled CP-4C ModuleView is out of section.
- Fix direction: group by the class identity carried in `companion_fact_ids` (T4E.2.<class>.name) and use the name only as the label.

### Out of scope (one line each, optional)
- `deploy_vii/live/schema.py` `exact_json` + `model_validate_json`: losing JSON-number trailing zeros also affects any other precision-sensitive consumer, not only A03.

### Checked and sound (short bullets: what you attacked that held)
- LTM = FY + YTD - PYTD with hand values: calendar leap year (1000+530-480=1050, 365 days), 52-week retailer (5400, 364 days), 53-week FY (371 days); Q2 = H1 - Q1 and Q4 = FY - 9M with correct day counts (`repro/ltm_kernel.py`).
- Mislabelled fiscal year text (`Fiscal 2025 (ended 2026-01-31)` -> 2026) mis-selects the prior FY, but `_meets` and `LTM_DAYS` mark the LTM UNSPANNED (fails closed).
- Metric ratios: zero/negative EBITDA, interest and growth bases give ZERO_OR_NEGATIVE_DENOMINATOR, never inf. A missing input propagates its reason, never zero. Outflow signs in coverage/capex formulas are correct.
- FX: rate direction is bound by currency labels (source == facility, target == book, book != facility), the rate date must equal the period end, same-date rates must agree, rates must be positive, a missing rate or a conflict gives a null amount with a reason, and source registers are untouched. Facility currency is fixed across periods (`_series_issues`).
- Debt: a foreign facility without FX makes total debt COMPONENT_MISSING (never silently excluded in the adapter path). A facility issued later reads as a sourced 0. Leases are excluded per contract.
- Cash bridge: adjustment coefficients invert correctly (NCF = delta - adj), the restricted-cash scope needs cited BS rows at both dates, and a missing scope balance is BLOCK, not 0.
- Missing vs zero: an absent component makes reconciliation BLOCK. Sparse items only treat absence as nothing under the documented rules. `_zero_if_absent` is noted on `cfo_adjusted`.
- Statement identities: cycles, overlaps, mixed statements, mixed dimensions and expansion caps are rejected. Opposite-signed leaves are not cancelled.
- dates.py: two-year spellings, non-consecutive years, invalid days (`2025-02-30`) and non-ISO text all return None or the documented year.
