---
id: LU-CIRCL
type: organisation
name: Computer Incident Response Center Luxembourg
alternative_names:
  - CIRCL
description: >
  Luxembourg's CSIRT (Computer Security Incident Response Team) for the
  private sector, communes and non-governmental entities — a
  government-driven initiative operated by the Luxembourg House of
  Cybersecurity (an economic interest grouping). It is a CVE Numbering
  Authority under the ENISA CVE Root, and is designated as one of
  Luxembourg's two CSIRTs under the country's NIS2 transposition act,
  alongside GOVCERT.LU for the public sector.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-12"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - LU-LHC
  - LU-GOVCERT
  - LU-LOI-NIS2
relationships:
  - type: maintained-by
    target: LU-LHC
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #181; LU-CTIE, LU-LOI-NIS2). Confirmed by reading circl.lu directly (2026-09-12), via its own copyright attribution, and securitymadein.lu's own agency page, also read directly: 'a government-driven initiative' operated as one of LHC's two centres, the CERT for 'the private sector, communes and non-governmental entities in Luxembourg.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "CIRCL — Computer Incident Response Center Luxembourg"
    url: "https://www.circl.lu/"
    publisher: "CIRCL"
    accessed: "2026-09-12"
  - title: "The Cybersecurity Agency"
    url: "https://www.securitymadein.lu/agency/"
    publisher: "Luxembourg House of Cybersecurity (LHC) / SECURITYMADEIN.LU"
    accessed: "2026-09-12"
  - title: "CIRCL"
    url: "https://securitymadein.lu/agency/circl/"
    publisher: "Luxembourg House of Cybersecurity (LHC) / SECURITYMADEIN.LU"
    accessed: "2026-09-12"
---

# Computer Incident Response Center Luxembourg (CIRCL)

> **Created 2026-09-12**, closing part of `discovery/unresolved.md` row
> #181: CIRCL was named in secondary NIS2 sourcing on [[LU-CTIE]] and
> [[LU-LOI-NIS2]] but unmodelled. CIRCL's own site and two Luxembourg
> House of Cybersecurity pages were read directly.

## Description

Confirmed by reading `circl.lu` directly: CIRCL is "a government-driven
initiative" and "the CERT ... for the private sector, communes and
non-governmental entities in Luxembourg" — the counterpart to
[[LU-GOVCERT]], which covers the public sector. It is also a **CVE
Numbering Authority (CNA)** under the ENISA CVE Root, confirmed on the
same page.

## Operator

Confirmed by reading `securitymadein.lu`'s own agency pages directly:
CIRCL is one of two centres operated by [[LU-LHC]] (Luxembourg House of
Cybersecurity), an economic interest grouping overseen by Luxembourg's
Ministry of the Economy. CIRCL's own legal form and founding date were
not found on either page — CIRCL is operated by, but not itself
independently incorporated as, LHC.

## One of Luxembourg's two CSIRTs under NIS2

Per [[LU-LOI-NIS2]] and secondary tracking sources (`nisd2.eu`), CIRCL
and [[LU-GOVCERT]] are named as Luxembourg's two CSIRTs, splitting
private- and public-sector coverage respectively.

## Relationships

- `maintained-by` [[LU-LHC]] — its operator, per LHC's own site.

## Not modelled

- CIRCL's own legal form and founding date, if distinct from [[LU-LHC]]'s
  own 5 May 2010 date — not stated on either page read this pass.

## Sources

Listed in frontmatter, all three read directly 2026-09-12.
