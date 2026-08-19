---
id: CH
type: country
name: Switzerland
alternative_names:
  - Swiss Confederation
  - Schweiz
  - Suisse
  - Svizzera
description: >
  Country anchor entity for Switzerland, the ninth national scope covered by
  the Data Initiatives Atlas and the first that is neither a member state of
  the European Union nor a party to the Agreement on the European Economic
  Area. Its relationship with the Union runs through bilateral agreements,
  and its data protection law is autonomous rather than an implementation of
  the GDPR.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
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
    evidence: "Switzerland is one of the 46 member states of the Council of Europe, an intergovernmental organisation separate from the European Union (coe.int 'The Council of Europe's 46 member states'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "CH — Switzerland (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:CH"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Neues Datenschutzgesetz (revDSG)"
    url: "https://www.kmu.admin.ch/de/neues-datenschutzgesetz-revdsg"
    publisher: "KMU-Portal, Staatssekretariat für Wirtschaft (SECO)"
  - title: "Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)"
    url: "https://digital.swiss/de/aktionsplan/massnahme/bundesgesetz-uber-den-einsatz-elektronischer-mittel-zur-erfullung-von-behordenaufgaben-embag"
    publisher: "digital.swiss / Bundeskanzlei"
---

# Switzerland

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Switzerland (ISO 3166-1 alpha-2: **`CH`**) is the **ninth country** in the
Atlas and completes the set of four possible relationships to EU law.

## The fourth pattern

| Country type | How EU law reaches it | In the Atlas |
|---|---|---|
| Member state | Directly applicable, or transposed | [[NL]], [[DE]], [[BE]], [[FR]], [[ES]], [[PL]], [[IE]] |
| Former member state | Assimilated law, adequacy, extraterritorial scope | [[GB]] |
| EEA EFTA state | Incorporation by Joint Committee decision, then national implementation | [[NO]] |
| **Neither** | **Autonomous national law, plus an adequacy decision and bilateral agreements** | **Switzerland** |

Switzerland is not in the Union, not in the EEA, and not — unlike [[GB]] —
a former member with a body of assimilated Union law. It is the cleanest
case in the Atlas of a European country whose data law is **its own**.

## Autonomous, but not independent

The Swiss position is not indifference to EU law, and the entity would
mislead if it implied that.

[[CH-REVDSG]] replaced a 1992 act that, in the sources' words, no longer met
the EU's level of data protection. The revision was driven by the need to
**maintain Switzerland's adequacy status** under [[EU-GDPR]] Article 45, so
that data can keep flowing from the Union to Switzerland without additional
safeguards, and to prevent competitive disadvantage for Swiss companies
trading with EU ones.

So the influence is real and the mechanism is entirely different from every
other country here:

- **A member state** implements because it must.
- **[[NO]]** implements because the EEA Joint Committee incorporated the
  act.
- **Switzerland legislates for itself, and aims at a standard it is
  measured against.** The pressure is commercial and diplomatic, not legal.

## ⚠ No `applies-in` edge from any EU instrument points at Switzerland

None is asserted. Unlike [[NO]], where the question is *which instrument*
carries the effect, here there is no route at all: no Union act applies in
Switzerland by force of Union law, and no Joint Committee mechanism
substitutes for one.

[[EU-GDPR]] still reaches Swiss businesses through its **extraterritorial
scope** under Article 3, where they target or monitor people in the Union —
but that is the Regulation applying to a *controller*, not applying *in a
country*, and the Atlas has no relationship type that says so. It is
recorded here in prose. The same distinction is drawn on [[GB]].

## Not modelled

- **The EU–Switzerland adequacy decision.** The Atlas holds
  [[EU-UK-ADEQUACY]] and nothing equivalent for Switzerland, though the same
  kind of Commission act covers it. Queued in `discovery/candidates.md`.
- **The bilateral agreements** (*Bilaterale I* and *II*) and the framework
  agreement negotiations, which define the whole relationship.
- **The cantons.** Switzerland is federal, and each canton has its own data
  protection authority and its own administration. The Atlas has no
  sub-national level — the same limit recorded for the German Länder on
  [[DE-BFDI]] and, more sharply here, because Swiss federalism devolves more.

## Sources

Listed in frontmatter.
