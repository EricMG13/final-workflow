# Adversarial review protocol (pass 1)

Your job is to break your section, not to describe it. Assume each function is wrong
until an attack fails.

## Steps
1. Read `PROTOCOL-common.md` in the review root, then `AGENTS.md`, then your
   `files.txt`. Read the entry points first: find who calls your section
   (`grep -rn "from deploy_workflow.<mod> import\|import <mod>"` across `src/` and
   `apps/`), so you attack the paths that real callers use.
2. Build a threat list for the section. For each public function or boundary, write the
   invariant it claims (from its name, docstring, callers, tests and AGENTS.md). Typical
   attack surfaces in this codebase:
   - Numbers: missing vs zero, None vs 0 vs "", negative/parenthesised values, sign of
     outflows, rounding and float vs Decimal, thousands/millions scale, unit and
     currency mixing, percent vs ratio, NaN/inf, very large values.
   - Periods: fiscal vs calendar year, quarter boundaries, 52/53-week years, LTM, date
     parsing ambiguity (dd/mm vs mm/dd), timezone, period labels that collide.
   - Identity: source references dropped or rebound to the wrong source, issuer/date
     mixing across cases, duplicate keys silently overwritten in dicts.
   - Control flow: fallbacks that invent a value, broad `except` that hides failure,
     defaults that turn "unknown" into "pass", early returns that skip checks, retries
     without a bound, resume that re-runs or skips the wrong work, non-idempotent writes,
     partial writes on crash (non-atomic file replace).
   - Text/IO: Markdown/HTML parsing of handoffs (headings, tables, pipes, escaped chars,
     unicode, CRLF), HTML/JS injection into rendered reports, path traversal in file
     names from inputs, symlinks, regex catastrophic backtracking, encoding errors.
   - Money/limits: provider budget caps, cost accounting with unknown prices, attempt
     counters, concurrency on shared state files.
   - Secrets: keys or tokens written into records, logs, exports or error messages.
3. For each attack, write a minimal script or pytest in your section folder that feeds
   the hostile input to the real code and checks the invariant with an expected value
   you derive by hand (never by calling the production calculation). Run it.
4. Keep only what you reproduced (CONFIRMED) or what you can show by exact code reading
   with a concrete trigger you could not run for a stated reason (PLAUSIBLE). Drop
   everything else.
5. Then do one self-check per finding: try to refute it. Is the input reachable from a
   real caller? Does another layer already reject it (show the line)? If refuted, drop it.
6. Return the report in the format of `PROTOCOL-common.md`, PASS: adversarial, IDs
   `<SECTION>-Ann`.

Time-box: spend effort on the highest-risk paths (calculation, boundary parsing,
budget, resume, rendering of untrusted text). You do not need to read every line of very
large files; state coverage honestly.
