---
id: EU-SDG-INDICATORS
type: framework
name: EU SDG indicator set
alternative_names:
  - EU sustainable development indicators
  - EU SDG indicator list
description: >
  The indicator set against which Eurostat monitors the European Union's
  progress towards the Sustainable Development Goals, comprising around 100
  indicators — reported as 102 in one Eurostat source. Eurostat coordinates
  its development using statistics from the European Statistical System and
  publishes annual assessment reports. Of the 100 EU indicators, 55 are
  derived from or similar to the list of SDG indicators drawn up by the UN;
  the selected EU indicators have strong links with EU policies and
  initiatives and complement the UN global indicators from an EU angle. The
  European Commission contributed to the UN's global SDG monitoring in 2023
  through the first EU voluntary review.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2017-01-01
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains: []
organisations:
  - EU-EUROSTAT
related_entities:
  - UN-SDG-INDICATORS
  - EU-EUROSTAT
  - EU-ESS
relationships:
  - type: based-on
    target: UN-SDG-INDICATORS
    source: fact
    evidence: "Of the 100 EU indicators, 55 are derived from or similar to the list of SDG indicators drawn up by the UN; the selected EU indicators have strong links with EU policies and initiatives and complement from an EU angle the UN global indicators by referring to goals and targets specified in the 2030 Agenda (ec.europa.eu/eurostat 'SDG – Introduction'; ec.europa.eu/eurostat/web/sdi/information-data; ec.europa.eu/eurostat news 'New EU SDG indicator list established'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EU-EUROSTAT
    source: fact
    evidence: "Eurostat regularly monitors the EU's progress towards the SDGs, publishing annual assessment reports, and coordinates the development of the EU SDG indicator set using high-quality statistics from the European Statistical System; Eurostat monitors progress along a set of around 100 indicators (ec.europa.eu/eurostat 'SDG – Introduction'; ec.europa.eu/eurostat/web/sdi/publications). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SDG — Introduction — Statistics Explained"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=SDG_-_Introduction"
    publisher: "Eurostat — European Commission"
  - title: "New EU SDG indicator list established"
    url: "https://ec.europa.eu/eurostat/web/products-eurostat-news/-/WDN-20170707-1"
    publisher: "Eurostat — European Commission"
  - title: "Sustainable development indicators — information on data"
    url: "https://ec.europa.eu/eurostat/web/sdi/information-data"
    publisher: "Eurostat — European Commission"
  - title: "Sustainable development indicators — publications"
    url: "https://ec.europa.eu/eurostat/web/sdi/publications"
    publisher: "Eurostat — European Commission"
---

# EU SDG indicator set

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

Eurostat monitors the EU's progress towards the Sustainable Development
Goals against a set of around **100 indicators** — one Eurostat source says
102 — coordinating its development using statistics from [[EU-ESS]] and
publishing annual assessment reports.

**55 of the 100 are derived from or similar to the UN list.** The rest have
strong links to EU policies and complement the global indicators from an EU
angle.

## A quantified descent, which is unusual here

Most `based-on` edges in the Atlas are qualitative: a national profile is
"a German adaptation of DCAT-AP", a framework "is based on" another. This
one has a number attached — **55 of 100** — which makes it the most
precisely specified derivation in the Atlas.

It is also honest about being partial in both directions. The EU set is not
a subset of the global framework (45 indicators are EU-specific) and not a
superset (the global framework has 234). `based-on` is the right type
precisely because it does not claim either.

## The `applies-in` question, and why there is no answer here

Every other EU-level instrument in the Atlas carries `applies-in` to the
five modelled countries. **This one does not**, and the omission is
deliberate.

An indicator set is not an instrument that applies in a member state. It is
a measurement framework Eurostat uses to report on the Union. Nothing read
says member states are obliged to use it, and the sources are explicit that
SDG monitoring happens separately at *"global, regional, national, local and
thematic"* levels — implying national sets exist alongside this one rather
than deriving from it.

Adding `applies-in` here to match the pattern of the other EU entities would
be pattern-matching, not modelling. **No national SDG indicator set is
modelled either**, for any of the five countries; none was researched.

## The 2023 EU voluntary review is not modelled

The Commission contributed to the UN's global SDG monitoring in 2023 through
the **first EU voluntary review** — a genuine EU → UN act, and exactly the
kind of connection this batch went looking for.

It is not recorded as a relationship. A voluntary review is a one-off report
submitted to a UN process, and the Atlas has no relationship type for
"submitted a report to". `references` would be the closest and would
misstate it. Logged in `discovery/unresolved.md` with the UNESCO–Commission
agreement, which has the same problem: **both are real European↔UN
interactions that the vocabulary cannot express.**

That is now two examples rather than one, which is the point at which
`metadata/relationship-types.md` §2.3 says a new type may be worth
proposing. It is not proposed here — that is a decision for a batch that can
read the sources.

## Relationships

- `based-on` [[UN-SDG-INDICATORS]].
- `maintained-by` [[EU-EUROSTAT]].

## Sources

Listed in frontmatter — four Eurostat pages, including the 2017 news item
announcing the establishment of the indicator list, which is the basis for
the `start_date`.
