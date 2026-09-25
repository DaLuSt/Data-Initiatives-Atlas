---
id: INTL-DKIM
type: standard
name: "DKIM — DomainKeys Identified Mail"
alternative_names:
  - DKIM
  - DomainKeys Identified Mail
description: >
  IETF standard for cryptographic email authentication, published as
  RFC 6376 (September 2011). It permits a domain owner to sign
  outgoing mail with a private key, letting recipients verify
  authenticity against a public key published in DNS. Mandatory under
  the Netherlands' 'pas toe of leg uit' open-standards policy as
  protection against email phishing.

level: international
country: null
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2011-09-01
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
  - INTL-DMARC
  - INTL-SPF
relationships:
  - type: maintained-by
    target: INTL-IETF
    source: fact
    evidence: "Confirmed by reading datatracker.ietf.org's own RFC 6376 text directly (2026-09-25): 'DomainKeys Identified Mail (DKIM) Signatures', published September 2011, 'permits a person, role, or organization that owns the signing domain to claim some responsibility for a message by associating the domain with the message,' via cryptographic signature (rsa-sha1/rsa-sha256), with the public key distributed through DNS. forumstandaardisatie.nl's own 'verplicht' (mandatory) standards list, read directly, names 'DKIM — Bescherming tegen e-mailphishing' citing RFC 6376 and publisher IETF, mandatory under [[NL-PAS-TOE-OF-LEG-UIT]]. Closes part of `discovery/unresolved.md` row #165, alongside [[INTL-DNSSEC]] and [[INTL-HTTPS-HSTS]]."
    confidence: high
    valid_from: 2011-09-01
    valid_until: null

sources:
  - title: "RFC 6376 — DomainKeys Identified Mail (DKIM) Signatures"
    url: "https://datatracker.ietf.org/doc/html/rfc6376"
    publisher: "IETF Datatracker"
    accessed: "2026-09-25"
  - title: "DKIM — Bescherming tegen e-mailphishing"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht"
    publisher: "Forum Standaardisatie"
    accessed: "2026-09-25"
---

# DKIM (DomainKeys Identified Mail)

> **Created 2026-09-25**, further closing `discovery/unresolved.md` row
> #165 alongside [[INTL-DNSSEC]] and [[INTL-HTTPS-HSTS]]. Sourced from
> the IETF's own RFC 6376 text and Forum Standaardisatie's own
> mandatory-standards list, both read directly.

## Description

Confirmed directly on the IETF's own text: RFC 6376 ("DomainKeys
Identified Mail (DKIM) Signatures", September 2011) **"permits a
person, role, or organization that owns the signing domain to claim
some responsibility for a message by associating the domain with the
message."** A sender cryptographically signs outgoing mail with the
domain's private key; recipients verify authenticity against the
corresponding public key, published in the domain's own DNS records.

## Mandatory under Dutch policy, alongside DMARC and SPF

Confirmed directly on Forum Standaardisatie's own "verplicht" list:
listed as **"DKIM — Bescherming tegen e-mailphishing"** (protection
against email phishing) alongside [[INTL-DMARC]] and [[INTL-SPF]] under
the same phishing-protection heading, mandatory under
[[NL-PAS-TOE-OF-LEG-UIT]].

## Relationships

- `maintained-by` [[INTL-IETF]].

## Sources

Listed in frontmatter, both read directly.
