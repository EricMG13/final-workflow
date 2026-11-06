import io, random, collections, traceback, zipfile
from deploy_vii.preparation import prepare_source, SourceRequest
X='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
NS='xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
parts={
 "xl/workbook.xml": f'<workbook {NS}><sheets><sheet name="IS" sheetId="1" r:id="rId1"/></sheets></workbook>',
 "xl/_rels/workbook.xml.rels": '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="x" Target="worksheets/sheet1.xml"/></Relationships>',
 "xl/sharedStrings.xml": f'<sst {NS}><si><t>Revenue</t></si></sst>',
 "xl/worksheets/sheet1.xml": f'<worksheet {NS}><sheetData><row r="1"><c r="A1" t="s"><v>0</v></c><c r="B1"><v>1234.5</v></c></row></sheetData></worksheet>' + " "*2000,
}
buf=io.BytesIO()
with zipfile.ZipFile(buf,"w",zipfile.ZIP_DEFLATED) as z:
    for k,v in parts.items(): z.writestr(k,v)
base=buf.getvalue()
req=SourceRequest(source_id="s",path="x.xlsx",media_type=X)
print(prepare_source(req,base).status)
random.seed(2); crash=collections.Counter(); ex={}
for n in range(3000):
    b=bytearray(base)
    for _ in range(random.randint(1,4)):
        j=random.randrange(len(b)); b[j]=random.randrange(256)
    try: prepare_source(req,bytes(b))
    except Exception as e:
        k=f"{type(e).__module__}.{type(e).__name__}"; crash[k]+=1; ex.setdefault(k,(str(e)[:100]))
        if crash[k]==1: open(__file__.replace("fuzz_xlsx.py",f"crash_{type(e).__name__}.xlsx"),"wb").write(bytes(b))
print(crash); print(ex)
