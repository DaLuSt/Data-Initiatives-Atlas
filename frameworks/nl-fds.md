---
id: NL-FDS
type: framework
name: Federatief Datastelsel
alternative_names:
  - FDS
  - Afsprakenstelsel Federatief Datastelsel
description: >
  Dutch agreement system (afsprakenstelsel) enabling organisations with a
  public task to share and use data simply and responsibly. It focuses on
  standardisation and uniformity in how data is described and shared across
  domains, so that high-quality data from different sources can be found,
  shared and applied coherently for multiple uses.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-IBDS
  - NL-BASISREGISTRATIES
relationships:
  - type: implements
    target: NL-IBDS
    source: fact
    evidence: "Confirmed 2026-08-21 on noraonline.nl's 'Federatief Datastelsel' wiki page: 'Samen met stakeholders ontwikkelt de IBDS daarom een Federatief Datastelsel (FDS)' — the IBDS develops the FDS together with stakeholders. The Beleidsevaluatie Interbestuurlijke Datastrategie (Panteia, 7 January 2026) traces FDS building blocks and target architecture across the IBDS's implementation programme (Realisatie IBDS), 2022-2024."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "CLOSES A QUESTION OPEN SINCE BATCH 2 (discovery/unresolved.md rows #133 and #138). FDS's own knowledge base, read directly (2026-09-18): its 'Wat is het FDS?' page states plainly, 'Het Federatief Datastelsel (FDS) is zowel de realisatie van het Toekomstbeeld Stelsel van Basisregistraties als de realisatie van de Interbestuurlijke Datastrategie' (the FDS is both the realisation of the Future Vision for the System of Base Registries and the realisation of the Interbestuurlijke Datastrategie) — the same two-parent relationship the IBDS edge above already carries, extended to a second source. Its 'Scope van FDS' page, also read directly, describes the base-registries system as one of several Domain Data Systems (DDS) FDS connects ('Het Stelsel van Basisregistraties kunnen we beschouwen als een samenstel van DDS-en'), with FDS itself positioned as 'het verbindende stelsel van stelsels' (the connecting system of systems) — realising the base registries' own forward roadmap and linking it to other domain systems, not replacing or sitting unrelated beside it."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Interbestuurlijke Datastrategie (IBDS) — Federatief Datastelsel (presentatie, Dag van de Interoperabiliteit)"
    url: "https://www.forumstandaardisatie.nl/sites/default/files/BFS/8-Bijeenkomsten/20241015-Dag-van-de-interoperabiliteit/presentaties/Presentatie-Federatief-Datastelsel-en-resultaten-Mentimeter.pdf"
    publisher: "Forum Standaardisatie"
    accessed: "2026-08-22"
  - title: "Interbestuurlijke Datastrategie (IBDS)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/data/interbestuurlijke-datastrategie/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-22"
  - title: "Federatief Datastelsel"
    url: "https://www.noraonline.nl/wiki/Federatief_Datastelsel"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-22"
  - title: "Beleidsevaluatie Interbestuurlijke Datastrategie — Eindrapport"
    url: "https://open.overheid.nl/documenten/1edd5ed4-98e8-442e-bcd2-f6ec3f27a754/file"
    publisher: "Rijksoverheid (open.overheid.nl)"
    accessed: "2026-08-22"
  - title: "Wat is het FDS?"
    url: "https://federatief.datastelsel.nl/kennisbank/wat-is-het-fds/"
    publisher: "Federatief Datastelsel"
    accessed: "2026-09-18"
  - title: "Scope van FDS"
    url: "https://federatief.datastelsel.nl/kennisbank/scope-van-fds/"
    publisher: "Federatief Datastelsel"
    accessed: "2026-09-18"
---

# Federatief Datastelsel (FDS)

