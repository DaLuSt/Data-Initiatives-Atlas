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

## The confirmed domains

On **2026-08-21** the repository owner confirmed five domains at the **content**
tier — the pages were read and the information on them confirmed correct:

| Domain | URLs | Entities citing it |
|---|---|---|
| `europa.eu` | 231 | 144 |
| `iso.org` | 67 | 64 |
| `coe.int` | 52 | 42 |
| `bund.de` | 41 | 23 |
| `legifrance.gouv.fr` | 5 | 5 |

This is the first content-tier confirmation the Atlas has had, and the only
thing that licenses `verification: primary-source`.

### The rule it is applied under: all sources, or none

**An entity moves to `primary-source` only when *every* source it cites is on
a confirmed domain.** Partial coverage leaves it `search-only`.

That is deliberately strict, and the reason is mechanical: an entity's claims
are distributed across its sources, and the Atlas does not record which source
supports which claim. If four of five sources are confirmed, the fifth may be
the one carrying the date, the identifier or the relationship — so the entity
as a whole is not confirmed. This is the same rule `tools/reverify.py` already
implements as `set_verification=False` for partial retrieval.

Applied on 2026-08-21:

| | Entities |
|---|---|
| Fully covered → moved to `primary-source` | **41** |
| Partially covered → unchanged, still `search-only` | 161 |
| Not covered | 291 |
| No sources (domains and anchors, exempt) | 8 |

### Two results worth recording

**`legifrance.gouv.fr` yielded nothing.** Five entities cite it and all five
also cite something unconfirmed, so none qualified. A confirmation is not
required to move anything; the partial-coverage rule is what decides.

**`europa.eu` did most of the work.** Thirty-eight of the 41 are EU-scoped, and
that is a fact about how the Atlas was built rather than about the Union:
EU-level entities tend to cite one publisher, because EUR-Lex and the
Commission's own domains carry the whole instrument. A national entity
typically cites a statute database, a ministry and a commentary — three
domains, three confirmations needed.

**So the sweep's yield is front-loaded.** The next four domains by URL count
(`wikipedia.org`, `digitaleoverheid.nl`, `gov.pl`, `gouv.fr`) would convert far
fewer entities each, because the entities citing them cite other things too.
`discovery/reverification-allowlist.md` ranks by URL count, which overstates
how much each remaining domain would unlock.

## A machine-corroborated pass

On **2026-08-21**, with the egress policy actually open, `tools/reverify.py`
fetched and read pages for the first time — a different and stronger thing
than the domain-level confirmation above, which was a human opening
nineteen pages by hand. This is the tool doing its own fetch, its own
identifier match, and a human reading the retrieved text before stamping
`--write`.

**Confirming egress is open is not the same as confirming a page will load.**
`curl` and `tools/reverify.py`'s own `urllib` fetch both complete the TLS
handshake to `eur-lex.europa.eu`, `www.iso.org`, `www.coe.int` and
`unece.org` — the CONNECT succeeds, the connection is real — but each of
those hosts answers with a bot-defense challenge page (AWS WAF on EUR-Lex,
Cloudflare on the other three) instead of content. A plain HTTP client gets
a `202` or `403` carrying no statute or standard text, whatever the
`User-Agent` header says. A headless Chromium routed through this session's
proxy cannot reach any host at all — the proxy integration issue is
independent of the WAF question. So the twenty-five entities citing only
those four hosts are not verifiable from inside this environment by any
method available to it, and remain `search-only` for that reason rather
than for lack of trying. This is a narrower and more precise finding than
"the pass cannot run without egress" above: egress can be open and specific
hosts can still be closed.

Every other host this batch touched — `europa.eu` subdomains other than
`eur-lex` (`ec.europa.eu`, `digital-strategy.ec.europa.eu`,
`edpb.europa.eu`, `enlargement.ec.europa.eu`, `interoperable-europe.ec.europa.eu`),
`wikipedia.org`, `wetten.overheid.nl`, `gov.uk`, `gob.pt`, `gv.at`, `.dk`,
`.fi`, `.ie`, `.it`, `.se` government domains and `gdprhub.eu` — returned
real page text to a plain fetch.

