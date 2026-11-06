"""Repro: prepare_source lets pypdf errors escape instead of returning an unreadable Source."""
import io, random, logging, sys
logging.disable(logging.CRITICAL)
sys.argv=[""]
exec(open(__file__.replace("repro_pdf_crash.py","fuzz_pdf.py")).read().split("random.seed(1)")[0])
random.seed(1)
saved = {}
for n in range(1500):
    b = bytearray(base)
    for _ in range(random.randint(1, 8)):
        j = random.randrange(len(b)); b[j] = random.randrange(256)
    try:
        prepare_source(req, bytes(b))
    except Exception as e:
        k = type(e).__name__
        if k not in saved:
            saved[k] = bytes(b)
            open(__file__.replace("repro_pdf_crash.py", f"crash_{k}.pdf"), "wb").write(bytes(b))
    if len(saved) == 2: break
for k, raw in saved.items():
    try:
        prepare_source(req, raw); print(k, "no crash")
    except Exception as e:
        print(f"{k}: prepare_source raised {type(e).__module__}.{type(e).__name__}: {str(e)[:90]}")
