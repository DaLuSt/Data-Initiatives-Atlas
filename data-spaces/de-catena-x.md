---
id: DE-CATENA-X
type: data-space
name: Catena-X Automotive Network
alternative_names:
  - Catena-X
description: >
  Open and collaborative data ecosystem for the automotive industry. The
  Catena-X Automotive Network e.V. was founded in May 2021 and the founding
  research consortium ran from August 2021 to July 2024. It is a
  distributed, Gaia-X-based data ecosystem built on European standards and
  following the International Data Spaces reference architecture, intended
  to guarantee the digital sovereignty of actors in the automotive industry
  and to enable secure, decentralised and standardised data exchange between
  vehicle manufacturers, suppliers and service providers along the
  automotive value chain.

level: sectoral
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - INTL-IDS-RAM
  - INTL-IDSA
  - EU-GAIA-X
  - DE-MANUFACTURING-X
  - DE-FACTORY-X
relationships:
  - type: based-on
    target: INTL-IDS-RAM
    source: fact
    evidence: "Confirmed by reading three sources directly (2026-08-28): Fraunhofer ISST's own current Catena-X page (isst.fraunhofer.de/en/departments/industrial-manufacturing/projects/CatenaX.html — the entity's originally-cited ISST URL, under /mobility-und-smart-cities/, now 404s and was located afresh via search) states 'Catena-X is based on GAIA-X and the International Data Spaces, using the Dataspace Connector,' and that Fraunhofer ISST contributed International Data Spaces components 'further developed and industrially hardened in the consortium.' ARENA2036's own page, read directly, states Catena-X was 'established as a data space for the automotive industry based on GAIA-X and International Data Spaces.' Fraunhofer IFF's own page, read directly, confirms the Gaia-X basis but does not itself mention IDS. This closes a gap queued in discovery/research-queue.md since Batch 5."
    confidence: high
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-GAIA-X
    source: fact
    evidence: "Confirmed by reading Fraunhofer IFF's own page directly (2026-08-28): Catena-X 'creates a distributed GAIA-X-based data ecosystem built on European standards,' and Fraunhofer ISST's own page (see above) and ARENA2036's own page both independently confirm the same Gaia-X basis in their own words. ARENA2036 additionally describes Catena-X as 'the first major use case of GAIA-X via system-relevant representatives of the automotive value chain.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Offener und kollaborativer Datenraum für die Automobilindustrie (Projekt Catena-X)"
    url: "https://www.iff.fraunhofer.de/de/geschaeftsbereiche/logistik-fabriksysteme/catena-x.html"
    publisher: "Fraunhofer-Institut für Fabrikbetrieb und -automatisierung (IFF)"
    accessed: "2026-08-28"
  - title: "Catena-X Automotive Network — Alliance for secure and standardized data exchange"
    url: "https://www.isst.fraunhofer.de/en/departments/industrial-manufacturing/projects/CatenaX.html"
    publisher: "Fraunhofer-Institut für Software- und Systemtechnik (ISST)"
    accessed: "2026-08-28"
  - title: "Catena-X — Datenökosystem für die Autoindustrie"
    url: "https://www.automotiveit.eu/catena-x"
    publisher: "automotiveIT"
    accessed: "2026-08-28"
  - title: "Catena-X"
    url: "https://arena2036.de/en/catena-x/"
    publisher: "ARENA2036"
    accessed: "2026-08-28"
  - title: "Was ist Catena-X?"
    url: "https://www.springerprofessional.de/automobilwirtschaft/unternehmen---institutionen/was-ist-catena-x-/50174986"
    publisher: "Springer Professional"
    accessed: "2026-08-28"
  - title: "Catena-X Launches World's First Cross-Border Automotive Industry Data Ecosystem Between China and Europe"
    url: "https://catena-x.net/news/catena-x-launches-worlds-first-cross-border-automotive-industry-data-ecosystem-between-china-and-europe/"
    publisher: "Catena-X Automotive Network e.V."
    accessed: "2026-09-13"
  - title: "Catena-X launches China-Europe auto data ecosystem"
    url: "https://www.bestmag.co.uk/catena-x-launch-china-europe-auto-data-ecosystem/"
    publisher: "Best Magazine"
    accessed: "2026-09-13"
---

# Catena-X Automotive Network

> **Re-verified 2026-08-28.** All five cited sources were fetched. Four
> loaded directly (one — the originally-cited `isst.fraunhofer.de`
> `/mobility-und-smart-cities/` URL — had gone dead and was replaced with
> the institute's current URL for the same page, found via search); the
> Springer Professional page is paywalled and returned only a stub.
> `verification: primary-source`. Both relationships this entity carries
> are now confirmed by two or three independently-read primary pages each,
> not the search-engine snippets they previously rested on.
>
> **Narrowed 2026-09-13**, closing part of `discovery/unresolved.md` row
> #64 (the row asked for a directly-cited `catena-x.net` source; the
> previous pass consulted the site via search but did not add it to the
> formal source list). A catena-x.net press release, read directly and
> now added as a frontmatter source, and an independent trade-press
> corroboration give the "contested practical record" section below a
> concrete, dated, named operational milestone rather than only the
> operator's general "fully operational" claim.

## Description

Catena-X was founded as an association — **Catena-X Automotive Network
e.V.** — in May 2021, and its founding research consortium ran, per
Fraunhofer IFF's own page (read directly), from **August 2021 to July
2024**. No source read this pass states a specific day for either event, so
`start_date` is left `null` rather than the fabricated `2021-01-01` this
entity previously carried; the year-and-phase precision is recorded in
prose instead.

