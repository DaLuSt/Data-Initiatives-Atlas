---
id: FR
type: country
name: France
alternative_names:
  - French Republic
  - République française
description: >
  Country anchor entity for France, the fourth national scope covered by
  the Data Initiatives Atlas. Used as the target of `country` fields and
  `applies-in` relationships for French-scoped entities.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Confirmed verbatim by reading european-union.europa.eu's own 'EU countries' page directly (2026-08-26): 'France EU Member State since 1958, Euro area member since 1999, Schengen area member since 1995.' Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-26"
  - title: "La direction interministérielle du numérique (DINUM)"
    url: "https://www.numerique.gouv.fr/numerique-etat/dinum/"
    publisher: "DINUM — numerique.gouv.fr"
    accessed: "2026-08-26"
  - title: "FR — France (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:FR"
    publisher: "International Organization for Standardization (ISO)"
  - title: "LOI n° 2016-1321 du 7 octobre 2016 pour une République numérique"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033202746"
    publisher: "Légifrance (Direction de l'information légale et administrative)"
---

# France

> **Re-verified 2026-08-26.** `european-union.europa.eu` was read
> directly and confirms EU, euro-area and Schengen membership verbatim.
> `legifrance.gouv.fr` is genuinely bot-walled (403) even with an
> honest, identifying User-Agent — confirmed on multiple JORF text
> pages across this cluster, contrary to this file's own earlier note
> that Légifrance was confirmed readable on 2026-08-21 (that
> confirmation evidently no longer holds, or covered a different part
> of the site). `iso.org` remains bot-walled as established elsewhere
> this session.

## Description

France (ISO 3166-1 alpha-2: `FR`) is the **fourth country** populated in
the Data Initiatives Atlas, after [[NL]], [[DE]] and [[BE]].

French entities live in the same flat type folders as every other country's,
tagged `country: FR`. EU instruments that apply in France reference it via
an `applies-in` relationship — the same single entity that already carries
`applies-in` to three other countries.

## Why France, specifically

`progress/backlog.md` asked for this one by name:

> *A fourth country — a **unitary** one. All three tests so far have been
> the Netherlands plus two federal states. A second unitary country would
> show whether anything else in the model is Netherlands-shaped, which the
> two federal cases could not isolate.*

Germany and Belgium both strained the model in the same place — the missing
sub-national `level` — and that shared failure made it hard to tell whether
anything *else* was wrong. A second unitary state separates the two
questions.

**Result: nothing else broke.** France is the first country added that
raised **no new ontology question at all**. Every entity fits an existing
type, level, status and relationship type; nothing needed a caveat about
what the Atlas could not express.

That is a genuinely informative negative. Combined with the German and
Belgian batches it isolates the defect: the Atlas's ontology is sound for
unitary states and lossy for federal ones, and the loss is confined to the
`level` vocabulary rather than being a general country-shape problem.

## France is *more* centralised than the Netherlands, not less

The obvious worry with a second unitary country is that it would just
re-confirm the first. It does not, because France sits further along the
same axis:

- [[FR-DINUM]] is a service of the **Prime Minister**, setting the state's
  digital strategy across all ministries.
- [[FR-ETALAB]] is a **department inside DINUM**, not a separate body — so
  France's open-data function is one level *inside* its digital-government
  function.
- [[FR-RGI]] is a **legal obligation** under an ordonnance, not a
  comply-or-explain list like [[NL-PAS-TOE-OF-LEG-UIT]].

So the four countries now span a real range — France (centralised, binding),
the Netherlands (central, comply-or-explain), Belgium (federal, coordinated
by agreement), Germany (federal, Bund-Länder council) — and the model
carried all four without modification.

## The one thing France does that no other country here does

France implemented the GDPR by **amending a 1978 act rather than passing a
new one**, and the sources record that as a deliberate, symbolic choice.
See [[FR-LIL]]. The Atlas already had trouble with an amending act in
Germany ([[DE-NIS2UMSUCG]] → [[DE-BSIG]]); France shows the pattern is not
a German quirk, and — because the amended act keeps its own identity —
shows the case the Atlas models *well*.

## Relationships

See `countries/fr/index.md` for the curated index of French entities.

## ⚠ Two dates, and why this entity uses 1958

A verification pass on 2026-08-20 supplied **25 March 1957** as this
country's accession date. This entity says **1 January 1958**. Both are
right, about different events:

| Date | Event |
|---|---|
| **25 March 1957** | the Treaty of Rome was **signed**, in Rome |
| **1 January 1958** | the Treaty **entered into force**, and the Communities existed |

Strictly neither is an *accession*. The six founding members — [[BE]],
[[DE]], [[FR]], [[IT]], [[LU]] and [[NL]] — did not accede to anything; they
founded it. "Accession date" is a column borrowed from the twenty-one states
that did join later.

The Atlas uses **1 January 1958** because that is what its own cited source
says: the Union's list of EU countries records the founding six under 1958,
and this entity's `part-of` [[EU]] evidence cites that page. Using 1957 would
put the entity in contradiction with the source it names.

**This is recorded rather than resolved.** The signature date is genuinely
useful and is now here; if the Atlas would rather key the founders on 1957,
the evidence strings and the cited source both need changing together.

## Sources

Listed in frontmatter. `european-union.europa.eu` and
`numerique.gouv.fr` were read directly this pass; `iso.org` remains
bot-walled, and `legifrance.gouv.fr`'s JORF text pages are genuinely
bot-walled even with an honest User-Agent (see the caveat above).
