---
id: GB-RIPA-2000
type: law
name: Regulation of Investigatory Powers Act 2000
alternative_names:
  - RIPA
  - RIPA 2000
description: >
  United Kingdom act (2000 c. 23), Royal Assent 28 July 2000, providing
  for the interception of communications, the acquisition of
  communications data, covert surveillance, covert human intelligence
  sources, and powers to require disclosure of encryption keys, plus
  Commissioners and a Tribunal to oversee them. Its Part I (interception
  and communications-data acquisition) has been entirely superseded by
  the Investigatory Powers Act 2016, but Part II (surveillance and
  covert human intelligence sources), Part III (encryption-key
  disclosure) and the Investigatory Powers Tribunal established by
  Part IV remain in force.

level: national
country: GB
region: null

status: active
confidence: high
coverage: medium
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
  - GB-IPA-2016
  - GB-MI5
  - GB-SIS
  - GB-GCHQ
relationships:
  - type: applies-in
    target: GB
    source: fact
    evidence: "Confirmed by reading legislation.gov.uk's own introductory text directly (2026-09-17): the Act provides 'for and about the interception of communications, the acquisition and disclosure of data relating to communications, the carrying out of surveillance, the use of covert human intelligence sources and the acquisition of the means by which electronic data protected by encryption or passwords may be decrypted or accessed... by the Security Service, the Secret Intelligence Service and the Government Communications Headquarters.' Anchor edge under metadata/relationship-types.md §2.3."
    confidence: high
    valid_from: "2000-07-28"
    valid_until: null

sources:
  - title: "Regulation of Investigatory Powers Act 2000 — Introductory Text"
    url: "https://www.legislation.gov.uk/ukpga/2000/23/introduction"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-09-17"
  - title: "Regulation of Investigatory Powers Act 2000, Part I"
    url: "https://www.legislation.gov.uk/ukpga/2000/23/part/I"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-09-17"
  - title: "Regulation of Investigatory Powers Act 2000, Part II"
    url: "https://www.legislation.gov.uk/ukpga/2000/23/part/II"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-09-17"
  - title: "Regulation of Investigatory Powers Act 2000, Part III"
    url: "https://www.legislation.gov.uk/ukpga/2000/23/part/III"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-09-17"
  - title: "Regulation of Investigatory Powers Act 2000, Part IV"
    url: "https://www.legislation.gov.uk/ukpga/2000/23/part/IV"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-09-17"
---

# Regulation of Investigatory Powers Act 2000 (RIPA)

> **Created 2026-09-17**, closing a gap flagged on both
> [[GB-IPA-2016]] ("RIPA 2000, largely superseded by this act but not
> wholly repealed") and [[GB-MI5]] ("substantially superseded... but
> not wholly repealed"). All five Parts' current-status notes were
> read directly at legislation.gov.uk this pass, since which parts
> remain in force turned out to be the actual substance worth
> recording — RIPA is not a bare repeal fact.

## Description

Confirmed by reading the Act's own introductory text directly at
legislation.gov.uk: RIPA received **Royal Assent on 28 July 2000** and
provides "for and about the interception of communications, the
acquisition and disclosure of data relating to communications, the
carrying out of surveillance, the use of covert human intelligence
sources and the acquisition of the means by which electronic data
protected by encryption or passwords may be decrypted or accessed... by
the Security Service, the Secret Intelligence Service and the
Government Communications Headquarters."

## Which parts survived the Investigatory Powers Act 2016 — read part by part

This is the fact the "largely superseded but not wholly repealed"
shorthand on [[GB-IPA-2016]] and [[GB-MI5]] left unstated. Reading each
Part's own current-status note directly at legislation.gov.uk:

| Part | Subject | Status as of 2026-09-17 |
|---|---|---|
| **I** | Interception of communications (Ch. I); acquisition/disclosure of communications data (Ch. II) | **Entirely superseded** — Chapter I "substantially omitted" by [[GB-IPA-2016]], phased out March–December 2018; Chapter II "entirely omitted" as of 22 July 2020 |
| **II** | Directed and intrusive surveillance; covert human intelligence sources | **Remains in force.** The 2016 Act did not supersede it — it created a complementary framework instead (s.27(4) now cross-refers to "an enactment contained in this Act or the Investigatory Powers Act 2016"). Substantially expanded by the Covert Human Intelligence Sources (Criminal Conduct) Act 2021 (new ss.29B–29D, in force August–September 2021) |
| **III** | Powers to require disclosure of encryption keys / protected electronic data | **Remains in force**, with some amendments from the IPA 2016 and the Armed Forces Act 2021 still pending implementation |
| **IV** | Oversight: Commissioners and the Tribunal | **Mixed.** The original Interception of Communications Commissioner and Intelligence Services Commissioner (ss.57–60) and the separate surveillance-commissioner roles (ss.62–63) were repealed in 2017, replaced by [[GB-IPCO]]. The **Investigatory Powers Commissioner for Northern Ireland** (s.61) and **the Tribunal** (ss.65–67) remain in force — the Tribunal's jurisdiction was extended in 2024 to cover "relevant personal data breaches" |
| **V** | Miscellaneous, amendments to other acts | Not separately researched this pass |

## The Investigatory Powers Tribunal is still RIPA's, not IPCO's

[[GB-IPA-2016]] and [[GB-MI5]] both separately flag the Investigatory
Powers Tribunal as unmodelled and distinct from [[GB-IPCO]]. Now
confirmed directly: the Tribunal is established by **RIPA's own
Part IV, sections 65–67** — it was never one of the offices IPCO
absorbed. It hears complaints about intelligence-service conduct and
investigatory-powers use, and can award compensation or cancel
warrants and authorisations.

## Relationships

- `applies-in` [[GB]] — anchor edge.

No `supersedes` edge is asserted from [[GB-IPA-2016]] to this entity:
the relationship is real for Part I alone, and the Atlas's vocabulary
gap for "comprehensively revised but did not repeal" (see
`discovery/unresolved.md` ontology item #7, also affecting
[[DE-NIS2UMSUCG]] → [[DE-BSIG]]) applies here too, now with a third
example. Asserting `supersedes` at the whole-entity level would
misstate Parts II–IV, which is exactly the case for not forcing it.

## Not modelled

- Part V (Miscellaneous) and the Act's amendments to other legislation.
- The Investigatory Powers Tribunal as its own entity — flagged here
  and on [[GB-IPA-2016]]/[[GB-MI5]], not yet created; it would need its
  own membership, procedure and caseload research beyond what this
  batch covered.
- The Investigatory Powers (Amendment) Act 2024's effect on RIPA
  specifically (as opposed to the IPA 2016).

## Sources

Five of five pages read directly this pass: the introductory text and
all four Parts' current-status notes.
