import http.server, json, subprocess, sys, functools
from pathlib import Path
REPO=Path('/workspace/final-workflow'); WEB=REPO/'apps/issuer-library/web'
ws=Path(sys.argv[1]); cat=(ws.parent/'catalogue.json').read_bytes(); port=int(sys.argv[2]); CSP=len(sys.argv)>3
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
    def j(self,b):
        self.send_response(200); self.send_header('Content-Type','application/json'); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        p=self.path.split('?')[0]
        if p=='/api/catalogue': return self.j(cat)
        if p=='/api/workspace':
            out=subprocess.run([str(REPO/'.venv/bin/python'),'-I','-B','-X','utf8',str(REPO/'apps/issuer-library/engine/store.py'),str(ws)],input=cat,capture_output=True).stdout
            return self.j(out)
        if p.startswith('/api/runs/list'): return self.j(b'[]')
        if p.startswith('/files/') or p.startswith('/api/'): self.send_error(404); return
        return super().do_GET()
    def end_headers(self):
        if CSP and not self.path.startswith('/api/'): self.send_header('Content-Security-Policy',"default-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
        super().end_headers()
http.server.ThreadingHTTPServer(('127.0.0.1',port),functools.partial(H,directory=str(WEB))).serve_forever()
