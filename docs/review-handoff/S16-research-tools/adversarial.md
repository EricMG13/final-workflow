SECTION: S16-research-tools   PASS: adversarial
COVERAGE: read fully: research/{__init__,anchors,brief,contracts,dossier,evidence,intake,peers,review,steps,tables,webfetch}.py, tools/{__init__,source}.py / skimmed: tools/upstream.py (lines 1-890 in full: v1/v2 grants, lookup, verify, invoke, paging; integrity catalogue 890-1838 only at safe_fact/_citation_set/_payload) / not read: rest of upstream.py _IntegrityCatalog lineage code
Repro scripts: `<review root>/S16-research-tools/scripts/`. Run each as `cd /workspace/final-workflow && PYTHONPATH=src:. .venv/bin/python <script>`.

### S16-research-tools-A01  [high] [CONFIRMED]  Identity / quote anchoring (wrong figure accepted as "located")
- Location: `src/deploy_workflow/research/peers.py:295` (`_amount_cell` -> `amount_from_quote`), with the check at `peers.py:144-149` (`_citation_issues` -> `deploy_vii.readiness.citation_issues`)
- Defect: a TDR.6 figure's amount is read from `citation.quote`. The only check on that quote is `quotes.quoted`, which accepts any contiguous substring of the span. Nothing checks that the quote is a whole figure token, so part of a number, a sign-less number, or a year or date fragment is accepted as the "located" amount.
- Failure scenario: span `ev-1 line:11` = "Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 200.0". The model submits revenue quote "20", "0.0", "2025" or "-12". `peer_issues` returns no issue, and `compose_peer_tables` writes a `known` source fact: revenue 20, 0.0, 2025 or -12 (USD MILLIONS, "Twelve months to 2025-12-31"). The same substring rule lets "12.3" pass from a span reading "(12.3)" or "-12.3", so the sign is lost. `cp1c._pack_sheet` -> `peer_sheet` (`peers.py:450-453`) then takes the head fact as the peer amount with no further check, so the wrong figure reaches CP-1C's peer sheet and the deliverables built from it.
- Evidence: `scripts/peer_quote_substring.py` prints, for each quote: `quote='20' issues=[] status=known amount=20 unit=MILLIONS`; `quote='0.0' ... amount=0.0`; `quote='2025' ... amount=2025`; `quote='-12' ... amount=-12`. The expected result, worked out by hand, is an issue or a `missing` cell, because the span states only 200.0.
- Fix direction: accept a figure quote only if it sits in the span with no digit, `.`, `,` or sign right before or after it (and refuse it next to `(`/`-`). Better still, make the citation quote the whole `<label>: <figure>` line and parse the figure out of it.

### S16-research-tools-A02  [high] [CONFIRMED]  Units / currency / period invented or unverified on the pack path
- Location: `src/deploy_workflow/research/peers.py:298-308` (`_amount_cell`), `peers.py:90-96` (`LocatedFigure`)
- Defect: the `unit` (scale), `currency` and duration of a TDR.6 figure are model text that is never checked against the cited span. Python also writes `period="Twelve months to <period_end>"` for every figure. `LocatedFigure` has no duration field, so a quarterly or half-year figure cannot be told apart from an annual one. The user-source path of CP-1C reads currency, unit and the twelve-month basis from a `Basis:` line in the source (`cp1c._basis`). The pack path skips that check.
- Failure scenario: the cited span reads "...revenue for the three months to 2025-12-31, EUR thousands: 200.0". The model declares `unit: millions` and `currency: USD`. There is no review issue, and the fact becomes 200.0 MILLIONS USD, scale 1000000, "Twelve months to 2025-12-31". `peer_sheet` admits it, because it is in the run's currency and in millions. The result is a 1000x scale error, a currency error and a 4x period error in CP-1C's peer figures.
- Evidence: `scripts/peer_unit_period.py`. It edits the span text and keeps the source hash, as a held item would carry. Output: `issues: []` / `fact: 200.0 MILLIONS USD 1000000 'Twelve months to 2025-12-31'`.
- Fix direction: require the cited span (or a basis line in the same `ev-*` item) to state the currency, the scale and a twelve-month basis, as `cp1c._basis` does for a user source. Otherwise compose the amount as `missing` with a limitation, not as a twelve-month figure.

### S16-research-tools-A03  [medium] [CONFIRMED]  Swallowed contract: network-layer error escapes fetch and aborts all intake
- Location: `src/deploy_workflow/research/webfetch.py:165-168` (`resolve_public` catches only `OSError`), `webfetch.py:177-180` (`system_resolver`), `webfetch.py:517` (`fetch` catches `OSError`/`HTTPException`)
- Defect: `check_url` accepts a host that the IDNA codec refuses, such as an empty label (`www..example.com`) or a label longer than 63 characters. `socket.getaddrinfo` then raises `UnicodeEncodeError`, which is a `ValueError` and not an `OSError`. The error escapes `fetch()`, even though its docstring says network failures are refusals recorded on the `FetchRecord`.
- Failure scenario: a research manifest url row with a typo, `https://www..example.com/a`, passes `parse_rows`. `intake` then raises a raw `UnicodeEncodeError` out of `run_inputs._research_staging`/`check_arguments`, which is not a `RunInputError` or `ResearchError`. The whole run stops: no `rejected.json` entry, and no other row is assessed.
- Evidence: `unshare -n env PYTHONPATH=src:. .venv/bin/python scripts/idna_crash.py` (no network) prints: `ESCAPED: UnicodeEncodeError 'idna' codec can't encode character '\x2e' in position 4: label empty` and `ESCAPED: UnicodeEncodeError ... label too long`.
- Fix direction: in `resolve_public`, catch `UnicodeError` (or `ValueError`) and turn it into a `FetchRefusal`, or reject such hosts in `_shape` by checking `host.encode("idna")`.

