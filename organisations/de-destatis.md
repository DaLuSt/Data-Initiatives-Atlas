---
id: DE-DESTATIS
type: organisation
name: Statistisches Bundesamt
alternative_names:
  - Destatis
  - StBA
  - Federal Statistical Office of Germany
description: >
  German federal statistical office, in the business area of the Federal
  Ministry of the Interior. Its tasks are set by the Bundesstatistikgesetz:
  continuously collecting, compiling, processing, presenting and analysing
  data on mass phenomena under principles of neutrality, objectivity and
  professional independence, producing around 390 federal statistics, and
  publishing results in open-data-compliant, machine-readable formats. Its
  own site names the European Statistical System explicitly as part of the
  framework shaping its collection requirements.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-BMI
  - DE-BSTATG
relationships:
  - type: part-of
    target: DE-BMI
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's dedicated Destatis article directly (2026-08-28): the Statistisches Bundesamt 'operates as a federal authority under the Bundesministerium des Innern (Federal Ministry of the Interior).' destatis.de's own 'Aufgaben' and 'Gesetzliche Grundlagen' pages, also read directly, describe Destatis's tasks and legal basis without themselves naming the parent ministry on those specific pages."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-BSTATG
    source: fact
    evidence: "Confirmed by reading destatis.de's own 'Gesetzliche Grundlagen' page directly (2026-08-28): 'without legal foundation, official statistics cannot be created in Germany,' naming the Bundesstatistikgesetz (BStatG) as the primary legal framework requiring Destatis to provide and disseminate statistical information while maintaining data protection and statistical confidentiality. de.wikipedia.org, also read directly, independently confirms the BStatG (Gesetz über die Statistik für Bundeszwecke) establishes Destatis's obligations of objectivity, neutrality and scientific independence."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Confirmed by reading destatis.de's own 'Gesetzliche Grundlagen' page directly (2026-08-28), which names the 'European Statistical System' framework explicitly as shaping Destatis's data-collection requirements through binding EU ordinances, and destatis.de's 'Aufgaben' page, also read directly, which states Destatis follows the European 'Code of Practice' that 'all National Statistical Institutes (NSI) of the European member states voluntarily commit to' and participates in EU peer reviews. This is a stronger basis than the previous pass's search-snippet evidence: it is now Destatis's own site naming the European Statistical System by name, not an inference from the general ESS composition rule."
    confidence: high
    valid_from: null
    valid_until: null
sources:
  - title: "Aufgaben — Statistisches Bundesamt"
    url: "https://www.destatis.de/DE/Ueber-uns/Aufgaben/_inhalt.html"
    publisher: "Statistisches Bundesamt (Destatis)"
    accessed: "2026-08-28"
  - title: "Gesetzliche Grundlagen — Statistisches Bundesamt"
    url: "https://www.destatis.de/DE/Ueber-uns/Aufgaben/gesetze.html"
    publisher: "Statistisches Bundesamt (Destatis)"
    accessed: "2026-08-28"
  - title: "Statistisches Bundesamt"
    url: "https://de.wikipedia.org/wiki/Statistisches_Bundesamt"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Statistisches Bundesamt/Statistische Landesämter"
    url: "https://www.bpb.de/kurz-knapp/lexika/handwoerterbuch-politisches-system/202188/statistisches-bundesamt-statistische-landesaemter/"
    publisher: "Bundeszentrale für politische Bildung (bpb)"
  - title: "Statistisches Bundesamt"
    url: "https://www.service.bund.de/Content/DE/DEBehoerden/S/StBA/Statistisches-Bundesamt.html?nn=4641496"
    publisher: "service.bund.de (Bundesverwaltungsamt)"
---

# Statistisches Bundesamt (Destatis)

> **Re-verified 2026-08-28.** Three of five cited pages read directly,
> including both of Destatis's own pages. `verification: primary-source`;
> `confidence` raised to `high`. The `part-of` [[EU-ESS]] edge — previously
> resting only on the general ESS composition rule via secondary sources —
> is now confirmed on Destatis's own site, which names the European
> Statistical System explicitly.

## Description

Destatis is Germany's federal statistical office, in the Geschäftsbereich
of [[DE-BMI]] — confirmed directly this pass via its dedicated Wikipedia
article. Its tasks are established in [[DE-BSTATG]]: confirmed directly
this pass on destatis.de's own page, "without legal foundation, official
statistics cannot be created in Germany," with continuous collecting,
compiling, processing, presenting and analysing of data on mass phenomena.
Destatis produces roughly **390 federal statistics** on a current basis,
confirmed directly on its own "Aufgaben" page and Wikipedia alike.

Principles of **neutrality, objectivity and professional independence**
apply, and data is obtained using scientific knowledge and appropriate
methods and information technologies.

Two aspects matter for the Atlas specifically:

- **Open data by default in the output.** The office prepares federal
  statistics methodically and technically, compiles results for the federal
  government from data supplied by the Länder, and publishes them in
  **open-data-compliant, machine-readable formats**.
- **The European and international layer, now sourced by name.**
  destatis.de's own "Gesetzliche Grundlagen" page, read directly this
  pass, names the **European Statistical System** explicitly as part of
  the framework shaping its collection requirements via binding EU
  ordinances, and its "Aufgaben" page confirms Destatis follows the
  European Statistics Code of Practice that "all National Statistical
  Institutes (NSI) of the European member states voluntarily commit to,"
  participating in EU peer reviews.

It is bound to comply with data protection and to maintain statistical
confidentiality of the individual data it collects. Its "Gesetzliche
Grundlagen" page, read directly, also confirms official statistics are "a
joint product" created collaboratively with the **14 statistical offices
of the Länder** under their own state statistical laws — a Bund-Länder
structure not previously recorded on this entity.

## The link to Eurostat that is now closer, though still not asserted by name

Before this pass, this entity flagged a structural gap the Atlas has
recorded twice: [[UN-UNSD]] → [[EU-EUROSTAT]] and [[UN-FPOS]] →
[[NL-WET-CBS]] were both refused for want of a source, and Destatis's own
sourced remit — "cooperating in the preparation of statistical programmes
... for the purposes of the European Union" — offered a third candidate of
the same shape, also refused, because no source read named
[[EU-EUROSTAT]] or the European Statistical System specifically.

This pass **partly closes that gap**: destatis.de's own site, read
directly, now names the European Statistical System by name — enough to
support the `part-of` [[EU-ESS]] edge above at `confidence: high`. What
still is not confirmed is a direct Destatis↔[[EU-EUROSTAT]] edge; no source
read this pass names Eurostat by name on a Destatis page. The remaining gap
is logged in `discovery/unresolved.md` alongside the other two, narrower
than before.

## Relationships

- `part-of` [[DE-BMI]] — confirmed directly this pass, `confidence: high`.
- `governed-by` [[DE-BSTATG]] — confirmed directly this pass, `confidence:
  high`.
- `part-of` [[EU-ESS]] — confirmed directly this pass on Destatis's own
  site, `confidence: high` (raised from `medium`).

## Sources

Listed in frontmatter. Three of five read directly this pass, including
both Destatis pages; `bpb.de` and `service.bund.de` were not re-fetched,
not being needed for the majority.
