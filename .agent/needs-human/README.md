# needs-human

Files here flag a decision an autonomous session couldn't make safely from
the evidence available. See `CLAUDE.md`'s "Human intervention" section for
the format and when to use it.

This directory intentionally holds nothing else — no state files, no task
queue. `progress/current-batch.md` and `discovery/unresolved.md` already
serve those roles; see `CLAUDE.md` for the full map.

A human clears an entry by resolving the question and deleting the file.
An autonomous session should never delete its own entry here.
