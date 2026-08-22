---
id: GB-MI5
type: organisation
name: Security Service
alternative_names:
  - MI5
  - The Security Service
description: >
  The United Kingdom's domestic security and counter-intelligence service.
  The Security Service Act 1989 placed it on a statutory basis and enabled
  certain actions to be taken on the authority of warrants issued by the
  Secretary of State. Its use of investigatory powers is governed by the
  Investigatory Powers Act 2016 and overseen by IPCO.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - GB-SSA-1989
  - GB-IPA-2016
  - GB-DPA-2018
  - GB-SIS
  - GB-GCHQ
  - GB-IPCO
  - GB-ISC
relationships:
  - type: governed-by
    target: GB-DPA-2018
    source: fact
    evidence: "Confirmed by reading the DPA 2018 statute text at legislation.gov.uk (2026-08-22), Part 4, § 82(2): 'In this Part, \"intelligence service\" means— (a) the Security Service; (b) the Secret Intelligence Service; (c) the Government Communications Headquarters.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: GB-SSA-1989
    source: fact
    evidence: "Confirmed by reading the SSA 1989 statute text at legislation.gov.uk (2026-08-22): 'An Act to place the Security Service on a statutory basis; to enable certain actions to be taken on the authority of warrants issued by the Secretary of State', enacted 27 April 1989."
    confidence: medium
    valid_from: 1989-01-01
    valid_until: null
  - type: governed-by
    target: GB-IPA-2016
    source: fact
    evidence: "Confirmed by reading the IPA 2016 statute text at legislation.gov.uk (2026-08-22): the Act's long title covers 'the interception of communications, equipment interference and the acquisition and retention of communications data, bulk personal datasets and other information', enacted 29 November 2016."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Security Service Act 1989"
    url: "https://www.legislation.gov.uk/ukpga/1989/5"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-08-22"
  - title: "Security Service Act 1989"
    url: "https://en.wikipedia.org/wiki/Security_Service_Act_1989"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Roles and Responsibilities of the Security Service and Secret Intelligence Service"
    url: "https://tile.loc.gov/storage-services/service/ll/llglrd/2024555215/2024555215.pdf"
    publisher: "Law Library of Congress"
    accessed: "2026-08-22"
  - title: "National Intelligence Machinery"
    url: "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/61808/nim-november2010.pdf"
    publisher: "Cabinet Office"
    accessed: "2026-08-22"
---

# Security Service (MI5)

> **Verified 2026-08-22.** The SSA 1989, IPA 2016 and DPA 2018 statute
> texts at legislation.gov.uk, now reachable in this environment, were
> read directly and confirmed the claims below.

## Description

Confirmed directly on legislation.gov.uk (2026-08-22): "An Act to place
the Security Service on a statutory basis; to enable certain actions to be
taken on the authority of warrants issued by the Secretary of State", the
SSA 1989's long title, enacted 27 April 1989. MI5 is the UK's **domestic**
security and counter-intelligence service. The
[[GB-SSA-1989]] placed it on a statutory basis — the operative word being
*placed*: the service existed for decades before the act, which regularised
rather than created it.

## The UK avowed its services one at a time

The British sequence is unlike any other in this batch. Rather than a single
organic act covering the intelligence community, the UK put its services on
a statutory footing **separately and five years apart**:

| Year | Act | Service |
|---|---|---|
| 1989 | [[GB-SSA-1989]] | MI5 |
| 1994 | [[GB-ISA-1994]] | [[GB-SIS]] and [[GB-GCHQ]] |

Compare the single-act countries ([[NL-WIV-2017]], [[BE-WIV-1998]]) and the
one-act-per-service country (Germany). The UK is a third pattern: acts of
avowal, added as each service was publicly acknowledged.

Cutting across both is [[GB-IPA-2016]], which governs the *powers* rather
than the bodies — structurally the same choice France made with
[[FR-LOI-RENSEIGNEMENT-2015]], arrived at from the opposite direction.

## Warrants issued by the Secretary of State

The 1989 act's mechanism, as the sources describe it, is ministerial:
certain actions may be taken on the authority of **warrants issued by the
Secretary of State**. The UK's independent check came much later, with the
[[GB-IPCO]] under the 2016 act — where the Netherlands built [[NL-TIB]] into
the same statute as the services.

## The UK includes its services in its data protection act

Every other country in this batch keeps intelligence outside the ordinary
data protection regime, on the strength of Article 4(2) TEU and
[[EU-GDPR]] Article 2(2)(a). The UK does something different, and it is the
most interesting single fact this batch turned up.

**Part 4 of [[GB-DPA-2018]] is a data protection regime built specifically
for the intelligence services** — MI5, [[GB-SIS]] and [[GB-GCHQ]] — sitting
separately from [[GB-UK-GDPR]]. All personal data processing these three
undertake is governed by it, as is processing by anyone acting on their
behalf. Its six data protection principles are the GDPR's, with one wording
change in the sixth.

So the UK's intelligence services sit **inside** the national data
protection act, and [[GB-ICO]] — already an Atlas entity — is the regulator
of the legislation containing them.

That is what gives the UK cluster its bridge into the Atlas's existing
legislation layer. Belgium reaches a similar result by a different route:
[[BE-GDPR-WET]] carries a dedicated subtitle for processing by the
intelligence and security services, though there the verification work is
referred to [[BE-COMITE-I]] rather than kept with the data protection
authority.

Neither is a counter-example to [[DOMAIN-NATIONAL-SECURITY]]. The EU-law
carve-out says the *Union* does not regulate here; it does not stop a member
state — or a former one — from regulating in its own right, and these two
did.

## No ministry edge

MI5 answers to the Home Secretary. The Home Office is not an Atlas entity,
so no `part-of` is asserted — as for [[FR-DGSI]], [[NL-MIVD]] and
[[DE-BND]].

## Not modelled

- The **Regulation of Investigatory Powers Act 2000 (RIPA)**, substantially
  superseded by [[GB-IPA-2016]] but not wholly repealed.
- The **Investigatory Powers Tribunal**, the judicial body hearing
  complaints, distinct from [[GB-IPCO]].
- The **Investigatory Powers (Amendment) Act 2024**.
- **Defence Intelligence**, the UK's military intelligence organisation,
  which has no equivalent avowal act and was not researched. The UK therefore
  appears here with three services where France has four and Poland four.

## Relationships

- `governed-by` [[GB-SSA-1989]], [[GB-IPA-2016]] and [[GB-DPA-2018]].

## Sources

Listed in frontmatter.
