# Research Queue

Confirmed-relevant areas that are known to need research but haven't been
worked yet, beyond the batch plan itself (`progress/backlog.md`). Use this
for gaps discovered mid-batch that fall outside the current batch's scope,
so they aren't lost.

**See also `discovery/reverification-allowlist.md`** — the generated list of
every host the Atlas cites, which is the worklist for the re-verification
pass and the allowlist to request if outbound HTTPS is restricted.

---

## Batch 1 — Netherlands: Core Data Governance (COMPLETED search-only; needs re-verification)

Batch 1 was completed on 2026-08-14 from search-engine results only. The
session's network egress policy blocked all direct page retrieval, so no
authoritative source was read. This trade-off was raised and then accepted
explicitly; every resulting entity carries `verification: search-only` and
`confidence: low`/`medium`.

**The URLs below are now cited as `sources:` on the Batch 1 entities, but
none of them have been read.** They remain listed here as the worklist for
the re-verification pass: fetch each, confirm or correct the claims in the
corresponding entity, then set `verification: primary-source`,
`last_verified`, and per-source `accessed:` dates.

Find all affected entities with: `grep -rl "verification: search-only" .`

### Forum Standaardisatie / open standards

| Candidate source | URL | Verified? |
|---|---|---|
| Lijst open standaarden | https://www.forumstandaardisatie.nl/open-standaarden | No |
| 'Pas toe of leg uit'-standaarden (verplicht) | https://www.forumstandaardisatie.nl/open-standaarden/verplicht | No |
| 'Pas toe of leg uit'-beleid | https://www.forumstandaardisatie.nl/pas-toe-leg-uit-beleid | No |
| Toetsingsprocedure en criteria voor de lijst open standaarden | https://www.forumstandaardisatie.nl/toetsingsprocedure-en-criteria-voor-de-lijst-open-standaarden | No |
| Open Standaarden (Digitale Overheid) | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/open-standaarden/ | No |

### Interbestuurlijke Datastrategie (IBDS) / Federatief Datastelsel (FDS)

| Candidate source | URL | Verified? |
|---|---|---|
| Interbestuurlijke Datastrategie (IBDS) — Digitale Overheid | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/data/interbestuurlijke-datastrategie/ | No |
| Interbestuurlijke Datastrategie (IBDS) — NORA Online | https://www.noraonline.nl/wiki/Interbestuurlijke_Datastrategie_(IBDS) | No |
| Realisatie IBDS — Digitale Overheid | https://www.digitaleoverheid.nl/community/realisatie-ibds/ | No |
| Beleidsevaluatie Interbestuurlijke Datastrategie — Eindrapport (open.overheid.nl) | https://open.overheid.nl/documenten/1edd5ed4-98e8-442e-bcd2-f6ec3f27a754/file | No |
| IBDS / Federatief Datastelsel presentatie (Forum Standaardisatie, Dag van de Interoperabiliteit 2024) | https://www.forumstandaardisatie.nl/sites/default/files/BFS/8-Bijeenkomsten/20241015-Dag-van-de-interoperabiliteit/presentaties/Presentatie-Federatief-Datastelsel-en-resultaten-Mentimeter.pdf | No |

Open questions to resolve when researching: the exact date the IBDS was
presented to the Tweede Kamer; the current status of the IBDS (is it still
running, or superseded/absorbed?); the governance status of the Federatief
Datastelsel and whether a formal "Afsprakenstelsel Federatief Datastelsel"
has been adopted and when; whether FDS is best typed as `framework`,
`initiative` or `programme`.

### NORA

| Candidate source | URL | Verified? |
|---|---|---|
| NORA Online — Positionering NORA | https://www.noraonline.nl/wiki/Positionering_NORA | No |
| NORA — Digitale Overheid | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/nora/ | No |
| Overheidsarchitectuur NORA — ICTU | https://www.ictu.nl/diensten/dienstenoverzicht/overheidsarchitectuur-nora/ | No |
| Architectuur Digitale Overheid — NORA Online | https://www.noraonline.nl/wiki/Architectuur_Digitale_Overheid | No |

Open questions: confirm BZK is opdrachtgever and ICTU is beheerder;
confirm current NORA version and its relationship to GEMMA/EAR/ROSA/PETRA
(the latter are Batch 4 scope but the relationship should be captured).

### Common Ground

| Candidate source | URL | Verified? |
|---|---|---|
| Common Ground — VNG | https://vng.nl/onderwerpen/common-ground | No |
| Programma Common Ground — VNG | https://vng.nl/projecten/programma-common-ground | No |
| Realisatiekoers Common Ground Informatiesamenleving (21 mei 2025) | https://vng.nl/sites/default/files/2025-05/20250521-08b-realisatiekoers-common-ground.pdf | No |

Open questions: current programme status; whether Common Ground is best
typed as `initiative`, `framework` or `programme`; its formal relationship
to GEMMA and to the FDS.

