---
id: DE-OZG
type: law
name: Onlinezugangsgesetz
alternative_names:
  - OZG
  - Online Access Act
description: >
  German federal act obliging the federation, the Länder and the
  municipalities to offer their administrative services electronically
  through linked administrative portals. It was substantially amended by
  the OZG-Änderungsgesetz, which entered into force in July 2024, and it
  provides the legal basis for the central citizen account BundID.

level: national
country: DE
region: EU

status: active
confidence: low
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
  - DE-BUNDID
  - DE-EGOVG
relationships: []

sources:
  - title: "Upgrade für ein Digitales Deutschland ist da: Das OZG-Änderungsgesetz tritt in Kraft"
    url: "https://www.bmi.bund.de/SharedDocs/kurzmeldungen/DE/2024/07/ozg.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Bund hat seine 115 wichtigsten Verwaltungsleistungen bis Ende 2024 erfolgreich digitalisiert"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2024/12/ozg.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "FITKO (Föderale IT-Kooperation) — OZG-Grundlagen, Akteure"
    url: "https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/ozg-grundlagen/akteure/fitko/fitko-node.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
  - title: "BundID (Nutzerkonto) — DeutschlandID | Onlinezugangsgesetz in Brandenburg"
    url: "https://ozg.brandenburg.de/ozg/de/it-infrastrukturen/it-basiskomponenten/bundid-nutzerkonto-deutschlandid/"
    publisher: "Land Brandenburg"
---

# Onlinezugangsgesetz (OZG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The OZG obliges German public administration at federal, Land and municipal
level to offer administrative services electronically through linked
administrative portals. It is the instrument the German administrative
digitalisation programme is organised around, and the reason
[[DE-FITKO]] is described in the sources under the heading of OZG
governance actors.

Two sourced developments:

- The **OZG-Änderungsgesetz** entered into force in July 2024, described by
  the BMI as an "upgrade for a digital Germany".
- The federal government reported having **digitalised its 115 most
  important administrative services by the end of 2024**.

It provides the legal basis for [[DE-BUNDID]].

## ⚠ Why `confidence: low` and `start_date: null`

This entity records an act whose **own enactment date was not established**.
Every source returned by search concerns the 2024 amendment or the
programme run under the act, not the act's original passage. The OZG is
widely known to date from 2017, and that is precisely why it is **not
recorded here**: §21 of the brief rules out writing down what is merely
well known.

The same reasoning kept the **OZG-Änderungsgesetz from becoming its own
entity**. It is a substantial amending act with its own content, and a case
could be made for modelling it separately — but the Atlas has no
amendment-lineage relationship type (see [[DE-NIS2UMSUCG]]), and creating a
second entity would have forced the same `supersedes` compromise a second
time. One entity, with the amendment recorded as a fact in the body, keeps
the record accurate at the cost of some resolution.

`coverage: low` reflects both gaps.

## Relationships

**None asserted.** The links a reader would expect — to [[DE-EGOVG]], which
the OZG builds on, and *from* [[DE-BUNDID]], whose legal basis it provides
— are recorded where they are sourced: [[DE-BUNDID]] carries
`governed-by` → this entity. The EGovG connection is not sourced and is
not asserted.

## Sources

Listed in frontmatter. **No statutory text is cited** — no
Gesetze-im-Internet URL for the OZG was returned by search — which is the
direct cause of the missing date.
