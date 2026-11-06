import sys, tempfile
from pathlib import Path
sys.path.insert(0, "tests")
import test_connect_cp3c as tc
tmp = Path(tempfile.mkdtemp(dir=sys.argv[1]))
store, pack = tc.make_store(tmp)
print("heads before:", [(h.module_id, h.status) for h in store.read().heads])
store.replace_pack(pack.model_copy(update={"sources": pack.sources[:1]}))  # accidental swap
store.replace_pack(pack)  # revert to the original pack A
snap = store.read()
print("pack restored:", snap.pack_sha256 == pack.content_hash())
print("heads after revert:", [(h.module_id, h.status) for h in snap.heads])
try:
    store.begin("CP-0")
    print("begin CP-0 ok")
except ValueError as e:
    print("begin CP-0 refused:", e)
for m in [h.module_id for h in snap.heads if h.module_id != "CP-0"][:1]:
    try:
        store.begin(m); print("begin", m, "ok")
    except ValueError as e:
        print("begin", m, "refused:", e)
