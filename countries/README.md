# countries/

One sub-folder per participating country, `countries/<iso2-lowercase>/`.
Each sub-folder holds exactly two things (`metadata/ontology.md` §3.1):

1. The `country` anchor entity itself, e.g. `nl/nl.md`.
2. A curated `index.md` of wikilinks into the flat type folders
   (`initiatives/`, `legislation/`, ...) for that country's key entities.

A country whose national layer has not been researched still has both: the
anchor carries its position in the European frameworks, and the index is the
standard empty skeleton. Those are marked **anchor only** in the table below.

Country-scoped entities themselves (initiatives, legislation, organisations,
...) do **not** live here — they live in their type folder, tagged with
`country: <ISO2>`.

## Participating countries

**Fifty-eight**, of which thirteen have a modelled national layer,
thirty-seven are European base anchors created on 2026-08-19, and **eight are
outside Europe entirely** — the non-European parties to
[[INTL-CONVENTION-108]], added with that treaty on the same day.

| Country | Code | Folder | State |
|---|---|---|---|
| Andorra | `AD` | [`ad/`](ad/) | anchor only |
| Albania | `AL` | [`al/`](al/) | anchor only |
| Armenia | `AM` | [`am/`](am/) | anchor only |
| Austria | `AT` | [`at/`](at/) | anchor only |
| Azerbaijan | `AZ` | [`az/`](az/) | anchor only |
| Bosnia and Herzegovina | `BA` | [`ba/`](ba/) | anchor only |
| Belgium | `BE` | [`be/`](be/) | modelled |
| Bulgaria | `BG` | [`bg/`](bg/) | anchor only |
| Belarus | `BY` | [`by/`](by/) | anchor only |
| Switzerland | `CH` | [`ch/`](ch/) | modelled |
| Cyprus | `CY` | [`cy/`](cy/) | anchor only |
| Czechia | `CZ` | [`cz/`](cz/) | modelled |
| Germany | `DE` | [`de/`](de/) | modelled |
| Denmark | `DK` | [`dk/`](dk/) | anchor only |
| Estonia | `EE` | [`ee/`](ee/) | anchor only |
| Spain | `ES` | [`es/`](es/) | modelled |
| Finland | `FI` | [`fi/`](fi/) | anchor only |
| France | `FR` | [`fr/`](fr/) | modelled |
| United Kingdom | `GB` | [`gb/`](gb/) | modelled |
| Georgia | `GE` | [`ge/`](ge/) | anchor only |
| Greece | `GR` | [`gr/`](gr/) | anchor only |
| Croatia | `HR` | [`hr/`](hr/) | anchor only |
| Hungary | `HU` | [`hu/`](hu/) | anchor only |
| Ireland | `IE` | [`ie/`](ie/) | modelled |
| Iceland | `IS` | [`is/`](is/) | anchor only |
| Italy | `IT` | [`it/`](it/) | anchor only |
| Liechtenstein | `LI` | [`li/`](li/) | anchor only |
| Lithuania | `LT` | [`lt/`](lt/) | anchor only |
| Luxembourg | `LU` | [`lu/`](lu/) | modelled |
| Latvia | `LV` | [`lv/`](lv/) | anchor only |
| Monaco | `MC` | [`mc/`](mc/) | anchor only |
| Moldova | `MD` | [`md/`](md/) | anchor only |
| Montenegro | `ME` | [`me/`](me/) | anchor only |
| North Macedonia | `MK` | [`mk/`](mk/) | anchor only |
| Malta | `MT` | [`mt/`](mt/) | anchor only |
| Netherlands | `NL` | [`nl/`](nl/) | modelled |
| Norway | `NO` | [`no/`](no/) | modelled |
| Poland | `PL` | [`pl/`](pl/) | modelled |
| Portugal | `PT` | [`pt/`](pt/) | modelled |
| Romania | `RO` | [`ro/`](ro/) | anchor only |
| Serbia | `RS` | [`rs/`](rs/) | anchor only |
| Russia | `RU` | [`ru/`](ru/) | anchor only |
| Sweden | `SE` | [`se/`](se/) | anchor only |
| Slovenia | `SI` | [`si/`](si/) | anchor only |
| Slovakia | `SK` | [`sk/`](sk/) | anchor only |
| San Marino | `SM` | [`sm/`](sm/) | anchor only |
| Türkiye | `TR` | [`tr/`](tr/) | anchor only |
| Ukraine | `UA` | [`ua/`](ua/) | anchor only |
| Holy See | `VA` | [`va/`](va/) | anchor only |
| Kosovo | `XK` | [`xk/`](xk/) | anchor only |

