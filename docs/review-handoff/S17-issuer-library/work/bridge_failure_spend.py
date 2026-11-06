"""bridge.start: a non-ValueError/RuntimeError failure after paid calls drops spent_usd and the retained-work note."""
import importlib.util, json, sys, tempfile, types
from decimal import Decimal
from pathlib import Path
REPO=Path('/workspace/final-workflow')
spec=importlib.util.spec_from_file_location('b',REPO/'apps/issuer-library/engine/bridge.py'); b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
BASE=sys.argv[1]
for exc in (RuntimeError('provider refused'), OSError(32,'The process cannot access the file because it is being used by another process')):
    d=Path(tempfile.mkdtemp(dir=BASE))
    (d/'review.json').write_text(json.dumps({'review_id':'R'}))
    run_dir=d/'run'; run_dir.mkdir()
    b.review=lambda directory:{'review_id':'R','provider_ready':True}
    b.read_job=lambda directory:({'id':'web-x','config':'sol-medium','max_turns':1},d)
    b.launch=lambda job,directory,out:types.SimpleNamespace(directory=run_dir,manifest=None,layout=None,plan=types.SimpleNamespace(provider_cap_usd=Decimal('10')))
    b.checker=lambda layout:None
    spent={'v':Decimal('0')}
    class FakeBudget:
        def __init__(s,cap,path): pass
        @property
        def spent(s): return spent['v']
    b.Budget=FakeBudget
    def fake_run(*a,on_start,on_handoff,**k):
        on_start(types.SimpleNamespace(module_id='CP-1'))
        spent['v']=Decimal('7.42')  # a paid call settled
        raise exc
    b.run_live_handoffs=fake_run
    sys.argv=['bridge.py','start',str(d)]
    try: b.main()
    except SystemExit: pass
    print(type(exc).__name__, 'status.json =', (d/'status.json').read_text().replace('\n',' '))
    print('   progress.json =', (run_dir/'progress.json').read_text().replace('\n',' '))
