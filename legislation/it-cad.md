---
id: IT-CAD
type: law
name: Codice dell'Amministrazione Digitale
alternative_names:
  - CAD
  - Decreto Legislativo 7 marzo 2005, n. 82
  - D.Lgs. 82/2005
  - Digital Administration Code
description: >
  Italian legislative decree 82/2005, in force since 1 January 2006,
  unifying, reorganising and integrating the existing rules on the
  digitalisation and simplification of public administration into a single
  source. It establishes citizens' digital rights, including the right to
  access the online services of public administrations through a digital
  identity, and creates SPID at Article 64. It has been reformed
  repeatedly, most recently by the Decreto Semplificazioni, converted with
  amendments by Law 120 of 11 September 2020.

level: national
country: IT
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2005-03-07
end_date: null
last_verified: "2026-08-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IT
  - IT-AGID
  - IT-SPID
relationships:
  - type: applies-in
    target: IT
    source: fact
    evidence: "Confirmed by reading bosettiegatti.eu's text of Decreto Legislativo 7 marzo 2005, n. 82 directly (2026-08-25): the decree's own Article 64 establishes SPID verbatim — 'è istituito, a cura dell'Agenzia per l'Italia digitale, il sistema pubblico per la gestione dell'identità digitale' (the public system for managing digital identity — SPID — is established, under the responsibility of the Agency for Digital Italy) — and its text carries repeated amendment markers citing 'legge n. 120 del 2020' (Law 120/2020), confirming the CAD is a live, amended-in-place code rather than a static original text. The specific promulgation day (11 September 2020) and the colloquial name 'Decreto Semplificazioni' are carried from this entity's original sourcing and were not independently reconfirmed by any page read this pass. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Decreto legislativo 7 marzo 2005, n. 82 - Codice dell'amministrazione digitale"
    url: "https://www.bosettiegatti.eu/info/norme/statali/2005_0082.htm"
    publisher: "Bosetti & Gatti"
    accessed: "2026-08-25"
  - title: "Guida ai diritti di cittadinanza digitale"
    url: "https://www.agid.gov.it/sites/default/files/repository_files/guida_riepilogo_diritti_cittadinanza_digitale_03-2022.pdf"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
    accessed: "2026-08-25"
---

# Codice dell'Amministrazione Digitale

> **Verified 2026-08-25.** Both cited pages were read directly. The
> decree's own Article 64 text confirms it establishes SPID "a cura
> dell'Agenzia per l'Italia digitale" (under the responsibility of
> AgID), and AgID's own "Guida ai diritti di cittadinanza digitale"
> confirms the citizens'-rights framing verbatim. `bosettiegatti.eu`
> blocks this project's honest, identifying User-Agent (a custom IIS
> "999" bot-defense response) but serves the page normally to a
> browser-spoofing one — the mirror image of the `efta.int` finding
> earlier this session, where the honest UA was the one that worked.

## Description

Italy's digital administration law - and the reason Italy sat first on
the expansion shortlist.

## A codified act, which no other Atlas country has

Every other national digital-government instrument the Atlas holds is a
single act addressing a single subject: [[DE-OZG]] on online access,
[[NL-WDO]] on digital government, [[FR-LRN]] on open data by default.

The CAD is a **code**. Italian practice consolidates a whole field into
one numbered instrument that is then amended in place - so digital
identity, electronic documents, digital signatures, public registers and
citizens' digital rights all live at one citation, and the 2020 Decreto
Semplificazioni changed that text rather than sitting beside it.

That is a legislative **form**, not merely a longer act, and the Atlas's
`type: law` flattens it exactly as it flattens the primary/secondary
distinction on [[IE-PSI-REGULATIONS-2021]]. Only this paragraph records
the difference.

## Relationships

- `applies-in` [[IT]] (anchor edge).
- [[IT-AGID]] is `governed-by` this Code; [[IT-SPID]] is created by its
  Article 64.

## ⚠ A blocked host that blocks the honest User-Agent, not the deceptive one

Every other genuinely-blocked host this session found (`iso.org`,
`coe.int`, `consilium.europa.eu`) blocks equally regardless of
User-Agent, and every fixable one (`efta.int`) blocked the
browser-spoofing UA while serving the honest one. `bosettiegatti.eu` is
the first host found doing the reverse: it returns a custom IIS "999"
error to `tools/reverify.py`'s own honest, identifying User-Agent, and
a normal `200` to a browser-spoofing one. The law text itself was read
and confirmed this pass — via the browser-spoofing fetch — but
`tools/reverify.py`, which only sends the honest UA, will report this
source UNREACHABLE on any future automated run against this exact
host.

## Sources

Listed in frontmatter, both read directly this pass.