> **Verified 2026-08-20, deepened 2026-08-21.** Every cited source was read
> and confirmed to support what this entity says. `verification:
> primary-source`.
>
> **Closed 2026-09-18** (`discovery/unresolved.md` rows #133 and #138): the
> relationship to [[NL-BASISREGISTRATIES]], open since Batch 2, is sourced
> from FDS's own knowledge base. See "The basisregistraties relationship,
> closed" below.

## Description

The Federatief Datastelsel is an agreement system (afsprakenstelsel) for
organisations carrying out a public task, intended to make it possible for
them to share and use each other's data simply and responsibly. Rather than
centralising data, it is federative: it standardises *how* data is described
and exchanged across domains, so that high-quality data held in different
source systems can be found, shared and applied coherently for multiple
purposes. noraonline.nl's own FDS page confirms this description almost
word for word and confirms FDS is being developed *by* the IBDS, together
with stakeholders — resolving what was previously an unconfirmed
relationship (see below).

## Correction: `status` was `planned`, now `active`

The claim that the OBDO formally established an *Afsprakenstelsel Federatief
Datastelsel* in February 2026 — previously an unconfirmed search result — is
now confirmed directly on digitaleoverheid.nl's IBDS page: *"In februari 2026
heeft het Overheidsbreed Beleidsoverleg Digitale Overheid (OBDO) het
Afsprakenstelsel Federatief Datastelsel vastgesteld. Daarmee zijn
gezamenlijke spelregels vastgelegd voor aanbieders van data"* — the OBDO
adopted the Afsprakenstelsel in February 2026, establishing joint rules for
data providers. The same page states organisations can already consult the
Afsprakenstelsel and get implementation support, while rules for data
*consumers* ("afnemers") are still to follow later in the year — so adoption
is real but not yet complete on the consumer side. `status` moves from
`planned` to `active`; `start_date` stays `null` because the source gives
only the month, not a day, and a day should not be guessed. This also
resolves the corroborating detail from the evaluation report (Panteia,
published 7 January 2026 — necessarily silent on a February event) that the
FDS target architecture was "afgerond" (completed) in 2024 with "eerste
voorzieningen beproefd" (first facilities piloted) that year: the
architecture work preceded, and set up, the formal February 2026 adoption.

The typing of FDS as `framework` rather than `initiative` or `programme`
remains an Atlas judgement. noraonline.nl itself is ambiguous here: its FDS
wiki page is filed under NORA's "initiatief" content type, but the page's
own definition text calls FDS "een afsprakenstelsel" (an agreement system) —
both readings are attested by the same source, so this stays flagged for
review in `discovery/unresolved.md` rather than resolved.

## The basisregistraties relationship, closed — 2026-09-18

Open since Batch 2, and asked again identically when the basisregistraties
batch touched [[NL-BASISREGISTRATIES]] itself without resolving it: does
FDS extend, replace, or sit beside the Stelsel van Basisregistraties?

FDS's own knowledge base, read directly, answers it in the same terms it
already uses for the IBDS relationship above: *"Het Federatief Datastelsel
(FDS) is zowel de realisatie van het Toekomstbeeld Stelsel van
Basisregistraties als de realisatie van de Interbestuurlijke
Datastrategie"* — the FDS is **both** the realisation of the base
registries' own **Future Vision** and the realisation of the IBDS. Its
"Scope van FDS" page adds the mechanism: the base-registries system is
one of several Domain Data Systems (DDS) that FDS connects — *"Het Stelsel
van Basisregistraties kunnen we beschouwen als een samenstel van
DDS-en"* — with FDS itself positioned as *"het verbindende stelsel van
stelsels"* (the connecting system of systems).

Neither "extends," "replaces" nor "sits beside" describes this cleanly:
FDS realises a forward-looking plan the base-registries system's own
documentation already names (a *Toekomstbeeld*, future vision), while
also functioning as a connective layer across it and other domain
systems. The base-registries stelsel continues to exist and is not
superseded — no `supersedes` or `successor` relationship is asserted —
but FDS is its own stated evolution path, not an unrelated parallel
system.

## Relationships

- Implements / realises [[NL-IBDS]] — **now a sourced fact**, not an Atlas
  interpretation: "Samen met stakeholders ontwikkelt de IBDS daarom een
  Federatief Datastelsel (FDS)" (noraonline.nl).
- `implements` [[NL-BASISREGISTRATIES]] — closed 2026-09-18, see above.
- Sits within the [[NL-BZK]] digital-government policy remit.
- Governance decisions taken via the [[NL-OBDO]] (still unconfirmed).

## Sources

Listed in frontmatter. The first four read directly across the 2026-08-20
and 2026-08-21 passes; FDS's own "Wat is het FDS?" and "Scope van FDS"
knowledge-base pages, added and read directly 2026-09-18, close the
basisregistraties relationship question.
