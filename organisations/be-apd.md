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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
  - BE-GDPR-WET
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Confirmed by reading gdpr-info.eu directly (2026-08-26): Article 68(3) GDPR states 'The Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives.' The Gegevensbeschermingsautoriteit is Belgium's supervisory authority. gdprhub.eu was not re-fetched this pass."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-to
    target: BE-GDPR-WET
    source: fact
    evidence: "Confirmed by reading both gegevensbeschermingsautoriteit.be pages directly (2026-08-26). The authority's own page states the wet van 30 juli 2018 'integreert de beginsels van de AVG' and 'annuleert definitief de privacywet van 8 december 1992'; its sensitive-data page sets out the Article 9 GDPR special categories and the criminal-data category, and the exceptions to the processing prohibition, as guidance under the Belgian implementing act."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-26"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
  - title: "Wet van 30 juli 2018"
    url: "https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/recht-op-afbeelding/wet-van-30-juli-2018"
    publisher: "Gegevensbeschermingsautoriteit (GBA/APD)"
    accessed: "2026-08-26"
  - title: "Gevoelige gegevens"
    url: "https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/gevoelige-gegevens"
    publisher: "Gegevensbeschermingsautoriteit (GBA/APD)"
    accessed: "2026-08-26"
  - title: "Kruispuntbank van de Sociale Zekerheid — AVG Register"
    url: "https://gdpr.belgium.be/nl/federal-institutions/kruispuntbank-van-de-sociale-zekerheid"
    publisher: "gdpr.belgium.be (Belgian federal government)"
    accessed: "2026-08-26"
---

# Gegevensbeschermingsautoriteit (GBA / APD)

> **Verified 2026-08-26.** Four of five sources were read directly — both
> `gegevensbeschermingsautoriteit.be` pages, `gdpr-info.eu`, and `gdpr.belgium.be`'s
> KSZ register entry — confirming both relationships this entity asserts.
> `gdprhub.eu` was not re-fetched. `verification: primary-source`.

## Description

The GBA/APD is Belgium's data protection supervisory authority. It
supervises compliance with [[EU-GDPR]] and [[BE-GDPR-WET]], and publishes
guidance for citizens and controllers — on data subject rights, on the
enhanced protection the GDPR and the 2018 act give to special categories of
personal data, and a thirteen-step implementation plan for controllers. Its
`gdpr.belgium.be` register lists federal institutions' own GDPR
declarations, including [[BE-KSZ]]'s.

`coverage: low`: its constitution, powers, governance structure and the
relationship between its constituent chambers were not established. What is
recorded is its role relative to the Belgian implementing act.

## The third data protection authority, and a pre-existing inconsistency corrected

This section previously described the `participates-in` [[EU-EDPB]] edge as
"refused for want of a source" while the frontmatter already carried it —
a frontmatter/body mismatch predating this pass, now corrected. Confirmed
this pass by reading gdpr-info.eu directly: Article 68(3) GDPR requires the
Board to be composed of the head of one supervisory authority of each
Member State, and the GBA/APD is Belgium's, so the edge rests on the
regulation's own text rather than on a Belgium-specific announcement.

| Country | Authority | `participates-in` [[EU-EDPB]]? |
|---|---|---|
| Netherlands | [[NL-AP]] | **yes** — a Dutch source states it |
| Germany | [[DE-BFDI]] | **no** — refused; German Board representation is complicated by the Land authorities and should not be guessed |
| Belgium | **GBA/APD** | **yes** — confirmed this pass from Article 68(3) GDPR's own text |

Two of three national DPAs in the Atlas now connect to the Board — one on a
country-specific statement, one on the regulation's own composition rule.
Germany's remains open because its situation is genuinely more complex, not
for want of trying.

## Relationships

- `participates-in` [[EU-EDPB]] — confirmed from Article 68(3) GDPR's text.
- `applies-to` [[BE-GDPR-WET]] — confirmed from the authority's own pages,
  which discuss the Belgian act directly.

## Sources

Four of five read directly this pass — both gegevensbeschermingsautoriteit.be
pages, gdpr-info.eu, and gdpr.belgium.be's KSZ register entry. gdprhub.eu
was not re-fetched.
