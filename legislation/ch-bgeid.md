---
id: CH-BGEID
type: act
name: "Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise"
name_en: "E-ID Act"
alternative_names:
  - E-ID-Gesetz
  - BGEID
  - E-ID Act
  - Federal Act on Electronic Identity and Other Electronic Credentials
description: >
  Swiss federal act of 20 December 2024 creating a state-issued electronic
  identity (the e-ID) and the federal trust infrastructure for issuing,
  revoking, verifying, storing and presenting electronic credentials.
  Parliament adopted it on 20 December 2024 and voters approved it in a
  referendum on 28 September 2025 by 50.39% to 49.61%. It is not yet in
  force: the Federal Council sets the date, and on 30 June 2026 the federal
  government postponed the e-ID's introduction, expecting the trust
  infrastructure itself to become operational in the first half of 2027.

level: national
country: CH
region: null

status: adopted
rank: ordinary
confidence: high
coverage: medium
verification: primary-source

start_date: 2024-12-20
end_date: null
last_verified: "2026-10-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CH
  - CH-E-ID
  - CH-ISG
  - CH-EMBAG
  - CH-AGOV
relationships:
  - type: amends
    target: CH-ISG
    source: fact
    evidence: "Confirmed 2026-10-01 by reading the Act's own text (the final-vote text published on parlament.ch), Annex 'Änderung anderer Erlasse', item 1: it amends the Informationssicherheitsgesetz of 18 December 2020 (in the version of the amendment of 29 September 2023) by adding, at Art. 74b para. 1 letter v, 'Ausstellerinnen und Verifikatorinnen von elektronischen Nachweisen im Sinn des E-ID-Gesetzes' to the entities subject to the duty to report cyber attacks. The ISG continues to exist under its own name."
    confidence: high
    valid_from: null
    valid_until: null
  - type: amends
    target: CH-EMBAG
    source: fact
    evidence: "Confirmed 2026-10-01 by reading the Act's own text, Annex item 8: it amends the Bundesgesetz vom 17. März 2023 über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (SR 172.019) by inserting Art. 11 para. 3bis: 'Als IKT-Mittel im Sinne der Absätze 1–3 betreibt die Bundeskanzlei ein System, das auf der Grundlage der E-ID nach dem E-ID-Gesetz vom 20. Dezember 2024 die Authentifizierung natürlicher Personen ermöglicht.' (As an ICT means the Federal Chancellery operates a system that, on the basis of the e-ID, enables the authentication of natural persons.) The EMBAG continues to exist under its own name."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (E-ID-Gesetz, BGEID) — Vorlage der Redaktionskommission für die Schlussabstimmung"
    url: "https://www.parlament.ch/centers/eparl/curia/2023/20230073/Schlussabstimmungstext%201%20NS%20D.pdf"
    publisher: "Das Schweizer Parlament"
    accessed: "2026-10-01"
    note: "The text put to the final vote of 20 December 2024 (e-parl, 19.12.2024). It is not the Federal Gazette publication, and no SR number exists yet: the footnotes cite the Act as 'SR ...'."
  - title: "e-ID blog — legislative timeline and news"
    url: "https://www.eid.admin.ch/en/blog-e"
    publisher: "e-ID programme, Swiss federal authorities"
    accessed: "2026-10-01"
  - title: "e-ID law approved at the ballot box"
    url: "https://www.eid.admin.ch/en/e-id-gesetz-an-der-urne-angenommen-e"
    publisher: "e-ID programme, Swiss federal authorities"
    accessed: "2026-10-01"
  - title: "e-ID Act published in the Federal Gazette"
    url: "https://www.eid.admin.ch/en/e-id-gesetz-im-bundesblatt-publiziert-e"
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
---

# E-ID-Gesetz (BGEID)

> **Created 2026-10-01**, closing a gap `countries/ch/index.md` itself
> flagged: "The Swiss e-ID, legislated for and not yet an Atlas entity."
> Sourced from the Act's own text on parlament.ch and from the federal
> e-ID programme's official site, both read directly.

## Description

The BGEID creates two things. The first is the **trust infrastructure**
("Vertrauensinfrastruktur"): infrastructure the Confederation provides
for issuing, revoking, verifying, storing and presenting electronic
credentials (Art. 1 para. 1 letter a). The second is the **e-ID**, the
electronic proof of identity for natural persons that the Confederation
issues, together with other electronic credentials (letter c). Its stated
purpose is to ensure that the technical and organisational measures
match the risk to personality and fundamental rights, through principles
including privacy by design and by default, data security, data
minimisation, **decentralised data storage**, traceability and
reusability (Art. 1 para. 2).

It rests on Articles 38(1), 81 and 121(1) of the Federal Constitution
(SR 101) and on the Federal Council's dispatch of **22 November 2023**
(BBl 2023 2842), both cited in the Act's own preamble.

## What the text says

Read directly from the final-vote text:

- **Who issues the e-ID**: the Federal Office of Police, **fedpol**, "mittels
  der Vertrauensinfrastruktur" (Art. 13, Art. 18). Eligibility requires a
  valid Swiss identity document, a foreign-national ID or a host-state
  legitimation card, or having applied for one (Art. 14).
- **Who runs the infrastructure**: the Federal Office of Information
  Technology, Systems and Telecommunication, the **BIT** (FOITT), provides
  the public base register (Art. 2), the trust register (Art. 3) and the
  application for storing and presenting credentials (Art. 8).
- **Source code**: the BIT must disclose the infrastructure's source code,
  withholding it only where third-party rights or security reasons rule
  disclosure out, must publish coordinated-disclosure guidelines, and must
  have the infrastructure's security reviewed regularly by suitable third
  parties (Art. 12).