### Eight countries that are not European

| Argentina | `AR` | [`ar/`](ar/) | Convention 108 party |
| Cabo Verde | `CV` | [`cv/`](cv/) | Convention 108 party |
| Mauritius | `MU` | [`mu/`](mu/) | Convention 108 party |
| Mexico | `MX` | [`mx/`](mx/) | Convention 108 party |
| Morocco | `MA` | [`ma/`](ma/) | Convention 108 party |
| Senegal | `SN` | [`sn/`](sn/) | Convention 108 party |
| Tunisia | `TN` | [`tn/`](tn/) | Convention 108 party |
| Uruguay | `UY` | [`uy/`](uy/) | Convention 108 party |

These eight are **not** in the Atlas under the European rule below. They are
here because [[INTL-CONVENTION-108]] — the only binding international treaty
on data protection — is open to accession by any state, and they acceded.
Modelling that treaty without them would have modelled it as the regional
instrument it is expressly not.

They are base anchors and are **not the start of a global country layer**.
The Atlas's scope is European data governance; these eight are the reach of
one treaty. Each says so on its own page.

### Which states count as European

There is no single authoritative list, so the Atlas states its rule instead
of implying one. A state gets an anchor if it satisfies **any** of:

1. **EU membership** — the 27 member states.
2. **EFTA or EEA membership** — [[IS]], [[LI]], [[NO]], [[CH]].
3. **Council of Europe membership** — the 46 member states, plus [[RU]],
   whose membership was terminated in 2022.
4. **A live EU accession relationship** — the nine candidate countries and
   [[XK]] as a potential candidate.

Plus [[BY]] and [[VA]], which are European states satisfying none of the
four: Belarus has never been a Council of Europe member, and the Holy See is
an observer rather than a member.

The rule is a **union, not a geography**. It admits [[AM]], [[AZ]], [[GE]]
and [[TR]], which the UN M49 geoscheme places in Western Asia, on their
Council of Europe membership. Each of those four entities says so on its own
page rather than leaving the reader to wonder. Drawing a tighter line was
possible; drawing it silently was not.

### One code is not an ISO code

[[XK]] is the single exception to `metadata/ontology.md` §3.1's rule that a
national scope segment is the ISO 3166-1 alpha-2 code. Kosovo has no ISO
code; `XK` is a user-assigned code used operationally by the European
Commission, the IMF and the World Bank. §3.1 now names the exception rather
than being quietly broken by it.

Adding a new country means creating its sub-folder with an anchor entity and
an index — the ontology requires no other change (README
§"Country-Neutral Architecture").

## That claim has now been tested

Germany was added as the second country after the Netherlands layer was
complete. What it required, in full:

- a new `de/` sub-folder with an anchor entity and an index;
- German entities added to the **existing flat type folders**, tagged
  `country: DE`;
- `applies-in` → `DE` relationships added to the EU instruments that
  already carried `applies-in` → `NL`.

What it did **not** require: any change to `metadata/schema.json`,
`metadata/ontology.md`, `metadata/taxonomy.md`,
`metadata/relationship-types.md`, the folder structure, or any validation
rule. No entity type, relationship type, status or level was added. No
`DE-EU-*` entity was created.

One genuine limitation surfaced, and it is a limitation of the model rather
than of the country-neutral design: the `level` vocabulary has no term
between `national` and `local`, so Germany's sixteen Länder cannot be
represented.

