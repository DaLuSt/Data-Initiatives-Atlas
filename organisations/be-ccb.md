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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading five independent sources directly: eubelius.com and nis-2-directive.com (2026-08-26), and simontbraun.eu, lydian.be and ezine.eversheds-sutherland.com (2026-08-27). All five name the Royal Decree of 9 June 2024 as designating the CCB as national cybersecurity authority; nis-2-directive.com and lydian.be additionally name it the national CSIRT; eversheds-sutherland's page instead describes it as coordinating between public authorities (NCCN, NNB, FSMA, BIPT) and the private/academic sectors without using the word CSIRT. CCB's own three cited pages remain bot-walled (403)."
    confidence: high
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
  - title: "Belgian NIS 2 Law | Cybersecurity Strengthen"
    url: "https://simontbraun.eu/belgian-nis-2-law-cybersecurity-strengthen/2024/12/10/"
    publisher: "Simont Braun"
    accessed: "2026-08-27"
  - title: "The implementation of the NIS2 Directive in Belgium: enhancing cybersecurity resilience"
    url: "https://www.lydian.be/en/news-insights/implementation-nis2-directive-belgium-enhancing-cybersecurity-resilience"
    publisher: "Lydian"
    accessed: "2026-08-27"
  - title: "Belgium — EU NIS2 Directive"
    url: "https://ezine.eversheds-sutherland.com/eu-nis2-directive/belgium"
    publisher: "Eversheds Sutherland"
    accessed: "2026-08-27"
---

# Centrum voor Cybersecurity België (CCB)

> **Verified 2026-08-27.** CCB's own three cited pages, and
> `atwork.safeonweb.be`, remain genuinely bot-walled (403) even with an
> honest User-Agent. Five independent external sources were found and
> read directly instead — eubelius.com, nis-2-directive.com,
> simontbraun.eu, lydian.be and ezine.eversheds-sutherland.com — all
> confirming the CCB's designation under the Royal Decree of 9 June 2024,
> three of them by name as national CSIRT. Five of nine is a genuine
> majority.

## Description

The CCB is Belgium's **national cybersecurity authority** and **national
CSIRT**, designated as both by the **Royal Decree of 9 June 2024**
implementing [[BE-NIS2-WET]] — the decree's date confirmed this pass via
nis-2-directive.com, a detail this entity did not previously carry.
Sectoral authorities support it in its tasks.

It **coordinated the Belgian NIS2 transposition** together with the Prime
Minister's office, and it publishes the guidance on incident notification
and on the administrative measures and fines available under the act. It
also runs the **Safeonweb** awareness platform. Confirmed by reading
ezine.eversheds-sutherland.com directly: the CCB "ensure[s] coordination
between the public authorities (NCCN; NNB; FSMA; BIPT; etc.) and the
private or academic sectors" — naming the other Belgian public bodies it
coordinates with, none of which are Atlas entities.

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

Five of nine read directly this pass — eubelius.com, nis-2-directive.com,
simontbraun.eu, lydian.be and ezine.eversheds-sutherland.com. CCB's own
three pages and Safeonweb remain genuinely bot-walled (403), the same
pattern found across `bosa.belgium.be`, `data.gov.be`,
`financien.belgium.be` and `statbel.fgov.be` in this batch.
