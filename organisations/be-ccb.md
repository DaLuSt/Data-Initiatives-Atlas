---
id: BE-CCB
type: organisation
name: Centrum voor Cybersecurity België
alternative_names:
  - CCB
  - Centre for Cybersecurity Belgium
  - Centre pour la Cybersécurité Belgique
description: >
  Belgian national cybersecurity authority and national CSIRT, designated
  as such by the royal decree implementing the NIS2 law. It coordinated the
  Belgian NIS2 transposition together with the Prime Minister's office, and
  operates the Safeonweb awareness platform.

level: national
country: BE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - BE-NIS2-WET
relationships:
  - type: governed-by
    target: BE-NIS2-WET
    source: fact
    evidence: "Confirmed by reading eubelius.com and nis-2-directive.com directly (2026-08-26): eubelius.com states organisations 'must register with the competent authority, namely the Centre for Cybersecurity Belgium (\"CCB\") through its online tool'; nis-2-directive.com independently states the CCB 'was designated as both the national cybersecurity authority and national CSIRT, working alongside sectoral authorities for supervision', naming the implementing instrument as the Royal Decree of 9 June 2024. CCB's own three cited pages remain bot-walled (403)."
    confidence: medium
    valid_from: 2024-10-18
    valid_until: null
  - type: produces
    target: BE-NIS2-WET
    source: fact
    evidence: "The NIS2 law was coordinated by the Centre for Cybersecurity Belgium (CCB) and the Prime Minister's office (eubelius.com 'Entry into force of Belgian acts transposing NIS2'). Not independently re-confirmed this pass — eubelius.com was read but the excerpt retrieved this time did not repeat the co-authorship detail; kept as previously sourced rather than re-asserted as newly confirmed."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "De NIS2-wet"
    url: "https://ccb.belgium.be/nl/nis2"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "Publicatie van de NIS2-wet in het Belgisch Staatsblad"
    url: "https://ccb.belgium.be/nl/news/publicatie-van-de-nis2-wet-het-belgisch-staatsblad"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "Aanname van het koninklijk besluit betreffende NIS2"
    url: "https://ccb.belgium.be/nl/news/aanname-van-het-koninklijk-besluit-betreffende-nis2"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "Entry into force of Belgian acts transposing NIS2: what you need to know"
    url: "https://www.eubelius.com/en/news/entry-into-force-of-belgian-acts-transposing-nis2-what-you-need-to-know"
    publisher: "Eubelius"
    accessed: "2026-08-26"
  - title: "De NIS2-wet | CCB Safeonweb"
    url: "https://atwork.safeonweb.be/nis2"
    publisher: "Safeonweb (CCB)"
  - title: "Transposition in Belgium — The NIS 2 Directive"
    url: "https://www.nis-2-directive.com/Transposition/Belgium.html"
    publisher: "nis-2-directive.com"
    accessed: "2026-08-26"
---

# Centrum voor Cybersecurity België (CCB)

> **Re-checked 2026-08-26, still `search-only`.** CCB's own three cited
> pages, and `atwork.safeonweb.be`, are genuinely bot-walled (403) even
> with an honest User-Agent. Two independent external sources were read
> instead — eubelius.com (a law firm) and nis-2-directive.com — and both
> confirm the CCB's designation as national cybersecurity authority and
> CSIRT, naming the implementing Royal Decree of 9 June 2024. Two of six is
> not a majority, so this entity stays `search-only`.

## Description

The CCB is Belgium's **national cybersecurity authority** and **national
CSIRT**, designated as both by the **Royal Decree of 9 June 2024**
implementing [[BE-NIS2-WET]] — the decree's date confirmed this pass via
nis-2-directive.com, a detail this entity did not previously carry.
Sectoral authorities support it in its tasks.

It **coordinated the Belgian NIS2 transposition** together with the Prime
Minister's office, and it publishes the guidance on incident notification
and on the administrative measures and fines available under the act. It
also runs the **Safeonweb** awareness platform.

## Two relationships in opposite directions, both sourced

This entity carries both `produces` → [[BE-NIS2-WET]] and `governed-by` →
the same act, which looks contradictory and is not:

- The CCB **coordinated the drafting** of the law (with the Prime
  Minister's office).
- The law's implementing royal decree then **designated the CCB** as the
  authority under it.

An agency that helps write the statute that subsequently empowers it is
ordinary, and both facts are separately sourced. Recording only one would
lose half of what the sources say. The `produces` evidence names the
co-author that is not an Atlas entity, so the record does not imply sole
authorship.

## The third national cybersecurity authority in the Atlas

| Country | Authority | Under |
|---|---|---|
| Belgium | **CCB** | [[BE-NIS2-WET]] |
| Germany | [[DE-BSI]] | [[DE-BSIG]] as revised by [[DE-NIS2UMSUCG]] |
| Netherlands | *not modelled* | [[NL-CBW]] |

The Dutch gap is real and pre-dates this batch: the NCSC has never been an
Atlas entity, so the Netherlands has a NIS2 act with no authority attached
to it. Now that two other countries have one, the omission is visible.
Logged in `discovery/research-queue.md`.

**No relationship between the three authorities is asserted.**

## Sources

Two of six read directly this pass — eubelius.com and nis-2-directive.com.
CCB's own three pages and Safeonweb are genuinely bot-walled (403), the
same pattern found across `bosa.belgium.be`, `data.gov.be`,
`financien.belgium.be` and `statbel.fgov.be` in this batch.
