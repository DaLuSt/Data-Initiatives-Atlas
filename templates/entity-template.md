---
id: SCOPE-SLUG                  # e.g. NL-EXAMPLE-INITIATIVE — see metadata/ontology.md §2
type: initiative                 # one of metadata/controlled-vocabularies.md#type
name: Example Initiative
alternative_names:               # optional
  - EXAMPLE
description: >
  One or two factual sentences. No interpretation, no marketing language.

level: national                  # international | regional | national | sectoral | local
country: NL                      # ISO 3166-1 alpha-2, or null
region: null                     # e.g. EU — optional, not a substitute for country

status: unknown                  # see metadata/controlled-vocabularies.md#status
confidence: low                  # high | medium | low — confidence in THIS Atlas entry
coverage: low                    # high | medium | low — how thoroughly researched

start_date: null
end_date: null
last_verified: null              # ISO date — set once this entry is more than a stub
previous_version: null
successor: null

domains: []                      # list of domain entity ids, e.g. [DOMAIN-MOBILITY]
organisations: []                # lightweight reference list, see metadata/relationship-types.md §1.1
related_entities: []             # lightweight reference list

relationships: []                # provenanced relationships, see metadata/relationship-types.md §1.2
# relationships:
#   - type: implements-requirement-from
#     target: EU-EXAMPLE-REGULATION
#     source: fact
#     evidence: "Explanatory memorandum, section 2"
#     confidence: high
#     valid_from: 2024-01-01
#     valid_until: null

sources: []
# sources:
#   - title: "Official page title"
#     url: "https://example.gov/..."
#     publisher: "Publishing organisation"
#     accessed: "2026-08-14"
---

# Example Initiative

## Description

Factual description, may expand on the frontmatter `description`. Cite
sources inline with a footnote-style reference or by naming the source, e.g.
"According to the Forum Standaardisatie register[^1] ..."

## Relationships

Prose summary of how this entity connects to others, using wikilinks so the
graph stays navigable in Obsidian/GitHub, e.g.:

- Implements requirements from [[EU-EXAMPLE-REGULATION]].
- Maintained by [[NL-EXAMPLE-ORG]].

## Atlas interpretation

*(Only include this section if there is genuine Atlas-derived interpretation
to record, clearly separated from the facts above — see
metadata/relationship-types.md §3. Delete this section if there is none.)*

## Sources

[^1]: Full citation matching an entry in the `sources:` frontmatter list.

---

<!--
Before committing a new entity:
1. Search existing entities for this name/alias to avoid duplicates
   (README §"Do Not Overwrite Existing Work").
2. Confirm the id is unique and has never been used before.
3. Confirm the filename matches the id (lower-cased).
4. Confirm the file lives in the folder mapped from `type`
   (metadata/ontology.md §3).
5. Run the validation suite: python validation/run_all.py
-->
