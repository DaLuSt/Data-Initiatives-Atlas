# Ireland — Index

Curated navigation hub for all Ireland-scoped (`country: IE`) entities in
the Atlas. This is a human-maintained page, not a generated one — add a
wikilink here whenever a new IE-scoped entity is judged important enough to
belong on the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[IE]]

> **Sourcing caveat.** Every Irish entity below was compiled from
> search-engine results only: the cited pages were confirmed to exist but
> were **not read**. They carry `verification: search-only`. [[IE-DPC]] is
> the best-sourced of them — its claims rest on the Commission's own
> published decisions.

## Organisations

- [[IE-DPC]] — Data Protection Commission _(**lead supervisory authority**
  under [[EU-GDPR]] Article 56 for much of the technology sector
  established in the Union; only the **third** entity in the Atlas to carry
  `participates-in` [[EU-EDPB]])_
- [[IE-NCSC]] — National Cyber Security Centre _(**will be** the NIS2
  competent authority — contrast [[GB-NCSC]], which explicitly is not)_
- [[IE-CSO]] — Central Statistics Office _(the **sixth** member of
  [[EU-ESS]] in the Atlas)_
- [[IE-TAILTE]] — Tailte Éireann _(⚠ `confidence: low`; mapping, land
  registration and valuation merged into one body)_
- [[IE-NSAI]] — National Standards Authority of Ireland _(⚠ no
  `participates-in` edges asserted — see the entity)_

## Legislation

- [[IE-DPA-2018]] — Data Protection Act 2018 _(a national procedural
  statute doing work in twenty-seven member states, through Article 60)_
- [[IE-NCS-BILL]] — National Cyber Security Bill _(`proposed`; the NIS2
  transposition is **overdue**, deadline 17 October 2024 missed)_

## Platforms

- [[IE-DATA-GOV-IE]] — the national open data portal _(⚠ no custodian
  modelled, like [[NL-DATA-OVERHEID]] and [[ES-DATOS-GOB-ES]])_

---

## Why Ireland, ahead of larger member states

**The one-stop-shop has a centre, and it is Dublin.**

Before this batch the Atlas held **eight** national data protection
authorities and modelled no mechanism connecting any of them. The GDPR's
one-stop-shop — how most consequential enforcement in the Union actually
happens — existed nowhere in the graph.

[[EU-GDPR]] Article 56 makes the authority of the member state where a
controller has its **main EU establishment** the lead authority for its
cross-border processing; Article 60 then requires that authority to submit a
**draft decision** to the other concerned authorities before it binds.
Because so much of the technology sector places its EU headquarters in
Dublin, that concentrates enforcement in [[IE-DPC]].

The worked example is the DPC's **€530 million TikTok decision**, published
by the EDPB as the "Irish Supervisory Authority" decision following an
Article 60 draft.

**Ireland is also the only common-law member state in the Atlas.** [[GB]]
brought common law in, but as a *former* member.

## EU instruments that apply in Ireland

Eighteen, recorded as `applies-in` edges on the instruments themselves:
[[EU-GDPR]], [[EU-NIS2]], [[EU-AI-ACT]], [[EU-DATA-ACT]], [[EU-DGA]],
[[EU-EIDAS]], [[EU-EIDAS2]], [[EU-CER]], [[EU-CYBERSECURITY-ACT]],
[[EU-INSPIRE]], [[EU-ITS-DIRECTIVE]], [[EU-OPEN-DATA-DIRECTIVE]],
[[EU-SDG]], [[EU-INTEROPERABLE-EUROPE-ACT]],
[[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]], [[EU-EHDS]], [[EU-EIF]] and
[[EU-DIGITAL-DECADE]].

[[UN-AARHUS]] is **deliberately excluded**. It is a mixed agreement, and
Ireland's ratification date and terms were not researched — the other six
member states carry the edge on evidence this batch did not gather for
Ireland.

## A transposition that is overdue, not merely pending

Ireland missed the **17 October 2024** NIS2 deadline. [[IE-NCS-BILL]] is
carried as `status: proposed`.

The Atlas holds one other pending cyber instrument, [[GB-CSRB]], and the two
are **not the same kind of thing**: the UK's is a sovereign choice about a
directive that no longer binds it, Ireland's is a member state late on an
obligation. The graph shows them identically; the entities say why they
differ.

## Not modelled

- **Northern Ireland** and the post-Brexit interaction between the two
  jurisdictions.
- **CSIRT-IE**, designated alongside [[IE-NCSC]] by the Bill.
- Ireland's **Open Data Directive transposition** — an S.I. that was not
  identified, joining Belgium, France and Spain on that list.
- The **Freedom of Information Act 2014**.
- The **Law Enforcement Directive** transposition in [[IE-DPA-2018]]'s
  Part 5 — the Directive itself is still not an Atlas entity.
- The **Statistics Act 1993** and [[IE-TAILTE]]'s establishing legislation.
