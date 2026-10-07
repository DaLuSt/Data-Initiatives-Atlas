# countries/

One sub-folder per participating country, `countries/<iso2-lowercase>/`.
Each sub-folder holds exactly two things (`metadata/ontology.md` §3.1):

1. The `country` anchor entity itself, e.g. `nl/nl.md`.
2. A curated `index.md` of wikilinks into the flat type folders
   (`initiatives/`, `legislation/`, ...) for that country's key entities.

A country whose national layer has not been researched still has both: the
anchor carries its position in the European frameworks, and the index is the
standard empty skeleton. How far each country is modelled is visible on the
site, where the country filter shows its entities.

Country-scoped entities themselves (initiatives, legislation, organisations,
...) do **not** live here — they live in their type folder, tagged with
`country: <ISO2>`.

## Participating countries

Most countries start as a base anchor (an anchor entity and an empty index) and
gain a modelled national layer as contributors add it. The non-European parties
to [[INTL-CONVENTION-108]] were added with that treaty and are listed
separately below.

| Country | Code | Folder |
|---|---|---|
| Andorra | `AD` | [`ad/`](ad/) |
| Albania | `AL` | [`al/`](al/) |
| Armenia | `AM` | [`am/`](am/) |
| Austria | `AT` | [`at/`](at/) |
| Azerbaijan | `AZ` | [`az/`](az/) |
| Bosnia and Herzegovina | `BA` | [`ba/`](ba/) |
| Belgium | `BE` | [`be/`](be/) |
| Bulgaria | `BG` | [`bg/`](bg/) |
| Belarus | `BY` | [`by/`](by/) |
| Switzerland | `CH` | [`ch/`](ch/) |
| Cyprus | `CY` | [`cy/`](cy/) |
| Czechia | `CZ` | [`cz/`](cz/) |
| Germany | `DE` | [`de/`](de/) |
| Denmark | `DK` | [`dk/`](dk/) |
| Estonia | `EE` | [`ee/`](ee/) |
| Spain | `ES` | [`es/`](es/) |
| Finland | `FI` | [`fi/`](fi/) |
| France | `FR` | [`fr/`](fr/) |
| United Kingdom | `GB` | [`gb/`](gb/) |
| Georgia | `GE` | [`ge/`](ge/) |
| Greece | `GR` | [`gr/`](gr/) |
| Croatia | `HR` | [`hr/`](hr/) |
| Hungary | `HU` | [`hu/`](hu/) |
| Ireland | `IE` | [`ie/`](ie/) |
| Iceland | `IS` | [`is/`](is/) |
| Italy | `IT` | [`it/`](it/) |
| Liechtenstein | `LI` | [`li/`](li/) |
| Lithuania | `LT` | [`lt/`](lt/) |
| Luxembourg | `LU` | [`lu/`](lu/) |
| Latvia | `LV` | [`lv/`](lv/) |
| Monaco | `MC` | [`mc/`](mc/) |
| Moldova | `MD` | [`md/`](md/) |
| Montenegro | `ME` | [`me/`](me/) |
| North Macedonia | `MK` | [`mk/`](mk/) |
| Malta | `MT` | [`mt/`](mt/) |
| Netherlands | `NL` | [`nl/`](nl/) |
| Norway | `NO` | [`no/`](no/) |
| Poland | `PL` | [`pl/`](pl/) |
| Portugal | `PT` | [`pt/`](pt/) |
| Romania | `RO` | [`ro/`](ro/) |
| Serbia | `RS` | [`rs/`](rs/) |
| Russia | `RU` | [`ru/`](ru/) |
| Sweden | `SE` | [`se/`](se/) |
| Slovenia | `SI` | [`si/`](si/) |
| Slovakia | `SK` | [`sk/`](sk/) |
| San Marino | `SM` | [`sm/`](sm/) |
| Türkiye | `TR` | [`tr/`](tr/) |
| Ukraine | `UA` | [`ua/`](ua/) |
| Holy See | `VA` | [`va/`](va/) |
| Kosovo | `XK` | [`xk/`](xk/) |

### Countries outside Europe that are parties to Convention 108

| Country | Code | Folder |
|---|---|---|
| Argentina | `AR` | [`ar/`](ar/) |
| Cabo Verde | `CV` | [`cv/`](cv/) |
| Mauritius | `MU` | [`mu/`](mu/) |
| Mexico | `MX` | [`mx/`](mx/) |
| Morocco | `MA` | [`ma/`](ma/) |
| Senegal | `SN` | [`sn/`](sn/) |
| Tunisia | `TN` | [`tn/`](tn/) |
| Uruguay | `UY` | [`uy/`](uy/) |

These eight are **not** in the Atlas under the European rule below. They are
here because [[INTL-CONVENTION-108]] — the only binding international treaty
on data protection — is open to accession by any state, and they acceded.
Modelling that treaty without them would have modelled it as the regional
instrument it is expressly not.

They are base anchors, added for the reach of one treaty rather than as a
global country layer. Each says so on its own page. Whether the Atlas should
extend to every United Nations member state is an open scope decision, tracked
in roadmap issue [#451](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/451);
until it is taken, the European rule below is the rule.

### Which states count as European

There is no single authoritative list, so the Atlas states its rule instead
of implying one. A state gets an anchor if it satisfies **any** of:

1. **EU membership** — every member state.
2. **EFTA or EEA membership** — [[IS]], [[LI]], [[NO]], [[CH]].
3. **Council of Europe membership** — every member state, plus [[RU]],
   whose membership was terminated in 2022.
4. **A live EU accession relationship** — the candidate countries and
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
§"Geographic scope").

## What adding countries has shown

The country-neutral design has been tested against states with very different
constitutional shapes (unitary, federal, devolved, and a non-EU state), and
adding them has not required a change to the schema, ontology, taxonomy,
relationship types, folder structure or any validation rule. Two points are
worth keeping:

- **Sub-national scope.** The `level` vocabulary includes `subnational` (part
  of one country's territory) and `local`, so regions, Länder and similar units
  can be represented. `metadata/ontology.md` defines how each is used.
  `level: regional` still means *supra-national* (it is what [[EU]] carries).
  Where a sub-national programme has not yet been modelled, it is listed in
  `discovery/unresolved.md` rather than invented.
- **Non-EU states.** The United Kingdom is not an EU member state, so no EU
  instrument carries `applies-in` to it and its entities have `region: null`.
  It reaches the European layer through `derived-from` (assimilated law) and
  `implements-requirement-from` (transposition made while still a member
  state). A `country` field is not an edge, so a country anchor with no EU
  instrument pointing at it is connected through its own anchor edges.

No sub-national term was invented for any single country, because doing so for
one country is exactly the country-specific change the model exists to
prevent. See `discovery/unresolved.md` for what is still open, and
`validation/germany-second-country-report.md` for the second-country test.
