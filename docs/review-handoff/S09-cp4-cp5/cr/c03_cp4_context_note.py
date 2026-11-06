"""CP-4 CONTEXT: facilities listed yet the note says 'name no facility' when no CP-1 figure is offered."""
from types import SimpleNamespace
from deploy_vii.cp4_legal import Upstream, context_block
up = Upstream(cp0_sha256="0"*64, cp1_sha256="1"*64, cp1_status="restricted", authority={},
              legal_sources=(), facilities={"term-loan": "Senior secured term loan"}, facts=(),
              rows={}, cp1_gaps=("CP-1: reported leverage not disclosed",))
block = context_block(SimpleNamespace(sources=()), up)
print("facilities:", block["facilities"])
print("cp1_facts_note:", block["cp1_facts_note"])
