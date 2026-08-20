# The re-verification pass

Every entity in this Atlas was compiled from search-engine results. The URLs
in `sources:` were confirmed by a search index to exist and **were not read**.
That is what `verification: search-only` records, and closing it is the
re-verification pass.

This page is the procedure. `tools/reverify.py` does the mechanical half of
it; the judgment half is yours.

## The state of the debt

```bash
# how many entities still owe the pass
grep -rl "verification: search-only" --include=*.md . | grep -v node_modules | wc -l

# every host the Atlas cites, ranked by how many entities it unblocks
python tools/source_hosts.py

# regenerate the committed worklist (it is a generated artefact — do not edit)
python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md
```

## Prerequisite: outbound HTTPS

The pass cannot run without it. In a network-restricted environment the proxy
answers `403` to `CONNECT` for every host, and every source comes back
`BLOCKED`:

```bash
curl -sS "$HTTPS_PROXY/__agentproxy/status"
```

`discovery/reverification-allowlist.md` is the list to request. Twenty domains
cover the bulk of it — `europa.eu` alone unblocks 80 entities.

**Never work around this by disabling TLS verification.** `tools/reverify.py`
has no such switch and `tools/test_reverify.py` asserts, against the module's
syntax tree, that none is ever added. A `primary-source` claim made over an
unverified connection is worth less than the `search-only` claim it replaced.

## Running it

```bash
# report on one entity
python tools/reverify.py --id NL-KADASTERWET

# report on a set
python tools/reverify.py --path 'legislation/nl-*.md'

# work the backlog, most-recently-added first is not the order — it is by path
python tools/reverify.py --search-only --limit 20

# see exactly what would be checked, without fetching
python tools/reverify.py --id EU-GDPR --offline --verbose

# machine-readable, for scripting a sweep
python tools/reverify.py --search-only --json > /tmp/pass.json
```

### What it checks

The tool extracts the entity's **checkable claims** and looks for each one in
the retrieved page text. Two kinds, and the difference matters when you read a
report:

- **Identifiers** — `BWBR0004541`, `BOE-A-2021-17910`, `CETS No. 223`,
  `Directive (EU) 2019/1024`, `S.I. No. 376/2021` and the rest. Absence is a
  **real signal**: that string is the one thing the page is certain to contain
  if the citation is right.
- **Names** — the entity's `name` and `alternative_names`, where longer than
  eight characters. Absence is **weak** evidence: pages are multilingual,
  titles get abbreviated, and an official page often never spells out its own
  long-form title.

This exists because of a specific near-miss. A search returned **BWBR0007376**
for the Kadasterwet; that identifier is the **Archiefwet 1995**. Fetching it
succeeds — a wrong identifier in this field does not 404, it silently returns
another real act. Only checking for the identifier the entity *claims* catches
that class of error.

### The current baseline

A full sweep on 2026-08-19, for reference when you run your own:

```
python tools/reverify.py --search-only --timeout 8
```

| | |
|---|---|
| Entities swept | **443** |
| Sources attempted | **1,500** |
| Retrieved | **0** |
| Refused by egress policy | **1,494** (99.6%) |
| Other | **6** |

Roughly six minutes. Not one page was read.

The six are worth knowing, because they are three different things and only
one of them is fixable by an allowlist:

- **5 × `github.com`** — refused by the *GitHub* proxy, which scopes a session
  to its configured repositories. A different policy from the egress
  allowlist, and it will not lift by adding a host. The tool surfaces the
  gateway's own message so this is visible rather than inferred.
- **1 × `catedrapsyd.unizar.es`** (cited on `ES-LO-2-2002`) — did not resolve
  at all, while every other host tested resolved to the interceptor. That
  points at a genuinely dead host rather than a blocked one. Recorded in
  `discovery/unresolved.md`.
- **1 entity with no sources** — `DOMAIN-NATIONAL-SECURITY`, and correctly so:
  domains are classification nodes and carry no factual claims.

Six entities have **no checkable claims** — `RO`, `UA`, `FR-ETALAB`,
`NL-LOGIUS`, `NL-NICTIZ`, `NO-ALTINN`. Short names, no legal identifier. The
tool says so rather than passing them silently: an entity it cannot check is
not an entity it has checked.

### Verdicts