- **Acceptance**: every authority or other body performing public tasks
  must accept the e-ID where it identifies a person in enforcing federal
  law (Art. 24), but whoever accepts the e-ID must **also accept an
  ordinary identity document** when the holder appears in person (Art. 25).
- **Fees**: the person applying for an e-ID pays nothing for issuing or
  revoking it; municipal and cantonal authorities pay no fees; issuers and
  verifiers pay the BIT for their register entries (Art. 31).
- **International treaties**: the Federal Council may conclude treaties on
  its own to ease the use and foreign recognition of the Swiss e-ID and the
  recognition of foreign e-IDs in Switzerland (Art. 32). **No such treaty
  is asserted here**; see "Not modelled".
- **Entry into force**: the Act is subject to the optional referendum and
  "der Bundesrat bestimmt das Inkrafttreten" (Art. 36).

**Voluntariness is not in the Act's text.** The programme's official site
says using the e-ID is "voluntary and free of charge", and Art. 25 means
holders can still show a physical document in person, but the word
"freiwillig" does not appear in the text read. It is recorded here as the
programme's statement, not as a statutory provision.

## Legislative history, each date from the programme's own record

| Date | Step |
|---|---|
| 22 Nov 2023 | Federal Council adopts the dispatch (also the Act's own preamble) |
| 14 Mar 2024 | National Council adopts the draft, 175 to 14, 1 abstention |
| 10 Sep 2024 | Council of States adopts it, 43 to 1, no abstention |
| 11 Dec 2024 | Council of States resolves the final differences |
| 20 Dec 2024 | Final votes in both chambers — **the Act's date** |
| 9 Jan 2025 | Published in the Federal Gazette; the referendum period runs to 19 April, in practice 22 April 2025 |
| 7 May 2025 | The referendum request succeeds |
| 21 May 2025 | The Federal Council sets the vote for 28 September 2025 |
| 28 Sep 2025 | **Approved: 50.39% yes, 49.61% no, turnout 49.55%** |

This is the second attempt at a Swiss e-ID; the programme's site refers to
"a second attempt at introducing an e-ID" without the Atlas having read
the first attempt's history, so the earlier law is not modelled.

## Adopted, not in force

`status: adopted` and `start_date: 2024-12-20` follow the precedent of
[[INTL-CONVENTION-108-PLUS]]: the date is the adoption date, not entry into
force, which Art. 36 leaves to the Federal Council. **No `applies-in`
edge to [[CH]] is asserted**, because applicability starts only when the Act
enters into force. The Swiss link is carried by `country: CH` and a
`related_entities` association only; the entity is connected into the graph
through its two `amends` edges and the inbound `governed-by` from
[[CH-E-ID]].

The programme's own record of how the date has moved:

- **25 Feb 2026**: the Federal Council was informed of adjustments
  strengthening data protection after the close vote (for example, only
  legally authorised providers may retrieve AHV numbers, and providers must
  register their data requests and purposes in a public federal register).
  The e-ID was then "expected to go live on December 1, 2026".
- **30 Jun 2026**: introduction **postponed**. The programme cites
  "the latest developments in artificial intelligence" as creating
  additional challenges, and says the Federal Office of Justice decided to
  strengthen security in the online issuing process, for example against
  malware on end-user devices and to improve deepfake detection. It says "the exact
  date for the introduction of the e-ID will be announced as soon as this
  work is largely complete." The trust infrastructure is expected to
  become operational in the **first half of 2027**, and the Federal
  Council will then bring the Act into force "at least in part" from that
  date, so that other credentials such as the electronic driving licence
  can be issued.
- **15 Sep 2026**: the Federal Office of Justice published a WTO tender
  for a launch communication campaign "from 2027 onwards".

## Not modelled

- The **Federal Office of Justice**, **fedpol**, the **BIT** and the
  **Federal Chancellery** as entities. The Act names fedpol and the BIT as
  the issuer and operator, and the programme names the FOJ as responsible
  for the legislation; none is an Atlas entity, matching the convention of
  not modelling federal offices without a dedicated digital-government
  role.
- The Act's **other amendments** (Annex items 2 to 7: the foreign-nationals
  and asylum information system, the Identity Documents Act, the Civil
  Code, the Debt Enforcement and Bankruptcy Act, the Electronic Patient
  Record Act and the Electronic Signature Act). Only the two amended
  instruments that are Atlas entities carry an `amends` edge.
- Any **treaty or connection to the EU's identity framework**. Art. 32
  allows treaties, but none is read, and the programme says that, for
  cost reasons, "the connection to international e-ID systems" and
  issuing e-IDs in third-party wallets "must currently be abandoned".
  Nothing connects this Act to [[EU-EIDAS2]] in any source read, so no
  relationship is asserted.
- The **Federal Gazette citation**. A search result gave "FF 2025 20" but
  it was not confirmed on a page read; the programme's site confirms only
  the publication date, 9 January 2025.
- The **ordinance** the Federal Council consulted on from 20 June to
  15 October 2025, and the **first, rejected** e-ID law.

## Relationships

- `amends` [[CH-ISG]] — adds issuers and verifiers of electronic
  credentials to the cyber-attack reporting duty.
- `amends` [[CH-EMBAG]] — obliges the Federal Chancellery to operate an
  e-ID-based authentication system. This is the Act's link to [[CH-AGOV]];
  see that entity.

[[CH-E-ID]] carries the `governed-by` edge pointing here.

## Sources

Listed in frontmatter. The Act's text is the final-vote draft from
parlament.ch, read directly. The dates, the referendum result and the
postponement come from the e-ID programme's own site, run by the federal
authorities, also read directly.