### MIDO (Meerjarenprogramma Infrastructuur Digitale Overheid)

| Candidate source | URL | Verified? |
|---|---|---|
| Wat is het MIDO? | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/wat-is-het-mido/ | No |
| Governance MIDO | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/governance/ | No |
| Kabinetsbeleid MIDO | https://www.digitaleoverheid.nl/mido/kabinetsbeleid/ | No |
| Voortgang MIDO (tijdlijn) | https://www.digitaleoverheid.nl/mido/voortgang-mido/ | No |
| Sturing van de ontwikkeling van de digitale overheid — NORA Online | https://www.noraonline.nl/wiki/Sturing_van_de_ontwikkeling_van_de_digitale_overheid | No |

Open questions: confirm MIDO's start year; confirm the OBDO's composition
and its advisory relationship to the responsible bewindspersoon (the search
result named a specific serving State Secretary, which is exactly the kind
of time-sensitive fact that must be read from the source, not inferred);
confirm the relationship between MIDO, the GDI and the Meerjarenvisie
Digitale Overheid.

### Additional sources located during Batch 1

| Candidate source | URL | Relevant to |
|---|---|---|
| Overheidsbreed Beleidsoverleg Digitale Overheid (OBDO) | https://www.digitaleoverheid.nl/dossiers/regie-op-gegevens/dossierpostcontext/overheidsbrede-beleidsoverleg-digitale-overheid-obdo/ | NL-OBDO |
| Governance Digitale Overheid (VNG) | https://vng.nl/artikelen/governance-digitale-overheid | NL-OBDO, NL-VNG |
| Staatscourant 2018, 9728 | https://zoek.officielebekendmakingen.nl/stcrt-2018-9728.html | NL-OBDO / NL-FORUM-STANDAARDISATIE instellingsbesluit (suspected) |
| Staatscourant 2022, 18861 | https://zoek.officielebekendmakingen.nl/stcrt-2022-18861.html | NL-OBDO / NL-FORUM-STANDAARDISATIE instellingsbesluit (suspected) |
| Forum Standaardisatie — Over ons | https://www.forumstandaardisatie.nl/over-ons | NL-FORUM-STANDAARDISATIE |
| Contactgegevens Stichting ICTU | https://organisaties.overheid.nl/27912852/Stichting_ICTU | NL-ICTU |
| Rapport Governance ICTU (Eerste Kamer) | https://www.eerstekamer.nl/overig/20220816/toelichting_op_governance_ictu/document | NL-ICTU |
| 5.2 Logius — Memorie van toelichting | https://www.rijksfinancien.nl/memorie-van-toelichting/2022/owb/vii/onderdeel/1060049 | NL-LOGIUS, NL-BZK |
| NL DIGITAAL: Data Agenda Overheid (PDF) | https://zoek.officielebekendmakingen.nl/blg-876545.pdf | NL-DATA-AGENDA-OVERHEID |
| Kabinetsbeleid Digitalisering | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/kabinetsbeleid-digitalisering/ | NL-DIGIBETER successor question |

---

## Germany — queued from the second-country batch (2026-08-15)

