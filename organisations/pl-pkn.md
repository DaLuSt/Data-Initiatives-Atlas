---
id: PL-PKN
type: organisation
name: Polski Komitet Normalizacyjny
alternative_names:
  - PKN
  - Polish Committee for Standardization
description: >
  The national standardization body of Poland, and therefore its national
  member of CEN and its national committee in CENELEC. The national bodies
  operate the technical groups that draw up European Standards, coordinated
  by the CEN-CENELEC Management Centre in Brussels.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2004-01-01
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-CEN
  - EU-CENELEC
relationships:
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Confirmed by reading pkn.pl's own page directly (2026-08-26): 'Since 1 January 2004, the PKN has been a member of the CEN and CENELEC' — a precise date this entity did not previously carry. standards.cencenelec.eu's own current member list, also read directly, names PKN by row: 'PKN | Poland | Polish Committee for Standardization | www.pkn.pl'."
    confidence: medium
    valid_from: 2004-01-01
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "Confirmed by reading pkn.pl's own page directly (2026-08-26): 'Since 1 January 2004, the PKN has been a member of the CEN and CENELEC', and that PKN 'participates in CENELEC as a national electrotechnical committee.'"
    confidence: medium
    valid_from: 2004-01-01
    valid_until: null

sources:
  - title: "European Standards"
    url: "https://www.cencenelec.eu/european-standardization/european-standards/"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "CEN Community — List of members"
    url: "https://standards.cencenelec.eu/ords/f?p=CEN:5"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "Cooperation with European Standards Organizations"
    url: "https://www.pkn.pl/en/about-pkn/international-cooperation/cooperation-european-standards-organizations"
    publisher: "Polski Komitet Normalizacyjny (PKN)"
    accessed: "2026-08-26"
---

# Polski Komitet Normalizacyjny (PKN)

> **Verified 2026-08-26.** All three cited pages were read directly, and
> gave an exact membership date this entity did not previously carry.

## Description

PKN is the national standardization body of Poland. Confirmed by reading
pkn.pl directly: "Since 1 January 2004, the PKN has been a member of the
CEN and CENELEC" — full membership in CEN from that date, and
participation in CENELEC as Poland's national electrotechnical committee.

## The best-sourced of the four, confirmed independently

PKN is the only one of the four standards bodies added in the earlier
batch that publishes **its own page on cooperation with the European
standards organizations**. The other three rest on the CEN-CENELEC
membership rule. This pass adds independent confirmation from the other
side: standards.cencenelec.eu's own current member list, read directly,
names PKN by row for Poland.

That is a small difference and worth recording, because it is the difference
between a body's membership being stated by the organisation it belongs to
and being stated by the body itself — and here, this pass, by both.

**No [[INTL-ISO]] edge is asserted.** pkn.pl's own page, read directly,
makes no mention of ISO, only CEN, CENELEC and ETSI — consistent with the
reason given on [[BE-NBN]].

## Not modelled

- Any **standard** PKN maintains. That is now true of **seven** national
  standards bodies in the Atlas — [[DE-DIN]], [[NL-NEN]], [[GB-BSI]],
  [[IE-NSAI]] and the three others added with this one — none of which
  maintains a single document the Atlas holds. The exception is
  [[INTL-IDS-RAM]], which reaches [[DE-DIN]] from the other direction.
- PKN's **relationship to [[EU-ETSI]]**, which only [[GB-BSI]] carries.

## Relationships

- `participates-in` [[EU-CEN]] and [[EU-CENELEC]].

## Sources

Listed in frontmatter, all three read directly this pass.
