---
id: EU-LED
type: directive
name: Directive (EU) 2016/680
alternative_names:
  - Law Enforcement Directive
  - LED
  - Data Protection Law Enforcement Directive
description: >
  EU directive on the protection of natural persons with regard to the
  processing of personal data by competent authorities for the purposes
  of the prevention, investigation, detection or prosecution of criminal
  offences or the execution of criminal penalties, and on the free
  movement of such data. Adopted 27 April 2016 alongside the GDPR, which
  it complements: the GDPR governs general data processing, while this
  Directive governs processing by law enforcement authorities for
  criminal-justice purposes. Requires member states to designate
  independent supervisory authorities and to transpose its rules into
  national law, unlike the directly-applicable GDPR.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2016-04-27
end_date: null
last_verified: "2026-09-12"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-GDPR
  - IE-DPA-2018
  - EU-UK-ADEQUACY
relationships:
  - type: related-to
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading eur-lex.europa.eu's own TXT/HTML text of CELEX:32016L0680 directly (2026-09-12): adopted the same day as the GDPR (27 April 2016) as its complementary instrument — the GDPR applies to general data processing by public and private entities, while this Directive specifically addresses law enforcement processing for criminal purposes, with the GDPR applying when law enforcement authorities process data outside that mandate. Recorded as `related-to` rather than a directional type, since neither instrument implements or is governed by the other — they divide the same subject matter by scope."
    confidence: high
    valid_from: 2016-04-27
    valid_until: null

sources:
  - title: "Directive (EU) 2016/680 of the European Parliament and of the Council of 27 April 2016"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016L0680"
    publisher: "EUR-Lex"
    accessed: "2026-09-12"
---

# Directive (EU) 2016/680 — Law Enforcement Directive

> **Created 2026-09-12**, closing `discovery/unresolved.md` row #119: the
> Directive was named on [[IE-DPA-2018]] (Part 5 transposes it) and on
> [[EU-UK-ADEQUACY]] (one of its two legal bases) but left unmodelled
> since the UK batch. Read directly via EUR-Lex's TXT/HTML URL form,
> which works where other CELEX URL forms return a generic "today's
> Official Journal" redirect (a block already logged in
> `discovery/unresolved.md` row #223).

## Description

Confirmed by reading `eur-lex.europa.eu`'s own text of CELEX:32016L0680
directly: **Directive (EU) 2016/680**, adopted **27 April 2016** — the
same day as [[EU-GDPR]] — governs "the protection of natural persons with
regard to the processing of personal data by competent authorities for
the purposes of the prevention, investigation, detection or prosecution
of criminal offences or the execution of criminal penalties." Unlike the
directly-applicable GDPR, it requires member states to **transpose** its
rules into national law and to designate independent supervisory
authorities.

## Complementary to the GDPR, not implementing it

The two instruments divide the same subject matter by scope: the GDPR
covers general data processing by public and private bodies, while this
Directive covers **law enforcement processing** for criminal-justice
purposes — with the GDPR reasserting itself when a law enforcement body
processes data outside that specific mandate. Neither implements nor is
governed by the other, so the relationship recorded here is `related-to`.

## Where it surfaces in the Atlas

- [[IE-DPA-2018]] — **Part 5** of the Irish Data Protection Act 2018
  transposes this Directive, per that entity's own "Not modelled" note.
- [[EU-UK-ADEQUACY]] — one of the two legal bases (alongside the GDPR)
  for the European Commission's UK adequacy decisions, renewed
  19 December 2025.

## Relationships

- `related-to` [[EU-GDPR]] — complementary EU data-protection instrument,
  adopted the same day, dividing scope by processing purpose rather than
  one implementing the other.

[[IE-DPA-2018]] carries the inverse `implements-requirement-from` edge
pointing here, and [[EU-UK-ADEQUACY]] a second `governed-by` edge
alongside its existing one to [[EU-GDPR]] — both added on their own
files in this same batch, closing row #119 in full.

## Not modelled

- The Directive's substantive chapters (data subject rights, controller
  obligations, transfers to third countries) beyond the scope-dividing
  fact recorded above.

## Sources

Listed in frontmatter, read directly 2026-09-12.
