SECTION: S16-research-tools   PASS: code-review
COVERAGE: 15/15 read fully by the code-review skill fork; I re-read 10 fully myself to verify (research/peers.py, webfetch.py, intake.py, review.py, tables.py, steps.py, anchors.py, dossier.py, evidence.py, tools/source.py) / research/brief.py, research/contracts.py, tools/upstream.py and the two __init__.py were read only by the fork / none unread

Independence note: the code-review skill ran as a forked reviewer. Although the constraint line was written immediately before the call, the fork read docs/review-handoff/S16-research-tools/adversarial.md. It said its findings C01, C02, C04, C07 and C09 below (its own numbers 1, 2, 3, 6 and 5) match earlier adversarial IDs A01, A02, A03, A06 and A05, and that its 'NUL path' finding (C08 here) matches A04. It called C03, C05, C06 and C10 new. I did not open adversarial.md, any repro file or the section's scripts/ folder myself. I re-verified every finding below with my own scripts in cr/.

### S16-research-tools-C01  [high] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/peers.py:295` (_amount_cell), with the only quote check at `peers.py:207` (_figure_issues -> citation_issues)
- Defect: the TDR.6 amount is parsed from `citation.quote`, and the only check on the quote is that it is a contiguous substring of the cited span. Part of a number, or a run of digits from a date, passes as the located figure.
- Failure scenario: span ev-1 line:11 is 'Alder Ridge Holdings revenue for the twelve months to 2025-12-31: 200.0'. The model quotes '20', '0.0' or '00'. peer_issues returns (). compose_peer_tables writes TDR.6.p01.revenue.amount = 20 (or 0.0, a known zero in place of 200), status known, value_class source. peer_sheet then hands it to CP-1C's peer benchmark. A span such as '(12.3)' quoted as '12.3' loses its sign the same way.
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:.:tests/research .venv/bin/python <section>/cr/c_peer_quote.py` gives `quote='20': issues=() -> amount=20 status=known` and `quote='0.0': issues=() -> amount=0.0 status=known`.
- Fix direction: require the quote to be a whole numeric token in the span (not bordered by a digit, '.', ',', '-' or '('), or locate the token in the span and refuse any quote that is not one.

### S16-research-tools-C02  [high] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/peers.py:298-308` (_amount_cell), `peers.py:90-96` (LocatedFigure), `peers.py:187-208` (_figure_issues)
- Defect: the model declares unit (scale), currency and period_end as free fields, and nothing checks them against the cited span. Python also always labels the period 'Twelve months to <period_end>', and LocatedFigure has no field for the period's length.
- Failure scenario: the span reads 'three months to 2025-12-31, EUR thousands: 200.0'. The model submits unit=millions and currency=USD. No issue is raised, and the fact becomes 200.0 MILLIONS USD, 'Twelve months to 2025-12-31'. peer_sheet admits it because it is in the run's currency and in millions. The reverse also passes: unit=thousands and currency=EUR over a span that says USD millions composes as 200.0 THOUSANDS EUR with no issue. CP-1C's peer figures can then be wrong by a factor of 1000, in the wrong currency, or a quarter treated as a full year.
- Evidence: c_peer_quote.py gives `unit=thousands currency=EUR: issues= () -> 200.0 THOUSANDS EUR Twelve months to 2025-12-31` (the cited span says nothing about thousands or EUR).
- Fix direction: take or check the scale, currency and period length from the cited span (or from a quoted basis line), and refuse a figure whose declared basis the span does not state, instead of trusting model fields.

### S16-research-tools-C03  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/peers.py:187-208` (_figure_issues), with the effect at `peers.py:428-434` (_cell_text) and `peers.py:449-475` (_figures)
- Defect: review never puts a figure's free-text `currency` through the fence or the table-cell rule. peer_sheet later applies those rules and turns one bad currency cell into PackUnusable for the whole pack, after the head has already settled, so the model gets no repair step.
- Failure scenario: one TDR.6 figure has currency 'USD|x' or 'USD\n'. peer_issues returns (), the head settles, and peer_sheet returns PackUnusable('TDR.6 p01.revenue currency: holds a line break or a pipe character'). CP-1C's _pack_sheet raises PeerPackRefused, and every peer is lost, not just the bad figure. A near-miss such as 'USD ' is not flagged either. That peer is silently dropped as "currency USD  is not the run's USD".
- Evidence: `PYTHONPATH=src:.:tests:tests/research .venv/bin/python <section>/cr/c_peer_currency.py` gives `currency='USD|x' review issues=()` and then `-> PackUnusable: TDR.6 p01.revenue currency: holds a line break or a pipe character`.
- Fix direction: in _figure_issues, run the same _unsafe check (fence plus cell rule) over currency, and flag a currency that is not a plain ISO-4217-shaped code, so the model repairs it during review.

