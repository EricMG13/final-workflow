import sys
sys.path.insert(0, "tests")
from deploy_vii.quotes import quoted
from deploy_vii import prose
from deploy_vii.contracts import Claim

print("== quoted")
print(quoted("2.50:1.00", "shall not exceed 12.50:1.00 as of the last day"))
print(quoted("1.2 billion", "total debt of $11.2 billion"))
print(quoted("a", "The Company has a revolving facility"))

print("== prose bare figures")
for text in ("Covenant headroom was breached in 3 of 4 quarters.",
             "Margin fell by 2024 basis points.",
             "Leverage rose to five times EBITDA.",
             "Leverage rose to 5x EBITDA."):
    print(repr(text), "->", prose.check(text, refs=(), gaps=()))

print("== issuer name in claim text")
for name in ("Acme Holdings [UK] Ltd", "Acme [Holdings Ltd", "Acme {Group}"):
    text = f"Leverage · Title\n\nEvidence\n{name} reported higher leverage"
    try:
        Claim(claim_id="f1", text=text, citations=())
        print(repr(name), "-> Claim ok; prose.issues:", prose.issues(text, {}, names=(name,)))
    except Exception as e:
        print(repr(name), "-> Claim raises:", str(e).splitlines()[-1][:120])
