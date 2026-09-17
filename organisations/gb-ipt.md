---
id: GB-IPT
type: organisation
name: Investigatory Powers Tribunal
alternative_names:
  - IPT
  - The Tribunal
description: >
  Independent UK judicial body established by Part IV of the Regulation
  of Investigatory Powers Act 2000, hearing complaints from anyone who
  believes they have been the victim of unlawful conduct by a public
  authority using covert investigatory techniques, including conduct
  by the intelligence services. It has UK-wide jurisdiction, can award
  compensation and cancel warrants or authorisations, and — separately
  from the Investigatory Powers Commissioner's Office, which oversees
  the use of covert powers — adjudicates complaints about them.

level: national
country: GB
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: "2000-07-28"
end_date: null
last_verified: "2026-09-17"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - GB
  - GB-RIPA-2000
  - GB-IPCO
  - GB-MI5
  - GB-SIS
  - GB-GCHQ
relationships:
  - type: governed-by
    target: GB-RIPA-2000
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (named on GB-MI5, GB-IPA-2016 and GB-RIPA-2000's own files as an unmodelled body distinct from GB-IPCO). Confirmed by reading legislation.gov.uk's own text of RIPA 2000 Part IV directly (2026-09-17): section 65 establishes 'The Tribunal', with jurisdiction to hear proceedings regarding intelligence-service conduct and complaints about investigatory-powers use, including (since a 2024 amendment) 'relevant personal data breaches'; section 67 gives it power to make compensation awards and cancel warrants or authorisations."
    confidence: high
    valid_from: "2000-07-28"
    valid_until: null
  - type: part-of
    target: GB
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading investigatorypowerstribunal.org.uk's own homepage directly (2026-09-17): the Tribunal describes itself as 'an independent judicial body' with UK-wide jurisdiction considering complaints about unlawful covert investigative techniques by public authorities, including UK intelligence services (MI5, MI6 and GCHQ)."
    confidence: high
    valid_from: "2000-07-28"
    valid_until: null

sources:
  - title: "Regulation of Investigatory Powers Act 2000, Part IV"
    url: "https://www.legislation.gov.uk/ukpga/2000/23/part/IV"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-09-17"
  - title: "Investigatory Powers Tribunal — homepage"
    url: "https://investigatorypowerstribunal.org.uk/"
    publisher: "Investigatory Powers Tribunal"
    accessed: "2026-09-17"
---

# Investigatory Powers Tribunal (IPT)

> **Created 2026-09-17**, closing a gap flagged on three files this
> pass: [[GB-MI5]], [[GB-IPA-2016]] and the newly-created
> [[GB-RIPA-2000]] all separately named the Tribunal as unmodelled and
> distinct from [[GB-IPCO]]. Both RIPA's own Part IV text and the
> Tribunal's own homepage were read directly.

## Description

Confirmed by reading the Tribunal's own homepage directly: it is "an
independent judicial body" providing "the right of redress to anyone
who believes they have been the victim of unlawful action by a public
authority using covert investigative techniques." It has UK-wide
jurisdiction, considering complaints about unlawful covert
investigative techniques by public authorities and conduct by or on
behalf of the UK's intelligence services (the Tribunal's own page
names MI5, MI6 and GCHQ specifically).

## Established by RIPA, not by the 2016 Act

Confirmed by reading [[GB-RIPA-2000]]'s own Part IV directly:
**Section 65** establishes "The Tribunal," with jurisdiction over
proceedings concerning intelligence-service conduct and complaints
about the use of investigatory powers — extended in 2024 to cover
"relevant personal data breaches." **Section 67** gives the Tribunal
power to make **compensation awards** and to **cancel warrants or
authorisations**. Unlike the original Interception of Communications
Commissioner and Intelligence Services Commissioner (RIPA ss.57–63,
repealed in 2017 and replaced by [[GB-IPCO]]), the Tribunal was never
one of the offices [[GB-IPCO]] absorbed — it has operated continuously
under RIPA's own Part IV since 2000.

## Oversight versus adjudication

[[GB-IPCO]]'s own file already draws this line in prose: "IPCO
oversees; the Tribunal adjudicates. They are separate." This entity
completes that distinction with a body of its own — [[GB-IPCO]]
reviews and authorises covert-power use (including the "double lock"
warrant mechanism), while the Tribunal is the judicial forum a person
who believes they were the target of unlawful covert activity brings
a complaint to.

## Relationships

- `governed-by` [[GB-RIPA-2000]] — the Act whose own Part IV
  establishes the Tribunal.
- `part-of` [[GB]] — anchor edge.

No `applies-to` edge is asserted toward [[GB-MI5]], [[GB-SIS]] or
[[GB-GCHQ]]: the Tribunal's jurisdiction runs to complaints about any
public authority's covert conduct, not a bounded set of overseen
bodies the way [[GB-IPCO]]'s remit is — asserting `applies-to` for the
three named agencies would understate a jurisdiction the Tribunal's own
sources describe as running to "any public authority."

## Not modelled

- Individual case law or the Tribunal's own published rulings.
- Membership and the current President/Vice-President, which the
  Tribunal's own homepage names but which turns over frequently enough
  that a snapshot would go stale quickly.
- The appeals route from Tribunal decisions (to the Court of Appeal
  since 2019), not researched this pass.

## Sources

Two of two read directly this pass.
