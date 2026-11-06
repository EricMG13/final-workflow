#!/bin/bash
cd /tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S18-issuer-library-server/scratch
ISSUER_LIBRARY_ENGINE_ROOT=/tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S18-issuer-library-server/scratch/engine ISSUER_LIBRARY_PYTHON=/usr/local/bin/python3 FAKE_REVIEW_SECONDS=190 ./issuer-library --state-dir /tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S18-issuer-library-server/scratch/state --workspace /tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S18-issuer-library-server/scratch/ws --no-browser --port 51888 > server.out 2>&1 &
SP=$!
sleep 1
echo "hello" > src.txt
start=$(date +%s)
curl -sS -o resp.body -w 'http=%{http_code} bytes=%{size_download}\n' --noproxy '*' -H 'Host: 127.0.0.1:51888' -H 'Origin: http://127.0.0.1:51888' -H 'X-Issuer-Library: 1'   -F context='{}' -F config=sol-medium -F cap_usd=10 -F modules=CP-4 -F max_turns=7 -F 'source_paths=["a.txt"]' -F 'sources=@src.txt;filename=a.txt'   http://127.0.0.1:51888/api/runs/review > curl.out 2>&1
echo "curl exit=$? elapsed=$(($(date +%s)-start))s" >> curl.out
find ws/intake -maxdepth 2 > intake.after
cat ws/intake/*/status.json >> intake.after 2>/dev/null
kill $SP
