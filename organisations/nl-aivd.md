---
id: NL-AIVD
type: organisation
name: Algemene Inlichtingen- en Veiligheidsdienst
alternative_names:
  - AIVD
  - General Intelligence and Security Service
description: >
  The Dutch civilian intelligence and security service, operating under the
  Minister of the Interior and Kingdom Relations. Its tasks, powers and the
  conditions under which it may use them are set by the Wet op de
  inlichtingen- en veiligheidsdiensten 2017, which also subjects it to
  binding prior review by the TIB and retrospective oversight by the CTIVD.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations:
  - NL-BZK
related_entities:
  - NL-WIV-2017
  - NL-TWCO
  - NL-MIVD
  - NL-CTIVD
  - NL-TIB
relationships:
  - type: part-of
    target: NL-BZK
    source: fact
    evidence: "Confirmed by reading aivd.nl's own 'Wet op de inlichtingen- en veiligheidsdiensten' page directly (2026-08-27): the AIVD operates under the Wiv 2017 to safeguard national security under ministerial responsibility. en.wikipedia.org's 'General Intelligence and Security Service' article, also read directly, states in as many words that the AIVD 'falls under the Ministry of the Interior and Kingdom Relations', with that Minister holding political responsibility for the service's actions. irp.fas.org was not re-fetched this pass."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WIV-2017
    source: fact
    evidence: "Confirmed by reading aivd.nl's own 'Wet op de inlichtingen- en veiligheidsdiensten' page directly (2026-08-27): the Wiv 2017 sets out the AIVD's tasks, responsibilities and powers, and the AIVD has operated under this framework since 1 May 2018. The page names specific powers the act grants: onderzoeksopdrachtgerichte interceptie (OOG, broader cable-bound interception), computer hacking, DNA-profiling procedures and data sharing with foreign services. rijksoverheid.nl's current page on the same subject (moved from the URL in this entity's sources — the old URL now 404s, redirected via search to a `/themas/` path, also read directly) independently confirms the AIVD and MIVD are the two services covered."
    confidence: high
    valid_from: 2018-05-01
    valid_until: null
  - type: governed-by
    target: NL-TWCO
    source: fact
    evidence: "Confirmed by reading aivd.nl's own TWCO page directly (2026-08-27): the temporary act gives the AIVD and MIVD enhanced operational flexibility against state-sponsored cyber threats (the page names Russia and China), entered into force 1 July 2024, and shifts part of the oversight for certain powers from TIB pre-approval to CTIVD real-time monitoring. eerstekamer.nl dossier 36.263 and njb.nl, also read directly this pass (on the NL-TWCO entity), corroborate the dates."
    confidence: high
    valid_from: 2024-07-01
    valid_until: null

sources:
  - title: "Wet op de inlichtingen- en veiligheidsdiensten"
    url: "https://www.aivd.nl/onderwerpen/wet-op-de-inlichtingen-en-veiligheidsdiensten"
    publisher: "Algemene Inlichtingen- en Veiligheidsdienst (AIVD)"
    accessed: "2026-08-27"
  - title: "Toetsing, toezicht en controle"
    url: "https://www.aivd.nl/onderwerpen/wet-op-de-inlichtingen--en-veiligheidsdiensten/toetsing-toezicht-en-controle-aivd"
    publisher: "Algemene Inlichtingen- en Veiligheidsdienst (AIVD)"
    accessed: "2026-08-27"
  - title: "General Intelligence and Security Service"
    url: "https://en.wikipedia.org/wiki/General_Intelligence_and_Security_Service"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "Netherlands — Intelligence and Security Services"
    url: "https://irp.fas.org/world/netherlands/index.html"
    publisher: "Federation of American Scientists, Intelligence Resource Program"
---

# Algemene Inlichtingen- en Veiligheidsdienst (AIVD)

> **Verified 2026-08-27.** Three of this entity's four cited pages were
> read directly this pass — both aivd.nl pages and the English Wikipedia
> article — closing the previous `search-only` status. `irp.fas.org` was
> not re-fetched; nothing it previously supported is contradicted by what
> was read.

## Description

