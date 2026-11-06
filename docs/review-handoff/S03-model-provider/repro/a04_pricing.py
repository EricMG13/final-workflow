from decimal import Decimal as D
from deploy_workflow.model.pricing import price_usage, request_reservation_usd, price_of, reservation_usd
from deploy_workflow.model.turn import Usage
# hand-derived expectations
cases = [
 ("sol-medium", Usage(input_tokens=300000, cached_read_tokens=100000, output_tokens=1000), False, D("0.835")),
 ("sol-medium", Usage(input_tokens=272000, cached_read_tokens=0, output_tokens=0), False, D("0.544")),
 ("sol-medium", Usage(input_tokens=272001, output_tokens=0), False, D("1.088004")),
 ("opus-medium", Usage(input_tokens=1000, cached_read_tokens=2000, cache_write_tokens=400, cache_write_5m_tokens=300, cache_write_1h_tokens=100, output_tokens=500), False, D("0.0167")),
 ("opus-medium", Usage(input_tokens=1000, cached_read_tokens=None, output_tokens=5), False, None),
 ("sol-medium", Usage(input_tokens=None, output_tokens=5), False, None),
 ("sol-medium", Usage(input_tokens=10, cached_read_tokens=20, output_tokens=5), False, None),  # cached > input
 ("deepseek-max", Usage(input_tokens=1000, cached_read_tokens=0, output_tokens=0), False, None),  # live openrouter, no billed
 ("deepseek-max", Usage(input_tokens=1000, cached_read_tokens=0, output_tokens=0), True, D("0.00045")),
 ("copilot-sol-medium", Usage(input_tokens=1000, output_tokens=10), False, None),
 ("copilot-sol-medium", Usage(input_tokens=1000, output_tokens=10), True, None),
 ("sol-medium", Usage(input_tokens=1_050_001, output_tokens=0), False, None),
]
for cfg, u, off, want in cases:
    got = price_usage(cfg, u, None, offline=off).usd
    print("OK " if got == want else "BAD", cfg, off, got, want)
print(request_reservation_usd(price_of("sol-medium"), 10, 1000), "want", D("5.25")+D("0.015"))
print(request_reservation_usd(price_of("copilot-opus-medium"), 1000, 1000), "want", D("0.008")+D("2.56"))
