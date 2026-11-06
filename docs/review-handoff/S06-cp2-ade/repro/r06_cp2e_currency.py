"""CP-2E reporting currency: any [A-Z]{3} token in any quoted line passes when the run has no
context, and every money fact is stamped with it."""
import copy, sys
sys.path.insert(0, "tests")
import test_method_cp2e as tm
from deploy_workflow.owners import cp2e
case = "positive"; pages = tm._pages(case); sub = copy.deepcopy(tm.SUBMISSIONS[case])
print("orig:", sub["reporting_currency"])
loc, line = next((k, l) for k, v in pages.items() for l in v.split("\n") if "RCF commitment" in l)
sub["reporting_currency"] = {"source_id": "financial", "locator": loc, "quote": line[:120], "code_text": "RCF"}
print("issues:", cp2e.validate_macro_fx(submission=sub, pages=pages))
res = cp2e.compute(cp2e.inputs_from_submission(sub, source_names=tm._names(case)))
facts = [c.fact() for t in res.tables for r in t.rows for c in r.cells]
print("currencies stamped:", sorted({f.currency for f in facts if f.currency}))
