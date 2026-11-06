import io, zipfile
from deploy_vii.preparation import text_content, prepare_source, SourceRequest

# 1. text_content line numbering vs newline-delimited lines
raw = b"Revenue 10\x0cPage 2 header\nNet debt 42\n"
ext = text_content(raw)
print("splitlines spans:", [(s.locator, s.text) for s in ext.spans])
print("real line of 'Net debt 42':", raw.decode().split("\n").index("Net debt 42") + 1)

# 2/3. xlsx helpers
def xlsx(sheet_xml: str) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("[Content_Types].xml", '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>')
        z.writestr("xl/workbook.xml", '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Data" sheetId="1" r:id="rId1"/><sheet name="Notes" sheetId="2" r:id="rId2"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/></Relationships>')
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml)
        z.writestr("xl/worksheets/sheet2.xml", '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1" s="0"/><c r="B1" s="0"/></row></sheetData><mergeCells count="1"><mergeCell ref="A1:B1"/></mergeCells></worksheet>')
    return buf.getvalue()

MT = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
ok = '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1"><v>42</v></c></row></sheetData></worksheet>'
src = prepare_source(SourceRequest(source_id="wb", path="wb.xlsx", media_type=MT), xlsx(ok))
print("empty Notes sheet coverage:", [(c.locator, c.status) for c in src.coverage])
print("limitation mentions Notes empty:", "sheet:Notes: empty" in (src.limitation or ""))

no_r = '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c><v>42</v></c></row></sheetData></worksheet>'
src = prepare_source(SourceRequest(source_id="wb", path="wb.xlsx", media_type=MT), xlsx(no_r))
print("cell without r:", src.status, src.extraction_status, src.limitation)
