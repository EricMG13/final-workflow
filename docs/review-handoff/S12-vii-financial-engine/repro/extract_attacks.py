from deploy_vii.statement_extract import extract_statement_lines
page = """CONSOLIDATED STATEMENTS OF OPERATIONS
                                   2025        2024
Revenue                           1,200       1,100
Net loss                         -1,234        -567
Other expense                    −123        −45
Umsatzerlöse                     1.234         987
Tax rate                          12.5%       11.0%
Operating income                    300         250
"""
t = extract_statement_lines(page, "p1")
for l in t.lines:
    print("DATA", l.line_no, repr(l.label), l.raw_values, l.values, l.flags)
for o in t.omitted:
    print("OMITTED", o.line_no, repr(o.text))
