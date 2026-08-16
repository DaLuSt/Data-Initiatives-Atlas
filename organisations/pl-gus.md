---
id: PL-GUS
type: organisation
name: Główny Urząd Statystyczny
alternative_names:
  - GUS
  - Statistics Poland
  - Central Statistical Office
description: >
  Polish national statistical office: a central government office
  responsible for collecting and providing statistical information on most
  areas of public life and some aspects of private life. It operates under
  the Act on Public Statistics of 29 June 1995, which defines its
  competencies, tasks and organisation. As national coordinator of Polish
  public statistics it is obliged to provide statistical information at many
  levels, including transmitting European statistics to Eurostat, and it
  describes the European Statistical System as the partnership between the
  Commission through Eurostat and the national statistical offices, with
  Regulation (EC) No 223/2009 as its framework legal act.

level: national
country: PL
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-ESS
  - EU-EUROSTAT
relationships:
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Polish public statistics, and particularly GUS as its national coordinator, is obliged to provide statistical information on many levels, including transmitting European statistics to Eurostat; GUS describes the European Statistical System as the partnership between the Community's statistical body, the Commission (Eurostat), and the national statistical offices and other national bodies responsible in each member state for developing, producing and disseminating European statistics, with Regulation (EC) No 223/2009 as the framework legal act specifying the scope and forms of action of the ESS (stat.gov.pl 'ESS — Europejski System Statystyczny oraz Eurostat'; bip.stat.gov.pl 'Polski system statystyczny'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ESS — Europejski System Statystyczny oraz Eurostat"
    url: "https://stat.gov.pl/statystyka-miedzynarodowa/instytucjeorganizacje-miedzynarodowe/ess-europejski-system-statystyczny-oraz-eurostat/"
    publisher: "Główny Urząd Statystyczny (GUS)"
  - title: "Polski system statystyczny — Biuletyn Informacji Publicznej GUS"
    url: "https://bip.stat.gov.pl/dzialalnosc-statystyki-publicznej/polski-system-statystyczny/"
    publisher: "Główny Urząd Statystyczny (GUS)"
  - title: "Dane Eurostatu — GUS"
    url: "https://stat.gov.pl/dla-mediow/dane-eurostatu/"
    publisher: "Główny Urząd Statystyczny (GUS)"
  - title: "Rekomendacje międzynarodowe dotyczące doskonalenia jakości w statystyce publicznej"
    url: "https://bip.stat.gov.pl/dzialalnosc-statystyki-publicznej/jakosc-w-statystyce/rekomendacje-miedzynarodowe"
    publisher: "Główny Urząd Statystyczny (GUS)"
---

# GUS — Główny Urząd Statystyczny

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

GUS is Poland's national statistical office — a central government office
collecting and providing statistical information across most areas of public
life. It operates under the **Act on Public Statistics of 29 June 1995**,
which defines its competencies, tasks and organisation.

As **national coordinator** of Polish public statistics it is obliged to
provide statistical information at many levels, **including transmitting
European statistics to Eurostat**.

## The best-sourced ESS membership in the Atlas

Five national statistical offices now sit in [[EU-ESS]], and this one has
the strongest evidence of any of them.

The other four attach on the ESS **composition rule** — the partnership is
defined as the Commission plus the national statistical institutes, and each
office is its country's NSI, so membership follows. That reasoning is sound
but it is the Atlas joining two facts.

GUS's own pages **describe the European Statistical System directly**, in
the same terms as Eurostat and Regulation (EC) No 223/2009, and state GUS's
obligation to transmit European statistics to Eurostat. The membership is
asserted by the member, on its own site, in its own words.

| Country | Office | Basis for `part-of` [[EU-ESS]] |
|---|---|---|
| Netherlands | [[NL-CBS]] | composition rule |
| Germany | [[DE-DESTATIS]] | composition rule |
| Belgium | [[BE-STATBEL]] | composition rule |
| Spain | [[ES-INE]] | composition rule + INE's own SEE explanation |
| **Poland** | **GUS** | **its own ESS page + stated Eurostat obligation** |
| France | *(INSEE not modelled)* | — |

**France remains the only modelled country with no statistical office**, and
that hole is now visible in a five-member structure rather than among
unconnected nodes.

## Not asserted

**No edge to [[EU-EUROSTAT]] directly**, despite the sourced obligation to
transmit statistics to it. The transmission is an operational duty flowing
from ESS membership, and the Atlas records the membership. Adding a second
edge would double-count one relationship — and "transmits data to" is
another instance of the missing data-movement vocabulary the register batch
documented.

**No edge to [[UN-FPOS]]**, [[UN-UNSC]] or [[UN-CES]]. Nothing read connects
GUS to the UN statistical layer, which the UN batch reached through
[[EU-EUROSTAT]] rather than through national offices.

**The Act on Public Statistics is not modelled.** It is named and dated, and
no law entity was created — consistent with how the register batch handled
the Dutch statutes.

## Relationships

- `part-of` [[EU-ESS]].

## Sources

Listed in frontmatter — four GUS pages, two of them from its public
information bulletin.
