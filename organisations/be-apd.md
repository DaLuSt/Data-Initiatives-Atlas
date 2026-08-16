---
id: BE-APD
type: organisation
name: Gegevensbeschermingsautoriteit
alternative_names:
  - GBA
  - Autorité de protection des données
  - APD
  - Belgian Data Protection Authority
description: >
  Belgian data protection supervisory authority. It supervises compliance
  with the GDPR and the Belgian act of 30 July 2018 implementing it, and
  publishes guidance for citizens and controllers on data subject rights
  and on the enhanced protection of special categories of personal data.

level: national
country: BE
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-GDPR-WET
relationships:
  - type: applies-to
    target: BE-GDPR-WET
    source: fact
    evidence: "The Gegevensbeschermingsautoriteit publishes and maintains guidance on the wet van 30 juli 2018, including on sensitive data, where the GDPR and the law of 30 July 2018 together provide enhanced protection for special categories of personal data (gegevensbeschermingsautoriteit.be 'Wet van 30 juli 2018'; 'Gevoelige gegevens'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Wet van 30 juli 2018"
    url: "https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/recht-op-afbeelding/wet-van-30-juli-2018"
    publisher: "Gegevensbeschermingsautoriteit (GBA/APD)"
  - title: "Gevoelige gegevens"
    url: "https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/gevoelige-gegevens"
    publisher: "Gegevensbeschermingsautoriteit (GBA/APD)"
  - title: "Kruispuntbank van de Sociale Zekerheid — AVG Register"
    url: "https://gdpr.belgium.be/nl/federal-institutions/kruispuntbank-van-de-sociale-zekerheid"
    publisher: "gdpr.belgium.be (Belgian federal government)"
---

# Gegevensbeschermingsautoriteit (GBA / APD)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The GBA/APD is Belgium's data protection supervisory authority. It
supervises compliance with [[EU-GDPR]] and [[BE-GDPR-WET]], and publishes
guidance for citizens and controllers — on data subject rights, on the
enhanced protection the GDPR and the 2018 act give to special categories of
personal data, and a thirteen-step implementation plan for controllers.

`coverage: low`: its constitution, powers, governance structure and the
relationship between its constituent chambers were not established. What is
recorded is its role relative to the Belgian implementing act.

## The third data protection authority, and the one relationship that is now askable

| Country | Authority | `participates-in` [[EU-EDPB]]? |
|---|---|---|
| Netherlands | [[NL-AP]] | **yes** — sourced |
| Germany | [[DE-BFDI]] | **no** — refused for want of a source |
| Belgium | **GBA/APD** | **no** — refused for want of a source |

The Dutch link is recorded because a Dutch source stated it. The German one
was refused because German representation on the Board is complicated by
the Land authorities and should not be guessed. The Belgian one is refused
for the plainer reason that **no source read mentions the EDPB at all**.

Three national DPAs now sit in the Atlas and only one connects to the
European Data Protection Board. That is a sourcing artefact, not a fact
about European data protection governance, and it is exactly the kind of
distortion the `verification` field exists to keep visible. Logged in
`discovery/unresolved.md`.

## Relationships

- `applies-to` [[BE-GDPR-WET]].

Note this is the mirror of the German case: [[DE-BFDI]] could not be
connected to [[DE-BDSG]] for want of a citable statement, while the Belgian
authority's own pages discuss the Belgian act directly, so the link is
recorded here.

## Sources

Listed in frontmatter.
