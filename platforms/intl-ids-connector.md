---
id: INTL-IDS-CONNECTOR
type: technology
name: IDS Connector
alternative_names:
  - Dataspace Connector (DSC)
  - Eclipse Dataspace Connector
description: >
  Software gateway component installed at a participating organisation to
  provide technical access to the International Data Spaces ecosystem,
  implementing the roles and interactions of the IDS Reference Architecture
  Model. It registers offered data resources and their metadata, attaches
  usage rules on the provider's side, and negotiates usage contracts on the
  consumer's side, communicating over the IDSA Dataspace Protocol. Its
  security-gateway requirements were standardised as DIN SPEC 27070 in
  three profiles — Base, Trust and Trust+. The best-known implementation,
  the Dataspace Connector, was developed by Fraunhofer ISST, achieved
  "IDS-ready" Base-level certification, and is now maintained as open
  source under the Eclipse Dataspace Components initiative.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains: []
organisations:
  - INTL-IDSA
related_entities:
  - INTL-IDSA
  - INTL-IDS-RAM
  - DE-DIN
  - DE-CATENA-X
relationships:
  - type: implements-requirement-from
    target: INTL-IDS-RAM
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #128. Confirmed by reading internationaldataspaces.org's own DIN SPEC 27070 announcement page directly (already cited on [[INTL-IDS-RAM]]): the IDS Connector is the security gateway the DIN SPEC specifies, defining Base, Trust and Trust+ profiles addressing the IDS-RAM's security, certification and governance perspectives. Fraunhofer ISST's own Dataspace Connector page, read directly (2026-09-19), states the connector framework and its components 'adhere to the specifications outlined in the Reference Architecture Model (RAM) and the International Data Spaces certification criteria derived from it.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: INTL-IDSA
    source: fact
    evidence: "Confirmed by reading internationaldataspaces.org's own 'IDS-ready' announcement page directly (2026-09-19): the Dataspace Connector achieved 'IDS-ready' certification at the Base level, with the IDSA's CTO quoted stating it 'fulfills the security requirements and all functionalities required by the International Data Spaces (IDS) for trustworthy data sharing' — the IDSA certifying and governing conformance, though Fraunhofer ISST developed the specific implementation (see description)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "IDS is Officially a Standard: DIN SPEC 27070 is Published"
    url: "https://internationaldataspaces.org/ids-is-officially-a-standard-din-spec-27070-is-published/"
    publisher: "International Data Spaces Association (IDSA)"
    accessed: "2026-08-28"
  - title: "IDS-ready: Open-Source-Software \"Dataspace Connector\" Enables Sovereign Data Exchange"
    url: "https://internationaldataspaces.org/ids-ready-open-source-software-dataspace-connector-enables-sovereign-data-exchange/"
    publisher: "International Data Spaces Association (IDSA)"
    accessed: "2026-09-19"
  - title: "Connector: Technical access to the International Data Spaces ecosystem"
    url: "https://www.isst.fraunhofer.de/en/departments/it-service-providers/technologies/Dataspace-Connector.html"
    publisher: "Fraunhofer-Institut für Software- und Systemtechnik (ISST)"
    accessed: "2026-09-19"
---

# IDS Connector

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #128 ("the IDS Connector is not modelled"). Sourced from the IDSA's own
> DIN SPEC 27070 announcement (already cited on [[INTL-IDS-RAM]]), its own
> "IDS-ready" certification announcement, and Fraunhofer ISST's own
> Dataspace Connector page — all read directly.

## Description

The IDS Connector is the **software gateway** a participating organisation
installs to gain technical access to the International Data Spaces
ecosystem. Confirmed by reading Fraunhofer ISST's own page directly: it
registers offered data resources and metadata, attaches usage rules on the
provider's side, and negotiates usage contracts on the consumer's side,
communicating over the **IDSA Dataspace Protocol**.

## Three security profiles, standardised as a German standard

[[INTL-IDS-RAM]] already records that the connector's security-gateway
requirements were published as **DIN SPEC 27070** on 21 February 2020,
defining three profiles:

| Profile | What it adds |
|---|---|
| **Base** | Basic security for communication across company boundaries |
| **Trust** | Strict isolation of service containers, mutual integrity verification |
| **Trust+** | Protection against manipulation by malicious administrators |

This entity is the connector itself; [[INTL-IDS-RAM]] carries the
`references` edge to [[DE-DIN]] for the DIN SPEC, and is not duplicated
here.

## The best-known implementation: the Dataspace Connector

Fraunhofer ISST developed the **Dataspace Connector (DSC)**, later
transferred to the **Eclipse Dataspace Components** initiative as open
source, freely available on GitHub, requiring only a Java environment and
deployable via Docker or Kubernetes. It achieved **"IDS-ready" Base-level
certification** — confirmed by reading the IDSA's own announcement
directly, which quotes the IDSA's CTO stating it "fulfills the security
requirements and all functionalities required by the International Data
Spaces (IDS) for trustworthy data sharing." The Base level was chosen
deliberately: it does not require specialised hardware such as a Trusted
Platform Module, easing deployment. Despite the entry-level certification,
the DSC supports enforcement of eight usage-condition classes from the
IDSA framework — exceeding what Base level requires.

## Not modelled

- The Eclipse Dataspace Components project's individual modules, as
  distinct from the Dataspace Connector as a whole.
- Other IDS-certified connector implementations besides the Dataspace
  Connector — no source read this pass names or compares them.
- The IDS Certification programme itself (launched 2022) as a separate
  entity.

## Relationships

- `implements-requirement-from` [[INTL-IDS-RAM]] — `confidence: high`.
- `maintained-by` [[INTL-IDSA]] — `confidence: medium`, reflecting the
  IDSA's certification/governance role rather than day-to-day development,
  which Fraunhofer ISST and the Eclipse Dataspace Components project carry
  out.

## Sources

Listed in frontmatter, all three read directly.
