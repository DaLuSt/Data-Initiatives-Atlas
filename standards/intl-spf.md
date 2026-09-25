---
id: INTL-SPF
type: standard
name: "SPF — Sender Policy Framework"
alternative_names:
  - SPF
  - Sender Policy Framework
description: >
  IETF standard letting a domain administrator publish, in DNS, which
  mail servers are authorised to send email on the domain's behalf,
  published as RFC 7208 (April 2014, "Version 1"). Receiving mail
  servers check a message's sending host against the domain's
  published SPF record. Mandatory under the Netherlands' 'pas toe of
  leg uit' open-standards policy as protection against email phishing.

level: international
country: null
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2014-04-01
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
  - INTL-DKIM
  - INTL-DMARC
relationships:
  - type: maintained-by
    target: INTL-IETF
    source: fact
    evidence: "Confirmed by reading datatracker.ietf.org's own RFC 7208 text directly (2026-09-25): 'Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1', published April 2014, states 'ADministrative Management Domains (ADMDs) can explicitly authorize the hosts that are allowed to use their domain names, and a receiving host can check such authorization' by publishing and querying SPF records in DNS, checked against the MAIL FROM/HELO identities. forumstandaardisatie.nl's own 'verplicht' (mandatory) standards list, read directly, names 'SPF — Bescherming tegen e-mailphishing' (Version 1) and publisher IETF, mandatory under [[NL-PAS-TOE-OF-LEG-UIT]]. Closes part of `discovery/unresolved.md` row #165."
    confidence: high
    valid_from: 2014-04-01
    valid_until: null

sources:
  - title: "RFC 7208 — Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1"
    url: "https://datatracker.ietf.org/doc/html/rfc7208"
    publisher: "IETF Datatracker"
    accessed: "2026-09-25"
  - title: "SPF — Bescherming tegen e-mailphishing"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht"
    publisher: "Forum Standaardisatie"
    accessed: "2026-09-25"
---

# SPF (Sender Policy Framework)

> **Created 2026-09-25**, further closing `discovery/unresolved.md` row
> #165 alongside [[INTL-DNSSEC]], [[INTL-HTTPS-HSTS]], [[INTL-DKIM]] and
> [[INTL-DMARC]]. Sourced from the IETF's own RFC 7208 text and Forum
> Standaardisatie's own mandatory-standards list, both read directly.

## Description

Confirmed directly on the IETF's own text: RFC 7208 ("Sender Policy
Framework (SPF) for Authorizing Use of Domains in Email, Version 1",
April 2014) lets domain administrators — "ADministrative Management
Domains (ADMDs)" — **"explicitly authorize the hosts that are allowed to
use their domain names,"** publishing that authorisation as a DNS
record. A receiving mail server checks the sending host against the
domain's published SPF record before accepting a message on that
domain's behalf.

## Mandatory under Dutch policy, alongside DKIM and DMARC

Confirmed directly on Forum Standaardisatie's own "verplicht" list:
listed as **"SPF — Bescherming tegen e-mailphishing"** alongside
[[INTL-DKIM]] and [[INTL-DMARC]] under the same phishing-protection
heading, mandatory under [[NL-PAS-TOE-OF-LEG-UIT]].

## Relationships

- `maintained-by` [[INTL-IETF]].

## Sources

Listed in frontmatter, both read directly.
