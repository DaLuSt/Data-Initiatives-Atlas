# Research Queue

**Purpose.** A list of specific, scoped research leads that are not yet
entities: something named or implied by an existing entity's sources, but
not itself researched, sourced and written up. This is the Atlas's
to-do list for turning a loose end into a real entity — not a place to
store findings, and not a historical log.

## How to use this file

- **Adding an item.** One row per lead. Name the entity or edge you'd
  create, say why it matters (what it would connect to, what gap it
  closes), and note where it was seen (which existing entity's sources
  mentioned it, or where you found it). Keep it to what's needed to pick
  the item back up cold — this file is a pointer, not a draft.
- **Closing an item.** Once a lead has a `type`, an ID, at least one
  authoritative source read directly, and a clear relationship to the
  rest of the graph, create the entity (or add the relationship) and
  **delete the row**. Don't strike it through — a struck-out row still
  takes up space and this file is supposed to get shorter as work
  closes, not longer.
- **Batches.** When picking up several items in one pass, it's fine to
  work through them together and land them in one commit/PR, but still
  delete each row as its item closes rather than batching the deletions
  into a single end-of-pass edit.
- **When a lead turns out to be unfounded, or the source doesn't hold
  up**, delete the row anyway and say why in the commit — a closed
  question (even "no, that's not real") doesn't belong on an open-work
  list either. If it's worth remembering *that* it was checked and came
  back empty, that belongs in `discovery/unresolved.md` instead.

## Where this differs from the other `discovery/` files

- **`discovery/candidates.md`** is for weaker, less-verified leads —
  compiled from search results rather than a source actually read, or
  not yet clearly scoped enough to research directly. A candidate
  graduates to this file once it's specific enough to act on, and
  graduates again to a real entity once it's sourced.
- **`discovery/unresolved.md`** is for open *questions* about existing
  entities — a fact that couldn't be verified, a relationship that seems
  plausible but isn't directly sourced — not for missing entities.
- **`progress/completed.md`** is the historical record of what has
  already been researched and closed, batch by batch. Once a row here
  closes, its story belongs there and on the entity itself, not in this
  file.

## All queued leads

This page uses the same master-table layout as `discovery/unresolved.md`
(one table, sorted by area; closed rows are deleted, not struck through;
row IDs are `Q1`, `Q2`, … so they cannot be confused with the numeric rows
in `unresolved.md`, and are not renumbered when a row is removed).

| # | Area | Entity / Topic | Lead | Why it matters / where seen | Status | Noted |
|---|---|---|---|---|---|---|
| 1 | Statistics oversight | Italy: Commissione per la garanzia della qualità dell'informazione statistica (COGIS) | A body under d.lgs. 322/1989 art. 12 (name changed in 2012-13) that checks impartiality and quality of the national statistical system; five members, five-year terms, Istat's president attends. Create it when a page can be read: the annual reports are at presidenza.governo.it/COGIS/ (the 2025 report returned HTTP 503 to the agent and all three pages timed out on a runner, 2026-10-11) | The UK's OSR, France's ASP and the EU's ESGAB are in; roadmap #459 asked whether other countries have the same layer. Facts here are from search results only | Open | 2026-10-11 |
| 2 | Statistics oversight | Portugal (Conselho Superior de Estatística) | The national statistical system's steering body under Lei 22/2008 (arts. 10-13), per search summaries of acts that cite it: three-year terms, members named by the Prime Minister. Create it when the law or the Council's own page can be read (`diariodarepublica.pt` is a JavaScript shell) | Sweden's ROS (SE-ROS) and Germany's Statistischer Beirat (DE-STATISTISCHER-BEIRAT) were added 2026-10-11 from their own pages and the statute. Austria and Ireland on 2026-10-11 earlier; Spain's CSE is consultative and was not added | Open | 2026-10-11 |
| 3 | EU core | Digital Services Act (Regulation (EU) 2022/2065) | Create `EU-DSA` from the EUR-Lex text. The EU KIDS Act proposal says in its Article 1 that it 'specifies and complements' this Regulation, and its Article 2(6) refers to DSA Article 28(1). | Candidate C11 (the EU KIDS Act) cannot have its main edge without it. Seen in COM(2026) 681 final, read 2026-11-09. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |
| 4 | EU core | Digital Markets Act (Regulation (EU) 2022/1925) | Create `EU-DMA` from the EUR-Lex text. The EU KIDS Act proposal takes definitions from Article 2 of this Regulation (software application stores, operating systems). | Named in COM(2026) 681 final, Article 3, read 2026-11-09. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |
| 5 | EU core | ePrivacy Directive (Directive 2002/58/EC) | Create `EU-EPRIVACY-DIRECTIVE` from the EUR-Lex text. | [[EU-DIGITAL-OMNIBUS]] says the proposal would amend it; the EU KIDS Act proposal names it beside the GDPR (Article 2(7)). An amendment edge has nothing to point at today. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |
| 6 | EU core | Cyber Resilience Act | Create it from the EUR-Lex text; number and dates not checked. | A cybersecurity regulation for products beside [[EU-NIS2]] and [[EU-CYBERSECURITY-ACT]], which the Atlas holds. Noted in the repository scan of 2026-11-13; no existing entity's source was re-read for it. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |
| 7 | EU core | DORA (the Digital Operational Resilience Act) | Create it from the EUR-Lex text; number and dates not checked. | [[FR-NIS2-LOI]]'s description says the French bill transposes NIS2 together with the Critical Entities Resilience Directive and DORA; [[EU-CER]] exists, DORA does not. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |
| 8 | EU core | European Data Innovation Board | Create it as an organisation once the article of the Data Governance Act that sets it up has been read. | [[EU-DGA]] is in the Atlas without the board it is understood to create; the article was not read for this row, so confirm it first. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |
| 9 | EU core | AI Office (European Commission) | Create it from the Commission's own page or decision; which act establishes it was not checked. | [[EU-AI-ACT]] has no supervising body at EU level in the Atlas. Noted in the repository scan of 2026-11-13. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |
| 10 | EU core | data.europa.eu (the official portal for European data) | Create it as a platform from the portal's own pages. | The national open-data portals are in the Atlas ([[DE-GOVDATA]], [[FR-DATA-GOUV]], [[ES-DATOS-GOB-ES]] and others) and [[EU-DCAT-AP]] exists for cross-portal search, but the EU portal they feed is not. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |
| 11 | EU core | Once-Only Technical System (OOTS) | Create it as a platform from the Commission's pages; its legal basis is understood to be the Single Digital Gateway Regulation, to be confirmed from the text. | [[EU-SDG]] is in the Atlas; the system that carries evidence between Member States under it is not. | Queued (roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771)) | 2026-11-13 |

**11 leads are queued.** Delete a row when its entity exists; when the table is empty again, say so here.
