---
id: DE-BND
type: organisation
name: Bundesnachrichtendienst
alternative_names:
  - BND
  - Federal Intelligence Service
description: >
  Germany's foreign intelligence service, under the supervision of the Head
  of the Federal Chancellery. It gathers information of foreign and security
  policy importance for the Federal Republic. Its statutory basis is the
  BND-Gesetz, supplemented for interception measures by the Artikel
  10-Gesetz.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - DE-BNDG
  - DE-G10
  - DE-BFV
  - DE-BAMAD
  - DE-PKGR
  - DE-UKR
relationships:
  - type: governed-by
    target: DE-BNDG
    source: fact
    evidence: "Each of the three federal intelligence services has its own law: the BND is governed by the Gesetz über den Bundesnachrichtendienst (BNDG) (bundestag.de 'Die Arbeit der Nachrichtendienste'; gesetze-im-internet.de/bndg; geheimdienste.org 'Recht und Gesetz'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-G10
    source: fact
    evidence: "The essential legal foundations for data processing by the federal intelligence services are the BVerfSchG, the MADG, the BNDG, the G10G and the TKG; the main legal frameworks include the Gesetz zur Beschränkung des Brief-, Post- und Fernmeldegeheimnisses (Artikel 10-Gesetz, G10) (bfdi.bund.de 'Kontrolllandschaft Nachrichtendienste des Bundes'; bundestag.de; geheimdienste.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BNDG — Gesetz über den Bundesnachrichtendienst"
    url: "https://www.gesetze-im-internet.de/bndg/BJNR029790990.html"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
  - title: "Die Arbeit der Nachrichtendienste"
    url: "https://www.bundestag.de/webarchiv/Ausschuesse/ausschuesse20/weitere_gremien/parlamentarisches_kontrollgremium/nachrichtendienste-867434"
    publisher: "Deutscher Bundestag"
  - title: "Aufsicht über die Nachrichtendienste des Bundes"
    url: "https://www.bfdi.bund.de/DE/Fachthemen/Inhalte/Nachrichtendienste/Kontrollandschaft-Nachrichtendienste-des-Bundes.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
  - title: "Bundestag novelliert die Rechtsgrundlagen der Nachrichtendienste"
    url: "https://www.bundestag.de/dokumente/textarchiv/2023/kw46-de-bnd-976564"
    publisher: "Deutscher Bundestag"
---

# Bundesnachrichtendienst (BND)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The BND is Germany's **foreign** intelligence service. It falls under the
supervision of the Head of the Federal Chancellery — not under a line
ministry, unlike [[DE-BFV]] (Interior) and [[DE-BAMAD]] (Defence) — and
gathers information of foreign and security policy importance for the
Federal Republic.

## Germany's three services, three acts

Germany is the clearest case in the Atlas of **one statute per service**:

| Service | Act | Reports to |
|---|---|---|
| BND | [[DE-BNDG]] | Federal Chancellery |
| [[DE-BFV]] | [[DE-BVERFSCHG]] | [[DE-BMI]] |
| [[DE-BAMAD]] | [[DE-MADG]] | Federal Ministry of Defence |

Cutting across all three is **[[DE-G10]]**, the Artikel 10-Gesetz, which
restricts the privacy of correspondence, post and telecommunications
guaranteed by Article 10 of the Basic Law and sets the conditions under
which the services may interfere with it. The BfDI's own description of the
oversight landscape lists BVerfSchG, MADG, BNDG, G10G and the TKG together
as the essential legal foundations for data processing by the federal
services.

Contrast the Dutch and Belgian model, where a **single** organic act
([[NL-WIV-2017]], [[BE-WIV-1998]]) covers both the civilian and the military
service.

## No `part-of` edge

The Federal Chancellery is not an Atlas entity, so the BND's reporting line
cannot be modelled the way [[DE-BFV]]'s to [[DE-BMI]] can. The asymmetry in
the graph is a coverage artefact, not a claim about German administrative
structure.

## The oversight the Constitutional Court ordered

Germany's intelligence oversight was rebuilt after litigation, and the
timeline is unusual enough to record:

- The **[[DE-PKGR]]** — the Bundestag's Parliamentary Control Panel — is the
  long-standing parliamentary control body for all three services.
- The **[[DE-UKR]]**, an independent judicial-style control council, was
  created for the BND specifically, and its provisions were subsequently
  moved out of the BND-Gesetz in implementation of a Federal Constitutional
  Court decision of **28 September 2022**.
- Reform proposals reported by the sources would upgrade the UKR to cover
  [[DE-BFV]] as well, not only the BND.

The last of those is a **proposal**, and [[DE-UKR]] records it as one.

## Not modelled

- The **Länder Verfassungsschutz authorities**. Each Land has its own, and
  the Atlas has no sub-national level — the same limitation recorded on
  [[DE-BFDI]].
- The **Telekommunikationsgesetz (TKG)**, named by the BfDI among the legal
  foundations for intelligence data processing but not researched here.
- The **2021 and 2023 BND-Gesetz amendments**, which the Bundestag's own
  archive records but whose content was not established.

## Relationships

- `governed-by` [[DE-BNDG]] and [[DE-G10]].

## Sources

Listed in frontmatter.
