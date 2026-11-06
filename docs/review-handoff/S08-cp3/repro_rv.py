"""rv_quotes validator attacks: real XLSX bytes through validate_rv_bytes."""
import io, sys
from pathlib import Path
import openpyxl
from deploy_vii.inputs.rv_quotes import COLUMNS, validate_rv_bytes, TEMPLATE

def book(rows):
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "rv_quotes"
    ws.append(list(COLUMNS))
    for r in rows:
        ws.append([str(r.get(c, "")) if r.get(c, "") != "" else None for c in COLUMNS])
    buf = io.BytesIO(); wb.save(buf); return buf.getvalue()

def row(**kw):
    d = dict(provider="Dealer A", as_of="2026-01-09", issuer="Acme", facility_id="TLB-2030",
             instrument="Term Loan B due 2030", quote_kind="observed", currency="USD")
    d.update(kw); return d

def run(label, rows):
    try:
        rep = validate_rv_bytes("q.xlsx", book(rows))
        print(f"== {label}: ok={rep.ok}", *rep.lines(), sep="\n   ")
    except Exception as e:
        print(f"== {label}: CRASH {type(e).__name__}: {e!r}")

run("R1 duplicate quote differing only in case/spacing of key", [
    row(price="98.5"), row(price="97.0", facility_id="tlb-2030", provider="dealer a")])
run("R2 zero and negative price accepted as levels", [row(price="0"), row(price="-5", provider="Dealer B")])
run("R3 bid/ask with huge exponent", [row(bid="1e9999999999999999999999", ask="1")])
run("R4 spread-quoted bid/ask (bid 350 bps wider than ask 325 bps)", [row(bid="350", ask="325")])
print("template exists:", Path(TEMPLATE).exists())
