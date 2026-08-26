---
id: BE-ADIV
type: organisation
name: Algemene Dienst Inlichting en Veiligheid
alternative_names:
  - ADIV
  - SGRS
  - Service Général du Renseignement et de la Sécurité
  - General Intelligence and Security Service
description: >
  Belgium's military intelligence and security service, operating under the
  authority of the Minister of Defence. Its missions are described in the
  organic law of 30 November 1998 on the intelligence and security services,
  the same act that governs the civilian VSSE, and it is subject to
  oversight by the Standing Intelligence Agencies Review Committee.

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
  - BE-VSSE
  - BE-COMITE-I
relationships:
  - type: governed-by
    target: BE-GDPR-WET
    source: fact
    evidence: "The law of 30 July 2018 on the protection of natural persons with regard to the processing of personal data contains a subtitle on the protection of natural persons with regard to the processing of personal data by the intelligence and security services; where a request or complaint concerning processing covered by Title 3 reaches the supervisory authority, that authority first turns to the Vast Comité I to carry out the necessary verifications (etaamb.openjustice.be 'Wet van 30/07/2018'; jurion.fanc.fgov.be 'GDPR-wet, Ondertitel 1 — verwerking van persoonsgegevens door de inlichtingen- en veiligheidsdiensten'; gegevensbeschermingsautoriteit.be). Not independently re-confirmed this pass — the two sources read (sgrs.be, etaamb wet-van-30-november-1998) are about the 1998 organic act, not the 2018 data protection act."
    confidence: medium
    valid_from: 2018-09-05
    valid_until: null
  - type: governed-by
    target: BE-WIV-1998
    source: fact
    evidence: "Confirmed by reading sgrs.be and the act's own text at etaamb.openjustice.be directly (2026-08-26). SGRS's own missions page: 'de Organieke Wet van 30 november 1998 tot regeling van de inlichtingen- en veiligheidsdiensten' governs all its missions. The act's own Article 2, §1 names the ADIV, alongside the VSSE, as one of the 'twee inlichtingen- en veiligheidsdiensten van het Rijk', under the Minister of Defence."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Onze Missies"
    url: "https://www.sgrs.be/nl/over-ons/onze-missies/"
    publisher: "Algemene Dienst Inlichting en Veiligheid (ADIV/SGRS)"
    accessed: "2026-08-26"
  - title: "De Algemene Dienst Inlichting en Veiligheid (ADIV)"
    url: "https://vsse.be/nl/de-algemene-dienst-inlichting-en-veiligheid-adiv"
    publisher: "Veiligheid van de Staat (VSSE)"
  - title: "Wet van 30/11/1998 houdende regeling van de inlichtingen- en veiligheidsdienst"
    url: "https://etaamb.openjustice.be/nl/wet-van-30-november-1998_n1998007272.html"
    publisher: "eTaamb / OpenJustice (Belgisch Staatsblad)"
    accessed: "2026-08-26"
---

# Algemene Dienst Inlichting en Veiligheid / Service Général du Renseignement et de la Sécurité (ADIV / SGRS)

> **Verified 2026-08-26.** Two of three sources were read directly — SGRS's
> own missions page and the organic act's own text — both confirming the
> `governed-by` [[BE-WIV-1998]] edge directly. The `governed-by`
> [[BE-GDPR-WET]] edge was not independently re-confirmed this pass.
> `verification: primary-source`.

## Description

The ADIV is the **military** counterpart to [[BE-VSSE]], under the authority
of the Minister of Defence. Both services are constituted by the same
organic act, [[BE-WIV-1998]], confirmed by reading its Article 2, §1
directly.

## One service, two names, and why both are in the frontmatter

ADIV (Dutch: *Algemene Dienst Inlichting en Veiligheid*) and SGRS (French:
*Service Général du Renseignement et de la Sécurité*) are the same body. The
service runs its own site under `sgrs.be` while [[BE-VSSE]] describes it as
the ADIV.

The Atlas files it under the Dutch name with the French one as an
`alternative_name`, matching the convention already used for the other
Belgian entities ([[BE-KSZ]], [[BE-APD]]). **That is a filing convention and
nothing more.** In a federal bilingual state the choice of headword is not
neutral, and a reader should not infer any precedence from it. Search on
either name resolves to this entity.

## Relationships

- `governed-by` [[BE-WIV-1998]] and [[BE-GDPR-WET]] — the latter for the
  processing of personal data, under the subtitle covering the intelligence
  and security services. See [[BE-VSSE]] for how that regime routes
  verification through [[BE-COMITE-I]].

## Not modelled

- The ADIV's **CERT and cyber-defence functions**, and how they relate to
  [[BE-CCB]], the Centre for Cybersecurity Belgium. A relationship between
  the military intelligence service and the national cyber-security centre
  is plausible in both directions and **is not asserted**, because no source
  read states one.

## Sources

Two of three read directly this pass — SGRS's own missions page and the
1998 organic act's own text. VSSE's page on the ADIV was not re-fetched.
