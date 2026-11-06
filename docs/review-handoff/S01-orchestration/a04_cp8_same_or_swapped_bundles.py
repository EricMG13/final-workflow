"""Attack: CP-8 run_comparison with prior == current (the same delivery twice), and with the
current bundle given as prior. Neither is refused; a checked comparison is published."""
import sys, json, shutil
from pathlib import Path
sys.path.insert(0, "/workspace/final-workflow/tests")
import test_cpos_comparison as t
from deploy_workflow.owners import cpos
S = Path(sys.argv[1])
for name, prior in (("same", t.CURRENT), ):
    d = S / "work" / f"a04-{name}"; shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
    path = t.job(d)
    data = json.loads(path.read_text())
    data["prior"] = t.pin(prior / "delivery.json")
    path.write_text(json.dumps(data))
    try:
        report = cpos.run_comparison(path, d / "state", execute=lambda task: t.RESPONSE, check=t.check)
        print(name, "-> published", report.relative_to(d))
    except ValueError as e:
        print(name, "-> refused", e)
# prior/current as_of and run ids
from deploy_vii.contracts import View
for label, b in (("PRIOR", t.PRIOR), ("CURRENT", t.CURRENT)):
    v = View.model_validate_json((b / "view.json").read_bytes())
    print(label, v.run.run_id, v.run.as_of)