### S16-research-tools-C04  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/webfetch.py:165-168` (resolve_public); webfetch.py:141 (check_url) accepts the host
- Defect: resolve_public catches only OSError. socket.getaddrinfo raises UnicodeEncodeError (a ValueError) for a host the IDNA codec refuses, so the error escapes fetch() instead of becoming a FetchRefusal on the record.
- Failure scenario: a manifest url row with a typo, 'https://www..example.com/a' (or a label over 63 characters), passes parse_rows/check_url. fetch then raises a raw UnicodeEncodeError through intake and run_inputs._research_staging, and check_arguments aborts. No rejected.json entry is written and the remaining rows are never assessed. This contradicts fetch's own contract that refusals are recorded.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/cr/c_webfetch.py` gives `check_url accepts: www..example.com` and then `fetch RAISED UnicodeEncodeError ... label empty`. The real `system_resolver('www..example.com')` raises `UnicodeEncodeError` during local encoding, before any lookup.
- Fix direction: catch UnicodeError (or ValueError) in resolve_public as a 'did not resolve' FetchRefusal, or reject hosts in _shape that fail `host.encode('idna')`.

### S16-research-tools-C05  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/webfetch.py:317-335` (locate_published), used at `src/deploy_workflow/research/intake.py:354-363` (_assess_web)
- Defect: when a Last-Modified header parses, it alone becomes the 'located publication date' and the body's 'Published:' line is never read. The cutoff check, which is meant only to refuse, therefore sees just one of the two dates.
- Failure scenario: (a) Cutoff leak: a stale Last-Modified of 2025-01-01 on an article whose body says 'Published: 2025-09-01' is accepted into a run with cutoff 2025-06-30. (b) Over-refusal: a page dynamically served with Last-Modified set to today is refused in every historical run, even though its body says 'Published: 2025-03-01'.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/cr/c_located_date.py` (fake connector) gives `located=2025-01-01 via header:last-modified; accepted=['ev-1']` for (a) and `refused=['evidence item L1 has a located publication date 2026-11-06 after the cutoff 2025-06-30']` for (b).
- Fix direction: locate both dates and refuse when either is after the cutoff, or prefer the body's publication line over the modification header.

### S16-research-tools-C06  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/intake.py:428-440` (intake), with the effect in `src/deploy_workflow/research/review.py:175-189` (_family_issues)
- Defect: intake never removes duplicates. Two rows naming the same file (or identical bytes) become two accepted items with the same sha256, and the independence rule compares only family labels.
- Failure scenario: rows {path a.txt, family 'Wire A'} and {path a.txt, family 'Wire B'} become ev-1 and ev-2 with an identical hash. A claim with independent_items [ev-1, ev-2] passes review as corroborated by two independent sources.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/cr/c_intake_review.py <section>/cr/work` gives `duplicate file: [('ev-1','Wire A','cdbacfec60cf'), ('ev-2','Wire B','cdbacfec60cf')]` and `family issues for [ev-1, ev-2]: []`.
- Fix direction: refuse (or merge) a second accepted item whose sha256 equals an earlier one, or treat equal-hash items as one family in _family_issues.

### S16-research-tools-C07  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/review.py:182` (_family_issues)
- Defect: the 'two items of one family never count as independent' rule compares the raw family strings, so labels that differ only in case or surrounding whitespace count as different families.
- Failure scenario: the manifest gives family 'Reuters' for ev-1 and 'reuters' or 'Reuters ' for ev-2. A claim listing both as independent passes as independently corroborated in TDR.2 and downstream.
- Evidence: c_intake_review.py gives `families 'Reuters'/'Reuters': [ReviewIssue(... share family Reuters)]` but `'Reuters'/'reuters': []` and `'Reuters'/'Reuters ': []`.
- Fix direction: compare `family.strip().casefold()`, or normalise the family once at intake (parse_rows).

