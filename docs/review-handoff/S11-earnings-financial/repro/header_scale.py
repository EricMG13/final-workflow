"""Share-count scale under common US header phrasings (expected by hand from the header text)."""
from deploy_workflow.statement_compose import _header_scale, _currency_matches
cases = [
    ("(in thousands, except share and per share data)", "UNITS"),
    ("(in thousands, except per share and share data)", "UNITS"),
    ("(in millions, except per share amounts and number of shares)", "UNITS"),
    ("(in thousands, except per share amounts and share counts)", "UNITS"),
    ("(in millions, except per share data; shares in thousands)", "THOUSANDS"),
]
for header, expected in cases:
    got = _header_scale(header.casefold(), True)
    print(f"{'OK ' if got == expected else 'BAD'} shares scale {got!r:12} expected {expected!r:12} {header}")
print("EUR book, header '(in millions of US$)':", _currency_matches("EUR", "(in millions of us$)"))
