---
id: GB
type: country
name: United Kingdom
alternative_names:
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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - INTL-COE
relationships:
  - type: part-of
    target: INTL-COE
    source: fact
    evidence: "NOT independently re-confirmed 2026-08-22: coe.int returns a bot-defense challenge (403, Cloudflare 'Attention Required!') and was not read. The claim (the UK is one of the 46 member states of the Council of Europe, an intergovernmental organisation separate from the European Union) is retained rather than removed, since a bot-wall is not evidence it is wrong. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "A blueprint for modern digital government"
    url: "https://assets.publishing.service.gov.uk/media/678f6665f4ff8740d978864c/a-blueprint-for-modern-digital-government-web-optimised.pdf"
    publisher: "Department for Science, Innovation and Technology (UK)"
    accessed: "2026-08-22"
  - title: "Retained EU Law (Revocation and Reform) Act 2023 — Explanatory Notes"
    url: "https://www.legislation.gov.uk/ukpga/2023/28/notes/division/7/index.htm"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-08-22"
  - title: "Assimilated law (Retained EU law)"
    url: "https://www.gov.scot/policies/europe/retained-eu-law/"
    publisher: "Scottish Government"
    accessed: "2026-08-22"
---

# United Kingdom

> **Verified 2026-08-22.** The Retained EU Law (Revocation and Reform) Act
> 2023 explanatory notes and gov.scot's assimilated-law page were read
> directly and confirm "United Kingdom" and "Great Britain" verbatim. The
> unattested alternative name "United Kingdom of Great Britain and
> Northern Ireland" has been removed — it appeared only on the ISO Online
> Browsing Platform entry, which is bot-walled (403) and was never read.
> The Council of Europe membership claim below could not be
> independently re-confirmed this pass — `coe.int` is also bot-walled —
> and is retained rather than removed; see that relationship's evidence.

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
| Route to the international layer | via [[EU-ESS]] | **directly, via [[UN-CES]] and [[UN-GGIM]]** |

No schema, ontology, taxonomy, relationship-type, folder, validation or
generator change was needed. **The country-neutral design absorbed a
non-member state without modification** — which is a stronger result than
Poland's, because Poland was the same kind of thing as its five
predecessors and the UK is not.

`region: null` is not a new convention: every country anchor already carries
it. What is new is that the UK's *national entities* carry it too. All 97
`region: EU` entities in the Atlas belong to the six member states.

## The EU layer is still reachable — by three edges, none of them membership

**No *EU instrument* carries `applies-in` to [[GB]]**, and none ever will
while the UK is outside the Union. The anchor is reached instead by the UK's
own instruments — [[GB-UK-GDPR]], [[GB-DPA-2018]], [[GB-DUAA]],
[[GB-NIS-REGULATIONS]] and [[GB-CAF]] all carry `applies-in` [[GB]], the
same treatment [[NL-BIO]] carries for the Netherlands.

The links to Europe are these:

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
3. **[[EU-UK-ADEQUACY]] `references` [[GB-UK-GDPR]] and [[GB-DUAA]].** The
   only edge in the Atlas running *from* the EU *to* a non-member state — and
   the only one of the three that is current rather than historical.

A fourth route runs through standards rather than law: [[GB-BSI]]
`participates-in` [[EU-CEN]], [[EU-CENELEC]] and [[EU-ETSI]], **because those
are not EU institutions** and its membership survived Brexit.

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

## The EU adequacy decisions — now recorded

The batch that created this entity said the adequacy decisions were *"the
single most important connective fact between the UK and the EU data layer"*
and that no edge represented them. [[EU-UK-ADEQUACY]] now does: renewed
**19 December 2025**, expiring **27 December 2031** under a sunset clause,
following the changes made by [[GB-DUAA]].

It is filed at `level: regional`, `region: EU` — because it is a **Commission
act, not a UK one** — and it is the only edge in the Atlas running *from* the
European Union *to* a non-member state's instrument. The other two EU links
run the other way and are both historical; this one is current and carries an
expiry date.

## Relationships

See `countries/gb/index.md` for the curated index of UK entities.

## Sources

Listed in frontmatter. The REUL Act explanatory notes and gov.scot's
assimilated-law page were read directly this pass. The ISO Online
Browsing Platform entry — the citation [[DE]], [[BE]], [[FR]], [[ES]] and
[[PL]] carry — has been dropped: it is bot-walled (403) and was never
read, and it supported only the alternative name removed above. `coe.int`
remains cited but unread, also bot-walled.
