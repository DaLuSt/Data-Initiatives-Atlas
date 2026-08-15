# Controlled Vocabularies

Single source of truth for every closed value list used in frontmatter. The
machine-readable copy validation actually runs against is
`metadata/schema.json` — if the two ever disagree, `schema.json` is correct
and this file should be fixed to match, since it's what the tooling reads.

## `type`

`initiative`, `organisation`, `country`, `region`, `policy`, `law`,
`regulation`, `directive`, `strategy`, `standard`, `framework`, `programme`,
`data-space`, `platform`, `technology`, `domain`, `publication`

Definitions: `metadata/ontology.md` §1. Folder mapping: `metadata/ontology.md` §3.

## `level`

`international`, `regional`, `national`, `sectoral`, `local`

## `status`

`proposed`, `planned`, `active`, `implemented`, `superseded`, `replaced`,
`completed`, `archived`, `unknown`

## `confidence` / relationship `confidence`

`high`, `medium`, `low` — see `metadata/metadata-schema.md` for the
distinction between this and `status`.

## `coverage`

`low`, `medium`, `high`

## `verification`

`primary-source`, `search-only`, `unverified` — how the entity's sources
were actually consulted. See `metadata/metadata-schema.md`. Validation
rejects `confidence: high` on any entity whose `verification` is
`search-only` or `unverified`.

## `country`

ISO 3166-1 alpha-2 codes only (e.g. `NL`, `DE`, `BE`, `FR`), or `null`.
Validation checks the value is a syntactically plausible 2-letter code; it
does not maintain its own copy of the full ISO list.

## `region`

Free-form but should reuse an existing anchor scope (`EU`) wherever
possible; introduce a new region code only when a `region`-type anchor
entity is created for it (`metadata/ontology.md` §3.1).

## Relationship `type`

See `metadata/relationship-types.md` §2.1 for the full list and definitions:
`related-to`, `influences`, `implements`, `implemented-by`, `depends-on`,
`derived-from`, `based-on`, `references`, `supersedes`, `replaces`,
`proposes-to-supersede`, `part-of`, `governed-by`, `applies-to`,
`applies-in`, `produces`, `maintained-by`, `owned-by`, `participates-in`,
`aligned-with`, `implements-requirement-from`.

## Relationship `source`

`fact`, `interpretation` — see `metadata/relationship-types.md` §3.
