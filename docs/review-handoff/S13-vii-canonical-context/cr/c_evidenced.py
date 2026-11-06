import sys
sys.path.insert(0, "tests")
import test_engine_blank_text as t
from deploy_vii import business_context as bc
sub = t._credit_translation_submission(t.PLAIN)
ct = sub.credit_translations[0].model_copy(update={"confidence": "Insufficient Information", "citations": ()})
sub = sub.model_copy(update={"credit_translations": (ct,)})
issues = bc.validate_business_context(t._pack(), sub)
print("evidenced-row issue raised:", any(i.startswith("cp1a.credit_translation_has_evidenced_row") for i in issues))
print([i for i in issues if "credit_translations" in i or "evidenced" in i])
