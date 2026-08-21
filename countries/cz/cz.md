---
id: CZ
type: country
name: Czechia
alternative_names:
  - Czech Republic
  - Česká republika
description: >
  Country anchor entity for Czechia, the thirteenth national scope covered by
  the Data Initiatives Atlas and its eleventh European Union member state.
  Used as the target of `country` fields for Czechia-scoped entities and of
  `applies-in` relationships from EU instruments.

level: national
country: CZ
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Czechia is one of the 27 member states of the European Union, having acceded on 1 May 2004; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-20"
  - title: "CZ — Czechia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:CZ"
    publisher: "International Organization for Standardization (ISO)"
    accessed: "2026-08-20"
  - title: "Digitální a informační agentura"
    url: "https://www.dia.gov.cz/cs"
    publisher: "Digitální a informační agentura (DIA)"
    accessed: "2026-08-20"
  - title: "Zákon o správě dat a řízeném přístupu otevírá cestu státu k efektivnímu rozhodování"
    url: "https://www.dia.gov.cz/cs/aktuality/zakon-o-sprave-dat-a-rizenem-pristupu-otevira-cestu-statu-k-efektivnimu-rozhodovani"
    publisher: "Digitální a informační agentura (DIA)"
    accessed: "2026-08-20"
---

# Czechia

> **Verified 2026-08-20.** Every cited source was read and confirmed to
> support what this entity says, including its accession date.
> `verification: primary-source`.

## Description

Czechia (ISO 3166-1 alpha-2: **`CZ`**) is the **thirteenth country** in the
Atlas and its **eleventh EU member state**. It doubles the Central European
sample, which was [[PL]] alone.

## What Czechia adds that no other country here has

**A general act on data management and controlled access.**

[[CZ-ZAKON-60-2026]] — *zákon o správě dat a řízeném přístupu* — is a
horizontal statute about how the **state itself** manages and shares its
data. Under it [[CZ-DIA]] becomes the **single information point** for
Czechia and the node connecting Czech data sources to the **European data
portal**.

Nothing else in the Atlas is quite this. The Netherlands has an
interbestuurlijke datastrategie ([[NL-IBDS]]) and a federative data system
([[NL-FDS]]) — but those are a strategy and a system, not an act. Czechia
legislated the thing.

## The naming question, answered the way ISO does

The country's short name in ISO 3166-1 is **Czechia**; *Czech Republic* is
the formal name and is recorded as an alternative. The Atlas follows the ISO
short name for the same reason it uses **GB** rather than UK: the standard is
what `metadata/schema.json` points at.

## EU instruments that apply in Czechia

Recorded as `applies-in` edges on the instruments themselves. See
`countries/cz/index.md`.

## Not modelled

- The **regions and municipalities**. No sub-national level exists in the
  Atlas.
- **Portál občana** and the Czech digital identity means.
- **Slovakia**, whose standardisation body shares a centenary with Czechia's
  and whose separation from it in 1993 makes the two institutional histories
  hard to read apart.

## Sources

Listed in frontmatter.
