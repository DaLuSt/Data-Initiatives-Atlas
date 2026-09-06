---
id: GB-DI
type: organisation
name: Defence Intelligence
alternative_names:
  - DI
description: >
  The United Kingdom's military intelligence organisation, providing
  strategic defence intelligence to the Ministry of Defence and the
  armed forces. Unlike the Security Service, the Secret Intelligence
  Service and GCHQ, it is an integral part of a government department
  (the MOD, within Strategic Command) rather than an independent
  statutory body, and has no equivalent avowal act.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - GB-IPA-2016
  - GB-ISC
  - GB-IPCO
  - GB-MI5
relationships:
  - type: governed-by
    target: GB-IPA-2016
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (GB-MI5's own 'Not modelled' section, which named Defence Intelligence as having 'no equivalent avowal act' and left it unresearched). Confirmed by reading gov.uk's own 'Defence Intelligence' group page directly (2026-09-06): DI's activity 'must comply with' the Regulation of Investigatory Powers Act 2000 and the Investigatory Powers Act 2016 (RIPA 2000 is not itself an Atlas entity — see GB-MI5's 'Not modelled' section)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Defence Intelligence"
    url: "https://www.gov.uk/government/groups/defence-intelligence"
    publisher: "GOV.UK (Ministry of Defence)"
    accessed: "2026-09-06"
  - title: "Defence Intelligence"
    url: "https://en.wikipedia.org/wiki/Defence_Intelligence"
    publisher: "Wikipedia"
    accessed: "2026-09-06"
  - title: "Justice and Security Act 2013, Section 2"
    url: "https://www.legislation.gov.uk/ukpga/2013/18/section/2"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-09-06"
---

# Defence Intelligence (DI)

> **Created 2026-09-06**, closing a gap [[GB-MI5]] flagged explicitly:
> "Defence Intelligence, the UK's military intelligence organisation,
> ... has no equivalent avowal act and was not researched. The UK
> therefore appears here with three services where France has four and
> Poland four." gov.uk's own page and Wikipedia agree: DI genuinely has
> no avowal act — this is a documented negative, not a research gap —
> because it is not an independent body at all.

## Description

Confirmed by reading gov.uk's own "Defence Intelligence" group page
directly: DI "empowers decision makers in the Ministry of Defence (MOD)
and UK government by providing intelligence products and assessments,"
working "in close partnership with" MI5, MI6 and GCHQ. It sits within
**Strategic Command** and has roughly **5,000 staff**, two-thirds armed
forces personnel and one-third civilians.

## Why it has no avowal act — a documented negative, not a gap

Confirmed by reading Wikipedia's own article directly, which states the
key structural difference plainly: DI "differs from the UK's intelligence
agencies (MI6, GCHQ and MI5) in that it is an integral part of a
government department — the Ministry of Defence — rather than operating
independently." There was never a Security Service Act 1989 or
Intelligence Services Act 1994 equivalent to avow, because DI is not a
freestanding body the way [[GB-MI5]], [[GB-SIS]] and [[GB-GCHQ]] are — it
is a directorate of the MOD. The UK's three-service count on [[GB-MI5]]
is therefore not an omission; DI is a fourth kind of body the same
question doesn't apply to in the same way.

## Oversight without an avowal act

DI is not left ungoverned. gov.uk's own page, read directly, states its
activity "must comply with" the Regulation of Investigatory Powers Act
2000 and [[GB-IPA-2016]], and names two oversight bodies: the
**Investigatory Powers Commissioner** and the **Parliamentary Intelligence
and Security Committee**, which "oversees the administration, policy and
expenditure of Defence Intelligence."

The [[GB-ISC]]'s statutory oversight of [[GB-MI5]], [[GB-SIS]] and
[[GB-GCHQ]] runs through **§2(1)** of the Justice and Security Act 2013,
naming those three bodies specifically. DI's oversight runs through the
different mechanism in **§2(2)**, confirmed by reading the Act's own text
directly: the ISC "may examine or otherwise oversee such other activities
of Her Majesty's Government in relation to intelligence or security
matters as are set out in a memorandum of understanding" — a weaker,
non-statutory-list basis than §2(1)'s. No `applies-to` edge from
[[GB-ISC]] is added here for that reason: the evidence is gov.uk's own
prose statement of the oversight relationship, not a citable §2(1)-style
statutory list entry, and the distinction between the two mechanisms is
itself the finding worth recording accurately.

## Not modelled

- The **memorandum of understanding** under JSA 2013 §2(2) that actually
  extends ISC oversight to DI — not located as a citable document this
  pass.
- DI's own **internal structure and specific units**.

## Relationships

- `governed-by` [[GB-IPA-2016]].

## Sources

Listed in frontmatter, all three read directly 2026-09-06.
