---
id: NL-WDO
type: act
name: Wet digitale overheid
name_en: "Digital Government Act"
alternative_names:
  - Wdo
  - Digital Government Act
description: >
  Dutch digital government act, in force in phases from 1 July 2023. It
  requires public service providers to determine the assurance level
  required for access to each digital service, mandates digital
  accessibility, and gives statutory force to designated open standards.

level: national
country: NL
region: null

status: active
rank: ordinary
confidence: medium
coverage: medium
verification: primary-source

start_date: 2023-07-01
end_date: null
last_verified: "2026-10-10"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
  - NL-LOGIUS
related_entities:
  - NL-PAS-TOE-OF-LEG-UIT
  - NL-GDI
relationships:
  - type: influences
    target: NL-PAS-TOE-OF-LEG-UIT
    source: fact
    evidence: "Confirmed by reading the Wdo's own statutory text at wetten.overheid.nl directly (2026-08-27, BWBR0048156): Article 3 mandates compliance with designated standards for electronic communication, requiring 'a procedure accessible to everyone' and that specifications be 'publicly accessible and freely usable' and remain 'permanently available at reasonable cost' — the open-standards criteria the comply-or-explain regime is built on. The statutory text read does not itself name HTTPS; that specific detail is now confirmed by a genuine direct read (2026-09-27) of digitaleoverheid.nl's own Wdo overview page, via its WordPress REST API (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=wet-digitale-overheid-wdo — the workaround documented in discovery/unresolved.md row #216, the rendered page itself remaining bot-walled): 'Sinds 1 juli 2023 ... is bijvoorbeeld de HTTPS-standaard wettelijk verplicht voor publiek toegankelijke overheidswebsites en webapplicaties' (since 1 July 2023, the HTTPS standard is legally mandatory for publicly accessible government websites and web applications), with the HSTS standard additionally required and HTTPS configuration required to meet the NCSC's TLS and web-application guidelines."
    confidence: high
    valid_from: 2023-07-01
    valid_until: null
  - type: related-to
    target: EU-EIDAS
    source: fact
    evidence: "ANSWERS discovery/unresolved.md row #36 (read directly 2026-10-10, Kamerstuk 34972 nr. AE, the letter of the Staatssecretaris van Binnenlandse Zaken en Koninkrijksrelaties of 3 March 2023 to the Eerste Kamer, on zoek.officielebekendmakingen.nl). It states that the eIDAS Regulation applies to the Netherlands whether or not the Wdo enters into force: 'Indien de beide wetsvoorstellen niet in werking treden, dan blijft de situatie dat de verplichtingen uit de huidige eIDAS-verordening voor Nederland blijven gelden en dus ook Nederlanders met erkende inlogmiddelen (zowel publieke als private) uit andere lidstaten bij de Nederlandse overheid moeten kunnen inloggen. Met de Wet digitale overheid en de bijhorende novelle hebben wij in Nederland de mogelijkheid om private middelen toe te laten op grond van onder meer de novelle-eisen.' So the Wdo does not transpose the regulation (a regulation is directly applicable and nothing here says otherwise); it sits beside its cross-border acceptance obligation and lets the Netherlands admit private login means that meet Dutch requirements. Typed `related-to`, not `implements-requirement-from`. The Eerste Kamer committee report (nr. AF, 17 March 2023) records the same scope debate: the Landsadvocaat's advice is that eIDAS is in principle limited to cross-border authentication."
    confidence: medium
    valid_from: 2023-07-01
    valid_until: null

