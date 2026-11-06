"""CP-4C: a CP-4 head whose rating is not the pinned 'Insufficient Information' (or whose basket
r02 conditions differ) passes every content check, then the composer raises inside the step
validator; the view (sent to the model) offers that very head without an issue."""
import sys
from dataclasses import replace
sys.path.insert(0, "tests")
import test_method_cp4c as t
from deploy_workflow.owners import cp4c

ctx = t._context("positive")
facts = tuple(t._refact(f, text="Adequate") if f.fact_id == "T4.13.rating.rating" else f for f in ctx.cp4.facts)
bad = replace(ctx, cp4=replace(ctx.cp4, facts=facts))
inputs = cp4c.Cp4cInputs(context=bad, submission=t._inputs("positive").submission)
print("content_issues (what _lines/_validate_step checks first):", cp4c.content_issues(inputs))
try:
    cp4c.compute(inputs)
    print("composed")
except ValueError as e:
    print("compute raised ValueError:", str(e)[:160])
