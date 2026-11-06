from deploy_vii.quotes import quoted
from deploy_vii.cp4_legal import parse_threshold
quote = "the Total Net Leverage Ratio shall not exceed 12.50:1.00 as of the last day"
for threshold_text in ("2.50:1.00", "2.50", "50:1.00"):
    print(repr(threshold_text), "quoted in covenant text:", quoted(threshold_text, quote))
print("span says $11.2 billion; quote '1.2 billion' accepted:", quoted("1.2 billion", "total debt of $11.2 billion"))
print("one-letter quote accepted:", quoted("a", "Any page text at all"))
import inspect; print(inspect.signature(parse_threshold))
for u in ("ratio", "multiple", "x"):
    try: print(u, parse_threshold("2.50:1.00", u))
    except Exception as e: print(u, "err", e)
