---
id: UN-ITU
type: organisation
name: International Telecommunication Union
alternative_names:
  - ITU
description: >
  UN specialised agency for information and communication technologies. It
  promotes shared global use of the radio spectrum, facilitates
  international cooperation in assigning satellite orbits, assists in
  developing and coordinating worldwide technical standards, and works to
  improve telecommunication infrastructure in the developing world.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - UN
  - UN-ITU-X509
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed by reading itu.int's own page directly (2026-08-28): the ITU became a UN specialised agency through a special agreement effective 1 January 1949, and participates in UN governance as an observer in the Main Committees of the General Assembly and ECOSOC, plus membership of the Chief Executive Board. The UN's own 'UN System' page (un.org/en/about-us/un-system), read directly 2026-11-22: 'The International Telecommunication Union is the United Nations specialized agency for information and communication technologies.' The OECD iLibrary source returned HTTP 403; an encyclopedia corroboration of the 1947 signature date was dropped from this evidence (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "The UN System"
    url: "https://www.un.org/en/about-us/un-system"
    publisher: "United Nations (un.org)"
    accessed: "2026-11-22"
  - title: "ITU as a UN Specialized Agency"
    url: "https://www.itu.int/en/un/Pages/un-agency.aspx"
    publisher: "International Telecommunication Union"
    accessed: "2026-08-28"
  - title: "International Telecommunication Union"
    url: "https://en.wikipedia.org/wiki/International_Telecommunication_Union"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# International Telecommunication Union (ITU)

> **Verified 2026-08-28.** itu.int's own page was read directly. The
> originally-cited OECD iLibrary page returned HTTP 403 on every attempt;
> per this batch's instruction to find alternate primary/secondary sources
> when a cited one is stuck, it is replaced here with Wikipedia's ITU
> article (also read directly), which independently corroborates the same
> 1949 UN-agency effective date. Two of two sources in the resulting list
> are now genuinely read.

## Description

The ITU is a **UN specialised agency** for information and communication
technologies. It promotes shared global use of the radio spectrum,
facilitates international cooperation in assigning satellite orbits, assists
in developing and coordinating worldwide technical standards, and works to
improve telecommunication infrastructure in developing countries. It has two
sectors central to digital standards.

## Why the UN scope matters here

Batch 13's brief warns explicitly: *"Do not incorrectly classify non-UN
organisations as UN organisations."* The ITU is the case where that warning
bites hardest, because it sits in standards-development listings alongside
[[INTL-ISO]], [[INTL-IEC]], [[INTL-W3C]], [[INTL-IETF]] and [[EU-ETSI]] —
company that makes it look like a peer standards body rather than a UN
organ.

It is nonetheless a UN specialised agency, confirmed by reading itu.int's own
page directly this pass, and therefore carries the **`UN` ID scope** while
the others carry `INTL`. The previously-cited ecosystem taxonomy — formal
international bodies based on national delegation (ISO, IEC, ITU), global
organisations with direct membership (IEEE, IETF, W3C), and European
organisations recognised by the EU (ETSI) — came from the OECD iLibrary
page, which was unreachable (HTTP 403) both in the original research and on
every retry this pass. It is plausible and consistent with how those bodies
are elsewhere described in this Atlas, but it is carried forward as an
**unconfirmed** characterisation rather than a verified one.

**Closed 2026-09-05:** [[UN-ITU-X509]], the Recommendation defining
public-key infrastructure (PKI) that underlies most digital certificate
systems in use today, is now modelled — jointly published as an
identical text with [[INTL-ISO]]/IEC as ISO/IEC 9594-8. `coverage`
remains `low` since only this one standard is modelled among ITU's much
larger output.

## Relationships

- Part of [[UN]] as a specialised agency.
- `maintained-by` edge (ITU as target) recorded on [[UN-ITU-X509]]'s own
  file, added 2026-09-05.

## Sources

Listed in frontmatter, both read directly this pass. The OECD iLibrary page
originally cited here is replaced with Wikipedia's ITU article after
repeated HTTP 403s.