### S16-research-tools-C08  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/intake.py:190-195` (_resolve)
- Defect: Path.resolve() runs before any check, so a manifest path containing NUL raises a raw ValueError instead of the documented IntakeError.
- Failure scenario: a JSON manifest row {"path": "a\u0000b.txt", ...} passes parse_rows, and intake raises `ValueError: lstat: embedded null character in path`. check_arguments documents only RunInputError/ResearchError kinds, so this surfaces as an unclassified crash instead of a manifest error.
- Evidence: c_intake_review.py gives `NUL path: RAW ValueError lstat: embedded null character in path`.
- Fix direction: in parse_rows or _resolve, refuse a path containing '\x00' with IntakeError, or wrap the resolve in `except ValueError` and re-raise it as IntakeError.

### S16-research-tools-C09  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/research/tables.py:165` (_Table.add); only TDR.3 question ids are kept from using 'total' (`steps.py:113`, `tables.py:461`)
- Defect: every table marks a row whose id is 'total' as row_kind='total', but claim ids (TDR.2) and peer ids (TDR.4-6) are never kept from being 'total'.
- Failure scenario: the model names a peer_id or claim_id 'total'. peer_issues and research_issues pass, and that ordinary candidate or claim row is written with row_kind 'total', which report_view styles as a summary/total row in the rendered report.
- Evidence: `PYTHONPATH=src:.:tests/research .venv/bin/python <section>/cr/c_port_total.py` gives `peer_id total issues: ()` and `total-styled row: TDR.4 total`.
- Fix direction: set row_kind='total' only on TDR.3's own sum row (pass it explicitly from _tdr3), or refuse 'total' as a claim or peer id during review.

### S16-research-tools-C10  [low] [CONFIRMED]  security
- Location: `src/deploy_workflow/research/webfetch.py:390` (_next_hop)
- Defect: a redirect is checked only for whether its host is named in the manifest. Its port is never checked, so a manifest host can send the fetch to any port on itself.
- Failure scenario: https://example.com/a answers 302 with Location https://example.com:8443/admin. The fetcher connects to port 8443, a port the user never named, and takes that body in as evidence. The address-is-public check still applies, so the reach is limited to public addresses of hosts the manifest names.
- Evidence: c_port_total.py (fake connector) gives `connections: [('example.com', 443), ('example.com', 8443)] reason: None body: b'internal admin page'`.
- Fix direction: allow a redirect only to a (host, port) pair the manifest named (443 by default).

### Out of scope (one line each, optional)
- `src/deploy_workflow/owners/cpdr.py:267` (_research_texts) leaves TDR.6 figure texts (currency, and the quote cell) out of the step's fence and cell checks. This is the step-side half of C03.

### Checked and sound (short bullets: what you attacked that held)
- webfetch: the connection is pinned to the checked address (no second lookup), IPv4-mapped IPv6 is unwrapped before the public check, the body is bounded at cap+1 and refused rather than truncated, a Content-Length mismatch is refused, redirects are limited to 3, the total deadline is enforced per socket operation, and no Accept-Encoding is sent.
- intake: a path that escapes via '..' or a symlink is refused (resolve plus is_relative_to), the file is opened with O_NOFOLLOW/O_NONBLOCK and fstat checks for a regular file, family and locator are refused if they contain a pipe, a line break or '<<<', the fence check runs before any fetch, and nothing is copied before every row is assessed.
- review/peers: the peer_id length bound keeps fact ids within 160 characters, duplicate TDR.4/5/6 rows are flagged, period_end must be a real calendar date, a period after the cutoff composes as a missing gap (not zero), and a typed amount field is a shape refusal (strict contracts).
- tables: the count totals are checked against the sum of the question rows, an ev-* citation that is not accepted raises (a case-folded prefix check), and missing and not_applicable stay distinct.
- tools/source.py: an ev-* block with no recorded retrieval time fails closed, and an unrecognised research header left outside the fence raises.
- evidence.py: record readers refuse a wrong shape, duplicate ids and inconsistent fetch records, and rerun retrieval times are kept only after cpdr.check_records authenticates them.
