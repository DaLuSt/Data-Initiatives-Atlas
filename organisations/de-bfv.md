---
id: DE-BFV
type: organisation
name: Bundesamt für Verfassungsschutz
alternative_names:
  - BfV
  - Federal Office for the Protection of the Constitution
description: >
  Germany's domestic intelligence service, in the portfolio of the Federal
  Ministry of the Interior. It is responsible for anti-constitutional and
  security-threatening activities, and for espionage by foreign intelligence
  services in Germany. Its statutory basis is the Bundesverfassungsschutzgesetz,
  supplemented for interception measures by the Artikel 10-Gesetz.

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
organisations:
  - DE-BMI
related_entities:
  - DE-BVERFSCHG
  - DE-G10
  - DE-BND
  - DE-BAMAD
  - DE-PKGR
relationships:
  - type: part-of
    target: DE-BMI
    source: fact
    evidence: "The BfV falls under the Federal Ministry of the Interior and is a domestic intelligence service responsible for anti-constitutional and security-threatening activities as well as espionage activities by foreign intelligence services in Germany (bundestag.de 'Die Arbeit der Nachrichtendienste'; geheimdienste.org 'Recht und Gesetz'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-BVERFSCHG
    source: fact
    evidence: "Each of the three federal intelligence services has its own law: the Verfassungsschutz is governed by the Bundesverfassungsschutzgesetz (BVerfSchG) (bundestag.de 'Die Arbeit der Nachrichtendienste'; bfdi.bund.de 'Kontrolllandschaft Nachrichtendienste des Bundes'; geheimdienste.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-G10
    source: fact
    evidence: "The main legal frameworks for the federal intelligence services include the Bundesverfassungsschutzgesetz, the BND-Gesetz, the MAD-Gesetz and the Gesetz zur Beschränkung des Brief-, Post- und Fernmeldegeheimnisses (Artikel 10-Gesetz, G10); the BVerfSchG, MADG, BNDG, G10G and TKG are the essential legal foundations for data processing by the federal services (bfdi.bund.de; geheimdienste.org 'Recht und Gesetz'). NOT READ — search-only."
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

# Bundesamt für Verfassungsschutz (BfV)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The BfV is Germany's **domestic** intelligence service, in the portfolio of
[[DE-BMI]]. Its remit as the sources describe it has two halves:
anti-constitutional and security-threatening activities, and **espionage by
foreign intelligence services operating in Germany** — counter-intelligence
for the civilian sphere, with [[DE-BAMAD]] doing the equivalent job for the
Bundeswehr.

## The one German service the Atlas can place in a ministry

[[DE-BMI]] is an Atlas entity, so `part-of` can be asserted here. It cannot
be for [[DE-BND]] (Federal Chancellery) or [[DE-BAMAD]] (Federal Ministry
of Defence), neither of which the Atlas holds.

This puts the BfV in the same ministry as two entities the Atlas already
had: [[DE-BSI]] and [[DE-DESTATIS]] are both `part-of` [[DE-BMI]]. The
federal interior ministry now anchors the German cyber-security authority,
the federal statistical office and the domestic intelligence service — three
very different kinds of body, and a good illustration of why `part-of` to a
ministry says less than it appears to.

## An oversight change that is proposed, not made

The sources report a government bill under which the [[DE-UKR]] — created
for [[DE-BND]] — would be **upgraded to cover the BfV as well**. That has
not happened, and no relationship between the BfV and the UKR is asserted
here. The BfV's parliamentary oversight through [[DE-PKGR]] is not in
question and is asserted on that entity.

## Not modelled

- The **sixteen Landesämter für Verfassungsschutz**. Germany's domestic
  intelligence function is federal *and* state-level; the Atlas has no
  sub-national level, so only the federal office appears. Reading
  `country: DE` here as national coverage would be the same mistake
  [[DE-BFDI]] warns about.
- The **Bundesamt für Verfassungsschutz's report** (*Verfassungsschutzbericht*),
  an annual publication that would be a `publication` entity.

## Relationships

- `part-of` [[DE-BMI]].
- `governed-by` [[DE-BVERFSCHG]] and [[DE-G10]].

## Sources

Listed in frontmatter.
