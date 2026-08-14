# Research Queue

Confirmed-relevant areas that are known to need research but haven't been
worked yet, beyond the batch plan itself (`progress/backlog.md`). Use this
for gaps discovered mid-batch that fall outside the current batch's scope,
so they aren't lost.

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

## Other queued research

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| Interprovinciaal Overleg (IPO) | Named as an OBDO member; belongs in the organisation graph | Batch 2 | Batch 1 / 2026-08-14 |
| Unie van Waterschappen (UvW) | Named as an OBDO member; belongs in the organisation graph | Batch 2 | Batch 1 / 2026-08-14 |
| CIO Rijk | Named as an OBDO member | Batch 2 | Batch 1 / 2026-08-14 |
| College Standaardisatie | Established in 2006 alongside Forum Standaardisatie; current status unknown — may be superseded, which would need a `supersedes` link | Batch 2 | Batch 1 / 2026-08-14 |
| Individual GDI services (DigiD, DigiD Machtigen, MijnOverheid, Digipoort) | Referenced by NL-GDI and NL-LOGIUS but not yet entities; decide whether they warrant separate entities | Batch 2 or 5 | Batch 1 / 2026-08-14 |
| GEMMA, EAR, ROSA, PETRA | NORA's derived reference architectures; need `derived-from`/`based-on` links to NL-NORA | Batch 4 | Batch 1 / 2026-08-14 |
| Individual open standards on the 'pas toe of leg uit' list | Referenced by NL-PAS-TOE-OF-LEG-UIT | Batch 4 | Batch 1 / 2026-08-14 |
| Meerjarenvisie Digitale Overheid; GDI programmeringsplan | Named as MIDO components; may warrant entities or may be publications | Batch 4 | Batch 1 / 2026-08-14 |
