---
id: IE-DPC
type: organisation
name: Data Protection Commission
alternative_names:
  - DPC
  - An Coimisiún um Chosaint Sonraí
  - Irish Data Protection Commission
description: >
  Ireland's data protection supervisory authority, established under the
  Data Protection Act 2018. It is competent to act as lead supervisory
  authority under Article 56 of the GDPR for controllers whose main
  establishment in the Union is in Ireland, which includes much of the
  technology sector, and conducts inquiries under the Article 60
  cooperation procedure.

level: national
country: IE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IE-DPA-2018
  - EU-GDPR
  - EU-EDPB
relationships:
  - type: applies-to
    target: IE-DPA-2018
    source: fact
    evidence: "The Data Protection Commission's inquiry into TikTok was carried out in accordance with the Data Protection Act 2018 and Article 60 of the GDPR; the DPC is Ireland's supervisory authority established under that Act (dataprotection.ie 'Inquiry into TikTok Technology Limited'; dataprotection.ie 'Irish Data Protection Commission submits Article 60 draft decision'; edpb.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "The Irish Data Protection Commission submitted an Article 60 draft decision on its inquiry into TikTok to the other concerned supervisory authorities, and the European Data Protection Board published the Irish supervisory authority's decision fining TikTok EUR 530 million; Article 60 is the GDPR's cooperation procedure between the lead supervisory authority and the other concerned authorities, operated through the Board (dataprotection.ie 'Irish Data Protection Commission submits Article 60 draft decision on inquiry into TikTok'; edpb.europa.eu 'Irish Supervisory Authority fines TikTok EUR 530 million'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Inquiry into TikTok Technology Limited"
    url: "https://www.dataprotection.ie/en/dpc-guidance/decisions/inquiry-tiktok-technology-limited"
    publisher: "Data Protection Commission (Ireland)"
  - title: "Irish Data Protection Commission submits Article 60 draft decision on inquiry into TikTok"
    url: "https://www.dataprotection.ie/en/news-media/latest-news/irish-data-protection-commission-submits-article-60-draft-decision-inquiry-tiktok"
    publisher: "Data Protection Commission (Ireland)"
  - title: "Irish Supervisory Authority fines TikTok €530 million and orders corrective measures following Inquiry into transfers of EEA User Data to China"
    url: "https://www.edpb.europa.eu/news/irish-supervisory-authority-fines-tiktok-eu530-million-and-orders-corrective-measures_en"
    publisher: "European Data Protection Board (EDPB)"
---

# Data Protection Commission (DPC)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The DPC is Ireland's data protection supervisory authority under
[[IE-DPA-2018]], and the **lead supervisory authority** under [[EU-GDPR]]
Article 56 for controllers whose main EU establishment is in Ireland.

## The one-stop-shop, finally visible in the graph

Article 56 makes the authority of the member state where a controller has
its **main EU establishment** the lead supervisory authority for that
controller's cross-border processing. Article 60 then requires the lead
authority to submit a **draft decision** to the other concerned authorities
before it binds.

Because so much of the technology sector places its EU headquarters in
Dublin, that mechanism concentrates a disproportionate share of GDPR
enforcement in this one entity.

The Atlas can now show it. The DPC's **€530 million TikTok decision**,
published by the EDPB as the "Irish Supervisory Authority" decision
following an Article 60 draft, is the worked example: an Irish regulator, an
EU-wide procedure, a company established in Ireland, and data transfers to
China.

## `participates-in` [[EU-EDPB]] — the Atlas's second such edge

Before this batch, [[EU-EDPB]] had **two** incoming relationships in the
whole graph: [[NL-AP]] and [[EU-EDPS]]. Eight national data protection
authorities existed and one was connected.

This entity makes three. It is asserted here and not elsewhere because the
sources *for this authority* show the Article 60 procedure operating through
the Board by name — a stronger basis than membership inferred from the
authority simply existing, which is the standard [[DE-BFDI]] declined to
meet and [[NO-DATATILSYNET]] cannot meet at all.

**The general fix is still outstanding.** Connecting the remaining five
member-state authorities is logged in `discovery/candidates.md` as the
highest-value cheap item on that page, and this batch has not done it.

## Not modelled

- The **Article 60 cooperation procedure** and the **consistency mechanism**
  as entities in their own right. They are mechanisms inside [[EU-GDPR]],
  and the Atlas has no type for a procedure.
- The **controllers** — Meta, Google, TikTok, Microsoft, Apple. Private
  companies are outside the Atlas's scope, which is why the one-stop-shop
  can be described here but its subjects cannot.
- Ireland's **Circuit Court and High Court** appeal routes, which the
  sources show TikTok using.

## Relationships

- `applies-to` [[IE-DPA-2018]].
- `participates-in` [[EU-EDPB]].

## Sources

Listed in frontmatter — two from the DPC itself and one from the EDPB. This
is among the **best-sourced** entities in the batch: unlike most, the claims
rest on the authority's own published decisions rather than on secondary
description.
