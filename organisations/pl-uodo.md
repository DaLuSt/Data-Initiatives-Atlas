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
verification: primary-source

start_date: 2018-05-25
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading gdpr-info.eu's own text of Article 68(3) GDPR directly (2026-08-26): 'The Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives.' The President of UODO is Poland's supervisory authority, per UODO's own annual report, also read directly. `gdprhub.eu` was not read this pass."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: PL-ODO
    source: fact
    evidence: "Confirmed by reading UODO's own 2018 annual report directly (2026-08-26): it is submitted under 'art. 50 ustawy z dnia 10 maja 2018 r. o ochronie danych osobowych' (Article 50 of the Act of 10 May 2018), the President's own statutory reporting obligation. odoserwis.pl, also read directly, confirms the President is appointed by the Sejm with Senate consent for a four-year term."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-26"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
  - title: "Sprawozdanie z działalności Prezesa Urzędu Ochrony Danych Osobowych w roku 2018"
    url: "https://uodo.gov.pl/pl/file/3909"
    publisher: "Urząd Ochrony Danych Osobowych (UODO)"
    accessed: "2026-08-26"
  - title: "Prezes Urzędu Ochrony Danych Osobowych (PUODO)"
    url: "https://odoserwis.pl/p/405/prezes-urzedu-ochrony-danych-osobowych-puodo"
    publisher: "odoserwis.pl"
    accessed: "2026-08-26"
  - title: "Prezes UODO zamiast Generalnego Inspektora ODO"
    url: "https://www.politykabezpieczenstwa.pl/pl/a/puodo-zamiast-giodo"
    publisher: "Polityka Bezpieczeństwa"
    accessed: "2026-08-26"
  - title: "Generalny Inspektor Ochrony Danych Osobowych — archiwum GIODO (domain no longer resolves)"
    url: "https://archiwum.giodo.gov.pl/"
    publisher: "Generalny Inspektor Ochrony Danych Osobowych (archive)"
---

# UODO — Urząd Ochrony Danych Osobowych

> **Verified 2026-08-26.** Four of six cited pages were read directly.
> UODO's own 2018 annual report uses stronger language for the GIODO
> transition than this entity previously carried — see below.
> `archiwum.giodo.gov.pl` no longer resolves at all (DNS failure, not a
> 403); `gdprhub.eu` was not read this pass.

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

## The GIODO succession — stronger language found, still no entity created

The President **replaced the Generalny Inspektor Ochrony Danych Osobowych
(GIODO)**. This entity previously hedged that as "took over *part* of
GIODO's competencies... not a clean succession." UODO's own 2018 annual
report, read directly this pass, uses more definite language: it covers
"działalność Prezesa UODO od 25 maja do 31 grudnia 2018 r. oraz działalność
[GIODO], **którego Prezes UODO jest następcą prawnym**" (the activity of
the President of UODO from 25 May to 31 December 2018, and the activity
of GIODO, **whose legal successor the President of UODO is**) for the
period before that. politykabezpieczenstwa.pl, also read directly, frames
it even more simply as a renaming: "urząd... GIODO... został przemianowany
na Prezesa [UODO]" (the GIODO office was renamed to the President of
UODO).

Both readings point the same way — a continuation under new law rather
than a partial, uncertain handover — and the "not a clean succession"
caveat this entity previously carried reads like an overcaution now.
**Still no GIODO entity was created and no `supersedes` edge asserted**:
`archiwum.giodo.gov.pl`'s own site, which would be GIODO's own voice on
the matter, no longer resolves at all (DNS failure), so nothing GIODO
itself said could be checked. Creating a predecessor entity from only the
successor's own characterisation would be one-sided.

Logged in `discovery/research-queue.md`, narrower than before: the
succession's *character* now has primary-source support, and what
remains open is only whether the transition merits its own entity.

## `coverage: low`

The office's structure, staffing, sanctioning record and its relationship
to sectoral regulators are unrecorded, and several of the six sources are
secondary commentary rather than UODO publications.

## Relationships

- `applies-to` [[PL-ODO]].

## Sources

Listed in frontmatter, four of six read directly this pass.
`archiwum.giodo.gov.pl` no longer resolves; `gdprhub.eu` was not
attempted.
