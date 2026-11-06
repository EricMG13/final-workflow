"""C05: _MONTH_DAY has no right boundary; 'June 2024' is read as June 20."""
from deploy_workflow.pdf_headers import mapping_headers
cases = [
    ("BS", "CONSOLIDATED BALANCE SHEETS\nJune 2024  June 2023\nAssets\nCash  10  9\n"),
    ("BS", "CONSOLIDATED BALANCE SHEETS\nAs at 30 June\n2024  2023\nCash  10  9\n"),
    ("IS", "CONSOLIDATED STATEMENTS OF OPERATIONS\nSix months ended June\n2024  2023\nRevenue  10  9\n"),
    ("IS", "CONSOLIDATED STATEMENTS OF OPERATIONS\nYear ended December\n2024  2023\nRevenue  10  9\n"),
]
for st, text in cases:
    first = len(text.splitlines())  # last line treated as first data line
    print(st, repr(text.splitlines()[1:-1]), "->", mapping_headers(text, first_data_line=first, statement=st))
