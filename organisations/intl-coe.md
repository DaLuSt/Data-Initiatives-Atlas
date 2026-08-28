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
verification: primary-source

start_date: 1949-05-05
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU
  - EU-GDPR
  - INTL-CONVENTION-108
  - INTL-CONVENTION-108-PLUS
relationships:
  - type: related-to
    target: EU
    source: fact
    evidence: "The Council of Europe is an intergovernmental organisation of 46 member states, separate from the European Union; every EU member state is also a Council of Europe member, and the two organisations are routinely distinguished from one another and from the European Council in official and parliamentary material. Confirmed by reading the EU's own External Action Service page directly (2026-08-28, eeas.europa.eu): the two bodies are 'separate organizations with complementary roles' whose cooperation 'is based on our shared fundamental values: human rights, democracy and the rule of law,' formalised through a 2007 Memorandum of Understanding and operating on three pillars (political dialogue, legal cooperation via bodies like the Venice Commission and GRECO, and jointly funded cooperation projects). Independently confirmed by reading the UK government's own page directly (2026-08-28, gov.uk): the Council of Europe has '46 member states, including all 27 member states of the European Union' — corroborating the overlapping-but-distinct membership this edge asserts. `commonslibrary.parliament.uk` and all `coe.int` pages remain unread (403). This edge records that the two organisations are distinct but overlapping in membership; it asserts no hierarchy."
    confidence: high
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
  - title: "Council of Europe"
    url: "https://en.wikipedia.org/wiki/Council_of_Europe"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Member states of the Council of Europe"
    url: "https://en.wikipedia.org/wiki/Member_states_of_the_Council_of_Europe"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "The European Union and the Council of Europe"
    url: "https://www.eeas.europa.eu/council-europe/european-union-and-council-europe_en?s=51"
    publisher: "European External Action Service (EEAS)"
    accessed: "2026-08-28"
  - title: "UK and the Council of Europe"
    url: "https://www.gov.uk/world/uk-delegation-to-council-of-europe"
    publisher: "GOV.UK"
    accessed: "2026-08-28"
  - title: "Treaties & International Agreements — International and Foreign Cyberspace Law Research Guide"
    url: "https://guides.ll.georgetown.edu/c.php?g=363530&p=4795565"
    publisher: "Georgetown Law Library"
    accessed: "2026-08-28"
---

# Council of Europe

> **Promoted to `primary-source` 2026-08-28.** All three `coe.int` pages
> cited stay unread: `coe.int` is domain-wide 403-blocked for this pass's
> retrieval tool, confirmed again this pass across multiple paths (the
> 46-member-states page, the Russia-exclusion announcement, the
> ECHR-cessation announcement, `coe.int/en` itself, and — on the related
> Convention 108 family entities — `coe.int/en/web/data-protection/*` and
> `rm.coe.int`, all 403). `commonslibrary.parliament.uk` was also retried
> and also returned 403. `web.archive.org`, this pass's suggested next
> step, cannot be reached at all by this environment's fetch tool (a
> tool-level restriction, confirmed by testing the bare domain). Per this
> pass's instruction to look for academic/NGO trackers and other member
> states' own government pages that reproduce Council of Europe facts,
> four further sources were found and read directly: a second, distinct
> Wikipedia article ("Member states of the Council of Europe," confirming
> the post-2022 46-member count and the Article 4 membership-eligibility
> criteria); the EU's own External Action Service page on its relationship
> with the Council of Europe; the UK government's own page on its Council
> of Europe delegation; and a Georgetown Law Library research guide
> confirming the CoE/EU distinction and Convention 108's basic facts from
> an independent academic source. That brings this entity to 5 of 9
> sources read directly — a genuine majority — so `verification` is
> promoted to `primary-source`.

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

**Both are now Atlas entities**, created in the batch immediately after this
one: [[INTL-CONVENTION-108]], [[INTL-CONVENTION-108-PROTOCOL]] (ETS 181,
2001) and [[INTL-CONVENTION-108-PLUS]] (CETS 223, 2018 — adopted, ratified by
34 states, **not in force**).

Between them they brought the Atlas's first eight entities outside Europe and
the UN system: the non-European parties to Convention 108.

## Three organisations that are not each other

The Atlas now holds two of the three bodies English routinely conflates:

| Body | What it is | In the Atlas |
|---|---|---|
| **Council of Europe** | 46-state human-rights organisation, Strasbourg, founded 1949 | this entity |
| **European Union** | 27-state supranational union, Brussels | [[EU]] |
| **European Council** | The EU institution of heads of state or government | not modelled |

The `related-to` edge to [[EU]] records that the first two are distinct.
Every EU member state is a Council of Europe member; the reverse does not
hold, and nineteen Council of Europe members are not in the EU. Confirmed
by reading gov.uk directly this pass: even after the UK left the EU on 31
January 2020, its Council of Europe membership was unaffected — direct
evidence that the two memberships are genuinely independent of one
another, not just definitionally distinct.

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

- The **Committee of Convention 108 (T-PD)** — the treaty's consultative
  committee, which met for its 50th plenary and is the body pressing state
  parties to ratify [[INTL-CONVENTION-108-PLUS]]. It is the Convention's
  counterpart to [[EU-EDPB]] and it is not modelled.
- The **European Court of Human Rights**, the **Committee of Ministers**,
  the **Parliamentary Assembly** and the **Venice Commission**.
- The **Convention 108 Committee** and the accession of non-European states.

## Sources

Listed in frontmatter. None of the four originally-cited pages could be
read this pass — `coe.int` is domain-wide blocked and
`commonslibrary.parliament.uk` also 403'd on retry; `web.archive.org`
cannot be reached at all by this environment's tool. Five of nine sources
read directly: the original Wikipedia "Council of Europe" article (prior
pass), plus four found and read this pass (2026-08-28) — a second
Wikipedia article on CoE member states, the EEAS's own page on EU–CoE
relations, the UK government's own page on its CoE delegation, and a
Georgetown Law Library research guide. A genuine majority, promoting
`verification` to `primary-source`.
