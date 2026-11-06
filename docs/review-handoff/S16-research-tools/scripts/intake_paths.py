"""Intake path attacks: NUL byte, symlink out, dir symlink, absolute, FIFO, directory."""
import os, sys
from datetime import date
from pathlib import Path
from deploy_workflow.research.intake import parse_rows, intake
base = Path(sys.argv[1])
fifo = base / "fifo.txt"
if not fifo.exists(): os.mkfifo(fifo)
for p in ["a.txt", "a\x00b.txt", "out.txt", "sub/etcdir/hostname", "/etc/hostname", "../m/a.txt", "fifo.txt", "sub", "missing.txt"]:
    rows = parse_rows([{"path": p, "family": "f", "locator": "loc", "tag": "research", "published": "2026-01-01"}])
    try:
        r = intake(rows, base_dir=base, dest_dir=None, as_of=date(2026,6,30), cutoff=date(2026,6,30), today=date(2026,11,6))
        print(f"{p!r:28} accepted={[a.item_id for a in r.accepted]} refused={[x.reason for x in r.refused]}")
    except Exception as e:
        print(f"{p!r:28} RAISED {type(e).__name__}: {e}")