sources:
  - title: "Kamerstuk 34972, nr. AE — Wet digitale overheid: brief van de Staatssecretaris (juridische analyses van de Landsadvocaat), 3 maart 2023"
    url: "https://zoek.officielebekendmakingen.nl/kst-34972-AE.html"
    publisher: "Overheid.nl — Officiële bekendmakingen (Eerste Kamer)"
    accessed: "2026-10-10"
  - title: "Kamerstuk 34972, nr. AF — Wet digitale overheid: verslag van een schriftelijk overleg, 17 maart 2023"
    url: "https://zoek.officielebekendmakingen.nl/kst-34972-AF.html"
    publisher: "Overheid.nl — Officiële bekendmakingen (Eerste Kamer)"
    accessed: "2026-10-10"
  - title: "Staatsblad 2023, 160 (inwerkingtredingsbesluit)"
    url: "https://zoek.officielebekendmakingen.nl/stb-2023-160.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
    accessed: "2026-08-27"
  - title: "Wet digitale overheid — officiële wettekst (BWBR0048156)"
    url: "https://wetten.overheid.nl/BWBR0048156/2025-11-11"
    publisher: "Overheid.nl — wetten.overheid.nl"
    accessed: "2026-08-27"
  - title: "Wet Digitale Overheid"
    url: "https://www.noraonline.nl/wiki/Wet_Digitale_Overheid"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
  - title: "Wet digitale overheid — Wikipedia"
    url: "https://nl.wikipedia.org/wiki/Wet_digitale_overheid"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "Wet digitale overheid (Wdo)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/wetgeving/wet-digitale-overheid-wdo/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-27"
    note: "The rendered page is genuinely bot-walled (JavaScript verification challenge). Read directly via the site's own WordPress REST API instead (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=wet-digitale-overheid-wdo) — the workaround documented in discovery/unresolved.md row #216."
  - title: "Veelgestelde vragen over de inwerkingtreding van de Wdo"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/wetgeving/wet-digitale-overheid/veelgestelde-vragen-over-de-inwerkingtreding-van-de-wdo/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-27"
    note: "Read directly via the WordPress REST API workaround (?slug=veelgestelde-vragen-over-de-inwerkingtreding-van-de-wdo). A long FAQ (32 questions) mostly about the Stelsel Toegang access system's mechanics, not the Wdo's own legal text; used sparingly here."
---

# Wet digitale overheid (Wdo)

> **Verified 2026-08-27, sources rebuilt.** Staatsblad 2023, 160 (the
> commencement decree) was read directly, closing the previous "not read"
> gap. Two of the four originally-cited digitaleoverheid.nl pages proved
> genuinely and repeatedly bot-walled — a JavaScript verification challenge,
> not real content, on every attempt — so two alternate primary/official
> sources (the Wdo's own statutory text, and NORA's wiki) were found and
> read directly to reach a genuine majority. `verification` moves from
> `search-only` to `primary-source`.
>
> **Closed 2026-09-27**: both digitaleoverheid.nl pages, genuinely
> bot-walled to direct fetch, are now read directly via the site's own
> WordPress REST API (the workaround documented in
> `discovery/unresolved.md` row #216) — 6 of 6 sources now read directly.
> The HTTPS/HSTS claim, previously carried as unconfirmed, is now
> confirmed by a genuine direct read (`confidence` raised to `high` on
> that edge). New facts: the Wdo is a *kaderwet* (framework law); the RDI
> (Rijksinspectie Digitale Infrastructuur) is the designated supervisor
> for authentication/authorisation services, with Logius supervising
> information security; and the transition period for lower-assurance
> logins was extended three years, to 1 July 2028.

## Description

The Wdo gives legal substance to the intention of a digitally functioning
(semi-)government. Confirmed by reading Staatsblad 2023, 160 directly: it
entered into force **in phases**. Articles 28b, 29 and 30 (the legal basis
for digital accessibility requirements) took effect the day after
publication (11 May 2023); most substantive provisions — the trust-level
classification system, the DigiD identification system, and the duty on
BZK to establish digital facilities — took effect on **1 July 2023**, which
`start_date` records; a further tranche (the access system and
authorisation procedures) was expected around year-end 2023 via a second
decree not itself read this pass.

Obligations confirmed from the Wdo's own statutory text (wetten.overheid.nl,
read directly) and NORA's wiki (read directly):

- **Assurance levels.** Article 6 establishes a tiered system — low,
  substantial, high (betrouwbaarheidsniveau) — under which public bodies
  must determine and publish which level each digital service requires, and
  may permit lower-assurance credentials only temporarily during a
  transition.
- **Accessibility.** Confirmed by Staatsblad 2023, 160 as one of the
  provisions given statutory basis; the specific WCAG 2.1 reference was not
  re-confirmed by any page read this pass and is carried over from the
  prior text.
