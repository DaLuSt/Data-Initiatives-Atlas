---
id: DE-DIN
type: organisation
name: DIN Deutsches Institut für Normung
alternative_names:
  - DIN
  - German Institute for Standardisation
description: >
  National standards body of the Federal Republic of Germany, founded on
  22 December 1917 as the Normenausschuss der deutschen Industrie (renamed
  Deutscher Normenausschuss in 1926, and DIN in 1975 when it signed an
  agreement with the German federal government recognising it as the
  national standards body). It is the recognised national standards
  organisation representing German interests in European and international
  standardisation. It has been the German member of ISO since 1951 and is a
  member of CEN.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 1917-12-22
end_date: null
last_verified: "2026-09-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-ISO
  - EU-CEN
  - DE-DKE
relationships:
  - type: participates-in
    target: INTL-ISO
    source: fact
    evidence: "DIN has been the ISO member body for the Federal Republic of Germany since 1951 and is listed as such by ISO (iso.org/member/1511.html; de.wikipedia.org 'Internationale Organisation für Normung'). The ISO member-directory page returned HTTP 403 on two attempts this pass and could not be re-fetched directly; din.de's own history page, read directly this pass, independently confirms DIN's role as Germany's internationally-representing standards body without itself giving the 1951 ISO accession date, so that specific year remains sourced to the previous pass's unread ISO page rather than confirmed by a direct read this pass. Corroborated from ISO's own side 2026-09-27: iso.org/member/1511.html itself remains genuinely bot-walled, but committee.iso.org/iso/home/about/iso_members.htm — a different, reachable iso.org subdomain (the workaround documented in discovery/unresolved.md row #220) — lists 'Germany DIN Member body' with 785 TC and 3 PDC participations, confirming current full voting membership directly. This does not confirm the specific 1951 accession year, which still rests on the unread member-directory page and is carried as previously sourced."
    confidence: high
    valid_from: 1951-01-01
    valid_until: null
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Confirmed by reading telusio.com directly (2026-08-28): DIN 'is a member of both ISO and CEN, ensuring that German interests in international and European standardization processes are represented,' and DIN standards are increasingly superseded by ISO or EN standards through harmonisation. din.de's own history page, also read directly, confirms DIN's role as Germany's recognised standards organisation without itself naming CEN specifically."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "DIN — DIN Deutsches Institut für Normung e.V. (ISO member body)"
    url: "https://www.iso.org/member/1511.html"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Deutsches Institut für Normung (DIN)"
    url: "https://www.quality.de/lexikon/deutsches-institut-fuer-normung/"
    publisher: "Quality.de"
  - title: "Normungsorganisationen im Vergleich: ISO, DIN und EN"
    url: "https://www.telusio.com/normungsorganisationen"
    publisher: "Telusio"
    accessed: "2026-08-28"
  - title: "Das ist Norm — DIN"
    url: "https://blog.dnb.de/das-ist-norm-din/"
    publisher: "Deutsche Nationalbibliothek (DNB)"
    accessed: "2026-08-28"
  - title: "Die Geschichte von DIN"
    url: "https://www.din.de/en/din-and-our-partners/din-e-v/history"
    publisher: "DIN Deutsches Institut für Normung"
    accessed: "2026-08-28"
  - title: "ISO — Members"
    url: "https://committee.iso.org/iso/home/about/iso_members.htm"
    publisher: "International Organization for Standardization (ISO)"
    accessed: "2026-09-27"
    note: "A different, reachable iso.org subdomain, found this pass, substituting for the still-bot-walled iso.org/member/1511.html page above — the workaround documented in discovery/unresolved.md row #220. Its member table lists Germany/DIN as a full voting 'Member body' with 785 TC and 3 PDC participations, the highest TC-participation count of any national standards body cited in this Atlas. It does not give an accession date."
---

# DIN Deutsches Institut für Normung

