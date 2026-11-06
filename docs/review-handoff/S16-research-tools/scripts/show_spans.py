import sys; sys.path.insert(0,'tests/research')
from cpdr_peers_support import peers_case
c=peers_case()
for s in c.sources:
    if s.source_id=='ev-1':
        for sp in s.spans[:20]: print(repr(sp.locator), repr(sp.text))
