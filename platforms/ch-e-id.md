---
id: CH-E-ID
type: platform
name: Swiss e-ID and swiyu trust infrastructure
alternative_names:
  - e-ID
  - E-ID
  - swiyu
  - swiyu Wallet
  - Swiss e-ID
  - Vertrauensinfrastruktur
description: >
  Switzerland's planned state-issued electronic identity and the federal
  trust infrastructure behind it. The e-ID is a free electronic proof of
  identity that fedpol issues into the swiyu Wallet app; the Federal Office
  of Information Technology, Systems and Telecommunication develops and
  operates the infrastructure, which is designed around decentralised
  storage and is open source. It was in public beta and has not launched:
  on 30 June 2026 the federal government postponed the e-ID's introduction,
  expecting the trust infrastructure itself to become operational in the
  first half of 2027.

level: national
country: CH
region: null

status: planned
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-10-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - CH
  - CH-BGEID
  - CH-AGOV
  - CH-DVS
relationships:
  - type: part-of
    target: CH
    source: fact
    evidence: "Confirmed 2026-10-01 by reading the e-ID programme's own site (eid.admin.ch, run by the Swiss federal authorities) directly: 'The federal government operates the Trust Infrastructure required for this and issues the e-ID.' Anchor edge under metadata/relationship-types.md §2.3: it records that this is a Swiss federal infrastructure and asserts no more than that."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: CH-BGEID
    source: fact
    evidence: "Confirmed 2026-10-01 by reading the Act's own text (final-vote text, parlament.ch). Art. 1 para. 1 states that the Act regulates 'die vom Bund zur Verfügung gestellte Infrastruktur zum Ausstellen, Widerrufen, Überprüfen, Aufbewahren und Vorweisen von elektronischen Nachweisen (Vertrauensinfrastruktur)' and 'den vom Bund ausgestellten elektronischen Identitätsnachweis für natürliche Personen (E-ID)'. The Act is adopted but not yet in force, so `valid_from` is left null."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: CH-AGOV
    source: fact
    evidence: "Confirmed 2026-10-01 by reading eid.admin.ch directly. Its 'About us' page lists, among the principal authorities involved, 'Digital Public Services Switzerland (DPSS) and Federal Chancellery (FCh): Provides the authentication service of the Swiss authorities (AGOV) and coordinates with communes, cities and cantons'; its e-ID page lists 'Use the nationwide government login' among the uses expected from the e-ID's introduction; and its 25 February 2026 post says AGOV's operation and development 'are financed from other budget items'. The Act's own Annex inserts Art. 11 para. 3bis into the EMBAG, obliging the Federal Chancellery to operate an e-ID-based authentication system, without naming AGOV. `related-to` at medium: the sources place AGOV inside the e-ID programme and expect the two to be used together, but none describes the technical relationship."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The e-ID works like a digital ID card"
    url: "https://www.eid.admin.ch/en"
    publisher: "e-ID programme, Swiss federal authorities"
    accessed: "2026-10-01"
  - title: "The Electronic Identity (e-ID)"
    url: "https://www.eid.admin.ch/en/e-id-e"
    publisher: "e-ID programme, Swiss federal authorities"
    accessed: "2026-10-01"
  - title: "About us"
    url: "https://www.eid.admin.ch/en/ueber-uns-e"
    publisher: "e-ID programme, Swiss federal authorities"
    accessed: "2026-10-01"
  - title: "e-ID blog"
    url: "https://www.eid.admin.ch/en/blog-e"
    publisher: "e-ID programme, Swiss federal authorities"
    accessed: "2026-10-01"
  - title: "Strengthening acceptance of e-ID with additional measures"
    url: "https://www.eid.admin.ch/en/akzeptanz-der-e-id-mit-zusaetzlichen-massnahmen-staerken-e"
    publisher: "e-ID programme, Swiss federal authorities"
    accessed: "2026-10-01"
  - title: "New Timeline for the Introduction of the e-ID and the Trust Infrastructure"
    url: "https://www.eid.admin.ch/en/20260625-neuer-zeitplan-fuer-die-einfuehrung-der-e-id-und-der-vertrauensinfrastruktur-en"
    publisher: "e-ID programme, Swiss federal authorities"
    accessed: "2026-10-01"
  - title: "Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (E-ID-Gesetz, BGEID) — Vorlage der Redaktionskommission für die Schlussabstimmung"
    url: "https://www.parlament.ch/centers/eparl/curia/2023/20230073/Schlussabstimmungstext%201%20NS%20D.pdf"
    publisher: "Das Schweizer Parlament"
    accessed: "2026-10-01"
---

# Swiss e-ID and swiyu trust infrastructure

> **Created 2026-10-01**, closing a gap `countries/ch/index.md` flagged:
> "The Swiss e-ID, legislated for and not yet an Atlas entity." Its
> statutory basis is [[CH-BGEID]]. Both were read directly: the federal
> e-ID programme's own site and the Act's text.

## Description

