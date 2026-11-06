"""C: effective_accounts/account_outflow rebuilt per _account call: quadratic cost."""
import time
from datetime import date, timedelta
from test_cash_scope import book, cite, line, period
from deploy_vii.statement_validation import ACCOUNT_LINKS, effective_accounts
from deploy_vii.financial_reconciliation import _account

links = [(s, i) for (s, i) in ACCOUNT_LINKS][:30]
periods, lines = [], []
for n in range(40):
    end = date(2016, 1, 1) + timedelta(days=91 * (n + 1))
    pid = f"q{n}"
    periods.append(period(pid, "QUARTER", 1 + n % 4, f"FY{end.year}", end - timedelta(days=90), end))
    for k, (s, item) in enumerate(links):
        for dup in range(3):
            lines.append(line(f"{pid}-{k}-{dup}", s, item, pid, 10 + k, cite(f"{item} {10+k}"), priority=1 + k))
b = book().model_copy(update={"periods": tuple(periods), "statement_lines": tuple(lines), "cash_movement_bridges": ()})
print("statement lines:", len(lines))
t = time.perf_counter(); effective_accounts(b); one = time.perf_counter() - t
print(f"one effective_accounts: {one*1000:.1f} ms")
metrics = sorted({m for m in ACCOUNT_LINKS.values()})[:26]
t = time.perf_counter()
for p in periods:
    for m in metrics:
        _account(b, p.period_id, m)
print(f"{len(periods)*len(metrics)} _account calls: {time.perf_counter()-t:.1f} s")
