---
id: INTL-DNSSEC
type: standard
name: "DNSSEC — Domain Name System Security Extensions"
alternative_names:
  - DNSSEC
  - Domain Name System Security Extensions
description: >
  Set of IETF standards extending the Domain Name System with origin
  authentication and integrity protection for DNS data, published as
  RFC 4033, RFC 4034 and RFC 4035 (March 2005). It does not provide
  confidentiality or protection against denial-of-service attacks.
  Mandatory under the Netherlands' 'pas toe of leg uit' open-standards
  policy as the standard for domain-name security.

level: international
country: null
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2005-03-01
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations:
  - INTL-IETF
related_entities:
  - NL-PAS-TOE-OF-LEG-UIT
relationships:
  - type: maintained-by
    target: INTL-IETF
    source: fact
    evidence: "Confirmed by reading datatracker.ietf.org's own RFC 4033 text directly (2026-09-25): 'DNS Security Introduction and Requirements', published March 2005, states 'The DNS security extensions provide origin authentication and integrity protection for DNS data, as well as a means of public key distribution,' adding four new resource record types (RRSIG, DNSKEY, DS, NSEC) and explicitly disclaiming confidentiality or denial-of-service protection. forumstandaardisatie.nl's own 'verplicht' (mandatory) standards list, read directly, names 'DNSSEC — Domeinnaambeveiliging' with version citation 'RFC 4033, RFC4034, RFC4035' and publisher IETF, and lists it as one of the standards mandatory under [[NL-PAS-TOE-OF-LEG-UIT]]'s apply-or-explain policy. Closes part of `discovery/unresolved.md` row #165: the first IETF RFC modelled as an Atlas standard, connecting [[INTL-IETF]] to real content beyond its ISOC relationship."
    confidence: high
    valid_from: 2005-03-01
    valid_until: null

sources:
  - title: "RFC 4033 — DNS Security Introduction and Requirements"
    url: "https://datatracker.ietf.org/doc/html/rfc4033"
    publisher: "IETF Datatracker"
    accessed: "2026-09-25"
  - title: "DNSSEC — Domeinnaambeveiliging"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht"
    publisher: "Forum Standaardisatie"
    accessed: "2026-09-25"
---

# DNSSEC (Domain Name System Security Extensions)

> **Created 2026-09-25**, narrowing `discovery/unresolved.md` row #165
> — the first IETF RFC modelled as an Atlas standard, closing the gap
> [[INTL-IETF]]'s own file flagged: "a properly researched IETF entity
> would connect to real content. That connection is queued, not
> asserted." Sourced from the IETF's own RFC 4033 text and Forum
> Standaardisatie's own mandatory-standards list, both read directly.

## Description

DNSSEC is a set of extensions to the Domain Name System, published as
**RFC 4033, RFC 4034 and RFC 4035** in **March 2005**. Confirmed directly
on the IETF's own RFC 4033 text: it provides **"origin authentication and
integrity protection for DNS data, as well as a means of public key
distribution,"** through four new resource record types (RRSIG, DNSKEY,
DS, NSEC). The RFC itself is explicit about what DNSSEC does **not** do:
no confidentiality, and **"no protection against denial of service
attacks."**

## Mandatory under Dutch policy

Confirmed directly on Forum Standaardisatie's own "verplicht" (mandatory)
standards list: DNSSEC appears there as **"Domeinnaambeveiliging"**
(domain-name security), citing the same three RFCs and naming the IETF
as publisher. It is one of several IETF-originated standards
[[NL-PAS-TOE-OF-LEG-UIT]] mandates for Dutch (semi-)government ICT
procurement above the policy's €50,000 threshold — the specific
connection [[INTL-IETF]]'s own file had flagged as real but unmodelled.

## Not modelled

- The other IETF-originated standards on the same mandatory list —
  HTTPS/HSTS (RFC 9110, RFC 6797), DKIM (RFC 6376), DMARC (RFC 7489),
  SPF, and STARTTLS/DANE (RFC 3207, RFC 7672) — all confirmed present on
  the same Forum Standaardisatie page but not created as entities this
  pass. DNSSEC was chosen as the first because item #165's own text
  named it specifically.
- No `applies-to` or similar edge is asserted from
  [[NL-PAS-TOE-OF-LEG-UIT]] to this entity; the connection is recorded
  via `related_entities` and this entity's own prose for now.

## Relationships

- `maintained-by` [[INTL-IETF]].

## Sources

Listed in frontmatter, both read directly.
