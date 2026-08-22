---
id: GB-ONS
type: organisation
name: Office for National Statistics
alternative_names:
  - ONS
description: >
  The United Kingdom's largest independent producer of official statistics
  and the recognised national statistical institute of the UK, responsible
  for collecting, analysing and disseminating statistics about the UK
  economy, society and population, and for conducting the census in England
  and Wales. It is the executive office of the UK Statistics Authority,
  reporting through the Authority to Parliament and the devolved
  governments rather than to ministers, and its outputs are regulated by the
  Office for Statistics Regulation. The UK is a member of the Conference of
  European Statisticians and of its Bureau.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB-UKSA
  - UN-CES
  - UN-UNECE
  - NL-CBS
  - DE-DESTATIS
  - BE-STATBEL
  - ES-INE
  - PL-GUS
relationships:
  - type: part-of
    target: GB-UKSA
    source: fact
    evidence: "Confirmed verbatim by reading ons.gov.uk's own 'About us' page (2026-08-22): 'We are independent of ministers and instead report through the UK Statistics Authority to Parliament and the devolved governments of Scotland, Wales and Northern Ireland. We are the executive office of the UK Statistics Authority.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: UN-CES
    source: fact
    evidence: "NOT independently re-confirmed 2026-08-22: unece.org returns a bot-defense challenge (403) on both cited pages, and the UKSA 'Multilateral Engagement' URL has moved — its replacement (uksa.statisticsauthority.gov.uk/about-the-authority/working-internationally/) lists UNECE among the bodies UKSA works with but does not name the Conference of European Statisticians or its Bureau specifically. The original claim is retained rather than removed, since a page move and a bot-wall are not evidence the claim is wrong — but it is not re-verified. CAVEAT: the original sources establish UK membership of the CES and its Bureau; whether the member is the ONS or the UK Statistics Authority is not distinguished."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "About us — Office for National Statistics"
    url: "https://www.ons.gov.uk/aboutus"
    publisher: "Office for National Statistics (UK)"
    accessed: "2026-08-22"
  - title: "What we do — Office for National Statistics"
    url: "https://www.ons.gov.uk/aboutus/whatwedo"
    publisher: "Office for National Statistics (UK)"
    accessed: "2026-08-22"
  - title: "Working internationally — UK Statistics Authority"
    url: "https://uksa.statisticsauthority.gov.uk/about-the-authority/working-internationally/"
    publisher: "UK Statistics Authority"
    accessed: "2026-08-22"
  - title: "Bureau of the Conference of European Statisticians (CES)"
    url: "https://unece.org/statistics/ces/bureau-conference-european-statisticians-ces"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "About the Conference of European Statisticians (CES)"
    url: "https://unece.org/statistics/ces/about-conference-european-statisticians-ces"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
---

# Office for National Statistics

> **Verified 2026-08-22.** ons.gov.uk's own "About us" page was read
> directly and confirmed the claims below verbatim. The UN-CES/Bureau
> claim could not be re-confirmed this pass — see that relationship's
> evidence — because `unece.org` is bot-walled and the UKSA page that
> originally supported it has moved to one that no longer states it. The
> claim is retained, not removed, since neither obstacle is evidence it is
> wrong.

## Description

Confirmed verbatim on ons.gov.uk's "About us" page (2026-08-22): "We are
the UK's largest independent producer of official statistics and its
recognised national statistical institute." The ONS is the UK's recognised **national statistical institute** and its
largest independent producer of official statistics. It runs the census in
England and Wales and publishes over 600 statistical releases a year.

Structurally it is the **executive office of the UK Statistics Authority**,
reporting through the Authority to Parliament and the devolved governments
**rather than to ministers** — an independence arrangement none of the other
six statistical offices in the Atlas is recorded as having.

## The sixth statistical office, and the first that joins through the UN

This is the finding the UK batch exists to produce.

| Country | Office | Attaches upward via |
|---|---|---|
| Netherlands | [[NL-CBS]] | [[EU-ESS]] |
| Germany | [[DE-DESTATIS]] | [[EU-ESS]] |
| Belgium | [[BE-STATBEL]] | [[EU-ESS]] |
| Spain | [[ES-INE]] | [[EU-ESS]] |
| Poland | [[PL-GUS]] | [[EU-ESS]] |
| **United Kingdom** | **this entity** | **[[UN-CES]] — the UN layer, directly** |
| France | — | *no statistical office modelled* |

Five member states reach the international statistical system **through**
the European Statistical System. The UK cannot: the ESS comprises Eurostat
and the statistical authorities of the member states, and the UK is not one.

It reaches it **directly instead**, through the Conference of European
Statisticians — a UNECE body whose ~65 members are not limited to the EU,
and on whose **Bureau the UK sits**. The ONS has hosted that Bureau in
Cardiff.

**This edge is only possible because the UN batch created [[UN-CES]].** At
the time it was written, the CES looked like completeness work on the
statistics chain. It turns out to have been the connector for a country that
did not yet exist in the Atlas — and without it, the UK's statistical office
would have had no upward link of any kind.

## What is refused

**No `participates-in` [[EU-ESS]] edge.** The UK is not a member of the
European Statistical System and none is asserted. This is the first time the
Atlas has had a national statistical office that *cannot* join the structure
the previous five share, and the absence is the informative part.

**The Office for Statistics Regulation is not modelled** — the regulator
that sets the code of practice for UK official statistics.

⚠ **[[GB-UKSA]] is now modelled, and it did not resolve the caveat.** The
sources establish that **the UK** is a CES and Bureau member; they do not
say whether the seat belongs to the ONS or to the Authority. Researching the
Authority was the obvious way to settle it and produced no answer, so the
participation is recorded on **both** entities — here at `confidence: medium`
and on [[GB-UKSA]] at `low` — with the ambiguity written into both evidence
strings. Two edges where one belongs is worse than a clean answer and better
than a confident guess.

## Relationships

- `part-of` [[GB-UKSA]] — the ONS is the Authority's executive office. This
  is the best-founded edge on this entity.
- `participates-in` [[UN-CES]] — with the caveat above.

## Sources

Listed in frontmatter — two ONS pages, one UK Statistics Authority page and
two UNECE pages. The two ONS pages and the (updated) UKSA page were read
directly; the two UNECE pages remain unread, blocked by a bot-defense
challenge.
