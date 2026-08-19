---
id: PL-UODO
type: organisation
name: Urząd Ochrony Danych Osobowych
alternative_names:
  - UODO
  - PUODO
  - Prezes Urzędu Ochrony Danych Osobowych
  - Personal Data Protection Office
description: >
  Polish data protection supervisory authority, headed by the President of
  the Office for Personal Data Protection. Since 25 May 2018 the President
  has been the competent body for personal data protection in Poland,
  replacing the Generalny Inspektor Ochrony Danych Osobowych and taking over
  part of that office's tasks and competencies. Its status, tasks,
  competencies and appointment procedure are regulated by the Act of 10 May
  2018 on the protection of personal data. As a supervisory body it is
  subject only to the law. The President is appointed by the Sejm with the
  consent of the Senate for a four-year term, and must hold higher education
  and knowledge and experience in personal data protection. Its main task is
  monitoring and enforcing personal data protection rules in Poland.

level: national
country: PL
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 2018-05-25
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
  - PL-ODO
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Article 68(3) GDPR provides that the European Data Protection Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives; the President of the Personal Data Protection Office is Poland's supervisory authority (gdpr-info.eu 'Art. 68 GDPR — European Data Protection Board'; gdprhub.eu 'Article 68 GDPR'; edpb.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: PL-ODO
    source: fact
    evidence: "The status, tasks, competencies, principles and mode of appointment of the President of the Office for Personal Data Protection are regulated by the provisions of the Act of 10 May 2018 on the protection of personal data; as of 25 May 2018 the President is the competent body for the protection of personal data, and its main task is to monitor and enforce provisions on personal data protection in Poland (uodo.gov.pl; odoserwis.pl PUODO page; politykabezpieczenstwa.pl). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
  - title: "Sprawozdanie z działalności Prezesa Urzędu Ochrony Danych Osobowych w roku 2018"
    url: "https://uodo.gov.pl/pl/file/3909"
    publisher: "Urząd Ochrony Danych Osobowych (UODO)"
  - title: "Prezes Urzędu Ochrony Danych Osobowych (PUODO)"
    url: "https://odoserwis.pl/p/405/prezes-urzedu-ochrony-danych-osobowych-puodo"
    publisher: "odoserwis.pl"
  - title: "Prezes UODO zamiast Generalnego Inspektora ODO"
    url: "https://www.politykabezpieczenstwa.pl/pl/a/puodo-zamiast-giodo"
    publisher: "Polityka Bezpieczeństwa"
  - title: "Generalny Inspektor Ochrony Danych Osobowych — archiwum GIODO"
    url: "https://archiwum.giodo.gov.pl/"
    publisher: "Generalny Inspektor Ochrony Danych Osobowych (archive)"
---

# UODO — Urząd Ochrony Danych Osobowych

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The **President of the Office for Personal Data Protection** has been
Poland's competent data protection body since **25 May 2018** — the day the
GDPR became applicable. The office is regulated by the **Act of 10 May 2018**
([[PL-ODO]]), and as a supervisory body is **subject only to the law**.

The President is **appointed by the Sejm with the consent of the Senate**
for a **four-year term**, and must hold higher education plus knowledge and
experience in data protection.

## Six national DPAs, one European link

| Country | Authority | `participates-in` [[EU-EDPB]]? |
|---|---|---|
| Netherlands | [[NL-AP]] | **yes** — sourced |
| Germany | [[DE-BFDI]] | no — refused |
| Belgium | [[BE-APD]] | no — refused |
| France | [[FR-CNIL]] | no — refused |
| Spain | [[ES-AEPD]] | no — refused |
| **Poland** | **UODO** | no — refused |

Six now, and the sourced-link count is still **one**.

[[FR-CNIL]] called this *"the Atlas's clearest single example of a sourcing
artefact masquerading as structure"* at four. [[ES-AEPD]] noted that a fifth
made it *"more expensive to leave open"* rather than clearer. A sixth adds
nothing but cost: a reader taking the graph at face value would conclude the
European Data Protection Board has one member out of six modelled
candidates, all of which certainly sit on it.

Nothing was asserted, because no source read for the Polish authority
mentions the EDPB. **Six page reads would fix five edges.** It remains the
cheapest high-value item in `discovery/unresolved.md`, and it has now
survived four country batches.

## A second organisational succession, not modelled

The President **replaced the Generalny Inspektor Ochrony Danych Osobowych
(GIODO)**, taking over part of that office's tasks and competencies — the
archived GIODO site is cited above.

**No GIODO entity was created and no `supersedes` edge asserted.** The
sources say the President took over *part* of GIODO's competencies, which is
not the clean succession [[ES-AEAD]] → [[ES-SGAD]] records, and nothing read
establishes what happened to the remainder. Creating a superseded entity on
that basis would assert a tidier transition than the evidence supports.

Logged in `discovery/research-queue.md`. It is the third institutional
transformation the Atlas has now touched — Spain's completed, Poland's COI
one pending, and this one partial — which is starting to look like a
recurring shape worth handling deliberately rather than case by case.

## `coverage: low`

The office's structure, staffing, sanctioning record and its relationship
to sectoral regulators are unrecorded, and two of the four sources are
secondary commentary rather than UODO publications.

## Relationships

- `applies-to` [[PL-ODO]].

## Sources

Listed in frontmatter.
