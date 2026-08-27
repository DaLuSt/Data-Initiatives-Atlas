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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading logius.nl's own Digikoppeling pages directly (2026-08-27): Logius 'manages the Digikoppeling standard' and is 'responsible for the development and management of government-wide standards' regarding its use, including inquiries, complaints, change requests and monitoring the Compliance facility and CPA Register. gitdocumentatie.logius.nl's own Architecture 2.0.1 document, also read directly, confirms it was 'established as an official standard by Logius on August 12, 2022.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-PAS-TOE-OF-LEG-UIT
    source: fact
    evidence: "The claim that Digikoppeling 2.0 appears on the comply-or-explain list was not re-confirmed by any page read directly this pass — logius.nl's own pages describe governance and responsibilities but do not state comply-or-explain status in the text read, and vngrealisatie.nl returned HTTP 404. Carried over from the prior text as unconfirmed rather than deleted; `confidence` lowered accordingly."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Digikoppeling"
    url: "https://www.logius.nl/onze-dienstverlening/gegevensuitwisseling/digikoppeling"
    publisher: "Logius"
    accessed: "2026-08-27"
  - title: "Wie doet wat voor Digikoppeling?"
    url: "https://www.logius.nl/onze-dienstverlening/gegevensuitwisseling/digikoppeling/wie-doet-wat"
    publisher: "Logius"
    accessed: "2026-08-27"
  - title: "Digikoppeling Architectuur 2.0.1"
    url: "https://gitdocumentatie.logius.nl/publicatie/dk/architectuur/2.0.1/"
    publisher: "Logius"
    accessed: "2026-08-27"
  - title: "Digikoppeling (confirmed dead, HTTP 404)"
    url: "https://www.vngrealisatie.nl/index.php/producten/digikoppeling"
    publisher: "VNG Realisatie"
---

# Digikoppeling

> **Verified 2026-08-27.** Three of four cited pages were read directly;
> vngrealisatie.nl returned HTTP 404 — confirmed genuinely dead, not
> silently dropped. `verification` moves from `search-only` to
> `primary-source` on the strength of the three direct reads; the
> comply-or-explain-list claim, which rested on the dead page, is
> downgraded to `confidence: low` rather than dropped.

## Description

Digikoppeling is a set of standards carrying the logistical agreements for
electronic message traffic between government organisations, and between
government organisations and organisations with a public task. Confirmed
by reading logius.nl directly: "like a letter in an envelope for mailing,
so an electronic message goes in a digital packaging. This digital
packaging is Digikoppeling" — the framework does not concern itself with
message content, which is the business of sector standards such as those
maintained by [[NL-GEONOVUM]] or in the municipal domain.

It supports signing and/or encrypting individual messages, with transport
over an encrypted (TLS) connection. Confirmed by reading Architecture 2.0.1
directly: the standard, finalised by Logius on **12 August 2022**, defines
three primary interface standards — WUS (web services), ebMS2 (reliable
messaging) and REST APIs — plus a large-file-transfer standard, and applies
to government-to-government (G2G) exchange of "closed data" requiring
authentication between known parties.

Digikoppeling is one of the Stelselvoorzieningen and is managed by
[[NL-LOGIUS]], confirmed directly this pass — logius.nl's own "wie doet
wat" page details Logius's responsibilities (inquiries, change requests,
governance, monitoring the Compliance facility and CPA Register) versus
users' own responsibilities (their ICT infrastructure, their Service
Register domain). **The claim that Digikoppeling 2.0 appears on the
[[NL-PAS-TOE-OF-LEG-UIT]] comply-or-explain list could not be re-confirmed**
this pass: neither logius.nl page read states this, and vngrealisatie.nl —
the source that would have — returned HTTP 404. It is kept in the text as
an unconfirmed carry-over rather than deleted, with `confidence: low` on
that specific relationship.

**A historical note worth flagging.** One source describes Digikoppeling as
being on the comply-or-explain list "of the College Standaardisatie", while
Batch 1 sources describe the [[NL-OBDO]] as the deciding body. This is
consistent with the College having been the earlier decision-making body,
later succeeded by the OBDO — which would resolve the open question about
the College's status recorded in `discovery/unresolved.md`. It is
corroboration, not confirmation, and the question stays open.

## Relationships

- Maintained by [[NL-LOGIUS]] — confirmed this pass, with a precise date
  (12 August 2022) for the current architecture version.
- Part of the [[NL-PAS-TOE-OF-LEG-UIT]] mandatory standards list — carried
  over unconfirmed this pass; its sole supporting source is now dead.
- A Stelselvoorziening within [[NL-GDI]].

## Sources

Listed in frontmatter, three of four read directly this pass.
vngrealisatie.nl is confirmed genuinely dead (HTTP 404).
