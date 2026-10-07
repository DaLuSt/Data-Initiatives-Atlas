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
- **Constitutions were read on constituteproject.org (English text, the
  version named in each row).** For the countries that have a higher statutory
  rank (AT, BE, CZ, EE, FR, IT, PT; ES is covered in the entity files) the
  designation was confirmed against the constitution's own wording. For the
  countries marked "no higher rank" the constitution was searched for an
  organic, cardinal, qualified-majority or constitutional-law category of
  statute and none was found. That is negative evidence from an English
  translation of a particular year, not a legal opinion. The United Kingdom has
  no written constitution, so that row rests on standard knowledge. Germany
  was read in the official German text (below). If a row is wrong for an entity,
  change the entity and the row together.

An instrument with the rank of law that is not an act of parliament (a
decree-law, a legislative decree, a ratified *ordonnance*) is `ordinary`.
A bill or draft has no rank until it is enacted and is left unset (validation
rejects a rank on a `proposed` or `planned` instrument).

| Country | Ranks in the system | How the higher rank is recognised | Checked | Result |
|---|---|---|---|---|
| AT | Constitutional provisions can sit *inside* an ordinary federal act | The text marks them *(Verfassungsbestimmung)* | RIS consolidated text of the E-Government-Gesetz (version of 2026-10-02) searched: no such marker | `AT-EGOVG` is `ordinary` |
| BE | Special-majority laws (*bijzondere wet* / *loi spéciale*) and ordinary laws; regional decrees and ordinances (*decreet*, *décret*, *ordonnantie*, *ordonnance*) have the force of law in their sphere | "Bijzondere wet" or "loi spéciale" in the title | Constitution (Belgium 2014) read: Art. 4, last paragraph, makes a "law passed by a majority as described in Article 4" a distinct category, and Arts. 11bis and 142 treat "a law, a federate law or a rule referred to in Article 134" side by side. Fifteen entity names read; none carries the special-law marker. A "loi organique" in the file is a body's founding statute (*organieke wet*), not a rank | All `ordinary` |
| BG | Ordinary law only, for this purpose | none | Constitution (Bulgaria 2015) searched: "qualified majority" appears only for votes the Constitution names, not as a category of statute. Name read | `ordinary` |
| CH | Federal acts (*Bundesgesetz*) are the ordinary rank; the Constitution is separate | none needed | Constitution (Switzerland 2014) searched: no higher statutory category found. Four names read | `ordinary` |
| CZ | Constitutional acts (*ústavní zákon*) and ordinary acts (*zákon*) | "Ústavní zákon" | Constitution (Czechia 2013) read: it "may be supplemented or amended only by constitutional acts", which is the higher category. Four names read | `ordinary` |
| DE | Federal statutes (*Gesetz*) are one rank; the Basic Law is separate. Consent of the Bundesrat does not change rank | none needed | Basic Law read in the official German text on gesetze-im-internet.de (the Federal Ministry of Justice, version last amended by Art. 1 of the Act of 22 March 2025, BGBl. 2025 I Nr. 94): Art. 79(1) and (2) say it can be changed only by a statute that expressly alters or supplements its wording, passed by two thirds of the Bundestag and of the Bundesrat; Art. 78 sets when an ordinary federal statute comes into being (Bundesrat consent or no objection), which is procedure, not rank; Art. 80(1) lets a statute authorise ordinances (*Rechtsverordnungen*), the `delegated` rung. No organic or cardinal category of statute appears in the German or the English text. Seventeen names read | `ordinary` |
| EE | Ordinary acts, and acts that may be passed or amended only by a majority of the Riigikogu's membership (Constitution, Art. 104) | The subject: only the acts listed in Art. 104 | Art. 104 read on constituteproject.org (Estonia 2015): it lists citizenship, elections, parliamentary procedure, the Government, the budget, the Bank of Estonia, the State Audit Office, courts, state of emergency and defence acts. `EE-ATS` (public information), `EE-IKS` (personal data) and `EE-KUBERTURVALISUSE-SEADUS` (cybersecurity) are not on it | All `ordinary` |
| EU | Primary law (the Treaties), legislative acts of Parliament and Council, and non-legislative acts of the Commission (delegated and implementing acts, decisions) | The adopting body in the Official Journal record | CELLAR record read for 33 instruments (see above) | 30 `ordinary` (12 directives, 18 regulations); `delegated`: `EU-HVD-REGULATION` (implementing regulation), `EU-CH-ADEQUACY` (Commission Decision 2000/518/EC), `EU-UK-ADEQUACY` (see below). Left unset: `EU-DIGITAL-OMNIBUS` and `EU-FIDA` (proposals) |
| ES | Organic laws (*Ley Orgánica*, Constitution Art. 81) and ordinary laws; decree-laws (*Real Decreto-ley*) have the rank of law | "Ley Orgánica" in the title | Eight entities | `organic`: `ES-LO-2-2002`, `ES-LOPDGDD`; `ordinary`: the other enacted ones; `ES-LCGC` is a draft and unset |
| FI | Acts (*laki*) and the Constitution; exceptions to the Constitution are passed as ordinary acts in a special order | none needed | Constitution (Finland 2011) read: "constitutional act" there means the Constitution itself, and Section 73 gives the Constitution and "a limited derogation of the Constitution" their own enactment procedure (an ordinary act passed under it is still an ordinary act). Name read | `ordinary` |
| FR | Organic laws (*loi organique*, Constitution Art. 46) and ordinary laws; an *ordonnance* ranks as a law once Parliament has ratified it | "Loi organique" in the title | Constitution (France 2008) read: Art. 46 defines organic laws and their procedure; Art. 38 says ordinances lapse unless a ratification bill is tabled and may only be ratified in explicit terms. That a ratified ordinance has the force of law is the Constitutional Council's doctrine, read in its decision no. 2020-851/852 QPC of 3 July 2020, para. 11: "les dispositions d'une ordonnance acquièrent valeur législative à compter de sa signature lorsqu'elles ont été ratifiées par le législateur". Eight names read; none is organic. Both *ordonnances* are `ordinary` because each was ratified by statute. The ratification was read in statute text, not on Légifrance (Cloudflare-blocked): Art. 138 I, 16° of Loi n° 2009-526 names Ordonnance 2005-1516 ("Sont ratifiées"; the enacted text, a copy of the Légifrance page held at data.globalcit.eu), and Art. 1 of Loi n° 2011-12 states "L'ordonnance n° 2010-1232 du 21 octobre 2010 … est ratifiée" (as reproduced by INERIS's AIDA database and by senat.fr). `FR-NIS2-LOI` is a bill and unset | `ordinary` |
| GB | Acts of Parliament are one rank; there is no organic category | none needed | No written constitution. legislation.gov.uk (The National Archives) classes Acts of the UK Parliament as "primary legislation" and statutory instruments and ministerial orders as "secondary", with no higher statutory category; read directly on 2026-10-07 (the page reads with curl and with the fetch tool): the Data Protection Act 2018's contents page files it under "UK Public General Acts" within "All Primary Legislation". The UK Parliament's own sovereignty page is Cloudflare-blocked and was not read. Nine names read | `ordinary`; `GB-CSRB` is a bill and unset |
| IE | Acts of the Oireachtas are one rank; the Constitution is separate | none needed | Constitution (Ireland 2019) searched: no higher statutory category found. Names read | `IE-DPA-2018` `ordinary`; `IE-NCS-BILL` unset |
| IS | Acts (*lög*) are one rank | none needed | Constitution (Iceland 2013) searched: "constitutional law" there means constitutional amendments. Name read | `ordinary` |
| IT | Constitutional laws (*legge costituzionale*, Art. 138) and ordinary laws; a legislative decree (*decreto legislativo*) and a decree-law have the force of law | "Legge costituzionale" | Constitution (Italy 2012) read: Art. 138 ("Laws amending the Constitution and other constitutional laws"), Art. 76 (delegation of legislative function to the Government) and Art. 77 (a decree having force of law). `IT-CAD` is Decreto Legislativo 82/2005 | `ordinary` |
| LI | Acts (*Gesetz*) are one rank | none needed | Constitution (Liechtenstein 2011) searched: no higher statutory category found. Name read | `ordinary` |
| LU | Laws (*loi*) are one rank for this purpose | none needed | Constitution (Luxembourg 2009) searched: no higher statutory category found. Three names read | `ordinary` |
| LV | Laws (*likums*) are one rank for this purpose | none needed | Constitution (Latvia 2016) searched: no higher statutory category found. Name read | `ordinary` |
| NL | Acts (*wet*) are one rank; a *Rijkswet* would be marked in its title | none needed | Constitution (Netherlands 2008) searched: no higher statutory category found. Twenty-four names read; `Organisatiewet Kadaster` is a statute, "organisatie" is not a rank | `ordinary`; `NL-ARCHIEFWET-2026` is planned and unset |
| NO | Acts (*lov*) are one rank | none needed | Constitution (Norway 2014) searched: no higher statutory category found. Six names read | `ordinary` |
| PL | Acts (*ustawa*) are one rank; the Constitution is separate | none needed | Constitution (Poland 2009) searched: the only "Constitutional Act" hits are repealed 1990s acts. Eight names read | `ordinary` |
| PT | Organic laws (*Lei Orgânica*) and ordinary laws; a government decree-law (*Decreto-Lei*) has the rank of law | "Lei Orgânica" | Constitution read in the Portuguese text on the Assembleia da República's site (parlamento.pt): Art. 112(1)–(2) name laws and decree-laws as legislative acts of equal value ("As leis e os decretos-leis têm igual valor"), except that a decree-law made under legislative authorisation is subordinate to the corresponding law; Art. 112(3) gives reinforced value to organic laws, two-thirds laws and some others; Art. 166(2) fixes the matters that must take organic-law form (Art. 164 a–f, h, j, l, q, t and Art. 255: elections, referendums, the Constitutional Court, national defence, states of siege and emergency, citizenship, associations and parties, the intelligence system and state secrecy, regional finance); Art. 168(6) lists the two-thirds matters (the media regulator among them). None of the four Portuguese entities concerns a listed matter (data protection; access to administrative information; cybersecurity), so the marker is not the only evidence here: the subject was checked. The residual Art. 112(3) category (laws that "under this Constitution are compulsory legal prerequisites for other laws or which must be obeyed by other laws") was checked on 2026-10-07 in the English text (constituteproject.org, Portugal 1976 rev. 2005): the Constitution names framework laws for the Budget (Art. 106), for the regions' use of the tax system, and for reprivatisations (Art. 293), and refers to the "basic laws" under which decree-laws are made (Art. 198, 227); none concerns data protection, access to administrative information or cybersecurity, so none of the four is in that category. That is negative evidence from one English text, not a legal opinion | `ordinary` |

Not given a rank, on purpose:

- **EEA Joint Committee Decisions** (`INTL-EEA-JCD-*`) are decisions of a
  body created by an international agreement. They sit in no state's
  hierarchy and are not EU acts, so none of the four values fits.
- **`GB-UK-GDPR`** is retained EU law carried into UK domestic law. Its
  domestic rank is a question of UK law that its own file does not answer, so
  it stays unset.
- **Agreements and soft law** have no rank (ontology §1.2).
- **`EU-UK-ADEQUACY`** covers the decisions renewed on 19 December 2025. The
  Publications Office records for those decisions were read directly:
  CELEX 32025D2574 (amending the GDPR decision 2021/1772) and 32025D2571
  (amending the Law Enforcement Directive decision 2021/1773), plus the
  original 2021 decisions (32021D1772, 32021D1773) and the June 2025
  extensions (32025D1226, 32025D1225). All are *Implementing decision* by the
  European Commission, so `delegated` is confirmed for every decision the
  entity covers.

Instruments below the rank of an act are not in this table: they are
`subordinate-legislation`, which is always `delegated`.
