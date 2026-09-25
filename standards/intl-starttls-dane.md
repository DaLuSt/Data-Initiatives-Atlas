---
id: INTL-STARTTLS-DANE
type: standard
name: "STARTTLS and DANE — Secured connection between mail servers"
alternative_names:
  - STARTTLS
  - DANE
  - SMTP STARTTLS
description: >
  Combined IETF standards for securing mail-server-to-mail-server
  connections: the STARTTLS extension to SMTP (RFC 3207, February
  2002), which lets an SMTP client and server negotiate TLS on an
  existing plaintext connection, and DANE for SMTP (RFC 7672, October
  2015), which uses DNSSEC-validated TLSA records to make that TLS
  negotiation downgrade-resistant rather than merely opportunistic.
  Mandatory under the Netherlands' 'pas toe of leg uit' open-standards
  policy as "Beveiligde verbinding tussen mailservers" (secured
  connection between mail servers).

level: international
country: null
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2002-02-01
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
    evidence: "Confirmed by reading datatracker.ietf.org's own text of both RFCs directly (2026-09-25). RFC 3207 ('SMTP Service Extension for Secure SMTP over Transport Layer Security', February 2002) 'describes an extension to the SMTP... service that allows an SMTP server and client to use TLS... to provide private, authenticated communication,' defining the STARTTLS command and ESMTP keyword; it obsoletes RFC 2487. RFC 7672 ('SMTP Security via Opportunistic DNS-Based Authentication of Named Entities (DANE) Transport Layer Security (TLS)', October 2015) describes 'a downgrade-resistant protocol for SMTP transport security between Message Transfer Agents (MTAs), based on the DNS-Based Authentication of Named Entities (DANE) TLSA DNS record,' using DNSSEC-validated TLSA records to authenticate destination mail servers and resist man-in-the-middle attacks against plain STARTTLS. forumstandaardisatie.nl's own 'verplicht' (mandatory) standards list, read directly, names 'STARTTLS en DANE — Beveiligde verbinding tussen mailservers,' citing both RFCs and publisher IETF, mandatory under [[NL-PAS-TOE-OF-LEG-UIT]]. Closes part of `discovery/unresolved.md` row #165 — the last of the six mandatory IETF-originated standards on that list to be modelled."
    confidence: high
    valid_from: 2002-02-01
    valid_until: null

sources:
  - title: "RFC 3207 — SMTP Service Extension for Secure SMTP over Transport Layer Security"
    url: "https://datatracker.ietf.org/doc/html/rfc3207"
    publisher: "IETF Datatracker"
    accessed: "2026-09-25"
  - title: "RFC 7672 — SMTP Security via Opportunistic DANE TLS"
    url: "https://datatracker.ietf.org/doc/html/rfc7672"
    publisher: "IETF Datatracker"
    accessed: "2026-09-25"
  - title: "STARTTLS en DANE — Beveiligde verbinding tussen mailservers"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht"
    publisher: "Forum Standaardisatie"
    accessed: "2026-09-25"
---

# STARTTLS and DANE

> **Created 2026-09-25**, closing `discovery/unresolved.md` row #165 —
> the last of the six mandatory IETF-originated standards on Forum
> Standaardisatie's list to be modelled, alongside [[INTL-DNSSEC]],
> [[INTL-HTTPS-HSTS]], [[INTL-DKIM]], [[INTL-DMARC]] and [[INTL-SPF]].
> Sourced from the IETF's own text of both RFCs and Forum
> Standaardisatie's own mandatory-standards list, all read directly.

## Description

Confirmed directly on the IETF's own texts: **RFC 3207** ("SMTP Service
Extension for Secure SMTP over Transport Layer Security", February
2002) defines **STARTTLS**, letting an SMTP client and server negotiate
TLS on top of an existing plaintext connection — obsoleting the earlier
RFC 2487. **RFC 7672** ("SMTP Security via Opportunistic DANE TLS",
October 2015) adds **DANE**, described in the RFC's own words as **"a
downgrade-resistant protocol for SMTP transport security between
Message Transfer Agents (MTAs), based on the DNS-Based Authentication
of Named Entities (DANE) TLSA DNS record"** — using [[INTL-DNSSEC]]-
validated TLSA records so mail servers can authenticate each other
rather than trust an unauthenticated STARTTLS offer, closing the
man-in-the-middle weakness of plain opportunistic TLS.

## Mandatory under Dutch policy

Confirmed directly on Forum Standaardisatie's own "verplicht" list:
listed as **"STARTTLS en DANE — Beveiligde verbinding tussen
mailservers"** (secured connection between mail servers), citing both
RFCs, mandatory under [[NL-PAS-TOE-OF-LEG-UIT]].

## Relationships

- `maintained-by` [[INTL-IETF]].
- Depends on [[INTL-DNSSEC]] for the DANE half's authentication
  mechanism (described in prose; no typed edge asserted, since no
  source read this pass states it as a formal dependency rather than a
  technical building block).

## Sources

Listed in frontmatter, all three read directly.
