---
id: INTL-DMARC
type: standard
name: "DMARC — Domain-based Message Authentication, Reporting, and Conformance"
alternative_names:
  - DMARC
description: >
  IETF standard letting a mail-originating domain publish authentication
  and handling policies in DNS, published as RFC 7489 (March 2015). It
  ties together SPF and DKIM authentication results, requiring alignment
  with the visible From-address domain, and provides a feedback-reporting
  mechanism. Mandatory under the Netherlands' 'pas toe of leg uit'
  open-standards policy as protection against email phishing.

level: international
country: null
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2015-03-01
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
  - INTL-SPF
relationships:
  - type: maintained-by
    target: INTL-IETF
    source: fact
    evidence: "Confirmed by reading datatracker.ietf.org's own RFC 7489 text directly (2026-09-25): 'Domain-based Message Authentication, Reporting, and Conformance (DMARC)', published March 2015, is 'a scalable mechanism by which a mail-originating organization can express domain-level policies and preferences for message validation, disposition, and reporting,' requiring the From-field domain to align with domains validated by SPF and DKIM, and generating feedback reports to domain owners. forumstandaardisatie.nl's own 'verplicht' (mandatory) standards list, read directly, names 'DMARC — Bescherming tegen e-mailphishing' citing RFC 7489 and publisher IETF, mandatory under [[NL-PAS-TOE-OF-LEG-UIT]]. Closes part of `discovery/unresolved.md` row #165."
    confidence: high
    valid_from: 2015-03-01
    valid_until: null

sources:
  - title: "RFC 7489 — Domain-based Message Authentication, Reporting, and Conformance (DMARC)"
    url: "https://datatracker.ietf.org/doc/html/rfc7489"
    publisher: "IETF Datatracker"
    accessed: "2026-09-25"
  - title: "DMARC — Bescherming tegen e-mailphishing"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht"
    publisher: "Forum Standaardisatie"
    accessed: "2026-09-25"
---

# DMARC (Domain-based Message Authentication, Reporting, and Conformance)

> **Created 2026-09-25**, further closing `discovery/unresolved.md` row
> #165 alongside [[INTL-DNSSEC]], [[INTL-HTTPS-HSTS]] and [[INTL-DKIM]].
> Sourced from the IETF's own RFC 7489 text and Forum Standaardisatie's
> own mandatory-standards list, both read directly.

## Description

Confirmed directly on the IETF's own text: RFC 7489 (March 2015) is
**"a scalable mechanism by which a mail-originating organization can
express domain-level policies and preferences for message validation,
disposition, and reporting."** It ties SPF and DKIM together by
requiring their results to **align** with the domain visible in the
message's From field, and lets receivers send **feedback reports** back
to domain owners — functioning, in the RFC's own words, as "a mechanism
for policy distribution that enables increasingly strict handling of
messages that fail authentication checks, ranging from no action...
up to message rejection."

## Mandatory under Dutch policy, alongside DKIM and SPF

Confirmed directly on Forum Standaardisatie's own "verplicht" list:
listed as **"DMARC — Bescherming tegen e-mailphishing"** alongside
[[INTL-DKIM]] and [[INTL-SPF]] under the same phishing-protection
heading, mandatory under [[NL-PAS-TOE-OF-LEG-UIT]].

## Relationships

- `maintained-by` [[INTL-IETF]].

## Sources

Listed in frontmatter, both read directly.