It is a **distributed [[EU-GAIA-X]]-based data ecosystem built on European
standards**, confirmed directly this pass on three independent pages —
Fraunhofer IFF's, Fraunhofer ISST's and ARENA2036's own sites all state the
Gaia-X basis in their own words, and ARENA2036 goes further, calling it
"the first major use case of GAIA-X" in the automotive value chain. It
**follows the International Data Spaces (IDS) reference architecture**,
also confirmed directly: ISST's own page states plainly that "Catena-X is
based on GAIA-X and the International Data Spaces, using the Dataspace
Connector," and names Fraunhofer ISST's own contribution of IDS components
to the consortium. That Dataspace Connector is now its own Atlas entity,
[[INTL-IDS-CONNECTOR]], created 2026-09-19.

It is the data-centric platform on which vehicle manufacturers, suppliers
and service providers exchange information securely along the automotive
value chain. Its reach is not European-only: a Catena-X hub opened in
Shanghai in 2024, and current news on catena-x.net (read directly this
pass) describes ongoing cross-border operations between China and Europe
and a new €23 million "Data Space Accelerator" initiative.

## A contested practical record, read directly this pass

catena-x.net's own current page, read directly, describes the network as
"fully operational and entering its next phase of adoption." A WirtschaftsWoche
investigative piece, also read directly (2026-08-28), takes the opposite
view: journalist Michael Kroker calls Catena-X "the greatest IT hot air of
German industry," reports spending two and a half years unable to find
concrete operating examples beyond isolated pilots (BMW's CO2 tracking,
Fujitsu's identity-management work), and describes the industry consortium
Cofinity-X as unresponsive to enquiries.

Both are read directly and both are kept. The Atlas records that Catena-X's
own operator and an investigative business publication disagree sharply on
whether the network delivers in practice, rather than adopting either
side's framing. `status: active` reflects that the network continues to
exist and expand institutionally; it says nothing about adoption, which
remains contested per the sources above.

**A concrete milestone, added 2026-09-13.** Confirmed by reading
catena-x.net's own press release directly (22 July 2026), corroborated
independently by Best Magazine's trade-press coverage: Catena-X named
**Zhonglian** as its **second operating partner and first presence
outside Europe**, to run core market services and act as the regulatory
interface for a new cross-border data ecosystem linking Europe and China,
launched jointly with the China Association of Automobile Manufacturers
(CAAM) and VDA China. Operations are scheduled to begin **mid-November
2026**. The stated purpose is battery-passport data recognised under both
Chinese and EU rules ahead of the EU Battery Regulation's mandatory
battery-passport requirement from **February 2027** — the Battery
Regulation itself is not an Atlas entity, and no edge is asserted to it.
This is a specific, named, dated commitment rather than the general
"fully operational" language the operator's page already carried, though
it does not on its own resolve WirtschaftsWoche's separate scepticism
about adoption depth within Europe.

## ⚠ `country: DE` is the weakest field in this entity

Catena-X is recorded as German on the basis of German origin and German
institutional backing — the cited Fraunhofer institutes, ARENA2036, the
German automotive industry — a basis unchanged by this pass's fetches,
which if anything sharpen the point: ARENA2036's own page frames Catena-X's
purpose as serving "the international competitiveness of the German **and
European** automotive industry" without calling the network itself German.

That is a thin basis, and it is the **same problem [[NL-ISHARE]] already
has**. iSHARE was recorded `country: NL` for its Dutch origin while
operating at ishare.eu in a European data-space context; its entity body
calls this "exactly the case the `country` field handles least well" and
flags it as provisional. Catena-X is the identical case in a second
country, with a Shanghai hub and a Chinese industry agreement making it
sharper still.

Two independent instances mean this is **a property of the model, not of
either entity**. The `country` field conflates three different things —
where an initiative originated, where it is governed, and where it
operates — and industry data spaces routinely differ on all three.

`level: sectoral` is recorded rather than `national`, which is at least
honest about the second axis. The `country` field is logged as an open
ontology question in `discovery/unresolved.md`, now with two supporting
cases rather than one.

## The IDS reference architecture is not an entity

Catena-X follows the **International Data Spaces reference architecture**,
and [[NL-ISHARE]] records that the IDSA incorporated the iSHARE agreement
system into the IDS architecture. Two entities in two countries now point
at the same missing node.

**Neither the IDSA nor the IDS-RAM is an Atlas entity**, and neither is
created here: even with this pass's direct reads, the sources describe IDS
as a component Catena-X uses, not enough to build an international
standards body on. This is now the best-evidenced gap in the Atlas's
international layer — two independent references from two national data
spaces, both now confirmed by primary reading rather than search
snippets — and it is queued in `discovery/research-queue.md` accordingly.

## Manufacturing-X and the wider family

Catena-X sits within a broader German industrial data-space family
including [[DE-MANUFACTURING-X]], confirmed this pass as the initiative
Catena-X's approach was generalised into. **Closed 2026-09-19**:
[[DE-FACTORY-X]], Manufacturing-X's mechanical-engineering lighthouse
project, is now an Atlas entity, `based-on` this one and `part-of`
[[DE-MANUFACTURING-X]]. No other family member is modelled, and no
industry or manufacturing domain entity was created:
`metadata/taxonomy.md` §1 requires a domain to connect at least two
entities, and Catena-X alone does not meet the threshold. `domains: []` is
therefore correct rather than an omission.

## Relationships

- `based-on` [[EU-GAIA-X]] — confirmed this pass, `confidence: high`.
- `based-on` [[INTL-IDS-RAM]] — confirmed this pass, `confidence: high`.

## Sources

Listed in frontmatter, seven of seven read directly across two passes.
The original five: four loaded with substantive content, one (Springer
Professional) paywalled to a stub. Two added 2026-09-13 — catena-x.net's
own press release and an independent trade-press corroboration — closing
the previous gap where the operator's site was consulted via search but
never added as a formal citation.