Every German entity in the Atlas is `verification: search-only`. The items
below are things **not created**, with the reason. Nothing here was omitted
by accident.

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **EN 16931 and Directive 2014/55/EU** | The European e-invoicing norm and its directive. Would connect [[DE-XRECHNUNG]] to [[EU-CEN]] and give the Atlas a standards-body EU→national chain. **Highest-value German item** | Next | Germany batch |
| **IDSA and the IDS reference architecture** | Now referenced by **two** entities in two countries — [[DE-CATENA-X]] follows the IDS-RAM, and [[NL-ISHARE]] records the IDSA incorporating iSHARE into it. Best-evidenced gap in the international layer. Was already queued from Batch 5; the German batch strengthens the case | Next | Batch 5; reinforced Germany batch |
| The sixteen Land INSPIRE transposition acts | Jointly with [[DE-GEOZG]] they constitute Germany's transposition. **Blocked on the `level` ontology question**, not on sourcing | Blocked | Germany batch |
| Land data protection authorities | [[DE-BFDI]] covers federal bodies only; sixteen Land authorities cover the rest. Same blocker | Blocked | Germany batch |
| Individual XÖV standards | XPersonenstand, XMeld, XBau, XPlanung and others. Only [[DE-XRECHNUNG]] is modelled. Creating one entity per standard would inflate the layer without adding structure (brief §1) | Later | Germany batch |
| FIM (Föderales Informationsmanagement) | Named as a third body under the [[DE-FITKO]]'s roof alongside [[DE-KOSIT]] and [[DE-GOVDATA]]; nothing else established. A single mention in a list is not enough | Next | Germany batch |
| DKE | German electrotechnical standards commission, [[DE-DIN]]'s counterpart towards [[EU-CENELEC]] | Later | Germany batch |
| National Gaia-X hubs | Germany's and Austria's hubs are cited as sources on [[EU-GAIA-X]]. A `DE-GAIA-X-HUB` would be a legitimate national entity, not a duplicate — but nothing beyond website existence was established | Later | Germany batch |
| Manufacturing-X and the wider X-family | [[DE-CATENA-X]] sits in a broader German industrial data-space family. No industry domain entity created — Catena-X alone is below the taxonomy §1 threshold | Later | Germany batch |
| Mobility Data Marketplace (MDM) | Replaced by [[DE-MOBILITHEK]] as National Access Point. **No superseded entity created** — unlike [[DE-IWG]], nothing beyond the replacement is established | Later | Germany batch |
| BMWK / BMWE, BMDV / BMV | Co-authors of [[DE-DATENSTRATEGIE]] and publisher of [[DE-MOBILITHEK]] sources. Both ministries have been renamed or reorganised around [[DE-BMDS]] | Next | Germany batch |
| gematik, Gesundheitsdatennutzungsgesetz | German health data infrastructure and legislation. Would connect [[DOMAIN-HEALTH]] to the German layer and possibly to [[EU-EHDS]] | Later | Germany batch |
| Bundesdruckerei; ITZBund | Federal printing/eID body and the federal IT service centre. ITZBund is already cited as a source on [[DE-XOEV]] | Later | Germany batch |
| OZG-Änderungsgesetz | A substantial amending act, deliberately **not** given its own entity — doing so would force the same `supersedes` compromise as [[DE-NIS2UMSUCG]] → [[DE-BSIG]]. Revisit if an amendment relationship type is added | Blocked | Germany batch |
| Lenkungsgremium GDI-DE | Governing committee of [[DE-GDI-DE]]; would be reachable only from that one entity | Later | Germany batch |
| A cybersecurity domain entity | [[DE-BSI]], [[DE-BSIG]], [[DE-NIS2UMSUCG]], [[DE-IT-GRUNDSCHUTZ]], [[EU-NIS2]], [[EU-CER]], [[EU-CYBERSECURITY-ACT]], [[EU-ENISA]], [[NL-BIO]], [[NL-CBW]] would all qualify — **well over the taxonomy §1 threshold**. Not created in this batch to keep a country PR from silently retagging ten existing entities | Next | Germany batch |

## Belgium — queued from the third-country batch (2026-08-15)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **Belgium's Open Data Directive transposition** | The instrument transposing Directive (EU) 2019/1024 was **not identified**. [[BE-HERGEBRUIK-WET]] (2016) is not it. Belgium is the only Atlas country without one recorded | Next | Belgium batch |
| **The PSI Directive (2003/98/EC, as amended 2013/37/EU)** | Predecessor of [[EU-OPEN-DATA-DIRECTIVE]], not an Atlas entity. Would give [[BE-HERGEBRUIK-WET]] and [[DE-IWG]] somewhere to point | Next | Belgium batch; DE-IWG carried |
| **OSLO and Digitaal Vlaanderen** | A major European semantic-interoperability programme, entirely unmodelled. **Blocked on the `level` ontology question**, not on sourcing | Blocked | Belgium batch |
| Agence du Numérique; Paradigm; the Regions and Communities | Same blocker | Blocked | Belgium batch |
| The other five public service integrators | BELGIF names six; only [[BE-KSZ]] is modelled | Later | Belgium batch |
| Belgian eID / itsme; eHealth platform; Kruispuntbank van Ondernemingen | Belgium's digital identity and registry infrastructure, none modelled. itsme is one of Europe's more distinctive national identity schemes | Later | Belgium batch |
| NBN (Bureau voor Normalisatie) | Belgium's national standards body — the counterpart to [[DE-DIN]] and [[NL-NEN]], and the third leg of the CEN/ISO membership pattern | Later | Belgium batch |
| **The Dutch NCSC** | Not an Atlas entity, so [[NL-CBW]] has a NIS2 act with **no authority attached**, while Belgium ([[BE-CCB]]) and Germany ([[DE-BSI]]) both have one. Visible only now that two other countries do | Next | Belgium batch |
| Belgian statistics act | No statutory basis for [[BE-STATBEL]] was found | Later | Belgium batch |

