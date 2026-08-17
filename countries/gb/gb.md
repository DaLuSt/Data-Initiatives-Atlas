---
id: GB
type: country
name: United Kingdom
alternative_names:
  - United Kingdom of Great Britain and Northern Ireland
  - UK
  - Great Britain
description: >
  Country anchor entity for the United Kingdom, the seventh national scope
  covered by the Data Initiatives Atlas and the first that is not a member
  state of the European Union. Used as the target of `country` fields for
  UK-scoped entities. Unlike the six member states, the UK is not the target
  of `applies-in` relationships from EU instruments.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "GB — United Kingdom of Great Britain and Northern Ireland (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:GB"
    publisher: "International Organization for Standardization (ISO)"
  - title: "A blueprint for modern digital government"
    url: "https://assets.publishing.service.gov.uk/media/678f6665f4ff8740d978864c/a-blueprint-for-modern-digital-government-web-optimised.pdf"
    publisher: "Department for Science, Innovation and Technology (UK)"
  - title: "Retained EU Law (Revocation and Reform) Act 2023 — Explanatory Notes"
    url: "https://www.legislation.gov.uk/ukpga/2023/28/notes/division/7/index.htm"
    publisher: "legislation.gov.uk (The National Archives)"
  - title: "Assimilated law (Retained EU law)"
    url: "https://www.gov.scot/policies/europe/retained-eu-law/"
    publisher: "Scottish Government"
---

# United Kingdom

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The United Kingdom (ISO 3166-1 alpha-2: `GB`) is the **seventh country**
populated in the Data Initiatives Atlas, after [[NL]], [[DE]], [[BE]],
[[FR]], [[ES]] and [[PL]] — and **the first that is not an EU member
state**.

## The ID is `GB`, not `UK`

`metadata/schema.json` fixes the ID scope to an **ISO 3166-1 alpha-2** code,
and the alpha-2 code for the United Kingdom is **`GB`**. `UK` is reserved
for the UK at ISO's request but is not the alpha-2 assignment, and the Atlas
follows the standard rather than common usage. Every other country anchor —
`NL`, `DE`, `BE`, `FR`, `ES`, `PL` — is an alpha-2 code, so `UK` would have
been the only ID in the Atlas that is not.

The name field still reads *United Kingdom*, and `UK` is carried in
`alternative_names`, so search finds it either way.

## Why the UK, specifically

Six batches produced six EU member states. `progress/backlog.md` had asked
for a country that would test *"the two assumptions five EU members cannot:
that **the EU layer is the right regional parent**, and that **`applies-in`
is the right way to attach a country** to it."* Poland — a 2004 accession
state — confirmed both.

**The United Kingdom breaks the first one, and the Atlas needed no change to
say so.**

## What changes, and what does not

| | Six member states | United Kingdom |
|---|---|---|
| `region:` on national entities | `EU` | **`null`** |
| `applies-in` from EU instruments | 17–18 each | **none** |
| Route to the European layer | membership | **`derived-from` and an adequacy decision** |
| Route to the international layer | via [[EU-ESS]] | **directly, via [[UN-CES]]** |

No schema, ontology, taxonomy, relationship-type, folder, validation or
generator change was needed. **The country-neutral design absorbed a
non-member state without modification** — which is a stronger result than
Poland's, because Poland was the same kind of thing as its five
predecessors and the UK is not.

`region: null` is not a new convention: every country anchor already carries
it. What is new is that the UK's *national entities* carry it too. All 97
`region: EU` entities in the Atlas belong to the six member states.

## The EU layer is still reachable — by a different edge

The Atlas connects the UK to Europe twice, and **neither link is
`applies-in`**:

1. **[[GB-UK-GDPR]] `derived-from` [[EU-GDPR]].** UK GDPR is *assimilated
   law*: the EU regulation's own text, carried into UK domestic law at the
   end of the transition period and amended since. It does not *transpose*
   the GDPR the way [[NL-UAVG]] or [[PL-ODO]] do — it **is** the GDPR text,
   domesticated and now diverging. `derived-from` ("produced by adapting
   another") already expressed this; no new relationship type was needed.
2. **[[GB-NIS-REGULATIONS]] `implements-requirement-from` [[EU-NIS]].**
   A genuine transposition, made in 2018 **while the UK was a member
   state**, and still in force. It is the only edge of its kind from a
   non-member country, and it makes the UK the second country on the
   [[EU-NIS]] row of the Compare view, next to the Netherlands.

## The Compare view will show the UK as a nearly empty column

That is correct, and it is the point. The comparison matrix reads
`applies-in` and `implements-requirement-from`; the UK has one of the latter
and none of the former. Every other country column is dense with *"applies —
none modelled"*. **The UK column is almost entirely "nothing recorded"**,
which is exactly what non-membership looks like when it is rendered
honestly.

An empty cell there is not a claim that an EU instrument does not reach the
UK. Some do, through the Trade and Cooperation Agreement, through adequacy,
or through extraterritorial scope. The Atlas has established none of that
and says so.

## What the Atlas does not record

**The EU adequacy decisions.** The European Commission renewed both UK
adequacy decisions — GDPR and Law Enforcement Directive — on **19 December
2025**, for a six-year term expiring **27 December 2031**, following the
changes made by [[GB-DUAA]]. This is the single most important connective
fact between the UK and the EU data layer, and **no entity or edge in this
batch represents it**: the decisions are Commission implementing acts that
have not been researched, and inventing an edge for them was refused. It is
the first item in `progress/backlog.md`'s UK section.

## Relationships

See `countries/gb/index.md` for the curated index of UK entities.

## Sources

Listed in frontmatter, including the ISO Online Browsing Platform entry —
the same citation [[DE]], [[BE]], [[FR]], [[ES]] and [[PL]] carry.

**No `accessed` date and no `last_verified`** — nothing about this entity
has been checked against a source.
