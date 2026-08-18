# Norway — Index

Curated navigation hub for all Norway-scoped (`country: NO`) entities in the
Atlas. This is a human-maintained page, not a generated one — add a wikilink
here whenever a new NO-scoped entity is judged important enough to belong on
the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[NO]]

> **Sourcing caveat.** Every Norwegian entity below was compiled from
> search-engine results only: the cited pages were confirmed to exist but
> were **not read**, because the working environment blocked page
> retrieval. They carry `verification: search-only`. See
> `discovery/reverification-allowlist.md`.

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

## Legislation

- [[NO-PERSONOPPLYSNINGSLOVEN]] — Personal Data Act, LOV-2018-06-15-38

## Platforms

- [[NO-ID-PORTEN]] — the national login solution _(**no eIDAS relationship
  in either direction**, like [[GB-ONE-LOGIN]])_
- [[NO-ALTINN]] — the national platform for digital dialogue _(⚠ no
  `maintained-by` edge — see the entity)_

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

**The EEA Agreement and JCD No 154/2018 are not Atlas entities.** Until one
of them is, Norway's route to EU instruments is recorded in prose and not in
the graph. Both are queued in `discovery/candidates.md`.

## Not modelled

- The **EEA Agreement**, the **EEA Joint Committee**, **EFTA**, the **EFTA
  Surveillance Authority** and the **EFTA Court**.
- **Norway's intelligence services** — Etterretningstjenesten and PST. The
  country has a national security authority ([[NO-NSM]]) and no services,
  which is not a complete picture; contrast the seven countries covered by
  the intelligence batch.
- The **sikkerhetsloven** (Security Act), [[NO-NSM]]'s statutory basis, and
  the **statistikkloven**, [[NO-SSB]]'s.
- **Brønnøysundregistrene**, and therefore who actually operates
  [[NO-ALTINN]].
- **Standard Norge**, the national standards body — the same gap Belgium,
  France, Spain and Poland carry.
- Whether **INSPIRE** or **eIDAS** were incorporated into the EEA Agreement.
