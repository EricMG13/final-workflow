from pydantic import BaseModel
import json
class C(BaseModel):
    source_id: str
    locator: str
p = '{"source_id":"s","locator":"page:999","locator":"page:1"}'
print("pydantic:", C.model_validate_json(p).locator, "json:", json.loads(p)["locator"])
for raw in ['{"source_id":"s\\ud800","locator":"x"}']:
    try: print("pyd surrogate ok", C.model_validate_json(raw))
    except Exception as e: print("pyd refuses surrogate:", type(e).__name__)
