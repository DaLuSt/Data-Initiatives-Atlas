---
id: EU-SDG-INDICATORS
type: framework
name: EU SDG indicator set
alternative_names:
  - EU sustainable development indicators
  - EU SDG indicator list
description: >
  The indicator set against which Eurostat monitors the European Union's
  progress towards the Sustainable Development Goals. Established in July
  2017 with 100 indicators, it has 102 in the 2026 monitoring report, of
  which 34 are multi-purpose and around two-thirds are aligned with the UN
  SDG indicators. Eurostat coordinates its development using statistics from
  the European Statistical System and publishes annual assessment reports;
  the indicators have strong links with EU policies and complement the UN
  global indicators from an EU angle. The
  European Commission contributed to the UN's global SDG monitoring in 2023
  through the first EU voluntary review.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-18"
previous_version: null
successor: null

domains: []
organisations:
  - EU-EUROSTAT
related_entities:
  - UN-SDG-INDICATORS
  - EU-EUROSTAT
  - EU-ESS
  - DE-NACHHALTIGKEITSINDIKATOREN
  - FR-INDICATEURS-ODD
  - BE-INDICATEURS-DEVELOPPEMENT-DURABLE
  - NL-MONITOR-BREDE-WELVAART-SDG
  - ES-INDICADORES-ODS
relationships:
  - type: based-on
    target: UN-SDG-INDICATORS
    source: fact
    evidence: "Eurostat's Statistics Explained article 'SDG – Introduction' (2026 edition, data extracted April 2026), read directly 2026-11-18: 'Out of the 102 indicators, 34 are ‘multi-purpose’' and 'Around two-thirds of the current EU SDG indicators are aligned with the UN SDG indicators.' Eurostat's news item of 7 July 2017, read directly: the indicators 'complement from an EU angle the UN global indicators, which refer to the goals and targets specified in the 2030 Agenda'. The earlier '55 of the 100' figure was not found on any page read and is dropped."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EU-EUROSTAT
    source: fact
    evidence: "Eurostat's 'Information on data' page for the SDG indicators, read directly 2026-11-18: 'Eurostat regularly monitors the EU’s progress towards the SDGs, publishing annual assessment reports. Making use of high-quality statistics of the European Statistical System and complementary data from partner institutions, Eurostat coordinates the development of the EU SDG indicator set and keeps it up to date.'"
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
>
> **Narrowed 2026-09-19** (`discovery/unresolved.md` row #175): all five
> of the Atlas's original countries now have a national SDG indicator set
> modelled. See "The `applies-in` question" below.

## Description

Eurostat monitors the EU's progress towards the Sustainable Development
Goals against a set that Eurostat's 2017 news item gives as **100 indicators**
and the 2026 monitoring report as **102**, coordinating its development using
statistics from [[EU-ESS]] and publishing annual assessment reports.

**Around two-thirds are aligned with the UN SDG indicators** (Statistics
Explained, "SDG – Introduction", 2026 edition, read directly 2026-11-18). The
rest have strong links to EU policies and complement the global indicators
from an EU angle.

> **Corrected 2026-11-18.** This entity said "55 of the 100 are derived from or
> similar to the UN list", from search results. None of the four Eurostat pages
> it cites, read directly, gives that figure; the current one gives "around
> two-thirds" of 102.

## A quantified descent, which is unusual here

Most `based-on` edges in the Atlas are qualitative: a national profile is
"a German adaptation of DCAT-AP", a framework "is based on" another. This
one has a proportion attached — **around two-thirds of 102** — which makes it
one of the more precisely specified derivations in the Atlas.

It is also honest about being partial in both directions. The EU set is not
a subset of the global framework (about a third of the indicators are not
aligned with it) and not a superset (the UN General Assembly's list covered 232
indicators when it was adopted in July 2017, per the same Eurostat page). `based-on` is the right type
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
be pattern-matching, not modelling. **All five of the Atlas's original
countries now have a national SDG indicator set modelled, 2026-09-19**:
[[DE-NACHHALTIGKEITSINDIKATOREN]] (Germany, maintained by
[[DE-DESTATIS]] since 2006), [[FR-INDICATEURS-ODD]] (France, 98
indicators, maintained by [[FR-INSEE]]), [[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]]
(Belgium, 84 indicators, maintained by [[BE-BUREAU-FEDERAL-DU-PLAN]]),
[[NL-MONITOR-BREDE-WELVAART-SDG]] (the Netherlands, 293 indicators merged
into the domestic Monitor Brede Welvaart, maintained by [[NL-CBS]]), and
[[ES-INDICADORES-ODS]] (Spain, 234 indicators, maintained by [[ES-INE]]).
Each is `based-on` [[UN-SDG-INDICATORS]] independently, with its own
indicator count and national selection basis. **No relationship is
asserted between any of the five and this entity, or between any of them
and each other**: nothing read connects any national set to the EU set
specifically, or to any other national set — all descend independently
from the shared UN ancestor.

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

## Year only (2026-11-17)

The sources read give the year 2017, not a day. `start_date` was `2017-01-01`, a placeholder for "in 2017" that `metadata/metadata-schema.md` rules out, and is now empty. The year stays in the description and the text above.

## Sources

Listed in frontmatter — four Eurostat pages, including the 2017 news item
announcing the establishment of the indicator list, which is the basis for
the year 2017 (the `start_date` itself is empty, see "Year only"). Each national statistical office's own page on its
country's indicator set was read directly on the corresponding entity —
[[DE-NACHHALTIGKEITSINDIKATOREN]], [[FR-INDICATEURS-ODD]],
[[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]],
[[NL-MONITOR-BREDE-WELVAART-SDG]] and [[ES-INDICADORES-ODS]] — not
re-fetched here.
