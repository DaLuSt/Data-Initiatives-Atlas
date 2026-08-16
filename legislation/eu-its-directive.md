---
id: EU-ITS-DIRECTIVE
type: directive
name: ITS Directive
alternative_names:
  - Directive 2010/40/EU
  - Intelligent Transport Systems Directive
description: >
  EU directive on the framework for the deployment of Intelligent Transport
  Systems in road transport. Under delegated regulations supplementing it,
  member states have established national access points (NAPs) organising
  access to and reuse of transport-related data.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - NL-NTM
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "Member States have established national access points (NAPs) under delegated regulations supplementing Directive 2010/40/EU, organising access to and reuse of transport-related data (transport.ec.europa.eu National Access Points; EUR-Lex CELEX 32010L0040). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "The Mobilithek is Germany's National Access Point for mobility data, having replaced the Mobility Data Marketplace in that role, and implements requirements from the delegated regulations on the European ITS Directive (bmv.de 'Mobilithek'; forschungsinformationssystem.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "Member States have established national access points (NAPs) under the delegated regulations supplementing Directive 2010/40/EU (transport.ec.europa.eu National Access Points; EUR-Lex CELEX 32010L0040). NOT READ — search-only. No Belgian national access point is recorded in this Atlas."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: FR
    source: fact
    evidence: "Member States have established national access points under the delegated regulations supplementing Directive 2010/40/EU (transport.ec.europa.eu National Access Points). NOT READ — search-only. No French national access point is recorded in this Atlas."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: ES
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, Spain included. NOT READ - search-only. No Spanish transposing instrument was identified in this batch and none is asserted."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: PL
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, Poland included. NOT READ - search-only. No Polish transposing instrument was identified in this batch and none is asserted."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Directive 2010/40/EU"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32010L0040"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "National Access Points — Mobility and Transport"
    url: "https://transport.ec.europa.eu/transport-themes/smart-mobility/road/its-directive-and-action-plan/national-access-points_en"
    publisher: "European Commission — Mobility and Transport"
  - title: "Commission Delegated Regulation (EU) 2017/1926 — consolidated text"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02017R1926-20240304"
    publisher: "EUR-Lex (Publications Office of the European Union)"
---

# ITS Directive (Directive 2010/40/EU)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Directive 2010/40/EU sets the framework for deploying Intelligent Transport
Systems in road transport, including specifications ensuring that EU-wide
multimodal travel information services are accurate and available across
borders.

Its significance for the Atlas is the **national access point** mechanism:
under delegated regulations supplementing the directive, member states have
established NAPs that organise access to and reuse of transport-related
data, supporting EU-wide interoperable travel and traffic services.
Commission Delegated Regulation (EU) 2017/1926 specifies which data types
must be made accessible via a member state's national access point in a
standardised format.

## What this entity closes

Batch 5 created [[NL-NTM]], the Dutch national access point, and recorded
that it exists because "every European country is obliged to have one" — but
**refused to assert an `implements-requirement-from` relationship because no
source located named the instrument imposing the obligation.**

Batch 8 found it. The relationship is now recorded on [[NL-NTM]], completing
another EU→national chain:

```
EU-ITS-DIRECTIVE ──(delegated regulations)──→ NL-NTM ──part-of──→ NL-NDW
```

This is a small illustration of the discipline paying off: the honest gap
left in Batch 5 was closable three batches later with a real citation,
whereas a plausible guess would have needed correcting instead.

`coverage: low`: the directive's priority areas and its wider delegated-act
family were not researched, and the delegated regulation is cited as a
source rather than modelled as its own entity.

## Relationships

- Applies in [[NL]], [[DE]], [[BE]], [[FR]], [[ES]] and [[PL]] — one entity, six
  countries. Every other member state belongs here too; the
  `applies-in` relationships are added as countries join the Atlas.
- Underpins [[NL-NTM]] (relationship recorded on that entity).

## Sources

Listed in frontmatter.
