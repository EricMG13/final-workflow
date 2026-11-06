import time
from datetime import date
from deploy_vii.contracts import Run, Source, Span
from deploy_vii.preparation import PreparedPack
from deploy_vii.live.tools import PackTools, ToolError, MAX_LINE_READ_BYTES
run = Run(run_id="r", issuer_id="i", issuer_name="I", as_of=date(2025,12,31), case_kind="synthetic")
H = "a"*64
def pack(sources): return PreparedPack(run=run, sources=tuple(sources))
# 1. line source byte cap inconsistency
big = "x"*1_000_000
lines = Source(source_id="txt", name="t", status="ready", sha256=H,
               spans=tuple(Span(locator=f"line:{i}", text=big if i<=5 else "y"*6000) for i in range(1,12)))
t = PackTools(pack([lines]))
out = t.read_pages({"source_id":"txt","first_page":1,"last_page":5})
print("5-line read bytes:", len(out.encode()), "cap for wider reads:", MAX_LINE_READ_BYTES)
try:
    t.read_pages({"source_id":"txt","first_page":6,"last_page":11}); print("6-line 36KB read accepted")
except ToolError as e: print("6-line read of 36KB refused:", str(e)[:60])
# 2. search query term DoS
spans = tuple(Span(locator=f"page:{i}", text=("Revenue grew while costs fell. "*100)) for i in range(1,301))
p = PackTools(pack([Source(source_id="fin", name="f", status="ready", sha256=H, spans=spans)]))
for n in (100, 2000, 8000):
    q = " ".join(f"w{i}" for i in range(n))
    s=time.time(); r = p.search_pack({"query": q}); dt=time.time()-s
    print(f"query terms={n} query_bytes={len(q)} seconds={dt:.2f} result_bytes={len(r)}")
