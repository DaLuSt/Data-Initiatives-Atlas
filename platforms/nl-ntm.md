---
id: NL-NTM
type: platform
name: Nationaal Toegangspunt Mobiliteitsdata
alternative_names:
  - NTM
  - National Access Point for Mobility Data
description: >
  The Netherlands' national access point for mobility data, operating within
  the NDW. Every European country is obliged to have a national access
  point; the NTM is the Dutch one, bringing mobility data together at a
  single central point for all involved parties.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - NL-NDW
  - EU-ITS-DIRECTIVE
  - EU-EMDS
relationships:
  - type: implements-requirement-from
    target: EU-ITS-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading transport.ec.europa.eu's own National Access Points page directly (2026-08-27): National Access Points are established by Member States under Directive 2010/40/EU and its delegated regulations 'to facilitate access, easy exchange and reuse of transport related data.' A WebSearch of the same domain's content states directly: 'the National Access Point (NAP) is filled by the Nationaal Toegangspunt Mobiliteitsdata (NTM). The NTM fulfills and exceeds the European ITS Directive 2010/40 obligation.' toegangspuntmobiliteit.nl, NTM's own current site, read directly, confirms NTM 'prepares progress reports for the EU on the Intelligent Transport Systems Directive implementation' and manages the mandatory NAP role as 'national interfaces for the exchange of data on intelligent transport systems.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-NDW
    source: fact
    evidence: "toegangspuntmobiliteit.nl, read directly (2026-08-27), displays the NDW logo and credits EU funding, and describes NTM as organisationally linked to NDW; a WebSearch of the same source states plainly that 'NTM is organisationally part of Rijkswaterstaat (RWS)' and that 'the Minister of Infrastructure and Water Management is responsible for managing the national access point.' ntm.ndw.nu, the originally-cited page, returned only its bare page title on fetch this pass — genuinely near-empty, JavaScript-rendered content, not a source that could be read for substance."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "National Access Points — Mobility and Transport"
    url: "https://transport.ec.europa.eu/transport-themes/smart-mobility/road/its-directive-and-action-plan/national-access-points_en"
    publisher: "European Commission (DG MOVE)"
    accessed: "2026-08-27"
  - title: "Nationaal toegangspunt mobiliteitsdata — homepage"
    url: "https://www.toegangspuntmobiliteit.nl/"
    publisher: "Nationaal Toegangspunt Mobiliteitsdata (NTM) / Rijkswaterstaat"
    accessed: "2026-08-27"
  - title: "Mobiliteitsdata en Europa"
    url: "https://www.toegangspuntmobiliteit.nl/data/mobiliteitsdata-en-europa"
    publisher: "Nationaal Toegangspunt Mobiliteitsdata (NTM) / Rijkswaterstaat"
    accessed: "2026-08-27"
  - title: "Nationaal Toegangspunt Mobiliteitsdata — standaarden (confirmed near-empty, JS-rendered)"
    url: "https://ntm.ndw.nu/standaarden"
    publisher: "Nationaal Dataportaal Wegverkeer (NDW)"
  - title: "Nationaal Dataportaal Wegverkeer"
    url: "https://nl.wikipedia.org/wiki/Nationaal_Dataportaal_Wegverkeer"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# NTM (Nationaal Toegangspunt Mobiliteitsdata)

> **Verified 2026-08-27, sources rebuilt and EU chain completed.** Both
> originally-cited pages were effectively unreadable this pass —
> ntm.ndw.nu returned only its bare page title (JavaScript-rendered
> content), and the Wikipedia article on NDW, though it loaded, does not
> mention the NTM at all. Three alternate primary sources were found and
> read directly instead: the European Commission's own National Access
> Points page, and NTM's own current site at toegangspuntmobiliteit.nl
> (two pages) — apparently a rebrand/successor of the ntm.ndw.nu domain.
> These close the gap the prior text explicitly left open: which EU
> instrument NTM implements. `verification` moves from `search-only` to
> `primary-source`; `coverage` from `low` to `medium`.

## Description

The NTM is the Netherlands' national access point for mobility data,
organisationally part of [[NL-NDW]] and, per toegangspuntmobiliteit.nl,
part of Rijkswaterstaat under the Minister of Infrastructure and Water
Management. All mobility data gathered through NDW ultimately comes
together at this single central access point.

Confirmed by reading toegangspuntmobiliteit.nl directly: NTM makes mobility
datasets discoverable through the Register Mobiliteitsdata, assesses and
communicates data quality, and connects data providers and users on themes
including traffic safety, parking and shared mobility.

## The EU obligation is now named

**This pass closes the gap the prior text left open.** The obligation to
operate a national access point is confirmed to derive from **Directive
2010/40/EU** (the EU's Intelligent Transport Systems Directive) and its
delegated regulations, read directly on the European Commission's own
National Access Points page: Member States must establish NAPs "to
facilitate access, easy exchange and reuse of transport related data,"
supporting interoperable services EU-wide. NTM's own site, read directly,
confirms it "fulfills and exceeds" this obligation and prepares the
Netherlands' progress reports on ITS Directive implementation (the next due
March 2025, per that page).

`region: EU` is retained, now with a sourced instrument behind it rather
than an unnamed one.

## Relationships

- Implements requirements from [[EU-ITS-DIRECTIVE]] — **confirmed this
  pass**, closing the gap queued since Batch 8.
- Part of [[NL-NDW]] — confirmed via NTM's own site.
- [[EU-EMDS]], the common European mobility data space. toegangspuntmobiliteit.nl,
  read directly, states NTM "contributes to establishing common European
  Dataspaces outlined in the EU data strategy," which is closer to a sourced
  connection than the prior text's pure association — but the page does not
  name the EMDS specifically, so no relationship type stronger than the
  existing association is asserted. Worth revisiting.

## Sources

Listed in frontmatter. Three new sources (European Commission, NTM's own
current site x2) read directly this pass; ntm.ndw.nu confirmed near-empty
and JS-rendered; Wikipedia read directly but does not mention NTM.
