---
id: DE-BAMAD
type: organisation
name: Bundesamt für den Militärischen Abschirmdienst
alternative_names:
  - BAMAD
  - MAD
  - Militärischer Abschirmdienst
  - Military Counterintelligence Service
description: >
  Germany's military intelligence and counter-intelligence service, assigned
  to the Federal Ministry of Defence. It investigates anti-constitutional or
  security-threatening activities directed against the Bundeswehr. Its
  statutory basis is the MAD-Gesetz, supplemented for interception measures
  by the Artikel 10-Gesetz.

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
  - DE-MADG
  - DE-G10
  - DE-BND
  - DE-BFV
  - DE-PKGR
relationships:
  - type: governed-by
    target: DE-MADG
    source: fact
    evidence: "Each of the three federal intelligence services has its own law: the MAD is governed by the Gesetz über den Militärischen Abschirmdienst (MADG) (bundestag.de 'Die Arbeit der Nachrichtendienste'; geheimdienste.org 'Recht und Gesetz'; bfdi.bund.de 'Kontrolllandschaft Nachrichtendienste des Bundes'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-G10
    source: fact
    evidence: "The essential legal foundations for data processing by the federal intelligence services are the BVerfSchG, the MADG, the BNDG, the G10G and the TKG; the Artikel 10-Gesetz is listed among the main legal frameworks for all three services (bfdi.bund.de 'Kontrolllandschaft Nachrichtendienste des Bundes'; geheimdienste.org 'Recht und Gesetz'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Die Arbeit der Nachrichtendienste"
    url: "https://www.bundestag.de/webarchiv/Ausschuesse/ausschuesse20/weitere_gremien/parlamentarisches_kontrollgremium/nachrichtendienste-867434"
    publisher: "Deutscher Bundestag"
  - title: "Aufsicht über die Nachrichtendienste des Bundes"
    url: "https://www.bfdi.bund.de/DE/Fachthemen/Inhalte/Nachrichtendienste/Kontrollandschaft-Nachrichtendienste-des-Bundes.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
  - title: "Recht & Gesetz"
    url: "https://geheimdienste.org/recht-und-gesetz"
    publisher: "geheimdienste.org"
---

# Bundesamt für den Militärischen Abschirmdienst (BAMAD / MAD)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The MAD is assigned to the Federal Ministry of Defence and, in the sources'
words, clarifies anti-constitutional or security-threatening activities
**directed against the Bundeswehr**.

That scope is narrower than the name "military intelligence" suggests. The
MAD is a counter-intelligence and security service *for the armed forces*,
not a foreign military intelligence collector — the German equivalent of
France's [[FR-DRSD]] rather than of [[FR-DRM]], and closer to Poland's
[[PL-SKW]] than to [[PL-SWW]].

## Germany has no foreign military intelligence service in this Atlas

This is worth stating because the pattern differs from the other countries
with a military/civilian split. France and Poland each field **two** military
services — collection ([[FR-DRM]], [[PL-SWW]]) and security
([[FR-DRSD]], [[PL-SKW]]). Germany's federal triad is BND / BfV / MAD, with
the foreign collection role sitting with [[DE-BND]] rather than with a
separate military body.

Whether the Bundeswehr holds a distinct intelligence-collection organisation
outside the MAD was **not researched**, and its absence here should not be
read as a finding.

## Naming

Both "MAD" and "BAMAD" appear in the sources. The Bundestag's own page uses
*Militärischer Abschirmdienst* (MAD) when listing the three services; the
office's formal name is the **Bundesamt für den Militärischen
Abschirmdienst**. The Atlas files it under the formal name with the common
abbreviation as an alternative name, the same convention used for
[[DE-BFDI]].

## Relationships

- `governed-by` [[DE-MADG]] and [[DE-G10]].

## Sources

Listed in frontmatter.
