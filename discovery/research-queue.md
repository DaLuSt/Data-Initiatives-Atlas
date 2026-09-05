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

## Nothing is currently queued

Every item this file has carried has either become a real entity, been
found already covered by an existing one, or been judged not worth
pursuing (and noted as such in `discovery/unresolved.md` where the
finding itself was worth keeping). Add the next lead above this line,
one row per item, using a "lead / why it matters / where seen" shape.
