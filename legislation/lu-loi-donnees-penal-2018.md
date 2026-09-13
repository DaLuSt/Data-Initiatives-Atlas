---
id: LU-LOI-DONNEES-PENAL-2018
type: law
name: "Loi du 1er août 2018 relative à la protection des personnes physiques à l'égard du traitement des données à caractère personnel en matière pénale ainsi qu'en matière de sécurité nationale"
alternative_names:
  - Luxembourg Law Enforcement Directive Implementation Act
description: >
  Luxembourg's companion act to the Loi du 1er août 2018 sur la protection
  des données (Mémorial A No. 686), transposing the EU's Law Enforcement
  Directive (2016/680) for personal data processing in criminal and
  national-security matters. Published as Mémorial A No. 689. It applies
  to the police, the State Intelligence Service, the national security
  authority, the army, and the financial intelligence unit, and amends
  fifteen other Luxembourg acts, including those governing the Police
  grand-ducale, the Inspection générale de la Police, and the State
  Intelligence Service.

level: national
country: LU
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: "2018-08-01"
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-NATIONAL-SECURITY
organisations:
  - LU-CNPD
related_entities:
  - EU-LED
  - LU-LOI-PROTECTION-DONNEES
relationships:
  - type: implements-requirement-from
    target: EU-LED
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (LU-LOI-PROTECTION-DONNEES's own 'not modelled' note). Confirmed by reading the Journal Officiel's own text directly, via data.legilux.public.lu's static filestore (which serves readable PDFs even though legilux.public.lu's own page is a JavaScript SPA returning no static content): Mémorial A No. 689 du 16 août 2018 carries the law's full official title, 'Loi du 1er août 2018 relative à la protection des personnes physiques à l'égard du traitement des données à caractère personnel en matière pénale ainsi qu'en matière de sécurité nationale', and Article 1er defines its scope as processing by any 'autorité compétente' for crime prevention, detection, investigation or prosecution, or the execution of criminal sanctions, including protection against threats to public security. A WebSearch cross-check independently confirmed the same law transposes EU Directive 2016/680 (the Law Enforcement Directive) into Luxembourg law, matching CNPD's own 'Droit luxembourgeois' page, which already named this as the LED implementation companion to LU-LOI-PROTECTION-DONNEES's GDPR implementation."
    confidence: high
    valid_from: "2018-08-01"
    valid_until: null
  - type: applies-to
    target: LU-CNPD
    source: fact
    evidence: "Article 2(1)(15°) of the Act's own text, read directly via data.legilux.public.lu, defines 'autorité de contrôle' for its purposes as (a) the CNPD, 'instituée par la loi du 1er août 2018 portant organisation de la Commission nationale pour la protection des données' — the sibling Act, Mémorial A No. 686 — and (b) a separate judicial supervisory authority instituted by the Act's own Article 40, not itself modelled as an Atlas entity."
    confidence: high
    valid_from: "2018-08-01"
    valid_until: null

sources:
  - title: "JOURNAL OFFICIEL DU GRAND-DUCHÉ DE LUXEMBOURG — MÉMORIAL A N° 689 du 16 août 2018"
    url: "https://data.legilux.public.lu/filestore/eli/etat/leg/loi/2018/08/01/a689/jo/fr/pdfa/eli-etat-leg-loi-2018-08-01-a689-jo-fr-pdfa.pdf"
    publisher: "Journal Officiel du Grand-Duché de Luxembourg (Legilux)"
    accessed: "2026-09-13"
  - title: "Droit luxembourgeois — CNPD"
    url: "https://cnpd.public.lu/fr/legislation/droit-lux.html"
    publisher: "Commission nationale pour la protection des données (CNPD)"
    accessed: "2026-09-05"
---

# Loi du 1er août 2018 (Luxembourg's LED implementation)

> **Created 2026-09-13.** [[LU-LOI-PROTECTION-DONNEES]]'s own file named this
> as a "second, separate law of the same date... not modelled here or
> anywhere else in the Atlas yet." Closed by reading the Journal Officiel's
> own text directly — found via `data.legilux.public.lu`'s static filestore,
> which serves readable PDFs even though `legilux.public.lu`'s own page is
> a JavaScript single-page application that has returned no static content
> on every prior pass. This is the first Luxembourg legislation entity in
> the Atlas sourced from Legilux's own text rather than a secondary
> description of it.

