---
id: NL-UVW
type: organisation
name: Unie van Waterschappen
alternative_names:
  - UvW
  - Dutch Water Authorities
description: >
  Umbrella organisation representing the twenty-one Dutch water authorities
  (waterschappen). Within the data/digital ecosystem it supports joint
  digital development across the water authorities, including data
  management and information security, and represents them in
  government-wide digital governance.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-VNG
  - NL-IPO
relationships:
  - type: participates-in
    target: NL-OBDO
    source: fact
    evidence: "Confirmed by reading ibestuur.nl's article on the OBDO directly (2026-08-27), quoting the OBDO's own governance description: 'In dit overleg zijn alle departementen, Interprovinciaal Overleg (IPO), Unie van Waterschappen (UvW), CIO-Rijk en de voorzitter van de Programmeringsraad Logius vertegenwoordigd' (all ministries, IPO, UvW, CIO-Rijk and the chair of the Logius Programming Council are represented). Both originally-cited pages (unievanwaterschappen.nl and digitaleoverheid.nl) returned HTTP 403 / a bot-verification challenge on every fetch attempt this pass — genuinely blocked, not silently dropped — so this edge is now sourced to an alternate primary-adjacent report rather than to either original citation."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Heidag digitalisering decentrale overheden (confirmed genuinely blocked, HTTP 403)"
    url: "https://unievanwaterschappen.nl/heidag-digitalisering-decentrale-overheden/"
    publisher: "Unie van Waterschappen"
  - title: "Organisaties rondom digitalisering (confirmed genuinely bot-walled)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/organisaties-rondom-digitalisering/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "OBDO stelt Architectuur Digitale Overheid 2030 vast"
    url: "https://ibestuur.nl/artikel/obdo-stelt-architectuur-digitale-overheid-2030-vast/"
    publisher: "iBestuur"
    accessed: "2026-08-27"
  - title: "Unie van Waterschappen — Wikipedia"
    url: "https://nl.wikipedia.org/wiki/Unie_van_Waterschappen"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "Partners | Het Waterschapshuis"
    url: "https://www.hetwaterschapshuis.nl/partners"
    publisher: "Het Waterschapshuis"
    accessed: "2026-08-27"
---

# Unie van Waterschappen (UvW)

> **Verified 2026-08-27, sources rebuilt.** Both originally-cited pages
> (unievanwaterschappen.nl, digitaleoverheid.nl) are confirmed genuinely
> blocked to direct fetch on every attempt this pass — HTTP 403 and a
> bot-verification challenge respectively. Three alternate sources were
> found and read directly to replace them: iBestuur's OBDO reporting,
> Wikipedia, and Het Waterschapshuis's own partners page. `verification`
> moves from `search-only` to `primary-source` on the strength of those
> alternates, per the Atlas's established practice of substituting reachable
> primary-adjacent sources when an entity's original citations are
> genuinely stuck.

## Description

The Unie van Waterschappen represents the twenty-one Dutch water
authorities. Confirmed by reading nl.wikipedia.org directly: it was
established in 1927 when provincial water-board associations unified into a
national federation, and its role is "belangenbehartiging en het stimuleren
van kennisuitwisseling, samenwerking en innovatie" (interest representation
and fostering knowledge sharing, collaboration and innovation) — it
represents the waterschappen nationally and internationally, with around 70
staff. Wikipedia's own article, read directly, does not itself describe a
digital-government or data-governance role.

That role is confirmed by other sources read directly this pass. iBestuur's
reporting on the [[NL-OBDO]]'s own governance names the UvW explicitly as a
represented body. Het Waterschapshuis's own partners page, read directly,
distinguishes the two organisations precisely: the UvW "represents the water
authorities in the national and international arena," while Het
Waterschapshuis is a separate, independent regieorganisatie that "the
waterschappen themselves" established to manage shared ICT and ensure the
authorities "benefit from collaborations" — confirming the existing text's
description of Het Waterschapshuis as a distinct body, not a UvW subsidiary.
Het Waterschapshuis itself is still not an Atlas entity; queued in
`discovery/research-queue.md`.

The claim that the UvW, [[NL-VNG]] and [[NL-IPO]] jointly set digitalisation
priorities was not confirmed by any page read this pass and is left as an
unsourced association rather than an asserted relationship.

## Relationships

- Participates in [[NL-OBDO]] — confirmed this pass via iBestuur's reporting
  on the OBDO's own governance description, which names the UvW explicitly.
- The claimed co-signatory role on [[NL-NDS]] with [[NL-VNG]] and [[NL-IPO]]
  was not re-confirmed by any source read this pass; left as an unsourced
  association. See `discovery/unresolved.md`.

## Sources

Listed in frontmatter. iBestuur, Wikipedia and Het Waterschapshuis read
directly this pass; both original sources are confirmed genuinely blocked.
