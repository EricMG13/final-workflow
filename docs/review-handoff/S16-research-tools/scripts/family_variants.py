"""Independence rule compares family labels exactly: 'Reuters' and 'Reuters ' / 'reuters' count as
two independent families."""
from deploy_workflow.research.review import _family_issues
from deploy_workflow.research.intake import parse_rows
rows = parse_rows([{"path": "a.txt", "family": "Reuters ", "locator": "a", "tag": "research"},
                   {"path": "b.txt", "family": "reuters", "locator": "b", "tag": "research"}])
print("intake keeps:", [r.family for r in rows])
fam = {"ev-1": "Reuters", "ev-2": "Reuters ", "ev-3": "reuters", "ev-4": "Reuters"}
print("ev-1/ev-2:", _family_issues("q", ["ev-1", "ev-2"], fam))
print("ev-1/ev-3:", _family_issues("q", ["ev-1", "ev-3"], fam))
print("ev-1/ev-4:", [str(i) for i in _family_issues("q", ["ev-1", "ev-4"], fam)])
