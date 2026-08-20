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

### Verdicts

| Verdict | Meaning |
|---|---|
| `BLOCKED` | The egress policy refused every source. Nothing to judge; fix the allowlist. |
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
