---
id: XK
type: country
name: Kosovo
alternative_names:
  - Republic of Kosovo
  - Kosovë
  - Republika e Kosovës
  - Косово
description: >
  Country anchor entity for Kosovo, a potential candidate for European
  Union membership. It is a base anchor: it carries the country's position
  in the European legal and institutional frameworks so that entities
  scoped to it have somewhere to attach, and no national entities are
  modelled yet.

level: national
country: XK
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: related-to
    target: EU
    source: fact
    evidence: "Kosovo applied to join the European Union in December 2022 and is listed as a potential candidate rather than a candidate country; its Stabilisation and Association Agreement with the EU has been in force since 2016. The December 2022 application date and potential-candidate status are confirmed on en.wikipedia.org/wiki/Kosovo ('On 15 December 2022 Kosovo filed a formal application to become a member of the European Union'); the enlargement.ec.europa.eu page was read but its Kosovo-specific detail is rendered client-side and did not appear in the retrieved page text, so it corroborates the page's existence rather than these specific dates. The 2016 SAA date was not independently re-confirmed this pass. Anchor edge: it records an accession relationship in progress and asserts nothing about recognition."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Candidate countries and potential candidates"
    url: "https://enlargement.ec.europa.eu/enlargement-policy/candidate-countries-and-potential-candidates_en"
    publisher: "European Commission — Enlargement and Eastern Neighbourhood"
    accessed: "2026-08-21"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
    accessed: "2026-08-21"
  - title: "Kosovo"
    url: "https://en.wikipedia.org/wiki/Kosovo"
    publisher: "Wikipedia"
    accessed: "2026-08-21"
---

# Kosovo

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.

## Description

Kosovo (**`XK`** — a user-assigned code; Kosovo has no ISO 3166-1 code) is
a **base country anchor**, created so that entities scoped to it have
somewhere to attach. No Kosovo entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | **Potential candidate** — applied December 2022 |
| Euro area | No |
| Schengen area | No |
| Council of Europe | **Not a member** |

> The December 2022 application date is now confirmed on Wikipedia. The
> 2016 Stabilisation and Association Agreement date and the non-membership
> of the Council of Europe, Schengen and the euro area were not
> independently re-confirmed this pass and still come from general
> reference knowledge.

## ⚠ The one anchor with no ISO 3166-1 code

**Kosovo has no ISO 3166-1 alpha-2 code.** `XK` is a *user-assigned*
code — the range ISO reserves for exactly this situation — and it is what the
European Commission, the IMF and the World Bank use operationally. (This
explanatory note previously lived inside `alternative_names` as
"XK (user-assigned code, not ISO 3166-1)" — moved here on this pass, since it
is commentary about the code, not a name anyone calls the country.)

`metadata/ontology.md` §3.1 says the national scope segment is the ISO
3166-1 alpha-2 code. This anchor is the first exception, and the rule has
been amended to name it rather than being quietly broken.

Kosovo applied to join the EU in **December 2022** and is a **potential
candidate**, not a candidate — both confirmed on Wikipedia, which also
confirms it is recognised by 22 of 27 EU member states, matching the
Atlas's count of five non-recognisers: [[GR]], [[ES]], [[CY]], [[RO]] and
[[SK]] (the specific five were not independently re-confirmed this pass).
Nor does [[RS]] recognise it. Its Stabilisation and Association Agreement
with the EU has been in force since 2016, which is why its anchor edge
points at [[EU]] — this date was not independently re-confirmed this pass.

It uses the **euro unilaterally**, like [[ME]].

**Creating an entity is a record, not a recognition.** The Atlas describes
what exists in the sources it cites; it takes no position on statehood, and
this note exists so that no reader has to infer one.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter.