**Belgium, added third, confirmed the limitation is general and made it
worse.** In Germany no term fits; in Belgium the term that would fit is
already taken, because `level: regional` means *supra-national* in this
Atlas — it is what [[EU]] carries. A Belgian Region cannot even borrow the
word. The cost is concrete: **OSLO**, one of Europe's most developed
public-sector semantic interoperability programmes, is a Flemish product
and is therefore not modelled at all.

**France, added fourth, isolated the defect.** France is unitary, and it is
the first country whose addition raised **no new ontology question at all** —
every entity fitted an existing type, level, status and relationship type,
and nothing needed a caveat about what the Atlas could not express.

That negative result is what makes the finding precise. With only Germany
and Belgium it was unclear whether the model was federal-lossy or simply
Netherlands-shaped. A second unitary state separates the two: the ontology
is sound for unitary states and lossy for federal ones, and the loss is
confined to the `level` vocabulary.

**Spain, added fifth, answered the remaining question and gave the defect a
third shape.** The first four countries are neighbours with similar
administrative traditions, so a reasonable objection was that the ontology
might be *western-European*-shaped rather than country-neutral. Spain is
southern European, joined the EU in a later enlargement, and organises its
state on a constitutional principle none of the others use — and it too
required no ontology, schema, folder, validation or generator change.

It also sharpened the `level` finding rather than repeating it. Spain is a
**State of Autonomies**: seventeen Comunidades Autónomas with devolved
competences of differing scope, which is neither a federation nor a unitary
state. Germany's Länder, Belgium's Regions and Spain's Comunidades Autónomas
are three constitutionally distinct things, and **the Atlas fails on all
three identically**. That is the strongest available evidence that the
defect sits in the `level` vocabulary rather than in any one country's
constitutional shape.

Three of five countries are now affected, and the cost is measurable: in
Spain it hides seventeen regional open data portals and half of a named
axis of the national digital strategy.

**Poland, added sixth, tested the last untested assumption.** The five
before it are all western European; Poland acceded in **2004**, in a
different enlargement, with a post-1989 administrative tradition none of
them share. `progress/backlog.md` had asked whether the EU layer is the
right regional parent for such a state, and whether `applies-in` is the
right way to attach it. **Both held**, with no ontology, schema, folder,
validation or generator change and no `PL-EU-*` entity.

Poland raised two new questions, and both are about **time** rather than
structure: an instrument can be *in force* while the member state is in
infringement proceedings over the delay ([[PL-KSC]]), and a national system
can be *subject to* an EU requirement it **cannot meet**
([[PL-MOBYWATEL]] and eIDAS 2.0). Neither is expressible in the current
vocabulary.

**The United Kingdom, added seventh, was the first real test.** Six batches
produced six EU member states, so every "no change was needed" result until
now was measured against countries that share a regional parent. The UK does
not have one: it is **not an EU member state**, no EU instrument carries
`applies-in` to it, and its entities are the first in the Atlas with
`region: null`.

**That needed no change either** — no schema, ontology, taxonomy,
relationship-type, folder, validation or generator change, and no `GB-EU-*`
entity. The UK reaches the European layer by two edges that already existed
in the vocabulary: `derived-from` for assimilated law
(`GB-UK-GDPR` ← `EU-GDPR`) and `implements-requirement-from` for a
transposition made **while still a member state** and never repealed
(`GB-NIS-REGULATIONS` ← `EU-NIS`).

It also exposed one thing six member states could not. **`country` is a
field, not an edge.** The other six anchors are reachable in the graph only
because EU instruments point `applies-in` at them; with no such edges, `GB`
is the Atlas's first country anchor with no frontmatter-level connection at
all. See `progress/backlog.md`.

No sub-national level has been invented, because doing so for one country
is exactly the country-specific change the model exists to prevent. See
`de/de.md`, `be/be.md`, `fr/fr.md`, `es/es.md`, `pl/pl.md`, `gb/gb.md` and
`discovery/unresolved.md`.