### S16-research-tools-A04  [low] [CONFIRMED]  Independence rule defeated by label variants
- Location: `src/deploy_workflow/research/review.py:175-189` (`_family_issues`); labels are kept unnormalised at `intake.py:109-123` (`_cell_text`)
- Defect: the rule "two items of one family never count as independent" compares raw family strings, so labels that differ only in trailing whitespace or case count as different families.
- Failure scenario: the manifest gives `family: "Reuters"` for ev-1 and `"Reuters "` or `"reuters"` for ev-2. A claim that lists both as `independent_items` passes review as independently corroborated.
- Evidence: `scripts/family_variants.py` -> `ev-1/ev-2: []`, `ev-1/ev-3: []`, while an exact match gives `families not independent`.
- Fix direction: compare `family.strip().casefold()` in `_family_issues`, or normalise or refuse such labels at intake.

### S16-research-tools-A05  [low] [CONFIRMED]  A model claim_id or peer_id `total` makes an ordinary row a total row
- Location: `src/deploy_workflow/research/tables.py:165` (`_Table.add`, `row_kind="total" if row_id == TOTAL_ROW`)
- Defect: every table uses `_Table.add`, and any row whose id is `total` is marked `row_kind="total"`. Only TDR.3 question ids are kept from using `total` (`steps.py:113`). Claim ids (TDR.2) and peer ids (TDR.4) are not checked.
- Failure scenario: the model names a claim `total`. Review passes, `validate_tables` passes, and TDR.2's first claim row is emitted as a total row, which `report_view` renders with total styling.
- Evidence: `scripts/claim_total.py` -> `issues: []`, `[('total', 'total'), ('ctx-2.c1', 'row'), ...]`, `validate_tables ok`.
- Fix direction: pass `row_kind` explicitly, as total only for the TDR.3 sum row, or add `total` to the claim_id and peer_id checks.

### S16-research-tools-A06  [low] [CONFIRMED]  Manifest path with NUL raises a raw ValueError, not IntakeError
- Location: `src/deploy_workflow/research/intake.py:190-195` (`_resolve`)
- Defect: `Path.resolve()` raises `ValueError: lstat: embedded null character` before any check, so a JSON manifest path containing `\u0000` raises a raw `ValueError` instead of the documented `IntakeError`.
- Failure scenario: `{"path": "a\u0000b.txt", ...}` makes `intake` raise `ValueError`, which none of `check_arguments`' documented error types cover.
- Evidence: `scripts/intake_paths.py <review root>/S16-research-tools/data/m` -> `'a\x00b.txt' RAISED ValueError: lstat: embedded null character in path`.
- Fix direction: refuse NUL (and other control characters) in `path` within `parse_rows`, or catch `ValueError` in `_resolve` and raise `IntakeError`.

### Out of scope (one line each, optional)
- `tests/research/test_contracts.py::test_decision_amendment_states_two_anchors` fails: `docs/decisions/0007-amendment-cp-dr-local-anchors.md` does not exist (a missing doc, not a section code defect).
- `cp1c._pack_sheet` trusts the TDR.6 head facts with no second check, so A01 and A02 both reach CP-1C. The root cause is in this section.

### Checked and sound (short bullets: what you attacked that held)
- webfetch SSRF, tested with stubs and no network: a redirect to a non-manifest host (including `169.254.169.254` and protocol-relative `//evil`), a redirect to `http`, userinfo `a@evil`, a Location containing `|` or `<<<`, more than 3 redirects, DNS rebinding on the second hop (re-resolved and refused), mixed public and private A records, `::ffff:10.x`, and decimal-IP hosts (resolved and refused). All were refused, and the connection always goes to the address that was checked (`scripts/webfetch_stubs.py`).
- `is_public` refuses NAT64 `64:ff9b::/96` and `64:ff9b:1::/48`, 6to4 `2002::`, Teredo, IPv4-compatible `::a.b.c.d`, SIIT, CGNAT, `fe80::%scope`, `fd00:ec2::254`, `192.0.0/24` and `198.18/15` (`scripts/ip_edges.py`).
- Body cap: a body exactly at the cap is accepted and one byte over is refused, never truncated. A short body against Content-Length is refused. A slow drip runs into the total deadline (checked with a fake clock). There is no Accept-Encoding header and no proxy-environment use (`http.client`).
- Refusal reasons that reach `rejected.json` or the dossier only repeat server text that passed `_URL_CHARS` or `_PLAIN_MEDIA`, so they cannot contain `|`, a line break or `<<<`.
- Intake paths: symlinks out of the folder (file and directory), absolute paths and `..` escapes are refused, a FIFO or a directory is refused as not a regular file, reads are capped at cap+1, and NUL in text is refused (`scripts/intake_paths.py`).
- `tools/source.py`: the fence regex cannot be forged, because block bodies cannot hold `<<<END>>>`/`<<<SOURCE`. An unmatched `ev-*` header fails closed. A missing retrieval time refuses the call.
- `anchors.check_anchors`: module/head hash, inputs, status, identity and CP-0 lineage binding all hold. `evidence.read_evidence`/`read_fetches` hold their shape invariants. `brief.load_locked_brief` catches a rewrite of the stored hash.
- `tables.compose`: the counts are checked against the row sums, and `ev-*` citations must be accepted items. Missing and not-applicable cells stay explicit (`∅ G#` / `not applicable`), never 0.
- `upstream.py` v1/v2 paths: grants are checked against the producer's facts, exact-tuple v2 coordinates are unique, `citation_handles` never includes quotes, bodies are capped at 8192 bytes, and the staleness recheck runs before success.
