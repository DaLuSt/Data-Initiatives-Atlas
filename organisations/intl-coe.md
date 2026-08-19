---
id: INTL-COE
type: organisation
name: Council of Europe
alternative_names:
  - CoE
  - Conseil de l'Europe
description: >
  Intergovernmental organisation founded in 1949 and headquartered in
  Strasbourg, with 46 member states covering almost the whole of geographic
  Europe. It is distinct from the European Union and from the European
  Council, and is the body that produced the European Convention on Human
  Rights and Convention 108 — the only binding international treaty on the
  protection of personal data, opened for signature in 1981 and modernised
  as Convention 108+ by an amending protocol in 2018. Russia's membership
  was terminated on 16 March 2022, the first expulsion in the
  organisation's history.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 1949-05-05
end_date: null
last_verified: "2026-08-19"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU
  - EU-GDPR
relationships:
  - type: related-to
    target: EU
    source: fact
    evidence: "The Council of Europe is an intergovernmental organisation of 46 member states, separate from the European Union; every EU member state is also a Council of Europe member, and the two organisations are routinely distinguished from one another and from the European Council in official and parliamentary material (coe.int portal '46 member states'; commonslibrary.parliament.uk CBP-9570 'Work of the Council of Europe and the expulsion of Russia'). NOT READ — search-only. This edge records that the two organisations are distinct but overlapping in membership; it asserts no hierarchy."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "The Russian Federation is excluded from the Council of Europe"
    url: "https://www.coe.int/en/web/ccpe/-/the-russian-federation-is-excluded-from-the-council-of-europe"
    publisher: "Council of Europe"
  - title: "Russia ceases to be a Party to the European Convention on Human Rights on 16 September 2022"
    url: "https://www.coe.int/en/web/portal/-/russia-ceases-to-be-a-party-to-the-european-convention-of-human-rights-on-16-september-2022"
    publisher: "Council of Europe"
  - title: "Work of the Council of Europe and the expulsion of Russia — research briefing CBP-9570"
    url: "https://commonslibrary.parliament.uk/research-briefings/cbp-9570/"
    publisher: "House of Commons Library"
---

# Council of Europe

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The pan-European intergovernmental organisation, and the membership frame
that lets the Atlas anchor a European country that is not in the EU.

## Why a data atlas holds this entity

Two reasons, one structural and one substantive.

**Structural.** Before this batch, every country anchor in the Atlas reached
the graph only through the national entities that pointed *at* it. That
works for a country with a modelled layer and fails for a country that has
just been created. EU member states can anchor on [[EU]]; the twenty
European states that are not EU members had nowhere to anchor. The Council
of Europe is the membership frame that covers almost all of them.

**Substantive.** The Council of Europe produced **Convention 108** —
formally the Convention for the Protection of Individuals with regard to
Automatic Processing of Personal Data, opened for signature in Strasbourg on
28 January 1981 — and its modernising amending protocol, **Convention 108+**,
opened in 2018.

Convention 108 is the **only binding international treaty on data
protection**. [[EU-GDPR]] is a regional instrument binding 27 states;
Convention 108+ is open to accession by states outside Europe entirely. A
data governance atlas that holds the GDPR and not Convention 108 is missing
the older and geographically wider of the two.

**Convention 108 and 108+ are not yet Atlas entities.** They are queued in
`discovery/research-queue.md` as the highest-value item this batch
surfaced. This entity exists first because the country anchors needed it.

## Three organisations that are not each other

The Atlas now holds two of the three bodies English routinely conflates:

| Body | What it is | In the Atlas |
|---|---|---|
| **Council of Europe** | 46-state human-rights organisation, Strasbourg, founded 1949 | this entity |
| **European Union** | 27-state supranational union, Brussels | [[EU]] |
| **European Council** | The EU institution of heads of state or government | not modelled |

The `related-to` edge to [[EU]] records that the first two are distinct.
Every EU member state is a Council of Europe member; the reverse does not
hold, and nineteen Council of Europe members are not in the EU.

## The first expulsion

Russia's membership was terminated on **16 March 2022** under Article 8 of
the Statute, with immediate effect, after 26 years — the first expulsion in
the organisation's history. Russia ceased to be a party to the European
Convention on Human Rights on 16 September 2022.

[[RU]] carries this as a `part-of` edge with a `valid_until` date rather
than as a missing edge, because a membership that ended is a different fact
from a membership that never existed. [[BY]] is the second case: Belarus has
never been a member, and its special guest status was suspended in 1997.

## Not modelled

- **Convention 108 and Convention 108+** — queued, and the reason this
  entity is worth more than its anchoring role.
- The **European Court of Human Rights**, the **Committee of Ministers**,
  the **Parliamentary Assembly** and the **Venice Commission**.
- The **Convention 108 Committee** and the accession of non-European states.

## Sources

Listed in frontmatter.
