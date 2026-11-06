"""Run text may attach any period label to a referenced figure; the fact's own period is never compared."""
from decimal import Decimal
from deploy_vii.contracts import Fact
from deploy_vii import prose
from deploy_vii.business_context import spelled

fy23 = Fact(fact_id="rev-fy2023", label="Revenue", amount=Decimal("812"), unit="MILLIONS",
            currency="USD", scale=Decimal(1000000), period="FY2023: 2023-01-01 to 2023-12-31",
            calculation_id="calc-rev-fy2023")
bound = prose.bind([fy23])
text = "FY2025 revenue reached {rev-fy2023}, up from FY2024."
print("issues:", prose.issues(text, bound))
print("rendered figure:", spelled(fy23), "| fact period:", fy23.period)
