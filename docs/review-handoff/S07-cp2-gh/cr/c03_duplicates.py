"""Show that cp2h re-defines cp2g helpers with identical bodies (C03)."""
import ast, inspect, textwrap
from deploy_workflow.owners import cp2g, cp2h, cp4c

def body(mod, name):
    node = ast.parse(textwrap.dedent(inspect.getsource(getattr(mod, name)))).body[0]
    if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
        node.body = node.body[1:]  # drop docstring
    return ast.dump(node)

for name in ("stale_issues", "_run_text_issues", "SynthesisGap"):
    print(name, "cp2g==cp2h:", body(cp2g, name) == body(cp2h, name),
          "cp2g==cp4c:", body(cp2g, name) == body(cp4c, name))
