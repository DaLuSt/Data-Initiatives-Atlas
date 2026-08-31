---
id: EE-CERT-EE
type: organisation
name: CERT-EE
alternative_names:
  - Computer Emergency Response Team Estonia
description: >
  Estonia's national computer emergency response team, operating as a
  department within RIA (the Information System Authority). It monitors
  Estonian cyberspace, provides preventive protection for the public
  sector, detects and handles cyber incidents in Estonia's computer
  networks, and acts as the national contact point for international
  cooperation on IT security. It began operations on 1 January 2006 and
  gained its first major test the following year, coordinating Estonia's
  response to the 2007 cyberattacks that followed the removal of the
  Bronze Soldier monument.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2006-01-01
end_date: null
last_verified: "2026-08-30"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations:
  - EE-RIA
related_entities:
  - EE-RIA
  - EE-KUBERTURVALISUSE-SEADUS
relationships:
  - type: part-of
    target: EE-RIA
    source: fact
    evidence: "Confirmed by reading ria.ee's own retrospective article directly (2026-08-30), published on CERT-EE's twentieth anniversary: CERT-EE is 'RIA's incident response department that monitors Estonian cyberspace, provides preventive protection for the public sector and detects cyber incidents in Estonia's computer networks', and 'began operations on January 1, 2006, marking its 20th anniversary on January 1, 2026'. The article names Toomas Viira, then RIA's head of information security, as having built the case for the unit through 2005 before it was approved, and describes its first major test — coordinating Estonia's response, with a team of two, to the 2007 cyberattacks following the removal of the Bronze Soldier monument, called in the article 'the world's first coordinated cyber campaign'."
    confidence: high
    valid_from: 2006-01-01
    valid_until: null

sources:
  - title: "CERT-EE: 20 years of protecting Estonia's cyberspace"
    url: "https://www.ria.ee/en/cert-ee-20-years-protecting-estonias-cyberspace"
    publisher: "Riigi Infosüsteemi Amet (RIA)"
    accessed: "2026-08-30"
  - title: "NIS 2 Directive | Transposition in Estonia"
    url: "https://www.nis-2-directive.com/Transposition/Estonia.html"
    publisher: "nis-2-directive.com"
    accessed: "2026-08-30"
---

# CERT-EE

> **Added 2026-08-30, `verification: primary-source` from creation.** RIA's
> own entity previously flagged this exact gap: "CERT-EE still has no
> Atlas entity of its own, the same gap recorded against [[NL-NCSC]],
> [[BE-CCB]] and [[DE-BSI]]'s counterparts." Two sources were read directly
> before this entity was written, including RIA's own twentieth-anniversary
> retrospective.

## Description

CERT-EE is Estonia's national computer emergency response team, run as a
department **within** [[EE-RIA]] rather than as a separate legal body.
Confirmed by reading `ria.ee`'s own retrospective article directly, it
"monitors Estonian cyberspace, provides preventive protection for the
public sector and detects cyber incidents in Estonia's computer networks,"
and RIA's own site elsewhere states RIA "is the National Cyber Security
Centre of Estonia (NCSC-EE)" with CERT-EE as the body handling incidents.

## Founded in 2006, tested in 2007

CERT-EE **began operations on 1 January 2006**, confirmed directly by
`ria.ee`'s own twentieth-anniversary article, published to mark that date
falling exactly twenty years earlier, on 1 January 2026. The unit's case
was built through 2005 by Toomas Viira, then RIA's head of information
security, before approval.

Its first major test came almost immediately: in 2007, following the
relocation of the Bronze Soldier monument, Estonia faced what the article
calls **"the world's first coordinated cyber campaign"** — coordinated at
the time by a CERT-EE team of just two people.

## One agency, several roles other countries split up

Confirmed by reading `nis-2-directive.com`'s Estonia transposition page
directly: under [[EE-KUBERTURVALISUSE-SEADUS]] (the NIS2-transposing
Cybersecurity Act), RIA "performs the functions of national competent
authority, cybersecurity regulator, and coordinator of incident response
through the national CERT capability (CERT-EE)" — CERT-EE is the
operational incident-response layer of a role the Atlas records as split
across multiple bodies elsewhere, e.g. [[BE-CCB]] in Belgium and [[DE-BSI]]
in Germany.

## Relationships

- `part-of` [[EE-RIA]].

No relationship to [[EE-KUBERTURVALISUSE-SEADUS]] is asserted directly from
this entity: the Act's oversight role is RIA's, described in prose above
rather than as a graph edge, since no source read names CERT-EE itself
(rather than RIA) as the Act's designated authority.

## Sources

Listed in frontmatter, both read directly.
