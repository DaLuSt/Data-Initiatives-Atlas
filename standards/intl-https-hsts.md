---
id: INTL-HTTPS-HSTS
type: standard
name: "HTTPS and HSTS — Secure website connection"
alternative_names:
  - HTTPS
  - HSTS
  - HTTP Strict Transport Security
description: >
  Combined IETF standards for secure web connections: HTTP Semantics
  (RFC 9110, June 2022), which defines the "https" URI scheme among
  HTTP's core protocol elements, and HTTP Strict Transport Security
  (RFC 6797, November 2012), which lets a website declare itself
  accessible only over secure connections via the Strict-Transport-
  Security response header. Mandatory under the Netherlands' 'pas toe
  of leg uit' open-standards policy as "Beveiligde websiteverbinding"
  (secured website connection).

level: international
country: null
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2012-11-01
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
  - INTL-DNSSEC
relationships:
  - type: maintained-by
    target: INTL-IETF
    source: fact
    evidence: "Confirmed by reading datatracker.ietf.org's own text of both RFCs directly (2026-09-25). RFC 9110 ('HTTP Semantics', June 2022) 'describes the overall architecture of HTTP... In this definition are core protocol elements, extensibility mechanisms, and the \"http\" and \"https\" Uniform Resource Identifier (URI) schemes,' obsoleting nine prior RFCs to consolidate HTTP semantics. RFC 6797 ('HTTP Strict Transport Security (HSTS)', November 2012) establishes 'a mechanism enabling web sites to declare themselves accessible only via secure connections,' via the Strict-Transport-Security response header, forcing browsers to upgrade HTTP references to HTTPS and to refuse to bypass certificate errors. forumstandaardisatie.nl's own 'verplicht' (mandatory) standards list, read directly, names 'HTTPS en HSTS — Beveiligde websiteverbinding,' citing 'RFC 9110 en RFC 6797' and publisher IETF, mandatory under [[NL-PAS-TOE-OF-LEG-UIT]]. Second and third IETF RFC-pair modelled as Atlas standards, alongside [[INTL-DNSSEC]], closing `discovery/unresolved.md` row #165."
    confidence: high
    valid_from: 2012-11-01
    valid_until: null

sources:
  - title: "RFC 9110 — HTTP Semantics"
    url: "https://datatracker.ietf.org/doc/html/rfc9110"
    publisher: "IETF Datatracker"
    accessed: "2026-09-25"
  - title: "RFC 6797 — HTTP Strict Transport Security (HSTS)"
    url: "https://datatracker.ietf.org/doc/html/rfc6797"
    publisher: "IETF Datatracker"
    accessed: "2026-09-25"
  - title: "HTTPS en HSTS — Beveiligde websiteverbinding"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht"
    publisher: "Forum Standaardisatie"
    accessed: "2026-09-25"
---

# HTTPS and HSTS

> **Created 2026-09-25**, further closing `discovery/unresolved.md` row
> #165 alongside [[INTL-DNSSEC]]. Sourced from the IETF's own text of
> both RFCs and Forum Standaardisatie's own mandatory-standards list, all
> read directly.

## Description

Confirmed directly on the IETF's own texts: **RFC 9110** ("HTTP
Semantics", June 2022) defines the **"https" URI scheme** among HTTP's
core protocol elements, consolidating semantics previously scattered
across nine now-obsolete RFCs. **RFC 6797** ("HTTP Strict Transport
Security", November 2012) lets a website declare itself accessible
**only** over secure connections, via the **Strict-Transport-Security**
response header — once received, a browser upgrades HTTP links to
HTTPS and refuses to let users bypass certificate warnings for that
site.

## Mandatory under Dutch policy

Confirmed directly on Forum Standaardisatie's own "verplicht" list:
listed as **"HTTPS en HSTS — Beveiligde websiteverbinding"** (secured
website connection), citing both RFCs by number, mandatory under
[[NL-PAS-TOE-OF-LEG-UIT]] for Dutch (semi-)government ICT procurement.

## Relationships

- `maintained-by` [[INTL-IETF]].

## Sources

Listed in frontmatter, all three read directly.
