# Candidates

Entities that appear potentially relevant but have not yet been researched
and sourced enough to add to the graph. Move a row here to a real entity
file once it has a `type`, an ID, at least one authoritative source, and a
clear enough relationship to the rest of the graph — then delete the row.

Do not add anything here without noting where it was seen.

**Cleared 2026-10-03.** Every lead this page carried had been closed, so they
were removed; the page now holds only the one reference measurement below.
Nothing was lost: a lead that became an entity is recorded on that entity and
in `progress/completed.md`; a lead that turned out to be a decision or an open
question is a row in `discovery/unresolved.md`; the one methodological lesson is
in `.agent/research-policy.md`. The page as it stood, with its batch history
and the numbered sections that entity files cite (`candidates.md §1`, `§2`,
`§3`, `§4`, `§6`, "the cheap structural fixes"), is in git at
`d7d07d1:discovery/candidates.md` (`git show d7d07d1:discovery/candidates.md`).
Entity files that say "`candidates.md` had flagged…" refer to that text.

How the table works:

- **Closed rows are removed, not struck through.** A lead that closes is
  recorded where it now lives (above) and its row is deleted.
- **Row IDs are `C1`, `C2`, …** so they cannot be confused with the numeric
  row numbers in `unresolved.md`. They are not renumbered when a row is
  removed, and a removed ID is not reused (`C1`–`C8` are gone).
- **Proposed IDs are written in `backticks`, not `[[wikilinks]]`, when the
  entity does not exist yet.** `validate_links` does not scan `discovery/`, so
  wikilinks here are unchecked by tooling and must be verified by hand.

## All candidates

| # | Area | Entity / Topic | Lead | Why it matters / status detail | Status | Noted |
|---|---|---|---|---|---|---|
| C9 | Coverage | Domain coverage | Which domains are thin? (measured as distinct countries with at least one entity listing the domain) | **Reference, re-measured 2026-10-09 across 63 country anchors:** government 28, cybersecurity 14, national security 9, geospatial 8, environment 7, health 7, digital infrastructure 5, energy 5, finance 5, mobility 5, water 5, chemicals 4, food 4, manufacturing 4, postal 4, research 4, space 4; **three domains sit at 1 or 2 countries**: education at 2; built environment and social security at 1. Deepened on 2026-10-09 by the owner's choice (roadmap #450, "all in alphabetical order"): environment and finance through national transpositions of the Environmental Information Directive in Germany ([[DE-UIG]]), Spain ([[ES-LEY-27-2006]]), Ireland ([[IE-SI-133-2007]]) and Austria ([[AT-UIG]]) and the Spanish payment-services decree-law ([[ES-RDL-19-2018]]); and chemicals, food, manufacturing, postal, research, space and water through the sector annexes of the national NIS2 acts, which were read directly and tagged on [[DE-BSIG]] (Anlagen 1 and 2), [[BE-NIS2-WET]] (Bijlagen I and II) and [[LU-LOI-NIS2]] (Annexes I and II), as [[NL-CBW]] already was. Not added, for want of a source read: Germany's ZAG (its text does not say it implements PSD2), Luxembourg's 2005 environmental information law (Legilux is a JavaScript shell), the French, Dutch and Belgian environmental information measures (France's Légifrance answers 403, the Dutch Wob was repealed in 2022, the Belgian federal law of 5 August 2006 has no dossier number found), and the NIS2 acts of Poland and France (not read; [[FR-NIS2-LOI]] is `unknown`). Mobility has no obvious set of national counterparts to add: [[EU-EMSWE]] and [[UN-LOCODE]] are supra-national. This is a reference measurement, not work to do. | Reference | 2026-08-21; re-measured 2026-10-09 |
| C10 | Coverage | Countries not yet in the Atlas | **132 of the 193 UN member states are not yet implemented** (no country anchor in `countries/`). The Atlas has 63 country anchors; 61 of them are UN member states, and the other two, the Holy See and Kosovo, are not among the 193. | **Count only; the countries are deliberately not listed or added** (owner's instruction, 2026-10-06). Measured against the member-state list on the UN's own page, which has 193 entries, matching each country anchor to its entry by name. The list was read from the live page and is not stored in the repository, so the count changes when an anchor is added or the UN admits a member; re-measure the same way. Which of the 137 are worth adding is a separate decision, to be made country by country (a country needs sources for its legislation and bodies, not just an anchor entity). The 137 were split into 14 randomly drawn groups (seed 20261007; five countries of group 1, #470, were added on 2026-10-09) that are roadmap issues [#470](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/470) to [#483](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/483), sub-issues of [#451](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/451), on milestones 2027.01 to 2028.02; the countries are listed in those issues, not here. | Not yet implemented | UN member states page (https://www.un.org/en/about-us/member-states), accessed 2026-10-06 |

**1 open lead (a count of countries not yet implemented), 1 reference measurement.**

## Where the removed rows went

| Removed row | Now |
|---|---|
| C1 [[EU-INSPIRE]] ↔ [[UN-GGIM]] | `unresolved.md` #227 (open, deliberate non-assertion) |
| C2 UN DESA | `unresolved.md` #229 (declined) |
| C3 Nordic Council and Benelux | `unresolved.md` #230 (declined) |
| C4 `level: local` | `unresolved.md` #231 (declined, level kept unused) |
| C5 `level: sectoral` | retired 2026-10-03, recorded in `metadata/ontology.md` §4 |
| C6 "Modelled on" | `unresolved.md` #232 (declined) |
| C7 enforcement against a member state | `unresolved.md` #44 |
| C8 `type: law` flattens rank | split into types and `rank`; remainder in `unresolved.md` #11 |