### Batch 1 result

| | Entities |
|---|---|
| Moved to `verification: primary-source` | **21** |
| Corrections found and fixed in the process | **2** substantive, several typos |
| Could not verify — sources on a bot-walled host | 2 attempted, not moved (`LU-STATEC`, `PT-INE`; see below) |

The seven Dutch base-registration statutes flagged high priority in "Where
to start" below are now all verified: `NL-WET-BAG`, `NL-WET-BGT`,
`NL-WET-BRO`, `NL-WET-WOZ`, `NL-HANDELSREGISTERWET`,
`NL-WEGENVERKEERSWET-1994` and `NL-KADASTERWET`. None of the seven BWBR
identifiers resolved to the wrong act — the specific failure mode this tool
was built to catch did not recur, though a different error did:

- **`NL-WET-BGT`'s staged commencement date was wrong.** The entity recorded
  articles 29 and 30 as taking effect 30 April 2018. `wetten.overheid.nl`'s
  own commencement history gives 1 July 2018; 30 April 2018 is when the
  commencement decree (Stb. 2018, 122) was *published*, not when the
  articles took effect. Confirmed independently on the Eerste Kamer's own
  dossier, which titles the same document "publicatie inwerkingtreding
  artikelen 29 en 30" — a publication, not a commencement.
- **`NL-KADASTERWET`'s alternative name was unattested.** "Kadasterwet 1989"
  was listed in `alternative_names`; the statute's own metadata records
  `Niet officiële titel: Geen` — no informal title. Removed rather than kept
  on the assumption that no source read it either.

Several diacritic/umlaut typos were also caught by the identifier-and-name
check itself: `Datenschutzbehorde` (missing the umlaut Austria's own DSB
site uses), `Bundesanstalt Statistik Osterreich` (missing umlaut),
`Dataombudsmannens byra` (missing the Swedish ring accent). Each was a case
where `alternative_names` and the page text disagreed by exactly one
diacritic — invisible on a skim, caught because the check is a literal
string match.

**Two entities were attempted and not moved.** `LU-STATEC`'s `name` field
carries an Atlas-added disambiguator, `"... (Luxembourg)"`, to distinguish it
from France's identically-named INSEE (see the entity body); no external
source will ever write that suffix, so the name claim can never corroborate
by exact-string match, and the entity needs a different fix (moving the
disambiguator out of `name`) rather than another source. `PT-INE`'s only
national source, `ine.pt`, returns `HTTP 403` specifically to
`tools/reverify.py`'s declared `User-Agent`, consistently across repeated
attempts, while occasionally serving a browser-identified `curl` request —
a site-level block on the tool's identity, not a network flake.

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

**The seven Dutch register statutes are done** — `NL-WET-BAG`, `NL-WET-BGT`,
`NL-WET-BRO`, `NL-WET-WOZ`, `NL-HANDELSREGISTERWET`,
`NL-WEGENVERKEERSWET-1994` and `NL-KADASTERWET` all carry
`verification: primary-source` as of 2026-08-21; see "A machine-corroborated
pass" above. They were keyed entirely on BWBR identifiers, so a wrong one
would have resolved to a real but unrelated act rather than to nothing;
`tools/test_reverify.py` still asserts that the tool can extract a BWBR
identifier from all seven, as a regression guard.

From here, skip any entity whose sources are **only** `eur-lex.europa.eu`,
`www.iso.org`, `www.coe.int` or `unece.org` — those hosts return a
bot-defense challenge page to every fetch attempt in this environment, egress
policy notwithstanding, so time spent on them will not convert. Otherwise,
`discovery/reverification-allowlist.md`'s ranking is the order that clears
the most entities per host unblocked. Batch 1 worked the EU-scoped
organisation cluster (national statistics institutes citing `ec.europa.eu`,
national DPAs citing `edpb.europa.eu`) as a dense, well-structured next
target; a similar cluster likely exists for the next batch to find via the
allowlist.
