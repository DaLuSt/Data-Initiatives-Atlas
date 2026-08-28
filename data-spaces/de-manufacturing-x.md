---
id: DE-MANUFACTURING-X
type: data-space
name: Manufacturing-X
alternative_names:
  - Manufacturing X
description: >
  German cross-sector industrial data ecosystem initiative, funded by the
  Federal Ministry for Economic Affairs (and Climate Action, since renamed
  Federal Ministry for Economic Affairs and Energy) with up to 150 million
  euros and moderated by it with support from the Federal Ministry of
  Research, Technology and Space. It followed Catena-X, the automotive data
  space, and extends the same approach across industry; the Factory-X
  lighthouse project for mechanical and industrial engineering was launched
  under it in 2024.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading oiger.de and the Plattform Industrie 4.0 Manufacturing-X Council Germany page directly (2026-08-28): the Federal Ministry for Economic Affairs and Climate Action funds Manufacturing-X with up to 150 million euros, and the Manufacturing-X Council Germany — 'the overarching body for coordinating the national cooperation of the Manufacturing-X initiative' — is 'moderated by the Federal Ministry of Economics and Energy (BMWE) and supported by the Federal Ministry of Research, Technology and Space (BMFTR)' (the ministries' post-2025 renamed successors of the BMWK and BMBF respectively). The ministry's own bundeswirtschaftsministerium.de pages returned a Radware bot-verification challenge on every attempt this pass and could not be read directly; oiger.de's direct reporting of the same 150-million-euro figure and Fraunhofer ISST's own page (also read directly) that Manufacturing-X 'is a global initiative funded by the Federal Ministry for Economic Affairs and Energy (BMWE)' substitute for it."
    confidence: high
    valid_from: null
    valid_until: null
  - type: based-on
    target: DE-CATENA-X
    source: fact
    evidence: "Confirmed by reading Fraunhofer ISST's own page and Fraunhofer IOSB's own Factory-X page directly (2026-08-28): ISST states Manufacturing-X 'builds upon and incorporates Catena-X principles' and that Fraunhofer ISST and Industry 4.0 platform representatives produced a 'Manufacturing-X Manifesto' laying out paths to interoperability between the initiatives, with Catena-X now 'one of several supported projects within the broader Manufacturing-X ecosystem.' IOSB's Factory-X page states directly: 'The German Federal Ministry for Economic Affairs and Climate Protection (BMWK) has launched Catena-X, a corresponding data room for the automotive industry. This was followed by the more comprehensive Manufacturing-X initiative.' oiger.de, also read directly, confirms Manufacturing-X 'is modeled directly after Catena-X.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Manufacturing-X Funding Program"
    url: "https://www.bundeswirtschaftsministerium.de/Redaktion/EN/Dossier/manufacturing-x.html"
    publisher: "Bundesministerium für Wirtschaft und Energie (BMWE)"
    accessed: "2026-08-28"
  - title: "Manufacturing-X Council Germany"
    url: "https://www.plattform-i40.de/IP/Navigation/EN/Manufacturing-X/Manufacturing-X-Council-Germany/manufacturing-x-council-germany.html"
    publisher: "Plattform Industrie 4.0"
    accessed: "2026-08-28"
  - title: "Manufacturing-X"
    url: "https://www.isst.fraunhofer.de/en/departments/industrial-manufacturing/manufacturing-x.html"
    publisher: "Fraunhofer ISST"
    accessed: "2026-08-28"
  - title: "Factory-X — a sovereign data room for mechanical and industrial engineering"
    url: "https://www.iosb.fraunhofer.de/en/projects-and-products/factory-x.html"
    publisher: "Fraunhofer IOSB"
    accessed: "2026-08-28"
  - title: "Bund gibt 150 Millionen Euro für „Manufacturing-X“"
    url: "https://oiger.de/2023/08/21/bund-gibt-150-millionen-euro-manufacturing-x/187925"
    publisher: "oiger.de"
    accessed: "2026-08-28"
---

# Manufacturing-X

> **Re-verified 2026-08-28.** Three of four originally-cited sources loaded
> directly; the fourth (`bundeswirtschaftsministerium.de`) returned a
> Radware bot-verification challenge on every attempt, confirmed by
> retrying, and was substituted with a directly-read alternate primary
> source (oiger.de's contemporaneous reporting, corroborated independently
> by Fraunhofer ISST's own page) covering the same €150 million funding
> fact. `verification: primary-source` — a genuine majority (four of five
> sources now listed) was read directly.

## Description

Manufacturing-X is Germany's cross-sector industrial data ecosystem
initiative, funded by the federal economics ministry (BMWK at launch in
2023, renamed BMWE) with **up to €150 million** — confirmed directly this
pass via oiger.de's contemporary reporting and via Fraunhofer ISST's own
current page, since the ministry's own dossier page could not be reached
past its bot-verification wall. It is moderated by that ministry through
the **Manufacturing-X Council Germany**, whose own page (Plattform
Industrie 4.0, read directly) confirms it is "moderated by the Federal
Ministry of Economics and Energy (BMWE) and supported by the Federal
Ministry of Research, Technology and Space (BMFTR)" — the post-2025
renamed successors of the BMWK and the education/research ministry named
in this entity's earlier text.

## The Atlas's first data-space *lineage*

Every other data space in the Atlas stands alone or hangs off the EU
umbrella. This one has an ancestor, and three independently-read sources
now confirm it directly: Fraunhofer ISST's own page states Manufacturing-X
"builds upon and incorporates Catena-X principles"; Fraunhofer IOSB's own
Factory-X page states plainly that the BMWK "launched Catena-X ... This was
followed by the more comprehensive Manufacturing-X initiative"; and
oiger.de's direct reporting states Manufacturing-X "is modeled directly
after Catena-X."

So the graph can now show a sector data space being generalised into an
industrial one — `based-on` rather than `part-of`, because Manufacturing-X
does not contain Catena-X, it builds on it — and that call is now backed by
primary reading rather than search snippets.

Germany's family, as the sources describe it: **Catena-X** for cars,
**Manufacturing-X** for factories, and — confirmed this pass via Fraunhofer
ISST's own page, which names Manufacturing-X's supported projects
directly — **Construct-X**, **Factory-X** (2024) and **Aerospace-X** as
lighthouse projects within Manufacturing-X. ISST's page also names
**HealthTrack-X**, not previously recorded here.

## No edge to [[EU-MANUFACTURING-DATA-SPACE]]

The German initiative and the common European manufacturing data space
occupy the same sector, and it would be easy to draw a line between them.

**No source read this pass states one**, including the two new sources
fetched (oiger.de, Fraunhofer IOSB's Factory-X page). The EU data space's
own deployment projects are named elsewhere as UNDERPIN and SM4RTENANCE,
neither of which any source read connects to Manufacturing-X, and a
national initiative predating the EU deployment is not thereby part of it.
The question remains logged in `discovery/unresolved.md`.

## Not modelled

- **Factory-X**, **Construct-X**, **Aerospace-X** and **HealthTrack-X** —
  lighthouse projects and sibling initiatives named directly in Fraunhofer
  ISST's own page.
- **Plattform Industrie 4.0**, whose concepts Manufacturing-X builds on and
  which publishes the Council's material.
- The **BMWK/BMWE** itself. No German ministry other than [[DE-BMI]] is an
  Atlas entity, so no `part-of` edge is asserted — the same coverage limit
  recorded on [[DE-BND]].

## Sources

Listed in frontmatter. The ministry's own dossier page (`bundeswirtschaftsministerium.de`)
returned only a Radware "please verify you are a human" challenge page on
every attempt — a genuinely blocked domain, not silently dropped — and
oiger.de's 2023 reporting was added as a directly-read substitute covering
the same funding fact. Plattform Industrie 4.0, Fraunhofer ISST and
Fraunhofer IOSB's own pages were all read directly and corroborate each
other independently.
