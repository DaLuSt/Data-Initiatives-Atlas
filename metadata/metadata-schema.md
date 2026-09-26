# Metadata Schema (YAML Frontmatter)

Every substantive entity file starts with YAML frontmatter. This document is
the field-by-field reference; `metadata/schema.json` is the same schema in
machine-readable form, used by `validation/validate_frontmatter.py`.

Do not invent information to fill a field. Omit optional fields, or use
`null` / `unknown` where the schema calls for an explicit value.

## Full field list

```yaml
---
id:                    # required — see metadata/ontology.md §2
type:                  # required — controlled vocabulary, ontology.md §1
name:                  # required — official or commonly recognised name
alternative_names:     # optional — list of known aliases/abbreviations
description:           # required — short factual description, no interpretation

level:                 # required — international | regional | national | subnational | sectoral | local
country:               # required — ISO 3166-1 alpha-2, or null
region:                # optional — e.g. EU, UN; not a substitute for country

status:                # required — controlled vocabulary, see below
confidence:            # required — high | medium | low (confidence in the Atlas's representation)
coverage:              # required — low | medium | high (how thoroughly researched)
verification:          # optional — primary-source | search-only | unverified

start_date:            # optional — ISO date
end_date:              # optional — ISO date
last_verified:         # required once an entity leaves draft status — ISO date
previous_version:      # optional — entity id
successor:             # optional — entity id

organisation_role:     # optional, type: organisation only — executive | consultative | regulatory | standards-body | advisory (ontology.md §1.1)

domains:               # optional — list of domain entity ids
organisations:         # optional — list of organisation entity ids (lightweight ref, §relationship-types.md)
related_entities:      # optional — list of entity ids (lightweight ref)
relationships:         # optional — list of provenanced relationship objects, see relationship-types.md

sources:               # required for any entity making factual claims
  - title:
    url:
    publisher:
    accessed:
---
```

## Field notes

- **id**: stable, unique, never reused. Format in `ontology.md` §2.
- **type**: one value from the entity type table in `ontology.md` §1.
- **name**: the name used in prose and in wikilinks' display text.
- **alternative_names**: helps discovery/deduplication; also searched by
  contributors before creating a new entity (README §"Do Not Overwrite").
- **description**: factual only. Interpretation belongs in `relationships:`
  entries with `source: interpretation`, or in a clearly labelled
  "Atlas interpretation" prose subsection, never in `description`.
- **level / country / region**: see `ontology.md` §4.
- **status**: one of `proposed`, `planned`, `adopted`, `active`,
  `implemented`, `superseded`, `replaced`, `completed`, `archived`,
  `unknown`. Never infer `active` purely from "the website still resolves" —
  require an actual source dated recently enough to support it, otherwise use
  `unknown`. Use `adopted` for an instrument that has been formally adopted
  but has **not entered into force**; it is a real instrument that binds
  nobody yet, which neither `proposed` nor `active` can say.
- **confidence**: how much the Atlas trusts its *own representation* of the
  entity — not the entity's real-world status. `status: unknown` +
  `confidence: low` is a normal, honest combination.
- **coverage**: distinguishes "this area has no relevant initiatives" (would
  be represented by simply not creating entities, with coverage on the
  parent domain/country marked `high`) from "this area has not yet been
  researched" (`coverage: low` on whatever entity represents that area, plus
  a `discovery/research-queue.md` entry).
- **verification**: how the entity's sources were actually consulted.
  - `primary-source` — the cited sources were retrieved and read.
  - `search-only` — the entity was compiled from search-engine results.
    The cited URLs were confirmed by a search index to exist, but **were
    not read**. Such entities carry no `accessed:` dates (nothing was
    accessed) and must not claim `confidence: high` — validation enforces
    this. They need a re-verification pass against the primary sources.
  - `unverified` — asserted without either; should be rare and paired with
    a `discovery/unresolved.md` entry.

  Omitting the field is treated as "not stated"; prefer stating it
  explicitly on any entity added under constrained sourcing conditions, so
  a later pass can find them with a single grep.
- **start_date / end_date**: full ISO dates only. **When only the year (or
  year and month) is known, use `null` and explain the imprecision in
  prose** — never a `YYYY-01-01`-style placeholder implying a precision the
  sources don't support. Decided in practice on [[NL-RORA]] (2026-08-27)
  and formalised here 2026-09-20, closing `discovery/unresolved.md` item
  #14. This repository does not have a separate `date_precision` field;
  `null` plus a prose note (e.g. "founded in 1996, exact date not stated by
  any source read") carries the same information without a schema change.
  Existing entities still carrying a `YYYY-01-01` placeholder from before
  this convention was written down (e.g. [[NL-PDOK]]) are not touched
  retroactively by this decision alone — fix them at reverification.
- **last_verified**: the date a human/agent last checked the sources still
  support the current field values. Required once an entity is anything
  other than a stub.
- **previous_version / successor**: chain superseded entities together
  without ever deleting or reusing an ID.
- **organisation_role**: only valid on `type: organisation`; distinguishes
  bodies that deliberate/select/coordinate (`consultative`, `advisory`) or
  set/mirror standards (`regulatory`, `standards-body`) from bodies that
  execute/publish/operate directly (`executive`). Optional and additive —
  omit it rather than guess; see `ontology.md` §1.1.
- **domains / organisations / related_entities / relationships**: see
  `metadata/relationship-types.md`.
- **sources**: each entry needs `title`, `url`, `publisher`. `accessed` (ISO
  date) is required for anything used to support a `status` or factual
  claim. Never invent a URL — if no authoritative source exists yet, leave
  `sources:` absent/empty and record the gap in `discovery/unresolved.md`
  rather than fabricating one.

## Minimal valid stub

An entity may be committed as an intentionally shallow stub (e.g. to anchor
a relationship target discovered mid-batch) provided it is honest about it:

```yaml
---
id: NL-EXAMPLE-STUB
type: initiative
name: Example Initiative
description: "Placeholder — identified via [source] but not yet researched in depth."
level: national
country: NL
status: unknown
confidence: low
coverage: low
sources: []
---
```

Such stubs should also get a `discovery/research-queue.md` entry.
