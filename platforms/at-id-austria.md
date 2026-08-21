---
id: AT-ID-AUSTRIA
type: platform
name: ID Austria
alternative_names:
  - ID-Austria
description: >
  Austria's national digital identity, which enables citizens to prove
  their identity to digital applications and services. It is delivered by
  the Bundesrechenzentrum, and its introduction required amendments to the
  E-Government Act, the Registration Act, the Civil Status Act and the
  Passport Act.

level: national
country: AT
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - AT
  - AT-BRZ
relationships:
  - type: part-of
    target: AT
    source: fact
    evidence: "ID Austria is a public body of AT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: AT-BRZ
    source: fact
    evidence: "ID Austria enables citizens to prove their identity to digital applications and services and is presented by the Bundesrechenzentrum among its services and products; BRZ and ID Austria took gold at an international e-government competition (brz.gv.at 'ID Austria'; brz.gv.at press release). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ID Austria - BRZ"
    url: "https://www.brz.gv.at/was-wir-tun/services-produkte/id-austria.html"
    publisher: "Bundesrechenzentrum (BRZ)"
  - title: "Plattform oesterreich.gv.at"
    url: "https://www.bmdw.gv.at/Themen/Digitalisierung/Verwaltung/Plattform-oesterreich-gv-at.html"
    publisher: "Bundesministerium fur Digitalisierung und Wirtschaftsstandort"
---

# ID Austria

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Austria's national digital identity.

## Four statutes had to move

Introducing the oesterreich.gv.at platform and ID Austria required
amendments to the **E-Government Act, the Registration Act, the Civil
Status Act and the Passport Act**.

None of those four is an Atlas entity, so the Austrian identity layer
currently has a platform with no legal basis attached - the same shape
as [[ES-CLAVE]], whose statutory basis is also queued.

## Sources

Listed in frontmatter.
