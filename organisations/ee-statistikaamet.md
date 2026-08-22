---
id: EE-STATISTIKAAMET
type: organisation
name: Statistikaamet
alternative_names:
  - Statistics Estonia
description: >
  Estonian government agency responsible for producing official
  statistics regarding Estonia, part of the Ministry of Finance, with
  roughly 320 employees and headquarters in Tallinn. Official statistics
  are produced on the basis of the Official Statistics Act and in
  accordance with Regulation (EC) No 223/2009, the framework regulation
  of the European Statistical System — the partnership between Eurostat
  and the national statistical institutes of the EU member states and
  the EFTA countries that this agency's own pages describe directly.
  Estonia's other producer of official statistics is Eesti Pank, the
  central bank.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 1991-01-01
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EE
  - EU-ESS
  - EU-EUROSTAT
relationships:
  - type: part-of
    target: EE
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/Statistics_Estonia directly (2026-08-22): 'Statistics Estonia (Estonian: Statistikaamet) is the Estonian government agency responsible for producing official statistics regarding Estonia. It is part of the Ministry of Finance.' No Estonian Ministry of Finance entity exists in the Atlas, so this anchors directly to the country rather than to an unmodelled parent ministry, under metadata/relationship-types.md §2.3. Corroborated by reading stat.ee's own 'About us' and 'Official statistics and European statistics' pages directly, both of which describe the agency's Estonian statutory role."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Confirmed verbatim by reading stat.ee's own 'Official statistics and European statistics' page directly (2026-08-22): 'Official statistics are produced on the basis of the Official Statistics Act and in accordance with the principles and quality criteria laid down in Regulation (EC) No 223/2009 of the European Parliament and of the Council ... Eurostat produces European statistics in partnership with national statistical institutes and other national authorities in the EU Member States and the European Free Trade Agreement (EFTA) countries. This partnership is known as the European Statistical System (ESS).' Confirmed independently by reading stat.ee's own 'Legal acts' page directly, which lists 'Regulation (EC) No 223/2009 of the European Parliament and of the Council on Eu[ropean statistics]' among its own governing legal acts under an 'Europe' heading, alongside two Commission implementing regulations on access to confidential data. This is the agency describing its own ESS membership directly, the same strength of evidence [[PL-GUS]] carries and stronger than the composition-rule inference most other national statistical offices in the Atlas rely on."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Official statistics and European statistics"
    url: "https://www.stat.ee/en/statistikaamet/meist/official-statistics-and-european-statistics"
    publisher: "Statistics Estonia (Statistikaamet)"
    accessed: "2026-08-22"
  - title: "Legal acts"
    url: "https://www.stat.ee/en/statistics-estonia/about-statistics-estonia/legal-acts"
    publisher: "Statistics Estonia (Statistikaamet)"
    accessed: "2026-08-22"
  - title: "About us"
    url: "https://www.stat.ee/en/statistics-estonia/about-us"
    publisher: "Statistics Estonia (Statistikaamet)"
    accessed: "2026-08-22"
  - title: "Statistics Estonia"
    url: "https://en.wikipedia.org/wiki/Statistics_Estonia"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
---

# Statistikaamet — Statistics Estonia

> **Verified 2026-08-22.** Closes the research-queue item carried since
> the Estonia batch: "Statistikaamet ... would be the twelfth national
> statistical office and another [[EU-ESS]] member. Named only as a
> research-project partner in what was read." All four cited pages were
> read directly this pass. `riigiteataja.ee` — Estonia's official legal
> gazette, tried for a precise citation of the Official Statistics
> Act — is a JavaScript single-page application with no static content
> regardless of the URL guessed, so no Riigi Teataja citation number is
> asserted; the Act is named exactly as stat.ee itself names it, with no
> date or number attached.

## Description

Confirmed by reading en.wikipedia.org/wiki/Statistics_Estonia directly
(2026-08-22): "Statistics Estonia (Estonian: Statistikaamet) is the
Estonian government agency responsible for producing official statistics
regarding Estonia. It is part of the Ministry of Finance. The agency has
approximately 320 employees." Formed in **1991** per the same article's
infobox, headquartered at Tatari 51, Tallinn.

## The best-evidenced ESS membership since Poland's

Confirmed verbatim by reading stat.ee's own "Official statistics and
European statistics" page directly (2026-08-22): "Official statistics
are produced on the basis of the Official Statistics Act and in
accordance with the principles and quality criteria laid down in
Regulation (EC) No 223/2009 of the European Parliament and of the
Council ... Eurostat produces European statistics in partnership with
national statistical institutes and other national authorities in the
EU Member States and the European Free Trade Agreement (EFTA) countries.
This partnership is known as the European Statistical System (ESS)."

[[PL-GUS]]'s entity notes it carries "the best-sourced ESS membership in
the Atlas" because GUS describes the ESS directly rather than relying on
the composition rule most national offices are attached by. Statistikaamet
matches that standard and adds a second, independent confirmation:
stat.ee's own "Legal acts" page, read directly the same pass, lists
"Regulation (EC) No 223/2009 of the European Parliament and of the
Council on Eu[ropean statistics]" among its own governing legal acts
under an "Europe" heading — the agency naming its ESS framework
regulation as one of *its own* legal acts, not just describing the
system in the abstract.

## A second producer, not modelled

Confirmed by reading stat.ee's own "Official statistics and European
statistics" page directly (2026-08-22): "In Estonia, the producers of
official statistics are Statistics Estonia **and Eesti Pank** (Bank of
Estonia)." Estonia's central bank is therefore a second, legally
recognised producer of Estonian official statistics alongside this
entity — named here and not modelled, since nothing else read
establishes what that shared role means for either body's scope.

## Not modelled

- **Eesti Pank**, Estonia's central bank, per the finding above.
- The **Official Statistics Act** itself (Riikliku statistika seadus) as
  a separate law entity — named by stat.ee, but with no date or
  Riigi Teataja citation confirmed. `riigiteataja.ee` is a JavaScript
  single-page application and returned no static content for any URL
  tried.
- The **Statutes of Statistics Estonia**, also named on the "Legal acts"
  page, available only in Estonian and not read.
- [[UN-CES]] or any UN statistical body. Nothing read connects this
  entity to the UN statistical layer, which the Atlas's UN batch reached
  through [[EU-EUROSTAT]] rather than through national offices — the
  same gap [[PL-GUS]] and most other national statistical offices carry.

## Relationships

- `part-of` [[EE]] — anchor edge; no Estonian Ministry of Finance entity
  exists to carry the more specific parent-agency relationship
  en.wikipedia.org names.
- `part-of` [[EU-ESS]] — on the agency's own description of its
  membership, corroborated by its own legal-acts page.

## Sources

Listed in frontmatter. All four pages were read directly this pass;
`riigiteataja.ee` was tried and found genuinely unreadable (a
JavaScript single-page application), not a repeat of the `efta.int`
User-Agent finding from an earlier pass.
