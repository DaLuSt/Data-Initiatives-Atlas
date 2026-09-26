# needs-human

Files here flag a decision an autonomous session couldn't make safely from
the evidence available. See `.agent/operating-model.md`'s "Human
intervention" section for the format and when to use it.

This directory intentionally holds nothing else — no state files, no task
queue. `.agent/state.yaml` and `.agent/current-task.yaml` are the
authoritative live-status files; see `AGENTS.md` for the full map.

A human clears an entry by resolving the question and deleting the file.
An autonomous session should never delete its own entry here.
