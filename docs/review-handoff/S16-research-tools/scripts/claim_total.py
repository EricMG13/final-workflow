"""A claim_id 'total' composes a TDR.2 row marked row_kind='total'."""
import copy, json, sys
sys.path.insert(0, 'tests/research'); sys.path.insert(0, 'tests')
from pathlib import Path
from cpdr_o7b1b_support import brief, evidence, sources
from deploy_vii.contracts import validate_tables
from deploy_workflow.research import review, tables as t
case = Path('cases/cpdr-research-owner')
exp = json.loads((case/'expected.json').read_text()); subs = json.loads((case/'submissions.json').read_text())
man = json.loads((case/'manifest.json').read_text())
body = copy.deepcopy(subs['research_v1'])
first = next(a for a in body['answers'] if a['claims'])
first['claims'][0]['claim_id'] = 'total'
sub = review.ResearchSubmission.parse(body)
b = brief(exp, 'positive'); ev = evidence(exp)
print('issues:', [str(i) for i in review.research_issues(submission=sub, brief=b, evidence=ev, sources=sources(man))])
comp = t.compose(b, sub, ev, review.answer_counts(sub), review.claim_states(sub, b), b.as_of.isoformat())
tdr2 = next(x for x in comp.tables if x.table_id == 'TDR.2')
print([(r.row_id, r.row_kind) for r in tdr2.rows])
try:
    validate_tables(comp.tables, comp.facts); print('validate_tables ok')
except Exception as e: print('validate_tables', type(e).__name__, e)
