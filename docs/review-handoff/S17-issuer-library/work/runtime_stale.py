"""runtime.bundle overlays a re-pinned runtime onto the old one: stale dist-info/modules survive (offline fakes)."""
import importlib.util, io, json, sys, tempfile, zipfile
from pathlib import Path
REPO=Path('/workspace/final-workflow')
sys.path.insert(0,str(REPO/'apps/issuer-library/packaging'))
spec=importlib.util.spec_from_file_location('runtime',REPO/'apps/issuer-library/packaging/runtime.py'); rt=importlib.util.module_from_spec(spec); spec.loader.exec_module(rt)
tmp=Path(tempfile.mkdtemp(dir=sys.argv[1]))
def z(files):
    b=io.BytesIO()
    with zipfile.ZipFile(b,'w') as a:
        for n,c in files.items(): a.writestr(n,c)
    p=tmp/f'z{len(list(tmp.iterdir()))}.zip'; p.write_bytes(b.getvalue()); return p
def fake_download(url,sha,name):
    if name.startswith('python-'): return z({'python.exe':'x'})
    ver=name.split('-')[1]
    files={f'{name.split("-")[0]}-{ver}.dist-info/METADATA':f'Version: {ver}'}
    if ver=='OLD': files['pypdf/removed_in_new.py']='STALE=1'
    return z(files)
class R:
    def __init__(s,d): s.d=d
    def __enter__(s): return io.BytesIO(json.dumps(s.d).encode())
    def __exit__(s,*a): pass
def fake_urlopen(url,timeout=0):
    name=url.split('/pypi/')[1].split('/')[0]; ver=url.split('/')[-2]
    return R({'urls':[{'filename':f'{name}-{ver}-py3-none-any.whl','url':'u','digests':{'sha256':'0'}}]})
rt.download=fake_download; rt.urllib.request.urlopen=fake_urlopen
rt.APP=REPO/'apps/issuer-library'; rt.ROOT=REPO
target=tmp/'windows-amd64'; target.mkdir()
rt.PINS={'pypdf':'OLD'}; rt.bundle(target,'amd64')
rt.PINS={'pypdf':'NEW'}; rt.bundle(target,'amd64')
site=target/'engine/runtime/Lib/site-packages'
print(sorted(p.name for p in site.iterdir()), 'stale module present:', (site/'pypdf/removed_in_new.py').exists())
