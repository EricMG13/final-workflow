"""Typed composition of a share-count row under '(In thousands, except per share and share data)'.
By hand: the header excepts share data from the thousands scale, so shares are UNITS."""
from deploy_vii.contracts import Citation
from deploy_vii.financial_contracts import StatementQuantity
from deploy_vii.statement_extract import extract_statement_lines
from deploy_workflow.statement_compose import RowJudgment, compose_unit

SID, H, PAGE = "issuer", "a" * 64, "page:7"
HDR = "(In thousands, except per share and share data)"
TEXT = f"""STATEMENT OF OPERATIONS
{HDR}
2024       2023
Weighted average shares outstanding     41,234,567     40,987,654
Net sales                            10          9
"""
table = extract_statement_lines(TEXT, PAGE, SID)
row = table.lines[0]
print("row:", row.label, row.values)
for scale in ("UNITS", "THOUSANDS"):
    q = StatementQuantity(kind="shares", scale=scale, citations=(Citation(source_id=SID, source_sha256=H, locator=PAGE, quote=HDR),))
    r = compose_unit(table, source_id=SID, source_sha256=H, unit_locator=PAGE, kind="IS",
        column_periods=("FY2024", "FY2023"),
        row_map={row.line_no: RowJudgment("washo", "other:shares", "detail", "signed")},
        declared_periods=("FY2024", "FY2023"),
        row_label_selections={row.line_no: (row.line_no,)},
        row_dimensions={row.line_no: q}, typed_profile=True, book_currency="USD", book_unit="THOUSANDS")
    print(f"model scale {scale:9}: composed={len(r.lines)} left={[x.reason for x in r.left_to_model]}")
