---
id: DE-BFV
type: organisation
name: Bundesamt für Verfassungsschutz
alternative_names:
  - BfV
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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed verbatim by reading bundestag.de's 'Die Arbeit der Nachrichtendienste' page (2026-08-22): 'Das BfV untersteht dem Bundesministerium des Innern. Es ist ein Inlandsnachrichtendienst und für verfassungsfeindliche und sicherheitsgefährdende Bestrebungen sowie Spionageaktivitäten ausländischer Nachrichtendienste in Deutschland zuständig.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-BVERFSCHG
    source: fact
    evidence: "Confirmed by reading bundestag.de's 'Die Arbeit der Nachrichtendienste' page (2026-08-22), which names the BfV as one of the three federal services each with its own statute, and bfdi.bund.de's 'Kontrolllandschaft Nachrichtendienste des Bundes' page, which lists the BVerfSchG first among the essential legal foundations for the federal services' data processing."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-G10
    source: fact
    evidence: "Confirmed by reading bfdi.bund.de's 'Kontrolllandschaft Nachrichtendienste des Bundes' page (2026-08-22): 'Die wesentlichen Rechtsgrundlagen für Datenverarbeitungen der Nachrichtendienste des Bundes ... sind das BVerfSchG, das MADG, das BNDG, das G10G und das TKG.'"
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

# Bundesamt für Verfassungsschutz (BfV)

> **Verified 2026-08-22.** The Bundestag's "Die Arbeit
> der Nachrichtendienste" page and the BfDI's "Kontrolllandschaft
> Nachrichtendienste des Bundes" page were read directly and confirmed the
> claims below.

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
