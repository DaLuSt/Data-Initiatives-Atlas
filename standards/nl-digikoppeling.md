---
id: NL-DIGIKOPPELING
type: standard
name: Digikoppeling
alternative_names: []
description: >
  Dutch set of standards containing logistical agreements for electronic
  message exchange between government organisations and organisations with a
  public task. It governs the technical framework for secure exchange rather
  than message content, and has been extended with a standard for REST-API
  interfaces.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-LOGIUS
related_entities:
  - NL-GDI
  - NL-PAS-TOE-OF-LEG-UIT
relationships:
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "Digikoppeling is one of the Stelselvoorzieningen and is managed by Logius (logius.nl Digikoppeling pages). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-PAS-TOE-OF-LEG-UIT
    source: fact
    evidence: "Digikoppeling 2.0 is included on the 'pas toe of leg uit' list of mandatory open standards (vngrealisatie.nl; logius.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Digikoppeling"
    url: "https://www.logius.nl/onze-dienstverlening/gegevensuitwisseling/digikoppeling"
    publisher: "Logius"
  - title: "Wie doet wat voor Digikoppeling?"
    url: "https://www.logius.nl/onze-dienstverlening/gegevensuitwisseling/digikoppeling/wie-doet-wat"
    publisher: "Logius"
  - title: "Digikoppeling Architectuur 2.0.1"
    url: "https://gitdocumentatie.logius.nl/publicatie/dk/architectuur/2.0.1/"
    publisher: "Logius"
  - title: "Digikoppeling"
    url: "https://www.vngrealisatie.nl/index.php/producten/digikoppeling"
    publisher: "VNG Realisatie"
---

# Digikoppeling

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Digikoppeling is a set of standards carrying the logistical agreements for
electronic message traffic between government organisations, and between
government organisations and organisations with a public task. Its scope is
deliberately narrow: it concerns the technical framework for secure
exchange, not the content of the messages — content semantics are the
business of sector standards such as those maintained by
[[NL-GEONOVUM]] or in the municipal domain.

It supports signing and/or encrypting individual messages, with transport
over an encrypted (TLS) connection, and has been extended with a standard
for REST-API interfaces enabling government organisations to share data
securely via REST APIs.

Digikoppeling is one of the Stelselvoorzieningen and is managed by
[[NL-LOGIUS]]. Digikoppeling 2.0 appears on the mandatory
[[NL-PAS-TOE-OF-LEG-UIT]] list.

**A historical note worth flagging.** One source describes Digikoppeling as
being on the comply-or-explain list "of the College Standaardisatie", while
Batch 1 sources describe the [[NL-OBDO]] as the deciding body. This is
consistent with the College having been the earlier decision-making body,
later succeeded by the OBDO — which would resolve the open question about
the College's status recorded in `discovery/unresolved.md`. It is
corroboration, not confirmation, and the question stays open.

## Relationships

- Maintained by [[NL-LOGIUS]].
- Part of the [[NL-PAS-TOE-OF-LEG-UIT]] mandatory standards list.
- A Stelselvoorziening within [[NL-GDI]].

## Sources

Listed in frontmatter.
