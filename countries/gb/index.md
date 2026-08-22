# United Kingdom — Index

Curated navigation hub for all UK-scoped (`country: GB`) entities in the
Atlas. This is a human-maintained page, not a generated one — add a wikilink
here whenever a new GB-scoped entity is judged important enough to belong on
the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[GB]]

> **Re-verified 2026-08-22.** Every UK entity below, and [[EU-UK-ADEQUACY]],
> has now been re-verified against primary sources read directly and
> carries `verification: primary-source`. A handful of individual claims
> could not be independently re-confirmed this pass — the [[GB-UKSA]]/
> [[GB-ONS]] UN-CES seat-holder ambiguity, and [[GB]]'s own Council of
> Europe membership (`coe.int` is bot-walled) — and are recorded as such
> in their evidence rather than silently dropped or re-asserted.

**The ID scope is `GB`, not `UK`** — `metadata/schema.json` requires an
ISO 3166-1 alpha-2 code, and `GB` is the alpha-2 assignment for the United
Kingdom. See [[GB]].

## Organisations

- [[GB-GDS]] — Government Digital Service _(the digital centre of
  government; sets direction **and** runs the platforms)_
  - [[GB-DCMS]] — its department since 21 Jul 2026 _(⚠ `confidence: low`;
    trade press only)_
  - [[GB-DSIT]] — its department until 21 Jul 2026 _(**abolished**; the
    Atlas's first entity to stop existing)_
- [[GB-ICO]] — Information Commissioner's Office _(⚠ [[GB-DUAA]] s.117
  replaces it with an **Information Commission**; completion unverified)_
- [[GB-ONS]] — Office for National Statistics _(`participates-in`
  [[UN-CES]] — the **only** statistical office in the Atlas that reaches
  the international layer without [[EU-ESS]])_
- [[GB-NCSC]] — National Cyber Security Centre _(technical authority,
  explicitly **not** the NIS competent authority; `produces` [[GB-CAF]])_
- [[GB-UKSA]] — UK Statistics Authority _([[GB-ONS]] is its executive
  office; ⚠ did **not** settle which body holds the CES seat)_
- [[GB-BSI]] — British Standards Institution _(**the most connective UK
  entity**: [[INTL-ISO]], [[INTL-IEC]], [[EU-CEN]], [[EU-CENELEC]],
  [[EU-ETSI]])_
