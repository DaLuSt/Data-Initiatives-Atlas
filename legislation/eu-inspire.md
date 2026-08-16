---
id: EU-INSPIRE
type: directive
name: INSPIRE Directive
alternative_names:
  - Directive 2007/2/EC
  - Infrastructure for Spatial Information in the European Community
description: >
  Directive of the European Parliament and of the Council of 14 March 2007
  establishing an Infrastructure for Spatial Information in the European
  Community. It lays down general rules for an infrastructure for spatial
  information in Europe serving EU environmental policies and policies or
  activities that may have an impact on the environment, building on the
  spatial data infrastructures established and operated by the member
  states. It addresses 34 spatial data themes and is given effect through
  implementing rules on metadata, data specifications, network services,
  data and service sharing, and monitoring and reporting.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2007-05-15
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - DE-GEOZG
  - DE-GDI-DE
relationships:
  - type: applies-in
    target: DE
    source: fact
    evidence: "Germany transposed the directive into national law through the federal Geodatenzugangsgesetz and the corresponding acts of the individual Länder; the GeoZG forms the legal basis for implementing the INSPIRE directive at federal level (gdi-de.org/en/praxis-projekte/inspire-umsetzung; mik.brandenburg.de; gdi.bayern.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "Federal DCAT-AP 2 is the profile developed by the Belgian federal administrations involved in the implementation of the INSPIRE Directive, and contains a mapping between INSPIRE and DCAT-AP elements (belgif.be/page/specification/dcat-ap.en.html; github.com/belgif/inspire-dcat). NOT READ — search-only. Note this evidences Belgian INSPIRE implementation activity, not a Belgian transposing act, which was not identified."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: FR
    source: fact
    evidence: "The INSPIRE Directive was transposed into French law by an ordonnance of 21 October 2010, according to the Etalab and data.gouv.fr open data legal chronologies (guides.etalab.gouv.fr/juridique/chronologie; guides.data.gouv.fr; datactivist.coop). NOT READ — search-only. The ordonnance's number was not established, so no entity was created for it."
    confidence: medium
    valid_from: 2010-10-21
    valid_until: null
  - type: applies-in
    target: ES
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, Spain included (EUR-Lex ELI dir/2007/2). NOT READ - search-only. No Spanish transposing instrument was identified in this batch and none is asserted."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The EU's infrastructure for spatial information (Inspire)"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/the-eu-s-infrastructure-for-spatial-information-inspire.html"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "INSPIRE Directive"
    url: "https://knowledge-base.inspire.ec.europa.eu/legislation/inspire-directive_en"
    publisher: "European Commission — INSPIRE Knowledge Base"
  - title: "Directive 2007/2/EC of the European Parliament and of the Council of 14 March 2007 establishing an Infrastructure for Spatial Information in the European Community (INSPIRE)"
    url: "https://www.legislation.gov.uk/eudr/2007/2/body/adopted?view=plain"
    publisher: "The National Archives (legislation.gov.uk)"
  - title: "INSPIRE Umsetzung | Geodateninfrastruktur Deutschland"
    url: "https://www.gdi-de.org/en/praxis-projekte/inspire-umsetzung"
    publisher: "Geodateninfrastruktur Deutschland (GDI-DE)"
---

# INSPIRE Directive

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Directive 2007/2/EC of **14 March 2007** establishes an Infrastructure for
Spatial Information in the European Community. It was published in the
Official Journal on 25 April 2007 and **entered into force on 15 May
2007**.

It lays down general rules for a European spatial information
infrastructure serving EU environmental policies and policies or activities
that may affect the environment. Crucially it is **built on the
infrastructures established and operated by the member states** rather than
on a central EU system — which is why national implementations such as
[[DE-GDI-DE]] exist at all.

It addresses **34 spatial data themes**, and its key components are
specified through common **implementing rules** in five areas: metadata,
data specifications, network services, data and service sharing, and
monitoring and reporting.

## An EU entity added by the German batch, extended by the Belgian one

This directive is not a German entity and does not belong to Germany. It is
recorded here because the German batch reached it: [[DE-GEOZG]] is
Germany's transposition, and modelling the GeoZG without its parent would
have left a national implementing act implementing nothing.

**No `DE-INSPIRE` was created.** The directive is one entity, in
`legislation/`, `country: null`, `region: EU` — the same treatment as
[[EU-GDPR]] and [[EU-NIS2]] — and Germany's relationship to it is expressed
as `applies-in` plus a national implementing act. This is the
country-neutral model doing exactly what it exists for: a second country
adding an EU instrument that the first country's batches happened to miss,
and the instrument arriving country-neutral rather than German-shaped.

## ⚠ The Netherlands relationship is missing, not absent

**No `applies-in` → [[NL]] is recorded**, and that is a gap rather than a
statement. INSPIRE binds all member states, so it certainly applies in the
Netherlands, and [[NL-GEONOVUM]], [[NL-PDOK]] and [[NL-NEN-3610]] are all
plainly part of the Dutch response to it.

None of that is sourced. The German transposition is sourced — the
GDI-DE's own INSPIRE implementation page and two Land geoportals state it —
and the Dutch one is not, because the Dutch geospatial batch was researched
before this directive was an Atlas entity and none of its sources named
INSPIRE.

Recording the German link and not the Dutch one produced a directive that
looked German-specific, which is misleading in the opposite direction from
the usual failure mode.

Belgium has since been added — [[BE-DCAT-AP-BE]]'s federal profile was
built by the administrations implementing INSPIRE and maps between INSPIRE
and DCAT-AP elements — so the directive now reaches two of the Atlas's
three countries and still not the Netherlands. **A third country touched
this directive without closing the Dutch gap**, which makes it harder to
keep describing as an oversight.

It remains a **first-priority gap** in `discovery/unresolved.md`: unlike
most refused links in this Atlas, this one is near-certain to be closable
by a single page read.

## Relationships

- `applies-in` [[DE]] and [[BE]] — **not** [[NL]], see above.

Inbound: [[DE-GEOZG]] implements requirements from this directive, and
[[BE-DCAT-AP-BE]] `references` it through the INSPIRE↔DCAT-AP mapping.

Note the two are different in kind. Germany's is a transposing act;
Belgium's is a metadata mapping produced by the administrations doing the
implementing. **No Belgian transposing act was identified**, and none is
asserted.

## Sources

Listed in frontmatter. Note the third: the **UK National Archives**
holds the adopted text of an EU directive because of the retained-EU-law
arrangements following the UK's withdrawal. It is cited as a text source
only, and it is an odd provenance for a live EU instrument — the EUR-Lex
summary and the Commission's INSPIRE knowledge base carry the weight here.