> **Re-verified 2026-08-28.** Three of five cited pages read directly,
> including — closing the previously-flagged gap ("DIN's own site is not
> cited") — DIN's own history page, found via targeted search.
> `iso.org`'s member-directory page returned HTTP 403 on two attempts and
> `quality.de` returned genuinely empty content on two attempts (not a
> paywall message, just no extractable text); both are treated as
> unreadable this pass rather than silently dropped. `verification:
> primary-source`; `confidence` raised to `high`; the founding date is now
> precise to the day.
>
> **Closed 2026-09-27**: `iso.org/member/1511.html` itself remains
> bot-walled, but `committee.iso.org` — a different, reachable `iso.org`
> subdomain found this pass (`discovery/unresolved.md` row #220) —
> confirms DIN's current ISO membership directly (785 TC participations,
> the highest of any national body this Atlas tracks), though not the
> specific 1951 accession year. `confidence` on the ISO edge raised
> medium→high. This same pass also found that [[NL-NEN]]'s ISO membership
> **is** now recorded — the "asymmetry" section below, unchanged since
> 2026-08-28, was stale; see the correction inline.

## Description

DIN's own history page, read directly this pass, gives a fuller and more
precise account than the entity previously carried: founded **22 December
1917** as the *Normenausschuss der deutschen Industrie (NADI)*, renamed
*Deutscher Normenausschuss (DNA)* in 1926, and renamed again to its current
**DIN** designation in **1975** — the same year DIN and the German federal
government **signed an agreement recognising DIN as the national standards
body for Germany**, confirmed directly in the source's own words. This is
the specific agreement the entity's description previously referred to only
generically ("by agreement with the German federal government").

It has been the German member of [[INTL-ISO]] since **1951** and is a
member of [[EU-CEN]] — the CEN membership now confirmed directly this pass
via telusio.com, read directly, which states DIN "is a member of both ISO
and CEN, ensuring that German interests in international and European
standardization processes are represented," and that DIN's own national
standards increasingly apply "only in areas where no ISO or EN standards
exist," reflecting a trend toward international harmonisation. The 1951
ISO-accession year itself still rests on the ISO member-directory page,
which could not be re-fetched this pass (HTTP 403 on two attempts) —
`confidence` on that specific edge stays `medium` for that reason, even
though the entity as a whole is now well-sourced enough for
`verification: primary-source`.

## The most valuable structural entity in the German batch

This entity earns its place less for what it says about DIN than for what
it does to the graph.

Before Germany, the Atlas had **two** international→national descents, both
noted in Batch 15 as "the template for what the UN layer lacks":

```
INTL-DCAT (W3C)            → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL
INTL-ISO-IEC-27001 / -27002 → NL-BIO
```

DIN adds a third shape — not a standards descent but an **institutional
membership chain**, and the first one in the Atlas that runs from a
national body up to both the European and the international standards
layer:

```
DE-DIN ──participates-in──> EU-CEN
       └─participates-in──> INTL-ISO
```

This matters because [[NL-NEN]] is the Dutch equivalent, and this section
used to describe an asymmetry: Germany's ISO membership recorded, the
Netherlands' refused for want of a source (Batch 14). **That asymmetry is
now stale and corrected 2026-09-27**: [[NL-NEN]]'s own "Over NEN" page,
read directly in a later pass (2026-08-27, closing `discovery/unresolved.md`'s
NEN-ISO question), states plainly "NEN is lid van de Europese en
internationale normalisatienetwerken CEN en ISO" — NL-NEN's `participates-in`
[[INTL-ISO]] edge has carried `confidence: high` since that pass. This
entity's own text simply was not updated to reflect it, a stale
cross-reference of exactly the kind this Atlas has repeatedly found and
fixed elsewhere. Both Germany and the Netherlands are now recorded as ISO
members, each on its own sourced basis.

## Scope note

`coverage: medium` (raised from `low`): DIN's founding, renaming history and
its 1975 government agreement are now recorded in more depth. DIN publishes
standards across technology, services and management; **none of them is an
Atlas entity**, and no German DIN standard is recorded. The German
standards recorded in this batch — [[DE-XOEV]], [[DE-XRECHNUNG]],
[[DE-IT-GRUNDSCHUTZ]] — come from [[DE-KOSIT]] and [[DE-BSI]] rather than
from DIN, which reflects that public-administration IT standards in
Germany are set by government bodies rather than by the national standards
institute.

## Relationships

- `participates-in` [[INTL-ISO]] — `confidence: high` (current membership
  corroborated via `committee.iso.org`, 2026-09-27; the specific 1951
  accession year still rests on a page unreachable to this Atlas).
- `participates-in` [[EU-CEN]] — confirmed directly this pass, `confidence:
  high`.
- [[DE-DKE]], DIN's electrotechnical-standards counterpart towards
  [[EU-CENELEC]], carries the inbound `part-of` edge pointing here —
  closed 2026-09-04.

## Sources

Listed in frontmatter. **4 of 6 now read directly.** Three read directly
in the 2026-08-28 pass, including DIN's own history page — the
previously-flagged gap ("DIN's own site (din.de) is not cited") is now
closed. And, closing part of this file 2026-09-27, `committee.iso.org`'s
own member table, corroborating current ISO membership.
`iso.org/member/1511.html` (HTTP 403) and `quality.de` (empty content)
remain genuinely unreadable, kept listed with those statuses noted here
rather than silently dropped.
