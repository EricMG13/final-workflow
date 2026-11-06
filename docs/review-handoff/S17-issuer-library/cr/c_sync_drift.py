# Recompute sync_assets.py outputs in memory and compare with the checked-in web files (no writes to the repo).
import base64, re, json
from pathlib import Path
ROOT = Path("/home/user/final-workflow"); APP = ROOT / "apps/issuer-library"; WEB = APP / "web"; SHARED = ROOT / "src/deploy_vii/assets"
form = (ROOT / 'docs/templates/context-form.html').read_text()
print("</body> count", form.count("</body>"), "</head> count", form.count("</head>"))
for number, label in [(4, 'Deal terms'), (5, 'Quotes'), (7, 'Valuation')]:
    form = form.replace(f'section {number}', f'“{label}”')
form = re.sub(r'\.\./\.\./src/deploy_vii/assets/fonts/([^\x27]+)', lambda m: 'data:font/woff2;base64,' + base64.b64encode((SHARED/'fonts'/m[1]).read_bytes()).decode(), form)
form = form.replace("font-src 'self'", "font-src data:")
form = form.replace('</head>', '<style>' + (WEB / 'context-embed.css').read_text() + '</style></head>')
form = form.replace('</body>', '<script>' + (WEB / 'context-embed.js').read_text() + '</script></body>')
cur = (WEB / 'context-form.html').read_text()
print("context-form.html matches sync output:", form == cur)
symbol = base64.b64encode((WEB / 'brand/symbol.svg').read_bytes()).decode()
brand = '.brand-mark { border:0; background:center / 24px 24px no-repeat ' f'url("data:image/svg+xml;base64,{symbol}"); }}\n'
print("brand.css matches:", brand == (WEB/'brand.css').read_text())
c = json.loads((ROOT / 'examples/issuer-library/catalog.json').read_text()); c['illustrative'] = []
print("legacy-catalog matches:", json.dumps(c, indent=2) + '\n' == (WEB/'legacy-catalog.json').read_text() if (WEB/'legacy-catalog.json').exists() else "missing")
print("section 4/5/7 phrases replaced in standalone template:", [p for p in ['section 4','section 5','section 7'] if p in (ROOT/'docs/templates/context-form.html').read_text()])
