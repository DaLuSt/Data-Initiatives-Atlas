# Norway — Index

Curated navigation hub for all Norway-scoped (`country: NO`) entities in the
Atlas. This is a human-maintained page, not a generated one — add a wikilink
here whenever a new NO-scoped entity is judged important enough to belong on
the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[NO]]

> **Re-verified 2026-08-22.** Every Norwegian entity below, plus
> [[INTL-EEA-AGREEMENT]] and [[INTL-EEA-JCD-154-2018]], now carries
> `verification: primary-source`. The network egress restriction this
> caveat described no longer blocks `eur-lex.europa.eu` or
> `europarl.europa.eu` — both were read directly this pass. A significant
> finding: [[NO-NSM]]'s own website confirms NSM is one of Norway's three
> intelligence, surveillance and security services, overturning the
> entity's previous restraint on that question (see the entity for the
> full account).

> ⚠ **`NO` must be quoted in YAML.** `country: NO` unquoted parses as the
> boolean `false` under YAML 1.1, which is what PyYAML implements. Every
> Norwegian entity writes `id: "NO"` and `country: "NO"`. The frontmatter
> validator now catches this with a named error — it was found the hard way
> in this batch.

## Organisations

- [[NO-DIGDIR]] — Digitaliseringsdirektoratet _(sets direction **and** runs
  the national common solutions, like [[GB-GDS]] and [[FR-DINUM]])_
- [[NO-DATATILSYNET]] — data protection authority _(notified to the **EEA
  Joint Committee**, not to the European Commission)_
- [[NO-NSM]] — Nasjonal sikkerhetsmyndighet _(two ministries, one
  directorate: administratively Justice, technically Defence for the
  military sector)_
- [[NO-SSB]] — Statistisk sentralbyrå _(⚠ the only statistical office in the
  Atlas with **no** [[EU-ESS]] edge and no [[UN-CES]] edge)_
- [[NO-KARTVERKET]] — national mapping and cadastral authority
  _(`participates-in` [[UN-GGIM]], confirmed 2026-08-22)_

## Legislation

- [[NO-PERSONOPPLYSNINGSLOVEN]] — Personal Data Act, LOV-2018-06-15-38

## Platforms

- [[NO-ID-PORTEN]] — the national login solution _(**no eIDAS relationship
  in either direction**, like [[GB-ONE-LOGIN]])_
- [[NO-ALTINN]] — the national platform for digital dialogue _(`maintained-by`
  [[NO-DIGDIR]] at `confidence: low`, found 2026-08-22 via the site's own
  publisher footer)_

---

## EU instruments that apply in Norway

**None is recorded, and it is not for the same reason as the United
Kingdom.**

Norway is an **EEA EFTA state**. EU acts do not apply in Norway by force of
Union law. They take effect only once **incorporated into the EEA
Agreement** by a decision of the EEA Joint Committee, and then implemented
in Norwegian law.

The worked example is [[EU-GDPR]]:

| Date | Event |
|---|---|
| 25 May 2018 | GDPR applicable **in the member states** |
| 15 June 2018 | [[NO-PERSONOPPLYSNINGSLOVEN]] adopted |
| **6 July 2018** | **JCD No 154/2018 incorporates the GDPR into Annex XI of the EEA Agreement** |
| **20 July 2018** | The Act enters into force — the GDPR takes effect in Norway |

**Eight weeks** in which the Regulation was in force across the Union and
had no effect in Norway. That gap cannot happen in a member state.

The incorporation also carried an **adaptation**: Norway notifies its
supervisory authority to the EEA Joint Committee rather than to the
Commission, and the GDPR's cooperation mechanisms run through EEA-specific
channels — which is why [[NO-DATATILSYNET]] carries no `participates-in`
[[EU-EDPB]] edge where [[NL-AP]] and [[IE-DPC]] do.

**[[INTL-EEA-AGREEMENT]] and [[INTL-EEA-JCD-154-2018]] are now Atlas
entities**, both re-verified in the same pass as this index, and Norway's
route to [[EU-GDPR]] is drawable end to end through them rather than
recorded only in prose.

## Not modelled

- ~~The **EEA Joint Committee** itself (as opposed to its decisions),
  **EFTA**, the **EFTA Surveillance Authority** and the **EFTA
  Court**~~ — now [[INTL-EEA-JOINT-COMMITTEE]], [[INTL-EFTA]],
  [[INTL-EFTA-SURVEILLANCE-AUTHORITY]] and [[INTL-EFTA-COURT]].
- **Norway's intelligence services** — Etterretningstjenesten and PST.
  [[NO-NSM]]'s own site now confirms it is one of Norway's three
  intelligence, surveillance and security services alongside these two —
  see the entity — but they remain unmodelled themselves, so the country
  still appears with one of three services; contrast the seven countries
  covered by the intelligence batch.
- The **sikkerhetsloven** (Security Act) — named this pass as the 1998
  Act, though whether that is still current or superseded by a newer
  digital-security statute was not resolved — and the **statistikkloven**,
  [[NO-SSB]]'s statutory basis.
- Whether [[NO-DIGDIR]] currently operates [[NO-ALTINN]] outright or
  alongside a continuing **Brønnøysundregistrene** role — the entity now
  carries `maintained-by` at low confidence on the strength of a site
  footer, not a stated operating role.
- **Standard Norge**, the national standards body — the same gap Belgium,
  France, Spain and Poland carry.
- Whether **INSPIRE** or **eIDAS** were incorporated into the EEA Agreement.
