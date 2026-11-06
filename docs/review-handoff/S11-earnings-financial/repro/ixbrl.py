"""Inline XBRL period_lines over spec-valid documents."""
from deploy_workflow.inline_xbrl import parse, period_lines
from deploy_workflow.html_text import convert_html

HEAD = """<html xmlns:ix="http://www.xbrl.org/2013/inlineXBRL"><head><meta charset="{cs}"></head><body>
<div style="display:none"><ix:header><ix:resources>
<xbrli:context id="c1"><xbrli:entity><xbrli:identifier scheme="http://www.sec.gov/CIK">0000001</xbrli:identifier></xbrli:entity>
<xbrli:period><xbrli:startDate>2024-01-01</xbrli:startDate><xbrli:endDate>2024-12-31</xbrli:endDate></xbrli:period></xbrli:context>
<xbrli:unit id="usd"><xbrli:measure>iso4217:USD</xbrli:measure></xbrli:unit>
</ix:resources></ix:header></div>
<p>Revenue {fact}</p></body></html>"""

cases = {
    "fact without optional id": (HEAD.format(cs="utf-8", fact='<ix:nonFraction name="us-gaap:Revenues" contextRef="c1" unitRef="usd" decimals="-6" scale="6" format="ixt:num-dot-decimal">1,234</ix:nonFraction>').encode(), ),
    "windows-1252 declared, 0x92 byte": (HEAD.format(cs="windows-1252", fact='<ix:nonFraction id="f1" name="us-gaap:Revenues" contextRef="c1" unitRef="usd" scale="6" format="ixt:num-dot-decimal">1,234</ix:nonFraction> company\x92s').encode("latin-1"), ),
    "scale attribute with whitespace/plus": (HEAD.format(cs="utf-8", fact='<ix:nonFraction id="f1" name="us-gaap:Revenues" contextRef="c1" unitRef="usd" scale="+6" format="ixt:num-dot-decimal">1,234</ix:nonFraction>').encode(), ),
}
for name, (raw,) in cases.items():
    try:
        print(name, "html ok:", bool(convert_html(raw).text), "| period_lines:", period_lines(parse(raw)))
    except Exception as e:
        print(name, "html ok:", bool(convert_html(raw).text), "| parse ->", type(e).__name__, e)