## Description

Luxembourg's twin data-protection acts of **1 August 2018** split GDPR
implementation from Law Enforcement Directive implementation, unlike most
member states in the Atlas, which fold both into one act. This entity is
the second half: it transposes the EU's **Law Enforcement Directive**
([[EU-LED]], 2016/680) for data processing in **criminal and
national-security matters**, published as **Mémorial A No. 689** (16
August 2018) — [[LU-LOI-PROTECTION-DONNEES]] (Mémorial A No. 686, the
same date) covers the GDPR side.

Confirmed by reading the Act's own text directly: **Article 1er** defines
its scope as processing carried out for the prevention, detection,
investigation or prosecution of criminal offences, or the execution of
criminal penalties, including protection against threats to public
security, by any "autorité compétente." Article 1(2) extends this
explicitly to:

- the **Police grand-ducale**, for tasks outside ordinary policing;
- the **Service de renseignement de l'État** (State Intelligence
  Service), under its own 5 July 2016 reorganisation act;
- the **Autorité nationale de sécurité** (national security clearance
  authority);
- the **Armée luxembourgeoise** (Luxembourg Army);
- the **Cellule de renseignement financier** (financial intelligence
  unit).

The Act was **signed by Grand-Duc Henri** following approval by the
Chambre des Députés on 26 July 2018 and the Conseil d'État's opinion of
27 July 2018 (dispensing with a second vote). It **amends fifteen other
Luxembourg acts** listed in its own preamble, spanning judicial
organisation (1980), Europol/customs-cooperation conventions (1998,
2002), security classifications (2004), the socio-educational centre
(2004), genetic-fingerprint procedures (2006), traveller checks in
accommodation establishments (2008), the judicial record (2013),
cross-border road-safety information exchange (2014), automated
sanctions (2015), the State Intelligence Service's reorganisation and
its specific personal-data regime (both 2016), police information
exchange (2018), the Police grand-ducale (2018), and the Inspection
générale de la Police (2018).

## The supervisory authority, confirmed from the Act's own definitions

Article 2(1)(15°), read directly, defines "autorité de contrôle" for this
Act's purposes as **the CNPD** — citing [[LU-LOI-PROTECTION-DONNEES]] by
its own full title — **and** a separate judicial control authority
instituted by the Act's own Article 40, not itself an Atlas entity. This
gives [[LU-CNPD]] a second Luxembourg statutory basis alongside the GDPR
one, both dated the same day.

## `data.legilux.public.lu` as a working alternate to a blocked domain

`legilux.public.lu` itself has been confirmed unreadable across at least
two prior passes (LU-CNPD, 2026-08-25; [[LU-LOI-PROTECTION-DONNEES]],
2026-09-05) — a JavaScript single-page application with no static
content this environment's fetch tooling can retrieve. Its **filestore
subdomain**, `data.legilux.public.lu`, serving direct PDF paths in the
form `.../eli/etat/leg/loi/YYYY/MM/DD/aNNN/jo/fr/pdfa/...`, is not
blocked and returns the Journal Officiel's own scanned/typeset text in
full. This is a genuine workaround for future Luxembourg legislation
passes, not previously identified in `discovery/unresolved.md`'s "Known
source-access blocks" section.

## Not modelled

- **The Act's own Article 40** judicial control authority, distinct from
  the CNPD — named in the Act's own definitions but not independently
  researched this pass.
- **The fifteen amended acts**, none individually researched or modelled
  here; the 5 July 2016 State Intelligence Service reorganisation act in
  particular is a plausible future [[LU]] intelligence-oversight entity,
  parallel to [[NO-ETTERRETNINGSTJENESTELOVEN]] and similar acts already
  modelled for other countries, but not created on this pass's evidence
  alone.

## Relationships

- `implements-requirement-from` [[EU-LED]] — Article 1's own scope
  definition matches the Directive's subject matter precisely.
- `applies-to` [[LU-CNPD]] — named as one of two supervisory authorities
  in the Act's own Article 2(1)(15°).

## Sources

Two of two read directly: the Journal Officiel's own text (Mémorial A No.
689), retrieved via Legilux's filestore subdomain rather than its
unreadable main site, and CNPD's own legislation page, already cited on
[[LU-LOI-PROTECTION-DONNEES]].
