---
id: INTL-IDS-RAM
type: standard
name: IDS Reference Architecture Model
alternative_names:
  - IDS-RAM
  - International Data Spaces Reference Architecture Model
description: >
  Reference architecture model constituting the conceptual basis of
  IDS-compliant data exchange between organisations. It establishes
  standardised roles and interactions through a five-layer structure —
  business, functional, process, information and system — addressed from the
  perspectives of security, certification and governance. Its security
  gateway requirements were published as a German standard, DIN SPEC 27070,
  on 21 February 2020.

level: international
country: null
region: null

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
organisations:
  - INTL-IDSA
related_entities:
  - INTL-IDSA
  - DE-DIN
  - DE-CATENA-X
  - NL-ISHARE
relationships:
  - type: maintained-by
    target: INTL-IDSA
    source: fact
    evidence: "Confirmed by reading internationaldataspaces.org's own 'IDS-RAM 3.0' announcement page directly (2026-08-28), which states the version 'focuses on certification, security, and governance' and 'defines security standards plus roles and responsibilities for the data economy'; and by reading datos.gob.es directly, which confirms the IDSA (formed 2016) publishes and maintains the RAM and describes the same five-layer, three-perspective structure. The IDS-RAM 3.0 PDF itself (April 2019) was fetched but returned as unreadable binary/image content by the retrieval tool rather than extractable text — not a site block, a large-PDF text-extraction limitation — so it remains unread; the other two IDSA sources cover its content instead."
    confidence: high
    valid_from: null
    valid_until: null
  - type: references
    target: DE-DIN
    source: fact
    evidence: "Confirmed by reading internationaldataspaces.org's own announcement page directly (2026-08-28): 'DIN SPEC 27070 was published on February 21, 2020,' developed by 'the German Institute for Standardization (DIN) collaborating with Fraunhofer AISEC, SICK AG, and 13 other organizations,' specifying 'Requirements and reference architecture of a security gateway for the exchange of industry data and services,' with the IDS Connector security gateway defining Base, Trust and Trust+ profiles — Trust+ providing 'protection against manipulation by malicious administrators.' pressebox.com was not part of the frontmatter sources list and was not independently fetched this pass. `references` and not `maintained-by`: DIN published the DIN SPEC, which specifies the security gateway, not the IDS-RAM as a whole."
    confidence: high
    valid_from: 2020-02-21
    valid_until: null

sources:
  - title: "IDS Reference Architecture Model 3.0 (April 2019)"
    url: "https://internationaldataspaces.org/wp-content/uploads/IDS-Reference-Architecture-Model-3.0-2019.pdf"
    publisher: "International Data Spaces Association (IDSA)"
  - title: "IDS-RAM 3.0"
    url: "https://internationaldataspaces.org/ids-ram-3-0/"
    publisher: "International Data Spaces Association (IDSA)"
    accessed: "2026-08-28"
  - title: "IDS is Officially a Standard: DIN SPEC 27070 is Published"
    url: "https://internationaldataspaces.org/ids-is-officially-a-standard-din-spec-27070-is-published/"
    publisher: "International Data Spaces Association (IDSA)"
    accessed: "2026-08-28"
  - title: "The IDS-RAM reference architecture model and its role in data spaces"
    url: "https://datos.gob.es/en/blog/ids-ram-reference-architecture-model-and-its-role-data-spaces"
    publisher: "datos.gob.es (Gobierno de España)"
    accessed: "2026-08-28"
---

# IDS Reference Architecture Model (IDS-RAM)

> **Verified 2026-08-28.** Three of four cited pages were read directly.
> `verification` moves from `search-only` to `primary-source`. The fourth
> — the IDS-RAM 3.0 PDF itself — was fetched but came back as unreadable
> binary/metadata content rather than extractable text (an
> Illustrator/Photoshop-authored PDF whose text layer the retrieval tool
> could not parse); this is a tool limitation on that specific large PDF,
> not a site block, and is recorded rather than papered over. The two
> other internationaldataspaces.org pages plus datos.gob.es independently
> cover the same five-layer, three-perspective structure the PDF would
> have confirmed directly.

## Description

The IDS-RAM is the conceptual basis of IDS-compliant data exchange between
organisations. It defines standardised **roles and interactions** across a
**five-layer structure** — business, functional, process, information and
system — each addressed from the perspectives of **security, certification
and governance**.

## The edge that makes this entity worth having

**DIN SPEC 27070 turned part of the IDS architecture into a German
standard**, published **21 February 2020**: *"Requirements and reference
architecture of a security gateway for the exchange of industry data and
services"*. It was developed by DIN with Fraunhofer AISEC, SICK AG and
thirteen other organisations, and is sold through Beuth Verlag.

[[DE-DIN]] has been an Atlas entity since the Germany batch, where it
`participates-in` [[INTL-ISO]] and [[EU-CEN]] — a standards body that,
in the Atlas's own words, **maintained nothing the Atlas held**. This is the
first specification connecting to it from the other direction.

The edge is `references`, not `maintained-by`. DIN published a DIN SPEC that
**specifies the security gateway**; it does not maintain the IDS-RAM, which
[[INTL-IDSA]] does. Collapsing that into `maintained-by` would hand DIN
ownership of a model it standardised one component of.

## Three security profiles

The IDS Connector — the gateway the DIN SPEC specifies — supports three
levels:

| Profile | What it adds |
|---|---|
| **Base** | Basic security for communication across company boundaries |
| **Trust** | Strict isolation of service containers, mutual integrity verification |
| **Trust+** | Protection against manipulation **by malicious administrators** |

The third is worth noting: a profile whose threat model includes the
operator's own administrators is a strong statement of what "data
sovereignty" is meant to mean in this architecture.

## What now points here

- [[DE-CATENA-X]] follows the IDS-RAM.
- [[NL-ISHARE]] records the IDSA incorporating iSHARE into it.

Both edges are asserted on those entities, which is where they are most
naturally authored.

## Not modelled

- **DIN SPEC 27070** as an entity of its own. It is a DIN SPEC — a
  specification published through a fast-track procedure — rather than a full
  DIN standard, and the Atlas holds no other DIN document to sit it beside.
- The **IDS Connector** and the **Dataspace Connector** implementation.
- **Version history.** The entity describes IDS-RAM **3.0** of April 2019,
  which is the version the sources returned; version 4 exists and was not
  established.

## Sources

Listed in frontmatter, three of four read directly this pass; the IDS-RAM
3.0 PDF was fetched but not machine-readable (see verification note above).
