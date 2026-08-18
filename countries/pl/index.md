# Poland — Index

Curated navigation hub for all Poland-scoped (`country: PL`) entities in the
Atlas. This is a human-maintained page, not a generated one — add a wikilink
here whenever a new PL-scoped entity is judged important enough to belong on
the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[PL]]

> **Sourcing caveat.** Every Polish entity below was compiled from
> search-engine results only: the cited pages were confirmed to exist but
> were **not read**, because the working environment blocked page
> retrieval. They carry `verification: search-only` and need a
> re-verification pass against primary sources. See
> `discovery/reverification-allowlist.md`.

## Organisations

- [[PL-MC]] — Ministerstwo Cyfryzacji _(sets direction)_
  - [[PL-COI]] — Centralny Ośrodek Informatyki _(runs the systems; a draft
    law would convert it into an Agencja Informatyzacji)_
- [[PL-UODO]] — data protection authority _(since 25 May 2018)_
- [[PL-GUS]] — national statistical office _(`part-of` [[EU-ESS]])_

## Legislation

- [[PL-ODO]] — Ustawa o ochronie danych osobowych, 2018 _(implements
  [[EU-GDPR]]; ⚠ no Dz.U. citation found)_
- [[PL-KSC]] — Ustawa o krajowym systemie cyberbezpieczeństwa _(NIS2
  amendment in force 3 Apr 2026; ⚠ Poland is before the CJEU for the delay)_
- [[PL-OTWARTE-DANE]] — Ustawa o otwartych danych, 2021 _(transposes
  [[EU-OPEN-DATA-DIRECTIVE]]; repeals the 2016 act)_

## Platforms

- [[PL-MOBYWATEL]] — citizen application and mDowód _(⚠ reported
  **incompatible with eIDAS 2.0**)_
- [[PL-DANE-GOV-PL]] — national open data portal

---

## EU instruments that apply in Poland

**No Polish copy of any EU instrument exists**, and none should be created
(README §"Country-Neutral Architecture"). Each instrument below is a single
Atlas entity now carrying `applies-in` → [[PL]] alongside the other five
countries:

[[EU-GDPR]] · [[EU-NIS2]] · [[EU-CER]] · [[EU-DATA-ACT]] · [[EU-DGA]] ·
[[EU-OPEN-DATA-DIRECTIVE]] · [[EU-AI-ACT]] · [[EU-CYBERSECURITY-ACT]] ·
[[EU-EIDAS2]] · [[EU-SDG]] · [[EU-INTEROPERABLE-EUROPE-ACT]] ·
[[EU-ITS-DIRECTIVE]] · [[EU-INSPIRE]] · [[EU-EHDS]] · [[EU-EIF]] ·
[[EU-DIGITAL-DECADE]] · [[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]]

...and one **UN** instrument: [[UN-AARHUS]].

### The six-country picture

| Instrument | Poland | Spain | France | Belgium | Germany | Netherlands |
|---|---|---|---|---|---|---|
| [[EU-GDPR]] | [[PL-ODO]] | [[ES-LOPDGDD]] | [[FR-LIL]] | [[BE-GDPR-WET]] | [[DE-BDSG]] | [[NL-UAVG]] |
| [[EU-NIS2]] | [[PL-KSC]] ⚠ CJEU | [[ES-LCGC]] ⚠ draft | [[FR-NIS2-LOI]] ⚠ unknown | [[BE-NIS2-WET]] | [[DE-NIS2UMSUCG]] | [[NL-CBW]] |
| [[EU-OPEN-DATA-DIRECTIVE]] | **[[PL-OTWARTE-DANE]]** | [[ES-LEY-37-2007]] | _(not identified)_ | _(not identified)_ | [[DE-DNG]] | [[NL-WHO]] |
| [[EU-EIDAS2]] | **[[PL-MOBYWATEL]]** ⚠ incompatible | _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |
| [[EU-DCAT-AP]] | _(not researched)_ | [[ES-NTI-RISP]] | _(none found)_ | [[BE-DCAT-AP-BE]] | [[DE-DCAT-AP-DE]] | [[NL-DCAT-AP-NL]] |
| [[EU-ESS]] | **[[PL-GUS]]** | [[ES-INE]] | _(INSEE not modelled)_ | [[BE-STATBEL]] | [[DE-DESTATIS]] | [[NL-CBS]] |

## What Poland added to the Atlas's understanding

- **The model is not western-European-shaped either.** A 2004 accession
  state attached with no ontology change, which tests the two assumptions
  five western EU members could not. See [[PL]].
- **The first sourced eIDAS2 link — and it is negative.** [[PL-MOBYWATEL]]
  cannot serve as an EUDI Wallet and must be replaced. Four batches had
  recorded that no country was linked to [[EU-EIDAS2]] at all.
- **A sixth NIS2 state, off the done/not-done axis.** In force *and* before
  the CJEU. See [[PL-KSC]].
- **The 2016-act trap now has a documented answer.** [[PL-OTWARTE-DANE]]
  explicitly repeals Poland's 2016 act — showing what Belgium's and France's
  missing transpositions should look like.
- **The best-sourced [[EU-ESS]] membership so far.** [[PL-GUS]] describes
  the ESS on its own pages rather than being attached by the composition
  rule.

## Intelligence and security services

Added with the intelligence-services batch. Poland has the **most
symmetrical** structure in the Atlas — four services, two acts, one axis
repeated twice:

```
            civilian              military
internal    PL-ABW      2002      PL-SKW      2006
external    PL-AW       2002      PL-SWW      2006
```

- [[PL-ABW]] — internal security _(head reports **directly** to the Prime
  Minister)_
- [[PL-AW]] — foreign intelligence
- [[PL-SKW]] — military counter-intelligence _(⚠ `coverage: low`)_
- [[PL-SWW]] — military intelligence _(⚠ `coverage: low`)_
- [[PL-KSS]] — the Sejm's oversight committee

Legislation:

- [[PL-UABWAW-2002]] — names **both** civilian agencies in its own title.
  The best-sourced statute in the batch: ISAP, the ABW's BIP, and the AW's
  own *Ramy prawne* page.
- [[PL-USKWSWW-2006]] — the military pair. ⚠ **No official Polish
  government URL could be found for it**, in contrast to its civilian
  counterpart.

**[[PL-ABW]] `implements` [[PL-KSC]]**: CSIRT GOV, one of the three
national-level CSIRTs under the national cybersecurity system act, is led by
the Head of the ABW.

⚠ [[PL-KSS]] carries **no `governed-by` edge**, and that is the finding.
Every other oversight body in the batch is created by statute; the KSS comes
from **Chapter 12 of the Sejm's Regulamin** — the chamber's own standing
orders, which the chamber can change.

## Not modelled

- **CSIRT NASK, CSIRT GOV, CSIRT MON** — the operational bodies of the
  national cybersecurity system. Poland therefore joins the Netherlands as a
  country with cybersecurity legislation and **no cyber authority** in
  [[DOMAIN-CYBERSECURITY]].
- **PESEL**, the population register — the direct counterpart of
  [[NL-BRP]], named in [[PL-COI]]'s list of systems and nothing more.
- **The Agencja Informatyzacji** that would replace [[PL-COI]]. It does not
  exist yet.
- **GIODO**, the predecessor data protection authority — the sources say
  the President took over only *part* of its competencies, which is not a
  clean succession.
- **Krajowe Ramy Interoperacyjności**, a Polish DCAT profile, and the Act on
  Public Statistics. All queued in `discovery/research-queue.md`.