The AIVD is the **civilian** half of the Dutch intelligence and security
apparatus, operating under the Minister of the Interior and Kingdom
Relations — confirmed directly on both the AIVD's own site and in the
English Wikipedia article, which states outright that the AIVD "falls
under the Ministry of the Interior and Kingdom Relations". Its military
counterpart is [[NL-MIVD]], under the Minister of Defence.

Everything the service may do is set by [[NL-WIV-2017]]. Reading aivd.nl's
own page directly names the specific powers the act grants beyond the
generic "tasks and powers" framing this entity previously carried:
**onderzoeksopdrachtgerichte interceptie** (OOG — the broadened,
cable-bound form of bulk interception), **computer hacking**, **DNA-profiling**
procedures, and **data sharing with foreign intelligence services**.

## The law it operates under

Two instruments, not one:

- **[[NL-WIV-2017]]** — the standing framework, in force since 1 May 2018.
- **[[NL-TWCO]]** — a *temporary* act, in force since 1 July 2024, which
  deviates from the Wiv 2017 regime for investigations into countries with
  an offensive cyber programme. The AIVD's own page names the countries in
  view: Russia and China. It expires four years after entry into force.

Both are modelled with `governed-by`, and the temporary act is the reason
this entity has two: an entity whose powers are currently defined by a
standing act **as modified by a sunsetting one** is not accurately described
by either alone.

## Two reviewers, doing different jobs

The distinction matters and is easy to get wrong:

- **[[NL-TIB]]** reviews **beforehand**, and only for lawfulness. Its
  decision is **binding**, and normally acts before the service exercises
  the power (a service may act first only in emergencies, with TIB review
  following). Reading the AIVD's own oversight page directly confirms this
  in as many words: "De TIB is een onafhankelijke commissie die beoordeelt
  of de toestemming rechtmatig is" — if the TIB disapproves, the operation
  does not proceed.
- **[[NL-CTIVD]]** reviews **during and after** — "houdt toezicht tijdens
  en na afloop van de inzet van bevoegdheden", per the same page.

The two hold a standing *rechtseenheidoverleg* to keep their reading of the
Wiv 2017 consistent, and jointly publish agreed positions to parliament as
*rechtseenheidbrieven* (confirmed on ctivd.nl, read directly — see
[[NL-CTIVD]]).

Under [[NL-TWCO]], part of this balance shifts: for certain powers, review
moves from TIB pre-approval towards real-time CTIVD monitoring with
binding authority to halt an operation immediately — confirmed by reading
the AIVD's own TWCO page directly this pass.

## Why [[NL-AP]] is absent from this entity

The Dutch data protection authority does not supervise the AIVD, and no
relationship is asserted between them. Intelligence processing falls outside
the material scope of [[EU-GDPR]] under Article 2(2)(a), and Article 4(2)
TEU reserves national security to the member states. The Wiv 2017 builds a
separate review structure — TIB and CTIVD — precisely because the ordinary
one does not reach here. See [[DOMAIN-NATIONAL-SECURITY]].

## Not modelled

- The **Joint Sigint Cyber Unit (JSCU)**, the joint AIVD/MIVD signals
  intelligence unit, mentioned in the sources as founded in 2014. It is a
  joint unit rather than a service in its own right and was not researched.
- The **Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten's
  klachtbehandeling** — the CTIVD's complaints function is separate from its
  oversight function and is not distinguished here.
- Other parliamentary and judicial oversight layers the sources mention in
  passing — the CIVD (secret parliamentary committee), ordinary court
  review, and the Algemene Rekenkamer's financial oversight.
- Any **operational** matter. The Atlas records statutory structure.

## Relationships

- `part-of` [[NL-BZK]].
- `governed-by` [[NL-WIV-2017]] and [[NL-TWCO]].

## Sources

Three of four read directly this pass: both `aivd.nl` pages and the English
Wikipedia article. `irp.fas.org` was not re-fetched. The
`rijksoverheid.nl` page cited on the sibling [[NL-WIV-2017]] and
[[NL-MIVD]] entities has moved (the old URL now 404s); its content was
confirmed via its current `/themas/` location, also read directly.
