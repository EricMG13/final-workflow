# Repro: validate.clean_env() strips three provider keys but passes the Copilot token through to every gate.
import importlib.util, os
from pathlib import Path
spec = importlib.util.spec_from_file_location("validate", "/home/user/final-workflow/apps/issuer-library/validate.py")
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
from deploy_workflow.model.adapter import KEY_VARIABLES
for name in KEY_VARIABLES.values():
    os.environ[name] = "dummy-not-a-key"
env = v.clean_env()
print({p: (n in env) for p, n in KEY_VARIABLES.items()})
