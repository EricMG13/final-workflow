"""Live loop reserves with request_reservation_usd (1.05M ceiling); the offline (recorded) loop
reserves with reservation_usd, which refuses above 272K for sol. A recorded live call whose
input bound is between 272K and 1.05M tokens cannot be replayed offline."""
from deploy_workflow.model.pricing import price_of, request_reservation_usd, reservation_usd, price_usage
from deploy_workflow.model.turn import Usage
p = price_of("sol-medium")
bound = 400_000  # tokens; loop bound = ceil(bytes/3.0)+64 => ~1.2 MB request body
print("live hold:", request_reservation_usd(p, bound, 98_304))
try:
    print("offline hold:", reservation_usd(p, bound, 98_304))
except Exception as e:
    print("offline hold refused:", type(e).__name__, e)
# the recorded reply itself prices fine offline (long-context rates exist up to 1.05M)
print("offline price of the recorded usage:", price_usage("sol-medium", Usage(input_tokens=390_000, cached_read_tokens=0, output_tokens=2000), offline=True))
