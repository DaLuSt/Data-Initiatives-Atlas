---
id: TD-ANSICE
type: organisation
name: "National Agency for Information Security and Electronic Certification (ANSICE, Chad)"
alternative_names:
  - "ANSICE"
  - "Agence Nationale de Sécurité Informatique et de Certification Électronique"
description: >
  The agency the data protection Law (Loi n° 007/PR/2015) names as the authority for personal data: articles 40 and 44 have access requests addressed to the ANSICE, which carries out the verifications. ARCEP's Laws page lists Loi N°006/PR/2015 'portant création de l'Agence Nationale de Sécurité Informatique et de Certification Électronique' (number and title only).
  No page of the agency itself was found or read, so whether it operates is not established (`status: unknown`).

level: national
country: TD
region: null

status: unknown
organisation_role: regulatory
confidence: low
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - TD
  - TD-LOI-007-2015
relationships:
  - type: part-of
    target: TD
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Loi n° 007/PR/2015 (read 2026-11-06 as page images): the ANSICE is the authority to which access requests are addressed (articles 40 to 44); a statutory agency of the State."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: TD-LOI-007-2015
    source: fact
    evidence: "Loi n° 007/PR/2015, articles 40 and 44 (page 17 of the scanned PDF): the ANSICE verifies data processing on request; the Law governs its personal data role."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Loi n° 007/PR/2015 portant protection des données à caractère personnel (scanned PDF on the ARCEP site)"
    url: "https://www.arcep.td/sites/default/files/Loi-N%C2%B007-PR-2015.pdf"
    publisher: "ARCEP, Chad (copy of the Law)"
    accessed: "2026-11-06"
  - title: "ARCEP Tchad, Lois"
    url: "https://www.arcep.td/lois.html"
    publisher: "ARCEP, Chad"
    accessed: "2026-11-06"
---

# National Agency for Information Security and Electronic Certification (ANSICE, Chad)

> **Created 2026-11-06** (roadmap #481). `status: unknown`: known from the Law that names it and from the title of the law that created it; no page of its own was read.

## Relationships

Part of [[TD]]; governed by [[TD-LOI-007-2015]].