## France — queued from the fourth-country batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **France's Open Data Directive transposition** | Understood to be a 2021 ordinance; not identified. France joins Belgium as the second country with this gap | Next | France batch |
| **INSEE** | National statistical office. Would be the fourth in the Atlas — all of which are unconnected to Eurostat or the UN statistical system. Only a passing mention found | Next | France batch |
| **A French DCAT application profile** | data.gouv.fr exposes DCAT and the European portal harvests it, but no named profile was found. Would complete the DCAT fork across four countries | Next | France batch |
| **The Dutch open-data portal custodian** | [[NL-DATA-OVERHEID]] is the only national portal in the Atlas with no custodian modelled. Three other countries now have one | Next | France batch |
| AFNOR | French national standards body — the fourth leg of the CEN/ISO membership pattern after [[DE-DIN]], [[NL-NEN]] and Belgium's NBN | Later | France batch |
| RGS and RGAA | France's security and accessibility reference frameworks, siblings of [[FR-RGI]] | Later | France batch |
| France Identité | Recorded in prose on [[FR-FRANCECONNECT]]; not its own entity | Later | France batch |
| Health Data Hub | France's health data platform — would connect [[DOMAIN-HEALTH]] to the French layer and possibly to [[EU-EHDS]] | Later | France batch |
| Ordonnance n° 2005-1516 | Legal basis of [[FR-RGI]]; not modelled | Later | France batch |
| Ordonnance of 21 October 2010 | France's INSPIRE transposition, cited on [[EU-INSPIRE]]'s `applies-in`; its number was not established so no entity was created | Later | France batch |

## Spain — queued from the fifth-country batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **European Statistical System (`EU-ESS`)** | The single highest-value item this batch produced. The sources describe Eurostat and the national statistical offices as members of one system; the Atlas currently carries that as one weak `related-to` edge on [[ES-INE]] marked `source: interpretation`. One entity with `part-of` edges would connect **four** national statistical offices at once. Deliberately not created inside a country batch | **Next** | Spain batch |
| **BOE citation for Real Decreto 729/2023** | The decree creating [[ES-AESIA]]. No search result returned its BOE identifier, so the Atlas's first AI Act link rests on secondary sources and government press material | **Next** | Spain batch |
| **Red.es** | Public business entity operating [[ES-DATOS-GOB-ES]]. Cited but too thinly sourced to create, which is why that portal is the only national open data portal in the Atlas besides the Dutch one with no `maintained-by` edge | Next | Spain batch |
| **Spanish organic law on artificial intelligence** | Sources refer to one landing the AI Act domestically with sanctions and sandboxes, at a stage they describe inconsistently. Not created — the Atlas already carries one instrument whose sources conflict ([[FR-NIS2-LOI]]) and does not need a second on weaker evidence | Next | Spain batch |
| **Ley 39/2015 and Ley 40/2015** | Spain's common administrative procedure and public-sector legal regime acts — the current legal base for much of what [[ES-AEAD]] does, and the successors to Ley 11/2007 which established [[ES-ENI]] | Next | Spain batch |
| **Spain's INSPIRE transposition** | [[EU-INSPIRE]] now carries `applies-in` → `ES` with no transposing instrument identified | Later | Spain batch |
| **AENOR / UNE** | Spanish national standards body — the fifth leg of the CEN/ISO membership pattern after [[DE-DIN]], [[NL-NEN]], Belgium's NBN and France's AFNOR | Later | Spain batch |
| **INCIBE's founding instrument** | Its legal form, its relationship to the earlier INTECO, and how INCIBE-CERT relates to CCN-CERT are all unrecorded. [[ES-INCIBE]] is `coverage: low` because of it | Later | Spain batch |
| **Cl@ve's legal basis and operator** | Plus the relationship between Cl@ve PIN and Cl@ve Permanente, and the status of any Spanish digital identity wallet under [[EU-EIDAS2]] | Later | Spain batch |
| **Centro Nacional de Ciberseguridad** | Would be created by [[ES-LCGC]]. **Deliberately not modelled** — it does not exist, and a node for it would be indistinguishable in the graph from a body that does | Blocked | Spain batch |
| **The Comunidades Autónomas** | Seventeen regional open data portals, regional data protection authorities, and the co-governance half of [[ES-ESPANA-DIGITAL-2026]]. **Blocked on the `level` vocabulary**, not on sourcing | Blocked | Spain batch |

## Basisregistraties — queued from the register batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **Wet BAG, Wet BGT, Wet BRO, Wet WOZ, AWR ch. IVA** | Statutory bases named in the ten register descriptions with **no entities**. Six-plus Dutch statutes is a legislation batch; doing half would leave the layer inconsistent | **Next** | Register batch |
| **[[NL-BRT]]'s statutory basis** | The only one of the ten where **no statute was found at all**. Its scale levels and products are also unrecorded — the weakest of the ten | **Next** | Register batch |
| **Handelsregisterwet, Kadasterwet, Wegenverkeerswet** | The statutes behind [[NL-NHR]], [[NL-BRK]] and [[NL-BRV]]; none sourced with a year | Next | Register batch |
| **Digimelding** | The stelsel's facility for reporting suspected errors in the registrations, alongside [[NL-DIGIKOPPELING]]. Named in one sentence of one source | Next | Register batch |
| **SVB-BGT** | Samenwerkingsverband Bronhouders voor de BGT — the cooperative organising seven categories of bronhouder into one national map. Named in one source | Later | Register batch |
| **Rijkswaterstaat, ProRail, RVO** | BGT and BRO bronhouders; none is an Atlas entity | Later | Register batch |
| **Dutch municipalities as entities** | They hold the [[NL-BAG]] and determine [[NL-WOZ]] values. `level: local` exists, so this is **not** the federal gap — the question is what entity to create | Blocked (design) | Register batch |
| **DINO and BIS** | [[NL-BRO]]'s predecessors, described as registrations it *builds on*. Whether either continues to exist determines if `supersedes` is ever right | Later | Register batch |
| **Geonovum's role in BRO standards** | Geonovum publishes BRO geo-standards; whether it maintains them or publishes them for the programme was not established, so no relationship was asserted | Later | Register batch |