The programme describes the e-ID as "an official means of identification
issued by the state", a "free and optional complementary offer to the
physical identity card". To order one, a person needs a valid Swiss ID
card or foreigner's ID card; it is shown with the **swiyu Wallet** app by
scanning a QR code, and the holder sees which data a verifier requests and
approves or declines. The state operates the trust infrastructure so that
other authorities and organisations can issue their own electronic
credentials as well, and the programme names the electronic driving
licence, a learner-driver permit, residence certificates and customer or
membership cards as examples.

Who does what, per the programme's "About us" page and the Act:

| Body | Role |
|---|---|
| Federal Office of Justice (FOJ) | Responsible for the legislation; commissions the trust infrastructure |
| Federal Office of Information Technology, Systems and Telecommunication (FOITT / BIT) | Develops and operates the trust infrastructure and the mobile app |
| Federal Office of Police (fedpol) | Issues the e-ID |
| Federal Roads Office (FEDRO) and the road traffic offices' association (asa) | Issue electronic credentials in road transport |
| Digital Public Services Switzerland (DPSS, which is [[CH-DVS]]) and the Federal Chancellery | Provide the authorities' authentication service, [[CH-AGOV]], and coordinate with communes, cities and cantons |

Of these bodies only DPSS is an Atlas entity, as [[CH-DVS]]: that entity
lists "Digital Public Services Switzerland" as an alternative name and
cites a DPSS homepage as its source. The programme says more than 120
people from various disciplines work on the development.

The programme states the design properties as: **decentralised storage**
(the e-ID is bound to the smartphone and cannot be copied; a lost or
changed phone means applying for a new e-ID), **consent** (the holder
checks a verifier's trustworthiness and requested data first), **data
minimisation** (for example, only proof that a minimum age is met) and
**unlinkability** (technical data cannot be used to link a person's
behaviour). These are the programme's claims about the design; the Atlas
has not assessed them.

## Status: planned, and recently postponed

This is why the entity is `status: planned` with `start_date: null`.

- **Public beta**: the programme ran a public beta (its blog records
  that the public could try the e-ID "free of charge" from 26 March 2025),
  and published its source code. In September 2026 the beta became a
  **sandbox**: the swiyu Wallet will in future work only with the
  production infrastructure, and a separate "swiyu Sandbox Wallet" is
  available for testing.
- **Planned go-live**: on 25 February 2026 the programme said the e-ID
  was "expected to go live on December 1, 2026".
- **Postponement**: on 30 June 2026 the introduction was postponed and no
  new date was given: "The exact date for the introduction of the e-ID
  will be announced as soon as this work is largely complete." The trust
  infrastructure is expected to become operational in the first half of
  2027 regardless, with the Federal Council then bringing [[CH-BGEID]]
  into force "at least in part".
- **Cost cuts**: Parliament cut CHF 1.7 million from the 2026 budget. The
  programme says that, for cost reasons, planned further developments
  "must currently be abandoned": "the connection to international e-ID
  systems", the federal government's back-up service and issuing e-IDs in
  third-party wallets. It also warns that the federal government may lack
  the funds to develop further digital credentials beyond the e-ID. The
  trust infrastructure is operated by the FOITT at two independent
  federal sites (PRIMUS in Bern and CAMPUS in Frauenfeld).
- **Audit**: on 18 February 2026 the Swiss Federal Audit Office audited the
  programme for the second time, covering e-ID issuance, the trust
  infrastructure and the technical design of IT security. The post read
  does not summarise the findings, and none is asserted.

The programme lists uses expected from the e-ID's introduction onwards:
proving age, opening a bank account, electronic signatures, registering in
the organ and tissue donation register, subscribing to a mobile plan,
using the nationwide government login, ordering a criminal-record extract
and founding a company. They are expectations, not live services.

## The AGOV link

[[CH-AGOV]] is the government login the Federal Chancellery and Digital
Public Services Switzerland run. The programme names it as the
authentication service within the e-ID programme, expects the e-ID to be
usable with the government login, and says AGOV is funded separately. The
Act's annex requires the Federal Chancellery to operate an e-ID-based
authentication system (EMBAG Art. 11 para. 3bis) without naming AGOV. The
edge is therefore `related-to` at `confidence: medium`, not a claim that
AGOV *is* that system.

## Not modelled

- Any **connection to the EU's identity framework**. No source read links
  the Swiss e-ID to [[EU-EIDAS2]] or the EU Digital Identity Wallet, and the
  programme says the connection to international e-ID systems is currently
  abandoned.
- The **FOJ, fedpol, FOITT and FEDRO** as entities.
- The **swiyu technical standards** and any open-source repositories; the
  programme's "Technology" page was not read in detail.
- The **ordinance** implementing the Act.

## Relationships

- `part-of` [[CH]] — anchor edge.
- `governed-by` [[CH-BGEID]] — the Act regulating the trust
  infrastructure and the e-ID.
- `related-to` [[CH-AGOV]] — the programme names AGOV as its
  authentication service; see above.

## Sources

Listed in frontmatter. Every cited page was read directly on 2026-10-01.
The programme's site is run by the Swiss federal authorities, so it is a
primary source for the programme's own plans, dates and design claims,
though not independent of the programme.
