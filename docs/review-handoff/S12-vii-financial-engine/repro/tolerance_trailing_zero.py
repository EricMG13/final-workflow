"""Reporting-precision tolerance is read from the parsed Decimal exponent, but Pydantic's JSON
parse drops trailing zeros of JSON numbers (the live path: json_object -> exact_json ->
model_validate_json), so a total printed `1,234.0` (one decimal) gets tolerance 0.5, not 0.05.

Hand-derived: printed 1234.0 has one decimal -> tolerance 0.05. Components 1000.0 + 233.6 =
1233.6 -> difference -0.4 -> must not PASS.
"""
import sys
sys.path.insert(0, "tests")
from deploy_vii.live.schema import json_object, exact_json
from deploy_vii.financial_contracts import Observation
from deploy_vii.financial_reconciliation import _check, _term
import test_cash_scope as cs

def parse(amount_text, oid):
    payload = '{"observation_id":"%s","status":"known","amount":%s,"citations":[{"source_id":"k","source_sha256":"%s","locator":"page:1","quote":"q"}]}' % (oid, amount_text, "a"*64)
    text = exact_json(json_object(payload))
    return Observation.model_validate_json(text)

total = parse("1234.0", "tot")
print("parsed total:", repr(total.amount), "exponent", total.amount.as_tuple().exponent)
a, b = parse("1000.0", "a"), parse("233.6", "b")
period = cs.flow(cs.book(), "fy-2025")
check = _check(period, "SOURCE_STATEMENT_IDENTITY", "x", _term("total", total), (_term("a", a), _term("b", b)), "a+b")
print("tolerance", check.tolerance, "difference", check.difference, "status", check.status)