## Poland — queued from the sixth-country batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **Dz.U./ISAP citation for [[PL-ODO]]** | The weakest-sourced of the six national GDPR instruments — no primary legal citation found, and its substantive GDPR-specification provisions are entirely unestablished | **Next** | Poland batch |
| **A ministry or Commission source for the eIDAS 2.0 incompatibility** | [[PL-MOBYWATEL]]'s edge to [[EU-EIDAS2]] — the Atlas's **only** eIDAS2 link — rests on press reporting alone | **Next** | Poland batch |
| **CSIRT NASK, CSIRT GOV, CSIRT MON** | Poland's operational cybersecurity bodies. Two of six countries now have cybersecurity legislation modelled and no cyber authority | **Next** | Poland batch |
| **PESEL** | Poland's population register, the direct counterpart of [[NL-BRP]] and the ten Dutch base registries | Next | Poland batch |
| **The operator of [[PL-DANE-GOV-PL]]** | Not identified by any source found. Three of six national open data portals still have no custodian in the graph | Next | Poland batch |
| **Krajowe Ramy Interoperacyjności** | Poland's national interoperability framework — the sixth national NIF, and the sixth potential [[EU-EIF]] descent | Later | Poland batch |
| **A Polish DCAT application profile** | [[EU-DCAT-AP]] has four national children; whether Poland has a fifth was not researched | Later | Poland batch |
| **Ustawa o statystyce publicznej (1995)** | [[PL-GUS]]'s legal basis, named and dated, not modelled — same treatment as the Dutch and Spanish statutes | Later | Poland batch |
| **GIODO** | The predecessor data protection authority. Whether the succession to [[PL-UODO]] can be modelled depends on establishing what happened to the competencies the President did **not** take over | Later | Poland batch |
| **Agencja Informatyzacji** | Would replace [[PL-COI]]. **Blocked** — the draft law is in consultation and the body does not exist | Blocked | Poland batch |

