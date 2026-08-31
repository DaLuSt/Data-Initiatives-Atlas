# Poland — Index

Curated navigation hub for all Poland-scoped (`country: PL`) entities in the
Atlas. This is a human-maintained page, not a generated one — add a wikilink
here whenever a new PL-scoped entity is judged important enough to belong on
the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[PL]]

> **Re-verified 2026-08-26, completed 2026-08-27.** All eighteen
> `search-only` entities are now `verification: primary-source`.
> [[PL-DANE-GOV-PL]] was the last: its own portal remains a JavaScript
> application with no static content to fetch, but a second gov.pl page
> — the Ministry of Digitisation's own page about the portal, not
> previously cited — closed the "operator not identified" gap.
> `isap.sejm.gov.pl` and `sejm.gov.pl` are both genuinely CAPTCHA-blocked
> domain-wide, confirmed on many separate attempts across both passes —
> not a one-off failure. [[PL-PESEL]] and [[PL-EWIDENCJA-LUDNOSCI]],
> added 2026-08-22, were already `verification: primary-source` before
> either pass.

## Organisations

- [[PL-MC]] — Ministerstwo Cyfryzacji _(sets direction; confirmed as
  [[PL-MOBYWATEL]]'s legal operator this pass, and as [[PL-NASK]]'s
  supervising ministry too)_
  - [[PL-COI]] — Centralny Ośrodek Informatyki _(runs the systems; a
    draft law would convert it into an Agencja Informatyzacji; founded
    2010 by the then Ministry of Internal Affairs and Administration —
    `start_date` corrected to `null`, the source gives only the bare year)_
  - [[PL-NASK]] — CSIRT NASK operator and .pl registry _(`governed-by`
    [[PL-MC]], confirmed this pass — previously unestablished)_
- [[PL-UODO]] — data protection authority _(since 25 May 2018; its own
  annual report calls it GIODO's legal successor, stronger language than
  this entity previously carried)_
- [[PL-GUS]] — national statistical office _(`part-of` [[EU-ESS]])_
- [[PL-PKN]] — standards body _(CEN/CENELEC member since 1 January 2004,
  now dated precisely)_
- Intelligence and security services — see below.

## Legislation

- [[PL-ODO]] — Ustawa o ochronie danych osobowych, 2018 _(implements
  [[EU-GDPR]]; official Dz.U. 2018 poz. 1000 citation confirmed
  2026-08-30 via `eli.gov.pl` — ISAP itself remains CAPTCHA-blocked)_
- [[PL-KSC]] — Ustawa o krajowym systemie cyberbezpieczeństwa _(NIS2
  amendment in force 3 Apr 2026; **corrected 2026-08-26**: Poland
  received a Commission letter of formal notice, not a CJEU referral as
  previously stated)_
- [[PL-OTWARTE-DANE]] — Ustawa o otwartych danych, 2021 _(transposes
  [[EU-OPEN-DATA-DIRECTIVE]]; repeals the 2016 act)_
- [[PL-EWIDENCJA-LUDNOSCI]] — Ustawa o ewidencji ludności, 2010 _(legal
  basis for [[PL-PESEL]] since 1 March 2015; ⚠ ISAP unreadable, so only
  the consolidated-text Dz.U. citation is asserted)_

## Platforms

- [[PL-MOBYWATEL]] — citizen application and mDowód _(⚠ reported
  **incompatible with eIDAS 2.0**; `maintained-by` [[PL-MC]], confirmed
  this pass via the Act's own Article 19 — previously unestablished)_
- [[PL-DANE-GOV-PL]] — national open data portal _(`maintained-by`
  [[PL-MC]], confirmed 2026-08-27)_
- [[PL-PESEL]] — population register and identification number
  _(`maintained-by` [[PL-COI]] since 1 March 2015)_

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
| [[EU-NIS2]] | [[PL-KSC]] ⚠ late, formal notice | [[ES-LCGC]] ⚠ draft | [[FR-NIS2-LOI]] ⚠ unknown | [[BE-NIS2-WET]] | [[DE-NIS2UMSUCG]] | [[NL-CBW]] |
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
- **A sixth NIS2 state, off the done/not-done axis.** In force, after
  missing the deadline and drawing a Commission letter of formal notice —
  **not** a CJEU referral, corrected 2026-08-26. See [[PL-KSC]].
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
  The best-sourced statute in the batch: the ABW's BIP and the AW's own
  *Ramy prawne* page were both read directly in the 2026-08-26
  re-verification pass; ISAP itself remains genuinely CAPTCHA-blocked.
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

- ~~**CSIRT NASK, CSIRT GOV, CSIRT MON** — none modelled~~ — **stale as of
  2026-08-26.** [[PL-ABW]] `implements` [[PL-KSC]] for CSIRT GOV and
  [[PL-NASK]] `implements` it for CSIRT NASK, both added in the
  intelligence-services batch but never cross-referenced back to
  [[PL-KSC]]'s own "not modelled" section until this pass. Only **CSIRT
  MON** remains unmodelled, because Poland's Ministry of National Defence
  is not an Atlas entity.
- ~~**PESEL**, the population register~~ — now [[PL-PESEL]] and
  [[PL-EWIDENCJA-LUDNOSCI]].
- **The Agencja Informatyzacji** that would replace [[PL-COI]]. It does not
  exist yet.
- **GIODO**, the predecessor data protection authority. **Narrower as of
  2026-08-26**: UODO's own annual report, read directly, calls the
  President of UODO GIODO's "następcą prawnym" (legal successor) —
  stronger language than the "took over only part of its competencies"
  this index previously carried. Still no GIODO entity exists: GIODO's
  own site no longer resolves (DNS failure), so nothing in its own words
  could be checked.
- **Krajowe Ramy Interoperacyjności**, a Polish DCAT profile, and the Act on
  Public Statistics. All queued in `discovery/research-queue.md`.
