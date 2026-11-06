import json
from typing import Annotated
from pydantic import Field, ValidationError
from deploy_vii.contracts import Contract
from deploy_vii.readiness import shape_issues

class M(Contract):
    a: Annotated[tuple[int, ...], Field(min_length=3)]

for value in ([1, 2, "x"], [1, "x"], [1]):
    try:
        M.model_validate_json(json.dumps({"a": value}))
    except ValidationError as e:
        raw = [(x["loc"], x["type"]) for x in e.errors()]
        print(value, "pydantic:", raw)
        print("   shape_issues:", shape_issues(e))
