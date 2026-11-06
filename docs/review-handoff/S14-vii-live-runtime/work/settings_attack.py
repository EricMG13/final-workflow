import tempfile, pathlib
from deploy_vii.live.settings import load_settings
toml = '''
[ci]
model_calls = "false"
[model_tests]
credential_file = "~/.keys/openrouter"
prompt_bytes_per_token_lower_bound = 3
artifact_root = "runs"
default_effort = "low"
complex_effort = "high"
cumulative_ceiling_usd = inf
candidates = [{key="a", model_id="m", resolution="r"}]
[model_tests.recurring_caps_usd]
e1_per_case = inf
e2_per_milestone = -5
e3_per_week = nan
'''
d = pathlib.Path(tempfile.mkdtemp(dir="/tmp/claude-0/-workspace-final-workflow/10d71552-cdca-5952-86dc-d4ef0b76ab9e/scratchpad/review/S14-vii-live-runtime/work")); p = d/"project.toml"; p.write_text(toml)
s = load_settings(p, root=d)
print("model_calls_in_ci:", s.model_calls_in_ci, "caps:", s.caps, "credential_file:", s.credential_file)
