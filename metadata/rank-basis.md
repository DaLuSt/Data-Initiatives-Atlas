# Basis for `rank`, by country

`rank` (ontology §1.2) says where an instrument sits in its legal order.
Whether an instrument is `organic` or `ordinary` can only be read against the
legal system it belongs to, so this file records, for each country that has a
ranked entity, **which ranks the system has, how an instrument of the higher
rank is recognised, and what was checked**. Add a row before setting a rank
for a country that is not listed.

Three things a reader should know about how this was done:

- **The marker is read from the entity's own name.** Where a system has a
  higher statutory rank, an instrument of that rank carries it in its official
  title (*Ley Orgánica*, *loi organique*, *bijzondere wet*, *Lei Orgânica*,
  *ústavní zákon*, *legge costituzionale*). An entity whose name lacks the
  marker is therefore `ordinary`. The two countries where rank is not
  visible in the title (Austria, Estonia) were checked against primary text.
- **EU instruments were checked against the Official Journal record.** An EU
  act's number does not show who adopted it, because `Regulation (EU)
  2023/138` is a Commission act and `Regulation (EU) 2016/679` is not. For
  each one the EU Publications Office's own record was read (CELLAR, by CELEX
  number, `https://publications.europa.eu/resource/celex/<CELEX>` with
  `Accept: application/xml;notice=object`), and the work's **author** and
  **resource type** were taken from it. European Parliament and Council as
  authors of a regulation or directive means a legislative act, `ordinary`;
  the Commission as author of an implementing regulation or a decision means
  `delegated`. Each record's CELEX was checked to match the one requested.
  EUR-Lex pages themselves are not reachable from this environment.
- **The constitutional designations are standard knowledge, not re-sourced.**
  Only the Austria and Estonia rows (and the EU row, above) were checked
  against a primary text in the 2026-10-02 pass; the other rows state the usual
  constitutional designation and were not re-read from each constitution. If a row is wrong
  for an entity, change the entity and the row together.

An instrument with the rank of law that is not an act of parliament (a
decree-law, a legislative decree, a ratified *ordonnance*) is `ordinary`.
A bill or draft has no rank until it is enacted and is left unset (validation
rejects a rank on a `proposed` or `planned` instrument).

