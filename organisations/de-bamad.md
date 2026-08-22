---
id: DE-BAMAD
type: organisation
name: Bundesamt für den Militärischen Abschirmdienst
alternative_names:
  - BAMAD
  - MAD
  - Militärischer Abschirmdienst
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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading bundestag.de's 'Die Arbeit der Nachrichtendienste' page (2026-08-22): 'Die drei Nachrichtendienste des Bundes sind der Bundesnachrichtendienst (BND), der Militärische Abschirmdienst (MAD) und das Bundesamt für Verfassungsschutz (BfV).' Each of the three has its own act; the MAD's is the Gesetz über den Militärischen Abschirmdienst (MADG)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-G10
    source: fact
    evidence: "Confirmed by reading bfdi.bund.de's 'Kontrolllandschaft Nachrichtendienste des Bundes' page (2026-08-22): 'Die wesentlichen Rechtsgrundlagen für Datenverarbeitungen der Nachrichtendienste des Bundes ... sind das BVerfSchG, das MADG, das BNDG, das G10G und das TKG.' The Artikel 10-Gesetz (G10G) applies across all three services, including the MAD."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Die Arbeit der Nachrichtendienste"
    url: "https://www.bundestag.de/webarchiv/Ausschuesse/ausschuesse20/weitere_gremien/parlamentarisches_kontrollgremium/nachrichtendienste-867434"
    publisher: "Deutscher Bundestag"
    accessed: "2026-08-22"
  - title: "Aufsicht über die Nachrichtendienste des Bundes"
    url: "https://www.bfdi.bund.de/DE/Fachthemen/Inhalte/Nachrichtendienste/Kontrollandschaft-Nachrichtendienste-des-Bundes.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
    accessed: "2026-08-22"
  - title: "Recht & Gesetz"
    url: "https://geheimdienste.org/recht-und-gesetz"
    publisher: "geheimdienste.org"
    accessed: "2026-08-22"
---

# Bundesamt für den Militärischen Abschirmdienst (BAMAD / MAD)

> **Verified 2026-08-22.** The Bundestag's "Die Arbeit
> der Nachrichtendienste" page and the BfDI's "Kontrolllandschaft
> Nachrichtendienste des Bundes" page were read directly and confirmed the
> claims below.

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
