import io, random, collections, traceback, logging
logging.disable(logging.CRITICAL)
from pypdf import PdfWriter
from pypdf.generic import NameObject, DecodedStreamObject, DictionaryObject
from deploy_vii.preparation import prepare_source, SourceRequest
import deploy_vii.preparation as P
P.shutil.which = lambda n: None  # no OCR
w = PdfWriter()
for i in range(3):
    page = w.add_blank_page(612, 792)
    s = DecodedStreamObject(); s.set_data(f"BT /F1 12 Tf 72 700 Td (Revenue {i} 1,234.5) Tj ET".encode())
    font = DictionaryObject({NameObject("/Type"): NameObject("/Font"), NameObject("/Subtype"): NameObject("/Type1"), NameObject("/BaseFont"): NameObject("/Helvetica")})
    page[NameObject("/Resources")] = DictionaryObject({NameObject("/Font"): DictionaryObject({NameObject("/F1"): font})})
    page[NameObject("/Contents")] = w._add_object(s)
buf = io.BytesIO(); w.write(buf); base = buf.getvalue()
req = SourceRequest(source_id="s", path="x.pdf", media_type="application/pdf")
print(prepare_source(req, base).status)
random.seed(1)
crash = collections.Counter(); ex = {}
for n in range(1500):
    b = bytearray(base)
    for _ in range(random.randint(1, 8)):
        j = random.randrange(len(b)); b[j] = random.randrange(256)
    try:
        prepare_source(req, bytes(b))
    except Exception as e:
        k = type(e).__name__; crash[k] += 1; ex.setdefault(k, traceback.format_exc().splitlines()[-4:])
print(crash)

for k, v in ex.items(): print(k, v)
