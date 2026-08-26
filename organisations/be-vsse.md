---
id: BE-VSSE
type: organisation
name: Veiligheid van de Staat
alternative_names:
  - VSSE
  - Sûreté de l'État
  - State Security Service
description: >
  Belgium's civilian intelligence and security service, a department of the
  Federal Public Service Justice operating under the authority of the
  Minister of Justice. Its statutory tasks are set by the organic law of
  30 November 1998 on the intelligence and security services, and it is
  subject to democratic oversight by the Standing Intelligence Agencies
  Review Committee (Comité I).

level: national
country: BE
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

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - BE-WIV-1998
  - BE-GDPR-WET
  - BE-ADIV
  - BE-COMITE-I
relationships:
  - type: governed-by
    target: BE-GDPR-WET
    source: fact
    evidence: "The law of 30 July 2018 on the protection of natural persons with regard to the processing of personal data contains a subtitle on the protection of natural persons with regard to the processing of personal data by the intelligence and security services; where a request or complaint concerning processing covered by Title 3 reaches the supervisory authority, that authority first turns to the Vast Comité I to carry out the necessary verifications (etaamb.openjustice.be 'Wet van 30/07/2018'; jurion.fanc.fgov.be 'GDPR-wet, Ondertitel 1 — verwerking van persoonsgegevens door de inlichtingen- en veiligheidsdiensten'; gegevensbeschermingsautoriteit.be). Not independently re-confirmed this pass — the two sources read (vsse.be, etaamb wet-van-30-november-1998) are about the 1998 organic act, not the 2018 data protection act."
    confidence: medium
    valid_from: 2018-09-05
    valid_until: null
  - type: governed-by
    target: BE-WIV-1998
    source: fact
    evidence: "Confirmed by reading vsse.be and the act's own text at etaamb.openjustice.be directly (2026-08-26). VSSE's own legal-framework page confirms the 1998 law defines its task of gathering information about threats to state security; the act's own Article 2, §1 names the VSSE, under the Minister of Justice, as one of the 'twee inlichtingen- en veiligheidsdiensten van het Rijk' alongside the ADIV."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Het wettelijk kader"
    url: "https://vsse.be/nl/het-wettelijk-kader"
    publisher: "Veiligheid van de Staat (VSSE)"
    accessed: "2026-08-26"
  - title: "Wet van 30/11/1998 houdende regeling van de inlichtingen- en veiligheidsdienst"
    url: "https://etaamb.openjustice.be/nl/wet-van-30-november-1998_n1998007272.html"
    publisher: "eTaamb / OpenJustice (Belgisch Staatsblad)"
    accessed: "2026-08-26"
  - title: "Dienst voor de Veiligheid van de Staat"
    url: "https://nl.wikipedia.org/wiki/Dienst_voor_de_Veiligheid_van_de_Staat"
    publisher: "Wikipedia"
---

# Veiligheid van de Staat / Sûreté de l'État (VSSE)

> **Verified 2026-08-26.** Two of three sources were read directly —
> VSSE's own legal-framework page and the organic act's own text — both
> confirming the `governed-by` [[BE-WIV-1998]] edge directly. The
> `governed-by` [[BE-GDPR-WET]] edge was not independently re-confirmed
> this pass. `verification: primary-source`.

## Description

The VSSE is Belgium's **only civilian** intelligence service — the sources
put it exactly that way — and is a department of the Federal Public Service
Justice, under the authority of the Minister of Justice. Confirmed by
reading the 1998 organic act's own Article 2, §1 directly: it names the
VSSE, under the Minister of Justice. Its military counterpart is
[[BE-ADIV]], under the Minister of Defence.

## A service inside a ministry, not beside one

The Belgian arrangement differs from every other in this batch. The VSSE is
not an agency with its own legal personality attached to a ministry — as
[[ES-CNI]] is to Spanish Defence, or [[DE-BFV]] to [[DE-BMI]] — it is a
**department of** the FPS Justice.

**No `part-of` edge is asserted** even so, because the Atlas does not hold
an entity for the Federal Public Service Justice. [[BE-BOSA]] is the FPS the
Atlas has, and it is a different one.

## One act for both services

[[BE-WIV-1998]] prescribes the statutory duties of **both** the VSSE and
[[BE-ADIV]] — the same single-organic-act pattern as the Netherlands
([[NL-WIV-2017]]), and unlike Germany's three acts or the UK's two.

## Belgium legislates intelligence data protection, and routes it to Comité I

[[BE-GDPR-WET]], the act of 30 July 2018, carries a dedicated subtitle on
the processing of personal data **by the intelligence and security
services**. Belgium did not leave the carve-out empty.

The enforcement route is the distinctive part. Where a request or complaint
about that processing reaches the supervisory authority, the authority
**first turns to [[BE-COMITE-I]]** to carry out the necessary verifications,
and informs it of violations by the services. [[BE-APD]] — the Belgian data
protection authority, already an Atlas entity — does not inspect the
services itself.

The UK reaches a comparable destination by the opposite arrangement: Part 4
of [[GB-DPA-2018]] covers [[GB-MI5]], [[GB-SIS]] and [[GB-GCHQ]] while
leaving [[GB-ICO]] as the regulator, rather than handing verification to
[[GB-IPCO]].

## Oversight

[[BE-COMITE-I]] exercises democratic control over the VSSE and [[BE-ADIV]],
reporting to Parliament, under a **separate** statute — the law of
18 July 1991 — rather than under the 1998 organic act. Belgium is the one
country in this batch where the constituting act and the oversight act are
cleanly different instruments **and both are modelled**.

## Not modelled

- **OCAD/OCAM**, the Coordination Unit for Threat Analysis. The sources
  name it as a fusion centre subject to the joint supervision of Comité P
  and Comité I, and record that the 1991 act was amended on 10 July 2006 to
  bring it under that supervision. It is a threat-analysis body rather than
  an intelligence service, and was not researched further.
- **Comité P**, the equivalent oversight committee for the police services.
- The **BIM-commissie** and the 2010 act on specific and exceptional
  intelligence methods.

## Relationships

- `governed-by` [[BE-WIV-1998]] and [[BE-GDPR-WET]].

## Sources

Two of three read directly this pass — VSSE's own legal-framework page and
the 1998 organic act's own text. Wikipedia was not re-fetched.