- [[GB-OS]] — Ordnance Survey _(`participates-in` [[UN-GGIM]]; closes the
  UK's [[DOMAIN-GEOSPATIAL]] gap — but maps **Great Britain**, not the UK)_
- [[GB-OFCOM]] — Ofcom _(NIS competent authority for digital
  infrastructure, alongside [[GB-ICO]] for digital service providers)_

## Frameworks and strategies

- [[GB-CAF]] — Cyber Assessment Framework _(`aligned-with`
  [[INTL-ISO-IEC-27001]]; the UK counterpart to [[NL-BIO]],
  [[DE-IT-GRUNDSCHUTZ]] and [[ES-ENS]])_
- [[GB-GEOSPATIAL-STRATEGY]] — UK Geospatial Strategy 2030 _(⚠
  `confidence: low`; no owner establishable after the Geospatial Commission
  was merged into [[GB-GDS]])_

## Legislation

- [[GB-UK-GDPR]] — UK GDPR _(`derived-from` [[EU-GDPR]] — **assimilated
  law**, not a transposition)_
- [[GB-DPA-2018]] — Data Protection Act 2018 _(⚠ no legislation.gov.uk
  citation found)_
- [[GB-DUAA]] — Data (Use and Access) Act 2025 _(amends **both** of the
  above; main provisions in force 5 Feb 2026)_
- [[GB-NIS-REGULATIONS]] — NIS Regulations 2018 _(`implements-requirement-from`
  [[EU-NIS]] — a transposition made **while a member state**, still in
  force)_
- [[GB-CSRB]] — Cyber Security and Resilience Bill _(`proposed`; the UK's
  answer to the problem [[EU-NIS2]] addresses, and not a transposition of
  it)_

## Platforms

- [[GB-ONE-LOGIN]] — GOV.UK One Login _(single sign-in, identity and the
  GOV.UK Wallet; **no eIDAS relationship in either direction**)_
- [[GB-DATA-GOV-UK]] — national open data portal _(launched 2010 — the
  oldest in the Atlas, and nine years before
  [[EU-OPEN-DATA-DIRECTIVE]])_

---

## EU instruments that apply in the United Kingdom

**None is recorded, and that is the structural point of this batch.**

Every other country page in the Atlas ends with a list of EU instruments
carrying `applies-in` to that country. The UK is not an EU member state, so
there is no such list, and **no EU instrument carries `applies-in` to
[[GB]]**. The anchor is reached instead by the UK's *own* instruments, which
do — the same treatment [[NL-BIO]] carries for the Netherlands.

The UK reaches the European layer by three edges, none of them `applies-in`
from an EU instrument:

- [[GB-UK-GDPR]] **`derived-from`** [[EU-GDPR]] — assimilated law: the
  Regulation's own text, domesticated and now diverging.
- [[GB-NIS-REGULATIONS]] **`implements-requirement-from`** [[EU-NIS]] — a
  2018 transposition, made while the UK was a member state, still in force
  as assimilated law, and never repealed by [[EU-NIS2]] because the UK was
  outside its scope by then.
- [[EU-UK-ADEQUACY]] **`references`** [[GB-UK-GDPR]] and [[GB-DUAA]] — the
  only edge in the Atlas running *from* the EU *to* a non-member state.

An empty cell in the Compare view's UK column is **not** a claim that an EU
instrument does not reach the UK. Some do — through the Trade and
Cooperation Agreement, through adequacy, or through extraterritorial scope.
The Atlas has established none of that.

## The EU adequacy decisions

[[EU-UK-ADEQUACY]] — renewed **19 December 2025**, expiring **27 December
2031** under a sunset clause. Filed as an **EU** entity, because the
decisions are Commission acts, and it carries the only edge in the Atlas
running *from* the European Union *to* a non-member state's instrument.

## Standards — the link Brexit did not cut

[[GB-BSI]] `participates-in` [[INTL-ISO]], [[INTL-IEC]], [[EU-CEN]],
[[EU-CENELEC]] and [[EU-ETSI]].

**CEN and CENELEC are not EU institutions** — their members are national
standards bodies, not member states — so BSI's membership survived the UK's
departure. The UK therefore takes no `applies-in` edge from any EU
instrument while sitting inside three European standardisation bodies. Both
facts are true and neither is visible without the other.

## Intelligence and security services

Added with the intelligence-services batch. The UK **avowed its services one
at a time**, rather than passing a single organic act:

| Year | Act | Service |
|---|---|---|
| 1989 | [[GB-SSA-1989]] | [[GB-MI5]] — domestic, Home Office |
| 1994 | [[GB-ISA-1994]] | [[GB-SIS]] and [[GB-GCHQ]] — both Foreign Office |

The 1994 pairing follows the **ministerial line, not the discipline**: human
and signals intelligence share an act because they share a minister.

Cutting across all three: [[GB-IPA-2016]], which governs **powers** rather
than bodies — the same choice France made in
[[FR-LOI-RENSEIGNEMENT-2015]], but layered on top of existing agency acts
rather than filling their absence.

Oversight:

- [[GB-ISC]] — parliamentary, under [[GB-JSA-2013]]. The 1994 act had
  already created an ISC covering *expenditure, administration and policy*;
  2013 re-founded it and added **operations**. One word, and the committee
  moved from scrutinising how the agencies are run to what they do.
- [[GB-IPCO]] — independent, under [[GB-IPA-2016]]. It merged three
  predecessor commissioner offices and oversees **over 600 public
  authorities**, far beyond the three agencies.

### The UK legislates its services *into* data protection law

Unlike every other country in this batch, the UK did not leave the
national-security carve-out empty. **Part 4 of [[GB-DPA-2018]] is a data
protection regime built for the intelligence services** — [[GB-MI5]],
[[GB-SIS]] and [[GB-GCHQ]] — separate from [[GB-UK-GDPR]], with
[[GB-ICO]] as the regulator of the act containing it. Belgium reaches a
comparable result through [[BE-GDPR-WET]], by a different route.

### [[GB-NCSC]] is part of [[GB-GCHQ]]

Established October 2016 from CESG — GCHQ's own information security arm —
plus CPNI, CERT-UK and the Centre for Cyber Assessment.

The body that publishes [[GB-CAF]] and advises British industry is a
component of a **signals intelligence agency**. Only Spain is arranged the
same way ([[ES-CCN]] inside [[ES-CNI]]); [[DE-BSI]], [[FR-ANSSI]] and
[[BE-CCB]] all sit outside their countries' intelligence structures.

### Not an intelligence service, and not modelled

**Defence Intelligence** has no avowal act and was not researched, so the UK
appears here with three services where France has four and Poland four.

## Not modelled

- **The Office for Statistics Regulation** — [[GB-ONS]]'s regulator.
- **Ordnance Survey of Northern Ireland**, leaving a UK-wide geospatial gap:
  [[GB-OS]] maps Great Britain only.
- **The sectoral NIS competent authorities** — energy, transport, health and
  drinking water — although [[GB-OFCOM]] and [[GB-ICO]] are now both
  modelled.
- **DBIST** and the **Cabinet Office** — two of the three destinations of
  [[GB-DSIT]]'s functions.
- **The Re-use of Public Sector Information Regulations** — whether any UK
  open data instrument survives as assimilated law was not researched, so
  [[GB-DATA-GOV-UK]] still connects to [[EU-OPEN-DATA-DIRECTIVE]] not at all.
- **Any British Standard**, so [[GB-BSI]] participates in five standards
  bodies while maintaining nothing the Atlas holds.
