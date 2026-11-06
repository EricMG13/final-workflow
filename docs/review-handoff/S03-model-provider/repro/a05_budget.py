import os, tempfile
from decimal import Decimal as D
from pathlib import Path
from deploy_workflow.model.budget import Budget, BudgetError, BudgetExhausted, RunStopped, RetryUsed, OverrunStop
S = os.environ["SCRATCH"]
def fresh(cap="10"):
    d = Path(tempfile.mkdtemp(dir=S)); return d, Budget(D(cap), d)
# 1 cap boundary exact
d,b = fresh("1"); b.reserve("a", D("0.6"), config_id="sol-medium")
try: b.reserve("b", D("0.4000000000000000000000000001"), config_id="sol-medium"); print("BAD cap passed")
except BudgetExhausted: print("OK cap refused just over")
b.reserve("c", D("0.4"), config_id="sol-medium"); print("OK exact cap allowed", b.reserved)
# 2 unknown then retry then second retry
d,b = fresh(); b.reserve("a", D(1), config_id="sol-medium"); b.settle("a", None, retryable=True)
try: b.reserve("x", D(1), config_id="sol-medium"); print("BAD reserve after unknown")
except RunStopped: print("OK stopped after unknown")
b.reserve("r", D(1), retry_of="a", config_id="sol-medium"); b.settle("r", None, retryable=True)
try: b.reserve("r2", D(1), retry_of="r", config_id="sol-medium"); print("BAD second retry")
except (RetryUsed, RunStopped) as e: print("OK second retry refused", type(e).__name__)
print("spent includes both holds:", b.spent == D(2))
# 3 overrun: spend beyond cap
d,b = fresh("1"); b.reserve("a", D("0.5"), config_id="sol-medium")
try: b.settle("a", D("5"))
except OverrunStop: print("overrun recorded; spent", b.spent, "cap", b.cap_usd, "(spent > cap by one call's overrun)")
# 4 reader during in-flight reservation write (O_CREAT done, bytes not yet written)
d,b = fresh(); b.reserve("a", D(1), config_id="sol-medium")
(d/"owner-run-audit"/"reservations"/"b").write_bytes(b"")  # what a reader sees mid-_write_once
try: Budget(D(10), d).spent; print("reader ok")
except BudgetError as e: print("reader crashes:", e)
# 5 reload: crash-left hold blocks and is counted
d,b = fresh(); b.reserve("a", D(3), config_id="sol-medium")
b2 = Budget(D(10), d); print("crash-left:", b2.unsettled, "reserved", b2.reserved, "stop", b2.stop_kind)
try: b2.release("a"); print("BAD release crash-left")
except RunStopped: print("OK crash-left cannot be released")
