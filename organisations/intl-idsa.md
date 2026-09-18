---
id: INTL-IDSA
type: organisation
name: International Data Spaces Association
alternative_names:
  - IDSA
  - International Data Spaces
description: >
  International not-for-profit association working on the concept of data
  spaces and the principles their design should follow, so that value can be
  obtained from data through sharing on secure, transparent and fair terms
  that guarantee sovereignty and trust. Formed in 2016, it maintains the IDS
  Reference Architecture Model.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - INTL-IDS-RAM
  - DE-CATENA-X
  - NL-ISHARE
relationships:
  - type: produces
    target: INTL-IDS-RAM
    source: fact
    evidence: "Confirmed by reading all three cited pages directly (2026-08-28): internationaldataspaces.org's own 'Reference Architecture' page describes the IDS-RAM as 'a practical blueprint' for constructing data spaces addressing role model, data sovereignty, information model and usage-policy enforcement; its 'Understanding the IDSA Reference Architecture Model' page states the IDSA 'has developed a comprehensive Reference Architecture Model (RAM)' with the five-layer structure (business, functional, information, system, process) and names the IDSA as currently developing the model's fifth edition; datos.gob.es confirms the IDSA was 'formed in 2016' and comprises '133 international companies across 22 countries.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About IDSA"
    url: "https://internationaldataspaces.org/about/"
    publisher: "International Data Spaces Association (IDSA)"
    accessed: "2026-09-18"
  - title: "IDS Reference Architecture Model"
    url: "https://internationaldataspaces.org/offers/reference-architecture/"
    publisher: "International Data Spaces Association (IDSA)"
    accessed: "2026-08-28"
  - title: "Understanding the IDSA Reference Architecture Model"
    url: "https://internationaldataspaces.org/understanding-the-idsa-reference-architecture-model/"
    publisher: "International Data Spaces Association (IDSA)"
    accessed: "2026-08-28"
  - title: "The IDS-RAM reference architecture model and its role in data spaces"
    url: "https://datos.gob.es/en/blog/ids-ram-reference-architecture-model-and-its-role-data-spaces"
    publisher: "datos.gob.es (Gobierno de España)"
    accessed: "2026-08-28"
---

# International Data Spaces Association (IDSA)

> **Verified 2026-08-28.** All three cited pages were read directly.
> `verification` moves from `search-only` to `primary-source`. One
> nuance found on re-reading: the IDSA's own reference-architecture page
> now describes the model as on its fifth edition in development, with
> version 4 current — the "3.0 (April 2019)" version this Atlas ties to
> DIN SPEC 27070 (see [[INTL-IDS-RAM]]) is the version contemporaneous
> with that standard, not the association's current output.
>
> **Closed 2026-09-18** (`discovery/unresolved.md` row #130): the
> membership count, previously resting on one secondary source, is now
> confirmed directly by IDSA's own "About" page. See "Membership,
> verified" below.

## Description

The IDSA is an international not-for-profit association, formed in **2016**,
working on the concept of data spaces and the design principles they should
follow — so that value can be obtained from data through sharing on secure,
transparent and fair terms that guarantee **sovereignty and trust**.

## A gap this repository has been carrying since Batch 5

`discovery/research-queue.md` has listed the IDSA and the IDS reference
architecture since the Dutch platform batch, and reinforced it in the German
one, describing it as the **best-evidenced gap in the international layer**.
The reason was that two entities in two countries already referred to it and
had nowhere to point:

- [[DE-CATENA-X]] follows the IDS-RAM.
- [[NL-ISHARE]] records the IDSA incorporating iSHARE into it.

Both edges are now assertable, and are asserted on those entities.

## Why the association and the model are separate entities

[[INTL-IDS-RAM]] is a distinct entity rather than a property of this one,
following the pattern the Atlas already uses for [[INTL-ISO]] and
[[INTL-ISO-IEC-27001]], and for [[INTL-W3C]] and [[INTL-DCAT]]: the body that
maintains a specification and the specification itself are different things,
and other entities need to point at the specification, not the body.

## Membership, verified — 2026-09-18

`discovery/unresolved.md` row #130 flagged the previous "133 companies
across 22 countries" figure as resting on one secondary source
(datos.gob.es). IDSA's own "About" page, read directly, gives a newer,
directly-sourced figure instead: *"Its 140+ member companies and
institutions have created the International Data Spaces (IDS)
standard."* The page does not repeat a country count, so that detail is
dropped rather than carried forward unconfirmed. The same page also
names **Eclipse Dataspace Components (EDC)** — the current name for
what earlier sources called the Eclipse Dataspace Connector — as an
IDSA-affiliated implementation, used as the technical foundation of the
Gaia-X4KI project (its Connector, Federated Catalog, Identity Hub and
Registration Service components named specifically).

## Not modelled

- The **IDS Connector**, the central technical component — a security gateway
  through which data is exchanged, with **Base**, **Trust** and **Trust+**
  certification profiles. It is a software component, and `technology` is a
  type the Atlas defines and does not yet use.
- **Data sovereignty** as a concept, defined by the IDSA sources as a natural
  or legal person's capability of being entirely self-determined regarding
  its data.
- **Eclipse Dataspace Components (EDC)** and the Gaia-X4KI project itself —
  named above as IDSA-affiliated, but neither is an Atlas entity.

## Relationships

- `produces` [[INTL-IDS-RAM]].

## Sources

Listed in frontmatter. The original three read directly in the
2026-08-28 pass; IDSA's own "About" page, added and read directly
2026-09-18, closes the membership-count question.
