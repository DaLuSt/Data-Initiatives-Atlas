---
id: NL-BELASTINGDIENST
type: organisation
name: Belastingdienst
alternative_names:
  - Dutch Tax Administration
  - Netherlands Tax Administration
description: >
  The Dutch tax administration. Within the system of base registries it
  holds the Basisregistratie Inkomen, determining the authentic income
  datum — the combined income, or where that is unavailable the taxable
  annual wage — for the relevant tax year. It is also a major user of the
  base registry of property values, applying WOZ values to income tax
  through the owner-occupied home allowance, and to corporate income, gift,
  inheritance and landlord levies.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-BRI
  - NL-WOZ
relationships: []

sources:
  - title: "Alles over het geregistreerde inkomen"
    url: "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/geregistreerde_inkomen_en_de_inkomensverklaring/alles_over_geregistreerde_inkomen/alles-over-het-geregistreerde-inkomen"
    publisher: "Belastingdienst"
    accessed: "2026-08-27"
  - title: "BRI — Stelsel van basisregistraties (confirmed bot-walled, not read)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/bri/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Waardering Onroerende Zaken (WOZ) | CBS"
    url: "https://www.cbs.nl/nl-nl/deelnemers-enquetes/decentrale-overheden/vastgoed-overheden/waardering-onroerende-zaken--woz--"
    publisher: "Centraal Bureau voor de Statistiek (CBS)"
    accessed: "2026-08-27"
---

# Belastingdienst

> **Verified 2026-08-27.** Two of three cited pages read directly. The
> Belastingdienst's own page confirms the BRI's authentic-datum logic in its
> own words; digitaleoverheid.nl's BRI page returned a bot-verification
> wall on two attempts and is confirmed genuinely unreadable, not merely
> unread. CBS's own WOZ page, read directly, describes municipalities and
> CBS as WOZ stakeholders but does not itself name the Belastingdienst or
> water boards as users — that detail is not independently re-confirmed
> this pass and is downgraded below.

## Description

The Belastingdienst is the Dutch tax administration. It enters this Atlas
in two distinct roles within the `stelsel van basisregistraties`, and the
distinction is the point of recording it:

1. **As a holder** — it holds [[NL-BRI]], determining the *authentic income
   datum* for each tax year. Confirmed by reading belastingdienst.nl's own
   page directly this pass: registered income is based on the verzamelinkomen
   from a filed return, or on registered wage/benefit/pension income where no
   return was filed.
2. **As a user** — it consumes [[NL-WOZ]] values for income tax (the
   owner-occupied home allowance), corporate income tax, gift and
   inheritance tax, and the landlord levy. **This specific list of taxes is
   not independently re-confirmed this pass**: cbs.nl's own WOZ page, read
   directly, describes municipalities as WOZ data sources and CBS itself as
   a user (for municipal tax-capacity calculations), but does not name the
   Belastingdienst or water boards — the claim here is carried over from a
   prior pass's sourcing, not re-verified against primary text this time.

## Holder and user in one organisation

The stelsel's own documentation describes organisations as occupying
several roles at once — *"an organisation can be a provider, holder, and
user at the same time"*, with [[NL-RDW]] given as the example: it holds the
vehicle register and also receives BRP data.

The Belastingdienst is the same pattern on a different pair of registers,
and it shows why the stelsel is a system rather than a collection.

**The Atlas models only the holder role.** [[NL-BRI]] carries
`maintained-by` pointing here; **no edge records the WOZ consumption**,
because the relationship vocabulary has no term for "is an authorised user
of". `applies-to` would invert the meaning and `depends-on` would overstate
it.

This is the same expressive gap the UN batch hit from a different angle
when it could not record the UNESCO–Commission agreement or the EU voluntary
review. It is logged in `discovery/unresolved.md`, and it matters more here:
**the "afnemer" (user) relationship is arguably the whole point of a base
registry**, and the Atlas cannot express it for any of the ten.

## `coverage: low`

The Belastingdienst is a very large organisation whose tax role is almost
entirely outside this Atlas's scope. Only its base-registry roles are
recorded, and no attempt was made to describe it more broadly.

## Relationships

None asserted from this entity. [[NL-BRI]] carries the `maintained-by` edge
pointing here.

## Sources

Listed in frontmatter, two of three read directly this pass —
belastingdienst.nl's own page and CBS's WOZ page. digitaleoverheid.nl's BRI
page is confirmed genuinely bot-walled in this environment on two separate
attempts, not merely unread.