## Other queued research

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| ~~Interprovinciaal Overleg (IPO)~~ | Added in Batch 2 as [[NL-IPO]] | — | Done |
| ~~Unie van Waterschappen (UvW)~~ | Added in Batch 2 as [[NL-UVW]] | — | Done |
| CIO Rijk | Named as an OBDO member; not yet researched | Batch 3 or later | Batch 1 / 2026-08-14 |
| Het Waterschapshuis | Develops and manages shared ICT facilities for the 21 water authorities; sourcing in Batch 2 was a single passing mention | Batch 3 or later | Batch 2 / 2026-08-14 |
| VNG Realisatie | VNG's implementation arm; not yet researched | Batch 3 or later | Batch 2 / 2026-08-14 |
| Centrale Commissie voor de Statistiek (CCS) | Statutory supervisor of the CBS under the Wet op het CBS | Batch 3 or later | Batch 2 / 2026-08-14 |
| Ministerie responsible for CBS (Economic Affairs) | Needed to complete CBS governance; Dutch ministry naming is volatile and must be read from a current source | Batch 3 or later | Batch 2 / 2026-08-14 |
| Adviescollege ICT-toetsing (AcICT) | ICT oversight body; surfaced in Batch 1 search results | Batch 3 or later | Batch 2 / 2026-08-14 |
| DANS, Health-RI, RIVM, NWO | Research/health data infrastructure organisations | Batch 5 | Batch 2 / 2026-08-14 |
| SIDN | .nl registry / internet infrastructure | Batch 5 | Batch 2 / 2026-08-14 |
| ~~BOMOS~~ | Added in Batch 4 as [[NL-BOMOS]] | — | Done |
| Programmaraad (geo-standaarden) | Commissioning body for Geonovum's standards management | Batch 5+ | Batch 2 / 2026-08-14 |
| VNG Realisatie | Now doubly needed: maintains [[NL-GEMMA]], and [[NL-GEMMA]]'s `maintained-by` currently points at [[NL-VNG]] as a simplification | Batch 5+ | Batch 2; raised Batch 4 |
| WILMA (Waterschaps Informatie & Logisch Model Architectuur) | Water authorities' reference architecture; completes the NORA family. Not created in Batch 4 — single mention, and not named in the batch scope (unlike PETRA) | Batch 5+ | Batch 4 / 2026-08-14 |
| Edustandaard | Publishes/maintains [[NL-ROSA]]; its `maintained-by` link is unasserted without it | Batch 5+ | Batch 4 / 2026-08-14 |
| StUF (Standaard Uitwisselings Formaat) | VNG municipal exchange standard. Searched in Batch 4 but no usable source returned — deliberately not created | Batch 5+ | Batch 4 / 2026-08-14 |
| ENSIA | Accountability system paired with the BIO | Batch 5+ | Batch 4 / 2026-08-14 |
| NOiV programme bureau | Built BOMOS; appears historical. Needed to resolve BOMOS custody | Batch 5+ | Batch 4 / 2026-08-14 |
| Remaining 'pas toe of leg uit' standards | Only Digikoppeling and ADR are modelled. The full mandatory + recommended lists (DNSSEC, DMARC, TLS, WCAG, SAML, OAuth profiles, …) are not enumerated | Batch 5+ | Batch 4 / 2026-08-14 |
| The 10 individual basisregistraties | Still not enumerated (carried from Batch 2) | Batch 5 | Batch 2 / 2026-08-14 |
| The ten individual basisregistraties (BRK, BAG, BRP, Handelsregister, BRV, …) | Referenced by [[NL-BASISREGISTRATIES]]; the full list of ten has not been enumerated from a source | Batch 4 or 5 | Batch 2 / 2026-08-14 |
| `DOMAIN-HEALTH` | Needed by [[NL-NICTIZ]]; withheld because taxonomy §1 requires a domain to connect 2+ entities | Batch 5 | Batch 2 / 2026-08-14 |
| `DOMAIN-EDUCATION` | Needed by [[NL-SURF]]; withheld for the same reason | Batch 5 | Batch 2 / 2026-08-14 |
| Handelsregisterwet | Statutory basis of the Handelsregister held by [[NL-KVK]]; not created in Batch 3 for lack of a located source | Batch 4 or later | Batch 2 / 2026-08-14 |
| ~~Archiefwet (and its revision)~~ | Added in Batch 3 as [[NL-ARCHIEFWET-1995]] and [[NL-ARCHIEFWET-2026]] | — | Done |
| ~~Wet op het Centraal bureau voor de statistiek~~ | Added in Batch 3 as [[NL-WET-CBS]] | — | Done |
| ~~TNO-wet (1930)~~ | Added in Batch 3 as [[NL-TNO-WET]] | — | Done |
| ~~EU-GDPR → [[NL-AP]] link~~ | Closed in Batch 3: [[NL-AP]] now links to both [[NL-UAVG]] and [[EU-GDPR]] | — | Done |
| Wet bescherming persoonsgegevens (Wbp) | Predecessor regime replaced by GDPR/UAVG on 25 May 2018; needed for temporal completeness | Batch 4 or later | Batch 3 / 2026-08-14 |
| Aanpassingswet AVG (dossier 34.939) | Adjusted other Dutch legislation to the GDPR | Batch 4 or later | Batch 3 / 2026-08-14 |
| ~~Original NIS Directive~~ | Added in Batch 8 as [[EU-NIS]]; the [[NL-WBNI]] chain is now closed | — | Done |
| Wet weerbaarheid kritieke entiteiten (CER implementation) | Passed alongside the Cyberbeveiligingswet; adjacent to but distinct from NIS2 | Batch 4 or later | Batch 3 / 2026-08-14 |
| Rijksdienst voor Identiteitsgegevens (RvIG) | Administers the BRP under [[NL-WET-BRP]] | Batch 4 or later | Batch 3 / 2026-08-14 |
| NCSC / NCTV | Cybersecurity authorities named in Cyberbeveiligingswet sources | Batch 4 or later | Batch 3 / 2026-08-14 |
| eIDAS → [[NL-WDO]] link | Both eIDAS entities now exist; eIDAS 2.0 ruled out on dates, but the transposition from 910/2014 remains **unsourced** and unasserted | Batch 9+ | Batch 3; updated Batch 8 |
| Wet elektronische publicaties; Wet politiegegevens; Telecommunicatiewet | Further Dutch legislation with data relevance, not assessed in Batch 3 | Batch 4 or later | Batch 3 / 2026-08-14 |
| ISO / IEC / CEN → [[NL-NEN]] links | NEN's most significant relationships; need the international standards bodies | Batch 9 / 13 | Batch 2 / 2026-08-14 |
| ISO/IEC 27001 & 27002 → [[NL-BIO]] link | BIO2 is explicitly based on NEN-EN-ISO/IEC 27001:2023 and 27002:2022; the `based-on` relationship is unassertable until those entities exist | Batch 14 | Batch 4 / 2026-08-14 |
| **W3C DCAT → EU DCAT-AP → [[NL-DCAT-AP-NL]] chain** | A clean international→EU→national standards descent, and one of the clearest demonstrations available of what the Atlas is for. Complete it when Batches 9 and 14 land | Batch 9, 14 | Batch 4 / 2026-08-14 |
| ~~`DOMAIN-EDUCATION`~~ | Created in Batch 5; [[NL-SURF]] and [[NL-ROSA]] tagged | — | Done |
| ~~`DOMAIN-HEALTH`~~ | Created in Batch 5; [[NL-NICTIZ]] and [[NL-HEALTH-RI]] tagged | — | Done |
| ~~Health-RI~~ | Added in Batch 5 as [[NL-HEALTH-RI]] | — | Done |
| Topsector Logistiek | Originator of [[NL-ISHARE]]; needed to assert its `maintained-by` | Batch 10 | Batch 5 / 2026-08-14 |
| digiGO | Initiator of [[NL-DSGO]]; needed to assert its `maintained-by` | Batch 10 | Batch 5 / 2026-08-14 |
| DMI ecosystem; IDSA / IDS architecture | Named in iSHARE sources as data-space users of its trust framework | Batch 10 | Batch 5 / 2026-08-14 |
| Ministerie van Infrastructuur en Waterstaat; Rijkswaterstaat | Founding partners of [[NL-PDOK]] not yet modelled, making its founding collaboration look narrower than it was | Batch 5+ | Batch 5 / 2026-08-14 |
| Ministeries van VWS, EZK, OCW | Named partners of [[NL-HEALTH-RI]] | Batch 5+ | Batch 5 / 2026-08-14 |
| Nationaal Groeifonds | Funds [[NL-HEALTH-RI]] | Batch 5+ | Batch 5 / 2026-08-14 |
| Nationaal Wegenbestand (NWB) | Part of the [[NL-NDW]] expansion | Batch 5+ | Batch 5 / 2026-08-14 |
| ~~EU ITS Directive~~ | Added in Batch 8 as [[EU-ITS-DIRECTIVE]]; the [[NL-NTM]] chain is now closed | — | Done |
| DANS, ODISSEI, RIVM, NWO, SIDN | Research/health/internet-infrastructure organisations still unqueued from Batch 2 | Batch 5+ | Batch 2; carried |
| ~~Official EUR-Lex text for eIDAS 2.0~~ | Found in Batch 8; both entities rebuilt | — | Done |
| ~~Original eIDAS Regulation (910/2014)~~ | Added in Batch 8 as [[EU-EIDAS]] | — | Done |
| ~~CER Directive~~ | Added in Batch 8 as [[EU-CER]] | — | Done |
| ~~Interoperable Europe Act~~ | Added in Batch 8 as [[EU-INTEROPERABLE-EUROPE-ACT]] | — | Done |
| Interoperable Europe Board | Adopts new EIF versions; needed to resolve the EIF/Act relationship | Batch 9 | Batch 7; carried |
| ENISA | Established under [[EU-CYBERSECURITY-ACT]]; relationship unassertable without it | Batch 9 | Batch 8 / 2026-08-14 |
| Free Flow of Non-Personal Data Regulation | Third repeal target of [[EU-DIGITAL-OMNIBUS]] | Batch 9 | Batch 8 / 2026-08-14 |
| Wet weerbaarheid kritieke entiteiten | Dutch CER transposition, approved 15 Apr 2026; should mirror [[NL-CBW]] → [[EU-NIS2]] | Batch 9+ | Batch 3; raised again Batch 8 |
| EUR-Lex citation for the AI Act | [[EU-AI-ACT]] lacks an Official Journal link | Batch 9 | Batch 8 / 2026-08-14 |
| Dutch EUDI Wallet implementation | Every member state must provide one; no Dutch arrangement researched | Batch 9+ | Batch 8 / 2026-08-14 |
| **The 10 remaining common European data spaces** | Batch 10 created Health, Mobility, Green Deal and Agriculture. **Not created:** cultural heritage, energy, finance, industry, language, media, public administrations, research and innovation, skills, tourism — research returned only their names in the list of fourteen | Later | Batch 7; narrowed Batch 10 |
| ~~ENISA~~ | Added in Batch 9 as [[EU-ENISA]] | — | Done |
| ~~W3C source for DCAT~~ | Found in Batch 14; [[INTL-DCAT]] rebuilt on w3.org, confidence low → medium | — | Done |
| ~~W3C (the organisation)~~ | Added in Batch 13 as [[INTL-W3C]] | — | Done |
| ~~ISO/IEC 27001 & 27002~~ | Added in Batch 14; [[NL-BIO]] gap closed | — | Done |
| UN DESA, UNDP, UNESCO, WHO, UNECE | Named in Batch 13's scope; **no usable source located for any**, so none created | Later | Batch 13 / 2026-08-14 |
| World Bank | Named in Batch 13's scope; omitted deliberately — its institutions are technically UN specialised agencies and misclassifying it is the specific error the brief warns against | Later | Batch 13 / 2026-08-14 |
| IEEE | Named in the standards-ecosystem source alongside ISO/IEC/ITU/IETF/W3C; not created | Later | Batch 13 / 2026-08-14 |
| ISO/IEC JTC 1 and SC 27 | Arguably the actual producer of the 27000-family standards | Later | Batch 14 / 2026-08-14 |
| Current-edition URL for ISO/IEC 27002:2022 | The cited ISO OBP link resolves to the superseded 2013 edition | Later | Batch 14 / 2026-08-14 |
| IETF RFCs behind [[NL-PAS-TOE-OF-LEG-UIT]] | HTTPS, DNSSEC, DMARC/SPF/DKIM, TLS all originate in IETF RFCs and are mandatory Dutch standards — a real international → national chain, entirely unmodelled | Later | Batch 13 / 2026-08-14 |
| OECD Privacy Guidelines / data governance recommendations | [[INTL-OECD]] exists but no OECD instrument is modelled | Later | Batch 13 / 2026-08-14 |
| ITU standards | [[UN-ITU]] exists but no ITU standard is modelled | Later | Batch 13 / 2026-08-14 |
| UNCTAD CSTD working group on data governance | May warrant an `initiative` entity if its outputs are substantive | Later | Batch 13 / 2026-08-14 |
| Data quality, information management, digital identity, AI, data sharing, API and knowledge-graph standards | Batch 14's scope lists all of these; **only information security (27001/27002) and metadata (DCAT) were covered** | Later | Batch 14 / 2026-08-14 |
| ~~Interoperable Europe Board~~ | Still not created — two passing mentions only | Later | Batch 7; carried |
| W3C source for DCAT | [[INTL-DCAT]] rests on second-hand descriptions; the top of the flagship standards chain | Batch 14 | Batch 9 / 2026-08-14 |
| W3C (the organisation) | Needed for [[INTL-DCAT]]'s `maintained-by` | Batch 13 | Batch 9 / 2026-08-14 |
| GeoDCAT-AP and StatDCAT-AP | Extensions of [[EU-DCAT-AP]]; GeoDCAT-AP would likely connect [[NL-GEONOVUM]]'s geo and metadata work | Later | Batch 9 / 2026-08-14 |
| ETSI standards | [[EU-ETSI]] exists but **no ETSI standard is modelled**, despite ICT standardisation being central to this Atlas | Later | Batch 9 / 2026-08-14 |
| Regulation (EU) 1025/2012; Regulation (EC) 223/2009 | Legal bases of the ESOs and the European Statistical System; described but not modelled | Later | Batch 9 / 2026-08-14 |
| EUR-Lex citation for EHDS Reg. (EU) 2025/327 | [[EU-EHDS]]'s strongest source is the Parliament's Legislative Observatory | Later | Batch 10 / 2026-08-14 |
| IDSA / IDS architecture | [[NL-ISHARE]]'s documented route into the EU data-space world | Later | Batch 5; carried |
| Environment / Energy / Agriculture domains | Still below the 2-entity threshold even after Batch 10 | Later | Batch 5; rechecked Batch 10 |
| EU AI strategy (if distinct from the AI Act) | Named in Batch 7 scope; no clearly identifiable standalone strategy document found | Batch 8 | Batch 7 / 2026-08-14 |
| Digital Europe Programme; EuroHPC | EU digital infrastructure funding instruments, not researched in Batch 7 | Batch 9 | Batch 7 / 2026-08-14 |
| Energy, Environment, Finance, Justice, Agriculture, Social Security, Built Environment domains | All named in the Batch 5 brief but each currently below the 2-entity threshold in taxonomy §1. Create as the ecosystems that would populate them are researched | Later | Batch 5 / 2026-08-14 |
| College Standaardisatie | Established in 2006 alongside Forum Standaardisatie; current status unknown — may be superseded, which would need a `supersedes` link | Batch 2 | Batch 1 / 2026-08-14 |
| Individual GDI services (DigiD, DigiD Machtigen, MijnOverheid, Digipoort) | Referenced by NL-GDI and NL-LOGIUS but not yet entities; decide whether they warrant separate entities | Batch 2 or 5 | Batch 1 / 2026-08-14 |
| GEMMA, EAR, ROSA, PETRA | NORA's derived reference architectures; need `derived-from`/`based-on` links to NL-NORA | Batch 4 | Batch 1 / 2026-08-14 |
| Individual open standards on the 'pas toe of leg uit' list | Referenced by NL-PAS-TOE-OF-LEG-UIT | Batch 4 | Batch 1 / 2026-08-14 |
| Meerjarenvisie Digitale Overheid; GDI programmeringsplan | Named as MIDO components; may warrant entities or may be publications | Batch 4 | Batch 1 / 2026-08-14 |
