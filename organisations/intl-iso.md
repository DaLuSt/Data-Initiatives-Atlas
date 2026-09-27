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
coverage: medium
verification: primary-source

start_date: 1947-02-23
end_date: null
last_verified: "2026-09-27"
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
    note: "This exact landing page remains genuinely bot-walled (domain-wide iso.org 403). Substituted 2026-09-27 with a direct read of the standard it describes, ISO/IEC 27000:2018 itself, via standards.iteh.ai's free redline preview PDF (catalog 73906, https://cdn.standards.iteh.ai/samples/73906/5617255f98eb4621b8d8adaa844a8c1b/ISO-IEC-27000-2018.pdf) — the same workaround already used to close INTL-ISO-IEC-27001 and -27002 (discovery/unresolved.md row #220)."
  - title: "Standards overview: the global digital standardisation ecosystem"
    url: "https://epc.ac.uk/toolkit/standards-overview-the-global-digital-standardisation-ecosystem/"
    publisher: "Engineering Professors Council"
    accessed: "2026-08-28"
  - title: "International Organization for Standardization"
    url: "https://en.wikipedia.org/wiki/International_Organization_for_Standardization"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "ISO/IEC 27000:2018 — redline preview PDF (catalog 73906)"
    url: "https://cdn.standards.iteh.ai/samples/73906/5617255f98eb4621b8d8adaa844a8c1b/ISO-IEC-27000-2018.pdf"
    publisher: "standards.iteh.ai (authorized ISO/IEC standards reseller)"
    accessed: "2026-09-27"
    note: "Read directly to substitute for the still-bot-walled iso.org family landing page above. Its own Introduction and Clause 5 list the ISMS family of standards by number (ISO/IEC 27000 through 27019, plus ISO 27799) and its Foreword confirms preparation by 'Technical Committee ISO/IEC JTC 1, Information technology, SC 27, IT Security techniques.'"
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
>
> **Closed 2026-09-27**: the `iso.org` family landing page itself remains
> bot-walled, but `standards.iteh.ai`'s free redline preview PDF of the
> standard it describes, ISO/IEC 27000:2018 (the same workaround already
> used to close [[INTL-ISO-IEC-27001]] and [[INTL-ISO-IEC-27002]], row
> #220), gives a genuine primary-source read of the ISMS family list —
> see "The ISMS family, read directly" below. 3 of 4 sources now read
> directly.

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

## The ISMS family, read directly — 2026-09-27

The redline preview PDF of ISO/IEC 27000:2018 itself, read via the
standards.iteh.ai workaround, gives the ISMS family in the standard's own
words (Clause 5, "ISMS family of standards"): **ISO/IEC 27000** (this
standard, overview and vocabulary), **27001** (requirements), **27002**
(controls), **27003** (implementation guidance), **27004** (measurement),
**27005** (risk management), **27006** (certification-body requirements),
**27007** (auditing guidelines), **27008** (TR, auditor guidelines on
controls), **27009** (sector-specific application), **27010**
(inter-sector/inter-organizational communications), **27011**
(telecommunications), **27013** (integration with ISO/IEC 20000-1),
**27014** (governance), **27015** (TR, financial services), **27016**
(TR, organizational economics), **27017**–**27019** (cloud, PII
protection, energy-utility process control) — plus **ISO 27799**
(health informatics), named as part of the family without carrying the
same general title. Only two of these, 27001 and 27002, are Atlas
entities; the rest are named here for completeness rather than
individually modelled.

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

`coverage` raised low→medium 2026-09-27: the standards catalogue gap is
now partly closed for the one family this Atlas tracks (see above). ISO's
governance beyond membership categories remains unresearched.

## Relationships

- Operates JTC 1 jointly with [[INTL-IEC]].
- [[NL-NEN]] `participates-in` this entity — the typed edge is recorded
  on NEN's own side (closed 2026-09-05).

## Sources

Listed in frontmatter. **3 of 4 now read directly.** epc.ac.uk and the
Wikipedia ISO article (2026-08-28 pass); and, closing part of this file
2026-09-27, `standards.iteh.ai`'s redline preview PDF of ISO/IEC
27000:2018 itself, substituting for the still-bot-walled `iso.org`
family landing page (the same workaround already used for
[[INTL-ISO-IEC-27001]] and [[INTL-ISO-IEC-27002]], `discovery/unresolved.md`
row #220).
