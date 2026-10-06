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
| C9 | Coverage | Domain coverage | Which domains are thin? (measured as distinct countries with at least one entity listing the domain) | **Reference, re-measured 2026-10-03 across 58 country anchors:** government 23, cybersecurity 14, national security 9, geospatial 8, health 5, energy 3, digital infrastructure 3; **thirteen domains sit at 1 or 2 countries**: mobility, postal, research, manufacturing and education at 2; finance, water, space, environment, food, chemicals, social security and built environment at 1 (the last two were created 2026-10-03 when `level: sectoral` was retired, each for two entities in one country). The 2026-08-21 measurement, which listed eight domains, is in git history. Mobility has no obvious set of national counterparts to add: [[EU-EMSWE]] and [[UN-LOCODE]] are supra-national. This is a reference measurement, not work to do. | Reference | 2026-08-21; re-measured 2026-10-03 |
| C10 | Coverage | Countries not yet in the Atlas | **137 of the 193 UN member states are not yet implemented** (no country anchor in `countries/`). The Atlas has 58 country anchors; 56 of them are UN member states, and the other two, the Holy See and Kosovo, are not among the 193. | **Count only; the countries are deliberately not listed or added** (owner's instruction, 2026-10-06). Measured against the member-state list on the UN's own page, which has 193 entries, matching each country anchor to its entry by name. The list was read from the live page and is not stored in the repository, so the count changes when an anchor is added or the UN admits a member; re-measure the same way. Which of the 137 are worth adding is a separate decision, to be made country by country (a country needs sources for its legislation and bodies, not just an anchor entity). | Not yet implemented | UN member states page (https://www.un.org/en/about-us/member-states), accessed 2026-10-06 |

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
