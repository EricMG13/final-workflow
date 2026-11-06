from itertools import combinations
from deploy_vii.bindings.shipped import SHIPPED_MAPS
from deploy_vii.bindings import RAIL_DESTINATIONS
from deploy_vii.report_view import pathways
def overlap(a, b):
    ca, cb = a.fact_coord, b.fact_coord
    return ca.module_id == cb.module_id and all(x is None or y is None or x == y for x, y in
        ((ca.table_id, cb.table_id), (ca.row_id, cb.row_id), (ca.fact_id, cb.fact_id)))
for p in pathways():
    composed = RAIL_DESTINATIONS | set(p.blocks)
    for m in SHIPPED_MAPS:
        for a, b in combinations(m.entries, 2):
            if overlap(a, b) and (a.block_id == b.block_id or (a.block_id in composed and b.block_id in composed)):
                print(p.id, m.module_id, a.fact_coord.table_id, a.fact_coord.row_id, a.block_id, "|", b.fact_coord.table_id, b.fact_coord.row_id, b.block_id)
print("blocks per pathway:")
for p in pathways(): print(p.id, p.blocks)