| Country | Ranks in the system | How the higher rank is recognised | Checked | Result |
|---|---|---|---|---|
| AT | Constitutional provisions can sit *inside* an ordinary federal act | The text marks them *(Verfassungsbestimmung)* | RIS consolidated text of the E-Government-Gesetz (version of 2026-10-02) searched: no such marker | `AT-EGOVG` is `ordinary` |
| BE | Special-majority laws (*bijzondere wet* / *loi spéciale*) and ordinary laws; regional decrees and ordinances (*decreet*, *décret*, *ordonnantie*, *ordonnance*) have the force of law in their sphere | "Bijzondere wet" or "loi spéciale" in the title | Fifteen entity names read; none carries it. A "loi organique" in the file is a body's founding statute (*organieke wet*), not a rank | All `ordinary` |
| BG | Ordinary law only, for this purpose | none | Name read | `ordinary` |
| CH | Federal acts (*Bundesgesetz*) are the ordinary rank; the Constitution is separate | none needed | Four names read | `ordinary` |
| CZ | Constitutional acts (*ústavní zákon*) and ordinary acts (*zákon*) | "Ústavní zákon" | Four names read | `ordinary` |
| DE | Federal statutes (*Gesetz*) are one rank; the Basic Law is separate. Consent of the Bundesrat does not change rank | none needed | Seventeen names read | `ordinary` |
| EE | Ordinary acts, and acts that may be passed or amended only by a majority of the Riigikogu's membership (Constitution, Art. 104) | The subject: only the acts listed in Art. 104 | Art. 104 read on constituteproject.org (Estonia 2015): it lists citizenship, elections, parliamentary procedure, the Government, the budget, the Bank of Estonia, the State Audit Office, courts, state of emergency and defence acts. `EE-ATS` (public information), `EE-IKS` (personal data) and `EE-KUBERTURVALISUSE-SEADUS` (cybersecurity) are not on it | All `ordinary` |
| EU | Primary law (the Treaties), legislative acts of Parliament and Council, and non-legislative acts of the Commission (delegated and implementing acts, decisions) | The adopting body in the Official Journal record | CELLAR record read for 33 instruments (see above) | 30 `ordinary` (12 directives, 18 regulations); `delegated`: `EU-HVD-REGULATION` (implementing regulation), `EU-CH-ADEQUACY` (Commission Decision 2000/518/EC), `EU-UK-ADEQUACY` (see below). Left unset: `EU-DIGITAL-OMNIBUS` and `EU-FIDA` (proposals) |
| ES | Organic laws (*Ley Orgánica*, Constitution Art. 81) and ordinary laws; decree-laws (*Real Decreto-ley*) have the rank of law | "Ley Orgánica" in the title | Eight entities | `organic`: `ES-LO-2-2002`, `ES-LOPDGDD`; `ordinary`: the other enacted ones; `ES-LCGC` is a draft and unset |
| FI | Acts (*laki*) and the Constitution; exceptions to the Constitution are passed as ordinary acts in a special order | none needed | Name read | `ordinary` |
| FR | Organic laws (*loi organique*, Constitution Art. 46) and ordinary laws; an *ordonnance* ranks as a law once Parliament has ratified it | "Loi organique" in the title | Eight names read; none is organic. Both *ordonnances* are `ordinary` because each was ratified by statute (2009-526 and 2011-12), which comes from search results, not from Légifrance. `FR-NIS2-LOI` is a bill and unset | `ordinary` |
| GB | Acts of Parliament are one rank; there is no organic category | none needed | Nine names read | `ordinary`; `GB-CSRB` is a bill and unset |
| IE | Acts of the Oireachtas are one rank; the Constitution is separate | none needed | Names read | `IE-DPA-2018` `ordinary`; `IE-NCS-BILL` unset |
| IS | Acts (*lög*) are one rank | none needed | Name read | `ordinary` |
| IT | Constitutional laws (*legge costituzionale*, Art. 138) and ordinary laws; a legislative decree (*decreto legislativo*) and a decree-law have the force of law | "Legge costituzionale" | `IT-CAD` is Decreto Legislativo 82/2005 | `ordinary` |
| LI | Acts (*Gesetz*) are one rank | none needed | Name read | `ordinary` |
| LU | Laws (*loi*) are one rank for this purpose | none needed | Three names read | `ordinary` |
| LV | Laws (*likums*) are one rank for this purpose | none needed | Name read | `ordinary` |
| NL | Acts (*wet*) are one rank; a *Rijkswet* would be marked in its title | none needed | Twenty-four names read; `Organisatiewet Kadaster` is a statute, "organisatie" is not a rank | `ordinary`; `NL-ARCHIEFWET-2026` is planned and unset |
| NO | Acts (*lov*) are one rank | none needed | Six names read | `ordinary` |
| PL | Acts (*ustawa*) are one rank; the Constitution is separate | none needed | Eight names read | `ordinary` |
| PT | Organic laws (*Lei Orgânica*) and ordinary laws; a government decree-law (*Decreto-Lei*) has the rank of law | "Lei Orgânica" | Four names read; none carries it | `ordinary` |

Not given a rank, on purpose:

- **EEA Joint Committee Decisions** (`INTL-EEA-JCD-*`) are decisions of a
  body created by an international agreement. They sit in no state's
  hierarchy and are not EU acts, so none of the four values fits.
- **`GB-UK-GDPR`** is retained EU law carried into UK domestic law. Its
  domestic rank is a question of UK law that its own file does not answer, so
  it stays unset.
- **Agreements and soft law** have no rank (ontology §1.2).
- **`EU-UK-ADEQUACY`** covers the decisions renewed on 19 December 2025. The
  Publications Office records for the two original 2021 decisions
  (CELEX 32021D1772 and 32021D1773) say *Implementing decision* by the
  Commission; the 2025 decisions amend those, and their own records were not
  read, so `delegated` rests on that inference.

Instruments below the rank of an act are not in this table: they are
`subordinate-legislation`, which is always `delegated`.