- **Open standards.** Article 3, read directly, mandates designated
  standards for electronic communication meeting open-standard criteria
  (accessible procedure, freely usable, permanently available at reasonable
  cost). **Confirmed 2026-09-27**: digitaleoverheid.nl's own page, read
  directly via the WordPress REST API workaround, states that since
  1 July 2023 the HTTPS standard has been legally mandatory for publicly
  accessible government websites and web applications, with HSTS
  additionally required and HTTPS configuration required to meet the
  NCSC's TLS and web-application guidelines.
- **Stelsel Toegang**, the access system enabling service providers to
  connect to all recognised login methods — named in the Wdo's own text
  (wetten.overheid.nl) as part of Chapter 5 on data protection and access.

The Wdo is the point where the Dutch open-standards regime acquires
statutory teeth: [[NL-PAS-TOE-OF-LEG-UIT]] operates on an
apply-or-explain basis, while the Wdo makes specified standards
outright mandatory. That relationship is recorded as `influences`; whether a
more precise relationship type is warranted is worth revisiting.

The Wdo also connects to the identity and access services within
[[NL-GDI]] operated by [[NL-LOGIUS]], though the specific services covered
have not been established.

## A kaderwet, its supervisors, and a three-year extension — read directly 2026-09-27

digitaleoverheid.nl's own Wdo overview page, read directly via the
WordPress REST API workaround, adds three facts not previously carried:

- **The Wdo is a *kaderwet*** (framework law): it regulates general
  principles, responsibilities and procedures rather than detailed rules,
  by the page's own description, so that flexibility for new developments
  is possible.
- **Supervision is split.** The Rijksinspectie Digitale Infrastructuur
  (RDI) is designated supervisor for authentication and authorisation
  services and their compliance with the Wdo and its subordinate
  regulations; [[NL-LOGIUS]] supervises information security separately.
  Neither body is a separate Atlas entity; both are named here in prose.
- **The low-assurance transition period was extended three years**, from
  1 July 2025 to **1 July 2028**, giving public bodies more time to make
  substantial- and high-assurance login methods more widely available
  before lower-assurance methods are phased out. As of the source's own
  writing, only DigiD is a recognised public login method under the new
  Stelsel Toegang access system; no private login methods have yet been
  recognised.

## Classification

Dutch national legislation: `region` is `null` rather than `EU`.

**The question is answered, 2026-10-10.** Batch 8 left the Wdo without a relationship to [[EU-EIDAS]]
because no source said how they relate. The Eerste Kamer dossier does: the Staatssecretaris's letter of
3 March 2023 (Kamerstuk 34972 nr. AE, read directly) says the obligations of the eIDAS Regulation apply to
the Netherlands whether or not the Wdo and its novelle enter into force, and that the Wdo gives the
Netherlands the possibility to admit private login means that meet Dutch requirements. So the Wdo is **not**
a transposition of 910/2014 (a regulation applies directly, and nothing read says otherwise); it is
`related-to` it, and the edge is recorded on this entity with that quotation. [[EU-EIDAS2]] stays ruled out on
dates (the Wdo, July 2023, predates it, May 2024). `region` stays `null`: this is Dutch national legislation.

The same dossier records a legal debate worth knowing: the Landsadvocaat's analysis (summarised in nr. AE and
discussed in nr. AF, 17 March 2023) is that the Regulation is in principle limited to cross-border
authentication, but that the notion of a cross-border situation is read so widely (dual nationals, a Dutch
citizen working in Belgium with a Belgian means) that applying it broadly is the practical course.

## Relationships

- Influences [[NL-PAS-TOE-OF-LEG-UIT]] by giving statutory force to
  designated open standards.
- Relates to [[NL-GDI]] and [[NL-LOGIUS]] through the Stelsel Toegang.
- `related-to` [[EU-EIDAS]]: not a transposition; sits beside the Regulation's cross-border acceptance
  obligation (Kamerstuk 34972 nr. AE, read directly 2026-10-10).

## Sources

Listed in frontmatter. **6 of 6 now read directly.** Staatsblad 2023, 160,
the Wdo's own statutory text, NORA's wiki and Wikipedia (earlier passes);
and, closing this file 2026-09-27, both digitaleoverheid.nl pages via the
site's own WordPress REST API
(`www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=<slug>`) — the
workaround documented in `discovery/unresolved.md` row #216. The rendered
HTML at both URLs remains genuinely bot-walled.
