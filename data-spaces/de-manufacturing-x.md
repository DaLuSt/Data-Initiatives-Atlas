---
id: DE-MANUFACTURING-X
type: data-space
name: Manufacturing-X
alternative_names:
  - Manufacturing X
description: >
  German cross-sector industrial data ecosystem initiative, funded by the
  Federal Ministry for Economic Affairs with up to 150 million euros and
  moderated by it with support from the Federal Ministry of Education and
  Research. It followed Catena-X, the automotive data space, and extends the
  same approach across industry; the Factory-X lighthouse project for
  mechanical and industrial engineering was launched under it in 2024.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - DE-CATENA-X
  - EU-MANUFACTURING-DATA-SPACE
relationships:
  - type: applies-in
    target: DE
    source: fact
    evidence: "Manufacturing-X is a German initiative: the Federal Ministry for Economic Affairs and Climate Protection is funding the development of a cross-sector digital ecosystem for industrial data exchange with up to EUR 150 million, and the Manufacturing-X Council Germany is moderated by that ministry with support from the Federal Ministry of Education and Research (bundeswirtschaftsministerium.de 'Manufacturing-X Funding Program'; plattform-i40.de 'Manufacturing-X Council Germany'; isst.fraunhofer.de 'Manufacturing-X'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: DE-CATENA-X
    source: fact
    evidence: "The BMWK launched Catena-X, a data room for the automotive industry; this was followed by the more comprehensive Manufacturing-X initiative, whose primary goal is the creation of an open and collaborative data ecosystem for factory equipment suppliers and operators on the basis of Catena-X and concepts from Plattform Industrie 4.0 (iosb.fraunhofer.de 'Factory-X'; isst.fraunhofer.de 'Manufacturing-X'; bundeswirtschaftsministerium.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Manufacturing-X Funding Program"
    url: "https://www.bundeswirtschaftsministerium.de/Redaktion/EN/Dossier/manufacturing-x.html"
    publisher: "Bundesministerium für Wirtschaft und Energie (BMWE)"
  - title: "Manufacturing-X Council Germany"
    url: "https://www.plattform-i40.de/IP/Navigation/EN/Manufacturing-X/Manufacturing-X-Council-Germany/manufacturing-x-council-germany.html"
    publisher: "Plattform Industrie 4.0"
  - title: "Manufacturing-X"
    url: "https://www.isst.fraunhofer.de/en/departments/industrial-manufacturing/manufacturing-x.html"
    publisher: "Fraunhofer ISST"
  - title: "Factory-X — a sovereign data room for mechanical and industrial engineering"
    url: "https://www.iosb.fraunhofer.de/en/projects-and-products/factory-x.html"
    publisher: "Fraunhofer IOSB"
---

# Manufacturing-X

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Manufacturing-X is Germany's cross-sector industrial data ecosystem
initiative, funded by the federal economics ministry with **up to €150
million** and moderated by it, with support from the research ministry,
through the Manufacturing-X Council Germany.

## The Atlas's first data-space *lineage*

Every other data space in the Atlas stands alone or hangs off the EU
umbrella. This one has an ancestor, and the sources state it plainly: the
BMWK launched [[DE-CATENA-X]] for the automotive industry, **this followed**,
and its goal is a data ecosystem for factory equipment suppliers and
operators **on the basis of Catena-X** and concepts from Plattform Industrie
4.0.

So the graph can now show a sector data space being generalised into an
industrial one — `based-on` rather than `part-of`, because Manufacturing-X
does not contain Catena-X, it builds on it.

Germany's family, as the sources describe it: **Catena-X** for cars,
**Manufacturing-X** for factories, **energy data-X** for power, and
**Factory-X** (2024) and **Aerospace-X** as lighthouse projects within
Manufacturing-X.

## No edge to [[EU-MANUFACTURING-DATA-SPACE]]

The German initiative and the common European manufacturing data space
occupy the same sector, and it would be easy to draw a line between them.

**No source read states one.** The EU data space's own deployment projects
are named as UNDERPIN and SM4RTENANCE, neither of which the sources connect
to Manufacturing-X, and a national initiative predating the EU deployment is
not thereby part of it. The question is logged in `discovery/unresolved.md`.

## Not modelled

- **Factory-X**, **Aerospace-X** and **energy data-X** — lighthouse projects
  and sibling initiatives named in the sources.
- **Plattform Industrie 4.0**, whose concepts Manufacturing-X builds on and
  which publishes the Council's material.
- The **BMWK/BMWE** itself. No German ministry other than [[DE-BMI]] is an
  Atlas entity, so no `part-of` edge is asserted — the same coverage limit
  recorded on [[DE-BND]].

## Sources

Listed in frontmatter.
