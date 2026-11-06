from deploy_workflow.research.webfetch import is_public
cases = {
 "64:ff9b::7f00:1": "NAT64 of 127.0.0.1",
 "64:ff9b::a9fe:a9fe": "NAT64 of 169.254.169.254 (metadata)",
 "64:ff9b::a00:1": "NAT64 of 10.0.0.1",
 "64:ff9b:1::a00:1": "local-use NAT64 10.0.0.1",
 "2002:7f00:1::": "6to4 127.0.0.1",
 "2002:a9fe:a9fe::": "6to4 169.254.169.254",
 "2002:a00:1::": "6to4 10.0.0.1",
 "2001:0:4136:e378:8000:63bf:3fff:fdd2": "teredo",
 "::127.0.0.1": "IPv4-compatible 127.0.0.1",
 "::a9fe:a9fe": "IPv4-compatible 169.254.169.254",
 "::ffff:0:7f00:1": "SIIT 127.0.0.1",
 "100.64.0.1": "CGNAT", "0.0.0.0": "zero", "fe80::1%eth0":"ll scoped","fd00:ec2::254":"AWS IMDS v6",
 "192.0.0.171": "192.0.0/24", "198.18.0.1":"bench","8.8.8.8":"public", "2606:4700::1111":"public6",
}
for a,d in cases.items(): print(f"{a:40} {is_public(a)!s:6} {d}")
