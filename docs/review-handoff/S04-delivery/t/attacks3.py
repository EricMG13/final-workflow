from deploy_workflow.reader_summary import reader_issues
base = """# CP-1 Acme Corp
## Request
x
## Sources
y
## Findings
### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| {bl} | Medium | Source scope limited |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| {f} | Weaker cushion | Medium |

### Financials
| Metric | FY2024 |
| --- | --- |
| Revenue change | (12.3)% |
| Net leverage | 4.1x |
| Cash | 250 US$ thousands |
## Calculations
## Gaps
## Next module
"""
cases = {
  "sign flipped: handoff (12.3)% decline, summary says grew 12.3%": ("Revenue grew 12.3% in FY2024.", "Leverage 4.1x"),
  "unit swapped: 4.1x stated as 4.1%": ("Revenue fell 12.3%.", "Leverage margin of 4.1%"),
  "scale swapped: 250 thousand stated as 250 million": ("Cash of US$250 million.", "Leverage 4.1x"),
  "control: number absent": ("Revenue fell 13.0%.", "Leverage 4.1x"),
}
for name, (bl, f) in cases.items():
    print(name, "->", reader_issues(base.format(bl=bl, f=f)) or "ACCEPTED (no issues)")
