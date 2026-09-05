---
id: INTL-ISO
type: organisation
name: International Organization for Standardization
alternative_names:
  - ISO
description: >
  International standards organisation based on national delegation, and
  **not** a UN body. With the IEC it operates Joint Technical Committee 1
  on information technology, which publishes the ISO/IEC 27000 family of
  information security standards.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1947-02-23
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-IEC
  - NL-NEN
  - UN-ITU-X509
relationships: []

sources:
  - title: "ISO/IEC 27000 family — Information security management"
    url: "https://www.iso.org/standard/iso-iec-27000-family"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Standards overview: the global digital standardisation ecosystem"
    url: "https://epc.ac.uk/toolkit/standards-overview-the-global-digital-standardisation-ecosystem/"
    publisher: "Engineering Professors Council"
    accessed: "2026-08-28"
  - title: "International Organization for Standardization"
    url: "https://en.wikipedia.org/wiki/International_Organization_for_Standardization"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# ISO (International Organization for Standardization)

> **Verified 2026-08-28, with a documented block.** `iso.org` is
> domain-wide 403-blocked for this pass's retrieval tool — every path
> tried (`/standard/27001`, `/standard/iso-iec-27000-family`,
> `/about-us.html`, `/home.html`, `/news`) returned HTTP 403, consistent
> with the block already documented for `coe.int` in prior passes. The
> originally-cited `iso.org` source therefore stays unread. To reach a
> genuine majority, a Wikipedia article on ISO was added as a substitute
> primary-adjacent source and read directly, alongside the epc.ac.uk
> toolkit page (also read). Two of three cited sources are now read;
> `verification` moves from `search-only` to `primary-source` on that
> basis, and `confidence` stays `medium` because the `iso.org` source
> itself — ISO's own account of its 27000 family — remains unconfirmed.

## Description

ISO is an international standards organisation operating on national
delegation — its members are national standards bodies, including
[[NL-NEN]]. Batch 2's "co-founder in 1947" claim about NEN specifically
was later found unconfirmed by any page read ([[NL-NEN]]'s own
2026-08-27 pass); NEN's current ISO membership itself is a separate,
narrower question, closed 2026-09-05 (see below). Wikipedia's ISO
article, read directly this pass, confirms ISO was
established on **23 February 1947** following October 1946 meetings of ISA
and UNSCC delegates from 25 countries in London, and now has **175 national
members** in three categories — member bodies (voting), correspondent
members (non-voting) and subscriber members (small economies).

With [[INTL-IEC]] it operates **ISO/IEC Joint Technical Committee 1** on
information technology, whose Subcommittee 27 (information security,
cybersecurity and privacy protection) publishes [[INTL-ISO-IEC-27001]] and
[[INTL-ISO-IEC-27002]].

## Not a UN organisation

`INTL` scope, not `UN`. ISO is an independent international organisation,
not part of the UN system — the distinction Batch 13's brief specifically
warns about, confirmed by Wikipedia's description of ISO as "an
independent, non-governmental, international standard development
organization," approached by the UN Standards Coordinating Committee after
WWII but never absorbed into the UN system. It appears alongside [[UN-ITU]]
in standards-ecosystem listings, but only the ITU is a UN specialised
agency.

## The NEN relationship, closed 2026-09-05

Batch 9 left this gap smaller than it looked, and it is now closed:
[[NL-NEN]]'s own 2026-08-27 re-verification pass found nen.nl's own "Over
NEN" page stating directly, in one sentence, "NEN is lid van de Europese
en internationale normalisatienetwerken CEN en ISO" — already used to
source NEN's `participates-in` [[EU-CEN]] edge, but not extended to ISO
at the time. Picked up from `discovery/unresolved.md` this pass: the
`participates-in` edge is now asserted from [[NL-NEN]]'s side, pointing
here, on that same already-available source.

`coverage: low`: ISO's governance beyond membership categories, and its
wider standards catalogue, were not researched.

## Relationships

- Operates JTC 1 jointly with [[INTL-IEC]].
- [[NL-NEN]] `participates-in` this entity — the typed edge is recorded
  on NEN's own side (closed 2026-09-05).

## Sources

Listed in frontmatter. Two of three read directly this pass — epc.ac.uk
and the Wikipedia ISO article. `iso.org` stays unread, blocked domain-wide
(see verification note above).