| Verdict | Meaning |
|---|---|
| `BLOCKED` | The egress policy refused every source. Nothing to judge; fix the allowlist. Includes 403s carrying the proxy's `x-deny-reason` header, which arrive over plain `http://` as ordinary responses rather than as failed CONNECTs. |
| `UNREACHABLE` | Hosts answered, but no source came back. Dead links, or a mix of blocked and dead. |
| `NEEDS REVIEW` | Something came back, and something needs looking at — an unretrieved source, or a claim nobody corroborated. |
| `CORROBORATED` | Every source retrieved, and every claim appears on one of them. |
| `NO SOURCES` | The entity cites nothing. |

Exit code is `0` from `NEEDS REVIEW` upwards, `1` for `BLOCKED` and
`UNREACHABLE`.

**`CORROBORATED` is not "verified".** It means the identifiers are on the
pages. It says nothing about whether the entity's description, dates,
relationships or evidence strings are right — which is the part that actually
matters and the part only a reader can do.

## A link check is not a content check

Worth stating plainly, because the two get conflated and the difference is the
whole point of the `verification` field.

| | What it establishes | What it does not |
|---|---|---|
| **Reachability check** | the host resolves | anything about the page, let alone the entity |
| **Link check** | the citation points somewhere real | anything about the entity's claims |
| **Content check** | the page supports the entity's dates, identifiers, relationships and evidence | — |

Only the third is `verification: primary-source`.

The first is the only one that runs **without egress** — a DNS resolution of
every cited host — and it is worth running precisely because it is cheap. It
is what would have caught `gob.es` before a human had to: that domain has no
address at all, while every Spanish host the Atlas actually cites resolves
fine. A sweep on 2026-08-20 resolved all 52 institutional domains. On **2026-08-20** the
repository owner manually opened the nineteen highest-value domains in
`discovery/reverification-allowlist.md` — the Atlas's first primary-source
signal of any kind. Eighteen resolved to what the Atlas claims; `gob.es` did
not, because Spain's government namespace has **no apex site**. That was a
defect in the report, which listed an allowlist pattern where a reader would
try a URL, and not in any citation. **No entity's `verification` changed**,
and none should have: a link check upgrades what is known about the
*citations*, not about the *entities*.

`tools/reverify.py` sits between the two. Its identifier matching is stronger
than a link check — it confirms the page contains the citation the entity
claims — and weaker than a content check, which is why its best verdict is
called `CORROBORATED` and not `VERIFIED`.

## Completing an entity

Read the pages. Then, for each field the sources support: confirm it, or
correct it. Then stamp it:

```bash
python tools/reverify.py --id NL-KADASTERWET --write
```

`--write` takes exactly one `--id`, refuses on `BLOCKED` and `UNREACHABLE`,
and refuses when a claim went uncorroborated unless you add `--force` — which
is the right call when a page abbreviates a title, and the wrong call when the
identifier is missing.

It writes three things:

- `accessed: "<today>"` on **the sources that actually came back**, and only
  those. A source that did not respond was not accessed.
- `last_verified: "<today>"`
- `verification: primary-source`

It does **not** touch `confidence`. Raising it is a judgment about how well
the sources support the entity, and `validate_frontmatter.py` rejects
`confidence: high` on anything still `search-only` — so this is the gate that
lifts, deliberately by hand.

It does not touch the body either. The tool warns when the **"Sourcing
caveat" blockquote** is still there; remove it yourself, along with any
`NOT READ — search-only` suffix in the `evidence:` strings you just confirmed.

Finally, close or annotate the entity's row in `discovery/unresolved.md`.

## Where to start

`discovery/unresolved.md` flags the **seven Dutch register statutes** as high
priority — `NL-WET-BAG`, `NL-WET-BGT`, `NL-WET-BRO`, `NL-WET-WOZ`,
`NL-HANDELSREGISTERWET`, `NL-WEGENVERKEERSWET-1994` and `NL-KADASTERWET`.
They are keyed entirely on BWBR identifiers, so a wrong one resolves to a real
but unrelated act rather than to nothing. `tools/test_reverify.py` asserts
that the tool can extract a BWBR identifier from all seven.

```bash
python tools/reverify.py \
  --id NL-WET-BAG --id NL-WET-BGT --id NL-WET-BRO --id NL-WET-WOZ \
  --id NL-HANDELSREGISTERWET --id NL-WEGENVERKEERSWET-1994 --id NL-KADASTERWET
```

After them, `discovery/reverification-allowlist.md`'s ranking is the order
that clears the most entities per host unblocked.
